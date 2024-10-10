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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e57db1e1-9845-360e-a383-85b83e0809a6 | -5.18028 | -60.27986 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d72438f-00ae-3c7c-a31d-e2ea0a3870d1 | -5.17966 | -60.28345 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e067f617-f76a-3bfe-8edb-a7c55e6f304c | -6.80377 | -59.34847 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b89e3b7c-2534-31fb-b1f9-721ae82d6569 | -6.80326 | -59.35137 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56a45394-e2d5-30fe-a0ba-fdcc74f44720 | -6.79878 | -59.34748 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd8bc8bc-2b6c-326c-a8c1-ac52701b9136 | -6.79827 | -59.3504 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd542228-2c7d-3853-b04b-a82a737b0763 | -6.79801 | -59.14999 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af6cb0cf-b064-3f17-a958-827685bc44fb | -6.78419 | -59.31417 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 801dcec9-3e86-3c28-bc7b-16f71de29d47 | -6.78341 | -59.31791 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57398ef5-74e9-3cf2-99d6-d2da94ed1216 | -6.78225 | -59.32558 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc091a64-d584-3db0-baf3-498d8644e1ff | -6.78215 | -60.05069 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c0756e1-1fb3-3a9d-8c87-4bfc8d341484 | -6.78189 | -59.32646 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca47a51-c295-3741-937b-6ea346216ba5 | -6.78156 | -60.05402 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bbb2874-a13a-3520-894d-86b298362ee2 | -6.77996 | -59.30841 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97d9789d-2a51-3d79-b651-b58d5296a8ef | -6.7792 | -59.31323 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab2720d8-63f9-394c-b3cb-b166753903cc | -6.77894 | -59.31413 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 64afc71f-8787-36ca-84f2-3f278dc32d06 | -6.77776 | -59.32172 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ec818aa-5386-305f-a44d-112447958289 | -6.77753 | -60.04625 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2fbd3f05-7cd2-32fc-89b9-aa702b092945 | -6.77726 | -59.32462 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 062700b4-7a04-3d2f-a3b8-6f3f92f50560 | -6.77694 | -60.04957 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fa940e2a-b7a3-3673-889b-dd794c16a858 | -6.77691 | -59.32551 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc60882c-fbb9-3809-910e-5c6e30261ca0 | -6.77634 | -60.05289 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0be3934a-9d39-3b6d-9b4d-602d470175ea | -6.77575 | -60.05622 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2db6c76b-f0a3-31b6-8525-8c9e3239c556 | -6.77374 | -59.31512 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 80ad0159-a9bb-3586-9017-80160fbbd6f9 | -6.77345 | -59.31603 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d713902f-0876-312c-a0ea-7cb4cc26eef1 | -6.77276 | -59.32081 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a7b4b8f4-888f-3287-b261-a8ca1544bd3e | -6.77227 | -59.3237 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9296efeb-ff40-36d1-b224-1d284140a513 | -6.77178 | -59.32659 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a3ba11e9-f5cb-3abf-b0ab-6a1e4de0b379 | -6.77171 | -60.04853 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4526f0b2-1a1d-3c31-a783-6a8e1e713b17 | -6.7714 | -59.3275 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e21007f-1511-3a87-a80b-5935e9d48f00 | -6.77112 | -60.05183 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2132028b-602b-360b-b6ec-735eb1eee81b | -6.77052 | -60.05517 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad9fd072-54f6-3f36-8bfb-a5025c82f728 | -6.76993 | -60.05849 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bbd66ff-dc7c-36c3-bff3-9628a107fb38 | -6.76932 | -60.06185 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb022427-a8f6-3b1f-960f-a2c6cee6a576 | -6.76777 | -59.3199 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c6abcee8-ae55-3c34-a4eb-0df5b856c6b7 | -6.76727 | -59.32281 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2ca1a31b-5b95-3532-88da-a9ec2d58bc05 | -6.76627 | -59.32867 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ffcb08c-df6a-3004-819b-b26bde2629d8 | -6.76586 | -60.05096 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b48e39b-ec12-388e-b1ed-45529231d659 | -6.76571 | -60.05318 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1abc0397-1527-3118-b35e-5e5808540483 | -6.76526 | -60.05428 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 841e9943-a4f4-3f53-b70e-896ed6498a36 | -6.76513 | -60.05656 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c038166f-eaf3-33c6-901d-2b62e609ee32 | -6.76466 | -60.05764 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebc1a8e9-1531-38b0-b58f-dbf9ec4f1bbb | -6.76454 | -60.05997 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87ba25b-7975-3ae7-a626-fa983b25c879 | -6.76405 | -60.06103 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7644ba39-998f-3e00-9dd8-e385139342c7 | -6.76278 | -59.31899 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b63a9320-fae1-3065-9cd5-489ecbfa7d8f | -6.76076 | -59.33077 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07410fed-3e7a-3414-b84e-2a320799e1db | -6.76045 | -60.05231 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d15887bc-7105-3318-ab7c-9e2df39a130a | -6.7593 | -60.05897 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d110cab2-dd48-38a0-865f-a10f0d8a406a | -6.75627 | -59.32691 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e391893-b822-3a85-a2fe-14667e6e5662 | -6.75128 | -59.32597 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64105fec-4e59-3a0f-8041-2bcbc044dc99 | -6.75028 | -59.33178 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff98684a-e5df-3def-9c98-4123e4c1e3b5 | -6.74978 | -59.33467 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b29847fc-1bf8-3517-ae33-914f64a7dd34 | -6.74629 | -59.32503 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f04f2d9-9d74-3c1d-a9f8-dc09208f8994 | -6.7418 | -59.29152 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a92bf5c5-860e-378f-b830-f872c8e8d278 | -6.73481 | -59.30215 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ef069e8-eee2-364c-8f81-659b428c55bf | -6.72732 | -59.3156 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9d43e4c-dc74-333a-a62e-e86256818626 | -6.7258 | -59.32433 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eb46a8a-f978-35af-9d9d-2850d03cacbe | -6.72384 | -59.30602 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d67088-3edb-377f-a171-a75e0ba9034e | -6.71986 | -59.29936 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d270bcdc-9bff-36d6-8373-46c50483fec6 | -6.71935 | -59.30223 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b5a4c1-698f-3008-ac0e-a467b8124ed8 | -6.71885 | -59.30512 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0df989a-29cf-345f-9c9d-7c8af9597910 | -6.71703 | -60.11502 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34a99671-3871-3372-afa6-4eb8324f3a7e | -6.71236 | -60.11066 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad1cce8a-5351-37a3-9287-2e2e80048579 | -6.71176 | -60.11407 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e1cbd12-c0ab-3453-b78f-e2bac127e263 | -6.60176 | -60.00303 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74a6c2e5-0f8e-3697-ac5c-26849955ce37 | -6.54781 | -60.00355 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34859ffe-a43b-321f-82af-c8b6f9563c54 | -6.54762 | -60.00307 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c69e05ff-c43e-3d42-ae60-53e417580074 | -6.54668 | -60.01013 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5226962e-05f6-3c83-bc93-2816feece4cc | -6.54644 | -60.00963 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75ab0131-a0e0-348b-9b2c-718b245f0078 | -6.54611 | -60.01342 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 402ee020-e93a-3003-a1c6-c3fba7fcda29 | -6.54585 | -60.01292 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85117868-8ddd-3bd0-8211-60b307c3e94f | -6.54556 | -60.01663 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1241ac0d-00f9-3b57-908c-6ec7d699938c | -6.54527 | -60.01614 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12a99646-2af4-334f-ad94-cde7cb287463 | -6.54501 | -60.01984 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8526e252-5d67-3ca9-81b7-5f0c24e100a8 | -6.5447 | -60.01934 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e1f81c7-8203-3e08-b8e3-7624eae9066a | -6.54311 | -59.99942 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96d66c31-f675-38b6-b890-d1225e3b0519 | -6.54294 | -59.99899 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b9e314c-8c32-3b33-9630-d82a0276ad28 | -6.54254 | -60.00269 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c982b340-180c-31ed-8779-ec188db8e408 | -6.54235 | -60.00224 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22994243-d45e-3a22-91ab-8685356f0978 | -6.54198 | -60.00598 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d0fa9d-b325-3b2c-8d8c-e8c230eee8b5 | -6.54176 | -60.00551 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 658a806d-19a2-3a24-9406-cd501eabc2a6 | -6.54141 | -60.00929 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 926f72e1-5e3a-37b9-aa8b-29be70e8c7cc | -6.54117 | -60.00881 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9199a0b-efd4-3609-91e8-63ffdf674b98 | -6.54084 | -60.01258 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 108f25c8-5565-38a3-a18e-0d50b278d403 | -6.54058 | -60.0121 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be4da1e1-8f41-3e1a-9d9d-d2e3aa2f7521 | -6.54028 | -60.01583 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0415cf2-1dc4-3697-8506-322edbcfa492 | -6.53999 | -60.01534 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0778d996-d449-3ed6-b2b4-985af18a2b4f | -6.53728 | -60.00185 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2201226e-01ea-3369-b6b6-19b056c7d2e5 | -6.53615 | -60.00836 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e7b2ca3-c005-3188-971d-f03fa756e132 | -6.53559 | -60.01162 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d760cda2-58df-3bab-9bf3-64c46eff3c89 | -6.52718 | -60.06033 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b843e9b0-6161-3bd6-9031-86ee52268a5b | -6.52659 | -60.06375 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98527bd6-1322-367f-9b68-c60209b1d2cb | -6.52247 | -60.05613 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1dbfe425-7c5d-3047-9e3b-ea14ca4849a4 | -6.52188 | -60.05956 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d70e240-4b00-354d-82d8-508aa205f164 | -6.52128 | -60.06301 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7ac88d9-1406-3cb8-861c-09c52d6355db | -6.51718 | -60.05531 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b45c5d50-4c95-3606-bd8a-22f5142e83e8 | -6.5166 | -60.05869 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f75ff72e-35fd-3fc5-8c27-aa5d0b9e6378 | -6.51601 | -60.06209 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d45a6a96-2b8c-3867-b29f-9fde14308f12 | -6.51543 | -60.0654 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e98d25d9-da08-39ea-ae2b-2ae3be76d80f | -6.51074 | -60.06112 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README116.md)
