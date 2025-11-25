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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4489c69a-9c26-3862-b354-ae58517a2f01 | -3.45051 | -40.2189 | 2025-11-25 11:57:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 98e83fbf-1f4d-3498-a0d3-ce5d66c8c3b8 | -4.59816 | -44.88112 | 2025-11-25 11:57:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b01ee486-47e7-3f1e-acaf-eb3d83f9abe1 | -3.83392 | -40.5668 | 2025-11-25 11:57:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 8c2dd3cc-86cf-34ce-b4c0-9f67026621e5 | -3.77876 | -44.049 | 2025-11-25 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fae0828c-155e-3a72-9373-cdddc92f9b9f | -4.55243 | -43.30021 | 2025-11-25 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6b2dcd5b-586a-3747-ab6c-bd02b4dbe1d7 | -4.53181 | -40.327 | 2025-11-25 11:57:00 | TERRA_M-M | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 17859def-4f2b-3928-9b53-e584414c9f3f | -4.82826 | -43.8186 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 2c70f978-6760-3f5c-82d5-276bb7e5d1e8 | -6.21855 | -43.26928 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ec5664ea-5f93-3e51-a715-c7919be6beab | -6.68282 | -42.47703 | 2025-11-25 11:57:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 6089128d-d5fb-39bd-887a-57d32efcf04a | -3.72588 | -42.75505 | 2025-11-25 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 60725a49-67c4-3f95-9c92-95872dfdad41 | -6.99964 | -43.1596 | 2025-11-25 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d9cab876-da04-3cc0-af3e-732e4abf83a2 | -4.56253 | -43.29263 | 2025-11-25 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ff7b7fc3-94ad-303f-b61c-00caff1f7123 | -4.07074 | -43.56393 | 2025-11-25 11:57:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9bc9028d-acc6-35ff-80f4-4212a28cb91c | -4.01071 | -41.80218 | 2025-11-25 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7f353196-974f-3374-9400-ab22ea7641ce | -2.88068 | -44.00281 | 2025-11-25 11:57:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e934a731-a015-3026-9e56-de6fd0b1db5a | -7.18335 | -41.93123 | 2025-11-25 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| e73eebf7-a0d7-35be-91be-f95aa49929a8 | -3.55511 | -42.07829 | 2025-11-25 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 3cec8147-2b1f-3458-b2f7-5b6c52909f9b | -2.58656 | -43.8034 | 2025-11-25 11:57:00 | TERRA_M-M | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c690c080-325f-3ca1-ac73-8f00de4960b1 | -4.01997 | -42.44865 | 2025-11-25 11:57:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| edad3e68-8632-37c1-84c5-f107008ec214 | -7.76161 | -37.77668 | 2025-11-25 11:57:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 6cb2bda7-fa2e-31c4-a340-999ce99be04d | -3.35949 | -42.15514 | 2025-11-25 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7bea9c30-ce76-397c-a936-77478ea08967 | -3.48168 | -41.29996 | 2025-11-25 11:57:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 524ef2fd-3429-354b-adf1-e4946fd1ca61 | -5.25022 | -41.25312 | 2025-11-25 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f986b6aa-bc17-31d0-ae5a-33251994961b | -3.83335 | -43.99059 | 2025-11-25 11:57:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1db2d595-284a-3830-871b-5ea4605b54c8 | -6.68427 | -43.94077 | 2025-11-25 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9a4e17d4-6e54-3c69-931e-e001efc7216a | -2.92498 | -40.86811 | 2025-11-25 11:57:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 96b70fbb-f2e6-3356-8d42-866110477736 | -9.33201 | -36.95747 | 2025-11-25 11:57:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 75.9 |
| dff893f3-1d14-3bf3-9653-4aea7d7dbb8f | -2.92364 | -40.87746 | 2025-11-25 11:57:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| a6f04de1-c69b-3924-bb0d-9d4dfa2cd351 | -3.51105 | -42.13495 | 2025-11-25 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 538a47da-0081-3388-8703-ea82ba76f7e8 | -2.8544 | -43.28789 | 2025-11-25 11:57:00 | TERRA_M-M | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69909b45-65b2-3c9c-bf3e-837ced7a2f36 | -7.18466 | -41.92193 | 2025-11-25 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a09b182b-45d9-39c5-a328-b9db79e17146 | -6.10152 | -41.68965 | 2025-11-25 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 4306c38a-51ba-3e37-a7b0-23013bb70cf2 | -4.01197 | -41.79326 | 2025-11-25 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 706494f0-54e0-3839-8117-f2574863af0e | -4.65229 | -39.09607 | 2025-11-25 11:57:00 | TERRA_M-M | CHORÓ | CEARÁ | Brasil | 2303931 | 23 | 33 | nan | nan | nan | Caatinga | 35.9 |
| e652995d-8fc8-3c82-865a-5829c1ed90de | -3.19869 | -43.46153 | 2025-11-25 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 682f9d21-d3e1-3127-a6ba-591e369071f9 | -3.3105 | -42.4341 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 731fc6a4-5af0-3dfa-8e23-4ccc22b374af | -8.68287 | -40.7282 | 2025-11-25 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 6973edd2-471f-3908-ab63-fc31df2a9ec4 | -7.56562 | -37.37029 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 3dd99c84-ac68-368b-90eb-eb1f5e10865a | -3.56519 | -42.07071 | 2025-11-25 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| f7439b9b-2823-3dbb-b41f-267866a19c94 | -2.96451 | -42.52157 | 2025-11-25 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d5819d4d-178d-3d42-93ab-075c60d2718b | -2.79427 | -42.81331 | 2025-11-25 11:57:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a8185e91-984a-3914-82ce-55abbe7204c1 | -3.72932 | -42.33871 | 2025-11-25 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d5f2be5e-69a7-30d8-82ad-5210a10a7f88 | -9.62479 | -36.11227 | 2025-11-25 11:57:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| cb71a0c2-882b-3e5b-bba4-37948bbab7ad | -7.07126 | -45.20554 | 2025-11-25 11:57:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7f4e5fc5-2596-368a-bcfd-753955bc96a3 | -4.82694 | -43.82761 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 59ff1bbe-8c67-3a61-9925-738e2e894a16 | -3.44775 | -42.05739 | 2025-11-25 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cc22dc93-16cc-3250-8d38-7f495c5b85ec | -6.21729 | -43.27806 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5d46b3ad-39d6-37e7-aae4-7ebe3ef80fe4 | -6.03337 | -43.78648 | 2025-11-25 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0f8cd2df-c7c4-3a94-a849-21b4f1832121 | -4.04384 | -42.59481 | 2025-11-25 11:57:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 84397add-ec77-3b2a-8202-49990047d3a9 | -8.3893 | -44.01398 | 2025-11-25 11:57:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 639cd273-6a05-3502-8f9e-e9fd53e87b6c | -8.15674 | -37.65424 | 2025-11-25 11:57:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 8b18b893-193e-394f-96cc-254f1a382dfc | -3.62463 | -43.2071 | 2025-11-25 11:57:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 741ee62e-af11-31e0-800f-6fdbc5787225 | -8.14827 | -37.65891 | 2025-11-25 11:57:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 16.9 |
| d30586a3-898d-3abd-8d67-21075ab2a74d | -3.70167 | -42.34381 | 2025-11-25 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 07ed55ad-0cb1-3643-bdd5-72547dc0084e | -6.46322 | -38.22034 | 2025-11-25 11:57:00 | TERRA_M-M | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 17.2 |
| d17dc752-33ca-33cb-9c58-001811074c93 | -7.30439 | -45.43853 | 2025-11-25 11:57:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89d8d3f0-584f-3ad5-9915-f23a76139872 | -8.15912 | -37.63622 | 2025-11-25 11:57:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 20.7 |
| c9482a77-0b5a-3094-8184-a3b9de21e60d | -3.5098 | -42.14372 | 2025-11-25 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| fc20cc10-4de7-3a05-b04e-4d575db134d0 | -6.125 | -42.94795 | 2025-11-25 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 47da777c-f0b2-3979-b469-c859f7d092aa | -9.62424 | -36.08059 | 2025-11-25 11:57:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| 980e47a0-e6d8-3f7e-836a-1472f023065c | -3.83564 | -40.48646 | 2025-11-25 11:57:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 7c78821c-f591-3071-af11-eccb643cfce1 | -6.12626 | -42.93916 | 2025-11-25 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6bf5d125-86e7-3289-9503-dfcf28dbe5b7 | -6.11368 | -42.96428 | 2025-11-25 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 77ce5d5e-a080-34d4-b225-eecdcbd74d03 | -3.76911 | -44.05099 | 2025-11-25 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4c661dba-00dd-3211-9206-459865b7d0d7 | -7.71147 | -38.40795 | 2025-11-25 11:57:00 | TERRA_M-M | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 21.7 |
| faa05c9e-58e4-374c-b7d5-8432b476b243 | -5.93029 | -38.17475 | 2025-11-25 11:57:00 | TERRA_M-M | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 34.6 |
| b97ee5c4-4d6f-3243-9ade-6b31d2ff6f8a | -6.89608 | -42.84494 | 2025-11-25 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| dbd98b46-32c8-32f2-aa8d-663c3735bc35 | -3.31929 | -42.43532 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 17148c83-b38e-34a6-9531-3860b0fc8a66 | -8.1505 | -37.64086 | 2025-11-25 11:57:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 09ee5ffd-c12c-31a8-a366-17e7c22c5df4 | -3.78993 | -42.18343 | 2025-11-25 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 93f2328a-34b3-3402-b5c2-49861ae9ffd6 | -4.81634 | -43.82891 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| daca1d25-384b-37fd-b9ac-1d8c15b37d14 | -3.7133 | -42.78009 | 2025-11-25 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0de5b69d-22c2-3cbc-b801-cde5df481f2a | -3.62592 | -43.19825 | 2025-11-25 11:57:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b4935945-8e2f-325d-9f97-ff8ef16b862f | -6.68022 | -39.50872 | 2025-11-25 11:57:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ba51d4ea-d392-32c3-b132-1a840a1df8b1 | -3.39875 | -42.27437 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 67058fee-5046-3e53-8393-f4824b7737e9 | -6.68156 | -42.4859 | 2025-11-25 11:57:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 66e07f5c-ce07-3dd5-8e49-7e4e96fd0968 | -6.55768 | -43.60244 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ac885e20-7961-30e3-bc22-e3572a43e127 | -6.69313 | -43.94204 | 2025-11-25 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8bb5a67c-f075-3515-8237-94d631119685 | -8.68142 | -40.73907 | 2025-11-25 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 12fd24eb-6b7a-3e11-a56d-591b6298bac7 | -6.7962 | -44.62706 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8c2eaac4-d5da-336e-9925-69f2b13816b7 | -3.71708 | -42.75383 | 2025-11-25 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2503d9b3-96b0-31d4-a211-0a8e95468f84 | -9.40411 | -40.29527 | 2025-11-25 11:59:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 33fb32ea-a8b4-39da-8bff-eb989faa446a | -9.40569 | -40.28329 | 2025-11-25 11:59:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| dc1d0fbf-f078-355e-b4a4-cfa53ddd07ab | -22.39967 | -47.23649 | 2025-11-25 12:01:00 | TERRA_M-T | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |


