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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f120d805-c4df-386c-9000-9e67fad63e93 | -2.45062 | -50.99379 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0183b90-4fce-306d-9f79-b6708e3a8a18 | -2.42142 | -50.5027 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5103f3ad-0f0e-3f7e-b470-e4d3ce6bbf23 | -2.41756 | -50.50212 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9fa8779-d526-327d-a3be-20ddde8c15b6 | -2.31013 | -50.52687 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ce02de2-3e33-33b4-86ba-ce6cd86498d8 | -2.28919 | -50.66366 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b31bee0-36d4-3570-8242-7b7abeaa3a7f | -3.3423 | -50.75584 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 616caf70-125f-3814-b472-0316c052aab3 | -3.33844 | -50.75524 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de886c57-8f4e-32a5-9212-4dc50dcbe7e5 | -3.32159 | -50.76242 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30017717-bb68-32c2-87f1-d702794fbc56 | -3.27439 | -50.69881 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1381599-101d-360b-8dfa-3c746161aa18 | -3.27426 | -50.95392 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 975c9996-1846-3b16-b1cd-0b3786f1e778 | -3.27126 | -50.69343 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46f25da1-cffd-390f-b344-06bd0c46318d | -3.27052 | -50.69822 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ec258a48-7631-3581-90d3-96b00b6af5fa | -3.26422 | -51.01839 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a4d2853d-83a8-3fd2-99ee-228722fa2b82 | -3.26351 | -51.02295 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6dc6ab8-859d-3406-9632-5368e9c438ec | -3.25535 | -50.6417 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbf68697-72fb-30dc-850c-d98adabe1382 | -3.25147 | -50.64112 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eaa7c784-405c-359a-a6ae-fb60f924fd9b | -3.25073 | -50.64598 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 808e8757-e641-304d-b96d-2f5e90ac3208 | -3.23771 | -50.73222 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2b031f4-bb0b-3ca5-8fd2-51f0a27b0e95 | -3.23458 | -50.72686 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36e9a5e4-c899-37c1-98b5-da29a8b9cdbd | -3.23386 | -50.73165 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdec89fc-e201-369a-b116-837280083db4 | -3.23362 | -51.1902 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 526b72a0-6fb3-34f4-aec1-29e4ae847d88 | -3.23292 | -51.19469 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30ff56d7-3644-3f7f-b901-79dbfd9f5171 | -3.22916 | -51.19417 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50faf197-8a12-329f-909c-79ae251baa6a | -3.1852 | -51.15532 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6579d297-9121-3eef-83db-9ca82c6c51fd | -3.18451 | -51.15981 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f58359dc-7947-3e77-9dcd-9cedc5006d45 | -3.16846 | -51.0879 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 147ec380-8f04-3cd0-80e4-39b7069e4ad4 | -3.16332 | -50.59136 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3cd2347f-74d5-3770-8df1-1728941b73f4 | -3.15943 | -50.59077 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6abe13cc-623f-3fb3-b8ec-868979e63998 | -3.1587 | -50.59559 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6908235a-3f6a-36f5-a46f-945358028a1a | -3.15555 | -50.59018 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d05cfe32-52bb-3cbb-8847-92608e47ca06 | -3.15482 | -50.59501 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84e1eacb-dc61-3a4d-baab-837b49dcac15 | -3.15093 | -50.59441 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f0203f3-85dc-3cc5-9afe-0bd824d656f5 | -3.12482 | -50.60314 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d2d1819-b9ce-3758-8754-9b0b32248908 | -3.09985 | -51.25898 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35872da4-3022-3cb2-8972-f182054ab799 | -3.09916 | -51.2634 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e7a22e4-851f-318f-818c-9d13502aeac2 | -3.07928 | -51.1184 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a742af02-5c84-3d51-ad3f-4715e74b62b1 | -3.0786 | -51.12289 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ede60de-0c06-34c5-bbbd-ad2fa4c8aa46 | -3.07743 | -51.35463 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d9cd8f8-5b7c-3756-a27d-2afa22115c06 | -3.07372 | -51.35407 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b06a4dd-ac50-3563-8640-128f764e7317 | -3.07304 | -51.35848 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b7cd0f8-3cdb-342e-a9ee-65389c682010 | -3.03678 | -51.44655 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63f5f3e3-23aa-3e4d-b19d-3c929a488498 | -3.0331 | -51.44591 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e892936e-7a88-36d2-8fbb-e16bb9607d82 | -3.03111 | -51.45894 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12a62e59-b62c-33b5-b973-c565bbdeeb4b | -3.03044 | -51.46332 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2e93a1-7735-385e-a23e-4ea393eeafce | -2.9676 | -51.43774 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec63f071-c52d-349f-8e41-b45ef385f423 | -2.96692 | -51.44206 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9206336d-56a3-3ced-b36e-a4abcdf7c178 | -2.95437 | -50.99952 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91b7b37b-c1b3-3a0b-bac7-b8a7f3c2efeb | -2.89707 | -51.47985 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ec1880d-184f-3f75-8db4-d62a953c46fd | -2.89641 | -51.48415 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29690d8c-858d-3a8a-8d09-50ed45d33c8b | -2.8752 | -51.31426 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d90888d8-a5cc-325a-bbe8-412cda6b2ad4 | -2.87217 | -51.30933 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 589e1c51-dd63-3b34-82c7-692de7d7a991 | -2.82559 | -51.03562 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d811c618-2645-3de2-b6de-4db3ecc4441c | -2.54348 | -51.16541 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 580aee55-361f-302e-959d-4823b135a9a6 | -2.5428 | -51.16982 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 719727d9-7076-31a8-9397-f3ec7fc8959e | -2.54212 | -51.17422 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca25e54-41c8-3b89-8620-c5f7528e519c | -2.54144 | -51.17864 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f92d190f-89b1-3620-9bdf-350998a8a6ea | -2.53772 | -51.17806 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 221fe1b3-c8b8-307c-9eb5-79580e086b49 | -2.53636 | -51.1869 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a21d545-fc25-39ee-90b3-bc6b73c3a09b | -2.53197 | -51.19072 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f11ae647-eeec-3b6e-acef-076918a2270c | -2.53028 | -51.17692 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d60218b0-2cbf-39b9-9ac0-3e1b70696706 | -2.5296 | -51.18133 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7229576-f12f-3381-934d-215b26a2dd6d | -2.52454 | -51.18958 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f76ae597-f9d8-3fe1-98e8-e407307eea20 | -2.51777 | -51.18401 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb37733d-f2b6-38b0-893f-32c2873babb2 | -2.51406 | -51.18343 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59ca8e1e-aabf-3247-9fd5-d33ecffdb2dd | -2.5139 | -50.70782 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a5f276b-7f2c-3c3d-93d4-b980d4de47bf | -2.51034 | -51.18283 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72ef9e1e-dc3b-31b1-9c79-fd20810e2b46 | -2.28608 | -50.6584 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a1fa5b6-ba23-3cb8-af84-f36bfca28587 | -2.25431 | -50.69426 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2208add2-9d4b-3887-9f08-e6f0f0b6d30d | -2.25368 | -50.69156 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c007567-b666-3861-9434-b4ccf03c086a | -3.54701 | -51.38953 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2771f78-015e-3392-a253-106a470a1d59 | -3.54569 | -51.39164 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22faec3a-86ff-3fc9-b44e-fa857bc5ae7f | -3.54397 | -51.38445 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30f4440c-0855-3466-8d21-20be934f2d8c | -3.54337 | -51.38211 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53404467-44d2-3024-8f71-b1dbd69ee7de | -3.51208 | -51.2127 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99d2acfd-ce56-37dd-9f66-9b88dd4e1a75 | -4.67014 | -50.97797 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7d03711-e8b6-320e-842f-681b8d786770 | -4.6694 | -50.98276 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bba5434-8d29-3485-9026-c3845ac6b5c3 | -4.66626 | -50.97739 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61880b0e-9c1f-3af3-97c5-7f3ddd764352 | -4.66553 | -50.98219 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 189ce872-c20e-34a3-a961-88ca6e82a561 | -4.53621 | -50.96539 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f08a252e-e4cd-3dc6-a5d7-f115ef19a7d0 | -4.52944 | -50.98396 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de084f36-145e-316b-a858-ef27949f64a4 | -4.4771 | -50.99065 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2352cc8c-6e75-3f99-8341-380ba5feb194 | -4.47639 | -50.99544 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2933b5b9-a31e-389d-8eeb-3c78ab3fe043 | -4.47567 | -50.99343 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d33fbe1-416a-3dff-8c82-51f3f8e0612d | -4.47493 | -50.9982 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e35be76b-8b7b-3e73-98e5-c551f811e0b0 | -4.47182 | -50.99963 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eed411bc-e857-37c5-baf2-f611484710a4 | -4.47108 | -50.99761 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fea22ec1-cd01-36e9-943e-abef0e164580 | -3.95897 | -52.19115 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69561085-0cd0-3789-917d-e8a7444f8140 | -3.92762 | -52.12054 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3555c707-6070-3686-9c72-ea1d37a6a19f | -3.92699 | -52.12464 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82389b6c-fff0-3b50-890e-2403221b4088 | -3.92402 | -52.11998 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 113c1b53-743b-34d5-8a88-6db329dcf371 | -3.82014 | -52.11827 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2d3f10d-91e5-3dfc-b3f4-bc55c1506338 | -3.66233 | -52.15367 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0fbc1ba-3e8c-3538-865f-73f1f4a02745 | -3.65573 | -52.04554 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6cfc0e3-8774-3765-9691-e40d13398413 | -3.55816 | -52.10576 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59f43ca8-ca34-38e7-a6a8-b6de9ae893f8 | -3.76922 | -51.39749 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bea827b6-0fe0-303f-895a-54393d4c77a9 | -3.76352 | -51.66025 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74cf3a2d-55a9-3f12-8727-3a3657538163 | -3.76214 | -51.06455 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80548270-200f-340b-8f5d-1d45f031b409 | -3.75835 | -51.06388 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11600e26-8972-351f-9580-913b5d4f6754 | -3.69915 | -51.8376 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0e93d28-35b7-3946-9919-d1a1119bb142 | -3.69552 | -51.83874 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README79.md)
