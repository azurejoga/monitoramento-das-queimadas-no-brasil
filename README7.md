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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdc86867-bc43-3f6d-8417-f4414cb30460 | -7.1271 | -43.16451 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9c4c28f3-061c-3b7b-a3cc-47b2e3a91ef0 | -10.24375 | -47.67936 | 2025-07-04 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c84774f6-88e7-328a-8770-064c33089ac4 | -7.84545 | -44.21665 | 2025-07-04 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77b4b0d4-f41b-37e9-a50c-a83eecc3c757 | -10.34078 | -47.29015 | 2025-07-04 03:49:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d66ff92a-b88a-375c-9c11-663324441be6 | -11.54717 | -47.86801 | 2025-07-04 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c34fa970-fa07-3555-b595-a1e8c437c17a | -7.96805 | -45.93732 | 2025-07-04 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3c0352f-50be-3700-a35e-1db49a4edf15 | -10.56308 | -49.13015 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2d6a1a95-b829-3aa7-bf4c-17ed86723d3a | -9.08561 | -48.32979 | 2025-07-04 03:49:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 997a16cd-6c7a-3856-9bcd-2e65e4eba42f | -11.92781 | -45.40037 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0afe6218-68d5-383e-8642-71408a04a959 | -12.13441 | -44.91105 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8fe4abe6-4c11-3041-b8ad-a454a994ef75 | -8.44722 | -49.63018 | 2025-07-04 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bcf76810-7f7b-342c-98c4-11b438e2711a | -7.20064 | -43.58511 | 2025-07-04 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e6d6ec5-b3be-3fea-9882-6b1059e3bb8c | -10.65198 | -44.4823 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1822eb61-724f-39be-8ab8-661100bee347 | -8.58144 | -48.2079 | 2025-07-04 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1cd50c2c-d502-3c4e-b6c4-57fe0aca7124 | -10.5586 | -49.1337 | 2025-07-04 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6c885256-147c-314d-8398-387a7a551f7e | -6.6112 | -43.8941 | 2025-07-04 03:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8fd2a8d5-c37b-3195-9ea5-bc96db1c313e | -7.2217 | -43.0917 | 2025-07-04 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 110b8f73-e620-358b-a808-af7e0b539a08 | -14.63633 | -45.12602 | 2025-07-04 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c241e4be-177e-34d3-9613-f241f4cf3e3a | -17.09546 | -43.80415 | 2025-07-04 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bcd7a7f-b0da-3114-87c0-962b3faee4f4 | -18.9122 | -47.01261 | 2025-07-04 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 55f17f02-3f4a-3dd9-b388-3979c6ba69cc | -17.92031 | -45.55931 | 2025-07-04 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56da9b5b-ef17-371c-a781-114f838a95ee | -14.47896 | -46.35835 | 2025-07-04 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63190032-f80c-3af4-934f-9dc204936a6e | -14.63902 | -45.12658 | 2025-07-04 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99d809ba-7b2d-3884-92dc-065e2aeeda58 | -17.866 | -44.5728 | 2025-07-04 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17d72b5b-930a-31e5-a0f1-62d5bbfbff87 | -14.60841 | -48.24895 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27b0d2fb-6987-3938-ae49-2e5506454b02 | -14.80285 | -48.30835 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14069a7b-e8b8-304c-a015-e7d4ce2fdc75 | -14.87941 | -48.35789 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 574aa66e-717b-32c6-84f6-fc333d5755dc | -19.74302 | -54.00252 | 2025-07-04 03:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f62f42e-0e5a-3671-9ce5-119afe7d4ed6 | -14.88538 | -48.35569 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c203714-b2bf-37dd-87ce-0d2867ff3428 | -19.81732 | -54.41114 | 2025-07-04 03:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bf4d44b-3111-31a0-ac72-2b66d24f2211 | -15.54935 | -40.72247 | 2025-07-04 03:51:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f98a9b79-8228-3232-ad54-79c699a7d1f0 | -20.54274 | -48.7516 | 2025-07-04 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9085c341-0cdd-37dd-91b9-a22e85551767 | -18.03728 | -46.05396 | 2025-07-04 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 408bacbe-6829-3f57-9568-c52a9499a557 | -18.71712 | -46.61083 | 2025-07-04 03:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfcf17e3-bb52-3331-be3f-e9cf3a312976 | -18.37276 | -49.27081 | 2025-07-04 03:51:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5abded0b-7c75-3c25-b087-1c55e2f4be4d | -20.44866 | -47.41179 | 2025-07-04 03:51:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c42acffc-5c19-3c21-a04e-23c199a3ea92 | -14.61379 | -48.24961 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c1dedbc-fc98-36d3-a2ba-6a57c0c71de6 | -19.74102 | -54.0041 | 2025-07-04 03:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4ae925a-93fd-3942-a953-7be930d7c708 | -19.44028 | -44.33944 | 2025-07-04 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a578c730-5f76-3998-97a4-7e18ab7777b7 | -18.37347 | -49.2674 | 2025-07-04 03:51:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd267233-f9b9-346a-94c6-83ed6f766646 | -20.76365 | -46.77028 | 2025-07-04 03:51:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 294a456f-59eb-3190-8685-7bf0c34f6558 | -18.7136 | -46.61073 | 2025-07-04 03:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96ef7274-051e-3afd-93c0-a740e342d1af | -19.74919 | -53.99972 | 2025-07-04 03:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4dbe33c-f9b2-3e94-a98e-9cc9c526989c | -20.71856 | -43.05138 | 2025-07-04 03:51:00 | NOAA-21 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c19343ef-8ca8-34b4-87bc-04ab88649784 | -19.74452 | -53.99636 | 2025-07-04 03:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 918a8763-72c9-32d3-951e-d5a491c5b332 | -16.54211 | -45.13351 | 2025-07-04 03:51:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0971d693-5575-3eab-b83d-b43cbec5161e | -18.53478 | -48.4295 | 2025-07-04 03:51:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dffc4b6d-5b48-361a-ada0-91ac2348bdad | -21.34921 | -45.51241 | 2025-07-04 03:51:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ceb24247-4c4b-3e11-9602-15419521a06f | -18.0424 | -46.05055 | 2025-07-04 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f30c0b9-27ae-3acb-9a71-6ae62a2ae3e2 | -16.68034 | -43.88475 | 2025-07-04 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5189a72d-44d2-3753-a0a0-5bcbf413f73a | -18.03809 | -46.04966 | 2025-07-04 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86f3d7b9-efaa-34dd-9ab4-d9044e39dbe7 | -14.47995 | -46.35305 | 2025-07-04 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abb3146f-bbbf-38f0-b036-4d214c7ef269 | -18.49757 | -45.90393 | 2025-07-04 03:51:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4b2b583-2a3e-3763-8181-8bec801a4681 | -18.71271 | -46.60991 | 2025-07-04 03:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5f5b6f8-45a7-371e-bed4-b35d3e616a78 | -19.72133 | -44.88671 | 2025-07-04 03:51:00 | NOAA-21 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1273cec-c59b-3660-af83-bf206d156b82 | -14.88129 | -48.35767 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c6d99a6-0fa4-3f1f-845e-10e434652fca | -15.17171 | -42.37899 | 2025-07-04 03:51:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 203235fa-213b-3308-a356-35f1ae1db026 | -15.07917 | -48.94527 | 2025-07-04 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7002f895-080c-3588-8d70-88e3ff9a6883 | -15.17245 | -42.37466 | 2025-07-04 03:51:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0295ba68-9946-3b27-b877-806af7d8bcd7 | -14.79725 | -48.30873 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a707a514-f307-3ed4-a970-64e0d87d4aa8 | -19.44806 | -48.53948 | 2025-07-04 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dedeb5af-3e42-341e-ac7a-a28b04776431 | -16.73401 | -46.00121 | 2025-07-04 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b47cc259-f44f-3153-a428-c6aded2f9386 | -15.98802 | -43.61797 | 2025-07-04 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 326e8816-5b45-382a-ab91-bb8efff7dbcf | -19.86479 | -48.32948 | 2025-07-04 03:51:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 618c204e-9eea-3d36-9a3c-60dff494ce93 | -19.79251 | -46.30489 | 2025-07-04 03:51:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a436802-9122-3f48-b90c-7d6c476b121c | -19.8696 | -48.33055 | 2025-07-04 03:51:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28e10903-1fb1-37e1-9a8b-d740bab8a2cb | -18.90768 | -47.0117 | 2025-07-04 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a8f0fe9-5379-3f69-9c2d-093953fe0676 | -14.94859 | -41.53576 | 2025-07-04 03:51:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49fb0c25-2760-335d-9ffb-9dc9a41d4bdd | -19.96953 | -44.21678 | 2025-07-04 03:51:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5848244-2b5f-3815-858b-e3d365f876e4 | -20.01535 | -44.0481 | 2025-07-04 03:51:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 989dd3e5-9166-3ba3-95ee-6bd83d50ebd7 | -15.56822 | -47.8552 | 2025-07-04 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81ca27d5-dc76-3ea9-8831-9465ca574cb2 | -19.72427 | -44.8927 | 2025-07-04 03:51:00 | NOAA-21 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 815bcf0b-9cdc-3167-b48b-e121c9ec2bf5 | -19.72525 | -44.8874 | 2025-07-04 03:51:00 | NOAA-21 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a75f62b1-7d4d-3cf7-8505-a0a93a2b1319 | -15.98504 | -43.61229 | 2025-07-04 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02ca862b-52df-3eac-a00e-2e0bfa7e4628 | -14.88474 | -48.35887 | 2025-07-04 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a963f595-f8ce-3c2a-956e-1309c7172165 | -18.45401 | -51.23914 | 2025-07-04 03:51:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6593ad14-7cdd-3d32-9d30-39ba923aa261 | -22.6768 | -47.46292 | 2025-07-04 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f1b5580-381c-32f8-a4da-21090bf27352 | -22.53854 | -48.81381 | 2025-07-04 03:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbf2d61b-f4c6-36c1-851d-a4d7c456817d | -22.67251 | -47.46182 | 2025-07-04 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55819477-2647-3017-9258-e9ed4a8f9e22 | -23.98577 | -48.91608 | 2025-07-04 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d7cf95e-f58d-3176-b7f0-9cbb9525c4d8 | -24.74167 | -53.80628 | 2025-07-04 03:53:00 | NOAA-21 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b3a32def-74ec-31b7-87b3-7423080a8784 | -22.66821 | -47.4607 | 2025-07-04 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dd6ad62-ed75-3c7e-abe6-65dacd25f60c | -6.6112 | -43.8941 | 2025-07-04 04:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3b9bff3a-d413-3923-ab88-e67d28fd8d21 | -10.5586 | -49.1337 | 2025-07-04 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 20edb1c6-27fa-3800-8eb8-61c3b30962d4 | -10.5586 | -49.1337 | 2025-07-04 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ee0495e3-8844-3fb2-8851-e664c4d3e896 | -6.6112 | -43.8941 | 2025-07-04 04:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9d61fc61-f8af-3c4d-9052-2dfe35ef6f20 | -4.00899 | -43.23809 | 2025-07-04 04:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b6fa1a1-0c62-396d-a04e-c6c795571124 | -4.01232 | -43.23862 | 2025-07-04 04:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66c71b59-fdbf-3041-82b8-8b8f78fec9f2 | -5.44724 | -43.58323 | 2025-07-04 04:14:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e64dd17-613e-3a24-a21e-464cf5a43f07 | -5.19632 | -44.80705 | 2025-07-04 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 811f48bc-18d7-3841-8969-3c03c9112f02 | -2.93978 | -40.1007 | 2025-07-04 04:14:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2ec71e9-c9c7-3377-aa4d-3f2b65ea8eba | -3.38373 | -43.12579 | 2025-07-04 04:14:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9bb2b73-e402-3c5b-90d0-089bfcfe8b0f | -4.54018 | -48.01988 | 2025-07-04 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 07bae60e-ba3b-3e10-b21c-37045f978a19 | -4.53543 | -48.02297 | 2025-07-04 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3f8246b-1e15-3f19-9088-8d65a45c400c | -4.53956 | -48.02357 | 2025-07-04 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 05aeef9c-7d80-357e-8e9f-a9920090d073 | -5.06715 | -37.6674 | 2025-07-04 04:14:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 610a7e10-1728-3556-b60b-728fe120f76f | -4.01288 | -43.23514 | 2025-07-04 04:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83edd25e-047a-3549-88c6-f5de796ff6e5 | -4.82161 | -47.32003 | 2025-07-04 04:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 279ded1b-804f-38e3-8801-b30a0efd13a7 | -4.17283 | -40.72039 | 2025-07-04 04:14:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 16e0709e-546f-3496-978c-e5b74b8312a1 | -4.53605 | -48.01928 | 2025-07-04 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
