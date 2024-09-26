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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f3c64ef-298f-3778-bf36-63000979f127 | -12.09026 | -60.90801 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f30eed5-c2f8-3c7c-a124-fbb709a5e939 | -11.50854 | -60.37785 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ef581cc-36de-34c1-88a2-13077f3ae68d | -11.50817 | -60.23911 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b98b409d-7164-3bdb-a2bf-a7948ecabbc2 | -11.50741 | -60.24341 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2c48bb9-92e8-3829-9d08-e586eb325a76 | -11.50115 | -60.23256 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6c339fe-b13f-3aca-999a-cbb3d394a13e | -11.49898 | -60.22168 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97243436-adc5-32a5-954c-665892203181 | -11.49808 | -60.22676 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfb99f19-6e42-3178-82e7-060dbb5e8b37 | -11.49716 | -60.23198 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9cb7cb4-1c5c-3066-a209-e833fd1c21f8 | -11.4929 | -60.20982 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36c7702e-a92d-362e-8e4a-7f302df25ffe | -11.49197 | -60.2151 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 632e21b9-2e3f-31ba-a956-5272c9204d91 | -11.37271 | -60.38955 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e0ee5d7-124a-3cf8-adc5-bf344e2505cf | -11.33028 | -60.58278 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd3b1c46-bd36-33aa-80eb-193be3de179d | -11.29552 | -60.61506 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4ea339d-edeb-333a-b627-074e948b7bf9 | -11.29527 | -60.59207 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6a1f65f-e588-390d-b4cf-f76e1a0af604 | -11.29519 | -60.61488 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84432354-c257-3732-a230-49b9b05ba13b | -11.2912 | -60.59137 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0293592e-d42a-3484-852c-32375d87ff8e | -11.2859 | -60.59781 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| daab5f3e-145d-3eff-a822-4297e901faa3 | -11.18521 | -61.2035 | 2024-09-26 04:59:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| debbb625-cc58-3d24-bb27-d2597534da0d | -11.16386 | -60.723 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd6bd30a-9856-33c0-92ff-2745d05f9a8d | -11.1591 | -60.72604 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a15ddc9d-9749-37fc-8c1f-e77bdda1dbcc | -11.15245 | -60.66669 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00b44dc8-bfa5-3255-aced-c99304bb641b | -11.14965 | -60.6585 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 89e7368a-5997-3045-9186-c908eee64116 | -11.14899 | -60.66229 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 062903fd-255f-3fd6-a0fa-2d597c8784b3 | -11.14835 | -60.66601 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 460b2654-6a65-39a6-8673-2f83bb97c8c4 | -11.14273 | -60.64975 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 976730cf-a182-3e37-a5f1-964bd21bec60 | -11.14209 | -60.65342 | 2024-09-26 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ace15751-96ae-3be9-8b75-a84b6042e4f0 | -10.99984 | -61.41292 | 2024-09-26 04:59:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 035a1025-e3af-33e6-8ce5-95facd4fb3be | -10.92553 | -60.92477 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e07485cd-251c-39c6-aec2-e8e947502fd7 | -10.92483 | -60.92866 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c48108ec-5297-347d-a4c0-16eb905f0078 | -10.92414 | -60.93253 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cbc4bda-f259-37be-9527-f45a82408cb1 | -10.84494 | -61.37212 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2854c496-da03-366a-acbe-3210b7bc1ea3 | -13.52095 | -61.41643 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db5ea569-d121-38d6-b044-be2a3bdd2bc7 | -13.50027 | -61.27121 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ce76612-e832-349b-8e57-1d3adbef8664 | -13.49959 | -61.27497 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 29d15186-e60d-32bb-a525-152fec86e70e | -13.49686 | -61.26668 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c0ce907-649d-30b1-88b0-598b30e0e6d3 | -13.49617 | -61.27044 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c43adefc-9dd0-3537-99c0-f244aa3a0e71 | -13.49549 | -61.27422 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50b77bd2-3100-3ae1-9c9e-c0b9f774757d | -13.49481 | -61.27798 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb845890-afcc-3bab-91f9-0625b192f2b2 | -13.49345 | -61.26216 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 58e75ce8-cdcc-34e1-8109-dbba9fbec5cd | -13.49276 | -61.26592 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ce69b81-5dc1-3417-ac8a-dab1b196de6b | -13.48867 | -61.26517 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0177f6a1-1450-39d8-9e10-0608f9b2c30a | -13.48731 | -61.24937 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf193ed4-367d-39b3-9d84-c41039dbd06c | -13.48662 | -61.25314 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bf0ac99-e6d8-3795-ab5e-c57d62a8b91c | -13.48524 | -61.284 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14231376-f300-307e-8087-615c706395a9 | -8.96756 | -62.14058 | 2024-09-26 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91f8caa3-d294-3b43-8794-9dfc7a3a1439 | -8.95819 | -62.13884 | 2024-09-26 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73d59456-9aed-346a-bda4-5d2e90f0fa25 | -9.13011 | -61.35101 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c52f1a7d-95a2-395c-b96e-4f3286c8bc05 | -9.12854 | -61.35983 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc098f12-dfa0-3ab3-af95-87f6e92d5f60 | -9.12411 | -61.35906 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 199057d6-63e0-396a-a41b-c35321492140 | -9.12359 | -61.33627 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b6aebdc-e602-3d2f-980b-09b3e7d3a2da | -9.12202 | -61.3451 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff49464c-c27f-3452-94e0-15bd0b2fe728 | -9.12153 | -61.32221 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99a057ac-236f-3cc3-8611-016ae2183474 | -9.12103 | -61.29947 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9391b04-b9c7-3c21-9688-581977c81583 | -9.11867 | -61.31266 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46745a6c-e5fb-39d8-b115-23013852991c | -9.11847 | -61.26456 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57ca12cf-b26c-3df1-9a9a-4d4d852efd73 | -9.11846 | -61.26292 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a549c4a-40c8-368a-977c-79fc75afca3e | -9.11789 | -61.31705 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 007e2ea3-d01e-3b21-a476-49053906d8c6 | -9.11758 | -61.34434 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01943b07-35de-3296-83d9-519882667a7e | -9.11639 | -61.45422 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0df323cb-bfb0-36cb-af19-a6207cdc96fd | -9.11632 | -61.32582 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7cbe227-7db4-3746-8e66-4391e34a1d70 | -9.11554 | -61.3302 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fc82294c-ee80-3ebf-aca4-70bca65800c9 | -9.11475 | -61.33463 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| faa25e3a-03b2-303e-8da1-0563e4a5cd98 | -9.11395 | -61.33907 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8b8c4b27-3903-3cd5-b6df-ef8532c14a14 | -9.11346 | -61.31631 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afdc8db8-a1f1-388f-b580-b644ecf26742 | -9.11249 | -61.27085 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc67ebd9-7556-382b-aad8-9b6981fb9a23 | -9.11236 | -61.34799 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a876d02-f755-36f5-bcf9-f0e14a41dd85 | -9.11192 | -61.45344 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef6bbe23-3016-3b94-b55d-d117a6d2adfc | -9.11111 | -61.32942 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6caf328f-292e-3247-a84f-dc1b2f67af99 | -9.11085 | -61.33569 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f1bdc62-a93e-3ed2-a936-0a00f75e06b0 | -9.11032 | -61.33384 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac74a65f-4800-3e5f-8060-6d64c1a2c8bb | -9.11008 | -61.34017 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ddb454a6-3037-3390-8613-0cae49bd11a2 | -9.10964 | -61.26139 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acd00f8f-88dc-3798-924c-6f62af07999c | -9.10953 | -61.33828 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5271576a-8446-3758-8004-fa778be0ddeb | -9.10867 | -61.32176 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7c886a4-3928-3b75-8df9-4d05b96029ce | -9.10856 | -61.34909 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2f1b2a9-ed83-3642-accb-93d2f8905d40 | -9.10808 | -61.27008 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 301bbb2d-c503-31c3-881b-5d081f1ec5da | -9.10792 | -61.32614 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a546c4fa-4f9b-3dab-ab59-40f833df8596 | -9.10717 | -61.33053 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09020ec1-37e2-3909-8c67-922d64b65530 | -9.10641 | -61.33493 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21eb9a26-d412-3455-919f-3da0ae98d057 | -9.10588 | -61.33311 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6783157e-0c68-3879-b0a6-f6e8afee9e52 | -9.10565 | -61.33938 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb7a5d2b-9fe1-3d53-86cf-57950f67476d | -9.105 | -61.31657 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87cd0caa-ff8e-39a6-8a3b-a2c9be44aeb5 | -9.10488 | -61.34388 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c189d1e-1083-3596-a5d9-73562493314d | -9.10449 | -61.26659 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 399242f8-921e-38a5-8a9b-9418ffdf03c3 | -9.10424 | -61.321 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f952260-b3ec-3d91-8bdb-f033bb30aa76 | -9.10381 | -61.3192 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43b8c651-981b-3b81-8526-7ba8ba08c78d | -9.10349 | -61.32539 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 524a5c3d-6871-3e58-a275-53406f6e0620 | -9.10302 | -61.3236 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db97e8a1-75f8-34b3-ba06-6fb4dd12f72a | -9.10121 | -61.33862 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5536d26b-776c-36cf-81de-3c2958f2e21a | -9.10065 | -61.33678 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ac94f76-f940-3644-af7d-7e76da5c9b68 | -9.10018 | -61.314 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7c8486d-7043-3af5-815c-e02e9f9a44c8 | -9.10008 | -61.26582 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56aa4f60-5f85-37e3-91b8-cda9315edf42 | -9.09985 | -61.34122 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6e0356f-5727-3d28-9a66-37ce2bcb2b65 | -9.09981 | -61.32022 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59325ba1-be22-381b-b4d2-1aa252a1feb7 | -9.09939 | -61.31841 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6f1eeb2-1ccd-370d-85e6-dfcb19a46a89 | -9.09932 | -61.27018 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bf56a0b-b62d-3dfc-8f26-37c6ae40ac87 | -9.07731 | -61.37119 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd85504a-2913-3fe9-b070-d33221d46e67 | -9.06766 | -61.37395 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e032e48a-ecf7-3f22-b866-3cb0c38ea75b | -9.06168 | -61.382 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 837670db-621a-3390-845b-14feb7c11147 | -9.14653 | -62.41759 | 2024-09-26 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README139.md)
