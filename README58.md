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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5760162b-a226-34ad-92cd-79f733b737d4 | -5.83721 | -52.08536 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0f0ff8-90b4-3406-8c18-b8c0f702c387 | -6.43504 | -60.00906 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb18c147-62ba-38eb-a5d9-d2c8929e57f7 | -8.25891 | -42.1793 | 2026-09-17 05:16:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8e655ab8-3a41-38e9-babe-c49ab568a0d6 | -4.81153 | -42.8902 | 2026-09-17 05:16:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 12b4b263-0ca5-3231-ba20-d31a3ae78317 | -9.61944 | -45.36913 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 507aa4ea-0015-309c-8c95-5d7063cd3fe8 | -10.11621 | -45.57317 | 2026-09-17 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33e36a43-cc2e-30b3-8fe8-0deb4136e195 | -6.90364 | -59.03885 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60a66364-7b26-3a8b-9c77-23eacbc5a103 | -6.71417 | -58.80582 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64da5fe2-8956-3cac-941d-e2022b92d257 | -3.64263 | -58.5589 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f560e72-d6d7-38c9-8be0-ba622332c297 | -3.44623 | -50.66381 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d1fc30d7-e57f-34b4-bd23-39887c3dcdcc | -4.38417 | -55.04898 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9f12305-c463-3df9-b93a-f93a9eb24e6b | -2.85811 | -48.67512 | 2026-09-17 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b956a64-3e77-3a3f-8f8b-20a3fa86d79b | -8.2229 | -55.45936 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 451ffd87-71b3-33e4-826c-3583e69efba7 | -3.47709 | -54.68981 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63600a7f-071a-375a-ae97-a7d2969750d9 | -4.50759 | -54.97596 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b50bc0c-5d7f-3027-a885-1a3b0bea3278 | -4.37972 | -55.03408 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a95f004-221c-3bd6-adf3-a7787734a071 | -9.7709 | -46.54887 | 2026-09-17 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6873fda3-a31c-3a79-a20a-40c4fa1bf15c | -5.77332 | -45.11149 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 99ee71c1-bc36-338d-80f5-96f72a91ee73 | -8.29664 | -54.78617 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46ec5554-3e54-347e-9ba1-d05e42519d00 | -4.34043 | -46.61877 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6713279-ffc3-31cf-8968-3d96e09c45b5 | -4.53802 | -54.93453 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33e69fe1-7a12-3bff-b51c-21d96996f805 | -6.79864 | -58.79294 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6455b215-e025-3eea-9543-ee3312109d83 | -5.14316 | -55.93917 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a7521b7-0008-3429-9e07-1d00b529f631 | -8.57913 | -44.56855 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34245568-f316-314d-af32-0d3384c9a779 | -8.13801 | -44.8585 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c5270c74-a110-3ff9-adf3-993812cc4ab2 | -3.81257 | -58.89558 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f7e2a12-ceb7-3b01-9f92-eddb04c2143c | -3.4843 | -54.68738 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cc99d7c-8c41-391d-8aa6-aa963fd892b5 | -6.7979 | -59.18105 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 452ce1a9-7d61-3630-af90-842ef1d4d81b | -9.95021 | -45.30864 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2973e84-702f-3c02-b2e0-db3ec076609f | -6.84013 | -55.75295 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc75da6f-d174-324c-9600-9af8803bea48 | -5.15369 | -55.93728 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4881b34c-a5eb-3d88-a004-194a98db8da4 | -8.58611 | -44.56443 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0d746497-7d90-362f-b067-14b6bcb9f7e4 | -9.10763 | -45.71651 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4531852b-d749-3e70-9e0a-bc2c5f4f3c64 | -5.84091 | -55.72274 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c814aa-7405-34c0-b323-0bd3b9a0a9fb | -2.91089 | -54.18399 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c56317eb-9973-3d24-a5e3-990ccfeb2dd2 | -6.83105 | -58.98396 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 941f3e60-d86a-31e4-b04c-4e9e47f49ca8 | -4.55842 | -42.94791 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 51fe430c-8891-3f09-900d-deb8e5913d19 | -3.13569 | -59.02514 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31ace678-fb0d-3f70-924f-929b5eea6ab0 | -8.86118 | -46.96708 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d4cc972-4462-3172-a245-0ffb44fd3422 | -8.42704 | -47.75184 | 2026-09-17 05:16:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b94754b-0e4d-355f-8ef0-2a81573efa0e | -5.14426 | -55.93224 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c5f29a8-a9eb-3095-8c7e-7ffb702b12da | -3.59621 | -59.0655 | 2026-09-17 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 035c8818-117b-37ea-9e8f-9a7eab333b1c | -6.707 | -58.80465 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d2ff5f5-8575-3007-85b9-fec92ee75993 | -3.47102 | -54.70664 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9664632b-a4da-3831-beba-fed73b605bd1 | -9.95242 | -45.29087 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5716cd5-df90-3766-9a8e-7d2c9305b773 | -4.87596 | -56.06427 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d67f9af6-6214-317a-b5d4-c4cf41ad7f83 | -4.51918 | -54.94581 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8e657f6-ae69-3154-81e6-3b812fb7ecbc | -8.55625 | -44.47709 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cdd75d42-9b1d-3f79-9215-852704c3d7b9 | -7.092 | -41.84451 | 2026-09-17 05:16:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f3fba5e5-6b64-300c-9de4-83b01672cfe6 | -6.81686 | -59.17976 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df161464-c2ed-324d-b332-0ae691af2926 | -6.79573 | -58.78831 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaf5de21-45c0-30ee-ab2f-e6bb0698b0cf | -6.21156 | -55.28344 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4e649fd-9259-398c-b3ea-2257e6652956 | -4.39261 | -55.44366 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a738d560-e3f1-34eb-b5ad-00af89f763fd | -9.60442 | -45.33999 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7c65df5-6385-3bd1-b154-c5f43276fa76 | -8.69626 | -44.86908 | 2026-09-17 05:16:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18b1a030-152c-3a7d-bc42-056f4ab32827 | -8.28415 | -45.65053 | 2026-09-17 05:16:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7828f640-7d2e-3bc4-841a-1d6d7b9d7803 | -4.52968 | -54.92255 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acdff6fc-0cbc-360e-a158-fe4756e18a07 | -4.51366 | -54.95916 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 451dce77-2ff3-3f28-b069-0994c1a04256 | -5.63616 | -44.80817 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3c4a385-40d9-37c4-ac86-7d765e84a7ef | -2.93594 | -54.15562 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af9ab11f-273a-3708-8c19-1bf4fe583616 | -4.29889 | -56.26725 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2f64d8f-8202-3f76-803e-e9e797875db0 | -9.96077 | -45.32433 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 121fef5a-f1fa-36cf-90da-2fe910b7fdaf | -8.00451 | -61.37323 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c023d52c-9729-3450-87a9-ed0282b0df6f | -4.36987 | -55.44015 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17e36cf1-f944-36b8-bd24-1ddb1e69a29a | -8.11476 | -54.81056 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 602d4a27-95ca-3297-ba10-1c30adb8f24e | -9.91011 | -46.51196 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 838faa4e-9818-3033-8748-91a6d28ba385 | -7.08471 | -41.84342 | 2026-09-17 05:16:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 903f131d-1ada-3dad-bff9-0a56302a84ff | -6.75893 | -56.32809 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 495cc213-b678-310c-bd1e-45187eb97151 | -4.54244 | -54.92812 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3f31b44b-8e2c-32e7-85e9-4116dcdb33af | -4.50518 | -48.31431 | 2026-09-17 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33b5d599-db11-311c-8bae-3027d04dcb92 | -5.14538 | -55.94665 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36aaff38-5fce-3811-af91-9b6f944ecabd | -4.52635 | -54.92203 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d273c4-784f-3a9a-93ee-31e891343fba | -6.3692 | -58.28929 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae46be09-5bf0-339b-8012-434474155a3f | -6.80165 | -59.18243 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 473d99ac-fafa-39cf-a921-537acd5078ce | -4.51973 | -54.94233 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43dc7e37-60cc-3b32-9403-d51fc81684f3 | -3.4799 | -54.71512 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 31febbfe-5a18-36be-b4cb-9265026824ab | -6.22471 | -57.77976 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92b6814a-ac47-37d5-8f71-5a0eb873a358 | -3.50596 | -53.20042 | 2026-09-17 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 541a8e8a-f80c-3bc6-a272-cceaf39001d4 | -4.56909 | -54.90364 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b314587-0bf6-35de-99b5-54600e235c3b | -9.99507 | -45.44412 | 2026-09-17 05:16:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d389aa6-9e92-3c6b-ac3d-adf72997c94b | -5.83512 | -52.04931 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13fffed1-7c73-3ca4-85ab-e67b76e087a9 | -5.90255 | -59.93809 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26cf8bb1-96c3-3122-a7df-478eba5da2cb | -2.09404 | -56.42664 | 2026-09-17 05:16:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8021aad1-34e7-36b8-8f42-08dd495d66bf | -9.16099 | -49.99237 | 2026-09-17 05:16:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af783f24-fb6e-3eee-9890-c8fc5d0a2cd4 | -9.88759 | -48.39236 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 444be02f-7ea0-31d6-b7b6-3ed5bd2bf143 | -7.93644 | -44.8322 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2ad2e25b-9399-3c6b-a3e9-8e781f46651c | -6.42736 | -60.00782 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9013f0c-ad01-3927-ad53-bb520ec3b201 | -4.93355 | -55.78833 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65b1497b-dec3-339b-b817-2e2f43075cec | -9.87715 | -48.35543 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bd206367-eaa2-3f2b-9f01-dec1ea466ec8 | -5.91411 | -59.93998 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b704bde3-026d-3180-b3db-0557c29143e5 | -8.85857 | -45.86044 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aec8caa2-c813-37d9-b28d-4c14bebf6b78 | -7.58693 | -46.33413 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa48950-60d3-34f5-8b81-a71a251e8db7 | -4.52713 | -55.66339 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9f5c441-a2d0-35c7-8f22-84a96e2258ba | -5.14071 | -47.60204 | 2026-09-17 05:16:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58284eb6-e5a7-37d7-be71-0247bcb70155 | -3.47489 | -54.7037 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61fe954b-0ef9-3887-858f-b04972bb208c | -5.97712 | -46.63354 | 2026-09-17 05:16:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c209971-ff06-34aa-8c65-61e4f06f0474 | -9.11716 | -45.73574 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 150ca1c3-26e3-3ae1-b155-ea1c40ae4984 | -6.04343 | -44.02926 | 2026-09-17 05:16:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30626fec-374b-3032-bab3-b0862375df85 | -7.37521 | -44.4798 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d52c918f-322c-3841-a85b-df39ed8a5a3b | -4.38693 | -56.3498 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README59.md)
