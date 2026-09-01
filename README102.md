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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f92f96b-c1cd-3b25-8f78-54630f38f86d | -3.1083 | -61.2191 | 2026-09-01 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e65d7095-3346-34ed-9f65-f1ac9bac4421 | -10.3388 | -49.9977 | 2026-09-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| dd1a96f7-7e18-31e0-afde-c352530e50dc | -7.3302 | -60.589 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2bd9a3a9-92c5-35ea-bd14-62a00d127ace | -10.1528 | -45.7665 | 2026-09-01 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 91545a61-3d84-3c16-975c-eeeffb01d4c1 | -11.2488 | -51.2435 | 2026-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 1d061dc3-a475-323e-9704-30f2112fe7df | -17.1345 | -46.8516 | 2026-09-01 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 0774118a-94ef-3c1f-b19a-c063c6e7a36f | -14.7108 | -53.599 | 2026-09-01 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| c2a66c36-da3a-3ed1-888a-fd55a52b2481 | -9.4421 | -67.4535 | 2026-09-01 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0cad77a4-c70f-31d4-bb1d-8213e611f850 | -11.7024 | -47.6352 | 2026-09-01 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2e667b20-3f2a-36cd-99d0-cd0a9c7f280e | -13.4767 | -51.4086 | 2026-09-01 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 2fdc4591-08b4-3655-9f48-314678a9be51 | -5.9635 | -57.6899 | 2026-09-01 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| afa692eb-ccec-34a6-95a1-721e6853f590 | -10.0101 | -46.4386 | 2026-09-01 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 89dbf6cb-016f-315c-bbbd-c6ae52a76b71 | -13.4519 | -57.039 | 2026-09-01 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 213.6 |
| c1f0ea16-18df-3c50-8e14-d2a74af252d0 | -14.6538 | -53.5433 | 2026-09-01 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 936a1601-7b63-3860-a7e9-e304fa432e40 | -10.746 | -50.6386 | 2026-09-01 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 800c1033-0bd7-369e-ab00-60130354669d | -6.6726 | -59.4445 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ecc00657-72a2-3034-b08e-70f2b28344b9 | -6.8035 | -59.1114 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 427b75a8-832e-3180-8cd8-c1ef499b1298 | -6.9553 | -55.6151 | 2026-09-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 28dc595d-fef0-3ea4-aef9-419a095b4aa0 | -7.4986 | -63.7448 | 2026-09-01 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| fda6f6ca-0f06-3d75-a682-ddb9c2426260 | -3.1265 | -61.2377 | 2026-09-01 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 182.3 |
| a450fcbe-efe5-325a-a86a-518c12420cfa | -7.3119 | -60.5706 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5c83dd8a-4f63-394c-b2a3-80b6509d4d28 | -7.5845 | -61.3423 | 2026-09-01 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0c32d087-7a25-322d-8de2-6ba43fdc0da0 | -13.0897 | -45.163 | 2026-09-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 83ad0371-17b2-3528-965a-11ee11e44604 | -5.5649 | -60.193 | 2026-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 22a4fab8-6a79-33a9-8a2c-3bc3c9134b1b | -7.5659 | -61.362 | 2026-09-01 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0b56c014-0684-3b52-9f48-ff0e1c7cdc3b | -4.181 | -63.1543 | 2026-09-01 14:40:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 236.2 |
| efed83f9-72ed-361f-875d-3518af566091 | -6.7699 | -55.6644 | 2026-09-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| aeb03c29-9587-3c77-9963-aed3920ac030 | -10.3388 | -49.9977 | 2026-09-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| aa06de73-ef08-3e7a-98a7-b94e89162b9e | -10.7856 | -50.5066 | 2026-09-01 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 531f49a7-49b5-34fc-a3c0-072643bc6338 | -13.471 | -57.0373 | 2026-09-01 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 633b0b89-7950-3b0c-b0f3-f81231afb396 | -3.6215 | -60.566 | 2026-09-01 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 0956aba3-7ebc-3dba-910e-a5003dc98515 | -3.2623 | -58.2367 | 2026-09-01 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 7d9ff803-75eb-3758-837b-971b37f91e81 | -15.6359 | -53.8586 | 2026-09-01 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4f7a893b-6803-3ffb-a1d3-f31921cd6f9d | -7.9425 | -44.2538 | 2026-09-01 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f97d8d14-0a57-388f-ad22-701628a36cee | -9.9741 | -46.308 | 2026-09-01 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f0ddad5d-800a-3a3f-87c5-4a2771785f31 | -11.7219 | -47.6104 | 2026-09-01 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c185e9b2-24d6-31a2-b804-a3ebdcdf7532 | -10.7274 | -50.6192 | 2026-09-01 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 583579b3-396d-382e-a3ce-103aab92e53a | -10.358 | -49.9742 | 2026-09-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ed5c82d1-406e-303a-9c93-1d5ef7c5afe5 | -5.9635 | -57.6899 | 2026-09-01 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8aa4e4a6-e3f7-34fd-9329-daebabe95613 | -7.9611 | -44.275 | 2026-09-01 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3be8189d-e2d4-3fa2-91ae-e4a7fba70e1e | -13.4519 | -57.039 | 2026-09-01 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 233.2 |
| dc18decf-fd3b-3fe6-bffb-62fcb2ab5c83 | -6.6542 | -59.426 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 6fe21766-937c-3c02-a8ce-a3afdf156327 | -10.8627 | -45.356 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 465.7 |
| 1af4d692-ef76-380c-ba97-248784d762da | -8.9242 | -63.2804 | 2026-09-01 14:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e7a95895-4c4a-3649-8e59-786d74d2e237 | -6.8035 | -59.1114 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ad4d1ad5-d030-325d-8817-3b1d52a76ab3 | -10.1531 | -45.7438 | 2026-09-01 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a0e0b503-0f10-3933-9584-9e07a513d62b | -7.2005 | -60.6897 | 2026-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 6329f621-090e-3231-98cd-af1df2c10952 | -7.5845 | -61.3423 | 2026-09-01 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b348acb2-b842-31ae-88e7-777fbd3dcbde | -11.2298 | -51.2456 | 2026-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 7ea40c4c-9791-3f3c-8a88-d083623f237e | -8.7817 | -46.4623 | 2026-09-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 205.8 |
| a297aad1-907a-3d43-88c3-78c994acc37d | -11.2478 | -45.1425 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 9080ce83-d6f0-3190-beee-388dfd119b77 | -8.7989 | -62.5095 | 2026-09-01 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 6d0d1459-4522-3e21-9ca8-28b153d8d7e3 | -16.1523 | -46.6749 | 2026-09-01 14:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 141.7 |
| b627b242-b352-31ab-8431-611ef1cd548a | -8.4235 | -44.9849 | 2026-09-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ee23a99e-2985-3129-93f5-1b40fdc42be8 | -11.2485 | -51.2647 | 2026-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 92d2058d-9028-35fb-a76c-53441ba091e5 | -7.571 | -60.4643 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 01c8180c-e2c9-316f-8a12-41b5f9f97de2 | -3.1266 | -61.2188 | 2026-09-01 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bc48b9c2-bdd7-34c1-90e2-4d8c7151019d | -17.1345 | -46.8516 | 2026-09-01 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 283.4 |
| 86213b23-89d7-3093-8596-ff407b3b5d01 | -10.3764 | -50.0152 | 2026-09-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 69a85ceb-5b4e-3ede-8f2a-f06f8ad3ae64 | -11.2642 | -45.3011 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 9ccb78af-1149-361c-b3a0-0407d04c575b | -7.5289 | -61.3825 | 2026-09-01 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 27ee012a-84e3-3869-b741-a703b7952264 | -7.1822 | -60.6713 | 2026-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 29268b54-f8e9-3013-8490-98d00a6a8d42 | -5.5648 | -60.2121 | 2026-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 20fec004-0e1e-3352-8491-8df6c7d6448c | -6.9553 | -55.6151 | 2026-09-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 354339c7-52eb-369b-a6f3-60f419db7c19 | -11.2673 | -45.1167 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 309.6 |
| ad31a2d4-5f99-3f21-b728-e34d0154e520 | -3.1265 | -61.2377 | 2026-09-01 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 89fa6073-b1c8-359f-b44d-e56bea577ce3 | -6.7885 | -55.6436 | 2026-09-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e63d88bc-22fc-3f6a-bcf3-4d101b1cbd89 | -10.3574 | -50.0171 | 2026-09-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 1a8adcd0-7964-38b5-b953-de9dbc4dfb9e | -7.9239 | -44.2327 | 2026-09-01 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| d7e340ac-9181-387b-b0bb-dc3653468115 | -7.7938 | -44.084 | 2026-09-01 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 72b10d8c-5941-3516-b39d-34ddf90fc627 | -7.3118 | -60.5897 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 76014fd8-8856-3447-b502-35cefe759848 | -11.0623 | -49.6829 | 2026-09-01 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 3c28cac4-4448-3c9f-94d1-0cf817a15592 | -10.7271 | -50.6405 | 2026-09-01 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 150.1 |
| df402388-f9f5-324a-8444-50090d1ad629 | -13.9477 | -54.3971 | 2026-09-01 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 238.7 |
| befa069d-1b63-37f2-a0c3-311c89a409e7 | -12.9589 | -45.944 | 2026-09-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| fb52d730-803b-3af2-8b20-a9f3e800b2c8 | -9.9931 | -46.3057 | 2026-09-01 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 627dd4fa-9a2f-3358-ad30-c99504474e0f | -7.0242 | -59.2374 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5c782160-783d-348c-874a-285660b4af9f | -15.2478 | -53.8666 | 2026-09-01 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 07d49804-2716-34ef-8087-55b3f9eb8079 | -11.112 | -51.5536 | 2026-09-01 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 199.7 |
| f1def28f-3aa5-372c-a714-91b98e88249f | -10.7407 | -54.0401 | 2026-09-01 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 45211305-db41-3fa8-88e0-653d23ec12a3 | -10.2212 | -50.3303 | 2026-09-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 403fdec8-6b45-3817-8a93-6392fae113db | -13.4516 | -57.0592 | 2026-09-01 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 1cb7f72a-e9ff-3d0d-a618-6a2ec3882bab | -11.2829 | -45.3214 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| e9dfc129-4c57-377c-9289-9b74e77c9b93 | -13.4707 | -57.0574 | 2026-09-01 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 37208b49-9437-3f19-aedc-05fbf06b2b7c | -7.3488 | -60.5691 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| e409339a-6953-3d27-9d41-e613114e4cfe | -6.6541 | -59.4452 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 524608a2-a489-3df1-a4fc-be506046fd08 | -3.79 | -59.3031 | 2026-09-01 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5ac2caf5-3915-3456-87d5-984b73888d3a | -7.3685 | -45.066 | 2026-09-01 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ffef91f3-4b93-3334-a993-acc26e191a30 | -9.4606 | -67.4531 | 2026-09-01 14:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 7a625807-8c7f-31d5-9c07-f11211ff032b | -11.2482 | -45.1194 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 76ab733b-5da8-3d11-83f6-732b6fc1abea | -10.8624 | -45.3789 | 2026-09-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 798c2bad-3f12-3da2-b85a-1f457902910e | -7.3119 | -60.5706 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7c1835fb-71c0-31b7-9540-734b37581f01 | -13.3374 | -51.7241 | 2026-09-01 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| da300f07-bda7-3222-8261-e79672736852 | -9.7217 | -48.1346 | 2026-09-01 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 0e931245-d873-332e-8931-72fa8a3d7ddb | -13.4325 | -57.061 | 2026-09-01 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| cfbf00de-2d44-3adc-92bf-09c137676658 | -17.1146 | -46.8556 | 2026-09-01 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 245.5 |
| de866f4d-b69f-3574-8a6e-f18f31eb794d | -10.1525 | -45.7892 | 2026-09-01 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 1e91ad3c-2345-39b5-971f-f01427e533b8 | -11.7216 | -47.6327 | 2026-09-01 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| b733b0b0-5e8e-37a3-b2a3-8de4da84a81a | -8.499 | -55.3051 | 2026-09-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| acba5cf9-bbb8-34fe-b7ab-b952f8a5301d | -7.2934 | -60.5713 | 2026-09-01 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README103.md)
