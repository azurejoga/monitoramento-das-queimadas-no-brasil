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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a72a896d-fefc-3ee2-b258-60aab33641d5 | -17.89596 | -57.37724 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 96416606-8a89-369a-b19d-c8e6d27e9c17 | -17.89536 | -57.35819 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 57bb6c01-1067-3e1b-ad74-2e5661ac55eb | -17.89527 | -57.3809 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 97d3fe00-408a-3964-99c2-362b7673dd1f | -17.89408 | -57.3428 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fb919040-1fed-3350-945e-ff2ad93ba5dd | -17.8934 | -57.34645 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 03d1b2ad-61a0-3bd2-860e-ad9b92623c9a | -17.89272 | -57.35009 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0ccd212c-042e-3df0-9065-fb6be01f807b | -17.89204 | -57.35374 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fd779144-cb5d-3372-92cd-db1ce15313fa | -17.89195 | -57.37646 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4ff1bab2-09ad-356d-9379-41ff6c758904 | -17.89136 | -57.3574 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 63dfbe3d-a5f6-38bb-bf6b-d028e99ccc77 | -17.89058 | -57.38379 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e529512f-7727-390c-9f94-fed80ba93c46 | -17.8894 | -57.34565 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0c075f31-889e-3573-9df7-abef7a04e504 | -17.88872 | -57.3493 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f2c042f8-f53b-32b7-a37c-4f42c3d1f1b8 | -17.88804 | -57.35295 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e0eb4726-a8b5-3aa2-8a1f-01f0dc65de90 | -17.88541 | -57.34486 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 55344b9d-c1be-3bd6-8bbe-a1dafd67329e | -17.88472 | -57.3485 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9f78063a-3bf0-3310-ab7d-054e67c2671e | -17.88404 | -57.35215 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 68571ce4-f4c3-3a8b-88a6-1dc91f277fca | -17.88073 | -57.3477 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6316b0f9-bc20-353e-95ca-e8aa4281d273 | -17.87604 | -57.35056 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f3677d4e-bf83-3fc0-8bc3-5e655ed78e32 | -17.87536 | -57.35421 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 71383bd5-d394-3ab0-9d5e-93bcf39682bc | -17.87483 | -57.35029 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 1e7ab725-160c-362c-919d-c614504a7037 | -17.87417 | -57.35395 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f8a2ffd1-78de-3ada-84d3-0553d7a845a4 | -17.87351 | -57.3576 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 117f369f-cf50-3ec1-9c44-506006562bf3 | -17.87329 | -57.36517 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a25b84c2-d374-374a-affa-a6a605f02cc5 | -17.87261 | -57.36882 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e6ca5fa5-3b51-3929-8fe3-1a0cbc400bdb | -17.87218 | -57.36493 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3c6f21ed-c2bb-34bb-9b8c-839d0ed19275 | -17.87152 | -57.36859 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 732f71c0-4781-3d2f-a884-7c0f2fc79ec5 | -17.87136 | -57.35341 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ea81e9f1-05e1-3ba4-ba7d-93816b406367 | -17.8693 | -57.36437 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 71642a35-7fb7-32e2-8d5f-626142215c61 | -17.8686 | -57.36802 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e6d95e5b-a6c2-3d5a-a0e0-f2c59646c10b | -17.86818 | -57.36412 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8659cee0-d94b-3047-9556-1fa5b776ab1b | -17.86752 | -57.36778 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bd3dab9d-2866-3b93-9ffd-3295e741a706 | -17.8655 | -57.356 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7fdbda76-7ace-344e-bb36-befe376d70a3 | -17.86418 | -57.36332 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8ae61dda-f7a8-35ec-9317-32eaba7d5888 | -17.86351 | -57.36698 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 136d4584-ce42-3b66-b19d-a296cb49d68b | -17.85951 | -57.36617 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 319422bf-e466-33e1-826b-797e146366f1 | -17.85884 | -57.36985 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f9061043-a527-34d1-94c7-aaa8c5e9ba94 | -17.85751 | -57.37719 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 57c187ff-1b71-3606-9ab1-39e3e9794c36 | -17.85684 | -57.38086 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 76449d4b-b99f-3a29-a54d-dab25658289c | -17.85617 | -57.38454 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| e286de4d-7be0-375b-be50-669e05c138fa | -17.8555 | -57.38822 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 26154a9f-2b59-3efb-8553-a6c61d5d5656 | -17.85484 | -57.36904 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 60d2025c-de7d-3e68-bdf0-d026913e65a9 | -17.85416 | -57.37272 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 076dcac3-15f4-3b8f-80d5-22bdfc3d401a | -17.8535 | -57.37639 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| a18182bf-e480-3a57-b4ed-3b1d80bdf403 | -17.85283 | -57.38007 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 73ed3f59-e81d-3dd8-abaa-0afb6d35ea89 | -17.85216 | -57.38374 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1c663374-8f47-389a-ae20-79a677cf25c2 | -17.85149 | -57.38742 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 35da6c28-cc9a-3c0e-b4e1-a2ccb444a840 | -17.85016 | -57.37191 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3b47442f-0329-3bc6-9a30-3138c05449bb | -17.84815 | -57.38293 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8ed7ab02-94c1-3a97-a7a0-957179a2bfc8 | -17.84748 | -57.38662 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5fcf6de4-8572-3196-a21e-5e36c72cd54a | -17.84681 | -57.3903 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 90eabc8e-41f9-305f-8356-94fb3375e82a | -17.84615 | -57.37111 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 720906ab-3f7f-3002-adf5-0c2b4c9610f0 | -17.84548 | -57.37478 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 937a94e7-abb1-3ddd-8538-cd3ed05d1acb | -17.84481 | -57.37845 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ac74bdce-549b-32f6-bd11-43387a70e4af | -17.84414 | -57.38213 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 357783c6-2c96-3b3d-8a0c-9c23abcfebf9 | -17.8415 | -57.3285 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 40de08fc-175f-31a1-9fd2-98342372a1ba | -17.84147 | -57.37398 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e103139d-6175-3c60-a293-da0dd2dd3d9e | -17.84081 | -57.37765 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8c7104c1-f61f-3572-9285-4e49d024e8ee | -17.83814 | -57.36951 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f3dad280-6512-3706-9fd0-cb5479852ef9 | -17.84347 | -57.38581 | 2024-10-13 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dd04b967-a6fa-3296-a768-1655f57f4564 | -17.84279 | -57.3895 | 2024-10-13 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1bcf8623-35fc-3654-bbb4-57b3fc057cc5 | -17.994 | -57.37108 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e5562816-d440-3257-a5da-bb8381232a59 | -17.99068 | -57.36665 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3317e221-3af7-31ba-8274-b3a5907019cf | -17.99 | -57.37029 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 42a9d30b-30cb-318f-b042-e85a568c93d6 | -17.98932 | -57.37394 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6f84cb95-3fa9-38be-a57f-fc7114954404 | -17.98737 | -57.36221 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e79ceefa-2a36-3da9-b9a0-6c0a3a6f51d3 | -17.98669 | -57.36585 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 860c793b-ffcd-30f4-88a1-fd9167f80b89 | -17.98463 | -57.37679 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9f396be3-523e-3e84-a1d9-f59f06dbceb7 | -17.98395 | -57.38044 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3b85ea16-f024-3611-87aa-8cc59b00c952 | -17.98338 | -57.36141 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| e49e6a74-fc39-300a-a25d-f696fe80adc5 | -17.98326 | -57.38409 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 922a2ea5-86d9-3b57-b988-6e6740a3187d | -17.98199 | -57.36036 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 038a7c54-0b65-34d8-9446-6d82ad24bd2f | -17.98133 | -57.36402 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 92876ae2-a55f-3867-9227-5b29f8628c4c | -17.98007 | -57.35697 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 4e3b1a95-65ec-3ffb-a035-5cb7a8bb99c7 | -17.97995 | -57.37965 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 43a64ba2-3dfb-3cdf-9f18-d7fe47e34b52 | -17.97938 | -57.36062 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| d63cd7b2-8fb0-3056-aca8-cc84898d1b4f | -17.97926 | -57.3833 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 566823d5-108c-3446-b91a-829f3f6ca78f | -17.97869 | -57.36427 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 79881807-dcd7-3e4b-bf3e-2fbaf9c29c25 | -17.97801 | -57.3679 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 17bb7c8c-89c8-363e-8377-1cd8147cec22 | -17.978 | -57.35956 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 3d98bd19-8e2b-3dbc-ba4e-652fdbf78b72 | -17.97733 | -57.36322 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 978e197b-554e-3262-b204-0e885a566fd8 | -17.97667 | -57.36686 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 7d768012-945e-3494-9b7b-674438ba9cff | -17.97334 | -57.36241 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 0f5b7798-67d2-382d-a0cd-500c24bd8ab9 | -17.97268 | -57.36606 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3e84bdc6-5475-3ba8-b3c2-7ce940f62552 | -17.96868 | -57.36526 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 41854669-c788-3980-9b54-4bd1868fa4c1 | -17.96535 | -57.38355 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| cb629efc-ffc9-3e81-a560-588a04d27124 | -17.96469 | -57.3872 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| d9708ed0-4e7b-37ac-8272-547124695386 | -17.96468 | -57.36446 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| de48a151-9974-3fdf-b42a-f7a5fa1237c8 | -17.96402 | -57.39086 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9b8ddbe1-6e0c-386e-badb-936c20c27113 | -17.96402 | -57.36811 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 197b2eec-b825-3d42-b56c-9b7de1b76715 | -17.96135 | -57.38274 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 3a65baf4-2a08-3d7e-b7dc-310c23101769 | -17.96069 | -57.38639 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| b2657928-e8c6-3042-b3c1-2ad69e202c85 | -17.96068 | -57.36366 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 36a12878-3d93-309d-baea-c388ef270ee2 | -17.96002 | -57.39006 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b290a400-7198-33a6-805a-bac59db48c81 | -17.96002 | -57.36731 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8082cfc1-7da0-3662-8638-66f8d5c186e5 | -17.95935 | -57.37097 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 379bb2b3-197c-3146-a6bb-c0cb80871c5c | -17.95869 | -57.37463 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6ec8be2f-4e3b-3a6f-b90f-86aa4f37620d | -17.95802 | -57.37828 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0d7e4135-a008-369d-a1dd-53176c87f96f | -17.95735 | -57.38194 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| ba15187a-800f-356d-8609-ba62de4bb69f | -17.95668 | -57.3856 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 8943be7a-3b9a-35bb-bf8e-c94e39946198 | -17.95602 | -57.38926 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |


[Clique aqui para ver as próximas entradas](README72.md)
