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

## Dados Diários - Página 206

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c847abb4-c7f6-350a-97c0-f937bbf63bdc | -10.5813 | -64.00956 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3ce330a-bb1a-3208-be07-408a11d1a8cc | -10.87671 | -63.90962 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 92058e26-0458-36c0-9a0c-1c11bdae054d | -10.92891 | -63.86965 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c509bec-ef91-3a36-9cdc-243422715055 | -10.92584 | -63.8611 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a44b6e75-5a1b-316d-8b29-0df7b26b290a | -10.92527 | -63.86519 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a46d5db6-5ff6-3c9c-ab49-d387ae31db69 | -10.92473 | -63.86911 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39bb4023-0e6a-3617-92c1-b60505e24d71 | -10.92422 | -63.87279 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c5b2603-a0bb-313f-a61f-79e214138730 | -10.92216 | -63.85691 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fc62a0b-93f8-338b-9bce-1d359dd8421a | -10.92158 | -63.86111 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b9b95f0-d5fa-3b80-83e6-415c0a7cc061 | -10.92004 | -63.87225 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f19bbd47-71fe-3f68-a462-2edbd716f682 | -10.91795 | -63.85653 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17dc7dfc-fb8a-378a-a6e7-b98abb047623 | -10.91531 | -63.87577 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02138539-09af-35b2-ad93-24c1ce0c2b9f | -10.90803 | -63.89774 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a52f2162-c41b-3007-90f6-cfc989c4683a | -10.90326 | -63.90155 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d997e01f-5a2c-3490-a1eb-8b50e74225fa | -10.90121 | -63.91653 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5c1f37e-fa95-3f6c-b1f3-48e09e1a5812 | -10.89701 | -63.91624 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 482ac668-0e02-3a49-9d48-c20ece1f8e37 | -10.89283 | -63.91584 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27a03dde-c730-3a5e-add8-12a300da96f7 | -10.89178 | -63.92352 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da6f9204-7fca-317b-b332-fd4b6f8b5387 | -10.88865 | -63.91539 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5a1a265-4bc2-320b-a1a8-b0b44c65786a | -10.88811 | -63.91933 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c225660f-033b-32d4-a35c-3dad69e46e7a | -10.88759 | -63.92313 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a989d0-6ba0-3388-91b3-f29f0cbf9e75 | -10.88708 | -63.92685 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1a4ef08-cd3b-3742-8f3b-fa3b9e24d0e3 | -10.88449 | -63.91483 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a9fd40c-713d-3e56-9a7e-b5a7cefc1cac | -10.88395 | -63.91874 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d3caeee-e2fb-38bf-a6eb-1e86db2de0ba | -10.88343 | -63.92256 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca650dfb-4fd0-3b09-9f32-fe82dc92460b | -10.88293 | -63.92627 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88c4079c-48f2-3a45-b0dd-ef4bc7429939 | -10.88033 | -63.91423 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7116cdc-0717-3bff-8bda-ef730fb8ba12 | -10.87928 | -63.92194 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce95c0f6-c306-3a60-a75a-09f8434646e9 | -10.87877 | -63.92566 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07850cdd-7363-34e9-a6a5-edc92a1474fb | -10.87463 | -63.92499 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f43b4cd2-476c-3a7d-9e33-664634f28069 | -10.87413 | -63.92862 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67ea2d1b-db45-3a9c-8abd-7dc86a08ef33 | -10.87366 | -63.90076 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af0d6b92-926e-33db-a073-1cb5386cb92f | -10.87313 | -63.90469 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ab66d21-b5ac-33ab-9fdf-c9b4bddb5535 | -10.87257 | -63.9089 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 19d73f52-301a-35a5-8574-8fb148c655b1 | -10.87048 | -63.92434 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b579c3a5-da0f-3f4a-9ad4-bd231e880ad5 | -10.86998 | -63.92798 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7662099-0388-3808-9211-549aea004411 | -10.86952 | -63.89998 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2af92bc2-2751-34a4-86a1-f0cf1b0a3092 | -10.869 | -63.90386 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f7341d41-a6b3-3814-bf7e-ee731dc5ee80 | -10.86844 | -63.90803 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 36f08a9b-45e7-3ec4-8e9d-5d2be4da5425 | -10.86788 | -63.91223 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e79318fe-5029-3ba3-90d8-1d5e8ea22711 | -10.86684 | -63.91993 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbcacec8-98c4-3179-88b6-857339a7e966 | -10.86633 | -63.92373 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9077a74-8727-3581-931f-c0a997bbd195 | -10.86486 | -63.90311 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 42993739-ff9b-3124-8447-dbc7145beea4 | -10.86432 | -63.90714 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6d1143f0-9456-3735-b49c-533c1e1aea56 | -10.86377 | -63.91123 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9e3647e-d093-3662-95fe-097f576180e4 | -10.86324 | -63.91518 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a5e5ba6-7a61-31e0-8e09-9f5024ecf499 | -10.86279 | -63.88684 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9596391c-1851-310a-9169-c591bb78efc2 | -10.86271 | -63.91909 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7f72dce-0790-3a0b-bcf7-475a01f8f58f | -10.86244 | -63.90719 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7af1cd70-5152-3c89-9705-4ad4c7d2ac4e | -10.86228 | -63.89064 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05ec05f8-641e-3691-82f0-864ce206faa8 | -10.86218 | -63.92302 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| babe40c4-96d4-3af7-8450-7d80bf1367aa | -10.86187 | -63.91122 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d0cc2d65-3e8a-3f48-bc55-f666338b362a | -10.86131 | -63.91516 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab1cbc25-96e2-3353-891e-8d9d7b1d61a8 | -10.86106 | -63.88695 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| deb1cfbc-d24a-3255-aa07-9f93048a4358 | -10.86075 | -63.91907 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b85b360f-174f-321f-84c3-04199f0b2083 | -10.86052 | -63.89077 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cbb2f0a-c317-322d-acb4-0565f46b3c3a | -10.8591 | -63.91439 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e8979bf-2835-3f34-889f-38905c9d2f9a | -10.85692 | -63.88624 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6a5806-8096-3d15-8de3-01fc9448d817 | -12.12634 | -63.36002 | 2024-10-09 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7063009-4493-3176-807c-c128e1aedff9 | -12.12569 | -63.36259 | 2024-10-09 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7a8975f-6484-3e54-a4fc-7f944949c532 | -12.05056 | -63.7809 | 2024-10-09 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4709d723-8d18-3cf3-b40a-2a7994926c49 | -11.89379 | -63.28502 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6abf0b97-896d-3412-a63c-89a406654c41 | -11.88939 | -63.28443 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8e929c3-fe6a-333f-ae5d-4d960f022265 | -11.875 | -63.29129 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c460c11e-4059-3699-86e1-ed75093aa229 | -11.87061 | -63.29066 | 2024-10-09 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d3d1489-e29d-3691-b52a-ae9c605897cc | -11.75271 | -63.81108 | 2024-10-09 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74343c0f-d949-3421-b1a5-ba669821e379 | -11.74846 | -63.81051 | 2024-10-09 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e25f670f-81f6-3a6c-83a9-223be5c8866c | -11.74631 | -63.8268 | 2024-10-09 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1244f227-1c49-34d0-961c-81350d870a43 | -11.74258 | -63.82239 | 2024-10-09 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16af489d-92e9-3eb9-8a8c-48d67b3321dd | -11.74204 | -63.82645 | 2024-10-09 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46de8962-7d0f-3b9a-8928-abacf8de2808 | -11.75034 | -64.08318 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5d130ba-f20c-30b0-84a3-20ec3085eb5e | -11.74722 | -64.07488 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2db020cd-8171-3b88-ab7e-98f36e441d80 | -11.74305 | -64.0743 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ecab0df-9266-3018-a47e-0a6179a441c1 | -11.73889 | -64.07371 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4af72be6-10ba-37eb-9c9f-94a3c78b127a | -11.73419 | -64.13952 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 160910f5-7ca7-3eed-b840-32419aacb17d | -11.7316 | -64.06477 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32319036-fe5d-3c7b-989b-25c92a3a6def | -11.73107 | -64.06869 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f07adf4-79d3-3dd3-ba4d-4acca953987c | -11.73004 | -64.13893 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5885bbf6-750f-3e8f-a138-f04dfcbc22e2 | -11.72951 | -64.17398 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42c8df59-92ae-3e55-85b9-863244dbceab | -11.72537 | -64.17339 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c1f557-7275-3f2c-861d-9f513e292f71 | -11.72175 | -64.16899 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba57b0d0-594e-3a50-86e4-f3e19ff763ac | -11.72122 | -64.14164 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 260075a9-a9fe-3b7a-98f0-e39199ae42c6 | -11.71854 | -64.03537 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 897a8123-52ee-34d0-9402-fac257426250 | -11.71803 | -64.03915 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae81a1d7-a2b5-3161-bee3-45d47fbf9ed1 | -11.71761 | -64.16838 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa545d9a-65c5-397b-8345-1af06d4bee96 | -11.7055 | -64.0374 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a795c2e5-6620-3a0e-bc4e-68023dab8b2c | -11.705 | -64.04118 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 190a0aa9-effa-3695-bdd0-cb632640636b | -11.70449 | -64.04497 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a66166e-3001-3e94-b490-f63616c0adf3 | -11.70389 | -64.03857 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e00f5ecc-cfb6-3a60-ae9c-d81cd37cc408 | -11.70336 | -64.04235 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47185eb5-331c-3554-88ea-17d493c14d8e | -11.70131 | -64.03687 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5242a032-202a-33f6-894d-d146f86b814b | -11.69656 | -64.03009 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54f0e037-22fb-3a6d-b404-65b0ee3c0e12 | -11.69508 | -64.01014 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34b8c01d-f91e-3863-ab0c-aea78ba02d60 | -11.69455 | -64.01396 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 76a26728-db53-344f-8cd2-21f28114cb43 | -11.69292 | -64.02566 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1b43aefe-017a-3d55-a55f-b8970c13cbde | -11.69089 | -64.00964 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb7d8069-39e8-39a0-84e4-2aed54a53d99 | -11.68932 | -64.02093 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c9fe177c-910c-3fd6-b7cd-5d5bb381eb3b | -11.68872 | -64.02525 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 65ea73f8-3d38-3aaf-b5d4-cfd2b79ca819 | -11.6876 | -64.03336 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 314fef43-6afd-3f64-8b93-9683f124256c | -11.68722 | -64.00541 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README207.md)
