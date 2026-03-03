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
| ff52d246-a4b5-32de-aa25-59e838169fc7 | 3.15865 | -60.696 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 204b1921-9692-36cf-9acc-48ad02a189ff | 4.28008 | -59.92104 | 2026-03-03 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e73c0d83-0470-3800-944f-db0476c64210 | 3.15283 | -60.68314 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72964a75-74fb-3104-bd9d-6ea81d2bb188 | 2.68645 | -60.07359 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1c17e03-6e0f-359a-a4b0-43ed27af333e | 3.18128 | -60.69256 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05696e62-893d-346a-b91b-704bfca788b3 | 3.12509 | -60.47717 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2515ce40-f0cc-391a-bc14-0b7aac9db068 | 2.89077 | -60.63187 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7405aabd-681b-3437-a062-2132eb9f9d6b | 2.89758 | -60.62625 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01f80d45-5a8f-30e1-83d7-2027954d9c51 | 2.30059 | -60.5138 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e53f3f4-22d7-3823-a976-9c6b48afa8ee | 2.86813 | -60.81355 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8127f50f-fa08-3dab-8df5-8253e61885b4 | 1.97518 | -60.70156 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12f1fe39-9054-3d3a-aad5-b70da5444b19 | 4.64665 | -60.70199 | 2026-03-03 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc9e6907-22d0-39a0-9841-aae4c512236a | 3.15937 | -60.70068 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2320a3c4-259e-393c-a027-9e94b9dfb040 | 1.95424 | -60.51801 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9fd28dd-2324-3e99-842a-f709a1a5c29d | 3.12137 | -60.47774 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a3d330ab-b0b6-3b38-970d-86bd6dcd9a0d | 3.15561 | -60.70132 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22ac9541-6b81-38ee-828f-6da983882948 | 3.14906 | -60.68373 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0349f0f-0024-3ebb-8a54-f6a67bf7875d | 3.64168 | -61.03352 | 2026-03-03 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c8d4d08-d41a-39af-b520-aca53318f6b8 | 2.52514 | -60.99137 | 2026-03-03 05:20:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a79c91-0b40-3ead-a415-f98e933be0e6 | 2.52444 | -60.98676 | 2026-03-03 05:20:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5990b52-5238-3a1d-ba95-58970dda3636 | 3.16763 | -60.70417 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e57b886c-9efc-3670-ad35-95ce07a8a5e2 | 2.90575 | -60.62955 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfd92856-a2d9-3fe7-a2d3-ba6f33860fa5 | 3.12205 | -60.48214 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c8ce93af-bb31-3080-9d94-d3953c6aa8cf | 0.49655 | -60.51734 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab5410af-5f94-351f-9498-4c53f6aced66 | 0.50115 | -60.4924 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fe5d49a-e49d-3c10-ba13-d9d3a42002dc | 1.52541 | -60.71051 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51233b39-88e3-339f-b1fb-cb3c68ee750c | 1.78538 | -60.48449 | 2026-03-03 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf0a2980-eef3-3b89-a454-6492ac920ec6 | 1.86957 | -60.40274 | 2026-03-03 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b143c262-4ac1-3718-a60b-f0bb35c69fa2 | 0.09324 | -60.6277 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ada87af5-c9b4-30e6-97b1-fc5a49767b90 | 1.48855 | -59.91417 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2996eb1-738c-373a-bb13-4332ab6bd100 | 0.08494 | -60.62777 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7d16624-c1c8-31d8-852a-cc78ba0ac379 | 0.46179 | -60.39233 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d83a98b6-99ae-3d09-852e-6e307d1f205a | 1.35311 | -60.03542 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 566065fe-c125-3ad0-ac10-5035aadd0a8d | 0.8 | -59.87016 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a546c7a0-beaf-3a06-8f0a-d16f6fcf2db9 | 0.9988 | -60.41584 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56613191-6f2a-323e-9670-639fd597fc15 | 1.15193 | -59.90247 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e606f86-dae5-336b-bc88-5e883b6cf049 | 1.45392 | -59.96732 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ad95a2c-c45a-32d0-a2f3-9d192a250be5 | 0.70046 | -59.96499 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6622d73c-8a7d-3cfb-93b3-3d644cc4f864 | 1.33907 | -60.06229 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9773a557-c5e3-337b-a4e4-3571dc22be9f | 1.35985 | -60.05499 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ddff19-f758-32d2-b5d0-fbbdfeba5af5 | 1.48668 | -59.92146 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc1ae6b3-f381-3cbf-b15d-c34e4fa6830d | 0.31052 | -60.44465 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 015ab051-8a34-3209-8d84-1e9b98f928c1 | 1.49053 | -59.95057 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e18433c5-3bbd-34ee-a693-bb93f8e4b672 | 0.89563 | -59.78824 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e381c7a-8d67-3cb0-a112-20421a01a3b8 | 1.55269 | -60.28257 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2e7741c-81f7-3eb4-9b4e-2cbc6901e5ed | 0.74719 | -59.76321 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec86a520-a1d2-30d4-9954-0bccf2c89af8 | 1.12003 | -59.20053 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f361e22b-ebf3-3791-b143-e452fee2e80d | 0.30397 | -60.44989 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c37fbc4-09f9-337a-b3d5-39f034920f63 | 1.48622 | -59.92264 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f6090d7-3c74-33f9-974c-0f9d9d036a62 | 0.94333 | -60.18153 | 2026-03-03 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 679948a1-2847-31c8-a364-95bebe0aa910 | 0.4582 | -60.39289 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 446907eb-ec31-38da-b601-351f4cb67343 | 1.48376 | -59.92593 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bcaaa1e-3963-3f19-b9dd-85854366eafc | 0.4939 | -60.5008 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b044599d-e38b-3ee0-947f-69118c88f77a | 0.49227 | -60.51377 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6db55255-4598-3199-8b2e-835544c2cf18 | 0.30693 | -60.44523 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28fd6fa9-d16f-3281-ac3d-a84218cbc094 | 0.77 | -60.47444 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38541225-da03-3b48-9261-9dac65966c84 | 0.06127 | -60.97332 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e6b4ee9-90fd-3e40-945e-fdef19f9f614 | 0.31411 | -60.4441 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0b48e31-ed39-37ae-b09f-9131ed7b1759 | 1.48916 | -59.91814 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf86c1ac-9f91-34f3-bf4c-fa6345bd207f | 0.87255 | -60.46821 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc49f9ef-36d4-3c6d-803f-3426b4fc4061 | 1.48896 | -59.91299 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00e99647-1354-34da-8489-5cba96203f87 | 1.00052 | -59.51031 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a6fcc2e-64f3-319e-a716-9f3f78183fd8 | 1.83151 | -60.84725 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e554c31-0dd6-333a-8647-1d4812345e0f | 1.48478 | -59.90956 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d5e220b-88e9-3786-98d6-113b7e1c252c | 1.13082 | -60.52075 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7b4fdfe-0a1c-35b3-a805-2822df2a9a98 | 1.51293 | -59.93074 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 712c295e-3a76-3623-a1da-85333e0d7c84 | 1.51043 | -59.91464 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 36d3f833-a02b-3c4d-bb73-a2d87e362fb6 | 0.96507 | -60.53209 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 633799f0-93e6-309b-aa3e-53abefc8f5b3 | 0.23153 | -60.51463 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e56f71f8-ca81-312d-8310-e43c86cd3b1f | -1.50983 | -54.52438 | 2026-03-03 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53961931-7ba9-3090-934f-33393b371636 | 1.12718 | -60.52132 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae95470-3f4b-3722-b5e6-b6cae10a8155 | 1.50211 | -59.90786 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a17f8f6-0e44-3c13-983a-4b247f003e55 | 1.51105 | -59.91867 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e272d4d-d375-351b-8bf4-bedfcef738f9 | 0.08962 | -60.62826 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9253dac1-3b39-36d7-a1ea-d97c9da6585d | 0.23513 | -60.51407 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54ba28be-2681-327c-b687-5869260e42a8 | 0.30102 | -60.45455 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3025088f-6db7-3c5a-bd55-d89852a46f29 | 1.45603 | -60.07368 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cee228a4-d9c4-3b29-9d48-002bdc1f0e76 | 1.12651 | -60.51712 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d584adb7-a94d-38a2-89b5-0e724e24aee1 | 0.23939 | -60.51764 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed21e04c-4713-3331-90ce-2d91c82a3f5b | 0.49649 | -60.51006 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 498f462f-823d-332a-a519-f6a5acd6ad23 | 0.086 | -60.62885 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 599be4ae-9bc3-354c-a640-cce49fdf46f5 | 0.30988 | -60.44057 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8bc0fb5-2de8-3e5d-9437-6b18a7b3685c | 0.45102 | -60.39401 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cc5f162-268d-3aa7-a449-64503093b563 | 0.92418 | -59.5566 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e211783-64e1-3233-b457-b5896def3fff | 0.49456 | -60.50493 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6f1a09e-5aea-3b89-924d-3a9ad1e67f92 | 1.50751 | -59.91927 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89f9ec72-dc57-3a38-bc41-c6ebf608dd44 | 0.50045 | -60.49554 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 523b4c26-0b06-3844-b837-346334db1d86 | 1.07951 | -59.25635 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df2ad92c-ff60-32d2-bdc6-5b0bce95c6fe | 1.3397 | -60.06631 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea0c1be3-a1cf-334d-93f5-09f8eae9a6c8 | 0.70108 | -59.96891 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d019067-a5dd-3bac-ba33-2b5d57a3262f | 0.87888 | -60.39098 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcc94fea-2b96-36be-a43b-7e75ecc6fa88 | 0.4133 | -60.5771 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 868363e8-ac4d-3734-9c2a-f71def245ccd | 1.11093 | -59.57182 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d52c73a-b24e-34bb-8c0d-d7320be11a32 | 1.47249 | -59.92369 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e05821a-70e3-3c17-87a3-63a854786bb8 | 0.17525 | -59.42778 | 2026-03-03 05:22:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 512ca3f6-9f72-389c-99a8-9acff5526fbe | 1.87737 | -60.91469 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5bab46e-9f48-37a3-9a8b-348e71ff7f58 | 1.50149 | -59.90386 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 324c4739-9788-3f72-910b-b9e081c9da3c | 1.4802 | -59.92645 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b266d4e-df8d-3c4e-b2fb-4ab02603de5d | 1.8616 | -60.39965 | 2026-03-03 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58f3e962-2750-3785-8293-4ba088bfc56f | 1.50999 | -59.93528 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
