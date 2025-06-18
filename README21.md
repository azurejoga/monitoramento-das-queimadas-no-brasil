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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c314cb95-0536-3e3b-8a6f-6ab43c698b26 | -12.58064 | -56.9896 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dc7b514-c884-388e-b2a6-041fb6e57f56 | -13.77628 | -54.19431 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca653e30-849c-3e34-81e3-3b58fd57070d | -16.3138 | -58.2501 | 2025-06-18 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 97b2d85f-0d89-3910-ad9f-3d6c457cca97 | -12.53654 | -57.7195 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c9ec24f-44f3-3efb-9df7-db4e553e6336 | -12.57711 | -56.98464 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20437574-b1c9-3a44-8fd6-2093a9cd6d36 | -15.40244 | -47.83039 | 2025-06-18 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb5b63d9-c5d4-3a78-a508-7bb27bf5b887 | -14.06994 | -53.37901 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 31e2ee40-99f6-36ac-8ba9-cc3e6398b31f | -12.65112 | -54.12724 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52075c7a-8c5c-3221-b546-d1f6914f3c7b | -12.53399 | -57.72557 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 470ea55f-16f7-322a-b1b5-c6b9ad023bb6 | -11.9619 | -58.73 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3df69df9-e818-3116-82e7-a1629718c007 | -14.64714 | -48.05234 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a557c18-fb84-3c33-b38f-5a9de0b743a9 | -14.43654 | -48.90336 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81444e20-8e23-33f9-ad11-8b8e826e6d0b | -16.35608 | -54.55753 | 2025-06-18 04:40:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| beff298e-5346-3a84-84d7-dc0ec2629879 | -16.17553 | -44.12839 | 2025-06-18 04:40:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| affe7fa5-e824-3435-a969-a7fc26491f01 | -11.64778 | -54.13437 | 2025-06-18 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0aa2410f-6660-3dc6-9724-1ec715e8286f | -12.65405 | -54.11008 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a429cb14-fa29-3fbd-a729-e9036b6d049a | -10.93132 | -56.84273 | 2025-06-18 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0d43e71-19bb-3609-8675-5fe3b07fcf45 | -12.51163 | -58.35154 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb9757f3-d13b-3793-8e5d-6a543a292942 | -14.20293 | -45.50854 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39df2aa7-6a7f-33d6-a704-b5b6d9986d65 | -13.95996 | -56.79771 | 2025-06-18 04:40:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 944913a1-d9ff-3e33-a444-c04a8f31c5ec | -16.31297 | -58.25453 | 2025-06-18 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4665bd76-417a-3d64-b900-658bdd05ff34 | -13.36733 | -52.6617 | 2025-06-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c14c3ef-6f01-3aa0-87d2-dc32ca5378f0 | -12.34475 | -49.30557 | 2025-06-18 04:40:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc653bd3-359f-33f8-813c-e92e5313a5b5 | -10.27336 | -60.54741 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d59a4ea-b9b9-376b-a91e-844823c9c978 | -11.64338 | -54.13804 | 2025-06-18 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad66bc2e-e9f3-3d34-83c1-dd4d9982a8bb | -10.27263 | -60.55119 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6826e9fd-7c87-3e5a-a510-ab4bc65d0f43 | -11.88463 | -54.67409 | 2025-06-18 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c1a9b37-cac9-3f56-83cb-4661e481fdc0 | -15.62367 | -46.46466 | 2025-06-18 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c47991f5-a7f9-3aff-a21a-e93fc5b310f9 | -13.79756 | -54.29684 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eae2f90f-3c0d-3188-b480-1053c92f4c35 | -12.50877 | -58.35994 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 860968d1-b74e-3355-9020-51660cfe32c5 | -18.10957 | -54.27701 | 2025-06-18 04:40:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e01157c4-df53-3b09-bea9-25bf17a60665 | -20.41872 | -45.58362 | 2025-06-18 04:40:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd69fe9f-e14b-39f4-8b22-26dd4a910c8b | -15.41289 | -47.83646 | 2025-06-18 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b77f5908-0f84-3c57-b289-30c2d709c5e9 | -12.53481 | -57.721 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8924ea05-bc2d-3c00-8d6f-8218c65730f6 | -11.96573 | -58.7365 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0912d4b2-6dfa-3a6d-a6a8-c72e173b54ba | -11.91104 | -54.81368 | 2025-06-18 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 879a6425-8580-300d-bcda-1d2743be7176 | -12.50502 | -58.35384 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1b1ac7a-4acd-3dfe-b7cc-1d6953250ad9 | -12.27934 | -57.27389 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 389056d3-cb25-3884-a3cb-d8ff2303fb97 | -11.64263 | -54.14239 | 2025-06-18 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd712c87-6631-34dd-8569-63496f015a4a | -10.92618 | -56.84629 | 2025-06-18 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b7c0add7-2684-375f-9a39-23e1c38bfaac | -13.14511 | -56.80607 | 2025-06-18 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa5c71f5-6210-36bf-b34c-16a43c506c0a | -10.6591 | -59.29481 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4660a38-8007-352b-8c50-9d50ff7bd394 | -18.01 | -49.39411 | 2025-06-18 04:40:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea51490a-c8a9-362d-8a69-5d55053bfa9a | -12.42976 | -54.87049 | 2025-06-18 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcbdc0a6-00ed-3e8b-aae1-0763d4d0d168 | -16.65561 | -45.49554 | 2025-06-18 04:40:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56bbc417-0dea-3af5-92b9-b2acf0990ede | -12.6439 | -54.12592 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6b9a811-504e-3925-8c54-4c51ae90d5fa | -19.96188 | -47.20341 | 2025-06-18 04:40:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1097919b-a822-3f12-9f15-dd7d78efb40a | -12.5173 | -58.34733 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eac4f9b-9d9b-3405-b8f6-955cb4e13a00 | -12.50407 | -58.35902 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59890c83-a7ec-344f-bc05-2e007e68cd83 | -20.495 | -54.69218 | 2025-06-18 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b98d820e-b380-3f7a-84f4-8fa7123ba801 | -22.54101 | -48.81396 | 2025-06-18 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62bac312-c215-3f86-bc92-c1085dd52561 | -20.98849 | -47.39213 | 2025-06-18 04:42:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 559386dc-23bf-3ba7-b577-a2de2977bde9 | -21.37178 | -48.95924 | 2025-06-18 04:42:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c922b56f-acc8-3983-9755-47ec673118b1 | -20.99459 | -51.79237 | 2025-06-18 04:42:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5aaf8234-aac7-3b1d-9548-a1d16e42d279 | -20.75539 | -48.52566 | 2025-06-18 04:42:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 439b1465-22c5-3f0d-8599-f6d9a08eb535 | -21.42463 | -48.64498 | 2025-06-18 04:42:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aa300e7-0b6e-3dbe-bc4a-9709d02a0342 | -20.50255 | -45.58578 | 2025-06-18 04:42:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab24e674-22e6-3dde-aaa0-0ca46093c4b6 | -21.8617 | -49.7407 | 2025-06-18 04:42:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 81f6381c-572b-3d74-b4c5-b564ba5acfe7 | -21.64537 | -44.23118 | 2025-06-18 04:42:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 61daf7d0-7ee1-35c3-84db-863d526af9e9 | -20.98801 | -47.39595 | 2025-06-18 04:42:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d9e8aa7-a477-3ec0-a838-762de8f9171c | -21.35909 | -56.11905 | 2025-06-18 04:42:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6bbcb43-0252-3ed8-a7d9-c9781235eb77 | -19.58767 | -53.50126 | 2025-06-18 04:42:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12198442-1037-35c7-bbf9-f710ecf87bb8 | -21.19627 | -44.9373 | 2025-06-18 04:42:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a4dee7cb-1f51-3f6a-b548-069b9ac1aba4 | -22.7866 | -49.32058 | 2025-06-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 433aa577-ac45-328d-b4ca-5c140f4cbb3c | -22.53876 | -48.81178 | 2025-06-18 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 933e83a0-dc3a-365b-8c96-8f2d2b17eabe | -21.06717 | -46.21852 | 2025-06-18 04:42:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96b6a0c7-ea46-35e2-bdb3-c11035c89be9 | -23.33606 | -46.77213 | 2025-06-18 04:42:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c5c47ee-0d3d-36d3-829b-210f7195b25e | -19.58433 | -53.50067 | 2025-06-18 04:42:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30356d6f-841b-3ca0-9fcb-af67e631edd0 | -23.33699 | -46.77052 | 2025-06-18 04:42:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0174bb9f-c052-3745-b8b2-4ebe5486d939 | -20.92194 | -49.09716 | 2025-06-18 04:42:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ebad53a-ab47-37ce-b5ff-383cca912d51 | -21.95252 | -46.43164 | 2025-06-18 04:42:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68802894-08ea-3b7f-94a1-a4c469005956 | -20.54763 | -55.83624 | 2025-06-18 04:42:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85fb0947-b776-3e24-8bed-522269a31154 | -22.67492 | -42.85398 | 2025-06-18 04:42:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 77bf3787-201b-301b-a494-06bbbb2c2b2a | -21.58864 | -57.58725 | 2025-06-18 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47c615c3-b097-3cde-a593-825b20bbede1 | -20.47775 | -53.67535 | 2025-06-18 04:42:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580a91d1-68ff-3ec2-afb0-d2aeec502580 | -20.99662 | -47.39334 | 2025-06-18 04:42:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfa7ce4c-1bd9-3078-9d2a-fadad2a6a78c | -22.76043 | -47.69978 | 2025-06-18 04:42:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 665a14fb-3921-3e39-8f4e-559e90433f15 | -21.8653 | -49.74128 | 2025-06-18 04:42:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 238db0a7-b580-3eff-b551-6d7eade9fe77 | -22.77605 | -49.31415 | 2025-06-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3602eda1-5d2c-3e56-95cb-55e13679e41d | -21.37551 | -48.95984 | 2025-06-18 04:42:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f1623f1-eeb4-3f4e-8682-2f1f6e72b1f4 | -22.77541 | -49.31897 | 2025-06-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ec4e70-7874-3a76-8d0b-4e9c6d607cbd | -21.58991 | -57.58933 | 2025-06-18 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17e69f22-dcae-3f50-822f-84e5a0ac2cb6 | -23.40579 | -46.55496 | 2025-06-18 04:42:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d77843a2-ef64-343f-9aeb-4296e1097a4f | -22.67629 | -42.85059 | 2025-06-18 04:42:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6e6cf85c-ad90-3483-ad77-9e432b9040a6 | -20.99305 | -47.3889 | 2025-06-18 04:42:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27e5fd74-dcc7-3ecc-adc0-3376ab7edd5e | -22.31376 | -53.58747 | 2025-06-18 04:42:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 026f31fd-751c-373b-a868-9a4f64898e12 | -19.17276 | -57.54598 | 2025-06-18 04:42:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5d1eb3d0-9b55-3b4b-9d5b-f9120cd04235 | -23.59111 | -47.43821 | 2025-06-18 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 07ff3c90-c26f-3e5c-8355-ea8ae07eb894 | -19.17375 | -57.54064 | 2025-06-18 04:42:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f5116d82-a511-3aaf-929b-a0d85c2437f2 | -22.77913 | -49.31952 | 2025-06-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 45d62b0e-c71b-35cd-9a36-efa75bd70c37 | -20.98899 | -47.38827 | 2025-06-18 04:42:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05fd6b6f-22cb-39e6-8767-51f8ebd33005 | -22.67591 | -42.85454 | 2025-06-18 04:42:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 143e0061-0105-3301-b175-e5611c4fd828 | -22.78596 | -49.32532 | 2025-06-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79cc2885-df1c-3bd5-984e-4c5db7b9e69d | -22.78286 | -49.32005 | 2025-06-18 04:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1353f7aa-c129-39ac-96ca-e3a6bc3bb1c3 | -20.99256 | -47.39275 | 2025-06-18 04:42:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f33db04-794c-3bb6-8ce7-63f48bb5045f | -22.67527 | -42.85004 | 2025-06-18 04:42:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| bf92cb15-476f-313b-b66e-dc85d6e88c09 | -11.1379 | -53.9429 | 2025-06-18 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| b7b2d9a9-6f19-3f2b-a0c3-23d293c8cc57 | -11.1382 | -53.9223 | 2025-06-18 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 300a3731-0205-3086-ae13-4d04c600f07d | -11.1379 | -53.9429 | 2025-06-18 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 07ac0cb3-6e06-36ad-ba83-f1d402d2f861 | -11.1382 | -53.9223 | 2025-06-18 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |


[Clique aqui para ver as próximas entradas](README22.md)
