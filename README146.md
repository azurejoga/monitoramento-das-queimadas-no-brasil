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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8393c8-bf53-39fb-b0cf-1ea511929227 | -9.17552 | -62.29628 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25289b43-7946-36ff-af4d-20cead14d04c | -9.17521 | -61.57552 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c16a39e7-ed56-39de-bbea-8b2070af0f5c | -9.17466 | -61.57909 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c542861-99af-3423-b176-a0d8c3a41a1c | -9.17186 | -61.575 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 904c9b40-a966-38ca-bb5d-c6abc51d2d7c | -9.17131 | -61.57856 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5396cf1-da4f-3764-aab1-78001ac5bf62 | -9.16852 | -61.57448 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9421f984-6652-31ba-8434-fc8eef42ad76 | -9.09348 | -61.13116 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cda04b2c-51ef-3d52-a9b1-de8fd9d13e71 | -9.09293 | -61.13481 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 714076b2-a19c-3a7c-8ef2-60a29452cf2a | -9.09237 | -61.13845 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45a8ec8e-e926-3927-9f7b-f69d27c2ff37 | -9.0901 | -61.13064 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f532965c-e4d7-3e38-ba66-abf473ed34c1 | -9.08955 | -61.13428 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1cfbf302-3214-3560-9dd9-926c708d3a0a | -9.08493 | -61.38932 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de89af29-fc3d-3f71-9cb4-944c19a9d51c | -9.08157 | -61.38881 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47948654-425e-3c05-be57-d1fad721c9c2 | -9.05613 | -62.34171 | 2024-10-05 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaca63e1-45bc-398a-b63f-6832b00af326 | -8.97552 | -62.4678 | 2024-10-05 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35092848-54a7-3c02-9423-f0972e0b9874 | -10.19959 | -62.18555 | 2024-10-05 05:31:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8600ff6-5009-3a4a-a54a-024a76951ab9 | -10.11666 | -62.76416 | 2024-10-05 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 272456eb-60ae-35fa-a5e3-9fd1c407151c | -9.69838 | -62.17175 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2334a406-c821-3920-8a46-8bac83d1db98 | -9.69507 | -62.17123 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e53131c6-dd6a-3167-9591-1459da0b7999 | -9.6925 | -62.25343 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 795cce4c-465c-353e-87d3-c7a3e395a880 | -9.62424 | -62.30003 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0b4c905-8a13-3010-9271-ad89c4351a13 | -9.53773 | -62.04524 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fcbf66c-4be5-3c26-b077-fcfdcb5964fd | -9.4727 | -62.35425 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b0c222f-55e2-3fcd-95d3-f1abb40e559e | -11.68872 | -62.40645 | 2024-10-05 05:31:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c7188a5-5db3-3625-99a0-0bb7b4c202a2 | -11.70266 | -62.73499 | 2024-10-05 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 030e8a5b-2465-3dfa-803e-e50566c0c0b2 | -12.91544 | -62.45289 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddf275da-5adc-36c4-b231-f294d5ee5835 | -12.90876 | -62.45184 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 14c44afc-8622-3db8-b606-827cd4ab7474 | -12.90596 | -62.4477 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9dac9aab-bada-30aa-b7e5-ea7210fdc8f9 | -12.87533 | -62.44653 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e9636162-b8f8-3d34-9a9a-dd3ca741a315 | -12.98214 | -62.68396 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b9e4628-e357-35b7-9e25-0f13a092fb48 | -12.97826 | -62.68701 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bd19e0a-c597-3750-9c93-b3a05826eb7d | -12.9283 | -62.4808 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dd6e8b56-beab-3a4c-ab78-bfad5ba958ae | -12.92606 | -62.47306 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| eb94b639-7b29-34bc-b774-7f2dcf758585 | -12.92554 | -62.49883 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9aab8109-25b2-3f29-8a84-5bd87b8ebb7d | -12.92551 | -62.47666 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d34b0870-155a-38d2-aacf-251aee9d38b2 | -12.92496 | -62.48027 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 723cf11c-3c09-3d77-96f2-b74a96281663 | -12.92441 | -62.48387 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3a1f0cf8-115f-3363-b129-9776bb2cdafc | -12.9222 | -62.4983 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e98924a6-54be-3bc8-a7c5-bbad119da907 | -12.91993 | -62.46838 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e60dd7-a17d-3952-9a79-f3afd72405ee | -12.91658 | -62.46785 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5ba895e-206d-39a6-814e-cba21b3f102e | -12.91324 | -62.46733 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42d27631-85c6-3618-bf3a-1012174a5c85 | -12.9121 | -62.45237 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce82bae8-b5b7-3ef8-a29f-fc249d131ba0 | -12.911 | -62.45958 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16707655-5d85-31b0-815c-089033ba338c | -12.91045 | -62.46318 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204d7105-374a-3005-8923-be81166bc230 | -12.90931 | -62.44823 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c3f44198-9aa1-3b6f-a8bd-8269e932e705 | -12.90541 | -62.45131 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2538e47d-6571-30bf-a43e-c7bf22e3d9d7 | -12.88481 | -62.45173 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd6ace45-0605-335a-9864-5a12d26a8e38 | -12.88209 | -62.78188 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 767c6ac6-4d6c-34df-b693-a1e6441705d7 | -12.88146 | -62.4512 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| df4f6572-5bc1-3b3a-9237-188802bea219 | -12.87812 | -62.45067 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 342399a1-38f6-3451-a2be-2ee921cbb621 | -12.87478 | -62.45014 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| dc443b1e-f9c2-3672-a379-1d3a9fef8da8 | -12.87103 | -62.7874 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2467af38-48a0-3ee9-b03f-e9dfbc813289 | -12.84836 | -62.80202 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb846ddf-72ac-3bef-befd-f9d3598ab354 | -12.84558 | -62.79793 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06566207-4e77-35e4-9fbd-e4a5dbc176fd | -12.64193 | -63.10262 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4131580e-7d17-372a-8cdc-60c6b0b92c44 | -12.64138 | -63.10614 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a29a3742-10d8-3c81-8a70-322bf5527de1 | -12.64028 | -63.11319 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15392d8f-966d-34ab-945a-32e4e109cf4c | -12.63917 | -63.09855 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d5ea07fd-763a-334a-970e-ce20762ff49f | -12.63697 | -63.11266 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8de8bd14-086b-374f-96e7-35a9cd80b2a3 | -12.63531 | -63.10155 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2626cf4c-e3c5-393f-a9f2-668a91df4445 | -12.63476 | -63.10508 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45954395-c26d-3a06-bf8a-4b57a18275df | -12.63421 | -63.1086 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0b2bb19-4d9f-3654-96c7-96a8e5bef300 | -12.99051 | -62.71829 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7e1fefe-01ad-365d-84fd-884c1b232d67 | -12.98269 | -62.68038 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57b44583-0dd0-3d62-ab4b-c79b2976984c | -12.97772 | -62.69059 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce02abb1-a097-393f-aa6f-271d0ad34130 | -12.87877 | -62.78134 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5304671a-9465-3b09-8ef5-1bfb4cee63e3 | -12.87435 | -62.78793 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af94cdd6-35ed-3ef0-894e-b8bb3c636f90 | -12.84891 | -62.79847 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38ab08fd-ada2-3a0c-a177-66892e9638f5 | -12.84504 | -62.80149 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a73b769-0a35-374e-a1a3-14d7aa5de89f | -12.73205 | -62.93943 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56d788f6-f054-35ab-bb70-a82e2b6df167 | -12.72928 | -62.93535 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62bd9412-bd91-3854-be36-c6db66fbcdab | -12.72873 | -62.9389 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40db0205-534c-3d29-9f4e-1757f8d40ae6 | -12.72764 | -62.94598 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7882ccd3-b232-3f84-ae52-0e744bdaa934 | -12.72542 | -62.93836 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 787beac6-84fb-3c9d-93fd-dafc9ef78897 | -12.72211 | -62.93783 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3327de37-75c1-3826-a36c-e37729f4dc92 | -12.71992 | -62.952 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be8ab8cd-e122-3a8c-bf1f-687521a923b8 | -12.71824 | -62.94084 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd108a86-4acf-38ac-9935-2150f3626856 | -12.7166 | -62.95147 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e20b560b-0dfe-3cca-b55e-c8e093b93320 | -12.71162 | -62.93979 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69c10156-0b8f-3004-ab8c-04d9cc5ea002 | -12.71107 | -62.94332 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e1f7cef-f491-3d9b-92f6-19120f15def1 | -12.70132 | -63.07221 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20c23a34-bb34-3b2d-ad2d-a0009754cf09 | -12.64247 | -63.09908 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 97419e16-ef05-31d1-b081-00ce91558f6f | -12.63643 | -63.11619 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfec57f9-8320-37a7-90c3-119f5d784627 | -12.63586 | -63.09803 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b73112d-8a9c-3e28-ad92-afc66b249a6f | -12.63367 | -63.11213 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 065e4517-6c97-3bf0-bc09-e98be6e88047 | -12.63312 | -63.11565 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37e01efa-9e71-3270-ab55-5c1ded2afdc9 | -12.62817 | -63.12569 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e44a6e7d-9d02-3dba-b5ab-12f169bf1b16 | -12.62762 | -63.12921 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c311c1ee-20c0-392f-910c-838812ad733f | -12.62541 | -63.12163 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0891ad5-8eb6-3f37-ac2e-8abdc029d7e3 | -12.85223 | -62.799 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19f85046-1dd3-34f2-8f55-0a9fc67749f8 | -12.84172 | -62.80096 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd4bced8-05be-3608-88aa-63cda9db388a | -12.73968 | -62.86799 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017a99ab-066c-3697-bb2e-db1414fff34a | -12.72597 | -62.93483 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 254fea5e-d7fd-3910-8070-d1c5bdd047b4 | -12.72432 | -62.94545 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ef53f65-7858-3030-a473-cea83e528630 | -12.72156 | -62.94138 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b5c2c9d-2f59-3100-bdba-9c9faad1a97a | -12.72101 | -62.94492 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa0d79f8-413c-30c7-9fe8-dd49a123afc0 | -12.72046 | -62.94846 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 859861f7-b3a8-3144-99d1-73c4edc43d4d | -12.71216 | -62.93624 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d3c16c0-c645-3392-9cdd-e4e6ad2b1030 | -20.63278 | -51.48219 | 2024-10-05 05:33:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| f42a9fa3-2705-3142-ac1d-4752bd1280c6 | -20.58331 | -51.39479 | 2024-10-05 05:33:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README147.md)
