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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20fbd7a2-c648-3604-9cd3-da7eae557496 | -1.15607 | -53.57623 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79b4a9e8-675d-3543-8bf2-1f63b04a8836 | 1.97413 | -60.91701 | 2024-11-29 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d026f99b-37d6-3b84-a689-65ce11868343 | -0.94895 | -51.65567 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 415ba74f-53ac-37f2-9e1b-b1cfad5bee86 | -1.53161 | -52.66814 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47a6a7c8-ed78-3627-9646-2460a2b3d812 | -1.4094 | -51.58601 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ec24fec-0be8-3007-b78a-00fcfd0022d9 | -1.34878 | -51.96653 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4dcc70f-d27e-3b5c-a107-015435b8ab21 | -1.08762 | -54.04053 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fbf124b-b49c-365a-aba3-6b16f58e14bb | -1.60063 | -52.28884 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fc8d5430-6ba8-3a3e-8345-fc65163c2922 | 1.48593 | -55.96075 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 801d362b-d46a-3af5-9ee9-0a931dad08cc | 1.45826 | -55.9243 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835da246-0ec0-343b-b232-edb60f40460e | -1.33887 | -51.93518 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93741348-7b21-3296-aced-e9469dc6a210 | -1.2688 | -52.19799 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a384954c-52f1-3f11-8a62-65512eeaba9b | -1.47783 | -52.65517 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6829852-6ea5-380b-99bd-78508f9909aa | 1.28513 | -55.94492 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6856c8e-511b-39c9-ae32-2936d5ffa144 | 2.251 | -60.65808 | 2024-11-29 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e5e084-4191-3ea7-9e2b-73f24ee8c8f5 | -0.79721 | -53.0601 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd4739cd-b1f4-359e-a666-bdab3d3e1389 | -1.20616 | -51.62309 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34563fb3-4af8-3618-b76a-378856b7d360 | -1.48816 | -52.41229 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6898c51a-6b7c-36ad-a96f-6a3784d283cd | -1.08555 | -53.64043 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fe6593e-1000-35ac-ab0b-b574d8b883a3 | 0.98309 | -50.25383 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cf950f3-7363-3db5-a245-858f7194e3cc | -0.26596 | -51.49045 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 450455ca-4d07-3c5e-b8f1-4b8f2bdc0715 | -1.12234 | -53.73699 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c57ee6ed-822e-37e8-ada2-bb52c2d89d70 | -1.34474 | -51.99186 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69438e01-b69c-3c50-8cf7-12ee5c4df265 | -1.68062 | -45.79642 | 2024-11-29 05:20:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5411296a-f46a-3e82-8b55-abb25ac76d81 | -1.31541 | -52.86658 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ad498ca-269d-3d96-acb3-11b24e24ee77 | 0.98272 | -50.12095 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a835f94-9f07-31d7-b6a7-1b3c5b4b3675 | -1.26062 | -51.59317 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e82347a6-d102-3609-8055-5cc5a45ac85d | -1.50629 | -52.56078 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b36f4431-89a3-3f42-ac29-1679509a5550 | -1.25914 | -54.54443 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9159747c-ebc3-39c5-bf9b-17b6b223829f | 1.23274 | -55.93663 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7544ee6-6200-3a37-ab57-f39fe8a015d2 | -1.14801 | -53.68286 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 892f04d4-f7e8-39bc-8bfb-1e1d924cc9dd | -1.15217 | -53.68382 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb5d9401-dedb-3d45-9548-32dcfd7dfb13 | -1.08913 | -53.64531 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b047a2ba-2c56-38b7-ac32-023cb9f317ed | 1.20769 | -55.97682 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f543ee9-f862-3eae-a8bd-d18885741a02 | -1.17101 | -53.67377 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e1a9ac0-4c23-3863-8c14-cc564867ccd8 | -0.95461 | -51.65117 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9cfa7b7b-ab83-375d-b50d-01eaa54327f9 | -1.6053 | -52.28955 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41e88a36-dd44-3249-b934-b3637b4b1a62 | 1.86108 | -55.80384 | 2024-11-29 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3348880-2c9e-36c3-9e67-a7ed47bb95ad | -1.96234 | -46.44483 | 2024-11-29 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ecbed0da-c754-3099-881d-c519d5f5990e | -1.24518 | -53.35823 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45b8e575-3df7-35d8-a8b7-32fc690588ee | -1.20205 | -51.74653 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 809d4eb7-2e92-3b7e-bacf-1111fc3dfc8e | -1.16343 | -53.58469 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76c2268b-5c62-349b-8f39-32ac8a131601 | 0.98974 | -50.26216 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4f20ee9-aa7b-3ce4-8f6a-0870893305d0 | -2.3338 | -46.87781 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e56fefa0-8573-315f-8951-0423f7dc815e | 0.97782 | -50.26112 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b169b4ea-139b-392b-b36b-52a5cf1ef4de | -1.25733 | -54.54245 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7a06de2-0591-358b-851b-c5496bc1067c | -1.49732 | -52.43482 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b86e3441-ef4c-36f4-9d0f-a82abcea162e | -1.09335 | -53.64592 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dea1ffcd-97ec-3819-9a8e-16da1b5025ee | 1.24886 | -55.99157 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc6b14b1-42cf-3bcf-b444-ba54244f13e7 | -1.20044 | -51.75697 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2433d0c7-772b-3568-b8a9-382a79ba0e94 | -1.61686 | -52.45029 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ffe8c9d-a016-3764-b712-a0759fee49b5 | 0.7368 | -50.87343 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0ff533b-72c5-3227-88fc-9288764d67b2 | -1.09028 | -53.3662 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebd90c04-b163-3d36-bb9e-a0b0f1deebe0 | -1.31961 | -51.74617 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50691091-7a2f-37a4-9cba-ffc51689beda | 0.59752 | -60.46607 | 2024-11-29 05:20:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c825ae27-cdca-3ab2-9ab9-6d8654649cb0 | -1.96201 | -46.44379 | 2024-11-29 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6af390cb-8ba5-3c92-913f-0c4402eea432 | -1.2133 | -51.7376 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e722104-1163-32d2-9c60-3330e3d1778a | -1.29308 | -51.72585 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71c5a89b-ae21-3a50-9d6c-a7afbaf04bda | -1.08712 | -53.3863 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 804446a2-8843-3596-8b83-3c3abfe8b6d6 | -0.97141 | -53.6848 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c56e1325-49ec-3552-8d85-740875bb0b4e | -1.16548 | -53.68143 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0559937-d624-3af6-adb5-a450c67ab18c | -1.53706 | -52.69259 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469aa8d9-13f7-3a89-b78f-abf5b848400f | -0.26514 | -51.49574 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ae58b7f-9f41-34d4-a7c6-2757877b22e4 | -1.13483 | -54.21689 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de6475fe-0ebc-3d5d-8676-e198e3801bf8 | 0.97893 | -50.26076 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc908c00-9354-352f-bf62-435054bda418 | 0.99073 | -50.26826 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8737677c-e92e-3925-97ac-5b2dde62cedb | -0.56564 | -51.69669 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d73c510-9116-33e8-b76d-7059ce7f5cef | -1.14198 | -48.33913 | 2024-11-29 05:20:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d855bb3-ad87-36d2-9856-69a7c43b5b92 | -1.60218 | -52.29588 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8cfe589a-dbb5-35d6-a3eb-705a3948c756 | -1.33377 | -51.93828 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e803bd8c-2c6c-341e-9ac6-2b5ebca0182b | -1.10232 | -53.40133 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14784e16-8fe5-3e17-99cb-99dc2f4ffaeb | -1.06902 | -53.63881 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1f4ed63-75db-3dae-a9af-3d4f08b8c53f | 0.98323 | -50.12407 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7f2fd4ff-02c5-3ad5-bec0-27254e583391 | -1.15669 | -53.57224 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5df75888-33a4-32da-b37a-82a7d68a9786 | -1.18922 | -51.7659 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 705227cf-b9cd-3810-b3c6-a160ed1b04f7 | -1.59281 | -52.27771 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca2cff27-25d1-32d3-ae8f-d89af4a26699 | -1.66029 | -52.50523 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb8fa775-3c49-34c8-b3e3-5eca2b74fb4a | -1.07026 | -53.63095 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d24362d-22a2-3d53-a848-db72c523347e | -1.2145 | -53.75637 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c06445ee-22c2-3509-9f46-196f9a74410c | -1.09091 | -53.36216 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f88d081-fe92-3f9f-8ed8-d5ae59851297 | -1.07028 | -52.33466 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff5d339e-0cd7-3905-bc85-179036266a80 | -1.2971 | -51.73187 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07727166-723f-3d28-a5d3-13707743afaf | -1.96332 | -46.43851 | 2024-11-29 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 23cd550e-5395-3b37-bdf7-d6d2ea626c95 | -1.20737 | -53.5492 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5ce963f-4209-3f82-8278-91bd3738feb2 | 1.21417 | -55.97171 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8052b1b8-105d-326c-8645-8708e96cd017 | -1.20773 | -53.71666 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3034de97-ab44-31c8-bfea-a44571644fe4 | 0.94329 | -50.72958 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 184e0c3d-c696-3529-8beb-281ac214dbc3 | 1.48656 | -55.96473 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afe663ff-07f7-3118-875d-165ea7886ff6 | -1.63535 | -52.26613 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f351822-93c8-3f3d-bb77-dd61a34df329 | -2.33185 | -46.87796 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 42655727-54f2-3cbf-9614-2e72c9d97b4b | -1.04727 | -51.73751 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b43cb538-ff4e-367a-8515-7acf53fa7ee6 | 1.20872 | -55.96021 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07e5ed55-763c-316d-9f5d-159929aa0ede | -1.38827 | -53.63617 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26f178cd-f152-3290-95a2-2ba2ace14c14 | 1.45762 | -55.92031 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6151b943-d417-3dc6-b9c3-50fbe9f295b9 | -0.26805 | -51.63432 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 392f5190-e43a-336b-85a2-30eadf0d4ef2 | -1.27347 | -52.19871 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee98344e-6b5f-34c3-81ce-04ceda5f6c52 | 1.28259 | -55.92889 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b1057bf-3e13-3ba1-a0fa-349006b18d6f | 1.85451 | -55.79939 | 2024-11-29 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 909ab249-a691-3a13-8dba-ba1bc03d0fc1 | 0.03839 | -51.11126 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eaa3f61d-dbbb-3ae7-8bdb-d99c1e98b7e7 | -1.96295 | -46.43744 | 2024-11-29 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README87.md)
