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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0977cc6-29c4-3f1b-a5f3-d675d461da8c | -16.31063 | -58.60966 | 2024-10-16 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f9b1502e-7014-3d31-828a-c25e4f7ff99d | -15.46949 | -59.33128 | 2024-10-16 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94604d5e-edf2-3e47-8134-473b11e49d84 | -17.02407 | -58.29453 | 2024-10-16 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 8f421b2d-2fce-3ebd-93a7-53e899f4d803 | -3.38706 | -59.86436 | 2024-10-16 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11f1b01a-55fb-388e-ac91-7b880bc93389 | -3.55877 | -58.70334 | 2024-10-16 05:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f6c020c-b4ad-398e-816c-c330ec8d270e | -3.40521 | -59.70563 | 2024-10-16 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ba933a5-9bfc-36e0-905b-84d6ccf1df35 | -3.40192 | -59.70512 | 2024-10-16 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8acbe747-a586-33af-9bce-82d2e67e7feb | -4.38421 | -59.95511 | 2024-10-16 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 028facbc-5da8-359e-b59c-455bfba7ac13 | -11.11059 | -60.46671 | 2024-10-16 05:25:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 915e8486-9a0c-3cea-ae85-5ac500ee4609 | -3.99524 | -60.39337 | 2024-10-16 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8046521f-aabe-3ff8-81ae-f2a1316a28c6 | -3.95582 | -60.46831 | 2024-10-16 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ee9bf8b-5707-3b2b-82f1-1106003bbaad | -3.95251 | -60.4678 | 2024-10-16 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6a30ff0-01d0-3cdb-a477-1bf90823967a | -12.53401 | -63.29227 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a968f71c-42b7-3265-93da-80d871404269 | -12.53183 | -63.28443 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc6f4ff5-d08e-3a38-b4f7-cfc6f9f23a3b | -12.53006 | -63.29535 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 49359fd9-88ed-3ea8-bf56-d9aa5c5eabfa | -12.52612 | -63.29842 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7530960-8982-392f-ae4d-31c161ebaf25 | -12.52453 | -63.28694 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e395c6d-310a-3727-be76-a817083e51d1 | -12.52235 | -63.27911 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e20af65-71f7-3fff-a525-7882bc74b2d3 | -12.52117 | -63.28638 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8a36d7cd-d9a2-3518-a7cf-b4619b0f289d | -12.52059 | -63.29002 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94b01541-c621-3ca9-b508-97929f7cb3f1 | -12.52 | -63.29366 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94d7a045-678b-32b4-9c79-5ea7a52208b4 | -12.51899 | -63.27855 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad3e8a29-730d-3648-aa45-05572153d6f2 | -12.51841 | -63.28219 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e963e2ea-f38f-3540-8869-eb0db1dbb937 | -12.51782 | -63.28582 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be675879-999f-3b1f-8e50-2527e14fa4a6 | -12.5117 | -63.28107 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a63e6b55-4854-3bab-bc62-a7db74342def | -12.50993 | -63.29198 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a49bbef-319a-3a32-a369-b440b018442b | -12.50893 | -63.27687 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a518bb1-bb9f-378a-8c32-0fb9b42a9a69 | -12.50834 | -63.28051 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4773aa88-7fd2-3f96-ae27-ab73b16e8789 | -12.50775 | -63.28414 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ddb8f50-7d83-3cae-9466-1b04fe9e40f6 | -12.50558 | -63.27631 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 176fc16a-5199-349f-9340-f1fbb223a7a0 | -12.50499 | -63.27995 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ad40202-4bf4-3b83-9861-bf9e9cc0721c | -12.5044 | -63.28358 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 640e8585-5c30-3bb7-8d72-40b71a0a6e31 | -12.53342 | -63.29591 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ba4c88d-c913-3b6f-b9c8-d19c23b25e74 | -12.53124 | -63.28807 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fb1167c-65b0-3415-b385-9fb62ce59ff4 | -12.53065 | -63.29171 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bd39500-0bc8-3c77-8229-35bd56522d18 | -12.52948 | -63.29899 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8eeeaf41-f480-3f1d-9a82-79db0346f49c | -12.52847 | -63.28387 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a8859ea-cac4-30b3-8776-1b4ebdb7aa62 | -12.52788 | -63.28751 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 212d190e-0fa0-328d-a1a7-8c075e0d8308 | -12.52671 | -63.29478 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b76a2ed-3b45-31f8-ace0-150612e0efdc | -12.5257 | -63.27967 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ed2a69a-0e10-3935-af6a-fe985372d4ea | -12.52512 | -63.28331 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d87f86b-09b9-3bb9-bbb0-3d409675bef0 | -12.52335 | -63.29422 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a2c70d9-3976-3b7f-8505-d472c973ec88 | -12.52176 | -63.28275 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 49a21896-bf59-3a72-8a52-2e45f5775740 | -12.51664 | -63.2931 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb70a128-8bc5-3067-8913-63b48332b176 | -12.51229 | -63.27744 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c93094d-ddcd-35ab-a38a-f19e5def66a3 | -12.51052 | -63.28834 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e5d557e-f55f-3e68-a1c4-599525186823 | -12.50716 | -63.28778 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dacae112-5d13-3710-9e7c-cb568f1defdc | -12.4961 | -63.27099 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 930f37ac-5f83-37b2-80f6-5c8ab5424272 | -12.49334 | -63.26681 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6a2df5a2-8282-3168-9dcf-5670cc310bf7 | -9.9823 | -62.90124 | 2024-10-16 05:25:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e704466f-2aa2-3e26-9c4b-d6ab6678d511 | -9.97892 | -62.90073 | 2024-10-16 05:25:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ca295b1-5c23-3a3b-8d89-88c7a7d23556 | -9.97833 | -62.90437 | 2024-10-16 05:25:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f44ff49-2156-3103-8526-68a990f1a517 | -9.54768 | -62.80819 | 2024-10-16 05:25:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0feeae88-620e-3fb7-9e8f-22b487fed194 | -9.62535 | -62.95958 | 2024-10-16 05:25:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cd448bc-9bed-399c-b05e-f49e6372145b | -12.08791 | -64.81701 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 008826f0-b389-3a8c-bed8-f9563d9c1fe7 | -11.96076 | -64.84341 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88baf078-586e-3b87-9b75-4fe46f565008 | -12.13798 | -64.73698 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bbbe43d-5554-3e36-bded-40baeae6301f | -12.13444 | -64.73637 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adbde2d1-18cc-377d-a860-29dff6cc054b | -12.11958 | -64.73801 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 060c9131-d56f-3b5d-8d86-65bf3db8521f | -12.0571 | -64.67737 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7811007f-07bb-3f27-a1bb-61c02bf9b33c | -12.05642 | -64.68144 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5637e8e4-ff88-303a-bc43-b143cc5fe4f7 | -12.03611 | -64.71573 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e120ab80-7cdd-3cb9-872c-c8d7b40c2417 | -12.0184 | -64.71264 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6501b594-12b2-315b-a44a-ddc8917695f3 | -12.00786 | -64.73186 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f62d1359-02c2-3f9c-9fc5-327acf714d54 | -11.97918 | -64.73212 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5111ff8-2b54-3535-9946-3ff30b28d55f | -11.9785 | -64.73623 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fdf20ed-6935-3e06-88f5-4c638479113d | -11.96377 | -64.75901 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3abfab4-9e55-36ea-950a-3328d40cc117 | -11.96022 | -64.7584 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62d9dccd-8f0a-3661-ad9b-9122f4560543 | -11.95666 | -64.75778 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0300bdb3-855d-3ccd-a17e-2a71f9c5e494 | -11.95598 | -64.76189 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4d7129e-089a-3bc8-90a1-ef820635eae6 | -11.79633 | -64.17216 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d1a9a7d-8445-3c99-8050-5c0200db7fc6 | -11.7909 | -63.80066 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adced748-6eb0-3908-99bc-ed2ab15afbf9 | -11.78852 | -64.15482 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bff1aa9-cd1e-3e01-9e57-0bfde5c38eb8 | -11.76936 | -64.08452 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01de02a4-5d0c-3e1d-b143-09b8d503e51d | -11.76873 | -64.08839 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f864d67-7774-35f1-9dba-ba5898585947 | -11.75962 | -64.07887 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e490f1a-de40-3561-8280-97f9888c0ab2 | -11.75899 | -64.08273 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87a76c61-900f-3b55-96c3-0c46045a96b0 | -11.7587 | -64.06277 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5e5c67d-a899-3697-bbe3-c4b127d9477e | -11.75743 | -64.07054 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60a3888e-3daa-3a8d-8f76-5ec3ac111c50 | -11.75665 | -64.15345 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 380035f4-1049-36e7-ad90-5399b1b1b149 | -11.75229 | -64.14549 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed05e3ad-99df-346e-a0e4-5cbb97a7f37d | -11.74691 | -64.15659 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c063f681-464b-321d-8bee-6bccd5ea5265 | -11.73677 | -64.02333 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ea96670-35f2-385a-8e54-2adbc26ae7d9 | -11.73332 | -64.02272 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df67695b-ef34-30eb-a6b6-763a4bc28fc3 | -11.73296 | -64.04649 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 722e0f96-6af6-3210-a504-bfca8dbc6a70 | -11.73232 | -64.05036 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8af29bc-0b4b-38dd-878f-aa26c9c02006 | -11.73168 | -64.05426 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96ca9e22-826f-36a1-be02-065b409369a1 | -11.72605 | -64.0453 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f791c1d5-7374-31db-ae1b-b65d1a703d46 | -11.72579 | -64.02534 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb5c85d8-755f-3f78-8e57-e9759853826d | -11.72234 | -64.02473 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ca17e91-e2c0-3964-9a47-dcd8660da566 | -11.67842 | -63.93089 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9717c53-3695-36ee-ae86-9814c7d36e81 | -11.66437 | -64.0389 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edf21020-1dc1-39fb-9cb1-1f7d52f480a3 | -11.66373 | -64.04281 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b0a6a25-e27e-38a1-aabd-00022bccd50f | -11.6614 | -64.26293 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2aa92f7f-789c-3226-a2f2-dc6a9b78888b | -11.79416 | -64.16377 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d963af8-97d9-3625-8b97-f81988a922bd | -11.79221 | -64.17549 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f90d353f-9d4e-355a-9b4c-2a07d6f2cda9 | -11.7857 | -64.15034 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9759303-1996-387b-bee4-61a61dc93d42 | -11.78505 | -64.15423 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3fadf24-e89a-3784-9955-c928a70a7da2 | -11.78223 | -64.14975 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06bd7eae-4aed-3787-984b-5213f558ae43 | -11.76836 | -64.0836 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README62.md)
