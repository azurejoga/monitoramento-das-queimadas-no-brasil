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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0be498b5-3059-384c-81d2-89b703fa1a56 | -8.57301 | -54.69933 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c374021f-9b9e-3877-8df6-273e22306aa8 | -7.08205 | -59.18765 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80c1be3e-d13c-350d-9f3c-9d0f5b36470a | -6.28162 | -43.70485 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e84b2a14-4e38-3768-893b-80968c8fa36b | -7.35391 | -44.59414 | 2025-08-11 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df1fec1c-0155-3bc3-9b1e-983f366f205e | -4.0605 | -46.9353 | 2025-08-11 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2286d1fa-bdcf-3dad-9468-2c1738b43aa8 | -10.36609 | -50.82995 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09332a0e-aa7c-3407-9982-998f5a9a1a5f | -9.86781 | -49.95472 | 2025-08-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0acb9bf0-7ddf-33b1-ab3b-f75454f94a45 | -7.2185 | -46.23655 | 2025-08-11 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91b1e647-6c5d-3ece-a296-94a413f13289 | -8.55741 | -54.67438 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0803b333-6f77-3b70-a4f1-c84390801d83 | -8.56911 | -54.69304 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 639a5d94-49f8-30ea-a39d-ad86d5878e58 | -7.15944 | -44.2835 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27a4638c-792a-39c2-b136-8d6e08573c6d | -11.75267 | -45.02986 | 2025-08-11 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88b50c01-0173-3fc0-8e35-6ce691c09dc9 | -10.36683 | -50.82558 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb92c815-f96f-37d7-9abd-cdc6ea3d5be1 | -7.07702 | -59.19012 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14afd4da-62ea-368c-974f-540aa4c6bc6e | -5.48625 | -44.3949 | 2025-08-11 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 32f37770-b8f7-3ae5-ad4f-8ca2dabcdb96 | -8.57097 | -54.68243 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c2f49d2-91a6-3f31-a91e-a0cf82994e40 | -7.16752 | -44.277 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e04e86d7-f2a5-3a25-a7d0-febc4475559e | -7.05511 | -59.19756 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 438c1d61-5b0a-33af-9c5a-4f035fe9cc35 | -7.16983 | -44.28515 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3dd75ed5-a281-38e3-9ae9-11d085ed2d87 | -5.48683 | -44.39122 | 2025-08-11 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 91fb3938-985a-311d-b095-5c2130332e5c | -7.0595 | -59.2107 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f01b9626-ac31-3649-ba04-251f31d15b33 | -8.56333 | -54.69754 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5e86f22b-3f3f-3585-9887-f75ba75dd367 | -6.9789 | -43.09285 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8071f95a-7061-3000-bc47-0677ac0c256e | -8.56726 | -54.69496 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ecc0606d-1d5d-3cbb-a6b6-fd9f2c3e52e7 | -7.17098 | -44.27758 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12f686c2-0729-36ee-8dc8-ae622e3362cc | -5.4874 | -44.38755 | 2025-08-11 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd4f2e8d-009c-3347-9ece-7bcd20624a00 | -7.31799 | -44.69182 | 2025-08-11 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15110fbd-1639-3445-8377-86416ee32ee6 | -7.61971 | -45.18769 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b936024b-f04f-3861-a914-236c5df8bd26 | -6.27927 | -43.69653 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cba59744-006e-3ee8-a4ab-73fa9b3cd5ac | -7.61186 | -45.19384 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c05f7b85-b301-37eb-8a18-6aa828e7b2ed | -7.16349 | -44.28021 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95481968-fee6-3dab-9923-b70a9b491029 | -8.56533 | -54.67819 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fbb4731-e90e-3ab3-8626-ca4186f55498 | -3.64965 | -48.32652 | 2025-08-11 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb87f5f3-3440-32ca-89b5-83b7ae3a073b | -11.75327 | -45.02583 | 2025-08-11 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4349428c-a23e-3ec9-a857-9168fa0f5725 | -6.31058 | -42.34846 | 2025-08-11 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 46271209-f09d-3e55-83d5-a4413cfa219d | -7.06719 | -59.20618 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4606d6f0-6fce-35bf-bc95-0a90bbe1a7a2 | -10.36976 | -50.83062 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4554b964-dd48-32b6-bcda-b4fddf2112d4 | -10.30855 | -48.11163 | 2025-08-11 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc32d803-0533-3621-adb1-8565060e6bf0 | -4.10946 | -48.12368 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 834e68d6-305b-3e41-a8fb-70cee1ea1e88 | -8.56037 | -54.68594 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88e20d85-9821-3968-8243-8998680f4311 | -3.50982 | -50.74635 | 2025-08-11 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a169408b-3867-3402-a23c-cffc5af7d4b7 | -6.29156 | -43.71051 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cff79b8a-5e92-307e-af0b-e4e160c8c0f7 | -6.57746 | -44.56676 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 500f504f-d848-30aa-be20-de36f906f495 | -9.19754 | -59.68381 | 2025-08-11 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd28de59-9c05-31e1-8816-c627ff129ab6 | -6.58144 | -44.56358 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8eae0c41-e48a-33f3-8a55-6b34fe02ae52 | -7.43062 | -43.75754 | 2025-08-11 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2875134-1a88-3d95-988b-0d27857b40a8 | -7.06283 | -59.1929 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2df58208-ddb4-389b-b129-9cb6f6564807 | -7.08861 | -59.18911 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd559fe-6e19-3a11-865a-0cdb2cfd2c03 | -6.58704 | -42.7695 | 2025-08-11 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c5a774f9-bb56-3341-898c-c316cf4c375e | -7.60737 | -45.20054 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 784f7271-4d59-3e80-bd1c-c639618bcfd0 | -8.57394 | -54.69398 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c853431a-c45c-392f-9dbc-127993e07685 | -6.5894 | -44.5572 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd340090-df4e-38a4-bb3e-06e0e732910d | -9.2072 | -44.53424 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46b9f079-8214-3968-bceb-cdd21f3b74b1 | -8.57209 | -54.69585 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fe4daa9-5fba-3da9-a033-996f3c1e33c8 | -6.29096 | -43.71443 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef8428ad-262c-3e7a-980c-2ceae0bfec75 | -7.87419 | -44.96869 | 2025-08-11 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 607a3d5a-a132-3a47-9567-3e372ed8b931 | -7.12687 | -44.22833 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbb0da8b-a755-38ab-a57a-8ac014706a6a | -7.06489 | -59.18183 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbcc8537-d8cb-3515-9f83-069bc19a1ebb | -6.57915 | -44.55566 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 959c8b66-5161-384a-aa2c-a348cb1996f3 | -6.92673 | -42.96576 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 880e5bb4-20e6-3244-9a73-62d6eb2a8441 | -7.61129 | -45.19747 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 163cff29-6a2f-3879-bc85-134396fbdf21 | -9.86847 | -43.54776 | 2025-08-11 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d51f57e-d752-3f7b-b1e3-c017bfaa7d9f | -4.29634 | -48.07088 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 732baa3b-ff33-308d-851c-7570d18ebc85 | -7.22235 | -46.2336 | 2025-08-11 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c96b01e0-9744-3cd5-847e-85ffa9949f51 | -7.07756 | -59.21098 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22e821d6-33ea-3b6b-aacc-2c1399e7f762 | -10.36317 | -50.82491 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb153f9f-019a-307b-999d-28dea8b2fff4 | -4.48114 | -44.93447 | 2025-08-11 04:25:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| acdc06fa-ade8-30b6-a806-f7bef5b6f2f2 | -7.61859 | -45.19492 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61a49f95-7eae-3afe-8035-8f095d310bde | -6.28685 | -43.71781 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebafedd7-ed20-3a8d-8e86-006fe5849784 | -6.42185 | -42.35362 | 2025-08-11 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 705c5ab3-5e00-3eaa-8fe8-002f8fee3ff7 | -6.9819 | -43.09771 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17efda2b-80b6-377a-b8b9-05700fb1dc76 | -7.05289 | -59.20946 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b8286ac-18d4-3898-b689-ad8a343c4407 | -7.35392 | -45.27916 | 2025-08-11 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95af64a2-d1d7-3a11-8538-805d00129bce | -7.27818 | -44.58685 | 2025-08-11 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 732f40de-3ada-3f94-8927-fd16cb5ad9ed | -7.06609 | -59.21214 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e69ddff3-7f04-3e2d-982d-09635c159655 | -8.5692 | -54.68435 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9324791b-99c2-306d-85c7-b4a3d5e5450b | -5.8166 | -47.32104 | 2025-08-11 04:25:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00b7bcdd-242b-324b-8ab3-3af50b354c48 | -6.98059 | -44.79255 | 2025-08-11 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 814ac4a6-c57f-3c91-adb1-56d313e1e46a | -7.69646 | -45.54704 | 2025-08-11 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbce3e36-51a9-3a3d-ae0d-6ec1a403e6cf | -9.20778 | -44.53036 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 710f8f78-e3c2-3d11-8a2f-f3a1c52724f4 | -6.28512 | -43.70546 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d89007df-2500-3617-8d05-7346a011b471 | -9.20429 | -44.52981 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dac66cea-2eca-3dbf-9972-bef98fb5a7ee | -6.97248 | -43.86769 | 2025-08-11 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4283ff56-241e-3659-8467-1dade6cdbca6 | -10.327 | -48.3122 | 2025-08-11 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 83274da2-4065-3e4f-8276-aef305bae53d | -6.57633 | -44.57416 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9326aa86-f1b5-3b16-9534-d7c38fcb25b4 | -7.61578 | -45.19076 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c57434e-9064-363f-82c7-b94a23493282 | -8.56241 | -54.69411 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7bd314e-207f-3a3c-9f29-b7b4d695f809 | -8.56799 | -54.67093 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a33bfeae-6015-3947-9585-376fd3e2e1b2 | -8.98652 | -45.69175 | 2025-08-11 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf40a18d-d98b-384a-b525-38592aedc9de | -7.07915 | -59.17866 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc1760f8-7e9c-3329-b640-4c55deb09c20 | -7.11935 | -44.23109 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1926d234-7040-3994-924b-072cc35ede43 | -10.36244 | -46.62973 | 2025-08-11 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f09cc06-b9fc-34c0-888e-bd50b4702ee3 | -7.08749 | -59.19491 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4388d14e-8af5-3272-8553-62c89b26c2ee | -4.77773 | -42.71908 | 2025-08-11 04:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 543bb15f-cece-3c20-b9e8-b19ebf25418a | -7.60792 | -45.19693 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e526f0b3-f01a-321a-baf4-52486e6f4bb8 | -9.20488 | -44.52589 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 629c2003-2604-3112-b302-9cb0d142fca7 | -6.97816 | -43.9522 | 2025-08-11 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a366ab9-961c-3308-b9f0-f0b401a4bd9e | -7.06498 | -59.21806 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a225ebc-5212-3806-8dd6-9722d9f56c63 | -8.56143 | -54.69946 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56f991c4-1306-31ac-b745-de57559f9e7d | -8.80472 | -48.78108 | 2025-08-11 04:25:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
