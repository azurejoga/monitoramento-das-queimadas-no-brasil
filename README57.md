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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4371cfbb-9af9-3e11-92db-7a7c4f7d2c03 | -9.50069 | -54.47606 | 2025-09-27 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed7f1c7f-5f85-3117-828d-5cfcf27c0c5e | -11.7934 | -62.73999 | 2025-09-27 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5585bd8-7eed-38fc-a06c-3ecad0efc48e | -15.37097 | -59.17207 | 2025-09-27 05:38:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c33c1191-5592-3ca4-9cfb-d6ca6468050f | -15.01299 | -54.98994 | 2025-09-27 05:38:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98a7b0a1-9266-37ae-b446-34e0212ee137 | -15.93232 | -59.48287 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e0d730f7-3842-35fb-8fde-20c46c34f255 | -15.91087 | -57.50067 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6d272eb-1d84-3a65-bde8-6652704b962e | -11.7234 | -62.59008 | 2025-09-27 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06310720-0b44-39d5-8764-c4f13e40c91a | -9.98217 | -64.9866 | 2025-09-27 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce88744-4abb-3f56-910f-e6aa6cbee6a3 | -10.96279 | -68.4941 | 2025-09-27 05:38:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6dceeea-7000-3815-a2df-2216614b74c2 | -15.93794 | -57.48768 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f56fadcb-7b88-3e4d-9ea4-8df5c53c9687 | -15.93517 | -59.49601 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b674d2c8-f3ec-32d1-bacd-8bbe436b7a77 | -16.75814 | -53.35367 | 2025-09-27 05:38:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 76ba090f-6538-3d49-bc37-a5ad0a499d69 | -16.75759 | -53.35956 | 2025-09-27 05:38:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9329da00-fc1d-34e5-af30-042ac08ad2ec | -15.91588 | -57.50148 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0cd9c09-3baf-3598-9305-239183248cad | -11.74482 | -62.0955 | 2025-09-27 05:38:00 | NOAA-21 | NOVO HORIZONTE DO OESTE | RONDÔNIA | Brasil | 1100502 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2979515-adb8-350b-87ad-571e8c684cd7 | -15.88523 | -59.32088 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78d8ba58-d3ec-352a-9fd2-d0ca3deca1d9 | -15.83587 | -59.608 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35fd4504-e23f-3f12-8b1f-8c835edc930d | -9.93141 | -59.92647 | 2025-09-27 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d227517-e4b9-3cd1-b103-b2aaeafbde2d | -15.90119 | -57.49622 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dad8ad02-6dbd-371a-a264-c44f42088a6c | -15.83098 | -59.61169 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4753fe6f-fe10-3e9c-92d7-ab56cf24daad | -15.9318 | -59.48707 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1bc4bbdc-df4a-3c59-ae84-736781200ffb | -9.79582 | -63.33734 | 2025-09-27 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9dfe40f-770e-3e6c-a0cc-9a9bb349a4c5 | -15.94236 | -57.49343 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18ed7d4b-48b4-35e3-b0f9-828a6275c774 | -15.90178 | -57.49121 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35f96b19-a893-35b4-b62a-2e76265c07cf | -15.74838 | -59.52002 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b12331af-1990-3130-b8a2-d0bfb4877d53 | -11.78824 | -62.70358 | 2025-09-27 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87500325-7b67-31bf-89d0-bfba9f293a74 | -10.18397 | -64.74403 | 2025-09-27 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d36d26d3-779b-35fc-a095-83c22c4517c0 | -15.90587 | -57.49981 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4cc46ad8-470f-38cf-90e2-d3888a7fdda0 | -14.78107 | -60.17848 | 2025-09-27 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea695d98-e900-3e55-beab-e3c2540a62a9 | -15.90683 | -59.3287 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b63b38e-8b67-3fb0-812d-fa3815a7abe7 | -15.91557 | -57.50407 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fba0d51-2fb8-3a5f-a712-3f519781247c | -15.91057 | -57.50327 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2292b2b-995f-381c-a2cd-d49e8194eea8 | -9.82156 | -67.60184 | 2025-09-27 05:38:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3a554fe-99ba-3d43-8bfa-4aef7ff34589 | -15.92088 | -57.50231 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2a65620-a29b-3231-91c6-b437c13f1ea2 | -8.88496 | -66.68271 | 2025-09-27 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29808a77-5654-3709-b40c-0262e88d0b38 | -15.57024 | -51.71359 | 2025-09-27 05:38:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac23575f-0aa2-35cc-9693-04c1448c847b | -11.79475 | -62.3957 | 2025-09-27 05:38:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a7160c4-61e8-3845-849c-f50baaa03b18 | -14.78521 | -60.17899 | 2025-09-27 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 169b2689-609f-3300-9f35-bd16fa14ac26 | -15.85959 | -59.34579 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d84831c-28c0-3ad9-b672-823a196f741e | -15.82174 | -59.61475 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4de88aa7-7371-3b07-8b34-5a8c349fbace | -15.86349 | -59.35061 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f499456d-df71-3efd-87b5-25aeff5a88ea | -10.14942 | -66.96874 | 2025-09-27 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 353c21ef-93e9-34d2-98d4-688cfb17b614 | -15.94201 | -57.49446 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9c93771-c7d6-3312-b8fb-20723e0ea6d1 | -10.1438 | -64.86609 | 2025-09-27 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff4212ad-aa5a-322e-97d3-5eb3320278e4 | -15.93076 | -59.49556 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c211016-ccc8-3f8f-b60f-51d4360a64f9 | -9.95603 | -64.19733 | 2025-09-27 05:38:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b49690e-ca88-3023-b677-c406d85f48c6 | -15.82609 | -59.61537 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db81444e-65be-3719-8075-b034e0485e7d | -15.9024 | -59.32803 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d489070f-9d1f-3eeb-82df-7f124f9ce36d | -15.94232 | -57.49174 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b04bc17-8ad2-3529-9474-1e6f8b1a1e1b | -15.9376 | -57.49047 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d1786e3-eb9f-3177-b785-c0fdb9ab9cfe | -15.90648 | -57.49461 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ba80f54-9178-36a8-88de-1006c336f5a1 | -12.24479 | -63.40306 | 2025-09-27 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9d7f84c-3d92-3d7b-ad70-073681dcd74f | -15.93664 | -57.49688 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de830019-c7d8-3fc6-8546-3713157bea62 | -15.93695 | -57.4941 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8789abf-4ea8-39bb-9c77-db1ffe62f2f6 | -15.93696 | -57.49582 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61fe1bee-ff06-3c0a-87ed-4c4f2121bbe3 | -15.83533 | -59.61229 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54eeeb50-49b2-3519-a04e-e297dd8b73d4 | -15.90618 | -57.49716 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47be5762-7157-3db1-bb7a-d1e94fd8cc3c | -15.01205 | -54.99854 | 2025-09-27 05:38:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0059db29-152f-3ba2-a541-2e0b28db6335 | -15.74401 | -59.51945 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2e80205-6d26-368d-ab3b-5fd9b823a032 | -10.28198 | -67.22989 | 2025-09-27 05:38:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d4eb112-20f5-312d-a9d5-783453181d60 | -11.71993 | -62.58955 | 2025-09-27 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 743871f1-8e1b-3fc3-b205-588135ed14c1 | -10.55837 | -68.17117 | 2025-09-27 05:38:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9f5a314-1748-3301-8f13-eedfd1d57afd | -15.93755 | -57.48879 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60bc055d-d5cb-38c2-90b1-0e6c06b1fe10 | -12.89329 | -62.12542 | 2025-09-27 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e3634a7-3c65-36e4-997d-b9e09b238cd3 | -12.88971 | -62.09899 | 2025-09-27 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1ff2d60-b5e6-3a93-8fc6-9249905d0f21 | -9.53985 | -64.5727 | 2025-09-27 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26c3da72-0838-3203-8f91-8cfbc8731955 | -9.84723 | -63.62291 | 2025-09-27 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71feb473-af19-38f2-a16e-f5491cd42b33 | -12.87243 | -60.20413 | 2025-09-27 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 194dc635-f944-34f1-8d58-1fd90b2c3ee1 | -14.02416 | -56.10636 | 2025-09-27 05:38:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a1e1891-e34a-314c-9c0f-80c0528f71eb | -15.88461 | -59.32587 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83308b9f-0d21-3aaa-8311-fbbe0c7e43b7 | -9.94079 | -65.20561 | 2025-09-27 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08d4d4e0-bb40-3e85-aa0e-0b9f823fa5ce | -15.90149 | -57.49368 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a544d4d0-4d13-3a3d-919e-e0e59103f949 | -14.02457 | -56.10291 | 2025-09-27 05:38:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 318258af-c979-3378-be59-a67e09da533f | -10.19873 | -58.21938 | 2025-09-27 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 793e408a-e25c-39ce-8787-d450f4a732d1 | -15.83479 | -59.61658 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d08ee525-9889-3d30-b758-adcf552e1e95 | -15.01252 | -54.99422 | 2025-09-27 05:38:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f786a131-e221-3f4f-96e8-633a67bc95fe | -9.65091 | -62.83662 | 2025-09-27 05:38:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef01253-493e-3163-99dc-4af5d5b6cd3a | -11.79605 | -62.73928 | 2025-09-27 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71715ab7-8f5b-35f7-821f-bac3e4fcf780 | -15.86398 | -59.34676 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5413a2e2-bfb6-3fe4-a4dd-e9884441d838 | -15.94268 | -57.49071 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b2d4d75-3100-3b13-86b1-1f30f3e85ef0 | -15.93729 | -57.49312 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95e18281-8e4d-3651-8e3b-1e0a100298b4 | -16.7642 | -53.36013 | 2025-09-27 05:38:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fee3cf45-a213-3191-bd0e-acf37ebf4e2d | -15.83044 | -59.61597 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6dc99a8-85aa-32b1-8e78-d51ed1603b1e | -12.1737 | -64.10387 | 2025-09-27 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beae9c75-5716-376f-ae86-5c499a16219a | -11.99707 | -61.02116 | 2025-09-27 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a6492fc-f067-3210-95cf-728caf8d79e4 | -12.86441 | -60.20291 | 2025-09-27 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24e2f589-6143-31ac-ad84-097ee8c3cc32 | -15.93465 | -59.50024 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b793a056-3f94-3180-8f22-e1151e7d09a8 | -12.17704 | -64.1044 | 2025-09-27 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61164536-d2ea-314c-91fb-391ee2041faa | -10.25513 | -64.30928 | 2025-09-27 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbc08464-8a35-39ca-85bf-060fde7c066d | -15.93725 | -57.49146 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f96e6176-bbfe-3b2c-9db7-4165d725b341 | -15.89798 | -59.32725 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96686bcf-ce6e-3b67-9a4d-28fc5b57a814 | -15.91128 | -59.32927 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff315013-935c-3683-885f-a0636ae2ac91 | -15.90207 | -57.48875 | 2025-09-27 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e175415d-37ec-3964-8f96-8e41f55e82dd | -11.00719 | -68.42857 | 2025-09-27 05:38:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0a65c0e-8c17-371d-b210-ee374a155abe | -10.14596 | -66.96817 | 2025-09-27 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d09f7479-98af-3b5b-ab6e-16498c417b81 | -11.72398 | -62.58616 | 2025-09-27 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df5583f4-048a-3ee4-81eb-843319113741 | -10.18342 | -64.74751 | 2025-09-27 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0369c832-9806-360f-be25-996116c63d49 | -15.92795 | -59.48203 | 2025-09-27 05:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 23aca5a4-8202-3b25-b964-60b1f2f2bd47 | -9.54039 | -64.56923 | 2025-09-27 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68239252-e7dd-34dd-9bd4-0613520442c3 | -20.88614 | -56.60427 | 2025-09-27 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 29.3 |


[Clique aqui para ver as próximas entradas](README58.md)
