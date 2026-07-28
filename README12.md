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
| 9a5fb26f-4d05-3900-a13d-df7b0a387ea1 | -5.84428 | -44.8987 | 2026-07-28 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82f33ae1-ecf4-324d-8dc4-14f6c8669ca5 | -5.79798 | -45.083 | 2026-07-28 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b43c7f9-4b50-3f50-9934-caf1bcf16ac2 | -4.88048 | -48.15691 | 2026-07-28 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faa79a79-374b-34c4-bbc4-59daf30d7828 | -5.82694 | -43.48303 | 2026-07-28 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7695782-1184-3b95-b771-c62339aea797 | -2.48129 | -47.08961 | 2026-07-28 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66f7a912-c845-3d3d-b933-725adfa22040 | -2.42619 | -48.19478 | 2026-07-28 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db9deb65-9456-308e-bd0b-c22e816278b9 | -4.94325 | -48.24674 | 2026-07-28 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9dce082-1a3a-38f4-8d2c-87a18b06405d | -4.36873 | -47.76608 | 2026-07-28 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 348c23b7-b39b-323b-9e2e-b7b64657dcb0 | -4.94698 | -48.24734 | 2026-07-28 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63712d9-bde3-33f1-9701-5367203f8646 | -2.4237 | -48.19657 | 2026-07-28 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e925bc25-9527-3c8c-a2b8-81689cfffaeb | -4.37169 | -47.77096 | 2026-07-28 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5a9af5bb-2547-3a0f-85d0-86ab646f9551 | -3.14132 | -51.09941 | 2026-07-28 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e793e544-c3c0-31ef-b562-df6dd125e6a3 | -5.80302 | -43.63598 | 2026-07-28 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b55979c7-2686-3311-a8d0-8a21b58b0ae1 | -5.82639 | -43.4866 | 2026-07-28 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09d14ec6-0f29-3fe1-90e9-db01bbe77392 | -3.67504 | -49.48104 | 2026-07-28 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b9199bb-ac48-3247-9f9d-de6f83a9cb27 | -4.23094 | -39.21327 | 2026-07-28 04:29:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 817f7dbd-1253-38e1-a5ad-c1e9bc58e760 | -5.93819 | -43.66035 | 2026-07-28 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cb32eda-282e-3798-b602-d93205dafa0c | -4.54516 | -47.80429 | 2026-07-28 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54e30fdd-a7b0-3d07-8147-e86e63f9b243 | -5.90839 | -35.72845 | 2026-07-28 04:29:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7690c8a5-dde6-359a-9a6a-04daecd89c3b | -3.67854 | -49.48539 | 2026-07-28 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13603cee-4da2-3450-93ee-117a5e8d2273 | -5.90887 | -35.72512 | 2026-07-28 04:29:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13894b29-ae15-3057-aecb-a6c1b519a307 | -4.22686 | -39.21262 | 2026-07-28 04:29:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf374b90-7c92-3922-a143-4cd46798d5a1 | -5.48853 | -44.98382 | 2026-07-28 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cae094ad-6c41-36ee-9d98-4363b70d7f25 | -4.37239 | -47.76666 | 2026-07-28 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a57dadd4-4bf1-300e-9263-3a9af56b8bea | -3.74994 | -49.09833 | 2026-07-28 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0771ea8b-d6a7-3be2-889a-ee49541de514 | -4.01104 | -48.06251 | 2026-07-28 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b20d71c9-4c25-33bc-bb59-14f11929e9e2 | -5.90356 | -35.72422 | 2026-07-28 04:29:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9a6263f7-9c2d-3202-9a52-2931849f74ce | -4.09224 | -44.09725 | 2026-07-28 04:29:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0344df78-6c3d-3631-899e-e1063debfe0d | -5.49083 | -45.11926 | 2026-07-28 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ea0453d-524f-3c0b-9ef6-4726f23a83d7 | -6.27833 | -41.7698 | 2026-07-28 04:29:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9130a641-05bd-39a9-9d26-04cdf2711427 | -3.16988 | -48.12934 | 2026-07-28 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6539ea27-7b70-32bb-8663-bd4ac9640958 | -3.48207 | -47.68423 | 2026-07-28 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d910eeb6-5521-375a-bb3c-c1387ff50616 | -2.42544 | -48.19953 | 2026-07-28 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e18d7e52-eb59-3508-af13-fab8a6818664 | -3.14212 | -51.09466 | 2026-07-28 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee194d58-bdea-35f8-919f-ffcea20c93d0 | -5.48419 | -45.1182 | 2026-07-28 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae96f6e5-01c8-390e-b3ce-ea62716edf56 | -5.82527 | -43.49372 | 2026-07-28 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7be7804-ff10-3a13-a327-05a6897b7410 | -3.17366 | -48.12998 | 2026-07-28 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da10bbe9-d629-32b5-9a62-3628039676ab | -5.48751 | -45.11873 | 2026-07-28 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a693c30-6e52-3616-83af-ae2869835321 | -5.59706 | -44.92001 | 2026-07-28 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50970cc1-56ee-3db2-9bb6-5e9ecd4ddeee | -4.36803 | -47.77038 | 2026-07-28 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8bdcdfd-7ede-3f59-a48f-850883ee67fa | -3.14331 | -51.0969 | 2026-07-28 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09f952ed-70af-3002-9e99-55ff37e9ac8e | -6.27771 | -41.77391 | 2026-07-28 04:29:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2fff59a4-c6a6-3310-b5bd-d9644763c76b | -3.67914 | -49.48172 | 2026-07-28 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a7229ab-1f63-3e4a-989c-f42fcda09bd7 | -3.14255 | -51.10168 | 2026-07-28 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18366e66-4eef-3a55-9477-74715e85ab8e | -5.84483 | -44.89525 | 2026-07-28 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 250f2ca3-b765-350b-bdaf-b4a5442d6610 | -5.82583 | -43.49017 | 2026-07-28 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ef61e47-6ef2-3aa4-8d61-41b4b4106f37 | -20.723 | -49.4242 | 2026-07-28 04:30:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e49301e4-0840-3ceb-aadf-44717709bbd5 | -10.9588 | -43.0565 | 2026-07-28 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 9b3debd3-311c-3b85-82a8-009d221a2b46 | -13.3032 | -45.1045 | 2026-07-28 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 55ce6314-3faf-3a3e-9e96-e2ec46ced939 | -13.3037 | -45.0812 | 2026-07-28 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 92711235-005c-39ee-ad07-45373bf59eda | -10.9397 | -43.0593 | 2026-07-28 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| b59e861a-fb9f-3b5a-ac45-ccbd3a5de566 | -18.3543 | -50.6822 | 2026-07-28 04:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 36197c0a-2070-374b-92d8-a70ac8a63e05 | -18.3743 | -50.6786 | 2026-07-28 04:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 5deb1c91-150c-39f1-b2cc-c831b4f26db6 | -13.2843 | -45.0844 | 2026-07-28 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 847e7ab1-e129-379a-8cfc-522fa5cc8438 | -18.3749 | -50.6564 | 2026-07-28 04:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d3d290fb-f40f-355b-bdea-d653b474d8e5 | -10.9401 | -43.0355 | 2026-07-28 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a5d86541-8564-3c0a-8034-72bdffd9627f | -13.29315 | -45.09295 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| fdcc0fc8-8a8d-3f76-a2a3-fa0a13107aa4 | -12.33101 | -47.16294 | 2026-07-28 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd4e6626-34d3-34be-aafc-c5e904c7736c | -12.45567 | -46.50854 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 357b5d44-9062-3719-bd56-22cdbf543ff9 | -7.72011 | -46.50274 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab2efd81-990c-36ae-a1b2-52ef5987afb7 | -7.89972 | -48.2755 | 2026-07-28 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205f1c7b-698c-3ec9-8bf4-edb76dae99ca | -13.39778 | -43.56865 | 2026-07-28 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f81e77f5-597d-3216-83c0-3af93af5c5cc | -9.56669 | -44.57392 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20a4f848-8a7a-3c4f-9114-cc6834230f25 | -9.93566 | -47.90415 | 2026-07-28 04:32:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33a1004a-88cb-329a-a941-6829f19564e1 | -7.41113 | -46.83384 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d945ae2-4686-3460-831f-aa3d76e68b41 | -13.29988 | -45.11657 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8edb2500-d05e-37bb-989b-bcab6b318961 | -9.92935 | -47.89916 | 2026-07-28 04:32:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26879c58-df71-3b76-86ed-e8ce2f95d22b | -6.83656 | -42.88562 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1a2f4a86-f98c-37f9-b4f7-b4979ab48870 | -6.16118 | -44.64761 | 2026-07-28 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 285cdd3a-d8f8-3d34-9d8e-e548ec6e7285 | -11.49825 | -47.53872 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93589ca4-e65c-3954-8124-776017ae42db | -7.24335 | -43.14544 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d257df71-180e-3918-adb3-07f74d695dba | -9.33961 | -47.90652 | 2026-07-28 04:32:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77e00719-707f-3fc1-8615-92bd5d875ddd | -9.5639 | -44.56982 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85cc40fb-67b9-3ddb-a3bf-d710aa848f4c | -9.65746 | -40.59868 | 2026-07-28 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 081ff591-9b76-3d03-aa3b-dccec8efb1f6 | -13.29202 | -45.1003 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ec18710b-92b6-3683-b043-d21638ce2813 | -11.50723 | -47.54768 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5de295f5-5b46-3389-a636-0a608ba5ebb0 | -11.78527 | -47.08369 | 2026-07-28 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b2c56519-691f-3927-87e6-373c2ff09d3e | -9.36641 | -44.72398 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d88185d-f4fd-3c4b-b131-6090b2284bb7 | -10.75321 | -42.09489 | 2026-07-28 04:32:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 673752cd-15d8-32fa-81c1-c10f4a89e7f4 | -10.75386 | -42.09037 | 2026-07-28 04:32:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 90de3ec4-2fc8-3339-aac6-cd62f9f6a213 | -12.45398 | -46.51913 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf3aa758-5586-38f3-9a33-c1b98a371048 | -7.40773 | -46.83325 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2cb6fb3-f9fc-3066-9efc-7152f09e3e8a | -10.83687 | -49.38966 | 2026-07-28 04:32:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7af7792c-485e-3534-832b-fdccc3aed906 | -10.97061 | -49.44287 | 2026-07-28 04:32:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13ee87f6-7141-3906-89f2-2102773bc380 | -6.16504 | -44.64467 | 2026-07-28 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| faef6ca0-08c0-386a-b541-95afc35a9c60 | -7.44287 | -49.48886 | 2026-07-28 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eefc6c31-163e-3b2d-8945-a2ccd5cae194 | -7.00852 | -45.42939 | 2026-07-28 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cdb4a10f-bb3a-3e30-9206-e5d5d0471d79 | -7.25079 | -43.14277 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac7aac77-3ce3-37e1-90db-cb2c30cd8bc9 | -10.74947 | -42.09433 | 2026-07-28 04:32:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb4bfec0-8f2d-36c3-b235-09452f28adda | -12.67476 | -47.67378 | 2026-07-28 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7b48753-172c-3c34-88b5-84db338bf441 | -13.29482 | -45.1045 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4ae98919-687b-3394-ad24-090b34131a91 | -9.64614 | -48.28328 | 2026-07-28 04:32:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aec5fe2-b93b-3e9e-88c8-884fd54b568a | -9.92589 | -47.89857 | 2026-07-28 04:32:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35e6b8ab-c7f9-3eea-b590-6a93433f08c3 | -7.4626 | -49.73083 | 2026-07-28 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b720db1-3bc2-37d1-87ea-c0b263fa776e | -9.60895 | -47.76046 | 2026-07-28 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06acd052-3f19-3e1b-a44c-117fd9cf461c | -6.16172 | -44.64415 | 2026-07-28 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e917559f-1bda-3f0b-8e85-d7437dedcb15 | -6.84002 | -42.88615 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5ef04667-b62b-3ea9-a79d-9f6c39e40911 | -7.72626 | -46.50745 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 741f34ca-c659-3389-81cd-01687462916f | -11.77915 | -47.07899 | 2026-07-28 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 27075a99-7ef6-3cca-99e6-2e17267558eb | -13.29877 | -45.10136 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README13.md)
