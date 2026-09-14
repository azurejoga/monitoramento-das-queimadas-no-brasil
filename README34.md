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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be036c17-de15-3e8d-b116-1ceb866c81be | -1.46477 | -52.96259 | 2026-09-14 04:51:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dc950db-e7c2-3526-8fd9-6b34bb93c95b | -3.37777 | -50.77247 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3aa2190-24c7-30f4-aaf8-ecc716158b09 | -1.71692 | -54.94894 | 2026-09-14 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36e0b73f-1fb3-3449-813e-c8b312187808 | -2.90712 | -50.39865 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9ad977fd-9e9e-3d53-bae4-075008eebaae | -2.93307 | -50.42737 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60cf4db3-906a-3fa5-a548-8be8517547af | -2.91709 | -50.42134 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 939bd442-148e-3314-81d3-2ba8d00c32d6 | -2.90942 | -50.44832 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64678269-68f2-39f4-b67c-7b4b55285f03 | -2.916 | -50.42822 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7cefc3ac-5246-3054-8413-ef9adcdf36f2 | -3.1658 | -58.65291 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6aa656f8-d6e5-3e41-9f97-aaaa7aae3166 | -2.90604 | -50.40552 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c16103bb-b4d8-3262-9c59-48d778f196cc | -4.6259 | -47.20913 | 2026-09-14 04:51:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffed8432-3092-392d-9054-a67ef04d737f | -3.46126 | -47.46807 | 2026-09-14 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5affb635-dc09-3e8b-80d0-fc1985480246 | -5.28682 | -45.26749 | 2026-09-14 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2de5c90a-8c99-32bf-b8f4-ddee119e3d48 | -3.04468 | -51.26611 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 629129fd-916d-3d95-b2ef-c74633dd9dbe | -2.89452 | -50.43542 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a880def7-b2d4-31b0-8608-823d8a7df91b | -2.91541 | -50.41051 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 5d8eae0d-3705-3e21-8d7b-bfb046fa318e | -2.94957 | -50.40881 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95178927-7d84-3511-9e4d-ee6952271d6f | -2.95011 | -50.40538 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21ed1885-cdb6-3347-bbba-38ab95c83a5b | -2.70696 | -57.62086 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28b38bbf-d28f-3678-a93b-ae52210f5262 | -3.39264 | -50.76423 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebfb22b1-3fa8-3c51-a152-139799bc3ecc | -2.9718 | -51.19007 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 551e9b98-78f4-3d02-b540-265daeb23f91 | -3.21682 | -56.83768 | 2026-09-14 04:51:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55142252-b224-3cab-b9fd-1ccb397b1304 | -2.90721 | -50.44093 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfc44d02-591e-32d5-aa8a-caa950d2b038 | -2.96166 | -50.39662 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fc108f1-7722-3253-be35-0ec42cc7efab | -2.92483 | -50.43665 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef6ae637-4bc1-3eb0-87ba-42e1c41344e5 | -2.91545 | -50.43166 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| fa2fc455-6a71-3a2e-ad31-46520ff696ce | -2.9286 | -50.39144 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53c703b-ee8a-3052-bfe6-1b3034d30b0c | -1.22124 | -54.13326 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12e842d5-8e23-306e-a761-369d9c57a529 | -2.88904 | -50.44865 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb85ae20-a296-396a-8907-28ddc70ba974 | -1.19674 | -54.11887 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2383056a-67c2-3354-a1ec-296c30df8b47 | -2.91043 | -50.39916 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2422dcf1-4c65-3fbe-a4a6-c7de804b1f40 | -2.90055 | -50.41875 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0dd695ad-a9dc-3cc3-9eb3-c8ea3262f26b | -2.91374 | -50.39968 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 057bad36-bada-3a73-80f7-4a10574e2771 | -2.94517 | -50.41517 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b69c60e-e1f4-3b52-9cd1-832007a6b33a | -2.92864 | -50.41258 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 924ac336-8767-3561-a035-af79b4148161 | -2.91926 | -50.40759 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8de63a6f-3bcd-339d-aad6-862967607fd7 | -2.96404 | -49.56417 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a992f45-efd9-3bde-97ff-f426e309e849 | -2.9083 | -50.43406 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5d69da4c-0187-3fc6-aa37-92f3572b9670 | -2.92696 | -50.40175 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4d4e3c00-b22e-38fc-b22e-e0f353d6f9d0 | -3.05079 | -51.27065 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb36cf8e-ba6a-3d01-98f2-730a0fff7f84 | -3.2413 | -43.02557 | 2026-09-14 04:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d29e7246-81b3-3083-8526-45928a8119e6 | -2.96792 | -49.56119 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb212dfe-bfd9-30b7-8188-efd2a78b80ad | -3.53351 | -55.53203 | 2026-09-14 04:51:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f032620-77b3-3884-8289-045a533ee9bb | -2.92039 | -50.42186 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea6835ef-5f5c-3d8c-be01-6cf6c4978852 | -3.23316 | -50.59121 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 587408eb-0817-335f-9375-b91c18423955 | -2.8995 | -50.44677 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 820a3839-55ac-3ea2-87bc-1c4b4985112f | -1.6834 | -50.01585 | 2026-09-14 04:51:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb851c86-ac82-324b-be72-7eb1c18a9dbd | -2.90993 | -50.42374 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| eb0b4f1f-39ae-38c7-b14c-f41a06d3948b | -3.04579 | -51.25914 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eb17cc8-5c36-301e-bb28-c0696e5706fb | -3.40593 | -48.8936 | 2026-09-14 04:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac9f8292-6dd3-3fd4-977a-d880b6838064 | -1.22268 | -54.12434 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94404df4-244b-351e-913a-06a6a9638346 | -2.96606 | -50.39026 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f6957b5-eac7-3d25-9cd6-cec281063534 | -2.69806 | -57.54329 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 36c87dfb-7293-350d-9aa5-bd26620c4937 | -3.88117 | -51.92033 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 176e0e9a-e98a-34fb-a76c-bfa352f295fe | -3.92714 | -52.24757 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4d53691-796f-34ed-85f2-7cddb3c89a67 | -2.88406 | -50.43731 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3997e358-2368-3763-8346-f623c4e9796e | -2.93358 | -50.40279 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3b25927-b77c-37f2-8320-2055f30f31f1 | -2.92588 | -50.40863 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ab135478-0004-32e5-93a2-189b55d8923b | -2.95174 | -50.39507 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8e43113-dbc7-322a-ab9e-9c868e8322fa | -3.86476 | -51.97983 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7dd66b03-f4b4-316b-adb7-47e056145667 | -3.15976 | -48.60843 | 2026-09-14 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d81a259-404a-395b-87a8-22595c0bcdbe | -2.89067 | -50.43834 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b15fc4b0-9c76-3785-b730-c0b6f5f5da8d | -2.93199 | -50.43424 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b499b9f8-1750-38fa-8ef7-c13954d7fefe | -2.92315 | -50.42582 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d45a0e78-16ec-3aa6-88ab-b3ad7a7a26e9 | -2.91269 | -50.4277 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 47211e28-402f-3281-b295-7ce97b469dad | -4.55151 | -50.46023 | 2026-09-14 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ac96fb4d-3305-32a9-8fbe-84441304873f | -1.196 | -54.12077 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 468902ee-81de-35df-a809-0a62dc742f95 | -4.81043 | -42.88819 | 2026-09-14 04:51:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d32c9d1b-4015-341e-8679-6e3a74dd6609 | -2.8918 | -50.4526 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b3f86b3-bd4b-3341-b80a-ce695f155202 | -2.91872 | -50.41103 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e4c61075-8253-3d1f-8ecb-6e7460d3b00f | -2.93521 | -50.39248 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fcafef0-4edd-32a8-919a-c545a5f4b727 | -2.90767 | -50.39521 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| bfa159bf-888b-3bf1-ac96-d868d2ec5918 | -2.92253 | -50.38697 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7db8edc-afab-36a6-88c2-444a59a9ccd3 | -2.89833 | -50.41136 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d7243d46-aeca-392f-ab7f-8bebfa6ea5f4 | -3.04856 | -51.26315 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67ffbc74-bd42-3c66-91cc-7eb20d0a7788 | -3.33224 | -54.18892 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6b83c0c-06e1-32b5-b01a-4c6d94185cb6 | -4.35976 | -50.85735 | 2026-09-14 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df2810fd-c338-384a-9800-6fcf9f5f0902 | -2.90553 | -50.4301 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a442dd08-9122-31d4-9625-3142aef2eba7 | -2.96334 | -50.40745 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3d9540-3d1c-3494-ac77-6bb7e1d00f8a | -2.9011 | -50.41531 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| bd9a4c77-aea2-394a-b6c7-ca9639870c0c | -2.82622 | -49.23356 | 2026-09-14 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 591be3f2-c7de-3630-af0c-39b87190c10b | -2.90223 | -50.42958 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| fa9e10f4-a38e-3657-8203-3bd1be6a4cc3 | -1.71215 | -54.95339 | 2026-09-14 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9aaa093-a49c-3fec-ab94-ec886651b8aa | -2.87745 | -50.43627 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66cc895b-773c-3b43-9d37-98656022daff | -2.77082 | -45.50078 | 2026-09-14 04:51:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82e41af0-e577-3d16-a645-a6a766a89fc8 | -3.78462 | -54.34829 | 2026-09-14 04:51:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06216fc5-36ec-39af-80d2-b2387c605681 | -2.6111 | -54.75949 | 2026-09-14 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8a910da4-ac55-3301-86e6-edf0dc122661 | -2.92529 | -50.39093 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a89f1e-76ba-3df7-9568-00e45057c00c | -3.85746 | -51.98234 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52a43e8a-f97c-35c2-a9ee-436c44df07f5 | -2.92914 | -50.388 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83343d45-77d8-3de9-a10d-e68ef73921a7 | -3.37886 | -50.76559 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61b83265-a223-3adf-b39a-9c38b5504261 | -2.90934 | -50.40604 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 96c0048c-0a39-37a2-b0fe-32ae7408f321 | -3.78312 | -51.34306 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8be50f6a-7207-3f9e-b355-ef200581f33c | -2.92198 | -50.39041 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32e7b9ca-5ee3-3817-ad32-21ef89a6fdd4 | -2.95342 | -50.4059 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baa98f01-23ce-3458-89cb-440dc67de8f9 | -2.96112 | -50.40006 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85712658-784b-3066-a734-eb7639e45239 | -4.272 | -46.53488 | 2026-09-14 04:51:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcdb37a3-8224-3b2c-8a6e-7fd4b9fcb0da | -3.07566 | -51.19965 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 237109af-96be-3891-9f20-19ce575db4c1 | -2.8967 | -50.42167 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c6ab2362-c453-3028-865b-f63067e87462 | -2.87912 | -50.4471 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
