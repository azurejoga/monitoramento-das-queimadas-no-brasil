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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb207216-bd8c-3f8b-a1d8-05015d43c774 | -2.70924 | -53.99102 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a10698bc-b44e-39a1-8c21-52bd989a77db | -2.33054 | -54.38019 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4ac6096-0813-3cec-b829-4db394b9da11 | -2.32999 | -54.38347 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db64deda-e775-3593-abd6-aa702b7e82db | -2.32682 | -54.37568 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f8d6bf8-2dca-3a3d-a14a-7f7ac98618bc | -2.32629 | -54.37896 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 879be370-e3f5-3c8a-96b2-4819eb350ce1 | -2.32576 | -54.38225 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9355b000-3fc5-3c5d-b0d3-85af182b0766 | -2.32525 | -54.37935 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2663672b-5cbd-382a-92bd-0cc675cd8ceb | -2.3247 | -54.38263 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a068849-1c50-3f40-b199-4b934a622476 | -3.27018 | -54.18009 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6431c41b-0463-345d-aac1-46485a71f4be | -3.26967 | -54.18312 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bef09172-fdcd-35b3-9ffa-4f4b0ea69edd | -3.15757 | -54.92213 | 2024-10-19 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72c24520-f083-3de1-a4c3-9f04fae489b5 | -3.11322 | -54.98708 | 2024-10-19 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2fb8a68-a95f-35b3-82be-901d232e49be | -2.9522 | -54.14515 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22130b8f-0c7b-3db9-9d9b-1cff85df2ae4 | -2.95169 | -54.14822 | 2024-10-19 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24ca1c6b-1fc6-3850-9528-a052e001d062 | -2.94816 | -53.70246 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32ca1cfc-c77d-3022-9767-e6a5d4ff6e11 | -2.94769 | -53.70534 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c768ca9-b0eb-395e-ac8d-2ec930d9040f | -2.94722 | -53.70822 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f7c843-cea5-35c1-92b0-5dbc12388958 | -2.94362 | -53.6988 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 629aa13c-2f13-3897-8bc6-2d79a8475470 | -2.94221 | -53.70742 | 2024-10-19 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9776a6ef-48eb-3f38-87e1-ae63b1860fc6 | -3.68633 | -54.56524 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b690c40-d5e3-3f6a-afa7-bb71cda60e49 | -3.68629 | -54.21141 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd08c463-3fdd-34f4-8c94-bee168dea48a | -3.68577 | -54.21448 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03f39afb-fefc-36a4-a776-f7b27f44510f | -3.68116 | -54.564 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3be243aa-63b1-3060-990a-ca13407ce988 | -3.62487 | -54.67271 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d9b7cb0-8192-3829-a45a-6fe9a163279e | -4.05638 | -53.87886 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26e4f369-66f2-37a9-8d16-d71c37852620 | -4.0514 | -53.87804 | 2024-10-19 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c7fb77b-249d-39b1-9e42-289e4d0bfea1 | -3.63017 | -54.67348 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cfd48d7-87c8-3e8f-81ef-bb7369d0158e | -3.62543 | -54.6694 | 2024-10-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a284eaae-a264-3288-8af9-ad568f15f6b9 | -4.14298 | -56.10172 | 2024-10-19 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b0dfb90-fd22-372e-a736-536762b7570b | -3.06276 | -59.19096 | 2024-10-19 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6d50f7bd-cc2b-3470-91ed-583e6b8eb284 | -3.98681 | -59.22149 | 2024-10-19 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f4520e2c-042e-362f-9d3e-e326c40cfe9d | -2.9489 | -52.9174 | 2024-10-19 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| cb1fac5d-1603-3856-a902-e6fc9e11d0b7 | -2.9489 | -52.897 | 2024-10-19 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9f956d5c-5be1-36da-87aa-ff0fe378f6fc | -2.9673 | -52.9169 | 2024-10-19 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6c097921-ce03-3b7b-b2e4-2b647ec6595b | -2.9673 | -52.8966 | 2024-10-19 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8ada1add-1bea-3f65-8955-5743b9fb014e | -3.4202 | -50.2164 | 2024-10-19 04:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4b5d6a9c-c2e2-3d50-ab1d-538bf86de082 | -3.4387 | -50.2158 | 2024-10-19 04:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 11b0f66a-17d2-3be2-9bfe-69474210d4ad | -4.706 | -45.8493 | 2024-10-19 04:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 256ed7dc-564e-3429-9678-0ab1727a8f70 | -4.7061 | -45.8269 | 2024-10-19 04:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 4cc473e6-64ae-39b5-9c14-fb1600caee8a | -5.5716 | -44.8927 | 2024-10-19 04:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c8196be9-eb8e-3489-8e9a-d4bf393d3f46 | -9.0344 | -67.4641 | 2024-10-19 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 31fce12b-b6dd-3b6e-888e-bb6de07ff7bb | -9.0345 | -67.4455 | 2024-10-19 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a5dec7db-8ce4-3fdb-af03-b1796fdee364 | -9.053 | -67.4636 | 2024-10-19 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 80471e02-85f3-34a6-9ae1-f66d65a20534 | -9.053 | -67.4451 | 2024-10-19 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c94e06e1-f11e-35f2-955c-54031b6b80b8 | -12.496 | -63.2832 | 2024-10-19 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d0a4ea0d-652d-3af5-98a1-89dfaef31fd4 | -12.5147 | -63.3014 | 2024-10-19 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 06d28a8a-dbb4-30e1-b085-ae098740a3f8 | -12.5149 | -63.2822 | 2024-10-19 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 97855607-8bac-3d95-9e07-c3d27c626a96 | -12.5336 | -63.3003 | 2024-10-19 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| fbd3401f-f448-3190-90bc-3ed6696daf11 | -12.5338 | -63.2812 | 2024-10-19 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| be766c2d-a73b-3ecf-98fa-d63013af8ec5 | -9.29085 | -43.27384 | 2024-10-19 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a7050de-ed64-3fe3-a548-d0474850237e | -9.17415 | -43.14963 | 2024-10-19 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33b624c0-ba9a-3029-8b1c-bdb40c575201 | -7.85114 | -46.248 | 2024-10-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3f1a002-5bce-329e-b86e-8f1a53e84cd9 | -7.71928 | -47.58082 | 2024-10-19 04:27:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95fef858-b49a-3f3e-ad74-42455260f556 | -6.99907 | -47.78212 | 2024-10-19 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1403551f-be00-371a-9520-287cf270470b | -6.63225 | -47.35223 | 2024-10-19 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ce474a8-d7fa-3c17-b9f9-86a21e58e286 | -6.62891 | -47.3517 | 2024-10-19 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 903bda4b-abc2-3471-8efe-1d46b778319f | -6.61773 | -47.37888 | 2024-10-19 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24230d4a-b680-3f19-b005-fc11b069e4c2 | -6.61496 | -47.37483 | 2024-10-19 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e43a24f6-da2b-3b65-ad95-f9fac21aee98 | -6.61439 | -47.37835 | 2024-10-19 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1c8c524f-f2ee-3d84-b8e4-0a55ae24c131 | -13.05915 | -48.84288 | 2024-10-19 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6597a074-a54e-3ec5-829b-5fcb561b9218 | -13.00895 | -48.88271 | 2024-10-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4a4337ce-e41f-3ac1-8848-97b401a1e474 | -13.00837 | -48.8863 | 2024-10-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 831753e5-74d0-340d-8395-7b2edb0080c3 | -13.00779 | -48.8899 | 2024-10-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 841fdcd3-4073-30ca-b36a-028e005a4e2a | -13.00722 | -48.89351 | 2024-10-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e886c427-027e-3efa-95b3-bd07b5226d58 | -13.00503 | -48.88574 | 2024-10-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92928f33-64ca-3bab-8fd9-5f60a1ef5858 | -13.00446 | -48.88934 | 2024-10-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adbb2bc7-117e-345b-8a63-606cc61d8759 | -13.00112 | -48.88879 | 2024-10-19 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c159c10-976f-35ad-b568-8eafcd433b39 | -8.57282 | -49.21863 | 2024-10-19 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73c3b3f0-8213-31af-ab31-5e6af80066fd | -8.57219 | -49.22253 | 2024-10-19 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcbe9e8a-b9f6-3e11-b608-78c1e0293b95 | -7.98492 | -50.17467 | 2024-10-19 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61410dbb-03c1-381f-a38f-e7af08d549c7 | -7.98421 | -50.17903 | 2024-10-19 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44b76bc7-78cf-3108-9439-2fd55f14026c | -8.9173 | -51.62358 | 2024-10-19 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e7bc6f5-0144-3c7a-af6c-4738748ee23d | -10.1629 | -54.89837 | 2024-10-19 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7b97a8f-736c-36a9-a3b4-12c3ed364b67 | -10.15808 | -54.89756 | 2024-10-19 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0f4d2b7f-64fc-3113-8e2d-c5bf4ae0f894 | -11.91698 | -55.26959 | 2024-10-19 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa9a0cfe-67bb-3bfe-af66-9d9fb9b31386 | -11.91656 | -55.27172 | 2024-10-19 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5d1a2f7-e8cb-3bbe-9758-e34012d6f7d8 | -12.50463 | -54.43198 | 2024-10-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e00b4977-e878-3875-85bd-908dac405805 | -12.50181 | -54.43327 | 2024-10-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a174d87b-3809-3c8e-ac39-4963ae50f63e | -12.50016 | -54.43115 | 2024-10-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87bb3e1c-6e92-3dd8-85ab-ec5bed62ca73 | -12.49931 | -54.43569 | 2024-10-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4431bb2-523e-3e19-be52-334b7e9596b2 | -12.47039 | -54.47958 | 2024-10-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d0282fa-87fe-3ae4-bf16-02250586a518 | -11.91288 | -56.19341 | 2024-10-19 04:27:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9297540d-019b-383f-afd4-0fe688544eb1 | -11.91231 | -56.19645 | 2024-10-19 04:27:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b202547d-6d60-39d1-861b-5bf2b0a7b8e4 | -11.90724 | -56.19545 | 2024-10-19 04:27:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8df3a1b-4677-33ef-9a31-c7175b114722 | -9.35569 | -57.60446 | 2024-10-19 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6028c26c-fb0a-3ed8-8874-d9f59c5a1159 | -11.8211 | -57.36482 | 2024-10-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8a9c5f3-f78d-3086-9eee-8cf1206a91dd | -11.8006 | -57.47209 | 2024-10-19 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc52540-12bc-3829-990c-17d77bfdb23c | -11.8002 | -57.47167 | 2024-10-19 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc971d9b-4ce2-3378-954d-ba721a0b9a8c | -17.62994 | -41.20547 | 2024-10-19 04:29:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 827b86e0-d5d7-313f-8fbb-d2c749e4a9d1 | -18.60661 | -41.60614 | 2024-10-19 04:29:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5c2c67e6-fa02-3cc3-9021-a998ddc066da | -18.05968 | -41.70549 | 2024-10-19 04:29:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e87c8ca5-e333-3ecb-b777-5abd64238b63 | -18.05911 | -41.71038 | 2024-10-19 04:29:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d3a985cb-10e3-32b4-a9c2-c711af5de380 | -18.05511 | -41.7046 | 2024-10-19 04:29:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4bdc1483-9367-3efa-8587-019c3ed3f212 | -17.99827 | -42.59346 | 2024-10-19 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 33708eda-5e41-3972-a0c1-1b40407d29d6 | -17.9977 | -42.59801 | 2024-10-19 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 461a1ffe-b7e0-3a6b-a3e7-d5a0af08538e | -17.99336 | -42.59746 | 2024-10-19 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b469b1d5-ee40-3a62-ac0a-5a3c36a8b6cb | -17.97408 | -42.02657 | 2024-10-19 04:29:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 111e7ee2-175f-3a3a-b7c9-ede27b1d6895 | -17.97344 | -42.03181 | 2024-10-19 04:29:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ecb02da3-cbf1-34aa-8dd8-e4bc98d07ff9 | -17.3983 | -41.42947 | 2024-10-19 04:29:00 | NOAA-21 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d603e3f3-3974-3395-8045-74fcc9cc64d5 | -17.39368 | -41.42863 | 2024-10-19 04:29:00 | NOAA-21 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
