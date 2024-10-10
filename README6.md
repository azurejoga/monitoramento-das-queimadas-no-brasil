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
| d1bcc127-92a8-397e-b769-9bed553d1a02 | -14.4861 | -42.103199 | 2024-10-10 00:18:11 | METOP-C | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 52e57a99-ad85-38d2-847a-74a83dd3e316 | -14.5716 | -42.455002 | 2024-10-10 00:18:11 | METOP-C | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2b404ab4-e02a-30be-89c0-cae165600cba | -13.9049 | -41.881901 | 2024-10-10 00:18:20 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d25292c9-25dd-3f1f-a12b-1a5e4a00f2aa | -13.9065 | -41.8895 | 2024-10-10 00:18:20 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aedce3b1-c13b-3420-a7ca-2ea169db2022 | -13.8677 | -42.567001 | 2024-10-10 00:18:23 | METOP-C | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dbf8b631-53eb-3418-a08a-7aca2ef7f2a9 | -13.8694 | -42.5751 | 2024-10-10 00:18:23 | METOP-C | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6a55bc3b-b778-3be8-8d88-0f3d309a5c5a | -13.7819 | -42.645599 | 2024-10-10 00:18:24 | METOP-C | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f945e877-253e-33a7-b5a4-5609a28c317f | -13.7893 | -42.440601 | 2024-10-10 00:18:24 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 28554414-bb7f-3d90-abd2-763e7d57f988 | -13.791 | -42.448601 | 2024-10-10 00:18:24 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 68026b8f-8299-3471-a7aa-70325a45b975 | -13.7837 | -42.653801 | 2024-10-10 00:18:24 | METOP-C | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6a6ce277-2ac9-326a-96c2-644275b67f49 | -13.9999 | -43.676102 | 2024-10-10 00:18:24 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4fce7952-c6f2-3856-985a-0dc96d6e2772 | -14.0018 | -43.685299 | 2024-10-10 00:18:24 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a845a693-1fc8-3257-b376-8d63b5b2c5db | -14.0037 | -43.694599 | 2024-10-10 00:18:24 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e3b6515-95c8-3342-b81f-19b01283cd70 | -14.0686 | -44.006199 | 2024-10-10 00:18:24 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 607c62e5-be00-3b7b-b6b5-d340b56fdc07 | -13.992 | -43.687401 | 2024-10-10 00:18:25 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fcc790a-b2ce-3459-a636-3fe25b35531f | -13.9939 | -43.696701 | 2024-10-10 00:18:25 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f448b1f5-ddab-366d-80f2-1beb9621b0e7 | -14.0588 | -44.008301 | 2024-10-10 00:18:25 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 031bb2af-f025-3ca4-a9cb-343f1e407dc0 | -14.0608 | -44.017899 | 2024-10-10 00:18:25 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80e42054-121e-3907-8c9d-3b56566aeacd | -13.9841 | -43.698799 | 2024-10-10 00:18:25 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f79c23cc-d255-324e-ae32-2936ab5ac8c3 | -14.0166 | -44.1492 | 2024-10-10 00:18:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99853c21-2981-3190-a5a2-eb658e382ec5 | -14.0186 | -44.159 | 2024-10-10 00:18:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b78dfdaf-1d16-3728-8de4-39ff3ee27fef | -14.0206 | -44.1689 | 2024-10-10 00:18:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18b88edd-c682-3631-9955-6b37fa4ab0f4 | -14.0068 | -44.151299 | 2024-10-10 00:18:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9112b934-104b-317a-889d-fa060c0eef82 | -14.0088 | -44.161098 | 2024-10-10 00:18:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aeb04906-b7de-3f6b-8ad2-6f2cd972bf6b | -14.0108 | -44.171001 | 2024-10-10 00:18:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afcf39f4-57e7-3898-839f-3c3f9c4454a8 | -13.9708 | -44.027 | 2024-10-10 00:18:26 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4855c0-e460-3535-9f26-6e94cb69e62e | -13.9728 | -44.036598 | 2024-10-10 00:18:26 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8cb7df6-bff4-38f4-8d7c-f080b7f1b84d | -13.961 | -44.029099 | 2024-10-10 00:18:26 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 495294ba-b6dd-3360-92b4-32d8a81d2833 | -13.963 | -44.0387 | 2024-10-10 00:18:26 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c4b8887-fd34-3c6a-be51-9ef1c7eeb099 | -13.6101 | -42.513699 | 2024-10-10 00:18:27 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d7ac68a6-cd98-3f69-af75-24f996290c1c | -13.6118 | -42.521702 | 2024-10-10 00:18:27 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dbe3c9eb-27f7-3c22-890a-4bd11e07127d | -13.8235 | -43.810902 | 2024-10-10 00:18:28 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44d40659-f26a-31ff-8ca0-1aff3ae5227b | -13.6675 | -43.651798 | 2024-10-10 00:18:30 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 286ce659-7c6d-3415-8562-c4f297451f57 | -13.5911 | -43.6777 | 2024-10-10 00:18:31 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5214661d-b8fa-30d7-90e7-4a1b5b59008a | -13.7852 | -44.5116 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 88ca8572-0168-3e10-aa76-fbeaecbdc007 | -13.7873 | -44.521801 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4940f39c-cf54-30e6-91d0-ecac2afd53e6 | -13.7796 | -44.5341 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 292cc071-60b6-3755-9fb2-4f72b9627527 | -13.7818 | -44.5443 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 728e8fac-837b-311a-95d4-6147531f1a8f | -13.7839 | -44.5546 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d528217-31fb-3695-8b5c-f558434b8eb5 | -13.7699 | -44.536098 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de949947-a349-3383-af0c-313b650382fd | -13.772 | -44.546398 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c97ee5c-1626-3647-8248-6bf38ad8098e | -13.7741 | -44.556599 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f50f4d11-fce0-315d-b37f-7d1c565473a9 | -13.7762 | -44.566898 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 083c6b38-922c-3898-8cd2-7ea6fbcfb94e | -13.758 | -44.528 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a625be2-24e0-375d-91d8-27e8f87d3272 | -13.7601 | -44.5382 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4642e88b-a45c-3423-bfad-f1fc0be78c00 | -13.7622 | -44.5485 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57c5cf9a-414e-36af-850a-a81fee85cad3 | -13.7643 | -44.558701 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16ce0397-fa4b-3e81-95d6-08995cdc2d79 | -13.7482 | -44.530102 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b10d2a61-5317-3e1e-9b0a-57b097d51dac | -13.7503 | -44.540298 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0eb0059-4d61-3fc8-93b5-e3b570f6e791 | -13.7525 | -44.550598 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dbfecdd4-3f17-36bd-b3be-b56ddf486ada | -13.7567 | -44.571098 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b37c667-3098-32af-a503-a486f73477bc | -13.7588 | -44.581402 | 2024-10-10 00:18:31 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79f8f026-5f6e-3e4b-9654-85d2501df5c1 | -13.2446 | -42.435799 | 2024-10-10 00:18:32 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| be114f9c-1be8-3780-a076-f5092888e028 | -13.2463 | -42.443699 | 2024-10-10 00:18:32 | METOP-C | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fb7e5169-52d9-321e-b019-e47e4692456e | -13.726 | -44.620602 | 2024-10-10 00:18:32 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 954f4688-8c5a-3036-9136-ee928494667e | -13.7282 | -44.630901 | 2024-10-10 00:18:32 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89169529-89d1-3f6b-8d5e-8c21752e68d7 | -13.738 | -44.628899 | 2024-10-10 00:18:32 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 005e97b6-088e-3dc9-8f63-ce1e3f115fa1 | -12.5394 | -39.629501 | 2024-10-10 00:18:34 | METOP-C | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab237911-e56a-3c61-a32a-fd5cdcac8ac2 | -13.4573 | -44.309101 | 2024-10-10 00:18:35 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33f18e74-fa9d-313e-9e77-92b9eb82a189 | -13.4594 | -44.318901 | 2024-10-10 00:18:35 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e136bc8b-ac14-39c1-b62b-8982b93727d0 | -13.4475 | -44.3111 | 2024-10-10 00:18:36 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad5d0f6-bd6f-3835-bf60-a883216b3477 | -13.4496 | -44.320999 | 2024-10-10 00:18:36 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c1eb482-b14a-3fc8-b6a4-e217a6da4176 | -12.2404 | -39.2244 | 2024-10-10 00:18:37 | METOP-C | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c629164d-12fd-326c-890d-71fd637a498c | -13.1381 | -43.134102 | 2024-10-10 00:18:37 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 32602658-0d2b-348e-827e-d2fc10d4bebc | -13.1283 | -43.1362 | 2024-10-10 00:18:37 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5fa9c486-91e9-31f1-9942-2869e6e51627 | -13.1301 | -43.1446 | 2024-10-10 00:18:37 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3e1020f1-8726-3915-96d3-daad667265b1 | -13.3349 | -44.702999 | 2024-10-10 00:18:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 095fac42-ba9b-3d34-a844-1a4a910740eb | -13.3229 | -44.694801 | 2024-10-10 00:18:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48f16756-71a5-3d73-9886-a0987e33cfc2 | -13.3251 | -44.705101 | 2024-10-10 00:18:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3af3d887-2cc1-3e62-b3c5-672f056d5d0b | -13.311 | -44.6866 | 2024-10-10 00:18:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0f428f7-6b6e-327e-8bab-ee19e182abc6 | -13.3132 | -44.696899 | 2024-10-10 00:18:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a7a2be1-4221-3bd6-a512-0f69f6ac02e9 | -13.2991 | -44.678299 | 2024-10-10 00:18:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f857ca6-6303-3dc9-aefc-96d102a934fe | -13.3012 | -44.688599 | 2024-10-10 00:18:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e9aeca0-e7b1-3a15-9def-6f70fff8377f | -12.9017 | -46.219898 | 2024-10-10 00:18:51 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7491126a-62ec-3e4b-92c0-a2f62042febb | -12.9042 | -46.232601 | 2024-10-10 00:18:51 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecd34b0b-a748-322e-aa5a-b1b682a81fdf | -12.2222 | -43.738602 | 2024-10-10 00:18:54 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c302423-84e0-33d5-8ae3-fe21272c7e07 | -12.2241 | -43.747398 | 2024-10-10 00:18:54 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e35366bd-e1e5-340a-bb60-a335ba2a909b | -12.2124 | -43.7407 | 2024-10-10 00:18:54 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 480d1eea-4cb4-31a9-b245-29563796a9d9 | -12.2143 | -43.749599 | 2024-10-10 00:18:54 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5395e2-e77f-3372-840d-21fd242e9be7 | -12.2161 | -43.7584 | 2024-10-10 00:18:54 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9323ded4-7cf1-3b70-b96e-ed48a10fc742 | -12.2075 | -44.393002 | 2024-10-10 00:18:56 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89189b8d-62e9-3595-b5d2-a6df0253df2b | -12.2095 | -44.402599 | 2024-10-10 00:18:56 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34ba398d-7b99-3045-a8ed-65448b99ecb8 | -12.2892 | -44.733101 | 2024-10-10 00:18:56 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c7ba0c6-1afa-372d-9f5d-03fec34b7e4a | -12.2914 | -44.743198 | 2024-10-10 00:18:56 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2ed2ed1-4422-3da4-9573-91b9cd54b03b | -12.221 | -44.6026 | 2024-10-10 00:18:57 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2fa17e-6345-371c-9739-18e0a13cf53a | -12.2231 | -44.612499 | 2024-10-10 00:18:57 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d45f247-5304-3cdc-b8be-674b463341ee | -10.1579 | -36.351501 | 2024-10-10 00:19:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69b3a6d8-d769-397c-adeb-c5864b8dec58 | -10.1602 | -36.361 | 2024-10-10 00:19:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9537bf6-babf-3293-a6bb-65c114e945ac | -10.1625 | -36.370499 | 2024-10-10 00:19:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f093f530-246c-3b42-ae6e-30ae6ee45e95 | -10.0259 | -36.1903 | 2024-10-10 00:19:01 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 370d6b76-229b-3bd0-ab85-45d0d0774431 | -10.0283 | -36.200001 | 2024-10-10 00:19:01 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ca52e2e-6881-3e0b-8e58-cb447fa87863 | -11.8242 | -43.889198 | 2024-10-10 00:19:01 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c054a58-298b-3328-8174-d2f481d0442b | -11.8261 | -43.898102 | 2024-10-10 00:19:01 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00e7cb84-4c86-35ad-9d39-dae52c623c2d | -11.8163 | -43.9002 | 2024-10-10 00:19:01 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81187200-cd72-37d4-a2b0-18e8a0b6d489 | -12.379 | -47.305698 | 2024-10-10 00:19:03 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aeb2fb14-4bb0-3b19-bc07-6bf61f4674cf | -9.8412 | -36.1525 | 2024-10-10 00:19:04 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 844d78e3-7930-34bf-9bda-fba42c084ccf | -9.8435 | -36.1623 | 2024-10-10 00:19:04 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8de9b100-2c67-3a19-8d70-d94e6536e2ea | -9.8459 | -36.172199 | 2024-10-10 00:19:04 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31ab5446-57ba-32b2-8f08-e4797853957a | -9.8314 | -36.1549 | 2024-10-10 00:19:04 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6dc93907-f5a6-36eb-9583-ed5c8902bd34 | -9.8337 | -36.1647 | 2024-10-10 00:19:04 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README7.md)
