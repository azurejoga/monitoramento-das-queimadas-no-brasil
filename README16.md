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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7834fb42-37fd-3822-8887-2e40350ccfb1 | -5.85925 | -44.71177 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fa1be26-2115-391d-8767-dda0c40fd7d5 | -6.07524 | -43.09086 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0abff9df-6402-3b83-87ad-36e758140b3c | -4.47711 | -46.56279 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 59d6dab3-6a19-3493-a014-e126ba861e9b | -3.22855 | -50.65374 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb80f2bf-915d-329d-99bf-14212127723a | -4.67489 | -46.52437 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f43c7c70-cdbe-3203-af2f-b456fb38a93a | -5.64906 | -39.6365 | 2025-10-31 04:06:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cc8f7833-8e82-36e7-8a8b-2d7dae0ca786 | -5.03892 | -43.61656 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 3edc1583-34f1-35a3-a5d9-57ac653f8d7e | -6.90015 | -42.20013 | 2025-10-31 04:06:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2766e4b6-4a34-3ab0-a0b7-1bf74c7d39bc | -4.13088 | -43.9826 | 2025-10-31 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33328fa6-14c5-33b5-9279-c57b45033253 | -5.85119 | -39.51016 | 2025-10-31 04:06:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 799f733a-6f57-3e5b-b156-80a5e8b38928 | -5.0534 | -45.85548 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0763b5d8-06a9-3590-8f2d-a40c2c2778d1 | -5.69712 | -43.15227 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b99b683f-f237-3d1d-bfb5-abe89639cf16 | -7.31133 | -44.97797 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 25f4a70b-2efc-39aa-a90b-b95eb5907e6c | -4.80512 | -43.0285 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| c0bcc69b-4294-3d70-8bb5-a7342d08a402 | -6.92609 | -42.25073 | 2025-10-31 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 428a5e06-29eb-3c8f-88dd-2d35d8525940 | -7.18167 | -43.79685 | 2025-10-31 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84fd9e1d-f078-3d54-823b-17c8004229d3 | -6.22135 | -43.94314 | 2025-10-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6e4dff8-6924-3085-878d-8c5660ede867 | -7.03924 | -41.47296 | 2025-10-31 04:06:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c540ff4b-61c2-3824-94b0-bf71cbdb06b1 | -6.52608 | -43.71296 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9070bdf9-2486-31e1-abb6-5926a196734f | -4.64746 | -46.3184 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0531518-3235-3a12-a1f0-f0fd37b7d01d | -7.54184 | -44.04564 | 2025-10-31 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e68a080-08e9-30b2-aed6-2b8776b474fb | -5.71565 | -44.53498 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fcaec16-8b2d-3634-a440-49fb03b96012 | -5.28943 | -43.94655 | 2025-10-31 04:06:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 996b1cbd-9faf-3307-97d5-f9b7b77fdd93 | -7.43567 | -44.25594 | 2025-10-31 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1da0b662-2f45-340a-bb4b-8f7233738afc | -5.36505 | -45.52157 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07d3745b-2ef7-30a3-833d-a446093b3a65 | -4.48779 | -45.18885 | 2025-10-31 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85d3c8d5-6087-3766-b097-8c87c938e39d | -5.33935 | -45.36584 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dc0e5a1-8beb-3400-9e72-38e20abff0a7 | -5.03606 | -43.6121 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63f10da6-d123-38eb-b461-997bbe4815a3 | -3.43658 | -42.50492 | 2025-10-31 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37d53d71-d126-34ba-ab29-26a28f7d6998 | -3.01942 | -49.44955 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| eefa09d3-cca0-3d2d-a031-873e462f0d34 | -8.02386 | -40.93292 | 2025-10-31 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 33bf4321-af7f-3ab1-b5b4-8477b7df40e5 | -5.28333 | -45.41933 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c440236a-3c48-31ec-861a-460ff66d2591 | -5.1524 | -45.27684 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 649df815-b757-3195-8971-6591e3306499 | -6.03296 | -40.2631 | 2025-10-31 04:06:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 715a60fa-6c99-3bde-84e1-f09140ea723c | -2.31679 | -48.58227 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b74c40d-691e-38b6-9e61-9e870d9f6b38 | -5.03542 | -43.616 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 3ca4a0f7-21fc-39ae-bb63-58f958cbe948 | -7.59214 | -43.56181 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a7bfa1a-372e-3772-b4f9-2ea7cc319b7d | -5.78783 | -43.73627 | 2025-10-31 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3bade88-32ac-3a9a-8e05-39c8385e3687 | -3.42893 | -44.45127 | 2025-10-31 04:06:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef6b371c-ca5c-3e40-ae70-d469c03ea6f7 | -4.75584 | -45.78405 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b946f32-5972-3631-8b2f-85f4ef53dab7 | -5.50441 | -46.38497 | 2025-10-31 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03ca8ee6-9cfd-3904-9a13-07e338fe6409 | -7.62345 | -43.56299 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae2e6bde-12bc-3f7d-9a33-292b17997605 | -3.52514 | -47.55505 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 359fdf38-c852-3521-a455-e4e0ab60710e | -7.33574 | -42.73068 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fa0845d2-fa70-3068-8498-bde756489acf | -5.25455 | -44.60516 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbee052f-f29e-328f-8ccc-fef1ee9f197a | -5.03702 | -43.62075 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| acaea3dc-954e-39a0-b17c-602a2a98a083 | -5.80278 | -35.58597 | 2025-10-31 04:06:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc0effa7-a6ac-3371-84ee-72c8ad7b1df0 | -3.60155 | -50.62745 | 2025-10-31 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7b28b20-0b72-35b5-b49b-401a94126e72 | -5.27742 | -45.12988 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cc1e228-d4ae-31c0-8caa-ca712ed3b9b1 | -6.57287 | -41.58659 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9756a8ba-f24c-32c1-a843-64ba205bdb77 | -5.75841 | -45.87165 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cab60042-3943-3acc-9189-40501862fc4f | -5.22907 | -46.1312 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9931a6dd-9f4f-3e12-bc40-ecff3648b57b | -4.57009 | -46.94471 | 2025-10-31 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11a9ddfc-396c-344f-972e-78cd7cbdd339 | -7.65228 | -42.72746 | 2025-10-31 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6dee12e-349d-31cb-83cf-12b7063b676f | -5.65531 | -45.98309 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d08eca9a-1112-3e18-a6ac-7a56f8cd11ae | -5.70713 | -48.8888 | 2025-10-31 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 39639944-3c87-3bee-84f6-29cbb146c1bc | -7.82757 | -40.36472 | 2025-10-31 04:06:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47484f88-9763-3e01-8b19-7fa1dc75c9c1 | -5.80198 | -40.82823 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b84b465-7634-3d70-adb4-ccaffa20a539 | -5.88637 | -43.19732 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 103de4a3-0c24-30eb-8ae2-b0df951c6144 | -4.30809 | -46.6917 | 2025-10-31 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be567abe-3cb0-3062-9448-3fbb344af8c2 | -7.03593 | -41.47244 | 2025-10-31 04:06:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de813135-758f-3bac-9d58-695cb9ed61f5 | -5.28449 | -45.42213 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cdfb798-ed58-3c1b-ae7e-a1b20a7c8246 | -3.2881 | -51.9147 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c76f6157-d1ab-3748-bf2b-6557a7a1e255 | -3.48218 | -46.02179 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aebe1a40-d5ea-3335-94c3-7b5ac8440b98 | -4.85272 | -42.73407 | 2025-10-31 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3c024ef-bdd7-3eb3-9c3e-aa82b99074ee | -4.67302 | -46.52478 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34268a7a-1aac-3c54-90bd-d58835981e71 | -5.53836 | -41.70194 | 2025-10-31 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7894da32-2049-3654-8b78-04d26e4a50a1 | -4.56763 | -45.68169 | 2025-10-31 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb27917b-8bfc-3169-9daa-9b5b9d12b65e | -3.5446 | -46.43168 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0623f35-bd4e-3017-bf8a-7c171dac7ce0 | -5.05026 | -45.84991 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43a59890-646d-37a4-bc32-6a1e17a4a922 | -5.32965 | -42.66813 | 2025-10-31 04:06:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca7bb570-6d30-33dd-8072-984596b69b83 | -2.31088 | -48.58717 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8314dbb4-433e-3b81-81f4-416ad960414c | -3.98707 | -43.41953 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6a5a12-27f8-395e-a196-4ba15c04d08e | -5.41875 | -44.58665 | 2025-10-31 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8898aa91-c9d3-343f-80ca-da47b6cb3c13 | -2.909 | -45.40734 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e85be508-c078-355d-924c-801d9b5ad17f | -3.29791 | -51.93081 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a567c164-4fe6-3938-a5af-b29f83b3f4be | -7.59616 | -43.55865 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ec6f6e4-47c0-32d5-bd55-6870916192e1 | -6.28072 | -45.32646 | 2025-10-31 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ead8c11-2a6f-36a5-9e0a-1490c4eed38d | -5.22833 | -45.47668 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cfa54fd-bac4-3f55-8d7e-6f773e917524 | -6.93027 | -46.01213 | 2025-10-31 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3f149c7-59f6-37fa-b773-af20fede4e99 | -3.14233 | -49.42245 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 385ff251-609b-37a4-9628-d9f1767dce21 | -7.17552 | -41.42753 | 2025-10-31 04:06:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 193beaef-a08c-326c-95f4-6bde046ad415 | -4.76056 | -46.89189 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4053efb3-d6e4-33f8-a2fc-d3945e9c061a | -6.23997 | -44.65271 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a92beb5-c0ef-3576-9d15-b7bb1266efd9 | -4.0169 | -44.82001 | 2025-10-31 04:06:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14a2281c-0cdd-3c37-922d-2de28d1074d4 | -5.94139 | -43.83584 | 2025-10-31 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 033ce073-5a2d-33ab-8c9a-e13357e8708b | -2.9144 | -48.7289 | 2025-10-31 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1bcd43c0-49f3-3e2d-b9ab-18e1a9ff0b66 | -7.62285 | -43.56672 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 323f07e5-b9d6-361e-a9f0-75dcd25af623 | -5.03065 | -43.61573 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb8f7c02-fafe-3021-bce1-feb16bd4627f | -6.163 | -41.62064 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 98b3a32c-15e2-3be2-afa9-d86824780936 | -6.15625 | -42.39017 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 82a4f362-5d21-37fc-b263-5735db2adc8f | -6.17583 | -44.08892 | 2025-10-31 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06291ffa-0dac-3383-990a-ea19559399cb | -4.78695 | -44.3233 | 2025-10-31 04:06:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce2f6a38-fcfb-326b-a7d6-577f85ae9f4a | -5.79132 | -43.73683 | 2025-10-31 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 190635cd-a0c4-3cae-8492-cb2a7b8049da | -2.49108 | -48.14832 | 2025-10-31 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af957e86-7fc6-3a85-988a-1601a5f33ac4 | -4.90472 | -42.01181 | 2025-10-31 04:06:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2fad422c-8c42-35bf-aca7-04aaa7df2460 | -6.85154 | -45.13173 | 2025-10-31 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e70a2813-e96a-38c5-b681-2215224d6c06 | -4.83742 | -40.7394 | 2025-10-31 04:06:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3a6b7817-34b6-3947-8777-e78db85ff447 | -7.38961 | -43.01018 | 2025-10-31 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f013efb5-b0ea-3f47-8145-c9fa92dfcb00 | -6.36427 | -40.96947 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
