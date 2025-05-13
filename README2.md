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
| e3b592e5-d2f5-35bc-a58b-c3e13340d649 | -12.1499 | -48.003899 | 2025-05-13 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97a6feda-eaae-3bf6-99de-1e913368eea3 | -5.80056 | -43.62171 | 2025-05-13 00:16:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4749bb20-df00-3b3b-99d2-d7e56b88370b | -6.18809 | -48.0777 | 2025-05-13 00:16:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 925e6997-174c-321b-af42-3437ddf089dc | -8.07343 | -43.13465 | 2025-05-13 00:16:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| da767194-4de3-3c71-bddd-d10b641b5c1b | -8.08125 | -43.12387 | 2025-05-13 00:16:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 0be3187a-84a3-37d7-b541-e26795f2d635 | -8.4071 | -43.84433 | 2025-05-13 00:16:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a949c34c-5491-3f18-ba3d-6311d2f91510 | -7.17958 | -35.93617 | 2025-05-13 00:16:00 | TERRA_M-M | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a43bcd3d-30d4-3836-afe8-d36b05635980 | -7.5902 | -45.86381 | 2025-05-13 00:16:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| b4434b03-2e85-3951-92d4-230efe4701e4 | -8.08254 | -43.13337 | 2025-05-13 00:16:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.0 |
| bb636b5e-e96e-3aba-8e8c-bcad2b9621de | -5.72552 | -44.14753 | 2025-05-13 00:16:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30234cca-28f2-365a-89c4-f4072d9630c7 | -8.07213 | -43.12514 | 2025-05-13 00:16:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| ccf4dca6-b217-39ea-bfd0-306ad6a42069 | -6.79457 | -47.59717 | 2025-05-13 00:16:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e3c7316c-e26f-3829-b7a7-40ed98e8b31a | -6.18941 | -48.0711 | 2025-05-13 00:16:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ece445e9-677c-377a-9881-d59ff4a66108 | -4.82425 | -43.21637 | 2025-05-13 00:18:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2867e392-d79d-3e11-8b87-5c1e7b13b931 | -12.1548 | -47.9968 | 2025-05-13 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7c01930e-eefa-3a3c-bd69-1098885e785e | -8.0889 | -43.1196 | 2025-05-13 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| c72a1aad-3aa6-3a71-8fc1-b55a2230f62f | -13.9902 | -56.8058 | 2025-05-13 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 48faf0fe-d975-3e59-86f3-2ac8906ed94f | -8.07 | -43.1216 | 2025-05-13 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 19566a94-6fe0-38e9-b52e-fe2ba8190092 | -12.1544 | -48.019 | 2025-05-13 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 403e65ff-b14c-3ae0-80bc-39234e9191f1 | -13.9905 | -56.7855 | 2025-05-13 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a18fff3d-d6de-3718-869a-7008dfd4e88f | -12.1544 | -48.019 | 2025-05-13 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d7efc5e5-0522-33da-bd91-9b092ee2dbc3 | -13.9902 | -56.8058 | 2025-05-13 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 3b710e49-8eda-37ae-ac8b-1bda317e9522 | -12.1548 | -47.9968 | 2025-05-13 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 926e9088-aa3c-3779-b481-3be4775d941f | -8.0696 | -43.1452 | 2025-05-13 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| c857db4f-a4a4-349d-80aa-07a540d4189a | -8.07 | -43.1216 | 2025-05-13 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 48721fc3-c78c-306e-8176-2bc8cbf700a4 | -13.971 | -56.8077 | 2025-05-13 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| bb1641cf-e292-3486-8b4e-7a78350c49b5 | -12.1548 | -47.9968 | 2025-05-13 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| d94ff8ae-dabe-31a9-a378-e3745e0440ab | -13.9905 | -56.7855 | 2025-05-13 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 75b84b04-ae8c-336d-afe3-3a35a5f5f833 | -12.1544 | -48.019 | 2025-05-13 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| b74c6a58-7aab-37b2-a1ce-264a3eb95492 | -8.0889 | -43.1196 | 2025-05-13 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 0a83bbf8-45bb-3ce9-b15f-a1814ba95c9c | -13.971 | -56.8077 | 2025-05-13 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| dcee5615-a2e2-3bc7-be7c-b19eb4c71975 | -13.9902 | -56.8058 | 2025-05-13 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 572a620a-bc41-35fa-8ab8-79d387e5d8ac | -8.07 | -43.1216 | 2025-05-13 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| acc004f4-91dc-34ee-b5bc-032256b255f7 | -13.5686 | -52.8573 | 2025-05-13 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4001f7f1-0bd7-3589-b8bb-11b967aac877 | -12.1544 | -48.019 | 2025-05-13 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 63e4dede-4afe-3869-bcee-7b7e12299d69 | -8.07 | -43.1216 | 2025-05-13 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 9695df88-89c8-38fa-b74f-8e6558e10f55 | -13.5683 | -52.8783 | 2025-05-13 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c2391d35-6860-3926-954a-34cd5e7dfb74 | -13.9902 | -56.8058 | 2025-05-13 00:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 20589760-0b54-39c0-b01b-c192f79bf570 | -8.0889 | -43.1196 | 2025-05-13 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 0aa62410-b14e-36a6-be7c-1cf1a04bd6a1 | -8.07 | -43.1216 | 2025-05-13 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 12dcb834-f798-3a6e-a324-7d68cffef09e | -13.9902 | -56.8058 | 2025-05-13 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 67bdc24f-360e-3ccb-837d-ed9675d7be6b | -13.9905 | -56.7855 | 2025-05-13 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 5668cd20-420f-3b41-b01e-3fb01a60619b | -8.0889 | -43.1196 | 2025-05-13 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 474e5cb3-e1d9-348c-b802-172956fcd99a | -12.1548 | -47.9968 | 2025-05-13 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e8c1f976-b260-362a-bce6-42107657d6fc | -13.5683 | -52.8783 | 2025-05-13 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6ff4944f-6275-3f50-9829-e69b593903f9 | -12.1544 | -48.019 | 2025-05-13 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b96a33bf-8589-3882-98c3-97c0be3e1985 | -8.0959 | -43.1395 | 2025-05-13 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a48d463b-50e9-331a-80f8-d55228f0c5ae | -21.7875 | -52.7444 | 2025-05-13 01:04:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 413a1f9c-d2bd-387b-84a7-486111d49427 | -20.2264 | -46.746799 | 2025-05-13 01:04:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd909941-3230-3cfc-b2e2-e5b5e80581d0 | -21.7973 | -52.7421 | 2025-05-13 01:04:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5955ae-1583-3e3a-98df-455b49cbaa47 | -20.2239 | -46.736698 | 2025-05-13 01:04:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c1f15cb5-56ab-3437-8c78-3496de407282 | -8.0889 | -43.112598 | 2025-05-13 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 80f57c40-918a-33fa-84b7-24b5f570cd26 | -17.1203 | -49.142101 | 2025-05-13 01:04:00 | METOP-C | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64730cde-5a20-3173-8acd-8890b0d822cd | -8.0793 | -43.115101 | 2025-05-13 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a692814-2984-3232-afb3-5b68fdac43ee | -8.0863 | -43.141998 | 2025-05-13 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b421ed37-06d9-35f2-a75f-1c4c5cbab871 | -12.1544 | -48.019 | 2025-05-13 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 55e15224-dc08-3e23-912f-388ebe94cf59 | -13.9902 | -56.8058 | 2025-05-13 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f0de511b-9d71-3542-abeb-faa1189750ab | -13.971 | -56.8077 | 2025-05-13 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 89a00bdf-9e2b-3fca-8046-7b24fb76db0a | -8.07 | -43.1216 | 2025-05-13 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 19a64d67-fa46-3908-989c-ed6d9b703187 | -8.0889 | -43.1196 | 2025-05-13 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 1c66377e-24b0-396a-8538-8fae1cf17172 | -13.5683 | -52.8783 | 2025-05-13 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5c3b4ce5-f2d8-33df-ba39-d9687cc5cb67 | -13.5686 | -52.8573 | 2025-05-13 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b4e94995-2fa6-3873-9802-69acad11403a | -13.9713 | -56.7874 | 2025-05-13 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d21739fe-ff6a-3479-a7c8-b3c499fee4cc | -13.5683 | -52.8783 | 2025-05-13 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 188fcbbc-16a8-3d67-b279-8cb8f232492f | -13.9902 | -56.8058 | 2025-05-13 01:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 6f9b8208-8bc0-3dc0-b17c-fd5996521f8d | -8.07 | -43.1216 | 2025-05-13 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| bb53d97b-3d02-3b51-a265-4f3652f9bece | -13.971 | -56.8077 | 2025-05-13 01:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 94d8674c-1acc-3c33-a8a7-da59d9de9bb6 | -13.5686 | -52.8573 | 2025-05-13 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d73b2350-7475-30b3-bd9b-ef2f85bbe853 | -13.5686 | -52.8573 | 2025-05-13 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 354bcfbc-88ee-3bdc-a6ee-9d0fd3336d2e | -13.971 | -56.8077 | 2025-05-13 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 3427a69d-4bd5-3654-8115-339c771c58c3 | -13.5683 | -52.8783 | 2025-05-13 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 02584270-7684-3ec7-9eba-4880305c9d2b | -8.0889 | -43.1196 | 2025-05-13 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 6b3ac024-6eba-37d6-a547-59141b4e4db2 | -13.9902 | -56.8058 | 2025-05-13 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a4c38390-e04d-3a0d-8bfd-f72abd9f5f0a | -8.07 | -43.1216 | 2025-05-13 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| b21542a7-a133-3e9f-9cea-6ace4d61c501 | -12.1544 | -48.019 | 2025-05-13 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 60880bd0-61b7-361c-b5ad-d1df51c513d2 | -13.9905 | -56.7855 | 2025-05-13 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a401efbb-9bf9-353f-a467-bd99b84caae9 | -12.1544 | -48.019 | 2025-05-13 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 534600da-9466-3ddd-abd4-b59b7384f638 | -8.07 | -43.1216 | 2025-05-13 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 162b4450-50b5-3a61-8541-ceb9cbc6c957 | -8.0696 | -43.1452 | 2025-05-13 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 40b6e53d-70b5-3e25-9441-907b1c51f2e7 | -12.1548 | -47.9968 | 2025-05-13 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 8bbd4f28-7c74-337e-951e-991a1f837a37 | -13.971 | -56.8077 | 2025-05-13 01:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 993961e3-5133-34fc-b03a-4b03515b3533 | -13.9902 | -56.8058 | 2025-05-13 01:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 35b4f2eb-353a-3648-aaa6-c654cdaf4a45 | -13.5683 | -52.8783 | 2025-05-13 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9b7aad84-5f9b-3f4a-a871-07b1e051ef44 | -13.5686 | -52.8573 | 2025-05-13 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b32b0d4e-ef7e-358c-ae68-5320697d6620 | -8.0889 | -43.1196 | 2025-05-13 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 42ae2c67-5822-34c4-9e39-0e619f05f078 | -12.1544 | -48.019 | 2025-05-13 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c6f7a7c0-44b9-3aa9-a3cf-5bf8bfdabc5a | -13.9902 | -56.8058 | 2025-05-13 01:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| efa17917-f0bd-32c4-b77d-087faa66c005 | -13.5683 | -52.8783 | 2025-05-13 01:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 10c5327b-7b6a-349f-a4a3-6301bbc29f45 | -8.07 | -43.1216 | 2025-05-13 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 09745a47-0e34-3497-b225-12e4e4b4b31a | -13.5686 | -52.8573 | 2025-05-13 01:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e015062c-e001-3bd0-9f7e-13ea4595b39d | -13.9905 | -56.7855 | 2025-05-13 01:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f3d23f2e-8d55-3a48-b3d2-b6ac5b9f31b4 | -13.98584 | -56.81583 | 2025-05-13 01:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d5906293-155b-395b-929b-237f34db6fe5 | -13.97328 | -56.81276 | 2025-05-13 01:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 1c54536c-9c19-31c4-a9d3-2afb495fadc0 | -13.98289 | -56.78326 | 2025-05-13 01:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 8cac348e-e31a-313c-855d-57da8d1115d1 | -12.22078 | -63.78469 | 2025-05-13 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 197e800f-83d6-370c-aac4-574a9bc36f1d | -13.9876 | -56.80982 | 2025-05-13 01:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 26c784e9-f868-3ac3-ae0f-980288d6be0c | -13.98136 | -56.78942 | 2025-05-13 01:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d3563030-3900-353d-8393-ee5c3641fd20 | -13.5683 | -52.8783 | 2025-05-13 02:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 6444d9fd-c417-3903-8f00-91839a7ca9b4 | -13.5686 | -52.8573 | 2025-05-13 02:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 0203bf29-ef06-36fe-9ec0-50028724a950 | -13.9905 | -56.7855 | 2025-05-13 02:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |


[Clique aqui para ver as próximas entradas](README3.md)
