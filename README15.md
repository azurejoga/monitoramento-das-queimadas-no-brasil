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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79895b0a-6171-39f1-96c5-bd3080f6d563 | -5.88243 | -44.52102 | 2025-11-01 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fcdcb2f4-87d4-3d99-996d-aeaab4cd7841 | -4.66221 | -41.96454 | 2025-11-01 03:49:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6663dfd9-b63e-311d-bddd-d96a0c86384c | -12.59843 | -48.34352 | 2025-11-01 03:49:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92525bca-9640-3080-9edc-b14b2036e704 | -13.50867 | -47.11423 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a69484b7-4290-31ff-acb2-4973452e23c6 | -5.83485 | -44.06384 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 4c5c136f-3edd-360c-a025-3a61213a4c17 | -4.74369 | -44.43679 | 2025-11-01 03:49:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30133ff9-6594-396f-b6a1-f7e3dae1a76b | -13.53254 | -47.11426 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44c5da82-5ca0-306b-b0aa-6cef7363715a | -13.65082 | -44.40342 | 2025-11-01 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c72dc332-d31d-3196-9f24-8b0a5350914c | -4.55799 | -46.69263 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c3a7f68-bc85-3e17-8f6e-d303d78e5846 | -5.63381 | -42.80916 | 2025-11-01 03:49:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a869c075-01a0-31f7-81b1-6423f5fab249 | -13.71154 | -43.78912 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6ecce03-d077-3d5b-a763-1ea56ca960a7 | -5.25785 | -45.61217 | 2025-11-01 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c79b593d-dc05-3fd0-b8c1-0ed0737ec470 | -13.00615 | -43.8526 | 2025-11-01 03:49:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4151653e-3f42-3637-a291-a03b7c9cff27 | -4.56442 | -45.87661 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 080ddc18-71de-332a-b790-9e90c44a7f7b | -10.4224 | -49.37323 | 2025-11-01 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5f322ed-e4eb-32b2-9fec-5bc0c14316a8 | -5.26318 | -45.61308 | 2025-11-01 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d10a6530-0176-36ef-965a-accdbec8c36e | -5.25847 | -45.60863 | 2025-11-01 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b971f2cc-f1b9-3e01-a250-b8cf99ebcde8 | -4.29246 | -46.26535 | 2025-11-01 03:49:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b171c6a7-0d0b-3653-a5fe-06633c0e0f06 | -13.72288 | -51.45949 | 2025-11-01 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a943e245-c89b-310d-a024-946baf91918e | -4.66157 | -41.96841 | 2025-11-01 03:49:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9b1273d1-cf22-39cc-ae73-d4600e50fa48 | -3.52386 | -47.55513 | 2025-11-01 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 787cb1f7-a29b-35a8-bc8a-2665b0e519ba | -14.90995 | -42.80306 | 2025-11-01 03:49:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43128f4c-4280-3ee5-8350-a41d717b6ed1 | -13.70879 | -43.78578 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77bc9831-1e44-332c-a126-9b15e9354354 | -5.21068 | -45.83831 | 2025-11-01 03:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b4ae1dd-c96a-3eb9-b67f-bc48a3476b2f | -12.31214 | -37.91783 | 2025-11-01 03:49:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa1ff6be-c37c-3624-ad11-5966b67797f0 | -13.74529 | -43.60203 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0de35aee-7466-3d32-b192-57ae32a87ff0 | -13.04551 | -43.37417 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46684690-b38a-37f7-b1f7-7c23c40a08ec | -4.80816 | -45.87615 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc927a55-c3d2-3549-9817-ae8f88a4cf4d | -10.41288 | -44.33021 | 2025-11-01 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b301228d-be95-3e0d-a79a-2adf1b6c219a | -13.52505 | -47.11158 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9ea00b0c-5b07-30dd-ab65-aac84725f447 | -4.94141 | -45.50993 | 2025-11-01 03:49:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d84954f-c1c7-3a64-b78a-9eb1cbc80365 | -5.2401 | -45.05903 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ba5d1b8-81a9-307d-b7b1-5a3fd070abd9 | -4.81115 | -45.75451 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afbaac63-e274-3486-8499-590157aba273 | -5.21388 | -45.92377 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0758d4e8-b7e9-316c-87ba-2c54718c7752 | -10.6313 | -52.1891 | 2025-11-01 03:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 863a6ccf-ef7c-37e0-973b-99f3a1d54c0d | -3.234 | -50.5789 | 2025-11-01 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b3feb662-8eda-3e8f-97a5-58f4b34437fe | -25.46195 | -52.90606 | 2025-11-01 03:53:00 | NOAA-20 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6373f97b-9c5c-3ad7-8570-9e2e4b972302 | -10.4219 | -44.3542 | 2025-11-01 04:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 530db6df-6b77-3eee-ad14-4b1528aa3b93 | -10.4222 | -44.331 | 2025-11-01 04:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 86e25ed0-daf2-3a0b-af9c-2d19fd6f4501 | -3.234 | -50.5789 | 2025-11-01 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| dadd5313-d4b1-35d0-9a36-1e1aad02f1c1 | -3.234 | -50.5789 | 2025-11-01 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7c1e2307-b850-36ee-9b8e-1dff67c006a9 | -3.2156 | -50.5795 | 2025-11-01 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 1be91511-b36b-3037-b989-673ee29e643d | -3.234 | -50.5789 | 2025-11-01 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 808a4885-1d23-34bb-acf9-ac699c1b94b8 | -3.1094 | -45.2293 | 2025-11-01 04:20:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 2748fe79-d2eb-3faa-892f-3592f2afce76 | -3.2156 | -50.5795 | 2025-11-01 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1c6ce9e5-05d6-3a09-9388-82986c33ea18 | -3.1094 | -45.2293 | 2025-11-01 04:30:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 73062a6f-3346-35aa-8a46-6f43b214be65 | -3.234 | -50.5789 | 2025-11-01 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 98648ebe-1df1-398f-8a6e-eaca67369b44 | -1.49834 | -47.80444 | 2025-11-01 04:36:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5f04d86-6142-33d7-9678-586be4f49c49 | 1.25938 | -50.84631 | 2025-11-01 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af6acaf1-c08e-32a4-96c7-c824b4b83417 | -1.18061 | -48.85541 | 2025-11-01 04:36:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2672ae04-604e-31d6-85d2-75612f8bd839 | 1.68964 | -50.8897 | 2025-11-01 04:36:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd29d1a3-2c1a-3499-8133-f0afea685f5f | 0.50141 | -50.7725 | 2025-11-01 04:36:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6871917d-05c1-34cc-ae6a-39d11f933951 | 1.26403 | -50.82845 | 2025-11-01 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14e05ab6-896c-3ec1-9e24-1da324f9b027 | 1.64428 | -55.64217 | 2025-11-01 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75da32d3-df01-37f6-a3d6-3592ee633939 | -1.4945 | -47.80736 | 2025-11-01 04:36:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f78a53b9-8568-3dd9-8ec3-9b996b27d72c | 1.64928 | -55.64144 | 2025-11-01 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07e93840-3bcd-34fd-8512-fb9767d3988f | -0.17262 | -49.96502 | 2025-11-01 04:36:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fef0a8aa-0f52-3710-a220-3fcffe32a732 | -0.40564 | -51.75159 | 2025-11-01 04:36:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bb7e669-9e68-3cc6-9fb2-e1e19192b675 | -0.43107 | -51.76007 | 2025-11-01 04:36:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1a3dbc1-c81e-35fc-ab40-bac3897fb845 | 0.50077 | -50.76842 | 2025-11-01 04:36:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f8b8735-f953-3a02-b0c6-9791266de5fc | 0.59646 | -51.57681 | 2025-11-01 04:36:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89046484-c200-3456-8154-f1b38b8c261f | -1.49503 | -47.80393 | 2025-11-01 04:36:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa7e27f9-3fc3-3f00-9a71-5eaf0ad7ce7d | -0.43177 | -51.7556 | 2025-11-01 04:36:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cb1f568-6804-312a-8f05-51517979197e | -0.40493 | -51.75604 | 2025-11-01 04:36:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80e876e7-c3da-360b-949c-1554b4b1f818 | -0.4348 | -51.76065 | 2025-11-01 04:36:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5c2a8e8-e722-35c4-8def-3d9926e245bf | 1.26236 | -50.84156 | 2025-11-01 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 584a7d69-55fd-3a1f-9277-a80022347fe2 | 1.31133 | -51.20669 | 2025-11-01 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da16a5b-ef1c-3109-8c3a-b28683e79e4f | -1.45536 | -48.0575 | 2025-11-01 04:36:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2634a60a-3ddf-352b-ac52-42270d614f31 | -3.81288 | -51.69917 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 369245b8-1747-3aff-b054-dbb660fd9445 | -7.02923 | -47.6172 | 2025-11-01 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a856885e-8a1c-3d37-8abf-31bd311c935d | -6.40528 | -49.17495 | 2025-11-01 04:38:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b2b02e-1e80-359c-8063-3d5199f2f314 | -3.22984 | -50.57804 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c622b6d4-3841-32f0-b437-9848d0e9ca33 | -2.96897 | -50.38263 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55e58e23-bd6c-3c73-97e9-22a96b2d672b | -5.08199 | -49.23752 | 2025-11-01 04:38:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6cdd1f8-0ec5-3de1-8525-97855a6740a0 | -2.91092 | -54.29616 | 2025-11-01 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9675e05d-711d-3ee3-b347-8dd1f36659cf | -3.38304 | -52.79938 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7293f5bf-eb11-31e2-aa5c-cdc84ebd7d97 | -5.21532 | -45.8377 | 2025-11-01 04:38:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 88410ad8-0119-388e-b443-5e72e7b6632e | -4.07502 | -50.36046 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1c3acba-1e82-343b-90e0-5aa764874f03 | -3.37783 | -44.24231 | 2025-11-01 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e3e2786-f205-331b-bf2b-801a0e33d579 | -4.66432 | -41.96033 | 2025-11-01 04:38:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a1b6ca41-dc21-367e-a304-348419eeb278 | -6.5411 | -48.03496 | 2025-11-01 04:38:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9080ff88-8da4-3a87-8ce5-4fae69ed68b1 | -8.85718 | -49.88079 | 2025-11-01 04:38:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 56a0b9a6-c33e-3f58-8509-44a744600166 | -4.68054 | -50.44424 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdfcd247-8eac-3305-80f4-7f3f574fb904 | -5.22524 | -46.17357 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8ed0be7-1cb5-38b9-a9dc-663dc7980fde | -5.8514 | -44.65161 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42f44f9a-bd5e-3f4b-93e7-47b01c27b34a | -8.15635 | -45.43346 | 2025-11-01 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67d823a0-9af1-38ce-81d2-7ad1c088e114 | -3.87953 | -51.19362 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 194f0959-3970-30c8-b28f-e45786a1de9d | -7.84395 | -40.25993 | 2025-11-01 04:38:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 166d0cb0-0c84-35af-8da2-65b613718e78 | -3.22181 | -50.58441 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a256ffe1-b563-3342-a618-6c35bc430193 | -3.57057 | -50.27076 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3d50fa2-27f5-357e-a5b9-faeb77c33291 | -5.83285 | -44.05949 | 2025-11-01 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0e513a0e-6862-355c-9325-039c751766a3 | -5.26601 | -44.71949 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bda0e68f-507f-31ec-acce-97056135dc51 | -5.07105 | -45.11136 | 2025-11-01 04:38:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea196c37-7bbe-3940-a643-6af1d09510fb | -3.88016 | -51.18975 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e21686-94a2-3bc1-b893-eb77030db219 | -3.22464 | -50.58866 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 638c937e-3b55-3548-aef2-dbdb254d2821 | -4.30396 | -41.4423 | 2025-11-01 04:38:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a12d91e-ddd5-3eb8-8ba4-cfe92ff17b7e | -3.37943 | -51.07359 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfeb3e7c-b7ff-36c2-91e1-995d4c6a4cca | -3.44411 | -52.80884 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93243c02-cd71-3c1b-84e2-38f58174f96d | -4.55557 | -50.30691 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fde67297-e53d-3906-a10a-cb8eb942550f | -4.57407 | -48.02372 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README16.md)
