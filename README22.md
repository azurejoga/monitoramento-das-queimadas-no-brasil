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
| 82a991a9-b3fe-35fb-853e-f652b9de5dfd | -4.42659 | -44.72771 | 2024-11-26 04:38:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b40309b-15aa-32ac-be60-40ed90a8504d | -2.24976 | -53.46981 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e2e4b3-6271-3617-82d1-db7bbfa0ae52 | -3.66067 | -43.38958 | 2024-11-26 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9040b41-3c74-38eb-90b2-747983117ba7 | -3.24715 | -50.66587 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48559a7e-4e61-3b7f-b172-ac8783558447 | -3.47108 | -47.68483 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7c5a35-c84d-3efa-83b8-c50704244996 | -3.06177 | -53.27678 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a12ce2e7-1e2d-3133-aa45-2261a50ef0b9 | -3.97336 | -48.06753 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3fb4caf7-ce66-3e34-8e05-4bc36a7819b5 | -3.25851 | -50.39786 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff57b057-6ec0-3b32-9dc3-acf74ad24b14 | -4.31274 | -48.6004 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e5a440b-eefb-39a2-ada3-5b4cef2982f2 | -3.83004 | -46.54305 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a030ca2-83f4-31b7-b101-c32eb7eb8b2c | -4.23651 | -48.69823 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35759fb2-31bd-3269-9766-e0e3e58ef476 | -1.72472 | -52.48924 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df2ff557-9158-3d95-80c5-42eeb5d8c1cd | -3.50594 | -50.00618 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e4f0b79-d01e-3c5c-9b6b-768c8046b217 | -3.33026 | -53.72366 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f4590a9-3188-3bd9-bf80-28d50bf06be5 | -3.68435 | -50.22506 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c611fd61-9369-3fbb-940d-a404fd5cb3e1 | -3.17337 | -48.44355 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 110602ba-c605-3c63-96ce-25a8af56ac63 | -2.69953 | -48.65891 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5e71c34-9d36-3ddc-862c-bd81213fcb54 | -1.77987 | -52.73946 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 655efb74-4eba-3054-addb-1b74969e4847 | -6.38833 | -47.08918 | 2024-11-26 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7626fa9-fdcc-39fa-9393-45bbeee6178b | -3.95852 | -46.90392 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63c3a69b-bfe6-340c-8227-68124e5890ac | -4.53711 | -43.29123 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 954f9b57-bc40-39f2-8476-7c1b1f5d5a8c | -3.27298 | -48.75943 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a83c17d-15cb-327a-9c20-db381827d29c | -3.68579 | -49.63879 | 2024-11-26 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d95df9e-8b8b-341d-b587-451145c86996 | -4.29151 | -48.19564 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8247f66-e075-39ef-a065-80d08cce7a00 | -5.73741 | -46.51295 | 2024-11-26 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d98eb9a-35ab-367e-b5dd-69b90e2040cb | -6.18791 | -43.41059 | 2024-11-26 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45fcbaa1-e5d7-3239-9367-2212e663cc09 | -4.94967 | -47.80014 | 2024-11-26 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5310e9ea-0b9e-3869-8fbf-e51d2865e357 | -1.79081 | -52.74621 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac115f96-7d5f-3b4e-b235-68699d5a6799 | -3.1402 | -48.63266 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b76b8184-1d5c-3842-b871-6d90019af7ad | -4.04471 | -48.3242 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd169581-3e46-3a50-a263-227ae2bf1346 | -3.49497 | -49.68462 | 2024-11-26 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bc197ce-b100-3c72-9b8d-a57378afe843 | -2.2213 | -47.72041 | 2024-11-26 04:38:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc0fe832-7e76-3bb7-b65b-e879ea213776 | -4.50856 | -45.2037 | 2024-11-26 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca8dab63-746d-338c-956d-affc28969b3c | -3.50317 | -53.80856 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4de9f60a-c2bf-3e5b-a211-2eef5ffae685 | -1.56286 | -52.00845 | 2024-11-26 04:38:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa1b0f34-5478-3dcc-bb22-ac0a6c86683d | -3.39503 | -50.02187 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9ef4a4c-9690-3152-846b-ff51c9d74b35 | -3.05194 | -44.7433 | 2024-11-26 04:38:00 | NPP-375D | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad361300-3fd3-380f-bb43-9f44e45e9b0a | -2.93389 | -48.82614 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70c801bb-7df5-3eab-97d3-f19571f38571 | -1.57106 | -52.00513 | 2024-11-26 04:38:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6b5aef5-0c87-307f-b0c9-491d09443564 | -2.90012 | -51.57016 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67c6500-5830-334f-992f-4b6cf455d8c4 | -1.92695 | -50.59608 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a42fe4df-b056-3558-a6f7-db6b256ca943 | -6.06967 | -48.02986 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 14b597aa-541f-3573-a0bd-742592796fbf | -3.97445 | -48.06054 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ea69521a-deec-3fac-a084-320b8206d781 | -2.71412 | -47.70404 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed3b033e-5260-3e70-94e7-2d9abd297b1b | -1.47121 | -52.2927 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d88b2fb1-953d-3f30-9c55-a5b46f733b37 | -2.26419 | -50.46177 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d384d3b2-0492-33e0-8671-9f7eaaeb5842 | -4.3151 | -48.65031 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66bf56c4-c463-3814-aab9-17da38639cd5 | -2.80077 | -54.11649 | 2024-11-26 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2fbfdac-898e-39cf-8709-169331c3701b | -2.62938 | -51.76899 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b58393b-5fa1-377d-b5d1-36d331d32fdd | -5.7615 | -47.81392 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40e551b4-95b5-39c6-a6a6-8b5ac562d62f | -4.23705 | -48.69478 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f85a6ef-f5b0-37d7-94a8-64860f3190fc | -2.98285 | -53.35091 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a2b7d48-32fe-3477-88a7-9043b369ad2b | -1.79193 | -52.73824 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaaf569f-6e90-3650-8909-b8dacf738244 | -4.35748 | -48.57549 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c304c8bd-94e5-3c77-8df7-10e647a1bea1 | -3.97067 | -46.73399 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc561b37-f5b4-3e46-809a-3fee814265ef | -2.17274 | -53.80228 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93724f2e-791b-322d-9717-47c2a21aa7da | -3.98785 | -48.08407 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00196d0d-44b2-36b2-b189-0f113e6f94ac | -2.79883 | -53.02342 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a06a556-d64c-3a6f-8895-65674e66da41 | -2.57767 | -48.20861 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 150a50e6-af8a-3064-9c36-e92402500831 | -4.5191 | -49.05439 | 2024-11-26 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6242cf3-1fc6-30cf-895f-1d6a967b909d | -3.59259 | -50.38542 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fbbe38f-c523-3889-87ad-e1555ad34982 | -6.00268 | -46.54798 | 2024-11-26 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20328737-9693-3743-9a12-0b862f4d26bc | -4.24617 | -48.59352 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 225674f8-76dd-3244-8d93-debdf84586a7 | -5.65266 | -46.64254 | 2024-11-26 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00dc2cfa-3004-35e6-be4a-746190ecf2c4 | -3.27793 | -48.7496 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30d9e010-1408-36c0-8f9b-697f85e20fb9 | -3.13765 | -50.56451 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 091a47aa-3455-32b1-bcc7-b1b4803d3a04 | -2.7157 | -46.26223 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0eb74744-a42e-394e-ad2f-7f51a964d345 | -2.36008 | -53.71379 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e69d719e-1adc-3818-864f-37d9e0d38de9 | -4.03342 | -45.54276 | 2024-11-26 04:38:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d983e4f-f79b-3a2c-9644-35fbcbd12fef | -4.23319 | -48.69772 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de38e493-04bc-342a-9ecb-1a5798d4a4ce | -3.9429 | -47.98412 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61aacf0e-c710-3fab-91a3-f1a3b8e08b65 | -1.84132 | -55.3112 | 2024-11-26 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67992d14-885e-3c6c-aa5e-a0dfd2aa5ad3 | -1.63366 | -53.29927 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 243325cc-1ed2-38cd-82c7-8cdb96c75d57 | -3.28113 | -50.01482 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ccce68a-bcd6-3348-a23a-09254684dff2 | -2.70935 | -46.25734 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de6a0076-da7c-3f61-97ae-6d33718bcc39 | -3.27684 | -48.7565 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 844a88c6-88e0-3384-9fa7-528686b501d5 | -4.36834 | -48.50628 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d31ecb1-39cb-3d97-8ac6-06c34e17c11f | -3.58977 | -50.38123 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15c04aa4-d8db-3a99-9483-a3033ef0ad54 | -3.91494 | -42.42199 | 2024-11-26 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 32baf309-11f6-3faa-9e69-5155b04ed7f1 | -3.9878 | -48.06256 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b0a32b01-f3ea-3c82-8357-6851b3dad7ce | -2.81978 | -51.79173 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 867b06d4-d57f-3369-9120-0a4e1f6af43f | -4.3608 | -48.57601 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49bf4b6d-8ebb-39a3-8831-271f7f819bf3 | -3.2957 | -50.36237 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2ef0eec-e987-3348-bb29-e96f68867961 | -4.27388 | -48.61201 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f886a82-3c51-3815-87ac-e3a3c7df80e4 | -3.38762 | -50.09068 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4811fb18-c9fd-39d0-a750-12cf71cc6d12 | -3.4155 | -50.44487 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f8b7a12-0523-3616-8df9-05fa2e61f744 | -2.93995 | -51.29875 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8dadb27-0c5b-31e5-abae-c47fc5be1c06 | -4.53289 | -43.29062 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91319596-3824-3dde-be49-f67ddc5b2401 | -4.25468 | -48.66921 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcaff9c9-1bef-3c96-b30e-c6ef3f4de905 | -2.91924 | -48.72488 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b77e7b7-fc8d-3af4-8803-00ea194a1b3c | -3.97057 | -48.06353 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 482d900a-9d29-31d2-9d2a-07b6b4b80696 | -3.29204 | -50.53931 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd164f03-72b9-34c9-9341-eb6697f6e536 | -1.77674 | -52.73394 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c43111-f1c7-35c1-93a2-45c3e4fd8739 | -1.631 | -53.87579 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d47afaa0-6087-3244-9214-2f60e61c607b | -4.28994 | -48.2275 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d180c9a7-d96c-3bfb-8059-8d6497189759 | -3.80959 | -46.60603 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad93ded-18de-3dbb-bc49-dcd21029e50d | -2.90061 | -49.79089 | 2024-11-26 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8358d8d-d98f-33b9-81e9-03550bf05aa1 | -3.81752 | -47.46994 | 2024-11-26 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfa6c543-fefc-386f-bcab-787961336f92 | -2.25685 | -52.21034 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6588bd28-9b2f-3c68-9281-061c176a0fde | -3.23358 | -50.31506 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
