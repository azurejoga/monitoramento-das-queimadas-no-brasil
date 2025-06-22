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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f282de5d-5c21-35c6-ba65-8be50ab6413f | -11.7938 | -57.23922 | 2025-06-22 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9038e2d-a8df-3e17-ae75-e64b3598439d | -17.7809 | -42.80952 | 2025-06-22 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b027d45-0113-39a9-8d91-4cd1dc5b7804 | -11.42527 | -54.32588 | 2025-06-22 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04a7f682-8b7d-3a32-ab3c-c363f6dff6c7 | -12.65201 | -54.08498 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1342cbdf-cfc6-3fb1-a52f-cb02911deb1b | -17.38688 | -42.65964 | 2025-06-22 04:17:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b3ded9d-b1cd-3fe2-bbfa-f5524d877645 | -10.51275 | -47.57597 | 2025-06-22 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a61efb24-43b1-3f31-90f7-c493af18a66f | -13.23638 | -49.83751 | 2025-06-22 04:17:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e44603ad-602f-3576-b166-118dbb203042 | -11.363 | -55.12758 | 2025-06-22 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7024c83c-0e53-3d9c-8a92-78e652b8da60 | -9.46937 | -57.84028 | 2025-06-22 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f46ab1f4-98af-3e7a-8a23-9b5a33f9f1a6 | -12.47884 | -54.42302 | 2025-06-22 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3706d1d2-d6d1-32ce-8637-4f1d4122d8e2 | -11.62657 | -58.29025 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 800db07b-c59d-3177-912a-11f6ba431eaf | -10.52765 | -53.62396 | 2025-06-22 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a4ae8d8-1c12-3572-9e9a-6dad6bde9905 | -13.26784 | -46.82516 | 2025-06-22 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ecd4307-f185-3018-b6ae-c864fe137fe8 | -10.74596 | -52.51028 | 2025-06-22 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b4753f9-8bd8-3051-8677-b2c64bc1bc56 | -13.74992 | -47.7513 | 2025-06-22 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 105ac849-216a-37d5-928f-3a1e83e473b0 | -17.75434 | -42.89558 | 2025-06-22 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5af7987d-ff59-3fb8-bf77-15ba3acd2c7c | -11.62112 | -58.28894 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2a4db360-bbda-31d2-9999-d755d89a4f0e | -9.46104 | -56.05736 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8d90650a-72c5-3f35-a9c5-fb84d209835d | -11.78607 | -57.24366 | 2025-06-22 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4b61e0b-a7e2-3552-a8a0-fee914fe78a7 | -12.47813 | -54.4267 | 2025-06-22 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a0cfb66f-566f-348e-aa4f-9c524be4f144 | -14.49007 | -46.98462 | 2025-06-22 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e1535a4-75c0-362a-9230-8b3cc9b4d14a | -10.52163 | -53.62639 | 2025-06-22 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 115b32d5-8ac0-3610-8711-6cb6b07b9ffd | -13.04572 | -48.83958 | 2025-06-22 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04d8c4cc-2147-3223-bae1-8bbcd4ae7d1f | -11.61273 | -58.29443 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17f40cb9-03c7-3252-ab33-ac0fa80f4382 | -10.88774 | -56.46628 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c2cf9c5-3c37-37f2-9514-aa29781edeaa | -18.68223 | -40.55587 | 2025-06-22 04:17:00 | NOAA-21 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da3e1a4b-99a3-3f17-9eb5-6e8133b9d0a8 | -13.7992 | -54.29646 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 384c1e03-f3fb-3405-ad8c-bd57ed730bff | -13.24036 | -49.83827 | 2025-06-22 04:17:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35ad3323-1ff9-3cf9-ad22-f55c4d6aa77f | -13.79392 | -54.29539 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18a09202-902c-3a95-b19a-407e9f1d380c | -10.88665 | -56.47158 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e42854e-b816-344c-9d5e-3e04838ff2c3 | -10.12637 | -51.65986 | 2025-06-22 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e10e9c84-17da-3f18-8683-ff3ac1ef9201 | -14.49284 | -46.989 | 2025-06-22 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1912c06c-855b-3343-862b-eb70aae9d8fd | -11.84379 | -57.76013 | 2025-06-22 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53f0b2da-2f85-33d9-8d4f-1c85b7606dc3 | -11.84554 | -57.76165 | 2025-06-22 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b344e1f2-1146-3a3e-ab82-4e95c8a422af | -10.527 | -53.62739 | 2025-06-22 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c76656d0-9eb2-342b-855c-cde525ea7d7a | -11.57254 | -52.09623 | 2025-06-22 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 59185bb7-b5b2-34b8-aa12-07738cae574c | -9.25806 | -57.53174 | 2025-06-22 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8becb18e-02eb-3707-b087-b02d35e47a70 | -11.46989 | -41.43432 | 2025-06-22 04:17:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0628bc7f-d56e-3d62-b192-9cc4768f906e | -14.26149 | -45.50008 | 2025-06-22 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24844b0d-170b-36fc-9398-ba0212be8708 | -10.05907 | -49.6647 | 2025-06-22 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6facb459-5b45-3868-8777-ccd72fbf7375 | -11.57158 | -52.10143 | 2025-06-22 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0746a386-af94-3001-bce6-66ca0fdba3a6 | -10.86428 | -53.76901 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58945c86-307a-3f8f-8faa-3f103735897b | -13.04308 | -53.71373 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c27bc81a-599c-3c41-94e2-019c3f6d0689 | -13.5903 | -48.09357 | 2025-06-22 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f161616-0af9-31c9-b8a2-1b2f55e99f73 | -11.61412 | -58.28768 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 89791a4d-d428-3551-8faf-e8cad69eb89a | -11.42524 | -54.32962 | 2025-06-22 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79cfa046-b3fb-3e8b-ad15-187618cdafcb | -12.60686 | -48.37404 | 2025-06-22 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a420ac98-222b-31c5-a6ee-1ea421e6eb04 | -9.25106 | -57.53065 | 2025-06-22 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f59cf16-fd1f-3739-97b7-879ce7bd2360 | -10.88545 | -56.46706 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5152857e-b332-3424-b65a-36dbbb53b64b | -14.25375 | -45.50608 | 2025-06-22 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fafe03e1-0bb4-3281-b855-1bc9b0b64809 | -10.51129 | -47.58464 | 2025-06-22 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7f1a4a7-66ac-3282-b44e-76fe2f5cbd4c | -9.46635 | -56.06385 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8ba10862-7312-3021-a491-152429fdd194 | -10.06388 | -49.66158 | 2025-06-22 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f676cda-0c97-3eff-a505-359bd5551fc2 | -11.6281 | -58.29034 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3320bde-40e9-332f-ad28-0b3510e6e889 | -9.46367 | -56.06673 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9cb54338-7937-3ca5-8707-bc99d5e89c2a | -13.2706 | -46.82973 | 2025-06-22 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46108b8f-98a1-3713-ac7f-c124bbdd3c68 | -10.52293 | -53.61951 | 2025-06-22 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5113009f-89e1-3365-80e1-0bc93ecdfeed | -12.86161 | -44.49215 | 2025-06-22 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e4f3279-5050-3429-836b-c910c08939ef | -10.5283 | -53.62051 | 2025-06-22 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ea0983b9-848b-3913-9644-cdd341adde16 | -11.61812 | -58.2958 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b1a062ad-44e2-3a6f-8811-37a639f30057 | -10.89816 | -56.46959 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4ddddaa-7d3f-3f87-87e9-22f014617973 | -13.04195 | -48.83894 | 2025-06-22 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef0172a3-6484-303f-b474-22dce8b72163 | -10.9882 | -45.08735 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c12bba8-a324-3dc1-8fba-79cdc7ffde7f | -10.51202 | -47.58031 | 2025-06-22 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1fd7e81-5c60-388c-80db-33be09c11acf | -13.04114 | -48.84367 | 2025-06-22 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79c7637f-4f3e-3c32-a929-f4dd7579c023 | -10.43238 | -47.03542 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 792d8390-b180-3b6a-b0f4-07d6aa2e4639 | -15.56862 | -47.8542 | 2025-06-22 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebc579ae-135f-3020-a26c-7cfbd6faee10 | -12.1289 | -58.18685 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4721f6d6-8520-3f8a-814e-c06aae16fa7e | -12.07661 | -44.98355 | 2025-06-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5f4a189-6a0a-35f8-9643-b6ee7a444460 | -10.98432 | -45.09035 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 62f66de3-be37-3566-a8f3-61b4dbfcbaeb | -15.07979 | -48.94602 | 2025-06-22 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45f1ece2-9e42-34b9-8ad7-5b9790a44f2a | -11.58509 | -44.66906 | 2025-06-22 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f6c0ba-5a16-3d74-a4de-20353d441b13 | -10.89302 | -56.47281 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0af59c74-dab6-3c16-83a2-db652c00c816 | -10.98707 | -45.09442 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7a8dd0db-4d97-3737-bfda-2e0a1b74efda | -11.13848 | -53.91892 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cadc5b48-215d-3d3b-85c4-0e8868e345d6 | -13.79985 | -54.29315 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e3e147f5-2b29-34d9-89c8-914923248357 | -11.10182 | -46.67728 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5e0fed0-e8da-364b-9f04-9a2a70ccd5c7 | -9.45999 | -56.06265 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e5bacc87-c083-3d90-a436-8b132fa2df5e | -10.89283 | -56.46314 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38917e0a-8594-39c6-8baf-82207651e4b6 | -10.8609 | -53.7573 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59ad3460-93ab-3ab4-96ce-3a897ef44af7 | -10.59687 | -46.91976 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06bac0f7-c5e1-3857-9f83-12c42e5803d2 | -10.85488 | -53.75969 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49e03be8-8518-372b-a785-37a563e96143 | -10.89514 | -56.46241 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1d6515aa-5cea-3a5a-ba05-670401fdc143 | -14.25762 | -45.50308 | 2025-06-22 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b509d464-09df-303d-b497-f40c16ba26d1 | -13.78801 | -54.29757 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25fb5934-6e98-3c86-816c-3de1c4fab901 | -14.02486 | -53.36824 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 294a6f64-c3d6-3e94-bfbc-f80240fb7af5 | -11.78728 | -57.23774 | 2025-06-22 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b34e0d4d-eb98-3487-9c6d-8758b65faa79 | -13.65668 | -53.93893 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7241cba-8a3d-3bce-a15e-d5d9c720dbd9 | -15.39551 | -46.68844 | 2025-06-22 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d810e43-17d7-34dc-8d0b-38e70d309b11 | -11.10658 | -46.67001 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de930396-4406-39ec-943c-a39def87f22e | -11.10246 | -46.67339 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8c89c68-6bba-3325-83ba-db345862e6cf | -14.25818 | -45.49953 | 2025-06-22 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 614eeece-2c1f-3ef2-9696-f75f419f39d1 | -10.52228 | -53.62296 | 2025-06-22 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a0df992-a5c1-3a6b-accf-5ab494edf71c | -10.44436 | -47.02897 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64fb2fd8-0144-3276-b23b-0b51a60188f9 | -10.52635 | -53.63083 | 2025-06-22 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccc9ac02-76ca-3f48-84c1-44ee258401bf | -13.04368 | -53.71062 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ade2c38e-05e1-3151-aeb3-0d7505af9d80 | -11.93883 | -51.74829 | 2025-06-22 04:17:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39023504-2714-3862-a5c1-12f2e6b1479c | -13.75347 | -47.75179 | 2025-06-22 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eb058fb-1a6c-3422-80df-782681cdaf65 | -18.01981 | -43.06287 | 2025-06-22 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a4059e29-6da1-3c68-a4c9-93cd126ffcf7 | -10.28134 | -47.611 | 2025-06-22 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
