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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f13ce46b-59f3-3337-b895-5616452a51b5 | -10.25933 | -44.37031 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dcdc997-02d6-3702-a5b7-b3bec434ff43 | -10.3557 | -46.94313 | 2025-10-07 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e11fa049-9199-33ff-bcaa-ae9eed3e1933 | -10.41492 | -45.39161 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bee99a25-fced-317e-85bd-edf2ae8ff388 | -6.98147 | -42.86666 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4068d042-7d97-34be-8a8a-941ae49c35dc | -10.03828 | -48.28782 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 994efd70-b354-31ba-b2ab-ee8c1fe7a817 | -6.64851 | -43.99563 | 2025-10-07 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a92535d-e4c4-30bc-a59f-f8ae613f4926 | -5.25682 | -46.48886 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a40edb6-be93-3f76-9838-fcfbb9adc8f9 | -5.49299 | -43.07455 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 8b7f72aa-2fab-3073-95e9-595ef7ee422c | -8.20747 | -46.98979 | 2025-10-07 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6e07fe84-f7b6-32a4-af5e-5bff5310394f | -6.72728 | -42.81913 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 388786fc-666a-3da0-82fa-93937145f719 | -8.91049 | -50.60707 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb824b0a-903e-3ca2-8b38-c3b75f8df31f | -8.96914 | -50.80105 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1e37739-313d-3efd-ad6d-1272e0840f0b | -8.18735 | -50.30466 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 864b662a-5b50-3450-bb08-9db221fdb103 | -10.18637 | -45.53074 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60100ca9-55ae-38ef-ad7d-cfcb6b703809 | -10.25085 | -44.37402 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e53a50a5-0ab8-372e-b084-33d053f41b86 | -8.18018 | -43.35128 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d80ea4d8-be3e-37bd-82bf-83865457fc31 | -9.18658 | -47.82811 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0c32895-d1da-3fae-998a-4efa11952928 | -7.00432 | -42.84809 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf6ad09e-ef80-3d4c-893e-80ab533a7fca | -10.29557 | -47.9621 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dade98ed-df1c-320d-b55e-9ff1e8929b0d | -5.49224 | -43.07956 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f8c49157-4fd8-3ad0-89f8-58bb2cf996f7 | -6.24076 | -43.27626 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d583363-28ee-344c-8bfc-9d08d9b0603d | -8.55823 | -50.08521 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15b7f09d-474c-3e4c-ac13-267b9289ec46 | -9.78113 | -48.28613 | 2025-10-07 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ffb8f8b-d060-3e63-a1a4-b1e57d3a1ded | -5.23857 | -43.74479 | 2025-10-07 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea6a0861-2560-359a-93b0-ffa13d0b5e2c | -5.75632 | -43.39199 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 66f7604a-a019-3ad6-a837-b3f208487dfb | -6.45485 | -44.59004 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f792203-8c6c-3a35-9c30-e565c3ad4f0a | -4.56559 | -55.96107 | 2025-10-07 04:36:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54333f5e-13a3-352b-b071-485a8cfc7ce1 | -7.52102 | -49.90773 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e10e9d10-159f-3718-a67d-c893361172bd | -8.55882 | -50.08151 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff6c58a9-6f09-3c4c-8cd2-1dbe3943ce7f | -8.87783 | -46.77776 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2caf5cd0-165e-3c5d-b9be-8a2c58bdb888 | -6.72121 | -42.80358 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 027e2131-eedc-3755-8704-1d1a2d204870 | -8.85036 | -46.09612 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f96014d-a69c-3863-b6a0-d3d23a78f762 | -7.02456 | -42.7951 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b0c3bfaa-f0c8-3f4b-a866-7d85a316cfd8 | -3.40621 | -52.72547 | 2025-10-07 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05fb423c-f32b-3324-b593-7688c281b4f8 | -6.24863 | -43.27754 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f979e7ab-2289-3cc7-b32d-207fa7c6a952 | -7.88985 | -47.81819 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f0ac4ac-9160-341a-9292-f1940957f0ee | -6.45787 | -44.5948 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2760647d-bff6-3936-beb3-9ab208090ead | -7.80416 | -44.14283 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7896818a-3b2d-388d-b877-4156e1ebb1f8 | -5.45615 | -42.79127 | 2025-10-07 04:36:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 72556a73-24bd-3e39-9a7c-14ce48c8c29d | -10.4125 | -45.38242 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a5ca0122-8783-3fd5-8d48-89e820d139f7 | -8.1742 | -43.33595 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d610e299-14c5-38b4-b1ac-c442236f5c1b | -8.1904 | -44.11552 | 2025-10-07 04:36:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 361dfcb1-cffa-3b12-9ac1-56a52ebdbd72 | -9.09254 | -47.958 | 2025-10-07 04:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58332002-1cd9-338e-a23c-e578d597d39a | -9.34195 | -54.52086 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39b3b211-5f0a-3388-8bff-6b92aaa1f2e6 | -6.67582 | -41.38677 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fd91a86a-e578-3d81-9aee-817065a809f2 | -10.23287 | -48.18824 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5a1f1cd-dbe2-3a4a-8047-fe75ff374cf0 | -8.61592 | -54.96217 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c29a883-94d0-3471-b5a6-89072881fd66 | -7.00453 | -42.7884 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8a6f85c9-9b5a-3573-b27d-f186ce080729 | -8.61416 | -44.93032 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af61d32d-690f-324a-809e-aa1a859c7761 | -3.46973 | -53.45321 | 2025-10-07 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 109ecd1e-a6b5-3a90-befd-609b73c2a583 | -6.98456 | -42.01069 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c51fa935-10f4-3225-b662-a498ad84a818 | -4.91151 | -48.02073 | 2025-10-07 04:36:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35ba27e5-480a-31ac-9269-7177853d75d4 | -7.88318 | -47.81714 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d8491e7-eb89-3ffa-a568-2652415e5bc0 | -7.7208 | -42.40559 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd74963a-554c-3241-958c-62341409edd7 | -8.65468 | -46.2996 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| deea2e17-d8d2-394a-a97d-60012e50dc29 | -5.76206 | -45.75188 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3df75b7-2452-3337-8b25-10f5ac2d423c | -8.54009 | -46.24749 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 421de8f0-e10d-33b8-b6e3-a641dee82ef2 | -5.51474 | -44.40899 | 2025-10-07 04:36:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b01764c6-ce2c-300d-ab52-679362dc00b6 | -10.26003 | -44.36539 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3ab3332-404d-31cd-bb84-0b69034c36c6 | -8.56164 | -50.08577 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 029d5d77-a4f8-3962-a75a-0f0f48789fad | -7.67184 | -50.21164 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec0ec32c-d41b-336d-b3ce-63af92a76a09 | -5.87074 | -45.19003 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e9df986-9821-3abb-a5d1-549be9bb473c | -8.41557 | -50.7016 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 52ea37b1-ea16-3f91-ad0f-ffab4eb4c1ad | -6.49668 | -41.55241 | 2025-10-07 04:36:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 58151aef-1033-3b40-9a87-00847ac8de12 | -7.67874 | -50.21278 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad895ea-5561-37f2-a26f-ab9d8bba9790 | -7.72194 | -42.39763 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 52d48b16-14b4-3d25-aa07-40204c01bae9 | -5.46066 | -45.27801 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeac0af7-511e-356d-9b3c-d5af3bd88864 | -6.71075 | -42.84639 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a1ba0e7-eee6-312b-8d9f-10f2a802289f | -4.58423 | -48.12223 | 2025-10-07 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8077af88-90e9-30cf-91d8-c2cdccd1137a | -8.48948 | -46.26795 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ffc4c29-bd72-36b6-b45a-6171538878fe | -5.84996 | -42.84395 | 2025-10-07 04:36:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 80d27d92-1a9e-39cb-a591-7bfc6f4bbd65 | -5.54714 | -42.68388 | 2025-10-07 04:36:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 11cedeb3-96d5-33c2-a375-30acabc39a80 | -5.23797 | -46.56591 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc60fe61-927c-333a-bc04-ab40a584b451 | -9.00556 | -49.21209 | 2025-10-07 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe55b117-3799-3dac-a677-da37258aa2cc | -10.41554 | -45.38733 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 381d9007-88a1-38b8-9f20-1a26b088d1c8 | -8.84919 | -46.1038 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6061ee2-0eec-3f46-b72d-51981a22c04c | -9.79168 | -48.28416 | 2025-10-07 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67c8ec1a-3524-35b6-9f03-0badee4eee5e | -9.78447 | -48.28662 | 2025-10-07 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6695a2de-5b98-32a3-960d-47b83c744a87 | -9.46996 | -46.02113 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71889d6d-2415-384f-ac37-629828273b34 | -7.68703 | -42.40582 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c78ee8bc-aaf0-3bdb-8bd5-d1553b126c90 | -7.61949 | -44.35059 | 2025-10-07 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff13c007-11f5-3d45-8c36-94d17d486a5a | -6.59122 | -44.62643 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fb4d6dfd-ac79-3c5e-abab-15c30bb3c416 | -9.40359 | -49.36684 | 2025-10-07 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c889804-9a54-3ee1-b5e1-470a1d704ba4 | -8.61936 | -44.93806 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d5e71315-8115-30ca-813f-b93f47701c54 | -6.72174 | -42.8 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8bc60f3c-d1ce-3933-a5ac-7b2717d00138 | -4.18469 | -55.69903 | 2025-10-07 04:36:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd4aca31-0bb3-38d5-8f67-91a2cc8620b3 | -5.21814 | -43.67617 | 2025-10-07 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44eb5b14-95d0-354d-a5b1-5d6566a26506 | -8.17701 | -50.30295 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3867fe31-d262-30e2-ba97-fe8d5b461e00 | -6.13219 | -42.67403 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5056b03e-348d-3669-800d-ea653c7310aa | -8.47222 | -43.7255 | 2025-10-07 04:36:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7f10aee-c9e0-32f0-b87c-a3e10a061718 | -5.0743 | -50.72416 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a5e1df1-fa34-37c3-804c-f347fa1efd01 | -6.98533 | -42.86389 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b1c68037-f5b4-31ec-8e4b-e7f389507f42 | -7.68989 | -42.40882 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5ecd5424-6d27-3df5-a736-96384e1acc77 | -7.46678 | -42.62098 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab99586d-f99d-38e0-a752-55d21f34c21a | -5.77654 | -46.15128 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b4414ba-cc9a-3f89-b4fb-2d22b2e7b6c6 | -6.33552 | -44.02664 | 2025-10-07 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfa8f47b-feca-34f4-af4c-9c7da52dafd5 | -6.7216 | -42.82935 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6017b8d1-6675-3e9f-a3e2-180055773d31 | -6.59554 | -44.62268 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bafe5862-081e-3c88-9be0-6f191b94e1b9 | -5.2486 | -46.56393 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e53d2df7-dbeb-3661-9c32-6e5c5ed559f7 | -6.75258 | -42.23306 | 2025-10-07 04:36:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README59.md)
