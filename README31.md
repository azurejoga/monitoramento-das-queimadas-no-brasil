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
| 9027048a-a754-3822-8224-b3df78d79c66 | -18.22298 | -41.24257 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 19c0229c-fad2-310f-a3f8-352625fa766b | -12.62882 | -50.79996 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ad24992-9568-32f4-9bbb-a14afa27a804 | -15.8838 | -39.94166 | 2026-09-16 04:17:00 | NOAA-20 | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 74ffdc62-78ed-3ae8-89d9-c07e39320eac | -13.56129 | -43.52899 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d6b0f77-513e-3b00-b47e-e0ea2240e4f7 | -11.54183 | -46.85555 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b7a9917-ff4b-352d-907e-7805097c5e51 | -15.892 | -40.23271 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 96f7a8da-dc37-3eb0-adda-4baaada43c52 | -18.22534 | -41.25185 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f481c0b-0bba-3a8b-94a8-2da48d7d63f5 | -11.78996 | -46.58826 | 2026-09-16 04:17:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 182de25b-b36d-3ca9-855b-a4ee01b0f547 | -12.3805 | -48.0061 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab0621ab-c07c-365f-9227-1906651ffde2 | -10.97072 | -48.31294 | 2026-09-16 04:17:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36842792-13ad-3a35-9d73-ccc3885e9fc9 | -11.55234 | -46.86193 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 905e4921-90f6-3616-98de-b151e7c704ce | -12.47277 | -41.41808 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2f15919b-f2c0-3705-951f-a01c514103d7 | -12.5315 | -47.10868 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 746b84f7-d78a-3695-8fe1-e53cbcf75319 | -15.63651 | -39.80563 | 2026-09-16 04:17:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd67b535-c71e-36ee-8a84-0dbe102f2926 | -12.54438 | -47.10423 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db1aad98-6920-34cb-9564-7ea28537bd13 | -12.46827 | -41.3984 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ff18cbac-ead7-3672-9eea-f646951472c1 | -11.31562 | -47.23763 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd6c33b1-d918-3962-818f-16d16943c467 | -18.23314 | -41.24884 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 29ffdb58-1af7-3a2f-8f7a-24df164c7db6 | -12.31584 | -47.96454 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08894bc6-26dd-3a05-818e-c26ea6b13925 | -11.54106 | -46.86003 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 455289a6-bdf9-3336-ac51-09f8af547f41 | -14.22659 | -48.51054 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d0d2baf4-3b06-3dca-b9f8-bf6bc72b1838 | -15.03001 | -41.46061 | 2026-09-16 04:17:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 47e4ac15-d03a-324c-b9e3-7777516bfcd6 | -11.40977 | -51.42579 | 2026-09-16 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dacb4ead-5221-3a44-bab7-d3488d3e957a | -14.22561 | -48.51614 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 337f4073-0b07-3e38-97e3-0f17735cda9a | -17.0356 | -41.27448 | 2026-09-16 04:17:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3f7a8474-b94b-35b8-ae82-fcfa054d741b | -17.04321 | -41.29107 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| a4b3af07-543a-3f50-9f36-8b2b52f4a87f | -12.15117 | -47.99067 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d59eca0-2e85-35cb-bf4b-961af85be276 | -12.53523 | -47.1122 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18450e96-f361-3b22-8c7e-1e4ebb8c0cc6 | -11.98246 | -52.46975 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41946384-84b4-3ad0-adea-b2058ef658d9 | -11.89082 | -43.83815 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c205a4e-9acb-3f75-96c7-c34828bf0930 | -11.34052 | -47.3227 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18e0399d-3c27-31ce-b5e5-2815af994ff2 | -15.49316 | -53.80853 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7b94574-78c7-3646-aac1-29645131de6f | -15.78824 | -41.81247 | 2026-09-16 04:17:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e52a0822-404c-385f-8d04-d0622541a7e6 | -11.54029 | -46.86454 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a653ea3e-291f-3c22-8d3f-0fa1fd37b31f | -17.77838 | -46.481 | 2026-09-16 04:17:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ca719e8-2d59-3076-9b37-8681be47b836 | -13.42072 | -44.42106 | 2026-09-16 04:17:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13178838-7056-38ec-a109-b355c8471eca | -13.21206 | -51.63719 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83c4de8e-e810-3a16-bdef-39a3948b6052 | -17.04446 | -41.28847 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 6642ec30-b186-3001-b8bb-960f004bce0b | -11.34438 | -47.32349 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 774f825d-4037-3da7-a641-c0ba525590d2 | -11.26502 | -54.1322 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d429212-97ac-3fee-ac8e-b9d2810d7403 | -13.55466 | -43.52769 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd030ee1-1ed5-3cb8-9069-7255daac7f17 | -18.22594 | -41.2476 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6e6951cd-4f31-3a69-ba4e-6e99d63d0825 | -16.25213 | -40.3155 | 2026-09-16 04:17:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5e4520ef-ea45-326a-9b72-9006bd8aa253 | -14.85914 | -48.1286 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f39a9d9a-7dbd-3116-936b-84865bac0539 | -16.03947 | -51.74469 | 2026-09-16 04:17:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22b9090a-45b0-3fdd-8277-deeb18b9b7e2 | -11.98181 | -52.47321 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b9dc446-c67f-3707-945c-fe01c09a45fa | -11.61355 | -46.95764 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74363744-5070-30da-9d0d-220fec49d588 | -12.11992 | -44.21112 | 2026-09-16 04:17:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65382246-7c26-378c-afaa-b9511d90239f | -13.55141 | -43.50536 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c5978809-abb4-3348-b6e3-b7aa675ac4f1 | -11.25644 | -46.57108 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64f15b1f-2d8b-31d4-96cc-50bb2018240d | -11.89038 | -43.81977 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63e3b9c9-e964-360f-a61c-b380f3a2cc49 | -12.51953 | -47.15729 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a663363f-cbe2-3853-9983-68c00dc1a700 | -11.31094 | -47.2417 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbb52649-b324-3e44-a568-935dbb5b4732 | -16.86282 | -50.15763 | 2026-09-16 04:17:00 | NOAA-20 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc45ebbb-fc26-357d-bdb1-16a587c4fc14 | -16.03949 | -51.74242 | 2026-09-16 04:17:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f97ae385-703d-376f-bd99-9db14ab86dd9 | -17.03794 | -41.28336 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4e435601-1820-3329-aa72-fe2d7db813a9 | -17.03965 | -41.29056 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| d57cdabc-14e9-3b55-be50-ecb8cfece2d1 | -11.54405 | -46.86514 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7428ccf-ab7a-3cf4-adf7-5e23a5e34975 | -12.47166 | -41.39898 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c08314fa-9c94-3507-9259-6226237c0f54 | -11.54781 | -46.86578 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 230eb740-8d09-33ba-996d-b0737b03f600 | -18.64546 | -47.28802 | 2026-09-16 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868332a3-016d-3e00-b507-bc8dd07004bc | -10.8888 | -51.50027 | 2026-09-16 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77f4e869-c0dc-37f0-bbdb-bb5c968f0214 | -13.29502 | -51.27599 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3debd928-2982-32df-885a-6cdaf5dc6c28 | -13.75508 | -48.80802 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da9bcd60-a1e4-36ce-850e-59d8b000db21 | -11.19545 | -54.12833 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed063a2a-958b-3247-94e4-e9e2199a32e3 | -11.54482 | -46.86063 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c2edbf6-0eeb-3bec-a547-72cb5649056d | -15.041 | -48.55095 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c69a9b0-d16f-3422-a010-7e1e3c252910 | -10.47407 | -50.96247 | 2026-09-16 04:17:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5dcf32a-3b3d-3241-9caf-d1ed8c05fcb0 | -18.23178 | -47.26544 | 2026-09-16 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8b744d3-c30f-3fbe-b646-2bc1c2e95f8e | -13.75049 | -48.78713 | 2026-09-16 04:17:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83aef591-0069-3a63-956b-45b9ebb884a6 | -17.03854 | -41.27923 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 67a77efe-90d4-30d0-a5be-0d0dd133c706 | -14.84264 | -42.4053 | 2026-09-16 04:17:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a8e9cb3d-c3a2-37d2-8157-93f4fb5687de | -11.97964 | -52.46996 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87b1f4f9-761c-33e7-b7e5-1685b0baeda5 | -15.28075 | -42.80413 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65f09af5-a3ee-3c04-9c75-09d3cd47de89 | -14.60825 | -42.14613 | 2026-09-16 04:17:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 90127a65-7197-3ded-af42-a59d8c2608f9 | -17.03498 | -41.2787 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 68fa29ab-305b-3792-81dd-523d393b5db9 | -13.77117 | -43.64026 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a434e2a6-4b66-3b74-bf90-10414d2029d4 | -12.62138 | -50.78935 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc909178-5812-34d0-b068-d8c65edda904 | -14.66451 | -48.02157 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ff8f9af-5dd7-31be-b1b4-2cf64163ef9d | -15.4736 | -53.79259 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ec351ee-60cb-3aea-b27b-078878196945 | -12.47334 | -41.4143 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 499244be-1856-3492-a84c-df023e13b51a | -11.41033 | -51.42278 | 2026-09-16 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57bb1a8e-922c-3dbe-9079-58fd438dca87 | -14.85818 | -49.97168 | 2026-09-16 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f108e86b-0dd8-3cac-a52d-485042f8fe78 | -14.66068 | -48.02082 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d05e6cd8-f62a-3e10-992f-e1f3edf0e5c3 | -15.4587 | -53.7819 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec0551d2-a88e-3af6-a830-a6cfc05b1479 | -11.88922 | -43.8269 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa1dfb2c-c6dc-39ee-b049-def8d36413a0 | -13.76586 | -48.81831 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0600a659-5608-3284-b3d3-9a5b7b20321b | -10.69286 | -54.17173 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83733c83-d07e-38f6-95a3-78c4069cba1e | -12.32376 | -47.96602 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fe1e3f54-6c9d-34ff-9578-7ed393666542 | -13.34762 | -46.30388 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b1d40af-b802-3649-84c1-4b08a495130c | -12.53148 | -47.11152 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a19ef425-db27-3d06-aec1-f1458be687fe | -11.31178 | -47.23689 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07cb43bf-6498-3689-be97-2b0f6bbc24ba | -18.236 | -47.262 | 2026-09-16 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0037a993-73c6-3ac7-b7c2-baa7a705a8ae | -15.5129 | -53.85098 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03fcccf0-ab7a-300e-bedd-4ead1e43d9aa | -13.29019 | -51.275 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f661b80b-57d0-3b43-af5d-7802b2d5581c | -15.28354 | -42.80823 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5d7e5fa7-b559-3edf-8ca4-f5b41993fe08 | -12.41253 | -48.47838 | 2026-09-16 04:17:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 320600a5-e5db-3e59-8ff4-11372d0308b9 | -13.21223 | -51.6391 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad3bc116-692d-3596-adcc-618995c958db | -18.2272 | -41.23886 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| feb2d0e4-cdc7-3655-a0cb-920f36dad0f6 | -11.59895 | -47.33923 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README32.md)
