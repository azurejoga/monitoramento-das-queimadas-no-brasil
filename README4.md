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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9fb1c5e-4e65-325a-9cc0-5e10a79f2397 | -7.3307 | -47.262299 | 2026-09-15 00:02:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1618d639-3ee4-3c0d-8471-0aef5e307c55 | -10.7489 | -44.7971 | 2026-09-15 00:02:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cde3e5fe-14ed-3ac3-9d02-631d36bdc32f | -15.5254 | -53.780102 | 2026-09-15 00:02:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d60b53a-0a4a-3f9b-abb0-20adef03d157 | -3.95 | -43.098598 | 2026-09-15 00:02:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8de0240-1fd1-3a76-9630-9e246117f7c9 | -10.6628 | -54.108101 | 2026-09-15 00:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a658a793-bd66-36d4-9935-3dcb702d4412 | -2.661 | -57.494499 | 2026-09-15 00:02:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0979daaa-d452-3c06-95b5-9efe2d036baf | -10.6966 | -47.486301 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14ddedd8-eb99-3e5b-9729-b87239912bd0 | -16.974001 | -49.699001 | 2026-09-15 00:02:00 | METOP-B | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 555352a6-3148-3f35-9607-56cba3669e1d | -9.8867 | -47.7785 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a793f9d9-173d-3f84-8d0f-a4fce6f4a931 | -13.3047 | -51.2733 | 2026-09-15 00:02:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5bc98a-c1f6-3bdc-b97e-ca3618e8422c | -2.689 | -57.529301 | 2026-09-15 00:02:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18f1fd3b-7653-30be-90f9-91067409951b | -8.3772 | -54.700199 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e332e42-b691-3c84-b7e0-2530d5c2313a | -5.964 | -49.250301 | 2026-09-15 00:02:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6f25d2d-e3fe-3198-9461-7e0665e8dd5f | -12.8486 | -44.371101 | 2026-09-15 00:02:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03d1ac51-7a5a-3fff-87f2-6503d757cb20 | -11.9204 | -48.238499 | 2026-09-15 00:02:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0984b426-e168-3948-bd71-dff4839c81a4 | -7.1254 | -42.109299 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85f83a01-6b5e-3238-8d7c-93d3aec523b5 | -5.1873 | -48.174301 | 2026-09-15 00:02:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e5b4b7c-4f3e-3289-ab14-5c4224450e74 | -5.7812 | -49.862499 | 2026-09-15 00:02:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37cdbf02-1547-3a80-8ff1-20c470b5824b | -5.4018 | -48.486801 | 2026-09-15 00:02:00 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4feacabe-c8a2-3570-844a-6cf36ae56479 | -12.4866 | -41.398499 | 2026-09-15 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9b363249-5095-30aa-b3ae-4cb41e673fda | -15.5825 | -48.779301 | 2026-09-15 00:02:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8364aae7-7a78-375a-941b-c3ff86d1a231 | -4.5783 | -44.605301 | 2026-09-15 00:02:00 | METOP-B | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94aa1726-0f78-33d7-9bce-17b63c4ebed8 | -16.335501 | -43.4217 | 2026-09-15 00:02:00 | METOP-B | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f825e23-cac6-3c37-8a57-01148dae1508 | -9.6184 | -46.715698 | 2026-09-15 00:02:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36dfcbba-8741-3dec-a5d3-ad456fe49ba6 | -2.9073 | -50.401501 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f7c02b8-ae19-3282-b9fd-0aefc37e61ec | -15.5433 | -48.7878 | 2026-09-15 00:02:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c34e6f7-b888-3f7e-ae9e-03d5e2771844 | -2.9024 | -50.379501 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059f7771-3bfc-3474-839d-f108b9b2f522 | -14.6698 | -42.834 | 2026-09-15 00:02:00 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1b97ad7c-b024-3511-9e80-db40084cefe3 | -7.0724 | -41.757999 | 2026-09-15 00:02:00 | METOP-B | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ced4085-e097-3fba-9a26-dc14e5399301 | -8.0837 | -43.763302 | 2026-09-15 00:02:00 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ca8d9bc-98f0-3a7b-af8e-d550f16a072b | -9.3122 | -44.340599 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3d531e-888e-3b27-9f42-a8037cd8941a | -17.302099 | -42.512798 | 2026-09-15 00:02:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| afba12b1-6533-309c-b45a-e31a45a8a9f0 | -6.5721 | -51.073601 | 2026-09-15 00:02:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c889947-0efe-3a3b-b47c-3d237ab23ca2 | -6.3358 | -45.5201 | 2026-09-15 00:02:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c109f43-df80-314a-87ed-0e62de43c519 | -9.2837 | -49.763199 | 2026-09-15 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3fe494d-1d83-35af-acf3-fa54fd36e4b2 | -2.6836 | -57.550999 | 2026-09-15 00:02:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd87dc9-9d6f-3aae-b1cc-3f75820cd7ba | -8.5084 | -50.116199 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed2f50f7-f04a-3256-af94-4e97954bf50a | -5.9329 | -53.5079 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3892aaf6-e930-3a94-b518-46168b7c4136 | -11.8814 | -43.805698 | 2026-09-15 00:02:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8bde716-11b3-31de-bae6-020eab0ab0db | -10.5767 | -47.734901 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa89ea4d-e046-388d-b07a-65b4e7d6cad0 | -12.3615 | -46.918499 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60a1ccc0-487b-33c0-bc25-60c3758a83ec | -4.664 | -42.063599 | 2026-09-15 00:02:00 | METOP-B | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7dba5e89-5e0d-3f90-9428-949cce00eb61 | -10.5849 | -47.7257 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0ed6451-b878-3cee-be27-8553312280c9 | -4.9131 | -44.805099 | 2026-09-15 00:02:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e79c4289-5eac-33db-ae58-6aecfda7bbf2 | -4.1837 | -49.390701 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 707f4b28-17ed-3b9f-83c4-463805ea5d01 | -10.7523 | -44.812 | 2026-09-15 00:02:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9b727b9-287b-3b37-aed8-ad0560d5d364 | -7.3796 | -49.5116 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ec1562-1597-3ab7-84da-3f04a6b11d09 | -5.4655 | -45.0993 | 2026-09-15 00:02:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62384801-3fe1-3489-9b34-d466be029c2e | -14.8463 | -49.226398 | 2026-09-15 00:02:00 | METOP-B | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d74757dc-295c-3aea-bb05-aef511ac3785 | -6.1516 | -52.768299 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cde7b2d5-f759-3c0e-a5cc-e86240b74ac9 | -5.8554 | -51.924999 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d925a26-8241-3f2a-9088-94b644e712c6 | -2.8263 | -49.217098 | 2026-09-15 00:02:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746bed32-c659-3ae4-89ee-e1bf7b41550f | -6.4198 | -43.0462 | 2026-09-15 00:02:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1569bd18-e981-3751-8012-91edd0469c69 | -5.3519 | -50.152599 | 2026-09-15 00:02:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3a4ff6-c003-3c19-b328-b193aab0c262 | -14.158 | -47.375999 | 2026-09-15 00:02:00 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dc975ec4-2916-3b2c-a5e9-26d8452f6e15 | -11.241 | -43.4519 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4abf3ce0-cc98-3493-992d-85e4a81a56c9 | -3.7721 | -51.325401 | 2026-09-15 00:02:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 026ec773-0da7-3f1d-b2eb-5775db5632cd | -3.9598 | -43.096298 | 2026-09-15 00:02:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfdf9c59-4a20-3682-b3c8-8928206ec5fd | -11.8083 | -46.5597 | 2026-09-15 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac95c89a-dc07-30eb-8813-66753bd2f2e8 | -3.4117 | -58.1376 | 2026-09-15 00:02:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 985ff9c2-eb3c-3bea-8615-f6d2c62c86bc | -10.7917 | -46.2066 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 668b6ea4-7e52-37b3-a5c4-fadb51ec0f70 | -10.7851 | -46.222801 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da7c9e9e-f8b2-35ca-a763-73b3bba5fe49 | -12.0305 | -47.799599 | 2026-09-15 00:02:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bfb80e4-ea18-3b3a-b511-817a9e27e62f | -7.4658 | -46.131802 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec0b0839-351c-3b0f-8c4f-a1f0a793206f | -4.3007 | -49.086498 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68260fa1-3f58-323b-82e0-8c02cb9bc737 | -13.6025 | -47.895901 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 850dd249-5d24-3b67-a1dc-35c4c9ffac83 | -14.8529 | -48.131001 | 2026-09-15 00:02:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e59fc17e-85d9-3312-9989-3fdbdbf6c841 | -2.6653 | -57.514 | 2026-09-15 00:02:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 955d2961-0e8d-3b4e-a7c5-63982fc0b446 | -13.6009 | -47.888401 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cea98956-8235-374b-afb1-544f72a6038a | -3.2236 | -50.572601 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afa55082-e0b6-3627-9e99-b27cb94e45b9 | -4.2621 | -46.504002 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d67a8348-5b6b-3db2-80b1-555a1521de3b | -11.2215 | -43.412399 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4978f8a7-2b3d-34e0-a8cc-b7c0f09c0929 | -7.1555 | -43.500401 | 2026-09-15 00:02:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ba46d53-02ed-3d98-8bfe-65fe377c776f | -1.2003 | -47.587399 | 2026-09-15 00:02:00 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfdb14d3-8c18-3401-a322-a4f0a7744133 | -8.8114 | -45.883801 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2f2020b-ce7a-3683-be07-a8bbe23826d0 | -11.4747 | -47.422199 | 2026-09-15 00:02:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8afd975b-d42a-3cf1-8693-7380dd50c824 | -7.0809 | -41.793301 | 2026-09-15 00:02:00 | METOP-B | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06515204-2126-33be-bf05-3eb26c09e871 | -14.6845 | -48.013699 | 2026-09-15 00:02:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 14cf145c-39ad-3077-a78c-0f200df898ea | -3.8477 | -49.041401 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c65cad-8cfe-3dcf-90fa-26789a221785 | -15.2535 | -42.767601 | 2026-09-15 00:02:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7eec7c0-f0ef-3dd6-9c8f-094090237797 | -5.513 | -43.352901 | 2026-09-15 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4cfa874-8f36-3509-a93f-a4dd460f4e6c | -12.9706 | -41.051201 | 2026-09-15 00:02:00 | METOP-B | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d867a6a0-be0b-3e70-ab55-c4037b4c4dce | -3.235 | -50.5779 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25cd081f-8ae9-3f86-bcfd-8b1e02c3b7ab | -15.5286 | -53.797199 | 2026-09-15 00:02:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aaa64c5f-dbe6-3116-8ece-88059d29be7f | -5.3126 | -49.237499 | 2026-09-15 00:02:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6c86c9-0f2d-3840-a859-5259d401da24 | -5.7209 | -46.1661 | 2026-09-15 00:02:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d14d6d32-be2b-30c8-a17e-c5f526d038a6 | -13.5682 | -47.8801 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd9ab7d4-6d52-32d2-b139-efbba5b83c82 | -15.8224 | -49.2005 | 2026-09-15 00:02:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b233aa1e-c9cc-3167-809c-83d8b4a47056 | -14.1733 | -47.0676 | 2026-09-15 00:02:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c26cbe32-5837-3260-afe8-cff5f11900e4 | -2.9204 | -50.414001 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979490c6-3155-328c-80d7-04510d7f039a | -9.8784 | -47.787701 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa705668-fcde-3abb-881b-34edd34c06be | -4.3619 | -46.625301 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 100b2698-7f0a-35ca-921d-e947139743ca | -8.5004 | -50.1264 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f53a12f-2738-34bb-a710-d41f7bc2b210 | -4.6669 | -42.075802 | 2026-09-15 00:02:00 | METOP-B | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9915db3-b1f1-3901-82e8-5d76f2ce66e8 | -9.0202 | -47.723202 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05e10c20-3937-3cc3-a145-efb4379e09f7 | -7.0098 | -44.598999 | 2026-09-15 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16cf7b3e-5f8e-30e5-9760-d377b1d6600b | -2.6793 | -57.531399 | 2026-09-15 00:02:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15b3ad24-6409-340c-96fc-2da3afb8c629 | -10.4435 | -48.627399 | 2026-09-15 00:02:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4801cae9-ea84-3425-ac2c-ebc3e5e36bc0 | -11.3322 | -47.662498 | 2026-09-15 00:02:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 391be1a8-18a1-385f-bde2-b394f9a2975e | -7.554 | -44.900398 | 2026-09-15 00:02:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
