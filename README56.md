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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc0a7106-a13a-37a8-88e0-9c5091f2d42c | -8.61643 | -70.03544 | 2024-10-17 05:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8772627a-f1c0-3321-b7e6-453085b11da3 | -9.50229 | -70.45691 | 2024-10-17 05:29:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c054c533-c967-35b5-b90a-71e9da801b9d | -10.91999 | -69.45718 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3721b479-80e2-33c7-8e86-5862ef21b8e8 | -10.91854 | -69.45908 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a0419ab-3323-38d3-8502-10f63b061b47 | -10.90486 | -69.4141 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b470ee64-49ad-35ad-ae90-a8558e709092 | -10.8997 | -69.41761 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d7b69d7-16eb-35b5-b6ca-4115b0364118 | -10.89301 | -69.32789 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8cb133b-a04c-3ae4-b8da-d5f784b502ae | -10.89275 | -69.56051 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3feec79-7b4f-39cf-bada-e88e98d7b4b4 | -10.89038 | -69.39352 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ffa766-9091-39a3-b33c-5805fee596ad | -10.88961 | -69.39784 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f1f94ae-b3d3-34ba-b295-f68d5dd7535e | -10.88864 | -69.32706 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f307b524-537e-3a4d-b96b-b94b7b129952 | -10.88599 | -69.3927 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa670ff2-4bde-39d4-be80-a13b8656325e | -10.88293 | -69.40995 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5947ed36-e27a-303a-a108-bc3f1b87e768 | -10.86255 | -69.39713 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8e63cd6-2dee-3155-a526-9226962cbe24 | -10.861 | -69.40575 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6340d535-6997-330a-99aa-ddec32663ab9 | -10.84332 | -69.47887 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55f7b1bd-c52a-3120-88e0-ff7fa8501fd5 | -10.72499 | -69.45779 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7e769a1-717b-3c6e-b49f-e5fcaf962f9f | -10.72065 | -69.36066 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24b7a1c6-1e75-3d01-9fab-d3ddc1a56509 | -10.72029 | -69.3584 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7f1fac0-e34a-390e-8ee6-a87754d2945f | -10.69202 | -69.36886 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 571ed7d3-f8dc-373f-b736-014852955fb8 | -10.68917 | -69.35929 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb8e5bce-46f8-33d0-9e73-9fc38d8dc800 | -10.68841 | -69.36359 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6428064-390e-36f3-a2cf-0f678b57a477 | -10.68764 | -69.36796 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74d965a3-499b-3ed6-bfc8-7206ddfdfb68 | -10.6733 | -69.42337 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d99ac8fd-1dc7-34f6-9187-df00ae9a1aa8 | -10.67197 | -69.40518 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6df115d4-06a9-37f7-a4bc-56257de67009 | -10.66967 | -69.41815 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5014f50b-483f-3f92-a320-7b2a5ecb61b8 | -10.6689 | -69.42251 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 721ea2a6-9093-3e6e-a5e9-1963e2b3458e | -10.63306 | -69.59829 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bada45c4-1e7f-3092-b9b7-d27c316dfa4a | -10.58762 | -69.34672 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1be7812b-fddc-3a72-a714-6de1b1e88e36 | -10.58526 | -69.25757 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc34c4f5-039d-337d-8dc5-23ba086427f3 | -10.58324 | -69.34583 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf477fcb-949a-365e-aa85-fb0018047bc9 | -10.5279 | -69.20084 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4281c819-baf3-3ee5-a7ee-6393fe8ec432 | -10.52354 | -69.20004 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b85acf1f-45b6-34da-bf45-ad37ea1f011b | -10.47116 | -69.21641 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb66816c-7f6c-343f-8b6f-a40993ae9c66 | -10.45233 | -69.2968 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ab7754d-9c03-388e-9960-01a32c3d0df3 | -10.39458 | -69.16356 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59a4649e-4957-3de6-a72c-a496209e84c1 | -10.39022 | -69.16279 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee2871a9-249c-3e2d-9590-b03e88b0e168 | -10.18972 | -69.09907 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ffa3a72-c921-36ab-808f-270c62a40778 | -10.18536 | -69.09829 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5ac2b6-25cc-3178-8554-0ea4136385ea | -10.14596 | -69.32207 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbe27fa3-8a27-3435-bc75-67f582b71dc0 | -10.11859 | -69.16982 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc38503b-5bbb-3be0-a377-8c9bc726ff0c | -10.11782 | -69.1741 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1a3bd8a-c185-33d3-b6bc-2c807eec8ecc | -10.11515 | -69.1668 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbb6a306-9ea5-38a1-ad19-f9fd742d224d | -10.11441 | -69.17109 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95389600-330e-3f92-9b71-60f3b665568a | -10.11421 | -69.16907 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49963a7-95b8-3900-9cae-aa669e728b31 | -10.11003 | -69.17033 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad9ea8d6-cc29-3040-bd31-d7ae8de39c64 | -10.10982 | -69.16831 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07a0f7c3-fa42-3d0b-84e4-17a941152c0e | -10.00575 | -69.06959 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6686ad6a-5307-381a-bd59-68094c32a612 | -10.00139 | -69.0688 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5b0d3d8-a5b2-3b42-8b3a-a59eb0a8fe53 | -10.92437 | -69.4581 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d7ef3eb-7cd7-34dd-9f57-f262e84b63ee | -10.92292 | -69.45995 | 2024-10-17 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e1de85c-dfcc-390b-88cd-6d8d025cd25e | -7.94186 | -70.68496 | 2024-10-17 05:29:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa635bc0-35b4-37e1-8e8e-2d2905c4ea00 | -7.93684 | -70.68398 | 2024-10-17 05:29:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f37d4924-8526-3ba1-9eb6-2328dca3cff2 | -8.70542 | -71.02667 | 2024-10-17 05:29:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b725020-532d-35d2-9c34-2d0f19be472f | -8.70487 | -71.02962 | 2024-10-17 05:29:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df12f28a-6f04-34b0-9ea9-6307705e0829 | -7.89397 | -72.44338 | 2024-10-17 05:29:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20f98b24-ed01-3fb0-8350-d512c4cf21fc | -7.89326 | -72.44723 | 2024-10-17 05:29:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92b1d4f9-246a-33bc-91e7-dce0c2ac2668 | -7.89123 | -72.44562 | 2024-10-17 05:29:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bd12005-9182-30e8-af10-59a0ff7bff1a | -7.89054 | -72.44949 | 2024-10-17 05:29:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cead1eaf-9757-3474-b748-09eafed3d18e | -7.8869 | -72.44991 | 2024-10-17 05:29:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1f3562b-6bae-3340-94e9-209ac3503491 | -7.88543 | -72.45773 | 2024-10-17 05:29:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d2dfb55-2fd9-3aca-9b96-a87926970ed4 | -7.8114 | -73.11062 | 2024-10-17 05:29:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0afb4521-77ef-338e-8fc7-31682f727537 | -7.25399 | -72.4824 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8aeb04cd-eff9-3f5c-ab28-89523a01a894 | -7.25372 | -72.47931 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 844265fb-83fa-3b04-9a63-ff9629e2a946 | -7.25303 | -72.48323 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9b4f9d3-2b57-3bac-ba0e-f2d5b4222d5f | -7.2483 | -72.48112 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b928212c-9995-3a69-a766-c5c09b568eb3 | -7.24733 | -72.48194 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0d0e890-d8a2-3adc-8761-857eeb918c16 | -8.30699 | -72.81574 | 2024-10-17 05:29:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda7d681-f954-3c86-8c9c-9a10f7e73a0a | -8.30625 | -72.81974 | 2024-10-17 05:29:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b2e3be-1fb1-3af4-81ff-f958ad78a7c6 | -18.93912 | -54.53667 | 2024-10-17 05:31:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55934e57-8214-34ea-b020-cd268e9e33df | -18.93341 | -54.53633 | 2024-10-17 05:31:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb9f55ed-5858-3014-af87-0e1c76415290 | -17.87955 | -56.85426 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7c39186f-fc4a-3623-8b07-3a3f5a885b13 | -17.8789 | -56.85966 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b15e6064-d03b-3eae-a499-508a3e7d39a6 | -17.87826 | -56.86506 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 39bf88a2-dde9-344e-a20f-86c9624b3c65 | -17.87312 | -56.82592 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d1611af8-477d-3cf3-98b6-540bd572485a | -17.87248 | -56.83134 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bd615d12-28f3-3cc7-b453-4466f12ecd21 | -17.86766 | -56.83073 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6bf7c872-de4c-3e47-8a4a-819070ecbf86 | -17.86703 | -56.83615 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b4a5d182-b14c-3bad-a361-eabbffd24872 | -17.85676 | -56.84034 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8335d3e8-e47f-338d-882f-cb95bfbd4b1c | -17.64884 | -56.23784 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d773e3fb-1668-39c8-b0cb-4a4ca4a8068f | -17.64871 | -56.23229 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c7105e59-2f85-3af9-940d-89d4471f1b49 | -17.64806 | -56.2382 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8fef451c-59b0-3d28-80e4-0736c051bccd | -17.64315 | -56.24309 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ed51d4d6-8359-3abc-b3d1-90111ee8f847 | -17.64242 | -56.24345 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 31ed224b-0954-3db7-9689-a462bafed044 | -17.63884 | -56.23659 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 38531274-f427-3c30-8217-be0ae4da49d4 | -17.63747 | -56.24835 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 880ee88e-addd-321e-a237-cfa418257c69 | -17.63454 | -56.23003 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b25bf4f3-9a21-3d1d-b8a3-33290fbaafb2 | -17.21232 | -56.68398 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5f1ad883-223a-3f1b-a155-8e3d20147707 | -17.20813 | -56.67793 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 876a2725-2b88-3cd2-85f1-290b28599f53 | -17.2075 | -56.68335 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 33adec9e-ce9a-3a94-9855-80a49921e465 | -17.20331 | -56.6773 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cbcb8475-8b84-394d-ab18-0372674dbe8a | -17.15067 | -56.12248 | 2024-10-17 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 54466770-af05-3166-a652-27878ed89e43 | -18.26787 | -56.60997 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f1aa8725-c9d9-3987-a407-cffd737c0ccf | -18.25871 | -56.60304 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| a6efc440-e3de-36cf-9926-4ca21ca82030 | -18.25577 | -56.59712 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 121d1056-45fe-3a74-b906-9bec90f37f04 | -18.25514 | -56.60283 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 01adf969-6f53-36ee-bfb7-c5ad8a48efaa | -18.25451 | -56.60852 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 6b3ba40d-1239-3b2c-a201-3fc9fc542cfb | -18.25447 | -56.59672 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 79b22205-159b-35be-accc-659dd2b30b5b | -18.2538 | -56.60242 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| a193dcbe-a573-39a6-ac8b-bb23482c4501 | -18.25313 | -56.60812 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |


[Clique aqui para ver as próximas entradas](README57.md)
