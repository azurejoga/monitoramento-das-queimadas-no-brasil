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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1793e976-3e58-34d9-960d-e6ea7addcff6 | -3.27351 | -52.74287 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d696b1d9-37b0-3991-a287-2f8cbc4f01f2 | -3.22276 | -50.38266 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 29271ff6-a483-33f2-9c68-378204a22129 | -2.43491 | -53.66228 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24fc0aef-d021-3041-852b-403b6562830c | -3.18822 | -50.43978 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3769aff-356a-3569-b91a-c85a152d707d | -2.62007 | -51.74524 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe41ddc2-8339-3bb7-8e60-3bbb6eb8c8e6 | -2.18943 | -53.63493 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a2287a4-f347-3b2c-9b31-066b0940b4b9 | -3.59876 | -47.35104 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5070af8c-0058-3c7d-a5f7-ddc05529a73e | -2.67825 | -51.81688 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4ea53d3b-e95e-3047-b747-d91957ec3bcd | -4.20089 | -45.85416 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f52b7130-d1ab-303f-92f7-cf7fd9890355 | -4.6154 | -49.57673 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80ab7963-264a-3b2d-8ce2-c8dc45c5d25b | -2.73567 | -51.71822 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9c054b3-6f1d-3610-a035-50a1ceede99f | -3.03791 | -50.32301 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 86c25159-e025-3935-b1a0-b774580316b3 | -2.21758 | -53.73153 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce9f5b49-b9ca-3eb1-a6ac-7f1f1957c7a3 | -3.1142 | -50.14747 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d41c8ef0-8d3c-34c9-8328-7cee5f546b83 | -2.13528 | -52.45184 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f602f9e2-e49e-3d33-86c4-db99c42f3b07 | -1.68762 | -54.2552 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea920b13-29a8-391c-9777-9551a0e2fc1a | -3.19135 | -50.58495 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8ca45ac-9513-321e-9de4-c76dba046985 | -2.79621 | -51.59733 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a5d8444-4a0b-32e3-a784-6e9bda24e78e | -4.05751 | -48.24234 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7ef60de-7577-32f6-8247-79816a4b86f9 | -2.10666 | -48.55462 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 346a599b-0315-3fa3-bc9d-e7d4d0eb39b2 | -4.0746 | -54.97434 | 2024-11-09 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75f8f3f1-363d-37d7-a9b9-bbc2b9b04bcf | -2.97366 | -53.27315 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b61baca0-5b69-38d1-b73f-06335da0d0ee | -3.10053 | -53.32884 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 16251b9a-8b02-3bda-95c5-89f6f9b7dcb0 | -2.21393 | -50.68132 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 022b9606-6e92-3bbe-bf1f-3a672d99b222 | -3.52199 | -51.50684 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb02902f-927f-3717-9319-58405203c5d7 | -3.22824 | -50.44192 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fe5668e-5b4d-3436-81a3-ace39e505f6f | -4.56248 | -46.34551 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cae5f81f-01e3-31f1-b385-ef214bd8e88c | -2.86745 | -50.32351 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d52abf46-9513-3520-989d-24f877aa643e | -3.23776 | -51.18857 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a97fd415-dcd4-38c9-8329-1da4664d3ae8 | -1.9547 | -46.30555 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea7cd5fa-f883-3713-891c-4357d567203a | -2.07689 | -52.04504 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6212bb4-2ace-37d4-80a1-87612f6d2ce9 | -1.14427 | -53.64886 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d0f078e-8673-35a2-bfb4-2918dd476428 | -2.68445 | -51.82153 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c24d09b6-7393-3324-9d4e-01c1048ce93d | 0.62587 | -60.0923 | 2024-11-09 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac7dfe1e-9c9d-30e4-a5d8-13f9de94189c | -2.98397 | -53.20767 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19cfa8a0-b135-3099-85ec-ee0772b55c5d | -1.92343 | -48.9347 | 2024-11-09 04:55:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25b7f834-c7e6-3fe5-9988-d1fa37e846ea | -2.15768 | -48.27951 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61fc5764-f5fa-3baa-a1ed-2f99de71857c | -7.00855 | -45.61906 | 2024-11-09 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e91ab86-cb1c-380c-b457-743e7a3a9353 | -1.73098 | -52.4636 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 398d5716-72d5-342d-9d5a-15d78ea8fa06 | -2.10447 | -50.66535 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86c79511-3635-3326-8c38-3db5fb17510b | -1.76274 | -52.68868 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb0dc51c-aca6-3571-a92d-5a6dc57626b2 | -3.04164 | -50.36964 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa74301-b56a-3a2b-912a-0f91bf6a4a58 | -3.94898 | -48.16188 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4fc2d049-0bc3-3af5-8ea2-9ea574d81525 | -2.26883 | -48.06967 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a334e48c-2b4a-3272-8301-df9817bda80e | -3.89389 | -52.19336 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 155bff7d-87ce-3539-95b7-98c05204a958 | -1.05479 | -51.74691 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 774e9549-9d01-37aa-a1e9-57810d8b4206 | -0.22562 | -51.64065 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ca07427d-3e0e-324e-8a93-755e8211c3ff | -3.58605 | -51.20454 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc91e8ac-5d4b-3fe2-91c5-8e28a0ac7e6e | -3.47857 | -54.6799 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63250374-4423-34fd-8779-9dea07652456 | -5.21266 | -48.63342 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1897c818-2e9c-3a3f-bcb4-7cacbe449b8f | -3.02531 | -51.09546 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 141369d6-e0b3-3465-995d-420636a338eb | -4.20653 | -45.84972 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f238ea2-8b9c-3945-a045-210737253cbd | -3.17776 | -50.38833 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29e5ee19-578c-3dc5-a64f-7da93b5a08fb | -0.93458 | -52.44623 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b955af57-b590-301e-b0a4-df54cd93dc3e | -2.83534 | -53.99876 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7171de92-8a60-303d-91ea-e91bfeae6278 | -3.46734 | -51.05865 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a125d06-6d81-3c21-89c7-6b6ce69becbe | -0.16991 | -51.41858 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a856e732-1b03-34da-8c5e-19d8ba87b755 | -3.09719 | -51.32566 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f79b4417-0da0-3e42-8305-65e33648587c | -3.60003 | -47.34279 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3e68aa52-6a11-34cf-9410-3d37617539a7 | -2.24214 | -48.3755 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4fc7504-42f7-3199-aff0-7dd53ff9f5e6 | -2.86449 | -50.31886 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67835952-d5eb-3676-ad8b-5e130953992c | -3.617 | -50.19677 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6957b399-13b9-39b2-a5c3-cf68c2a7b7ef | -2.9229 | -49.35328 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ba50a1f-7271-3c52-b2f0-d6655947ab1d | -2.45025 | -46.30677 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1cec7e63-8997-3ea2-ae01-6a85f6293189 | -3.91922 | -52.20817 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb4c9810-526a-3238-b200-aabc9e259e51 | -2.46761 | -51.15475 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b190d9a1-ba59-3c4f-b946-ee4a830910da | -3.09444 | -53.32436 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9793dec3-31fa-3d31-b226-277fe6ce243a | -1.32952 | -54.59606 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc7a83f5-9dc5-3641-bada-66c5f00e13da | -2.98584 | -50.30244 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4debc27b-6f6e-391f-bca1-bdce4732e2ab | -2.18834 | -53.64185 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd3a3880-9b02-3c28-ab0d-dffcd7dddda2 | -5.98177 | -45.36658 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74e30b06-d7ab-3b7a-916a-53e092aaccf0 | -3.12106 | -51.1053 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd7bfeee-d773-3c11-9acf-ea1195471d86 | -3.59067 | -47.34569 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| a7c12aa7-7542-3626-b0ab-42259412c2ed | -2.23539 | -53.76985 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7ef53086-2363-33e4-bdde-9397e8ddbef6 | -1.94357 | -51.40157 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ded73d0e-a665-33b4-a25d-6f200279833c | -2.63145 | -46.77814 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d6f9eb8-2731-3156-a9a2-d320537cf24b | -3.90143 | -50.3079 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93a5db93-fc84-39de-af3f-72ac4dee9486 | -2.07969 | -52.04909 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 121345ec-f4a2-31f0-8366-0fdfe5e0db0a | -3.32216 | -49.91164 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9c683dc-75fd-3eab-ac0c-bb1b89cbbac8 | -2.17342 | -53.24006 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d77bb44-913e-3443-828f-dcd48b908fa7 | -2.76886 | -54.72326 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7076e64-1451-3bd5-985c-1f92bcfa3d50 | -3.63112 | -51.49981 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6de71b0f-9a99-3179-b82f-f2e314b5fcd1 | -5.44876 | -43.26562 | 2024-11-09 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| acfae10c-cef5-34d0-9fad-6fa6714727ba | -2.30633 | -46.48081 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 171bad0b-2c33-3ac3-ac83-57ce30245aa6 | -2.93907 | -51.53349 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f11d95a2-d5e4-3d91-a005-8166baf99889 | -1.38201 | -52.20328 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d04c21e1-0d7c-3351-9af6-1d3b83336573 | -1.39348 | -52.13007 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1815f9e5-f121-3e6e-9124-b9fc128334f4 | -3.43713 | -50.29857 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 851f4db5-8870-3bf0-9966-b12c8e33f3db | -2.16288 | -53.65207 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7759176a-8ef0-380f-b467-29b6aebb1817 | -1.8125 | -52.26307 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57b33ce2-a10a-33ff-9cd7-51bcf7b4666d | -4.11727 | -48.50624 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 02112700-f34d-3537-8d93-a914f5bfbbd4 | -3.76277 | -51.75797 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e023b2fd-4ff3-3049-a0ae-a5dca4c74dd2 | -2.60475 | -51.30142 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f08fee73-3f88-37fc-8f5a-82d8f79ab934 | -4.39232 | -50.97282 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fd18f1b-b5b5-326c-af67-216af8ab161a | -2.83864 | -53.97788 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ee6f493-22df-3c4a-bd38-4e526f3d71fa | -3.19725 | -48.66313 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74d4aace-f876-34a4-aea2-b11427af69a2 | -1.41268 | -54.77467 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59cf4bb9-6bc5-328d-93cb-70f85db06276 | -5.14724 | -46.20923 | 2024-11-09 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f6de0c6-2f5c-3989-87ab-971228407a31 | -2.71364 | -51.99395 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f336cab3-c847-3510-9f9f-9e90919e838c | -1.32608 | -52.24066 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README78.md)
