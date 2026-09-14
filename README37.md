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
| 5e01199e-358e-33ce-a39c-c02edbd7efeb | -2.70525 | -57.54528 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 448454f9-dc71-3649-b223-5854249322d7 | -2.94459 | -50.39747 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f911546-2d81-3d09-9bf5-337507037569 | -2.89013 | -50.44178 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7216d738-85be-3a93-8a10-ab6b60c0e957 | -2.9044 | -50.41583 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6418503c-2bf1-3b0e-a98f-0df3bb444c36 | -2.9512 | -50.3985 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acf9dc20-f79c-3cc4-95fa-3eed963af071 | -2.91432 | -50.41739 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0773fef0-d637-3f66-927c-dbe68fa567ae | -2.91328 | -50.4454 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfa93864-6278-3d69-8b4a-6d2a147475bd | -2.8846 | -50.43387 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 167d4978-e942-3b41-b77b-9f3003616fa2 | -2.89942 | -50.40448 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ed61c14-28fd-3ff9-bdb7-f199ce2e30a6 | -2.89892 | -50.42906 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| f0ffc163-2e6d-3267-9dad-c6d5ce3c39b6 | -2.92311 | -50.40467 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 770bde8e-3570-377c-954e-c4ec44095d72 | -2.96058 | -50.40349 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07f5da2d-2974-3e3b-8b71-8e6f4bccab7d | -2.91102 | -50.41687 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 7cc66311-20d8-3578-86d8-bcaf750c4c17 | -2.89565 | -50.44969 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a85a1859-bfde-38fd-8976-7cc33ae7f7b2 | -3.33595 | -54.18951 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 10bde33c-fd49-3b02-8f7f-896fde4c90a0 | -2.88958 | -50.44522 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbb2943f-4292-3d27-b8c7-37252ab07a5e | -2.95781 | -50.39954 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efe79d23-3a0f-335c-b134-e8ba4c20da47 | -2.92533 | -50.41207 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ff477293-5498-3cce-a49a-ced0a052dbd7 | -3.78958 | -48.92935 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a624c5d-776b-34f9-a0da-a24c808e3015 | -2.95618 | -50.40985 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f30f70fb-d4bb-3074-bdbb-052324867602 | -3.1667 | -58.64816 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2b3f0d1-4a90-3c5b-a187-e8569ae93634 | -2.91491 | -50.43509 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| dffcd29e-5ca4-322e-90bb-2f5873d19e62 | 2.58217 | -60.30619 | 2026-09-14 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c8c7c24-c55b-3c4b-abac-e4c7a94d810e | -2.6739 | -57.57433 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 229d6a26-1244-3fdb-a198-8645bf615b4c | -2.87712 | -50.41467 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5063a0af-6b8a-3a34-a14c-5d18a64385b0 | -3.60803 | -53.84638 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de681b8d-3378-36a0-9e89-01b9faca7b65 | -1.8596 | -47.9809 | 2026-09-14 04:51:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8427f33f-8c02-3077-b582-047b1ef8210c | -1.71913 | -54.95162 | 2026-09-14 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 829d8772-0a69-366b-96f6-a7afbb6ec7c0 | -2.90051 | -50.39761 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 387e35c2-a340-3ee1-bba7-37aa92c203c5 | -3.75165 | -53.42383 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97d0c3ba-ae95-3d25-8ff2-00aa54d0cef1 | -2.92977 | -50.42685 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd1d20ce-c7ea-396e-be2f-95b726d4a37b | -2.90336 | -50.44385 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba2a23e2-c7a9-3bb0-86fb-53a58e751f14 | -2.90227 | -50.45072 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2465d45-ed76-3e02-8110-f5b4cd30198c | -2.92207 | -50.43269 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b58a096-7a83-3f9f-9e2b-4f825f5c12dc | -3.16176 | -58.64625 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 627279d9-56a8-3a35-9e8b-03eb61c93125 | -3.38879 | -50.76715 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6043c548-c6ad-305d-8691-06d3a5132ad3 | -2.87381 | -50.41415 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f9346d-2b72-3f24-bc3a-e0249796d409 | -4.85758 | -48.36112 | 2026-09-14 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2627e59a-837c-3e2b-bc00-5775065eeab3 | -2.88239 | -50.42648 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acfa0f85-5b37-371e-a13e-23faa1d90f74 | -3.22655 | -50.59017 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d531cce9-6938-3edf-9a60-462e9248a62f | -2.88569 | -50.42699 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d7fd578e-1a0a-3da5-96c8-55672f1835f3 | -2.91273 | -50.44884 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e488d4e1-ab92-3b5f-9493-19aefc3b396e | -2.61464 | -54.72878 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb0f627-81dc-3bdb-a447-c40b6158e941 | -2.9314 | -50.41653 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c91bbbf3-e9a9-32ef-9926-290f173acb4a | -3.86533 | -51.97626 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c084234b-2eb1-3e61-a327-2814feb8e6f3 | -3.38411 | -50.38914 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d90b8f9-9214-3156-901c-a4ac3918754c | -3.79274 | -44.11452 | 2026-09-14 04:51:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22019005-2964-390f-9e47-c52ab8ac480d | -2.88628 | -50.4447 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45419838-581e-350d-8290-eeebd6b5badf | -2.70443 | -57.55014 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba943deb-6b4d-3e99-8aed-ab56630ecc69 | -2.93136 | -50.3954 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707a855d-87f4-384f-b2ba-f03725cefd0d | -2.61084 | -54.75273 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| c6170dbf-935d-33fb-a22c-85335f9279b1 | -2.93416 | -50.42049 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da096ce5-34a7-33f8-affc-00a060e77a09 | -2.93086 | -50.41998 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6448a2a-82c3-3014-aa2c-3454c8b1f6d0 | -2.9396 | -50.38612 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04dde86b-e08c-3592-8eb9-41caf5d951a4 | -2.90503 | -50.45468 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bace02db-e964-36a3-a2de-ec41affefef3 | -2.94023 | -50.42497 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b086d585-de70-346f-8ba3-31d6394b5d92 | -2.9039 | -50.44041 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af414a4f-ab09-3657-aa75-c00e89842fde | -2.87494 | -50.42843 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 249f2bbf-8462-3097-85a7-b64a25bd1eb7 | -4.75824 | -42.78808 | 2026-09-14 04:51:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57e6f51e-0feb-30d2-901d-1348a71b88d4 | -3.77481 | -51.35245 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c20326fe-b0bf-316a-b664-4e1f22eccd01 | -4.45322 | -50.15748 | 2026-09-14 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98bf885d-c525-3e9c-91e2-0d88a162e10b | -3.55021 | -48.17807 | 2026-09-14 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a79c921-ea7c-3346-87fd-3483b0d5d587 | -2.90666 | -50.44437 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 949b8362-f0af-3409-bd0e-b70c5f6f4a3c | -2.93245 | -50.38852 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2b64e27-7f66-35ea-a947-833dad042882 | -2.88293 | -50.42304 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3d595a1-825d-3197-aa2a-9baf405e0001 | -2.90612 | -50.4478 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2413060e-388e-35b3-b7ac-cdfae8a8e50a | -2.93693 | -50.42445 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6e656b4-950c-3b4b-9d49-b2bc98a202f1 | -2.889 | -50.42751 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4045cf37-c848-3703-95fb-6422d17296ba | -2.92094 | -50.41842 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8148cbfd-e89c-3da6-9518-08fed026af50 | -2.93852 | -50.39299 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d9bc280-ac12-34d7-a589-34852082b457 | -2.67161 | -57.55888 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3087f7eb-ee9f-3a4b-b39e-a12bb5ed057b | -3.36109 | -50.74862 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89ec5052-501e-31e9-959d-ca8bb75a5c5f | -2.88573 | -50.44813 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 549ea3f5-e8fd-3549-9cd1-3459fc327341 | -2.88678 | -50.42012 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cfacb6b1-67ba-3209-b645-173b3b76ec7c | -2.88954 | -50.42407 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 43bda335-f306-36d5-917d-7107dad1357e | -3.45829 | -47.46334 | 2026-09-14 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 572f4469-a8b0-34e9-bc60-5810efab4d31 | -2.78046 | -51.36738 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6faac062-f194-3b7d-b752-2de5f281ffbf | -3.04801 | -51.26664 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45e88755-e29f-3a89-9451-1bdd00c7eb26 | -2.69101 | -57.5729 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53ff0155-0951-3ed1-bc8f-5551b2a5a0fe | -2.94572 | -50.41174 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53a6ca68-8e26-3223-8046-c3ebce52e4b5 | -2.89394 | -50.41771 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 03db8d26-7ba5-3f71-ac8c-256c1855216e | -3.338 | -53.2713 | 2026-09-14 04:51:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7e29371-ae82-3d06-a3f1-f727bad1ec5e | -2.93797 | -50.39643 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae278093-8762-3241-bf99-54fcece0865f | -2.92805 | -50.39488 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00247168-1443-39b6-bbfd-fefcc1e5c60b | -3.3921 | -50.76767 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f545ecb-e768-3e25-80dd-f6252376f01e | -2.90938 | -50.42718 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9db7b895-364c-3ef3-b63e-40f2278828a5 | -3.79798 | -52.4175 | 2026-09-14 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3638be7f-c5fb-33bd-8d96-f3f6fb04aeb3 | -4.59286 | -47.17721 | 2026-09-14 04:51:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87850640-2b62-3a35-85fd-0a864ff70874 | -3.38493 | -50.77007 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a1fbabd-cb21-3a0f-aa1e-72889816904e | -2.88347 | -50.4196 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd08d43a-546f-3afc-b347-7837d9710454 | 2.58824 | -60.3052 | 2026-09-14 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2838a47-fee5-3f5b-90fa-a727a1f13fe8 | -2.91382 | -50.44197 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34490510-2b39-3a61-9445-06a7cb0a4045 | -4.55206 | -50.45678 | 2026-09-14 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 096fe4a3-9363-3eb8-9570-5678102e6c41 | -2.91487 | -50.41395 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ed80f233-1d1f-3416-8157-956a855f2c09 | -2.90005 | -50.44333 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ba85b00-26aa-31e9-b15f-a64488aae1a9 | -2.48894 | -49.10926 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 661bd17b-b466-3201-9262-dacb9613f549 | -2.93906 | -50.38956 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c14f5094-a17a-356a-94e1-0f650534c618 | -2.93194 | -50.4131 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9ce94e7-9471-3d9a-ab02-ac56b7903319 | -2.8962 | -50.44625 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d6be9bb-df9e-3be4-a000-f38a4d3266c3 | -2.91047 | -50.42031 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |


[Clique aqui para ver as próximas entradas](README38.md)
