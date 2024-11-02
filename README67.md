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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f085365f-2ea6-3336-8267-f66a6b545aa2 | -3.84548 | -49.92065 | 2024-11-02 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 083b58e5-2d1e-32b7-aaa8-9050700c881c | -3.76246 | -50.0044 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ece371e-d448-3962-9bb5-62d5293cccb1 | -3.75307 | -50.03953 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e49f014d-883c-3211-b49d-6d6e934583d5 | -3.75016 | -49.94693 | 2024-11-02 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a99cf96-4fe8-39f1-a1f0-1ad20a9cef40 | -3.55717 | -50.3351 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c188f03d-4873-36da-a56d-79fbfd0eae81 | -2.23242 | -50.69982 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4bb7a5fc-8435-36f4-8316-9367adfad16b | 0.13824 | -50.48303 | 2024-11-02 05:04:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7de9eec7-7ad6-3de3-8a2e-3fb166c18bc8 | 0.09915 | -51.24564 | 2024-11-02 05:04:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01871daa-9a50-3031-b9ea-99072ba805ef | 0.06105 | -51.12042 | 2024-11-02 05:04:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03400cc4-6bba-3fef-b466-f21085ee5ae9 | -0.62754 | -50.4463 | 2024-11-02 05:04:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5710c968-66cf-3c4e-8a36-d74a721093d2 | -0.15753 | -51.38623 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 571efd28-41cf-31ef-aad2-fbdaeaad7a4b | -0.12256 | -51.33625 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0822e17e-da33-3949-a675-8373e393fa8d | -1.96271 | -51.41292 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eb99a50-d6dc-34fe-818b-6cbc535a4721 | -1.96176 | -50.74635 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba54e3f3-1e03-3829-9c02-ed195134b22f | -1.87279 | -51.02394 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f9fbab5-6d59-3562-af41-c2e86c9f4045 | -1.86907 | -51.02337 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ed37e47-2e31-33e7-b5c9-ba1482206203 | -1.86765 | -51.18046 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e829aea-526c-3ab9-8780-d4062cc462e2 | -1.86396 | -51.17988 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43d5de78-53ba-3aea-81d4-e34674e0a81f | -1.78974 | -51.10362 | 2024-11-02 05:04:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 255e1a0f-979d-3517-8c52-958b1a9faada | -1.67993 | -50.4135 | 2024-11-02 05:04:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26103555-5eb9-30a0-9614-1903ab3ded2b | -1.58763 | -51.7035 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6782e0ac-9e47-35d3-bbed-841bb422ebb5 | -1.55669 | -51.61924 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1bc643ad-0fb2-3394-9bfd-9575b48ce624 | -1.55311 | -51.61866 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 30a4aa17-660d-3d39-b6be-2b5ab776d12a | -1.55097 | -51.58469 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a3a00aa-35b2-3679-bf75-df2f39cb5dd6 | -1.4512 | -51.47792 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acbc5a97-443f-3e06-86dc-bb195334cc9f | -1.38943 | -51.57986 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d37da9-6514-3034-b12d-362a439c17d7 | -1.37355 | -51.42067 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 505cfc0a-45e9-3220-be75-34f75c22c281 | -1.37291 | -51.42484 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d26b9d6-f2b1-3551-a1a5-a5b8ff65bbbb | -1.37227 | -51.42901 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcfefde1-428e-3bf6-b888-622345280295 | -1.36696 | -51.41537 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dfe98c8-7da0-3682-9660-584f902f7c1d | -1.35973 | -51.41426 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a75788b-04d8-3296-9f6b-1aaa38b01e78 | -1.35547 | -51.41788 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a88c7e8e-4f8d-350d-83d2-8390b25ca85e | -1.35122 | -51.4215 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c7fc228-e9f3-3b08-b4cc-3594c381c988 | -2.26355 | -50.44182 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7c4f74fd-6d74-3d5e-9daa-1f54876a8b3d | -2.25968 | -50.44121 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b87edb4a-7994-37b5-9581-c38372119a7a | -2.25895 | -50.44607 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5c965be7-8690-3024-a927-ede4dd9d8b5e | -2.25581 | -50.44061 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e807b18-e18a-3074-b360-4df57e958e6f | -2.25508 | -50.44547 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 492808b5-cb92-320a-b6ee-1bf5e499cb11 | -2.25267 | -50.43515 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 231dd311-eec7-398c-9772-f929efe0a900 | -2.25194 | -50.44 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32e04420-2093-3e36-925f-b5588dadb99f | -2.25121 | -50.44486 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf03dfc1-df14-3eb7-a255-24eba8e556d4 | -2.24977 | -50.53323 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5762ffc9-983f-3b57-b902-322d1a08d878 | -2.24904 | -50.45935 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2e5582b-a6af-3312-a9b7-14c0b650ced6 | -2.2488 | -50.43455 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a477b1a5-f906-30dc-a30c-87bf3427baa4 | -2.24807 | -50.4394 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c481fea2-36c9-35e8-8c94-4bc7fe6db494 | -2.2452 | -50.53742 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08476509-ad41-361d-950f-2732b10047d3 | -2.24493 | -50.43394 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8f172aad-21a9-3cf1-9f31-80ae12531c83 | -2.2442 | -50.4388 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3394b372-8272-38a6-81df-cfb61742c6e7 | -2.24375 | -50.43198 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff90fdbd-e261-394b-9f95-1d69158ec3ea | -2.24299 | -50.43684 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed2438cf-a604-3dc3-b34b-bf5422fd8d7c | -2.24106 | -50.43332 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce2ad134-8a2c-36d7-aaa0-7f8cee36d09d | -2.17686 | -50.48097 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fdf226b-be3a-300d-b11d-4b505309d10a | -2.16935 | -50.5043 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8cab489-1043-3af3-a3c8-e6e214653f2d | -2.2032 | -50.79027 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c32d09f3-7e74-3b2b-babd-d1b1902adf89 | -2.19143 | -50.86835 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e363356-d1c6-3bb3-b6f4-17df4f0b7eb5 | -2.19115 | -50.79314 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5edcbadf-af01-3b5a-af9c-516507c66f53 | -2.19046 | -50.79773 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 932cf448-f664-3b51-aa99-ab73cc25cfea | -2.15827 | -50.90982 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dfdabb5d-34a8-3ad4-aec2-5f90bf67c1cb | -2.15777 | -50.90761 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1339ffb9-cb78-38a1-bdf3-a618452034fe | -2.15706 | -50.91213 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efdf3db3-eea8-3b9f-803e-a5a1a7b01daf | -2.14747 | -50.99823 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53d05965-c223-35c8-95d3-5f4a9ac135fe | -2.14547 | -50.99553 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1245edf-3c0a-342d-8d8b-f2fa71577bce | -2.14479 | -51.00004 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 803d854a-e98b-33fc-9bb1-183d63531b40 | -2.14373 | -50.99768 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57d8a824-8c8f-3d92-b66a-f16d0450135f | -2.14362 | -50.69848 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc07c3af-e37b-31d7-acc7-c9733ae1d534 | -2.14342 | -50.8261 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ad81934-481f-3ea3-8715-95dcfef267e0 | -2.14232 | -51.00666 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e59fecbf-d327-3046-afe6-a5868a41fae6 | -2.13982 | -50.6979 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b6143b7-fea3-3462-9e0a-445348b6cf1e | -2.13965 | -50.82549 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 638832f4-a360-3d57-9198-0f7f730a1361 | -2.13911 | -50.70255 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d38788e5-6fee-3376-8498-b11b406f4244 | -2.11938 | -50.83177 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93c980e0-ac53-3e9b-8095-ccd68ee8f872 | -2.11868 | -50.83632 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af838325-abf2-3177-a29e-46c9d495f5d2 | -2.11183 | -50.83061 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c6e05e1f-3337-389b-b2b7-0c8d510c4de7 | -2.05125 | -51.1783 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f07f8d6e-0515-3d95-9492-ede56e3ac8a0 | -3.18744 | -51.33498 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fddb1a67-d313-3af9-96ba-f80b8c1cae62 | -3.04853 | -51.78664 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 624e999d-d4ed-3200-8231-581c328722ba | -3.02956 | -51.36969 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84560165-d275-30cb-b791-be81f2820180 | -3.02519 | -51.37353 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29aee08d-d6b1-30d4-a00a-9f42226a5f9b | -3.02452 | -51.37793 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58a221ee-3cfe-304b-869c-98833bdb5390 | -3.02216 | -51.36856 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c1a5425c-202a-3141-9dc8-393a8b1bdb8b | -3.02149 | -51.37296 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 36841ecf-cc8f-3343-86cd-4b1d4d0a2666 | -3.02082 | -51.37735 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| caed0458-cd4b-32d7-a7a9-a4862bfce318 | -3.00869 | -51.57948 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 110e57fb-4840-31a7-9855-4f8a427ca89f | -3.00812 | -51.79947 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4331e810-facf-3136-bd6d-e29e73aca18c | -3.00803 | -51.58377 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce0bbaa9-24cd-387f-8d60-096b7203872a | -3.00569 | -51.57463 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1accf532-105c-380d-be21-99b68bc03938 | -3.0056 | -51.80141 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96888165-e2bd-348f-b0ad-bac25dcd0688 | -3.00516 | -51.79477 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb93793-6974-3d49-85c4-0f8072415f31 | -3.00502 | -51.57896 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0a73024f-c0cc-31fd-92c2-9a0f994a4611 | -3.00451 | -51.79892 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55a757f4-7bc8-3b97-81ba-0b89335886d3 | -3.00437 | -51.58325 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dcccac90-a99c-3cd7-ad88-b61d04ad6b1b | -3.00261 | -51.7967 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50328b25-9897-3f79-9eb3-31248f666cf4 | -3.00203 | -51.57407 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aa35be1-64fe-3b1e-94d0-156b1db92b38 | -3.00137 | -51.57839 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 11a25ba7-0e49-30f7-bd06-04ac52d9f911 | -3.00071 | -51.58267 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b6afd368-e165-3423-aa6b-94c1258798f9 | -2.99904 | -51.56918 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4037d094-a9e5-356c-9d9c-aab2f1b61294 | -2.99772 | -51.5778 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 44dc3a04-7518-3bf4-96de-3ae7ba0ff71c | -2.97465 | -51.43282 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a630fe88-2897-3d76-ba04-49247a8573f4 | -2.97162 | -51.42788 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68a3494b-bfe2-3e80-81b5-26ff2f738e1e | -2.97096 | -51.43226 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README68.md)
