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
| f4f7080c-b070-3274-98c4-a4c43fd06a8b | -12.4464 | -58.4825 | 2026-06-09 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 511bdf41-f589-319a-bb39-7b626ee18f7d | -11.5499 | -52.7867 | 2026-06-09 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 158.7 |
| e8a3af10-8eec-321e-88c6-83abefb0882b | -11.5502 | -52.7659 | 2026-06-09 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 5ad2ba1a-39ad-3285-aea5-bf40fcf9b9e3 | -7.1092 | -46.5065 | 2026-06-09 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 22db600a-6dc4-383f-964f-8fbb0867231e | -12.4466 | -58.4627 | 2026-06-09 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 16e38684-e4bb-36b4-b7cd-33cfddce2941 | -9.0699 | -50.6091 | 2026-06-09 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b856c763-569e-3673-89a4-ae8072cd17fb | -5.7939 | -45.1267 | 2026-06-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fc638c03-c5ab-3b8d-a38c-5c1b507301b0 | -5.7941 | -45.104 | 2026-06-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3f82c453-1928-3d30-a61f-f779b8b7bb42 | -9.3045 | -45.4809 | 2026-06-09 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 17738882-41e7-3a2c-ba7c-f642352a69f4 | -11.0281 | -49.4276 | 2026-06-09 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| e2758988-643e-3a44-a5b9-0ebdb798b13e | -12.0498 | -49.7612 | 2026-06-09 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| befde7a9-6674-3302-bf00-7670fd3f2ee8 | -15.1782 | -43.8655 | 2026-06-09 00:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 50.3 |
| a1f5d441-aa33-32bf-a6b4-c77b73dbf345 | -5.8128 | -45.1026 | 2026-06-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 481310ab-df55-3db9-bba1-bc19840999a3 | -12.0689 | -49.7589 | 2026-06-09 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| bba20b20-1985-3f46-9951-7ab3523aa215 | -17.5961 | -46.6415 | 2026-06-09 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 5c60a758-7221-32a8-839d-77a21fbb85aa | -11.5309 | -52.7887 | 2026-06-09 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 7a5e0ed7-a453-39d4-b2f7-aacfeb5304b1 | -10.6498 | -49.3834 | 2026-06-09 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4d6cf40f-999b-3de3-aef0-50980b94c260 | -10.6498 | -49.3834 | 2026-06-09 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 50f9adc7-5fd5-3b7f-9909-12a8713cc734 | -11.5309 | -52.7887 | 2026-06-09 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 1d8a34b5-d6cb-39a2-9e5e-47f301756f3c | -11.5502 | -52.7659 | 2026-06-09 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 82364c81-96f8-3fe1-9eff-cbf631ce679b | -11.0281 | -49.4276 | 2026-06-09 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 6f5e599a-eeb0-3b57-8b77-2b034da636f0 | -17.5961 | -46.6415 | 2026-06-09 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 73cb2d79-5066-3cd1-8516-5c4cb5fa1750 | -12.4466 | -58.4627 | 2026-06-09 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 61744cf1-04a3-369c-8eab-60c8aa49d97a | -12.0689 | -49.7589 | 2026-06-09 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 480b18c0-16a0-3521-8267-140b551023e4 | -9.3045 | -45.4809 | 2026-06-09 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 4d554312-8e16-3369-bdee-94f072915148 | -5.8128 | -45.1026 | 2026-06-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e03f9022-0b43-3fdb-8ef1-6793ff4cf2d7 | -11.0091 | -49.4298 | 2026-06-09 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 6ed35adf-e518-3e70-a6bc-34ec579e0f9c | -11.5499 | -52.7867 | 2026-06-09 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 68a1e981-6a7c-348a-95ee-8c80f6c5ed52 | -9.0699 | -50.6091 | 2026-06-09 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 7746de63-777e-32e2-a821-5dfae6f7df45 | -7.1092 | -46.5065 | 2026-06-09 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9c7e0495-c5b0-3930-b345-164ad6181d0d | -5.7941 | -45.104 | 2026-06-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 023d9f3f-1462-38d5-99b6-cbdaa0f984fa | -12.0498 | -49.7612 | 2026-06-09 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 07945623-f0ff-334e-af0b-1177a105841c | -5.7941 | -45.104 | 2026-06-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 972382d0-0393-3537-ae6d-00443022aa18 | -17.5961 | -46.6415 | 2026-06-09 00:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e709865a-ae1f-3b74-9b3e-be371f90afee | -12.0689 | -49.7589 | 2026-06-09 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 06d8b411-69a5-3be8-8b90-f18138cbf781 | -10.6498 | -49.3834 | 2026-06-09 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d78aca58-bfca-39e6-a28a-7912e4ed1163 | -12.0498 | -49.7612 | 2026-06-09 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b8ee73b7-e29f-3a98-bc09-523d4f8f38d8 | -11.5499 | -52.7867 | 2026-06-09 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| e3aff34b-be0d-363c-9696-249ad114c0bc | -5.8128 | -45.1026 | 2026-06-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3ba41f89-9737-34bd-b927-67fb1fd90773 | -9.3045 | -45.4809 | 2026-06-09 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 93dbaab5-daf1-3274-8497-8ecfdc2a966c | -7.1092 | -46.5065 | 2026-06-09 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b270dbc4-0c6a-3440-ab56-4f9aed8d8022 | -11.5502 | -52.7659 | 2026-06-09 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 57242bbe-0b48-38a7-bddb-f2ddc1688953 | -12.4466 | -58.4627 | 2026-06-09 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5f3b632f-b745-3eec-af00-6cab9c54d947 | -12.4464 | -58.4825 | 2026-06-09 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 5aa55d35-995d-3b0a-b1ce-5d329f6df2a2 | -9.0699 | -50.6091 | 2026-06-09 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 1e9d6f51-d582-3d05-86b1-fa06bf904603 | -11.5309 | -52.7887 | 2026-06-09 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| da63dae8-64c2-3f2a-9ae4-83bb0c3b204d | -9.2869 | -45.457298 | 2026-06-09 00:25:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc998e80-b8dd-3a79-9f15-64c4783d9f87 | -12.3674 | -47.894001 | 2026-06-09 00:25:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 628e07a7-4292-3dd2-98dc-1f6508e7f463 | -12.0336 | -47.794498 | 2026-06-09 00:25:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3a881df-2730-3d33-bf04-5167d725bbd8 | -11.483 | -57.1082 | 2026-06-09 00:25:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e9b11b4-87c5-3c04-ba3a-e1346b1dc89b | -11.0557 | -56.917801 | 2026-06-09 00:25:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c02c5132-727a-3f1d-8bb2-201296c2d554 | -11.3382 | -51.388401 | 2026-06-09 00:25:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 992df8b9-9969-31a9-9579-f3f5ff3a7ff4 | -10.6394 | -49.375301 | 2026-06-09 00:25:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5cde897-13fd-3e3e-8efa-3a8ddb1fd9cd | -9.0717 | -50.585999 | 2026-06-09 00:25:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53032273-5e92-3649-ba8e-d3e98d64c103 | -11.5914 | -58.491001 | 2026-06-09 00:25:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2732571-081c-353b-9330-f4cd0c821fbc | -7.3345 | -49.856899 | 2026-06-09 00:25:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6caf8dd-241b-3eec-ba97-d85c1d64057e | -9.2296 | -48.559898 | 2026-06-09 00:25:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9950db31-7342-3a0a-b529-2dd98de2b071 | -10.426 | -49.434399 | 2026-06-09 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9d54c50-4521-3efe-976c-36e98307e587 | -20.4207 | -51.279202 | 2026-06-09 00:25:00 | METOP-B | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5053e039-bcc4-388f-a736-146988424c47 | -5.7942 | -45.111801 | 2026-06-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2e1f77d-22a8-35ea-9498-dd5cee809c6b | -10.4278 | -49.442299 | 2026-06-09 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cebf426a-2f8e-332c-a1d9-80921b1f7279 | -12.4362 | -58.447899 | 2026-06-09 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ee5cc14-883c-39f8-a15e-c5616abe5f72 | -9.2966 | -45.454899 | 2026-06-09 00:25:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 101a9ddc-c01c-3384-9e9f-bab740f0ebb8 | -5.7316 | -49.087502 | 2026-06-09 00:25:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b19777ab-2b4e-361f-9a18-81f6606119b7 | -14.0302 | -47.365898 | 2026-06-09 00:25:00 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b4ee8d4-ec79-3f08-ae77-b45fe2514b05 | -12.0571 | -49.7449 | 2026-06-09 00:25:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3601cba-39c9-3fef-887b-ebdfb74a68d1 | -9.3 | -45.4688 | 2026-06-09 00:25:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57f80d1d-f0d2-3881-b9cc-21d0f4fc6d3f | -5.7338 | -49.096699 | 2026-06-09 00:25:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c6bbeb-eb91-360e-a57d-6d2ed586ef42 | -15.1811 | -43.858101 | 2026-06-09 00:25:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4e484e2d-5b6f-3113-9f43-5184d07b683d | -12.3631 | -47.876099 | 2026-06-09 00:25:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4928d3f9-1652-36a4-b174-eeee5ae55b4c | -8.9765 | -47.971001 | 2026-06-09 00:25:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed62301-e735-355b-9a9a-4282e7db673d | -11.574 | -54.5686 | 2026-06-09 00:25:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3473ef1-718b-313d-a909-4360280c7afa | -11.5562 | -52.782902 | 2026-06-09 00:25:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 282e46c9-a01f-3eac-b15f-9aa487381010 | -8.9788 | -47.980701 | 2026-06-09 00:25:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7f81112-37fb-3bf0-8a35-e63b7785454e | -13.9587 | -46.173 | 2026-06-09 00:25:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23df8e83-2965-31fe-8411-4a88a1641f1e | -10.859 | -53.731499 | 2026-06-09 00:25:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b88255a-6ae8-3be7-85c8-37dcb218a6c6 | -11.5433 | -52.771 | 2026-06-09 00:25:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8981231-4236-330d-b506-da014963d717 | -13.9613 | -46.183701 | 2026-06-09 00:25:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31ae1a2d-6757-34bd-a0ae-decf2c611891 | -12.4711 | -55.124599 | 2026-06-09 00:25:00 | METOP-B | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf1bb62-ef69-3383-8d38-1aff783efefc | -10.6491 | -49.373001 | 2026-06-09 00:25:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3b4e711-8d23-37e9-b591-2cb4f32c9b49 | -5.7999 | -45.092701 | 2026-06-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00700aae-7611-3079-a184-3137f8064874 | -7.108 | -46.5014 | 2026-06-09 00:25:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24dde9de-3d9f-3045-8517-e413c5cabb30 | -11.0228 | -49.4254 | 2026-06-09 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cb496a8-2baa-393b-aa14-01a61458f731 | -12.0508 | -49.7621 | 2026-06-09 00:25:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6a60407-7ef1-3f31-8598-3f0e2cd95fa7 | -9.2903 | -45.471199 | 2026-06-09 00:25:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 559de9d9-c18d-33ca-be4b-760a8b283b68 | -12.8492 | -44.376499 | 2026-06-09 00:25:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed77ed2-918c-3dd6-ae6e-e316f3c7d11d | -21.4349 | -48.632 | 2026-06-09 00:25:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0eed979b-ff31-3dcb-b3a3-a91782d0c4dd | -9.0734 | -50.5933 | 2026-06-09 00:25:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec443cb-4c28-3dcc-bcca-e9a7a6a52af9 | -10.6412 | -49.383202 | 2026-06-09 00:25:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 749ab1a2-6ba7-3e40-a758-74e1b763547e | -21.547899 | -47.037201 | 2026-06-09 00:25:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4cba8d1f-7360-3a2c-8464-ea2012a7673e | -11.4808 | -57.097301 | 2026-06-09 00:25:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15d18f5f-78cc-390b-ada9-89c666b909a2 | -12.8456 | -44.362099 | 2026-06-09 00:25:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ceb5056a-6aed-3a2d-96bc-17574f2fe7d0 | -17.593901 | -46.6465 | 2026-06-09 00:25:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 81c9980c-4258-3176-be20-972e38d0681f | -9.0849 | -50.5984 | 2026-06-09 00:25:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68df15c9-0871-385e-ba64-7e206e95ff13 | -11.5464 | -52.785099 | 2026-06-09 00:25:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf2994e1-ce35-3397-bcbb-e96a40ca33a9 | -17.5961 | -46.655602 | 2026-06-09 00:25:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1d74e104-80dd-32ff-bede-fe66b603e679 | -10.651 | -49.380901 | 2026-06-09 00:25:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a850d3b-fabc-303f-8574-80280264af0a | -10.9109 | -49.3442 | 2026-06-09 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fcfcd9e-407e-392c-827a-f15e3014038b | -5.8136 | -45.106998 | 2026-06-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44cda75a-dafa-3b76-9403-b543aa094940 | -15.2279 | -50.853901 | 2026-06-09 00:25:00 | METOP-B | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
