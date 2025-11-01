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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fdab910-d635-3d3c-8dc4-ed6d5d8dc91b | -3.2082 | -51.02846 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5225974a-9fcd-3992-ade7-467132a51835 | -2.06566 | -46.35047 | 2025-11-01 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 561112fd-7cf5-3676-b904-327267987e42 | -4.66363 | -41.96503 | 2025-11-01 04:38:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4f19f157-046d-3863-8b81-38d08909615c | -6.78861 | -46.94155 | 2025-11-01 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d175421d-d1aa-3900-afea-eb32fe15baf9 | -4.64691 | -45.39098 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e94d8a95-80e5-3ce9-bbea-54420a0b91a1 | -6.13684 | -45.93937 | 2025-11-01 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ad767d5-0cf0-327c-bc5f-68e36335b205 | -7.45431 | -46.71065 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d0cdc78-85be-336f-8be0-5cb14474f67e | -4.93966 | -44.82444 | 2025-11-01 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8753b07-4229-3075-ba2b-5e199bd3a9ff | -5.83689 | -44.06013 | 2025-11-01 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fc3d15d6-cf96-32e7-84d0-3d573e80dbba | -4.18551 | -47.6545 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37702a1b-e470-33ee-89d8-ec49fe8ec74a | -3.10901 | -45.2333 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3b34b6cc-7db7-3556-91e3-1e0f2b0139c0 | -5.06918 | -43.96063 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9754a79d-6aa0-312c-a27e-64122d72048a | -5.21558 | -45.92183 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c78be0f-a778-3e5b-83e9-72e1d0250543 | -3.86522 | -51.17157 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a4e1889-2cc7-38ab-9d24-d8469fdd073e | -3.11628 | -45.23438 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 22101254-824d-3cb5-90b3-e6bbe7620013 | -4.44765 | -44.20926 | 2025-11-01 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3879d8f-49dc-331a-af9f-8fc2269180ed | -4.75442 | -44.46362 | 2025-11-01 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c905c2a-9e97-3ae6-ac98-8dd9c2edc308 | -5.79206 | -43.02217 | 2025-11-01 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc6c6dbe-8809-383b-bd7f-dbb20f9e2010 | -4.96667 | -40.54601 | 2025-11-01 04:38:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 76759e5c-d434-34b7-af41-288915cd4d8b | -6.54287 | -55.05075 | 2025-11-01 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1727137-9e81-3e90-b761-6eeed4b34129 | -2.04968 | -52.07807 | 2025-11-01 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07f24992-ba19-3f81-958c-53c01e3852f6 | -3.77216 | -47.6231 | 2025-11-01 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e45a292-d52a-378e-b03a-370c0103e2c4 | -7.07283 | -47.00634 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38870fb1-5421-313f-bc75-4eccfe5129d9 | -5.48384 | -47.62077 | 2025-11-01 04:38:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41bd7b97-d565-31c9-8329-44638aef6687 | -7.07341 | -47.00249 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf8da2de-802d-31b8-b2b7-dcad85cf25f6 | -4.96624 | -40.54899 | 2025-11-01 04:38:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e24e552f-ca96-3eca-84e6-acbbc6a06107 | -4.45157 | -44.20985 | 2025-11-01 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9627792-ce40-32a5-85a8-2798cb1e41df | -5.12934 | -43.38412 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1132a08c-17d1-3c60-a61e-16f464c1800e | -5.19038 | -44.91083 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4afd8078-e15e-361f-977b-47b0c500671d | -5.72922 | -44.63642 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d45a51a-5d19-3b73-9f72-6c2c9285a805 | -5.11623 | -43.38604 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41b9cf76-7ee6-346e-b14a-278d478d6228 | -3.87667 | -51.18918 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd287bdb-5313-364a-b5f7-6eb800b63326 | -3.11758 | -45.22596 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 855fc705-3c9b-3101-a553-dc22ac1f7215 | -7.0268 | -37.24109 | 2025-11-01 04:38:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d958c67d-e406-3f74-8f26-db37eed9e1d2 | -3.65629 | -50.18811 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2769e3db-5f5f-3f5e-8a0c-1687820b56a8 | -5.20996 | -45.13909 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de6eca29-d2e9-3f54-9577-d8488f3c7cc5 | -6.85236 | -48.6851 | 2025-11-01 04:38:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 595cb51f-fbad-3108-a433-c751b7e0c66b | -4.55138 | -45.62632 | 2025-11-01 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ecd11a99-e347-398b-863b-0365c26c256a | -5.08951 | -47.7035 | 2025-11-01 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46504f22-6e3c-3760-a4c0-970b6beb6975 | -2.02534 | -46.99922 | 2025-11-01 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ab1c1d2-54b4-3755-b916-0cef517bcf6f | -3.1592 | -51.04458 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2184e3d5-61c5-3ee4-b879-23bc207173b1 | -4.42835 | -47.60169 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 562b9bd1-de3a-385c-a0ce-602a35b8ea9e | -8.18257 | -44.75642 | 2025-11-01 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b9870c6-f73d-376d-8a12-13e2e123663f | -5.89947 | -49.14453 | 2025-11-01 04:38:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5baab983-4c96-3452-8a9b-9780619ab621 | -4.81964 | -45.71408 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68c55d31-ceb7-3ded-a94e-c217ec344b59 | -4.80615 | -45.75514 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd1e8bd1-2198-32e9-98c3-f6af6dee61ac | -3.43382 | -42.5432 | 2025-11-01 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28cca3e5-923c-349a-9962-c1c917ad02f7 | -7.70474 | -45.98745 | 2025-11-01 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8edae6c5-66bc-3ae2-be2b-f62b643b9916 | -2.95966 | -51.52168 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10c57b60-3cd5-38ee-b14f-0ba9a7b234b3 | -5.30449 | -45.34622 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4774bdd2-a5fd-3800-a7cf-805840c24a12 | -2.95543 | -51.5252 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cfcd709-eb0e-3436-b9c8-e49e47200dba | -3.2479 | -47.32203 | 2025-11-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8656b03e-06ff-3fc1-b78b-d2d30f9a2dfb | -8.18607 | -44.76037 | 2025-11-01 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9183fd7-3e55-330d-9108-52f7019f2d8d | -7.9656 | -38.28209 | 2025-11-01 04:38:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9c1add4a-b53a-39b4-aed7-9e9162c12330 | -3.88011 | -52.26322 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6db2867-fd34-301d-90eb-f38018376560 | -3.04363 | -45.82005 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3e733f3-0e81-3932-ac1c-d5539579a4c9 | -4.58179 | -44.98715 | 2025-11-01 04:38:00 | NOAA-21 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afda9ac9-6ffc-38a7-b9db-dfab6c9e7643 | -4.49377 | -48.27708 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f951107-a6b0-31f9-9f1e-aeb06eb1cc51 | -6.85964 | -46.93197 | 2025-11-01 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a0e9163-f370-37e1-8413-4ca01805b266 | -5.39431 | -43.32153 | 2025-11-01 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eabc25a-f8e7-3009-bf70-1fc4de1a2b22 | -6.93979 | -49.63114 | 2025-11-01 04:38:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ab064db-14c3-36d7-b6e8-6baaef518642 | -6.35558 | -42.39361 | 2025-11-01 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9568906f-57ec-3979-8e56-ad46aa7cb9d5 | -4.21703 | -44.53432 | 2025-11-01 04:38:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b58951e3-8bb0-3db7-8e94-a703c645c535 | -4.33087 | -49.81467 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbced0b0-969d-341c-a1a3-528f5f9c0e9f | -3.01565 | -53.97062 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d49e965a-16ad-38bb-a15d-b6c5c2c71516 | -4.43564 | -45.91316 | 2025-11-01 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c456bd4-6bbd-3711-87eb-d224cf1a5bb4 | -5.09458 | -47.71508 | 2025-11-01 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea283701-545d-3f8b-8db0-dc20cdc79c6d | -4.55762 | -48.47847 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2c6b567-f1e1-3136-a42c-7f18b0d47db2 | -2.89737 | -48.06229 | 2025-11-01 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91398f12-3b23-3fde-8400-55dd81b07e34 | -5.50731 | -48.38926 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85a36282-a6ef-3b65-a1e2-135a5dcddfd8 | -3.59747 | -54.04336 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c804894-0e78-3412-a3f2-9950f763c8c2 | -3.28325 | -45.32082 | 2025-11-01 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 480f91c4-e7d1-35ec-8957-f0b40d5ae37f | -5.62146 | -47.41207 | 2025-11-01 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 779152fd-6c7d-35ed-9ecd-2fc613da08a4 | -2.93247 | -51.46336 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dde8ae71-129d-3ed7-8242-6844c8464648 | -7.36551 | -47.78012 | 2025-11-01 04:38:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa4413a5-f2dc-3d17-a4b0-8d0ddffaa3d9 | -5.21066 | -45.13453 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d737c87d-e5c7-3557-ba30-1cc2683e0706 | -5.10529 | -44.26833 | 2025-11-01 04:38:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62749769-8fd3-3168-9f91-a82db316d019 | -6.55859 | -47.61715 | 2025-11-01 04:38:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e61298bb-1736-32e7-b508-1ab15dfe631e | -3.33825 | -51.28714 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da029f78-7238-3b3d-851e-db46cce26f45 | -5.46119 | -45.40363 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9941d7ed-5399-36e5-a950-bbb9208cbe64 | -9.6933 | -43.99289 | 2025-11-01 04:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f7e5979a-341f-3c63-9d93-ff450d804c90 | -5.80218 | -44.54683 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2115b625-51bc-34da-9ac1-b031fe5de24a | -3.49217 | -50.2099 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e639d9c9-e733-3cf7-bd3c-8396e4c7f7b4 | -3.66493 | -51.71448 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 626b35e6-461f-3063-855f-614ea85407ca | -5.46501 | -44.88992 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee696c27-4039-3de3-8294-7d26c06756d9 | -4.64578 | -47.9561 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bd05678d-eb52-3a59-9356-9a4db31ca888 | -3.30858 | -50.01615 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fe25930-fa1c-3dab-806a-e20167f6f716 | -6.563 | -52.79645 | 2025-11-01 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 523593b5-1904-3aa8-91a7-3b9502c79a34 | -5.59879 | -50.06154 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f2ea352-2633-3cfc-8461-cd5ee4057548 | -3.22925 | -50.58175 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| a1264c9e-d3ab-39c3-b51d-a10bc0b87047 | -3.11031 | -45.22485 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53cafbc8-c08d-3334-8b96-09c9c42d51f5 | -2.37469 | -45.45766 | 2025-11-01 04:38:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcb14c06-8150-3f92-bd34-e7a822a24e9b | -6.81732 | -46.75424 | 2025-11-01 04:38:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62fa587a-ae48-37ab-8387-1560ee010976 | -5.67316 | -46.73145 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8215abb3-61ca-3327-82e4-9d11dfac7509 | -3.48929 | -52.35861 | 2025-11-01 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af379f21-4840-34dc-9e0a-5eadc1ceb651 | -3.01488 | -51.38124 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c590f71-9057-358e-9a4f-6850130f6de7 | -3.22523 | -50.58494 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e288f64e-8d47-3b4e-8671-befb2c6142d4 | -5.35475 | -45.03031 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fdf6c41-8b8f-3655-b6c6-8ee7f62b9c77 | -5.17094 | -45.71574 | 2025-11-01 04:38:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21a0b56e-25dc-397d-85dd-99caf4b42739 | -3.53157 | -47.55351 | 2025-11-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README18.md)
