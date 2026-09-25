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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20bfd2b4-a192-325d-be4b-e43f8438fe63 | -3.2314 | -46.9376 | 2026-09-25 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| b60dd1a4-5467-3236-b772-f76a9ef4e41c | -5.7754 | -45.1053 | 2026-09-25 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 654fbf06-266c-3976-9443-6706ac190bd0 | -9.1536 | -59.464 | 2026-09-25 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6756a189-c704-3861-b51e-e5bea55b0b75 | -11.91 | -50.71 | 2026-09-25 03:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a368e3e-58f6-3ae0-a821-561a8af0cad1 | -11.94 | -50.67 | 2026-09-25 03:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 89f1e691-ab03-31d3-b030-5e10b803d1a1 | -11.94 | -50.72 | 2026-09-25 03:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a16aee38-189f-32e0-9b61-ed29426c53d0 | -12.2063 | -50.7316 | 2026-09-25 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 16dac491-ffd0-38ad-9302-1d8cb39887db | -11.7332 | -50.5516 | 2026-09-25 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 3e4a9285-620f-3e3b-aa9a-de14c2fafe77 | -5.7754 | -45.1053 | 2026-09-25 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 421fa5f9-691c-35b3-9798-679109413c24 | -11.7329 | -50.573 | 2026-09-25 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a8f6f512-6406-336e-a56d-ee920ee6526c | -12.206 | -50.7531 | 2026-09-25 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b78d6d99-3e80-3855-b076-7a79a24fa5ce | -1.1461 | -54.0996 | 2026-09-25 03:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5c145f08-eaae-3fd9-aa5d-406badbc1996 | -12.1866 | -50.7767 | 2026-09-25 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7bdd2a17-d1b0-3aba-abb0-510ef09700fa | -9.1536 | -59.464 | 2026-09-25 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c971dffd-0170-3b10-91f7-d9b6df013ee9 | -12.1872 | -50.7339 | 2026-09-25 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 43a27281-c279-3d34-99c1-3bd0ce415868 | -9.1535 | -59.4834 | 2026-09-25 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f8ece002-0428-3b9f-b927-783753224766 | -12.2057 | -50.7745 | 2026-09-25 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 61c37cb9-7a8a-3d1d-8ea7-aae7843ed34b | -8.34 | -44.1427 | 2026-09-25 03:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d79b2ac3-3518-388d-88ff-da70f61b469a | -3.2314 | -46.9376 | 2026-09-25 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 186758c1-b8ca-349a-98fd-4d9c288808bb | -3.2047 | -53.4179 | 2026-09-25 03:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 57e81f2a-15e0-3b10-9658-4d761856fb43 | -12.1869 | -50.7553 | 2026-09-25 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 6b97f4be-7599-3075-9d1a-03148ea5a885 | -11.7522 | -50.5494 | 2026-09-25 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3e08b3c8-7e3a-3aff-b387-f55cf5bd36ee | -9.1535 | -59.4834 | 2026-09-25 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4bad5c6c-bd04-3d56-b7bc-8e8f4b40dbfa | -9.0343 | -60.5321 | 2026-09-25 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 23a664dc-a6f5-33f9-ba37-3e5b4da74ffd | -3.2047 | -53.4179 | 2026-09-25 03:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| cdb898c5-b967-37fe-9052-608489d589f1 | -8.34 | -44.1427 | 2026-09-25 03:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| be3e76e4-6cde-3684-9f3d-d4738e6a3534 | -11.9593 | -50.6965 | 2026-09-25 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2a41e3f2-eb20-338e-9aa2-8d4a554ee186 | -9.0157 | -60.533 | 2026-09-25 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5cb7c4b4-3a39-3c3a-84b6-55f68700ec07 | -5.7754 | -45.1053 | 2026-09-25 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c4900542-472c-3aa3-8985-19fab8954874 | -1.1461 | -54.0996 | 2026-09-25 03:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| eb521826-0b63-3c22-87be-6133b7224149 | -3.2314 | -46.9376 | 2026-09-25 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| fd99f9c2-a89a-3c4f-96ec-924964cd145b | -1.1461 | -54.0996 | 2026-09-25 03:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 1e9974bc-66e2-3e77-8f7a-e5201164f1cd | -8.34 | -44.1427 | 2026-09-25 03:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 45989607-08da-3e62-aec1-3e9db1f067af | -11.9399 | -50.7201 | 2026-09-25 03:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 93dbbc84-4823-3978-b9c9-711ed9b10261 | -9.0249 | -49.6334 | 2026-09-25 03:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 83d50741-5990-38dc-839f-20d4d9bb199c | -3.2314 | -46.9376 | 2026-09-25 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 2a681087-037f-358c-88dc-c10f51cd1aef | -5.7754 | -45.1053 | 2026-09-25 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1ef521b3-5e58-3923-bd84-844c3a38318b | -9.1535 | -59.4834 | 2026-09-25 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e07e650e-8bc0-35f2-81b9-d90779b56f33 | -3.23158 | -46.94395 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c37d5747-e529-3f20-b93d-8e365459e7e9 | -4.46168 | -47.92544 | 2026-09-25 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59b48bee-4faa-3d7a-856b-f49ddda47519 | -3.23438 | -46.9269 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8458b737-322a-3245-bd86-6dc5bf75eceb | -2.8651 | -49.63114 | 2026-09-25 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6fe9a26b-7db7-33d6-b628-f901ba2fe6ad | -6.43021 | -35.25286 | 2026-09-25 03:47:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e2d30b6d-4f00-33b1-9114-997044de0876 | -4.84996 | -42.90136 | 2026-09-25 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9379b9e0-430f-3e15-a77c-d483d525233b | -4.96087 | -37.40654 | 2026-09-25 03:47:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8790aa8-8c03-3ca9-9b27-345153e4a763 | -3.23128 | -46.93545 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 682f7d22-e962-3bff-9b33-197a10911df7 | -3.2379 | -46.93218 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9be7be2c-3c08-3b26-bec2-c2f3fc70858c | -5.01418 | -41.7134 | 2026-09-25 03:47:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3b47b014-acc1-3385-afc4-4667d1d7aefc | -4.4625 | -47.92063 | 2026-09-25 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 880ee084-935b-3ea2-b15a-b51cbd293ce6 | -2.87052 | -49.63244 | 2026-09-25 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09ef5c95-2277-3a06-96e7-545d7000b57e | -3.22982 | -46.94394 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e2d159c9-78ea-3f6a-b177-11ba5ab53a82 | -3.45141 | -50.086 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da3333fa-c211-398f-848a-2810bac1c09b | -5.04675 | -45.53471 | 2026-09-25 03:47:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb238c44-2e4a-3f05-b8fb-3625d21ec298 | -4.02225 | -42.46612 | 2026-09-25 03:47:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3367717a-5234-33c8-a1ad-c5f0bd370547 | -3.23368 | -46.93118 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 11387304-256d-3ceb-b689-ad7720b35a87 | -3.4443 | -50.08482 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f8cb8ed9-407a-3266-bd3c-52404996335e | -1.9604 | -48.38247 | 2026-09-25 03:47:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 199e4683-7409-3f80-a074-815d9db5de6b | -5.04152 | -45.5338 | 2026-09-25 03:47:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 713b1259-1c5d-3348-9b13-7cabc241f9b7 | -3.76994 | -47.54633 | 2026-09-25 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ef97b5b-e546-3886-a92e-af17e42b0ab2 | -2.92051 | -40.90079 | 2026-09-25 03:47:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| eb135ea0-1964-3f17-9293-d5bbb32c780f | -6.29402 | -35.24337 | 2026-09-25 03:47:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7c9884b3-444c-3c0c-ad4c-5f3eac43b560 | -4.61364 | -42.80038 | 2026-09-25 03:47:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fb198b0-a32d-3746-823d-ecb505658aea | -3.23201 | -46.93119 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ae17ca1b-60ba-3818-ab57-88cfed9dbb79 | -5.12318 | -42.69165 | 2026-09-25 03:47:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14c3a917-8549-3293-9fdc-180d0915266d | -4.28547 | -48.61135 | 2026-09-25 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 197c594a-8cf2-37b8-aa25-5bd0780aa1f0 | -3.23274 | -46.92693 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 394c2640-90a6-320a-932c-4b3e18815c0d | -3.26075 | -49.19179 | 2026-09-25 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96ee0352-e0b6-32a1-af84-09d46ba54f2b | -3.23717 | -46.93644 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| dfdd5de4-10cd-3dc1-bc85-9fdcb2644ef6 | -5.17115 | -35.9292 | 2026-09-25 03:47:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6da3e7ae-d206-3590-84c6-f052a7082729 | -4.61503 | -42.79196 | 2026-09-25 03:47:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b027a1f-5520-3ae6-8eb6-c84c525690fa | -6.2974 | -35.2439 | 2026-09-25 03:47:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1a6d8e5-b405-3b37-82f2-ff15e1a070bc | -3.06009 | -46.92883 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 044b6b9a-a92b-3480-98e3-495c36e109fb | -3.23863 | -46.92793 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1e6ef9d6-18f1-3988-93b7-49778b64e73d | -3.77072 | -47.54188 | 2026-09-25 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51132339-7462-31de-bb3c-8efb8d276633 | -4.61433 | -42.79618 | 2026-09-25 03:47:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40646627-9c40-3eda-9a3c-9ed176538dce | -4.3773 | -46.23873 | 2026-09-25 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99c3b9e9-ad6e-3a02-8c50-b7f93e33fd2b | -4.95672 | -45.14835 | 2026-09-25 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d8db727-ad0b-3f61-8a51-2ead1f46c7c1 | -3.23228 | -46.93969 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 65ab9d7a-c76d-33f3-9cad-09a098354498 | -3.98239 | -48.43223 | 2026-09-25 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7f54231e-5959-3d05-b1ac-e04938d5fb5d | -4.78047 | -46.50158 | 2026-09-25 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbf906da-ee68-3bfb-9b7e-757ca4d350d8 | -5.427 | -36.75795 | 2026-09-25 03:47:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3f03e487-2ea1-38f2-93ba-d17e92a5ccac | -4.61067 | -42.79125 | 2026-09-25 03:47:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efd9b10c-1b62-3924-aa0b-157e2438dabb | -4.30456 | -48.06918 | 2026-09-25 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d19254c9-aeac-3624-abeb-baac85e861d8 | -5.14634 | -45.18136 | 2026-09-25 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af107362-bdce-3d36-9ca6-c376c470f5e9 | -5.15144 | -45.18217 | 2026-09-25 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83f616a5-1ec6-344d-8c61-bd8e8d4c98f6 | -3.23957 | -46.93217 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 57d8f345-b3a9-35e5-a8bb-bfd22ac219e8 | -3.23055 | -46.93968 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2c0f5fcd-3bd0-3113-802b-3fc759716cdf | -3.24452 | -46.92891 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7c79d1c0-01ba-30be-bab8-88200e3b576f | -5.14685 | -45.17842 | 2026-09-25 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8265bd6-bb6d-3b55-bdda-200e1e0d1546 | -5.24751 | -36.75103 | 2026-09-25 03:47:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17fda26e-cfad-3738-ae7e-e5143e803afe | -3.24027 | -46.92791 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d9e1e952-902f-3997-958d-f7099083e21f | -3.44549 | -50.07808 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aef0fa3d-aabe-37d2-949e-1f84929229e0 | -3.45263 | -50.07909 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c57222e6-b0ad-3a26-b5cf-506c9c6a54cf | -5.12384 | -42.68754 | 2026-09-25 03:47:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 188ca035-1977-3e7b-9f4b-143904308587 | -6.43076 | -35.24919 | 2026-09-25 03:47:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5a312651-8f69-36bd-9404-5d85aed8afa1 | -3.44752 | -50.08539 | 2026-09-25 03:47:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ff8d367a-2eaa-3cd8-97c3-616e1c23126b | -3.23298 | -46.93544 | 2026-09-25 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 1cf5638b-6e00-32ba-bd4d-63ef05bed5da | -5.93481 | -35.38904 | 2026-09-25 03:47:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8e70290-5de3-3ca2-aa34-d0651baddaaf | -5.09832 | -45.51891 | 2026-09-25 03:47:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c45f0a4d-1ddc-37e9-9627-1918f671d3e2 | -2.8721 | -49.63224 | 2026-09-25 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README11.md)
