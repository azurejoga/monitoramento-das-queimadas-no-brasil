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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbcea23f-e669-304e-a3ab-7994f94b1bd6 | -16.99785 | -56.81849 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 76a0814c-c2ea-38ce-a7bf-40cd3e2c766b | -16.99748 | -56.82187 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8b5ef4e4-e204-3cee-83b5-aa91a3165b07 | -16.99466 | -56.81557 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e9d7f477-f00c-30b9-981a-434ff5c28ecd | -16.99051 | -56.80483 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0b041977-9162-39b3-abbf-5cd220d212c0 | -16.98974 | -56.81156 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cd38b497-eb86-3b4c-b504-731634f70650 | -16.98936 | -56.81492 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 06a27bb4-949b-396a-ab54-74adc11120ed | -16.9852 | -56.80419 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0faa4e24-0334-3843-8ab9-9864f29f9583 | -16.98482 | -56.80754 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9879704e-c29f-3fef-b12c-289e707035f6 | -16.97952 | -56.80688 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0922221d-179c-34f6-bc61-d2d8154287a5 | -18.71344 | -57.36483 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| f2a715d5-5b31-3a9f-8c94-73869a2206fc | -18.64774 | -57.29207 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e02bc52-feb6-33f0-bed6-9f18e2cdf25d | -18.64737 | -57.29539 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e2f5a4aa-46de-3bfc-86c9-011c7ebce706 | -18.64684 | -57.29299 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2d5a0b67-5fd0-350d-b20b-3c21410cf8ee | -18.64249 | -57.29145 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3a9b2776-7be7-3f65-be13-9094b0faa77e | -18.64212 | -57.29477 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e48ad9a3-1215-3d6a-bc32-447b0755842c | -18.64159 | -57.29236 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e66589fc-b8ac-356b-8f56-36ae9f5d228e | -18.63835 | -57.28087 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a868ea19-ee83-30fa-a66a-0aec932149e0 | -18.63309 | -57.28022 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| dfe12567-0228-35bc-80f9-5942adbd5cd6 | -18.69204 | -57.26816 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b34da26b-62b8-3e85-bf68-ca81bd9fcf69 | -18.68188 | -57.26354 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 1e9d41c9-ce4b-3461-8dd9-b46a86890bea | -18.66609 | -57.26161 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3517cc0e-1108-3781-bd80-f674100ae3da | -18.66159 | -57.26344 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 901f68a1-4927-3963-b00f-a4f6feaf0db1 | -18.66122 | -57.26676 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fe8471af-3d04-3773-8f42-f2d436f3d925 | -18.66048 | -57.2643 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c2b697e0-f275-3ac9-81e0-bd3525608d13 | -18.65634 | -57.2628 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e5a50057-68de-3c44-8725-f09b2726ba94 | -18.65596 | -57.26613 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c1f206e5-9e35-3eda-af42-bdb00142d03a | -18.65557 | -57.26031 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 106fdee2-3d5b-395d-8d1d-8e79c31486dd | -15.17804 | -59.44684 | 2024-10-06 05:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 982445b2-a822-3f14-ad9e-e46c62b64494 | -13.73386 | -60.65752 | 2024-10-06 05:38:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cd13e53-e469-312a-955c-30f2d1d7dd3d | -25.01775 | -54.0799 | 2024-10-06 05:40:00 | NPP-375D | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7a1bcbe7-3aaf-3a3c-980f-e30108a3c74a | -25.01744 | -54.07817 | 2024-10-06 05:40:00 | NPP-375D | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d67be78d-93c7-3b8e-a2af-c368600c4ad7 | -25.01707 | -54.08369 | 2024-10-06 05:40:00 | NPP-375D | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 446c25bc-7bbc-3e5d-a9f8-a47df353ff27 | -3.92643 | -51.24258 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7729fc2b-a2bd-30fd-9c8e-7bb180fbf017 | -6.36868 | -45.70976 | 2024-10-06 05:48:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 36d7ec5b-b88d-32eb-87b8-1a6688888079 | -6.36746 | -45.70271 | 2024-10-06 05:48:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| d43a40f3-9d5c-375f-82d7-f6df51f890af | -5.73292 | -47.1479 | 2024-10-06 05:48:00 | AQUA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c5b09856-0d1d-33ec-90a7-d06501a0237b | -5.60021 | -44.86535 | 2024-10-06 05:48:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 5c757f97-af34-3e03-8001-0f4f76a40f2f | -4.88325 | -50.76986 | 2024-10-06 05:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3b2186a8-eb8f-316c-9f94-6d9da2100217 | -4.68562 | -50.99126 | 2024-10-06 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a82794c-6712-31dd-aabe-3dbb0094b4b0 | -4.41257 | -48.71679 | 2024-10-06 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d35311d0-2bb0-3849-a65e-5e88940a85ea | -4.29516 | -48.64481 | 2024-10-06 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| eaaa985d-024b-31c6-bdc0-d86460feec93 | -4.12142 | -51.10389 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8f1abd50-79a7-30a8-8e31-bb0e20cddb35 | -4.11646 | -51.09655 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e6290aaf-17c3-3ae0-abad-ce30f54508e6 | -4.11501 | -51.10628 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4e5373e-b307-3675-b2f6-b169ce854093 | -3.92493 | -48.34839 | 2024-10-06 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 2b3e57af-4328-3bf8-b1dc-d3cd8917aa71 | -3.91373 | -48.34677 | 2024-10-06 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2dbfd5bc-5fb9-35ad-bf07-1bc1c5684c7b | -3.86803 | -46.45284 | 2024-10-06 05:48:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 311a95bc-1cf6-3488-9590-bd6a5e82dba6 | -3.86511 | -46.47301 | 2024-10-06 05:48:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| ac83da2c-6e93-39a7-90f7-43cc563c489c | -3.86485 | -46.45954 | 2024-10-06 05:48:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5d79cbe4-5fda-327f-8c8f-7dee8a5eecf1 | -3.80515 | -49.4683 | 2024-10-06 05:48:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9c92f9d5-f42c-3290-bf43-ce05ddc4be14 | -3.80323 | -49.46228 | 2024-10-06 05:48:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7d776f1b-60cc-3126-b77d-1c67db194376 | -3.53338 | -50.84409 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5deef591-4ee1-388a-8926-a9cb2b04b74f | -3.52424 | -50.26827 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33b45406-ccf1-32fd-b09b-df80409b63a7 | -3.51454 | -50.26687 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 952e77f7-384d-3791-a1d5-c624e8fa1d16 | -3.51299 | -50.27765 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 244b6919-9e77-34b7-83b1-2e777b05537a | -3.51 | -48.90054 | 2024-10-06 05:48:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28348768-4eab-391b-93cd-17a6e71b49e6 | -3.5041 | -50.80365 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5b9dadd0-74da-3dcd-b524-72880924fd00 | -3.48319 | -47.66849 | 2024-10-06 05:48:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0abbea84-2c46-3a4b-84e8-9cb1d6e938de | -3.44586 | -50.38028 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9197474f-41be-3b79-9f19-292657fa497e | -3.44431 | -50.39085 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b6e3e90f-bf56-33d8-ad09-53c7bf8e2b3f | -3.44124 | -50.13982 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 25838cfd-6f08-371a-b5ff-4c1349402adf | -3.43623 | -50.37896 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e05cb406-c9fd-312c-9411-2c1bf7f478ca | -3.43469 | -50.38954 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 746d69ed-e67f-3b48-b0db-ecb85c5640ab | -3.42662 | -50.37761 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c8d34cbc-00b4-3c4d-a8a1-6bdc7dce9cba | -3.42509 | -50.38812 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2f39304f-79c5-3046-809f-83fc2a7425f6 | -3.33853 | -49.14581 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 071c72e3-67c1-3aaa-b842-28b4e2802354 | -3.33246 | -50.45455 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b3f3856b-86ca-345f-9b5a-1b3d13dbdc6b | -3.33094 | -50.46492 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2281cf62-7f69-354d-8f36-7bae5487a8d2 | -3.32289 | -50.4532 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0410103f-437a-3445-8c6c-945aea227517 | -3.32139 | -50.46354 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| dce0e97b-0ed8-3a80-8958-4549f64bb394 | -3.31333 | -50.45184 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ce47f9ec-b9b7-31c2-8e5d-f47fea4386d9 | -3.30378 | -50.45042 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b2c2d5a1-dfe5-3d44-b66d-f177427dddbd | -3.29155 | -49.13231 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 03ebe7fc-d35a-3e05-aed0-9d7df7e63828 | -3.2897 | -49.14481 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3edd9890-559e-3893-a4d5-2f674a245632 | -3.28296 | -49.11831 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| eb720241-9abc-31c1-b373-d2821f7c9ff7 | -3.28111 | -49.13084 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 83d17fdc-6b53-3962-90e2-08158d61e7ad | -3.27878 | -50.1264 | 2024-10-06 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1390a58c-f5e2-32b5-b49b-e6b490c68e9b | -3.27721 | -50.1372 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| cd9520f6-f7cd-3cee-a95c-c5fc89b0ea3b | -3.26391 | -50.3634 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 95a43b6f-bb8c-3fbe-b1ed-bdaa49739e79 | -3.25278 | -50.37251 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a046508f-6dc8-3a16-a461-a95f0f5d8888 | -3.24791 | -50.83578 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| ee8e5acd-7151-37f0-af2c-48faf04a56e1 | -3.24647 | -50.84567 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| faf7efd2-2ee7-3b23-86cd-e314ab23bcbf | -3.23477 | -48.96306 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fc2bc95a-a969-3743-9db1-dedf99e082cd | -3.23286 | -48.97588 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c64edd23-0ed6-3490-849b-07fc8e8cdfa6 | -3.22958 | -48.96796 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a3b7bc50-7237-3278-9648-99885c824dba | -3.14406 | -50.41504 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c62b1494-5dc9-398b-8147-53ad7b30254a | -3.14295 | -48.59224 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 696eb617-309b-30c0-a50d-44554b660775 | -3.14255 | -50.42543 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 93e4e38c-8c1a-3b9b-80dc-4e5561e2725d | -3.14099 | -48.60585 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 200.9 |
| 9a8682ec-36b7-36e9-9869-2a2ee6ea32de | -3.13903 | -48.61941 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| ad62cf17-6204-3b0b-acea-fbbe1ae5e52f | -3.13451 | -50.41364 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9c877e6f-e9df-3005-89e1-9647bbd6cefe | -3.13014 | -48.60432 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d24daa29-fdd5-31c3-b4a7-b92800edad0f | -3.11893 | -50.4539 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fc4cdfb1-03b3-3abb-8f8f-011f9d0af99a | -3.11743 | -50.46424 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| abab54f5-6012-35f7-bb8a-37ed3779afc6 | -3.11594 | -50.47454 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e87bc02-b778-3da5-b39b-daa06e101640 | -3.1079 | -50.46285 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7e8ea41e-fb0b-3634-9124-f5c0b1cd8db1 | -3.08553 | -54.77462 | 2024-10-06 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a04a8549-20a8-3a34-b2e0-694519a79ac1 | -3.01752 | -49.80573 | 2024-10-06 05:48:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8447b1b0-fa7a-30a6-8ba8-62e2b678b28f | -2.91614 | -50.71277 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 31c5362a-0154-3f88-8619-83fde88fef11 | -2.90676 | -50.71142 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README148.md)
