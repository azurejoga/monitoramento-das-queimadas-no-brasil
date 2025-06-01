# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 912bbcfd-b560-3b1a-8e97-6598f6ef3063 | -12.5286 | -57.19804 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f22af3d-cc20-3efd-bfc8-4175e76b00bc | -13.09071 | -45.26732 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6daf52ae-77e2-339a-8a1c-85f79c47df60 | -11.43376 | -55.00061 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23859916-9cb5-3b15-b384-9b059c4ce2ed | -11.44923 | -55.01031 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0684f37-3338-3a9b-be1c-61c2cc4b918c | -11.57697 | -47.45577 | 2025-06-01 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abbce029-ab52-3477-8d42-d780eb4bebfe | -12.12753 | -54.59944 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1bc35a8-d091-38b2-ae6a-a8107544a926 | -14.68938 | -45.09177 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 326b366a-8b1d-3681-84bd-dbc565506a0e | -13.91171 | -54.66251 | 2025-06-01 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7945021-ccd7-317d-9bdc-ea10cbc406f4 | -10.00641 | -57.35996 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0591c8cf-1769-34c1-a137-5f7d7a082a5e | -14.02964 | -55.13664 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69ef85e5-3f33-30c9-bb39-3e551a90840c | -10.29184 | -57.14247 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ef74980-92db-372d-bae7-35edbc8598ce | -14.69234 | -45.11908 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a46f48c9-045c-3f9b-8c06-b7493c08e10b | -11.42606 | -55.09299 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a09b1fb9-2d9e-3883-a37e-47721b8710e1 | -11.43266 | -55.00764 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8b51dbd-2740-3a9a-b5b5-6f9741c4ddbb | -14.60365 | -47.96197 | 2025-06-01 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d32c336-dc6e-34e5-a5ee-88c2a720534a | -12.71762 | -54.97411 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 751726d6-d7a9-38cd-81f5-05d48597b335 | -12.52765 | -57.18269 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be2e472f-2291-348e-9300-e3c01fd7f92d | -14.69331 | -45.11039 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0d7181e-5d25-36af-8a4b-527d0c0e8d03 | -14.01522 | -55.11957 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48eaa425-82ac-35f0-8072-5fa0141c58cd | -11.81619 | -58.86454 | 2025-06-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59242f1e-05f9-39be-859b-4ac80ae49c75 | -11.0826 | -54.77134 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9a3a1a4-6faf-350d-bf72-c821024e4d22 | -12.5292 | -57.19435 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eab69c68-3646-37e1-ad81-fe652eddb327 | -13.95179 | -54.4887 | 2025-06-01 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f9da0a3-1f0b-37ec-a077-b7d9226f40c7 | -11.72596 | -56.43417 | 2025-06-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc3a3c0c-87a3-3a1d-b496-8cbaf3eb878d | -10.29872 | -57.14358 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dfed38b-5f42-3014-9556-23b7adad9ca7 | -9.67246 | -49.73264 | 2025-06-01 04:57:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f2fb895-a080-3aa6-97a6-c3352260b62b | -12.12808 | -54.59587 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 770f82e1-f5d0-39e2-a0b2-e72d7157a57c | -14.67402 | -45.12152 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1a584ed-7267-3253-867f-ee9c6da739f1 | -14.68199 | -52.68773 | 2025-06-01 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14887943-28a1-3d73-823d-9dc7189cf811 | -12.02023 | -49.52512 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 621d119c-77d6-355b-a701-9e9f96d8cb65 | -13.10803 | -45.26929 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edbdd654-7469-30db-8c42-810005638718 | -11.44978 | -55.00679 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8333deed-7a80-3f01-830d-b9165e4bf9e5 | -11.07542 | -54.77379 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac7414c5-7927-3749-915b-60a1755961f2 | -10.29613 | -59.0927 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa68ae45-5c0a-35ed-aee6-780780c0b243 | -11.91415 | -54.41965 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8af471de-3cc5-388f-bca6-e01d0f89d75b | -10.65409 | -49.43145 | 2025-06-01 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b036c8b6-2b74-33a4-a401-08ea364ad162 | -10.46565 | -47.94104 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19d0f845-414b-36e1-9d10-a0799c650522 | -10.83049 | -56.96012 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a62a7ee-d766-3696-9658-d585b79d4f60 | -11.43653 | -55.00466 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 503fbf28-caac-3d66-b3d0-0b33bf000e89 | -10.67943 | -57.60471 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87784b87-3655-34a2-833d-cb3723515d53 | -11.57769 | -47.45005 | 2025-06-01 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3b95d80-57f3-3612-b24f-82515c7df1cc | -10.14057 | -52.13577 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57e05f24-215a-32cf-b49c-b601efdd7d1e | -10.29591 | -57.13921 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a7adfa7-1c17-314c-9b7d-5b00acb1b973 | -12.08305 | -54.57769 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c024c91e-6dbc-39ff-a4cc-5e1768581900 | -11.83013 | -51.27341 | 2025-06-01 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58bfc117-7a7e-3a67-8066-5e1939b64a52 | -9.73962 | -57.87395 | 2025-06-01 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6902673e-06ca-364a-8b26-c21f51f4f05b | -11.07265 | -54.76974 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9004a711-ce0d-3666-8e0b-dc365fd2fa9e | -14.69535 | -45.09229 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d55efa12-c0eb-371c-954a-ca200ae6b780 | -14.69282 | -45.11481 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5cda4bb-97ae-3882-ab8f-1a6bc406ed68 | -11.43321 | -55.00412 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db14d1d3-83e7-31b2-8527-cd580aa214a3 | -13.10261 | -45.27147 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd893cbb-a5f4-30e4-aa89-b8c2bdac3f42 | -10.65469 | -49.42954 | 2025-06-01 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3154386f-dbb0-380a-8a06-f7be97642de6 | -14.60567 | -47.96282 | 2025-06-01 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 431d485a-0fe6-3721-835c-408f696fbda7 | -11.43708 | -55.00115 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d9e4bf1-e6f2-34a4-ab30-d282ef997832 | -11.41999 | -55.08841 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30794550-5558-36a6-82e5-d35f3e74015f | -11.90124 | -54.78977 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f37791e-9a0b-345c-ab6c-1c0f2bbe527a | -12.12529 | -54.59177 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1799f676-d602-3907-bd24-8f252db10292 | -10.47363 | -47.95207 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 91cfdab1-c40e-3ebe-83f8-44621a178c1f | -12.52886 | -57.17529 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e53d27ff-6a44-3e97-abd8-37770f0e48bf | -11.42275 | -55.09245 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c776bd66-0e25-314a-855c-a173ea6d8f75 | -13.09136 | -52.04565 | 2025-06-01 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 410945ed-5a72-3cd0-a586-12b8d9d779a8 | -14.66758 | -45.12535 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d89fee2b-ec94-3ecf-bb22-bf377236aabc | -10.13995 | -52.13985 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fddcb90-75bf-3fb0-851a-02fd8a7610b6 | -10.73094 | -49.28261 | 2025-06-01 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55d1c9df-8020-35c7-bfe8-8cf64e282067 | -14.68262 | -52.68335 | 2025-06-01 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e32d91d3-8165-38bc-8f2c-014504508e6d | -10.82273 | -56.94359 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cf8d1a6-7d99-392e-883d-b3e7c725f51c | -13.95516 | -54.48923 | 2025-06-01 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2b58589-c427-326c-9dce-f30e3e423b0a | -10.82831 | -56.95213 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1a1899b-b3a7-37bf-9d89-0cbfb5a5a486 | -13.10307 | -45.26738 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0eba7d2-c87e-384a-822e-395ac438ef0f | -11.43598 | -55.00817 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c89fb473-0260-3c82-9511-47fb3e23f924 | -14.68045 | -45.11781 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fdcaeb2-c8c6-33ed-b483-ac22570f4e5b | -14.68639 | -45.11845 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96cd0e61-0bd3-38c9-bfa6-eb592b437cc4 | -9.39134 | -63.43477 | 2025-06-01 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 073e4d6c-4596-3cc3-a5e6-24b479c9fdc9 | -14.80955 | -48.37054 | 2025-06-01 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3805e96e-521b-31e1-8576-b043ba1ed41e | -9.37133 | -64.45496 | 2025-06-01 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 964361a3-a3f8-3af1-ab1f-bcf14fe68d8e | -9.26403 | -56.29863 | 2025-06-01 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f5f7f9-f81b-361e-94bf-3e8b6314599b | -12.09263 | -54.67056 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 343f08fe-380a-3cd6-8855-ad44ce627d9b | -11.71246 | -56.45407 | 2025-06-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8af085bd-dcc0-3611-b5dc-e6fa6905d044 | -11.4437 | -55.00221 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb1e864b-94fa-338d-b5e4-21d1e882287a | -11.07819 | -54.77784 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 090f677c-8bf8-33d0-bca0-e747cf162383 | -13.10175 | -45.27279 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2cacf3c-fb45-38c8-9480-95d5ea3ce682 | -12.71817 | -54.97055 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20a2dd4c-42f6-3de4-8281-e338261247aa | -10.29529 | -57.14301 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53fd461b-daaa-3274-bb32-8e70b175e4dd | -10.47429 | -47.94719 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6584c68c-8c2b-3d5b-9f40-31a61b85c27f | -10.82709 | -56.95956 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44551617-f3d0-3edd-b045-e0649a8eafa2 | -11.4894 | -54.26876 | 2025-06-01 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7917e57-b3e2-31fa-8d89-fde15c5c8c40 | -14.69383 | -45.10577 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61102d33-42f7-3408-8f29-3fdfcfcbab7d | -10.46963 | -47.94667 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 647c3abc-f37d-3498-822b-fa8babd47240 | -15.89822 | -46.0164 | 2025-06-01 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f4a0db0-aff3-3896-836a-55f00d5bc6b5 | -12.49941 | -55.73874 | 2025-06-01 04:57:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4183f355-4640-3cb9-b111-cd638095dfbb | -12.53164 | -57.17956 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2369ea5-eaeb-3ab9-9622-c92fbd61ed54 | -12.08693 | -54.57466 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 442f6c99-cd92-30d4-9cb4-6dd254751ecc | -11.45374 | -55.0035 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f17e9f14-3d32-3873-bc31-443bf1544e25 | -11.08427 | -54.78242 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74039913-b4c8-3b6f-83d9-853c58c3c81f | -11.89792 | -54.78924 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ebeb619-cb7f-3714-b71b-ea761431a0f3 | -14.01854 | -55.1422 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bd4251c-6bff-30c1-a5cd-f61c4a37ac5f | -12.09004 | -49.48432 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f9bbd98-6f3e-3bfd-85c5-96871171d4b0 | -12.52981 | -57.19065 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccf65aca-2af9-3d4f-830a-62cdfeb4764f | -7.2205 | -43.12352 | 2025-06-01 04:59:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 6921bb73-8eba-39ec-bf24-c115a813bc9d | -22.65252 | -50.66918 | 2025-06-01 04:59:00 | NOAA-20 | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README14.md)
