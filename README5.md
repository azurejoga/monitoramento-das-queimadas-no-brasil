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
| 280668a8-5399-3ab0-a9a6-7c72a6ec0ef5 | -21.2619 | -49.142899 | 2026-08-25 00:32:00 | METOP-B | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1febb018-61a5-32f5-9839-a18add9c5487 | -6.5129 | -55.205601 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0cf42d3-af07-3815-9629-88d296b34c92 | -13.9107 | -54.0233 | 2026-08-25 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdee083d-f568-36cd-ba14-659328a68b7a | -10.4618 | -50.420601 | 2026-08-25 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f45a2a28-85c2-3d66-ad05-e7f6cd058af9 | -10.4642 | -50.430698 | 2026-08-25 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5226a59a-2512-36f3-bc93-fdbb911bbf48 | -6.5153 | -58.292702 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1df67ed-f88a-3265-b83c-0d2a4d71fbc2 | -6.7984 | -59.581699 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9db757b4-c990-36bc-a1cd-c8869b411395 | -6.1872 | -53.469601 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea84ca59-2984-3b38-b627-cc8dad583984 | -6.6276 | -58.4757 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28aa70a5-ded7-370b-81bf-8c75ed5e2bed | -6.8199 | -59.586102 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9083b9d1-20a0-30a1-844b-c235f8d30aca | -17.587799 | -50.8853 | 2026-08-25 00:32:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5616a8dc-a523-33ff-88ee-0bc8725a3c34 | -6.5561 | -56.536499 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40bd36a0-cf45-3468-b7a6-1d41884f2258 | -6.2227 | -55.606701 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 232c778a-8b89-3e5f-b99a-603a5cca34e5 | -6.011 | -57.641998 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d60a093-c479-31a1-a102-5e59195a7f48 | -6.1441 | -57.824001 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dfadb81-b541-3c2c-9c7a-6e99109acacd | -6.6991 | -55.571999 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9a0351-bfe9-37be-a1cc-8147d0c0a8d1 | -3.5442 | -54.4786 | 2026-08-25 00:32:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0495c35a-7eea-3bdc-8add-37319978f087 | -10.474 | -50.428299 | 2026-08-25 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8bb840e8-35d7-37b6-98c8-0799d5651d4c | -6.2109 | -55.463902 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0cd69a1-1512-36fc-ab53-7d2081b8b6c0 | -7.2479 | -45.825699 | 2026-08-25 00:32:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bff4c608-f201-366a-8e23-3543991a7986 | -13.862 | -53.990101 | 2026-08-25 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 654bbfaf-d68b-3619-9855-fd3d53c11efe | -7.0192 | -59.230301 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab81cf7-5117-3d35-9d89-76ac417a9af6 | -6.7217 | -59.4184 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2bf1c88-6ad2-374b-bdb7-e5ef5fcd413c | -6.0869 | -53.392399 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4425a78-72ba-36a3-9200-a7a0e8b62e62 | -5.7926 | -57.5854 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3167ec-d29d-3165-bde6-02e228597be8 | -8.5732 | -54.840698 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b5457fd-407e-30a9-ba28-b57777e1f889 | -4.035 | -48.951401 | 2026-08-25 00:32:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66681b2d-b92e-3603-97d7-e08fbe703ef7 | -17.3123 | -54.905499 | 2026-08-25 00:32:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9357b0e9-61d3-316b-b144-f72025fe45a5 | -7.5445 | -61.332001 | 2026-08-25 00:32:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dac4d76-a8d5-34e2-b0bc-93be741be98c | -6.418 | -54.9244 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77a70453-e622-3874-8cc0-5823fa9fbe55 | -10.9259 | -51.066399 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6dd0df1-7aad-35b4-a720-b7324338382f | -6.1473 | -59.887501 | 2026-08-25 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c909d41d-c45c-364b-9e90-66b304db97ca | -6.322 | -54.729301 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc3b8bb-8e85-3cb4-a404-171c87a09d0d | -5.9752 | -57.6199 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0300989-5e22-3940-9c16-6287c282faa5 | -12.6959 | -48.363899 | 2026-08-25 00:32:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2ae147d-3d3c-3405-8cd9-a76210a1d2e9 | -6.1803 | -55.419701 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4c5213e-9744-3fca-88ac-11884ed26c06 | -6.9587 | -52.795799 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca5ac34-8108-37ef-bd46-130684a652e1 | -10.3424 | -45.041801 | 2026-08-25 00:32:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a7efaf8-9bcc-3b01-bdfe-1e677b989fb2 | -7.3453 | -55.651001 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3d41f1d-2569-3ec0-8566-ac1ec7fea79c | -8.5984 | -54.7244 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa5c82be-389b-31d3-a117-5c9c3a7b2b16 | -8.212 | -54.9743 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f13633f3-61fe-34c1-8fb4-d32fb3cf938a | -6.2473 | -55.397301 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa6b78e-7be5-3c1f-82fb-8baddcdb7e3a | -6.7393 | -59.639999 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c84e8845-7700-3aea-acab-139869268410 | -6.1429 | -57.6805 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 531162d9-7f04-3d59-86a6-3c1ee32797da | -6.6391 | -58.4813 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11ece43c-fb4a-3c38-b795-2e97f80feb01 | -6.3334 | -54.734299 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c24a117f-0060-3179-a600-147072fa9c1d | -12.8694 | -48.479599 | 2026-08-25 00:32:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08b9032c-0810-3bd3-b031-7150b558871d | -6.1454 | -57.922798 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee574c8-853f-3b32-b1ea-55cb520a179d | -13.3398 | -48.169102 | 2026-08-25 00:32:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 87d1da49-1b5f-3221-8f48-0811461d9bff | -6.3513 | -54.7677 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94102c42-cd56-374d-9b92-311966c4140a | -6.2226 | -57.761101 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56b0fb5c-0e90-3b13-886c-cf6446e6598e | -6.4343 | -54.950298 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff20cdc-83cd-36cc-857c-c13ff4ca8892 | -6.1438 | -57.915501 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 272f435e-1c46-3bb5-843c-74d21e0be94d | -16.371099 | -49.897598 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b333d76-c756-39e7-aded-f0d66401d7d1 | -8.5469 | -55.270599 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a09344-8258-31c2-b24e-3e73cb1dfa64 | -6.6087 | -53.330799 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e03ede95-eae1-34b6-8e4e-6424f0e3781f | -15.2377 | -52.7798 | 2026-08-25 00:32:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32ec9609-7439-331e-bc07-64b6fc0ea19e | -6.3317 | -54.7271 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f144ce7-c983-3293-8a84-3c29e9d72e9e | -10.0043 | -46.405602 | 2026-08-25 00:32:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ece3991c-80bc-3739-a95b-5176900ddf6e | -6.7006 | -55.578899 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60cfdbfe-039c-311f-92a8-5fb33b984e9b | -6.7589 | -59.635799 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1ae020a-f555-3ba9-a34c-b1669f9101b1 | -6.0028 | -57.651199 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd9eb3e-0bdb-3b3b-bdc1-4851c22a540e | -11.4137 | -44.4977 | 2026-08-25 00:32:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4864eaf7-c036-342b-9ac2-f2edfa78d591 | -7.4397 | -59.749001 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67a7b8a6-fa3d-3b7e-875a-4250f1ccd145 | -6.2195 | -55.4109 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf67d61-274d-37c1-91b7-e47b806b6f79 | -6.1775 | -57.373901 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57543a5e-2b16-38b3-8933-172ba3d62f6b | -6.1262 | -57.790001 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bee84ac-c525-3c47-bb20-8e8c1f672d23 | -7.2482 | -45.340599 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 916044ef-4c72-35cb-a290-69dc527a579c | -7.4903 | -55.335201 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c343080-f9ec-3ce1-8f79-9960f2e64ffd | -4.0312 | -48.935501 | 2026-08-25 00:32:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67ce56e7-5dcf-3489-81d3-f2259bd69378 | -6.2125 | -55.470798 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff8609ca-4fdb-3cb8-905b-b0a4a7f4798b | -6.7935 | -59.794399 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa6c4fec-0269-3670-9d46-568172ed0c5d | -5.7717 | -57.537998 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96805286-ca91-3ccc-93d7-e60109efca17 | -6.079 | -53.402599 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 243de211-aca9-3996-a143-520d29842ca9 | -6.2489 | -55.404202 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5bddeba-bb19-30a0-a2b2-3e7172167ce4 | -6.1543 | -57.685501 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad445e2-59d4-3d1f-a16e-75867b873459 | -15.3178 | -52.814499 | 2026-08-25 00:32:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 376490be-f3e7-37f7-96f9-04a4252175ea | -16.383101 | -49.904301 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21d4f1b2-62ea-33a3-9799-b3870776152d | -7.2421 | -45.802601 | 2026-08-25 00:32:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f7a3ac1-61db-32f4-a61a-fd98188f3856 | -6.8883 | -59.007599 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 335f8681-cb80-39d5-a554-6566f68cf619 | -6.8705 | -56.837399 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a242a4c-5170-383e-87fa-239d29b78545 | -3.5122 | -48.176498 | 2026-08-25 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48ddd5a3-0f51-3361-aac5-ea5abec58e1b | -6.1768 | -53.5135 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec6d9d8c-7d26-3663-9d3e-bf9738400c59 | -6.147 | -57.930099 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b35d310-030c-38cd-9eb7-12bd3aaa8971 | -14.9136 | -52.624901 | 2026-08-25 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 263ebfa5-2836-3358-9aab-05c6bc59a678 | -9.5208 | -49.262199 | 2026-08-25 00:32:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5911045d-19c3-3df7-9a66-e05875c903bf | -10.3399 | -44.992699 | 2026-08-25 00:32:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64774a23-d14f-39b7-9288-0c9543155d6b | -13.9091 | -54.0163 | 2026-08-25 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0b19e84-7ad0-350c-ab43-71fef102dab5 | -5.7942 | -57.592602 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d36bf7fd-afa6-354c-99f6-ab2fb4663d86 | -6.2321 | -55.4664 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6dfecb-290f-3737-99eb-b167b24e8d5e | -6.1568 | -57.927898 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efd9cb9f-df81-3e21-a122-c75674bc867a | -7.2324 | -45.805099 | 2026-08-25 00:32:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10fe3349-089f-3997-8c6a-4d3f103fb504 | -6.1847 | -53.503502 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96e63561-b761-30e6-92cc-596151c93e28 | -9.4614 | -56.878799 | 2026-08-25 00:32:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de1805cb-c9d7-359d-bb5f-54c5a451f3d5 | -10.3555 | -45.0135 | 2026-08-25 00:32:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e12d2ce2-95c1-3444-979e-7fc30009771d | -6.3579 | -54.751301 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe5ced2-2c05-3bce-9c8a-cb8e45549a10 | -6.7236 | -59.426899 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05757d62-1379-3d6a-a98e-1d85a8392fec | -7.2419 | -45.315601 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4f913c-2100-3615-b687-f266b77e8442 | -10.3303 | -44.9953 | 2026-08-25 00:32:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 98932f97-7067-3fcb-b20f-44849d91fe0b | -6.1374 | -57.840599 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
