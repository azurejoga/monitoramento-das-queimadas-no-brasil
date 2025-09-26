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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af20ebd9-740c-353c-b7f8-1c2df828ab6e | -12.84533 | -44.70489 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 08871376-c778-35cb-83ea-4c442719e06e | -11.43217 | -44.96534 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 57c3b834-e807-34a1-9c09-25cb2227c0f7 | -11.62187 | -44.4298 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| f5b1f8ae-55f1-3907-ab54-7d56e733beb7 | -13.29806 | -43.566 | 2025-09-26 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 88be98e6-d6ab-3aa0-ac5c-c6ffee0a8f4f | -11.95524 | -47.87248 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d2cc5438-53ca-33d2-a62c-3507de06e0fa | -10.27227 | -40.19797 | 2025-09-26 12:00:00 | TERRA_M-T | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 71891385-3f54-3b43-a4e4-42f3c3453ede | -11.42776 | -44.99486 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 265.3 |
| 961593d0-ed95-3530-a07d-9268fc145ab5 | -11.38864 | -44.93838 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 4ff005ef-418f-3719-bdfd-384b12024437 | -15.1378 | -46.43481 | 2025-09-26 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9fa39bf4-48bc-3ea2-b58f-c22554816441 | -14.82553 | -45.40297 | 2025-09-26 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4f5bbc8e-5bd0-38cc-b4f7-9c14d4aa6818 | -15.45385 | -43.64582 | 2025-09-26 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 47f3119d-8ec0-335e-8c95-677b6072388e | -11.70083 | -44.46109 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dbdc6572-afca-3a75-be8f-5d22f344c7cf | -11.41588 | -43.515 | 2025-09-26 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4c823556-2af0-3e76-af75-6ed07374e8bf | -12.88288 | -44.69754 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 718833e6-8515-33e7-951b-1e7d201ee8d6 | -14.71266 | -46.79054 | 2025-09-26 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 22764fc9-97ab-326d-8198-8d353e25b88e | -9.06537 | -43.00214 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e118b873-14a0-3a3f-9059-85f203771f3e | -14.96312 | -46.76647 | 2025-09-26 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 83740f76-5077-3a1d-9fea-9c00559a3250 | -15.2686 | -46.44032 | 2025-09-26 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a1454f5d-14e2-3d5d-988e-bc21c9fbc5d9 | -9.70785 | -48.24324 | 2025-09-26 12:00:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ecd86bb6-f760-35b2-b17b-b500de0911a3 | -11.65129 | -45.35074 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f5c9aa0c-e258-3083-ac39-507c5af4e1e1 | -11.38717 | -44.94809 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d387b28c-c796-37d8-8476-e1494c5eff2c | -13.19667 | -47.40989 | 2025-09-26 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 232f3a76-1f24-3c4e-b99e-435e790b264d | -15.53864 | -44.33392 | 2025-09-26 12:00:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 360957a8-ce09-37f2-85f0-ae5897c86e02 | -11.70223 | -44.45158 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9ba2dd96-c472-32f6-8363-f9f9dbee8d24 | -11.41993 | -44.98347 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| be9f85cc-8bfc-3143-9987-f230ca6cf229 | -14.46046 | -42.7243 | 2025-09-26 12:00:00 | TERRA_M-T | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9f117316-212f-35c6-b10c-40f7d7e1d2b0 | -12.23791 | -47.0169 | 2025-09-26 12:00:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f6de1137-23ef-3a6c-9912-ff93f2c5b0b1 | -12.14721 | -45.81889 | 2025-09-26 12:00:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 98512124-7851-383f-8701-5c785f0a79a1 | -14.82701 | -45.39319 | 2025-09-26 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b3ff6d66-4c64-360d-8fce-b2c2c5310f63 | -13.25449 | -50.66092 | 2025-09-26 12:00:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 5844f7df-99b7-3ec1-ad2e-33d26d732c80 | -10.42937 | -39.49949 | 2025-09-26 12:00:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 52.6 |
| c8b2d8e9-061e-3537-bbec-c2c17566f8f2 | -13.44841 | -45.89104 | 2025-09-26 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 886e579c-ce1d-3bbe-bee5-cf946a715152 | -18.58204 | -45.2094 | 2025-09-26 12:00:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| f4512506-b1fe-3b18-ae8e-24a93580b041 | -15.01651 | -46.9469 | 2025-09-26 12:00:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c0386796-7882-38eb-96d1-c46e58e625bd | -10.93797 | -47.7457 | 2025-09-26 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7aa41b50-ea55-308c-ad9f-07b488f7be5e | -11.42923 | -44.98501 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 21a23ea7-7011-314d-b8ca-18e92bc4d81b | -12.97837 | -47.18038 | 2025-09-26 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4ead44ae-be5d-392a-85f6-e72908341cbd | -11.41721 | -43.50596 | 2025-09-26 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f2c01628-3c66-3e6c-bc83-59b4ba052b45 | -14.40479 | -43.76466 | 2025-09-26 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6564ce5e-9627-3f82-8962-923b0faf1054 | -19.03241 | -46.44991 | 2025-09-26 12:00:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b01d89c-0d8a-3354-a5ac-973f2c96a3e5 | -12.8738 | -44.69618 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f15338b7-aa02-3044-9ae7-68468479a37a | -18.59233 | -45.20139 | 2025-09-26 12:00:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2844868d-bf57-3868-bd61-6b5c36b619dd | -11.70783 | -44.41359 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 34c9519d-b43c-3b50-b981-3fc842a55772 | -11.01676 | -44.34363 | 2025-09-26 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6749eb4f-ddd0-3a62-8c06-8fa7c65daa70 | -15.44631 | -43.63538 | 2025-09-26 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 320e8b7c-d97b-3c48-be2e-e7c23dddb7f8 | -9.55748 | -47.51744 | 2025-09-26 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 804a1020-be25-38dc-83d4-59f120d01683 | -15.78297 | -43.65725 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61fd7f9f-ce5a-3c35-aaf1-08cc8e688313 | -12.03847 | -46.90655 | 2025-09-26 12:00:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d2107f71-891f-3d7c-9feb-7391dc14b09a | -15.53999 | -44.32473 | 2025-09-26 12:00:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 472171a3-9ad0-3ff0-891b-ee0e8cccf166 | -14.71083 | -46.80214 | 2025-09-26 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5212e93d-a0a0-318c-ba28-3508eb0b7141 | -9.70505 | -48.26088 | 2025-09-26 12:00:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 868bb3b0-da10-32b8-8994-cd042e943e70 | -10.72345 | -42.17149 | 2025-09-26 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 247ce970-0ac1-30ba-9412-1b03ac9ca65a | -9.98205 | -46.70111 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e0bb4532-51f5-3e9a-b772-735ec16a5466 | -12.3732 | -44.15449 | 2025-09-26 12:00:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2b751571-3082-3510-b5de-ce7754b6aa35 | -13.71574 | -47.89687 | 2025-09-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 205.8 |
| d2c79080-1622-34bd-91b9-0cde2567d3a2 | -14.87831 | -45.53875 | 2025-09-26 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e50f1650-e35d-311e-956b-183df8309bf5 | -11.4366 | -44.93562 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a01414b6-7621-3c45-b56a-e2c9784edce9 | -10.92668 | -47.74385 | 2025-09-26 12:00:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b23539d4-bbb3-3c9a-8381-7a2fe40ba8da | -13.33816 | -47.87936 | 2025-09-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 25a9c739-5b9b-3673-90c2-e2edda57400b | -12.9763 | -47.19328 | 2025-09-26 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 682d3101-aafe-3c56-9783-70bbe0ebf698 | -15.07391 | -44.98025 | 2025-09-26 12:00:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cb4d820d-77af-37a6-8b67-5d939d202095 | -11.01534 | -44.35316 | 2025-09-26 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6cad64b2-c247-3f37-a686-82807ea56eeb | -11.26623 | -47.78482 | 2025-09-26 12:00:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ebba3f38-c868-38c6-a0b1-8503489f2c19 | -13.27729 | -46.97641 | 2025-09-26 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7c4d501d-851d-32f3-8269-dc6f7ac76ee3 | -13.75298 | -47.87296 | 2025-09-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 761b7404-be35-3261-ac81-a2c439338d80 | -11.4307 | -44.97519 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 856bfeb4-daa3-34d2-a742-7c041b39c20f | -13.19244 | -47.40247 | 2025-09-26 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ea816604-2dd1-310d-b5f2-c0af903005f7 | -12.62884 | -48.12767 | 2025-09-26 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 431cab16-587d-3435-b4e1-ee87b0af66ba | -15.445 | -43.6445 | 2025-09-26 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 48.1 |
| be8f314e-f33b-3580-9f50-b4f69b01d407 | -9.98006 | -46.71419 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ecf7bb21-ae79-3064-91cf-94e9da5ab809 | -11.62044 | -44.4393 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 722184fa-3294-39a8-9ddf-bbb586384af2 | -13.27926 | -46.96411 | 2025-09-26 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f969cf2b-93ba-321f-9aa6-869caf4ff317 | -13.7181 | -47.88223 | 2025-09-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 84a8a03c-9d1f-3187-8217-74e3bee01969 | -11.71062 | -44.39464 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d6e224db-0a30-3a43-8c68-2ed2586bfb47 | -12.2434 | -47.02375 | 2025-09-26 12:00:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 002331f7-aa66-33b6-b9bd-cbb349ccecb4 | -11.70922 | -44.40411 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1ec67fe7-395c-321c-af50-23ac024ed258 | -12.57013 | -45.85468 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| b846e1fd-5b9e-39dc-ab76-a49292e28a06 | -12.80161 | -42.79296 | 2025-09-26 12:00:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 1d7b28a9-4055-3aec-aa2d-72b8c17f4237 | -15.02833 | -46.93679 | 2025-09-26 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1f13d7d1-7173-396a-b4d8-df4b23265f44 | -11.56689 | -50.21813 | 2025-09-26 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| e7a65aa3-3478-3292-a79e-149bccd22b73 | -19.02321 | -46.44836 | 2025-09-26 12:00:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1c01664a-2cf5-38a2-b6a7-ecbf621d570b | -11.42883 | -44.92396 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3d775190-a966-3887-9cfb-850a85db6b43 | -11.96388 | -40.00521 | 2025-09-26 12:00:00 | TERRA_M-T | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| a0ffed43-4f36-3df4-8489-209e7c9d54f2 | -8.85676 | -46.61347 | 2025-09-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8e79aa5e-625e-3fba-933b-a397d6540f39 | -11.42288 | -44.96378 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fbb956c3-6560-35e9-b8fe-4a079300606d | -13.20011 | -47.21571 | 2025-09-26 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4ff02eaf-d46f-3c02-a6df-c11af6366ec2 | -10.00834 | -44.1738 | 2025-09-26 12:00:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 4a4a6494-afa1-3140-8982-14c9bbe44fab | -11.96648 | -47.87403 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 450fb559-e0bb-3477-8a76-51b94597fdfe | -9.47626 | -48.22997 | 2025-09-26 12:00:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 352d0722-e50a-3d5c-a300-a50737ed50c6 | -11.9782 | -46.63509 | 2025-09-26 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 659d1da7-2b53-3c2c-9379-fded1e8701e3 | -10.9358 | -44.26729 | 2025-09-26 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 54fe32d1-7ac6-3b74-aee6-7d8ecc33f932 | -14.87679 | -45.54867 | 2025-09-26 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 875b879c-a48d-366e-8660-6335bd8718b6 | -14.72974 | -45.18601 | 2025-09-26 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5bf5d74f-b5eb-3fa1-a999-b89c38bb5549 | -11.98012 | -46.62278 | 2025-09-26 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b53e3e1b-3249-3253-bddd-818f3749c030 | -22.53384 | -46.97279 | 2025-09-26 12:02:00 | TERRA_M-T | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0d7567cc-f989-3635-8216-6698a21cf194 | -21.67865 | -46.0987 | 2025-09-26 12:02:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| b62f5199-4cad-3cdd-a932-012712902b26 | -19.78539 | -49.39461 | 2025-09-26 12:02:00 | TERRA_M-T | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 313806f7-55ab-3d30-b854-541262ce2af2 | -19.79189 | -49.40489 | 2025-09-26 12:02:00 | TERRA_M-T | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 294367c3-2e72-3ea8-8db2-7ca4d63245e7 | -20.39047 | -46.01472 | 2025-09-26 12:02:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5f4fd4d5-db20-38e0-802e-936bcf930445 | -20.46677 | -46.24346 | 2025-09-26 12:02:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README51.md)
