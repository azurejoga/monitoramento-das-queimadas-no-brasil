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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f366f62e-1db2-308a-8a39-e5729c2d9332 | -6.98992 | -42.79726 | 2025-10-01 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7037fad3-4d92-3bb8-8e72-caea4c4f6283 | -8.73956 | -45.91888 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dcfaf1e-f4d0-37d4-b082-d7784e194e77 | -6.55882 | -46.59341 | 2025-10-01 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 746d5202-b4a6-3ec6-8032-0db320eda8db | -5.80104 | -43.0702 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3b338e7-307b-307b-8d92-006399eb5724 | -6.27992 | -44.06655 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50c5cb49-b13b-3849-92d6-9020cb179669 | -5.47158 | -43.06796 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea3c9ba8-caea-3b8f-be61-f00b47a169a0 | -5.86185 | -47.63107 | 2025-10-01 04:19:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a64d8017-ce47-377b-8c60-5707bb8ae0ca | -3.50107 | -52.4662 | 2025-10-01 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ff83c8e-208c-3151-9e3d-bcb1a87de631 | -6.79795 | -44.87 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9e7c556-0ee9-39b5-af34-1450ee02d9ad | -6.03206 | -43.6018 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87aeae6b-1178-32af-b152-4e314479ac0d | -5.86775 | -42.63449 | 2025-10-01 04:19:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14a0b3ea-c9ac-383f-ab1b-a74a74a50436 | -5.72486 | -42.88077 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a8f6120c-a9ac-341f-95db-1811f5ffcabc | -5.38671 | -42.86666 | 2025-10-01 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d47cb79f-5e89-30d4-bd67-cb0121a74530 | -7.47845 | -47.28056 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe6c1e94-6eab-3ff1-9842-a6d22b515425 | -5.94123 | -45.83464 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d92a031-eada-3c24-baf8-f98b8c3e51f9 | -5.91073 | -43.92357 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ab28c35-dcd6-37c6-8fb9-447d141ec09b | -2.25029 | -47.88644 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2cdfaaa7-bbdf-3145-9184-54d2b6005efc | -5.99651 | -39.30906 | 2025-10-01 04:19:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2bfa7c84-f367-3646-b795-f318a244e323 | -8.70674 | -44.84703 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76af77d7-771e-3116-b97f-1b92f1ab8b03 | -3.75189 | -41.04213 | 2025-10-01 04:19:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d00ac004-fbfd-3024-94d2-ceaf63ea257c | -3.40239 | -46.9003 | 2025-10-01 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ab788b7-d6c8-3c74-872b-7ca3c4532f42 | -8.91603 | -46.07301 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 008a8bec-c591-3f32-9ad4-110e15741d5c | -5.79028 | -43.29632 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6570b002-d0ed-3a6b-8bd2-dd7218d52bf5 | -9.42019 | -47.33152 | 2025-10-01 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92380387-625b-3d8a-b791-8425dbc20f29 | -4.14366 | -38.24471 | 2025-10-01 04:19:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dab9f8b4-8d77-3258-9a44-476ed91819f5 | -7.02558 | -44.47779 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b43d9f0-35b7-3dda-ae9f-3014aa95ee41 | -7.63295 | -45.44558 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8dee9567-cf6e-34c3-acfd-d7a3cc1de994 | -5.49905 | -42.75292 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 27de9491-661f-3f2b-bfbe-2536ce9413eb | -2.59368 | -48.11858 | 2025-10-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a37b350f-9f09-3f58-9dde-2991b2adbfba | -9.79516 | -45.93892 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07e2c79e-90ab-38b0-b16e-0351a7ab4ed9 | -5.9317 | -45.89489 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1deae061-3914-311b-93af-5aacd5d8c898 | -5.88415 | -48.12011 | 2025-10-01 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b004a196-e23a-3c47-b821-6d8df4e66fcc | -9.48159 | -45.5498 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a380144-cc29-38ad-9435-9211415d3e1c | -4.25521 | -48.55487 | 2025-10-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d46ded4-9010-3a84-83e8-3c7c42c39431 | -5.4945 | -42.73713 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4a019e7c-379c-387c-a837-ba4cd649350b | -9.79625 | -45.93197 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f7e8768-8ab2-3e8d-86fd-fc2b73cd150b | -5.77354 | -43.2937 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41e86d9d-c94c-3406-aced-f5ccc2909e6a | -6.43383 | -40.62274 | 2025-10-01 04:19:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dab98b9b-6719-3338-96f5-4db08b029f43 | -5.83037 | -43.9608 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb097f40-4d21-39cd-8b51-0b9e0051685e | -7.02547 | -44.78611 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f88f6eca-7e7e-3110-8a7d-48311816952c | -8.58508 | -44.66726 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7718a16-6ec1-360f-af2a-d94c4d9674e1 | -3.25689 | -40.63167 | 2025-10-01 04:19:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8206e12f-66a2-30ff-80dc-80c04455aef2 | -5.78583 | -43.30293 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd6f7b99-64af-3f88-8b23-b0fa325d3c22 | -6.46308 | -43.93784 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 204ae605-07f9-3ffc-b166-bd78cec27024 | -5.93561 | -45.89187 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 79609805-2e66-3e57-8da3-e5ee2db1fb4c | -7.21312 | -45.47406 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39e26baa-7244-30c5-a194-415c7ee839af | -6.05512 | -44.43785 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 142d2c3b-facd-3e6d-8cd3-eab0a38f47ac | -7.4508 | -47.27617 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94fdfd65-c8f5-323e-a459-634790451fd2 | -6.10259 | -42.68128 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 94e76144-3aeb-3186-99f6-2f0538842630 | -8.5446 | -40.60684 | 2025-10-01 04:19:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 907d9ab3-6c67-3c48-8b49-055f2678ded5 | -3.05178 | -51.10259 | 2025-10-01 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e884e3f7-6005-3598-a989-ef2a67c71a19 | -7.39739 | -44.60437 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b37ffd48-bb91-31af-8bf8-fa662656d176 | -9.9321 | -43.65666 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a840793-55e7-3841-b13f-4acb03d89be6 | -5.6388 | -43.92337 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 5463d2a5-3ca8-34b7-a979-3e416c62e5aa | -3.496 | -52.46547 | 2025-10-01 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75349bb2-42c1-3286-b986-f378bd5c0094 | -6.06838 | -42.67606 | 2025-10-01 04:19:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db640499-0224-355a-97d7-4d8d3edb9c48 | -8.70728 | -44.84356 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b59e156-1e20-300f-88c7-5e93783dbb77 | -5.64372 | -43.91345 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4465c601-4545-3bef-9313-3adff6527a52 | -6.09514 | -42.47659 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 125b36c3-e276-3091-a068-98ac7084a395 | -3.40241 | -46.90053 | 2025-10-01 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b65609c6-11f4-39dc-a54c-07a8a679b305 | -5.64865 | -43.90353 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 945ecf59-f551-3dd4-b255-5669dcdfa939 | -6.28178 | -43.63733 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f0fc162-5396-3038-af1f-4bca47ac5f97 | -8.23184 | -45.51324 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0fc3370-717f-394b-821d-d7c13f984f32 | -7.4079 | -44.62372 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 414313ec-cf39-3295-b992-07c8ce108375 | -8.2126 | -45.52797 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8a46e2d-66e8-3b84-9261-7c72e5eaa06b | -6.05581 | -43.2232 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 91db46bd-fd40-3e68-ae97-2276321bb1e3 | -5.49622 | -42.74871 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a0da4f48-f945-3f22-b07b-e910ff44f7e4 | -9.85334 | -43.47955 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b921cd3-8aa4-31e1-888e-87f904c08380 | -9.2771 | -45.6846 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ceeecb9e-4a88-3f9a-97a6-6132313b9614 | -7.56397 | -46.77189 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b9ac7d8-edbf-32ff-bfbd-63856f083146 | -7.11279 | -45.07545 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0864e15e-53dd-3ccf-8564-f541998f2744 | -5.83466 | -43.93305 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28c4ffc5-a8ea-3975-8bde-2cc0535f946b | -8.68098 | -40.94734 | 2025-10-01 04:19:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7f301dbf-43ef-38f3-87ad-8eb43c7cff24 | -8.53741 | -44.70966 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d0232df-a35b-33b2-9fa0-033f472cdc1d | -6.98649 | -42.79675 | 2025-10-01 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ce02895e-e0fe-3877-afaa-29a3be22d350 | -5.84835 | -45.75434 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 20a8351a-90fb-3086-b7be-29f442681fd2 | -6.99622 | -42.80205 | 2025-10-01 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 608bf568-3687-3fce-8785-43314066188a | -8.53682 | -44.69174 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 94a6f3da-9540-30dc-acf4-66dfcb866a13 | -8.70122 | -44.83903 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c83890e-e092-35e6-a288-dce10c4c2712 | -8.52078 | -44.6642 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33730e67-b851-3e7f-b43c-3307bb13138e | -5.80049 | -43.07379 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83b1d849-c378-366f-bce2-36937af8e2d9 | -9.93322 | -43.64918 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4ae0908f-73a4-3f84-8bd5-02df870f3628 | -6.26933 | -44.17857 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6528867b-398a-30f7-aadf-4ae9f95830f7 | -5.63872 | -43.902 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc68bed1-bcd0-312a-9990-a5a58aa7ff83 | -5.87887 | -43.55976 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd663403-7cb9-3b26-97ce-a2c24b128d1d | -5.94289 | -45.86748 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a48b9ac-88f6-3bc6-b452-0f4f8a40e492 | -6.07466 | -42.68079 | 2025-10-01 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7cbaa1d-9804-3cc9-8e48-d1e978e55c63 | -5.31933 | -42.77781 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0781c968-5c0e-3768-b6e3-906f2d45fc18 | -6.32396 | -47.22179 | 2025-10-01 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7b09439b-aba7-3f2e-bd4a-e8b4311dadc1 | -5.82201 | -42.86553 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00513f26-55f7-3c71-895d-4920f51ad822 | -7.02443 | -44.46347 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee1eb4da-cba1-344d-b04c-9a3f1abfc1cb | -7.47622 | -47.27239 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 794c6bb8-b6a2-34db-a596-ed73fc535a69 | -4.8177 | -43.27325 | 2025-10-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5973fa05-60b8-301b-870f-08de6cf14a03 | -5.77409 | -43.29013 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9cac311-6aeb-305a-8bf2-2452f19cb9f5 | -3.11676 | -40.83554 | 2025-10-01 04:19:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 264ac879-7447-3e24-99a1-9e502afd763b | -4.25982 | -48.55073 | 2025-10-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a64b2d9-f793-39d2-90f9-356a0171b639 | -8.23514 | -45.51376 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0a5ec315-6389-34df-8c55-3fed72d0f279 | -5.17706 | -44.78909 | 2025-10-01 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c36169e9-8ac7-33d9-a489-fff7884a4662 | -6.53363 | -45.23062 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ba9d1be-c214-3167-884a-6831e2c8bec0 | -5.15715 | -43.71618 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README32.md)
