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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fb63f34-09c7-3bd0-8940-be96c2120e13 | -16.887 | -57.67595 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 534edf06-0d9c-3ff2-9311-e0316ef7669c | -16.88603 | -57.68102 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9a682116-dc78-33c9-ad58-c35bdf7427bd | -16.87653 | -57.70542 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 977fef4f-1c15-39f4-bc8c-c36340ee5888 | -16.85329 | -57.47655 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f8d9ad01-64db-3257-bd8d-1c5a2baa4f67 | -16.84966 | -57.47065 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b61d8777-8770-38cc-96a7-3aa0e72e2c26 | -16.84047 | -57.46873 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7bedb4ca-aba1-3685-a7cc-098b8631d154 | -16.83684 | -57.46288 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 77def153-0605-3cf1-b21e-86418cbbb4f0 | -16.83492 | -57.47266 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 13815e36-3877-3780-b88a-9228369ab647 | -16.81843 | -57.466 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e2965ea6-043d-30f9-9f4c-439203d92a86 | -16.81751 | -57.46391 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d8dc7181-f9e6-3177-9303-1010ece26bfe | -16.81654 | -57.46882 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0f824e63-965e-313c-90d8-8dfe3e24a92b | -16.79672 | -57.37997 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ec82664f-1b74-3791-9dd0-b3cc07506b59 | -16.79169 | -57.48082 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a8d1071d-67c0-3f91-af13-5f9661d479a1 | -16.79121 | -57.38386 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 44d2c683-4e7c-3666-9c1a-5407451c3a18 | -16.78879 | -57.83105 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3ea3a41d-5e36-3a99-89e0-ecb623787350 | -16.78758 | -57.37803 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 91ef85ae-18b2-3730-a854-335a1efa97f7 | -16.78571 | -57.38774 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 617d6ad3-353c-33b2-82b0-07bde53f3030 | -16.7806 | -57.48872 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c9922e88-bed6-3132-8a8a-0a7a9922239a | -16.77965 | -57.49368 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4ebdc6c1-fa69-3001-8a45-475f68817aab | -16.77534 | -57.44151 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6f029c82-5318-3557-b905-7f7c055198e3 | -16.77345 | -57.45132 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7d51a6df-8ab8-3aa1-ba45-525aa982cf1b | -16.7725 | -57.45624 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6c3c66d4-b28c-3383-9f85-e41f2bff9759 | -16.76965 | -57.47099 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c724f8dc-bca1-336f-b56c-5d834fd5a67e | -16.76886 | -57.45035 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e3f75ace-4454-3e35-bf9b-e3ebc096b32a | -16.7687 | -57.47593 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 93ce12ac-6f50-361f-81be-4fe70e7bba16 | -16.76791 | -57.45527 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 17e57356-260e-312a-891d-074f848f8545 | -16.76654 | -57.74566 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3745ec89-4164-3be2-b734-63db945a8f21 | -16.76505 | -57.47002 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d8e622c3-b4e6-3766-9e29-5e4c0371d949 | -16.76482 | -57.74761 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 30d0aeaa-720a-34c0-a860-92ac54cf3464 | -16.7641 | -57.47495 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d23ff203-ac3d-3c71-b41e-2869a3f34841 | -16.76219 | -57.48482 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d9cbd20d-4371-3f87-89e8-be9e225e45f9 | -16.76123 | -57.48975 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ce2225be-d2c5-3b80-b1bd-108d48c1bff5 | -16.76083 | -57.74981 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0bd2594e-2c01-3a7b-af67-b20e05aba0d8 | -16.76045 | -57.46905 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a88a0347-e061-3c50-b27a-d96d81f13c5a | -16.75816 | -57.7569 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d92aab52-7b6a-3de4-aca7-82c1a8b6f702 | -16.75681 | -57.46315 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2e554e24-039a-3faf-8302-04cd70332b65 | -16.75513 | -57.75396 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dbb7c96c-82e2-3610-846c-6465ca514f7e | -16.75483 | -57.8292 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 55b798db-e845-38c5-b7a3-6ebf5105d144 | -16.7541 | -57.75909 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 677dc334-667d-3e9b-849a-070185e7580b | -16.75348 | -57.75589 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ff6e312c-f51f-3c84-a10f-5dae793dfae0 | -16.75222 | -57.46218 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dd5f5c34-a68d-3d7c-850e-0dbe8e5e5482 | -16.75203 | -57.4878 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 16fe1b9f-3d76-3a18-accc-c6900d6b52f4 | -16.75176 | -57.73943 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 33e0bff3-e9ca-3d4b-ba0f-daf87ed5b3d8 | -16.74302 | -57.46023 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2eeb8d0c-4bc6-32b1-81f5-b81c52554828 | -16.74206 | -57.46515 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7e9e6626-4e76-3a05-be2c-3fbeabbfd029 | -16.73746 | -57.46419 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 95735a68-86de-387c-bcf9-dde6e4822778 | -16.73479 | -57.45338 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0a575667-e5ed-314d-aa24-8f93b12c1768 | -16.73383 | -57.45831 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 180e5e6c-4f37-3e93-8d14-7672d67b4a23 | -16.7164 | -57.4495 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eaba78dd-690f-3dbd-86db-c79b5449d8e2 | -16.71573 | -57.46326 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 11f5bf56-0214-3bd0-a258-7cea284fc710 | -16.71544 | -57.45442 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f3d6a4e3-6fcf-363b-a925-e7338df4bbc4 | -16.71487 | -57.44256 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7bf120b1-25a8-3397-b918-c6f553724b74 | -16.71447 | -57.45934 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e7ce9aac-2915-3c44-a5b4-8019637d156d | -16.71394 | -57.44749 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b674ba6f-509c-3d90-9a4a-2c4717f399c2 | -16.7135 | -57.46427 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| afedc264-23dc-3a8a-bbb1-078cb841672c | -16.713 | -57.45242 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c9e695db-e7a3-3980-bc5c-4e8ac63f5448 | -16.71278 | -57.44363 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e30b72e-6178-3145-b152-06e33771f66a | -16.71084 | -57.45345 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a7776739-a6b1-39be-ab83-c730700aa24e | -16.71027 | -57.44158 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0cf55e69-387e-30e8-b0c1-f8df089655ad | -16.70793 | -57.46822 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2c3c28e2-918a-3acd-a2ac-42f2295c12ec | -16.69639 | -57.46429 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3b0e9087-e113-39eb-9dbf-e8eb44224dc3 | -16.68353 | -57.45641 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2ecb0d74-1488-31ff-940e-62565e29231d | -16.68258 | -57.46136 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9f031466-0474-3053-a578-bf7e341d0437 | -16.68163 | -57.4663 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7bc82044-2ad9-361a-a033-ebbe98a9d010 | -16.68149 | -57.29366 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c3b8d34b-28dc-3ce9-b541-cfe73fbcf3d8 | -16.67892 | -57.45545 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e6d566eb-f6cc-35bf-99c6-4c37331d50f1 | -16.67798 | -57.46038 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 619005e7-06e2-3ca1-a9ac-6307bb232463 | -16.67703 | -57.46532 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 11736b02-4f88-39d6-ad22-01911559ded0 | -16.67694 | -57.2927 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5ca44b10-10f8-37d9-a8d5-ba18cf733bd3 | -16.67242 | -57.46435 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7c3a5ffa-c777-3b75-ae33-605261b0e386 | -16.67147 | -57.4693 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ff3c2e3c-dd90-34d8-b824-bb9b877709f8 | -16.66782 | -57.46338 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ef7b9df5-5572-3a59-861c-9e8c419a7ea8 | -16.65308 | -57.31783 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2169f2a3-6dcb-39a3-9738-5ad5b67491fc | -16.63217 | -57.30603 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dbd31a01-c7f6-38c3-9ace-223a9ae322d2 | -17.17469 | -57.39848 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9defe1b3-6bb8-36ac-9cec-e8c216d53137 | -17.17102 | -57.37098 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 14274ede-a77b-35c8-a0ac-8da7b642f961 | -17.17031 | -57.3726 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 363327eb-4938-3d00-82c3-c6ae6dcd0823 | -17.17011 | -57.37579 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 841ecf0a-f4cb-31e8-b33a-8b91ef7989e7 | -17.16937 | -57.37739 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ab79a740-42af-3f22-ae79-642502e32614 | -17.1692 | -57.40232 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 07c218e2-4cb4-3e55-8d8c-9d0bf5aa808e | -17.16672 | -57.36686 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9072b4d6-d778-3b15-8c1c-09051c78a4a3 | -17.16648 | -57.395 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a83b1ef5-c459-38d5-9d9f-f8dc6e6e250b | -17.16648 | -57.37001 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| aec1602f-ce10-37c5-b55b-bcf5507982e2 | -17.16578 | -57.37163 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4b7551eb-9027-38f2-b017-8651e699f153 | -17.16561 | -57.39655 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| ad8a9f06-43bc-3092-91c1-cd82d8a179db | -17.16558 | -57.3998 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 922ac5b3-67fc-3e77-a3c8-340f92f3da51 | -17.16558 | -57.37481 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f08289c4-c240-37b3-b680-75c2ccdd7a55 | -17.16484 | -57.37642 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 49368dd3-84bc-36e4-b71d-089adee749e9 | -17.16467 | -57.40461 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 108bfb25-28dd-366f-82e9-1d74a437c051 | -17.16467 | -57.40134 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| e90ad9f6-7496-3fdf-885c-a134245a36d2 | -17.16467 | -57.37961 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8377e0e7-50bb-3907-ac03-860c621e582e | -17.16389 | -57.38121 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 60066544-cf7e-3065-8130-0ae375218d1f | -17.16372 | -57.40614 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 01d890d7-bea2-3639-99f4-cbf56d29db6e | -17.16286 | -57.36425 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3c3b9659-797f-31d3-8522-b65d077e0f81 | -17.16219 | -57.36589 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7c90c7a4-0d4b-3309-8b29-17bb5912b725 | -17.16195 | -57.36904 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 836e2afb-63f0-36ff-b136-996de7489682 | -17.16194 | -57.39402 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5d038e9f-d88f-316c-8838-5f534eae1fb1 | -17.16125 | -57.37067 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fa5a6ce8-4e05-3a3a-b532-935df8f784c9 | -17.16107 | -57.39558 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| eebfe2cd-aada-3c51-bb9c-a9cd9e878ba9 | -17.16104 | -57.37384 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |


[Clique aqui para ver as próximas entradas](README130.md)
