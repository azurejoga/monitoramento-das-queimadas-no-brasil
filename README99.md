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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c26099b0-6f38-3412-b601-ffb2f48cdcc0 | -5.82847 | -45.37955 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6619bc97-f6c8-325d-90a6-98811bf71dfb | -6.20643 | -43.35006 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 21b4083e-83c8-39c3-bbc0-1e761d98ee0f | -6.36434 | -45.6272 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| eb216170-afda-3331-b13f-76cfa378a86c | -6.23095 | -43.55946 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 478a2330-53c5-3eaf-b99e-9ea4b59fbcab | -6.29799 | -44.14904 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 17946dae-157c-3cb9-89b0-1fa42732c964 | -7.2516 | -43.84887 | 2025-09-04 12:14:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0e23484-2b6a-3462-b7e4-d60e31085900 | -5.53838 | -46.42655 | 2025-09-04 12:14:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2f162f1b-ce23-366b-864e-48f7c4e98560 | -5.94269 | -43.71693 | 2025-09-04 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 18350a37-1423-3d40-8e4b-cd3ab571feba | -7.68261 | -48.73573 | 2025-09-04 12:14:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a42ba26e-b6ca-3a29-90d3-82fcc8f037c2 | -4.96218 | -42.06408 | 2025-09-04 12:14:00 | TERRA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 45aa51d7-d738-34d9-8178-9ee19a1fa5a4 | -7.68417 | -48.72518 | 2025-09-04 12:14:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 6de35d25-b1c8-381e-8fbd-e41d325f11ce | -6.42216 | -43.26313 | 2025-09-04 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2d3f51de-f935-32c3-b8c3-70736d9d6251 | -5.56738 | -45.20714 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 26ed6ccf-272a-3de3-a85a-db92140d419d | -3.80358 | -44.12509 | 2025-09-04 12:14:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 787237f1-7dc0-3be4-8276-bca79cf29782 | -8.03961 | -45.39018 | 2025-09-04 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| c5970867-cae2-372f-952b-285db9a7a17a | -5.70265 | -45.1595 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 983d5832-7844-3ff9-a411-44a44f9644e1 | -7.59841 | -46.21239 | 2025-09-04 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 86eb51c1-ba33-3e28-94d5-9262a81f24e1 | -6.3277 | -45.6941 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2f132dfc-74b6-35b1-badf-d1843ce654b5 | -6.21735 | -44.65417 | 2025-09-04 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a6b5c7c3-7b46-30c5-93ef-578dadc91521 | -6.92866 | -44.31718 | 2025-09-04 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3361cec-4652-30e3-92df-58d0659cda44 | -7.69873 | -48.72267 | 2025-09-04 12:14:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 15e1f85e-b2da-3249-984e-9387d9502fad | -4.89279 | -41.76708 | 2025-09-04 12:14:00 | TERRA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| efd9df41-81dd-39b8-9b5d-871c1f3bf3df | -6.505 | -43.57383 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cf0f57b3-e2a7-37b3-a092-934c5760d841 | -6.86146 | -44.27288 | 2025-09-04 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 834593fd-3650-335e-81b4-5673e388b671 | -7.97636 | -46.35145 | 2025-09-04 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| a2f0c266-d539-34c2-a79c-6d34b322d6fa | -6.8094 | -45.67572 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9d3acf06-7010-31d9-97e1-4323caf393ab | -6.0267 | -46.68842 | 2025-09-04 12:14:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4e2a6247-4913-3771-88d8-76c034bea4f3 | -5.89938 | -42.98005 | 2025-09-04 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 7cc4f232-a3e0-3ac0-be97-7a938da189b1 | -6.54723 | -42.95333 | 2025-09-04 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e7c41d50-1977-3b33-980d-34a45ba7467d | -5.68319 | -45.62351 | 2025-09-04 12:14:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b4e2a4a7-9bbe-341a-abd0-c7e77059463d | -6.75624 | -45.92067 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7a40c75f-907c-3d2d-a6d6-cb48cb4afb08 | -7.29849 | -43.71996 | 2025-09-04 12:14:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a7ea7c3c-a7bc-3821-b6eb-d6301b9d0aa6 | -7.55098 | -45.71159 | 2025-09-04 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3a60a2d7-9cb2-3ca3-8f3d-6fae3d95399b | -6.64611 | -44.09312 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 1ee1a068-c32f-3450-8451-d746d126a6c3 | -6.07295 | -45.54086 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e2e971fd-b9fe-390b-985b-df8185a104b5 | -7.97764 | -46.34259 | 2025-09-04 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 658769b1-de63-30d3-a585-6054d8ddd4e0 | -6.89277 | -45.54851 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cb55e7a1-825b-380f-b0bf-14f390edb3b1 | -5.03642 | -45.11421 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7ad3bd16-a0ad-31df-b2c9-438ffd80f8a9 | -6.35305 | -43.75752 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 08a791cb-dea9-37a2-92c1-70d21d1bc549 | -6.92656 | -46.90659 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1335b7fe-f120-3cd8-8a48-f29703c7cda4 | -5.98406 | -44.9986 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 03f63b89-9ff3-3d1f-8971-a6fcc392fa09 | -7.05548 | -43.27113 | 2025-09-04 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5936424f-b2b5-3121-96ac-045bfd1f4200 | -5.71152 | -45.16074 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6f6f2f40-ef6f-36ce-a31e-e0d417f05c34 | -8.02485 | -44.04059 | 2025-09-04 12:14:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 56d99ce0-c58d-3f91-8e0e-4cd0e0ac802c | -8.03195 | -45.37997 | 2025-09-04 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 92d8504a-f051-344c-8484-39c4d70ccffa | -8.02036 | -44.14288 | 2025-09-04 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f3e9f3e2-fac8-3761-b210-9b720d269a74 | -6.28317 | -43.84946 | 2025-09-04 12:14:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d1a42cad-306f-3a23-8e54-583d16fc1c71 | -7.69219 | -48.73703 | 2025-09-04 12:14:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 61f68195-513c-3bfe-91d1-416a7a1832b5 | -9.69692 | -48.99955 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 5e0a6247-162e-3753-bcb6-8f0a7a00f8ae | -11.91583 | -46.65247 | 2025-09-04 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d3cc291f-a1c4-313d-81d9-f3a5810ebecc | -8.38032 | -45.06457 | 2025-09-04 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3d5aa265-ed7c-3948-b052-aaedb3dd01df | -14.55136 | -48.07157 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| da5d76d7-59eb-3963-8b3f-a07d06a44813 | -9.80995 | -48.31511 | 2025-09-04 12:17:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 303af2fd-5a2c-370a-b334-c0848ab96322 | -12.45588 | -48.08108 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0981255f-42fa-334f-bfa0-9efbe02453ad | -9.43308 | -46.79472 | 2025-09-04 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ac00a69a-5385-35aa-bea1-3dab9719e47e | -14.03635 | -41.42426 | 2025-09-04 12:17:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 4b0203ed-afd7-3d0d-b40c-e1597bd6941f | -11.95654 | -45.77246 | 2025-09-04 12:17:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 57e592f4-42a6-3340-be95-3019b6f19c0b | -10.4447 | -50.26501 | 2025-09-04 12:17:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 5ab035e4-59e2-3a47-93c2-38bf6b3a922f | -11.95785 | -45.76304 | 2025-09-04 12:17:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 86d873d8-e0f1-3f6d-9ef0-07e27b87de08 | -15.14926 | -52.36348 | 2025-09-04 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9ef8beb2-638d-3769-82b8-ad503989fe25 | -9.54701 | -48.34702 | 2025-09-04 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4d71b295-e88b-3d86-b901-cfcfc3a65f84 | -7.71199 | -50.32199 | 2025-09-04 12:17:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 396aba13-cdb9-35a5-ac88-bc07a54d491a | -15.03408 | -48.10976 | 2025-09-04 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1c68e5db-4b70-354e-9942-3ec3a9cae50a | -10.98506 | -46.84105 | 2025-09-04 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e5757407-00c0-33b2-afeb-f31e30818b14 | -14.54116 | -48.07938 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| f13631c8-56e7-3e8d-afcd-bb5c69dab292 | -8.05572 | -47.57698 | 2025-09-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| a268c8ba-4602-3ccd-811d-b603e03b3f1f | -15.03363 | -50.09204 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b5286f62-4d06-3da2-9163-6d7fc8a03413 | -10.66452 | -51.5761 | 2025-09-04 12:17:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 7084e303-f6ce-30e2-b902-ab997b810750 | -14.57044 | -48.06496 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7a0b1c97-f99e-3a27-a308-982001fbd8f5 | -9.92425 | -45.87683 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cb072e4e-e865-3c60-b458-c8d0fec4dc5b | -11.88895 | -50.60518 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7fc605a4-a083-3269-bc54-123e1f762c42 | -12.23552 | -50.15543 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ae722167-dca1-3074-aee2-72a812b7d62f | -15.06524 | -50.04871 | 2025-09-04 12:17:00 | TERRA_M-T | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e85f0255-f63a-3b8e-b3a7-ca2093a3d240 | -15.19913 | -52.34856 | 2025-09-04 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1a0ee9f6-75d6-3c97-819a-8b83fb3d0088 | -10.91411 | -50.60116 | 2025-09-04 12:17:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e858a57c-4999-3fd6-9537-a735c7a7097f | -10.53642 | -46.75482 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2838d85f-ffba-3db4-8584-0ee072ad5214 | -15.15076 | -52.37006 | 2025-09-04 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e9314e23-b120-37bd-a6c1-847a4728d3f7 | -8.89898 | -45.82975 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 5131e63d-509a-30ee-a651-ec91d78f6175 | -13.85378 | -47.98239 | 2025-09-04 12:17:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d5f187d5-8fc2-3f86-a043-44be399e529a | -10.14794 | -46.24874 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3240537b-0d01-3db4-a190-f0a1a58a2cf0 | -9.4166 | -48.35092 | 2025-09-04 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80603f9f-b3c1-391b-b363-ff5105df7430 | -8.91796 | -45.8872 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3e774be0-7829-3fa2-af47-68b3dca2dbe2 | -13.30801 | -51.76099 | 2025-09-04 12:17:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4cbb25fe-9c6f-39ee-bdb3-8cf20a937cde | -10.09727 | -48.06027 | 2025-09-04 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 6bf592d3-dbc8-3e29-89a0-b47481b48fb6 | -12.45453 | -48.09027 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| fe004e4f-0291-366d-8c55-e53d963a7c3d | -11.73956 | -47.74768 | 2025-09-04 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 37184974-156e-363c-b8bf-4ff99881ab1f | -9.69534 | -49.00987 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 0d7d8f08-d3a1-3fd5-aa68-54dd81943deb | -15.19456 | -48.02542 | 2025-09-04 12:17:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 576a57b5-b248-3ea3-94fd-bf6261e792c6 | -14.49213 | -53.07671 | 2025-09-04 12:17:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5b252871-e41b-3d6a-805f-ee89450d0080 | -9.70796 | -48.99063 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c69267c5-8488-3628-b5c7-676f7833b85e | -15.29123 | -43.81836 | 2025-09-04 12:17:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 70d69ecf-109f-3c74-b5c5-a5f3359b5c69 | -9.92296 | -45.88591 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 340c7649-c827-36fd-87c0-c57487f0d0f0 | -12.29994 | -49.99525 | 2025-09-04 12:17:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f6179958-7cbb-3cf3-9855-5d8b882fb2e8 | -14.48737 | -53.08276 | 2025-09-04 12:17:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7ec9ae90-4ce9-35b0-8cc0-d51722ecb9a6 | -14.59011 | -53.02237 | 2025-09-04 12:17:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1a0e9eec-1ac9-3c72-be78-486264451e7e | -9.44835 | -46.75147 | 2025-09-04 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a1d5801a-3683-31a9-8b34-c2b8c3a15f93 | -9.61244 | -47.03036 | 2025-09-04 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d0ab3422-901a-3915-8c63-60aaf8bb97f9 | -8.73599 | -47.53092 | 2025-09-04 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4e796c33-1d21-3ecf-a39d-4e8961003c68 | -15.03275 | -48.11891 | 2025-09-04 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 483acb66-3b71-3bed-99b8-981545f98402 | -12.97418 | -54.76285 | 2025-09-04 12:17:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |


[Clique aqui para ver as próximas entradas](README100.md)
