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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4c54600-4dc9-3551-aa5c-64123ed6e6ee | -2.94377 | -49.35507 | 2025-11-07 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cca3950b-cc6c-311c-a449-5739e629a0a2 | -2.94466 | -49.35249 | 2025-11-07 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2cb4cf0-1e65-3ad5-a17e-23341f4c66e9 | -3.67216 | -50.492 | 2025-11-07 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86f482bb-e51c-366c-a47f-de7f39a7718f | -3.52927 | -47.55016 | 2025-11-07 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f1b8347b-3222-301e-b6e3-b4e73e32db2b | -3.35413 | -53.22215 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 87b9b3c7-1289-350a-87ba-5f96ef833a08 | -3.54296 | -49.44151 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c23b16f-4e63-3692-8165-420a8276c8a9 | -4.44604 | -46.44573 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef95421c-e47c-3257-beaf-041d1a389084 | -4.4532 | -46.44183 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8336e6e5-769a-3a02-8268-de6c710d4c43 | -4.4953 | -45.13609 | 2025-11-07 05:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f689007e-1062-3425-9ba2-d57924daed82 | -4.45445 | -46.43815 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 586c6b15-f082-3a1c-a79d-542eb139d589 | -3.11873 | -50.14701 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a8d13425-5e09-36cc-b1da-e422de1bb513 | -5.2785 | -47.16561 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b062a43d-bfb8-3bac-8450-81452809aaeb | -9.00387 | -51.1055 | 2025-11-07 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b44e4c4-022b-316c-b740-3333dd5d38ff | -4.28835 | -45.89049 | 2025-11-07 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 075aa875-9692-308c-9512-68602d01555c | -3.33725 | -50.20045 | 2025-11-07 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62e30136-c216-3529-a187-e501293ca3e3 | -5.27687 | -47.16582 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1456e4e3-ca59-3a28-9dd0-d520fdce685a | -4.42441 | -56.14098 | 2025-11-07 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0235e511-4e2a-31ac-bf45-34d19086fa39 | -4.67787 | -46.30961 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56a9627b-796a-39eb-8913-d6f542d9eaa5 | -3.5963 | -49.44339 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b460698a-1282-3560-9ed1-0843ef85bbc6 | -6.04472 | -57.69416 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2024c1f-0e00-3e75-8cf4-32be0d15ba26 | -3.28174 | -49.46737 | 2025-11-07 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059ab9bd-4dd9-334c-8ef3-91edcf8664f8 | -9.04677 | -51.12369 | 2025-11-07 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3120482a-6c2f-3309-90b0-2cd7185d0255 | -4.24376 | -45.62847 | 2025-11-07 05:16:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3dab3351-dd62-3eaf-9785-875bc4b3d63b | -2.79314 | -50.314 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7901318d-e734-39a6-b9fe-ce5e79a1427a | -4.72034 | -46.43121 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0913b0-b741-36f0-bbd4-5bf33548fbed | -5.27776 | -47.17073 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36532455-619c-315f-ba63-a7cc5ccdb15d | -4.29502 | -45.89132 | 2025-11-07 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 90bee87b-209d-331a-98e3-33fc43a8e61d | -11.85444 | -63.67318 | 2025-11-07 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e31dc8de-fa9a-3fbf-bdcd-b2a365ceaf9a | -9.32059 | -62.03054 | 2025-11-07 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 681f0cef-d3f8-308d-8020-76b727e0d961 | -11.73243 | -59.30757 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0250cbf-1af4-3da8-bf77-e3c13d6e66d1 | -9.51252 | -64.34806 | 2025-11-07 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fed3ae2-e677-32e3-928b-2d279edb62dc | -11.72339 | -59.3242 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d98e696-a16e-35f0-8be8-87b11ddfaadf | -11.99469 | -63.94952 | 2025-11-07 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4cefefd-3c14-3db9-b25e-c4c334c0f1a0 | -9.11817 | -63.33345 | 2025-11-07 05:18:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368181eb-ccab-33d6-be61-659b739e3ae4 | -9.46438 | -63.51944 | 2025-11-07 05:18:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d254c055-6873-3196-8ee6-53611b5662fd | -11.5607 | -61.69654 | 2025-11-07 05:18:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18e39277-795b-308a-bd4a-12904eb124df | -9.44587 | -59.20774 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 73318223-564a-387a-99a3-26e42a2815d8 | -9.19491 | -61.72152 | 2025-11-07 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb51f905-84b8-3b67-8b1a-6ef3983e1771 | -11.72691 | -59.32127 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d2e6c84-6204-3c2d-9154-3855c7b3b952 | -9.46362 | -63.52396 | 2025-11-07 05:18:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68dd482a-b234-30aa-aecb-aae9111b6921 | -9.50509 | -63.39151 | 2025-11-07 05:18:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb55c402-9d4b-3d72-95fd-d01c7c995601 | -9.44532 | -59.21123 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3bf8fa2-9b38-3be6-bf63-ecf4d6f7bcf5 | -9.37935 | -65.61153 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fba13d06-d8b9-3961-975b-9147463b9eed | -11.7291 | -59.30704 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee2a412e-3970-3f6b-a4f7-46e250fa552b | -9.38177 | -65.6144 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 075a1ffc-09b3-3a0b-8f02-07b63e2efc71 | -11.73188 | -59.31113 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83679353-19fd-35ff-8e06-436f3ed103f5 | -9.15044 | -62.4073 | 2025-11-07 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cb5ffaa-abc0-37b9-b105-706ca0809e30 | -9.72357 | -61.90048 | 2025-11-07 05:18:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bd1f8f9-46f1-3776-b1cb-00e7b0c77da3 | -9.60665 | -67.14839 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a844bd6-c40a-3dde-956a-835e88201da1 | -9.60954 | -67.15948 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92ec56a5-558f-3590-86e7-e3da9bb2c68f | -10.60309 | -65.26614 | 2025-11-07 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56eb0cd4-8f8d-3cc8-98c1-a4526c5cd66e | -9.64041 | -64.74405 | 2025-11-07 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e14e94f5-4d44-3e18-b300-73997b47ad64 | -9.44256 | -59.20721 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ffb44f71-0f89-3afb-a7f4-0c5df2cb5e55 | -11.70465 | -58.93651 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f10bbb2-3454-3a0d-9bb8-e28ef7a97551 | -9.54517 | -63.50357 | 2025-11-07 05:18:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b69348-c8ac-3080-aaf9-79686dd2863e | -9.86249 | -64.08646 | 2025-11-07 05:18:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26cd6a99-623f-3cf6-abee-434d1250cc75 | -9.5562 | -66.74281 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cf6b715-b1c0-38c1-bd42-92262118d4db | -9.44202 | -59.2107 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f14dda29-d387-3d09-9c29-8f75ec38fb58 | -9.38362 | -65.61232 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44aa747a-8f41-3ad7-ad5a-449f7972215e | -11.73521 | -59.31166 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23dcf712-9fa7-35d5-b644-f286c5f54c9b | -9.72703 | -61.90107 | 2025-11-07 05:18:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b776f4-078a-372d-a6b6-9691b180f7ae | -9.93688 | -62.12135 | 2025-11-07 05:18:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a444d458-a067-3664-9783-0dafff9f31b2 | -11.72061 | -59.32012 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3da294d3-eaaf-39e0-9ffe-f95a18cb999c | -11.9635 | -64.04164 | 2025-11-07 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b70983-7083-3878-9fa1-c7b5076208d1 | -11.72449 | -59.3171 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 485a4c34-7841-36b1-83bc-0c1e3381291f | -11.99546 | -63.945 | 2025-11-07 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24a61e7-8bd5-34e5-b5d1-4b22c85f9264 | -9.43871 | -59.21018 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c28b09a-7459-3393-87ef-d1191626bfd7 | -9.44642 | -59.20426 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 6c1c818c-93a5-3335-ba23-845754742955 | -9.15111 | -62.40324 | 2025-11-07 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f68a491e-4f10-3a64-bbb2-cbfa5977e51e | -8.53295 | -63.49409 | 2025-11-07 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18a9830e-b31c-3e59-907a-b31cd8140406 | -11.92958 | -63.93996 | 2025-11-07 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64137df3-5b44-3929-a811-ef5bd0f68935 | -9.43925 | -59.20669 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6269245a-5d1e-3b86-a8af-a6c32279c822 | -9.64012 | -64.74057 | 2025-11-07 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33759ad4-fd6a-39e5-a756-8202bb8af094 | -12.02148 | -63.92659 | 2025-11-07 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d41bb06-27e6-31fb-b8cc-03c19d9a3b26 | -9.4398 | -59.2032 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7220de6e-5250-3ef6-9e63-ca762870fd10 | -11.8537 | -63.67755 | 2025-11-07 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c938cd2-bffd-3cd7-810a-b59b5c3c45a9 | -9.64104 | -64.7405 | 2025-11-07 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a061a00f-5630-3a40-a390-efc5ead2f103 | -9.66542 | -66.84588 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61b12f12-1800-31c8-a2e3-49926b16e675 | -9.44311 | -59.20373 | 2025-11-07 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 188e7d02-f96f-38ed-8650-9dc45666191f | -9.11632 | -63.33142 | 2025-11-07 05:18:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2617a0c9-fda0-3520-83dc-3d9c6559ac15 | -9.3775 | -65.61362 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4f6d431-20d5-3bac-957c-9ac1ec254ff0 | -10.6389 | -59.46265 | 2025-11-07 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d60ba85-0811-3843-a068-ba8c8d45bfb0 | -9.63952 | -64.74412 | 2025-11-07 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8bf2344-8167-3e69-a011-ec33ac97ab07 | -8.68373 | -66.88086 | 2025-11-07 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36580442-bb84-316f-b908-bd14c0f33e94 | -11.73024 | -59.3218 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17bf3a23-f40c-33fd-8767-3e23fa9efc9d | -11.72746 | -59.31771 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31e3a746-b49e-3bd7-966b-c7fc4fb1f673 | -9.1469 | -62.40668 | 2025-11-07 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d24409-f110-3b59-87a4-d47202a480fa | -11.72855 | -59.3106 | 2025-11-07 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff3b4e90-b724-3dd8-ad28-c77525cc4958 | -9.19147 | -61.72094 | 2025-11-07 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42772be1-c5f9-3de2-b580-ba496bbc1f9e | -12.01779 | -63.92594 | 2025-11-07 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 384ecefd-b470-3428-9364-c97d3e40a505 | -9.4535 | -59.2143 | 2025-11-07 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ab6f4d27-1172-3cd4-9d9b-6869fa94e37b | -9.4537 | -59.1949 | 2025-11-07 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 842a2532-e232-3fd6-8e3d-c76059e3dd4d | -9.435 | -59.1959 | 2025-11-07 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6e68f7f4-a921-3a41-9e42-bcf3f8b65713 | -9.4349 | -59.2154 | 2025-11-07 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2b879614-ca05-35d6-bdfe-05ec5a56b41a | -18.98064 | -50.02959 | 2025-11-07 05:20:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b3a6436-6fd9-3c2c-986d-62a849077e9a | -18.98013 | -50.03492 | 2025-11-07 05:20:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5c442f9-0210-3179-a6b8-8b823ec287e5 | -21.89803 | -57.3017 | 2025-11-07 05:20:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a88d75b-1b05-352b-8811-12cf989e441a | -9.4535 | -59.2143 | 2025-11-07 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d9a1ba37-2a77-3ae0-b678-456f8991504e | -9.4537 | -59.1949 | 2025-11-07 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cf9af502-f48e-3d4b-88a3-4eb4afb91c52 | -9.4349 | -59.2154 | 2025-11-07 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |


[Clique aqui para ver as próximas entradas](README18.md)
