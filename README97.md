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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4078f89-8654-3cc0-a682-bf31a6302234 | -18.20345 | -54.45299 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ca01ec9-f050-3794-88ae-ddef060218e7 | -18.20287 | -54.45701 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30e79760-66c7-3dd4-8d64-c35ea8aa07f8 | -18.19997 | -54.45244 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55010b95-7df5-3c68-8329-cab126e5810b | -18.19939 | -54.45645 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45715a35-92be-35bc-a8a5-dc409d05dceb | -18.19648 | -54.45188 | 2024-10-08 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e65075d-03ad-3e36-b8ea-e0855982d32f | -20.47303 | -55.80364 | 2024-10-08 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6d79a1d-4944-319e-8f33-c19b8449b382 | -20.78892 | -54.8388 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 426375b8-8d76-37b6-9658-fcd48da9f4e9 | -20.78867 | -54.83701 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a355757e-c436-3252-83e4-92c2bc2c6640 | -20.7881 | -54.84108 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38448513-a2f8-3f1b-9afd-1416d0346939 | -20.78599 | -54.83413 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ad39b42-c372-3270-8c49-4dc0d1a397eb | -20.78541 | -54.83818 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19bd1c6d-170b-39ec-9709-b3cf68e064da | -20.78482 | -54.84226 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae32d17e-3f5e-3f3a-bbc5-ea1a2819bdf1 | -20.7819 | -54.83754 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9de73b5-cd67-33fc-8345-77d02b98331f | -20.78131 | -54.84163 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a252de7-3147-39ca-8760-14f6014dfbfc | -20.77545 | -54.83236 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adb09f36-4f0e-3f5e-b432-7bdc681bed54 | -20.77427 | -54.81547 | 2024-10-08 04:59:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f70c01a9-55a8-3565-913a-efcfd943d76c | -20.08045 | -54.51846 | 2024-10-08 04:59:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17463b63-6a36-3549-8e38-e679f983bb39 | -20.08 | -54.51754 | 2024-10-08 04:59:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64b7fb44-d989-3eed-b52d-c8f13f5e395b | -20.07943 | -54.52168 | 2024-10-08 04:59:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64a2c6dd-62fd-3249-9e5e-0307b13a7e90 | -14.82484 | -55.89504 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6710b67-cbc7-3e2a-9849-5af2a365d7fa | -14.81483 | -55.91537 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff3b95aa-11f9-3198-ab95-53be71afd184 | -14.8115 | -55.91481 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4454f654-c7ba-3189-8709-734df651113d | -14.81097 | -55.8964 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 943ccd94-ae76-380e-80a3-569b419d3cca | -14.80765 | -55.89585 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0e6f1dbc-0a92-36f2-bd86-7b4cc1605e92 | -14.78265 | -55.91048 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cbbfe19-33f1-3425-aafb-483d6c8c90fc | -14.78152 | -55.91762 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b036da7b-33b3-3d7e-b5f7-8743d4e38710 | -14.78096 | -55.92119 | 2024-10-08 04:59:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de7a4302-d816-394a-88a1-28289105ff27 | -16.6132 | -55.56507 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 019e8b80-675d-3968-8896-9b701c1313b7 | -16.60595 | -55.56761 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ee8d5ca7-43ba-3b04-9e68-98c7c3626b4f | -16.60316 | -55.5634 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9091f35c-1ea9-3d11-83d7-93a1f638a453 | -16.60292 | -55.89904 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4346bf63-1c12-37dd-87a3-42f99595becf | -16.6026 | -55.56705 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d369f3ef-29a3-3ef8-b19f-f53c198193a2 | -16.60236 | -55.90267 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4760e61f-166b-3062-9a7d-edfaa51d54f6 | -16.60092 | -55.57801 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dd059b02-8057-3112-9f29-5f0fcb60e8f5 | -16.59014 | -55.8932 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 931dcf57-d06f-3be7-bfe2-1c38fadedc59 | -16.58958 | -55.89682 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 48d0b742-0881-3ec1-8e09-6a4b1d1cbd5e | -16.58624 | -55.89627 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8adb3b8f-ec7f-36b7-b50b-9d08766cf6f1 | -16.58235 | -55.89933 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c1ee68c4-063e-3aa5-93c7-3a59c6b7ae39 | -16.57652 | -56.06895 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ec38b8fe-e6ff-3c52-afe1-11c35f730673 | -16.56844 | -55.90073 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d93bdc22-51f1-3d64-952b-7825ab328eba | -16.56732 | -55.90798 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6b52c00d-3fec-3d34-9bef-258d6f90f27e | -16.56399 | -55.90742 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ce54901b-5cc4-3569-bb12-3d54a35eaa07 | -16.55676 | -55.90993 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d096cef3-24c5-3661-a5c7-09b54b6a50a7 | -16.55286 | -55.91299 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 01ad9a19-936e-3084-9467-2aa36c05b1df | -16.54841 | -55.91968 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7c1ca606-8003-38c0-81f4-819babd8ba05 | -16.52672 | -55.9272 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 978f1b24-6905-3103-810d-03a6edc72b22 | -16.52437 | -55.93042 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 11dca50a-5584-3b95-885a-527b4d65d2aa | -16.42598 | -55.9474 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| b5f7b3ac-aa85-352a-81c0-e296df0e6ff4 | -16.42542 | -55.95102 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| a6a08b2a-e2b4-3eb9-b6f3-1434654bd594 | -16.42209 | -55.95047 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 820c0e32-a977-3f55-9f3d-b290f94d3913 | -16.41987 | -55.94268 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 71c08f34-4010-34b2-a97d-8ce9daf1e653 | -16.41875 | -55.94991 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e1268f29-d654-3490-9f86-de97324e45c7 | -16.41542 | -55.94935 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b1b4bc3a-c028-33c5-ae98-ee06ca8d69ca | -16.41363 | -55.9457 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3d1b4329-7b20-38de-9d33-2978bfddd9e1 | -16.36746 | -55.97876 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bf9fd8d3-8b40-384b-997f-5adf9e7f977c | -16.35746 | -55.97709 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7bd0953d-a73e-3f84-8a0b-44930466b157 | -16.20272 | -55.99249 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 850af7fc-a915-3af3-990a-118a1a68b8b6 | -16.2016 | -55.99969 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3892c237-d001-30cb-b622-be9550532d20 | -16.15822 | -55.93362 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 50d02afb-96d5-325f-a9bc-855dcef1a836 | -16.13498 | -55.86316 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a64178e4-3565-3096-89c6-02795f0c64c2 | -16.61711 | -55.56199 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1817e550-6097-3aaa-bed8-30eb49407ac1 | -16.61488 | -55.55409 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7699c3a5-f52a-358e-943b-033235f29ae9 | -16.61432 | -55.55775 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b8c9c004-4396-3635-9aa4-43c548466d52 | -16.61376 | -55.56142 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c08125bc-b1e2-3194-806d-af6a6e2ba604 | -16.60626 | -55.8996 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3b174123-eb4d-3d31-978a-1832e98a29f6 | -16.60371 | -55.55974 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ffa1519d-e6ea-30af-9f6b-57a55e1d6f7b | -16.60348 | -55.89542 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7b02142a-5337-3a1a-899e-4cd0b479f130 | -16.59958 | -55.89849 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b2c9bdf4-20ee-3652-aba5-8e31e88647a9 | -16.59902 | -55.90211 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| aa940d1c-3d76-3328-9efe-6a2143c66293 | -16.59347 | -55.89376 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 242ebd2b-927c-33db-aa0f-8aa1f2a16c61 | -16.59291 | -55.89738 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0b591bd3-8727-3eef-84e8-9c38f0ac5820 | -16.58902 | -55.90044 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 776ce23f-6716-34d9-9aa5-fe41a0db3b10 | -16.58568 | -55.89989 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 629d46bf-dcf0-3fec-9aa2-b151f8bb4f42 | -16.5829 | -55.89571 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3e2ca2f1-17a0-3993-b67a-87db4a35cec8 | -16.57596 | -56.07256 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 03388943-658a-3ddf-b0a3-2fc1de565db0 | -16.56839 | -55.94528 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 4187fcbd-8d29-34f8-87e8-e26be872c624 | -16.56788 | -55.90436 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ad713ebd-eaa1-3d26-9dec-ee5cbcebbd98 | -16.56455 | -55.9038 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b39b274a-35e5-3299-8ec2-21bea3f845e4 | -18.71163 | -57.23935 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| efd0fd4f-cba3-3440-9e85-8eee45e9d42f | -16.56065 | -55.90687 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5a40b390-8f0b-31c7-bc34-907729de030b | -16.55732 | -55.90631 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 771eca61-f793-3ac3-b0ee-d302a020acf3 | -16.55342 | -55.90938 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 026fa271-8378-3029-b1dd-ccfe3568fbb9 | -16.5523 | -55.91661 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bfb375b5-4000-3e80-84e1-66af66b312c1 | -16.52616 | -55.93082 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3352a13e-5ea1-3ed1-ac00-557d7fe657c6 | -16.52493 | -55.92681 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 7dac9b58-a542-3b3d-a434-b23a5d075d7b | -16.42265 | -55.94685 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 7541a58f-33fd-3d2f-a074-99683d22e702 | -16.41931 | -55.94629 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dcd312c3-715c-3238-854e-ab5fb3cbd269 | -16.41598 | -55.94574 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 834bad40-2f5f-355f-8420-d441adfcf728 | -16.41307 | -55.94931 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7404fc2b-b75b-3550-8609-e868162b121d | -16.3669 | -55.98236 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3742ff79-a291-3ee3-9ddb-f8c214f343de | -16.20605 | -55.99304 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 668c1d8e-c7f6-3f7d-8c76-a65726771365 | -16.19827 | -55.99913 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 05e2f892-3bda-39d5-b268-206484cd706a | -16.16211 | -55.93057 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 95c9eb56-a6ad-37a6-987e-dd3f23ff78e8 | -16.16155 | -55.93418 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5d900953-feb7-307f-82d8-ee786267014b | -16.15878 | -55.93002 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e477e7c9-1051-3b8a-b37a-347270f9d75c | -16.15488 | -55.93306 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f0c722c6-1757-33ad-8dd8-648817ee7253 | -16.13831 | -55.86372 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 96442fe3-4541-3612-b8de-ba32c0ea47d5 | -15.89842 | -55.40572 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3094497a-d676-3496-ad09-624aad32c615 | -15.59155 | -55.08727 | 2024-10-08 04:59:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8f23e07e-97ff-330d-a210-a2190c0534f1 | -15.59099 | -55.09096 | 2024-10-08 04:59:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README98.md)
