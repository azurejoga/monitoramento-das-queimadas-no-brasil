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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd3115c8-0f2c-3c79-ad93-eee9e6a28515 | -7.47579 | -42.67503 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2612db45-b0a6-38e2-b70c-d384d860c111 | -7.46014 | -39.96322 | 2025-10-16 12:00:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 526091d7-9364-3f31-a386-62cb535e8374 | -7.41776 | -43.77592 | 2025-10-16 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f6152d6b-a524-3578-9461-b5f5b8196911 | -10.13128 | -44.59096 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 28.6 |
| d00d878d-3080-31cf-9f97-dae4d823709b | -13.70819 | -42.40783 | 2025-10-16 12:00:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 73f4ef99-9af9-3cd4-9717-e5a69eab7d3f | -11.57615 | -44.05591 | 2025-10-16 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a500b342-4a93-32b8-b7a2-1ccb70ebdae4 | -11.47609 | -44.10885 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 68f582ee-47b2-372b-bb70-ed503ba53e48 | -7.92876 | -44.13131 | 2025-10-16 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e6906091-1538-34dc-9426-010707bdc699 | -7.9485 | -38.20282 | 2025-10-16 12:00:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 4cc68f0f-c404-39b5-9f8d-cf67fe63738e | -6.35865 | -45.48365 | 2025-10-16 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d1ec4e94-2bc3-3dff-9ed7-19463c748bb0 | -9.25444 | -45.26236 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 9f816fb8-8973-36bb-9a54-60fd9332d4cf | -8.4678 | -46.24057 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| daf65afe-f5d3-3fc7-9ca8-3ce43977b823 | -8.24534 | -44.05092 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 53038de3-42fb-3429-8c5b-02ca9b2a34b8 | -9.71632 | -44.52693 | 2025-10-16 12:00:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| bda6592d-4e6f-3f19-bf16-3b011c5c7a12 | -11.585 | -44.0572 | 2025-10-16 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 528ade5d-1b4a-31f4-9efe-a64b9d4254fe | -6.78066 | -44.6517 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 771a91a4-1cc1-38a4-9ff4-ba9d37d48072 | -9.67877 | -44.53109 | 2025-10-16 12:00:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 47021ddf-66a5-3a26-9c17-2bd1d48ceae6 | -9.27093 | -44.35448 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 182b7033-05b6-3af4-8c28-5e6760ba0fe3 | -8.06991 | -45.41601 | 2025-10-16 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 25260826-c6b7-32e1-825c-0397379ab433 | -11.46419 | -44.19017 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 1cce20e5-b9e2-3cb8-8a04-fb76e94b807f | -8.39135 | -46.27103 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| ceea79a7-2f80-36ef-98d7-7d156f4db6dd | -8.25106 | -44.13666 | 2025-10-16 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6e9d0043-1b7b-37bf-9d96-78b1af2d7c0d | -6.50558 | -43.70417 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1d1a98e1-9b69-3120-b175-a5ce925e59b0 | -11.42047 | -44.16812 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| b30dc4b8-dea9-3ac2-8968-5083a08d21e9 | -11.90862 | -46.80772 | 2025-10-16 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 1a4e0f43-b8ac-3831-be56-fdd0f301cbec | -14.2068 | -41.84754 | 2025-10-16 12:00:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 301dd660-54e4-3af0-bf4e-11eb9a45e27f | -6.4507 | -43.38378 | 2025-10-16 12:00:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c336a71c-5921-3853-ad37-97fea806f0ad | -12.28712 | -47.14539 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 299.5 |
| fccf610c-24d1-31ff-bc35-0c20374ec32c | -12.98955 | -43.45917 | 2025-10-16 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 129838e3-14f8-3843-9fb7-3e5379842c2c | -8.1854 | -44.01758 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 87abb427-f62e-3a8b-9051-113e1f230d93 | -6.54719 | -43.92451 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9886884a-2fb7-3aeb-a69f-b1506ec93762 | -11.85063 | -42.91082 | 2025-10-16 12:00:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 57a779aa-691e-34a7-89d8-b44508b974db | -11.43066 | -44.16038 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 320fad10-ddf2-32bf-b6cc-ded65b86ddc5 | -7.4616 | -39.95254 | 2025-10-16 12:00:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 11b94ad9-3bb5-329a-acda-7c0159437985 | -12.30871 | -45.65346 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 273.4 |
| 1b493b9e-e2ac-399d-ac00-d2702def6f49 | -13.62877 | -47.87944 | 2025-10-16 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c55aeb7a-e326-3381-9d79-364f85684c16 | -7.48199 | -42.75698 | 2025-10-16 12:00:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 210e5c3d-2a61-3a84-9f99-f2779d78deef | -12.30542 | -45.61244 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 40c3cc6f-4c59-3ef6-9f40-5185290c426c | -13.6672 | -44.26799 | 2025-10-16 12:00:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2bc6a9f3-0f96-36ad-ae70-17ced962ae56 | -11.42442 | -44.141 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 5a7c2c3e-67b1-349e-84d4-6c2d850628a1 | -10.58995 | -47.423 | 2025-10-16 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eb0e8a40-58b0-3096-9182-5a0b1b47af5c | -11.43427 | -44.19787 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 238d6c18-2290-3a05-a677-4271b4fe0047 | -10.50292 | -43.3717 | 2025-10-16 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2a45e74e-dcbb-364f-975c-7732c347472f | -11.42574 | -44.13197 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| d211acf8-561d-3ed2-854f-93485bd4f732 | -8.23782 | -43.3362 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 1a3435ba-dcda-34e3-9604-80c4b929f024 | -11.43099 | -44.09586 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9787a8fb-5838-32a6-8dc7-7a7bc72cbd0f | -12.28071 | -47.11989 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 645c55c7-f83e-3577-ba7f-ab181233f624 | -10.65253 | -45.23956 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1b788942-197e-31e6-ae67-bc70687cbdb4 | -8.30181 | -43.40638 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 23868c45-dc40-32b1-9f21-af16fc76316d | -11.58992 | -44.08553 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| ca2f438b-1931-3fdd-9c0b-0807b750711e | -8.24942 | -44.02333 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d98f3ab5-6053-3534-b470-3513fff6d23f | -14.17924 | -47.96869 | 2025-10-16 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2081c019-8762-3187-aa77-96ee1e5a39ff | -18.75635 | -44.45435 | 2025-10-16 12:02:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d820cdf2-a278-3971-aff8-599dbc6b1a9e | -18.4002 | -46.63978 | 2025-10-16 12:02:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 23fc89dc-b326-3955-b4ab-316c4483de85 | -19.24481 | -48.76276 | 2025-10-16 12:02:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 25.2 |
| b4660e6e-1193-3ed3-addb-27afb997bfc1 | -23.06128 | -46.57737 | 2025-10-16 12:02:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 62eb221e-9e36-362d-9d44-bc23210eeb98 | -18.44841 | -44.48487 | 2025-10-16 12:02:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e05fc19f-98c9-3257-8c73-c751687ae6b3 | -20.82941 | -45.82189 | 2025-10-16 12:02:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e60b4217-fc7d-3e3f-91e9-773453980b2b | -22.62017 | -47.0026 | 2025-10-16 12:02:00 | TERRA_M-T | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d1aa1457-41a5-30ff-a94d-561fd960e8ad | -18.90235 | -47.22441 | 2025-10-16 12:02:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2d0084df-7ea9-3e40-9236-ee0f6ebef602 | -22.71172 | -46.44478 | 2025-10-16 12:02:00 | TERRA_M-T | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 5e180a6d-c920-3e8d-9ab1-98454ee7f475 | -17.62767 | -46.43806 | 2025-10-16 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| faee348a-60ee-3d58-b9b8-e07690085e16 | -17.62154 | -46.41706 | 2025-10-16 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 27c32ce5-d753-3360-8bc2-fc688928128f | -19.23452 | -48.76699 | 2025-10-16 12:02:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ccb7d068-9e3d-3fde-8f72-8d85fe40d43a | -21.4261 | -47.56879 | 2025-10-16 12:02:00 | TERRA_M-T | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 7964942c-caeb-3277-91e8-615293f6f375 | -21.69131 | -47.28186 | 2025-10-16 12:02:00 | TERRA_M-T | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6b6ddef0-5e4c-3ff5-a1eb-6df507d1c2c3 | -17.63063 | -46.41848 | 2025-10-16 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| db07a280-88ab-3346-918f-05757253607e | -18.13242 | -45.71268 | 2025-10-16 12:02:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8a807a07-0a0e-3324-8081-0bca5d8994a9 | -20.59914 | -44.65241 | 2025-10-16 12:02:00 | TERRA_M-T | CARMÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3114501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 426e9a11-8ba9-3980-bcfa-3a75d500cd3a | -17.63824 | -46.42973 | 2025-10-16 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ba77152a-afc9-3452-8b92-4f0e6f936c36 | -19.24279 | -48.77498 | 2025-10-16 12:02:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 230.2 |
| bcba566a-6778-3bea-937c-6d35cb4941e0 | -17.62915 | -46.42826 | 2025-10-16 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 188.6 |
| f4063548-5c01-3848-b95d-fcb060f29706 | -19.23255 | -48.77935 | 2025-10-16 12:02:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0f4c8798-1090-3d1e-917e-9d1484889faa | -19.2327 | -48.77337 | 2025-10-16 12:02:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 86fa69f7-4971-3253-8083-3e7e8d58d865 | -21.63331 | -48.98883 | 2025-10-16 12:02:00 | TERRA_M-T | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 20.7 |
| cb692511-4c78-3866-9d3c-34871320ee2e | -20.63979 | -45.216 | 2025-10-16 12:02:00 | TERRA_M-T | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| d36d05f4-c01d-3e29-9bd8-6a939d12d565 | -19.04075 | -44.52599 | 2025-10-16 12:02:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| be329e03-b1cb-34a4-aacc-59256669fc83 | -17.85334 | -44.3236 | 2025-10-16 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6a9ac0b7-082c-3781-9eae-455ba93c2611 | -20.77279 | -45.95085 | 2025-10-16 12:02:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 651cd6ec-72c8-3b78-a8f4-fe7245b4a3ae | -17.62007 | -46.42682 | 2025-10-16 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 1389e9f0-cd9d-301d-a096-30ad2980b64b | -20.64112 | -45.20661 | 2025-10-16 12:02:00 | TERRA_M-T | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 8cf01097-d932-3027-8a18-5f9426c19045 | -10.6024 | -47.4178 | 2025-10-16 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| abe09ec4-1129-3027-8942-a66e55576fc1 | -11.5724 | -44.0736 | 2025-10-16 12:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| af4dd4a8-b18b-3f05-9ab0-d4abe32790e0 | -13.0165 | -43.0547 | 2025-10-16 12:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 126.7 |
| 0c572a07-0392-3c11-bfae-f0d99ba3d45e | -12.9975 | -43.0341 | 2025-10-16 12:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 66275d29-a9cb-34b1-9a1f-8d4202e234fd | -12.3116 | -45.6081 | 2025-10-16 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ae3ccd7d-9228-3c61-bc2c-e016c97aa769 | -12.9905 | -47.3442 | 2025-10-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 84e5b9d1-0fe2-38c0-81ee-d86fa1b5b256 | -11.5917 | -44.0707 | 2025-10-16 12:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 74d88a09-7ee2-3ae5-a4b3-049ed15a91ff | -13.9127 | -45.5808 | 2025-10-16 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| efacf8a8-10f8-3457-85c6-8d879925a1bd | -10.6021 | -47.44 | 2025-10-16 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b23e9d29-47d4-3446-94af-a08ab22d6bc9 | 1.84 | -55.7824 | 2025-10-16 12:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 09997fbe-2a67-3b8b-a878-6bc74e01791d | -11.4756 | -44.135 | 2025-10-16 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 39562df3-4d97-3698-8174-cb46c18f41fb | -10.6021 | -47.44 | 2025-10-16 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a6af77c1-cd10-331f-bc81-6c289adb2071 | -11.5724 | -44.0736 | 2025-10-16 12:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b68dfc75-3e72-339b-9ca0-f9666e30e448 | -10.6726 | -45.3355 | 2025-10-16 12:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ef574ba9-670b-3816-86fe-09449ec1c7ef | -10.6024 | -47.4178 | 2025-10-16 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7d2deb56-4bfe-37f1-9c60-6d7f0d8cb19d | 1.8217 | -55.8023 | 2025-10-16 12:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 70b71d8a-6a55-3dd5-b90b-a4d887c8cec4 | 1.84 | -55.7824 | 2025-10-16 12:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 55c5334a-0de0-38c0-a28e-0069c5ed2498 | -11.5917 | -44.0707 | 2025-10-16 12:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8fb12ec2-4289-3863-aa0e-d1861f65874c | 1.8217 | -55.7826 | 2025-10-16 12:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |


[Clique aqui para ver as próximas entradas](README89.md)
