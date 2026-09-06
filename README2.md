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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 548d038d-f7ee-3339-8b2c-48a85ac4b839 | -4.0999 | -49.085098 | 2026-09-06 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ee1944-1eee-31e8-819c-f4b04d9c3539 | -3.2031 | -53.166302 | 2026-09-06 00:12:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dea7ab7-0620-393f-a24b-2565bd9a6da3 | -5.5064 | -44.021301 | 2026-09-06 00:12:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15e01561-ebe0-3af7-aa7b-dfce56673871 | -19.5301 | -43.532902 | 2026-09-06 00:12:00 | METOP-C | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 24722f74-681d-3486-8b75-bd6a5e6508e5 | -14.9109 | -44.678799 | 2026-09-06 00:12:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d8216ebb-a9b0-3689-9c08-56294905cafe | -6.4121 | -38.968498 | 2026-09-06 00:12:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7f82d9d1-396f-3048-831d-6a803d75b79a | -13.806 | -51.642399 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3e06b5b-f6ca-326c-9aa8-441d9c37ea0b | -3.6004 | -42.973999 | 2026-09-06 00:12:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ec10fa8-47b5-3229-beed-be01054e5bd6 | -4.1065 | -49.0686 | 2026-09-06 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d25fe70-8214-3e6b-af11-2cf8847169bb | -3.5519 | -48.183998 | 2026-09-06 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 849df6bb-2af4-3d72-ae61-c96d9af39e3f | -13.7577 | -51.6511 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e059bba-52e6-3b0f-bbf8-626b26e17d72 | -16.223 | -40.296101 | 2026-09-06 00:12:00 | METOP-C | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d4fcc84-9118-3976-a33a-328745cb7f34 | -4.1097 | -49.083 | 2026-09-06 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58c18258-b717-3605-abef-ad254a38b6ac | -13.7481 | -51.652901 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49cac0a1-e2ed-39d8-bb84-3363f7d91904 | -18.3808 | -39.958801 | 2026-09-06 00:12:00 | METOP-C | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8cdb4fe-0db4-3c9e-8be6-414a87c6c9a2 | -5.8942 | -44.742802 | 2026-09-06 00:12:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97e2b925-d607-36bc-8091-24c1f2f20f77 | -18.301201 | -40.935001 | 2026-09-06 00:12:00 | METOP-C | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db808917-467d-3a2b-8363-66ce48387f75 | -5.5686 | -49.035099 | 2026-09-06 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4b81cf9-e7f9-341d-88fe-a5f3ff3f4754 | -2.165 | -48.803501 | 2026-09-06 00:12:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601e5a33-fca1-32d8-95ad-8235f3f68049 | -6.4103 | -38.9608 | 2026-09-06 00:12:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f5a2fc3a-fb1e-3d04-9ead-3b2212926ae1 | -10.681 | -45.931499 | 2026-09-06 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c41b889-0773-3b5b-afff-85c9191ab602 | -13.3222 | -44.052898 | 2026-09-06 00:12:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e0efbee-c54f-3869-ad8c-18a6e74e7b9b | -12.9437 | -42.417999 | 2026-09-06 00:12:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8adaf8ab-3907-3807-9b81-78ae9eedda32 | -3.5394 | -48.173801 | 2026-09-06 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d535956b-5acd-3606-8b36-ade20e2076bd | -13.5356 | -43.997398 | 2026-09-06 00:12:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0f7273c-8443-3d70-8be2-4611b59edf07 | -16.2246 | -40.303398 | 2026-09-06 00:12:00 | METOP-C | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7aa0c96-2ae0-3aa2-bf75-15873ff697cd | -2.9835 | -47.751202 | 2026-09-06 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d399c452-1e21-3eba-956a-68e04df377e1 | -13.5375 | -44.006901 | 2026-09-06 00:12:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 662fed72-e6cf-37aa-9fde-6749fb94454e | -15.7107 | -43.694698 | 2026-09-06 00:12:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 147d5e1a-7ef2-3a12-a827-1264c72cbd9b | -11.2849 | -45.1115 | 2026-09-06 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16a701df-c771-372d-94a2-426ec7381221 | -14.9087 | -44.667999 | 2026-09-06 00:12:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eafae80c-fcc5-3c2d-a002-87bb20eb755c | -19.3584 | -40.014599 | 2026-09-06 00:12:00 | METOP-C | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ba7ef68-0dfd-3338-8ffa-b714282837a8 | -7.3668 | -47.014099 | 2026-09-06 00:12:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efcde4cf-7d6d-3e65-b849-98cb139ade50 | -18.916401 | -42.080002 | 2026-09-06 00:12:00 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0cc19690-ade2-336f-88ff-5804eee557f5 | -9.5672 | -40.338501 | 2026-09-06 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 29f47f60-73bc-3a32-aced-13393cc7a4c4 | -15.7127 | -43.704399 | 2026-09-06 00:12:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac7bd387-c1f6-3458-a93f-edf12752eba4 | -11.2871 | -45.1217 | 2026-09-06 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90db842a-6ee1-319c-96ea-3e6d87c374e6 | -13.4236 | -41.884102 | 2026-09-06 00:12:00 | METOP-C | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 33229d7a-d445-39b5-b6a8-942773e1ad94 | -8.9717 | -44.4016 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89556cd2-4a71-3dad-bed4-695109aec44c | -6.8736 | -41.052299 | 2026-09-06 00:12:00 | METOP-C | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49800802-72c0-3f40-a39f-de57c116aeb4 | -8.9637 | -44.412399 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 647065a4-7b6b-3bf4-a99b-0815c60cf588 | -16.7551 | -41.723999 | 2026-09-06 00:12:00 | METOP-C | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 677fff89-c204-3993-aa84-a54d727127bd | -4.3534 | -47.782299 | 2026-09-06 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f47a43d5-fa3a-3134-8464-10c9ed76f918 | -8.1166 | -40.8503 | 2026-09-06 00:12:00 | METOP-C | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9dc5acd9-82dc-3c3b-bf1e-f228bf385626 | -4.8063 | -49.373402 | 2026-09-06 00:12:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e8cfafc-5696-3f2c-94fe-68946c5fd7ec | -7.3694 | -47.025902 | 2026-09-06 00:12:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04e708f9-23f1-36b7-9b61-3e80f6689b32 | -14.8681 | -40.919601 | 2026-09-06 00:12:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e26f1397-0cb9-37c1-9816-758317e32717 | -13.7867 | -51.645901 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d2beeb97-4aeb-3df1-a95d-51a246048dc3 | -12.7114 | -43.1982 | 2026-09-06 00:12:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 905ea069-6406-35a8-a410-77eab4b9b939 | -10.6834 | -45.942799 | 2026-09-06 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9b850cb-083c-3417-bb64-07e390b3b4b5 | -8.9833 | -44.4081 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a0734a4-c87e-3ef4-bf75-6ebf623213df | -14.6098 | -41.055099 | 2026-09-06 00:12:00 | METOP-C | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c11a9315-ebd8-308f-9639-1e1529f232b7 | -4.3407 | -48.973099 | 2026-09-06 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eeb6eeb-3b65-3040-ac63-4ea441c371a5 | -4.4466 | -46.1283 | 2026-09-06 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd6c8beb-022a-3ad2-abfe-ca1bceff329d | -3.2068 | -53.137299 | 2026-09-06 00:12:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e7eb58-3731-3e50-a22b-8d3ad9fea18b | -8.9852 | -44.416801 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3cb56c1e-24c0-3245-bc31-f27dfb2219bc | -14.8649 | -40.904999 | 2026-09-06 00:12:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 398d2856-c13e-3dd9-934f-81da312b1e9f | -5.742 | -43.284599 | 2026-09-06 00:12:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1b4700-083a-3fb9-9b15-d965216a2b35 | -18.797701 | -41.598598 | 2026-09-06 00:12:00 | METOP-C | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ccd8c566-b2a9-3a16-810e-d1c447418f0d | -10.3817 | -46.8423 | 2026-09-06 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26d8fc47-b9a7-34bd-95b4-fae0b9cc777a | -13.4252 | -41.891602 | 2026-09-06 00:12:00 | METOP-C | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 41a52b45-9cce-33df-9b05-4c8dfd65b441 | -13.7771 | -51.647701 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82767334-697f-3dfa-96aa-104b6fb70289 | -4.893 | -45.092499 | 2026-09-06 00:12:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc0e98e5-a6cf-3d5c-9c18-af1da1d7c741 | -4.8098 | -49.389 | 2026-09-06 00:12:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1158da5-08e4-30ad-a891-0d091d384097 | -7.8919 | -47.701 | 2026-09-06 00:12:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4cba058-03bd-383e-a4eb-cd0421f378ce | -10.3844 | -46.855099 | 2026-09-06 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10245d27-0351-3c38-b377-5d01197c3b39 | -4.3507 | -47.770401 | 2026-09-06 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a636f6c-93dc-3432-a798-9507191415f8 | -18.796 | -41.590199 | 2026-09-06 00:12:00 | METOP-C | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| be8bc5d3-7bb2-31e3-89b2-dcba8e11aa0e | -15.4373 | -40.937199 | 2026-09-06 00:12:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9ab3f9c-76be-3b03-ae69-b8ddcf42a1ba | -3.5989 | -42.967098 | 2026-09-06 00:12:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6511eac4-35d3-3a40-9586-be899dab8a6c | -13.7522 | -51.620499 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4655c58f-cf4e-3e79-a4ae-4b0c87fb8f4a | -3.8521 | -42.947102 | 2026-09-06 00:12:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb235396-de5d-3ba4-a760-80d350890e1d | -13.3183 | -44.034 | 2026-09-06 00:12:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8505165b-49d5-3f9e-9221-84d23a50f3fc | -3.5449 | -48.198399 | 2026-09-06 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d37ea7-c155-3661-97ff-bf55c28d9aa3 | -14.9131 | -44.689701 | 2026-09-06 00:12:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62ce820a-e856-3dd7-bd20-964341c37d96 | -10.4848 | -46.067101 | 2026-09-06 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 439b0a70-1b65-3735-accb-5e0377da5d99 | -13.3202 | -44.043499 | 2026-09-06 00:12:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3fc4082-8ece-38cc-905f-3e3f0ce1fdf4 | -4.1407 | -45.634102 | 2026-09-06 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2831cf-057c-33ae-87e9-18c1eede1235 | -13.4269 | -41.8992 | 2026-09-06 00:12:00 | METOP-C | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a96eee7f-85fa-3299-8a4e-89d16844dadb | -5.5653 | -49.02 | 2026-09-06 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5b3d55c-fe21-3937-ac65-d403aa80669b | -3.2128 | -53.1642 | 2026-09-06 00:12:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c71e271-aea4-3afe-a016-d234413bf5aa | -5.4984 | -44.031101 | 2026-09-06 00:12:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 378de6b7-9867-3219-aa4d-18fae8fa7c65 | -4.4487 | -46.137699 | 2026-09-06 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4815db42-ff2b-3574-bbaa-280e0f293176 | -18.302799 | -40.942902 | 2026-09-06 00:12:00 | METOP-C | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2b7bc7d-1861-3047-a9b1-eddbaab37834 | -12.9535 | -42.415798 | 2026-09-06 00:12:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6aefbb50-d8a5-3390-834e-5f333b2936a9 | -3.1971 | -53.1394 | 2026-09-06 00:12:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c62e530-113e-3b53-947b-bd7b45a29e44 | -5.7388 | -43.270199 | 2026-09-06 00:12:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b516413-916e-3c65-92e4-42dc885e4568 | -2.9082 | -48.8759 | 2026-09-06 00:12:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abdc375b-471c-340d-9dba-a879084049e3 | -6.7068 | -44.0993 | 2026-09-06 00:12:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f775f5b3-cef3-3dc0-bfac-b8aed7febe5f | -18.9182 | -42.088902 | 2026-09-06 00:12:00 | METOP-C | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2af4125b-0820-3ce7-bab0-c75def764841 | -6.872 | -41.045399 | 2026-09-06 00:12:00 | METOP-C | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99234334-ad6f-304a-9db2-49e305f8c6f7 | -4.247 | -44.598 | 2026-09-06 00:12:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 124c0f3a-1727-34b9-8108-1cda6886e4a3 | -5.6934 | -44.487999 | 2026-09-06 00:12:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92c0f85e-56a4-3301-bd74-ae5e889c4d28 | -7.8891 | -47.687698 | 2026-09-06 00:12:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 396e12e3-e6dd-3b1b-97fe-43fd397c9b5f | -16.142799 | -40.683601 | 2026-09-06 00:12:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9fadcb2e-9aed-3589-b3d4-d7e638c8bfd2 | -8.9539 | -44.414501 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17ac8c1f-1a2a-3175-b238-5e143be0e4b3 | -10.4775 | -46.080502 | 2026-09-06 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 272c7500-bfaa-3b9f-a739-626c6b917146 | -5.6951 | -44.495998 | 2026-09-06 00:12:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db3c3755-dd2c-3d3d-a274-92087d481468 | -6.8646 | -41.645199 | 2026-09-06 00:12:00 | METOP-C | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1d91ffd-6ad4-38b1-8088-c33fba5c8a06 | -8.9815 | -44.399502 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
