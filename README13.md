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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1edf0e5-ece5-3e89-abdd-14e66c5f4c2b | -10.79463 | -47.2577 | 2025-08-05 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b71a6049-8789-3aa8-9521-505adfb141f0 | -11.75482 | -47.54668 | 2025-08-05 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beeef27d-154f-3e01-9693-1b6633b7bef0 | -7.56823 | -44.90695 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd57fa87-62a3-3763-9ed3-81b8b406b996 | -9.74448 | -48.57325 | 2025-08-05 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee9012f-0d1c-3e85-a166-dabbfcb1bbc6 | -12.51222 | -47.18447 | 2025-08-05 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c461387-f622-342c-928c-efb2ffe6d324 | -6.49954 | -45.54411 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b25bb7fa-9fab-30b3-8da0-5da1ffb77c98 | -12.54791 | -44.7276 | 2025-08-05 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b266a916-73bb-3986-84f1-06d0d5021a7e | -8.24911 | -45.0611 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ea46437-c35b-3eea-a07c-9d5d6fa5d4ab | -7.98588 | -43.16777 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| f12f35c7-2182-30de-bbee-9c15e748fd22 | -7.11646 | -43.44674 | 2025-08-05 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73939586-fbe3-34f4-9021-ad2289c8feb8 | -14.26243 | -51.98638 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1bfde887-e5a3-3c9b-a7cc-e5cefd1a1c4d | -10.46452 | -44.33804 | 2025-08-05 04:17:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52389c1d-93d5-3376-ba75-d8ce3120d14a | -8.00076 | -43.13805 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0b48668f-9ecc-3bea-b3ed-14abcd22f796 | -9.69679 | -51.94078 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34a5039d-23b5-30ac-9698-d94e5ec524d4 | -8.24571 | -45.06054 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4b16a4b-b033-3039-b47c-9c7f90897636 | -11.28163 | -40.97814 | 2025-08-05 04:17:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f37d41c-6d55-3bab-8e88-5cf9aab98281 | -13.29686 | -39.86546 | 2025-08-05 04:17:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c2f054cf-ea5e-3e86-becb-5436f974aa38 | -10.91085 | -48.36524 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a36a187-9476-3bc6-9ae4-4bcbb19f6698 | -8.11068 | -45.5211 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd85a872-f5c8-309b-b3e3-fba2c9b5368d | -10.45453 | -44.35804 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6abeae00-db8b-3803-97d1-f7a1ab77c5e8 | -14.27252 | -51.98336 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fe41817c-396c-3b69-b5e4-f0992c532062 | -12.72919 | -45.07809 | 2025-08-05 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33415ab1-20ba-3026-8a01-66bdd1dc7c5d | -7.53948 | -44.86898 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9581d027-7053-336c-954c-82ec5fda665d | -6.43645 | -44.81872 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b5d4ae9-154b-3944-aa14-f0cd381ef46c | -11.75065 | -44.99365 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 239e5a3a-bfa5-399a-94a6-43ba1f28162c | -6.44908 | -44.80558 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a034f60-b5a2-370c-8b19-6d01dc030fc7 | -11.76521 | -44.96675 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31d78405-f08d-34fa-a2e5-53d32bbee615 | -8.38964 | -46.55987 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93f82b1c-e634-325f-8107-7c9e0933b3a4 | -12.57288 | -43.79237 | 2025-08-05 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 072f4334-d4a1-377b-beaa-e103bb1edc6b | -8.01127 | -43.13615 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c8856a88-f36c-38a5-9974-8a0e6bfa3b44 | -15.7741 | -49.9599 | 2025-08-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 907ba9fc-13ad-36db-aa3f-62204830e253 | -6.57767 | -43.49221 | 2025-08-05 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d9e8976-3e4e-3b64-acff-97840039f3c7 | -7.09629 | -44.36154 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61332a7a-90c5-3b7d-ba11-0cf0834923f8 | -10.80188 | -47.25902 | 2025-08-05 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2a445f33-45fe-3120-b4e0-ae4677225172 | -11.91648 | -44.96934 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8b611da-9b99-344b-a32c-5044185760c8 | -12.51576 | -47.18509 | 2025-08-05 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d6f47e0-479d-37f7-91d0-849247379b9a | -11.74837 | -45.00791 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b8d5e18-1b9a-31d9-b7c5-9a5f1330e8d6 | -7.38969 | -44.65118 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 258298e8-01a4-3af3-86c6-8d86134aafab | -7.38748 | -44.64342 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a44f5af9-3a60-3a4e-b728-50c645f556a7 | -8.00022 | -43.14153 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 4c7dc613-9cc3-323f-9e7e-ebb53a873bc5 | -9.17786 | -48.84562 | 2025-08-05 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23240d33-1b32-3b7c-9869-26070ec80899 | -8.019 | -43.13024 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5322d74-56d2-3912-9128-764d15bef9f5 | -17.22207 | -44.83065 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 512a69d5-7f45-3f2b-a375-dae0421565e7 | -6.32361 | -45.62651 | 2025-08-05 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7e991ca-34ba-388b-80c7-e1e4f9d6d4ff | -8.25871 | -45.06642 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83d43dd5-a339-3820-b5b2-f8a00ee09c57 | -8.11477 | -45.51781 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aaa8f80-8128-35ea-97f5-210f95373a72 | -17.2154 | -44.82954 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4ae65981-8102-3340-9bfc-5ceea9512d53 | -5.78737 | -43.61031 | 2025-08-05 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 29aee743-ce7a-3c45-83ec-28827fd64297 | -6.90979 | -43.89264 | 2025-08-05 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc5a84ec-990a-30fd-800c-d7f7596965fa | -8.21511 | -45.05555 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01e68e06-80d3-3261-910f-24ef8d217b1c | -17.36244 | -46.08816 | 2025-08-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f183c89-6640-3929-ac48-7665f7779ffb | -8.21851 | -45.0561 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fae1f44-b615-3abe-84db-0a0a75af5ab5 | -8.23891 | -45.05943 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa37e866-5551-39dd-ba50-c6327a5d5f40 | -11.91981 | -44.96992 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e87ab529-87d3-3c91-9bfe-7f30bf6dd164 | -17.37575 | -46.09048 | 2025-08-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b0e1be4-e4bd-3cfa-9b2c-50603ac42dd1 | -9.39679 | -45.50698 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38ea4445-fc2d-3fa2-b88b-6643855c048b | -8.78995 | -47.18602 | 2025-08-05 04:17:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92dd7c15-701f-3684-a41c-a00931fb2416 | -6.42561 | -44.82069 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22bbdf59-e9a8-31a5-9d02-97be366cda34 | -5.64987 | -42.59626 | 2025-08-05 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eac566ff-0825-3441-8554-066482721623 | -8.0074 | -43.13911 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f3340989-122a-3a0a-b2e5-1d8dc83528df | -8.23211 | -45.05832 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6375b2ae-6727-3597-8f5f-6a64d16433dc | -6.90867 | -43.89966 | 2025-08-05 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b56b34-1f98-3903-ab91-8c4c2681ff03 | -14.2716 | -51.9882 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5b4dcb65-bf7e-371f-a957-57dc9175ea24 | -6.95954 | -44.4981 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdc56aec-4778-322d-93dd-c26ac6b40f7c | -8.94993 | -46.73857 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 08ff9b9d-74dc-3004-a4d1-ecd8c17e3781 | -7.75693 | -45.22916 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6e92b87-6ecf-3cfc-8d74-e1daa97965c6 | -17.36185 | -46.09181 | 2025-08-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8dcd526e-5d31-3956-89dc-1304f6206755 | -7.39365 | -44.64814 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c25df780-057b-3e44-a7d3-0bc3f6f21812 | -7.20505 | -44.49606 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7357a5a2-ff9e-3b90-9026-beda25923957 | -6.96073 | -43.31479 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3aad16fd-3df1-3177-9635-fe0cbe052fca | -8.38109 | -46.53898 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99dd6500-d52a-3109-97e6-c5ea0a338276 | -11.91933 | -44.95157 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d36d9917-cd6c-337e-9c90-d970b5dc8b97 | -6.46494 | -43.02663 | 2025-08-05 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6106279a-1593-31ce-9970-36bf66bad971 | -18.77551 | -47.61925 | 2025-08-05 04:17:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cc1e53b-b6cf-3d90-a5bf-3463f3c6399a | -10.46738 | -44.3779 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ab19bef-f131-30c9-b686-9e6d044d96b6 | -11.92266 | -44.95213 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7170ceb4-e5b0-30ee-9728-404fd257a23d | -6.7372 | -45.30807 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cd7aaa7-9d03-34ab-90f4-a2b8d0e80607 | -12.34795 | -46.05686 | 2025-08-05 04:17:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23827ddf-0933-3f0a-aeaa-be87bbd8f61c | -11.0677 | -48.36106 | 2025-08-05 04:17:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69109100-9340-3936-9589-1d8a89a83dc6 | -6.91622 | -44.20897 | 2025-08-05 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20ed5fad-48cd-3246-a69c-e8608758738b | -10.9594 | -48.15301 | 2025-08-05 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f9104a7-84be-3cd7-8de0-fc371163760b | -7.81974 | -46.88537 | 2025-08-05 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aacff73-68e2-35c1-890a-2ac3f6a153da | -17.21873 | -44.8301 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f38ab684-0e0e-38e9-996a-c764ac9cb998 | -7.76298 | -45.85413 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9aa38ae4-bfad-3c74-9480-421918deec2b | -7.60403 | -45.30853 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fed7be60-6610-3911-af4e-c6be2b7c9b1d | -10.47572 | -44.36842 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa575ccf-28ed-3912-8b62-222e15c50663 | -17.68549 | -46.64007 | 2025-08-05 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff10c63e-5441-3335-8bce-1e2683b5ed02 | -11.06852 | -48.35629 | 2025-08-05 04:17:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99f78c6a-ab97-37c3-a027-eba980540e97 | -12.22312 | -44.19356 | 2025-08-05 04:17:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2204f1a-dd8f-3f40-9f21-ea3fa55146c4 | -6.67643 | -49.79501 | 2025-08-05 04:17:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab65e9c5-d5a3-3730-919b-65acc024b557 | -11.74754 | -47.54541 | 2025-08-05 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1fef9ec-ce8d-3268-ab82-bcbac982e867 | -9.07472 | -45.05839 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7493ffce-93e1-372e-8d80-470788d71f58 | -7.75814 | -45.22175 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8db7fcd-907b-373f-a5a1-a05c9702cd4c | -6.97013 | -42.87201 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d1f55d26-0c97-3b41-9a87-b45a78fb3602 | -7.83367 | -45.22975 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29394151-64c6-3f0e-99aa-cbb802dd1047 | -8.2463 | -45.05687 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda74d5d-fa08-31c9-8ed1-a436dee7db9f | -6.97123 | -42.86505 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 4025d8b1-740d-3a67-b57d-efa180f4656c | -18.92659 | -42.08542 | 2025-08-05 04:17:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ea5db2a-6a38-319d-b336-c27ae96c8937 | -17.20258 | -44.83161 | 2025-08-05 04:17:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4518a6c4-213b-32c8-9710-0f4598fde3a9 | -17.3597 | -46.08392 | 2025-08-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
