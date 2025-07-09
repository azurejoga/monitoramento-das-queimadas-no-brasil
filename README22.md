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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d6b7ce7-7092-3474-801f-cc527eb69b18 | -10.70375 | -48.43402 | 2025-07-09 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44d6bffa-1234-3d32-bbde-06e2cbf48edb | -12.05454 | -48.54312 | 2025-07-09 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 529ec12b-6b6b-3b4a-a8c0-4d2137eb4205 | -13.02002 | -46.28934 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60397cda-df98-3bc2-9115-158917ca1f8d | -9.92783 | -59.93731 | 2025-07-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eea5ef69-f472-33ae-9b05-9e279b991edc | -11.66895 | -43.78094 | 2025-07-09 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ba0c3fb-a584-38d2-9299-dc92715159fc | -11.52766 | -48.95924 | 2025-07-09 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e74eec47-8f60-38ff-bf5d-6dbe97dad453 | -8.54457 | -49.94778 | 2025-07-09 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54b28bf0-da79-3603-afa8-bb9943c6887f | -14.87885 | -48.37582 | 2025-07-09 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db93b163-0e55-3b38-ac42-db5325234c51 | -16.63056 | -42.20845 | 2025-07-09 04:46:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71e64540-7b47-33ab-acd9-2b71283675fb | -10.58037 | -49.12373 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 84a0cda8-b1c2-3965-8006-11a9047231a0 | -10.34499 | -49.91768 | 2025-07-09 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6535bc6-dccf-3cf5-a080-2f536dae5db6 | -13.92694 | -43.94818 | 2025-07-09 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38a1a3b2-6552-3202-9d65-06eebe5ed0cc | -11.43121 | -45.10503 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84ac9a2f-6e11-333f-96ee-cd703f8287d7 | -9.40741 | -48.44659 | 2025-07-09 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8f872e0-c395-3ca3-a731-e25b5f62f182 | -13.00828 | -46.7567 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d4bd111-ec80-360a-af82-d9f61bb7b155 | -9.33413 | -58.84465 | 2025-07-09 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af241ff2-0be1-3025-bd21-b2cae92a331d | -8.97209 | -49.85263 | 2025-07-09 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a04f28f5-7417-3b6b-966c-624b871db26b | -12.0596 | -43.51184 | 2025-07-09 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 520ec7f5-2765-3938-9c35-637a97800237 | -8.58413 | -49.87087 | 2025-07-09 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe838475-599d-36a2-b73f-d17616f88a31 | -10.33991 | -52.55011 | 2025-07-09 04:46:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 631dcbab-1394-3f48-9ded-d798a76139fa | -12.57837 | -56.97023 | 2025-07-09 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f085aa2-6f64-361c-87f3-754c2f1280d6 | -8.76236 | -47.66911 | 2025-07-09 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff49bd8-904e-3c3d-8edc-1c937031de72 | -9.29048 | -44.83957 | 2025-07-09 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80564838-74fb-31dc-8b24-106c746ddaa2 | -9.92884 | -59.93179 | 2025-07-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33e2b323-1773-3d1a-a758-92a68d4cf0cb | -11.10668 | -48.87651 | 2025-07-09 04:46:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e09f163-16df-3e27-80e9-57559c31d356 | -8.30611 | -55.10746 | 2025-07-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ac19055-0546-3eb9-9559-b06890621c1b | -11.42329 | -54.33385 | 2025-07-09 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b73d2135-a24c-3147-8f49-955f7b31595b | -10.65035 | -44.48413 | 2025-07-09 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9994c399-f1a8-31af-bf59-42deeaf59ad9 | -13.00574 | -46.29587 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf6eb31f-b5a3-3f52-ad5e-f8dbc65a10d6 | -10.34444 | -56.49332 | 2025-07-09 04:46:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 523a6b81-3ca1-36e9-af8d-260507daea61 | -16.62541 | -42.21512 | 2025-07-09 04:46:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 880ecc06-b45c-3e9a-b1da-beca8858df5c | -10.57619 | -49.12725 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ce795dd8-70ac-30ee-8b48-438b3c5e0668 | -8.76205 | -47.6718 | 2025-07-09 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d5176d0-97b8-3d5f-8420-01fff6d380de | -16.62586 | -42.2106 | 2025-07-09 04:46:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2a6b6a28-48f5-34a2-a860-e54c6a94c6d7 | -11.80981 | -58.85054 | 2025-07-09 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 381e0aa6-fbb4-3d1c-9e84-8ea8bb37d19b | -9.41256 | -58.90805 | 2025-07-09 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b1b316f-4f78-3f42-996d-c46f058c0a53 | -11.43251 | -45.09519 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b6c0c4b-7275-351d-bad1-98ab3275b871 | -10.18295 | -51.15016 | 2025-07-09 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1a94d58-d15c-35f2-af04-ba96cef2d899 | -13.10381 | -46.87962 | 2025-07-09 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf93e9e5-60d2-3f43-9091-f8767f8b6130 | -10.57741 | -49.11906 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2180a7f9-c97f-351a-89c2-d9e21805685a | -10.17796 | -51.16026 | 2025-07-09 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c16aeb81-b6a9-3a39-a177-3e3b608a5610 | -10.57262 | -49.12666 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 42a7a0b6-286e-3dc9-a6b3-740280ec3a19 | -15.61926 | -46.46155 | 2025-07-09 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0be69ac8-b344-3aaf-8b8f-c0e7c7957e4a | -9.02135 | -61.23417 | 2025-07-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 056e0857-6965-3d89-9974-6af999e0c9c5 | -12.05013 | -48.54716 | 2025-07-09 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f6db8f2-1c1a-32c1-9466-8ae832e7e494 | -12.47093 | -46.90936 | 2025-07-09 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c1c2fe1-f176-3962-8f3d-287080d4dddf | -10.63077 | -49.4615 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a37e664-b269-3805-a485-cafb2d816bb7 | -13.39037 | -47.89346 | 2025-07-09 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ea5bee3-4e3b-38ec-91a2-182d5bdef716 | -12.98246 | -44.87065 | 2025-07-09 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 793207c6-aa0f-3072-af7f-dc1b18996412 | -14.85731 | -45.12645 | 2025-07-09 04:46:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 009e5a76-4dbe-3440-8123-a45c65f61745 | -11.10731 | -48.87222 | 2025-07-09 04:46:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7929804f-a910-367e-97e3-627b7fe9d3bd | -10.57384 | -49.11847 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 2a68fc26-8f5b-3f83-b062-70cb681568ae | -15.56769 | -52.21004 | 2025-07-09 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 857370df-2054-3fb0-9879-de7a911f1e40 | -10.6273 | -51.58883 | 2025-07-09 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1bcf407-7e06-3dcf-922e-91390efe7284 | -9.62235 | -49.10191 | 2025-07-09 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 183f4d03-c79d-3eb2-9605-6128c7a60732 | -11.43316 | -45.09026 | 2025-07-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3657b737-1a6b-3711-a9e7-38b35fc00b9f | -12.97662 | -47.82342 | 2025-07-09 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f469805-47b3-3d05-8ae7-19ad830fe599 | -10.64964 | -44.48945 | 2025-07-09 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc7ed452-e6a6-3b77-827b-10b7a67c558e | -11.67406 | -43.78162 | 2025-07-09 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 264dbe3d-55ff-375b-86f0-5ff5740beee3 | -11.4746 | -47.92782 | 2025-07-09 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c7faf8e-0357-39c0-98e8-fab7c9d333f2 | -14.05232 | -46.26822 | 2025-07-09 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48176832-9bd7-3f28-8c10-70c0c31c247c | -13.0002 | -46.30391 | 2025-07-09 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de3db0ba-fd2f-3920-b564-78d98a1e53b6 | -10.34557 | -49.91387 | 2025-07-09 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 503dd252-aafc-34e1-9f6e-7820f0af249f | -8.71704 | -50.00753 | 2025-07-09 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96b02735-ed9a-3af8-828b-bff7fe773b04 | -10.312 | -51.71471 | 2025-07-09 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e6fd64e-128c-3194-8b14-446ddf034290 | -9.92418 | -59.90251 | 2025-07-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38c95387-8d14-3b45-baa6-88f94cfef5e1 | -10.57976 | -49.12782 | 2025-07-09 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 68a93323-c42c-35ea-8cfa-eb93c5f496a3 | -9.33888 | -58.84389 | 2025-07-09 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40482681-d6c2-3916-8d2f-5139e35bcd71 | -12.47511 | -46.90995 | 2025-07-09 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efef2173-256f-3cfe-9d37-5051b0a81e1e | -21.04406 | -45.27777 | 2025-07-09 04:49:00 | NOAA-20 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ede8382e-209b-3123-b6c2-9cda33c2c493 | -19.26465 | -55.15471 | 2025-07-09 04:49:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00fac32b-3989-3ad8-a64f-d8b9b82df0bd | -15.89013 | -58.55873 | 2025-07-09 04:49:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ed5f054b-394e-3a2d-a496-bf6c0e34e5d2 | -18.64567 | -55.73388 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d7cf8fd4-0fd3-33b6-94bb-5a6e65add4db | -19.34595 | -49.92642 | 2025-07-09 04:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4301982-bbb5-39d6-b934-24d35556c6e0 | -18.41101 | -51.97953 | 2025-07-09 04:49:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66e53f60-53a8-3366-89f0-22dd2eafb8e7 | -17.26563 | -49.00875 | 2025-07-09 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 667d007c-b2f3-399f-ab77-c4bbab47c930 | -20.86061 | -55.29359 | 2025-07-09 04:49:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9f657c9-fda5-3938-aed0-01dd5208f32b | -18.08916 | -54.28743 | 2025-07-09 04:49:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8875cabb-a41b-343e-98fb-1b08a5b46fae | -18.64631 | -55.73006 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d70484ea-6436-38fb-81ec-826a9b8fd1b6 | -18.41695 | -54.70355 | 2025-07-09 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d4069e0-af17-34f3-955d-d025528878f1 | -20.40289 | -48.61653 | 2025-07-09 04:49:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70205e7a-73da-3785-9653-5fd11ad9dde6 | -20.99488 | -51.79069 | 2025-07-09 04:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6eceb1a9-7a82-364a-9b69-100f208d1a16 | -19.75132 | -54.00056 | 2025-07-09 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6438f62d-7d24-319b-87a7-dc7cf3a699de | -18.40159 | -44.19525 | 2025-07-09 04:49:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ff37ace-f5b9-300c-9399-c5031671701d | -18.64694 | -55.72625 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1f55d1f5-06a6-36ee-ad49-56f74ffdac74 | -20.47712 | -53.67373 | 2025-07-09 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b0119f9-7591-3646-aca4-771ee7d499c0 | -19.09199 | -56.04699 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bd76d1ed-ad00-3c09-9ac1-0897b59e7e14 | -21.04178 | -56.00033 | 2025-07-09 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8b1d633-fe16-3887-a236-232ae56a4e19 | -18.08642 | -54.28323 | 2025-07-09 04:49:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df05e620-434b-30df-8e8c-480ad77ed6c4 | -21.19067 | -48.94201 | 2025-07-09 04:49:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d5ac7472-077f-3d05-9c2d-7f21b829217c | -20.69682 | -45.09044 | 2025-07-09 04:49:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 50405708-2487-3f12-b609-793f8ea5b086 | -18.64081 | -55.72118 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7a0fdf71-c853-3940-830d-e70f64560352 | -18.97152 | -54.37975 | 2025-07-09 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2519e129-fa65-3a73-bd12-ee1b4e76e7c7 | -18.65033 | -55.72687 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d4109b87-85ca-3c0d-b253-e2dff3efdb02 | -18.40741 | -44.19231 | 2025-07-09 04:49:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 421db569-0ce3-3fd8-ba39-adccb3f26f37 | -18.41422 | -51.97916 | 2025-07-09 04:49:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26c5f506-b372-3a13-81e2-028a343e83cb | -19.08793 | -56.05023 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c4f87e97-5376-3e0d-951c-72862a24e264 | -16.38318 | -54.57728 | 2025-07-09 04:49:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66eb3226-e602-337a-afda-b1504b9ba19b | -18.63953 | -55.72882 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7a911ca9-f290-3495-909f-0a1e3c980e2e | -19.08452 | -56.04959 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README23.md)
