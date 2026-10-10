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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d9545aa-3979-3796-a0bf-e1f2b678c0cf | -14.53318 | -48.0415 | 2026-10-10 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fd5fcca-cb79-39ca-86d5-24b76ab9d9e4 | -5.08858 | -60.22047 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d7a813a-c7ee-3c4c-84f4-bd531c4f3da9 | -6.93584 | -59.24834 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39c37e2b-3e42-3f64-abb5-f48f9fe5561a | -11.73907 | -43.50402 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df0c3987-e7a9-3c13-a19e-757ac0927311 | -12.15127 | -55.42941 | 2026-10-10 04:46:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd5159c5-c7c2-3e6f-a025-621a3bd98431 | -6.49048 | -55.28976 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e57d777e-ad13-3fee-b027-021e71c7acbf | -13.52859 | -47.42443 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53d5ed4f-29c9-3b4c-8bdf-392fb1177e56 | -6.46186 | -55.05835 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 261e2c41-fd84-3ffc-85e4-1fa8fb52ce99 | -12.36689 | -46.60294 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 583cea82-0aa6-37eb-a9b4-6c3718ef2dbc | -9.83224 | -44.78205 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b6bc72a-5088-34ae-920e-7a23222d7ff1 | -6.49346 | -55.96931 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1694eca4-2e2e-385b-a608-c5ea86dc1a3a | -13.76953 | -48.13519 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92897158-bb5b-3416-b55b-a8968e66c589 | -7.56306 | -45.64563 | 2026-10-10 04:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ba6ab06-4ffe-3748-b5ca-d51c5ed9606d | -7.20233 | -55.14189 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99660456-912c-3272-a296-afbdf3788bf2 | -8.22708 | -46.38431 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2aa97ee-25c7-380f-a3b4-0b7d34bb47ef | -6.33554 | -55.31124 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5d8d88c-b541-3866-af08-c40265e4345e | -11.99189 | -43.50446 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c713870f-6b02-39dd-a56f-3fddbe943459 | -13.39533 | -43.8801 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7da6b9e-83d0-3e7d-8495-36c87e38c2e9 | -12.36161 | -46.58994 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9554c2f-7e1c-3fb5-9743-e14e38671c0e | -6.32148 | -55.33561 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37909b2c-cd3d-36cd-8206-6d950f844ab0 | -7.18145 | -46.53608 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5679d227-6da4-3d53-b190-6e9b7b70d35b | -11.37966 | -55.15754 | 2026-10-10 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 365743ac-b739-3757-a92a-883e86700666 | -7.38397 | -46.8908 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8be7f538-a795-3961-8d26-3f9653beca0b | -6.9437 | -59.10604 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2ce4ea8-22ed-35bb-aba9-3ffcb4949c78 | -12.37928 | -46.5681 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff81ba94-d2a6-301a-9882-1342918dd0de | -11.98768 | -43.5041 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abd5291b-f407-3816-83fd-b915d5cdb709 | -6.27398 | -55.26748 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d97a723-d5a4-38e6-8307-62c297ce19d7 | -9.51066 | -54.67266 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e49d6449-88a8-3508-a307-4f1d1a0197ee | -11.90201 | -46.56134 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15e3612a-d8f0-3d99-a840-760b2f862b10 | -12.73015 | -47.01355 | 2026-10-10 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6587057-b651-36e1-a2e2-23dad0c0da62 | -7.04277 | -47.66119 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58d6c876-5f50-38a6-a77b-144c027d4572 | -6.36989 | -55.16628 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e2d66b5-e52f-3e5e-8cd1-6f1e6022a48e | -5.88966 | -57.72142 | 2026-10-10 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0adf584-1549-3b70-8fb0-a133eb5c126c | -14.05844 | -43.82712 | 2026-10-10 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5ea32b0-1fe7-3d40-b1e3-30873e6fd068 | -6.01634 | -53.47476 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd00d33e-7536-3513-a273-0cec8ee6bdd6 | -12.93694 | -48.62288 | 2026-10-10 04:46:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd96d1a9-32da-38f3-b3d8-6b2b1ed1a92d | -13.10881 | -46.35723 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88126a28-b817-3482-8767-1c0c14cd1569 | -13.10343 | -46.34406 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7173ec29-2ff1-32d6-9490-7bff60b31561 | -8.64694 | -54.53912 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4a2be70-63c6-3ff6-a96b-8159c78e6ec2 | -5.07517 | -60.21799 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb007ffc-fbd2-39d5-87c0-8a158b9bb883 | -11.90798 | -46.56909 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82ae46c9-3438-3eae-973c-0393f3e81cfe | -8.49479 | -54.613 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7d84ea1-dc8b-3053-a233-6c45b33d3ddd | -9.31534 | -47.37701 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1dffe724-f5f9-3586-81db-edc2bfb49255 | -7.52837 | -45.31056 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 21ba6787-7171-3751-8064-e012c24e5829 | -11.09606 | -43.98765 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5beeea79-3d99-3c39-b712-14157c5291ad | -7.02948 | -47.6805 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17a00d2e-65d6-3c59-b1d4-aca95710f0d7 | -13.68839 | -49.13186 | 2026-10-10 04:46:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5ade8e4-5e24-38ae-ad7b-afc2991396eb | -6.44306 | -55.05491 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4ff44689-d7dc-31a6-bb66-9ae9be487896 | -6.4946 | -55.32249 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a3f4bb3-f795-39b1-921e-6974627f5e25 | -13.35854 | -43.90203 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4672e268-ceca-3f5a-9664-8edc1e864e3c | -10.59657 | -60.48363 | 2026-10-10 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fa336901-b750-3908-ba91-2835bedc53df | -9.29968 | -47.38916 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64d464aa-be7e-3584-b512-74d6d9b6084f | -11.75848 | -46.77901 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dfafd78-fbc2-37c7-8f57-2744e6dd5f3e | -8.76518 | -49.60475 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76bc9aaf-c984-3c4e-8844-9ac66c6e019b | -11.5771 | -45.40267 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8437cb7c-4bf5-3641-b113-1b3ab43d63b9 | -13.67786 | -49.11185 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ed7604d-2572-3fab-b51e-60c3b708b87f | -6.37352 | -55.17481 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc5599ff-92c5-33d5-9b41-88c73a2a9d7a | -9.29632 | -47.38863 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c885f34-8a74-3a44-a16f-55cacec61edf | -13.699 | -49.0861 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64c826b4-d575-360a-b7fb-02998d6ffbc0 | -13.37253 | -43.89227 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8e4e30c-f067-3cd8-900e-0ae036a9e8f4 | -5.85916 | -55.70094 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e82dc4fc-4044-3533-8a06-134846aae763 | -8.40452 | -46.90518 | 2026-10-10 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd43d038-e6f7-30d0-a002-83e56934001a | -11.98348 | -43.50372 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe027b0b-9adc-3544-90e7-08c1a70ed774 | -9.51583 | -54.66891 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab61cb9a-7adc-3d0b-ad01-9a7b08b92c1e | -6.34546 | -55.13869 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01dee52c-76c7-3b06-8809-71e86f5f94c0 | -9.8631 | -47.48442 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c0211ec-ae64-3305-931d-5ba275bffde0 | -10.95203 | -47.97805 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a6fe0f5-a193-380e-93c7-3718b84fb485 | -7.77723 | -42.31181 | 2026-10-10 04:46:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0fff128f-07d0-33b0-b36b-f46350e16bf3 | -8.36305 | -48.14644 | 2026-10-10 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5675a595-edc8-335b-90a8-5d1d6dd535e6 | -13.92122 | -47.84772 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a118d6b6-0129-36c7-b5a4-61c8d76cc5a6 | -6.43708 | -55.03356 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3756740e-f111-304e-b1d9-b0621e548fcd | -6.48549 | -55.95601 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ce4d821-9b00-3d7e-a82e-3635808c8691 | -6.37524 | -55.16467 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1c20ed8-cc93-350a-9b1a-284a4d2e8d90 | -11.38348 | -46.66136 | 2026-10-10 04:46:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bd3e336-79fc-3deb-867c-99a04c646ada | -6.38355 | -56.22223 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 516019da-704b-372e-ab82-93e83efd4be4 | -11.57338 | -45.40231 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dcbf01a-4362-35cb-94d2-665c17b9b1c9 | -8.2414 | -54.72366 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afc3f0fb-ec47-384c-a917-3922004f839f | -9.95651 | -55.11037 | 2026-10-10 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4fdedbe-78f1-3881-b323-b50d46504dc4 | -7.63355 | -45.37465 | 2026-10-10 04:46:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c2d58e7-bc76-3e73-80ba-04294b7309ae | -13.35338 | -43.90911 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 376db505-1554-3080-97be-72324b1a2373 | -14.45023 | -43.9429 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b26f6b8-a711-350a-a158-f040f89a22cf | -11.92773 | -46.7721 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 586fb1ff-8352-3991-895d-299b9ddf8cb5 | -13.35608 | -43.91073 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ac02290-af8f-348e-aa71-3afce38e2555 | -8.36327 | -44.20491 | 2026-10-10 04:46:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c8ff902-f128-321a-863e-72bc5ba44338 | -12.69447 | -43.07913 | 2026-10-10 04:46:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 81bf1156-07e1-3ebf-8cc2-2fc5fe7a326a | -9.87478 | -50.49247 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1fe4652-b152-35f6-a39b-4022302d0e88 | -7.2382 | -55.15735 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85caf93f-af15-37ae-9fe8-27c692662d07 | -8.4574 | -48.69919 | 2026-10-10 04:46:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7f33d9e-4414-3bd0-b2ad-a405a8e97e36 | -12.45691 | -46.52994 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d01915da-e688-3aff-b8e0-b8f1e0ee6a2d | -9.6298 | -48.87733 | 2026-10-10 04:46:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3d358401-36b2-3959-bdf4-796a9d01fb71 | -13.68562 | -49.12775 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2695528-9a63-391f-869c-6f981325d448 | -11.78799 | -46.72435 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c704123-4131-31f3-b26b-b4ebf65d888f | -9.93807 | -44.87437 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be3312d8-c9ec-307e-b6a1-a71f6b8c4279 | -6.4584 | -55.50044 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecb75067-d372-3b4b-a298-0a1ae04fe74b | -11.56363 | -43.70133 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35e6cdf9-d779-3223-bc48-787788cbcd66 | -8.58438 | -53.10354 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a759468-6c1a-3a0e-be62-95629ba5c934 | -13.635 | -44.42559 | 2026-10-10 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1312a699-8b84-3ea6-8ed0-0952c89387fc | -6.49894 | -55.38256 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6c91111-a4fc-3e5d-8611-26d0512d9bd2 | -12.41477 | -54.36216 | 2026-10-10 04:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9924e9c5-d288-3389-894c-de049132754e | -7.52653 | -45.3225 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README77.md)
