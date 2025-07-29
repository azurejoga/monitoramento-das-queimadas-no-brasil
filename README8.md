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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99b954e9-6038-3992-9427-daa48d1a97a2 | -11.99436 | -46.96842 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 845fda24-8a2d-33ed-ba1f-c2ef0a81428e | -11.26975 | -44.65557 | 2025-07-29 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f088e6bb-2df6-316e-89a5-34f8f557ecb0 | -9.39434 | -45.49288 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cb7bf65-e6ff-3ff6-806b-9bb733769793 | -7.93715 | -44.08769 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2867fde-d600-330e-8359-b21215987555 | -11.43511 | -45.12794 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da8f3667-b1e9-32bc-b662-e58806d117d6 | -19.49481 | -40.62795 | 2025-07-29 03:32:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 482d56b1-6567-3d43-ba4c-0c7d2dd49fad | -12.99899 | -44.8978 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b15842a9-c3a7-33f7-9280-6d119a5f53d5 | -13.48903 | -45.60114 | 2025-07-29 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c661d3fc-2b2c-364a-98f7-541f17680a7e | -13.131 | -47.34739 | 2025-07-29 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3361828-79ca-3a01-a796-a172952c8392 | -17.0466 | -43.77557 | 2025-07-29 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d42d7a16-48f1-356c-a6d6-bfc6fe8f8b89 | -12.99308 | -44.89627 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da0df8a1-098f-3725-9d3e-f8cfee5c24df | -14.50962 | -46.54585 | 2025-07-29 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66cde5dc-dc76-32c1-a5f3-caa3ab8dbb2f | -14.49794 | -46.53785 | 2025-07-29 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4861cefb-0688-31ac-a38c-c865e344dc1f | -12.94311 | -44.73294 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f55a106-db6a-3e64-b429-f4eab5252cbd | -15.12648 | -45.32769 | 2025-07-29 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 799c40e7-84ea-3c1a-a607-36dcef5b19b9 | -12.99991 | -44.89325 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5f87faa-dd3a-3f11-95b2-9ab2d71da4f5 | -13.13232 | -47.34129 | 2025-07-29 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f119c1f-8ad1-3efe-ba64-4227801d0155 | -14.34795 | -47.10265 | 2025-07-29 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ded8618d-01c0-3a0c-97de-5b551b08a3a7 | -13.48392 | -45.5948 | 2025-07-29 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a86dd301-f2d5-3f6e-9284-0e083a47d9bb | -15.81784 | -41.88992 | 2025-07-29 03:32:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6a0f841-b772-366c-85f6-7e71093bf52b | -14.49676 | -46.54334 | 2025-07-29 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8d72828-4c55-39c4-9fe1-b0d4a0de1bdd | -14.12744 | -45.28342 | 2025-07-29 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa7c5ebd-6d8e-3746-a929-35b13a2ba756 | -14.35136 | -47.10118 | 2025-07-29 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11d5cd10-12f8-3db0-946f-03f5f992ff57 | -12.99217 | -44.9007 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 774c9e5c-2b4e-3ed6-b676-d941d79a9d27 | -12.98717 | -44.89478 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94995ac0-5e4e-3aed-9daa-db6c2727d6e1 | -12.99807 | -44.90229 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 315c3490-8b76-3f07-ab90-ce87f3b42dd3 | -13.51654 | -45.62363 | 2025-07-29 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 546eb40d-bfac-393b-a9ab-63fa55f683d0 | -13.48472 | -45.59856 | 2025-07-29 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4a183dd-2bce-3dcc-ba4b-65edfaf380e0 | -14.5032 | -46.54452 | 2025-07-29 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc574562-6143-319d-8417-b7317f6db046 | -14.00459 | -44.62299 | 2025-07-29 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5711abba-a603-3e2d-bd69-9baa8eae1644 | -15.12554 | -45.3321 | 2025-07-29 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef696652-7ee0-3323-a93b-b9cc3ce22d68 | -13.00265 | -44.87988 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12446ce7-14bc-3769-b8d5-447eff9f2f18 | -14.12555 | -45.29254 | 2025-07-29 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ee0703-7976-3172-93d9-e4ecedb10d9b | -13.00854 | -44.88145 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ef28a57-6068-3243-bf79-0252075c102d | -15.12767 | -45.33349 | 2025-07-29 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c94ba47d-5eb1-3111-b580-10f1e6d006ff | -13.48571 | -45.59367 | 2025-07-29 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35f0cd0e-a168-3b6d-8720-ca1fdacad355 | -13.52268 | -45.62508 | 2025-07-29 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f418dc65-62c1-3d3b-8b3d-b3a14d27487e | -13.48289 | -45.59969 | 2025-07-29 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ac41238-2f5d-3643-a9f7-5b223add420e | -14.34476 | -47.09962 | 2025-07-29 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d52da3e-45f2-34b6-b26b-1ca719b9303d | -16.55183 | -40.50585 | 2025-07-29 03:32:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 62a38d53-572a-3db8-bd17-35390996c356 | -14.34922 | -47.09689 | 2025-07-29 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e42a6af-73d9-3774-9e19-192ce896e3d9 | -15.1218 | -45.33214 | 2025-07-29 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38cc619b-fddf-371a-9630-4400a38471a2 | -13.00673 | -44.8903 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 441151a5-1f56-34d8-8e1c-d4147a6f3c9e | -17.04079 | -43.77763 | 2025-07-29 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 463198ef-c931-37f6-aedb-d5d401f60969 | -13.00581 | -44.8948 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc5e0056-c9ce-37f2-96ba-cd88c37297e3 | -14.13246 | -45.28935 | 2025-07-29 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70e08c91-0175-3873-b8e7-60e7c5178e15 | -15.12089 | -45.33654 | 2025-07-29 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c791edd-33d9-3062-9ad8-770c1509dea3 | -14.74101 | -46.30664 | 2025-07-29 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f5ff32f-2e3c-356a-bacb-c1110cfd2827 | -14.50438 | -46.53907 | 2025-07-29 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ae5d7f2-d3b3-3624-8145-3182e3e83d99 | -17.04596 | -43.77869 | 2025-07-29 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f1d85bc-e8b7-3990-8a8b-66903a2ae34f | -15.12271 | -45.32773 | 2025-07-29 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e71f3f0b-13cd-3700-a35c-bbcdce56228b | -14.12649 | -45.28797 | 2025-07-29 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 653c4614-8216-35e8-8e57-3f03847bee91 | -13.00764 | -44.88585 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25c751e8-0fae-3fc0-951d-be6c6611cf90 | -14.74209 | -46.30145 | 2025-07-29 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fdc32f2-1c9d-3068-b28d-028a082f26f0 | -15.12859 | -45.32907 | 2025-07-29 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 502ba7ef-3097-306e-87ec-37769745c4a2 | -12.9481 | -44.73869 | 2025-07-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14f3fc81-97c9-3511-9da7-c7f7ab553592 | -14.50597 | -42.23537 | 2025-07-29 03:32:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab598200-37b7-3df5-bb84-9ac6b59d55ca | -23.01557 | -43.50434 | 2025-07-29 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d314a1f-3ba8-3095-aae8-be305bdce378 | -23.00104 | -43.50596 | 2025-07-29 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eabff676-2e02-320c-b07c-b9ef4cfaf507 | -23.01006 | -43.50814 | 2025-07-29 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 914d1d37-4780-338b-a40d-9f812ca0bf1f | -23.01107 | -43.50323 | 2025-07-29 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d22d7f06-cd8b-39c4-aa17-388e3f94c1e6 | -11.4393 | -45.1154 | 2025-07-29 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9e0bcb8a-9ac7-3f00-9b7a-14aafc5dcc70 | -14.3796 | -59.3333 | 2025-07-29 03:40:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| bb8fe804-51ab-371d-9f67-001cf2487926 | -8.9475 | -46.7577 | 2025-07-29 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2a10b56e-7649-3235-ae82-8b51f388f638 | -11.4197 | -45.1412 | 2025-07-29 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| efece879-9089-32af-96f9-130b257857d8 | -11.7508 | -48.1825 | 2025-07-29 03:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 731e2c11-4d29-3404-bbe9-0102a18d7f6a | -11.4201 | -45.1181 | 2025-07-29 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 724bc069-4539-3ed4-b908-17f6a3409d2c | -11.4393 | -45.1154 | 2025-07-29 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e2aa2d2e-b41b-3abe-97ba-4d786c792c7e | -11.7508 | -48.1825 | 2025-07-29 03:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1c65abb9-09d0-346f-a745-0eb1b4a9505a | -11.4389 | -45.1385 | 2025-07-29 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 7b7da801-cae3-377f-b652-19527afdaa3a | -11.4201 | -45.1181 | 2025-07-29 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 49baf690-2f1d-3701-869d-9a24031204ea | -12.0001 | -46.9696 | 2025-07-29 03:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 0cecac62-f75a-3cbe-b77a-776fedde3bc0 | -11.4197 | -45.1412 | 2025-07-29 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f3008f32-1216-349d-9fab-5065410287d5 | -11.4389 | -45.1385 | 2025-07-29 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f56b8647-36ba-3d97-9731-fd3ccd0dfd89 | -11.4393 | -45.1154 | 2025-07-29 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 22ad281f-c0f0-3fa2-9f37-d8a97a9eadd3 | -11.4201 | -45.1181 | 2025-07-29 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b52f012b-ef90-3351-8441-5393c17d9e95 | -11.7508 | -48.1825 | 2025-07-29 04:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 99b3a7d2-879e-3ebe-8482-748bca6c1e90 | -11.4201 | -45.1181 | 2025-07-29 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| a3b45bd1-1d20-36c8-8483-9b5032080fb1 | -11.4393 | -45.1154 | 2025-07-29 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fff65c2c-f590-380f-aff6-6c5800247a26 | -11.4389 | -45.1385 | 2025-07-29 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 30c4fd9b-f591-3546-8ce4-f507f02d538b | -8.63826 | -45.52235 | 2025-07-29 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 465f051a-cec4-3e64-b691-2579c4469347 | -6.40587 | -53.32183 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95332d61-3dfe-33d3-8215-eb1cd388cce0 | -7.53585 | -44.38984 | 2025-07-29 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 654fb697-6b4b-3a87-8211-8240a64b710c | -2.83365 | -52.35933 | 2025-07-29 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3059650-93b4-3499-a2a2-ec8b32d9e8e3 | -7.85512 | -46.72805 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d73a61e-45f2-3e8e-80e7-caf4b36927b0 | -3.30038 | -48.92503 | 2025-07-29 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd9631e8-4a47-3c7d-9dc3-ded2f6abd604 | -7.93195 | -44.09088 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3ad727b8-6d94-3d00-8f74-91536639b541 | -7.34415 | -43.73711 | 2025-07-29 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01405cb3-4f8e-3625-b1b1-ae57acf8a310 | -6.38803 | -53.33424 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5eb12722-a49f-3616-a96e-f5196abc86af | -3.27533 | -49.14559 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faa6b7cf-0efb-3138-a17c-1591fdb1d393 | -6.40535 | -53.32481 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdf0523-8547-3d2b-b2ac-2b63f947c91b | -3.74703 | -49.04448 | 2025-07-29 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b42c6f3-dc13-3ffd-ad67-3534c52dffe8 | -5.18936 | -44.95584 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 62ab6fdf-fef9-3ef8-9655-93cd36609eff | -7.24996 | -43.06895 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6d72f2dc-5712-34a3-aa19-3d18c58244da | -3.88434 | -54.24371 | 2025-07-29 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e36c111-c4d1-3d1f-b284-2d1fab6a0da2 | -7.61958 | -44.81348 | 2025-07-29 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31e20cf1-128c-3426-948c-810878868aed | -8.21935 | -44.91494 | 2025-07-29 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08c164a4-0964-3ff1-a52a-82e29ad38924 | -2.81264 | -49.00574 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8477a2f8-9496-380c-9c10-acfafe586f4a | -7.24768 | -43.06091 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e6a98a4a-97dc-37fc-a9ab-b4ae73b634f2 | -5.49572 | -45.38801 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
