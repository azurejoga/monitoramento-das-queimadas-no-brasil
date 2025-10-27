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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce0d580b-8bcf-3999-a973-f821c1f3b8c7 | -10.31606 | -47.17105 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a10966e3-bb5a-3412-9394-dda417d80e4d | -10.33963 | -47.21933 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8adab913-39d4-33cd-b2fc-bb57ff46c817 | -10.31533 | -47.17647 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 751279ef-7744-353b-8c19-8e3dfc69c669 | -7.34202 | -48.48866 | 2025-10-27 05:01:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2dd4ced9-cfce-3094-9499-2eabc56ef3c5 | -8.0587 | -54.92311 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d809134-2d2a-3241-bf3e-0f339d46209b | -9.73019 | -45.42009 | 2025-10-27 05:01:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd79e9f-ffc2-3ce9-aa8d-689148dbf515 | -7.3359 | -47.14061 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f1914888-143a-3df7-9e32-ae2c302ec335 | -10.33888 | -47.22477 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a949ae0-8bc1-3da8-b020-5c455cfdd6e7 | -5.82523 | -50.03299 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2223cfbf-4de4-399b-a6f2-ae46becbf492 | -9.98856 | -47.18417 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 656e88cc-eaa6-3783-9332-117d26ce3087 | -9.13148 | -45.86131 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9669fb08-8460-39f4-82f2-81183e0cb82c | -9.99152 | -47.16226 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cf60906-ad62-35a3-8b02-17ad8b50d483 | -8.27027 | -46.88464 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88c8f5d0-6a6e-3f8c-806f-d2c51f71a981 | -7.85665 | -46.45181 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e33a69b-dbc2-33b9-9e6c-f570175597ef | -10.35474 | -47.18226 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 500c945d-43ff-3c53-beb3-3b658dbe4d4c | -11.63381 | -54.58117 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9ab4043-f6c2-3f4e-8d89-929665ded8ed | -7.83189 | -46.48326 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c898e839-b7d9-3fdc-8e7a-e3526ae2686b | -7.82727 | -46.44305 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc1d5ab4-100e-3f1b-bcf2-a07badd35ea9 | -7.60026 | -45.68661 | 2025-10-27 05:01:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d81c0930-f2af-3f81-bdd8-19a191092633 | -10.35529 | -47.18411 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 0aefff85-4ead-302b-be37-5a5c4574faa7 | -8.88312 | -44.84208 | 2025-10-27 05:01:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb6bd676-8282-3874-b447-9432193cc790 | -10.87596 | -54.05051 | 2025-10-27 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4ce2901-a20f-30e8-88cd-b81cf5166ed0 | -10.35399 | -47.18776 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb383faa-1b88-3e21-9bf7-57e2848c1eef | -8.12528 | -47.03004 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a31d0728-44c2-3107-9452-c23218eb14db | -4.47634 | -55.54182 | 2025-10-27 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96303cdf-c2d3-359f-8728-689c0dba0e51 | -6.37698 | -44.26657 | 2025-10-27 05:01:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37a6b484-7539-36db-b1af-5461a30545b2 | -7.80293 | -45.38413 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a8aa49f-7a71-3b3b-88b3-a8a73bfeaf98 | -10.83278 | -56.96026 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e0736ff-d9a8-3f46-861d-e091c5be2bd2 | -8.0276 | -46.75664 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b88cf91-9666-3594-b526-8faacce38dcc | -5.60603 | -51.86714 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8b393b9-de3a-380c-a9d9-cf6b43e39c80 | -7.85348 | -46.47444 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8d865ea-d16c-3276-bbf2-88bcfa433dba | -7.84189 | -46.48446 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce026479-c1a7-3839-958a-6ec8d0c4b8d5 | -10.53655 | -51.59807 | 2025-10-27 05:01:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccd92617-6119-35e5-a0c6-265a1e3fdbd3 | -10.23101 | -52.15825 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e349035-1a58-3bd7-85fa-d595708124b7 | -9.60363 | -45.48584 | 2025-10-27 05:01:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64bc2b4f-f0ca-3b47-ae59-2bc7c2886451 | -8.69444 | -44.4322 | 2025-10-27 05:01:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 211aba7f-aacc-316e-99ba-49335a17f91a | -10.83679 | -56.95712 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3ff47fd5-cf77-3dad-9c84-445e7474b495 | -12.04053 | -46.39304 | 2025-10-27 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a10f500-1c30-3a5c-933c-9473b26dc908 | -6.89105 | -43.57291 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72e145ab-cc7a-3ed6-90d5-b4d0ffce3aac | -9.44667 | -56.65113 | 2025-10-27 05:01:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ec50ef-8f29-3f17-881f-25e145ead6da | -11.98285 | -49.76877 | 2025-10-27 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41331379-99bb-3686-adee-4a471f3d41f0 | -12.08838 | -46.40037 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3085d0b5-c007-39b7-bb94-81e2cc1c8127 | -6.57937 | -47.53879 | 2025-10-27 05:01:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 077e0b4d-7bdc-3991-8f6e-b03c86cbaed8 | -7.85083 | -46.45702 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d8fbc3d-48d0-3fac-b587-edd81b397a10 | -10.54661 | -48.00939 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 90fa88df-deaa-3479-8ff6-8ebee9e45980 | -12.0599 | -43.98958 | 2025-10-27 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fc45b36-83bd-3fa9-bc54-035b424f0301 | -7.83535 | -46.49495 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2fe9080f-8422-317b-953a-5ed0a834a99e | -8.64847 | -44.77115 | 2025-10-27 05:01:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b21af65-157f-32ae-8cd2-05c42ac5dace | -11.05814 | -50.35707 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7599ebaa-1c1a-365e-911c-46e24363bfde | -7.85766 | -46.48088 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edcca684-67c1-31c4-a660-8a2c841914bf | -7.8215 | -46.4479 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbf7ba22-13a0-368d-aec7-1fbdfe99056e | -12.05493 | -46.37845 | 2025-10-27 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2545e440-eee2-3941-98c7-119566017112 | -12.32783 | -47.47995 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c3e2cf34-6c9c-3682-b7d3-9147d7b4caaa | -8.64877 | -47.24623 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0ff2013-4637-3fca-92dc-e2b988ee5b5f | -7.24913 | -46.96268 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53496a04-797c-3f67-bfc8-7a5ef7a515fe | -6.88446 | -43.5765 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f9ac0f27-6f1c-32f6-9470-1fbb916b3dfd | -12.08767 | -46.40606 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a4f12b6-a152-30c2-a6f4-52d7ee231b6f | -8.31043 | -46.18511 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee0137f0-6cfe-320c-909c-347f85f36043 | -6.2597 | -41.83657 | 2025-10-27 05:01:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e117c553-faa9-3bd0-af9c-2db847ee725b | -9.25158 | -45.56991 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac0f261d-b210-3b56-823a-8a160d90faa7 | -7.81391 | -45.39923 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbf13dcf-bcda-3e85-a4a0-4f4e097f5ff1 | -8.89106 | -47.9964 | 2025-10-27 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45ac1c1c-72d6-3c5e-bd8c-19306d6cdc04 | -8.1434 | -47.03425 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8c0ac9d-8818-37f3-99d8-3d9c63f4f7e6 | -8.02992 | -46.74013 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac06cf61-2b8f-38e4-9660-67be169e1144 | -7.855 | -46.46357 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 97121832-3b7a-3cae-8005-77b563e91f5d | -7.06005 | -46.75358 | 2025-10-27 05:01:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31fd9712-9ed4-3cd9-8363-d52b2c0dd4fd | -13.17248 | -43.44407 | 2025-10-27 05:01:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 494453f7-2771-386b-8433-a11fb52d9531 | -10.70876 | -48.07453 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc919b44-d7c1-3c10-b749-57bf7a454875 | -7.94449 | -47.24285 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cde057c-b4e3-3389-a898-eeaa04533600 | -10.34008 | -54.19934 | 2025-10-27 05:01:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6faf0cb-19de-33cc-a40a-424d7c1657ef | -9.1314 | -51.3024 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86105cf6-742c-3d7d-ae75-95a6501c2ec0 | -7.25581 | -44.96473 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35928168-724c-323d-b064-e35a552ea2c6 | -5.60661 | -51.86333 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0793f5ac-8e72-3a37-9c52-6b5505ee9014 | -5.60751 | -47.10329 | 2025-10-27 05:01:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f481a913-8a93-34a7-8f5d-d41929e66de6 | -7.86861 | -45.71387 | 2025-10-27 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e06520c-a452-3391-9b8d-359b52ea8187 | -8.03482 | -46.7409 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 471b20a6-4c92-3016-bf51-02d247c809d7 | -5.89137 | -49.37827 | 2025-10-27 05:01:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21128688-a738-3b7f-9e8f-5567db6cafc2 | -5.77303 | -53.45274 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4492e47-416e-3126-8c9c-7189359760bf | -7.44176 | -41.86757 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e4eec0da-4527-3e1d-926e-8c089757b2ac | -11.60927 | -50.98952 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f43bf72f-4646-3572-a6f0-bc58f3e53e85 | -11.33626 | -53.93514 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 344b0821-8245-3879-8781-b2e5c92941b4 | -9.23216 | -45.8363 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29f22aaa-afd7-3fe3-ab86-6c447259efc5 | -7.44024 | -41.87888 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4ebad9bd-f0dc-32a9-97b3-6ab527d40e25 | -12.32658 | -47.48425 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ceea658a-35e6-3160-90d2-a64884dd3973 | -9.13998 | -51.30606 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 21298b89-2967-3ba2-b294-9a479dce321e | -12.04093 | -46.38969 | 2025-10-27 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b8a35d8-c80c-3753-87ce-ba5c3c78aa96 | -6.45571 | -42.33632 | 2025-10-27 05:01:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f10d3ef4-8238-36b9-a650-a27d7a82394c | -9.252 | -45.56675 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e640fbc9-1d75-383c-8cfd-13a66eb19263 | -12.04212 | -46.39369 | 2025-10-27 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ef89119-db4a-3630-b34f-06b43cf6c7b4 | -8.95849 | -47.19085 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c6ea3926-2a8e-3626-9373-5c907bb0086b | -9.63445 | -46.86913 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61ce6f7a-d923-3a20-8865-801865a03583 | -6.37649 | -44.27012 | 2025-10-27 05:01:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b5a8619-5676-3565-af18-9b29623eddc9 | -5.63214 | -50.31499 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e5292fe-14e7-31c9-8acd-f90637645153 | -7.23695 | -46.94531 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9306ea2-02b4-3496-97bd-8cf30f7060c2 | -6.44723 | -42.3508 | 2025-10-27 05:01:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 24f4f7a0-8f0c-3fb7-801b-585858650504 | -7.81239 | -45.39488 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e508873d-25d4-308c-8e0b-1926cb94ef34 | -9.587 | -44.94561 | 2025-10-27 05:01:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71f77919-fea7-3ee5-afca-875fa082aee8 | -9.98784 | -47.1895 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9842f37c-abc2-3233-8040-cd4dc925034e | -4.96631 | -56.27653 | 2025-10-27 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52142dee-35cf-3c2c-a29c-0013af73459b | -12.04959 | -46.37782 | 2025-10-27 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README61.md)
