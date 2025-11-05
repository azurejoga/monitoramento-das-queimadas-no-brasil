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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a0520ab-bcb3-3b02-87b6-d324efaf1551 | -6.0962 | -41.70144 | 2025-11-05 03:21:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c088695d-5078-35a4-bdfb-df0cd80cf492 | -4.54115 | -40.64164 | 2025-11-05 03:21:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c7002a0d-6603-35a1-ab9d-b6997dc5fc7c | -8.39293 | -38.79965 | 2025-11-05 03:21:00 | NOAA-21 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f3ffbac6-ee97-3ae6-8e00-855762b4150b | -4.57504 | -43.33998 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ded81c35-b295-345f-ad2e-e407b886e1be | -6.26969 | -42.57248 | 2025-11-05 03:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 832829a6-36a5-3d36-bedd-f745fa4b4023 | -5.69715 | -35.33468 | 2025-11-05 03:21:00 | NOAA-21 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2785fe14-baf1-316d-9bf4-e5082187aa80 | -7.1584 | -40.10442 | 2025-11-05 03:21:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 12bc64eb-1119-3e70-befe-13668077be95 | -5.92343 | -41.29291 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2066f459-b360-3c87-a0a5-79e50ac2a250 | -6.07794 | -43.25224 | 2025-11-05 03:21:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f88a68ff-79a3-336b-8860-39fa2606f563 | -5.77985 | -40.81116 | 2025-11-05 03:21:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 916f599a-e7a7-3021-891e-bca2b5c46292 | -4.46635 | -43.2319 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f4b1d800-d066-300d-9bdf-90742796d2e9 | -5.15254 | -41.21468 | 2025-11-05 03:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bf2eca23-4e95-3790-b69f-22e6eb6b07be | -5.92941 | -41.29432 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b178ff63-6dea-3490-9b3a-2d186578f061 | -5.03653 | -43.61637 | 2025-11-05 03:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 342b723a-b3c9-3163-b137-b7a12d84e513 | -5.03527 | -43.62332 | 2025-11-05 03:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0b32f167-af74-3631-b131-5abbedb00387 | -5.0282 | -43.62225 | 2025-11-05 03:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3fa5fa65-47fc-3ae8-a743-285d096ad74f | -8.67577 | -36.68873 | 2025-11-05 03:21:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f88b0674-920f-350f-b198-c802ce46335e | -5.52019 | -41.14467 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d2448bfb-0534-3c05-b3b1-9ea92166a626 | -4.46174 | -43.21768 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| fd55b7f4-f500-3954-83af-f387d2e36d58 | -6.12699 | -41.63117 | 2025-11-05 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6ddb3b01-5629-3a11-b083-0a59c1c3d8e7 | -7.16392 | -40.10524 | 2025-11-05 03:21:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 18b8d00a-daf5-3130-b8ae-120df6381e27 | -5.46877 | -43.58528 | 2025-11-05 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 08034677-45a8-31c3-bed5-b8be731bca48 | -7.33178 | -38.85257 | 2025-11-05 03:21:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 19665673-e79f-3c65-ad79-63f63f8d9719 | -4.47446 | -43.22659 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cea802f9-153b-3b8f-81fa-433fdaa04aa8 | -4.45362 | -43.22305 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 6f8aa199-5353-364f-ba5a-64f6f8e5fb2a | -7.36051 | -35.26753 | 2025-11-05 03:21:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ea5f5ed3-b314-3d35-9410-698af4d4a9c0 | -5.51826 | -41.14597 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fcda4b0a-1911-384b-9ece-5538bd986c01 | -4.54345 | -40.64346 | 2025-11-05 03:21:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 70ec40ae-1ff8-3e95-b22c-356565198f98 | -6.52139 | -39.68944 | 2025-11-05 03:21:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4388c47c-6c77-309b-ae0b-2752a6b1fc14 | -11.62761 | -41.47064 | 2025-11-05 03:23:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c35a2f68-caa2-3fc0-8a02-3bfca3c8ab88 | -9.98137 | -36.31638 | 2025-11-05 03:23:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 24571f5c-336b-3f81-ab07-185f731dc4db | -12.02142 | -45.69044 | 2025-11-05 03:23:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a7a6f79-9869-366c-a0f3-f7e19c208c2b | -8.93295 | -40.87222 | 2025-11-05 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 358df3ed-13bb-3035-b92c-e0e08e7f4926 | -8.93854 | -40.87332 | 2025-11-05 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9a234578-d42c-3d6f-aa38-ab1a8503550a | -11.84974 | -43.72523 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b168287d-f90c-342c-91e8-1c7e98e4f68e | -8.93479 | -40.8732 | 2025-11-05 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d7649017-0d97-38fe-919e-8509948ae9b1 | -11.62708 | -41.46816 | 2025-11-05 03:23:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8872144c-0860-3435-b56d-4617d1bdf208 | -11.84351 | -43.73388 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a6ba4ac4-2603-355e-b40c-b253e958c4db | -9.98611 | -36.31327 | 2025-11-05 03:23:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5eb0b64e-79dc-3b7d-bf97-b6c4c40913eb | -11.01783 | -42.73161 | 2025-11-05 03:23:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8d27b83a-ed4e-33d9-b1bc-cf9003df0d4d | -9.9848 | -36.32072 | 2025-11-05 03:23:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 25b64402-88fc-3cc1-b05a-1dc7816d96d4 | -11.01178 | -42.73036 | 2025-11-05 03:23:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ef19c496-ab1b-3edf-9ca9-1a2eb77e8c80 | -11.85205 | -43.72457 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d976e70-3429-3f53-aaf8-f94fb4771ec2 | -11.62833 | -41.46688 | 2025-11-05 03:23:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1fae1f8c-4641-3a51-9def-73121c58fd98 | -11.84234 | -43.72922 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f494f7f-65b6-31d5-bfb2-545d83b4bb60 | -11.43405 | -43.95506 | 2025-11-05 03:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02335ae5-d5af-3762-ad54-a824eb74c4b7 | -11.43407 | -43.95395 | 2025-11-05 03:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74e302d2-09ec-32ac-b92e-c97366c78d0d | -11.01085 | -42.73508 | 2025-11-05 03:23:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cfe64564-eaf9-3734-9c7d-a95f1ebb782f | -11.84339 | -43.72393 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16984c39-3509-3657-9e36-960edd7c3861 | -11.84128 | -43.73455 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b55a8c2b-8f82-3ff0-a5c8-ff917bed782b | -11.84461 | -43.72857 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58d0091c-351f-3436-a110-0a85eb3d4782 | -10.50465 | -42.4038 | 2025-11-05 03:23:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d27a53d9-b9e5-3972-ad7a-77f1891aee13 | -8.93548 | -40.86937 | 2025-11-05 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fe23d6ea-fa57-33a3-91aa-cdc614d58549 | -11.8457 | -43.72329 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64a223f3-b1a6-3da6-9994-751307b7601b | -9.98203 | -36.31265 | 2025-11-05 03:23:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 485dd18e-b8fa-3cdc-bfd5-deb91935ddc0 | -11.84763 | -43.73587 | 2025-11-05 03:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4a6834a-9262-362b-9c8b-7bed306f54e2 | -9.98072 | -36.3201 | 2025-11-05 03:23:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b5d7bb49-cf84-38dd-b851-dc948ccc2834 | -9.98546 | -36.31697 | 2025-11-05 03:23:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 860391e5-f482-34f8-84d1-b0bd6ea391cf | -16.61418 | -41.85427 | 2025-11-05 03:25:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 43f0f0a2-2572-3871-aa28-1607b525c247 | -17.98601 | -43.43806 | 2025-11-05 03:25:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cd81e3f-2600-3060-98d4-f759dc5bfcae | -16.61475 | -41.85144 | 2025-11-05 03:25:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c9f61802-110c-33fa-aa63-2c2b1d556d6a | -16.81194 | -41.00345 | 2025-11-05 03:25:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bcd2a37c-6db6-38a0-83a2-a5e2eec6df16 | -16.61532 | -41.84863 | 2025-11-05 03:25:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 82150ef3-1992-3a31-b849-8ee9a5b6e9aa | -16.81541 | -41.00259 | 2025-11-05 03:25:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b6035c10-bd83-3d93-b443-e6498c4fd0a9 | -4.4259 | -48.9465 | 2025-11-05 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| eedc1542-0e03-3fb4-be49-5551f5614526 | -5.4707 | -43.5674 | 2025-11-05 03:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b64ffc13-111d-3a67-8a16-4363d34c32ee | -2.6508 | -48.52 | 2025-11-05 03:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 54ca4c10-96ad-316f-80a1-b74be57b5044 | -3.4899 | -43.6383 | 2025-11-05 03:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 517388a1-5b12-3019-aa0a-012f5fb81550 | -4.4072 | -48.9688 | 2025-11-05 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 04411dc7-fc27-3987-8c9d-0c717a300129 | -4.4632 | -43.2386 | 2025-11-05 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 912236a7-0ad1-37bf-ba43-0aaf370a9d65 | -5.0399 | -43.6205 | 2025-11-05 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 48751d57-6a76-3792-b4dc-f958cb654d8c | -4.4073 | -48.9474 | 2025-11-05 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 4393b1d6-ab8e-38b4-96e3-d35459f50cda | -5.4705 | -43.5906 | 2025-11-05 03:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6dafa4dc-e621-3dbc-ab25-ff264109b287 | -4.426 | -48.9251 | 2025-11-05 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 4e77885c-b211-36d4-9e5a-7969dede9f34 | -4.4075 | -48.926 | 2025-11-05 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 7c196473-5997-375d-988f-bd9273fbb1e0 | -4.4633 | -43.2152 | 2025-11-05 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 86913f10-d669-3781-a9d0-2c40bd553215 | -5.4553 | -45.3988 | 2025-11-05 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| b92f46c7-7b63-3249-be95-f1c05d86b8b0 | -4.4446 | -43.2164 | 2025-11-05 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| dc995908-51f7-38da-bce2-c1ad5196f864 | -4.4632 | -43.2386 | 2025-11-05 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b7d8f2d0-9b8a-3374-89f1-6a2b5224f4a2 | -5.4705 | -43.5906 | 2025-11-05 03:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 951968eb-56eb-34c8-bc4e-f0377afe9ccf | -4.4073 | -48.9474 | 2025-11-05 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 356035f2-8cf7-39ee-9b7a-2e74ce0b0ec8 | -5.4553 | -45.3988 | 2025-11-05 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1043600e-a031-30ab-8e7f-9b2e6607222a | -2.6508 | -48.52 | 2025-11-05 03:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| fbaf54b3-0a43-34cb-8b94-499e5b94e4bc | -4.4633 | -43.2152 | 2025-11-05 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 5c1943e3-e5a7-3634-a3c7-1a5ef11d64ff | -4.4259 | -48.9465 | 2025-11-05 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| cda3389e-6d6c-3508-813f-4153226c6015 | -4.4075 | -48.926 | 2025-11-05 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 62b0325d-78fb-3ee4-8c8c-66ad7f879e58 | -2.6509 | -48.4985 | 2025-11-05 03:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| d1c219e9-bca4-3aa4-9d09-a0573dff28ab | -5.4707 | -43.5674 | 2025-11-05 03:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a70c404a-e431-3288-9520-c27b8d7fde51 | -4.4446 | -43.2164 | 2025-11-05 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 47c430c3-c7f6-396f-a884-3b16e95c6344 | -5.0399 | -43.6205 | 2025-11-05 03:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8f966d83-e2f5-3e90-87a0-9243c2245a5d | -1.28635 | -49.15389 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d2fd035b-45ab-3219-a85a-689b729e9d7d | -1.29739 | -49.15446 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2aee2e5-e691-3c6f-8331-f9f0377d12f5 | -1.29624 | -49.16119 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 159869b1-f5ac-380d-8e19-aedfa71b6fbb | -1.25816 | -49.14903 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9859fb1-0fb7-38e2-80d8-c88afd0c550e | -1.2833 | -49.15206 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f58eac2e-4d4e-310d-9eeb-5e5282b6220d | -1.29035 | -49.15325 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9dafe249-9462-3347-970a-017c5becc5b5 | -1.30044 | -49.15635 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af23e19e-b816-3188-a408-edd50fbd444a | -1.25928 | -49.14229 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12366efb-2393-3ea7-8455-c0ed39d3b85b | -1.30329 | -49.16239 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a0b049f-8afb-3461-8dc2-cfc32c4b7ddf | -1.27226 | -49.15144 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README9.md)
