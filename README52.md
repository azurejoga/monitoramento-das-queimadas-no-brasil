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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceaa0abd-bfeb-308c-8ba0-6903cdaf1c69 | -10.20417 | -49.99801 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c4049a1-6aa7-3916-9e13-0829e17f9b0c | -7.88856 | -45.4438 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b20845a3-0204-3828-aa97-604c4e695f7b | -10.21176 | -50.00276 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac727d40-bed8-3674-8e4f-26dba6bec0ed | -10.20316 | -50.00514 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a5059b7-a339-3bfe-825b-5ddcbb8e20fa | -3.14515 | -54.08052 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3b42c58-3d44-3ab1-ac8d-5bd7ca107cbe | -3.07272 | -54.38509 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0c9af1b-b62d-378a-be1f-aa0b7f6cac45 | -8.03474 | -54.90179 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c12eab6c-398e-35ea-96ee-03d283e2591c | -2.92276 | -54.20326 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08020546-09ac-3171-bc89-c4fac01ff01b | -6.78083 | -59.38743 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e9babee-e9a7-30cb-a28d-c75bcd12ece8 | -2.89375 | -54.08401 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10bad1e8-36b5-3305-8e84-543a7d977986 | -6.30482 | -56.03153 | 2026-09-28 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb122b13-9a91-38ce-aa6a-d83f0e668921 | -9.74732 | -48.95218 | 2026-09-28 05:10:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8acbf643-bb28-39fe-9765-cf51e3752918 | -3.01527 | -54.21778 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52448de2-8e33-3f29-b4d6-ebf13a95b799 | -11.18904 | -44.80925 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 2a4df914-4981-309f-9580-d0e9fdcb22d1 | -3.43277 | -50.66376 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 686436d8-4726-3a4b-8713-61860cc640e0 | -11.18373 | -44.80429 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 61cd0d6c-8910-3b0d-96cd-5b5a06d3fd0c | -6.71544 | -45.59515 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38a7b3e9-a55c-393e-94b6-1e790b1022b3 | -8.42161 | -44.87318 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a4e5f41-02c3-364b-95a5-d7114f5e951e | -9.98893 | -50.14314 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a600044a-084c-381c-b807-45fdc790af90 | -8.66007 | -45.41805 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd72976b-7b25-3f5e-810e-74219c777b1c | -5.72114 | -53.45275 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e234e7c-a017-34f7-a520-16cd72a75d6c | -2.91102 | -54.12609 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2af88f2-f111-3f10-a353-ccdcab196f6f | -8.9691 | -44.14057 | 2026-09-28 05:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f78fd598-2ee2-390b-9ccb-574217f632d4 | -6.73346 | -55.08503 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa436d41-bc72-34de-927d-ec233dc4c497 | -9.77341 | -48.21008 | 2026-09-28 05:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb939606-269f-3423-b1d0-af03c700cff9 | -7.6779 | -44.78861 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ad81789-6ae0-3391-8bb7-1f7a91c2b36d | -9.13943 | -47.98336 | 2026-09-28 05:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11601aff-ba21-33b0-b346-4438007610aa | -10.20265 | -50.00871 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8ac5741-4b67-3d55-b074-eb91536eba81 | -8.2411 | -45.4066 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b96d88ed-da94-3d29-bf34-362d70760e95 | -11.18805 | -44.81742 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ecdfb8ad-142d-32fd-9cfa-e6beab915ec9 | -6.66737 | -60.02822 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aea94e9-e5ae-3b1e-acf7-5e2bbc48c052 | -3.6966 | -51.37329 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e2c103c-ce6d-3588-936c-f704b42696f3 | -11.189 | -44.81167 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3bd39c55-0b1e-3c6f-9fd6-1cb0df94768f | -7.28646 | -55.57775 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b048c40-7d53-3773-958b-889a11f821de | -10.21989 | -49.97478 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 180ab0bb-1565-3d23-8e73-d2c18a6bd891 | -8.80186 | -54.54829 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c6856b0-8a95-38c5-b8cb-793b674ad519 | -9.79193 | -44.82742 | 2026-09-28 05:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0506115c-c45c-38bf-96dc-7b899f7ccf76 | -3.20858 | -51.04153 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e2f2363c-778b-32b8-bab0-2e5588ef82e2 | -6.69794 | -45.6488 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb2d7a20-9567-301e-9f53-6fa450b22462 | -10.70989 | -44.42651 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9563aca-53fd-3375-94fb-15ef511e913d | -6.94707 | -41.61209 | 2026-09-28 05:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4d84ff84-5a14-3f1c-8fd6-ea1667ea5fe8 | -6.71634 | -45.58893 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 267f28c4-c64e-3763-b171-82cce93a3f6d | -3.07326 | -54.40324 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0d329a7d-d42f-3a30-9730-3902cb3395b8 | -11.19109 | -44.79236 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 77ad7184-7d86-343d-8a83-46c5c5f59639 | -8.24364 | -45.40285 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a22c5675-e091-3b1c-800e-91edd3ff8029 | -2.55364 | -58.04439 | 2026-09-28 05:10:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89c3879b-4f17-33ba-8ee8-ee3f3b833771 | -11.19057 | -44.7966 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c36c9ab9-b566-300c-b229-85a2af6de989 | -10.70934 | -44.43078 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68b7691f-c079-3394-88e1-a6d238239bec | -3.42188 | -48.34165 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d77584c4-0ece-3222-9b5b-bae5d116753e | -3.0108 | -54.20273 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af2b19a7-b743-3c06-aec8-0970e09f74cc | -7.37854 | -47.0188 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82360216-e733-3641-9ad9-7d7310b973b5 | -8.23976 | -45.432 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1deadf62-6558-3ebc-9262-f98e83b4d8fa | -3.22608 | -54.3191 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41b9b9b4-4163-3814-b9b3-40662319cad9 | -2.97848 | -54.14748 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e2a58a-0740-3b34-8f1c-d15a78390789 | -6.94245 | -41.61815 | 2026-09-28 05:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f3838999-839c-3a3f-9417-992980297c45 | -3.20977 | -51.0338 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 632f66cd-8168-397c-8a82-742dccbdb130 | -3.41445 | -48.34093 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc055c14-1790-3a93-b202-0a9346b2d71c | -6.08467 | -57.80388 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58200b01-da5c-3865-a20a-4fd6c4c6af9a | -8.41602 | -44.87248 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c77a6c63-27e0-3fba-9ba6-0b29bb9a46da | -9.82283 | -45.26305 | 2026-09-28 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a938943e-f819-3e65-824f-eaec36b8202d | -9.98268 | -50.15813 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d2579270-c6f0-340f-9362-3caacfb19f99 | -7.498 | -55.02027 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fb7dc6d-d386-3472-962b-6f4f033fc857 | -6.07199 | -57.81098 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9de6afa9-bd05-3bd3-be47-37f07fe2fe12 | -7.34415 | -42.07331 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 823f6c41-9499-3488-846b-2c6269f968f6 | -8.03141 | -54.90126 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b715819c-7a0d-3c68-b6fd-d8cd50607406 | -2.06265 | -56.86657 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 729073b8-2968-319c-af46-bd9686dc52b5 | -4.0576 | -47.50056 | 2026-09-28 05:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48d74b3c-4d6c-3101-84d3-010864e24b64 | -5.89543 | -42.4329 | 2026-09-28 05:10:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8c0fe9e4-1d12-3615-986d-505b990048d5 | -10.00795 | -50.12465 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d86ce75d-f32d-3547-b77c-75dbafa9e60c | -10.79538 | -48.73778 | 2026-09-28 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 54f93009-e8e3-3dd4-95c0-e6dade1e5297 | -6.16391 | -57.70128 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 527f017d-9d1c-3665-b3c5-f7bec3179c48 | -8.03919 | -54.89534 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aff4045e-ddf7-3754-a132-0cde2473d83b | -2.96402 | -54.08791 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28149201-eef4-3f08-8b9f-781e5d4dea07 | -2.93876 | -57.91703 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6077b723-9c42-324c-a68a-dcd8f2273dd9 | -3.14906 | -54.099 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d959380-ebec-3bdb-83dc-122d8fba327e | -3.23738 | -50.57782 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e58fedb-ccc8-36a1-8398-c65955758549 | -7.50133 | -55.02082 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54f93b12-691c-3c28-8ffb-1a6b9d1e3358 | -9.47853 | -46.39419 | 2026-09-28 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3ef4c74-afbf-3e3e-8798-6fd892459995 | -6.78266 | -59.3766 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fdfaf0a-9010-302e-aed3-89f9bf14b7dd | -8.90021 | -46.19055 | 2026-09-28 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d193197-47ad-36ae-a6c4-3c7766fb066b | -1.81243 | -57.10106 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a2889a-e605-33f4-a05c-603c3cc98335 | -7.27239 | -55.5792 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04e92520-c1b6-3c13-ad34-4d28d36aed59 | -3.20551 | -51.03407 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7552ad4b-ab8e-37a4-a51f-9cb5ddebf410 | -10.22291 | -49.98256 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fac1d390-6904-3483-b812-a297ad53f074 | -8.96687 | -44.15781 | 2026-09-28 05:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 181c7ff7-da92-3752-95eb-45db320e5471 | -4.85189 | -42.888 | 2026-09-28 05:10:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09e0a936-6998-3f98-a2af-65c0eed07ee8 | -7.37984 | -47.01011 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96cb0f11-e843-3004-8662-b191a019cb20 | -8.6621 | -45.41413 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd3436e2-dd32-363c-91d4-b8dccd09499c | -6.09376 | -57.63359 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb75ee08-0e1b-3a03-9377-df0ca88d6f70 | -9.77668 | -48.21953 | 2026-09-28 05:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c38787e-e3cf-3261-8073-a26e5be25f69 | -10.00395 | -50.12405 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 13e544be-64a0-3d7f-bb8c-4371a2b49cce | -3.41146 | -48.33328 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5046aa2-abaa-35f9-ba0d-1c0fa8de4e44 | -3.1979 | -51.03683 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13718fcf-e523-314e-8160-a58d9dc6e015 | -10.21076 | -49.98075 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19f80d4e-55e0-3547-82c7-27f2d20a63cd | -3.26728 | -50.14573 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cee8254e-5448-3d4b-85ae-ce2a58c5b771 | -3.01025 | -54.20623 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d801d9a-df13-3a24-b4f5-bc7411aa2b9a | -6.07221 | -47.30368 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d0de3068-0702-3937-a2fc-fea0da16c413 | -8.0353 | -54.89829 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2e807ca-f352-391f-ad0b-70148214e11e | -9.98568 | -50.13734 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 106d47ae-d3be-3f75-bde7-7c26bb7ddc58 | -3.415 | -48.33739 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
