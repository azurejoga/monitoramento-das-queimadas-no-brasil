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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 587ae3f3-0e7a-31bb-9a76-9fb8fd50b49d | -3.4003 | -61.3087 | 2026-09-04 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4746a452-5fa4-3769-8549-201d37ef9eca | -3.3871 | -59.3883 | 2026-09-04 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 96674f0f-9cfc-3432-8b96-44bf04aacf74 | -3.4002 | -61.3276 | 2026-09-04 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7d5eeff4-765c-3727-baed-1628aa7ca638 | -19.1543 | -57.377 | 2026-09-04 16:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| 9b763f16-f2da-3c7c-b52c-0aaaecfb5ea3 | -14.1363 | -58.8577 | 2026-09-04 16:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 754b0e42-2f3e-3778-854f-0063dd5ae736 | -3.4185 | -61.3273 | 2026-09-04 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0b6e1995-968d-3fad-a796-cb74393c9387 | -5.565 | -60.1739 | 2026-09-04 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 143.3 |
| f81a4ce2-5a2b-3eea-b80a-70414c4a0cfc | -14.1172 | -58.8594 | 2026-09-04 16:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 09e83521-18f5-337d-9d43-a6ca16a8c701 | -3.4003 | -61.3087 | 2026-09-04 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| b58f9752-9c21-3ae6-a574-5618e6430175 | -3.1633 | -61.1238 | 2026-09-04 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 152a0483-de7f-3e33-a150-8c5574d0c62d | -3.7646 | -61.736 | 2026-09-04 16:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| bfcb2f2c-2df9-30be-9bcf-460e21dda3f3 | -3.1449 | -61.1808 | 2026-09-04 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6c7fd681-be98-3573-9261-69e6d058cdbf | -9.0983 | -65.4717 | 2026-09-04 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 568dc90b-0306-37b3-879c-106982a4ad95 | -3.4002 | -61.3276 | 2026-09-04 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| a312bb82-6006-3e92-b595-b5d02f379775 | -19.1347 | -57.3589 | 2026-09-04 16:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 270.8 |
| 21cb08ff-8a3b-3c91-a1a2-4987d3f26ffb | -3.2181 | -61.1418 | 2026-09-04 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a18b998f-4b6a-3c55-8a2a-9f75eef9d943 | -3.3871 | -59.3883 | 2026-09-04 16:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 457651b6-e793-3c0a-9fb7-84489041fba0 | -9.0797 | -65.491 | 2026-09-04 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 968ef9d9-152e-30c8-acfa-affb697969ed | -8.631 | -66.5473 | 2026-09-04 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0fee499f-b0f7-3246-9cd0-a931c70c270c | -11.2126 | -46.1066 | 2026-09-04 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 51ae72bf-3540-3c0e-81e2-7706c9208a9d | -3.1633 | -61.1238 | 2026-09-04 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 5d9812cb-5d2a-3ad6-82b6-6185f81599b2 | -3.2181 | -61.1418 | 2026-09-04 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| af01b0e0-13ed-343e-9d62-303815343bd7 | -3.9363 | -59.3381 | 2026-09-04 16:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 2e19b976-d5ee-3103-8f6e-4a9060cd7971 | -3.4003 | -61.3087 | 2026-09-04 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 5a7fbe42-d8a0-309c-88ae-7b5bbdf9f52a | -19.0751 | -57.346 | 2026-09-04 16:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.4 |
| 7c1c672b-6cd2-3d3d-b26f-ba682552816e | -20.8776 | -57.7043 | 2026-09-04 16:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 16773714-b1c9-3e5b-ae0e-121e2ac04f4e | -8.5555 | -66.9574 | 2026-09-04 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c49729c4-966c-3f28-a712-671356e71dd0 | -3.4185 | -61.3273 | 2026-09-04 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9c7b6b31-35e9-3888-9387-bf3aed4217b2 | -14.1363 | -58.8577 | 2026-09-04 16:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 75e613ce-e862-3bfd-a749-916603bef733 | -3.7462 | -61.7552 | 2026-09-04 16:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 6e28be11-2070-3fbb-8a53-3d58099f8865 | -8.631 | -66.5473 | 2026-09-04 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2cd165f5-bf65-36ad-8bd5-ae4972e00abc | -19.0944 | -57.3849 | 2026-09-04 16:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.0 |
| 254b19dd-1906-3e04-84da-28eceaa87196 | -3.0902 | -61.1628 | 2026-09-04 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| cf8695bd-192f-388b-ad35-223a3006aefb | -3.7828 | -61.7545 | 2026-09-04 16:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 188.5 |
| 09f1aa28-bb1b-3e48-adb7-a59dd255a9a1 | -14.1172 | -58.8594 | 2026-09-04 16:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 652ca1eb-6ea1-3129-97b3-2b956357f863 | -3.1998 | -61.161 | 2026-09-04 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5d02f2c6-dcc5-36e3-878f-b9f5a2745b9c | -3.218 | -61.1607 | 2026-09-04 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 73f9a2de-5867-38e0-946e-01a805e79bdd | -14.1366 | -58.8378 | 2026-09-04 16:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 53df3cef-9151-3c9b-a956-704f453b31cd | -3.1449 | -61.1808 | 2026-09-04 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |


