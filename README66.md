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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3573020e-9ebc-3f61-88ae-8408e8cffa4a | -8.78846 | -49.97557 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5283737-41e2-3eb1-b5ad-7bbfd0df1bb0 | -8.78635 | -49.96175 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9922b5d1-dfbe-3fe5-b11d-f023329978fb | -8.78558 | -49.96608 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02bc0607-134b-3243-b42a-98269bdbec8c | -8.78501 | -49.94359 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07eee30e-b5d5-34d5-b560-0f32a67dd175 | -8.78481 | -49.97042 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10db0206-3d21-325a-98e9-543c9560d88b | -8.78425 | -49.94792 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fca1913d-bf78-37d2-ac6b-d620ea3eebd2 | -8.78404 | -49.97476 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c54df256-1a0a-3bcd-96c7-3f1abb7985ba | -8.7827 | -49.9566 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df3777fb-71f4-3441-b2ec-d04086ea4cd9 | -8.78193 | -49.96094 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ea73d3d-f09a-33d3-8da8-fa7090480e64 | -8.7816 | -49.94532 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61858a53-2332-3a3f-86e3-d5e2c125d9d3 | -8.78116 | -49.96528 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a769d01f-68e0-3c96-8207-c19d1e2a05eb | -8.78087 | -49.94967 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cb51678-6fec-39da-bd42-92867c1bb4f5 | -8.7806 | -49.94281 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d3dcc7d-67ca-31a1-9718-79b8311a1f2a | -8.78013 | -49.95402 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7be339ef-c31d-3ba9-bd1b-e1e0f5ab806c | -8.77983 | -49.94713 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef76da6f-7ab3-3835-8647-fb31220864d3 | -8.77939 | -49.95838 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0905c1c-a241-3074-a0a8-46f3b2d6b64a | -8.77906 | -49.95147 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 137f8d40-6b95-3643-91e2-dc1b3be777eb | -8.77864 | -49.96273 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d07f9d79-2acd-36cc-8abc-afc37e3420e0 | -8.77829 | -49.95581 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2fb0f56-146b-32d4-a0eb-ae8a627ea2f8 | -8.77793 | -49.9402 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af58892e-55df-3991-b0c8-fb911df10e8b | -8.77791 | -49.96708 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3464a7ce-1d7f-3e7d-bfdd-3be599212804 | -8.77751 | -49.96015 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8b8d175-dafa-3688-b1ed-5d7773058a2b | -8.77719 | -49.94453 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fccef29-f637-3ceb-bf7c-4797aba46219 | -8.77674 | -49.96449 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00a58b95-f1b3-3859-8181-f1c206f06855 | -8.77645 | -49.94888 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf9a3de8-7e83-37c9-8530-f23998347209 | -8.77619 | -49.94202 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 140e8bce-6352-3492-b342-479683583c92 | -8.77571 | -49.95324 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0250ea25-dae6-3eb2-94ae-94e177e746e8 | -8.77542 | -49.94635 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 981057a6-96d2-3855-bc45-57612327cf8f | -8.77497 | -49.95759 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07146611-3aad-3e27-ade5-121358da8e8d | -8.77464 | -49.95069 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d192a78f-8341-30b2-b671-14338bb342ba | -8.77422 | -49.96195 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7236be90-9aed-334c-8b4f-f33bdb51ecdf | -8.77387 | -49.95502 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cabc00a-ded5-32dd-9071-8d899c2acf0e | -8.77352 | -49.9394 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78b54728-e1bd-3340-ba82-ab544bceda27 | -8.77309 | -49.95937 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe8c8c0d-278c-30a3-aa45-c21a65e4500a | -8.77277 | -49.94375 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c65b34f-36be-311a-93a0-99cb603710f6 | -8.77203 | -49.94809 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 59e7c7c8-236b-3130-8a29-e79bfdd05cd9 | -8.77178 | -49.94123 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf4da02c-b895-3354-ad58-41bc2f36bbe0 | -8.77129 | -49.95245 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d7cba0b8-b8c8-351b-b006-ca4732127350 | -8.771 | -49.94557 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e20ac3c8-737e-3037-8711-9c23e814a450 | -8.77055 | -49.9568 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28e36265-0deb-3c0b-a0fe-9b4c0ed0d89f | -8.77023 | -49.94991 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d1cb70e-5b74-360a-a195-7ac4487d074d | -8.7698 | -49.96117 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c9cb5f9-c167-3566-9ebb-6f117d755e87 | -8.76945 | -49.95425 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 734ecc01-e312-31ba-a92a-48e57903b8b3 | -8.76867 | -49.9586 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10f92bc2-9fc9-3cc8-9586-4648ab4df751 | -8.76786 | -46.80338 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b59fba4-1c69-32e3-a4db-b39d40dcf72a | -8.76761 | -49.94731 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cdfe749d-6dbc-3f94-8d54-848711cf4733 | -8.76735 | -46.80604 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03dc08a0-0268-3d37-8a42-09875f72101e | -8.76687 | -49.95166 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e1b63a20-e670-30bf-aa02-f3c7bc06ef12 | -8.76612 | -49.95602 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11bac754-ab69-38ab-a908-6a300a5ee9a8 | -8.76581 | -49.94913 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 607c5123-270d-3d9a-9473-40d77ec27284 | -8.76503 | -49.95347 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3ebe324d-f633-3d6a-901c-323a8828a336 | -8.76371 | -46.80544 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f629a0c1-3601-32e0-95fb-fff3b8442e53 | -8.76353 | -46.80704 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50ae9608-e1b7-3bb5-b752-bd2f83e64222 | -8.74531 | -46.80408 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 232b82ae-0b37-37a4-8296-82a814c9e6b5 | -8.6518 | -49.10436 | 2024-10-05 04:14:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cc6a946-3a6a-3e61-8aae-2c0a04c9bdaf | -8.65114 | -49.1082 | 2024-10-05 04:14:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ede4ce38-b64e-3297-a6c6-08e46db769ab | -8.64416 | -53.17245 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c27c3265-5d45-3c95-ac04-9202fda4d56e | -8.6441 | -49.09903 | 2024-10-05 04:14:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b30074cc-6b1d-3fc2-8849-d36f7ab1618c | -8.64058 | -49.09445 | 2024-10-05 04:14:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b9d9ada-2722-3d79-a167-84870e440c0c | -8.63923 | -53.1727 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54668e96-86e6-30e7-8533-185a56f9e3b9 | -8.63863 | -53.17163 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30ade569-c8d5-35d3-9eb8-fbd6c68e5e80 | -8.63862 | -53.17613 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dc8a877-3052-318e-b83f-3e7ba2163b24 | -8.63799 | -53.17507 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c88b2f9e-156b-3df8-b3a0-19cba17c26e7 | -8.61068 | -46.51565 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4de17df3-b1fd-3518-9550-df3fe1590fb2 | -8.60627 | -46.49792 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c902edf-b236-33ef-9e2d-3a46742f74f1 | -8.60518 | -46.49477 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ad3a60c-23a6-3542-a82d-7b3f0450ea49 | -8.60451 | -46.4989 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abfc2950-51b1-316f-adbd-4bf019e97817 | -8.60268 | -46.49732 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ec17957-557d-3424-bf7e-fafd0f8b3d89 | -8.60092 | -46.49829 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c47f967-7f11-32e9-8c8a-a0a9f5cc01a5 | -8.59908 | -46.49672 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f626882-3ea5-3774-856c-22c2b44fe624 | -8.59839 | -46.50083 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e74fa802-8fb7-3945-9c50-28c4a5ff10ce | -8.5977 | -46.50494 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41c1280e-1cae-3217-8ae3-4fc9b9bab181 | -8.59733 | -46.49769 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 028b8d60-75bb-39ac-96f0-e1b523485ea3 | -8.59666 | -46.5018 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29fec5f9-a93c-36ba-835a-b795bb4ef891 | -8.59462 | -47.13297 | 2024-10-05 04:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fe17f7d-5653-3d12-a1d8-8f268853f138 | -8.5939 | -47.13739 | 2024-10-05 04:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 843ba957-d8de-3af2-a296-24281219d370 | -8.59317 | -47.14181 | 2024-10-05 04:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93c156ed-2d04-3f37-93a9-7e29a7d470bb | -8.58948 | -46.50059 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 557a7ab9-555d-373f-b23d-9baf04c507f7 | -8.58589 | -46.5 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 560f9388-cf79-39a5-8963-5a57ca538995 | -8.58522 | -46.5041 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e5de9e0-39be-3a2c-b834-c4a3992180be | -8.58455 | -46.50819 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc5fec07-bb0d-3aec-a3f4-abd592ba5f4e | -8.58388 | -46.51228 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ff14bde-fd41-33ab-be0a-ae507953a204 | -8.58162 | -46.50351 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a4a8369-916f-3f56-8144-f000dbbd05c3 | -8.58095 | -46.5076 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd0f0f1a-18e7-3c87-9e08-72b59cabcfae | -8.58028 | -46.51168 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac9bad92-dae7-3e19-9ad3-e43d5e80957f | -8.55669 | -47.63744 | 2024-10-05 04:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd15b6c9-e3f2-33ab-9469-ee3bd1ee1f92 | -8.55589 | -47.64214 | 2024-10-05 04:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d444eab5-3994-3733-9359-932a02503a24 | -8.54116 | -50.09957 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 177bf98e-fc52-393e-9237-96d4cac3df59 | -8.50101 | -46.85814 | 2024-10-05 04:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4998623d-8098-38eb-9659-b0706e3696fd | -8.49766 | -47.30077 | 2024-10-05 04:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b44982e-11ae-303a-b356-bad8e5bb0165 | -8.49315 | -47.30463 | 2024-10-05 04:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 593cccb9-9d2d-36fd-a130-12f33a5e59ad | -8.49242 | -47.30894 | 2024-10-05 04:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afc23240-f3c0-32a4-9d05-7a35f046baf2 | -8.49169 | -47.31326 | 2024-10-05 04:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e89de62-31eb-33af-a4d0-8b5169dab449 | -8.47879 | -49.02841 | 2024-10-05 04:14:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4008150-90b6-3a92-badf-c3cf08d1d0c3 | -8.47526 | -49.02386 | 2024-10-05 04:14:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42684225-9c29-3384-a420-5912aef9d153 | -8.47461 | -49.02768 | 2024-10-05 04:14:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cb3a242-57e9-36e0-a63a-e4d5573963f8 | -8.41901 | -46.2859 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7189dcc0-1437-35df-9f19-f1f62e40964a | -8.4178 | -46.28461 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a7678fd-3e99-33c3-92cf-6374c6b9c433 | -8.41713 | -46.28865 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a3e13cf-a2c6-3597-8fa8-a7e286282159 | -8.40227 | -47.73825 | 2024-10-05 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README67.md)
