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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17c43a80-3e0d-3f00-8d8c-78c21b94d512 | -12.70601 | -46.97924 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d30b229-59f7-3163-a1a6-2150059ef91f | -13.70906 | -45.68167 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0164923b-4f9d-3acf-a472-116fec60ef92 | -14.93975 | -46.97968 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a770f06-d26a-3cda-abac-6391b58d8a03 | -14.20956 | -43.94978 | 2025-07-25 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d06167a-62df-3590-9d95-a7e3f1d5de2d | -14.93585 | -46.98271 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fe9b808-9bc8-3ebc-aa08-01a52b65d7b7 | -15.56727 | -44.76317 | 2025-07-25 04:23:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c45a7db-3cc2-3269-945b-0353430be12e | -15.91859 | -46.08531 | 2025-07-25 04:23:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef3eeeab-3e0c-3c74-8e10-8860bfd51fdf | -13.7146 | -45.66791 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb3754af-89c4-3a72-800e-adbe9d520f92 | -10.63321 | -55.31357 | 2025-07-25 04:23:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b4c1d1-bf3a-3737-a585-b306986e96ac | -15.82845 | -45.77682 | 2025-07-25 04:23:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79f831cb-702a-34b9-9d7c-eb0e518101c8 | -11.94074 | -58.76607 | 2025-07-25 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81893849-7eb5-31f3-bac9-490dfe62700b | -10.04043 | -59.10297 | 2025-07-25 04:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20dc4b19-ef70-3170-b2db-8713ac2e0466 | -13.64424 | -45.71175 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80276d9c-1ced-3041-8c10-a3daf83c1e78 | -17.50982 | -44.67104 | 2025-07-25 04:23:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d7c61df-cd3d-32cf-a08e-591e8126f018 | -17.70512 | -44.30743 | 2025-07-25 04:23:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8901659d-24a3-3bff-9c4a-c19b23835632 | -15.58332 | -49.85068 | 2025-07-25 04:23:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 94cf8ca2-34ac-3b0c-8595-e30b3d8bdfb9 | -14.94858 | -46.9885 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00abffbc-43a9-3297-8ea2-36094fdbd397 | -13.40485 | -46.80168 | 2025-07-25 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bca77758-850a-3b02-8659-65d8b67022d5 | -13.70808 | -45.67455 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ade6dcc9-4493-32c0-a94f-3f0a873ded59 | -14.94365 | -46.97662 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b4250ac-ad8b-3bf5-a5dd-a4dd2c6bdd0b | -15.5905 | -49.85194 | 2025-07-25 04:23:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2602ceac-ba6a-339c-996b-71bb8401e86d | -12.25847 | -44.58459 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 151aeac0-3350-36ab-8d59-3dc5a219da5f | -12.69482 | -46.98481 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b9e4374-e3c1-38a1-a306-eade69b1623c | -16.08809 | -45.16971 | 2025-07-25 04:23:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 038a474d-7a19-3779-a153-b32522de079b | -14.21307 | -43.95032 | 2025-07-25 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfac0d1a-e9b6-3e1d-be7a-0df7ff014bae | -12.4249 | -45.37843 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1a79ba9-9855-36f6-a7e4-867b97963719 | -15.6011 | -46.52134 | 2025-07-25 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 422a39df-2970-333c-9a91-2df7ebd9578a | -12.04809 | -45.42693 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81a130ae-9567-3c16-b88b-29c870a67f1b | -15.57071 | -44.7637 | 2025-07-25 04:23:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 311f877f-01d4-39b2-827d-ff3a500da666 | -14.94974 | -46.98129 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0f4f8bc-cd6c-3679-8c4c-d96006c63da4 | -16.60506 | -47.966 | 2025-07-25 04:23:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b44ef613-7f00-33ad-a1e5-d46809ef23df | -17.75608 | -46.17604 | 2025-07-25 04:23:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a24d00b5-d38f-370f-8f34-f5e25535401a | -16.5095 | -50.85292 | 2025-07-25 04:23:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1fb59a6-3ecc-39c2-bd58-cd1bde7234d8 | -15.58259 | -49.85491 | 2025-07-25 04:23:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a42d44d4-1bc7-31f8-aad2-1fc99f6204aa | -14.30417 | -43.79584 | 2025-07-25 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dbdc3a6-ad1b-3b16-b4a2-d21e760e375d | -14.95031 | -46.97768 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77217d33-0651-35c9-a635-ca9f8bf9988c | -14.3065 | -43.80447 | 2025-07-25 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 003e1c9a-d46a-357b-ab8c-1bef4ce163cc | -15.05264 | -47.68705 | 2025-07-25 04:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b056a88-313a-35cf-b0e9-b64b588fde8e | -13.7185 | -45.68687 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f23f0962-f8ea-3349-a386-a615638cac01 | -11.32175 | -55.2154 | 2025-07-25 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b181b41a-f4fb-36a4-9307-44da44352a78 | -15.05205 | -47.6907 | 2025-07-25 04:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9567eb40-6a37-3dba-aa82-ab2bb678af90 | -17.75272 | -46.17549 | 2025-07-25 04:23:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93b04925-dbea-3746-954b-21b2670cefaf | -13.64479 | -45.70819 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 122e2bb2-14c0-3590-82ef-c659cf1789c4 | -12.42379 | -45.38554 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfea43c6-4c38-3d01-981d-1f308047e643 | -15.58618 | -49.85556 | 2025-07-25 04:23:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 406b6dbb-8b7a-35e0-b623-ae1bf62eed02 | -12.77603 | -48.8168 | 2025-07-25 04:23:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b9d8e4d-0942-3025-bc00-40993e6a49ae | -17.30313 | -44.85764 | 2025-07-25 04:23:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc30f0a5-62eb-349d-8c61-3f22c528c99d | -12.05032 | -45.43454 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55f5ce18-6ed8-35b4-b155-724452f026c1 | -17.59633 | -43.19717 | 2025-07-25 04:23:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f4d525f-3964-310b-8439-a3a4d16e4a4a | -11.7797 | -47.32499 | 2025-07-25 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07e31b95-6390-347f-89cc-ee8db6801816 | -14.65503 | -46.83363 | 2025-07-25 04:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a4b5314-3ee1-3905-b70f-ccc4fed30b19 | -14.53652 | -49.13837 | 2025-07-25 04:23:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9cccc24-50ff-3108-8e61-1407e51b08c3 | -13.70863 | -45.67098 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25e79e05-b001-37ab-8c31-110fae2ab32d | -15.59722 | -46.52437 | 2025-07-25 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a165a4-ff3c-3b8c-b5fd-82a1cd440479 | -15.60054 | -46.52493 | 2025-07-25 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 847ff033-ebdd-3a42-9874-0a72c9f3ac45 | -13.69697 | -45.68007 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3783177d-0570-3745-905d-551f31cdd6e9 | -12.04366 | -45.43346 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5c6437b-db8a-37cf-9621-9f76740e8357 | -11.67623 | -58.48784 | 2025-07-25 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce216304-ca0d-339d-9c72-d4475e1dda69 | -13.21119 | -51.11206 | 2025-07-25 04:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e65707d8-5aa1-3343-b77d-0dd3d2065ca0 | -17.86172 | -46.32914 | 2025-07-25 04:23:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed98f67b-4f12-3aff-aa4a-4830916b5bdb | -13.09634 | -52.14674 | 2025-07-25 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17b352ec-115b-3e71-be55-7f7efac336d8 | -12.43545 | -45.37648 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d097a7c-06f9-3bc8-8c88-5b1e79e557cd | -13.71129 | -45.68936 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80658131-f0d4-3d9c-b037-76fa735068f6 | -14.9597 | -46.98296 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4fb73f4-ea93-3a42-9f35-5b399b6e739b | -12.04754 | -45.43046 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0a17879-79cf-3ebd-85d6-c7d018c92f14 | -11.67503 | -58.49371 | 2025-07-25 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a99413f8-e0c2-3cf2-8b21-38219bb00957 | -12.22972 | -44.62926 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9d607e0-78a3-3220-a462-a1f21ca09bb7 | -11.78646 | -47.32614 | 2025-07-25 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 951f6bda-c503-39ce-8a70-1a9d3a610049 | -12.46072 | -44.65363 | 2025-07-25 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79dcb1b5-e48d-3467-9c01-0972f8cf2722 | -12.43211 | -45.37595 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2a8840b-0eea-351c-b30a-c4e061d8ac7a | -13.64512 | -46.81979 | 2025-07-25 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe33cbfa-3078-3953-b860-e5a313432fed | -12.4641 | -44.65417 | 2025-07-25 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f92dfb48-8a48-3d6c-a380-551294cefe28 | -12.42823 | -45.37897 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdabe766-fd42-33e8-9783-8fc7a1b681b6 | -12.73016 | -46.30072 | 2025-07-25 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c10dd050-1150-37aa-8a7b-d247a95af07a | -12.69874 | -46.98178 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b81d2d63-5f83-3334-9c27-9843316bf806 | -14.21599 | -43.95485 | 2025-07-25 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8c2f9d6-fdd0-3f46-90cf-e5e03fbd9f71 | -12.04421 | -45.42993 | 2025-07-25 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d81ce79-3871-380a-aa9a-be4e69eb033b | -13.09781 | -52.13866 | 2025-07-25 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adbf7b16-9535-3765-b53d-6aa582d98bb0 | -13.70851 | -45.68525 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2342b1c-3bfd-3854-b4fe-0e5256ca8ecb | -13.69974 | -45.68418 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c2ed7c3-685c-354b-abfd-0e0bd2eff2c5 | -14.94916 | -46.9849 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a3d071e-9c46-37de-a603-122d658c29f0 | -12.69702 | -46.99247 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27589d43-6478-3353-b2e4-94212971648e | -12.42767 | -45.38253 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13114143-7507-3e70-a6ad-ba06fcca5e12 | -16.51322 | -50.85368 | 2025-07-25 04:23:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eee3baa3-e94a-38ed-b897-e62fbdaf9f70 | -12.6954 | -46.98125 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9665df92-d040-3ff6-8963-2d4979cfdd1c | -11.78308 | -47.32557 | 2025-07-25 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bee83df2-48f7-3895-ab60-ac48bf2c91d6 | -14.74274 | -46.29968 | 2025-07-25 04:23:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e319cc02-d262-3dc4-af39-363f80cfbc9f | -16.56428 | -49.05602 | 2025-07-25 04:23:00 | NPP-375D | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8821e8db-3c5b-34e9-bee4-85afd3b50a95 | -12.73392 | -46.97638 | 2025-07-25 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa9dfab-8c9c-3a79-8652-f1ec8a4bc286 | -12.43101 | -45.38306 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf043e06-df25-341f-8cd3-3ef462b8151e | -13.09708 | -52.14269 | 2025-07-25 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcb2c8c7-47f5-33f2-9f8f-bece653af8c2 | -12.89765 | -45.33257 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 369bdf77-951b-38f6-bc6d-ce21bea7ebd4 | -12.2331 | -44.6298 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e4b7c69-73bf-321f-9871-0c15d2995a78 | -11.94204 | -58.75975 | 2025-07-25 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f501335-c951-329f-a019-7d00c2c2620e | -14.93918 | -46.98326 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a656a43c-cd85-3eec-bf0a-93d132e9530c | -13.71517 | -45.68633 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8e9b358-3b17-3321-9445-672550b04e06 | -15.82509 | -45.77628 | 2025-07-25 04:23:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7dbf9bf-4706-3e57-92d9-0b1d608849ce | -11.31437 | -55.22472 | 2025-07-25 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1580fbe0-43fb-3663-b85d-d814375f7bf5 | -12.71023 | -47.79464 | 2025-07-25 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d544d35-0b09-39cf-b22b-c216bfd30fd5 | -16.69526 | -41.01254 | 2025-07-25 04:23:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
