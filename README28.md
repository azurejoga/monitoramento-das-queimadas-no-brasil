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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca66b4c5-889d-34fa-9049-e65e131727a8 | -17.66623 | -46.67777 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f029ea6-2e34-32db-972c-deccca844735 | -19.75552 | -46.088 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 427a8dc9-3491-380a-bbb4-d826ef266dae | -17.28112 | -46.08562 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b0c84e3-19d6-3439-b819-eef92f473398 | -19.96352 | -41.60481 | 2025-09-12 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b0ead4a8-748b-3761-967f-af1f4621e29b | -21.9467 | -47.55373 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bc84d675-bdec-3d02-a105-7390a0fccaf2 | -17.13849 | -48.48853 | 2025-09-12 03:40:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07217373-9577-3999-bd1b-23052b2e7adb | -17.35375 | -46.69167 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6795b380-e6a4-31a5-90bc-1dabec82a67d | -20.5894 | -48.57864 | 2025-09-12 03:40:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a37647ec-4d6f-3458-8b57-3fea33761a86 | -20.00875 | -46.9213 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ff8775e-68fb-3411-a069-3f429b325645 | -23.12174 | -47.49565 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 083e7c14-ab76-3819-b288-59f70b4eff12 | -17.96053 | -45.2859 | 2025-09-12 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cfb5373-800e-3dac-a41f-1dcc216faba5 | -18.02285 | -46.86337 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7105d9d5-36e1-3c66-a018-b35037faa054 | -21.95494 | -47.56725 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc47bf18-49ed-3300-aa45-bd95acb80aaf | -27.68563 | -48.75067 | 2025-09-12 03:42:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 203bb348-a4dc-314e-aeb6-b3e1d99f8cc9 | -23.60563 | -47.19103 | 2025-09-12 03:42:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b81dfadb-b472-3ad6-a1db-4a14eef0dfee | -23.14431 | -49.65318 | 2025-09-12 03:42:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 53ba2bbe-8b95-37fc-8101-005f2b048c1d | -23.84238 | -51.0789 | 2025-09-12 03:42:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 912e0d9f-cb63-3dcc-a8a6-a521998efa39 | -26.18016 | -51.73695 | 2025-09-12 03:42:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f396e8e7-f710-3d24-8743-427232cd9050 | -23.14215 | -49.66222 | 2025-09-12 03:42:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 64547c76-94a3-347c-8856-a2e82ffcdc3b | -24.12269 | -48.70742 | 2025-09-12 03:42:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01d5cac1-9c2b-3bbb-b813-bf29f781bea0 | -24.11722 | -48.70598 | 2025-09-12 03:42:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9eda90bd-7d2d-32b1-afdc-5ff8373e8462 | -23.14322 | -49.65772 | 2025-09-12 03:42:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 55677cb0-7482-3b6c-9869-e9bfe94b31e9 | -26.18151 | -51.73162 | 2025-09-12 03:42:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e22ce7f4-6f0f-3234-847f-f815fe25adc7 | -21.2061 | -47.5296 | 2025-09-12 03:50:00 | GOES-19 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 125.6 |
| ed322627-aa72-3270-a7e8-76c13bcda7f6 | -21.9679 | -47.5525 | 2025-09-12 03:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a76d77cf-08b0-308a-a15a-cb6ada805625 | -12.9289 | -54.7744 | 2025-09-12 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 858f3db8-d547-3e9e-aab4-0f76d0749f71 | -13.8983 | -48.2581 | 2025-09-12 03:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 64628e50-3cc4-3010-864b-f1ec92b986c4 | -11.5263 | -50.404 | 2025-09-12 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 1cbcd282-dcb7-35ee-92dc-e374303aae9d | -11.5235 | -50.5968 | 2025-09-12 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 56afb3be-4914-3bef-a238-9bba245412ac | -9.3017 | -65.5959 | 2025-09-12 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b67cdf4a-3d0f-3a39-bddc-1685ce711161 | -11.5454 | -50.4019 | 2025-09-12 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| af3c1a61-2a78-35d2-9b9e-b022e286583f | -12.9294 | -54.7333 | 2025-09-12 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 6f4e2622-d8cc-32fc-b5cb-8f3b2292c845 | -21.947 | -47.5578 | 2025-09-12 03:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 54214f25-e845-3a4e-a5e8-cd45a679eb8d | -12.9103 | -54.7352 | 2025-09-12 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 07c0f7a3-6b24-339f-b2da-d9dbbf6e7be3 | -12.9098 | -54.7763 | 2025-09-12 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| a4ac1762-d3b4-3986-9563-472c2218cdd6 | -21.2068 | -47.5059 | 2025-09-12 03:50:00 | GOES-19 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f955a442-e5c3-3fd7-9d3d-a5f918d9191c | -13.8987 | -48.2358 | 2025-09-12 03:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5b058584-dde5-3839-bd3a-6565d26b60bb | -11.5266 | -50.3826 | 2025-09-12 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 8d6b0af4-4c5d-3ac6-8cab-6cf68e257817 | -21.1861 | -47.5109 | 2025-09-12 03:50:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 4b444a41-7cf3-30d3-8c4e-ec388f99c6f3 | -22.7014 | -48.6852 | 2025-09-12 03:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7a5b6d3f-8cba-3731-afa5-409c43ac40d2 | -13.9177 | -48.2552 | 2025-09-12 03:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4db42b7c-4435-3c10-a8b5-f34a01fc396c | -22.1931 | -49.7353 | 2025-09-12 03:50:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| bea026db-3240-3df1-a3df-4ded6b77b72e | -12.9292 | -54.7538 | 2025-09-12 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 611.3 |
| e0d1eeca-3f88-3feb-aa5b-a0d83d6682eb | -12.9101 | -54.7558 | 2025-09-12 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 329.9 |
| cabdf1bc-32fa-3afa-b8b8-f157c4a82cba | -21.1854 | -47.5346 | 2025-09-12 03:50:00 | GOES-19 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1fbe1e38-0566-35ed-81d1-3a725709468a | -11.5425 | -50.5947 | 2025-09-12 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 0164220c-3e55-361c-827f-01507b76c91c | -22.7007 | -48.7088 | 2025-09-12 04:00:00 | GOES-19 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f00fc74b-ddff-3964-83d8-21ccda493881 | -12.9101 | -54.7558 | 2025-09-12 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 223.5 |
| a261d90a-fdca-3a90-8140-1c194fbfa59d | -21.947 | -47.5578 | 2025-09-12 04:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 11605416-97f2-3794-a89e-4674c8328408 | -12.9098 | -54.7763 | 2025-09-12 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b01aa101-fb67-31df-b1f5-8b7e5b2f5067 | -12.9103 | -54.7352 | 2025-09-12 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9d70ecf1-5f61-36a2-867c-f851e5551939 | -12.9294 | -54.7333 | 2025-09-12 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 87e46b26-d08f-355e-a901-5aeb9b1f672a | -12.9292 | -54.7538 | 2025-09-12 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 441.2 |
| 2bafa7a6-1652-31b1-8e2a-a4e8cb5951e2 | -21.1861 | -47.5109 | 2025-09-12 04:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 127.3 |
| acfdc3f3-d3f6-38ce-b562-5db9d6544003 | -12.9289 | -54.7744 | 2025-09-12 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| baa7a202-ed83-3a25-bb7c-cff33e89a158 | -21.9679 | -47.5525 | 2025-09-12 04:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 719475a2-ee9d-33dd-95e8-7f3336fedc03 | -21.2068 | -47.5059 | 2025-09-12 04:00:00 | GOES-19 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 618ae84f-e188-390d-b99d-8205182e8ca7 | -22.7014 | -48.6852 | 2025-09-12 04:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 943da9c9-95ac-319e-8efa-431b18ed37a0 | -21.1854 | -47.5346 | 2025-09-12 04:00:00 | GOES-19 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 1326d50f-ba41-3a34-95c5-ab12df140f94 | -21.2061 | -47.5296 | 2025-09-12 04:00:00 | GOES-19 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 7d14e47a-2aab-3700-81f4-e631d1e11181 | -3.26256 | -48.4577 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb0229b0-ea42-3fe1-9741-fbaf5a5e2559 | -3.26137 | -48.46461 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47870efd-0878-3400-bc2c-ea97bda27383 | -3.316 | -50.07998 | 2025-09-12 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4d5eb4a-c94e-30d2-a2f5-ef3fb4464239 | -3.26067 | -48.46161 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed7cd1f9-020a-39d5-99d2-f774aefe05a9 | -3.31994 | -50.0811 | 2025-09-12 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 712c5fcc-aeb5-3d19-9320-945ecece1619 | -3.21795 | -47.12984 | 2025-09-12 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 79444d24-5462-3ecc-a948-ee464ddb9abd | -3.72199 | -41.07616 | 2025-09-12 04:02:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ac8466f-95bd-31dd-ad2d-e3f4b7eb2eae | -3.31394 | -50.08004 | 2025-09-12 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4899c3e7-08be-35f7-9a6a-a0fac1ec6296 | -2.92276 | -48.63287 | 2025-09-12 04:02:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6e7c44d-be6a-3a3a-bf0d-74bf0755b665 | -2.92614 | -40.41831 | 2025-09-12 04:02:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2742e3bf-65b5-3bcf-9cc8-f26bf99f5af5 | -3.26197 | -48.46115 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cdeb18e-d44e-323f-92cf-fe42a6b37b18 | -2.62704 | -46.83234 | 2025-09-12 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39e6392a-7167-3c94-bbbd-df683b9b2e47 | -2.44277 | -47.33252 | 2025-09-12 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 453865a6-de50-34ae-b760-d6f2a1368120 | -3.89662 | -40.92327 | 2025-09-12 04:02:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2bd70769-4d99-3435-b501-417a618f4a7c | -2.43817 | -47.32874 | 2025-09-12 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 018943e7-ed70-3ec4-90eb-13013f918b09 | -3.25717 | -48.45671 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad6bd554-c931-3c6c-8389-08a77fb8833f | -3.32277 | -50.07653 | 2025-09-12 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8ef25a2-b5bd-387d-ab2d-290afe44211b | -2.7432 | -48.69654 | 2025-09-12 04:02:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be9e094b-2a0b-3340-a0ed-b265ee1aec87 | -3.2601 | -48.46508 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e07b043-7c04-3481-8db6-37411d335906 | -4.4858 | -38.41745 | 2025-09-12 04:02:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1e3eaba-bed5-3209-a86c-d0432ea65dc4 | -2.62126 | -46.83698 | 2025-09-12 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2298c27-e6b0-3abf-90d9-df50a489d42f | -3.67865 | -47.4937 | 2025-09-12 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c9580d9-24a2-3f85-8bc7-d05d1d24dde2 | -3.32067 | -50.07666 | 2025-09-12 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e688056-3bd4-3950-8065-48537b937352 | -5.24935 | -38.93941 | 2025-09-12 04:02:00 | NPP-375D | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f0c41b8d-7a7b-3576-8888-22f5b231b3cf | -3.26124 | -48.45814 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 788fd422-09fc-311f-b385-19a71d64066e | -3.67364 | -47.49275 | 2025-09-12 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 757ffb76-b3b2-3dd6-a15b-774e996aad0a | -3.14305 | -44.42977 | 2025-09-12 04:02:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc138f43-5c0b-36f9-b768-77adbac30ec3 | -3.67458 | -47.48719 | 2025-09-12 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 051da833-d67a-3c8c-9419-e35b01ad101b | -3.25585 | -48.45711 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7acdd5a6-16ae-33be-b335-45ba3032dcaf | -2.91727 | -48.63192 | 2025-09-12 04:02:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20265ae0-db90-3051-9eb8-6c45d73f6ade | -2.92287 | -48.63311 | 2025-09-12 04:02:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd9a68d7-fe64-30fb-8593-37580306a619 | -3.35021 | -39.27792 | 2025-09-12 04:02:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 847c2e86-16de-38a1-a3b7-8244f774a8b4 | -2.62616 | -46.83772 | 2025-09-12 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e980c88e-57b6-31d1-a02e-c871ac886ea7 | -4.11038 | -38.33453 | 2025-09-12 04:02:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8e5cd9f1-3e26-36e8-a0b1-60b3709aa3aa | -2.91737 | -48.63214 | 2025-09-12 04:02:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75399adb-d887-35cb-b361-9f3f4b3885a8 | -3.22289 | -47.13066 | 2025-09-12 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8e4604ae-a00c-389d-bd63-07215fb4d103 | -3.89721 | -40.91962 | 2025-09-12 04:02:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5a4a096b-5eeb-3128-9f54-0c1cd30d8136 | -3.25641 | -48.45368 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4c3cc74-fec6-301e-9bac-73bc696561bc | -4.43675 | -38.4574 | 2025-09-12 04:02:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 18a7809b-2e87-32ee-ab26-9071c95cc98f | -3.25658 | -48.46015 | 2025-09-12 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README29.md)
