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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9b7a67b-71d5-34f6-8b9c-123aed04cda7 | -8.05401 | -61.71749 | 2026-08-21 04:46:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bc2c181-f0c7-3f6f-9c6f-9d59c068e6e6 | -10.30229 | -48.23294 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01b8567a-d968-36b5-bc10-d348561baa7c | -5.3625 | -48.81245 | 2026-08-21 04:46:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1b5d1ef-74dc-3242-9955-bbcda9be8a79 | -9.12099 | -61.59635 | 2026-08-21 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80eadf8b-adcd-3625-acd4-86a2cc3e59c1 | -8.89127 | -60.54941 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fabdbe28-20ce-375b-9086-2c3f608180e0 | -8.10317 | -51.65308 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59e4ea00-f456-349c-8203-4802f28881f4 | -6.86556 | -59.44697 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ed6e942-4e78-3db0-af03-cf284333756a | -6.65785 | -56.34536 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a50c20f9-bff6-396c-804a-3301418a4088 | -6.87954 | -59.42903 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6fee17b2-69b2-32ad-bbba-ff91fe5c8801 | -8.18291 | -54.99238 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e27a5a98-7a2e-3335-8920-dba83cd380d5 | -7.72797 | -46.15492 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69fe76e4-fa6c-3b00-8df2-6f82ea514cf7 | -8.49964 | -54.86707 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c91704a9-7953-318e-8c1f-bd454da44828 | -9.41111 | -60.55057 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55f70fd2-9747-360a-a4c7-590ec3f2003a | -9.3966 | -55.98527 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 043f3801-9211-3144-8164-69871d49d76b | -2.70532 | -54.75921 | 2026-08-21 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e04f765-dac4-35ca-b013-d41fdb1c733a | -6.22801 | -55.61972 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 1d343a75-5813-399c-ae5a-d9fc842b5936 | -5.32494 | -50.95451 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d14e8bc4-b322-33a7-b2be-92a272bdc0c0 | -9.50441 | -51.67315 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d46ad6ca-e500-3ed6-a8df-867f66899925 | -6.65607 | -56.35593 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92131d54-d83a-3d69-81a6-cd6529aeeafe | -7.77266 | -61.13566 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7f4fe84-d0cf-3c73-a233-cedfa623c5b3 | -6.58747 | -58.96788 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b425a20a-3ecb-3cf0-a5c8-dd8a7a49366b | -4.95342 | -56.26859 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 667a58c1-254b-3d93-a869-c5860e628a8c | -8.07657 | -50.10377 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f7e58b8-b5dc-39ef-8e8a-cc10fd7cefce | -9.3997 | -60.55491 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5e7c12-ea5f-3e7f-ade5-573d6ed4bedb | -8.58978 | -54.70961 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27d3d39e-7165-3972-a3fa-af19e82daebf | -6.97559 | -59.58513 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bc215cd-f038-3df1-ae8f-35f3ddfb6772 | -9.41769 | -60.42859 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 919de680-ac4a-3414-a408-7adcb0afda03 | -6.82341 | -59.39435 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6c0725f4-2d85-3a2b-83d4-6541a604b008 | -9.45094 | -51.62194 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cadf1e9-a2c6-3b17-bcc1-e900c25bc77e | -6.20168 | -55.48223 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6b61abd-d9c2-31a6-b0ff-5c1aee8bba31 | -10.82514 | -50.99663 | 2026-08-21 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 675d6253-1690-3fd4-94f2-acf6272d0a69 | -10.30604 | -48.23338 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cee99978-eadc-3107-92f9-371665617806 | -9.51866 | -51.64687 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd04f79e-997f-359c-b618-c1a67569c7ce | -6.43223 | -52.76083 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 48f0afc3-074c-3c12-88b0-7cb75d3d2ddf | -6.75427 | -59.46658 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4071e2eb-bf52-3363-bd91-377f7d84b88d | -8.71688 | -49.6195 | 2026-08-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8668776b-34be-376a-942d-fbdcbc4ab431 | -9.05091 | -50.84476 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddfaa0e6-0357-3d94-9f75-8bea035d796c | -5.86527 | -57.66411 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfe7f178-9488-35e9-b26e-f01fc2fa80bd | -6.87887 | -56.42279 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc8993a1-2fd8-3516-b00c-68d7c369dc5e | -5.61363 | -45.70626 | 2026-08-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28840d96-11e6-3a19-b03a-dbc13218530f | -5.49585 | -60.13328 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93396648-c848-3570-892b-d93ffeffb8b3 | -6.24599 | -55.41751 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0014be15-3c80-3de1-8407-ce00e8289714 | -9.5094 | -51.68464 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef1de491-d906-39f9-a29e-f664e88b2547 | -9.40694 | -60.41269 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 46636683-7f76-3580-b914-43d980d41f6a | -6.61952 | -56.34864 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abb84734-fd38-351f-b529-6641152c9012 | -9.05653 | -60.4389 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a904adb-f455-3b5e-9751-00476d11e1dd | -6.84727 | -59.40419 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 243ad00b-d829-307c-9115-97147fa46c73 | -7.36926 | -45.81859 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| db02710a-762a-32b0-b0f6-5d187cd19e86 | -6.2471 | -48.66134 | 2026-08-21 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aba0035c-9d19-327c-a8f0-851bcc38af9d | -6.87199 | -59.4393 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc09caf-e129-3897-9258-9cab7810aef3 | -6.70152 | -59.09665 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95012e6b-40c7-3a07-9a59-6d0e1d4ef02c | -7.63253 | -45.76495 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c17fc03a-4882-3633-82a2-f7f73eed6166 | -11.35737 | -46.00924 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 092c48bc-30e2-352f-9bc4-56309f00b08b | -10.29164 | -48.21662 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f1b8708-8e1a-3e76-95e7-d0e8b066c90a | -4.47245 | -55.40137 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fab9e00-3896-3ec1-b5a4-b566258f96d6 | -8.45552 | -46.94772 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc20dc7c-69ec-3ce6-b18c-24c29ff370d2 | -8.54062 | -55.3205 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| baff5c24-b966-34a0-a3c1-ef8a8353fa8d | -9.06554 | -60.43223 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07d64584-1704-3b9f-ba24-fc969dc6f448 | -6.88849 | -59.43634 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c11a7cd5-c081-304d-94b2-62426eeb208f | -9.41259 | -60.42772 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fa1068f-5fa7-3447-945c-f09c127f1fff | -9.41993 | -60.41645 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3dc20e92-fed9-3c25-a9fa-1b2fe7ae239d | -6.43121 | -52.72343 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c57fb19-2d00-3d8e-824b-675ff928541a | -5.87056 | -53.80679 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71d3bbf3-7088-3caa-af99-74882e3a41a8 | -5.6623 | -51.64632 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 449fd69c-cd96-325a-80d0-f7c496ed4ff1 | -6.87256 | -59.43948 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 783ec49e-d06c-389b-b085-9af916d59228 | -10.66069 | -49.01791 | 2026-08-21 04:46:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de511b4b-2528-3424-8e6f-2c189acb31ef | -7.25845 | -49.87931 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 207d21bd-444c-3093-acfb-3d086f7ce703 | -11.33241 | -45.01633 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 84354862-b24a-3f6f-be00-a3786dc55318 | -6.69085 | -58.93771 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 624a0cee-df02-3ef6-bedd-ba8bc8ded64e | -6.63299 | -53.37447 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 624773bf-ed01-3de8-8bde-0f242bba90c3 | -6.85724 | -59.02666 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6952916d-1769-360b-91cd-4fb7171e8f99 | -7.74549 | -61.09559 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3f5c168-f42a-35c1-a7c9-1b28ea0caa32 | -8.56462 | -54.79514 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2fdca05-0756-3614-b8a3-f306ac0477c0 | -8.37382 | -62.70897 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| eb2f9285-1e9a-358d-b2c3-e2b85b7f9d8f | -9.21335 | -59.65752 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b974e1a-a028-3df7-a7b1-754bad5dec7c | -8.52798 | -55.33823 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2384d784-e865-30da-b2e5-0b9de93cdffe | -8.38235 | -62.69654 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 4ab5cc2c-e300-31b5-b25a-1e92b209db55 | -7.37288 | -45.82296 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 235e5829-a7f3-36f3-8997-3d1ed5c0ad1a | -9.51643 | -51.63939 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a77e248d-918f-3db0-b87d-ee0655feadfc | -9.05263 | -57.06712 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1036bd83-30e0-306e-8af8-0930c8eb2499 | -9.41316 | -60.42466 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24a1ea3e-809e-3131-bba6-2c7c2d5e9d39 | -6.77184 | -59.45454 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4d37c1b-273b-32da-8645-4fcf57e312f5 | -5.81715 | -55.71758 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b77ef4-747f-3426-a956-454c88034b18 | -9.45431 | -51.64388 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57559bde-b264-35b6-94e0-0bc72cf3da84 | -9.40465 | -60.4138 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bb6769dd-18cb-3c23-84dd-77cdc962f6bb | -6.57624 | -55.44106 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23e80e7-bd45-3dc1-96f5-d0d7ea7b60fb | -7.60669 | -60.95308 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0b250ca-302c-363e-9381-705bffb8ff61 | -8.37466 | -62.70446 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| fc3b79b6-35bb-359c-8777-4e034f38222c | -8.65401 | -54.63121 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39183fa6-40ff-35f0-b3c3-00d08bf99971 | -6.88949 | -59.4307 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f21e82b4-0130-3324-83fa-46b47820ecd3 | -6.24733 | -55.42022 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e11a4fbb-3ce0-3889-9e4b-0a46be6809a0 | -6.57686 | -58.97164 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b80e83be-b7d2-33ab-9b2e-90da42f9158d | -8.68309 | -54.73649 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ced14c20-4874-30a3-97ff-94a5303ad35c | -7.79774 | -61.18482 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f8ce046-82b5-3ad4-a6a3-ea08f13ef944 | -7.62942 | -45.75651 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a761a38-68d6-35da-b6ed-6d1236347344 | -11.37263 | -46.36702 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd2d3e37-e344-3f90-a8d5-4ea4db1a9610 | -6.87357 | -59.43379 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5814de29-5559-3ec3-a56f-dfefa6301f0c | -8.64358 | -54.73017 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7285671-854f-3bf2-8402-01e8c3891ee7 | -6.8675 | -59.43555 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db38f139-1eb2-3d1d-8934-205cf85196c8 | -5.79186 | -46.1089 | 2026-08-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README43.md)
