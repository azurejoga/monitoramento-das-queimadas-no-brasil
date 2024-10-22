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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a44ec15-7160-32b9-97f1-7609fda679e2 | -5.69951 | -43.14378 | 2024-10-22 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3c7c7dc8-b7cf-3263-be97-2d89a96a1771 | -5.69895 | -43.14738 | 2024-10-22 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8fa04f86-40eb-3099-9bcc-9c685f065dae | -5.62707 | -43.28667 | 2024-10-22 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00c68d13-00f6-370a-9d8f-2db84f45919e | -5.62652 | -43.29021 | 2024-10-22 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa51756-4088-3e04-9b02-f27136010c72 | -5.61858 | -42.77675 | 2024-10-22 04:17:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8921937a-f5fb-3077-8d26-09a789a4b7cb | -5.61802 | -42.78039 | 2024-10-22 04:17:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e982d948-9e43-3d99-b7af-4f4b3d63f8ce | -5.61519 | -42.77621 | 2024-10-22 04:17:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 55b56a21-607d-3eaa-891f-e942bb067a9c | -5.52541 | -42.22057 | 2024-10-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 796efac4-9ed2-305c-9ca2-cf94dcaf0f64 | -5.51187 | -43.46066 | 2024-10-22 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92443121-2413-34c0-8106-2baef8fc23a9 | -5.50854 | -43.46014 | 2024-10-22 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51f0ad84-49b9-36e9-838d-87bc9e2ac96e | -5.36332 | -42.73039 | 2024-10-22 04:17:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f86ad74-bf18-3f90-80bb-ff6a12843bb6 | -5.3316 | -43.15739 | 2024-10-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86398236-e247-30fa-96c2-5865dfb28f62 | -5.30183 | -43.9773 | 2024-10-22 04:17:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c2dafb8-762e-3602-b49e-f5b9909e84ad | -5.30129 | -43.98075 | 2024-10-22 04:17:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f5b0a9d-bbb1-31fd-9f0f-0b7f75ac9e55 | -5.12487 | -41.06305 | 2024-10-22 04:19:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3cbfb9f-b82f-3a49-89e3-b061e12e17c5 | -5.12481 | -41.05988 | 2024-10-22 04:19:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 179e104a-05fb-3976-a2e7-f8d594935b75 | -5.12416 | -41.06408 | 2024-10-22 04:19:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 742beccc-14cd-31b3-9edf-852afc896869 | -5.0799 | -42.56808 | 2024-10-22 04:19:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d08f7ffc-d504-302e-b1bc-fdd740138ccc | -5.05238 | -41.95186 | 2024-10-22 04:19:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae61e7e6-fcb0-3d3d-9d15-45dd0eb53cd0 | -4.938 | -43.01678 | 2024-10-22 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea3cb86c-4b5e-3048-942e-1c7cf6017689 | -4.93745 | -43.02036 | 2024-10-22 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1526db1-0d26-3eac-99a7-220e2aa52360 | -4.93554 | -43.02021 | 2024-10-22 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ac43baa-97bc-3981-bca0-1b0973062710 | -4.93274 | -43.01612 | 2024-10-22 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5d70cce-8f6b-3c60-b5a2-745ba70a7489 | -4.92286 | -41.97184 | 2024-10-22 04:19:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 231bdbae-4cbf-3617-bbed-b36acd6ce63d | -4.92129 | -43.21424 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4cc36c2-fca7-394b-96a6-97a86e94093a | -4.91997 | -41.96746 | 2024-10-22 04:19:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f723222d-bdee-3486-81c1-2aeb62f9bf19 | -4.91939 | -41.9713 | 2024-10-22 04:19:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e6ebb09-a9f8-352c-baeb-baeb7ef830e6 | -4.91794 | -43.21373 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6f7a50b-59e1-3332-81dd-53c832c6f7d7 | -4.86495 | -43.25257 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1cf17a7-2d0a-3572-be21-4b890bd119cb | -4.6246 | -42.38655 | 2024-10-22 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d62f09a6-4d70-3a37-a627-816126f0b080 | -4.62118 | -42.38602 | 2024-10-22 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 065e8fd4-a313-3cfb-9e21-7c26d506e4bf | -4.61833 | -42.3818 | 2024-10-22 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a6ddb0d1-d885-313f-a871-f6e1cfcacbaf | -4.61806 | -43.39803 | 2024-10-22 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c05580b0-2f5f-353f-a10f-1ba3cc0529b2 | -4.55381 | -43.57005 | 2024-10-22 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02c9a8e8-b1ce-3b81-8f9f-70c9a0423b8b | -4.55049 | -43.56953 | 2024-10-22 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 360ef94d-e2ec-30c5-8915-411af007a7dd | -4.53548 | -43.27388 | 2024-10-22 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47a068ba-e15c-3edc-9108-6add085275f7 | -4.46834 | -42.89772 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6be513c9-4780-37a7-bf96-c3675261486a | -4.46554 | -42.89363 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fceb1dd-0a36-352b-8b99-ec694e375164 | -4.46498 | -42.8972 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9b1fac9-96be-3bfe-b214-fb96ba83aba0 | -4.46387 | -42.90435 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7131ba19-b654-3840-9e25-3bab775c3448 | -4.46332 | -42.90793 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ddcd2b0f-dc23-33b0-b102-2c2b784b3c0f | -4.39972 | -43.57777 | 2024-10-22 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c40dc49-f1dd-3c9e-85ea-a36466e036d0 | -4.39641 | -43.57726 | 2024-10-22 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da30e198-f9f1-3813-8843-d838d470ce5e | -4.30192 | -43.59423 | 2024-10-22 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c7b7594-ee07-3d84-9043-b5bf820f2dff | -4.17681 | -42.98423 | 2024-10-22 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8cd8955-f745-3835-b231-a80d828e582d | -4.17626 | -42.98777 | 2024-10-22 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3d20473-7ba0-34f8-af84-5263b0b7cc2f | -4.1588 | -43.3586 | 2024-10-22 04:19:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a031b6e-57f1-3096-8ba2-633985296562 | -4.12119 | -43.33881 | 2024-10-22 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f376a32a-bdb4-3838-8343-f25e990b7ef2 | -4.12065 | -43.34229 | 2024-10-22 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a54f43f7-6213-3fcc-84d0-7838b7347c76 | -4.03828 | -43.21511 | 2024-10-22 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0057682-5139-33f0-a9a4-663e5fff0047 | -4.03773 | -43.21861 | 2024-10-22 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4daf1e6f-4e0c-3170-afa3-9d721437227c | -4.00199 | -40.38451 | 2024-10-22 04:19:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a83148d9-598c-3139-9654-7209be07153b | -4.0013 | -40.38899 | 2024-10-22 04:19:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16c72dad-1cb0-37c4-bc6c-6b3a6a17e20b | -3.95894 | -43.22434 | 2024-10-22 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e5a402-b857-3c5d-b5fe-250e270c0ea6 | -3.95561 | -43.22385 | 2024-10-22 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d57752c2-8d2a-3ac9-9077-e114baec9a08 | -3.94627 | -41.4967 | 2024-10-22 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e2d60c3-69f3-31d1-9477-99baa94da748 | -3.92615 | -43.71659 | 2024-10-22 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9fdcd87-2954-35cc-8740-5e09a3400740 | -3.89086 | -43.13834 | 2024-10-22 04:19:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a454f4b5-f636-3a8c-9a34-d262f3ae2f92 | -3.87157 | -42.45341 | 2024-10-22 04:19:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85b0cc83-c2cf-3383-b0a0-ddf6e2c0036a | -3.85513 | -43.25807 | 2024-10-22 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 987e32e1-fa8f-3d5b-9bbf-8fffbddaedf9 | -3.7751 | -40.9859 | 2024-10-22 04:19:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d54c0e41-d86f-31a8-9573-4111d9d89969 | -3.774 | -43.23482 | 2024-10-22 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c8f18ce-8bb4-3acc-80c8-151f4121b5df | -3.60635 | -40.37192 | 2024-10-22 04:19:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c4d2905-e83e-32a7-a254-c55c18bec332 | -3.5925 | -42.82946 | 2024-10-22 04:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db388e99-210f-3ec1-b114-81ba3f207490 | -3.59195 | -42.833 | 2024-10-22 04:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 474ae802-6094-3bc3-8806-a9f98b020db8 | -3.58916 | -42.82895 | 2024-10-22 04:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df24ef84-6846-3b58-b6ae-1b45c1356fd5 | -3.5886 | -42.83249 | 2024-10-22 04:19:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43b2bfd7-cde8-390d-99c6-e77d6f54bf94 | -3.55623 | -41.40104 | 2024-10-22 04:19:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b1a3565e-7306-3f00-9ac0-afed231c19b2 | -3.52415 | -43.61497 | 2024-10-22 04:19:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5391ad32-66be-3ada-b6ec-10990093fc37 | -3.52139 | -43.61101 | 2024-10-22 04:19:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c00b4b1-f072-3810-b268-7676a144818a | -3.52084 | -43.61446 | 2024-10-22 04:19:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1f88af3-65a9-3a82-b6d2-12d813b7c50b | -3.44685 | -41.26398 | 2024-10-22 04:19:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0afbe719-2440-3342-bf29-9e46a595f839 | -3.44512 | -41.2518 | 2024-10-22 04:19:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a3d5d50-84df-3f60-9f05-5f30d97edb36 | -3.44392 | -41.25952 | 2024-10-22 04:19:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0008ba82-0fd9-380c-a404-6b6ef111740f | -3.44332 | -41.2634 | 2024-10-22 04:19:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ec0135f-f551-37fe-a216-dd38c1613126 | -3.43979 | -41.26281 | 2024-10-22 04:19:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 759ac004-d5ba-3bfa-8f0f-005e5434a911 | -3.41083 | -42.71051 | 2024-10-22 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95507f36-8a2c-3e25-8347-0737da0e3953 | -3.40692 | -42.71355 | 2024-10-22 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 646f2e6c-9366-3127-94b0-7b0e8603eb3a | -3.28063 | -42.03782 | 2024-10-22 04:19:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2245e2ba-7dc6-3a49-b484-e7b38d7135de | -15.56762 | -47.85489 | 2024-10-22 04:19:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25b9e50e-6840-3d53-9770-24c2ed4ec487 | -15.34815 | -48.13377 | 2024-10-22 04:19:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9dd2d3f-89f9-3f53-912b-0b89abcd2437 | -13.39134 | -40.47431 | 2024-10-22 04:19:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1e181951-c961-379f-b23e-fa3db97e7ecf | -12.54609 | -38.99752 | 2024-10-22 04:19:00 | NOAA-20 | CONCEIÇÃO DA FEIRA | BAHIA | Brasil | 2908200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0fc3166f-13f7-3f15-bc3e-74bc23986510 | -11.72924 | -37.61647 | 2024-10-22 04:19:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7590f638-170b-3598-ae10-34f76f582ff8 | -10.84079 | -44.78373 | 2024-10-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4de9c1a7-a81a-3160-ac58-cba904fd71a4 | -10.75985 | -45.02066 | 2024-10-22 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30674b6c-ea4f-3bb4-bcb9-3bb69dfd1747 | -10.75654 | -45.02013 | 2024-10-22 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f40af3d-502d-35c4-a6cb-c74c7216db2b | -10.44667 | -44.89521 | 2024-10-22 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 007f6013-db37-3f44-9344-ec78ffdc26c2 | -10.44612 | -44.89873 | 2024-10-22 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 503d03ab-8798-3623-974e-948f9ca378d3 | -10.4428 | -44.8982 | 2024-10-22 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52d7e751-40b2-34cc-8cbf-ff7cdb17aca1 | -10.30056 | -36.67996 | 2024-10-22 04:19:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0c48b5f8-f5a9-355f-83e2-6a9991c53cce | -10.29495 | -36.68221 | 2024-10-22 04:19:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af707e33-a7ab-3316-a05b-56194c939b5b | -10.29456 | -36.68533 | 2024-10-22 04:19:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 763fdd86-91d3-3f57-9ec5-ce986a00d8d6 | -10.28755 | -36.32694 | 2024-10-22 04:19:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ab9b8936-d053-3736-95fa-f7d8b1201f0e | -10.28711 | -36.33035 | 2024-10-22 04:19:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0bf0436e-42b8-37d9-af15-efe1ceb24646 | -4.81811 | -44.35345 | 2024-10-22 04:19:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 064063a4-083a-3334-a41f-e1a2f14945ce | -4.62405 | -44.5522 | 2024-10-22 04:19:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b488833b-c9ca-34b8-a678-e6138d472d95 | -4.6235 | -44.55565 | 2024-10-22 04:19:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca93d06e-5684-3c2d-acfb-6e225096f7cb | -4.62074 | -44.55169 | 2024-10-22 04:19:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c70ceb32-2386-3729-9f08-734b1c8f17b7 | -4.6202 | -44.55513 | 2024-10-22 04:19:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
