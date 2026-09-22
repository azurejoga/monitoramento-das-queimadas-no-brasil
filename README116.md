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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3be4432e-18d1-3c55-a972-c5544820adba | -14.04528 | -52.05646 | 2026-09-22 05:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 925a87ca-75bf-315e-835c-068d8157f6fc | -10.24715 | -68.29068 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5055aca0-6313-330e-9433-89e212b54a33 | -9.19985 | -64.50977 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9922599d-b11b-39a6-aa81-d06716f36053 | -9.55613 | -65.99955 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76c42172-60f7-33b7-aca8-473369df90cd | -10.91879 | -53.94466 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed939f63-d971-3039-976e-8a9f5170a736 | -8.52878 | -67.00872 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf0b23e1-b1f9-383e-8dcd-c39f12c7bba8 | -9.67637 | -54.34436 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ba43e89-8ac8-3621-ab26-63e14378334b | -9.18889 | -65.84721 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6485686f-37a6-3015-ae48-156f31a3f188 | -9.55364 | -66.03631 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86d6922e-a1ba-334f-a93b-08dc78a65cae | -8.79871 | -60.80136 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba01f54e-d749-394b-aadb-10593352fa47 | -9.87412 | -55.73093 | 2026-09-22 05:44:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54a14e63-7ee8-343e-b13a-a5d6c1003677 | -10.93516 | -58.33558 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbfd0c01-ed12-377c-ad13-722e781b1f1c | -14.04658 | -52.05703 | 2026-09-22 05:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5be8e5bf-99b6-32fb-8c88-9702ee4d4feb | -7.90246 | -72.94929 | 2026-09-22 05:44:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8ff3afe-6055-3363-b992-e2d4bbba62fb | -8.7097 | -69.65561 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae6cea1d-257f-3e30-8bca-07312b4247b6 | -10.42824 | -57.22771 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7befdf94-f629-30c1-a57b-b1a8a777c3b2 | -8.08225 | -70.14563 | 2026-09-22 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27afb339-921c-3469-a41f-bfcd7ca9eb8e | -7.84106 | -70.59888 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a41d93e4-08e3-3492-abb7-1c6df3489507 | -9.56331 | -66.01929 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 698e58c1-5aac-3095-bee5-99840b5aaa62 | -11.31866 | -54.04438 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3bfa4e0b-06e4-3d68-9092-ed4aa87d4a03 | -10.86576 | -57.16475 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f72d307-726f-3996-9b82-e97562c7b364 | -11.32465 | -54.04523 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 083b3a01-4fcb-3e6a-bb76-c766e6de7f5a | -9.94677 | -53.98626 | 2026-09-22 05:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32ce10e9-dec8-30a2-90fc-f0e4b7d565b4 | -9.13873 | -65.97639 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef4cc8dd-1d1c-3e74-9ff2-f688583cf20b | -8.92123 | -72.81306 | 2026-09-22 05:44:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3715530-53b4-3627-9b36-1fdb50b6d41b | -9.7643 | -65.06226 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c614875-8bce-325b-a964-60a8155e3a33 | -9.55642 | -66.04049 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dde8a08d-4243-38f5-bc66-61585660a88d | -12.79367 | -54.05053 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d12e737-6525-3909-b17b-059b64e3e9e1 | -9.10192 | -65.37966 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 309a5f0f-566f-32e3-8ed7-c19706e8e26b | -13.52304 | -51.50897 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 207744e4-3379-3c65-b8c0-866936f7dd65 | -9.36329 | -65.76175 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 977537d5-27b5-39b2-9219-05bf50a83e5e | -9.56726 | -66.01624 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f785676e-429b-305a-9ad7-fe64eb9b2d8f | -9.55935 | -66.02235 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64be9988-d7f8-3d6e-bf4b-9420c6196967 | -8.7796 | -69.53864 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 045d5309-2e2d-3e64-9b04-9d8fa316192f | -9.94737 | -60.21959 | 2026-09-22 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c9a9614-aae6-3080-8c52-f903e5ca9db4 | -10.14815 | -58.75988 | 2026-09-22 05:44:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04b4cdba-973f-3f2c-be1b-0532a67fcb41 | -9.55305 | -66.03993 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b57d723-913c-36d6-a6ed-18e46e82c062 | -8.795 | -60.80079 | 2026-09-22 05:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26f79a1a-34a7-3e66-bba8-d5b5bf909582 | -9.30234 | -58.91437 | 2026-09-22 05:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a9a4741-5a30-33f2-872b-d35ad746216c | -9.55979 | -66.04105 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 121e86fb-2a1c-38c0-a447-7bd79c4b4886 | -8.73456 | -72.7919 | 2026-09-22 05:44:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8835e10-225e-3e30-b7c3-6e5b119ff8f9 | -10.10207 | -67.92665 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c010e248-86a6-3c4d-be5c-7a3d0c5fff95 | -9.37292 | -68.66073 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14d7b587-edb6-3e84-8178-2bdb1d6741a6 | -10.27252 | -68.87228 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 947df217-6640-3686-b47f-f7816fcc0726 | -11.04204 | -54.15159 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e25dad4b-07f9-3c02-8f39-4ad8cc63417c | -9.56433 | -66.03435 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c699ee7a-16a4-3a90-8f92-89d4cd19444f | -8.91709 | -64.30067 | 2026-09-22 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 863a1434-f767-38fe-a102-05be3a1dddaf | -13.5144 | -51.52259 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 6717fbff-af55-3e5f-9222-bafc4c720a1f | -9.12424 | -58.9208 | 2026-09-22 05:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0fdf3f5-7c0f-30f5-9749-7d01ed2b6052 | -9.28028 | -60.62509 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2bd5c61-b193-33d3-9199-3f63203bd9a9 | -10.54147 | -57.44252 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 974fe7d7-09eb-3bd4-a8fc-c3df6798867f | -9.13171 | -67.94358 | 2026-09-22 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea57432f-105d-3600-bded-cc5249058d33 | -10.59512 | -53.99075 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f695989d-ee8f-3915-939b-ee570b9d7d22 | -9.12537 | -65.86658 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97c009d0-7531-379b-9cc6-8290834fcd92 | -10.62218 | -68.80293 | 2026-09-22 05:44:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70fb4c44-27d9-385f-b930-554b9393eb89 | -9.10419 | -65.36555 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5496eca3-e4d0-3b68-9f9d-2c0a2a2ed286 | -10.89432 | -53.97524 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f2b3a23-54a0-32e5-aa15-fc5d24ba38eb | -9.11269 | -60.95061 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b2aac10-8a52-3f21-a023-1535af5cbb20 | -9.40176 | -65.91833 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f91b11b-f8b7-3384-836d-fda6f5ae5f45 | -9.55525 | -66.04773 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac8e0e7-e6e4-39f6-af3e-b9c736dca760 | -9.13829 | -67.94913 | 2026-09-22 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a9f0431-d32a-3afa-9d82-a81b9fc7bfcf | -13.51048 | -51.53008 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 76c1fcbf-f0bb-33da-984f-cd157ee4279c | -9.10306 | -65.3726 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a0b7287-c235-3cc5-8c2c-f8f03e94f893 | -12.78881 | -54.04227 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fe5ee79-f497-3e90-86a3-63f1ffa83dfe | -12.801 | -54.04397 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d05ce236-3427-3c60-a036-89831fe06059 | -8.91764 | -64.2972 | 2026-09-22 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 329074d8-b325-330f-a9b0-96bc19a60f34 | -13.51204 | -51.51583 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a3083fa9-1746-31ee-96d1-408d3afd6eeb | -9.55247 | -66.04355 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 324ea21c-ed55-34a7-be26-506fcd8d7176 | -9.6039 | -66.11884 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b240bcc5-51de-3ed0-b44c-c7e966c3e12e | -7.9205 | -71.34747 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2098d1da-d42b-3493-a783-274591703bd8 | -9.47745 | -68.02942 | 2026-09-22 05:44:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a81ae261-9e50-367f-8116-c72338859ba1 | -9.13901 | -67.94484 | 2026-09-22 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c4fb523-6cee-35e7-8c53-a85043383312 | -11.32359 | -54.05402 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bbcc5c1-62c8-3ee7-9bcb-fa158f14182e | -9.20531 | -60.29019 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e2a1803-7fc3-35c9-ad1b-bf1ca25805a2 | -12.14062 | -61.16608 | 2026-09-22 05:44:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 85c2958b-ae3e-3d0e-8cb0-24f1468b2542 | -11.31972 | -54.03548 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1a2845b8-ccf8-37c7-be12-f9d251465297 | -8.80241 | -60.80194 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0dd76ed-9fa1-3133-b824-ff8197a2efa8 | -9.55027 | -66.03574 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6a2efab-562d-36c2-b2cd-57bc45bcc681 | -12.79862 | -54.0608 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c893cc0-f9a6-3351-ad6c-393a6044d913 | -10.24866 | -68.73963 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f70c238-4a7b-393d-8d42-2a373dcfecbd | -12.8499 | -54.04972 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c73499a-ab62-31f1-acc9-8917a7f3529b | -8.79805 | -60.8058 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1afd5f58-bd27-3234-ac94-986f6492bddd | -9.4666 | -65.39595 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d64c347-08c1-386f-9af1-93987ffa6e1e | -8.54886 | -67.04057 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40fbbf2c-4196-3916-89ea-6873bd2c1fa7 | -10.61357 | -53.98841 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 807ef7cd-ae43-3d55-beed-1dde80a567db | -8.76852 | -71.10802 | 2026-09-22 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79da9ce5-1a6f-3e21-9acd-cfad5d28a2ff | -12.79437 | -54.04779 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e76a25b7-1c85-35d5-ace7-179927f2b02c | -11.32649 | -51.37508 | 2026-09-22 05:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68a20f9a-46e5-353d-9b83-e35781efdfff | -10.10038 | -69.12898 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa421da5-4dd5-3eae-ba48-753540d0ebb5 | -9.54462 | -65.68826 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca696731-6266-3d98-8a7c-0f5b86db147b | -9.0964 | -65.37152 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a4967f1-80b0-3f12-92c3-c34dd01c847d | -8.91985 | -64.30469 | 2026-09-22 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d38eb3-9ad3-3e80-9003-9c64faffb7b6 | -11.03609 | -54.15096 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9daf596-ef24-36c8-a089-c573dcb1cf25 | -9.5452 | -65.68469 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 939af76a-d0c2-3710-9f56-edbc87e3192d | -9.76486 | -65.05876 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fad0b6b-783f-3e91-b23d-d467e59c6409 | -11.15991 | -51.10262 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1805c9b5-26fe-37dd-b617-42e6cf42b1ad | -9.56389 | -66.01569 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc9f0990-5805-3096-a44c-f51453b4ac8c | -9.10582 | -65.37667 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cac37d3-da29-3726-8195-112e1a494d17 | -8.76406 | -71.10719 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 109a92b1-b05e-3905-a498-1809c4bcd834 | -9.1899 | -65.86214 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README117.md)
