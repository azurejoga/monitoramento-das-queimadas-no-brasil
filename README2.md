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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abc78402-eaed-35a0-b63e-a36f2207ca67 | -20.7764 | -57.906399 | 2026-07-18 00:20:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d9ae755f-560b-3cd6-9456-e65cb13cc7cb | -12.5009 | -48.247101 | 2026-07-18 00:20:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 175c116d-8cbc-3667-91db-6ee364515375 | -9.3951 | -48.562401 | 2026-07-18 00:20:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 062d4f9d-18a4-3444-8faf-17c0271f9237 | -10.5271 | -48.150002 | 2026-07-18 00:20:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96c9a53d-66e4-3ca8-baee-9bbdd4d8aeee | -19.7868 | -48.250099 | 2026-07-18 00:20:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4283d04c-2b36-3d2a-9a66-f837626f677a | -8.6907 | -49.845402 | 2026-07-18 00:20:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df79434-7c6f-342c-8373-97274b656906 | -7.291 | -46.2491 | 2026-07-18 00:20:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 365ceaee-af3d-3aaf-9a98-750c5badd28e | -7.9089 | -48.251701 | 2026-07-18 00:20:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4eaed33-9746-3b14-9782-73e65163da56 | -11.7855 | -45.926701 | 2026-07-18 00:20:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf9ad8a1-b951-3170-827b-7523020e3783 | -18.7306 | -54.190899 | 2026-07-18 00:20:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f43ab2a7-a970-3a4d-9278-dd267402a9fc | -20.6348 | -41.391201 | 2026-07-18 00:20:00 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8593aa2-369c-3027-88d8-70caf442913e | -22.4098 | -51.520302 | 2026-07-18 00:20:00 | METOP-B | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10d9cea3-b70a-32d6-bd52-d20c978063f7 | -8.7152 | -49.592899 | 2026-07-18 00:20:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1f7f8b-e082-3138-91e1-cfae98248746 | -14.892 | -48.453999 | 2026-07-18 00:20:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 317b1c18-4973-3aff-890a-e5f9860583f3 | -22.3914 | -51.5354 | 2026-07-18 00:30:00 | GOES-19 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| a408bf3f-1f12-33c1-a3ec-3903256da007 | -22.4122 | -51.5309 | 2026-07-18 00:30:00 | GOES-19 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| 65cda82c-ef41-313d-827f-3d78e29cc51c | -15.7676 | -49.9555 | 2026-07-18 00:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0c681ea7-4a9d-3fa9-880b-9cf3202aa894 | -18.7364 | -54.1988 | 2026-07-18 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 84.3 |
| b892a3e5-207e-3c47-84ac-6d09c7586af8 | -29.2983 | -55.5593 | 2026-07-18 00:33:00 | TERRA_M-M | MANOEL VIANA | RIO GRANDE DO SUL | Brasil | 4311759 | 43 | 33 | nan | nan | nan | Pampa | 7.3 |
| 416a66fb-5d8c-31e5-9661-398adadf7c2b | -29.83118 | -51.92493 | 2026-07-18 00:33:00 | TERRA_M-M | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| dc71c2ac-bbea-322c-b61b-857feb40bef5 | -28.98739 | -53.66312 | 2026-07-18 00:33:00 | TERRA_M-M | TUPANCIRETÃ | RIO GRANDE DO SUL | Brasil | 4322202 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 9ee96c45-67f6-393d-81f6-ae4bc21221e8 | -29.02882 | -52.38298 | 2026-07-18 00:33:00 | TERRA_M-M | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5ccf7f9c-47cc-3323-88a3-500fd49f70ea | -29.87456 | -55.90581 | 2026-07-18 00:33:00 | TERRA_M-M | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 14.0 |
| 58c65cdd-8f34-3189-b61b-ce902fd6adcb | -28.8552 | -52.59204 | 2026-07-18 00:33:00 | TERRA_M-M | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| d7ad3953-0680-3925-adb3-b0b273b7be53 | -29.75827 | -53.88105 | 2026-07-18 00:33:00 | TERRA_M-M | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 512f8775-c11c-3ef6-8f88-8bd2cf40d3c4 | -30.11992 | -52.08353 | 2026-07-18 00:33:00 | TERRA_M-M | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| 1c6e6bb2-96f0-3e29-9876-9302004f61b5 | -20.78469 | -57.9412 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 814de028-a824-3cce-ac62-6fb0c73109d1 | -18.73529 | -54.21116 | 2026-07-18 00:35:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c867c994-91ca-3553-9130-e002c9dfe790 | -22.2571 | -52.87238 | 2026-07-18 00:35:00 | TERRA_M-M | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 4eb9fa21-29e9-31fb-b47b-01af0d43d196 | -22.40209 | -51.55168 | 2026-07-18 00:35:00 | TERRA_M-M | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| 7c067694-ecc2-3d55-bf68-27755a1e7a5a | -20.5673 | -57.39576 | 2026-07-18 00:35:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b233e08d-6cf7-3501-baf4-c19dde6ea6bc | -21.66153 | -56.33116 | 2026-07-18 00:35:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f37f6672-05f9-34fc-b9e5-618b22ee3079 | -19.87164 | -57.95712 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 98a67344-b525-30c7-9287-9f68929b730f | -19.83603 | -57.99297 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| c86241f1-bd06-310a-8e97-7c4901089ebb | -19.82587 | -57.99433 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 2aacaf95-676b-37a8-bf5c-de5519fcdc9c | -19.7851 | -48.26357 | 2026-07-18 00:35:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 03f7b546-5e97-33ba-b83e-c160e40aaa64 | -22.39882 | -51.53036 | 2026-07-18 00:35:00 | TERRA_M-M | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| 081da7b5-0877-30a9-b86c-bf5cee979d69 | -26.6071 | -53.58137 | 2026-07-18 00:35:00 | TERRA_M-M | GUARACIABA | SANTA CATARINA | Brasil | 4206405 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8afbad1b-19f3-3d10-af24-26fe77572c58 | -15.75228 | -49.95689 | 2026-07-18 00:35:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| d0b17fe4-3c9d-314d-81a4-055ed3cb84a5 | -18.74285 | -54.20044 | 2026-07-18 00:35:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 27980536-6615-38bc-9885-43a971c4f739 | -21.27586 | -49.15591 | 2026-07-18 00:35:00 | TERRA_M-M | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| dd815018-d4cd-376d-a849-4e4128e8e049 | -22.24815 | -52.87393 | 2026-07-18 00:35:00 | TERRA_M-M | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| b92cea04-81a4-346e-acb9-1934cbf9ec57 | -23.92784 | -52.50874 | 2026-07-18 00:35:00 | TERRA_M-M | ARARUNA | PARANÁ | Brasil | 4101705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e63bbd1c-f8ab-36ab-b453-6422b86e5916 | -21.91902 | -53.80387 | 2026-07-18 00:35:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e7020b60-9d82-3c74-baf9-325c13a519c7 | -18.73398 | -54.20181 | 2026-07-18 00:35:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8c0b0fb9-f84e-3491-a387-ed817f05be84 | -19.81834 | -57.93223 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 16147a18-3c01-305b-b701-042ff8bd8332 | -20.77444 | -57.94257 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 49832776-d747-3bf5-b766-60c51649d036 | -22.40046 | -51.54103 | 2026-07-18 00:35:00 | TERRA_M-M | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.8 |
| c6e87cf0-7250-3dcd-bb39-dffefe182f52 | -22.7981 | -49.34515 | 2026-07-18 00:35:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 5ae9f720-99e0-34ff-9320-fc139a45a104 | -15.75502 | -49.97322 | 2026-07-18 00:35:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| df6f864e-52e5-362d-9ee5-7ddc5cb5709b | -15.75864 | -49.97815 | 2026-07-18 00:35:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 4567b57f-49c1-372c-8040-1e455f00c042 | -22.24956 | -52.88367 | 2026-07-18 00:35:00 | TERRA_M-M | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 72217ebe-482f-3a67-ab39-f4c7c50bcc6d | -18.73267 | -54.19246 | 2026-07-18 00:35:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8381d9b3-cf7c-32ba-886a-fcf240393592 | -20.56586 | -57.38398 | 2026-07-18 00:35:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 529a15db-03de-3b92-8600-d6bc89bce183 | -19.83542 | -57.99998 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| a0f48332-64fb-3656-9130-f41d9f74c2cc | -21.67097 | -56.32989 | 2026-07-18 00:35:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 320fa856-c698-34da-be90-b9bddef259a3 | -19.81985 | -57.94461 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 38f9bd8e-4edc-3894-b64c-041d0e5e1ea8 | -15.75605 | -49.96188 | 2026-07-18 00:35:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2cd0452d-7d2e-30af-aa4f-38e20af930ca | -19.81422 | -57.98322 | 2026-07-18 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| b9ce3ea2-b0f6-3315-9140-955e18f676fb | -12.45013 | -49.59454 | 2026-07-18 00:37:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| cfc4e3e9-d0ee-330c-a011-08c9bda23a90 | -12.53839 | -57.22889 | 2026-07-18 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 55e70073-2cc7-31ff-b8e1-e2e1b1552e4b | -9.47747 | -57.32061 | 2026-07-18 00:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5bc2bff4-ab42-3b87-8e92-bcc0a2744ca6 | -9.47869 | -57.32962 | 2026-07-18 00:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c8900a6f-4112-34d3-a672-7fb00dc18f7b | -14.09035 | -50.3643 | 2026-07-18 00:37:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d5ee93f3-9d0f-356a-a32c-e456c6424893 | -8.47766 | -50.23065 | 2026-07-18 00:37:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 8bc9c93e-3342-3f72-98fc-ea4dc8a0d012 | -8.12899 | -47.87679 | 2026-07-18 00:37:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4a36e71d-4fee-39a6-a221-ed85268ef584 | -9.16039 | -50.88136 | 2026-07-18 00:37:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1cc55910-1e81-3e8b-87bc-bcac626b3c4f | -9.07432 | -50.60106 | 2026-07-18 00:37:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 73aff954-cccd-343f-ab4b-073b4cf803cd | -12.46266 | -49.59876 | 2026-07-18 00:37:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 52952655-b1cf-3c27-8b29-c27e92ecfa1e | -10.53213 | -48.16374 | 2026-07-18 00:37:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 8760abb1-29c1-3e99-98e0-c757ed62bd2d | -9.89975 | -53.39383 | 2026-07-18 00:37:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac9ec60f-9b95-3eca-b685-dba8f5317ab5 | -10.22257 | -59.41857 | 2026-07-18 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c669f2b2-525b-387e-8765-cb5ac1ed1b84 | -12.46276 | -49.59214 | 2026-07-18 00:37:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1d499ba5-011d-3418-8d7c-eca9e0048981 | -15.67428 | -56.2561 | 2026-07-18 00:37:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 394936b9-e903-3dba-bf77-f0824612bf8d | -10.91218 | -56.36378 | 2026-07-18 00:37:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 464fa873-7d28-3e4d-ad0c-84fe398147a6 | -9.68715 | -56.10056 | 2026-07-18 00:37:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 10ac1672-3312-3fa7-8ebe-ed1e4f4ac6ce | -11.54586 | -48.27278 | 2026-07-18 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| e38f6c7f-7104-3344-84f9-e6942ac0f4ce | -12.45002 | -49.60116 | 2026-07-18 00:37:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dc3fe76d-0633-3f71-8f00-a53c3a8a7f9f | -12.12337 | -49.93893 | 2026-07-18 00:37:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| d0c14d66-759c-3d84-9f48-b2a70c08bdf9 | -9.16885 | -50.88609 | 2026-07-18 00:37:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ba51c13e-4bbe-3067-9d47-10a9e3e85d27 | -3.02395 | -55.90261 | 2026-07-18 00:39:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35dd1395-b3f5-3b6c-9b39-75ab64eadbd7 | -18.7364 | -54.1988 | 2026-07-18 00:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 100.7 |
| f98030ce-9b07-32d2-9731-8c11484dd066 | -22.4122 | -51.5309 | 2026-07-18 00:40:00 | GOES-19 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 18b45a1a-54e2-3ffe-895c-edb574b3cb78 | -22.4116 | -51.5536 | 2026-07-18 00:40:00 | GOES-19 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 7499e4fe-6f4e-3bae-8861-9c7059390633 | -10.5337 | -48.152901 | 2026-07-18 00:46:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 786f2123-135a-347c-8b89-26fa48b99a5e | -5.9366 | -43.648399 | 2026-07-18 00:46:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0325216b-5928-3105-946b-d2b3e6ffcf32 | -8.7197 | -49.601299 | 2026-07-18 00:46:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae26b25-3dc9-329a-90e4-93396edfa1e0 | -7.9152 | -48.252399 | 2026-07-18 00:46:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41e706a1-d112-33e4-9f7a-1720b316f3df | -7.8538 | -48.387798 | 2026-07-18 00:46:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5402d88-f385-3f2b-a357-8e177a27c4e5 | -9.5278 | -47.109299 | 2026-07-18 00:46:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2abf26-c97d-3553-805a-b83c0f6faa98 | -18.732201 | -54.187599 | 2026-07-18 00:46:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f6db8c9c-a271-31a5-b472-f38370ccc850 | -20.633301 | -41.385799 | 2026-07-18 00:46:00 | METOP-C | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e64a37ca-49d9-33a5-8931-475b5a7ac83b | -10.5353 | -48.16 | 2026-07-18 00:46:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c8f1fc1-6cd8-3540-9185-904f9fe7213a | -22.241199 | -52.8601 | 2026-07-18 00:46:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b03aa5f6-8673-3478-8ab1-e9d8e4d65bb1 | -11.7915 | -45.932701 | 2026-07-18 00:46:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 373ee6c5-44b7-3955-92dd-e555b7c19d8a | -22.394899 | -51.541 | 2026-07-18 00:46:00 | METOP-C | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2600f0cf-6515-3211-8dd0-023b6de9e9d0 | -5.5313 | -45.2649 | 2026-07-18 00:46:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71dc30ae-1b6e-398a-b7f6-3e0d89d7cbbb | -22.2509 | -52.8582 | 2026-07-18 00:46:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5770cc2e-12b6-302a-bb3a-5291bdf3452a | -22.404699 | -51.539001 | 2026-07-18 00:46:00 | METOP-C | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae2f23e1-fb5e-33d0-bb35-39709d86542b | -9.0918 | -50.611401 | 2026-07-18 00:46:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
