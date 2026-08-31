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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a1da596-db38-3552-8fe3-1a619f7874ab | -8.86662 | -66.89839 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eadfbb3a-d705-39f5-adf6-5d3f799de259 | -9.85295 | -64.99039 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73cd0661-1101-3d13-9248-e87a50d2dea5 | -9.00498 | -69.43761 | 2026-08-31 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9afbf46-c47f-3e14-a2cd-729261fc2a50 | -9.06306 | -65.4185 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f36d773-362a-380c-abfc-e515b48e13fe | -4.85394 | -55.83414 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d08652dd-2338-3cc7-9bf3-286d915ed284 | -8.80472 | -62.49566 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31b69976-521c-3665-b9d9-789e64c6a512 | -9.00801 | -60.60299 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817a7deb-4587-3fa2-a1c5-bc84ef297ac8 | -9.14601 | -61.09556 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04b6d10b-7128-3096-a37e-d665edf2c978 | -9.12882 | -65.47574 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b07ad43-825c-3f3e-99b6-f364b1865a49 | -9.79662 | -60.18459 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0ae0aa7-4243-3284-bfab-7bbd47802af2 | -8.22901 | -71.03292 | 2026-08-31 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c61e417-39b5-34ac-b0ad-86bbdd4766e4 | -10.10269 | -68.40439 | 2026-08-31 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a9c098c-ec4d-38bd-9852-07e1957ec1f8 | -8.94369 | -62.37128 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f335d3d-076e-3b8b-8136-0fcb143e190b | -8.67452 | -66.51727 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae25e72d-79af-3f8c-9296-b8688b3db982 | -8.57992 | -66.97221 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18cdacd1-04f1-3a12-a113-43fd81361c1b | -9.93386 | -60.50095 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0e33554-4cb9-3350-a1eb-a14c9168033a | -9.13093 | -65.47535 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95596f22-f01e-380d-b874-dff5f74bd6af | -8.79555 | -62.50166 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d75571e2-a887-3d97-a2b1-5b54e6103e07 | -9.05901 | -65.42181 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 800faa55-56e0-38e0-980f-d6390146c2fa | -8.80419 | -62.49925 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 697a9846-7180-36a0-a603-00fb9efa4a34 | -4.95831 | -55.84776 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6cc61d3-95e5-3742-8d08-de80fd83a9ff | -8.28035 | -70.85833 | 2026-08-31 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c24947a-7661-35e9-8cc6-6664726fe9bf | -10.31397 | -58.08837 | 2026-08-31 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 770b4386-768a-306b-9ad6-76005d8a91a4 | -9.16428 | -59.37291 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6f2d9f7-16e3-3246-a0be-f4bf8c974152 | -9.85795 | -64.98819 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ed7d00c-e4c1-3d0b-874d-a65a03cadba7 | -8.57714 | -66.96818 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc2900b5-2f94-3552-a70a-debbed9b93c6 | -10.44497 | -64.46466 | 2026-08-31 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 265a70d5-23b5-3523-954b-7e5023533795 | -9.85651 | -64.99093 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79b2b69f-8e80-3f54-b03e-f0b3ef79d7c8 | -9.70212 | -65.06055 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c7ca96a-d674-32f9-9aee-7f3b6964d93f | -4.1508 | -60.70474 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0a58ea6-f369-3047-baa7-98970c9f6746 | -8.58635 | -70.64022 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a36e0b0f-7fdf-3a73-8aa6-f0768af8ee83 | -8.8709 | -66.78355 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c64583f-0848-388d-b645-acff840b4e9e | -3.93859 | -59.33013 | 2026-08-31 05:55:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7b56747-b92a-3805-9809-b935e2225407 | -9.05497 | -65.42513 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 769b11bd-11c1-345d-97cb-bbe87f1dffb8 | -15.547 | -56.2883 | 2026-08-31 05:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8d7b39d-d44f-34a0-9f8a-39ff3183fdce | -9.00068 | -65.44142 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47fdd1ad-6961-3a9b-9d88-b4000d86f2b7 | -9.7213 | -65.00569 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fff6e75-e960-3e7f-a089-7d3c271f7a11 | -8.72792 | -70.78493 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc5b7208-33d8-3932-b2f4-3c6418d30dcc | -4.96309 | -55.85735 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44cdf9e3-0f9e-3659-8ed7-74d3de663a9d | -8.7936 | -62.48666 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beb304a3-0e9a-3b2b-8aa7-03409472da22 | -9.05554 | -65.42128 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3d7aff7-fdd5-3be2-a7e0-f136aefcda7c | -3.62902 | -60.55376 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ef7202e-79fd-3ddb-ba3a-d943839dbafa | -9.06075 | -65.41027 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fde1dcea-823a-3dbb-8f26-8001683abcab | -9.19323 | -65.50849 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd7ca18-9fe4-37ab-bf36-aad89fac46d4 | -10.47873 | -59.61246 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa8aec07-6b3c-3c5f-bd04-680cfc29e166 | -4.84599 | -55.82931 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cbfe9ac-9f4f-325e-a8f6-648e45223e3d | -8.7966 | -62.49446 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f483c10-abac-37ee-a6e4-ed0fa963ad03 | -9.94319 | -60.515 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f569849b-ae2c-3e52-89e8-933a08bf381e | -9.05034 | -65.40866 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4059b789-3ca1-376a-9dea-07be1932ba2c | -10.48883 | -59.61401 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0a9bae5-f174-3299-a962-2869245af43e | -8.91499 | -66.95639 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04926a5d-039e-3a3b-a545-0e9d4e383204 | -8.86929 | -70.67975 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4e6627c-7f86-3e08-888b-0ba7e8e08766 | -9.1734 | -59.60839 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01b39481-b9cf-3ba1-b2ea-1d8cc3332991 | -9.85021 | -64.99118 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 003d21af-9485-3e2b-9a0c-67c0f71d5ce2 | -8.67507 | -66.51371 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9175e94e-a575-38de-a348-679985bc6e24 | -8.86995 | -66.89892 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e0aa2cd-9fce-31cd-b8ee-fb04959e125a | -9.05266 | -65.4169 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be275909-9035-38af-a524-289d6a2a46b4 | -9.00185 | -65.43375 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dd24ac9-dc37-3762-bbdd-f0fc3656b868 | -3.25868 | -60.66009 | 2026-08-31 05:55:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba831775-1088-3dc0-930d-36c32fe3fb31 | -8.60315 | -70.21088 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 290bfce2-79b7-3085-bd30-65bf5b913d32 | -3.61064 | -59.0704 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0b1717e-a9a4-316b-acbd-9a4596b56c16 | -9.18851 | -67.7875 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d509a436-c9b4-3ddc-afa9-67dc28779231 | -8.93905 | -62.37437 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe26dfa6-2fd6-3861-9048-b0ee1f06d21d | -14.68263 | -54.91257 | 2026-08-31 05:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 760750d2-5610-3e29-83ef-63a5715b96e9 | -9.71836 | -65.00108 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8421505-6915-3a7f-85eb-c6381954121b | -8.70268 | -69.97845 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8c8fb07-5d6b-339d-b377-874b96076b18 | -10.1949 | -69.34966 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcd3631f-810b-32c4-a746-230e9b2b289d | -8.59043 | -66.97027 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 682f7cb7-a900-3b33-9d64-073bd09ca1ed | -8.94754 | -62.3666 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7c8d108-8e0c-3f4e-b79e-eae8bf48bf95 | -3.62106 | -60.54843 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c68c6630-facb-3a57-9277-2230bc6698a7 | -8.94198 | -62.06369 | 2026-08-31 05:55:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8539cba8-af49-3a5c-bda7-59f7a5316b94 | -9.04514 | -65.44325 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09a4ffa7-0414-3eb6-b988-49b809f960ce | -9.1522 | -59.50209 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5622da58-2d4e-399c-b202-87ad7d89f110 | -9.16468 | -59.36991 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 452f58c6-8ea3-37fe-9697-5140e4be1a0d | -9.14539 | -61.10005 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 909067c3-f1e6-3ed6-ad5d-20967b39f6a3 | -3.62353 | -60.56116 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04b04e44-ded7-35c4-bdd6-237b317eae90 | -9.17263 | -59.61406 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b9c18ba-7305-3eb4-8450-cc168d3be0f0 | -8.63035 | -66.54296 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74297744-22f8-34d5-b3cd-6b84cbd881fd | -8.42236 | -70.14172 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fc54958-8e96-33d4-8cb8-44f2b492db06 | -10.48298 | -59.61916 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44e34343-7b26-3cf4-8656-2f801ac2bd74 | -4.95706 | -55.85664 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea44b535-cb55-39b6-adfd-1bf186629979 | -8.67998 | -62.81855 | 2026-08-31 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c4591b4-ab51-3729-aa1a-ae0168065680 | -8.4477 | -70.20695 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c4a4bf7-4482-340d-8df9-6137f4087bad | -4.15568 | -60.70137 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23d5bf14-be4d-30df-a8f2-f4a716f7516d | -8.90071 | -68.8875 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ba974ef-afa2-30e7-96da-35b2115786a9 | -9.15698 | -59.54239 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47c13373-039c-3094-8cd1-a4c3fe37a296 | -9.94049 | -60.52254 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ee08b35-72de-322b-99b8-d10872635102 | -9.01696 | -65.40466 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3936fa53-5889-34d6-82b3-c6241b3dac03 | -9.44672 | -67.4213 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef17d0a5-1f21-3bbc-a976-564e66ccb8d3 | -9.46154 | -68.22813 | 2026-08-31 05:55:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9962c269-e50c-373e-b052-bfd4d8081e91 | -9.84823 | -67.88966 | 2026-08-31 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bc73296-eedb-39f9-9270-2c8c00ee7a3c | -8.01727 | -71.21702 | 2026-08-31 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78b5957d-273d-3164-b101-84ab7adfcc10 | -10.4795 | -59.6067 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 250518a2-e0d5-3f0d-a3b6-3163a16fdefa | -3.88575 | -59.39707 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 078d3316-c2b1-328b-a691-2a3a2744a3da | -9.78604 | -59.44903 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bc3a342-f012-309e-a9aa-7e507d5fd052 | -9.89509 | -60.28633 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7764b6c2-e053-33be-8774-57a5051fd5d8 | -10.49467 | -59.60886 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ff0a77-c193-3191-af9e-56e5f0c61804 | -9.05959 | -65.41796 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 123e7e5a-ea7e-3d9a-b0b1-2fa77ffd4338 | -9.93788 | -60.50669 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b13ca8b-ea99-396d-bcf7-97472a4d2ee3 | -8.80066 | -62.49506 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README76.md)
