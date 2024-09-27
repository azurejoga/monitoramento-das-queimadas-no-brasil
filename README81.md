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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c0c515a-74cb-3de9-93d0-291f1f910d0a | -11.19501 | -54.77496 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a47db17a-02ec-30af-bd38-d3499302dd89 | -11.19441 | -54.75528 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99c4bceb-a04e-3497-b882-14f28694ce7e | -11.19361 | -54.76001 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f5c852d-a841-3fa9-94c1-8d098d9314a0 | -11.19281 | -54.76474 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870b37c6-daf4-3288-bc32-ba1e7ae52261 | -11.192 | -54.76949 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95376258-471c-3de5-ae08-8d6963a07e7d | -11.1898 | -54.75936 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ce92b61-405a-3dc8-86ff-2c029dedeab9 | -11.18899 | -54.76409 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffbb6c60-b724-3db8-b4a3-db72cfec1895 | -11.18437 | -54.76818 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ca5733-07c7-3518-a5ec-77b16166560e | -11.18357 | -54.77294 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8844e243-8df6-3285-969a-37587fb9d6cb | -11.17975 | -54.77228 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d3a1b19-9bec-3f51-ae7c-fd6efae6007f | -11.17894 | -54.77706 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e82a8b46-988c-35c5-85b3-88185703c18f | -11.67875 | -54.44464 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdfe95f6-fa5b-338f-9ded-9369dcc4bd5a | -11.6758 | -54.43946 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b3f330e-83a5-37d2-bb10-ff1a5abb5b92 | -11.67503 | -54.444 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ade6700d-0d50-3d93-b9da-b253f61b074a | -11.67208 | -54.4388 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7c9f267-5433-362a-97f1-fdc13f6ed821 | -11.67131 | -54.44334 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b35ab3ae-220d-3792-8c7b-88c1fd231658 | -11.66836 | -54.43816 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ede45f9-d88f-3f9f-a411-f5859cd415ca | -11.22935 | -54.77472 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 53f8498d-185e-328f-9185-3b6e9559da08 | -11.21868 | -54.77425 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 569fc167-ca3e-39b8-87e9-76bafdd795ae | -11.21793 | -54.77265 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8625d0c3-d69d-3be1-ad26-0f1a31c916ee | -11.2171 | -54.77745 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cdef6089-fbae-30c9-b6c4-e50f6ffcb546 | -11.21568 | -54.76875 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d65a7c1-874b-3040-861e-e9c47370dd31 | -11.21496 | -54.76717 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 698ec6be-fc61-3d42-a17a-34c3f1ed855e | -11.21487 | -54.77356 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 460522a5-f4f6-37e4-872e-35f405f81144 | -11.21413 | -54.77196 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe22e926-9dfc-3fc3-ae9f-9f146e1c16c8 | -11.21406 | -54.77837 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 332f6478-ddf5-31e9-b90c-54e8b76fc730 | -11.21329 | -54.77676 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b006d42-f83c-3964-ad47-a6bb490deb8c | -12.44941 | -54.99385 | 2024-09-27 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68ef4b9a-6cfd-3902-9073-1860bb6f1637 | -12.44858 | -54.99866 | 2024-09-27 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 9997b98d-42dd-3781-a7ab-ba3874773c7a | -12.44776 | -55.00346 | 2024-09-27 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f6b9617e-4dcb-3003-aa51-1f5fa2698788 | -12.44479 | -54.998 | 2024-09-27 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0deb3b2f-1203-34e1-b2d0-61a0a58d784f | -12.44396 | -55.0028 | 2024-09-27 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 410b191c-b9b7-34a2-a811-befa218add18 | -7.93123 | -54.72025 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f23d88d-9594-3bd3-9b01-6719d96f0b26 | -7.92725 | -54.71952 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1afc14f2-0e1d-3100-a339-d790443f3b16 | -7.92385 | -54.71529 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23c412e7-2ce2-3971-ba87-3fa7cc6608a4 | -7.91986 | -54.71457 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbf6d761-f186-380c-ab10-98078c7a0e4c | -7.91928 | -54.71807 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e53187b1-6b99-3b03-90c5-aa2b83d65b58 | -7.91588 | -54.71387 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d10f1c93-63e2-3fce-b076-dcd22c559306 | -7.91529 | -54.71738 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d7e1bc3-05b6-370e-8122-fb4f70a4d92f | -7.90447 | -55.12605 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01662ac3-4cba-3a45-8a4b-5897a3484d2f | -7.88843 | -54.7304 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a0c1f9-3d7a-32e5-ae4b-2eaa8320b84d | -7.88562 | -54.72272 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ceda63cb-fc21-3f9d-b5e8-75b393646aed | -7.88504 | -54.72614 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb3203d4-b22e-38b7-b558-cfa2d6a7147b | -7.88445 | -54.7296 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e19305-e48b-3483-87b6-12cf3a16b6ee | -7.88104 | -54.72548 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4b69194-6331-3f76-b756-018ad67d809a | -7.8244 | -54.73301 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9541cbc-8ece-35c1-b7d0-7cc0dc3263d8 | -7.82377 | -54.73675 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22a4f423-b343-303e-943f-4d6785bc48be | -7.82106 | -54.72834 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0789eba8-fb0e-3a4c-aca2-3097428fe9e2 | -7.82043 | -54.7321 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8b97c25-4183-3328-98cb-e797ed8fc2b4 | -7.81979 | -54.73595 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9789f209-5908-3390-880d-60bea4ae8495 | -7.81916 | -54.73971 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b9328d7-2817-346d-b9fc-27292b22cab8 | -7.81707 | -54.72756 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5ac5ff62-6239-384f-a248-9e09b1d44729 | -7.81644 | -54.73133 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f499584-ca1a-3cfc-8334-2fdf89a8e14d | -7.81369 | -54.72321 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b170d54b-a7a5-38dd-80de-d1276b525379 | -7.81309 | -54.72681 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b58e4533-d9ae-3d26-8dab-1de9fbde2b8f | -7.81246 | -54.73056 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7d12911-8bfa-3afb-96c0-3417e13996de | -7.80969 | -54.72253 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0aba75c3-f110-32fe-b799-3a9561e662e6 | -7.80908 | -54.72618 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 912109a6-e4f5-3b57-b2c9-f553d4c9656a | -7.80734 | -54.71201 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 899635ce-81bf-374d-afaf-39b8d100ec41 | -7.80679 | -54.71527 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 242cbf3b-45ec-3d93-b33d-336ad8529ec0 | -7.80656 | -54.74118 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48f77a58-dd5a-345b-91fd-e6a8c23f655b | -7.80625 | -54.71853 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3cbbcc79-9ea7-3647-8904-69ce4323dad9 | -7.80568 | -54.72192 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e51dfa65-8a6f-36ab-9371-f9f6a791622c | -7.80506 | -54.72559 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 444d4d1a-b590-3e47-ae58-7e44cea9a9a9 | -7.80331 | -54.71152 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dce7eeaf-713e-38f1-a67a-60ff91f61779 | -7.80276 | -54.71481 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6720922a-0a58-360b-9edf-2e3bbc5b61a5 | -7.80256 | -54.74045 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e82b39ee-cecd-3ba9-ada5-bf4941cc47d4 | -7.80164 | -54.72146 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ff023b5-6d79-3f30-b8f5-e0dcd863da4b | -7.80101 | -54.72518 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 638eeacf-1d98-35bc-98af-2b2d27d84312 | -7.80038 | -54.72891 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50f5b1ed-ca31-3f7a-880f-34c2b9dddc1f | -7.7951 | -54.73581 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68ce6023-fa82-35b6-ad54-81aa54f94f86 | -7.79469 | -54.71387 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2670a37-e260-3ceb-af9a-c21d16ab9cf4 | -7.79066 | -54.71336 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af0d4833-4503-3ac8-b136-3b8bf7246ff4 | -7.75599 | -54.7476 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76ea87ed-bc77-397d-bf29-a3d491debbf5 | -7.75198 | -54.74692 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 065f5568-bdcc-3092-a990-a9d932723948 | -7.74535 | -54.78563 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d7bf2d1-282f-3a67-baf0-1b11aacd817f | -7.74474 | -54.78918 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e98854c4-3bb8-3f6c-b576-91eea4150733 | -7.73889 | -54.79916 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee0d99a5-df06-3701-b7e0-33db2e5b9275 | -7.73791 | -54.78074 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e5f3d77-ed42-3922-9ccd-93c97d462cca | -7.70105 | -54.79635 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c84feb21-6a9d-33c4-8660-935807538a71 | -7.69859 | -55.33136 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43e7f6e4-b228-3032-8051-6feb24310451 | -7.69442 | -55.33064 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65a5a63b-dd4c-3129-89c2-5b51e3d59a73 | -7.65445 | -55.28872 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4629128-3709-3121-a768-170f2c3f840e | -7.6224 | -55.3742 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fc33a9f-28df-328e-b153-1d79de96f905 | -7.61745 | -54.97049 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5fbbc55-6faf-31c5-b2f7-817d6e52e48e | -7.61679 | -54.97435 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd7da527-f481-3bc1-8363-9c6c480801b4 | -7.61276 | -55.34924 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e96d3ef1-53e5-30e9-b98a-fe02022c71f3 | -7.6121 | -55.35313 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8030f70c-abb0-3615-b0d4-4501b40ceff7 | -7.61145 | -55.357 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce5db4b4-fec7-3c24-972a-e8ed5003fe71 | -7.60835 | -55.27346 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c53174a5-b3d0-3e12-ae8d-f33250002bd3 | -7.60769 | -55.27732 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4338f993-d62f-3550-b0f1-59c305456c90 | -7.60704 | -55.28118 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdca6f0f-1ae9-3cad-a17a-5331a2e05479 | -7.60503 | -55.34403 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 471c4c4d-6342-35bd-9e43-d4096cb5431e | -7.59826 | -54.96011 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54a9a471-54ed-3054-8981-f46361648f89 | -7.5967 | -55.1661 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c549029-ac70-372c-a754-757a9b109559 | -7.59605 | -55.16995 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71bf9ef3-396f-388d-85b5-ad8c33e5e9b1 | -7.57135 | -55.16519 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 100470f5-3a4b-390d-8d73-debf90a9f96a | -7.56785 | -55.16083 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 573534c6-df03-3464-8680-52b07e7aca0f | -7.56367 | -55.16036 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3588555-cf49-3eec-a5cd-480fb6cd8f27 | -7.55852 | -55.12513 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README82.md)
