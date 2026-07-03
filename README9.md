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
| 3243be0d-3650-3fbb-b545-2f79cd0d54b0 | -17.7161 | -46.78826 | 2026-07-03 04:02:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0bfb5b4-d0b8-3ce3-a146-c0f28329cf7e | -15.69081 | -43.29196 | 2026-07-03 04:02:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df79e2f6-2ed8-3b12-a453-d5662983e4e2 | -20.43137 | -47.55098 | 2026-07-03 04:02:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3867be18-b672-36dc-b0a3-62fbbbfb6e7b | -13.9857 | -47.44941 | 2026-07-03 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdab272b-a723-398b-a606-0486207869b0 | -13.98238 | -47.43939 | 2026-07-03 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee5c77f8-c1cb-3b50-8432-20076c2b2320 | -20.51629 | -44.08493 | 2026-07-03 04:02:00 | NPP-375D | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| be5ab82b-2ec5-3920-b1d1-8dd9291891a9 | -17.71706 | -46.78335 | 2026-07-03 04:02:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d354ad3-eadd-3fb4-94bd-cf4db4e53123 | -17.31329 | -42.65363 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ffaf9e5b-b391-3c48-a03e-f1546472c57e | -20.06012 | -41.86954 | 2026-07-03 04:02:00 | NPP-375D | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f336681-fe28-3231-bf7d-108a6854d8ea | -18.52649 | -47.24346 | 2026-07-03 04:02:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b31de4c0-9669-3ef8-b922-492dc5baa85d | -15.68848 | -43.28936 | 2026-07-03 04:02:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9dad65ab-4996-3854-9361-1808e2991e7b | -15.68764 | -43.29415 | 2026-07-03 04:02:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1228b4f-b103-36d0-a490-2464b859c3fd | -17.26434 | -42.65772 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c31d4dc-77c9-3034-ab4e-c14b8e4799e7 | -17.3097 | -42.65292 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 9fb3a14e-cf8b-38cb-ba9e-cb42b6c9c7ec | -19.84501 | -49.06867 | 2026-07-03 04:02:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d254d63-4db1-3077-b0b5-88055b3d3f91 | -17.31403 | -42.64931 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 43466dc5-6268-3994-9f55-7481ab90953b | -17.30895 | -42.65723 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 029044ed-8325-3a5c-8c28-11efc5ec9be3 | -19.1837 | -42.43825 | 2026-07-03 04:02:00 | NPP-375D | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e79559c9-89a5-30ac-bbab-495276c7bfe0 | -20.23303 | -43.95604 | 2026-07-03 04:02:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ee67686-6270-3d2e-a942-dee4f81db628 | -21.49228 | -48.54105 | 2026-07-03 04:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 710ae766-d109-39c4-8fd6-6fa2640d5294 | -22.79364 | -49.3483 | 2026-07-03 04:04:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b1a2ebc-2299-3503-b03a-77b35fa5450d | -19.51115 | -52.73793 | 2026-07-03 04:04:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee3461bd-3fec-3a30-aacf-db1ad6da5775 | -19.50987 | -52.74351 | 2026-07-03 04:04:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1033bce-9b29-387d-a535-83c990497cd4 | -21.70714 | -47.16496 | 2026-07-03 04:04:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65e2df70-463c-3e35-bc8f-34cafdb27a03 | -22.65218 | -43.26093 | 2026-07-03 04:04:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f6ba1f5e-538e-3dbc-a3a0-81354b30cea4 | -22.65321 | -43.25984 | 2026-07-03 04:04:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d73147d3-4fe7-3d45-9733-498dc58e7870 | -22.85357 | -42.04337 | 2026-07-03 04:04:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b1115b9-fd4a-302a-89d9-3f8a620664c9 | -20.77009 | -48.56978 | 2026-07-03 04:04:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9f9a09e-f190-30d3-b4e9-b0a0ce218cea | -21.10686 | -49.00149 | 2026-07-03 04:04:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 622d0777-3bac-3cf8-8be7-026b4de731d5 | -21.11177 | -49.00257 | 2026-07-03 04:04:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9e8e6cb2-8a6c-3133-9fe3-508e2f09abc6 | -19.51069 | -52.74463 | 2026-07-03 04:04:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 624edfae-bbd2-338c-b000-b7825506a3c8 | -20.76795 | -48.57202 | 2026-07-03 04:04:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2d9f979-bc14-3cdd-9c1e-fc34ad3692e8 | -19.50578 | -52.73714 | 2026-07-03 04:04:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fd029d7-397b-38bc-be8a-2a5f4b117fff | -22.54022 | -46.97186 | 2026-07-03 04:04:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b466c618-abed-34a8-91b7-7d35b5a3ea5a | -22.53602 | -46.9709 | 2026-07-03 04:04:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a20b907-6cb4-35c7-a5eb-a1caa11929fc | -19.51201 | -52.73906 | 2026-07-03 04:04:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4bbc8d9-51c7-3dd3-bbf8-f87ace13ab95 | -21.11121 | -48.9998 | 2026-07-03 04:04:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 14349592-2c5f-3796-a990-94a9741400d7 | -10.9588 | -43.0565 | 2026-07-03 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4d384edd-34af-3ba1-b366-69e64d85da21 | -5.7945 | -45.0586 | 2026-07-03 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 8d3990ac-aab9-3d2f-a92f-3337666575b8 | -10.9401 | -43.0355 | 2026-07-03 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 320.8 |
| 78f1308c-4f02-3ba5-886f-7e824ddbddba | -12.7548 | -44.5428 | 2026-07-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 561dff14-c65e-3ea6-b077-e1ba85845c29 | -12.7746 | -44.5162 | 2026-07-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ce38c361-7e02-3530-91dc-8d4505616750 | -10.9593 | -43.0326 | 2026-07-03 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b23e600f-9bf4-33f4-b165-87ba986c8a92 | -12.7553 | -44.5194 | 2026-07-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 446.8 |
| 9ec36c2f-53f2-344a-9966-9040691c0211 | -12.7557 | -44.4959 | 2026-07-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 6f6daf86-3438-36be-aa95-4c2d2a46da56 | -10.9397 | -43.0593 | 2026-07-03 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 353.4 |
| 308f4b83-b53f-3ccb-8c8b-cb0f8e87850a | -12.7359 | -44.5225 | 2026-07-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 79d68686-b681-3967-a364-e77782f57418 | -6.3977 | -44.84006 | 2026-07-03 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5155649-e203-3896-bf25-d198641888a8 | -9.20484 | -45.32091 | 2026-07-03 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fe6a3f2-a6b4-3d43-b186-aec03dbb5754 | -3.50791 | -38.98397 | 2026-07-03 04:17:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f74522c5-d987-3989-b480-93a3d151757f | -7.61393 | -49.54285 | 2026-07-03 04:17:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3702d6d6-4d90-30f1-bbb9-80e1dc326955 | -7.1769 | -42.95251 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40d39399-e810-3515-91e7-c97c7bd6d331 | -9.1981 | -45.3198 | 2026-07-03 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 132f57f7-b254-3c29-b117-5970afd8a065 | -5.72972 | -51.71487 | 2026-07-03 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5616b615-1d1b-326c-bcab-c0d04a230420 | -2.16209 | -48.2296 | 2026-07-03 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c69ad9ad-b919-384e-8d57-f8a9ff664506 | -6.89712 | -42.85144 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d2fe6095-316b-3658-bdc4-56aac8081d64 | -7.22871 | -43.20568 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5d63845-ffa1-3225-9a50-296db36a0529 | -7.80252 | -47.16088 | 2026-07-03 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dad6842e-9a95-37e2-a148-fdd648d6857e | -6.93055 | -43.71459 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70d64d0e-8524-3b93-8050-391307598e9a | -6.92889 | -43.72499 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07f9dd04-ed21-30b6-a18a-069f62166262 | -9.19473 | -45.31924 | 2026-07-03 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d488a910-e20f-34bf-bcec-d26b8a90519a | -8.73283 | -48.32591 | 2026-07-03 04:17:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67befd03-2ae5-3c7c-8815-8c36d34f37e5 | -3.41782 | -41.71111 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 16e2fcf7-23d3-3e50-a0ef-36fe920ea021 | -6.90097 | -42.8485 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2fe9833-c782-33ad-bdea-178ec837e2ef | -6.9129 | -43.71889 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 30e5163d-722b-3cce-ab32-34ae1162b63c | -7.7288 | -41.06395 | 2026-07-03 04:17:00 | NOAA-20 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| da091580-dcc9-39ec-940e-1dca00123f16 | -7.27375 | -44.50135 | 2026-07-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 583b174c-fe99-36f6-bbff-a8059b494a26 | -7.39679 | -44.43433 | 2026-07-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d73dacf5-b581-3b0c-aa95-ae8d7bb309c8 | -5.72918 | -51.71792 | 2026-07-03 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faffcefe-55a8-3dd7-bf4c-5e55109bd4db | -8.732 | -48.33086 | 2026-07-03 04:17:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a73614cf-48ac-33bf-9166-b44194775ce5 | -3.42159 | -41.70786 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4cde81c-8b33-3b0b-ad41-59beb50a7420 | -6.92724 | -43.71407 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8647199-8034-3cfc-b176-45ba1a98c9fc | -7.18021 | -42.95303 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 695a8f28-8dc4-3549-8e42-d089c14a4751 | -6.92007 | -43.71648 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 446f6c7a-64fb-3daa-beff-4f3dd71cdd92 | -8.38105 | -48.21686 | 2026-07-03 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37ce14bb-8346-3f95-be2f-ae2b2e93cbdf | -9.20147 | -45.32035 | 2026-07-03 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06ccd415-148b-340a-af41-47d0096d9fb6 | -7.01465 | -45.43205 | 2026-07-03 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3e1a66a-3219-32bb-adfd-e6219d7d4e64 | -7.27142 | -46.81518 | 2026-07-03 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ccbc10b-61b3-3f50-af31-3468dfb442e6 | -6.41165 | -51.23211 | 2026-07-03 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf0092c-0b93-3a8b-9559-a3ae1b99d64c | -6.92062 | -43.71301 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfc22e6f-bd10-3c1b-bb55-ede3afe90eb3 | -7.64249 | -50.02819 | 2026-07-03 04:17:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ae3d81f-69ef-302f-b02b-98420a8f9c46 | -7.91989 | -48.25273 | 2026-07-03 04:17:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acc980a2-a456-30c8-b0af-432e2ccf872b | -3.52247 | -42.79077 | 2026-07-03 04:17:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f76a32f3-7f3c-390a-a4f9-d7ec4ceddff3 | -8.388 | -48.22313 | 2026-07-03 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5203b48-91da-3467-9157-d345ecfe48a2 | -6.39712 | -44.84372 | 2026-07-03 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b98970c1-27a8-3f24-bd5d-4f35ac60dff9 | -6.92393 | -43.71354 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c505842-64f9-3be7-a60f-71536d1f8c0f | -6.91621 | -43.71941 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9328161-1b68-3d3b-9daa-3ada92106118 | -6.87915 | -43.65313 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b14a9da9-ebf4-3d8f-b69f-6be8d7b936a0 | -7.27709 | -44.50189 | 2026-07-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3279f7d4-6983-3716-aad4-b18c6def3d55 | -6.90959 | -43.71836 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6dcc555a-b2ec-3772-b212-3714eae9ff1f | -7.91672 | -47.82111 | 2026-07-03 04:17:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebee4777-b143-3dbc-80fc-33865186f6fc | -8.3802 | -48.22183 | 2026-07-03 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7cf39fe-dda1-3f21-8e04-8139a14f019d | -3.41837 | -41.70763 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a306f492-b38d-36ce-9185-8b9c72f0812d | -7.92382 | -48.25341 | 2026-07-03 04:17:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 710bf437-fe47-3221-97fd-f627d98dc7eb | -9.04167 | -47.73528 | 2026-07-03 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5837186c-1b3a-3d92-b8f4-d722ae09d5d9 | -8.0491 | -46.71139 | 2026-07-03 04:17:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ccca030-cf6a-30f6-9c44-23fc069139b8 | -2.16379 | -48.23059 | 2026-07-03 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a22706e-a3b7-3eed-96df-7b1dfa5f30ca | -9.15891 | -47.23582 | 2026-07-03 04:17:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14406f16-425a-375c-9423-c6a149b244a2 | -3.87011 | -42.97591 | 2026-07-03 04:17:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6074aebf-22ab-35e3-82dd-b834269bf44a | -6.92338 | -43.71701 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README10.md)
