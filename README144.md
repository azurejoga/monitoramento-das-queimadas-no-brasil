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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57fa79a5-ff85-37d3-8d07-98f369dd5cd5 | -9.859 | -46.4114 | 2026-09-22 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| b2cbae79-bb42-34e8-904c-69da8b5e9b77 | -10.7446 | -50.7451 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 89abfb7c-a74c-314c-92de-7b82e92db90b | -11.137 | -51.1071 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.6 |
| fe67de42-e8b2-30e8-9940-dc7d86271df9 | -5.5846 | -45.5703 | 2026-09-22 14:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 75158875-4c01-36e3-b795-30069d181c38 | -3.3001 | -57.8487 | 2026-09-22 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| fdd17263-0a7a-33b1-a055-6358686768c9 | -3.1278 | -60.6889 | 2026-09-22 14:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 999f14ed-93e6-3a56-9454-e320258c6616 | -5.7304 | -53.465 | 2026-09-22 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a327dc48-f132-38f8-a52b-8bb2e39dd338 | 3.859 | -60.6371 | 2026-09-22 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a644a731-ae3b-3e8f-a695-0ef632ab1798 | -7.1553 | -47.4971 | 2026-09-22 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e4e95c28-8b6c-3e8e-94e3-ef06b64e6dd3 | 4.0579 | -61.4095 | 2026-09-22 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 82bce2c1-770a-357c-a79c-1796221aacca | -14.6492 | -45.66 | 2026-09-22 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 287.5 |
| bd65fa6b-7eb8-3a8e-a76a-1619ccfd403b | -7.0046 | -45.7544 | 2026-09-22 14:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e99c6ed5-dfe1-3c5c-8980-c36f32c599f6 | -12.283 | -50.7011 | 2026-09-22 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ae8fd04b-83ea-39fe-bc46-a59995ee5def | -3.6452 | -58.7685 | 2026-09-22 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c0a24301-b34b-3991-8186-81af0a738228 | -8.3952 | -47.2784 | 2026-09-22 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 75df3288-c6b7-3439-8cd8-1974f63edfee | -6.6704 | -47.3811 | 2026-09-22 14:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ba18ba87-d1b3-32ef-92c4-2614fb6e1090 | -5.8314 | -52.1918 | 2026-09-22 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 86a2049d-3c0c-3510-9dd1-88c53e040978 | -5.6411 | -43.3687 | 2026-09-22 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 542f0523-0dad-3759-837a-dc4fa14f9394 | -6.6834 | -52.3296 | 2026-09-22 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 28ee747a-bb8d-3b30-b104-1eb8fbd99ec7 | -8.7703 | -45.8793 | 2026-09-22 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| b4a7ad80-4786-30da-9924-244c08b506d8 | -4.2042 | -56.3412 | 2026-09-22 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| da956ce9-317a-3087-b565-6631b4335662 | -6.3015 | -59.9387 | 2026-09-22 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5063f1ae-4c7e-338b-85bc-ffe5339e7c30 | -5.4179 | -60.2166 | 2026-09-22 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2702ba2f-6436-3a1e-894c-96f73048fbea | -5.3646 | -56.0249 | 2026-09-22 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 590faf39-a4a0-3662-865a-676c98bac2eb | -2.9709 | -57.7197 | 2026-09-22 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a5380f70-5404-3424-a23f-f5f1bc70c029 | -10.7997 | -50.8668 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| db9276ca-c12b-3024-a3eb-c759e069c239 | -12.3484 | -50.1779 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 434.1 |
| 63082682-6e26-3eb0-a40d-88f2388d7900 | -7.146 | -48.4352 | 2026-09-22 14:50:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 6827b496-df06-3392-a920-1fe188993ca6 | -6.7464 | -59.4223 | 2026-09-22 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| aaec8931-9c6a-3fda-8420-e0db76acc17c | -10.7248 | -50.8109 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a38a2060-6ee4-373c-a95d-2da7c164e216 | -3.4272 | -58.1945 | 2026-09-22 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1177eb6f-9cff-30b3-897e-1a3377256758 | 1.9793 | -50.8609 | 2026-09-22 14:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c110c1ba-1451-3df9-aa09-ed5cdbe0467e | -5.7615 | -57.5807 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6271a722-4704-393c-af78-2290666259b5 | -7.9172 | -61.329 | 2026-09-22 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b45f60a5-b0e5-3aec-84fd-b7fb74772f73 | -5.9333 | -53.5362 | 2026-09-22 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ddd645cd-7dd5-3027-97d8-6f36bbff514e | -6.0925 | -57.6847 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 350.4 |
| 213a1f4a-05ba-314f-8b7d-e08e5a696bb3 | -3.0352 | -61.2581 | 2026-09-22 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 0be27510-02e2-314e-958a-5e4e8ea25505 | -8.1496 | -54.8049 | 2026-09-22 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9b88e86b-8fb5-3d19-bfb9-a8d4cfb57b5d | -6.3196 | -59.9956 | 2026-09-22 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| cc1163ff-9808-3eb3-835a-174cc47616ce | -3.2211 | -53.9623 | 2026-09-22 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7f8dfc45-095d-3415-914a-b2a2286ef6ae | -9.3797 | -48.3232 | 2026-09-22 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 2a2a9725-5244-3fe9-a7cb-7e082949576a | -3.8096 | -58.8994 | 2026-09-22 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 489af155-6292-30f6-88c7-9e061affce9b | -3.4599 | -59.5209 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0c95cfac-c755-3a16-81d2-74a14cc3d559 | -3.3645 | -61.0257 | 2026-09-22 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| b8af3bd8-17e5-36bc-b331-a58e0743ffde | -3.4634 | -58.329 | 2026-09-22 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 65f1299a-7711-3a44-9ee3-6d698e9a62e7 | -8.4799 | -57.6085 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| bcc7e85f-d66d-3946-bf5e-0cb09b2ec7f8 | -12.2827 | -50.7226 | 2026-09-22 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| c6432e51-2f9e-3763-a76c-7c505c4476ab | -3.4781 | -59.5396 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 132.2 |
| e25fe70f-7927-3a14-850f-d2ec281f00d7 | -7.6942 | -61.5473 | 2026-09-22 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 10c5295f-135a-325b-9cfd-0ac9ebe4224f | -6.4302 | -59.9724 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| bb1444e4-2faf-3974-9179-bfb1a2c12daa | -3.3001 | -57.8487 | 2026-09-22 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 62b768fc-c3cd-3ff6-b7fb-fab71c10cd9f | -12.3102 | -50.1826 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| cc56e8a8-e058-3e6a-aeb8-e61425cf9250 | -5.9152 | -59.933 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 28d46267-0396-3547-97dc-0efb6821a957 | -3.0352 | -61.2581 | 2026-09-22 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 128f6759-ed06-3819-a24c-c59aa94fc87f | -3.7857 | -60.7146 | 2026-09-22 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 21573c0c-cc0c-378e-b3c4-4e93871331e4 | -10.8195 | -50.801 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 608fdfc0-7b63-337c-8bf0-764217ce18c5 | -6.3199 | -59.9381 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e669b467-3c8d-3df0-b2f7-684a982a3912 | -2.9997 | -60.8047 | 2026-09-22 15:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7e8b5207-f544-3426-a433-b2ef988c1832 | -6.9411 | -42.9306 | 2026-09-22 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| b7b2f3a4-80a4-37a3-b499-042c2cab8923 | -7.0661 | -45.2521 | 2026-09-22 15:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 21aa2768-4ccc-3c87-841e-821786e619d3 | -6.7354 | -55.3074 | 2026-09-22 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1eec9dc4-de27-306c-9018-d0bed92370dd | -11.44 | -47.3579 | 2026-09-22 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 588c2770-5c44-38ae-bb0e-69f006ead993 | -6.9762 | -52.8669 | 2026-09-22 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 75203659-09ad-325d-a939-0b1da07bb4ff | -2.9709 | -57.7197 | 2026-09-22 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 195f77a5-c145-31b7-b8af-80cf4de7fcbb | -5.4179 | -60.2166 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| aad46c97-7fb2-34ca-978c-def4376af4ec | 3.9354 | -59.6063 | 2026-09-22 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 76adfbb7-9ff8-32b5-bdfd-f45e4d374911 | -6.3196 | -59.9956 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 11ed5c34-cc48-3089-93b9-750cc735a750 | -12.6681 | -45.0455 | 2026-09-22 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 5d6f2c64-e0a8-336c-b458-c498b9d6df60 | -11.1563 | -51.0839 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| ae50fde8-ab90-357b-890b-d85e4ba628f6 | 3.9356 | -59.568 | 2026-09-22 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a150da10-48c2-3e80-813c-87251052c70e | -6.6706 | -47.3591 | 2026-09-22 15:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 8febea1e-5a1e-3ca0-ac2b-fc32edd67019 | -3.3138 | -59.4281 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| bdc305f6-8036-342c-a78c-3a65218fc21c | 3.8953 | -60.7313 | 2026-09-22 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 078601d1-928a-36fe-af8d-26d3dab55d80 | -7.0619 | -47.4826 | 2026-09-22 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e750d457-0690-358a-a334-c9144b4e0b09 | -10.6878 | -50.751 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| d89f245a-b9b8-3324-9c3a-2a4cfa622cf1 | -7.7661 | -44.823 | 2026-09-22 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 2471c58e-a2d6-3d82-ab43-e79cddb2332e | 2.6715 | -60.6012 | 2026-09-22 15:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ead6f779-691b-3fd5-8a28-e058957aea7c | -6.3842 | -55.265 | 2026-09-22 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 05f574fe-c32f-3049-bae5-9ac1f76e8c67 | -3.405 | -59.522 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 205.1 |
| d0222248-4b2b-3fbd-879a-ae181d2f370b | -12.329 | -50.2018 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 71b2f370-2d81-359c-9f7c-c11b4cff28ba | 3.8592 | -60.5992 | 2026-09-22 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 51660c14-29cb-3d85-b0ea-09e9f7189ff1 | 4.0595 | -60.8795 | 2026-09-22 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6ab1f438-c269-397c-a10f-07304ff126ad | -4.2042 | -56.3412 | 2026-09-22 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| e8ab8ef5-0f78-3892-9899-e8f98c96645f | -11.156 | -51.1051 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| ead04bd4-a793-337d-8f7b-69d2957bccad | 3.0563 | -60.0629 | 2026-09-22 15:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c05bea35-706b-306e-a925-1f78421cf632 | -12.4008 | -47.0481 | 2026-09-22 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 49eebf29-d9de-364c-9932-f68a4e930abf | -7.0352 | -44.6396 | 2026-09-22 15:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 9c3135b1-8e04-3f55-a046-b44f0ad616a2 | -6.3013 | -59.9771 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 70bd93e3-ab11-3fcb-bc75-7aa3182c0ac9 | -12.0642 | -50.0617 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6bbd3661-f44b-3105-bb8d-517577cedc1e | -7.1273 | -48.4366 | 2026-09-22 15:00:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 40264e30-64db-3411-9c16-6af3aa394564 | -12.3478 | -50.221 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 2f24e66c-9090-3cf9-bae5-12516b3a8b0c | -3.3309 | -59.8673 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c73fd0cd-762e-37f2-b555-71552b594c8e | -10.7999 | -50.8455 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 8caad2dc-a35a-3ed0-98e4-57a71c74b6bc | -6.3195 | -60.0147 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0098c5e9-1c55-3bab-9409-9d305d196a0e | -3.6452 | -58.7685 | 2026-09-22 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 40456f0d-74c9-3363-b4d1-d8e9252831e9 | -7.5704 | -57.6766 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 196d68d6-3013-3e73-b1d5-da9cbd5cdecd | -7.146 | -48.4352 | 2026-09-22 15:00:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 4e6100e8-3dba-3a2d-be7f-f96e21d85151 | -10.4105 | -50.2897 | 2026-09-22 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| ad63a9e3-30a6-38bf-80bb-c3edee5aed2b | -3.7674 | -60.7149 | 2026-09-22 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 64a22ea2-d848-3c6c-a991-9e7c55a3975f | 3.9168 | -59.7023 | 2026-09-22 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |


[Clique aqui para ver as próximas entradas](README145.md)
