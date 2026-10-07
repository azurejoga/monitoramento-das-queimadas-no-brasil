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

## Dados Diários - Página 255

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df9fd61a-dc46-383e-a776-b159dc92581f | -5.977 | -43.529 | 2026-10-07 19:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c52fe726-175a-35b5-999b-a47833874178 | -9.96 | -43.481 | 2026-10-07 19:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| d9dea9ff-b5fb-337b-ad2a-579e5211a25b | -2.9327 | -58.3204 | 2026-10-07 19:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 1c48f24e-579c-3257-a118-59bde485961a | 1.3346 | -50.8711 | 2026-10-07 19:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b3fb9787-4355-3c53-a394-777c22e12620 | -1.9535 | -54.0493 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 07d0ebca-4e96-3a7d-a873-0406b015dd41 | -1.1094 | -54.1601 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| ddf942c5-a194-3170-8f7e-4774cacef8a7 | -8.5366 | -67.069 | 2026-10-07 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 34d70372-51e5-35a4-8c3c-81b8732c74bf | -12.1922 | -44.7953 | 2026-10-07 19:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| c9d66d5d-2e86-3e70-abe6-54370242a3e6 | -3.7166 | -54.2096 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| e5dc378a-dfd5-3953-83b4-6e5668dd1b45 | -5.9772 | -43.5057 | 2026-10-07 19:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 988bc0a2-9cdd-3627-bcd2-5422281b4325 | -2.6859 | -49.0539 | 2026-10-07 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 7263ec84-b770-3fb5-a0b3-09c0f895ff2e | -6.6037 | -53.0321 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 5978b289-6169-306d-ba13-36cfbcb7bc65 | -6.8764 | -43.685 | 2026-10-07 19:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 211.5 |
| cd6f1fe7-cd95-3d44-aff5-2691f13b8330 | -2.1361 | -54.4671 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2e582535-196c-3042-a41f-6c02b1be5d81 | 1.6937 | -55.6461 | 2026-10-07 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 3b78de5a-da86-3a90-a2e1-9568076e2803 | -9.9409 | -43.4835 | 2026-10-07 19:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e6c49918-8214-3646-af61-53f6bbc91663 | -8.5368 | -67.0135 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 061c29d2-edf9-367c-9972-e2def45dcc4a | -3.55 | -54.4952 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 01105138-f28f-3db2-9aca-ea09db1d1094 | -5.4958 | -42.8413 | 2026-10-07 19:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 187.3 |
| 157ca7bb-f665-3ef3-bc88-af58cbde5d40 | -4.1458 | -43.187 | 2026-10-07 19:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 50323e42-8c04-31f8-8c15-1095e7205b0b | -3.7622 | -41.7924 | 2026-10-07 19:00:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 188.4 |
| 18b365b1-f1ca-36f9-a2ba-0f61ca7bbc1f | -13.3865 | -43.8708 | 2026-10-07 19:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c78d2b6b-d66e-3b61-8651-f114f47a5421 | -3.2199 | -54.3038 | 2026-10-07 19:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 57e1ec42-1c02-372c-9701-9e261ae09d0a | -4.1551 | -54.9165 | 2026-10-07 19:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7d0dd400-cab9-3154-97ac-c9fd00c213f6 | -3.5873 | -54.3739 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d38b3f9a-5134-327d-b615-2aa97eb2da70 | -5.8205 | -53.8255 | 2026-10-07 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 52a68adc-2317-3d69-bff9-55c4f0abb75f | -3.7809 | -41.7913 | 2026-10-07 19:00:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| d9bf3e0c-698a-3c2a-b507-120c9b73d111 | -4.7954 | -55.7097 | 2026-10-07 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d1e76fc9-8dd7-377c-b851-2f01d647da2c | -6.1402 | -53.0574 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1192799a-8b0a-3bbd-9981-365ae2496682 | -7.1709 | -47.8024 | 2026-10-07 19:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 2baa7621-cc34-35a6-8bc7-9109bd97485e | -8.9961 | -45.9228 | 2026-10-07 19:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 0164a86c-db21-3c81-8bed-193371529316 | -9.1015 | -45.1164 | 2026-10-07 19:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 83f8479e-1089-30ef-9aac-51cf737e59df | -3.0184 | -54.1082 | 2026-10-07 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 38e59eff-9440-3645-a65e-b0a32e50d221 | -6.9737 | -45.124 | 2026-10-07 19:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c8c912f1-66e8-3a0d-9895-8fb789910148 | -6.1244 | -47.9227 | 2026-10-07 19:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| aa3e3465-66ea-3077-9041-575097c39981 | -6.5853 | -53.0127 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| d1603510-57fb-3171-966e-28ff33d98959 | -5.8204 | -53.8457 | 2026-10-07 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 45095477-8649-38f5-a9aa-3ed0d2d7839b | -5.9644 | -40.9627 | 2026-10-07 19:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 8871e94d-e1f9-33d4-891d-c568eb252bd3 | -3.5127 | -54.6562 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 594cec6a-eecf-375d-8a71-669a2197d279 | -3.7166 | -54.2297 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d361e665-c506-3051-a3d4-6f91325f5f98 | -2.7043 | -49.0533 | 2026-10-07 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 1b573be2-20cf-3ead-a0b6-83e6b71ae323 | -4.777 | -55.7104 | 2026-10-07 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| edbd4e4d-1468-33ab-b1d1-bd53c7514d53 | 1.3346 | -50.8503 | 2026-10-07 19:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 048b8a62-6b12-38a0-8753-baef7635dfc4 | -3.569 | -54.3344 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7d9182e3-3cbb-39cc-b878-536150e4832d | -3.5684 | -54.4946 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| fa0f13f5-4913-3b12-a301-cc1f92cc1afc | -3.1973 | -50.5382 | 2026-10-07 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 4e793c9d-565a-3dc1-ba31-9e2a86e2f5cf | -8.5183 | -67.0139 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 163.0 |
| f6a4a846-5226-34b9-a041-382f8473953c | -3.5865 | -54.5742 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 66a55e8d-5726-3cc4-b358-1791be3c1362 | -5.9647 | -40.9383 | 2026-10-07 19:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 284.3 |
| dbb71cc4-2d6b-3f31-a916-5f8c94cb281a | -6.211 | -40.7943 | 2026-10-07 19:00:00 | GOES-19 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 101.1 |
| fc36a916-4fa2-34d3-97ab-bdfbeee5c6b2 | -11.2333 | -44.8678 | 2026-10-07 19:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 818792a6-c69f-34f4-8cca-48f5c2ce523e | 1.8768 | -55.7227 | 2026-10-07 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c23c28a6-0c34-3453-afe6-8ff9e5d3ca75 | -3.5311 | -54.6357 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e2225356-e722-394c-844b-6f02e9ef5873 | -3.195 | -42.9772 | 2026-10-07 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| b8ab83d5-7f19-3a20-a0be-85e63c4ae11f | -10.4727 | -47.211 | 2026-10-07 19:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4f72e064-b91c-362b-ae53-ee68f412db6b | -5.9649 | -40.914 | 2026-10-07 19:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 140.4 |
| ef6220d0-bdd1-3212-866f-332aa9e42dac | -3.735 | -54.2091 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 5c3ab248-5b37-3273-96cf-0f9f99679557 | -5.7189 | -45.1547 | 2026-10-07 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 285.4 |
| fed2dc71-93a7-3ece-b9ec-938da68ff5b8 | -5.9512 | -46.3727 | 2026-10-07 19:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 82c32128-c499-37d5-b9b0-2002a223fbd1 | 1.7121 | -55.6063 | 2026-10-07 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6ae49878-0e0b-34d1-9c23-d22ed5454d30 | -6.6599 | -52.9675 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 0812e710-579d-3c45-93a4-dda51633f1e0 | -9.9589 | -43.5516 | 2026-10-07 19:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3430785d-5fce-3f45-ab54-403248dbfe1b | -3.4943 | -54.6367 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 494a2d0e-c067-3619-a91c-f1cfbeda127d | -3.3637 | -50.4701 | 2026-10-07 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| d5ad272d-2f85-3f2a-925c-4648a35b2643 | -8.6292 | -67.0111 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 9af63e71-8aeb-30b8-b9e0-0a864f329cff | -3.476 | -54.6172 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4dda4684-19b3-3f40-a4cd-60d5d878b34d | -3.6612 | -54.2715 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f4cc0b12-a9cb-317a-9eea-f05a95f48412 | -1.1278 | -54.1199 | 2026-10-07 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7739320c-009c-3dc7-896a-228ea60dd203 | -9.5468 | -64.8196 | 2026-10-07 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 1b7109e4-289b-314b-aea2-939735b11a06 | -8.5184 | -66.9954 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 939d88ca-7d77-33a5-8309-cecc79b0dd91 | -6.3353 | -43.3365 | 2026-10-07 19:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 207cf50d-7f53-3a06-b855-30ae03728455 | -8.6293 | -66.9926 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| c44c9fc7-077d-39fb-8b77-d35ffd3cc4f0 | 1.7121 | -55.6261 | 2026-10-07 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a386f4c8-fe6d-34ac-8aa0-19c2e979000a | -8.6108 | -66.993 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 750a8ecd-b92e-3f91-9a89-2cb39683ac51 | -3.328 | -50.1775 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| edf90e52-5ce3-35c9-972b-980aa820a87d | -9.4819 | -66.7836 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| fc08df61-5579-3a08-9a1c-855578dfb566 | -4.1223 | -54.0158 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6ea6d49d-d246-3871-b0e0-05b1bb33b479 | -8.5183 | -67.0139 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 169.8 |
| ec6c1d7b-84fe-3807-87cc-67c1cc06622e | -3.5494 | -54.6552 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| c9bbfff4-368a-3904-8889-6d1deb8a1327 | -3.269 | -51.0575 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 264.6 |
| a9f0fd9e-2b75-3a23-af9f-53e475aba1aa | -8.5368 | -67.0135 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.3 |
| ea9f6a5c-79d4-380d-9162-2e5db055b9cb | -8.2181 | -46.362 | 2026-10-07 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 70dfa9b2-19a2-3b6a-bf02-67e577a4f4bd | -6.0075 | -53.5122 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 40877dcb-8298-3a7e-8ca4-81f20ed7495f | -11.7335 | -43.649 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ceac3996-b274-3fd3-9894-3a651a3e907d | -5.9512 | -46.3727 | 2026-10-07 19:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 41e3ce59-589b-31ef-90ce-298741ea59d8 | -6.0074 | -53.5325 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fc8ba1f4-1392-3a3f-8f64-c32477dc1614 | -11.7143 | -43.652 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 825bfa34-3e97-38b9-83ae-87556aa32b6a | -2.9271 | -53.9295 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 58e2aba8-6604-3c8c-af2f-1026bea0e652 | -6.1781 | -52.9328 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b8a05567-9cd1-350d-927c-f70d8117f3fe | -2.7043 | -49.0533 | 2026-10-07 19:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 47a469a6-93ad-3326-aeb1-9e693cdd6397 | -11.6374 | -43.664 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 0fa79f63-9b64-3376-b405-2d17a986b72d | -3.2199 | -54.3038 | 2026-10-07 19:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6eb59a1f-3582-3a3c-9403-ccd2712cc2b6 | -3.1787 | -50.5807 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b29de924-1f73-3eb5-bad9-0d8b78acd8e7 | -9.0407 | -65.9215 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 171.7 |
| be017944-1fdd-365b-a83b-5512ee2a4227 | -4.3044 | -50.7909 | 2026-10-07 19:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 5f26a9f5-18a5-3da8-ac01-941b2ad2562f | 1.6937 | -55.6461 | 2026-10-07 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| be7d5144-bbfa-341b-ac65-a199a194d04f | -2.6859 | -49.0325 | 2026-10-07 19:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 129143e5-e1f3-3387-9ec6-13f14fe3e11a | -9.9589 | -43.5516 | 2026-10-07 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d6705341-76e0-388b-b33f-a6f6086bc6f2 | -5.7304 | -53.465 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 20f1cd8d-a1d4-31c0-aa16-18a00b0bed64 | -2.9447 | -54.1902 | 2026-10-07 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |


[Clique aqui para ver as próximas entradas](README256.md)
