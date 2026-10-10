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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04eae13f-57d4-3d16-9ff9-69427edc5203 | -3.8749 | -55.9961 | 2026-10-10 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fa3034f5-74c9-3e44-b230-ac07ab2e1f62 | -4.3582 | -54.75 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| e89e6be6-3bae-3035-bb0f-e1516049df6c | -6.9504 | -59.2405 | 2026-10-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1e3cbe64-f1e1-38a9-a928-3d5a1b872f7d | -6.4903 | -62.8554 | 2026-10-10 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| e716c910-d52d-35da-9fc4-3f52ff3eedd0 | -3.2737 | -54.6826 | 2026-10-10 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9fed48ad-67a0-3ef7-9abf-0d61368607dc | -9.2976 | -47.3871 | 2026-10-10 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| bc725ba9-51b8-3d37-bd20-802ebaef954f | -6.9503 | -59.2598 | 2026-10-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f0a4a9a2-3a93-372a-a878-5a7d1af14005 | -6.4567 | -55.4809 | 2026-10-10 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ed946fb4-13cc-393e-bb4f-acf13ca38bf1 | -7.4977 | -54.9854 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 7a3d21c4-c542-3c43-b81d-ee1c32657561 | -7.9084 | -54.7396 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 005d5525-0c9f-36f2-80b5-e31424021630 | -7.5162 | -45.3024 | 2026-10-10 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 66b526a5-81d2-3981-bf1c-323afd6e5d53 | -13.3865 | -43.8708 | 2026-10-10 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e4bf44f4-8d9e-3768-bf29-f5c92f8dde06 | -7.0228 | -47.661 | 2026-10-10 00:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 1bb40141-c03d-3b86-ac2c-a48543ac0e5e | -3.9911 | -59.3752 | 2026-10-10 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3bb18a0c-08e3-3b31-8966-64e8e9f74624 | -3.7495 | -60.5824 | 2026-10-10 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 6ff0cbc9-340b-3cf7-8229-f7431e29ade2 | -14.4535 | -43.9359 | 2026-10-10 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 244.9 |
| 8cdd5bbb-f9d5-3832-a2aa-51647bded00f | -5.7059 | -49.05 | 2026-10-10 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| b995a3e1-2acf-345f-a066-412d3fdc2075 | -4.4025 | -49.7774 | 2026-10-10 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 55a9f0d4-007c-3865-8322-08d82e50c6aa | -6.1482 | -42.832802 | 2026-10-10 00:09:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e70ef4ba-1dcd-3ae3-9157-303d1ead43fe | -15.997 | -40.6576 | 2026-10-10 00:09:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b44d56b9-412d-3502-ba8f-9d29cf70ce25 | -4.3894 | -46.5425 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eebd76e9-dd61-3c73-899a-f0f017e2565c | -11.4552 | -43.388802 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb31f76e-f8bd-366f-bf27-8310a5ad2af5 | -15.3796 | -41.904701 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86fbe1f6-2bee-3402-9bae-249797efbf6e | -13.7327 | -44.314602 | 2026-10-10 00:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c03d9f83-52f0-3c4d-b4f7-9b47ad3cc4c5 | -6.8637 | -45.034302 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1413da47-1ceb-3112-8730-31a5ae662da9 | -10.8937 | -44.84 | 2026-10-10 00:09:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e6607a59-1b96-3912-b272-e0c543a759c8 | -13.2528 | -42.2603 | 2026-10-10 00:09:00 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b72c7ad7-5d03-36f9-839c-a891d4a97aad | -18.3459 | -42.273499 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3742152a-c9f0-354c-86d8-d2d9428fe110 | -11.7633 | -43.537498 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 315796e2-c883-3929-8a8a-39dc32ca8051 | -10.889 | -44.818001 | 2026-10-10 00:09:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d75183b5-fe8d-3636-b2bc-77a0bbf22d76 | -4.7784 | -42.739101 | 2026-10-10 00:09:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 497aacc3-133a-3a15-a3f0-346c222de220 | -11.0132 | -44.051998 | 2026-10-10 00:09:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61905662-c5d2-3f42-a6a6-ebacd59dd143 | -5.706 | -41.652 | 2026-10-10 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46276a27-457b-37b3-90df-1339cfc59235 | -17.9778 | -47.2164 | 2026-10-10 00:09:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 597cac50-db81-388d-8452-add9219d5440 | -13.3901 | -43.8881 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5266b52-0f03-32b0-96bd-802fab3b591e | -8.2509 | -46.4333 | 2026-10-10 00:09:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5240f9ed-6e33-37c8-bd96-d1c5283264eb | -11.9452 | -43.478699 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b83350c-91bb-345b-a722-06a6d9f8eff4 | -7.0163 | -47.667099 | 2026-10-10 00:09:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea855d57-7293-34b8-852d-b1c3051762a9 | -6.4986 | -44.355598 | 2026-10-10 00:09:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11371b8d-0c67-3e28-9f15-bdc3a313fd46 | -4.5858 | -40.6768 | 2026-10-10 00:09:00 | METOP-C | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 886c9122-3ab4-3995-9d6a-0417ce8a748b | -11.9843 | -43.470299 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49c4a130-9ba2-3f0b-afb3-01ee47a3dc49 | -11.5645 | -43.709801 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a31e36d-e521-3c76-a4ea-9d715736fb18 | -10.912 | -45.512402 | 2026-10-10 00:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea16f6d6-8ac7-38e3-94c7-a5e5151a72bc | -7.5181 | -45.3097 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82fc90ef-15ab-3d1a-b3ac-dd4de094fcae | -6.1465 | -42.825298 | 2026-10-10 00:09:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 47659b67-9cbc-3441-8093-69e98162cdfc | -7.0896 | -41.757198 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8584ab7e-2b8e-3fce-af75-86c2992d04e3 | -15.3673 | -41.943802 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c761d31b-2b71-3022-9537-4bc290c6f3c2 | -12.0178 | -43.483002 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9bcd69e7-c2ed-3de3-8f84-e9a341395752 | -5.7374 | -45.134399 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0e8afee-2f31-3d3f-acc5-97cd8341115b | -6.5005 | -44.364498 | 2026-10-10 00:09:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b833f15-45c1-3cfb-b50f-9308d64c5b42 | -3.4822 | -49.5839 | 2026-10-10 00:09:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88d4b18b-2b3a-39ac-a6ef-b462a629a417 | -5.0975 | -46.225101 | 2026-10-10 00:09:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08ab3a10-d7fa-36d8-812e-d07d2b2ec429 | -5.5182 | -43.051201 | 2026-10-10 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b000983-1178-3949-90f5-0ff12ebf17a5 | -16.955 | -41.165501 | 2026-10-10 00:09:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38342ebc-d6c7-326b-8868-0d924b786677 | -4.921 | -45.062901 | 2026-10-10 00:09:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be3a0729-c36c-3ad5-aed5-90b0c198799d | -6.8659 | -45.044201 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41cc6b88-3baa-31a5-9849-d025524484ab | -6.012 | -40.959999 | 2026-10-10 00:09:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fde03211-3a0a-31ff-822d-226dc20a7361 | -5.3372 | -42.933201 | 2026-10-10 00:09:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 70b7553d-57d5-37e5-9767-14f56d391802 | -12.9522 | -44.583801 | 2026-10-10 00:09:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95be04f6-d5c8-38fe-81ab-e80ac9b91a5a | -15.3869 | -41.939499 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79ba949d-ae5c-3fbb-a0ef-0e300266abdd | -12.3575 | -46.614899 | 2026-10-10 00:09:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74d6ddb5-d179-3f6f-9f13-8ad00341e137 | -5.322 | -45.2043 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79dfaf14-950d-3765-bac2-e04648813c0c | -9.2961 | -47.381802 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f53e1dc1-2a52-3a8f-860a-961027643ecd | -6.0629 | -44.6591 | 2026-10-10 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1943f442-7712-3d51-a50f-ce46b1f74e1f | -4.4509 | -47.9258 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e40cc0a-085b-3bf5-907d-e3f839697341 | -4.5047 | -43.621899 | 2026-10-10 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c895431-33c7-33a6-b95f-4b82bb733554 | -6.4927 | -44.375702 | 2026-10-10 00:09:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2a972fd-0790-3a16-8b6e-2e1cd76feb85 | -17.1479 | -41.354698 | 2026-10-10 00:09:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 787e9b69-a9da-3f36-94f1-872c3481320f | -8.9732 | -45.9436 | 2026-10-10 00:09:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 880643ce-3373-3ca6-bd3a-801fbafe7b70 | -11.5665 | -43.719398 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e9550f9-9813-3b8c-a88e-5d0c34fae62b | -5.9951 | -41.383202 | 2026-10-10 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 21ab77ee-ef32-3bf6-854c-b87139bf6b3e | -11.6465 | -43.662102 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a815cb16-b1ac-3976-babc-9cd10995cfac | -17.146099 | -41.346001 | 2026-10-10 00:09:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad680780-9eb7-3242-8344-b706d395a78b | -11.0671 | -44.113201 | 2026-10-10 00:09:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72feb6ed-13f3-349e-9520-31b1ffbb4d72 | -6.6949 | -40.4748 | 2026-10-10 00:09:00 | METOP-C | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8fe6b7d5-5993-345c-a09c-6d63afb2cc70 | -5.6221 | -43.6506 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e8519d4-033e-341a-85a9-aeac147f7653 | -4.9196 | -45.793301 | 2026-10-10 00:09:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a70eea4-c977-3122-bcb7-d83ea4d82a6d | -10.4494 | -47.858898 | 2026-10-10 00:09:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e22fde96-ce74-3223-b11c-5800882815b4 | -8.3224 | -45.006802 | 2026-10-10 00:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d17afd3-48e6-35bf-9744-51fcc780bd88 | -7.0608 | -40.948399 | 2026-10-10 00:09:00 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5bc17158-7b70-3113-8559-e4c73aeb5633 | -4.78 | -42.746399 | 2026-10-10 00:09:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55bf5ae3-89d5-3288-a2db-8fe349fd1ec2 | -6.8615 | -45.024399 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52400368-7f0b-3649-afd5-7c18345064a5 | -13.3532 | -43.906898 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ba3b26d-595e-37b1-a8c7-8f3c354e8b3f | -9.2635 | -47.420601 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e17e5e4-64ac-3fe6-b1c4-32526486939f | -12.3544 | -46.599701 | 2026-10-10 00:09:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bef90c6a-40f2-361c-a661-073f0ee9b7ec | -4.3792 | -49.773899 | 2026-10-10 00:09:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29073c8a-9df2-362f-b0d5-abbbe9d4b9bd | -6.8773 | -43.702499 | 2026-10-10 00:09:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7f6cc80-1a8b-385b-a2ed-63ab75047ffc | -12.8657 | -39.9216 | 2026-10-10 00:09:00 | METOP-C | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d6652786-094f-3ec4-ae82-856df9724015 | -12.0312 | -43.450401 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bac67aed-db55-33f5-a818-510c29718efb | -16.1164 | -46.871799 | 2026-10-10 00:09:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2d15189-9936-3027-9a28-e906ea037cbe | -16.659599 | -40.541801 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b68c09fd-271d-3fba-93e2-2811db107ada | -6.0552 | -44.670399 | 2026-10-10 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f54f6ebd-71b2-31ae-ab76-261382a1e6a1 | -9.2701 | -47.403198 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aced4c52-88f7-351d-ac55-1b4c5c9c7410 | -9.2929 | -47.366501 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e29d2268-1eaf-3f6d-ad66-78fe623e7dad | -11.9901 | -43.449299 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3417d7e0-197d-3454-adc2-f4d57c3e6793 | -15.7384 | -41.565899 | 2026-10-10 00:09:00 | METOP-C | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 55e578bd-a6b4-3cda-acfe-d99eab53045a | -12.0271 | -43.382401 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 144594a6-cc86-3053-9fd0-23fb5300c491 | -11.9627 | -43.465099 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4766bb44-17d9-31d3-8dba-8c4fc8a67f61 | -5.999 | -40.948502 | 2026-10-10 00:09:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5d1747d-af06-3a95-b1e8-9e0e39736f43 | -17.091499 | -41.576599 | 2026-10-10 00:09:00 | METOP-C | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README3.md)
