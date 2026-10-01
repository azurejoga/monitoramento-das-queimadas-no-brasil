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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5f76e29-5474-3ef3-8130-f2d3de94b0fe | -7.78153 | -49.87271 | 2026-10-01 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e660e6e5-6eba-3a26-a2eb-b46416c9734f | -6.14036 | -53.25763 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e6a2929-d5a2-3cd6-85d1-379bfe180dd9 | -8.16043 | -54.83084 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0182cb16-08a0-3654-b129-e2e059b7175d | -6.15903 | -57.70118 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5551e50c-905d-3627-ac3a-4a795670ae58 | -7.55386 | -55.03036 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05d6cfee-185d-3153-bbcb-16f8d17ce8e7 | -6.65773 | -58.87708 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fc2ae20-6bc5-395d-a948-c25328c8dde5 | -5.98452 | -57.71165 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 710987d0-4ed4-3eda-a01c-cffcf26d29ed | -6.35448 | -55.33548 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de58f2bd-fb73-3d33-a28b-1feac5c13c20 | -7.03989 | -55.6285 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bde1ac77-feda-3d1d-8a5a-44e7e08b948a | -11.72969 | -50.41304 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed3403be-e119-3bbe-8fa7-8f2d1eb526e1 | -12.18936 | -48.43985 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 408ce96e-9389-3274-b802-9cf75f608754 | -10.25278 | -59.02881 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c708f6-ee0a-3be8-b3fa-2cbec839bbdb | -10.53023 | -57.77891 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 043aa01a-62d1-34dc-826c-40ff871ea11a | -9.36252 | -56.46847 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b66cb56-7ea9-3c2c-ae93-4678ada362a8 | -10.52042 | -57.77346 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91fe2213-da08-3148-8383-291bba4b15df | -7.68497 | -55.1161 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2932a505-f285-3ff1-923b-1a46f08af5c5 | -6.34837 | -55.32538 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a251b8c-751b-3093-9053-1fe3e7653d44 | -9.74583 | -65.05013 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f85ee53-52e6-305c-b7d9-4faa61ab97ad | -10.25297 | -49.67361 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dce378bd-1361-3b4a-82a1-d0fd4e590654 | -9.38824 | -49.15265 | 2026-10-01 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da923fc6-a309-34fe-8038-264703d34d2b | -7.50868 | -55.04304 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8c59e6a-afb5-3161-81e0-99b4062f02db | -7.50936 | -55.03827 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d46a3d3d-0e64-34ce-a3c1-46aac8116d50 | -8.26215 | -54.73763 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a8d88f4-dbdd-34c2-bed8-b2605a3c02a8 | -7.49986 | -55.03533 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cb0e055-08c8-3926-b48c-daab07f7a6d5 | -7.7855 | -49.87864 | 2026-10-01 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68fda51d-c96e-3a22-b298-050877ae09fe | -7.49492 | -55.00124 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9fa5b67-9303-39a4-8611-1ead416c6ee4 | -10.82856 | -57.20729 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8dc868-3f2f-3eea-a1f2-02cdf07a9b16 | -10.30516 | -59.46021 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5be95aab-3648-30ca-84cb-5bad9813dcc1 | -9.14434 | -60.29548 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b231d53-fd1d-38d3-b11f-b28d3e0357fb | -6.45268 | -55.47974 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 919adf34-45c9-347c-81ad-57db8c4659b6 | -9.70972 | -65.06256 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eb6e456-7a80-35d5-93b6-2d6ff35f7a82 | -7.50482 | -55.04246 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92356c4e-d89c-3f8f-a576-ca0f0eb23b3e | -11.3973 | -51.02559 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1cf90b4-6427-318a-b0b3-1079f14323b1 | -8.26538 | -54.74332 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26b487ab-fea2-3e1f-a1aa-83bc6b0564ab | -7.47273 | -49.57166 | 2026-10-01 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1a0a092-9dac-341f-8942-088f26d01ea9 | -10.53312 | -57.78328 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 287ede88-d91f-3b73-b202-cae7d0c6ff18 | -8.23639 | -54.77579 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50677292-1036-3df8-9af7-71a9fa215903 | -7.52936 | -50.53272 | 2026-10-01 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84034456-36aa-3a31-8e8e-7c832d1f72de | -10.54596 | -50.01121 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 945ccc27-83a5-3170-9ed2-058b21c2e06b | -10.07371 | -63.08235 | 2026-10-01 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce1b8efe-013d-3993-b6aa-1bbed28391db | -11.26202 | -54.81456 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8036b408-2434-3b28-9183-f1b1a9341dd9 | -6.01604 | -49.56137 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8f5cac3d-c220-3e79-8c13-cb07d15b7850 | -9.58738 | -54.63612 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46401cc0-766e-3230-8acd-7f93257ce730 | -10.54408 | -57.78104 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a37e8815-f900-3db9-ac69-eb83c0b2454a | -6.47343 | -46.55823 | 2026-10-01 05:18:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d1e075b-7d09-359a-bc40-4a0fe4c24651 | -9.66875 | -54.34616 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f48d6ed6-6326-39d7-990a-cdc07f91fa17 | -6.49024 | -58.5318 | 2026-10-01 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a251c2c7-2810-380e-9b11-9c01595a2dc9 | -8.0677 | -50.96268 | 2026-10-01 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 703c8633-10f5-3e89-8cb4-bd86394d0588 | -7.17329 | -55.40762 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 526e65e8-4842-386a-8a2e-64df5cb59cec | -9.69952 | -58.12963 | 2026-10-01 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 784152aa-9716-3f24-bd7c-6eaf447991f4 | -7.51322 | -55.03884 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cada8b66-6d64-3da5-a7fb-dede80252436 | -7.47222 | -49.57539 | 2026-10-01 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94c44f1a-b144-321a-8761-23caa598add4 | -11.37763 | -55.12337 | 2026-10-01 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5491b5ac-8455-39f7-a1a3-1161bb2e1e9d | -11.33051 | -50.96692 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 10a16774-c26a-384b-896b-576a75683167 | -9.02209 | -60.55177 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 786e729b-5010-367f-98b2-d63aefa47f0b | -11.25935 | -54.07358 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c72f867-2980-3090-a2cc-db8a0a8bb7fe | -6.69865 | -55.05651 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f0cae20d-cf6d-31d2-837a-9cfb5b4a7db9 | -5.91176 | -53.49509 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3abeb6b-985a-3f55-83ed-a99f360660a8 | -11.17674 | -54.11526 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e74ee4c8-fc8f-3bc2-8276-ddcde7a72484 | -6.49355 | -58.53231 | 2026-10-01 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e9f6e58-486e-311d-b6a6-3232a5487697 | -9.35099 | -57.16498 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94c5ac1f-3558-3da6-836c-342bd037cbd3 | -7.787 | -49.87361 | 2026-10-01 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 426fee0a-a31d-3a13-9edf-e1e0c313db0c | -8.52101 | -54.77129 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f5c9b04-5bc6-3b8d-b1b2-ee32093047c8 | -6.91396 | -51.67336 | 2026-10-01 05:18:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 970b3c46-08ce-3cf6-ac15-a8505479ab1e | -11.78957 | -50.5202 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c38ac6a-c015-385c-8ef1-90a3c01afd39 | -6.683 | -58.86684 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 964abd60-1064-341d-964e-412d66f06465 | -6.75586 | -55.08648 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9877df3-2692-3cf0-84f0-757f83a6c583 | -6.08444 | -56.47546 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5722064-5346-3bba-9364-7bffda6ce660 | -8.27031 | -54.76511 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2d128d9-e4ce-3c60-a42e-6c5ef0a55684 | -6.16294 | -57.69809 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4a9f442-c72d-3425-bbfc-e454ec838611 | -7.49164 | -54.98453 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2d8b47f-937d-360a-8695-7fc5367fd115 | -6.16636 | -57.72066 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cafb8fb-d2b0-3d0f-b17e-cda991d4bc54 | -7.72508 | -54.79028 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9fae2b9-5819-39eb-8720-c1dbbc6fc0cc | -7.49722 | -55.00011 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 287696b5-a2f1-33ce-bcca-1328c289e47b | -7.03706 | -50.72961 | 2026-10-01 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1e58567-058b-35cb-9ae0-b68f233b3ab2 | -7.70398 | -54.79736 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a9d2b4e-4cf2-3b55-a699-235d3caf18d9 | -6.1316 | -53.05379 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0225d22-35e9-36f6-82d0-bb0661921df4 | -6.16239 | -57.70168 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69304d09-c5d9-3632-beeb-3c3a872eef83 | -10.81003 | -48.75726 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ab6f494-9ffa-36bf-8c9d-e3d34cc853ea | -10.52273 | -57.78173 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7abeff2a-5276-3c90-a27e-13f8722cea12 | -6.14459 | -53.25835 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b55fc79d-0d84-3809-8dfb-d70ebf1c64af | -6.08115 | -53.30976 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7dde43a-dbdf-3275-bd3a-49f38272bb7e | -11.39237 | -51.02145 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70420bcf-2399-3f3f-b792-c737e2718783 | -9.5879 | -54.63248 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e864c5f6-c45f-313f-9bae-6ce43132c83d | -11.51411 | -47.17444 | 2026-10-01 05:18:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2d04d5d-2eab-373d-b758-a4531ea12d79 | -8.17667 | -54.79824 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 178c4704-c0b8-3668-a232-9761ee1ff5d0 | -7.60212 | -55.69872 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0361d3-8550-39a4-a86d-e028aead9464 | -9.00593 | -65.69917 | 2026-10-01 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd798d06-9113-36c9-80ba-bae514a2c2f7 | -8.06468 | -50.96296 | 2026-10-01 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca720caa-7d9d-3f64-9dfc-8c448852cf06 | -6.85465 | -59.96815 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d7e244c-5407-38c7-a798-5b750c810325 | -10.35328 | -55.44398 | 2026-10-01 05:18:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91166af3-86f4-3dd2-8a4b-c573e265d4b8 | -6.06768 | -57.61023 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea6fb965-159b-384b-b2f7-8a74317e3899 | -7.71894 | -54.80477 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a6d02f6-b8fb-3cd4-9e25-d8a73d6c3a58 | -6.43756 | -55.8035 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4226ff1-a4b9-3664-83cc-3eb5d03b1e24 | -9.21736 | -50.68362 | 2026-10-01 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85dd5dee-4df9-3d05-93b2-975341b824df | -5.29969 | -55.8693 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 972837df-45cf-3064-8f3b-6a75102e1cdc | -5.86167 | -57.75869 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1a59e47-ca2e-3855-9370-993f7d6e44f1 | -9.58434 | -54.62826 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 381a8312-c406-38ca-9ecd-28557bce4d8e | -9.34687 | -57.16847 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1684aac-51b8-36e4-a9d4-3afe96bfd4ce | -7.63811 | -55.05977 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README82.md)
