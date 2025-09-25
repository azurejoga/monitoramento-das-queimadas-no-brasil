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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22bb7fa6-6cf0-3901-b836-073a02ffb802 | -3.82907 | -50.97561 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 060f731a-5997-30cb-aaa4-43ced0c86116 | -15.36561 | -59.17465 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31c0a4b4-a644-37dc-93a0-fced46800c46 | -15.28461 | -59.43017 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3d30abf-e664-31c7-9259-e4f8e603f618 | -15.87071 | -59.34628 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce9bf76d-4297-3940-b9aa-4cfbb0ba3b13 | -15.77135 | -59.50063 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| feb56c27-5273-3294-a08a-238ec857e595 | -2.70474 | -54.65471 | 2025-09-25 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09d95c27-0eda-3d98-adfe-99f6a4a9e593 | -3.36754 | -59.49872 | 2025-09-25 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01a191c9-b567-397f-aa35-83ffd38eb5f6 | -15.87435 | -59.34676 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01050a57-759e-3fc4-8408-4118084ce7f0 | -3.51351 | -60.42551 | 2025-09-25 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 161e3a01-9564-337b-98d5-f68df97dd9b8 | -15.86709 | -59.34568 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d875e61-824d-34de-9086-4f1cd009287c | -15.76898 | -59.48002 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b2c5ca2-4958-3652-b670-75c489de245e | -15.2577 | -59.43884 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa27905b-28f6-3db4-80b3-26f1d614599a | -15.76835 | -59.4958 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 606df766-833f-3a7f-986b-1e1a1c51fbea | -15.75933 | -59.49583 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3f7eb53-3d84-3567-a83f-69cd409f89e5 | -3.61838 | -51.79884 | 2025-09-25 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc1761c3-8e43-3148-8121-cab28545aaf5 | -15.88393 | -59.38314 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80e69d61-19eb-3a94-b832-3cbda9a7b8f2 | -3.82882 | -50.97926 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a92bd94c-3db2-3eb7-97b0-a3e5f7e59693 | -3.61694 | -51.80302 | 2025-09-25 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6bbf6f2-f0b1-3ca6-b810-d1e463ed5354 | -15.81032 | -59.48503 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed4cacca-2380-3e2c-8900-912261490570 | -15.36623 | -59.17033 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 870c506d-26ca-3fee-8554-4366830d30c8 | -16.85664 | -50.51222 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a47daf68-e123-3076-8c85-eb4a1d9a8af5 | -15.75756 | -59.48272 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c7eb3f2a-eb19-3121-8e81-c00a4d350a76 | -15.82635 | -59.60381 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a106f9fe-9991-393c-807c-ab739904a4a8 | -3.08397 | -52.91711 | 2025-09-25 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c94fe50-92a0-3fda-8d52-06b34d36de55 | -15.76537 | -59.47958 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 197bc4d0-ac41-3fd4-9d1d-8403d2097362 | -15.77125 | -59.46428 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0272903b-f49f-319a-8696-da9c58ef8f54 | -15.14709 | -56.45287 | 2025-09-25 05:23:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93da1e4d-335d-3c75-814d-324e100871f7 | -15.8816 | -59.34788 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8281c7eb-0b82-3c29-be73-4a8efa4d6733 | -15.14655 | -56.45699 | 2025-09-25 05:23:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99697db5-0a03-3a82-b4e8-dc30f78588d2 | -4.20243 | -55.15529 | 2025-09-25 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fd8a4e0-b241-3376-9b52-22209a0458b2 | -15.76716 | -59.49261 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 348d0430-b1f2-3219-8080-73d08a04a325 | -15.3437 | -59.19782 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6184c23-bee9-3ad0-80e2-1cef83f4c782 | -2.38217 | -57.24356 | 2025-09-25 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a6aba5f-0f75-30b2-81ab-75ae64b2c490 | -15.83953 | -59.58862 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ba052d3-56ba-35b9-b617-f63a2e88e452 | -15.76294 | -59.49632 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| babf25c8-acd4-39d6-aaea-90fc2858635b | -9.56137 | -47.53445 | 2025-09-25 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9951dd0-f474-3630-9f88-1302e908b80d | -15.7707 | -59.46811 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26bfa01e-7b75-34a9-bab0-33e0bd811157 | -16.84816 | -50.51963 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70ed9703-f13b-3e12-adbc-04193e382e63 | -15.82696 | -59.5996 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ecc4b9-1313-3eeb-a3e8-e2ca66cb3c86 | -3.11126 | -59.44422 | 2025-09-25 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e26b33bc-b282-384f-8aa7-23a3ccf58b96 | -15.2774 | -59.42925 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3c43e6f-c1c4-3375-a527-6b71699c9da9 | -15.75635 | -59.49107 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97150e26-b244-3efb-9664-7edf38719a2a | -15.24999 | -59.44154 | 2025-09-25 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0145e1b2-0d3c-301a-99a9-f6af2920e085 | -3.4951 | -59.0546 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe8463de-0a4f-3e39-86d5-30391723872c | -15.76176 | -59.47911 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bcffbda2-f6d5-3f91-99ca-72bcd82ac2be | -4.80288 | -47.27646 | 2025-09-25 05:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 470d6cb9-0cda-3fde-8652-7942b33bb5e7 | -15.76533 | -59.50518 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7cd8d186-0014-378b-812d-4cd37921621f | -15.77194 | -59.49636 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b355047e-e185-3e24-bd6c-99af70e8b6ae | -2.38277 | -57.23972 | 2025-09-25 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 258637fe-8db8-30c6-9144-8ced29c7a6b9 | -15.80309 | -59.48409 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 840c6411-d640-3eea-82ea-122913049168 | -15.75336 | -59.48634 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8c10a4a0-c394-37db-8af5-447a80040ae2 | -9.56844 | -47.53529 | 2025-09-25 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c5508f0-0985-3630-aaa6-6fa4b251d162 | -3.03954 | -59.29589 | 2025-09-25 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b77d4ecc-0855-3c1d-8a4d-6306e18bd5f9 | -3.61779 | -51.79747 | 2025-09-25 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d265a5-acfc-390a-9b09-c49c2d77ee6e | -3.76303 | -59.31653 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4efd0b8-e9a0-3f53-82c4-45163ca1108f | -15.35709 | -59.18217 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54f10e4c-329f-30b5-81a7-65e916d05f05 | -3.82979 | -50.97284 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e1445a4-b328-3271-b8a0-1e30fd60c93b | -15.36197 | -59.17411 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3b69faa-8d4c-35c8-b1c5-05e32a8d172c | -15.15136 | -56.45347 | 2025-09-25 05:23:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f1d297f1-c32b-35fa-b897-1d17012d4bfa | -15.7989 | -59.48774 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a077e0d-37d8-36e7-a1a9-47c68cc11e15 | -3.83046 | -50.96588 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6da9983-c3b1-3aac-a89c-cd6604a69396 | -3.21092 | -54.96075 | 2025-09-25 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f1ea8f0-9272-3f15-a86b-41ca5441fcf5 | -15.76116 | -59.48324 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9b94b7d8-cf7f-33b8-bd24-7b0e76429a7b | -15.80368 | -59.47992 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4479af01-28a8-3f59-8619-32c0f6fb1b47 | -15.75275 | -59.49055 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c029dc0-70f2-3fe3-8cce-ac5e0db9c801 | -15.76651 | -59.47167 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 299ebdb8-81a3-3c36-b218-f632afac1a67 | -15.77076 | -59.49313 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7c957161-01e0-311f-a646-76fa341d39fa | -16.84921 | -50.52205 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0b08a227-37f9-3a27-82b0-b5bb41869100 | -15.88946 | -59.34477 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 50324727-8c3b-30a7-8f32-5fa482443858 | -3.08782 | -52.92243 | 2025-09-25 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd651247-4d21-373b-a712-a31ff54cabfc | -15.28044 | -59.43366 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09467e0d-498e-32f6-b33b-6e34cdd709c4 | -15.281 | -59.42973 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43308f48-4a1e-3caa-b5e3-b393e5242c34 | -15.83831 | -59.59704 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 431573ab-7d8b-3de6-bced-f21d872a0893 | -15.77254 | -59.49212 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c6cb315-aca0-36f0-b002-1079681760c4 | -3.76026 | -59.31255 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e73d8e3c-a83f-3893-9a1f-6594a57520fb | -15.35346 | -59.18161 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a8a5c9c-9a9b-3e99-a971-4cd890ad8d5b | -15.82574 | -59.60802 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad502469-dc14-3ccb-8fdd-6d379a0dc50b | -15.76894 | -59.49158 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c0e5539-f5fc-3116-85c9-57c629d2da1b | -3.08852 | -52.91782 | 2025-09-25 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94b392ba-4d70-356d-97ba-289f85078f99 | -21.97733 | -49.51056 | 2025-09-25 05:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ffee58aa-065f-3f38-a4cf-0663a0975d17 | -15.96688 | -59.50616 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ce8777d-bbf6-3439-8824-5b3282cc6c15 | -17.92948 | -55.86163 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 645c9b06-a949-3042-a2d3-14bb1b18445e | -20.99263 | -50.47906 | 2025-09-25 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 190da128-65fe-373f-8804-59fcef058b85 | -15.90487 | -59.39745 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0a1e631-5761-31ec-9acd-ddd52560b9f3 | -20.98637 | -50.47256 | 2025-09-25 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| dcff3250-3f9a-340e-935e-5a4cdf7444cc | -15.90425 | -59.34884 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0f8f098-d498-35c6-93dd-275981f6c4e3 | -20.98658 | -50.02173 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c8063f30-7bc9-36a2-ba6d-1c1b91410ed9 | -20.97912 | -50.02684 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| b81f844c-65c9-3004-b5a5-6cb2ce070307 | -15.93077 | -59.42342 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dfd26da-8eb7-3a5c-b93a-121ef153bf8d | -17.93813 | -55.86779 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 88cb00e7-091e-37e5-9d7e-598944ff1c8e | -18.18405 | -53.32925 | 2025-09-25 05:25:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd0df026-696a-3ceb-8d30-14c23e9ac3e3 | -16.0038 | -59.48979 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0de99c6f-7d58-3e52-b448-3853d5fad7c4 | -15.96565 | -59.5147 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 665ec946-7fea-3876-86c1-c4d5bacdfd7c | -21.97786 | -49.50341 | 2025-09-25 05:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 2dcab74b-af51-39f6-8fde-03896efbd704 | -20.99289 | -50.02856 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 302f437d-1eca-31b7-90e3-6f1e71f73ab8 | -20.99449 | -50.00986 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5bd367e0-e4cb-3698-abbe-641610e60160 | -20.77804 | -56.91926 | 2025-09-25 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a802c043-1116-31e6-abc3-6ecdb4578b09 | -21.0014 | -50.01035 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9cc6afd3-d236-3d17-82be-c63a18847bb8 | -22.36376 | -54.64336 | 2025-09-25 05:25:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f120ca53-757e-35e7-a945-b4581540c5f1 | -20.97919 | -50.02725 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |


[Clique aqui para ver as próximas entradas](README36.md)
