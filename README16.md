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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfc69f77-0104-3063-ae17-5a4ca51916b3 | -14.0982 | -44.8195 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3176b6e0-0a88-3b37-96ac-3f1aecdcfbc1 | -6.6637 | -50.891602 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53401e71-9179-39ec-ac32-0d4a1ff7c386 | -8.4119 | -54.7318 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2de86ad-e807-3c61-8af6-d5bb09b40b66 | -5.8602 | -51.9398 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0876a0be-c827-3251-b042-bd7340dcbbf8 | -10.824 | -50.1674 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3379bdea-3c84-3d66-a68b-762a94d01acd | -10.9149 | -53.970699 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fad3e13-b607-3b2d-beee-e70d76fd595a | -14.6753 | -46.674599 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2560af2b-20b9-3cad-8ac6-5c2af9cc92db | -11.8166 | -46.855499 | 2026-09-19 00:41:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74331621-8c28-3d0a-8c69-4a7680975037 | -13.6427 | -46.9417 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 443b5300-bfe1-34b5-ac66-30926fe91287 | -16.8076 | -46.983101 | 2026-09-19 00:41:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 278c93ef-7e8e-3365-9514-aff77cc8ea7c | -7.3663 | -44.633202 | 2026-09-19 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40dfbe0e-2f64-3f05-ab80-817bb27a08d7 | -8.7618 | -46.9063 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5a442e-b3ae-345c-b528-394c26ea054a | -3.325 | -59.8139 | 2026-09-19 00:41:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1c4460-818c-3a69-bf5e-a1e8f35c67b9 | -8.4848 | -57.636398 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96dbc572-48c9-3c6f-8467-9284c451a2a9 | -12.1596 | -47.0 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9990661-f5f3-3b7c-830d-08b2a659d127 | -13.2274 | -50.210201 | 2026-09-19 00:41:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a71dc652-1972-3f27-abc1-9993f9fd6ab6 | -6.3474 | -51.727299 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88b2697-3edd-33ef-bbee-7a9f4dc9abf6 | -1.1916 | -54.224098 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8af8b59-584d-3501-b6e7-7c04fd1ff7ee | 1.2286 | -51.004299 | 2026-09-19 00:41:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf1c73c-1316-3878-be69-be6d9c84974c | -13.0097 | -46.971802 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05f26c09-f3a3-3520-853d-c17d149a99d7 | -11.9384 | -50.139999 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f315be4-58f4-36ba-b58c-5ca6f9da8ef0 | -11.3694 | -44.093899 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95710aa8-3c33-3cab-9cfa-8b292519c44f | -13.0032 | -46.943401 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc1e7774-21f0-3fdd-93e6-d07609cefe67 | -10.4498 | -48.680599 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7efbd46-66fb-375d-ba99-f9b82f44fae0 | -14.863 | -47.137199 | 2026-09-19 00:41:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f6c0f515-fd07-3050-8fee-be3403ebbb5c | -8.9977 | -44.976299 | 2026-09-19 00:41:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4c2071d-9ac4-30b6-b410-bef7423d4c59 | -4.4877 | -55.4958 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff3cd30-2213-304b-ba0f-8e8b973c2eb7 | -6.3193 | -45.610699 | 2026-09-19 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9131ff1c-1903-3e8b-9cae-a510e1210979 | -6.3155 | -47.572102 | 2026-09-19 00:41:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30d34b2c-52f9-3ee8-8e34-bfde216b7f70 | -4.36 | -47.772499 | 2026-09-19 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96e523e1-f0d1-3d8e-8a78-e6fe755547b3 | -3.3599 | -50.458099 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9082aa87-3f76-3639-8a2b-dc45369de56c | -12.1417 | -47.0117 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 882e4724-6570-3e85-8f6d-bae56b407c7d | -11.0659 | -49.773998 | 2026-09-19 00:41:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2385a0b6-ea81-36b9-adf6-386108184587 | -5.7486 | -57.424 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c547aa38-b3fc-3575-be15-6717f8894bd6 | -3.747 | -44.374901 | 2026-09-19 00:41:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72631aa9-a289-3156-9193-a5569ef38c18 | -12.3329 | -50.724499 | 2026-09-19 00:41:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45ebd6aa-7141-3f6f-ad04-9f944a4da58b | -10.3648 | -48.897099 | 2026-09-19 00:41:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8333e4b7-0ea5-32fe-84ef-b584e9075aa0 | -9.9645 | -46.617199 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8216f5b7-9793-32c7-b772-8bde5903f7d3 | -14.1395 | -45.168499 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5cf943e-282e-3d78-b875-019adb451364 | -13.0147 | -46.9482 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 771ef0d8-adbc-3e37-8b96-51458223653c | -5.762 | -57.438599 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc464d8-69dd-3b7b-8c1f-e18e7443d258 | -4.3497 | -55.427799 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cff367f-e4e6-3109-88e1-ce23210e289b | -9.5548 | -46.5881 | 2026-09-19 00:41:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 838eb5cd-c167-3032-bf6c-8b11402f6f85 | -9.0374 | -48.726002 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a797ad62-7591-3079-9240-14b75f9515b4 | -7.7603 | -46.730202 | 2026-09-19 00:41:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d54f4b3f-20d9-34eb-85fa-9ff86562489d | -4.445 | -44.364899 | 2026-09-19 00:41:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dad6f6c-2e35-3b49-a09f-956134ce9390 | -10.8353 | -50.919601 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de087d4e-5f35-31da-a78a-354886e981af | -13.6021 | -48.312698 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29cdc183-a19a-3150-b4e7-a1afe805767b | -5.877 | -46.711498 | 2026-09-19 00:41:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bff15e2-ce3e-3751-b3cd-5c4cb734a9bc | -19.5506 | -47.6208 | 2026-09-19 00:41:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4c9dee-0642-348b-8b89-a04af96f7687 | -3.2292 | -46.948399 | 2026-09-19 00:41:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23c8bff0-8241-3f74-9bd4-7cba303b78ff | -8.7754 | -48.662399 | 2026-09-19 00:41:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bbb0e00a-0406-3865-b042-9d5b6f0e070c | -5.811 | -49.859001 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff5aea5-ea80-34ba-a3fe-efa60905e839 | -5.8633 | -52.045399 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9af224d-7825-3465-b547-e2421baccb88 | -10.1772 | -48.5243 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0688110f-480e-3f9f-a42a-12a267580848 | -11.0107 | -54.136299 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1423818-0ef7-30de-912b-c75a734308a1 | -5.2538 | -48.199799 | 2026-09-19 00:41:00 | METOP-C | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c2984a5a-74f5-311a-a847-7e3a387a283e | -7.6974 | -46.111599 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa6e198d-0870-30ea-a7a4-4422c1280bd8 | -8.475 | -44.5201 | 2026-09-19 00:41:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37799074-4118-3d04-8413-0b5900559ac2 | -10.9762 | -49.7407 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df28ad07-1a64-3d22-b53e-d7d5ba7071e6 | -8.6641 | -45.4398 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 39343394-8788-359d-8496-ea5c1190225a | -8.7636 | -46.9137 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 284ffcde-3020-3003-a8ff-6e1f4669dfb5 | -11.8264 | -46.853199 | 2026-09-19 00:41:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8c9ab93-db6f-3cb9-a9c3-d64ea7907bc3 | -9.9377 | -53.9837 | 2026-09-19 00:41:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4885bc2d-ca3b-316f-8dc4-e104dd05c1e6 | -5.8799 | -53.5466 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 747dfd23-e27f-3958-8167-ad0652c33c63 | -3.7312 | -54.6343 | 2026-09-19 00:41:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3c43c2-11f3-31f6-915b-1d4d40649bed | -5.8778 | -53.537201 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c18922b0-c9df-3d81-a1fd-922b359ae2bb | -6.2024 | -45.335499 | 2026-09-19 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 667a1a95-b65f-34a9-a837-f65398eca498 | -6.9835 | -42.166698 | 2026-09-19 00:41:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cec2b57d-6c44-3a65-8d9d-1291c29e6952 | -18.827801 | -47.939301 | 2026-09-19 00:41:00 | METOP-C | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4e3f356-e387-32d6-bc98-e2edb8bae038 | -1.2164 | -55.726101 | 2026-09-19 00:41:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9039dc94-aca3-3882-9d43-ce0e563fdd9f | -11.1374 | -54.010201 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 679cef83-3f61-3574-871b-cd81af777f61 | -4.2799 | -48.584 | 2026-09-19 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b96d877-3d76-31a9-9998-d3eeec4e162a | -13.8821 | -48.599899 | 2026-09-19 00:41:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3fd58014-410b-3591-8f99-6d10713c5b12 | -2.7393 | -49.463799 | 2026-09-19 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09ad3913-a66f-3ee8-86be-d2b9a63373e0 | -11.3335 | -43.3941 | 2026-09-19 00:41:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72a1e20c-27d4-3f65-9891-f9950259e7f0 | -4.5541 | -42.972198 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5547cd8-b682-3326-b962-f67764dd5a4f | -12.1466 | -46.988098 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35d7a97f-c90b-3b60-807a-9caf5b0b4a92 | -12.4165 | -45.052601 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93ef7356-d80d-3d7d-b72d-95e84c2d8daa | -1.2058 | -49.121498 | 2026-09-19 00:41:00 | METOP-C | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec5a396-a8d0-3962-aa33-fabd9f30f493 | -8.7734 | -46.911499 | 2026-09-19 00:41:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6b07888-029b-3a7e-b229-da5f63135864 | -8.3721 | -47.227699 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba1986fa-3859-3c64-b58b-1cc7904b3963 | -18.8262 | -47.931801 | 2026-09-19 00:41:00 | METOP-C | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba93da5e-f41b-32a8-bff9-65b90b876ad4 | -12.982 | -46.985699 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e89ad7f-6d36-3d64-9941-bb0c43ba5d08 | -14.1691 | -47.033401 | 2026-09-19 00:41:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5ccd9ccb-fb45-3f8c-97da-c9eb45956219 | -9.9264 | -46.587101 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52f5d282-f61b-3a3a-ab64-3280ee381b1f | -7.6428 | -46.0989 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5376839f-ffa0-35e6-927b-6fc3260d7715 | -11.3222 | -47.352299 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fd3f810-d27b-3ab2-8fed-c3cd4291c80a | -6.5713 | -44.159401 | 2026-09-19 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d9fcf3a-f743-3ef8-96a2-f409aba0d374 | -10.9957 | -48.315201 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab292ae0-a9f0-3501-b500-16eb14328e91 | -12.5943 | -49.103802 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 143614ad-b8e3-3ecf-b0d3-030b173e8070 | -14.6623 | -46.662701 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3084e232-9c51-3417-8e6b-83dfe7dc4165 | -8.3657 | -47.244499 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8c66ba5-d2ec-374e-94d4-90dd33346fa2 | -10.915 | -48.413898 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44363a3c-a44a-3e97-99db-cb5a6b609b0b | -8.3623 | -47.23 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df1145da-3cbe-31b1-aedc-46d557b58eda | -11.1206 | -45.2981 | 2026-09-19 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1692dc1-116b-32ff-8255-9839e5368f84 | -6.6654 | -50.8988 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903d59aa-fc12-328a-8f36-6d3525b7de52 | -5.8995 | -53.542301 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae2553f1-ec13-39d2-ba1a-f96678971059 | -12.1237 | -46.9785 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99379a5d-4493-310b-a8df-0b779f968649 | -13.6865 | -48.599602 | 2026-09-19 00:41:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
