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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7671eba-36cf-3c4c-b271-a1ff3d28f672 | -6.3039 | -43.647499 | 2026-07-23 00:17:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8cef721-0853-3fd2-b9ab-0fb15ebc3d16 | -6.3001 | -43.632 | 2026-07-23 00:17:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b28ef1c-16db-39bd-a52d-9e3844d61b3a | -12.0364 | -50.340599 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9551abfe-9335-394d-9fe2-c994b3ab2029 | -11.7913 | -47.093899 | 2026-07-23 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5520085-591a-3556-81a2-8fcbe340d6b3 | -11.7348 | -50.372501 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2aeafd-5a5c-35bc-992a-430bfc136ebc | -11.5864 | -48.391899 | 2026-07-23 00:17:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8650394d-90b1-31da-bdf0-9e512d2e047a | -9.1518 | -59.148602 | 2026-07-23 00:17:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52d48ca0-5987-36cf-90b9-09c7a2b01afa | -11.8145 | -47.326 | 2026-07-23 00:17:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65c108dd-0b98-32fe-803e-2601f8bd3f5e | -21.067101 | -45.934299 | 2026-07-23 00:17:00 | METOP-B | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f24defb8-35a7-3c3d-93b7-8cb8ad6ee9f8 | -10.6309 | -47.473801 | 2026-07-23 00:17:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9b69348-e337-3938-9483-c592fa591506 | -5.0899 | -41.6992 | 2026-07-23 00:17:00 | METOP-B | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 556e65c3-0013-328e-8e07-30aa34fb008e | -12.842 | -44.362301 | 2026-07-23 00:17:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50098fb2-6fd8-3b3b-93ce-0e1c34bc7bbd | -11.7755 | -50.370602 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3a3097-bdf9-3076-812c-0973e691f0b8 | -11.7626 | -50.358799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e89a0ac-ba1f-348a-b029-16b2beee7ce0 | -5.7636 | -49.082802 | 2026-07-23 00:17:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eacbefe-bb53-3619-b777-d1a2a631baf5 | -12.0349 | -50.333599 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f33b42ac-406d-3cac-b88c-24319452e159 | -11.7724 | -50.356602 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6c34509-e0c5-3ba4-ae7d-ec964ba877b3 | -21.0452 | -47.778 | 2026-07-23 00:17:00 | METOP-B | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ab7a4ce-a66f-364c-a8ce-274cb7afd090 | -6.0363 | -43.858398 | 2026-07-23 00:17:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31420753-9246-3172-b2fa-e7cba5d398ff | -11.6651 | -50.336899 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78989482-52c6-3083-9b46-d2a0763d629b | -18.7978 | -51.243599 | 2026-07-23 00:17:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab3101e1-5cc2-3465-96a7-90cc565c1cfe | -1.6421 | -53.576302 | 2026-07-23 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa72e5f3-b7e2-3233-95da-3ab3bf4e63a5 | -11.9173 | -50.360298 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c8de453-cee0-3f75-a6d7-b9c3fefc446b | -11.9874 | -50.351799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efb4f38e-309a-3ccc-9599-8b19669c7ce1 | -12.4546 | -49.583698 | 2026-07-23 00:17:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1043dd8-656e-3096-8cef-4183a1dd0a82 | -11.7967 | -50.3731 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b59c020-de57-3be7-8a13-e809a0bfa174 | -12.3254 | -46.7299 | 2026-07-23 00:17:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5cf1764-873c-3132-b2f8-297d2d5e6a38 | -11.9648 | -50.342201 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd5bc2ad-53eb-322b-a085-a6137883e528 | -11.9761 | -50.347 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2106aa10-e5be-3534-9606-78cccc3ab7c4 | -8.8391 | -48.333302 | 2026-07-23 00:17:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc6b2b84-0638-3527-b0b6-660630bf4018 | -11.7384 | -50.3423 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de7de482-84c3-3f0b-94d8-a805bb543ffa | -11.9777 | -50.354 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13a9582f-12ec-35f9-a6bf-004e33e6f715 | -9.1555 | -59.166901 | 2026-07-23 00:17:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 789058ec-ff6f-3d2f-b4a1-845ad18b5c3d | -10.8022 | -50.437801 | 2026-07-23 00:17:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 720e26a4-33b2-35b5-9047-8633ddf5ec0e | -11.8127 | -47.3181 | 2026-07-23 00:17:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c39e2ce-1a65-3f72-b12c-65d8ef84f4b7 | -6.2355 | -48.9828 | 2026-07-23 00:17:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef2f317-66e5-3a95-a193-04b0e164ed28 | -11.8879 | -50.367001 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d816297-be73-3803-b935-da6f551dd463 | -18.786301 | -51.237499 | 2026-07-23 00:17:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dc031833-14df-30e1-af60-0c5078404e43 | -11.9859 | -50.344799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc57221-06ff-3c7a-9fc0-28f9cde24314 | -11.6749 | -50.334702 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b542919-bf44-3f48-91eb-befc55e90359 | -11.9663 | -50.349201 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e42446f-d6e4-3020-9ddb-0d1fc0c30b26 | -12.0086 | -50.354301 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 861d1ebc-01d1-3550-9305-819cf33ef3ed | -22.337099 | -45.931999 | 2026-07-23 00:17:00 | METOP-B | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 60a99c0c-23f1-38d3-a539-3d4f0c25bfc4 | -13.371 | -54.290798 | 2026-07-23 00:17:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09de8996-765e-305f-ac52-7333afc91cff | -9.1093 | -49.645901 | 2026-07-23 00:17:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7d3efb-8df1-3b15-993a-893363a3e410 | -11.6847 | -50.3325 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ca3b35f-7e3e-3e56-b470-57ce2a2edede | -11.8011 | -47.091599 | 2026-07-23 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09385001-782f-32ed-991d-c6557eaef459 | -11.7869 | -50.375301 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55b51de2-83f1-37ec-958e-573b5fb2aec4 | -10.8961 | -51.092602 | 2026-07-23 00:17:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c1c554a-f033-3ecd-a688-c2e5dc2cefd6 | -11.9385 | -50.3629 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b066b828-b205-305c-8122-788ff35659ea | -11.628 | -50.3088 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0b93f93-6775-3516-a6f8-edeba92de5ef | -11.9988 | -50.356499 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e6e56e8-a135-3fd5-85f4-e45927e7580c | -12.0003 | -50.363499 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6df802f-4fa8-3f1c-8f9e-2183fe171853 | -12.0215 | -50.3661 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90219b3d-d6e9-3f5c-b3a6-f1a916d876a3 | -12.0101 | -50.361301 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db57f1c0-9cc1-30f3-a48a-bbe75a25b757 | -11.8426 | -50.348 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa60dbc1-918b-3687-a3d8-5d4efb248792 | -11.9189 | -50.367298 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9ef28cd-454a-3846-9bc6-620b5eb7829c | -11.7982 | -50.3801 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04f7b79f-2d17-352d-b368-c2e560bc89eb | -11.9354 | -50.3489 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8dc99f61-38ef-3c25-8929-26d8f7905e1e | -11.6765 | -50.341702 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d59be7f1-f3ad-3a3e-ba11-f386ae66f551 | -11.6976 | -50.3442 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d3175b1-3a48-30cb-8ae7-5f334193b285 | -7.0057 | -45.4076 | 2026-07-23 00:17:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86091e9b-b51b-3aa6-be3a-735173d583cb | -5.0953 | -41.721298 | 2026-07-23 00:17:00 | METOP-B | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fcda124c-9ade-3d71-b39c-f54d156ead31 | -11.9452 | -50.346699 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8c9b6e-71aa-34ba-9843-081fad51c407 | -11.7399 | -50.3493 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17ba8a3f-ee22-35e1-a7e0-8a3c0f454440 | -11.9679 | -50.356201 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30ad29a0-37c1-36b0-8de3-71d63fb1ac54 | -19.709499 | -48.072899 | 2026-07-23 00:17:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fdc119fd-fac4-3256-955b-ce29ba563716 | -11.6878 | -50.346401 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4748fbb2-0962-352a-872a-bee33fc33b49 | -11.989 | -50.358799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd350791-b173-3814-b2ec-cede498e45db | -20.1145 | -50.4753 | 2026-07-23 00:17:00 | METOP-B | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63a340ea-06ca-3ca8-a52d-a472db469b59 | -8.8081 | -49.364899 | 2026-07-23 00:17:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2105eb3f-f60f-37c7-a1e5-47bdb9370296 | -6.046 | -43.855999 | 2026-07-23 00:17:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15da28ac-5b0d-3bdc-8bd2-0477860d34cb | -11.7838 | -50.361401 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8a71aba-76f9-3dc0-9555-3ef6cdac1913 | -22.291401 | -47.259998 | 2026-07-23 00:17:00 | METOP-B | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b2180062-6ade-3085-900f-3a7110f986a3 | -11.9746 | -50.34 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d242882-77b7-39d8-b5b1-48eee1450980 | -11.803 | -47.0998 | 2026-07-23 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 052c123e-09b1-3989-ae39-e859a8c09fbc | -11.7513 | -50.354099 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05ee9078-7abc-3ccf-807a-ce47bfc9f627 | -11.7894 | -47.0858 | 2026-07-23 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cad963c3-a438-3fe4-af88-8823d279a8e1 | -11.8895 | -50.374001 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b7c9db7-b1c9-3e94-8db6-1a02247b8f77 | -11.9972 | -50.349499 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3fcedf-4197-3458-8f2e-1215c8dbdf17 | -11.3935 | -47.468601 | 2026-07-23 00:17:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5079c69d-3523-38a4-83f9-7f4f21d6cb4d | -18.788 | -51.2458 | 2026-07-23 00:17:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c528874e-1e09-3d2a-a3c5-d6d73af071a2 | -11.7951 | -50.3661 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8040876f-1eae-39dd-ab69-d49a0a17e699 | -7.0357 | -45.533298 | 2026-07-23 00:17:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d943daa6-8431-3963-ae25-7c36a2cfc946 | -11.9369 | -50.3559 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3c40b10-e3eb-36d0-8ee3-8a43bfaa0db8 | -5.6327 | -47.0965 | 2026-07-23 00:17:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de81b836-a6ad-3844-bb16-8cfaef7998d8 | -20.5144 | -48.8493 | 2026-07-23 00:17:00 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b1b305ef-daa9-3692-8ac9-dcf3035876d9 | -11.7796 | -47.0882 | 2026-07-23 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04cc7615-2398-3aff-ad73-2dcdbe787f19 | -11.9075 | -50.362598 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9057a756-986c-3de9-9687-23ae1e1c4f72 | -11.7834 | -47.1045 | 2026-07-23 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bacd8b67-e5ca-359e-9f41-9af4bbd39c49 | -11.6983 | -50.3415 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c9d58553-7ea7-34a6-b411-afeff0eb3279 | -11.698 | -50.3629 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| c1b434d1-520f-3314-a1c4-107674c0c710 | -11.807 | -47.0858 | 2026-07-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8db49882-8290-3fda-af91-5beca9275508 | -11.7683 | -47.1134 | 2026-07-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2779f608-e1cd-3c3d-b90b-c24428ab7db6 | -11.736 | -50.3585 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| eefbda3f-7111-3782-b225-af098cabf839 | -11.7741 | -50.3541 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 38dfbdf3-30a9-3318-b127-53e07effe448 | -11.7875 | -47.1108 | 2026-07-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 8d88cdc3-67d9-3f8c-b9d5-9fa85958da46 | -11.9069 | -50.3815 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 689a0f05-1438-3333-8209-38603de976b7 | -18.7804 | -51.2453 | 2026-07-23 00:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 99ebaf52-d2e8-3fe7-a151-fe96b2438b74 | -11.7738 | -50.3756 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |


[Clique aqui para ver as próximas entradas](README3.md)
