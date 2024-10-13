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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f77eeba2-7acb-307f-acf5-129f884997de | -1.56078 | -55.89754 | 2024-10-13 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feb5bd45-6564-3f5a-8ce8-d21ff34e423d | -4.35788 | -55.56188 | 2024-10-13 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e7935e1-9a6a-35ab-ae5f-5f05dc9a09c0 | -4.32252 | -55.61317 | 2024-10-13 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cf66790-1305-3421-af7b-2ea8f11d29c6 | -4.3192 | -55.61265 | 2024-10-13 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d203997f-2f48-354a-91a0-1753e6664464 | -2.01561 | -56.64328 | 2024-10-13 05:01:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1693ac14-037a-3a58-b85b-91b121348bc3 | -1.80569 | -57.13089 | 2024-10-13 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ddbaeb6-dfa6-3b4f-b2fd-d002bc98a39d | -1.80279 | -57.12645 | 2024-10-13 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7db15952-37ac-3be7-bebb-8c6650861c34 | -1.80217 | -57.13036 | 2024-10-13 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 004afdca-4d9e-36c9-9c46-2685ddf31544 | -1.57349 | -57.60857 | 2024-10-13 05:01:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22d876ad-20ff-3998-b196-df1678e231c9 | -2.45303 | -58.03149 | 2024-10-13 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48cdd7a2-0431-34b3-af82-4ab14f4b4763 | 1.13288 | -59.52721 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef72c9e5-c358-3a4a-8790-5c0a8975d95c | 1.1323 | -59.52338 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad04d155-50b2-33f8-bad3-0914deb1e551 | 1.12868 | -59.52786 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21af5a26-c7ae-31dc-9a7d-39683962346e | 1.1281 | -59.52402 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05dccab8-ab6b-37c1-a9c5-ff4d58c57b65 | 1.12331 | -59.52086 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62a064cc-a23f-366a-a3b5-7588e904e08b | 1.11911 | -59.52151 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88596483-1160-3898-ac3b-f313d241b0c3 | 1.0595 | -59.5534 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df054ef1-14e4-309b-a136-504fc60e0967 | 1.0589 | -59.54952 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8e07b81-823d-37a5-9da6-46a7838ffc10 | 1.03765 | -59.74358 | 2024-10-13 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca581daa-618b-311e-8982-c540b9463c2a | 0.70495 | -60.21792 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37c5b1a3-1e15-3f75-a94e-0c242404a990 | 0.7043 | -60.21373 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cb1f15d-5868-3461-8f01-d2a144c4ab33 | -3.24833 | -60.71605 | 2024-10-13 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca067890-e1e5-383f-b473-f8a6ef8448c6 | -3.24408 | -60.71534 | 2024-10-13 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fc9b605-1407-3580-8d52-7d58a34b3f85 | -3.11284 | -61.10175 | 2024-10-13 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0de404ed-d312-3302-bb42-b7edac5e86e3 | -2.9788 | -60.92889 | 2024-10-13 05:01:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a14d69-4c99-34f3-a3cf-840a8cde78d2 | -3.99636 | -60.39314 | 2024-10-13 05:01:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4db4d735-3e18-31bc-befe-8d163d02d776 | -3.99576 | -60.39681 | 2024-10-13 05:01:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2ac36fb-51d0-3f33-9e4b-13da3f0de538 | -3.81401 | -60.74485 | 2024-10-13 05:01:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c67aada3-49d3-392e-a868-a5ef25c6ed85 | -1.51232 | -61.58963 | 2024-10-13 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b547e3e0-5218-3a1d-a5a8-612909a43a3e | 2.58193 | -60.69335 | 2024-10-13 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa16385a-1454-30fa-920a-05c89ab03668 | 2.57943 | -60.69239 | 2024-10-13 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae3faf83-cfdf-3696-a63c-9223ed150d52 | 0.86369 | -60.61382 | 2024-10-13 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11eaca27-0584-3f6c-aff4-ec3a14d4839c | -1.93249 | -61.7409 | 2024-10-13 05:01:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b471419-ba09-3f50-a7c7-33db43ffdacb | -1.92783 | -61.74014 | 2024-10-13 05:01:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cde901c9-4db6-3522-816a-d9954d0862af | -1.92704 | -61.74499 | 2024-10-13 05:01:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95b0c851-1f53-327b-812e-32f86dbf5a63 | -1.92316 | -61.73938 | 2024-10-13 05:01:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36e59790-49e0-318d-82ea-9f6d556c205a | -1.5216 | -61.59118 | 2024-10-13 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 252731dd-4f08-37bc-8218-f96655b89060 | -1.51696 | -61.5904 | 2024-10-13 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 104912e8-26b2-3f00-a312-029255bff4f6 | -1.4883 | -61.5907 | 2024-10-13 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0df36342-193f-31fe-989f-fb6df23ff590 | -3.08653 | -61.69196 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 82946729-7a0e-383c-b3b3-358396a23900 | -3.05135 | -61.67959 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dfb0214b-b57c-35ed-93e4-8d32b7edcffc | -3.05061 | -61.6842 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94f26cf8-4a9f-3c78-bb74-6b1d3d6f1fe2 | -3.04679 | -61.67885 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 92429beb-e907-3b66-a9c9-0b80d7cf309d | -3.04298 | -61.67344 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3ef74cf-0b5f-321a-8d1d-459c5b45a40a | -3.03767 | -61.67732 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45e503df-c4c6-3414-9e82-aa841b451341 | -3.00253 | -61.41157 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e814225b-917b-33e7-9dda-6d2d5d2bcee7 | -3.00002 | -61.4133 | 2024-10-13 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e88b6b63-e498-3688-8907-fd279a5682b1 | -9.45874 | -67.14644 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23c50921-33db-34aa-926e-bc8edcaac5cd | -9.45285 | -67.14531 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61acfb56-f884-3caa-bb3d-8bb2699a37fb | -10.50691 | -42.50853 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| f67c9979-d148-3f0d-92ba-7c8f1527a0a3 | -10.50609 | -42.51575 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| f82c9998-f695-3935-91c5-f67ab40f4c30 | -10.50484 | -42.50959 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 9c0d733c-a704-3b53-b9cd-0c142cd77037 | -10.50398 | -42.51681 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 42ff6ba9-b7e7-38a8-abb5-07b536d13737 | -10.50048 | -42.50027 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f574020c-fa27-364f-bd01-72314b190a86 | -10.49967 | -42.50748 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 52133afd-d95e-31f1-b0b6-ef2d76232ac0 | -10.49885 | -42.51474 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a6f5f55c-26cd-35c7-8e51-813b07160c17 | -10.49846 | -42.50139 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 563cbb07-121d-3ba6-a098-99f681f5b703 | -10.4976 | -42.5086 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9d568150-e48b-3c89-a0ab-d46e4f6896b0 | -10.49674 | -42.51585 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7a9d0086-9494-3b34-ac47-bcc03a2b31e7 | -10.49161 | -42.51379 | 2024-10-13 05:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 94d2682a-14f7-3f84-af85-6b8d1e9e8d20 | -7.73619 | -43.30131 | 2024-10-13 05:04:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d169e67-c472-3320-94c7-e0cd0495a80e | -7.7295 | -43.30029 | 2024-10-13 05:04:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fdb986f1-2c4d-3dde-8965-8f27de573ccf | -7.72282 | -43.29921 | 2024-10-13 05:04:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 284f853f-f4ae-3c53-b2a1-c677081efb8b | -7.70873 | -43.19618 | 2024-10-13 05:04:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73659962-4d57-3bc9-8687-c8d17288b8c2 | -7.70795 | -43.2023 | 2024-10-13 05:04:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 167f926b-2203-3e39-8097-b0baf43b4ef7 | -7.7072 | -43.20816 | 2024-10-13 05:04:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9cefbece-538f-36b7-91d2-f1855107fb0d | -7.702 | -43.1952 | 2024-10-13 05:04:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38f9ceed-ab18-3fed-8b81-e91b52eb844c | -8.13758 | -43.01777 | 2024-10-13 05:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a7921e51-1ba4-34b6-95a9-4df1353d22e6 | -8.13071 | -43.01701 | 2024-10-13 05:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b23fa128-a742-3145-8d8a-248a34689e3e | -8.12464 | -43.00979 | 2024-10-13 05:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 29aad17c-16f6-3ec0-99a4-a0afbecb71b3 | -9.44985 | -44.14695 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| edb2df34-c9d6-3e3a-b883-da6233222cd7 | -9.44383 | -44.14126 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60762c49-b5cd-37b7-b854-896a570575ab | -9.44339 | -44.14577 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 42b8f547-380d-32a1-a361-b488d272a22f | -9.44318 | -44.14669 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34143bd7-cb14-3398-9ead-075ad5955d3d | -11.11102 | -43.33383 | 2024-10-13 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 11aedf34-a23d-3034-a134-901c9e317e8b | -11.11023 | -43.34055 | 2024-10-13 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7f4801a4-9fb1-3ab5-99b8-6b49cf187390 | -11.10885 | -43.33596 | 2024-10-13 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3e7d69f4-81ab-32b3-a4e0-0fff41b69000 | -11.10811 | -43.34267 | 2024-10-13 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a650266d-0f12-3e9b-a3e8-a79c8ef320ee | -11.10326 | -43.33973 | 2024-10-13 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02a86b7f-ea93-3c80-8bb2-e574e8503d35 | -13.85964 | -44.40646 | 2024-10-13 05:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7438d9d-a2ca-3aca-b1e8-788d6c9baacb | -13.859 | -44.41259 | 2024-10-13 05:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d768362-5eb9-319a-b739-aea2f8eca985 | -7.89837 | -44.61407 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65259f3c-0aa7-31d7-a3c0-f33e18e081e7 | -7.89771 | -44.61902 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92e2c69b-a999-3b46-9763-1c7cb04553f7 | -7.89709 | -44.61544 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a0197c8-18fa-3896-832e-901f1f1cdcf8 | -7.89705 | -44.62392 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fa82143-1b24-31a5-a6a4-4c3bf3e6ef3a | -7.89646 | -44.62039 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62dcfa49-2ef8-3e72-b0d0-d342d623cfc6 | -7.89216 | -44.61329 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4947e00-1511-366c-9dee-d4ab6bcd86e5 | -7.89151 | -44.61819 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0c94d75-9709-3f50-9398-619376781003 | -7.89086 | -44.62305 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3627efbf-cc25-3af5-a949-426bd0958dee | -7.89027 | -44.61951 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a9467b0-762a-37ce-be94-1ec52c0bb86a | -7.27872 | -44.96978 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ee8fb9c-cf53-3ee5-8547-e066f3fb4a19 | -7.27817 | -44.97387 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c9df721-7ca0-35ff-adb8-4aa0485ae540 | -7.27271 | -44.96889 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1dd7374-cb1b-38e1-adb6-a8d284c1d06e | -8.07058 | -44.81535 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 880ba08a-6e00-34c5-8582-44a997190c45 | -8.06988 | -44.8206 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe149106-29f6-3fc4-aa17-600b03581c5f | -8.06442 | -44.81472 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86818708-5559-3a9b-909e-ccf4038f8f1a | -8.06367 | -44.82038 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39c42f0a-6e27-32d4-8a2c-ef573899638b | -8.06291 | -44.82611 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8391ead1-9ff9-3f56-b212-6e2b27fa0679 | -8.06221 | -44.83139 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b23812e1-6574-3df7-bc34-52eb50f82683 | -8.05676 | -44.82546 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README82.md)
