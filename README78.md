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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0710b4c-4556-375a-9b6a-bda21be1c240 | -20.10469 | -50.01408 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| d7c445bd-99c6-3dda-8ffb-167508170788 | -23.42269 | -47.05651 | 2025-09-04 04:57:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6e473c3c-ebb8-32f6-b379-26d9fd527ac6 | -19.83579 | -54.37446 | 2025-09-04 04:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3de40780-d680-3363-a92c-dfc5438c5941 | -22.27848 | -52.03782 | 2025-09-04 04:57:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8072334f-b0d3-3afe-ad9a-9e24e70190e2 | -20.33713 | -54.06882 | 2025-09-04 04:57:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 102e3631-edc2-30aa-9f4c-04098338d3af | -19.25483 | -46.53482 | 2025-09-04 04:57:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1a8985a-c001-3e9c-b6c8-5705de323a69 | -21.94626 | -50.5158 | 2025-09-04 04:57:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9a2b9f46-3ace-35a7-ac9d-b359cde43836 | -23.01228 | -47.08378 | 2025-09-04 04:57:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de477ef8-412d-31ce-8e16-f7a1df9628bf | -22.45873 | -47.54688 | 2025-09-04 04:57:00 | NPP-375D | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fe511370-ba90-3472-89c7-c1af1e9f4a13 | -23.01195 | -47.0872 | 2025-09-04 04:57:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6e5b0b46-f70b-3bdc-ba49-19d0868ff959 | -23.51164 | -47.16736 | 2025-09-04 04:57:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 86f5bc82-a1d1-34f2-a9f0-0f16c180c5f3 | -20.1052 | -50.0101 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 6a174c4e-4f5a-37c8-b35e-05c1bd474efb | -19.25514 | -46.53194 | 2025-09-04 04:57:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1af32c97-4d41-31d7-8da2-496ff84ddc8a | -21.94993 | -50.52026 | 2025-09-04 04:57:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3e939f90-348c-3a91-9779-0f170ed319bd | -22.33897 | -49.88559 | 2025-09-04 04:57:00 | NPP-375D | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 828683f6-539d-35a3-a187-1dbfa52d951d | -22.57944 | -50.78731 | 2025-09-04 04:57:00 | NPP-375D | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a863967-beaa-37f3-8113-b1dcdb0eb416 | -20.29475 | -46.71466 | 2025-09-04 04:57:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04c750f0-2a74-38a0-a560-17bcaf4be776 | -20.29002 | -46.70957 | 2025-09-04 04:57:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cbf04f77-7f7d-3fc2-a6f2-cd945b295303 | -19.24101 | -48.68305 | 2025-09-04 04:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d899f10c-454d-3e94-8d78-cc53b44370e5 | -20.10001 | -50.01747 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f4cfa8cb-e93b-36b2-bcb0-0e1d1df01023 | -20.09787 | -50.00089 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8632a153-97ca-3dce-af7f-fe9358b52a04 | -22.66151 | -43.68801 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| a1d22b83-cb62-3a5f-ae04-3a341c6efb18 | -22.46314 | -47.55378 | 2025-09-04 04:57:00 | NPP-375D | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2f4998d3-7080-36fa-9017-038da6919bd7 | -23.42694 | -47.05257 | 2025-09-04 04:57:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3ea3678-0716-3f33-868a-eda0b99c6099 | -19.68921 | -49.36101 | 2025-09-04 04:57:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e94246a2-c742-3dde-a871-c956a151d038 | -20.09268 | -50.00829 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 608d93ae-88ff-3d0a-8c8b-82f3406ff01e | -19.56845 | -49.43751 | 2025-09-04 04:57:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57beec82-2158-340e-b939-8027798f0147 | -21.45596 | -54.55309 | 2025-09-04 04:57:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99ce4f62-7c22-3735-b515-17b7d8e05800 | -22.28228 | -52.03846 | 2025-09-04 04:57:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 16a30087-e615-3a39-a94d-b296088c8a55 | -19.28336 | -49.77529 | 2025-09-04 04:57:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1924817-bc21-316f-a329-8744eeac98fe | -20.10629 | -50.00452 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 08bd7063-5d34-3bc6-bf7f-ebcf95a48851 | -22.22702 | -55.97022 | 2025-09-04 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 963444d5-895d-3ee0-8d3b-10801efbc311 | -18.32855 | -50.97789 | 2025-09-04 04:57:00 | NPP-375D | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67045c0f-fbdd-3dc7-b9eb-d4cf1c453dc9 | -22.28395 | -47.63137 | 2025-09-04 04:57:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 576825d0-1a1c-3558-89d1-c3a454534617 | -22.64884 | -43.68444 | 2025-09-04 04:57:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f3dee12b-7373-3d1c-9871-eeb517491fb0 | -20.09686 | -50.00889 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 6cdd7ce5-bbd3-3f40-a28e-c9042076bdd5 | -23.29928 | -46.16167 | 2025-09-04 04:57:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec2b3e28-5c77-38e9-b45f-990bb07a82ce | -18.71798 | -46.88576 | 2025-09-04 04:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74818c3c-3b94-307c-afd1-8e2f9a95029f | -22.65475 | -43.69147 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 88f658d7-efe5-3ebe-9f63-26bf46a9496f | -23.31403 | -48.8099 | 2025-09-04 04:57:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ff1c086-647a-3f3c-bf8b-19f400dea812 | -19.68435 | -49.36483 | 2025-09-04 04:57:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7525f436-a757-35f1-8780-388e9ff9ef41 | -20.09737 | -50.00488 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7af0ae46-0191-3701-8df9-267ef3bbafcc | -19.23706 | -48.67778 | 2025-09-04 04:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e1553a0-1ac5-3f00-8cc7-6b0d48b1d939 | -22.58356 | -50.7879 | 2025-09-04 04:57:00 | NPP-375D | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83a1ab3d-4fec-3892-8826-421ee9677350 | -23.42303 | -47.0531 | 2025-09-04 04:57:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2414ddcf-bd0c-3602-88c4-6751471f4d1b | -22.2231 | -55.97337 | 2025-09-04 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7154e319-509e-3678-9c49-a3488eafb15b | -21.95042 | -50.51631 | 2025-09-04 04:57:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c41a8a1a-c9ab-3fdc-a6d6-4d230d505122 | -19.75336 | -44.11074 | 2025-09-04 04:57:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7b6a3d5-1e0f-38aa-9b05-27ae0e369b97 | -18.14319 | -51.79178 | 2025-09-04 04:57:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa4da33d-5683-3ae2-b02d-47c5a28a7e87 | -19.05408 | -57.66333 | 2025-09-04 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 86205665-2fc2-3da3-a7eb-f5bd95c0e9a2 | -21.34173 | -45.64003 | 2025-09-04 04:57:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94cf8e24-132e-3ce5-9ac7-010d668f3d02 | -22.98576 | -47.09179 | 2025-09-04 04:57:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d075262b-93f9-3331-8067-d3ccc7c8e0e3 | -22.22585 | -55.9777 | 2025-09-04 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 30eedbdf-bf10-3704-bd97-800d7c43768c | -22.81862 | -47.7275 | 2025-09-04 04:57:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d50bb3f-b562-3779-9faa-1d3d2e3b435a | -22.66107 | -43.69338 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 40050d4c-6973-37f5-a70a-a0e70bfb267e | -20.47185 | -54.40315 | 2025-09-04 04:57:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2cecfb1-5ff9-32e0-a145-6c057d6b2e06 | -22.26216 | -49.55924 | 2025-09-04 04:57:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 63924cdb-bb33-3405-a7b9-975935642636 | -22.64879 | -43.68705 | 2025-09-04 04:57:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| eaf3cafa-e354-3641-a6f0-7a3a240c85a1 | -22.61206 | -54.9757 | 2025-09-04 04:57:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9885998-328f-3180-82ec-b2fbe7a4bd66 | -22.46378 | -47.54762 | 2025-09-04 04:57:00 | NPP-375D | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 842e6f38-2590-3596-9313-80c1876956ca | -22.26269 | -49.5547 | 2025-09-04 04:57:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| afa8abb8-06d6-3b94-8468-7b17d8cbfeef | -22.91222 | -42.42003 | 2025-09-04 04:57:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cd3868fc-2f14-34f2-875d-e271198c2536 | -22.6615 | -43.69044 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| ed6f6023-565d-349c-8d5e-0615605bc41e | -22.22919 | -55.9783 | 2025-09-04 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 4b62e579-0459-3e3b-b0ce-3f1f0cde00e0 | -23.51686 | -47.16828 | 2025-09-04 04:57:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ed84b3a7-4b21-3489-aa0c-af691fbb2477 | -22.6552 | -43.68589 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 496d9fc5-1323-39b4-b329-af15bec3d6a5 | -19.21648 | -44.48323 | 2025-09-04 04:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c742e23-4c39-3e28-bfdc-0578eb9af634 | -20.88468 | -51.5855 | 2025-09-04 04:57:00 | NPP-375D | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 74d97535-d86d-399b-9370-6f962346449f | -20.09319 | -50.00426 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3bad6d4a-74b5-3d2a-ab25-52e5bea7317d | -19.25974 | -46.53811 | 2025-09-04 04:57:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd2a013f-f69e-3bdc-8870-f7783e8fa139 | -23.40097 | -46.84018 | 2025-09-04 04:57:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 826b66b0-f998-3822-bccf-2ecdf3498286 | -22.64923 | -43.68119 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 446d38bf-69c6-371e-83e4-84fc601ec76d | -20.10052 | -50.01349 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 54e81fb4-7134-33ae-b715-9b912cf67588 | -20.29444 | -46.71774 | 2025-09-04 04:57:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 513e65a2-66d9-3740-bc5d-aabccfbd30dc | -22.4581 | -47.55303 | 2025-09-04 04:57:00 | NPP-375D | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| df8c18c4-22f4-399c-8785-883b437fcffb | -20.10571 | -50.0061 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 85992d40-8b02-3982-9270-1ef73c85214e | -20.47243 | -54.39931 | 2025-09-04 04:57:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02866259-70c3-3a2a-898d-43e2a601b6cc | -20.09634 | -50.0129 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 8dfae32d-9877-3894-97f4-030424052b62 | -22.61827 | -54.98073 | 2025-09-04 04:57:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b5d83ba6-ca7a-318c-9d77-a13fbc85f937 | -21.33911 | -45.64169 | 2025-09-04 04:57:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78741e05-1874-3550-b064-41283b380328 | -19.2365 | -48.68247 | 2025-09-04 04:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9d092384-693a-317b-9a7b-db7ad7b370ac | -19.69509 | -49.34881 | 2025-09-04 04:57:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 827db78a-556d-3060-ab4a-f9d2582b4d61 | -22.28266 | -47.63263 | 2025-09-04 04:57:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81448367-e3d9-39e6-b02f-79fe352ca315 | -22.64839 | -43.68996 | 2025-09-04 04:57:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4b6a0954-4633-3f26-ba41-168c8c1e254f | -22.27327 | -47.63616 | 2025-09-04 04:57:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a2c9cb-f8f0-3d3f-b15a-f14363b6041d | -19.21989 | -44.48039 | 2025-09-04 04:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e213a8b-9617-3ae8-a95b-61c932e463d6 | -20.10205 | -50.00151 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9caadea3-2cb5-3b0b-bfc6-c4fe891a5086 | -20.10532 | -50.01251 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03288d03-ac30-3014-8ed1-ef7b8a25ac3e | -22.98539 | -47.09538 | 2025-09-04 04:57:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e2baaee-3721-3c97-821d-865ae27a5fca | -19.56095 | -50.01228 | 2025-09-04 04:57:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a81af66d-3e60-3bd6-8acd-7cba81f7f05e | -22.91915 | -42.42059 | 2025-09-04 04:57:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 961f72dd-ca08-3ad7-8353-d5d123d32910 | -22.81799 | -47.72924 | 2025-09-04 04:57:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c7d8a72-706d-3859-b7e7-cc6212a3c661 | -23.76945 | -47.44914 | 2025-09-04 04:57:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d2fc9b3f-7991-3a4f-8a00-bfdc98d4852d | -23.40132 | -46.83659 | 2025-09-04 04:57:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1f378b6-81be-375c-b09b-e935f4f18c4f | -20.10154 | -50.00549 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e094c356-a03e-32ee-9b50-5a1d2729fcb9 | -22.66198 | -43.68399 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| bb06ef36-fc09-3949-9305-ffe8df7bfb1c | -19.68486 | -49.36054 | 2025-09-04 04:57:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58ea62bd-ddb7-3435-acf7-cd6273b19075 | -22.62165 | -54.9813 | 2025-09-04 04:57:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 89640038-c658-376e-b566-747cdb504040 | -19.69457 | -49.3531 | 2025-09-04 04:57:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 798d149f-ffba-3679-b258-bd7b7c44f0e9 | -19.71553 | -49.14215 | 2025-09-04 04:57:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README79.md)
