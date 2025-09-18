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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba688b30-b1ee-3f81-ae77-98338ebcd017 | -7.25168 | -46.62215 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 431b6c01-8a55-3708-905b-38da76df2ea0 | -7.66312 | -44.45731 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63ca1472-33b1-3ea0-a37e-44e2a6aa2f85 | -8.13567 | -44.83794 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf14c5b7-da6b-3c54-a5b5-e35a2c055c5b | -8.82845 | -43.01467 | 2025-09-18 04:14:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43578b3e-13da-32af-879f-4ff1025b5999 | -7.69721 | -44.47392 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b05dd9b4-46db-3c72-af4a-9c6abb028c7f | -9.82952 | -48.42812 | 2025-09-18 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ae5a4ab-55c4-357f-b3f1-12cd5eafe9f5 | -9.72725 | -46.57853 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e4a7e24-2a25-37ff-a00a-fef63dd728fc | -11.37913 | -50.82683 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 04888970-bd64-36ee-b912-2f46f96b4d06 | -9.08351 | -44.94196 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8fa0315-6df6-36dc-9247-7526e45e6357 | -13.93952 | -48.00418 | 2025-09-18 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f2bf77a-e691-3245-96b3-d89d4f250335 | -13.30495 | -43.7365 | 2025-09-18 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87b7a701-f387-32f5-96d8-483d033de645 | -7.63856 | -44.46068 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92b5b1ee-edc8-3b04-bdcc-01219adba90b | -12.0997 | -44.81772 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da45cad8-d042-3296-9061-4924b46bfd39 | -7.51216 | -45.31397 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c966a7c-9eec-3dda-9e89-f6a38a9acc25 | -12.59868 | -44.41199 | 2025-09-18 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07c922e3-832f-35b3-86d3-fad1ee1b33bd | -14.59381 | -45.17529 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 972d63a3-fb48-316c-90ea-e2415961b183 | -8.97248 | -47.04959 | 2025-09-18 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe65a3dc-e53b-3e29-8bb7-721045276b77 | -14.70986 | -45.12825 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 657915bc-f5b6-35d3-afe7-acd3386d065a | -11.37276 | -50.82875 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ad46b53-c78b-3585-b108-1d8f9d3d9f9f | -12.242 | -46.78396 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bb5522dd-67cf-3185-bb3f-0a395ead5323 | -7.17325 | -46.71269 | 2025-09-18 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54f811f0-2aae-32cb-8513-64df9d74c696 | -8.07892 | -50.1628 | 2025-09-18 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 982659e2-dd40-3eea-921d-c15733fafdfb | -11.71831 | -50.77535 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83d72597-1667-3b89-bd38-0fcec90c5b3d | -12.02308 | -46.72757 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f42e5d2-1619-3821-b54a-973058af7fc0 | -11.67636 | -50.50609 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4183367-7fc1-3844-8471-7445cb4cec70 | -13.82625 | -43.23607 | 2025-09-18 04:14:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e7d6fe7-b5ff-3373-9c1e-b86778427abe | -10.62486 | -46.5236 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c19ea4c-c4e0-34a9-8ef0-6a5eb77e1d0e | -11.17545 | -45.32685 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6c17040-4370-38c9-8e12-9606ad671373 | -7.29131 | -43.93223 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2f4e26b-e6b2-3b9e-9d4d-4ed445b0c0f2 | -11.50083 | -43.68288 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9aa6a1cd-9b4c-3d39-a8f3-cbfe71db4a86 | -8.06079 | -41.27405 | 2025-09-18 04:14:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 15aa1a6c-76cc-3fc8-96f5-21a77a64b850 | -7.51635 | -45.28792 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7adbec2a-e02f-399c-a158-70a05d5be167 | -8.60756 | -45.71684 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b04da42f-032a-3e8e-a000-611874599fc6 | -7.41708 | -49.98988 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dea8e215-3ff2-3815-9894-250b6d61e98d | -9.87737 | -46.43895 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c0ad967-eb2f-35e1-94af-4f4390b7e0c4 | -12.44127 | -49.74435 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d61c849-9864-3526-931a-b7406dd0a8eb | -9.82899 | -48.40747 | 2025-09-18 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25e1c603-d000-3399-a41f-38152cfe26b1 | -12.1724 | -43.57534 | 2025-09-18 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c2cd99c-a83c-372b-8589-7d1be4282960 | -7.24516 | -46.61633 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2d363199-dfd9-3fcc-9274-7e176b7dd144 | -7.26766 | -44.91468 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73091a0a-fd8f-3749-9e37-ce7dee4217c8 | -7.93466 | -43.88095 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af705e7a-04a8-3cc2-b9ba-779c5903c2dc | -7.51755 | -45.28047 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f806453-3153-38ca-b02b-238019a82295 | -12.07843 | -46.56531 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0310b07-f77e-3b79-9ac6-40bef572b77c | -13.66034 | -44.39615 | 2025-09-18 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dd2d110-0abb-3f8e-8e01-0485636dc529 | -8.88586 | -46.1405 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c53566ca-216d-30e9-9630-ecb530fd32f0 | -13.53414 | -44.1171 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26281b35-1f77-391a-9a86-c67239ec0a58 | -11.71391 | -50.77452 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe18e98-a50f-389f-9c88-790856abb572 | -8.13058 | -44.84819 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd30922d-f0ef-3dd9-be52-4b1443bc226c | -14.47204 | -44.87055 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42558b97-926b-359b-96b7-45a9d21b0ed7 | -7.55836 | -44.7674 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7715cc00-b9a0-383a-9385-78a6d7c375f9 | -10.68157 | -46.48426 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ae6f4e1-185f-32c4-b33a-af2b0ac5daf6 | -7.18007 | -44.35099 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca41e76a-2c3d-36b1-a182-67df41ff3061 | -8.14048 | -46.75417 | 2025-09-18 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9732f8f9-b7c2-3901-a106-7c9ccfaac47e | -8.69661 | -46.3665 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 152f0d51-78e4-3190-be3b-d0ceca19a626 | -9.06398 | -47.01806 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a624aaf3-a4b4-3b03-9fbe-80ac2bd71d30 | -8.98897 | -47.04126 | 2025-09-18 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee329d54-69a0-369d-baf6-fd386b2ad2f5 | -7.99909 | -45.64346 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee40e584-78ae-3eda-a602-5b84dc632634 | -12.10295 | -44.84001 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89272f28-34c5-30a8-bbcf-3972afd2a413 | -8.0243 | -45.65442 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f41181ac-744e-37ed-864d-35c2f3f0423e | -8.01128 | -45.79804 | 2025-09-18 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 813b8e6d-fc62-34c2-abd9-2d796f275acc | -8.14635 | -44.83599 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e16dd97a-daf9-3388-b08e-a73ed18f82f3 | -7.51571 | -45.22643 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5278eaaa-4ec8-37c7-a6fc-474d83e6055c | -12.10414 | -44.8112 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3d71219-80ab-3af7-80a5-b3577178ed8a | -14.47033 | -45.98951 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 584331ef-2698-370e-b28b-3f03c56a0b4b | -9.15996 | -46.95963 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2b3a4f74-cbbd-3eb9-b127-249ce1b684f1 | -11.16904 | -45.36651 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2dcbf54-e856-31b6-b298-1edd5bf292dc | -8.65019 | -46.43014 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75c60329-d1ca-37cd-83e3-24c2d161aad2 | -9.11386 | -48.11538 | 2025-09-18 04:14:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5320d4e-5b69-33db-9e81-4a72c4ec4e0b | -9.96763 | -45.4424 | 2025-09-18 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31911f63-a204-3424-89ef-f587e031f798 | -11.37469 | -50.82598 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 09a2cc54-3abf-3526-8bb4-148bd3251bc5 | -7.52665 | -45.28946 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d4ad353-1e59-3228-afb4-53ca3aefc4f9 | -7.44904 | -42.6293 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7dc3672b-5a58-37f1-9c73-0fdbff2494ab | -7.53222 | -44.71516 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f57c2fde-4ce7-3ba6-a418-5ab48f11d9d1 | -11.247 | -47.39628 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e3866b2-385a-3d94-9c49-6ebe528347df | -12.10239 | -44.84355 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d99066b-a164-32ae-bb1d-2d159f04d653 | -9.13908 | -44.8667 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffd153f3-9736-3b3b-94b5-d2ff0f815edc | -11.16467 | -45.35096 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1ca1058d-b309-3656-bda6-2d003b61fa2f | -12.90588 | -44.66088 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a5cb1f5-1da6-3664-8c2b-37b82a336db1 | -7.3828 | -47.0492 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae3b1273-5e08-3062-9a24-21c0049060e2 | -10.64553 | -46.44248 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a1efd9c-ba44-3e40-839a-0c1de8d45697 | -7.94792 | -43.88304 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1c57818-ff30-3b76-a6bb-fadc7c493469 | -7.65586 | -44.45979 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85c1ce2f-2931-3264-b1f6-b09594bd151a | -7.53249 | -43.97438 | 2025-09-18 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f598f9d-7dd9-342a-83f2-5145aa732fbb | -12.13088 | -43.2271 | 2025-09-18 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a39fca0f-0452-33a6-a1cd-49db69bfeeae | -7.80388 | -48.38723 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa2e70b9-ef09-358e-8147-b583a31baf86 | -10.07644 | -48.18128 | 2025-09-18 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d3646fd-2e6b-35a4-86b2-2920049a0a1e | -8.01657 | -45.68916 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16000332-107d-32e4-bfd3-e9405d7d81cd | -7.4413 | -42.63526 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 55f278cc-1c22-3f6f-a39d-3438498a79fa | -8.87761 | -46.14697 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35aebc80-5249-3866-9a93-3dbfdd55570c | -14.46916 | -45.99677 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f940eb0c-f34c-3140-ac75-5c5465635fd9 | -10.87969 | -47.7715 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85a3f60c-65d8-304c-ab02-ad058bedd01a | -8.69308 | -46.36591 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfa634b6-0b53-3d2a-817d-af1d697801f3 | -8.4738 | -44.74068 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd55c219-23da-3699-aa63-5c25087fe15a | -7.81781 | -46.89557 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f7a00fe-b094-3581-8f0a-a69a3ccf275e | -7.83083 | -43.8508 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c8e7b8-651c-33be-841a-ea36c2fe50a1 | -7.45127 | -42.63683 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a80dec58-8607-3ad4-a0cf-0de80da4d81c | -11.36415 | -43.68977 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65c57df9-476a-31be-b964-928c397be74d | -12.90034 | -44.67444 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8623ca41-b555-3853-b4c8-b41dd97c6b11 | -8.04363 | -49.81913 | 2025-09-18 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d2a88c5-793f-33af-b88c-9ad22107e863 | -9.22636 | -43.27087 | 2025-09-18 04:14:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |


[Clique aqui para ver as próximas entradas](README20.md)
