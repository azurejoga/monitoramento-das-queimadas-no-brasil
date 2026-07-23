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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94defee1-65c4-3362-ad06-b16200a8347a | -9.52383 | -47.13275 | 2026-07-23 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec6171d2-d6d2-3cc3-85e2-e4d5e2b017cd | -10.68585 | -46.60357 | 2026-07-23 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf01fde7-1559-3206-a4c9-29a273dae626 | -11.96111 | -50.35895 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 587e34c3-71d3-36d0-8a75-1f7d88b5ae12 | -11.96828 | -50.36932 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3d472b48-63c6-3a58-9809-b5cca00dd553 | -11.9416 | -50.3725 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 77f1e1ba-96e4-3ec8-8ad9-0c0a6e3f98f6 | -12.13898 | -48.26019 | 2026-07-23 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93c467ed-a024-353a-a3e5-60ff14004fa9 | -11.96459 | -50.36369 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6e4a7013-6cfb-3ce0-af2f-f07053472a60 | -12.32507 | -46.73828 | 2026-07-23 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2a04835-b72c-371d-9df4-98b8b570cf91 | -8.06926 | -48.01936 | 2026-07-23 04:25:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cbcd071-4513-386f-a3de-8ced1857e430 | -12.40567 | -50.39422 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 815d4ea8-0db6-30cb-bd22-ca78310cfe29 | -12.66749 | -48.21545 | 2026-07-23 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bd71c94-2d39-3b96-8dae-28bcf30f26aa | -11.78323 | -50.38532 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8ca6645-b6c0-3c9d-9843-d3aa2745a2a1 | -7.88419 | -46.90421 | 2026-07-23 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d20d69de-5a0b-366d-aa5a-d18a5f0204b8 | -8.83676 | -47.08165 | 2026-07-23 04:25:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d92e6143-a702-3ec2-a655-e6c96de92595 | -8.68122 | -47.83345 | 2026-07-23 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d8781e1-ed3b-3f0c-b106-e3e77ab44efe | -11.69508 | -50.3691 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d1cb487-de63-3373-9d38-275343b04c75 | -11.68804 | -50.35955 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f5ffdcc-e7f4-3f83-bd67-5b1cfa8ac895 | -7.72971 | -44.55864 | 2026-07-23 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f8bdc88-3107-35c5-8fa2-ed4d67de73e4 | -12.84518 | -44.38075 | 2026-07-23 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da580b09-3615-3723-ae81-464f359e3197 | -11.66834 | -50.34763 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bfe834ab-4f22-30be-be5f-1401daac9271 | -13.37013 | -54.30318 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b85d51c6-6722-3244-afba-12c429ace293 | -11.99357 | -45.80096 | 2026-07-23 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83e4b3d8-2c5b-31ae-9a42-bec16a6792c1 | -11.70354 | -50.37067 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d54acb9-5610-3134-8285-0ae31e2a5845 | -11.67887 | -50.36195 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f22db721-48f4-3cdf-8501-2e4c9d5ae82a | -11.96124 | -50.35982 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86f3dfb0-0bf2-30f8-ad37-d1bde7da6d9c | -12.39753 | -50.38962 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08313a58-518e-380f-a980-a2f2a68284ea | -10.95752 | -49.81133 | 2026-07-23 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0ebb02c-dce5-3a07-bcdf-7fce15dbd295 | -12.44678 | -49.58922 | 2026-07-23 04:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f362083-7b54-3842-be99-5de0a00e5f54 | -11.57516 | -48.40422 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 353e85e4-2767-359e-93b3-961b1c4a6127 | -11.68453 | -50.35477 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af86dd37-5576-31d7-aec7-b095de0901a3 | -11.95703 | -50.35903 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 625b7043-4f86-33c3-9094-6917e8f8dbbb | -11.7907 | -47.1034 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b8866576-f955-3f23-8a27-d42049800060 | -11.79003 | -47.10739 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3052a12a-7734-300c-8521-2157f3cd1202 | -11.68238 | -50.36673 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e056248b-0808-306e-97e2-387a58fee279 | -13.32413 | -54.31163 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8c1d430-b49e-3e57-af85-814adf4bb405 | -13.36479 | -54.30215 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd7e6eec-f2d5-38c9-a139-02b04c22239b | -7.7303 | -47.25012 | 2026-07-23 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ad8c297-15c2-35d0-9b29-16013f35a15c | -10.63059 | -47.48389 | 2026-07-23 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3ad7592-4621-3e21-b13e-8f8f02e5a19c | -11.91346 | -43.8456 | 2026-07-23 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd87ce8d-5d8b-37f1-8fdb-6fe2747ea34d | -11.67959 | -50.35796 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c26c53ed-b08e-3fb3-b6c5-b1734fe6aff0 | -11.58347 | -48.40095 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0d129c5-15de-3372-a098-ed6c5886dc7d | -11.81351 | -47.33522 | 2026-07-23 04:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0279d5af-524a-3b55-a9a5-30b0f9b5bd1e | -11.69156 | -50.36432 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4153a912-5301-3d4b-977a-c7deef700689 | -11.6732 | -50.36914 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e383f65-4708-39dc-befa-9d135b2a8c0e | -12.03477 | -50.3605 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5b5f444-8c26-3185-be45-ed0ef1532231 | -7.88853 | -46.90055 | 2026-07-23 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fb2ee8a-6176-389e-8ca1-169059d29234 | -10.6865 | -46.59969 | 2026-07-23 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7186a3ed-911c-3b94-964e-3b77d8f1beb8 | -12.66209 | -48.21704 | 2026-07-23 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4506ef7d-e2a2-3458-96e3-31599d6dcb69 | -12.32099 | -46.7415 | 2026-07-23 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b73691b-4ce6-3c0e-9736-21cb7ccbff7d | -11.66339 | -50.35081 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| bae765a5-ea46-30d5-a02b-65fc9e8a8fea | -11.77477 | -50.38375 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 051925c7-5741-3344-8fc3-a6aeb5eec2d6 | -12.25317 | -43.57274 | 2026-07-23 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9f2df61-e8e3-3424-8dd2-6e89814974a9 | -11.68661 | -50.36752 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 029cd2a9-6097-3a34-a897-4e07a7fdfffb | -11.83158 | -44.75126 | 2026-07-23 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b65daa37-18ce-3a35-9089-6bbf784d095d | -10.95675 | -43.64985 | 2026-07-23 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bbf857f5-0e54-319c-ab03-58b54b1e4425 | -12.84795 | -44.38483 | 2026-07-23 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cff1886-1c40-3089-a380-0eef76e29b16 | -12.84797 | -44.36304 | 2026-07-23 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c02cc717-c591-3c05-bdcb-94582f9e175d | -11.88844 | -43.83063 | 2026-07-23 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 669235e6-9468-3edb-8c68-a1fc6d3b4e00 | -11.58427 | -48.39634 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85f14e5d-8430-318e-b0f8-c9b2d0bacade | -12.03548 | -50.35655 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17093852-08f9-37ce-9891-a5127d7ebfbf | -6.41377 | -51.23565 | 2026-07-23 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 097f4f5d-f888-3ba7-b606-2c3a6e92e8ec | -11.79773 | -47.10461 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8922a02-338c-3529-ba67-aea2e9438f22 | -11.93668 | -50.37568 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5713cd3-a283-3abf-9ca6-4c30f91ab63a | -11.94581 | -50.37329 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ef57ee0-5ac3-3c9d-9e8b-4faa714bc63d | -11.78719 | -47.10279 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c6dd6ab-1655-3b77-8659-cf80f059e745 | -13.43754 | -43.85218 | 2026-07-23 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79a69863-c2d7-3aaa-b489-108090cd7c32 | -13.37611 | -54.30089 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e28a5c0e-8f83-304d-8c6c-20981e3ce1aa | -13.3188 | -54.31055 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea88d384-cccb-3ff5-a991-d9bc59d51c31 | -11.91068 | -43.84151 | 2026-07-23 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3c4e6cf-adcf-33d6-ab61-54aee30ba95d | -12.52357 | -48.24538 | 2026-07-23 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f6c6ad0-dcc4-3bcb-b8cd-83a5c8f69368 | -11.95842 | -50.35112 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ee2cbe9-1357-302a-966c-2b79a3ecc06b | -11.6803 | -50.35398 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec66f064-ca39-3ff6-9160-0a81776cb60f | -11.69227 | -50.36033 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb3a287a-0566-3520-9f61-30202d386bf4 | -12.45076 | -49.58993 | 2026-07-23 04:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77a4cfe7-f4d7-3db4-ba05-b9d0ad1c0644 | -8.83746 | -47.07741 | 2026-07-23 04:25:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df7be269-04ac-367c-8b54-d2309f6bac7c | -11.69436 | -50.37309 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5694ee78-b630-3443-ad1c-284362b8ece7 | -11.95073 | -50.37012 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa6352c8-ffd1-3fc5-86da-4d135a2ca680 | -11.54357 | -48.27341 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1402a365-0af8-3eba-bf16-1f37834d93f5 | -11.68382 | -50.35875 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7c4726d-d044-35bc-901f-a41411a5f08f | -11.57891 | -48.40488 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1340626c-cfb8-3fe6-8659-80a92a7ac680 | -11.39764 | -47.48155 | 2026-07-23 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f55cf531-d9f2-32ee-9d06-59ed2fa73120 | -15.32247 | -43.72863 | 2026-07-23 04:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a5b2e16d-0b8a-3901-a694-8689645a1c24 | -11.94089 | -50.37647 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60a83af4-5dda-31e0-bb9c-ef6a01a167d3 | -12.8485 | -44.38129 | 2026-07-23 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18ca407d-dba0-3d42-8046-01dc4b3fd989 | -12.52282 | -48.24977 | 2026-07-23 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 988f0172-d49e-3d26-8c3d-e070c9db8854 | -12.39821 | -50.3857 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbb87e1e-9d7a-3855-960f-da4b710458cc | -11.69931 | -50.36989 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 577e49d9-6985-3b82-a8f5-ef2fa9ca7e47 | -11.70706 | -50.37545 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1fef594-5684-3b4b-a945-fde37616e21d | -11.78436 | -47.09818 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3fa45b4-38b8-397f-b8ed-cace191736bc | -7.82746 | -47.11121 | 2026-07-23 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d098d85a-9ab0-3270-8f71-195557adee5d | -11.779 | -50.38453 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e01ee54-53b3-3b48-9f07-acdf23e82a9e | -13.32545 | -54.30499 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e13ff163-ebc6-3d80-979b-17eb796e8a99 | -11.79138 | -47.09941 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 33a349b3-85e4-3417-92f0-6420558bf405 | -8.80456 | -49.37678 | 2026-07-23 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09ab7958-67d1-3991-ac51-7739214a0b24 | -7.83114 | -47.11185 | 2026-07-23 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff80c77e-3649-3012-ac06-b94d1902744b | -11.8287 | -44.75091 | 2026-07-23 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d67a5a1-981f-3d7c-ae56-9790a552920b | -9.55733 | -40.34071 | 2026-07-23 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| df6995b5-1898-3516-a8d2-548b465f2fdd | -11.80087 | -50.38449 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78fe75ab-2dd7-3ad4-9bfc-fe8c7dab975b | -11.96387 | -50.36763 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 15e7f46e-c4f0-3785-945c-d011aec08286 | -9.52093 | -47.12795 | 2026-07-23 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README12.md)
