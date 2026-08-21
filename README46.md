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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa703de2-21cd-3e12-9ae5-fdc2c30dddc5 | -9.05762 | -60.43278 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e2302a2-38d6-3e11-be49-23fd73700bf2 | -8.52501 | -55.33315 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f37a16ab-b52e-33c6-a4a4-50ff8b9143ed | -7.45797 | -46.15309 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 57323fb7-9c1e-31d8-8396-10c6a4b622f6 | -7.02386 | -48.03912 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abe02846-2562-3a78-ab3e-161c273900a7 | -8.55229 | -54.78023 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f62a93-59ca-30b3-b64e-08d9bb81d5b3 | -8.45874 | -46.9533 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 796841c2-f9da-31af-b83b-f9f47e92b52f | -8.61578 | -54.73096 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 308ecc6d-6268-3c09-815f-4ea52fc5a8ee | -9.40369 | -60.43101 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e2800cd4-c719-326b-af6b-f936ec5b3a58 | -8.44946 | -46.96218 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef459848-fbe9-3d7d-87bb-db5a541999f9 | -6.23124 | -55.39763 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af275a7d-6d29-3c36-8e38-3c83f9f5344f | -8.5818 | -54.78075 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 812a31ec-ed70-3d46-a96e-3c46e2e60251 | -10.24689 | -54.36816 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6677cf05-16a8-38ba-9dbd-49876362a7a0 | -7.37814 | -45.81604 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4e541fb1-7faf-3a5d-b462-f6536596bb76 | -6.94141 | -52.78537 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1db07f02-0033-3390-84c3-ba6bac9a8da1 | -6.86058 | -59.44611 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8970303-a380-3eef-9a8e-02062a8f78c6 | -6.52087 | -45.90152 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54676ed8-fa12-3927-8440-b266d37150ad | -3.5086 | -53.20082 | 2026-08-21 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dbc8473-8eb4-3604-a034-3b4cc008ac52 | -8.10377 | -51.67093 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98a8d5db-a5e7-3673-9bed-012027c57f76 | -11.48696 | -45.08924 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4314a39-53ed-36fb-888c-25054222de32 | -11.5566 | -46.93835 | 2026-08-21 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d8f436c-e886-38cc-9d8c-920c98daee6c | -6.86262 | -59.43773 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 338ca954-b65a-3042-8175-20df3b7a8494 | -8.03629 | -51.7989 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7180d04a-5f81-32e8-af51-9d639027a928 | -7.00936 | -48.03705 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 83d6b1a7-4a8f-31de-b78e-acc2ac395417 | -5.7167 | -46.18656 | 2026-08-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80ff4697-648d-32cd-8ecb-b3d340c8cbe1 | -8.04904 | -61.71261 | 2026-08-21 04:46:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3769223-c3f3-3009-9323-501eec11b441 | -6.66566 | -52.8874 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f64e7b-b164-37d0-87c9-87251f0b9ea9 | -10.24625 | -54.37203 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 012950e1-6d16-31dc-a71a-bd66f8ad539a | -15.49665 | -53.90064 | 2026-08-21 04:49:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b50c7b87-25c4-35d9-b5ad-c7b6c2f11d9e | -12.75093 | -48.45993 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6ea582f1-c899-3371-9135-86838e8f3d24 | -11.17041 | -54.00774 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b012d252-171a-394c-8198-0b2871bfa41f | -14.44745 | -45.6189 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 385ccae6-4be6-33fb-8f59-460b2baefef6 | -13.93899 | -53.85367 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e47dbc37-613a-397c-b0e7-41a27b8d504f | -18.02788 | -44.61515 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc794ad7-2762-3bd5-bd0a-f3e1d536f1f4 | -12.00929 | -53.43462 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a32dc3cf-af3d-3ca8-a586-b828c304204d | -12.74478 | -48.44875 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fc3f75e-af6e-3209-a2d2-cefd3484e4db | -18.06057 | -44.41199 | 2026-08-21 04:49:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8a3241b-837a-3b8e-a396-cc2f632fa3e2 | -11.17539 | -54.02003 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8c2d986-f502-3208-bd0a-a0f3f0706040 | -11.19021 | -54.01485 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebcf9a7c-4f87-3a17-aa90-deee97bb60f7 | -14.57506 | -53.01501 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08d89a8b-30d7-3c1d-83e2-3874060369ba | -14.32064 | -51.90442 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01c90fa3-3ba9-376f-8ac4-43c8883126f8 | -17.97388 | -44.42684 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4bc1e5cb-042b-330d-ba1f-508670d11164 | -13.44802 | -51.84068 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa823237-7ed7-3dbc-8987-54ab3b43c65b | -12.75793 | -48.46522 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e0702166-1aff-3f43-8f15-fd8abbc9e3dc | -13.67793 | -48.76369 | 2026-08-21 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4141d0b3-2d25-3ae6-a490-e00267e10d05 | -15.72231 | -47.79325 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5f7e917-38de-31ee-8e59-709d662a336e | -12.00872 | -53.4382 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 316b220e-d8ae-3ba8-b1fc-3576112a0df6 | -16.76864 | -49.25005 | 2026-08-21 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 867c2fed-c5f3-3265-8d53-8426849311e2 | -14.45212 | -45.61955 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63c751b1-d378-3edd-9952-bbe21baeace0 | -12.26262 | -43.1643 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bfcc0a12-9aff-3092-8d4a-4b466bafc61b | -15.59988 | -46.57634 | 2026-08-21 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 914ccd7d-fc37-3170-8f01-e643e6ed57d9 | -14.00886 | -53.67324 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecb40215-7f97-31f8-bd6d-e131aad71cd0 | -11.18001 | -54.01316 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ebe5981-06d4-3437-8654-cc32fd939494 | -11.17757 | -54.02807 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b46250b3-7639-3c3d-b8ef-c2d05e9566d4 | -11.21984 | -54.00448 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44c66de6-bcea-347d-8eb8-dffafec2b6a2 | -11.16675 | -54.03011 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 040932d0-03f9-3526-a4a3-217b2c1de3f8 | -14.52981 | -53.0003 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fbb0fd9-0bdb-3168-a19a-822b965e2793 | -13.94117 | -53.86144 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9498ba3a-e2c7-3a4d-8db4-120ebc0d9675 | -13.93565 | -53.85312 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c42d4ad8-1221-34d7-b1a8-f52acdac6923 | -15.55865 | -50.27591 | 2026-08-21 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0465fd84-d481-3112-9831-99f144e02756 | -14.45294 | -53.18791 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd0e98bb-2d34-3799-89f7-8f8608762e0d | -11.68249 | -54.57372 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a46797e4-b1f0-31e4-9686-95ffc47a4e57 | -11.68594 | -54.57428 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 529c4da2-13ea-36aa-ab67-0f0ac4e26b19 | -12.50266 | -54.75558 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4e0a8b1d-77a6-3c46-ad09-7101dda6bf73 | -11.16919 | -54.01517 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4c6a38f6-3172-3fbc-9d7c-5f644cb3e31c | -11.20974 | -55.06453 | 2026-08-21 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51b30f97-4773-3322-a047-bba0603909d7 | -13.37592 | -54.37605 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1b152ad8-2141-3db1-bdcc-d659fdad25e8 | -14.57783 | -52.99725 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed4360f1-4ace-325c-a397-bda1315b066d | -13.40911 | -54.39264 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 129cd47e-5bec-3756-84cb-febf94cb1868 | -13.92897 | -53.85204 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c3525b6-4bd8-339c-8b55-ec11b711daa6 | -11.17417 | -54.02751 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec5071ad-d766-3107-b333-d023c11cc90a | -11.17818 | -54.02433 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4779306-b30a-3bd2-bc7f-456f308755a7 | -14.72566 | -47.14418 | 2026-08-21 04:49:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ae60e6f-3c0c-380a-8b81-b8f69edda4e3 | -12.22478 | -43.16237 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 78c14cac-471a-32f6-a22b-985474d7b403 | -11.23882 | -54.82619 | 2026-08-21 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 545f4c48-14d9-31eb-b97a-033911f8f0f5 | -13.394 | -54.37862 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8630cfc5-00bf-3205-928b-346f91fea680 | -12.51712 | -54.75399 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 950cab82-1342-3e09-aaee-86ef6cc024af | -14.03222 | -58.86788 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba9985c-2c97-3ead-9972-81d738a7a100 | -13.94727 | -53.86614 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 885b6bc4-7731-368b-99d7-d84b375091bf | -13.44633 | -51.82937 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26f96732-19a5-359a-95d7-b5a53fbc6dd4 | -15.55807 | -50.28004 | 2026-08-21 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ead8fa0c-5707-3836-9bd3-cbc7293b4678 | -11.2202 | -55.04554 | 2026-08-21 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3940d0ec-24e7-3c8f-8472-422987b02e84 | -12.8066 | -48.42019 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c8690892-6b2c-36d6-bc97-16247534730c | -12.75755 | -48.46667 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e27568f-f0a8-39eb-94ce-731f53e4ef52 | -12.26558 | -43.16711 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 81974709-b312-3692-854d-7d879234f20b | -13.44449 | -43.84268 | 2026-08-21 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e9c7c89-0318-371d-8bc1-040de6dd5003 | -12.85742 | -48.41811 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4125372a-1f03-3a65-81b0-200c6a8b7b45 | -13.38269 | -54.37718 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| a4f65a2a-c9be-341d-89eb-3c51105165af | -14.08444 | -58.86927 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 542992d5-b87b-372d-b30b-b9551bcb4719 | -11.99984 | -53.42939 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d674d3bd-a3c1-3c24-bd78-e18da948a9d7 | -12.26143 | -43.17382 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8b186e6d-8961-3210-ac14-d43a46db1e58 | -12.01141 | -53.43837 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64daa727-fd25-371b-a2cf-8b32cf3ee4a1 | -14.32009 | -51.90804 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3c2c821-5b79-30ae-93e5-3bcbdf344e4c | -12.86053 | -48.42357 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d29008dc-ec0a-3ede-b15c-4d05a4ae8938 | -11.19203 | -54.0037 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9dbe4c2-db5d-3f71-a1ea-ef11689065e1 | -14.22646 | -51.92244 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c41a376b-f93e-3857-98e9-690f54193ec8 | -11.16579 | -54.01461 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0b884a7a-150d-3b47-a080-ae4f88470a61 | -13.39616 | -54.38665 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| f54bb9d1-2c58-3b43-8402-cb65b33c068a | -14.33401 | -51.90657 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5f235d3-6d8a-3fe5-b258-056c585bdbd5 | -13.26328 | -51.627 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5de40ea9-ca1b-3a4e-984a-5ef32a8ce07a | -15.4436 | -41.38351 | 2026-08-21 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |


[Clique aqui para ver as próximas entradas](README47.md)
