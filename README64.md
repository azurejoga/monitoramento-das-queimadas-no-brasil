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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f4147da-5bd7-3b4e-9800-961f827c6f82 | -8.64165 | -50.04025 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9604ad7d-17c4-380c-a6b6-be63e2b2c697 | -8.63962 | -50.0513 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7dae62a2-d102-33bf-ac63-b1dc75de9ca9 | -8.63956 | -50.0382 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e65d62ca-b1a5-3dad-8fed-f638273e95ae | -8.63675 | -50.03938 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76fa7ea8-0a1d-32c7-ac88-9970540423fa | -8.34207 | -49.51546 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82e8028c-5d25-3527-9696-bc4e36b32319 | -8.32245 | -49.57038 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 59efd14c-90ec-343f-92a3-fe014de9e7a2 | -8.31769 | -49.56948 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00ca9376-daf8-3986-8e8a-aaa50e54fb70 | -8.31674 | -49.57475 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 131f83dc-d9ce-3c4e-abb4-0bd444001e2a | -8.31293 | -49.56858 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e9399cb-c857-33e1-bdae-198f73cd74fc | -8.31198 | -49.57387 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae36109c-1e53-3c4b-8c24-6b031032740f | -9.60008 | -50.18004 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 922c9b52-795e-3128-b25b-a4a9b62211fb | -9.59879 | -50.17617 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f687a85-2aeb-32f9-819a-7b3e89010b24 | -9.59778 | -50.18161 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47eb18e3-8199-325a-a11f-826abf6d6b00 | -9.59619 | -50.17369 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1de4a23-d13b-3748-b821-e73474f53eb1 | -9.59522 | -50.17915 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6aedd661-ed19-3ba6-8c1b-1230b4fd2e73 | -9.59494 | -50.16984 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a70939c2-017c-3b90-8d59-00ba26dfdfad | -9.59393 | -50.17528 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4a782f1-1b63-3dc4-b295-ac8ce9e4a079 | -9.59292 | -50.18073 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd86d831-6ce0-3241-b1ee-870df51ba83d | -9.59133 | -50.1728 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82282b10-f5a9-323d-95c8-5ab9ce0c2711 | -9.59109 | -50.16353 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac407147-c701-3316-9ca8-f1b2f1a62a19 | -9.59036 | -50.17825 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61f2ca7a-0ed0-3142-9996-3f9d62c99a9f | -9.59008 | -50.16896 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32f319db-ff57-3574-a565-fc8dfe3d5de4 | -9.58939 | -50.18369 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f9ade994-d82c-3d70-8e88-2995a1dc68fd | -9.58907 | -50.1744 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31bdc586-aeed-3a8b-b54b-3b64f41f7e48 | -9.58807 | -50.17984 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 461ebec0-c723-3435-a47f-667d8b44b83b | -9.58744 | -50.16645 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62a82d0c-1a21-35f1-98d2-141a4daba744 | -9.58647 | -50.1719 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 553a80a9-065d-33af-8bda-23c0438965cd | -9.58219 | -50.18441 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98fd5741-4d53-321b-ac6c-e1b097b87d6a | -9.57506 | -50.22272 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2f061f0-b10a-38b9-8289-9a285570fb70 | -9.57282 | -50.22033 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1bf33b33-00df-3723-bcd3-18b6c3f1513a | -9.57184 | -50.22581 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b50592a-fa95-3e74-a32b-d390baf526fd | -9.56696 | -50.22496 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f44616a-94c3-3d22-a17f-48e004acb956 | -9.56597 | -50.23047 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9b16207-7eb9-3012-b050-0b53a8419f4f | -9.56404 | -50.21309 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 260caa48-ae20-3e07-a366-8c03b6262110 | -9.56016 | -50.2067 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad1a6ddd-d635-3a60-ab7f-fad51f8738e5 | -9.55917 | -50.2122 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f42ce6ee-c17e-3956-96d8-6ba4afb8f00d | -9.55818 | -50.2177 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaeab25c-5410-3d8c-ba98-c35551ff3fbc | -9.5533 | -50.21682 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb40b88c-9dfd-3d08-9194-0f5d6fb28e7a | -9.4982 | -50.1997 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51fbb272-d8b7-32d6-a28b-1b8ba4e349b4 | -9.49578 | -50.20074 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43ed97f2-ce31-3352-8eda-641804c8f294 | -3.56272 | -49.44662 | 2024-10-04 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53956cdd-0d2a-392a-a84b-c2783d01b04d | -3.5622 | -49.44967 | 2024-10-04 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f57d72f-0385-3fa9-8751-a1e72000117e | -3.32224 | -50.07541 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c66f2236-a847-315a-b763-2f788615a409 | -3.31686 | -50.07457 | 2024-10-04 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a297ac6a-8d43-3d32-a34b-1c8ff2b240b1 | -3.31105 | -50.45171 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5153b37-2569-3a96-82b5-2c4300f80d5f | -3.31044 | -50.45534 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5cf72b5-8200-3e1e-8b41-3a61198c181c | -3.3098 | -50.45909 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54e65547-7fef-3b1c-b944-cb199172800d | -3.30614 | -50.44732 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2cf8558-b584-310b-bbc0-9a05ed526030 | -3.30552 | -50.45097 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 570ef62c-fde3-3203-83d2-1b6f3e97ade8 | -3.30427 | -50.45831 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 2ec64079-613e-3e0f-90bc-54c98266f89a | -3.30365 | -50.46196 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| b9eb0e0c-89f0-3b11-b9e7-3559769c2a1e | -3.30304 | -50.46556 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93c41c28-fcda-3b2e-99d0-1849ac949b91 | -3.30062 | -50.44653 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2573538-f646-39d9-89f9-994c6a0ed2dd | -3.3 | -50.45013 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 18ad5eef-c640-33ac-8e55-e0c66c42f0b8 | -3.29939 | -50.45372 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8501e296-fcca-37e3-800f-841aa1bfad24 | -3.29876 | -50.45739 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 16c4acfd-55c7-3680-83e3-38771c19f8de | -3.29813 | -50.46109 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| a85022ac-b59d-3b78-8c78-66e123b85fbb | -3.29752 | -50.46469 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21f79448-1596-35f0-9efb-e860b4c496f9 | -3.29509 | -50.44574 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0dbe6ff5-e93a-3a24-ac52-9784d18fb439 | -3.29448 | -50.44929 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 6700f830-0021-3534-8ed6-f26bd8c1d54e | -3.29388 | -50.45281 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 06f499fe-02d2-3eca-a8ad-6ce2572aeed8 | -3.29326 | -50.45644 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b101459e-8fa7-3e5c-922a-c3d2dc448ad1 | -3.29264 | -50.46012 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| c7c76538-6178-3e0a-b01e-dd5324ca5976 | -3.29202 | -50.46374 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c38eb36b-ce7e-39a2-8ddb-0d0d560c914c | -3.28959 | -50.44482 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 142280f1-7070-347b-a96d-6b808a69975c | -3.28954 | -50.44464 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20dbcf54-4ad1-323d-ace1-3975547e019a | -3.28897 | -50.44842 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| f73e7e04-9d24-30a9-82c0-8ea6b069c47d | -3.28895 | -50.44827 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 668832ab-e0d7-3599-95fe-021f615666bf | -3.28837 | -50.45194 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a6c89522-094a-3b78-b52e-41b0a69af36a | -3.28837 | -50.45179 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 596225e0-4f52-3b5f-961d-6bc5b61254a3 | -3.28779 | -50.45537 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f8fdf0e5-8307-3cfd-b464-73af4128a0a5 | -3.28776 | -50.45551 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| f8b8cf4d-14f3-3c2d-a96a-6f50ec59d8f9 | -3.2872 | -50.459 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a3b4a5e7-7b25-3fd8-8136-de310962023e | -3.28714 | -50.45911 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 223d97ea-cdd5-3ec6-a9ad-9045a3537358 | -3.2866 | -50.46262 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7061de2-f96b-388c-98cb-b1771487db8b | -3.28652 | -50.46274 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54a9ba48-46ce-3f06-9705-4b439b97cc51 | -3.26995 | -49.11229 | 2024-10-04 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5564e282-3828-31b7-a239-edc9e48eea3c | -3.25624 | -50.10666 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42233087-c880-3cb2-8074-a717b0a61f46 | -3.25582 | -50.1419 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90889917-e193-36ee-bc0c-123e12ff8dbc | -3.251 | -50.13759 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c54f67dc-2d2a-32ba-a288-28a4cc5ed674 | -3.25083 | -50.10589 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8af117c-fe88-3fc6-b53f-9958365f7fdf | -3.25042 | -50.14102 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa626829-ae8a-34b0-b4bf-4e49bbb5d015 | -3.2465 | -50.36363 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60ed3966-f1af-351c-ba83-f12f0aee5107 | -3.2459 | -50.36722 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 294a33a9-e397-30bc-89c5-99af0c4050f0 | -3.24531 | -50.37079 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 124a1b27-7464-3de5-abc5-c7cb48de72e1 | -3.24471 | -50.37438 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 88da48df-bebe-39dc-86ef-a8110e836e0f | -3.24411 | -50.37797 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 752db58e-5020-3f27-9455-3340e657a752 | -3.24102 | -50.36278 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 052c7a64-b277-346f-a967-2793f624a2a0 | -3.24042 | -50.36636 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b2d337c0-744d-3fe6-8059-f0bbc6acd5d2 | -3.23981 | -50.36995 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4dd5e69e-43b4-311b-b426-9b12e7340e9d | -3.23921 | -50.37355 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 772576f6-fdec-3f22-86c2-cce49c3f1059 | -3.13003 | -50.18213 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a6af105-d71e-35d4-8bc3-c3df345f78e3 | -3.12522 | -50.17761 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a79d87f-951c-3a4e-b7b2-014aa7f5260b | -3.11429 | -50.4761 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 297f8882-3dee-3232-a2e3-42964b59ab37 | -3.10938 | -50.47148 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dba2180d-0106-3815-a2e1-2856776d6677 | -3.10876 | -50.47521 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8803e5b7-19ba-3e7a-a9b9-6aad63d8d824 | -3.10445 | -50.467 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0c5d3a3-a0ba-37ab-b340-caaf1b6222ab | -3.10385 | -50.47059 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e6cf086-46ef-33ca-a696-5ff3eaaff83e | -3.0387 | -50.45464 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae73a8c1-1a10-38e0-940e-9f6f47d45856 | -2.80052 | -50.28603 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README65.md)
