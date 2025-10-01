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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a986d0d-76f0-3f9e-96fb-f439bb6f4cc4 | -13.70314 | -48.64894 | 2025-10-01 01:09:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 13aaffdd-40e7-39f4-83e8-68554a5571e9 | -15.00961 | -56.04159 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b2ea7e88-7547-338a-aeb1-15a52fdcdcf4 | -17.3966 | -47.18689 | 2025-10-01 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b92a1a12-08ea-345d-8560-d708327ebb23 | -15.17825 | -49.09617 | 2025-10-01 01:09:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 61d52854-c2a8-3813-add3-c74ca5524fdc | -15.17112 | -49.11772 | 2025-10-01 01:09:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 31aa25af-2c7c-385f-94b4-a89c57625964 | -15.84429 | -59.60367 | 2025-10-01 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1838966c-e756-3a8f-8c1d-447f34673b7e | -14.89376 | -48.1127 | 2025-10-01 01:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| eb25723f-f507-3a39-b9cf-82dec233cfc4 | -13.18362 | -50.92631 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 353.4 |
| af7562b1-2630-3bc0-a585-61150704fdb9 | -22.2787 | -46.72811 | 2025-10-01 01:09:00 | TERRA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 6c3165da-6b6d-32e3-ae72-261cd2656ddf | -17.40584 | -47.17904 | 2025-10-01 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| ce16638f-d325-396c-9ecc-d8f1cf4a69d7 | -16.25495 | -50.92306 | 2025-10-01 01:09:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 240.7 |
| 34ccdf00-7644-3e67-a0f9-31fb59393589 | -15.34227 | -56.95734 | 2025-10-01 01:09:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47e073c2-3700-341e-9d4a-683398c69e01 | -21.13339 | -50.38784 | 2025-10-01 01:09:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| dcba358a-98e9-38a4-a0a7-e32b10fa3bf3 | -22.57836 | -46.75989 | 2025-10-01 01:09:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 50de7bad-27e7-3ec4-abb4-1e9b02aac999 | -21.04614 | -45.69189 | 2025-10-01 01:09:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 157.4 |
| e4e1719f-3ae5-321a-877d-d3e6f4235fc3 | -15.83327 | -56.3874 | 2025-10-01 01:09:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e4f889c-1914-302e-abd6-2ad7984eef68 | -21.0395 | -45.69855 | 2025-10-01 01:09:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a95e615a-b5ab-307f-8d6b-cb5c185cd2ca | -13.19063 | -50.96733 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f15f247c-02f3-30a8-a27d-1feba8716cf5 | -14.99096 | -46.98482 | 2025-10-01 01:09:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| bc00bd13-1c97-34c2-8b37-6f043b33d6c9 | -16.25804 | -50.94121 | 2025-10-01 01:09:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| afd62f0a-8b52-3f72-858a-76160dbe83e9 | -18.70235 | -49.159 | 2025-10-01 01:09:00 | TERRA_M-M | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 47552af6-d351-3feb-9d7a-e641b9c77d40 | -14.36246 | -47.15619 | 2025-10-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ae808e18-a3de-3faf-ac8c-7e794f104a8f | -14.98088 | -46.96 | 2025-10-01 01:09:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 151.8 |
| f1cf0a67-d9bb-3625-90b4-a7517668dd73 | -14.9914 | -46.9549 | 2025-10-01 01:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 7e0b8c9b-e6c6-3dad-bf8f-e82a2b82b8ff | -5.8469 | -43.3995 | 2025-10-01 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8fa3a6ba-c7fd-3bda-9954-8d8a85a23e23 | -14.3714 | -45.9172 | 2025-10-01 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 00a48d05-5577-3028-b98c-55801c97aacf | -14.3519 | -45.9206 | 2025-10-01 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a9216596-b7dc-351a-9ecb-fbdb18b7d15b | -11.1523 | -54.3104 | 2025-10-01 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 47fecd28-36b1-3cce-977e-c3ac73e304a8 | -9.2902 | -54.5242 | 2025-10-01 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 97d8aa77-0163-32e1-b44e-9f63d635f9df | -9.9383 | -43.6483 | 2025-10-01 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| ccd6e272-dbd7-3705-92a6-5544c4a0584e | -14.7826 | -45.7981 | 2025-10-01 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 1e8619af-ddd4-3528-9a81-a82315d720ab | -15.9431 | -48.1245 | 2025-10-01 01:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5a09d3c5-7e1b-36be-bf41-3907147052f3 | -13.1966 | -50.9525 | 2025-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 17cc3912-ecc4-330c-b256-f54a87d20246 | -3.0827 | -47.0088 | 2025-10-01 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 72f05696-15a0-34d0-a4d4-528e2bf7b8b3 | -18.71 | -49.1621 | 2025-10-01 01:10:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8745e4bf-fe93-32d2-a2e7-baf0116b528b | -13.327 | -47.876 | 2025-10-01 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a37021fb-7547-36c1-8942-b2b19e6a8b79 | -3.5161 | -49.4528 | 2025-10-01 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2a625fdf-fc3a-3518-831c-c4cf91e70e73 | -13.3467 | -47.8508 | 2025-10-01 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e4b7146e-d14a-3c0d-a973-91fec295b611 | -14.3719 | -45.894 | 2025-10-01 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ed1476d2-8e02-33a1-a545-41973ce930bd | -9.938 | -43.6718 | 2025-10-01 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 2a7ce047-6261-306f-885b-ee3726f89772 | -21.0572 | -45.6638 | 2025-10-01 01:10:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a8be74d9-32ea-3222-b3b0-b32598a84da7 | -16.2562 | -50.9275 | 2025-10-01 01:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 255.7 |
| 799dd4c3-f383-3961-bc16-4a7d959ae435 | -13.1969 | -50.931 | 2025-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 268.5 |
| a1ff9328-4ff7-324f-a2a7-809962bec4d0 | -14.3524 | -45.8974 | 2025-10-01 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c24339d3-f0ac-3129-9bc3-62c179aee1b5 | -13.1777 | -50.9335 | 2025-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 438.0 |
| 0cef0c10-bd71-3fac-80fa-f53a293cd0f5 | -20.6103 | -46.2098 | 2025-10-01 01:10:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a8f19a25-d018-391c-ab03-2f71ec04c63b | -15.1611 | -49.1042 | 2025-10-01 01:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9beec0ef-99cd-3ca6-915e-3eb9ef78e762 | -16.2558 | -50.9494 | 2025-10-01 01:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 26e02ec1-fd6b-3f84-8c60-227e4670d5fe | -12.8394 | -50.5471 | 2025-10-01 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| be38e97c-9cb7-3289-8f98-990e402efbae | -9.4396 | -54.5537 | 2025-10-01 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2a9fc41e-3167-381c-9275-284273456055 | -13.3463 | -47.8732 | 2025-10-01 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| e4db8524-1a2d-3697-9d17-585f3decf715 | -14.7831 | -45.7749 | 2025-10-01 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9300757c-3f72-349b-a0ca-f83ecba99ad2 | -13.1774 | -50.9549 | 2025-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 9c22db8e-57c6-3eaa-bdec-c9d37f0782ae | -8.5079 | -47.2897 | 2025-10-01 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 0979e331-c5f1-35ca-9b1b-4aeead43f0e7 | -9.4394 | -54.5739 | 2025-10-01 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| bb1979fb-bddb-3237-8fe7-768206d72000 | -9.3089 | -54.5229 | 2025-10-01 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e98ca00d-a254-39b5-9424-d4e0869ac926 | -16.2366 | -50.9306 | 2025-10-01 01:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d5d4aef1-0dc0-36d3-bdae-59851bf6a4b4 | -12.8202 | -50.5495 | 2025-10-01 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 66758d5e-6849-3bea-9637-ca5bf72889e6 | -12.839 | -50.5686 | 2025-10-01 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| b089cebf-9aab-391a-9ec4-63c46c175425 | -5.8657 | -43.3981 | 2025-10-01 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 282787e5-a49f-311c-9e9f-a6a73dd302eb | -20.6309 | -46.2046 | 2025-10-01 01:10:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 6bb4da6a-7d5d-3e21-a996-8bd0768392f5 | -3.1013 | -47.0082 | 2025-10-01 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 00a3e933-e193-3d27-8492-a3f474f6c4b7 | -15.1806 | -49.1011 | 2025-10-01 01:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c623a773-2bb5-3ac5-bf1e-ffb33356c7bd | -13.3274 | -47.8536 | 2025-10-01 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 57fd3d30-b8b8-3182-919c-93f1a22b54a4 | -12.8198 | -50.571 | 2025-10-01 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 74b01fe1-7ad6-3d85-9391-89c67e0f856d | -12.4625 | -50.2068 | 2025-10-01 01:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a4a1b46c-da13-39e7-aca3-2436ec22e658 | -9.9189 | -43.6743 | 2025-10-01 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 96206818-e992-3b89-9109-056e62a789dd | -8.5267 | -47.2879 | 2025-10-01 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8d94850f-1668-3bf2-a1da-87a89a3ce70a | -15.9234 | -48.1279 | 2025-10-01 01:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 55.8 |
| abc21b15-6e9e-3855-82c1-6eb3228047dc | -3.4762 | -50.0883 | 2025-10-01 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| a219891b-5edf-3b9a-b26c-40c38360bb46 | -11.43526 | -55.04858 | 2025-10-01 01:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2fd5f78a-8a17-3957-854d-e442b0d9ede6 | -12.92606 | -54.73064 | 2025-10-01 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dd7f5c69-69c7-3e93-bd01-6d630986ffca | -6.95878 | -63.1029 | 2025-10-01 01:11:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3aad2fb2-c69d-390e-988b-590c06395ba6 | -6.9481 | -63.10431 | 2025-10-01 01:11:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 24c1cd12-3bb7-3485-8a23-9f233ed98af3 | -11.15328 | -54.12505 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 5e2e9c83-f47d-3233-ad86-9786c3574eca | -9.58659 | -54.6013 | 2025-10-01 01:11:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| db7fba86-f575-3d85-bce5-564b4ba3b341 | -8.9232 | -51.6544 | 2025-10-01 01:11:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 049b6d6d-720f-3238-97a2-2a7fda6544a1 | -11.95875 | -50.5253 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 74a8573a-a4d1-3c4b-8d80-eabce4bf7fca | -12.8365 | -50.57177 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 299.0 |
| 9debfc93-04f6-3ff7-8a31-67e21fd29e28 | -9.07535 | -48.03 | 2025-10-01 01:11:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 853b7e24-522e-31b3-9001-41aa41723235 | -9.3002 | -54.53454 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 3bda8660-d81d-3393-b0e9-eec51c8f229e | -9.30873 | -54.52006 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| e9c49050-a935-32de-880c-43c412cae4a3 | -9.42575 | -54.5683 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 97730c0f-4464-30bc-98ca-556af9e9aa19 | -9.58468 | -54.58849 | 2025-10-01 01:11:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ce5377dc-af49-3c52-9a98-6c839049bd44 | -9.29829 | -54.52171 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| c34cd57d-fc62-3922-b2ce-5a15e9970e45 | -9.35997 | -54.53233 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 40c8ba32-e6fc-386b-a500-16f4d86eb186 | -11.14259 | -54.31349 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 584e9981-c942-3ff1-8068-8f2113923ad6 | -12.43888 | -50.18242 | 2025-10-01 01:11:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b8be04d4-b1b3-3240-9724-a8c322457d35 | -10.92966 | -54.33442 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 386d8f4b-534c-3625-a2c7-e4ae12000277 | -11.48298 | -54.6073 | 2025-10-01 01:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 038782b1-46a0-3315-a2f9-2ec6affd6568 | -8.39988 | -50.12495 | 2025-10-01 01:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b82e1ef6-080d-3a88-a07a-e6b680bb9a8b | -12.82317 | -50.57418 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 132e38b9-1bc2-3ecd-94c2-fb3923aeb2d3 | -12.82278 | -56.55094 | 2025-10-01 01:11:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 68cc63eb-7360-3e77-8dcf-2461223452e4 | -10.29512 | -50.47997 | 2025-10-01 01:11:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 2ed41202-88ab-3eb6-8655-03f25f8fc4c2 | -11.43688 | -55.05968 | 2025-10-01 01:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f48780d5-7428-3f97-af87-2506544a59ec | -10.89037 | -53.7583 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1ca9177b-571c-3b9b-9638-bd6ae3509dd5 | -9.28783 | -54.52325 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 583630d7-7715-3929-adb5-b0ea28bad5db | -9.42768 | -54.58081 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1e18c29b-6373-3f66-b20a-5780041d12a3 | -10.20377 | -53.87573 | 2025-10-01 01:11:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 95420f33-1db3-37a6-b0d6-83813a27d90b | -9.43006 | -54.57399 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |


[Clique aqui para ver as próximas entradas](README7.md)
