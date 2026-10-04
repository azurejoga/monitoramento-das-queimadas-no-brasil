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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8be60f3-7e42-31eb-a840-ad10945a2cd7 | -3.1116 | -53.7234 | 2026-10-04 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 55777a19-8d26-35c4-a22e-c3db6d81aeda | -4.2701 | -50.2894 | 2026-10-04 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 76412ad4-7963-3a33-a22a-df479d651160 | -2.7979 | -54.1134 | 2026-10-04 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d0456623-d092-3965-966d-372dcef41e59 | -2.8163 | -54.1129 | 2026-10-04 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9c51c890-c77d-384e-aa69-2b3d5d9375b5 | -4.2886 | -50.2886 | 2026-10-04 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 219.9 |
| a62728df-ba7d-3909-af68-6da0007b312f | -16.56619 | -40.51649 | 2026-10-04 03:40:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99e466ee-2472-3123-a0f5-03d70a6aa824 | -16.83829 | -39.15351 | 2026-10-04 03:40:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 53960dc3-f229-32d4-a24a-8acb7000bc53 | -16.83919 | -39.14851 | 2026-10-04 03:40:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a84f1df6-8760-37c9-9604-7955fb204d57 | -16.84304 | -39.14928 | 2026-10-04 03:40:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ebb525ea-2eff-3c31-8431-c5ffcb0dfe11 | -2.8163 | -54.1129 | 2026-10-04 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| d7f2040e-e781-3bc4-ac6f-690fd71a4cb8 | -4.2744 | -46.3846 | 2026-10-04 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 2046b42e-57fc-3e49-b883-261a303446df | -4.2886 | -50.2886 | 2026-10-04 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 3b404eb5-6d90-3cfc-9847-7adfed633e99 | -4.2888 | -50.2465 | 2026-10-04 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ea4c1b7f-a547-318e-9a0f-4eadb1ac4c2e | -4.2559 | -46.3633 | 2026-10-04 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| ad121ce9-74cf-3586-996a-344de5a4f8d0 | -2.7979 | -54.1134 | 2026-10-04 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 075c4613-e4b9-3999-92e8-42addfd2f03f | -3.072 | -49.5525 | 2026-10-04 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| daa63c04-0fce-325d-8501-7aa7dc57145e | -4.2887 | -50.2675 | 2026-10-04 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 484.5 |
| 1cedccd4-b941-37e0-a2b2-e278c4e9e8e8 | -3.1116 | -53.7234 | 2026-10-04 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| cece897f-7c71-3dd3-a023-306cc2ac6e9f | -3.1299 | -53.7431 | 2026-10-04 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d874fc0d-b6e2-3185-8e39-5f3c4dcae2bc | -4.3072 | -50.2668 | 2026-10-04 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 6100f60a-cd6d-31b5-becd-fa4354146803 | -2.5842 | -51.8623 | 2026-10-04 03:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e5c38e71-a8a5-3ddd-8cdf-77377a5cadc9 | -3.0721 | -49.5313 | 2026-10-04 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3542e287-bd6a-360f-aef1-79155b945549 | -3.0364 | -54.2282 | 2026-10-04 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 87e51c1f-d1ff-3bb5-8429-92bfe0a0a7fa | -3.1116 | -53.7436 | 2026-10-04 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| c82c2ab4-578e-325a-b922-67d4946b2cf6 | -2.8163 | -54.133 | 2026-10-04 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9399f013-5db6-3d45-85dc-361094cdd91f | -4.2558 | -46.3855 | 2026-10-04 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 17e1cff6-59b3-3014-b23f-de5a803f8c70 | -4.2701 | -50.2894 | 2026-10-04 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 2f8bd529-7258-30d8-8384-3225d71a269f | -4.2702 | -50.2683 | 2026-10-04 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 328.9 |
| 63f39cb0-0a82-3fef-92a0-dfdcce5fe619 | -5.8642 | -55.7071 | 2026-10-04 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| bf9991c6-a62f-3f0c-962d-19b8dcc5fdfc | -4.2745 | -46.3624 | 2026-10-04 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 80361ef2-f18a-39a7-8767-e1c9ad06a9f8 | -3.13 | -53.7229 | 2026-10-04 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| fb5bf54d-8456-3236-a631-bebbb339fd6e | -2.8163 | -54.133 | 2026-10-04 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 58b32338-bdc4-316e-9616-cbfe724b196a | -3.1116 | -53.7234 | 2026-10-04 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 203.1 |
| c2a3c11a-f1f5-350c-aa4a-f1a3dc172d3a | -2.7979 | -54.1134 | 2026-10-04 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9ea4dbf7-292e-3cc6-8862-dac68e1f3e48 | -4.2744 | -46.3846 | 2026-10-04 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 6a5ca674-4549-3b5a-ae8c-5ef53488c0da | -3.8756 | -55.8184 | 2026-10-04 04:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 77a7f5ff-937f-3918-b349-f025cb6f3a82 | -2.5842 | -51.8623 | 2026-10-04 04:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 19ec768a-9ed9-35ab-bdfe-f1d76b278078 | -4.2745 | -46.3624 | 2026-10-04 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 630647a4-2a79-3279-96d4-0bb48c3e348f | -4.2558 | -46.3855 | 2026-10-04 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d86f5987-ce46-31b4-9dc6-30f624333812 | -3.0548 | -54.2277 | 2026-10-04 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 96a8fbb3-772a-3d9b-87b8-a9cf93d11430 | -3.1116 | -53.7436 | 2026-10-04 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| a2f777d9-3367-3055-899e-afb386faf1f1 | -2.8163 | -54.1129 | 2026-10-04 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| f8baa6ac-297b-3e6b-a2cd-91c5e2b15d6e | -3.13 | -53.7229 | 2026-10-04 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 97afb777-266c-3c9a-bd69-c891fe14a665 | -3.4762 | -50.0883 | 2026-10-04 04:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e418a03e-dfcf-3251-8b9b-d0849bd5711d | -4.2559 | -46.3633 | 2026-10-04 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 125.7 |
| b419e81b-e776-3e95-988f-92b2349f7120 | -3.1299 | -53.7431 | 2026-10-04 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6f5469ea-b5db-35b3-b4bd-7c5dcfafdfa0 | -2.7979 | -54.1134 | 2026-10-04 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3a3a2304-b8d7-3b7c-b313-a861e355ce52 | -4.3072 | -50.2668 | 2026-10-04 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 237b9113-56cd-3d96-b78a-568f3a3e6b0c | -3.8757 | -55.7986 | 2026-10-04 04:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e14c519a-6081-35aa-b10a-9ee51ad9a2da | -3.1116 | -53.7436 | 2026-10-04 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 040ba784-1f86-3f6b-a408-7f57735ecfc1 | -4.2559 | -46.3633 | 2026-10-04 04:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e24d1958-097e-384d-a2eb-0f43ad4640da | -4.2888 | -50.2465 | 2026-10-04 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| cbdb1849-7624-36fd-97bf-bea8aa744bee | -4.2744 | -46.3846 | 2026-10-04 04:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 73ca866c-2ece-34b6-9018-406cda68d608 | -2.8163 | -54.1129 | 2026-10-04 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 05077e3d-1ada-3f73-bd3b-33e449cd9071 | -2.5842 | -51.8623 | 2026-10-04 04:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3a6b22e7-0b41-350e-aebb-98f7272fcdd5 | -4.2745 | -46.3624 | 2026-10-04 04:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 1aa4c0f6-b36c-3742-8b93-6f43da0630c3 | -3.1117 | -53.7032 | 2026-10-04 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c8c69afd-fe86-3e07-b0b3-2bec4de14cce | -2.8163 | -54.133 | 2026-10-04 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| db1f2c8b-31db-3187-b782-b8d19fce3b24 | -3.1116 | -53.7234 | 2026-10-04 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 17cef592-c165-358e-ae0c-8bdc86dabdff | -3.13 | -53.7229 | 2026-10-04 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 24c79a09-0607-3908-888b-5452d2b5ce84 | -4.2886 | -50.2886 | 2026-10-04 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| b6f5ee5e-8733-369a-98d4-d32fc8deb8b0 | -4.2702 | -50.2683 | 2026-10-04 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 342.6 |
| 00a24b1f-b49c-35e5-9739-bae7cc9d104d | -4.2701 | -50.2894 | 2026-10-04 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| ee2a9879-7778-3a37-9b29-1e5d426e4f65 | -3.1299 | -53.7431 | 2026-10-04 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 091110d6-ca66-38f3-baf3-3294c8876bab | -3.8756 | -55.8184 | 2026-10-04 04:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1babfa1d-4665-3352-b0f6-4b727e176478 | -4.2887 | -50.2675 | 2026-10-04 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 600.8 |
| c2615598-dac7-3f1a-b3b9-2d1d044cf185 | -4.28 | -50.32 | 2026-10-04 04:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1474e800-9459-399b-9310-5b9282f059ba | -4.28 | -50.26 | 2026-10-04 04:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d53c32f5-3c57-3cf2-a0fd-49562485e510 | 1.75854 | -55.65554 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e4c9739-c8bb-3d7c-872c-248ee5f8a76a | 3.42477 | -51.30399 | 2026-10-04 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffc98c80-4c3f-3e89-b1fe-1605d2797d4f | 2.34739 | -50.7526 | 2026-10-04 04:17:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07a4fcdb-ae1f-3a30-b430-a9f36e4bbe9c | 2.09662 | -50.74106 | 2026-10-04 04:17:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cd176283-3755-3da5-82c1-48fcac277bfa | 2.09905 | -50.73346 | 2026-10-04 04:17:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7927272d-a12f-3490-acea-d77bf1a2a1bf | 2.0008 | -50.93286 | 2026-10-04 04:17:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f6b3179-6c46-330e-b0af-997e359965f7 | 1.75842 | -55.63818 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71ce449e-be63-387f-b2dc-7ed611d1ddf5 | 1.76233 | -50.92975 | 2026-10-04 04:17:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d371a259-5d8f-3daf-970b-def7ac612fd9 | 2.35717 | -50.75122 | 2026-10-04 04:17:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee5071a8-b977-3a6d-9a2c-bc78b0692a2f | 1.81187 | -55.55855 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a8ea2b4-de5a-3105-bdec-721049bd1a3d | 2.35228 | -50.7519 | 2026-10-04 04:17:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6cbc8c3-27a7-3f6f-88a7-bb34f0800c5f | 2.09578 | -50.73572 | 2026-10-04 04:17:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 73a526b5-135d-329e-8ab0-0072798487fa | 1.76416 | -55.63137 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a2adcdf-8195-3c5c-b3c9-f7e7e33347fa | 2.09499 | -50.73954 | 2026-10-04 04:17:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d9cfd3b-70a6-39be-bc52-71ccaf03894a | 1.03911 | -50.02093 | 2026-10-04 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 921edbdc-3864-3c94-89a5-9e478bc2e4af | 2.09985 | -50.73883 | 2026-10-04 04:17:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67dd08c0-32d9-328f-8745-616414c90ea5 | 0.70068 | -51.43446 | 2026-10-04 04:17:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e43e31-0f14-33ab-9d3e-4a99c7b8057d | 1.80524 | -55.55951 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6877f0f3-d0be-3843-be64-67f4beea8ed0 | 1.99903 | -50.93486 | 2026-10-04 04:17:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2725b50b-74ff-3136-b281-314485310dec | 2.47542 | -50.78765 | 2026-10-04 04:17:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aeec8481-aa0b-3409-9d75-03311608623a | 1.7617 | -55.63104 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b138ab4-2c68-3340-b5be-c8e2737e452d | 1.76257 | -55.63686 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51843d51-fd13-34f4-8ee3-bbaa13e7e3ca | 3.42431 | -51.30091 | 2026-10-04 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a07a0cb5-f6f4-35af-a069-0ecb25bf727d | 0.70024 | -51.43164 | 2026-10-04 04:17:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc819554-3ab1-3bb9-b33f-ce1b5a570a70 | 3.41916 | -51.30165 | 2026-10-04 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17933b58-df56-3cb9-a4de-53058dfdbe0b | 1.81276 | -55.56438 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b96ce8-1291-36f3-95b7-6da194e59ff5 | 1.90827 | -55.76456 | 2026-10-04 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8aeb5d16-b44d-3899-a95f-192760a0f6ef | 3.36044 | -51.34586 | 2026-10-04 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09151d07-452b-3840-a219-55d6d32ef4f4 | -4.29329 | -50.2712 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 09f4d084-0235-3bcf-8400-c11f088b1de7 | -6.0842 | -53.30573 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1eecc721-7da3-3cea-9d5f-62471bf870ed | -2.82345 | -54.11844 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26d088eb-ca3c-358a-b9c9-31a8858008d6 | -3.12165 | -53.75506 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README23.md)
