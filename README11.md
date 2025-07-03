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
| 76ddc7f0-369e-3302-9e08-74b2af4d52fa | -11.66201 | -44.59381 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| a234e608-9cfe-39c0-ba76-ce29c679cdb5 | -10.66475 | -49.44973 | 2025-07-03 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b95667a-4d01-30eb-9cb5-b93592934310 | -11.66042 | -44.58213 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34f8d1f0-dfd6-33bb-8c2f-488ece14ff28 | -12.11463 | -44.9876 | 2025-07-03 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c5f6759-cdb7-33da-9b04-5c5f1c1be7d9 | -14.15294 | -45.227 | 2025-07-03 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1b82bb6-8377-30c3-b404-81ea2daa48e6 | -11.50204 | -48.95998 | 2025-07-03 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8540c082-c90c-3cde-998b-88ed1e98702f | -19.71802 | -40.35296 | 2025-07-03 04:10:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3d0d2584-4820-30df-b198-a73d431757ba | -17.86411 | -44.5679 | 2025-07-03 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 678ca375-d1c2-3949-b6f8-959023561e35 | -11.65123 | -44.59584 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 29efd460-efa6-36f6-b02a-37071ea6d3d6 | -13.75206 | -49.55664 | 2025-07-03 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8db59110-e61d-3e5f-a36f-567cbc882989 | -13.39016 | -47.8435 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 05817b59-13ea-3c38-9684-3c7f40c2ac32 | -16.29085 | -49.95105 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8f27966-697d-378d-a9a6-f5a342f0ed29 | -12.76443 | -44.40643 | 2025-07-03 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52f1b7f4-e4f4-3cc3-91da-f901d919572b | -11.84375 | -43.80083 | 2025-07-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8fe9aa8-b32c-34b5-af7d-6c2eaa2bbcc6 | -11.54845 | -47.31376 | 2025-07-03 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 631e0e0c-d5db-3524-8eff-e692e74ae1ed | -15.35717 | -49.23199 | 2025-07-03 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97954851-e955-36b2-b96f-765790b7ac1d | -14.11904 | -41.67672 | 2025-07-03 04:10:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 135ee297-5d88-3e55-9980-47b4847f1713 | -16.09255 | -46.75574 | 2025-07-03 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f935c591-b26f-323f-aeba-9f0eaf082529 | -16.30073 | -49.94477 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9f1be06a-e8a4-3aad-822a-1b3b85195836 | -13.43414 | -47.8201 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 476d5402-5211-3bbe-94eb-d662a6f75c48 | -14.89946 | -41.98413 | 2025-07-03 04:10:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c8b43b0-abe3-34e0-b053-0e9128d56f18 | -18.90322 | -39.90764 | 2025-07-03 04:10:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3172c8cc-0d4b-3ea2-9e97-30d7fa682191 | -12.57473 | -48.88304 | 2025-07-03 04:10:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c266c5b-5c89-3d96-903b-1815c3fa5007 | -11.478 | -47.92666 | 2025-07-03 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05dd6fd1-dca1-3365-80af-f3a9433f516c | -10.79165 | -48.28034 | 2025-07-03 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d1c12be-382f-3ba0-9b33-970c5d53a970 | -11.63543 | -48.07713 | 2025-07-03 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0ce2b5ca-4bb0-3306-bd59-f80cbf788a40 | -19.71943 | -40.35191 | 2025-07-03 04:10:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0108b4df-2cf8-3555-b82a-406228f4803a | -12.11121 | -44.98698 | 2025-07-03 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f93370db-7e88-3a94-b0b7-e82dcc7e1a34 | -18.90393 | -39.90986 | 2025-07-03 04:10:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4d0d3e15-3ad6-3202-b03f-65e5643daa4a | -11.5028 | -48.95582 | 2025-07-03 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9cae50b2-e3ba-362b-87ec-16e2c2fd69e4 | -15.62229 | -46.46204 | 2025-07-03 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a146966b-9993-3b1c-a44c-ade8008c9128 | -12.10282 | -44.73449 | 2025-07-03 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b952d364-9759-38d2-a1e1-804bde3b3de9 | -17.65823 | -46.83068 | 2025-07-03 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f42c26e4-ece2-35aa-b9a5-a00da263cc5b | -12.16234 | -45.53215 | 2025-07-03 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79f16fa2-59b8-3d6f-9053-89819b1e9b49 | -13.44929 | -47.83155 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 267f0112-81e2-3eaa-83da-f59b6ba279c3 | -17.67768 | -42.742 | 2025-07-03 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7264a9f-2311-3212-9776-cf8dd097f519 | -17.63419 | -42.12775 | 2025-07-03 04:10:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0b567b6-cb7b-3186-a1b3-5de7b597a88d | -10.94417 | -48.29994 | 2025-07-03 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bb164b6-377d-33eb-b354-bb153b251943 | -11.65402 | -44.60011 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f3833bda-7cd6-312b-a43b-6086da37d964 | -11.77609 | -44.90803 | 2025-07-03 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d98f253b-653a-38c9-8921-c030da6509f2 | -10.70822 | -49.67828 | 2025-07-03 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0331a9b-b131-3406-8a67-cc9aab989da2 | -12.16584 | -45.53272 | 2025-07-03 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e620648-5162-383b-96ab-a409c66c1b65 | -12.56916 | -48.89003 | 2025-07-03 04:10:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4817ba0f-f4f3-3546-bfa7-e3f2dd4a31bf | -17.65405 | -46.83409 | 2025-07-03 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80e38975-6539-317d-8957-7ec34247253e | -14.63978 | -53.89301 | 2025-07-03 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2832cc7c-38c7-30a3-99cd-be65eb817bb8 | -13.65473 | -46.81044 | 2025-07-03 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee58d866-fd3f-385c-aec6-4fd4521a1cdc | -16.29999 | -49.94878 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| fc1093fe-ef82-3838-bf1e-f5a5aa258889 | -11.84708 | -43.80138 | 2025-07-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d22767ff-dcd0-3f80-8877-d860fdd7efaa | -11.6614 | -44.59752 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 5ffbc3a7-6c04-31e5-9541-0cb5576e0789 | -13.65398 | -46.81481 | 2025-07-03 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c2c4978-8a52-3ebc-82de-deb2b691ad19 | -11.65741 | -44.60067 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 27f5ac94-8012-3629-929c-d0df0b25eddf | -15.35308 | -49.23119 | 2025-07-03 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80ae92cc-aa72-3101-9fc4-906094339c94 | -17.65475 | -46.83005 | 2025-07-03 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d8af188-b373-3dca-8ebc-583b993b011b | -12.41056 | -49.6762 | 2025-07-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1e242fb-d662-30fa-a4ed-904e73a3546e | -10.92764 | -49.27575 | 2025-07-03 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 961a0211-65c9-3a76-9ee8-1c8bf7321308 | -12.01761 | -47.77758 | 2025-07-03 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 70f00932-d0e2-3495-aba2-df0196645fe2 | -11.79374 | -48.08387 | 2025-07-03 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d80d459-eab7-301f-96b6-14d3484cd6a8 | -11.50037 | -48.95546 | 2025-07-03 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d145431-069e-36ee-83f4-3d538e6ceb19 | -11.53771 | -47.30674 | 2025-07-03 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75a58d51-8697-3698-a0d8-7badaec7c9f8 | -11.666 | -44.59067 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d705e9c-d922-39c0-9e60-9e204a44edb6 | -17.78327 | -42.80848 | 2025-07-03 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dccfad2-fbb9-3d0f-b633-a21208ada6df | -16.29159 | -49.94701 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 713fe508-3ea9-37a4-b685-b0a16689ef1c | -18.05948 | -44.49398 | 2025-07-03 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83adf8e5-0c23-37c4-a431-6c979069bbfd | -11.11355 | -48.87109 | 2025-07-03 04:10:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42c185fe-715a-3d77-9ddb-c988fb176667 | -12.57404 | -48.88695 | 2025-07-03 04:10:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be43d8d3-ff13-3736-bd41-3b7660b01ece | -13.39401 | -47.84433 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2042e226-6473-3144-9ea9-861b00e41503 | -11.47398 | -47.92597 | 2025-07-03 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0249d621-f2a1-337c-8e7a-d79623dd8cd6 | -13.95122 | -46.37249 | 2025-07-03 04:10:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55c702dc-235a-30a1-ab84-28f09b123d5e | -12.67926 | -45.03819 | 2025-07-03 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 750eb43c-8224-3087-ae1f-d7a1cad6a564 | -16.07651 | -51.56269 | 2025-07-03 04:10:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ecbc052-55b9-3258-a515-66186b44fc41 | -11.49964 | -48.95964 | 2025-07-03 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a44fa0c-3030-3f77-8194-b61f0729f7e2 | -18.67294 | -44.59499 | 2025-07-03 04:10:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca620b13-57fd-3735-b9c3-2d4032e86a66 | -13.43116 | -47.81422 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64462d40-0d9d-39cd-a15a-8fa92a362b27 | -10.66025 | -49.4489 | 2025-07-03 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52eb0fce-9666-3896-a229-5bae45fca33e | -15.83485 | -45.64552 | 2025-07-03 04:10:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfc0d807-14dc-31d4-b6af-9d564ca01d57 | -18.90711 | -39.90819 | 2025-07-03 04:10:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 79e875a8-f105-344e-a96b-b040dbee2192 | -14.88155 | -48.36233 | 2025-07-03 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e82c316-c2ba-3d93-ad81-542e16c6955c | -18.18302 | -45.12994 | 2025-07-03 04:10:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43bc387b-f25b-3183-9641-45527f13733d | -11.65462 | -44.5964 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c918c64f-ba47-351f-a100-df3e8b8222b3 | -14.63415 | -53.89199 | 2025-07-03 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc3afc96-226c-3b54-b293-964499846482 | -11.65424 | -44.57729 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b61a8f47-297b-34f5-8818-9ab6d6393b85 | -14.9975 | -48.32464 | 2025-07-03 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef9d85ed-df6c-3ae7-914f-85281c7e7bfd | -15.31326 | -45.99072 | 2025-07-03 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3af84b13-aa16-32b0-a8f1-803d51c839a3 | -14.88061 | -48.36752 | 2025-07-03 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 832ea4c9-87b0-3684-ab5d-30fdcdc5d8af | -10.68508 | -49.49159 | 2025-07-03 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40b99c29-0bcd-3958-a888-8b0814927d9b | -11.6654 | -44.59438 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76542c7e-fc35-3404-a080-802cb5012f87 | -11.85612 | -44.84805 | 2025-07-03 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 35237b94-ea08-369a-8c49-f0d597cdb610 | -13.94697 | -46.37595 | 2025-07-03 04:10:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f204868-9389-370c-95c4-2fc792b70ed9 | -12.4325 | -50.0244 | 2025-07-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f831b1ad-2002-3c48-8c4e-2f015c56d2af | -12.57054 | -48.88227 | 2025-07-03 04:10:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 488ca618-13c5-3a91-99fa-d8863613f51c | -13.43579 | -47.81781 | 2025-07-03 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e6943e9-6bf4-30b2-a08a-dc8c8fd17057 | -11.79842 | -48.08094 | 2025-07-03 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 416ca66e-5e54-314b-90ac-2dfe9ce9d899 | -11.65085 | -44.57673 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26d03847-35cf-321b-8cab-bf718d838d9b | -17.66296 | -42.26832 | 2025-07-03 04:10:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca514f32-2182-31a3-bc70-68686d156e3b | -17.7799 | -42.80793 | 2025-07-03 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| addd7dc8-a9c7-38e6-9ab1-50c89e350643 | -11.84432 | -43.79728 | 2025-07-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfed2f1b-f549-3a72-8dd8-5e447da1b9dd | -15.31391 | -45.98684 | 2025-07-03 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa6ef05f-12a1-3389-924d-bd40a4e341f2 | -15.74241 | -41.15141 | 2025-07-03 04:10:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 848511b0-635b-3222-9f9a-228b1d7a281e | -13.24359 | -42.55312 | 2025-07-03 04:10:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| afce6936-84ac-3426-8072-982506f9b620 | -11.54074 | -47.31234 | 2025-07-03 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README12.md)
