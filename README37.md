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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e24ef24-6b8d-31d4-872b-97eface0072d | -17.20008 | -57.38123 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| eae6a4ce-c7c1-3c9e-9d4e-8b30b9912a93 | -17.20861 | -57.36786 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| a32bf763-90a2-3bbd-9060-6d0f62cf3e77 | -17.21012 | -57.37985 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 7d1d67d9-00d8-3812-86ee-887c230da24e | -16.44287 | -57.43525 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 92a1be2a-221a-33f5-809d-80f362bb0dd6 | -16.44844 | -57.39867 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 55fb77cd-5b3a-3f6a-83da-3cc8acaa7473 | -16.45285 | -57.43391 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 69afd33c-1716-3957-ad44-60582b1ce9cb | -16.45947 | -57.32588 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| ce243ed1-3ac1-3d33-8eca-c0ef6f297839 | -16.46135 | -57.42082 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| f9c20714-e282-3bfe-9cd9-8df10b0278ce | -16.46283 | -57.43257 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 685d96ce-0e4d-38a0-b2fc-2f26ac26cac2 | -14.56759 | -44.86417 | 2024-10-02 01:26:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 0494654f-7b4f-385b-a128-703bd464674f | -9.5584 | -62.7997 | 2024-10-02 01:26:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 70683e2b-8c3a-3488-af6c-9e2e4017dd9e | -9.9367 | -64.9179 | 2024-10-02 01:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 5ac4e704-6847-3439-b014-097ae5acc14d | -9.9368 | -64.8991 | 2024-10-02 01:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 156.6 |
| a9b9967f-0b72-3dde-9051-dde2c25c6b89 | -9.9553 | -64.9172 | 2024-10-02 01:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 2b43e8b7-ab9c-3738-9141-3839666f4a2b | -9.9554 | -64.8984 | 2024-10-02 01:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 304d4f89-643b-32b0-8b77-a37e8cf17681 | -10.3711 | -64.090103 | 2024-10-02 01:26:07 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cbabd5e1-0757-380b-bebf-d503651bf1ce | -9.9581 | -62.9902 | 2024-10-02 01:26:10 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ea87bab-11d4-37dd-87a8-4b21d0fb76b5 | -9.3973 | -61.041 | 2024-10-02 01:26:12 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01932ac3-b482-3076-8512-dc7b647caa21 | -9.3875 | -61.043098 | 2024-10-02 01:26:12 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8ec9f3-d260-3d2e-8a84-6de3cefb666b | -9.3894 | -61.051899 | 2024-10-02 01:26:12 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c570c00a-cdc1-37b2-bf93-839e439ace4d | -11.6554 | -65.018 | 2024-10-02 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 90e92d17-0f4d-317d-97e7-f15481bb7b7e | -11.6555 | -64.9991 | 2024-10-02 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 62d29065-56c0-3899-83b0-335454ea22d2 | -11.6556 | -64.9802 | 2024-10-02 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 06b46a83-2d2e-3ef4-a454-218d3c27814c | -11.6743 | -64.9983 | 2024-10-02 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 63a6dc70-dbbe-34c6-8452-19e9b4272b7e | -9.7752 | -63.139198 | 2024-10-02 01:26:13 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7883cbb-a771-350f-b847-dec2604ccc7e | -12.4433 | -43.7242 | 2024-10-02 01:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1d32dfaf-33d7-3ac9-a5b9-d65a6efa6779 | -12.2946 | -47.6446 | 2024-10-02 01:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b9872bf8-5585-330e-b9e0-020c5a54561b | -9.979 | -64.7509 | 2024-10-02 01:26:15 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b619b73-635c-3582-af1a-6f19794d8331 | -9.9822 | -64.766296 | 2024-10-02 01:26:15 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9e854557-aaa9-3bdf-91f1-81eff8c79823 | -9.5506 | -62.8013 | 2024-10-02 01:26:16 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5aceb01-6a26-3770-88a4-870d193072e2 | -9.553 | -62.8125 | 2024-10-02 01:26:16 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9dec8af-ddd5-3a06-b990-420925e9e2af | -9.5385 | -62.792198 | 2024-10-02 01:26:16 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 25a0f965-c39c-397d-a8f4-ce141bb8a71b | -9.5409 | -62.803398 | 2024-10-02 01:26:16 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b89c49f-cb14-35ab-8ba5-26131da04731 | -9.5433 | -62.814602 | 2024-10-02 01:26:16 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce8297d-10d9-37b0-ae6d-a3ab517156e4 | -9.9461 | -64.886803 | 2024-10-02 01:26:16 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d201458-a6c9-3899-ae5a-90319d9d1de8 | -9.9494 | -64.902496 | 2024-10-02 01:26:16 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 71a7cae9-45a7-3aaf-8723-cadd8f1eecd6 | -9.9526 | -64.918198 | 2024-10-02 01:26:16 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa0325d7-68b9-3c18-bfb7-bc6c4a132c7d | -9.9363 | -64.888802 | 2024-10-02 01:26:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1512ef14-3525-3e42-9850-583fcae11b82 | -9.9396 | -64.904503 | 2024-10-02 01:26:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba7b22e2-110d-3e4e-bdf6-31c035914b92 | -9.9428 | -64.920197 | 2024-10-02 01:26:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8baf5850-5e5f-3127-a305-e53d1fa5eb6e | -9.9266 | -64.8908 | 2024-10-02 01:26:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc980ee2-bf45-3932-b46a-e7bb3186d963 | -9.9299 | -64.906502 | 2024-10-02 01:26:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba9a06b-cba4-34fd-ba3e-c33cffe29aee | -9.9331 | -64.922203 | 2024-10-02 01:26:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f20444bc-0760-32c9-b89d-7629e5d58c70 | -12.6295 | -63.1225 | 2024-10-02 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| f4d0eb39-ace8-3b62-9919-442cd7c82ecd | -12.6484 | -63.1214 | 2024-10-02 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| b0c9d271-5997-3631-a7e6-f338279d85f0 | -12.6486 | -63.1022 | 2024-10-02 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c78978ea-1ef9-3c2e-ab19-88777021d0b5 | -12.7054 | -63.0798 | 2024-10-02 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a8e7472d-5e53-3883-80e3-12df17c0939c | -12.9578 | -51.5156 | 2024-10-02 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 7f96fabd-60f6-3888-9ace-ef2e847dea6e | -12.8593 | -62.7826 | 2024-10-02 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| db4680ac-bcdd-3d8e-9932-01fd43f08157 | -12.8782 | -62.7815 | 2024-10-02 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d6ba57c0-765f-387c-8331-ffddaeaf7907 | -13.2173 | -48.624 | 2024-10-02 01:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 407e8b23-3fd3-3a2d-b307-4c88ebcd6011 | -13.2177 | -48.6019 | 2024-10-02 01:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fc9e925a-4094-3c38-864c-f7e12981d195 | -12.9167 | -62.7022 | 2024-10-02 01:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 77af10f7-090e-3aef-b0a4-5ef33677e350 | -13.0557 | -51.3759 | 2024-10-02 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 034eafac-9717-382a-a18d-6021517648d7 | -12.9357 | -62.701 | 2024-10-02 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 174.3 |
| fc929f4f-a796-3e0e-a61c-21cccc9a2c07 | -12.9358 | -62.6818 | 2024-10-02 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 2e095688-cb94-3c68-a21d-16518948ca15 | -13.0738 | -51.4376 | 2024-10-02 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 8e44ebab-3da9-316e-9bae-bf0bb5cb399c | -13.0742 | -51.4163 | 2024-10-02 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 2badf61b-c861-3478-aae4-57ae5776ba6f | -13.0748 | -51.3736 | 2024-10-02 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5ac4b621-b1b7-301b-865c-2ebe1679a6c2 | -12.9546 | -62.6999 | 2024-10-02 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 40fddf0f-219f-382a-918c-01ffb4ac8be1 | -12.9548 | -62.6806 | 2024-10-02 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 202.5 |
| daa5ad0b-4023-35c9-958c-37441e54763c | -13.093 | -51.4352 | 2024-10-02 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 59b5b4b0-d608-3f5a-8f48-767edf806f58 | -13.0933 | -51.4139 | 2024-10-02 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 174.2 |
| bf0340e4-99b8-34e6-a49e-f6d4e9be1c14 | -12.9738 | -62.6795 | 2024-10-02 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8757e207-50b9-3d34-989c-423c119bf511 | -13.2373 | -48.577 | 2024-10-02 01:26:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 11ae21e4-4b92-3830-92d7-b9ffdd06bc3d | -9.5615 | -64.256897 | 2024-10-02 01:26:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fabcbce8-10af-34ef-866d-3e74edf8bbc9 | -13.5965 | -51.1367 | 2024-10-02 01:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 0cb74d5a-3c97-3f66-ab1f-3b4861c06c92 | -14.5699 | -44.8351 | 2024-10-02 01:26:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 04cdedd7-1819-38b2-874f-d24d475b5d46 | -14.5704 | -44.8116 | 2024-10-02 01:26:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| b33f2366-e915-3c08-ac37-2f345c5ee6bf | -6.5744 | -52.9249 | 2024-10-02 01:26:28 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122ae09c-58ef-347d-b4b9-1e63756e36e3 | -9.2981 | -65.336502 | 2024-10-02 01:26:29 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71cacc62-3e3d-3d5f-8716-ec9131b6b95a | -15.095 | -49.49 | 2024-10-02 01:26:31 | GOES-16 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 8c073833-d078-3dc1-a894-69edba124b7b | -15.1145 | -49.4869 | 2024-10-02 01:26:31 | GOES-16 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e245628d-96a7-33cb-b1d9-b86166eb221c | -15.139 | -55.8285 | 2024-10-02 01:26:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 41312f6a-b8ef-3e74-9083-a45443c90c38 | -8.5602 | -62.472198 | 2024-10-02 01:26:31 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32a44bad-b5f5-38d1-9558-bf69c29cc956 | -8.5624 | -62.482498 | 2024-10-02 01:26:31 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1c791c-336a-3dd9-ad3c-5590cbfd6fb9 | -8.951 | -64.354301 | 2024-10-02 01:26:31 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cbf75a8a-6ec3-3ac5-b23c-fcc2f3222728 | -9.5366 | -67.6996 | 2024-10-02 01:26:33 | METOP-C | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cae3e4c3-cc7c-3ee4-80cc-fab413f8f7dc | -8.4685 | -62.710999 | 2024-10-02 01:26:33 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7e6bd3-8f25-3cb2-9fef-75bba81637bd | -8.4708 | -62.7216 | 2024-10-02 01:26:33 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1754a28c-4da3-353c-8bec-6b16fc1e0a8d | -8.4587 | -62.7131 | 2024-10-02 01:26:33 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cbb35d82-a8f6-3069-a73c-0c622900c8fe | -8.461 | -62.723701 | 2024-10-02 01:26:33 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcf42966-d9bf-3981-a707-7c5a31b1dd3a | -16.4533 | -57.4392 | 2024-10-02 01:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 0403865d-3c9a-3b3f-89c1-a4ad6a81d4e4 | -16.4536 | -57.4188 | 2024-10-02 01:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 0fe3bf21-2e6d-3e79-a87a-367ac9957717 | -16.689 | -57.3309 | 2024-10-02 01:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 0e494c2b-8e6f-3fcc-86f6-c2ee21030fba | -16.6868 | -57.4741 | 2024-10-02 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 2fb940d1-0501-3c4e-95d8-7b1f393bf431 | -16.6884 | -57.3718 | 2024-10-02 01:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.7 |
| 180986b5-b3cd-34ce-8e4f-03874fdebbbc | -16.6887 | -57.3513 | 2024-10-02 01:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| af46528b-48f3-31c2-a3b9-ed794601f8f5 | -16.7082 | -57.3491 | 2024-10-02 01:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 2421ce35-df61-3a20-b511-f51215839600 | -16.7086 | -57.3286 | 2024-10-02 01:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| cd7218a5-8afa-3562-bbac-b21fcc38b861 | -16.7265 | -57.4287 | 2024-10-02 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| a32b6091-1b83-341f-a810-86a6e826a9b6 | -16.7269 | -57.4083 | 2024-10-02 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 3632fc9c-604b-3063-9b38-f5ca180b71a1 | -16.7452 | -57.4878 | 2024-10-02 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| f5012b1c-c86d-308a-81c4-d67e6827e45e | -16.7461 | -57.4265 | 2024-10-02 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 2e572090-ed06-32be-9937-04cd153a3227 | -17.2717 | -40.2853 | 2024-10-02 01:26:41 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 132.8 |
| 379cbba9-47ec-33e2-8775-e23c4625aa82 | -17.2918 | -40.28 | 2024-10-02 01:26:41 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| 9ea93838-7363-36dd-8f87-d77f744c3ae5 | -16.8292 | -55.9152 | 2024-10-02 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.9 |
| 2445552c-efa2-3f99-9009-5e69af0c0388 | -16.8295 | -55.8945 | 2024-10-02 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 139.1 |
| 84e845cc-9393-3a16-a652-0f55b7d1c0e1 | -16.8299 | -55.8737 | 2024-10-02 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| d2eab934-6947-3a4f-bcb8-19c76624377e | -16.8488 | -55.9128 | 2024-10-02 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |


[Clique aqui para ver as próximas entradas](README38.md)
