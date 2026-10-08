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

## Dados Diários - Página 275

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1ecbc07-bb5a-3de3-8461-2620493638cb | -10.60379 | -43.84314 | 2026-10-08 16:18:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ac3ecce5-2a86-3a51-ba46-7d69730aace1 | -8.88339 | -41.44908 | 2026-10-08 16:18:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 3c1be6e5-5797-3a90-8962-66633aaecba0 | -13.96864 | -44.83866 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 481b4874-3e06-3010-b26a-5e7d9d8403e7 | -10.48854 | -47.22938 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6390e05a-ea06-3b4c-a802-3384037e2441 | -11.84946 | -45.28594 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 68ed3633-5eef-35fd-9fe9-329662f31d5a | -11.09067 | -47.51693 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fafe9b0e-930c-3083-8047-a0a0f845be38 | -11.78217 | -45.5882 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b9ec476-167b-3f34-8024-9c82c0754c3b | -12.17336 | -44.81557 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9a980832-5947-3817-a517-dfdb0bf96897 | -8.97147 | -47.55856 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebb81195-e410-38bb-af72-d4575924e4ea | -11.3992 | -46.67876 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 372e6122-2c8a-3a02-9461-4346fa152b61 | -13.18815 | -47.86547 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 59c13986-d572-3079-8e1e-ccd1b233f1a8 | -8.93462 | -45.18176 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 1fd64d38-543d-327f-9652-43585344a246 | -9.8177 | -45.68085 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 7263286b-a686-3b29-8de6-f7fd5af387df | -11.34215 | -41.59048 | 2026-10-08 16:18:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 4bb7bf32-6ae8-331b-8cf8-b7202e0671cd | -8.60044 | -44.87174 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d78f5670-a60c-3f1b-82dc-1eb84ce0bed5 | -13.61244 | -43.27991 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 82d555c1-a300-364c-ba3a-87dac438d175 | -11.54594 | -37.9701 | 2026-10-08 16:18:00 | NPP-375 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| bded1f2f-438f-3d7d-853e-57c697894964 | -13.02798 | -48.51616 | 2026-10-08 16:18:00 | NPP-375 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| de1272b8-e12c-309e-b0a0-de8c26ccc4b9 | -9.80837 | -45.68206 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 16a0270b-553c-371f-9adc-4b5250521828 | -13.69043 | -49.11855 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| faf022c7-ba20-36a8-8fc8-273a44d02553 | -9.82887 | -45.76483 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f31726d7-2079-336f-b370-781c815705d0 | -13.97271 | -44.83316 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 29ed5089-cf3f-3f0b-9d6f-4204eee0706c | -11.08373 | -44.03294 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 415.1 |
| eb0dd975-ad80-3ae3-947e-e58af566164b | -9.08243 | -45.12501 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 092be5f1-cec7-3ac4-83b8-6380b8f9a36b | -11.27153 | -45.21074 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 87edbd0c-e07b-3970-a0d0-84fc55f0653f | -8.28287 | -45.72021 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 86f4c58f-9b69-3466-ad84-5b97b6f9c540 | -9.43325 | -41.73439 | 2026-10-08 16:18:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 36.5 |
| d6faec86-79d1-3de0-ad1f-5d128cc1591b | -9.14504 | -49.926 | 2026-10-08 16:18:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d8528792-6353-32e1-8e59-b467ae62ef23 | -12.31815 | -45.25994 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 475ecbcd-daf0-39de-a3c4-80781acbe252 | -10.75784 | -46.60484 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0f1e05d3-3363-364e-9ce6-524433475035 | -11.33419 | -40.91809 | 2026-10-08 16:18:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a3b08b62-451d-3173-8597-8c8b62bd1416 | -10.47724 | -47.22434 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bd30b94f-696d-3ad3-807e-14b96dfeee97 | -9.14355 | -45.84512 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4427ef6f-81d5-3154-bc99-e0e90375e9f9 | -11.01651 | -45.43819 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 099802bb-7748-37d6-aae8-dd2993d240f4 | -8.59241 | -44.86971 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 18456c71-42d5-3fd9-95d1-3f8c0e5e7ad6 | -8.76811 | -45.76239 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f2448db4-65f7-3f2d-baa5-c04f7f711363 | -10.07355 | -45.99903 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 3139773a-e470-3826-8681-af6a0e987e8b | -8.77227 | -47.26352 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6543e11-8179-38e3-9a43-b6d3106ccfe9 | -9.38945 | -47.09349 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 11b58dda-7e9b-3ea6-b46d-f347d6cb947e | -12.23944 | -44.75175 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 7b9a36dd-a2a2-3e40-879f-793acdab7c77 | -12.23432 | -44.74779 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 05051f61-fa55-3034-8c82-752048f2da76 | -8.74947 | -47.13218 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc81cf60-c907-38a6-a6c1-baa2f6566e87 | -13.11696 | -43.48546 | 2026-10-08 16:18:00 | NPP-375 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 479b4755-1603-3ba9-a715-e18e46395431 | -14.58312 | -47.53892 | 2026-10-08 16:18:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0e560a7d-79e8-344f-8205-dbb5b165ec89 | -9.88655 | -44.8654 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 224.3 |
| e08f66ab-2231-39f7-82e2-c981eca060c6 | -11.11075 | -44.00908 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| d98360bd-ac8b-37bd-9edb-b0b3e2fc6c8e | -11.33637 | -46.69236 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f3265f4e-df2b-3203-90af-863e89c3ac1c | -11.40972 | -47.56316 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8f8fbe6a-b8b9-3237-84eb-af70305a909d | -12.04354 | -47.38711 | 2026-10-08 16:18:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 52aa140c-74bd-3b93-b6c5-76aa4e08602c | -10.44712 | -47.2804 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 55fada4e-9eda-30e3-82e9-68f8ed295d9f | -11.08903 | -44.00801 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 55ab85f4-25af-3d76-ab9e-4b17390c7ce2 | -9.74438 | -46.94333 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08fd0940-f1b9-3b81-b850-55e5eac50b9a | -13.12152 | -46.33316 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 49beb139-df81-388f-8fcd-f281b40c1194 | -8.2892 | -45.73261 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 225.8 |
| dfdf5a79-1c6d-3371-bc14-fc3378099fd2 | -12.03676 | -43.38926 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 56f95a96-f476-31c6-bdca-326d7ebe6a7b | -8.94886 | -45.12774 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3bb5c3e4-b3ef-3238-b5cc-9134d34988c1 | -11.61273 | -43.6594 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bedc876a-3ffa-3e3c-b8b6-8012e59e2ef1 | -10.46393 | -47.20359 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51f28147-9e25-3d62-9dad-7364ac1c1e9f | -12.04562 | -43.43782 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 23c37895-4674-344c-8b87-f63e3dce8ab8 | -9.34573 | -45.42193 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d3dbef34-63f7-3a0f-9600-71bf4137e726 | -12.23766 | -44.73784 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| aa19aac4-1e0f-3d79-858b-b99d622e0b72 | -13.70562 | -49.08723 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e8bb5dcd-c1a7-3b35-926b-cd412d7d5a42 | -12.18893 | -44.65419 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 6a7afe88-e73d-30f0-a63b-a8a64e0f1bb3 | -11.85903 | -48.02986 | 2026-10-08 16:18:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d43d1276-5477-38a1-b38c-3513f77504e3 | -11.21327 | -49.4199 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 59bbef28-7288-35f6-87a9-e67f36d736af | -11.84695 | -47.33637 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4bcc22d7-4543-3e7e-85b4-a528ab4457a6 | -11.09433 | -44.01535 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ffe229fe-6925-318e-9b63-06dbeafc9c26 | -12.18383 | -44.65028 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4e8755f2-0c8e-3290-bbf8-118274292e0e | -8.93661 | -45.16362 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 972414a3-99c2-3033-881b-9fa43ffb6109 | -8.99245 | -45.9081 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d9e9edc5-15d3-3ed9-9f14-ed754b54ec0d | -11.07419 | -44.02619 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| b863ffc9-4365-3e7d-8e0a-6a245c9038ff | -7.61353 | -39.75204 | 2026-10-08 16:18:00 | NPP-375 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 80fc202e-14a9-37d4-839b-ee416bc81a0c | -11.15543 | -47.29107 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fce98d21-40cf-3a5c-bc48-1f253444c9b8 | -8.95407 | -45.16677 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 59206759-2d73-30f8-90a5-17e799c8782f | -8.96508 | -45.14768 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 834cd5a1-e5ec-31a4-ae25-631cef336922 | -8.28464 | -45.73334 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 225.8 |
| ace4fe44-2322-3a10-a7ff-f698661c4b9e | -9.84254 | -47.85884 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| cba5910c-8cb7-3ca7-b803-18055abf4080 | -8.28336 | -45.72206 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 61e2fa1e-1353-3ab9-aa51-cfc3a496d403 | -8.94947 | -45.12659 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d0de4c23-f371-3567-b941-193a37d7f3a3 | -8.59617 | -44.86489 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 650ee30c-d5fd-370f-958c-1c2d2533cd20 | -9.32947 | -38.09239 | 2026-10-08 16:18:00 | NPP-375 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 63d270ad-f493-3644-b037-f1fe2633bc9e | -8.5961 | -44.87223 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 249acebc-737e-375a-87cb-3a3d60c0fac0 | -9.88541 | -44.85685 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 932a1b46-c027-3a51-be23-14a5fc1e0a2f | -9.77675 | -47.81746 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a1e9a4d9-4376-34d4-9d90-f4b0aaef24ad | -12.16048 | -42.26502 | 2026-10-08 16:18:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 599ed2a9-ae35-3058-a319-1652427afc79 | -11.85526 | -47.3596 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d87a53d6-eefd-3fbb-a525-a2c21655a851 | -11.60389 | -43.65681 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 27c8a4ff-a28f-3d62-ac46-906e8fb3a149 | -11.40468 | -47.55136 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80fbe8b1-96a1-30ac-a1ca-f0358aa31804 | -9.84422 | -47.86118 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 95430915-dc0d-33b1-a781-876cabf8e0da | -11.85738 | -47.3768 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fd7b5310-c293-3387-9250-7aefaa1137c4 | -10.32962 | -43.60846 | 2026-10-08 16:18:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7a24cdc3-6e9a-3911-923e-a11cda878401 | -11.58796 | -47.17714 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| feea8f4d-294b-3b8e-bb32-34111642dd77 | -9.63479 | -45.73509 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 985279bb-ae0a-3b1c-b1cd-40f8ff5ea2db | -10.51033 | -47.31475 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3971d814-bfa7-321b-b1fa-c3fa97cd454e | -8.61148 | -44.8802 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| d938e4e4-d655-3359-b913-881e36782171 | -11.85568 | -47.36301 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8d9903dc-bb6c-3e9e-8b86-faf53c33f991 | -11.77681 | -45.54753 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 966eef20-4116-3ed3-8502-26de2b437e55 | -13.13993 | -46.35612 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 015fc063-47e3-380d-bf0e-7d7e2ad7d47d | -8.78332 | -47.26818 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b0b8511c-d528-3e34-b1d7-378793d754cf | -13.13878 | -46.34684 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README276.md)
