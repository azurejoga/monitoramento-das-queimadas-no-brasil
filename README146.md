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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87473181-30c6-361c-9ac4-a09c3185965a | -17.10501 | -56.81059 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fdec62d2-4688-3183-8828-4bb0d11ed30f | -17.10246 | -56.79712 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 759ac8af-0c64-3630-9368-6b4f9ea349a0 | -17.10208 | -56.80049 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 45bf4c79-1039-39e2-b10b-98f48c8f7e3a | -17.10169 | -56.80386 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ef50fcc9-1ad3-3ea7-b851-6c48946ff9ed | -17.10131 | -56.80724 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 398a3f2a-de1b-3c3a-b4de-be9d935c5558 | -17.10053 | -56.814 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| adbb8f50-a541-31fb-a6a6-aa8a701faac6 | -17.10015 | -56.81739 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8ad1dac2-80a8-3571-a2df-5266ae908d81 | -17.09715 | -56.79646 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9d9d3f85-899a-333a-b18c-fb319bfe6b30 | -17.09676 | -56.79983 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4f2ca8ae-32f9-3b87-8dc0-32ae17bb9186 | -17.09638 | -56.80321 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b1758ccb-8460-350b-8d91-0dee87f2d047 | -17.09183 | -56.79582 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f224b924-bb7a-3693-9b79-0ccd93408692 | -17.09145 | -56.7992 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5accd4eb-67c7-39b4-97dc-32832d07544d | -17.09106 | -56.80257 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eac8eabd-e4c9-3b77-8dc2-077d82418ba0 | -17.09068 | -56.80595 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 043f9110-a4e7-30db-8a0d-5f73f6432ea3 | -17.0903 | -56.80935 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3ab93cc7-6b47-3127-97e5-707fe1c55753 | -17.08613 | -56.79855 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1d29d74f-5beb-38d5-9b97-7de5892c75a5 | -17.08575 | -56.80193 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 11d03794-3a1a-3777-9fd8-eeaee464d2dc | -17.08537 | -56.80532 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 009eb1ff-b4a7-3ca9-8933-a383c6038dce | -17.08499 | -56.8087 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c0e35c44-efbc-3878-af72-60182ad3848a | -17.08044 | -56.80128 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b4703c95-0cae-3e87-9665-bd529abca232 | -17.08006 | -56.80466 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a89f1e37-4318-3d94-b494-7c5a5de46268 | -17.07968 | -56.80804 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e96f931c-2976-34a4-98aa-b179e4a21892 | -17.19406 | -57.34929 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bb59fc8c-e1e1-3a71-ac93-45dfe52d15e3 | -17.1937 | -57.35242 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4213decc-c64c-3297-b2e3-3dd0beb7f920 | -17.18857 | -57.35176 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 25aea124-3754-36e4-8181-471f5b651b86 | -17.18344 | -57.35112 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 360b14e5-7855-34c9-ad8a-1f4cba004514 | -17.17831 | -57.35047 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 617892fa-6c14-3697-9e5f-5365cfae6f21 | -17.17214 | -57.3592 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ab0a62f4-ad10-3d49-b1c9-916d2aa54eeb | -17.17179 | -57.36233 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0781cbce-08c7-3926-8899-f1fc936e6268 | -17.16702 | -57.35855 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6e655919-e465-3aa4-931b-8ab7b82cb27d | -17.16667 | -57.36168 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 15ae65dc-eb76-3c30-a600-80534262f0c5 | -17.16662 | -57.40894 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 933b5b47-df4a-371f-b553-a09033780fba | -17.16507 | -57.35848 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3ef14b91-2d41-3ae6-8c09-528bdd6afe17 | -17.1647 | -57.3616 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 78b913b1-3f5c-33aa-8f36-7405af71de05 | -17.16189 | -57.35789 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0d291bc0-b3cd-3b84-9bfa-a0f7198f9d8a | -17.16185 | -57.40522 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 353ccf0b-e357-3d18-a34d-c8414bef6875 | -17.1615 | -57.40832 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9ed1815e-43e1-3a41-8b3f-fc667365dad2 | -17.15994 | -57.35783 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7ca368ae-6a54-3e36-a903-e2f7b3af5e08 | -17.1592 | -57.40814 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 58e928cc-f05c-3e38-a858-5a721703c5a8 | -17.15883 | -57.41124 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f9545ff6-4ef8-355a-a919-5d61d6c1a81a | -17.15847 | -57.41433 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c186a921-afda-36c2-8ff0-5b89f8e0c049 | -17.15676 | -57.35723 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 35d55640-7809-3619-8a76-e27e55e9a846 | -17.15642 | -57.36037 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 01e82c51-4518-377c-85b5-e33da2ef68d6 | -17.15639 | -57.40766 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fd369c9f-c2c9-384e-bcb9-32b1ea39b086 | -17.15608 | -57.36348 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 72178d00-4aec-3960-a7da-bc6155085f77 | -17.15605 | -57.41077 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c8158630-eb20-3829-8bc8-61b3cea8f939 | -17.15574 | -57.3666 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| ef24d725-872d-36cc-b518-c6d7d6dbcb59 | -17.15571 | -57.41386 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 25c76ccb-3cc0-3eb8-b303-a102364e0015 | -17.15445 | -57.36031 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 84f82d2d-b93c-3e93-a75e-00d179b75206 | -17.15409 | -57.40749 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 846a0a40-7167-3132-bf27-b89185e5b145 | -17.15409 | -57.36341 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5b67132f-28ad-39f5-abee-b2347c7a1f13 | -17.15373 | -57.4106 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9d39a411-1100-3a2b-8510-f0d9f11f20b1 | -17.15372 | -57.36653 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5750be84-7dfd-34a1-af1d-f5959f9e3c98 | -17.15336 | -57.4137 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2f6ae189-c6ac-345e-8fe6-445ecf1dfddd | -17.153 | -57.41677 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d00fbbee-c39f-3b1c-9855-322f8402630b | -17.15095 | -57.36283 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 15cb98a5-1d17-32b5-a8c4-396f90726c58 | -17.1506 | -57.41319 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d9a6c37d-922d-3851-9e25-2df76b32f553 | -17.15026 | -57.41628 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fd5d2169-edb2-3151-b6a5-777dc2b07654 | -17.14826 | -57.41302 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 29ae9061-a9f1-3039-b633-7a3594e9914e | -17.1479 | -57.41612 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4d6ceb16-19ea-3a76-98bf-3205db671f2a | -17.14584 | -57.40942 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9e073c83-076f-3143-abe6-84d99ea7fcfa | -17.1455 | -57.41251 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 430ee3fe-4a1c-30db-92f6-150df77e6155 | -17.14516 | -57.41562 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4f8c688e-bc8d-3fda-8bc9-786ae53d7cb3 | -17.14482 | -57.41872 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a77d6b8b-3674-32b1-893c-2eee60d9c6d7 | -17.14448 | -57.42181 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ec808a16-865f-3e7b-a64c-afd63cea3438 | -17.14414 | -57.42491 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 471da419-685f-333c-bf68-08c66664ca60 | -17.14279 | -57.41547 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8d10425d-7f98-35aa-bc56-7dbb1b3819ac | -17.14243 | -57.41857 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 332a8949-7f5b-308a-948c-03f0287fbfe4 | -17.14207 | -57.42166 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8d5c0c69-e4ed-3ca0-aac0-edf8489b4f2f | -17.1417 | -57.42476 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ca34c2aa-3025-3dcc-983a-95c73ad8b532 | -17.13733 | -57.41794 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c33efeeb-6a99-3171-967a-e3822fe49866 | -17.13696 | -57.42102 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 75926daa-2b78-3393-b8bb-2956cc40972d | -17.1366 | -57.42413 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 85ffd970-77e6-328c-9916-b9919f0ec7b6 | -17.07475 | -56.804 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4f0da565-283b-3861-9957-ed1f53362bbf | -17.07437 | -56.80739 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3f04b0d0-6579-3c26-ab65-d11efe821389 | -17.07398 | -56.81078 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 198e2323-2c4f-397c-aeb7-44edf6589ae3 | -17.06905 | -56.80674 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0188cd88-f484-3eb7-be35-60308259b950 | -17.06868 | -56.81012 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6aae76e1-982f-3eec-b08b-c1760c35cb16 | -17.05806 | -56.80883 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 002e7fea-cdaf-3e03-ac26-40abb6d589cd | -17.05349 | -56.80144 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d4e828a5-2d85-3c3e-92e7-36afb4bec74c | -17.04819 | -56.80076 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2090eeda-e6e4-3998-a11e-8264ab363bca | -17.04744 | -56.80753 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d9b5bc8c-f8ea-3acd-b443-6741acff9844 | -17.04706 | -56.81091 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 56adb846-e13f-34a8-b546-0afdb611d531 | -17.04325 | -56.79673 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5d592aea-f43d-346b-b328-76bf44682960 | -17.0425 | -56.80349 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b958ce9e-8cd6-361e-8917-ba67e852a891 | -17.04213 | -56.80687 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 49b2b82e-e35f-3bb3-a602-1b8889a2f561 | -17.04176 | -56.81026 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4934280a-4aea-343f-ac5e-03e33138db1d | -17.04138 | -56.81364 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cca0b199-c34a-3b6a-91ee-051d142724bd | -17.03719 | -56.80285 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8563a88f-e16c-3112-aa02-527504dff949 | -17.03645 | -56.8096 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 61fbcfd2-2fb3-3ab0-a042-bdbf3e0f3baa | -17.03608 | -56.81297 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8c87aa52-9d1a-3129-a7be-23dcd006b1a7 | -17.03003 | -56.81906 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5f1536b5-e974-3cef-bc7e-c3e405b9a6c0 | -17.02966 | -56.82244 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b11dde45-6ed2-3542-a513-b27984d18766 | -17.02399 | -56.82515 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f6c2ec87-2d6e-3e17-933e-73921bdbac6b | -17.01906 | -56.82112 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7bb4ec09-f19d-3344-80d2-fa187c1f178e | -17.01869 | -56.8245 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2ff919c8-4fd7-38d1-adac-6613d40639f5 | -17.01508 | -56.82489 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ba0604c3-458b-369e-8a11-759f078a2fae | -17.01339 | -56.82385 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 86713b95-87a7-300d-8013-1fbd66108428 | -17.00315 | -56.81915 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 56b72cfc-6735-3427-a466-8cc41a7967bd | -16.99957 | -56.81958 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README147.md)
