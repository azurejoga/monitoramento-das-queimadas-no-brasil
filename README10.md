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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f686fa4-6ebd-3479-b9c3-19512e82a7df | -6.72666 | -44.36857 | 2026-06-06 05:10:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2219be9e-b4ea-3868-b3a2-a529f7b153f7 | -6.55296 | -55.03765 | 2026-06-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6421ce98-9880-3bbf-9644-f3b3d50b4e9e | -6.43726 | -44.58938 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9e8c1134-0360-396d-b347-213c6ef4f615 | -6.43872 | -44.57845 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 144ac9fe-6494-3566-abc6-be9955b29349 | -6.12033 | -48.56369 | 2026-06-06 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5571824-2447-316e-89f6-ef4297fd54c2 | -6.11026 | -45.8525 | 2026-06-06 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d77910f2-9ff3-3ac8-a877-892f362050f5 | -6.44776 | -44.56181 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9834eab9-d7b7-3f32-893b-a2facaf2ae4a | -6.45087 | -44.56716 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4b684f1-3c8d-398f-90ec-19fb1fdfb117 | -11.05787 | -56.92437 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d6edc00-f598-395b-8b72-4b34e64f46a1 | -12.79716 | -54.86845 | 2026-06-06 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b2bbae7-1576-3661-8ebd-f2591922a038 | -11.61951 | -55.1834 | 2026-06-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51c7aa7f-1f06-3405-91e4-036b518eb428 | -12.80089 | -54.86902 | 2026-06-06 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2f9f181-a90b-3d3f-9b03-c3f6350975a5 | -11.07896 | -48.25851 | 2026-06-06 05:12:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e790692a-2770-3fd9-9116-8e2a1fbd2e25 | -11.27037 | -53.96538 | 2026-06-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5a0253e-a063-34f8-9fc7-38cf9763835c | -9.08688 | -50.6096 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4e7b98da-36af-3fc9-86fc-df6217b282bb | -14.23295 | -45.80407 | 2026-06-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32ee3c89-d6ac-3148-842b-06d90e4c9770 | -10.03542 | -59.34013 | 2026-06-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1578d4d7-4454-353b-8d46-50a3aeeebcee | -10.85589 | -53.75101 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bfa068f-513d-3fb3-b9f7-97f0d45420ea | -10.86966 | -53.73767 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d70a00ee-aeeb-36f3-a053-8323ab109f97 | -10.0315 | -59.34318 | 2026-06-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8505f6b8-691a-3bf7-8ea4-c53a942cf747 | -10.18636 | -52.65237 | 2026-06-06 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ce976fa-20bc-34e6-9bab-ba6483c36cd0 | -10.84882 | -53.74481 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99107bb0-ea54-32fd-ba7d-6d6959293a05 | -12.06712 | -48.42345 | 2026-06-06 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0e334c2-d9c5-3135-8499-2b9dddcd5853 | -12.51231 | -46.30069 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baa8449b-ed7d-388f-9f3e-79b43b1ea017 | -12.06692 | -48.07405 | 2026-06-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9d7a95a-c330-3864-89fc-1b0cd0854d28 | -8.47277 | -47.00122 | 2026-06-06 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a92f41b4-341a-3722-934d-963f930ede5c | -11.0357 | -44.32225 | 2026-06-06 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f002ae50-f3e5-3658-835f-5929b905afa0 | -9.17078 | -58.0684 | 2026-06-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38f4cb02-231e-3729-b3e2-cf24933cc024 | -12.06644 | -48.07821 | 2026-06-06 05:12:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce318c0e-ba8d-3a8d-a147-fe3dfad92d2d | -11.26969 | -53.97021 | 2026-06-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23211873-4b32-395b-867e-863827438dbb | -12.50112 | -46.28345 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a0a302ba-710e-3b4d-a9b6-a18768e0102b | -12.50045 | -46.29071 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8095f66c-b1da-369a-933f-34712fbda8e1 | -12.28891 | -57.38842 | 2026-06-06 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0003612-1648-3d5e-bb91-e9af12333893 | -10.77567 | -54.09943 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7665fcdf-c14b-3180-8257-377cbdbcd9ea | -12.10109 | -52.00418 | 2026-06-06 05:12:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 566c217f-ad3c-3bb5-89b6-3d0f0d6553fb | -11.55433 | -52.79022 | 2026-06-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16a41a38-e7de-3d7b-88b3-518cea2626cb | -9.92634 | -48.00476 | 2026-06-06 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f34c3af7-84f1-3e26-b85a-ac0806fa572c | -11.73257 | -54.80779 | 2026-06-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60ba46c0-8ae8-380b-8afd-3c1cc47c5ddb | -9.16748 | -58.06789 | 2026-06-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acc4a69b-6246-3e9f-b1fd-4fdcc07d8c6d | -12.07232 | -48.42801 | 2026-06-06 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 703a12f6-7eaa-3b99-ad44-3e01c1536350 | -12.06576 | -45.98833 | 2026-06-06 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 397b7e2c-ba37-35e3-94bf-d2fdb56fcc61 | -10.80967 | -56.59136 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5f8f8047-69ed-356a-a364-cba89dd31418 | -10.77187 | -54.09886 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bc51f9a-9239-3fe4-9445-f2918a929adf | -12.50394 | -54.73563 | 2026-06-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2441cbbb-ead6-3fdc-b6c7-b3293fe1af7c | -9.37328 | -50.5411 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8ec1e39-5df4-3a4f-98ac-4bd2d4e428b5 | -9.08341 | -50.61313 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79450496-8d31-326a-a1a7-68e29381ab47 | -12.0664 | -45.9826 | 2026-06-06 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec4a183c-8da9-3ac6-9f5b-6a7efbb5a0e0 | -12.73615 | -54.20211 | 2026-06-06 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5243d4b7-7f3b-3c73-88ca-1eb48500e2b8 | -8.93077 | -45.67997 | 2026-06-06 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acff28b8-7acd-3956-bea5-2959645fc344 | -9.07546 | -50.60188 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f9ecc737-7746-387a-8482-eeb993884110 | -10.86577 | -53.7371 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93731d72-ded1-3e23-9d14-9642e93fce9c | -11.00875 | -54.31017 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b789cf16-8b70-3d8f-a8ff-4255ebf13e50 | -11.46831 | -47.9876 | 2026-06-06 05:12:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6f118c9b-4ad0-355d-a0f8-e2081eb25c82 | -10.84813 | -53.74981 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8483ee3a-0f7f-335e-bfce-1c0682baeaa9 | -11.05396 | -56.92747 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7f4da82-3eea-33a3-becc-355121691e22 | -12.07186 | -48.43186 | 2026-06-06 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ac2c5d0-5329-34f1-bd3a-72efeb32c0b3 | -10.85411 | -53.73539 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7610351a-4d2a-373f-a25d-4a84c4cb7ae4 | -12.73684 | -54.19717 | 2026-06-06 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 552237d2-e347-300c-801c-0335993803f7 | -11.88033 | -55.53025 | 2026-06-06 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b79bc1d1-476a-3d35-b3f1-939ad8811fd7 | -11.01251 | -54.31073 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91cb0bb3-3bbe-31c0-92db-991d9e47b82f | -12.5117 | -46.30598 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37bc96cb-064e-379f-94ce-851a50937d5c | -12.09666 | -52.00354 | 2026-06-06 05:12:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5971d4cd-fc20-3882-b97f-bad00b03e139 | -12.1005 | -52.00855 | 2026-06-06 05:12:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 332debef-c1fd-3933-a073-aa48d7ae744f | -11.03988 | -44.32125 | 2026-06-06 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6ddf798-7441-35a7-ac84-358567aa7477 | -12.50803 | -46.28142 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 912e0053-da82-3ae1-8437-3a39c98b7a0a | -9.08878 | -50.60883 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fee8d91-782b-30bd-837e-2b8879136f8d | -11.00432 | -54.31421 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d62aad7-2e74-37f1-8d35-f8ee2c135ddd | -9.92685 | -48.00079 | 2026-06-06 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ddf5bcd-74f5-39f1-8d46-e5f80b4e8a24 | -10.71951 | -56.04861 | 2026-06-06 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb8d22dd-4440-3075-a4d9-2fe135206fc3 | -7.50701 | -55.00702 | 2026-06-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce9fc18-925c-3c6d-b127-31e8d7f88c6f | -10.80911 | -56.59506 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca1b8291-0179-32a8-98da-c01d46474699 | -12.0664 | -48.07264 | 2026-06-06 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c11133ed-0f13-3965-ae3e-9c05db524e07 | -11.57419 | -54.58142 | 2026-06-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 738c63b0-7549-371e-9c59-fc838749c8dc | -12.50638 | -46.29679 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c46d035c-0eca-33f0-b03d-89bd56ede956 | -10.858 | -53.73596 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cb34d8-b993-3dce-b7de-e8d6e6f099b5 | -12.51344 | -46.29232 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06431f43-11e6-3c75-a5cc-3e00d044416e | -9.09156 | -50.61026 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 38364b1d-e4cd-3adf-a588-f24956003b51 | -11.05451 | -56.92384 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2f7dd49-e35d-3bd9-9cc3-8a577ba8e771 | -12.50583 | -46.29984 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f17eb40-df1f-365d-901f-15887d4b52d1 | -12.50154 | -46.28054 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7be0b939-58c0-3781-ab8f-0373a754c13b | -13.40388 | -46.60529 | 2026-06-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37511474-9a3d-37fb-94c6-dc9477011759 | -12.51353 | -46.29005 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74bb8904-d40d-3f77-af73-3d660bbb827e | -10.82293 | -56.60468 | 2026-06-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d0bb6dc-dfad-3e79-a0ad-4d0bd78611e7 | -12.51229 | -46.30296 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74846224-dd3b-303c-9db7-9b29aa6f0db8 | -12.09724 | -51.99916 | 2026-06-06 05:12:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b49be51f-b881-3d79-882b-2b7873a32e97 | -12.50054 | -46.28852 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0a3cb8bf-4cac-3dad-b534-9648953cbb97 | -12.49933 | -46.29916 | 2026-06-06 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fc6a3780-3ef5-34b9-bf14-ed6cb1c3e785 | -9.08807 | -50.61385 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5afd3651-efcf-3b86-a69b-e0372cb5e912 | -10.14487 | -48.08183 | 2026-06-06 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47183e74-61e2-349d-bd27-80c8d6a91a46 | -10.51489 | -51.9431 | 2026-06-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 605d6929-a165-3fb8-8ae1-2fbd9f7d2c92 | -10.19049 | -52.65294 | 2026-06-06 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f48b04f-5ecf-39bd-aaf2-e2f1c1a46585 | -10.03485 | -59.34372 | 2026-06-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e037a31-027f-33b5-b374-20e60703d046 | -9.07352 | -50.60258 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be4118bb-25d3-3d6d-8cbb-a2e430d41535 | -8.87266 | -50.19532 | 2026-06-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b979a1c2-bebd-3152-9d27-9d647be326ab | -14.2268 | -45.79689 | 2026-06-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4a13f80d-222b-381c-a6d8-930e7564a4e3 | -12.0659 | -48.07679 | 2026-06-06 05:12:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad434db0-e26a-3c12-a41c-cd563385936e | -10.90588 | -54.13575 | 2026-06-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b81d18db-536a-3cb7-8b9b-141c82317724 | -8.87337 | -50.19004 | 2026-06-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 240d5449-e4a1-3121-8582-988a84dcbcd3 | -12.50238 | -54.73796 | 2026-06-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76e7687d-a576-3094-aa2e-8476a379fe3d | -9.08622 | -50.61461 | 2026-06-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README11.md)
