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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a88557e-fc0a-3506-ab9c-f7746a4e019e | -8.50489 | -43.32232 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 933b5a1a-8c85-383e-b45a-00a17e5f8d95 | -10.56925 | -49.12756 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5270cb6-a9d9-36b2-954d-73dab8d8466e | -13.33505 | -52.92198 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a94ca5b-e1c1-302c-99a9-c8bb44544f49 | -8.49791 | -43.27515 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 3d7fdb70-c798-39d2-8d5c-3d39fe2c1542 | -13.33496 | -52.92644 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f09abdb9-da71-3211-b04d-ecbd3426b24e | -7.70849 | -45.77253 | 2025-07-10 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2508ce25-94ee-37bb-961a-31abf107524f | -8.49816 | -43.29606 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| db699f42-ac28-3531-9544-cc4de0a3903e | -9.30245 | -40.23843 | 2025-07-10 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70b4d23b-f848-3b31-95f7-f945465955e1 | -11.95734 | -46.35646 | 2025-07-10 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d28f1976-f26f-3dd5-82db-9b327e2881e4 | -7.48511 | -43.93757 | 2025-07-10 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0236043a-d4d6-3aca-91c0-64af0584d2a3 | -13.34777 | -52.89529 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b1e84db-cc34-31a1-a902-b1387af51969 | -13.00801 | -46.28646 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d5beda3-ac20-31ac-b716-a8759bb132d0 | -12.56612 | -52.21967 | 2025-07-10 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05ec7f92-be38-30bd-9b7b-ecd5a1ca9753 | -11.45821 | -45.10666 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dd8ab79-7ee4-3904-a3a1-4d46ccbb4085 | -13.33691 | -52.91714 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5c65f8f-4288-374f-bc4b-72f8c0008790 | -10.57816 | -49.13512 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 389c47af-0885-3d11-8765-0666b802dbb8 | -8.50464 | -43.30134 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 92c7bcdc-0c26-34f5-83ce-968bbb35da9e | -11.87684 | -46.76511 | 2025-07-10 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf994025-df29-3ae7-bf92-e9feca421891 | -13.34668 | -52.89552 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d34864a-38c8-3ba9-82ed-33c7338a756c | -8.50504 | -43.27636 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e00a0be4-638b-3971-b516-fc713f49eb5b | -7.46117 | -49.40299 | 2025-07-10 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8669042-f8d3-34b1-9dc1-2867a7f7fb12 | -8.49949 | -43.28792 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3afe3336-7c03-3c48-9f36-85bce951b4a5 | -13.89958 | -42.13229 | 2025-07-10 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 437be3f1-7c3d-3a91-8475-6fa7f5212c9f | -8.5004 | -43.30481 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 291c5332-0d8d-3183-912c-be1ef03e8671 | -8.50726 | -43.29609 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| d9de98ff-65ac-3c3d-a8f0-42133133eeb5 | -11.67504 | -43.78168 | 2025-07-10 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5e266dd-0958-343c-b885-f306c467ce02 | -7.72513 | -46.61375 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd9c5aac-3dd0-33a8-bca0-71dff9c55d98 | -10.63113 | -45.23419 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f789fb7a-d6fd-3719-aaaa-3c96c9ed86c4 | -10.65839 | -49.45637 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 568f233c-8717-3534-a228-ced05c7cd9ba | -11.3817 | -48.05574 | 2025-07-10 04:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e646a83-5570-3440-825e-3141a2873cb3 | -8.50081 | -43.2798 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 9d1214c2-cd67-33cb-bbf1-fd2363900aa2 | -9.21726 | -48.60191 | 2025-07-10 04:04:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 090a928a-41fc-35bc-9dd0-5e5acdcf0185 | -13.89568 | -42.13529 | 2025-07-10 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3844459e-59e6-30b1-96a7-e79f536bb419 | -8.49725 | -43.2792 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| ec8f20e0-bf22-3877-9002-2aa2f01bce07 | -11.36928 | -48.70689 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8003dcb2-82d1-3e5e-972a-4d9dfb240578 | -10.66236 | -49.46339 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b18d9967-e139-38f7-95aa-12cfd46845e8 | -11.36487 | -48.70228 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91083eb7-46b3-3039-90e7-c940e3a84df9 | -7.20589 | -45.35222 | 2025-07-10 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5900a5fa-26a5-3509-a05b-4712bd930312 | -12.56697 | -52.21544 | 2025-07-10 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c36d1c3-535a-3831-985e-9398ed9c4225 | -11.36863 | -48.70856 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 267de81f-dbbd-3a2c-b219-d45f0daaabb6 | -10.57711 | -49.14081 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 45f96d93-ba7d-3cb5-9dfc-b2cc0ec07062 | -8.99498 | -47.45328 | 2025-07-10 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39d1b788-a467-35a6-a601-37ef8dbd81ad | -18.64508 | -55.7173 | 2025-07-10 04:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3055a363-0637-3f87-a212-813f1cfa966e | -19.6973 | -44.61742 | 2025-07-10 04:06:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 989049f3-930e-3f53-a0c5-0fe32d992b67 | -18.65016 | -55.72459 | 2025-07-10 04:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 72143de3-65ae-3133-936c-b31eda3224df | -19.98033 | -47.18581 | 2025-07-10 04:06:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d1657a7-4e12-35cf-9b47-f2554fd91385 | -19.44542 | -48.53926 | 2025-07-10 04:06:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 874c713e-7e30-3322-a2f1-5569e26adcb9 | -16.68151 | -43.88291 | 2025-07-10 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd373877-0436-3ba6-8415-44b9a861ae5e | -19.95882 | -44.70763 | 2025-07-10 04:06:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 392f24e1-f681-31e2-9022-3cdd934cc8ff | -16.58029 | -43.64649 | 2025-07-10 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e93a94ee-a299-3b1e-8d39-cfa270548a5c | -15.92336 | -43.51807 | 2025-07-10 04:06:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d6fcd67-f9ba-33ef-9c8a-228339711d8f | -17.6534 | -46.83356 | 2025-07-10 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a690c93-da71-3400-bc9c-768b0a7b6ab5 | -17.65483 | -46.83701 | 2025-07-10 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a395266-7ce1-3824-b9fd-dd36bc08279f | -19.45023 | -48.53629 | 2025-07-10 04:06:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 770d126c-2a2d-380d-804c-d23eb547e7b1 | -19.05764 | -48.33384 | 2025-07-10 04:06:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef37bbe-1cfb-3c86-a9ab-a8dce4101c3b | -15.47516 | -45.19562 | 2025-07-10 04:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 911f2519-5530-3762-904e-86b13558f671 | -15.47441 | -45.1999 | 2025-07-10 04:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d5d374e-5cc0-30b2-8dae-68b9a23408e5 | -15.92397 | -43.51435 | 2025-07-10 04:06:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2030be9e-dc87-3186-be43-288c45cecd61 | -20.07865 | -45.81642 | 2025-07-10 04:06:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cdc9d4e-a119-3f9e-9160-fb149e29f045 | -18.64463 | -55.72296 | 2025-07-10 04:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2d1f65f6-7c04-310a-97c6-5c165ff72d34 | -18.64376 | -55.72292 | 2025-07-10 04:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cd92c76c-972f-34b9-9ef2-25cba9e5b10b | -19.98101 | -47.18394 | 2025-07-10 04:06:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4ad9768-fb24-35ce-8587-22e600a87974 | -20.56968 | -47.86749 | 2025-07-10 04:06:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4ab5d03-49a3-3e05-a942-ccd44a312ed2 | -16.84562 | -49.35619 | 2025-07-10 04:06:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7810f50b-4638-361a-bc74-f0a89c683b03 | -16.06286 | -51.56052 | 2025-07-10 04:06:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a4636c-ca97-3c55-8ac3-714da5e41ff8 | -17.65632 | -46.83918 | 2025-07-10 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 891b6fa6-d310-3b81-950b-6a823ca3b3e2 | -16.84652 | -49.35146 | 2025-07-10 04:06:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8e805f0-348d-3ec4-8d17-5d358b459443 | -18.65148 | -55.71897 | 2025-07-10 04:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d8b429d0-40bf-3b9f-931a-adfc8d2f7c33 | -19.36901 | -51.39501 | 2025-07-10 04:06:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceb31787-1c6c-3a17-8b69-1498098883ed | -19.44947 | -48.54026 | 2025-07-10 04:06:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8b7f93ee-a139-3a15-83af-5abc5290b63d | -16.84201 | -49.35056 | 2025-07-10 04:06:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09de4d73-08ee-38b5-8a94-45e90442712a | -16.58413 | -43.65057 | 2025-07-10 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9e4665e-a111-30c5-93b3-4e48055546d2 | -19.96432 | -44.71662 | 2025-07-10 04:06:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 213f32ec-ed43-3ed7-aaa7-a4f5357b19a9 | -19.37418 | -51.39853 | 2025-07-10 04:06:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 455208f7-0468-3fe6-9f48-394a0c0c9013 | -19.37275 | -51.40183 | 2025-07-10 04:06:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d7dd866-931c-3b75-af4a-0ffb584bea3e | -20.19441 | -49.12214 | 2025-07-10 04:06:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f0bb7b6-884a-3f54-8f02-ea2fca04acf0 | -14.72084 | -48.4039 | 2025-07-10 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3683947-bde6-3b1d-84ad-e4d14bdaff94 | -20.76523 | -46.76877 | 2025-07-10 04:06:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7089ed1c-d4f4-3656-95a0-72bcce6d4c36 | -18.79299 | -47.96259 | 2025-07-10 04:06:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 393d5e63-cd1e-3c00-ac7f-a0acc50721de | -17.65863 | -46.83775 | 2025-07-10 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 204ce4e8-95aa-3be0-a14d-963c166d4c02 | -16.06219 | -51.56379 | 2025-07-10 04:06:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37180d8f-e190-3de6-9b2d-0b8cc42119ce | -17.8676 | -50.71741 | 2025-07-10 04:06:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e747d29-6a73-3d3e-86dd-4282e2890e4d | -17.0709 | -43.93955 | 2025-07-10 04:06:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69caf8ad-32d8-393f-9b28-49e190c44f75 | -16.58474 | -43.64685 | 2025-07-10 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca590ff5-168e-356f-87e5-176eb54ef511 | -18.64592 | -55.71733 | 2025-07-10 04:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e0bf9766-e46d-309d-bc21-0e94c0b19c1e | -20.19589 | -41.37705 | 2025-07-10 04:06:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 905d773c-53d4-314e-9ab2-03b0bb66b46f | -19.05693 | -48.33763 | 2025-07-10 04:06:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 542f3c18-f041-3341-a375-27fb8fb0d6bc | -18.789 | -47.96175 | 2025-07-10 04:06:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0bad80e6-64d0-3eda-9cb3-af6f823da679 | -18.65103 | -55.72467 | 2025-07-10 04:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1fb36a89-e054-3750-8290-dd31b3ed80b0 | -19.44806 | -48.37024 | 2025-07-10 04:06:00 | NPP-375D | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75a8e508-63c4-3586-ab26-7f5ba15681b0 | -19.37391 | -51.3961 | 2025-07-10 04:06:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fd67181-9019-386a-a310-3402eb34dd60 | -20.19362 | -49.12619 | 2025-07-10 04:06:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf43e5bd-b88f-3205-8c38-6e0b3ecb0b47 | -20.41731 | -43.55169 | 2025-07-10 04:06:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ac7a0ae8-d1a9-3f90-af7b-20b8292afa1b | -20.28877 | -46.67114 | 2025-07-10 04:06:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 928befb4-36d8-3880-801b-d47891bea28f | -19.96771 | -44.71728 | 2025-07-10 04:06:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7610afb8-b799-3982-bc58-980e24d0754f | -16.58137 | -43.64626 | 2025-07-10 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d78dad1-40b9-36fd-afd1-c9d99d321298 | -18.79782 | -47.95889 | 2025-07-10 04:06:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 43ad6423-f5b7-38ef-a37e-d239fa9d8f58 | -21.76591 | -48.12584 | 2025-07-10 04:08:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1fd38c3-6b3c-39b7-8643-3336f14c090a | -25.19203 | -49.32756 | 2025-07-10 04:08:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a1091b5-9b1d-3948-a900-fe55b7c6ed23 | -21.34954 | -48.62239 | 2025-07-10 04:08:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |


[Clique aqui para ver as próximas entradas](README16.md)
