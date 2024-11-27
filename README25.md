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
| e10d4ad3-929b-37f5-a982-a2e32fe85423 | -8.13582 | -44.47196 | 2024-11-27 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ee993eac-ca62-33a4-8095-5b292301cc31 | -3.10049 | -50.36045 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ab19658-d0c1-32a8-b45b-e88b375db4c1 | -3.57519 | -41.95671 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e6c9b125-6886-3ad2-99da-093340b9fe29 | -2.81306 | -46.83284 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fff02525-6436-3907-8bac-dae6caf071f8 | -5.66448 | -46.42205 | 2024-11-27 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| afb020f6-d74f-382f-8978-b980d392270d | -2.93147 | -48.63279 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0a08f65-b88c-32fe-8c1d-23437c90fa62 | -2.85021 | -46.83854 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 276f3060-ccd6-3bbd-9879-8ecff9dcdb42 | -2.81634 | -46.81314 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05b66124-5ecf-3e8a-be87-5cb6e10f05e4 | -4.16934 | -46.71912 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b93fcdc0-88ec-33cd-a44f-b566e6495dfa | -5.20563 | -40.63772 | 2024-11-27 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1154ae6-4d8b-3a3a-865d-ac240cbfd578 | -5.12748 | -39.85672 | 2024-11-27 03:55:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 04a9afc5-9bc8-3bf6-8db5-a40921fef8fd | -4.72849 | -46.57358 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69274ff8-4497-372c-a80e-3ac947083007 | -4.17142 | -48.45239 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d39d8b7f-f067-3cba-9ede-deea58ecfdca | -5.02964 | -43.60378 | 2024-11-27 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5198d72-ba4d-34fc-9461-e05be491a5f5 | -2.99606 | -45.46704 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6cddfce5-9c99-3448-803f-a0af33d81ac2 | -3.06459 | -49.20251 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7367bbf3-47b1-3350-b195-d3eb24c14381 | -1.42639 | -45.95761 | 2024-11-27 03:55:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 069a3ab7-e704-3002-a925-54d26302b056 | -2.68843 | -45.66211 | 2024-11-27 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 83ade403-accb-3ec7-89f4-34843cfe8dea | -3.1715 | -48.43225 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 9ee5feb3-5fbf-3e69-8f65-34ef833fb94a | -4.22161 | -47.2159 | 2024-11-27 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9e747e6-ef61-3e16-92df-3a8a8eccee9e | -5.03084 | -43.59634 | 2024-11-27 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ada3a4bf-4142-3cd4-935e-13e3dc6334df | -2.81837 | -46.83364 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e31f324-290c-3e94-a6b5-fb023b5423ac | -6.4685 | -35.25092 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40381c40-73f0-36f6-99f3-30a4b2d1c1e7 | -3.18251 | -48.43828 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9dcdc77e-8e7d-3c59-b070-b585025124e7 | -4.14798 | -43.79642 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a463ba4-9905-3401-9a75-7ca9ae384c8f | -5.80568 | -43.00859 | 2024-11-27 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2d2e04e-a1e6-375e-876b-c2b2a9e9987a | -3.17267 | -48.4315 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 064a9aa9-5587-3c0b-8c17-f22486fe8356 | -5.42611 | -37.60733 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 963121a2-ab4e-300a-8f4b-a5f92f41cc76 | -5.58442 | -43.15476 | 2024-11-27 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a438b77e-4888-381c-b145-44be26255453 | -3.51875 | -50.21752 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e63737a-0a3b-33ea-9b2f-e9a732348fee | -3.45179 | -50.29799 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7ccb0313-48cb-3a90-946b-c7e600b441cc | -6.19258 | -44.43007 | 2024-11-27 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdfdfd7e-9be1-3884-8919-6beb8c80a5f6 | -8.11323 | -38.96024 | 2024-11-27 03:55:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 222524c1-8d3d-3d50-ace3-b7fcd8aee697 | -2.78629 | -49.21164 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c2bccc4f-19f8-3d95-afd5-51f603a188b0 | -1.51091 | -47.27505 | 2024-11-27 03:55:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f40f4a1-fe4b-3c80-b5e4-c8f3a9b9cedd | -5.66105 | -46.42337 | 2024-11-27 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 312d1de1-71ab-38fb-a398-d68dad8f076c | -2.93898 | -49.12661 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4833b391-cfda-3253-994e-5841c5a3d1b0 | -2.83905 | -46.84024 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 78717ca2-ad25-3f67-8fcd-3314d1468534 | -3.04538 | -48.5166 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ab7d0761-2222-3e13-910e-973b94712f86 | -3.57929 | -41.95616 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cf4aea71-dbab-38f6-8fe4-881911ac5230 | -3.96685 | -48.08513 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 7e472a30-992a-3000-9ddc-18a6c72cc874 | -4.49653 | -46.60598 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13722fd2-3f12-3636-aa24-7cb72fb3baf5 | -4.91392 | -47.85932 | 2024-11-27 03:55:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a14fd954-8a18-3b5d-87a4-06aefeb239b2 | -3.93375 | -46.64758 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed586cd-764e-35dc-9e0b-bf1ffd76d96a | -2.99691 | -45.46177 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d3603adc-cdd3-3362-9c7c-1f618424057b | -8.86564 | -35.1537 | 2024-11-27 03:55:00 | NOAA-21 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c4cdc89-8e51-3b1c-b659-94b6913a999c | -4.31463 | -47.51746 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d352f4d-8da6-341f-8585-7916f15a2267 | -4.21961 | -50.89615 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 7e53e65e-e08f-36e9-804b-91673b116b6e | -4.14642 | -43.80769 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 707edb68-d632-37e6-8df3-ee8d3cbfb6be | -2.81526 | -46.81964 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e40e62f-ea4a-3922-9f02-b140218ba228 | -2.55453 | -46.40992 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17fa496a-5bee-3d55-8684-c548c564ed36 | -3.17007 | -48.44062 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fc847eef-7737-3712-af39-5b5e7ada2324 | -3.57591 | -41.95215 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 55b465d5-0488-336f-bc68-deeb96374888 | -3.88627 | -43.16109 | 2024-11-27 03:55:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bb2ea3c-e09b-3703-8a54-6035b95a7b5b | -7.05428 | -40.34597 | 2024-11-27 03:55:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd96825c-e620-3d66-9030-a6d880900575 | -1.72013 | -45.37447 | 2024-11-27 03:55:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ed85090-532e-343b-aea3-8076633bc1eb | -3.92792 | -45.84066 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a28f5f81-b930-3b25-90b9-8710f111626e | -4.14673 | -43.80426 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 1a314b3f-bcf7-346c-bb8d-3b99dc13f5db | -4.15711 | -43.82146 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a5f5199-8cf1-3f28-81eb-495fabb1568d | -1.52119 | -46.06982 | 2024-11-27 03:55:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64c2e15-3ba2-3be0-8467-41cd429463cd | -2.54629 | -45.39196 | 2024-11-27 03:55:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c983e58-de39-3724-9c0e-973b36f83c91 | -3.69746 | -50.22773 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a78554af-60e0-347b-aa43-31090c11f506 | -6.69491 | -43.0648 | 2024-11-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 065b7e3c-426e-3af5-a11f-5fc751178529 | -3.37706 | -50.10946 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5ccb2e0d-90aa-3f2f-af26-4f237e554780 | -3.82364 | -44.44203 | 2024-11-27 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0735b7cb-6557-3435-a3ca-44cd87aae7dd | -1.94145 | -46.59922 | 2024-11-27 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9e04aec-dd69-3fea-b9d0-c146a12116a4 | -5.80656 | -43.00599 | 2024-11-27 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6bf6b182-fded-3151-8f8f-6acb6a824abf | -2.85127 | -46.83209 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a75964ac-9c5e-3e52-8f09-e85501a16940 | -3.684 | -50.22889 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad5cf24-3703-3267-9c59-61c3b6fd4d2d | -5.83526 | -39.21342 | 2024-11-27 03:55:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 831f44c7-92e7-34ef-9b00-f6b0fcedaa7f | -5.14748 | -37.73822 | 2024-11-27 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb5158b0-4fda-3385-9676-64aeb08b6a13 | -4.32192 | -45.89109 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6950d53c-3ada-3ad0-851a-ceb0ff503775 | -4.13683 | -38.69974 | 2024-11-27 03:55:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba0dfd1d-7a07-32c4-9684-7d1c204cc161 | -4.94767 | -45.88175 | 2024-11-27 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dc34d45-663e-3c90-837a-43e5f2fe3926 | -4.4452 | -46.60078 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7525681f-3b09-34c4-aef7-1d2d980dd551 | -4.33089 | -45.889 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b58b5da-fe76-384a-a42d-8b0beba5c154 | -3.08914 | -41.14045 | 2024-11-27 03:55:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a6dcd91f-4ef3-3ddd-b9a1-d16e046e0de7 | -3.14825 | -48.53262 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23a28b32-d573-35c2-9bb4-c4a38debbeb5 | -4.81232 | -46.84222 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 012542a4-33c9-3c25-abb7-1e6ffdedca0c | -3.51781 | -50.22291 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb3450af-a95a-311d-8218-08da7241db90 | -3.42003 | -50.44397 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60897a4c-ec4b-3e72-9213-6980a8dfaec2 | -6.92994 | -37.13713 | 2024-11-27 03:55:00 | NOAA-21 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5b8d0db2-8606-3a5f-8ee4-146aec7876bf | -3.71055 | -47.6661 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f12dfe4c-af0c-3441-9629-ae21d35f5121 | -4.31405 | -47.52084 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2bf179bb-fdf7-3aba-a77e-ce408044ecfb | -6.18211 | -39.36496 | 2024-11-27 03:55:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee0b939e-79d9-3c1c-8407-6c6b48c1726d | -3.79982 | -45.22169 | 2024-11-27 03:55:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aad261f0-c73f-3ed9-a899-9d1808cace36 | -5.62049 | -43.94873 | 2024-11-27 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cede42b-21cc-3d91-befa-3a47039e4f2a | -2.56385 | -46.41781 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55ca3b94-f6e8-3917-a57f-16161152332b | -2.8396 | -46.83692 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0800259e-32c0-344f-8218-df569ddcca12 | -4.22454 | -50.88926 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 8eb25b9c-13ee-3578-b060-22b764c155a7 | -3.98505 | -48.06184 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36fc3cd1-3823-3c81-962c-9ea0670a5693 | -3.21817 | -50.91702 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 655def9b-444c-3e7c-b39e-ac72cab18f4e | -5.32051 | -43.07306 | 2024-11-27 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db5aaf8a-acac-39d6-b07a-4a2e5be6e86d | -6.02423 | -45.80413 | 2024-11-27 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97cbd45b-d1da-3f9c-842d-9b0043037957 | -5.37335 | -35.6158 | 2024-11-27 03:55:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec9549f0-22a0-3066-9412-38b1cdaf0976 | -3.38444 | -50.10524 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 689ec737-e075-349e-a04e-aed98c02683c | -2.8222 | -46.81063 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b8d4299-32ec-316d-9bf8-cd9e6ae8ade3 | -3.26627 | -44.54236 | 2024-11-27 03:55:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4918042f-e8fb-3274-8a52-c7ff45f0e2e0 | -3.98272 | -48.06064 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff416397-d74e-357b-bfc6-de038345ef49 | -3.24818 | -50.62292 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README26.md)
