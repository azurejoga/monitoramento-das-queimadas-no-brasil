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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02aafcf9-172d-381f-b69d-242adf55e2f4 | -3.98857 | -49.71168 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 158c394a-ded8-3110-953d-34267422f606 | -3.07211 | -53.80772 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c14255d-dce7-3205-9d1a-b14069f42293 | -1.68768 | -55.01671 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5536f8ba-382a-37ab-beb7-66cb5af6e3dd | -1.0862 | -53.63949 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d1ee0d-8458-39f2-95f1-e8deba594d1b | -2.73841 | -47.9851 | 2024-12-02 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d8e7c0-e8d7-3045-a932-a52a251d4da3 | -2.95408 | -49.58611 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09e4c5fc-b510-304e-98a7-0ce548e06cb5 | -2.41458 | -53.6645 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3231350-3b78-3e7f-a2f3-ad0ea221db1c | -3.71094 | -52.19039 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96e244c1-9c4f-3850-bd51-69ffd7bb2fc0 | -3.02622 | -51.01296 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 417a201a-8d93-3830-881b-4bb139e1c558 | -2.20051 | -48.34193 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c97dd985-87eb-3800-b935-a8e40590470d | -4.08905 | -51.05646 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6fb69f8-9dde-383d-98b5-5c720779b8b8 | -2.47825 | -50.36847 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9dfe7e3-e86d-30a8-9b01-a55604d218ce | -4.02063 | -51.01784 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 099c4577-9243-31cd-b053-3e4719567120 | -2.92046 | -48.01307 | 2024-12-02 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 381d67d5-d798-3e80-be28-f14e719bc107 | -1.09101 | -53.60919 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89907707-98be-369e-b78d-f4b35c153c7e | -1.59147 | -51.25944 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f07dc889-98dc-37c7-b55d-d9d50c9c0351 | -3.32171 | -54.17907 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0f130f8-7c52-3a67-8904-504db3161b62 | -2.81878 | -54.14985 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d25a478d-06d6-371f-b7e9-b1d31f818919 | -1.66547 | -53.21661 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172d807c-061c-3d99-ad88-259ed2379282 | -2.59172 | -45.65453 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54110003-31b8-3525-9bf6-7e5781e16aa7 | -2.79747 | -54.03602 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db5c77ad-a8dc-371d-9fbf-a5d711665d64 | -1.70265 | -52.47192 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e65ba795-5a8f-36e2-a400-07441c313e67 | 1.21619 | -56.00897 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42e28f4a-436e-3c6d-9388-28c267b761c6 | -2.87785 | -54.01316 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df87c02c-6ad8-3397-b4ec-1571c48e2c30 | -1.72781 | -52.63807 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8e50f85-42bc-3390-ba83-840708c4af82 | -2.57329 | -54.2157 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a74cae02-a3c1-32e1-83cc-2f4c43fdd29f | -2.20479 | -48.33833 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3afaf99d-0eaa-3e44-a76e-22985dd50828 | -1.93036 | -53.44632 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ecc4b85-d3fe-36b5-b31f-e449cba4928f | -4.18576 | -50.67701 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb6d3587-1663-3c7d-b196-479e8d53c7da | -2.38561 | -53.71378 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b2f2996-e11e-3b60-a24f-6951f6dedad1 | -4.01227 | -46.99742 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bc7c99b-a9e4-3aec-b4ea-de78a7c9c9de | -3.09271 | -54.29804 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78fad6cc-568b-31aa-9e5c-644ec67d500f | -2.77766 | -54.04859 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9aa3c81-6077-366d-8136-957822f16be2 | -2.92401 | -54.12645 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 732492c4-cf0d-3fd5-b3c5-143439db7057 | -3.55115 | -51.45654 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16317231-541f-337e-a6db-11d1a2d69c06 | -1.95714 | -46.44638 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06ad8017-8315-3981-80d6-d5157ef4a278 | -2.86744 | -54.01154 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cec41b2f-9996-3512-a6e1-02bacd2e3646 | -2.45303 | -48.16455 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4af94117-cc99-3c57-bd59-a717cd8ec9e7 | -1.99319 | -53.29367 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7497712c-3260-376e-b5d2-e6fd4bf6a573 | -2.78017 | -49.21652 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b637aa0-0cc1-3099-bae6-7dc35d113585 | -4.05609 | -46.81953 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 26d82501-7486-362d-a1db-e00a1b827ac6 | -1.99227 | -51.1742 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df52ac37-4be6-3869-9d67-9070ce2c05eb | -2.26205 | -53.74106 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cef92c0-938e-392f-b396-5287f372dd92 | -4.91888 | -41.34233 | 2024-12-02 04:48:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c125c195-0166-3c0d-a2d6-b9cf1aace0ee | -1.57178 | -52.26931 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77b2b12b-9705-3447-a2e0-760263e83e87 | -2.94624 | -52.92229 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 393c6310-6b22-3d5a-b4c1-fedc4462f7d9 | -3.23353 | -53.63048 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a75660f-9e4d-3330-b821-83d369e8b75b | -2.43288 | -54.03251 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0981a26-7af1-33fb-a1c5-63954eee68c2 | -2.65891 | -54.09007 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1114dbb9-73a2-3766-ad0d-2598b8da9811 | -2.74347 | -51.75299 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed83f40-3ed4-3db1-9657-72c591cd3b82 | -3.94629 | -49.98614 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dad29183-cf47-372b-9a07-c6e62c35614b | -1.27455 | -54.55132 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f80f000-1388-30b0-be8d-1c6750baa82c | -2.37042 | -53.92086 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39202e2b-7aa3-3edc-8987-36268c2bf47f | -2.79791 | -54.05571 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0b73c5e-ce81-374d-a599-07a95434d507 | 1.12928 | -55.98591 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37a93b33-b7f9-3cce-8e0f-f734cdaeb423 | -1.62203 | -52.38112 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ca6b9af-b413-30f3-aac2-02dbb7340d6a | -3.51283 | -51.54942 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62a83068-8841-3a20-ae9f-b5ba8d62b073 | -3.37752 | -49.85948 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 024d738f-6ad1-3266-b5ff-d1e0cd45218c | -2.93627 | -54.32669 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af598862-15e7-3bca-af0c-5ee3ec7817a3 | -4.27286 | -50.68331 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50c8d0da-cddc-3736-9ce8-ff7c32b9db3c | -1.23741 | -51.60836 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 091aaedc-60a1-326e-b0bb-95b70b0e05ff | -2.80199 | -54.05243 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f72fa427-b653-30c9-9858-c0eb1683a050 | -2.24294 | -50.78823 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f9cf736-893e-3fc1-aee8-188ab371703d | -0.96231 | -51.71648 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5631e0cb-1474-3acb-a099-65ea6165ff6e | -1.07629 | -53.39518 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78acb7e8-fa5d-3488-83ea-c8a6b802754b | -3.81418 | -51.8788 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59f65de7-bc89-3122-bec5-f076dcbe4617 | -3.553 | -51.53098 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1537ae89-2bb8-3711-a8a1-af2c343e7152 | -1.48423 | -52.09198 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fa0dec7-b4c0-3c7f-9b83-88aad087b743 | -3.46147 | -53.4947 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 104430ea-7f93-3707-a5d7-f7958188a74c | -2.01495 | -51.20238 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd24ff9f-e0df-35ec-941a-90594ad76e58 | -2.77419 | -54.04804 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65cbeb4b-7053-3d73-85a2-216395b8c4c7 | -3.07859 | -53.76659 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 495e42cb-a1fb-3aa6-9a19-fdb2540b30f3 | -3.17744 | -54.33496 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ccdff619-a6b9-3d5c-b98e-05dfd2249812 | -1.99002 | -46.45125 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 542ad86b-3c8c-35af-96cf-a0056497d618 | -1.59424 | -51.26338 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f14bdfed-3059-3fa3-bd8e-169b925b6e49 | -1.32475 | -51.74499 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bb50668-f7e8-38ea-9e0b-b6aa81ce3ee4 | -1.61792 | -53.89303 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b0667b4-b64f-3783-bc42-65b7e090d9c1 | -2.79814 | -48.68361 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d830316-df53-3914-9543-02bca9086abd | -1.37549 | -52.56553 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d96bf55-a6ae-396c-8eb3-62a4a24fbedb | -2.44537 | -53.99902 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3f61fa7-45a8-3c53-bdc3-904189b40157 | -3.26008 | -50.05268 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a47f8ce7-a4bb-34dd-8be4-73e10b272611 | -1.27822 | -51.65322 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20cf9231-aeb4-3b07-9d64-12b28793102b | -2.43546 | -48.63977 | 2024-12-02 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9160bc4-f778-3d0e-a67d-9a1c181a25d8 | -3.07099 | -50.98785 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22d485df-d22f-3897-a940-6748550c0b0b | -2.81706 | -53.95716 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 61fcdf6d-bdf0-3937-9938-3915fc6448b4 | -1.38326 | -55.18422 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b29f6f8-8203-3ca2-accc-5aff616b329c | -2.72457 | -54.13484 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7db2a85-6cf8-3b29-a6c0-f694368f5225 | -3.88417 | -49.93487 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14c3ca8f-731e-384a-a00c-6091d325afdd | -1.46777 | -54.49366 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47788a39-e246-37ca-821b-ff7922dae5ec | 0.94457 | -50.74996 | 2024-12-02 04:48:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc025e96-a999-3ba1-8418-8d00a8cfaa0e | -3.09024 | -53.71493 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 996b8b27-7289-30df-9e7a-7e69fd6e68e5 | -1.79318 | -52.76097 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ddc0cdc-2381-3aa5-8132-c46e0048cbc8 | -2.22703 | -53.63203 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348e63db-3ca6-326e-b6f8-45d8ba07b372 | -2.56855 | -53.40107 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 62f08ec6-3a6d-3700-ab36-d4294fd4b2e8 | -4.25417 | -50.8479 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da605bb0-7ef2-3271-81be-06abdccff723 | -3.15916 | -51.11922 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fae7d998-ac16-302f-8595-e630b7c39555 | -2.89909 | -51.36916 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf74d32d-ba33-3998-8e95-5fa7b1906d1f | -2.19193 | -50.56947 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6657f681-9201-39a5-857c-7050fd06af86 | -2.97663 | -46.94598 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3177a457-b46f-31ed-b24c-c90a8e1bda75 | -3.7418 | -51.30242 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README58.md)
