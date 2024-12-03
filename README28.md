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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dda65ab0-444c-3bc2-b7e8-a2a3c232ebb8 | -3.26971 | -46.92878 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 759c66ba-30b6-3239-9048-7cb485b95107 | -3.26563 | -45.3768 | 2024-12-03 04:06:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f038acc-41c9-3a15-9c57-f2915dee50ac | -3.84577 | -46.51788 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16fe4cc9-0271-3003-b577-1a7bd235fb9d | -2.16923 | -46.64807 | 2024-12-03 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a040b0c-f1cf-3834-8074-468aa5e3420b | -5.54294 | -43.89569 | 2024-12-03 04:06:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1b68b35-efa6-3bf9-9c8d-67efd03c8dfa | -4.34351 | -43.75108 | 2024-12-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f93ec1cf-e1db-387c-9815-97f6d62c6142 | -3.3334 | -46.05529 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71c55980-c0e8-3636-a15b-876fdb89bfac | -3.26613 | -53.63091 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 760d6068-6a17-309e-8dfe-8ee76caa64f8 | -6.12099 | -43.96103 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 593031d4-d98f-3d64-86d4-a04664c7a044 | -3.34157 | -46.05695 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a37d59d7-a954-3f7a-91ad-7d91c3ca03b3 | -5.79637 | -46.48287 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d594dd74-17b0-39cb-a416-8b8e3e5798ae | -3.34965 | -44.36409 | 2024-12-03 04:06:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 144e6b4c-5609-3d53-b9b0-406d064b9780 | -3.33281 | -46.05893 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2455f2be-da47-3977-8f69-47c4669afa93 | -3.53487 | -50.17585 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31a95441-0d56-344a-87f9-3c65d7b502a8 | -3.08576 | -40.05002 | 2024-12-03 04:06:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 39a15371-cfc1-30f4-9560-ed97f48d2494 | -3.39811 | -50.22156 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29012b1f-bd33-33ff-9a63-2cf9fddda0de | -3.48349 | -50.24948 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac8cf37d-c5a8-3ba2-b4f1-8fa916451c22 | -5.80982 | -46.47752 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b6d0a1fb-6163-3355-aaea-3b305c05b56a | -3.85226 | -46.53086 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63de634b-b3fa-3214-b024-79ee78b97fa3 | -1.88017 | -45.48491 | 2024-12-03 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3276f1c-4d37-3bba-abff-fcc945fc135b | -4.43856 | -45.35191 | 2024-12-03 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43f5cc7e-9a61-31b2-9c64-9e122d5be5a3 | -3.54714 | -51.45541 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8ea3792-a002-33f4-b32b-16edf832a131 | -1.89555 | -47.14142 | 2024-12-03 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1438abd3-e470-3f16-89ac-44d75880c45d | -4.53217 | -45.73546 | 2024-12-03 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05ead411-555d-3e41-9361-8adc8a1c5199 | -4.15976 | -48.59069 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 296e3afd-b4cc-384f-9661-5f858447caad | -4.0518 | -46.81553 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1482f0e-58ba-3416-a66b-00288bcf906d | -6.00294 | -45.41134 | 2024-12-03 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13d23f22-141e-36ea-b25c-f85cdaa109a4 | -2.51493 | -47.42036 | 2024-12-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be641708-a0f2-3aaf-8008-aa100a1668f3 | -3.4888 | -39.61572 | 2024-12-03 04:06:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 859250eb-9d85-3c2e-b1a0-8091dbf75786 | -4.08556 | -47.35165 | 2024-12-03 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74332855-258e-3d3d-ad1d-aa888a2283b4 | -3.85412 | -46.51961 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc45b0a0-29c6-338e-9ce7-4e37a10db346 | -2.97035 | -53.87659 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dc01376-7ae2-3d17-893c-7d9a53992693 | -0.59946 | -51.68981 | 2024-12-03 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5fe90ba-3b83-34d4-8bb8-f66bc1277cf4 | -1.94005 | -45.55248 | 2024-12-03 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42755a07-d43c-37e2-a343-81af7391d862 | -2.81774 | -53.06181 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b7167d9-eec8-32d4-860e-18fde851e0a5 | -3.16329 | -46.55338 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 356ffec4-3730-3197-8c1c-0f614d0589c0 | -4.47253 | -45.92286 | 2024-12-03 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2da95dc-a987-39d0-9c25-d8120f6a4833 | -5.14081 | -43.23868 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 468b88db-ea71-3390-928a-c4ab70ebec53 | -2.97726 | -53.87769 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f51aa6ea-7a6e-3652-9e20-aafa9709d3bd | -4.82752 | -43.43187 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 714648dd-420c-35c4-ba03-1911cc57e8d5 | -6.03448 | -42.52356 | 2024-12-03 04:06:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fbf2c229-3d63-3b66-b84d-364aa23c4908 | -3.37975 | -51.01464 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8b8b3f11-83b5-3325-baac-97ccfd63eb1b | -5.51031 | -44.50003 | 2024-12-03 04:06:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88256416-56bc-30e6-b396-089bf47d4bb4 | -3.18702 | -51.16813 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35b54359-ea15-351b-9475-8b57f3208ad2 | -2.81003 | -53.05585 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2db6ce37-4497-3251-908f-b827a0001e64 | -4.44012 | -45.367 | 2024-12-03 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77d5b86a-7a30-3a66-956a-e6074d833b75 | -3.1403 | -45.99192 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8301b258-1cfc-3281-a1e8-934ef294c86d | -3.26725 | -53.63062 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6a5a18a8-f81a-314f-a57d-a82f369e1c17 | -3.25319 | -53.66614 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d070b819-0284-36e9-88b9-55129fff2252 | -2.2031 | -53.77734 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8bc08773-6604-3eca-b935-3fe16d835243 | -5.80514 | -46.48048 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 3a23e1da-a461-35e9-8853-ec2f74182df5 | -2.58974 | -47.48078 | 2024-12-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e2bf511-f107-37fc-b892-eae470b1d693 | -3.8487 | -46.52626 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 916f9fe9-2987-313d-bb30-db9446e8ce96 | -6.02621 | -44.01016 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65f727c0-3e10-3f3e-bb05-bb6896eb9c13 | -3.17779 | -54.34404 | 2024-12-03 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a16afdee-9a40-3ced-8001-318310555289 | -3.544 | -50.18822 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e03020-41a3-3b6b-a577-4868df6de187 | -3.54286 | -50.19522 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 599e490c-33a9-363e-848e-0ea8092d781c | -5.14426 | -43.23925 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 93115905-cb63-339c-8f45-aaa05e544fa3 | -2.80456 | -53.05957 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01e8898f-5e8a-3fe4-99c3-f48207f8b0fe | -4.78777 | -45.42297 | 2024-12-03 04:06:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2091c645-bf0d-3b74-a7aa-58c81c00a107 | -4.08485 | -47.35599 | 2024-12-03 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd7f369e-b3d9-3719-ae9e-65ab5063be8a | -1.61603 | -45.92114 | 2024-12-03 04:06:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fad7e936-d308-3e9f-a50c-39a1f1ec500d | -4.47138 | -45.7184 | 2024-12-03 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0c50b33-0995-3420-893d-1575ea537d41 | -0.59707 | -51.68534 | 2024-12-03 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2e65bfa-69c5-3cec-999b-bbd10ce4df68 | -6.12451 | -43.96161 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0cd1741-8812-3709-8f41-0df1d9f5dfc3 | -5.74151 | -44.43208 | 2024-12-03 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70f06a04-270a-3780-97ef-e0f51e8aae0f | -2.58861 | -47.48232 | 2024-12-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8def03e-9e2b-3819-9ba9-c35f7dfd4708 | -2.72828 | -45.20797 | 2024-12-03 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9681c906-81f5-30ae-a821-0d5616b99916 | -3.68145 | -44.7016 | 2024-12-03 04:06:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbc4a43a-e1e9-35a3-a99f-5474ad1e1f01 | -3.92146 | -52.38317 | 2024-12-03 04:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10dad5d0-c1a3-32de-beeb-34bf6155eb58 | -1.07286 | -53.45417 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78fb5e5e-d12d-3b9c-9ace-7efe8b14bc7e | -4.03904 | -54.23341 | 2024-12-03 04:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfbdba52-182e-3873-87f2-1ba87402155b | -2.66256 | -46.09466 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08ca4be8-b691-3686-8ee9-08d5b5e062d3 | -3.25516 | -53.65961 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 43e2facf-3dfd-39a0-8814-10e33ef8f179 | -2.79796 | -53.05849 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b22bef74-2c77-3ee9-8bfa-d074883acac7 | -3.76851 | -44.05876 | 2024-12-03 04:06:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74999932-5cca-3f66-8e8f-f37c381de9d2 | -5.4568 | -43.58002 | 2024-12-03 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee44e6bc-0797-337f-8ffc-6af35ca8a94a | -4.43953 | -45.3499 | 2024-12-03 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e03b886-418f-3144-b32b-4402f3f33eef | -2.85236 | -45.38429 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fd1baf15-94cb-3020-928a-ac73ccce4873 | -3.825 | -46.59068 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c18ff374-df83-3c7a-96c1-74a0ccf28e58 | -4.16371 | -48.59671 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f3a1c8fb-7e6d-3e0f-a1f8-cb77cefb944e | -4.13392 | -45.82879 | 2024-12-03 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c85db082-aa12-322c-8c1f-661fe686b656 | -3.66822 | -50.19262 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32c95729-2d4b-31e2-9198-97a9368bf15e | -3.26051 | -53.62932 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 102dda92-f127-3fd0-b37b-dd7ddb575ee3 | -3.1315 | -45.99427 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ad0f01d-8d79-372e-92a6-71f9f27ad72a | -5.21989 | -44.90862 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61c28e74-af6b-3d6c-a692-94afdc3f7d0a | -4.04846 | -46.99881 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06f46751-3318-3c8f-b2ba-b4739054c8fb | -2.33522 | -46.1726 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d096ab62-850d-312a-8ddb-701810926166 | -5.30177 | -35.47427 | 2024-12-03 04:06:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af91cc06-d485-3ea8-98b0-c13843b29ae0 | -2.221 | -45.56153 | 2024-12-03 04:06:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 180e4fa9-072a-3cbb-b3c0-a352ca662cf4 | -5.53231 | -46.44998 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3003116-e2bd-3242-9a9e-57e4385af8b6 | -3.25997 | -53.66735 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e26bc47-6740-3be9-8a6d-b40f5f8b3f71 | -6.11748 | -43.96043 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a71aee9f-6fdd-310c-bc0b-4bdcfd9aef8f | -3.96773 | -47.24527 | 2024-12-03 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab74b0c6-b2f3-3360-a268-821f04f4f991 | -4.16589 | -48.61328 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1a35faf-a3c9-3ddd-ad41-240b71e6aef3 | -5.81856 | -46.47527 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f1c01162-eb84-328a-9ddf-d8f61ccbb582 | -2.84934 | -45.83302 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fc4da5b-bb27-36a3-a4e1-06db8bef2564 | -4.47533 | -45.71906 | 2024-12-03 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af5a3bac-2294-38a0-8c3f-7664d1fab47a | -3.46902 | -50.26878 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ea162b4-e213-3285-a14f-e7c9997c7888 | -4.40178 | -46.39742 | 2024-12-03 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
