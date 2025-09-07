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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db80abba-8c8f-3838-a75c-dda7d4c080d0 | -6.19772 | -53.2668 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6419bcbd-5127-3173-b271-12657fbc6b4a | -6.26708 | -43.49247 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| b4e60f4e-733f-36de-8fbc-8a0f6577c5bf | -6.23072 | -53.5751 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 401cee75-6eda-3feb-82b4-f1c88d4f9c14 | -11.40031 | -43.6176 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73eff40e-e6ed-324c-be9d-7d2eda21c60a | -12.80109 | -48.0223 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d2a0364-fe2a-39f3-a045-675af53c34d9 | -10.73184 | -48.59905 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8f0ea23-4cfe-3467-8fb0-6190f3ef7dc2 | -11.31503 | -46.54441 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8273efd7-f9f4-3344-8d01-a5868b376a64 | -8.07221 | -52.34451 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11027f7f-1870-3e43-936b-12fa71121d65 | -9.02019 | -49.79987 | 2025-09-07 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcf89e74-9cc7-37b1-a2ad-7d893d38f261 | -11.60567 | -47.1619 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 040976c3-e6d9-30c2-bab6-dd74b5138581 | -6.63461 | -53.17641 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0714ce93-fa51-3b63-a671-0a9fa98b13dd | -11.26125 | -51.12098 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e26c89f-3fc2-375e-8083-72ef163029c5 | -8.3782 | -52.53457 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3ac7f42-30c0-398c-8ece-dabbdbe143a9 | -6.18627 | -42.63446 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c7a1619b-bbcc-38dd-81de-5b96d91796fa | -6.52576 | -42.93165 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0877458-c331-33a4-b3bf-da3784a68b8d | -6.88642 | -45.59878 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a000a39-d5e7-391b-ad29-df28be42022e | -5.89192 | -43.65452 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e58d0ff-1d9b-3dcb-bda3-9ab212dafcb9 | -8.6898 | -45.30177 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 145ee662-64a9-3a8c-8ee0-025b615e1419 | -7.74851 | -44.0083 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33bd17c6-4ab1-3bca-9752-af648921030c | -11.00254 | -52.04933 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cbeacb2-c5b8-3c56-8c32-3a3a91cee725 | -9.98133 | -51.6622 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f27f9c39-873b-388b-90b8-11bf82568df0 | -12.52225 | -48.05436 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 948eb73b-0655-330b-b1e5-4026a7043408 | -6.19717 | -43.3757 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3ab7ffb-c198-3414-a5e4-297af85b448b | -6.21776 | -42.63552 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98ea73fd-d50b-331f-a0e7-6b2c42579c0e | -11.40952 | -43.60319 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 432ce9be-784f-3a74-ab04-deecfe361a3c | -13.00459 | -45.20925 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68899e2a-e783-33e0-8c2f-d936faf8aea3 | -6.15219 | -44.24934 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf9326fb-0c5f-31f7-ab80-0deceb7867cf | -8.11742 | -45.31365 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fff1c8c-a3bc-3038-b9a9-88309604d211 | -5.96722 | -53.6007 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cce533e2-6c3f-3831-866e-6fa36d08d65a | -10.60765 | -44.34494 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7eae0d04-3f11-3174-89e8-4dee74671009 | -8.12018 | -45.31765 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5418d0bb-3235-3c92-a702-e332fb409829 | -6.21885 | -41.78581 | 2025-09-07 04:19:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52452074-f221-31b7-9b5c-739e9869324f | -12.95048 | -44.70555 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 382a237e-1156-371f-8c25-717b77312e8f | -5.89785 | -51.94319 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 831859ba-8ef1-3bc4-83f0-8fc283a30469 | -6.15486 | -43.20373 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 942c50d4-a786-369c-8096-956ce6fc458e | -6.385 | -43.00138 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffcf6eb2-0c91-3322-8f15-67c47b08b290 | -11.26035 | -46.39869 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b97232dd-36d3-3f8c-8db8-8860ac5fca48 | -8.91788 | -45.81331 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 926253ac-70a6-3d02-a405-2098bd4ce324 | -11.58256 | -47.72869 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be43aae0-5ac6-3ee1-aecb-f016a9f314d6 | -6.22349 | -43.3174 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf92f80a-dc58-3f45-a04f-5ad2f1bdb28c | -6.58943 | -43.99348 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1b58583-dee8-3adc-ae38-6e0f94f6d473 | -6.27058 | -53.43827 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffef239a-b53b-3d92-badb-17949033d098 | -11.24309 | -46.44284 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc1448b2-e6f9-32c7-8b20-6e91e37d8ec2 | -7.81322 | -45.43188 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5896e8c9-840e-3470-b42c-418365c35e02 | -11.11204 | -52.02055 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 389ae4f8-7e7f-368c-9d17-213bcb196877 | -6.10566 | -43.19999 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b9bcc7a-8227-3d91-9ae7-b15930172a33 | -11.32054 | -46.55257 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6aee7b8f-cde8-361f-93c7-97caedd1e53d | -5.89138 | -43.65803 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 570a46c5-5414-3f0b-9e8e-0472c1aaafe1 | -6.49 | -43.97759 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb753d70-0187-37af-8548-1db0c641eac7 | -6.07704 | -45.4557 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fef21426-cbc6-32c0-a7de-a252aa9218bb | -9.98062 | -51.66619 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 733906a5-5e24-38c2-8686-b1238851ef32 | -8.11798 | -45.33155 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8865653c-11c6-3492-bbf9-ac6902552163 | -11.596 | -47.16809 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 333da81e-f240-3c1c-90ed-e921991d44ad | -6.39513 | -46.07999 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69647891-056f-361c-a08e-5912f1fe321e | -13.00683 | -45.21698 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d83b11b4-47d2-3d09-90c3-e8a21fee3775 | -5.79742 | -45.65276 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d298ffc5-b0d1-3d24-8008-3a9fac07339c | -11.11053 | -52.02888 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7e2f2d4-2967-3f96-8cb1-ff83b96e034d | -6.2006 | -44.17884 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ce01a63-2e21-3274-aa51-85b3266d3ba7 | -10.77964 | -46.02455 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 808e4a86-133f-3052-b24c-d0741ea4977b | -6.63063 | -53.16933 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c2294ed-46a2-382c-84c3-3acc223b09ee | -10.52265 | -44.38314 | 2025-09-07 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e953a15-5be6-3951-8743-e8c89d3f6aa6 | -8.29758 | -47.41096 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44fa7852-71a1-352f-b284-eb9b9d7e76e0 | -6.54054 | -44.82455 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 98821aa0-562b-360b-88ef-dbc786e3f0e6 | -8.9405 | -44.26229 | 2025-09-07 04:19:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56c55d19-555f-3993-b2f1-5b1dccd08b6a | -7.73002 | -50.33063 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 984eb97a-8d18-314e-b79c-8804803579f5 | -11.40842 | -43.63453 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe4305ff-6108-3103-9abc-7519fb38871a | -11.2562 | -46.51016 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 347f5556-73d0-3572-b7f2-42a68b8283ee | -6.29598 | -43.32871 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18c902d3-97f5-3bd8-9a55-a06b5b4f7c0b | -10.80161 | -47.72018 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2da945a6-c9d4-3e44-b873-fb9a130f2694 | -10.7354 | -48.59968 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfb668e6-a077-317e-b6d8-d00caf529071 | -7.73881 | -48.81924 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50c9734d-7788-3ec7-b38f-af4a185efcde | -8.35509 | -48.27247 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58d4ed71-fe2a-302a-928a-148730c580c2 | -10.58734 | -48.46777 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd95c5cd-13ba-35d3-860b-da8b56411c22 | -6.1042 | -44.76953 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61975d71-0270-33ab-89bb-85268dab7be2 | -11.31998 | -46.5561 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d94733be-c46b-397f-98c1-0f243452db23 | -10.6054 | -44.33721 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61b0d484-82cf-3fa0-91c7-472c2436a60f | -6.20287 | -42.64082 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 99faa8ba-b81e-3cf2-80c7-0c504237660d | -6.3625 | -43.53262 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| accb8042-43e7-311d-a100-f2e99cafe340 | -5.83218 | -44.12394 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5c240673-9e47-368c-a094-c0b006b127f5 | -11.61635 | -47.15986 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64cec031-96f6-3eb1-864b-330629b1bdfb | -7.84889 | -44.79742 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a703b185-fca0-3717-8f42-0b4ad49254b3 | -5.84322 | -44.11855 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1f7a0dd-ecb0-379c-9a46-1b1070cc5112 | -10.77633 | -46.02401 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c07264f0-707b-3447-a595-73d44ba6ac12 | -12.84455 | -48.01371 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c944afd-87c4-36cd-838f-b4a8f6ea3165 | -7.73805 | -48.8237 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5b49ff0-6ab9-3edc-8c7a-95c927b8ec2a | -11.15968 | -48.3828 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ba1a74c-2136-34bb-bc5d-14900b4c78d7 | -11.25068 | -46.50202 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30a4fb83-dd83-36e9-8bb1-8ae234ff95e1 | -6.27985 | -53.44638 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c7202a9-04f7-39d7-a5f0-1e9769ac7b09 | -6.9276 | -44.328 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31f3847d-3249-3953-945c-0f8f89847932 | -9.98919 | -51.64313 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6da18b3-9c1c-383a-b047-89e418e9ed45 | -6.29206 | -43.33177 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0631c44-c17b-3a55-8d9f-9178cd9c75b0 | -11.25844 | -46.49612 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3b27643-62d3-379d-8f0e-6ee233ef028d | -6.19811 | -43.58352 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b248dc59-0971-3be0-90f6-ea4477af6589 | -6.18947 | -53.25343 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77f0c552-72ca-3298-bbf6-67e94e6f0f47 | -6.94465 | -50.97078 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1ba4bc9-a855-3002-b287-e33c9fa65c82 | -6.18765 | -43.37056 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8864e82c-ed65-36c6-93e3-35a6fd2cf6ad | -8.3456 | -52.55447 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c0d0019-c474-37bd-aa99-f241488d72ef | -6.30175 | -51.41503 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 90e3e394-19cd-35a9-a284-e37899ed8a7b | -6.88096 | -45.54754 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2c84eb7-5b9d-37e9-b40f-559c875937d0 | -11.34327 | -43.51015 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README50.md)
