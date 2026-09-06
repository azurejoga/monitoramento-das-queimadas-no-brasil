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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8559544-abf1-35ad-8436-4cf8e6dd47a9 | -6.12873 | -57.74993 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 559dd636-a9b6-30f5-966f-4c98d1b76877 | -5.34365 | -56.02053 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67db37b4-15f5-345f-b037-c8a039e75498 | -3.15957 | -50.82546 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e534eda-b529-3241-888a-ce5af48ac701 | -5.36324 | -56.02746 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b312426d-ba8d-34fa-bec1-7808be7a79db | -5.15135 | -55.96935 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 21ad67e2-e004-3bb1-875f-221da671fb08 | -5.3569 | -56.0155 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5299bcf0-58dc-3f5d-b53b-d9a5a38115cd | -7.45075 | -49.7277 | 2026-09-06 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9236a503-879e-3cf4-97e9-c9a58e782957 | -5.64912 | -60.23373 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd78af39-e38c-35d7-bef8-b5cdf33c0e21 | -2.45936 | -57.91733 | 2026-09-06 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b91942c3-4088-3974-b655-8d5569b222ae | -6.02084 | -57.69263 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 59d82e85-0c16-38a1-8e78-10c6b2bb490f | -5.36613 | -56.03522 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 728ce038-a75d-368d-9a0e-a372743d93fd | -3.85846 | -51.03396 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d35007d-f989-374f-820c-3ea0d710b105 | -3.62387 | -54.60912 | 2026-09-06 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fcc5733-530e-38df-852b-8f8548f817a6 | -6.06263 | -57.80094 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb2d6a65-b65a-303a-a9da-7260546cdf01 | -4.47711 | -55.09192 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd8fb8ad-4559-31c8-ba25-598c2b562759 | -5.35748 | -56.03745 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5f22d5e-a9fb-3ec3-9bb5-0f8f5a1de244 | -4.47326 | -55.09129 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad47ad5c-3be4-3476-b643-688d1b320367 | -2.46028 | -57.90984 | 2026-09-06 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a9921995-cb35-3da7-8d8d-5703fbd0c6cf | -6.25503 | -51.84605 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ec7ca6b-81ab-3bec-91d1-97f0dbbecab0 | -5.15364 | -55.95524 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05987fb3-09a5-3378-ad05-5f9e94095a77 | -3.23294 | -50.57613 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d389def9-c0ab-3d29-ad02-80f350a39d4e | -6.06337 | -57.79642 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9782f0f-7d00-32e7-bb36-31250f30e851 | -7.10403 | -56.51905 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fdbe7e72-6cd4-3e25-8806-5412f996105f | -5.92485 | -47.89617 | 2026-09-06 04:46:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3837db89-1f81-3af5-a4c7-eb093e6ffc7a | -5.33845 | -56.02699 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 200d64eb-5d75-3ce9-9e91-74212262ddaf | -12.46366 | -54.43069 | 2026-09-06 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2a01768-4d36-373d-8de2-36ca1d26122b | -10.75254 | -60.71904 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 020510e8-5b78-302d-9278-6ded6a81cfc3 | -13.80702 | -51.677 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d3c444a-34e7-3a5d-9876-a919ec651500 | -13.75572 | -51.66116 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82a09736-e880-387a-9937-beb123add163 | -13.42958 | -41.89704 | 2026-09-06 04:49:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5823e821-a358-313e-bfb8-98be29cde7f6 | -10.7587 | -60.7141 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 58149b6b-e2b2-3f08-9abf-154069bbc245 | -10.75028 | -60.731 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f163ee43-af8d-3f73-8def-82b94f54ccdd | -13.78305 | -51.63939 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ce17f97b-2e4e-3274-b03f-91108517158b | -10.75086 | -60.73604 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb94908-db63-362c-a204-b2986f92a430 | -14.91451 | -44.67067 | 2026-09-06 04:49:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa25223e-028d-3ec2-8ce5-2f47ed7b0bb2 | -10.75303 | -60.72404 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c92b1b28-b602-3910-bba3-2469b9588fad | -10.74346 | -60.71923 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55b65236-0b70-3f7d-b6cf-e9517bb0d58a | -10.75197 | -60.72202 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fcda58b-fe13-3a00-8123-b42e4549bf9f | -10.75357 | -60.72105 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2fe8c91-8943-39a9-a20a-f14d07c537fb | -13.86835 | -44.30606 | 2026-09-06 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb5ab80b-78d5-32a0-b3ff-c292c2825faf | -15.00959 | -48.62315 | 2026-09-06 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 247b40a1-f9c3-30d5-8644-65ce735e2340 | -13.43723 | -41.88234 | 2026-09-06 04:49:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| db589ab7-9823-3311-8c8f-97e53a2f3bab | -13.77244 | -51.64144 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d6fd6c3-9075-3fd6-83ce-ef7985afe640 | -13.77804 | -51.64977 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2929a969-9204-3a96-b2b9-1440f2abc289 | -13.7808 | -51.63158 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f28e68f-bce3-34f4-82dd-1bd1c3b0bc84 | -10.74487 | -60.76913 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42fb406b-e191-3841-ab87-644650503559 | -10.7496 | -60.71415 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 788169fc-3701-3232-a249-0b85be17308d | -13.77915 | -51.64249 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b85cc34a-c6bf-39e8-8bfc-740982099001 | -10.74861 | -60.71215 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7a9c0327-694d-3454-b61c-677ea76797f6 | -10.74805 | -60.71514 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7f3c2d9-6060-35ef-9006-3a07f82fa7a0 | -14.14553 | -52.88494 | 2026-09-06 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6276016-759d-382b-ad05-e0dc15737c11 | -13.8049 | -51.67638 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2536a724-71a3-3097-9a72-00bd3625f1ca | -13.77859 | -51.64613 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00b68537-84be-3bf8-97a1-fbf5ac1c47b0 | -17.43287 | -40.02413 | 2026-09-06 04:49:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b3ac792e-c171-3ece-bca2-cf096fe220ea | -13.43607 | -41.89264 | 2026-09-06 04:49:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 46593f33-53f6-33ca-961a-e8b6eced5984 | -13.76743 | -51.65183 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 859eafd3-5f79-3955-b961-914640f92814 | -10.74972 | -60.73399 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bf65efc-db77-39c6-b159-74f7c336721c | -10.7398 | -60.76818 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dae86536-93e0-32c5-b9d6-b076982f822d | -10.75862 | -60.72202 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed9b9727-310f-3b51-83b4-a35e285129b9 | -13.32381 | -44.04048 | 2026-09-06 04:49:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae370bd5-be0a-3b1e-aa96-d13f46c51fe5 | -13.75292 | -51.65699 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e064e121-4d5b-34e0-aa3d-6f9b7f2f51cf | -10.75756 | -60.77578 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a721028d-ebb7-3cc5-9030-c8486cd1ceae | -16.76002 | -49.30304 | 2026-09-06 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcab3a96-2bd3-352e-9156-e0e8bd05d03d | -15.08965 | -52.51699 | 2026-09-06 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 713c36a3-ff5d-3c1c-aa25-e8b2ee1143d1 | -12.61866 | -52.53822 | 2026-09-06 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e854ed9-6905-38b6-89d6-e65db991d731 | -10.74917 | -60.7092 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b43f642-7f60-391d-9b9c-b6d8329bbe43 | -13.35325 | -61.13234 | 2026-09-06 04:49:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe4b8ff9-87f4-31ac-9be9-1e026fa1587f | -17.42646 | -40.0167 | 2026-09-06 04:49:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0948be3b-9995-39dd-9f45-7244cb572315 | -11.50315 | -50.256 | 2026-09-06 04:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7f129ba-79c9-3eae-ab32-546b2c2e4a77 | -16.39989 | -49.20193 | 2026-09-06 04:49:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a54d2f58-fb5d-3fac-b955-8953b06d37d9 | -13.4307 | -41.88708 | 2026-09-06 04:49:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c963f273-fe6f-3c6d-8505-3159e39cbe7b | -11.94572 | -44.86163 | 2026-09-06 04:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a12b051b-28c7-3194-b6ed-0dbf7d9f8a17 | -17.42657 | -40.01635 | 2026-09-06 04:49:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3f2f55e6-1a8d-3747-9ad1-983ebef64c19 | -13.77579 | -51.64196 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8175144e-324b-390f-bffb-02c59badbd3e | -14.91953 | -44.67135 | 2026-09-06 04:49:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf11a1dc-a834-34ed-ac40-4aa0e75f159b | -13.77189 | -51.64508 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8f38147-9f67-34e7-add1-e9a135e90e72 | -13.33433 | -54.05112 | 2026-09-06 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d91470d-5d63-3781-b37f-a9d31fe7c5bf | -10.75814 | -60.71704 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 498d3181-07c9-3f82-99a8-0443adcd5b2a | -13.80037 | -51.63842 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a972ec1f-ce76-351a-ba4e-e1218d01b908 | -10.75421 | -60.71017 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e2f66aac-c3d9-3fa7-8c00-4927590688ce | -13.75237 | -51.66063 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86f00e5d-9fa1-3363-ba54-934031508dac | -13.77524 | -51.64561 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e32d910-7746-3497-8795-02e951d4c488 | -13.75963 | -51.65805 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 84db1246-6f16-30e9-bd62-355488ef7e18 | -10.75014 | -60.71117 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e25d9353-3f4f-356f-8498-edeb36374b5d | -10.75366 | -60.71312 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fb24a86d-89bf-3acb-be94-502e1690479e | -13.32419 | -44.03731 | 2026-09-06 04:49:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f7a4cad-6b46-3bb3-af77-5025dc0b092f | -10.75813 | -60.77272 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31e6d16a-3d3e-355d-80f6-f97314685eea | -10.744 | -60.71621 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ed3bdb5-a604-3fe0-8067-ee9f1f75db8a | -13.86871 | -44.30306 | 2026-09-06 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3da0616-7453-3d17-a22b-76bbc6e13ffe | -15.70685 | -56.12221 | 2026-09-06 04:49:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12714454-161a-3718-b86f-6aef559eee85 | -12.40543 | -55.20791 | 2026-09-06 04:49:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 257c38b7-aa42-363a-84b8-d0e8693b2b91 | -10.74797 | -60.72316 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b153bc87-2606-3293-b24f-4e8018bcc095 | -13.7797 | -51.63885 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b34039df-272a-354e-bf5e-de83c2d887e8 | -14.26897 | -51.95013 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea13faea-28fe-3dd6-bf52-4cec3eb8d647 | -10.74291 | -60.77001 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc6523b3-5278-3ec1-9d65-b3545523f178 | -13.75182 | -51.66426 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1e397f1-d674-39c0-91d9-3a9eb7752deb | -13.7836 | -51.63575 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf33afa6-f553-30a5-93ca-d81d95fb3a16 | -10.74906 | -60.71715 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27939c14-97d1-31f4-9520-d4ae1d13d9f8 | -13.79702 | -51.63788 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fc180b6-0927-3a09-9780-81d1a246a4ce | -12.92672 | -46.94645 | 2026-09-06 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README22.md)
