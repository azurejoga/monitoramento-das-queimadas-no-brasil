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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f98888d-fc1d-3c72-acb9-85d7c571d82f | -8.9242 | -63.2804 | 2026-09-01 16:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 33e1287b-4ea9-31c1-a5fc-c90165bef58e | -6.7507 | -58.6687 | 2026-09-01 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b14a7e23-4f22-3c87-ae9a-a7b1ab1554af | -15.7937 | -47.7898 | 2026-09-01 16:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 62963fd3-c637-3eb5-9267-b4e5f17c211b | -9.1315 | -57.5703 | 2026-09-01 16:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9e58f156-2aff-3d94-a9f5-7f21dfb07867 | -8.5739 | -66.9754 | 2026-09-01 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 4fd6da92-d821-3c32-bbdd-b7cec2666812 | -13.0897 | -45.163 | 2026-09-01 16:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1385.5 |
| e2383b2f-6aa7-3306-aee2-dbd31c6e58e9 | -7.1822 | -60.6713 | 2026-09-01 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 1f2c9842-3e51-3f96-883c-28965802f224 | -6.9112 | -59.6467 | 2026-09-01 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 53670efd-0bde-313f-9dba-2595fc9496c4 | -7.5667 | -61.2287 | 2026-09-01 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4381b0e9-4fd0-3bef-a40c-cc0fb8dbb990 | -3.1449 | -61.1808 | 2026-09-01 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| aefa6600-7f11-365c-9e33-7d8a671c08bf | -7.5662 | -61.3049 | 2026-09-01 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f5617642-26d8-3ec2-99ce-a39921a0b031 | -15.1827 | -46.2336 | 2026-09-01 16:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 5f72e1ec-8d5c-3eb3-8452-3d907feca70a | -6.6541 | -59.4452 | 2026-09-01 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d3db40fe-4463-3836-8b6c-56cbc0aa4b85 | -7.2192 | -60.6507 | 2026-09-01 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f15d669e-7c3b-3d61-bd64-d0ba46b6ea7b | -3.4002 | -61.3276 | 2026-09-01 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 817b971e-1d21-350f-a3cc-9f1077250a98 | -3.1267 | -61.1622 | 2026-09-01 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| e6705b85-7428-3748-9dc7-a903e77a9c0c | -3.1083 | -61.2191 | 2026-09-01 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 58a0e134-b13b-3ece-bd73-4dd6d17c1bba | -7.4364 | -61.4241 | 2026-09-01 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 4d3c2689-f3e6-303e-9c20-c69207031903 | -7.2931 | -60.6287 | 2026-09-01 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| cba427f1-1c89-3619-aada-794cea504183 | -7.4803 | -63.7267 | 2026-09-01 16:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 160cb9ad-94f3-3f37-8d79-5521b4d01670 | -5.9636 | -57.6704 | 2026-09-01 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 447bb8cf-f9bf-3e30-8f66-84a3bfd21845 | -3.4002 | -61.3465 | 2026-09-01 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 5cde783e-3b5b-369d-8d01-4e156e880576 | -3.4185 | -61.3273 | 2026-09-01 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| dce76771-8bad-35d2-bd56-9adf3b1bdb94 | -8.3717 | -62.716 | 2026-09-01 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 7ba12a0c-3dbb-3ac0-bc64-e51e6a53c7a0 | -3.1266 | -61.2 | 2026-09-01 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 81841524-1d8a-3e6b-bf52-2fd6941265a9 | -6.8358 | -59.9379 | 2026-09-01 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4c658bca-f6b8-3ef6-b4be-e75e11e2b908 | -3.1083 | -61.238 | 2026-09-01 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 284e1ad6-8bef-358d-89c0-93992904e40e | -9.6941 | -65.077 | 2026-09-01 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f8488ad9-b16a-3627-a191-5c998585e742 | -6.6938 | -58.942 | 2026-09-01 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7c6e44f2-d66a-32b4-9a68-7bf3d460a646 | -3.4392 | -60.3985 | 2026-09-01 16:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8f21273d-871e-313d-9df2-73be2227d155 | -3.9707 | -60.0258 | 2026-09-01 16:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b987d6cc-d1fe-3f9b-b004-3832dbe810b6 | -7.5289 | -61.3825 | 2026-09-01 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 7b1e7897-0c20-3e8f-bcc7-cf7bc080d79b | -7.5475 | -61.3627 | 2026-09-01 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1a950caf-e653-36ae-91f9-42081d630b63 | -9.694 | -65.0958 | 2026-09-01 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9b8cb83a-a1af-3eaf-a05c-a6ca55c36ad9 | -12.1457 | -44.196 | 2026-09-01 16:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e54d948e-166e-364a-922a-fbec0133280d | -8.9242 | -63.2804 | 2026-09-01 16:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 44b1243e-addd-3a36-8b73-c903f67cbb75 | -6.4868 | -45.0738 | 2026-09-01 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| dd65f4c4-043c-30cd-a36e-250094c6991b | -3.4185 | -61.3461 | 2026-09-01 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c8fa4eac-1e55-379d-b662-d236e6069d65 | -3.0718 | -61.2197 | 2026-09-01 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 89b370db-f28c-393c-9e30-6a1188331b84 | -7.5667 | -61.2287 | 2026-09-01 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a7b94668-b1d7-3b49-988d-69da16690422 | -3.1267 | -61.1811 | 2026-09-01 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 3b270556-2090-3d72-bd42-ce2c3caba046 | -7.1822 | -60.6713 | 2026-09-01 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 7e98ff82-da76-32d0-baa9-cb6360e85f82 | -3.79 | -59.3031 | 2026-09-01 16:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8af1f0fd-6a17-38ba-aab0-6bfc23d49dd7 | -9.5238 | -65.7008 | 2026-09-01 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| fad2c39e-3adb-363b-a37b-ab679e15ddef | -8.5555 | -66.9574 | 2026-09-01 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 296e6eb8-57fc-3131-86b6-0c0032c4ae0c | -7.5526 | -60.4651 | 2026-09-01 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 00d2afa6-d05d-329a-9fe2-8fd5a85ed3d7 | -3.6399 | -60.5466 | 2026-09-01 16:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| cbc41a13-c998-39de-914a-21d27c5defb6 | -7.5668 | -61.2096 | 2026-09-01 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| bf9df189-1931-3d7a-8428-205cb6aeebb9 | -7.5659 | -61.362 | 2026-09-01 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 124.8 |
| de9b0e12-0e6c-39bf-8ec1-386806a8b0f3 | -7.3635 | -73.2632 | 2026-09-01 16:40:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 281f58f1-5356-39d4-b1c2-afd8058ea20c | -7.5104 | -61.3832 | 2026-09-01 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1e966569-f78c-333d-b21d-c219ececcd94 | -3.218 | -61.1607 | 2026-09-01 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 0fc57c64-5328-3cbb-bc94-304ea2089edd | -7.4803 | -63.7267 | 2026-09-01 16:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 87be2d2a-4ca9-34a8-9d6e-e2af8bccd630 | -7.5668 | -61.2096 | 2026-09-01 16:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3979e693-6c10-360b-9283-a2a7624cea1f | -3.4185 | -61.3461 | 2026-09-01 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5332feb6-f3aa-3072-acec-a32697eb41b5 | -10.8818 | -45.3534 | 2026-09-01 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 2cb0201d-2cae-3461-9c98-c047a1a896e4 | -7.2192 | -60.6507 | 2026-09-01 16:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 44fabb1c-f7d9-3f54-b9a5-0c75b26d8485 | -6.7507 | -58.6687 | 2026-09-01 16:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7970ddb5-f3d7-3415-a76e-d1b33b886a94 | -6.6541 | -59.4452 | 2026-09-01 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 7b0118f4-de3b-3400-8346-83ef0a845687 | -7.5667 | -61.2287 | 2026-09-01 16:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 757f6a71-a781-37ac-abd6-c87c6d7f3179 | -3.6216 | -60.547 | 2026-09-01 16:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| c8aa10a7-c338-375d-b082-e7d2a6bfa0fd | -5.9636 | -57.6704 | 2026-09-01 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 326c5ccd-35cc-3c61-a6e9-08aacd76dfbf | -11.2767 | -50.6029 | 2026-09-01 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 53656d24-3f82-3fbe-8520-af4c2fba0cb0 | -3.4002 | -61.3465 | 2026-09-01 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d534052f-bde6-3e87-bb6a-ace6db243ed0 | -7.9172 | -61.329 | 2026-09-01 16:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| cc447b9b-f832-3b4d-9859-235c5fdf5297 | -7.3119 | -60.5706 | 2026-09-01 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 70967250-b477-3606-9f4d-57ff2620a37a | -3.1267 | -61.1811 | 2026-09-01 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 6359c6cd-60de-37ab-8aca-4fcfee23e936 | -8.3718 | -62.697 | 2026-09-01 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 78aef723-c521-326b-b6e1-db1c5a151b72 | -8.9242 | -63.2804 | 2026-09-01 16:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e467e182-27a3-35b6-b487-be3146faef31 | -11.2577 | -50.605 | 2026-09-01 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 888323b0-379b-363b-b066-080fe25f9d83 | -7.4364 | -61.4241 | 2026-09-01 16:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 98a7007e-d5ac-3591-9ce6-080f65648912 | -15.1827 | -46.2336 | 2026-09-01 16:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 123.7 |
| cb6e7ee5-7223-36b7-9440-d3ba0881495c | -6.6938 | -58.942 | 2026-09-01 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3d63c420-8388-355d-aeb9-17706fe4acda | -9.4349 | -45.625 | 2026-09-01 16:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0342ff00-28fa-35dc-b4ac-0d8dc29eb2ce | -3.1266 | -61.2 | 2026-09-01 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 11e0d554-5cbe-3349-ae0b-712358442303 | -3.4002 | -61.3276 | 2026-09-01 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ceb1631a-9739-3194-9440-ed721fc3adbb | -3.4185 | -61.3273 | 2026-09-01 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| cf88d116-9d47-358f-b331-839c2fa146e0 | -3.9707 | -60.0258 | 2026-09-01 16:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3189d32c-29bb-31c7-9554-8c6b5e1f4c6a | -8.3717 | -62.716 | 2026-09-01 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6e4a8641-249a-30df-9b38-c59dc8bc63df | -3.1083 | -61.2191 | 2026-09-01 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 61b4e810-9362-31e1-9782-b33bca9645ab | -9.694 | -65.0958 | 2026-09-01 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| cd27df60-5f84-322d-aafd-8fd6893dd9d1 | -3.1084 | -61.2003 | 2026-09-01 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1b7d04ce-e589-3973-a162-7c0e8acd8774 | -6.7507 | -58.6687 | 2026-09-01 17:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c6c2a3c2-0f17-38ec-9531-660867aac84c | -8.3717 | -62.716 | 2026-09-01 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d507dae7-c33d-38a5-89ab-3cc982355fa7 | -3.1083 | -61.2191 | 2026-09-01 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 069eccab-c15d-3716-8a16-530c6d12004c | -10.1087 | -50.2776 | 2026-09-01 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 392f0b3f-c477-3e04-ba48-580428ce6abe | -3.4002 | -61.3276 | 2026-09-01 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b7ea80d2-fc27-38a5-8f99-a46b87fd10c1 | -8.631 | -66.5473 | 2026-09-01 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3e7f44f1-77ae-3878-bc52-a48c71d794d2 | -3.4185 | -61.3461 | 2026-09-01 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d77aafa2-931f-317d-b249-a4d4c225e055 | -8.9242 | -63.2804 | 2026-09-01 17:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 68260d90-231a-38db-a37a-20975bba3094 | -7.4735 | -61.3846 | 2026-09-01 17:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| bb92b89a-e9a5-3d9f-a34c-de5e58e6352d | -8.5555 | -66.9574 | 2026-09-01 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 92ce1fa1-4f2d-30ba-99e9-3552af2c3e9e | -3.4185 | -61.3273 | 2026-09-01 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8150665a-07bd-39e8-bcc5-792aa1e2a6d7 | -10.1321 | -45.8825 | 2026-09-01 17:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 95bda704-e452-3be3-be2b-dcd82a665fff | -8.4089 | -62.6767 | 2026-09-01 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2479b5ae-5007-3606-bf43-7cf8134c992a | -3.9707 | -60.0258 | 2026-09-01 17:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3897390b-56a0-358a-8cf8-4c883f7859ff | -3.1998 | -61.161 | 2026-09-01 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b0bddbb1-d4aa-3bf6-84e7-547e989740bd | -6.1795 | -45.9097 | 2026-09-01 17:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3b666829-c137-3e34-8426-d0352c9acd98 | -3.1267 | -61.1811 | 2026-09-01 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| db129dd7-7c2e-3be9-bceb-74e1e0ee09d5 | -8.2606 | -62.7391 | 2026-09-01 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |


[Clique aqui para ver as próximas entradas](README113.md)
