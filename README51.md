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
| 8cd725a4-adb4-3317-8e38-ea4f56221184 | -1.16478 | -53.67912 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e295fca-13d9-3d44-8292-3a40d152d1bd | -3.28877 | -53.7805 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 547662fb-6056-3175-b058-a07fc118e030 | -1.21119 | -53.75402 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cb74976-7aa2-3e46-9098-8dc59a767d8a | -5.22369 | -44.92037 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edf545f5-e325-3018-8513-ac01de4aa616 | -2.60712 | -54.07146 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bffa9aaa-2cfe-3ee3-8608-e38453914a42 | -2.79816 | -53.96067 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 677a2b25-7847-35f9-8e08-40fbf1a82d94 | -3.28894 | -53.27699 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c26512a9-5898-3207-9b90-39200e95cfcd | -3.02677 | -54.02076 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 32d3e2f1-8f84-3267-b062-b1fcbdffb8b7 | -3.97644 | -49.97886 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2fef29e-7792-359c-9142-b10516da8b4f | -2.57484 | -53.97473 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9544c6b1-d3a0-37db-b2f2-ac9b218f59e6 | -1.71598 | -52.76311 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a8391a2f-f59d-38fc-9c38-d968f78cf455 | -2.83453 | -54.11789 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcec997c-eb7e-39ea-b40a-845db4719cba | -2.81156 | -53.02199 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54ff0e78-2dd4-3a1f-91ad-9d8fa95980ee | -1.00007 | -51.72413 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a75c9f58-68f8-3c28-8ac4-969ef5bb0420 | -1.30634 | -51.92106 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 781e9fe8-17e1-30cb-a50d-abeb975b6ee4 | -3.11785 | -53.10864 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7693981f-9c20-3ac0-801f-fca31727b358 | -2.60595 | -54.20918 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 233a3701-0c6c-35f4-9636-6ec71165704f | -1.15424 | -53.39994 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb7eb92-01e9-3ef3-8a0a-b405834f7a73 | -4.17809 | -49.40738 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acd23415-2098-3174-9f0c-bff36a5e9670 | -1.98638 | -51.51956 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66c824df-4a95-31e6-aa1b-066ab62521c3 | -2.69563 | -52.91549 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92267b13-c4c7-3d93-b9f3-201c0b63c613 | -3.82931 | -53.58739 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63b37ffb-3d80-3667-a193-28721b85e04e | -1.37527 | -53.63853 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1875abc4-86d5-3b34-83b7-c43f68fc39b8 | -1.06893 | -53.63969 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbb9fd0f-1d26-3d13-85f8-a636d129922d | -2.84906 | -54.02489 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b62274e0-ace6-3ad5-92ef-09d581f7e9aa | -2.25972 | -53.46463 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83f44c90-9443-34b4-856a-8bca979208c0 | -1.24914 | -51.63314 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c10cb82-e288-3f7c-a5cd-c74584ade8f0 | -2.81204 | -52.99719 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf7e040b-038f-338d-8aaf-e82d900fb6ee | -4.41357 | -50.82713 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9514e7a7-abbe-366b-bf19-f6419469f4f1 | -1.33828 | -51.93692 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 734da149-4fba-3a4e-8c27-dba1be40106e | -3.41799 | -50.15989 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cdfd7d1c-cf29-352a-896b-13b569985240 | -3.09636 | -54.29342 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8db36b24-e637-3589-a862-3125c67526b2 | -3.70172 | -47.12686 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a08d65d-4b4c-3242-9a1b-4bba232600f4 | -4.07378 | -54.5677 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56e22ba8-5931-3a4a-bb04-fee0bd794d3b | -1.52738 | -52.03162 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c3e0585-e958-3fd6-bc69-2e11a4bd7714 | -3.26825 | -50.62469 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbfb979c-b940-3033-89e7-87ac4a6f1394 | -3.22057 | -53.38985 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f836d07-d01b-312b-a98a-f5dad3c0bc8e | -3.81514 | -50.9518 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b22110d1-bf18-35de-a6f9-9a3ef235f577 | -1.15088 | -51.69907 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59cca61e-4cc0-3884-8ffa-10647b3fc245 | -2.45113 | -54.00495 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f85cdc0-e663-3477-8d02-c1a4928ae60f | -1.36056 | -52.53355 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7dd80f7-0a54-3ab5-a99e-d4ace7631fe7 | -2.84099 | -54.07652 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d077c88-fe1c-3e7a-aba1-d64c49663c49 | -3.11991 | -53.2716 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f2acd9a9-07b3-3991-8d69-8a1e5e837d96 | -1.52742 | -52.05343 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf71f473-bc04-35ad-bdcf-0b385e37c844 | -2.42543 | -54.01451 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67a5bd5c-8e3c-32fd-8cd7-f11ca0a8e4e8 | -1.15032 | -51.70266 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa43d7a6-dd5a-3ef7-a521-9023dc11d36a | -2.59468 | -53.97779 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f197f21-3507-3a34-88c3-02d09a55289a | -3.0516 | -54.03516 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e526f3b0-991c-3010-a438-d686a46fd359 | -2.43763 | -53.893 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d33884f7-2b5c-3e4c-95d3-9cbe758df0f9 | -2.78115 | -52.8683 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d546b561-29d2-3f9b-8ca7-494d387a1394 | -0.30777 | -51.77874 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 457d0827-f77f-3ac0-a5e1-4a95dba4a3e7 | -1.35294 | -54.6329 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0df9e1dc-c512-347c-8afe-57a686867d2e | -2.87774 | -46.86967 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ae036d2-91b8-3aef-b5e4-f5281349c8a8 | -3.84356 | -50.09009 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a677b881-976a-36fb-bbb1-5d5c985e2939 | -2.79684 | -54.05561 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88c4c617-21c5-361d-a73d-0f12e4892b98 | -1.10363 | -53.39554 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7005bc1-9034-3590-9bb1-c6d4bc2d2314 | -3.52818 | -53.68454 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ded01a43-50c2-33a2-a37d-ce56986086b1 | -2.26928 | -51.91385 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dd8e65d-3afe-3240-9186-2ffa5f511117 | -3.21998 | -54.06903 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8674fd-828d-35c6-be29-2e161f233f60 | -2.60766 | -54.06802 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d25c4cc4-d666-3326-9b2d-a5c937163a1c | -2.76659 | -54.07564 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9109317-65f5-3a76-9954-25315fa2cb07 | -3.15837 | -50.58424 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1fe5b4-aecc-34b4-be26-87bc96718d6e | -2.66105 | -48.79387 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 9fa0f1f8-63e7-36b0-84a4-7f141c02cbf5 | -2.40535 | -53.66644 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1112113-d04a-37be-ae93-ad84621b5ddd | -3.37409 | -50.82681 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec9b39a-c695-3f96-896e-7ee37012ee5f | -3.95393 | -46.72793 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ad92d1b-1502-3c4c-90d2-0632018da795 | -1.35675 | -55.64231 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 044fcc8b-464a-37ef-9e29-738195de114f | -3.86464 | -50.15239 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dda08aa3-fc4a-3f52-b5a1-f1ddeac2b0a2 | 1.28172 | -55.9173 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d16329a0-4252-3a9b-9eae-4c2458dec4b3 | -3.22158 | -53.62228 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da58d440-5e1b-3b5f-8f59-1a177f25d05d | -5.23278 | -44.91417 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a74cf66-08cc-39cb-9b6f-319397a01874 | -3.06974 | -54.0274 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201978d4-9d2f-30c2-a677-e80747acbb48 | -2.79015 | -53.20592 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed8bf30-2a05-3f85-bdb6-6af7ada0aa77 | -1.92174 | -52.88322 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c57ce28-c277-34bc-bf05-547bc63d662f | -2.6439 | -54.03126 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f158844-df00-35e2-980e-d5fb9517698b | -3.11188 | -53.97815 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef36a5d3-6f9a-309f-9e18-92c72ce79c05 | -0.1036 | -53.22158 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61bc551e-8748-3d2f-9036-285c7ca502eb | -3.19978 | -54.74097 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f0347c-1e37-388a-8c34-22ee66b3153e | -3.10669 | -50.35963 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8cc9c3d-66b4-313d-9682-9ac74c6c9eeb | -3.10919 | -53.99533 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a75f7f28-2f15-31d6-a0a4-9da94eecfae7 | -1.22952 | -51.80347 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b37b7db1-6c55-3e1c-976e-1c4224d548c6 | -3.70842 | -53.75121 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64750a48-05f9-38ae-9ece-3a56c4f1c90c | -2.79162 | -53.9808 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61cbfcec-a5d5-371c-be2d-0f84800ae38f | -1.4612 | -51.51186 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b06f1f65-89cd-3efa-84b4-446410550f7d | -2.86489 | -53.98856 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 526159aa-9e7d-38e3-8280-f40921fc233a | -3.63434 | -54.4415 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e897e0-7ca7-328c-a8cb-f01cf1d751f6 | -2.01233 | -55.40356 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d59c6a86-7fb6-3f39-a395-e4fafed906c2 | -3.70948 | -54.6136 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f8e6495-911d-3a74-a660-22c62e109ef5 | 1.26926 | -56.0048 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc9e1196-2c12-3f2d-8413-bfb9491fbaef | -2.98109 | -53.35235 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab95a864-5e7d-35df-8b0f-8e151a4e2ac1 | -2.40333 | -53.85251 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68e74082-4835-3c3a-94e2-083edac75506 | -3.24471 | -53.62584 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c713964-5fb8-39ea-8ba5-c12189d76bb0 | -2.41477 | -53.82259 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e67eda46-4a8b-311f-bab2-f04a2bc65219 | -3.29279 | -53.27404 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8910815c-ac83-3ad2-b5bd-64fb2b5fbef1 | -1.30151 | -51.72954 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e7bb783-b3b3-3cfb-ba3e-3eb72593899f | -1.27305 | -51.82447 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b83157c-edd2-31c4-bc4a-2c2304d7bd12 | -2.06236 | -51.18596 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 668a5687-b0f3-3fb4-bd6c-01233aa798c2 | -2.76461 | -55.32738 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e32e2c6c-1334-3cee-9b92-d8c4a3c6f34e | -2.58024 | -51.92382 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64770357-f7be-3e59-9a3b-61fd32df36a1 | -2.6451 | -54.28612 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README52.md)
