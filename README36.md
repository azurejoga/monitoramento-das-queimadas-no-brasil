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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85f661f5-4105-3ee7-b9cd-34785bb32400 | -23.00291 | -46.59775 | 2024-11-24 04:04:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1886c102-3723-311a-a0fa-a2e383134738 | -23.06696 | -47.42531 | 2024-11-24 04:04:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 084b4c31-65ee-399c-a258-2a09eb376b89 | -20.72255 | -53.5481 | 2024-11-24 04:04:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 547b2f74-37c9-3fdf-baf2-57eb313dece7 | -23.6294 | -46.42674 | 2024-11-24 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2d71f82d-48d8-3fb3-aab6-f0e3d017af6d | -20.32428 | -48.82007 | 2024-11-24 04:04:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08b213c8-ba6e-3e75-a99d-fc26820a8d58 | -21.31369 | -55.95234 | 2024-11-24 04:04:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ca28fe1-6edc-31f7-b3f3-6e7fa9841f8a | -23.43892 | -46.51553 | 2024-11-24 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a2c2160-7c5b-3184-8992-6f5810085812 | -20.32354 | -48.824 | 2024-11-24 04:04:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 853168c0-6e2d-35cd-8b11-0ec2bf424eca | -3.054 | -49.4471 | 2024-11-24 04:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e1527504-e4be-306c-9396-596da564e958 | -5.0998 | -43.151 | 2024-11-24 04:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 166793a7-625d-3a94-a618-8ad4bee53cd0 | -3.0355 | -49.4476 | 2024-11-24 04:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f9a13462-0a99-38ea-828f-dd7f991345c0 | -3.5159 | -53.8132 | 2024-11-24 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 509eb14d-2bac-3fd5-804c-08b7fc3b6185 | -3.5159 | -53.8132 | 2024-11-24 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 265c1b0a-d0a7-3d6b-b248-b1aab7a7e27c | -3.0355 | -49.4476 | 2024-11-24 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8e8daa7d-bce2-31f8-bd26-426c0ab31a4e | -3.5159 | -53.8132 | 2024-11-24 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b01a3dc7-1dc7-3cec-8d7e-213f9ed873bb | -5.0998 | -43.151 | 2024-11-24 04:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 90a37e70-b511-3989-9f90-3b07f1e4575e | -3.0355 | -49.4476 | 2024-11-24 04:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 051c3b44-45bb-3508-8bad-3945579533bb | -1.2964 | -51.741 | 2024-11-24 04:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| aabe4633-fd86-3394-8b09-8d6e6dc3dd7d | -3.0355 | -49.4476 | 2024-11-24 04:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e45454c5-7443-399c-85c0-87c5269ce28a | -3.5159 | -53.8132 | 2024-11-24 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3bdffb51-76b5-3bc2-86a4-79974e16eaff | -3.0355 | -49.4476 | 2024-11-24 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ba5e80b1-8a55-3aa6-9dcd-a62a9ce81f86 | -3.5159 | -53.8132 | 2024-11-24 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 728ac84c-bb6f-354f-a2a7-5dac2f36693d | 1.77153 | -50.95251 | 2024-11-24 04:50:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a3e552a-907c-3045-9c6a-7c6a86c668c5 | 1.78804 | -50.42574 | 2024-11-24 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df545027-29fe-3dae-9bdb-5fbb3a335c17 | 2.19076 | -50.71843 | 2024-11-24 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 230c0d0a-bf63-326e-b946-73fb0bb84e3f | 2.02486 | -50.80731 | 2024-11-24 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afbf4d6d-17fd-34f9-9f8d-1118ad97cca4 | 1.79189 | -50.42868 | 2024-11-24 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f2fbe1b-b21e-3191-b6e3-fdc88bcabc63 | 1.77483 | -50.952 | 2024-11-24 04:50:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf81e4a-a833-32e8-9467-9f8f8742a4e2 | -2.951 | -51.42613 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94b5dac0-5fb2-3f11-a48c-abe9a9ec2031 | -2.81071 | -54.02692 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c051ed01-7d08-374d-8541-029b762302e0 | -2.48775 | -49.03019 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 852f190e-8c44-3b64-8f59-822bffd3b030 | -3.13306 | -52.98343 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef69856e-30e5-33d4-a694-93cba11cfc0b | -1.60854 | -52.57374 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e42cb138-df4d-3df8-9463-2e6dd7587e14 | -1.4812 | -52.51845 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2be34533-0c97-38bf-ba7c-7c1c5d67c9c8 | -1.96882 | -48.39039 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a438d5a6-f046-33c1-9aa1-5946440a7e4b | -2.97193 | -53.85201 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75fa823a-4615-33f3-9d22-53b6a4a43955 | -2.99086 | -51.45355 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2232bde4-e7a0-3ebc-a3db-6d0585f85809 | -3.31714 | -50.12532 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 407f2b68-e44e-3dc2-84b1-0580bacf9aad | -2.22512 | -50.78111 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 779f722f-ddfe-3964-b090-2c4783126221 | -3.05271 | -53.42886 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbbd663e-bb63-330b-acd7-cd3d2d6f8f30 | -3.79159 | -43.59944 | 2024-11-24 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6800322e-038c-390d-a980-85dd2e8657ba | -0.03791 | -51.61147 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 854424a8-4b4d-354a-8c8f-b9c9ba011b01 | -3.50421 | -53.81844 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ab69bca0-19f8-3009-b8c8-c261b67e3197 | -0.81803 | -51.60347 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 736d0db0-0cb4-32b7-88f9-c6957f993d78 | -3.28633 | -53.84086 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 132903fe-126c-3532-a8c8-4da6dd070198 | -0.03416 | -49.64326 | 2024-11-24 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2ddc7b2-a9fe-3c66-b076-0f4af2852834 | -1.81916 | -50.98368 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54cfa599-0142-38ed-83f0-3e86932ec969 | -2.19723 | -50.54114 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70a379c9-6934-3460-8a11-d8fc0b3b5ade | -0.83972 | -53.03067 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b282516a-ed5f-3499-90e6-f4dded72b919 | -2.3114 | -50.59495 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d26d3c3-35ca-353f-bdb2-e7f1914476b4 | -5.41729 | -45.76179 | 2024-11-24 04:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d063efa6-21c3-3a42-8901-63af9addc609 | -3.07404 | -45.96775 | 2024-11-24 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f32ccbe-fe66-3584-8a88-962a6b758578 | -3.2814 | -53.01359 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3666dfc5-1413-3a5a-94ff-84fd94f551c7 | -1.69939 | -52.75541 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49a0098e-7d8b-38d8-8020-1e81bdd25194 | -2.81129 | -54.02321 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d11b5f74-bcee-3ab0-970d-a8d64db1a3ad | -2.27485 | -53.57331 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65f79238-6d12-3b9f-910a-315c3b2cae6d | -1.51522 | -54.18232 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3f5ac962-13d3-34e9-99e4-c2fb8d44624c | -1.64097 | -53.87499 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab596492-8846-3b8e-9ead-c072f24d2f55 | -2.68407 | -52.0715 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c584de43-e501-330c-9275-332fb84d4964 | -1.72396 | -52.4885 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0556ed46-6c65-3e01-8390-dbce7f1b9407 | -5.94911 | -48.05715 | 2024-11-24 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10b29376-d30f-3419-a149-62f2bf7c4484 | -2.83756 | -54.01248 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5e272f4-8dc8-34e1-867d-ee1f37d2cc3b | -4.88919 | -48.90735 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7dce9925-c11d-30d0-8a0f-c2b87fc8ec51 | -2.45345 | -49.08684 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ca8a621-afcc-3465-a729-36febf7d89f8 | 0.0449 | -51.70406 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c33b6076-4047-38c2-ac4f-9db1b261f0cf | -2.57173 | -55.91434 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ae6a96-7c06-3de5-bd42-e228735489be | -2.8398 | -54.02043 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae81d082-5bcc-33b9-9e2f-6bb090438d43 | -1.12929 | -51.68027 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b03ecf8a-acbf-3476-9253-46a1fca558b8 | -2.8536 | -53.99977 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 321c8119-14c0-301b-8bc9-f74e88931e5d | -3.70671 | -51.79495 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06c2b183-6462-3ab7-b247-c97d22fc3783 | -3.58545 | -50.52741 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 477a2534-ac98-39c6-830b-5d07f5fea0a0 | -2.83072 | -54.01142 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6981d9c2-a054-309b-bead-9c20779b5d4f | -1.0992 | -47.50512 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6b3c188-e251-38d1-a52d-ece930b29aef | -1.2439 | -51.62142 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 076bf5ad-a12b-3348-8faa-b7610f91ab64 | -0.81533 | -51.49075 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb50206a-def1-3bab-9b8b-43901f5c86ac | -1.73827 | -52.72272 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 88415d10-a0dd-3640-9b49-cdac3938f7a6 | -5.19561 | -49.15606 | 2024-11-24 04:53:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9b55a96d-36b6-326a-b6d8-e439b47f6d2a | -2.05769 | -49.02253 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d22a11f1-607f-3ce4-a221-7b24b50ac7de | -3.1764 | -46.54339 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00fbe217-4592-3437-9fb4-6699f0a20dd9 | -3.63307 | -54.44093 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8159a0bc-5c0b-3990-a040-7c1923fbf0e2 | -1.48802 | -55.08855 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0557832-069c-3666-b441-0804fa906a21 | -0.36 | -50.02605 | 2024-11-24 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3adc3066-a7ce-312d-ad3c-bc767f7c32da | -2.45834 | -49.14919 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f027282c-395e-3510-a773-77ab9ef3e458 | -2.14638 | -50.71487 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 235a1f8e-bbb7-3f85-a814-857883fa5b4c | -3.09894 | -53.73723 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e2ab697-2104-3ea7-8e44-a2c32efdf41f | -2.20616 | -50.77098 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9712775-6778-3988-9ccc-c55cb11c0838 | -1.1425 | -51.6823 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb07f57b-ba1b-3373-8673-f65660761329 | -3.17528 | -54.32058 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5516efb8-5f84-3063-8373-040e859316dc | -2.37277 | -50.33269 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73f45503-55f8-3876-b451-3d55dc422fd2 | -1.75193 | -54.52145 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4dbb004b-14db-3d0e-95a3-166ddcc90b55 | -1.93158 | -51.13593 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75855724-a506-3307-9379-31296da83796 | -3.19955 | -54.6302 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 206835d6-56ae-3848-8c4f-580a0cbcc0d1 | -3.22067 | -51.00272 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd692d40-0b54-343d-a521-053e157e7ee8 | -1.89834 | -48.5078 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f816960-d51f-3ca9-920f-f4eab0669bbc | -3.25609 | -54.22918 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f0a20c2-611b-32d7-91c1-93782bc40a0a | -2.79942 | -53.00633 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 048477bf-194a-3519-8bc8-be67346250d0 | 0.08976 | -51.48925 | 2024-11-24 04:53:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de213b4c-8b4d-3149-b1fb-3c5684d7bad3 | -0.90997 | -51.73402 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3466eac7-19ed-3875-97b5-aae43f9b0392 | -2.29549 | -49.0517 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18082c48-217f-3481-a1ea-80285a536f1b | -5.4325 | -45.45598 | 2024-11-24 04:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
