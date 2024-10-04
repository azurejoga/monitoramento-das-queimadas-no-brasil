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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 396e273f-7f7e-3888-a177-d333995cb3c7 | -7.05035 | -45.33455 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8bf09700-3ad1-3147-a9bd-39f5b58e56b5 | -7.03854 | -45.33708 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 330c4623-ff24-38ef-85ef-8f5b2773f6f2 | -6.93016 | -45.48421 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c304ceb-dc57-3223-a5db-07f48f0c92e4 | -6.92941 | -45.48867 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 828025f1-27e2-3905-90ce-92d6553a2db4 | -6.9285 | -45.48574 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 899da8c4-99cc-3516-bf4d-1e58c62bf54d | -6.92642 | -45.48362 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ddf279-1eb7-3686-8595-ff114d1ddd50 | -6.76176 | -45.65193 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f41c0cc0-476a-3de6-8f76-4c1233a41731 | -9.3346 | -46.56858 | 2024-10-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56d460f3-e169-306a-9807-52b3983c29fd | -9.33379 | -46.57343 | 2024-10-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38536f84-0208-3cdc-b227-f77b93bec5c6 | -9.33076 | -46.56791 | 2024-10-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa54a61b-07d7-3d97-ba3a-4cd472e243c5 | -8.93338 | -47.06201 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca167e01-28c6-3f2d-87d9-3946851b00f3 | -8.74986 | -46.81018 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c5a6ec5-873d-33ad-b5d2-0aeba826ac75 | -8.74901 | -46.81524 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6ebf050-106f-3399-974c-eb39d785a1b6 | -8.63388 | -46.51988 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 657baf7a-4e24-3b5e-a305-c043b9859bc3 | -8.63305 | -46.52476 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91044bad-1ce5-370b-a8f0-cad23ce6612b | -8.62224 | -46.51801 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed883592-25ed-3ebf-9113-56291b22a480 | -8.59811 | -46.51156 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db7ded31-fd23-3494-a8ed-7062a933c09c | -8.5973 | -46.51645 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5c69e42c-11ca-31ca-9e93-75b885c87d1a | -8.59424 | -46.51086 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ea86859f-3fe8-358c-9754-2e9d9fef49c9 | -8.59343 | -46.51573 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eb33bc14-563d-3502-97a8-447c6e8d0ec3 | -8.58957 | -46.515 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 71e859ca-56e1-33b6-a739-66a8be358367 | -8.58876 | -46.51983 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 947da2bd-f561-37b8-b149-b20b2ad9ef04 | -8.58489 | -46.51913 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3f228558-3e29-3b67-9006-1e389e069b96 | -8.58408 | -46.52401 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7c8c943e-65bb-37a1-8920-67d0ccad62c7 | -8.42889 | -46.44487 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c533c372-43d5-318b-bc4d-fe9be1fb1d74 | -8.42027 | -46.85413 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ba8ba96-1349-3cb3-bc5e-7999df4ba46e | -10.13392 | -46.34596 | 2024-10-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f0c91cd-1f4f-3ad7-ae52-9fd5a68d4ab6 | -10.13094 | -46.34069 | 2024-10-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b97cc04-4a9f-34e8-b280-a82d090f33de | -3.31805 | -46.98728 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25136d57-7b1a-3e38-a3bb-aba11859608f | -3.31735 | -46.99148 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 06e481ed-a9f3-3a15-a67f-4aea76b8bc09 | -3.31659 | -46.98732 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0bd2d2f-24a6-3650-9d04-dcb0b2c98416 | -3.31592 | -46.99153 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7e7be1e1-8a77-3e04-928d-4be8e0a0683b | -2.62484 | -46.91178 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba0f9c99-ac43-3c66-b1a4-6e68a2b53d2d | -2.62416 | -46.91601 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57854c69-492b-3f74-9272-2f6175f488a4 | -2.62047 | -46.91108 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d9b1791-4786-3621-87cb-ca6c9ed471d4 | -4.94296 | -47.1412 | 2024-10-04 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42eb01c3-263a-344f-ae12-d9a4efdb9de2 | -4.93867 | -47.14053 | 2024-10-04 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c77ceef5-d13a-3c1e-835e-1c9003236859 | -4.92762 | -46.79008 | 2024-10-04 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f4fb30c-568a-3076-8666-9442b0a1bda5 | -4.70646 | -47.20401 | 2024-10-04 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41ec975d-648c-38ef-aede-687019148c4d | -4.69496 | -46.75401 | 2024-10-04 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b51db160-90d0-3870-8b4b-0afba9a716b1 | -4.69076 | -46.75346 | 2024-10-04 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56f4d819-8feb-319f-9211-3853b6b71696 | -4.65375 | -47.43648 | 2024-10-04 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dac3c41-9142-3c25-abc4-92e4f0079e7c | -4.65319 | -47.43779 | 2024-10-04 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54ef9cbe-eadd-36b4-b664-7c15fac10059 | -4.55615 | -46.4073 | 2024-10-04 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f1bc405-1227-3a09-836f-8d30bd06d51f | -4.13279 | -46.71241 | 2024-10-04 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 028138d9-e6f6-3e0d-aaf2-1148ba2462c8 | -4.12858 | -46.7117 | 2024-10-04 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f0dbb17-9c1b-33f5-b19b-80f6aa57fbdd | -3.92491 | -46.43862 | 2024-10-04 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 480ba2c8-3b17-34d1-9a84-2d6e7956bc10 | -3.92431 | -46.44235 | 2024-10-04 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e119a5-c067-3fcf-92f5-911a96810506 | -5.60157 | -47.95913 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c9c77245-06ba-32d2-88eb-c609d716bede | -5.50975 | -46.47859 | 2024-10-04 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fa9c773-9a32-3c91-a9e4-589f6ccaf1e0 | -5.46532 | -47.37016 | 2024-10-04 04:08:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b9c219f-fd75-3a4d-ae18-fc8991ec99c3 | -5.4639 | -47.14473 | 2024-10-04 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47689ba3-6922-3c38-a0f6-108fa0aa8ebc | -5.4011 | -46.57973 | 2024-10-04 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcd9a42d-15e1-3fb6-8188-18a832e8399c | -5.39701 | -46.57907 | 2024-10-04 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b531b5de-a161-3f2b-8776-fb3306b7627c | -5.31343 | -47.26971 | 2024-10-04 04:08:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 481e7183-7c85-3087-8593-dd8f80e1ae0e | -5.31048 | -47.26084 | 2024-10-04 04:08:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd10efa4-a2ab-34d5-ac07-e6754089b28c | -5.30981 | -47.26494 | 2024-10-04 04:08:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38adda30-3b19-32fd-a635-5a8c18c38e61 | -5.28744 | -47.32037 | 2024-10-04 04:08:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea7041f9-0846-3e25-99a9-2c2cfb1f6ffb | -5.28677 | -47.32443 | 2024-10-04 04:08:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc43a2c3-8a29-3c54-b022-adea1506cddd | -7.80414 | -47.47309 | 2024-10-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62487041-216f-328d-9f1a-cbf91bc1424a | -6.89607 | -47.23519 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0833f300-b992-394a-8a83-dcdf9484b04b | -6.89541 | -47.23904 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6dde5ac1-e9bb-3b5a-aa16-6700bd5bba76 | -6.8919 | -47.23446 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7135bc3-9b93-305b-908f-942c8e7680b5 | -6.89125 | -47.23829 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fb6fda36-ad03-3c08-993d-e9d08dc039b4 | -6.79717 | -47.25408 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae8a577-6e84-3ae3-bc73-0deea79815b7 | -6.72923 | -47.94865 | 2024-10-04 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cbc828b-51f8-3e39-bf4c-e1d7a7d9c3fb | -6.72906 | -47.94886 | 2024-10-04 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10ea71c7-6ed8-3965-b5a4-9520d090850d | -6.7285 | -47.95287 | 2024-10-04 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 994fe42d-c404-3ea6-8b35-b68726918b4a | -6.72835 | -47.95309 | 2024-10-04 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6d54b9b-c46f-3ea1-b856-58f7a47b4708 | -6.72625 | -46.95433 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 917ebbbe-8f81-3008-810d-af050f7b7e7d | -6.72562 | -46.95806 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60027468-7045-3b17-ba73-03e6070f55eb | -6.72214 | -46.95367 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b534e3f-b50b-3287-a70c-fe1e5ce3a845 | -6.72151 | -46.95742 | 2024-10-04 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51926be7-9952-3de1-a860-cdbd0749b08e | -6.51505 | -47.82275 | 2024-10-04 04:08:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d4f9b36-39ba-35ad-98f5-f9989c8ce8da | -8.83163 | -48.30365 | 2024-10-04 04:08:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64186332-a194-3a82-91dd-3e3b1f9c6401 | -8.82729 | -48.30291 | 2024-10-04 04:08:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c296922f-79cd-3ef7-9153-bbf416ceb81f | -8.59091 | -47.13345 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5400634-d2b0-3633-bd0a-f4dc68948732 | -8.59031 | -47.13702 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97aa2c00-a681-3b1f-b259-bb478f8a21e0 | -8.58688 | -47.13277 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70225afc-ab89-3952-b86b-87d8f2ee6063 | -8.53698 | -47.15751 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 502fa584-9c58-33f8-ad6c-032a9d398254 | -8.53638 | -47.16104 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dc46b8b-2c75-32d9-b4ee-e4a12d48f203 | -8.53576 | -47.16462 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37ec4866-6784-305f-9028-e5e2b4d67706 | -8.53354 | -47.15332 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 336633d0-23fb-3a19-88f8-083332545586 | -8.53293 | -47.15688 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef48dbb7-f3c6-3676-83bf-ee62df99a627 | -8.52398 | -47.23322 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6ba6d24-4835-3569-b230-d4a9111f8bbc | -8.51992 | -47.23252 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 69722998-7a09-3017-bb88-be7a25581da6 | -8.51585 | -47.23187 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2677af3d-aad1-3ff3-8d14-26da99afe2f6 | -8.51114 | -47.23489 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80f1756f-4532-3e5f-be6c-498af323bcf6 | -8.51081 | -47.30981 | 2024-10-04 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85f13383-cfe9-304b-9664-c817321168eb | -8.50673 | -47.30912 | 2024-10-04 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f639dd8-8b10-32a9-836b-3e21d0ebc1c8 | -8.50203 | -47.31199 | 2024-10-04 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c5a86db-3f6f-37ab-9cb8-0ba875926c48 | -8.47561 | -47.22163 | 2024-10-04 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7f82aef-486f-32ff-96c7-d05ae6b695cf | -8.45903 | -47.12231 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae11961-59d5-38c8-b2d3-819ac8fdbe21 | -8.45561 | -47.118 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58f1c7fc-8115-3195-9ca8-1c1b6adf5237 | -8.43948 | -47.11511 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e99e35b-186e-3c91-a978-46606748d029 | -8.43729 | -47.10364 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3000bc9-f30c-37ba-9591-9c1c21acdb2b | -8.43668 | -47.10724 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a965da57-27a6-386c-96e9-5256c82b4fda | -8.43544 | -47.11447 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 938821bc-18eb-332c-98bb-8c47023f32a4 | -8.432 | -47.11026 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 939fc2cf-51f2-36df-b1e4-c7e577411556 | -8.43138 | -47.11389 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README63.md)
