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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e345bb08-2a85-3031-b081-9fec2db1fb07 | -11.88063 | -58.7139 | 2025-07-17 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adc056ee-39e5-3cf1-b8fc-0396fbf44366 | -7.88273 | -55.37144 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3009b264-dd0d-3d75-9ff5-1354c659d92b | -7.50801 | -55.01279 | 2025-07-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a20e59a4-8a62-3f54-9dfe-2bf9ed40e775 | -14.957 | -56.40411 | 2025-07-17 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d769f84-59fe-31cc-8ed8-f12b0f509f1a | -14.95741 | -56.40064 | 2025-07-17 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 273b379f-0986-34c9-a452-8dd026338d0a | -18.65325 | -55.73205 | 2025-07-17 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a06dd103-e8e5-36e7-9f4e-66030c82d913 | -18.65911 | -55.73271 | 2025-07-17 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3e8c53f5-61e8-315c-bfcb-af76eab3daf2 | -13.20776 | -56.63742 | 2025-07-17 05:38:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94fe23b8-cb05-3468-864e-c03db98a16ca | -5.6567 | -43.7161 | 2025-07-17 05:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| ab549405-9d01-3631-be3a-68b1920be431 | -17.3628 | -44.1399 | 2025-07-17 05:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| af085154-7284-3c6c-9f9a-a3a599f2f6aa | -3.3772 | -47.4792 | 2025-07-17 05:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 53c430b6-668d-332b-afd9-5e245599457b | -5.6754 | -43.7147 | 2025-07-17 05:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1c23e79a-8f0d-3b3b-a63e-5620aaf1e4a8 | -6.7194 | -44.3231 | 2025-07-17 05:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d0b722ce-01d1-3671-b866-8abfdef583e6 | -19.9623 | -48.9949 | 2025-07-17 05:40:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 13c6e8ea-1ace-3500-a85b-249f3f8ddd88 | -6.7194 | -44.3231 | 2025-07-17 05:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 23a2c208-32e2-3aea-9c7f-a5e5c7d96aaa | -19.9623 | -48.9949 | 2025-07-17 05:50:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7bc46148-b255-38d2-93cc-44482d9d7c9a | -17.3628 | -44.1399 | 2025-07-17 05:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 897408b7-1a8c-33a7-a048-99473ad4b68a | -3.3772 | -47.4792 | 2025-07-17 05:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 60987c07-fba2-371f-9fae-0e8e6a629e6a | -5.6754 | -43.7147 | 2025-07-17 05:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 07413237-3c19-3fca-b650-3c19e4e78f7d | -5.6567 | -43.7161 | 2025-07-17 05:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e4b6c366-0083-36d3-b7d1-aa030a02d3db | -17.3628 | -44.1399 | 2025-07-17 06:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b619c270-b203-35ca-9fd2-80f1f8b35c2c | -3.3958 | -47.4785 | 2025-07-17 06:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 27451ef7-b31e-3c0a-8b7f-4813fd5bdff3 | -6.7194 | -44.3231 | 2025-07-17 06:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c86d4035-f6c0-3f8b-b146-52a6d0a93864 | -19.9623 | -48.9949 | 2025-07-17 06:00:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e653388a-52fb-3f6d-86dc-2df09f4761df | -5.6567 | -43.7161 | 2025-07-17 06:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| f64f0f4c-5a6c-3439-86d6-d9a1a75ee0bd | -17.3628 | -44.1399 | 2025-07-17 06:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 45.9 |
| a2547e08-8e69-359a-896d-1d045423bcc2 | -5.6567 | -43.7161 | 2025-07-17 06:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 666d59aa-24bf-3ffa-b29e-2ebeea16f64a | -3.3958 | -47.4785 | 2025-07-17 06:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c6f1d7c8-036d-38fc-bfab-77b4d2f63306 | -5.6567 | -43.7161 | 2025-07-17 06:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| eea5322b-11dc-39fd-9974-798168302ba0 | -3.3958 | -47.4785 | 2025-07-17 06:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 4d631ee9-37e2-3220-955d-69dc865d0a05 | -3.3772 | -47.4792 | 2025-07-17 06:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 7fd419f6-ca69-31f6-af62-09801a63beb4 | -5.6754 | -43.7147 | 2025-07-17 06:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 680934eb-a0ef-3599-969f-a07132f2da7f | -11.95003 | -63.83997 | 2025-07-17 06:27:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a4042db-d098-39de-b7d2-3174f7756a39 | -11.94559 | -63.84401 | 2025-07-17 06:27:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a356409-0703-3cfd-be89-82dd9a1126bc | -11.93845 | -63.84304 | 2025-07-17 06:27:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a39d17d2-7ecb-3672-92f8-78be31b5905e | -11.94925 | -63.84706 | 2025-07-17 06:27:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ae5defec-9154-350b-8180-4aeb93202d43 | -5.6754 | -43.7147 | 2025-07-17 06:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 881b174b-2400-3495-8e64-2fcd3bf19075 | -3.3958 | -47.4785 | 2025-07-17 06:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d724b85d-f998-37c9-aecb-6e9dd5ead09b | -5.6567 | -43.7161 | 2025-07-17 06:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 5e8b6c49-8bce-3b2e-885b-e8b38c893ed2 | -5.6754 | -43.7147 | 2025-07-17 06:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 628a4f2f-8748-3391-b543-442dd992adaa | -5.6567 | -43.7161 | 2025-07-17 06:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 74fa7e43-1768-3fac-ac7f-e4710b219887 | -5.6567 | -43.7161 | 2025-07-17 06:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 29757ab6-3ffe-3bf6-9600-bd1b2bd097de | -3.3958 | -47.4785 | 2025-07-17 06:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 6f68c6e9-8758-3812-bb05-146cd8cd2921 | -11.87597 | -55.44986 | 2025-07-17 06:59:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 0232c3b8-0925-35d6-b58c-427f3890fb91 | -11.86862 | -55.44137 | 2025-07-17 06:59:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 48a76099-79b6-3722-91a1-55e8c8d54d71 | -5.6567 | -43.7161 | 2025-07-17 07:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| de968578-b84b-3e38-ba9a-fc58f47b52b0 | -3.3958 | -47.4785 | 2025-07-17 07:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 2cf6d4cf-d96a-38bd-852d-6e87bf24d562 | -3.3958 | -47.4785 | 2025-07-17 07:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 05f79099-2e9e-398c-85c5-c92aecb8ba76 | -5.6567 | -43.7161 | 2025-07-17 07:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1a70e10a-0d6c-3186-833a-9e15f6d0de06 | -3.3958 | -47.4785 | 2025-07-17 07:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 247441c7-f461-3c54-af45-27e8f24b5461 | -5.6567 | -43.7161 | 2025-07-17 07:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f123885b-b335-3ef9-adb3-274f5bfe643b | -3.3958 | -47.4785 | 2025-07-17 07:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 46191557-70ed-32a4-bfef-002add7a7131 | -5.6567 | -43.7161 | 2025-07-17 07:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 011511c4-e2db-3807-b474-5c29a843a7e6 | -5.6567 | -43.7161 | 2025-07-17 07:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 25179063-edbe-3941-93db-a60e46181bab | -5.6567 | -43.7161 | 2025-07-17 07:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c76cc0fb-03da-392b-b9a6-c548127cb64c | -5.6567 | -43.7161 | 2025-07-17 08:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| bb371604-77e0-3842-a897-ac11f79ab523 | -5.6567 | -43.7161 | 2025-07-17 08:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ad08495e-808d-3a9c-9fa2-7d0801ea22c0 | -5.6567 | -43.7161 | 2025-07-17 08:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 43fe08d2-bde2-3226-8bf5-a4f15f15ab30 | -12.4121 | -45.3628 | 2025-07-17 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| fa4f738f-593f-352b-b9b8-a0dfd7103648 | -12.4121 | -45.3628 | 2025-07-17 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 6826b61c-d355-3e2a-a550-12575f6f81fc | -12.4121 | -45.3628 | 2025-07-17 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| e7e0d0bb-02d3-3304-bee6-c0f694f92910 | -12.427 | -50.0387 | 2025-07-17 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| bc38098a-0e9e-3691-ab96-d26e854fa30b | -12.8809 | -49.1977 | 2025-07-17 11:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 973baac2-e714-3918-88e7-88d470b531d8 | -12.4862 | -44.4928 | 2025-07-17 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 35adc3ed-18a6-375e-91bc-e7b3549de63b | -12.4121 | -45.3628 | 2025-07-17 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 1ef25cf1-88d6-3d55-a154-9e24474bdb97 | -12.427 | -50.0387 | 2025-07-17 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 3325522d-db1c-3d7e-9ed3-0564c5a953f8 | -12.427 | -50.0387 | 2025-07-17 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 4c1846ac-5879-3f2c-8888-71cfd8d82a17 | -12.4121 | -45.3628 | 2025-07-17 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| d26aec91-d693-3267-b16e-4f7692fcb36e | -12.4862 | -44.4928 | 2025-07-17 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| a3997cf9-51b1-3a46-954f-3ab79fca77c9 | -12.427 | -50.0387 | 2025-07-17 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 00b44070-fb55-3452-a6fd-f0edf19168e3 | -12.4121 | -45.3628 | 2025-07-17 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| ac47cd1f-33bb-3464-85c4-74ce930b182e | -12.4862 | -44.4928 | 2025-07-17 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 98e58467-a797-3af7-89a4-69ce8057d31a | -12.4862 | -44.4928 | 2025-07-17 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 0e36b767-eefc-34f4-8741-b467c3d7f8a0 | -12.4669 | -44.4959 | 2025-07-17 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 94da6c2d-a949-3f2c-8494-b7cb873d93e0 | -12.427 | -50.0387 | 2025-07-17 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 200.2 |
| c6c7ac5b-4a92-35b9-8dec-750ea992ebc9 | -12.4669 | -44.4959 | 2025-07-17 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 57d3e091-6d57-3a56-8969-882574467a50 | -6.1107 | -49.5804 | 2025-07-17 12:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a6750e7c-4c5c-3737-b428-1cf1871dfa94 | -12.427 | -50.0387 | 2025-07-17 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 5ae3f1a8-6942-3a03-b11d-36f63e6da8df | -12.4862 | -44.4928 | 2025-07-17 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| b51f1e3d-97da-36fe-9e81-e8e2274e79a2 | -12.4121 | -45.3628 | 2025-07-17 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| c1f5ff95-5d0b-3212-b55d-91f8eb5cfdc9 | -12.4862 | -44.4928 | 2025-07-17 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| edaea454-ebb5-334c-843b-66754a0539b3 | -12.4011 | -50.4725 | 2025-07-17 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1e89ae0d-5c1b-3118-8be9-e70570d97593 | -12.427 | -50.0387 | 2025-07-17 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 200.6 |
| aa9d28d3-5240-3078-a864-d46201ee827e | -12.4669 | -44.4959 | 2025-07-17 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 27bff353-e2d0-3d5c-a3df-e518f1850c6e | -12.427 | -50.0387 | 2025-07-17 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 68d20018-c4a9-3a19-a245-115da41abbe4 | -10.9784 | -46.454 | 2025-07-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 782198fd-e879-327e-8182-7dbcf187d6f0 | -12.4862 | -44.4928 | 2025-07-17 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e84cc7e6-9577-3958-ab02-92c15bc795c2 | -12.4011 | -50.4725 | 2025-07-17 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6cee27a1-d6f3-3147-b78f-d4d458136e31 | -10.978 | -46.4766 | 2025-07-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ee3e2ce7-6479-380b-a264-9382746033d1 | -12.4669 | -44.4959 | 2025-07-17 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1abbcd93-ea5e-3a6f-b45c-5be9add0a818 | -7.22369 | -44.24949 | 2025-07-17 12:49:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 86889cff-25e5-3739-b36c-40e439297732 | -11.68537 | -47.96757 | 2025-07-17 12:49:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 7bf1aaeb-a524-3908-b3d3-1cf08555b70b | -9.41006 | -47.47537 | 2025-07-17 12:49:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| cbdf8401-8d0b-3203-8779-c08430fd8234 | -4.61287 | -43.30285 | 2025-07-17 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 0f68ea89-ad61-3f37-8981-955ae2eb22c7 | -4.85879 | -45.32659 | 2025-07-17 12:49:00 | TERRA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5c55830c-339e-311f-b115-54c091eda19e | -10.60631 | -46.24016 | 2025-07-17 12:49:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| cb845a87-d3cd-3590-b0f6-50b64d7b1e38 | -7.90092 | -55.42449 | 2025-07-17 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9dfd7f40-10be-3eb0-9a47-b37e30792531 | -10.97227 | -46.46801 | 2025-07-17 12:49:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9fb089f4-b4b0-3e5d-8d64-2fc169156f43 | -4.30168 | -48.09626 | 2025-07-17 12:49:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a35be136-7699-350c-bbc2-533d2b4c7755 | -8.24025 | -46.21412 | 2025-07-17 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |


[Clique aqui para ver as próximas entradas](README32.md)
