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
| b986dc2e-dffb-3e8c-b979-10787110c13d | -18.4193 | -42.8592 | 2025-09-22 00:10:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| c0ead438-2ed5-3750-9d65-596490414096 | -18.3998 | -42.8395 | 2025-09-22 00:10:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 151.8 |
| 6d25d008-4d61-3cc1-9c4a-72ee6a80d669 | -18.399 | -42.8644 | 2025-09-22 00:10:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.2 |
| 570fe4cd-67e4-3e34-bb1e-f7b5d41dd3ea | -20.2533 | -55.5172 | 2025-09-22 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 3fdc3e47-21cf-348f-9ddf-8cdd58bea029 | -10.4129 | -46.142 | 2025-09-22 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cc3b99bc-fe72-3a68-a5a5-68726fda0e55 | -10.4132 | -46.1194 | 2025-09-22 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 71b00b64-9cbc-3b29-a28a-93494eff0222 | -22.9262 | -48.1581 | 2025-09-22 00:10:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ba1205dd-cc78-3f7d-8abc-45050264b68f | -6.9024 | -44.7656 | 2025-09-22 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1ae13ded-bf89-3403-aa89-26ba803ffb77 | -15.9969 | -59.4651 | 2025-09-22 00:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 4da9697d-449c-3e7c-8c52-584d51c15f7c | -10.3752 | -46.1241 | 2025-09-22 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 76f8521d-1a7b-3a99-937d-208d93e5d541 | -18.42 | -42.8343 | 2025-09-22 00:10:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| b54c73db-21e2-3eeb-83c3-f9424334d235 | -21.1889 | -48.8377 | 2025-09-22 00:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.6 |
| 97b43248-3eb9-3e5e-bcc1-6fe5a06d864e | -4.3197 | -48.0908 | 2025-09-22 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 0f9a53c4-4eb3-331c-b026-baee33519178 | -20.2735 | -55.5141 | 2025-09-22 00:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 9f3fc6dd-ce27-3104-a581-3b96b3c8150e | -11.6249 | -52.8416 | 2025-09-22 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 01012f89-9eb6-3728-8644-aa763fe6d221 | -10.3755 | -46.1015 | 2025-09-22 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c7035fab-f350-345f-a885-bae54661bb5b | -20.274 | -55.4927 | 2025-09-22 00:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 3ee7f858-ce50-38a5-9747-f020220c9bdc | -20.2942 | -55.4896 | 2025-09-22 00:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e7ba92bf-9fd9-3b20-acf9-5c84a7eb7b3a | -22.9255 | -48.1819 | 2025-09-22 00:10:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 162.0 |
| e38d964a-5e7d-3892-a17b-b3470285ccfc | -11.6247 | -52.8624 | 2025-09-22 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| a7cb4f6e-bdb8-372f-a56f-3fc313eef3bf | -11.322 | -54.3359 | 2025-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 3a8a8f66-de42-3f0b-b617-1d945c8d4da3 | -4.3012 | -48.0917 | 2025-09-22 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3b42b224-74e5-383b-ab97-7b8cbdcf0dc2 | -10.4322 | -46.117 | 2025-09-22 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ca894a89-7096-35b0-acd4-398222bc152c | -21.2095 | -48.833 | 2025-09-22 00:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| 66b7a0fc-7b96-3824-955e-89f2c028198e | -11.3217 | -54.3564 | 2025-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 8a4bcead-62a1-34b0-816b-b6b9ebb566b3 | -7.6596 | -61.1297 | 2025-09-22 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 84265806-140d-3513-b099-7e49cf9965f3 | -20.2537 | -55.4959 | 2025-09-22 00:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 920fbef0-f3b6-36e7-8e1e-a9ea3c55d0db | -21.2102 | -48.8098 | 2025-09-22 00:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| 6c4423a2-dbf7-3baa-9048-1ae7469a6587 | -10.3565 | -46.1038 | 2025-09-22 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e59ff14b-574f-3227-9176-10ea2075f68d | -7.6597 | -61.1106 | 2025-09-22 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 9fb1ea0e-9b33-3688-bf78-6fbe8c3b01e1 | -22.9044 | -48.1873 | 2025-09-22 00:10:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 127.8 |
| e0f24da0-3c89-3717-b1f5-d391c97f10a4 | -11.6436 | -52.8605 | 2025-09-22 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 1fad1032-8ae9-35c6-acfd-bebc5d77e7c3 | -20.2744 | -55.4714 | 2025-09-22 00:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4da9a74f-0b11-3f82-985e-6772e956e9e5 | -7.95973 | -43.88982 | 2025-09-22 00:11:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 03da37bf-255d-3607-8773-d6cea1ea10c4 | -10.41959 | -46.12808 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 3098ed29-c7eb-3ab2-a49a-5c06780b0936 | -10.42941 | -46.12663 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 11feada6-60f3-390c-9d9c-ce521fd2fd18 | -7.47602 | -44.39344 | 2025-09-22 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3f08b5d7-a6b7-3252-bce7-9a2127d96c9d | -11.64498 | -52.87158 | 2025-09-22 00:11:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| cd95af25-c844-3401-aaa6-1bf3ecc15584 | -13.73966 | -43.78886 | 2025-09-22 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 410a9d90-d99e-311e-a917-bd060848acbe | -15.09683 | -43.8301 | 2025-09-22 00:11:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 40825e44-0832-3af9-a3ec-49ae5bf06f86 | -11.65805 | -52.87695 | 2025-09-22 00:11:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| da68a48a-5689-37a6-a2ba-b61aeaaf4423 | -13.85257 | -40.94877 | 2025-09-22 00:11:00 | TERRA_M-M | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 47ab68cb-9eb2-3555-acc1-ce41232a3c13 | -14.98516 | -42.24014 | 2025-09-22 00:11:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 17a90cd8-911b-3a76-acae-8b8ca3c139a6 | -7.60964 | -44.43201 | 2025-09-22 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bff72935-8567-329e-aead-77165166b739 | -13.75013 | -43.7294 | 2025-09-22 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ea3c1066-e334-3264-bbc1-ed1bca40b50a | -8.34775 | -44.7044 | 2025-09-22 00:11:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 877090ae-4790-3edc-9548-84783f3f0266 | -8.34651 | -44.6953 | 2025-09-22 00:11:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b43a386-f284-36db-ae3f-023bf6782923 | -11.99398 | -47.20056 | 2025-09-22 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fc9114dd-861e-3251-ba67-04196573b58d | -10.33567 | -46.11109 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 92d6dd60-f69f-334b-b248-c9b243157d37 | -12.98015 | -46.37529 | 2025-09-22 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 79018bee-138e-336d-b121-46d637af3ba2 | -9.70146 | -47.63576 | 2025-09-22 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 80bd85af-3ffb-3b11-9281-e5da1ab4a017 | -7.94489 | -44.10885 | 2025-09-22 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9846649-97db-322c-aee5-50a2dc4beb38 | -10.46073 | -44.18653 | 2025-09-22 00:11:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5951c73a-caf3-33c8-8567-8197a557ca11 | -14.73288 | -46.83509 | 2025-09-22 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1ae8be2e-4018-30ec-9799-d402e6fea0e9 | -10.41857 | -46.13404 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| d02d8411-f204-360e-8218-9c294e1f0288 | -7.93354 | -44.10726 | 2025-09-22 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8fa9835f-7ffc-3b74-b5c5-3708ab5fcc04 | -9.99592 | -46.24957 | 2025-09-22 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9db4ac8f-15a6-3d4d-8a44-5de5804c8f31 | -14.23237 | -44.3266 | 2025-09-22 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2f520d97-715e-3348-9b1c-a0deaf2fa158 | -10.37632 | -46.11682 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| a527cfd5-b8e5-3108-a6c8-bcabf872ff0d | -10.32444 | -46.10123 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e8fd346f-d5f8-3da0-98ec-2a493b015b14 | -10.30639 | -46.13259 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9ab0d602-30dc-3961-a529-4807b3f6f62b | -10.50703 | -44.05826 | 2025-09-22 00:11:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f51e55ab-2f46-3b47-a16f-8f0566e8449d | -13.72757 | -43.90678 | 2025-09-22 00:11:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6c5e2e35-ff8a-305e-a421-961e5fae1d39 | -14.69034 | -48.77307 | 2025-09-22 00:11:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 52ff9912-d12a-3c06-a994-4a34721dd4a1 | -9.74117 | -45.95629 | 2025-09-22 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4af5f947-f802-350f-81bf-3bbb4ae7d255 | -8.76868 | -46.1774 | 2025-09-22 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7d12ca9-f6e5-3c40-9021-aea26ccf6b74 | -11.23011 | -46.16814 | 2025-09-22 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e370436c-8d41-323c-a8c1-b2137b13b329 | -11.47033 | -46.93975 | 2025-09-22 00:11:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0d2118e0-0c97-30a9-bac7-6a597437ce73 | -10.5932 | -46.45108 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2691751a-b578-30f6-a6b2-585dcb9c7884 | -12.97136 | -46.38933 | 2025-09-22 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2cf45661-ac16-30ea-93dc-4a0240546294 | -10.40874 | -46.13541 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 2ad39d86-b32b-3f2e-800b-65eaeeb65d51 | -15.96197 | -50.37344 | 2025-09-22 00:11:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9b0253c9-8a87-3f8e-bdc7-2a5b3dd32914 | -13.3771 | -44.31399 | 2025-09-22 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ba4b977-7138-3193-aadd-79f95b6bb00c | -11.22013 | -46.16938 | 2025-09-22 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6708ecb8-d381-3210-90d4-602f98a4bb4d | -12.1013 | -39.95238 | 2025-09-22 00:11:00 | TERRA_M-M | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f5060f15-71af-3b3f-9dc1-b5f3f3dff542 | -8.40298 | -40.85322 | 2025-09-22 00:11:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 888877c8-fe12-33ee-b07c-bb2d7345e0bb | -10.37779 | -46.12807 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 76af574d-723c-303e-8668-32dafa39ea46 | -14.73177 | -46.84096 | 2025-09-22 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5dce3847-0c7c-36c2-873b-d00ed8e225c3 | -11.637 | -52.84068 | 2025-09-22 00:11:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 01e216f9-ee36-3590-bbd1-f1b26cc5cab8 | -11.64112 | -52.83357 | 2025-09-22 00:11:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b3aad2d3-fe08-3cb2-82c3-0a4dac2a9058 | -14.07834 | -50.15588 | 2025-09-22 00:11:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 32e1aa3d-1ddc-3040-b2e9-0894f1a3c7e1 | -7.94246 | -44.09109 | 2025-09-22 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f229b7ad-8610-3644-8f84-800aeed00b7b | -11.64112 | -52.87875 | 2025-09-22 00:11:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 6664a4de-df80-3b54-ad4f-ff8edd928627 | -10.31474 | -45.238 | 2025-09-22 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ad7de12d-a6ed-3cc4-b78f-9ac6b0be0575 | -10.42005 | -46.14525 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7a3c1428-6abd-3f62-aba9-9c206ba71814 | -9.47658 | -40.3604 | 2025-09-22 00:11:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 2f068ff8-bd31-3792-b0cb-e093c855519d | -15.09811 | -43.83994 | 2025-09-22 00:11:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 53d40a57-ec7d-3896-9287-e9f52948ffe0 | -13.9631 | -44.42884 | 2025-09-22 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 49ec15b8-8447-3199-bfd3-ea19c6b914a0 | -10.42102 | -46.13934 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 88c45e6c-946f-38d1-8ba3-f8be4f9243fd | -14.9721 | -44.40915 | 2025-09-22 00:11:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52e66c0c-b4b3-3fd2-9a4b-d813ea0abdc9 | -9.99741 | -46.26113 | 2025-09-22 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cd01a1fc-575e-3f96-a5fc-5797971a26ce | -8.85822 | -46.1592 | 2025-09-22 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9021d68d-535a-3704-a8c1-0d99dedc313e | -13.7384 | -43.77937 | 2025-09-22 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 7bf292a6-9d72-3af9-8785-f46e3bca0078 | -10.36798 | -46.12948 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c11552ee-f5db-33a3-859f-2006b3ee0bca | -8.80868 | -43.02362 | 2025-09-22 00:11:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7798ff5e-9cde-3460-bc20-74ccd2a4ccf3 | -10.39151 | -46.0805 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0709e589-138d-392f-ae15-29f86461a2d1 | -7.94367 | -44.09997 | 2025-09-22 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e86c0a04-41c8-35e8-ad8e-27389189e789 | -10.40322 | -47.85015 | 2025-09-22 00:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 1ebef90f-2ead-3649-aed1-0d5779fd8e05 | -7.96095 | -43.89865 | 2025-09-22 00:11:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1143c1c8-2bac-3c64-8d24-ff34a057a37e | -10.5947 | -46.46281 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |


[Clique aqui para ver as próximas entradas](README3.md)
