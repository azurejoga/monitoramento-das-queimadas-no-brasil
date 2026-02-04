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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ff425fe-398a-3fac-9455-ca07011a7f6c | -7.1909 | -35.0541 | 2026-02-04 00:00:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| a4931631-5b71-3aec-aa29-062271a2ec29 | -15.26094 | -39.28136 | 2026-02-04 00:07:00 | TERRA_M-M | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 053dd70e-9693-379f-aeef-51f263930126 | -13.36465 | -39.90965 | 2026-02-04 00:07:00 | TERRA_M-M | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 6b6c8098-d0eb-3306-a108-e56427b60f2c | -8.88253 | -35.41485 | 2026-02-04 00:09:00 | TERRA_M-M | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.1 |
| 36956285-e9f3-36f7-a555-71ba4d8aef39 | -5.90793 | -43.84717 | 2026-02-04 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 49ea372f-6564-3fe5-aa1e-e13489188676 | -5.93882 | -39.68489 | 2026-02-04 00:09:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 45.5 |
| d9094585-96c3-3c4e-93a2-2ed3fe9b0079 | -10.80191 | -44.4867 | 2026-02-04 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a87545bc-c8f1-3a22-8783-6186f7c50463 | -5.47145 | -39.12065 | 2026-02-04 00:09:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 4d582058-ded7-3984-9871-763c75b2d322 | -9.06724 | -35.59363 | 2026-02-04 00:09:00 | TERRA_M-M | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 45a463a3-1b35-37b1-9974-5056710520c9 | -5.90936 | -43.85718 | 2026-02-04 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1caa7d20-f54c-3319-9339-b82ce04cc346 | -5.87055 | -50.15332 | 2026-02-04 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5447426f-34b3-3c5b-b1b0-ba4b00a5ab04 | -9.28993 | -35.42717 | 2026-02-04 00:09:00 | TERRA_M-M | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 3a8c59ba-67e5-38f8-81a0-dd881d46dbd4 | -8.88632 | -35.40928 | 2026-02-04 00:09:00 | TERRA_M-M | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.4 |
| ded1f58f-7a90-3cf3-8aa7-b90ded628309 | -5.88112 | -50.15149 | 2026-02-04 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a4dff951-e654-3084-8edf-60e7c9e82d13 | -5.94181 | -39.70454 | 2026-02-04 00:09:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 26b18a3d-a0a8-3349-a4bf-a9acda9528a4 | -6.87072 | -35.27704 | 2026-02-04 00:09:00 | TERRA_M-M | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 9e457369-4290-3c01-8b50-147f59de12e4 | -9.28547 | -35.43296 | 2026-02-04 00:09:00 | TERRA_M-M | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| c9b0ed63-0e91-3a36-905c-00347a39acf0 | -4.12083 | -47.3646 | 2026-02-04 00:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f0bad904-3e81-322a-958c-eaecdf33b513 | -9.9487 | -36.3377 | 2026-02-04 00:40:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| f687cb6d-ac97-3f3a-b61f-2aaf8a674775 | -8.23992 | -35.35428 | 2026-02-04 03:17:00 | NOAA-21 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 54f19bc1-7756-3355-86e0-f59206e5dfb9 | -7.97611 | -34.96444 | 2026-02-04 03:17:00 | NOAA-21 | CAMARAGIBE | PERNAMBUCO | Brasil | 2603454 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b2092d3-6cb1-3467-ae41-af561f850103 | -6.43781 | -35.46147 | 2026-02-04 03:17:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c0fd83e-5089-390a-93e7-4af7ce332fd6 | -6.44222 | -35.46223 | 2026-02-04 03:17:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d747df5e-bdda-3412-987e-895b9742776e | -8.70318 | -35.11518 | 2026-02-04 03:17:00 | NOAA-21 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e7478d93-17c9-3f47-a29d-223f53b6366d | -7.70521 | -35.30202 | 2026-02-04 03:17:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ece4d1f8-823d-326c-94d5-10e3f8ef83e8 | -9.47449 | -35.91375 | 2026-02-04 03:17:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73390b94-eae8-353b-a901-9f9e55826d1c | -9.49922 | -35.59357 | 2026-02-04 03:17:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| eccfee37-62f0-3c64-9f43-a390101e97e4 | -8.70668 | -35.11974 | 2026-02-04 03:17:00 | NOAA-21 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7b7eb742-588d-3bec-bb32-78914276f9c4 | -8.84135 | -35.70015 | 2026-02-04 03:17:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 79162fcb-a1db-3a99-8ef3-ac099deff698 | -5.93836 | -39.69091 | 2026-02-04 03:17:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 86fdd038-7afe-35fd-8c5a-8bb84a11b69a | -5.93243 | -39.68998 | 2026-02-04 03:17:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d9597e0f-f31a-3b7f-97a0-c88624a561ce | -5.27373 | -35.97024 | 2026-02-04 03:19:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8b46209e-2959-3d6c-afed-4f099bc13862 | -10.6463 | -37.12265 | 2026-02-04 03:19:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e5e670f9-1d22-3dd8-8abc-b3868c15e1b8 | -5.11873 | -39.0857 | 2026-02-04 03:19:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bc10ddf2-e59c-3e4c-944f-331e8567b1f8 | -10.65004 | -37.12828 | 2026-02-04 03:19:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b8ca5a2-11e3-334c-9c5e-58103f94e0da | -10.65463 | -37.12918 | 2026-02-04 03:19:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7cdb2fce-66bb-3cba-808d-2d20077c961f | -15.25717 | -39.27496 | 2026-02-04 03:19:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1fc3f61c-7ecf-37d0-9e09-6b26dad503db | -10.3246 | -36.77884 | 2026-02-04 03:19:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a45930d3-2c40-347e-82f3-92824ddfeb93 | -10.32179 | -36.77612 | 2026-02-04 03:19:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d4bd0202-3047-303a-9334-0e0f1aeb0ba5 | -10.32007 | -36.77803 | 2026-02-04 03:19:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c62d43a5-f85f-3acd-bda5-2552a063b32b | -10.52745 | -36.96994 | 2026-02-04 03:19:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f6a544ce-fe79-3e85-a3a1-96d89315235d | -9.49946 | -35.59534 | 2026-02-04 03:49:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 591e8d1b-e4c9-33d3-93b7-aff4b70a70d7 | -5.70519 | -39.13132 | 2026-02-04 03:49:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7ea16d8-d448-3cf1-9f36-d9393fd06f2d | -5.17746 | -36.89745 | 2026-02-04 03:49:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f46620c-e5d2-3f42-9d1f-c9e7cca78635 | -5.93731 | -39.69051 | 2026-02-04 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 712d6d2b-34e8-3fb1-9531-4f0ee9869663 | -3.43705 | -39.02206 | 2026-02-04 03:49:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82c496b6-6973-30a1-8f3c-c03761d0597a | -4.23651 | -40.39127 | 2026-02-04 03:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 845ffa07-e1cc-3cda-bc2d-b606033d68ee | -8.84356 | -35.70241 | 2026-02-04 03:49:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f582f95a-b974-3184-a9c5-d56712d18d10 | -5.12029 | -39.08914 | 2026-02-04 03:49:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0369c095-7198-3178-8421-6095d6ab8ae9 | -5.93339 | -39.68987 | 2026-02-04 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fe79aa55-0336-3ce4-a581-fba700546877 | -3.49115 | -43.64177 | 2026-02-04 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd190140-f217-37e5-b6b1-d77c6ed4bf76 | -7.7022 | -35.30287 | 2026-02-04 03:49:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d3f2b97-1ba3-30d5-a20f-7afe79730ddd | -8.7055 | -35.11636 | 2026-02-04 03:49:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66299ee7-aeb7-31c4-97d1-f2dc337723cc | -3.65154 | -43.52347 | 2026-02-04 03:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a1a8df9-bb8d-342f-90d8-9c033671dbb1 | -5.47032 | -39.12522 | 2026-02-04 03:49:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb6dcf9b-e0f3-35f3-bb51-0045171010b2 | -3.6521 | -43.5202 | 2026-02-04 03:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f77613a6-13b2-3fca-9c4b-1c03116b7383 | -5.22028 | -37.32238 | 2026-02-04 03:49:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e952324-d5c7-3aa0-9de3-8371899257fd | -7.70553 | -35.3034 | 2026-02-04 03:49:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1f7a3cb0-bd41-3b1b-96c6-9dfc404eb2b1 | -6.39777 | -39.83471 | 2026-02-04 03:49:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3ff537dd-a0f8-3694-a294-163f9188d05d | -5.11725 | -39.08383 | 2026-02-04 03:49:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1efe1706-0099-3e14-89cd-1b132458285e | -5.27274 | -35.97215 | 2026-02-04 03:49:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 013c292b-85d4-3a66-b519-bf3dd71b7ec8 | -3.48853 | -43.6385 | 2026-02-04 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30ebc40b-d712-3b95-a7dd-f015150b9e15 | -5.12107 | -39.08447 | 2026-02-04 03:49:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b2a31a1-26d6-367e-a45e-7b839c9e7811 | -7.34752 | -35.17521 | 2026-02-04 03:49:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d1bfa11d-d6a7-3b79-beb9-fbbc5a85efbe | -6.15063 | -35.40271 | 2026-02-04 03:49:00 | NPP-375D | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 881fb5d6-e606-3975-838e-06106099b10f | -6.7917 | -35.26938 | 2026-02-04 03:49:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1672d862-4c07-378a-99c9-e0d947c04a10 | -4.9213 | -37.43192 | 2026-02-04 03:49:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6be64af7-1ce4-3c2e-bb00-9ce9c588d56e | -3.49172 | -43.63845 | 2026-02-04 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4b8e877-893a-321a-86d1-efab46620091 | -6.44008 | -35.45903 | 2026-02-04 03:49:00 | NPP-375D | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ea531150-63e1-3632-ac75-e6652edd7817 | -8.70884 | -35.11689 | 2026-02-04 03:49:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 047048e9-a9b1-396e-8d19-efeed5dd6fd2 | -7.98099 | -35.37895 | 2026-02-04 03:49:00 | NPP-375D | FEIRA NOVA | PERNAMBUCO | Brasil | 2605400 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc11d399-060e-3a77-a6ef-5334323ddb44 | -3.49058 | -43.64508 | 2026-02-04 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af614b55-c317-36f5-acad-3848cfbad196 | -5.2761 | -35.97269 | 2026-02-04 03:49:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07265ae8-cb7e-33b7-8b98-7f8939510376 | -4.94357 | -38.73498 | 2026-02-04 03:49:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7a8b2732-9882-388d-8a46-d07229d2be1f | -5.11647 | -39.08849 | 2026-02-04 03:49:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d777bcb5-c18a-3247-8e05-ba361b2c83aa | -9.73154 | -37.69907 | 2026-02-04 03:49:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1d5ee6e-6a91-341f-bbb7-3e415d229df9 | -4.86468 | -39.00616 | 2026-02-04 03:49:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5f567e68-16de-3774-a764-04ffea3a5d93 | -7.77685 | -35.86104 | 2026-02-04 03:49:00 | NPP-375D | VERTENTE DO LÉRIO | PERNAMBUCO | Brasil | 2616183 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d505fa2-038f-3f63-b3ee-4bd42b1261d6 | -3.43241 | -39.27533 | 2026-02-04 03:49:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c694071f-b8f7-3136-8794-3c64fbf89e58 | -5.70296 | -35.73101 | 2026-02-04 03:49:00 | NPP-375D | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ec01934-0af7-3d53-8452-783f57b3f8f9 | -3.49592 | -43.64585 | 2026-02-04 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1cd6ec1-0285-34e6-8137-ad5aecac052c | -3.49648 | -43.64256 | 2026-02-04 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d650d6d3-32a0-3c6e-aa65-4c0927bd4d5c | -4.23654 | -40.39248 | 2026-02-04 03:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e846e11-3103-34da-89ed-d943f800bcfe | -3.48798 | -43.64183 | 2026-02-04 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c1ba21-d277-3e54-8991-ea07d4d56734 | -4.46082 | -38.38494 | 2026-02-04 03:49:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c6b79696-55ca-3b8f-9962-7ab8027d9f67 | -4.77288 | -40.07352 | 2026-02-04 03:49:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4ce1a8d8-9af9-3774-a6cb-9c0189b73327 | -8.70495 | -35.11989 | 2026-02-04 03:49:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e7e2efc-9861-3a99-85e1-352d1e73d622 | -4.36489 | -37.90242 | 2026-02-04 03:49:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 88f6e14a-51d5-352b-834e-c620463acabf | -10.3199 | -36.77868 | 2026-02-04 03:51:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c5a54c28-3f07-3d54-9b0f-139e8c050d03 | -10.6498 | -37.12305 | 2026-02-04 03:51:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 052298b0-8940-3fc8-8a52-05fe448bf8d3 | -10.652 | -37.13073 | 2026-02-04 03:51:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 35a81274-80c5-31e5-994d-659bd826c4a3 | -15.25812 | -39.27771 | 2026-02-04 03:51:00 | NPP-375D | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 97d2d47f-30e0-3008-a0a6-87598c58e110 | -10.3238 | -36.77569 | 2026-02-04 03:51:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1635428c-d068-311b-9c2c-8573d7ae1802 | -10.64703 | -37.11893 | 2026-02-04 03:51:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da3e78a4-f62c-392c-ac3c-8d5b5bed834e | -10.37412 | -37.97807 | 2026-02-04 03:51:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf17cf7b-1bf3-3afc-b078-4e8f9e5f07b9 | -10.32324 | -36.77922 | 2026-02-04 03:51:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 87211165-8f6c-3d2a-9b8a-ad3cfbed4fb5 | -11.66596 | -37.89837 | 2026-02-04 03:51:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8787dde-2d59-38df-b9a6-6dd483843413 | -10.533 | -36.6934 | 2026-02-04 03:51:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1575f1bf-65c8-3f86-bc1a-9e3d62c8cf2c | -11.13035 | -37.19098 | 2026-02-04 03:51:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3bf6c179-84fc-3026-8256-d7e488f540df | -6.05913 | -43.25441 | 2026-02-04 04:08:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README2.md)
