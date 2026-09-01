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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e94baf34-539c-30fb-ad2d-f76307935352 | -3.1266 | -61.2 | 2026-09-01 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8627fdf3-f855-3f27-ba0e-f4dabd5e4550 | -3.1084 | -61.2003 | 2026-09-01 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ea199801-157d-31a4-8e16-e2f6c9cfb9d3 | -7.905 | -44.2346 | 2026-09-01 17:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 05ebcccd-4661-35e9-82e3-58117f87e30a | -3.4002 | -61.3465 | 2026-09-01 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9ef36b89-0935-3781-802a-d7ce93c9a87e | -7.4803 | -63.7267 | 2026-09-01 17:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b9018027-15f4-3244-9c5c-6152481d75b1 | -7.4364 | -61.4241 | 2026-09-01 17:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| c4916167-60b7-31e9-895f-9ea2b39f3e3a | -5.9636 | -57.6704 | 2026-09-01 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 589ccaf3-ea84-3950-a331-3f23cc2a2969 | -10.7856 | -50.5066 | 2026-09-01 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 107bbb1b-4a08-3c49-bf42-604698f3c23a | -11.2767 | -50.6029 | 2026-09-01 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5d2c6eec-1db7-33b0-9c29-455dc2c37773 | -3.4002 | -61.3276 | 2026-09-01 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 474c600e-1e25-3028-9327-7515821af37e | -10.746 | -50.6386 | 2026-09-01 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| da312f25-5ee1-3b34-bf51-29a6e4ee5a5e | -3.1083 | -61.2191 | 2026-09-01 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c834cf58-7203-3c78-bcb9-184a704b3a26 | -7.566 | -61.343 | 2026-09-01 17:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7830eb60-519b-319a-843b-c023c5a249a9 | -7.8628 | -61.1405 | 2026-09-01 17:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ce097130-dfe2-3164-90c4-8d6efa5e5fb9 | -10.7271 | -50.6405 | 2026-09-01 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 7cd88aec-ff85-3ae1-a8b4-3f7ba2af0658 | -7.4364 | -61.4241 | 2026-09-01 17:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 212d7035-ab37-3dc1-9af3-3608719d2de7 | -3.1267 | -61.1622 | 2026-09-01 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| e2ccf82a-c437-3c18-9ab6-3dcbf7b4b922 | -3.1267 | -61.1811 | 2026-09-01 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 5732a520-b1c3-39fb-9cdd-ba21cb1f11bf | -3.4002 | -61.3465 | 2026-09-01 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 226f24bc-cd48-3ddb-aaa5-dbc302fe6419 | -3.4185 | -61.3273 | 2026-09-01 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 59cb5681-a8e5-324a-a798-f9aad67ccc57 | -8.5555 | -66.9574 | 2026-09-01 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b64d56d8-e4d1-381b-9544-a84308b562bc | -3.9707 | -60.0258 | 2026-09-01 17:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 13056344-8b7c-3a59-9bbd-c61fcbc46825 | -3.4185 | -61.3461 | 2026-09-01 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 5df1830f-f1ed-3371-86ca-00ee9538fa9a | -5.9636 | -57.6704 | 2026-09-01 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3b63df77-156d-3bb9-b80d-d61d5e82dcca | -6.8599 | -58.9351 | 2026-09-01 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 240b7a32-ce09-3197-be23-8578e5edb53c | -8.6852 | -62.9496 | 2026-09-01 17:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 720c3bc7-879b-374c-977b-753223d77442 | -7.5847 | -61.3042 | 2026-09-01 17:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| eb2ffc3b-9578-3b79-8e51-7a464bb238a8 | -7.5662 | -61.3049 | 2026-09-01 17:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2c751f11-10d1-372a-a0de-0adbefa9be49 | -6.6766 | -58.7299 | 2026-09-01 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 053006fb-4da7-3d11-9a1e-bfe703ebdf2e | -7.9794 | -44.3193 | 2026-09-01 17:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| cb7361cd-7c07-3c32-ab88-86361f661b3f | -8.7628 | -46.4642 | 2026-09-01 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1fa3d216-5815-378f-9f43-31eb25ffee13 | -8.2606 | -62.7391 | 2026-09-01 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a2f6db6e-bcde-3ca9-8a27-f72cbbc328b2 | -8.631 | -66.5473 | 2026-09-01 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 28f4d83d-d925-3898-a347-614ba7242110 | -11.13 | -51.59 | 2026-09-01 17:15:00 | MSG-03 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c406dc5-0f3e-311b-bc2a-16d4a29de67a | -3.84 | -44.02 | 2026-09-01 17:15:00 | MSG-03 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6247a9be-f1a4-3e2a-b376-38b95f917412 | -11.16 | -51.54 | 2026-09-01 17:15:00 | MSG-03 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e397c437-3bd8-3be0-8a3f-d4da68e84685 | -3.84 | -44.07 | 2026-09-01 17:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae3a2b5-ae19-3c14-856a-65ceca859a5e | -11.13 | -51.53 | 2026-09-01 17:15:00 | MSG-03 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44f900b6-f1b3-3c5f-a2ba-d12c4901f631 | -5.59 | -60.18 | 2026-09-01 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90014334-80a4-395a-b3f7-4d7fdd02b11a | -3.87 | -44.07 | 2026-09-01 17:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3618f10-2670-311e-a5b6-11451627bdc9 | -3.87 | -44.02 | 2026-09-01 17:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd09649-6906-344d-863d-e03ae4094c63 | -3.4185 | -61.3461 | 2026-09-01 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5501c1ae-d0c4-3dfa-9f76-a63405f08802 | -3.4002 | -61.3276 | 2026-09-01 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| cece3678-5d5d-3871-867f-069ce8348bf9 | -7.5668 | -61.2096 | 2026-09-01 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 3a11707a-4b45-3e40-8daf-65f169ecea53 | -8.2606 | -62.7391 | 2026-09-01 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 5d6ffa7b-8979-3b67-aa58-a819faeab357 | -7.4735 | -61.3846 | 2026-09-01 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 136.7 |
| b470a81f-ea36-349a-8084-a0222a7ab37c | -3.6033 | -60.5474 | 2026-09-01 17:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a99756e6-2ae8-3759-83ca-5f1dcf0fc9cd | -3.6399 | -60.5466 | 2026-09-01 17:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 316db5f9-96ff-3436-85c0-ef482b7ef561 | -3.2178 | -61.2551 | 2026-09-01 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| cd235318-e6db-3f1e-b4cf-a6fd81a0cd3a | -10.7856 | -50.5066 | 2026-09-01 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| fb4b9be4-fd70-3545-a36a-70ae7723e041 | -7.4803 | -63.7267 | 2026-09-01 17:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e136f9b0-3cca-3022-a696-677a428810e9 | -3.1267 | -61.1811 | 2026-09-01 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 3fb9702f-3cd3-359b-b77a-d879f6039fe1 | -10.8807 | -50.4751 | 2026-09-01 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 71a94b24-0ffe-36bd-bb50-d21de351cbfb | -10.746 | -50.6386 | 2026-09-01 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 190a1821-02d3-3528-9918-34b16c5648d9 | -10.7271 | -50.6405 | 2026-09-01 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 4aa586c0-14f2-3297-82ae-f112df06bcc3 | -7.5847 | -61.3042 | 2026-09-01 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| cf79cea0-d0ee-33f8-890d-3995447308cc | -7.8443 | -61.1413 | 2026-09-01 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ae53280e-55c2-3d50-9b84-722b8d87661a | -3.4185 | -61.3273 | 2026-09-01 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 583935b7-b193-302e-ba6f-5276ac9db74c | -7.5289 | -61.3825 | 2026-09-01 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 23492e1a-55b0-3c36-a98a-3126c655765d | -3.4002 | -61.3465 | 2026-09-01 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 35e4d027-2804-3c87-a87b-73bb45aacef9 | -3.6398 | -60.5656 | 2026-09-01 17:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 01f4d7dc-4420-3581-900e-26cb03e6766f | -3.1266 | -61.2 | 2026-09-01 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 52673a0d-ba5e-3ed5-9ace-9d0dcefddc1b | -7.7522 | -61.0878 | 2026-09-01 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 17d5e4c3-d322-3d93-85d3-ac70c9e95268 | -3.6216 | -60.547 | 2026-09-01 17:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| b67a3b93-b398-3d4d-9347-37d866765a84 | -3.1083 | -61.2191 | 2026-09-01 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 2c63ea61-7877-34ce-9ea3-9afd2e194e5e | -5.9636 | -57.6704 | 2026-09-01 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| fc39787e-234a-360d-b1f6-c751984c47b4 | -7.5661 | -61.3239 | 2026-09-01 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 95d6dd5a-5346-3d3a-a914-7f75e1a4e4fb | -7.4364 | -61.4241 | 2026-09-01 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| e5432743-8a98-375b-a250-394fdc3cdf51 | -3.9707 | -60.0258 | 2026-09-01 17:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| bf814a74-42fb-3986-bc86-b6d6cbd5c752 | -8.6852 | -62.9496 | 2026-09-01 17:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4553ebb1-cbb7-3498-ae34-721f5d82b6de | -7.8628 | -61.1405 | 2026-09-01 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 109d8ee0-4c33-386f-95cf-33c4dba17e9c | -3.4002 | -61.3465 | 2026-09-01 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3fd3ecc4-16e0-3c29-8e37-4a5b5fc6d001 | -7.2934 | -60.5713 | 2026-09-01 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| d4899aac-018c-34d8-9e86-fec09937e528 | -8.9873 | -65.4379 | 2026-09-01 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| aa490666-786d-30b9-b4ed-40bdebb7df09 | -3.4002 | -61.3276 | 2026-09-01 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| eca6debf-b21b-30f9-a004-049b42c7825a | -3.1267 | -61.1811 | 2026-09-01 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| da483aae-0632-3bb9-b5fb-a9fd17a50a42 | -7.566 | -61.343 | 2026-09-01 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 37f24f87-9ce5-3d6e-9eb1-898369ba242f | -7.5662 | -61.3049 | 2026-09-01 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 0cfb1c4f-c288-3b8f-a4dc-9b0c85608e3d | -7.8443 | -61.1413 | 2026-09-01 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2352d4ba-a612-3d5a-855b-236a1c7a5a4a | -8.7628 | -46.4642 | 2026-09-01 17:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e7d15026-6e2a-323d-a6de-b72cfc21bf02 | -3.4185 | -61.3461 | 2026-09-01 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 405ab157-0de7-36d9-9e00-add429a45178 | -7.4364 | -61.4241 | 2026-09-01 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 138.9 |
| bf3fe8f6-eb4e-3ba7-9a2e-c014367fe07e | -10.2743 | -64.4907 | 2026-09-01 17:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 59de4359-ecad-3352-93b2-56c59452b7f1 | -8.2606 | -62.7391 | 2026-09-01 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 756cff9b-1d81-3950-9478-2aa01821e5f7 | -7.5847 | -61.3042 | 2026-09-01 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 05855308-26ed-36bd-bf96-5758891c6ef9 | -6.6541 | -59.4452 | 2026-09-01 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 39a51044-5527-3adb-8733-d4ea6de1801d | -11.0247 | -49.6656 | 2026-09-01 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d7319658-8004-38f1-a82a-64e463b6cec8 | -5.9636 | -57.6704 | 2026-09-01 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b8f47485-f8a2-3b19-9cc6-623f21a99143 | -7.5289 | -61.3825 | 2026-09-01 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 7a442c99-4722-3c0f-8b35-fa550d8484e2 | -7.7522 | -61.0878 | 2026-09-01 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a305c450-41d5-35de-bdeb-3882bd5cf10f | -9.5238 | -65.7008 | 2026-09-01 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cdd29cfe-b2d6-3724-9536-f6c2c61fbe2f | -3.1083 | -61.2191 | 2026-09-01 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 4cc8abba-5015-3a18-b793-7321422086bf | -7.5478 | -61.3056 | 2026-09-01 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2d1e1361-d618-36a0-88bb-b929b8ccaccf | -10.1538 | -45.6982 | 2026-09-01 17:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 24d2de55-5fd4-3b23-a39c-67313652bde2 | -10.7856 | -50.5066 | 2026-09-01 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 14f58d1f-21b3-38cb-85f4-81dddbc6fbc6 | -10.2212 | -50.3303 | 2026-09-01 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6e2a1657-f086-3c60-9079-ac7492a0ea4a | -3.4185 | -61.3273 | 2026-09-01 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 588f85f6-f233-3420-b933-c7929b778ddc | -3.1084 | -61.2003 | 2026-09-01 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 57d067fe-f32c-359e-8f85-2a25e8467dbf | -10.1087 | -50.2776 | 2026-09-01 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 611e81a6-6be1-3683-bae7-a211accb07ab | -8.9242 | -63.2804 | 2026-09-01 17:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |


[Clique aqui para ver as próximas entradas](README114.md)
