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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aa941b1-61fe-3bb8-918c-dfd17fe7e57b | -3.63482 | -50.79321 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceb9a7d3-659a-355b-ac54-b37a7484dec1 | -3.51065 | -51.1958 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bb85626-7762-30b7-83a1-4f5e22bf0f9e | -3.51011 | -51.19927 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84930b0f-a131-3d43-ad02-46593c2616a6 | -3.50733 | -51.19528 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bca8098c-7435-38fe-9e87-d6b5e60741b4 | -3.50679 | -51.19875 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9f38e2fb-5668-3786-899f-8e366fdc86c0 | -3.50625 | -51.20222 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa99c137-ca2a-342d-b826-1def4c49b35d | -3.47369 | -51.21455 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee92baf-10f5-3377-bb5d-594fc458788f | -3.46987 | -51.3702 | 2024-09-29 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14dddd0f-5a46-383e-bf18-33847f05a4ef | -3.38977 | -51.22992 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb3ba455-46e6-3a8f-bfd2-4bd27c1ff1e6 | -3.36111 | -52.17104 | 2024-09-29 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a31a5561-87f6-3368-910c-a48cbe1001d2 | -3.30128 | -50.66563 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 552c27d2-3577-3ca6-beb4-ea5becca4f82 | -3.30073 | -50.66915 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75f36c91-a946-37a5-8758-f82fa4bcdbad | -3.29793 | -50.66511 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83954fbb-5e10-362f-b3f3-24e09fc93a9c | -3.29738 | -50.66864 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 36088657-3fd1-33e9-a92b-9bd3fd598d7b | -3.20069 | -51.15767 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80c2ff8c-ce8c-383f-b641-80e885381342 | -3.63604 | -51.78384 | 2024-09-29 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f5d88ab-6912-30d4-a8c1-9ae310d56014 | -3.5715 | -52.12961 | 2024-09-29 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d55ad651-d019-3c8c-ad28-9dc23bab1110 | -3.8208 | -50.77456 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6cbed888-df7c-302a-bf1b-be61436cebc3 | -3.82025 | -50.77808 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebfd1ee4-32fa-38a7-bb59-e3227de8f31d | -3.93294 | -51.03637 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a664757-da75-3467-9917-20c30fe4d437 | -3.87842 | -51.1672 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a59c3b-e615-37ae-b671-325643039eef | -3.82049 | -51.5376 | 2024-09-29 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c08ecf8-ec82-3798-9c43-a225aae584e0 | -2.0033 | -53.30107 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67e86ddd-4ce2-3a3f-a46a-963e198c8f1a | -2.00047 | -53.29687 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdf707f0-6318-3f41-bca1-b314038e3191 | -1.30223 | -52.62771 | 2024-09-29 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 840c1030-3b90-3cca-beaf-9064c21c8895 | -1.29888 | -52.62713 | 2024-09-29 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c31785b8-9dd8-37c6-8b22-113c7bab166e | -2.07048 | -52.01787 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a46850b-ecce-3e09-8d49-75e00a903db6 | -1.87897 | -52.09034 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f3c2ba4c-03b6-3b03-b357-f93ea46ae297 | -1.87842 | -52.0938 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 16e2c9ae-7a52-3eb2-b10f-0c21177488f2 | -1.87565 | -52.08982 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d470cf9a-76c4-3b4a-8403-6fa5202f3fe1 | -1.87511 | -52.09328 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 78be7735-0788-3637-85d6-be76e76c0b85 | -1.80188 | -52.01833 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 536006ef-5089-39fe-80b3-923c06510cca | -2.85662 | -53.31621 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca3c4e6b-3e0c-34a6-ba73-57186df526d7 | -2.85604 | -53.31984 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21680f9c-fbcc-393a-8789-874648e5db5e | -2.85324 | -53.31567 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca4aa5f5-cbd0-3a27-8161-6ccc69247e99 | -2.85266 | -53.3193 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94e55555-086b-39b6-81e2-a92493e0a404 | -2.76151 | -53.23139 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdcdbc2a-c3d7-312a-8eac-1ee1a3ea6856 | -2.75812 | -53.23086 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29c3bc71-b162-3a74-bf97-21ca315d5e36 | -2.75755 | -53.23449 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea76bf27-970a-3ce7-aa99-f027f30a6dd9 | -2.75474 | -53.23034 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4562f179-20cf-3f2d-aa16-f6dfc05747ec | -2.75417 | -53.23395 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3f1995d-f716-375e-b83d-94c08ed9aa10 | -2.68713 | -52.43745 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cb61bc38-fb1f-3a2a-b116-1a83d9f6e5c5 | -2.68381 | -52.43691 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 580dfb24-c8b6-3ee4-8b92-70f0ae6f83f6 | -2.68326 | -52.44039 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3a54de6e-74eb-3fc1-95ac-8071abee659a | -2.75773 | -52.0974 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7462ec24-3fed-371f-9f3e-cc2ab38b71b6 | -2.75719 | -52.10085 | 2024-09-29 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1829e238-7ebc-3503-9085-6fa8113f81e0 | -3.69235 | -52.37466 | 2024-09-29 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a57ba7f8-6e21-30b9-892a-ea34ccc08e41 | -3.69181 | -52.37812 | 2024-09-29 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c8df740-31c0-3593-8827-d4290cd39a3f | -3.57794 | -53.25138 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f643f60b-c351-3937-b1cf-9950c607d47c | -3.30033 | -53.6996 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a7f75ce-8dc8-3fa3-929b-2085fcd5ee37 | -3.29975 | -53.70331 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f219e0f-4f3f-3f15-8bf0-0f0a064ab497 | -3.29691 | -53.69905 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1329424b-9b8b-3acc-9154-1bcf50146619 | -3.29633 | -53.70275 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8da7b70c-9aea-3141-902e-609445b90740 | -3.24154 | -52.88296 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a83aeaa6-40d4-3823-9f26-c2d0f8762789 | -3.24098 | -52.88648 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6212e09f-13bd-35c1-a69a-cf5826b27d76 | -3.12963 | -53.0537 | 2024-09-29 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94ae2150-641b-3241-b7f9-cdc03d6173cb | -3.5813 | -53.2519 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3659ccd-853a-3b56-ad2c-7c155d812310 | -1.574 | -54.77375 | 2024-09-29 04:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40861217-e20e-3b72-987e-0131de9a1c6f | -1.4879 | -54.3772 | 2024-09-29 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 909471c3-a6e9-35bb-99c3-58ff3d62bbc6 | -2.21828 | -53.67178 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc959cf7-e462-33a4-b143-2488e2c7c0b8 | -2.21769 | -53.67555 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62d60bf9-dcd7-3db2-8f54-63bcdac047c8 | -2.21542 | -53.66749 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a5f4be3-af42-3264-b9b7-790a905ad2a3 | -2.15444 | -53.67338 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96f73c76-0cb7-3d9c-8041-deb494ab63a3 | -2.15099 | -53.67286 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8fc3a6e3-bcd4-3c35-9c88-b9802801c134 | -2.14934 | -53.66104 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c0dd62e-fa5b-3ad7-a154-29de92d19971 | -2.14814 | -53.66856 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11cb6df4-2893-3674-89b1-28bdb5f9f399 | -2.14754 | -53.67233 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b2ab6a47-192c-3161-9312-110805999981 | -2.14693 | -53.67611 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b80315b7-27d3-3856-b846-bb1aacd133e9 | -2.14589 | -53.66051 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb2957b1-772b-3b52-b788-8ef2b25e3bee | -2.14469 | -53.66804 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| ea30f223-5c02-3560-8da0-07131b7b6264 | -2.14409 | -53.67181 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| ed02f597-a972-3e0b-a431-8a4501f28fda | -2.14348 | -53.67558 | 2024-09-29 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| ea5b67ea-50f5-3974-a557-fc4fa00f5ab7 | -3.45445 | -54.10029 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| efbbb806-6151-3c6a-9aea-f469c4ae316a | -3.45385 | -54.10413 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de10d9c5-e721-31b1-95bc-059807b37dd6 | -3.4522 | -54.09205 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad3634b5-13fd-3bc5-99b6-7e844261f989 | -3.44934 | -54.08765 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4250828e-7c4a-33e5-8a0b-1d03b42efc59 | -3.44874 | -54.09148 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50e0c96d-b22f-38aa-8ac6-1edfe3cc9cba | -3.44588 | -54.08709 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bafd53f-8cad-3d6e-8344-573db15d2c45 | -3.44527 | -54.09091 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e829400-3364-3cbc-884e-67b5513c9c88 | -3.3128 | -54.92739 | 2024-09-29 04:46:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b15f98b-fd2e-34ad-bbab-0cb427ac9170 | -3.31214 | -54.93153 | 2024-09-29 04:46:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1be2350-7da5-3f59-a3c1-2d2e5117ef76 | -3.46365 | -53.79704 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e1f9503-0642-314c-8e34-85845b65865c | -3.46306 | -53.80077 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e8f727b-9688-37fc-8296-af783794c906 | -3.45963 | -53.80024 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9922d052-fe2c-3514-a04e-57f7a8abe50b | -3.35419 | -53.78042 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2171f9d0-63be-3852-8f50-ce3972f89a8a | -3.14114 | -53.68711 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ac39095-7850-34c2-814f-37df2427e7b4 | -3.1383 | -53.6829 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f504497-953b-3c82-9d90-fa7ab33b5545 | -3.13772 | -53.68658 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 184fd28f-5759-34ff-a1d9-046e39a20546 | -3.13429 | -53.68605 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c6ee57b-ad9b-3bfd-a359-495499354d76 | -3.13109 | -53.75013 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 668aad18-9a5f-3a35-b796-16cdb1891a85 | -3.1305 | -53.75385 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2e14e0e-5252-3f66-977e-ea70607c257e | -3.1299 | -53.75757 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1cbf4ce2-7d09-3b62-abe7-5016ddf972e9 | -3.12826 | -53.74587 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea8925c1-fc19-3b84-8155-b75f722f5c78 | -3.12766 | -53.74958 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c82a3cad-3085-3e0a-bcfb-bc1a0c82df70 | -3.12707 | -53.7533 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42b5d775-6d17-3d8e-9913-cb41f7e77a20 | -3.12647 | -53.75702 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f89efa4b-7f3e-3cab-b4a4-de9146539bea | -3.12483 | -53.74532 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def1212a-ca58-369c-a70e-d0ea4e75b0b5 | -3.12423 | -53.74904 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc1afa33-4caf-3cce-8cbc-c113a5beea6d | -3.12364 | -53.75276 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f15455d0-df51-32f3-979e-fe61b9bb71c5 | -3.12305 | -53.75648 | 2024-09-29 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
