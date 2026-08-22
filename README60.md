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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f66571b-aea5-38d8-9de0-1c3d0f4040e6 | -5.74973 | -53.58279 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c91fb00f-0eb0-3d49-a96b-6873afea01c0 | -13.94936 | -53.8484 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5e8056d-1cdd-360c-bada-54ba2bc970d2 | -14.06749 | -58.8149 | 2026-08-22 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 393da319-2ac7-3720-8ef9-3f85580c5328 | -6.1249 | -59.90995 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f745bfea-4448-3f57-b851-1f1ec992deb6 | -6.82184 | -59.41579 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e30e0462-ae86-35b0-ae2e-7e132946980a | -6.36485 | -62.90194 | 2026-08-22 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2227e683-1617-365c-95f1-12a9178a635d | -6.78098 | -58.66344 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0137b032-5814-32f0-aec9-11d27be1d642 | -6.9777 | -59.59001 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 769424fd-8ecf-3cae-9b09-fe3bd9f1b5c8 | -6.75666 | -58.66676 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9ae61180-835e-3fb4-a186-46c26a500bb5 | -6.93596 | -59.31693 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e56e447-6c8c-3f5f-8a5e-09a34f1d8a48 | -6.76838 | -59.45342 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed970cfb-8eb7-3a92-a7b3-2a3013027207 | -10.83561 | -57.51751 | 2026-08-22 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19712dc9-41c3-3466-bd14-f86525b28bea | -7.45675 | -59.99439 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68880e3d-e8a9-3008-9b19-cc3943ddd40c | -8.0245 | -54.02399 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5e63eb4-0123-326f-a6ab-9115cf80c7fc | -6.3745 | -54.94964 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7af3759b-9167-3376-afb8-802b99c15579 | -8.6254 | -54.68561 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 827db5c2-b186-3812-a613-66c90cc1f21c | -6.88368 | -59.41148 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c6668cb-0423-3d41-9f4d-75372cb58aa1 | -8.63939 | -54.70215 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b9159cc-a5d7-3793-add7-cc1a42662eb8 | -3.03646 | -48.41218 | 2026-08-22 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 805ee04e-a9b6-3e6c-9838-49dac3682a96 | -6.80352 | -59.01538 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6f3e038-b68f-3c3b-9349-2593b734537d | -7.36555 | -55.69151 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c98a3add-6cad-35b8-92a3-832ab5f63fab | -6.87873 | -59.44262 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28f75d4b-8bf6-38f9-93e6-0d47eb59ce2a | -6.8881 | -59.42638 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8fa8e5-3a45-3d05-b70a-7c25c0d2aeed | -3.42451 | -49.47889 | 2026-08-22 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc16bb2-bef3-3658-9f8b-b61ee20230e3 | -8.02624 | -51.80138 | 2026-08-22 05:23:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8197b48a-3e94-30ec-b0f7-efc788fd3351 | -6.75331 | -59.46126 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08a57678-9763-33d8-8f15-bd20a32fd6be | -6.76507 | -59.77277 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6445bd6d-51f4-3013-a49e-3fc369a1cdda | -6.66939 | -56.3429 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1454010e-b124-31e1-b4dd-2e13e6a493f4 | -7.68683 | -46.17272 | 2026-08-22 05:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4dc18dd4-6330-3d99-8697-3fe63cd6a7f7 | -11.17745 | -54.80235 | 2026-08-22 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 119270b7-510b-3053-99bc-fc1b8845617f | -6.79815 | -59.43687 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3e6241b-0215-3c61-9caa-7c7df51a56c6 | -12.76499 | -48.40057 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a72c9194-5b18-3752-80e2-57a8cb091120 | -8.52831 | -54.83321 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bf648094-a19e-3062-b9fa-d77de3d7a6c5 | -8.53625 | -54.83435 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8cfc7ea6-ac65-393b-809b-f858a4e239c7 | -6.80861 | -59.41368 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b250f8-d7d6-3f53-b1d3-59bd71d0d4f2 | -6.88055 | -56.63897 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77c762f1-629f-3705-8f34-cf795776e12c | -6.80114 | -58.6202 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d3c26ab-bd65-3dea-b8b7-d71931a3c462 | -14.3155 | -53.00238 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f221bf58-9048-34e2-94d8-1d108e261fe9 | -7.61056 | -60.9768 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81ab83a6-cc6c-302e-bb65-a8b578b8a621 | -6.71188 | -58.99382 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f85a74ab-3de0-3a3c-9fe3-aba88e7ff16e | -13.9928 | -53.69686 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5d5ece0-2acd-375c-a027-81cf1730c953 | -6.75557 | -58.67371 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20165135-45ce-3a10-901a-675e8228e4e7 | -6.13156 | -59.91102 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fe50720-1cd0-3885-8938-4e2f3d6937ec | -5.796 | -57.55547 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60f5d613-0927-31c0-b82a-bd7eb3cd7eae | -6.88921 | -59.44074 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6d531fb-a281-314a-9280-30309f797525 | -8.17387 | -54.98324 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 661db34a-0826-36e9-ba40-9709ecf998f0 | -14.00977 | -53.70117 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3bca25c-3fa1-3714-8075-d73e0f94d67a | -6.3807 | -54.96019 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 490f0f46-fabf-39db-86cf-6e393dba0b8b | -8.03322 | -54.00618 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a836d6f9-66e1-3ea7-9449-c41b1bad40d2 | -8.5793 | -54.75045 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfd6d8a9-f881-3e16-98f1-1c67aedecfc7 | -8.57837 | -54.78556 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8d52f1c-57f3-3ca5-a629-4dd161ccb394 | -6.88975 | -59.02939 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b404757-a0f9-34c1-a098-b6c8fe86cf95 | -6.77048 | -58.66536 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e6bcb7f-1ede-3724-95f4-b18547409568 | -6.82237 | -59.39104 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 167cbc44-117e-3569-af53-0806b3c872d9 | -6.75225 | -58.67319 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b55b5e99-5c02-3b4f-95bb-91c5aa791521 | -6.77555 | -59.45102 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e599a49-297e-3b93-bac1-cd7062c823de | -2.4974 | -48.13398 | 2026-08-22 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9a02976-b117-3f51-93ed-28420cba69f8 | -12.00797 | -53.4231 | 2026-08-22 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9216c0ba-95ff-3ad8-aaa4-0853727d9fd3 | -8.99165 | -50.73661 | 2026-08-22 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3277bb2c-0682-3877-a50a-6ea40adce902 | -14.39107 | -51.797 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e61642fa-a720-3b19-9af1-96bc0e65fe5e | -6.79233 | -58.6331 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c09f8f2-cd7b-3ed7-b120-b5ed136cef83 | -8.60134 | -54.71057 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec9c5c49-fc7f-3786-a4ee-c0bca2341976 | -7.25356 | -49.91526 | 2026-08-22 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9024e2ca-1f28-39fe-94bd-1f16a4cabf2f | -3.54097 | -48.18563 | 2026-08-22 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 324557a4-49b9-3d1b-accd-55aff42fcfe4 | -6.9134 | -59.35235 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b3a627e-16a7-39bf-9408-b0a159e7de7a | -8.21963 | -55.02649 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d5b8b88-021e-382d-9296-3c8680cf5fb0 | -6.25637 | -55.39642 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e38bce49-4377-3ac1-8705-1d89175ee154 | -6.85051 | -58.97704 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8a2f126-4745-37c7-ad39-96993eec6408 | -6.69163 | -59.10054 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58758d7-12ec-3d0e-ac84-00d14d815742 | -12.77096 | -48.40552 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 554e8fe1-d795-30ed-9b65-a7c108df557e | -6.81137 | -59.41768 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46f5cce1-4d1b-3a28-a4e1-4d5ebef3864f | -3.07919 | -61.06046 | 2026-08-22 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e05c1df4-4ca4-3fb9-9bf1-a5a196c68953 | -11.82395 | -56.59243 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 825589c5-786a-3de4-b26a-5bd4e7232f45 | -6.78491 | -59.43476 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a26a541e-e844-3282-88bd-0f420a229067 | -6.88104 | -56.63808 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 444cff6b-e63a-392c-a8cc-45863f1a2183 | -6.78105 | -59.4164 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 973cf279-95d6-33b8-998a-745e2287d797 | -6.80902 | -59.00206 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0bb260f-3644-3313-acfa-fd4930ecbf66 | -6.8643 | -59.42607 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f51552c9-1987-3ebb-9034-df76962338c5 | -6.76719 | -58.68623 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14671561-5710-3071-9b83-90c2e6fd11be | -6.75057 | -58.66224 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 10a2ca79-93fa-3b25-8023-df350948a41d | -6.88203 | -59.42186 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a16ee128-7a69-3dcc-8422-d9ecdcb9e09b | -6.80089 | -59.41955 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 95b9b936-9a80-352b-96a5-b07724e7d36d | -6.80475 | -59.41662 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 615ed7ed-68d7-3b48-ae66-2dea7edc59c5 | -6.13046 | -59.89649 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29376f66-2806-37fa-845f-ff9f8d7086f9 | -6.55704 | -58.51077 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a154860-6c47-3618-bba6-b0d53bd3d4d1 | -6.75003 | -58.66571 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6cbc63d8-2368-321f-8cc0-50418d0508b2 | -6.81027 | -59.42459 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 02261603-b6c6-30b7-a1db-6455fbe4dcad | -6.1719 | -55.43988 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 884e75ef-c5f8-3bba-897c-55cebcbfc680 | -6.85826 | -59.46416 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad13390b-6254-3d9f-8494-fe2cc163272c | -14.54924 | -53.00222 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef1c151a-3dff-343f-b8eb-29dd48504ffa | -6.80586 | -59.43099 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b46134c3-2d52-3158-9f37-639d583c799b | -6.86704 | -59.40878 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97a3877a-0aa7-3322-9619-09e0913df668 | -7.59931 | -60.95255 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87cff569-d646-31d6-8e00-22947e728a48 | -11.21023 | -55.04523 | 2026-08-22 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 004a57e1-1f39-3932-b43f-d84a82d180a3 | -12.82302 | -48.4631 | 2026-08-22 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94395d18-9b5e-3cf9-9b17-fc5733a59038 | -8.51257 | -55.32576 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa7b2888-a603-3f52-bfe2-3736878175f5 | -6.79704 | -59.42249 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 28616744-1671-3528-830a-b0b188326b20 | -8.02333 | -54.01607 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4dffaff-bc35-303a-b066-33b6996735a0 | -4.96337 | -56.26471 | 2026-08-22 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 249ae0c1-0202-3f14-84d4-b0d0b65a362b | -7.02125 | -59.55082 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README61.md)
