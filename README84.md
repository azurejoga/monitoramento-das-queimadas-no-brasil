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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9fd75ff-d930-318c-9973-9395fabf9bb4 | -9.4683 | -62.3476 | 2025-08-31 07:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 95624195-f98c-3127-a44b-d25fbcf77a4c | -15.7102 | -48.9479 | 2025-08-31 07:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2f103a91-c431-38ec-9635-c601cc247307 | -15.7098 | -48.9702 | 2025-08-31 07:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| cd8e679d-825a-368c-a8f7-13d64e99e7d9 | -15.7294 | -48.9669 | 2025-08-31 07:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9305846b-ab6f-362f-8a6d-6fe1f6b1d05f | -11.8181 | -46.4314 | 2025-08-31 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 2e12c207-d17c-3a94-8e75-5e50ed889c03 | -9.4497 | -62.3485 | 2025-08-31 07:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d7e46eab-b55d-3976-b68c-cd35a73fcae3 | -6.5758 | -43.6885 | 2025-08-31 07:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5c7c2d21-5a8f-304f-b8aa-6a891709ac24 | -15.7298 | -48.9446 | 2025-08-31 07:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8e97a24b-8668-3259-92ca-1d7af2960365 | -6.1853 | -43.3257 | 2025-08-31 07:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 0773ad0a-5598-3d09-92d7-be395b20ed80 | -9.4432 | -60.5692 | 2025-08-31 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 689dbd66-97cb-3a7a-8ccd-6b02d3605446 | -11.8181 | -46.4314 | 2025-08-31 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| cf1ffae6-3383-399d-8772-d4b1be3c7b74 | -6.1853 | -43.3257 | 2025-08-31 07:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| eb6f2ab4-1000-387f-924b-a6f50152fecf | -15.7298 | -48.9446 | 2025-08-31 07:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1c081e55-4e73-3f24-b847-f2b6db653261 | -9.4432 | -60.5692 | 2025-08-31 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b7f43a62-fafa-3c31-ab0e-fed141e9095d | -15.7098 | -48.9702 | 2025-08-31 07:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 7bc79e14-8ff8-3d33-9ac4-5fb9c27f09cf | -15.7294 | -48.9669 | 2025-08-31 07:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b9ba5c27-b43c-304b-8d04-9dae82dce1a3 | -6.1665 | -43.3273 | 2025-08-31 07:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 73c63b23-81aa-3a4c-91f6-c6ed545947a7 | -15.7102 | -48.9479 | 2025-08-31 07:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 70428dc3-ee41-3bb3-89c4-3b6c93d72745 | -9.4497 | -62.3485 | 2025-08-31 07:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 592ed862-d5ae-3848-b6ec-0790c838afb0 | -6.1667 | -43.3039 | 2025-08-31 07:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 0646e2a6-37af-36ed-9edb-d95c70cbe080 | -6.1665 | -43.3273 | 2025-08-31 07:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 0ed7a31e-0b10-3057-a0ce-431e870dc7d0 | -11.8956 | -46.3753 | 2025-08-31 07:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 34bdcff6-d343-3569-9e53-dbc246718d0d | -15.7098 | -48.9702 | 2025-08-31 07:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7849ad6f-147a-3bc7-b752-e6237f713d27 | -9.4432 | -60.5692 | 2025-08-31 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| cb877f15-bf3e-358e-996f-23d55821ac3b | -9.4497 | -62.3485 | 2025-08-31 07:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8864db7f-0596-315c-b733-aaeee87e9a25 | -15.7102 | -48.9479 | 2025-08-31 07:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 288918b6-5a60-38cb-b379-48d879123217 | -6.4441 | -45.62 | 2025-08-31 07:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 238ee699-8e61-3688-9606-ffcc3a1ebd35 | -11.8956 | -46.3753 | 2025-08-31 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| bb9c2d6d-2a00-36b0-9649-f006c9c94695 | -15.7102 | -48.9479 | 2025-08-31 07:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a719ed46-4e8f-350a-bd52-ca1c070b493d | -6.5758 | -43.6885 | 2025-08-31 07:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6ff8f998-8986-33ed-8598-7033ede2bdf0 | -9.4497 | -62.3485 | 2025-08-31 07:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2d9ba987-c244-3742-87fa-74245928776f | -6.1667 | -43.3039 | 2025-08-31 07:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 40.9 |
| 45e015af-55bc-3964-9981-69321a9157aa | -6.1665 | -43.3273 | 2025-08-31 07:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| cddf8064-8921-3f41-a0c7-ab4dc1c2deda | -11.9147 | -46.3726 | 2025-08-31 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c3aa7dd0-3320-3f13-8e97-0fa9e575d2b0 | -15.7098 | -48.9702 | 2025-08-31 07:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e32e1148-db00-37ec-a8f1-76ac79ae0552 | -7.9266 | -62.9969 | 2025-08-31 08:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0e4759e4-0600-35d9-95a0-83658a4b9f55 | -6.1853 | -43.3257 | 2025-08-31 08:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 60113dee-bf6a-3765-ac4f-ca93c0b1d420 | -15.7098 | -48.9702 | 2025-08-31 08:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 669cd6ef-f95e-3585-9e50-b545e4fd3a04 | -11.8956 | -46.3753 | 2025-08-31 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 10cfc833-be1c-34ba-a6c8-2afaea1059b2 | -12.8621 | -48.0768 | 2025-08-31 08:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 18f6e9ac-b905-342f-99de-a1b1801af783 | -11.8959 | -46.3526 | 2025-08-31 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| d1c3269e-0449-36fd-828b-db5e1972b9b9 | -6.1665 | -43.3273 | 2025-08-31 08:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 84f8a02a-e1f9-3db7-a16b-5d03b7ac8a07 | -11.8952 | -46.398 | 2025-08-31 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 93b013b8-f923-304a-957d-b49766662e44 | -9.4497 | -62.3485 | 2025-08-31 08:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bae66dde-8c5c-37e8-98ea-268fb3e30adb | -7.9265 | -63.0158 | 2025-08-31 08:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 967f47d3-799a-3791-a2cd-b71fadabd486 | -15.7298 | -48.9446 | 2025-08-31 08:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 80a22bcb-4e91-3915-a42f-bc36c378a5ba | -7.9265 | -63.0158 | 2025-08-31 08:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 63fc01dd-089a-33be-8e3a-60d562158370 | -11.8956 | -46.3753 | 2025-08-31 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0554d5d5-0753-3733-9025-6ec0c229f28d | -7.908 | -63.0164 | 2025-08-31 08:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7788dfd6-07b7-34cb-90ca-02f2c8aef447 | -9.4497 | -62.3485 | 2025-08-31 08:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 230045df-3e6e-369a-84fa-eecaa1c37d0e | -6.1665 | -43.3273 | 2025-08-31 08:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| d5226186-0729-3fcc-8254-53bd95f8824e | -7.9266 | -62.9969 | 2025-08-31 08:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b39c8509-5eb3-3f28-9c13-6fc398a8b81b | -15.7098 | -48.9702 | 2025-08-31 08:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e6cca0b4-b306-3bd5-bd53-6aefbc127084 | -7.9265 | -63.0158 | 2025-08-31 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 7170d6cb-b345-3742-abb9-114783634a9b | -11.8956 | -46.3753 | 2025-08-31 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2ea1078c-5f4d-33d4-959d-46353429a384 | -7.9266 | -62.9969 | 2025-08-31 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 479caa2a-101c-3ab6-9327-2cf3dedab3e2 | -11.3504 | -43.637 | 2025-08-31 08:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 586a96e6-e0ad-36e9-827d-9ff846ff5796 | -15.7298 | -48.9446 | 2025-08-31 08:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| af458893-ec78-36fb-9f1a-1722e299dbc7 | -7.9265 | -63.0158 | 2025-08-31 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8be14fdc-7174-3f10-855e-acfd9a25adfd | -11.8952 | -46.398 | 2025-08-31 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| bde7d3d1-8a3e-3403-9a17-60df80fd211b | -11.8956 | -46.3753 | 2025-08-31 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| e082bac4-9923-3a0e-9b0c-678f0a0d5f4d | -15.7294 | -48.9669 | 2025-08-31 08:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 84a68700-f046-3a85-8647-3736fa35f6a5 | -11.9147 | -46.3726 | 2025-08-31 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| f18dba8f-d07f-33a0-aa6c-61de032646e2 | -15.7298 | -48.9446 | 2025-08-31 08:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1f7466d8-76d3-3c9e-a385-90a50948a647 | -7.9265 | -63.0158 | 2025-08-31 08:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| c4a29195-70d0-39ff-8174-48a092b85a6c | -20.4133 | -54.6365 | 2025-08-31 09:10:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 65f9be85-b304-32b4-9cf9-1628034575ea | -20.393 | -54.6398 | 2025-08-31 09:10:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3d083ca2-34f4-3c08-800c-17c7fc787b1f | -6.1665 | -43.3273 | 2025-08-31 09:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 19f0822f-aad8-3b75-b392-9ccf44e5daac | -6.1665 | -43.3273 | 2025-08-31 09:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 4b9575d1-1439-38c7-86df-dccc19d0895a | -23.3751 | -52.0897 | 2025-08-31 09:50:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 220.5 |
| 9d2804b2-ce52-3a6c-ba62-f6a4ab2d69b4 | -23.3751 | -52.0897 | 2025-08-31 10:00:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 413.8 |
| 05e26777-40ca-30b6-9800-354e55e7b9c8 | -11.8376 | -46.406 | 2025-08-31 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 7d15db12-e6a5-3df9-a0af-db26d441fd17 | -23.3962 | -52.0851 | 2025-08-31 10:00:00 | GOES-19 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 128.5 |
| 2856ae22-e45f-39a5-b066-b32e3f6d838f | -6.1665 | -43.3273 | 2025-08-31 10:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| e7fc4795-8f5b-37b4-ac19-0246d981d982 | -23.3962 | -52.0851 | 2025-08-31 10:10:00 | GOES-19 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 136.5 |
| 5fa92766-5918-344a-97bb-26f1cffc4851 | -23.3745 | -52.1125 | 2025-08-31 10:10:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 214.7 |
| 5517ba06-e664-3136-a7c9-aebcd7be15d9 | -23.3751 | -52.0897 | 2025-08-31 10:10:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 423.5 |
| bb0e331c-52b2-3b06-a2fd-6285a1097274 | -6.1665 | -43.3273 | 2025-08-31 10:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| ccff34c5-6599-376a-9a8a-2486686259f2 | -23.3962 | -52.0851 | 2025-08-31 10:20:00 | GOES-19 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 149.6 |
| 7020e041-33ce-3456-9f19-00a4fd1b6b37 | -23.3751 | -52.0897 | 2025-08-31 10:20:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 384.0 |
| 0c8f9e80-76da-3d97-8b3b-2cef08c5dbea | -23.3745 | -52.1125 | 2025-08-31 10:20:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 170.2 |
| 45a012e4-5e54-35db-834e-e03102f656ae | -6.1665 | -43.3273 | 2025-08-31 10:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| f2a1c14f-7a31-31e0-b02e-123474c54da9 | -11.8956 | -46.3753 | 2025-08-31 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| eb9b80d3-dab8-343b-a177-b3663bf3a97d | -23.3751 | -52.0897 | 2025-08-31 10:30:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 186.6 |
| a829bbe5-117f-3f62-8ab1-ebdea28c890b | -23.3962 | -52.0851 | 2025-08-31 10:30:00 | GOES-19 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 147.1 |
| 2b4a8b56-1b72-33a9-8970-cb1ae390198c | -12.6294 | -48.2201 | 2025-08-31 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 6a040e1b-026f-3901-a978-671335dd3266 | -23.3751 | -52.0897 | 2025-08-31 10:40:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 239.9 |
| 55008289-c8b1-31cb-9bb8-01083ae2bc57 | -6.1665 | -43.3273 | 2025-08-31 10:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 173.6 |
| b291455f-2533-3379-b808-5dba7fae5250 | -11.8956 | -46.3753 | 2025-08-31 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 309f6c27-d6fe-375f-9367-2f15721fba34 | -23.3962 | -52.0851 | 2025-08-31 10:40:00 | GOES-19 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 118.0 |
| fffae241-c786-33fa-8480-9f313de29ed3 | -6.1665 | -43.3273 | 2025-08-31 10:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 208.0 |
| f3e55d9d-cbec-352d-a2e9-1c127d227852 | -14.8208 | -46.7337 | 2025-08-31 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 3abf38fe-c21b-3114-b646-4492299e82f8 | -9.2639 | -47.0804 | 2025-08-31 10:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 47079aeb-d430-378b-a16e-88832e535409 | -23.3962 | -52.0851 | 2025-08-31 10:50:00 | GOES-19 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 8b964968-ca1f-3400-9153-4b9744f0f04c | -11.9147 | -46.3726 | 2025-08-31 10:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 18e18590-9184-3165-a112-dd2db1e12592 | -23.3751 | -52.0897 | 2025-08-31 10:50:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 119.4 |
| d4a7fe1e-9e49-317c-853f-22b4f903f726 | -12.6294 | -48.2201 | 2025-08-31 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 526f4fde-b621-35e2-9035-d8836ec1cc3a | -14.8208 | -46.7337 | 2025-08-31 11:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| de5d7d4a-1cf2-34fd-84f5-0696ccfb50b9 | -6.1665 | -43.3273 | 2025-08-31 11:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 260.5 |
| cdbc0fa4-98ca-373b-8243-d865e0e5baea | -11.8956 | -46.3753 | 2025-08-31 11:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |


[Clique aqui para ver as próximas entradas](README85.md)
