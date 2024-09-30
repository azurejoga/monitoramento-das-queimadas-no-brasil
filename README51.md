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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f947a04-d2b0-3a7e-aa1a-9b94f91ab0a1 | -16.78279 | -57.81245 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fcee7b81-fe20-3c4f-b3af-2fac155082af | -16.78117 | -57.79595 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e9a59911-0b7d-39c5-8872-5a4cc62cacb9 | -16.77978 | -57.79456 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4bcfeeb0-6802-3398-be85-52584f05efd1 | -16.7788 | -57.79975 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3b38760a-4824-3b6a-9dfc-a011d6231ed8 | -16.7781 | -57.81144 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 84a7ba07-e64c-3122-a9ed-0121f1247a14 | -16.77707 | -57.81662 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fb63214f-4a7d-3b5b-b6a5-6c232e7631d4 | -16.77682 | -57.81013 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 80092a8d-a07f-3210-bc3c-d3f95d0e9b06 | -16.77649 | -57.79495 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 555574d8-5748-3539-8630-21f1810d0e56 | -16.77583 | -57.81531 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0ff24f5c-296f-3c05-8d53-78f7e3ac3b9d | -16.77546 | -57.80012 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bed40b05-c18a-32e6-805b-5ed6396b1033 | -16.7751 | -57.79355 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 267067e9-1ce3-35d2-b2cd-7b1831644a7f | -16.77411 | -57.79875 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 82085e7f-65a6-3d80-881c-0b66cf63bbe9 | -16.77341 | -57.81045 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 871e0fbf-ad07-3ef6-b298-c30bb167ed90 | -16.77312 | -57.80393 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3472cea4-608b-3b99-9b88-b87612628222 | -16.77239 | -57.81562 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0d8095a8-f47b-3d37-98ab-503a34900a61 | -16.77213 | -57.80912 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7a57593b-62b0-3e63-9831-cebc4869a737 | -16.77181 | -57.79395 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| da156823-f083-31d2-b678-0fbd031ab31a | -16.77114 | -57.81431 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 64d92570-ad9d-3133-9b4d-d017078d3fb9 | -16.77078 | -57.79912 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 2fd29b9d-25ed-3c42-bc31-efb3daf24764 | -16.77042 | -57.79255 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 6e28cd57-1ffa-3d0a-8514-ace0c5479a45 | -16.77013 | -57.729 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1c66b757-cfef-303c-b119-e9cb17c33e26 | -16.76976 | -57.80429 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| dd030297-900a-3bae-9bd7-8bbe329ce050 | -16.76943 | -57.79774 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a1042112-36f2-3917-80bb-5092bf2827c8 | -16.76873 | -57.80944 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e8b4678c-5a34-3109-a6ee-c1eb6790adc1 | -16.76844 | -57.80292 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3a60449b-97bd-303b-a9a0-4289d7c1aad3 | -16.76745 | -57.80811 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 541e7ed1-6597-3640-9d7a-f5bbddb006d2 | -16.7661 | -57.79812 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 88f25838-0851-3437-a41f-d59fa0ea5f38 | -16.76507 | -57.80328 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 147d41e0-caa9-3fb7-bca9-c69f9571e2d1 | -16.76475 | -57.79673 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 75e88afa-c210-37f1-82e4-17a256a86de7 | -16.76404 | -57.80846 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9e085f48-27cb-38e6-8dd7-a9e5251df656 | -16.76376 | -57.80191 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 87d85cf2-7e0e-3895-9c0a-f6f6bd4fe96b | -16.71552 | -57.53556 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ad081926-c431-30cb-901c-c5c9a580b89b | -16.71459 | -57.53207 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| c583e91c-4288-37ce-8b0d-ed9e08ae9bb9 | -16.71361 | -57.53706 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 11a08e12-0f3c-37e2-bea5-4ec3daf54716 | -16.71091 | -57.53457 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| dd2f215f-b9f4-37a8-a505-7fca2e8a4256 | -16.70999 | -57.53109 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| be8843c8-829c-33ba-93b1-93f42e9567a0 | -16.709 | -57.53607 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 2985915c-5d6c-3308-9ae9-47f900526436 | -16.70725 | -57.52859 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 29665e9f-dcb6-3fb0-9375-280ff8796de5 | -16.7063 | -57.53358 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| ce100141-7767-3b71-a221-dca64d8c1cf6 | -16.70538 | -57.53012 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 0bf0e122-e177-3bec-a1c7-86313bc78fe2 | -16.70535 | -57.53858 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| a7e5f8d7-fdd7-3d1d-8bc3-de0bc7e9839f | -16.7044 | -57.53509 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 8f27714a-c4ac-307f-bf8b-ec0a37643a29 | -16.70341 | -57.54007 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a749f61a-0332-323c-b06b-24d6a04f3ec5 | -16.7017 | -57.53259 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 9cf4a074-5f59-3a64-ada4-d1793a3fab37 | -16.8236 | -57.48811 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6819be2f-8836-3d26-ad09-126ce87aa922 | -16.785 | -57.49019 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 80fd2208-c4b6-3655-bf3b-aad55297d87e | -16.74733 | -57.48732 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 70355e88-b3f1-3518-b196-e7b37aa5e7af | -16.74274 | -57.48634 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e41fd6d6-67d8-343b-b44e-2f82fffbbd5c | -16.73141 | -57.47686 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1a3e536f-24e1-36b0-b9a9-29cfbe6b2e1e | -16.73047 | -57.48181 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0047e9b1-19a6-31dd-862b-d5c9919c0add | -16.72993 | -57.47849 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e9820e14-74d8-3426-a2d3-0b27a706bde4 | -16.71764 | -57.47392 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3b68d671-e131-3eb7-9b50-769a653d1fcf | -16.71714 | -57.47065 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4c4d9570-39f4-3b11-b217-c92e25f2b092 | -16.71399 | -57.46799 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 63f6b7e7-1d16-3bc5-84af-bb6b7094fd09 | -16.71305 | -57.47293 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 53a5a699-a55d-33b6-8261-0151c5281ce2 | -16.71255 | -57.46968 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4d8a8257-1472-3ae5-bab6-90b8d384c5c9 | -16.71157 | -57.47461 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c13e7295-bae8-3089-a2be-2689482b3ed0 | -16.70846 | -57.47196 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b87a6c70-1b4a-36ad-a029-21babe3cae82 | -16.70775 | -57.42563 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 5cee8697-3bf6-3869-9f5d-0ea7af5dd2f6 | -16.70681 | -57.43054 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| faeeb25c-1f7c-324a-9d04-11ab387f69be | -16.70317 | -57.42466 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 9c8ca706-9793-341b-8e95-5c2e42c5b6db | -16.70224 | -57.42956 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e05cf992-3e8b-3fd7-a5b8-bd5af7c23b54 | -16.69671 | -57.43351 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eb5e73a7-b55c-30ea-8698-9231ddfd4e94 | -16.68566 | -57.44141 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 75819b8f-3570-3c50-bcda-99cc42f48c84 | -16.68471 | -57.44634 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1a3a9e24-9dca-38e9-9c48-fdcdd108ab91 | -16.68377 | -57.45127 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 528ef8a7-b805-3500-9015-eedd589072ab | -16.67918 | -57.45031 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f0d086de-047b-3725-a224-fb75b25292a3 | -16.67823 | -57.45524 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 796739e7-1d72-39e2-8273-4822ea6bb7a6 | -16.67459 | -57.44933 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| bad6c7af-e1e1-33ea-b780-3cf47812e032 | -16.67364 | -57.45427 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b5bdad68-8964-3296-a692-8c244d038ec7 | -16.67269 | -57.4592 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 1ad45370-3fbd-35a6-8cb0-dc50e0a4972c | -16.66905 | -57.4533 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cef6dfb0-2000-31a2-b2a1-d6f90f8d565e | -16.6681 | -57.45824 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 700c9f5a-afae-3388-9ea1-b6d2972c96c9 | -16.66446 | -57.45234 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1cd38f8b-6dba-3d3f-a4c1-3adab3e479b1 | -16.65166 | -57.44448 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5481804b-6cc2-32d4-95dc-21a05d7d456c | -17.10182 | -56.73426 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8f25775d-c635-3af0-a7c6-5500e0b50508 | -17.10098 | -56.73864 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 51e73205-e9c6-3737-9ae6-dd857ab00295 | -17.10014 | -56.74301 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 815ef531-c2d2-3ad2-9430-6194e93edb9d | -17.09748 | -56.73336 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0d59748e-4a83-396a-80bf-1c6437258a82 | -17.09664 | -56.73772 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c46e06d0-2d1b-30ea-905e-e41deb7af73a | -17.06739 | -56.74731 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1c0e8857-9b7b-3e58-a062-cfd3a1366af4 | -17.06468 | -56.7376 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fb5708b4-2ba2-3cfe-ae55-2171cdc4676a | -17.06386 | -56.742 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 160e3fd3-d01a-3f30-85f4-cba73c20eaaa | -17.06304 | -56.7464 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 45aef566-19d2-3329-bc43-05046b6a2262 | -17.06034 | -56.73669 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 530ba90c-bb5f-32cb-9c6a-629c9436eb9d | -17.05951 | -56.74108 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8e9cb5a6-ea6b-347a-b676-8dfd2e24c034 | -17.05869 | -56.74549 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| aa9e5442-269f-3d31-ab2c-0e7431431df0 | -17.05786 | -56.74989 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2921894b-42c6-3b0c-b6d3-543c758b6ddf | -17.05763 | -56.72703 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7da45709-26f2-3dfc-ad37-7375bfda7c6d | -17.05704 | -56.75428 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 6a8d1869-4801-35b1-afe7-df5dc20f4aec | -17.05681 | -56.7314 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e008d439-d1cd-36f8-961b-b6e0edeb8bb1 | -17.05598 | -56.73578 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f82e07ca-0196-3c44-a132-afe6a8e3905c | -17.05516 | -56.74017 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 61a52dfe-bb98-338b-8d09-2f2e07d2ec17 | -17.05433 | -56.74458 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3d6cff04-90ac-349e-9ce0-fb84cbff7ee2 | -17.05351 | -56.74898 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e970f98f-1733-30a1-ad02-c03661f5b999 | -17.05268 | -56.75337 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| a8037016-b655-3e83-a2ee-dbb10cd3fc87 | -17.05246 | -56.7305 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 57fb386a-a561-3ba4-b9be-fe9a5187009a | -17.05186 | -56.75777 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 9547c96a-47fd-3213-80ec-a297e2d8406c | -17.05081 | -56.73926 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b7850d9c-6434-319a-9577-fab230b6f6f7 | -17.04998 | -56.74366 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |


[Clique aqui para ver as próximas entradas](README52.md)
