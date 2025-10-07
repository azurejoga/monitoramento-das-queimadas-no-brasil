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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 890e1670-b259-38ce-82e4-7a9de0d17028 | -13.5067 | -43.6832 | 2025-10-07 03:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f451493b-99c7-3148-9ae8-91d0b1f23274 | -10.4288 | -50.3305 | 2025-10-07 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 74ccb458-5aaf-3d3e-9421-daa246705f28 | -10.8731 | -51.0289 | 2025-10-07 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1b9640b1-43f6-30f3-bfea-52f17bce4e65 | -14.922 | -51.4507 | 2025-10-07 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 044a3282-64c2-3b9f-9004-155d56087ed5 | -6.4543 | -44.5749 | 2025-10-07 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 3b069836-beea-3b61-abc0-83102a7a5347 | -10.4102 | -50.311 | 2025-10-07 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b98b2829-87d4-3743-8521-ee30a69fca6d | -10.8728 | -51.0501 | 2025-10-07 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b0ba4e3a-6e6b-3da9-a824-0df240c5b760 | -22.0279 | -49.7274 | 2025-10-07 03:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| c5e60b06-8f20-3c24-8a4a-24c7e56cf900 | -4.706 | -45.8493 | 2025-10-07 03:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a0515347-32ea-3672-a6c8-5a36755b1d2d | -4.6875 | -45.828 | 2025-10-07 03:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 89ec8853-09b6-3d79-abee-27cd68c6b8d1 | -22.0077 | -49.709 | 2025-10-07 03:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| e29bb6e4-e522-350f-ad0f-2d119c778fb3 | -3.0864 | -50.5835 | 2025-10-07 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 068eadb0-df4e-3c50-b8f3-85b52a567701 | -10.4099 | -50.3324 | 2025-10-07 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 172b76e9-e34f-3799-b598-d2a4c07b8342 | -4.7061 | -45.8269 | 2025-10-07 03:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ba6ebbc6-6351-3df5-878d-bd7cb9e7f267 | -10.4291 | -50.3091 | 2025-10-07 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 5c21e8cb-63ae-3a09-9989-ae2229c6cfa6 | -13.5072 | -43.6594 | 2025-10-07 03:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 5a1538e5-8436-3064-b3ca-d4bacdbfc8c8 | -4.6687 | -45.8514 | 2025-10-07 03:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ea511839-a08a-3f08-8438-fb510a2f6075 | -18.157 | -53.37 | 2025-10-07 03:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 03d02269-f32b-3d73-aa77-ba35caf1b0f4 | -4.6875 | -45.828 | 2025-10-07 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 137.9 |
| ea8192e0-965c-3178-8eab-631a7d981366 | -4.6873 | -45.8504 | 2025-10-07 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 193.9 |
| 2751f716-8db2-3c3c-a419-1fc14afa687a | -14.7389 | -46.0138 | 2025-10-07 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 8e6e082a-65e8-360f-912f-ced6b53ba4f4 | -18.157 | -53.37 | 2025-10-07 03:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b4540b43-07dd-3dcc-a127-40af338f4818 | -10.8731 | -51.0289 | 2025-10-07 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d8eda6e1-a3d5-362d-bae3-fc70faa61c3d | -6.4543 | -44.5749 | 2025-10-07 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 23727b88-055f-3088-8895-e00cfa595384 | -13.5072 | -43.6594 | 2025-10-07 03:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1dad0e60-1c6e-3d5b-aef4-a9b80ee49e0d | -4.706 | -45.8493 | 2025-10-07 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ae7dd573-b59c-3618-811f-deae7bd26cbe | -14.7384 | -46.037 | 2025-10-07 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 88d0fe95-28f3-35a2-b6b3-776cb224752e | -10.4466 | -50.414 | 2025-10-07 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6ab98a4a-5870-32e8-86ff-d2d2cb0c221f | -11.9496 | -45.4783 | 2025-10-07 03:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4351250c-d5da-3853-8c11-fcfb35f3f702 | -10.4655 | -50.412 | 2025-10-07 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| cd351d2f-3063-316f-9096-58aa5237120f | -10.4102 | -50.311 | 2025-10-07 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 355567e4-5e61-3f0a-9825-893847316075 | -10.4099 | -50.3324 | 2025-10-07 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 064b0c1e-809e-3d67-bd26-c67f2410c7e2 | -22.0071 | -49.7321 | 2025-10-07 03:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| 4ed6507b-5781-3374-a44d-584d7d6b3e2a | -22.0279 | -49.7274 | 2025-10-07 03:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 9470c403-ff41-3d47-aa40-0ba5f73edd57 | -18.1176 | -53.3548 | 2025-10-07 03:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.4 |
| b35be402-22f8-3df5-8324-38f478a25c5a | -14.758 | -46.0335 | 2025-10-07 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 194.9 |
| ff63c9a3-b271-3911-a94b-09e2fd3c1e58 | -14.7775 | -46.03 | 2025-10-07 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 519813df-a148-3ed5-af80-88fe0d5bf700 | -14.7575 | -46.0566 | 2025-10-07 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 37ef9dc9-d8fc-3ef6-8cce-15eac48651e0 | -5.852 | -42.8608 | 2025-10-07 03:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 17217d12-f920-3cc0-9a21-44d6af66f93f | -22.0077 | -49.709 | 2025-10-07 03:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| f378d8f0-6b84-3db2-82e5-3f1141a98b50 | -14.777 | -46.0532 | 2025-10-07 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 212.4 |
| c96de6f9-56cc-3439-b88c-4fe549fca2ce | -12.2585 | -56.6842 | 2025-10-07 03:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 12715dee-8a4d-356d-be88-aa8165cca07b | -7.70031 | -42.39862 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d804fb47-527d-3e2d-9f77-80d833cf9545 | -10.1816 | -40.95848 | 2025-10-07 03:15:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3abfa970-f76e-3ea1-b7c3-352e514f9f2a | -7.6839 | -42.40979 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 94652f44-685a-386a-be27-4decb98b4141 | -6.15363 | -42.59167 | 2025-10-07 03:15:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5e092d47-c754-37ac-bf90-c4147e2d3b0b | -7.01734 | -42.7854 | 2025-10-07 03:15:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2cfbb0a5-43f7-35d3-94d6-5d49ffc7d0ed | -7.68266 | -42.41631 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 55970e2e-eb62-3778-93c5-9166b512bf26 | -6.982 | -42.86948 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a9e47c20-a484-3cca-a0e8-391e265992d9 | -7.68207 | -42.41615 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8f507ae0-7ca8-32e5-bf56-b2600d6c0b10 | -5.20296 | -37.63051 | 2025-10-07 03:15:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f18a940f-348f-367c-8d90-119edff1d089 | -7.67619 | -42.59273 | 2025-10-07 03:15:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 407e68b8-b6a9-3605-819a-0ce9a111c4ac | -6.64746 | -39.31046 | 2025-10-07 03:15:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ef69e8ea-9937-3f6b-bdf5-a8006413742d | -6.71968 | -42.84324 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46fe7ea5-6285-3385-8cd0-267a11d7a720 | -6.98588 | -42.87478 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d4274450-df4a-367b-98cd-01bc63cee252 | -7.69164 | -42.40384 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee9250c9-1374-3bc7-ae5d-9a03e1fc213a | -5.20888 | -37.6281 | 2025-10-07 03:15:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eed8e99b-41b9-352a-8a3a-cd2529547d04 | -7.78573 | -42.61638 | 2025-10-07 03:15:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 51296cf5-3fd4-362b-a0b8-32e5911345be | -5.38873 | -40.99776 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d1e68645-2bda-38f5-ae0d-ec3e816e2a3a | -7.69986 | -42.39843 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 856df463-7e96-3abf-9300-75bbd8d143cd | -5.38875 | -40.98607 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91f898f7-4663-3048-be62-824fa2418d1e | -5.37452 | -41.00112 | 2025-10-07 03:15:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5a1d811c-cfde-3a2b-9500-ad227463f517 | -7.67761 | -42.58545 | 2025-10-07 03:15:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4874b534-ef65-370f-911d-3bee66315a67 | -5.38763 | -40.99209 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 631bd108-a876-3901-a8a9-7ddafc3a08d7 | -6.98063 | -42.87653 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 23bf6674-5935-3f19-b17f-4af4dbb5c3c3 | -7.69029 | -42.41074 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e0bc9498-bb15-3211-90cb-a41a1f61941f | -9.30084 | -40.22562 | 2025-10-07 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 50bc0efb-282b-3466-9dc4-b2706ea7f451 | -7.46238 | -42.63105 | 2025-10-07 03:15:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fc550845-ecfe-309e-a7be-49e0f15eab4f | -7.68335 | -42.40964 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2eded397-6e29-3d64-9a47-4d9dc5b25a21 | -6.65254 | -39.31565 | 2025-10-07 03:15:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a295183a-936f-3a5d-98e3-6d11f350d2a2 | -6.72101 | -42.83621 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9505f908-96c9-3e6a-875f-b11a2185c2ac | -8.38338 | -41.85332 | 2025-10-07 03:15:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa5dae79-eac1-375c-853a-8445b925f20b | -6.15941 | -42.60004 | 2025-10-07 03:15:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 16386a32-e5fa-3a03-98b4-afb3ae185b15 | -5.3898 | -40.99173 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4478666-35d4-32e7-8f3e-702b4e45b398 | -7.69214 | -42.40403 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7cbf21af-33bd-3649-a12d-4c55d459903c | -6.97739 | -42.88049 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03c166db-9777-3281-bfd6-88ba1400384c | -5.38652 | -40.99807 | 2025-10-07 03:15:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 646d8d72-ac75-3391-9f10-787085cdf3cb | -6.98456 | -42.88181 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 608cf668-b8ec-369a-99e4-f10786ef61b1 | -6.15777 | -42.59318 | 2025-10-07 03:15:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 771501b2-c0d6-375d-a687-848cb7939ce4 | -7.69083 | -42.41094 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cb23b60c-647c-3ec7-89f9-376e3088cb78 | -6.16083 | -42.59266 | 2025-10-07 03:15:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac1eeb2c-f69d-3c94-91ed-438a3d63ea50 | -7.46362 | -42.62466 | 2025-10-07 03:15:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e6ddbe20-8024-36d7-9688-b0cc967aae42 | -7.01599 | -42.79267 | 2025-10-07 03:15:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a25930b0-4e5a-33ca-96b9-0edb58386026 | -7.68903 | -42.41713 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ee10d46f-fbea-39b0-8464-6ec6c756e4dc | -6.98719 | -42.86776 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 13570f51-2c74-33a3-87a0-1168a0edfb0b | -7.00423 | -42.79295 | 2025-10-07 03:15:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| adb340b2-93ed-3f4f-b72f-61917c4f4781 | -7.01982 | -42.78864 | 2025-10-07 03:15:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 647f2cff-34b4-39bd-98fb-55a86690a18b | -7.68962 | -42.41732 | 2025-10-07 03:15:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ea3f963f-0ea5-3e20-9e47-dc131a7c832b | -8.38227 | -41.85906 | 2025-10-07 03:15:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e9ce3d9-5c70-328e-bfd2-7db90680f769 | -10.08913 | -40.78453 | 2025-10-07 03:15:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d2eecd9-9f8d-3349-97e1-d24a2f85e7fd | -6.97928 | -42.88348 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b2b37f87-f632-3dd1-9eac-0e2aa41f0226 | -7.01269 | -42.78736 | 2025-10-07 03:15:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b5fdb017-6382-381e-bc42-561bf78d4ba6 | -6.15226 | -42.59878 | 2025-10-07 03:15:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f0df1c20-c75e-3f78-a602-9ed736b3006a | -4.42882 | -38.96651 | 2025-10-07 03:15:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3f19150e-a74b-3968-8c51-954cad4ce31a | -6.15644 | -42.60041 | 2025-10-07 03:15:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 67f00f7b-79e5-3e5a-9ead-23c1842a626a | -6.64671 | -39.31466 | 2025-10-07 03:15:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2960da77-090e-30cb-bb79-a3b18c28dd08 | -6.97871 | -42.87349 | 2025-10-07 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bddb45f8-8ff9-31fa-a459-c82ec57e336d | -10.09003 | -40.77992 | 2025-10-07 03:15:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 174cc90b-1506-3645-b81d-bca1be6b7821 | -5.20354 | -37.62714 | 2025-10-07 03:15:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eaff1d43-0062-3cea-9ae9-5b356c97e2c9 | -9.29882 | -40.2245 | 2025-10-07 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |


[Clique aqui para ver as próximas entradas](README17.md)
