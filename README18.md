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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 399eede1-aa3e-378b-b2be-919d21bcd743 | -9.46128 | -57.83457 | 2025-08-04 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b12c1d5-17f9-31b3-90ec-a701e880ef1d | -12.43632 | -44.85324 | 2025-08-04 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 008684cf-b48f-33f5-bdd6-91ab6b1f3f70 | -11.78061 | -44.99474 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 850721b2-f2f3-3447-9e01-039c521c9edd | -11.74847 | -45.00606 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 752364ce-41f4-3f49-81d0-296a1d3fccfb | -13.04703 | -56.8868 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43e97cf7-f7a3-30da-bcc0-409674f58adb | -15.56428 | -47.08865 | 2025-08-04 04:36:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02e167e9-30c2-3b8e-b409-cb6226e28cd9 | -12.75882 | -45.88002 | 2025-08-04 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2caa927-d995-3e10-8507-0b470cf07b19 | -15.27024 | -43.07367 | 2025-08-04 04:36:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3d60b25-8c4a-3543-b5aa-d3ed9c85b8ac | -10.45372 | -47.22067 | 2025-08-04 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 80da6c0e-c4cc-3395-9e1c-51d7f2a0580a | -13.06505 | -56.89549 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfc5f64f-cf73-32a6-8bc1-6131e8c09267 | -11.40916 | -54.7182 | 2025-08-04 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 699dc557-9ffd-3ecf-a785-d3a06956fa0e | -10.6826 | -56.54975 | 2025-08-04 04:36:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da64795f-7fc2-3417-939a-80dc245dc0e0 | -14.62897 | -49.18063 | 2025-08-04 04:36:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd79514b-5317-3057-8f0b-5ea0eab2b8b2 | -12.76124 | -45.88923 | 2025-08-04 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df95b395-1714-3839-9c9f-1bbe3a153e7d | -10.2545 | -50.16476 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48467d9b-d5ba-3b26-9293-be984e58745d | -11.76134 | -44.9706 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92367624-97ce-3002-bf40-89c9874457b0 | -11.4153 | -56.86478 | 2025-08-04 04:36:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 304b885c-8c35-31e6-9500-b9c4a3e0b93b | -12.08008 | -43.36221 | 2025-08-04 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e1f1c04-0216-348e-b7f2-17aa1a3bebf9 | -15.07419 | -47.26596 | 2025-08-04 04:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53078e83-502b-35e5-ae91-1267f27d0e2b | -10.32864 | -50.07207 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b09213e9-8b64-3c2b-ac19-244326afd074 | -10.70868 | -48.30062 | 2025-08-04 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8084b424-4f1b-3280-a2bd-05c349b36c0b | -11.92968 | -44.94619 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5117bea5-c888-3496-b461-ff9edd84fb97 | -10.3332 | -50.06535 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b0cfece-6208-3524-b581-3d8ab43ae12b | -12.69298 | -48.08453 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22edfe53-f6d9-3fa8-9127-ac7418435a1d | -11.93037 | -44.94131 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2ef0427-5fb8-3313-984e-ccb4674012f1 | -11.77203 | -44.97701 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55e51184-17eb-3a51-a448-f8162fe7c6b2 | -11.22543 | -48.43349 | 2025-08-04 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be5caef4-c1b9-392d-8d34-580b257605a0 | -11.52832 | -44.34843 | 2025-08-04 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ada927a6-3a8f-3314-90ae-dd5a8c41b08b | -11.74936 | -44.97312 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f2135aee-e31b-3ce2-8f53-500b4af2c9aa | -11.93522 | -44.96195 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4428f524-5fa4-3934-9a0e-2e2096ce4c39 | -13.06046 | -56.89636 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdecc9ac-77ba-31ab-af5e-cb12397d84b1 | -11.76513 | -44.97119 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12b6b567-abc1-3d50-afc4-f41e053abeef | -13.02448 | -47.39702 | 2025-08-04 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90e820ee-db5a-341b-ae47-8413e86e572c | -15.76796 | -46.55936 | 2025-08-04 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92e6e0ef-9083-3176-b65c-effb0d4503b6 | -11.75003 | -44.96846 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 819a1d70-caf2-3148-b538-f7baa2f2ebfc | -11.75757 | -44.96993 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca38ce07-5b77-3b31-87d6-3abcaf34637b | -13.0641 | -56.90065 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb19b3f1-9983-3619-acda-e9d7b868e5cd | -14.50845 | -52.07178 | 2025-08-04 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6184d1e-02d4-3e7c-b325-93e36a8fe844 | -11.92892 | -44.97894 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8e91a65-f882-300f-94c9-aff905a8c514 | -13.03702 | -47.45315 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 418d126e-a6c5-35de-9b08-b9527df4f6ee | -10.33261 | -50.06899 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 107c9c45-7556-3d00-b38e-35d4f683f624 | -12.70422 | -48.10101 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4907d023-ed53-3433-9f72-e5e444d533df | -11.41011 | -54.71851 | 2025-08-04 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97ab970e-66eb-3174-94e6-c4b43cfcaafd | -9.27156 | -50.25587 | 2025-08-04 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9206a71d-7d25-36fa-9bbf-bfcc5531cbfb | -13.0652 | -56.89729 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8bde854-d86b-3ec4-8d7c-75d615aae053 | -9.46665 | -57.83558 | 2025-08-04 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec59ed2-ce85-3344-857d-b412d99a3154 | -13.2547 | -46.9698 | 2025-08-04 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79501e2c-2028-39c1-934d-bf2c1de50296 | -10.56466 | -45.26883 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7547463b-2bdf-3e8b-82d6-4bb176c40b93 | -14.84319 | -48.39119 | 2025-08-04 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3a3a73b-7022-3f13-aaff-50ca93c72037 | -11.78383 | -45.00226 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2016ea31-7c95-3dd0-9ec2-6471048e31b3 | -14.84656 | -48.39174 | 2025-08-04 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebf667ac-0e7e-3efd-8bdb-a1b540cc70b1 | -12.69913 | -48.08927 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16ba28f8-0be1-38fd-9caa-137b67f263b4 | -15.56191 | -47.08001 | 2025-08-04 04:36:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6b4b827-f511-3aed-a58b-49dbe1cb3621 | -14.84679 | -48.39487 | 2025-08-04 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2e34784-fbd5-31f6-9990-f0501ba1a2a6 | -15.27475 | -43.07422 | 2025-08-04 04:36:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6857960e-9877-32ca-8acf-29c6624b1f78 | -13.05178 | -56.88765 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fb9cb9a0-923f-381b-8ac4-102b44d70358 | -11.76445 | -44.97586 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 740dfbb0-d94f-37c6-b8d5-733fb40e3646 | -11.78449 | -44.99771 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47b0ed2a-953a-329c-bc25-9abc37b5737a | -13.25412 | -46.97375 | 2025-08-04 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbebe127-ab5d-31fe-8ff3-657c32419df2 | -10.29656 | -45.17624 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0143332b-c78b-3858-a25c-e4828a35efd2 | -10.24433 | -50.16308 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a639ada7-a110-320f-9406-bf1a8ccef81f | -10.29287 | -45.17575 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb153195-5939-3266-bef8-7bd127da691c | -11.75669 | -45.00269 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1060894-a657-3a45-8a16-72cd7529e424 | -10.57631 | -45.26618 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ba77b75-749d-3886-8b02-ff8382d93c44 | -13.05461 | -56.89885 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34702cec-e822-37ec-8f13-3dd56700844b | -11.22422 | -51.52939 | 2025-08-04 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be765068-e499-352b-a156-b826eb188ede | -10.32923 | -50.06843 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b8a698c-4af7-3e29-bc1b-12e57e2ad982 | -11.75379 | -44.96925 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 068ca833-b08a-3123-941f-d948113550a4 | -14.21439 | -51.21555 | 2025-08-04 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 435ddc64-eda0-3f4c-b5d1-66bb306a4f1b | -10.81474 | -44.34997 | 2025-08-04 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a502c877-0b63-3df8-a321-28dba6fb921a | -15.76704 | -46.56139 | 2025-08-04 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d2b34cf-0ba2-33fe-9a97-c5fb8014fef4 | -13.04607 | -56.89198 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6f4e152-a799-3807-832b-cdc5395193af | -10.56164 | -45.27402 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80065680-e429-3524-b535-2615b352e7d8 | -11.77514 | -44.98223 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f9409562-6968-3879-aebf-e11d990ef933 | -11.93079 | -44.9658 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e107ed-cbf3-3d76-b955-d10c764d00ad | -14.21099 | -51.21496 | 2025-08-04 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0239aee-364b-3883-96ee-ccfab0301de8 | -12.69634 | -48.08507 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b967fa65-c5cd-3749-ae5c-78f9e0f81004 | -10.19149 | -48.18984 | 2025-08-04 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9211e38c-8dbb-3eb4-b5fb-502856577947 | -12.68962 | -48.08399 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48a38a43-68ea-342b-9b0a-c34e7ca02864 | -10.45033 | -47.22014 | 2025-08-04 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a37a40c1-e879-31df-9d20-9b9d4f71ab33 | -10.36288 | -45.18594 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38aaa49b-b43a-3814-9293-9bd63dfceb24 | -12.70085 | -48.10049 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b85e5f4-f71a-30d9-9019-f528b0fc879c | -11.78377 | -44.9998 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd19d72-2a6b-3842-806b-0e080b1c5e22 | -10.2551 | -50.1611 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3cded04-93ba-3bce-8f94-d53143795586 | -14.16168 | -43.66919 | 2025-08-04 04:36:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7c37f1e-edc8-3af7-be2a-3d3e9fcf224c | -9.46601 | -57.839 | 2025-08-04 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2483d55f-720e-354e-90e4-a70ce8c5e32d | -12.69749 | -48.09998 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfca2995-44a1-364a-90d1-5c8158af295d | -12.69577 | -48.08875 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e96de953-7317-39b1-a581-eb3b4d984e2f | -12.14141 | -43.3819 | 2025-08-04 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c2b8328-61b2-372a-9487-429824095e71 | -11.2282 | -48.43756 | 2025-08-04 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6a347bc-f79b-3d01-a4f7-a43919a999df | -10.78181 | -48.80154 | 2025-08-04 04:36:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8000f4a-9d6a-337a-b1f3-3fcda94395e3 | -11.93418 | -44.94186 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5853c482-ea3d-3e2a-aaba-d785765f6e43 | -9.46063 | -57.838 | 2025-08-04 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93d8127d-6533-328e-bf37-fe80a1ea41e6 | -11.41338 | -54.71898 | 2025-08-04 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5cf1cc6-229d-301b-bffe-3af7f0e1cf40 | -10.56833 | -45.26941 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaa93c86-0c67-32ef-b9c5-b46af048c3d4 | -15.56488 | -47.08457 | 2025-08-04 04:36:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d35e1c0c-5796-33a0-a47b-4405f5cab480 | -12.44087 | -44.849 | 2025-08-04 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9136368b-0c4c-3eed-a9f1-92311acef2b2 | -10.24373 | -50.16674 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8222353-4415-3758-a6e2-b5b6845bf2b5 | -15.2719 | -43.0756 | 2025-08-04 04:36:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b8a2d149-514f-3bbc-bb0e-4801e3b62a90 | -11.23153 | -48.43808 | 2025-08-04 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README19.md)
