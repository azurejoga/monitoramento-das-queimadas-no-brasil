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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf94bc2f-9f2e-3df6-b45f-90d60e049c73 | -10.05288 | -68.59021 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f0b248-4e16-32bd-a2f3-474f3970d799 | -9.89297 | -68.89169 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fea112f-ce00-36ff-961f-6882763ec7bb | -9.89213 | -68.89602 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bfd5259-4d67-3ba5-90f5-37d922ba3ce5 | -9.76012 | -68.52874 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6d66646-91ab-38b3-8a5f-829bbf7b970b | -9.67556 | -68.81052 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 695ed93e-67f0-3fe9-9341-fe634bc15986 | -9.67474 | -68.81477 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52f615ae-77a9-35a1-b61b-5f907fb5a6a2 | -9.67391 | -68.81903 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 006b0daf-5388-3408-86d9-98b2a4bf7c22 | -9.6717 | -68.81234 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ecb23e8-6c15-39be-9895-3733ac950aac | -9.67091 | -68.81659 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c027e82-60d2-3faf-bbc2-8ce2882deb6a | -9.6205 | -68.60719 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3c3c5c-5481-3750-a494-298c16c2458c | -9.61973 | -68.61135 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06602b14-fd53-3b4f-ba32-9f46b838c5b2 | -9.61938 | -68.60952 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8eaea66a-12ac-30c0-8864-9bfee89b9fd6 | -9.61269 | -68.73862 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19c540ff-19bc-33a5-ae4f-1f1645bb01dd | -9.60682 | -68.73757 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c12ec953-0a7f-3f67-95ed-4ff676810cc2 | -9.53827 | -68.56477 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50b05383-504f-34f7-a3e0-0168ab1d94a1 | -9.53247 | -68.56366 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87790b6a-5ee1-385f-aff8-17cb7a535ab4 | -9.47943 | -68.53216 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b113733-096d-3298-8177-81d0c635ba32 | -14.74409 | -48.78357 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8335dc1a-6940-31df-b875-f4f590b1fec5 | -9.47365 | -68.53096 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c60f3e2c-ad98-35a3-b3b2-e83aff2dae99 | -9.46863 | -68.52571 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfbd5008-c08a-39eb-ac85-3f198e2ef613 | -9.46362 | -68.5205 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ce89aa3-26e2-3f67-9912-04ca065d0566 | -9.46284 | -68.52463 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e1c69d0a-02f8-345c-95db-0ee859b8019a | -9.46206 | -68.52873 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3ee56d1e-f719-35e7-a80f-61c3ef850785 | -9.45704 | -68.52354 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a07472b-c65e-3dfd-91f8-2af3d3ee7189 | -9.40263 | -68.30491 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26653766-7200-3d89-9e94-1d8415e0cc13 | -9.40188 | -68.3089 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c27ef63-8989-3291-b9f5-c1b73f9e3f30 | -9.39615 | -68.3078 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9b6c3d5-74e9-3718-9c24-64922e0b73d1 | -9.39375 | -68.25781 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eff6ff8-c0d1-3411-bac2-d4461cc97486 | -9.393 | -68.26178 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b52cc0-8a90-3c59-8b18-ae7831d96e6f | -9.38803 | -68.25677 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 079a8e5d-bc8b-32cf-9597-414ba7d5ea55 | -9.38729 | -68.26069 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bebe4870-9fe5-3675-b0a8-39720d2af366 | -9.38252 | -68.70206 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6940c6cc-0b91-36f3-8a28-fc9b038eb2f4 | -9.378 | -68.34111 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f412c0f-4200-3182-aec4-5c305aa17c9b | -9.37725 | -68.34507 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78c8fd48-9db8-3fe5-b9f9-c55302152a5f | -9.37649 | -68.34911 | 2024-10-02 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14bf8842-ed24-3f99-82e3-600886a3d75b | -9.63292 | -67.46886 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35bd49e4-d6fd-3962-9d8d-5692f33720cc | -9.63226 | -67.47235 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0728bdb-d40f-381e-b7bd-f3c520181368 | -9.61484 | -67.43654 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7ab012e-a0bb-3e67-a221-a5fc1356e6c5 | -9.6142 | -67.44005 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71cdeb12-e947-3a59-a18f-9302bdd74f5e | -10.61591 | -67.87018 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7f3e428-c694-3a91-9c87-e8b4ae4acd11 | -10.61087 | -67.8707 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ec50b70-afea-332a-8831-78c9e8295966 | -10.61048 | -67.86904 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab69a9cd-3030-3f94-b833-cc1600d58d41 | -10.61018 | -67.8743 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b145be97-9536-39e4-9052-c1cefe9d206d | -10.60982 | -67.87261 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e098166-9b73-3482-bca1-4a4eeaf0f510 | -10.50299 | -67.89917 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 565990c0-87fd-3437-aa87-7703f93022b0 | -10.45388 | -67.89086 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| facf75bd-317b-318b-a237-b6e9c4c71786 | -10.45322 | -67.89436 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cbca1c4-973d-3139-916b-484ab4c8af33 | -10.4484 | -67.88986 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d8c425c-204c-32a5-a70e-4f9ab1264d6e | -10.44774 | -67.89336 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d72ebc40-3160-3ded-ad57-bba0bc585a7b | -10.41118 | -68.11722 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbf71286-3994-3263-b1ce-43e73c9e64c1 | -10.40562 | -68.11618 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd2fc011-8abd-3800-aba7-81a0c7cb0f8f | -10.39125 | -67.95402 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a5a19af-1e2f-3249-9df0-d350efbb7c74 | -10.39083 | -67.95346 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61afc7eb-a74d-3dfa-a146-ee48428197e0 | -10.39059 | -67.95761 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d9aa40c-8ec0-3fa6-b51a-351a211c9d1d | -10.39028 | -68.13628 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0358513-d79d-3bdc-b330-2544c48e2cdf | -10.39014 | -67.95703 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc6216de-b688-3456-ba63-0dfd5b6c953e | -10.385 | -68.22491 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba681561-eda2-3d80-9627-67745f74ef74 | -10.38429 | -68.22868 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9002a26b-9517-378e-ad18-33cca56ed884 | -10.384 | -68.13898 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb91f95-fb01-38e5-a7a9-f217f8ca90ff | -10.38388 | -68.16991 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53889e0d-1518-3e63-802a-4a136f4f46e1 | -10.38316 | -68.17367 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9ca6c9c-bfb2-3b9d-914c-89cae33ff7f6 | -10.33878 | -67.75046 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3995e700-2168-37b8-a80b-de67580cde0a | -10.33812 | -67.75394 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5efe5dca-1a5f-3662-ac45-3b1a8d7bfa89 | -10.33336 | -67.74937 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12b581ef-1613-33f0-ae1d-7c95e21097c4 | -10.33269 | -67.75288 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba4a913b-55e4-3c7a-b9bb-f3af645bd210 | -10.33067 | -67.7635 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc19b69c-9e8d-31a1-839e-3881fd3272a1 | -10.33 | -67.76701 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 517748e5-b78c-38d8-9603-178e6497d0a8 | -10.32522 | -67.76254 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a72a33d6-b23d-38b7-a06c-434e55f3008a | -10.32455 | -67.76606 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccddc541-26df-308f-881c-94139723cd34 | -10.3218 | -67.75093 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11d6e1b4-150e-333e-a7f0-c5b3ccf62c5e | -10.32127 | -67.75184 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40982663-107d-37cb-b4d9-1e283497e73f | -10.32112 | -67.7545 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 424155ab-f8fa-339d-a7f1-4d422bed8b2d | -10.32062 | -67.7554 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ea80a3d-5f3d-3b9e-b229-5d202423f116 | -10.31909 | -67.76514 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 284c6da8-a46a-3d50-9e94-874da410ee5b | -10.31867 | -67.76604 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ae07eb8-183c-325f-b74c-084198f5223f | -10.31841 | -67.76865 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0aa47583-f548-39e4-8aa3-e39e1332d99d | -10.31802 | -67.76958 | 2024-10-02 05:12:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c5cdd4a-1026-3049-a98e-24af483e1b2b | -10.25976 | -68.01492 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41178dd5-b300-3d2d-8f3e-0b5878b31cdc | -10.25905 | -68.01859 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9833713f-ffbc-322f-a3d2-6378deff4119 | -10.13481 | -67.90154 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97b45c39-e0f3-3539-897e-a70c9212ea65 | -10.12931 | -67.90044 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01ae80b0-7dce-3c53-988e-3050fb34c861 | -10.01375 | -67.55656 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b336780-fa72-338c-9788-78badb7387c2 | -10.01193 | -67.55635 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b6ebee9-b376-3f1d-bcf5-f98e45687f57 | -9.89854 | -67.58929 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a273347-b98d-39bb-9819-cf39e76fef98 | -9.89313 | -67.58822 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e76230c-d2ec-32fa-8b71-df133f540765 | -9.58302 | -67.8553 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fe0a338-d4fe-366c-a660-4ea551f24784 | -9.58232 | -67.85902 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0f3cec6-f6fd-3aed-992f-23b17040faeb | -9.54745 | -67.71284 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78a1caa-61e9-36ed-9df7-de2abd309eb6 | -9.54678 | -67.71646 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e567ded-a055-3b37-abf1-37c50565642a | -9.54195 | -67.71181 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d99148e7-e977-390e-b02e-13e2c2263848 | -9.54128 | -67.71545 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac2c7152-f30d-3e0c-86d1-296d54ee9539 | -9.54061 | -67.71911 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0568d76-8a15-335e-a140-3163fe435e66 | -9.53646 | -67.71077 | 2024-10-02 05:12:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee9f1467-fda6-3ec2-9df7-c753a2b91689 | -10.87794 | -68.21895 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efd1d7ee-8016-3abe-b592-7b3b06628382 | -10.87722 | -68.22263 | 2024-10-02 05:12:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03192e9d-aead-3d06-ac94-4a5be938dbb9 | -13.16262 | -46.32757 | 2024-10-02 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6f44ccb-1ffa-358d-8be1-f7d6073c53b5 | -13.16203 | -46.3329 | 2024-10-02 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8efc981f-7360-3ce0-a759-da91162e6c85 | -14.6567 | -45.9206 | 2024-10-02 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51e9ee28-7912-33ae-a2ea-20b5b4c11491 | -14.65047 | -45.91348 | 2024-10-02 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f0b3bda-f350-3eb8-a19b-af8f1a05420a | -14.64984 | -45.91983 | 2024-10-02 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README136.md)
