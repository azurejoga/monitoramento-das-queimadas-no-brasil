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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0769ea5f-6872-36af-aedd-08c99ff049c1 | -4.6743 | -45.80749 | 2025-10-30 00:35:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d576e190-e758-3f11-8e45-defd88e567fa | -4.75921 | -46.84785 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bb735e6e-cd1a-3018-bf18-5b03c421f758 | -5.92443 | -47.32629 | 2025-10-30 00:35:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e87a366d-1c0b-3f57-80c5-8147b6f3cd96 | -6.40769 | -47.06994 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f0e4bde6-2e43-3a41-8635-3605736670ef | -4.43721 | -50.10425 | 2025-10-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14e738ac-1916-306e-8c36-63c4221324b3 | -4.68623 | -46.54201 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 280f16e7-7fd3-3d3e-bbea-ab35d107bb69 | -5.59266 | -51.13148 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4e31d496-d3ce-374e-844a-e7c379bd40c2 | -5.58622 | -46.54799 | 2025-10-30 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6efc79ed-6148-3be4-85cc-486bfa6a604d | -3.48779 | -49.90235 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d7fd9ba-5baf-35be-ad23-f6a5ecdc567b | -9.18051 | -48.30024 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b64a1e6b-70fb-31a0-9241-9134403e1eb4 | -7.60784 | -46.79424 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 768009f5-b8ef-3c46-9799-4a505077a15c | -7.46169 | -46.85088 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82c89f1b-8b4d-3a58-afcf-8c4c3f5b64ec | -3.47251 | -49.92266 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fa4e493b-fc5a-3174-9d05-3b48ee328db1 | -3.60772 | -52.65183 | 2025-10-30 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 626964e7-b593-30cc-875f-8e257eaaf4fd | -5.37311 | -47.2 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7c7ddc3e-96aa-3af2-8b67-00556d409450 | -3.46369 | -52.8783 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 903fb78e-9e46-332e-8814-9887b5a41654 | -2.66331 | -47.87145 | 2025-10-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5eff3a5a-4df2-364f-aeb8-c571fe9fd2f6 | -6.02878 | -44.3259 | 2025-10-30 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2d566517-f602-36a4-979f-edaa3ddeed3c | -6.00999 | -41.96242 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 7d2cd0ad-33fa-3ca2-aeb2-e12a30a2c5d6 | -5.94893 | -46.65298 | 2025-10-30 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2c34d031-c20a-3bca-b108-eb0d4d5b3f38 | -9.24688 | -47.53406 | 2025-10-30 00:35:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 78922985-9d70-3ec8-8048-59577a9655b0 | -3.0415 | -50.26654 | 2025-10-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3bd5e44d-851a-34f7-b3f9-496c94cc5fee | -4.74744 | -46.47467 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 759646aa-2c90-3bf0-9408-30d192b43d6d | -9.24003 | -45.5668 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cb6ba88c-8657-35bb-b28c-7728e00cb1ea | -6.99426 | -46.24084 | 2025-10-30 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bf0ae284-6cde-3805-b55c-07ae91bb3975 | -3.51823 | -49.7188 | 2025-10-30 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37aec551-56ef-3c80-994c-e93ec2bb1c7b | -3.26091 | -52.85259 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6294a55f-9cc5-3e2e-9e1f-8568df77400f | -9.0171 | -48.64952 | 2025-10-30 00:35:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a709d0e7-2749-3e5d-9311-d2aea3fc655c | -9.48245 | -47.00607 | 2025-10-30 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| e571014e-ccc7-37a5-b3e9-6ac64b70b223 | -4.17759 | -47.6493 | 2025-10-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ec0f0d54-ba1c-3b15-9a04-07078db0d43c | -9.1792 | -48.29106 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 29044537-276a-3b87-b881-a87b51d179fb | -8.71109 | -47.98279 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c2fbc6b9-92f2-3323-8dae-150c986ec0d1 | -6.48804 | -39.73493 | 2025-10-30 00:35:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 74.7 |
| ecbcde3e-6222-32d2-aab2-89cce6dcabf9 | -7.79802 | -48.30233 | 2025-10-30 00:35:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b4e27a97-4091-3a0f-b310-9e0f9651a558 | -4.48793 | -43.44486 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 24c6894d-6a81-3c23-b58e-a5f411657065 | -7.30153 | -44.97484 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 010059b6-2d06-3825-a658-92aa6a132421 | -4.31245 | -48.22625 | 2025-10-30 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3a3e82ad-3981-39c7-84b3-ce75ba92e5bf | -7.49924 | -45.98822 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1882edeb-79ca-31a2-87d6-33e42e51fd53 | -8.53915 | -48.97823 | 2025-10-30 00:35:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c9daad5-9752-365a-9918-1847b118d9f4 | -3.76689 | -50.3759 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed49b7e1-8441-33c3-bec7-bd1c0006966f | -9.86789 | -47.6926 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b968b37a-48b9-30bd-a832-d81367e57ab3 | -4.47269 | -45.76162 | 2025-10-30 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 659c78f1-485c-31cb-86db-872aa6a05e51 | -9.04608 | -47.81203 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32dbcf8f-a917-36d7-b5e0-c6c4900a19c6 | -8.33587 | -47.93678 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 82bd4cec-1295-3ca6-8a43-0ec53f9b2874 | -7.50093 | -47.05468 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6481e585-aa55-3437-8ba1-d117f5dd10fe | -9.80639 | -47.58165 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c3b0863b-b750-39f4-bff5-d66cb597b38a | -8.01445 | -49.7129 | 2025-10-30 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5ce40c8b-97be-38ff-a5ae-29da7601443f | -7.31471 | -47.81926 | 2025-10-30 00:35:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a4af729-09c1-30e2-8fd2-0395fa18a12b | -9.81492 | -47.58369 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| df21b8fc-e11a-3d4e-91e9-e70c328114ab | -4.27456 | -59.64202 | 2025-10-30 00:35:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| f3899788-f7bc-354a-b066-42ee4fec923d | -5.65609 | -48.02074 | 2025-10-30 00:35:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 740f6210-29cb-3b42-8a45-d02e84eb509e | -5.68669 | -47.83224 | 2025-10-30 00:35:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 028b247e-0d89-327e-87a8-b7594d7267f5 | -7.37868 | -47.62263 | 2025-10-30 00:35:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 75243660-bbbf-30b7-bbe2-9c312463ae6b | -4.27051 | -59.6698 | 2025-10-30 00:35:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 40c80a74-a4c4-316e-a87c-5f4c96839ccc | -6.5199 | -46.91763 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 00545e3e-cd65-37a1-98c0-b84f2c783546 | -5.417 | -46.00977 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 210aba5b-15a1-3b25-97a1-cf0cd67ba83a | -5.84562 | -45.54553 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 54bd0011-4fd1-367e-822a-c67ea792ee2f | -7.07867 | -44.94551 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| f5433ac9-a1f5-34fe-a415-157c1ade01e2 | -4.44635 | -43.23042 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| c15ef04f-8478-3456-b46b-d131094b3294 | -7.49738 | -46.73777 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0da58b81-d587-348d-90c6-4c294533a8c8 | -6.51828 | -46.90656 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c0e20353-63f6-36dd-86be-cb6dc35bb30d | -7.36932 | -47.62386 | 2025-10-30 00:35:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fdc55da7-6412-37be-8f93-13287ebd3ad8 | -2.94879 | -51.53048 | 2025-10-30 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 61a13076-c010-3a8c-9a65-953d7aaf9213 | -5.40316 | -49.4235 | 2025-10-30 00:35:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 56f9d70e-cbb5-391a-9fa9-dd23b365f998 | -8.91075 | -47.64204 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 99c60017-fe80-313b-81d5-ffc6aec81757 | -9.89326 | -49.11548 | 2025-10-30 00:35:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6c571d0b-6af5-34d9-8c62-05dbc422fed4 | -7.30368 | -44.98946 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c75783f4-8bdc-3ffb-90aa-7c0a37aa5813 | -10.01002 | -48.23606 | 2025-10-30 00:35:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bb7c6f73-67ce-367e-b7dc-d8549862ca75 | 0.28637 | -51.19831 | 2025-10-30 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 822ef988-1ced-3ac6-8de5-6a90b46455da | 0.62232 | -51.56461 | 2025-10-30 00:37:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ee75b3c3-d98c-3def-bf38-bba5da3b1033 | 0.29519 | -51.19954 | 2025-10-30 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 52dcf2a5-98e1-3e32-8d55-ba3d51735fea | 1.59087 | -55.69129 | 2025-10-30 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7fa9bfac-2bd3-3be4-83a2-f59fbba27fa9 | 0.29398 | -51.20831 | 2025-10-30 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a651606d-117c-3894-890a-be45b5fd7081 | 2.08458 | -50.8537 | 2025-10-30 00:37:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8565a388-7e76-3cef-b1d3-af03a4bb3734 | 3.14449 | -60.6861 | 2025-10-30 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| d1c14019-99f1-3912-a620-b1616bf1960b | 3.1486 | -60.6816 | 2025-10-30 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a41ce8e5-9780-3abf-a7dd-d73c0aaa6246 | 0.28516 | -51.20708 | 2025-10-30 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| eeca52b9-0084-332a-bfe1-513567a05d74 | 2.08336 | -50.86267 | 2025-10-30 00:37:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a7d57270-8ea2-3022-af50-4474af553604 | 0.83345 | -59.32032 | 2025-10-30 00:37:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| bf6b1cdb-d93a-3215-8d82-53c676a87e6f | 1.59533 | -55.69815 | 2025-10-30 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fdcb9b3d-9538-38c1-852f-9003d28a1005 | 3.13972 | -60.71688 | 2025-10-30 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 694ae746-063e-30ab-833c-3c1689742601 | 0.62353 | -51.55584 | 2025-10-30 00:37:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6307d47e-0095-367f-aab0-3de2d57ec4bf | 3.14408 | -60.7123 | 2025-10-30 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 3021bc2b-e00b-3b3d-a4e0-ac32beaf60a1 | -2.7741 | -45.3989 | 2025-10-30 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 5d1b7cc6-bb3f-36c8-80dc-8624e38644c4 | -8.3313 | -47.9219 | 2025-10-30 00:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 4d6e6311-3010-30c8-a834-f794290002d7 | 3.1461 | -60.6886 | 2025-10-30 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 86d2c3aa-f660-38d2-adfa-a1690a9de375 | -4.2649 | -59.6558 | 2025-10-30 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 6e3e4e39-9fb7-3c7e-bca9-733582900c9e | -4.2648 | -59.675 | 2025-10-30 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 511c61df-1021-3c25-9428-020c1f745a73 | -13.3935 | -54.3138 | 2025-10-30 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f9ac0d33-9ee9-34ee-b48a-898116c88791 | -13.374 | -54.3365 | 2025-10-30 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a6d03224-bfa0-366a-b02f-a9d82872c402 | -13.5316 | -44.341 | 2025-10-30 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c3629ad5-4242-3108-8f73-f890fe0f4f9c | -3.2317 | -46.8716 | 2025-10-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 0924feb9-b533-3274-a251-34120ef2c38c | -12.5138 | -50.5875 | 2025-10-30 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| aeea505c-4d55-3c2a-bfb7-64c0e0e00b33 | -12.1958 | -46.717 | 2025-10-30 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0021ed9c-a620-3c1b-9565-831d3b910615 | -5.3851 | -47.2052 | 2025-10-30 00:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 209ac530-9446-32d5-8df9-f0231b9cd226 | 0.2852 | -51.2114 | 2025-10-30 00:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0f9bd2d2-09e0-3c83-88e8-34cad2090b9c | -3.8054 | -43.9002 | 2025-10-30 00:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 4a5bec45-1966-3c97-8f35-2a4672bb5704 | 3.146 | -60.7075 | 2025-10-30 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a85d6a04-1ab2-33d3-a118-5187cccca637 | -3.7867 | -43.9011 | 2025-10-30 00:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 016a468b-c706-32d9-9075-6a6225c95cc9 | -8.3311 | -47.9438 | 2025-10-30 00:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |


[Clique aqui para ver as próximas entradas](README8.md)
