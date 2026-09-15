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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbb1e575-7a1b-376c-ab40-50a119ce7867 | -13.59408 | -47.91385 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87f03acf-de4c-3543-aee8-7c98da804051 | -26.82597 | -52.79168 | 2026-09-15 04:19:00 | NPP-375D | CORONEL FREITAS | SANTA CATARINA | Brasil | 4204400 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbecba71-8838-3289-9f81-c539f768b9ba | -27.52395 | -49.64316 | 2026-09-15 04:19:00 | NPP-375D | PETROLÂNDIA | SANTA CATARINA | Brasil | 4212700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8518a25-5ffa-3131-9a0c-5f160a436348 | -4.51096 | -54.97202 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5b4738e-1912-36ee-a87e-7ec3fff0e037 | -7.23355 | -46.14698 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4345a27c-ca6a-3110-9dc5-d9d0f9e50f0a | -2.90001 | -50.39521 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4504c17c-eb22-3cc0-8b7b-56dae3ed5e7a | -3.01968 | -51.37421 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f59ba56-b1c5-39c9-96d3-25f37329a6b4 | -3.15701 | -58.64281 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d28c06c9-29f2-3146-815e-e61d5584702b | -2.91812 | -50.40852 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71317210-192d-3d91-ae2f-f51a8d26a616 | -5.29178 | -49.08917 | 2026-09-15 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c8ee5d-4ddf-3fd1-9e1f-2a035000845a | -7.01814 | -44.63226 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24859c88-cfef-3b8b-8e6d-c44ac1ccba7d | -7.10422 | -41.80778 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ed9a76f7-9e8a-3380-8170-aced74044288 | -5.33513 | -49.09206 | 2026-09-15 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d9fa0f7-e02f-35e3-ab38-e05074bdb378 | -2.91977 | -50.39838 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf08b76e-9147-33b8-ae1c-10e4bc46687d | -4.56493 | -54.90924 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32a2a980-7cc7-367d-a1ca-5def3b8eb8a9 | -4.15644 | -40.85831 | 2026-09-15 04:32:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c24ec8d-1639-3207-b417-36f57ef29d9e | -6.95044 | -42.55758 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74b2f300-9972-3203-8cc7-c168e92566f6 | -2.57886 | -49.44316 | 2026-09-15 04:32:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15fa2d7a-f7bc-32f1-b14a-7ac488020b30 | -3.33545 | -54.19082 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f4238c6-4395-308b-aaab-25a47af62936 | -8.10848 | -45.62728 | 2026-09-15 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1db7f67-15fe-315b-aa44-99312575bec0 | -2.684 | -57.58979 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 02f849d1-6053-30ce-9109-654187697029 | -6.36041 | -55.83652 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2396bd4d-54e5-3988-b400-71c662ed5ef3 | -3.96859 | -52.22299 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d858c173-f17d-37ac-9f29-9fd252e29ca0 | -7.16976 | -43.5215 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 68f5e062-f831-38b0-b6a2-ee68db7419ad | -2.89813 | -50.43131 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e85c517-a133-36e6-889d-96c84989fd23 | -5.1952 | -49.33086 | 2026-09-15 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86aca091-bbbc-352c-9e27-916e3389c6c8 | -2.88034 | -50.46508 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be032103-61a6-32a7-b428-7ce05e6a41a2 | -3.41711 | -58.2268 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bbf3770-230a-343b-ab28-ced28d32a191 | -5.83091 | -52.09486 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 150b4a05-59e8-3a0a-9b4f-283ab81fc533 | -2.66364 | -57.56484 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bfbbdf9-e75c-3c07-be63-d90405b6ae7d | -7.1304 | -42.0904 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fb5f7a81-9099-3bae-911a-4cc14fa091e0 | -7.56399 | -41.84299 | 2026-09-15 04:32:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4fc842bf-693b-34a5-a566-fef064b72c3f | -3.37172 | -45.09167 | 2026-09-15 04:32:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 548aa55e-a6c3-3c6a-bd3f-531fb4db177f | -3.01589 | -51.21265 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9f5b784-445d-3b45-9815-18a2595ba2c0 | -5.64124 | -40.8559 | 2026-09-15 04:32:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 03f75ea4-248c-306e-af73-735bb84d6887 | -1.22584 | -54.13902 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89c66b11-ebaa-3b18-8282-7ae179490013 | -3.07893 | -50.57623 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa3f7e7f-f969-3a7f-97be-fb0846d2f1e8 | -5.61711 | -43.5597 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc0df2db-1f67-3f54-bf8a-1a9f632cc336 | -4.49598 | -45.90977 | 2026-09-15 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4e29ec2-3a40-39e8-ad74-6548afb1dbec | -5.63356 | -40.85056 | 2026-09-15 04:32:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 72ac84c4-2551-32c6-85bd-15e3b2874299 | -3.49367 | -50.3788 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 514722cd-bfe8-376a-931b-3e2b62a8d2c1 | -7.16553 | -43.52508 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d455d452-3dcc-3f90-9883-f0c632364686 | -4.18369 | -48.68663 | 2026-09-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5ac8bcc7-b049-3e4e-b501-83249e6c441f | -7.10023 | -41.80723 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 01ef93d8-42f2-3837-a7ab-8434afdb0135 | -2.78306 | -51.36464 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5d3ed39-3730-3710-a58c-d4922e903598 | -3.48664 | -50.37258 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6bc1b1af-017e-3e31-80ae-0b1d6f2edf8f | -4.53864 | -55.62393 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b045df1c-7932-3b8f-ba17-8e31d739de60 | -6.16199 | -55.70752 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22e8000d-2553-3e87-b877-d846601e609b | -4.53802 | -55.62749 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aa75183-8fe0-3ede-856f-4c5785c0065f | -2.96242 | -50.41051 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba142808-c70c-3319-bc44-9561e3684ca8 | -3.07154 | -50.57144 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c859f8d-d9d5-35cc-bebd-84f1420bafb0 | -7.61257 | -47.29239 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af573d84-fcf6-36ae-92d2-46dbbf82360e | -2.90147 | -50.41103 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 578cb000-1e89-33e3-9b39-a5c04c958ab1 | -3.68704 | -44.18227 | 2026-09-15 04:32:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca457c22-7ac9-3c19-907e-a07bd41328fc | -3.39537 | -50.75567 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 307c4910-f44e-35c3-ac65-65a9722525bf | -2.9537 | -50.41427 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10f6b408-8d5e-3ce3-b249-b3cb87f44f33 | -1.19608 | -54.1234 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efa14c73-ce6b-3dbd-b7b7-ec9030869cb1 | -7.47943 | -42.11448 | 2026-09-15 04:32:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e17918f5-d6aa-3851-a832-23007ba59fdf | -2.69106 | -57.59649 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3b2dba5-29ae-3071-bae7-19921a21fc59 | -7.09518 | -43.54079 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9816bc16-9c2d-3f16-a487-76e63440b7d7 | -6.9557 | -44.53825 | 2026-09-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4d8aa83b-cc92-3f27-bf44-eabd35810147 | -3.07208 | -51.07601 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02d0fa60-acdc-38da-aaa1-8eb682021f00 | -6.49991 | -47.1318 | 2026-09-15 04:32:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37141b86-cff4-306f-82c2-12ed0dfafb23 | -6.67588 | -46.19387 | 2026-09-15 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 409c36ee-46ae-3acb-bb92-7c36c779e132 | -6.95914 | -44.53877 | 2026-09-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 84ffb2a2-80c7-3497-9edc-32af1b86a92c | -7.11219 | -41.80883 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd1dd5c6-913f-3eae-b28c-579eb18ba525 | -7.25516 | -46.67643 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff52fb47-65d0-3505-a126-7bd4a4ea1540 | -5.60589 | -43.56204 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee5fadff-de99-3e00-8c2c-2b3ecda909ea | -3.01651 | -51.20884 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69ec002e-aa8b-3a37-bd08-c1ae39f3590e | -2.65355 | -57.50975 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7c7dbf1-8325-3f44-912c-d07109213fab | -4.92051 | -49.22947 | 2026-09-15 04:32:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce167b8a-a2e4-3741-960d-5246e9cdef23 | -5.92637 | -53.54787 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 492de0b1-82cc-378b-b083-f839fc7affe1 | -4.36187 | -47.77795 | 2026-09-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cbbd6d6c-9aaf-378a-a457-8628684f80ff | -3.73968 | -54.38089 | 2026-09-15 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d60845f0-dd9f-374b-a77a-8cf2645a8ca7 | -2.69835 | -57.59237 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63113e55-0759-3d25-acc7-5953428bc607 | -3.84873 | -51.76518 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a79f568-0f52-3c06-beac-5db038e01e05 | -6.72268 | -48.12167 | 2026-09-15 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d522b3d-17c4-33aa-8625-29c1b9608223 | -3.77251 | -51.35544 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4ab143e-c1a3-3424-8f38-f1d92559197c | -4.80759 | -42.87852 | 2026-09-15 04:32:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eaca000-8df7-381d-85e2-081e917a13e3 | -3.54027 | -53.98577 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| dadb2c08-8a64-356b-af8c-5998e913b87f | -7.61589 | -47.29292 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb8d9876-9487-340d-ad67-b796ab09afc9 | -2.62243 | -50.83914 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f89354a0-2ff0-3d3f-a531-c625ea14881b | -2.03836 | -46.93991 | 2026-09-15 04:32:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e62492f9-99ec-3e74-9d49-d0eeb40f9614 | -2.82547 | -49.23399 | 2026-09-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fd485d0-abfd-3e6f-82e5-80008459bdea | -5.22415 | -49.34265 | 2026-09-15 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f38aa89f-6695-3fcc-afa9-d0b244930ba2 | -2.89021 | -50.43002 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11e56d40-a349-3a98-8a08-2c71e5ec1068 | -2.91084 | -50.42817 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03a8eff8-c6be-349b-a40a-25ab7a0cf164 | -6.32613 | -44.12318 | 2026-09-15 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89890d07-1b0a-3619-bbab-dad597735baa | -7.08453 | -41.83117 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4a1f38b0-ecee-3fc3-adad-283347e60b22 | -3.22686 | -50.58566 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 59708448-077b-36b2-a452-e447a11bc46f | -6.15661 | -55.70665 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9aaec946-17f5-3a2a-b96b-09a27ed42c56 | -7.24684 | -46.17046 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57a71648-64da-3b48-8f18-ce1b2c4d9c46 | -7.54849 | -41.83732 | 2026-09-15 04:32:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| db7faefe-1a97-39a6-997b-c51228a82c54 | -4.37993 | -55.20025 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 312a8c7e-85b2-3f72-99d4-14d2a6f9ea5f | -2.8998 | -50.42115 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d7c5769c-3eb9-3502-a371-af2191d11eb6 | -5.29468 | -49.0938 | 2026-09-15 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11613b25-e3dc-3003-8b5a-3221a39da9a8 | -5.84443 | -52.06567 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc7431e5-b3bf-3744-92c5-ec820cafb69e | -4.91874 | -49.23014 | 2026-09-15 04:32:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 417004d8-83a2-35db-a42b-6e4de87605e4 | -6.94907 | -42.56696 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8b5f5bc-0dab-375c-ac04-589abb451824 | -4.53923 | -54.93353 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README35.md)
