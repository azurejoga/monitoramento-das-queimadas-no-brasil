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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f13758ce-bda7-353a-81a4-150f81614194 | -3.85309 | -46.50766 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37486eb0-4ac1-3a01-9aa0-4dc5021ed725 | -4.35718 | -48.087 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2dc211a-8c6f-3740-8fda-a2f9c4807893 | -1.73679 | -54.73601 | 2024-11-27 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0df922d-13b8-3eeb-949b-26e13e917ee3 | -3.07481 | -50.9643 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10a2cbff-96c9-3808-b34d-f8d2b25a89fe | -1.51035 | -52.22015 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4c46877-d265-3b8d-87f1-4803e098d727 | -0.98772 | -51.71292 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bff43cf6-85c5-36fd-9bfd-d14020f41550 | -3.31133 | -50.49884 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cbcd9b4-7d0b-3495-9e52-4de7e0a33429 | -4.21882 | -50.88523 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 416a3430-35f9-3917-9f2d-c8fc3b4f0090 | -3.71957 | -51.80218 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26322bb6-2336-3a61-8383-5eb4974ab64a | -3.98192 | -48.06287 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cad185ed-6eb3-39cf-b79a-7f59306d1a23 | -4.20834 | -50.88713 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 988b4c3d-9039-3361-900a-f1d45f71a1c1 | -4.30298 | -48.18475 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44872e73-b200-3fcf-b9a2-d4ae5c74d152 | -1.36725 | -52.12404 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60fa6f0d-846e-36f7-9a19-29658074f8e3 | -0.25819 | -51.49257 | 2024-11-27 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8438ee39-0e41-3cff-b157-1ad6245d0977 | -2.72822 | -51.74416 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4cc01e1-90aa-3918-8ebf-25051076ea79 | -1.49646 | -52.44403 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc0dd249-b663-3cb1-83c0-6da58e01ca7f | -1.79987 | -52.74853 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1b6767b-9d3d-36a8-95e2-ccd8dd01adac | -1.65385 | -53.80846 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08cdbc0b-2c15-311e-8343-8495e8a9a116 | -3.90657 | -50.60317 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3249790-c568-300b-8720-8ce839afec75 | -1.18955 | -51.76673 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2f71f62-1ef2-354f-9d82-e1a01afcfb04 | -3.39706 | -50.30133 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6584de0c-8a30-36b2-8641-4a4e261eb751 | -1.19944 | -53.88493 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b60896c-5fc3-3087-a11b-5c30451d59c6 | -4.30645 | -48.18523 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d805216e-c3ed-3cb8-b6e8-993a7ce9df70 | -4.38545 | -48.13443 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67982211-fc20-32fc-bacf-6f3902e90afb | -1.24676 | -51.62751 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68474cdb-c478-3562-815b-a9a6f445ea28 | -3.05456 | -53.2773 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e56034f4-c9c2-36a4-bbc9-e36dc25611db | -4.37659 | -48.50427 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 167a404a-ccc4-3192-a16f-2ab86a81bc53 | -2.03403 | -51.18922 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a821423-51fe-39d2-9c9a-27dbb2750c17 | -4.21057 | -50.89455 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa7bbf3f-4b03-3970-be7c-f30f2ef4e817 | -3.83284 | -46.56438 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4204c0a3-1ab9-32ae-80a3-f0bc5be628c1 | -1.35986 | -51.43995 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28c157eb-fb3a-344c-988f-946d0e41cbe1 | -1.49295 | -52.44347 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 563360e2-c12f-3bf8-b282-19b7e1e0c277 | -4.72526 | -46.5755 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e57ccc4-a0b7-350c-a778-87bf300f2dc8 | -1.06194 | -53.20752 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5a2573e5-c457-32e5-8cff-28c002bca1c7 | -2.81977 | -46.82677 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81c85c31-0081-36db-91d4-7e3ef7b05ee1 | -3.30037 | -51.1928 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cff02e04-77a5-3d7d-9705-dc51bb4a14f4 | -2.23219 | -53.68458 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 104730ff-dc11-3c87-896c-8a19ad80c8f1 | -3.00208 | -45.46838 | 2024-11-27 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 19713310-a7d4-378c-b523-3287762c8f1e | -4.31511 | -49.90434 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db280232-4576-3b1d-aadf-cad99a45420c | -3.11006 | -53.25242 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 05f2c20c-7e3f-305c-be97-c4d74b31f144 | -4.04561 | -48.33209 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f391dfa8-4070-37e5-956c-a7375a3b328f | -1.83408 | -47.91068 | 2024-11-27 04:42:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c095fea-60d4-3f48-9543-f589b7cb0647 | -3.04787 | -48.51151 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 166a57d8-0bb4-3f07-9a89-211da406ac2c | -4.13194 | -46.70882 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3832b372-bfb0-3d83-8bc9-8bd4c7bb7a44 | -2.41504 | -53.89727 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7999f194-5282-3a75-9a45-464de4f4e050 | -2.10071 | -53.36121 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cc516cf-83e5-3e2b-a6e9-7368b2aa5be0 | -5.58464 | -42.92991 | 2024-11-27 04:42:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca874f2d-ef11-378b-8489-c671f89d7555 | -0.99057 | -51.71717 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8075585a-7a6f-32ef-bb28-be73496a5f43 | -4.03989 | -48.32343 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95042b7b-373b-3a4d-b430-200b12f8fbe8 | -2.28243 | -47.39524 | 2024-11-27 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bfdc040-11d5-3d14-93a1-aac6577b5aff | -2.8095 | -53.02474 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34efc07-092f-3f09-91f0-e1c62b82a9b7 | -2.59662 | -53.96884 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15124e08-5028-30e0-bb56-88cd8fc78787 | -3.48608 | -50.25183 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4afa3f3-f900-3140-b801-3c786bfc0961 | -2.87201 | -49.12016 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aeb77a9-e8e0-38b8-b849-2b0408660569 | -2.53305 | -54.00548 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46a942ce-fe5f-3e6a-a4a0-e7643ed0315b | -4.19548 | -50.68701 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7493d012-4634-3d20-82e2-340ee158d3d8 | -3.08475 | -47.82164 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 98a64f33-1c8b-394f-bd66-fd58e1160f3c | -3.24825 | -50.61949 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 172dbc23-797a-390a-9743-1d47ab2743d0 | -2.6098 | -53.96462 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02b7d155-a3f4-3d9c-b477-f6016224329f | -1.96732 | -53.13669 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8479d55-7e83-3471-ba74-e11617c4d0af | -3.97027 | -48.09255 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d85f15f-fd7a-3d5d-a9ce-f4f98d98c708 | -1.19413 | -51.75985 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b07ae9-c8cb-3a4e-83ce-27c3bf843ba2 | -3.78676 | -50.13306 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f52914ba-77b4-3800-a0e3-84609d063043 | -4.21111 | -50.8911 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b24cc8-a516-30a9-9dd5-b512c54adfdd | -4.21718 | -50.89558 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 59255fce-c276-3ede-9229-b9e012b978ed | -3.42685 | -51.67931 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 394fc79e-2656-3006-a5fd-03531d94963f | -1.20099 | -51.76092 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 884f41ee-c74d-35b3-bdda-9c3223b2e290 | -3.50165 | -50.30355 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b82f28e2-1529-3394-bbdf-7e32ab63b22f | -3.27141 | -50.6231 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e9188ce-a3e7-31af-8aa4-2d0d38855afb | -3.30471 | -50.49781 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98b551bd-d250-3d51-b0f4-b3712c91ce54 | -1.15454 | -53.68227 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9505a69-4f7c-3667-9016-924d2ff22f7a | -3.47179 | -50.25665 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0dfb0e1-0c44-35a8-a717-5086ae920b30 | -2.01706 | -46.38374 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 739db20c-f6c0-3c23-aed1-0e15582d0d76 | -3.6899 | -50.23066 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 819ccd17-f3f1-3f1a-b4e1-9da6b044c4e6 | -2.57782 | -54.06417 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab8e13e7-0333-37dc-8f74-d08f47ff384f | -2.81446 | -46.81293 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccafe928-7917-39bd-be18-51c8938b9625 | -3.37848 | -50.11499 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03e4ff55-4957-3ed0-8077-6cf775141b81 | -3.44678 | -50.0062 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 858d6c67-8c76-3c96-896c-0d8fb7756c16 | -3.11841 | -53.10799 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 564f6dcf-5527-3865-9e13-9c962493e191 | -3.77645 | -46.68388 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99051224-6af7-363e-930d-839aa7db79b0 | -3.24771 | -50.62293 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40cde9e5-c586-3acb-b52d-5919cd8e660d | -1.72126 | -53.06187 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a70c9ac-552a-3b19-9bb5-e625e3421723 | -2.23148 | -53.68898 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2f81180-6140-3f0d-b4e1-9ff569a82484 | -3.17552 | -50.21666 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33c2225d-4f87-371b-a3d7-9b3c1764a7c5 | -0.98999 | -51.72089 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43fc97f4-18de-3312-9304-0dc864b88479 | -3.81913 | -47.4735 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f8f0d35-f8c7-3a79-9d0e-d5f9dd4c9977 | -4.25456 | -48.0722 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9270f9bf-d41f-3fc6-8599-80f00c220a5f | -5.23716 | -48.05824 | 2024-11-27 04:42:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ec79302-49cb-3058-a477-2bb4e1a6f0aa | -3.68236 | -49.93327 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bc55e49-3a06-348c-9a4a-a39befb98902 | 0.95061 | -50.74964 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e037f466-2cab-3df9-b872-9819db1641c4 | -2.92378 | -48.63318 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f40a48d5-53b9-3f46-88fd-5430fef41fe9 | -3.13587 | -48.57683 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46464299-c0ca-36d9-9797-50a25f85a38d | -2.26741 | -51.24033 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d71575d5-1647-308e-9d56-a12205465ca7 | -4.24243 | -48.66919 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc43734b-cf83-3b85-b73e-c7f45512eaf8 | -3.97955 | -48.07834 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d2515c5-4247-3af1-8c5e-7997606af6f2 | -4.1129 | -48.48748 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7166b5e-4af0-3607-8dd7-4a144e621651 | -2.58109 | -51.92317 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a753a74-532c-3391-a611-5420341aede2 | -3.09227 | -50.35855 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 817ed83a-6f6c-3e30-a805-488134754415 | -1.70319 | -45.48897 | 2024-11-27 04:42:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59dc64ed-9a5b-394f-8738-97e20bfdb45f | -1.28623 | -51.73177 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README73.md)
