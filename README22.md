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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 451dae1b-ca18-3923-a42e-acf0774299ff | -6.0 | -42.7998 | 2025-08-23 04:00:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f217965-ffce-31a0-85f1-3150a8074fdf | -7.496 | -34.9101 | 2025-08-23 04:00:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 360463ab-4938-34b1-8a76-311ab85d0bba | -3.04918 | -47.01482 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97bb0979-8b85-3882-a58b-784d9a13d632 | -5.87441 | -53.633 | 2025-08-23 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04abe673-98b2-3a51-a18e-fa22587af1ad | -6.12263 | -44.40949 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87c64bfb-00c6-3c0c-be44-0e3c611ca671 | -4.97581 | -38.6003 | 2025-08-23 04:00:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 92197e3c-968c-3861-a1f4-ef2d2e8a6b34 | -5.83484 | -45.16761 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c056f977-1dbb-33fe-8d36-c4399db7dcfa | -7.06916 | -44.6179 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 11fd828e-12c7-3dd9-b56d-0baf3cf6c3da | -6.97956 | -44.03372 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33356c7b-65c9-3dac-9dbd-d3be2bc9d0e1 | -6.38467 | -45.52983 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a91819de-904e-31d6-a255-4da0fe6248bc | -4.87284 | -41.5799 | 2025-08-23 04:00:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8062d8d2-13df-3533-80d9-cf0d4ab8cd23 | -6.37987 | -45.53297 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d00fc112-e163-39ec-b0a0-afb6a754a81e | -6.0492 | -44.36499 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47e16a51-8119-3bdc-96ce-94d368f05d3f | -6.40579 | -45.49032 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1693cc5b-f832-304c-b81c-6e2a296e2d4f | -3.55531 | -41.62339 | 2025-08-23 04:00:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ecdb5661-07fc-3c91-8d3b-67838df85f1c | -6.93357 | -39.5648 | 2025-08-23 04:00:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5dd9798a-62ed-3e93-acc2-8c817f64010e | -6.393 | -45.51504 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6759dac4-ff08-3183-89e7-114f90349fb6 | -2.90787 | -48.24919 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 200aa1a5-6840-3f10-9e95-04333eb7520b | -3.64858 | -48.32956 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43030f79-7536-3489-8099-30fa99ce7fb4 | -3.36427 | -43.37241 | 2025-08-23 04:00:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8162cf4e-2c2e-366a-afc3-2f7cef1148e3 | -6.94575 | -44.16505 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d0265d3-3158-37d2-94a7-21cd30e79bd4 | -7.07871 | -44.06395 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fc186a0-6bbe-3187-b94d-7746fdb5e5c1 | -7.43351 | -45.41692 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d248dcfe-ca92-3cfe-aa71-3290e5c1f91a | -2.44692 | -47.33176 | 2025-08-23 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 328e20c4-0048-33df-b0d8-9b6d441772d8 | -6.36841 | -45.55051 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ff76590-1a1f-3210-86cf-f626783dfdaf | -6.41766 | -41.21714 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 244853c6-2e00-31c2-8462-15e4f2f89ed3 | -5.80325 | -46.5485 | 2025-08-23 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4e551cc-8962-338b-8239-a0749bcd161b | -3.81721 | -41.55805 | 2025-08-23 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2edf201b-f970-30c8-b7d9-42b014a67835 | -2.70448 | -48.2103 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ab8b9f0-7d0c-323b-ad55-d3636d599c4d | -4.09036 | -46.92714 | 2025-08-23 04:00:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 157db935-136b-3f67-a465-5fe8d6789409 | -4.77131 | -45.32444 | 2025-08-23 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b97e05b-1669-361e-9908-f419564b0db0 | -7.44654 | -46.12962 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 967960d1-d812-3991-87a9-da05712ce22f | -7.02046 | -44.59903 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6924168-b056-352e-b007-d81ab3a68c0e | -3.43537 | -49.04507 | 2025-08-23 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8cf2e5bb-e719-3afd-84ce-7c79220718d5 | -5.90529 | -43.46548 | 2025-08-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cc3cc63-b66d-3abe-a26e-d4d143b74db9 | -6.50153 | -42.98924 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc53c228-4125-36f3-8282-405b64040667 | -2.70393 | -48.21356 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8b461fa-a41b-35e3-b5ea-8639a0339b0c | -7.02083 | -44.64436 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f7452402-d87d-3c44-a1ff-18df4d8448a3 | -6.11487 | -44.40818 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a32f48d-4f34-383c-a207-2f0ba1643b40 | -5.79116 | -50.18703 | 2025-08-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2415c1b6-9b62-3420-bf80-b2519ecc1bbb | -4.33905 | -46.46487 | 2025-08-23 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891fe15d-b8d3-39a6-be4f-c8de09d93d94 | -6.36898 | -44.74287 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbf58dee-ea70-3b96-a520-5f62066f5cb1 | -5.94101 | -42.54114 | 2025-08-23 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b7db3ce8-3f1b-3f15-8dab-784e519efc33 | -6.78066 | -44.32058 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 906dcf17-3a21-3871-b7b8-2a71ba7a0e23 | -6.76468 | -44.32202 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f0a08c4-586e-3a24-8138-79ee66cc7273 | -5.10501 | -44.79218 | 2025-08-23 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ea651d-b6a2-349e-a266-f674be9abece | -5.82767 | -52.07114 | 2025-08-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e8866190-1c70-36c8-9935-940191e87597 | -7.96218 | -42.64129 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af4e2e6e-8fd3-3849-827f-ce67aecdc765 | -7.14843 | -44.67482 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2e269a4-9537-3be8-b6eb-9f0e505e8272 | -6.39068 | -45.51925 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7597ebff-f22d-3c56-9565-7bc0f00d8f1c | -6.5051 | -42.98985 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 917767fa-cb27-3ce6-ac01-adba45e5e472 | -4.11989 | -48.11726 | 2025-08-23 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb7d7f82-f176-38a3-af19-3b04aee70f27 | -6.79174 | -39.32076 | 2025-08-23 04:00:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fb4c116c-14fe-3963-8b29-687876783b7d | -5.9026 | -37.81956 | 2025-08-23 04:00:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a7a33fe-c3fc-3ce0-acb2-3260d8083c26 | -6.11098 | -44.40754 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61fe151b-c4a6-3bc5-a872-2db463d9d42d | -3.81782 | -41.55429 | 2025-08-23 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b0a348d5-6b3d-34ab-a666-9053e1623c06 | -5.9601 | -43.04221 | 2025-08-23 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c639fb68-c3f8-35dc-9e11-4f09b31a367b | -7.67607 | -45.41437 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d098fce9-3011-3a79-821d-f5edb220a33f | -7.72292 | -44.08495 | 2025-08-23 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a90d9973-30e0-30c5-898a-46f13efd64c5 | -6.23436 | -46.24764 | 2025-08-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9acb0d5-9191-3784-afa2-d8386f072552 | -5.88903 | -43.44935 | 2025-08-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6f43ab1e-f771-30c6-9e49-1c80777dd9a0 | -7.07961 | -44.06173 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e24fb31e-eacf-3180-bcea-a6286edeb6b9 | -7.02001 | -44.64928 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53558573-4456-312d-adc0-c1ac3862f10a | -6.97015 | -44.13559 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0799d141-98c2-3a18-a843-be1f1abec002 | -6.44678 | -44.5397 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d880d05-260d-3f89-863f-99f82660aaec | -3.98596 | -43.24468 | 2025-08-23 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ca6a88c-e78c-3c05-ab6b-a0b0e951597e | -4.63819 | -41.40329 | 2025-08-23 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3f340fd9-1287-3c3f-9150-6898b33f5c43 | -2.54994 | -47.71148 | 2025-08-23 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1057ce96-c1e7-325e-8a70-1c9ad02317b7 | -6.36779 | -45.55427 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0028a680-9be9-37fd-bd25-8fa910c223a1 | -5.83137 | -45.16323 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94d627c7-6605-3d79-ac30-c02b30f4e9f8 | -7.63455 | -45.23533 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 99e2ca91-1c4a-3344-bac6-0da9b4ef2550 | -4.97916 | -38.60081 | 2025-08-23 04:00:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| adeb925d-4146-3e6e-9170-438645f4f79a | -6.38528 | -45.52608 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ea92cb3-a17d-354d-ae52-29bec2b6e87e | -6.17989 | -45.43112 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ddd0edb-9987-3600-a49b-4207e00543c1 | -4.63361 | -41.41005 | 2025-08-23 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ae458d2a-bc84-3cb1-a544-445133ed13ac | -2.69917 | -48.20946 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71f9ac94-704b-30ac-9ff8-a614a542c0c8 | -5.48922 | -42.15207 | 2025-08-23 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec81b773-33e5-343d-ba2f-76d912b6f9a8 | -6.05144 | -44.35802 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83dcf795-3ba9-396f-ba8c-73f2afc0207e | -7.0286 | -44.64574 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 79c30b8e-c17b-3f27-bc6c-78744389036c | -7.31656 | -44.55433 | 2025-08-23 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d945397f-78ba-3699-abc7-4b3824f39c64 | -4.64488 | -43.65044 | 2025-08-23 04:00:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf269a81-c73b-33dc-b627-c2c2201be356 | -7.07417 | -44.06816 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2ddccb2-9860-39ba-bf4b-f097aa4401e4 | -6.77685 | -44.31983 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 870dacb5-9b7a-357c-a610-996ec69c06c2 | -6.7933 | -44.9991 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73f8eae2-997e-3e3c-bd1d-b50346d40981 | -6.28102 | -52.82991 | 2025-08-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e089f2be-355b-38b7-8455-90e9a1033c5e | -2.82344 | -47.72435 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c2d407b-6e12-3ed6-a326-436b16e8a7dd | -6.11803 | -44.38892 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d02d4914-5fe0-3c74-a66b-7c34e779e43d | -6.10789 | -44.40205 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 541d400b-fb1c-3c36-88ca-f89209f5c019 | -6.39129 | -45.51554 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73643177-a757-3495-9e06-6431d171aabd | -7.61416 | -46.26396 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 232d0346-5d70-318f-8ef5-ec581949aaec | -6.95048 | -37.39126 | 2025-08-23 04:00:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 27fd3e2c-3f02-3a86-8d25-6d0532c215e9 | -7.64354 | -45.24092 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96f23a4f-6bb1-303c-b631-b240e11e2aa5 | -3.51381 | -47.21014 | 2025-08-23 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7059cf14-e9de-3791-833a-328c4e85fff2 | -4.65345 | -41.41715 | 2025-08-23 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aaadd7ba-337c-3e8f-95b7-a2a02565b496 | -7.02307 | -44.65484 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c25fa1e3-716d-3f55-aa6b-89d08db2a930 | -6.97368 | -44.18401 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa755a6b-e844-352b-9498-5f404024d9bf | -5.79886 | -42.29893 | 2025-08-23 04:00:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60730c95-7422-3598-b0ce-dc451a4598f6 | -6.79387 | -44.9956 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 274d980c-cd88-3245-803c-08bc904e8f8c | -7.02389 | -44.64994 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cb4b779d-f5d2-3b37-af49-a10f871ae266 | -3.79113 | -41.00063 | 2025-08-23 04:00:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
