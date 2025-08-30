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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1c10edc-b507-34b9-8e61-a6c69a06d047 | -12.6953 | -48.14303 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2834a5b3-d530-3e78-a335-41c302301f15 | -13.37312 | -46.97905 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d1030ad-22b3-3d66-b573-7a01dfebbd34 | -13.38404 | -47.0027 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1af28b7b-13dd-37f2-bc02-e703adc20b1c | -12.8991 | -48.88189 | 2025-08-30 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2de95661-d3d0-36e6-9679-894e95ec35d6 | -12.61421 | -57.01438 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 367bf785-a698-307c-aee3-1597e14f05ee | -11.33719 | -63.29922 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f26fede-c3cd-374c-bf55-65b86aa85c84 | -13.46555 | -46.96589 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507d1712-923a-3b6b-8da7-133923cfc899 | -13.63628 | -48.13251 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf8be283-7826-3b2d-84b4-f641a23cd497 | -13.38868 | -46.99967 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc252173-5d2b-3427-a380-08f9fee68417 | -13.37924 | -46.97484 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d05a564d-d229-3068-8e70-b4207b8fba0e | -9.674 | -65.02182 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85624d63-93ee-3c55-b52d-d16155d23b07 | -13.62755 | -48.19356 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5befe04e-62f9-3493-b5c8-2399647a2544 | -14.54285 | -49.15702 | 2025-08-30 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef611e42-7034-3535-bb0b-35b326d1e563 | -13.69229 | -46.90891 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19637c5b-1b24-30ca-81f7-05e8695dff69 | -12.65798 | -48.18626 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74dc4396-2e3d-35ab-a0c9-b8a1d155a45c | -13.39418 | -46.95848 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07f7b21c-42f0-3e35-871c-3c24a30addb1 | -12.84386 | -48.13269 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8e4e1c5-f1be-32be-bbc8-3f4508cbbd74 | -14.23442 | -48.06781 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c62666d-cef5-3afe-8c4a-e5ce105e8520 | -12.98218 | -54.76039 | 2025-08-30 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2da00c14-19e4-3fe8-b714-577a8f793d91 | -13.59185 | -46.89054 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1d08929-58a7-329e-8e26-a61be52fe1fe | -13.40091 | -46.84326 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c71e878f-c93c-3357-9542-5cebcd061da0 | -13.35806 | -46.87193 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a31369f-9fae-3d82-8e80-460cd9a7bcab | -15.06155 | -48.38958 | 2025-08-30 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b578972c-e999-3977-851f-91a6051da8bd | -12.92294 | -46.36016 | 2025-08-30 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eee8b814-c826-3411-a376-2acd1beccd49 | -12.9787 | -54.75978 | 2025-08-30 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8d198f0-445a-3963-92d1-5da1606e5342 | -14.45847 | -52.00979 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48e6486f-0759-3027-9171-299cd3e96853 | -14.00336 | -44.56968 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27fa3b25-4012-33b3-a125-e2e09efae6d2 | -12.69982 | -48.13881 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e067070a-fe05-3092-9a33-c5f06274c9a0 | -13.36288 | -46.86803 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2efcd70d-1f9f-3db3-8579-7794659538fa | -14.34285 | -53.29972 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3bbdb07-5725-3d25-b835-3a3ec0670901 | -14.56161 | -51.99648 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b2551a3-03c7-3ea6-a44b-72c1f7e19621 | -12.69463 | -48.14788 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 802479f4-3ffa-3c99-94b7-f491e5f5a23d | -13.38771 | -47.00697 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02a39d29-ef17-35d4-951a-3c71b0ff0462 | -13.19839 | -45.28173 | 2025-08-30 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a4b4b42-f68d-356a-98b1-f8dcb36f1fcd | -12.65445 | -48.19845 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a31273ce-f545-3a9e-8cda-a53429ffa207 | -12.82205 | -48.12008 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0aeec151-15d7-3706-9e7c-19167fe90838 | -13.67836 | -46.91679 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a4f60c4-2e0e-3a9a-b09d-ef5e1581543f | -13.365 | -46.88374 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bf420f9-3522-3754-9470-b9b6f8b642a3 | -13.01259 | -48.72541 | 2025-08-30 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ecadeee-41c8-38ca-8f28-424fcef88153 | -13.53634 | -46.94993 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 895303a9-8b0f-3dc8-806f-d9641168b3a5 | -16.05047 | -49.04019 | 2025-08-30 04:51:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b65f7e5-e046-3b01-b2ff-954d7fdaf1d5 | -13.62899 | -48.18348 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c54f54e-f5f0-3b8a-bc44-b548741d4e4a | -13.66464 | -46.92315 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0441136-572d-334f-91fd-0d8d5d57039e | -12.85272 | -48.15326 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0c12eea-a721-3296-8167-adbe4ea2400c | -12.84923 | -48.17767 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e0ce4982-da81-3da4-a031-46589b5f5db4 | -13.45248 | -46.96804 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58089a91-0281-3b01-8318-ddbe21f9017a | -14.50138 | -52.05327 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5062a037-1ac1-321e-8197-96e153b54775 | -12.65601 | -48.20053 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea9d7af6-b135-3c45-a262-e8fdd227a7ce | -13.38917 | -46.99601 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 87385c08-5986-39b9-8800-1d5c824676f9 | -14.04291 | -44.49313 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a259195-3db4-3e2b-b1ac-5b4aadd7bf71 | -14.23833 | -48.06853 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fc94a1e-86b7-3f41-865c-dc9f5dbd7862 | -13.6872 | -46.91478 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0fd12d4-b50a-3b37-af1c-3972ddfb5b4b | -14.84949 | -46.77735 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ad3fee6-909e-3972-a1ff-8c1b2f9e94c2 | -13.3882 | -47.00327 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 627bca28-7b7e-3f3d-90f1-2b860496f111 | -14.02228 | -44.49636 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51040f79-b086-3b0c-8371-8b9a2df261d1 | -11.30715 | -63.29284 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a979716-9932-3529-a9d7-c54978c8476e | -12.93865 | -46.14701 | 2025-08-30 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0e7bd15-31c4-3897-982f-f28a92e58fee | -13.36932 | -46.98559 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fcf0006c-aff8-335a-9084-dedbaba359c5 | -15.10469 | -48.19285 | 2025-08-30 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 826cbe5b-bb41-377a-ae77-79d9062111cf | -12.85225 | -48.12898 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36efa64c-c480-3049-8630-bcbb8e2fbde9 | -14.53196 | -53.00827 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9d72bfe-558d-3e5f-94d5-b81cc68eeb5e | -14.2503 | -45.2436 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8489000-54fa-345b-8058-99136f803ad4 | -13.35758 | -46.87545 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f807a747-13ba-37dd-8a04-b1734032ef4b | -9.75976 | -65.09274 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b153738e-97a0-3c3c-ae55-4213799533a0 | -12.84537 | -48.17726 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a80a3e3-31f8-3125-b977-3c99ce9341a0 | -12.69598 | -48.13821 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8225cb20-e433-3556-8a02-19cdc29b1cc8 | -12.84518 | -48.12333 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d040e98-0bb4-37a9-84fc-2996045b01c8 | -13.65286 | -46.91522 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a09837bc-17b9-39e6-baed-2bea710a27ce | -14.00806 | -44.56845 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17b40349-4c68-3758-880f-5030b031c342 | -9.72414 | -64.91384 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f35a54c9-2565-3e01-a7c6-830d696fccae | -13.49108 | -46.83953 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b2efff-ae36-3084-aedb-5181bbdf7828 | -16.537 | -55.04185 | 2025-08-30 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 41750acd-3f28-3256-bcf3-6743a064d0c0 | -13.36436 | -47.02316 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b8c00ec-7d45-35d8-9b09-854ed725ae9b | -13.39035 | -47.01895 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ae78236-8e93-32e3-9b47-ec16dc1283db | -14.25161 | -45.23969 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f506e253-48ae-3991-95f3-8ff149f61458 | -13.38416 | -47.03352 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b84e005d-ee4a-31d1-b0c5-752aed2e6b2e | -14.04077 | -44.51065 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b853022b-ed25-339a-8153-d5682bcf3064 | -11.30068 | -63.25605 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6aff18e-fb63-3c94-b6a4-98c6e9a0a492 | -15.62058 | -48.72687 | 2025-08-30 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85e3525a-b066-3b4e-bd01-7ba069d21d4c | -13.42968 | -46.94783 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c75fa09a-9704-3f94-b832-e6f87b8a8185 | -14.10439 | -51.77881 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80f4a008-5b44-3c55-87e9-ad861f85af22 | -14.45123 | -51.99012 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bc463da-83c4-3a08-8997-bffc62cebf01 | -14.84467 | -46.74697 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fac5525-2d03-32fc-88d1-70c56bc4eb3e | -15.216 | -53.80486 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a3c0186-95c1-35e4-8514-538ac5338dca | -14.00405 | -44.56398 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1294419-bc42-32bc-9369-f1117870d973 | -13.68347 | -46.91069 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce3b48da-e1d1-3fbf-92db-a5e99d0d903f | -11.39172 | -63.24422 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d678618-f96e-34f6-bae7-b9e51f68e3cc | -13.35564 | -54.38713 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8909aeeb-90c2-3a34-bff7-50ba90cf4c1e | -12.61901 | -57.01009 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea47cd97-b4e3-32ca-a9aa-74c4053e5341 | -13.36732 | -47.0206 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb16af10-13a8-3b8a-9d30-8b8f5146ae9b | -12.84838 | -48.12849 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39fa91e6-bd65-34c6-91ce-aa8096f4d1b4 | -13.37104 | -47.00468 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 465b09b8-3470-3fc2-8e84-403ba482aa5b | -17.44757 | -44.4892 | 2025-08-30 04:51:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3443e825-5dfa-35d1-ab4a-23bffa56ec93 | -13.62418 | -48.25488 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 552ad858-dca7-3f46-9693-2787da127b92 | -14.02258 | -44.49457 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b8143bc-839f-356c-b4bf-0265d8c138f7 | -12.52604 | -53.13074 | 2025-08-30 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b862058-09b8-343d-baaa-9e3ea40e9d63 | -15.07722 | -48.15769 | 2025-08-30 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 603c419b-96f9-33ed-a8ff-9ff941805e1a | -12.93042 | -56.97432 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd717738-221b-37f8-9b93-ff191721789e | -14.03934 | -44.52238 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c36948bf-061b-37b7-9dcf-374508246a04 | -13.4829 | -46.83996 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README59.md)
