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
| 88a7506b-1b22-33a1-8e93-740fa4379231 | -5.52536 | -43.21135 | 2025-06-03 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30584945-5a35-3976-a638-c3fa5cff59f5 | -7.88593 | -46.22657 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18de328c-f5de-3532-8a75-7c4220ad579e | -7.69005 | -44.57301 | 2025-06-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c8aa033-55ca-34af-a0c1-9460d85a4049 | -7.22938 | -43.12714 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2273f8b2-087f-3ccd-8e56-a0d87fe65469 | -7.20428 | -45.34833 | 2025-06-03 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8efd9ef-4f50-36a6-ae01-cb4f068b6c97 | -7.2803 | -44.21912 | 2025-06-03 04:17:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deaef598-b310-3a72-b9cb-dba018a76425 | -7.87114 | -45.98372 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b9e0eec-8fa9-36c4-bb93-badf2a945fe8 | -7.68343 | -44.57196 | 2025-06-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ff66cae-88bf-3b07-93e5-9f4fe5fd9104 | -7.37804 | -43.11895 | 2025-06-03 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92b5b9e6-ee3f-33ef-872b-0ceedcc4b131 | -8.07525 | -43.11409 | 2025-06-03 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| b57c4c2b-ef22-3d9e-823b-545a61babb0b | -6.96857 | -42.91022 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| eb56e61a-9d8b-3d88-92ce-1868296c7107 | -7.07071 | -44.92566 | 2025-06-03 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45b6096d-a236-3229-8d09-2b5a4ff8a915 | -3.98492 | -48.40769 | 2025-06-03 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a7bdcd1-79cc-339f-9200-a1d2f062ad6e | -7.21918 | -43.12556 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6896ae5f-d9c9-3188-9e88-4ef4deac290e | -7.5109 | -43.32278 | 2025-06-03 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25da227e-b55e-373b-a00f-446a2f3b5dc1 | -7.80531 | -46.03117 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d59c52d-7645-3701-9a2e-84879f31439b | -7.70872 | -46.31911 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2229cf3d-1c1e-3c43-983e-3eea16779281 | -4.81271 | -45.26208 | 2025-06-03 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4913765-e202-32db-a81d-0a62532e7574 | -4.80993 | -45.25806 | 2025-06-03 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1a7deff-35e4-338c-a1b7-25240bffc822 | -7.70389 | -45.77581 | 2025-06-03 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8132adfa-8c2a-35a3-9e18-6a04c4455ba3 | -7.22598 | -43.12661 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2a36cec7-f295-3e1b-ba29-73e24949cff7 | -5.92195 | -45.5276 | 2025-06-03 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0529e73e-21f5-30a9-905b-7464c29191e1 | -7.70056 | -45.77527 | 2025-06-03 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 807b39b1-f49b-3575-9270-b62994e4fbab | -7.22258 | -43.12609 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a1548ded-fd56-3aab-9052-4ccebe0cdfc8 | -3.98569 | -48.40295 | 2025-06-03 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea21fdcf-8a70-3e81-8c79-ad1fc1fe36bf | -7.0674 | -44.92514 | 2025-06-03 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf0b4af7-1cc4-32dc-97e3-a0620f4c03b8 | -6.97218 | -42.91065 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f6fac2d1-5bd4-382c-98fe-d069f0230b55 | -6.9703 | -42.89909 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 86b31f93-7003-34fb-a866-25fb0d5ba653 | -5.18295 | -48.07891 | 2025-06-03 04:17:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b3bcc3-15b0-3776-9e31-a63854da979e | -7.01102 | -44.59349 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d210512a-e0ed-3dd2-9986-bd10dd6ab453 | -7.68674 | -44.57248 | 2025-06-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2356bdba-7236-3e12-a610-c6159de33068 | -7.43399 | -45.42089 | 2025-06-03 04:17:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a905e647-8820-3d54-8464-f2f2a6afc5a7 | -7.69344 | -44.57293 | 2025-06-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 629912b3-3bcb-3c9d-a1aa-ba3d282ea196 | -6.91405 | -38.56036 | 2025-06-03 04:17:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 23ce0afe-73bc-3286-9413-90e387cf7d30 | -7.21861 | -43.12923 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5e1553b8-4e47-3c50-9e8c-d55dc57cdcf0 | -7.81917 | -46.57474 | 2025-06-03 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d5b5871-497e-34a7-acfa-517d6e98965f | -7.47776 | -47.05777 | 2025-06-03 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcbd4c52-9d06-3897-af00-c6357975158e | -5.76838 | -43.63962 | 2025-06-03 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e45c8f3-479a-3068-8dc0-4bebc4ff1c81 | -7.19869 | -43.55961 | 2025-06-03 04:17:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 30b6a15b-98dd-36d6-b918-268861c55b0b | -7.19684 | -43.55951 | 2025-06-03 04:17:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 44cc0a4a-e20c-3083-87f4-7d15ccfef7ef | -7.43454 | -45.41741 | 2025-06-03 04:17:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 629f4ca7-0bc4-359c-b0c0-7960d32cba20 | -4.8066 | -45.25753 | 2025-06-03 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e365263a-a8a1-38e6-a382-1f1c04b39b4b | -8.07125 | -43.11731 | 2025-06-03 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 8f9e9a32-d1a8-3682-bf43-437847038410 | -5.78178 | -43.61623 | 2025-06-03 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cac6296a-1335-3313-8742-7a016846b229 | -7.01651 | -44.58016 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8af223aa-1fc3-3196-b1a5-d5cbe9e6e890 | -6.97274 | -42.90694 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 69c036a9-32b2-3d38-968b-5d238fe1fee5 | -4.80604 | -45.26105 | 2025-06-03 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bad09850-2221-3a75-a2bc-52adeea84b64 | -7.86579 | -46.86938 | 2025-06-03 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc2c8258-0c9d-38bc-a55e-28dc67ae6541 | -6.96972 | -42.90281 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c6833391-86f4-3015-bf3f-7a88d3853154 | -4.82081 | -44.35362 | 2025-06-03 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5d41efb-9045-322d-99f3-c492f9a6b49a | -5.78124 | -43.61975 | 2025-06-03 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63032f3b-868a-33ca-9054-b9c8cd78af7d | -7.01706 | -44.5767 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 68d290f2-e536-3f9a-900f-518918e5f153 | -4.81604 | -45.26261 | 2025-06-03 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e836221-16fc-31b4-b824-80f299cf3e2d | -7.07016 | -44.92912 | 2025-06-03 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 810a26ee-bbe4-3755-bd89-ad4190c1b4a8 | -7.3752 | -43.11472 | 2025-06-03 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 812ff8ad-d413-3fe7-abc4-15b2d2ce70a4 | -7.6906 | -44.56953 | 2025-06-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 408db72b-116c-390a-8eae-d90de7e3b6ef | -7.8678 | -45.98318 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ec8335f-e642-3c4f-9416-8ec7bca873fa | -7.70929 | -46.31551 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a5d2206-0155-3565-9050-2f22dee8e471 | -7.37453 | -43.11533 | 2025-06-03 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af242def-a2da-37fa-9e31-b1a23869a23d | -6.97331 | -42.90324 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 55acb68b-2b94-3b90-8559-9f04375f6f8d | -8.07867 | -43.11462 | 2025-06-03 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| c88d19ac-de3d-3052-ac44-e667ae15c5f0 | -7.54534 | -43.30197 | 2025-06-03 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 609fff53-8fa3-3942-a3eb-eeb0519ceac8 | -7.22654 | -43.12294 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f9393326-0c1a-3a57-8aaf-088ab4a4cd6c | -7.00993 | -44.60041 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2afce200-651a-331f-bd70-94ea270b42aa | -7.69114 | -44.56606 | 2025-06-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 459e3aea-4cb0-3b8d-8dda-2981736e8d66 | -7.20259 | -43.55656 | 2025-06-03 04:17:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3fa6c939-9ff5-32e0-b7f0-8cab526baae7 | -7.56115 | -43.28952 | 2025-06-03 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98ad4715-9096-34d5-be4c-2cc084444574 | -7.22541 | -43.13028 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3e158b08-239d-331c-938f-73d890efc575 | -5.84967 | -46.2359 | 2025-06-03 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0f410c4-77bd-38a1-a9b6-8c13a8fdd56c | -7.08151 | -46.55829 | 2025-06-03 04:17:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60519216-dbf8-3a20-b486-99085cce7a6e | -7.56059 | -43.29316 | 2025-06-03 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbb3a63d-8b28-3bbe-8166-de77b4108534 | -5.83302 | -46.36123 | 2025-06-03 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e7edd38-34fe-340b-8cd0-03a0145513e2 | -7.88315 | -46.22245 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ae7f2d6-45ad-3c4a-b027-2bcc75422ad3 | -7.27672 | -42.91101 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e4262fb-a77a-3bef-8ead-e63f9307b97f | -6.54371 | -44.02171 | 2025-06-03 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9dc687d-df9a-3f98-955d-4bf8b723bab4 | -9.8711 | -49.33921 | 2025-06-03 04:19:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 655ea6f7-6a01-39e3-8c27-27e1b519a73b | -11.57437 | -47.44733 | 2025-06-03 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff75c9dc-1679-33d6-b006-f1a8cb0f5f18 | -8.9083 | -50.04436 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 321ca5e4-89ee-3186-963b-ddf6e52ff4c1 | -9.66922 | -48.7168 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3fc6b24-145d-3136-961f-26e0f48dcfe8 | -8.47348 | -46.50045 | 2025-06-03 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c08e1a8-6fe7-3bef-80fb-9e456c153fd5 | -11.91623 | -54.81869 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91d2d4f0-8ace-39b7-98e8-4ea05db5d920 | -9.60996 | -49.02339 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecfdf530-71d9-3fda-99f1-58670ccbe0fa | -3.89055 | -42.54666 | 2025-06-03 04:19:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d20539a7-6425-352b-81a9-b741dfb421b3 | -12.283 | -50.11174 | 2025-06-03 04:19:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b44c06a1-ac4a-3c02-ac92-cfada8c62f6b | -12.29758 | -43.54613 | 2025-06-03 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b72dbef-ee52-37da-a8a9-52f194114c25 | -10.67279 | -44.37812 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bbe639a-0337-3b13-aff6-3e2f77bd7ccb | -10.24174 | -52.22241 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45e42241-c44f-3521-be89-d0dd518591a2 | -8.60277 | -51.57344 | 2025-06-03 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2671ab30-e88a-3d41-bc69-17f8a0fa5785 | -11.905 | -47.44099 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2f80770-0133-397c-a12c-3c7b60b99933 | -12.19339 | -54.26244 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3c3253a-f613-3883-938e-6e102d1fb32f | -12.64173 | -48.17395 | 2025-06-03 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2042261b-fadd-337e-b624-b6127dceeb2d | -12.29681 | -43.54255 | 2025-06-03 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c23963f5-64e2-3f66-83d7-c7d7205c3954 | -3.03935 | -49.42582 | 2025-06-03 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2c639665-8bf3-3a44-b47b-5618a1a5f198 | -12.66975 | -58.21675 | 2025-06-03 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb605dbe-edd9-3b01-9b9e-ad36dfe57105 | -9.12916 | -47.579 | 2025-06-03 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 953c205a-f193-3103-b8d1-5ce491bdb961 | -11.92081 | -54.42129 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f857d3fd-b99f-34cd-a3bf-4836234fcdf6 | -12.16761 | -54.26318 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc137c9b-b135-3a1e-b737-0f30439a685a | -10.13933 | -52.13688 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8d7b48ac-fcb5-339a-b7b1-b5d7747aa314 | -12.09649 | -54.66534 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21d75e54-aaba-30be-9e1e-4a4aa2b1d64e | -8.60279 | -51.57467 | 2025-06-03 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
