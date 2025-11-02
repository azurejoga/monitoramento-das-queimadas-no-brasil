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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bd131be-6ee4-317b-b4b2-d0b25bd55322 | -3.56604 | -54.5854 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1b02dc1-25f0-37b4-9d0a-fa415c2c2b0b | -5.12588 | -45.82281 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93b5b558-fa07-37fb-b09e-4c320d3cdc60 | -3.56845 | -51.64057 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91ebd944-b52b-301a-ba7a-b1b293dcd874 | -1.26705 | -53.86119 | 2025-11-02 04:48:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2adfc53-06e0-3d5e-9124-9514edfad1ee | -2.74344 | -52.94516 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 736a3e29-dd89-30b9-8568-f1d167dd2fe0 | -3.56854 | -54.58372 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff129b3b-3597-3c9e-8ff7-1edd78af69a2 | -7.40996 | -40.07492 | 2025-11-02 04:48:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 856d88b3-bcb4-32e7-8d96-4269e09aae03 | -3.50507 | -54.37569 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40a13381-191d-3aba-aaac-90cec5b8315e | -2.61294 | -50.00038 | 2025-11-02 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83c6ce95-7724-3357-932c-6df16b443500 | -5.52032 | -41.10341 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de3b4fbc-6150-37ec-adf3-0d43f07ccee9 | -3.82635 | -52.36397 | 2025-11-02 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce669812-de25-31cc-9545-f291dced9696 | -3.22161 | -50.58361 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ceaeb4e-46e0-3a2b-8c67-fb4988ade0d3 | -4.13638 | -51.15009 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 299062d0-d4b2-30bf-9f24-533934cf0cc9 | -1.27693 | -52.92991 | 2025-11-02 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0267f74-6497-3221-8ad0-75665e1aa782 | -4.13971 | -51.15061 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24d8903c-10fe-3fa5-850e-ef24a4a7de65 | -4.41438 | -48.30402 | 2025-11-02 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f7a4aae-63e8-3968-a7ca-58b91c6f4647 | -4.31658 | -45.63833 | 2025-11-02 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e98aaa-112a-328e-905a-01f08a930018 | -3.93507 | -52.18898 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7bb5a50-02eb-3632-9459-44a4605b7188 | -3.29264 | -50.19876 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9fdeaa0-6cb9-30c9-b3cb-b6ada99918bf | -2.82443 | -49.12645 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40d44754-02c8-372d-9a62-5cc5b3ee7cf2 | -3.43766 | -52.63924 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd211b0c-c63f-373a-91da-6256c4f5e25c | -3.43827 | -52.6354 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1cd4be8-c409-319a-85a4-f6dd05b2af46 | -3.44058 | -51.65339 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e4423c9-871b-376a-94c3-1ef5cfa4d968 | -3.44174 | -52.63596 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2641b3a3-886f-3328-a4e0-3428c5a85b00 | -4.29684 | -45.89803 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a48fa4e3-1155-3d63-8042-8fcf8f4df851 | -7.18108 | -41.93645 | 2025-11-02 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd6b4fa0-10d8-351d-b4b2-ef2003ac8a83 | -4.21544 | -48.35299 | 2025-11-02 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08e897e6-8165-3934-84df-9e9ae3c3c0ed | -3.9627 | -49.29821 | 2025-11-02 04:48:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6398c110-7f06-3cba-89e3-fe35f5124367 | -0.40607 | -52.05452 | 2025-11-02 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00fbfa48-7bda-3930-a8c3-107b3c3fcdff | -1.42556 | -55.23499 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fd4e8c8-32f4-342e-9dec-429d5e3ac297 | -4.29945 | -45.89491 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4e67829-0f79-3ada-a010-e2dbf9412ca1 | -4.20789 | -48.35576 | 2025-11-02 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0660c9d-3d11-30c9-b041-1d68444135a1 | -3.23157 | -50.58517 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eeae8c10-7e1e-3cba-bfdb-51753ff29940 | -3.31992 | -52.56298 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8899bab3-5514-34ad-a91b-18c16013a4f2 | -2.8328 | -49.40174 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bac1a81-4749-39ff-a86f-32882d0364ee | -6.48089 | -42.05967 | 2025-11-02 04:48:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e11ebf50-ca84-34f3-8394-72d194a5f16c | -3.50008 | -49.95467 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5354bf32-8f82-36ed-a7a9-d284c8a948c7 | -2.77095 | -48.01859 | 2025-11-02 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 944ca8a3-23d2-3575-aa76-3fef645f56e5 | -3.43109 | -45.90992 | 2025-11-02 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc27f89b-3d71-33c8-bc89-4d51470477a1 | -3.70975 | -53.37267 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd2670ae-607c-3045-b4d6-12fe61665e20 | -2.35028 | -56.05582 | 2025-11-02 04:48:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cd39020-d2fc-3e68-941e-4141a23d83bc | -0.68759 | -52.37385 | 2025-11-02 04:48:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71c73141-a1ab-31fb-8faf-ac720b97a94c | -3.44114 | -52.63977 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25d5d2d3-76ba-308d-b774-f486056ebda7 | -5.52539 | -48.10796 | 2025-11-02 04:48:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5acc74-99ff-3f9a-912c-a92b98acc81a | -3.56394 | -54.58788 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92f25856-4221-3d24-95ab-680d6d3c83f5 | -5.12131 | -45.82581 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4582335-280c-3c60-bb14-836be19d2e97 | -1.74005 | -54.45847 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fea8a3e2-c067-3e3b-87b9-654c574018c0 | -2.9685 | -50.38436 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6fff3a1-b67d-3197-b47c-e52dac240d8c | -2.37452 | -47.7205 | 2025-11-02 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ee67139-82ee-3a18-a4c9-44446c75d59d | -2.89293 | -54.1941 | 2025-11-02 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c3488cf-aec7-3e21-b98b-8fcf0566bfcb | -2.70556 | -54.65247 | 2025-11-02 04:48:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aadd7eb-ef66-35d6-be33-9ab20c87caa0 | -2.8419 | -49.51769 | 2025-11-02 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec680a44-8a9d-31cc-8ae1-bad7192adc93 | -0.80204 | -47.17445 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fff44203-6fdd-36d6-8d4b-0f4bcf20eb91 | -3.41581 | -49.99855 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bd1506a-908f-34b6-9710-7662d9ecafe6 | -5.12004 | -43.37404 | 2025-11-02 04:48:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4d2850d-be12-3007-b3a6-0212805ab8e2 | -3.77393 | -51.34391 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49373402-6122-3cd1-aa07-98deeffcca29 | -3.41858 | -50.00253 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc48bac1-9200-3dd6-8b24-86a1da1100a8 | -3.28986 | -50.19478 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c19a7e8-6136-3838-868e-dd92cae79342 | -3.80829 | -52.41509 | 2025-11-02 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da4e543e-1ed2-3f7d-b7a3-e3727b138228 | -3.93557 | -52.20783 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4cd117df-5af4-373b-ba16-d8f8fd8e5e64 | -3.06807 | -51.25064 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c4d48b5-3faa-31bd-97e9-f019ef025a95 | -2.74188 | -47.14442 | 2025-11-02 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41bc89c7-f4ec-3a35-bb97-801266842d90 | -4.63653 | -38.56833 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e321d409-3e86-3bd3-af01-4ed778ccf4e8 | -3.28156 | -51.61725 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fe34655-24c6-332b-814c-251c3be7aac9 | -3.5034 | -49.95519 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10163e45-dc0f-3ecc-88ab-1876d98c52a6 | -4.26676 | -48.71794 | 2025-11-02 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1586d6c6-c870-39ce-9bc7-05b36061666b | -4.30342 | -45.89542 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d450b120-3284-3ee3-b501-a190a9c837e9 | -7.32463 | -41.54032 | 2025-11-02 04:48:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 011eb081-9ec4-34e5-a87f-a00b84e280b4 | -1.25407 | -53.84521 | 2025-11-02 04:48:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53c88b82-32f7-3c83-b45a-31989800a6b1 | -3.02253 | -49.4417 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01dfec79-c29b-3cd5-99ef-75e643be86ff | -5.07161 | -43.67656 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e8fdfa2-580b-30bc-a1ed-f11dc66ba1d9 | -5.78518 | -40.8058 | 2025-11-02 04:48:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7964c534-a8b8-3a60-ab69-54d615dfa151 | -3.79574 | -53.88136 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4491cee4-7104-32c7-aef0-a25e2087d3df | -4.7021 | -45.88348 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 074198f0-b420-369a-8715-877330c8941d | -4.63571 | -38.57438 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2da53240-17ee-36da-ac4c-e871f9a4425b | -2.83225 | -49.40524 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee60d95d-b182-3293-b526-7cbf0460b98f | -3.24262 | -50.79244 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f8c7dd0-0821-38ef-b2a7-d6fbadb9e47f | -4.58354 | -44.78773 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f5e1ea3-9a83-36a2-98e4-c8bf0299327a | -4.64223 | -38.57465 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d91bfe97-8f04-3632-8eb2-ab21a669b4a6 | -4.14082 | -51.14365 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71995aa3-d8d5-37bd-9013-16e437bffec3 | -1.49543 | -47.80517 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfa992f3-81e2-3539-9a9e-bc1db14ffa51 | -1.41843 | -55.2379 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1cdad00-28a4-3f78-9703-32ad897b46ea | -4.17999 | -47.65371 | 2025-11-02 04:48:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d7c109-c7de-330f-8143-62cb271f3582 | -3.08146 | -51.25275 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07f7f236-1132-3c01-abe9-0123b0f58f6b | -7.23752 | -44.94201 | 2025-11-02 04:48:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c921b2df-b541-384d-8dea-806a8a1accc0 | -3.92873 | -49.96145 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aca78c2-7ddd-3fb3-ae09-3f0d17276be6 | -3.18505 | -49.78511 | 2025-11-02 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 893bc244-2b95-35bf-b45d-bd4e5fe65df8 | -3.81517 | -50.93922 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26db52b7-f9dc-3380-853a-0ef15510e6bc | -3.18957 | -50.61397 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89a4b133-aee2-3982-a835-8215694c9e17 | -2.64061 | -49.50745 | 2025-11-02 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b516f15-7987-306e-b8bf-9a8166d5c83d | -2.97369 | -51.31536 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a85714a-6efb-3600-9855-09d2e495aec4 | -4.37233 | -49.74103 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2ce8cd4-216a-3888-8a24-8493b487f704 | -2.79403 | -50.29 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c9f194b-c537-3e27-b59d-f7674439d603 | -3.45517 | -45.57695 | 2025-11-02 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55a585d5-482e-3550-adb3-8d5172539b30 | -3.39175 | -51.67169 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe04316e-ba90-336a-b14b-98d61c676ced | -2.63198 | -47.2965 | 2025-11-02 04:48:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0faea2-56c4-3700-badd-8c432ece2644 | -0.8441 | -48.61706 | 2025-11-02 04:48:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 392831f3-9027-3df1-b43b-a7b06abd0f50 | -2.31093 | -48.58947 | 2025-11-02 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75f6470a-bf55-30cc-bc9a-7c4da85d0b7f | -3.51249 | -54.37452 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 732bfebc-83ce-377f-98fb-f16a117e8529 | -5.52404 | -41.08978 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
