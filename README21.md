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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1760fd0e-c802-3556-bd95-f4cbabb79308 | -24.31644 | -50.85428 | 2025-07-11 05:04:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e0612b7b-467a-3677-8e6a-f5847c1b2b8c | -24.31972 | -50.84951 | 2025-07-11 05:04:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d5757a76-2d7c-394c-9783-b63f7dee1dfc | -25.25416 | -52.2364 | 2025-07-11 05:04:00 | NOAA-21 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41fce2f0-f30c-3db6-a43a-0e82ab629d59 | -25.25683 | -52.2353 | 2025-07-11 05:04:00 | NOAA-21 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 34e5ec47-6ab1-3315-a8d9-626a57d21656 | -25.25899 | -52.23235 | 2025-07-11 05:04:00 | NOAA-21 | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85ddea15-6cf6-33e4-9342-8b5796ab7ff2 | -10.6862 | -49.4874 | 2025-07-11 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1adf64a3-0b2d-3d54-b092-63e0912cc1ff | -10.6672 | -49.4895 | 2025-07-11 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 4816b4b0-f150-3a2d-8a1d-935a4015a9f6 | -5.5427 | -43.9096 | 2025-07-11 05:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 9777880c-469c-37de-be4d-bf6685bc30ae | -5.5429 | -43.8864 | 2025-07-11 05:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d28df0c0-0ba0-3503-85f3-a851191443f9 | -10.6862 | -49.4874 | 2025-07-11 05:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| ea511176-bfd2-3e6f-aa22-d4834a2c1f20 | -5.5427 | -43.9096 | 2025-07-11 05:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4c429ec1-cbf5-341d-9b7c-0a77b4203b23 | -10.6672 | -49.4895 | 2025-07-11 05:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7114f67e-0b2f-3896-9636-31cb1f722178 | -5.5429 | -43.8864 | 2025-07-11 05:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c0e3401b-a6cb-3ad1-a77d-19681e4eaaff | -4.54797 | -48.00674 | 2025-07-11 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ba214f8f-df14-313b-a039-367906611042 | -7.27614 | -49.57038 | 2025-07-11 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 108827ba-1134-3cc6-8ac0-eaebee1c5f3d | -4.5472 | -48.01222 | 2025-07-11 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e09744fc-bc06-3cb8-be14-bb858790effe | -4.54832 | -48.00563 | 2025-07-11 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9d4fa9e3-efa0-3f87-a9a0-3accd0d00776 | -7.27549 | -49.57509 | 2025-07-11 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b849773-b2c1-39f3-8bc9-eb08d7dad26f | -6.15894 | -47.26938 | 2025-07-11 05:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aac099f6-8c9e-3cc6-9443-cded40d4f384 | -4.54751 | -48.01112 | 2025-07-11 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c64e3449-444c-3bd7-9133-62449cdae0fd | -6.15807 | -47.27579 | 2025-07-11 05:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d5a891f-c5e4-3e30-9b02-d4739f976e4b | -9.96209 | -64.97552 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cad9d5eb-d5a2-39e0-b165-fd5d65a5df90 | -9.63215 | -61.45482 | 2025-07-11 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43d3fe34-a924-36e4-8886-79a25e85b036 | -11.84639 | -47.50408 | 2025-07-11 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29d601b6-93de-34f4-9439-580a565988eb | -11.57271 | -47.42641 | 2025-07-11 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bb840c8-021b-333e-ad89-8d37b7e0cbfe | -9.96434 | -64.96223 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 543245c6-a63a-3e3e-9aaa-648e930d1745 | -11.93674 | -49.30306 | 2025-07-11 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bdb8500-a2b9-3420-af32-6322bf845d0d | -12.5798 | -56.97553 | 2025-07-11 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c421200-af7b-3dfa-9376-a00881d12941 | -9.86087 | -60.29465 | 2025-07-11 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14196e5b-8bbf-3469-b0d9-bff75e6f7170 | -10.66815 | -49.48959 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f7138b7-8464-3aeb-b61a-0cf1dc00ffd3 | -10.6793 | -49.49495 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 90c7abc5-91bd-37a3-9e9b-119a4dce11f5 | -9.92473 | -59.90215 | 2025-07-11 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a3ef911-fbae-3990-a046-486037299968 | -10.67352 | -49.48896 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d2c463a4-4390-3148-97b8-0eb7a794d620 | -8.57315 | -47.18764 | 2025-07-11 05:25:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c749048-07b4-3b1f-b790-7148b9de6403 | -7.89307 | -61.47309 | 2025-07-11 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7f85cb2b-d9db-3efb-996c-3e0e05a63692 | -9.86831 | -63.29971 | 2025-07-11 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6923062-09b7-3078-8380-9b8a684fa33d | -10.11852 | -65.14983 | 2025-07-11 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dad52363-6cb2-36d6-87a2-ba0a17c2683f | -10.68747 | -49.49169 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de270c06-d6f0-3889-a57f-d34be85fe3d9 | -9.61993 | -49.0165 | 2025-07-11 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 150a4080-5f27-31a7-a9d6-ccc067ba9cea | -9.96064 | -64.96159 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47ffc602-6493-37bf-8acc-2e6e5414a175 | -12.05381 | -48.54959 | 2025-07-11 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52984790-5243-3656-a118-31e6ec3bedf9 | -9.70548 | -56.18692 | 2025-07-11 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74d87417-4521-3102-9e2c-8c1cb922a016 | -10.57328 | -49.13012 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9946137e-f7b3-366e-b1e5-f02df648d879 | -7.93004 | -61.55798 | 2025-07-11 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 059734f2-54bf-3ce2-bdde-3f21599b60a3 | -9.94139 | -64.96282 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8150a49d-69e4-32e0-bb4f-8f8912bfa6a7 | -12.05456 | -48.54315 | 2025-07-11 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fd4d871-b505-3705-8b27-8947650b7205 | -10.84901 | -49.12298 | 2025-07-11 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 36f913d0-065c-37cb-8bac-67be55808acd | -10.57022 | -49.14049 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa64575a-c385-3dc7-923c-73be1dd7a30a | -11.32361 | -55.21465 | 2025-07-11 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd3817ba-0a66-3a6f-89da-e8051677a67d | -12.58028 | -56.97196 | 2025-07-11 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d17c2d6-a378-3d44-b200-5e75bdb4507f | -9.61339 | -49.01575 | 2025-07-11 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97637a05-2ab9-30a5-b693-294c55723430 | -6.62676 | -56.27559 | 2025-07-11 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1c6e32e2-f8fd-39e5-86d9-1de462bd6a31 | -9.61208 | -64.52551 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b99b53b8-7bc3-3b2f-9f59-a0b80805aabb | -10.67284 | -49.49436 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 033f5265-048c-3a9e-97f2-7c67662cb7a8 | -9.94509 | -64.96346 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5f90f2fb-2c5b-386d-98d9-192da54981be | -12.0547 | -48.54262 | 2025-07-11 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cc41ddd-1774-37fa-a51d-b8c63a60317d | -9.62883 | -61.45428 | 2025-07-11 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0579ccf8-2ddb-3b69-b94b-52fedb8ef946 | -9.8677 | -63.30348 | 2025-07-11 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69b9b279-abcf-3022-be2f-7a3433ebcf73 | -9.25764 | -57.79882 | 2025-07-11 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6357aa79-90b7-361f-b272-f3ccefb4cdd0 | -10.80765 | -62.00027 | 2025-07-11 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cbb4e29-30bd-3e7f-859c-867b1c49b4f3 | -9.91328 | -47.82707 | 2025-07-11 05:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d8d5fe91-9e8d-3bc1-a0d6-6f19412fe857 | -10.57741 | -49.13585 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cb8dbc0c-197b-3b4e-9084-710959018534 | -9.85786 | -47.87293 | 2025-07-11 05:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9381f6d0-07bb-3282-a350-8928b50bd8b4 | -12.01701 | -49.52244 | 2025-07-11 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ade0f3a-c1af-3138-b3c7-285119e0fb10 | -10.8556 | -49.12381 | 2025-07-11 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80c9c64f-dc4c-37f1-9947-588646b62f6a | -11.87845 | -58.71768 | 2025-07-11 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f489670-d8dc-34bd-b401-b35a5b29c679 | -9.86477 | -60.29161 | 2025-07-11 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07545fd0-efd1-370c-8ecb-5e2082f69bc4 | -9.91682 | -47.83326 | 2025-07-11 05:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 858a574a-01de-3aff-bf84-fda905499d1a | -9.96879 | -64.95844 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a06c4d1-129e-3e2d-a5b8-2f04ec70aef6 | -9.94585 | -64.95905 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a94a881b-7cb8-3cd2-9988-0b3b980ca27d | -12.57931 | -56.97911 | 2025-07-11 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4751d78-f61a-3a73-b5f5-886badff2fb0 | -10.57803 | -49.13045 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 39a89cb5-9b02-3502-ab20-e8ce2b4fd324 | -13.6089 | -59.8078 | 2025-07-11 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e74e863c-79a6-3d33-83ec-77cf245ff08e | -10.8722 | -54.06347 | 2025-07-11 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b93ad2ae-cbb0-3056-9077-88287b89e5d2 | -9.96954 | -64.95402 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8d0bb8a-bef2-34e1-a781-c6a5df08933c | -10.9753 | -58.66454 | 2025-07-11 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 207a3111-2154-3bb3-a4b0-117ce5bc0572 | -10.67458 | -49.49034 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 64e9a4c7-08bb-3954-97c4-f081bc2e2666 | -10.84968 | -49.11731 | 2025-07-11 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d575b7b4-5d7f-33af-8122-bdc9e7b986dc | -11.32421 | -55.21019 | 2025-07-11 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3fd8c5-bbc4-38f5-ab6d-7d431206e00a | -10.67395 | -49.49572 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 81abfe15-286d-394f-a1f8-c76c67c5e1e2 | -8.38039 | -51.07631 | 2025-07-11 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa5d784f-d8d8-3bbf-850d-955fe8afec21 | -9.96284 | -64.97108 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddc029d7-9455-3567-a3a4-c77205ae7d56 | -10.68063 | -49.48431 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ce7c59ae-b46e-3557-859a-e0778aa55bfb | -13.00273 | -47.8245 | 2025-07-11 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e69fd57c-aad1-3870-95c1-4849bd0f09f8 | -9.87114 | -63.30404 | 2025-07-11 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e2fcbe1-4f50-3f9a-90d2-7cac042c4187 | -8.57227 | -47.19471 | 2025-07-11 05:25:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf7cbbca-9919-32eb-b20c-c33315ddaeb5 | -12.02354 | -49.52322 | 2025-07-11 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 453a18c2-73ab-3e63-9bca-f12dde21ed4c | -9.95989 | -64.96601 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fdb1d9ca-9074-3b3c-bbd5-3f6f1ae4436d | -9.04614 | -61.62919 | 2025-07-11 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20ff93e3-9fb0-36d0-ab12-8ba197a5be84 | -10.57675 | -49.14164 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07cb5f66-4a1d-3969-89c0-79c966d83954 | -11.87485 | -58.71711 | 2025-07-11 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6bd0fc8-719c-3b35-b40d-eadb3bdf4990 | -9.64682 | -65.74052 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a58a31e2-86dc-31a3-874f-cd3ef47ed0e9 | -12.02462 | -49.52327 | 2025-07-11 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da0cd06a-c95c-34fe-9955-063fbf551338 | -9.70599 | -56.18332 | 2025-07-11 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 687aaa2c-6d19-355b-a6fd-e85038959988 | -9.33078 | -58.85406 | 2025-07-11 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a695ada-b2f4-3458-94aa-c3fc56e3f6ad | -10.57608 | -49.14746 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d01a5378-3a8a-3fec-b0e2-7eaae2d44a69 | -10.0975 | -60.49537 | 2025-07-11 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a038a4f-7731-306b-a630-f928b5e31c34 | -9.91757 | -47.82686 | 2025-07-11 05:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8b9d79f7-fbb9-3130-a6f2-20c396687de1 | -10.11716 | -65.15163 | 2025-07-11 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 688da586-29fe-374f-881b-f320a64866d4 | -11.87783 | -58.72186 | 2025-07-11 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
