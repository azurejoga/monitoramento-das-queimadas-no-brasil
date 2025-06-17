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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e6d3fbf-834d-3195-b8dc-44a5ecffa46c | -10.33626 | -48.10931 | 2025-06-17 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b31591db-0eb9-3b4c-a021-fd07ec55f4d3 | -10.28166 | -60.54084 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d68fcbed-c0b1-3d77-90d8-81a739cfe3ac | -10.35806 | -57.23186 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13cf97ce-9c2e-33ff-81da-10a9d945c03d | -10.29489 | -57.14286 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aebf3ba-cbd6-30ee-9eb6-1a57ec9674ca | -10.29467 | -60.53938 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ab69ab7-3906-3b28-a0ca-faac5e4a08e2 | -10.52078 | -59.39283 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 118d1c15-eeec-370e-b499-1e04773e9106 | -13.73785 | -53.93552 | 2025-06-17 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a871de1b-3daf-3a8b-a660-e6b581da233a | -15.38536 | -47.84138 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cf1543c-9c3a-3846-ac73-507d3db220dc | -15.39071 | -47.83923 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 603a6f2a-97d1-30dd-9ce3-3841ab09cf9f | -10.92997 | -56.8442 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e1d6a2b-7ee2-3fa3-a2eb-6efd3022c4d1 | -13.29053 | -57.06571 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b420a750-a3b8-3845-bc05-1508f8feb3f3 | -11.84111 | -57.8547 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fbe0c96-2ec0-33a4-b9f0-4b1fe19e478c | -12.20658 | -49.6374 | 2025-06-17 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1533c30c-4935-3b3f-93ad-25918684f3bc | -11.00855 | -55.05671 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb8e8820-e17d-3642-bb75-e97c8685b343 | -10.93118 | -56.83683 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28e0388b-4660-3d19-a7a5-3504bd94724e | -14.81605 | -48.4323 | 2025-06-17 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f98ba8fd-4c99-3f81-9b98-e9c702d06cdc | -13.49719 | -53.50703 | 2025-06-17 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bafa6bcd-9a6e-3e4e-bd6f-4f25ed513eb2 | -15.89221 | -48.89438 | 2025-06-17 04:57:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 086ea973-f28f-3438-a95a-6c9117a7c568 | -10.93575 | -56.83006 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c4fe3ca-0bf1-3a32-809b-96730f30e0b1 | -11.9182 | -54.82014 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4427736c-e142-3ea2-8f3c-1222b1efc151 | -10.2734 | -60.53941 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5ad96a3-6f9e-33a1-a762-26517ecbfcff | -13.38942 | -48.46011 | 2025-06-17 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d713f9e7-eba5-3429-bf79-f8436b795bbc | -12.42985 | -54.86875 | 2025-06-17 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9626bab1-aaf7-3ae3-a065-c3085dc06ef9 | -14.17055 | -60.06008 | 2025-06-17 04:57:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd217327-1958-3c91-983c-1a86717ae32a | -10.29944 | -60.5364 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11802abd-7bcb-3b61-bc3f-83f3eb0c00bd | -11.80892 | -57.34864 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b27a57a-3953-313f-99ff-e510d920158f | -10.3615 | -57.23242 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8adeed00-6700-388d-86d2-4ef64e059a04 | -11.03175 | -44.64999 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11e0d0a1-8135-3344-a07b-2096f5913eef | -10.85022 | -53.77677 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e9a9d8c-ebb2-3884-a09d-41c8d29fb799 | -12.65704 | -54.1184 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9b432b8-1520-307f-a47b-217832357061 | -10.44711 | -47.94908 | 2025-06-17 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61d5c5a8-4c14-3144-aa69-9c956ed344d7 | -9.4092 | -48.41553 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6af5450d-ab93-37d4-af37-a64b10ad2da8 | -13.72362 | -58.67964 | 2025-06-17 04:57:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c422f40d-15a0-3769-9697-4b81763bb191 | -10.85636 | -53.75914 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9896e012-c7a9-3597-8042-2c4f7df619d3 | -10.85188 | -53.76588 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 766d217e-7c87-3d03-8236-c3ac9b647603 | -16.29301 | -52.93357 | 2025-06-17 04:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8f147ca-0f9a-383b-8ba9-8f5f9cedb095 | -9.45586 | -58.21038 | 2025-06-17 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78a1f3a0-9bcb-33b4-868d-27c734faa03f | -13.74127 | -53.93603 | 2025-06-17 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7134f87e-26fb-30fd-b637-3fdbbf34df5b | -12.28461 | -51.07703 | 2025-06-17 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a06dc27a-365d-3466-a24f-8be6067f9ab3 | -15.89282 | -48.88948 | 2025-06-17 04:57:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3ec7468-fe6f-3fb6-ba6f-f856f929fadb | -14.21311 | -57.41215 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fcb0af07-7732-3952-a1de-4190adab39db | -13.44343 | -56.85649 | 2025-06-17 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93b4d516-01f0-3246-bef6-7bb9610b6f68 | -9.40415 | -48.41936 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b099be14-2018-3ab3-aaae-310ab39e59c3 | -10.74544 | -48.57279 | 2025-06-17 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef57c3d7-010e-34f5-95b6-dcc09fa24815 | -12.66097 | -54.11528 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68bd6cc6-d59f-3b84-bd84-242e651ccf81 | -13.95472 | -54.4889 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3035f35-e196-3776-9bce-4bf6ad96c2ab | -10.93057 | -56.84051 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dfeee578-cd94-374b-895b-009a9b7fe7da | -14.20974 | -57.41155 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02443804-a947-3406-b3ce-89eb168fa9f1 | -12.23142 | -44.21556 | 2025-06-17 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07115209-6141-3c02-9faa-4978e2632854 | -14.64722 | -48.06018 | 2025-06-17 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d5b3d18-2503-3b99-b618-3014cd6ca82e | -16.29667 | -52.93415 | 2025-06-17 04:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f53d32f1-d32e-3e63-ac07-d71671b7810f | -10.86915 | -54.29475 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5aa8350-f00f-34f5-a43e-0052a1d8c0d2 | -12.17198 | -56.54152 | 2025-06-17 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe1e9c65-20a9-31a6-ba8c-dc7d3edff792 | -12.42875 | -54.87585 | 2025-06-17 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f4d829a-e582-377b-bd60-5f6fb6b62365 | -10.29532 | -60.53563 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8178ef63-f735-3675-9ec9-9234e5bfde31 | -11.56217 | -54.57494 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a6791c2-833e-3c20-a410-6140b8616e3f | -12.20711 | -49.63344 | 2025-06-17 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e79ca529-3375-3e3a-b8bd-68a2b31d03ba | -15.39604 | -47.83731 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8277150-8725-3ad9-a3e0-c4249bbeba08 | -12.52794 | -57.22144 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c699aac3-08c7-3949-a8bc-676d1478ff78 | -15.62415 | -57.30575 | 2025-06-17 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eac1ec3a-e1a9-3f84-bfc5-4ae90caa4579 | -13.58648 | -54.29152 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b1eb985-870f-3f94-ad7e-4468ad2049bf | -16.29969 | -52.9393 | 2025-06-17 04:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3db09f87-b576-350f-8ec8-dd57e3cee297 | -11.57379 | -54.56588 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c07ed78e-9034-38ca-948a-9c0be8132a32 | -13.28875 | -57.07665 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62aafe73-ec40-3e90-9a75-267f3d92e6b0 | -11.08029 | -55.05383 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f97b5119-eb3b-3ae8-8e51-a1b3ed20c72f | -10.45025 | -47.95211 | 2025-06-17 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fd80644-ef95-36a2-a9c4-3abfb548b3a3 | -14.02918 | -55.12785 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46fe7917-c717-31bd-a391-751b5cd31c54 | -14.02641 | -55.12372 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7580278-2a4f-3b55-9ca9-bf3d20cdede0 | -9.41556 | -48.43431 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 847e1fd7-7125-3bbc-a10d-acf3830d48d0 | -9.44663 | -58.21927 | 2025-06-17 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b078e24-b6db-342d-8345-f415606bde8e | -12.02593 | -57.09309 | 2025-06-17 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dfbf038-d430-3477-bfdb-09c76cb653c4 | -11.92207 | -54.81714 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc176c7e-9d43-34c9-9eab-3246272f0ea0 | -9.4628 | -57.85162 | 2025-06-17 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1176368d-7b87-3506-bde5-ed8e11a06cdf | -11.56604 | -54.57192 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2166969-8a59-363d-b5a3-5ebf7ca0d677 | -9.45991 | -57.84689 | 2025-06-17 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ffba7b11-1029-3d2a-bf5e-cd18d08ca971 | -11.57434 | -54.56232 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5bd9e5d-11cc-37c2-917c-f8a4ab4dd229 | -9.39789 | -48.43177 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b848f5a6-7056-3f6b-9302-78e6c31a83de | -11.14447 | -53.93771 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 76643d65-0e50-3651-a20e-c2b0616c5052 | -9.51138 | -55.96696 | 2025-06-17 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94457e04-9768-3219-b0c2-4000313778b4 | -16.29238 | -52.93807 | 2025-06-17 04:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7f3b519-1fd4-355d-9c8e-8fe7873a70ac | -9.40733 | -48.42873 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49362029-6287-33ec-b20f-34ae89825784 | -9.3985 | -48.42744 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb91969c-50f8-35c4-9b01-5f1e93a1abc6 | -13.58366 | -54.28728 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fc4eb8e-34ec-3c23-a576-724bb9fd233c | -13.35951 | -47.8537 | 2025-06-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bddd23f6-371f-36fa-bc0f-57c5e93003fe | -12.4293 | -54.8723 | 2025-06-17 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b77bf5b-85cd-3018-afdd-3e319905f818 | -14.82278 | -48.45668 | 2025-06-17 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dd688bb-19a2-3885-8ac3-591e51c1dbc4 | -10.87531 | -54.32121 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ca4d9d6-3beb-37d0-80f6-2bb79bd67f3b | -11.00867 | -50.75883 | 2025-06-17 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4486745-6db4-32b7-810a-e12344b436ff | -10.2412 | -52.22436 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55cdd5f8-ffc8-3d1a-9d4e-e89a4aa9ed65 | -14.21095 | -57.40417 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a9e3058-138a-3471-b989-f0437b654181 | -15.57416 | -55.64867 | 2025-06-17 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 103f8efe-686d-361c-9004-cdafd724ac13 | -12.22975 | -54.29874 | 2025-06-17 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f12f66c0-bc41-3336-afa6-3e9f07027d84 | -10.28709 | -60.53409 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3015b932-7a37-3aa9-a882-fbcc16287a60 | -10.29187 | -60.53109 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb59118d-a732-3376-8cfd-8a27d84a1cff | -14.03362 | -55.1212 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af593fdc-7c0b-30ee-9543-23083ce9e209 | -9.20061 | -49.69744 | 2025-06-17 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 282f7640-8d05-3e35-934a-6b42a899515f | -10.29055 | -60.53862 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06ce641e-0ea1-31f3-9841-7ff6cf5c34fe | -12.16864 | -56.54097 | 2025-06-17 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db7964a9-4bd3-322c-9d3e-606df1e97759 | -11.02592 | -44.64913 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc599a2a-3449-3da4-a442-000e09a6fbcd | -13.36664 | -52.66638 | 2025-06-17 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
