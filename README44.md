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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92f9d38b-fc46-3a43-8e44-fe0e45fef747 | -2.32142 | -46.1211 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8698c9a-5d24-3220-84e3-fc6265dceacd | -3.34375 | -50.50968 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 228671f2-4344-3de9-ac4a-71a9a38d6151 | -3.09685 | -53.2787 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3be8b5e5-ea62-37ed-80ea-fbd5cfaef09d | -2.1796 | -53.77424 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1177a862-6d4c-3c7f-b6c3-8fbeb0f82635 | -2.83226 | -54.12778 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 47e2645f-10ca-3f2d-bf89-1c92f3bcc509 | -2.54744 | -46.3996 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe5b4009-2049-3488-8659-1759a3740798 | -3.21929 | -48.82087 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24152c19-10af-3c4b-b37e-2cbcccb1aa42 | -1.42615 | -45.96328 | 2024-11-27 04:18:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf750a6a-668a-305e-9818-0b16d582fb71 | -3.32637 | -50.05785 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 111e8941-bd7c-3115-8d9a-469496edb1fc | -1.15087 | -53.67698 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f411491d-d26c-320e-b3c4-d17cb883b974 | -3.10402 | -48.0197 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad2d5075-0ef6-3f6e-a6f5-45b9f0fa98ee | -1.7923 | -52.74984 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28e06550-9b02-3376-86e6-cb696019a381 | -3.18626 | -48.43393 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da7b6968-0820-312a-9a26-dd808fec4ca2 | -2.73638 | -54.13451 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0b74592-6e2e-3723-b783-7b65d50b7900 | -3.44031 | -40.83414 | 2024-11-27 04:18:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c8f86a40-14ba-30e5-bc31-75eaa66fc2fe | -4.13986 | -43.84404 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30951a35-7621-381b-ad1e-952ba7209592 | -3.80908 | -46.60896 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30ee5d8c-6e4c-3387-9b00-2811b5922c2b | -5.32203 | -43.07311 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e50a501e-922e-3741-a979-e106be68b9c4 | -2.8333 | -54.1258 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 5ff5f278-8051-37e8-a972-421fef9e7a11 | -3.00268 | -45.46881 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cc407010-3b5a-3d1a-aad8-87a0f9744900 | -2.24341 | -53.63651 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a2880ca-09f4-3cef-9721-1cb59d91c7dc | -3.58764 | -50.3595 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b65980f-d664-3fbb-981c-ca04116874b5 | -5.3563 | -42.12508 | 2024-11-27 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9bb8799a-6b51-390e-8950-d88666b59748 | -1.67807 | -52.44063 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2546c1d-7b33-3b6e-bc18-fffd9d6ba720 | -3.09816 | -53.26603 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e2b45b4-58a1-3527-94ee-3eb1b85474fa | -3.28512 | -50.75862 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04b367d7-6b66-367a-b227-283dd2d1a079 | -3.9513 | -46.91157 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebdbf575-e4cc-3cc0-bbfe-4e07425fcd0e | -3.07084 | -50.94686 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2aa730b1-1fd7-3ac0-bf1f-9478b30779a1 | -2.80233 | -52.90912 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 333dd563-4a2d-3e87-93c3-824857741662 | -3.26755 | -43.04247 | 2024-11-27 04:18:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f010f95c-001d-3935-b0b9-53ff136fa1e4 | -2.16952 | -48.38169 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e3fd8a5-04b3-3080-afc1-9b6d13bfd937 | -1.67727 | -46.91898 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7dbd1af-728b-3f25-93af-2a71e22a9658 | -3.82947 | -45.93604 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7276346e-9790-3f28-97e3-73a12aab8b7b | -3.08651 | -53.27352 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0b02047-0ded-316e-87bd-e4642d2f45df | -4.32274 | -45.88696 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c2d2a0f-d7a5-3244-bdb8-4464b2df2ca6 | -3.10569 | -48.02222 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b7fc93ec-afe7-3fc5-a011-9f2ed3ef47fd | -2.87436 | -45.26329 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2485d5e-7420-340a-aaba-a9e3a4642e5b | -3.08517 | -49.21333 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0324ab79-e249-3c1d-a728-daef10688018 | -0.80684 | -48.0077 | 2024-11-27 04:18:00 | NPP-375D | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bf895fb-8525-382d-8858-1cb0cf07c073 | -2.97506 | -51.58017 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fdf2c7c8-9368-3e88-b83a-34222087e9c2 | -4.54423 | -46.79294 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4d0f831-770e-3a98-9e6d-c7072c35c65a | -4.91341 | -47.85924 | 2024-11-27 04:18:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90da4fa0-acf6-34ae-aa5b-dd558a2f60e1 | -1.06848 | -47.22347 | 2024-11-27 04:18:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23677c23-c35e-3da4-8807-1de53c35d387 | -4.71679 | -46.57235 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28ed89f9-64d7-308a-b37f-a9839aa05f15 | -1.48128 | -52.5358 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80f6f4ed-4f95-34f6-a2f2-94e1b4dbd7c0 | -4.22269 | -47.21614 | 2024-11-27 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc364bfc-f48f-3238-a834-a751b33897c2 | -2.50666 | -48.36152 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f8a4805-13a8-3555-8136-230a4c2ecfa5 | -3.38638 | -50.10238 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1edd91d-16c5-3de5-be41-d81d06fad798 | -3.09586 | -53.28018 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09fd9c38-e5ac-36ad-beb3-62907135c4ac | -1.95854 | -52.16551 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e93f36c4-52d3-392d-898f-3fd7063d306b | -3.10413 | -53.26894 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e5ccd56-949a-34c7-bec1-a5da4158e103 | -2.7013 | -48.65834 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31e10707-b057-3324-a6d6-6517dfc56407 | -2.81826 | -46.82832 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df1e3a7a-282c-387b-bc10-605fad3134a6 | -3.7697 | -46.51553 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6e7543f-11e5-3f3f-a922-4ed982b54ec3 | -2.4444 | -46.27517 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e842cf29-889e-3c40-bc37-7f6e2633bda4 | -4.00026 | -47.91567 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05e56ed4-46d1-3f03-b89b-e9e1a366e698 | -3.49407 | -50.45656 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e8cf97b-b011-3069-9f5b-0fe682f4a977 | -3.96266 | -46.90928 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a863246-7a7f-3c30-87e7-66b40452e8b2 | -3.26336 | -50.43689 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8eb8c2e-f666-3853-a514-a5301e2d0d03 | -3.93263 | -46.6478 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10ca8f96-65dc-3178-be83-69211d964054 | -1.31093 | -51.73874 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69032ea4-3ce1-3ba9-9bb1-37de736597b8 | -1.98911 | -53.29892 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 612d21f4-db2e-3946-b7e3-9ed7cee49503 | -2.88773 | -48.73892 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8752ab1-7419-3b9f-9e7e-61b1c4242901 | -3.89086 | -46.09846 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 680c271b-56cd-3e86-a624-f893030d6f7e | -2.8176 | -46.83243 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b17fb478-d1a4-3b37-b95a-59ed474ddd69 | -1.78323 | -52.73794 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08d283ee-4c7a-3847-bea6-da29c2501266 | -2.92572 | -48.63237 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82f8c82e-e233-3417-8af0-a914db9b4f0e | -3.07277 | -51.25771 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cb1cd25-3e96-3f10-9f35-5bbc94f94246 | -3.37998 | -50.11422 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4cd7006-ce3c-3232-978e-3c8125cde541 | -3.34625 | -50.75679 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a9eb896-5e20-38de-a1de-5831ba68d9f2 | -3.10473 | -53.2654 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ded6d0e-55d5-322b-b35e-35cbf91e5440 | -3.0884 | -50.35795 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83d9d097-bb0f-3904-a346-445bb24db1b6 | -2.11234 | -52.77767 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9ebb87d-3374-3fe8-b5db-faaabc7893ef | -5.83903 | -40.83663 | 2024-11-27 04:18:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ccbe6fd8-7db3-38b8-9401-c0edfab19c0a | -3.09927 | -53.26453 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 283c4c03-f332-3533-add2-0a4298ae6018 | -3.17391 | -50.2182 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9562d5c-4ce4-3d94-98a8-2932e96f6dad | -5.14939 | -37.74026 | 2024-11-27 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c289e81b-adcc-3774-8caa-d916d62478cf | -4.13632 | -38.69925 | 2024-11-27 04:18:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d8e287e-aa78-36ff-b390-a3dc0eed5267 | -3.81639 | -47.46961 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d45ab0-e3a2-316c-9789-54c6ed3250da | -3.37628 | -50.10927 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59e22121-0b45-3be4-b14b-76cb1d9c3027 | -4.0186 | -47.78034 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9160d31e-5f9d-3f71-8f76-23fed78797b2 | -1.31261 | -51.74154 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11307416-8f67-3ad0-87f8-b31f530d4990 | -3.93114 | -46.49932 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fd8583a-dbb8-3a5c-8ffe-a1c289b06c31 | -3.16661 | -48.43077 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8a9767c5-f913-3fa1-b388-40c1ed0cf8a8 | -3.24101 | -50.14104 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfe4732c-4171-3c52-a50a-705d716b5a6c | -4.26581 | -42.43546 | 2024-11-27 04:18:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4be86e1-cefd-3566-8dfd-eaa22678e89f | -3.39155 | -44.16838 | 2024-11-27 04:18:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cca1a7a4-7005-34a5-9e94-97a1b8d324f6 | -1.39922 | -46.15627 | 2024-11-27 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bc359a8b-2365-3ccf-bf90-7ce08bfa487f | -2.82776 | -46.83826 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a1c08e7-4c10-3b2f-8d17-72a82288a95f | -3.2298 | -45.92706 | 2024-11-27 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f995968-f4c5-3d52-ac27-0d41721be35a | -2.46726 | -48.79453 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb2bf582-9544-3b5d-af16-d65be735895f | -3.10292 | -53.27604 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8977ed02-272e-3a13-acb5-f5850af04314 | -4.65778 | -45.04069 | 2024-11-27 04:18:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 961e47b6-aae5-3c02-8ea6-a0144bc6c198 | -2.04108 | -46.5164 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ba9f5cc-e9b9-334b-8fc7-0a0f894e4848 | -3.27416 | -48.76199 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 764abe93-c51f-3db4-bfd0-1a6e4f50e9b5 | -3.50319 | -53.81271 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b97dda58-902f-33e2-afed-9f1340e00ca7 | -3.27904 | -50.0177 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60ecef10-bab5-32af-b1d1-9541e255fba3 | -3.4165 | -50.44209 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7e762ca-7c00-3952-926f-d99f6fdd5b91 | -3.67008 | -53.65876 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cda89095-d0bb-3dd6-a1b4-5ac9666edb31 | -3.46919 | -50.25817 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README45.md)
