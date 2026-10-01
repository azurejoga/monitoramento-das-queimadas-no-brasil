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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ccb5dea-d088-373d-b168-4930a51e82d1 | -15.77737 | -46.02816 | 2026-10-01 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9f75e37-5fc2-38c0-b7ab-f3e42b691177 | -14.15132 | -51.14424 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3d960b3-258f-36a8-8438-7bba1eb3e941 | -16.43164 | -47.17768 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0088ca10-76b7-3dc3-a116-2eaf488a05ec | -15.12204 | -43.61738 | 2026-10-01 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca1d1f83-c22c-3b07-8996-977c212eb39f | -12.78322 | -47.28992 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b7d3b10-2042-3bd1-b146-a312f60d8893 | -18.06398 | -44.52697 | 2026-10-01 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6344a143-d62d-39e8-aea0-0e9cededda53 | -19.34055 | -41.45411 | 2026-10-01 04:17:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1667d7a0-7105-353e-ae35-bdb11fd92463 | -15.23722 | -46.15232 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5031a3c-39d9-30a7-a65a-f33a905831e3 | -12.66826 | -45.0976 | 2026-10-01 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fbc7439-41f4-37a8-aad0-5bda9d586333 | -15.85294 | -41.70627 | 2026-10-01 04:17:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0645b907-2f06-3403-a14b-ae57fc3a7c07 | -13.37673 | -43.99544 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19c9b1eb-8b39-37c4-b61f-4c6d227963d4 | -12.08726 | -50.69789 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7e91bba-1b1f-360d-b4ca-7e96cc3ce8f3 | -12.70523 | -46.95633 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2b86e71-f767-3b08-8968-360a98862931 | -13.38672 | -46.81231 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4f20617-e6ad-3656-9d9c-c97f6a017df0 | -14.55019 | -42.73977 | 2026-10-01 04:17:00 | NPP-375D | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5c1d117-c36a-3857-8116-aff5633b10d0 | -13.39294 | -44.00646 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc4c2f6e-2e7a-379e-aa72-e0d5e457348b | -14.34379 | -44.74519 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 600464db-d63b-3050-9990-1c30e03d9d51 | -11.79881 | -50.51686 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b3abce0-15fb-3151-8329-449e0fe1f349 | -13.39223 | -46.82831 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed142e2f-97d5-3c9f-906f-461263387d40 | -14.38307 | -51.29972 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5547f949-ad40-3ac5-b0a9-25ce3fbbeda6 | -19.23125 | -42.94673 | 2026-10-01 04:17:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fc510a46-09c6-3db5-8221-71da8d348b22 | -13.65974 | -53.94053 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c3889dab-9445-30a6-b06f-d9df8ab7b811 | -14.88426 | -51.88199 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39dc2c35-3831-3bb4-afd9-c6c536498370 | -11.82427 | -50.52917 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78c756b2-9164-386a-9128-c58a1520d3ce | -15.85627 | -41.70683 | 2026-10-01 04:17:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 112ff6bd-e7df-3819-9255-6298593e8237 | -15.81625 | -41.8957 | 2026-10-01 04:17:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 49d56291-c2e1-3d17-8c01-eec86ab1d409 | -18.06807 | -44.52371 | 2026-10-01 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 179a779b-09b3-35f8-a363-4af4d25b4e1c | -11.83229 | -50.52668 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5a4e3c2-cbf3-3eda-9080-a502e829ca4c | -13.37946 | -46.81513 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c13ed25-06cf-303b-8410-c71b9642ff26 | -14.14275 | -46.23905 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be8468d1-a7f8-3039-a1eb-11717626b64d | -12.55294 | -47.17865 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 482e933d-7358-352f-8f9e-9cb9d2df9f4a | -11.81957 | -50.52465 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acace9cf-fed8-35d0-b5e2-019b48b791a7 | -15.44928 | -42.09943 | 2026-10-01 04:17:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6fb1de86-79dc-3156-82d2-5840bbf907cd | -16.18279 | -42.8826 | 2026-10-01 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7835b280-bf60-3e23-96ee-9a3f6d462a8a | -11.74554 | -50.40367 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5814c9d3-5600-3cbc-91c0-d190ea9dcfc3 | -14.4318 | -51.25227 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 291f46a2-679e-3619-8575-fe1748012303 | -17.90893 | -44.26376 | 2026-10-01 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a12e9e03-58ec-326e-a7a3-362780926447 | -13.3824 | -44.00464 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99367050-19e4-364f-808e-1b82a3206664 | -14.39692 | -51.25922 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| fec442b9-21ad-3a92-9af7-28f7d2b0c84b | -18.10084 | -44.41288 | 2026-10-01 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f17299d-1a83-3f19-83c5-f5f5cab89440 | -14.86204 | -51.84975 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 083c0021-962a-3b2f-be16-0a62fcf58439 | -18.47361 | -41.42702 | 2026-10-01 04:17:00 | NPP-375D | SÃO JOSÉ DO DIVINO | MINAS GERAIS | Brasil | 3163300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6b83027d-fd96-38bd-90c0-658f59098650 | -14.14874 | -42.08834 | 2026-10-01 04:17:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 341649fa-cb21-370c-b207-c419983a8383 | -11.38032 | -55.1282 | 2026-10-01 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ad7b881-534e-316b-88a1-20f399d358b9 | -14.1621 | -51.11795 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dd444a1-852d-3577-bcaf-28f76ac1b3a5 | -13.10825 | -51.22217 | 2026-10-01 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b4e91f0-cd6a-3c0d-9c41-519ec22c1420 | -14.38857 | -51.29016 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c85bacd-51d8-3054-a4b5-1589d4e2a8e0 | -12.03675 | -51.01809 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 738ffbe1-5edb-33c7-ac3d-d46fba53f15f | -14.49424 | -48.30962 | 2026-10-01 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec1979c4-7cd4-3c0a-81de-832c365d8589 | -14.3646 | -44.77496 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1ab8daf5-eac7-3cb2-a62e-acd9570e8cd5 | -11.16413 | -54.1185 | 2026-10-01 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f7011fb-4f07-37a1-921d-10914aabb39a | -13.09741 | -47.44268 | 2026-10-01 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd607a4e-0fa7-345a-b636-a2fe002d42ba | -16.19006 | -42.8801 | 2026-10-01 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 417289dc-905a-34d4-bf71-7732a53c8fd8 | -14.14339 | -51.12822 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a6927cd-aa50-31a1-8d74-fc3c9ad44bee | -13.65217 | -53.94469 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a928c62-b7cb-3e50-98e2-4f2d11541884 | -12.57704 | -47.16137 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0d616ca-792a-3fee-8497-598839b36d52 | -18.12938 | -44.34761 | 2026-10-01 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff1a3fd9-62d5-365f-9d14-7db3ecad0d77 | -14.14736 | -51.13622 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94f3897a-13ea-35d2-b978-e20ece72df29 | -14.3852 | -51.28929 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 438a10a6-c7cf-3580-8a20-0d75bdfd66f5 | -14.38449 | -51.29276 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a7c8d326-8d8d-3063-b188-368b6290e521 | -14.82876 | -42.31562 | 2026-10-01 04:17:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1d5408e-add6-3821-9e34-9ea1f359ea0a | -14.48981 | -48.30884 | 2026-10-01 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a69f2317-a061-3b0f-a95d-5efdf60334ff | -17.95543 | -39.70493 | 2026-10-01 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bcfc20f2-dd29-39d2-8e4b-ba1f68a71465 | -17.09092 | -46.82193 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fa56ff2-5dc4-31ad-a623-feee23ad1c87 | -15.44701 | -45.68632 | 2026-10-01 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b6de57b-df01-3ec4-9cab-3ca5c10b894b | -14.88502 | -51.87827 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 055a691b-1700-3fdf-93db-43869effab86 | -16.42177 | -47.18668 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 62bcec5f-e48c-3bf2-8fbc-3d167d1aecea | -10.77573 | -54.74911 | 2026-10-01 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0cc9c11-951c-3572-802e-14f933c3e04a | -13.38698 | -46.82035 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69c13f00-6745-3ddf-9ab5-284565d139ae | -12.18636 | -48.4287 | 2026-10-01 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d2c57f2c-9ff3-3bdf-ab14-72fa2ef14f1e | -14.49511 | -48.30492 | 2026-10-01 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfeccac5-c5b3-385f-9ac2-9cbb2477b8b6 | -17.10532 | -46.47013 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44c4d959-fbfc-3a8e-ab7d-a92b4e8a88a1 | -11.38184 | -55.12101 | 2026-10-01 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41203762-37b0-3c64-9254-f1fb9362fa16 | -12.7127 | -54.06757 | 2026-10-01 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d52d7678-2d9d-375e-b95c-9f9c4525b911 | -11.82557 | -50.52232 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f2c19eb-4ec6-3d69-8fb0-b670c1696c0f | -14.40156 | -51.26384 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 3a1c41fc-9508-31bd-979d-10f436c5a737 | -17.91297 | -44.26058 | 2026-10-01 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f0f6559-26fc-3a38-8f25-a4774b8cedd8 | -12.64191 | -47.63921 | 2026-10-01 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd4e8432-6839-35fc-bcb7-219361f125ac | -12.86313 | -44.3352 | 2026-10-01 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 797fedd6-d6c7-3d43-8669-7e88aed4ddbb | -12.19104 | -47.38875 | 2026-10-01 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e27d451-73f5-3968-8ddb-814c1955805b | -12.03125 | -51.01695 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c89ad14-446c-3162-b1a3-6bf69019ca39 | -13.38545 | -46.81921 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d792c743-4632-3b8d-b162-b6eb4549c08c | -14.14891 | -46.24693 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ac3c442-fd14-35e9-aab2-21362b818637 | -19.83824 | -45.01731 | 2026-10-01 04:17:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec399b39-af9d-379c-980e-bfe7a1f37d6b | -13.3839 | -44.0172 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1384a69-2f63-3101-9f5f-d7ef54e4e2c2 | -13.64575 | -53.94344 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8c9e00d-9f2f-350d-987f-028ff862593c | -14.14683 | -46.23613 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 646db88d-91f7-3094-b36f-5a8d53ef5598 | -17.52593 | -43.73012 | 2026-10-01 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 541ff827-d4c7-3636-a09e-f704c9a2b943 | -17.22338 | -46.84477 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f975cb9-e3ed-361a-bd7d-97955dde97e4 | -13.88359 | -44.4585 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e379897-8a57-349f-b0c6-80c2558e53b3 | -18.58084 | -40.12637 | 2026-10-01 04:17:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae0a4175-fa2d-3512-ab73-23768c7ed9b9 | -13.42901 | -43.81334 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 789bb49a-af10-3e10-a622-850239feb95b | -14.14667 | -51.13966 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ebe4edd-1ac9-35ec-9a8f-17d5c45a1e43 | -14.85524 | -42.15078 | 2026-10-01 04:17:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6dc8e0c-d703-316b-b31e-d1ec7830b2fa | -13.38253 | -44.0253 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d41fb45-7f70-34fa-a221-857ae0a124be | -11.26089 | -54.82166 | 2026-10-01 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1ecc92b-b3d7-3ddd-bdda-2e3138172c59 | -12.86242 | -44.33935 | 2026-10-01 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f1520c8b-b5d9-3e28-b4dd-1e8ea1866819 | -16.02338 | -45.13044 | 2026-10-01 04:17:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4d6073a-6fba-3446-bd2d-d16280c85507 | -12.0886 | -50.69093 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3855f39-b3f5-3269-8684-c6d26cb86b65 | -13.90168 | -43.74886 | 2026-10-01 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README41.md)
