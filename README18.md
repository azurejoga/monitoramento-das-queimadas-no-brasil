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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93252f44-9c59-3a5a-9d71-011775ce31e3 | -3.57331 | -50.67517 | 2024-12-28 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 855b09c1-ba9b-3a72-b6ef-fdd872367b64 | -4.03886 | -46.71888 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 683488f5-c0d1-3e6c-80d4-2c67f941d214 | -4.00035 | -46.94243 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e9999cb6-82a2-3f43-91a8-11e57fb53092 | -3.72597 | -47.17947 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b159cc74-584e-3ac0-9c8f-b048c9f7af74 | -4.33697 | -46.4947 | 2024-12-28 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4345a8c-b04c-382c-a5de-d5184c6d2451 | -3.81681 | -46.73356 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13728a0a-25d4-301f-86b6-8cf98b10ce14 | -3.84034 | -46.68145 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ba77870-104d-316c-949f-f468fb7cbdff | -3.75842 | -47.21844 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f998c3c-27ec-3672-86e9-5352f964ba5c | -3.89583 | -46.98865 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cee9a6a-0875-3bc8-aebb-0d314347127a | -3.79726 | -46.85854 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c19f23-4714-3a24-a215-10e40cf78bcb | -2.87544 | -54.2103 | 2024-12-28 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45caf934-8337-3c09-b297-96a191016436 | -4.08984 | -45.30609 | 2024-12-28 04:38:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1559b391-f6c7-3aec-b42a-0e0df8c43494 | -4.11985 | -46.71105 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd564a5c-1152-34a2-a89a-6a2831e07fbe | -3.99644 | -46.69273 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 375a6f23-db3a-3c46-bc7a-c2715d0a4966 | -4.08988 | -46.81241 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac02c6f-2417-353d-a8b1-b6d94ae85916 | -4.56281 | -45.98822 | 2024-12-28 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 04d0bed4-b08b-334e-a211-5d80468cdae8 | -4.04524 | -46.72376 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c01fe7-0282-3998-8afa-1bcac49ee964 | -4.06177 | -46.99415 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 24445af0-3ac7-35df-9e0b-0eaea5055847 | -4.04389 | -47.04117 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ccc10f6-4889-342c-aac1-283070404fb4 | -4.00797 | -46.91642 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a10ffa6-c651-3c34-8d17-890ca70158cc | -5.31579 | -46.05822 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 857c313d-0a0f-3ad5-b0b8-02cbd680c027 | -3.91678 | -47.02538 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39deefcc-8408-356f-8ee5-e700f5dbc79d | -5.21117 | -41.24154 | 2024-12-28 04:38:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 14f421b6-a8e8-30f6-bd7f-08dc4677f06e | -3.18529 | -46.13437 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 623584da-724c-309b-bb7b-4efffbd19f74 | -4.83714 | -45.97441 | 2024-12-28 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59af2b7c-69ab-37c4-821b-618b94be8fe3 | -3.96984 | -46.58581 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a860bdc2-b40f-326a-a615-83beff8dc6bc | -3.96871 | -46.89519 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2994023b-75f5-3da9-ad4a-25a88191f90b | -3.34085 | -50.38156 | 2024-12-28 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 847e0be1-009b-3495-b500-178ce10df032 | -4.50346 | -44.23615 | 2024-12-28 04:38:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2380f56-4a41-3162-bf1f-5001f988d95f | -4.09744 | -46.80964 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0ecfe22-cbde-355f-b62b-6b6714259dfd | -3.81044 | -46.72869 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fc7cc00-bb6e-39a6-8670-1eb368e34178 | -3.19539 | -45.99646 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba3a83a8-8e35-3cbe-8a99-6e621546acf7 | -5.63559 | -43.72281 | 2024-12-28 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 626047cf-736f-3137-a0ba-00edf3a04038 | -3.74705 | -47.20158 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8faf3f10-10dd-3bbc-a5b6-9cb8b03cc82b | -3.90938 | -46.90224 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59116a86-76e0-3d25-870b-fc0ba8f33683 | -3.73855 | -47.34598 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1577a01-7935-3e22-9529-869a2333ac22 | -2.5205 | -51.86311 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d2dfca-3ad2-32ee-ac77-6ce4645ab196 | -3.87065 | -46.94617 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9eed30af-8d48-38e1-97e6-edd9fe899d4e | -3.91107 | -46.91406 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4407e32-da99-30ff-9536-8081dde32c46 | -3.91101 | -46.93706 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b8b7d4e-f096-3679-9b50-cec4c13d9809 | -3.93803 | -46.34879 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d64fc62-31a2-3726-98ab-dfa6ba1767f2 | -3.91284 | -46.9028 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c64035d9-7fa5-3c11-95fd-fc0893a12c5f | -3.19835 | -46.00105 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20618a4f-758e-3f40-8100-c06e6a14c46d | -3.53228 | -53.80162 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 603472b4-2db4-39f3-85c3-23d918132560 | -3.91735 | -46.88319 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e622a877-7481-3f2c-86db-9dfa13351cc9 | -3.95632 | -46.67452 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f368576-c1ff-35a2-9fe3-bab6ec46e350 | -3.73509 | -47.18844 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fe7bcc9-836c-39ca-a26f-52722e59e12b | -3.81842 | -46.63165 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d69a242-ab86-3235-95ec-8633bd81c760 | -3.58737 | -53.71394 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9773bc4-f6cf-3ba4-b673-cb928c1d4061 | -2.48474 | -54.16934 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 905ae3fe-5c6e-30cf-9342-20d2e93fb1d0 | -5.71255 | -43.25985 | 2024-12-28 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a23b4819-f499-35b9-8b5a-0277b7aa2796 | -3.72425 | -47.19053 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbe995f4-0db8-3ef5-b9b9-bf1071c9f39d | -1.95172 | -54.10092 | 2024-12-28 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 496479a8-2437-3fb5-a136-c2578d0fd8c1 | -4.40872 | -50.43012 | 2024-12-28 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e323aeb-0955-3a2a-899e-f83b0090f692 | -3.92132 | -46.66632 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fe6c96f-40f2-3f85-9d2e-cc97b613b200 | -6.11829 | -43.94758 | 2024-12-28 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03e32fc6-f997-3c33-ad6b-24f5b382da48 | -3.18651 | -46.12637 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d459676f-9a7f-36fe-a09d-3bf812944a07 | -3.93996 | -46.75839 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2d5bfbd-8309-3db2-a7ba-5e54a31d02c2 | -4.01033 | -46.71846 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e03fba0f-bb82-36db-9ad0-8923f7189fe5 | -3.90985 | -46.93225 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c30982a-e9f5-3e09-a03e-caeddc62ca2c | -3.1859 | -46.13036 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56e14668-dd69-3759-a112-45e3cacb2fff | -5.73774 | -44.43036 | 2024-12-28 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a1a7fec-5926-3d42-9f4f-f95d2019488d | -3.91563 | -46.94074 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a051d1fc-3a1a-3375-8cfd-67598a1648ca | -3.91909 | -46.94127 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ae853d6-b44e-3590-8383-6050a9254e0c | -4.01093 | -46.71462 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06357bad-1061-3db7-b074-dafd85012996 | -3.96562 | -46.68391 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bbc6496-ff90-3c03-a436-6339697aed4e | -3.85955 | -46.67264 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 259356c2-5f42-336f-8be1-6f1f5c032e03 | -4.7442 | -44.64579 | 2024-12-28 04:38:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b655fc7-9b77-3767-a08d-9a33f1cd864a | -3.90044 | -46.98175 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 55055fe4-007c-3a49-84f5-78c27c4009cb | -2.95478 | -51.76187 | 2024-12-28 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56fe1b1f-57ba-33d8-b83a-fe03996b0224 | -3.99401 | -46.73162 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e339e7c-cbae-3c3b-8a8d-f4bd3b297258 | -3.19057 | -45.99297 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed37570a-8817-3f35-ae04-d52b9b4ccf56 | -3.76565 | -47.21535 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2494dab6-a658-37cc-ba1f-cc926154afdf | -3.90389 | -46.98229 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74a5100f-2735-3d5d-9044-dbb9fb00f32f | -4.03986 | -47.04439 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dee9aca-7bff-3fe8-b05b-ecf9c626ac66 | -5.56643 | -46.2928 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9283e6a6-3943-3ffd-a964-ed566b516db6 | -4.55823 | -44.06717 | 2024-12-28 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fe8a05e-4586-3984-8a40-ae26003ff314 | -3.91492 | -46.66145 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa47ce7b-ac9f-3904-b49c-42de18b6314e | -3.84383 | -46.68199 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a922609-c4f2-3afa-b608-5bd0ba5714f9 | -3.91782 | -46.6658 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 576806fc-da2b-30e3-bad7-25e37850e62d | -3.84174 | -47.04123 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb778896-c74a-3ee2-9ab2-78761b747bc0 | -3.82193 | -46.63212 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f16d3cc1-7bb4-3d93-90cb-c36a8e84796b | -2.2257 | -50.45633 | 2024-12-28 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 640e2b22-e25a-3d02-82b3-28fea19ef5e3 | -5.57658 | -46.12728 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 2d41cfda-77e3-3968-aa7d-8384157d27c6 | -3.71882 | -41.69738 | 2024-12-28 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cb4f1d64-9aaa-3104-b405-94cc7482dccb | -4.2263 | -46.78953 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94bffbfb-4ad9-3db3-bbe7-4c3b224e9702 | -2.8869 | -54.02169 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee6859bb-c8a2-3894-8fbd-a8d0cb3a38a0 | -3.91176 | -46.88707 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b85e996a-ad6a-3e9d-aa21-7e160dfa9cb5 | -3.58978 | -53.7109 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a380b64-34dc-3742-b46b-8590a46da50b | -2.47996 | -54.17242 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 98b4e57e-f475-31c2-b53b-e61dac4f8e9c | -1.45804 | -53.55871 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86814a8d-0af0-38ff-806c-c211f2a6f963 | -2.28396 | -45.59362 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ca73e60-19c0-3e36-b87d-17f59ab7d7ad | -3.9843 | -46.90898 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da8144d9-2113-35fb-8852-e1aba6377cb4 | -3.84265 | -46.68973 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52dc2ea6-d1ef-3eae-abde-6e94c6cb923f | -3.98093 | -46.60719 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b03cde5a-1a0a-3a82-987b-db674ecfabf9 | -3.99632 | -46.73978 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9b269c2-f2ac-3c07-99a2-8c41827ab710 | -3.99236 | -46.92557 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce966a6-37b9-38f1-af08-f4ceec492db1 | -4.01676 | -46.56099 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a63f629e-43ab-3a25-9882-44d1df48fc33 | -4.05195 | -47.0347 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e16332a9-4d35-352f-af69-fc5be3a054c8 | -3.80288 | -46.73143 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README19.md)
