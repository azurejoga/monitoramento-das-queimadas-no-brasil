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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12802f6d-cabf-31ff-a4ac-7ed10f194354 | -5.08635 | -43.79798 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4266d14d-b722-367d-8d5f-09d0063f2f25 | -4.84682 | -43.35376 | 2024-10-10 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93280a84-291a-374a-82be-2c16e94172c3 | -4.81747 | -44.35283 | 2024-10-10 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc6f65bd-38ca-3787-9420-2b1d3fdef059 | -4.65675 | -43.76925 | 2024-10-10 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 763750f1-4677-3902-ac9b-c8c4aba4f7b3 | -5.99919 | -43.48613 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8bb91035-e467-31cd-a87c-a6eb51b41eef | -5.99858 | -43.4898 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 85590dac-5704-3a87-a5e5-e90af9dc0f22 | -5.99797 | -43.49346 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 944588c1-c835-38bc-8c6e-e37923afc99d | -5.99575 | -43.48173 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b436b2c4-1676-3072-843e-bab5df14a019 | -5.99514 | -43.48538 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e25c9109-c861-3612-a2e7-fcbe5bc0ebf6 | -5.99452 | -43.48906 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95072a36-fae0-3586-b1f5-1111b4a3aa1c | -5.9939 | -43.49277 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a9083da-1be8-3759-816f-42134b563235 | -5.99168 | -43.48106 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ecf491b8-f019-37b5-a3bb-9af64f9a7db4 | -5.99107 | -43.48472 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c302c93-e04d-3e08-8ac4-24defb14ee97 | -5.98761 | -43.48041 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83d66cf8-65f9-38e5-91da-5eadb7363b9c | -5.98699 | -43.48408 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| abec1648-9f2f-39c6-9084-46515e5e80f5 | -5.56747 | -43.69754 | 2024-10-10 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e3165e6-8fea-3b9c-b973-a1a0cf7eef5c | -5.48505 | -43.93416 | 2024-10-10 03:55:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d8211c-fbec-3b37-be61-8fa70295e2c2 | -5.38719 | -43.62883 | 2024-10-10 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e60abd3d-e49c-3598-9664-64819a918850 | -5.38506 | -43.62902 | 2024-10-10 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e00bd732-270d-336e-ab84-b244f00ccf1f | -5.32261 | -43.73556 | 2024-10-10 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f434839-7e91-358e-8abe-28191bb34bfd | -5.23951 | -43.42874 | 2024-10-10 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6122aa10-0936-3073-be3a-33a2b6a6c238 | -5.2389 | -43.43244 | 2024-10-10 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b0e8127-337d-317a-af85-4ceb95fe7704 | -5.11094 | -43.75391 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c71f5f9-9b76-3dc5-a540-52c1ba619d37 | -5.7127 | -44.48946 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c35e8c2d-67d7-344d-977a-e63b0ee66e58 | -5.49495 | -44.28325 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6129c67-c5fd-3777-8401-8c99872d7ded | -5.49423 | -44.2874 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ab3288e-e2ad-32bd-812b-cf55cb0e4909 | -5.49315 | -44.53066 | 2024-10-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57472a44-01ad-3f74-bfc0-a0dd4e82dcbe | -5.49287 | -44.28418 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9334aaed-3847-3749-af73-fa918d2cfd2d | -5.49242 | -44.53497 | 2024-10-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc41148e-2018-3d21-96a4-372bd7163376 | -5.49219 | -44.28834 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb1f66b3-9c7c-33ed-a766-de3a1005769e | -5.49062 | -44.2825 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9b921d3-5664-32d8-8a01-f8253c0bf6f6 | -5.48991 | -44.28664 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a3159b3-a2db-30b0-b149-f972f039d403 | -5.48855 | -44.28343 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ccf4c65-c38a-3d4b-aa9a-650d19d4076a | -5.48803 | -44.5342 | 2024-10-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8baced1-9b49-3bf8-a0c1-91c7dec53c30 | -5.48354 | -44.28686 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 460d1039-c7c4-3f7f-8b6b-ba0812c5c86f | -5.47989 | -44.28201 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7e9197c-a779-396f-8b96-97d2479ffd2d | -5.47921 | -44.28615 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88b038ba-4b8e-3f79-9819-a492240ab4dc | -5.47487 | -44.28546 | 2024-10-10 03:55:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b52f69-40d8-323f-91da-8821549b6835 | -5.34264 | -44.08347 | 2024-10-10 03:55:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5df129de-3e7f-378b-b084-5d5c865429df | -5.27094 | -44.20653 | 2024-10-10 03:55:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bc45ab7a-cae6-36b6-aa7b-9abbb4ca7a98 | -5.26747 | -44.60859 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7150dc3c-9772-3b99-bc07-d265c0d67bac | -6.34888 | -43.81625 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 761ee69c-be98-3dd2-a945-9fdc7505daa5 | -6.34827 | -43.81987 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eb73cd9b-bf7e-3d6c-98f8-d3e6ee0133e6 | -6.34412 | -43.81925 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f0f8bb1-cb8e-3e89-94dc-eaf17d9c48b6 | -6.32983 | -43.76275 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d5677a8-4470-3a18-a91d-318c4d7b803a | -6.32572 | -43.76201 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23483ad9-20aa-3a96-830b-c1c5c604e1d4 | -6.32509 | -43.76581 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1197fe98-e16a-3fd5-b9f2-6d21a1f68fb9 | -6.28669 | -43.818 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 059427ed-9726-39fb-887c-2cbeb2a9c88e | -6.17109 | -43.70718 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf97a8e1-30b7-3b7e-92ab-7c285785a913 | -6.17047 | -43.71087 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f1f93bb9-0781-3c90-a43d-15382c396ca3 | -6.16697 | -43.70651 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 994dce44-c84f-3363-9d0c-f300a2653df5 | -6.16634 | -43.71023 | 2024-10-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd2dfc1b-e49f-3de9-92ba-9308d65a7466 | -5.9683 | -43.79756 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e81fb98-e3dc-3f16-a9ab-adbfaf575158 | -5.96414 | -43.79688 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fe9f772-50fb-35e2-9022-6cd1d1aaf589 | -5.89612 | -43.9711 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e5a084a-5d3d-3629-96d4-0df64d8a5b79 | -5.85286 | -43.73627 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b9c540b-c9e9-3421-99ec-d42144f073d6 | -5.85223 | -43.74001 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48d30024-f23a-31f7-9509-2b23e8be192e | -5.85161 | -43.74376 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 341ff3a9-c5a8-348d-abfe-a91a02ab5bdf | -5.84745 | -43.74309 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 910d6834-8579-31ba-9e36-20f5134bb099 | -5.84682 | -43.74687 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8920d8c-edce-39fa-b1c0-24b7505aa9bd | -5.80332 | -43.92868 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb3f24df-859b-3fc0-a82b-33c780f66e22 | -5.79998 | -43.94837 | 2024-10-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15e127aa-4cc0-3497-8f62-e69f5f2752a0 | -6.36115 | -44.56138 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3e2af0a5-eb7c-3ccc-892f-f0fde01e24f3 | -6.28819 | -44.5618 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5936b5b6-0e74-3f36-b408-31912066e384 | -6.28746 | -44.5662 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5324fa7-2ad7-3089-86ee-09cdc3d605ce | -6.26399 | -44.96882 | 2024-10-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ee65372-2394-3867-91e3-88b83d947076 | -6.26177 | -44.17479 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff347c9e-5b69-382c-956e-25b5ecbb7ade | -6.26152 | -44.66714 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11b3a424-0c98-39a5-9169-754fd1344068 | -6.26109 | -44.17889 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8c5d006-8656-3dff-abee-42cf86481f1b | -6.25953 | -44.78692 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d31759cc-f3b6-3c75-bb38-41d4af84e96c | -6.25363 | -44.79498 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7ab89ae-a26c-30b9-a5eb-d8676fcbad57 | -6.21742 | -44.20509 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c14ea7e4-735b-3dd4-8738-8614e607aeda | -6.21656 | -44.10689 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5fe23c72-da3d-3c2c-ab66-bd56fefdc32f | -6.21235 | -44.1061 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5763e072-546d-3cf9-9144-66c9a8eb8799 | -6.20813 | -44.1054 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c42cb9a-a556-3f31-a65a-71fc060a451f | -6.20747 | -44.10926 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acd7ea31-746b-3558-8690-3cb9d89e759f | -6.2039 | -44.10473 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 747b0aea-5715-3ad9-9614-b51a12230148 | -6.19458 | -45.0365 | 2024-10-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fc98800-bd16-3465-bde6-33755d3a87e8 | -6.19217 | -44.38124 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd4009a5-b647-3b1b-8583-33b17af5537e | -6.19151 | -44.38516 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| effcabac-88d9-3b9e-8fe2-e20501453b1f | -6.19006 | -45.03582 | 2024-10-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 167bdaa3-6537-3ea9-8e21-198405338ae1 | -6.18786 | -44.3805 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 433f6376-d140-308c-90c4-a81b44f7a954 | -6.1872 | -44.38444 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 974a99a7-9bed-327f-8d2a-24aebbaddd6d | -6.18051 | -44.45049 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f028d14f-d644-3112-a8cf-505d414f4617 | -6.07606 | -44.64005 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54bcf432-11b7-36a4-a5d9-215df7dcd808 | -6.07533 | -44.64444 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4f71881-8aa5-3bab-9c77-1debbec71f1e | -6.07094 | -44.64368 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c9727a4-52a1-3da7-94f3-72cdf5d77fbb | -6.07022 | -44.64803 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76ebe51e-e35d-336b-9595-c710410c7279 | -6.06655 | -44.64291 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc240975-2ea9-3ab4-ba72-bdccc948e37c | -6.06583 | -44.64728 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81b20c1b-3cb7-33a9-9137-d10757b22825 | -6.06526 | -44.70507 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fe05648-faec-3d26-9c8b-247198cb60a2 | -6.03951 | -44.23268 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56f82abb-a062-3800-8c91-55a42a375b64 | -5.95414 | -44.58574 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df613640-5b82-3a80-9f0d-d9de313c6ade | -5.95099 | -44.74054 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b237c939-1d97-3edf-8d9d-48850c99e1c0 | -5.94975 | -44.58506 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8327328a-5a26-3f75-a567-6896fb4464cd | -5.94904 | -44.58931 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6e7e54c-6b00-392d-a25c-d52f099d91f2 | -5.94654 | -44.73989 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 979015da-9145-3244-b904-268315f40241 | -5.93076 | -44.53753 | 2024-10-10 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f20f09a-8e3d-3389-8fcb-6ad43a961995 | -5.91477 | -44.63181 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5d7a0c6-3d28-3d72-a0c2-590592b1dd24 | -5.70469 | -44.77934 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README45.md)
