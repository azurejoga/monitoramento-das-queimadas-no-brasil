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
| 6f20ef7d-9a0f-3310-b1f4-ebd1a511fbf3 | -7.35386 | -60.59023 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1da0b93-8617-3211-83b5-20872901042a | -8.88173 | -66.89391 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ef6fad7-6659-3dc3-aa43-b9553ce179fa | -7.28998 | -60.57299 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdaa9a9e-9b2e-3272-81cc-ac11ecd2080e | -8.98864 | -65.39027 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de7f619b-db3d-352b-b846-257453be0741 | -7.30528 | -60.56358 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea3cec09-d970-3996-8884-a7ddd711e34b | -11.1108 | -51.53896 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6aa992f2-5132-3a1b-8025-842df7920c09 | -9.16827 | -59.36743 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb75c50-aba0-3648-8a7d-74eb5c8f1ec0 | -10.23657 | -54.34596 | 2026-09-01 05:36:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 078a66bf-f5cd-3fb4-8c1e-1634d2aa6d9d | -9.51783 | -65.69742 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88f17db4-9921-3c66-87cc-b484d76e393f | -7.52359 | -61.37638 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2255e680-f3bb-37fe-aba9-f47c8a1dd56c | -6.91796 | -55.70374 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d86cd3-cd7b-33fd-819f-5fff7c3da7ef | -7.57223 | -61.37299 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c888bcf1-4bd0-3eba-a0d9-d07c520b5836 | -6.61013 | -58.60143 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 728cd11a-6d44-37fb-9bb2-651769c204d7 | -7.18845 | -60.68658 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1f95320e-2e15-3e1f-b546-f11d16ba7360 | -7.35065 | -72.95181 | 2026-09-01 05:36:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3062b2f2-95cd-38c0-8d41-b0c8f2ed9b35 | -7.30546 | -60.56379 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65d5b71e-eeb4-3fd0-86d4-6fa6498c4c3f | -8.59262 | -54.77204 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e15f102f-4768-3f89-baba-6601fe4132ad | -5.48667 | -57.15161 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db405283-a7b9-3803-9976-71deb47e024c | -8.62232 | -54.84988 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1302467-0391-38c2-9e2d-cc42d1c507fe | -6.95976 | -55.64672 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d4d6634c-3408-3fb3-9d95-9ad793db2b48 | -7.57359 | -60.45766 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1da02ac1-5363-3c17-a129-5551129eddb5 | -6.56321 | -58.55777 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78ddb88b-3592-3ae1-828d-2e9967bf4feb | -7.62806 | -55.29158 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd109c85-0dc0-3830-887b-b71804629637 | -5.86901 | -57.77985 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85e0623c-7e36-3065-8eeb-0d0a282f9f5c | -6.60403 | -58.59133 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 077113f6-96f1-3f61-97d2-2727d522f0af | -6.77203 | -59.47577 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cafe5a4d-719a-3eab-8b56-dc47a967d7ac | -9.21066 | -60.87876 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45d86462-f2c0-3494-9c0b-e92626814f79 | -6.91344 | -55.70306 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58feceee-b8b6-3080-83df-05d458b3ff1e | -8.95143 | -62.36673 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e131e51-e302-3235-a93a-833779b2e970 | -7.58171 | -61.33421 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5217317-85b0-3ce8-8df8-ae1da2ff2351 | -6.60335 | -58.5958 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 688c2a95-d4c1-3518-ab43-84a031e6e0a7 | -7.56496 | -60.46795 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acea927f-6f4f-3014-b17f-9c00bca90c6a | -10.51261 | -57.44359 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8cc81b24-c330-3524-b01d-7b693551579f | -5.94728 | -57.68723 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| acd56858-af22-3f4c-80dd-759e7029109f | -6.93726 | -62.88205 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e8b3baf-81ef-3d48-908e-65d84d6a359e | -11.26496 | -50.56748 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93bac13e-de9f-3fd2-8005-8959005a855c | -8.87342 | -66.89724 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c17e5761-9ec5-3803-b2b3-31c41616b342 | -9.62423 | -68.60144 | 2026-09-01 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d77ef3af-dffd-30ab-bbf3-a3797bcfe541 | -9.14907 | -61.09605 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2fc29fd-8ed9-361f-ae0c-b0641898de13 | -6.25123 | -55.42893 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e15c8ffa-637c-3f31-90c1-59d405e14d64 | -10.41852 | -64.4584 | 2026-09-01 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f33b4307-885c-300c-8040-f94940c70a61 | -11.25023 | -54.00765 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81ae8cd3-bc14-302d-abdb-3360b276adef | -7.48128 | -61.3925 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c93bbcf-fbb3-3fbd-a463-55b954f3915f | -8.5056 | -55.30853 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b55a2332-0ba8-3b60-9519-89eee7d1686a | -7.30027 | -60.57454 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9018c70e-a9f5-32f0-b919-61669505f9e8 | -6.90868 | -59.48329 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c46ace6-4a89-3ff4-8b51-eea9b976ea8a | -10.51316 | -57.43963 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fd408d09-4a2f-35df-8528-19630577b53f | -7.59597 | -60.47293 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c974857-233d-3b19-9a16-53a78e769a96 | -8.93761 | -62.36813 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b42adca-afd0-31cf-9327-8b0b51b4057c | -7.58909 | -60.47181 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bdefa059-f263-3b85-8159-de360a3b4559 | -9.85083 | -64.98925 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd13a30a-f38c-3695-9781-a3a8326dd818 | -10.82676 | -50.71545 | 2026-09-01 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e93dc502-9916-3ffe-a69d-12d7acdfa665 | -6.9334 | -62.88499 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c28fffdd-4653-365b-8498-dde80cbd76ce | -9.94687 | -53.99292 | 2026-09-01 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27fd036b-6faf-39fd-972e-0f2e75200469 | -6.12391 | -53.54857 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 778e61d5-81e2-3f5f-a0d5-85b750103cb6 | -9.16761 | -59.37186 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71457efd-d4d9-3a25-b442-abbc9801eea9 | -9.39642 | -60.57105 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dac61567-0ca5-3fb7-b482-0284277e3654 | -9.15034 | -59.53852 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3066460-109b-3255-a90c-6baf886578f8 | -9.46377 | -57.02024 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 204ccca9-6b52-3dac-adbe-dc35389d69d8 | -8.93429 | -62.3676 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee926d4-e3b3-3c24-8f17-d163d1583df3 | -9.0683 | -60.49592 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d7783fc-c951-34fb-b290-484954867594 | -9.32199 | -68.88663 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 782b7a1d-2819-3f25-877c-4fc94a74259e | -9.19398 | -59.44756 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d8a7089-8f45-3aab-8a41-16a61d895b8b | -7.57555 | -61.32959 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8420b2ea-c728-3daf-9235-613e3dde5c65 | -9.48468 | -57.02748 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8289efa0-5c76-3a1c-959a-d266571c29c5 | -7.5822 | -60.47065 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9dcbbd6-b04c-37d2-a1c6-906912cad428 | -8.77157 | -69.33646 | 2026-09-01 05:36:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce035890-fa9d-335a-b941-49053a4f17b6 | -8.81471 | -62.50257 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69ab7e14-8aee-37bf-962b-f14f35c5f228 | -7.45419 | -59.93418 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef54b838-57ca-3524-a073-2d887ead6a74 | -6.95535 | -55.63853 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41425ab1-ff5e-3ad7-a38d-d38965ef9264 | -10.06239 | -59.40793 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a75f525-5a7f-3305-a057-a874b8df5a80 | -10.33432 | -50.00353 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38d0f9df-f165-357a-b15e-493f64d383bb | -9.92826 | -60.49478 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d10ace3-f996-37e1-bdae-4c92bc552e89 | -9.21013 | -60.90099 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38a20427-7e5e-31e0-9eaa-906aa90bb441 | -6.803 | -59.77143 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4e8b683-ebde-3c52-9480-8739514e8f71 | -7.57185 | -60.46906 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8651a17d-3964-3c27-ad60-09762b1c3630 | -7.48183 | -61.38893 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f196dde7-790d-3f85-8d92-2db20c1045f6 | -6.12466 | -57.6807 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06113ce0-17be-3173-a71b-d30b1e603be4 | -9.03179 | -65.43373 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6737792e-0a4f-3ba1-be9c-1de1dea90242 | -9.1789 | -59.62179 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 814065f4-dd08-3981-9b98-3283d4f0c3a4 | -8.7179 | -52.367 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfb33662-fede-3f79-aba1-f0df2c6de2ec | -6.6595 | -59.43137 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7bd9534a-d627-3077-bba0-89260fea5de7 | -9.21482 | -65.79711 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63d74ea6-2b47-3137-99ce-8e0910e4f133 | -7.2894 | -60.5767 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fc6aca3-9ec4-331d-bde7-b38dc8fb3306 | -9.08096 | -65.48946 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16a83416-b6fe-3804-9d20-f0cc618470e9 | -8.54171 | -67.15585 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6112483c-ca29-3fca-ad86-8f61ee88d520 | -7.33216 | -60.59444 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aebfb92-4457-3abc-a59a-249739919696 | -6.18022 | -57.73673 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e7e5c13-5e07-354a-ad61-a9959fbff1c2 | -9.08793 | -65.38198 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edb596b8-f80b-35a3-9fcf-de2d23b613c4 | -6.7573 | -59.15339 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb2beae1-33b8-3d30-926d-e8c800805ae3 | -10.84216 | -54.03659 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a298c6a7-b07a-33de-b504-1a42c9fa904f | -9.17267 | -59.63829 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db300276-70aa-3cf3-a7ec-b919437b9a4c | -6.60708 | -58.59639 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06af609c-ef74-3811-a1bb-1f60c60c642d | -7.56608 | -61.36837 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2016c4ce-90bb-3447-a60d-93319e6d203a | -9.05995 | -65.48593 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8f8a477-4ef0-3fe8-97c8-5abab0d50ece | -6.13212 | -57.8451 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2eb3c949-c843-3b5e-a093-52a4ca23c36a | -11.47798 | -58.5154 | 2026-09-01 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56ef20e6-0d28-39f7-895c-ad600c5f8605 | -7.58047 | -60.48198 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19bd744c-58b4-3a8c-b4aa-4a789429096a | -8.93207 | -62.36008 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7fc2cdb-6853-3245-9b13-f24b789d2305 | -8.86783 | -66.76905 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README83.md)
