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
| 634bcb6a-0fd5-3269-8089-cc79cfb751a9 | -2.7741 | -45.3989 | 2025-10-30 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 958e90cd-d046-3c84-ae23-8195cb4a02f0 | -3.2316 | -46.8936 | 2025-10-30 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| cc4fd715-cf41-31ec-a067-a19ceb19fc77 | -4.2648 | -59.675 | 2025-10-30 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 5fb0178b-4de1-3b7c-b738-ac6113e1c851 | -4.2833 | -59.6362 | 2025-10-30 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 158e112c-2ecc-3da5-9eb6-d61df33d395e | -3.2317 | -46.8716 | 2025-10-30 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8a099710-ebf4-3fcc-b829-a2ab0e911ee7 | -8.3311 | -47.9438 | 2025-10-30 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| ad06af7a-11aa-34c4-811a-99be82d343ad | -10.6313 | -52.1891 | 2025-10-30 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 426886f6-4125-3b6c-925e-d076b42f7079 | -5.3851 | -47.2052 | 2025-10-30 00:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e2d02d3c-15c9-304c-bbf9-e0dc00f075b5 | -4.2649 | -59.6558 | 2025-10-30 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 130.1 |
| a92f8341-36ae-346b-9630-2d683a7922f8 | -15.0862 | -41.9924 | 2025-10-30 00:30:00 | GOES-19 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.3 |
| 3097c210-fe84-3c2a-a679-2e648e12c426 | -4.2832 | -59.6554 | 2025-10-30 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 0523122a-fcba-3e4a-948d-cabe6e5a14df | -13.3743 | -54.3159 | 2025-10-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 3576e8cc-be1b-3e5b-b16e-9a7ff04eb569 | -4.4804 | -43.447 | 2025-10-30 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fa0d9362-2862-3dc0-af4f-b61e209002d3 | 3.1461 | -60.6886 | 2025-10-30 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e771bf58-c7e9-3d0b-a393-ff38ea096c01 | -12.1958 | -46.717 | 2025-10-30 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| ca7475b0-fbce-3b6a-948f-ac205908ed7c | -4.4805 | -43.4237 | 2025-10-30 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 1ef64b55-78a5-3619-9e8a-575da7ee064b | -10.6502 | -52.1873 | 2025-10-30 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| b06374bb-5b9e-3f9e-8004-03cdf386022e | -6.4868 | -39.7324 | 2025-10-30 00:30:00 | GOES-19 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 34bc96b8-296c-3ec2-a8ba-148bd02f1efd | -18.04627 | -43.15861 | 2025-10-30 00:30:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38e99c1a-3054-31df-8742-e34672793865 | -17.77705 | -40.18659 | 2025-10-30 00:30:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| 43aa8382-aa05-35e1-aa15-05c53ef9e5d1 | -18.24882 | -42.63264 | 2025-10-30 00:30:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.6 |
| 3630967b-e3a6-3a49-be84-21b2ad9a697a | -18.55425 | -41.57921 | 2025-10-30 00:30:00 | TERRA_M-M | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 819c52b1-1725-37a0-a287-27c0547adbf8 | -17.94979 | -42.99662 | 2025-10-30 00:30:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1685c565-172e-350f-9486-5a742781ad76 | -17.78236 | -40.19112 | 2025-10-30 00:30:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 86957729-2464-381a-9cff-0bd6c060f832 | -18.13084 | -42.61408 | 2025-10-30 00:30:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1624d88e-f00b-3d84-b41b-302fbf1738c0 | -18.72368 | -42.57564 | 2025-10-30 00:30:00 | TERRA_M-M | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d5db1295-e16d-3748-9ab7-00d5ebcdb1e1 | -18.35933 | -42.25271 | 2025-10-30 00:30:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| f688cf42-2abd-371f-ac64-46b7ece41538 | -19.33347 | -43.05756 | 2025-10-30 00:30:00 | TERRA_M-M | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| b28ed06b-ced6-3e01-a678-e4d79bdb102f | -19.33561 | -43.07087 | 2025-10-30 00:30:00 | TERRA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 747ea420-92ac-3a6e-8c7b-cf9c52ff0668 | -18.24642 | -42.61798 | 2025-10-30 00:30:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.5 |
| 771a1cc0-eb26-3853-b8b0-cfb4852aa748 | -18.23046 | -42.37974 | 2025-10-30 00:30:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| cf4fab53-8ff2-3fa9-a04f-8ab83aa24cb8 | -20.65701 | -42.93784 | 2025-10-30 00:30:00 | TERRA_M-M | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| 43e25f10-1c8f-30ad-bc3f-a56a8246176e | -19.42663 | -43.0632 | 2025-10-30 00:30:00 | TERRA_M-M | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 07adafe3-fded-3e65-b583-73d79ecc402e | -17.77289 | -40.16367 | 2025-10-30 00:30:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 77bb0c32-4fe6-39b9-be9d-f6d89dc8c8bc | -18.35685 | -42.23778 | 2025-10-30 00:30:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 223a37f6-fb39-3fd9-86d7-37fb2d676a62 | -18.5485 | -41.58617 | 2025-10-30 00:30:00 | TERRA_M-M | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 33f08ef1-a403-39d6-811e-61cb8ef05dc9 | -18.04401 | -43.14458 | 2025-10-30 00:30:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3dbd9801-496e-3cbb-8d1f-58c52369c64e | -17.77838 | -40.16816 | 2025-10-30 00:30:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| 4e3723af-3e97-36ab-b604-cae41f660a10 | -20.65911 | -42.95061 | 2025-10-30 00:30:00 | TERRA_M-M | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 4ea7cf04-a423-3cb6-9ec1-03468442d41a | -19.06649 | -41.12605 | 2025-10-30 00:30:00 | TERRA_M-M | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 319328f6-b79d-33fe-bcc5-0ec9f2681f09 | -11.54698 | -47.95949 | 2025-10-30 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cef9436d-e91d-3ba9-bd84-c83441d345ab | -13.16525 | -48.45747 | 2025-10-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51831a5d-3125-3abc-9611-9bf7bf9f5bfb | -12.00846 | -49.97078 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 90dcfc73-faba-31ca-8d61-e4005d86fa21 | -9.49488 | -40.38596 | 2025-10-30 00:33:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 35.5 |
| cf0a9551-ebb2-34c1-8b7c-50ab722ee67e | -12.49485 | -50.58265 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9d0d666f-2132-3593-8fed-641ad0ae8a83 | -14.97939 | -43.37955 | 2025-10-30 00:33:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 9ef5c0db-9c78-3f2d-98f5-3dd5c05f8d63 | -10.91767 | -47.81442 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8f01a6ab-002b-38a4-8770-126dbf54d5e2 | -13.30806 | -47.71027 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9366f53-5f5e-3e0a-aa42-7ee297929744 | -12.81034 | -43.44746 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 617e2e5b-bdfb-3fc8-95a7-c375338f3a89 | -13.04042 | -46.74433 | 2025-10-30 00:33:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 73bcd33a-8e6c-3cce-b9ac-932dc3716273 | -13.15516 | -44.01252 | 2025-10-30 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4f1fd3d7-3f8e-3916-897d-315877227d2b | -14.13099 | -44.06988 | 2025-10-30 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e493fa69-b7cd-3ee7-9e91-aae4b2e0f3c3 | -10.65214 | -47.8912 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 10440758-c1a9-35a5-bcc7-b1f437884967 | -12.31756 | -48.06614 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ec3c9f09-0091-3758-b02e-238fd50f82ec | -13.04669 | -48.67116 | 2025-10-30 00:33:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bb5841a-3014-3dd0-8483-377688bd9c2c | -12.91927 | -45.04656 | 2025-10-30 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 18c34cab-3e3c-3837-a64a-607c2316b9d6 | -12.90951 | -43.19347 | 2025-10-30 00:33:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 5e0ded8f-84bd-31cf-a3ac-5cb328ef6c58 | -11.53541 | -44.96601 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4cc87563-1d1d-37db-a496-b1fddbb3ea2e | -11.68196 | -49.0535 | 2025-10-30 00:33:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d797fc6-2883-3fff-aba0-fa6a8c611f5a | -12.82428 | -43.4612 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7db0981c-d62c-3233-942e-f31dec6c887b | -12.23484 | -46.47807 | 2025-10-30 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 76fe2503-996f-3678-9a80-7a51ae5ef918 | -14.38843 | -43.71682 | 2025-10-30 00:33:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a9572bac-4b3c-3986-9fe0-a47616dc5ee2 | -10.9503 | -48.04477 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39a6377a-f5ee-3ea7-9b82-9a06ac17ac64 | -12.39891 | -46.83567 | 2025-10-30 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7040dd5b-2c47-396c-8878-1a240b7ae5e8 | -12.47182 | -46.88452 | 2025-10-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 652ddd7e-d9d6-334a-bca2-0fd8fc64d5e1 | -13.13106 | -42.51015 | 2025-10-30 00:33:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 0818513a-f8e4-3e56-8e0d-795294427c79 | -16.67898 | -41.36623 | 2025-10-30 00:33:00 | TERRA_M-M | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 6152f8ee-a3e8-3cac-b5c9-843c5a6c350f | -11.07226 | -50.33237 | 2025-10-30 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 7dd8171a-e10f-345b-9929-c8b6ae7bbf41 | -11.07078 | -47.53005 | 2025-10-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8d7b4268-36b8-3023-8cdc-e4948837c5fc | -12.52951 | -47.54685 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 138b11e1-9a42-3bf0-8c6b-14205b808830 | -13.57879 | -47.34269 | 2025-10-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| afe19c15-5897-3fca-a90d-bcd420003481 | -15.09778 | -41.98756 | 2025-10-30 00:33:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| dddacfc7-49cc-390f-ac60-607ad336821f | -10.76207 | -47.88758 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f23f48c-86a7-369d-ac54-d0a7543f2f5a | -14.30859 | -48.00406 | 2025-10-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8a5ca838-a044-3cce-b72f-55e8d26ff926 | -12.69423 | -48.65546 | 2025-10-30 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 388ef12d-e32e-3af7-83ea-5015d08f2ec0 | -11.5546 | -47.94898 | 2025-10-30 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ef4b366-0aac-3bbf-863f-c5bed950a313 | -14.32627 | -48.00141 | 2025-10-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d1b3f814-7423-35fc-974e-59f9a2621391 | -13.0269 | -47.02987 | 2025-10-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c4242d45-df52-356f-b60e-652b6793a144 | -13.36739 | -44.89228 | 2025-10-30 00:33:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fa3a8203-e38b-3a64-b17d-71627f7b74b5 | -15.79849 | -43.83945 | 2025-10-30 00:33:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 00894b10-5ca1-3709-be0f-9a22705282d5 | -12.39747 | -46.82586 | 2025-10-30 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a54d218a-3e08-33e6-af9a-37a6dfa1c5b6 | -10.64278 | -52.18513 | 2025-10-30 00:33:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 3fba05c9-decd-3fc5-a116-9c04de7d43b6 | -13.30677 | -47.70114 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 74cfc939-7d48-3f3f-abb4-a3dd5e52ef66 | -12.31153 | -50.31587 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a34680f9-663d-3202-a97c-66ee4e133530 | -13.33037 | -47.47463 | 2025-10-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd786220-4a6e-3d96-b20e-4de228a6b0be | -10.87427 | -48.62289 | 2025-10-30 00:33:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b9eeac49-6bfb-3617-80dd-99c52fe3ae28 | -16.81417 | -41.22789 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 8aba7a8c-c15f-3ce2-9813-9a42aed33e84 | -13.98638 | -44.0169 | 2025-10-30 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8758d526-1301-32c9-b09e-d3435b97e54c | -11.54568 | -47.95034 | 2025-10-30 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37762cab-8113-3342-9ed2-69488477b20a | -12.29218 | -48.07899 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0ae16bde-28f7-33d9-9010-fd935c579505 | -16.86535 | -42.36557 | 2025-10-30 00:33:00 | TERRA_M-M | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6588a1c2-7005-3feb-91d2-7075c5930df7 | -12.00721 | -49.96144 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ffe1516-f971-364a-b5aa-7d3807c68a5e | -10.47754 | -45.03048 | 2025-10-30 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c66c31a7-6b47-34c1-b175-2b174c3319b1 | -15.61428 | -43.97931 | 2025-10-30 00:33:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2d278682-3d1b-3acd-bc5d-2b19c411d9bd | -12.32898 | -50.16696 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c2c893e-cda8-3bab-8393-61b468452f0c | -13.59883 | -42.30016 | 2025-10-30 00:33:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6b1124d6-a20c-3f29-8478-b6e59cb28aa2 | -11.38747 | -48.07022 | 2025-10-30 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eaf15f94-f950-30db-b86e-dcb43a245536 | -10.63287 | -52.1865 | 2025-10-30 00:33:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ab569841-d6fd-39e8-bba0-fb97ce64cc7b | -14.68244 | -46.36649 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f12be9e-dc10-3fd4-acba-c4ee62cb6e10 | -12.30522 | -50.26775 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README3.md)
