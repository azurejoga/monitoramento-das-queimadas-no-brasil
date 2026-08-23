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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a10fa9cf-6bff-37ee-a618-d040ea789c17 | -12.59427 | -47.88617 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5c42cbd-7277-385c-a2a0-68e58b3aa74b | -14.35825 | -51.82741 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f143be3-567d-3406-b8c3-698715d684a3 | -10.27446 | -50.38225 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6f87800-8f4d-3f29-a1c8-b787e3b91ba2 | -13.09553 | -43.34998 | 2026-08-23 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9663d941-809b-3fa6-8777-733f41b6868c | -13.2591 | -51.59851 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b948a77-cd20-3680-9c40-637a63d0bbe9 | -12.21499 | -43.15173 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7d225527-ab87-3754-8643-aa8ba1c9ed0b | -14.36587 | -51.78143 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd294f7b-976f-3822-9f30-824ea0cf9cd0 | -10.01566 | -44.28167 | 2026-08-23 04:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efa7a851-e90b-31c6-96fb-a21c7eb19e38 | -11.36614 | -46.94672 | 2026-08-23 04:46:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a3a08de-bde5-3178-93ed-b920f9990db4 | -12.01576 | -55.34221 | 2026-08-23 04:46:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0daa6763-c930-3a0d-94ec-3c68c4f43094 | -15.33693 | -52.77836 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d344aa94-37f5-397a-98da-2a7c3d089383 | -14.95406 | -52.65077 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a28eb2c9-1214-30ec-9e2a-ba73ec27dd56 | -13.18046 | -51.42135 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fd037c8e-ab08-3422-9e3b-4ea4a322b65f | -12.74232 | -48.39574 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69a40120-07b2-385c-be56-4cfc72796edd | -12.25603 | -43.18493 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 80d48df2-b8ec-301c-bca8-6dbe94fa40da | -9.79906 | -46.61749 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2b343db0-c5ca-3685-be7a-0ba4595319ed | -15.75969 | -49.96827 | 2026-08-23 04:46:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49f4b448-e090-3d67-a1dc-bb502166666e | -9.12343 | -61.59204 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1244636f-8ecc-303b-bd40-5d6ade2ff7c6 | -13.17235 | -51.42773 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f877f862-a08f-3953-8d75-129fe27d0bd9 | -12.2649 | -45.0783 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6024f88-0c3c-3cdb-9695-e65cacd325ce | -13.16955 | -51.42336 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f3296ce-1f8d-30db-bc78-e3a34c288084 | -13.84342 | -54.01096 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9730a589-4a09-30ee-9d60-576d6b384465 | -12.22251 | -43.16135 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ce2d66df-5852-35ea-bff2-93a8dde42795 | -10.55764 | -61.46301 | 2026-08-23 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca021219-75ee-37ba-856b-069ca9eceb14 | -10.8413 | -50.97564 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3553a088-4007-3570-8cb1-9851138d5868 | -8.55779 | -54.84691 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983b18e8-d250-3ddc-ad6d-9dad5e2b3325 | -10.51929 | -50.4488 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 45647736-968c-34ea-9d79-15e17572be53 | -8.96595 | -50.75346 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35054b09-983b-3190-abad-d91c49eda356 | -14.99369 | -52.69029 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c10e1e9-58f2-3a58-ad1f-7d4890353181 | -9.17413 | -58.33815 | 2026-08-23 04:46:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61bae463-d919-3cce-a116-70dd1d67b283 | -13.16423 | -51.43412 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46c012aa-ecae-36f8-b519-6efcb27d1cb9 | -16.28809 | -48.01949 | 2026-08-23 04:46:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dfc0aa7-f127-3449-89e6-a0c381edb3f5 | -15.70341 | -48.27648 | 2026-08-23 04:46:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df8ce582-2844-3590-b010-fe4fd2caaa56 | -8.53281 | -54.80754 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b1e6662-c5ea-3e32-bc24-4b3698f081c8 | -15.76046 | -55.55597 | 2026-08-23 04:46:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01afb1aa-4f43-3770-b724-fc90a393f7a7 | -13.83872 | -54.01517 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79cadf35-1803-3b62-a846-7b08b971fa29 | -12.7317 | -48.39769 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cefa0f7-f50c-3499-9a18-a992c0b48fec | -13.8939 | -54.00229 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16deb880-2766-3d8c-b8fa-a34369935605 | -8.53642 | -54.83916 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b08e37d-a39c-3adc-a3f5-a64a34fc3e8e | -10.51603 | -50.76794 | 2026-08-23 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bb54cff-4e15-345a-b7e4-c1e4ca097bdd | -8.58448 | -54.79257 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ff31c0b-b947-3bc0-b1f7-febd28fa9440 | -8.96471 | -50.76101 | 2026-08-23 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2285c07e-dd9f-383b-bb7b-da2d3301a0cd | -9.15626 | -59.48161 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b21b3747-6f59-3f38-ab80-749fbe279bc2 | -14.38648 | -51.78506 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab78a931-2d9d-33fd-89ff-00167e7addc6 | -16.05754 | -50.43398 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3ef0df7-799a-3274-b2b3-c94b1387dbc8 | -10.30788 | -45.36096 | 2026-08-23 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23ac0a26-0a65-3f7b-9e50-92dbec710290 | -9.19323 | -59.44831 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 32e3f3ea-7819-3a40-8460-83beaf064a81 | -12.73562 | -48.39458 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 194ad9e4-8f6b-3ce0-9706-e4e3fad2326e | -10.45853 | -49.96576 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 628dcfba-fc0e-3d06-9fb8-094904dac3cc | -9.85667 | -60.10338 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc88f55d-e280-3f76-9cdb-977b1068a9cf | -11.05794 | -49.51012 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 057f3c8c-a765-32fc-ac35-50aa6a4502d4 | -7.59978 | -60.94678 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed5e96a5-3b4c-357b-a0c3-f21f393428ae | -13.19074 | -51.42313 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8416dcee-62b5-3c29-8f87-171f4757f9d4 | -11.1466 | -46.20084 | 2026-08-23 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fd8e087-30de-3c18-8f04-6a2ca51923d3 | -9.10321 | -61.58826 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f68b6297-778b-3527-bd48-4f4320d659fc | -11.9385 | -45.52516 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75ef33b3-6b33-33e6-92a3-f3b8075cf963 | -11.21157 | -55.04554 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 142f0d33-36e5-35f8-b3f2-c22d6c063d8a | -8.53865 | -54.82623 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b1512f-d1de-3922-884b-d6b7bf3a8ef9 | -14.56182 | -52.99811 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dc28fe7-5f38-384b-ad8d-86cf8c531fb5 | -11.43829 | -44.53349 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d020b2ad-2eec-3bf1-ab4f-0991556a672e | -12.78384 | -48.38326 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7831dd11-f9b3-35f6-96c6-80e08c8d351e | -16.05307 | -50.44059 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 58f6d5ce-80f4-34f7-a72e-00c63134ec98 | -12.84306 | -48.46703 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3032ec47-ee18-3f29-8ec8-67782484ef7e | -14.56242 | -53.03791 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5070ae44-a1bb-36dd-a774-eddb096d1208 | -12.24245 | -43.18733 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9f7e96f0-f7b5-3150-8372-9cdf7947d48b | -15.24708 | -52.86039 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac67c10e-1818-3f25-99d0-06364526c69e | -15.31748 | -53.79811 | 2026-08-23 04:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8cf8cea2-ab88-3e74-8700-d38175020029 | -12.75743 | -48.40911 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0700efe-d52f-3ae6-8892-0067335129af | -12.25549 | -43.18888 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8ecf43b9-ae3b-33a0-a665-2545977af3f2 | -16.18622 | -46.48376 | 2026-08-23 04:46:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4708cef-7c04-3106-a473-ab2baf90d8f0 | -9.8584 | -60.12755 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1555364c-d0e7-3c07-bb59-b00195afc43c | -13.17298 | -51.42395 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5ede36f0-b83a-3599-bb39-c62332b0adc3 | -8.59437 | -54.71127 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1da25f04-6306-3431-aa89-7796d62b1305 | -11.21084 | -55.07487 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7d9599-eb8e-32fc-a7c6-b987df1085a5 | -10.69944 | -47.72809 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 486b3b1a-b9c6-3567-8cbe-9f16f1f84ca9 | -12.84532 | -48.47464 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0090526f-b501-3fcd-8da3-66db4b7abe76 | -9.58972 | -60.50183 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f0beea2-762e-3ea5-ade5-790d212a5adf | -8.51824 | -55.32343 | 2026-08-23 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b9af781-806b-3328-8e88-fedd226ac620 | -10.45708 | -49.966 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20180e80-abc4-37d0-8ef9-2414d5c9a7cf | -13.18326 | -51.42573 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cd801dd9-6d7f-32be-83af-e751cd442a88 | -16.05422 | -50.43341 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 95102cb2-982b-3b56-88be-d2eafba99d4e | -9.02161 | -50.7395 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48522d7b-936a-331e-8602-3187e32bd5a1 | -16.06477 | -50.43152 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f24cb1f6-2d2b-3dac-a5a8-7bd2722d4c80 | -16.06087 | -50.43454 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f6172ad-ae80-35ff-983e-e9a7f1d9a4b1 | -12.24299 | -43.18329 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dbf3f705-85e4-38b1-9d91-5548503ffb00 | -12.84143 | -48.47759 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de85d765-637f-3320-a655-2af81f8f6747 | -12.73955 | -48.39145 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 382ed0cc-ddc9-3cb3-b96c-297746f70a3b | -7.43803 | -59.77581 | 2026-08-23 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 889287d5-b709-3834-90bf-a497cc6be267 | -9.03634 | -60.44706 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d227ce77-3f7b-3ffc-8955-88f6c73c4e71 | -13.15927 | -51.42158 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ac9f3b03-493a-3675-830c-627165272842 | -9.52826 | -51.64653 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fd99176-61eb-35ef-a322-8d77f43c7e4b | -14.96182 | -52.64787 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74c23896-5a3c-3f2b-ba5d-b5cabab0994d | -10.71271 | -47.74098 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 622b2209-bd8f-33f0-abe5-7961c598e883 | -9.51767 | -51.68038 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2f87e39-5e89-34fb-88b3-0be626cad4e9 | -8.96628 | -50.77308 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b13c103-cdc9-3d18-a614-9b9cf987138a | -10.31122 | -48.21536 | 2026-08-23 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6389183b-58b3-362c-939f-99a65f7c138a | -9.44541 | -48.23653 | 2026-08-23 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b56beb2-eeaa-3479-a729-ad037ba9a02a | -12.84585 | -48.47113 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4f366a9-def5-3d11-babf-c2054a0c15e4 | -10.68709 | -47.71875 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fca20aac-0d33-3d34-a358-974d34d43e28 | -15.22161 | -52.77454 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
