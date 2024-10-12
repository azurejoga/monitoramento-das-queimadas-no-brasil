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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f712bc0-b7ec-30cb-b00d-021c3144bcf8 | -6.12551 | -47.87658 | 2024-10-12 03:42:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c86fc563-752c-339a-bd6e-db23aedf35a3 | -6.11992 | -47.86897 | 2024-10-12 03:42:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4055f8a-e25c-357c-8a2a-5544e7dd55a0 | -6.1188 | -47.87509 | 2024-10-12 03:42:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 488b436e-8893-35f4-bf41-7df7337bc58a | -6.51139 | -47.82784 | 2024-10-12 03:42:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 831781ed-8d5c-3894-8c88-ac75bedd24a6 | -6.5096 | -47.82498 | 2024-10-12 03:42:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a63bb68-e4e4-3613-9fa7-555a1ada2002 | -6.50855 | -47.83083 | 2024-10-12 03:42:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b848a0c2-39f9-343b-aa4d-278d42b4a9a6 | -8.73669 | -47.18459 | 2024-10-12 03:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58ad3ad1-2d03-3e8d-aac0-e97bcbc85895 | -8.73336 | -47.18299 | 2024-10-12 03:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| daa4d97b-fc03-30cf-bd24-3d251ccc249f | -8.73235 | -47.18843 | 2024-10-12 03:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e42c3db-8eef-38d4-80bc-cc3eb65e33f7 | -8.73048 | -47.18338 | 2024-10-12 03:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67f1ca5b-4661-3652-b7a3-4c0cda7d4d56 | -17.54608 | -42.30176 | 2024-10-12 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b4f2e74a-3c3c-3039-8c75-140fcd10dbd8 | -17.54546 | -42.30435 | 2024-10-12 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5b1bc4ff-d33f-3347-b6b9-f3b627655a7d | -17.54517 | -42.30687 | 2024-10-12 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 73cca88d-a984-3d84-952e-43823a677ae5 | -17.5422 | -42.30086 | 2024-10-12 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1efbf08-0ec4-3199-b737-be8f099df362 | -17.54159 | -42.30347 | 2024-10-12 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7a84ef40-6552-364b-a867-c9ff277b22b1 | -17.54129 | -42.30599 | 2024-10-12 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8593cd81-2943-3d0b-8f6a-12b34f1d5440 | -16.83017 | -42.87286 | 2024-10-12 03:45:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 709181ff-e852-360f-b68a-71b59bb1268b | -16.73653 | -43.02257 | 2024-10-12 03:45:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb332b5a-674c-33c5-ae53-496e88016004 | -13.70529 | -44.27002 | 2024-10-12 03:45:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a072def6-608d-3d69-b9f7-866f0cd796a3 | -18.03914 | -39.92568 | 2024-10-12 03:45:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4500b5ad-50ff-3c2d-a43a-1ee69e7fb9fd | -14.71162 | -40.36784 | 2024-10-12 03:45:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c5f044b7-b937-3972-8f42-04fd79043013 | -14.55658 | -40.18164 | 2024-10-12 03:45:00 | NPP-375D | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fff6ef7c-117e-35d1-b3cc-3bcb7c04fb3a | -14.22507 | -39.75911 | 2024-10-12 03:45:00 | NPP-375D | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff47883f-621e-3b52-8f60-791c29e02d80 | -18.66752 | -40.46226 | 2024-10-12 03:45:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 72d1ef9e-06a6-32c3-8596-742e9f6a28eb | -13.64109 | -41.35876 | 2024-10-12 03:45:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6e36a0d0-74c2-3a9d-8e35-11862016dc1c | -13.46735 | -40.84352 | 2024-10-12 03:45:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f2b7dd27-031b-3657-a36c-8fe39d0d4f67 | -13.46568 | -40.83996 | 2024-10-12 03:45:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc2de09b-8e8d-3fff-9d7e-0d3bae8a82aa | -13.46487 | -40.84468 | 2024-10-12 03:45:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 61d13764-65b2-3fbc-b2d1-ba81d893245c | -13.46355 | -40.84281 | 2024-10-12 03:45:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 13f1c1f9-f98f-3682-80f2-559e1dc57392 | -13.46107 | -40.84396 | 2024-10-12 03:45:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 007f3155-d9e2-3522-ab9c-0662b03b0481 | -15.03372 | -41.65804 | 2024-10-12 03:45:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eed2b850-9dc1-3d35-a728-06996a12dacb | -16.12282 | -41.62909 | 2024-10-12 03:45:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ce4711a3-688f-309e-944c-ad262f40dee1 | -15.26265 | -41.76953 | 2024-10-12 03:45:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5b674400-7d26-3460-8675-12227bf4e83c | -18.15967 | -42.44185 | 2024-10-12 03:45:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1fed595-8e1e-3683-82a7-886c9441f723 | -18.15918 | -42.4451 | 2024-10-12 03:45:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3610e590-d545-3a37-bb10-440f1084dc41 | -18.15872 | -42.44699 | 2024-10-12 03:45:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d65cd038-1c4c-342e-8382-32fc5c85194c | -18.15529 | -42.44431 | 2024-10-12 03:45:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e364d041-2523-34e1-ab99-19ab1647ad38 | -13.0357 | -43.25922 | 2024-10-12 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5efd4136-dca6-341b-af0c-7ccd8e950566 | -13.0337 | -43.25958 | 2024-10-12 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 17dba87e-72c9-3f3e-8e21-d836c18053b4 | -13.03123 | -43.25835 | 2024-10-12 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bbdc2e15-6dcf-3b5e-bca9-08bb6e5ae8a0 | -13.14499 | -43.37713 | 2024-10-12 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb96b67d-0219-33ff-ba49-69592b47c263 | -14.76768 | -42.31074 | 2024-10-12 03:45:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b7e2b95b-de5e-3f6e-9fee-d8446639fdb5 | -14.48204 | -42.34947 | 2024-10-12 03:45:00 | NPP-375D | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd40bd31-a7b4-3c7c-948d-ff0db72ab922 | -14.2159 | -42.31753 | 2024-10-12 03:45:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 047a8b98-6abe-3258-903d-60f28472f486 | -13.92413 | -42.39583 | 2024-10-12 03:45:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37e44915-bab7-384f-b5e4-10b7ea901ec7 | -13.91996 | -42.39511 | 2024-10-12 03:45:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d57e0782-e552-32ac-b296-de16f71864d8 | -15.39149 | -43.07236 | 2024-10-12 03:45:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f716432-ec68-334c-b44e-e5bb99a9ed56 | -15.60502 | -42.57012 | 2024-10-12 03:45:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2065e11-c6b6-3a29-a379-a35e7be01430 | -13.70871 | -44.04251 | 2024-10-12 03:45:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0e89888-7a52-3238-83db-361db700bcb5 | -13.70656 | -44.26699 | 2024-10-12 03:45:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ea92683-cb68-3c07-b6dd-9b87e1a49f26 | -13.70559 | -44.27202 | 2024-10-12 03:45:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 470b617b-2265-3074-b01a-9cbaa7989905 | -13.37327 | -43.79429 | 2024-10-12 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef08d5d3-70d3-3520-807b-7cd5863f5e9c | -13.36919 | -43.79662 | 2024-10-12 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 148288f4-cd82-3137-95a7-ca7f85527f9d | -13.36867 | -43.7934 | 2024-10-12 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1d6aeae-fb95-3b21-99f4-fd10e4711600 | -13.35453 | -43.6692 | 2024-10-12 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 00d5c684-5acf-371a-942f-c7c766bf4912 | -13.34996 | -43.66832 | 2024-10-12 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d20bf0ce-2d74-339d-82cb-82107f241703 | -13.19239 | -43.50404 | 2024-10-12 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79463c55-f4fb-3c70-8a79-1bc018c45f2e | -13.19134 | -43.50625 | 2024-10-12 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7651909-0ee5-31a7-8a44-614c461e8a48 | -14.05758 | -44.48755 | 2024-10-12 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4f1d709f-5ca6-3df4-a468-1a6e713e1570 | -13.93432 | -44.04416 | 2024-10-12 03:45:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da5d8224-d82e-30a9-9fc2-4f344629fdec | -13.87397 | -43.78827 | 2024-10-12 03:45:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b65cf58f-0b3d-3911-9f84-614f9ece810e | -2.77 | -51.3829 | 2024-10-12 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 48165c07-39e4-3dbc-9ced-cf8a8db26618 | -2.7701 | -51.3622 | 2024-10-12 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9ddaf8dd-62a6-30a5-93e7-cbdaab2debbe | -2.7884 | -51.3825 | 2024-10-12 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2a08ac08-29b1-30d1-9fa7-442120090a6b | -2.7885 | -51.3618 | 2024-10-12 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 17f72741-4e83-3bf8-b18e-a6e39705cf11 | -2.8254 | -51.3401 | 2024-10-12 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1f6d916a-9429-39b1-9a45-b75b392b6b52 | -2.8319 | -49.5385 | 2024-10-12 03:45:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c3985b90-1cde-3a40-8e52-9f3fa04d6858 | -3.6978 | -50.1225 | 2024-10-12 03:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f6398a83-7d5a-3f23-a24d-8db3373553f6 | -3.9394 | -46.445 | 2024-10-12 03:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 3a9c3733-d3c2-3687-88eb-ff3ddb4ab561 | -3.9396 | -46.4229 | 2024-10-12 03:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 90252743-0a7d-3cf3-8f4d-fb9c58268e4e | -3.958 | -46.4442 | 2024-10-12 03:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.7 |
| c1aab164-b04c-3fa9-b6b1-02f633224b81 | -4.1148 | -48.2515 | 2024-10-12 03:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 4dce4f83-3b86-3bd0-ae78-059bcaade3db | -4.4538 | -44.5763 | 2024-10-12 03:45:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 085928e8-8c8f-31ce-883d-5512f38f3a72 | -4.2665 | -50.9594 | 2024-10-12 03:45:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d6a82352-40ce-3bfc-b4e8-b15c695cc0bd | -4.5859 | -47.0968 | 2024-10-12 03:45:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 147ea201-3317-39ad-a1ef-35e663f4a1ae | -5.2486 | -48.0424 | 2024-10-12 03:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 557a4f7f-e0fc-311a-8483-b2ae8ce655c1 | -5.3998 | -45.3348 | 2024-10-12 03:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9eb54761-8a30-39dc-9051-24b2457960f6 | -5.3997 | -45.3574 | 2024-10-12 03:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 4a45e29f-183e-38fc-ac70-5b9c0236b002 | -5.3995 | -45.38 | 2024-10-12 03:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 9fb712d1-1f4a-39f3-a087-94c303aa28a1 | -5.381 | -45.3586 | 2024-10-12 03:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2e9c0713-ad65-3737-9e15-e77072853de8 | -6.747 | -59.3259 | 2024-10-12 03:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6d640e64-2181-38ad-8990-eca846af033f | -6.7469 | -59.3452 | 2024-10-12 03:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 9001474b-fffc-34fd-a5d6-509ede8c553b | -6.7285 | -59.3267 | 2024-10-12 03:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| cceb72ba-84ea-3bdf-9180-3a9485734e7a | -8.4231 | -55.4704 | 2024-10-12 03:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a7b04288-ca95-34c8-8d08-15999d01b6ba | -8.2325 | -61.1823 | 2024-10-12 03:45:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b7b8be30-e213-38d4-a648-a7dab94a3c12 | -11.8377 | -58.8445 | 2024-10-12 03:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 81736296-e9f8-3730-8042-23538626301c | -12.456 | -54.5554 | 2024-10-12 03:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4c2588c4-66da-3490-a124-3eec1b880b4b | -12.437 | -54.5573 | 2024-10-12 03:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 05ab2987-f6b4-36f8-b84a-9e1e21c8f5c3 | -12.8135 | -53.4861 | 2024-10-12 03:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 77a6e310-ea8c-3a65-9d61-4632255dd438 | -12.8132 | -53.5069 | 2024-10-12 03:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 23c040a5-8c1e-385e-a9e9-6f6e4ffcb78f | -12.9652 | -53.5527 | 2024-10-12 03:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| b22ec918-5f6d-3732-83d9-add3e4451eb0 | -12.9655 | -53.5319 | 2024-10-12 03:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 238.5 |
| 00035e70-fc98-30a6-87a3-1c52443da6a7 | -12.9658 | -53.511 | 2024-10-12 03:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 76e82e92-d37d-3c24-88ea-9cab82a4797a | -12.9467 | -53.5131 | 2024-10-12 03:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| b4fba6ee-81bb-3efa-a072-e8c9c3f2f603 | -12.9464 | -53.5339 | 2024-10-12 03:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 231.7 |
| d829f760-f42d-34ae-8569-3d6e2ca1700d | -12.9461 | -53.5548 | 2024-10-12 03:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0a87ddc6-45e5-3ef7-8f0c-62a93b47fd34 | -14.3246 | -57.6002 | 2024-10-12 03:46:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a8dc0074-ecd4-3de9-a1ae-6f0c8e2bc71b | -16.9998 | -57.4586 | 2024-10-12 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| e5974ad6-98bd-38cd-9b09-62671aecb660 | -16.9805 | -57.4404 | 2024-10-12 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 212d5831-4010-3631-baf1-e677b257183f | -17.1761 | -57.4585 | 2024-10-12 03:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |


[Clique aqui para ver as próximas entradas](README39.md)
