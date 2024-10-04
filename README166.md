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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9061292-b133-31d2-9bb6-9f13fb1d0d41 | -17.0438 | -56.7905 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ab378153-059d-3ba8-8133-df8f40ab3294 | -17.04323 | -56.7941 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d2741df9-f1c8-33d1-b853-a0e37a4d4cd0 | -17.04219 | -56.77913 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 739233a8-a172-3f5f-ac28-f9a60149ffbd | -17.04162 | -56.78273 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c86d4cd5-519d-3241-80b7-73311e67a4f4 | -17.04105 | -56.78633 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 08a34aa8-5032-308b-8147-8978b2018dd9 | -17.04049 | -56.78993 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a05270af-04c8-3423-9f21-56ece035e143 | -17.03888 | -56.77857 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4f4ac7c1-cc2a-3fc9-bf51-e094d45a1bc6 | -17.03717 | -56.78936 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 33e5f855-64a8-376c-97ff-32588d3c8d8b | -17.03661 | -56.79296 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0853caa7-ab82-35f9-8d76-fd1fd15a0b36 | -17.03557 | -56.778 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fa6076ee-f411-3904-bca1-5d163dfc8174 | -17.035 | -56.7816 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 37054100-0d82-37cd-b6f4-cabf9f95f1c8 | -17.03443 | -56.7852 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 58c8643b-ce89-3080-98f3-c9b68f041c69 | -17.03386 | -56.7888 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b343274f-be4f-368a-8e7e-7680ec631adf | -17.03226 | -56.77744 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d02bd706-09d3-3e29-a3c4-31fa9a8f7fe1 | -17.03112 | -56.78463 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a5efb202-84eb-31f2-af56-cc9ccce1b20b | -17.02838 | -56.78047 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b16db906-d957-336c-a916-319c9d19a409 | -17.02781 | -56.78407 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e0b74e68-ef63-38df-809a-0afe018e08d1 | -17.02507 | -56.77991 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| da18c8f2-ecbf-37ab-8fc7-176d7561c506 | -17.0245 | -56.7835 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 572c29b2-f2fd-3de1-90fe-f43c4255b3b1 | -17.02176 | -56.77934 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 57b65572-3b8d-3ae4-9d8c-02c38ffab9fc | -17.02118 | -56.78294 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c2c02949-1d28-328e-b6d7-2b6d8411cbdc | -17.02062 | -56.78653 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b4992797-2a2e-3be3-be47-2e262ae14223 | -17.01731 | -56.78597 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1d774a61-e785-3c55-bfb2-5e86985430a0 | -17.01456 | -56.7818 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 77444a8d-d1de-366f-8328-95e1212f4f3f | -17.01182 | -56.77764 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| e1770593-bca8-37da-b5ab-0356d3f8640c | -17.01068 | -56.78484 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| ba50e76f-6805-3039-9e4a-83b868081545 | -17.00737 | -56.78428 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 5c02a4ac-a066-3b43-83b1-aa9765c532f3 | -17.00463 | -56.78011 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| bc2cbc9e-d097-3708-bf16-b23825e91c1f | -17.00406 | -56.78371 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| af46d689-f2f0-3708-bde7-5ba443a8e163 | -17.00132 | -56.77954 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 789900b4-f2af-3757-9241-652dfc6aa020 | -17.00018 | -56.78674 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1b0e0e4d-ddbf-3c1a-bc45-ca6c91660931 | -16.99858 | -56.77538 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| cbaa91c9-f433-341e-9ca4-bdf30544893a | -16.99469 | -56.77841 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| fc5cc77b-5023-37c2-9545-d6c9ada49128 | -16.99413 | -56.78201 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 587f15a0-558c-3cd4-ab80-b6fa0191986c | -16.98693 | -56.78447 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 7c7089e3-a1e5-31a6-b216-cd019102917e | -16.98636 | -56.78807 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| f355c9de-094c-3bfa-b1c8-f95c974c9523 | -16.69073 | -57.15228 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 28983396-3102-358f-8c5d-6f82e31faad7 | -16.6874 | -57.1517 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| effcd396-7596-32e0-b95b-5706e18158ed | -16.66458 | -57.16636 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 5b560fb2-1be5-3309-a436-121de92d0870 | -16.66126 | -57.16578 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 020c9835-fa77-3c99-956d-ef3378c7303c | -16.65361 | -57.14958 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4c0d256a-f43e-30e3-ba42-6f0a49cff51c | -16.85302 | -57.47526 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 11946c36-fb98-3501-9893-0be20a0b2f7a | -16.85087 | -57.46738 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3305e840-2e50-3aaa-bdbb-2d38348a3cea | -16.85028 | -57.47102 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6b0c2a10-057a-30ac-9feb-a0a361b9d6cb | -16.84969 | -57.47467 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7680874a-0e62-360f-91f0-a5eb2b3c02c9 | -16.84753 | -57.46679 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 3c85e101-9f33-3452-95fc-d2ec49c502d8 | -16.84694 | -57.47044 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f9981695-8561-3e0c-ae60-4f72f0ef589d | -16.84635 | -57.47409 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 63858a14-c576-3de6-9863-b09afdc4602f | -16.84361 | -57.46987 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dca7755d-cfdb-38e3-a3f2-0057600cdda2 | -16.84086 | -57.46563 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8e7b0cbd-6977-3955-9c01-7af9b60ecaa7 | -16.84027 | -57.46929 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4a5640f2-e583-377c-94fd-8f30563018be | -16.83969 | -57.47293 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d3f43922-d495-3b7f-9b98-08b75dd393e6 | -16.8391 | -57.47658 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a5578fa9-2563-3553-bebe-416d9fd482f4 | -16.83753 | -57.46505 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f0f949d9-0285-3e56-b09c-f0f4ea69c477 | -16.83694 | -57.4687 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c3d7f177-d0ac-3a84-8f89-c5b35053b4eb | -16.83635 | -57.47235 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3efc5f16-4d89-3713-aa3e-04a17b236b85 | -16.83576 | -57.476 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a7245371-3e03-3f4b-b850-feb0a4ed2796 | -16.83478 | -57.46082 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a0194141-8a3c-365c-8e4e-a36c4e7d3026 | -16.83419 | -57.46447 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a870a6dd-7508-3ed6-91d6-d772b0a45234 | -16.8336 | -57.46812 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 51c1a925-353f-35e7-b7c5-fb3f1e80ae94 | -16.83302 | -57.47177 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bf8f27da-879f-3627-8f59-227442e44a9c | -16.82419 | -57.46272 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 3149926b-c556-3204-a9a0-ccd3591f6854 | -16.8236 | -57.46637 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8f45a8f1-b09e-3c6e-9e00-f5f8f0437e95 | -16.82086 | -57.46214 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 72d095d7-b6e9-3b62-8e92-43a37f344b4e | -16.82027 | -57.46579 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cece0978-9f24-3f9e-a52a-6b6f9e4f1627 | -16.81752 | -57.46156 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8c98a46c-3fa2-3db1-ad2d-1bc9706fa6a3 | -16.81693 | -57.46521 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 38d1d857-fe0e-3d18-bb19-d247a60fa233 | -16.81634 | -57.46886 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 335691f3-f7ea-3a53-bf53-ab909ebf37db | -16.79634 | -57.46537 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d5a5efc5-ac9d-3dd0-856f-6bada916f69b | -16.79397 | -57.47998 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8249dcf5-2dc2-3f09-b4ac-805a44aa68db | -16.79123 | -57.47575 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b4704f37-e0d2-3103-b766-16bc9e8ff714 | -16.79064 | -57.4794 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 78035c8e-f03e-36ac-a9dc-8552c87d572e | -16.79005 | -57.48306 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 44b3741f-08fe-3adb-b1b4-91991b5c2e6f | -16.78337 | -57.48189 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6585952d-8b1e-3604-8050-76088960a3f1 | -16.78278 | -57.48554 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4acbc237-e181-3579-a0be-b7519f989f3c | -16.78219 | -57.4892 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 770478dc-9ad2-3a41-a9fe-2c7297ab9d7c | -16.78004 | -57.48131 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 70f46a79-cada-325d-b5bf-091de0777288 | -16.77988 | -57.43999 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f5337a22-2caa-3b39-a508-5d27165d6d6b | -16.77945 | -57.48496 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e473a0bd-4c2b-31ca-ab5c-7d697ed0dcd8 | -16.77885 | -57.48862 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 039a5e4a-17ae-33a8-8b08-ddc4803aabd9 | -16.77655 | -57.4394 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c780553d-5812-3b5a-ae4a-efad078311a3 | -16.77596 | -57.44305 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a70c8e5a-dad8-3133-a6cc-8b25a9bc4f2e | -16.77537 | -57.4467 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 87c8f586-c54a-32c0-b1ac-b9d4a9674a76 | -16.77478 | -57.45035 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3bfd9bae-f551-3654-8fd0-9191c5146fa5 | -16.77418 | -57.454 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 020d1d7e-f2e9-3f72-a5e4-8357e4e236fd | -16.77203 | -57.44612 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2ddc8e67-c7db-3e24-8f87-cbcb31fbaf9b | -16.77144 | -57.44976 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ac81b32f-a039-3872-8c91-df49e8f94fe6 | -16.77085 | -57.45342 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 69c626cc-b9fb-30e4-8b92-b8bcbfa6f653 | -16.77026 | -57.45707 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 4442684a-3ee6-3405-8843-1ebb2a36ff95 | -16.76789 | -57.47167 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4acda4c5-2162-3435-a199-ff9f74fd6f42 | -16.76729 | -57.47533 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| dbebda1c-b7af-3f3f-b9b7-dc0970da474f | -16.7667 | -57.47898 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 87007ca3-be4e-3f59-836c-b2cb6de27aea | -16.76633 | -57.46014 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 53f16bad-19f3-3ef3-af30-352d3d2c0d8b | -16.76455 | -57.47109 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f026d48d-bed1-3f4c-beb9-71445658014e | -16.76396 | -57.47474 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ad9af054-ac79-3e57-8a4d-833b800db4f4 | -16.76263 | -57.44073 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 75708937-0e45-3880-91ed-3b03e398fd4b | -16.76217 | -57.48571 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 25ef542d-0dd7-3fa2-aa3d-54b8bcfaecf9 | -16.76121 | -57.47051 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2f122086-66a4-3a09-9093-cdb5c3e2e017 | -16.75907 | -57.46262 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fc62665f-521a-39bd-8f6d-d62b0f9f8284 | -16.75884 | -57.48512 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |


[Clique aqui para ver as próximas entradas](README167.md)
