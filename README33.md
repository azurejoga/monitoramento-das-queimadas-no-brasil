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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43b1ccc9-bf43-39be-a40e-a23142778517 | -4.22189 | -47.21396 | 2024-11-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f82e79e3-dba0-39e4-b0cc-e551ed7ccbbb | -2.66299 | -46.20129 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59f27915-2a3c-3f6f-aadd-ec141342235c | -3.74368 | -45.65237 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0805111e-1bbc-37f4-95f6-ba8f09584d81 | -1.86501 | -54.27738 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5670dc3f-1de6-3a55-8bcd-61d7b7076974 | -2.81383 | -46.6632 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e194cc4-d8f8-3588-b068-8eb21264d3d6 | -3.12724 | -45.89528 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2131ce44-e4b2-3925-b1df-04edb3a3fa0d | -2.16672 | -46.40558 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1df54f44-cd54-3e5f-912b-989d15ea3c69 | -3.99043 | -48.41796 | 2024-11-16 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41d40f2d-fabd-38fa-97d6-4724eeea1c68 | -3.79189 | -43.91007 | 2024-11-16 04:23:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e9fe8ee1-0a05-36a1-9fc1-9f3b0c876269 | -4.20677 | -45.61557 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2327819-7134-3f82-a314-1de25c34edb1 | -2.07472 | -48.5447 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 383a3eac-f322-332b-9a93-c4160ebf8368 | -2.8861 | -40.38946 | 2024-11-16 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54a8b8cd-a13a-35f1-8a05-9db4d5a87424 | -2.13969 | -46.55479 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 56dd2f8b-4431-3c08-a7ff-1c76a09c6f5a | -3.63884 | -43.61247 | 2024-11-16 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b026acde-529c-3676-826d-cf86aeed2b0b | -3.79669 | -40.99253 | 2024-11-16 04:23:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c8ae99f-55a9-3b14-bb32-afeb1192e5e0 | -2.55929 | -46.90471 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c75e70ff-ce6f-3c43-8a8f-0d1f5041b1ab | -2.35863 | -49.12027 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73d2206b-775a-3935-904a-a647db3852f2 | -2.19625 | -45.12359 | 2024-11-16 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1363719e-8f34-3862-9de0-be7ad0245246 | -4.01528 | -43.9995 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c31d25a3-eb33-3406-a0c8-e4910320336a | -3.97752 | -46.70638 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1209d44d-19e9-37b5-9c1a-a0dedcb0b9f6 | -0.64958 | -49.39376 | 2024-11-16 04:23:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be9cedee-9cda-376b-ab08-5126eb81b567 | -2.34552 | -47.46548 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2b1b5418-12fd-3d60-92fa-d947d2d863c6 | -2.29176 | -46.45425 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db1b55c5-cb7b-3f4f-9865-1b47609d8f17 | -3.91228 | -49.04199 | 2024-11-16 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ae555c22-831c-361e-a5a1-d41f3dcbcb68 | -2.55048 | -45.47564 | 2024-11-16 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81cca569-0de0-30be-b163-48b60da7d969 | -2.13678 | -50.81655 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30499fd8-5ca4-36ad-8b84-24cd471a8c39 | -2.68285 | -46.83091 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bd83f5b-4189-3a28-82d7-26b95021694f | -3.76433 | -50.78605 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 007cd3ed-0a04-3ad4-ac95-a3c001e07554 | -2.62013 | -46.25569 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff61697-eed3-30ff-a949-65762ad7a2a4 | -4.03294 | -44.10974 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d19baa8f-7b9a-3d3f-876b-8effbec84498 | -4.22619 | -50.6737 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d039190-24dc-38df-8a4f-11bf0b7fd138 | -2.66909 | -46.18429 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 133691bd-35ea-3803-b57a-5a656db8a1ca | -2.1921 | -46.60329 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81814335-0995-3c5d-b720-5c04dde2c9a6 | -2.63084 | -46.83006 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c3f9aae-72af-3eb6-9214-a38eaa7d47f6 | -2.36033 | -47.14808 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b99cf47-b503-31af-a874-1860aebe047e | -2.65406 | -46.1927 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de5bdfc8-bbfa-3fdf-81e2-17ecfa3e8cc3 | -2.66743 | -46.19481 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a1feac0-2f14-3a60-a609-1b4d1b7cbe8c | -3.73992 | -50.18739 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a55b8c45-7bac-3197-93f4-bad1beb9bcd6 | -2.03609 | -46.37393 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5432bbd-4996-33b4-8fe5-df3387cfa35f | -3.95849 | -46.7179 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93ec8c18-795a-3c94-acbf-14a0a2afbdbe | -3.74036 | -45.65185 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ff3e3397-4ae0-350e-b87b-9145056c2c0d | -3.54552 | -51.59245 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 178ab285-e10a-35ee-983f-e4b2d2c8d99b | -3.79186 | -43.90936 | 2024-11-16 04:23:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f4543ed-4e94-3379-89cd-38250da6e7ba | -2.68171 | -46.83817 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2a9a621-56cd-31b4-ad2c-dc5c7fbbe75d | -4.31292 | -43.63261 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d9cd756-de1d-3365-aa07-4ccb5ab4fe83 | -1.13246 | -54.17123 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5cfd6ca-7e03-36a3-a3f2-b5458fbc27eb | -2.17164 | -48.33374 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3dd0049-484a-3f33-9d6d-804c81b802d3 | -4.15954 | -48.59716 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6268cded-8223-3a16-801b-d13a8cdfe438 | -3.58548 | -50.52937 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 38498578-ef46-304d-8749-48d9f6fe0986 | -2.20617 | -46.04725 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 600b5639-65b2-32f9-9a95-3e1a79e04875 | -4.9995 | -44.31594 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4379dae-56f3-3b1a-9340-c59b61c911c9 | -2.92386 | -48.31769 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36695a29-8bf4-38c6-9d86-f70a8125bd39 | -2.68003 | -46.82676 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e45746c0-560c-322d-8364-34c34db88aec | -2.9268 | -48.32233 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 302413b2-dcc4-3f9f-b0e0-5959626741eb | -1.21392 | -53.56559 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224520e9-54c8-3a61-b89e-8372c8aa2495 | -3.11357 | -45.98198 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ae8b39c-ed1d-3c5f-9f2d-930cd92765e8 | -3.28343 | -45.50623 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| c0d1a0c7-0270-32ad-ba65-60dfa13a7c43 | -3.75962 | -50.78913 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84b63ab2-e76e-320b-88ec-fe21df93119a | -1.89665 | -47.00856 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e72f5051-777d-3cfa-aa22-80c610810a41 | -3.31443 | -45.33093 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836509d5-5bf7-3621-bdd4-1d17cd7fff90 | -1.15855 | -53.50814 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9c3bc6-cabd-37d6-8383-98485da3f96a | -2.63583 | -46.55893 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 574ac248-d741-3569-8ba6-1b738073ef35 | -2.6806 | -46.82312 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc74fbcf-6442-374e-85ba-d73b2a427058 | -3.36809 | -46.1253 | 2024-11-16 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8343451a-caa8-304f-b74e-c4b9569f7dca | -2.23855 | -47.20954 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a496cf08-2178-36b0-ac60-cb4b4b07c026 | -4.37517 | -45.62428 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c7712c-5abc-3a69-8840-f0d35b56eae8 | -1.68648 | -54.26278 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df883cb7-a870-3f2f-b88b-3e1fe270eec5 | -2.90365 | -48.30612 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae2eb2a5-33c9-35e4-b6b3-cf709a0a17bf | -4.27474 | -50.68151 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dde7772d-df01-3b55-b39c-7c7cf5e1b384 | -3.96237 | -43.89112 | 2024-11-16 04:23:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57b7d9e3-3846-3cfd-bb0f-2a89004caf8a | -1.22896 | -53.70428 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ff1cb0c-7ecf-3c26-9b95-0ec0638fa320 | -4.126 | -46.94089 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec3e13bf-4b66-37ff-a618-96bd0fd781a9 | -2.93757 | -48.32402 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a7f89f1-03f8-3334-a682-8a1e097472c6 | -2.90724 | -48.30668 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcff260e-5215-30a9-a8dc-0a5145030db9 | -3.99471 | -46.40283 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16a226df-4ce5-3a7a-a9be-4ca578c6d5dc | -3.94005 | -46.40797 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51cb7dad-6f46-3f0d-9517-38f68a29bbe8 | -4.90829 | -44.02592 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2291347-ee26-32f9-9ab6-3bab72a57c00 | -2.1398 | -46.40136 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c818a8e-440c-3851-b6e2-43ce7c7b21fb | -4.3772 | -48.56675 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae740a76-289a-3a9b-a643-0d55a4779dbb | -3.58893 | -47.34821 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9194fbe-66b1-3116-a0d7-7a3f08e6e03e | -3.9375 | -44.09545 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0381d7ef-14c1-36d6-bedf-6d6673c293d1 | -2.28217 | -47.91377 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cf9229ea-5b11-31dd-af38-2543ddda397d | -4.13218 | -46.94551 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac0aeeef-8b0b-3d07-9cc0-4359fae22c39 | -3.58023 | -50.5104 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8bb9346-1701-3618-ba30-bd4558ae7d1d | -4.18478 | -43.94302 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b61a0ea8-1129-3467-a3c8-4d7ae72f84bc | -2.84996 | -46.66138 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f734ee9-24bb-34a4-9f21-1c5badc52536 | -2.71014 | -47.99008 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15c5d0b-d0d9-3fb1-8157-99deb9215cb0 | -5.67111 | -35.65 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 75df6133-df3a-3649-b2f6-cb79899f6310 | -2.18906 | -50.32758 | 2024-11-16 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b0810e4-0a01-3b67-85e3-5fc6270d8a79 | -2.68212 | -46.83769 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a64c8e36-6f4e-3179-b644-50f4e2b456af | -4.90858 | -43.22989 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97cf1f17-b371-3e62-999e-0f9442f6be5f | -4.3339 | -48.64463 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95c56eda-c543-3379-9876-f05809119b97 | -3.206 | -46.68041 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59aaf522-6ba4-3b75-b45c-1b278f0880be | -3.9691 | -46.39166 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77a0975f-325e-3a12-ba81-68dc505858f4 | -2.62677 | -46.192 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfc3e070-b8ac-3b14-9f48-274702032a51 | -2.88556 | -40.39296 | 2024-11-16 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 90b2ca97-6cec-3440-89a8-9e4d2f64707c | -4.87748 | -45.05285 | 2024-11-16 04:23:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a936be8a-7c8c-3a94-8751-fab9a3ded704 | -1.86983 | -54.28165 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1399cfc-0ea2-34f2-8b2e-923340fe7194 | -2.35256 | -49.10993 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66cc03c2-c6ea-316f-b4bc-dc5ee0caac8a | -3.21678 | -42.08315 | 2024-11-16 04:23:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README34.md)
