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
| 466c0529-11d4-3e48-92fe-76d5b8d9dd72 | -10.13706 | -52.13684 | 2025-06-24 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d4e77f-5e03-3fab-b68a-5631f8dee46e | -7.32723 | -43.21775 | 2025-06-24 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1eee1fda-e66f-3a9f-a756-73241dcc5549 | -12.40379 | -43.80142 | 2025-06-24 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4eb0952d-bf56-3727-97b3-c9f069b31dde | -10.59685 | -49.45897 | 2025-06-24 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0526ebb-9f5a-32b3-8d5b-97851221ba41 | -10.41628 | -47.88245 | 2025-06-24 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39c5f72c-a100-3d0d-801b-ba31e606467a | -6.17026 | -47.27604 | 2025-06-24 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3927938-7d43-3183-8397-4748149f6dd9 | -12.2486 | -46.68439 | 2025-06-24 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15bfdd6e-e33e-3ab4-9d9b-9efe97fa46a4 | -8.57066 | -51.55022 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6431384d-8327-306f-a2cb-579ee1cd3f8c | -10.59674 | -49.64453 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a455ba85-198d-3e56-8b1a-0c3acc74e51e | -8.98894 | -49.86785 | 2025-06-24 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0558b21f-6dbb-3fae-84c8-2dd8f3f988d0 | -9.13498 | -47.58512 | 2025-06-24 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f79568f-420b-3c35-b355-f128b4914a0f | -10.65115 | -44.49192 | 2025-06-24 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 096cb1fb-ded1-345c-bc39-49612fbaab4f | -8.0678 | -43.11091 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 070d1ced-e71f-35f0-b1f1-62324e69a2f1 | -6.40114 | -47.33796 | 2025-06-24 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 32247696-1a21-38b9-9d8b-2d0e44729ec9 | -7.19928 | -43.09946 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fae3d778-8653-3c15-8c68-5d9082b6d19b | -11.10023 | -46.64534 | 2025-06-24 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ea8030f-d1cd-3be9-add1-ab1b68fd9514 | -7.19864 | -43.10372 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c9691e1f-017b-3b3b-9e7b-a993d611dcdb | -7.34347 | -45.34798 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fd6ccbb-f9e4-39a8-9d40-53806a818ed7 | -6.96002 | -42.92776 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0582eb42-b772-3fca-8c73-c521252df699 | -7.85805 | -47.1109 | 2025-06-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f529cb9-78d2-3e8a-9520-5bd87ff7c052 | -9.40274 | -40.31824 | 2025-06-24 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 220d82f2-cf4c-3fd4-abce-f08c85ee6cc0 | -9.68884 | -48.20115 | 2025-06-24 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61192749-a395-3ddb-9631-365bda5be5b1 | -10.14751 | -48.98672 | 2025-06-24 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 797c00b1-f95c-3371-84c2-a01bc5046985 | -10.59622 | -49.46281 | 2025-06-24 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c8e7884c-39ac-320b-8c94-9ce1df125758 | -8.56016 | -51.56408 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cf13670-67e5-3696-bdbc-1e2ade481ea7 | -10.95268 | -48.22413 | 2025-06-24 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19528d25-0e53-338e-8c3f-2d33071ccab9 | -9.68157 | -48.20362 | 2025-06-24 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87455dfb-1797-3731-af35-60119be46ea1 | -10.28315 | -47.60947 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f911bc19-d1cf-3f2f-b148-b0234a684da6 | -8.24519 | -44.95667 | 2025-06-24 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f3971f9-6465-30c5-8b17-8862c074e797 | -10.23951 | -44.63622 | 2025-06-24 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6914a218-b90d-3158-86ab-59a0f3e4e6c9 | -10.05534 | -48.66857 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ff4b644-cadb-3d38-882e-72f886953f35 | -8.5698 | -51.55526 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2779aa50-bc25-338d-837f-6db646c56cb2 | -6.95419 | -44.03341 | 2025-06-24 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec01c0fa-07ef-3a7b-ac57-52fdf7497004 | -11.61053 | -47.61623 | 2025-06-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86959f57-a8fe-356b-8079-9ec9e091f352 | -7.43588 | -45.5186 | 2025-06-24 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3cafc4b7-9563-3b6b-8712-330badef7aa3 | -10.49891 | -53.57125 | 2025-06-24 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61e0f0b8-1092-3448-9173-2db3a5a4d512 | -9.40099 | -40.31522 | 2025-06-24 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbce1a43-825c-3cef-86c8-ef173f5b93b9 | -10.65469 | -44.49246 | 2025-06-24 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38545d7e-2499-3e9b-b7d6-9db0020df29d | -13.07084 | -48.83392 | 2025-06-24 04:25:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 162433de-0705-3288-be37-c97d83e1a6b9 | -6.95206 | -42.80612 | 2025-06-24 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2f08d739-3ccf-3116-a815-762e7c62d298 | -11.56852 | -47.42942 | 2025-06-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63a54745-40fb-360c-9507-005980e12dec | -8.56672 | -51.54952 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 487fde56-f225-3f5c-919c-5465af562c05 | -7.91243 | -49.64563 | 2025-06-24 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10e47f44-7587-32c1-a848-e4fb73ecd251 | -7.86146 | -46.6604 | 2025-06-24 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1da22f4-e5f3-3c36-946a-65006e612554 | -10.07736 | -52.74112 | 2025-06-24 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 09d1c705-1bb5-3da3-b4f5-53f151ea7260 | -10.27928 | -47.61243 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6427717-64a2-3a90-8d77-51fae58777ce | -11.09636 | -46.64833 | 2025-06-24 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 435b585d-73c4-3a5b-90da-f5eaa472b9e5 | -9.29313 | -50.42942 | 2025-06-24 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3375dc4b-327d-3e18-958a-75a0b69d88dc | -8.70502 | -50.04501 | 2025-06-24 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de605248-28cd-37f6-b48f-0d3b7e7cb26c | -12.3226 | -50.05923 | 2025-06-24 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9579cd96-8fce-3ac2-8bbb-2df139997e25 | -11.2 | -49.01029 | 2025-06-24 04:25:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42a82ddd-f7d9-3a93-bb74-fb7e430463f8 | -7.45192 | -45.56434 | 2025-06-24 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b704547-541f-30dc-8ee0-7d6a72b139bc | -9.12835 | -47.58404 | 2025-06-24 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14971c62-663e-37b1-b732-1a403c133577 | -8.24235 | -44.95244 | 2025-06-24 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46891b04-5d80-3608-a020-0bbcbe322c75 | -12.28682 | -48.80424 | 2025-06-24 04:25:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f65eb14-e63a-31cb-bb3b-ef7b1929e795 | -8.55622 | -51.5634 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aebff26-abef-3943-afdc-a5f1cdd518a0 | -8.37089 | -47.43314 | 2025-06-24 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4f80855-6f4e-36ff-b98d-a97beeab2794 | -8.81895 | -45.00546 | 2025-06-24 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4f0b9ee-6738-32d2-8777-fed5556295a6 | -10.59491 | -49.64538 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47b4b1de-0a86-3e7e-be2b-34c0703b8b6a | -10.47339 | -47.00635 | 2025-06-24 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bb34aab-dcee-3916-952e-c41d207bfbac | -10.59261 | -49.64783 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ccd4f4e-2fac-39d2-9e4c-6d16ee2ac9b1 | -7.31442 | -45.77309 | 2025-06-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f1be0a-3911-3b29-a622-fbd49123eeb0 | -8.06347 | -43.11474 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c2f78580-af3d-3b49-9092-5b481e8cf7bd | -13.95213 | -45.05055 | 2025-06-24 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3df2a75b-ab94-3e54-8e61-f170ed00dde9 | -13.55149 | -44.0924 | 2025-06-24 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38e3c099-c239-3480-abcd-dfc038ead254 | -7.24215 | -47.07344 | 2025-06-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ed746ba-3f6d-3a04-9d69-6139c306f578 | -10.58859 | -49.64031 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45859a23-de32-3e96-9501-bed6e1481a6a | -10.65528 | -44.48841 | 2025-06-24 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de40693d-576a-36d8-b4bf-00d56e997387 | -10.5157 | -47.57859 | 2025-06-24 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1a2f888-5076-3c3e-aeef-beaa3e90cde8 | -12.22034 | -44.24891 | 2025-06-24 04:25:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acdf96ee-8a32-3f4a-bc41-ccf3abe30541 | -8.5694 | -51.58139 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 960417ee-755f-3a85-85ee-d8c0854767f0 | -10.0602 | -49.66231 | 2025-06-24 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e79071e6-a342-3274-bc5b-4135d6004270 | -11.56262 | -47.91813 | 2025-06-24 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b7b814d-806c-3e05-a93f-d142669496a5 | -10.23241 | -47.45758 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adae561e-b4e7-3010-8eaa-10b501387523 | -8.70072 | -47.17504 | 2025-06-24 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5569958-7288-35ca-96fb-5ccacd5cba05 | -8.70678 | -47.17957 | 2025-06-24 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d825c05c-c884-3810-875e-d5afc4012f10 | -13.55457 | -44.09751 | 2025-06-24 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c59fc82-38b9-32e0-8bb8-6d7f49c60177 | -8.71795 | -47.85388 | 2025-06-24 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3b864e7-f7c7-3503-b901-ee2b66bd7ce6 | -7.47586 | -45.58611 | 2025-06-24 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93c30ffb-ad77-347f-a9e3-f49bc299488c | -8.86924 | -47.26966 | 2025-06-24 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 76eb8d04-20bd-3b96-8b3c-5b543c1c2640 | -13.07142 | -48.83031 | 2025-06-24 04:25:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 09033a50-ddaa-3bd0-a5a4-a840d18fe147 | -11.93808 | -47.84258 | 2025-06-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15a92fc6-7d6d-3d75-8fac-32e7e712bcc5 | -13.07476 | -48.83088 | 2025-06-24 04:25:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4c6e54b-c381-38be-ab09-01e839060830 | -7.36923 | -43.48645 | 2025-06-24 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4b4bfba-ab52-3ea0-ae31-40b7e8626e81 | -8.57645 | -51.58776 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2388870-291e-332d-b0f9-e3b3745bf1b4 | -8.06107 | -43.10543 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 3d2ca42a-7b5e-37ee-be8c-144dfcc79922 | -8.56499 | -51.55966 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfb53712-8805-3858-8ad0-ce457d5183d1 | -10.08499 | -52.74645 | 2025-06-24 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9805ff98-e06d-311e-8e9e-f70de5480b79 | -13.62152 | -41.8307 | 2025-06-24 04:25:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b1364b8-794f-33d5-8c48-b3485a3200d3 | -10.86661 | -53.76678 | 2025-06-24 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51eaadfc-d4cc-33a4-81e3-d155cf731713 | -8.56586 | -51.55458 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23295e62-4427-3b5c-9a46-69fcd8e2c0a8 | -14.19285 | -42.77739 | 2025-06-24 04:25:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c0db8565-796d-3c62-af35-8c01ccd1bff8 | -13.76707 | -44.09636 | 2025-06-24 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcf2d8a0-8675-3e1d-af05-e266079411f0 | -7.09485 | -44.37349 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d58a1fe7-6bbb-302e-b0e4-dade5d33ba99 | -13.2764 | -46.8174 | 2025-06-24 04:25:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6af37c7a-85c5-3c23-aaad-e919af6e3946 | -10.51514 | -47.58208 | 2025-06-24 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f2af8a7-8545-3393-9721-8ba32f6cb680 | -11.28038 | -52.46431 | 2025-06-24 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 973afb58-839a-30eb-9da6-9e1800f522bb | -7.43481 | -45.54731 | 2025-06-24 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06620907-3deb-3f57-801a-92a067f09420 | -7.20356 | -43.09575 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4af7083b-e018-3450-86bf-e408b434a371 | -12.89553 | -43.78912 | 2025-06-24 04:25:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
