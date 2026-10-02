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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc2208ed-ab2d-38f8-8cee-ae75c7f36d60 | -6.14786 | -47.46326 | 2026-10-02 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4ef51505-a139-3608-934e-e6a08aa5ac75 | -4.98953 | -56.14988 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bd55651-47e6-3ad3-8940-52f9ae427f93 | -4.25019 | -50.74795 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb5a0a57-bea6-32db-ad01-993dfdd3d34f | -3.29888 | -53.85408 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 650db01a-ecd7-35c3-8445-d81ea3a86058 | -7.8316 | -55.13713 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13957fc1-3d99-3b19-9295-0461e44477c7 | -7.57693 | -55.13182 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 54c8317f-eaab-3b5e-8c68-5ef7c1b17260 | -7.5955 | -55.05657 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f68564dd-df84-32dd-8c12-7ca02cdcc7b4 | -6.44616 | -51.70073 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a8dc21e-3ab7-31e3-a5c6-abfa16d1c254 | -7.74223 | -54.79259 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ba3dbf-beb6-34ba-80bb-0be06c8b66de | -6.25542 | -55.48347 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb331d66-7218-3ea5-be85-2a6635f5f783 | -2.95489 | -54.09538 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2ea9f27-f5d4-3a92-a92d-c0475ab8e0a9 | -7.49356 | -54.99014 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 230d7843-6dab-3990-9a18-e53acd854f87 | -6.23672 | -53.14104 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cbb55d4-7b9c-3cc4-934f-5c57256e9f3c | -2.99149 | -51.04649 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dc7b481-8be9-33cb-9c6f-e5f4fe8cfd35 | -4.28903 | -50.78365 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 306983b7-58f0-3e9c-81af-8b60567c56f9 | -3.01244 | -53.88276 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084fabc7-623f-3a31-912d-42fc11134e7f | -3.12602 | -50.27895 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d776382-74cf-36e9-90c7-158e3bd31786 | -7.83876 | -55.1347 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f643673-3366-3002-a8ba-87e2416744cf | -3.13135 | -53.75427 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c4616f26-0ff6-3ee9-8e23-ae2897f71ede | -6.24061 | -53.13801 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| debf557a-0321-3b36-b938-0c88776d7a39 | -3.53937 | -55.52781 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e192036-7b52-362b-b78a-b2d0d6d16d42 | -3.6859 | -55.48708 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf715b25-8536-3465-9a33-5de2162505a3 | -3.18267 | -54.09986 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ab39b286-7eec-3679-845d-9b0572489abf | -6.40182 | -55.20452 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eed30303-002e-3872-a0fa-e9b952ea280a | -6.44027 | -55.62603 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0943cce1-47ef-376b-b0fe-a8620d01e55f | -6.15253 | -55.44585 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70210b36-6399-3bdc-ad37-3aeba4b6d34f | -3.20954 | -53.40466 | 2026-10-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0ca254b-5ea0-3a2b-ba0b-813f38e722b6 | -2.04955 | -56.87079 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 59f55f9d-a51c-3c1d-aa3a-8bfa9029d1fb | -3.28898 | -53.85255 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37b45fed-9331-339f-b997-efbf87698a8e | -2.9834 | -51.02926 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f91562d0-ed1b-320a-98ff-d3e1ce7203d7 | -6.2473 | -53.13903 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 189cdf4e-42c0-36cd-8906-597691953c38 | -3.10089 | -50.29431 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83d5ebb9-0e37-38ae-9f4e-9b5ce075527c | -3.58674 | -52.21631 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b353035c-19a3-318c-abf3-e1c0886962da | -8.18134 | -54.7913 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3bd036f-5890-3927-b54e-8a8efdecc939 | -2.62231 | -51.70618 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37145ad3-4e2e-3799-8d12-11a318fceee1 | -1.63886 | -55.13005 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22fafe61-8845-3410-a7fa-44a46ae422d5 | -7.2771 | -55.58844 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 808cc7ed-69f2-3f0d-96c3-8c24e2cb00af | -5.23611 | -49.58541 | 2026-10-02 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37eb3c56-c331-35ce-9ce6-fe37234551d7 | -3.07555 | -54.36945 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bb73af1-ed4c-32d4-b048-3e0fc39145c8 | -2.94552 | -54.09041 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a232fbe-39c6-35bc-9872-842d37510b2a | -6.41 | -56.40619 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e08c29c-fa16-32fd-8e94-444ed0ea5b7f | -3.7236 | -52.39207 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd9a7058-ffb5-3b8c-a663-4c20b0344fc4 | -2.88285 | -54.8803 | 2026-10-02 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 303a28aa-5d56-3663-8ab3-c1788253c326 | -8.16322 | -54.7991 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9357c53-9b69-350d-9434-4db7fd4cf74f | -3.98036 | -41.51678 | 2026-10-02 04:57:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3ab4fafd-bd13-3ff4-8dcf-91c787134dcf | -1.4495 | -48.93445 | 2026-10-02 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad4ad5f3-8f67-33f0-b762-c6843e1c5b48 | -7.46389 | -55.00676 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15973c2b-09a6-3ffd-a45a-9f34e317f043 | -7.46611 | -55.0142 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b0a76f0-c975-3aaf-9c92-0554f81db7c1 | -6.70364 | -55.57663 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1142a7dc-a46f-38b6-b605-000e139e756c | -9.52952 | -45.32933 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d0026d9-2d54-3daf-8c28-ff7d7f439fc4 | -1.65341 | -55.21492 | 2026-10-02 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a40ee83c-7bef-3c8f-8538-784a94b58545 | -2.93705 | -54.18793 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4235a587-b88e-3d8f-be35-eb4d00054c36 | -1.08448 | -54.11077 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9636afc6-e32c-3ead-9670-37accbd1c01f | -5.39364 | -55.88058 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5018c1d4-e3ca-3dea-8672-5e463f710971 | -2.92187 | -53.9389 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf72b4f4-2b3b-35d5-881d-7f04c21f8422 | -8.2549 | -54.73619 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39b1bfdc-af7b-3e44-b34f-3c5b5cea915a | -4.29091 | -50.77123 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05fa16e0-92fa-3849-8629-c2b751ec850b | -3.18213 | -54.10331 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ba94b21f-1e62-3cea-b9d9-94e770406c33 | -6.40626 | -56.40619 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fde8130-bbc0-3267-9fb5-d8c0f198da74 | -2.25531 | -51.35577 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 536a8de3-dcdd-3201-9840-df6e29a778e8 | -3.29834 | -53.85751 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a1e9888-6d98-3931-aa46-77c698051416 | -3.07887 | -54.36995 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 390e1bef-e92e-3430-b129-a690bb27be62 | -2.71562 | -51.9183 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ce00727-7599-30db-9cfa-bc79bc5f7c38 | -3.88051 | -51.89904 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f54ebf54-914f-3acb-b146-4b982d4df682 | -6.39684 | -55.19303 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02a1f928-853b-31c8-956d-a2da8431cdb7 | -3.13956 | -53.745 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bfde8317-91d2-314b-a9d7-c4c6b31d379d | -3.02941 | -51.27295 | 2026-10-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81a4e8fd-2f99-37be-af3c-a160e244506a | -2.89225 | -54.12804 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f726875f-18a5-3dfe-8168-ab0ff77d3494 | -7.72783 | -54.75492 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07c4b5ba-4bed-3a83-8b04-43028daa9699 | -1.41536 | -48.89966 | 2026-10-02 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83e31f1e-352a-306e-b49b-46163af3576f | -3.15895 | -54.07483 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f6186fb-4507-34e1-b6e5-534127d1e7ac | -3.04374 | -53.87704 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83172c92-cd1b-3f59-8935-240cb459ef01 | -2.90533 | -54.08774 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83de12de-5a48-394b-bcb8-2f7e48039cf7 | -3.49296 | -54.72359 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1afc708-871b-389f-b561-a3a54dc66c8c | -2.9801 | -57.9087 | 2026-10-02 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6697c957-4531-3f8f-92f9-61967c75e459 | -7.4169 | -55.58586 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 465c52ae-622d-31fa-9f40-35f0d75637be | -8.16771 | -54.83527 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b24d33f-04c8-3af8-bc6d-0a839d063541 | -3.14446 | -53.73522 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc6d6d30-79f2-3d16-aaca-39422fac936b | -7.77821 | -55.62558 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28bade4c-3580-3226-a8a4-023cea785960 | -4.25554 | -50.76149 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04602179-1c22-380f-ab6f-98b4853fb001 | -7.69567 | -54.85253 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40411ef2-e34d-37c0-8e37-cfe2ed71654a | -7.87968 | -44.17664 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f487d29-8328-39f4-9c15-38dbc8723da7 | -8.23523 | -54.77565 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dca4bffc-af67-3d4e-8149-e2fd779bcb8e | -9.52742 | -45.34451 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f19423f-9f6b-34cd-88bd-a035713b4004 | -4.92734 | -47.54612 | 2026-10-02 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802843ff-1907-3131-8eb0-e14f6a13b904 | -3.8061 | -51.03022 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bee06f4d-7630-31a7-ac83-17a9b91ccc96 | -4.28073 | -50.76544 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 478cf142-abfd-35c8-a2d5-501fc68ab4e4 | -7.28542 | -55.60053 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce2437be-46ab-3b9c-96b1-efa6147c64a2 | -6.75461 | -55.08224 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23a61f93-d827-3f7e-8a93-2ba8e3a4a2eb | -3.27225 | -50.7031 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96261d30-8f5f-3e73-81d1-9ccd03fff100 | -3.2695 | -50.70401 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2daa93f4-d4d5-326d-8830-588afea73790 | -5.16842 | -55.99911 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb33137e-348b-3619-bc91-31297b0bff3a | -3.97865 | -41.52229 | 2026-10-02 04:57:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6743590e-18f6-38fc-a8ac-720def70b5d3 | -4.26695 | -50.75906 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1941b7b8-e23f-3247-a446-8716bb811f9d | -6.74645 | -44.14159 | 2026-10-02 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d929176c-8ef9-325b-b81b-894f20869972 | -1.69106 | -55.66836 | 2026-10-02 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f07a0611-2f62-38f5-bdb8-12a180241cdd | -2.90878 | -54.13059 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c6faf2e-02f3-3cfa-aa8d-5df347c9bbf4 | -7.33615 | -55.57976 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a53f7aba-4571-3cca-aea9-8d5c5868dfc0 | -1.6033 | -55.12857 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f01ecf43-21a6-3ac5-b632-d116e9058c2f | -4.29685 | -50.78062 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README63.md)
