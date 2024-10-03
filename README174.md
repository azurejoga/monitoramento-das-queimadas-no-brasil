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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 298a366c-d06d-3bbd-9427-a122e15efc2b | -9.29464 | -65.34674 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 145e948b-6185-30a2-9d34-1f439cd297e6 | -9.24501 | -65.60438 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12b231f2-5ed6-3b88-84cb-cfbf3d337f48 | -9.24072 | -65.60362 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7aba920-b466-37bf-933b-4bf5f2c35d87 | -9.17613 | -65.55523 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c28c24f-43aa-3dc7-bccf-c2d58d33ffb0 | -9.17541 | -65.55932 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acec1ab9-26b0-3d58-bfeb-e9770e9ab8cf | -9.17254 | -65.55039 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c080726-cf03-3b57-8f84-9141ceeb928d | -9.14538 | -65.55399 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69619ad7-ecf6-35de-b6ef-de2386b3234e | -9.13931 | -65.3167 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88dd71a7-a970-3276-bdb4-dbe3023f0f22 | -9.44239 | -64.54442 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4cfbdbee-e16d-3814-8dbe-a821f7b1ae9f | -9.44179 | -64.54792 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| abf16a6e-615a-36ae-b218-0cd970f567bb | -9.43841 | -64.54364 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05ba2055-7f90-33c1-b648-bbecd8dea115 | -9.4378 | -64.54716 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b611cf76-1a0e-3844-ab42-ce844391da06 | -9.4344 | -64.54296 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e631c032-9c22-33f8-8df8-c71f49e38c91 | -9.43379 | -64.54651 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| feafdd92-bcb8-3fd4-966a-0bcae3c6a723 | -9.4304 | -64.54229 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e6a56c1-5881-3685-a919-43ea250673b6 | -9.42978 | -64.54587 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b64c933f-f36f-33b9-a5f0-65af5637cbb8 | -9.42918 | -64.54936 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f3f2e59-e2d9-358e-80db-b07c99c47be6 | -9.42578 | -64.5452 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 359d19b0-bd5f-3388-bd83-f2c2d1c357eb | -9.21396 | -64.41801 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46bdd91b-c0b3-36f2-87b1-9f7b96d64c11 | -9.04514 | -64.44634 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6fa30cd-326a-3c48-a6ca-dede484b7bcf | -9.04115 | -64.44564 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 35c32320-70e0-39da-9e81-8e7b6fa5fead | -9.02494 | -64.46812 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a5f8d36-c740-3001-aa27-354cef9dbe12 | -9.02434 | -64.47163 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 206f3bd9-6104-3c82-ba05-6897035b04eb | -8.95099 | -64.36177 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae5614b9-2b2f-3bb7-b628-97f432d4290f | -8.94701 | -64.36108 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 041c4bbe-95d8-3d8a-9c1c-bcda6fc09182 | -8.94189 | -64.20007 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2826bf46-50b4-38bd-9dc7-5705f6147a00 | -8.80467 | -64.25663 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c98e4b3f-773f-32bc-922d-7d566ce7072b | -8.74292 | -64.18774 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6d5eb1e-daed-36da-8542-b23a8245f03f | -9.94853 | -64.90561 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3624eb48-b07a-306e-b82e-a40b6617f37e | -9.9479 | -64.90925 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1332a2e0-11fe-3c04-a6d8-67570ad28ec7 | -9.94728 | -64.9129 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 862bfbb9-6182-3cba-a8fa-db589b00a850 | -9.94664 | -64.91658 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5499260f-6bc4-3a82-adcd-ab5c9d929664 | -9.94447 | -64.90488 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25218f26-f2a5-36e9-adca-c6f722b1acac | -9.94384 | -64.90852 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ecd7463-016c-379f-81f1-066ef937bff3 | -9.94322 | -64.91216 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d74c5db-9030-3998-80a2-2d433c54486d | -9.94258 | -64.91582 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e75dba9c-b700-3d7f-ae6e-9d75e4b04da9 | -9.94195 | -64.91949 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec8551b1-609d-39ec-87ff-c676342cd9ef | -9.94041 | -64.90417 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25025a50-6cb3-3110-b2ed-6c908199911c | -9.93978 | -64.90781 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9908ca2b-d56d-302c-9019-81be2a996718 | -9.93916 | -64.91145 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f20e7ea-66fb-303b-828d-efc97c31a88f | -9.93853 | -64.91508 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9b6af11-6d49-3231-b22e-95094411aa20 | -9.9379 | -64.91873 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3b7dd9-92ac-3d9b-99c8-b6f5ce32691e | -9.86123 | -64.97682 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7902d97b-b9c8-338c-bc2e-a309a600ff98 | -9.85715 | -64.9761 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d65a8e-5ef1-3090-8656-b8b72be4e33c | -9.85489 | -64.86644 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f2c0e03-ee9d-3399-a6b5-755449e3abcf | -9.85427 | -64.87008 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3554165-ad7e-3b00-b240-3993b54d3180 | -9.85084 | -64.86572 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47c41d17-393e-3643-a81e-9f305ff1273f | -9.85021 | -64.86935 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29ae308d-288c-3b96-92b9-b2d3f6bd7a54 | -9.81885 | -64.95414 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8cfe243-799a-3180-8909-84ccbee34dd4 | -9.81821 | -64.95786 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8985d8ac-5fdb-3adc-9182-b8f663122a15 | -9.81412 | -64.95715 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f18c9d70-88dd-3eec-a002-844b5abe2d4b | -9.81004 | -64.95646 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e10c6fbd-b2d6-31d5-9e4a-db80db769812 | -9.80659 | -64.95206 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01e64e84-e4df-3292-a732-53d9a77c8651 | -9.78351 | -65.85789 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 983bfa2f-22a4-3e91-bc1e-38fbe893fd0e | -9.73201 | -64.90134 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b43e1fe-4102-311a-b8be-7f55f4642229 | -9.70987 | -65.75926 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2abb97b-369b-3164-bde3-462985691132 | -9.70914 | -65.76348 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ce66275-0ba7-389b-a7da-6e7f1e04f846 | -9.70629 | -65.75424 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6a9c349-3584-34f9-8ef4-1fe90ebac4df | -9.70556 | -65.75848 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c3e24fe-f820-3e2f-b387-1d1348bd5225 | -9.64675 | -65.73905 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713179c3-5eeb-3b21-95d0-0744ce1f440a | -9.64602 | -65.74315 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d08190bf-20c2-3ce8-bac4-838c9ce21700 | -10.03637 | -64.9771 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33707d6e-6581-3d2f-83fb-19c022be725c | -10.03574 | -64.98076 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5c87910-cc66-362a-9597-ddfb6ed87855 | -9.5942 | -64.43665 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f270ce1-e065-3b8e-b703-74a1986b311f | -9.59024 | -64.43595 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f9a2207-be2e-3f68-9d64-7fcf0d877e32 | -9.55198 | -64.33172 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7f6cd37-9ffe-367b-836f-ab6fce2ed312 | -9.55173 | -64.32884 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76c65398-c471-394a-9a6f-c903c81fa806 | -9.55084 | -64.33396 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b4fada1-a995-3cd2-a3ef-90823edc8e7b | -9.54804 | -64.33102 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c46b7c9-7a4c-3f51-b241-be0ca1fe2294 | -9.54779 | -64.32817 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a5bf7e-b61b-3dca-b874-d70744806abf | -9.54719 | -64.33616 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad990fc1-8805-3fb8-8760-48d17a125ae5 | -9.5469 | -64.33327 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62227cf3-4b75-3d0d-bdee-ed3fe2dc6aa9 | -9.47967 | -64.68987 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e477e27-e622-35e3-afc5-7f7d47fe1db4 | -9.47906 | -64.69348 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22396428-88a7-3fab-8a38-9bb5c1f89921 | -9.38271 | -65.51459 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e0acf8d-5e92-3c5a-a4da-14b7afa3952c | -9.382 | -65.51865 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6fc10ae-7cd3-341d-9080-017f0e2894dd | -9.37987 | -65.5057 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db4490ab-71e9-32da-96a1-e0824c345bd6 | -9.37771 | -65.468 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1cda18c-c86f-300c-8521-0bcc377aa870 | -9.377 | -65.47205 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e61529f-a95f-30fb-a908-b01440f0ac88 | -9.37561 | -65.50495 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ddef63-22a6-34c6-a0f8-6e00ae8e0f87 | -9.37347 | -65.46724 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffbc100d-80a8-3ba8-a4e6-d9cba49d5217 | -9.36819 | -65.8018 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 207214f6-7a2f-36a6-9723-becd3bd257d2 | -9.36457 | -65.79681 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b77907c-850a-3139-afe7-e32a54854cbf | -9.5988 | -65.67222 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9a8226b-798f-3a0b-ac39-c791cea83d9b | -9.36893 | -65.7975 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f588f50b-6294-3f1a-bca2-7606bced5cdd | -9.34437 | -65.75866 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b98d36af-fbf4-3082-935c-37a021b170cf | -9.99336 | -64.76514 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b43b269b-8b69-39c8-a867-d629aea96d1b | -9.99276 | -64.76868 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4d5d06f-96f6-3cc4-a25c-7418953e906e | -9.98935 | -64.76441 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5867b4b6-3005-3cd4-98aa-f760c189d450 | -9.98874 | -64.76798 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51a7f665-6973-375a-8832-4a6f5e4c57f1 | -9.98813 | -64.77156 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7fb6b60-e2fd-3b82-b41b-1d2533311858 | -9.98471 | -64.76729 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 363de0ff-1c91-395c-99d1-a0aabe6bc660 | -9.97203 | -64.76877 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dda215bb-d62a-3026-8025-547a9e778cd1 | -9.97142 | -64.77232 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61a59aaf-7ff6-3ca2-9cb2-ca34fc50df87 | -9.97021 | -64.7794 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ebd51ce-d83b-37b2-b16f-eb0248e1c5c8 | -9.9674 | -64.77161 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0082ce2-fa03-316c-b813-17be1873523c | -9.96679 | -64.77514 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6903f737-4be2-37bf-af6a-d941314398d2 | -9.96618 | -64.77868 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58df12e8-ed7c-315d-bda2-87a12ca9e25c | -9.96557 | -64.78223 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a63874c-35e5-33fa-9abf-5d11749b0a7d | -9.96277 | -64.77441 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README175.md)
