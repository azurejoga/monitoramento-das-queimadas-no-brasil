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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3394733-4c59-3b3c-9b25-d1cbc57acca8 | -3.12079 | -53.27068 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fd982a4-de8f-341c-b9f0-41994127bd49 | -2.59522 | -53.98 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 45e6f656-376f-35e5-8eeb-35a97e5c6124 | -3.49477 | -53.82969 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23392873-17e9-3276-90b0-1e66304f9ac7 | -2.44803 | -54.01819 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5fba3f7-f351-3b7c-abab-47f00de94c91 | -3.58402 | -50.34249 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 687c7d6c-5df5-31fb-a328-53aad5e365fd | 1.1858 | -55.96277 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 433ecb61-b246-3946-8ad2-16df596430b1 | -3.30363 | -54.16528 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 62ea5ab4-67e8-30fd-bf4d-8675fb3abe75 | -1.07508 | -53.38551 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f39d0023-4a7f-3e00-9229-6747dcd02783 | -0.09895 | -51.27628 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d18c48e-e111-3716-bc38-9a483c9c2a0f | -3.11058 | -53.7599 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bcdf9fb-736b-32f7-97cd-ca9ceff44b3d | -2.32871 | -50.67416 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 47eeced2-cb98-36e8-8738-43e5afa42229 | -2.25434 | -53.4567 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9e05e39-11b2-3b05-9499-a530ccdbb4e3 | -1.78283 | -52.74522 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04da2a43-f044-372e-b668-dcbb1e6791e1 | -1.71863 | -52.77326 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48df9f5a-270f-331e-b738-a3ad9f2c8705 | -2.92023 | -54.26301 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fe9de62-ff34-3a75-99d7-7913d3838d4c | -1.37088 | -51.97282 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 856421d3-e07d-387a-87a0-b7ef2aea65f6 | -1.3209 | -51.6679 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f85b4aa3-d805-3d3d-a31b-e9304e419f1a | -3.69665 | -50.16795 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97e3b9b8-7f95-344a-9e8f-380d2caff495 | -4.87078 | -41.29707 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d3f5951-5647-3df3-a6c0-8d22b68eeb91 | -1.53608 | -51.56988 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b122c991-c2fc-3775-874f-f46d0b056de5 | -2.57681 | -55.99382 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8527eea9-e2aa-35d2-9e83-382f586364db | -3.11573 | -53.10471 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60589614-843d-3e66-b092-5d309090f346 | -3.27104 | -53.83205 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3ec9579-418f-303f-acee-8cd7b1d253cf | -2.84818 | -46.68333 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4e1416b-c5fd-313c-bb06-3fd349b3c572 | -3.05613 | -51.06154 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f22ab51b-55dd-3ca2-9c77-af67f7d49d41 | -2.45868 | -53.71056 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 111eca70-fd12-3917-8e0a-49937e732339 | -2.53671 | -54.05694 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f88ba08-e967-3555-a732-facebd53d3db | -1.43173 | -55.24782 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55824ea1-a014-3989-b697-7559f24ac9c4 | -2.5395 | -54.06095 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34cf6f43-810a-3f85-8d76-40397a82d4d5 | -3.37685 | -50.42155 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8171b210-40ef-3aad-9db4-a2cf00ce3e98 | -3.21756 | -49.22395 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3147cac-7700-3458-b455-b4937a779847 | -4.8631 | -41.29871 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ec5f2505-c221-325f-adee-42b795923351 | -1.14085 | -54.11021 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0a967f8-c65d-3cbf-a9c4-6114adf46d2c | -2.87874 | -53.94519 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4466b15c-3548-33d6-92cf-aa0bd2e04f3e | 0.98389 | -50.24929 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f33fe05-4543-3a49-bf82-97fbe8546ffe | -1.18202 | -51.77138 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a17d1eec-8b2f-3abe-a372-bca41a121ecd | -1.06655 | -53.6364 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01fd5b74-abf9-3d7b-bb46-565efbdcfeed | -3.08772 | -49.20684 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ab7a927-476c-3c0b-afcd-331724edb2d5 | -2.80316 | -53.00442 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d3af237-1631-3135-95ea-ca2d42d606bb | -3.46556 | -53.78915 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20a17f0b-5352-383b-858f-a2534410571f | -2.02041 | -52.08401 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea666341-2765-3e72-a419-b607da4e47a9 | -1.62317 | -53.87981 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e4638fa-b75e-385a-8f55-66039e9adcdb | -4.8794 | -41.28878 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 137d644d-6700-3c75-b380-e36e973192dd | -2.673 | -46.10101 | 2024-11-30 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96fd7775-8458-38fa-a130-fd3aa8352af0 | -2.97842 | -53.87032 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b91d555-1e02-3456-bf94-f3c5abed84ff | -0.89868 | -51.6487 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 796e8172-40da-3854-87b2-3766d6ee4e32 | -2.9751 | -53.89148 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 869a3547-49a1-3390-b244-d199060b134f | -3.59808 | -49.97603 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7560153-04b8-318e-93f7-44300227bfb9 | -3.05796 | -54.05173 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b003e7d4-be60-37c3-8042-681c9ba02e20 | -2.82333 | -54.10173 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a7cba4f-df64-314c-bc65-018307ec217a | -2.88662 | -54.00399 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62418d2a-4c9a-3210-8b1d-6971ef74fe80 | -1.07844 | -53.38602 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d83b27f-a1cc-3994-a9d1-e0a4bb0c0201 | 1.20603 | -55.9413 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeda2f88-9c86-397a-b203-b42dbf9bc621 | -1.2216 | -51.79797 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00a547a5-aca2-3916-b6fd-319c0be3d446 | -3.73301 | -54.23173 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 701a01e1-24c3-31e8-936b-728d7e78ccc8 | -3.24927 | -53.8614 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbfb8021-7856-3b72-9693-ae2fafad4c4d | -3.21948 | -54.18465 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 324dd654-b73e-3c23-866c-931b91de15ee | -1.62208 | -53.88679 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 749fa656-1cf1-3c6e-a53f-8cccc825c472 | -3.07613 | -53.29055 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46a0f8ee-c87e-33f7-8194-f0f1c896a3ad | -2.53411 | -58.02868 | 2024-11-30 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1144293f-d7d2-3252-bd4d-c197cd1ddf57 | -2.66233 | -48.80003 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c08b0957-d88e-34f7-a4f1-f2bfe63a8d50 | -2.77015 | -54.05783 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae5e8fa8-a47c-3aaf-bf89-e28d6045b509 | -0.87268 | -51.72262 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfce3d59-fe85-3f43-9087-23e35b2c9bbe | -3.42248 | -53.88788 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4068371d-d065-3cd5-9897-332f40b07462 | -3.03895 | -51.78469 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aa1f42f-0153-3430-894c-31b35d2bf38a | -3.17455 | -53.84635 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 690407b5-a10d-3336-8aae-e18537d352c7 | -2.73359 | -54.138 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63039c28-16db-32c3-8a16-e8d827a9023b | -3.4879 | -54.02802 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 644d3901-53ff-321f-88f3-296a30051d87 | -2.77512 | -54.02634 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c892510b-6f94-37d4-99b4-c27ef7017f87 | -1.09692 | -53.39978 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72b4caf2-79f1-35be-b709-49350bebae5d | -2.64209 | -49.90867 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1e87f88-afdf-30f3-a88a-3f9c92058949 | -2.54787 | -55.23133 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bf34a4d-249b-3f6b-9041-2609fca04e37 | -1.62354 | -52.69087 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cad8e951-2dd5-37a6-96dd-c5e68a0162c7 | -2.37761 | -50.40276 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3219abf3-d401-334a-9edf-0257e1671598 | -1.65611 | -52.73014 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f51e131e-2843-3dba-803f-e8b014255df0 | -3.17936 | -53.25352 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 171fe949-d8db-3fca-b712-66633caaea08 | -3.99575 | -41.51221 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c133ac78-0b77-3189-b22a-d9a340db5860 | -1.23322 | -55.77358 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87cff859-69a1-3e52-b6a5-e564f6be075b | -0.97849 | -53.72328 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06fb87f5-b67e-394f-a4a2-68f6e1b066e5 | -3.23132 | -53.39238 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b9403c9-9ffd-3929-82c2-e94ee1259f2b | -1.33982 | -54.99218 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9b8c0329-7e6e-356d-b71f-6ec48a2f7688 | -3.20578 | -53.37737 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 047c2d92-989d-3583-af2f-35f3cf8b2230 | -2.83669 | -54.10381 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06bc0896-a6ef-350e-a010-4fbf77a86171 | -1.23644 | -52.5339 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c92c5b-29b2-30c4-9361-e172f7e783f4 | -3.22003 | -54.18114 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6ffc297-82d6-3100-9dd6-43de87354a69 | -2.8345 | -54.11777 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2ad5687-0afb-33d9-a0b4-39b12e2ba7a0 | -2.69105 | -51.9875 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10474552-af63-31a7-adde-96be9bfdc24f | -2.90277 | -54.17832 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 369fc5bf-b8f8-31db-9bed-6282a4e53421 | -1.3204 | -51.74231 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c4c89e5-d1a6-3596-8120-0f3bc8e7a4ec | -3.12704 | -53.2754 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6c93417-c848-3c9f-b862-66c56208aa6e | -3.98151 | -41.5099 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1c8f339a-dbb3-3e66-8fd1-b3921222a151 | -2.69463 | -51.98805 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8c95b84-2e40-3106-bde0-5cb14394e56f | -1.07379 | -53.63394 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b5ebe495-6bf2-36a5-a0ee-d7c1564a8d8e | -2.35473 | -49.01346 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 67e1f8e3-30f9-3f01-b889-d0a38f6a83c5 | -1.00918 | -51.72605 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e69382c-7221-3597-bc5e-f0a9a772959b | -3.74769 | -53.39146 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9f18445-9663-314e-a42c-c98177a14595 | -3.254 | -53.64732 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f27d2a0-22b2-3d2f-87b6-8be18532beee | -1.11772 | -53.73718 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d01f25c4-915d-3c76-8a6c-db136acdf936 | -0.26343 | -51.49131 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af56f1a-d7f2-3c40-9173-44f53ce976ab | -1.26663 | -54.55727 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README97.md)
