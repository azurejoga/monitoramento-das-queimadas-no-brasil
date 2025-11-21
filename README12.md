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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40fbf671-f303-3841-8e52-e81354cd42e1 | -12.13557 | -56.99932 | 2025-11-21 05:05:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8efc2baa-a6e7-343b-93aa-e219ac4697c3 | -13.78884 | -49.57424 | 2025-11-21 05:05:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 027b0d64-cf25-39b8-838f-f53c4197151a | -12.20335 | -63.44448 | 2025-11-21 05:05:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21fa56ab-64cb-31f8-8030-ee4dea5e1fd0 | -12.87368 | -54.73822 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9df621bc-202a-3e3c-bd05-1e6153e19f46 | -12.88586 | -54.72803 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3b9b924-1667-3878-a395-d2540797a4a5 | -13.34688 | -54.34081 | 2025-11-21 05:05:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d11143e5-cd1d-3d5d-89c5-981cbe532444 | -20.49643 | -55.19309 | 2025-11-21 05:08:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd76b5f5-e98e-3bf7-bcaa-ddea0c4797a4 | -19.50121 | -55.34833 | 2025-11-21 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3f03b35b-6246-3fc4-89a4-4cd2b486b45c | -20.88498 | -52.34602 | 2025-11-21 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78aaed72-e403-39d5-a752-3d6d67118eda | -22.92421 | -48.68214 | 2025-11-21 05:08:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ee5d1e6-c231-3adf-bf19-448232d31507 | -22.91845 | -48.68172 | 2025-11-21 05:08:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4584fe9a-3aad-34c3-8765-09f5787b95de | -18.10223 | -54.51729 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2ae227b-01a8-3266-9759-6d1e2a70534e | -18.10336 | -54.52008 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 69cc3074-c315-3e7e-bbb4-8d25f9a35451 | -18.7549 | -53.96489 | 2025-11-21 05:08:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 326f500a-7fe7-32f7-b0d0-fc9c523abe3f | -19.48052 | -53.94455 | 2025-11-21 05:08:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecd52c48-0521-3153-9714-b763f33c95b1 | -21.04507 | -48.55954 | 2025-11-21 05:08:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2089a5bd-67fd-37ec-89f5-2078dcaafba6 | -17.6215 | -54.19727 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c8f73eb3-d1d9-314e-90eb-329195f19281 | -20.32067 | -53.98797 | 2025-11-21 05:08:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39bcb204-3125-375e-b5bb-9a445848d29e | -18.95348 | -55.18329 | 2025-11-21 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8fb5a1d6-c398-35f2-bbab-d89ca2897af4 | -19.50059 | -55.35276 | 2025-11-21 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5329ea43-61bc-3b20-974b-941fbeb50dff | -17.62213 | -54.19255 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a2e9c99-edd2-39fe-92b5-faa653436633 | -18.10708 | -54.52068 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2987c3d2-43fc-3750-86d7-c1a2613ced27 | -18.1077 | -54.51603 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95522191-1ef3-3f26-a49c-7fd1860e1044 | -22.92559 | -48.67904 | 2025-11-21 05:08:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beaf9a74-c6f7-3027-b363-8c70541e89d3 | -18.11455 | -54.52184 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f149be66-b2fb-36dc-94f7-025693bff401 | -16.26513 | -60.14745 | 2025-11-21 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f672269-e0b0-3748-b7f9-7fe1e6381724 | -20.25131 | -49.33759 | 2025-11-21 05:08:00 | NOAA-21 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9f921263-119b-38bc-b1e9-93a4f9959399 | -18.11082 | -54.52126 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e435d420-7d61-3a2b-abfe-01ba2b067e3b | -17.80973 | -54.68541 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8e4d95-be46-3d73-89c3-251bf4c2cb9b | -18.76297 | -45.28144 | 2025-11-21 05:08:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 059089ed-b112-392b-930e-4aa7e9df2480 | -17.62088 | -54.20194 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad31c607-b5af-316f-b848-4370e6658705 | -21.03974 | -48.55515 | 2025-11-21 05:08:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 423113e2-d74b-3cc2-b8a8-9c0e99712f34 | -20.88942 | -52.34653 | 2025-11-21 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51ba6555-9e16-3d04-be21-c45c71110c89 | -17.61836 | -54.19191 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 99d138a8-a0f9-32e5-892b-76f37a598bed | -18.10531 | -54.52253 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ba6b8983-e275-3ca7-a58c-0f5f224732f2 | -22.91883 | -48.67744 | 2025-11-21 05:08:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2ba9eaf-352b-380f-9642-c1f9799742ae | -18.10596 | -54.51788 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 33eae249-6c3f-33f9-b847-e8f3245269c4 | -22.19714 | -56.81335 | 2025-11-21 05:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b594b58a-0e41-385d-a209-1c4a2a486b87 | -18.1102 | -54.52588 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5bd71d2-923a-3d86-bcbd-92cda19572e7 | -17.61066 | -52.99931 | 2025-11-21 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1ff97cb-3fda-3ffc-bada-7834ee4ca4a8 | -20.3218 | -53.98727 | 2025-11-21 05:08:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f18addb-ba7e-377e-a1e4-8944ac6b57f7 | -18.10647 | -54.52531 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b83c97a-fea4-358e-b448-ce25fedf510b | -18.10159 | -54.52194 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5dda2331-a93d-34c2-a413-295028e6d589 | -20.49452 | -55.19474 | 2025-11-21 05:08:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 462c0b1c-edc6-3dfb-9a8f-22726c75215a | -17.61114 | -52.99557 | 2025-11-21 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 256bdf24-526b-39c7-97a3-a130be791458 | -17.66486 | -54.21852 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed5f88a-6045-3d13-84e9-fa6b5a983649 | -16.2268 | -59.52574 | 2025-11-21 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c5952f2-02c4-3b46-8fd5-f300227fd4cd | -17.62527 | -54.19787 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92b80a46-fe44-3419-a31f-b0dba3c81f39 | -18.76242 | -45.28783 | 2025-11-21 05:08:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a08079c9-1e2d-3feb-a27b-f43a5bde6e3e | -19.49791 | -55.34995 | 2025-11-21 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7a04677f-41ba-3c75-9832-c500c35db723 | -21.15324 | -48.59776 | 2025-11-21 05:08:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bee65e39-d4d7-30b5-bda2-999cb7c12c30 | -17.66864 | -54.21901 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50fa68dc-7346-3ce3-acb1-28b2d51c0b97 | -18.10398 | -54.51542 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c25475aa-6f80-3abb-9809-5403fe323f51 | -20.90519 | -56.32364 | 2025-11-21 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a697798-e16d-3f67-a9d3-ae0c5922b3ae | -16.26449 | -60.15133 | 2025-11-21 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89421352-4590-3f36-ac8c-541aa44f61f9 | -22.91948 | -48.68288 | 2025-11-21 05:08:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81476c5c-d439-3d4c-a4c1-572e8028d018 | -20.88891 | -52.35102 | 2025-11-21 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 364ad5f1-902c-312c-aeb1-2ba999405a45 | -20.88447 | -52.3505 | 2025-11-21 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b3be052-bcfd-391c-b759-39ac2858291a | -18.11143 | -54.51664 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df645cdb-8d62-353d-a8a3-62fda97d6c16 | -19.12233 | -54.45407 | 2025-11-21 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e5f401c-9af3-31d1-8270-c8365b4dc7fe | -17.62464 | -54.20259 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4358e475-a20b-3b31-a656-095e77ec766f | -17.61522 | -54.1865 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae927226-bc0c-3d7f-97a2-ccbf97a9a54e | -22.19225 | -53.97435 | 2025-11-21 05:08:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8df797e5-0a10-3f7c-be20-641fea3def2b | -21.04231 | -48.56007 | 2025-11-21 05:08:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bcee5578-f502-3a3b-a48c-bd8120d1b000 | -21.0427 | -48.55606 | 2025-11-21 05:08:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ec9b995e-8e5d-39a7-ada3-846b44a5a9e8 | -19.50154 | -55.35051 | 2025-11-21 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 63c9e694-c641-3c4e-94d6-72f76402c1a9 | -19.12299 | -54.44912 | 2025-11-21 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03f780dd-b69b-3be3-87d4-95002d6f689c | -19.00268 | -57.62278 | 2025-11-21 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 28af8a2d-04f9-3325-a87f-3d82659682a8 | -16.23083 | -59.33163 | 2025-11-21 05:08:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4fa7c9c-2028-358d-a614-9fc98e9b700d | -21.04544 | -48.55549 | 2025-11-21 05:08:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa189248-5b04-314e-aea2-c6a5817b8704 | -19.5036 | -55.35775 | 2025-11-21 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ea2ef432-e64e-3b09-a47c-8a8264ccfc8f | -20.38111 | -56.27668 | 2025-11-21 05:08:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 608e3d45-d759-3624-84c3-182b3e7cd876 | -18.10274 | -54.52473 | 2025-11-21 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 424e20ea-6ef4-3d52-ae02-5a03774821e4 | -19.49695 | -55.3522 | 2025-11-21 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6e00f72d-5841-33b6-90bc-99d49de228fb | -19.50398 | -55.35995 | 2025-11-21 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4cf433e4-c673-3f18-99bb-780f9c721577 | -17.61926 | -52.99673 | 2025-11-21 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cdada5-1784-3341-9509-a8661c8ff42f | -22.91983 | -48.67864 | 2025-11-21 05:08:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8dabbe48-ccab-3d58-8f6c-fa015e9ee530 | -17.61899 | -54.18719 | 2025-11-21 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 635e7c28-b199-3fa0-b1f7-cfbc5ec3e0bb | -22.92459 | -48.67787 | 2025-11-21 05:08:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46d190dc-fbb2-32ee-8fdc-9df4db13c3cb | 3.24787 | -60.43769 | 2025-11-21 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39f142d1-1ae8-3236-89a8-9f650cfc54ca | 3.48793 | -61.0884 | 2025-11-21 05:29:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 42070725-acad-3043-bb29-6d0130c303d3 | -12.88877 | -54.75829 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5b89e5-4556-3fe4-841b-caadf2a6520b | -9.54195 | -63.50466 | 2025-11-21 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a4f8826-5a35-37b4-ac08-29a3dff63a73 | -9.49749 | -63.50466 | 2025-11-21 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71dbbdb2-0e82-3667-ab0f-4b620bcc2668 | -12.8695 | -54.7432 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92396798-08fc-313f-8551-ad845b954abd | -11.99128 | -63.25243 | 2025-11-21 05:33:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d3af733-2962-3b1d-afea-eb18709e7669 | -9.62839 | -64.74708 | 2025-11-21 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66740ecf-f5dd-3bad-9705-c19850881176 | -9.82013 | -63.2467 | 2025-11-21 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e0a5b90-388c-3ec3-b152-f7705905d42b | -9.6959 | -65.71642 | 2025-11-21 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39c8d62-ec87-3d69-9eeb-4c25ede28353 | -10.83853 | -56.95922 | 2025-11-21 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e614f0a2-b760-34cd-ae9a-5f29e4509e50 | -12.87504 | -54.74034 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a9867d-4d31-3ffe-9107-597e39fec4b2 | -9.99293 | -65.1879 | 2025-11-21 05:33:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35cef307-4154-39fd-8b87-086521084ca9 | -8.71001 | -66.66076 | 2025-11-21 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3e5b245-23f1-3d71-9ace-e9b3ee0b0ad3 | -8.55431 | -63.11501 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e28322b-6a8d-397a-b87a-802f44dd223d | -12.87471 | -54.74394 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc361a8-8e9a-384a-915a-e98dce3e2b84 | -9.27488 | -64.23534 | 2025-11-21 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b87c4827-7de3-3465-8fd9-c1cb041e85ab | -9.03259 | -63.65783 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54f8b87a-dd10-35fe-8834-359e4c36ac06 | -12.86983 | -54.7396 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d11eefc-3968-3fa7-8edb-c9cb3416c9b9 | -12.5491 | -54.80076 | 2025-11-21 05:33:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| deae00ed-0030-3eba-ba8e-c787619e1645 | -9.57215 | -65.17603 | 2025-11-21 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
