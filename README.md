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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2216957-51a0-3c73-ad28-561d5995463c | -7.1482 | -60.1366 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 38d7652b-eea5-3e00-8ee6-d8dfef5a2fc9 | -6.0992 | -59.9267 | 2025-08-13 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| dedb6b91-d26c-3218-9310-04558adb6501 | -18.5303 | -46.0414 | 2025-08-13 00:00:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 76b167f7-4b0c-3340-831f-65272c4b01e9 | -9.0521 | -60.6466 | 2025-08-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 512d7978-4f4a-31d1-8ddb-57715d234019 | -12.5361 | -46.9837 | 2025-08-13 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0699ce5e-fcee-3f91-b10b-709189fde964 | -7.0934 | -60.0429 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a18a0217-b7ac-304b-9209-e7baa0a20e5b | -7.0935 | -60.0237 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.9 |
| a9d9fb47-b13c-3383-9ba0-85435ffade98 | -9.052 | -60.6658 | 2025-08-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9db62b80-179a-3269-9e9d-e10139588cea | -15.0787 | -51.364 | 2025-08-13 00:00:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| e4c68a8c-34cb-3c87-9fea-b9c2f1d70067 | -7.1299 | -60.1182 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 1dc12236-b52f-32d5-b3d2-7cf248b225e4 | -18.6301 | -43.9106 | 2025-08-13 00:00:00 | GOES-19 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 157b87b0-284d-3e3b-9a6d-55a67d8bad6f | -7.2746 | -60.6294 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 820d759c-2dd2-3c3e-9a21-308cb16121ee | -9.208 | -59.6548 | 2025-08-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7c0a18a8-d5a6-388f-9e79-c1383ac4f608 | -9.1894 | -59.6558 | 2025-08-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f521e542-7570-305d-bc7c-c325f399b000 | -10.9689 | -49.5856 | 2025-08-13 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| d09d8150-fe0a-3bc5-ae35-67e4bf900af1 | -8.1247 | -55.549 | 2025-08-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| e2d3969c-3eae-3908-a04a-aa61fd668aa0 | -11.7695 | -48.2021 | 2025-08-13 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3e036104-2878-3452-950f-18d16d8a6d4d | -8.106 | -55.5701 | 2025-08-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| ad5d9bf9-edbd-3bbd-b8cc-b52d2abd7294 | -10.9693 | -49.5639 | 2025-08-13 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ce477126-ede7-353c-8d84-fdb70516d01c | -7.1298 | -60.1374 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 07c46753-f10e-35b5-a0d4-a9428b48e5f4 | -7.2562 | -60.6302 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| df8acf5e-3315-300a-8fac-6163307d3c7f | -22.4079 | -45.4657 | 2025-08-13 00:00:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| c17176bb-8ad0-38fc-b70c-d0436deea524 | -15.5681 | -43.1595 | 2025-08-13 00:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 8279e076-bea4-3e4d-80df-c5928d3c84e3 | -9.0707 | -60.6457 | 2025-08-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 2db066d6-48cf-356f-9203-ec290957c43f | -11.7699 | -48.18 | 2025-08-13 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 4cbb5e75-5e90-3262-a76e-4a5278fb3a23 | -7.1483 | -60.1174 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| dcfb5991-2e8c-3b95-86ea-bf4d24aa8bae | -6.0991 | -59.9459 | 2025-08-13 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 7eec6dd0-2b18-3aed-a3de-eaccc65fcae3 | -11.7177 | -51.6159 | 2025-08-13 00:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 264157e0-0963-3f09-8818-6e789ec4977d | -9.723 | -49.4806 | 2025-08-13 00:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9ff1dd1f-8b60-3a48-8b55-9dd78cfcbca5 | -12.3229 | -46.0409 | 2025-08-13 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 354a734e-d89d-3e47-b2b8-ce4e8fd1ff55 | -15.0981 | -51.3612 | 2025-08-13 00:00:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a9c2850e-6e24-36e7-aa73-610a2100a419 | -8.1061 | -55.5501 | 2025-08-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 7f5f1a43-63e5-3ca0-a6b5-a578f4225978 | -11.7504 | -48.2046 | 2025-08-13 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| df0f8a09-f41b-37a4-ad06-d6e05b0f7a6b | -11.7508 | -48.1825 | 2025-08-13 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4ebaa9c2-23d7-3d0d-b706-d004e25a5b7c | -9.1892 | -59.6752 | 2025-08-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 656e5cae-1270-31c2-bcbd-6a9ef3424487 | -22.3877 | -45.447 | 2025-08-13 00:00:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 562deb0c-c6c1-319d-9a94-de3d4697a238 | -15.0985 | -51.3396 | 2025-08-13 00:00:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 84f58249-b157-3c01-b101-d8f714e40b95 | -8.1246 | -55.569 | 2025-08-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 198.9 |
| c21a0b61-2763-3857-bc75-c7ffebe49bb9 | -12.3225 | -46.0638 | 2025-08-13 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ea9b5b29-2323-35b8-9de5-3a73309310c5 | -10.2415 | -50.2215 | 2025-08-13 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 9dc7dc6a-4c0a-3b94-83dd-658f82514f77 | -7.4636 | -59.8931 | 2025-08-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a4b28527-ba79-3b11-a350-b6cafe588e08 | -15.5687 | -43.1351 | 2025-08-13 00:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 63.7 |
| b54af1bd-754c-3473-b85e-c9b2ef67e374 | -22.3869 | -45.4716 | 2025-08-13 00:00:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.5 |
| 1e409e77-0f2e-319b-af83-580875d8b942 | -22.38614 | -45.47279 | 2025-08-13 00:05:00 | TERRA_M-M | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 198.6 |
| 3ec5cea5-9bf4-352a-8eb0-c5a25318c6a2 | -20.98982 | -43.26565 | 2025-08-13 00:05:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| e5a560ee-013a-3ca4-81b0-b41a5f0ada07 | -13.76968 | -42.62119 | 2025-08-13 00:07:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 492f89e5-d981-3afd-98cd-938b6aac27af | -18.45458 | -44.45251 | 2025-08-13 00:07:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 313cd568-8843-3e7d-b2d6-b27022e87e25 | -16.60204 | -47.04153 | 2025-08-13 00:07:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| b86499b4-9e0f-34bd-a090-796fc57b0c97 | -15.70208 | -41.94216 | 2025-08-13 00:07:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 141cb3f0-b545-3969-9bda-f1aa9f97c240 | -18.54006 | -46.07045 | 2025-08-13 00:07:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| cb5d615e-1337-305c-8379-6af68ee4f36b | -14.11802 | -44.31078 | 2025-08-13 00:07:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 239dbd57-5149-38fc-a11f-c660100e951d | -14.71637 | -42.49349 | 2025-08-13 00:07:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9abad3ef-694b-3327-9aed-55ab8957af81 | -15.55338 | -43.15047 | 2025-08-13 00:07:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 47a56a7a-0245-3d5d-abbb-b9848304c65d | -15.55477 | -43.16156 | 2025-08-13 00:07:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 87.2 |
| fb008042-b72b-325c-9f25-1a26b432bf8e | -18.53792 | -46.05016 | 2025-08-13 00:07:00 | TERRA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 119.3 |
| e972bb45-ac69-3909-b6c1-1421a70d30a0 | -14.11954 | -44.32334 | 2025-08-13 00:07:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 62c6280d-b12d-3548-9daa-828c49f18cf1 | -13.43988 | -44.50002 | 2025-08-13 00:07:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 0cc7fdb3-f12e-3f87-af1d-ad1f73662fd7 | -13.44144 | -44.51255 | 2025-08-13 00:07:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| caffbdd2-182c-36b6-af93-c3e475cf141c | -7.05812 | -44.36275 | 2025-08-13 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ce4bbd2e-cfb0-300c-bcfb-bc3232ebb10e | -11.87957 | -46.8116 | 2025-08-13 00:09:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 551f9e21-69a1-3715-acd8-b2897c91b195 | -4.23097 | -47.22683 | 2025-08-13 00:09:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 73d3e242-53eb-3656-b1dd-d4956337606e | -11.98595 | -45.15939 | 2025-08-13 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 79ab93d6-ba29-383a-9de5-b9c85b3227d9 | -6.4504 | -44.56089 | 2025-08-13 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f5f55aa8-910c-3dba-b7d6-00266d905b89 | -6.12239 | -44.71445 | 2025-08-13 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f19fd59d-7141-352f-b986-778d154d84fd | -12.69165 | -46.97421 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6c10485f-537b-3b6b-9be0-5ee4f251ac3a | -11.99658 | -45.15801 | 2025-08-13 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 378175eb-6df5-3bc8-a3b2-502f9cce57d7 | -7.48848 | -43.92828 | 2025-08-13 00:09:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b7e1f1b3-49f4-3b4f-8f4a-7244e90df625 | -12.31742 | -46.06766 | 2025-08-13 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 584f938d-3246-3e6f-9039-b643ec467b85 | -6.60595 | -42.78682 | 2025-08-13 00:09:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 665ebbb1-1a14-32ee-a65c-01b88e2eb8ab | -4.2291 | -47.21269 | 2025-08-13 00:09:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 41.1 |
| af77eebe-f418-3b30-931f-0fef91844657 | -10.96878 | -49.56932 | 2025-08-13 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f0b5b996-c4b1-39cf-8293-456bf6e2005b | -11.72285 | -51.61105 | 2025-08-13 00:09:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b61c2728-48fc-3338-84ab-f00ba443f9fe | -4.77302 | -45.32822 | 2025-08-13 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a23ef2b6-b7b9-32c1-8480-5024c59854bd | -4.9567 | -47.59876 | 2025-08-13 00:09:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 920d3138-20d1-3bc3-bd8c-65ce95c3ea46 | -12.57546 | -46.97621 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 783ab56a-568c-3eda-991c-0f45b5706ffa | -10.97146 | -49.59084 | 2025-08-13 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 00cd5f1f-0dca-3808-8576-804df6f37530 | -5.44355 | -43.57743 | 2025-08-13 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| abb409c8-8cfe-3bc3-ab55-e6828efd3ae2 | -10.18963 | -49.51916 | 2025-08-13 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ed9444d1-b744-3963-b0fc-cd95d0707ec6 | -10.74068 | -48.18542 | 2025-08-13 00:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8245a79c-c171-38b4-a154-5c0d75b15721 | -5.18604 | -37.66763 | 2025-08-13 00:09:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 48daca28-d803-3462-aa59-d29db6250da7 | -5.82752 | -44.03176 | 2025-08-13 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1dd3598a-7c01-3a90-a76d-6e1decc174c7 | -10.24233 | -50.21136 | 2025-08-13 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 485f51b7-0b69-337c-b36d-0c0b4ca5eeeb | -5.32338 | -45.22123 | 2025-08-13 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 68751024-3abc-34c7-a62d-8f519de8622e | -8.38211 | -49.35815 | 2025-08-13 00:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| a0b6385f-c44e-3ff4-b5a2-76c8447189d1 | -9.7173 | -49.49756 | 2025-08-13 00:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 61c158bc-bd9c-398a-82db-9ff690b4ccde | -5.25859 | -36.16678 | 2025-08-13 00:09:00 | TERRA_M-M | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 8f996ebc-32d5-379e-a75a-867a9d641242 | -7.72704 | -42.1679 | 2025-08-13 00:09:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| abdbb486-ebb9-300f-86f9-9fbdb12bab71 | -9.36557 | -40.70567 | 2025-08-13 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5d8fdb83-4c2d-3a9c-9a66-8d21847075b2 | -9.37578 | -40.71346 | 2025-08-13 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1416cac5-b93c-3574-9ecd-92bad8ec4f4e | -10.24595 | -50.24209 | 2025-08-13 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 8fcde2e6-f5cc-32de-ba6e-beaeb00c92e9 | -9.71608 | -49.46458 | 2025-08-13 00:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 45e65a5c-bf77-3d77-9dba-9a053f580005 | -11.76682 | -48.19026 | 2025-08-13 00:09:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 334.7 |
| 78796008-32e7-3082-b7ad-94039f7e2eab | -6.55252 | -44.01941 | 2025-08-13 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee103ffd-8f9f-3957-9e29-6442621ca02f | -12.68181 | -46.96922 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ba090dae-689a-3ec3-82be-fa6edbae6963 | -5.18379 | -37.65273 | 2025-08-13 00:09:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 00364732-e870-36e8-bf60-11dfa54d53cf | -12.57762 | -46.99422 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| fa976548-f82a-32e7-b0db-1f8af2283a23 | -9.36685 | -40.71478 | 2025-08-13 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 39ec0f9d-7c3a-3705-ba9a-92d2e16958c8 | -12.30403 | -46.05369 | 2025-08-13 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 4846359f-393c-3974-bbd4-b8f41b3597a5 | -10.08666 | -50.32981 | 2025-08-13 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 36e82456-5f9c-3456-a447-0980c5e5724b | -5.45127 | -43.56703 | 2025-08-13 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README2.md)
