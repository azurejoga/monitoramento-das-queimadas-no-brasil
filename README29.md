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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5156800d-4908-3654-a584-89301cec1e29 | -3.322 | -50.08098 | 2025-09-12 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff69c096-b89b-3468-ab4e-018d9719ff67 | -2.43769 | -47.33171 | 2025-09-12 04:02:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 246344f8-0968-3655-bdd9-9b918c36ac62 | -3.67961 | -47.48801 | 2025-09-12 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 466d3cca-2e1e-3f2b-b860-4cf8c297a333 | -2.74259 | -48.70024 | 2025-09-12 04:02:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91fc805c-b1fa-3bbf-85db-127814219e6b | -3.11679 | -43.27377 | 2025-09-12 04:02:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63b0da6b-5845-315e-8114-6e5660281225 | -4.47254 | -38.72158 | 2025-09-12 04:02:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d168134c-f665-33ff-89de-5d572891083d | -4.72692 | -40.32056 | 2025-09-12 04:02:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 449f890c-c8b6-397c-b308-926e9dc284bf | -9.02987 | -47.10963 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d158fe48-a4e4-346b-9331-f5eda2b3fa64 | -6.15715 | -47.27335 | 2025-09-12 04:04:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 50df7960-b0db-3d7c-ae19-9b888e195419 | -10.7476 | -48.18615 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61c0034f-6eea-3257-9ced-15b39cfc2090 | -8.1744 | -46.12265 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a4b18d2-2251-3504-b4b3-9402974dd28f | -11.68051 | -46.5833 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1adf94e4-726b-32fe-afdf-630118cba708 | -11.67103 | -46.57871 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f99082e3-4e59-385b-b00b-356625247c38 | -7.85026 | -44.80622 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f45b499b-0730-3191-9408-12154c37645b | -6.55342 | -43.95876 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3da6f674-654e-323d-a42b-360c37df4f8c | -9.00466 | -46.11815 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 969aa542-57d3-3b14-adb5-aabb5637ae79 | -9.02447 | -45.75784 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 106d49d2-9d42-3d31-bb57-a5146547c134 | -6.21404 | -42.57231 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e996fb08-b15a-36e4-972a-7550b2fa0bf8 | -9.06385 | -46.57911 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44a358e3-c790-3f92-b7c0-7673455abd88 | -6.45039 | -44.06897 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 086f0679-b5d0-3143-a1bd-ef36fd19a828 | -12.11066 | -44.87019 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e9aff55-6f6e-3150-be12-ea5fc48f61e8 | -8.17677 | -46.08284 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c720ad6b-d67b-30c7-afc3-48270bc40136 | -11.41958 | -43.53794 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e32eac-f9ca-3340-8dc8-5edbb9c06ae6 | -9.74078 | -45.42147 | 2025-09-12 04:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff8004f0-a5a7-3ea1-a0cc-d28eeee18365 | -10.41069 | -50.00828 | 2025-09-12 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b4c48f8-d1fe-328d-aa2d-b16293fd535e | -7.40711 | -44.36292 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9530d055-4cbf-3168-9b15-dd2e221c4b90 | -10.13044 | -47.92179 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad82eb56-4dc8-32ad-898a-4d383c89e308 | -11.46934 | -43.60628 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a952b137-66fb-3116-99a6-745282646eb6 | -6.81689 | -52.79704 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31217124-0153-3467-b3bf-649cbcda3cac | -8.6403 | -45.72203 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf518373-3c41-36a3-afb1-cb3ed63c4ee8 | -6.27472 | -43.18212 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74307137-328b-3711-9e06-13ef98262a8e | -11.6667 | -46.61241 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0026edbf-b81c-3d83-a117-f8ad10f47c32 | -12.10163 | -44.87818 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63f68bca-0314-311b-a416-ec4027f0e0d3 | -10.58231 | -47.21603 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bba10ad8-322b-397c-8bd8-00e4b9996693 | -9.38535 | -46.77855 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25b55abd-aa7f-37e0-b897-5d7c419ec0b9 | -9.00753 | -46.12657 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab8e6f19-e773-3f5b-8460-aaa5879c303b | -11.37724 | -43.51042 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be21b30c-3cb3-319e-9a6e-b28bc8edda4b | -11.68533 | -46.58023 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 0fd01b97-e7a3-3aae-8a88-a0ac2475644f | -6.55723 | -43.9593 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 898aa5f5-b3e2-3f23-9e3f-f2c5b7062453 | -5.29488 | -48.12938 | 2025-09-12 04:04:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01a7a9aa-c476-3835-b358-f8ddd4302b20 | -11.15309 | -45.30307 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d42a8380-794e-30a9-8859-b0b01d0d07d7 | -5.94366 | -42.78827 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dce3dadb-fe8c-3a68-a19b-6f3418826d1b | -11.15087 | -45.24052 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48466e8e-8a20-34b9-9764-6cbbd6b830ed | -9.45415 | -46.41547 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99942409-cb15-3700-b9bb-7ac1655a8266 | -7.7284 | -44.8661 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c05fd33-7cf4-3ef9-b10d-8ab2fff2b095 | -6.18979 | -42.74255 | 2025-09-12 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55bdcaf7-293e-3d4f-9e68-40658ebf805d | -5.11694 | -47.5245 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3daac5f-c78d-3a0d-b417-0011ed5e116f | -8.87457 | -49.53441 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8441797f-cd7f-3950-b802-c9e47d02bc9a | -7.44302 | -44.98598 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28403b37-9be0-37d5-b72e-1310fcafb850 | -11.48075 | -43.62469 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 342040c2-9c92-3f6e-bdb3-4ba00b7f92a2 | -11.67846 | -46.61837 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52de743c-c42d-3571-9ba3-d3c785ce7f84 | -6.6854 | -44.12288 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ce9dc89-d346-3be7-b2c8-513f2f236a80 | -10.44292 | -50.60941 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 814aa940-6805-3122-8dfd-281a83973203 | -6.19954 | -42.66077 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2e445fa9-fb93-39a6-a638-c24572affad6 | -11.14024 | -45.24075 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bdc1dec6-c3f8-3fd6-a121-0a2e38f5ae29 | -11.67217 | -46.55857 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b74294d2-ba8d-30b7-baf3-27c8b697d818 | -6.36023 | -42.54179 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4a5eb60a-9449-30a3-9832-8c389d6d66cf | -10.41897 | -50.61499 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04940c68-9ba8-3fd0-a6bc-443658691f35 | -10.65118 | -48.65184 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cfd47f6b-c94e-389a-b723-d23fdef48bb0 | -9.82964 | -54.5379 | 2025-09-12 04:04:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83a5c516-2dc0-3c32-a2ef-2d7764f145b8 | -11.14923 | -45.30242 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1f941bc-7191-3c65-be81-12fb522c8189 | -9.04763 | -47.0611 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf240808-631c-3a73-888f-7d675e5d13b5 | -10.19325 | -46.1962 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05cf8c17-810e-3ded-94c8-555aa0bb0ad3 | -8.88669 | -49.93901 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f77f2fec-940a-30d4-9f02-d01f95e2ee49 | -7.30157 | -44.35523 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f68c3f8-0ae4-3b58-bde9-e78a9d4e7100 | -9.03381 | -47.08728 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f328813-60ec-3d94-865d-c256c74e8c5e | -11.48712 | -43.62993 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e37d52c7-9bfa-3c25-a460-8880a731c945 | -6.59538 | -41.45233 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 68b46eb6-7add-39aa-af3b-70f6c80d8884 | -4.93576 | -45.59781 | 2025-09-12 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05fb7efd-487a-3cb3-9a4b-334f3bb65dc1 | -11.68811 | -46.58849 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6396b23-877e-3e49-aab3-5e20cbadfec6 | -5.0756 | -41.15351 | 2025-09-12 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| edc3c0c7-4b80-33f5-a8ad-f66467a4304b | -5.11612 | -45.34972 | 2025-09-12 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e61bd6ec-169a-37eb-8781-633e8e135c5e | -11.67086 | -46.61308 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bfeaceab-5be3-3ddd-9bfa-ff55006dc29f | -8.19046 | -46.10519 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b846fd71-9ef1-34d0-be2e-2896b917fd36 | -11.68119 | -46.57952 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| befb8d67-6706-3c54-a8a4-aefdf4f5caae | -9.03703 | -47.06902 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5510a037-5ae3-3c4c-801f-a1a7a5751e5d | -8.949 | -46.7256 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2203bb0c-3b52-3eb4-a147-8c82b7c9bf64 | -8.64096 | -45.71815 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 350748cb-6a7c-370a-ae63-88eeaf4f0322 | -9.11397 | -46.95951 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 061cd867-be09-32dc-b92f-beedf74fff5b | -6.24958 | -43.43046 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd03e1aa-3325-3bd7-ba9a-3ab4ee719713 | -11.39281 | -43.52525 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 717e0368-032d-3afb-944e-698aa661bc7a | -8.64513 | -45.71848 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5eb73c1-86e8-3a3a-87a3-fba7f899778d | -7.85987 | -44.84051 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0b873d6-4341-3c00-a7a7-259b8c2321c2 | -9.67984 | -47.54782 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73832a95-db07-3960-8ae5-01dd0a30f77a | -9.07175 | -50.50003 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3a55577-f91b-3e70-b125-fd9f59abd93c | -9.85505 | -43.12797 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d84ee423-a457-385f-b993-2d9de02a7c61 | -12.11436 | -44.87086 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f2e8422-6011-3062-b89d-b4c703a6c514 | -6.1696 | -47.28617 | 2025-09-12 04:04:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 21e06877-93d9-369c-a72b-3d5ab319a0a2 | -8.73215 | -47.11785 | 2025-09-12 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e509d5e1-3c78-3812-8d5a-e6cbe97989d8 | -8.17741 | -46.12175 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8140097-7610-3059-a951-b4660a832205 | -11.4836 | -43.6293 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b791d6-cb76-3e36-b821-6ef8dece3d3a | -7.22293 | -43.97645 | 2025-09-12 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de655842-1606-3a1d-a38e-51d6a7b9f287 | -10.12364 | -47.90604 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c501e64a-875e-3d74-b9ce-8764c3abebb0 | -9.04484 | -47.05084 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29eec196-a2b1-3b77-a190-eb6d027bf7fd | -6.40459 | -42.59718 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e7647fdd-8818-356a-871d-741aa20fee96 | -6.60002 | -43.22226 | 2025-09-12 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 915f72e1-d9e0-30dc-833f-6bef39026ac8 | -12.10987 | -44.8748 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e7e8342-bb5a-3952-a3f9-aeccab3bc033 | -7.46128 | -44.92666 | 2025-09-12 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56c31541-0be7-3d0e-ac47-834eec805040 | -6.52999 | -44.60307 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57e338d2-4a6e-3626-96d5-06ffcc3be71c | -7.85419 | -44.80688 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README30.md)
