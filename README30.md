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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc68c823-fcaa-328f-9026-36a5cf6db38c | -18.05053 | -44.96822 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48f0cac1-92d4-3042-8816-c0585b5f934e | -15.99289 | -50.98274 | 2025-10-09 04:02:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5853f7a6-1766-3725-8499-3ea446899f54 | -19.68825 | -44.86981 | 2025-10-09 04:02:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a853e593-03aa-39cf-9f13-0d809b195f3d | -18.41028 | -45.2342 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1ed3de98-8f42-3df2-9f73-e662ebc0dcff | -17.63904 | -47.20323 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 75e93c13-993f-3430-9894-8ff28900703c | -17.99151 | -45.61798 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9d57859e-18e4-3c12-883b-c1f3d65a3b1f | -18.18496 | -47.42897 | 2025-10-09 04:02:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80b3f145-8844-3fe5-b4eb-836633fefa58 | -17.9556 | -45.00279 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74161124-39a3-3f23-adcf-669b7dd1641e | -19.54302 | -44.04016 | 2025-10-09 04:02:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc2ca814-2287-3dac-8312-c7d09c08d25b | -18.05424 | -44.96898 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ef3dd5bd-5de4-3475-aeb9-7f905f5786fa | -18.41576 | -45.22533 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f220a55-35e2-3b30-8d96-cd18c1fabbea | -18.78254 | -44.61344 | 2025-10-09 04:02:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a866ffd3-3474-3bd1-adb8-b4bf625052d0 | -17.34287 | -42.11499 | 2025-10-09 04:02:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 417d9e44-609f-3048-91d5-eb131469e614 | -17.15593 | -43.43187 | 2025-10-09 04:02:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 234a473b-f748-302f-a084-75df84f19b62 | -16.26246 | -48.63012 | 2025-10-09 04:02:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77251670-61e7-3366-b9c7-983b8054972d | -17.53603 | -46.75577 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8e559ac8-71e3-3b9f-80f9-20987ff26dd5 | -17.09472 | -45.48642 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c2da235-2dec-31a1-a8cf-c4e555bafd57 | -17.93049 | -44.60449 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3af2c66a-eefb-3dde-8cf6-d9aeca61546c | -17.22989 | -46.93105 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98291c88-7930-3f4e-9a6b-9f0f8f19343d | -17.38477 | -45.05344 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cfc2ced-b75f-376a-8e90-071ada2232e6 | -17.386 | -45.06854 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f48c680-966a-3508-ab07-459327e68e8e | -20.55643 | -54.65884 | 2025-10-09 04:02:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1b3d406-ba53-38d2-b574-5031b07859bf | -16.2808 | -47.14618 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9ed8332-03fb-3ba9-995c-418353ae02bd | -15.98702 | -50.98279 | 2025-10-09 04:02:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ad64907-34e1-3067-be03-7e17b24bc58d | -18.04055 | -44.45019 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a030cf14-fe5a-36ae-9b37-cc8e0f33e006 | -18.41489 | -45.23019 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aef7878e-2a38-3759-bf12-4bec0dc30b07 | -18.78178 | -44.61784 | 2025-10-09 04:02:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 08231e9b-9ded-32d1-97b5-1acd3a418887 | -18.06404 | -44.42263 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dabf1d0b-8bd3-3738-b2d5-1c499f0b8bc1 | -17.97726 | -44.9685 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b387808-b411-3c0e-9f87-989b465c3139 | -17.49408 | -45.3027 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fdd8726-9f71-3fd6-93a7-29415496941d | -18.99226 | -43.08969 | 2025-10-09 04:02:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3628badb-3334-38db-9d9b-d63fc553990a | -17.52831 | -46.75419 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| db620fe6-cc1d-3d87-9772-a548ea543b35 | -17.3946 | -46.88906 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 156de722-4bd7-3fc2-8b62-0961b7067585 | -19.54268 | -44.04139 | 2025-10-09 04:02:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e62d284-bd43-310e-9744-d0b6daf2c16f | -18.04681 | -44.96749 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fbfce11-c755-3be9-874d-0649acc8b878 | -18.64972 | -43.91368 | 2025-10-09 04:02:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15077e3a-47e9-3b6c-bceb-b26b4b3fe0c5 | -17.45719 | -43.38177 | 2025-10-09 04:02:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9977e9dd-39f4-3c88-b20f-7e4c2f2e0721 | -17.26741 | -46.96561 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9e1b64a9-cb84-307d-aa1f-f234652bed68 | -16.70341 | -47.58972 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfee206a-37d8-3445-8018-e23ddb75e817 | -17.46002 | -43.3863 | 2025-10-09 04:02:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 881dd128-a0f1-31ab-9482-38772ac84521 | -18.06454 | -44.48165 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42d83654-5dd4-356b-91ff-9fb77fa69e22 | -18.03394 | -44.97492 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85253747-bd4a-3550-9f44-8cc337cb3617 | -16.42384 | -47.82147 | 2025-10-09 04:02:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52ebfee6-0079-32d1-af5e-512bcc30786e | -16.69719 | -47.59815 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3be0faf2-a132-3eeb-bdd6-995284ab1f4f | -17.63478 | -47.20234 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3b1f66f4-0c81-3e8c-ac9f-17f8179131e1 | -17.37632 | -46.89337 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d48b9e80-2f12-3378-85ae-43c87cad611b | -18.06093 | -44.48081 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba1aadd9-d28a-3437-a415-8469888d975e | -19.71961 | -44.00064 | 2025-10-09 04:02:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90cc7ee7-cfdf-3318-9da3-1c2843cb6095 | -17.57942 | -46.06336 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f3fb7ec-34e4-3cab-a6a0-6033e80d3ed3 | -17.98556 | -44.96523 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1550d8a-5b07-3aed-9dae-14614bc44031 | -16.71133 | -47.60791 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a1e61f5-e8bc-36c0-9896-22af9de5e5eb | -17.9633 | -45.00211 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc4c66da-9502-3bfa-bf8d-2c6b1cab39b9 | -18.24658 | -46.99613 | 2025-10-09 04:02:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1198e5e7-e024-30a6-bb5a-46660ea556d2 | -19.9351 | -44.89057 | 2025-10-09 04:02:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f3a9c7d-abe1-3ba6-8464-52411de482f5 | -18.053 | -44.95422 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a34c73-76a2-3562-8477-e039789d7ed5 | -18.09116 | -44.4585 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcfccd7f-5293-3df4-8e35-edf9478a5c0d | -19.33849 | -43.9032 | 2025-10-09 04:02:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3eac00c-5a77-3b40-b582-8d920bd341e8 | -18.29367 | -45.43258 | 2025-10-09 04:02:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99caaf3d-c004-305b-acc1-1d03ec261c2f | -17.39123 | -46.88362 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23b94665-67be-308d-a2ee-16652c54d6ad | -17.39316 | -46.89152 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e9512490-dddb-387b-9987-67afc36b3bcd | -16.62983 | -45.43426 | 2025-10-09 04:02:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ce11d71-f6bb-3d9f-a45c-8bafba15d79d | -17.52356 | -46.75312 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0134836b-0ced-3da4-8a94-f895a1ac6168 | -17.63826 | -47.20742 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50b70c11-7df0-35d0-98ad-8d48635d2794 | -18.00625 | -44.97882 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75580c8b-5466-37d9-b72b-34970ec1ea71 | -17.46068 | -43.38238 | 2025-10-09 04:02:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe310412-f1b9-3b61-8f51-d71be97cdc23 | -17.57847 | -46.06847 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1353670-ffd8-366a-af8b-29d48e15b711 | -18.16792 | -39.64291 | 2025-10-09 04:02:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 859e051d-6224-35bc-a149-f1d6f09f0054 | -16.69809 | -45.01141 | 2025-10-09 04:02:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 287b987a-033f-3fe7-9008-7bbad272f0c8 | -17.58248 | -46.06916 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab034c88-1c08-3a4a-a547-7931d6201bc7 | -18.54575 | -45.06351 | 2025-10-09 04:02:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a4ca313-d9ab-3247-8b4a-cc63a159d9e2 | -18.83057 | -42.97034 | 2025-10-09 04:02:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6487593b-0431-325f-a2ca-e43e64d20918 | -17.38393 | -45.05819 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78ec3326-0868-37dc-834f-07a74ec22f5b | -19.93871 | -44.8913 | 2025-10-09 04:02:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82573439-b07e-3669-9e39-cfca3c761032 | -17.37119 | -46.66557 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e9135ec-86c9-3ee1-87a1-6ffb75b4431e | -17.65372 | -44.43502 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fb46f76-9c5b-3628-a58d-e9a1e69d089c | -17.39047 | -46.88773 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b318203-259f-3d17-86e6-f97eae70e8e9 | -17.95829 | -44.98667 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fb1afb7e-180d-3739-a0ea-6383eaa36235 | -18.06779 | -44.4213 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89b0910b-8e8c-3ef9-8b95-834137e73081 | -17.63985 | -47.19892 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 942ad260-e41a-361b-a14d-957f8641db1b | -19.71613 | -43.99994 | 2025-10-09 04:02:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b0e6f31-8f76-3f53-9d25-f902b7e7bbc0 | -16.28415 | -47.12873 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cdcca0b-736c-3a68-8e9a-2601a6e1d3e6 | -18.03144 | -44.98899 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 033803c0-b455-30fc-99da-7bb9ec0d0aec | -19.71889 | -44.00483 | 2025-10-09 04:02:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71de6e58-1c97-38d7-9922-8510c912480a | -17.63399 | -47.20652 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ba92a463-9a04-3467-ba40-c609e758088d | -18.05382 | -44.94958 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93aa2fe6-8dc7-3d8d-bbb0-944dd29e6a9e | -17.98674 | -45.62221 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cb88a353-2237-3b45-bda5-43481b9edb72 | -18.04225 | -44.97149 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61f14968-bec0-3966-b9ff-2046164adde0 | -19.74106 | -42.20003 | 2025-10-09 04:02:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 357b7884-b344-3d36-9b4b-bbb5f2c5f74d | -17.37553 | -46.89759 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ddf5d49-9647-3e13-90d4-5897f5867970 | -19.93496 | -44.89278 | 2025-10-09 04:02:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ee5ff90-f718-3271-bc7d-246f4cfa69f6 | -17.39381 | -46.8933 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b532cb8-28cb-3743-a315-614fdd912368 | -16.27382 | -47.13797 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adf294d7-6b4a-33d7-85c8-616936649ea3 | -16.28253 | -47.13721 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a47a308-7a86-3371-ad73-aebdc6a27b31 | -18.08756 | -44.45767 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 172d6a22-cf44-3f25-98a5-d251ff6ae082 | -17.95124 | -45.0048 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f04ee782-7e7f-3cd7-88e7-21dbdfe21a11 | -18.05135 | -44.96354 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dd44e4d-3901-3479-82d9-41fc7973fa15 | -17.53187 | -46.75489 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16c8e285-1bfc-3bb6-9119-a8861305bcdb | -17.33187 | -42.13989 | 2025-10-09 04:02:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 17321a17-b9ff-3510-86ee-d8f88d6666fd | -16.61677 | -46.77686 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58416700-212a-300a-838a-d93f307417c3 | -18.7854 | -44.61856 | 2025-10-09 04:02:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README31.md)
