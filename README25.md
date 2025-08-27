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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9206450f-ccc4-3da1-84b3-3009a6fc3ce1 | -7.88375 | -45.87414 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7597ba09-5df8-3885-ad43-da0d53f700ce | -10.78517 | -46.38059 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7613ba27-2a92-34f2-9a91-e5a2be11983a | -13.66702 | -46.90292 | 2025-08-27 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bdacbe1-2ac8-3206-b6cf-5c8e7640c57c | -9.10671 | -49.58246 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9686fc23-8fdd-3be3-9dab-1910e6c44661 | -13.39834 | -46.88471 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a98b167-1aa8-3166-91a5-06d420301715 | -13.23012 | -46.54605 | 2025-08-27 04:04:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75fcbbd8-e417-3d9b-bef4-ba1c6e72902e | -7.76228 | -43.63316 | 2025-08-27 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f9f46da-be38-37f8-ba6d-072af7d6b639 | -9.13216 | -45.23663 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d90bffa3-0d62-3d08-870a-49a4b93c3f76 | -12.76552 | -48.17374 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fadfb6d0-0fcc-3f9e-a724-aa2efb49c826 | -7.12551 | -43.69124 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8fbb8d73-c361-3a36-9b95-9e6759fe4f1e | -9.10202 | -49.57819 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 58758c69-a4be-3c2b-a3ed-203e49f5fb28 | -7.64408 | -42.67668 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1d05d7b7-c9c7-377c-970b-a8784a76cbe3 | -7.64472 | -42.67276 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 25d338db-49fb-316f-95bc-02da51a78016 | -11.64525 | -44.86643 | 2025-08-27 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6367ec6-9f02-3a58-a7f8-8e3f48b13c26 | -8.87294 | -47.18905 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0c345df-bafe-36db-9461-83be68e08058 | -11.03251 | -52.02691 | 2025-08-27 04:04:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76249b6d-bd38-37cd-ae0b-e49d7280557d | -8.26104 | -45.12371 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6984deda-4d59-358c-98d6-1672ec59f968 | -7.65305 | -42.66607 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1184e625-0473-3f8c-8de2-336c8edaf8f7 | -13.42445 | -47.00072 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06647286-ee3b-39cc-b047-b91f2eaf74fe | -11.7985 | -51.41553 | 2025-08-27 04:04:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| def41862-cbeb-35c6-bc1c-3c38d13fa66d | -6.7349 | -44.297 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3311ba7e-e4f9-3ffe-8674-f19fe37720bc | -11.10385 | -44.75354 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efc381bc-67e9-32b1-b9af-7e2b257f4ca4 | -12.7627 | -48.18911 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1899b68a-7fcf-3070-ae75-f505816b92bb | -9.09026 | -49.56234 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dce190b-d540-35c8-9445-238ceedef438 | -12.89784 | -44.6358 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abff9da2-5f67-3730-9451-8dabef13c47f | -11.92301 | -47.10858 | 2025-08-27 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 540a9ce0-3a88-39e5-b921-78b36af828b8 | -12.4043 | -46.50425 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3f44de3-5424-3e77-b08d-00e1cc885b9a | -8.26504 | -45.12434 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf65763e-18ec-393a-a1ff-52e90db5177f | -13.45376 | -46.98927 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0f758a5-2de1-33f5-8856-d0e3c112502a | -6.71557 | -43.1023 | 2025-08-27 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ca59d19-f71a-3eb3-bf1a-66d1109aab43 | -11.25164 | -44.97434 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18a40b81-6ea0-3c8a-aebe-d5975d99765f | -8.87826 | -47.18529 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 400789c4-1420-3dab-bca1-d1a0b35ca6b2 | -6.6262 | -53.33001 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae76fa1d-62a2-3be8-b5c9-9a98a624b5f0 | -7.10183 | -44.61817 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68e0d328-1689-34c9-aaac-ef657b9bff60 | -7.70232 | -45.77182 | 2025-08-27 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e50ab353-5227-3fb3-a3bc-668ca844ffda | -11.15573 | -44.78822 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76c3b017-e889-3417-80c9-00b0746d7830 | -7.66137 | -42.6594 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7016601b-901a-329b-99ac-d6b54fbe364a | -9.0985 | -49.57747 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8ee2efb5-29c2-37da-9560-51d862db79f7 | -9.08181 | -49.60915 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 200fa8a8-6dea-3d29-81f5-e9e7954ce166 | -12.68328 | -47.88242 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0ebed45-0e91-3370-b052-f4f00ca0041b | -8.6926 | -47.20227 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1c8ac52-28e7-35ce-81d2-a4fa052cd30e | -8.29656 | -46.33168 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c42cae90-f498-37f3-b1b7-8d33eef82a9b | -9.19602 | -46.72445 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10a1bf01-2c24-332c-82e2-1b2ac04b9dbe | -7.16916 | -43.84624 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a11588e9-b920-31f8-ad83-fedf3f50e2af | -13.42875 | -47.00064 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 629e2ae6-12d5-391b-bf8a-f8cb40948d3e | -6.9008 | -43.13376 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1de30a0f-2266-33cb-bafc-ea24ac84bb76 | -11.91451 | -46.74914 | 2025-08-27 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f01f075-51bc-3f37-8bbf-6bcbdb9affed | -6.79828 | -44.3511 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43196a36-e5f3-3ef4-b4b1-d2ccdb1e0a75 | -9.07241 | -49.60033 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 735472f5-b098-3a08-84cc-7fc11bae441c | -6.57633 | -47.37965 | 2025-08-27 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 33b69d4e-b438-34ba-b51e-c48cebced0c0 | -6.43509 | -44.60276 | 2025-08-27 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cca56ff-0d00-30cf-af0a-98d25e48b04d | -12.70767 | -48.18201 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14f31a34-b5ed-38e8-8568-1e99489d2164 | -6.46104 | -44.56982 | 2025-08-27 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0818dca9-1fd2-39f5-b541-1f066fda31d6 | -7.21211 | -44.44012 | 2025-08-27 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30692445-ea86-3d2a-9b63-0360244b8309 | -12.57001 | -43.78772 | 2025-08-27 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5afea08f-03be-3c1f-ab81-75e5f5a2bf1c | -9.07845 | -49.56701 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dd8acae-ed93-323c-aabf-e1415f0cf644 | -12.76907 | -48.17996 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed815682-c178-3b01-b02e-3d7c55c9fa08 | -12.89677 | -44.64568 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f07c4cb2-b389-378d-aa1a-5e7f80927fea | -12.78489 | -48.14466 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c283ad3-48bd-351c-b606-15a2a2971862 | -6.91417 | -52.85615 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66440ef5-543a-3e2b-9b98-883e939dc640 | -12.56873 | -44.81204 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 733fefe9-2016-340b-a3cf-bf3e2e71f34c | -8.90078 | -45.71284 | 2025-08-27 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbfa8060-ff03-3c3d-951b-f1eb1fba845a | -12.93007 | -46.31528 | 2025-08-27 04:04:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8ddb516-5630-304f-8bd4-b32b8ffdf5e7 | -11.24375 | -45.48164 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9baa0eb9-d85c-3496-a187-ce5e4dbd6619 | -7.28786 | -47.00072 | 2025-08-27 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9608864b-6cb0-359e-98d5-b1247eb67dae | -13.53866 | -46.89764 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1517a2d4-6595-35d0-842d-82e46183cee5 | -12.3869 | -45.0106 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1cb0225-8cc8-3994-9908-4ca59b835152 | -9.19809 | -46.73819 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47ab7818-a203-3b2d-a9bd-7582c8aafe2d | -13.43243 | -46.86068 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7805f71-3c9a-30f5-95a0-6fd1bf407e7b | -11.24462 | -44.99241 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1abf9fa8-b30b-3529-86ff-5b78c53ee194 | -9.10609 | -49.58579 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d5e4a6f-69a7-3e32-9dee-3ceb0365aa7a | -6.9001 | -43.13797 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0dfd9b0d-c0c2-3c82-9af0-2afd6aa70f82 | -7.73836 | -47.46649 | 2025-08-27 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67972f27-da6a-3f46-8c71-9cc846bd316b | -9.07976 | -49.60887 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00e1e973-d339-391b-8e14-78b0950aac8e | -12.78933 | -48.1203 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf591c09-55a0-3a50-8c12-29d5838b6c06 | -7.73607 | -50.29719 | 2025-08-27 04:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8baebdc7-fe5b-3a3e-a753-e609e6281eda | -8.45544 | -43.6899 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e77ad420-0e0c-395d-a518-2ebbe41e16b0 | -10.68601 | -47.13892 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c148f9f4-d868-308e-b2b6-1333954ebea8 | -7.14882 | -44.14948 | 2025-08-27 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f112999-2bfa-34ae-bde7-5dd16cd64beb | -7.17146 | -43.85575 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50111a13-b1c5-3014-a33a-0d770065c0eb | -7.88443 | -45.87015 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2851df7d-3ce7-3a0a-bbc5-ae9f931d0d48 | -12.74461 | -48.18539 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 314efe5b-8c80-30c4-8ae2-cb267e08ed3d | -8.08776 | -45.01593 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23a6d551-7c18-3b8e-bd4f-1c7650a85d8a | -7.65785 | -42.65882 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8c166f27-bc08-3bdb-a264-beacd6ec041c | -7.08523 | -43.64987 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1906ca02-f6c4-3bcb-8108-41220ec27fca | -11.32629 | -43.29618 | 2025-08-27 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87e1d0f2-3970-37ea-8930-e8914dc39ef2 | -12.42731 | -45.96995 | 2025-08-27 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbdda8a1-551f-359b-8cce-c7006ef9a49a | -11.25219 | -44.99386 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a218a15-4cc9-3dfe-b8c2-9485e8a0d198 | -12.77249 | -48.16128 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 12f524bf-42f5-3b62-a0cc-9024dccec065 | -10.48985 | -51.60143 | 2025-08-27 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05c087a4-04ab-39c0-aaea-81f488a99607 | -11.64305 | -44.85663 | 2025-08-27 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb9da209-e079-3cdc-9b91-09b846cf6363 | -12.56059 | -44.81514 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7430cc01-1bd2-394e-a037-0c02bd4cc318 | -6.57163 | -47.38293 | 2025-08-27 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a98b8b1f-3d44-35d3-a9e6-ab4356340470 | -8.13635 | -49.58979 | 2025-08-27 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b79aa1ab-a6ee-3c55-9bfd-f801b3a3aa84 | -8.25069 | -41.69598 | 2025-08-27 04:04:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 34eb6d3e-fef2-397a-923c-b83ae3b6cb44 | -13.06401 | -46.33285 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 136eccba-8bf6-3cb6-82b7-b91db39908f9 | -9.09325 | -49.56642 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62cfd8b3-da3d-3bf9-b1d2-6c32cf4d0a81 | -9.31621 | -40.20882 | 2025-08-27 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a25027b-35c1-3c20-b51e-2ff3db6608ce | -11.58368 | -46.38933 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6d74a89-712b-3598-a259-af8d3723cfe5 | -7.73677 | -50.29337 | 2025-08-27 04:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README26.md)
