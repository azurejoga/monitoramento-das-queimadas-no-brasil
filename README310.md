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

## Dados Diários - Página 310

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1c10895-be49-332b-97ce-5974d8cc7a00 | -24.36294 | -52.33438 | 2026-10-08 16:35:00 | NOAA-20 | LUIZIANA | PARANÁ | Brasil | 4113734 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 23f70177-4752-3716-9959-93cfd1fdfd20 | -16.31561 | -44.56064 | 2026-10-08 16:35:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6aca81a3-93cd-3d68-976b-e22d689babd9 | -14.24199 | -44.43513 | 2026-10-08 16:35:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 24d459fd-a2d6-3dd8-8a30-63ce6fc556d8 | -16.05091 | -40.64933 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| cfab124b-7051-37ed-9d3a-2b43b839fd62 | -13.95641 | -44.85698 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a0052f76-cb07-3c51-9591-3802c6ca08ab | -16.20484 | -40.17719 | 2026-10-08 16:35:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a1088c58-95c3-39c4-824d-04e5097fbfed | -13.96423 | -44.84112 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83e17790-4476-3198-83d1-c912fb1f1015 | -13.36985 | -40.89393 | 2026-10-08 16:35:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bd91abce-27c4-3d38-8703-ae4f961fa189 | -28.06213 | -49.02533 | 2026-10-08 16:35:00 | NOAA-20 | SÃO MARTINHO | SANTA CATARINA | Brasil | 4217105 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| ac153790-cfd9-37f6-956c-781c2f68a9d2 | -14.26392 | -40.70193 | 2026-10-08 16:35:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 11738985-5f95-3f24-9ab6-5c025df8e84a | -13.34496 | -38.9841 | 2026-10-08 16:35:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| a22f3ef2-04f2-3732-8b81-ad1b85c543c2 | -15.85762 | -40.80092 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| cbfb9487-e936-30ef-b408-087fcb94e529 | -15.47943 | -42.07419 | 2026-10-08 16:35:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 6541d8db-c437-362d-96e7-8e604416aa73 | -14.89463 | -39.72726 | 2026-10-08 16:35:00 | NOAA-20 | FLORESTA AZUL | BAHIA | Brasil | 2911006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b309daa7-0972-3abe-aeb8-524db572f319 | -14.62636 | -43.68663 | 2026-10-08 16:35:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aa9b360b-7be6-3ea5-aa4f-ff603d03e750 | -16.58766 | -46.75621 | 2026-10-08 16:35:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 30.7 |
| f31bd18b-0cc4-388f-9fd8-65464d01fc2d | -13.74117 | -43.51615 | 2026-10-08 16:35:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fcc99f94-a4b8-39dc-b4c1-44a6398be5e8 | -14.79497 | -41.61208 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 37f44295-eeb3-331e-8e1e-91b285d9cdee | -14.84664 | -47.26572 | 2026-10-08 16:35:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e97b418a-cc9e-3342-92b0-24bc8f21cda4 | -15.99444 | -53.69508 | 2026-10-08 16:35:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 0827eaa0-756a-30e6-ab2b-ec107ba07e7d | -15.12891 | -41.38813 | 2026-10-08 16:35:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 109.2 |
| 522f5edd-7f56-3327-9b5b-41ef9cb2e138 | -16.04898 | -40.64628 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| b9242fc2-cab2-3119-9f3a-928e448843bb | -21.70506 | -56.00387 | 2026-10-08 16:35:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0d1ffac4-896a-36a4-8de6-23a18157435f | -16.63602 | -45.50632 | 2026-10-08 16:35:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d98ec039-dc89-3ed6-ac15-ee381762f6c6 | -14.6426 | -41.23279 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a9484288-db8b-3b24-9777-77a8e32e6e44 | -14.44524 | -43.92087 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ba76d218-20a8-3a9b-9317-768f34e79e21 | -16.4923 | -41.80828 | 2026-10-08 16:35:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| f5eab950-0005-3a66-986b-48ebcd187132 | -16.4855 | -41.80947 | 2026-10-08 16:35:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 089b605b-0667-3693-aa7e-f5c2d51aedb7 | -14.45183 | -41.19706 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b56ab299-7540-3550-b5a0-877bd7d57d36 | -15.95735 | -41.09208 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.1 |
| 5763fc7b-8956-35d8-9847-3587c9bb72a4 | -7.88157 | -54.99829 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3559a29a-9163-312e-8025-27f35a8e779a | -9.90667 | -44.81782 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| fb334f46-6ef4-359d-9c1a-bef9a14b876f | -7.59215 | -46.69 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1250468a-016d-307f-9dbd-dd0d3e2bc784 | -7.46289 | -42.82167 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 17b77ddb-4a2d-309e-a198-655851b396fc | -11.76533 | -45.48562 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 99f13d18-81ba-3f76-a6af-ad063b7254b7 | -7.25563 | -39.40879 | 2026-10-08 16:37:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e28a89b5-90b8-3901-abaf-60e2c287da6f | -6.10884 | -38.16277 | 2026-10-08 16:37:00 | NOAA-20 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 13.6 |
| df277bbc-93c7-33d4-9ca8-2ec68f09e08c | -11.58371 | -43.68063 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 6bf4d3f5-3434-36f8-a46b-ff94b390ac9c | -8.65875 | -54.55939 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 65cdb013-8d85-3745-ab23-0b914365263b | -6.03669 | -37.28268 | 2026-10-08 16:37:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b0ead00d-d589-31d7-8024-aee8a1cdf2a4 | -9.81187 | -45.68776 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8ba86b59-6ef8-3972-8de6-759ee887c78f | -6.76352 | -43.70089 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 62970be7-c6ab-3ddc-91a2-bfd0777da2cd | -7.85732 | -45.15298 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8cab944a-1e79-3405-83e7-2dd196776f55 | -9.00956 | -45.94494 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0d531038-82e8-3480-8478-6fd7afab1bdc | -6.32925 | -43.83198 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| acd696e4-b29f-326f-ab75-4e81027842f8 | -9.89843 | -44.80835 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| fc5da660-0f6d-3a60-9246-28401cb9ee2e | -6.67533 | -45.36765 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2eee500a-4172-3f43-ab9a-5a02ab5ad122 | -9.70108 | -45.69469 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 304f30e2-47c8-38ea-a25d-8ad3f4c98f15 | -12.76481 | -44.87121 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2c40e1a7-8bff-3fc4-98c3-570833738726 | -6.36704 | -42.56876 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c2baf0f7-c3a1-3d14-a44c-5610f23e0239 | -7.88929 | -55.01505 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b0aba11-c089-361e-b675-9e2dc51a2b71 | -8.39812 | -46.90869 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fbf47cea-623c-314e-a4f1-68f631d45d10 | -8.71153 | -37.91579 | 2026-10-08 16:37:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 77804e94-fa93-3bf2-83be-f52d3cef0d9d | -5.24655 | -37.57504 | 2026-10-08 16:37:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c91cd441-0713-38ce-9b76-2ef7ca484a5c | -8.81174 | -47.07646 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7283051-d659-3954-be55-c9718f60a834 | -10.86753 | -45.55925 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 40eb8807-8542-3e90-8efa-91fdbd4976e7 | -6.06799 | -44.11123 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| de0b8f7b-71d5-34d6-8ec1-85d96a36aa7e | -8.93277 | -50.69878 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a77c2eb0-fe41-3abb-9a5e-41c46a1fc69c | -11.79214 | -46.78104 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8d08c457-d29a-3a5f-b381-6124b68c608a | -7.06346 | -40.93554 | 2026-10-08 16:37:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 558ee03b-25e4-36f9-aaa3-d591f4f77d57 | -9.8312 | -45.77101 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 8671e388-fa32-328c-85ac-9b63e5b3b5e3 | -12.13605 | -43.32232 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 8cf2d0f9-6b8e-35c8-a60e-bf694187000b | -5.96137 | -43.90129 | 2026-10-08 16:37:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b44ef5d3-d683-3584-8e4c-db4ef57fdd04 | -7.20603 | -45.08921 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3f8d00dd-e50c-3569-b406-86a0c86f2de0 | -11.22138 | -45.25108 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| db052602-5c64-375c-9046-d2ce1279c400 | -7.31512 | -44.5412 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8bdd5508-af32-3141-90b3-9379da111f0a | -7.88203 | -55.00182 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d791dc7c-597b-3640-ad44-0a2285e17447 | -18.04951 | -44.60262 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53aca546-3240-30a8-b634-be6f1178a721 | -9.75396 | -44.7962 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c58c43df-66e9-378e-b659-af2732ff67b5 | -6.97198 | -45.13393 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8510950d-0279-35e8-9734-53a6980ceb5b | -7.70392 | -44.75383 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35aa1099-42ff-3360-a68d-c68a2eca1670 | -7.8991 | -54.71802 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4119c69-5134-341f-94f1-23bcc7960369 | -11.65056 | -43.69199 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 09ddb967-79a9-34ae-b520-34408dc08dd4 | -8.93769 | -45.16083 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 83d6281a-8a9a-33a5-8225-dff471422627 | -11.87752 | -47.40832 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 45a47574-efb8-39f9-9fdd-258446a99114 | -6.3233 | -43.48746 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2bc206b-a239-3e09-a5d9-9dcf7687ba68 | -11.25097 | -45.24527 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5c6821be-2065-32a6-a705-ffd3c9666f69 | -11.76602 | -44.95008 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| cb23fbd3-78d7-364c-ac8e-97b8c836fa3a | -5.99306 | -43.61829 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 58c87b98-6642-3d43-bc9b-7599d8ee3cbe | -11.748 | -43.64254 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 19e83fe7-e9c9-3173-a3f5-35eca9579a7a | -8.35621 | -50.72721 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ac653c8-9161-3af6-afcf-ff22a37c498c | -5.71164 | -41.66824 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8ff30f67-8270-3233-97f3-9b144afddb79 | -8.2094 | -46.41929 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b18aef9b-0935-3ba1-bf64-e47667e0f23b | -11.26885 | -45.20655 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 48083a0c-253c-3803-a427-1bb7c66019a5 | -10.85811 | -39.24804 | 2026-10-08 16:37:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 51b8e7ac-1993-3a12-b6fb-67a5f2ec1f41 | -7.85679 | -45.1495 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5e01a08a-7a39-3aa2-8589-17e56a166f1f | -8.75498 | -46.84298 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af350ed6-3be6-3870-a9a7-8150cdfee587 | -9.83067 | -45.76749 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| caa661b7-cab5-3e6f-ab8f-c024c4442dba | -8.56853 | -46.89741 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 16062312-15d0-350f-ab1e-7c348a39a527 | -11.63776 | -43.69773 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77ca949f-6f66-350a-a32d-4e4bfb401c29 | -17.9471 | -42.31743 | 2026-10-08 16:37:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| da7ac797-e18d-3923-85d1-83b41f3851eb | -6.36253 | -42.91602 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 383c881b-2795-3392-99a4-b5b35064d106 | -8.06909 | -45.62683 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 68ed549d-20d2-36cd-8687-2c404c0c68de | -6.72462 | -45.18109 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 3936039c-5fd2-3d4a-9689-62feb6684e5a | -8.95054 | -45.17627 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.8 |
| f0568f9f-48e1-3485-9a0d-465797a86503 | -6.97252 | -45.13743 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 36f7d80e-ff1a-37c8-a720-46d0a0e009e5 | -8.34657 | -47.66655 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 82173936-a86b-3718-b2bf-c1702ba3720b | -6.17317 | -38.30662 | 2026-10-08 16:37:00 | NOAA-20 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cd7cc100-9c00-3b5b-a2f2-5c6208611de6 | -8.07478 | -45.59753 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4cb5f1b-c26c-307a-b3c3-6f0665085c8a | -7.89335 | -55.00389 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README311.md)
