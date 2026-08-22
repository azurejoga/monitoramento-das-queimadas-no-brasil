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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e2c4053-4357-3df9-bbd6-43ba8e0c7a67 | -15.20808 | -52.77247 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dea4117-1c1d-38b8-954a-0bd5defb8a01 | -11.62819 | -46.51909 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 345b89d1-2189-31f8-b2e1-2e4eb6453b1c | -9.18055 | -59.45034 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31ad7b91-da52-3998-856a-168dde8abdad | -9.44352 | -51.64697 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b62cd6c-aaf6-334f-a42b-8d8cce179380 | -9.17505 | -59.46376 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2b009bdb-2e69-39b7-8291-d7cab814fc21 | -10.81335 | -50.98287 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87d9a70b-28c4-3038-bd9f-0c43e50add85 | -11.63067 | -46.52733 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ade0428a-9850-34da-b0d4-7bdecf0329e4 | -9.39136 | -60.56168 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17f07593-b2eb-3b77-bc61-f0317847472e | -9.84345 | -57.71682 | 2026-08-22 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4c3fca5-2422-3b08-a94f-93e56af32a15 | -9.28444 | -60.90752 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b219a7b1-f6a4-31f9-a3e8-212355f4e830 | -15.23673 | -52.83025 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a925d6db-0953-34a4-9161-6d6c3e1c4d31 | -8.90126 | -60.54371 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 62638f6f-c8fc-386c-9345-ca070e3ee5b6 | -9.17171 | -59.44179 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e5c2710b-2af3-3554-b85e-32208bfa55da | -9.40734 | -60.31243 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba367b5-8798-36d8-b425-7f02653575e9 | -7.87796 | -63.74383 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73f74c3b-ff55-30e0-872c-0592117b1aaa | -9.20864 | -60.76762 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9608f7a3-4114-3e56-8708-6336d09c7fac | -10.90594 | -50.2374 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0442d5f2-c82d-3428-a597-221c3b0d4c84 | -9.39969 | -60.55222 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60789d99-56d3-3766-958e-2bc637839b12 | -9.4182 | -60.43633 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5729c39f-6ccb-3227-9986-02526c497039 | -10.52319 | -50.77566 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ff9eec5-fead-3641-895f-c59bbf2e1c0d | -9.04541 | -60.45124 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b8a7836-1b12-3fab-96fd-6c58d0558d86 | -8.95107 | -60.59521 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1b89995-9268-3ad0-acc1-213d0d751152 | -9.18608 | -59.45838 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4157326-6d51-3c10-ae2f-6584deb9ddf6 | -9.10577 | -60.92226 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28dbec0c-924a-349f-94e0-fdcd186b3b1d | -9.43954 | -51.60233 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d8a1ac9-c9fb-3dca-952d-d861c3de9a40 | -10.80727 | -50.9761 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f033f14e-378d-308c-a803-d6d2dd8ea830 | -9.11258 | -60.35068 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fdafc16-6003-3a32-b2fd-841ab7a039d4 | -9.12692 | -61.59414 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f0c8ec8-e7a0-3f37-a19f-48b522be1032 | -9.11488 | -61.60362 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd6856f6-68e9-3050-aa25-08524800f098 | -9.17338 | -59.45277 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 059369ea-a0f5-3a3b-a9a6-f6ca99092bb0 | -9.11481 | -60.33667 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc17aea9-c26e-31e1-9a65-ab52861e06ed | -9.15032 | -59.55622 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7790cdde-4ab1-3dd1-9c27-fba4b89f0bc4 | -11.56232 | -46.94158 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e699de01-008b-3d96-a9ce-1a2019a2bd38 | -10.81424 | -50.97615 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b6f3e94-5d4c-303b-bf46-c1fbf2c1c101 | -9.17228 | -59.45975 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4b244f0f-54af-39b0-a912-7b0c4b1517f5 | -9.06207 | -60.43238 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd4ac80-e9c4-3240-945b-3c59e4832a0a | -8.6844 | -54.741 | 2026-08-22 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f79dfd6c-cc9f-370f-99e8-787802834e22 | -10.51762 | -50.81982 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cfe5061-272d-3a4f-a51e-6185638668c1 | -10.52113 | -50.77197 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9d3a8f7-0b9b-38b8-9829-72f4c9f9089c | -9.17724 | -59.44982 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c1537bd6-3e47-31c6-94af-65319ff3b58b | -10.29832 | -48.22935 | 2026-08-22 05:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1abc6da-ce3a-3dcd-9329-07244101f390 | -14.50638 | -59.81982 | 2026-08-22 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94246ddf-9b2e-3933-bdff-d83fb9d7c12a | -9.04434 | -60.4367 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d90e0cd-88c9-35da-b75d-90c5b19ff212 | -9.38804 | -60.56114 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbb5cd0d-853e-3e62-a22f-fb12d8eee712 | -9.41243 | -60.55789 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cd27151-ef7d-313b-99ba-579d2e6be508 | -9.36362 | -61.02703 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2cfe7be-04d1-3ca2-8492-9ee321685681 | -9.40604 | -60.42716 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed517768-8ba8-3434-899f-5d8fda59c7b2 | -15.21771 | -52.77716 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 899c08a6-0d07-3aab-8d1c-77a1926f769e | -9.18772 | -59.44792 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 66f4a467-e2e0-3d2e-bfef-689386b53b9d | -9.1618 | -59.46165 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| be696727-12a7-38ea-b059-91e238906706 | -9.16897 | -59.45922 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 34ed531d-e765-3baa-b95a-7a9b32d97d53 | -10.65378 | -51.59174 | 2026-08-22 05:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fce3b19-29bc-3b88-8f42-13f36b1e7047 | -9.51085 | -60.49485 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4457c127-11a1-3fe1-ac67-7df5a34e87c8 | -9.40992 | -60.42419 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 745ed3ad-e5c8-3565-86da-99b2cd4e277d | -9.1629 | -59.45468 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cb8fcafe-086e-332f-8309-a6df523efd31 | -9.21721 | -59.77751 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a619dd4b-be73-3003-a346-5bc054cd65a5 | -15.20308 | -52.7717 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c684e6c-769d-3ed1-b51c-ea1dad013818 | -10.5178 | -50.77497 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c28171f-257c-3f33-aa09-6553b5a12e87 | -9.16688 | -57.00915 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f678d040-3d1a-3be2-a05d-18c17350575a | -8.40071 | -62.69253 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7204c3d-cd74-3dc0-85ad-685961e40318 | -16.50036 | -55.18515 | 2026-08-22 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ba6da66f-58e5-31a3-bfb8-e60cf95ca610 | -10.68408 | -50.29717 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c8e17c8-1439-3201-a3c4-a7dba93abcfb | -9.15849 | -59.46113 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fead20ec-87d0-3e98-9dad-13476ddf2e19 | -9.41156 | -60.43525 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76ba4f77-fe22-31bf-a8fb-9fa2f358edef | -7.89192 | -61.18349 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3446820c-d521-39b3-a5fa-04bae09aae56 | -8.95327 | -60.60281 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6b7fe2a-e5ec-32b8-8776-0f0ae1542139 | -9.40884 | -60.40962 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e54dadc8-1ac5-346d-9511-d426fb4a3ea0 | -9.06427 | -60.43993 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01373d8f-66fe-393e-9ef7-6eb5f0dd893f | -9.44187 | -51.62223 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d10d9a2-53fd-306b-bf48-8b18158ca4be | -7.85944 | -63.7603 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c8e34f7-10e7-348f-81ec-35ad6b455a72 | -9.11757 | -60.3407 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 551a94a2-e1b1-3b6d-932d-e7048db9c19d | -9.20835 | -59.76896 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 615f296a-e467-36a8-b156-733e50643096 | -9.21198 | -60.76817 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b3b8f30-54e0-340e-8120-b5ee93ce61d8 | -9.17007 | -59.45225 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1958c7d0-f166-3f65-894f-d91714bdc620 | -10.8126 | -50.97681 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 44adaa54-e5fe-3c42-b53c-642e7965d8e7 | -9.16088 | -59.66143 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 477f5272-5230-381b-a82f-8150ede0fa9e | -15.21735 | -52.78016 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 695a5b49-04fc-3186-bd2a-fb7325c242a0 | -9.51127 | -51.67593 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e7c10ee5-30ce-38a0-b7b0-98fb89f02458 | -9.16514 | -59.48363 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07276c47-78f1-3f4a-bd03-9eae327c6c9a | -9.11813 | -60.3372 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16e2b4e2-4929-3c2d-8167-dbed390595e0 | -16.70705 | -47.70314 | 2026-08-22 05:25:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c542a991-03fd-349c-8ac8-0282d16d342d | -9.18663 | -59.45489 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b20d2cf6-86df-347e-aa65-da94216d8cb1 | -9.05875 | -60.43184 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a32439-acfa-3989-906a-2891265584b3 | -9.43912 | -51.6053 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc72a01b-2052-3d9c-8d72-5c4ffe256a19 | -10.52254 | -50.824 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 234855ca-1bd8-3b22-ac3f-94b84a33586c | -8.90013 | -60.55075 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a4f427f-460e-3443-afd7-c8f867aeb2c4 | -10.89869 | -50.23656 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61156d0c-474b-3bb7-91fa-df6d8354336b | -10.65417 | -51.58871 | 2026-08-22 05:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 917d3ec7-a6d8-396d-af11-34e63f0066b7 | -15.24101 | -52.83674 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cf292e2-0f91-3b42-85d1-97157717f545 | -9.18994 | -59.45543 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7bdc6ea-002c-3648-8d24-537347136f9b | -9.20921 | -60.76409 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e79aacda-efba-3666-bfb3-8697b66c6883 | -9.16676 | -59.45172 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 233922bf-1b0d-36d1-b3da-bd7f3749c7be | -9.43728 | -51.62026 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82af5aaa-4619-3370-82d6-5d3694f44c92 | -10.89268 | -50.28574 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 335a7655-e186-31bc-9efc-32bd1d6f9372 | -10.68362 | -50.30091 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64948399-a3fe-3075-928d-98d4c3615be0 | -10.52774 | -50.78297 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ae2124c-4526-3809-9634-f67de2ed70a7 | -9.04265 | -60.4472 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d76f539-75ae-3322-99ee-2f94f555a392 | -8.40924 | -62.68546 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb101285-2f02-3fc0-90c7-e894d107718e | -9.28617 | -60.89683 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 710c0d5d-6e77-3cbd-b15f-22faef42cbc0 | -9.43903 | -51.60697 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
