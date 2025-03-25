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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d4f48ee-b5c6-3140-925f-42d32227b967 | -12.12616 | -39.75287 | 2025-03-25 04:32:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce2d3e97-ce39-34cd-b540-0448f735272b | -16.03683 | -43.72932 | 2025-03-25 04:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 048b0ae5-0bb1-377c-ad81-8f85d72c13d2 | -16.09109 | -42.28313 | 2025-03-25 04:32:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 6ec879f1-1039-31b1-98fd-62d1b172f95a | -10.57885 | -45.14013 | 2025-03-25 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 201808be-f8eb-3150-8fb0-b2640174be8c | -16.03908 | -43.72852 | 2025-03-25 04:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5c481dc-a863-30fc-99f3-43427e46df84 | -17.8609 | -39.85925 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| bc4436db-c85c-3297-a4bf-0bf57243ee3a | -17.86223 | -39.86183 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 8588447a-5d48-34d1-9cb0-a9752a5c61b4 | -17.86263 | -39.85774 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 636a5392-ab25-3aef-84a8-bcd462946ad0 | -22.89236 | -53.50795 | 2025-03-25 04:34:00 | NOAA-20 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 04969bc1-484c-3fc9-8ca7-052226372313 | -22.20727 | -56.97483 | 2025-03-25 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96e2d3e0-c9da-3773-a4c4-edb46f80d57d | -17.86182 | -39.86594 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9a3bb218-4c8f-330c-93d9-d42541a2a890 | -17.00686 | -49.77943 | 2025-03-25 04:34:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55cdbc2a-a4b4-3cf8-bf6f-b19bdb376416 | -17.86575 | -39.86803 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 91a475f5-3c0c-3fe0-9e41-aab8ab85757e | -22.78508 | -43.75776 | 2025-03-25 04:34:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f4931472-2b27-3066-a9ee-75615924b37b | -22.20802 | -56.97101 | 2025-03-25 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 578c61c4-a106-39a2-95ee-66b3e17506d7 | -22.19426 | -57.08445 | 2025-03-25 04:34:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feec1dc0-8c12-302c-aa72-66ffdb771da3 | -17.85519 | -39.85856 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2298e707-8587-3b9d-9f75-32abd8c802e0 | -17.86663 | -39.8598 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1b8e9157-7a4e-32e7-8391-3e9f3b8dc2bd | -22.89576 | -53.5086 | 2025-03-25 04:34:00 | NOAA-20 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b12912c0-6c48-35b0-bfd7-774bd7e92d42 | -17.85035 | -39.84958 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9fedf6b2-3580-399f-8002-b8b169066714 | -22.89509 | -53.51257 | 2025-03-25 04:34:00 | NOAA-20 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e03c102-6a58-36ae-a9be-126fb993ddbc | -22.20699 | -56.97594 | 2025-03-25 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15acd6ff-c4a3-339b-a360-abab2132f49d | -17.86428 | -39.84112 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a200ef94-6ef1-3f6a-a1dd-75c70329f17d | -17.86919 | -39.84999 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e3c55ba-83f9-3a97-a963-1da6ca2de24a | -17.86047 | -39.86333 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 5fb3ac97-480f-37cf-b60c-dbe2e457e7ae | -17.55901 | -40.63492 | 2025-03-25 04:34:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f750d977-ddcd-3c9b-8c5d-2ab33d4b6aac | -17.85562 | -39.85447 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba262e51-07f2-3e64-a0f6-7cbf6eb37fc8 | -17.86345 | -39.84942 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b67f4cd-f4e0-3f64-9d3b-5f0cf8d490e7 | -17.85606 | -39.85032 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6a72da61-cf76-3c11-a29c-283bde35d5ce | -21.19277 | -44.93671 | 2025-03-25 04:34:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f012087b-a077-38b6-af21-f75284faed9c | -23.40288 | -46.55837 | 2025-03-25 04:34:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39750545-1b91-3bcd-9baf-e0476e1eeb9e | -21.10421 | -56.04004 | 2025-03-25 04:34:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7715cfa8-6304-3634-8ec1-d670dc6e18e1 | -17.55316 | -40.63821 | 2025-03-25 04:34:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc378ad1-30e5-3768-a0c3-3a58d71958c8 | -23.59349 | -47.44031 | 2025-03-25 04:34:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8fbb81ef-b171-31d5-8078-79e17be9f569 | -17.86387 | -39.84525 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 10f1b69b-0dc6-36c0-ae47-da16059c7a9a | -17.86878 | -39.85411 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8a86c00-f659-3bd7-a857-eaed7efcae20 | -17.86707 | -39.85569 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e63ba26f-b064-3fd2-8cf9-32d076104e8f | -22.89168 | -53.51192 | 2025-03-25 04:34:00 | NOAA-20 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 40beab8d-a614-39db-8f21-fcfb08e63fc4 | -22.20771 | -56.97209 | 2025-03-25 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87827110-261c-3f7b-8f2c-0fd080b8954c | -17.86755 | -39.8665 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 2ffb0d70-ba4c-3f85-ab93-c178910f554f | -22.78399 | -43.75629 | 2025-03-25 04:34:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c2d4b46d-f693-3851-a2c6-fdd884ba3899 | -23.33981 | -46.77203 | 2025-03-25 04:34:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5ade3fba-0477-304d-8e0b-4089c67d5e64 | -21.13103 | -47.80157 | 2025-03-25 04:34:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98ef17e7-3907-38cb-bf29-757183bd3105 | -17.55818 | -40.64245 | 2025-03-25 04:34:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4548c2b1-c87f-3340-8183-5c09393e5568 | -17.86619 | -39.86391 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| ac548f68-22f6-33d3-a54b-052b05097724 | -17.86134 | -39.85517 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ccfe5018-621b-3b08-870e-0cd783925c91 | -17.86796 | -39.86237 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| ebe82114-8370-30d8-ac44-ae10a0b51d06 | -17.8696 | -39.84587 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 63bfc5af-b5f2-30ed-82d3-2d6de330f173 | -17.86304 | -39.85363 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b03f05ee-5981-3e7c-b007-8d9b89232917 | -17.86837 | -39.85824 | 2025-03-25 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 46e7d426-ae14-3b16-bff4-a45308cf9380 | -17.55859 | -40.63873 | 2025-03-25 04:34:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9e51d04-dde3-3025-b682-860597559c21 | -25.34717 | -51.47351 | 2025-03-25 04:36:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 782abbb5-0271-337f-a8a3-2cba3ce3acb4 | -27.13881 | -52.09336 | 2025-03-25 04:36:00 | NOAA-20 | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 812a4cba-ff76-3809-b02b-a112ca7dc3d4 | -26.46658 | -53.35628 | 2025-03-25 04:36:00 | NOAA-20 | PALMA SOLA | SANTA CATARINA | Brasil | 4212007 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9903020b-138f-3a30-80ac-0dc15d198dc9 | -24.24149 | -50.74083 | 2025-03-25 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5269df0f-4d41-36fe-9d26-d4e1f6aac672 | -24.92418 | -51.15821 | 2025-03-25 04:36:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e3ae8a04-5377-3298-aa76-60178214482d | -25.3505 | -51.47412 | 2025-03-25 04:36:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3dd36ef3-671b-3819-b301-c55f7d089502 | -23.2633 | -54.98765 | 2025-03-25 04:36:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 47e6c156-7b42-3000-ba9a-83ea4d6267c4 | -27.13822 | -52.09725 | 2025-03-25 04:36:00 | NOAA-20 | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74ecdeb4-04df-3d8d-a7c6-12f4ff44ab10 | -23.56306 | -54.50916 | 2025-03-25 04:36:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e51ee46e-051b-3e26-bd65-c36343fd0367 | -25.33358 | -52.58585 | 2025-03-25 04:36:00 | NOAA-20 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 794c4f4e-30b6-352b-a4ee-ec049a0ec7e1 | -17.86223 | -39.87106 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c63cfa04-ef24-3d6c-80a2-6437455eaafa | -17.86497 | -39.85258 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.0 |
| 03b26020-6cea-3ad0-ba6b-de349728ad3b | -17.85585 | -39.84439 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 4596d7ee-89b5-3be7-b99c-a8d5e5c133c2 | -17.8636 | -39.86182 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| d919ec83-8299-343b-a060-6040c46231b7 | -17.8531 | -39.86285 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 620a33d1-8b39-35cb-afe5-9ec3b621e3e1 | -17.84701 | -39.84298 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 9cdee3d9-b3de-37c7-892a-d1192749baf5 | -17.85447 | -39.85362 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 132.8 |
| 79627378-57d9-3dbd-b408-892aa9fea722 | -17.84563 | -39.85221 | 2025-03-25 05:04:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 77213e4e-c4f5-3676-84fa-9f1d7fbda7a0 | 2.3102 | -60.24157 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06bd4424-ec5c-3ff8-9fe2-8005098e97c3 | 4.25639 | -60.8898 | 2025-03-25 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77e4108c-b83c-3aca-a902-4eefdd97343f | 3.61411 | -60.76362 | 2025-03-25 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ed2a983-5d75-3e69-af2d-9eeafe268729 | 3.03829 | -60.14604 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 922ed540-2268-30dd-be14-62455daf7b4e | 4.07119 | -61.58107 | 2025-03-25 05:21:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75a566f9-73bc-3223-bf82-cd7fcce14f99 | 2.47614 | -60.61492 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89dc4fc4-3689-3c6f-8664-7184dd2074f5 | 3.9796 | -60.08131 | 2025-03-25 05:21:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 712ae948-c905-3d3f-81e8-ded1dd7e0d88 | 2.89492 | -60.46438 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e17c3c30-b558-3692-b0c0-c36a91fd8946 | 3.28441 | -61.09843 | 2025-03-25 05:21:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe7087dc-44d1-3d7d-8eec-b55353540396 | 2.31358 | -60.24102 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5adcbaf0-c1c3-3df9-8e3f-7b4454145f35 | 2.90862 | -60.4623 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 78993ec7-445a-373e-b280-81f7cd19b503 | 2.82746 | -60.43638 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce626576-ed58-3556-b95b-e3bf1d4cbe45 | 3.98928 | -60.07629 | 2025-03-25 05:21:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2038bda9-6671-32de-b93f-148860063045 | 4.06008 | -61.55672 | 2025-03-25 05:21:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ca43a57-d14e-3d4f-9c10-41092f7ba4fa | 2.57805 | -60.27531 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a92dc1-3a80-3a3e-b063-392aacee6f87 | 2.52094 | -60.99158 | 2025-03-25 05:21:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 846d5cc3-faef-387a-9810-724cb0d7d949 | 2.47595 | -60.6146 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cccad40a-3ee4-3fb4-b7e0-141eaed7ef93 | 3.98871 | -60.07263 | 2025-03-25 05:21:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3eae01c-b33d-33c2-add9-e630fb6d54c3 | 4.03035 | -60.06613 | 2025-03-25 05:21:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d309df35-7482-3b4e-bb40-a213dae89d86 | 4.06735 | -61.5556 | 2025-03-25 05:21:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b4e11021-95eb-310c-9b32-168787f8495e | 2.24181 | -60.71075 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 985e6a03-d870-33b4-bc0d-0ef405719a75 | 4.05944 | -61.55251 | 2025-03-25 05:21:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f9fa2cd-d377-3a5d-bb73-cdbef6e0d0d0 | 2.89835 | -60.46386 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 48f2e7a1-3c4d-3777-96ad-d4d35592a235 | 2.932 | -60.43217 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c75bce65-0205-3214-b68b-ec433ec2967f | 2.93257 | -60.43588 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d164b1-a5e5-3f1f-ab00-9231fea05243 | 2.27525 | -61.22596 | 2025-03-25 05:21:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f571426c-074e-3fef-9da7-d9e8ac833701 | 3.3227 | -60.09902 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a93d3e2-faad-39bd-8d25-0868aceb53a5 | 2.91034 | -60.42786 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| abfe25bc-ef08-3318-b702-3a4bb33c5df5 | 2.47555 | -60.61118 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b3086a8-8794-3250-b273-dd10fb08d5df | 2.70186 | -60.08238 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff6e9ce2-9636-3a3b-a1f1-428ad895185f | 2.90407 | -60.43262 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README6.md)
