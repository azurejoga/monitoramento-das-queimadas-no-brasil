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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fec9e7c-b75e-3873-b01a-099ff668f207 | -8.52677 | -54.5923 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb8c8333-252a-31bd-a903-f19b70b2cc37 | -8.52667 | -54.57963 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab337b28-e727-3658-b597-2b9c001bd3a5 | -8.52566 | -54.59817 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f0e4230-ef5f-323c-a370-29bc792c1c5e | -8.52553 | -54.58542 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ad04f08f-dd61-3478-941d-9acb40b47c0e | -8.52437 | -54.59129 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9fbcd55-7d1d-3ce8-9d23-fde67eda372d | -8.52345 | -54.57369 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8db2e91-2e4f-33c7-ba1e-4a36671351e2 | -8.52323 | -54.59713 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4a0610c-7040-3919-9159-47977833bb64 | -8.52237 | -54.57937 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| deac62b1-0dd1-327e-b1b5-1b8b550c7391 | -8.52126 | -54.58521 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 12790f3a-11a1-3692-bc48-028089e4302b | -8.52115 | -54.5728 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55f307aa-2419-3169-bf10-4aa5e60450ac | -8.52003 | -54.57848 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99816333-02cd-32e5-901b-24325f1d2393 | -8.51889 | -54.58429 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b6ad33b-226b-3db6-a2cd-02ebfbea3d35 | -8.51573 | -54.57823 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a92d896-d2e4-3518-b91c-2882714dc722 | -8.51453 | -54.57163 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8352ef8-3696-366e-994c-c848c1c3eb5c | -8.51339 | -54.57735 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a50dd85-5992-3a64-b0de-ca5342d87090 | -8.51021 | -54.57126 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 997db650-132c-3404-9ef2-90191a93f60f | -8.42235 | -54.70521 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88f5889e-2e0c-3440-addf-8aa922796d16 | -8.41568 | -54.7039 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f4f7556-ad88-3ae3-8360-30b511e0e02d | -9.4622 | -54.56579 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f85ad8c-6ae5-35a2-8c90-a1287b379285 | -9.4612 | -54.57089 | 2024-09-26 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d68af806-34c6-3cf6-a66f-82da3c11226a | -10.58097 | -54.23785 | 2024-09-26 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0906b4ef-4df2-3b1d-9c58-c5ece362db7b | -10.57999 | -54.24278 | 2024-09-26 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9040545f-4dfb-3268-a3f6-87d781d5eba3 | -9.81277 | -53.57049 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9b860c3-c0d1-3b81-8b40-4fb264babe74 | -9.8067 | -53.56916 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63e60147-b9d8-3556-aa4f-5d961a28967e | -9.80668 | -53.56821 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc32b205-2d60-3635-b262-39fc7c0495df | -9.80577 | -53.57301 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5bfcf2f-1570-3a2a-9b3f-15a91cf6a1d1 | -9.8029 | -53.58853 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f907e213-9a1d-3a7d-ab68-946fc07d4e03 | -9.80196 | -53.59332 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5625e65-9d16-36f7-997a-192bd0ea0235 | -9.6679 | -53.53371 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f8a4e24-4aca-3739-80bf-54f40b327b6b | -9.66701 | -53.53837 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b31ef594-a106-336f-b5d9-4ac0aa1b059e | -9.6618 | -53.53252 | 2024-09-26 04:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c514eafb-66aa-3418-b29c-b5ed4e6c13a1 | -7.37696 | -55.49338 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0dc1fda4-17e4-31b0-9f78-78e53be309d4 | -7.37555 | -55.50053 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| e5c46534-4513-3357-a7c3-ffe967353c47 | -7.37417 | -55.50757 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 913f748d-507a-3b3e-a8a0-c5a57973ac37 | -7.37337 | -55.49361 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 85b925ff-0ef4-3504-9815-6cd259b398cc | -7.37281 | -55.51452 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| dfbdfad8-57a3-33d7-ab32-85677dbbe834 | -7.372 | -55.50082 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| e5ecba4e-33c7-3899-bc2d-08ec489b7f36 | -7.37166 | -55.55792 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82d4e328-f271-3140-9658-9a0fa218a0ab | -7.37143 | -55.52154 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7840aca5-7ac0-37b8-b243-74958f518e7d | -7.37121 | -55.5438 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e947c4b6-7cb4-39d2-857c-1d14e6ace79e | -7.37068 | -55.50777 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 01dc1db1-40c2-3609-b10c-3a8e5af29067 | -7.37 | -55.52879 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2fce410f-4000-39b5-93e2-841f38c9e2ae | -7.36984 | -55.55098 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f39bc4ef-73c2-3b45-8856-243774e0143f | -7.3694 | -55.51449 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cffb1253-d520-3a82-9a83-aca2379ec36c | -7.36869 | -55.53546 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 91e936e6-47a5-3b5a-a994-5f0efe54f414 | -7.36851 | -55.55801 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adaaa35e-18b2-3eba-9526-0cc37d643093 | -7.36844 | -55.4993 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| b7ecb21d-9e72-38ea-84e0-03fa4ddd9fff | -7.3681 | -55.52132 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| aebf9bcb-6d90-3c50-b9c4-6a2a5040e4e3 | -7.36737 | -55.5422 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8f24660-2754-3c54-8657-e25207f06e85 | -7.36711 | -55.50605 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 3adc3708-6c3b-326e-bb0b-faeb9bbc0339 | -7.36669 | -55.52878 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| eab8a458-f43b-3c52-9d67-4d84d357fbcd | -7.36597 | -55.54929 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cba62cf6-3c38-3184-a43e-cc06b1195c44 | -7.36582 | -55.51258 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a6dac862-8862-3139-8a9e-39fb4508b0f7 | -7.36542 | -55.53544 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04cf774f-0932-35a0-b0ac-f5d8c7c21171 | -7.36494 | -55.49928 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 04432cfb-b8a3-31a0-8ea1-5d60e1c760ce | -7.3646 | -55.55629 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c1a6c5f-1abb-375f-a2d2-5c0554203597 | -7.3645 | -55.51931 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 99f6f7af-b1fa-3e78-8ce3-b4103d07f676 | -7.36412 | -55.54229 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b37628e7-bf2e-3265-ae0d-3d324605541b | -7.36369 | -55.50584 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8d2d777f-a787-3285-b80a-6fc6d82a652c | -7.36329 | -55.56293 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a7f899a-e050-3b8c-8da3-5b02fca712c9 | -7.363 | -55.52691 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce31f8e1-84ac-3615-92d7-7ad6ed0f96fd | -7.36277 | -55.5494 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b06c7f9-e948-368c-8bb1-b2770a205ffe | -7.36246 | -55.51231 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 98649853-9e0a-3ecd-adbf-a0b1d392f939 | -7.36163 | -55.53388 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9e62ba94-6426-3c4e-8017-b90eb7aba9e9 | -7.36145 | -55.55635 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 378d33c0-0fdc-3335-97e0-5f64e5b5460e | -7.36114 | -55.51922 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 73cf6b5d-c539-3d8c-9ac7-0741ad0e3e58 | -7.36029 | -55.54067 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1a7e8b0-df3e-3dd0-932b-65f6d89201f3 | -7.36018 | -55.563 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4aaa88a-1800-3ed7-a599-53e709c7e089 | -7.35967 | -55.52696 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| a3d4da44-ab5b-34b6-b0d7-adf494f45831 | -7.3589 | -55.54771 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5c78f6a-1530-3744-8c9a-4c1ee4150e47 | -7.3575 | -55.55485 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a123eac1-e17d-39ab-baa7-23a0dc6b0714 | -7.35704 | -55.54075 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43b64a50-b3f3-33d5-80a3-84b72eea123a | -7.35619 | -55.56147 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496746f0-8c4b-3a42-852f-cac0d3c0fb51 | -7.35572 | -55.5477 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6bbf1a0-2981-3d95-93ca-ae317b7b5283 | -7.35434 | -55.55495 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b613658-c701-3fa7-af18-080f381f97f4 | -7.34865 | -55.54611 | 2024-09-26 04:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e68cda1-1436-321f-a480-1d5b774bc728 | -8.69536 | -44.80022 | 2024-09-26 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b605a28e-a7d1-311f-bb42-b9a7fb2e6270 | -8.68566 | -44.74854 | 2024-09-26 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0356ca57-1bfb-3f27-b3b5-04d43bfe4b9e | -8.6821 | -44.74797 | 2024-09-26 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dac460a7-3fca-3a7e-ba54-f70948a0d564 | -10.18669 | -36.57822 | 2024-09-26 04:06:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e6980e2d-9dae-3643-9f9b-d9a4344b3416 | -10.18615 | -36.58207 | 2024-09-26 04:06:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74d62b37-ec2c-3878-9c09-8ae15b1ce791 | -8.67274 | -38.14747 | 2024-09-26 04:06:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c666c2f5-d939-3e92-b41f-e4acf19a14f1 | -8.67339 | -38.14305 | 2024-09-26 04:06:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e520e982-3d77-3763-a5a0-b0ee6bde8e25 | -11.23748 | -39.41125 | 2024-09-26 04:06:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ac949dc-59fa-3726-87ca-e8e9e1b44b53 | -11.23594 | -39.4096 | 2024-09-26 04:06:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f839ef61-c71a-3e3b-b779-f01c4fcad306 | -13.05037 | -39.96685 | 2024-09-26 04:06:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84ad7d3c-f673-3110-b491-59c2ccea6583 | -7.80285 | -40.31949 | 2024-09-26 04:06:00 | NOAA-20 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 28916133-5f6f-3fc6-ba9f-3b1099d7d7fb | -7.63341 | -40.51334 | 2024-09-26 04:06:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2d854eb6-5906-3575-86b0-3cb08df5750e | -7.52262 | -39.95531 | 2024-09-26 04:06:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c285243f-3e79-3cad-95a8-0ea3fec7e2e6 | -7.26436 | -39.30571 | 2024-09-26 04:06:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5e93632-23a7-3219-8734-6e1a106f1250 | -7.25007 | -39.85875 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b995c166-3d40-3640-bed7-eefbdc1a40b0 | -7.24667 | -39.85823 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2e7fff2a-026f-38d4-9258-601b6c912e61 | -7.24309 | -39.35302 | 2024-09-26 04:06:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 73155a83-8a69-354f-a139-f54cb7d7bc31 | -7.23386 | -39.28167 | 2024-09-26 04:06:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 43d5e9f2-b515-3205-95c1-ec2dbb6daa00 | -6.95237 | -39.42587 | 2024-09-26 04:06:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ce2c4fb2-1cca-30e2-aa72-a1d7ccea355b | -6.94951 | -39.42159 | 2024-09-26 04:06:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d782c6d4-c0c9-3829-a40c-bc36044a10d9 | -6.94837 | -39.42905 | 2024-09-26 04:06:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 297ccb55-216d-3596-baea-4b8df1ad11eb | -6.9082 | -39.87284 | 2024-09-26 04:06:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c3dc5aa-be78-3ee2-9402-c8a5cf4818bd | -9.24985 | -40.19869 | 2024-09-26 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d54541e-dd35-3131-81fe-8b9a62e5c9eb | -9.36599 | -40.35887 | 2024-09-26 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README67.md)
