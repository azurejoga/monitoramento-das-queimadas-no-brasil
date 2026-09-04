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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0fdbaf6-9cb8-3508-ab5c-e929c7a6375b | -8.44317 | -54.68197 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27155489-9b42-3235-835e-7e204eb00c59 | -7.72753 | -61.12407 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7245857-a334-3fde-b12c-df15af848226 | -6.67158 | -60.01939 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c11f9e7c-dc3a-318a-8bd3-8ca630e5f167 | -7.55923 | -61.34985 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 33e66cb6-26f5-3c8b-aad1-bd89727fd276 | -8.48731 | -54.65681 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e58202a2-165a-3bce-9171-68702c132877 | -0.93144 | -47.19037 | 2026-09-04 05:23:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a70ad4e4-647e-340a-98a9-e5b0641df454 | -7.27786 | -64.5503 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aee1761-98af-3c95-8187-5cac3754595e | -6.56894 | -58.98142 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 718cac26-ef40-3113-bfb0-641e7fffb7f0 | -10.49917 | -51.33488 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b87d7de-9e15-3785-835c-0011f384f228 | -8.10722 | -54.77624 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f972e39-69da-3381-ab3a-d6f4b97aa409 | -8.92801 | -62.35687 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 493022a6-5d87-310c-b78c-b38189126c27 | -6.69137 | -59.97954 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 76e98a06-47df-3947-96f7-42f749cf813f | -6.69361 | -59.98703 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6845f28f-9c19-3976-8616-7ffe1747532a | -2.7603 | -49.47834 | 2026-09-04 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6bfaffa-09b5-351b-b533-c95f0aa45d3a | -8.44228 | -54.6927 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41ce2cb7-f9bd-3bc2-a34d-d5f1892f4962 | -3.08342 | -61.08627 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9389f97f-d7ac-3d79-8532-b8edd0007ae3 | -7.57048 | -61.21302 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cddc7df-a1b7-300a-9367-459b374432d6 | -3.19754 | -61.20587 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379c7917-2301-307d-8e46-78e07b2a0498 | -3.08235 | -61.18024 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96f73d70-c6fa-3db7-9d53-6d280e6d8406 | -6.71194 | -62.86874 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62ee1934-dacc-3709-b87b-7cb526f86a36 | -6.67854 | -59.9525 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddabbfcb-9446-3795-a967-397c71a02bd8 | -10.00694 | -50.28507 | 2026-09-04 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b82665a-c7b4-3021-8524-393016072cf7 | -6.99952 | -62.97964 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fa8e693-c1a6-3beb-9c83-aeed134b3fe2 | -10.50113 | -51.33172 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7d563769-0553-39f5-ae12-a535522ceb3f | -3.62913 | -54.59494 | 2026-09-04 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 119079c6-4e19-3bfe-8026-0740f61b718d | -3.90167 | -52.04928 | 2026-09-04 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f238b149-7aee-38c7-8c24-3fdfa8fc9e84 | -3.103 | -60.20335 | 2026-09-04 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b8ee8bc-23da-3c2d-9512-34d75a07eb5c | -4.11325 | -51.03032 | 2026-09-04 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 911d30ca-cb3e-354d-9b3a-a641553e0b7c | -6.69029 | -59.98651 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 52ed3adb-5d56-3ca5-9bd6-eb60a21fed7b | -6.70688 | -62.85635 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d735356-df9b-389f-bb50-7a498ab84695 | -7.55809 | -61.33549 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 824590c1-fadd-34fb-bca1-3f542bdfac64 | -3.14375 | -60.63744 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9191693-945b-3762-804a-294d25df6d6e | -8.76629 | -62.82977 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8858740d-196d-3e04-a943-2c71a1b55b9b | 2.44699 | -60.76066 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69fb1dd0-aac2-357e-b73d-95f858639a77 | -1.50731 | -55.68716 | 2026-09-04 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0f4f25e2-b17e-32e6-8165-f95bef8b90f7 | -6.11942 | -59.96239 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd74cfe1-04e4-3d82-93ec-85bbb4612689 | -3.34196 | -59.45478 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce17cd49-ea71-32aa-9d0e-910af58bfc65 | -3.14707 | -60.63795 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 928fd161-8e7c-36ec-a03f-917ef92de342 | -8.1142 | -54.78715 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f35b0642-81a0-3aa4-9d8e-e7c5cbf84f84 | -1.2767 | -60.33075 | 2026-09-04 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4085f6c1-b949-3919-a9a9-9795a3767529 | -8.49741 | -54.64931 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e691b43c-c73c-3093-85dc-b047f0e6d019 | -7.7962 | -62.3478 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c48e5e46-68d7-3e26-8d97-226620dbd33b | -7.02304 | -62.98728 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04bcfffd-c452-3e57-8be8-271238165418 | -6.88501 | -59.40833 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b166f80f-7094-3c49-b84c-d26b60995ee4 | -8.78462 | -62.48792 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 642b152e-b0bf-3e1a-b601-1729a27b23ee | -7.78777 | -63.38995 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67fafd66-6787-30c7-a698-b875e1d682ee | -6.68079 | -58.75172 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de9cf31-eb09-3b6b-8409-2a6a6592d1bc | -6.1374 | -59.89023 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7474a91b-2646-3819-96ba-0073db8cdde7 | -2.41042 | -57.89911 | 2026-09-04 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 795aed6d-e673-3e86-9b74-ca79e76ae1f2 | -2.7608 | -49.47302 | 2026-09-04 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 193a8e3f-7ebf-373d-84b6-168ddaf8955a | -7.55839 | -61.22533 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28aea9f1-1855-3b18-99c3-bb767bcc2eaa | -7.01959 | -62.98673 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7264dbe9-4087-32a9-8cab-d81126f31497 | -6.68016 | -59.94201 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2bcdc48-a673-3ffe-9308-b25b68d224e6 | -6.15416 | -59.93564 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 307f168b-dae9-328b-80a6-79eaadb3e7f4 | -8.80267 | -62.8844 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b092a925-5dd5-33b1-b0f6-473c368b4699 | 2.44414 | -60.76492 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af34d123-639d-3b8c-bcd7-b7aba56b28ed | -6.76553 | -59.43368 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e394edb-a432-3b11-bfa6-15bdd3ffb830 | -6.8802 | -56.50659 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cbc7755-2b15-3f6a-aa22-b5647aae27a4 | -8.49802 | -54.64489 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b2246f7b-144d-3a8c-b545-f0478798fe76 | -7.38847 | -72.80202 | 2026-09-04 05:23:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a02da024-10ca-338f-90c9-bfa184d41076 | -6.70972 | -62.86066 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48a7edeb-785b-3762-a233-e88f26a46be4 | -3.07729 | -61.08169 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc734a8b-891a-30be-bb29-075608e875ea | -8.71122 | -62.9492 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 481626cc-a7f8-3678-ac77-3ecf1b128970 | -3.0261 | -61.49376 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86f87540-0c56-3c40-b23a-def668e053d5 | -6.71078 | -63.18583 | 2026-09-04 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fa95aaf-2132-359f-8f8a-084e8ba23001 | 2.45445 | -60.76337 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d7d1fa-10a0-3f66-bf48-55281974b725 | -6.67243 | -59.94799 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6b2fb5a0-a021-3a24-82c4-70e457e83db4 | -8.44168 | -54.69697 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60621e37-e9ec-3e2b-bfff-f1f0f8bae43a | -7.59027 | -61.19481 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d7e3ee9-13ec-3174-b25a-c7f83aec627c | -3.16681 | -61.13951 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2ff277-a22d-3624-9dbc-8f2cc480b2a9 | -1.0371 | -53.72493 | 2026-09-04 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce09f79-4d4c-3502-8b04-972d7513c41d | -7.74009 | -67.06658 | 2026-09-04 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b17e96cb-b235-33c5-8bb5-7a1111f7cb0d | -6.973 | -59.78232 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ebc06b-6e3d-3c25-a699-28c7dab0748c | -8.50063 | -54.65882 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7f293795-4220-3211-ab4c-934ed2d51239 | -6.68635 | -59.96802 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a7c813a3-742a-3cb6-9c15-ba51b83f532f | -3.34581 | -59.45182 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63bbbfbd-9cad-36aa-bd83-33d1b3416a86 | -7.54866 | -61.3091 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b23452f4-f3a1-3e6e-9bd3-0636785b5158 | -7.98394 | -61.15783 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5145431-8696-3fe8-b395-4de3f6abd897 | -6.6408 | -59.44771 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9d77bd4-20b4-3abb-9365-6779648b9f11 | -10.63734 | -50.38738 | 2026-09-04 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3602c8e5-e18f-346c-bbbe-7db76140daed | -6.14072 | -59.89075 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97a806c8-68fa-397b-9886-a377d37e45b6 | -6.37636 | -58.28836 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adf56ed5-e34a-3a64-ba08-e50d58e0bf28 | -8.10921 | -54.79078 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 47248827-1002-3bf2-992c-49f89f3485e8 | -3.02215 | -61.49684 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f02d73-7265-30b6-9222-8e83433d4a97 | -7.46925 | -63.74844 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 526c6b97-bb16-3f82-bc07-95661d85d929 | -1.48241 | -55.54549 | 2026-09-04 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 717cf4dd-c8fd-3ebb-80fa-210393a753f7 | -6.14698 | -59.93811 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a8c4fc5-afd9-3538-a350-7ff4aedab433 | -6.35804 | -65.48948 | 2026-09-04 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc04bc22-7f33-358f-a940-c078aa307a52 | -9.44214 | -56.73299 | 2026-09-04 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b53424f-b361-3633-992c-1d17c2711ebf | -8.19057 | -62.80148 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fbe6117-9241-3507-b0df-e2473f65e276 | -8.88122 | -62.34937 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca3b357-d3ff-3e52-aa8c-c6b1e8e78ac1 | -6.6791 | -58.76297 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3b315d4-5333-38af-9c9f-86662c64d3de | -6.68024 | -59.9635 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cc8b5b7a-93c4-328d-88e9-8a7256a31a69 | -3.15711 | -58.65216 | 2026-09-04 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 569bda12-bce2-38ab-84c2-2fb8738490a3 | -3.17909 | -61.14865 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70018772-cec4-362d-8ff1-6201e71b5683 | -7.46636 | -63.74383 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbdaaaf5-190f-3309-a403-4dc3e4070ea9 | -6.9758 | -59.78635 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c12cd0a-b472-3d74-ae62-e4460278f951 | -6.68194 | -59.97451 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79578e71-140a-3587-8767-c22b4c83583f | -8.57094 | -63.19019 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de5c8352-b35f-3f6a-8713-1c98526c992b | -8.10606 | -54.78156 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README27.md)
