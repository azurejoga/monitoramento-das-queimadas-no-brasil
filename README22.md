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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62fa5815-db2f-39b3-952f-8bc2caf9a42e | -11.45167 | -44.9542 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71541f96-d4d1-3119-85f0-d67854ea2448 | -6.9919 | -42.32943 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6502c909-959b-3f86-892b-78493c1b6cbf | -5.72964 | -44.51026 | 2025-10-04 03:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e720dc9-dc0e-3dfc-b544-e99d6d4f5f8f | -11.42718 | -43.48874 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7261be68-a856-3390-86f2-7b0c30e53246 | -8.90291 | -46.05471 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 994488c4-03a3-34b3-b57e-9202b6810d5d | -11.4819 | -45.02337 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 377cb5c7-9dd8-388d-88da-0572e6f702bd | -6.43525 | -44.45731 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6303eeb-fbc0-37bc-9a09-442eb33b5fac | -6.67529 | -44.20474 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 625b2b8b-a2ba-36f7-b4bc-f6cb19b12869 | -5.1876 | -45.06886 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76df2b9f-528e-3618-bd49-428db7ab0d65 | -11.47364 | -45.01641 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 149a4909-4977-38d9-b7c4-2db22a839fa5 | -10.32963 | -50.34313 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 343dced9-302f-3b4b-9de4-767f3acf6cef | -6.71606 | -42.80383 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3bb27003-dbc7-3171-b33f-c8bf0f3eb2a4 | -7.80143 | -42.54283 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 423dcc18-05e6-3a5a-afa3-3379af916bf5 | -4.73323 | -43.26277 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8982c03-94a5-313a-9896-0655a9b357ea | -11.6697 | -44.26861 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a852187-ae0c-31b5-9f26-b1effe7d0ece | -8.63312 | -43.98787 | 2025-10-04 03:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e47ceab-fc74-3a06-bd35-87dae5e985f5 | -8.21935 | -46.79951 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b01fc92f-140f-3f3d-85da-2fc52d3ff2be | -6.87197 | -47.23872 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f0a41a92-e5bd-391a-9a47-52fa006c0878 | -7.65576 | -45.44396 | 2025-10-04 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8c15c6-3ed4-3c4d-bbaa-631fa1861073 | -8.91047 | -46.60453 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 419ad1b7-b936-3751-9ff5-e1c0e186b2d1 | -5.69166 | -42.84756 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 33a72337-40a7-3984-af7f-7bdfd2aac955 | -9.75696 | -43.6181 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92f7144b-999a-3046-92ca-457ea500cc9d | -6.36882 | -44.30372 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5f6ffb8-8b74-37d5-aa49-35f8b5733bea | -8.17062 | -44.13081 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3debca3-2d88-3ff3-b12e-acb433bd6a82 | -7.74207 | -46.28054 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bbaa52d-99d3-363b-b58d-51d9f7da4174 | -11.11512 | -47.89462 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f04d3776-a5c4-36f9-ab44-a39afecacf6a | -7.51479 | -44.27152 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4744a71-6623-3895-a257-a1fc96b648ec | -7.05058 | -37.97002 | 2025-10-04 03:51:00 | NPP-375D | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f37ff7d3-0c67-3e44-9a5e-c27b31367053 | -7.00039 | -44.19384 | 2025-10-04 03:51:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7002ce9e-96db-3981-9faf-57eb7ac43784 | -7.04709 | -42.78757 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 164f46ae-81e5-3ffa-a0e4-06825ce3c929 | -7.76856 | -42.61135 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 38fb64b0-324c-30f7-9aa0-005e59193cd9 | -5.69314 | -42.83904 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8fb9c312-f9a2-33e9-bbeb-b06f9f3e8fcc | -10.33843 | -50.33317 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 86ecaada-9530-3285-8e28-940fa30e9b5e | -11.41919 | -43.4901 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81628343-2610-3f1b-a354-5faf5123ef95 | -5.19788 | -45.07056 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 79274503-b134-3312-aac3-de8e4f3f3db6 | -6.34147 | -43.45789 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b64af96e-cb11-3b1d-a452-7819622b2cf7 | -5.08218 | -44.09716 | 2025-10-04 03:51:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e89615d1-fcd6-38e3-b95f-ab287cf4132a | -4.65791 | -45.79867 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 253fe524-c6c4-3d22-a5f3-cd60293f6a02 | -9.34613 | -45.80019 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9f18e7eb-0d72-3c42-bdcc-ad4b66c3e89e | -5.38416 | -36.8359 | 2025-10-04 03:51:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 50f36021-eb3e-34e8-9553-71098a63e420 | -8.62691 | -43.98895 | 2025-10-04 03:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aab028f6-919f-3302-9802-d0800793b59c | -7.79891 | -42.55792 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 12eedf23-9d9b-37cf-bef5-f2ec35e6388f | -9.90326 | -43.73637 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9ddd5265-bb8b-381e-9e88-2f1c0283c5f1 | -5.74 | -42.93446 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a1221f75-7080-3664-bb67-05af7dbce627 | -4.43702 | -43.24263 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92fb0c47-105c-3ca5-bf8a-825f361ba67e | -6.87776 | -44.50403 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| dca1d83e-6b08-3284-a59a-3f2747a9ed06 | -10.53057 | -44.51439 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 522fb527-d459-3501-8332-dbcf980ff5fe | -6.24048 | -44.22546 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca4d0794-e0bd-3f96-b854-fc8575eaae9e | -7.75296 | -42.52689 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e817f648-edfc-3a75-a0b9-9b6c11a0a57e | -7.00052 | -42.30405 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dbb9aad3-e1ab-3d7c-b233-e3bf57fa7da2 | -3.69663 | -49.57152 | 2025-10-04 03:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5df7503f-ea09-39ed-a0d1-67479c0b364b | -7.79496 | -42.56434 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 08cd02db-e42f-3531-ba83-0404f5207be6 | -8.62407 | -43.98655 | 2025-10-04 03:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ab3e423-a771-38b0-9f2d-1ac007b72ab2 | -11.48007 | -44.97734 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e9332de-fbe5-3c4e-a272-f15eadec9e99 | -6.87267 | -47.23476 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fad64a17-db4b-3b67-9f4d-17a299f2c02a | -7.75838 | -42.52009 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 805b6cd1-dea5-3f90-9ca5-ffee85143f7b | -5.78948 | -45.78408 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f5cc869-1895-36b7-b2b8-9ecc3ab32b09 | -6.66683 | -42.8328 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad23a915-b39f-3705-930a-d2271e69ec61 | -10.3285 | -50.34884 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1f12a5c4-3c17-3ec3-8771-9889d8ac3737 | -9.9335 | -50.24022 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00cbdeba-633f-3b51-b45a-da24b71faeab | -4.42337 | -46.41194 | 2025-10-04 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d5368b2-442e-3d51-97c4-a54c738255e2 | -6.3717 | -43.89808 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5febf260-63c9-32a0-b833-79682dda8554 | -8.05956 | -44.80665 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a6e0580e-d3be-3728-8533-c379786dd2e3 | -4.95184 | -45.06704 | 2025-10-04 03:51:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96ca3770-f891-3b37-a2bb-6bf6e158118b | -9.10461 | -44.40223 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 266d9ccb-8442-3113-86c9-b5fdba792e4c | -5.97439 | -44.14939 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 752ded9d-d617-31b2-a698-c45bde21fbe5 | -9.34721 | -45.79423 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 052706cc-d66b-352d-b3d6-10cb46d35f7a | -7.77404 | -42.60427 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f80ea439-d0c6-3d6d-92b5-0d70fc807615 | -11.07471 | -47.7243 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ce3d41e-888c-394a-942b-bc05fc30e291 | -9.08609 | -48.02422 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47bf80ac-e010-3afc-8d45-9dd1f5d5d080 | -5.19737 | -45.07359 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8fef4777-446c-3e89-8fb2-d76666814a98 | -9.90043 | -43.72715 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61de98cd-c17d-3e1e-a07f-ecf5f920f530 | -11.11587 | -47.89072 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa5e2878-2762-3f39-9331-11ea7e875340 | -9.91306 | -43.80758 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 194c7ce2-d315-3e6a-85f7-715a2cbd5ca9 | -6.55714 | -44.15128 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ff7ff2-4e97-3f26-94da-85fd3e8664f9 | -6.17456 | -43.91878 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa16ec68-9c77-31d4-bb16-24059b0d7717 | -8.5852 | -44.79738 | 2025-10-04 03:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b926d285-bced-357c-9ba5-68f3093d002a | -7.80304 | -42.54251 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 562ba305-c1b3-39f9-a84a-89a54efc7300 | -7.7842 | -44.14154 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3ffffe1-0b3c-3395-8846-dfa3925c6b96 | -5.95314 | -42.95033 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| afb522e9-0898-3574-b7cc-e8b318c5efaa | -8.23062 | -46.79863 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5b7be99-8bdd-31e6-aa87-922e9b198986 | -7.00464 | -42.30478 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80109f4b-079f-36dd-a815-7bcfe8abd737 | -10.33187 | -50.33179 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b07b8d20-0f11-37b5-9132-9d73e4032013 | -5.87024 | -42.67171 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd04f9b6-2fe8-3b24-8948-2b0dc269ca12 | -7.7151 | -42.59809 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5cc6277-83df-3bb8-b066-9db0a9768bda | -5.67297 | -44.19741 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c94a0a8-fd09-3420-8b4f-7fd1a8143111 | -9.95304 | -43.75825 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42e182a7-5f7c-39ea-875b-245c859753de | -4.95596 | -45.07397 | 2025-10-04 03:51:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2103f397-bdca-3092-8e8f-e50c9a5ed972 | -11.07639 | -47.88505 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ec2110c-c5e2-37e6-8666-c203189e2bd5 | -6.31117 | -44.27129 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e6afbaf-6fde-36bf-b794-e5041ff6b358 | -5.67043 | -42.70824 | 2025-10-04 03:51:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f01a160a-0033-3ee2-a7b9-bc066eb73839 | -7.558 | -42.63053 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b732eeed-cace-30c7-af08-6c93a4fc6104 | -6.09269 | -43.48195 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac4b96f6-38f0-3668-8eb3-66ef8ee345dd | -7.79627 | -42.5568 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ad93acf5-22d8-32d9-aa21-47bec8f5bcf1 | -4.9508 | -45.07311 | 2025-10-04 03:51:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba050f36-5fa4-36f4-9315-52bdaa6395aa | -6.99541 | -42.33381 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 33cc90a5-ed2b-339c-bb12-97759999c4ff | -6.69659 | -41.94255 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 37755dab-ce4d-3d03-bc66-2833e167d2a6 | -6.16905 | -43.92298 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccd3c3a9-2f1f-3643-99fa-82fa8bc15146 | -9.33362 | -45.75492 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b60c0433-356b-30e7-87e8-b3dede56e1d6 | -11.682 | -44.2753 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
