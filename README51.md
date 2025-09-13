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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ece4302b-e476-3793-882d-6681db4bab4c | -13.26098 | -51.71228 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d487393d-3198-356a-9d4b-93739e3c2ea4 | -11.80236 | -50.55013 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| db87818e-cd5c-3f57-8da4-ffe8fa836dc0 | -10.34019 | -48.82921 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a90ed1fd-6716-3978-befa-ad3790b8d29e | -11.3333 | -50.79221 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a45c1787-669c-3719-b42e-102c3da67c22 | -12.93753 | -47.97373 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73e4e4bb-a3d9-3889-8921-0bf718b8aabf | -10.22543 | -48.63321 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7822bfd3-896b-316c-962a-3a50cbd13bbe | -10.70637 | -54.44387 | 2025-09-13 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c48ff028-8c8e-3ccb-ac40-a26705b5be8b | -13.23617 | -51.73229 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27b3bc5c-7871-313c-aceb-02d5181f6b59 | -12.8984 | -47.95171 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3ea2b80-3cb0-338c-b23d-dd6c721fc071 | -13.15552 | -47.15271 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a676bd5-0afc-3fe8-a604-4bf1c54ffa23 | -7.9432 | -46.9063 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ddd70df7-f020-3bfd-ae74-83a7d5faf241 | -14.17551 | -46.27611 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 991dbbcd-3b81-3d70-9b98-7d4dacc4ed36 | -9.48595 | -46.42145 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 454e163b-d56f-3a69-beef-01eb0e074826 | -10.5169 | -51.53548 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbd635d4-986d-37ef-8726-9a29d76ec8b2 | -10.3354 | -54.32609 | 2025-09-13 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b06bac74-bf73-3c3c-a3ab-4029e7f85911 | -11.85316 | -50.57114 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 1541a3ea-0f73-3f14-92d0-8a1c548d2d59 | -11.72985 | -46.61242 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01de6f14-0199-31f2-b8ee-8f1e9dda033a | -11.42865 | -45.62259 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| baf9d518-74f8-3f05-8026-cc0d4b45ce69 | -8.52038 | -45.14638 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c779be-b7a7-317d-b4c3-19fd4c1f05dd | -14.27572 | -45.10273 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 285f2b54-6813-3783-b07c-f3c6fd59d85e | -10.71644 | -48.6135 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eef2ad69-cd99-37b3-8265-6c481e203ace | -14.43124 | -46.39761 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4a99415-36b5-38de-8cb4-5136c1744250 | -14.16247 | -46.1641 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6801a87e-eb2b-30da-a10e-517ea2140a0f | -11.20609 | -48.41846 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c0e8c27-40db-314a-baa0-7dfb08a95f10 | -8.36397 | -47.57823 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1c1e2c5-e23b-3b5b-897a-d868565a6d4b | -11.1377 | -50.70574 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc89b9b5-bb86-3f90-ac48-c6cd8cfaa710 | -11.14329 | -45.31015 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0adb497-3fc6-336a-adf7-7397f919ac81 | -12.80073 | -47.99282 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 046df499-c6bb-3668-a9d8-f935f1177be7 | -11.07189 | -51.43695 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58e0d25c-0214-34a7-96ff-254705cb23ca | -8.48291 | -45.14885 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 313aa6a3-08bd-37b1-a816-9e6fa91b9d50 | -11.85414 | -50.56581 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 4839f300-87ea-3d67-a145-de7ea257fcd0 | -11.86819 | -46.75444 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 26748189-3fa1-34f7-bd32-7d0dbe74c271 | -14.20892 | -46.27375 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cef85918-b167-3673-b6d7-26001b7eb368 | -10.76404 | -50.51871 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3726580c-1427-3f0b-8851-3da6337d5cc1 | -14.2274 | -46.29449 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e04f606e-12f7-34b2-a133-4abb3bb6c2a9 | -11.78292 | -43.76125 | 2025-09-13 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 130e6514-4047-398f-b5aa-a7ed5bf599ae | -9.90001 | -51.89857 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc6c2919-9607-3c03-a1f1-8d8c832b4429 | -9.49582 | -50.88691 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e02a2d8-23b4-3433-9550-011f1d22d45e | -8.05069 | -44.50224 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78225f5d-44ef-3b93-967d-6a0d6ca2aade | -12.94458 | -48.00357 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5b232369-d73f-3561-aeaf-9a6430a4a14b | -9.494 | -55.9641 | 2025-09-13 04:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3b9d799c-8e12-3f31-b072-e23676ddda67 | -9.90617 | -51.89558 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de0c907e-4a07-327b-be4e-54a36b5a3ba2 | -13.73093 | -45.44784 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfd46fed-ab61-3da5-a757-81f4d16467b9 | -13.48032 | -48.4495 | 2025-09-13 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce28c1be-da35-3ef3-b05c-fcce3163e3ee | -15.05496 | -47.99385 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 601a037b-ec08-3556-9001-cfa4a8f1c607 | -12.83299 | -47.95028 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87225c4b-a909-309e-ac60-53773b370595 | -11.42209 | -50.75154 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc787e5e-51fe-3a0d-aac2-555b91b03b69 | -14.22525 | -46.28555 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5d8660f6-853e-31d3-9d47-608df49a0161 | -12.56316 | -46.93864 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2ffe156-c33c-35a3-af8b-e2716a800823 | -10.3374 | -48.81923 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76aa30ab-03ce-3de0-9933-85f9d5022c73 | -9.22802 | -51.22866 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e705fcc-e6d6-388e-8009-3f2df99deb76 | -11.44717 | -43.57043 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06e83ce3-614b-3420-bd80-6925efbb4300 | -11.93708 | -44.30011 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c67eba6-a063-3e0c-8150-284224fc361c | -14.69666 | -45.14687 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0f9d51b-347a-3859-aaf1-32d0a24cb336 | -11.14968 | -45.31538 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac1b0fb7-87eb-36cd-a5a4-767b9992105f | -11.67231 | -46.51494 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a900215-f5a0-39a4-b89d-5ab92dd06ea3 | -10.36866 | -45.43542 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8af6b612-f30f-3405-add9-a53b9e90fd7c | -10.77566 | -50.53812 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d34a9377-395d-3874-b283-97badaf18e6a | -11.99711 | -47.75612 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64a28aa6-4ac7-3d7b-8e22-a82d3123b57a | -9.74077 | -45.38763 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cf022df-892e-38a3-8ac3-9e333f16eda1 | -14.19332 | -46.27916 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56e3471e-bc35-3345-9951-5212e921dd72 | -13.14669 | -47.13651 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fce990f-5a8b-3bad-9344-a741dc549f75 | -11.0599 | -45.67923 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a389eca9-1437-3c98-9f63-3abc7300a5d8 | -11.79277 | -50.54825 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ecb97e4d-1895-3580-96b9-c2ec6d4303de | -8.08923 | -50.17677 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fb3ed57-c019-3a19-b191-289733e9da29 | -14.4442 | -47.32062 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87112d6e-a18f-3a4b-9d58-022aa9210b4f | -11.73812 | -44.20746 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16aef4f5-f2c7-3b3e-b460-203c9a609081 | -9.7033 | -47.53475 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56ca8972-1053-3aaf-8f2b-9dda121dccc8 | -12.91863 | -54.74986 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de6645a3-f963-3ea6-8695-2e2049d23fc1 | -9.81336 | -48.88982 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a6aa43-ded4-3464-80e2-2dadb3d9d947 | -15.32287 | -42.04958 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 043319b6-22dd-316d-9599-2153725a39f8 | -9.50708 | -54.67773 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7380512-eaab-3ed4-8092-20e19765dc48 | -11.73318 | -46.59321 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83ee54c4-8a0b-3216-89cc-1413772ac5bf | -11.44578 | -45.62985 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0277b383-d28c-35a4-bfda-8e17ec60fb18 | -14.20395 | -46.25989 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 614b1cd3-3212-3ac8-b4aa-108b4ad1a550 | -10.50993 | -51.54356 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85f0eb2e-b15c-3731-9b71-ceae54b0f2b1 | -14.27894 | -46.05398 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cdbd27b-de53-33c9-bf6f-65ad5e934ce2 | -14.75063 | -45.26487 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 879e2e62-63db-3f6c-b92d-02bac55bd279 | -14.18978 | -46.27847 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a694dd5b-3f84-3339-abc8-52894d288eca | -11.72615 | -46.61157 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4c86ede-a04c-3673-b586-ced1eaebdbc3 | -14.46366 | -47.34174 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e83ea86c-0f4c-366a-aa24-af07ddab0aab | -13.23558 | -51.73537 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9092f18-408f-3637-8ea4-5cb83b434b6c | -15.06575 | -48.01577 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e981e1-06d2-3e6e-a889-54acd40b3a9e | -8.94792 | -44.44719 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26335799-1cb9-3944-a789-50686b71ebae | -14.20114 | -46.27635 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d5af272-4264-35b2-8a0a-7511fc712e21 | -11.85796 | -50.57209 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 44e8bb29-17d3-3e25-8d80-e0631dd24641 | -11.41331 | -50.74402 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f40e73c-93a3-37cf-b23c-d90f0b3767eb | -11.48298 | -43.704 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92f7b906-1f75-3644-9309-3a8e5cd35c1f | -11.82337 | -50.57083 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d83daafc-a3f4-3e40-a7a9-dfce3a051ca5 | -13.92726 | -48.22633 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cdfde0eb-e53c-3fdc-b1a3-65e4a03e0ac3 | -11.05799 | -51.50959 | 2025-09-13 04:08:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 338febe1-4122-3a79-b604-10d799ba571f | -9.02633 | -47.0425 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1e0a2565-253f-3dac-b84d-753216617868 | -9.71518 | -47.53538 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9b0eb5b-4231-369f-bdf4-90607c1cd176 | -11.54686 | -50.56886 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ababfc6-f783-3fb5-b846-cabdced627bd | -7.86324 | -46.25101 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 50763a86-fddc-3b88-bad3-67bba8f84e53 | -10.50148 | -51.53087 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fc1aa59-4fde-3c09-8c01-1dd67c128092 | -14.21449 | -46.24109 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc993b8e-b795-38a8-bb84-cb06f36f5cbd | -10.5093 | -51.55032 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b18afbb8-a927-3fb4-820b-9896821a392c | -11.4322 | -45.62325 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05b43fe8-84b7-3c68-987b-f8ab82b3bc63 | -9.03276 | -47.04028 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README52.md)
