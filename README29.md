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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c84a1f6-1564-37dd-bdfe-c43621b46fe0 | -12.59854 | -47.98435 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a112b325-03de-3464-8d9a-c4cedcaa0551 | -14.20298 | -47.00791 | 2025-09-17 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccee8e6b-1a0b-33d8-87bd-a064ae5f702b | -10.6307 | -44.22371 | 2025-09-17 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75826dd8-739b-325d-9820-89129a5305a0 | -14.80053 | -51.70712 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 40dd395a-1a9e-313b-891c-08e266b7f2ba | -12.86126 | -47.1359 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e87be36-542a-364c-a23f-74fc53781ec2 | -15.02853 | -43.24609 | 2025-09-17 04:12:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a1b9c213-e897-3b7a-9fba-bc4b1abdcfcf | -16.61843 | -43.37455 | 2025-09-17 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7aa4e1d-2cf5-399a-bc2b-ba02a817d100 | -12.15316 | -43.2128 | 2025-09-17 04:12:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 327cf2e1-3fd0-3648-a67f-16189c1eb476 | -14.61916 | -46.3939 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a127182a-cb35-348a-83a7-306d6d49beda | -13.02834 | -47.95433 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7511c9f1-dac3-3a55-a775-05da6cc917dc | -15.98849 | -46.45496 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7745c155-15e7-3dec-af2e-67b8b573c8d8 | -13.6496 | -44.26175 | 2025-09-17 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6333bd90-3076-3f05-b3b3-201a1cafc56a | -10.8125 | -50.6557 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee17140a-7e7d-3a86-91df-8405d7dcf728 | -10.48417 | -49.37365 | 2025-09-17 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f964270-5d93-37a0-b7e7-152c5b3a1f47 | -15.43717 | -47.31969 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17a598bd-c82f-3c5e-aee1-06199a6660ae | -11.21536 | -41.60265 | 2025-09-17 04:12:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85bca4af-1c58-3b57-a9c2-55884783e94e | -11.08234 | -49.75792 | 2025-09-17 04:12:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b899fc0e-5c62-3b04-9210-57b18ec10ebe | -15.39983 | -46.1328 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f51542b-4138-3028-8d1c-ef3a84336bc6 | -15.42022 | -46.14068 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 119dd9c0-7017-3f37-9e08-b36a411cff12 | -12.47952 | -46.92063 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22e6274a-2e3e-398c-8b6c-d15147c02cc5 | -12.43524 | -49.73204 | 2025-09-17 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31af9798-34f7-3d20-8e33-bcef4cb4d6ea | -12.98427 | -47.94749 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 633b83d8-5849-31e2-b3a8-dde21c6c2f9c | -15.93076 | -42.6396 | 2025-09-17 04:12:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 01df6952-e72e-3b60-ba4b-3907f6a5400a | -15.41934 | -46.14391 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59290288-112c-3eae-ba7a-1b938397511e | -16.42792 | -45.66782 | 2025-09-17 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdeb18b5-109e-35a2-a73f-3a965380c62d | -14.59616 | -46.37724 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b43443e-0f90-304d-baab-f101c2c92419 | -12.9722 | -47.94591 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1dbb510b-b25c-39e7-987a-443d5e929dfb | -15.98918 | -46.4509 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef45054c-b658-38c0-9065-6d56d2c73ccc | -13.9466 | -43.98847 | 2025-09-17 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ead266cd-2cd6-3cd9-87ec-095ad57b7adc | -15.21848 | -50.152 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 172fe23b-0b55-375e-afee-0021d903ee4b | -13.17716 | -47.31272 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28b12808-d006-33b5-ba14-910acaec1c90 | -14.15593 | -46.13556 | 2025-09-17 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21e7809a-5e11-3449-89d4-d7dc77f928c0 | -12.71203 | -47.74354 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a751f1bf-a5a5-3832-9cf0-1da32c19de2b | -10.87909 | -45.44107 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c23156d-7ad5-389d-9d54-544a0606eb5c | -13.86283 | -44.88469 | 2025-09-17 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f213ca5-fb1d-314a-ac4e-a37c8cb353ad | -14.14008 | -46.9894 | 2025-09-17 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 841eb14b-a914-36aa-ae8a-d96b1aa97af1 | -15.39707 | -46.1493 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9de73c28-3ebc-3150-9976-156c9df731b0 | -12.85432 | -47.13066 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e4d3aef-9ade-3a33-a111-7d367a3138ee | -11.13472 | -45.33073 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f09066b3-1a21-369b-b8a2-8d2fa29b1a17 | -14.90939 | -51.70242 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73aa8c02-6752-308b-bd8c-d6ebade3eb43 | -11.50681 | -43.62955 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe9abcf0-8e40-3bae-9920-d4cd2fea46a4 | -15.98634 | -46.44619 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b21f0e3b-3e92-35b4-925f-8ba7ec112128 | -15.40549 | -46.14223 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b751cb1-c731-39e0-b3ba-ab56f319b43a | -16.85264 | -44.05058 | 2025-09-17 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c7ca0a-0509-3e99-958f-3286b5d22a01 | -12.71482 | -47.98673 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37b46af2-b906-3fbe-8838-79fbf9f6c4c0 | -12.70401 | -47.97743 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21ab4e45-28ae-3ccf-aafa-25816bd0c76f | -14.5583 | -47.36784 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4e70d07-58eb-32a6-b2a3-6db920513e20 | -14.62167 | -46.38853 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89dff8d8-f581-3683-a2b2-afff1a2d1cc5 | -15.41739 | -46.13593 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fde7acf-16d4-3bc2-a91d-8df1c06420c5 | -11.50406 | -43.71024 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a67d6fa7-7a9c-3aa3-b49c-26dc0728c364 | -14.83227 | -51.70404 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf49d6ff-c7bf-345d-9f47-658ce7fd4150 | -10.32654 | -46.624 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f47a1f9-983d-36af-982b-648f2bd7421a | -12.44189 | -44.74794 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a28deb76-c91d-328c-9ff6-5ad0f0366178 | -12.84673 | -47.19799 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e18db4b-414c-3464-b263-1a625101d6ef | -14.60104 | -46.32667 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b12cc78-6d74-3d88-aebe-0cc3998ef6c3 | -14.70253 | -50.24694 | 2025-09-17 04:12:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3c0b03ea-ce69-35a1-9f54-e552966641a6 | -11.07307 | -49.75617 | 2025-09-17 04:12:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22ef89cf-8d68-3609-9c8f-5358b38b0683 | -14.69769 | -50.39537 | 2025-09-17 04:12:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1616a16d-50c1-30cb-a619-5387543974b1 | -12.72171 | -47.99579 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 925f5200-ade2-30aa-ab7e-ad8628d3dd85 | -12.29248 | -50.12713 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7782efde-c56c-33d9-855e-39baabd7b60a | -11.12094 | -45.1112 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 855c808f-69c1-327a-847e-dc426eb31be6 | -12.6951 | -47.95727 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15c51520-1ee6-36c3-9b88-393311cb025b | -11.32782 | -43.48222 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c72aba8e-a6ae-3663-902b-11aeb2a4944d | -11.1228 | -45.35803 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8013fe3-c489-33d7-b1a6-f2ba6bd4af1e | -12.70495 | -47.94828 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 70f807eb-68e3-3b75-91a8-d158befaa8e9 | -15.40626 | -46.15922 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c86485d-637d-39d2-a0cc-bc474ed20fcc | -13.71177 | -49.85413 | 2025-09-17 04:12:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d28496b9-034d-3fb9-88a1-042ee76ac1c1 | -14.61123 | -46.3753 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8818268-6dea-3fde-a2c6-8bc41d670832 | -10.32572 | -46.62882 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56a402c7-9cf3-3f0b-8edd-0bb3811e16c2 | -15.43129 | -46.15867 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| edb76e8e-e63d-3afd-9171-2c00d1eb2895 | -12.06636 | -46.53583 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c1254e0-064b-34df-ba77-fafcd1664e92 | -15.40978 | -46.15981 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 732bcfc8-4c69-3c34-b548-737a8c50bdb8 | -15.43266 | -47.32362 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d27b96d-ba9c-3a64-88e9-5d41ae7139a3 | -16.61787 | -43.37817 | 2025-09-17 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75f5891c-f6f0-3878-b167-56a47c844092 | -15.32604 | -42.05542 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1fa6d872-7739-3758-81c7-6ee25fa86a37 | -12.70435 | -47.95171 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1ee33beb-a505-3ef8-8695-4f789807152b | -14.62276 | -46.39445 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6779d2ab-002a-34c3-8974-96788cab2bc1 | -11.93419 | -38.33063 | 2025-09-17 04:12:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 61e294af-fb74-3501-bef6-dfb23a381f17 | -14.85417 | -45.1248 | 2025-09-17 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee1b496-cb37-3d49-ae8c-3450260e3cae | -14.61734 | -46.39226 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef7293cb-55ff-3f4b-8fb2-c7c377574193 | -10.31805 | -46.62749 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34a76f58-e2e0-3cd3-a1c7-4a36464897f2 | -14.82349 | -48.10474 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09556644-d3c6-3827-a694-427cf94ce6a9 | -12.86488 | -47.14927 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbee8b8e-1b55-3864-8400-000e7a9d4bf5 | -14.61846 | -46.39807 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b038e18e-6e59-3d42-aec3-03efafb4af58 | -12.70033 | -47.95103 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b7db4d5-30a7-3f5c-90ce-5fc49392b8e2 | -13.08795 | -50.09623 | 2025-09-17 04:12:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a96100c2-aae6-3e5b-82d9-76586daa6487 | -12.06918 | -46.56438 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38b07141-a306-38be-bec2-afd3a3b7d669 | -16.48101 | -43.68485 | 2025-09-17 04:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd290bc2-67db-394e-a545-676d411743db | -11.4712 | -43.56447 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4d1d947-64d2-3567-936d-2b070bd5f14f | -12.6923 | -47.94963 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 818c3d4e-ea5b-3fa3-ae28-f8232b6b5be8 | -12.69457 | -45.80579 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc58cb3b-c2e1-33ed-9e9f-d83364cf4f1e | -14.80545 | -51.70815 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 19c65a86-6fc4-3c0a-b607-d2ea48e92ae7 | -16.42346 | -43.69043 | 2025-09-17 04:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db5ed5d8-5c05-3cc4-a1ad-753dc18c8f5d | -11.02437 | -45.06343 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b03c0744-51e4-354b-9c02-76601524dc7c | -10.48502 | -49.3689 | 2025-09-17 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f6489bb-ec80-3f42-af5b-0b4c30545c84 | -13.27946 | -54.18403 | 2025-09-17 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e6296de-b2e3-3657-8ea3-4726234c2cc0 | -12.9445 | -47.96246 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3324617e-3c9f-310d-95cb-bdd0e77e14ae | -13.62774 | -45.37004 | 2025-09-17 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3cedeefa-ad5a-3df2-ab8d-15ebd0c92b51 | -12.6966 | -47.9724 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f811d0e7-0db3-3b13-ba57-7d746d9db14d | -15.42103 | -46.15749 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README30.md)
