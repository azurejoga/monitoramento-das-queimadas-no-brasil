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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7b47aa4-b069-391d-b50d-8fe0563ee9a8 | -8.43489 | -62.68543 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| eec1ba47-d8bb-3233-8d55-06f5ca30e222 | -8.43213 | -62.68143 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 73144eba-7f95-390e-a384-e44cb8919a5d | -8.42937 | -62.67744 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 581333d1-adf6-3318-9c3f-f9987357cba7 | -8.99113 | -60.59949 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 719b1aa6-0fa3-3e50-a793-4ca1940b490d | -9.39867 | -60.3625 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2848fd29-9e95-30ae-8f6f-12fc5af2dde3 | -6.68919 | -59.07521 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e766e739-d1b2-3656-9be6-6b14d8a2f644 | -6.60167 | -58.9882 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8547f483-f865-3c91-b509-814f3e37fa14 | -8.98535 | -60.59068 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dae32cce-94ef-3b4a-868e-1b33977e5cab | -6.6218 | -59.07805 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd676c94-3166-333f-89e1-7c25876a698c | -7.83704 | -61.34324 | 2026-08-16 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9e1da6e-684b-323d-9663-d8aa502d24cf | -6.43024 | -60.07058 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af6e5461-c892-3080-ac18-a5f631b67604 | -8.54482 | -54.59453 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 126842d1-1cfe-32b8-98dc-fe3bf9f63933 | -9.39899 | -65.95769 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e687d92e-5f9d-3def-8546-e6d6fa069265 | -6.60595 | -58.9845 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bf09378-af27-3158-8479-92e3b9b0efff | -8.95872 | -60.51975 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 797743e1-81c9-378a-a19c-17af412437e5 | -7.4126 | -60.01316 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2283eb08-cd93-3bb6-b5c6-c8ee40aca46e | -11.58532 | -54.68731 | 2026-08-16 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e834a3bc-86c2-3576-bc29-e34f622fa87c | -9.47569 | -60.52304 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 911f71ce-bbf1-389b-ac2e-10088b55b9df | -6.59025 | -58.98839 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23510eb9-03d1-327f-a8c1-ed759a361e98 | -7.88721 | -63.75506 | 2026-08-16 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd16b53d-ebee-3489-a570-e009a55f3193 | -8.90411 | -60.57458 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d49f978-b824-39ed-8fda-1a0ceb4475a8 | -7.06898 | -56.64956 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bca95d71-d4e8-3e05-a2c8-de69261aef5f | -8.95796 | -60.57106 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50608d69-246d-3ebd-91f0-65b912cec64a | -6.63334 | -59.07547 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 177dbb75-7e52-378c-bd75-e5402fa0080c | -7.55856 | -61.17116 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a63d5e9-a310-3a8a-a2c6-674f13e5f02f | -10.69866 | -62.23451 | 2026-08-16 05:36:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54903aee-f6aa-3887-87e7-4112595893e9 | -7.4231 | -60.0148 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c427034d-bbb0-31ba-94b2-d4607f8b768a | -8.95508 | -60.56669 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b4b549e-4d3a-3709-b3b3-ce55c87028ac | -8.97145 | -60.52964 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fdcac229-53f1-3dda-bb8c-5f7079e542eb | -7.34168 | -59.60247 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e731567c-831f-3640-97f7-85d9f1656dde | -9.15619 | -60.91943 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeecd172-7f2f-3815-99fa-7ccf5b41db00 | -11.2018 | -54.80905 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f152fdc4-d754-3db0-9ad2-6051fc76c590 | -6.73341 | -58.58709 | 2026-08-16 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1a4bad4-8b96-3bd9-aec1-8e5588c283ba | -8.81087 | -66.76861 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96fcd0bf-7891-3ec2-930c-146a923107f1 | -6.62844 | -59.08335 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5f8158e9-5968-3818-a3a3-0e4e54588faa | -8.97036 | -60.5136 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 430e0a59-2957-30ca-aec9-c1b84c69eeed | -7.42694 | -60.01847 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83774735-9514-37c8-9bc6-a2a6133a05e9 | -6.71663 | -58.94242 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 436d7a3c-f992-360f-a708-94d8383bc03a | -8.60617 | -54.70351 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aafa126-d526-37e7-ba4a-d6a5d906c47c | -6.84961 | -58.97879 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d07a6715-6183-3b5a-932b-35947e74ad60 | -6.7218 | -58.93614 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d31e3673-5133-3aee-bac1-a2393eb0b385 | -8.97667 | -60.52998 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4a889b4-9dbd-36ff-9d56-80c65ae89b5a | -6.70815 | -58.95174 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b00b6573-997e-35d3-a506-ce9ffd5869cb | -6.69584 | -58.95875 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb5dfa2f-f4f6-31e6-9269-72b9cc5e8d22 | -10.72059 | -52.11261 | 2026-08-16 05:36:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e94a5435-9c3a-30de-8c11-ad01b10da65f | -8.98766 | -60.59895 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb427250-dedb-3aa8-b5c4-2993e8980df7 | -9.08626 | -61.40134 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3b1a503-4531-3259-8cc1-d79c2e07d1c8 | -8.9622 | -60.5203 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad844c04-9087-3362-b3c5-9695eac1ff85 | -8.64558 | -54.71667 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22622275-6ac0-3de4-8cca-804a64e1806e | -6.5896 | -58.99265 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 750d8a0a-6fa5-347a-8643-9960951a3ff7 | -8.97666 | -60.50617 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b16ceb4d-f565-32ce-b528-78cb887a7d77 | -6.61531 | -59.04687 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0e6117d-c816-343a-abb3-ad48f7927912 | -8.97551 | -60.53774 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e826472-35a3-38f5-b926-5e943ab4def4 | -7.35068 | -59.59135 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e4c1392-a1fc-3b16-bf52-5952761f9541 | -9.37198 | -62.36254 | 2026-08-16 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef347f65-7377-354d-a248-8a59248da16f | -7.4085 | -60.01648 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 514e9e52-8150-3658-9327-717f4926225c | -6.96476 | -59.30227 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64d9553e-98ef-34cb-afe4-46eb8ef2998f | -10.72117 | -52.10782 | 2026-08-16 05:36:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c018ce9-a1f3-3dd8-9e41-2de13ee84bc1 | -6.81778 | -59.88607 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f51d071a-da39-3643-84ae-5d6afce6501d | -6.88911 | -58.94056 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c504f45-8ce6-3e32-ba3e-7b465cb1cb2a | -10.93955 | -57.11221 | 2026-08-16 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d370bb70-9a27-3dcb-bd7c-948fd4e062d0 | -6.96413 | -59.30641 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9c82abf8-aacb-37fd-9fb2-552a815aec24 | -11.21122 | -54.81689 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a87f30c4-7b09-3a4b-bcec-460bd8e31c79 | -10.0012 | -67.49195 | 2026-08-16 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d38ce986-1260-367e-b540-6b3b3e5a2d8c | -7.4242 | -60.03087 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81cb146c-1d7e-3bdf-8452-96223abfe171 | -6.7887 | -58.76183 | 2026-08-16 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b3a1d9b-a1f8-3d3a-8063-0cdf14e05c3d | -6.61643 | -59.06426 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4407b9d4-e5cd-3540-9d4c-46d34ef6d7ab | -6.60707 | -59.00212 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddeb3049-20c2-3dbd-8a35-3cb9c4abe7b8 | -8.95813 | -60.52363 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2b865c85-78de-33c5-916c-8ec54cdb32b1 | -6.60104 | -58.99247 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b8bb221-69ba-3b51-bc73-b972dd9935c3 | -7.55182 | -61.17011 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e9d5f8a-2a7f-3971-b1fc-7f5b7c0f1db7 | -8.26458 | -57.34441 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b7afc4-eca6-3098-a80f-840fab902db5 | -8.43598 | -62.67849 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 7a9784d5-b062-3444-aa32-5830d0c75a1e | -9.47338 | -60.51466 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a61ee826-2028-3bc2-bb91-910709cc8585 | -8.90001 | -60.6016 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba1bcb81-b34d-3137-903b-b23bbcd570f7 | -7.41792 | -60.00192 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6be715ce-d3f5-31d4-9251-1d374ebe18db | -9.35373 | -62.37044 | 2026-08-16 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec81aad8-34ad-3cff-a512-7e7530f33ea7 | -9.37362 | -62.35201 | 2026-08-16 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9b7a011-09fa-3762-9963-48b103704ef6 | -8.95642 | -60.51147 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 972e8e68-b5dd-3260-91f7-a47d20db19f1 | -6.71447 | -58.93502 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f24062da-6795-386f-9e74-343577ca666b | -6.62307 | -59.06959 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 353e4e81-a120-319b-adf0-78388858fd72 | -9.58648 | -60.5069 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ebbe24b-ddb9-3207-8468-9e14c1c4497c | -9.20334 | -59.67445 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8ff3824-a497-3794-bbcb-a4209aae7c48 | -7.38467 | -59.98474 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea33a0b3-1d97-3850-b000-92444835e6a4 | -6.63398 | -59.07124 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1fb1180-1123-39a2-b8c9-1982110dc233 | -8.96509 | -60.5247 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b052b644-9c18-314f-a5a9-3a19d80f0de5 | -6.59689 | -58.99378 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5544a36-02b1-3726-b150-a2ed0ddd82d0 | -6.43311 | -60.0749 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da85acd3-2724-35dc-a114-cf137dd301b4 | -8.89949 | -60.55808 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b257b56d-3867-3a35-8726-dd2c45e0cde4 | -8.41094 | -62.66348 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cebe97d8-d005-3970-b4a0-2adbc37a632b | -9.20783 | -59.67276 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0815dfcc-d71f-3d4c-a7c3-53e2ac8a2629 | -9.54765 | -56.80178 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fccecbb4-d706-3956-a2d6-23671abbf40d | -8.97027 | -60.53736 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66865472-4246-3e91-86fc-2a1ca65ee364 | -8.97384 | -60.51415 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c5aa7bbf-2fea-3076-8c7d-5c7ebabf32ee | -8.9755 | -60.51394 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 11626f03-ae3c-3ec0-9585-4828f91e07b9 | -9.14457 | -68.2037 | 2026-08-16 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29d354fc-2649-3bf4-8385-ba41ab10317c | -6.62544 | -59.0786 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e93436c0-882d-3cbb-9831-e8776fe374e6 | -8.43101 | -62.66702 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d90a52ab-ca57-3768-a526-02df96b37868 | -6.85089 | -58.9702 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a2acdaf-2e6d-3fe4-8a70-91afb131bdc6 | -8.98363 | -60.53107 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README49.md)
