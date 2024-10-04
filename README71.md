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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d60036e3-323f-3d9e-840d-60806e832137 | -11.10993 | -46.49389 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 6eb9d845-2b9d-3ebc-b916-930ce3a569c7 | -11.10907 | -46.49877 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 92d3a156-484f-3886-9df7-41e1a52323d9 | -11.10831 | -46.49577 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 21fd13d3-a133-370d-b444-e052b997ce70 | -11.10537 | -46.49039 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c32d3f1b-dfda-33b1-82e1-d52a5612911d | -11.10456 | -46.49524 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 239bd734-7a9f-3349-9f1a-849a64eb2579 | -11.10164 | -46.48973 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9edae85-0533-3983-a4b6-06fd7c2fcbcb | -11.10083 | -46.49455 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0fe3a918-2351-3c1f-afd7-904ffc7cff89 | -11.09711 | -46.49383 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e77395a9-2f2f-3df9-8354-76a3821d5d86 | -11.09549 | -46.50347 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 2a844df0-45c6-35bf-9339-bf1a9279f30a | -11.09533 | -46.52733 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 865f1474-f02a-3147-bd2e-dd379323b84c | -11.09472 | -46.50807 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 1bb23a72-d2ca-32a6-88bc-96c73bf01b76 | -11.09339 | -46.49307 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db341266-4c3c-3149-ab26-dbb1fbeeaef2 | -11.0926 | -46.49777 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 052e3338-1bbd-32fb-920c-7a76eeac23d3 | -11.09242 | -46.52172 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3cfbcca0-1fd6-310e-b1ed-fa45f2aed756 | -11.09181 | -46.50248 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 16dd6872-3ebd-379b-b40b-4c7e4d9564a7 | -11.0916 | -46.52658 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 074db9d0-4594-3bf3-93e6-8087a38d4bba | -11.09103 | -46.50708 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 2cedaec6-59af-3e81-ae97-925ddd8fd56f | -11.08872 | -46.52085 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 272ff3eb-717b-3edb-a2af-1132a8f94d9c | -11.08788 | -46.5258 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1886edeb-3c8e-3c08-ab9a-fea236f78ac9 | -11.08706 | -46.53073 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| b059bec7-0620-3fb8-af12-63cdb1096d81 | -11.08627 | -46.53539 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fbdce29c-9ab8-3c2a-a480-ed912e951151 | -11.08497 | -46.52023 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e61de9d9-8e27-3ab4-afc6-ba6f8ea96d75 | -11.08413 | -46.5252 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fce1ff9-f0e2-34cc-a9a3-db2e6b05b10f | -11.08331 | -46.53009 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 006f2d41-443b-3fee-a91d-5c6cafd1385b | -11.08253 | -46.53474 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abd1522b-28b6-3e74-ad5b-c7fdd8e25046 | -11.08037 | -46.52466 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae7df1e1-26c3-3a72-9a51-a5397a3e0d59 | -11.07956 | -46.52946 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5cb9aae-2a00-3655-a446-fd63e33a8e9b | -11.06994 | -46.51804 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e7304a55-1556-30c8-bf0f-ac6f588cffd9 | -11.06378 | -46.5316 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 35f6d465-9579-3ceb-8322-c8bbe78b358e | -10.92881 | -46.63862 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b70055b1-a20c-3302-88be-00c768ae3f0c | -10.91395 | -46.61197 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e6ffefdb-0a56-38c9-967f-9b4ac0ef5e52 | -10.91017 | -46.61132 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47eab1af-237a-3af1-a768-42048791254d | -10.90937 | -46.61601 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 405a42b5-bba1-3f17-ad6d-852c1a6e2ec7 | -10.89561 | -46.62821 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34b9cf04-cbb4-30c7-af2b-6229a127011b | -15.61502 | -47.19851 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 66cca788-5788-30c2-b89d-8f12d8bd7235 | -10.89265 | -46.62284 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a818e2c3-e0ef-38a0-aa41-647e73a87c53 | -10.89051 | -46.61275 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fd5575a-0059-307d-92a0-cca6de133f84 | -10.8897 | -46.61746 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c9d6baa-6353-3032-9210-6a4878a96203 | -10.88888 | -46.62217 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be9da17e-179e-3fe4-989e-4817002998b8 | -12.88779 | -46.85696 | 2024-10-04 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df27d994-777e-3880-8769-19046c01f882 | -12.88407 | -46.85628 | 2024-10-04 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 846c986b-f533-38f1-9c3f-58ef768404a3 | -12.80651 | -47.43668 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f2857a7-b113-3388-a031-078102e41706 | -12.80435 | -47.43826 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4d1f964-f435-3b9d-a8f7-6323c4e8f428 | -12.8005 | -47.43759 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d82e86a1-50a8-3590-b40d-a2f76b54bb3d | -12.79966 | -47.44249 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e529abd-a8e0-3cfc-b1f8-888b227d66f7 | -12.79793 | -47.44024 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31578e31-f0dc-3f98-a983-477c82a98b3d | -12.79706 | -47.44514 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61eaf007-caad-3005-98c8-9324f4f8afb6 | -12.7958 | -47.44182 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 825858dc-f33e-30b9-b8ee-35be9319b355 | -12.79496 | -47.44674 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a9512a5-84ed-34b0-8775-5e4a2c707c27 | -12.7911 | -47.44607 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6614874-e914-3969-8807-7be5b436b0c6 | -12.79025 | -47.45102 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efbd31e1-2b0e-3597-bf9b-b3b547f94390 | -12.37936 | -47.6814 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 748945a5-9c02-38d3-b3c4-1d05a7b4f7b8 | -12.28851 | -47.64683 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40fdac58-b7ed-309f-89ab-56a6e0df5a25 | -13.59634 | -48.12842 | 2024-10-04 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 275988c1-e3c1-36fc-9035-e2b0752ed9d4 | -13.59233 | -48.12789 | 2024-10-04 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 237e0208-280e-3a59-94f7-265bc1a6f022 | -13.56708 | -47.63338 | 2024-10-04 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8d389f1d-54b1-30ca-b473-0146c4642006 | -13.56622 | -47.63826 | 2024-10-04 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c97fa9d1-3a84-3083-9b12-2f25cc9f4f82 | -13.56325 | -47.63257 | 2024-10-04 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f4d3d81-72ec-3539-93f2-d8b69cfa615e | -15.2106 | -47.50715 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d078308f-e4e6-3ce0-9f93-b98d2169ab31 | -15.20685 | -47.5066 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c59806a5-4326-3558-b495-0b26ca5cc287 | -15.20616 | -47.51051 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 511d84e2-86e2-34f6-bdff-d1417afc03ba | -15.20239 | -47.51003 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8de6d792-d502-3a66-8235-18a9842a544c | -15.19631 | -47.51503 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10f3514d-092e-3487-b67a-8951ccbbc9a5 | -15.19629 | -47.52275 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb59c723-6bf7-3ab2-8cec-baa8c6e334d4 | -15.19407 | -47.51349 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee1ecd55-ae3b-3548-bb6e-9cdaed84026d | -15.19251 | -47.51479 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 760ef1e4-f9dd-3d25-8eba-17df38dcbf96 | -14.80025 | -48.03831 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e94001e4-c842-347d-b4a0-c95b4bbdab49 | -14.79933 | -48.04342 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3b169fd4-ed84-30cc-8645-248a7400f9de | -14.79889 | -48.09059 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3dba1761-0d87-3667-b274-8a421b6eace0 | -14.79802 | -48.0955 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08767e71-3ba0-3bb2-8ddb-7235e56c7ef7 | -14.79725 | -48.0327 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d238e2be-f753-3b5f-aa6e-de7a9808ae34 | -14.79542 | -48.04291 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f51947e-6f40-32e2-8ffb-8a803d3b8036 | -14.79428 | -48.02703 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c58cadcc-d539-3390-a9a3-aff3f66e9b54 | -14.79336 | -48.03217 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc8952de-5643-383a-aa33-afcf2d0fa0f1 | -14.79153 | -48.04236 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6ca2da2b-42f5-3e60-ac06-042d9b0d1c64 | -14.79063 | -48.04736 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cba2e8d9-ca73-3c7a-9b84-5a578b0b186a | -14.79038 | -48.02648 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb8b5cc3-c1d5-3e4e-8b31-52c91ba0a253 | -14.78945 | -48.03168 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a97cc74e-0036-3b8d-9336-f5a34b0d755f | -14.78673 | -48.04679 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd0d7b8c-d8b3-3ce0-b61f-cc24576a616f | -14.7865 | -48.02585 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 606002c9-8048-3343-9da2-a5a8546e5c86 | -14.78581 | -48.05189 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ddb36e8-c340-3386-b978-18b214ba3633 | -14.78556 | -48.03108 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0e6703fb-b039-32ae-b4da-4c1e75ae19e0 | -14.78463 | -48.03625 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 959be0fc-07d8-3eeb-a0db-40a7220a8821 | -14.78191 | -48.05132 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a297ba2-cf5e-3955-ac39-da5b88f817ad | -14.7817 | -48.03035 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e02ea55d-4b03-3aad-b238-0b5e31bf233a | -14.78107 | -48.02698 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deae80ad-4587-38d5-b0ff-fb2c676af42a | -14.781 | -48.05639 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 612afb6d-2772-3b5a-84da-48213afed2d3 | -14.78075 | -48.03561 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 886ca597-a6d9-3a2a-ace1-b13ed8fd43c0 | -14.78016 | -48.03222 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2ce7cb41-3cd5-3992-a986-f709e305c373 | -14.77925 | -48.03749 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0159c104-5cb7-3e73-98c9-1e221b39a860 | -14.77782 | -48.02969 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e1cfa909-c875-36d3-9574-fa679aba9593 | -14.77748 | -48.09817 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4c4747b-24c5-3ec5-90e5-33beb6ef12ac | -14.77718 | -48.02637 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3a57e06-8749-3a6a-9762-5d026663fe1d | -14.77686 | -48.03498 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a230991d-0ef4-3c28-aa05-d26a1f1b22e1 | -14.77628 | -48.03161 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d53622f3-f306-389f-9c0b-8862776830fa | -14.77594 | -48.0401 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 43e6ee72-2ef4-3178-b13e-b0a8b48d9365 | -14.77536 | -48.03687 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5253ed5a-c56d-3bfa-b8e3-581889b1d79c | -14.77392 | -48.02917 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d7d7928d-8a44-3c19-9207-dfe28a7959a3 | -14.77297 | -48.03438 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dc95b18c-83d2-3957-a972-2db3e532567d | -14.77238 | -48.03106 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README72.md)
