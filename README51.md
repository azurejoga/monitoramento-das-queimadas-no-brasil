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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97ee6140-718e-397f-a378-a3a5b73173ff | -15.51734 | -47.35495 | 2025-08-27 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e29ea19-09ef-38bd-a33b-c7f39132e686 | -12.93835 | -46.32914 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55e6ae07-afb4-3c64-b837-0ac3e847452e | -15.76745 | -43.22245 | 2025-08-27 04:27:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 014f77a3-0be9-3862-a2eb-2b0c9b200b66 | -15.123 | -48.66896 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d369b609-6d9a-351c-b83f-f286de54776c | -12.86932 | -48.10294 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 052f29de-7d52-33c8-abf3-0c57e8f770dd | -12.87706 | -48.09699 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1ec2dfc-6fd9-37b2-a81a-e4101949834c | -12.90116 | -44.66363 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a7db05b8-91c4-389a-8ed0-1996ed83d903 | -14.36806 | -53.35962 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28a4a55c-e643-3d11-a652-4256f12f771d | -13.2233 | -44.54715 | 2025-08-27 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbdf0093-081b-33b8-891d-eaebc08680a6 | -17.77273 | -44.48645 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2767d459-a91e-37ee-a0b8-8ac483e5bf1a | -11.76608 | -48.98929 | 2025-08-27 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 121d0e9d-811d-3371-b897-4227eecfe0ad | -15.65801 | -52.72741 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6077f97-4d79-3a35-ab7d-6ae284abc538 | -12.75215 | -48.1998 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89652079-7a45-31e3-adc3-9a6059a9e608 | -19.07869 | -44.32496 | 2025-08-27 04:27:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6890e8a5-0b2c-3fc0-8a18-6ef82d005859 | -17.21051 | -47.21159 | 2025-08-27 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77d38eff-5c26-3fed-b203-4b5d70864648 | -13.07367 | -46.31981 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2c35ab48-4a08-3aca-a9fc-ec578ff70d73 | -9.39034 | -60.52954 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4738b52-7379-3795-94f2-ce53c49946c0 | -11.79843 | -51.40651 | 2025-08-27 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c05e912-82a9-34a5-9601-c38e140bf9ad | -13.66685 | -46.90557 | 2025-08-27 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 159048f4-77ba-38ce-a6c1-0f20470fc64b | -21.04327 | -49.90607 | 2025-08-27 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7c20f734-ae25-3200-b2d5-de4add8001b3 | -20.87154 | -55.00875 | 2025-08-27 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcfa45e6-dc60-3ab0-8ef7-e79f93bbfcb1 | -20.98824 | -40.95487 | 2025-08-27 04:29:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1286d279-f3b2-3b84-8044-f37d864cc2e2 | -21.38502 | -46.94032 | 2025-08-27 04:29:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 01843bae-5b16-3568-a6e7-f170c5e16229 | -20.04588 | -46.09579 | 2025-08-27 04:29:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f9cdbbb-cade-3d19-a18c-e534309c2cde | -22.16163 | -47.07657 | 2025-08-27 04:29:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 977ff28f-f3fa-3cb6-88b4-7f016065fef5 | -21.13231 | -45.88629 | 2025-08-27 04:29:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c6f28ace-0bbb-362f-8c35-2ccc68e8b6ec | -22.16285 | -47.07377 | 2025-08-27 04:29:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c4a341e-7298-35df-b226-9b5f4f63bf6f | -20.86829 | -55.00407 | 2025-08-27 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58484e87-a8c4-39c0-8483-b4a5bc64735f | -20.02588 | -45.55532 | 2025-08-27 04:29:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3467452-893b-3c5d-ab4b-0453efd947cd | -20.67864 | -47.53765 | 2025-08-27 04:29:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3630461d-98b8-3415-a2bf-17b34fcb50a6 | -20.75656 | -44.75788 | 2025-08-27 04:29:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 688865a0-0c35-3a07-b465-a9acc5a81e85 | -20.39875 | -46.72474 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3036a885-3296-3456-9f8d-9dc4396ebad7 | -22.45586 | -46.79727 | 2025-08-27 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c233851-21cf-32a2-b63b-6614e1368cd2 | -20.48785 | -42.9705 | 2025-08-27 04:29:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4e1b8f2a-f30a-32ef-8af2-c955a9de74a9 | -20.11362 | -44.33108 | 2025-08-27 04:29:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 27983f8d-c26a-391a-9ed7-d8ef5585195b | -21.23992 | -44.58435 | 2025-08-27 04:29:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4389a46f-e9aa-3748-86cb-ab89a97e37f4 | -22.16518 | -47.07711 | 2025-08-27 04:29:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47cc27b3-487b-358e-b34a-c1dd76fb3f91 | -20.85018 | -49.47044 | 2025-08-27 04:29:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 27e49764-ab33-3d04-ba42-51ece1671d17 | -21.38562 | -46.936 | 2025-08-27 04:29:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48599867-d003-371f-9cab-e9506ac49d77 | -22.03264 | -45.27767 | 2025-08-27 04:29:00 | NOAA-20 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3458fa51-6c38-3e2a-a8f2-4df8924a00f2 | -20.53783 | -43.8382 | 2025-08-27 04:29:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 900198f4-bd40-3c19-ac3b-ae92fb6f3137 | -23.26555 | -49.51544 | 2025-08-27 04:29:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5f39cd05-3e51-3c9f-9d15-a070c75922d9 | -23.326 | -47.84553 | 2025-08-27 04:29:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0267e53d-25e1-321f-ba1c-d63c4302b3da | -22.65557 | -46.25197 | 2025-08-27 04:29:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9d6b23b-1e88-397c-8195-1eb8a0a8d54d | -21.78747 | -43.30416 | 2025-08-27 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 347edc13-ac22-34a9-b838-f69383983688 | -20.51797 | -42.27098 | 2025-08-27 04:29:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89a3624d-8335-3a7d-99b8-db3117fc8029 | -21.23945 | -44.5881 | 2025-08-27 04:29:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba06b24b-f592-37cb-afee-64ed5cc4d668 | -20.52772 | -46.11132 | 2025-08-27 04:29:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4870f756-b5a1-339c-b797-62c4073e20c8 | -23.08021 | -50.4015 | 2025-08-27 04:29:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a4fc48e7-bb9b-390b-b428-3c1dcf2f4350 | -21.13343 | -45.88864 | 2025-08-27 04:29:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 685a0fa8-e597-3de9-a826-f24768d0cbdb | -20.67521 | -47.53704 | 2025-08-27 04:29:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d698e97-3b09-379f-99dc-fb18b533444c | -21.34776 | -46.8952 | 2025-08-27 04:29:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e07675f-819d-3089-bfbb-e09686a4b58d | -21.38173 | -41.99767 | 2025-08-27 04:29:00 | NOAA-20 | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0b8557cc-8260-3771-83f0-f3f05594d3e1 | -20.75547 | -44.7597 | 2025-08-27 04:29:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 550340d2-660f-38d0-b93e-7a5f4814abb2 | -22.92042 | -46.69187 | 2025-08-27 04:29:00 | NOAA-20 | MORUNGABA | SÃO PAULO | Brasil | 3532009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b40d7544-90ba-3f8b-89f3-7f076f453f99 | -20.3928 | -46.71543 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db7b3ead-1cce-323b-9e34-d1297273afa9 | -21.58366 | -47.47566 | 2025-08-27 04:29:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0cdcf06-2436-31f5-a873-7558044e3531 | -22.16577 | -47.07282 | 2025-08-27 04:29:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83cbca8e-faae-32f4-996f-210f10604523 | -21.4319 | -45.48684 | 2025-08-27 04:29:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c5ce7f2b-1f1a-3867-a548-1be7ccf41162 | -20.7984 | -44.57872 | 2025-08-27 04:29:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9bb8998b-203c-3771-aba6-c0e50476f44a | -23.42187 | -53.73135 | 2025-08-27 04:29:00 | NOAA-20 | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fa618108-a213-3301-a6f5-ecd08e8814e5 | -20.36923 | -42.19405 | 2025-08-27 04:29:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05cce0cc-aa2f-3e02-99de-0a40fb28b6bf | -20.7944 | -44.5782 | 2025-08-27 04:29:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a8b4378d-764d-3e65-bc6f-66a94f2a1208 | -20.89558 | -42.87639 | 2025-08-27 04:29:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7b76908c-93b9-359b-821f-d132e75d2a26 | -20.39519 | -46.72428 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db426678-a713-337f-a3dd-163b44d22ba1 | -21.13403 | -45.88406 | 2025-08-27 04:29:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a8cc0f56-0aa1-344a-97d8-a9bcdde6cc51 | -20.11059 | -44.32283 | 2025-08-27 04:29:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fee7f450-de7d-31fc-a915-1151587bde4d | -20.10387 | -43.69362 | 2025-08-27 04:29:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 403674dc-b496-32ee-a1f7-5030bf47bf49 | -20.39461 | -46.72846 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c045e0f5-56c5-3441-9a15-ac11fd99c991 | -21.57901 | -47.48339 | 2025-08-27 04:29:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e91e6dba-0749-397a-9b44-a8a223f93465 | -20.51907 | -42.26955 | 2025-08-27 04:29:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7884c80d-44cd-35a6-bab6-a72fc12f5ac5 | -20.98285 | -40.95737 | 2025-08-27 04:29:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1bfc464e-8d08-3fe0-9cc9-fa361ed36bc0 | -19.97099 | -47.52467 | 2025-08-27 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e910b159-dcae-3717-ace6-566d9f3f8f31 | -20.47303 | -54.53195 | 2025-08-27 04:29:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9b299fd3-e011-3d28-ab95-a714e367af4e | -20.85389 | -54.9628 | 2025-08-27 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d46ec825-089d-367d-ae35-79ed14c11572 | -20.39339 | -46.71118 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a31939a2-2bc6-37f0-b3ee-166e917722bc | -23.54872 | -54.6553 | 2025-08-27 04:29:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 050519a2-4f55-3bfa-be81-73b59ead4fed | -20.02214 | -45.55474 | 2025-08-27 04:29:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 353dc130-1c26-3d8b-9860-dea1c486984e | -20.53451 | -43.97073 | 2025-08-27 04:29:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66edd2ce-c835-3adf-a42d-ae855940cf62 | -21.58249 | -47.48389 | 2025-08-27 04:29:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb3ca19a-1fec-330d-b32f-c009e9df3f7c | -20.98855 | -40.9518 | 2025-08-27 04:29:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f436defe-d7fb-37d8-81b2-78dd7c0ec6d3 | -21.78755 | -43.30131 | 2025-08-27 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 330d1207-f174-35e9-989a-4646aa657337 | -20.98792 | -40.95796 | 2025-08-27 04:29:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2866bfd-69c6-3c28-a6ff-c33f3a77ea6c | -22.68522 | -46.8342 | 2025-08-27 04:29:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| de3cf57a-8b32-3c8e-9aee-5aa19e21708a | -21.09706 | -48.83827 | 2025-08-27 04:29:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ec70d175-48a5-37ff-9888-482ba947819c | -22.18005 | -46.63344 | 2025-08-27 04:29:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3fd40f70-fc32-3c41-ba22-30f62ab477d6 | -21.09763 | -48.83452 | 2025-08-27 04:29:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1ebcb7d6-34ef-31a1-804e-c8ace4f8cf4d | -20.39694 | -46.71171 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0eb39620-37e4-3be6-80fa-64bc47e5c7ac | -21.13601 | -45.88698 | 2025-08-27 04:29:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7fc4bcfb-a87b-36b6-9ef4-ea8f5f6a6998 | -21.58077 | -47.49609 | 2025-08-27 04:29:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d77530b0-2760-36fd-825e-ff91a45abb73 | -22.22917 | -50.86042 | 2025-08-27 04:29:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6db67383-e3a9-35ba-bbd4-af1f0da9e30c | -21.58134 | -47.49202 | 2025-08-27 04:29:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 590fcf2d-d6c2-32d6-887b-ac3cf56d2f21 | -22.6774 | -46.83746 | 2025-08-27 04:29:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e1572597-9256-38d2-a7fd-805a70bd74fc | -21.63935 | -46.79798 | 2025-08-27 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0b5cc917-1df1-3cfb-959e-ac0b85799217 | -20.52259 | -42.27158 | 2025-08-27 04:29:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9119a14f-b8cd-3341-9ea6-661b3dc6024f | -23.04282 | -50.31813 | 2025-08-27 04:29:00 | NOAA-20 | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81bffe70-4163-35c0-b618-56d19fc74337 | -20.39992 | -46.71635 | 2025-08-27 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 224d4218-e6ca-3001-94cd-5f906bd570f4 | -21.13293 | -45.88173 | 2025-08-27 04:29:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 953406a8-b05f-3832-a38b-15b575c322b6 | -21.58598 | -47.48438 | 2025-08-27 04:29:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ed29e21-81e4-3b43-809b-73a79abe08db | -22.55195 | -49.76601 | 2025-08-27 04:29:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README52.md)
