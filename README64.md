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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7e037e2-6514-37a8-b386-e884c91ccffb | -5.8149 | -42.8167 | 2025-09-27 13:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 79648958-5b6a-36a9-ab6a-7488d2e6c009 | -11.4417 | -44.9767 | 2025-09-27 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| c3dc368c-e4d4-36fc-9b6c-d92a8bdbd954 | -10.0062 | -46.7081 | 2025-09-27 13:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| bd4a3031-b758-3301-9166-a42f3c2dcfd7 | -9.3519 | -47.558 | 2025-09-27 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| cb40b71e-f634-3f23-9c40-05e6baa9b619 | -8.822 | -46.2564 | 2025-09-27 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 323.1 |
| 437291d6-a59b-3d00-92f2-08b007735623 | -11.6058 | -45.4364 | 2025-09-27 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 9cf81119-8b57-31d4-b254-031708ea2dc1 | -5.1887 | -43.7263 | 2025-09-27 13:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9812eeb6-59e7-357d-b63f-5639f7b7c53e | -9.6159 | -47.5741 | 2025-09-27 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f9292c90-e256-3841-96f5-67e095102974 | -9.9772 | -43.5962 | 2025-09-27 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 7472fe44-bb3a-3ff2-b3c0-ddbbf5109caa | -8.6442 | -43.9931 | 2025-09-27 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7f80b29c-575b-31dc-88ec-4d8001086990 | -9.7386 | -48.286 | 2025-09-27 13:10:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9fcf4569-ea1d-355e-9a58-a55ace5db7e0 | -7.7794 | -46.9371 | 2025-09-27 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 3c1196ff-5e6b-36f2-81cb-76d6ecb03f25 | -12.2829 | -44.0568 | 2025-09-27 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 195.4 |
| f5ea9618-589c-3742-a615-fb6cafc06187 | -11.3646 | -45.0108 | 2025-09-27 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| bf453792-7927-39fb-9b93-99c686d8febe | -7.7792 | -46.9593 | 2025-09-27 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 4c849d78-3af5-3d00-9b87-217a5c1aa00d | -11.6062 | -44.3257 | 2025-09-27 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b9129cf9-e1dd-3661-941c-e9eef185d837 | -5.8295 | -41.2895 | 2025-09-27 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 9ffbc716-b6e3-39a9-9f49-b5b7ed1fbdac | -8.8409 | -46.2544 | 2025-09-27 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| dd0cb657-f650-38b5-bb2e-963bf4bf3a55 | -7.8637 | -44.5382 | 2025-09-27 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6e44cb96-8616-3194-a43d-1155736e85d5 | -5.7588 | -42.7976 | 2025-09-27 13:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| d2a21df3-3e5c-38df-aa91-55f5a637db1a | -5.7775 | -42.7961 | 2025-09-27 13:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| c792faed-93b8-37f7-8f5e-2167df1d4212 | -11.4413 | -44.9998 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 249.1 |
| 08520afd-f82f-38b3-a2eb-74842b72a370 | -14.0613 | -48.8321 | 2025-09-27 13:20:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| acc192b7-276a-3561-9a6b-48a9351fb347 | -11.6058 | -45.4364 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5d872017-d901-32c9-8133-703338358e43 | -13.7109 | -51.1861 | 2025-09-27 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0dc3df80-770c-3a0f-8a20-847b85547133 | -7.3849 | -47.0157 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fb6d8f77-48ca-38e8-a1c1-cc8b1e73676e | -11.4417 | -44.9767 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 0ec5d80b-cc63-3d42-9a49-49631f5318c9 | -8.4825 | -47.8421 | 2025-09-27 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3f57f134-155b-3ca9-b1ee-62040a28b95d | -10.0062 | -46.7081 | 2025-09-27 13:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 521fcaa4-f386-3a1a-9861-526937f08a03 | -5.7775 | -42.7961 | 2025-09-27 13:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 07614989-823c-3d87-9d0b-c3fe2b461f0c | -5.3693 | -42.3077 | 2025-09-27 13:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 7012d1c0-9ae5-3717-a28f-2cceb01b07b3 | -14.85 | -45.3911 | 2025-09-27 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a3f387c8-35b8-35a2-bee6-c27add737e27 | -8.8226 | -46.2115 | 2025-09-27 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f7d7f4d0-3753-3684-a121-4e1aca1eca66 | -17.1739 | -56.3892 | 2025-09-27 13:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 9fca7cfb-4ef2-3d6c-90f7-ce351595d832 | -8.8409 | -46.2544 | 2025-09-27 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 044bef65-cb99-3d3b-b273-11f1edfd0b0e | -14.8448 | -45.6246 | 2025-09-27 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 35def212-8fa2-388f-af7d-79922f4256a6 | -11.6062 | -44.3257 | 2025-09-27 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| efbcb42a-1d0f-340f-bbb6-98436764023d | -6.6983 | -42.7646 | 2025-09-27 13:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| ab4d4515-ada6-3f9b-8bfe-bfedd15f7463 | -14.8454 | -45.6013 | 2025-09-27 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 18730f4d-6796-3d6a-a636-fd1ad0086538 | -11.3451 | -45.0366 | 2025-09-27 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 01396e5a-79cc-3508-8864-abad1ab216a9 | -12.0369 | -47.0543 | 2025-09-27 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 3ae952ea-e764-3192-a9a4-4bb7af28eb20 | -12.6498 | -48.1509 | 2025-09-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f7c06d7f-17e7-3455-b35e-7e564f3f3291 | -9.3343 | -48.9364 | 2025-09-27 13:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 542dfd63-ed80-3297-9070-099edbd0440e | -7.1571 | -45.5158 | 2025-09-27 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2cbba11c-1915-3b6e-945f-2f1d7526d11c | -20.7342 | -57.7873 | 2025-09-27 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 15fb826f-ee85-37b4-a743-b87d3d149c13 | -5.6813 | -43.0619 | 2025-09-27 13:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| 80163ad7-b560-358d-a717-d5f7d3caeeaa | -18.3049 | -57.0938 | 2025-09-27 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 4d07174e-dbbc-370f-b7d9-4eb487dc4957 | -11.3642 | -45.0339 | 2025-09-27 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 8edfade2-48c5-313b-85ab-51c1d6f3c7b7 | -7.7794 | -46.9371 | 2025-09-27 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 277.6 |
| 635367d6-3a65-39c6-a61f-80fc1618939d | -11.4225 | -44.9794 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| fc0e2b19-8f50-314f-a116-70b891dcdf1d | -9.3517 | -47.5801 | 2025-09-27 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 0d5a8b02-5e79-3f2e-8580-de7474d50cae | -9.6162 | -47.552 | 2025-09-27 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d7595ef0-6800-36b1-9f7b-b5f065c4e29b | -11.4425 | -44.9303 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 850f5eec-a76d-304e-9ba5-45137d87853b | -5.7588 | -42.7976 | 2025-09-27 13:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| d0f52e96-3773-3458-90b7-c72b8ebbbdc1 | -9.6159 | -47.5741 | 2025-09-27 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| da5e03c8-4890-31f5-9bed-806b109445a2 | -5.7961 | -42.8182 | 2025-09-27 13:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| d7b0c105-fc47-3500-b11d-617b6f905738 | -6.8444 | -43.1745 | 2025-09-27 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 0140756c-797d-3da1-9b4b-6b9deb384922 | -7.3847 | -47.0378 | 2025-09-27 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 1d726bc5-d564-3b84-8801-9f30a644f8b5 | -8.822 | -46.2564 | 2025-09-27 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 0eda6ac2-65b7-35c9-8e10-844bfd3f8dcf | -14.0807 | -48.8292 | 2025-09-27 13:20:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a3184563-0e08-3849-b492-c775417bb1a2 | -11.3646 | -45.0108 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| cdf71ea4-1c68-319d-9124-0a0b234bb6b5 | -8.6439 | -44.0164 | 2025-09-27 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d6835ba6-e1cc-33fb-baa6-3573fc9170c1 | -7.7797 | -46.9149 | 2025-09-27 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 9ed1166f-159a-3d58-801b-e83793305d7a | -7.5568 | -46.7128 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 97f86b93-dacb-3ce3-b9d6-9f5b055216d3 | -9.9772 | -43.5962 | 2025-09-27 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 330ab534-4874-3530-97d8-d2293ad8b40f | -11.4221 | -45.0025 | 2025-09-27 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 77b00926-6eee-3656-be7a-ee5e5350ee06 | -12.6495 | -51.6797 | 2025-09-27 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 205.9 |
| fd965475-2c9c-341c-bea8-48855e766cb5 | -7.798 | -46.9576 | 2025-09-27 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| dfc9387b-932d-31d2-96a5-32c331578135 | -5.4937 | -43.0761 | 2025-09-27 13:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4eadffee-2c29-31ac-b16e-2f8e51c367a1 | -7.5568 | -46.7128 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d8559269-2f9d-348e-bcd1-782a2d13bbb4 | -5.3693 | -42.3077 | 2025-09-27 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| e5514c94-5dc6-362c-be81-bfac8596ef2a | -8.822 | -46.2564 | 2025-09-27 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 282.1 |
| 51e3d8b1-0dd7-326c-aa67-8e6e871cf6f3 | -5.7961 | -42.8182 | 2025-09-27 13:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 24d4b339-cd5e-326f-8e16-f4db54731c0c | -7.798 | -46.9576 | 2025-09-27 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d1052c43-92df-3392-9433-ace041b639d4 | -8.6442 | -43.9931 | 2025-09-27 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 44462d2b-8229-34a0-9e07-febed5df9073 | -14.0613 | -48.8321 | 2025-09-27 13:30:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c7ca3ca0-1eb7-3368-ba19-1c13a772686e | -11.6058 | -45.4364 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 9d8b7e91-4feb-3c5c-b75b-f3a82fd230ba | -6.9954 | -44.8488 | 2025-09-27 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 66ff1658-94ff-30ae-9add-9d490789732c | -8.4825 | -47.8421 | 2025-09-27 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| e893cfd9-4f3e-3900-8391-7794ec74aa6d | -9.597 | -47.5762 | 2025-09-27 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a7618bf7-1282-3ef8-bf3c-deed907b4d83 | -6.7174 | -42.7393 | 2025-09-27 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| e17c5e88-786b-3c58-b7a1-89feee615151 | -11.4413 | -44.9998 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 2a832e03-12ea-3ef2-bc36-9dde8e1a4ad2 | -5.7775 | -42.7961 | 2025-09-27 13:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| ba89f4e9-e752-36cc-99e9-9a24f3066358 | -8.1805 | -46.3657 | 2025-09-27 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3cbc388b-9042-307e-bad6-bf6531467dbd | -12.0365 | -47.0768 | 2025-09-27 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 0d4d6ce6-c4a5-349d-ad92-a6df2d74ba5f | -7.8732 | -45.3139 | 2025-09-27 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 480c12b4-3b9a-3544-a293-ebf3415fe795 | -14.0188 | -56.1131 | 2025-09-27 13:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 43f42253-df29-3500-a441-5c95ea607912 | -5.9472 | -42.7118 | 2025-09-27 13:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| a248d67c-46c0-3397-86b6-0715cdaaec5a | -7.1383 | -45.5174 | 2025-09-27 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 17315ef2-dd89-3abe-9938-3fff301da9b0 | -8.6631 | -43.991 | 2025-09-27 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 0daba198-6905-3b6c-bf53-0b4253f0e8be | -11.4221 | -45.0025 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6e23f858-c3e0-3967-aff2-11497baa241c | -9.3517 | -47.5801 | 2025-09-27 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 09d7b6ab-c89c-324c-94fb-c476f278d99c | -7.3659 | -47.0394 | 2025-09-27 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f90e0b51-4be6-3aa9-8ce6-79a68039ac17 | -11.3451 | -45.0366 | 2025-09-27 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 284.7 |
| db7b0338-a765-372a-985e-e0a461f3e5d4 | -9.6159 | -47.5741 | 2025-09-27 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 9ef06312-632f-34cb-9cc2-b1740c1ef7af | -8.1363 | -42.3801 | 2025-09-27 13:30:00 | GOES-19 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 3a99fc26-5860-3798-a93e-bf70dda0ddd7 | -12.0369 | -47.0543 | 2025-09-27 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ad08a927-89f8-3284-9a0f-91b145d2384c | -6.6986 | -42.741 | 2025-09-27 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| ad7785f0-9dbf-33cc-899b-f2a86a3eb385 | -11.4425 | -44.9303 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 85c06bd1-4ee9-361f-89da-f512e89b495c | -7.8637 | -44.5382 | 2025-09-27 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |


[Clique aqui para ver as próximas entradas](README65.md)
