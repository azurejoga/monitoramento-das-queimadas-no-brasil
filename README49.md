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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 360e52f6-d87c-3077-a823-b4e52a7ce1ea | -13.72743 | -51.46019 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad15aca-1c78-3d36-a8a7-6481fbda0c10 | -10.63911 | -52.18442 | 2025-10-24 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b110409-d928-3624-bccb-a1a7c668dac4 | -12.7697 | -47.37681 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 76fe80a3-7bdd-367b-bc63-da9fad5cf29c | -12.72638 | -46.9486 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de73d128-1c74-39c5-b9da-f026acb4e593 | -13.61848 | -47.05228 | 2025-10-24 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b94ae19a-d96f-3a0e-931a-faa3048b833f | -14.21279 | -48.35155 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 120550aa-bc56-317b-97cd-0f2e6b2b7305 | -14.52274 | -47.95169 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5787995-67b3-3ca4-b373-b531162bb580 | -12.84636 | -48.55307 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df7e3ae8-7211-3921-aea6-50e915967bd0 | -15.44648 | -48.58018 | 2025-10-24 04:40:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d5e7a46-b9ab-3dee-bc8e-e47c5c908ea8 | -11.52949 | -47.10161 | 2025-10-24 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c7ffbb0-797c-3b28-8ce6-092a4dcae4a4 | -13.92209 | -50.2659 | 2025-10-24 04:40:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3436875d-5fc7-30cb-bca1-f9c7726d1855 | -13.72355 | -51.46319 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12205195-7126-316d-bf8b-164e22a34af8 | -14.43646 | -50.95111 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 279e1cb6-793a-35ff-a6ad-3ab4a64ba733 | -12.77334 | -47.37736 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6a6c68c0-8a89-3aef-8f7b-9451074921e8 | -12.77272 | -47.38169 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 901d872e-c6f5-3088-8fd9-4b3e76724e18 | -12.01525 | -43.88536 | 2025-10-24 04:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee005089-84a0-358f-b8c1-ac37fdf218c1 | -12.39324 | -57.52818 | 2025-10-24 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b21121cb-d9d3-3fee-b1ce-533e4b7eb5c6 | -11.02344 | -49.84576 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2121d32d-42b9-345e-82e2-962a4f299b3d | -18.57631 | -44.03855 | 2025-10-24 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bce61e2c-888f-375a-8e00-ebee4e6b2660 | -11.36388 | -45.9427 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32355fb6-923c-346f-b1bc-f804f86516f7 | -12.07683 | -46.41365 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23f07a0a-27ec-39de-8cc3-0559411f81c3 | -10.99283 | -54.25308 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d70847b4-6901-39db-b12b-5645f460e123 | -14.7899 | -59.24119 | 2025-10-24 04:40:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 001b4adb-0540-38cc-88b3-84d9b7020f21 | -12.22347 | -43.31342 | 2025-10-24 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 507d2d65-74f7-3297-81f0-de98309bdca8 | -12.82965 | -48.66458 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae3cc107-9221-3ee2-b714-4a2134c36c05 | -12.809 | -48.66135 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aa5439a-c9b6-3c92-b9c7-dad62693fd5e | -14.73797 | -46.60548 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef5b84c5-49e5-3d95-b45e-6680f2091794 | -13.35625 | -47.96334 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e967c33-3242-3461-8d60-96d308209c23 | -10.53787 | -51.59712 | 2025-10-24 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28267cf2-08c1-31bc-8110-5f8ace3d8199 | -11.04556 | -47.88761 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 841a9473-6862-3d36-a257-a24b5d0c4707 | -14.3447 | -46.88232 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5b5a12d-349c-3c9d-bf0c-17b82d89a1ab | -10.9958 | -54.25837 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f1267e4-c8bc-342a-8ec8-faafc0248246 | -9.44386 | -56.65293 | 2025-10-24 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c99ba39d-cc52-3b22-b9d6-fc10e3ca1578 | -14.42984 | -50.95002 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f598631-5f67-3ad0-932d-b19461154688 | -11.48062 | -43.24872 | 2025-10-24 04:40:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f91da27a-d17c-3df8-96d7-6245c6b6bae1 | -13.77301 | -48.34557 | 2025-10-24 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c96215a-9af4-342b-8953-20639d06abcc | -12.84233 | -48.55633 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a58a96c-362e-33fa-b558-7d3acf871f1f | -12.81684 | -50.96811 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f22114b-4f11-3db3-b4a8-d16022df60b4 | -13.28375 | -47.48547 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b2a93e-622a-3bba-9e09-f955f99cb361 | -17.00514 | -49.15383 | 2025-10-24 04:40:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1be5383-b644-3533-b44b-628d3d835518 | -12.02977 | -46.60742 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 299b07b1-9853-33de-8a45-646927a4f41b | -16.95562 | -53.22422 | 2025-10-24 04:40:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2472e66-3775-3fa5-a76a-1becc41cf4d7 | -15.83533 | -49.10186 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f736cb4-d943-3629-81ac-0a4763ba9d3f | -10.47502 | -50.20294 | 2025-10-24 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 900b43dc-2dc7-3aa7-80ab-b9b2e94ca6f7 | -16.98929 | -51.47595 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d45e5a3-1cae-30a8-9ae7-1dc377eba976 | -16.50426 | -51.47251 | 2025-10-24 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c3dd617-1ef9-3e6f-a4c7-ef3e1a07016d | -14.8688 | -59.62863 | 2025-10-24 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c4fd32d-fb25-3f43-9ac4-0536eb4c359d | -13.36437 | -50.46745 | 2025-10-24 04:40:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e469b45-5132-3279-8c15-61ef07ef7ba7 | -15.83647 | -49.09415 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e768a5cc-0ded-3930-92e0-fdb47342035a | -14.42873 | -50.95712 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27450fbe-fd3b-37fb-bcd5-6d591983c9ed | -11.24925 | -49.87837 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c8500ad-2e92-3ae0-8bcb-1711ece3f1b0 | -15.66517 | -48.84059 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2c8cdcd-2efa-3789-9aec-da8a1461df1a | -12.80499 | -48.66463 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86dc6065-d551-3522-9678-edd1909f039d | -13.35027 | -47.97933 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99339aea-8798-3795-a72f-5d7d7dabf208 | -11.97811 | -49.17994 | 2025-10-24 04:40:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 02224f7b-320d-36d1-bd76-24deddc58c04 | -14.20383 | -44.5987 | 2025-10-24 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c250e46-085d-30d3-b1ee-5e9b37627ff8 | -12.77396 | -47.37304 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e624d88-3070-3c69-a9de-12b3173e9b17 | -12.28278 | -47.46032 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f0f5150-b5a3-37dc-88ca-ca76d7fd841c | -15.3199 | -47.85306 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f39076f-7a39-3e5a-8ce1-e6a5e4080345 | -11.35403 | -45.95635 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| acd5f2ec-a0f8-3779-bd0d-3ba5ac0dba36 | -11.35651 | -45.96686 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5711946d-eaee-3455-967f-77f463543cd0 | -12.83297 | -48.64236 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc28b257-92c2-34a9-b6d3-4a655d1ee1af | -16.54362 | -46.44012 | 2025-10-24 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e159bb21-ea41-306b-a6ee-18168b371023 | -13.1157 | -51.73499 | 2025-10-24 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95195864-62f0-3620-948c-642222e1f20c | -14.20338 | -44.6005 | 2025-10-24 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60b8cc4e-44b3-368c-bb3c-81da66e44863 | -13.88669 | -48.38608 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 74d2aaec-0fd9-3be1-9bc3-341d4a0078aa | -14.2667 | -48.07549 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c73d550f-8183-3be5-a9db-7b50aa9a104e | -15.83994 | -49.09468 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc629742-e323-38cd-bd85-64c988575faf | -10.9117 | -50.16919 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f37a1d3d-9e21-37f4-8f80-6b72bc7e92af | -14.20325 | -44.60296 | 2025-10-24 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c0be073-a66c-33a1-9bae-e200971baebf | -17.65174 | -46.67075 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99557b18-309b-3a83-8079-6e7661374dd6 | -14.43921 | -50.95521 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e695097-80e2-30f1-8f71-b84059d65c08 | -15.21153 | -47.95839 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4861759a-9320-33a8-b74d-df167cd85100 | -11.09392 | -54.5047 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04beb609-83b5-3208-b296-cdbae85fa134 | -11.00984 | -47.90348 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76365f0b-11ce-3d38-b2bc-9f492a52cd0d | -15.18727 | -47.94624 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bb27bc3-778d-39f8-bca2-5a58ecc6ddc5 | -15.60114 | -48.0519 | 2025-10-24 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33e0aea8-a1af-33f4-b068-792ee1ee2c8d | -12.8216 | -48.67125 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd6e26e6-d0f8-3350-a81e-3772f0bde2f6 | -12.8176 | -48.6745 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a8f0498-ac09-301a-a0b6-ba15a9f1cfb0 | -13.9843 | -50.30083 | 2025-10-24 04:40:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f42cb94c-9539-3ed4-a3b3-22d36d431996 | -15.67124 | -53.34387 | 2025-10-24 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0a9c63c-f5b7-32e5-b49c-95ae82490a77 | -15.66867 | -48.84118 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 07061a56-8207-32f8-8ae5-d31b79b5c8e1 | -12.81472 | -48.67019 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0773616e-3bf8-32bc-b19c-fe47c1919955 | -12.82187 | -50.93639 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24a0bb25-acdf-3c78-9b6e-cc5a3c9c5ab3 | -11.48558 | -54.01638 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88652c0a-5cdb-3abf-b911-03fa27b8ddec | -12.80971 | -50.94885 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f9a6daa0-f904-36c4-82e5-4789887e0401 | -14.69313 | -52.82435 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7ec3495-035e-3c44-a227-942352aa5c3f | -11.02122 | -49.83819 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8cc048e-4e24-35c8-bb0e-27f0da193f2a | -14.75824 | -46.60278 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c55ceb4f-bd57-3590-b63b-bb170ecc0121 | -12.81353 | -50.96756 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e217c91f-6a73-3231-9953-5955fcbb38d9 | -15.3101 | -46.89537 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0137f26-b060-3e3d-89dd-5db9157434b2 | -12.67249 | -48.6366 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42b9fb78-8e44-321e-8e1a-e477f0e958d7 | -13.64039 | -49.46294 | 2025-10-24 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c87d3b84-6304-3992-b275-dd17b5342ee9 | -11.89108 | -51.52826 | 2025-10-24 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 598314c2-45ec-3e4b-be9c-0eef440b74b2 | -11.35861 | -45.95195 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fec0cfb2-1925-3574-b689-f232646d6a9d | -13.92181 | -48.39156 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce079264-a010-39a9-89ef-7ec3a491cbaf | -14.43866 | -50.95876 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc06f7c2-5ce9-33ae-a071-4a923b38e4ea | -12.80662 | -48.63006 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b75b3b29-90a5-3dfd-81b4-8e215ec261f6 | -10.97865 | -54.24581 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ff1b2c5-c4a8-3c8b-b6c2-1b1fcdc8ed41 | -17.09859 | -46.18928 | 2025-10-24 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README50.md)
