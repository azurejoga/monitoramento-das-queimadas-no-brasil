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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5d54e7b-90e7-30f1-8778-81f777897d45 | -19.7901 | -43.137299 | 2025-07-31 00:31:00 | METOP-C | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc7dd721-4833-392f-bb27-e771fe3c09f8 | -10.5967 | -45.242199 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4d9d4a7-d9d2-3076-943f-21fa02d9cb43 | -6.6253 | -56.3927 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aacca157-3fea-3a66-9031-9de0dbb0d583 | -5.6855 | -44.518799 | 2025-07-31 00:31:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 243ee95d-6228-385c-8c13-679a89d0c044 | -6.4661 | -56.164001 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc801aa-56f9-3b10-b2a6-ea8b3ee516ba | -7.1035 | -46.110802 | 2025-07-31 00:31:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a12eb09-692c-3a51-b7c7-abed2760cd01 | -10.5704 | -45.262798 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 123afefb-3be8-3375-8894-5d87b4540cd0 | -8.1231 | -45.021 | 2025-07-31 00:31:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ceeaae17-8a34-39e3-81d2-a2eb9ae57939 | -11.4832 | -44.2873 | 2025-07-31 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e5c180c-5760-3744-b109-de392116dea6 | -7.8396 | -45.5406 | 2025-07-31 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1393c16-a60e-3a30-ad9d-1e440285bfaa | -8.0219 | -43.113899 | 2025-07-31 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 926ea860-95a7-3dbb-a546-5362194a449f | -9.5899 | -43.861698 | 2025-07-31 00:31:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1abe256a-f9e2-30dc-8e9a-12ea4b780d05 | -11.5047 | -44.245701 | 2025-07-31 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae68db1c-fa8b-3d98-be57-3c91e79e7e28 | -18.4098 | -46.916698 | 2025-07-31 00:31:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b540c931-ea15-31a2-ac7b-f954ce4a446b | -6.4713 | -56.188599 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff21a28-9837-31f4-9111-45ad1268a313 | -18.5702 | -43.772202 | 2025-07-31 00:31:00 | METOP-C | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b03ae26b-2945-3929-9fb5-9f240a947eb0 | -13.0249 | -47.397301 | 2025-07-31 00:31:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b3974cd-e3e6-331d-9131-3191cbd6dba4 | -8.5786 | -45.525398 | 2025-07-31 00:31:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87e87eb8-b84a-3fbb-ad6e-c731435aa809 | -13.1728 | -47.2262 | 2025-07-31 00:31:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19a5e563-2a9d-3f74-ab63-7b514704c864 | -6.6199 | -56.3671 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a83318-e2f4-3c06-a43f-cede91e0635b | -13.4773 | -45.693901 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15b55d66-3b3b-3c8d-aaa2-f2ce9dd90963 | -8.559 | -45.5298 | 2025-07-31 00:31:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc8e3291-c532-37ac-b10c-7a3e8507f027 | -16.3225 | -52.643398 | 2025-07-31 00:31:00 | METOP-C | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f790a47-44c7-3052-873f-0c963b1c1b1d | -11.5063 | -44.252701 | 2025-07-31 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca3299cd-78cb-397e-b300-f6e17ecaed0a | -8.0201 | -43.106201 | 2025-07-31 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 78009249-5d50-3bc2-9d49-57170f4e79a1 | -11.7169 | -48.183102 | 2025-07-31 00:31:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1b60e2c-b353-306b-8a5a-800087f6b4be | -10.8932 | -44.503799 | 2025-07-31 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82adff52-7610-3c93-8967-8a24974d3872 | -19.7885 | -43.130001 | 2025-07-31 00:31:00 | METOP-C | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5c552eb-1da9-3a2b-9827-1eb328e4ba25 | -19.418301 | -44.3204 | 2025-07-31 00:31:00 | METOP-C | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d86fd0ec-4908-3f0a-a8b8-61f347484d92 | -18.9254 | -44.561699 | 2025-07-31 00:31:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 75c855cf-6c05-3f0e-ab78-8c4d571bc0fb | -12.586 | -48.0788 | 2025-07-31 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a101766-7bc2-3ee2-ac68-a8f6f3b46784 | -10.5803 | -45.260601 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0dd05fef-b30a-32db-a679-09177139eb32 | -11.1708 | -42.7556 | 2025-07-31 00:31:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 070e4f67-d4eb-3b64-9afc-e96926f05887 | -12.7891 | -43.097301 | 2025-07-31 00:31:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d40a57a1-b4c3-39e2-b9fb-2b050c869e26 | -11.709 | -48.194 | 2025-07-31 00:31:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 005b89bc-b05b-3ade-9d40-b55e04570197 | -13.5041 | -44.149502 | 2025-07-31 00:31:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44975310-e51a-3b5f-b21e-aa92c50facf6 | -10.0377 | -53.882401 | 2025-07-31 00:31:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 200efb3b-c796-3056-ae5c-05ca628dbcd7 | -20.4958 | -46.1166 | 2025-07-31 00:31:00 | METOP-C | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 92e4fb52-c208-317b-9c02-b173c73f3ef3 | -16.5842 | -44.101501 | 2025-07-31 00:31:00 | METOP-C | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eddf8377-451f-35eb-90ff-af2434e29246 | -18.4196 | -46.914501 | 2025-07-31 00:31:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 445581c0-8aff-3467-974b-90eb7af75b69 | -6.481 | -56.1866 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 625e0376-4b59-3ff6-9496-d9ad2603c9ac | -6.5004 | -56.182598 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dc70bbf-ff27-368c-95bc-db32251d893c | -8.9745 | -47.983101 | 2025-07-31 00:31:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f518f04-edbf-3945-901a-e90b5c363d0e | -6.4907 | -56.184601 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98b74d7-2dff-31e8-a6a4-6ed161b12894 | -13.4839 | -45.677101 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b76429a-d70b-33b6-b04a-df9829af4ff8 | -18.927 | -44.569302 | 2025-07-31 00:31:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8394d310-e5e3-3498-95e4-91e114e75d1a | -8.8833 | -47.338402 | 2025-07-31 00:31:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 446598e8-5f9a-30ed-9a56-952547281104 | -19.1467 | -43.4902 | 2025-07-31 00:31:00 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| adc6b34c-f0dc-37f6-845f-f84ce3a1b11e | -12.5879 | -48.087799 | 2025-07-31 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4630147c-b329-3d09-954c-1916f8a436aa | -7.8443 | -45.561199 | 2025-07-31 00:31:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be1b7b04-9c54-30d7-af11-538dbd35d6c2 | -7.8314 | -45.549702 | 2025-07-31 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e6d838a-4dc0-3ddd-9e72-43c0b335f38c | -9.5981 | -43.852299 | 2025-07-31 00:31:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c2b20bc-a1f8-321f-bfa7-015f9d17e358 | -17.0082 | -43.783798 | 2025-07-31 00:31:00 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fae89824-b4c4-3c3b-a11c-7305c274c7ee | -11.8825 | -44.546501 | 2025-07-31 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66481ee0-cc9e-3ab2-b5c5-b2ebd97861da | -12.5898 | -48.096699 | 2025-07-31 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ad90889-280e-3a00-bf1c-7805d5b9ea2e | -4.2679 | -48.1022 | 2025-07-31 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf1cffb4-71c2-310a-ae47-356c6a7b808c | -13.1157 | -47.342701 | 2025-07-31 00:31:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59c52d7a-9e7a-358b-9c56-b498ed7135bb | -17.006599 | -43.776699 | 2025-07-31 00:31:00 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c4d771f4-3431-3e65-9760-967d0acdf6d1 | -9.5883 | -43.854599 | 2025-07-31 00:31:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ccbd8c4a-cc9e-388e-a4db-a73b96465b91 | -11.0984 | -48.644199 | 2025-07-31 00:31:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc78ac79-87dc-33a0-b99f-f527e45e813a | -18.497999 | -46.696098 | 2025-07-31 00:31:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3699eead-372e-3c74-badd-85cbb2b8a262 | -11.5028 | -44.282799 | 2025-07-31 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a69a8f4-7d5d-3116-ba27-b9826087b3a2 | -9.5263 | -43.8988 | 2025-07-31 00:31:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c21fcc18-5047-3f03-972c-ed17a43bbf7e | -8.0316 | -49.7225 | 2025-07-31 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c68d74b3-c48a-3584-8f33-5ee26939c97d | -11.4816 | -44.280399 | 2025-07-31 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5e200d0-8e74-3973-804c-9791ba127862 | -9.3567 | -45.501598 | 2025-07-31 00:31:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7389eb7-6139-3385-8749-14ec4d47f63d | -8.1329 | -45.018799 | 2025-07-31 00:31:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37f14fd7-c142-32b9-9696-c5dd762acbf8 | -5.6953 | -44.516602 | 2025-07-31 00:31:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f65b19a7-9af4-30e9-89a8-3938c452497f | -13.4758 | -45.640499 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 055f2eaa-5f4c-35a3-bb9c-5b9759238e0e | -10.0251 | -46.551201 | 2025-07-31 00:31:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2da8e74-85ab-3717-98f0-4614cc4b2ac7 | -5.4612 | -44.396702 | 2025-07-31 00:31:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8eaa3133-51ce-3968-977f-cf6ac558098a | -6.6102 | -56.369099 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d219b1af-31b5-3bb3-abfe-21803bac88dd | -10.572 | -45.269798 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7e3705c-bc9b-3f9b-9881-7de8682b5bbd | -5.3664 | -44.433399 | 2025-07-31 00:31:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cef498c-b02a-3aac-8bc7-ccf449a1871a | -6.6307 | -56.418301 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2db2e62-e4c4-3ab8-b7f9-bdd29e933e02 | -10.4861 | -42.567001 | 2025-07-31 00:31:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0486618e-0889-3441-b778-8c5c6c150bd8 | -13.1711 | -47.217899 | 2025-07-31 00:31:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95e61ac9-bec2-3cd5-894a-8b855d31a874 | -10.0435 | -53.861198 | 2025-07-31 00:31:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94070a04-a77b-32dc-9103-e3635e8c3d08 | -6.5399 | -51.102402 | 2025-07-31 00:31:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7d32de-a230-30df-a76a-54e67d199d90 | -10.4825 | -42.551701 | 2025-07-31 00:31:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f55a6637-422c-37bf-b8ff-63c2503dcb4e | -11.1725 | -42.7631 | 2025-07-31 00:31:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 23bae916-8db1-31fb-af34-df6b9b6e0e67 | -16.335899 | -52.661499 | 2025-07-31 00:31:00 | METOP-C | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ceac56f-94c5-3573-997e-df3500bae01f | -6.6156 | -56.394699 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4f6db94-cc0e-304b-9a3e-550d645e54a2 | -13.4855 | -45.684399 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e2c6240-d718-3ce8-9e24-5606c742819f | -6.4862 | -56.2113 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0c02db6-a917-3143-bbe8-156ad768a721 | -6.421 | -44.574902 | 2025-07-31 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb30f87c-e5b9-3b6c-9d12-e4ac856c8738 | -10.6081 | -45.246899 | 2025-07-31 00:31:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a955db3-0e29-37ca-bf64-81c59163d723 | -7.0861 | -44.908298 | 2025-07-31 00:31:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbe7ad41-3df6-3b6b-8ceb-21ff3aa17744 | -8.9728 | -47.975101 | 2025-07-31 00:31:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e6d27f8-8900-36a5-a63d-a46586380658 | -11.0886 | -48.646301 | 2025-07-31 00:31:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b187a0f8-847e-3b03-ad81-0aaab38cbb2b | -9.5344 | -43.8895 | 2025-07-31 00:31:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b971011-4f72-3c87-8cd9-8c34c472d299 | -6.5301 | -51.1045 | 2025-07-31 00:31:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96372b0e-287d-339b-9a54-6ad3cf439889 | -6.4213 | -43.201199 | 2025-07-31 00:31:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3933c76-c6be-3144-a913-9ab778fbf3db | -6.5197 | -56.178699 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 517528ed-ea72-357b-9acc-15bf75113939 | -16.3323 | -52.641602 | 2025-07-31 00:31:00 | METOP-C | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 442f488b-6313-30a6-bb22-9f2d695634ed | -10.6065 | -45.240002 | 2025-07-31 00:31:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e531c425-82cf-3efe-a722-94a6940272f7 | -7.1019 | -46.103901 | 2025-07-31 00:31:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a953e15-6889-3e08-b145-90742f290bb6 | -7.4508 | -43.941002 | 2025-07-31 00:31:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 38c3d477-db1d-3bae-bd40-8ae1d8c4c617 | -6.4403 | -50.135399 | 2025-07-31 00:31:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e878d5d-d072-3c8d-a0b3-1aec18a250fd | -11.7188 | -48.191898 | 2025-07-31 00:31:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
