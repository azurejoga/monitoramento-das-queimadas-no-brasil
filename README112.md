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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f03768b-f261-36ed-97d4-072507b03542 | -12.41376 | -54.35837 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee61024a-2af8-3533-b818-63e8fcd238f8 | -15.35145 | -46.27491 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffb4db5f-1ceb-3b1b-9bca-dae633ab4fcc | -12.4976 | -50.2578 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c15f1f6-d38f-3654-b18b-e53f0d136117 | -15.03813 | -48.06841 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dac0392b-7343-3e67-8c85-5e3fe2065c01 | -15.34764 | -46.26916 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c20b81c-47d1-39a2-9210-f9199a97f502 | -14.62207 | -48.30663 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31d9b2da-2e37-34b3-9cc9-8074378f1c74 | -11.91272 | -46.7459 | 2025-10-02 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 91bc8dec-eb63-3355-a0c3-937fb25dfa06 | -15.35191 | -46.27591 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae7e99d9-ad2c-3482-82a2-62aac8122464 | -13.96162 | -48.12357 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a97cfd9c-a6d6-3fe4-854e-e57c1fb5d00f | -13.57409 | -48.19767 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9011c1ca-fb4a-3970-9620-3741e4fca1fc | -11.35885 | -44.9447 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1601d78-e0b2-3818-b458-0016cdd69fc0 | -11.61658 | -52.24807 | 2025-10-02 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2df9862d-920d-3176-9c41-526b5ae58c75 | -13.80877 | -47.53373 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1c27921c-b751-3b9f-9b5f-c9dd9c46e5cc | -14.46392 | -48.39398 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d5e9df0-2ddb-3722-8983-c159c06fe84b | -13.36308 | -46.34189 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcbf5c0e-a810-3081-ae6c-d8b35c5da7d4 | -11.09108 | -47.71283 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fcb63a0-efa4-3e76-a62a-236e64e49172 | -13.23012 | -48.50847 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46189d02-76ec-3f0a-99b3-5dff9aa105b0 | -14.59606 | -46.71519 | 2025-10-02 04:51:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbf00445-2fad-39c9-ba93-b12715010583 | -10.22842 | -50.31358 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d96a255-cd47-36c1-ba0e-7376d1261017 | -9.93421 | -43.75922 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 36334aa6-a3cb-36c4-a725-42f6fd99ede8 | -15.25535 | -47.91145 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0899e168-aaa9-3626-97b4-9f01cf7131bd | -11.80237 | -44.98147 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b729ca66-4f23-3ff7-8183-cccd76b328b5 | -10.223 | -50.3255 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ce99a2d5-4627-3f04-8da0-919bb9d40b55 | -14.59541 | -46.72046 | 2025-10-02 04:51:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46110a79-2b54-35f8-96f3-f067ddc5fd27 | -15.69982 | -46.2542 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3aaadcb6-37cd-37e8-ad28-3a7d4c48d864 | -11.09428 | -47.71614 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 238016f4-4578-3a55-83d0-ab2688e346c6 | -12.26472 | -47.81327 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fda3bf92-a335-360d-b05a-a0dbcb49d499 | -12.26601 | -47.81529 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 17feef8e-a79e-3233-a7f0-99a19208d6b3 | -15.15967 | -52.79547 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf6880ab-2238-3405-bb42-da193515f59a | -14.30999 | -45.89056 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 084809d1-9da4-3411-888d-8927819f1fff | -11.27047 | -47.81626 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7308bf0d-d426-398c-a2e0-f1910b7ed1d1 | -13.31403 | -47.861 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bef3940-e55e-3f68-a13f-faaf5b0a9b10 | -10.22659 | -50.32604 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1de4df6-d75f-3730-8c17-6aff6fdffbf4 | -14.30427 | -45.89552 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97068239-6683-3941-aefe-7291adf6f39d | -12.94496 | -48.42955 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d043f715-b248-311b-8e21-c8d762817d0f | -13.75369 | -47.95508 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40456767-961e-3de5-ab5d-f4b0b7b67e81 | -11.98016 | -47.01511 | 2025-10-02 04:51:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09d2a8b3-c170-33e8-af47-20ea4613199a | -15.54743 | -48.1783 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8aa5682d-132f-329b-8ce9-611402e6ca1c | -15.94743 | -48.37033 | 2025-10-02 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30dfcfab-f2b2-3ae3-accc-7c3302c756af | -13.8121 | -47.54337 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7f22fa4d-3b21-3477-b02b-c20200de4ff4 | -14.03905 | -48.00298 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c7b18fd-4793-3463-8004-9815c8852d58 | -13.46972 | -47.25879 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ab5f3b4-361b-31a8-a892-eecf7257d18e | -9.93647 | -43.74149 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e0565b60-7158-35eb-8dd0-ee986d68151f | -14.8175 | -51.4067 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 863735e7-95bb-3780-9c97-184ef06f56ce | -11.8228 | -45.02779 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1329b21d-5e8a-3396-a850-8a6814ac33c6 | -14.89601 | -48.3246 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a226d4fd-a798-39a4-9664-8037b5adc794 | -14.21543 | -46.11394 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99089933-ac60-3c18-96df-9b59266690ac | -14.71153 | -48.20774 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 807a36fc-6288-3e17-848f-c795b6cf6385 | -13.7591 | -51.21714 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2c81e7e-5504-3ce1-b27f-d92b5a2f9b21 | -11.52038 | -54.4625 | 2025-10-02 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 622d4ef9-0d6e-3980-86ee-8b1dafb73ac0 | -9.94509 | -43.67363 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4987fdb7-0641-302f-ba91-918e0f0ee423 | -15.23894 | -46.98292 | 2025-10-02 04:51:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca69fb0-4638-341e-a59f-fa78be104954 | -14.39731 | -46.08798 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 623f4380-dfa9-31ed-9525-5ddcffb68c13 | -12.93342 | -45.1075 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50857763-2b38-3f5c-9cdd-9988106300fa | -15.27433 | -47.90472 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c189b40-b7e9-368f-b610-332fcdb56635 | -14.32567 | -45.96822 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20c34261-1456-3341-8236-f2fc4adbf202 | -12.79891 | -46.85644 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1201f592-28cd-34e3-8fff-f61d07c2e8b7 | -13.18763 | -47.83772 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48970163-cef4-3f1e-a1de-445b41674458 | -16.03685 | -50.85369 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a44fd0d0-8d91-3b2c-a8ee-bfcc65973a28 | -14.90593 | -47.224 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60caebf9-db71-3339-82f9-7bb3ef7dc692 | -15.23271 | -50.11876 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc1c25e7-b806-3a84-825a-49ab049d263b | -14.60064 | -48.23556 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14b25815-6682-3aa1-b755-477ee07e4fc9 | -13.07574 | -47.09416 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d26a03a-2c54-38f6-aa6f-a8893c1ef3ae | -11.08856 | -47.82193 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e9e52a2-6a65-39d5-9ab7-ed987d109f7e | -14.58872 | -48.32809 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f2eeedd-9b21-35e5-a346-15ee1dfa669a | -11.1863 | -47.61493 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8776ed0c-36c3-3c74-98f1-5d0c9aefd52b | -11.19985 | -47.19129 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f5feb62-b57b-3edc-9641-62a1ce941049 | -13.94355 | -48.1277 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e53b9624-bd14-39ba-a1ee-ae4c5e65adbc | -14.9698 | -49.96318 | 2025-10-02 04:51:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 036bb416-ceda-326e-b3d9-9dfe9b4db5ba | -11.61678 | -45.04966 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6aade55-d6e0-378d-8573-f2336c158922 | -13.23063 | -48.5048 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d02dec2a-4eed-3279-ab91-189f3997a0ae | -10.20217 | -50.26708 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bcf9268a-3fb7-36ab-8f9f-9bedf1348b74 | -9.95395 | -48.7798 | 2025-10-02 04:51:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3beb425-09da-3164-ab2e-90625371177d | -11.82324 | -47.68119 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c677a83-7c00-3c5c-baf6-276189c2f0dc | -13.74718 | -48.00303 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ae7fabd-751b-3566-8f6c-0b420371e86e | -13.17526 | -47.83106 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbf437c8-14af-394b-bb8a-1c60b97e4753 | -12.88698 | -46.93232 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ac10d7f-de63-3fff-9ae7-8c1772a54431 | -11.80917 | -47.59092 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0aadc4f3-6842-33cb-a384-fe618025f051 | -14.21609 | -46.10875 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fffbc82-cba8-3cba-9db5-3790f1b069af | -11.28203 | -47.82609 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9ae5e4dd-0174-344d-9784-eb1d5adfde74 | -12.8703 | -47.02362 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24b3c9af-1251-3166-a424-f277b2ebafa3 | -10.22239 | -50.32965 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1753f99e-ce14-325f-b5da-645d5f90746f | -13.32008 | -47.81607 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00ae458d-5ca2-3cf3-aed7-8133fdd42a11 | -13.77773 | -48.05341 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e3083129-c85f-36f4-8278-2b6a96b6691b | -11.26208 | -47.81465 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 492e0d44-c50c-3984-941f-453cc4357590 | -9.84785 | -49.95652 | 2025-10-02 04:51:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9999296-8db1-3e1d-b47a-075e47e533df | -11.7972 | -44.98079 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03400c42-3a13-3b05-b883-3509d31fd1af | -14.21046 | -46.11344 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ab3b8e2-3d4e-3285-936b-176819ea9000 | -10.247 | -50.31214 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 11161c45-5e27-3ce2-8dc5-3c81ad3e0aec | -13.37644 | -47.291 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c206f553-00f2-3dd0-a695-74138449764c | -13.20884 | -48.50939 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2af90391-9c5b-3198-adfc-1c3234048a30 | -14.47189 | -48.43272 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81c2bbc0-8075-3d87-9e96-dba27945734a | -9.62588 | -46.63534 | 2025-10-02 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29cfea27-c860-3e68-9a7e-6b11b2b22864 | -12.70709 | -48.57606 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 921592ba-0902-3caa-b66e-0c308892c776 | -11.00334 | -46.59866 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fb125f5-e2f7-3f7c-8770-19dd3eb16bc4 | -14.40501 | -46.1071 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 358019e9-74a4-3cd4-8613-7ef1a8a54d9f | -10.96315 | -46.65523 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 90957026-cd97-3091-b8ec-b2002229c9e7 | -12.02899 | -47.90829 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b62d2cc-2875-3e72-8109-f45771683f1b | -9.94647 | -43.70674 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78377f65-1165-3b1e-9f56-eb26e56b8537 | -11.87079 | -45.02166 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README113.md)
