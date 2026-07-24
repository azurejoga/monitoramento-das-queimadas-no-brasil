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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48d18ee3-da49-37f1-8cad-a709aa8bad29 | -10.61106 | -40.53065 | 2026-07-24 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e663ab83-48f5-3cba-9ce2-735ed5d5df12 | -9.2333 | -48.56255 | 2026-07-24 04:06:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e42c3e13-0bf3-3a87-950a-886615e0ae02 | -4.77167 | -41.79514 | 2026-07-24 04:06:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 899e629d-a0b8-396a-b8e8-ead67254c546 | -6.48395 | -43.7883 | 2026-07-24 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5c2d4285-1bf0-3c90-8cd3-bfbad5cd46e1 | -7.0203 | -42.78667 | 2026-07-24 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7312a11b-8d65-3961-9b43-66710b45855e | -9.01464 | -40.26782 | 2026-07-24 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15bece1f-39e7-3ee1-8143-54d9356ffb10 | -7.4306 | -46.88345 | 2026-07-24 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 350bd7cf-ac16-3ba6-a04a-f2de1b7e7d7c | -11.62037 | -50.14911 | 2026-07-24 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ed8e301-e196-3ede-a8b4-9fd2f2b63c4b | -13.4346 | -51.53498 | 2026-07-24 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e394392d-7bd5-39b3-a345-d65290c65124 | -12.46634 | -49.46019 | 2026-07-24 04:08:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 554c1944-406e-3744-89bd-7842b4d1db8a | -11.61865 | -50.1554 | 2026-07-24 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 866d3fb7-5e0b-381e-9ba3-59420c0bc63b | -17.91818 | -44.41027 | 2026-07-24 04:08:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ad6829c-b7b9-32aa-8c58-6dc30beeeb2e | -11.61957 | -50.15311 | 2026-07-24 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c06dd27b-da8a-3ee6-8744-be5ae921720c | -13.44851 | -51.52847 | 2026-07-24 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ea8ce68-5a56-30bf-bf9b-d11d742a8084 | -14.37731 | -50.33636 | 2026-07-24 04:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60625664-129d-315b-b878-f3eabbf2cb61 | -16.1462 | -43.61789 | 2026-07-24 04:08:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d7e0c90-bce3-3979-acc0-a8dd08f18f7b | -17.61423 | -46.64771 | 2026-07-24 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd1eb93b-d75c-3126-9428-be7c2816175b | -13.44156 | -51.53171 | 2026-07-24 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65a7d117-900f-314f-ac95-88564a281bea | -17.91895 | -44.4059 | 2026-07-24 04:08:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75ad1fea-8bea-3556-a428-91fe79f19e8b | -11.64318 | -50.36598 | 2026-07-24 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0db1f516-b325-3cbe-a357-c48ee63f9fb2 | -12.6666 | -48.20223 | 2026-07-24 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bed74e7c-9f0b-32dc-b188-71b2418f1ce7 | -13.43365 | -51.53958 | 2026-07-24 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f5dedad-24ba-35e2-8b18-3a7dea418eff | -13.4425 | -51.52713 | 2026-07-24 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20fcc6cb-1421-3a44-955b-fa49b4591eaa | -14.37259 | -50.33658 | 2026-07-24 04:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ce5e1bf-e177-38d8-b518-fa4f8f9e4572 | -16.74254 | -49.37209 | 2026-07-24 04:08:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e373fafa-e82a-3e34-82e0-ed1c960433d2 | -14.37808 | -50.33262 | 2026-07-24 04:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24d8f099-ae15-3781-8480-d367183410e9 | -17.61351 | -46.65151 | 2026-07-24 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f82f967e-0633-3b36-aa06-6a640a4b0451 | -17.91973 | -44.40147 | 2026-07-24 04:08:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4b74cd9-adc3-31f9-b836-80dbd315e2c0 | -12.45259 | -49.58899 | 2026-07-24 04:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9180b487-d815-3181-93a7-482ce363215f | -14.37808 | -50.33778 | 2026-07-24 04:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4050e7bc-4155-3c3f-9338-447428870de6 | -17.06181 | -45.03725 | 2026-07-24 04:08:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9def59d4-d1e1-3d58-82ec-bd874c838a30 | -12.44715 | -49.58794 | 2026-07-24 04:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b16a2a6c-c78e-3257-bc34-743afaefa0ec | -14.37883 | -50.33404 | 2026-07-24 04:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17728ece-5e65-347d-a4f7-c475427c2884 | -18.25413 | -42.52621 | 2026-07-24 04:08:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bfe15c5e-7dea-3bbc-909c-5961039a6e88 | -15.30472 | -41.31976 | 2026-07-24 04:08:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eff04253-80d7-3a10-9281-fb49eb77d252 | -16.14549 | -43.62202 | 2026-07-24 04:08:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d572cfc-c3c4-367d-9870-1cca800fd797 | -15.80423 | -41.64267 | 2026-07-24 04:08:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 56ee640d-4e4e-319b-bee9-f1d256948e28 | -14.23256 | -42.77167 | 2026-07-24 04:08:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 05fb6faa-a30f-3d4c-8cd5-9f55e3ad0b95 | -16.14974 | -43.61852 | 2026-07-24 04:08:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c67b7ca4-a453-3814-b320-e70a898a11c6 | -17.87017 | -45.52604 | 2026-07-24 04:08:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c5364d-a532-3375-9ac6-a49fb8f0364c | -16.34366 | -41.70156 | 2026-07-24 04:08:00 | NPP-375D | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0ff8dd6a-7ed3-3e0b-a0d4-c1b6c7fa8215 | -11.58535 | -48.39796 | 2026-07-24 04:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 972caf51-ac1d-329d-a595-e7a2185c97df | -17.41901 | -43.80873 | 2026-07-24 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2db0aa9a-b121-3522-b6ee-3e79c7adb6c6 | -11.6202 | -50.14738 | 2026-07-24 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e89e18b-2652-39d8-a4dc-434512c64189 | -11.64399 | -50.36184 | 2026-07-24 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7694edf-145c-3db1-9539-ffc9cd41b945 | -18.08495 | -42.32077 | 2026-07-24 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2d25ec3d-6999-3381-ac7c-d9b46b3973cc | -11.61943 | -50.15139 | 2026-07-24 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e749991b-4cf7-3bea-bf45-4cf62122721d | -12.66165 | -48.20131 | 2026-07-24 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb303b39-1654-32b8-bfd7-d966b9824665 | -19.0729 | -46.78075 | 2026-07-24 04:10:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 932de1fd-1414-3737-a04b-e5d68be007dd | -22.29011 | -42.51425 | 2026-07-24 04:10:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8ef9e7d0-a31f-3833-91e9-8b3bb6c003dd | -21.97174 | -47.66153 | 2026-07-24 04:10:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0af5d4ff-1451-3c61-88c1-04e3db10b348 | -18.198 | -44.73462 | 2026-07-24 04:10:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a96ffca-f5e0-396e-b671-3d95e8775c8d | -18.19878 | -44.73018 | 2026-07-24 04:10:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb9e8a7f-45b0-3437-a629-f3ef07a52fa5 | -20.44791 | -42.53625 | 2026-07-24 04:10:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b9d4d35f-0efb-38a8-87f9-c93ea851a2f5 | -20.44851 | -42.5325 | 2026-07-24 04:10:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b39ebbba-1d69-3551-8624-9641b5e98d80 | -21.97176 | -47.66208 | 2026-07-24 04:10:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15257de3-6310-3832-9d9e-4e15f6e01e5b | -21.32859 | -44.2211 | 2026-07-24 04:10:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a0efa886-f11f-36ea-a433-be1ee3cb9cde | -19.81474 | -44.1224 | 2026-07-24 04:10:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be561687-5e82-30f9-8f2f-9716292cba96 | -19.79592 | -41.96263 | 2026-07-24 04:10:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c0cea5de-ec1a-3fce-9801-9403deef046b | -21.66018 | -42.47474 | 2026-07-24 04:10:00 | NPP-375D | ESTRELA DALVA | MINAS GERAIS | Brasil | 3124609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3e11920f-b670-3124-8f79-e8ea33136031 | -19.57144 | -42.98004 | 2026-07-24 04:10:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5666062d-66dc-3120-accb-f7d653923923 | -19.72044 | -46.16902 | 2026-07-24 04:10:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a341d4c2-017a-38e0-a53f-6b7d3df8afd6 | -19.89975 | -42.19576 | 2026-07-24 04:10:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cd6f8df5-04d4-38b5-b150-b542e69a76c4 | -18.56303 | -42.87797 | 2026-07-24 04:10:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 72c9378c-dd3f-3fdf-9543-7e6e9f138d8a | -20.44518 | -42.53188 | 2026-07-24 04:10:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 45fb3b7f-d0f5-3762-a2c9-c18ee07ff30c | -17.77352 | -49.13429 | 2026-07-24 04:10:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66df79c7-518a-3abe-9767-b62c7cedefa9 | -21.33135 | -44.22574 | 2026-07-24 04:10:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 83a5cc36-efeb-3608-8cd8-b897612efac6 | -21.33204 | -44.22175 | 2026-07-24 04:10:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6894812a-6442-3eab-b73f-883bea8d3407 | -21.65289 | -41.70492 | 2026-07-24 04:10:00 | NPP-375D | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 559009ee-3889-34bb-84de-63424b2101bc | -21.71599 | -47.13411 | 2026-07-24 04:10:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91e98559-b063-37fc-847b-c3d1ca841552 | -17.77463 | -49.12885 | 2026-07-24 04:10:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d85134e0-f893-3e6a-916e-30e971b60c4c | -17.77456 | -49.13279 | 2026-07-24 04:10:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e83851e-e51b-33f2-b755-3f47e6d36748 | -21.09105 | -49.75106 | 2026-07-24 04:10:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c894b101-e347-361c-80a1-68bb71158582 | -21.53253 | -45.06568 | 2026-07-24 04:10:00 | NPP-375D | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab1b7590-d3f4-370d-9866-d3c630668d04 | -20.91723 | -43.30158 | 2026-07-24 04:10:00 | NPP-375D | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4b85e67a-a912-3dd0-8b80-c3dc6bd6937a | -19.72428 | -46.16976 | 2026-07-24 04:10:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 959d0bca-ede4-3044-8cc0-ab318506bbf1 | -4.77259 | -41.79517 | 2026-07-24 04:23:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b92f2e2e-205e-3f1b-93bb-ce2dabef816d | -5.3214 | -46.09721 | 2026-07-24 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 191f4f4c-fbf0-331d-b41d-009c67852c23 | -5.32264 | -43.5646 | 2026-07-24 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef6f0983-4e48-3629-8f4d-1c80a04f850d | -3.12505 | -40.98988 | 2026-07-24 04:23:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3350852a-6bee-3262-9656-247fa75211bb | -1.58685 | -50.43385 | 2026-07-24 04:23:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13ba31c9-92b7-3672-881d-4dd8f014331f | -4.371 | -47.76704 | 2026-07-24 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c4a66a69-914c-358d-bca2-aad88a50522a | -4.04535 | -43.23996 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbb7975c-1aff-3da0-86af-3a4dcbe4c5a9 | -4.04869 | -43.24047 | 2026-07-24 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9adf120f-001e-3d2e-85c4-b48d150fa379 | -2.01975 | -47.57026 | 2026-07-24 04:23:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac2897da-3a92-3130-9edd-cf1003d8390f | -3.14693 | -48.15026 | 2026-07-24 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f8a3c33-d8fa-3d31-8f08-29ecb8bebacb | -4.1578 | -43.08361 | 2026-07-24 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f394635c-14fe-366a-8bd6-93c44e1bb8a5 | -4.04924 | -43.23695 | 2026-07-24 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23ef2dc3-f172-375d-83d5-395f0d412091 | -4.03705 | -43.27107 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0132eb52-647c-315a-acff-2d3ccd6c7f03 | -5.49149 | -45.12082 | 2026-07-24 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdde9f61-d08c-322d-87ca-cded1fc5ddca | -5.9366 | -46.35059 | 2026-07-24 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27d30972-c79f-3ac6-9870-d4cdc9fe7c11 | -3.99707 | -43.28643 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a3dfd85-f0d2-3ed3-b06c-41550adb3e26 | -2.86782 | -46.76689 | 2026-07-24 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af72402b-fb2e-3518-bfad-0aaeac24a08a | -3.15147 | -48.14627 | 2026-07-24 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2180d03a-f1d7-3836-aa20-1a025d7adf37 | -4.01096 | -43.28498 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14ce5184-8740-3ff1-a2cc-1e0969021473 | -4.37052 | -47.76896 | 2026-07-24 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5df7b0fd-d515-3886-91b0-281a570ddc55 | -3.99762 | -43.28292 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34e35f80-85d4-3726-a6e6-d6e0f1447e1a | -5.82716 | -43.48323 | 2026-07-24 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bca60f76-ce10-3af8-af63-bba97d7eba06 | -3.63162 | -42.05253 | 2026-07-24 04:23:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a8077fb4-32c4-3060-8154-664659c5cf4e | -3.9942 | -43.2863 | 2026-07-24 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README4.md)
