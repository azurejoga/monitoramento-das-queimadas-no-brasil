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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0223457c-1be9-3c27-a43f-be8c4d6f8cda | -4.7976 | -43.5203 | 2025-09-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ed1ad5d9-f2a0-3950-b5e6-806515539bcd | -3.2176 | -54.9632 | 2025-09-25 00:40:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c72193a7-7825-3b65-93fa-aeba04ebff57 | -23.7362 | -51.9193 | 2025-09-25 00:40:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 7364af1a-7c89-391c-b9b2-b210d23c9618 | -21.0137 | -49.9988 | 2025-09-25 00:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| d9f871ad-249d-36be-8636-40512843ae70 | -20.9925 | -50.0261 | 2025-09-25 00:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 365.8 |
| d4efb597-2beb-34ac-85dc-858877cbb60b | -4.8163 | -43.5191 | 2025-09-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| eb0774d0-f3f0-3648-bf02-c47a4b0a2820 | -3.823 | -50.9765 | 2025-09-25 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cc46844b-9cb5-34df-91bb-d977e8df61ac | -21.0131 | -50.0217 | 2025-09-25 00:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.5 |
| 6f4d4688-6d36-392f-805a-dabbc287bef4 | -13.8345 | -45.6173 | 2025-09-25 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| bc616a93-a4e4-348d-845c-7946c40f333c | -4.7974 | -43.5435 | 2025-09-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 189.6 |
| bbfc5a0a-5a64-3fbc-b341-6a633206c7bf | -6.4129 | -43.0958 | 2025-09-25 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 884a3b95-a475-3647-84aa-7c683323561d | -20.9726 | -50.0077 | 2025-09-25 00:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.3 |
| 83af19b6-6302-30b7-863d-f2d848c799de | -17.9312 | -55.8548 | 2025-09-25 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 2afaad17-cb3a-3fc1-ac86-858377f6dd59 | -4.8161 | -43.5423 | 2025-09-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 179.1 |
| d7c2e31a-be4a-36d6-88b5-f2536a6b5acf | -2.9291 | -48.2966 | 2025-09-25 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7286c4a2-918d-3d27-a113-407d50f22a0b | -6.4317 | -43.0942 | 2025-09-25 00:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 235.0 |
| 3cf08bba-c7e2-3ac5-a905-3bacf622716b | -20.972 | -50.0305 | 2025-09-25 00:40:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 164.8 |
| e2936aa2-4c99-3630-a387-afb021f3e0f0 | -6.4319 | -43.0707 | 2025-09-25 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 9ed8ae6a-60f3-32fa-b80c-786fb9661243 | -6.4131 | -43.0724 | 2025-09-25 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 831fd2a9-1c15-366f-a996-351543e98dea | -2.9291 | -48.3181 | 2025-09-25 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 432b0c1d-4f21-3d0b-8d46-ee9b1721f1a2 | -20.972 | -50.0305 | 2025-09-25 00:50:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 207.8 |
| 35c91897-2757-364d-8804-0d438fdaa906 | -4.7976 | -43.5203 | 2025-09-25 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 08b31aa3-7c72-33b9-ad8e-16086bd00eee | -2.9291 | -48.2966 | 2025-09-25 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9e10039f-fbf0-36a7-9c5e-0a7329217716 | -20.9925 | -50.0261 | 2025-09-25 00:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 381.7 |
| caec0625-1870-36c2-8f4b-875c6165f012 | -6.4131 | -43.0724 | 2025-09-25 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 2da8a677-7f0b-3c7b-acc2-2613fa1efd5b | -4.8161 | -43.5423 | 2025-09-25 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| ed2bddf7-c53e-3cc8-9aac-dd5183ecec9f | -21.0137 | -49.9988 | 2025-09-25 00:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.4 |
| d5750667-7da2-39e9-a39b-af2bda7f966d | -11.6622 | -44.4107 | 2025-09-25 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 04f0653b-739a-311f-bf12-39ae4bc613d0 | -11.6814 | -44.4078 | 2025-09-25 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e4bda59f-496a-35ee-94dc-69d4223be46b | -13.8345 | -45.6173 | 2025-09-25 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 02781a18-84b1-37ca-bce5-4648a369cbde | -3.823 | -50.9765 | 2025-09-25 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| eb9b01ef-1832-380d-a832-996c8444e928 | -4.7974 | -43.5435 | 2025-09-25 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 55abc705-b702-3c19-931c-449d4e22974f | -17.9312 | -55.8548 | 2025-09-25 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 142bee79-9e3f-37c2-95e5-9992c6198ba9 | -20.9931 | -50.0032 | 2025-09-25 00:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 296.8 |
| 8a764627-45a5-32ea-b898-c8e4c4450e0f | -21.0131 | -50.0217 | 2025-09-25 00:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.0 |
| 0e657de1-865c-30e4-97c1-778ef86b48dc | -2.9291 | -48.3181 | 2025-09-25 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 00527c55-7c5b-3a36-83ca-51ab2623a92d | -20.9726 | -50.0077 | 2025-09-25 00:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| a8911eed-441d-3e3e-8299-c8b238df7630 | -6.4129 | -43.0958 | 2025-09-25 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| f5295431-4299-3711-9788-e38427a9188a | -23.7362 | -51.9193 | 2025-09-25 00:50:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 733721ae-71f2-326d-9860-c397981b4889 | -6.4317 | -43.0942 | 2025-09-25 00:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 247.4 |
| d6684c75-9c4d-3cbc-8a40-a67b78186e5f | -20.7127 | -57.8531 | 2025-09-25 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 3b39731c-0bdb-3cdf-90bb-974ae64f856a | -6.4319 | -43.0707 | 2025-09-25 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 263.9 |
| 657db553-14a9-3787-a68b-acae9c2903e2 | -20.7127 | -57.8531 | 2025-09-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 5b6e156b-efcd-35f2-a40f-4ccc14c6efe8 | -13.8345 | -45.6173 | 2025-09-25 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7ca78d9c-9099-32f4-be86-efaaf0b38c70 | -21.0131 | -50.0217 | 2025-09-25 01:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.2 |
| b0f12ba7-54cb-340f-b92e-43a7f28582fe | -2.9291 | -48.3181 | 2025-09-25 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b21cf3a5-45d8-3130-9b0e-84a05ceab47b | -21.0137 | -49.9988 | 2025-09-25 01:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 7c7c8500-36b8-3d5e-834d-5ebfd551eb7e | -6.4319 | -43.0707 | 2025-09-25 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 239.6 |
| a80f23e7-7c86-381b-98ac-ca2259d45541 | -3.823 | -50.9765 | 2025-09-25 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 44da052e-c105-3d3f-b297-d3c27c4bdd7e | -20.9931 | -50.0032 | 2025-09-25 01:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 272.1 |
| 6de5324f-ab30-341c-b2f9-43e33a716cb3 | -17.9312 | -55.8548 | 2025-09-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 3d4360a6-db8a-357d-946d-bd094df26ebe | -6.4317 | -43.0942 | 2025-09-25 01:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 67603f2c-b5aa-3d7c-a228-1b667096de04 | -6.4129 | -43.0958 | 2025-09-25 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 3438efba-339c-3f3b-b32b-6f7ac8008c95 | -17.951 | -55.8522 | 2025-09-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 6ebce2c6-b2d0-387b-83ad-c99406b25776 | -2.9291 | -48.2966 | 2025-09-25 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 34caf1f0-dac8-3303-8844-e3165a162981 | -6.4131 | -43.0724 | 2025-09-25 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 0dc6d742-6cfe-3cb3-8f18-b791c8e3b19f | -20.972 | -50.0305 | 2025-09-25 01:00:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 164.8 |
| 9d45d505-5766-316c-8bce-53ac6afc8d8e | -20.9726 | -50.0077 | 2025-09-25 01:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| 6bd4acaa-3d05-38c2-becd-09e2a341cc3c | -20.9925 | -50.0261 | 2025-09-25 01:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 328.7 |
| 45a064b5-c581-394b-b261-680e96caa05a | -20.733 | -57.8503 | 2025-09-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| cbd19bf6-1696-3490-90ff-f147b02e1c68 | -6.4317 | -43.0942 | 2025-09-25 01:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 46450a96-d8ce-31a3-b0fd-dc300e80ff8c | -20.9925 | -50.0261 | 2025-09-25 01:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 375.6 |
| 361aa3c6-9511-31f2-a0a6-1e228180166b | -4.8163 | -43.5191 | 2025-09-25 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c5cef4cc-2ede-335a-bc73-26eeeba7ab04 | -6.4131 | -43.0724 | 2025-09-25 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 8ade2904-8623-39d4-9209-cf3229d4fe24 | -21.0137 | -49.9988 | 2025-09-25 01:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 0bf59415-c80a-3bd6-9e37-f35d6e485610 | -5.0093 | -45.1565 | 2025-09-25 01:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 69e0c227-c3dd-33ae-9805-50e1142f04bc | -17.9312 | -55.8548 | 2025-09-25 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| a23f3691-9067-3f2c-b196-0d67624cfa7b | -20.7127 | -57.8531 | 2025-09-25 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 5f007430-c2ed-3b47-8aaf-7a6540d00aa7 | -20.972 | -50.0305 | 2025-09-25 01:10:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 255.7 |
| d40b21e6-12f4-303e-a3fb-9ee9f2f52423 | -20.9726 | -50.0077 | 2025-09-25 01:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.9 |
| 76a87f0b-7566-362b-a394-3484dc4b38fa | -4.8161 | -43.5423 | 2025-09-25 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 00448485-9a1f-3636-aeb9-7ee5727ed6d3 | -5.0091 | -45.1792 | 2025-09-25 01:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 137990b6-0e9b-3760-aacd-0b89636292e8 | -6.4129 | -43.0958 | 2025-09-25 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 205da4f9-c2ef-3fe6-a6e2-c79ef0a80898 | -20.9931 | -50.0032 | 2025-09-25 01:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 279.8 |
| a1afa90e-0c0f-39f1-8478-50a482c32e4d | -21.0131 | -50.0217 | 2025-09-25 01:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.8 |
| 324e4dda-c362-338a-af72-a31d3ed87ca9 | -4.7974 | -43.5435 | 2025-09-25 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 5b41cc41-3b4f-3dd6-b19c-607b0b4d8622 | -17.951 | -55.8522 | 2025-09-25 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 94b50185-7f9f-338f-9bea-15b15ec6250d | -4.7976 | -43.5203 | 2025-09-25 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8806b0ee-2ca9-3d21-8275-a4e150990dbf | -6.4319 | -43.0707 | 2025-09-25 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 53ec5b74-95cd-3a34-8101-7bc15a586fbe | -4.7976 | -43.5203 | 2025-09-25 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4f09e0d7-050f-380a-8f80-bcadb736a6ea | -6.4317 | -43.0942 | 2025-09-25 01:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 219.2 |
| fdd65e9e-f34d-3599-b7e3-bf5c904c7bd7 | -2.9291 | -48.3181 | 2025-09-25 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ac44459f-ebf4-3a88-93b1-b7e5fec53ccd | -17.951 | -55.8522 | 2025-09-25 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 498340c7-3663-34db-a683-a3da6faad7fb | -6.4129 | -43.0958 | 2025-09-25 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| cc7a7d1f-4cf9-3087-93b2-e60fdde54f6f | -4.8161 | -43.5423 | 2025-09-25 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 5d58f458-7a3e-3d76-9dd7-e217ed4f0573 | -22.0603 | -48.609 | 2025-09-25 01:20:00 | GOES-19 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2b6fe1be-5ce3-36cc-a074-6bf4d4415298 | -6.4131 | -43.0724 | 2025-09-25 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 1fe0e0a0-e397-35b5-9546-144124510908 | -17.9312 | -55.8548 | 2025-09-25 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| f2596234-788a-3f37-bc28-cd9d2ff5a3fc | -20.9726 | -50.0077 | 2025-09-25 01:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.6 |
| 87ef1582-0646-38d0-8a1b-01a2bd07a557 | -22.0395 | -48.6141 | 2025-09-25 01:20:00 | GOES-19 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b4e74565-6b79-3bc6-b0e3-e54f69a33f23 | -3.823 | -50.9765 | 2025-09-25 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8fb03d31-975a-3ee0-8c6d-e41e92ffcc56 | -4.7974 | -43.5435 | 2025-09-25 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 52386c20-fc5b-35ca-afdd-f79fa5184cee | -6.4319 | -43.0707 | 2025-09-25 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 194.7 |
| fb791979-e5a9-3518-8c42-6a1b438a2a29 | -20.972 | -50.0305 | 2025-09-25 01:20:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.8 |
| 23feaf0a-a1cb-3412-b83d-22455844029b | -20.9925 | -50.0261 | 2025-09-25 01:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 282.0 |
| a6074d90-4d30-34c5-bb47-88b95aa69527 | -20.7127 | -57.8531 | 2025-09-25 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 7c5789d4-93e9-36eb-937d-0bf8baf93ce5 | -13.8345 | -45.6173 | 2025-09-25 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d03efe1a-440d-32fc-9386-d45ee9fc8181 | -23.7004 | -51.7001 | 2025-09-25 01:20:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 140.2 |
| 8ca8b091-1ea4-3586-be1e-3917dc45d52a | -20.9931 | -50.0032 | 2025-09-25 01:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 294.3 |
| 736beb92-3135-3d55-8e77-dc8b3b4fd388 | -23.7215 | -51.6953 | 2025-09-25 01:20:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |


[Clique aqui para ver as próximas entradas](README5.md)
