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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b2e2a1b-3d95-34df-98f5-251703994de4 | -8.10927 | -61.18953 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81d0ff5c-33db-3e43-9a38-8ae42daaac0a | -13.57546 | -46.96913 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8397e86b-f172-3897-9819-742ccb40b692 | -13.11856 | -57.16193 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b639440-616d-350e-a0b5-0baeb972d441 | -11.35201 | -55.42239 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b231f70-094e-399a-ba9f-ac43773f3ee1 | -9.18245 | -59.6695 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 55bc9b4c-0451-39d3-af6a-41d09dced8dd | -10.00304 | -59.22217 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddc6487b-9748-372e-8038-efcd89c36d46 | -11.31779 | -55.20631 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9a5afb9-c350-347f-a572-c3936b7839c5 | -7.94048 | -61.76527 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47220b68-3d7e-3899-b85d-be2c875c7a73 | -7.94673 | -61.76003 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cad5014-4723-3777-b947-e8b6bf3bce85 | -14.06722 | -46.31088 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecd4bc43-2a4d-3554-8c16-a8a50da9e972 | -7.52937 | -61.32998 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8b717199-e281-3b8c-9979-0f4f033f3fde | -7.0388 | -59.85408 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4226778b-8c7f-34c2-a478-993c32d2221f | -7.9581 | -61.75571 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cc4009c-86a0-3595-9cb1-b990b1668e76 | -9.21591 | -59.65821 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad3a2127-77fd-307e-9200-56d16e278326 | -7.29198 | -60.62472 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f7c458a-7178-3301-a363-5dadddd124db | -7.24952 | -57.66584 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c615661-44ca-36ea-9794-c5469975259d | -9.14345 | -59.42271 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5790a202-95d0-3f19-97ba-eb2d8f7e813f | -6.89153 | -59.14621 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad066cad-dcf9-38bf-9d17-39d34fd151ce | -13.58064 | -46.96589 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 475db0f1-5e93-30a8-96f5-ac457373ddda | -13.04872 | -56.84143 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c00b1e6-9497-33b3-8f36-3d77c17ace0c | -11.35996 | -55.41618 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36de0283-9af4-30ac-b275-587110394f09 | -6.70304 | -58.82267 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8e27b41e-3d74-33b8-9789-3a7271e1bc12 | -9.39155 | -60.54578 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 778545a2-baa2-36e0-8275-c864ecb3cc11 | -9.38242 | -57.85377 | 2025-08-15 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2b02434-a4e0-3cba-8306-21c48b5183e4 | -7.08603 | -59.22392 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72e98b0b-24b2-3a0e-b56c-a643a9d45305 | -7.25547 | -57.63023 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03fd7758-3c20-3754-bf31-167494d18578 | -10.35636 | -50.80664 | 2025-08-15 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ca10564-aab5-3dfd-9499-0e567e01e34f | -6.70235 | -58.82669 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c64c1b49-36a3-306f-a9a6-0372592004eb | -9.50003 | -60.53951 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a33a5288-ed8a-3080-8109-4418cc71377a | -7.8703 | -61.8215 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a0d752d-0915-3404-8477-259643bf6597 | -6.65935 | -58.8193 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4ffc5d18-b9c3-37ea-b3c3-ecdcbc949f36 | -6.6491 | -59.08508 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ecce1a4-257a-382a-90ce-db33b2b679a9 | -9.17582 | -59.68161 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31c6fa73-7e60-33cd-873b-0eff02ec09cf | -10.04685 | -59.11879 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 641d4479-2918-3734-9e67-34c9c3b2b49f | -12.75938 | -44.41405 | 2025-08-15 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dfda0253-2f37-3021-8cdf-36ea2b7ae796 | -6.93873 | -59.99762 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19a23347-0cde-352f-a61c-88b8e1e8609a | -11.40725 | -58.53617 | 2025-08-15 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a26f097-4310-34a0-ad58-eb684a93c300 | -7.62286 | -63.52032 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb02e5d7-98b5-35d6-bb76-85b2ed1a62f7 | -6.6668 | -58.81397 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef989ddf-3b9d-3bec-8759-92b847321244 | -9.18279 | -45.32768 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2ec4c3b7-b1f3-319b-bddf-aded80ab7887 | -11.34365 | -55.40967 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 399dc572-b226-3980-af7a-08ee8dfcb7cb | -7.24162 | -57.66444 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ef8f737-f7ed-3799-9a08-89c9729f679d | -9.01007 | -59.54205 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0f07145-ea1d-3c61-ac4e-fd67b824d3f3 | -6.92364 | -59.14291 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66bd554f-09b6-3d85-a2e4-8634cec9ee8f | -7.95601 | -63.46426 | 2025-08-15 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cc56931-8a31-3ee0-9f4b-c07ffce39b76 | -9.16708 | -59.68006 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81acaa70-b734-3ea0-ba10-ec2621380837 | -12.68242 | -44.9594 | 2025-08-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f761bf25-3be7-32de-a50f-1a8ec4bc7ba2 | -9.17358 | -59.69444 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87224056-7a2e-3e58-8bc8-2e5f02e77484 | -8.94217 | -62.23256 | 2025-08-15 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88ddc2ed-6470-3cda-ab33-bd21dc49bfe6 | -6.91559 | -59.1372 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4104c6e-845b-30f4-abca-2b8763726552 | -8.60426 | -62.65687 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 667e7a84-e745-3515-a7ca-d73b1b38b162 | -7.03421 | -59.85326 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474f379b-79dc-3503-9573-bacdf3346c10 | -7.56799 | -47.06394 | 2025-08-15 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b9d66c1-b8c4-36e1-b9b0-e7ded738ebd5 | -7.96103 | -61.76907 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67a77291-2e1e-39b3-9f61-a5b445b5e304 | -10.32609 | -64.44884 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 453f7ac0-cc07-372d-a432-9126f51191e0 | -13.11492 | -57.13999 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67b03ba9-9227-3108-8680-e796d7558a38 | -6.70373 | -58.81865 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e27ad0a4-aa6a-3e01-897d-06cf4db6927a | -7.42516 | -60.01395 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3dd5bea-32f8-30ec-804d-97ac09a331f7 | -6.91989 | -59.53355 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 177c3598-a0ee-31a3-95b3-5d62e0e58818 | -9.15092 | -59.69491 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d435ef1b-e183-3413-aeff-e139c34a4c39 | -8.94159 | -62.23576 | 2025-08-15 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7160a05e-be05-32c1-9173-660147adc0a3 | -9.17432 | -59.69019 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a78005e4-5766-3c1e-85b3-695d6827f5fb | -12.35431 | -49.9096 | 2025-08-15 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df53f405-ccb8-3695-9938-5c054d0fdaf7 | -9.1621 | -59.65715 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bba9e5cf-7b87-3f7b-8d30-cc2affa64569 | -9.18453 | -45.3285 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d1504701-bbe6-3046-a4de-16fe83f96f4a | -9.93843 | -60.4905 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4e82b27-3651-32a0-ab0f-17ef5de820eb | -9.17069 | -59.68513 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b03b78d0-dabc-3bd5-aff2-5253c6446ee0 | -9.17145 | -59.68085 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdbedea7-739d-3de4-af58-aaff34280c4a | -9.18773 | -45.32834 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0e245748-3ae1-3336-ab14-3723ad1637bc | -13.11423 | -57.14411 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5bfa164-cc31-350e-ac8d-716c8a6a6e10 | -7.43081 | -60.01419 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7071a758-43b5-3f38-b51e-69107b6690c0 | -12.63365 | -54.07663 | 2025-08-15 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e588d337-a750-360c-a555-a4ce178e5d37 | -9.2072 | -59.65655 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6752778-b749-3a63-8aae-7cded7ac0c49 | -11.93214 | -63.24713 | 2025-08-15 04:51:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c80d125-0b12-3181-b902-373b1f708136 | -9.38629 | -57.85445 | 2025-08-15 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eefc2afc-a298-33f2-b243-430a183001b7 | -9.39071 | -60.55062 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1163ae95-bfc5-3af2-81d4-eb2afa35bd95 | -13.33129 | -45.23624 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7177d4d4-230e-3324-865a-01c7354bc781 | -11.35141 | -55.42607 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49e2a5f6-31d8-36ab-b8eb-d81ebe85970d | -9.16633 | -59.68433 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 308f57af-647a-303c-81e3-a4bcaf7aa440 | -7.61052 | -63.52225 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edf72f8c-2843-3a8c-b491-64baad2e3f1c | -7.59543 | -63.50662 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40cd141c-b078-3bf3-a96e-382278c6591f | -11.91928 | -43.44198 | 2025-08-15 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33be003c-0b24-3325-9f87-e61840c80680 | -6.64544 | -59.08012 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edd799d4-1748-322f-ac8a-40135e617e71 | -9.15757 | -59.68282 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e3ae003-f433-3caf-934f-8f8d2d49bb2a | -6.72384 | -58.83046 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05137121-9108-386e-82f7-8d60d98e55f8 | -6.89009 | -59.15467 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb2c1adf-4236-3a24-90d6-41eacb452c28 | -8.10036 | -61.18905 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45b488f0-bfc1-3192-8752-356ee364d845 | -6.88937 | -59.15893 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bc15f38-4edd-3fb5-9468-87b214f7b1c8 | -6.96872 | -60.13037 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e33ba6-3fe9-339a-a0ff-4b369b6a0147 | -7.52987 | -61.32709 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 15c1f0f2-020a-3c17-aea8-1a52f7cc9917 | -8.55319 | -63.91769 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a1deb3e-913f-30f8-bd8c-e88fcb1768db | -9.1511 | -59.6684 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ae0a180-1b2e-3e6d-8fb3-4a330dcf66bd | -6.90101 | -59.14352 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b80c1b1e-d558-39d7-b28f-d0167d283846 | -7.30734 | -60.62196 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1867f7ac-1183-39f7-af0d-f26c1edbb2d6 | -10.352 | -56.48533 | 2025-08-15 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47428c45-f519-3982-9774-5c424cb1e4f2 | -9.51864 | -58.35288 | 2025-08-15 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 07b8477c-7ccb-3cd5-bcf2-f46c499f7ce8 | -10.00722 | -59.22292 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 049407fd-8f2e-3d4b-9a99-60ce4f2f03b7 | -6.72745 | -58.83532 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7f65bacf-b800-33d7-a664-311bd878310f | -7.88009 | -61.82648 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbea2ba8-07b6-304f-a1ad-8fbcfa32187f | -7.87546 | -61.83041 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README47.md)
