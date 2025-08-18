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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba39c7a2-84e7-3503-aed7-a39f691a2003 | -23.67569 | -51.64879 | 2025-08-18 03:36:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 43d1eefd-4711-325c-b4d4-13ff83cf9893 | -23.06829 | -45.60767 | 2025-08-18 03:36:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1774b2b4-260c-3b7b-b1da-eb37d0bbc1d1 | -23.30451 | -46.89063 | 2025-08-18 03:36:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a9c2c171-e161-3abc-a99a-2c1ef455caa4 | -23.68271 | -51.65144 | 2025-08-18 03:36:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 73.3 |
| 15f6dba8-20e8-304f-873b-44f39e5f0192 | -23.67545 | -51.65061 | 2025-08-18 03:36:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8f37775a-ca39-36f6-a895-c606e07596c0 | -22.14293 | -50.02688 | 2025-08-18 03:36:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26108007-8821-3196-9f24-ef7e13aa5870 | -20.00032 | -46.15421 | 2025-08-18 03:36:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb9e9b15-e11d-3abe-a585-75d41a493c3f | -20.42203 | -43.67739 | 2025-08-18 03:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6ba2c0e9-604d-3cac-b891-4f0c59322dd8 | -20.21434 | -47.03882 | 2025-08-18 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fa21117-dd93-3a50-b9bc-1623915a814c | -20.42704 | -43.67798 | 2025-08-18 03:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0417f57a-87a5-329e-897c-d54cc457ebc2 | -20.20943 | -47.03247 | 2025-08-18 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 666d3214-2588-3294-80f8-afa174b00c6a | -22.0791 | -45.05656 | 2025-08-18 03:36:00 | NPP-375D | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6eb409ae-80cb-360f-9d0b-0e33e55c4071 | -19.9994 | -46.15832 | 2025-08-18 03:36:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d81230a-d03f-3953-a9ff-ed3efda592a7 | -20.00698 | -46.15155 | 2025-08-18 03:36:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46d4ac6c-5254-3e98-9761-ee1c7c6e5b03 | -20.21049 | -47.02792 | 2025-08-18 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f604a07f-ab15-3f59-95b2-8551d4f47761 | -20.21326 | -47.04348 | 2025-08-18 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f068425d-eadd-3e7d-98cb-a89b8ec5e271 | -20.2212 | -47.03667 | 2025-08-18 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7207bb3a-9b5c-3ffd-be52-a132a5fd9595 | -20.22329 | -47.02764 | 2025-08-18 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5d0a9cf-53e4-38ea-8a4b-165a61b5b7aa | -20.34758 | -45.30836 | 2025-08-18 03:36:00 | NPP-375D | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cbd746fd-a729-3130-9a61-f7194ed064d6 | -26.00128 | -52.06017 | 2025-08-18 03:38:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 913cbc60-54d7-30ef-adc5-42a8b7958336 | -9.4956 | -40.3586 | 2025-08-18 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 47da654a-b23c-3c4f-a3a9-d0949370c9b6 | -9.4765 | -40.3613 | 2025-08-18 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 28b005dc-b3fc-3a4d-b8ff-c204ace5de3a | -6.4335 | -44.7822 | 2025-08-18 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d766356c-548f-396a-abae-5ee45d55bd4a | -13.2186 | -50.7781 | 2025-08-18 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f3c19b0d-5677-3d39-9b68-d67b5155f627 | -14.9815 | -54.7743 | 2025-08-18 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d1d13c5f-b4df-3eb3-91c7-286d8c1b9485 | -13.219 | -50.7566 | 2025-08-18 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 195.7 |
| bfc6625c-5907-3838-970e-519f5d6f4493 | -3.982 | -42.516 | 2025-08-18 03:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 0fbadf2d-1d47-3a16-a469-fb9f7060de6b | -6.4335 | -44.7822 | 2025-08-18 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 091971a1-83a3-364c-aa9d-4399b1429c47 | -9.4956 | -40.3586 | 2025-08-18 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.3 |
| f9fc8ad1-978b-35ca-b8c7-60e50ea9ec64 | -13.219 | -50.7566 | 2025-08-18 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 9ab9e1e3-24b5-3b12-aa79-f8ffdc95c6a1 | -7.51384 | -44.99158 | 2025-08-18 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4204ba8-9729-34d4-ae74-b4107b95380a | -4.77956 | -45.32341 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1947dc34-e85a-3d6a-a0c8-2c9621390597 | -6.07978 | -44.61083 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 494caa57-85e0-3529-bdc8-3c27797e1624 | -8.23399 | -47.86365 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6f53d2e-ed26-3186-bf5b-bfa049315f0f | -6.54788 | -43.02327 | 2025-08-18 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4ae75d1-4926-37f8-8eed-ae8eeb0dcf01 | -3.7931 | -41.00168 | 2025-08-18 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ebfe753f-345a-3131-baa2-62d4db056cc8 | -7.20028 | -43.97277 | 2025-08-18 03:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2e8541e-c41a-3c48-ae50-9e6905211bec | -6.05119 | -44.12039 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28339640-f05e-3d1d-a757-690354305a94 | -3.21999 | -46.81774 | 2025-08-18 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c00e5637-e8e6-33bf-bb08-bb4a58872d2d | -7.56477 | -45.42284 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2195901-f0b0-349d-9675-b56c679d4788 | -8.03497 | -47.68139 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db525435-67f3-3b52-b147-f4e11ee1e4d2 | -3.78949 | -41.00112 | 2025-08-18 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db27998e-b371-33b2-9022-9f8ab8c4cf16 | -3.58886 | -47.53243 | 2025-08-18 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39e1f340-fe15-39e7-ae37-fdd682d941bb | -6.1504 | -42.70177 | 2025-08-18 03:53:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 97b774bf-1144-38c6-a789-a7bca1d0c6c3 | -6.11118 | -46.67334 | 2025-08-18 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e64e3f2-4302-3b63-bb6e-cc80b8d00d54 | -6.67357 | -41.7695 | 2025-08-18 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0922a1c3-4086-37d4-93fc-2538f6daf195 | -7.83052 | -38.41601 | 2025-08-18 03:53:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e5ab862-73db-3720-9aa1-79966d1491e6 | -6.42808 | -44.79145 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 967db911-56f9-3c3b-878d-00cde5b60648 | -8.03399 | -47.68415 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cef79c2-09c6-3b62-9f95-45bbe5b24c3e | -3.21902 | -46.81256 | 2025-08-18 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b74aad0f-9a18-32aa-ba65-14bdf6c2b563 | -4.78341 | -45.32906 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a25ac9e-befa-307a-b061-a4a23aeb0eaa | -9.49383 | -40.36631 | 2025-08-18 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e6f9d5e-0322-3b22-80d4-c023ef8354d6 | -7.60573 | -40.49456 | 2025-08-18 03:53:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0aaddc7f-b4ba-3a43-a696-b4e9e6a6024a | -6.67981 | -43.66928 | 2025-08-18 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dc6bb92-9f16-3e20-b1bc-5f02f06f3575 | -3.21845 | -46.81586 | 2025-08-18 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68c661d7-b2a4-3db5-b156-c7f4ad5d538e | -5.98464 | -44.13005 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb070c76-01f8-3ed0-89d2-9dc885d25070 | -6.7995 | -44.73013 | 2025-08-18 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9276b2b9-7e63-3769-8fe6-a7a27c2afae8 | -6.05405 | -44.12904 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac8b6216-6cc6-3886-b996-78b06d5038e7 | -5.7512 | -46.67204 | 2025-08-18 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bf0905e-9d1b-39c6-95b8-c65e17a36100 | -5.75625 | -46.67295 | 2025-08-18 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52354e4f-4dad-364c-bfdf-921473a04cb4 | -8.21756 | -47.30334 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35bce5b3-ca7a-3659-808a-dd6ae170e36b | -6.14656 | -42.7011 | 2025-08-18 03:53:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d46cb558-9a23-3e32-b832-a25bccb7c78d | -6.42952 | -44.78292 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 766442cc-c49f-38a0-868f-e2ee13d787e7 | -7.55075 | -45.44112 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89bc01f8-c740-31ca-8700-7f80579f39bd | -6.03545 | -44.34032 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e593e12d-03d0-38a6-84b9-9e0a002e10fe | -7.20091 | -43.96911 | 2025-08-18 03:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cb0cef4-c78e-3b87-b536-24260eb1f29d | -6.82477 | -39.89679 | 2025-08-18 03:53:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf4997c4-f76d-3808-8726-2345d2fa6d48 | -9.74823 | -37.91744 | 2025-08-18 03:53:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fe56d59f-6cf8-3957-a222-5c980fe7ee80 | -6.43391 | -44.78367 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b14c7c2c-0e41-333e-b9c6-ce4ca9dcb180 | -7.28541 | -43.69083 | 2025-08-18 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68a42e7c-b6bd-3c99-9502-2756d42bb9c5 | -6.98513 | -41.62447 | 2025-08-18 03:53:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ffc7bbd-739b-3198-868f-12e88b30cae9 | -4.77235 | -45.32536 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b982106-51c0-38fa-8760-c165182570e6 | -6.52814 | -44.55275 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e8d67d4-f7cf-3dc8-b1de-bd04dc7e70ae | -3.59504 | -47.52959 | 2025-08-18 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 875c03a2-6fdb-310e-8fb5-77dabb8b3380 | -8.10101 | -42.36021 | 2025-08-18 03:53:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 722b0bb5-e5c1-3ef5-8fa1-7845cf5c5fc4 | -6.15425 | -42.70246 | 2025-08-18 03:53:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4766fc93-6ae9-322d-8e23-31d4c183f303 | -6.52802 | -43.43039 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9552a8e8-4e7c-383f-8d8c-d2dcad19b70b | -6.42401 | -42.49932 | 2025-08-18 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6af18989-81a9-3ff2-a196-dddd6cebe466 | -6.11168 | -46.67046 | 2025-08-18 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf578770-9e21-359b-aeb2-cb090b3f9627 | -6.54876 | -43.02003 | 2025-08-18 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55737d17-709b-3673-8152-acedcd30d511 | -6.07895 | -44.61171 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0b6bf7f-e783-3e50-8dea-f23feb4b9e3c | -6.03117 | -44.33956 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0caf0113-557e-34a1-911c-148a11166e25 | -6.54784 | -43.48454 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df81cdd9-cb92-3a32-b111-3cd427e15690 | -7.13678 | -44.19465 | 2025-08-18 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19c7a0a9-fae1-3861-9e32-c1efce8ab6d8 | -8.04134 | -47.67594 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e057225-a5a7-37a1-8919-877183c57816 | -3.79377 | -40.99752 | 2025-08-18 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df884401-6eaf-3fc6-ba2d-7e704c2bcd14 | -3.61657 | -41.5423 | 2025-08-18 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6efb595-3edd-3bfa-ac35-83b7f84fe77c | -6.5645 | -44.46996 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b244860-76f6-3fc0-86ed-8bf106350310 | -6.52499 | -38.81157 | 2025-08-18 03:53:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9d052a63-c0fb-31ed-ab7c-4afa9319ff2d | -7.09646 | -40.65092 | 2025-08-18 03:53:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae6b3234-5e5e-3bf2-aebc-b2bd8328b9ce | -6.90369 | -39.55194 | 2025-08-18 03:53:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ef88c601-9cf3-38cd-abb6-6cae49b56f73 | -6.56877 | -44.47077 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a57a4966-bed2-3ad9-884a-1b46531a55df | -4.77489 | -45.32256 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d72b3ef5-8bb4-3317-ad06-c65a11616335 | -6.55341 | -43.01398 | 2025-08-18 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05b8238c-a800-3ee2-ae2e-55f194c4eb35 | -4.91062 | -43.24164 | 2025-08-18 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65a4393a-189c-3462-b3f5-24da10c36e49 | -6.55387 | -44.48045 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2d5f1dd0-1039-39cd-97cc-61f2abb643ee | -3.79243 | -41.00585 | 2025-08-18 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9d0c184c-2a4e-392e-9ec8-a8a5140abcf6 | -8.57428 | -39.42795 | 2025-08-18 03:53:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fe0dc2a-76ee-35b1-8ab3-199865bae4f8 | -6.16194 | -42.7038 | 2025-08-18 03:53:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d56b183-8012-394d-bd2c-c501fd253a0b | -6.67515 | -43.67212 | 2025-08-18 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README11.md)
