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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0328d795-77ec-3618-8f18-ce887d6ef8f9 | -3.9077 | -49.99137 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6dae707-97e6-3a53-8bad-ca10a0001df2 | -3.9038 | -49.99438 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f39ec9-6600-335d-b089-909c69a91a84 | -3.90102 | -49.99033 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36197f87-8335-30fe-8bdd-719127c3bfeb | -3.84454 | -50.00685 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e494f367-271c-3e3d-8616-d83562f4b4cc | -3.77456 | -50.18845 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da889682-03af-31a9-a053-425c14caa8ee | -3.74795 | -50.66212 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53059965-025c-36c0-821e-f08125b8fc69 | -3.69246 | -50.19363 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ddfd50-e8be-385a-aa83-a6d015f94b98 | -3.6891 | -50.19311 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5053effd-72a7-32bd-8153-1255ff0e26a3 | -3.6097 | -50.58398 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 658f6462-12fd-3fdb-853a-df52bbf713f5 | -3.60348 | -50.57926 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aac0c8bd-161e-397c-af4c-f22334d4e80c | -3.5995 | -50.58234 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27ce9194-e079-3e5a-8e17-50744d417f7a | -3.59436 | -50.59274 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2ea736d-4949-3f4b-916b-e9b9cbc2ef22 | -4.70693 | -50.58739 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d48b3b99-7758-3dae-892b-2708b60f8b04 | -4.67185 | -50.63359 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8953aa9-7c5b-3941-90b3-c97310796fa5 | -4.67127 | -50.6372 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fffca866-389c-39da-933a-a6525b9a7c75 | -4.66847 | -50.63307 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ebd05e1-3e13-390f-9c14-cb4bb1940edb | -4.66789 | -50.63669 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8544e273-a1d0-35b3-b85f-21d130a8c1e9 | -4.66508 | -50.63257 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2008344-d30c-3df9-afd0-1ed98182da3e | -4.6645 | -50.63618 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7feac75d-63e3-3b93-a33e-09a733d5abe9 | -4.64691 | -50.76749 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b4b6213-2683-378f-b731-e49d2bb455ec | -4.60961 | -50.66872 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d749f6c4-da8d-332f-b02f-aafa38ae96e6 | -4.60903 | -50.67233 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a6cffc-402c-3e29-9671-0413adc82dbf | -4.58757 | -50.67638 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df2ac3c8-90e7-3706-8c7b-fab6527f8eff | 1.65427 | -51.05994 | 2024-10-21 04:36:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 177035a5-eb64-3d3f-9b1b-a0be10a7d10d | 0.99611 | -51.18302 | 2024-10-21 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d786643-1c58-3476-99e1-ff54a9c1c06d | 0.99545 | -51.17875 | 2024-10-21 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a4838ba-b5c6-3a7b-a15d-0cd520019b90 | 0.39753 | -50.95166 | 2024-10-21 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91136e87-f4b6-3b58-bf4a-e089a0ce6957 | 0.39624 | -50.9435 | 2024-10-21 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2340cd2-6574-3d52-826b-974a1b806ef4 | 0.39559 | -50.93942 | 2024-10-21 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a25200c-fa51-3edf-9ca2-b067937db9ac | 0.27257 | -49.92227 | 2024-10-21 04:36:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dd9668f-e9ca-3c78-ba29-d8917c67eb65 | -1.67119 | -50.46835 | 2024-10-21 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffb7acb0-517a-3ac5-8331-92723b241c6c | -1.66776 | -50.46781 | 2024-10-21 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 604f6d01-29b6-3d19-b102-5e2959c02d1f | -2.23497 | -50.45176 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d16cb3b-f63f-30e6-a492-a2e44241f233 | -2.22754 | -50.45438 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bc91ccf-24b0-3d9b-9799-f13f5dee84a5 | -2.22695 | -50.45809 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d320993-ce3b-318e-b81c-edb7b61b1373 | -2.22637 | -50.46179 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfa727ad-4fbd-3e38-a08f-902cdef29b2e | -2.22412 | -50.45385 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 744564d9-5db0-3398-8e0c-bf9da66c643a | -2.22353 | -50.45755 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d58321c2-9af0-39aa-b22a-e7ca305a52a5 | -2.22295 | -50.46125 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6919b0db-ad5f-3188-b078-4b7ffefe1a70 | -2.22011 | -50.45701 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5c9a8c2d-1877-39fc-b882-ef3e354c6bf4 | -2.21952 | -50.46072 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 637abfb4-6cfe-39d7-b8c6-623374e4a9cb | -2.21894 | -50.46442 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90ad3342-8522-3def-8c2a-d5d0b29972fc | -2.20985 | -50.4554 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acf44d3c-e5cc-395c-bfdf-89f0967707d8 | -2.20926 | -50.4591 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38c78178-7e19-30b6-a9c6-cbc02cd8a2dc | -2.20867 | -50.46281 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca0b98cc-9acb-3b39-b7b1-198f0bea2f32 | -2.20808 | -50.46651 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8689e94f-c1cc-35cb-b271-a742e478e667 | -2.20525 | -50.46227 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a913189-e07f-35db-accd-bbe507ac2aed | -2.16717 | -50.52481 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 392bc8c5-5185-36e7-b832-cb683485b20d | -2.16657 | -50.52854 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 251be963-43e4-3034-9db2-47f91ee64e11 | -2.16368 | -50.70114 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f09e98bd-61cf-3383-82c9-06c7267579d9 | -2.16314 | -50.528 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f49bf42b-4f8d-31f6-acdd-cbbd5eac7d11 | -2.13204 | -50.83254 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 454b3abf-c0b8-350d-bbe7-8a2e1c5358d5 | -1.84874 | -51.26671 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b7ff54d-54db-3ede-9a86-52e5593b0d9f | -3.17652 | -51.25508 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0805961-00ac-3d52-b9c1-a20cc5977bf9 | -3.15562 | -51.2958 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb4cf03f-aa89-3c33-a23c-f1ed52858a8c | -3.12571 | -51.34733 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3957223e-d9ca-39ee-8e44-1d7e15a99377 | -3.1222 | -51.34674 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c4feafd-b82f-39e1-bffb-71e00636ed9c | -3.09984 | -51.27929 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71128ba0-fe2e-3f66-a066-6537edb1cfd1 | -3.09633 | -51.27873 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7142e67a-d18d-3382-9411-99742853b267 | -3.0916 | -51.21805 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bc1b454-44d0-3bdb-b537-00a9aa58f274 | -3.09098 | -51.22194 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86bb119b-4d14-3ceb-a335-ad7868577b08 | -3.08932 | -51.27763 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 422652d0-9b9d-39ad-98d5-12901c0b8068 | -3.0881 | -51.21751 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab5e03b0-ada8-3b3b-bb6e-4adce87d457c | -3.08748 | -51.22139 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5891444c-d4a7-359d-b71b-2540c4e36d9c | -3.0846 | -51.21696 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50656b7e-f21a-394d-a253-894a1fbc0dff | -3.0823 | -51.27653 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c8f0076-c2ad-3e64-8843-703973800842 | -3.08095 | -51.10543 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3970474-7eab-34f2-8e37-0b3a230fd214 | -3.07761 | -51.21584 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b4e33b7-26e1-30af-b10e-6ac7ea73abbd | -3.07551 | -51.25149 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fea29cd6-5543-3688-aae4-1fe6cd6249c5 | -3.06478 | -51.09497 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22ca0cb4-76f8-320a-9e88-6f3f1523c8ad | -3.04212 | -51.02525 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eda632f-3e46-32cf-9132-baae9afa5685 | -3.03925 | -51.0209 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1437e6cf-30df-3bfa-aa4e-fb0b9317b8e3 | -3.01572 | -51.35467 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30ee0dda-20bf-3768-a3b6-ba84274fa808 | -2.9968 | -51.04162 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71c45226-cb22-3ea6-afd5-79a3a0459ae2 | -2.99619 | -51.04545 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7d3a979-c7e5-32fa-8608-96e953e0b954 | -2.99026 | -51.06025 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4839aa4b-5bf0-3034-b3ee-7be27585a2f7 | -2.98965 | -51.06409 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 358807ee-c4a9-3c18-9ec3-6b2d2cb1b332 | -2.9876 | -51.03231 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffdac9ed-47a8-39a9-8fdc-f16aae7ce932 | -2.9874 | -51.05586 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7314f32-9eff-348a-924c-c2ac2f6c74e9 | -2.98678 | -51.0597 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bca7bcfe-ba59-380e-a823-20300c36035a | -2.98453 | -51.05147 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29aef165-b00a-37c4-b9b3-9cb66707bfb6 | -2.98412 | -51.03176 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0834e457-7c61-399b-b617-bbc570f8dcaa | -2.98392 | -51.05531 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a85467e6-b851-3ebf-adb7-533514436a6b | -2.94912 | -51.03846 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c5a7f16-e430-3890-8d2b-da3e6481465b | -2.94753 | -51.03776 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1eeb581-9eea-3d01-953b-c269875cfdc9 | -3.58795 | -51.28923 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 363ed302-3cef-3f2e-bea7-1f34b0d4db2e | -3.58446 | -51.28866 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d5184ae-cda7-3fe4-a712-ba8a4c1eef51 | -3.54774 | -51.38261 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3ce786b8-2d45-3980-8d2a-a1713d79c820 | -3.54267 | -51.38639 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 350befb7-c65e-367f-8a95-f6eefbce60ff | -3.53948 | -51.47799 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b36da98-57a3-3f8e-9d03-5cc573dc05da | -3.50494 | -51.35223 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7efeb8bb-41aa-3aed-8f5b-5f81da527900 | -3.48783 | -51.19081 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74b10649-ba90-3609-9560-baf05e33d6d1 | -3.38312 | -51.39009 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b35dcb7-9602-3c58-8701-d2aa63493d7d | -3.36771 | -51.50929 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 471acf98-37d7-36f8-9623-adb0458d38d7 | -3.36708 | -51.51326 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 987bc24e-52db-3b79-9391-8ab2c63a55cf | -3.36618 | -51.05931 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68acac40-0af0-3c23-be7f-871aa19353f4 | -3.28321 | -50.94174 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac598ce-18b3-3799-b557-7b8e32014c7d | -3.23881 | -51.36441 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83a6b88f-1520-36a3-99e3-78f20dbac16e | -3.234 | -51.14119 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc1f6450-b8b4-36eb-b096-7f1871fe50fa | -3.22704 | -51.14006 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README41.md)
