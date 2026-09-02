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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40800aba-3ace-3cd8-9986-47f1a0aefacd | -10.4142 | -50.0112 | 2026-09-02 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 21d91f75-d269-3c20-afaa-d9ecb1c7da55 | -1.4761 | -54.2365 | 2026-09-02 17:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 9b5cfa68-9bb6-3ce7-a030-81406f4e0d52 | -5.5648 | -60.2121 | 2026-09-02 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| bb72d345-e437-3b50-9c62-643919053b34 | -14.312 | -52.0676 | 2026-09-02 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 118bd442-fc20-32e3-999d-beb0f552e354 | -8.2412 | -62.9099 | 2026-09-02 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5a78c7d2-3597-3671-87ca-031d208236ea | -7.2933 | -60.5905 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 0c4c7d76-a84d-33e0-81a2-bebdf2a2c66b | -7.2192 | -60.6507 | 2026-09-02 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 4a7dc549-1867-3ad0-bda5-7960cc729021 | -3.218 | -61.1607 | 2026-09-02 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3cd451f1-6c4c-3f63-9b93-7bf7b29bbccc | -7.2193 | -60.6316 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 20248a4b-2cb0-32de-86a6-e7b607b270e9 | -3.3688 | -59.4079 | 2026-09-02 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 71103dbd-ab17-330e-849c-842b2d154ff5 | -6.1844 | -57.7395 | 2026-09-02 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 12a46e90-4808-383c-bf7a-7b57662da367 | -3.9707 | -60.0258 | 2026-09-02 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d4b5e948-c63a-3b4c-addd-3d1a72b7488d | -3.0893 | -61.5403 | 2026-09-02 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 3e84d48d-fef9-34fd-9cb3-fa62ad182d00 | -5.5649 | -60.193 | 2026-09-02 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 0d8e9af0-3d12-365f-907a-3f5b915b67c9 | -3.1998 | -61.161 | 2026-09-02 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f3b46c79-33d1-38ab-a92f-22a2f1d9318a | -14.2989 | -51.7072 | 2026-09-02 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4e82e0c2-af0a-3dc5-ac25-6f8be4cc50e5 | -7.2007 | -60.6515 | 2026-09-02 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| e7ed1ca9-381b-3bab-8f33-468c05757e9c | -7.0242 | -59.2374 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| b456a679-0bd1-3b80-9391-0d14a50170f5 | -6.7453 | -59.6341 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 20c7ecf2-03e9-3c78-9d12-aa26887be4e4 | -6.8019 | -59.4008 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| b27f29de-803c-37d3-979a-0596ccdd33e0 | -3.0347 | -61.4846 | 2026-09-02 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 410.3 |
| 4e4c9b6b-a554-35be-a38c-cfe33a14b558 | -3.4185 | -61.3461 | 2026-09-02 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 969d3c02-9ef1-3c33-9f99-a2a957c1ae4a | -3.7533 | -59.3231 | 2026-09-02 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 416cbd29-bf0c-340d-907f-1dcc3d9a0946 | -6.6409 | -58.5181 | 2026-09-02 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 32ac17a9-c8c4-3381-9cc5-bab39ba2f70e | -15.346 | -53.7912 | 2026-09-02 17:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ac0f46e4-f48a-3964-b747-2d6fca91b2cb | -6.8062 | -58.6469 | 2026-09-02 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 72619ab8-42f5-346a-a292-bfe7a0694911 | -3.4003 | -61.3087 | 2026-09-02 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5da07aea-8509-3715-9b82-1ec3d936429a | -3.4002 | -61.3276 | 2026-09-02 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 80bf0339-8a1b-35c8-bf5c-fc07d94082d8 | -4.2383 | -62.2349 | 2026-09-02 17:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c04d470b-ebd5-384a-9bfc-f3cb8a559538 | -14.5078 | -59.8375 | 2026-09-02 17:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 30d1e579-1148-3213-b41c-2a6a4c43d0a1 | -6.1426 | -62.5268 | 2026-09-02 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| adea6c1c-835c-3845-aa55-58777c494694 | -5.9635 | -57.6899 | 2026-09-02 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| bb71cfd4-a3d1-32c5-8019-c32611d4aca5 | -7.2934 | -60.5713 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 16954467-a299-3070-a1cb-44cca0c91dbf | -12.1457 | -44.196 | 2026-09-02 17:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 9fd37afd-e7f0-3e73-892d-660f158d4537 | -3.1267 | -61.1811 | 2026-09-02 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 333a76ce-473f-38f1-ae7a-2ea149e6e37c | -14.5448 | -51.9943 | 2026-09-02 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1d472c83-0012-340f-9d20-99f6711353e9 | -3.0901 | -61.1816 | 2026-09-02 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 26d738e0-39ba-368a-8866-0a46c8c40a8e | -12.5012 | -62.6305 | 2026-09-02 17:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 2bc79d29-3697-33a5-b4a5-2fd3dd442bfd | -3.0347 | -61.4657 | 2026-09-02 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 4ff43d73-501b-338f-9d94-fdce81587a4a | -6.6883 | -59.9436 | 2026-09-02 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 212.3 |
| 64780758-8a4c-34f1-8fa8-73dc529fdde4 | -15.3852 | -53.7652 | 2026-09-02 17:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 30647fa1-6fad-37e5-bb35-d8a0b2220735 | -8.4897 | -70.6059 | 2026-09-02 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 91a5e22d-8d57-3761-99e1-4e4d0b6fb39d | -14.9202 | -52.6454 | 2026-09-02 17:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |


