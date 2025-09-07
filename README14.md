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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9637aa9d-e34b-3a42-be76-828332086cea | -9.4495 | -62.3675 | 2025-09-07 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 639acaa9-ca21-31e0-9d40-49f61f015be6 | -7.7591 | -48.8189 | 2025-09-07 00:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f3262fae-9385-3887-b0df-219cb94d0f00 | -11.408 | -43.6283 | 2025-09-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 5192e5b7-3745-327d-9cc8-f192ee29af71 | -9.5156 | -40.3061 | 2025-09-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.4 |
| d862981c-956e-3ac4-86a5-20bbfae5aa2d | -17.3844 | -42.6235 | 2025-09-07 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5f8b0728-11b3-3f4d-8893-9d0d023687c2 | -11.2194 | -55.0178 | 2025-09-07 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1513f4a4-dacf-38c6-a240-31995d821358 | -6.0086 | -44.1513 | 2025-09-07 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e78eaeb2-878f-324f-8352-2d061769f204 | -9.4311 | -62.3493 | 2025-09-07 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ead81f38-bf5a-3457-8acf-cb296e37832d | -17.2375 | -46.6921 | 2025-09-07 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7ad5678c-4c03-30aa-ac52-7cc291479301 | -9.5347 | -40.3033 | 2025-09-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.3 |
| f427193d-d796-3fff-beef-a857ad970e02 | -5.9896 | -44.1758 | 2025-09-07 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e8300e7d-9985-343d-941a-0d8045b4c98c | -11.4076 | -43.6519 | 2025-09-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 583d4e04-5315-36ba-ad4b-86f1821d72da | -5.9899 | -44.1528 | 2025-09-07 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 8a48381a-2df7-3ace-bb5b-41f06fb365c6 | -17.237 | -46.7154 | 2025-09-07 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 5c7f59ba-5e21-38c9-a1a6-49ba9423875f | -6.8281 | -52.8143 | 2025-09-07 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 604f7da0-11fd-3848-a850-618bb4309730 | -10.3932 | -44.959 | 2025-09-07 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e3bf2927-7782-3975-b7de-100c3dd2e291 | -9.2971 | -66.6215 | 2025-09-07 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 651751bd-fd09-3e64-8268-74e9ed29df8e | -10.6128 | -44.3284 | 2025-09-07 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9e01e7bd-1f64-30e1-acde-28bfb7c7bbdb | -11.4272 | -43.6254 | 2025-09-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| edc5d13e-540b-3243-829b-b3f8629fe08c | -13.781 | -52.7688 | 2025-09-07 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8feb8f94-f8f9-3660-a7bf-7e5234abc909 | -5.9901 | -44.1297 | 2025-09-07 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 33cb2ab6-8389-3802-aa02-e151dada8469 | -17.3636 | -42.6532 | 2025-09-07 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e6ea2644-e14f-336b-9020-561b66af6349 | -17.3643 | -42.6284 | 2025-09-07 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 0f09efce-b0a7-331f-96df-4f3286a3fc09 | -1.9484 | -56.5868 | 2025-09-07 00:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| fd05f503-15f9-332d-a003-77ea12a4d387 | -19.8853 | -57.9031 | 2025-09-07 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| f85e3e77-95c6-3488-b2e9-36161acb2009 | -3.581 | -47.5149 | 2025-09-07 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b66d4f6a-2ea5-35bf-ab1c-84ec2c83f8bf | -22.4278 | -47.4346 | 2025-09-07 00:50:00 | GOES-19 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| b240ef5a-41f0-32a8-94d0-a3d152832642 | -13.8213 | -46.2631 | 2025-09-07 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f5662567-4ad2-30d4-a8b2-9b7a78437124 | -9.4309 | -62.3683 | 2025-09-07 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 111.1 |
| b162b539-a7c5-3c5d-8352-3cf84d0729a4 | -13.8407 | -46.2598 | 2025-09-07 00:50:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| fb8869e3-ceb1-36ee-9d45-7089e9e0adf9 | -17.3643 | -42.6284 | 2025-09-07 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 882401fe-53c8-3d96-ae75-bdf88600479f | -17.6785 | -43.5334 | 2025-09-07 01:00:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3fc094ff-5e98-35cd-843f-126fb8c4c4f2 | -2.4263 | -49.3161 | 2025-09-07 01:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5fa64f6b-e61a-3e3b-a4f3-f7c9c8877764 | -3.581 | -47.5149 | 2025-09-07 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 86cc3891-644a-3c9b-b9a9-f79632aeffb8 | -17.3636 | -42.6532 | 2025-09-07 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1d0d60a0-1e8f-32a2-94b3-a6950a5a5259 | -9.4309 | -62.3683 | 2025-09-07 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 857759ef-6abf-37f6-b721-279dc4dde16a | -7.7404 | -48.8204 | 2025-09-07 01:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2c2ceadb-54f0-3618-a5ee-0e8313fa82d4 | -11.2194 | -55.0178 | 2025-09-07 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b7bb005a-0c21-393b-ac97-73c8359be222 | -9.4311 | -62.3493 | 2025-09-07 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e4b3e2bb-2cdb-3548-a68e-5cb124dd38be | -17.0209 | -49.1667 | 2025-09-07 01:00:00 | GOES-19 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f4203b8b-d503-31cc-ad21-7cef14b80c2c | -5.9901 | -44.1297 | 2025-09-07 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 07e5348e-bd8d-3103-9e48-b0ca317bbbb9 | -11.408 | -43.6283 | 2025-09-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 10e633fd-0e05-3f70-a671-ac8a5f97bb77 | -6.0086 | -44.1513 | 2025-09-07 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| fb80c771-625b-3b50-a212-8a7128ae595a | -3.5995 | -47.5142 | 2025-09-07 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| eb77459c-54bf-357c-9db4-ff11b6fdea80 | -7.7591 | -48.8189 | 2025-09-07 01:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 34ea4e53-20f0-377e-90f6-209a1c259689 | -5.9899 | -44.1528 | 2025-09-07 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 188.3 |
| cc4ee8ec-7077-3d7e-b1d7-d351884368ad | -10.3932 | -44.959 | 2025-09-07 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 57e161be-6b1a-3ffe-b9b7-d6ad23ac426c | -17.3844 | -42.6235 | 2025-09-07 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| fdbfa79f-39ea-39f6-9dbe-50f12befb250 | -1.9484 | -56.5868 | 2025-09-07 01:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8b829577-5b36-36ac-91b8-966fe24a56fb | -9.5347 | -40.3033 | 2025-09-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.4 |
| d5faab3f-22b6-3a20-9a64-c3a63e660d56 | -9.4495 | -62.3675 | 2025-09-07 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6a9a646d-b69c-3e42-b5ac-53f34ffdddb5 | -6.8281 | -52.8143 | 2025-09-07 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6660290c-8542-33df-aba8-29237c5a3497 | -11.2194 | -55.0178 | 2025-09-07 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4cab94d2-7c93-3e4f-a6f2-af860c84bcda | -17.3844 | -42.6235 | 2025-09-07 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 1fca1514-c4d1-31ef-b4bf-e510c38bf106 | -10.6128 | -44.3284 | 2025-09-07 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e2c9e368-7915-3de0-8184-f34aa55c0ba6 | -17.3643 | -42.6284 | 2025-09-07 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 0c6d3ccd-c6c6-385e-b79a-207758146779 | -6.0086 | -44.1513 | 2025-09-07 01:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 3c47c114-6753-35d4-b983-582543c9bb25 | -11.408 | -43.6283 | 2025-09-07 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| d17f0f0c-b54a-30b3-b78e-8efd909a1136 | -21.7102 | -47.1919 | 2025-09-07 01:10:00 | GOES-19 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.3 |
| 183ce2cc-f958-353e-90df-9dfbd385adb5 | -6.2036 | -43.3709 | 2025-09-07 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1f8fc7ca-bcf0-3bb1-afde-fe069769f7aa | -9.4495 | -62.3675 | 2025-09-07 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ed0b81c6-1137-3a25-be28-340a4a26e194 | -5.9899 | -44.1528 | 2025-09-07 01:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 172.8 |
| b1cc46f2-8fa1-3005-8933-1cbced400f63 | -2.4263 | -49.3161 | 2025-09-07 01:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c1d6a03e-7020-34e3-a8c7-e65754bd6060 | -7.7404 | -48.8204 | 2025-09-07 01:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5a9d22fc-7a13-3e21-95f2-a6249452a9b2 | -9.4309 | -62.3683 | 2025-09-07 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 106.0 |
| b8508d1a-4bf4-35f5-b367-e0bb4bc71822 | -5.9901 | -44.1297 | 2025-09-07 01:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b4e48be9-c8fa-38c3-97e1-5e5ac6f8f396 | -3.581 | -47.5149 | 2025-09-07 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| f59ef383-6c0d-3350-95cd-ecc20285102c | -3.5995 | -47.5142 | 2025-09-07 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| ea869c4f-5ce6-36db-b436-f6982595c98a | -17.3636 | -42.6532 | 2025-09-07 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9665eac9-872e-3b76-b2fc-28a8f6793029 | -7.7591 | -48.8189 | 2025-09-07 01:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7e00b07e-402f-3bd8-b2ff-b214865b8d50 | -21.6894 | -47.1971 | 2025-09-07 01:10:00 | GOES-19 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 8a139301-383f-30e3-a11a-bb7b69000c8a | -6.2036 | -43.3709 | 2025-09-07 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e8163930-21ae-307c-b7aa-d4e6ec3c5bb4 | -5.9899 | -44.1528 | 2025-09-07 01:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| a04f5c73-6e9b-32a7-be07-975e79a1c3ce | -6.0086 | -44.1513 | 2025-09-07 01:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| fa856df8-08c0-3201-8435-196558f3219d | -17.3844 | -42.6235 | 2025-09-07 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 7a931049-eddf-3423-b636-cd57cbc1c077 | -9.4309 | -62.3683 | 2025-09-07 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 103.9 |
| ce50a7b1-d8b0-33ca-9386-9341670e813a | -11.408 | -43.6283 | 2025-09-07 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 00a1b1f0-6c92-37b4-8165-e77d7af89c99 | -21.6894 | -47.1971 | 2025-09-07 01:20:00 | GOES-19 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| fe998d9f-b1c4-36ab-b42a-0346c455709a | -3.581 | -47.5149 | 2025-09-07 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| cf07ac6c-121d-3d8f-8583-58337c8deae2 | -7.7591 | -48.8189 | 2025-09-07 01:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ba3a67c3-f4c8-3019-b584-b1b398a4134f | -3.5995 | -47.5142 | 2025-09-07 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| ac6cd2d7-afda-35b2-aeae-29aee0dcd694 | -17.3636 | -42.6532 | 2025-09-07 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c3cc2e32-2dfc-3ccf-9a40-07e53f50c31b | -17.3643 | -42.6284 | 2025-09-07 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| c8a2ba5f-0e44-3c41-8a02-77e8a2c2e942 | -9.4495 | -62.3675 | 2025-09-07 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 16086537-ebfc-3e42-8afb-314be4414ff3 | -7.7404 | -48.8204 | 2025-09-07 01:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7eaa3420-86dd-3113-808f-97bf23f08876 | -2.4263 | -49.3161 | 2025-09-07 01:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c648fd37-615d-3402-82a5-8dacb5d5000e | -19.4695 | -47.7691 | 2025-09-07 01:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 187b5966-731a-39b5-9b9e-52a732f1140f | -19.4898 | -47.7646 | 2025-09-07 01:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 77f8cc15-e8e6-3c03-a120-7b57b9e37150 | -5.9899 | -44.1528 | 2025-09-07 01:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 272.8 |
| ed5dfe10-46e2-3d15-bf59-7be78ebfd9c4 | -6.2036 | -43.3709 | 2025-09-07 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e671de5d-0c94-3ab3-80ae-360d255c8229 | -3.581 | -47.5149 | 2025-09-07 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0ba90c8e-fc52-33f8-bb2c-397a4f974682 | -10.8066 | -47.7256 | 2025-09-07 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 54b827a4-1f08-3a0a-93d0-49a5f6f3a27f | -17.3643 | -42.6284 | 2025-09-07 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 93820b5d-c283-3f4c-8f5a-e97e8a812e16 | -19.4898 | -47.7646 | 2025-09-07 01:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 93050192-b24d-3aa5-a0e3-e0f660587574 | -9.4309 | -62.3683 | 2025-09-07 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 107.2 |
| f221500a-760d-3f6b-8dff-1df7b42f07d6 | -9.4311 | -62.3493 | 2025-09-07 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 0c37ffd6-5b34-32df-9ef6-1c50e4b4c481 | -6.0086 | -44.1513 | 2025-09-07 01:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 98c4aa87-657e-396b-bd93-82448c86449f | -7.7591 | -48.8189 | 2025-09-07 01:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a7e4ecf3-d3b4-3c21-899f-a87fa8cc1b09 | -11.6149 | -47.1563 | 2025-09-07 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 351b13a8-bc71-3708-bc7a-9bde44183e24 | -7.7404 | -48.8204 | 2025-09-07 01:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 76.1 |


[Clique aqui para ver as próximas entradas](README15.md)
