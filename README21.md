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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eea80349-df09-3a54-9a0e-5f11edb3fc20 | -6.24712 | -51.66943 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf720afc-9735-396a-bd93-f0b3346d8ea9 | -6.79735 | -58.95102 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30623e47-b997-3252-a2dc-640e12b4555b | -17.09499 | -56.87391 | 2026-09-09 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b5bee0e8-173a-3308-8f15-5c58a01c2ad2 | -8.09734 | -45.67206 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f40e467a-3f63-34c1-8ee9-332c4e96bb57 | -5.79894 | -53.81585 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a3b9e2f-db8b-331e-aef0-0abf7c7cc693 | -9.70067 | -43.46809 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f8387817-7e1f-3573-85d5-03955543f370 | -11.39559 | -43.9218 | 2026-09-09 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbc95400-ead3-3b4d-9c5d-74acc2fac325 | -5.85027 | -51.95042 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb79d1bd-f970-35c8-986d-a49e82870353 | -9.7003 | -43.43717 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e27141ea-60e6-38d0-a3cc-98892d4e07c2 | -10.74703 | -45.96969 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 235d008d-37d2-3646-9aea-d97bccf83d11 | -9.71332 | -43.47716 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82520944-3d44-34a9-9690-9d5459d60ff3 | -9.71377 | -43.47465 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26728710-6b09-3be9-85c4-f905442d5905 | -10.71877 | -46.05549 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19eaa3b0-f793-3412-b13c-d9cb4c7150f5 | -8.74058 | -62.41268 | 2026-09-09 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2ee3aff-28e1-3808-96a6-833bfe8caf8b | -10.36404 | -45.17082 | 2026-09-09 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| facb10bf-0376-381c-9a29-d3618a018a07 | -14.28492 | -44.589 | 2026-09-09 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78c025e1-e2de-3d29-afb3-094f4a572214 | -10.24952 | -45.21947 | 2026-09-09 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99499674-5ba5-32be-9a40-ade3a2357d86 | -14.28186 | -44.5859 | 2026-09-09 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed5de65f-09fd-3205-ace8-ca192110b4d6 | -5.80662 | -53.8172 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb9bcdee-8144-31e0-9e60-207493593966 | -9.69108 | -43.50501 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ab980a5-ebad-30e9-a5ad-d8138e81c012 | -6.86579 | -46.01306 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29c83b13-4f05-3fc1-ae22-7de4fee6ccd1 | -10.94275 | -48.31504 | 2026-09-09 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29beecc3-fbb9-3613-98ab-12a82515b010 | -5.80278 | -53.81654 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c35ed5bf-97f5-337a-9750-eb8039ec1f8f | -5.13628 | -55.9622 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5eee033-2145-39d1-ab92-769524531d8b | -5.84266 | -52.04097 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b629df1-9420-3601-88f9-f560996dfbb4 | -5.37054 | -56.03442 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2480cf6b-d7a9-3449-b145-5976ddb1d7d7 | -10.71949 | -46.05052 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 538b9dcb-1802-320c-b664-63c223273e68 | -9.70366 | -43.41058 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 590ef0b6-13e8-3591-94c9-9f85f6c16124 | -6.86885 | -46.01811 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10c2fccf-941d-35b2-a99d-8390d4307fb8 | -6.90013 | -51.16303 | 2026-09-09 04:46:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 710e9dff-bfb0-3290-9a7a-2de91f370436 | -9.08838 | -47.82118 | 2026-09-09 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24a19e0e-142e-31c0-91a0-36ada5911960 | -6.39043 | -55.24812 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8e26d0c-3dc9-31ac-b672-4e3bb5f1401f | -8.98476 | -60.58835 | 2026-09-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1813df4f-f65c-3c9a-ac4b-a25119a4612b | -7.0835 | -59.82219 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b55ac3c4-37c3-33a7-840b-eb48b70088cb | -5.82208 | -53.79517 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 056c8f24-10d8-349d-949d-71ee5d1e46ec | -9.69495 | -43.5081 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d83a4132-2d4d-35ca-8ee6-6c0e67d236ce | -10.58622 | -45.74886 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9da09a5a-31f1-3de7-b764-92aba5acb388 | -10.64989 | -58.76546 | 2026-09-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d43effc9-1513-3672-9148-54325e67ed02 | -8.09091 | -45.67893 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c3ea721-07f8-3554-9c96-91211d3b957b | -10.26999 | -45.22258 | 2026-09-09 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de489f8b-ad97-30ab-96b7-b859724f0e54 | -14.28944 | -44.58971 | 2026-09-09 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71170245-9f96-387a-b3f4-545a5d18a3e9 | -9.77588 | -43.46412 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53422a08-cd9c-330d-a3c6-14a2c1766136 | -9.69942 | -43.47741 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1979b567-4d7f-369d-ab8b-5ce4c31d36eb | -9.70826 | -43.41125 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bc03b5d0-04ae-3ca9-9805-e98476f30723 | -7.56722 | -48.36283 | 2026-09-09 04:46:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a68bc50d-1001-31eb-8e47-f76347ac4fe0 | -6.86008 | -46.01402 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93966ef5-1119-3abe-a38a-54ea0c70f386 | -7.37367 | -47.01658 | 2026-09-09 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb19e584-9b42-31be-bbe5-cceb1c67c370 | -5.38177 | -54.44757 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89f7ac0b-62ff-3f3e-9fbf-6c83ca757672 | -8.98657 | -60.58646 | 2026-09-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 150249ee-4fa5-3086-8c1e-23b1e48eb725 | -5.88158 | -55.71409 | 2026-09-09 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7927e13c-8b77-3f96-866c-0b1faf3492b2 | -9.74586 | -43.51273 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de1ca5a4-1b1f-33d4-9c46-4f3e00bd6c8e | -8.61175 | -47.36055 | 2026-09-09 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6150d5b1-49a6-33b0-bbb8-4ce45c52ba9e | -9.69893 | -43.47996 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77f001c6-6078-3517-9d8c-2f4bf925c9ad | -7.68569 | -44.31519 | 2026-09-09 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e23c4d45-4c16-3dce-84c1-59bce38fcde9 | -7.68458 | -44.32288 | 2026-09-09 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 272a5f2c-515d-3d68-90d9-9c7029c4a975 | -6.82668 | -55.28553 | 2026-09-09 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1e237a5-2631-365d-99cc-255264322406 | -9.69984 | -43.43929 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c0165fe8-4471-316f-a5b1-1e8d16d444e7 | -12.35117 | -48.20006 | 2026-09-09 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f9e3ae3-d4a8-3ceb-b08e-bb739d1f60c1 | -7.2622 | -45.35414 | 2026-09-09 04:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ec9382e9-9369-3f26-aa1a-2734790b438c | -5.36653 | -56.01757 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6499dc6-91aa-3391-8629-760d31873040 | -10.74368 | -45.96684 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5736e97-23da-3a54-81a2-83ac047e3e70 | -8.72721 | -62.4093 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1bc7725-5b0b-3091-8614-e32feb89cd87 | -5.58859 | -60.24522 | 2026-09-09 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97e1542a-31f4-3dad-b234-ce77166de342 | -9.69959 | -43.47528 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c4e5a942-8bf4-383c-9f2a-ac9abff3bd95 | -8.41867 | -46.89421 | 2026-09-09 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e52665b9-ce82-3324-8611-88b26e3b10d6 | -5.82286 | -53.79039 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f41c6c85-4bc4-3077-a697-2f457131d159 | -5.31045 | -56.10497 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9240a07d-7d30-305c-a0f7-8dad8f481663 | -5.3713 | -56.02997 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f241dad-e10b-3bc1-a579-60d20249cf4a | -15.99846 | -56.42092 | 2026-09-09 04:46:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 09fda420-166d-305a-ab13-f9c801dc1c1a | -9.70098 | -43.43233 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f9154356-2174-358b-82c4-2875f9c7d355 | -6.78533 | -58.9383 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dfaafe5-7600-35a8-95f9-64ab62793070 | -9.7252 | -43.38967 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dc3a78b8-0264-33d0-b1a4-67e14939ef1b | -9.69961 | -43.44206 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 572d3d78-f0e1-3b21-9a4e-0a81e49b5d8c | -12.95713 | -48.61597 | 2026-09-09 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f68e098a-5488-37ba-87cd-9bedf6a8798c | -9.7009 | -43.46601 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ed0bbe0e-b929-386e-8b40-728efe08b77a | -17.59527 | -44.66705 | 2026-09-09 04:46:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb680142-31f7-3289-8dd5-441367f74f32 | -6.75876 | -58.96422 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f1595c9-e660-3b05-be9f-fee56dd9337f | -7.19228 | -43.61896 | 2026-09-09 04:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c4e0265-f8b4-3530-8549-e3e467a99dd8 | -7.08673 | -59.8218 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1c97a88-1060-31c9-ad6b-01ea58ef8912 | -9.77914 | -43.4743 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36f57641-feb8-3a18-bd3d-868731269faf | -6.55351 | -62.90121 | 2026-09-09 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7119583-9ef1-31b4-ac79-7cb28631240c | -9.70282 | -43.45246 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8e69e52c-62cb-31b5-beab-e83b3b7689eb | -6.86953 | -46.01354 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f926e61c-3085-35e9-bab8-4e38297ecc7a | -7.68514 | -44.31903 | 2026-09-09 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffd315c6-44f7-39ee-8615-82c659c06058 | -9.26043 | -45.65348 | 2026-09-09 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74bdbc09-e787-37b5-8a88-ad17969a02e3 | -8.72518 | -62.41997 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f93fe414-b473-38fe-a28c-6034cffd4936 | -6.39107 | -55.24437 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed32dbdf-fe3a-3722-a7a4-bc468edebc66 | -6.55469 | -62.89493 | 2026-09-09 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6c6ac25-663b-36e3-b3a9-7cd8640481f2 | -8.09208 | -45.68123 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43ab0d8b-55e1-3642-a316-a3f5a553a925 | -9.71315 | -43.47931 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92c5a019-f5db-36aa-9ae4-bddfc0e56c3f | -6.87258 | -46.01862 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ec580c7-d16f-3db9-9371-f912175c76c7 | -10.27217 | -47.4897 | 2026-09-09 04:46:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba4e367a-7a7a-3203-ba1c-50d5ae482732 | -9.77662 | -47.05632 | 2026-09-09 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e60d616d-a083-30a1-b679-994fc5857d24 | -11.53618 | -44.89378 | 2026-09-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e83cc7b7-6249-3b03-a8e1-bab27c88fba5 | -6.24246 | -51.67638 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5ea431c-9fd4-3411-9404-c0214c233ef2 | -9.25649 | -45.65302 | 2026-09-09 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23afb7b2-85d3-35ec-b6a4-0b4336e37ed0 | -6.76467 | -58.96194 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25cb696a-224a-37b5-848c-4e0e095361d1 | -13.4079 | -44.16236 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fecc5b3-fbf2-3c07-9753-a6932db71b4a | -6.63458 | -59.44048 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34516db1-5214-3fd0-92f9-1984065a588a | -6.6677 | -50.91299 | 2026-09-09 04:46:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
