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
| 65b738ed-1df4-35f8-b6ff-35f9894cb004 | -13.67059 | -41.37072 | 2025-08-03 03:15:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 84a7f84d-1399-32e9-b9ea-c35e129e3ddf | -13.69004 | -41.37426 | 2025-08-03 03:15:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dab09bc8-821e-3567-9c10-ccb5487b8f7a | -20.06768 | -43.74672 | 2025-08-03 03:17:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4c7299b8-9bff-367d-8c1a-13cdcfc0c8e8 | -22.73977 | -42.9622 | 2025-08-03 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0aca1938-8ca6-3a2e-8905-118a6c54f13d | -22.73386 | -42.96053 | 2025-08-03 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 91373b30-3230-3932-832e-54dabf3af4db | -4.5497 | -44.2047 | 2025-08-03 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| af230ae3-417f-347d-af28-8fad23d0626a | -4.5684 | -44.2036 | 2025-08-03 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| d47629e6-a1e6-3add-914b-0ef15786a7e9 | -12.6402 | -44.4913 | 2025-08-03 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| ee454232-4e40-33e0-b5f5-8f27fe662f64 | -6.656 | -59.0981 | 2025-08-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 15822ac8-d83c-312d-91d2-3b37416c14ef | -6.6559 | -59.1174 | 2025-08-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fae9f6ba-2d24-3745-9ab8-e79b7ffca1c8 | -12.6402 | -44.4913 | 2025-08-03 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 1e9fceda-ac66-3d9e-a9ed-ee90a28a4568 | -6.6375 | -59.1181 | 2025-08-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 59ae625b-49b6-3868-91ea-df3dc7640064 | -6.6559 | -59.1174 | 2025-08-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 144785fe-a693-3973-a02b-9b1240e788ea | -12.6595 | -44.4882 | 2025-08-03 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 9a7dd06c-1437-389d-9d7e-7ec51dd72f03 | -6.656 | -59.0981 | 2025-08-03 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 20a4705a-8a32-32ab-b52a-3be0260d6773 | -2.90607 | -40.13531 | 2025-08-03 03:34:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e7c0f8b0-918a-3832-8751-11f610a0c482 | -3.80983 | -42.54142 | 2025-08-03 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dac70b8a-c035-3c5d-b33d-fe2d232ec818 | -3.81525 | -42.54237 | 2025-08-03 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c8c0ea2-dcb0-368f-b003-7fc8b549a55f | -2.90889 | -40.1334 | 2025-08-03 03:34:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93fbdccc-0fbd-31c0-b1a2-a2fd973d80c2 | -3.81382 | -42.54142 | 2025-08-03 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d5b619b-bd19-363f-b6b1-7b3733370129 | -4.77141 | -45.34022 | 2025-08-03 03:34:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0a318f98-6461-32a3-a16a-800bb37591d2 | -5.51356 | -35.58138 | 2025-08-03 03:34:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 65166ae8-764e-3392-917e-9b799acd1490 | -2.93882 | -40.09783 | 2025-08-03 03:34:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3aa5ce7d-2923-36b7-85a1-e61084a3bbf8 | -2.90421 | -40.13263 | 2025-08-03 03:34:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a802a01-0687-3921-818a-0e24d2f0e8d7 | -3.81324 | -42.54496 | 2025-08-03 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5723eb0d-2f4a-30c6-afb3-bd1ebf03fa15 | -5.092 | -37.89199 | 2025-08-03 03:34:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7848825e-fb76-39de-8d15-6c75899d423b | -7.96351 | -45.10479 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| efe44945-bc8c-309b-b7dd-9b2e3a83cf91 | -8.00653 | -43.17768 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 30463239-755b-3c94-bac2-8b34e8df4ef7 | -8.00615 | -43.15017 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| fd9f8172-a8e8-3d83-b78f-587c4bcbcb43 | -8.01789 | -43.14551 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 239c06d1-24ce-3332-9267-0bdbb42a4181 | -8.01263 | -43.14456 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 72a87db7-349a-336b-aad0-f44bdcb0b11f | -8.01849 | -43.14224 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 576f3658-0b36-3e70-b88a-eff661b6d303 | -11.75121 | -44.97689 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c23e6eb2-a240-3abd-b39a-8a749c893d1d | -8.00774 | -43.17113 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f4fe372c-ef24-36df-a566-194519aa0a09 | -8.00835 | -43.16781 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4075a0ac-5366-3388-8f10-01d880975d0a | -7.96519 | -45.09594 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 321cf92c-bf4b-34ae-8b26-9f92399698d4 | -8.00937 | -43.16679 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a10bcf32-166c-3a04-aad5-37d3a15b6b2c | -7.11459 | -43.48346 | 2025-08-03 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aad802c7-5115-3411-ba6f-de7a9e909476 | -9.39927 | -45.50111 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e8828d4-566b-3aee-bd1c-b8e227dc17e0 | -7.96179 | -45.11381 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87398353-5a7e-3b53-9538-6ba34e81be5d | -7.88258 | -45.52883 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e67460fd-cceb-361e-a6d7-d536ac7470f5 | -8.01405 | -43.17117 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 20bb008b-c0c8-3d1a-8edb-f8b4e0cd9d8e | -7.96771 | -45.10329 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c367ad17-2d04-3854-a019-6db379e3c723 | -7.87672 | -45.53071 | 2025-08-03 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2d9fc52-fc62-32a4-b0f0-d653f0dea3e3 | -6.50119 | -42.81393 | 2025-08-03 03:36:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cbb33006-9505-3e4d-8946-7c06808b2528 | -8.04608 | -43.1102 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 63b2b239-41e2-3995-9a45-748805636a28 | -8.04024 | -43.11248 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 163672b8-734d-3e1c-938b-f28d759845f8 | -9.39497 | -45.50228 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| da8b8673-3b58-343b-9db2-b1cdba6f16e4 | -8.0129 | -43.14678 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c3c1644c-e7fd-3ca2-a878-2d2493b55f0f | -8.00347 | -43.19429 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| abc17159-79b9-3b01-959d-41ea679ef4f8 | -8.0082 | -43.17344 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 11953e6f-7455-3d59-bfe7-9ef1bd48a652 | -8.0043 | -43.16022 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 433b5721-2710-3e1a-a741-8673b69c5cb7 | -10.33711 | -44.90855 | 2025-08-03 03:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b843730e-9e52-3300-82de-42527844f6e4 | -8.01323 | -43.1413 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b537e1d6-fa9d-3a8f-8f50-9fe7e4740d30 | -7.75632 | -45.11821 | 2025-08-03 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb922675-2780-3a1f-ba81-c2a2c5908288 | -8.01142 | -43.15111 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 8f00686a-1666-3fab-9600-f35e6da61a4e | -8.00676 | -43.14689 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d254bc5a-f208-3931-b8e6-5b19effff67b | -8.00762 | -43.17672 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ccd7407f-2f55-3897-b91e-adbb609640b4 | -8.02047 | -43.13464 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 88a6d801-172b-321f-96eb-3d757e54665f | -8.00058 | -43.18577 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 1392257f-0afd-359f-8ba1-6e31c28189c2 | -11.753 | -44.99767 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e3c852-5e25-34b5-88bc-14459ba81400 | -8.941 | -46.75319 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9ae50bc-e21b-3e25-9f06-73e88ff9c57a | -7.97118 | -45.09694 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af329178-e83c-3198-9709-9ef79895df32 | -7.99645 | -43.1783 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| ef59057b-f932-3669-b820-c9045b9b776e | -8.93446 | -46.75213 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| edb17617-8256-36f2-807d-eb4968a3697f | -8.42025 | -47.46255 | 2025-08-03 03:36:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef04fc97-9c68-3aa4-b0d7-6457c1b018ba | -7.96435 | -45.10036 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 679a38fa-ae09-3ca8-ba29-b2f154e49ca6 | -8.01348 | -43.14351 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f1fcb892-ac44-3672-98a5-712a161d3850 | -8.00117 | -43.18242 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 4fb5b701-c4f0-33b2-8418-b861a52cabe6 | -6.52481 | -42.80353 | 2025-08-03 03:36:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fe003c8-a4fd-3c37-9423-54517bc970c3 | -8.02219 | -43.12486 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3cbeca9-1196-3644-aceb-0d0f5d02603e | -8.0197 | -43.1357 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dfb737bd-c347-3d77-820c-481866394f62 | -8.01202 | -43.14783 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 83ae0cd9-397a-386d-9756-980fcc849f19 | -8.00958 | -43.16112 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b520630c-3841-313a-85ba-45be93d15967 | -7.22827 | -36.69026 | 2025-08-03 03:36:00 | NOAA-20 | TAPEROÁ | PARAÍBA | Brasil | 2516508 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a9620d70-9f4a-327e-a9e3-8bede344c9a4 | -11.78375 | -45.00985 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c618049-75d3-380e-af73-ecb584644c15 | -7.10915 | -43.48235 | 2025-08-03 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8496e898-42b7-33d7-94e2-5cd8ffe262c2 | -7.88352 | -45.52388 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f2dd1435-a235-3d47-83b7-2bb56c906a39 | -8.00593 | -43.18096 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6efb5fc2-feef-3547-a7f3-e5a7c98ca051 | -7.9947 | -43.18267 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| a8430aab-61e0-3570-b153-ccf22b81d656 | -7.21871 | -35.77645 | 2025-08-03 03:36:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c637652e-7623-3c2e-81b7-336de3de19bf | -8.00185 | -43.1735 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 1996c489-b630-31e9-9ece-188706226d28 | -8.0047 | -43.19334 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ff4affae-33c4-355f-95b7-2cadf2420be0 | -7.95762 | -45.12463 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a92227f-f651-3cdb-9060-fcb2361e83d3 | -9.39248 | -45.50426 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 234f7519-467b-3f57-b955-f737a0ddb588 | -8.94111 | -46.7487 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f95c8fef-fc32-34fa-a3c1-33138f0ce6f8 | -7.96607 | -45.11229 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50cf3f10-6daf-38d9-8a66-721cf615b1f1 | -12.03673 | -44.01796 | 2025-08-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f54d9f9-ecec-38ab-8d06-2717aff3f8a2 | -8.01239 | -43.17545 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a9ab3e6f-9a28-3492-b07d-360fc3d9d76c | -7.95409 | -45.12166 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 353e6543-6353-3b71-b26f-78bf24883629 | -7.96264 | -45.10931 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c3a34006-e846-3d2b-9404-648a6a70f1a8 | -9.38903 | -45.50092 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e57d07f-f821-36b7-a9e8-50f0293e7f38 | -8.0102 | -43.15775 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2a3a4dc7-8c50-346d-92e9-3a754e1af84e | -6.20619 | -46.3538 | 2025-08-03 03:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85a4c297-0682-3a3c-9562-46b9fa3f87a5 | -8.17058 | -34.9802 | 2025-08-03 03:36:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cd2fea99-dc79-3456-833c-84b91cab1399 | -6.51893 | -42.80603 | 2025-08-03 03:36:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f7e6341-a3f1-32ca-95c8-5e2db7f4d07b | -8.03965 | -43.11573 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c5202108-50d2-3d82-abfd-9eb578e45d02 | -7.96852 | -45.09885 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96e031c7-27d9-3a8c-8692-85089c981a6a | -8.02854 | -43.1171 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5ea9ed9a-8b9d-34a5-8585-ff2da9bf620c | -11.77593 | -44.99092 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
