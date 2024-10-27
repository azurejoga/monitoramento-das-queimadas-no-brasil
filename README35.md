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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f1f3050-101f-34be-ad33-c2160e556834 | -3.26528 | -48.8001 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bdea22f-1c90-3312-8930-a7ee8aa7107a | -3.26465 | -48.80376 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a79924f4-7c1f-37fb-90ec-56bf4fb47e6c | -3.2613 | -48.79635 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dd84855-b799-364b-ba81-8200d86699e2 | -3.26069 | -48.80004 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdacb0b0-cf00-37d0-bcd0-ab6774d8b09e | -3.26036 | -48.79551 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3998364-5498-3290-8688-22e58b25109b | -3.26009 | -48.80372 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f94de018-0db8-398b-b6e1-9815b41c5948 | -3.25973 | -48.79918 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91fe841e-2f51-3cdc-95a5-cfa2df656851 | -2.15736 | -48.45074 | 2024-10-27 04:00:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df98a3d3-2b51-3f55-8910-f9a344d156c8 | -2.15677 | -48.45431 | 2024-10-27 04:00:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bbe4b8f-2b16-318c-885b-83e7e3cdaae2 | -2.10186 | -48.55441 | 2024-10-27 04:00:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c64cd5a-1ab5-38ee-bd22-9942d084688f | -2.36227 | -47.67195 | 2024-10-27 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d2c5723-3a3f-3073-92d7-b2d32ad1c6d4 | -4.95605 | -48.64513 | 2024-10-27 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5621ddfe-45d9-3f9f-8cb8-95b1560fb2e8 | -4.95547 | -48.64853 | 2024-10-27 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 158aeb3f-2978-3333-98f4-7e6c330f3bac | -4.95488 | -48.65197 | 2024-10-27 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c3e8965-58d1-309c-a7b8-c8e54023536a | -4.9543 | -48.65538 | 2024-10-27 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e2f3bd3-3193-3925-a8d4-de67c7a25692 | -4.82407 | -48.09793 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d1476ab-416b-3770-851e-64e6c53553ba | -4.82356 | -48.10092 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 617fd441-23ba-3dc2-8688-b0874fe4ceef | -4.57873 | -48.02813 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e8c7d3d-559d-32c9-b897-b363341682c4 | -4.57803 | -48.02639 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b14e7b75-93f0-373e-bc4e-4d63543c946e | -4.57751 | -48.02955 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9021cd6c-810f-3e7b-858a-133c9b2cb717 | -4.57698 | -48.03275 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33e21254-d9a5-38b9-b836-7591d45d84c0 | -4.57411 | -48.02414 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32e9a587-721c-396a-97a8-59fa37c17610 | -4.57357 | -48.02728 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84095dbc-adbd-32c7-a5eb-3eef12f06da5 | -4.57339 | -48.02238 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86a53cfe-c560-3aa3-93b6-74fa99d67026 | -4.57301 | -48.03049 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d930ae96-f0dc-369f-b8fa-c2134c3eef6a | -4.57244 | -48.03378 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfc42164-8e08-39eb-95c0-33eb1d1c3c10 | -4.57234 | -48.02871 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e583d4be-2d97-3f1f-8a82-0c27faad89e3 | -4.5718 | -48.03199 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa217773-4761-330b-bb63-8e728a839afe | -4.30041 | -48.6516 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b109333-5932-32e0-b6d5-b4d9a1c57aeb | -4.29982 | -48.65509 | 2024-10-27 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c04d219e-32f7-3f7e-bcf3-78758d740dce | -3.92905 | -48.3437 | 2024-10-27 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e16502ce-1be1-3af5-9d83-655eb07aa978 | -3.92849 | -48.34705 | 2024-10-27 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c3dc853-369f-3014-a267-93fa0c5bb47c | -2.84262 | -49.25343 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4b14fccf-bb99-38e5-ad8d-6d792fbb4896 | -2.84198 | -49.25735 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a9ebb7b7-d6c3-389a-b66a-03a5f3fd5c4d | -2.83753 | -49.24845 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7fc410d3-9a0a-3d3f-83f2-8d8f06832119 | -2.83688 | -49.25241 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5432e093-b191-35ca-832f-7b04b1546a28 | -2.83622 | -49.25638 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b715881a-a1b4-30f0-9213-a77fe2036877 | -2.83178 | -49.24747 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8dce4f52-a0b6-3630-8b59-aac5344e729d | -2.70773 | -49.31448 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c87aeb6c-3130-36cc-b2da-17f6e9bf710b | -2.70705 | -49.31858 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcbd4e0a-97d4-33eb-9c61-8db82c93defe | -2.70638 | -49.32265 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 249b3648-03fc-317c-989f-a41219faf127 | -2.70194 | -49.31348 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c73802f-8b73-3a29-acfc-35c3e4383269 | -2.70127 | -49.31755 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61a665f2-12a7-3425-ac79-4de2154940bb | -2.70059 | -49.32162 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78471279-1810-3bf9-83c1-1984ae5d4b55 | -2.69991 | -49.32572 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 80cc4a00-98d1-330c-b602-0187cd3546c4 | -2.69548 | -49.31654 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60ab8702-5402-3f15-a882-2f9a95af159f | -2.6948 | -49.32061 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a00ef65f-4b31-36e8-811a-8a3a101c0acd | -2.66306 | -49.3322 | 2024-10-27 04:00:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2673211b-61a6-39eb-9cec-c34ba0e01f4d | -2.64332 | -49.23919 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a0938f7e-6723-334f-b649-7d6a42655087 | -2.64277 | -49.24142 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d32d6f2-c052-344d-a708-ec8eab32b152 | -2.63821 | -49.23419 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8218e0e3-9f17-312e-97f9-a0b2b6207d92 | -2.6377 | -49.23642 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56e25b76-b9a8-3d70-b0bf-9ca3115718db | -2.63756 | -49.23817 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb17c06b-56e4-395d-bc42-2f0ab5f6346d | -2.63701 | -49.24042 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41feee35-f6d8-36d5-8d0a-b7269b5578c2 | -2.6369 | -49.24218 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8226446e-2910-3787-870a-f5cc3afb76b5 | -2.63632 | -49.24442 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 927992da-a1e5-3a53-ab75-29fd69afe3df | -2.63624 | -49.2462 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e9236ab-3ebc-39d7-bf29-88324fe34619 | -2.47565 | -49.10539 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d7485e3-abdc-30c2-861b-96d765e33e8f | -2.47515 | -49.10534 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea7d44ce-cefe-340d-94c1-cb0a887a7947 | -2.47498 | -49.10938 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 042d9297-9751-3258-a354-23733245340a | -2.47451 | -49.10935 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdef5d97-5bfd-3a52-b404-9fb39ccd23c2 | -2.46992 | -49.10446 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccafe377-6577-3d0e-8c4a-7c00e61cfe3d | -2.46942 | -49.10439 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e21f6dab-1858-36ba-82d6-39b6dacd6ba5 | -2.46925 | -49.10842 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a177fb8a-6f13-345b-b6fb-09f31988da76 | -2.41023 | -49.21357 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6720f1c3-a7f9-38ff-a9c9-7df8a7597b92 | -2.40956 | -49.21762 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c961cdd-908b-376c-a9f3-5e490807660d | -2.92973 | -51.75713 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ed9e79f3-9933-3ae8-8629-ebaa9e382b40 | -2.92873 | -51.76304 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cb207ec0-6845-398b-bd49-688d1e88da5d | -2.92771 | -51.76903 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae1dbbe4-b9f8-3036-8aee-149894002c91 | -2.92408 | -51.74974 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0864dc6e-eb9d-3077-969c-91ea03537a3c | -2.92308 | -51.75564 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 62309a01-a66e-3765-9ee9-74b197d73822 | -2.92209 | -51.7614 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 00f9b943-01c9-3c97-bc25-671731179c1e | -2.92105 | -51.76751 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a0f6252-bdf5-3b5e-9acc-48e562033fbd | -2.91638 | -51.75439 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e265b36d-2375-39ca-9f31-8c51ecb45c7b | -2.84467 | -51.80857 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35b796fc-44fb-3399-b176-22e21b465967 | -2.8439 | -51.80268 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dafc4826-9ffe-3198-94a0-f2b71d9f57c5 | -2.84359 | -51.8147 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 498b01e1-50b9-3194-aef6-d681643027bc | -2.84289 | -51.8087 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94637bc0-4e8d-3cfe-92cc-07c6a83e8319 | -2.84187 | -51.81479 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60feeb38-8f71-3c52-b05b-d580fc8a84db | -2.83897 | -51.80145 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3197b32e-25a8-3014-a218-5739f36ebf70 | -2.83793 | -51.80738 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88d89b0f-bda9-3d5f-a75f-a642a421801e | -2.83715 | -51.80156 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afeacf09-1140-3b2c-8fde-41232201aa59 | -2.83689 | -51.81332 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec572762-a877-3691-99ef-123aff7081d4 | -2.83615 | -51.8075 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce08536b-ccd0-37ef-8fee-579234ee0ae1 | -2.83515 | -51.81345 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4dafb71e-2633-3984-b21a-71c72fb3f061 | -2.83118 | -51.80632 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57f7660c-6cbe-3271-a5b1-b9d85086415f | -2.83014 | -51.81224 | 2024-10-27 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f80bf0e-a73a-3e33-8ca5-2c70439654b1 | -2.82548 | -51.04072 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4176c4e1-930e-3c36-9f81-e5cd8d160000 | -2.8165 | -51.5988 | 2024-10-27 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a0857ae-df28-33d9-af53-54deb72ad4c9 | -2.81313 | -51.59764 | 2024-10-27 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15553838-cf36-34b5-86e8-f6e36acfcad3 | -2.81218 | -51.60336 | 2024-10-27 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd5f99c6-3fe1-322c-992f-8d25b62156f2 | -2.80983 | -51.5977 | 2024-10-27 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6649851d-d554-378f-956d-0c8f586f8b80 | -2.60212 | -51.77341 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58da2a61-713f-3dff-aa75-66c53f48c6da | -2.6011 | -51.77945 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c84ab85e-b6ff-3544-93c1-94e919e71444 | -2.54922 | -51.17944 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ca50c7d8-d20b-3daa-b8ab-b3f4661b9ae0 | -2.54828 | -51.18492 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 70822995-e7f1-3070-9f24-82cac10c2264 | -2.54552 | -51.17024 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14f50e2a-f3e4-3bfc-ae6b-c4537b410373 | -2.54462 | -51.17571 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1e479c0c-fe3f-30b1-a8c2-2c931d5015ad | -2.54457 | -51.16744 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab65cd99-5b19-30c8-9b5e-8e166be33ce9 | -2.54372 | -51.18117 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README36.md)
