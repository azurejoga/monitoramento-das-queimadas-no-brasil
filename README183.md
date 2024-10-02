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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d7b8d80-0b3a-3e92-8d2f-2b0a2f116196 | -16.70106 | -57.33866 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e83dda79-117f-3e02-92ad-ab814a34742e | -11.66311 | -65.00768 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ebe42de-5994-3b14-a85b-f56d2eca6d46 | -11.66347 | -65.19865 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a69b114-7e33-3c7b-917b-16775065cc9d | -11.66367 | -65.00417 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7581b98-7f3e-358f-b4e0-19ab2c0d0777 | -11.66422 | -65.00066 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21116dde-c548-3dbd-97e9-4e1eb369e09c | -16.70004 | -57.18685 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b45b486d-f137-3141-83b4-0aab1b599b25 | -16.69967 | -57.18999 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0858041f-58f8-3546-a49d-681a2c6f2239 | -16.69953 | -57.21265 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 76d56022-d4d7-32c7-b197-e168ca9accaa | -16.69775 | -57.33764 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 88cb4cbf-fb01-340b-ac61-653c4b95463f | -16.69738 | -57.34071 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e1613b7c-d64b-348a-84cb-6c77ff019f37 | -16.6971 | -57.21191 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 47ba9f77-b461-3c5a-9ee4-b334209888e5 | -16.69598 | -57.33802 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 10781a23-a2db-3d9b-8846-556282ec5df2 | -16.69564 | -57.17993 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9967aef0-9d19-35a6-90c0-2532a44606fc | -16.69563 | -57.3411 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 57e2550a-be38-32b2-b141-10842a27dc80 | -16.69527 | -57.18307 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d7060078-364f-3314-be97-1e8332fdc0de | -16.69491 | -57.18622 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c3476b21-6a35-3d3f-8669-eb8cef2b2210 | -16.69454 | -57.18937 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 460540b0-32a6-3225-a8c4-32e1d3be8112 | -16.69417 | -57.1925 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b1c60253-2a17-3395-b7e9-2e6bf67fe9c0 | -16.69379 | -57.23999 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7ab52e33-4910-3979-87ea-185e289458a3 | -16.69343 | -57.24311 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3e2ea622-a2d7-36e4-b62c-d014c985b09f | -16.69267 | -57.33701 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dd85c7f2-f6e5-3e73-8df0-d7d3d5ddc4fe | -16.6923 | -57.34008 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fff20c24-ac94-38de-ab13-afbc1912c6c9 | -16.69194 | -57.34315 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cb0d870b-0a54-350e-8c2b-d8ac3625fe23 | -16.69158 | -57.34621 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 16e5808c-54d6-3066-9ac0-39af398275af | -16.69121 | -57.34927 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1b96d12e-850a-32dc-916d-edd4de2ffad1 | -16.69085 | -57.35234 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e2cdcbb4-2d72-35de-bb63-7f5f67031cd8 | -16.69055 | -57.34046 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 61d044af-47ed-3f79-a6de-b2cc5ddd1093 | -16.69051 | -57.38698 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 90debfee-1c66-315a-9e39-aa4c45028837 | -16.69051 | -57.17931 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9878a7ae-bc78-3d4e-81ee-283f769f8ab0 | -16.69021 | -57.34353 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d9596d6f-d3fe-32e7-9a0e-577c0268e3bb | -16.69014 | -57.18245 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 0cc7588d-b79b-3c38-94e0-1d2e9f0a393a | -16.68987 | -57.3466 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 83078253-7b3f-35ba-907d-419cb2100f5d | -16.68978 | -57.18559 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 8e432333-aead-323a-9a2f-716cca2e861e | -16.68953 | -57.34967 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 24e6cc8a-9e3a-3a9c-89d9-43ad48a99d6a | -16.68941 | -57.18873 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 662f79c2-c506-3ee5-b505-03a16ed1036d | -16.68919 | -57.35275 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 33e08f13-8f97-3e41-8a87-39b67d285b4b | -16.68885 | -57.35581 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 26a25933-b27d-32ed-93f4-53b11f39c810 | -16.68851 | -57.35886 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 155fd95b-162f-328b-92d3-5fa077e69487 | -16.68832 | -57.24248 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c4be32b3-25fa-3758-acb5-20bcf2750b54 | -16.68831 | -57.3737 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4307043a-d474-31cf-8368-a36188690ae9 | -16.68794 | -57.37675 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cdcdbfca-5920-3251-a861-0c40d1c01d4e | -16.68613 | -57.34864 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 947928a6-12fb-36f2-8815-0b927d731511 | -16.68577 | -57.35171 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f7230622-3a77-3f86-87bd-2431317eeb7a | -16.68545 | -57.38635 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83bff3a2-ecd1-3a80-9c28-c93fe7e154e7 | -16.68541 | -57.35478 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1640f3cc-0a58-3b22-8076-60a3b6d4bfa9 | -16.68505 | -57.35783 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c541d720-eefd-3f6f-9bbc-480afbbf9d0a | -16.68469 | -57.36088 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 06bdcf5a-6ac6-3ed6-8f34-4fe84b255c69 | -16.68464 | -57.18496 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 95890104-b083-34ce-ba87-089621b928d8 | -16.68432 | -57.36393 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 20462879-be75-35ae-8330-fcd6e32cf0bb | -16.68428 | -57.1881 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| abe93af4-8462-344d-b44a-83648735b8b7 | -16.68396 | -57.36699 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1924f4b5-824e-33d7-8a2d-2f9c43abc560 | -16.68391 | -57.19124 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3612f01b-6ff8-3729-8cb3-e858bf758a58 | -16.6836 | -57.37003 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c3e103e7-ac0d-3bba-ad7c-488e147aa405 | -16.68355 | -57.19437 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dd20ebac-e088-3d19-a953-f2d38a49e495 | -16.68343 | -57.35822 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| aacfa673-ab96-3c20-bf07-6db2c0b11bcc | -16.68318 | -57.19751 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bf7d381a-24f2-304d-9f66-c75e27fc6121 | -16.68309 | -57.36128 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a461a92e-db63-359d-aeda-156e498a368d | -16.68275 | -57.36434 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 3fb1a258-86a1-32d8-ba5d-2cc287be3446 | -16.68242 | -57.3674 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 01341c36-fcaa-388d-8b5a-44511a082192 | -16.68208 | -57.37045 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| cf9b2808-d829-35e0-85de-42484a2578e7 | -16.67805 | -57.19688 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c67a356e-1336-309b-b167-e649662ba330 | -16.66853 | -57.18934 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3896c9a8-ccd5-31a1-a344-bc30167acd36 | -16.66816 | -57.19248 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 154da2ee-0722-3c73-a29f-3f70bcc34d53 | -16.66195 | -57.20126 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 26b1f5f7-de2e-35fe-bf8c-f9da6a50fb7c | -16.66159 | -57.20439 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 372546c8-9845-38ce-9dcd-707cd3e373bd | -16.65683 | -57.20061 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d9e144ca-0b37-38f4-8755-6935210ebb7b | -16.65611 | -57.20687 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8d9bbf31-7a1d-3a05-b22b-5d8109488a69 | -16.65575 | -57.21 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1587c36e-769e-3601-97ca-062211066ac4 | -16.65497 | -57.351 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 756edf61-cd72-3f06-aa2e-2e18aa4d560f | -16.65461 | -57.35405 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| fe1cf924-c235-38fd-976d-f8ea20b7b837 | -16.65099 | -57.20623 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| daf843f3-2fe3-35a4-bcfe-3170909845f0 | -16.65063 | -57.20936 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d89d4a2f-3019-39c1-b9c8-4f54b888d223 | -16.65027 | -57.21248 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 32d27847-d61a-316f-b4bf-80f58827680f | -16.6499 | -57.35036 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a9fc97b4-0b55-322d-b48e-7bb2a41d3dea | -16.82919 | -57.46739 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ace728c9-2aad-3d7b-8763-aad4488db3bb | -16.82884 | -57.47042 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 51842af3-bfaa-342c-ba08-ea11c8607f8e | -16.8238 | -57.46978 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6020251b-5626-3820-bfca-d99e5df3bbfb | -16.82345 | -57.4728 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9e825163-779e-3680-a44b-c64b76f72bc0 | -16.82311 | -57.47581 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b55fe62c-bb8e-33e7-bd0d-e083163677e9 | -16.81841 | -57.47216 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e6fcee85-caf8-3f2b-8d4d-8bca3255d2ea | -16.81807 | -57.47517 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6069ce4b-cf4e-3618-8312-065775d758fb | -16.81772 | -57.4782 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 494a331f-5df9-3d5f-8f80-aa3deec40f5e | -16.81738 | -57.48121 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0d0bb425-8923-3ed8-b0cc-ba03b50b3bb3 | -16.81332 | -57.56129 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 287d595d-2d39-399f-8537-e55151650696 | -16.8026 | -57.4763 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2409681b-a030-3d7c-abca-0e6e9cc30e52 | -16.79756 | -57.47566 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7fa1e254-a917-3dc4-bc57-a43d926dcb70 | -16.79722 | -57.47868 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 236ebfa7-c0a3-3e15-9e38-978336f73dc5 | -16.7864 | -57.488 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5fa52812-7007-335c-a21f-a97cd47a80e0 | -16.78612 | -57.48647 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d1115775-d168-3fb1-a06b-054654e53e58 | -16.78605 | -57.491 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4e2e7743-67ab-30bf-b04d-c016b49a0793 | -16.78578 | -57.48948 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f5e82390-5f48-3ebc-a9d6-11214e3b6327 | -16.78477 | -57.49849 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 521754c7-79fb-3bea-8e23-d68f6a0af5e1 | -16.75151 | -57.48063 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| d4eef283-6c58-347f-9532-edd8e6be1e55 | -16.75116 | -57.48364 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| edebd307-2a45-3c55-a416-3e5d17f137bb | -16.7508 | -57.48665 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 6e314b1c-290c-37cf-825e-eae5e13216f8 | -16.75045 | -57.48965 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 121fea23-6deb-359a-abe5-cf977d35e1b0 | -16.74648 | -57.48 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b10e680e-11c6-317a-b68d-ff37ca7030a9 | -16.74612 | -57.48301 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4a3493b6-929c-3a86-b3d0-d03dd370d8ef | -16.74577 | -57.48602 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e29a03fa-6b2f-300b-959f-789898aedf81 | -16.74542 | -57.48902 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README184.md)
