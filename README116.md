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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 411af768-77ff-3a3e-a958-2c89f2f93226 | -7.73536 | -49.89451 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 441f70e5-0383-3e3b-93a6-9c15b1afca01 | -7.73449 | -49.89167 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d93a837-ac23-3c73-a3ec-34a408bf8e54 | -7.73238 | -49.88986 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44596436-aaaa-396c-804e-c1da4f69089e | -7.73178 | -49.89396 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55389831-deaa-34a4-b6d5-56ea7a3291aa | -7.7309 | -49.89113 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f8a82f9-7c4d-3f45-aea4-ec0b4e534304 | -7.56699 | -49.17469 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525d99ba-0fc4-399c-96a6-9e9c5b7e788a | -7.56633 | -49.17912 | 2024-10-03 04:49:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6574af92-b683-3732-89ff-3efd00a9b610 | -7.36543 | -49.6025 | 2024-10-03 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783310d1-a968-3f3a-b8c6-6f21da3517f1 | -6.97749 | -49.43398 | 2024-10-03 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc07911b-c5f3-3574-abb6-57725c2c00b5 | -6.97448 | -49.42918 | 2024-10-03 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05634bba-a04a-3d4f-bb97-6f21b9bd056a | -6.97385 | -49.43342 | 2024-10-03 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8db82c9-3d70-32ac-a884-f3bb5a03c998 | -6.97084 | -49.42862 | 2024-10-03 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54c542c6-eebd-369a-8fa5-c585d3be217d | -6.97021 | -49.43286 | 2024-10-03 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f152bfbe-a9d6-3055-86ca-12541beab4e7 | -6.9672 | -49.42807 | 2024-10-03 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa1d0d67-b525-387e-b901-c8b5ef53ea13 | -6.96657 | -49.4323 | 2024-10-03 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5703159f-1738-30a5-954f-faa3d4ec19ea | -3.45791 | -49.14778 | 2024-10-03 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75a7fe11-4d07-3b32-aed6-b998b08b3a83 | -3.42205 | -50.32629 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dde9e2f-79c5-3678-984d-216f163d8332 | -3.41469 | -50.32887 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2574f0a8-922c-3776-8bbd-a6174cc7509a | -3.31207 | -50.45004 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b018f28e-9627-32d6-83b7-e35319448dff | -3.31151 | -50.45363 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b36f2951-7da2-385f-991d-8fe07dfb9713 | -3.30869 | -50.4495 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 287bf350-d595-35f6-9b7c-2ff4a54b3533 | -3.30813 | -50.45309 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b2c6936-6606-3606-b5b9-7e695e39a240 | -3.30531 | -50.44897 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03b74214-513f-3d55-815a-acf64cd99991 | -3.30193 | -50.44845 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da7953a0-db15-3e1a-bb19-571327fda79d | -3.27307 | -49.10974 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 924cc98c-b0df-3e51-93ee-147e2e0207f1 | -3.26952 | -49.10918 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26e88f8b-f4ae-366a-bac2-2ef5cb167848 | -3.2689 | -49.11316 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 931b2430-99db-3791-b180-15c3cb8583fb | -3.25554 | -50.1414 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c364275f-94f1-3f0f-aa4d-7d7c31e76585 | -3.2527 | -50.13722 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33c3ad5e-c5ee-391f-9839-585a0725db18 | -3.25213 | -50.14088 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c75943b5-85a1-3d6f-b87b-95316ff64983 | -3.24929 | -50.1367 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04c7b2b6-a1d4-3872-a0bd-39135da4de33 | -3.24872 | -50.14035 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 79481307-f7d2-3266-9332-66a4bbcbc676 | -3.24845 | -50.48055 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec2a1eea-1d5d-3d06-95bd-71fd345f8049 | -3.24789 | -50.48412 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48a39eb6-5707-36a3-bb69-81c422f71f76 | -3.20781 | -50.37904 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99aca7d0-e384-37a5-ba45-5a6ad8180013 | -3.14196 | -49.41858 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adccb739-ee7a-3daf-95a5-4cc9df9eac7e | -3.14135 | -49.42244 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cecb215-abff-3780-9170-b62a0628b884 | -3.14075 | -49.4263 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1501422-2756-3c41-acb7-669dc3d1ab9a | -3.13846 | -49.41803 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f75309fb-0308-3c30-803c-3c70e00502cb | -3.13786 | -49.42191 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e85f641-f920-3119-904a-e34a72d24ac8 | -3.13496 | -49.41749 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 070239cb-6a0d-3cdd-8420-e2d75164d618 | -3.13436 | -49.42137 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 011167fb-6202-311d-93b1-04917d8be044 | -3.12338 | -49.11953 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4103a0cb-9142-3d68-bf9c-0bae1e0628f0 | -3.11867 | -49.4071 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ba81bc7-b6c8-376d-95fb-84f0bed7faf6 | -3.11807 | -49.41096 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed3e931e-3567-33a8-91b3-6fc578309410 | -3.11577 | -49.40271 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19f66562-6a69-38b5-8eb7-2fc7e715566b | -3.11517 | -49.40657 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 666b2a9e-d3f2-3103-9844-cf43bf7d9295 | -3.11457 | -49.41043 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21e37d31-c65d-3d10-a5d3-5c4dc85865ea | -3.09446 | -50.47943 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0d5d9c8-ab04-34f3-8d6a-7f36a8931c3a | -3.09108 | -50.47892 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd00fe88-9bad-3531-8ee6-4df3a10c264c | -3.08771 | -50.4784 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dd250a1-a3e8-332b-ad0e-92a78651180e | -3.03648 | -50.45218 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 956e85cc-e603-367c-a54d-4f55bf12d591 | -2.97737 | -50.29187 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3195505-3fb6-3366-b8eb-489679cfb334 | -2.96014 | -49.36397 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2900cfab-dea9-33c8-898d-09d5176b6af2 | -2.95781 | -49.35572 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 299efb50-21ca-387c-8f6e-02b7ef0da1c0 | -2.95722 | -49.35957 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3c440cb-0139-3a27-ac79-40b7fb68fea8 | -2.95694 | -49.3564 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd288a10-a0f3-3312-b21a-ec60f2562b8a | -2.95664 | -49.36343 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8e6860a-a94e-3b0a-a856-5a6ac17b7d6c | -2.95633 | -49.36025 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98823c34-373c-39cd-b58c-06de9d97b0ad | -2.95572 | -49.3641 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21e4dbca-e609-3cd6-a41d-1b41deafe92e | -2.80042 | -50.28371 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c7c2f6d-fe55-3731-8d06-c727894d7a28 | -2.79986 | -50.28731 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a9d4432-c23d-36a8-a0f4-6f7c9004fe81 | -2.79704 | -50.28319 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ec36c2e-8ff6-3f26-8c90-30d7d9cd2340 | -2.79647 | -50.28678 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e7d8d10-d5a2-31c7-8f16-64ac299d1f34 | -2.79591 | -50.29037 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f045b1b3-6d1b-3101-9d31-70c3692341a7 | -2.71285 | -49.44169 | 2024-10-03 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28a151f2-97f3-3cd8-bf73-2c5bb6d0b185 | -2.57245 | -49.07228 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f58647e-a698-32ce-aaf8-1b9cf39002c7 | -2.56946 | -49.06887 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5de19c60-b3d9-371d-9fd4-43fa68281e66 | -2.56892 | -49.07174 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a6525c-e97e-3b25-92b8-e5139db45690 | -2.56884 | -49.07281 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f42de9d-36bc-3307-bc3c-2a70f7b008c9 | -2.48884 | -49.05245 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5a2d967-10a0-32e4-8c28-8bb30680bacf | -2.48531 | -49.05192 | 2024-10-03 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 909cd175-fab4-3f3b-ab71-18056fe3e82e | -5.0669 | -49.78977 | 2024-10-03 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bc9709b-0963-3a0d-adfe-3e732a405cbf | -5.06162 | -49.80089 | 2024-10-03 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5527e4fa-dde1-3157-83cf-20162bbc72dc | -5.05988 | -49.7887 | 2024-10-03 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3128c561-68b9-3b63-ae1c-2640bb902dd9 | -5.0587 | -49.79649 | 2024-10-03 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b399e72-8570-3b73-a5b3-9f6a11c57804 | -5.05812 | -49.80037 | 2024-10-03 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e05abe16-aacf-3216-a2bf-cd1e4230cb3f | -4.3316 | -50.4936 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe935f0c-500a-36e8-bf7f-eb342d5f0477 | -4.3282 | -50.49307 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af95c363-e27f-394f-8349-41c8715e86da | -4.04136 | -50.38305 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3679aba6-1e4b-3008-b601-44520f8002fd | -4.0408 | -50.38669 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a58508a-0b00-39e6-ba56-6155ddf871fc | -4.03739 | -50.38616 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c2236c-db08-3b17-92d5-0b5f90f3b992 | -3.93482 | -49.99363 | 2024-10-03 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa39b893-2bb1-325b-8b77-c921d0c74ecf | -3.93398 | -49.88597 | 2024-10-03 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5108011b-7c26-3c78-9c89-5a5c446bf7ca | -3.93218 | -49.69162 | 2024-10-03 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 733138e6-ad1e-3d4d-80de-280f39439e56 | -3.93052 | -49.88545 | 2024-10-03 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef474819-5980-3178-ba81-461c7d379693 | -3.92927 | -49.68738 | 2024-10-03 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b165462-80bd-3a46-ab73-804f7a243193 | -3.92869 | -49.69114 | 2024-10-03 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 588ca5b8-b282-31bf-b870-95a57923eee2 | -3.92577 | -49.68689 | 2024-10-03 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0c808b2-1c60-3c39-aaed-b2357f9c2282 | -3.57249 | -50.57054 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 100a4299-7368-3b2c-9e02-5813be933f5d | -3.56967 | -50.56643 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 624b4aec-f481-333f-a9fb-760d74d863eb | -4.70231 | -50.87084 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b36e1039-ba5d-3a99-aeec-d149994c9167 | -4.69893 | -50.87031 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423d50db-a6e0-3ee9-bf1c-12eaeef74d70 | -3.9242 | -50.66416 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf532a32-d1cb-3465-b1a3-db984972029a | -3.92139 | -50.66006 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e63049a-f268-36d2-87eb-97854eb826cb | -3.92083 | -50.66363 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fc90ca5-6622-3351-a1ae-6bd3874399b1 | -5.02011 | -50.86809 | 2024-10-03 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16533c1a-acb6-3115-a004-33ffd6e6e7e4 | -5.52438 | -50.04548 | 2024-10-03 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201c5eeb-6a5b-331e-92e4-78c663d6061d | -5.52148 | -50.04112 | 2024-10-03 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5008a819-4c28-3aa1-9ea1-0def80a9a7f8 | -5.51681 | -50.04824 | 2024-10-03 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README117.md)
