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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 611909d1-1c3a-3e09-abe2-2e664eb9d7d9 | -14.13314 | -41.69247 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f99f482b-5d9b-3d75-97d4-90059a13b8d0 | -15.86179 | -41.95217 | 2024-09-26 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9c279c1e-3e60-31ed-8f6e-621074661e6c | -17.78036 | -42.8101 | 2024-09-26 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a0ecf44-093a-3022-9bf2-50bb0ba5db3c | -17.77881 | -42.80622 | 2024-09-26 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c508f6af-f19e-3d95-a517-a630f6ec863f | -17.67693 | -42.74059 | 2024-09-26 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6006dc4-4da0-3051-91e0-8959e332186d | -17.55919 | -42.86108 | 2024-09-26 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d38dd61-b02e-37e2-8a15-9176bc62ff3d | -17.38622 | -42.65993 | 2024-09-26 04:08:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72f3f83f-0a21-3153-9609-c83f24a1d524 | -16.75723 | -42.46901 | 2024-09-26 04:08:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d41701b-06c0-34e5-adda-53b82e3194f5 | -16.75387 | -42.46848 | 2024-09-26 04:08:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e873507-ffa6-3062-819b-ff1d8e5f1b77 | -16.75332 | -42.47219 | 2024-09-26 04:08:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a5ff4e7-458e-30fc-9012-4b04f414b4c0 | -16.63106 | -42.46005 | 2024-09-26 04:08:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d644ff6e-cd21-304b-baf5-93e273eb20d0 | -17.99425 | -42.30824 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b466bb52-2671-3d82-a8f5-3214ffd87f39 | -17.99197 | -42.30008 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8cfca26b-262e-34ee-998e-0e4770ef4ca7 | -17.99084 | -42.30773 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d912cee-636b-3886-b2bc-342167d27f7a | -17.98857 | -42.29954 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09742d34-9705-3d66-9d77-5ebf8fd58425 | -17.988 | -42.30339 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f6f463b3-dab5-330b-be8d-45b9e991c035 | -17.98744 | -42.30722 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f4763d0c-f5bc-3acc-a4f8-71533918525d | -17.9846 | -42.30285 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7dc86ae9-6859-37c8-be95-3e571ebbd642 | -17.98404 | -42.30667 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 02892c3b-0b28-3a4d-9d8f-a8e2dd1c22b9 | -17.91092 | -42.13847 | 2024-09-26 04:08:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b08bd92c-26c0-301e-9f19-6f09d13a659c | -16.65006 | -41.89391 | 2024-09-26 04:08:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e2159545-01d9-3412-be0f-e754fab795c8 | -16.6495 | -41.89774 | 2024-09-26 04:08:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0f0034ac-b755-3085-9b24-f697420eb04e | -18.58368 | -41.64872 | 2024-09-26 04:08:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 9a0b4489-f888-32db-b2a5-e27d0d36e29c | -18.5013 | -42.96025 | 2024-09-26 04:08:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c4d7a33f-26e5-3aa4-935b-bec27ff85584 | -18.48854 | -42.86243 | 2024-09-26 04:08:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cae118d8-dfe1-3ce2-a90b-7f5bcc06132c | -11.49306 | -56.78437 | 2024-09-26 04:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 359d0f8f-be26-3128-a17b-508bd50c4c86 | -11.48598 | -56.78263 | 2024-09-26 04:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b06b707-cd61-3d77-b72a-e417403cb472 | -15.84936 | -57.39728 | 2024-09-26 04:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8141d568-9aed-3e86-be10-fad691f2ac24 | -15.84426 | -57.38799 | 2024-09-26 04:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 753319a9-2e30-3def-84fc-949a6b901dab | -15.84268 | -57.42693 | 2024-09-26 04:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d5520824-68c5-37e5-b875-5d15b7ec382e | -15.6032 | -56.95813 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b93d9b1-2f0f-3089-9b90-385e42345010 | -15.60138 | -56.96626 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c8c8549-07b5-3cc7-a24f-dd6ec678ccbf | -15.59819 | -56.94904 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| baa4739f-020b-3474-8fa9-41e9ecbdd11b | -15.58727 | -56.93494 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d78e954a-2e8c-36a1-9d4b-a1e25e5609a3 | -15.5844 | -56.93705 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 88ad1563-be4d-33e9-b122-1e026a1fbc97 | -15.58082 | -56.93232 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9f296fee-e3a9-3d2a-b2bd-94dd21eb3711 | -15.57975 | -56.93703 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8da38d93-6c3b-37af-b4ca-f5f003f716db | -15.57893 | -56.9299 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2354f32c-1cf5-36b4-9923-771f2d11bb7c | -15.57787 | -56.93476 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba9fd200-c89e-354c-8fee-bb314f2db779 | -15.57522 | -56.92591 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a96d7e53-d788-3919-a004-7d881898c750 | -15.57409 | -56.93093 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ae4a78fa-d5ba-300f-a4f5-dee59e5f63d0 | -15.57219 | -56.92858 | 2024-09-26 04:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0cd36cd-411b-31ba-baa8-ef097512b946 | -20.75126 | -42.76408 | 2024-09-26 04:10:00 | NOAA-20 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d424704b-f3a8-3b80-b3bb-c8c592bdf482 | -20.7393 | -42.77421 | 2024-09-26 04:10:00 | NOAA-20 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1930bd8-71f0-3bc2-ad5a-960d7520f8e1 | -20.66094 | -43.09232 | 2024-09-26 04:10:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5bd8e7a8-44fd-3115-b2c1-1f5c03925430 | -20.66036 | -43.09623 | 2024-09-26 04:10:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d39798ca-4039-3f81-9b4a-7c4b6d4942ba | -20.61546 | -43.28107 | 2024-09-26 04:10:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8be30daa-f009-333b-b95f-dbf718d56a57 | -20.61489 | -43.28487 | 2024-09-26 04:10:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ed99140a-85f7-39d0-a2a9-79de9e88637f | -20.50818 | -43.49224 | 2024-09-26 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c18e803c-f1bc-3c60-ba5a-f859239113da | -20.50761 | -43.49606 | 2024-09-26 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d50fdbec-6ec2-3ccf-b90c-2671a3f7a165 | -20.5054 | -43.48782 | 2024-09-26 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 465e527e-92b3-3dd3-9138-617b7da26228 | -20.50484 | -43.49163 | 2024-09-26 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d17fb895-0254-38ad-bdf4-ad7a6f19e036 | -20.41774 | -43.55462 | 2024-09-26 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bc8c402d-3235-3ea3-88a0-3e0ad9fe2edd | -22.24545 | -43.91399 | 2024-09-26 04:10:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 944fbd5c-5827-3628-a39a-8c657c343fa9 | -22.17607 | -43.44105 | 2024-09-26 04:10:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 10e729b9-56b0-367b-845d-06f54687c6ba | -22.17549 | -43.44495 | 2024-09-26 04:10:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2b02a74-c719-3cfd-a013-23f27a62f066 | -22.17492 | -43.44886 | 2024-09-26 04:10:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e9f9a727-6a94-345a-a6df-74023505b9fc | -22.17211 | -43.44435 | 2024-09-26 04:10:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34299da6-fad3-3b9c-bd6b-cd6fc4e5c61c | -21.62694 | -43.46762 | 2024-09-26 04:10:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bc0c17f1-b181-31f5-8434-8e874e62ba21 | -21.39977 | -42.96577 | 2024-09-26 04:10:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 72bd67d4-970c-3ab0-8399-3ebbea6baef0 | -21.39634 | -42.96531 | 2024-09-26 04:10:00 | NOAA-20 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fcd3151b-4e29-344b-a96c-6811ff7764ca | -21.39579 | -42.96905 | 2024-09-26 04:10:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2da73560-69ab-356e-85d2-5a8155b13df0 | -21.37619 | -43.62674 | 2024-09-26 04:10:00 | NOAA-20 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 9a1b3bf9-da25-3d3e-886b-1424efe5dc22 | -22.9028 | -43.75274 | 2024-09-26 04:10:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 70c0a012-b48d-3f23-a64b-aeef14f124fb | -22.80202 | -43.72409 | 2024-09-26 04:10:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a903d6a-a393-3ffe-96f7-5499548d9a12 | -22.77585 | -43.80747 | 2024-09-26 04:10:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 978f972e-181b-3719-b04a-34cb5a041b22 | -22.77526 | -43.81152 | 2024-09-26 04:10:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 925dbdc8-d478-3db6-8ebc-357ab31d5a65 | -22.76485 | -43.01701 | 2024-09-26 04:10:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e74dbb6f-1fe7-3b2d-8954-5f6cd18c6fad | -22.63932 | -43.92788 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2c1d3b16-dbc4-3c97-a162-d862b1be4919 | -22.62506 | -44.02364 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b03d0013-11a3-3cc7-8a98-a1c2b7c40f47 | -22.60386 | -44.00439 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f5c88910-bfea-3122-8a77-cf67a8ca0570 | -22.6033 | -44.00816 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c9ef6fd8-3b6a-31fd-9b42-96ea63906f5c | -22.60273 | -44.01193 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 607313a4-ef66-3e44-b315-c883dc278b1c | -22.60052 | -44.00375 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3f9111ff-1f04-337c-b446-d3caa581351e | -22.59995 | -44.00753 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ddefb904-ec89-37a4-ae16-e4f8d9914625 | -22.59608 | -43.98736 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 70903d06-e371-31de-9eba-adecbf4fcf66 | -22.59443 | -43.97532 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ba66fcb-6149-306d-9170-7c70250ffaa5 | -22.59386 | -43.97915 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c23ff8d2-1cfb-3041-a65c-9e850e53e263 | -22.59273 | -43.98672 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 498d76b4-9b60-3396-8756-1bebb29b98d1 | -22.59252 | -43.97535 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1d2959ea-7a85-3490-b4d0-25dd9c7b06d9 | -22.58918 | -43.97472 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 390f038f-f038-3779-8c5a-c7eb7991c412 | -22.58861 | -43.97852 | 2024-09-26 04:10:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dd65f60b-a799-345e-8a36-0322e6de75e4 | -22.38391 | -43.95591 | 2024-09-26 04:10:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c0f1558e-f5fe-3b65-ae46-09a430424491 | -20.89995 | -43.81815 | 2024-09-26 04:10:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0b2ffe8-740b-3b09-9018-ca86adf5dabb | -20.51997 | -43.93434 | 2024-09-26 04:10:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| db597b9e-84ec-36a0-827b-fb03d3fdbc63 | -20.5194 | -43.93805 | 2024-09-26 04:10:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1becc285-94c2-3d29-aca5-8f53a7ae478b | -20.42905 | -44.10468 | 2024-09-26 04:10:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 659d30c9-42e9-3f99-9b23-38c0e77b9ebd | -20.4263 | -44.10042 | 2024-09-26 04:10:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4bff4116-7f1b-3b72-9ca1-77f9288656ab | -20.42574 | -44.10411 | 2024-09-26 04:10:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b903317-df74-302c-b18a-3ca722e12c36 | -20.12072 | -44.92594 | 2024-09-26 04:10:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c234afc-23bc-3481-88b3-0489907c8a97 | -20.12014 | -44.9296 | 2024-09-26 04:10:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83f37947-0f87-3225-9e8b-c6745ac57b4a | -20.11683 | -44.929 | 2024-09-26 04:10:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a69d46-dd1a-33be-ac45-48194858f311 | -20.78929 | -44.9297 | 2024-09-26 04:10:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| be86f9b9-1b2f-3e20-b561-62e42b7b7db0 | -20.68217 | -45.00524 | 2024-09-26 04:10:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4200df0d-33d6-3337-89cb-d42820f2f4ec | -20.58002 | -44.57573 | 2024-09-26 04:10:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1ac9b003-d766-36df-a817-b9c307bbec04 | -22.30617 | -44.04849 | 2024-09-26 04:10:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 81f9d85d-0aaa-3d9f-8119-129bfb76e2c5 | -22.30283 | -44.04789 | 2024-09-26 04:10:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b48f6076-d5e9-3140-b810-7a80428bb8ef | -22.28501 | -44.0523 | 2024-09-26 04:10:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 179dee84-8575-34ea-bbaa-67e9510a4dea | -22.28444 | -44.05609 | 2024-09-26 04:10:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2aab6046-6e70-3e90-b056-aa8f33bec2d0 | -21.30724 | -43.79735 | 2024-09-26 04:10:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README83.md)
