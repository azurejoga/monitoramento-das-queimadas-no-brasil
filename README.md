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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6fba790-ba86-3314-8cc2-14dfea2d42e4 | -11.9874 | -57.2076 | 2025-06-12 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| d5576ab3-d49d-3d11-9191-db1fe0813351 | -13.9056 | -54.6498 | 2025-06-12 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e067fbaf-f814-39cf-8cda-f9c771bec1a3 | -10.883 | -54.7624 | 2025-06-12 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 71cc88d6-ea41-3ff0-8479-9f084831021a | -13.2798 | -57.0751 | 2025-06-12 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 801516fb-04b0-3108-be4a-7d4a256e0128 | -13.2989 | -57.0734 | 2025-06-12 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 220.0 |
| 8b7fd00e-d36b-3d91-a101-a0a51055a9c5 | -20.5625 | -50.0948 | 2025-06-12 00:00:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| a7bf256f-1eed-3944-ac40-a9e09772dcc4 | -7.4575 | -45.5116 | 2025-06-12 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1f3d8692-323f-3a31-9440-a4beeb3c4051 | -13.2986 | -57.0935 | 2025-06-12 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 142.9 |
| b8c9de2e-0eee-33b9-9f6e-a8f69f197301 | -11.9278 | -57.4717 | 2025-06-12 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9c38f767-0c55-3d1c-a9c4-924c52603bcd | -10.669 | -49.3597 | 2025-06-12 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2146abe3-cff0-3e49-8baf-6c4f119c9d5b | -10.7048 | -49.507 | 2025-06-12 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9d27a856-e95a-3836-9392-5c4b93a91e53 | -7.4577 | -45.489 | 2025-06-12 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 2eb2a77b-a7a7-36aa-a6ef-b1cc5bacfd0e | -12.7169 | -58.0242 | 2025-06-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2c304c42-cf70-31d1-932b-fa12cc98b728 | -10.8832 | -54.742 | 2025-06-12 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e7ab0d33-2b3c-3a83-9928-d30e3e921481 | -7.4763 | -45.5099 | 2025-06-12 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 436ad50e-c491-3b4b-9e6a-42ade6e1d294 | -5.639 | -43.6015 | 2025-06-12 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7806814a-e58a-3e28-a1f7-58686f8bb7cd | -20.5619 | -50.1175 | 2025-06-12 00:00:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.2 |
| d3bb55fe-1747-344f-a84c-4246b3731864 | -5.6577 | -43.6001 | 2025-06-12 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 962c4be8-19f8-3762-aab0-f99c1066c2e4 | -13.8864 | -54.6519 | 2025-06-12 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 3d409e4c-0591-390b-a081-d1bf52134097 | -7.2403 | -43.1134 | 2025-06-12 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 0fc7be79-47a3-3d24-857e-5ad2570509ce | -13.2991 | -57.0532 | 2025-06-12 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 14d27211-c1e4-3fc8-843f-751ed26a1862 | -12.0063 | -57.2061 | 2025-06-12 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| eca9a89c-8def-31a2-ac0c-d7e116dcf58b | -12.6979 | -58.0257 | 2025-06-12 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| cbf73ecf-1249-38ec-be71-2d09c4977364 | -13.2796 | -57.0952 | 2025-06-12 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b63b5851-370a-3a4a-9688-5665e829091a | -13.8867 | -54.6312 | 2025-06-12 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 876e50f2-2bb3-3179-8c6f-e8c1255c6084 | -10.669 | -49.3597 | 2025-06-12 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 49ff7893-6dc8-32f5-8cdc-2ae8a3562700 | -13.2798 | -57.0751 | 2025-06-12 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| e28c0838-f24a-3bb5-a58b-2cb0f2c776ff | -10.7048 | -49.507 | 2025-06-12 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7fcaa16a-de55-3bbd-96b8-9118891ad3b7 | -7.4765 | -45.4872 | 2025-06-12 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 2c85f54e-0822-3e51-91aa-c0a53d265ccd | -13.9056 | -54.6498 | 2025-06-12 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0d701d2a-9d8c-3567-b5e7-b522a87357f0 | -10.8832 | -54.742 | 2025-06-12 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| aa4e4fe0-d208-30bf-98e9-021b34ac2698 | -13.8864 | -54.6519 | 2025-06-12 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| b816d05e-8930-3614-8ff1-b619ed108b8d | -7.4577 | -45.489 | 2025-06-12 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c0f09bdb-d374-313b-ab59-e5a09a25c5c8 | -13.8867 | -54.6312 | 2025-06-12 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| cce0a6e2-1d1e-3741-8f9b-7e3331a8aa59 | -13.2989 | -57.0734 | 2025-06-12 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 201.3 |
| b7df7d51-0d70-3cb0-b9f8-d550071399cf | -13.2796 | -57.0952 | 2025-06-12 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 63dc7733-79a5-3181-aa75-fa953383d3c6 | -10.883 | -54.7624 | 2025-06-12 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d4f0e2b1-c63c-384d-8eb8-64d3aa771a2f | -13.2991 | -57.0532 | 2025-06-12 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8ccb3220-236c-34a2-b0cc-a9470b5d52b3 | -13.2986 | -57.0935 | 2025-06-12 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 393acc45-68df-3630-8e1a-31eb411d5f60 | -20.5619 | -50.1175 | 2025-06-12 00:10:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.0 |
| 7e732319-77fd-3c25-af75-53f5ad1c5e01 | -20.5625 | -50.0948 | 2025-06-12 00:10:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| e1da44dd-6761-3a7e-b3eb-bea4287227d5 | -11.9278 | -57.4717 | 2025-06-12 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 129bacc0-52e0-39cc-820f-482680ab88e3 | -12.0063 | -57.2061 | 2025-06-12 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 09116479-aabf-385c-a51a-fc872dee2ccc | -11.9874 | -57.2076 | 2025-06-12 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 23db0efc-1fc9-3dd1-a5c1-c50f441f5e11 | -7.2403 | -43.1134 | 2025-06-12 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| c32e216b-1c56-3302-a600-8af3cf745816 | -12.6979 | -58.0257 | 2025-06-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 51693d23-ddd9-3baa-ace7-ade16d6d453a | -7.4575 | -45.5116 | 2025-06-12 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| d8d8051a-fd23-350b-80ae-280a6b1f44ca | -12.7169 | -58.0242 | 2025-06-12 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| a2301664-357a-36e3-ab6c-c42a4eb77087 | -7.4763 | -45.5099 | 2025-06-12 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| fb5bc9f5-66d8-3e70-8b61-9e49830ee979 | -5.6577 | -43.6001 | 2025-06-12 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 98ad18e3-ec9e-30f9-b2eb-2fa86aee29f8 | -7.4572 | -45.5342 | 2025-06-12 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 73e08c4c-4124-3a1f-a623-c083d876779c | -20.44918 | -46.40957 | 2025-06-12 00:18:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0e514143-e6ed-3b30-8c42-3784d59aea00 | -20.55394 | -50.11712 | 2025-06-12 00:18:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| 5a5f91e5-11c5-3199-a049-6f00686a0fa7 | -17.29321 | -42.6668 | 2025-06-12 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca364815-c4f7-34a5-8519-056e77cadd7f | -20.44439 | -46.40394 | 2025-06-12 00:18:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 27ae094b-f771-3e70-a92a-3baaf1137cfd | -20.56437 | -50.11086 | 2025-06-12 00:18:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 180.5 |
| ea07bf92-b115-395e-830a-0d1fb986814c | -9.2622 | -57.5426 | 2025-06-12 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3a316266-f575-3ece-875d-922d4c085596 | -7.476 | -45.5325 | 2025-06-12 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 002119a0-15a9-32fc-80fa-809507db3b85 | -11.9874 | -57.2076 | 2025-06-12 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 9e29b50e-9eca-362f-9200-a885c146d2bf | -10.7048 | -49.507 | 2025-06-12 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 263dec2a-a027-36c5-939f-7063b9fcaf7f | -12.7169 | -58.0242 | 2025-06-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 97cd0607-3904-3717-b514-9b5ed35c3c44 | -13.9056 | -54.6498 | 2025-06-12 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| bdd3fe16-a1bf-38bc-a1ac-afb65aac4b29 | -12.6979 | -58.0257 | 2025-06-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 45df10ea-5e78-3e3e-b8ff-7808d8cc13c4 | -13.2991 | -57.0532 | 2025-06-12 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3ff654b7-4587-3100-8f3f-44cd7cac9276 | -13.9059 | -54.6291 | 2025-06-12 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 76c2ab82-a33b-388c-b08c-199ba27d0425 | -7.4763 | -45.5099 | 2025-06-12 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5dd440d5-c681-39a3-97b4-39570b4633b0 | -20.5625 | -50.0948 | 2025-06-12 00:20:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.5 |
| 48addeb5-1595-3434-a427-8833738570fa | -9.5156 | -40.3061 | 2025-06-12 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.2 |
| d80b4221-cf6d-3597-a8f5-d7b7746559b1 | -13.8864 | -54.6519 | 2025-06-12 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 23d808b1-6745-358e-9bd6-8e1994c1b08e | -10.6492 | -49.4267 | 2025-06-12 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0e36b9ef-9aea-385d-8cb6-9d483033cdc6 | -12.0063 | -57.2061 | 2025-06-12 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cc154e7a-9c01-33f7-9bfc-eca0f48507c5 | -10.8832 | -54.742 | 2025-06-12 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| db279838-0ccb-3eba-87da-8e6f537af466 | -7.2403 | -43.1134 | 2025-06-12 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| a8751216-5a98-3ce4-8ce4-b63337fd4450 | -10.883 | -54.7624 | 2025-06-12 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4dc32aea-2f34-3867-b6de-6cc4b5338165 | -7.4575 | -45.5116 | 2025-06-12 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f7ea3138-336e-39f8-8790-098990e4220f | -13.2989 | -57.0734 | 2025-06-12 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 189.1 |
| 75c74443-9d62-32d1-9eb8-4967fd68ee2b | -10.2487 | -46.9702 | 2025-06-12 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 39788963-d235-3ae2-93bd-51cda303a314 | -13.2798 | -57.0751 | 2025-06-12 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 18d2f17a-e643-348e-955f-54387e0f32ac | -11.9278 | -57.4717 | 2025-06-12 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| d9f337a3-3da8-3bc8-9659-83ffbcca2167 | -13.2986 | -57.0935 | 2025-06-12 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 5aa82281-c1c1-3b14-985d-943617e17326 | -20.5619 | -50.1175 | 2025-06-12 00:20:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| a4ef1b4f-12fe-3b8f-a806-cc4f231f3862 | -11.27197 | -44.64685 | 2025-06-12 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d0509fdb-c82e-380f-91ac-d446eba3b5ac | -14.17602 | -45.49324 | 2025-06-12 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a9e5970d-dbf1-3060-8ebe-8f0ac7710429 | -10.25662 | -46.97968 | 2025-06-12 00:20:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 087ea924-0192-3037-b994-c6c3eabad9d5 | -10.24443 | -46.96811 | 2025-06-12 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 27cc8bd1-6c2a-384a-a518-9eee5a3d755f | -12.8279 | -47.37558 | 2025-06-12 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 000b9259-0f25-3d56-96b8-04c5d4a6673b | -14.18604 | -45.49188 | 2025-06-12 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e29111ce-b542-3d39-a63b-d775943409d5 | -11.88491 | -40.95478 | 2025-06-12 00:20:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ee3299e6-ec14-39c9-bf2f-782c2e00d41e | -12.82974 | -47.39088 | 2025-06-12 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 11550ab7-f489-337b-8b8a-b2b8ea6a7484 | -6.95258 | -44.56454 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f3a5a8dd-6d3b-3ec4-9507-eaa417b8309a | -9.51551 | -40.32299 | 2025-06-12 00:20:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 0f628fdf-b35a-3c3b-a2d3-7a32219c5be8 | -12.39611 | -40.91486 | 2025-06-12 00:20:00 | TERRA_M-M | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e01ce3ce-3c5e-381a-87f7-9e897d5fae99 | -10.65876 | -49.4402 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 48b8c173-33d4-32a1-ae5f-a7e91ccc23a2 | -9.85713 | -47.88044 | 2025-06-12 00:20:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 616077ae-72f8-3e6b-ba5f-07ce744872e5 | -7.23806 | -43.10058 | 2025-06-12 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d7d87889-16e9-3fdc-ad7b-698f7c467e23 | -12.23 | -44.1687 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8dc1282d-bb0a-3431-bdbf-16e759786f7e | -15.93091 | -43.9837 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 81ba6146-4743-3dec-985a-76d5e4d5582d | -14.18754 | -45.50374 | 2025-06-12 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 635a677e-0266-3894-a10c-4e95543df541 | -10.66279 | -49.36352 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9ac3d8a7-1051-3b82-938c-e9402999c540 | -15.37976 | -47.89319 | 2025-06-12 00:20:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |


[Clique aqui para ver as próximas entradas](README2.md)
