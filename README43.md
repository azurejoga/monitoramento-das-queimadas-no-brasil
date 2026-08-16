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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65653fc0-ac87-3fad-a290-1ea8bda17cda | -14.4214 | -51.82869 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d51763a2-8951-3610-adf7-8d24e45a5675 | -12.70002 | -48.48605 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d5feaf2-f815-36ef-bd19-07377df849c9 | -15.79095 | -55.57575 | 2026-08-16 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5c23e5f-a771-3782-b74c-9c4469c858d3 | -16.18425 | -55.95837 | 2026-08-16 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9458b020-4b87-349c-b914-0d61d123983f | -12.75478 | -48.432 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63504d71-15b1-3f00-89cb-649b0358b9e0 | -12.71831 | -48.46753 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ece615a-bf1e-3c95-9af6-f3b57f8225e2 | -14.41515 | -51.93913 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e514853c-673a-3420-8d1e-f7d81ea2d432 | -12.13379 | -57.20748 | 2026-08-16 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84012655-dc76-3588-9c4f-984b8e2d0c6b | -14.38236 | -51.89347 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4976305-3c98-3d91-b54f-b8d36736c7a8 | -12.75481 | -48.43203 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7492c16d-0901-35f4-a5b7-5ba0c08c392c | -13.80004 | -53.78629 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c8edc2-0893-39df-aa99-1b83599eeea5 | -13.44096 | -43.84365 | 2026-08-16 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5202dbe7-251f-3062-9592-290ecbff11a9 | -14.49274 | -51.96911 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1dcb1e0-b2e4-39f4-85a9-c813a8e4e3ea | -14.39241 | -51.91543 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 299657dd-4565-382e-ae91-132fc84d7dae | -15.17495 | -50.06806 | 2026-08-16 05:18:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9d291cfa-ba17-3d92-8dc0-8ee5d4c36a76 | -13.70067 | -46.27016 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ee6951-5d52-3c05-b40a-c835db039f1a | -14.90529 | -46.64017 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89fe4721-f03a-3632-9e97-ec697c959e11 | -14.91144 | -46.64013 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5e932ff-cdc5-3d8a-8a6e-d8a664a87405 | -14.7458 | -56.34976 | 2026-08-16 05:18:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0cef835-990b-3b33-84fb-ea1cfa31df29 | -14.39295 | -51.9114 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8b46b866-386e-38e1-92cb-fd99e4f87ce5 | -15.09929 | -48.71984 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5abb8e8a-6c55-3dc1-b73e-fc52b6baad5f | -13.80073 | -53.78143 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b83ed2f8-0f2c-3de7-bf92-19b51e5a3411 | -13.70676 | -51.87887 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67c26489-22c7-3d12-aa18-104afe7383bd | -14.89756 | -46.6548 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb7ea5ea-3b72-3ae6-b2c9-571bef694a9f | -14.48754 | -45.69176 | 2026-08-16 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc3b5d4e-97e4-3e14-a3ba-8f1589990cff | -14.76442 | -56.36424 | 2026-08-16 05:18:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c35dfd0-af65-39e4-827f-b9649c0cb5cd | -14.07646 | -53.70882 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e572fcb-bcbd-314f-b3b0-450e72449c30 | -12.69635 | -48.47286 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dcd05284-11f3-391f-aba8-8e4e13c5b687 | -13.79811 | -53.79987 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bef4248b-5064-3909-85f5-9501aa8ee94f | -13.70255 | -51.87827 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 690b5d04-8b1a-3b70-8768-c4dba532feb6 | -13.79874 | -53.79543 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dffbdc26-df7a-3292-a50c-21e8c391b7d6 | -14.41776 | -51.95175 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11a5812c-5a1a-3bff-b1b9-6dbbb971af7d | -12.8997 | -52.82536 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78acac79-7dac-31e9-9dd2-ead4fc2e7b29 | -13.53559 | -46.24551 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d16102eb-eff6-397c-ac98-c394e4cb7d81 | -11.58268 | -54.69237 | 2026-08-16 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a35600-bbe8-35c2-8084-9a6eb5fde960 | -14.38823 | -51.88193 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ba86b03-fe1d-3d08-b989-ebd4c824742e | -13.50313 | -48.23131 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dd9f649-2585-3cff-809c-b2169422a4e2 | -11.57976 | -54.68789 | 2026-08-16 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9daa6f40-5897-3ec4-878e-677f8d5468d2 | -12.67699 | -48.45747 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80d99139-56fd-3cba-bb85-bd673fde9f15 | -14.32937 | -51.97341 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e10198cc-84b4-3a22-9328-c4b1682eb6b5 | -14.07445 | -53.72274 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fcb05b6-965b-3c79-bcfe-3b9a44217653 | -14.32837 | -51.97582 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 81f95894-5855-30d2-ac14-5f60732e8ba0 | -12.9029 | -52.83095 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5302273-3d09-340c-bc8f-552f7a7d12ca | -15.14823 | -48.62635 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22d2c9a9-5adc-35df-8137-46c3561afdbb | -13.6902 | -46.25301 | 2026-08-16 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b56812e3-c565-3556-ac76-c38563801e6f | -14.76103 | -56.3637 | 2026-08-16 05:18:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a13ea8d0-98aa-3087-b90d-c27fd91df775 | -12.69596 | -48.47602 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2091ab6-8cad-3220-a7f5-250f92ba57d2 | -12.7075 | -48.4688 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f346504d-864d-39d9-922f-f5be7a20d943 | -14.0606 | -58.74453 | 2026-08-16 05:18:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 634bd725-6386-3d21-a038-9f33792d9282 | -12.70076 | -48.48014 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fceaa110-7460-3419-b8a8-2beec6c4908c | -13.5295 | -46.24851 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b9a7776-7f4b-3e77-a596-64b0bb8dd3fc | -13.54796 | -46.24577 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae76c2ea-cd82-3273-9299-6be70291d942 | -16.20907 | -57.64002 | 2026-08-16 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cb1577c3-59fd-36fe-ae0b-b34f2956d6bd | -12.69036 | -48.47826 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cc96538d-5948-3222-9538-808dca28301e | -13.80446 | -53.7821 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3774d389-16ab-3100-abcc-a27ba54614a3 | -13.90714 | -53.94831 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c98e0ae-f9a5-3336-b94d-6f924e89a718 | -13.90778 | -53.94384 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68f13985-4aeb-31bb-a4aa-4fb2228dbf4d | -14.23842 | -51.81275 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97419f73-5424-302a-ac63-fd5c54b07b1e | -14.31467 | -51.95498 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c185b79f-a3cd-34d1-bfe8-974c3c40fb45 | -14.8996 | -46.63604 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 991f5bec-0f76-3a1a-ae32-e7fc0d159123 | -14.65648 | -55.87633 | 2026-08-16 05:18:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 707916bb-6e9a-3432-a2a4-b825f6a9a6b0 | -12.90361 | -52.82594 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70b51a15-25cf-3c11-ace2-11af24e23f51 | -12.67178 | -48.4565 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebed5526-cc81-33d9-bf82-21ad4c4557b7 | -13.50851 | -48.23201 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf38b400-07c1-3124-b262-a993b79e7d41 | -14.46258 | -52.00152 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50e2018a-87f1-3653-b949-b28f2d9fe162 | -14.75821 | -56.35942 | 2026-08-16 05:18:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22695ef7-9fe3-3da4-8ffd-aab5244d5a8f | -15.17008 | -50.06747 | 2026-08-16 05:18:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c309d95-8283-3146-abf4-f1ca507d401c | -13.79424 | -53.827 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2aad3cc1-e354-309c-8a30-8704c91ca1f3 | -12.0606 | -58.04493 | 2026-08-16 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ea0fcb1-d165-3633-9a34-a3111eca01f5 | -12.74917 | -48.43431 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e5f3baa-554f-3c0c-a46b-c4c668878e84 | -14.41406 | -51.94717 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7ba86af-8bd8-3529-9157-a54aca4d1c44 | -16.66841 | -49.14091 | 2026-08-16 05:18:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a902d569-c900-31b5-af97-d066c91d6497 | -14.3695 | -53.10826 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31001313-7945-37e0-852e-2da8f85390ad | -14.42567 | -51.82929 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51231b11-838c-39bb-9433-b8659a2355f4 | -11.58326 | -54.68846 | 2026-08-16 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6782aed8-5acf-329b-bf81-65cf9dfbc898 | -14.33249 | -49.17164 | 2026-08-16 05:18:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c8443b5-e013-37ec-a52e-484cfeba7255 | -14.06001 | -58.74816 | 2026-08-16 05:18:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72f5ee7c-b777-3a61-8008-5f9f84f8d9e9 | -13.41681 | -57.04941 | 2026-08-16 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16ea70c7-a763-38d1-9b12-47ae888fed80 | -11.58384 | -54.68454 | 2026-08-16 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5782cec-8622-32f0-89b6-a8b70af0366d | -12.204 | -52.86948 | 2026-08-16 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00cddf29-a1ad-3fe9-b5a4-16f7ab13b22e | -12.68948 | -48.44258 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65a6d7fe-b4c2-35ba-a372-c79d9fd7e64c | -14.92671 | -46.613 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b2eb3bd-9179-3814-ba07-0c61c75bc12b | -12.67344 | -48.44302 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9baaef5c-e519-31be-99bd-a2c63782b565 | -12.70633 | -48.47814 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a7a1b8b4-6e5f-3555-adab-f2e07493a4b6 | -12.6815 | -48.46399 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27a0bbd4-fa51-37bd-a84f-3c162aad2ce7 | -13.81265 | -53.7784 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 421657ba-fa21-3cb2-821e-a441bbc6c756 | -13.75348 | -53.43573 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a5c0718-6e78-38a5-93f8-c6e3fe8424d9 | -13.65392 | -46.24145 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 707a45e8-0b51-342b-880e-d5bef4a7673f | -9.51124 | -68.49996 | 2026-08-16 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 314f393f-11c4-3c2b-8d2f-28ee433898c3 | -15.23244 | -57.65644 | 2026-08-16 05:18:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58d1bc52-2dc5-3d9b-96da-396aa7af7991 | -12.68593 | -48.47115 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 454d725d-a437-3fb2-b486-a6a1dc415d5a | -12.67104 | -48.46252 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c17557e5-9bd4-3b39-a919-2a5199427e24 | -14.89799 | -46.65082 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 03c09c93-a3e0-36f9-a4c6-198a7316ab9a | -14.30044 | -53.05628 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d3bfb75-e4ba-361d-892a-507868462dcf | -13.52941 | -46.24533 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a2d2835-15ff-33a1-9098-986e0c489f6f | -14.37343 | -53.10882 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d916d65-9ef9-3e4a-8ad1-4262422b651c | -12.74918 | -48.43435 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dd77f78-7f1a-3c84-b065-db00623084a7 | -13.26287 | -51.67653 | 2026-08-16 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b29e4242-a5b1-3041-8ec7-6f7835f94725 | -17.66536 | -50.48846 | 2026-08-16 05:18:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abc03a22-dec2-3ae7-a42e-341d9d3ef7de | -13.65345 | -46.24552 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README44.md)
