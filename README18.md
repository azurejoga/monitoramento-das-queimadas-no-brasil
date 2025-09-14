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
| 3ea87cc2-22a3-382e-8553-dc53cce456e6 | -14.15594 | -46.2501 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c7389a5-9b34-3404-8654-d47392938673 | -12.78787 | -48.02471 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aee83d22-a7f9-3be8-ae30-3bcfcaa8aec3 | -17.25864 | -47.2511 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd1ea76f-06d3-331d-a055-781576823e3f | -14.47843 | -47.34284 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c1f6555-3b02-317b-bc30-98fbfbb46f62 | -5.96103 | -43.21759 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 361c375f-0250-31c7-9675-427b776bb4c1 | -14.33343 | -46.61758 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c87aab9-c0be-309b-b81e-54b71a06f9e8 | -11.50343 | -43.64165 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3989ba56-fdaa-3c40-87d6-0eb356ffdf06 | -15.79732 | -52.20748 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7e13b7dc-d150-3537-9ca7-4ee3c9344723 | -14.33722 | -46.62416 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bb131ab-e2a6-32ef-8438-82811007b096 | -16.18732 | -43.13207 | 2025-09-14 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab595225-a821-3c2e-87af-aa8782f14cf2 | -12.25086 | -46.79524 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fc90ea4-d5e5-3ff1-80fa-e65b4da3e8ce | -10.9292 | -47.35672 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65e17df8-9054-3b38-a69e-f42208c882a2 | -12.7933 | -47.13939 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da5b9048-48db-34fc-9f63-7b58b30acb22 | -12.75714 | -48.00605 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 987fe9f3-971b-3947-b5a4-26be6524f993 | -12.77211 | -48.0166 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4cd6d3f1-1bb3-324b-b78f-384db6cd2b55 | -13.93351 | -44.84408 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cd7d10f-02df-3055-90cb-ea53a7f44cbb | -17.97335 | -45.27425 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a092aa02-3210-36d5-899e-d4da95826157 | -12.76734 | -48.01193 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0cd0d0a5-3eb8-32c5-b217-9cc87ba0a2ba | -14.48035 | -47.33304 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a6d027f-5639-33c2-b35e-0d6ad3d0b485 | -14.47985 | -47.33558 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f07dd4e0-ac5b-34c8-98c4-14d9295b1d71 | -11.46601 | -50.77946 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b09d9b14-d7ee-322d-8d32-486d0660c22a | -5.21691 | -45.45495 | 2025-09-14 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 481a4c0c-1d8f-319c-83a7-13da86c9586b | -6.16324 | -42.76639 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 85b61bf8-1d07-3fe2-95ab-33593d4d5b5d | -16.0797 | -44.26828 | 2025-09-14 03:49:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28baec4b-5030-34c4-a070-bbe60ba3341d | -11.83626 | -46.36019 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 445f7f52-af88-3f43-b961-f6a39c5ec1e1 | -14.32755 | -46.6221 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 117e87d7-885e-355f-98cd-1813784c551e | -12.61696 | -44.20291 | 2025-09-14 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45fea985-13cc-35f5-8773-26122d09bd8d | -16.91484 | -41.28587 | 2025-09-14 03:49:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 41e2b779-c368-3a52-9e9d-62174a89eee8 | -18.49601 | -43.9962 | 2025-09-14 03:49:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa8a6da4-12dd-3cf7-98eb-8eb105e92507 | -12.08947 | -44.72942 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c6d5d89-c08e-36c9-9730-4360e5463cee | -12.78486 | -47.97948 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d2bdb0d-33f9-3722-a043-3ef259084a57 | -12.12477 | -44.82832 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8356993-82e5-3f6a-bbe1-2399b2d74ab4 | -11.45151 | -50.76159 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3c9d8d9-3b23-3d9f-8e5c-558adfce91fe | -18.27751 | -45.39669 | 2025-09-14 03:49:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa059c4b-3ef2-32c7-8da5-0dcef54c5e3a | -18.00847 | -46.964 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fe7036a-3579-3b69-897a-ebb35467579d | -15.6017 | -47.94705 | 2025-09-14 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09a10be8-f6cd-3179-b6c8-ba67551d0b9d | -12.14311 | -47.59133 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aff6f62-dec3-3b11-b4c5-3cd65a9aa68e | -12.13568 | -47.60086 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38595fe0-2415-3f87-af0d-4cbed4922cdc | -15.91495 | -49.9755 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ce7935f-1c82-3805-bb45-065412a7470a | -14.48166 | -47.35325 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e3b07614-3db1-3b70-933b-fa199c8324e4 | -14.31398 | -46.09079 | 2025-09-14 03:49:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6956376f-c06d-37c5-9d56-ab0d2322ffe5 | -13.76481 | -43.61859 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24a58fa1-2bfa-3a58-a19c-1b435c2d9ffb | -15.84324 | -47.2376 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 260a9253-0111-3a31-ae82-f8a1c9cb5502 | -11.85285 | -50.50389 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eddbc509-ab38-3704-93c3-96f5a2094c50 | -14.61899 | -52.04202 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ce1f394-2495-37c2-912c-582159dae000 | -12.04362 | -46.54841 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a236ca7d-2a47-3539-8e3e-1a5b76bd2f72 | -12.78049 | -48.00244 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 51ba1473-1aad-3632-bfca-6a8527aba873 | -17.45001 | -49.24341 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ea0c410-0c2b-327e-bf6a-374182f41e86 | -12.09382 | -44.87071 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5fe61d7-79bd-3d80-91f0-d0a3b8413b3f | -10.76889 | -44.78335 | 2025-09-14 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9e4f3a6-a02c-31c7-859b-37721dff5508 | -11.78102 | -46.6531 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7eee833-11c1-3fcb-88c4-0afd8ae04a98 | -15.64957 | -47.03696 | 2025-09-14 03:49:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 419ae222-00ce-3085-abee-371c7018d887 | -12.78464 | -48.01243 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| ec6e07d4-5d46-3369-9936-9c5107ba4510 | -13.09851 | -42.34436 | 2025-09-14 03:49:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4903b94-76c5-3666-b234-34de96806e26 | -11.48879 | -43.62671 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1603799-49df-3d32-a6b2-3c87813f44fd | -11.14219 | -45.32097 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20f0660b-544b-312c-9170-e8e67ad4c1ab | -10.76741 | -46.48108 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9e6dbed-035f-3028-a88e-384d6a086d81 | -11.46915 | -48.70504 | 2025-09-14 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5403d94e-3ffa-3d2f-be87-b4dfe1b9dafa | -16.65048 | -49.76706 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c603ace8-b075-3edb-a2ff-84e5bba7b57e | -11.2964 | -50.79384 | 2025-09-14 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c99403ee-ca85-3732-8f0c-1402e4aafe1c | -6.31846 | -43.33951 | 2025-09-14 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a826ec7b-c2f0-3bc9-8ccb-9736b9a0ce10 | -12.81946 | -47.95083 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a6d8891-5799-3c6f-b80e-4401b5f86325 | -11.05546 | -43.30423 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 296d439f-9f68-3abe-ac56-3a72d89e5509 | -16.52639 | -43.75439 | 2025-09-14 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 841bfdb9-3545-3199-b5b0-494c17f602ca | -15.66343 | -44.69487 | 2025-09-14 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dcf159b-4ce7-3ce5-b034-67bbcd4b6baf | -18.48188 | -44.00872 | 2025-09-14 03:49:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b8de3e2-7fea-3b2f-8fb1-3c856bd20f02 | -11.66265 | -46.51273 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5b8e99e-db6c-33c4-95de-8397e760e8a3 | -12.13103 | -47.59609 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35082de2-57ac-3a2e-97ae-7de6ff7a8e79 | -6.68627 | -39.49564 | 2025-09-14 03:49:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4aff7664-b46a-3b3d-bc6e-8b1ac4e9aa75 | -14.43325 | -43.21087 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51a0f783-750e-3a86-93e3-a5151d3e7c08 | -16.11155 | -52.1715 | 2025-09-14 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 828a8262-c1c3-37cf-974a-aa07bab85fbd | -15.52416 | -48.52067 | 2025-09-14 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfedf6b8-88c0-31be-b523-5fd4489e122f | -6.33085 | -43.87466 | 2025-09-14 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 27e9fd31-5286-3681-9e4e-cd7b955da025 | -12.81728 | -47.15398 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c204e435-a0e4-38b6-9a78-f31b926689dd | -18.08748 | -42.93218 | 2025-09-14 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 17857d1e-88c0-3d2d-a084-b06e5fc80ed4 | -12.11941 | -44.83233 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40a9403b-fd8e-324f-a033-83c372b5e46d | -14.1435 | -45.41375 | 2025-09-14 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d4ef656-077c-3943-b332-13fd4a857811 | -12.78349 | -48.04679 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2072b80-6983-38fd-a372-beeabf09bcfe | -16.98939 | -45.86073 | 2025-09-14 03:49:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f5ad1a8-07ab-390f-83b1-ac8d1a13569a | -12.77876 | -48.04198 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 47445f14-c6d2-3b7e-abf3-839aba50689c | -12.77902 | -48.01015 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 03ed6f90-7120-3d71-a12b-ebcaba844391 | -13.89465 | -48.30552 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c485f6e-82a9-32cb-a68c-00abc8d5b011 | -12.79785 | -47.14357 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b389a755-7e2d-3985-84da-b8a2173662dd | -14.47587 | -47.32904 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1fd38a7-13be-3ad1-b8b9-c2daf5ae112b | -12.57701 | -45.66481 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bd94d07-2bc7-3637-9d93-d346d1e64a57 | -12.77425 | -48.00549 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 02c43dee-79d1-3636-82c1-4e3b9ee7be6f | -12.12218 | -44.84251 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a07b3d9a-39c2-31c4-86ac-9f2f16ec17ee | -11.44008 | -43.56141 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ced2af9-5d94-3734-9e56-25c4d81aba98 | -15.518 | -48.52349 | 2025-09-14 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9e62dc0-62d1-3324-8d9c-c5425f777e89 | -14.47693 | -47.32365 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c334affc-110a-36bd-810f-7979f0165c6a | -6.66008 | -43.5139 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68fc14d4-a806-3a48-a0f3-69fe021c9c5f | -12.94543 | -47.97603 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 201e9d9d-389e-35e5-852d-28c407a4b85f | -12.58283 | -45.66765 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2158ade8-45b7-367f-ac7c-41207db079f9 | -15.84449 | -47.23975 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a61852b-8d62-3e84-8b95-c8a51bca2af0 | -12.78315 | -48.01993 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83737e5d-789b-39a1-ad93-fdbeb70aa535 | -12.79269 | -47.14257 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caad2db6-a72e-32b1-8846-88cd1d204592 | -12.12754 | -44.8385 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2307e9ee-2500-3358-a16a-0071d4ccbda5 | -15.04182 | -50.15944 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e94fa7e6-f2a0-3326-8f93-a24c9c550a5c | -14.47495 | -47.33375 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1318dda8-0a1c-38db-820c-0f3be44237c6 | -10.7544 | -46.46546 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
