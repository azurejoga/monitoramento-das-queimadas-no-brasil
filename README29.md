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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d94bb08c-4eb7-3442-a9a5-edeb50bc1953 | -10.16316 | -48.25366 | 2026-08-15 04:59:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 892b292f-8a25-31cf-9052-dd65f45610b5 | -12.01127 | -46.41466 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b071c55-2fc8-323e-91db-bf9b8b4ea929 | -11.4116 | -46.34091 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e36649d5-3142-32ab-b8fd-5ad35ebc560b | -9.35744 | -62.34522 | 2026-08-15 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f38f311e-adb7-35ea-a3e1-3a9dfca0debd | -7.59082 | -60.87741 | 2026-08-15 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c49b94ef-cdd9-3a0e-afba-2b44ef346f79 | -10.65365 | -49.20255 | 2026-08-15 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c9ebfeb9-b290-39c2-9dd2-14b77b166572 | -7.55585 | -61.16774 | 2026-08-15 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a0653375-e1db-3582-a04e-45cfa7afc6af | -10.71933 | -50.55633 | 2026-08-15 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 07d8c585-2a45-3211-b54f-e5e2073a4637 | -10.52838 | -44.85375 | 2026-08-15 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05a42b8d-edea-3732-8b66-4de4be73c8bb | -8.89203 | -60.55225 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be3c7276-9f73-342e-b267-ed4c728047b9 | -10.29085 | -46.64605 | 2026-08-15 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccc6d31e-75ec-35ef-983c-e398df6b64a2 | -10.41965 | -47.98267 | 2026-08-15 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 67a6c082-1a9f-37bc-abfa-283311d143e9 | -8.95168 | -60.58664 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fae30251-a697-3589-b6bc-1013071567c0 | -8.96392 | -60.51694 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a81e776d-c04a-324a-bc98-0daff980094d | -11.41603 | -46.34283 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c09f5a9e-e3a6-357c-b92d-77367033cbf5 | -8.60315 | -54.68106 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2560f976-1017-3be1-bed4-4bf881b20b8c | -9.51852 | -48.56909 | 2026-08-15 04:59:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a964265-e69c-3074-afc3-cc0cb9ae7f39 | -11.40147 | -46.3299 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ee08514d-7f0a-33fc-901f-21f9b9ee7da3 | -11.49326 | -54.6324 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 120e5bc8-dc83-3027-814e-6f7c27dbc17f | -13.47869 | -44.03644 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9aaf34f-0c59-3333-a93f-8984409e7cb0 | -12.38336 | -46.42246 | 2026-08-15 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15feb563-41b1-3fb1-80bd-6c66c2a0f7fa | -14.43958 | -51.95018 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 012b84bf-fd26-3a9b-bba2-715ce445c5a5 | -14.53106 | -53.2512 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54819658-d59c-39c3-bc24-fca22b63d77c | -14.43015 | -51.85077 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 195245a2-fc5a-3b88-8ad3-b7c68aca0b0c | -14.51568 | -53.28254 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75bfbded-031a-3210-9cb8-eb0e47a9cee0 | -13.81146 | -53.79992 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b50663f-79fb-3b5a-93a0-f74f04be0903 | -14.1083 | -53.70411 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16e927c5-a0f0-30fd-80aa-4fc46814db33 | -14.11806 | -53.66117 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d80ba57d-2752-3e5e-8ac3-c0f1fae35c58 | -14.44675 | -51.92686 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a0e3b91-a3cb-3c31-855a-e0594eba1e60 | -14.44722 | -51.91883 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adccd705-bbdd-3a7d-b546-ba133f331baf | -14.44318 | -51.89695 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e37fffd-6d4c-3bc2-bc28-02e3d5c034f5 | -14.43488 | -51.90064 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f37bc4fa-c3df-326f-9671-a02c307ebea1 | -14.45527 | -45.67615 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08f8a25a-85d5-3b8f-b4c1-ddf8d66e5057 | -14.10426 | -53.70748 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fec3a33-a91e-359c-987d-94c49a8951ea | -14.99035 | -46.61497 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a773193f-0591-37f2-8f06-625e2933bd92 | -13.75061 | -53.42557 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bdae407-6811-337a-adc7-ecc1f2602050 | -14.08578 | -53.71258 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f36607cb-d012-354a-bfb0-ec095960b32e | -13.4199 | -57.04874 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78f60183-aa12-3e94-8aef-67a869d86978 | -13.44507 | -57.04179 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2460cabf-a9ac-359e-b721-a20b38102010 | -12.70481 | -48.43641 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fae79187-53a8-35b1-b1c0-6770afa4fcf3 | -14.46683 | -51.94616 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f58f7003-202b-3f84-92eb-5408973232e5 | -14.42592 | -51.90911 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 68f2f4dd-c1b3-3cc2-a2f9-218e2f146d21 | -13.42267 | -57.05293 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bae3c809-0203-3ace-ac7e-e330fa3929db | -13.55795 | -46.25199 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c181a969-c7a4-3d2e-9012-8d499e204e8e | -14.44786 | -51.91404 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffc75d95-ee50-381a-8906-3733037aa6d8 | -11.59655 | -54.66732 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ce0751a-05cd-3eef-8e76-872a897d7184 | -11.22239 | -54.8254 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5627bea-5ee9-3593-bb93-3f1554362be8 | -13.24003 | -54.17932 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88136939-b2c5-36d8-a9c1-a43996d86f4f | -14.08925 | -53.71311 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba726e9c-9c19-31e0-8e2a-42f79a34e020 | -13.23775 | -54.17134 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e27c31a-7553-3c21-9f0b-d03460258313 | -11.50597 | -54.6162 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd48e6ad-0a4f-3aef-bc1c-2dfbf73c861f | -14.94974 | -46.63256 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86940930-f642-39f6-a020-7acc7171ad22 | -13.23719 | -54.17506 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e2049a7-1ab5-3051-8d67-1b0705b423ec | -14.96144 | -46.62659 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57829955-fb80-3c3d-8492-257fedb85c43 | -11.49713 | -54.62937 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ebb768-e723-31c5-901e-7bba1c04428d | -14.43869 | -51.9012 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8bf43c7-ebe9-3ac7-a46a-d664def2b192 | -11.50603 | -54.63803 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8898d3db-6776-30c2-a1f9-5317c53b1312 | -14.44851 | -51.90923 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3027d0d-9d2b-32ba-bb68-f599a7d1f0e3 | -13.54153 | -46.25001 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ccde679-a0b9-3a11-b8d2-33e7e94f9e17 | -13.75468 | -53.42218 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2583bbb9-1364-30ab-85ff-3313742f9221 | -13.25588 | -54.19634 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad5f53c4-fefa-30d5-89e8-f897fc667d59 | -14.42772 | -51.92404 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b18d48c5-9a58-3616-91b4-08be9c3590db | -14.44915 | -51.90442 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01c188fd-abed-38a2-af5a-9d5b375fed2b | -14.22431 | -45.4127 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6eb27d83-ec5f-390e-a5f7-c72f2115d71a | -13.45222 | -57.06157 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27e507ca-efe5-33fb-b9ba-e1b1538c2bfb | -14.45926 | -45.68157 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28118abd-012f-3a3a-b145-5dc8e73d89bb | -13.55249 | -46.25122 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f607b02e-0f02-31a2-8b33-89566234f742 | -11.50542 | -54.61975 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d1fd578-1641-3e63-8090-f3f4f41f2460 | -14.04792 | -53.66716 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b64452bb-2429-3ce1-b280-50215f0e0c46 | -11.49543 | -54.61819 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0adddf-7e43-39a4-ac98-04bad1bc188b | -14.07925 | -53.62335 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e692dbf2-f698-373c-9c3e-c6da9956f6c1 | -14.43847 | -51.9305 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5eb9bebe-b61f-3963-9822-3d5a8a084139 | -14.71372 | -52.8843 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43d27b81-fb6c-3f21-8ba2-ac1a18039017 | -14.44719 | -51.95131 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06b08143-f8de-3895-86f8-53d3f0ea819a | -15.12475 | -48.69809 | 2026-08-15 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f912a69b-5e41-3f37-87c1-0a0775c29571 | -13.26266 | -54.19741 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f966fa84-9de4-3a10-9f8e-3eb1e539ff38 | -13.27963 | -54.20002 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d058935-6536-3aba-b730-05315d915ad4 | -12.74241 | -48.43943 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88465049-c235-382b-ab41-19d263af458e | -14.44608 | -51.93164 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b007a1f-0a92-34d6-886f-59759442064a | -14.31979 | -53.06001 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebf5b75e-ad79-3897-ba69-f1c1d15af660 | -15.65108 | -48.21108 | 2026-08-15 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 36674aa8-77ab-30df-b1c7-bdb186c4510f | -14.44026 | -51.94542 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db901ca2-b401-3ea0-afab-00c03e6e95e5 | -12.70939 | -48.43771 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06e6b7a9-1346-38f5-b506-a2632cbf75b5 | -15.10519 | -48.70045 | 2026-08-15 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32e165bf-c632-3f5e-aeef-8c36d5158ff8 | -14.96072 | -46.63282 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98cdb881-148e-3dd3-934c-7c602e77c5cb | -11.50216 | -54.64106 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8ab9ffd-01f4-3ea5-8a27-cb0d2fa4645b | -11.50657 | -54.63448 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 153a16d4-db2b-3b4b-9c83-4922cf9bd2ed | -14.30788 | -53.06666 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9310ad58-50b3-3b9b-88cb-ea166885a34a | -14.43802 | -51.90601 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6916e5e6-25a4-3acc-8cc1-4229ae63d0f2 | -13.91832 | -53.95347 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2322148-0da8-3345-affd-086efe8ab6f6 | -14.43735 | -51.9108 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 77dc7c5e-6e44-32b4-9640-41039cafe155 | -14.4402 | -45.69575 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9d2c462-8f01-3c52-ac5e-312244a7bdac | -14.71735 | -52.88482 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d921e9e6-976b-30f8-acb7-fe4a759043c3 | -14.48623 | -53.08795 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb83e75d-0d3e-3e80-992a-a8fbfea2ce24 | -14.45613 | -51.91035 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fe1d121-696b-3ef3-9433-e12142a44ee0 | -11.5861 | -54.69109 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9ceaf018-13a1-304d-9dde-cacd112bcd74 | -13.54115 | -46.25323 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a03f1e2-1574-335f-b1dd-f8cc8fafa143 | -11.48544 | -54.61662 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0932e22b-0a06-3cdf-8e3e-0f71f629b9a4 | -14.44161 | -51.85252 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29ffdb0c-dc14-3083-8c96-e85055a0034c | -14.91589 | -46.63973 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README30.md)
