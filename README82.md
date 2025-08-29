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
| 784449ec-cdb3-3b56-b962-53e2a2167b18 | -9.3047 | -65.47585 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 124c7960-34ec-390e-b0de-9eb95c07de9d | -8.44338 | -70.14795 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad3e8356-b245-325f-abb6-94f027f81d50 | -8.95482 | -65.96922 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26ab29f4-477b-3fa2-8b92-10ee4dbeed77 | -8.85434 | -68.5051 | 2025-08-29 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c070c13-0655-3b8f-8f21-acf50a1f51dc | -14.31777 | -51.90281 | 2025-08-29 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aefe1d6-15b7-3985-9c63-7613b5ce8da9 | -8.93983 | -64.15586 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06b52afc-f7d8-3bbb-8189-ce0130ce34a2 | -14.51464 | -52.99994 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 997cedcb-3ef0-3378-82e5-c9c801fd1dc1 | -7.45749 | -61.39613 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8e4e9b8-d029-3216-8f56-1f77098319d9 | -9.11824 | -65.77323 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad5ec5f7-b1c7-3c2f-88b3-ff8de7f4daef | -8.95621 | -65.96084 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e27a8ce2-a577-3e30-b4fa-e1e6262beb9f | -8.23118 | -61.4575 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7885e840-e766-381d-8965-6371e024d801 | -9.15485 | -60.9317 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0ab6e7dc-e599-3804-b22e-5011ab591496 | -9.16814 | -59.5737 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 167e11be-57b7-3124-929f-0e91a3457f7e | -9.45438 | -60.56841 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2b4626c3-559d-3af2-9e94-04368290dd21 | -8.18694 | -61.37362 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 573c8905-2d26-3010-9c82-a997751cd4ae | -9.22973 | -59.68166 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63df0f3b-d3f1-3661-9cb0-794fba8ed8c7 | -8.87674 | -62.48006 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52310e75-9258-38a9-b2c7-f6c5350dd961 | -9.31548 | -57.70031 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 210dcf89-29c0-35eb-aab7-1bbb700d18e4 | -9.1169 | -65.78141 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a17ee4a-8d0e-3731-b1c3-aea66c4318a7 | -9.67503 | -64.98676 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e82ba843-9458-3b81-a955-db8efa0b2cdc | -8.18639 | -61.3772 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f833c903-f34e-3858-98fd-f67181b11d20 | -9.9076 | -62.14002 | 2025-08-29 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd572520-cec8-313c-ab4a-4ca46a2e12c6 | -9.13779 | -65.28291 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bceb7ac1-6094-345e-8700-cc981e447363 | -7.54211 | -63.84252 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46473056-9d8e-3342-9013-781460590d1e | -7.60565 | -61.22198 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 519a5427-8f2f-3254-acf9-03a35264b2dc | -8.17577 | -61.3792 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e014567-6cfc-3a53-b60d-632635a69c29 | -11.36907 | -63.28023 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8bf970b-304f-3090-9435-ac45839cdf6d | -10.37968 | -57.83187 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ecef40f8-d8ad-3303-9424-8cef02c73aec | -12.9877 | -56.9198 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0667393-15ae-3f7d-8a90-fd302c52cea8 | -10.45425 | -57.95131 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5cebce5-48ec-3d85-a147-87eab674f9c8 | -11.36962 | -63.27672 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc9902a1-fe9e-3301-975f-551a62487bec | -8.89494 | -62.47224 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e58d22b2-33e2-39dc-9155-88e43afe1ce5 | -10.36951 | -57.81979 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 552bd704-6aca-3c17-a275-d1faf729cf96 | -9.11844 | -65.79434 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 629adadc-696f-338b-8225-c07ca11c8df6 | -14.50951 | -52.07689 | 2025-08-29 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e413636b-f2d7-3cfc-a80e-a02035854bb1 | -10.36543 | -57.81917 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e74754b4-af68-3a4c-b09d-bd2e749dc7be | -13.02046 | -56.91502 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9ad34b2-ccd5-3da8-9439-a6626cf2c29a | -13.36689 | -51.76356 | 2025-08-29 05:29:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79a6fc65-c285-3ed5-bb6f-73965dae707d | -9.25648 | -65.89588 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4ad0531-6610-359e-ac17-91e243d4b955 | -10.28851 | -64.49303 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d09fc7-d19b-3506-bca7-488050fbf7b1 | -9.16279 | -65.78365 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 413355e8-b4b9-332a-9403-2da8d33393c3 | -8.18193 | -61.38383 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22d61907-3dbe-3a72-b874-85a405e9ecc3 | -10.45478 | -57.94765 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf2d4fa9-ff6c-30d8-ada7-dd605be2bbdb | -11.38121 | -63.2678 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 341fd349-0d14-32f4-94a0-7980a6c87e90 | -9.13365 | -65.28624 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd744769-a973-3db8-892c-1d6299c736ad | -14.2674 | -53.22913 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a6e2b2c2-e56d-3e0a-86fb-a3dab37fac89 | -9.03826 | -65.7318 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2ff9923-01ed-33b3-a137-9452653760da | -11.155 | -54.30564 | 2025-08-29 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c0d6bd5-db90-3e1d-8b6f-d9dd00f93a3c | -10.6223 | -54.90736 | 2025-08-29 05:29:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cf66766-e508-393c-aa14-d1cb7f7e2b15 | -9.01157 | -65.69364 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c36b68a9-6e25-340a-a2a7-8d440833123f | -9.16701 | -60.78394 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb86f729-5e27-3fc1-932f-063e084ea946 | -9.167 | -59.55612 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 578ed462-bd18-38c7-8580-f50a08f3e675 | -10.05476 | -68.47063 | 2025-08-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e11e9ef7-5e32-301a-a0ff-825cc1311403 | -10.36292 | -57.80759 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e48e59d-e81a-3556-ab99-002b62268970 | -9.14941 | -59.57512 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f37bee82-e3a7-3cc4-9eb1-62030e8dca7f | -11.09278 | -65.15552 | 2025-08-29 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f91fdef3-df90-3b16-ab67-ad78c0feb764 | -11.15458 | -54.30894 | 2025-08-29 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c694ee16-acf3-35f5-967a-53808970a24b | -9.17569 | -65.79424 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef5dc9e1-dc9c-340b-84dc-955088c70f45 | -9.21932 | -60.80714 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64878c79-9faa-390f-a588-3ba93ba10c86 | -9.08293 | -65.72091 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3262d3a2-780b-3891-b6e4-8869eb7b5308 | -9.45959 | -60.55737 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac6d7255-85c5-36e1-adff-5c608a42f769 | -14.30054 | -53.29687 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47b4aa29-bd50-3d0a-9470-69e7539e301f | -12.43307 | -63.91877 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28003970-36f0-3ce5-a600-cd75f4fd7b98 | -9.24728 | -65.89532 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 817249a5-83e2-3b8f-9268-7c3fd496bcf7 | -10.47706 | -57.96859 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5904146-9236-36fb-9098-a223387ff2a9 | -10.93619 | -63.63384 | 2025-08-29 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28ad380d-7ecf-3748-b112-e47ab21502e7 | -9.46796 | -60.30342 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d628d67f-a56d-35aa-a477-62fb44fa1a22 | -9.1334 | -65.79267 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 229855e2-228b-3bef-afe9-a41bd79626c9 | -10.29188 | -64.49361 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1588f9d3-a1f6-3574-90cf-1d4889e20c72 | -9.46539 | -60.56612 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bcc45c4-6826-3e40-b60d-62b8734c9141 | -13.01533 | -56.91912 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb0f1a78-4410-3f48-a8ba-94a0be8d15c4 | -8.18137 | -61.38741 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc4d7128-4984-3fe9-9018-2ebed5bf1fd5 | -9.12491 | -65.79965 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83b3ed9d-5396-322e-aa63-6e6bd67dfaf3 | -9.46034 | -60.30629 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6145add1-e204-3b4d-b394-215c817d2d94 | -9.76993 | -64.25288 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aff0442b-5809-325b-80b1-8036b79dc782 | -12.42644 | -63.91768 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a536ecf3-8716-357a-8d9a-fd12cedf1047 | -9.47287 | -62.38169 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef3a6bb4-f353-3cb8-8e4e-defaeb78b62c | -9.13015 | -65.28568 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37501bce-94fe-37a6-9270-0ef4381490a0 | -9.1343 | -65.28234 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb5acc31-d981-33ff-9439-656155ac9a5a | -9.13714 | -65.2868 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c3394bf-7b23-3517-8205-f4fb7a035ea5 | -12.92851 | -56.97094 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15176f4a-42e3-34ca-bfb2-ee51a366b920 | -9.14894 | -59.57187 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8edaa3e9-e485-31c7-a3f2-f1a0915dbca4 | -10.38073 | -57.82874 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89cfb614-18eb-3ad2-8fd8-ca2dabea3572 | -9.12883 | -65.28664 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a92c5f95-78f2-3b15-b7e7-39ebdca1fd4b | -10.28514 | -64.49248 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7f9bf60-e85c-30ac-b0be-152338875664 | -9.44858 | -60.55969 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ebca1e3a-1a22-3f50-9705-43656d76f908 | -9.15768 | -59.53857 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49b63817-7460-38fe-9c29-8973c424e9da | -9.80376 | -61.19962 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 642f6b54-5cbc-38e9-9503-a185bcca7285 | -9.46134 | -60.56944 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e93f51bf-93bd-33f6-bcac-c39d94bfe716 | -9.17253 | -59.69446 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8ce5150-f2bd-32a3-8538-d4e80ee5bdfc | -9.16924 | -65.78895 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 327bcd3b-e700-3778-9da6-4e90f9bd3324 | -9.78789 | -64.24844 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0a38493-f007-3ac5-a253-b2a821c46d46 | -10.46386 | -57.97078 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6a4205d-fd42-324e-bc69-8526e109d59f | -12.99791 | -56.91185 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aae29c21-36a7-31d6-b631-e78b1eed58d4 | -10.25581 | -64.50259 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d245b45f-e172-3fc6-8a05-63babfa89036 | -9.42058 | -60.56765 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86ba3081-f7e1-320a-9dad-89d9d8822617 | -9.45611 | -60.55687 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 499e740a-f246-3ca7-a84b-dcb9517ecda1 | -9.41999 | -60.5715 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343db40e-fe83-3c57-bab7-f936e88d3dda | -10.46434 | -57.97096 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2803486e-ec11-3537-b289-a07eabebf32b | -9.1363 | -65.79739 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README83.md)
