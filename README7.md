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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3201629c-c2e3-3c6b-aea4-0c15a9b8f87d | -5.79253 | -43.63019 | 2025-07-18 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4202bfba-97e0-380f-90b1-b2cfffbf9b12 | -5.65797 | -43.72057 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 1a00e21d-79a2-3405-b6f1-0f5b6db4359d | -5.66432 | -43.71764 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0be7f947-a68d-39c8-a55c-43325dc89ff8 | -4.79716 | -43.22153 | 2025-07-18 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 73f7ce29-0571-3d4b-a15b-8c2137b9e1b2 | -5.36372 | -45.12226 | 2025-07-18 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 962174c9-0897-3786-9e06-ca7968ee5119 | -4.90509 | -37.29761 | 2025-07-18 03:34:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5ad5eda-9df0-3a9a-bd72-118584c7b33c | -3.8029 | -43.22355 | 2025-07-18 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98db7385-fb71-32b1-8d65-45323032503e | -4.64536 | -43.1202 | 2025-07-18 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 985e8c20-5abc-3332-a731-10be7a531dc2 | -5.65046 | -43.70827 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| e21a9352-8c9f-33ec-9838-fce472c855e9 | -5.6593 | -43.71283 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 8c509882-38e2-3f5b-91e7-e7d625517c73 | -3.80533 | -43.22285 | 2025-07-18 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2666cdd-7f0d-328b-8ce4-818fa6a3ab83 | -5.65405 | -43.72086 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a6c76e99-1efd-314a-bf9b-c83148c69b4e | -7.70315 | -47.28895 | 2025-07-18 03:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4385ca1-4994-3188-a37c-1fef325206d9 | -6.95783 | -43.75709 | 2025-07-18 03:36:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c701ebb-341a-38bb-9d67-ce2932eab942 | -5.73081 | -44.50494 | 2025-07-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f248259-08d3-31ec-8bbd-fd3597b3a78d | -8.09413 | -43.15259 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 206bd651-8cbf-31f0-a589-3a5c361547c8 | -11.88122 | -40.95359 | 2025-07-18 03:36:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| beee1975-941e-31d1-9251-c61d126f95ba | -5.91441 | -43.47142 | 2025-07-18 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51005c5b-3565-32e2-bf69-ba2a278f863c | -5.73001 | -44.50949 | 2025-07-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8abe2e22-9f9b-39fe-ad72-a7a0414fd745 | -6.03605 | -44.05399 | 2025-07-18 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e6a1e15-2cae-3b2d-923b-e68fd5291863 | -6.69104 | -43.18595 | 2025-07-18 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5f231f8a-8ec3-36e0-a83f-595b046a7a71 | -8.10521 | -43.15129 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7988284e-9953-322a-bfa3-af459ab6c233 | -9.53688 | -40.32627 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 90055529-59e3-355b-b89d-e081f837d6d1 | -6.23049 | -42.0216 | 2025-07-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7e65b7dc-b759-3036-b09e-49fc3872d870 | -7.00437 | -43.75421 | 2025-07-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 408d6b78-0f6f-35b5-bec2-a0a7065a42c7 | -5.8423 | -44.10267 | 2025-07-18 03:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab1d97e7-b384-3385-bfdf-db3569f8ed06 | -5.78181 | -45.07412 | 2025-07-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 70b78330-0a80-37b2-bd83-83fb00941c94 | -5.84982 | -44.97516 | 2025-07-18 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b451bc98-4b1f-3ba7-a4b1-814b62e93bf1 | -7.27934 | -44.21895 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 183379a3-fea1-3b6b-a0a6-14e51ff72ed6 | -11.87767 | -40.95357 | 2025-07-18 03:36:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86e5bec8-9479-3584-b612-d3a57ccb1d93 | -6.72679 | -44.33435 | 2025-07-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1881b008-da8e-30a6-a069-a13ba6c2a39c | -8.08303 | -43.15396 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| ae7685c9-0d0e-3464-85af-9027ab9da3fd | -7.58412 | -46.30849 | 2025-07-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2df4904-1820-318e-95d2-13c8565bb7cd | -6.9333 | -43.80833 | 2025-07-18 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9afdb37-d25c-362e-9f03-b9be0b043671 | -5.73377 | -44.50304 | 2025-07-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f4d87bf-fb7d-38c7-8845-7902c03eea5d | -9.79799 | -47.74155 | 2025-07-18 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f81486c6-486a-3d66-8ee8-686814ec6692 | -7.59164 | -46.3041 | 2025-07-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f34035dc-9824-3ba0-ba02-4c82f8c02f7d | -7.27864 | -44.22288 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c2d55c5-299c-3bda-92ae-0871b57b1526 | -7.05559 | -42.98418 | 2025-07-18 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b822824a-03a3-3de3-89da-30e338b07299 | -9.85992 | -44.70739 | 2025-07-18 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0962885d-e014-3aae-8382-ea67ff1a9125 | -6.94799 | -44.56504 | 2025-07-18 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82c8078a-7143-30db-8bbe-d0e999df857b | -7.70192 | -47.29556 | 2025-07-18 03:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4b0ad0e-e5a2-3513-87fb-3b119e7acd09 | -5.85683 | -44.97147 | 2025-07-18 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83958ac8-6716-3231-920e-3743e0ce3370 | -6.68504 | -43.18838 | 2025-07-18 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 27b4327e-01a1-39bf-b01b-64b4ccf7a965 | -7.2369 | -42.93356 | 2025-07-18 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6577abfe-6328-3778-865d-524bda5805f1 | -5.91508 | -43.47628 | 2025-07-18 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bb5584f-83a2-3c86-bac6-f8ccb399efbd | -8.10579 | -43.14801 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 910ac404-0448-323b-967c-b09e5554b63c | -9.53618 | -40.33026 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 73caa1f3-8445-3266-ae75-7fa35fed5b46 | -8.08947 | -43.14833 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e467530f-3a91-3389-95a3-afb2436d5895 | -8.09938 | -43.15357 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 59a00e45-decd-3a42-8e78-b5459078a8ee | -9.5034 | -47.57066 | 2025-07-18 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47d68727-9dbe-304b-a731-dd24d758b88d | -8.64609 | -47.75856 | 2025-07-18 03:36:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10e05dd7-758a-3a76-a35a-0908793f3203 | -7.34941 | -44.1979 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b73c958-f83e-3345-aac1-2c1df394f40f | -6.94949 | -44.55678 | 2025-07-18 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f6dda521-3b00-34c5-a618-a4915782289a | -9.49785 | -47.5633 | 2025-07-18 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1e6f5531-fada-3b06-9052-a43130d2d16f | -7.49451 | -37.28722 | 2025-07-18 03:36:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6b1c0e61-10be-3290-a6d1-08e946b224ee | -9.60077 | -40.60614 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| f0c3d7d8-0a23-362a-9a8f-8ba0da479292 | -9.7631 | -48.7561 | 2025-07-18 03:36:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 48b071ea-5cea-3d96-a97f-e45a54b4855c | -5.78801 | -45.07508 | 2025-07-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c1f2f3bd-6e7b-390d-8d78-792ca3d5e47b | -5.73295 | -44.50755 | 2025-07-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc1dbc7a-c57c-364c-9b64-01ae17863a8a | -9.58782 | -40.36022 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 76dbe5e7-1e81-388b-9377-7ca11b413ef6 | -6.72698 | -44.33468 | 2025-07-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15094acb-c65b-3890-94c1-546405bf9fb7 | -7.18594 | -44.0729 | 2025-07-18 03:36:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f85aef36-bc5e-3d60-8d1b-086eec2d88d5 | -9.80598 | -47.73682 | 2025-07-18 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69594963-e618-35ad-b2ef-6034024f0f32 | -7.06028 | -42.98854 | 2025-07-18 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 269185ac-403e-31a5-b67a-ea1abf534126 | -9.76865 | -48.76544 | 2025-07-18 03:36:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51397625-142c-3b31-8c5a-d67cca45ff55 | -6.98849 | -45.62024 | 2025-07-18 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5cc6bc8-0adf-396c-8fc8-b9653edbc68a | -11.74841 | -38.51859 | 2025-07-18 03:36:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60d4bac0-c55c-3339-9f24-8f2f0dfed2cc | -6.55203 | -43.61711 | 2025-07-18 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5aa0f62-ce78-32d2-9cd2-e47c92a32d95 | -5.83651 | -44.10151 | 2025-07-18 03:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31ce6452-655a-35c7-91db-a3d36c431265 | -9.62832 | -46.66624 | 2025-07-18 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5fadfb4-a4e1-3655-9ba9-51de9d83695e | -5.91574 | -43.47248 | 2025-07-18 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe3003f2-921b-3001-8d85-2f6e0c4de846 | -11.77823 | -45.22274 | 2025-07-18 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ad529dc-63b7-3cca-b045-2a4843bdbc4c | -5.78714 | -45.07994 | 2025-07-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ef5f191-753c-3dcf-a068-0d6adf743d93 | -7.59066 | -46.30928 | 2025-07-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eeb33603-0901-3131-b671-9a8718e015a7 | -8.08362 | -43.15067 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| b500efb6-e9ad-33db-b8cb-82fbb5c2065d | -11.88191 | -40.95439 | 2025-07-18 03:36:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12824b01-ebec-3a77-98e7-5fa1b0ded773 | -5.83722 | -44.09758 | 2025-07-18 03:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18c95694-7487-30fb-b679-fafee3f2d3db | -7.93816 | -43.86105 | 2025-07-18 03:36:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c02db19-153f-3cec-be52-16dd44168d32 | -5.91373 | -43.4752 | 2025-07-18 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbc6150d-037e-3638-9cd2-858c7f3e3b7c | -9.5046 | -47.5646 | 2025-07-18 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eceacbe-65be-3d3e-932c-f915b7008558 | -7.3437 | -44.19693 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0b561876-296a-3215-8fc5-92d63a737f8f | -5.91443 | -43.48006 | 2025-07-18 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d656dfb0-5c43-3f82-8e64-6a27e92faeee | -6.94874 | -44.56089 | 2025-07-18 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33ac7df2-5a4d-3af9-b54e-1a3a2331ad5e | -6.96543 | -43.74693 | 2025-07-18 03:36:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ee75984-fc31-3a82-bc18-9938734d8eaa | -8.88627 | -44.78965 | 2025-07-18 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6c93bdf0-fd49-3583-b82e-8dfa4043c04b | -6.55134 | -43.62096 | 2025-07-18 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99670b29-178b-33a2-995e-bec407769076 | -8.07777 | -43.15304 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| f7b443a7-4f94-3575-8040-979172b03c8e | -9.76149 | -48.76395 | 2025-07-18 03:36:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e740a702-cb56-3266-b8ad-b9814c034652 | -9.48512 | -40.39592 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 42cdf5e1-a55d-3edf-a6c8-034638ea03ff | -5.85598 | -44.97611 | 2025-07-18 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd3f04a-eb1b-33cd-915c-4d220995b924 | -7.28502 | -44.22017 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9e38541-d846-3d73-9817-612e240009ca | -11.94277 | -40.61609 | 2025-07-18 03:36:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1555a65b-a224-35b5-b610-071984095334 | -9.8592 | -44.7112 | 2025-07-18 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b7cb36-6b50-3654-a14e-f9c9e17f0e9e | -11.7846 | -45.22009 | 2025-07-18 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e1c4d6d-1861-34af-b0fe-c401422e1cfa | -10.0619 | -46.67254 | 2025-07-18 03:36:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76d78cf7-c0ad-328e-a527-0d390508831e | -6.99567 | -45.61641 | 2025-07-18 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4215a48-f347-3ad2-9d26-15e341fe2cc4 | -6.72754 | -44.33027 | 2025-07-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc0542bc-350e-33e9-a017-dc046f8df3a0 | -9.53759 | -40.32228 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 888ca3fd-265f-340d-9381-9e2f8f3d0d6a | -7.0667 | -42.98304 | 2025-07-18 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README8.md)
