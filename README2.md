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
| 4fb3f26d-e0e7-3ef5-9396-3f96ca627651 | -7.86661 | -39.09483 | 2026-01-24 03:23:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eeca11eb-15a4-3748-adce-df2a44d48849 | -7.2629 | -43.09035 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 408758dd-aab5-31f1-9d4f-e7b8a74176e8 | -7.2798 | -43.073 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5c6d36a-e127-3221-b245-9bb98c96958a | -5.26509 | -37.72412 | 2026-01-24 03:23:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a6121909-bc78-387f-80b8-05bb4cfb4ab1 | -7.97051 | -36.37514 | 2026-01-24 03:23:00 | NOAA-21 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 04106f97-7869-3b16-8cfa-f5c6b9206a8c | -8.81564 | -35.73809 | 2026-01-24 03:23:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96e73d97-f343-31b2-ae5b-2df6812f46e4 | -3.07056 | -40.10899 | 2026-01-24 03:23:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14eb114a-56f8-3a50-af4a-7ff66a069cbd | -7.27879 | -43.07835 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d57a67ff-85c8-34d5-bf48-69e8e4404ec2 | -3.07125 | -40.10495 | 2026-01-24 03:23:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bea38c04-3883-3f06-ae5a-81be01fdd812 | -4.14973 | -38.48323 | 2026-01-24 03:23:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 65b64060-3bd9-374f-8659-293ffa5c8b28 | -7.25741 | -43.0838 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b4312136-71d4-313b-bd80-e61998bb7710 | -7.2564 | -43.08932 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2575e2e3-1522-37d0-9f42-a97cfea237c7 | -7.26383 | -43.08671 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 69a31f5c-00dc-3823-b63a-2d42df2eaa15 | -7.27034 | -43.0862 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 982c8996-fc97-321f-81d0-e0edfe41a0a3 | -7.26389 | -43.08493 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b74c2b0f-a060-39f7-b606-3d0024637a71 | -5.83449 | -35.75067 | 2026-01-24 03:23:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9ecf8edb-5a94-3ff0-8bc8-377d253ccf68 | -5.83399 | -35.75037 | 2026-01-24 03:23:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f15acc7-1bd8-3565-ac66-1a291d982571 | -4.15022 | -38.48029 | 2026-01-24 03:23:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| daf34e18-5e0b-3bab-b965-05114a85906a | -7.70642 | -35.00901 | 2026-01-24 03:23:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08f22ba6-139d-364b-970f-d54cb748810f | -6.99739 | -42.86289 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9c89bb3f-0723-3285-9869-630992dd5d83 | -7.28627 | -43.07411 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a47ba7e0-a278-371e-9465-44e67681241c | -7.62303 | -35.08744 | 2026-01-24 03:23:00 | NOAA-21 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6871460f-11be-3858-823d-50a5e29d1da0 | -5.26981 | -37.7249 | 2026-01-24 03:23:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 04d6ffc9-5a6e-39ab-9fa1-7bdf5dd51de6 | -7.2628 | -43.09214 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3f9e7cbe-b8ac-3c90-a15a-037e299bf2ff | -6.99642 | -42.86811 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 42eeed02-0281-3a73-bd0f-27aa61ea56d3 | -7.51243 | -35.16885 | 2026-01-24 03:23:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c5fbdb9-9eb4-37b9-9003-2161b1cfc961 | -9.81281 | -38.10603 | 2026-01-24 03:25:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4f97f339-efa9-3ece-8291-2535cbb0c9d4 | -9.28466 | -39.28168 | 2026-01-24 03:25:00 | NOAA-21 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5a630a3-ef9d-36ae-bf1a-38e5a2562e25 | -11.31774 | -39.85852 | 2026-01-24 03:25:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| abf0cd31-8486-3ca8-999b-085e7daebd23 | -9.08268 | -37.0948 | 2026-01-24 03:25:00 | NOAA-21 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b57aa1f0-5fec-330c-8874-8ea0e63024d2 | -9.08249 | -37.09387 | 2026-01-24 03:25:00 | NOAA-21 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7de6452-f5b6-3050-968d-ad46327ef403 | -11.56136 | -37.82694 | 2026-01-24 03:25:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3ea2a6ee-ade1-31fb-92a8-2f08831bccf8 | -10.09576 | -36.15413 | 2026-01-24 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 21c86407-e7f2-347d-b458-013d7d012e99 | -11.31987 | -39.85624 | 2026-01-24 03:25:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66d48c29-5491-3d64-a86c-5d944b055524 | -10.09183 | -36.15344 | 2026-01-24 03:25:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 9ffd7cbf-6133-348d-ae37-7625d80d733e | -11.56458 | -37.82641 | 2026-01-24 03:25:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 65d05604-9c96-31b9-9092-d64dc4dc55f7 | -12.2185 | -38.94675 | 2026-01-24 03:25:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5f14b96c-11f0-3d01-a060-49105bb14906 | -17.07967 | -39.46315 | 2026-01-24 03:27:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86a67126-2fd0-33b7-b8b2-c9aecd04fe3a | -20.45492 | -48.68975 | 2026-01-24 03:27:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cd24ce0c-9414-3e5b-b400-582c2f261660 | -21.14252 | -48.6678 | 2026-01-24 03:27:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9517f4d2-d061-30c9-b354-f30c4fe104b6 | -20.45374 | -48.6825 | 2026-01-24 03:27:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f8efa141-b2c1-34a0-b2d3-03cb4d64365a | -21.14124 | -48.66767 | 2026-01-24 03:27:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e2eebf73-dfd3-3e66-a32b-c0df9a58e4dc | -21.13579 | -48.66534 | 2026-01-24 03:27:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a09c4342-3fa8-3d81-8917-115e5d7d9d69 | -20.45661 | -48.68294 | 2026-01-24 03:27:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 11686e27-7cee-3077-b5b2-496c9e2641c4 | -16.7282 | -39.61253 | 2026-01-24 03:27:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ae9e9aa-14db-35b0-b270-90d79334b2b0 | -22.8331 | -48.65231 | 2026-01-24 03:29:00 | NOAA-21 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8a094a2-5fa8-3d30-9f4b-0e78c4f873d9 | -22.03429 | -49.50844 | 2026-01-24 03:29:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2cdc92cb-e0a7-31a8-b659-c3a5e4e38716 | -22.83972 | -48.65426 | 2026-01-24 03:29:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ede96e1-3670-3b83-ae39-1f7b12189ed4 | -30.04694 | -50.75934 | 2026-01-24 03:32:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| afbf8b8f-a3d3-36ae-a46a-f4ce17a9ce44 | -30.04869 | -50.75307 | 2026-01-24 03:32:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 92ac8250-cffc-3b96-b2ad-b426de23a437 | -30.04711 | -50.75811 | 2026-01-24 03:32:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 0d906582-c134-3591-94ea-a3155b6f9012 | -7.27943 | -37.23131 | 2026-01-24 03:53:00 | NPP-375D | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| de804d9a-8423-3685-af91-0fe4d3b232c2 | -4.86588 | -39.00572 | 2026-01-24 03:53:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 802a8e9e-2c7b-3b69-8825-e97c55ea562e | -5.84191 | -35.64359 | 2026-01-24 03:53:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3cc22578-3d0d-3511-bdef-be248ece1f4f | -5.77352 | -38.68624 | 2026-01-24 03:53:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 32c3ab0a-a947-3414-a91f-642201b81515 | -7.62169 | -35.09165 | 2026-01-24 03:53:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3526311f-5246-3fe1-a60f-a907f9baa578 | -7.62573 | -35.08837 | 2026-01-24 03:53:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| a057a7cb-e4e9-37ad-b065-6b44851370ec | -8.05484 | -36.15334 | 2026-01-24 03:53:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aae6a280-4974-3232-a6b3-53e5f9371698 | -4.28989 | -38.05614 | 2026-01-24 03:53:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e1367c9-e89c-3556-9ecd-df9987c7eb35 | -7.8661 | -39.09235 | 2026-01-24 03:53:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 714c4e8d-4fe9-3665-addb-d0a635e76ce8 | -2.98826 | -40.29525 | 2026-01-24 03:53:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0bb7f386-18c8-3129-9480-ad766b3c1737 | -5.86082 | -39.63399 | 2026-01-24 03:53:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 582f910d-5bce-3852-b09a-c98117f2a921 | -7.8466 | -35.49373 | 2026-01-24 03:53:00 | NPP-375D | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae8f1204-c2be-3d70-9949-dd4a53bf29f0 | -5.07911 | -39.71312 | 2026-01-24 03:53:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 835ab388-ace8-3f12-a5d9-99eb3473f993 | -5.10042 | -38.29213 | 2026-01-24 03:53:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8172bcd-50eb-39a1-87b0-808be808ace7 | -6.99447 | -42.86613 | 2026-01-24 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1e090bd1-bb63-3ebd-a1fc-392af5ecd632 | -5.6762 | -39.52791 | 2026-01-24 03:53:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7300e1d-0976-3df0-8c03-c1f05006728f | -7.97188 | -36.37708 | 2026-01-24 03:53:00 | NPP-375D | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf303886-19af-3782-b973-91840c61559d | -6.20841 | -39.20919 | 2026-01-24 03:53:00 | NPP-375D | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8d46b66e-773c-3b9f-b66e-f4831390d4e3 | -4.60994 | -38.47348 | 2026-01-24 03:53:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64e7e762-b0f6-3c19-a16d-72f70f68ba77 | -6.99686 | -42.86286 | 2026-01-24 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a7ff35d7-3c33-302e-93ba-e0a7fb7fe56f | -6.31076 | -35.23139 | 2026-01-24 03:53:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fad722e6-131c-3f3c-9dc6-869c8d484a40 | -5.47024 | -37.81768 | 2026-01-24 03:53:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0efa0e60-88f2-3c83-b54c-cb749798479f | -5.77696 | -38.68679 | 2026-01-24 03:53:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d0e6f54-2ccf-3f71-a68b-8f2eeb968494 | -4.9256 | -37.88195 | 2026-01-24 03:53:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 58e2f553-8211-3ce1-b1cb-009331ca3097 | -6.50987 | -39.06002 | 2026-01-24 03:53:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af20acd4-5318-3c94-bd58-412c2c3482f2 | -4.86237 | -39.00516 | 2026-01-24 03:53:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b563dc38-f6f8-3d85-9574-fade0e956fc3 | -7.62919 | -35.08888 | 2026-01-24 03:53:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c8666935-7ffe-3147-8dda-616e2bdd8955 | -7.26058 | -43.08803 | 2026-01-24 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5ea64aa8-8884-3d3c-9b2c-2bc375517a02 | -3.07219 | -40.10564 | 2026-01-24 03:53:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 93a59172-401d-3f94-806f-227ed5c8da90 | -5.26488 | -37.72642 | 2026-01-24 03:53:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8d6bf1fd-23aa-3793-a891-a4d22bf62782 | -7.65648 | -36.58049 | 2026-01-24 03:53:00 | NPP-375D | COXIXOLA | PARAÍBA | Brasil | 2504850 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c39d5d7b-f883-3709-8811-c320373b7d01 | -6.9962 | -42.86682 | 2026-01-24 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b55bc5db-cf62-33fc-bcc8-e90312061051 | -7.26489 | -43.08877 | 2026-01-24 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 177610ee-1ec4-34a6-88ce-30e7944ae002 | -7.28892 | -39.05883 | 2026-01-24 03:53:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0796ad5e-d4d8-36e0-ad41-42a2241672ff | -6.31473 | -35.22829 | 2026-01-24 03:53:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5debb095-f683-3e36-b5ea-5e5ea1114908 | -6.4991 | -38.79967 | 2026-01-24 03:53:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 318ad051-c70c-34b1-8a0e-0e5c1ed6a3ef | -3.06765 | -40.10964 | 2026-01-24 03:53:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e176d8d9-4fa1-35bf-9140-c61c8719207f | -7.25627 | -43.08733 | 2026-01-24 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c470c2ee-a48a-36ac-9334-b1877d246c58 | -5.26824 | -37.72695 | 2026-01-24 03:53:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9934b1b9-c59b-322f-9480-132dd7bd6551 | -5.832 | -35.75113 | 2026-01-24 03:53:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4ac63ac4-3184-32bf-9533-fa0bb0f8bcb8 | -7.27702 | -37.23116 | 2026-01-24 03:53:00 | NPP-375D | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66253a49-8499-3b29-bb42-ea57b915e70c | -9.0645 | -39.92636 | 2026-01-24 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 415b4590-0c3e-3ec4-8ebf-a4d7152a3dc9 | -6.99194 | -42.86606 | 2026-01-24 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dceba46b-dfbb-33cc-8e6d-012b0d9240d8 | -3.0684 | -40.10503 | 2026-01-24 03:53:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 83129775-ee0f-34a9-b2a3-fe7b69593216 | -8.0644 | -35.16152 | 2026-01-24 03:53:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3b957f5-b742-3f35-a413-4853479a40e7 | -3.07144 | -40.11026 | 2026-01-24 03:53:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 24b73e88-bcc3-3374-91ec-193b9421fa2e | -4.24838 | -38.05328 | 2026-01-24 03:53:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42bd8dc3-01a0-3d83-ae4d-048720f6bee4 | -5.09697 | -37.59491 | 2026-01-24 03:53:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45032005-ae8d-3c99-aec5-d93e6f8ce5a3 | -7.86549 | -39.09608 | 2026-01-24 03:53:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
