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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51b4cf11-18c7-37b4-a8cb-7187ba161cab | -11.23798 | -43.35658 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e1619f84-f574-3ac6-8ecf-33a764c29f79 | -17.79747 | -44.57591 | 2026-06-24 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4858a60-21ea-3113-87f0-bec9b2a953dc | -11.28855 | -43.31314 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45ca778c-2df3-32e1-9d41-3bfc9f354aa4 | -9.44075 | -48.86839 | 2026-06-24 03:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a92fce2-a692-3aa7-963f-7156a2edfb09 | -19.21848 | -42.05785 | 2026-06-24 03:49:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2e49fecf-d78a-32db-9a56-0bad57aa4f17 | -10.11242 | -47.54995 | 2026-06-24 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 050effa9-a2c8-3056-b722-558e3404956f | -10.69335 | -49.61565 | 2026-06-24 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21b75300-eba8-3cf1-8915-40bfc359d24c | -11.25695 | -43.33182 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54894ec8-5d74-351e-bdeb-03ffdbb7aa05 | -11.24709 | -43.35825 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6a309169-2391-39a9-aa41-3fc53fef0261 | -11.30556 | -43.32273 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9a607974-5367-3a03-a38f-9f37d7a30f06 | -10.11151 | -47.55463 | 2026-06-24 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00aab3e1-4e98-3a29-bd19-1b028782191b | -11.2417 | -43.36208 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0b476007-173a-3bc2-92ca-224b6e6975e2 | -11.23784 | -43.35864 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 09ea41b7-8e30-3407-9c85-e4b86d5344f8 | -10.63175 | -44.85221 | 2026-06-24 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c937005-0d40-316e-b084-edcdd896a969 | -11.7913 | -42.63726 | 2026-06-24 03:49:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f544c540-2706-307e-9ace-a88bc8f6bd5a | -11.30923 | -43.32837 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8e776108-8738-38b2-820e-819742cf4759 | -17.61225 | -46.69479 | 2026-06-24 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a153c48b-30f4-35ff-acd3-0615adc39318 | -11.29565 | -43.32563 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d534b2e7-6ce1-354b-a68b-97d26e01fc44 | -10.69468 | -49.60928 | 2026-06-24 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1b0d6c7-585c-31c0-bd2d-87917cbba2de | -11.30017 | -43.32657 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 42a5ac39-595b-3532-8434-57a6204dc6ee | -19.22097 | -42.0564 | 2026-06-24 03:49:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| efda6275-0e07-3af2-9f98-d89c89ecccd6 | -11.47966 | -46.73282 | 2026-06-24 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20155bc7-48ad-3e21-9dd6-961bedea30a5 | -11.4789 | -46.73682 | 2026-06-24 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c19f8ab4-5969-393c-acdf-dcdb9fd00f6f | -11.48382 | -46.74181 | 2026-06-24 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d434863-34ae-3700-83ad-e8ed43c56f30 | -11.9051 | -43.40386 | 2026-06-24 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 353e2a49-923d-30d8-9684-43adf7b239ef | -11.95863 | -37.97889 | 2026-06-24 03:49:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b8f8167f-b1aa-35cb-b219-c01348ea1416 | -11.90961 | -43.40473 | 2026-06-24 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fed1375f-9960-3bd6-8b8b-39be78ed610c | -6.3703 | -43.5898 | 2026-06-24 03:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 4b344391-5a52-3824-a375-19e090e2ae06 | -12.8359 | -44.3422 | 2026-06-24 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 260.9 |
| 0a3fde12-5569-3032-8924-d0e82a469486 | -12.8548 | -44.3625 | 2026-06-24 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 292.9 |
| 027bb97a-ea1d-3cd9-8eda-7b598372208d | -12.8552 | -44.3389 | 2026-06-24 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| a6fd2da0-cc61-3dce-90c9-a1a9e53f1605 | -12.8354 | -44.3657 | 2026-06-24 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 546.0 |
| a72a8754-2336-3e45-ae7b-2508a626bd56 | -12.8543 | -44.386 | 2026-06-24 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 0a450070-b383-3301-ba05-0a8abc8e788d | -12.8354 | -44.3657 | 2026-06-24 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 478.8 |
| 8e25e7ac-427e-3dba-a43e-963c1cb27bff | -12.8349 | -44.3892 | 2026-06-24 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 6d8d8472-5ee7-3eca-9308-dac0ba097135 | -13.0635 | -53.3546 | 2026-06-24 04:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c1131b82-a71f-3ae6-b090-4627807b0a99 | -12.8552 | -44.3389 | 2026-06-24 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| e7d4cac3-06ee-3077-9fb4-e755534af5f8 | -12.8548 | -44.3625 | 2026-06-24 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 269.6 |
| d0e312bd-d734-3d29-b1b8-e2fc539517ce | -12.8359 | -44.3422 | 2026-06-24 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 234.6 |
| f1b43124-2ec7-3f53-8381-c27c34493254 | -13.0635 | -53.3546 | 2026-06-24 04:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2705a0de-1e5f-34b9-93c0-823188c24fd9 | -12.8349 | -44.3892 | 2026-06-24 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b0468cc8-2cef-328e-842a-90347cf37bb3 | -13.0635 | -53.3546 | 2026-06-24 04:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 8fa80a40-afb4-3277-995d-7dc8356ef8d9 | -12.8354 | -44.3657 | 2026-06-24 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 475.8 |
| 23d72f98-d7e9-344f-bda6-e3cda37f89e5 | -6.3703 | -43.5898 | 2026-06-24 04:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 4779c4de-01c9-3098-a1e0-7ee5c744214e | -12.8552 | -44.3389 | 2026-06-24 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d85ce164-a2e2-3f60-8c5d-af9a60b67530 | -12.8359 | -44.3422 | 2026-06-24 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 4eb7b654-b276-3d10-9134-fc1f1900e2e0 | -12.8543 | -44.386 | 2026-06-24 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| be2b8357-637f-32cc-9597-6b4c4b8fff0f | -12.8548 | -44.3625 | 2026-06-24 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 310.7 |
| cddfc78d-d5e0-3409-b282-1aa9f0400486 | -13.0827 | -53.3524 | 2026-06-24 04:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2d7f4c0d-903e-3061-8eb3-be8d172999d1 | -12.8552 | -44.3389 | 2026-06-24 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 003d579a-4ed0-386a-abcb-15bf64a9f5d9 | -13.0635 | -53.3546 | 2026-06-24 04:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b7ec11c1-b923-36e3-8cff-dbfd0e9b15b0 | -12.8354 | -44.3657 | 2026-06-24 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 430.2 |
| b09a4f27-cbdb-3455-808f-9d8403e0e2e4 | -12.8349 | -44.3892 | 2026-06-24 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 9b015704-5e13-30a1-8407-931e64b4ece4 | -12.8359 | -44.3422 | 2026-06-24 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| f5ebe6a4-6add-33ef-a31e-589698da637f | -13.0827 | -53.3524 | 2026-06-24 04:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 3efb58fe-3a02-3bcc-97ec-c2133fb16017 | -12.8548 | -44.3625 | 2026-06-24 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 263.5 |
| 09c2c78c-3bce-3f76-a269-2b7d06821160 | -6.99893 | -42.77716 | 2026-06-24 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fa06e24c-30cd-353a-91ae-e72a3c50f42d | -4.4542 | -48.022 | 2026-06-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48818d7e-5086-3305-ba81-ef5a3356bff5 | -6.99392 | -42.89526 | 2026-06-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| c8f89e91-b1d3-33ef-9e02-52f4d6291b22 | -4.34081 | -48.96283 | 2026-06-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc957157-5c95-3126-a432-12d1b4f3f78c | -7.36517 | -47.02818 | 2026-06-24 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe1016b4-c5dc-3c6b-bd1c-aa55bde138e6 | -5.30435 | -43.05742 | 2026-06-24 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc16b0bd-8175-3322-8eb8-6f436085bd8f | -7.2893 | -46.2532 | 2026-06-24 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fa6723f-c169-3781-a30f-9f85c6606cc8 | -7.37454 | -42.80204 | 2026-06-24 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3292bac3-afc5-3785-a70a-6e5c962fbc95 | -7.36462 | -47.03168 | 2026-06-24 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94f2d1d4-66ca-3738-b344-6dc7f78e5dcc | -3.87334 | -42.96435 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9020d126-5c22-3f05-bf7c-ed4e1b68c505 | -6.36775 | -43.59182 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31911516-e875-36c2-a813-a1096c559b9c | -6.84152 | -47.86198 | 2026-06-24 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf75a61d-431a-3b35-a3c6-82e8d6e99abb | -6.84098 | -47.86543 | 2026-06-24 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d494133b-e258-3c4a-9529-e510868004e7 | -3.9628 | -43.11826 | 2026-06-24 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9be536ef-35dd-3370-88b1-e28b93392a7c | -7.29716 | -46.24694 | 2026-06-24 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 76a445db-bc03-3440-a9ce-fa5988a6ab03 | -7.29433 | -46.24276 | 2026-06-24 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78863beb-ebfd-394f-a4ad-fb5347ad1f80 | -5.30822 | -43.05799 | 2026-06-24 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 131496f3-d487-3c8e-aeec-e8579d0986c0 | -1.59299 | -50.44069 | 2026-06-24 04:32:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b023da04-2b59-3f84-91ba-ac41af10c03f | -6.37088 | -43.597 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6bd71bcb-2c23-37bb-a6e3-34f66a6064d9 | -6.60213 | -45.97013 | 2026-06-24 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be7b55bc-134c-3443-9722-a5225a14fed7 | -7.17594 | -48.22259 | 2026-06-24 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f514a728-2282-32bd-a06b-57684ebd9c20 | -4.65575 | -43.12245 | 2026-06-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8df992a1-c57c-3601-9251-4f9a7c6c58cb | -4.66338 | -43.12362 | 2026-06-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bcb5972-ef9f-3ee1-9fe1-b8215387fd08 | -6.37208 | -43.5897 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c8c9d015-ed69-3f23-b089-18f894e31c53 | -6.25768 | -49.8812 | 2026-06-24 04:32:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2635a1cf-f1d8-3e53-a129-84a7387fc7be | -6.36686 | -43.59855 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c31b374f-f2c6-39d8-adad-28d66aec6532 | -6.84495 | -47.90488 | 2026-06-24 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1aa54183-f861-3a8c-a4a3-a07fc04b4f00 | -4.45089 | -48.02149 | 2026-06-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4511bfc6-4825-3fc0-9f14-dcf0d7967ddc | -6.99645 | -42.76597 | 2026-06-24 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 669508eb-ae2f-3eb5-bf2d-a5a9dd4c4259 | -4.35229 | -47.76109 | 2026-06-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a255fd97-6257-3f56-95dd-7d426145e660 | -6.84428 | -47.86594 | 2026-06-24 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9d45c44-e3ba-30f2-8926-c81b4b86ff9a | -6.36827 | -43.58918 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6fd07e7-30ba-3a6c-815b-33d52f3336f2 | -7.04196 | -46.51841 | 2026-06-24 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75a3ff03-e07b-3055-84d6-abb436e8852e | -6.8399 | -47.87232 | 2026-06-24 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d6f332-b995-38d1-8860-9f4d92cd5471 | -6.9894 | -42.8982 | 2026-06-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0dbaf5ac-06bb-34e1-a298-06ebad1847ad | -6.36757 | -43.59387 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47c60ac1-584f-33ca-8b2c-563324c0df8d | -6.56315 | -45.78717 | 2026-06-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5293c6b1-6dfd-3ca3-8bab-265b50c47431 | -7.29095 | -46.24224 | 2026-06-24 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b276a769-6de2-38e7-9499-69a791193814 | -6.37223 | -43.58766 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d371aa3b-3078-3dc2-ace0-d56ea027ee3b | -6.37518 | -43.59488 | 2026-06-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ec337587-a5c6-3ee8-be0b-99278df949ce | -6.99443 | -42.89177 | 2026-06-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0ba263a5-a9b4-310a-87ff-8822c63bad4a | -6.84811 | -47.86301 | 2026-06-24 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baa408d5-c9e8-31c4-801c-d26b4c66c3b8 | -4.08492 | -47.31762 | 2026-06-24 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4aa68de6-77d5-38c8-bd38-1de98d10ffc7 | -4.65956 | -43.12303 | 2026-06-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README11.md)
