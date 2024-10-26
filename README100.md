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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4ff71f9-8f27-3bb4-9132-d5ff5a79733b | -17.7532 | -57.49987 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8fa18d69-7362-3886-ba91-f74928944873 | -17.75285 | -57.50299 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2b7971ec-264f-3b11-95b5-26fd42c62acf | -17.75143 | -57.51554 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 24ed205a-33a3-3b0a-b7b4-41e4cb27fe79 | -17.75108 | -57.51868 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 7973272b-4727-348c-a53b-d1c29ea9ee46 | -17.75073 | -57.5218 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 5220b79c-af6a-3290-821f-09ec71b067dc | -17.75038 | -57.52493 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 65328335-ee02-3b99-bfb8-33432f4c0107 | -17.75002 | -57.52805 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ab3e811d-311c-396d-ac0c-cf93655d2e38 | -17.74967 | -57.53119 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c2e61a58-b517-3a91-add1-2234ed301696 | -17.74826 | -57.54367 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 06052f51-029d-3717-97d8-3de61aab9f99 | -17.74809 | -57.4992 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f2ef4efe-9bef-34cb-a956-1aa8ac97018f | -17.74633 | -57.51488 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5aeb1de6-2e1b-3387-95dc-bd0451a64a9f | -17.74527 | -57.52427 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1a40ac1e-fe51-3a6e-8dd2-438364652f7c | -17.74492 | -57.5274 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e749145e-e224-32b0-972f-037e2002defc | -17.74457 | -57.53053 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 54b55b06-008d-3217-a0b5-869876d95873 | -17.74422 | -57.53365 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a181fce6-c4ec-3f37-9130-f29105389614 | -17.74281 | -57.54613 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c37a3b89-df85-3ce8-90be-02647be44fe3 | -17.74246 | -57.54926 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 576dcc74-1144-3940-8871-3fad7eeb8688 | -17.7423 | -57.59645 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| dbd4ad74-0019-3bd6-a479-e8f3415b2390 | -17.74141 | -57.55858 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d7fa69d4-0333-3f4b-af8f-473c8a3e9604 | -17.74122 | -57.51423 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1441b672-0b80-3160-8401-ce9990cc65fb | -17.74106 | -57.56168 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 0191e80d-8bc5-3654-ac09-64cc59fe6632 | -17.74087 | -57.51735 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4a5300c6-f0fc-399a-8f8b-07f190aa1be5 | -17.73822 | -57.49475 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b5496e7b-d8b2-33cb-aca2-5f648ab709f4 | -17.73787 | -57.49791 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b23ac5dd-d2ed-38d9-820a-b0f0564c6686 | -17.73752 | -57.50104 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2b7bf2fe-6147-3a8f-9163-7d64865d2b6d | -17.73632 | -57.55793 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7cd1a136-1885-3b9c-b051-af64ef1ff8ab | -17.73611 | -57.51357 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 470be1d9-c0c0-3f35-9ac1-bff88b7c00e7 | -17.73597 | -57.56104 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d2f5bd8e-8f8a-301d-b11b-227a61ddd9cc | -17.73577 | -57.5167 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1f4bcb53-6db0-30f8-b4d4-323d1ec72ab0 | -17.73562 | -57.56413 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| faaf3428-c037-3666-afc9-f7947210dd72 | -17.73528 | -57.56724 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 0e7a6e33-eba6-3cd2-a80a-08d0138058bd | -17.73353 | -57.58275 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 819942ff-b201-37ab-a571-79eb6472afeb | -17.73283 | -57.58894 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ba24821d-5111-362d-b9e2-934b9b0acd6a | -17.73019 | -57.56657 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 04a87a01-cd46-3d1e-a450-5380c6303686 | -17.72358 | -57.48648 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e45515a4-d756-3667-89ff-d262b23b5f83 | -17.72323 | -57.48962 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 10070879-51d2-3847-b72c-5a022fc1abe5 | -17.93646 | -57.53808 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 1b1e0763-b56b-3ad3-941e-ce31f3790ad7 | -17.93566 | -57.54537 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 92d08f55-9931-30f7-8789-a7d17eba1bcd | -17.9352 | -57.54959 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2b13ee37-ff86-3a8a-b845-9081b6fa129b | -17.92329 | -57.5639 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ac8fea9f-b2bd-3910-8298-24f238bac8e9 | -17.91823 | -57.56281 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a285f9ff-5680-3ba9-a860-98e54e4973f7 | -17.89261 | -57.56035 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 006c39aa-46fe-308b-a93a-7a0eaf514acf | -17.88807 | -57.57243 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 009b2d42-c69c-3486-b20a-61feadfc249a | -17.88175 | -57.56516 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aa0deed0-db62-379c-8336-d69b93809e16 | -17.87453 | -57.58444 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8d8a8947-39b2-333a-9a01-60f86a80995c | -17.87151 | -57.58162 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b6157096-6ec8-3ac5-8b51-c7f9505df892 | -17.8669 | -57.57673 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4271ea4a-9726-3d1f-a51d-dac7b23f768c | -17.85424 | -57.59735 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 891e1f45-3a95-376c-9f7a-cabfe011d45e | -17.85271 | -57.61082 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 194e205c-0771-39cb-ae1d-b843add4b3f5 | -17.83871 | -57.55159 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 273d942f-a410-3b0a-8592-94dcf770eaeb | -17.82171 | -57.56501 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3ae3c04f-8d8f-33cf-ae02-cfbcb6b73d9f | -17.93685 | -57.53459 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 7fd0ab1a-1a61-32a9-acaa-934f06703f5d | -17.93607 | -57.54169 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| dc0906ab-6165-33d1-95b0-6702f53f87d7 | -17.92754 | -57.57221 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d7066cb8-ddd2-3775-aab7-5118041266fc | -17.90823 | -57.55957 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9fe90675-0ac9-3d33-ae1e-55a5759380e5 | -17.89577 | -57.53111 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| cfd095fd-6ab1-35f5-8946-6233602054c6 | -17.8913 | -57.57262 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ef3c5921-78da-397e-a762-f4ce525d7a02 | -17.88595 | -57.57436 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cf8d94a8-c43d-3e7e-a436-1e611c4814f8 | -17.88252 | -57.5093 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d886cfc3-44bb-3d92-a38e-5a62df630fe5 | -17.88216 | -57.51278 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 5b134ad4-3669-36fd-91fc-0b220546f3e4 | -17.88129 | -57.56952 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c370acd2-faa0-31ea-aee4-ffc5befba248 | -17.87976 | -57.50917 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 528989d3-0da7-306c-b317-4dd16c59f1ab | -17.87937 | -57.51257 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 11f5d208-f158-3642-b2d7-4732672dcaa3 | -17.87392 | -57.51487 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 018575ec-b876-3107-933f-baa898781369 | -17.87354 | -57.51826 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 25a9f31d-cb82-3753-bd09-cb101fc4c4be | -17.87316 | -57.52161 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 6e6269ce-1eb7-3c9c-a246-496d1c0ed566 | -17.87278 | -57.52497 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cc754701-36bb-38eb-aad4-e4cbea317e05 | -17.87239 | -57.52842 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| eec881ab-5369-3974-89da-00cfeb8b9c70 | -17.87118 | -57.58454 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a6da1af3-2107-3e8a-9a42-1b780567fec1 | -17.86884 | -57.51395 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 14612bb0-132f-39c5-9131-3fd82abc16b4 | -17.86848 | -57.51715 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 121e887c-a6d7-35c4-98ef-400da656120e | -17.86811 | -57.5204 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 293625c4-d53f-3d22-a290-661b4b0ef8f6 | -17.86772 | -57.52382 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8ea9118e-a881-33cf-b10e-567b1961574e | -17.86302 | -57.51958 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 57baa2e7-bec8-38d5-942b-febfc7b4a42a | -17.86265 | -57.52283 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9060d2b0-d3d4-3510-bacd-d70cd71ff1af | -17.86227 | -57.52617 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 30ed8467-4ea4-35a9-a0c8-56c6a3689b5b | -17.86189 | -57.52959 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| efb6e4dd-d8f9-3862-b13e-3b9ec29bd556 | -17.85811 | -57.60862 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b6da4419-2204-3585-b5c0-145d525d8969 | -17.8578 | -57.61136 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1e8e4ba3-9679-3e18-87cf-800b1fe696b0 | -17.85645 | -57.53181 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f22fd09a-7650-3941-b158-3740e7df3517 | -17.85458 | -57.59431 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fe0d9cd4-170f-3502-bc54-ce1d844b0703 | -17.8533 | -57.60563 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eaf1e14a-8ac2-32ec-a413-b0bf00373b87 | -17.84731 | -57.613 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1e4ce1ad-f33c-3657-96d5-203e3c91255d | -17.83942 | -57.5452 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 000c723c-d314-34b5-891e-64e6e61f7895 | -17.82205 | -57.56189 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 454d074b-6917-37d3-8a23-5525be89d450 | -17.81964 | -57.58367 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 56eeca1a-6944-3433-90bc-ff5af3c2f548 | -17.81352 | -57.59234 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 0c6e52f1-c728-36e7-8ba3-9c87a5dcd2da | -17.85719 | -57.52527 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 59afbdf0-16fd-3c57-998c-f2028ec15d3b | -17.85683 | -57.52848 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 052fce02-4b1f-3890-be1b-30e089cf98e3 | -17.85015 | -57.49551 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| e1593c7b-f096-33b7-a2ff-9b144a6f9f44 | -17.8498 | -57.49867 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 492d9604-a7ae-377d-a722-f2130f78a802 | -17.84433 | -57.50116 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f231122b-872f-3de4-b847-16d2bf0e2f33 | -17.8334 | -57.50613 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 50ed736f-8294-3778-b62b-700081bc5e02 | -17.82932 | -57.49602 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 0ca1d648-5f02-36b3-9a4b-5bb37f8f75e1 | -17.82898 | -57.49917 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| a38d779d-d582-370e-8d1e-75def8178733 | -17.82828 | -57.50548 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0ebadd61-6931-37d3-b3f1-f65d8c37c72d | -17.82421 | -57.49535 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 3cad70b4-04e0-3662-8994-caee3670b425 | -17.82386 | -57.4985 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 8b634955-d320-32b1-b221-e89548f964b0 | -17.82351 | -57.50166 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a227dc42-ed50-33e1-89d4-201f8501fd86 | -17.81771 | -57.50731 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |


[Clique aqui para ver as próximas entradas](README101.md)
