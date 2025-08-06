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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e436d04-7f25-3fc6-81ea-de5dc0c28975 | -8.00608 | -43.23397 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3877be8f-25d6-32c5-8706-4285891a40c9 | -7.08537 | -44.35884 | 2025-08-06 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1dda77e-3538-3ceb-9554-90920c65ded8 | -6.54707 | -43.61073 | 2025-08-06 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c78fe83-018a-32ea-89d8-b0c2cf09232b | -7.91327 | -45.52752 | 2025-08-06 03:30:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3fd9c63-a482-394b-9632-2d778356798b | -6.98809 | -42.10062 | 2025-08-06 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28e8f3f3-5496-3fb2-8324-b90e7d4ea07a | -8.51815 | -43.31264 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 642db9c1-4f8a-3cdb-8776-49fbd794cdd7 | -7.14695 | -41.2312 | 2025-08-06 03:30:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ad6df110-414b-32f1-924d-6a60b9015a32 | -7.99866 | -43.24161 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c9275591-78b8-3c3b-8969-3c7f3e61d3f9 | -6.74712 | -45.29599 | 2025-08-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17a2f6e6-bee3-3d8e-9c06-8eac44aab4cf | -4.19323 | -38.37558 | 2025-08-06 03:30:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8b5cf422-079b-38c4-a3d7-4896716f26ee | -7.37481 | -44.25497 | 2025-08-06 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb1888a1-e2a5-39fc-90b3-7a2535661baa | -7.90783 | -45.53367 | 2025-08-06 03:30:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8ea6443-0796-3b35-aa32-9607dcdbcbb6 | -3.94827 | -41.48059 | 2025-08-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d3e6d9e6-8a34-3e98-ae4d-9640f5f8401c | -4.32147 | -38.12865 | 2025-08-06 03:30:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5680b33f-a545-3243-832e-b77c400c1777 | -7.18915 | -45.48077 | 2025-08-06 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 654d461a-58eb-34fc-a6a5-391cfc9a73c4 | -6.55319 | -43.61189 | 2025-08-06 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e02f5922-30d9-3481-bf48-a59485e868f8 | -8.87529 | -44.79351 | 2025-08-06 03:30:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ff50ef2-9655-38a1-8067-da16cdc3e1a5 | -8.00768 | -43.21992 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2412cc3d-6965-397d-856f-166f8e2eeeea | -7.36974 | -44.15885 | 2025-08-06 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c5d5668-afcc-389c-a84e-dda005eb1423 | -7.98418 | -43.15551 | 2025-08-06 03:30:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0db66416-899a-3a46-a0c7-aa30c0cf2ad4 | -7.18237 | -45.47949 | 2025-08-06 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02d4f895-21af-3486-add3-0d0e9f2e4e9d | -8.00537 | -43.13644 | 2025-08-06 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac1d4120-d272-33bc-8009-74bfc6e8b5ec | -10.4319 | -44.36963 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75aa65f5-f2f6-3350-b202-2cfd05563572 | -12.04246 | -44.01919 | 2025-08-06 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc1f90d4-6e00-3f38-811c-32ecce62de2d | -11.43513 | -45.13546 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5445eec6-27ce-335f-87a8-12287a0b9b53 | -12.96928 | -44.8798 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64aba5fc-86c0-3026-8f96-fc6b514f3739 | -11.84167 | -43.72743 | 2025-08-06 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9e73629-9746-3cf4-87d4-cdbdb09e1ae0 | -11.76772 | -44.96616 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18eb42b5-da86-381d-afa7-7bbaaae61ef3 | -11.91205 | -44.94407 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca0f32c4-1df8-359f-9730-7bba3066eb65 | -12.99214 | -44.889 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 060d0a95-51cf-30c9-998f-59e3a9b6be08 | -10.47694 | -44.34097 | 2025-08-06 03:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cc32719-c975-332d-a806-a493e908ffeb | -11.76166 | -44.96474 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3157f05-c2a4-3bc4-9d7a-843671cff431 | -16.256 | -39.04752 | 2025-08-06 03:32:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 41df1661-8188-38f4-980e-4d8ed2f8dbd0 | -12.55579 | -44.73802 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eee07fe-56e2-3296-bd53-50c9a50751fd | -9.64559 | -43.84493 | 2025-08-06 03:32:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| edf764bd-1015-3d65-a90d-58f5f8a0bd5c | -10.48119 | -44.35095 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3e9bf5d-7623-389f-b723-0b6c08a5c3e4 | -11.7617 | -44.96491 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6139d1a-ed53-3cef-b6f5-b993bf75f294 | -11.43297 | -45.14616 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 299ac125-6a35-38a2-a9d8-4578ae8c422f | -9.46381 | -46.30418 | 2025-08-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65e0e89f-40d7-3631-b345-c857a0967847 | -12.38245 | -47.04292 | 2025-08-06 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 343e5418-c6d5-32c9-b860-f5909062101e | -12.55289 | -44.73814 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b06193-aa0b-361d-82ea-2d9570b27a78 | -10.48251 | -44.37574 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bc7a650-d433-3c19-ac0c-a3fe10104db8 | -10.47235 | -44.38655 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d382237-d217-363a-a862-140ea9256ecd | -8.98518 | -45.68602 | 2025-08-06 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b83d4130-23fb-3e8f-8378-8db73e897b6e | -15.54668 | -42.65723 | 2025-08-06 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17e3f37b-ec08-3f13-811c-b58d185aec6f | -16.25688 | -39.04248 | 2025-08-06 03:32:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6fa94daf-c31b-3442-aceb-84ff748992bf | -9.47069 | -46.30535 | 2025-08-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd8e61ec-b671-3855-bf45-b25abb83650b | -11.74472 | -45.01845 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4d2be69-7e3c-355c-a687-d3e1c789d0b8 | -11.83602 | -43.72633 | 2025-08-06 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 874694fc-0110-3501-9a4a-b8d3b405771a | -12.53456 | -47.17248 | 2025-08-06 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1a10a5c2-648d-3250-9f1f-1a716956148a | -13.37584 | -43.75589 | 2025-08-06 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fd92f6b-eac7-3f43-9422-f16d324705fb | -11.03064 | -45.06544 | 2025-08-06 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a7ef702f-577f-3a10-9d78-e7fcd3e5b68d | -11.74566 | -45.01368 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1db83480-4b84-32a3-a152-8554c213c3c2 | -11.75739 | -47.53112 | 2025-08-06 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a270666-632e-3c16-9bf5-36e552c47cad | -12.75716 | -44.41774 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 526de73c-536e-33ca-a2f3-d97947c95744 | -12.7589 | -44.41039 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 720be8da-1cac-309f-bf31-753724da6144 | -12.55884 | -44.73927 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b19501f-822c-39a0-91e4-d3d051cfdcab | -11.76776 | -44.96629 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f142adc2-ea52-346e-a48a-df0dd5375815 | -11.42925 | -45.14083 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 434479ad-36cf-310b-8ae7-58490ea2ec75 | -12.9718 | -44.88253 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe6be29a-d267-3863-910e-20698e9c0d46 | -12.5414 | -47.17391 | 2025-08-06 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c50713a1-569f-30ef-a320-e095a050b2d4 | -14.71292 | -47.85528 | 2025-08-06 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 959b9ba1-16d8-3914-acfe-97b7d71755b0 | -12.55198 | -44.74258 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04a5a403-3cef-3566-8b94-1809643cf43b | -9.47026 | -46.30516 | 2025-08-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8eae045-7349-3d87-ba94-5f1621bd76a4 | -11.75641 | -44.95922 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23207898-a922-3a9f-bee7-590eb56d6f4f | -12.97429 | -44.88553 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08ce14bc-d334-36d8-9da9-d32300728f17 | -12.75807 | -44.4146 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9750950a-100a-3bd1-ad75-598ac9408886 | -12.99618 | -44.89947 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35e33040-a62b-3540-9d25-93e6d0d71fa9 | -12.98529 | -44.89223 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99fe8329-8a5c-3b10-8a16-154ca3ceaecb | -9.07965 | -45.05835 | 2025-08-06 03:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c1f43fd-282f-3d1f-91f3-31dcb3ed2445 | -10.43888 | -44.36584 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 571c3e3c-44d6-3208-be4f-7b0e6e5edbb2 | -11.72743 | -47.53334 | 2025-08-06 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 345ffa76-f0b6-39fc-8d23-a0a00172361c | -12.03677 | -44.01785 | 2025-08-06 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f38caacf-b10b-3012-bdaa-1da1de9ccfa3 | -11.89884 | -44.97809 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a094e816-dd1a-3428-8682-e325cf40a373 | -12.02361 | -44.82581 | 2025-08-06 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acc5ec03-68af-3c96-b7ee-99790346137b | -13.37511 | -43.75958 | 2025-08-06 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03268565-4213-381d-a01a-df6919e13467 | -11.90495 | -44.97921 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7255348-5a1a-3309-8819-76df1618b72a | -10.48569 | -44.34938 | 2025-08-06 03:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7453dd05-d4b3-33ba-8cef-4be65e02775f | -11.43031 | -45.1354 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f76beed9-d4b1-3838-af5d-ed6dcf6ebc28 | -12.02545 | -44.82405 | 2025-08-06 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cc3ca2d-ee3b-34eb-b3d0-2d1189260a3a | -10.48029 | -44.37764 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7c48936-c674-3dc2-907b-03682edf90dd | -11.43616 | -45.13039 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| dc4ed92f-47f5-3eed-af55-097b74f3b06b | -10.43283 | -44.36484 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0a4b156-3854-32c2-9f83-ece9229be5d3 | -12.75802 | -44.41352 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f940e9fe-a664-399a-93b9-786a14db8316 | -12.54984 | -44.7369 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18c36498-d1e4-338a-835e-1bfbaa067d96 | -12.54895 | -44.74136 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19a844b0-4220-3bdf-9f17-087f6fe93b0a | -10.44592 | -44.36172 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3a9c8cc-51f0-30f9-9879-c898799875eb | -11.44135 | -45.13658 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c711be28-a271-3e7e-bddc-134e6a1b2dbc | -9.08053 | -45.05964 | 2025-08-06 03:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5bccbf60-963a-3abf-a214-ae2fda2ec4a4 | -10.65079 | -45.23637 | 2025-08-06 03:32:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ce01452-aa90-3156-af64-e3d52ab04450 | -11.73625 | -47.52649 | 2025-08-06 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c17d4960-f8aa-3226-9002-80e45c5fcfb3 | -12.89433 | -43.7942 | 2025-08-06 03:32:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdb57fe6-b282-3f0a-8121-baff1edc2205 | -12.99121 | -44.89354 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ab6a93a-905f-3315-9137-1d8769172891 | -12.7187 | -47.79709 | 2025-08-06 03:32:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd2623a4-1980-3905-a83b-b5bd4758ba9c | -12.0264 | -44.81937 | 2025-08-06 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1105a24e-7b3e-3cb5-90a3-caff1dee3b5e | -9.07322 | -45.05713 | 2025-08-06 03:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a095a092-9dab-3ac3-af4f-78f1e21012d6 | -11.91532 | -44.92785 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 162fe72a-0460-3a65-8bc3-71672f714cc4 | -12.71169 | -47.79543 | 2025-08-06 03:32:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 023eda98-bb22-35b4-81b7-4e6de7035297 | -11.43134 | -45.1301 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b08278e9-c945-3829-aa83-1b00feb86f88 | -11.90932 | -44.95759 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README7.md)
