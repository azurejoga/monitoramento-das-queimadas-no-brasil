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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8ed0b14-06c5-317c-8911-256a1b2fdf14 | -3.32513 | -44.56439 | 2025-11-16 04:55:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e6c0f6-1bf2-3dd2-a080-57c477718a38 | -3.58327 | -41.66463 | 2025-11-16 04:55:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 76fcba7d-367f-3894-81fb-fcb8acc31a05 | -5.06012 | -44.70081 | 2025-11-16 04:55:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c35a497-62bf-36bf-8b5e-a8e96e141b45 | -3.37753 | -50.13299 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac1f127c-70ff-3f72-9149-fd5b91f6e605 | -2.88353 | -51.43181 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0d8f9bd-a23f-3f10-8336-ef834f3ea90d | -1.82561 | -53.76537 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff997b35-34c4-3c09-ab3e-7aa1d3625b98 | -1.993 | -46.54964 | 2025-11-16 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab8f5019-456d-3924-b2ef-438d8f3aefd0 | -4.40895 | -43.40204 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2712e6d2-d07f-3b3f-9ffc-db6bce404b19 | -4.2319 | -44.64273 | 2025-11-16 04:55:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 596fccec-d2ce-38e6-88bc-be7be086a74d | -5.71546 | -41.40137 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1bbb6ce9-79d7-3e03-859d-4cb8291e3ee7 | -3.38372 | -50.17178 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e40bfdc7-474f-37f5-8e30-5d78efd48981 | -3.3858 | -50.13332 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29658795-6a73-328b-a6ca-172835c5a501 | -2.96659 | -53.21617 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c57f127-e749-31fa-b159-70a7e8424394 | -3.4291 | -50.16576 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c93b01b-a2c3-3597-b152-27313973b693 | -2.14293 | -45.34489 | 2025-11-16 04:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29570d87-c18d-348a-9e06-56e845059046 | -2.96276 | -53.21909 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7238360-aa68-3635-bcc1-4fdfef12e95c | -2.13572 | -56.68431 | 2025-11-16 04:55:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5ff5a9c3-d37b-3611-9331-572a02c58588 | -3.24684 | -51.3502 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10360c0c-e7d9-3ff4-ad5f-46e3a38c1980 | -4.08668 | -48.9068 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86d05adb-06d4-3c21-801b-ed4f57682364 | -4.8391 | -47.54366 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b5dfa22-3edf-36b9-9df9-de51cf996e36 | -2.58433 | -51.87099 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d130e9f8-21e7-35f6-8bcd-90aba6558828 | -3.28627 | -53.82574 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab64d952-8238-3e65-8534-4893652b13b9 | -3.2087 | -51.03157 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9da8db0d-7dc7-3dc7-b17b-6d1ef34012db | -2.8943 | -53.2893 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ef5bbb04-e61f-3858-a202-e6c3d0b85810 | -3.81812 | -48.6585 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de8f94bd-7b7f-3ebc-b976-f2f7d566f908 | -3.45384 | -50.80665 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5483165a-f122-3719-9d69-a2896d6e8cbd | -3.99715 | -44.26766 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eb1a5af-1c91-3349-bac2-dcb9e307a8e0 | -2.26105 | -51.8723 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b84e590-9539-3bd6-9c90-099e1a223716 | -3.06161 | -44.74662 | 2025-11-16 04:55:00 | NOAA-21 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2add1bb-1ad5-3872-bd11-548a7cf896f5 | -3.75483 | -50.94627 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 037e4287-8243-3ce1-8abd-af7752064cc9 | -5.47372 | -40.96972 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 623530b3-8e28-34cc-b350-4f0ff56aba3b | -4.6584 | -46.74372 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2783f1ff-af46-368e-a416-beff5e514e35 | -5.69703 | -45.98774 | 2025-11-16 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb9602d6-c801-3ab4-8ae4-133e510d5cde | -2.39782 | -52.00174 | 2025-11-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb26fbe2-3744-3b42-8c36-0a3cd356a282 | -4.70037 | -46.31533 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c37187ff-6623-37d7-8998-89f7e8aa41c2 | -2.46953 | -48.86546 | 2025-11-16 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7968bb3-1087-35f1-9b9d-bf243cb60187 | -2.13523 | -56.6827 | 2025-11-16 04:55:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 44ece475-372c-31ef-a82c-7a76a3f20a07 | -3.31954 | -52.08587 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57aff9f2-e908-3d82-a1c3-6e0851c622ad | -3.33319 | -50.27549 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f4a9d666-03af-3022-8b01-688add3c3f34 | -2.88878 | -53.28141 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c45be16-7f42-3c15-a5f4-e710ed20bd62 | -3.3121 | -53.18246 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a15de60-48f5-3b8e-b4e7-bc24e314535b | -3.42151 | -46.15213 | 2025-11-16 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 666bc143-87a9-378c-904f-3945753608fd | -2.58758 | -51.82767 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4d45a4b-03c4-3d60-864c-8a75c87ed383 | -5.41445 | -43.25761 | 2025-11-16 04:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a3cb2c1-c48d-3a29-b817-772977419287 | -2.47826 | -50.25108 | 2025-11-16 04:55:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86c4e820-f291-3f53-b9cc-ffb3c89a3721 | -2.88807 | -51.42499 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9919853-221a-3193-977f-6df4fdb1335d | -3.45623 | -51.02161 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc73eac3-9d9c-3b43-b50b-dbf81b992805 | -3.58351 | -52.09734 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbe66cd3-6f4c-3dcb-90ce-c63ad2c5f4d0 | -2.25067 | -46.05664 | 2025-11-16 04:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bd8f8a4-9c3c-387e-8d6a-6591536b311e | -2.79594 | -54.86376 | 2025-11-16 04:55:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94a9693d-46ef-3e72-b717-f9cb378eb433 | -5.21906 | -46.91867 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6da9cbc7-6bcc-3731-bb51-6ada24ff6148 | -3.42729 | -52.79475 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f522992-f9b1-38ab-a764-24dc2105d26a | -3.28405 | -53.81835 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26ac9cc4-2510-3577-a93a-84a7352527cd | -2.17704 | -52.08689 | 2025-11-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72848cb7-a4d0-3b9f-9b37-74224a5c9fb4 | -2.80173 | -52.96489 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44e96f5c-e2db-345c-9dd7-d37d81ad48bc | -5.48675 | -46.91647 | 2025-11-16 04:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1161a365-5685-37c3-9574-1666b69c5876 | -2.95414 | -48.58717 | 2025-11-16 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 53948e4d-4254-3a00-bca1-e7b7729719e1 | -4.01782 | -48.80713 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4dd9fe6-b034-3fc6-a274-fdb3da4bfb0d | -2.94363 | -48.73928 | 2025-11-16 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 706d71df-08c7-33fb-81f2-cb78ff96810c | -4.30955 | -50.87386 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8f60e70-1299-3558-a279-0aee6236b31f | -1.91387 | -54.59409 | 2025-11-16 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00134981-97e5-37dc-ba55-5bb09f5b6c4f | -4.65909 | -46.73895 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04e88835-5c6c-3306-896a-ff7a29a7625a | -4.2488 | -50.04788 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce9c9904-6dfa-3dc4-9834-db195af09de3 | -4.00254 | -44.26843 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6de35e70-4b21-3daf-9fbd-55c202ad0b0b | -4.67814 | -46.73702 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f28811b5-ad99-396b-857a-60706632354f | -2.8205 | -48.3306 | 2025-11-16 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 368f7a7a-6ba7-322b-a9f4-6e6289b88299 | 0.0483 | -51.19236 | 2025-11-16 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e97bf811-56b4-336c-afde-8d22df51b28a | -2.58877 | -46.93208 | 2025-11-16 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d856ce71-443e-3d80-9e5b-12f950f5a6ce | -1.22064 | -53.36975 | 2025-11-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4167e65-c766-319c-8866-ea49203cd7e7 | -3.13255 | -50.28581 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d1e1889-8628-39c0-a31a-39faf90d9eb8 | -3.60136 | -52.04897 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 697bdde8-1417-390f-a399-45fe78023add | -4.83923 | -47.5504 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a55e488-85b8-35b8-b70b-740730b50d4a | -4.25764 | -55.72022 | 2025-11-16 04:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42e4dac7-1197-3d0f-9362-37ace4f01d42 | -2.89377 | -53.29272 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ad71faf-673f-3325-b0a4-faef9b349f7a | -1.83912 | -53.81072 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e82e0cd7-6846-3079-9648-7550dc673878 | -3.22234 | -43.35107 | 2025-11-16 04:55:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c6e5237-55ea-33f7-aa9d-8a307f73712e | -3.81825 | -49.11375 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 985870a4-6df9-389b-8875-afc341b424f9 | -1.62486 | -52.17969 | 2025-11-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dda70d0-e994-300b-a557-4ce318eff370 | -4.89123 | -45.01765 | 2025-11-16 04:55:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b9b52bd-9564-38b2-a05d-e4570efe3359 | -3.30671 | -53.84654 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 945c3896-c22d-3122-ac90-4428315dc620 | -4.39812 | -49.78331 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f31a2389-4698-3425-971e-8f74f1bbf090 | -2.58813 | -46.93638 | 2025-11-16 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b31120-c489-3c51-93cc-cfb732644e87 | -3.39756 | -50.17821 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b6d936be-c5f8-3b0b-9e62-761ea5694227 | -2.42738 | -45.71028 | 2025-11-16 04:55:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6d26e88-7aa7-38dd-84dc-b89ea77b05e3 | -3.86028 | -52.08485 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e739bb89-bb40-3d3e-97ac-ff765e3bd553 | -4.64373 | -47.94981 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f6e1ce4-e3fb-3870-9a1f-826b2998ec61 | -3.11436 | -51.02983 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d7286b0-6f2e-333f-abc0-ec5858acee85 | -2.83717 | -53.00207 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6417bf8-1532-3ddf-97b6-d6354bc8440c | -2.95443 | -48.59007 | 2025-11-16 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 413dfd9b-0449-3fcb-8467-0dc35c5ff588 | -4.15771 | -50.22731 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3f8cd3fa-d6ac-366d-8232-b956c9f2fece | -4.69434 | -46.31352 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ba34f3f-21d5-3039-9517-c9f5ef8f2521 | -2.97156 | -51.04376 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3411af17-086d-3917-806c-9e3f395f2e82 | -6.08719 | -41.60293 | 2025-11-16 04:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a7c97b0a-c392-30cd-9f69-92b2ff3cd357 | -2.91765 | -45.2343 | 2025-11-16 04:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7759ca29-1e0a-3d87-afe9-377750c10dbb | -1.62541 | -52.17621 | 2025-11-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b35e5fd3-a658-359a-97d9-88f2b2bd2163 | -3.16373 | -50.16624 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5825783-2ee7-3f65-a0f0-dae06d0f77e2 | -2.89484 | -53.28587 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bfe39d91-5afd-3018-9425-7d5103eb9da7 | 0.54573 | -50.75037 | 2025-11-16 04:55:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5552ab49-9f4a-3e58-aa53-88c390e0ec89 | -1.196 | -53.72379 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa13b200-3d63-3210-ab6f-b81a374ffba7 | -0.21954 | -50.41644 | 2025-11-16 04:55:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README51.md)
