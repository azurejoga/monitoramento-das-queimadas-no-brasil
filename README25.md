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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecffd0e8-1649-34f2-9d6d-8fdbd299048d | -4.93751 | -43.77921 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3268e646-884d-395c-8c43-50fdb092abdd | -1.75823 | -52.80855 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70a06395-25a9-3c44-8641-404341eba744 | -3.6031 | -45.593 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4a264aaa-23bb-361b-9884-c72da127bf09 | -4.46032 | -45.09359 | 2024-12-03 04:06:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f65e811-3a15-306e-b6ec-4d0268ae9014 | -3.54904 | -51.45739 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0153742-5483-36ec-9138-a3c7d0c6aa40 | -5.81916 | -46.47168 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 556243cf-490f-3a92-8b0c-531a23af737e | -1.94764 | -45.81809 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ab291ad-b10e-3542-9ae0-ee1b9a0e7e5a | -5.14892 | -43.23229 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e8bc7255-34d5-370e-b882-c5579f931f76 | -3.25937 | -53.62967 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7fcaec7-3a00-3685-8cd1-f6f6324b31db | -5.81328 | -46.48186 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a70284d4-973e-3dbf-880e-98f27481759b | -3.26251 | -45.37118 | 2024-12-03 04:06:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17f0328c-5237-3d57-8071-230dd2240cae | -2.66202 | -44.97972 | 2024-12-03 04:06:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c93b0834-2ab5-33d4-8a06-fb1a564a8ce9 | -3.55309 | -50.17545 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2894e9c4-fc00-3ef7-9f7b-3a66c9c017c0 | -2.66896 | -46.61732 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1344d5e3-17e1-3261-8262-a1c1f30f0129 | -2.68257 | -46.61529 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67d9aac4-4a26-34b0-81cf-3b2c280ebd01 | -2.88306 | -45.44663 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df3fc910-d1fb-3010-9652-184492389c31 | -3.75448 | -48.15245 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9136f1dd-3c95-3b2b-b244-d7b97c7e08cf | -1.08505 | -53.46298 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b1f07433-2df4-32ec-9e5c-5a44fd9bb2cf | -3.45216 | -50.30205 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a7eca51-12b2-3c85-8cad-f9c8eb084184 | -2.53986 | -45.38595 | 2024-12-03 04:06:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ec1383b-9f47-307d-bbe2-51710ff0eac3 | -4.09316 | -44.85279 | 2024-12-03 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55b9d7e7-3807-303b-842b-7446e09d2abc | -0.60024 | -51.68485 | 2024-12-03 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88d4b68f-bbe6-37a0-9792-6f5a3db63bf3 | -5.45618 | -43.58384 | 2024-12-03 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c35e4c62-be8f-3116-97a6-09d0a5cac68c | -3.46501 | -42.00655 | 2024-12-03 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3133ad38-0476-3eb7-b35b-21d192cdabfb | -5.27488 | -45.45242 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1bfbcef-f5f0-302d-97da-a246ed6330d6 | -2.66066 | -44.98222 | 2024-12-03 04:06:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a0bcde2-2902-319e-94a4-2f3fae385005 | -3.46678 | -42.00279 | 2024-12-03 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1536b9b-52eb-3bfc-bd92-d98fcff20907 | -2.33873 | -53.81357 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d731d6a4-df47-3be0-a63c-acfac74bee91 | -3.2815 | -51.06512 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98e74b83-e1a5-3a62-9866-eb33d630c3ce | -1.79998 | -46.65767 | 2024-12-03 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1ca3d42-d6fb-30eb-8f85-d7bf0e590387 | -3.18119 | -51.1672 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9fb3e4b-2179-3a53-aed2-9303f328dd17 | -3.53629 | -50.17576 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89e560d8-3b83-3d2d-bf4b-17f42a5c18f5 | -3.54415 | -50.19506 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 691a7592-755c-3e0a-9392-b02b09977564 | -3.85351 | -46.52333 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85f04664-c784-3e4f-a0f9-0f9725e5d610 | -3.66341 | -50.18816 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e176b695-917d-375d-8a9a-754f25078453 | -2.29053 | -46.37033 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cecce5a3-0725-3ccd-bcf4-a06544f72308 | -6.04003 | -44.0368 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b29c4e2-bbcf-3109-8634-5272c9f60c28 | -5.69525 | -46.5934 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c0017e1-2f87-3807-9b8d-9ec60993647d | -3.46621 | -42.00635 | 2024-12-03 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 90c5c341-3e70-3368-a850-a062d8742246 | -3.1974 | -46.36486 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42fa5824-615d-3b90-b523-0213b9a6b4ce | -3.34271 | -46.04982 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 81b9ae21-0a3f-3778-baae-09cee2cee633 | -3.12798 | -45.98993 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c2f7c2e-c7eb-3960-b128-ba948c0b7ba2 | -4.05883 | -44.87696 | 2024-12-03 04:06:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d7d0c61-bba3-3ef7-8e5b-09ed6b7c48f6 | -5.81389 | -46.47818 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b3057679-b101-3ca9-9d05-5dae0f43d1f4 | -1.7426 | -52.62934 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a23678dd-4946-3429-904d-cd758952b55e | -4.80249 | -45.42999 | 2024-12-03 04:06:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef7444da-34fd-3039-afc8-6bc59aa278dc | -4.1871 | -51.18805 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd0be611-7376-3016-a8a3-963eabb8d046 | -6.11684 | -43.96434 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| de5160cd-5cc8-379a-82aa-4c96d3665de3 | -3.99132 | -46.63331 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 522fbdd2-ce6f-30a5-947f-68b5771f8a1f | -0.84479 | -48.72056 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e659ac17-c78d-3c39-814f-3ce680f499fc | -4.80305 | -45.00101 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a34f131-9d1c-34e1-ae6f-486ed28b7fc6 | -3.84711 | -46.56199 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3d53861-6edc-32aa-8b0b-dce5ca946b3c | -5.37168 | -44.04193 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 317a4d1a-11de-3225-801f-91631e3ca17e | -2.66076 | -46.10588 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b97e0df4-0a7d-3afc-8dbf-0fbcea043e56 | -3.92607 | -52.39377 | 2024-12-03 04:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0a86348-618d-3dff-942f-6f4e7915cb0b | -5.80391 | -46.48785 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bb24904e-62c8-3d5d-b522-245571574780 | -2.35515 | -45.70678 | 2024-12-03 04:06:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b016964-6d60-3a80-81fc-ff448ebff455 | -3.09855 | -53.22683 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| effcf538-296f-3fb9-a2df-24117b4e6aae | -3.60625 | -45.59878 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f01f59fe-3d87-3c3e-afca-3d06d8ce29b0 | -5.99838 | -45.41535 | 2024-12-03 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fde9865-e914-3496-abc6-1ad47c8dac9c | -5.11282 | -43.21492 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| b6f70915-499c-3908-b7a6-4de81b82b0c2 | -2.66608 | -46.12603 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fc80656-4bcf-3b54-bbd9-0187e7099c6e | -5.14487 | -43.23549 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| eb08eddc-6fa8-31fc-91ad-378498fef643 | -5.65004 | -44.32996 | 2024-12-03 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4d9503-97db-3f9e-a3d5-60165f550a9e | -2.66136 | -46.10215 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb9c255f-b588-3985-8f0a-9d4009643437 | -3.28081 | -51.06911 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96234fcc-14ef-3f0c-bac9-fdfb0a2ba1d9 | -6.03841 | -42.52053 | 2024-12-03 04:06:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 35410ea7-9f2a-34b3-a544-fff18117b247 | -3.47335 | -47.68533 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bda5af9-7ea7-31d0-b44a-455290360f9f | -3.17906 | -54.33678 | 2024-12-03 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59baed91-acd4-38f9-90ab-9b712869e6a1 | -2.92787 | -49.43176 | 2024-12-03 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e0914f0-4a5d-3b75-8dd1-6cfa2aedafd3 | -3.90143 | -46.65513 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0582f79b-fbe3-3383-aaa0-217ed383a5a3 | -2.57204 | -46.41301 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 378b12fa-0165-396c-995a-96ca856c4b04 | -3.19676 | -46.36872 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7abbab40-00b0-32e9-a07e-fb178f05aff9 | -3.35336 | -44.36468 | 2024-12-03 04:06:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea14e3be-7282-345e-965f-becc16b1dcca | -6.02736 | -46.24862 | 2024-12-03 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2019c89d-7cc0-3c89-84b0-2aa8c839d9f0 | -2.8232 | -53.05809 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff18913-f26f-3846-baf7-6e81f20c727f | -5.95426 | -46.65335 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b467be5-2045-3ea4-8813-7a4ed21327d0 | -3.27862 | -50.32913 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69368b6c-30b3-3e6e-8fbc-1a1252d9c075 | -3.70214 | -43.43054 | 2024-12-03 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfb157e5-7b2c-30f1-a7c4-261cde7c7c2b | -5.81734 | -46.48258 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7826eda3-60f0-332c-96f1-ea9ca1f9ffab | -3.13209 | -45.99061 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f6a2924-28f6-390b-9817-13c2745269d4 | -1.08021 | -53.44937 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c3a1fecf-6a57-3bb5-9150-6b8185568fbe | -5.16719 | -44.80273 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5d4fbde-5290-3036-ae4c-495dff560ec8 | -6.02266 | -44.00971 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 069b3dc6-e6a8-3824-92b3-e7add539dc84 | -4.43566 | -45.34931 | 2024-12-03 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a5f7ebb-7c7c-3dfc-b101-789bbd5a9f1a | -5.82666 | -46.35212 | 2024-12-03 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56fc7004-9687-36b5-86b3-360d64458074 | -5.17145 | -43.73893 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbbb48a0-8f6a-3597-8b3d-2cdcf048f0cc | -2.16857 | -46.65227 | 2024-12-03 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d2ac26-8a4b-3488-b1f6-28be14d97f41 | -4.18202 | -51.18318 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a0b882-7626-3e17-8cae-64c9c5678c39 | -2.68323 | -46.61121 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 289c53e3-093a-35c8-a255-704196f0916b | -3.1666 | -40.17979 | 2024-12-03 04:06:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 73cb2457-afc1-34d9-9412-0e3d8007d9a5 | -6.17878 | -42.62304 | 2024-12-03 04:06:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ae542875-d7f1-3272-aa23-3ef06f5b17c3 | -3.28232 | -53.25309 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf91f83f-f200-33ee-9227-e67a19027d5a | -2.72953 | -45.20647 | 2024-12-03 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ea10dd8e-14d5-3556-a4f9-681c824946b6 | -4.09342 | -44.85449 | 2024-12-03 04:06:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d88919da-a0b1-37ab-9834-bad110d680f0 | -2.47949 | -46.56433 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6de2aad9-49b5-3388-82c0-b688dcc6da16 | -3.02638 | -53.87569 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 92a0fc2f-9636-37e4-bf49-5e85ad7466ec | -1.79628 | -46.65274 | 2024-12-03 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 123825c4-d088-38f2-a85c-6075fe5dcf5b | -2.68191 | -46.61937 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d689d537-c42a-351b-88a6-dd5a0ad3f4f1 | -3.26072 | -53.33892 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README26.md)
