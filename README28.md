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
| 8c55ee02-04b2-3b1d-b592-7948bad5adc6 | -14.01392 | -43.47714 | 2025-11-02 06:14:00 | AQUA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| f2770fc3-591f-3eac-866d-e7c121a6be27 | -15.34256 | -50.29232 | 2025-11-02 06:14:00 | AQUA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4ad634f2-7a18-3773-85cc-ad84c52c1814 | -13.97689 | -51.50348 | 2025-11-02 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e47c8c3-b6d0-3c78-84fe-831b33123648 | -12.86235 | -50.87649 | 2025-11-02 06:14:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7102a3d2-7d51-30d9-804f-568224e5ec7e | -15.62836 | -58.22402 | 2025-11-02 06:14:00 | AQUA_M-M | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| ec55a2c1-e775-34d9-8c48-8732978928fe | -12.88475 | -50.85899 | 2025-11-02 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1020a01e-631e-301d-ac8a-73b01f801436 | -15.25469 | -51.74404 | 2025-11-02 06:14:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3fef014b-f0d3-331e-962f-f9b1250955c6 | -12.88338 | -50.86798 | 2025-11-02 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| feca7e2d-125e-350a-998a-c38fb64e47cf | -15.61785 | -58.21683 | 2025-11-02 06:14:00 | AQUA_M-M | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| ffff30bd-6de5-3d39-9bcf-410669a225c5 | -12.87388 | -50.85989 | 2025-11-02 06:14:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| f73d00cd-8456-344f-ad5f-425efe752287 | -14.45456 | -51.53259 | 2025-11-02 06:14:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 53647c41-9008-339e-886c-75babb64e19a | -14.45596 | -51.52347 | 2025-11-02 06:14:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 622b430f-9ae0-38fe-9656-e41fb286da2b | -12.88064 | -50.88595 | 2025-11-02 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 146f172e-4553-3e06-9abc-edd834420bf8 | -12.86099 | -50.88548 | 2025-11-02 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a958c88b-7b0e-3d64-ba29-a9deda8cf2f4 | -12.87252 | -50.86887 | 2025-11-02 06:14:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a2e2c763-8fec-3a69-845b-2aeb6de70e2c | -14.02753 | -43.47879 | 2025-11-02 06:14:00 | AQUA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 8ecb644f-9321-3715-a178-7dc5767ab499 | -12.86371 | -50.8675 | 2025-11-02 06:14:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 83bcf5f8-c919-3bc0-80e7-2fbce428876e | -4.60508 | -38.46443 | 2025-11-02 11:36:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| ed996eeb-5e84-3ebd-abd8-828c246ecfd3 | -4.58596 | -38.47089 | 2025-11-02 11:36:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 927c5e33-7fe6-3490-9afc-a07afc8a6faa | -4.60377 | -38.47342 | 2025-11-02 11:36:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 48bd0e96-a9ab-346b-be5e-1bb5d2c6bdab | -4.58727 | -38.46192 | 2025-11-02 11:36:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 63d78901-fecb-3b9d-8e64-d9a58962b71d | -5.36028 | -36.15494 | 2025-11-02 11:36:00 | TERRA_M-M | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 12832e55-bc56-3aa4-8e97-a37b2ef8d38f | -6.09167 | -35.35184 | 2025-11-02 11:38:00 | TERRA_M-M | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| cca1e778-3725-3f7c-9e22-b7211d0148b6 | -6.05987 | -39.62427 | 2025-11-02 11:38:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 4afeb9f0-9038-36ad-b7b9-a9e553adec94 | -6.01845 | -38.90256 | 2025-11-02 11:38:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 9352ef97-a52f-3994-9831-85f1498a45c2 | -9.10905 | -40.23167 | 2025-11-02 11:38:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4c172282-edd7-337f-9368-f95c01af21d6 | -6.26407 | -36.35138 | 2025-11-02 11:38:00 | TERRA_M-M | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 13c19a8c-6683-360f-8b10-2ff86c775d49 | -6.01978 | -38.8935 | 2025-11-02 11:38:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 53.8 |
| f671acc8-2959-3cbe-8e4a-0790b5a682e0 | -9.08596 | -41.12043 | 2025-11-02 11:38:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 28e2df83-359b-36dd-9f32-8930a2ffa4c6 | -11.20037 | -38.41854 | 2025-11-02 11:38:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d29c4b18-34db-31ee-966b-6bbd142bc3c7 | -8.86929 | -37.94562 | 2025-11-02 11:38:00 | TERRA_M-M | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 71cddca1-0161-36f8-802b-ac24f7b4c602 | -7.98099 | -38.86337 | 2025-11-02 11:38:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 13.3 |
| f1b1f805-a475-36b9-b608-1ce405c58f51 | -6.4797 | -39.4102 | 2025-11-02 11:38:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| e5ed90d1-c6de-38c6-9c17-c2abe4b66727 | -6.09022 | -35.36218 | 2025-11-02 11:38:00 | TERRA_M-M | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0138e481-2fe0-3870-a48e-2fca426feb94 | -9.91527 | -44.86428 | 2025-11-02 11:38:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 3fe48393-9310-3b8f-84c2-f572fa313d54 | -8.12751 | -35.5227 | 2025-11-02 11:38:00 | TERRA_M-M | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 6662f97d-4e25-3728-9cfe-00f369bdc5d4 | -6.59452 | -37.92713 | 2025-11-02 11:38:00 | TERRA_M-M | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 003b2905-812a-3257-a2a3-532e7eb39812 | -12.58509 | -42.83861 | 2025-11-02 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 75b55974-96bb-37c7-984e-2c4c021f66d9 | -13.15779 | -42.27062 | 2025-11-02 11:40:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| b8f8eb62-7987-3636-87f9-5b9652b674e1 | -13.81023 | -42.88505 | 2025-11-02 11:40:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 545f0627-cfd8-3110-b4dd-5966954cb0bd | -13.96672 | -43.26125 | 2025-11-02 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 8f231529-ece3-3de7-be46-07a1a56a8b4b | -14.02341 | -43.48603 | 2025-11-02 11:40:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c9d15be2-4c3f-3493-9576-0a7de39ae2ce | -12.67689 | -38.28347 | 2025-11-02 11:40:00 | TERRA_M-M | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 9af4266d-c401-3cd0-849c-13f3bf1a6dab | -12.58762 | -42.8327 | 2025-11-02 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 2d3c691a-5a63-3347-bb4a-9b4f96014836 | -12.5832 | -42.85039 | 2025-11-02 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 74fb2bf1-8c99-391e-a494-4b84000998b0 | -14.02546 | -43.47312 | 2025-11-02 11:40:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 351979bf-3b40-3274-b97a-99ec88ff9064 | -12.67806 | -42.3827 | 2025-11-02 11:40:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 7bb3dce3-41e0-3119-a036-9ff923e47060 | -12.5756 | -42.84291 | 2025-11-02 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| a310b709-7296-36ca-a66e-92c88198f91f | -12.81118 | -42.7752 | 2025-11-02 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| aaac2263-f076-33c8-9920-efb6028d0180 | -13.15602 | -42.28186 | 2025-11-02 11:40:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 350a9c3b-11b8-3fcd-ace2-2f9f3f79f5e7 | -12.58578 | -42.84465 | 2025-11-02 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 88.6 |
| ee52ea08-36f8-3a68-a501-8ba4d1f68581 | -12.85404 | -43.46051 | 2025-11-02 11:40:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 43020b75-12f1-3b8e-b920-91a512d98fd2 | -12.84998 | -43.45316 | 2025-11-02 11:40:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 4aa77bde-ab26-3a84-a4ae-0a41c86ee23a | -12.80923 | -42.78753 | 2025-11-02 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| f1e85f21-7bd8-3bc0-8d46-23d4b40e3af4 | -13.96474 | -43.27378 | 2025-11-02 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 40.3 |
| e0a4e8bd-8e01-3e5a-b755-24b6e3f24877 | -13.30319 | -41.92998 | 2025-11-02 11:40:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 1fc2968d-7f9a-3b28-95a8-68c941fce66b | -15.2463 | -51.7482 | 2025-11-02 12:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5aeb6d30-173f-3b36-81a9-2d9507324c85 | -15.2463 | -51.7482 | 2025-11-02 12:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 85c8e61b-ddb5-32b0-8753-b73062c8dfe6 | -15.2657 | -51.7455 | 2025-11-02 12:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| dff2f86b-0a5e-32cc-8343-b5053af8e505 | -13.9939 | -51.5126 | 2025-11-02 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d2655a8c-6f99-30e7-a5ab-643e2882bf20 | -13.9746 | -51.5151 | 2025-11-02 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ac6111e7-850e-37d0-831f-5790e4bb3d97 | -14.4756 | -51.5338 | 2025-11-02 12:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 16cc4ae5-b9ab-3301-9dbb-96e1c4ee0b11 | -14.476 | -51.5124 | 2025-11-02 12:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2343a10d-165e-3527-9320-6bed8c40fad7 | -14.495 | -51.5312 | 2025-11-02 12:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 20cf77c3-8ab5-3f3c-8579-b1b5002dd5c9 | -13.9939 | -51.5126 | 2025-11-02 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a319ff13-a612-39f5-aa31-8e0f4c6e9f54 | -14.4563 | -51.5364 | 2025-11-02 13:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| eaf01e40-2ff0-31a2-b269-b27e9f7d4caf | -1.2749 | -53.8573 | 2025-11-02 13:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1274a066-d2de-3307-946a-b082d5bb3f9d | -5.5304 | -41.0964 | 2025-11-02 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| a7c2ae96-c324-3b4f-89cf-25f78d435aca | 1.0028 | -51.2277 | 2025-11-02 13:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5d5f7a51-69d8-32b5-990f-5721646b8e16 | -13.9939 | -51.5126 | 2025-11-02 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a830cc23-006c-3a26-ab34-ce942a98d764 | -14.4756 | -51.5338 | 2025-11-02 13:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 81ece136-a13a-34e8-ab3c-8d3a9bd4d4ab | -14.476 | -51.5124 | 2025-11-02 13:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| eed69efd-8351-353c-89b6-0f42983d4a10 | -14.4566 | -51.515 | 2025-11-02 13:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4513fead-d97d-30be-b451-e004a4e0e268 | -14.4756 | -51.5338 | 2025-11-02 13:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 982d98a1-e796-3f46-840c-a8479b7d0c95 | -1.2749 | -53.8573 | 2025-11-02 13:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e0321cf6-c34a-3eee-a092-f1d6d15b1837 | -13.9939 | -51.5126 | 2025-11-02 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 463b5837-9924-3b94-b347-81efd971260c | -5.5304 | -41.0964 | 2025-11-02 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| 20ccf41a-4b3e-3d03-b333-c9cfd768b188 | -1.2565 | -53.8575 | 2025-11-02 13:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0bb4f2a3-9e32-3e6b-bc28-5990b3b40454 | -13.9746 | -51.5151 | 2025-11-02 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1216daf7-16ca-3891-a7d3-88f4c6fd3bda | -13.9939 | -51.5126 | 2025-11-02 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 3aabc279-d821-3fc3-b245-a73ba333ac82 | -1.2749 | -53.8573 | 2025-11-02 13:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 5e5fb3db-edcf-3ba2-b346-4e2e4f5ece69 | -5.5304 | -41.0964 | 2025-11-02 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 221.0 |
| 5820c57e-f8da-3252-80b4-de9abb4bcf0d | -13.9939 | -51.5126 | 2025-11-02 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 5eb2746d-5c2d-3d8e-9b64-d17e3ab5aabe | -1.2566 | -53.8374 | 2025-11-02 13:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| aa8f3fb6-6dfc-327a-b925-2d1760e99d6e | -1.2565 | -53.8575 | 2025-11-02 13:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| b7f20f86-19e5-3304-85c7-c0d5503c7b48 | -13.975 | -51.4937 | 2025-11-02 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 01324d77-9baa-3e0a-a7f9-a3a06cb672f9 | -13.9746 | -51.5151 | 2025-11-02 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0ff76656-0ef4-3a7f-8056-dd2dd55cf893 | -1.2565 | -53.8575 | 2025-11-02 13:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d65d37cf-5995-3c80-98f4-697e9dc84138 | -1.2749 | -53.8573 | 2025-11-02 13:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 8f584be5-b26d-3792-91c5-dc6c38eae278 | -13.975 | -51.4937 | 2025-11-02 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ef33462e-dc23-3be3-8f8d-3130daab7095 | -1.2566 | -53.8374 | 2025-11-02 13:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 16324361-2d50-3319-b7c8-c21043017361 | -7.0521 | -41.4653 | 2025-11-02 13:40:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| a4c647fe-863f-3f47-83e6-5455e69f29e6 | -13.9939 | -51.5126 | 2025-11-02 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 5d407251-a633-3455-b18c-a0fa344a9657 | -13.9746 | -51.5151 | 2025-11-02 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 1cb0d82c-f7aa-3792-850c-dc713c7555fc | -8.1658 | -44.4844 | 2025-11-02 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 688d54a3-11c7-3554-bc19-0f5e763519d1 | -1.2566 | -53.8374 | 2025-11-02 13:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 52de9e2b-9bc7-32b3-9bf1-2c5405c905af | -13.9939 | -51.5126 | 2025-11-02 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 332958b6-ee1a-3d10-980e-581d3297ed75 | -1.2565 | -53.8575 | 2025-11-02 13:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3d05c3f2-2b1a-3058-95de-f2f0a3d90a1a | -8.2225 | -44.4784 | 2025-11-02 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b139f715-4810-3d63-b6b2-f25bf186d76f | -7.0521 | -41.4653 | 2025-11-02 13:50:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |


[Clique aqui para ver as próximas entradas](README29.md)
