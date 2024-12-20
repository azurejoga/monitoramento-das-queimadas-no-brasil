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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 952c0c68-3135-3271-b6ec-66671ae27402 | -9.2403 | -60.3292 | 2024-12-20 03:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 1d19397d-7437-3b7e-8c65-8823b1f426e9 | -12.5492 | -57.7594 | 2024-12-20 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| dc3733c6-3944-31f0-a13a-f54b4ce06cce | -9.2215 | -60.3495 | 2024-12-20 03:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 13945947-5d12-33e0-a81f-b5d8200731e8 | -5.22963 | -36.81359 | 2024-12-20 03:23:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dc243982-1443-30eb-be19-28bbce2f1e72 | -6.68247 | -41.03402 | 2024-12-20 03:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b9370dc2-10e2-3539-860e-8f13cce29349 | -4.11872 | -43.55695 | 2024-12-20 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f9b179a-e4c7-3c74-a341-43e043e6ea40 | -4.92689 | -41.33423 | 2024-12-20 03:23:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67f06914-d243-3817-878b-771c95452b71 | -4.92613 | -41.3386 | 2024-12-20 03:23:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 51c3f29a-72f2-3320-97a0-2966f9ca3f2f | -4.93287 | -41.33548 | 2024-12-20 03:23:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9df1287c-41a8-36dd-a46a-f34449a23899 | -4.11982 | -43.55064 | 2024-12-20 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67226233-36f6-3ccb-afad-06db3bd644d2 | -6.39397 | -43.49742 | 2024-12-20 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9a6989c0-4438-35e7-a757-c170cde53a27 | -10.45565 | -37.12532 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d604f524-0b87-3c9e-bdb7-e00a39ade752 | -8.45752 | -40.8272 | 2024-12-20 03:25:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 79a1bbfd-09ce-32e5-b834-f54481a12a91 | -10.15231 | -42.16555 | 2024-12-20 03:25:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| faeb6367-94d6-3fc5-a8a7-119b2c588aed | -10.60961 | -37.00187 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 699002d7-c04b-3ff8-964c-9a455120a1b6 | -8.45818 | -40.82358 | 2024-12-20 03:25:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f5fb969f-fbd6-36eb-871c-1932e3b75e01 | -10.45214 | -37.12086 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fb8b4ab9-0d7a-3516-a1c8-62ff12408a4f | -10.15151 | -42.16975 | 2024-12-20 03:25:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa89d03a-b894-321b-83a7-ca833ac68f77 | -10.08529 | -36.14714 | 2024-12-20 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 8381922e-3f66-3157-b4d1-dd61bc04c8dd | -10.0858 | -36.1443 | 2024-12-20 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9814eff3-c7f9-376a-ab49-3070dbd71608 | -10.48737 | -36.86506 | 2024-12-20 03:25:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b1b1a8d2-419b-3a69-8c0a-743f9cb095cd | -10.61437 | -36.99887 | 2024-12-20 03:25:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8f61db09-9542-3261-9eab-d162d6e6aeec | -10.45629 | -37.12155 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 90a36520-b656-31c0-a2cd-67ca5c32a9c7 | -10.45752 | -37.12528 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5ad10631-b239-366e-ab5c-c2297a4a30eb | -10.08496 | -36.14935 | 2024-12-20 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ff8b005a-eb09-394b-917d-0d78151ed911 | -7.25381 | -44.70894 | 2024-12-20 03:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a8c4aad-7f70-38d1-8b71-37c58f928f63 | -10.1449 | -42.17282 | 2024-12-20 03:25:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81ee3a3c-0a7d-3d30-923f-89497ca082c0 | -10.45149 | -37.12463 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a68fcc5a-0f6e-3eec-9da0-4f5821a34469 | -9.91413 | -37.06297 | 2024-12-20 03:25:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 287e2201-f1a0-340a-82c7-78f2b85a3d04 | -10.61371 | -37.00261 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0d75bfc1-05aa-3af3-801a-b576b6fc934d | -10.49145 | -36.86579 | 2024-12-20 03:25:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 26e939ca-b4cd-3249-920e-3283a3c8db76 | -7.25246 | -44.71592 | 2024-12-20 03:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f60a4388-f265-329e-a847-0b666a441dec | -10.61308 | -37.00623 | 2024-12-20 03:25:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| acc977fa-4313-3ce1-9892-8b3fd73d0e79 | -17.75521 | -42.89733 | 2024-12-20 03:27:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68c874b2-b470-3154-b02e-f6a9fac33184 | -15.30871 | -43.1352 | 2024-12-20 03:27:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e88b148b-3fe7-306e-9fa3-f6b12ef223ec | -19.83919 | -40.08207 | 2024-12-20 03:27:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 56924be3-34db-36c2-8609-c0c2b8dcd340 | -17.74988 | -42.89635 | 2024-12-20 03:27:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1edf10be-abd2-31e8-866f-01a73044c0e7 | -15.30954 | -43.13122 | 2024-12-20 03:27:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a3c164f0-4577-3f33-aa09-1d2d371731dc | -15.30649 | -43.13155 | 2024-12-20 03:27:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f34c18e8-1b5f-3b2f-814e-5f68c7494bba | -12.5682 | -57.7579 | 2024-12-20 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 44447ad4-d035-3b31-8ce8-f9883da33a0f | -12.5492 | -57.7594 | 2024-12-20 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 732f3a1e-3ceb-3da8-8041-ed3eaa823ede | -9.2216 | -60.3302 | 2024-12-20 03:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| fd9abb0e-277d-3b02-b764-1581f08d91c3 | -9.2215 | -60.3495 | 2024-12-20 03:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d3499679-5eb7-35dd-8a29-0760e4a950f4 | -12.5682 | -57.7579 | 2024-12-20 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 769198df-0296-398a-96c7-7dd18f3243fb | -9.2216 | -60.3302 | 2024-12-20 03:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 00c5c7b7-ab1d-3640-b6ee-8aa2ed487e9c | -3.2321 | -46.7836 | 2024-12-20 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f756c39b-322c-3b75-9eb8-5e50471eff6d | -12.5492 | -57.7594 | 2024-12-20 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 20fe5983-8d52-322d-b24d-eafd154698c4 | -3.232 | -46.8056 | 2024-12-20 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b15b8f27-05fc-35e2-abea-974623c1247c | -9.2215 | -60.3495 | 2024-12-20 03:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fd68c634-d605-3b40-99cf-1c1b3ee84d19 | -5.50084 | -39.12866 | 2024-12-20 03:46:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0ce9afe-37d3-339a-9ea8-a3af070fa18c | -3.96697 | -44.05409 | 2024-12-20 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f60292c-6830-39ea-9d84-1d4c7ab622c1 | -4.92895 | -41.32515 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6521f2df-5c57-3c3a-b553-482c3bb75a54 | -4.15282 | -43.72483 | 2024-12-20 03:46:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 377b2af0-9d15-3263-ba7b-0169686e8c22 | -4.93126 | -41.33616 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2fa5d3ba-69b2-351f-9b08-aa3c8175458d | -6.38974 | -43.49688 | 2024-12-20 03:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f2d5670-3158-3483-b592-d11cce015c28 | -6.38901 | -43.50123 | 2024-12-20 03:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da63535f-5869-37f2-969f-cdca79fca4e6 | -6.0383 | -44.03995 | 2024-12-20 03:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cbe15d3b-66c7-3992-a916-27dc62adb20a | -4.91385 | -41.3173 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67e330dd-e634-30cb-95a2-be164746db4c | -5.39092 | -40.66944 | 2024-12-20 03:46:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4cd0d672-c34a-3175-8804-998c9093068c | -5.52343 | -42.85004 | 2024-12-20 03:46:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce6d5d53-f835-3e7b-bce0-82d66be1dec6 | -4.91783 | -41.318 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b34c391-ccd8-34aa-af01-9421b25246ac | -5.96538 | -44.28945 | 2024-12-20 03:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2901470d-ee95-39e8-b915-d662155fb418 | -5.96592 | -44.29235 | 2024-12-20 03:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 432f9da6-7a07-3a93-919b-14d190da462a | -4.85728 | -41.35283 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc725453-337c-3454-8933-12f79a76d61f | -5.29843 | -41.97468 | 2024-12-20 03:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a5f072a5-5fdb-3038-84aa-24e821a5b6dd | -5.22678 | -36.81403 | 2024-12-20 03:46:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d43e192c-2ccf-3c67-ae19-2e984468fc0d | -4.67428 | -43.30156 | 2024-12-20 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70514377-322a-3514-a646-250bb6f4941b | -8.23285 | -39.03393 | 2024-12-20 03:46:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1e006d65-223b-3256-97dd-782b500f32b0 | -4.85929 | -41.3493 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10970266-0cfb-340f-b16f-18408873b962 | -6.30599 | -39.87521 | 2024-12-20 03:46:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8768f447-959a-3647-b3f0-b0dd1af774ae | -4.92644 | -41.34054 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ef3f6dbb-89c9-3985-83a9-f1ffe1893fc3 | -4.38501 | -42.14562 | 2024-12-20 03:46:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e398c5b-7f54-35d4-9b5d-a549bfedb143 | -7.1449 | -40.10891 | 2024-12-20 03:46:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df7270a6-253d-3990-8251-a5a7b1d70972 | -5.9848 | -41.60598 | 2024-12-20 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b8d52ac4-d787-3f92-a024-043a7bf52ab2 | -4.15368 | -43.71979 | 2024-12-20 03:46:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c38739-85a8-3846-b8ea-9ac19cba7994 | -4.1227 | -43.55283 | 2024-12-20 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3bdff25-1da7-37d7-ad7d-ca188ba41d9a | -7.14649 | -40.21214 | 2024-12-20 03:46:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f2f2b2c-64c0-35f1-bbb1-666d2e4fcc23 | -4.38926 | -42.14633 | 2024-12-20 03:46:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 94c6a007-23ee-3146-a4a0-e8df85164b4d | -4.1172 | -43.5569 | 2024-12-20 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c22540ad-0df0-3945-905f-0b6d15c432e7 | -6.17251 | -39.75055 | 2024-12-20 03:46:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f087a567-414d-3b92-bfaf-f6a42fa317e7 | -4.92496 | -41.32449 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63375160-b7b0-3d74-8ce7-e0937b89969b | -5.96445 | -44.29475 | 2024-12-20 03:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b32f4c25-9aea-3553-9e68-5be52175930e | -5.96111 | -44.29159 | 2024-12-20 03:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b73bbccc-e35a-36be-84c9-f25418da6244 | -4.93042 | -41.34135 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c83f8a8c-3d0b-34d2-b868-caf50bd1339c | -4.92811 | -41.33031 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f4a815bc-c5b5-3d52-aec2-17fef0d06f65 | -5.98398 | -41.6044 | 2024-12-20 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 783914ba-053c-3448-b921-787ffeed5838 | -4.1133 | -43.55129 | 2024-12-20 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 988d3b81-48dd-3610-bfae-b260fddc616c | -5.09049 | -44.71502 | 2024-12-20 03:46:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edca97df-fb02-3c52-b80c-d4966a1a8813 | -4.92728 | -41.33544 | 2024-12-20 03:46:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b2d644a5-5bce-3200-9f29-ea74de58c302 | -5.39017 | -40.6741 | 2024-12-20 03:46:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5604beb7-e650-3514-a663-5ea6922a4a28 | -6.04303 | -44.04061 | 2024-12-20 03:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45fa1a52-28a1-3614-8070-732ca4b25ee2 | -4.388 | -42.1458 | 2024-12-20 03:46:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0944a02f-efa7-3a8d-b6e2-1eec344998ff | -5.11328 | -43.2 | 2024-12-20 03:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35bd7e56-c02d-34d8-8737-6ca5660816f9 | -4.00235 | -46.54994 | 2024-12-20 03:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 76b4a3ee-b761-302e-b1b9-51a923d9c911 | -4.24823 | -41.92371 | 2024-12-20 03:46:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1124ac23-264d-38af-89ce-8ce869046720 | -3.96917 | -44.05619 | 2024-12-20 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9f86a04-6225-3b24-87c3-4c4a99d6493f | -5.38943 | -40.6716 | 2024-12-20 03:46:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 292c07f2-0283-31fd-ba2d-d0bab5a440b8 | -6.1167 | -43.94827 | 2024-12-20 03:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecc98bcd-a75d-386e-8bed-c2a926ac0689 | -4.67884 | -43.30242 | 2024-12-20 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8c4d358-9e8b-3084-a242-a164ed9dd600 | -4.05415 | -38.79189 | 2024-12-20 03:49:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
