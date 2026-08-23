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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9436fd71-9a7a-3312-9d15-43e5359c66c0 | -6.94671 | -59.06728 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9be8b75-dbb9-3be2-90a4-f584645ce66d | -8.52838 | -54.8237 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c73c9367-af73-3b18-b99b-dec2fcbba684 | -8.92816 | -60.72526 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b487cc80-d0ad-3458-87cc-3b11ee8a8768 | -9.21068 | -59.7958 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bd2e3ff-51e6-3cbc-8c76-8e43228e5981 | -6.79648 | -59.41838 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e5c5418-380e-38f1-b089-948e300167ff | -8.94466 | -67.34424 | 2026-08-23 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe09fc95-367a-3efa-baa1-5b1d01348f16 | -6.70077 | -58.73532 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 631f427f-68a7-3d2b-a75e-9de1b1ab1116 | -9.86215 | -60.11319 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fdad1ed-e13c-3994-8ba2-71ac3ca474bc | -8.40543 | -62.6953 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39c9cbcc-d79b-3eae-8a22-c703cbf02189 | -8.89697 | -60.54306 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fcf74f73-f7f9-3518-abd6-6307c4027054 | -6.70158 | -58.72943 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96ebd03a-de96-3411-8ab0-4c9454cb7743 | -6.76635 | -58.67249 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d26984f7-f978-3278-b670-7f73a682d204 | -9.12555 | -61.59969 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a78ccf6c-b9b2-3cbe-8709-a52378598a32 | -6.79574 | -59.42375 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edac3d45-ea39-3f44-b5ae-4b9d3076930f | -6.7058 | -58.73614 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98aedb6f-807b-3fe6-9c81-03d73cbc2111 | -6.75704 | -58.66505 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51a1d3b1-0c2f-3145-8677-05be70a52f69 | -9.40647 | -65.94032 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1f40629-0c15-305f-a859-8fd89227b1de | -9.12126 | -61.59906 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98ce3f9e-a152-3d7c-bb75-469bccc807cb | -6.70117 | -58.7324 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4cbc3df-23a7-3c43-96a6-ac59580d9c5b | -6.79501 | -59.42908 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b5140c8-dd55-3249-b5fa-07c3d61a54e7 | -6.75578 | -58.67397 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b1d972-2fe6-3705-9092-b8ad7dc8c049 | -6.65092 | -58.79953 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f73543b-011c-3afb-85a9-e410032d2fb5 | -6.70241 | -58.72339 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f56846a6-f466-3a3d-86f9-5a35ddb51b53 | -6.55612 | -58.53011 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdf2ef5e-474a-3d5c-ad00-867aa917e1a6 | -9.85805 | -60.10713 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ec265f4-ed77-3424-b7b1-233ef54a9c9d | -7.69895 | -72.80728 | 2026-08-23 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0628714-e41a-36b1-8fa7-ce0c49ce8035 | -6.79777 | -58.65873 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8eda94fd-6213-3306-97f4-7b702d142a20 | -6.54669 | -58.52303 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961a483b-0eea-3fa4-81b9-2eaf0d176f74 | -7.59603 | -60.93795 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b62ed63-ed82-3635-816b-5a90760dac10 | -7.49565 | -64.69263 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afd7ac36-ffe2-327c-85eb-5dd362adcc0d | -9.21495 | -59.76318 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12bb9273-76a3-35ff-9dae-8b56fb043931 | -7.63293 | -61.61883 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46110f1a-1df2-3aa7-baa3-f17018925e5e | -6.61019 | -58.38339 | 2026-08-23 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bb39aac-053c-39be-b058-656edcf825fc | -6.7562 | -58.67102 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f52a91fd-79a3-39b5-9a23-baf008d18f81 | -6.80319 | -59.44106 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac600ec7-4149-3125-a15b-3781e97d886a | -7.59868 | -61.22915 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ee8fd17-8514-34d5-af81-6bb7d526dcb8 | -7.4412 | -59.77445 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a13cf970-e451-3084-b2ef-193e8d191211 | -6.85582 | -59.41647 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2784ff6b-ac7e-3fa6-bd59-c71aab1da5ee | -9.1373 | -65.95643 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a242d71-a658-34ad-a9bc-cada58423b90 | -9.13051 | -65.95538 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1eccc7e7-3e0c-33f1-9e16-2e7200b0cd8d | -9.12612 | -61.59563 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d97973f9-4322-32a9-b9bd-d31fcec2ded4 | -8.54029 | -54.83729 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2407daaa-1aa3-3f4f-9555-a097fe44b462 | -8.70056 | -62.8735 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d46dd2e4-79a9-3471-8867-3e6974a49c3b | -9.10522 | -61.58828 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69d9556a-1336-3747-84c3-fd1639387c78 | -8.40221 | -62.68959 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2953b454-dbc4-3c4d-81b4-2a9eaf0620d0 | -6.76208 | -58.6932 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb8b8b15-4970-3582-affd-086d5e17a9ae | -6.79672 | -59.5935 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 047382a1-342c-3973-b117-1c18757dd515 | -8.67773 | -69.72047 | 2026-08-23 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e1e3b86-5357-39e6-9047-ed2d263966b0 | -8.52611 | -55.33763 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 100a84fe-c485-3c77-942f-fb9e63f53d56 | -6.97718 | -59.06611 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 088c3638-1af5-3608-b088-8e7d34d1f012 | -6.68486 | -58.7387 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8594615b-1a77-3228-b7ae-e5f6b6d4dbbb | -7.07086 | -59.97623 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| efabf08a-79e3-3077-9755-038b0f3bfa96 | -6.80957 | -58.64829 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e7a8d6d-466f-30ba-b742-ba156efe5f40 | -6.82539 | -59.66556 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0d350e4e-3ef7-305c-b29b-f40f81f2feb7 | -8.54379 | -54.83241 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae4b4807-d292-3719-a674-8e8c3eef5e64 | -9.20768 | -65.91017 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bed4b87-a5dc-30ff-8501-f2781b2a51b8 | -6.66386 | -58.74179 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e458a04-b615-385e-b681-a07a91e0fa91 | -8.92879 | -60.72066 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 705564ea-dc1c-3e5d-b1b9-ffedeb1ce628 | -6.96575 | -59.07575 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9de48296-279b-321f-aca4-3d0c47fbcff6 | -6.80371 | -58.98683 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b8172ed-5086-340b-8eb2-17ad17149333 | -6.68142 | -58.72622 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cd4c5d3-e590-3d21-9888-d6293714f47f | -9.17007 | -65.94646 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5152e53f-abdb-3744-9162-af51b3dbe735 | -6.94392 | -59.0778 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3654942-e74a-36d8-9b06-d74d45f6669d | -7.77546 | -61.06822 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a70c513-3e9c-367a-94e7-decd3b3a4a63 | -9.11074 | -60.33729 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6608d2db-a2c4-3fcb-ab8c-d88b1e62f924 | -9.56088 | -64.18836 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54c562d6-c1ce-3a67-b50f-819635476565 | -9.2355 | -60.38799 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ec8eb3a0-c4c1-3f49-84c0-51eec9bd6bb6 | -6.76567 | -58.66633 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d069c9ec-5a59-3cee-b013-499a9bcfc9b1 | -6.80193 | -62.90828 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed9a9756-bacc-3af3-a71c-74971d050227 | -6.79983 | -59.42981 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2c08d4d-1205-3b02-8031-e5a100e8a8aa | -10.55972 | -61.45853 | 2026-08-23 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c01aa2ab-da12-38e3-a7be-c1add95b4ba0 | -6.82611 | -59.66043 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9f6da3bc-ef38-3c1c-b3d3-2dfc44791b99 | -6.55142 | -58.52649 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 724c151f-91e7-32c2-a7ff-83fa7426b4e9 | -9.14859 | -65.95065 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ab051a9-96fd-3e7b-957f-af198a1a8cf8 | -8.53269 | -54.81298 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bd1cb45-b9e6-3a40-81de-fbcf7f0e215c | -6.55311 | -58.51439 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f02f96cd-9443-30ea-897a-e9c5fe214911 | -9.58995 | -60.50412 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adedb0b4-b4fc-3b89-aa38-a5c4714e5a56 | -6.82206 | -59.41132 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9999f9c1-121e-3e28-a90b-f4b86979325a | -6.95509 | -59.07987 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3b514e81-f88f-3661-8644-2671173cac59 | -9.65972 | -63.84306 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60aecc60-15a6-3d98-9d71-ef867d431c47 | -11.20591 | -55.04698 | 2026-08-23 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d64bb51a-5a01-3ab0-a55d-87ab7a0eaacf | -6.95813 | -59.05757 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8f33dde-247b-3732-8901-c9400e3706c0 | -7.48715 | -55.33279 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97a3bb11-490d-32a0-aa12-d7ad31dca283 | -9.17833 | -59.45546 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| edc91b63-4306-3193-a134-ceba0d08df96 | -6.67899 | -58.74405 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4fa2bf7b-ac5f-3f20-992a-333107919867 | -9.06166 | -60.43478 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9cd466e-186d-30a9-bbfd-504e81cd44b7 | -7.67877 | -61.1162 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a995d092-86d6-319e-a1cd-a5c67a6f6b5f | -7.6042 | -60.94363 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7169af2-b59a-3a77-9185-62df66b1e6e7 | -6.96727 | -59.06464 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ab877754-3657-30a8-8301-dec33984234f | -6.75789 | -58.65905 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cf54a0b-a78b-353b-a52c-1be633cc6ea8 | -6.94595 | -59.07288 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cdf612c2-3cb4-3f77-97da-4bd0cb3c452d | -6.79217 | -59.66088 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a04feb87-6ce9-3a4f-930c-518787d48693 | -9.21423 | -59.76871 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 014e9279-0813-3cff-ac42-deaa8ca01948 | -9.22154 | -60.77276 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b38dfe-22a0-30e1-ba7d-c5c1511e3032 | -9.16188 | -59.46479 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b19a313-14c5-300d-aedd-fb8e59a0db1f | -6.79722 | -59.41298 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2856fc42-3f37-392b-ba90-d308e0c43054 | -7.78532 | -61.43108 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d789619-4dff-3022-af29-be6ee227c46b | -6.67817 | -58.74999 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbda10a3-9625-31db-9ae9-9f94c51f556c | -6.77603 | -59.14826 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6d727ba-a8f3-3843-96fd-558e5b47c639 | -6.85164 | -58.97092 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README63.md)
