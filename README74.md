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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35a65fe8-9ee5-3f6b-b574-e98d1099bf15 | -1.31933 | -55.88031 | 2024-11-09 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22eaa664-1d5e-3bc0-aafc-e494009dcafe | -3.02796 | -53.27164 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94223f12-d43c-3e9e-8f49-bad6ac01ec51 | -4.27098 | -49.66428 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 16caed40-b8d5-3085-be3b-6a82c9951ef6 | -1.42942 | -54.5379 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 928ec852-6c5b-3152-a2b7-40d2a9cd06be | -2.65223 | -49.88028 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 947e2089-2443-395c-9f0a-053b8bba5b75 | -2.61556 | -51.75193 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2802679-0b41-35c1-bc90-c9e589b89c17 | -2.82663 | -47.86404 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f283ca2-a65b-3ccc-a912-18f09cf88db2 | -3.95987 | -48.99945 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5684f21-3c4f-3ac9-999e-b2add7dd3129 | -2.87034 | -51.48119 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7eed07f-91be-3394-8905-0b6f771f5c7f | -3.52544 | -51.53019 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f1abd81-0293-3e0a-9270-6882ff5dd58b | -2.9369 | -51.05854 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8bdebae-6e8b-3441-b9ef-e68d4ccdedd5 | -3.10759 | -53.71127 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aa48675-d562-3026-b8d6-1e142e53e56c | -1.55808 | -52.27336 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7270a3bc-0ea2-31cb-abed-3d965b90d62d | -4.24206 | -47.8711 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5e1ab31-4ab2-383c-955d-20b9e6173721 | -3.044 | -53.27767 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef5ba3a-8f51-39d9-b1c3-7a4ef8fcbce2 | -4.82542 | -47.32212 | 2024-11-09 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af6857ac-646f-3d71-80fb-bb4867009885 | -2.576 | -50.53292 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86cef042-d904-369d-bb75-9066c0b23770 | -5.80796 | -44.48441 | 2024-11-09 04:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bac6bc08-9fab-3634-bc82-9b113787d54e | -2.28542 | -48.74161 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63b97b69-3d16-3e28-9791-d82984a2d9df | -3.24911 | -50.44927 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17429b96-72ef-35e8-8fa6-b4b68ee27d84 | -2.38751 | -46.7735 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f78cb96b-2203-3ee0-a1f3-e91ad67d6ed0 | -2.88054 | -51.30451 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31b203ad-3cb1-3a4c-b800-c5965a30c314 | -2.92131 | -51.66925 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3667d466-e11e-3a55-b6b8-ef2e37a8c754 | -2.97928 | -50.29719 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bbec6d0-ce99-3354-80a5-7fcf2279d63b | -2.20386 | -48.35915 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62382840-4ed1-3be6-9f34-4eac09a1d3f6 | -1.4161 | -54.77521 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16647d70-3550-3097-9ff1-63706f7c840b | -6.0512 | -47.26208 | 2024-11-09 04:55:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ede86858-31f0-30b6-9bac-f8195113c1b8 | -3.03328 | -50.3055 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e3a480b0-9edb-3e52-8d7d-c38894992138 | -2.67769 | -51.8205 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 35b4e49b-def3-3685-8783-aed792005884 | -2.20073 | -48.37961 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 427a8030-c78d-31ed-89c0-1a23c5af38da | -3.92218 | -50.24639 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0750b7a9-c2f6-3edb-ab28-c8b539330857 | -4.09592 | -48.51023 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e7f16a-0b84-3a75-96de-581c7dc5115d | -2.57512 | -53.97999 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c011cfb1-72b7-335e-bad0-84f7c07bea50 | -2.55687 | -54.03074 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbebd434-3f79-3ce8-b3ec-ab1feb4c87fd | -3.68753 | -50.19687 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d439a28-0750-3e6b-92c3-80a5c8b8e24f | -2.75491 | -54.03996 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a57b825-5dc0-355e-ae0b-6bdf5d329912 | -2.85394 | -49.2272 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8509df-5973-392f-9502-f784e6e22c54 | -3.97157 | -48.18079 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| a9153464-3495-3e63-9e7a-accd5bb10b2d | -2.91841 | -49.35729 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f296901c-d2ed-3ae2-b1de-980f0aabd49a | -2.31267 | -50.67155 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c2c6f1bc-7139-33c9-a404-7c6373418e7c | -3.02958 | -54.20461 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d550401-1576-3f3a-93a4-2a7f6dc563a8 | -1.77498 | -52.35001 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd02abf1-ec5a-3b4d-b0e2-20aed6a9ec72 | -2.23262 | -46.50367 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3ceca24-528e-315d-9c91-a3ae24fee4c4 | -2.09322 | -48.90197 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4780b0a3-26c3-3a74-ac83-04be46a852ca | -2.25196 | -50.53109 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2f50522-5689-3a77-997e-f8cbe284be7f | -2.10744 | -51.08985 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93017471-0f05-3c4f-85c4-65dfcd015e73 | -3.27687 | -53.67059 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2972ae6f-710e-3d25-b77d-c1aea15ccf1b | -4.10928 | -50.75258 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73da154a-f4b2-3e99-bd47-5ae516999858 | -2.55372 | -51.22935 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cebf6572-8f74-3c9f-8a5a-05c392974c98 | -2.13421 | -48.73643 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7351fdce-363f-3a55-8ecf-f7aed82518b3 | -3.25107 | -53.74798 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b225936b-c003-3206-bffd-e57c9e2d4242 | -0.65983 | -51.72223 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4519e60-ba94-3e10-9373-056de1818453 | -2.07286 | -52.26731 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8265c592-e7ed-3ea2-be89-e78c64a4806e | -4.41294 | -48.77352 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04e11d43-23ef-3e82-a2e8-b1910f28e9d7 | -2.62366 | -51.29293 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd2241e4-c838-3d4d-8a80-d6512558af26 | -2.88546 | -48.29297 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff1375e1-e79a-386c-ba51-2cc08ec8a583 | -3.53574 | -51.60001 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a11137b-0893-3fe1-81f2-af8560d4567d | -4.05475 | -46.93941 | 2024-11-09 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa7d3fea-50c6-35dc-a681-bf1aacd73224 | -3.05024 | -47.69489 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bd9ef58-b044-355b-bfbd-dc6f7e50915e | -2.19574 | -49.29438 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5fb34bb-2190-3e1f-8418-9a9609eeb811 | -3.09322 | -53.71611 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68b348f4-435f-398f-8ad6-a2d5dcf6c948 | -3.23369 | -51.19186 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26267332-2e3b-36a6-b745-6b73039f461f | -4.40486 | -46.28798 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7615dafb-21ca-3547-91cb-9e6365712388 | -2.15965 | -53.69418 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 471b7a72-2f42-396c-9efa-c1e1da0cbfe6 | -2.66521 | -51.67818 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85a06e7d-f381-348a-a6f9-c1e3b47d0d72 | -2.94727 | -54.08465 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 329c4e20-4f4a-3ecf-9cd9-3ec51aae5cd8 | -5.81325 | -44.12191 | 2024-11-09 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 79487deb-b96c-344e-989a-d49f5f7b736a | -3.28306 | -51.52043 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa2fa536-861f-364c-8b58-422027b1beed | -3.64074 | -50.18542 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0d2c07c-055c-3863-849a-c2b66b26083a | -3.42086 | -50.13739 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5055c673-84df-3f18-aa76-2c5b5d598992 | -1.89112 | -52.4534 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eefe5746-496c-3862-bb7c-6696757c8fc2 | -1.38425 | -52.21077 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ad80ca6-7286-32a6-a0cf-e0b5114d7337 | -3.64783 | -50.13882 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30602c18-06e4-3029-a55e-3bfde32ff71b | -3.63043 | -50.17955 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d94d86dd-f0ef-31e2-9a59-6429696cb81f | -3.33935 | -45.15945 | 2024-11-09 04:55:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 497ae947-4956-3485-892c-2cf7a4e5c518 | -2.8631 | -49.39319 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d3adc3e-181c-3b88-855a-f43afdccea2a | -2.72444 | -54.14618 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e27a3bf-f8b4-3b5f-be9b-d2ec1cb6f2ad | -2.5809 | -49.14198 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 72c2d604-82eb-37c7-9bf1-9beaebdbb9fc | -3.17276 | -51.30984 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15b7d7cd-e1f5-3e53-87e9-61c217bc275d | -3.66683 | -50.25849 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc25f028-9571-34f6-9810-7bcc14d4d7d8 | -2.41035 | -48.52515 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b3249246-a4cd-3ce6-a1db-731c455c5333 | -4.20308 | -46.69413 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d32b102c-84c7-3c2b-a2f2-99a330a5f628 | -2.98085 | -51.03793 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3fc2408-3f78-3c94-b6ef-7cc6fce189bb | -2.94763 | -53.93139 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0343a21c-dd50-39c6-a301-e43009a28d3a | -2.08894 | -46.52591 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05047a3e-2a7d-3ea3-b74d-ab3a5f58b205 | -1.40316 | -52.0025 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62a348a4-afa9-3406-b66b-17d8242fcf1e | -1.38419 | -52.18934 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee72c43d-023d-3d6f-971b-e19c729de4bd | -0.90948 | -52.56252 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e092d6e5-ca4d-321b-974c-58180a5a7b8d | -3.28296 | -53.67509 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf23e241-6e5a-3094-8adc-7ec6db36fc7a | -2.36591 | -46.85454 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9242bef0-f967-3268-b959-2ed8343ea1d9 | -4.12186 | -48.50333 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2a771eb-96c5-3b9d-99f0-703f2b126921 | -3.06181 | -48.06632 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a2d2b1b-d91a-394f-a01d-b4a9aac97edb | -2.82344 | -46.64551 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a674383-834b-3529-8fb2-e0bccc41e248 | -2.96804 | -53.86704 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9871c068-7707-3c2a-a5b4-066ed4975edd | -3.62052 | -54.79333 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 990c150e-a06f-3fe2-baf3-38a4b7411c95 | -2.62251 | -51.30035 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e55d131-c9f8-3cad-bb6a-89546d305cad | -4.24767 | -47.56771 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcf4fc6f-8c62-3d9b-b837-3196f231fd54 | -3.58494 | -50.23499 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1226377f-1ad5-360e-b5e7-4510e43e18db | -4.74973 | -48.42615 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cacd45ff-5884-3d8f-8457-760ec5baa2eb | -1.31729 | -55.88119 | 2024-11-09 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README75.md)
