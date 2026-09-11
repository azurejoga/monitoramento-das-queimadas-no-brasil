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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db3cc9c0-2c47-30d8-8f13-c33367c8b9be | -4.82339 | -42.88187 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 101b9cef-9e83-37ee-849c-2f3a047f5460 | -2.55042 | -56.28616 | 2026-09-11 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d52d3d36-a53b-3520-b367-a36b44a219af | -7.33229 | -49.25047 | 2026-09-11 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd058e00-b474-36ce-a54f-18c82db7fcc6 | -7.81033 | -42.77718 | 2026-09-11 04:51:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2c4a3fc0-ccbc-3d94-aaa4-599f6e5272ba | -4.86756 | -56.01219 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42ab4be8-2a31-3c50-ad35-95f1a621bca8 | -10.27876 | -45.27241 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20b69a2e-9e2b-3859-bd5b-ef3c0687fa66 | -6.02117 | -51.33266 | 2026-09-11 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 461aa38b-e741-398f-8cc8-07260282229e | -3.39824 | -54.07719 | 2026-09-11 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbd44357-0bac-3864-a138-c516977d62f7 | -3.06291 | -51.24802 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bef2d06-a58f-318e-84de-70e868e09e14 | -9.74814 | -41.96822 | 2026-09-11 04:51:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| cd5f637c-6975-32f6-a893-2344a37c589c | -9.63723 | -47.68781 | 2026-09-11 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f29ac847-e590-3598-8eb1-1d618114b09e | -2.72229 | -57.62303 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e586504-79a2-3c36-ad6d-17ede9892ca4 | -3.36981 | -50.75875 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fe9b5e9-f24a-35e3-b555-c6e276c312e3 | -2.73533 | -49.46055 | 2026-09-11 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dd94702-6cb2-38b9-b93c-ed8ceb863b61 | -3.76062 | -49.36631 | 2026-09-11 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc5cb56-4792-396f-ad5c-707ac22e81b0 | -4.77427 | -46.49859 | 2026-09-11 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 276f85b2-68a7-3bb8-8b5d-cbaa4f0430aa | -4.30943 | -48.07117 | 2026-09-11 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0b7d33d-d158-31da-bd71-d1a314282f04 | -6.85547 | -55.75681 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96b9da74-0dba-38b0-bdff-8342bbf8a5b8 | -2.93452 | -50.46893 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11b44d9a-d55a-3d8e-97e9-6d329749bf33 | -6.20648 | -55.27823 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d673ec90-8aa3-36f6-874c-c2148fb790ba | -6.19948 | -55.27713 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 823a3d3b-9cca-376b-99b8-697cb9187350 | -8.10318 | -55.62221 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6261bf0c-7657-3ced-9a09-57063c47bfc0 | -2.72058 | -57.60694 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47232808-2cb9-3478-8cbc-7cfb22d166a5 | -6.92398 | -55.64739 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d701de7-ccee-3270-aa27-bd6a92008e95 | -9.37251 | -49.38116 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f5b6b72-a60c-3ac2-accc-79ae97c8d80e | -3.37372 | -50.75571 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 095a008e-ba73-3d2e-a4c7-ecccf4b40a21 | -4.8639 | -56.01139 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ce5c716-65a6-3303-ac56-9ebcd1f82bd7 | -3.06991 | -49.52149 | 2026-09-11 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7df03b0b-c05d-3609-a44d-636b16d6b68a | -3.51754 | -43.25549 | 2026-09-11 04:51:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2023038-d6d7-38ab-a6e6-a013cdc95711 | -1.69871 | -55.02713 | 2026-09-11 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e47f49d-4d69-38be-a1b2-35e7073482ba | -4.53996 | -54.92952 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5000db6-0bdc-3eaa-85ab-bed133da09b4 | -7.10163 | -42.12939 | 2026-09-11 04:51:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 28d30816-ba46-315d-bee3-5cc2bb8750e4 | -3.25191 | -50.81736 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf33cd3d-9ce4-3148-b8c8-990923dbd1d2 | -3.37708 | -50.75623 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54460d06-c3a2-3408-a15f-05982e7503d1 | -6.19433 | -55.26436 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f966f45d-6f38-30c1-86b6-71d7582c29f6 | -5.96365 | -47.18021 | 2026-09-11 04:51:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f21ba2-c664-3829-8682-a3c314411b23 | -3.39765 | -54.0809 | 2026-09-11 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9970b4d-06b9-3e7b-8810-3a427903f533 | -4.36138 | -54.77511 | 2026-09-11 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 831da856-db3c-369f-882e-7f044fc4fed8 | -9.63013 | -49.01696 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20599c0e-0082-386d-86da-8d9b3cd785dd | -6.24345 | -51.67574 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29e253ff-5220-3315-bbe6-5f49a7a8e827 | -8.00987 | -43.87034 | 2026-09-11 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aab00ebb-918c-3db8-b8d4-2086357a48a3 | -4.46961 | -55.43279 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 286198fa-8ab6-315a-94b8-a65774abd379 | -4.53553 | -54.957 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a8d61d02-e246-3847-b35d-7b594be3aa09 | -2.94299 | -50.48125 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4b787d8-7227-3aaf-b22f-909988f781ad | -3.15115 | -60.65049 | 2026-09-11 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6c32ec0-bde6-32f0-8c81-679aab29bf38 | -9.36941 | -49.37591 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e46cca6-9729-35ae-b4d2-a88cf23965cf | -4.82888 | -42.88264 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a1a2a173-84a9-31b6-8e4c-ae8ddb548487 | -10.05835 | -46.27332 | 2026-09-11 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 587825fa-33f3-3938-bd5d-cfdd101166e8 | -7.02491 | -45.11185 | 2026-09-11 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 920b2f77-14ad-3d84-ae96-f0cef407df08 | -10.27962 | -45.27232 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16b3ad78-562e-34ce-ad07-e45cc0763281 | -8.73311 | -50.5992 | 2026-09-11 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 690014b1-a1e2-32c8-ae4a-202f1d2cdce0 | -4.36487 | -47.77813 | 2026-09-11 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 0297e0fb-2615-323f-8190-04b66361d399 | -8.50337 | -50.15216 | 2026-09-11 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4b7323d-f33e-3760-9989-710b480bb97d | -6.0973 | -47.38153 | 2026-09-11 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d79539b-3313-379d-bf74-1e6fa2bf1a43 | -6.12955 | -43.74881 | 2026-09-11 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00813e66-3e28-391c-9c55-3cea8697790c | -2.69167 | -57.51169 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9b4e590-0959-3c25-a3bc-4a07395f251f | -4.52437 | -54.95923 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89292b1e-d999-3d71-9d18-3d39b10f3a9d | -3.09404 | -51.28841 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27ce3fe9-e78c-3efd-a7f8-f37982c94230 | -10.22042 | -45.21373 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ecf60ea-e217-324a-b634-6a4fb895bc80 | -9.31424 | -44.35763 | 2026-09-11 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd9442d5-ac71-3ff9-a58b-f33601721b2a | -3.37091 | -50.75163 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4618f61-b70a-36d4-a35b-3a113e566d24 | -7.80934 | -42.7777 | 2026-09-11 04:51:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3d4e2cd7-1c2f-3b5f-81c1-0fb3d1ec798b | -8.82131 | -46.91182 | 2026-09-11 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18ebe9b4-ffa6-39cb-8b0a-2f19c2d33894 | -2.93734 | -50.47304 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec49c966-f666-3ac6-ad87-338cbf9d7b6f | -3.76121 | -49.36237 | 2026-09-11 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bf92609-91f4-3edc-934d-d0d7a1268a0d | -7.0083 | -43.86694 | 2026-09-11 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6047be53-70cd-313d-adb9-da0d7740b38a | -7.92962 | -49.73449 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edc9fce5-6914-3f85-8610-2c9760f05f1f | -3.5532 | -48.18244 | 2026-09-11 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 279e67da-e86b-3c06-bab0-08b935d6a70f | -3.26303 | -50.08509 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d660c13-aa51-35c7-81bc-18a9b66808c8 | -2.69245 | -57.51608 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a5d395b-300f-370f-b64a-6768bc505079 | -2.72649 | -57.62369 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51449cf2-5208-3bf7-a0ea-e32476edf626 | -2.56008 | -58.06594 | 2026-09-11 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4587340b-3e6a-3e4b-a3eb-679a2e0329f2 | -5.28254 | -56.04293 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af1053f4-3ba4-3a0f-8eb6-ffb667beb607 | -7.91027 | -56.63396 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25ede03b-f482-316e-8265-1bb0212890a5 | -2.94237 | -50.46277 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2b1f9f9-2a12-30fe-88d4-cca0aa1754f7 | -7.94328 | -49.33799 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 664ef6b3-cf58-3d89-b71d-e3c1f4d3ae4a | -9.32589 | -45.64533 | 2026-09-11 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7182a14-eb9b-3ca5-83b7-7c1ad12d1181 | -4.82418 | -42.88063 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 464ba660-e2df-3318-b590-32205185cc20 | -3.38043 | -50.75674 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bf48144-d6a2-3b07-88eb-0e3c1a535709 | -5.82618 | -53.80416 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a47d7718-e1a9-38b9-b518-eeb265b19864 | -3.41166 | -48.89603 | 2026-09-11 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 425a8cc3-a961-37a8-924a-3c539c5ab75e | -8.49059 | -44.74867 | 2026-09-11 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66fc9253-aa63-31d9-9148-e202137ff14b | -3.20316 | -51.19836 | 2026-09-11 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d18bcefb-94b1-3d1b-9202-7442acb4f65f | -4.29615 | -49.10856 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83192c7e-0226-3978-98fa-609262c6322b | -4.86522 | -56.00317 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c71e3f0b-aa3f-31eb-9ed7-595780bee201 | -8.71242 | -49.61907 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b0cb2632-6402-3a3a-9ecf-fca71a102462 | -3.3743 | -50.40638 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38faabd2-ba73-371a-a77f-4e4586429978 | -9.27602 | -47.79886 | 2026-09-11 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d8b367d-8510-324e-bbee-c0858f152e27 | -4.2421 | -49.94064 | 2026-09-11 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdb422db-368e-3755-9d1b-2503688c69a9 | -3.13374 | -60.66024 | 2026-09-11 04:51:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb1b9963-d2ca-3c31-b264-80795c915177 | -6.19783 | -55.26493 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83e91b8e-c35a-3a9f-9f04-cbe401cb8a59 | -9.70205 | -43.4011 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b247a71-0b77-34eb-8058-99bbdc8b4259 | -4.53903 | -54.95756 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0bf581e8-2c21-3bbd-bf1a-5d6ecc6ffb7e | -6.24237 | -51.6828 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abb30468-5524-3bd2-a71d-d20a2d13ff67 | -8.1853 | -49.03162 | 2026-09-11 04:51:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8433aca9-2abc-3c5e-bf3d-76de4bd6ede4 | -6.83892 | -51.49354 | 2026-09-11 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddbcef50-8305-33be-b996-08f031774e74 | -6.19721 | -55.26881 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b11d580a-e7d6-374a-9cc5-18ae348059ae | -2.93507 | -50.46533 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b5fb723-0a8c-3395-86e3-53c0483cbaf9 | -8.70604 | -49.62046 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2f5c928-6bb5-38bb-9256-bc4f1375fb6e | -6.09557 | -56.46739 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
