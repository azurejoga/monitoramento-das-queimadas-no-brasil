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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f830813b-d332-3b69-840e-58ae1af0c2df | -7.1615 | -42.10509 | 2026-09-14 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 880f54cf-e8df-34a9-95aa-7198a85aafee | -9.33465 | -44.37263 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 87e678d8-3149-3a6e-a618-9f766464bb04 | -9.31708 | -45.63864 | 2026-09-14 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aeb2833f-691d-3918-9b0e-6351e4068c6f | -9.39664 | -50.19964 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fd69a29-9ebc-3514-8442-de75c7f126da | -9.49471 | -45.47699 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac048ec0-9458-3516-9783-3dc8f89444d4 | -9.45296 | -50.1286 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 545c6121-260c-3e2a-bbe8-d223c8f741df | -7.07364 | -43.52435 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c4521db-17f6-3b29-89c5-5c4c5a7c3647 | -7.0874 | -41.7998 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f89e888-6a5a-34a8-a753-86f6b2fa1238 | -5.84468 | -40.70706 | 2026-09-14 03:55:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65364e0e-37bb-3ac6-900d-fdfe3a594b3a | -8.57419 | -44.46395 | 2026-09-14 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea237d16-3ec4-3d81-9ae3-806fa6bf9204 | -9.43444 | -50.12951 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 35dbbbfd-a898-3768-bee9-6654c3db2b20 | -9.43525 | -50.12522 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2ebefe2e-ee54-3fdb-9b6e-9e3b1c7cd228 | -6.3392 | -44.10728 | 2026-09-14 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09d2a049-d41a-3274-b54a-38c817a64ac9 | -9.42425 | -50.1187 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cb49839a-5ccd-39ad-829f-49ea9d6d4e1d | -11.13595 | -47.71526 | 2026-09-14 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55741ddc-3736-3bd4-a168-2f0c6f8c3357 | -8.69972 | -46.81964 | 2026-09-14 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e2deade-df9e-320a-ac12-78b58a0982f7 | -6.69503 | -43.14202 | 2026-09-14 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fe7f466-d62d-3edb-aa77-810deac37c95 | -10.17671 | -48.06277 | 2026-09-14 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b3a6540-7779-3054-b6b2-ffb5d82934f4 | -7.11322 | -41.79988 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| ea248abd-4314-3ad6-9a7e-9be1c32233c1 | -10.54567 | -51.31493 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f176e49-6b00-331a-a626-6325f6d22bd0 | -10.42922 | -48.65027 | 2026-09-14 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f8655c1-5a0a-3c5c-b40a-dc47dc88c268 | -6.53405 | -44.08895 | 2026-09-14 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d829ec0d-7207-314a-9fba-c29a0da94f54 | -8.39683 | -42.21904 | 2026-09-14 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6b5a0824-2861-3da0-b405-14a1f49a8859 | -9.49545 | -45.47276 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 681fce5b-d744-3d45-982e-47c5cc152c63 | -8.50493 | -40.1961 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20c37787-88d8-3212-8e6e-6063352fbca6 | -10.5458 | -51.30352 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39a76771-a705-33c5-ab5e-1bbd315f7de3 | -11.19225 | -42.79543 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e4f78fbe-dd77-3cb9-bf92-8c8431be690d | -7.96552 | -43.98821 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b873861b-45da-3f8d-a232-24b14cca1c17 | -11.17677 | -46.38636 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91cdcdcb-8d9c-32a4-afdb-1803b93ed58d | -11.18281 | -46.37857 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91942901-e91f-3ed1-837c-ff1c8e9b58c2 | -3.38339 | -50.39385 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c161da1a-8c4d-383f-9cc8-2e23b598981d | -3.37896 | -50.39153 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f23f82f6-0c00-3805-ae8b-e134b257a936 | -9.4193 | -50.14485 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de33db77-ce26-3aaf-be31-c98508226937 | -9.55044 | -45.43892 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a826a00e-b648-3156-97d0-f94feaadad3a | -5.28763 | -45.26971 | 2026-09-14 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa9285dc-b527-3b68-aa47-64ec003a9dc0 | -8.9979 | -50.82362 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 9f2ef611-eccb-3ee5-a1c2-30b0b17259f1 | -9.33187 | -44.36466 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06180cf6-41ee-39a1-9e87-ec4f00a80da1 | -3.37799 | -50.39718 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c533672d-cbaf-3f67-80ff-90c1e2aa5aef | -3.75372 | -51.14845 | 2026-09-14 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 46692435-2478-39a3-add8-8750937141b5 | -7.99797 | -43.78572 | 2026-09-14 03:55:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6b047827-c49d-3969-9557-1741aab4c9f2 | -8.30216 | -39.52367 | 2026-09-14 03:55:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 826fc14a-f2b7-3b2e-8800-cfce6c57055d | -10.31493 | -45.28898 | 2026-09-14 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0430c26d-e60a-3f35-8c3f-d040949f63d2 | -9.50622 | -45.48802 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca26db0-cd94-3e42-a8e5-126e1e9de43b | -6.25078 | -41.95977 | 2026-09-14 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cb091035-6fa9-30e4-b211-e2125e9158a5 | -9.53316 | -45.43571 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 519d0746-85c8-33fe-80a2-7969fd9d7553 | -7.10167 | -42.10415 | 2026-09-14 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27ea3984-8437-3aa3-9826-d707caa2c083 | -7.19926 | -45.92274 | 2026-09-14 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f39119b-96bd-370c-ab45-7c430253362e | -3.38836 | -50.75803 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b68376e2-5acd-3925-ab26-f467f6157eb8 | -9.44625 | -50.13177 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 87eb393d-43ac-30d1-94e4-e910e85381d6 | -5.63605 | -40.8521 | 2026-09-14 03:55:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4933ab84-4494-3a7e-aa32-51252bb76fc2 | -7.11748 | -41.79631 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8aa45c5a-b342-3896-88aa-bd87d1101417 | -7.11882 | -41.788 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5fea2770-4f71-38b0-8dc6-c850d3b90e7c | -9.71127 | -50.84181 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 143e3907-47c4-3c78-bb1a-9630811d9b2d | -6.53179 | -44.09182 | 2026-09-14 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce57cc86-4077-3d82-a907-6574d7c9af8b | -9.39748 | -50.19523 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d8b866f-aac7-3cb6-a805-c87884a0bbe5 | -7.10646 | -41.77318 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3adaad5c-eee4-3826-9ce4-aae19fdbbe94 | -9.4478 | -47.87217 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54ce43ad-e535-3a26-af0c-85322d84f8aa | -7.10244 | -41.79808 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 760205f1-6513-3daf-8417-d896cf1bd59d | -7.19609 | -43.68698 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed399a6b-7f08-3a77-8d50-886c0ba467f2 | -7.23788 | -39.175 | 2026-09-14 03:55:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c540ac14-d448-33f1-890b-e214c8977bad | -7.97017 | -43.98528 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aa6887df-07db-366c-b62e-3f3ea326e1ba | -10.10382 | -48.85994 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d8e896c-d56b-39d2-b797-1441b19a7073 | -11.42493 | -45.13618 | 2026-09-14 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc208a3b-b6c0-34d5-bbb8-0f85a334eb89 | -10.95075 | -39.26916 | 2026-09-14 03:55:00 | NOAA-21 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea0e860f-bee9-3e76-ad03-8b9d5bd4be98 | -11.6048 | -46.99684 | 2026-09-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 467dd585-1b77-3cb2-bfcf-74ac01d7b0ea | -6.20654 | -45.32436 | 2026-09-14 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 42b4bf9c-d0de-3877-aa9d-de30a20d24e7 | -7.5599 | -41.84288 | 2026-09-14 03:55:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50138eaa-8bdb-3b95-8be8-333a74261696 | -6.75538 | -39.81722 | 2026-09-14 03:55:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a9a15c8e-21d8-3971-a653-49959b8c5380 | -10.17555 | -48.06895 | 2026-09-14 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69928416-8df1-3c58-b68e-efc98099000a | -6.91173 | -46.14074 | 2026-09-14 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4aea8aee-13fe-3ab9-9909-83fec468bc55 | -7.55341 | -41.83746 | 2026-09-14 03:55:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fed65721-6482-3306-94d3-c5b5ac818993 | -7.10176 | -41.80225 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f6130496-8729-354f-983d-85e9462b1d8a | -9.44663 | -47.87843 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c06d2204-469d-3f0b-ae88-dfa7b157c0a5 | -7.11389 | -41.7957 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 820173ea-2439-349f-9f86-bf22589b73aa | -10.10014 | -43.95561 | 2026-09-14 03:55:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cff82e0-5c59-30a8-a9f2-262c12568670 | -5.81972 | -42.7348 | 2026-09-14 03:55:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62d4785c-2a7e-3bc9-8e58-fdde0a8edd7c | -11.23176 | -46.42745 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a02aa80f-0077-35d0-b9b3-be5a5cc43f98 | -10.10781 | -48.86848 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf5c0ca7-37a8-306a-ba53-08d62497c2ff | -5.85098 | -52.0962 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5348ff8d-3372-3824-a8e4-619e158e5af2 | -10.11054 | -48.85371 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5c92bd07-4b3a-3a79-8bed-613e5be8a79b | -7.55912 | -41.83803 | 2026-09-14 03:55:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 21f4cfff-c569-333f-b96a-7387bf1471d9 | -8.01334 | -39.47744 | 2026-09-14 03:55:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6020d2f8-8d26-3b1b-b904-2db769e3e8d1 | -11.37514 | -43.95545 | 2026-09-14 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27103f48-6d66-3f10-8c8d-b25cb3f1c345 | -5.76026 | -44.0585 | 2026-09-14 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4f9b6cf-1f7d-38d6-bca1-c54577b41c29 | -9.4026 | -50.20061 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7d7b31ba-9752-3d3b-82bc-204521a4d11e | -10.95129 | -39.26566 | 2026-09-14 03:55:00 | NOAA-21 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9d5ca316-03dd-3993-9e92-45e560e806c4 | -11.23244 | -43.44959 | 2026-09-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b11730e7-66e7-3ba2-a3b0-da7acc9fd132 | -6.42217 | -41.5575 | 2026-09-14 03:55:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7ea40d8-6e9e-3d83-85e8-9c67f07917fd | -11.18295 | -42.80686 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6acf72a5-c176-307c-b407-48f14ab69e8c | -9.0005 | -50.81926 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a388bf57-1461-34cb-b771-685b4bed5b2c | -11.04041 | -38.43964 | 2026-09-14 03:55:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 57b3b0e1-0ff9-314f-95ec-3da894dbfd0b | -6.17337 | -43.34922 | 2026-09-14 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 537666df-74e3-31e7-afac-6834310d5af5 | -9.39572 | -50.17217 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17dd81a1-022c-3e0f-9c63-0103d073f9b6 | -7.133 | -42.09598 | 2026-09-14 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb5b2a5b-e66e-3db5-8873-fb3bada76c7b | -3.38435 | -50.3884 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b88b0468-1df4-32c7-9cb7-a370c320652b | -6.65734 | -43.65797 | 2026-09-14 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 79549214-6515-368a-b221-f26eb71cd9f5 | -6.33478 | -43.36669 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ef4d7010-b8f3-3049-8b01-fa25fccc8457 | -7.02128 | -44.64674 | 2026-09-14 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9492d47-99ab-3e5f-bb4e-1340efd90960 | -11.21676 | -46.42181 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b05af97d-d69a-311e-9c52-66e64c67e3d9 | -7.47775 | -42.1221 | 2026-09-14 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README14.md)
