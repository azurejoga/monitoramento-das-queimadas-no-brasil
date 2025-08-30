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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71542017-f503-35a2-8d27-04c8a5749ed6 | -6.56104 | -43.67942 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8e16d37-269e-34fc-96a3-7b98d6bfd52f | -7.26311 | -39.67549 | 2025-08-30 03:28:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc406dfb-859d-374d-b996-dfa1e6a3e833 | -5.53544 | -36.85454 | 2025-08-30 03:28:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b861d616-0726-3acc-9279-7e414311804f | -6.59113 | -43.65493 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 186d0b1d-7cac-3dff-b8bc-1271db4ff328 | -6.62099 | -43.73851 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1590a001-08ea-3ff8-b38f-a34e0679db35 | -4.98577 | -38.60643 | 2025-08-30 03:28:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 44eada54-38cb-31e3-aeaa-cb477210ffbd | -5.91854 | -43.36007 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42d8deb7-3014-3f2a-b8b2-671a6ff4d53f | -6.27515 | -44.46763 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d79ec14-2e32-349d-b5bf-f31bd4e28754 | -5.61069 | -45.01007 | 2025-08-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4469c1ea-5346-32f0-9281-ae211d2781bd | -5.04702 | -37.99808 | 2025-08-30 03:28:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e588c4d-4fbe-3d1d-96b8-5cb6aa01a7b6 | -6.09497 | -43.32773 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e5815ee-9761-3b12-a732-1c29d10617f6 | -6.77482 | -43.78848 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30d4fd76-14ba-37e8-8e99-e4989931798f | -3.72433 | -38.67849 | 2025-08-30 03:28:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b54d8fc7-587f-323e-b642-1aa96cea3ba6 | -7.82575 | -35.82184 | 2025-08-30 03:28:00 | NOAA-20 | SURUBIM | PERNAMBUCO | Brasil | 2614501 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 25031b19-c086-351a-9462-6a2a601557e4 | -6.78373 | -43.77491 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d66e79a5-c465-38da-a923-c9f5bfc6da3d | -6.17602 | -43.33372 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3b52fc11-40f2-3a79-8add-10ab4c286847 | -6.59883 | -43.64777 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2ecd1789-fd5f-3f73-b6e7-88a9617d5b07 | -5.82772 | -41.26411 | 2025-08-30 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 836275a4-3e15-36fc-8162-8d168994490a | -5.99894 | -44.72791 | 2025-08-30 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c88a49b-dd78-36b9-adc6-1a2379b6391c | -5.9923 | -44.7266 | 2025-08-30 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df472b69-74e8-3c5c-976d-54d2f3023ac6 | -6.79526 | -43.78219 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed90ea2c-5ec3-3da4-875d-386c13ce5740 | -6.24894 | -43.38279 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae158655-0aac-38cf-b296-2a1342d91ceb | -6.69378 | -43.08755 | 2025-08-30 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1c739fe7-1173-32ce-911b-6dc696efe54f | -6.49796 | -43.54161 | 2025-08-30 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5144dc5-809e-3090-99b4-0fe75722c6bc | -6.55913 | -43.68983 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8488f68b-4a07-3755-8f6b-d88fb6dc4f69 | -6.2144 | -42.76557 | 2025-08-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 252f33f1-023a-35cb-b576-3dfea5f263bf | -6.61479 | -43.73721 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f66aed89-28b8-38fa-959d-74455f9938d1 | -7.40508 | -42.05972 | 2025-08-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b1e7e84-62fc-32ed-9ac5-b4b2763bab43 | -6.17767 | -44.86326 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d913328b-670c-3268-9aee-927e480eb57e | -5.8271 | -41.26764 | 2025-08-30 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc45af5a-836f-3d34-a1b2-0ebab6b9258c | -5.69432 | -45.96565 | 2025-08-30 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3682182b-7e5d-3738-bc00-41afd0224a08 | -6.78193 | -43.78474 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4a4d2a8f-6744-30c8-b556-7eae5bd748e4 | -5.60405 | -40.81494 | 2025-08-30 03:28:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab9440b4-872d-32dd-a3fc-e1701a8d1e66 | -6.80149 | -43.74791 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbddbf26-31a9-3f87-8ef2-f4267251e7e0 | -6.18695 | -44.00214 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 066ee1a0-7363-3103-984d-e6f6190ba86d | -5.60954 | -45.01641 | 2025-08-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ea3db756-af13-37ba-8c4e-f4ce4f966ec3 | -6.23109 | -42.40435 | 2025-08-30 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d44a5c5c-917e-32b9-b2cd-94d7e12a1261 | -6.00004 | -44.72206 | 2025-08-30 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31a3245c-b01a-3877-84aa-e040ec16c7a7 | -5.99691 | -44.72085 | 2025-08-30 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e872491-7a69-315a-ac47-52c567d7b9cd | -6.23558 | -41.81384 | 2025-08-30 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c057973-db7c-32ec-b742-55318e9970be | -6.78104 | -43.78967 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ed3bc378-b808-38a3-9635-7fc43642c931 | -6.23489 | -41.81772 | 2025-08-30 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a86afd2e-1c89-3fb4-aa63-c05461bc6618 | -5.72231 | -43.94155 | 2025-08-30 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6292a43d-46fe-39aa-b8ca-3e1ab4edbe4d | -6.78283 | -43.77982 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 4ae766d6-109d-3041-9f4d-a673a4f57d7f | -5.21316 | -35.51671 | 2025-08-30 03:28:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e57c7c78-d1f1-3338-af8a-069b87c0582f | -4.96441 | -37.89938 | 2025-08-30 03:28:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14ecd4da-f2a1-3f5f-be35-d08a15552c51 | -6.5951 | -43.6403 | 2025-08-30 03:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 32164f68-fedb-3017-8490-909c45e3c290 | -9.4435 | -60.5307 | 2025-08-30 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| afcad3fc-1879-3142-b34c-0c8334e8dc3f | -8.9126 | -62.1058 | 2025-08-30 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b25b794d-4ece-3f0e-b732-bd1cd94304ce | -6.1853 | -43.3257 | 2025-08-30 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 776d8539-8b72-3592-a50a-34e425995801 | -13.3817 | -47.015 | 2025-08-30 03:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9328d135-a591-32c6-aaee-df0be67dd94e | -9.462 | -60.549 | 2025-08-30 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| ee2f2a4d-57ae-3f70-8987-2a21688ad61e | -6.7814 | -43.7865 | 2025-08-30 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 0c0d1262-cfce-3513-860e-25dc959c534b | -6.185 | -43.3491 | 2025-08-30 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 95367b5f-f0ab-3d67-a508-47282bcfdf2f | -13.3821 | -46.9924 | 2025-08-30 03:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 079d4b65-a3f1-3be9-8c4a-09b36d79bf03 | -9.4432 | -60.5692 | 2025-08-30 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f8420c52-2b82-31b9-9b3b-462f3f6eb117 | -9.0614 | -65.4355 | 2025-08-30 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d2970acb-f494-3911-9928-b7044adecc27 | -9.4247 | -60.5509 | 2025-08-30 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a3766ce9-ed78-3781-ab75-df00c4af9b32 | -6.1665 | -43.3273 | 2025-08-30 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5006ae9b-1b2d-3f9a-b7a8-f56a25ededd2 | -9.1155 | -65.7699 | 2025-08-30 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e3b273c0-f772-381d-a23f-3d32ca649044 | -9.4433 | -60.5499 | 2025-08-30 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 3c062df5-b6a1-3edc-8c15-b1befc8536c8 | -13.3825 | -46.9697 | 2025-08-30 03:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| eb545b4c-b07c-3a5a-99ce-05977df43e4c | -9.31359 | -40.21207 | 2025-08-30 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 333881f7-a248-36c1-8045-a45ea0d5db11 | -11.33007 | -43.59819 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 215a2743-7683-3fa3-a3ce-448106047840 | -11.87869 | -46.39211 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 177a7307-79c2-300f-b648-49c86348dbd6 | -11.35469 | -43.56253 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7218ff1a-9a61-39d2-bcee-85f7ef4258f5 | -11.88035 | -46.45029 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7db91a53-98c1-39d3-8c57-0f81dc060b41 | -11.92903 | -46.68862 | 2025-08-30 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7e02e54-c4e3-3ccf-9f7f-3c3d50b63d29 | -11.33885 | -43.52251 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9740433e-9ab9-372e-8ad2-c844d1a2a9b4 | -11.29855 | -43.63834 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb1b07de-e06e-39a6-ad2a-6ca907c14e75 | -11.30509 | -43.63527 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fee56746-7b54-3f01-977a-b605f5642e0a | -7.11361 | -44.5996 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c6e8ff3d-2fe4-3e36-b65b-d0ba4492b8be | -11.3562 | -43.55468 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b9a7c83-f655-3e29-a963-741ed3ed4f9e | -11.31747 | -43.66318 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0ecebe4-e2a5-33eb-b42d-b614094d8d6a | -7.61254 | -42.73035 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b3fe287-5701-3eb0-906c-62920b0e927a | -7.95764 | -46.39507 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 978f3e7c-e71c-3fcd-81c8-75e2509b53d9 | -7.16878 | -44.15574 | 2025-08-30 03:30:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7799352c-2a7d-340d-97a2-e270a4b0d0f6 | -11.86448 | -46.39348 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 019303f1-ccba-3f32-99d2-9a4934fcc757 | -11.88854 | -46.3975 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ed1160b-153a-3a79-8c18-d5fea238a202 | -11.06795 | -44.61347 | 2025-08-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17d81ece-c63b-38df-8914-e7d0a989b474 | -11.84506 | -46.40575 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34460360-4f2b-3b23-b4ff-f6125342aa37 | -7.39272 | -45.93445 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aaac9f80-7f25-3258-83a2-379c329e5430 | -11.31907 | -43.6549 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1606b7d9-4f3b-356f-bf36-1b4f06e69408 | -11.57132 | -46.35363 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b223894b-c7de-376c-9008-c134bf2da89b | -11.77374 | -47.55874 | 2025-08-30 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aeb6212-1ec6-37a5-9b0a-0462963e72e8 | -12.00812 | -43.99598 | 2025-08-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3b4b5fe9-e6f5-311e-904b-1185d6bfc87e | -8.44166 | -43.65127 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98a61e5d-e005-3609-8c3e-00e48dd5d8de | -11.30402 | -43.61036 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 420ce577-ff15-3317-8718-ae54e3966b1f | -13.31569 | -43.01328 | 2025-08-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9cfbecf6-b483-3d08-b93c-037a6ddd8b3d | -7.11453 | -44.59866 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb415c7d-b8c1-3e7f-969c-a07584d431fb | -11.32454 | -43.6267 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8dd7fb4d-8fd7-3adf-aafd-fbacf110632e | -11.30324 | -43.61437 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e32c2950-b7ad-3386-b1c2-0b16fd858c5d | -11.31827 | -43.65903 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0784bcf-fe6a-3b8c-9bab-6cc223569ed7 | -11.30919 | -43.64465 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 926f46b2-aa9f-3775-8b6c-498e45e2686c | -11.33942 | -43.29052 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bd86de9-0b9a-368e-a6cb-654f6554cab3 | -9.31441 | -40.21332 | 2025-08-30 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 5e2d0c4b-15b5-34bf-97d8-c67b4f50c17b | -11.57985 | -46.36604 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9682e5f-8a97-3b00-87ab-94b0fdc0561e | -11.57865 | -46.37197 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d239681-1f81-349e-b4e5-b4be14964284 | -11.32607 | -43.61884 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d514447-1df8-39b4-8166-7bbb98025590 | -7.60177 | -42.72422 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
