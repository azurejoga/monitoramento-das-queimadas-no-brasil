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
| 38cb2135-dd20-3146-bd8f-3a9a22adfced | -9.94261 | -60.49413 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e62d68f-944c-3575-b93d-3a7466ecf1cf | -11.17815 | -51.4434 | 2025-08-07 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c544a5b-d2a0-39f0-8d98-f6b92279c522 | -14.92414 | -55.97979 | 2025-08-07 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ea4bc47-f146-3846-b988-d992f93b54c6 | -10.63873 | -55.3163 | 2025-08-07 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 52aaa07f-fd7e-3051-a05e-92f56dc4ecaa | -12.72076 | -46.3827 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c8d7fd1-f06e-3567-9a5b-79e57545cd78 | -12.33047 | -46.05945 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5c08c02-55e1-3d09-b45c-fce6ff0b216c | -12.34353 | -46.06106 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 723b126c-bd04-3735-b19e-b8418fcd0b16 | -14.35152 | -51.09333 | 2025-08-07 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 076cbc16-8a45-3a77-a4ac-acdd01db0c7b | -12.34846 | -46.06174 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41850be1-fc27-3685-b141-b384d0751ed9 | -11.89508 | -44.97246 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faa91675-78e7-3148-865a-b182982b4a1b | -9.70422 | -61.29789 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8b8ceaae-a6bf-3114-8820-4aefbc8d255a | -10.29717 | -56.45765 | 2025-08-07 04:53:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96849a70-bd16-3af0-ab3b-8cd8618a8442 | -12.71377 | -46.38786 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8aa3e73-7305-3d2a-b8c5-290348fef47a | -12.33295 | -46.06534 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 726631bf-3b6d-38ba-a185-69ea5024aec0 | -13.00694 | -44.87886 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1edd4e92-b8b6-3591-9423-12972e71b6e5 | -11.81454 | -44.25991 | 2025-08-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd7b3ae5-4324-36d7-8710-04d2e37b595e | -12.63613 | -48.11218 | 2025-08-07 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3eba923e-39c1-3f85-bf01-66cf1f981ce8 | -9.94306 | -60.46551 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ff6a206-56b8-3201-91b2-a9ba165c20df | -12.3354 | -46.06016 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29485444-716a-393b-a5e7-e951596d307c | -14.35885 | -51.09444 | 2025-08-07 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a6ad214-1d52-382a-a43f-d539a6ed8a6e | -10.83532 | -54.01561 | 2025-08-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f519169d-b647-32a6-b247-b37cd1600860 | -14.3583 | -51.0965 | 2025-08-07 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd1d4a37-f14a-3afd-b2dd-f3fe433803d7 | -13.64891 | -47.60618 | 2025-08-07 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbf6b608-faba-34de-ae0b-54d90f4560e3 | -11.18163 | -51.44393 | 2025-08-07 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67a04597-8167-30b3-a25f-df6b2a94dd65 | -12.71442 | -46.38258 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 15c254e1-c57a-3e3e-9b8d-27479dbab376 | -13.00651 | -44.8824 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9abfa9b-b74f-3f22-bbab-5e6ba560a593 | -12.32949 | -46.05333 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 702c5212-149d-3be9-a396-4e4f5499519a | -12.33442 | -46.05403 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cecb0525-ce26-30e9-8072-02288a5fee38 | -9.70517 | -61.29263 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e20686e2-e661-3373-a26e-1b137f00e2c7 | -15.74618 | -43.39017 | 2025-08-07 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2f8b7dc4-f518-34ab-ab9e-160807d93053 | -12.70903 | -46.39713 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b99f851f-9906-3488-a9f3-a9e42809e494 | -11.80815 | -44.26651 | 2025-08-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca6f8ac2-1c06-3453-bc50-14d109c22517 | -9.93725 | -60.49795 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16a52857-9b40-3ac2-b25c-2f619d29ef19 | -13.51039 | -47.7228 | 2025-08-07 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc82172e-20ee-3e4b-b4cc-2d9a873e6865 | -12.55265 | -44.74521 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 672693ea-da8d-31fe-8f2c-298ef64b6362 | -9.70807 | -61.30409 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ddaee81-b514-38ee-8f23-1bcd4ef750c3 | -12.54986 | -47.15128 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5861cc9a-4b94-3fc4-a97a-6df7e96f1f6f | -9.93771 | -60.46933 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53fa1ae5-5c89-3b1b-bc59-7eb89eac00f7 | -12.33861 | -46.06038 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63bf60f7-0cf2-3205-9b23-96ea9fba8347 | -14.3877 | -51.04661 | 2025-08-07 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50daead8-78e4-3e23-9237-c8e5c18db482 | -11.75939 | -48.1929 | 2025-08-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4dc44a4c-e0a0-39f7-aa99-7c1508ad4556 | -12.71388 | -46.39772 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1fd80e27-a31e-315c-840a-6eda2f403f51 | -11.89468 | -44.97567 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11a0defe-ab07-3f5f-8d6f-fa8c0d114845 | -11.74697 | -44.96042 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f37a1198-9d65-3a6c-9b08-1172964d394c | -12.71927 | -46.38323 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79e8a30b-ba5f-3ddc-bca1-735952abdba0 | -9.93439 | -60.48781 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1470cf8b-90ab-3ffa-b273-31c631d6820e | -9.93237 | -60.47306 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f22dc16-be30-3458-b05e-b272a40ca066 | -12.34033 | -46.06085 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 224e6c2e-ea62-36b6-ae53-7b533b416734 | -14.53729 | -45.59675 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b99df605-5c4b-3b31-9d14-9186633cba54 | -17.1988 | -44.32551 | 2025-08-07 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b705969-17bc-3431-a65c-364f2323504c | -13.00067 | -44.88546 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f300eb5-d848-357d-b5b7-879d9e6a1532 | -11.77747 | -47.51271 | 2025-08-07 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46b7f72a-5c48-30b4-9b1e-b0b50a1d070d | -11.74468 | -45.02292 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06d30775-8aed-33bd-8fee-9a7a55999154 | -11.90665 | -44.96571 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2336c600-0294-371e-b7ca-14ce817f265d | -12.52636 | -47.15139 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae359bb7-38b6-3411-b9ca-a2a8e0a79ae7 | -9.93486 | -60.45922 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35d4edf3-41cd-3121-ba57-7d851ae35625 | -13.0011 | -44.88192 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df400174-0bde-30c8-b30d-b88241320acc | -9.70997 | -61.2935 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d2b353f-fece-313f-9d13-d4ce1d86c8d9 | -9.93808 | -60.49332 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71b0869d-f680-3b47-95b1-8e801b893288 | -11.74774 | -44.95409 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7d11dff-5925-3ca0-a404-ff54bbd75122 | -11.77791 | -47.54321 | 2025-08-07 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48eeb285-9e50-3757-a24a-c127ed54428b | -14.50819 | -52.77018 | 2025-08-07 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eec48024-77f8-3ab1-947b-295ac76f2ac4 | -14.53723 | -45.59562 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de9a4089-a42a-388d-ae75-38952258b6b2 | -14.5312 | -45.60147 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccc4c809-b99a-3ac5-b193-a09c279c5244 | -11.80802 | -44.26643 | 2025-08-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7065815e-1ae9-3cd5-852f-3e5ebca6a4a4 | -12.52239 | -47.1469 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aab76a3-5536-33e6-85da-aedf1a362972 | -12.71862 | -46.38848 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 638a4c31-7830-3f82-97cf-ef80fa95c8ce | -11.75147 | -48.18763 | 2025-08-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 726291d5-60ec-3d7b-b412-4a85577fca65 | -9.93559 | -60.50719 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 09704732-becb-3c93-b19d-89ad6900df2c | -14.52569 | -45.60517 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 541f94e2-9c75-323c-8176-957e7d9c2a2b | -12.33609 | -46.05448 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68a24d66-aa8e-3b90-be9d-7cf0d69608e6 | -12.52701 | -47.14656 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1047a635-3781-3380-92d6-fcd058a05c9c | -12.72008 | -46.38794 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 504ce821-fca3-3cd4-bfce-82e6f75d90f8 | -13.00432 | -44.87886 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2426fa1-66cd-33b5-916e-a560dc0c9ff3 | -17.20287 | -44.32942 | 2025-08-07 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c57ca711-1567-3a40-a442-44133dc03e47 | -13.0085 | -44.88997 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c03b92d-fa72-3669-8206-46aa4deb7b80 | -14.82502 | -48.40943 | 2025-08-07 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34ea44c6-227c-3670-b433-375cd3a4e0bd | -13.69694 | -50.75739 | 2025-08-07 04:53:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8267184-070a-3276-b81d-ea9c36021303 | -11.75623 | -48.18425 | 2025-08-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 231be2fe-e523-398d-b574-015a898e4549 | -15.93177 | -43.51699 | 2025-08-07 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f31ccd55-0ed2-3abe-b671-83748ff0268d | -11.814 | -44.26353 | 2025-08-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f2df6aa-4a2f-35ba-9c7d-f27fcb4fc218 | -11.74658 | -44.96362 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4970229-2640-3f75-9a4f-8f1932bf9fc2 | -11.90104 | -44.96767 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4519fedf-6586-3a7b-ab4a-8245f31606cc | -9.71091 | -61.28825 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e87d2cb-fd6b-3c78-92d0-b3ae3bd12808 | -11.7557 | -48.18825 | 2025-08-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 39bd2dc8-1d9e-35e2-9962-b88468290ed7 | -12.70765 | -46.3977 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b94f780a-ce72-3c31-bffb-484abefc5823 | -12.53615 | -47.14891 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 169872b6-4f60-3a25-8469-2fe20c7c23b9 | -9.93854 | -60.46471 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e92e507c-2af9-3635-b55f-1cdc3555efd2 | -13.0031 | -44.88947 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c990776d-96e7-3815-afa7-a7c1f8289403 | -14.53683 | -45.5989 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 769ec029-96fd-33c0-9700-1c288bad17e3 | -14.35463 | -51.09595 | 2025-08-07 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0c84094-c5c5-3dfb-b43f-475691482b84 | -15.74623 | -43.39299 | 2025-08-07 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cc1a91b9-ac2b-30c0-a1c5-77da5ce53776 | -12.73119 | -46.3784 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 219df5f5-1c51-3d39-a5eb-84e0766728fd | -9.71381 | -61.29969 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| deedb2c0-6f86-3eb4-9af7-aa7adc736862 | -11.75516 | -48.1923 | 2025-08-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 157f2fa1-841a-33e3-9a9a-7594ea4f427f | -11.81446 | -44.25985 | 2025-08-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5135967b-f7f1-3ea8-9b0a-508077ae0639 | -14.50478 | -52.76959 | 2025-08-07 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 067a7f27-53de-3f35-b22d-02fa05ddf071 | -9.94139 | -60.4748 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5e17165-3b5e-3ed4-bf90-a589fa3a52f4 | -14.53691 | -45.60003 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 390aa7a5-87cb-339b-b0b8-07be14c13181 | -9.70902 | -61.29878 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README19.md)
