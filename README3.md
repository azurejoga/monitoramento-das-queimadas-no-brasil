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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 396e9681-5dbe-3b4d-803a-678aed4a8c45 | -17.60962 | -49.59887 | 2025-05-01 04:40:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24773e38-ef78-364c-8658-6d15df69a79f | -18.41296 | -51.99478 | 2025-05-01 04:40:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37b9d365-c284-3241-b318-e3fdc401974b | -20.76228 | -46.77026 | 2025-05-01 04:40:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d76fc0eb-9181-3561-9487-f43d69c5027c | -17.10185 | -53.61615 | 2025-05-01 04:40:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb2cf839-835a-3598-9a90-2bbd340e2a2d | -19.76764 | -49.74372 | 2025-05-01 04:40:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79205354-2c02-3435-a330-66339ded7de0 | -20.62266 | -55.04031 | 2025-05-01 04:40:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb13efb3-c116-3f08-9785-910e04cc2912 | -16.31546 | -53.82876 | 2025-05-01 04:40:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d45915cb-f41a-3f54-980d-a194e918c400 | -20.04395 | -51.5399 | 2025-05-01 04:40:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 325107b1-5561-31aa-9899-1b8cb88853bf | -16.30793 | -53.83137 | 2025-05-01 04:40:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 774e1e54-4034-37ed-b839-81517570db15 | -18.40965 | -51.99421 | 2025-05-01 04:40:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f04d5fba-a35d-37c9-a9c1-466e8032b24d | -19.7747 | -49.74482 | 2025-05-01 04:40:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77fd082b-ddb8-3238-8588-5c64d772a24c | -15.92796 | -49.60339 | 2025-05-01 04:40:00 | NOAA-20 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4161ae95-d3d8-3375-afc3-1c30aae6801f | -16.17571 | -57.69796 | 2025-05-01 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fec8cdb4-f049-3186-bc46-d9435b41a569 | -15.07818 | -48.94298 | 2025-05-01 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fa2356a-625d-3da7-85f2-3aa673f81d60 | -20.47841 | -53.67449 | 2025-05-01 04:40:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c35e620f-659d-32e1-8c6f-d55b49354f73 | -15.5155 | -53.50752 | 2025-05-01 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43a3730e-93c5-3240-981f-42aa3a1065e3 | -23.8724 | -53.43885 | 2025-05-01 04:42:00 | NOAA-20 | PEROBAL | PARANÁ | Brasil | 4118857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f7d46a91-7b9f-3388-9583-cdc730ed2bd5 | -26.33582 | -53.18595 | 2025-05-01 04:42:00 | NOAA-20 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 98db86e9-9b0a-3491-b4c0-438088af7b9a | -25.03315 | -53.16998 | 2025-05-01 04:42:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5272bf55-74cf-3538-8f5c-819842b798ae | -27.18268 | -48.80898 | 2025-05-01 04:42:00 | NOAA-20 | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e53f2d4-35b2-30d5-8825-538be6f6bb1e | -23.33804 | -46.7743 | 2025-05-01 04:42:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7d3d7d17-f781-38b8-9b5e-ba955b3c4cd1 | -21.4716 | -57.16224 | 2025-05-01 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da17a9cf-0a97-34c3-a76a-fdb58f999926 | -23.04494 | -49.89702 | 2025-05-01 04:42:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d124cc54-a4b3-3d4d-9be7-df28402eab5b | -23.27083 | -51.20544 | 2025-05-01 04:42:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da0bbbf5-06e1-309d-b9a8-3252ed9b1eb3 | -23.60795 | -49.00949 | 2025-05-01 04:42:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3cba3d4-76f0-3a09-bfd7-48103d1f041f | -23.5952 | -47.4384 | 2025-05-01 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f054d3bd-96c6-398b-a8f0-fbe06cfb63ca | -21.46784 | -57.16143 | 2025-05-01 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86e43c23-dbaf-3df4-a3c4-60ec21345206 | -24.24392 | -50.73959 | 2025-05-01 04:42:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fa94a4a2-5f25-3e2c-bb70-3b382df507da | -23.60096 | -49.00327 | 2025-05-01 04:42:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8826aee7-c24c-37d4-82f9-77f1e7a8aa7e | -20.98647 | -56.66113 | 2025-05-01 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b56b78e-54d5-3316-9805-b306d4a611be | -23.32684 | -52.04081 | 2025-05-01 04:42:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 08d98b1e-0343-3c90-945a-087d7e8c1bef | -23.60478 | -49.00391 | 2025-05-01 04:42:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0252926-286a-31a0-9d89-320d69699246 | -22.54089 | -48.81393 | 2025-05-01 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 157194a6-6793-30bd-b99d-ac4f784fa7e4 | -29.73891 | -51.26661 | 2025-05-01 04:44:00 | NOAA-20 | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 9d89c1c8-cae3-38ad-8686-c1cc841f89b9 | -30.04054 | -50.75386 | 2025-05-01 04:44:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 5b79ae25-bddd-3945-8faa-7a79bbef91e4 | -29.70657 | -52.57452 | 2025-05-01 04:44:00 | NOAA-20 | VERA CRUZ | RIO GRANDE DO SUL | Brasil | 4322707 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dec7f383-206d-3e32-a0f4-3db364326422 | -30.05316 | -53.77146 | 2025-05-01 04:44:00 | NOAA-20 | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 2e77acbd-884a-31b4-ac48-1816da6b6cba | -12.36123 | -63.92046 | 2025-05-01 05:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5120fc86-5d63-39cd-8bdb-90a6b21054e1 | -12.26199 | -63.8278 | 2025-05-01 05:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0d2b9bf-87f3-3b5f-b7c1-c1aaba26b68c | -12.36067 | -63.92455 | 2025-05-01 05:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


