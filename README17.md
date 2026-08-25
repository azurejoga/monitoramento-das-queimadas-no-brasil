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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d1f8793-c307-3ef6-b677-e47b12b0a6f5 | -7.26045 | -45.37628 | 2026-08-25 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 25f88480-e4d7-3e25-a6af-df187dda6bee | -7.44641 | -43.09703 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 83a938e0-ec02-3ffc-abe8-af7641481985 | -7.13095 | -42.78772 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 78f9c731-0cfb-3bb9-9b31-321855b5f417 | -7.43547 | -43.11557 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 05d46878-d020-3192-a7fd-221f55f30d49 | -7.28588 | -44.08227 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4e9a55c7-aa4c-3a6f-98eb-bc9833ef46ce | -3.96905 | -41.52056 | 2026-08-25 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dfb30df1-20b4-31a9-8d45-f97bee6a9c0e | -7.25618 | -45.85524 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f57818db-b417-3411-8748-1f71901d272f | -7.293 | -45.36369 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 9c4223e7-0a6a-3bf8-b6f2-bf2e482b6c55 | -7.43973 | -43.12529 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2802698a-ed8b-3b16-b813-997c0c75d290 | -7.24895 | -45.37474 | 2026-08-25 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02390345-ac1c-3231-9874-a409be6233b6 | -7.30674 | -42.97326 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8d510a0e-0156-3710-ad31-bc56e9e7c82e | -7.28236 | -44.07965 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d9058c3-45ab-320d-a0d4-0a226b8e4d84 | -7.18721 | -42.74279 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 900df68c-1783-35f3-ae69-1e51c2b70cda | -6.96934 | -35.2174 | 2026-08-25 03:30:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f2a0896b-decd-35ba-995e-bb4f685ff7bb | -8.08616 | -44.64074 | 2026-08-25 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6bff8b57-4d55-313d-9f51-44b9c0a09999 | -7.26371 | -45.3707 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d33d28fa-0940-369c-a932-0435d00eb434 | -7.25369 | -45.37505 | 2026-08-25 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49b49365-c1c8-3970-aed8-6da416042aa6 | -7.90152 | -46.36184 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 918bcc70-03f3-3277-85cc-1ce3fe722c5d | -7.28746 | -45.35605 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e3c6c609-7a13-3f77-8153-1275e4a4cd90 | -8.07232 | -44.64399 | 2026-08-25 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 329e8e9d-2404-31a3-b7fc-96df19a3e1f9 | -7.44567 | -43.10114 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 64ce9016-c3b9-3afe-82c3-8571d7f8ef8d | -7.19728 | -42.7528 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b94295c-babe-345d-890d-f0aa2df6a743 | -7.44182 | -43.12264 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 798586c0-0584-3dd2-8357-fd4aaf869faa | -7.43384 | -43.12425 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 90997ef4-ed53-3609-87e4-849c5394d04d | -3.97124 | -41.52115 | 2026-08-25 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fce93eeb-ffb2-3f01-86ce-07ec08c53166 | -7.6394 | -42.72757 | 2026-08-25 03:30:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ee1742c-2e64-3495-a5d1-7e35851391f0 | -7.25576 | -45.37574 | 2026-08-25 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0aeb0405-6f92-3c95-822d-4c0d29f8c0a6 | -7.25458 | -45.38192 | 2026-08-25 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0385fbf7-f5c3-3624-8a8d-b67d7a26cbcc | -8.05365 | -42.04665 | 2026-08-25 03:30:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e2c42a5-9edc-3d49-bf76-2c4da63a856c | -6.95122 | -42.68928 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2026889b-7c68-3ab4-89b6-2de33881447d | -7.24849 | -43.12565 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3b2f469-362d-34d8-8ebb-2a995a027d09 | -7.25746 | -45.84861 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6b15e847-b248-36e7-9cfc-4766950c2f37 | -7.43515 | -43.12599 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| deff1c39-b6ed-35ea-b80f-ac4cc668f48c | -4.71608 | -42.77201 | 2026-08-25 03:30:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c05c2a59-e3ee-3f26-9ee7-629b1bfa3a65 | -7.42877 | -43.11887 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b2f6273-ebe9-31fd-af8f-9edc414f21c6 | -7.24927 | -45.85379 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 75fb34da-d4c7-38a5-bbc0-b5368fc8027f | -7.43617 | -43.08652 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 35da0919-3d31-371f-90e2-e38c218c368b | -7.43827 | -43.10859 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5fad663a-99e7-30b1-9c3c-2aa6439cda13 | -7.43749 | -43.11292 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 214b855a-933e-306b-a2b3-1c80b73c0f07 | -7.43709 | -43.10691 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| efa484b9-9971-332b-97cd-ed47b25318d5 | -7.27959 | -44.08129 | 2026-08-25 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 86c98083-d417-3322-b658-a28b0e9a11fa | -5.92121 | -43.64248 | 2026-08-25 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dd3fb6b9-b075-39eb-a7b8-cc8239e11e54 | -7.28053 | -44.07631 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6dcde8a4-56b1-300f-b69b-f1b14ac34a4c | -7.26437 | -45.85004 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 328a7d5d-ea8a-3d14-9610-dd4060b6d337 | -7.25869 | -45.84805 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 66e6cec8-f133-34c3-a85a-e940859fb92d | -7.14899 | -42.75387 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 040a783c-d0f4-31e3-a62d-27b8d01beb43 | -3.364 | -42.15921 | 2026-08-25 03:30:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ea452a34-3d35-3d4b-be13-c44d13528682 | -4.95129 | -42.98622 | 2026-08-25 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f30a68d-6dd3-31d7-bf83-866e120dba32 | -7.2493 | -45.85986 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e256fea4-f59c-3ae1-b88b-8a5e0c5b94e7 | -3.89722 | -38.37549 | 2026-08-25 03:30:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7658223b-fb35-30ac-bbc1-a4c30b05fcb1 | -7.27162 | -45.36589 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 937a578b-f6a0-3c7d-9a86-72ff0b7895e7 | -7.27046 | -45.37196 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 07da6fdb-a392-3752-9800-41ab63a243a0 | -7.44454 | -43.09954 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb020c4a-09b4-35f8-a081-59f8601659fa | -12.98152 | -39.66513 | 2026-08-25 03:32:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8bdea3d5-3099-3113-9d0e-5823a190efd0 | -11.98804 | -45.92278 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f53a726e-6447-3c57-895e-7da8362fe228 | -12.41371 | -40.92405 | 2026-08-25 03:32:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca005f8a-adc6-35f4-a4a3-2ed89bb88847 | -12.75342 | -46.45253 | 2026-08-25 03:32:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0781651-0795-3c50-8a88-96cc467fcab6 | -9.46431 | -40.33125 | 2026-08-25 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8e817aad-6c89-3c1e-a3de-17a22bab96b5 | -12.25608 | -43.11454 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 79c00e53-3032-349e-b182-d8a12e76b38d | -12.71965 | -43.2006 | 2026-08-25 03:32:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7fe88f5-6105-33da-888b-4e66ecbac94a | -12.73745 | -46.47328 | 2026-08-25 03:32:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 17af207a-a7f2-30cc-a696-86562bc72661 | -11.97201 | -45.9023 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbd08b64-ecce-3196-bcd1-0eae1029dd2c | -9.33149 | -40.30405 | 2026-08-25 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4fea9d25-2f25-35ea-818d-e161f8f3f72c | -12.77774 | -44.25822 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1a547fd0-4391-382d-9c4b-2b6f3b6cdfbe | -12.78184 | -44.26771 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 61377061-153c-359d-b56d-e8808e5e64e1 | -15.68028 | -42.4703 | 2026-08-25 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57e604d5-45b6-3901-acbb-6cdbf591bed2 | -12.77115 | -44.26122 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f2c036f-5a08-3379-8823-b48bb5bdf13d | -11.44064 | -44.55173 | 2026-08-25 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5986570-eb7f-3b54-8351-296d5eed7fd6 | -11.43314 | -44.52657 | 2026-08-25 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 959c5a86-5347-3b64-978a-802f0439a98f | -14.6224 | -42.53283 | 2026-08-25 03:32:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1a5d539f-2c79-33dd-afe8-0ad865b7d36f | -12.73874 | -46.46694 | 2026-08-25 03:32:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22190fcf-cb76-355f-8707-ad732ff7e40b | -12.77198 | -44.25707 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be0325ac-eda2-362b-bdea-5c69bc1e23b5 | -11.13914 | -44.47073 | 2026-08-25 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f5824710-b6ce-3e09-9ef0-87b221f951fd | -11.43464 | -44.55053 | 2026-08-25 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1baec5b8-7e72-3237-b4e6-e4d8fde35a75 | -13.4476 | -43.8479 | 2026-08-25 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40ea19a5-8c8f-3a46-beb4-c6b15d742e49 | -9.70082 | -46.05159 | 2026-08-25 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 606982d6-fe61-3ede-96fe-df9ebefa2d19 | -10.37691 | -45.06057 | 2026-08-25 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 52693a3b-8861-31bc-ad0e-fcbb7f8b11f5 | -12.2615 | -43.11558 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c3dd09bd-77b7-36af-a036-5414671740a2 | -10.37063 | -45.05925 | 2026-08-25 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| e953c2ef-6728-3da8-80c4-dfecbe9de046 | -16.25143 | -41.77657 | 2026-08-25 03:32:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60251aa9-cbab-34ea-80ce-ee4508320095 | -12.75462 | -46.44682 | 2026-08-25 03:32:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 955ef768-eacb-3a90-a2f6-090b4f35a815 | -15.67741 | -42.47147 | 2026-08-25 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 559f2af8-ac1d-3fdc-ae82-69fcadd5cfd3 | -15.67925 | -42.47566 | 2026-08-25 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 151b7e2b-4090-38ae-a5d0-dd7c5910cde4 | -12.20516 | -43.17373 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4dbd0676-bad4-3cfd-a133-658d139ae2fc | -13.10206 | -43.36777 | 2026-08-25 03:32:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9246f47d-20f6-36a6-9365-05fe8aea65a8 | -9.69451 | -46.05794 | 2026-08-25 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 377c4055-f72f-320b-9ad1-00a98bd36703 | -10.37162 | -45.05419 | 2026-08-25 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 173f2370-9f1c-317a-89fb-5767b1114559 | -11.98706 | -45.92767 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69e8358c-f9b8-3fd9-ad7b-946cf0c379cd | -11.98818 | -45.92225 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfa53983-1e17-3384-9d59-f5cf0fb29687 | -12.77608 | -44.26654 | 2026-08-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 325a1136-a47b-3985-97ae-e90a102838f4 | -11.81093 | -46.66341 | 2026-08-25 03:32:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38238a0e-7cca-3bb8-81de-31d236722c9a | -12.20781 | -43.18903 | 2026-08-25 03:32:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 48b7dbec-bbe6-3ebe-9d39-c84b6182fca6 | -12.45124 | -43.40227 | 2026-08-25 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 064ed909-45ff-3207-8a93-246504557767 | -12.61328 | -44.63152 | 2026-08-25 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 658bec8e-403e-3b56-b87b-217cc558f5a2 | -13.09124 | -43.36554 | 2026-08-25 03:32:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cc98c13-569f-3003-9353-c895bccbce71 | -11.77527 | -47.24388 | 2026-08-25 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db76dae1-05f7-3c09-803a-cca919ca3a65 | -11.88464 | -43.82038 | 2026-08-25 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0cbbfaaa-822a-374c-ac55-1691c72ccbfb | -11.97734 | -45.90914 | 2026-08-25 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d6af3c1-3c91-305e-af62-56a15dc9fa38 | -16.02091 | -42.98472 | 2026-08-25 03:32:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03a73e9d-4279-302b-9de6-35855385eac0 | -13.09665 | -43.36666 | 2026-08-25 03:32:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
