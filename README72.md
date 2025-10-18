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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a73a9c47-e0e1-36ea-8c0a-f2c376ddb646 | -7.76739 | -42.48331 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cb53ccce-7a4d-33ee-b959-78656bac28e0 | -8.10612 | -55.08574 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6488c8a4-431a-30a6-8ea9-697064f2a494 | -2.57104 | -49.11808 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb386c8d-3984-389f-b592-eaa3c1990c25 | -8.58817 | -48.20428 | 2025-10-18 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb69a412-957e-370c-807b-fbb6f1aee62a | -8.36507 | -46.20765 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf2e5bb0-036b-3ce6-a863-266222f44a37 | -4.44712 | -43.23804 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecef05fc-6b5f-3ef5-8b80-f3fe5450c8ea | -7.35946 | -44.23077 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61c7d58e-74b6-3f6c-a67c-886d4216931c | -5.20564 | -45.75514 | 2025-10-18 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abc072b1-c9f3-3f59-bb28-1031f8cb1373 | -7.17324 | -42.36405 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 111c0ea5-eda7-3174-bad7-3a35439557a1 | -2.87954 | -50.7308 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6e3119a-73cc-32b7-8739-a259dcbe4aa3 | -6.61182 | -43.61451 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ec01c1a-a4e9-3c5a-840f-8787130a7b97 | -3.65999 | -51.75188 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02d09c82-8b92-315b-8a6b-b864b109a8ef | -7.98213 | -44.155 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64848f5e-244b-38fd-beb3-8aeba97b7d0a | -2.92274 | -49.18175 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90caaf3c-a6a7-3281-9b81-32d7b99ac91d | -6.99416 | -45.20282 | 2025-10-18 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fee36abe-97cb-3824-9299-cbacf7c6f12b | -5.00763 | -46.03069 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1caff272-d453-3a6b-a90a-8e47121d63d6 | -7.95511 | -44.12247 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7532169-dac3-368e-be1f-aeef9febc4ac | -5.65534 | -46.81477 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0210f694-c7e0-343d-b8e0-98e15b158b32 | -7.45201 | -46.84373 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fee1df4-3e0c-34e9-97b5-348375ab3f16 | -5.90863 | -44.76787 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 126df80d-5660-3c2b-8bb9-58400fce7a45 | -8.3637 | -46.23278 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f5e12e7-cceb-388d-af92-09b1447ffac1 | -2.81601 | -54.38208 | 2025-10-18 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb5d8800-4706-34d5-8508-b927e925cc36 | -2.79789 | -48.93946 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1487aae-2e36-31d0-9ed0-5f56e25c0843 | -8.2215 | -46.83331 | 2025-10-18 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc4f5dce-2958-3713-8d4d-88a78a7c2f1f | -4.45232 | -43.23879 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6c448b91-a635-35f0-9194-9531b2d0564c | -8.54294 | -50.08296 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8567929-fba4-30bd-9a59-4bbea9f7716a | -5.37674 | -46.00196 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a301d36-9e03-3e2c-a38c-92ac4f3f656e | -1.82842 | -57.1097 | 2025-10-18 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ae8240f-0fb4-33a9-93fd-931c318330da | -2.0243 | -56.59569 | 2025-10-18 04:49:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fa6421b-3e2a-3c3a-a393-ca82531c0607 | -3.51715 | -52.84699 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05f524e7-7fcf-3417-ba78-d6065807a283 | -9.75159 | -43.95536 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74f63225-1aa8-3bee-a830-6b92bb83a6ff | -2.80853 | -48.66476 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c629cfbe-6580-302c-abe8-2e929de9c330 | -7.58213 | -44.99 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d23c29f6-947d-3a38-8f0f-e98f304db072 | -4.34171 | -46.72896 | 2025-10-18 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6327a9f-febb-3165-b796-4d3ede86e61b | -6.54676 | -43.91464 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5014c0af-bac1-305e-ab28-8a53823860dc | -8.83389 | -49.66736 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eff287c-bbae-31c2-a170-1397c0a7f63a | -8.24765 | -44.01488 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3afcbab9-c324-3f1f-aecc-c43c827d7d33 | -7.4517 | -46.52616 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70df6d7b-a675-3991-b5c6-a1e09b7177cd | -4.48091 | -43.63198 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75e1571f-5f3b-3b4c-9ba2-adaa39e33466 | -6.99447 | -42.79679 | 2025-10-18 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59bcb783-c3b4-3812-a3f6-667566ea0845 | -6.99073 | -45.20301 | 2025-10-18 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae27e3a1-5487-39a5-85a5-eb8b0e74ab9b | -5.59923 | -50.05678 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 596b0309-db80-39f2-9c0d-576ef06a78e1 | -8.0909 | -44.10409 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fdb472a-e63f-370d-ade2-b0763eff9e3e | -4.53902 | -48.41529 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14453402-8f28-3234-a21a-9e2ac5ea2bb8 | -3.06417 | -43.22105 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c3b75d3-1036-3a63-8e83-31fe53cbe1d7 | -6.1083 | -45.85095 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a30be2f-c3fc-319d-9e18-f4ca648c721d | -7.43135 | -46.89748 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af45be7a-54c6-30f9-a5e7-179c4e955d3a | -3.06042 | -43.21135 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2106f731-ff6a-34cf-a5da-906b13a299b0 | -8.45176 | -44.17274 | 2025-10-18 04:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 890d757e-704e-3e03-a5f4-147ffbabb82c | -2.81665 | -54.37811 | 2025-10-18 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28a416d1-fda1-36d0-8288-124bff3778bc | -3.25469 | -52.91421 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bad29c18-45b2-34ce-b7c8-85d275c21224 | -7.1445 | -46.42325 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d6a653d-56e1-38f9-ae39-13dbe7a44451 | -4.82538 | -45.23828 | 2025-10-18 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23c58f18-840a-3c8a-a979-94fb1909bec3 | -3.29067 | -50.01026 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc850e08-7d7f-36f1-a973-a1be4c7af53e | -7.39617 | -44.75566 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 442dfa8b-078c-3c21-a639-df82bc66d104 | -7.44331 | -43.75566 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6e13326-8cda-3172-abaf-b8fac4e0232c | -3.79364 | -51.76616 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fcc53738-57cd-3ec3-98f6-2c6e2efee3ab | -7.66524 | -44.63365 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf0f80a6-a6d8-34a8-b3f4-2c0d68330b91 | -6.19822 | -52.74001 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35b7fb3f-0e63-3020-810d-d7b512f83534 | -2.87011 | -50.7257 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7aa45ec9-3ea8-31cf-ac2f-df1c52c64a2f | -6.2207 | -55.6398 | 2025-10-18 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa36ec4a-1118-3d7a-b523-1bdfa001757c | -5.25837 | -47.24289 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0f56c9fa-fc47-3976-9672-d11d47a19469 | -2.40682 | -49.36254 | 2025-10-18 04:49:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afef1cd2-f236-3c89-9109-f917fbb4573f | -9.50457 | -47.26917 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 813777b6-2847-3e4e-915d-7b8df5e8d3ba | -5.07401 | -49.85064 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cef4c44-193d-3bdd-96f3-6524e19baa3a | -6.65103 | -43.67706 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70b11494-2cc3-3e2a-9055-3048fb7de325 | -9.50515 | -47.2704 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c9220c6-ac9f-3951-9d81-7e8a29e81b00 | -6.83809 | -42.42902 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b714a8bf-6100-3da0-90c0-1f78860b4acf | -2.87677 | -50.72673 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 433550f8-4a9d-3597-89a7-43e79ad6c3b8 | -2.45242 | -54.11804 | 2025-10-18 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de61d869-788b-3418-9fd8-15f26d4ee152 | -8.69284 | -47.06408 | 2025-10-18 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07961b81-eb9e-3743-8b7a-dd8c9f33024c | -6.33779 | -46.344 | 2025-10-18 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a76b0c3-1c85-3a5c-ad09-f837e8311fe4 | -5.22306 | -44.78077 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7614b28d-3fff-393b-93a3-e6f79f32e00e | -5.91977 | -45.44226 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8e911d01-318d-37f7-a5ae-25582e310049 | -6.30216 | -44.71676 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 113d9620-b36a-3b71-99c7-6ac41f8e7543 | -8.82405 | -49.68324 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b417f92-2d91-3108-adec-6d3a52232bca | -3.49283 | -42.73118 | 2025-10-18 04:49:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 825b57cc-ade9-31e9-96b3-cc6d1fffce1d | -3.25017 | -45.9653 | 2025-10-18 04:49:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65584910-6474-3f03-a156-af0af7542764 | -2.70737 | -49.41065 | 2025-10-18 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e178571-d0d9-36ee-92f2-4944f3421324 | -4.11478 | -42.91165 | 2025-10-18 04:49:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 181a0f05-fc99-32f8-aa95-3fbe1c833bd4 | -3.40998 | -52.88093 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e6ed724e-0335-3199-ab04-e06aa3585e8c | -6.36267 | -58.21405 | 2025-10-18 04:49:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9446cdb7-15ef-35ab-8879-637786528d44 | -3.84544 | -41.58355 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba41f3e9-8028-34f9-9c33-3491dfecc75d | -3.74898 | -49.0361 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08b01a98-aaca-3ac8-8de4-e0cdc9664cb8 | -6.8499 | -50.71276 | 2025-10-18 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b03bea22-5941-3351-8504-a8b06c38e679 | -6.5638 | -44.42976 | 2025-10-18 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d367922-2980-36a0-a7b9-d48f2dee7305 | -6.14357 | -44.29503 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5410a5d-e9ac-37e2-9411-49cf5c7a10f1 | -3.77279 | -58.53816 | 2025-10-18 04:49:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d89bf140-69fc-3c14-bbfe-406e583bf009 | -3.15694 | -49.16484 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5585ef4b-9594-3ee2-96a3-e0e55908fa27 | -5.79151 | -49.41836 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e03a5067-b835-3286-8135-bf5f3040bf89 | -5.86722 | -44.8482 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f4dfecc-cce4-32ec-94d4-277d8e8c85f2 | -8.30546 | -43.40199 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4216eeb5-8cbf-3ac1-9ce4-df95dda9cc61 | -5.10415 | -56.1554 | 2025-10-18 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 730041a8-8968-3f9b-a954-9f4369c55d48 | -6.96337 | -47.12224 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c842cc77-b622-378d-8083-22941edf3b0f | -7.57779 | -44.97913 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29cf7317-53fb-3fb6-8505-99580c08b6f3 | -7.44815 | -42.68822 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3b71ec71-2a43-32b6-b2b2-db37e2b32702 | -4.66605 | -50.70301 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2854aacf-96ce-3cf7-9e8a-5c29f62c7cf6 | -8.54113 | -49.60455 | 2025-10-18 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 116b176c-16ea-3a0b-82ca-34e5cefeff47 | -7.92803 | -44.12843 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbf59a26-769f-35dc-9d69-fe5efb85eec6 | -6.36166 | -45.78007 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README73.md)
