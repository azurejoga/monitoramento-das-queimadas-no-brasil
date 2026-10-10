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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63352029-5468-306c-a3d4-4f8efb7fc473 | -3.64094 | -54.51879 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c956cfc-6006-3875-bd94-81a7f6bbd97e | -3.58136 | -54.38084 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c064d093-2ffd-3663-8a50-7e00b455feb9 | -3.16513 | -58.62164 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7567b09c-7a44-3221-ac26-3a4361260ee6 | -7.19169 | -55.15987 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 397bde7a-9a8a-30c3-b087-72b829a7c2ce | -1.42527 | -55.34298 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 051c5197-c8ea-33b4-b6d2-503f55bab6d7 | -3.31764 | -54.05251 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aed547d-fd14-3e9e-9712-d24b289529b8 | -4.28939 | -54.77882 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b85722cd-2740-37b7-9a4c-1d180d5bff9c | -3.63143 | -59.5702 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9709dddb-6426-35c4-9a76-f8ddc9303bb7 | -6.43275 | -55.27481 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8571eccc-1956-390b-b4a5-7a608451aa4d | -3.47289 | -50.08768 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0d8a9ba-2ddc-3855-828b-60db14f989f8 | -3.02002 | -49.62934 | 2026-10-10 05:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59f20950-218a-378f-99e4-7a1efddf6bdb | -4.16237 | -54.99988 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 105ed2a7-7d0f-3d9e-9b1c-2dbf5eb615dd | -4.40902 | -49.78222 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d5174808-b3fa-3b4c-b40f-6b774ef6dc7d | -4.96505 | -55.12027 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b86b96b-ac65-3ea8-8df7-6aca3ef1e36b | -2.75811 | -54.10886 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 894cf8ef-bac4-3f55-90f7-80711d68a19c | -3.24571 | -54.03374 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dec1c2d0-7338-3f9f-a18f-78506e20642d | -2.65447 | -54.31284 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 483b2796-e420-3d3f-a2c5-908ee048456f | -4.32039 | -54.90596 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0075885e-8767-3f18-8da0-35f38bcbfba9 | -6.66881 | -55.09407 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 588293f1-77e5-365e-8d6e-47ab8acdb5f6 | -4.55626 | -54.95712 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d824fe0-c16e-345f-9530-68834a89886c | -2.8676 | -54.21157 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a844090e-c9dd-3f4d-8cf0-66f2e97722b3 | -6.94227 | -59.11077 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dfea6219-3677-3481-981b-cf5a20d41f9c | -3.90507 | -58.94542 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89c9a2ca-3487-36f6-a9cc-d06da1219f3b | -3.95431 | -55.34033 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ccd4965-0958-39ff-ab1e-47c8686272ec | -7.46518 | -55.02141 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc790521-b6cb-35ee-b3e1-c0efa961fdd0 | -2.84987 | -54.13075 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d83c371-c1b4-3e06-ae99-13a7f64485be | -0.59473 | -52.06481 | 2026-10-10 05:04:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59cdd705-1e6c-381e-a696-21dd1f7d24f9 | -2.89012 | -54.06982 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 241f12ae-cc78-3350-80f8-d2ec1defbcc5 | -1.14727 | -54.21867 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87a5c0a8-df1f-3385-98a7-4d79b4898a66 | -7.18971 | -52.63024 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66383266-14c8-3c9f-b857-3ccddba61c7d | -1.63242 | -54.41387 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6dd60ea-4520-3d68-9818-9f08c583561f | -4.14247 | -54.03493 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22aa5ee-d99e-335e-b8e5-48c19f5bb0c1 | -3.2435 | -54.02633 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8367253f-0721-3a99-90a5-bb368f0ef6c5 | -7.03096 | -47.65814 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a43c79e8-5e95-38e1-8ffc-e3f4054e9159 | -6.93819 | -59.25488 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 71245d3d-90c6-301b-ae2f-548283af018b | -3.03185 | -59.15718 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5eebc8e9-e526-3109-8e11-7ee38d3cec03 | -6.42008 | -55.20449 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffbeb161-400b-3973-83d6-ca6f70cbe5e9 | -3.99112 | -59.3606 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fa507aa-5586-3ed4-bb9d-b4300953556e | -5.69222 | -53.47238 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58cd9ef8-fe61-3265-b9a3-134db309b5aa | -7.09989 | -55.73359 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74e53a22-62c5-3235-92be-ce74607a12e1 | -3.21255 | -53.96498 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bffab88f-c28b-3f24-a1e2-d831b80d3b27 | -3.38367 | -44.48034 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 919cd649-ae96-3420-8b56-673c286af961 | -3.01835 | -54.22468 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fefda2da-d952-3610-9255-f44f43a7ac99 | -3.563 | -54.68867 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba1b9661-0330-3c3f-bc35-c4f5f57684a9 | -3.02044 | -54.12577 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 151ecff4-6a56-3f81-8af8-463ba5428c30 | -3.0741 | -50.96713 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d36ae93-1f82-3724-9015-90fb082ad12d | -3.25314 | -54.67253 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30400b10-4e5b-317f-80d3-38bd6db5dc93 | -3.04277 | -54.26382 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f33aaed5-de01-369b-af58-a51f820ad156 | -5.38323 | -56.04864 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5db0fd0f-84b7-3d2a-93a3-081f43e06e40 | -6.12353 | -55.69803 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30d35dfc-e604-3a15-a77b-d264e1065b25 | -6.55579 | -61.41821 | 2026-10-10 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9529d60b-6d75-3d84-9973-61fe2358a4aa | -3.54128 | -54.73918 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3387618-2323-3793-8267-ac9fb6216116 | -5.99335 | -55.36712 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 347cbaf2-28d0-31b5-b43c-50f8ed5f8366 | -2.43234 | -55.98784 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f2c0242-095b-3a4b-9efe-da9e247045d0 | -3.10544 | -53.93398 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 188e82eb-a6c6-33bd-8e9f-5223ac411137 | -7.52866 | -45.31896 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7cda18a3-ec91-3a58-9a96-63b9189d8eec | -2.87754 | -54.19183 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a96b920-deb5-37f5-8682-3ebc4bb9fe2c | -2.95806 | -54.13368 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e191776e-4deb-3ee0-bd3d-229ae5ffb352 | -4.3815 | -55.16174 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59c7febf-c682-3250-8ced-4b3e92333f17 | -2.96361 | -54.18417 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46701bea-7c5d-3bfb-8953-df8272809d0d | -6.94394 | -59.10085 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8358f66c-4878-38f6-9d80-8f93c89d34b4 | -3.60244 | -54.59094 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 631ebbd0-6e24-325f-9a49-738a89fad1d8 | -3.01526 | -53.96591 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07922958-9250-34d5-be67-27170532eb31 | -6.43784 | -60.03563 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a25bf0-be37-30a9-b9ba-b5d98631548a | -3.25984 | -54.2664 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feb1bc3e-4788-3ceb-903d-ac83cd9c0e35 | -3.74337 | -55.94952 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f84f1c5-718a-3def-931f-ba2e796be39f | -3.85429 | -55.95847 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a120c9a0-f870-3977-8c46-2c393d82ff92 | -0.88152 | -48.71605 | 2026-10-10 05:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c32b73fa-e420-38f2-8316-214a116c127a | -3.10961 | -53.77961 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e575e93c-c831-36ed-acdc-2d0b0c74221d | -2.97461 | -54.11503 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91eab717-c914-3f77-9138-676124209ea0 | -1.62851 | -54.43848 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3c724bb-3063-3a23-9a29-daa553b0e65c | -1.33487 | -56.39627 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd765f13-c29c-3685-8229-f77e7a65ac4f | -3.80166 | -49.93603 | 2026-10-10 05:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 06f15e66-6245-3e70-9a60-50a3d7d34e35 | -1.95358 | -54.40302 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 922cc73e-768f-3aa4-874f-93dc67caa11c | -1.60812 | -55.16186 | 2026-10-10 05:04:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fab23546-5aa2-37ce-8f08-9ff9cda4b513 | -2.88122 | -56.66134 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5f06cfb-7bb5-3b72-9cf4-034cd761ba25 | -2.49389 | -56.18998 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0ff1aaf5-c624-36e8-a74a-26d0c7a304d7 | -3.81315 | -59.33298 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23533f7f-b0cb-33d8-a412-8f251758cd33 | -4.19738 | -49.90205 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4c483c0-0cb6-347a-8f4c-e1ddb0cc9c8c | -4.58636 | -55.7263 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2596aa10-d3bd-3477-b138-f4d8e3982679 | -5.10594 | -46.22885 | 2026-10-10 05:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9e63189-906b-35cf-8971-aec37b1e2746 | -3.32051 | -50.18319 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fde5278-4155-343d-b275-8ddf7f6e8052 | -3.9828 | -59.35921 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ad681a2-dd41-3e53-bbb4-f60061fa2b23 | -1.48085 | -54.64047 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adc07eac-e668-3a51-a94b-57c222c4a34a | -6.50625 | -55.4093 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50a069e0-c81f-3be0-90c8-e1f2df559748 | -1.42468 | -55.34673 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 457169d6-d886-389c-b8be-3b153d0f2b7c | -2.92056 | -54.13478 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f73a86d-2bfe-34a8-bf43-727a63e54947 | -7.03876 | -47.66851 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c9c951b-2028-348b-ba07-83c2f07f431d | -2.8438 | -54.12625 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dc5106f-b3b2-3ac8-ae11-938e4ff4a5c0 | -2.49308 | -58.08025 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b588818-2f18-3ee8-8b37-5410147cf560 | -5.33308 | -50.95478 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e8fe611-cc6c-306f-9f15-1e4f433b9b2a | -6.44439 | -55.28749 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b55b73f6-9338-36ef-96c9-6969a5b15d24 | -4.19913 | -59.41386 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54dca24b-197d-3946-a233-84f4b21e33f6 | -6.42998 | -55.27077 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de93dab7-ebd4-35f9-a1b6-f08e2b12fa3e | -6.20849 | -45.43066 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf6b59f9-b9b0-3e13-b5dc-53aa8a454b43 | -2.50773 | -56.12409 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0826230f-2771-3063-ac40-f4b343368e2f | -0.98009 | -52.44249 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c29710f3-b877-3a5d-9af4-650de896d8ee | -2.75425 | -54.11179 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e0f0e1-b00a-3b8a-bb0d-11d45c989ced | -7.025 | -47.66714 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e418b363-6a5f-341f-a69a-6f89f9c98433 | -6.13865 | -59.93119 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README101.md)
