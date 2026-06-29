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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e921b82a-6b0c-3a21-a896-6700c16d7312 | -9.32324 | -58.03499 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b470f0-1143-3d6b-8aaa-d36ea2ac425e | -9.08623 | -59.39901 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9275f1-026e-36fd-ac8c-eed6803f9332 | -9.09068 | -59.41634 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 517e6c38-8b18-3b6c-ada2-917a790380ae | -12.23359 | -56.5577 | 2026-06-29 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3af348c-a5a6-3a1f-ba5a-8985f8f10745 | -12.54772 | -57.18362 | 2026-06-29 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e76baa22-517b-3345-a72f-c2b4992d0695 | -10.31567 | -50.1812 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a64a930b-c1d9-3856-a021-aec2fdb6e196 | -9.9554 | -52.19978 | 2026-06-29 05:16:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f80d1d5-5931-3ad4-8396-da47e36b2fb9 | -9.09045 | -59.3956 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ba354cd-f499-38fa-9889-607670c5de61 | -9.31765 | -58.02662 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3827cd07-f2e2-32ae-9cf1-124e4e545d03 | -13.712 | -47.84892 | 2026-06-29 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42eb2451-fa90-3a20-976d-e0a89047aeb8 | -11.88755 | -57.14495 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 785778a3-3cdb-3806-b7a0-6bce3167e5c7 | -11.22234 | -54.3083 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0509aa87-55be-3a91-b615-5e914beae68e | -11.52656 | -54.79615 | 2026-06-29 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7df2b80b-f567-30e4-93a9-1978fc460c73 | -11.92105 | -57.40732 | 2026-06-29 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5df0f23-4d57-388c-a4cf-946ed818a389 | -10.33152 | -50.17134 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1550eee-a856-32a6-89a9-87a099b414d4 | -9.32954 | -58.01742 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 489acca6-c99b-3208-ae9c-b7dab27df9bc | -9.32617 | -58.01687 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9919789-b842-3285-afac-3772247fd0a6 | -9.08934 | -59.42445 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05f9274b-b8e2-32e3-936f-9cc6ef270cfd | -10.31502 | -50.18578 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2716bd5-4640-3bfd-8bf7-13a10240faaa | -9.08712 | -59.41575 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9612ae-66d6-33e3-8297-6210d46ba83e | -9.32662 | -58.03555 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62b503cb-03ea-3e2c-9fb8-9ea4a69e82cd | -9.32837 | -58.02466 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e93bc23-2a11-30b4-be0b-51074d41ad89 | -11.88259 | -57.11157 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 669bca4c-eb53-3ced-bdef-1cd88ca15056 | -13.70618 | -47.85028 | 2026-06-29 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06673ae8-e296-3792-8b1d-efd57380b5ed | -11.88369 | -57.12623 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2580e050-971a-3759-bbac-2307c2c1edfa | -13.85751 | -44.75138 | 2026-06-29 05:16:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 552498b7-4709-3a88-9a84-b763b2550813 | -9.08822 | -59.38696 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d346e38-6ac5-3e72-bbce-db426fd3615e | -12.10447 | -51.99055 | 2026-06-29 05:16:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8efb169a-3544-330d-829a-19d624dcaf48 | -11.73349 | -59.35741 | 2026-06-29 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12b01f66-4ea7-32ae-bcda-df54fa649ed7 | -11.90142 | -57.14359 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7473973-b166-301f-bda8-6743e03165ec | -13.71039 | -47.86193 | 2026-06-29 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 458cbad1-adf1-3995-8ae8-cbcbd0ce60d3 | -9.08756 | -59.39098 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 487737fb-e7cd-3fb3-82f4-bb85650a4b51 | -11.88257 | -57.13328 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0354f603-9524-3af7-90f9-50ac3021ca27 | -11.89311 | -57.13138 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2476089a-a3c2-332c-957b-5c85c16549d4 | -9.08689 | -59.39499 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d3a0112-eed8-340e-b181-c35aae7feabe | -11.88867 | -57.13789 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5db513fa-654e-3d7f-a15e-5f4966d0731b | -12.46001 | -58.494 | 2026-06-29 05:16:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6106e024-732e-3de3-98d3-36df876ec136 | -9.60225 | -56.92649 | 2026-06-29 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a08b565-7a7d-3277-9d0a-a5c7b1a69186 | -11.49818 | -54.50404 | 2026-06-29 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54a05da0-8082-32ef-b3e4-210dc5da281a | -11.89366 | -57.12785 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed7ecb57-ec35-3352-aecc-1b7a9a500dc5 | -11.91085 | -57.12703 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| babc7242-d78d-3811-a1a2-d993c4ca7bb3 | -14.63759 | -54.53022 | 2026-06-29 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 135a8b45-1fdf-39b0-9fbd-9bbb875f3774 | -11.21733 | -53.82112 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fc0446a0-0ca4-347f-8ce4-d4a179bc77f5 | -11.4994 | -54.49599 | 2026-06-29 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e865895-e4d7-30c7-9b29-4cfdee624e12 | -11.89144 | -57.14196 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54875d55-e06c-32c8-9da6-7eeb863e7d2b | -10.21365 | -46.50549 | 2026-06-29 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e135353-c8f2-3aab-b2be-5d5b35d7d84f | -10.5133 | -51.94021 | 2026-06-29 05:16:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 732cb3ca-a247-3276-a22f-2be62a0911fc | -12.28688 | -57.5504 | 2026-06-29 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a9ad971-fbae-3b40-ada2-a436c5234efb | -11.52015 | -54.79114 | 2026-06-29 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6d6d756-4404-3c27-a421-3505f09cf251 | -11.21368 | -53.82055 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 52acc4cc-5197-3452-b121-167a14296568 | -10.50594 | -53.57586 | 2026-06-29 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 698bb614-e22f-3a04-820e-716e6d2b5994 | -9.32896 | -58.02105 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb07d386-f86c-3d8f-b84b-fc65f546fdee | -11.22275 | -53.83504 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d665bb-29b0-347a-afc1-fa4cbd7c2166 | -9.58157 | -60.64623 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d03278-834b-360f-a386-2df4572d7893 | -13.93901 | -53.93678 | 2026-06-29 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f7f178b-ce16-3f50-b01d-dc6790073b21 | -11.89088 | -57.14549 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b230311a-0df7-3ecf-a96c-da6c136441ac | -11.06528 | -55.76558 | 2026-06-29 05:16:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f70da76-6eb8-35dc-9b4f-021dafbf24db | -11.91772 | -57.40678 | 2026-06-29 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1033a1d-268e-3c82-befd-80bae8b2783f | -11.52365 | -54.79168 | 2026-06-29 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dae4916a-4e5c-30ef-96fc-fb37012be8f4 | -9.32279 | -58.01631 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab87c4af-c7ac-3426-a42d-b01699d2afbb | -11.52074 | -54.7872 | 2026-06-29 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3f0cbfd-4d68-3fa5-af22-de2cc4a1eea1 | -11.88588 | -55.13849 | 2026-06-29 05:16:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ce4a2a-5387-39f4-a990-6889b77ef8c9 | -11.88701 | -57.12677 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee058ae2-3dbc-3abf-9545-8a68bfaf473f | -11.49525 | -54.49948 | 2026-06-29 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4904600-046d-36db-88bf-15f2b7ab07fa | -10.32122 | -50.17924 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a04109f1-4664-3355-a511-0d6540cbffc1 | -9.08134 | -59.40648 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bf6394f-9281-346a-b650-183f68d4d546 | -11.89089 | -57.12378 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 518ae7a4-6146-3a5d-b6db-1b79da7fd512 | -10.39335 | -56.75977 | 2026-06-29 05:16:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0937739f-952d-3ae8-adef-8ae8fe4e27d8 | -10.29728 | -57.129 | 2026-06-29 05:16:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80f194f8-7bcd-305e-ac82-4a533fff9289 | -11.88813 | -57.11971 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea6df2c3-01d9-3859-b329-08f02b4578ec | -9.08645 | -59.4198 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba03c4c7-f28b-3092-bcb5-667f0599b455 | -11.88811 | -57.14142 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3220326b-ae80-3bb7-bcba-fe5a79b9a865 | -9.08334 | -59.3944 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a2044d2-a131-34ff-bd11-b5c9a763dd0b | -9.08467 | -59.38636 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37cddcad-4093-3e25-8898-50640243bbc0 | -13.85993 | -44.75189 | 2026-06-29 05:16:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d182f635-3a46-3cb3-9007-2c8c8df09b6d | -11.90753 | -57.12649 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4665aa77-7830-3e62-8c67-85dd88ddfa77 | -9.24969 | -57.77513 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d388fc0-6ee4-3ba4-9299-31df4b6d26bd | -11.2194 | -54.30368 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 634c7f0b-ac46-31ab-81fe-f46c27dbb765 | -11.21305 | -53.82485 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b93bde7-ca8e-3896-9df6-bcd0508dc2b7 | -9.3272 | -58.03192 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0502e0f6-6f17-365c-bce6-79e99e8bc168 | -9.08845 | -59.40766 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb658dad-58bc-3bc5-b6dd-015febfdf773 | -11.89034 | -57.12731 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f191383a-36ec-32dd-b4aa-56b3c195f3f3 | -10.77286 | -54.11102 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e069ef3c-c6f1-3496-983c-c01fc0d5ac71 | -11.89476 | -57.1425 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30835b3a-364f-33ae-a997-52f55f59f2e5 | -9.33175 | -58.02523 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d0867ae-63ee-38af-8544-b0c38b496dc8 | -10.77347 | -54.10692 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c3f81c6-9144-3d65-8fe0-3c5b217c4dd1 | -11.88424 | -57.1227 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6da6675-8587-3c16-839e-7c460e9ba08b | -11.06866 | -55.76612 | 2026-06-29 05:16:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d53b8baf-4386-3817-ba64-cba3775a88ad | -9.32675 | -58.01324 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f4663c-0ed5-3074-8b77-4873b4719345 | -9.32103 | -58.02718 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48276055-ffa5-33fe-b08a-9f88e26a08fc | -10.31999 | -50.18844 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 806c0296-8aff-3cac-8bb2-388afc7e14fd | -9.14462 | -50.91158 | 2026-06-29 05:16:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 369e1e6c-00d6-364c-a234-677f02c24b16 | -11.88534 | -57.13735 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd79a492-f96b-3af8-a6e4-cb1899a989f4 | -10.97643 | -49.56253 | 2026-06-29 05:16:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c552d9bd-4ffb-37da-a335-2f68230b9666 | -11.88591 | -57.11211 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e93ca3c0-bd90-354f-928e-cf9620c9eba2 | -9.33058 | -58.03248 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8544c3ec-52e0-3ed0-85de-2bb2fcde8552 | -12.52389 | -48.29449 | 2026-06-29 05:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15f087f7-096a-3a21-9b51-0d04b0c8158c | -9.0849 | -59.40707 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f67c447c-6543-31ff-9649-e6587252571f | -9.11598 | -58.25621 | 2026-06-29 05:16:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a2c5e24-1fec-3450-8d97-b0a6f3f281a6 | -13.70568 | -47.85436 | 2026-06-29 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
