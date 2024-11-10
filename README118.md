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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea557d8d-d4c9-3a5c-8ef9-793760d2ae7a | -17.62877 | -57.50671 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9932b1d7-ca3a-33ed-a95c-e2b5a380daa1 | -17.62806 | -57.51054 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6628d32b-496c-330e-aed8-5b96d7983aeb | -17.61701 | -57.52424 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| ed57b83e-1fb3-34a8-b191-71788a894ade | -23.90733 | -54.07315 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 65a53b75-b9f2-31b7-bfa3-336d93574b70 | -23.86712 | -54.05441 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 35461c7b-865a-3f2b-853e-32860d97056a | -23.86379 | -54.05377 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 20ba3bc3-3026-3890-9a31-e2356efd03ba | -25.18045 | -52.03909 | 2024-11-10 04:44:00 | NPP-375D | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 00c981e5-8ebb-3476-b50e-e31384fd8dde | -23.91101 | -54.05036 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7a438d42-c4d3-3ea7-88ab-43cd156588ca | -23.84593 | -54.78551 | 2024-11-10 04:44:00 | NPP-375D | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0800f5de-22f8-3f3b-9e0a-8d8266817cc7 | -23.90005 | -54.07568 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 33016fec-b84b-37be-bb4e-47808d885ae9 | -25.18163 | -52.03665 | 2024-11-10 04:44:00 | NPP-375D | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1f2d88bb-5a64-3c3c-8439-6f8a89adaedf | -23.91435 | -54.05099 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| d66dab97-e01a-3d95-bf9a-01bf6bb526e2 | -23.90795 | -54.06935 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| d1fa9a36-be4d-324d-b949-1d49d3cf7465 | -23.86773 | -54.05061 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 04211d15-ee8e-3151-8d6d-9cab62931e75 | -23.87107 | -54.05124 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 690c4925-183b-3fb8-8b97-6ae40d6f7cdb | -23.91707 | -54.05542 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 40280fa2-1487-3cde-ab1d-4955b7908fda | -23.91373 | -54.05479 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 018b44fd-7a09-3f5e-ad16-56a4252fe4f1 | -23.904 | -54.07251 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| a3382627-6a38-38f7-8a81-50c8fe647129 | -23.91646 | -54.05922 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5348efc0-47bb-3e5b-a60c-fde6287f7cb2 | -23.90856 | -54.06555 | 2024-11-10 04:44:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 254d89c6-898d-3523-a0e2-92706b19f8d3 | -3.2169 | -50.2651 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9062fed5-c62b-3c0f-87cf-3adff577479e | -1.5347 | -52.2104 | 2024-11-10 04:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1ce70559-e874-3687-8274-2c1462f59941 | -3.9668 | -48.1932 | 2024-11-10 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7e365bbd-6855-34c8-84ad-ea58c41e2d34 | -3.9669 | -48.1716 | 2024-11-10 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 001095c1-427b-390c-8056-72a63439c007 | -3.1423 | -50.4352 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 3dd871b4-ba69-3a27-a165-2bd34c200b9c | -17.627 | -57.5075 | 2024-11-10 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 189.4 |
| cd705c14-821b-3ef2-bf36-43caa4ba0c56 | -3.1239 | -50.4358 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 199.8 |
| 16309463-64f1-3b75-8188-2df0428e6b23 | -3.1238 | -50.4568 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 34cadbaf-ae50-388f-8020-b4198bafefcc | -2.7587 | -49.3497 | 2024-11-10 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 783848bb-1b6e-356c-8560-f4761888a84e | -17.2933 | -57.4857 | 2024-11-10 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| e4af13b7-b501-3e5c-89c6-8a9d8b933891 | -17.6073 | -57.5099 | 2024-11-10 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 303.3 |
| c3426a69-4f28-3071-80d2-63e82adbd151 | -2.9171 | -51.4825 | 2024-11-10 04:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b2a5c550-4420-3dc6-bac4-82c62401ed07 | -3.2244 | -53.0524 | 2024-11-10 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| bb6f610c-1cfb-34c3-a5dc-5f6f189ffc08 | -3.9485 | -48.1508 | 2024-11-10 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 7517c41d-74df-3990-985b-ee5e1620a12b | -3.2352 | -50.3065 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 821bb409-52bd-30eb-989c-db68798fb4ac | -2.931 | -52.7753 | 2024-11-10 04:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 5a0de0f4-47e8-3af1-a45c-9f159772b683 | -3.2243 | -53.0727 | 2024-11-10 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1f426974-a453-3a1b-b06e-6403dfb4687e | -2.8803 | -51.4628 | 2024-11-10 04:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2d254d00-763a-30de-b6af-d91895300a56 | -2.9355 | -51.482 | 2024-11-10 04:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a21cd1e1-2581-3f86-b60a-110c1fa99c7f | -2.0953 | -48.8338 | 2024-11-10 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 47b1aa19-1e18-304d-ac60-68804ba85d7a | -3.9483 | -48.1724 | 2024-11-10 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a8961f2f-c043-3b59-abe5-fec01553f1b3 | -2.8802 | -51.4835 | 2024-11-10 04:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 100dd086-422b-3e8c-b732-248ec7693e6e | -3.2168 | -50.2861 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| b76da965-eb51-3423-a2b5-ee1b0dbb7c72 | -3.2536 | -50.3059 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1ccc9b6e-e88e-3bf4-98ba-f8902bfbdd18 | -2.418 | -46.3024 | 2024-11-10 04:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9b733922-f60c-3d47-9abb-9f40bd6e19fb | -3.2353 | -50.2645 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| aa3c9b2c-05ca-32b4-9a29-cd0288764c2c | -17.293 | -57.5062 | 2024-11-10 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| de3fc177-2e60-39c2-bc84-d0376ef0ea5a | -3.5064 | -44.0294 | 2024-11-10 04:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2685398a-ebd0-3fa1-8116-aec103bcfa69 | -3.2352 | -50.2855 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| db87e441-3076-35ba-ad06-4a74e50f186d | -2.7772 | -49.3492 | 2024-11-10 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| bde5c51f-260e-3116-b79b-efc1d028f766 | -17.6069 | -57.5304 | 2024-11-10 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 307.7 |
| e58d515a-f7fe-38f1-b514-0b53e5f740f4 | -17.6266 | -57.5281 | 2024-11-10 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 200.6 |
| 2debfbfb-7df5-379b-9436-83c8b659c88f | -3.1422 | -50.4562 | 2024-11-10 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 5daae48c-f1e3-347b-88de-b6ee48f8f2a1 | -17.2933 | -57.4857 | 2024-11-10 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 23405bfb-7e51-3673-9e0b-b4bef26d3881 | -2.9355 | -51.482 | 2024-11-10 05:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fdb4f37d-dde2-3445-90e8-d84eb3f1bb81 | -1.5347 | -52.2104 | 2024-11-10 05:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a43e1cf5-ef3e-31f9-b174-5dd877a63f2d | -2.7587 | -49.3497 | 2024-11-10 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f1e953e5-cdcf-347a-aace-7c77e90ccb1f | -17.6069 | -57.5304 | 2024-11-10 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 312.8 |
| 05722322-4b36-3baf-9da6-d723ee45434b | -2.931 | -52.7753 | 2024-11-10 05:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 8f7dd780-2657-33a4-b2fe-5e17ee864c26 | -2.9494 | -52.7748 | 2024-11-10 05:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 73e3caa2-7c8d-3c39-a428-afc4f608af6b | -3.9669 | -48.1716 | 2024-11-10 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 0386342c-0ca9-308f-b6be-10ec4113465c | -3.1239 | -50.4358 | 2024-11-10 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 759d05cb-dd8e-3a08-8216-b4b86742dcdb | -3.1423 | -50.4352 | 2024-11-10 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 261.8 |
| 0ae512b6-b03a-3747-baad-8d416e0796c1 | -3.9668 | -48.1932 | 2024-11-10 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 37b54291-9530-3d0f-907c-1b44ee617779 | -2.7772 | -49.3492 | 2024-11-10 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 81afd1d6-93c3-3aef-949f-255ff36158ce | -3.2243 | -53.0727 | 2024-11-10 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 88ae868a-c838-3d1e-9f80-a4dc324f6443 | -3.2244 | -53.0524 | 2024-11-10 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 944c0772-fb61-37df-970e-31e042de3079 | -3.1238 | -50.4568 | 2024-11-10 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 54d47369-585f-33f0-8f1a-f44d6f2f116e | -17.627 | -57.5075 | 2024-11-10 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.1 |
| ce3967dd-8c39-3ed4-94fd-13b39d992ebf | -3.1422 | -50.4562 | 2024-11-10 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 8067df82-f2a7-3848-ad2e-42885205ace2 | -17.6073 | -57.5099 | 2024-11-10 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 286.2 |
| 43db8fa7-1172-3eb5-89c3-20f488a77ddb | -17.6266 | -57.5281 | 2024-11-10 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 192.8 |
| 575b8319-584d-3fa4-92b6-94c379edfb59 | -3.9483 | -48.1724 | 2024-11-10 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| dcb749ba-1c01-3701-82c8-b40f6c14610d | -3.9485 | -48.1508 | 2024-11-10 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 3d33dce9-4232-30f6-a6b9-f25d2ded1d63 | -8.39 | -44.16 | 2024-11-10 05:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 227462bf-16a8-383d-bc6e-b47cdfa82cae | -8.39 | -44.12 | 2024-11-10 05:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ecd0266-5fbe-395e-b69a-c91bf44b5518 | -3.23 | -50.26 | 2024-11-10 05:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e9f54cc-818e-3c04-94f4-2859684670ed | -3.5064 | -44.0294 | 2024-11-10 05:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 32a71cfc-02dc-3213-bb92-9a682f589302 | -3.1238 | -50.4568 | 2024-11-10 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 3bebae9e-9b1e-38b0-9e34-beb1b62376c6 | -2.0953 | -48.8338 | 2024-11-10 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 597cc411-8bb2-3466-a1bf-76e3ba030796 | -2.931 | -52.7753 | 2024-11-10 05:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bdac6954-8e45-3dbf-87ca-331a1bd13612 | -3.1239 | -50.4358 | 2024-11-10 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| dbafee72-7227-3be1-aac6-a63df78fe8f8 | -1.5347 | -52.2104 | 2024-11-10 05:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3430a5c7-6a0a-3cbe-9ce9-a25b86e5566e | -3.1422 | -50.4562 | 2024-11-10 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 7e56f102-a79d-3c9a-a79b-717927d8ed5d | -3.1423 | -50.4352 | 2024-11-10 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 250ca561-d67d-3b48-b1a8-603841c800e7 | -3.9485 | -48.1508 | 2024-11-10 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 43a3f4b9-0dc0-3f7a-9c5e-f6fbf752eb83 | -2.8802 | -51.4835 | 2024-11-10 05:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 29bbfebe-c994-33c3-b843-3a87df83f835 | -3.9669 | -48.1716 | 2024-11-10 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 6cb3facd-bc98-3b54-8f3b-d1e176d23aa2 | -3.2244 | -53.0524 | 2024-11-10 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| cf09fc0e-c709-3aeb-9fc8-5b99eb383f69 | -3.9483 | -48.1724 | 2024-11-10 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 37980f4f-e261-3b7a-881b-e36a00f88fec | -3.9668 | -48.1932 | 2024-11-10 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fac13c37-7f62-357f-a9cd-077d01df2c79 | -2.7587 | -49.3497 | 2024-11-10 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8340736c-52b0-3044-bd94-2db8b8b3e24c | -2.7772 | -49.3492 | 2024-11-10 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b98a6f48-e979-36b6-8d77-bacc57715cbb | -3.2243 | -53.0727 | 2024-11-10 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cc1e0368-ff06-305a-ba38-75548a6ccee5 | -2.9355 | -51.482 | 2024-11-10 05:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 26c665af-0b63-3810-bfe4-8e5f63754b89 | -2.7587 | -49.3497 | 2024-11-10 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f038de19-0329-3d61-9d8a-7bda3d265606 | -3.1238 | -50.4568 | 2024-11-10 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f3f2c266-e33e-3348-ba53-10c865858bfd | -3.9485 | -48.1508 | 2024-11-10 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| dbb78579-9040-33a5-ab69-2da6a51c6d52 | -3.2244 | -53.0524 | 2024-11-10 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9c8fd03f-8038-3c62-9392-bdce888046c8 | -3.9483 | -48.1724 | 2024-11-10 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |


[Clique aqui para ver as próximas entradas](README119.md)
