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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad38de05-5550-3394-9150-2afb6f4761df | -3.5481 | -50.5267 | 2024-11-22 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f11ec3b3-bdd1-3007-b3cb-4b4fe4fd8419 | -3.5159 | -53.8132 | 2024-11-22 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| e3495813-77ad-3ec1-91c7-c6019d18918f | -3.2385 | -54.2431 | 2024-11-22 03:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 67c6d3c9-a6c5-3b10-8d74-4eced8214fde | -3.2201 | -54.2436 | 2024-11-22 03:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| c6038c32-28e0-3807-a4dc-cd895f9da3a0 | -1.2041 | -51.9683 | 2024-11-22 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1d150286-35eb-3edc-8adf-836141a6fdea | -3.2386 | -54.223 | 2024-11-22 03:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| fea89505-e076-3fdb-af79-3e62925e6e2e | -1.1857 | -51.948 | 2024-11-22 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 76e4ffa8-72a3-39d6-b6a8-19d170be7c9f | -3.2768 | -53.8199 | 2024-11-22 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d43e351b-298e-34c0-9f18-5b5b8158a8ae | -1.1287 | -53.3951 | 2024-11-22 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| da07cac2-161a-3411-a2a1-8ec937505079 | -3.516 | -53.793 | 2024-11-22 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 6e443735-879d-3a06-b2f6-1d02dba40290 | -3.2384 | -54.2632 | 2024-11-22 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 465c6028-3f6e-351b-8ddb-1b40a6df367f | -3.22 | -54.2636 | 2024-11-22 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 901100cb-ef94-3d1a-9a5b-fdea6b71d278 | -1.2041 | -51.9478 | 2024-11-22 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| c2bbb9e1-788e-33e8-b2c4-6329a0f89482 | -0.93721 | -47.56025 | 2024-11-22 03:46:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 77fb49e5-a19a-3f4c-803f-7f0782bb4a80 | -0.93802 | -47.55523 | 2024-11-22 03:46:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| aad976b6-f4e5-36f0-a436-0ce793200b0c | -3.90339 | -40.97572 | 2024-11-22 03:49:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 46ed43ae-03a6-3544-8a72-c3ced82d8266 | -4.72611 | -43.25398 | 2024-11-22 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04c85eba-9c7f-3024-8382-2de5ecd249f7 | -9.16911 | -43.15558 | 2024-11-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b52fe41f-e6ad-3932-9a3b-64c9aeec0cad | -4.53344 | -46.61891 | 2024-11-22 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aea7db7f-01d8-3a73-8f2c-5fff41b19626 | -4.44201 | -42.59181 | 2024-11-22 03:49:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6392d43d-3889-3712-b75e-18754ecbfac6 | -9.29907 | -43.13076 | 2024-11-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3da55cac-299d-33cb-92cf-412c20f3d23b | -9.04836 | -36.03989 | 2024-11-22 03:49:00 | NOAA-21 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 392d1f1c-ba04-38eb-81eb-48ccf2ce6204 | -6.92015 | -46.10941 | 2024-11-22 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d83b0ec-1391-3552-8a0e-168b0797eb6e | -6.62729 | -42.38612 | 2024-11-22 03:49:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10167df8-1f6c-3b57-ad0c-e844e7cfc3eb | -9.13015 | -43.10966 | 2024-11-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3273769d-1fe4-39be-a480-ea10d6d766c7 | -4.13658 | -46.70653 | 2024-11-22 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e6fce2-c014-3344-a71a-41c6abd4e811 | -7.65433 | -44.49973 | 2024-11-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e99ce8b-3880-36ee-8ac7-3f57a7cb2b5e | -1.52162 | -47.0661 | 2024-11-22 03:49:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 67b0e23b-507e-3bd1-a1eb-6e69d4e363c6 | -2.69897 | -46.22355 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f502b775-2405-34f8-96e4-c205869466c8 | -3.64755 | -41.91077 | 2024-11-22 03:49:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea1533f4-42a3-3b08-8fe6-9599b9099125 | -6.81994 | -46.78061 | 2024-11-22 03:49:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efed1602-8bb8-3037-b912-4629e705511d | -6.3936 | -39.93743 | 2024-11-22 03:49:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 545470dc-0db0-3ef9-ad40-d1d727ae02a0 | -5.24644 | -42.63906 | 2024-11-22 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 17cd257d-b226-3cbe-ad64-5b26a4a0bfaf | -4.36088 | -40.11734 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d52059cd-da4c-3b83-a8a9-7106a68b01f4 | -4.23021 | -40.38369 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e39b24fc-185e-3e05-824e-e18bf3739317 | -7.75916 | -46.22441 | 2024-11-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0253eaa-f75b-3ffc-af83-5b3330696360 | -8.92405 | -41.18961 | 2024-11-22 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9b96ada6-ba61-3d56-8d65-44a6a2f8d311 | -2.69848 | -46.08584 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c25b5fdb-3aad-3637-9073-bdca74eaa66e | -3.00696 | -45.13098 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da7b4c1d-496a-31c7-b643-8d69fc3e334f | -4.0075 | -43.2491 | 2024-11-22 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba1dea8a-48d3-3ff9-8cae-1b38548d9c28 | -6.82678 | -39.34752 | 2024-11-22 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1ca9e472-471e-35a1-99d2-a09a32bf6489 | -8.52533 | -37.0631 | 2024-11-22 03:49:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84400330-d37f-3c56-8710-463abf64ec62 | -6.18573 | -45.44846 | 2024-11-22 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75c38927-7587-31ef-a63f-d760e6a313b3 | -3.45788 | -45.91216 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3dab1200-df64-358c-a15f-8ddf295db48a | -2.65101 | -47.12962 | 2024-11-22 03:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09cd500b-e650-3c16-b9fb-d480ef41b42b | -4.40333 | -44.11867 | 2024-11-22 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d735d91-a351-3e1a-b385-7fb7df903a66 | -3.75132 | -44.56703 | 2024-11-22 03:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ea5f63e-7c1b-34e3-8232-47be0b6b15c6 | -4.70968 | -44.25674 | 2024-11-22 03:49:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ca68419-9bfa-3eea-90e8-8150a69772fd | -10.13893 | -36.19671 | 2024-11-22 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a165c648-aedc-3626-a9f1-232371d6b363 | -3.46944 | -45.91047 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66ca4137-e808-3915-b28e-e9ced5c666d9 | -1.96348 | -48.38446 | 2024-11-22 03:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1c2b7990-efce-35e8-88cc-55bcb73f3f94 | -4.4377 | -42.59113 | 2024-11-22 03:49:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80d78f71-0ecc-357c-9958-addadac31105 | -8.7233 | -44.01328 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 811e4bc3-b344-3b95-b0d0-e53f5a666cf5 | -4.5748 | -48.02157 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 002dfb11-11ac-31cc-9e38-d096b2113c62 | -6.11666 | -42.52129 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 2e04a2c1-e4f2-3bdf-a822-a52291a4345b | -5.09212 | -45.94158 | 2024-11-22 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5eec10f-a262-3988-8669-3244453e38ff | -8.72171 | -44.02225 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5f8b815-f9d9-33a8-a7d8-6470346388e7 | -6.269 | -44.55129 | 2024-11-22 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7ffa0b54-7cdf-3df4-a84e-154f507fdbbc | -5.43216 | -45.34043 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7c2ce06-73e5-3e10-a714-2cb6cf5cf47b | -9.56217 | -37.80831 | 2024-11-22 03:49:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07e8579d-d4f4-390f-b355-12471fc68bd2 | -2.72534 | -46.0979 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10442f82-abc3-3bb9-bf87-005337612b94 | -5.50355 | -44.56409 | 2024-11-22 03:49:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51beaa53-b27c-31a8-9367-c3620dca8617 | -3.90244 | -40.9776 | 2024-11-22 03:49:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9e94c013-cb8d-30bc-b8e7-fac7137e2739 | -7.66935 | -44.50504 | 2024-11-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6fc6691-eae1-37ad-8f75-5f9b702c023f | -3.13702 | -44.86355 | 2024-11-22 03:49:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c7adc59-d702-355e-b31a-03b57bad90de | -6.62321 | -42.38534 | 2024-11-22 03:49:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 07d565a9-5307-32c0-8e84-0331028a1f60 | -5.09267 | -45.93835 | 2024-11-22 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 977c797e-63d1-366b-b4b6-cdd4fe9d1481 | -1.80275 | -48.46794 | 2024-11-22 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ae9033f-5042-37ed-bb4d-a172e3290b2f | -4.25757 | -48.70724 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bd941e3-caf3-32c6-a4f8-4d803a15dc73 | -5.12797 | -42.82049 | 2024-11-22 03:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ace3137e-3347-32c6-8e99-f1a1fdc5afa6 | -4.58057 | -48.02015 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ee93177-58f4-3290-b218-2ef855e95d17 | -5.24153 | -42.6423 | 2024-11-22 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4cbc728-1f67-31f9-bdcd-1e2da7e90598 | -1.51486 | -47.06441 | 2024-11-22 03:49:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f272f7b-4c36-3f05-be85-d8aac172157c | -8.72614 | -44.02296 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bec8b7da-aae0-3ee3-956c-2b8bcda60034 | -6.50531 | -42.19178 | 2024-11-22 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 64c2f7a1-4a52-39c5-9da7-cb68fc7803e6 | -6.1173 | -42.51741 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 3f67acf4-0661-3d2d-9fe4-17bead52900f | -7.65076 | -44.5018 | 2024-11-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 851c2d40-7fd6-364c-a9ec-3eca528c2571 | -4.54449 | -42.98233 | 2024-11-22 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 915b80f5-5a9a-3abf-961e-633dba8d3ab3 | -8.37828 | -35.36756 | 2024-11-22 03:49:00 | NOAA-21 | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14728700-1c5e-3628-ae1d-3814176b19a5 | -2.6991 | -46.08208 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe47a425-4f83-3307-9779-f3c2fa3a9dbb | -3.48691 | -42.30289 | 2024-11-22 03:49:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9454e962-5f78-3d1b-9fa8-847709dc08e5 | -4.4072 | -44.12487 | 2024-11-22 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2adaadbd-1245-35cd-a381-22f815a1a36c | -3.65518 | -42.25871 | 2024-11-22 03:49:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f80c0d53-f7d0-3c5d-ab09-83a361879f87 | -3.31209 | -45.49818 | 2024-11-22 03:49:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cfd6b45-d6d2-3c12-b5e9-70e69a95eef0 | -4.00765 | -49.91986 | 2024-11-22 03:49:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 312bf5fa-12fe-3a58-b422-83df2a9d8cd2 | -5.8212 | -44.7507 | 2024-11-22 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| abccd2dc-c42e-315c-9f2a-4b250c4cc8aa | -3.13652 | -44.86661 | 2024-11-22 03:49:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf8f932a-321e-3917-9ca9-48bb98a07979 | -4.25854 | -48.70177 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30c9630e-ff16-31aa-a86c-88cf91eca25b | -5.57788 | -42.60181 | 2024-11-22 03:49:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 59838262-ce53-3bc0-bce7-17afcf45dcb7 | -2.7224 | -45.70311 | 2024-11-22 03:49:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23b55172-b493-3656-b58e-3a414e6844b1 | -8.72251 | -44.01777 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84c66f9f-6329-34be-8bd6-04d6ae70a47b | -2.08706 | -46.28533 | 2024-11-22 03:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b4e022e-8080-393f-a1bd-6c1c8a5185fd | -4.24309 | -41.92775 | 2024-11-22 03:49:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd8d6285-cd64-3dbc-9020-105a1a094c3e | -2.70426 | -45.23295 | 2024-11-22 03:49:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 701ecfa0-e35e-3cfb-a268-264a31104e8c | -4.39765 | -44.1232 | 2024-11-22 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1edfcc1d-6434-3937-996b-f314650688fe | -5.47267 | -42.0712 | 2024-11-22 03:49:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8248a701-80b8-3bb0-8ca1-10a96d28b953 | -5.24709 | -42.63506 | 2024-11-22 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7683e5d7-178a-3477-8a56-bd809dbce683 | -8.72367 | -44.01484 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98fc070d-4a4b-3e23-ba95-1e2573f038f8 | -6.11312 | -42.51677 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7d9c341e-7115-3d28-92a5-6743f2300825 | -7.65347 | -44.50455 | 2024-11-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README14.md)
