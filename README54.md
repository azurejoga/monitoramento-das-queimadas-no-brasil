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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c1e8245-7829-3dbc-9dc6-389066041af1 | -7.45721 | -45.28984 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f526cf75-164b-32e5-9d4e-c23e5fe68696 | -7.9208 | -44.86734 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 683e12cd-d217-310e-b1fd-ea62b6c33467 | -7.26583 | -44.90274 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b16a5728-a83c-3c77-b091-9ba8a3d1da07 | -6.17005 | -41.08043 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ffa1bcbb-47d0-3954-9db8-a7a1d8a102f0 | -6.4089 | -44.50605 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb220bb1-45b7-35fd-a017-f95d324e1eb5 | -8.47965 | -47.28891 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0feaebee-8d18-38a5-8004-2802e950e074 | -5.28315 | -43.74894 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c99bfc04-03e5-31ab-84ed-74ca7c980aab | -5.81304 | -45.68074 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70284f20-099d-35a2-8ffa-4762a582e5dd | -5.90677 | -45.74993 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e343e517-a187-3186-999a-51171fdd217c | -8.85908 | -47.27097 | 2025-09-11 04:21:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 991e354c-53fa-304b-b6e2-6a05a29d4bfb | -6.30952 | -44.57866 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3cfa93c0-adf5-3bc2-9395-80b7f7bd51cc | -7.48056 | -47.05726 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 744fdb96-d4d6-30b6-af04-e30656d958be | -7.65195 | -49.50063 | 2025-09-11 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ae5a359-5ea6-3771-a560-3e7ee0dc1f17 | -4.7109 | -47.23487 | 2025-09-11 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eba18db-90d8-36cb-b0fb-493c8b6e3c53 | -7.11554 | -50.76506 | 2025-09-11 04:21:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1021866b-69bd-3d34-967d-c84b4d157881 | -7.26705 | -39.38421 | 2025-09-11 04:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 490a5b8d-216f-3b48-bb94-6501fe4bf4b1 | -5.6033 | -45.78701 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bbb186f-e6c2-3346-849e-7be0be7337ba | -2.07319 | -47.14454 | 2025-09-11 04:21:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 32a60323-95e6-34b8-b854-68eef6c70816 | -6.2074 | -43.52015 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a77f7ecd-e485-3c24-a749-bdad63116cff | -8.4371 | -47.26611 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21bfda69-f19a-3adb-b6ca-27f35cd934f1 | -6.36932 | -45.16584 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 4a923ccd-7576-3670-9c89-be0293a83aad | -5.5435 | -43.04874 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c5b43e28-4a1a-3acd-9abe-7b86d9dfef6a | -8.01836 | -44.49969 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 702d1c4d-6d33-38f0-bab0-adb38a85e162 | -6.34803 | -43.03673 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc0dc5a7-0c0a-3d54-877c-686409afd91a | -5.94154 | -45.95023 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e03e663-f94c-3619-9b7d-a34ee2668b14 | -6.20234 | -45.61103 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32ce9d31-a1f2-3e88-a15d-8efa259895cf | -7.38732 | -50.88823 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84ee966c-a0a5-3df0-991c-1ae9b07ac48d | -7.29544 | -45.18209 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f421a657-254e-33c4-9354-e07fd804e686 | -5.43154 | -45.87814 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2e9a8f9-30ee-35c6-89e5-dab7e599ca33 | -5.73351 | -45.60639 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80ec80fe-79b1-374c-b715-67173e541f34 | -7.78527 | -50.76878 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 46d2f25c-acae-3573-9ca6-744999ba0ee1 | -5.72598 | -45.41644 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40f66e47-6ab1-37d6-83a6-7441830c49f3 | -7.27036 | -44.61468 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 534d5f35-3b0a-35ba-abb4-90daef4b3daf | -5.248 | -45.97623 | 2025-09-11 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ebc8f0c-2aee-333f-a80a-e7523dd910af | -7.49944 | -48.25703 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5a7bc34-6810-3233-bfe4-411b4d670cd3 | -8.56382 | -45.59169 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1defc12-34f9-3850-843b-cb2baabfbf95 | -7.47774 | -45.28955 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c39fdd4-dde5-3487-aa0f-d3446a4ddbce | -5.65112 | -42.62389 | 2025-09-11 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dfa93867-1dfb-320c-a866-9a0094c33042 | -5.93782 | -45.68531 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cb4af79-2be0-38dc-91d8-1de4bf9cf74d | -5.82663 | -45.27351 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1ea0ffb-e699-3b5b-a30e-461e8ff9db9c | -8.44098 | -49.11484 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23652f79-1321-3c55-a666-bd0464101fcb | -7.47496 | -45.28552 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4689d043-9268-39a6-9b27-3f3eaaadbd52 | -6.40666 | -44.49864 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdff73eb-d45e-3453-9510-9c2c6473cd1e | -7.65841 | -50.27082 | 2025-09-11 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f3556695-31f1-3cd5-9168-15b8769cd007 | -6.55262 | -43.96077 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84d6f025-1d04-3c7f-b2ee-e6118c0bf5eb | -6.67564 | -44.11965 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a668018d-da8a-313c-a07d-e908ab2f36db | -7.55226 | -48.20717 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ce4c809-673e-343f-a110-3f821924ded7 | -6.66787 | -44.12563 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2887ae5b-1a0e-395d-a0ac-041fd63d02f6 | -6.4954 | -44.49109 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd62fbb6-ec7d-3ebe-9c86-f948dccdb9a8 | -8.52043 | -45.69257 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5026de36-5886-3ff5-91fc-a4f7ae4c3e12 | -8.03807 | -48.67679 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 419f5bfc-1885-3d7b-8411-1f569e421627 | -7.78882 | -50.77355 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3303466c-9145-32f8-91c9-6fb839d2ad8e | -5.40699 | -45.92254 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d163ae69-5f7e-3835-9d25-20e6c6cb88e7 | -4.33008 | -47.94464 | 2025-09-11 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d4ceef3-29a1-3916-a5ae-83b1d14e3f06 | -4.47983 | -48.11448 | 2025-09-11 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e15f1be7-eaa3-3248-ad82-4889ed66c1da | -7.46053 | -45.29037 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b71fd34-beba-3fb5-8b43-58074af041d7 | -6.6531 | -51.99102 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2cea905-8ed0-304f-9c8e-24b29c3945b1 | -8.04181 | -48.67734 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beece5a1-ebe5-337e-a3e7-e0c98d5db9af | -7.22318 | -43.98294 | 2025-09-11 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f3a4eb8-beb7-36ce-86d0-28880de588ed | -7.26038 | -44.6131 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f2cebad-a512-395a-b58b-3ec2682d0c62 | -6.26258 | -42.4189 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 739f7b92-ac78-376d-b5b5-755d6800b84f | -12.01299 | -47.58319 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5ca03c4c-3d3e-349b-a91c-41a53d1d1542 | -11.15102 | -45.29072 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 253fcd00-d08c-35f8-9df1-c70815d11b57 | -12.94377 | -54.8162 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8c8ad15-b626-34e6-b522-bdf803fa94f7 | -11.3231 | -47.378 | 2025-09-11 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf3e6cf0-3737-3c9e-ac11-d0dead9a3d8e | -9.70299 | -46.88002 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9b13c5e-31b6-3842-a1a8-264298ceef76 | -11.64697 | -46.9145 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08898199-c890-3fd9-9961-85b70b6c5e7c | -9.70079 | -46.87215 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fef16e5-6024-39d6-83c7-74c6716a9898 | -10.06455 | -50.38052 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07844412-8d4a-36aa-9cda-c80c460d9db7 | -14.91556 | -47.30244 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8531b1ac-4a03-3008-b328-79a211b74281 | -12.14311 | -44.84811 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 013b42b1-6bfc-379e-8218-7b7f7ef70f92 | -11.1538 | -45.29478 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c83e4f02-3e2b-3c22-8b5b-aed2ade591b0 | -11.48788 | -43.65534 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d60bc011-23ca-3621-aaa5-bd89b5abbe56 | -9.72014 | -43.52929 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de511272-29db-3075-90da-575e2c7bf9f4 | -10.65575 | -48.63043 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ceef17c9-c3e0-3670-9699-15dfef61d5aa | -9.11532 | -46.97061 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80a329de-f4c1-3340-90b5-6301d04cf296 | -10.37856 | -48.83676 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 592c7e2c-9d56-3e31-a61d-5c584bf331df | -9.88434 | -51.87701 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef337f34-9d9e-306a-b7e8-75215408dbe6 | -12.95528 | -46.7328 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e49e1cc-65c9-320c-ae56-bdd3c28dda0b | -11.80924 | -46.74966 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83cc56f4-d135-3a54-b007-04fe0aae2d3e | -11.72801 | -50.65589 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 937a0070-3fe1-3251-87e2-503cd4838c4a | -8.08087 | -54.7437 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17f9bbb0-892b-3cd3-ab14-f9b6ff99efd5 | -11.2158 | -54.99809 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41aa2787-3872-302b-ae07-85fae4d22ed1 | -11.15047 | -45.29424 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6426d831-d400-3ea1-ad03-e587a6ed41f0 | -12.72854 | -45.08004 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a749bd2-5d29-341b-9dc9-88b04b4d78bf | -11.02144 | -45.06331 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ac7bff64-e84f-364b-b5d2-8c969a1d5608 | -10.2021 | -46.83804 | 2025-09-11 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a11bea71-aa8d-3c3f-8c9d-17fe349cb0d1 | -13.13601 | -54.922 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26d1489f-19f6-36a7-bdb0-f8affadb11e0 | -10.56355 | -43.66725 | 2025-09-11 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a8b2218-d041-33ad-9986-09033851a7f6 | -14.56973 | -48.76865 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e109239-d022-38a4-a6e9-0f8524cbfe5c | -15.22637 | -44.04881 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e0f9d0f-93c7-3988-8f9e-b96437258cf3 | -11.40307 | -45.6024 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c9107f04-3c54-38e7-b4b8-9699af10e999 | -13.26508 | -43.74727 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 332870f6-a92b-3e81-9fcc-d927ee961427 | -11.49017 | -43.63993 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5677fe84-f350-3660-95b1-3b0dc1e04eb7 | -9.0264 | -49.7645 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 47251abc-d4ca-3993-b37c-ecb78d475b68 | -11.36179 | -46.54052 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76c69eb9-306a-3179-b18d-0ef350c8bbe2 | -11.15603 | -45.30238 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49a3cde3-7374-3dcc-b92d-65da072af86a | -12.05365 | -50.9411 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ca5e19d-49f8-3336-8a99-b6cd2efc7adb | -11.15157 | -45.2872 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc9d7b60-9b21-3178-a789-5bab01ac4ee0 | -11.15548 | -45.30591 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README55.md)
