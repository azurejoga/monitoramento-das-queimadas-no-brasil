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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 134d3917-3507-3ca6-810a-5b044b099735 | -6.62569 | -44.74203 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c7d5073-15e6-3cae-a219-9146880f8921 | -8.8972 | -44.22532 | 2024-10-30 04:44:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff699c4b-d38e-30c3-a736-fd804c038de9 | -8.89635 | -44.22385 | 2024-10-30 04:44:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06cd2af0-c3b0-36e3-a57a-ffe1784b9971 | -8.77605 | -44.70819 | 2024-10-30 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73023ab4-a4ea-37a3-b6ee-7c610f1ce3a2 | -8.77541 | -44.71276 | 2024-10-30 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 51fdced1-1b7c-3eb8-8827-f6d635a7cec4 | -8.77285 | -44.73105 | 2024-10-30 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4644a68-1a58-32ed-b414-df9d24a904fc | -8.73504 | -44.46904 | 2024-10-30 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dcadead-baca-325a-a483-cadb5c9e9f50 | -8.73384 | -44.47065 | 2024-10-30 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4f6762d-18ae-37bd-819f-ff9f3b2cb493 | -8.54836 | -44.63832 | 2024-10-30 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 109ba6bc-1b1e-364f-8c8d-8bcb5ca6b09b | -2.57229 | -45.347 | 2024-10-30 04:44:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| acfcda3f-ba22-3472-a26b-1d877df3bef9 | -2.52919 | -45.28296 | 2024-10-30 04:44:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 58ddd1b2-265e-3d41-8b7a-99e2c7b8000a | -2.38625 | -44.86015 | 2024-10-30 04:44:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2e5ccd3-7384-32ea-84bc-a9c9abbc3895 | -3.44291 | -45.97203 | 2024-10-30 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9492d737-48be-3bc3-a536-edb750c9e008 | -3.24439 | -45.57133 | 2024-10-30 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8338872-e7bb-3039-ad1d-08fdf51ce76f | -3.24363 | -45.57634 | 2024-10-30 04:44:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61ca5564-aa1e-3692-8f76-a9c98679a5f1 | -4.03151 | -44.71887 | 2024-10-30 04:44:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e6fdf54-53b0-3ef3-806c-4fd397e9c3b4 | -3.84714 | -45.94279 | 2024-10-30 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a3c229c-f31f-3034-aa47-5d7cb4751b7b | -3.68613 | -45.47387 | 2024-10-30 04:44:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2e914de-1781-3ff6-a4da-5cd29a2995bb | -5.11721 | -45.14488 | 2024-10-30 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6792b5a-a5e8-3870-827f-969ba321aa04 | -5.05057 | -45.15856 | 2024-10-30 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9db41ee9-b2af-3dd8-af9c-b39e3bc2ac86 | -5.05 | -45.16236 | 2024-10-30 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8784a42-d98f-34dd-a0ea-deb89b950af2 | -4.8386 | -45.77242 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 163a89ca-3af8-38ea-bb8c-e5e4697e4276 | -4.83095 | -45.71383 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55db5010-fe1e-3b02-9bec-bfaa170d7829 | -4.82746 | -45.70977 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ae8665a-d1d9-37d3-8a9d-d12b01bcc363 | -4.82694 | -45.71325 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98d3f2db-ae3b-3675-ac49-53b2595ccc10 | -4.81736 | -45.72268 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 147a0331-05af-3a85-be5e-53d50263b922 | -4.62398 | -45.60175 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8a5e7e5-2a9f-3925-8ac1-89b27754ee05 | -4.62346 | -45.60531 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98158f95-895b-332f-b7fa-b9c76dfe4712 | -4.62294 | -45.60886 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d6daa59-2bf3-3ef5-a158-07d530dc1118 | -4.61995 | -45.6012 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72b89f38-d79b-3fb5-a81b-6aec5e5d93d4 | -4.61943 | -45.60475 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b31106-fcf7-3ee6-97bc-528e588ece0b | -4.61592 | -45.60062 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6006627f-f29e-3a28-8c4d-4213393a9ea4 | -4.61541 | -45.60414 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 296222cc-5237-3d75-977c-64a0a871e80c | -4.61189 | -45.60006 | 2024-10-30 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbd6cd2d-05f5-32e2-881a-8bf97774f2f6 | -6.37248 | -46.5678 | 2024-10-30 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fee32843-5fff-3995-8fce-ddb2c9746798 | -6.33786 | -46.02325 | 2024-10-30 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90fd6eda-0a19-3afe-8ac3-8841e50ac6bc | -5.65395 | -45.91882 | 2024-10-30 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d51035f0-5327-31b7-a05d-15ff99e29044 | -5.64908 | -46.3844 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6378022-e92f-345a-a49f-2b71dae4c84f | -5.60106 | -46.25185 | 2024-10-30 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae844493-76e9-3571-96eb-a0ccd842b5a0 | -5.48198 | -45.84696 | 2024-10-30 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06c51bb4-9bae-30ec-877a-6771d161e3a4 | -5.2701 | -46.25245 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d878dba-764b-3f7e-b595-de29269b2513 | -5.26992 | -46.25039 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c2c778e-98cb-3d07-98fe-9ded19153c58 | -5.17157 | -46.13824 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f83bfb0-f66b-305a-a5c7-17869acf82e3 | -5.16721 | -46.19265 | 2024-10-30 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78e6dcd6-855f-3288-b4d7-d79cf8bae870 | -5.10922 | -45.70576 | 2024-10-30 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1afbb086-a5d9-3d0d-90f2-8d68f1cd0d56 | -5.10516 | -45.70536 | 2024-10-30 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93280617-15c0-3e41-8a57-635ce94ab891 | -5.97497 | -45.36677 | 2024-10-30 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4d0b92b6-370c-309e-b530-901c9a7c0e96 | -5.97441 | -45.37055 | 2024-10-30 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c67d6c2c-e00d-3c01-9d47-83143efd3fe6 | -5.97386 | -45.37433 | 2024-10-30 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f12e8960-bbca-3e8f-8d14-d1a6bdd3c8d5 | -5.97081 | -45.36606 | 2024-10-30 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| afc6f86c-66e7-3117-bbaf-95681c01d883 | -5.97026 | -45.36985 | 2024-10-30 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cfec239f-9423-347c-a8c4-f4d1591b2a2e | -5.9697 | -45.37363 | 2024-10-30 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f5603e57-c98f-325a-88ec-e9723d0d6aab | -5.75154 | -45.56599 | 2024-10-30 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8be7fa8-50bc-364f-91e8-b449e94c7b9b | -5.74745 | -45.56533 | 2024-10-30 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6baa2152-6db4-33fa-9342-d4949a91e4fc | -5.66388 | -45.20264 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7aba28e9-3a1a-3b66-8ee7-2d52719d4883 | -5.47625 | -45.51878 | 2024-10-30 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ad6354c-5be1-3a89-980e-857d187e7a21 | -5.46355 | -45.50193 | 2024-10-30 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 091cb8b3-daf9-3586-be02-556e91d7c76e | -5.46299 | -45.5056 | 2024-10-30 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2937bf29-599a-3bf1-ad95-d502a69b4de4 | -5.45944 | -45.50134 | 2024-10-30 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3f4b096-f670-3909-8126-baf2f6f5e66a | -5.45889 | -45.505 | 2024-10-30 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c104943-96d9-30eb-ae56-6e316d572574 | -5.42221 | -45.32608 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 634a4c2a-857c-3554-a962-f7e73d4ccfd0 | -5.40859 | -45.15033 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e97a3938-73fa-3bc6-9519-c4f03c88ba7e | -5.29853 | -44.93755 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7326888-5693-3dc1-ad9d-43bfdd207d87 | -5.29796 | -44.9414 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 569f3ebb-8037-352f-a0b9-60564c8de4d3 | -5.29428 | -44.93699 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43428c75-300e-306d-aaae-d43ea630ba9e | -5.2937 | -44.94086 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f88a4910-f1de-3073-83a0-69685d22be9c | -5.22189 | -44.90305 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff48a333-3e3d-3633-81e4-2fa152db23d4 | -5.2213 | -44.90702 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 777734c1-a96b-3c91-bb59-433b32e6bf5a | -5.21762 | -44.90254 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e3a36a6-424e-3afb-9227-130134a6cbda | -5.21175 | -44.94177 | 2024-10-30 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f40ee1b-3869-3e72-9b8b-d7046ee49657 | -7.58108 | -46.4368 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc0714f9-7ec3-3508-b087-0ad0b2a141a3 | -7.57634 | -46.44136 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 504fa3fe-fc35-3553-8ba2-81d22173cf7a | -7.5521 | -46.12791 | 2024-10-30 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 800d9029-c3ba-392b-a843-b914b6af25e9 | -7.5516 | -46.13145 | 2024-10-30 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d14cc791-270f-3816-92a3-e15219c60fea | -7.43366 | -46.62513 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 945e6c90-6a89-3f1d-901b-e3e8604c4e6d | -7.42973 | -46.62458 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcd506bf-d239-3262-af2a-9e2a116b875c | -7.39629 | -46.5789 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2af49b4e-1679-386a-9699-8b82d7e9fcbc | -7.38273 | -46.53914 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81c4748a-c914-3cef-a9c0-b6ad6db21101 | -7.2459 | -46.57365 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5061616c-3bd4-387f-86c6-4e332321bf62 | -7.24516 | -46.57863 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d16d80b0-23ff-37d3-937f-00544ade0a1d | -7.24199 | -46.57301 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80d73d5a-9623-3de2-9ac9-26874f1b80e4 | -7.23708 | -45.53095 | 2024-10-30 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed622b9f-a541-3cbb-9144-13cc1c5c2068 | -7.23289 | -45.53026 | 2024-10-30 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfb28857-d03c-3e92-a3c4-999a9cdf43d0 | -7.22145 | -46.38412 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8de85c8-de6a-3dfc-8ca4-cf440fd46c37 | -7.18382 | -45.485 | 2024-10-30 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c17c9959-0012-335e-b7b7-214015609af0 | -7.12947 | -46.62966 | 2024-10-30 04:44:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4bc6085-d7c7-35df-8977-d99a9ca606a0 | -7.06659 | -45.66372 | 2024-10-30 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d8f7c50-0b35-36f0-b7a7-03e3e45894c1 | -7.06245 | -45.66303 | 2024-10-30 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47953cf8-64c1-3666-8e83-d1d59dbf7501 | -6.83578 | -46.07639 | 2024-10-30 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f68417e9-b5a3-3584-8483-5ef9cff74c40 | -8.48131 | -46.5167 | 2024-10-30 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd2a0576-9de2-3581-8ae5-f40781d61165 | -8.28672 | -46.79306 | 2024-10-30 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c2a1a5a-c191-3ec8-ad2e-6f28015ce20d | -8.20936 | -46.85697 | 2024-10-30 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3966fa4d-2cd8-3610-abfe-a93f2e7f0d11 | -7.88425 | -46.8975 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6540a108-9378-364a-8c0d-7f0ecb3e8f2c | -7.88355 | -46.90235 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aeb6c2e0-4934-3d6e-acc2-5f404580ac8c | -7.88037 | -46.8969 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66c7c2c1-40df-38ed-b22c-9ea5a02c534b | -7.87897 | -46.90663 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab517ffa-d958-3172-b5e5-7b3ebd9f9804 | -7.87438 | -46.91095 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d33c1984-cc0d-32a2-b572-3379f9b0e388 | -7.87192 | -46.90054 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 616150ed-ee11-39e4-9da1-eae224196366 | -7.87121 | -46.90543 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e58f06f-e96d-3d60-b79f-25ba88991a1c | -7.87051 | -46.91034 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README73.md)
