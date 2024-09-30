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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1f5e869-ca73-3867-a11c-98a759d11a68 | -17.12175 | -56.17742 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 88ca38e9-a455-3df1-88d9-62f81a6968b5 | -17.1212 | -56.18206 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 32bc32b2-2bd1-3797-9b8a-fdaa556cda36 | -17.11728 | -56.17678 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 913a8882-21c9-340a-9694-14dd92b89b2b | -17.11672 | -56.18143 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ebd46630-4ac5-3a46-9994-77390ed29ec9 | -17.11062 | -56.13556 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 89b3b97e-41b6-3342-acfb-1af80b33918e | -17.10826 | -56.1377 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 21af4e60-ae77-3a9d-aa1d-4795f234de23 | -17.10613 | -56.13496 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fb0e1995-78d8-3469-9d80-28569020b237 | -17.04499 | -56.11233 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ed805a8e-1f01-328e-9717-4b9b2ed08d82 | -17.0422 | -56.09769 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0a1d1205-bf4e-3e3d-bdd1-f91d46611099 | -17.04163 | -56.10237 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 20e844b8-f3ce-3cfc-9ab6-9fe3c7f7442a | -17.04107 | -56.10704 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 262369c0-e4ad-32ae-b80d-cd37f9968898 | -17.02871 | -56.09584 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d7ba7a18-3532-3316-8628-03b8592aa06f | -17.02814 | -56.10052 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3116eb8e-7dd8-3a86-aa6a-b7c1ddadebdb | -17.02027 | -56.08994 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 31c1c3a3-5e42-3ad3-862e-a5261c7cbbe7 | -17.01971 | -56.0946 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7596d2b6-cbfa-3747-8f4e-8cded086934d | -17.01577 | -56.08931 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 73a9260b-f8ab-33ad-9409-6cd632bba2d1 | -17.00968 | -56.17826 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c5198a19-5473-3fe7-a5ec-56d993b3fe7e | -17.00912 | -56.18288 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 29338755-88bd-3abc-bebf-8419924ee4ce | -17.00733 | -56.08338 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f220d86e-4660-38e9-b839-c9915eafe726 | -17.00554 | -56.08151 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6bd9a3cc-825c-3eaa-940d-47818557c414 | -17.00521 | -56.17765 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 769b4853-f499-3e82-bce0-1831de99b79b | -17.00129 | -56.17243 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 69d27347-5471-3d91-a541-c3c64893ac6f | -17.00074 | -56.17703 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a9e01f88-54be-359c-9e6d-d31fc522f6f7 | -16.99886 | -56.17036 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7f8e132c-6845-3b9c-acac-aede50150af4 | -16.99681 | -56.17181 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bbbea864-a6d8-3948-8260-c1bbac54c06c | -16.99654 | -56.08028 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 17231f44-b1ec-37d8-a348-d006629b6428 | -16.99565 | -56.14335 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e85fbbc0-fe38-3370-88d5-e85f15f43c0a | -16.99439 | -56.16974 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3b5a4273-45e0-35e1-9729-d01b4d55306d | -16.99383 | -56.08151 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 94d04ab2-a829-3cd7-a7d9-33969b1cb006 | -16.99342 | -56.14135 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 82cce919-ca35-311f-9042-2a0865eda8a3 | -16.99289 | -56.16657 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0da2e5e1-2256-3228-9220-7cf8d6ac7a08 | -16.99204 | -56.07966 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 618ed5ab-05c3-3e52-85a7-814f2bf2ee4a | -16.99117 | -56.14273 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1d98dfb5-d2fe-34e2-b331-0e86f3e6621d | -16.9905 | -56.16453 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 21ff3de3-76b9-3cec-97f6-fc7c790bdf47 | -16.98992 | -56.16912 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 832ecb27-2c19-3ab3-9f7d-ecff6e7c8288 | -16.98894 | -56.14074 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 73655b78-0531-30c4-9aa2-69f77958b0e4 | -16.98836 | -56.14537 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6ffb6040-1a7c-3153-a852-ef8bb59c3fe5 | -16.98668 | -56.14212 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d06e86c7-299e-3251-a684-c2964e5db0b3 | -16.97507 | -56.10581 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a5ccd030-5421-3c7e-92f7-ff4b4154db24 | -16.97058 | -56.1052 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 173f1326-e867-3762-a18a-aabc546a0ea9 | -16.97 | -56.10984 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4c8030f6-c3d1-30dd-bbae-fc29f0bc316b | -16.76853 | -55.85244 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 10a89187-45df-36e1-a4fb-0a79f4c52a57 | -16.76398 | -55.85183 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 252cd49e-bd74-3d9c-9ef6-0b3e3ae63298 | -16.75148 | -55.84036 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 2578b090-6f73-3f39-a985-1b786f53f37d | -16.7127 | -55.54454 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 63439026-96b1-31e6-b4b1-b38740aa601d | -16.70806 | -55.54392 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| cf46abf2-3fb7-3451-a817-d2e70cf3f77d | -16.60605 | -55.96431 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 92104230-fadd-388b-8d90-9cb58e7fc088 | -16.60549 | -55.96901 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9e268b18-9d54-31e0-9303-28ea72cd9383 | -16.60492 | -55.97371 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bb656ea6-2d2d-37c0-b5e7-82dc38c62664 | -16.60436 | -55.9784 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| dccf39c6-6bf5-38b5-86b1-31b7bc6f47de | -16.60211 | -55.95899 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9501838d-192e-316a-ac7c-f739ec279d1d | -16.60154 | -55.9637 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 782e17eb-e3f1-311b-a992-5402712abd9c | -16.60098 | -55.96838 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 628eeea1-f885-332b-953f-302707d6c2c3 | -16.59985 | -55.97778 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f1c4294a-848a-3fec-95df-66cd694abac2 | -17.26352 | -56.44852 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 242e48b7-d257-35ff-ac31-512ea920a445 | -17.25912 | -56.44792 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d2ac825-9b0c-30a8-a3c8-3c0448930334 | -17.25855 | -56.45238 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cc21e0f8-3380-3186-95a0-467eb163b3ac | -17.25471 | -56.44731 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ea99c352-b2b5-361c-88ca-45e642d2f34f | -17.25415 | -56.45177 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c029437f-22d2-3178-832b-efa259fa504b | -17.15192 | -56.22846 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 9ac51946-6d3a-3d5e-ba3a-69e78197859d | -17.15136 | -56.23309 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5f04f753-126f-3cec-b207-2cdf0fe62d9f | -17.14746 | -56.22784 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 97efc4a1-b3e6-357b-9401-cdb324fd6171 | -17.14689 | -56.23247 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cf684ad5-381e-3e43-8b26-740e1d233bdf | -17.14525 | -56.2088 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| af2030f1-51d7-3175-b64b-ce6aeff4a1c7 | -17.14468 | -56.21341 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 324ec161-3c7e-393e-ae57-8e126da212f0 | -17.14243 | -56.23185 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 44697bb4-e5cf-3519-b4f9-d5896e402e66 | -17.14078 | -56.20818 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 706bc8e0-239f-32a0-bb15-d8e6e21c6040 | -17.14021 | -56.21279 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 90835a86-a0ee-3545-b047-c589975280be | -17.13965 | -56.21741 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 80025d90-ec97-3e2d-9020-04ce5fdec53e | -17.13742 | -56.19837 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 568ae79c-9158-3080-8858-58b749b3ff3b | -17.13687 | -56.20296 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f1a2339b-470a-3fbb-901f-221a8e4a90d7 | -17.13631 | -56.20757 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d08a6ab8-e166-38c6-8e5b-63913cce0a7e | -17.13518 | -56.2168 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 270a555a-0208-3b21-b5b5-7f49d781bf91 | -17.13407 | -56.18854 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d27e028b-ccaa-3c53-8954-795b871809a3 | -17.13295 | -56.19775 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ba881923-8a4e-3714-aa7c-dcc40193989c | -17.13239 | -56.20234 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 51b01573-6c8e-3bc4-a87a-f910266a8c8b | -17.13184 | -56.20694 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2f34532f-1ca3-34a7-b71e-cef487f5bf21 | -17.13128 | -56.21156 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d9f62136-30a5-3795-9ad3-48e8a1a09105 | -17.12959 | -56.18793 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 43afa5e8-7bc7-38c6-be67-5892773c5d95 | -17.12904 | -56.19252 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c4cee9f1-93dc-3243-b300-26f3bc9d2cb5 | -17.12737 | -56.20634 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4a84c010-8696-3c03-9d1f-ce9ce977616c | -17.12681 | -56.21096 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9a97d47d-77f8-38d8-8442-632bba910ab8 | -17.12625 | -56.21558 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cc677d30-091f-3bd3-991b-2326cef3436b | -17.12569 | -56.22019 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 45755b5a-92e0-3add-88c8-abc7f06a0a87 | -17.12512 | -56.18731 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| dd0538df-5aee-329a-bacd-5b0fb64982f1 | -17.12456 | -56.19191 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9f1228b5-b5a4-3d25-80d0-c12cb1f1df6a | -17.12401 | -56.1965 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 18804a14-6a1b-3479-971d-8aa296d2a877 | -17.12345 | -56.20111 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3e045555-3843-3456-9049-070389ae0b86 | -17.12289 | -56.20573 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9a2c553e-4ee9-30fb-860e-4171eacad0c3 | -17.12234 | -56.21037 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 67431a22-710f-3518-99d8-7b4d2e4bf233 | -17.12178 | -56.21498 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d2ace737-03a2-3465-a1e2-040b90ae9f1a | -17.12122 | -56.21957 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2aaa2434-aaba-3c71-a877-8af370c84519 | -17.12064 | -56.18668 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 100f296b-5a38-30be-b806-383444c36e8f | -17.12009 | -56.19129 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 50e6cbc4-5591-3e04-affe-d063176accb5 | -17.11953 | -56.19589 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 43dcfec9-52eb-3ab8-84fd-51ea2a264c27 | -17.11898 | -56.2005 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ec4bc413-08a1-3c0c-a197-baa12c343e55 | -17.11731 | -56.21437 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e37b651c-0c75-3728-88cd-8daf7c5a033c | -17.11676 | -56.21896 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4973587c-97e1-3bcc-b4d4-5878212928a5 | -17.11617 | -56.18605 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1f83faa4-0292-3ca8-9e74-daba29021012 | -17.11561 | -56.19066 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README66.md)
