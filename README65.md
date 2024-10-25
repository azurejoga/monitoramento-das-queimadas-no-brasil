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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fef6c2f-204f-3c9c-a9d5-cf7b44a74c8e | -3.51784 | -51.06375 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11cc6b59-c28b-3de0-be32-78f0c2402723 | -3.51723 | -51.06761 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 295be921-f7ed-3234-8a15-0d1c33a4172a | -3.51434 | -51.06321 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38d991b3-76fb-3076-ac8c-8d4105f08bc6 | -3.51373 | -51.06706 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25a283cf-d099-33a5-aabf-66cfbb52f6b8 | -3.51312 | -51.07091 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df745ca2-081f-3837-80bf-7f8287c5b228 | -3.51024 | -51.06652 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3375013-6573-3601-a957-b138a0bd6d39 | -3.45297 | -51.5884 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a2d3b76-536c-37f9-b933-9bca7534a39e | -2.30061 | -50.82774 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4adbb1b1-cb2f-3100-9191-a8f002f86a9d | -2.29683 | -51.28439 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d9c4a8f-bf31-38d9-86e0-5015377c78cb | -2.29462 | -50.84268 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c3726b6-2ea4-3755-bae7-48dada4be9eb | -2.29054 | -51.13956 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b7ea5ee-a09c-3b0b-aff5-e21f8f2fe6f9 | -2.28774 | -50.42947 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c91d60b4-62dc-3325-876c-5a2f80e0a7bc | -2.28715 | -50.4332 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd0c4f71-2428-3e25-96ce-caf969aa6ddb | -2.287 | -51.13898 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb8be349-024b-33b5-b0b1-b39ae8f908b1 | -2.28345 | -51.13843 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a0e6f99-ede6-3487-b89a-401e0c4e180f | -2.27787 | -50.44708 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14df0792-4ad4-3640-820a-589821c93596 | -2.27728 | -50.45083 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e482c75-4159-3e12-94ab-fe16267b8dde | -2.27442 | -50.44654 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 570f8178-1dc8-351a-a290-56c605751099 | -2.27383 | -50.45028 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21e4b1a2-63d1-3e6d-b3e8-c2279fac37f9 | -2.22813 | -50.94073 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2c85e29-64ee-3148-8ca8-0cdabcfe1a1e | -2.22049 | -51.67416 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0db09b5a-2ca0-3855-b298-578602ad968e | -3.34728 | -51.65104 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eadaddbd-d724-3657-a80a-0349243b5e4b | -3.34435 | -51.6464 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 961d4501-2364-37ff-b5c1-6296c3657201 | -3.34368 | -51.65049 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87f76cd5-4324-3187-998f-39c6743d0776 | -3.34309 | -51.64772 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 855625d9-7b57-3f49-a264-b02d0b20a10f | -3.34244 | -51.65181 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ce72817-76b9-33e6-aef1-cafed1e1d9eb | -3.31136 | -51.63861 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d40075d-667e-3919-bd84-e7c73284fdc9 | -3.30777 | -51.63803 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a451d1c8-d529-38e3-992f-42460cd817fd | -3.30645 | -51.05516 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e58e869b-5d8a-3e37-8e87-efd820496654 | -3.29762 | -50.75244 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2f76402-8d87-3b4d-ba09-7690c8fbb751 | -3.29537 | -50.74435 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ae8570c-80ee-3c94-a298-026a25c3338d | -3.29477 | -50.74812 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a45294f-0c3b-3b62-9f9e-c74980d61af2 | -3.29131 | -50.74758 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ebb1efd-76e9-3020-a48b-ca0b390effc7 | -3.28456 | -50.94516 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df19c3e9-b7c9-3226-9fec-ad965f2cfb61 | -3.26915 | -50.77502 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e9b1ec2-1ec4-31be-b4e8-266a0096645f | -3.2663 | -50.77069 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc34cd2b-9281-3009-8224-928cf76a6e74 | -3.26569 | -50.77447 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a6de2c6-89b1-3bb9-a69a-ccd39ce80f45 | -3.26465 | -50.77122 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6df5eaaa-6d6f-3096-8334-cb8a9793179c | -3.26406 | -50.775 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 28a46737-bebf-31a4-8470-4a28b2f67268 | -3.26223 | -50.77392 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8638df73-36e3-35e4-a5b7-8ba27418e4ae | -3.2606 | -50.77445 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc2f0283-cc1e-3a8c-b3da-64b7fe31ce2f | -3.2417 | -50.84927 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52f62149-b508-33b5-9584-17b9930210db | -3.23823 | -50.84871 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03dd7e1f-bc8d-3172-901c-686992e1abc7 | -3.21633 | -51.01021 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cd1715c-d1b5-3dad-acc9-0befd0652dd1 | -3.20314 | -51.34028 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7408f02-348c-346c-8654-11957b6a721b | -3.2025 | -51.34426 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7f31306-da5c-3cc7-b6ec-70f7fae74212 | -3.19435 | -51.21844 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c818053-8354-3ab9-84dd-ab34f0f644c0 | -3.19401 | -51.21724 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731e8842-7da2-37a9-8df3-deb9f9853294 | -2.89934 | -50.73493 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50cb5415-803a-36e3-a87a-5067aeceffd1 | -2.41305 | -50.47923 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a43d7b5f-f6c3-3ec3-bd46-3ffb0d537d81 | -2.40978 | -50.5673 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63ab4056-e786-3415-ae98-9a6692a6005e | -2.4096 | -50.47869 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45ce22d9-158a-34f4-8a02-055f24a315ac | -3.16882 | -51.24264 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e10699b-e9ab-3686-aff0-cab2f7f6c77e | -3.08597 | -51.2618 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d406d11d-6a67-3529-b3ae-e694624eff18 | -3.08534 | -51.26575 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82f875b8-de57-3ea3-bc59-8b28ddcc4d6e | -3.08244 | -51.26125 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e5faa90-e705-3160-8028-dd32eff87b87 | -3.0818 | -51.26519 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49eeb385-1c81-3189-991b-34aadabfbcfa | -3.06919 | -51.25602 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c939111-64d9-326e-9d1f-979fa7dcd240 | -2.99863 | -52.00825 | 2024-10-25 04:38:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 908d1836-e38b-37fd-a7b8-84beef31ac8e | -2.87939 | -51.31287 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a085bd67-4bc8-39dd-947a-e1ba94b5a478 | -2.87708 | -51.01071 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72aa2754-c227-3cc8-8f3e-1198a2650041 | -2.87583 | -51.31231 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 962cd30b-21fc-33b4-9b5b-a1f721bb60e4 | -2.86674 | -51.59778 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d350e581-6836-37e2-a7d1-d447461374a6 | -2.86314 | -51.59721 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e2af417-c9aa-327f-94f8-689b8736d380 | -2.86181 | -51.01628 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b0b7d0a-4933-3892-92af-9be123739526 | -2.8612 | -51.02013 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7940734-2eea-33cd-afff-55c9d4317ff6 | -2.85887 | -51.60077 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78662a04-7101-36f1-92be-888015304568 | -2.85192 | -51.28503 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f39bde4-fb26-3e91-a292-d86784768979 | -2.83712 | -51.80669 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838be8bd-3857-3270-9b60-ab977e0ff439 | -2.83645 | -51.8109 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ef346bf7-e409-3783-b314-7c2d357c564f | -2.83347 | -51.80612 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efef0d7e-302c-3d32-9f82-7bc2df293138 | -2.8328 | -51.81033 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ad7c601d-5672-312f-86d0-bb3b55303ce7 | -2.83213 | -51.81455 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9c6d593a-fc95-3313-844d-e4311fe500ec | -2.82915 | -51.80976 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9c585ab9-1ab7-3a4d-bc33-70d539040a99 | -2.81563 | -51.35319 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b5df0a-be18-3e24-8fc2-f41d6053d741 | -2.81206 | -51.35262 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1063db71-0dab-3e9e-a561-c39e03903ac0 | -2.81142 | -51.35664 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce7e3405-3013-3d48-bcdd-32903164cd4c | -2.80786 | -51.35608 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e982732d-394c-3598-ae06-a25bfe910028 | -2.80301 | -51.36357 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3aa3a3f-e1fc-3244-89e3-0fee316e3cde | -2.80278 | -51.59757 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aaba71d-7942-3077-9832-16411fb36d83 | -2.79918 | -51.59697 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 828bdb76-25e1-353c-aafa-4d80f5bb9813 | -2.79853 | -51.60107 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3acf099e-4597-34ec-b6b8-e7c8eff55deb | -2.79524 | -51.36646 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3997da5c-6575-37ee-b329-caa4e6672527 | -2.79231 | -51.36187 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f69a7cc-36d7-32a6-8365-9fdf32da71af | -2.79167 | -51.3659 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79290361-54b1-3eee-a24e-bdafd192ae06 | -2.7391 | -51.62552 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68c791fc-fb9b-3b24-a603-bd36358ce01c | -2.60745 | -51.77291 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b9e90d-275c-3446-a18b-232e19d4f139 | -2.60312 | -51.77657 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89589b9a-0cb0-3341-a0b3-9095eda9cf63 | -2.5844 | -51.94012 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01c9a91e-3558-36c6-9ae7-988e22fb7a18 | -2.5835 | -51.9222 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4bd68a6-b68f-3c19-8b3b-bf0014a37598 | -2.55652 | -51.23178 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3ca093-e12a-3967-91ce-519a6908af38 | -4.67034 | -50.97116 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0baa5ed-f3ed-3847-b94a-ee75db2617d3 | -4.6675 | -50.96685 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6fc9d573-9de9-37e8-aefa-0780ed632cc8 | -4.66406 | -50.9663 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50a3a28b-d11c-3f46-a97a-72a0bd43753c | -4.64456 | -50.91764 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 864149aa-7449-38f0-a3ae-68c0ef2d3806 | -4.64111 | -50.91713 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| baa6920a-1f04-377a-8a77-81f2eb22698d | -4.57136 | -50.95591 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45983a70-cf04-3a0c-b781-a8e33202670b | -4.53668 | -50.97359 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 70a6ed2a-5452-3e80-9799-d4d5e1843c90 | -3.95154 | -52.25136 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74b689a7-0093-3766-9e93-502807c22acd | -3.95084 | -52.25571 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README66.md)
