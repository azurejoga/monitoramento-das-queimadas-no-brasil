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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 345476f1-48b1-3004-a44f-cfd45bb2931c | -5.41653 | -41.14626 | 2025-08-27 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03bf67d3-5e3d-3dc6-b5bb-830bb84668c9 | -9.585 | -55.37362 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f52983be-7d20-3b24-8879-fe3aa852c995 | -8.08211 | -44.82543 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63b17170-7636-3428-8781-7bc85b9d3949 | -8.45172 | -43.68626 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0899eae2-f374-33bf-a00e-21e0c8ed2812 | -11.6278 | -44.85962 | 2025-08-27 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4341394e-c706-3a95-9f59-da4677f399c7 | -9.56334 | -55.38055 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4063ba6-50e7-3e22-bc6d-973cada38087 | -8.87987 | -60.77174 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71400cdd-cf39-3bea-b981-eac926cfe19f | -7.59141 | -43.94956 | 2025-08-27 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d139d5ce-d261-3edc-ad83-0044739bffe1 | -9.17628 | -59.51582 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7eefda9-6551-3825-a1a8-35c0a5afe4bf | -6.24869 | -60.02142 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 317dca09-c513-3b16-be41-6bd4b10b50b0 | -7.43495 | -42.04389 | 2025-08-27 04:25:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c707e400-3e2e-3fc4-b0b8-9d7426d78a02 | -6.79068 | -44.34266 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce61b389-dd20-3884-9960-f987771e3e37 | -9.58538 | -55.37271 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcea2c54-c7f4-31e1-a765-5d4a9516fff6 | -11.24856 | -44.98312 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c39c575-c3b2-3d1e-9134-79af31818893 | -6.80866 | -44.99981 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 982e1456-6085-38fe-87c2-f38958e9deea | -7.14549 | -44.14921 | 2025-08-27 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d59a470d-39fb-33c5-8c60-67bbbbfcd431 | -7.34915 | -57.63473 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6a9c345-b6d0-32c9-bae1-3944722bc492 | -7.89535 | -45.87286 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da0ee1fc-8550-3551-9a60-6f187cfb9341 | -6.24446 | -60.01888 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df2fd1b4-4547-3a5c-9055-42bc3ecebee2 | -11.24389 | -44.99051 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5240f1c4-4a86-3aa5-83c3-e3337ea5e179 | -8.08249 | -45.00679 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae7d32e8-1ccb-3979-8c79-b296cbdd190d | -6.62387 | -53.32878 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| beb41d17-c585-3057-9ced-6fa6622015ed | -6.35731 | -55.8047 | 2025-08-27 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25cf996d-7810-30e0-969c-cfbe4012fbb0 | -5.11964 | -43.20625 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 963dd471-3c3c-35d8-9913-abfb0798aeec | -10.65518 | -47.19944 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25e5d685-91ff-3fda-9931-bf36a10654b6 | -8.90071 | -60.76311 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62651e1b-40dd-3302-a160-74a8a8eebad2 | -6.88868 | -44.43391 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88053642-d5ba-3cc9-b530-7b1c6af8c8d8 | -8.27763 | -45.05916 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f1d4d3d-dfbf-36a0-b2b7-50ab62e9fb6c | -6.63222 | -53.33498 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b60cdb26-91b3-3ea3-a8f3-82edcb3f54eb | -6.9402 | -59.56347 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8dd8b46-7b20-3172-b501-6ef894ec0d60 | -10.48617 | -51.60524 | 2025-08-27 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 15ae2f2f-df8a-3ab5-9bf1-5a61d51bcbfe | -9.08739 | -49.57336 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8991d25-6e82-304c-ad0c-b910e4da6147 | -4.79007 | -47.27159 | 2025-08-27 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa3518b8-697e-352e-99f1-d73dde515fd7 | -5.66283 | -47.49006 | 2025-08-27 04:25:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7d48237-d8db-3bd8-9eae-076e9ae9e066 | -3.80494 | -51.26445 | 2025-08-27 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2cbfa93-9d6b-340c-8ef0-225b6c361996 | -7.17159 | -43.85768 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc9c9586-218b-3897-b96b-ac05975b2577 | -5.59492 | -46.33575 | 2025-08-27 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 179ee9af-de43-3f42-b853-c5e035ab652a | -6.28939 | -43.78403 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82ae0674-2f34-3782-9d60-175ef7f2913f | -7.4699 | -45.00367 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae2f20ee-59e0-3484-80cd-8d3665259f03 | -5.76082 | -53.76648 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f03aedd-ed9a-31a6-9eea-82c01b17dd4e | -9.08937 | -49.5615 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b99a4ff-2175-32ee-9bd6-a4618355507f | -7.64845 | -42.67597 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 021559b7-7699-3603-afca-bb040ff1e200 | -4.9164 | -42.09205 | 2025-08-27 04:25:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 079ca82b-ecf9-3c4f-b3be-46b9122a53cb | -9.07188 | -49.60044 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9fe84e4-4115-3a2d-aa31-f9724480c0c4 | -11.24447 | -44.98657 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d756113-ed15-3278-a88c-529a7cd8bb7a | -6.87816 | -44.98507 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc35a6a5-622e-35e9-a9d6-49903908fda6 | -9.16658 | -59.46178 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6868c63-d872-3fdd-989c-424b599c0f1b | -8.48043 | -43.65083 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02cd14df-7f60-3f8b-8aa3-a20c5b35c284 | -8.8869 | -60.77319 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c5ed436-6518-371f-983e-a4a32f30bfb3 | -9.19053 | -60.80692 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 837907f8-ae1f-334b-a373-374a6a7c18aa | -9.27905 | -56.9094 | 2025-08-27 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2234c621-9dfd-3670-9dad-ca6b2ea93abd | -7.17093 | -59.73987 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc771f1b-f5b7-3de9-9ce4-9cfd23aac8d1 | -7.70411 | -45.77149 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 25fc63f3-1a17-3d11-96fd-e2869410edef | -7.65868 | -42.65854 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5d56530a-4242-38b0-9657-9937e67a4068 | -9.08805 | -49.56941 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e82bc5e4-100f-3267-abce-6d4dbe83a36d | -6.712 | -43.105 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2269100d-f794-3a01-ab8c-0d8dd582c6af | -6.29061 | -43.77615 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cf84cb4-6411-3ecb-a373-a4b1b446738d | -5.82193 | -44.10628 | 2025-08-27 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a172208-cb03-36c6-99a4-f420039bcc82 | -6.5228 | -42.97397 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd2de8e5-bc91-36e5-af94-576fbd53fcea | -8.73271 | -49.96395 | 2025-08-27 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89441f0f-ba62-304b-912f-1c7354bbf8d7 | -4.31317 | -48.10453 | 2025-08-27 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 27cf0936-d115-3d0b-9d2b-bb750f15d34e | -6.96454 | -44.09976 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee83d8c1-8374-3302-a0ae-854e51008f34 | -7.57445 | -47.49601 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 624abd6e-a738-3f39-a6a2-6d31c5fee134 | -9.18285 | -59.44774 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d2fa5f5-57fa-3741-8670-706a8ce4efdb | -6.8818 | -44.43291 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c81b43cf-428d-3095-accd-d376ee39ff12 | -9.09376 | -49.57849 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2e04c2f7-db37-3c78-b3f1-6ebd151a3478 | -9.15325 | -59.56403 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1b842da0-53b4-3aad-8844-3fb0587bec78 | -5.11315 | -43.20111 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f20b75e3-0ab0-3384-9ab2-6ec0839715ac | -10.68494 | -47.13971 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0683b861-fd22-3676-9653-f8cd00508a3c | -7.01095 | -43.1065 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c820152e-a218-38de-a821-010ba4459a9c | -6.43749 | -44.56792 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e78f0c6-b733-3d38-ab8c-3c7789856aca | -8.91688 | -46.65662 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 477cc218-8023-31b5-98f2-a4b2c829527e | -6.49002 | -44.68426 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fc0a7df-897c-32b8-8ec3-1e573b0f9dcc | -9.94597 | -46.37108 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 453a7dc4-ebc8-32c9-bc46-0975b479608f | -6.6201 | -53.32338 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 274b32bd-0769-3598-ac85-cce1e6f7e6d7 | -7.1734 | -43.84564 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d187678-9f02-328f-9885-615e0bbb46d4 | -5.47341 | -42.60024 | 2025-08-27 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6edddba4-7fb8-3305-831b-0b50c33cb834 | -9.85769 | -44.59694 | 2025-08-27 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa1631e-aa3b-31db-92f3-870a54dc3341 | -7.17632 | -43.85016 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8251b954-256a-3164-b106-5c05b1b9bcce | -6.79127 | -59.63837 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06725411-75ae-3bee-a899-dca8371d4fc7 | -11.24331 | -44.99444 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9775a0b7-cb4a-348b-9e35-d9c80851e135 | -9.58884 | -55.38225 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26b132fc-23a3-3723-8537-85f8075e2000 | -7.47783 | -45.04206 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ab49019-2d7e-3c38-93b4-203fec52e18f | -10.08444 | -47.26517 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaa877b5-deca-310f-b8f5-f39ee8db3df2 | -9.84885 | -46.45 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc476f98-7eb7-3478-a6ad-5fcaddfef9d8 | -9.59052 | -55.3717 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51839c72-d159-33ba-92f3-9e369260e3b3 | -9.16947 | -40.60376 | 2025-08-27 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4ef4b80a-74ff-3601-aeb6-c688f575d0c1 | -7.16249 | -45.15322 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2b3fd33-fb55-34ad-8ed9-9020d9868cc7 | -5.68656 | -40.97729 | 2025-08-27 04:25:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b217a61f-19e7-3082-ae13-f4ca768e0287 | -5.57713 | -45.67097 | 2025-08-27 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4859fb50-1631-37b8-a722-6a6e86d958f8 | -10.65574 | -47.19594 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1547e199-bb4b-3fee-ad90-bc0ef3a1d628 | -9.15435 | -59.5584 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 12d2f5d3-f09c-3512-9069-1a23625d440d | -6.79294 | -44.3509 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3427d699-b4b9-345c-9535-cce562dde338 | -6.18852 | -43.00842 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c010cd9-404c-3ded-b107-6a7f6a9b4162 | -6.81562 | -42.81491 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d7a3b4b-bd20-326c-9c00-015484f6c673 | -7.63945 | -42.68128 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4aefc765-6497-3ac2-a25e-d0eae12fbc84 | -9.07065 | -49.56349 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3db1d652-6434-3107-9c20-afd023143e3b | -11.24402 | -45.4823 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| caa6ae75-2d47-3d6a-a806-7c2ba74c8d3e | -6.13022 | -42.95147 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6134256d-b611-3ec6-b24d-7ee4366d02e5 | -6.82148 | -58.98058 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README43.md)
