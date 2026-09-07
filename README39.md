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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fecbc5f-aa69-3373-8f20-a4d33fd80707 | -9.72929 | -43.43449 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| fa2df349-c9c5-3c38-b43f-4b85ec68444d | -4.03797 | -50.8749 | 2026-09-07 11:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 89b0af71-ec50-37a9-adb2-95937b1f50ff | -9.73329 | -43.40277 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 362148b1-f8c4-38b0-b61c-5b7424457d68 | -4.03745 | -52.07391 | 2026-09-07 11:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 6bac55de-3eba-3adc-a813-a2c4ed359271 | -9.71962 | -43.41691 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 66f25ccf-a35f-3e7d-9993-3c2328fd073f | -3.24985 | -47.24495 | 2026-09-07 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 15a87d22-c2b6-3953-a707-92f2e75af346 | -8.92933 | -42.41957 | 2026-09-07 11:49:00 | TERRA_M-M | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 2d9ecf96-f6b3-3152-b002-11a6ced1073f | -9.73542 | -43.38589 | 2026-09-07 11:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 1a830afc-0571-3b76-a674-47b7d6f3f2d1 | -11.53356 | -49.62226 | 2026-09-07 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| cfb736e5-5899-3f3d-9db4-8a65e159c82f | -9.7328 | -43.4168 | 2026-09-07 11:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 232.8 |
| 3d9e3cb4-8d95-305e-8751-f4c61c52fe8a | -9.7519 | -43.4143 | 2026-09-07 11:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c2c8f0aa-32d5-3788-95b7-f658892b73ec | -9.7325 | -43.4403 | 2026-09-07 11:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| ac936790-a0a2-3a2f-84fb-feb7f7b31187 | -9.7332 | -43.3932 | 2026-09-07 11:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 99.1 |
| ef596942-cc2b-380e-a922-1bae22532dd5 | -15.06895 | -45.31678 | 2026-09-07 11:51:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 001dd6a7-f8b4-3877-9cc8-088a52b60f50 | -14.91908 | -44.66549 | 2026-09-07 11:51:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 738c0de9-0eef-3d0f-be65-cca14b551a83 | -14.25469 | -43.70025 | 2026-09-07 11:51:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 69bb5184-2691-3154-a96f-d55d0394052c | -12.7688 | -52.84175 | 2026-09-07 11:51:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9033d1bc-c53a-3df6-9db9-22c4ee883473 | -20.43161 | -57.41125 | 2026-09-07 11:53:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| f6085fa6-abe6-3c67-8edf-fc5cc200e387 | -20.43366 | -57.41858 | 2026-09-07 11:53:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 0161108c-e098-31d7-bf47-3c309b625d48 | -9.7332 | -43.3932 | 2026-09-07 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 120.1 |
| 49a2ac95-9a58-30c2-a844-ff51da4adf2c | -9.7325 | -43.4403 | 2026-09-07 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a36de8e5-7c91-3e6c-8b4d-ea1b6a2450bb | -9.7328 | -43.4168 | 2026-09-07 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 20477858-adb0-3cb8-8adf-6d11960b9f78 | -9.7325 | -43.4403 | 2026-09-07 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c422e2f2-57e3-3ea1-868a-04ba8c678237 | -9.7328 | -43.4168 | 2026-09-07 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| deff76ae-d99e-3713-b7d5-37731fbf0e9c | -2.6387 | -46.7817 | 2026-09-07 12:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| edbfe06f-b825-3614-bd62-3068dec5b81c | -9.7332 | -43.3932 | 2026-09-07 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 4f86833d-c635-3fcd-844f-3ec31d097bd5 | -9.7332 | -43.3932 | 2026-09-07 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 926dad5f-9780-35ce-bfcd-b3f867c1f370 | -9.7519 | -43.4143 | 2026-09-07 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7f913141-40bf-3b67-87e4-3b6394b28403 | -2.6387 | -46.7817 | 2026-09-07 12:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 23f3c62e-a6ec-333b-9b6f-82f3a65fd26d | -11.5001 | -49.6109 | 2026-09-07 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 515dcc2e-172f-3a5b-9441-152a69598acd | -9.7328 | -43.4168 | 2026-09-07 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 223.6 |
| a19369c4-a101-359c-9796-e6a8038d35da | -2.7582 | -49.4771 | 2026-09-07 12:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| fcdbaec4-d9be-3780-a882-eaff440b2589 | -9.7325 | -43.4403 | 2026-09-07 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 308f5f7e-cfd4-33bd-8599-fceb507a2f1d | -11.3443 | -45.0828 | 2026-09-07 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| bb972fdd-86ce-316d-86e6-279e182de2db | -9.7519 | -43.4143 | 2026-09-07 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| fc4e337e-d89e-3ac1-bf1d-a56054b52c82 | -9.7332 | -43.3932 | 2026-09-07 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 5ef56381-446d-39b9-bcad-839e670bcf36 | -11.5001 | -49.6109 | 2026-09-07 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| e894d7a3-abeb-3f5c-b2c6-bf18f03adf4d | -9.7325 | -43.4403 | 2026-09-07 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| ab684284-dffe-3134-ba74-5a297b5b35b3 | -2.6388 | -46.7597 | 2026-09-07 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 91776074-81ed-3361-8410-d9509fba9ed8 | -2.7582 | -49.4771 | 2026-09-07 12:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| ab836946-f378-370b-b52e-bc40a62c1da1 | -9.7328 | -43.4168 | 2026-09-07 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 54dd96e4-62f8-3979-be24-b420781220d6 | -2.6387 | -46.7817 | 2026-09-07 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 18d76f7b-d109-3b1d-b2f3-90be5e2613da | -3.5407 | -48.1673 | 2026-09-07 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c7b6f653-18d2-37b0-b609-87021455f5a1 | -2.6388 | -46.7597 | 2026-09-07 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c9b66cae-0ac4-315b-9a28-7c7801b2e548 | -2.6387 | -46.7817 | 2026-09-07 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 365842d2-0de7-32ca-af2f-ded00948c89f | -9.7332 | -43.3932 | 2026-09-07 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 782d07e9-bee4-35ab-905f-e9addeaba6c1 | -9.7328 | -43.4168 | 2026-09-07 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 79cd2379-08e3-3ca0-a62a-ae61acf6dd00 | -9.7519 | -43.4143 | 2026-09-07 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 286.8 |
| 8230d2b1-7fd5-3ac4-9a9c-d10844b343a5 | -11.5001 | -49.6109 | 2026-09-07 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| d6059d21-73fc-38fa-9a90-5e4b058dcdbf | -2.7582 | -49.4771 | 2026-09-07 12:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 28cd011a-90aa-3ad1-9776-8257ee4f369f | -9.7522 | -43.3907 | 2026-09-07 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 325.1 |
| 21f4944f-3ac8-3b78-810f-495d64ccb4d6 | -9.5267 | -41.9919 | 2026-09-07 12:40:00 | GOES-19 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 77adfa09-7166-34ea-a0c1-2a1975660aa8 | -9.7325 | -43.4403 | 2026-09-07 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 6190af10-412f-39a7-852c-c6f26187dc3a | -11.3443 | -45.0828 | 2026-09-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 9e45882c-be87-31b0-8e08-0f8ca556de3c | -9.7332 | -43.3932 | 2026-09-07 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 181.5 |
| 6c608dca-8ade-3571-9ed5-3fccf6e3d1c2 | -2.6388 | -46.7597 | 2026-09-07 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 3e46e52b-1fc9-3c8a-9670-0193472b297e | -4.0451 | -50.8847 | 2026-09-07 12:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d274b90a-af78-3ddf-b818-c38d0dec9ce9 | -9.7325 | -43.4403 | 2026-09-07 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 18d19595-2421-353f-9d78-01db8cecfcd7 | -9.7519 | -43.4143 | 2026-09-07 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 262.1 |
| 57e38ab7-e692-31f6-bb52-805cfd365dc4 | -9.7522 | -43.3907 | 2026-09-07 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 221.4 |
| ef13db98-e1ff-3858-a54b-dcff52197a6b | -9.7328 | -43.4168 | 2026-09-07 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 7e2da57f-0baf-3be2-81ef-3ac1247b765b | -9.5267 | -41.9919 | 2026-09-07 12:50:00 | GOES-19 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 620b4cfd-5a14-3b84-9695-25e7fc110552 | -2.7582 | -49.4771 | 2026-09-07 12:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 00e2c6a9-f3a8-309d-8ef6-1cc4ca3babc3 | -2.6387 | -46.7817 | 2026-09-07 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 224bdaa1-2c2d-3be4-b2e8-30f31b0f4610 | -9.7325 | -43.4403 | 2026-09-07 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| b86ee57b-7580-34be-8513-4bdf28520cd9 | -9.7332 | -43.3932 | 2026-09-07 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 178.7 |
| b25e2ae9-71aa-3b77-877e-1e1da2fa6030 | -9.5267 | -41.9919 | 2026-09-07 13:00:00 | GOES-19 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 246.3 |
| 2d309fd8-0ab0-3d6e-890d-b507bdc36639 | -2.6387 | -46.7817 | 2026-09-07 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 0e8d4381-1355-3b43-9239-f9caef4406e5 | -9.7519 | -43.4143 | 2026-09-07 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 301.9 |
| 2a8f8a9f-4882-3201-853f-0aa3020b72c5 | -9.7522 | -43.3907 | 2026-09-07 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 199.8 |
| 9dd1898a-8fc9-30a6-95ee-6befcdb8954d | -2.6388 | -46.7597 | 2026-09-07 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 61c3a74e-8748-3364-ba2c-1b3d6c5f436e | -9.7328 | -43.4168 | 2026-09-07 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 294.7 |
| 176694cf-fff9-34f3-8400-ba3a689b863f | -3.5407 | -48.1673 | 2026-09-07 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 774889cb-db3a-3b9a-8343-2da37887c173 | -2.7582 | -49.4771 | 2026-09-07 13:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 626f0241-432f-32ce-b837-a41eff0b9914 | -2.7582 | -49.4983 | 2026-09-07 13:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1e217fbb-105a-32bc-a477-4c26d81e4645 | -11.5001 | -49.6109 | 2026-09-07 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 537f2551-943f-3211-82ac-0b6dcc4a0021 | -11.3443 | -45.0828 | 2026-09-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| ade35e04-5894-3a69-a407-ce3c70558555 | -11.3251 | -45.0855 | 2026-09-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 68b21b89-0bda-3574-b3c7-57c5440b32dc | -3.5406 | -48.1889 | 2026-09-07 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cf989b46-db9e-3a4b-8d1b-027f1f7e92a1 | -4.3516 | -48.9713 | 2026-09-07 13:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e8263a10-410b-35a6-813e-32395b627594 | -4.3516 | -48.9713 | 2026-09-07 13:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e4ee3f15-b6fc-3efd-ae0a-d8c2cf7ad822 | -11.3443 | -45.0828 | 2026-09-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 1d7dcd10-2e0d-3e4f-ab83-0bfa97801b89 | -2.6388 | -46.7597 | 2026-09-07 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 1aa018cb-c0a3-3d56-85c3-a690073ef812 | -2.7582 | -49.4771 | 2026-09-07 13:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 243.4 |
| 7d727d5b-7af0-3ceb-8f0f-f8e5eb5f97de | -2.6387 | -46.7817 | 2026-09-07 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 660bd044-844d-347e-acda-f9deafe49150 | -11.3251 | -45.0855 | 2026-09-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2f91b8a1-7549-3f5b-a460-f55f0ac5a954 | -9.5267 | -41.9919 | 2026-09-07 13:10:00 | GOES-19 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 191.4 |
| 6b7a1a5e-fa3f-3f31-a60b-2157531e40ea | -4.0451 | -50.8847 | 2026-09-07 13:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 340ec23f-7732-3ef7-82cb-55968df67faf | -9.7328 | -43.4168 | 2026-09-07 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 320.0 |
| cbcee4b7-343f-38a0-87a8-29e296b17746 | -11.3251 | -45.0855 | 2026-09-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 17c0c223-4a00-3140-b9d1-be4ca533aa70 | -11.3247 | -45.1086 | 2026-09-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5b0b7204-6e9b-34a6-bcfa-7eb1d48638cf | -2.7582 | -49.4771 | 2026-09-07 13:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 247.5 |
| eb9a4c40-cf9f-3ce9-904a-64d22f84a14d | -2.6387 | -46.7817 | 2026-09-07 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 047b9fd7-d40e-3ec7-a07e-02b27ec5d60a | -3.1461 | -60.6696 | 2026-09-07 13:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 86d1f702-09f6-39bb-81c4-82dc0d09b21e | -11.3443 | -45.0828 | 2026-09-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 339.1 |
| 7f7c470e-1fc2-38df-b0f7-1568cf2b84de | -4.3516 | -48.9713 | 2026-09-07 13:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 122bdc34-98b5-34db-88e0-391a246d5137 | -11.3447 | -45.0597 | 2026-09-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f011a9f2-d015-3562-b56a-95e089aa2814 | -2.6388 | -46.7597 | 2026-09-07 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 20f9c63c-5546-3833-a9f2-dfb87a00f0ac | -9.7325 | -43.4403 | 2026-09-07 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 2fd56f5e-a411-3e9a-8493-2dc4716031cd | -2.7582 | -49.4983 | 2026-09-07 13:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |


[Clique aqui para ver as próximas entradas](README40.md)
