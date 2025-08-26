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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c9db404-5390-36e6-a14f-d1617950aef7 | -8.23635 | -67.36629 | 2025-08-26 05:38:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce4a72d9-0ef2-3a4d-9315-adf994ce4540 | -10.41686 | -64.38172 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df15b688-07dc-3511-bdb4-97a8f3a96dfd | -8.59793 | -62.58354 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7a0557c-b4d1-3934-843c-f9d698704206 | -9.03076 | -65.73045 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 925d26ab-8c32-365e-9ce2-a595d4cfac5b | -9.17028 | -59.50775 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68225398-d8fb-3668-80c4-79d71ce3e991 | -9.19544 | -59.61883 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a9812b7-2a8b-350c-8d65-b075975e8d43 | -9.16285 | -60.77814 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62ec922b-409d-3342-a20a-b7ea2c88bde5 | -9.79788 | -64.25097 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62b04b64-6bd9-3279-b10a-cbb811ba8b5a | -9.19188 | -59.52891 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46d7cbcf-6958-3db6-8025-df2436e1a2c2 | -9.80396 | -64.25551 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37b6d2cb-0ffc-391a-b371-18d990f6ec1f | -8.10636 | -71.25122 | 2025-08-26 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9d8eeda-6dd3-3c70-bb3c-0804d1ece468 | -12.07704 | -63.1462 | 2025-08-26 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daabcefd-efdb-313b-b09c-d0459d0a732c | -9.16078 | -59.51711 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbf18e67-4823-3373-8438-01d6f06f14be | -11.52009 | -52.13597 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 4d19a945-cb45-3599-88c6-054d5f625848 | -11.55858 | -52.12159 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49644f96-a891-3aea-9387-296cd9b66550 | -8.98487 | -65.4203 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddd5a6b7-f77d-3ae4-88eb-5558cb64c755 | -9.33385 | -63.20369 | 2025-08-26 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b792b3dc-3394-364e-9e3b-3e09b2f33e3e | -11.30607 | -55.12041 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e8345b8-3e15-33ec-a0a4-c4d9bc2f236d | -9.63822 | -59.63327 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3c119e30-d0db-31e7-a1c4-b1fe638823b1 | -14.75363 | -59.72203 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2e424bf8-b3ee-3a17-9f08-ef1a2b2edf2b | -9.00489 | -65.40174 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d956c5f1-6ec4-375e-b129-3841ba49b6bc | -11.50328 | -52.13559 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 512a05af-0b3e-3bed-b08e-d1d9a10a90c8 | -14.35592 | -51.93283 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89245cf2-0d8b-3c2e-b247-428a09699e15 | -8.54276 | -62.64361 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b6a1e2b-4eca-3b58-9777-84efbcb6ca8a | -9.18115 | -60.8083 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 413d0679-1cbe-384d-af81-f454dbc94f75 | -10.39967 | -57.69849 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d494203-8e61-31a3-a09f-7c545c1839bc | -9.17418 | -59.4504 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6854aa1-b3f4-3a96-b080-f3232478e782 | -14.11256 | -53.9837 | 2025-08-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd18e177-cd2c-38bf-8309-b1afe401779d | -9.01974 | -65.69192 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 996eee2e-5d3c-30f0-abc5-1b4813dbcbd6 | -8.57502 | -62.63729 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0de1270f-4de6-3c67-b510-ddcd2c0302bd | -8.98379 | -60.4963 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55bae5e6-f20e-3938-bd2c-3a395332e343 | -10.25317 | -59.10557 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 464a37da-e49c-3777-9346-30c533a8f12a | -9.88587 | -67.66293 | 2025-08-26 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71a23f32-691f-33ba-ab1d-41cd8458630e | -9.24165 | -60.82415 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4c0b18f-cb1f-381f-bccd-6640c18bd149 | -8.97985 | -65.43038 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d6fca1d-e2ee-34d4-932a-17e36a60c2b6 | -10.42077 | -64.40027 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cd352fd-8139-37ec-8d9f-a8d731d4ea4c | -9.18588 | -59.54247 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2e494d24-a033-3bb2-9cb3-b367e2ff255e | -9.18776 | -59.44154 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d1b6852-7821-34fe-964c-27dd2cbbbbf4 | -11.5632 | -52.11697 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb084573-353f-3cfa-8ce4-0f4a66169810 | -8.40503 | -63.78348 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6a2a314-e539-3dd0-99e1-4cb0ef734b0a | -9.17836 | -59.53778 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eb6db907-9745-33d2-91f1-d85c40b5eb21 | -11.52683 | -52.13674 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| a5418992-2ded-37f6-bc84-70d2f9da6f24 | -10.4235 | -60.30512 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 150069fa-4ff9-3fc0-a975-60f1a1a0a3a3 | -8.98988 | -65.41022 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20577b8c-9a27-3712-817b-c32ca7e05822 | -8.84517 | -62.4532 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b2103c3c-2c55-30f2-9127-ec5dd35eb34a | -14.29008 | -60.36045 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4827b6a-a515-3ff7-ba13-3baa97f25089 | -9.20091 | -60.9221 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d290f1a-ad18-3a0e-987e-093ffdc66403 | -8.87658 | -62.45419 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e6d8eb-f7bf-3e0c-8259-64cbba1a3637 | -8.99654 | -65.41129 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a6528cc2-5132-3e74-adf3-6a25e26309df | -11.55714 | -52.11014 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cf2203f-b390-315f-8c98-21bcf5ea5088 | -9.38729 | -60.54244 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec21bf3-ebd6-3841-9a03-d9a0c40111aa | -9.18687 | -59.53542 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3a7dd540-342e-3d81-9a46-141ffb96ecbc | -8.98041 | -65.42685 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a45684b4-bb5c-3516-b378-7f9196c4059e | -9.07585 | -66.0638 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09bf5f91-d10e-32a2-a5bf-d8443b7514a7 | -8.90628 | -62.46642 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e33df01-513f-32b4-bff9-f25a62001bd7 | -8.55634 | -62.64571 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28f05bfc-3675-38d0-9865-db8aaf12825b | -12.33377 | -64.22802 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fcc78663-7183-30dd-9888-bd18704bbc21 | -10.54111 | -62.66143 | 2025-08-26 05:38:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20e11587-8cb4-3754-baf8-45676637fe0d | -10.418 | -64.39625 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca3e1c07-d7f6-3071-b081-5d9fb7e66ee0 | -9.22264 | -59.67443 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ca9ab65-8d81-3cb2-8f2b-5b5a37c6dd84 | -9.25326 | -59.7739 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e6f33fb-2972-38e7-9036-fb8ad800174f | -9.80619 | -64.26302 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6692c46-4963-30a8-be40-d73055a26145 | -10.24977 | -59.66267 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f48655bd-98c1-30a3-8cc1-023513560d85 | -9.18676 | -59.44866 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65bc96c1-389d-3154-ac91-cdc6ec2d220b | -11.55922 | -52.11554 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d43395bc-31f2-350f-b381-86f18abca6a6 | -8.81253 | -69.2954 | 2025-08-26 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f9595605-8a1c-3904-9dcc-1d872c835ff2 | -8.90229 | -62.46965 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddfb0921-11ed-3f02-a622-4461423f1f4a | -9.18787 | -59.52834 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a78de52-6413-318c-a9fb-757f2bfafcb2 | -8.55578 | -62.64939 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72286c01-f5a3-314f-9df3-7e5263af85e4 | -9.09562 | -65.72617 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 491d6b11-e54d-3039-8fb5-ee0952a1e769 | -8.34444 | -62.9375 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ea63112-fe07-33c1-b628-b8932a48dc29 | -9.18634 | -59.51017 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 009227c5-b6e5-3235-b590-b4c418fc766e | -11.69554 | -60.17404 | 2025-08-26 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cb524e0-5a3c-37c0-ae68-b52411e0cc94 | -14.3017 | -60.3668 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e6dcd95-7d6e-3ffb-9bd4-3bb77fd3fa9b | -9.1589 | -59.55997 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 096a1099-a891-3b83-a086-a79d33f3c324 | -9.16127 | -59.51358 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9d4cc60-50fc-3dac-b0ee-328b8a3dca68 | -9.00044 | -65.40828 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d7074190-a64c-3d10-8acb-51fc998c2cdb | -8.86339 | -62.42525 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 226dc21a-47e4-3816-b6ce-e6ace84cc11b | -8.34389 | -62.94109 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d3e5d08-46c3-3b1b-af1a-50ec4ef13852 | -9.19789 | -59.51543 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 726cf4cf-f136-349e-9e0d-0a9dcfab66a0 | -9.6377 | -59.63688 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c5746dc4-d360-3c1c-b4cf-7257471f8f48 | -14.39744 | -51.94394 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 88d9de46-ce60-3d72-a66a-917943417b33 | -9.27152 | -59.78734 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 692f0a01-17c7-356d-b1d3-ad6a686d9e10 | -9.1738 | -59.51192 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 50641155-11eb-384d-9dbf-36b722a242c3 | -8.87485 | -62.44239 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a1e034d-edb9-328d-8b5c-cbe1cf5b2fcb | -8.98988 | -63.64944 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1286b292-a97e-32fb-9ab7-43de63fa6c15 | -8.97929 | -65.43393 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff8fd8f2-ef21-30a1-9f30-dac0ad0c9db3 | -8.40673 | -63.79447 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f690620-d6dd-392b-9c8c-f5b5525e7128 | -8.34162 | -62.93338 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d95187b6-f57b-3403-83ba-434066336051 | -11.70433 | -63.67179 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9fccc1f8-72ee-3cc2-8b4b-c36c4f13df60 | -9.18386 | -59.52777 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b044f8c1-c059-3ee9-822e-50c75169fb29 | -9.02855 | -65.72274 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 650d79c3-5b74-34dd-88cc-6cac687b4e13 | -8.33716 | -62.94006 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03ff7104-fce7-3a8d-b802-5ef7c257040b | -9.15837 | -62.35348 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 974f94d3-6c27-3f55-892b-5cb0862f7133 | -8.86799 | -62.44135 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c9c66a4-281d-3dc1-b2ab-996788f4a99e | -8.56991 | -62.62522 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6ae7e59-2730-3a48-8463-112fb3efa9b3 | -9.18627 | -59.45223 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f65948cb-e1fb-30db-a09f-26a10e26ab15 | -11.55987 | -52.10947 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a70d987-319b-35ad-a6fd-a29c985567e4 | -8.90343 | -62.46214 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63161748-84c4-3043-8fdf-6d4dd19969b3 | -9.00212 | -65.39767 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README81.md)
