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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 263f14a4-439b-3581-9677-e01743f8ca48 | -7.21581 | -60.61619 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d2fa54e8-ee6a-37ce-8905-275ae971fb28 | -8.57888 | -54.85273 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a975cd3f-2c7e-3603-82e1-b4b14d6984dc | -6.54247 | -56.26001 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73667745-bdc6-3f83-9173-5498ebf0e178 | -6.80806 | -59.5824 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ca46785-b483-3e65-87ce-ee0f89a11493 | -8.6021 | -54.74451 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44ac1b78-2c43-3843-8a9c-dc81d6bb5fd5 | -7.29568 | -60.68258 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 259c283e-0fa2-3ac4-86c0-daffa382066d | -6.6105 | -58.37944 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d6f6e5a-cb02-3021-82df-b7a7494676d0 | -6.35939 | -54.77105 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed0a48a5-de60-3731-93e1-6a98dd186702 | -8.6192 | -54.70379 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00ce6050-a9f9-3fdf-93b1-212585d061f7 | -8.69087 | -54.70073 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 651a2035-25ca-3004-9068-c9c003db5253 | -6.60661 | -58.38243 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a6a7d4a-8fc2-3978-bb84-3a6d3a45aa00 | -6.4376 | -54.97181 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af440dab-f4be-3445-b072-5c7ae22e78dd | -9.57476 | -49.2321 | 2026-08-25 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0980fe41-0a58-3946-ad7e-df7856e27a88 | -12.7211 | -48.38468 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4039a7ca-74c7-3292-9757-bf367afc4e56 | -9.16251 | -59.40212 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0748f975-3747-36b8-824a-32b4068a345c | -6.79284 | -59.63375 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6329e11-179a-38ad-bb05-f0281c33d621 | -6.63438 | -58.48752 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a56d495-9311-38d3-89aa-ace7cbd00ee4 | -9.69597 | -46.04161 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8be1e917-005d-3310-94c5-19b1be16b8ff | -6.43754 | -54.99576 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7947a0d5-c1a5-37b0-92d0-10a1ef4937b5 | -6.12405 | -57.81683 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7d6b2351-4e16-3084-b5db-7c60c15e8287 | -8.21424 | -54.97095 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a906ba3-e763-37d6-98ff-f963dd6b3ee3 | -7.54388 | -61.37057 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 049f6e8e-7fb4-3829-a010-00703b81e14d | -12.88097 | -48.48359 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 624d00c7-a4e1-3e0f-b44e-20679a7107cd | -6.84009 | -52.50603 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07c7586a-03cb-39fb-aec1-b4374674eb48 | -6.81195 | -59.60217 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c328b70-1cc6-377c-81ac-0532a526cbdb | -6.26074 | -55.41878 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5a758ce-7681-3eab-8385-8949b11e7f7b | -6.79164 | -59.64125 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47121abe-5cf1-3cc0-8d4b-b8abdaa080cf | -6.93901 | -52.79959 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7ddbe78-7d47-3f32-8c8b-a9fc46ed2eb6 | -10.05479 | -48.45301 | 2026-08-25 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53863bca-2406-3783-b9ab-25771ad255ac | -6.79941 | -59.59253 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9046eb83-ac72-3421-8524-5a9d1272472f | -10.30385 | -48.20069 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 446b6135-5707-39e0-a59b-a00cfb128867 | -6.99031 | -59.2514 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 43df828f-b1e3-3456-813e-8b61ff6bf2ef | -6.63549 | -58.50213 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 09a04330-794b-359d-aae8-636e214c58ed | -6.74858 | -59.64593 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbcc0c4b-21c1-397d-8ca9-13ca1a24e033 | -6.55103 | -58.52125 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08bf3338-126a-3069-936f-7f4bb2b8866c | -7.35601 | -55.66094 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d55fcf1f-6708-35ee-9c12-1ea0c3962e93 | -7.4926 | -55.35343 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70a979fe-5aef-3837-925b-6577420b468b | -8.5653 | -63.02851 | 2026-08-25 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c8fcc9b-e2f9-3930-bc17-0249b380210c | -6.63993 | -58.49561 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8a79cacc-ed1f-379c-a349-d11c4d599433 | -6.1279 | -57.81388 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5f7bfd23-f26c-31db-aabb-b7a691fee07d | -7.00222 | -59.24983 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| abd9bb01-24c2-3351-9f30-2be958a319b2 | -11.98514 | -45.91872 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9612be3f-917d-398f-b7d3-57dd26612794 | -10.86619 | -51.03966 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a741e6e-7ea7-3beb-81d0-608c05964363 | -6.78596 | -59.63265 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2576c612-d60c-377f-82c6-6097ef727781 | -9.39241 | -60.58966 | 2026-08-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77e74a14-dc37-3116-abda-ec18c358e6dc | -6.80509 | -59.68967 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 580e060e-f96b-3859-afb5-bb1a67ef2bae | -6.01201 | -57.66458 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 96b26cba-34ca-3753-8df4-63cc4e9f5c06 | -6.74514 | -59.64539 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f512557-00f0-3cc7-b600-ac369a98c8c0 | -8.08707 | -47.51633 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d466c497-5bd1-3d3e-b7c6-f258e2c26c7b | -6.81103 | -58.66042 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75a1f816-3908-3142-bedb-6bcb989e2963 | -12.8903 | -48.50417 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4606114c-9dea-33bd-826c-001c3f80f763 | -6.72137 | -59.44279 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13314986-10b7-3989-97ec-89522bab332f | -6.69206 | -58.72469 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f750c213-d1a6-34c4-a75e-c2b7f7399e29 | -8.58306 | -54.87442 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20f2c1ff-4b42-3c5c-a88e-53cb4b228b82 | -6.26132 | -55.415 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e238868-4e73-3e94-ac02-82c81537c5dc | -9.15579 | -59.40104 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c047b4-a650-36cd-ad91-bd27374ca763 | -6.6366 | -58.49508 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f64e2afa-f8cb-3611-9c96-81163a31fbf2 | -6.1529 | -57.69733 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 400c0916-147d-3908-939f-6f0429757d5b | -8.07923 | -47.53154 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d24c3e6-3fd5-31b7-bdf7-ad33d16295a0 | -6.13344 | -57.82184 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| debcead4-08a9-39f0-b748-41a6d48cd2ae | -6.01901 | -57.79316 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b2994d-8fc6-36f2-80d9-d751d018c870 | -10.77783 | -50.93075 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| dd3bf7c4-708e-3bec-9831-8b8666035850 | -6.80119 | -59.40591 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c5c5d0d-832e-31e0-863c-d977a4460e36 | -9.0364 | -60.44112 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12ebf0ae-3c4f-39fe-a339-a936c332d5ab | -6.6316 | -58.48348 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12b9ca93-5ec2-388f-a77f-0e2948c628be | -6.35112 | -54.778 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40308894-d347-3d9f-89bb-de467da00116 | -6.01532 | -57.66509 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 87c5c0bb-e3c2-34fe-a4cc-93a0d7d89533 | -6.13722 | -57.86493 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46b6ef87-0ac4-32e8-a0a9-52cdbb731b38 | -7.89464 | -46.38622 | 2026-08-25 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ab6c4ef-78e8-350d-bbfe-ec1b7e01910c | -6.97166 | -59.08493 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a5c151a-cd58-3535-bca7-63bdc19d4918 | -6.3606 | -54.76311 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a435073-2d2c-39c8-8149-79235e08d654 | -6.12873 | -57.72188 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 228238f1-72fa-3a7d-84a2-fb268b2a3faf | -8.09963 | -47.46459 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 389d90a0-59ca-366c-95e4-4912fcbf7095 | -6.86825 | -59.40488 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2ed1a49-ee0f-3fa2-8467-bab43b40b0e6 | -6.95817 | -59.0828 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88b0e231-1b0d-38d3-9684-8cc12f7d5010 | -8.09858 | -47.47271 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e4adf10-bed8-306e-a6be-fcec624615a7 | -9.19985 | -59.5784 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bcd6290-430f-34a1-a388-61978928249e | -6.86731 | -59.03528 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff350f4f-1605-38ff-9c39-18daccbdb02c | -7.54093 | -61.36554 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0bfba51f-cfd3-34cd-808d-738c998f6b43 | -11.16171 | -54.00679 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d0dc548-3440-3218-94bb-39ea53cb8bfa | -6.98807 | -59.24361 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 153d5291-696a-3827-97a4-0476f1c69771 | -6.7858 | -59.65573 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 692c340c-f61b-310e-a16b-0ce1a5db2909 | -6.60939 | -58.38646 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 210f330b-8e0e-3468-a92c-1bb5909325ab | -7.04682 | -56.60603 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caa46f8d-913a-3053-8c2e-851941c04121 | -6.54302 | -56.25643 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f2b14c-8a75-301e-b406-2a15fc219b7e | -5.94055 | -57.73133 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30b4c702-74bb-3b90-8378-f17e92aad4c8 | -8.17154 | -54.97013 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0946207-a061-32d2-a604-dda33137edff | -7.54831 | -61.36676 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2b69ea85-ec95-35ee-ab31-d381e1718804 | -6.99881 | -59.24155 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| f9d58b2c-5387-31db-9db8-cd45c174a14d | -6.61216 | -58.39048 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ea7a6ec-cf3f-34ba-a3b0-9142700db035 | -6.54192 | -56.26358 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e2a5da6-ef71-39f8-baa5-e3d7ef66c5d8 | -7.20446 | -60.61851 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 69fec79a-b466-34c2-8993-aa7939077000 | -9.65607 | -48.33127 | 2026-08-25 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbaef91b-b76c-3537-b284-07e8e212a161 | -6.14329 | -59.91167 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09f86e4f-ab49-3642-9873-027cda5fe143 | -10.32064 | -50.40327 | 2026-08-25 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7a53676-4aeb-31c9-b620-c53be16291af | -6.64215 | -58.48154 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2faf794-ca3a-3cf5-aa43-8a67d2d5e2f4 | -6.43879 | -54.96398 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b046d957-2ac3-3cc7-9f27-1bd5d81658d8 | -7.38352 | -55.18016 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 263014bf-6e1c-3742-beee-169338e80580 | -12.74169 | -46.47777 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4713632-da77-32fa-b065-6ee552278b4d | -6.52541 | -58.31575 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README50.md)
