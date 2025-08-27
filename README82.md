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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecef2948-0ee2-30d2-b25a-66e6e896f59b | -9.19436 | -60.80249 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bccdd593-917f-328b-bdeb-8cc62ad22fa5 | -8.92581 | -65.93929 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 4b0571bc-f738-3052-a229-70ac9356c271 | -8.07038 | -61.5466 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e04e5f-2846-3755-9355-3e333218ef4a | -9.65766 | -65.00146 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 009a9608-fb7b-3c46-8574-a3ba85156092 | -8.92641 | -65.93502 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 3143e8a1-7eb2-318d-9135-a514c8c97add | -8.94717 | -65.94684 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 57c332d9-805c-34c7-9043-62d0ae36f561 | -9.17284 | -59.51823 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9ab0ab5-222f-3723-a1e2-ecb36adbcd6b | -9.17652 | -59.45602 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9920cc67-4048-3c99-a7a6-6aaf422b49cb | -8.89773 | -62.46836 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80b022d2-e7d9-3b4b-b70a-579801d021c1 | -7.53638 | -61.38418 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9875cc34-dc7b-3788-8d4c-7dc7f1c2b2ba | -8.95596 | -65.94808 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ae8c810-2c55-3026-bf24-ce68a3281d1d | -9.1675 | -59.56033 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 910b7d69-94fe-34ce-a274-2e1710d3f0af | -7.54068 | -63.85184 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9386e0f-31f7-3e96-a2e6-3b438facf392 | -8.61091 | -62.64785 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b519e90-8f95-3289-978e-c91c83a32a0b | -7.378 | -64.366 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d51bba97-9f01-3862-ba5a-a76b9573614e | -9.4177 | -60.50841 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b3ce463-bdf3-382f-8faa-2ff585ae29b6 | -9.16568 | -59.54655 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c920374-6d93-38b0-9b0d-1c286fe23b4a | -8.10626 | -71.24973 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a300450-f10c-3c29-97aa-a3ca2392709e | -9.01305 | -65.6955 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4dd987a-def2-3167-a227-cc13fb3158dd | -10.27587 | -64.49264 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c5cce94-5149-35ed-b35a-47b8a09f7742 | -7.74721 | -61.08337 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3f3d8b8-3340-3d52-b9fe-2071f9f57751 | -9.41284 | -62.48482 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15ca70cd-dbf7-3209-9835-6aceda40d325 | -9.15999 | -59.5658 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88aed98f-2974-3995-ab8b-bed2867534be | -9.80847 | -64.24644 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5570d1b-24ad-333b-bad4-a92ad8676e89 | -8.89846 | -60.76662 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84fcb319-2fcd-3456-8317-d0de844fefe6 | -8.96097 | -65.94441 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ad29d749-5d23-3b07-aee5-92b07951b510 | -7.5472 | -63.84118 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1334244-4580-3602-a307-10016814314a | -9.79807 | -64.24797 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 191b3c3c-675b-3bb6-8708-07e7298dfd22 | -9.02729 | -65.7247 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a68a7b08-76d9-3db9-8d72-189190b4adc4 | -8.85074 | -62.44756 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24dfc4eb-2cf8-314a-9a90-6fb4f1d986f5 | -8.34864 | -62.93071 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b31e77d-74b9-3469-a2d4-0a7206b4f99f | -9.0848 | -65.73727 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55fd15ab-d4e4-3a0a-923a-d01c4456dca8 | -8.95095 | -65.95175 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3d1a162-de14-302c-8034-04ebd7c5b10b | -7.99832 | -70.28809 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 849ac978-1152-3afb-9fec-3e5ed097c0d5 | -8.95413 | -65.96087 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 6084930c-182e-3c7f-9482-edd2d2ff2072 | -7.54072 | -63.84564 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fa505a7-92dd-3420-bf36-51be3089d319 | -10.00957 | -65.03096 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 657e5329-88b2-3622-87ae-b0cb26879684 | -8.89348 | -60.76905 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a78b4cc-899e-3f14-a3a6-b830b20701b6 | -9.80347 | -64.24576 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd293fe-9af1-3f87-9fda-4ef8bb882123 | -9.40675 | -62.48779 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abc06677-04fe-3cc3-bd6d-70193989b1a9 | -10.08813 | -62.89925 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d23bddfc-1dba-33ce-bd1a-5c125e8ca4ed | -9.64351 | -64.99248 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c80b28a-86cf-3748-9586-1d065eb5fa56 | -8.72166 | -64.02148 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaa77177-d21a-3c0c-8687-74b4d5d8c86e | -10.09783 | -62.91075 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a0cea83-f7f3-372d-b7a7-46becaa578f7 | -9.08351 | -66.06374 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a9329b-4700-37cc-957b-ba31ecf417c9 | -8.91822 | -65.92945 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3061e8c4-143e-3a5c-a1ef-bb2598aa70ef | -7.48046 | -61.35521 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b893c9-b8b0-328f-ac95-041c4c5826d4 | -9.13557 | -65.27763 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d43a7f7-a601-3826-9c11-d6a04f370a34 | -9.1967 | -59.54542 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9316bd53-29ad-3c6b-9528-7f7a5182c243 | -9.14019 | -65.27827 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d09d9e7d-e8d5-3f51-8b6c-93465bad96ab | -7.54145 | -63.84616 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b512b5-9a23-3976-8ad2-dae1252fbb9d | -8.92822 | -65.92219 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 566c4668-5b62-3ceb-aca3-e97825a65b5e | -9.18049 | -59.45792 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 631fb5ca-60d0-3936-ae68-d7f5e4991e95 | -9.17599 | -59.5175 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 40ac057f-7bd0-3595-b3a8-373ed54764fa | -10.08727 | -62.90586 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ca21cd5e-8a63-399c-a09f-e4a60a75ead2 | -8.10293 | -71.24921 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f90e81f9-51bd-32a9-a767-e3a438e98cb6 | -9.07913 | -66.06316 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 160793e9-9cb3-32f1-ae03-a95ca77aa416 | -9.1664 | -59.54054 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 324abeb9-a8c7-31c3-a468-e4f2a5f3fa63 | -10.09827 | -62.90737 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d3d16b-80af-3c51-862f-1df516fb67a2 | -9.80809 | -64.24933 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c2ee9bf-51a2-390e-8dc3-1b8d42a1df1b | -9.40181 | -60.5324 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7b6e1e7c-f9f5-32e0-b5df-bdd2df1f61ca | -9.41642 | -60.51865 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1426f317-21fa-3b10-9aa5-cd71561241e9 | -8.94095 | -65.959 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 5ed11af4-deae-3b15-bca7-a62e16db99bc | -8.11101 | -62.88095 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 048825fa-f306-34a8-8197-25194c79785f | -8.88727 | -60.76822 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40a9b698-51ce-301a-a4f4-8f821f22e9ee | -10.7717 | -60.78351 | 2025-08-27 06:08:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a24d5814-2baa-3140-859e-07d7e90909a8 | -8.95218 | -65.94317 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07f2f491-60c0-30f5-b7cd-63bc4f464084 | -9.06523 | -66.06274 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b582f90d-6c27-32fc-8557-a9a16f9c9a2c | -9.19328 | -59.54397 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46dbf098-3b5b-3b76-81ba-32f2f47d6e6f | -9.06981 | -66.0661 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c70ab0eb-6d1a-393a-8bca-6507548bcb1a | -8.5806 | -70.11873 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c9fc6e-bebf-38c7-b27b-ba2fbd100027 | -8.71666 | -64.02073 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44a37d47-f19d-3f1b-9920-9b6b40b8e2f1 | -9.80308 | -64.24865 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca19f3c0-915e-3c48-abbb-f9358b671f5c | -8.92762 | -65.92646 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa2b24b9-829d-39c5-bf28-cf0d7362b9eb | -8.90331 | -62.46912 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 882e8f3d-c1e2-33e2-81ba-864705be7bed | -8.08675 | -70.1912 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43b0b005-0931-3d46-8c18-c56d4b172ff3 | -9.40308 | -60.52214 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e79b6b1-b85c-334a-9e1a-21a3bccd0d02 | -9.15605 | -59.56997 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4136d26d-984a-3dfb-8734-4d4d142fc4ea | -7.54489 | -63.852 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd6310f3-2ea1-3c0c-a57b-e834cd880fe1 | -8.96482 | -65.97997 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3adca4ec-d2ec-37d4-8c2b-cd856502aa59 | -9.40245 | -60.52723 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4875829e-02b5-3842-ab75-e94892a53ac3 | -8.53503 | -62.66609 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d976851-ed15-377e-98a8-0d36797e0ae0 | -8.57716 | -70.11819 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee2d5aed-46ba-37bd-b60f-1b051c7510de | -10.09365 | -62.89985 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1813d8d-b7a3-3e2d-a68f-e5404fc35847 | -9.2353 | -60.91914 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a574c3-0387-3bcb-a6ee-88e1c7198cac | -8.95156 | -65.94746 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 970782c4-31f4-30bd-8a24-59d5a82ffa40 | -9.00523 | -65.40643 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083a8a43-6417-3b47-91c4-3e99a62291a0 | -8.09905 | -71.2522 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fcd448a-fa1c-3d1e-84ef-31d341616986 | -9.40436 | -60.51183 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f3ca647a-b95d-3ea0-8979-1960914e5341 | -7.47432 | -61.40158 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1add991a-a572-3a94-9dc8-f10560182241 | -7.62018 | -61.0379 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe25925-2b3f-3d02-9859-74fe2358e713 | -8.85172 | -62.44011 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e02a01-4e36-3d8c-9a6c-b5b202b31ee9 | -9.08282 | -65.71902 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90a2484b-9e99-3950-a1e5-c2b797854e12 | -9.40943 | -60.52296 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c126e9ce-521c-36ce-b1eb-dccbc881afc7 | -8.96506 | -65.94817 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 69f81ddb-0d62-3e80-8b0b-c9dbe424215f | -8.95891 | -65.96038 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a50843e-c3e9-3a04-b5eb-f22535d2befa | -9.16422 | -59.55871 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5c1b8414-e9c1-399f-b92b-ad4e8e6ead66 | -9.32793 | -63.20424 | 2025-08-27 06:08:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93e60edc-31c3-31b3-9fc4-bd0ff69d791d | -9.184 | -59.45085 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb8cd0ec-47c3-31da-858a-2f864f33d4de | -9.40575 | -62.49536 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README83.md)
