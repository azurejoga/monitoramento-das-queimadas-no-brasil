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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef05dad2-e8f9-3fe1-b550-b80aef1f6ee4 | -5.47981 | -43.0745 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe96c5a7-4374-34ac-83d7-22d85a0e574b | -7.47552 | -46.47334 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3de37884-23a6-37ea-ba5f-9332cb11f1c0 | -4.40348 | -50.84502 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deb59b56-72eb-380a-8cc1-bafd5f311ac8 | -5.77426 | -43.29211 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec5a61a3-da4c-3818-85be-c9a8cba77e81 | -5.62982 | -43.92056 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cfa16221-423f-3fc5-bd4f-50f330f66fdd | -7.13566 | -47.34029 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7fab8b6-380c-3c9d-bdcc-ee78ecb5fcb9 | -8.57466 | -44.6687 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb6ccb68-bcfd-372a-ae2a-5c6c94581d5c | -7.76804 | -47.38797 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc4f404d-c6a9-346d-b6fa-eca68585b914 | -7.51626 | -45.43538 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2827a847-9150-3e00-acd1-1172a6adfa95 | -8.95975 | -47.34337 | 2025-10-01 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 875cea13-b2a6-3614-a458-87d77a0b9485 | -5.64423 | -41.2473 | 2025-10-01 04:49:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e091ed8b-2ed9-3453-88e1-80fd7ad1299e | -6.0342 | -43.60975 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecfb1c7b-598a-3921-b13f-6b613c87d863 | -6.06669 | -42.68221 | 2025-10-01 04:49:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66124653-9568-3ee5-a449-e137252c3c55 | -4.25511 | -48.56053 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d107d7d-e67a-331c-98b1-c0f68f8ce460 | -5.46008 | -47.23831 | 2025-10-01 04:49:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69572fde-6e79-3e7d-8d9e-d854b10442ee | -3.2412 | -52.89082 | 2025-10-01 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bb23d8f-9730-327e-b162-e12bfc4c7308 | -8.88986 | -46.64281 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3959d743-9286-3e84-8a32-3b971f2d04ab | -7.02178 | -44.48256 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82205844-0c80-35fa-9722-ec68ef212bec | -8.55695 | -44.76074 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e3003e41-6132-34f8-af89-a8c75f0a5bf6 | -5.9047 | -43.92792 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c383d6ab-93e7-38eb-9a74-9ebee586193b | -6.58049 | -51.68148 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d1d6368-4b3f-3ae8-9b21-e6bcc9f7384b | -8.75096 | -45.92529 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f8cc080-52fd-30e1-93f8-3cf6c39e20e7 | -3.81071 | -47.58458 | 2025-10-01 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38a9c70c-f088-3e11-830e-b86891f000f6 | -3.4633 | -50.09428 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 732e86cf-2ad1-3500-98be-01f7f19e405c | -4.05077 | -49.31779 | 2025-10-01 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98c40fb4-51eb-3259-aa1d-112a98cc8091 | -8.55305 | -44.65579 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d8a0b84-1f02-35fb-bef9-6e27ed59bf18 | -7.8241 | -47.06809 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3338c207-7ef9-34d6-9882-055579c1e48d | -6.80904 | -44.47304 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59a70d9d-df58-3cee-b6f7-2e86c585e836 | -8.55237 | -44.7272 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a93ed55f-2099-3ee7-b726-9cd283e834cc | -8.5505 | -44.64056 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16320ad3-1c26-3a60-8ba3-61d5c3a0701b | -5.95301 | -45.87398 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e3d8629-aa8a-3350-8974-9cf1517381c3 | -7.02658 | -46.98293 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c677d91-e89d-3987-89fc-f7996d15f9df | -8.58378 | -44.7359 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9168fec-2673-3ec2-9547-3e3036c7649b | -3.34628 | -43.19825 | 2025-10-01 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff01eefd-cc2d-3430-9174-7d8dc75a83a4 | -8.15923 | -46.26604 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c5d1411-0e2e-3fb7-8a97-5fb23275a62c | -8.15158 | -46.2612 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9792c5d-bfe8-322c-85b2-98c1656a8d52 | -4.63392 | -47.02034 | 2025-10-01 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d998b6c4-2b75-3345-b7a7-204b2771b293 | -3.46941 | -50.09878 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f4ee998-e420-3db6-906f-5fd4cd0b6543 | -7.73747 | -46.201 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c7a3ef8-b703-333e-96c5-65c08ce1745f | -7.02451 | -44.4586 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05521ef7-834e-35a6-99fc-b74ab8f86920 | -7.82557 | -46.97898 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 573b454a-d6e6-333c-8368-69e377b9f8bc | -6.20845 | -44.23729 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f953383f-9ead-3811-a166-6caf57323bd0 | -6.67458 | -42.8047 | 2025-10-01 04:49:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1fe832d3-bf87-305a-9630-0b4627398de9 | -5.90256 | -43.44316 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c9290ef-e739-35e1-b7be-0fff09c4cefe | -3.80945 | -47.59277 | 2025-10-01 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ded8d35e-65cc-32c9-8ea6-e5e6c15699da | -6.03899 | -51.89415 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eafe095-f8b8-37d4-be17-a494f28fd53d | -5.78797 | -43.29974 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb0c346b-8930-34a5-ab2a-472a3a9ea328 | -8.89481 | -45.04598 | 2025-10-01 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d33b8846-156f-3504-b929-29edfb72b7ed | -3.0901 | -47.01328 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 84270aef-e4fb-3d84-85c1-16f22433bdc4 | -6.28606 | -43.65483 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 860ddf9f-def7-3808-aa09-ee38d644bf30 | -6.20828 | -44.24071 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff9f4535-8caa-3b62-8b0c-1e9a16328269 | -7.05603 | -46.41475 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53253f55-9489-38ea-a634-c2e89f88d7b4 | -4.58034 | -45.61338 | 2025-10-01 04:49:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24d2da83-862a-3430-8215-6398db20a94f | -8.89391 | -46.64336 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 174b1c21-7df8-3903-b4a0-9fcec89976e2 | -8.55433 | -44.74632 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dc8cd96-d5c3-3341-95e6-9a9ff5a12614 | -6.89987 | -48.00398 | 2025-10-01 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2575a48b-2e2c-3a9e-8e23-76e24f650658 | -6.16554 | -43.09478 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab1cccfa-cc53-32c1-8d4e-fd0a6603bc4f | -3.81008 | -47.58866 | 2025-10-01 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06878b32-6bbf-3d3b-ace6-f68d6b22df67 | -7.05126 | -46.41936 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89bdfbc9-8b9f-367a-80af-1d01422bb026 | -8.92888 | -47.57674 | 2025-10-01 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d822550-4250-39d7-b6ca-d2ad4ff7b6f0 | -5.8064 | -43.73497 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7104ffb-2b1e-3332-852f-07a6ada6849d | -5.9502 | -43.31634 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce64d466-e3b6-3acb-8638-c6e56a4e8652 | -8.58231 | -44.74372 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1eeac105-48c3-34bd-898b-00c369f01ae3 | -7.54843 | -46.28091 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe77e050-a637-3b74-a774-616a4164e12c | -5.90076 | -43.92249 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a325799-3a9b-36cd-b339-2848d63495cb | -6.88021 | -44.52475 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e1d0058-5504-3484-ae2f-c21280cfe551 | -6.73194 | -49.64221 | 2025-10-01 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06d02bdc-a5b3-3f90-b091-e47159c19a30 | -5.77193 | -43.308 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76d36eb8-72b3-3868-9668-375774bef90c | -4.25338 | -48.55728 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d938296-95fc-3227-a210-b8b918ddfb1f | -3.55092 | -50.32813 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a9789f1-352f-37d3-ac4d-b5de6cec2d80 | -5.82884 | -42.81336 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 060b4abc-c5e2-3100-a0c7-e7a8371a1ec8 | -8.9275 | -47.58599 | 2025-10-01 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46a03bb3-2547-3da3-85ce-c3a590d07fc9 | -6.11563 | -43.21993 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80f344c2-abe5-3c00-9263-992457f53622 | -5.90934 | -43.9286 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05e7793a-be92-3074-933f-a48c7f9cc304 | -4.25801 | -48.55032 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 479d628d-dd39-32c7-a195-ba1354616862 | -8.14944 | -46.27565 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0aea7549-d9c0-3475-87d7-5275f87582f0 | -5.69708 | -42.66222 | 2025-10-01 04:49:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 479aa566-d515-3c36-a0aa-1ce33e01fbb8 | -8.5589 | -44.74693 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d1690f2-2714-38b1-9505-ebca20c9aa97 | -8.86325 | -47.65252 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c17fa88-338f-3328-bfc2-55f541125dbd | -8.55564 | -44.73705 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ecde1cd8-df22-3e42-99a9-8e795f837d35 | -7.77251 | -45.71287 | 2025-10-01 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3b56496-15b9-37aa-b648-a1d6c227f517 | -7.63164 | -45.44392 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c16e4839-51be-3e15-a958-a5df8320e7f4 | -3.09806 | -47.0102 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 9338bddb-4658-3189-b92a-b85b58137314 | -7.82096 | -47.06266 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 175119be-8049-38f3-919a-8ce090017d77 | -4.2528 | -48.561 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6280d4c0-3007-3164-bf30-d0471184c467 | -3.49303 | -52.46494 | 2025-10-01 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a03946b5-3448-3064-b52f-4929a409b8ab | -8.54982 | -44.64544 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db02a86f-ea26-341a-a1e6-6f6a834cd0f7 | -4.25972 | -48.55357 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bbf35f7-83ea-3e71-9f08-b8b795b5f1c5 | -5.42358 | -43.18744 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7076c570-5c13-34a7-9c25-bd22eb38212b | -5.6405 | -43.91201 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9b83c031-201c-305e-99ce-6507905eb9f2 | -8.29751 | -50.76925 | 2025-10-01 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a81634e8-e23c-3909-904b-fa003d88fe8d | -2.59528 | -48.11769 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c3046b3-3286-3d76-b847-5e682e21c759 | -2.89197 | -47.84122 | 2025-10-01 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c54b2ee-73fe-308f-a717-92ec33eded14 | -5.83139 | -43.87687 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| faab9a4f-cf52-334c-821a-7d7c323c79b0 | -5.89872 | -43.30589 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a4e39d3-43ed-302a-8eef-4ae60391cf93 | -3.46494 | -50.0839 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 68d9b2ed-96f4-3558-8d42-b07a0fc3e699 | -6.81205 | -44.47644 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e6259fe-dfa7-30d7-baed-3a1124ee2f45 | -8.23916 | -42.91348 | 2025-10-01 04:49:00 | NPP-375D | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37f0f57b-e26e-36fe-bbd5-c83f72bd31b2 | -8.40642 | -50.11288 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f15969a-054f-3aed-be0e-bb0856fed87f | -6.79827 | -44.74374 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README86.md)
