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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c676eb0-a797-39de-8e0c-141fedc734b5 | -3.2317 | -46.8716 | 2025-10-30 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2d2c48e1-8b22-3e27-b11e-64a33f988f30 | -12.495 | -50.5684 | 2025-10-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 41d59523-dd9b-3ea6-bd48-1c4f7e704897 | -6.5254 | -46.9074 | 2025-10-30 01:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 1d023250-e1bb-3544-acba-95a46efb1fd3 | -8.3125 | -47.9236 | 2025-10-30 02:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d494bc67-9b87-3402-b3ef-9e70cc262e0b | -12.5141 | -50.566 | 2025-10-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8a43c28c-cce6-347d-a8d5-d79b4a5351a1 | -8.3313 | -47.9219 | 2025-10-30 02:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| cd899684-f081-3c4f-92b5-bcc9ae3388ab | -12.495 | -50.5684 | 2025-10-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 10fa60ac-dcd7-3710-9298-70d42c3c3332 | -11.1755 | -51.0606 | 2025-10-30 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4cd176c4-7a4c-3718-8872-5005431a2588 | -12.5138 | -50.5875 | 2025-10-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7d29be78-97f0-371f-acc7-a783ecc1428c | -3.2317 | -46.8716 | 2025-10-30 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 74b2b10e-a698-3ebc-8268-2d0955c340f9 | -11.1373 | -51.0859 | 2025-10-30 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| eff48b20-cec8-323e-87bf-e80cc1e98938 | -8.3311 | -47.9438 | 2025-10-30 02:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 00330279-bb5b-38d4-8388-08bd93518663 | -3.7867 | -43.9011 | 2025-10-30 02:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ff331398-a65c-36e0-b7b6-cb99e5efd066 | -3.8054 | -43.9002 | 2025-10-30 02:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 806bd51b-f1f9-3e1e-a0bb-5c29e049aaac | -12.4947 | -50.5898 | 2025-10-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 338175bc-0bd6-3992-807b-e4e0a94630ce | -6.5254 | -46.9074 | 2025-10-30 02:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 09ad03d5-f9de-3d8d-94b1-60c82333f5ba | -11.1376 | -51.0647 | 2025-10-30 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| dc49037a-b9f5-3670-8139-7abf421f509f | -11.1563 | -51.0839 | 2025-10-30 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 4594c6e1-2dba-34be-a339-9cb15b3f3a20 | -11.1566 | -51.0626 | 2025-10-30 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 0387510b-5460-3ead-bd97-308e793e2b14 | -2.7741 | -45.3989 | 2025-10-30 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 06607b7b-9621-3ee7-87b8-4b58b80f33bf | -11.1373 | -51.0859 | 2025-10-30 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3a48546f-4f7a-3400-a7e5-5241efd72c4a | -2.7741 | -45.3989 | 2025-10-30 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d73414d8-a1d8-36f7-9b11-36900e81e50a | -11.1563 | -51.0839 | 2025-10-30 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 96c59ec1-8881-37aa-82d4-9965d4f7a8ae | -12.495 | -50.5684 | 2025-10-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 6cd907ec-9f9f-36e6-baab-d170238737df | -4.2832 | -59.6554 | 2025-10-30 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 964df1c4-5668-31bb-ae65-056739495903 | -12.5141 | -50.566 | 2025-10-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 55a0ca2e-9286-3b3a-8ff4-581c036a4aba | -3.7867 | -43.9011 | 2025-10-30 02:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 63c8d232-be8c-3cdd-8361-33da02788ed2 | -8.3313 | -47.9219 | 2025-10-30 02:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 09454662-6592-3b4d-86ce-83d017ae6066 | -7.7852 | -46.4251 | 2025-10-30 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 74c684f7-49df-390f-b508-98d3b54d7d9a | -12.5138 | -50.5875 | 2025-10-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2e39b211-d29a-3e92-bb25-9150090e87a6 | -11.1376 | -51.0647 | 2025-10-30 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c9d0543a-274e-388a-9acf-79ac91aade07 | -4.2649 | -59.6558 | 2025-10-30 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 52489295-8d16-3391-b707-3c4ede4e62a6 | -10.4871 | -45.0387 | 2025-10-30 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 027a97c9-c360-3386-a3d6-6b8ccfe3dc08 | -7.804 | -46.4234 | 2025-10-30 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f7262ac2-d135-34e1-9033-6711620a3279 | -11.1566 | -51.0626 | 2025-10-30 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 155.4 |
| d236f40c-5213-36c6-b390-00576adac5af | -4.2648 | -59.675 | 2025-10-30 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3600fd07-f1f2-3a13-9848-47d33ccd2cb8 | -3.8054 | -43.9002 | 2025-10-30 02:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 02ca2ce7-76ed-38b2-8461-dec26b069fbd | -7.7854 | -46.4028 | 2025-10-30 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 7b20a765-d35d-3c10-b8f6-0cdc01515ba6 | -3.2317 | -46.8716 | 2025-10-30 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 687926e4-1541-3b91-a01b-8811e3dd0910 | -8.3311 | -47.9438 | 2025-10-30 02:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 9b004ff3-387a-3e87-98b7-6942bee5e14e | -3.7867 | -43.9011 | 2025-10-30 02:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e135859a-ef3a-34ae-9d7c-645852afd657 | -8.3311 | -47.9438 | 2025-10-30 02:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ec7ff8f7-4152-33ab-b49d-a6cd02a85cc3 | -11.1376 | -51.0647 | 2025-10-30 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 16cf556b-754c-3bf9-ae2b-24856123c7d7 | -13.9526 | -48.4499 | 2025-10-30 02:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8e616dbc-3b6f-3c2a-8205-9cd02de15708 | -7.804 | -46.4234 | 2025-10-30 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 04679a6f-9932-3e09-bc39-8516000e25ec | -8.3313 | -47.9219 | 2025-10-30 02:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 8dc1a9bf-2e45-31de-9083-3e86362d20a4 | -12.5138 | -50.5875 | 2025-10-30 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e5bf58d8-1de9-37f8-aa44-beafaf0a7154 | -2.7741 | -45.3989 | 2025-10-30 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7c4c7279-ffe0-319f-9b61-054e49743b83 | -3.8054 | -43.9002 | 2025-10-30 02:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 92d71b66-8a8c-3168-b18a-3d36ff31d143 | -11.1373 | -51.0859 | 2025-10-30 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 9a2e6c6c-f056-3db7-91b3-ade434d58c7d | -12.5141 | -50.566 | 2025-10-30 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ac955bce-1733-3e20-9212-ad160665c453 | -6.112 | -47.2017 | 2025-10-30 02:20:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 7d3137d9-d3e2-3877-8cec-6c122f67fe81 | -7.7852 | -46.4251 | 2025-10-30 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 5a3a2cc1-71a7-34aa-b33c-658e9bb6ed30 | -11.1566 | -51.0626 | 2025-10-30 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2b9c0aa0-3a28-323b-bef5-6d3ac0ef17b7 | -10.6502 | -52.1873 | 2025-10-30 02:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 60e747bd-05a9-3122-8f28-b96a666b2fd5 | -4.2544 | -43.7149 | 2025-10-30 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 741905f2-2fb8-3881-8df2-76294a8c9b98 | -8.3313 | -47.9219 | 2025-10-30 02:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 47e71afb-3291-3f2b-bbb4-3dfc0d76ae7e | -11.1563 | -51.0839 | 2025-10-30 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 132eca3b-0594-3b72-bc52-435ced842ca4 | -4.2649 | -59.6558 | 2025-10-30 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 31f20b5a-cc24-372a-a8d4-af28df662933 | -8.3311 | -47.9438 | 2025-10-30 02:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 30ee68e4-b0a3-333b-8718-7b89723ef033 | -12.495 | -50.5684 | 2025-10-30 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ea49aad4-804e-3a40-91f3-998caa2f8f8b | -12.5141 | -50.566 | 2025-10-30 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| eed01ba0-0637-3d1b-9fd7-e4716fd33905 | -12.5138 | -50.5875 | 2025-10-30 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 82a5912d-8dc2-3a24-8c47-5fa3e1286db8 | -11.1566 | -51.0626 | 2025-10-30 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d0a9dffb-a4ea-3f63-9268-c681d9ddfb51 | -4.2832 | -59.6554 | 2025-10-30 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c7135c66-0f41-3940-88bc-13c7f380ac51 | -3.7867 | -43.9011 | 2025-10-30 02:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d57f68f5-40a1-3c62-85a7-2996c139713a | -3.2317 | -46.8716 | 2025-10-30 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 59d61dd5-727e-31bc-9cd0-66a17f46e697 | -7.7852 | -46.4251 | 2025-10-30 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 88ec2488-c139-3dfd-9baf-b6041338e5ae | -6.5254 | -46.9074 | 2025-10-30 02:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 17c8094a-5cdb-33eb-b584-5cfba5ddeb05 | -3.8054 | -43.9002 | 2025-10-30 02:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 38992742-4de2-3163-b434-ed21850a3b52 | -12.5141 | -50.566 | 2025-10-30 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| ea756c4c-e5c1-3c02-a5d6-c4e9c50d7a71 | -3.7867 | -43.9011 | 2025-10-30 02:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0ecf6291-d545-3f30-9a95-d10287b43ddd | -8.3313 | -47.9219 | 2025-10-30 02:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| b46f08e3-aa9b-33b0-a4de-cde60eca0abd | -4.2544 | -43.7149 | 2025-10-30 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 06a89b60-5739-3243-b8d2-de26b3538e0d | -8.3311 | -47.9438 | 2025-10-30 02:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| ea690317-5b32-386d-bc43-cc4044bdb289 | -7.7852 | -46.4251 | 2025-10-30 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 250467af-6624-3170-af5c-f8b824376fb4 | -11.1566 | -51.0626 | 2025-10-30 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 58cea3c2-36de-342d-9a91-bdef76c440a6 | -3.8054 | -43.9002 | 2025-10-30 02:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 40efee82-fcd8-3556-994c-f93928026f19 | -13.9526 | -48.4499 | 2025-10-30 02:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6bd3fa35-ba9a-33dc-bf46-158412f52269 | -7.7854 | -46.4028 | 2025-10-30 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 74dbf585-7f0b-32c3-a9cb-c144c6b6ebab | -15.0249 | -46.3082 | 2025-10-30 02:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 068a6ae9-34c9-34ae-9b9b-2185f861147d | -7.804 | -46.4234 | 2025-10-30 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 09d5b007-904b-3d43-9de4-7b6ac01aecee | -10.6502 | -52.1873 | 2025-10-30 02:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1e0d6562-3e29-3e75-ba46-25e2b28b0ccd | -18.7298 | -42.5799 | 2025-10-30 02:40:00 | GOES-19 | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| f7e1a8cb-cc2e-35dc-825a-d0061a5a3a4a | -8.3311 | -47.9438 | 2025-10-30 02:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| d28aa2aa-8a9c-37e4-bb79-cec3e4f88381 | -8.3125 | -47.9236 | 2025-10-30 02:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 4b5434c4-30ac-37f9-9377-5b4d32ad0741 | -4.2544 | -43.7149 | 2025-10-30 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 909d43b5-2658-3b76-bf30-22da02774a69 | -11.1373 | -51.0859 | 2025-10-30 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ef96900e-53cd-39f7-abd0-6c133e5c67ed | -12.495 | -50.5684 | 2025-10-30 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 05af10a1-8a17-3de8-94d4-d267d1bf6f39 | -7.7852 | -46.4251 | 2025-10-30 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d603c6f2-570e-3458-8607-4b64f0251e38 | -15.0249 | -46.3082 | 2025-10-30 02:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d2585f3b-8e3c-3446-ba3f-591314ee3a9e | -12.5141 | -50.566 | 2025-10-30 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 257a71e3-75ac-3f1a-94b3-cee404a90b90 | -8.3313 | -47.9219 | 2025-10-30 02:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 09de71b4-7cbb-31d7-8e48-6c58856e39e6 | -3.8054 | -43.9002 | 2025-10-30 02:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 90a9b201-1be6-3194-a711-bd40da61c71e | -3.7867 | -43.9011 | 2025-10-30 02:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b2e66a25-2b37-3730-9de8-dfc99578888b | -7.804 | -46.4234 | 2025-10-30 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 08ea538b-6c8e-3bbd-ada3-7ad58dc84591 | -12.4947 | -50.5898 | 2025-10-30 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c357792e-be2c-36bd-8064-e709bb84f1f3 | -8.3313 | -47.9219 | 2025-10-30 03:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 97f9ee95-f64d-3a4b-95c6-24474226c3a0 | -12.5141 | -50.566 | 2025-10-30 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 09ab5790-fbbb-3c46-af11-49fe7f50dcea | -12.495 | -50.5684 | 2025-10-30 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |


[Clique aqui para ver as próximas entradas](README11.md)
