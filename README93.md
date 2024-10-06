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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cad3b00b-5660-3525-b5ec-0ed762e7459e | -23.72157 | -50.05967 | 2024-10-06 04:21:00 | NOAA-20 | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6324d400-33fc-3a25-a29b-453561216187 | -23.14718 | -49.81319 | 2024-10-06 04:21:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a391bda6-6d17-334f-9be0-661909f7269d | -16.4707 | -49.94104 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 662e39bf-8602-3546-8310-3da56bd51ee7 | -16.42545 | -49.86906 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd557d38-19c4-3063-9a55-bab9cbbeb685 | -16.42241 | -50.17743 | 2024-10-06 04:21:00 | NOAA-20 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7468bcf8-f098-3240-9d87-165fbc2f5682 | -16.42261 | -49.86425 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdf5adc7-36ff-3ad3-8d38-81f49b977624 | -16.41339 | -49.87549 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bf7c37a-6a35-3042-b366-79f230351bed | -16.3558 | -49.93357 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dce9f222-4a2d-382d-b294-d3a70e273878 | -16.35296 | -49.92879 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 627cbba3-09a8-3b17-9518-5f932707bd86 | -16.44497 | -49.45521 | 2024-10-06 04:21:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df745213-d1b1-3e6e-902c-19ee168b989a | -16.44428 | -49.45926 | 2024-10-06 04:21:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64109647-eee6-3008-b1d8-ba14c9481e06 | -16.4408 | -49.45861 | 2024-10-06 04:21:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86921428-fb55-3050-80c3-5f91edfbf872 | -16.42687 | -49.92551 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ee3ff17-1a81-3d34-ac73-b48f067cf166 | -17.30875 | -49.33148 | 2024-10-06 04:21:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffe33db7-e2bd-3d79-8680-6d5de9cc7917 | -17.30663 | -49.32309 | 2024-10-06 04:21:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b989f1d-60e5-33e1-85ec-f8ddba542fc6 | -17.30597 | -49.32697 | 2024-10-06 04:21:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 517537bb-bfba-369b-a4bf-a730a572e555 | -17.2942 | -49.45892 | 2024-10-06 04:21:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b44fd652-1ad5-3ee4-a509-5f0e9d0d32d7 | -17.29075 | -49.45828 | 2024-10-06 04:21:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1efe95dc-b488-3c53-a0d3-4ebb2170c6f6 | -17.29007 | -49.46228 | 2024-10-06 04:21:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e226df7-8825-34f2-9d02-0d502a8675f9 | -16.78425 | -49.19162 | 2024-10-06 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6ddec176-dfe5-324c-84fe-fa2f8f95be78 | -20.45276 | -49.98197 | 2024-10-06 04:21:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 476435f7-b343-3011-8626-c18857db57f2 | -20.4521 | -49.98591 | 2024-10-06 04:21:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1e651be-c5a4-3bf0-9eec-6d6373b92d82 | -20.44097 | -49.94698 | 2024-10-06 04:21:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0dadbed8-963d-3021-9d7c-10184f7649b3 | -20.43755 | -49.94635 | 2024-10-06 04:21:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7adb06d4-50f6-3bb8-871f-f0ddccefec7a | -20.46038 | -51.28495 | 2024-10-06 04:21:00 | NOAA-20 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| 2d7fec63-0566-3ce6-8c7e-32b38bbe95b8 | -20.45756 | -51.27985 | 2024-10-06 04:21:00 | NOAA-20 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 88b2b9c8-9840-361a-94fd-99a04d820a38 | -20.45677 | -51.28424 | 2024-10-06 04:21:00 | NOAA-20 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 134b39c7-429e-33eb-b8b8-e60f54148fb4 | -20.14038 | -50.35177 | 2024-10-06 04:21:00 | NOAA-20 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 35734217-7b9d-3257-b2b5-59361b8258c7 | -20.1376 | -50.347 | 2024-10-06 04:21:00 | NOAA-20 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c7ebebc0-ee2d-343e-bfad-b536b818986e | -20.13691 | -50.35107 | 2024-10-06 04:21:00 | NOAA-20 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 087cbfe3-5d87-38dc-b617-3dedc231a9bb | -21.52405 | -50.90369 | 2024-10-06 04:21:00 | NOAA-20 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 954a57c3-f137-37b4-aa31-b2f45a394064 | -21.51982 | -50.90717 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ade85c3e-e179-3406-9568-120db0f96969 | -21.51632 | -50.9065 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 74b7e513-2081-3c9e-b569-1df243edc0b1 | -21.51281 | -50.90583 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 22c0bb54-9821-3816-80eb-bb9e120be3cd | -21.51208 | -50.91 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 56d49b44-1e16-366f-856a-69fbd34b4601 | -21.51134 | -50.91417 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 305a3ff5-f1b0-3fcd-aec4-22a342f35725 | -21.51061 | -50.91835 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| beb39350-c7f4-3469-ae0e-148633dbe49e | -21.5093 | -50.90516 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| a1d0cea6-90f0-3f36-a31b-a3f81b351010 | -21.50857 | -50.90933 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 66903263-5cc9-38c3-aa2f-3254eca353b1 | -21.50784 | -50.91349 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| c2d2fd0d-3d26-3fb7-9d26-791e9497157b | -21.5071 | -50.91767 | 2024-10-06 04:21:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 93cb58b3-164e-3259-9d45-1548656773b9 | -23.4198 | -50.53588 | 2024-10-06 04:21:00 | NOAA-20 | NOVA FÁTIMA | PARANÁ | Brasil | 4117008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e9a35512-3f28-382c-bad8-442fd2f2897a | -23.0983 | -51.60968 | 2024-10-06 04:21:00 | NOAA-20 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 05fe9ea2-a850-37bc-87c9-8b5e40698c09 | -23.09754 | -51.614 | 2024-10-06 04:21:00 | NOAA-20 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| bea9230f-3b0b-3e09-994e-0d48de2d14f4 | -23.09477 | -51.60887 | 2024-10-06 04:21:00 | NOAA-20 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 19377f47-ce02-3b73-b9ca-c87140efefd4 | -16.3211 | -51.27893 | 2024-10-06 04:21:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96f401a3-6567-33b2-99c4-ae81f5f15ede | -20.99397 | -51.79414 | 2024-10-06 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| acf8c328-acec-32aa-a5c5-d3f99612d1ab | -22.7106 | -53.24557 | 2024-10-06 04:21:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a1a73ea-d423-3ab0-ab0b-357e95ca96bf | -22.60686 | -53.04359 | 2024-10-06 04:21:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 29d10637-e45e-380e-859a-d43cd6bebd9f | -17.68796 | -53.07846 | 2024-10-06 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d095696-3906-3b75-88dc-db65ce476dfc | -17.82249 | -53.76789 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53a82787-b4a5-36ed-8783-5b99564f5212 | -17.82172 | -53.77185 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a5f7e26f-6076-3e4d-ae77-a4b452c165bb | -17.82098 | -53.77566 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| be9bf6b4-600f-30fc-8c0a-8978ef7aa395 | -17.82018 | -53.77976 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8e98aa3d-d668-3569-b607-457fa166e4fe | -17.81921 | -53.78477 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8fd3700c-7cc3-3b50-b879-2812db6f4bf3 | -17.8174 | -53.77086 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b625ff4d-4e3b-3124-82da-fd046ed33e9f | -17.8163 | -53.77187 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68def71d-5dbd-3a86-b701-302bfd85a42a | -17.81486 | -53.78394 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e4656bee-070c-3344-8c7f-0b25c1665566 | -17.81379 | -53.78535 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5d25e558-8082-347f-b4a5-f5ff26af4b08 | -17.81309 | -53.76987 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7bdd285-20e0-38bd-af34-ca179a7aa174 | -17.81229 | -53.77394 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3a9cbece-b1a6-3f54-839f-cb426bd28667 | -17.81199 | -53.7708 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8ae78f83-9367-3f0c-8a0f-d985ef0aa340 | -17.81148 | -53.77816 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e9511388-bd90-3cd8-9c8a-25445db9965a | -17.81121 | -53.77497 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 70836cba-f29a-3381-88cc-6a126979b51c | -17.81051 | -53.7831 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a49a35da-34c7-3498-8ffc-98985371885b | -17.81039 | -53.77938 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| decb2bd7-f4ba-3067-ad50-88753f5dc44c | -17.80944 | -53.7845 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 15f2bdaf-7b8a-3f07-92ce-7b749f6653c4 | -17.80617 | -53.78225 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3a4d21a1-03fa-3ebb-9568-9308ef5dbead | -18.81936 | -53.75862 | 2024-10-06 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89ec84dd-bf2f-3c02-9ac4-9b0a5cf854b1 | -18.81428 | -53.76202 | 2024-10-06 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60f73be1-61e1-3977-96de-05cb9f6fba4b | -18.80919 | -53.76541 | 2024-10-06 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4cb33d5-9ef9-3cf7-b563-82e40cd48144 | -18.80836 | -53.76973 | 2024-10-06 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a105c426-82b3-3f79-b97f-1927956621b2 | -18.8041 | -53.76881 | 2024-10-06 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14d627c7-66bb-3b6e-a29b-4bcbc1211606 | -18.80327 | -53.77309 | 2024-10-06 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f08c8027-7e67-3d51-b8f4-61338cdbbaf0 | -18.79902 | -53.77214 | 2024-10-06 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf526b1f-daf6-38c8-82a0-6600efc47d6c | -20.27964 | -56.93835 | 2024-10-06 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ad3a790-401a-3926-b675-e93c2890609d | -17.81824 | -53.78977 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ac833ab4-2ab9-34a2-87ee-0172314715f0 | -17.80952 | -53.78817 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e301cee2-1a7e-38f6-ada2-a33b505281ee | -17.80852 | -53.78944 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9bb9dce3-2b60-3f84-859e-b014c64ab95d | -17.80518 | -53.78733 | 2024-10-06 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eeb07d42-ffe6-3e1b-a5cb-197f2efa2366 | -16.86346 | -54.83877 | 2024-10-06 04:21:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b91a27bf-d9b2-3403-b2f1-47d72d47ab23 | -17.01297 | -55.0571 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 94c30fca-a273-3c2f-abe5-fe20c84870c3 | -17.01296 | -55.06137 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a0ed6323-3947-3b49-b2e3-5e867e8d1ac0 | -17.01241 | -55.03854 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 28fc8db7-7bdd-35fb-b668-e4e6729dd7b6 | -17.0119 | -55.06683 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 66f1b1a1-006f-3dca-b4fb-1c44c7bf90b0 | -17.01187 | -55.06255 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 84be5f99-ed32-3e9d-b504-8381c01cff3f | -17.01148 | -55.03977 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 31493d16-52f8-3127-9669-f2d6e17c9753 | -17.01136 | -55.04397 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0b2af3b3-b24d-3243-be22-d27452003faa | -17.01085 | -55.07228 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 20621bfd-fd5f-3c0a-bb11-8d1de3c56222 | -17.01077 | -55.068 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| efa08ae8-9b1c-368b-9680-70ac2753491c | -17.01039 | -55.04519 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| b8b116e7-c07d-3f4b-bca7-9808bceb745c | -17.0103 | -55.04942 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 338bbd3c-f0f8-3f5b-aa8f-d9542bdf7ac2 | -17.00968 | -55.07344 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 55c67810-27ae-31d8-bb1a-653b6d3ac395 | -17.00929 | -55.05062 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3ea690c5-d8ab-36c0-b68a-6b8412427cb7 | -17.00924 | -55.05486 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| ead4a9ee-1859-3777-8453-21384fb7a240 | -17.00819 | -55.05606 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d7920db0-1d67-3b79-a970-035dbdf2b1ca | -17.00818 | -55.06032 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6fcee4a9-a4d8-3cc6-8bf8-6fc3b12210c4 | -17.00713 | -55.06578 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| aae7dab6-a6f8-39a0-a4f6-99516df28191 | -17.00709 | -55.06151 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1cbfa11c-033f-399c-b13d-ad17c956fda5 | -17.00671 | -55.03873 | 2024-10-06 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |


[Clique aqui para ver as próximas entradas](README94.md)
