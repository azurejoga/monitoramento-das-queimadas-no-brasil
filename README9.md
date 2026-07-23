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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba6cd911-737d-3ad7-9b1c-62e85bbc0ebc | -12.66463 | -48.21519 | 2026-07-23 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97b1bffb-6911-30fb-820f-1008d0a927ba | -6.49791 | -42.22812 | 2026-07-23 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 957ea838-29c8-3a59-8a85-189f501c0b4a | -9.52047 | -47.12973 | 2026-07-23 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53f7ced3-da58-3ba0-a9db-f9859fb60935 | -13.78063 | -43.18295 | 2026-07-23 03:49:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d07c1c4f-c387-37ef-bb08-568fe941742c | -11.39907 | -47.48088 | 2026-07-23 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01e79531-f43a-3073-a37a-70de7e71ba5e | -7.45138 | -45.97737 | 2026-07-23 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1488a766-eacd-381d-b8d3-543449461e8e | -7.01164 | -45.42657 | 2026-07-23 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e8761a6-6a72-3f0d-8633-43dde3968a73 | -12.67018 | -48.21619 | 2026-07-23 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5024edbc-ccb3-36b1-b02e-81af70f9e4e6 | -11.57063 | -48.40144 | 2026-07-23 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b1984e5-1fee-3c54-99c8-fa1478bffbdb | -5.75893 | -49.08835 | 2026-07-23 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b8f96dc1-699b-376e-a02a-4fdba3ac00a9 | -11.77653 | -47.10209 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d93234ef-11ea-3445-93ec-77d60662d17e | -11.80326 | -47.10402 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ed4e1f4c-be9e-3757-bc76-e7d91d86fc8b | -11.79743 | -47.10626 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b48f9841-cfc4-37fb-9ae4-a330751e4aca | -11.56986 | -48.4055 | 2026-07-23 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f90bac09-ff38-31f7-ad80-a0065d57f3b4 | -12.25366 | -43.57249 | 2026-07-23 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1db8749a-337d-353a-b096-cea357dae563 | -6.49921 | -42.22048 | 2026-07-23 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25aa62ca-14b8-3d44-9c28-477d0b1746fd | -7.01319 | -45.41758 | 2026-07-23 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 409fd6cc-25c9-3f42-878e-891a664aa110 | -11.69545 | -50.36991 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f9ae818f-c6af-344f-9a49-ff86b4ce84bf | -11.70169 | -50.36676 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9a524b13-0ad7-3079-9614-faca482fb12a | -13.43633 | -43.85067 | 2026-07-23 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08f8a5a5-4c04-37fb-b49e-c1e019d07e2b | -11.57127 | -48.4054 | 2026-07-23 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2016ab2d-63ec-330d-a1ce-e16a99089ee7 | -11.80362 | -47.10183 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45925eb6-c1ca-3f69-b9b5-ac191c139c52 | -9.55647 | -40.33567 | 2026-07-23 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a46c81b-ff7a-3a17-a2be-dafe747ad1e5 | -11.70297 | -50.36582 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 922ca399-4ea8-3a3f-ad13-9029a2a6584b | -12.44775 | -49.586 | 2026-07-23 03:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5f61082-c5f0-3fa1-973f-9a88c9d90c1c | -11.77803 | -47.12297 | 2026-07-23 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86159b5c-a863-3801-91ef-c8d8586994d4 | -11.68487 | -50.35652 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 091bbaa5-987b-366c-9ed1-3915b8d8f4c3 | -12.41063 | -50.3952 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 84e85f42-1af6-3b25-95f5-84850ef1c490 | -12.84818 | -44.36466 | 2026-07-23 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c0e0cab-934e-31dd-8353-b4d5e2be30b6 | -11.69656 | -50.36452 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 60de9139-07fa-3c65-8d31-45aa06e32549 | -9.10568 | -49.65469 | 2026-07-23 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aba30bb-fb23-31f2-b85f-cb84f86a1b86 | -11.96496 | -50.36732 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ab014f4-7a51-35ef-af5a-5532ba52604e | -11.91263 | -43.84598 | 2026-07-23 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 46abfb93-b57d-311e-bba2-0efefabceea9 | -11.7081 | -50.36808 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30dee897-235c-3eb6-8ad4-9da182635e49 | -10.66224 | -46.59738 | 2026-07-23 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 504d190e-e398-30b1-a0cc-150d0c96c1ab | -6.4218 | -43.06878 | 2026-07-23 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad9fa992-9fe1-3d29-bf63-7f474f2c89b6 | -11.686 | -50.35112 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2af389d9-fefd-3e38-8c6a-217df6c3f00c | -11.68465 | -50.35197 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d0457eac-bd34-37a1-9fb2-5adaca881779 | -11.39839 | -47.48438 | 2026-07-23 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7918352a-6d6c-3c14-8c8e-2972cead01c7 | -11.7875 | -47.1108 | 2026-07-23 03:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 5eb721da-2ec7-3747-964a-a06ca0018d5e | -11.7879 | -47.0884 | 2026-07-23 03:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 4933c733-4d16-32b5-be7a-f5346eda1d4a | -16.85261 | -49.56083 | 2026-07-23 03:51:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf6bb1c7-d8f9-3bcf-b95f-28e9382b82df | -20.09503 | -44.26179 | 2026-07-23 03:51:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d8b567fa-7570-3767-8250-c815d740b773 | -20.16096 | -43.9205 | 2026-07-23 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6001e104-f7b2-39a9-be34-3c18a1a47a42 | -17.58386 | -47.50359 | 2026-07-23 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70d82a0d-a9c5-3eca-9fe3-4c9ef419ce84 | -21.07139 | -45.94113 | 2026-07-23 03:51:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f192fdc5-1eab-3b3e-889f-01bebf53199d | -17.57906 | -47.50249 | 2026-07-23 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f228be69-9202-3fb3-8fbc-acb8a17a144a | -21.27881 | -45.99264 | 2026-07-23 03:51:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cfef45b9-80c9-3b9e-b054-10185b5f43de | -15.87006 | -41.96466 | 2026-07-23 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 64c6a9e6-73dc-3a07-8e34-70f7ab8cb470 | -17.57315 | -47.50702 | 2026-07-23 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a11ffe95-8bd4-3939-a8ac-e781b53a273e | -15.91269 | -41.94585 | 2026-07-23 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27f6fb9f-1338-3790-8213-a63b4a87aa3d | -14.30407 | -52.08808 | 2026-07-23 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 83ee84df-d4a7-34cb-b1db-be25a3a37ea8 | -20.16466 | -43.92126 | 2026-07-23 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3a94d1d4-a6fe-37e1-b8a2-2f641af07dc5 | -20.16837 | -43.92196 | 2026-07-23 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d006dae9-ebfb-31ee-8deb-dc54312893f8 | -17.57797 | -47.50804 | 2026-07-23 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f8b46ef-2692-34c9-8a48-792eb23fc537 | -19.55757 | -46.9488 | 2026-07-23 03:51:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d5194a1-8ab9-3148-bea5-5d9ea6e1ca0f | -20.99109 | -42.99639 | 2026-07-23 03:51:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dbeb7a25-0e39-3a3d-b0bb-5cfbcb590ab1 | -19.70839 | -48.08314 | 2026-07-23 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cb588851-c749-38f9-a142-2f934b102635 | -21.36859 | -43.76268 | 2026-07-23 03:51:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4bfa39ae-7092-310e-a4ef-0878d9a865e7 | -18.37114 | -39.95558 | 2026-07-23 03:51:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6a3c8542-c089-3a5c-b74e-fab7d7c3ab7c | -20.71331 | -42.8555 | 2026-07-23 03:51:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d646ca13-80b3-3d35-8629-57c7ff433ed6 | -20.99182 | -42.99216 | 2026-07-23 03:51:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e628044e-e822-358c-bc77-b1912753188d | -16.08871 | -45.13741 | 2026-07-23 03:51:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adb534d2-ef55-35cc-a99c-cf89fa579468 | -20.80582 | -40.67054 | 2026-07-23 03:51:00 | NOAA-21 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d5dae79-904b-31db-9a46-49ed8cf04b02 | -15.32334 | -43.72815 | 2026-07-23 03:51:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d807e9ad-c7f5-3d8c-9941-ebbeaa41462a | -19.82087 | -43.83023 | 2026-07-23 03:51:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4715ac4-b7c3-36cd-a3f6-a1a7cbe51d47 | -21.36851 | -43.75978 | 2026-07-23 03:51:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8d09c102-5da5-301a-8c29-64d3700db074 | -14.31082 | -52.08958 | 2026-07-23 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fd1b5b74-d661-33a1-8d78-34c64dc73a42 | -17.74033 | -52.74135 | 2026-07-23 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a43a45a-bfcb-3c06-882c-7095106a5012 | -20.98917 | -42.96568 | 2026-07-23 03:51:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d7eb1c2-274f-325b-9970-457b9d9b103e | -21.07019 | -45.94009 | 2026-07-23 03:51:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 07f72114-e38f-3f31-a0b2-e8e7e6491cc8 | -13.99187 | -49.59375 | 2026-07-23 03:51:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 781f986f-83d1-3ef6-b065-16a75835455f | -21.27806 | -45.99649 | 2026-07-23 03:51:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a24e1cce-3c4f-30f5-8902-7161d0f24c62 | -14.30944 | -52.09593 | 2026-07-23 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c39edfcf-1a8b-3377-afe1-1d709c90e296 | -20.16179 | -43.91589 | 2026-07-23 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4c8cc4a2-918f-3a19-a47f-2edfc76fddaa | -20.44907 | -46.47513 | 2026-07-23 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a92156e-550f-37ad-8977-bbd95cd4e26a | -20.1655 | -43.9166 | 2026-07-23 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fd625816-0afe-36b2-9389-eb246ac31d25 | -21.3694 | -43.75815 | 2026-07-23 03:51:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 35e658a5-1e16-384f-b63a-7f1adf57804e | -19.81923 | -43.82758 | 2026-07-23 03:51:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79c61fce-964b-350a-bd0f-53632588f75e | -20.54627 | -41.72088 | 2026-07-23 03:51:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 205646e9-3710-33fa-b635-f48e9e1e2b70 | -18.80177 | -42.90407 | 2026-07-23 03:51:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 616c11f9-dac5-3114-bafa-f2fb0f5c0aba | -17.56832 | -47.50604 | 2026-07-23 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb178589-bff3-3e88-80cf-222e5af23ffd | -21.01632 | -40.88682 | 2026-07-23 03:51:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 38059098-6a64-3efc-85e4-a076864f7e51 | -17.61713 | -41.99052 | 2026-07-23 03:51:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ec6d15f0-1cce-3fd5-8d61-e160b86f1cf3 | -20.45527 | -46.46624 | 2026-07-23 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58f4cd48-5496-3b29-9b76-ad70bc9d85c7 | -20.16922 | -43.91725 | 2026-07-23 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0c0f72d0-2a81-36d1-bcd9-4b4c9aa3875a | -16.74406 | -47.63541 | 2026-07-23 03:51:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1753b88f-3968-3944-a674-95ff04005d01 | -23.16022 | -45.78515 | 2026-07-23 03:53:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5e4d4d6-2d64-3d82-bf60-29d8b1566595 | -22.28896 | -47.26438 | 2026-07-23 03:53:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed0d4d23-c341-3ec5-8603-e28fa1c2cb4c | -22.29239 | -47.2699 | 2026-07-23 03:53:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b8b0ada-a876-367e-a9cd-14cf223a2fce | -22.28804 | -47.26895 | 2026-07-23 03:53:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1915149a-1835-35d1-8247-0c6558e81d3a | -11.7879 | -47.0884 | 2026-07-23 04:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ba6336a6-eb32-3bcf-a63d-5b92516e5b9d | -11.7875 | -47.1108 | 2026-07-23 04:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f570e675-8513-34da-bb31-53f975f18cbb | -9.5534 | -40.3254 | 2026-07-23 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.9 |
| cb5f2f1f-efbb-3b66-b2f1-5130e4cd49bf | -11.7875 | -47.1108 | 2026-07-23 04:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 771bf852-9ac8-3b1d-881b-8fb63eeb6a7f | -9.553 | -40.3503 | 2026-07-23 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 7fc723ec-70dc-3b88-99ed-ef528e8bcdcb | -11.7879 | -47.0884 | 2026-07-23 04:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| bc903211-49c4-326e-bc7a-e0ce0b56a962 | -19.8624 | -48.1905 | 2026-07-23 04:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 26b1fc34-c771-3ea4-bc4a-24f19987bb0e | -11.7875 | -47.1108 | 2026-07-23 04:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 87ee5be9-653b-3432-b40d-2573108c8cd5 | -11.7879 | -47.0884 | 2026-07-23 04:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |


[Clique aqui para ver as próximas entradas](README10.md)
