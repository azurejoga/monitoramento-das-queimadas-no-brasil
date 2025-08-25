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
| 36ff370c-ef96-3fc8-a8ec-75e6ac8813a9 | -14.73411 | -55.92595 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c33637c-77f7-32ef-b4b2-e0c30819bd06 | -13.00349 | -56.88971 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4887307-1eed-35d1-81be-52dd71168a49 | -15.03554 | -48.51128 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa4c656c-9ff3-30bb-b746-4a89a484db3e | -14.65066 | -56.57109 | 2025-08-25 05:06:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ab97c51-2a1c-302e-a08d-a23b495c088c | -13.4363 | -46.92332 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb45c3b-d4a9-3604-b3de-177bb410e8f9 | -13.50871 | -46.90971 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3eecf4d-c017-3d5f-beac-a5cff2f40fe6 | -13.43001 | -47.02933 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f29f98ab-55c1-329c-8579-5c84b8f57790 | -15.1039 | -48.69613 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16d5be97-b8a5-394c-8ece-8db1b57a7d74 | -17.58175 | -48.73429 | 2025-08-25 05:06:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3c7c3b0-36f0-3959-9bee-a6eef7516c00 | -14.72274 | -55.93189 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 735ee2db-ac94-3e00-90a9-a25042f8b931 | -13.14899 | -53.74035 | 2025-08-25 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab24d643-9a2c-3d56-981c-801df55fadb6 | -14.71933 | -55.93135 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72efe26d-757f-30b7-bfbd-61abf25812c3 | -15.62417 | -52.70164 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49dc1d5c-ce2e-383d-809a-4b669b6a8972 | -13.50783 | -46.91755 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4af62a54-ecba-39fd-800f-ed5db39bfa69 | -14.10318 | -53.9955 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be2707fe-802e-3caa-854f-d29bb0e4dc25 | -12.43236 | -56.50358 | 2025-08-25 05:06:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2900e8de-4a9d-303f-ae6d-cdd7fbe1fe43 | -12.9963 | -56.89217 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f9a8e6b-7d19-3d63-8fd7-9a96f57fbd0b | -18.38774 | -46.8359 | 2025-08-25 05:06:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e89d9b4-8797-33af-a338-0c44def87425 | -15.07847 | -48.547 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4db08785-c4a8-3e94-af68-06211dc2eccd | -15.64554 | -52.72767 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5824777-1409-3556-b5a4-11b3de8759c2 | -14.64566 | -56.58133 | 2025-08-25 05:06:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abe1f26f-979f-328f-bfbd-73404cd2b4c3 | -14.27223 | -58.61478 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d765b001-838c-3fea-a0c2-244714fa726e | -14.38862 | -51.9557 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd66f55c-b783-33b4-8b8b-9aaef66fd125 | -12.99685 | -56.88863 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2d9b091-420c-34c2-921f-1df7c45e5e93 | -19.1781 | -44.52369 | 2025-08-25 05:06:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc1fbc3b-4c45-30a5-aafb-a5b5e1bc942a | -17.58039 | -48.48223 | 2025-08-25 05:06:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea072d3b-ed4c-370e-b40f-339ebb2c2864 | -18.34233 | -46.02079 | 2025-08-25 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81575044-d110-3194-acfb-03332388eb2f | -14.64506 | -56.56272 | 2025-08-25 05:06:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| feec715d-0c3c-3ed4-9c0c-f8692a2f12c7 | -14.74093 | -55.92707 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b1d535c-a19e-3d24-b4f4-f70b99a5305f | -13.43669 | -47.02205 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c5c8294-271e-36a7-af91-cfbd5fec7e27 | -15.14153 | -59.59458 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6763aac6-6913-3882-a77c-df533eb2c3f3 | -15.0781 | -48.55014 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98f5d711-6cfc-3f78-a470-2e3897e38a29 | -13.50243 | -46.91319 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afc5b2ff-4ab3-3052-aeff-34e856f8285f | -13.38794 | -51.80577 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ce4a1c4-f8f5-35c7-8eca-8bf10c27de3d | -14.42921 | -56.46475 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a5207a4-fe41-32bb-aaa4-2188e2707ffa | -13.44247 | -47.02262 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d035f353-ace1-30fa-957f-38f08e7129a5 | -14.29261 | -58.6109 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfcad2bd-285b-333f-8844-fac163482e72 | -13.48219 | -46.88295 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28f867d5-1b20-321b-a1ff-2a9f3903c5a6 | -15.63743 | -52.72642 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30279421-c081-3e57-b898-ed6a51f56086 | -13.44685 | -46.88255 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae58bd3b-c7d6-37f2-a2bf-6d2672235e9c | -15.18044 | -48.19973 | 2025-08-25 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcd9bad1-f8fd-37eb-bff7-692edb09a8d1 | -15.0382 | -48.16508 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 697b1aa0-2f9c-30ce-9e2d-0b42dd5378bd | -12.99906 | -56.89626 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e2f0343-fcb6-3a7d-9e59-98c2055bed18 | -14.47739 | -52.06689 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35aa8c53-b5e1-3a83-a6fc-8d359a407c55 | -15.03954 | -48.50917 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 643180cc-c1d1-3793-9c28-da304cf1c335 | -13.28506 | -47.50985 | 2025-08-25 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c79c846-fe39-32c3-bcae-c76046abc064 | -14.38823 | -51.95218 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b855708c-b606-3f05-bca9-ddea53a780af | -14.30029 | -60.37266 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c514f161-07e6-3de9-970a-5900be8509ac | -13.44002 | -46.89071 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83591a4d-1463-3157-9450-444bac3ffa6e | -13.50198 | -46.91728 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34dcb12b-de2a-3500-9d0d-a33799cd4b83 | -12.49796 | -53.82976 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b52e8477-0238-3ae8-b70d-dd240d43d236 | -14.81514 | -47.91656 | 2025-08-25 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57eead1c-2845-34fa-83b3-ef21cf657610 | -14.43537 | -56.46946 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67084f2c-2431-3cac-9515-1de27e72bcd7 | -14.43481 | -56.47311 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c10c6dd0-513d-34c6-abc5-dc8bd95dc1de | -13.42688 | -46.90305 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a5e34ab-e4e2-3a75-94e6-3fb9f7c9c9cb | -13.00293 | -56.89325 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d40f586-5337-3dab-b2d0-84f9e0574478 | -13.42962 | -47.03271 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5392812b-d4c8-3544-bf9e-7802c4143462 | -14.51148 | -51.93546 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1177f54-fa77-3b21-8475-062260a8c485 | -13.44639 | -46.8865 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2f11842-0964-308c-b339-ce906e4e7daf | -14.10381 | -53.99101 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eeb66df1-ccb1-34b5-a364-53b49294c529 | -14.24773 | -58.61803 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58371f88-4d64-3a91-af93-72d2ac0d510d | -14.25498 | -58.61555 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 161c257c-6963-3121-a45d-e0c23acf95fe | -19.17865 | -44.51685 | 2025-08-25 05:06:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6669f226-24e4-3ac7-8616-a6e4fdeadfa4 | -14.25106 | -58.6186 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f33f291-6339-3863-9d25-13aa7a968271 | -14.71592 | -55.93081 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 032b4d90-1cfd-3873-a2f4-807342f4e7d0 | -14.38544 | -51.94721 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 920ee789-704b-360a-9c11-fe9779d6a4f5 | -13.50939 | -46.9024 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1e7d0d2-3aec-3b5e-8950-83fcaadf012b | -12.59267 | -60.36357 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8d1264b-4323-3fa8-9788-72c777012774 | -14.76199 | -55.92651 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6458d943-c3da-3f9c-918d-6818bddc0af5 | -14.24381 | -58.62107 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a996609c-c0ab-3a1d-b361-9ce3e382a7a1 | -15.03862 | -48.16148 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 238aab1d-45e0-3830-9758-dcad55876421 | -14.2761 | -51.96043 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d609832-1d3d-3364-8007-c220e9e7fe13 | -13.50959 | -46.90176 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28c881f7-1f4c-38ef-94af-dddb777503d2 | -13.61999 | -48.18031 | 2025-08-25 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c937ab1c-94b9-3199-8e8a-da83edc4ae4b | -14.25774 | -48.04683 | 2025-08-25 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9350248-fa01-3d9a-b604-d6fecbcc9f21 | -18.44846 | -47.55559 | 2025-08-25 05:06:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f76f2d2b-8008-35dd-811f-2a0fe942702b | -13.06701 | -56.91777 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe2fec2b-0ed6-3575-b241-99422b587361 | -13.42654 | -46.90568 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28172ad6-c9cc-3278-a1d7-eed5bf483990 | -15.13411 | -59.59716 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15dc0600-c0ad-391c-aaac-8a73b16a274e | -13.42702 | -46.90146 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e0ef9df-f1f8-37fa-a628-dfa0d28183e4 | -13.11323 | -57.1211 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7e4cd88-0479-3cd0-8003-e7a76c23da7d | -14.20811 | -58.62989 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d921cfb6-971d-3a15-91d0-a3a696570bab | -15.1443 | -59.59895 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ab4702a-e442-354b-8e56-4c60d6ddceb4 | -14.26556 | -58.61364 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7edf04f4-580e-332b-849e-1a1c09f5d148 | -15.03804 | -48.52237 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1d4310d-b674-3b97-8008-847954dc8445 | -11.70035 | -60.17736 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25ee33f7-4e36-307a-93d9-ca44ecca7c6f | -15.14555 | -59.59142 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9988e68-b167-3abb-9bf9-35716482e317 | -12.16726 | -60.7467 | 2025-08-25 05:06:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b872f2db-efc8-3a46-98e2-de0f54a6f4c4 | -14.11425 | -53.99723 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 320d2157-0070-3384-bdbe-08aea0c8572c | -15.14956 | -59.58825 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b5ac57f-d525-31cd-9ed4-4c8035b94e06 | -15.03426 | -48.50799 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de0846b-3b47-301d-9fd0-5aa4b9c0557f | -15.17939 | -48.20013 | 2025-08-25 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 768d4939-0fa1-3c07-b789-73806d35a82b | -14.7125 | -55.93027 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33339952-9e06-3e22-b38b-43c0fc9535d1 | -13.50827 | -46.91368 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07f3cea6-aec7-380e-89be-f28065ffc61c | -18.23293 | -49.25813 | 2025-08-25 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00646f26-70a7-34fa-be57-3694d23ec578 | -13.00459 | -56.88261 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08bae953-d24f-325d-ab2d-097cd4b69312 | -14.1075 | -53.99158 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 130eaffb-c511-3f2a-9c8f-2a514a0f02ad | -14.10835 | -53.9934 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9a9c87a-924a-3c6e-b864-9fbe3541f80c | -17.57634 | -48.73336 | 2025-08-25 05:06:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 399d6350-50a8-3552-a8da-aae1f587ee62 | -12.05367 | -63.15218 | 2025-08-25 05:06:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README75.md)
