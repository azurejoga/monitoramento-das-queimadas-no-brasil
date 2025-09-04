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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be83bd81-2b62-3f4b-9101-41158a03e7ef | -22.89066 | -45.32087 | 2025-09-04 03:40:00 | NOAA-20 | ROSEIRA | SÃO PAULO | Brasil | 3544301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f5926e38-6dc3-3f4a-98d4-8b590180060a | -22.38522 | -48.38514 | 2025-09-04 03:40:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df8c81a1-eb34-32fc-a6e4-d03b700be1ad | -22.91263 | -42.41727 | 2025-09-04 03:40:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cebc1c29-1c88-30ac-bf9d-2a9931398582 | -22.46039 | -47.55152 | 2025-09-04 03:40:00 | NOAA-20 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 50888949-71c4-3072-a2fd-543db9ffbd15 | -22.81732 | -45.16939 | 2025-09-04 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22fe19b4-fe32-38a0-8dc6-b8af6c017258 | -22.6567 | -43.6825 | 2025-09-04 03:50:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| 6ba9d56d-0a19-38e2-a077-ae48311fb100 | -6.7319 | -58.7276 | 2025-09-04 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ae3dab2c-0d3c-36ed-9563-8d7ddbac8f7e | -6.7318 | -58.7469 | 2025-09-04 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3e03f97d-3a22-3790-99d3-2b854a42eec7 | -6.7504 | -58.7268 | 2025-09-04 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 0141502c-d3a8-3455-a69c-9afdd9da2624 | -6.7503 | -58.7462 | 2025-09-04 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 60e47bcd-099d-39b3-bfe5-13d8c1ad2f7a | -4.9951 | -56.256 | 2025-09-04 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 0ffe9748-f2fa-316f-ac3e-4195336c5b25 | -6.7649 | -63.1292 | 2025-09-04 03:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d0683d57-4380-34b4-86c5-f430e2859436 | -22.6558 | -43.7079 | 2025-09-04 03:50:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| c9c79a95-2e55-31ff-9aa2-1df0d3588567 | -2.9619 | -49.365 | 2025-09-04 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 11687956-f7a0-3984-adf7-9a07bc844643 | -6.6796 | -48.4049 | 2025-09-04 03:50:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0f71dc57-f49e-37cf-ad93-9a8500c7a9d2 | -11.6836 | -57.3518 | 2025-09-04 03:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 17769630-dc1a-3c93-a831-33b025cba40c | -11.6838 | -57.3319 | 2025-09-04 04:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 33f11855-72e9-3478-b8ed-a90d2278e5b0 | -6.7319 | -58.7276 | 2025-09-04 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 893a1d1e-719f-3e46-acfc-c4f960053308 | -6.7318 | -58.7469 | 2025-09-04 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7ccdf269-e6b9-3f64-9c31-bdfdee04543f | -11.6836 | -57.3518 | 2025-09-04 04:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d3e2e6dc-475e-3e59-913f-13cae48e57cc | -11.6647 | -57.3533 | 2025-09-04 04:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c23e0ed9-bd49-3219-81db-e23a1d860d24 | -6.7504 | -58.7268 | 2025-09-04 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 53d81ffd-a2e0-39c6-8b7c-d7b7b3d62df2 | -4.9951 | -56.256 | 2025-09-04 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 4768b9b1-e15b-3f8a-8fac-f6fc50cd8422 | -6.7649 | -63.1292 | 2025-09-04 04:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 14dbf53d-632c-3748-8029-58ae337cc31e | -6.7503 | -58.7462 | 2025-09-04 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| c54e2db5-13ca-3f36-ad75-f493f443ce58 | -4.9951 | -56.256 | 2025-09-04 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 304bc89c-1244-3c69-a77d-7cf7a993b56a | -6.7503 | -58.7462 | 2025-09-04 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5f13678a-cbd6-3ce8-b2da-bb5bb487e737 | -6.7649 | -63.1292 | 2025-09-04 04:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3bf76674-dd6c-39b8-9785-c1601f9e7189 | -6.7318 | -58.7469 | 2025-09-04 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 640cee2d-6de5-3df8-a306-26d790209b22 | -5.0135 | -56.2553 | 2025-09-04 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 7407e297-cce0-3345-bea7-e51c4a28f9be | -6.7319 | -58.7276 | 2025-09-04 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| bc9b94c6-1cf4-3fe1-82f4-b51011d418fc | -6.7504 | -58.7268 | 2025-09-04 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| f6d7f3cc-5d1e-382e-ada9-87f1826b2cc4 | -6.7833 | -63.1286 | 2025-09-04 04:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6271aaa8-627d-395d-9df2-e989b8497381 | -6.7504 | -58.7268 | 2025-09-04 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 7434165b-5daf-3768-99da-7074fa797aac | -6.7318 | -58.7469 | 2025-09-04 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6d7e51c2-a144-3d4c-804c-b5f69248302e | -6.7649 | -63.1292 | 2025-09-04 04:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 983faaeb-dae0-34cc-8f5e-32d5047bcb37 | -5.0135 | -56.2553 | 2025-09-04 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 950a0086-1056-33e7-bae7-3bceb0720ecd | -6.7319 | -58.7276 | 2025-09-04 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 9185e1a1-a5c9-32d8-8fb2-f1c5f588f8e0 | -6.7503 | -58.7462 | 2025-09-04 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 671745fb-c980-3875-9c66-003e7d40da5d | -4.9951 | -56.256 | 2025-09-04 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 60de6edc-8f45-37f8-a658-7dac78fdccb7 | -6.37765 | -42.99829 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac820df9-3bac-3509-89cf-cfd5e93ca32d | -3.76396 | -51.29026 | 2025-09-04 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4301b265-7c48-30d8-874e-38f2ba9dd01f | -6.73346 | -45.92236 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d53b969-80ec-3ad2-af26-883935c0b7af | -5.89352 | -45.96726 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a17e72c8-b02d-320f-92e2-b6c2e89e3dd3 | -6.54043 | -43.9145 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47763154-7d2d-32b6-92fc-587857ce086f | -6.29618 | -43.58863 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9234eba9-1b3a-3b46-a168-dc579e3980ae | -5.80025 | -49.12852 | 2025-09-04 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3dedb2f3-dcee-3065-aefb-82caa4338d97 | -4.56961 | -40.35293 | 2025-09-04 04:25:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e2c826ea-e610-314a-968b-1323bf1fc34a | -6.29203 | -43.59214 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb38b70-e14e-3e96-9120-601d09f19bee | -6.23178 | -43.55937 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26eef495-9a1d-329d-a43b-e69ef80f7599 | -6.26286 | -43.28431 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4f7c9c5-b28b-36a0-982b-7204afa759d6 | -6.26724 | -43.58831 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0997cead-1252-3600-94c2-3574ad4b742d | -3.30469 | -42.39982 | 2025-09-04 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b11ec29-54b2-3b48-837a-d5e72fa7929a | -7.80309 | -46.08637 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8e866f5-89e2-3649-b52a-8e21012de663 | -5.82558 | -46.35914 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1070ab98-c8a4-3c03-a1fa-a127a01ed44b | -6.78793 | -44.45894 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8473e117-e689-381e-ae58-089e2cfb8b1f | -7.50251 | -44.80977 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e87580c2-b713-3b8a-87c2-b936a2205174 | -2.95993 | -49.34856 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6de281d-7c13-3542-8ec8-62f086fab7b5 | -6.34331 | -45.67556 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f441abf-a91c-3f3f-b27f-7b24b4cd13f5 | -6.53847 | -44.55555 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04f6414d-ce9c-36cf-a300-68ec217fff38 | -6.78146 | -44.0882 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 3e5abd5e-30cf-37c9-ac5d-bf4096743302 | -5.69822 | -45.11892 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08b3c6a1-9710-3e9e-be06-ec3e02189fa1 | -6.54861 | -42.95478 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11c6ca64-4eac-3a1e-aa8e-becfeb0b687f | -5.48835 | -45.22391 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4f62c7e-a9cf-331a-b6d6-97029e29727e | -6.29776 | -43.50597 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9ae982e-6532-3d36-b601-fdbbd357451f | -5.7028 | -45.15582 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcad7e74-d8ac-3cbc-8615-ca6b4facb7f0 | -5.79894 | -45.63341 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfa7bf87-d26b-33d0-90e7-be0f1f7909c5 | -5.4109 | -42.33656 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e13fd3be-5d9e-360c-a5b0-a13bb9457e72 | -5.70397 | -45.17046 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a18cb477-8a25-32f8-b51b-09e5704ade4f | -6.26385 | -44.51482 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ee9b455c-62bc-3237-9110-1db4b3a6740e | -6.30441 | -44.15649 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7efec7d-1b5a-3251-b447-a1327a3e51c9 | -3.16425 | -49.47776 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2451cd80-a605-373f-8ee3-6d84fcf24d1a | -5.93577 | -43.02511 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 32e8a950-cc90-3b77-856d-4e57ae0709c4 | -5.68231 | -45.17792 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b1ec37-b00e-33f2-84e8-7dd7cefb3374 | -5.6849 | -45.6011 | 2025-09-04 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e0bcd2a-791e-341d-a5e3-006a2f3aec20 | -6.25985 | -45.09295 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9001e785-886f-36da-883f-0b8a3ecd1ad6 | -8.02651 | -44.04622 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9178b9d1-b19b-32e7-9eab-74775034e963 | -6.88713 | -44.8862 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63bdc6ed-4c49-3b29-92bd-83dd1b1a822b | -5.50548 | -42.65254 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f3cdbd3-ecb1-3d28-b1c7-ed41c4b43323 | -8.04165 | -44.13848 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95ac04e5-d945-3c2f-9a6b-e9ea3b50476a | -6.50093 | -44.08265 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 845b8326-a465-337a-83c3-492addca52ba | -7.00978 | -43.24973 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8efbeeb1-a532-34a1-9c70-1d93f6cc6795 | -4.78117 | -43.81837 | 2025-09-04 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3615a1d-f515-38e0-abea-a857072ad5ef | -6.24782 | -43.5484 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cb7cd27-83c0-3251-96b9-1edbfffa2b9b | -7.34718 | -48.18746 | 2025-09-04 04:25:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e17056b8-b449-3e00-836d-53df19f590f7 | -6.4661 | -43.97173 | 2025-09-04 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cb9dc4d-569c-3ceb-86d9-4c3be48f11ae | -3.4316 | -59.56836 | 2025-09-04 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1878aef-60a4-362a-90ed-c7552d092316 | -6.12405 | -44.14531 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a68dd8b-7117-353a-95ae-87dbc21b2299 | -5.7667 | -45.42508 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d04d7e5f-bce6-3a2b-bdb0-71318f13f7ac | -6.79368 | -44.49045 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f93f9d02-b030-37fa-a3b9-ef5ea1812da1 | -6.3621 | -45.64327 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56a0a7b2-f34a-3ae7-9788-e5d172e6d700 | -5.92417 | -44.16529 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b916a325-af54-377d-b996-be38c4d7ed32 | -3.47538 | -50.54125 | 2025-09-04 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dad15d2-bdcb-3540-aae3-eba059ddb0f7 | -5.83453 | -45.66748 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db288931-6c78-3f1e-bb55-fb784b2c814f | -5.77002 | -45.42558 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71e0b46a-7fdf-33fe-a95b-2942238563ef | -7.67664 | -44.74796 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af18acdb-f094-3753-a437-e75e954a26ab | -7.25925 | -43.85165 | 2025-09-04 04:25:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c31ba77b-4a71-3075-9f05-22c109278a96 | -2.9585 | -49.3574 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 21b95cdc-2320-3e24-b3c6-ff42933f3fb4 | -3.17059 | -48.80789 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e75434b-a8e4-3ad9-9845-291e8b508e02 | -5.74781 | -45.54718 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README25.md)
