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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68d1c0d5-edca-3798-bc51-54928c7c68b6 | -8.9411 | -65.97089 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| b420cb94-c31a-347b-a479-69973283eb5c | -6.58211 | -47.40411 | 2025-08-27 01:09:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 83eeac9b-db6c-38a9-822a-f4378707649e | -5.44975 | -60.15642 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6bbf694d-1a5a-3829-ae2b-3f646846f053 | -7.25997 | -57.68378 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a9759643-a7b7-31cd-84d4-33fb81412034 | -8.92247 | -65.91776 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| fa17214e-2b33-3fc2-8a30-32b7b10e8d7c | -9.40792 | -60.52399 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| c42e5a72-bc7c-3739-a246-58e2434fb7de | -9.64041 | -59.64259 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8c7854db-d041-3d89-87ae-5a0421a8bf8f | -6.81804 | -58.96409 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 962ce772-e4a5-3cc3-abd7-ad60bc94e2bf | -10.26666 | -64.4855 | 2025-08-27 01:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 59b31dbd-de8b-31b7-9341-18476864a1fc | -6.70928 | -58.56802 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d11667ec-0602-3ff5-8633-1541eef6ba8e | -9.16934 | -59.55528 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 863de1ce-7413-3ae5-82e8-e4a8bb97ed17 | -6.809 | -58.96535 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 085bb077-f71a-3bc2-a3f7-c2683ddd9143 | -9.15847 | -59.54623 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ed8cfb4b-9461-31bb-aefe-4fa8825afc09 | -13.40683 | -46.90596 | 2025-08-27 01:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 2af8b1ad-2961-3091-b910-0f656c113768 | -7.35429 | -59.66495 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7ee78465-e170-3e04-934f-41d7d0ec6b38 | -9.64859 | -59.6304 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 061416e5-32a5-3a12-aa17-10ae8df9b0bb | -8.90882 | -60.76196 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a9e21485-4f8d-3b07-b677-478dae246058 | -9.1841 | -59.44802 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a7d2b686-c506-3556-8a0f-a4060b6f6e81 | -10.41372 | -57.71342 | 2025-08-27 01:09:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 87065476-692f-3505-86ba-5ccdd14c4fa2 | -9.4718 | -57.82471 | 2025-08-27 01:09:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b88a8746-efb1-3c98-8e4c-9aec6a9ced23 | -5.62051 | -60.24139 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1d43895c-03bd-3e33-80e2-9bf8fb319c0b | -10.1014 | -62.90868 | 2025-08-27 01:09:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 574130ed-2373-383e-9a31-3c4f12d66a8e | -12.31711 | -55.30526 | 2025-08-27 01:09:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8000f4d0-7189-399e-8868-138b22064e7c | -14.36108 | -53.34402 | 2025-08-27 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 756023c0-dfe9-35d8-bbe9-a277ac29b039 | -9.1707 | -59.56567 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c7321b25-559f-375f-acda-e3df243f619c | -9.1965 | -59.54099 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0ac5d1a0-6846-30d9-b7de-3bfbf304b712 | -6.25828 | -60.01167 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 41181ce8-db9e-38c0-a933-cb25f983aa32 | -6.8374 | -58.97086 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 0e6e15b7-4eb7-360e-9e9b-a26ec011a70f | -7.62697 | -61.03032 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e123ac7f-61ec-3599-8b98-e868b6684b48 | -9.79779 | -64.25624 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 25e759fc-0b81-3578-8194-3ceeb927b5d5 | -9.11152 | -49.57642 | 2025-08-27 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 541838aa-03dc-3d3f-ba22-417a89572074 | -10.10408 | -62.9028 | 2025-08-27 01:09:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3d9cf98b-e0dd-3473-8e6c-859b592d62eb | -6.84517 | -58.96029 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 136578b3-8f72-3840-85e5-e67156270f7a | -7.35472 | -57.63695 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 720083c8-b90c-330d-826a-12d1063817cd | -5.737 | -59.88519 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de638214-aa76-39b0-a12a-02a159476c0d | -4.95875 | -55.80947 | 2025-08-27 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 259c2da7-8085-3e01-bcaf-ed4fcb8fd8c1 | -10.38224 | -59.39547 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 722d1eb1-ee99-348d-9554-b8b1725c9028 | -14.37391 | -53.36393 | 2025-08-27 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ede68532-bd23-3020-a571-3be5bc1843a1 | -10.02938 | -59.36196 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5996bd5d-246a-3c75-b4ea-5b9f74719ae5 | -9.17598 | -60.85914 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| ac9f3519-2a97-345e-bdc3-bef399ecc35d | -8.92207 | -65.94201 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4f6dcb4b-3f0f-31b1-ac7d-1258f1af3a20 | -7.54376 | -63.85262 | 2025-08-27 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| fca99656-34bd-3677-addf-42b7b81b2746 | -8.89696 | -60.75109 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4fd66ed4-18cd-307e-b813-e3bc6329f19e | -9.56342 | -55.384 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 7ce43989-f2da-3911-88eb-135e8097a15a | -13.50341 | -46.87342 | 2025-08-27 01:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 05e9d918-6be9-31e1-b8af-79d98e8e7ff3 | -8.95719 | -65.94473 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 255.6 |
| 92759818-9391-3b25-a503-55b9e8166fe5 | -6.82836 | -58.97214 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 2d42bd51-e2eb-3c96-94dd-6db2efa71807 | -9.57978 | -55.37518 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7a36adff-7008-3b7a-882f-d493276ca5d0 | -10.26959 | -64.51031 | 2025-08-27 01:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1314f510-0f0a-3b1f-b74e-31ef6bfecd34 | -6.84644 | -58.96959 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| e53629fe-40a5-32db-bde4-5bb688f68e33 | -9.80719 | -64.27226 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 399e6f05-3cb7-348a-a46b-5cd7f4278f99 | -9.531 | -60.5262 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| da588ee6-fd4b-330e-b7a9-51a719d08611 | -8.07191 | -61.54421 | 2025-08-27 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| cbe324f1-3299-33ed-bb95-26fe41bdedff | -6.25961 | -60.0218 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3a76a9b0-b9a7-33f8-8efc-4fd634a615b4 | -8.88991 | -60.77692 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f26580cc-669d-30d4-a9bd-a03dd5503c0d | -6.24286 | -60.00922 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0ec41848-deaa-39ad-acea-700998be108d | -10.42016 | -57.69394 | 2025-08-27 01:09:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 56612524-7157-38a7-a788-5c52a28f84dc | -10.08903 | -62.91019 | 2025-08-27 01:09:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f7617813-1e9a-3a01-8ce4-adcd56d1e5fc | -7.17116 | -59.74289 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| b859025e-e160-3986-b083-997916880dcc | -6.87238 | -59.90126 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| fba62a83-8102-3f75-b736-1b60b54a1659 | -9.639 | -59.63185 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4998e355-9543-31f0-97f9-a7f69ead8a43 | -4.55734 | -55.95833 | 2025-08-27 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8beb087b-9e30-30bc-8067-00fcf538cb0d | -8.96022 | -65.99994 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| df6450e3-7dc4-3d57-9fcf-2387e579f8da | -11.69698 | -60.17192 | 2025-08-27 01:09:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a0d1f3e-5d34-3c08-8747-e6539bf667a8 | -9.16254 | -59.5773 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| adb09778-3824-38f3-8b00-433a23d74216 | -7.3535 | -57.62811 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 25893a17-7ebb-341b-b46d-86dd91ce2d1c | -5.61102 | -60.24269 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8765a3cc-d1c9-3e5c-8190-86f51b370d8f | -6.24564 | -60.02961 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cfbd1d4a-bc6a-3f31-8151-751866e6feb8 | -9.39931 | -60.53732 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 10f7116f-3369-3894-8dd5-9cc9260e87e8 | -13.39879 | -51.77147 | 2025-08-27 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3196c693-089f-306f-a21f-50d7f1a12801 | -3.73356 | -48.94062 | 2025-08-27 01:09:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 5370f190-bc71-3d94-888b-852e8a8db1d4 | -9.79497 | -64.23298 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 7471ab14-8aa4-3ed1-9518-37232666e4bd | -9.4062 | -60.5326 | 2025-08-27 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 19781311-d1ee-369e-afe7-c9756391168d | -9.1007 | -49.5835 | 2025-08-27 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 0e8651b2-0472-3a1c-84b4-785aa3284c72 | -12.9068 | -44.658 | 2025-08-27 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 594ca2ee-c7b7-35e6-a1e8-1d78d71da557 | -9.1529 | -59.5609 | 2025-08-27 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f44e9e1b-e97f-35e7-8bba-cf6a0a8f203a | -5.118 | -43.2198 | 2025-08-27 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2ea5ba97-4f8d-30cc-909e-0e1cad6cb00f | -13.1837 | -45.2865 | 2025-08-27 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c7f1f1a4-4cef-372d-b028-82c862536cf4 | -5.1181 | -43.1964 | 2025-08-27 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 75ee1113-fc5d-3301-b3de-f7729d75db77 | -6.8229 | -58.956 | 2025-08-27 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e4c41fbf-ba8f-3f2b-a850-66d523f5967f | -21.5776 | -47.4852 | 2025-08-27 01:10:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ad0b70cf-1c65-34ca-af6d-d637516420a0 | -13.1644 | -45.2897 | 2025-08-27 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f5ac26c4-fc61-34e4-b6c3-f4122fba1d20 | -9.1009 | -49.5621 | 2025-08-27 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b3c102c7-9495-3ff9-a8d7-246a7d6976ff | -8.9026 | -60.769 | 2025-08-27 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 71f43e43-ac7a-35a7-8589-38e35f01fac3 | -9.4249 | -60.5316 | 2025-08-27 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 147b32c6-655e-336f-a430-e1a7c9042d34 | -6.8228 | -58.9753 | 2025-08-27 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 75ee3e8e-6b78-36fc-b6b8-dd2669774015 | -9.7916 | -64.2461 | 2025-08-27 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 895a79a4-9828-39f2-b83d-160547ef959d | -9.1715 | -59.5599 | 2025-08-27 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a2fef7b9-629a-3232-b93b-d22a57d0c4c7 | -12.9072 | -44.6346 | 2025-08-27 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 93891cad-82a1-3e60-bf9b-b9e44fdd8564 | -8.8841 | -60.7699 | 2025-08-27 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 248.0 |
| d6259ed5-e2a1-3e88-b432-9fa733ef8b13 | -6.8413 | -58.9552 | 2025-08-27 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5915615a-a453-32a1-943f-e5b0d2486a84 | -9.4061 | -60.5518 | 2025-08-27 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 66957718-82fc-37b2-a46c-783939b89b85 | -8.8842 | -60.7507 | 2025-08-27 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 0fcc10fc-b580-384d-9817-d5c15ae2fce2 | -9.425 | -60.5124 | 2025-08-27 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e017c348-8748-3387-874a-61bffdccdc80 | -9.4064 | -60.5133 | 2025-08-27 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 235.7 |
| c689a5d6-0064-3f23-9b18-08f0e861139b | -10.2742 | -64.5096 | 2025-08-27 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 2cfe3263-c810-3bcf-9e35-0b8716ace3e1 | -9.0821 | -49.5638 | 2025-08-27 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 007c409a-8c67-364b-af65-cf834742dcc6 | -16.5021 | -49.4805 | 2025-08-27 01:10:00 | GOES-19 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e1cf6bfd-8a77-32ad-b0ed-d58533e36c68 | -9.4065 | -60.4941 | 2025-08-27 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| b339273b-cd6a-37bf-b66e-d546fed69e81 | -8.9028 | -60.7498 | 2025-08-27 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |


[Clique aqui para ver as próximas entradas](README11.md)
