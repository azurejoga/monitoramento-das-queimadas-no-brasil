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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acc4a677-a943-3201-8629-3876a8798b96 | -8.71158 | -69.46013 | 2025-08-22 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 307c7a7b-6c0c-317c-a8bf-84bc7a78fc91 | -9.20603 | -59.46229 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86ba947d-8b8b-3c7d-954d-72898192c8d7 | -9.15365 | -59.59953 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa18b560-c716-31c5-9fdd-3755cdb5fad5 | -9.52038 | -68.47031 | 2025-08-22 05:38:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a538b425-e585-3395-b2cf-1d1fa467b90d | -7.583 | -63.43746 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3f4d708-aa7f-39c0-8cd1-97f1c3fe5e32 | -9.88723 | -60.28925 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fa79e77-4e33-33ff-9b33-9dcf541a2058 | -8.62171 | -62.61342 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50d621a6-c664-3f66-a67d-064eb08881d4 | -5.80343 | -59.21783 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3338212-1bee-36a9-9af6-81eda3074fe2 | -10.13251 | -65.28576 | 2025-08-22 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64c77bf5-07a6-3f19-9eea-9012f1c28c78 | -8.86421 | -62.39895 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00dfcf7c-efa7-348c-970c-fc60fce6f317 | -9.16791 | -59.6119 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8968a7e-86a0-3b6e-b593-c4ef43d93c2c | -7.93484 | -63.04281 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43399f20-d996-322a-a240-257f6f60590f | -5.80214 | -59.21452 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd870825-5016-3d39-bc71-82d9952791a6 | -8.86876 | -62.41478 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0933544f-93bb-3f47-86f4-686dec195787 | -9.95914 | -64.86564 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7e6ada2-1c87-3084-a53f-2e3074edafde | -7.63769 | -69.94666 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a70ea87-71da-37db-b025-e4a4accbee80 | -9.21285 | -60.79002 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1126699a-c2ae-3f6e-a9ac-f77b085abcba | -7.847 | -61.72941 | 2025-08-22 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a6603d-bbd8-3488-9add-aad16276853c | -7.29562 | -59.62222 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb59a430-7aca-3cad-b71d-738adc52bc88 | -8.88435 | -62.42405 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00e28262-dcea-3348-9546-353366096203 | -4.5564 | -55.964 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90d9fd21-492e-3333-9289-2b47c661d4eb | -8.60816 | -62.61132 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2487c54a-9cb3-3acf-adc1-84ce8a0aa0a8 | -6.27505 | -53.71016 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3870875-6e65-3b1d-8128-6ee20f7dbb7c | -10.86438 | -50.82014 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e12cf56-31f9-3dcc-b3fa-9ec1897d06ea | -6.56486 | -60.05892 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61ff0f50-3195-33b4-9319-295d5c03f337 | -5.43698 | -60.1823 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e7106ff-496c-31a2-8cdb-2d34616eafa3 | -7.05417 | -59.8233 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09251b75-a128-33b9-91de-48b81a07e06b | -9.1897 | -60.76882 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63974916-c712-3b68-b71b-5425aa164e86 | -6.16657 | -53.77168 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d7a12a6-aaeb-3e4d-94da-70d0d4cbdd2e | -5.15189 | -62.5273 | 2025-08-22 05:38:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93243676-e4a7-343d-8a62-4a8a6b7d0db0 | -6.44239 | -53.38231 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52841601-8ade-35b1-a1b0-6e9af8ce1cea | -6.27026 | -53.68412 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbeacd5b-54fe-3539-9dd5-127a376394fa | -9.5158 | -64.20173 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03a05edd-d442-345f-9090-2b56a6b6e37d | -6.16177 | -53.77596 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3d52174-babf-35c6-b7cd-e6cc974cda83 | -8.5486 | -66.94559 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca4181a-b3c1-3d62-818f-dc0346034bd3 | -9.66125 | -66.25655 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ae7adb1-595b-30f4-9bf4-39c797c6f962 | -9.21155 | -60.79868 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c181c28c-5d8e-3c41-ab87-131e8a680642 | -9.30975 | -57.01894 | 2025-08-22 05:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7609718-5820-390e-bc8d-ff224a23cc2d | -4.09779 | -60.66328 | 2025-08-22 05:38:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dccb3e8-2df2-3aed-8629-1176bec6c520 | -7.30327 | -59.62347 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d8f102d-aec8-3315-85c3-a06642a4a6e9 | -7.05282 | -59.83238 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5b5b8de-317a-3da9-b63d-a1d1c61dc922 | -9.21429 | -59.4493 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5308bd2a-ee34-3645-8be4-2e94186cb0be | -8.96441 | -61.67461 | 2025-08-22 05:38:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6277541-1735-3209-8de6-74fd59ac723d | -10.86021 | -50.81799 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 661622e2-912e-3c7b-a7cc-57df964039bf | -9.22876 | -59.76999 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01358b0e-c9df-3cfd-9837-4100e00ee9b6 | -9.09841 | -61.42947 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3739fa60-01f7-3eee-872d-b8643eddd4cc | -4.88534 | -55.98352 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8da82f6e-95b4-34dd-951b-af8d67b2f7fd | -8.54927 | -66.94151 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50cc5123-41d4-3522-9157-e420edd73c3a | -9.16545 | -59.60129 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b93ee5b1-e13e-3789-ad36-f94197c75abe | -8.67278 | -69.7273 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32b53365-e227-309b-a8e0-fa57e4c35af9 | -10.11159 | -57.75844 | 2025-08-22 05:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20b53559-5b26-366c-9bda-bf00c0a979d2 | -10.46044 | -59.13293 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 981a7ae9-bc76-316b-87fa-f6156deab526 | -5.43957 | -60.16558 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f93b6ba-c3a7-3e94-a0e8-a18542f0140f | -6.16229 | -53.77231 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e9aa825-1fc2-36a9-ae06-0411b908ac0e | -5.88358 | -53.63179 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 334d49fb-c447-3cf6-961a-f7d9738be513 | -5.88163 | -53.62523 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f90c597-f439-31f9-b5fa-a69075397df6 | -8.54995 | -66.93744 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72fa8c31-3055-3443-b460-0214b1f1e57f | -8.60081 | -62.6139 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c80e6bc-a637-3df6-918c-6c6fa0e8281f | -8.89289 | -72.7101 | 2025-08-22 05:38:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1762752-b276-31db-b0b6-836c2cc55656 | -9.17258 | -59.60747 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d5168f9-4a80-3243-88fa-47058c377680 | -8.87446 | -62.40051 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f417316b-6409-360e-a25b-61f0d59c664f | -10.97336 | -61.56154 | 2025-08-22 05:38:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70c1cf72-775a-3baa-96ac-5b78049fb9b6 | -9.16962 | -59.70912 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed707f6d-9c97-3748-a594-26fe621e91da | -10.96976 | -61.56095 | 2025-08-22 05:38:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33f0acbb-5aba-3808-bcf3-7227715a0829 | -9.18926 | -59.62716 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 906d8ea1-cc88-31ef-b8a7-259928dcb110 | -11.31712 | -55.22578 | 2025-08-22 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cad259d0-9c8a-3c3b-b049-6a486caae909 | -9.16152 | -59.60069 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45d95b46-5bc5-32e2-b963-63837354204a | -9.18534 | -59.62653 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af633abf-9f92-351a-942a-85942f9037fa | -8.87674 | -62.40844 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cfbb09a-164e-3231-9528-0cee1262cad4 | -10.55196 | -62.74068 | 2025-08-22 05:38:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 482a09dd-ce38-3af0-9d20-15fc8d54bc66 | -7.57247 | -63.43937 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c742fd0-49e1-3bd9-a842-4a22249d07fe | -9.52682 | -60.54772 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7020a251-bad4-31dd-bf3f-bcda9dd58dda | -8.88469 | -62.42482 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e902f43-c8ed-3444-a3cb-d4829ffcfbf7 | -9.16225 | -59.59567 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c743ad4-ba39-3d79-8f05-a13d44758ea2 | -7.624 | -69.94852 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b24f190c-c47e-3fc8-8171-74d728bafdd6 | -5.87746 | -53.63461 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d030b70a-ae5a-38d1-83c6-b37bdfb861f9 | -9.52066 | -60.53759 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19729b10-7394-3158-b2f0-11c49d55488e | -9.21323 | -59.46851 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc24b54e-5102-33bf-8748-7054dce6320e | -9.20959 | -59.45388 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e3a3689-0cda-320f-92b5-eb1a90c6224e | -7.3071 | -59.62407 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbb76369-19bf-35ab-b5bb-6cb03158e116 | -9.51431 | -60.555 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26301763-2d42-3cda-87a8-9b9fe8dd918f | -10.03654 | -59.3586 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 869cb168-f215-335c-9783-97125e692e35 | -6.31215 | -59.88759 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dd0161c-d934-3cb7-a907-13c5fe2feadc | -10.85806 | -50.81237 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a22c8904-a984-3cff-bee9-7580d713131e | -5.87601 | -53.62449 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 616c6a4c-e030-3dc9-afe3-cae3a8321f76 | -9.20887 | -59.45905 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57f41a8e-5765-3f70-b814-8b936e95b9c0 | -9.22382 | -59.7491 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a388e6cb-1026-3d87-8cb5-88e250f2853d | -9.65214 | -59.65149 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99992247-8e72-3067-93c0-b15a48dafc7d | -9.52551 | -60.55672 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f17ae164-cfb6-31c0-aedb-3b3920f5ac95 | -8.14463 | -70.50231 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1a663a8-9049-382b-be74-2160430ee0e6 | -9.19568 | -59.63852 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66b01da2-6e26-3de2-a875-c64fbd591820 | -6.90085 | -59.89534 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e47c5bea-2b89-3bcd-bdb2-8f055d55059a | -7.30188 | -59.63285 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e834f93d-c6f0-3c11-9ff4-a63b749df57b | -10.09871 | -68.96278 | 2025-08-22 05:38:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07324898-dcc2-3c25-992c-66544752a5f7 | -4.55568 | -55.96881 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28470c3e-bc1f-3aed-8ef8-f005aa5cb773 | -9.52289 | -68.29201 | 2025-08-22 05:38:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fed16a47-eb07-3acb-9295-63d564d4bf5f | -8.87616 | -62.41213 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b66739-08c4-387b-885c-05706967aeee | -8.86649 | -62.40686 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8879fc3d-d326-393b-b667-2eac063df72b | -7.75517 | -70.15427 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae725806-e8fe-3c73-9e28-71b5cc3aa477 | -9.21349 | -60.78569 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README58.md)
