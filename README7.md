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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee239f62-eedd-3e2d-826d-7007a7603dc5 | -12.84457 | -44.37304 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 047eac69-9a08-3652-af59-1fc5a8ca7c65 | -11.06682 | -45.18535 | 2026-06-17 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f4e2fa8-ff7b-31e9-b4ea-123dd4d5d523 | -9.20485 | -47.91162 | 2026-06-17 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e5879f1-f4e7-371a-a0f3-a44cf7466db5 | -8.94733 | -47.00168 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f47b5826-cc31-3f6a-90c9-c4f2c0b46818 | -12.18829 | -52.77549 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90796eee-ad4a-358b-9ac0-6762225917f0 | -12.17954 | -52.78113 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b5369a6c-bc3b-31fa-be72-472b306c3239 | -13.27909 | -46.0597 | 2026-06-17 04:00:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 497bc339-f43d-3f4c-9d52-898b7d4150f3 | -12.17884 | -52.82003 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 167880ff-9870-3f68-8b22-7710f587e009 | -12.20764 | -52.79339 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 688bac2f-9b01-3217-9612-c790d78b5c02 | -8.88984 | -46.97947 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26592c05-4dda-3a0e-890e-1ea3ce2583c9 | -9.26022 | -48.53647 | 2026-06-17 04:00:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ce9b24af-4e13-34c2-b01b-623e4cb45386 | -12.19322 | -52.79016 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| f08511c6-27f0-31e6-a062-85610bb68c6d | -8.88381 | -46.98181 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1ea39ac-4ee3-3bf6-a270-2c834ec25377 | -12.19396 | -52.78439 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 340cd273-1fa5-3e59-9cbe-ee057c8c2481 | -10.98351 | -46.47393 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dabcbb1d-cd7e-3551-9825-30b21de19626 | -8.94794 | -46.99828 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e84e3c3-2d1c-386d-9b25-fb47aba24b64 | -12.92459 | -43.61969 | 2026-06-17 04:00:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a917484f-3e6d-3590-b455-801de7529985 | -12.20522 | -52.80259 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2fa60f52-9130-3d13-9ad8-e416f7eea8ab | -8.88572 | -46.97146 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62b5f059-8b23-3edc-99a8-16dcb10ae4df | -8.98714 | -46.97616 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 021a4405-ce97-3a7b-a2de-5d20b799c728 | -12.20116 | -52.78601 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66a9bfbd-9fb7-3039-a60d-2ae67fe66534 | -9.29871 | -45.46987 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e38d85d3-78c1-3d22-8a27-9dcd6c125613 | -8.94695 | -46.97285 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f826b8bd-cfac-3030-9f1e-934b3c32aa48 | -8.97242 | -46.99517 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c29150f5-aee5-316c-a3fe-1e13ca433923 | -8.99124 | -46.98414 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 735f4cba-e379-324f-8380-51d29831b576 | -12.17233 | -52.77952 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9870834e-2763-362f-b9bd-806abf89666c | -12.44717 | -44.75449 | 2026-06-17 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c0a1973-4d18-39ce-b222-9c0f88c54e97 | -12.17387 | -52.77229 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a7ff3743-8f1c-39a7-b852-0c7a55fe5404 | -9.33547 | -45.47276 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23749172-9218-3da8-9f83-9a22a3984cd0 | -8.97525 | -47.01003 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1abe60b-3891-3a96-b4d8-6586386db571 | -8.98583 | -46.98319 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2bfbdf86-67ac-3d5a-a765-f9bf4d992927 | -8.68026 | -47.84991 | 2026-06-17 04:00:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1486f93f-ae37-3093-97fd-1bcffbd1d6ec | -9.3442 | -45.47992 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 17e4c75f-3c52-3dcc-8150-d6327d3534ed | -8.98779 | -46.97264 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93303735-ac9f-3dac-b7cc-aa1e2baf8d50 | -11.17707 | -46.59214 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d4b20a5-8f83-3967-8a20-ca95ec269e51 | -10.60364 | -44.32449 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c67b8fe7-07c3-3748-acea-33c18fe700ec | -9.21161 | -47.91204 | 2026-06-17 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a91472e-5cca-3290-bb42-8a12bc5c95cf | -8.97096 | -46.97305 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a06b7f4-03cd-3c7c-831c-1e3c5a8f4c79 | -10.98863 | -46.47446 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19514a5c-7840-3019-bee5-3ae36835d2eb | -11.18214 | -46.59311 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f156021a-0f76-3ba5-a783-5bfe4cd828dc | -12.18919 | -52.77399 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cf506930-d87f-3150-9598-049bf25546f5 | -9.33843 | -45.47209 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e63807fd-f955-34cf-a1d6-87afce2b280f | -10.98291 | -46.47709 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1672c863-2c68-308d-89c5-bbdd75254550 | -8.96983 | -47.00904 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c78a56e5-565c-327c-91b0-ec7a9c4696bf | -12.14588 | -48.46672 | 2026-06-17 04:00:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8ca586e-6db4-3de0-8e5c-1e4695784fde | -11.28721 | -41.99986 | 2026-06-17 04:00:00 | NPP-375D | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e3942561-b079-30d0-9a71-1b9f86b94b6c | -12.20601 | -52.80089 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 727853b7-e69f-3dfc-a201-04a13f0f9944 | -9.33449 | -45.4781 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a17e8be8-8c0b-3b3b-97f3-623b86f98adf | -8.27906 | -48.21805 | 2026-06-17 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18b9ab3c-1cbe-30ec-a725-f96baafc949a | -12.18601 | -52.78855 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 1806fe6f-e5cc-3db7-95fa-59cb1d27607f | -12.15378 | -48.45628 | 2026-06-17 04:00:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2baef79d-ca3e-38dc-a465-983f38b90361 | -9.32865 | -45.48256 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 9a532ffd-2221-34d4-b1d2-9551067858af | -12.20043 | -52.79178 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e23f3a3d-743e-3de7-a478-b8c9eb1d02a9 | -10.56702 | -46.23144 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a38a959f-dc0a-346e-b6fc-6c03e560f02e | -9.33074 | -45.48728 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| d0c89c52-b217-33e0-b6e1-1a414585fa3c | -8.97177 | -46.99866 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e79fcf5-ee46-3065-bd4b-a79888cfd20f | -8.98518 | -46.9867 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 667cbc42-34be-3294-8620-3bda12cd39ad | -11.79545 | -44.93137 | 2026-06-17 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5db7e93-e4c3-3a88-a298-aeac294196bc | -10.60058 | -44.32178 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35377d32-037f-3242-817e-ba10c9e6168a | -12.21646 | -52.7876 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9ef7944c-9920-31a0-928a-0ecc63b657ed | -8.9703 | -46.97656 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71153a35-9f77-39a5-89fa-1f8cdf16a6f9 | -9.3335 | -45.48347 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| de3ebe4a-89b7-3f2b-9077-f700525e6f64 | -8.97308 | -46.99164 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0a0e1b4-9c63-3c02-b048-6702bc22862b | -11.89101 | -43.82645 | 2026-06-17 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 886a13df-81e2-319f-814f-60149c82a72e | -8.9409 | -46.97541 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 856345a9-5116-3a34-ae14-6ff45885859b | -11.44843 | -39.27725 | 2026-06-17 04:00:00 | NPP-375D | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef943453-aa25-3a73-a9b3-98e191af70c5 | -10.59982 | -44.32613 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8da7b9f8-393a-33e5-a676-a70d39fb2789 | -9.32293 | -45.47467 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 674963c3-9b62-3c85-94dc-3f2426131494 | -12.22204 | -52.79669 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 07ea6884-d5ae-3f92-b532-e544aaec7158 | -9.33749 | -45.47744 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 8a7496d2-0536-3b29-bb3c-6d6b94bb5414 | -8.97374 | -46.98811 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 214aa7a6-9cef-35a8-82e9-f81ce3daf547 | -10.12224 | -52.18292 | 2026-06-17 04:00:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dc8da59c-9c40-3b5f-a984-8ae08fd66dad | -10.46692 | -37.43638 | 2026-06-17 04:00:00 | NPP-375D | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 14689972-fc08-325d-b764-bfc3e112c6e4 | -10.9724 | -46.45007 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95cb8607-01a1-38cf-b02b-aabb56c6e109 | -12.26264 | -43.50477 | 2026-06-17 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21b1be15-753e-3ed8-9c81-1710a4fe2ae4 | -13.5718 | -48.20377 | 2026-06-17 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0dd1284-a576-30a9-ba8e-cfe524220095 | -10.82271 | -44.3106 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f53fa4e2-3543-34e3-897e-6c5fe2a06fb9 | -12.19549 | -52.77713 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c88b188c-5648-3c75-ba7a-c2600e1cdb85 | -13.27814 | -46.06476 | 2026-06-17 04:00:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aae3ec98-bd6f-3aa2-829b-d22c491bc808 | -8.68133 | -47.84577 | 2026-06-17 04:00:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f9a01d7a-3abe-3bba-b575-a7d385edcc52 | -8.27605 | -48.22003 | 2026-06-17 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51923c31-c593-3462-a4b0-39c3cad58993 | -12.18438 | -52.79602 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| bacce1d2-ca5a-3190-bba4-29548afbe4b6 | -9.21055 | -47.91276 | 2026-06-17 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31108cb4-8975-3405-86e0-4b8603ffeefb | -11.88915 | -43.83109 | 2026-06-17 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f25efc84-5047-34bd-9b97-5ee7b87584e3 | -12.22526 | -52.78183 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 68f8718d-5494-3535-8107-f171b76f0c42 | -12.17225 | -52.81685 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a1a606b-6e32-315d-bdae-c7d39c576bdd | -8.27686 | -48.21579 | 2026-06-17 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc3c8ca5-73d9-3602-8d90-4fe7914c1c1b | -12.50711 | -46.35288 | 2026-06-17 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81b5baa7-569c-3c43-9a21-282d518a12ee | -12.84881 | -44.37384 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a133bf03-d643-34c4-ac71-193cdffd1ac4 | -8.94758 | -46.96933 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b89a3e98-7af4-35c0-91c8-014122916a48 | -8.94856 | -46.99486 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51a68d63-3f48-3c00-b082-e74e3efe502b | -8.68057 | -47.84977 | 2026-06-17 04:00:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da4585c6-4871-31ba-bc4b-3ae3755d8487 | -12.18607 | -52.82166 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76da94d8-af6b-3d54-bdd5-7c46bf23f88d | -13.5711 | -48.20724 | 2026-06-17 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53440cba-5e7f-3112-b797-11935a5e091c | -10.11659 | -52.17377 | 2026-06-17 04:00:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 519ad2de-7bb1-32b7-8fa0-aa5f2a236e1e | -12.1996 | -52.79339 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45c217dd-568d-3865-9f4d-21e5f98b5d76 | -12.50328 | -46.34637 | 2026-06-17 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f75d877-d7cc-3640-8da2-5238f9b0aacf | -8.96622 | -46.96852 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07aefb7a-b9b9-3de9-9f34-dcdf71562ae5 | -12.18671 | -52.82003 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9e968ad-f8b9-36ea-bcd9-ed60e8f4d4d3 | -13.27346 | -46.06369 | 2026-06-17 04:00:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README8.md)
