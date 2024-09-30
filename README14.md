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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a04eec25-1ea8-3d39-8750-2135f42ec34d | -17.06113 | -56.74373 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 0a3282a1-0bd7-3e42-8b7b-f8d242480cc3 | -17.05967 | -56.73374 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 2661362d-6e37-3293-adb0-1b78bc835efd | -17.0582 | -56.72374 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 29db4440-bba6-30b1-90bb-3998ad53af34 | -17.05576 | -56.40589 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| c21eb781-e663-3966-af83-c9110a84f554 | -17.05341 | -56.75522 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.9 |
| 0fea329e-cb39-325d-8b7d-991e503ef683 | -17.05194 | -56.74524 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.8 |
| 3ba5d2f0-3c98-34d9-b5a1-8f262845f99c | -17.05047 | -56.73526 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| da7ae059-a61e-3a0b-848e-3d2bb1084b5c | -17.049 | -56.72527 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 59d87c25-e358-3e72-af0f-14c7fc2e460a | -17.04643 | -56.40745 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| fa841657-1957-3ead-a856-31df87a78f1a | -17.03984 | -56.10827 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 75c0994d-3b4f-3645-895d-212af8de46aa | -17.01166 | -56.1782 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| fb46a963-8238-3746-8e80-023028e9254c | -17.00222 | -56.17979 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| f5f1c981-1ede-3f3d-982d-f6e43ec58f86 | -16.99709 | -56.08273 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 976b583a-f88e-3749-b065-35b67e3df3bf | -16.99305 | -57.99117 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 937945e9-db1f-30b5-b2d4-43e6a2b0f3f8 | -16.99173 | -57.98188 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 40ba3cd3-2f11-37a9-8601-aa577158aa4e | -16.98416 | -57.99257 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 04835cbd-b164-3ad0-9d59-b160adaf627c | -16.98078 | -56.20061 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d5817a3d-e5cf-39ea-8ff3-86e9d2f6db1d | -16.97792 | -58.01253 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d9f06815-d58a-3f58-a52e-ee884b6585bf | -16.97659 | -58.00325 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| c8511e45-9cbb-3296-b696-9c7b3c892c08 | -16.97527 | -57.99397 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 28100398-bbc3-3f6c-a534-4b5081155d58 | -16.97192 | -56.10882 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 2d7d92cf-ab12-3e39-b522-bcb5b614a8e3 | -16.97134 | -56.20219 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 13d1bd77-cb37-3e9d-8565-fcb03e094edd | -16.96736 | -58.01055 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5eebbefa-9619-3d56-85cc-c23638a099f0 | -16.96078 | -57.9641 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 54c8eb3c-74ac-34fc-b143-c17beaa82d6e | -16.95847 | -58.01195 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| fcbb2a6d-7b32-338a-aeab-b2afcb0c2966 | -16.95716 | -58.00267 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 78614bcd-d04a-3006-ae4a-f0ad958db29a | -16.95188 | -57.9655 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 9ad0a52f-8fd8-3bd8-8d5e-1f114df1cb02 | -16.94659 | -57.92829 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 06c2286c-9a61-3dc9-ad07-b6183a270afa | -16.92879 | -57.9311 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ab348c16-2790-383f-8e80-95bf201f7fc3 | -16.88914 | -57.71762 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 0714e383-b7c3-3a8a-a255-3bf65f242365 | -16.87262 | -57.72984 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 4c68c9d8-5ce6-36d0-8717-b89a4a9e3589 | -16.86368 | -57.73126 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| aac7d74d-0906-3afb-90fc-8d412edc7da5 | -16.85962 | -57.70311 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 098a49f9-57cf-3a8c-89e7-6c268b0c6d33 | -16.85826 | -57.69372 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 90698e65-560d-3f6c-bbf5-2dd615caed79 | -16.85068 | -57.70453 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 6f95f2e5-d346-3fcb-8e61-2d990a9dede3 | -16.81986 | -57.55525 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| d22a6225-a497-3692-a904-a1a3f09de082 | -16.80237 | -57.5644 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2b5031ac-e86f-37d4-bd2c-8fb13d81b150 | -16.80101 | -57.55494 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cc56fec2-ec37-3f6c-9cab-7897862297da | -16.79428 | -55.9637 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| b50e76c0-606c-3a30-a3f5-4a3534eba975 | -16.79261 | -55.95282 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| c2475652-cdfa-30e0-b8fc-2b8cd1189094 | -16.79008 | -57.79718 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a2b85ab0-796e-3be2-a814-026ce20e37db | -16.78385 | -57.81729 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 53af2f33-d9ef-3c51-b81e-0002ca2b6a9a | -16.78251 | -57.80795 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| ade61771-2ade-3702-9bb7-60218ce5a25c | -16.78116 | -57.79859 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 75950eec-5361-3709-8096-45b9f2b9656a | -16.77358 | -57.80936 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.4 |
| 601a8282-bf23-37c7-88b8-7566d87415d4 | -16.77223 | -57.80001 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| cd08c20a-ae1a-37bc-8c45-d46a243af5a2 | -16.77089 | -57.79065 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 474e7cda-8111-3598-a9f2-6dd67f72baad | -16.76466 | -57.81077 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 91e26d19-db0c-3671-9085-c85193db2874 | -16.76331 | -57.80142 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 0ecdba4a-d5dc-3967-8c11-9e4bc9ceeb17 | -16.74514 | -57.4863 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| a1462baf-1ef3-3980-8080-bdf9c52799d6 | -16.73477 | -57.47824 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 92179ce9-9d3a-34eb-9103-131be5d61325 | -16.71539 | -57.47162 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 4ebcc098-ba01-3f0b-8166-81066b04f68a | -16.71533 | -57.53578 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.8 |
| d5b62000-994f-3b01-9b95-e15343f94862 | -16.71397 | -57.5263 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 0dd8b574-df8c-3985-a948-195ec951f9e8 | -16.70982 | -57.43356 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| af90e4f1-4b26-36cc-97e1-9a7a50fa91d3 | -16.70905 | -55.54333 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 92a5a401-fdcd-3d74-9457-8688b54db789 | -16.70843 | -57.42403 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| f3a0eb2a-42e9-37a4-895e-f6b2728a73de | -16.70499 | -57.52774 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 8d034ad1-09fd-3f69-9083-a3b9cb19ab97 | -16.70028 | -57.43121 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| e3c2a4f1-7ce4-3f12-82e8-67e7af519fa1 | -16.68502 | -57.45316 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 48c6c051-ef9b-3870-869a-f17b826c25ec | -16.68365 | -57.44363 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 8c8c1d67-06ae-3fa8-bbfc-99a8c09d41c9 | -16.67602 | -57.45461 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 9af5bd08-0e1d-3f5e-9a2e-6a48d12aa0ef | -16.67464 | -57.44508 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 444ce720-fb76-3163-85a5-29bb4a632509 | -16.65025 | -55.23507 | 2024-09-30 01:43:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 996993f7-407b-37b7-93ee-42365e26c71e | -16.64901 | -55.22892 | 2024-09-30 01:43:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| e4fe3985-8873-38a0-af01-2713b2de232a | -16.64841 | -55.22308 | 2024-09-30 01:43:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 6c8e323d-9635-3e61-93b8-2a38e14889ec | -16.6471 | -55.21693 | 2024-09-30 01:43:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 99588f9c-58ae-3de8-b54e-f16772ab95e6 | -16.63838 | -55.22481 | 2024-09-30 01:43:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| f290bcc0-f285-30eb-870e-82ae4e60f3f6 | -16.60328 | -55.98589 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 0e4e7b12-4958-3c01-93d7-db3a6142f9ca | -16.6016 | -55.975 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 29.4 |
| 0a85a0d3-9b8d-3410-83b7-635d300224a8 | -16.59992 | -55.96411 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 664cb6ac-e6d9-3534-8037-8e5903de7119 | -16.59726 | -57.35625 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| e5441d9d-c1de-3347-8093-423b57eae848 | -16.59587 | -57.34666 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| b79998d6-dcd8-3479-9365-c4d6eed4c69b | -16.59369 | -55.98748 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5e0cac0a-a4ef-3be5-a6e1-609d448b0f54 | -16.59201 | -55.97661 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 92ac3fbe-7e2b-392e-ba93-a264f5f97b7d | -16.56809 | -57.40991 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| b6c607d2-f92a-3c5f-9b03-fcffa189d68e | -16.5236 | -57.3583 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 08bfe4e3-903f-3131-a5bb-e78f4a0a45f2 | -16.52219 | -57.34872 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| f20169d6-1252-3d1e-beca-69ad5205bc48 | -16.51456 | -57.35976 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2d4aece8-e948-3851-92bb-96e4700d4f43 | -16.51315 | -57.35018 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 25af9886-d8a5-39f1-9841-b77f1b6d648e | -16.50532 | -57.35738 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 536b9ece-d0ba-3cb0-8006-0ca5f822eb2d | -16.48239 | -57.3905 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| e1af5446-1887-33d7-bb72-d6d829b0fdb6 | -16.47892 | -57.43021 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5a4917a8-ed35-302f-a6d7-992d65447341 | -16.47336 | -57.39195 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| f7ffb98d-06af-3cab-b478-85be1132f014 | -16.47057 | -57.37279 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 9dc44861-daf8-32c8-8d4a-507ce630cf3d | -16.46712 | -57.41254 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2eb1c832-d385-39f4-81b5-fc32fbfe7e91 | -16.46637 | -57.34401 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| de1c7b0a-c3f6-311b-95c2-869b1828db9f | -11.68351 | -58.8854 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4ea1566-2448-3111-a169-c37b53a7bcdb | -11.67721 | -58.90504 | 2024-09-30 01:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92840d24-6570-3e76-9f49-97f817a50291 | -11.23007 | -53.88463 | 2024-09-30 01:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a32e67b8-300f-3602-b6cb-7d99936a0e64 | -11.2272 | -53.86674 | 2024-09-30 01:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| acd2d70d-9251-30ba-ab29-0a4f773eabed | -11.22407 | -54.7855 | 2024-09-30 01:45:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 50ff4cc7-ab28-344b-a752-901be870bd71 | -11.21501 | -53.86896 | 2024-09-30 01:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 4d17de33-0d1a-3a8a-967c-b7da3dbbb4ad | -11.21207 | -53.8508 | 2024-09-30 01:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1088a51b-5be6-3bae-82e9-e0a73e07ddf1 | -11.2057 | -53.88889 | 2024-09-30 01:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7386d4d9-6358-33ae-906c-18c51e876199 | -11.2028 | -53.8711 | 2024-09-30 01:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ccb138b7-dec0-334f-ab9e-27aef9400123 | -11.17623 | -54.77798 | 2024-09-30 01:45:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 78af8627-888d-3531-bfb7-fdd525aec4f3 | -11.06052 | -52.45568 | 2024-09-30 01:45:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 94dd17dd-dae4-30b0-9c6b-4c8c49ade5ac | -11.0544 | -52.46341 | 2024-09-30 01:45:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| eee45a41-149d-35f1-9dd6-e431859ad981 | -14.89082 | -57.98513 | 2024-09-30 01:45:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |


[Clique aqui para ver as próximas entradas](README15.md)
