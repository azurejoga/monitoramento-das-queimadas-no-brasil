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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e398f3e1-0258-388f-aa54-d684cd2b41ad | -14.1702 | -45.3276 | 2025-08-17 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a72f1b00-06b7-3ab9-913c-4785390b77ad | -12.6335 | -46.9019 | 2025-08-17 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 7b1cea61-6a79-3277-86ef-c7fccd11b669 | -12.6143 | -46.9047 | 2025-08-17 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 71f46ebf-397d-3b69-9147-2ec410a79ccb | -15.7544 | -47.7967 | 2025-08-17 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 362987af-7500-335f-af6a-a2fc2939e743 | -10.844 | -45.3356 | 2025-08-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 292434a0-4925-3292-881a-9fb138f0fa45 | -17.9137 | -44.4218 | 2025-08-17 14:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 3fed98ee-6396-3e8a-91b2-b49be8fc16c3 | -6.4831 | -45.4591 | 2025-08-17 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| bd96b1c0-b0d8-3727-8a62-8f76a168d04a | -6.5018 | -45.4576 | 2025-08-17 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 1db8380f-19a9-3714-876c-fdbc2fd22dd8 | -10.8253 | -45.3152 | 2025-08-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 8888bf4e-35e2-320d-8f97-44f8b30a22a5 | -12.8795 | -46.0707 | 2025-08-17 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 6e263362-b4d7-3f09-9736-04fa8242007f | -10.8444 | -45.3126 | 2025-08-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 36e2866f-37a7-338d-af31-03ddd0d50b83 | -5.6971 | -43.3878 | 2025-08-17 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 56373a5f-802b-3345-9f46-ca3c8b229c75 | -3.982 | -42.516 | 2025-08-17 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 6ff40ee6-56ad-3d32-89e4-e80a7ac35d40 | -12.6143 | -46.9047 | 2025-08-17 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 706ef910-27c8-324e-986a-d4530fd4ec61 | -8.071 | -47.7045 | 2025-08-17 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2b6cc91a-f27a-323f-96f5-85eeec13bff9 | -6.4831 | -45.4591 | 2025-08-17 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 3258748b-1a82-3e8a-8a5a-ee3689f9ee24 | -7.5198 | -44.9836 | 2025-08-17 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 7d2ce95c-14a7-37da-9701-99dc6ee3fe25 | -11.9104 | -43.4319 | 2025-08-17 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 16277718-5f63-3f08-923c-6f6ebc463341 | -6.0791 | -44.6276 | 2025-08-17 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 32ca4fbc-6d01-346a-a383-edf1bd7cc24e | -6.5018 | -45.4576 | 2025-08-17 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 633cf433-e523-3b0c-bf2d-10840b21fd50 | -5.6784 | -43.3892 | 2025-08-17 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 428.4 |
| e0d9a87e-c461-386f-907f-70286d8f9fb6 | -12.6335 | -46.9019 | 2025-08-17 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b557d3df-730c-39c4-a5fa-5b43c2a6e030 | -5.6969 | -43.4111 | 2025-08-17 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 1056741c-d2f7-3638-9e98-0770820720ee | -8.9971 | -60.5339 | 2025-08-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 171616d1-5f77-3e00-bff7-c30531b26659 | -20.2198 | -47.0148 | 2025-08-17 14:30:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d82464e7-f7a9-39b6-bf0e-2b784f90e993 | -7.427 | -44.8782 | 2025-08-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1b856c06-6aba-3bb5-8c15-549debdd71c0 | -5.6786 | -43.3659 | 2025-08-17 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 12cdeb03-b798-31c0-a19e-d3cd9145a82c | -13.1453 | -57.1678 | 2025-08-17 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1ce1d803-67df-3f9f-96d9-26fbb45c8e8d | -17.9137 | -44.4218 | 2025-08-17 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |
| ab133032-8da5-3cfe-b6a0-11c53718a11b | -6.0978 | -44.6261 | 2025-08-17 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b0e6fc98-6c7e-334f-8408-c345e5774bb7 | -5.6971 | -43.3878 | 2025-08-17 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 4085d65a-1305-3050-b215-77ba87ae2726 | -6.5018 | -45.4576 | 2025-08-17 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 56587387-3354-3c07-bb82-facfc5b8af69 | -15.9229 | -48.1505 | 2025-08-17 14:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5191abbd-615b-3e5b-8f51-c785123a1bfb | -15.9426 | -48.1471 | 2025-08-17 14:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d4fcb312-dbb8-3ae2-aa74-6cfa918b0de0 | -9.518 | -60.5268 | 2025-08-17 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 84e1e08f-c895-3cb4-9694-2e4e4e2fead4 | -18.5145 | -50.6531 | 2025-08-17 14:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 117.0 |
| 088ac76b-6040-3eff-902a-45b3bc1f9016 | -19.1792 | -46.576 | 2025-08-17 14:40:00 | GOES-19 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 1551d255-8ceb-3e12-9420-a41d2f846f87 | -7.2058 | -46.2307 | 2025-08-17 14:40:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 2bef8c9e-63ab-3066-af17-ebc0b91e7577 | -20.2198 | -47.0148 | 2025-08-17 14:40:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 574d5f27-4b61-32fb-b48f-c918db7f9ce6 | -6.4831 | -45.4591 | 2025-08-17 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 9e9e5063-69ab-31dd-8abb-285b95fe57ce | -12.8422 | -46.0079 | 2025-08-17 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 51b9dae9-f89e-3e45-805e-8b3be7cc2b92 | -5.6784 | -43.3892 | 2025-08-17 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 350.1 |
| 9f651529-05a3-3b64-a30d-65dbc3812984 | -15.8602 | -50.204 | 2025-08-17 14:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a5a72fef-5b5f-35f5-b2c9-c1d4dae6906b | -9.5179 | -60.5461 | 2025-08-17 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| bd2f7e90-5b8d-35e4-9a49-9ab151de7362 | -8.071 | -47.7045 | 2025-08-17 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ab435bde-b067-3116-8bf0-8abd8f6e0354 | -5.6971 | -43.3878 | 2025-08-17 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 35912c71-6a42-358e-b05a-d9fbcc19838a | -17.9137 | -44.4218 | 2025-08-17 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 01934ab1-f653-3441-baa2-91c03f93a647 | -12.8234 | -45.988 | 2025-08-17 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 6c7126c5-6cd7-3c5c-9367-60aa55309239 | -7.0206 | -44.2505 | 2025-08-17 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 871003bc-b2ba-3b0c-9449-8f5cead4c659 | -12.6335 | -46.9019 | 2025-08-17 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 30fafbf7-b303-3f1f-947f-f8f52e1097ac | -7.5198 | -44.9836 | 2025-08-17 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6420c750-18de-335e-875f-80ecf30f00cb | -7.5522 | -45.435 | 2025-08-17 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8bdafced-e2da-3ddd-a38a-ef4a651f822a | -13.1453 | -57.1678 | 2025-08-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 033b0c6c-2112-351b-88c5-10813400ef62 | -5.6786 | -43.3659 | 2025-08-17 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| a383434a-3a53-365f-b469-cd8390982027 | -6.0791 | -44.6276 | 2025-08-17 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |


