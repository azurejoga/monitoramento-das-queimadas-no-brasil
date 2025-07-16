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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f82423b0-3669-366c-a442-c4219590cc81 | -9.13386 | -47.58078 | 2025-07-16 12:10:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4daecba5-adf7-3dd9-9872-b508dbceabf9 | -8.84335 | -41.39889 | 2025-07-16 12:10:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 131454b5-3a80-378b-9171-8f2702b1d2f9 | -7.86426 | -46.22744 | 2025-07-16 12:10:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 07924a45-2842-3ce3-81d4-6c8c8499c3e6 | -6.73303 | -44.32692 | 2025-07-16 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| edee2921-ac46-31a2-945c-72afa922ab2a | -6.70644 | -44.32313 | 2025-07-16 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a80590ea-1402-3128-baed-5d3793f78b9f | -6.65538 | -45.73388 | 2025-07-16 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c6eb7e6c-437d-325b-948e-f40de0defebb | -6.43801 | -44.95999 | 2025-07-16 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 221cbb73-987c-39c5-a47a-fe453bbb1282 | -9.42539 | -47.4875 | 2025-07-16 12:10:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 43a0084c-4869-3bcf-bed2-cd776bffee3e | -7.63131 | -46.48023 | 2025-07-16 12:10:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| aec43a76-221b-31a9-a2ae-a3abd5133d54 | -7.62846 | -46.47368 | 2025-07-16 12:10:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b7c85195-10d1-3ae9-8c61-0e0b0971b857 | -6.95079 | -42.87756 | 2025-07-16 12:10:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3cc5eabf-ca79-39c5-ba60-69985a761304 | -8.76152 | -46.59327 | 2025-07-16 12:10:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 081b3b48-0b7c-33dd-bb6e-623b4097291b | -7.61204 | -44.50575 | 2025-07-16 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3b6a9d3f-a9b5-3066-92c5-a4af376290f2 | -8.99855 | -41.00339 | 2025-07-16 12:10:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| c8c84fb3-d21d-3db3-9f6d-9fca1e874f34 | -8.25307 | -44.92403 | 2025-07-16 12:10:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 1a7c5448-d26c-36d7-a648-6c7c1ad0c39c | -6.98077 | -42.80594 | 2025-07-16 12:10:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 08e913f5-e9c9-3f65-81b4-acf956ed425f | -8.24282 | -44.93178 | 2025-07-16 12:10:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51baf9ba-eda0-396d-8485-824048eba41d | -7.60101 | -46.32885 | 2025-07-16 12:10:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 954e163f-bd65-3644-94dd-044501e4698d | -8.82472 | -44.54206 | 2025-07-16 12:10:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e091482-dcb4-3f72-8c50-e94424756b3a | -13.73415 | -42.80677 | 2025-07-16 12:12:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a8714b4e-441e-3855-8113-bfa587041a0d | -16.37434 | -45.10426 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a3c5f9e8-c5ad-31c8-adad-3063957eb0de | -11.94982 | -48.41636 | 2025-07-16 12:12:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 275d4c20-6f9b-3d92-b6bc-60df2327ac05 | -12.99427 | -44.87725 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d37479e1-e4f9-3bb8-92a9-3f9ba27977c9 | -12.42165 | -50.0314 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 373.1 |
| 6399fa4c-0b6f-3dd5-a730-3f4479981cd4 | -11.94682 | -46.35291 | 2025-07-16 12:12:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5d3b3fe4-66eb-352a-abea-efe077f0758e | -12.5923 | -44.79368 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 3b30062e-d015-3f01-9179-aef3d779f488 | -17.20816 | -47.65722 | 2025-07-16 12:12:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cc1dbe17-d881-311f-bbca-c82fbc235592 | -10.38942 | -49.76732 | 2025-07-16 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 3934c8d4-8b55-3359-8a19-ec31357347bd | -17.92391 | -45.56123 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6bbdd40-5690-3c62-bea9-c2e72dc6702f | -12.41067 | -50.0401 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c46d2fcc-ce1f-3741-acec-019e0e873aff | -11.9545 | -46.36393 | 2025-07-16 12:12:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 82bdb0c5-63ae-38a2-ad31-11f77457ae9c | -12.29131 | -48.77648 | 2025-07-16 12:12:00 | TERRA_M-T | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 540c3ef0-93b2-33e6-8293-9a129ad8dc30 | -11.24058 | -41.50496 | 2025-07-16 12:12:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| beb5e484-3b67-3386-948c-5edeed9a6e35 | -13.16485 | -43.13986 | 2025-07-16 12:12:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| dc668a41-4d92-3f67-a698-526c40aea057 | -12.41896 | -50.04746 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 42e34265-f9a5-3396-985e-daf1a96d26d6 | -11.46973 | -47.32512 | 2025-07-16 12:12:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9067e06c-aaa9-3c37-b018-b46a8e008ce3 | -14.74301 | -46.30049 | 2025-07-16 12:12:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eecd50f3-ed19-3cad-ad87-15524f752552 | -13.34686 | -41.71724 | 2025-07-16 12:12:00 | TERRA_M-T | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b961fb9a-105e-321e-a679-996ff2c2b03f | -13.1635 | -43.14965 | 2025-07-16 12:12:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a2d49b58-2772-367f-9c14-d4516af1b4a9 | -12.41545 | -45.37592 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 17234045-2bb4-3ee0-8d7f-b26c47f15751 | -13.73553 | -42.79649 | 2025-07-16 12:12:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2df9650c-517e-3fbe-8802-75083d3cb8aa | -10.6368 | -48.48554 | 2025-07-16 12:12:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5d639cfb-ace0-3238-af79-4d07d150fb7b | -13.61598 | -45.23238 | 2025-07-16 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d100f849-c1eb-3b82-83ee-fdc26bcf724e | -13.28528 | -43.60049 | 2025-07-16 12:12:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b83f08d8-7c5d-30f5-bb08-354c4cdaf151 | -12.43315 | -50.03338 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 546b64a5-5a04-3743-94ab-8d15b7c1c22e | -12.4181 | -45.35785 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 914b6162-002b-3761-bf2b-31865c9ad5a8 | -13.16566 | -50.76653 | 2025-07-16 12:12:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 461aed58-347a-3824-bd5d-b42b681acf4e | -11.45821 | -45.10199 | 2025-07-16 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 40283ea0-7991-31b5-ba20-0f0bae39ea28 | -11.4739 | -47.32123 | 2025-07-16 12:12:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 8d1f11be-4ee2-36a5-a52e-48871493a3b8 | -10.89456 | -49.21171 | 2025-07-16 12:12:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fefd4557-4eaf-3761-a75d-1383a22e5596 | -10.59975 | -46.22381 | 2025-07-16 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 3cb371bd-e771-373b-9182-f6d27254dcb3 | -10.5983 | -46.23352 | 2025-07-16 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 66e3d8c5-a4d0-3e9e-bdc1-b32ef2a09da8 | -10.6348 | -48.49857 | 2025-07-16 12:12:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c81a936f-9d4a-3337-bc3a-91a2261340c2 | -16.78593 | -49.11549 | 2025-07-16 12:12:00 | TERRA_M-T | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 454fcc08-8c4f-3ae6-8b01-29a9b957c149 | -12.28922 | -48.78951 | 2025-07-16 12:12:00 | TERRA_M-T | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a109349a-e6e1-322f-94bb-de8e7ae61805 | -12.43048 | -50.04939 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 69ba50b1-d87c-3e46-b52b-82647acc5461 | -13.80305 | -41.50309 | 2025-07-16 12:12:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c085714d-5e13-3921-90f9-6ec461c72eab | -13.01521 | -45.06045 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| dbe5baf1-baf6-36d7-bdf6-cb8f996c78b0 | -13.05794 | -47.80988 | 2025-07-16 12:12:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 37f2629b-2a5e-3412-ad2c-1a23dd57ee44 | -17.322 | -46.77851 | 2025-07-16 12:12:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5fd11aba-953b-34f3-921a-bc4ac9e61317 | -10.58767 | -46.24183 | 2025-07-16 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 57350092-19e6-366e-87b1-6290b9284d14 | -11.95306 | -46.37358 | 2025-07-16 12:12:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 07fecbcc-98c4-3d9d-acf0-d859afc35b06 | -11.94538 | -46.36255 | 2025-07-16 12:12:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8b2ee96c-dbfa-31d8-ad05-fa3f0add603e | -15.51778 | -46.98672 | 2025-07-16 12:12:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 837a0d53-72ca-3300-ae5f-a949c73620df | -12.59359 | -44.78472 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c7b489ab-f4a8-38c6-806f-dce670458ae0 | -13.61468 | -45.24139 | 2025-07-16 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 08d24527-d32f-3c74-ba3e-42899526ff2b | -11.47135 | -47.31436 | 2025-07-16 12:12:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4b53037f-e1d5-36fd-b221-af35580eb7e0 | -12.4883 | -46.92299 | 2025-07-16 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5fae52de-64d3-35f1-927c-82d588883438 | -12.41326 | -50.02399 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| aedc1a22-056b-336c-b766-b212c1481518 | -11.54036 | -47.87621 | 2025-07-16 12:12:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0dbd8175-7122-3a88-943d-41954abbdd6d | -14.31697 | -43.33084 | 2025-07-16 12:12:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 47e0cba0-8e29-3b25-8e1c-26247c4508c5 | -12.51542 | -44.22894 | 2025-07-16 12:12:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04ba3d76-bfcc-3d6d-842a-09a8cd1dd1aa | -13.34531 | -41.72898 | 2025-07-16 12:12:00 | TERRA_M-T | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| f72ced21-cb99-307a-a4c2-c89df7b799b3 | -13.05976 | -47.81647 | 2025-07-16 12:12:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b6209c1c-abcb-3d03-9e13-e0f54c0eb60f | -12.02789 | -47.77331 | 2025-07-16 12:12:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 32804fb4-8e61-32de-85fb-1836e89e0d59 | -12.42476 | -50.02596 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 230.6 |
| fede9620-cab7-33ee-a9f4-37fcd2d2d663 | -13.72614 | -42.79523 | 2025-07-16 12:12:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f1ca1ce8-387f-300c-8364-f643423b1c4e | -12.48053 | -46.9115 | 2025-07-16 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 38edd952-a75a-3b0d-b6ee-83b91189d7bb | -12.47745 | -46.93163 | 2025-07-16 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e9160a6b-b8d3-3d79-bcc7-89074d64184f | -13.72477 | -42.80544 | 2025-07-16 12:12:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 292d309a-aa25-30a2-ac28-5bd769590fa4 | -12.02619 | -47.78443 | 2025-07-16 12:12:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 42527552-3997-371f-a11a-810167087897 | -10.59686 | -46.24324 | 2025-07-16 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 5ebc1478-ef11-3d23-80dd-2706070332a1 | -12.47899 | -46.92156 | 2025-07-16 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 30d4225b-ceb8-3625-83aa-7926ac385b5f | -10.58913 | -46.23208 | 2025-07-16 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9a2ecb64-a85f-3f6e-bef8-2b89ebe0d451 | -12.48676 | -46.93305 | 2025-07-16 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 39bd538a-cc13-3361-b3de-54928e19ea65 | -17.80578 | -44.34894 | 2025-07-16 12:12:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31e2db5d-ed5b-3e8a-bdad-ee5c5d5c8873 | -12.41678 | -45.36688 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 17c68b1f-3379-348c-942d-26f371206b91 | -14.31832 | -43.32092 | 2025-07-16 12:12:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2d4335c7-a028-3549-a5a0-b42154a5890f | -12.88238 | -49.1904 | 2025-07-16 12:12:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4ad9fec2-250a-3be1-89cd-4ac67c0f96de | -14.75192 | -46.30189 | 2025-07-16 12:12:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 15a516ed-309e-3ac8-a025-73f51a5a429b | -13.02402 | -45.06174 | 2025-07-16 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e32d9fe8-8a58-38f4-a82b-c55761c42ac3 | -12.07722 | -43.47468 | 2025-07-16 12:12:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6fc6d859-e883-3dcc-8b05-d33fdf7b618f | -12.42219 | -50.04202 | 2025-07-16 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 554.2 |
| 35cf4d39-c75b-349d-acff-3ed6378c0837 | -19.96812 | -45.29733 | 2025-07-16 12:14:00 | TERRA_M-T | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1aa43b2d-15d1-37f5-8c5a-6d3e777d8cb3 | -20.02784 | -47.39096 | 2025-07-16 12:14:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c54317a-bec0-3c41-be3d-a8fc4f0d3cb4 | -18.73774 | -46.87541 | 2025-07-16 12:14:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 319c10e6-e5fc-3c1c-a804-ea0559b0e21e | -19.53995 | -45.06374 | 2025-07-16 12:14:00 | TERRA_M-T | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f9c82e9-4898-3a30-b75c-a82f6c4e728f | -21.01915 | -51.34835 | 2025-07-16 12:14:00 | TERRA_M-T | MURUTINGA DO SUL | SÃO PAULO | Brasil | 3532108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| b2e46a36-30e6-3c7f-b826-8ba69a945249 | -20.38259 | -45.49862 | 2025-07-16 12:14:00 | TERRA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04cc3710-24b7-3c9d-be7f-b2b3354394bb | -20.37365 | -45.49724 | 2025-07-16 12:14:00 | TERRA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README28.md)
