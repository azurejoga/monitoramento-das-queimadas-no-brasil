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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a51f5510-4c61-349e-b67c-63c16279a165 | -17.08688 | -56.72686 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d5f796e4-cf09-304c-aa6c-f9b87ce762dd | -17.08602 | -56.72101 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6eb9b78a-3e2b-311f-93d8-0ebd88a15227 | -17.08594 | -56.73129 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 33778cf1-d2c4-3455-96df-6ec0c9f645fc | -17.08505 | -56.72545 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d42753f4-2c39-3c97-b0fe-74ae09f8da39 | -17.08408 | -56.72987 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9f40ac86-1ea5-34be-b074-fafdf4c17bd9 | -17.08198 | -56.72098 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a3621ad1-7ca3-3354-be30-4ea4346729f5 | -17.08115 | -56.7152 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7eb67b1a-cb88-37a9-b4de-3570ee313a69 | -17.08103 | -56.72543 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a75666e4-35c2-30e1-8ad3-2dcdcb2def3d | -17.08018 | -56.71962 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6694a34b-9b5b-3a69-ac47-636247c65856 | -17.08009 | -56.72987 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3c7f721f-a6e3-31f1-9136-cb51ae16d30c | -17.07921 | -56.72404 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7598cbe6-5db9-353f-9707-fb351c65d1e5 | -17.07824 | -56.72847 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cc8a2796-667f-3e7d-ab37-ff2035cd155f | -17.07707 | -56.71513 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7323f869-0cc1-3492-b6b9-2acc78f9a13d | -17.07613 | -56.71956 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4ef4a594-8619-3d65-be40-3aef902a1fa6 | -17.0753 | -56.71379 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6ff68e0d-5c0f-3c84-bdf5-b2fa943ec088 | -17.07519 | -56.724 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 802d6c65-f0d4-3731-8e23-ef61974fad4f | -17.07433 | -56.71821 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5e0d8fcb-55ec-3d57-b2f0-b1f2d3e32e2f | -17.07425 | -56.72843 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c38bd871-4add-3a0e-b8be-cd09bb33f5c6 | -17.07336 | -56.72263 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 32e1d10e-52a1-3f39-a860-249be8cc68aa | -17.07239 | -56.72704 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0a05318b-4c78-311c-a46d-6b5b974c9505 | -17.07142 | -56.73147 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b857da4a-bd58-3fa9-a266-226ae3398bd5 | -17.07123 | -56.71371 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 98c4519d-eaa3-37b5-a77a-1ca56524ce97 | -17.07028 | -56.71814 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3fbb01ff-07d8-37c1-a3bf-ad58476b2c45 | -17.06934 | -56.72257 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 98c55eb6-3650-3df9-bf13-f483d22d35f1 | -17.06848 | -56.71682 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 14f209df-3694-3f04-9326-94cfc240baba | -17.0684 | -56.727 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 408d3f8c-6e77-3de8-8266-535e37901474 | -17.06751 | -56.72123 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 98c13193-cb68-32d7-b550-b0c844652795 | -17.06746 | -56.73143 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 38f6e99c-2ad5-3399-8fba-f7f5dc1db019 | -17.06654 | -56.72564 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9fbb4617-d801-3b52-904a-825bc43fb347 | -17.06557 | -56.73006 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 24beaa69-f894-37c5-8850-22008c2a0276 | -17.06538 | -56.71228 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 489e7396-4c6d-3edc-81b1-26e72a12bb8c | -17.06444 | -56.71673 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 54ac1679-4939-302f-b7c4-505058562c53 | -17.06349 | -56.72116 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f46ccb77-b92a-3d88-9d56-7ea3db192ee3 | -17.06255 | -56.72559 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d47b57de-19d4-3b8a-ae0e-355b707ad9c3 | -17.0616 | -56.73002 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 20074608-3bab-342f-ae1b-762de07ecdff | -17.05954 | -56.71087 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cd650710-e9bc-380f-aa84-aa3e2969afb5 | -17.05859 | -56.7153 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 38ee033e-1739-3c58-ad90-120b0d622164 | -17.05764 | -56.71975 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2bab169e-525d-3da5-abef-24af68060784 | -17.0567 | -56.72419 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e7a937f5-ccb3-313a-bf77-e7170365edee | -17.05575 | -56.72863 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 83f3ceb4-afac-3b04-a625-c59851afad37 | -17.05369 | -56.70947 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 47a8bdf0-7b99-3812-b823-a3f85dc080b2 | -17.05274 | -56.71389 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ca0e6af6-3f7b-31aa-a1b7-b50b71e4369f | -17.05179 | -56.71833 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 45260edb-be1b-3632-8861-1fb45bfa01bc | -17.05085 | -56.72277 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c32963ab-bf71-3f2f-a33f-811a9d7b81a8 | -17.0499 | -56.72721 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 51cca07d-cc6f-30e0-b7e1-f869f8a61b9e | -17.04405 | -56.72579 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f763fc43-79dc-396c-8ea7-4200e90bdcf4 | -17.04309 | -56.73023 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 79d4096a-7018-3a0d-9843-3d50bd3e0e04 | -19.13106 | -57.46939 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2ba107eb-fd3b-3ff4-87b5-63be7f2ef742 | -19.13018 | -57.47332 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b95e734d-9271-33fe-a4b5-1c769324b2ca | -19.12518 | -57.46791 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| daa5293d-060b-3c45-bbe8-1de7b2fc4b77 | -19.12424 | -57.47213 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a2f3da15-29f0-37d0-9a2b-c6592cbf3a07 | -19.1234 | -57.47585 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c897a021-f419-375f-a877-feaabfe18d71 | -19.11931 | -57.46643 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 680dd325-0ac7-3de0-855e-1b7fe714f372 | -18.71127 | -57.31823 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 520d04fc-085f-3b2d-b14d-267ed44efda9 | -22.1759 | -47.5233 | 2024-10-01 04:17:07 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2652a303-475e-3f6d-9231-c8b5bb7e8db8 | -22.1968 | -47.5179 | 2024-10-01 04:17:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| 764e1fcc-28e6-3aa8-925f-08561fcce9c0 | -22.3498 | -49.3293 | 2024-10-01 04:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| f890ff32-9cac-34f4-b893-1bfe423d46ad | -22.37 | -49.3477 | 2024-10-01 04:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 7db70b07-468f-3117-85af-6a96448395c6 | -22.3707 | -49.3244 | 2024-10-01 04:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 229.3 |
| 7ce4a9f8-a742-3610-b4d1-dd7f4e5b244e | -22.3713 | -49.3011 | 2024-10-01 04:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.7 |
| 3d0dd95c-04de-3b75-9bff-7c70533d41e6 | -22.3916 | -49.3194 | 2024-10-01 04:17:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.7 |
| 6ed729fe-bc21-3e19-a47c-b3f8d40bb8e1 | -22.3922 | -49.2961 | 2024-10-01 04:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| f8d6cba5-e055-31d2-a517-2ef652167116 | -26.21789 | -52.37082 | 2024-10-01 04:19:00 | NOAA-20 | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4243dc85-44e0-31ef-b7de-8c057e6dbc97 | -26.2141 | -52.36988 | 2024-10-01 04:19:00 | NOAA-20 | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5539a15e-7e7a-3bce-9658-9214589c2918 | -26.41363 | -53.23065 | 2024-10-01 04:19:00 | NOAA-20 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 13394b61-b730-3f14-af9a-9432707283bd | -26.40968 | -53.22965 | 2024-10-01 04:19:00 | NOAA-20 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d6579d3f-90ac-3fa3-bda2-e4fa67e1d802 | -2.846 | -50.7366 | 2024-10-01 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 421846be-c0ee-36cd-bf76-f684acf2d627 | -2.8461 | -50.7157 | 2024-10-01 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 03287d7f-b83f-372c-8cb1-e642ce8d7d4b | -3.0282 | -51.3345 | 2024-10-01 04:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b4ff1179-b539-3dd0-b504-405196215b4d | -10.9964 | -46.5192 | 2024-10-01 04:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2cfbba8c-23ee-3eda-a43c-79bd2dabc005 | -10.9971 | -46.4741 | 2024-10-01 04:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cd6c10ea-694b-3cfd-af45-5148b4edc98d | -11.5695 | -63.8084 | 2024-10-01 04:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0b9e65a0-b97f-39a6-8835-16ff388fdf3b | -12.1406 | -50.0524 | 2024-10-01 04:26:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| abb5e94b-0ad4-3b9b-938e-5d98c92ebf5e | -12.9245 | -51.2002 | 2024-10-01 04:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| e2580ad7-b844-3a9b-b381-b28e32a63bc9 | -12.9054 | -51.2026 | 2024-10-01 04:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 07d0c536-d293-3e3c-be4f-d879e4675a30 | -12.7826 | -62.9025 | 2024-10-01 04:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 05084e45-5df0-3bc8-a97c-9b9fcdc2f5cb | -12.7827 | -62.8832 | 2024-10-01 04:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6df0bc6c-2d39-35ec-b424-8e2ef967b66a | -12.9249 | -51.1789 | 2024-10-01 04:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 7a3facc6-089c-3877-a6db-f945e733e603 | -13.2308 | -51.2048 | 2024-10-01 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| de84a659-1608-328d-9774-7b32bdedb8da | -13.2116 | -51.2073 | 2024-10-01 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 41b0fb57-4406-3c88-88b3-2c25d54b5be4 | -13.5768 | -51.1607 | 2024-10-01 04:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7db07ec3-972f-3ad6-9f61-c0533e4e9039 | -13.5961 | -51.1582 | 2024-10-01 04:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8411dc6e-d85c-335f-9509-ca3f2ff82550 | -13.6357 | -51.0888 | 2024-10-01 04:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 61a543cd-5020-30b4-9ab5-3894b735ea78 | -14.7406 | -48.7498 | 2024-10-01 04:26:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a34c6602-1b3e-3f15-965d-418c1f358520 | -16.5131 | -57.3509 | 2024-10-01 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| db76b968-c7c1-3f83-9cb0-00a809f67ce6 | -16.4536 | -57.4188 | 2024-10-01 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| ace658f8-db17-3e33-a926-2cfc3b5ed009 | -16.474 | -57.3553 | 2024-10-01 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| 340dbe96-a24b-3857-a78f-d974581cc83a | -16.4743 | -57.3349 | 2024-10-01 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| e42b021b-4e76-3e56-8139-75eb909fd2f6 | -16.5134 | -57.3305 | 2024-10-01 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| b0d4a13b-ea83-31f7-b35f-7f22bb51f445 | -16.4935 | -57.3531 | 2024-10-01 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| a9caf15a-bd2d-32a8-98a9-6e6fb575e1d1 | -16.4939 | -57.3327 | 2024-10-01 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 5f646d04-8da4-336c-84f6-e7a12ed0af53 | -16.6316 | -57.2557 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| a2fc1881-75e0-3bf8-a5fe-194f4671dacf | -16.6319 | -57.2352 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 2c74c0ea-d618-32f2-a179-f3cf57168331 | -16.6505 | -57.2944 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 29b94ad6-910f-33c6-bdb0-0c269d18680f | -16.6508 | -57.2739 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| ec1a9617-cf8b-3229-b758-65e8c31e7a96 | -16.6512 | -57.2535 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| b678ff3b-4c39-3267-843d-035602d15d81 | -16.6515 | -57.233 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 4f4d8590-18b3-3b6e-8187-b33d80d0d351 | -16.7076 | -57.39 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.7 |
| 55f4998d-7c8d-3f54-aeab-e6c0aefdd771 | -16.7079 | -57.3696 | 2024-10-01 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 23a4509b-6ec5-364b-8e20-57076a254df7 | -16.7528 | -55.8005 | 2024-10-01 04:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |


[Clique aqui para ver as próximas entradas](README98.md)
