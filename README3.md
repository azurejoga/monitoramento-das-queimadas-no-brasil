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
| 53ec0080-d360-3fac-b2ae-76f11b2676f4 | -17.4289 | -40.0252 | 2026-09-06 00:12:00 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e639cd8-5379-30e4-963a-ad9ede971c1f | -3.602 | -42.9809 | 2026-09-06 00:12:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2e0d389-9e3b-3b23-9807-1796b536ce72 | -5.6372 | -44.375198 | 2026-09-06 00:12:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c84e041-b2cb-36e8-949f-85f3a671555b | -4.1387 | -45.625301 | 2026-09-06 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 856eea9e-a28f-34f8-85c8-c05aec7e4daa | -4.9047 | -45.098701 | 2026-09-06 00:12:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef248276-c4d1-3007-92b6-c0be4ce417fd | -4.3605 | -47.768299 | 2026-09-06 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34878adc-1c79-32bd-9395-16096e30b63b | -17.427299 | -40.017899 | 2026-09-06 00:12:00 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 506e3711-ec61-3eb1-b9ac-ce3a491a0c15 | -13.7674 | -51.649399 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 567cf860-21f5-3620-ae6a-d7ac88e1190a | -12.7132 | -43.2066 | 2026-09-06 00:12:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 077f7382-40b8-3e59-b570-d8ebe9aaa285 | -18.309299 | -40.9249 | 2026-09-06 00:12:00 | METOP-C | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5f383ff-4ec3-3309-9741-2fca7c87c960 | -10.4751 | -46.069099 | 2026-09-06 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14749182-2807-3e10-a045-d57a3237b72e | -14.9011 | -44.680801 | 2026-09-06 00:12:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 747bf072-19d4-3375-a64d-3267d01b3d23 | -18.92 | -42.097801 | 2026-09-06 00:12:00 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5bc8b8d7-b386-3a72-b483-c8942002727f | -5.5589 | -49.037102 | 2026-09-06 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f994c49e-7c97-33d3-96ae-8d4f2f71dc18 | -10.4777 | -46.033001 | 2026-09-06 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8259bba3-bd4b-3e4f-8919-359eefbfb90c | -14.9207 | -44.676701 | 2026-09-06 00:12:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d491375c-229e-3d8d-9556-635966bc2384 | -12.942 | -42.410198 | 2026-09-06 00:12:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5255dd4d-86e2-3ae0-bcbf-6719789981bb | -19.3552 | -39.9995 | 2026-09-06 00:12:00 | METOP-C | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42303465-7f87-35f3-b3bb-6b63524ce114 | -19.3568 | -40.007 | 2026-09-06 00:12:00 | METOP-C | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a25ac5de-f6b3-3082-8053-31599fdd8e8b | -4.8949 | -45.100899 | 2026-09-06 00:12:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52da48a4-e065-35b0-912e-cd61a31130e0 | -6.7086 | -44.107201 | 2026-09-06 00:12:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d402531f-493e-3358-8d13-507ae7c02f76 | -16.1444 | -40.691002 | 2026-09-06 00:12:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2840da8d-0728-35aa-a1cf-452920671683 | -3.5421 | -48.1861 | 2026-09-06 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 310e099e-c692-3dc4-8c94-e0f6a8a797f1 | -15.4389 | -40.944599 | 2026-09-06 00:12:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75406291-ab13-34ee-a959-b8e43f2919b1 | -8.9735 | -44.410301 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72cac05d-c5e5-35d0-9366-cf9b6ea4af52 | -13.8156 | -51.640701 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94ca5ee3-bd44-3f55-9d4d-0fd189f827d9 | -4.3632 | -47.780201 | 2026-09-06 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b28868d-6678-3279-95eb-3d0a83e49fd2 | -13.7619 | -51.618801 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f68d4546-f491-3d08-95bf-27f403bf4475 | -8.9754 | -44.418999 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 274ef96b-c04d-3f83-be72-59d75ec990e8 | -8.3138 | -37.27 | 2026-09-06 00:12:00 | METOP-C | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 46f13148-df7b-3f54-9b97-8cf6e873011b | -11.6464 | -48.566101 | 2026-09-06 00:12:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c678169-0f47-3a97-a1e6-b0632fc9eee6 | -3.5491 | -48.1717 | 2026-09-06 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244e261b-b5aa-3d5a-8c1b-4d051b0074a9 | -2.2907 | -48.5891 | 2026-09-06 00:12:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7c13d46-2060-3ad6-9a0e-ec85d90ba314 | -18.311001 | -40.9328 | 2026-09-06 00:12:00 | METOP-C | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3148e9ca-a14b-3d94-950d-5f73ce4c49f4 | -13.7716 | -51.6171 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7318696f-4f02-39da-a98e-a46fc8afe030 | -11.6429 | -48.548599 | 2026-09-06 00:12:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 806d5769-d483-3872-aba1-78b4df3831c2 | -12.9454 | -42.4258 | 2026-09-06 00:12:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1b1c31fa-142b-3b2c-81c2-7c9c934c653d | -16.0434 | -40.652 | 2026-09-06 00:12:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d9028a45-6f9f-38fe-9fc0-26ae0de767b2 | -4.2488 | -44.605801 | 2026-09-06 00:12:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8eb093a-c94b-33be-969d-aa31b4c110a8 | -5.7404 | -43.277401 | 2026-09-06 00:12:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf481f8a-87d6-37bb-97e5-ecfeb6538786 | -14.8665 | -40.9123 | 2026-09-06 00:12:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0efe72e9-d844-32dc-848a-e6a2f5e67edd | -17.4191 | -40.027401 | 2026-09-06 00:12:00 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cab905b-71c2-318d-bbc6-78bdfbea4219 | -2.2853 | -46.114899 | 2026-09-06 00:12:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 303b719d-abde-3fd2-8d81-c2bc27d46d66 | -19.5322 | -43.5438 | 2026-09-06 00:12:00 | METOP-C | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 683cf823-a6ab-325e-a68d-0ee5a9bc88b0 | -9.5688 | -40.345402 | 2026-09-06 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ce8a4fb6-fd90-3858-ae03-0f04ce1826d6 | -2.2873 | -46.123798 | 2026-09-06 00:12:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f70e971-3fa9-333d-ad95-046af3500172 | -2.9052 | -48.862499 | 2026-09-06 00:12:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce2edd24-68c0-3172-b7fc-e00676b22c8f | -7.67 | -46.051601 | 2026-09-06 00:12:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe9417a4-06f2-3ffe-8330-772116f807a1 | -14.6082 | -41.047699 | 2026-09-06 00:12:00 | METOP-C | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 414dc3dd-f6a5-3e13-a468-3e60fb450031 | -4.1129 | -49.0975 | 2026-09-06 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9672a09-3323-32cc-b34a-75095a0e8661 | -4.7287 | -46.196301 | 2026-09-06 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f5333e5-dee7-3490-8e3c-3b9b76aa78ce | -12.2729 | -41.558701 | 2026-09-06 00:12:00 | METOP-C | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1237845c-e4a7-3e05-8e91-89a1c7545690 | -5.6355 | -44.367298 | 2026-09-06 00:12:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bb2ab40-e7af-3feb-94a5-0c1c7e29ac35 | -5.5082 | -44.028999 | 2026-09-06 00:12:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7315950-7353-372a-85fc-cc8130dcd91d | -5.38 | -55.98 | 2026-09-06 00:15:00 | MSG-03 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63ee4e71-b273-3075-b6db-3a6c36953421 | -20.4586 | -57.3864 | 2026-09-06 00:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| bfb9cf79-c579-3e40-93bb-358cbcbea97e | -5.5042 | -44.0277 | 2026-09-06 00:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 2c433b75-8fdf-374f-8d9c-7e6bf8fe6b3d | -6.0923 | -47.3129 | 2026-09-06 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e5fd867a-dde1-3cf4-bb9e-ddbf53d51a03 | -6.6698 | -59.9443 | 2026-09-06 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 60018066-f92a-3036-9b6e-3b60b4afb48f | -15.7489 | -49.9145 | 2026-09-06 00:20:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 43a79f10-6304-3bca-a48b-d4ec0092eb76 | -3.5406 | -48.1889 | 2026-09-06 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a26d90c0-5d7d-3ee5-a575-b07f58845e85 | -5.1423 | -56.2703 | 2026-09-06 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7911bc6f-84e0-31c7-90d7-7b1be3c06df1 | -10.7492 | -60.7097 | 2026-09-06 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 581f557d-efe2-33b6-b96c-b3278987335f | -20.4582 | -57.4074 | 2026-09-06 00:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 54194b22-d62b-3d67-b843-6491c0fbe4fc | -6.6699 | -59.9251 | 2026-09-06 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| cf46f7b1-63e3-35e7-8964-12dfb696b1bf | -9.5721 | -40.3475 | 2026-09-06 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 66991733-02fc-335c-aa58-ca126b456421 | -6.6514 | -59.945 | 2026-09-06 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 5295bae3-9c17-3686-846b-a56e90f875c6 | -10.701 | -45.9471 | 2026-09-06 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ae862efe-c400-3fb1-b3b7-7fbe59ee744f | -6.0925 | -47.291 | 2026-09-06 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 04d9e142-972e-35d9-87ae-c42f2fc4677f | -13.7801 | -51.647 | 2026-09-06 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 5f495c18-d1ad-36a0-9f84-2895302a3643 | -6.6515 | -59.9258 | 2026-09-06 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c8c2bde9-2eaa-3155-9613-4d0d50292973 | -3.5591 | -48.1882 | 2026-09-06 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 305712d1-22eb-3a21-88ad-c2a7279a43f2 | -5.1439 | -55.9543 | 2026-09-06 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 84e16304-7772-34b4-aa67-7d204454a096 | -13.7608 | -51.6495 | 2026-09-06 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 611604a8-8caf-327b-a69a-c1ab1b13c5a1 | -10.749 | -60.729 | 2026-09-06 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 9ba439f6-fc71-3365-be77-67d62a28068c | -5.1438 | -55.9741 | 2026-09-06 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 13c0d3c6-5d0e-3db3-9ced-5d4ccc943c13 | -10.6823 | -45.9268 | 2026-09-06 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 18b77c63-df92-3297-b040-d00938050605 | -6.8813 | -55.619 | 2026-09-06 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 710d397d-de5d-37c3-8f40-f34b135063da | -13.7605 | -51.6708 | 2026-09-06 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3c56ac4a-6933-3f05-87b7-74b3d6396a40 | -9.3665 | -67.8263 | 2026-09-06 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ba4e43e8-f867-3a4e-9d91-b41de009cadc | -13.7993 | -51.6445 | 2026-09-06 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 276569bf-e006-3961-a390-f25f7b207e2c | -20.4384 | -57.3893 | 2026-09-06 00:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| f70e39c1-0d4a-38ba-aaa9-c815ef4c9f82 | -10.7013 | -45.9244 | 2026-09-06 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| fa839201-9e80-3ecc-bb97-f32fb244a001 | -3.2239 | -53.1742 | 2026-09-06 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9ddfc4c2-9b9e-376b-bfea-f4187bcfb488 | -6.0737 | -47.3142 | 2026-09-06 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 3fd34dff-9e4d-319c-bb2b-aee4d7ae795f | -7.7616 | -67.1615 | 2026-09-06 00:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c1e9e7bb-1cdc-3c8c-9c8d-b2dc9126a791 | -9.1257 | -67.8322 | 2026-09-06 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b9eec841-d8b8-3423-85f3-f6de7bcb5a13 | -15.7685 | -49.9114 | 2026-09-06 00:20:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 03719f7f-73e6-3915-b07c-869cdeebea91 | -14.9246 | -44.6744 | 2026-09-06 00:20:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 197619fa-d455-3f30-8572-245cb4651077 | -30.80392 | -52.81423 | 2026-09-06 00:20:00 | TERRA_M-M | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 11.4 |
| 04dea659-e6fb-310d-aa6a-c6c220e69709 | -15.76867 | -49.92292 | 2026-09-06 00:22:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 653d5b41-8b34-3b4c-aad5-772ffb4e166e | -15.71666 | -43.70791 | 2026-09-06 00:22:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 4daf0358-affc-3edd-af7f-582bc2cd6f06 | -15.76687 | -49.911 | 2026-09-06 00:22:00 | TERRA_M-M | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 49af047d-cd15-377e-b30b-ffa8a2db676e | -14.91314 | -44.6961 | 2026-09-06 00:22:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 9dfdd201-d516-3b0b-bcdf-1c59cff2a729 | -16.40524 | -49.21254 | 2026-09-06 00:22:00 | TERRA_M-M | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c9ea457b-3931-3fd7-9432-97ca84dc6b0d | -15.75691 | -49.91287 | 2026-09-06 00:22:00 | TERRA_M-M | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 06323113-53ed-3038-8d8c-e44e4189bc7d | -20.44431 | -57.39467 | 2026-09-06 00:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 137c14ae-1248-3158-b264-f92ee87d13b4 | -20.45628 | -57.40348 | 2026-09-06 00:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 31c50083-a11f-320e-a9ca-07f410055729 | -18.924 | -42.08933 | 2026-09-06 00:22:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| 61ac2347-ccf7-3895-a071-d9496a657298 | -16.39714 | -49.20647 | 2026-09-06 00:22:00 | TERRA_M-M | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |


[Clique aqui para ver as próximas entradas](README4.md)
