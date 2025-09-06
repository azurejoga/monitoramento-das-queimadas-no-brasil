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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5487123c-f49f-324c-b246-92c1a8e7d440 | -15.539 | -53.625099 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b22fc1e-bb72-377e-af66-87df0e5b483b | -14.9948 | -52.4053 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6c894bb-b72b-314a-934a-d287b38c977f | -9.3767 | -40.6283 | 2025-09-06 00:15:00 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 91265c3b-656c-3b95-9ac1-5b2586c953a7 | -5.4238 | -45.0383 | 2025-09-06 00:15:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31ef9de6-121c-3961-bf27-6b58f365c1f0 | -12.802 | -54.839901 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15a9a4e0-af60-3896-9070-93f5d1eaa3a1 | -4.7989 | -45.140202 | 2025-09-06 00:15:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94691446-6944-31b0-9d02-4cfb0cf87d75 | -5.9952 | -53.283401 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceaaa044-f6a4-3aab-9e6b-900e1a0a3abd | -9.5113 | -49.027901 | 2025-09-06 00:15:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46a518a9-c29e-372c-9eda-c433dbd7e8ce | -11.9133 | -43.394402 | 2025-09-06 00:15:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4839fff2-ef76-334d-a361-004c82966081 | -6.0767 | -53.469501 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8fb772-8bdc-3e71-9ba0-14f660a0dd69 | -8.3236 | -51.388599 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1611ecaf-8d44-3d92-a3b9-9d22269d9a14 | -5.4968 | -53.773899 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a83453d2-92ee-30bd-9df7-852a5093c14b | -14.3779 | -48.041199 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e0ee85c3-c0b6-30d6-bf2a-e11fee45ae3f | -20.042299 | -40.295601 | 2025-09-06 00:15:00 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae10f7a1-f779-38fe-92ed-b944a793d429 | -7.6332 | -46.251598 | 2025-09-06 00:15:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94b8d17c-7150-3ce6-93a5-d92cba321179 | -1.9318 | -48.0396 | 2025-09-06 00:15:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7648ae93-8012-34cf-96fa-a9d0f187ee3c | -22.024099 | -45.9184 | 2025-09-06 00:15:00 | METOP-B | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 632f1c72-32c0-3074-afc8-189392de4336 | -9.8964 | -48.125099 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4861a21-dbf0-3384-b230-a352097af68c | -8.1523 | -52.540501 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcd6465e-05e7-3f9e-8aa9-406189bf2ab9 | -7.87 | -52.373199 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2b699d5-17dd-3c98-9cf5-6c068c0660b2 | -7.8741 | -50.230801 | 2025-09-06 00:15:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e19e149c-7c96-3d54-add7-71ed838e3c6a | -5.8484 | -51.723499 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5011184c-07ef-3996-983e-19344deb2bf1 | -9.7869 | -51.652302 | 2025-09-06 00:15:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bae2b4a4-dd47-3eff-86ef-28ad868c84a2 | -2.9658 | -49.513599 | 2025-09-06 00:15:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3a9a51d-91c3-363a-8a4d-64ff5842df0e | -15.5366 | -53.612598 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca13da64-9425-3810-af3d-00c6f8b9ed19 | -9.7725 | -51.680698 | 2025-09-06 00:15:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a741a69-f7fe-386b-bd09-bfda03fc2107 | -8.3203 | -51.373402 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81083d01-20b4-3b38-8e8f-a9ca5236eddf | -6.0958 | -44.609299 | 2025-09-06 00:15:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc15191-ba52-3fac-98d0-e641d097a46f | -5.3826 | -51.942402 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2e1291d-5b69-3902-8987-70261faf9506 | -8.88 | -47.053398 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc564735-fa10-3340-bcbd-6b8badbe3dc5 | -22.061701 | -48.784698 | 2025-09-06 00:15:00 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e1477acb-0c66-3b25-88df-e4152b5a48c1 | -20.722601 | -44.054501 | 2025-09-06 00:15:00 | METOP-B | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c036b1e6-40e0-30aa-b32b-d9259ea3fd69 | -14.8787 | -49.601799 | 2025-09-06 00:15:00 | METOP-B | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed5b8ac-261f-3455-a0ec-ea6b3096b9e9 | -10.1051 | -46.459099 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2432544d-2cc4-3130-bcae-905ad7e9a5ba | -12.762 | -54.791401 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd94d9d2-44bb-38dc-9c00-491ed88e611f | -9.5758 | -46.939602 | 2025-09-06 00:15:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cdae7e6-33dd-3f62-9e22-012b4ac3c9ce | -3.2769 | -48.975201 | 2025-09-06 00:15:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb60f24-6537-35c9-83c1-3bb524dcf038 | -22.629999 | -45.721901 | 2025-09-06 00:15:00 | METOP-B | GONÇALVES | MINAS GERAIS | Brasil | 3127404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e96ebf80-735a-3f81-9707-6ab4ab204c5f | -11.5507 | -47.783699 | 2025-09-06 00:15:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a341562-2dfa-3bca-9e79-ba2aa9569540 | -15.3473 | -48.4319 | 2025-09-06 00:15:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a573b5a9-fc56-3bfb-b020-58dcea4be90b | -7.4342 | -46.595001 | 2025-09-06 00:15:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5ee0b8c-38db-3b01-a61d-aa0ba24e2fdb | -14.8749 | -48.150101 | 2025-09-06 00:15:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca40b3e3-36a0-35e4-82c8-545bc1a99651 | -4.0735 | -48.215801 | 2025-09-06 00:15:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29d981eb-1a2f-34ed-b2f0-46e50833dc85 | -10.8046 | -45.9585 | 2025-09-06 00:15:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9c0f51f-d082-31d3-a758-3cd120586f98 | -3.7507 | -49.3391 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b16681-5286-3109-85a4-ed69d56d7640 | -3.0474 | -50.838299 | 2025-09-06 00:15:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb46a65-fdc1-3ec8-bf60-9fcaa7c4eeb8 | -12.8118 | -54.837898 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bec96fb6-36af-3bc9-8ce6-f82c48036ef2 | -7.6313 | -46.243401 | 2025-09-06 00:15:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c567ff0-af81-3486-b9d1-aa64c0bd4edb | -8.8801 | -50.455299 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98afc230-8fbe-3c56-a358-d9d88c23b5fe | -14.061 | -52.224201 | 2025-09-06 00:15:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 27396bd0-fa07-3c55-98b4-2f4430b7c47b | -11.2822 | -55.568901 | 2025-09-06 00:15:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b289c74f-f59c-38b1-875b-0fec29d78b22 | -5.6653 | -52.1991 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5085cefe-40b3-3bb7-b40d-fb5c0566267c | -7.2145 | -44.9851 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f3d24de-8dbc-3013-8a50-c3c21ea74388 | -6.0865 | -53.4674 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce91f94c-12e8-32cf-8408-c5aa8bbee384 | -8.8147 | -49.8316 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f208ce-5214-370b-a96c-c6a22c8e1fc1 | -14.6476 | -48.239399 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6eea00-8ae6-385a-b993-05f8b8ea6ded | -18.062401 | -43.0755 | 2025-09-06 00:15:00 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a99698f-11a5-311b-9204-125a68e87211 | -15.4258 | -42.445099 | 2025-09-06 00:15:00 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a24661c8-ecdb-3cf4-b86a-9c8a64d8432b | -13.3978 | -43.1651 | 2025-09-06 00:15:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ff483bb1-ce5e-38ff-baa5-75d16532bfbc | -9.4905 | -51.0867 | 2025-09-06 00:15:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa8a93b-1521-3f55-bc8c-3001726b7ec6 | -5.7615 | -44.764801 | 2025-09-06 00:15:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2edf0cb-60ec-32e8-b946-9e25f3e497e2 | -2.9641 | -48.6399 | 2025-09-06 00:15:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e99242e-93da-39c4-9960-703bd224bad5 | -5.9933 | -53.2747 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2985eb14-941c-3518-a47e-282f81464373 | -2.9544 | -49.508801 | 2025-09-06 00:15:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dec3a89c-4ed0-3175-8321-6504d87ddfa4 | -7.1873 | -50.940399 | 2025-09-06 00:15:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0b634d-9184-32b4-9392-a0e69b3e1e01 | -9.4758 | -51.113701 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bad0147e-069f-34fb-b37e-814c4187e095 | -6.3889 | -44.5849 | 2025-09-06 00:15:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b18cfac9-e716-32f8-b8ce-0c14e9a08f8d | -13.5378 | -46.950298 | 2025-09-06 00:15:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7de88abe-2444-30cd-893b-6f68145fd483 | -17.555901 | -42.5625 | 2025-09-06 00:15:00 | METOP-B | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 648cd487-1263-3bb7-9e12-102b71b03c01 | -11.4129 | -52.217701 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be2356d2-36ef-3b23-982c-d4ebe15c51ac | -18.520201 | -48.237598 | 2025-09-06 00:15:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c20dfc2-a398-3895-85cf-8cbc7eabdf7d | -13.3636 | -48.1553 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5b94047-2a21-3093-8f1b-f1e128de0d2b | -8.1662 | -48.312302 | 2025-09-06 00:15:00 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66c8b321-27f1-3be7-b281-7423d507a460 | -6.5847 | -52.8335 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 697998a6-cac6-3e55-9057-8f82880cd857 | -10.0394 | -48.348801 | 2025-09-06 00:15:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8865c6e2-1e9c-38f2-a8d9-001973ed1e50 | -5.9633 | -53.702599 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92ad22c4-973f-38e2-9df3-39dd442c49c2 | -5.7542 | -44.7775 | 2025-09-06 00:15:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2533e695-bad2-3f36-ad77-3cc1e991c1f1 | -7.8656 | -52.400101 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60ca1e58-b9b9-3390-8f99-462292d86118 | -5.722 | -46.412498 | 2025-09-06 00:15:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5c38399-5c13-30b8-946c-a9991978e61d | -4.2929 | -42.937401 | 2025-09-06 00:15:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5d78f65-c431-385a-9e8c-3e51fc948335 | -11.2793 | -55.554401 | 2025-09-06 00:15:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb9b49d8-26bc-3404-8326-b9071ca0025b | -8.1466 | -48.316799 | 2025-09-06 00:15:00 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed6d684-7af3-3a20-b698-14516bb544d4 | -13.6838 | -48.067299 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5a30b91e-e0f2-3eba-bb0a-6ca85cc6bb57 | -8.317 | -51.358299 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 174df026-49a3-3297-82af-6cd25e3cbec0 | -18.8606 | -41.209301 | 2025-09-06 00:15:00 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c21d95d1-4261-3073-bf4d-73608cb439b7 | -11.3509 | -47.354099 | 2025-09-06 00:15:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6268a52b-790e-3645-a8b8-34d016f338e5 | -2.9624 | -48.632702 | 2025-09-06 00:15:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87799214-a0dc-3c36-8798-62d3e6501fae | -7.2243 | -44.9828 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d84fc581-dadf-3493-97f3-24d6a07a064d | -2.5858 | -49.655998 | 2025-09-06 00:15:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54b5ae33-584d-3fee-ba1e-24f8107a356c | -12.3137 | -53.868301 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4a75ec-41a8-35a6-a94b-bff430e5b97d | -5.754 | -53.824902 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfbf8a73-61d3-318c-a58c-9b71993612da | -11.3395 | -47.3493 | 2025-09-06 00:15:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4fa7358-0827-39f5-8158-a1ddb50de84a | -5.1071 | -44.9608 | 2025-09-06 00:15:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd336bf3-d6f2-3f05-ba33-581a9f238d09 | -12.2965 | -53.883801 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b163298-24dd-3911-b36a-0b94bae6f8c5 | -6.1237 | -44.992001 | 2025-09-06 00:15:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 005f4939-3257-3e91-96b9-62b2ca96361f | -2.5842 | -49.649101 | 2025-09-06 00:15:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92fac1e7-6dbe-3ca6-bb0d-4437bc725162 | -5.7752 | -43.641602 | 2025-09-06 00:15:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30dc28e2-45f0-3a53-bbb9-10faa325f114 | -18.521799 | -48.244999 | 2025-09-06 00:15:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23b44d07-260f-3926-91ff-8340ddce9d29 | -11.4073 | -52.1908 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d722302-eac7-33f2-ae1b-b4e91ee45f3e | -23.955999 | -49.573502 | 2025-09-06 00:15:00 | METOP-B | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
