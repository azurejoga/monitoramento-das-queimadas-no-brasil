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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5717ed3-2e07-31c1-9bd6-5dba64fd062d | -17.30927 | -41.83524 | 2026-10-01 04:17:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85a76e1e-ccff-3946-98f8-7ed0388fc932 | -17.845 | -42.21936 | 2026-10-01 04:17:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e0a5e64-7a33-3fc2-8d3e-94a612ea6940 | -14.87152 | -51.85969 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64ecb8b3-c46c-3e43-a66d-4dde6e04f2eb | -14.41851 | -51.31826 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 26f3f600-971c-337d-bba2-a79ce17a7cb5 | -13.96126 | -43.97548 | 2026-10-01 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60203e2b-dd99-3525-bb32-924372d6fb73 | -15.95253 | -41.89245 | 2026-10-01 04:17:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de81c4bd-789f-3e61-abc6-b983d024c7e1 | -23.00272 | -48.61942 | 2026-10-01 04:17:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26ace22f-7b9a-32b2-bacb-b93d86f4ad76 | -15.85571 | -41.71043 | 2026-10-01 04:17:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 689d9c8d-4a35-39a2-a319-85d7d958312d | -11.81892 | -50.52808 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 469dc09f-d14b-3fae-934c-3036713b7251 | -13.53255 | -49.19389 | 2026-10-01 04:17:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3ac36c3-113e-3279-9bc0-74c62bd35a39 | -17.91427 | -45.04293 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55ac4124-5419-379f-9761-b27e90c3f7a0 | -18.58437 | -40.12692 | 2026-10-01 04:17:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9569a051-cb29-32db-9675-3942019d677a | -14.40367 | -51.25346 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a72e89e0-6acb-3587-93a2-1bbb9330994e | -13.38282 | -46.83353 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d686aad6-7054-3dd6-9fe9-475c197d8f94 | -14.36747 | -44.77982 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 610ea37d-6a34-3a5e-bb9a-15760891af02 | -16.42575 | -47.18745 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d0731ad0-5977-3c9e-89f8-7f9d2f5b559d | -11.82492 | -50.52575 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92673eee-f28f-3975-9e69-c60f922e80b1 | -12.37376 | -51.14534 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f79a266c-5bb2-3404-a0b7-e37057460420 | -13.77831 | -43.22682 | 2026-10-01 04:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a4322a78-e951-342f-8ed6-322fb6bc51fc | -16.18003 | -42.87841 | 2026-10-01 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b5ba99c-9ed7-3968-9e7e-3a2015da64ae | -14.13806 | -51.12709 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19da8c09-2ffc-3e50-a357-8bba31daca5c | -12.09466 | -50.68854 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eecc3ff-3ee7-33dd-a76b-b6cf9a6a637b | -11.83092 | -50.52341 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f1d88a4-96e3-3316-9295-41e340ddaa62 | -15.95586 | -41.89301 | 2026-10-01 04:17:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a20ff4c-a35c-3303-b406-00f2728cbc4a | -20.10233 | -41.43813 | 2026-10-01 04:17:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7cffcd65-6aa6-3c76-add6-66f27466ff75 | -16.11723 | -42.2193 | 2026-10-01 04:17:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a68348df-8e2d-31f0-9e5a-7ea470ef4ee6 | -14.43645 | -51.25688 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7d5de11-8c16-31d0-b3a8-0cebef08cdfe | -13.5245 | -46.88411 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 463b0cb5-01f2-3536-a94a-053b887ba6cd | -19.34113 | -41.45029 | 2026-10-01 04:17:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 88c6f1a0-66ef-36d8-8137-05d1c1f2f15e | -13.10897 | -51.21856 | 2026-10-01 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22c0e34c-fdf7-34d6-ba50-861025e7aa5e | -15.64016 | -40.99144 | 2026-10-01 04:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 11f7db94-11f3-314a-bd1e-0b6b380e89c3 | -14.14577 | -46.24483 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 118b4962-3861-3294-9835-8f0b78f29abf | -12.6427 | -47.63491 | 2026-10-01 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 111f8e49-1631-33e9-84d4-02be836d46a9 | -13.66088 | -53.93516 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 192ec8cc-985c-3a32-a40f-0f5d38e89706 | -16.43371 | -47.18894 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3e6e301-2383-3689-9a26-ed149afe6833 | -16.13622 | -43.73991 | 2026-10-01 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c441e9e4-f12e-39d1-a792-9b87b96d5685 | -11.73895 | -50.40934 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c292aa14-7a01-3ec0-809e-6a87c4518f73 | -11.74326 | -50.40324 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b9b38ad-85df-3ae0-9153-194387ceee35 | -10.77431 | -54.75586 | 2026-10-01 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d97ec23-e440-3614-81ad-69a5fcaba552 | -11.79074 | -50.50101 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 79259d75-1d09-36b6-8d90-c1dfae4d44b6 | -12.31227 | -50.28694 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd12c55b-f1c0-3f87-a244-13f12ac6dc59 | -13.32348 | -43.47704 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 456b77a6-a97e-3f65-87c5-50f65559eac5 | -15.85514 | -41.71404 | 2026-10-01 04:17:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 47a1e0a9-2732-3094-ac69-636d69f0a710 | -15.84961 | -41.70571 | 2026-10-01 04:17:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 45985f9c-f14c-318d-93be-9e45d7beddc9 | -17.90146 | -44.32935 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 253b8841-0098-3370-b204-51598e38e526 | -14.87627 | -51.86463 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a05ff20-88e4-3e82-b3cf-efe5ae25b53f | -13.38293 | -46.81937 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1d105541-aad4-3140-9c4e-35a3420518e3 | -11.79008 | -50.50443 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9c9b9513-f5ed-3d7e-a193-d6e0564d86d6 | -11.79478 | -50.50893 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ad802ca5-ee4a-30fc-888b-6046cba2c740 | -12.18453 | -48.4386 | 2026-10-01 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 23a284c1-0a6f-3d42-8620-4f35bac56217 | -15.89302 | -38.88329 | 2026-10-01 04:17:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 935d2f88-4313-3a3d-b656-ffdc3d0dfc26 | -16.02697 | -45.13111 | 2026-10-01 04:17:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f2820ab-d32c-3116-9f53-1dc695f7ab19 | -13.87174 | -43.99329 | 2026-10-01 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d30bc2e1-537e-3c4e-ae55-a29f0a2681eb | -16.18672 | -42.87952 | 2026-10-01 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a73f307-d343-3462-aab7-a9b69528a0bf | -12.62576 | -47.85235 | 2026-10-01 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63facfbf-a73b-3053-9560-8e386e51aae8 | -14.41921 | -51.31478 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ad1b726a-95a1-39b6-a117-c81faa874de9 | -18.06873 | -44.51983 | 2026-10-01 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 46c99705-864f-340d-bc8c-2688913e7aaf | -15.16357 | -46.12334 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1d8ab6f-8c39-3fb6-866d-7725b897466b | -13.65336 | -53.93911 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a1d4519e-50c8-3793-84b1-b0146bfdfe36 | -15.23514 | -46.14167 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec5f61d8-e374-3b0f-bc62-78b3f63d127f | -13.97293 | -38.95188 | 2026-10-01 04:17:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e9e667d1-96f1-33f0-8c9c-06b1d30db96d | -14.40226 | -51.26037 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 342aec61-bfc4-3805-9a47-7c8d2d42ed19 | -14.39945 | -51.27423 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 945aa809-1291-3e5f-995b-9d1e08d3b010 | -13.66667 | -44.30839 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02a0bacf-d67f-3a94-ab1f-57cad7490bd5 | -14.4862 | -48.30366 | 2026-10-01 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd039132-0582-3969-974b-53f9eb0cbdd5 | -14.90728 | -47.73766 | 2026-10-01 04:17:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1591e199-b6ad-3f68-9e0b-d0a72e0d71e3 | -13.32229 | -43.82393 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e4927c0-598d-3b60-a17f-9b21f6930da2 | -14.88351 | -51.88573 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc50a925-ab89-36ac-8687-1b618dfd8d30 | -14.73833 | -47.13606 | 2026-10-01 04:17:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b3cee33-369c-381f-a20d-ba52ff62412f | -17.88017 | -44.30954 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 992d4913-8745-3bcc-9898-73f772419b9a | -16.16508 | -42.86462 | 2026-10-01 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 585e226a-b4fb-3f92-91c3-e5c2024e7a89 | -12.70775 | -54.0676 | 2026-10-01 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c715501a-6831-314f-8a3b-a0e603fe1d1a | -13.36343 | -46.83401 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90f20640-421c-3789-90cc-b4a9740b2cf0 | -16.90215 | -42.1027 | 2026-10-01 04:17:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 547bda61-ea51-312c-a83b-009d6e8d2d1e | -13.38912 | -46.83215 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c47aecef-02c7-37dd-b92e-fe44fa79b0b8 | -10.7781 | -54.75502 | 2026-10-01 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9781914-ddab-3c4e-98dd-42fbe6b6d8fa | -13.54238 | -49.16817 | 2026-10-01 04:17:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3251400c-1e0f-325b-8546-0ffa8cca4c12 | -14.3872 | -51.29714 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e8abf359-ce5f-3634-8cf6-4ba8c1315164 | -18.27637 | -42.18345 | 2026-10-01 04:17:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4200e71c-7069-3916-9da2-44fc87523310 | -14.62176 | -42.53244 | 2026-10-01 04:17:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc90bb58-6c92-350a-9f16-b38b93e9799a | -17.97969 | -41.73937 | 2026-10-01 04:17:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c0fa040b-33b3-3634-92a7-521bde866ef7 | -16.30872 | -43.62803 | 2026-10-01 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e87f60a-a297-3f54-88ce-31e57b5f3fb4 | -13.38759 | -46.81689 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcb92c6d-a4be-3bc3-a60f-f5c39e7975bd | -13.38636 | -46.82386 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb5f8bcd-1ec7-3188-bd8c-37f5b678f7f7 | -14.3682 | -44.77557 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6ba59405-9288-3a89-a656-f1d1d1fe9d65 | -18.50809 | -45.14364 | 2026-10-01 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14dfc16c-08bd-3de0-acc2-8eba725fae1b | -18.16646 | -46.85754 | 2026-10-01 04:17:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90cd58f4-728d-3e1c-850c-940703fe2b61 | -17.473 | -43.56114 | 2026-10-01 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aea6dbea-7eae-302e-93c3-20e36f59b902 | -15.50873 | -41.5718 | 2026-10-01 04:17:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23557fe5-1482-3969-acee-d0d37a3efb0a | -12.85956 | -44.33455 | 2026-10-01 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3dec517e-537a-3765-af39-ae12e483b91e | -19.04301 | -45.66663 | 2026-10-01 04:17:00 | NPP-375D | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe402a3a-bfbb-3fca-8d19-98f7a0d40939 | -13.86432 | -44.44243 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb9f7420-c4ef-39c3-a8cf-1a5ac293dfae | -15.23941 | -46.15054 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98fbb7a2-566a-3d18-886f-d1d750376525 | -14.38252 | -51.29247 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0f9200dc-9cf0-3307-a0b4-e521bd0c680b | -11.80416 | -50.51796 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4737dfa-f2f5-37de-b680-49ce9810e5c9 | -13.47136 | -40.46778 | 2026-10-01 04:17:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb99d3b2-c5bd-38fd-995b-82ed694fa796 | -12.77161 | -54.01546 | 2026-10-01 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c239380d-86ca-33af-a7ac-63c3c23bd546 | -15.67254 | -41.03421 | 2026-10-01 04:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8eb56f20-b3bb-306f-ab42-3e03ae947d2b | -13.07634 | -51.18193 | 2026-10-01 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4c51743-c23a-3bb8-8762-741db7af5fed | -15.25488 | -44.82078 | 2026-10-01 04:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
