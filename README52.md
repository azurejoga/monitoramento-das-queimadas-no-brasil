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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 232a6611-fedf-3396-ac6a-091ba0b4316d | -12.11662 | -47.38582 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef867891-d49a-3b47-a784-b0424ede4a30 | -10.10275 | -50.18829 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ef9874e-8dea-3def-b537-a7ed2c46b92c | -12.7674 | -52.82737 | 2026-09-24 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0257bf31-9115-35f6-88b3-e965cf4ccfe7 | -15.24203 | -43.26925 | 2026-09-24 04:46:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f491323-22f5-308d-a299-f2be8817647c | -6.88997 | -55.5662 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddc79e0b-1305-3715-9842-769cf4273edf | -6.62037 | -59.9385 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 714c9765-3846-3106-b4c4-afaf8196c53f | -9.7526 | -48.34754 | 2026-09-24 04:46:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13e55524-4849-3460-96c9-715b0d4e02d0 | -14.40353 | -52.88187 | 2026-09-24 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c2f6ef6-6dd2-36cb-a2a3-319e86692f62 | -12.13257 | -50.74635 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b41b7e78-ec86-3f87-bfa8-1481485d58a3 | -12.68712 | -47.02275 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c16a6691-0f8c-39aa-9ff5-dbe6816ce9f5 | -11.95683 | -50.75073 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5e9c20e-3431-37a5-a511-c770eb0bb5b2 | -11.29203 | -51.31397 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc3cf471-8acf-321f-a849-4c06bd76fe5e | -8.93416 | -45.94668 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4aa6116c-5018-3d44-90a4-5fa9f1fa738e | -6.61703 | -59.92117 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b8c4c83-13bd-3525-a945-2670b85d7bfd | -8.45841 | -51.478 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95a6c352-ee26-3ee0-9ccc-ceae6b0f45a8 | -13.78878 | -54.06136 | 2026-09-24 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f32e12c-1251-3447-98e6-05e2e2cd81be | -10.27416 | -49.97334 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b74153bf-44f6-31c1-b101-b95955acb573 | -11.45026 | -47.63625 | 2026-09-24 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5485b58e-18ce-3661-ae18-c78ba66a69de | -11.42728 | -44.18512 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6310f035-d850-3b98-9b82-06e24c669da9 | -11.32903 | -47.33923 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0629f481-20ab-31d0-aaab-cc83ec224641 | -9.74926 | -48.34703 | 2026-09-24 04:46:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03948c85-0efa-34a8-a7be-5175fb0bf181 | -11.3512 | -43.37361 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a53e68b-cb23-3c99-8b63-dc5318d3bb56 | -6.11053 | -59.88262 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 36fde7d0-1918-35dd-9d49-e69e1410459b | -8.12621 | -54.81292 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8cc291d-7cbb-3ed4-902d-7c7e08fe00ac | -8.79666 | -45.64352 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddcc1244-a372-3d10-b6d2-bcd19fdd4684 | -8.11615 | -49.58267 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c4cc3f-7341-3f75-9a70-9a85caf2e67e | -6.08576 | -57.6307 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6dc108f9-e1bf-3c0d-b9ac-c2055a48578b | -11.36271 | -43.3832 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c603064-5ae3-3a6f-a951-6ad0ddf8594a | -10.26639 | -49.95721 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5599488e-5d7f-3de7-bbcb-040200dd28f5 | -6.43617 | -59.95897 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 648ed363-2f38-394b-bbf9-611caf61427b | -12.41489 | -46.96222 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 283d43a2-8997-330c-8d4a-fba8180137c0 | -11.95342 | -50.75015 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1bb4a9e-c2de-3ad0-880c-e7bafc6ac8f2 | -6.67577 | -58.56939 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7087a7e1-98e2-39ff-a3df-1ad2f5422ec0 | -14.02358 | -52.0657 | 2026-09-24 04:46:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e4c18e9-b994-31ee-9ea3-91b14ecb4471 | -9.84338 | -48.50222 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f859711b-6333-310c-bc71-d6de283f9176 | -6.61317 | -59.9394 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fa749df7-91ad-3563-9504-b417bfd9d54e | -11.22373 | -51.37889 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26846dd6-27ba-3827-a56d-8b978e75c305 | -9.47022 | -40.33274 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 55.0 |
| ca0ddfc1-6cc4-34fc-958c-8426aeaf19ec | -11.01224 | -49.70429 | 2026-09-24 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f7d277f-9972-3ebe-aace-5fe84fdcdac9 | -11.62524 | -50.60089 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 510d42f2-ffbe-3f09-b0f3-2f238fee4dd2 | -12.1402 | -50.72099 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73ced50e-571d-3515-bdce-d3fd37b085a6 | -11.68088 | -41.45532 | 2026-09-24 04:46:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97ed5bf4-c1d9-3e9b-936b-19ce996ef895 | -5.99034 | -57.72353 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bfec5b0-17fb-3f80-a6e5-eb45ce047298 | -6.0406 | -57.76828 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa1ffaed-1978-387f-a197-8433d33b3f3a | -11.98716 | -52.45547 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e42fe24-d320-36c9-a9a8-4b630b822713 | -12.146 | -50.74794 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 788a640c-1faa-3289-b5bc-f33004120733 | -9.18505 | -43.04985 | 2026-09-24 04:46:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a22f014a-e8e4-36c5-8e76-07c36cfc6ea9 | -9.17759 | -49.993 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df7de049-4938-300c-b21e-4ed565bfe877 | -14.69989 | -48.74697 | 2026-09-24 04:46:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5a8b71c-ed9e-31d1-a887-ca4465987419 | -12.10656 | -50.7343 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b0cb338-6546-3a3d-b79f-c0d1a126f037 | -10.1445 | -45.53867 | 2026-09-24 04:46:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba8f77b1-2347-389e-824d-2294e734fe82 | -9.59043 | -47.77291 | 2026-09-24 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51c3fd4b-1be9-3e63-81ca-82f4ff7c4624 | -5.8663 | -60.1571 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 321d7d1d-a6d7-302a-b5e1-d210057a6ef7 | -8.36515 | -47.55857 | 2026-09-24 04:46:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eed9407b-8f16-3df0-8805-c4db8151e94c | -11.00832 | -49.7073 | 2026-09-24 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7181ae-1baf-3dd1-8662-e9a411d2bc00 | -10.14089 | -45.53803 | 2026-09-24 04:46:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6aceddfc-bfd5-3004-9e8d-dca8f85c6abe | -10.10555 | -50.19252 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fb0329f-8e11-3f1b-a63e-34d085bc020b | -6.10024 | -57.67837 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a51213b-d267-3ede-b845-8628f627851b | -12.13597 | -50.74693 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7c508d50-c34c-3c44-9b0b-e842b3fd8c07 | -9.26371 | -46.23809 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71b3376d-b0c5-34f5-abf0-a563c44d8644 | -7.89633 | -61.16671 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2f91993-3b31-3a93-a505-fd8247afb70f | -11.92587 | -50.75003 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2978ce38-90da-3aa0-88a1-36bac56ebcd9 | -11.79977 | -50.04342 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8597bc2d-3fba-382d-8154-bd6bcac59a73 | -10.43616 | -46.27075 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 535dc779-1cb4-31c9-bd38-738625b8b580 | -6.08644 | -57.62697 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe663e1a-f63e-333c-82ca-c87580ad7748 | -10.268 | -49.9686 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fa5a006-4241-3bff-8208-b2ba2360b44e | -6.10954 | -59.88627 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6c14bfa-ab4c-3ee6-92b3-b87c86805272 | -12.70224 | -46.99339 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c942f74-a9cf-3f9b-977c-5b812fcccdda | -11.43251 | -44.18726 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ca14694b-dd13-37cc-9001-2f5a4f6dc766 | -12.13825 | -45.63086 | 2026-09-24 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9af8d070-8308-3b96-a29f-fb50c9da8fca | -11.21002 | -54.12774 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 901b3857-5e30-3ec7-b804-be4e66d11445 | -6.0135 | -59.9409 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c2398a9-21b2-35b3-8636-8bcaa171f644 | -6.88034 | -55.5646 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9e5e404-e054-3b1d-af3a-f8a2ce1583c3 | -12.00026 | -52.46673 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3497443a-c1ca-34db-bb28-063f66564b7b | -10.41674 | -49.36609 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6efb9c64-71fd-3bd2-bb9e-bf2a52ede29e | -13.4585 | -46.2858 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4beff098-b2a1-3acf-820f-9e6a5ce961f9 | -11.73384 | -50.76756 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b79b63d6-5de6-37fd-a5fc-5152e7472e19 | -10.25215 | -49.98083 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8d4640e-5535-38dd-9549-b830298f3b34 | -11.4241 | -47.39972 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4496403f-ae52-3118-a3d0-972fdf2d563c | -9.23507 | -47.37433 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 66fb6361-de31-3428-b964-031d7f34c861 | -13.06891 | -43.28702 | 2026-09-24 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ece38e9-7291-37e8-b3d0-d9bbb66333f2 | -11.12691 | -48.2998 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc751b1a-1b48-35a8-87f3-3ace11dc6c60 | -11.39744 | -47.39169 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88027da6-6303-3649-a074-5c8ae58cd421 | -12.12758 | -50.73407 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e6b91d5-392e-3c4a-8c52-bb3828234f23 | -11.41049 | -47.39754 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f9a26f1-0ac7-32d1-9681-9863609a025a | -13.06513 | -43.28226 | 2026-09-24 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e0cc021-7c9e-3557-8f02-ad23604ffc21 | -11.79351 | -50.06082 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e59b2e2e-1bcf-3b24-9c7b-d11248b867f7 | -9.26253 | -46.2458 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17bb344a-48e0-329e-b953-d3fe8bba6aee | -11.66158 | -43.48996 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9a63418e-adfb-3433-accf-992255b943c8 | -13.21897 | -51.56788 | 2026-09-24 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a3f4c28-9701-3397-840e-1cb5ce8e90a5 | -8.2636 | -54.77542 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a89b25a-b3a5-343f-b1c3-22c91ac12467 | -6.66908 | -58.57267 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 556e0579-5802-36c5-bf04-4d9225b1192f | -12.16056 | -50.76567 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6f5dfa9b-b3b0-3f97-99da-89362244daf5 | -12.41852 | -46.94598 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83bed226-1068-36f5-b18c-748338f60ae3 | -6.43519 | -59.9642 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da9db2c1-1508-3ba5-a13b-2b17c45de200 | -9.43941 | -48.18958 | 2026-09-24 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cb29463-1366-34e1-b99f-7ad078a9aa00 | -12.16631 | -47.3784 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a083b15f-aa86-3445-a7c1-e9b8448734b5 | -11.64903 | -43.48814 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1ec304fc-e591-391e-bcb4-10c5f812c2d0 | -12.92664 | -50.91212 | 2026-09-24 04:46:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57bb2c3c-d8d4-3d88-9be6-cbc24d881b2e | -14.70661 | -48.74807 | 2026-09-24 04:46:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README53.md)
