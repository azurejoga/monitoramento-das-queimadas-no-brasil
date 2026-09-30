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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9994749-c573-35c1-b1e9-b8bae635d9da | -15.44297 | -45.68845 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23e82a22-746c-3a31-bd6b-396a4eada222 | -11.42617 | -43.48928 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8c6af9d-1e4f-3937-a3c5-d188e745872f | -12.31453 | -47.95376 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0644c28a-4ade-33f1-bbe6-f29de12540b6 | -10.73698 | -44.43722 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82106653-0280-32fa-aefd-e099d0ecab41 | -9.80689 | -44.8315 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95eb8361-e43c-356e-8686-adbb511e740e | -10.75814 | -52.12997 | 2026-09-30 04:34:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ace943ff-4dc0-3c3b-8f96-f21cc384ba8f | -12.8361 | -50.62436 | 2026-09-30 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 88533dd3-7134-30a7-9078-2d80773ba39a | -11.1711 | -44.81423 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2b7ef74-88d8-3332-898d-f72729949956 | -12.30422 | -47.9519 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d56dd3a9-3edb-3e5a-b695-dc2ac747a1e8 | -13.90066 | -43.9269 | 2026-09-30 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0518ca7-0022-36f5-8b85-f87d40e3009d | -11.63272 | -43.52778 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 666a9713-3300-3ff6-9dc9-345352206f14 | -11.8399 | -50.4722 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 791707e7-d619-388c-9e0f-9c6a84d85643 | -12.56738 | -43.07394 | 2026-09-30 04:34:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce616af3-05d5-389e-8f2f-4a3ee45d513c | -11.84687 | -50.47865 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 878cbeb9-889a-3687-a6cd-81ed6955bbee | -11.35174 | -50.98145 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e983b27-712b-360e-8516-439a42294f13 | -12.30359 | -47.95569 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4adf165e-8daf-33b6-bdfd-6a40fe49aee7 | -15.99567 | -48.07468 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a8a29cf-e0dd-3e5e-a069-e2fc729e0c1c | -11.2656 | -43.52889 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e429215-0a58-32cf-bdfb-ba3bb4b5478f | -12.26561 | -50.28401 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34545171-2400-3670-bf32-3633c3f95b0c | -11.39989 | -50.99403 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a29a8220-4b7b-3b9b-b3c6-9914f3bc7e66 | -11.34961 | -50.96982 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c43a368a-0a14-3a69-a802-026760dbf534 | -13.37761 | -44.00751 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d0dc983-bafa-3df7-9c92-fae9f9e15a02 | -11.16889 | -44.8285 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1eeba7b-5670-328c-927c-2186e6eeb449 | -12.25876 | -50.27778 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ac939f7-7a92-3e07-9724-195c35f628e1 | -11.83582 | -50.46897 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 165ed9d2-b8eb-3bc1-b94e-7590b693048a | -8.48383 | -54.91369 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 362cc084-1930-3e9e-a2f7-c0f019dbab67 | -11.19682 | -44.82569 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12e382f2-f48c-3092-901e-58d05c17e935 | -14.53579 | -48.30226 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e87462a6-6395-39cd-8eb7-2eb2a8cdbd9a | -11.67043 | -44.51469 | 2026-09-30 04:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 534bd9b9-9e12-3d74-b99d-117dee6a2498 | -10.11157 | -43.92629 | 2026-09-30 04:34:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cb37977-6e37-3b88-bc18-ed83c1aad90e | -14.2 | -42.07458 | 2026-09-30 04:34:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 82e251a1-a210-322d-8fe4-23f0c03fc560 | -11.36906 | -51.02605 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcb6ad99-796a-3483-a6ac-3f59ffb6246e | -10.84097 | -48.7165 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f4222e8-e760-33e9-821e-de4d2d42cffe | -9.41618 | -51.7254 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58f685e9-3751-3e98-a603-7401df8ad613 | -10.5805 | -50.85047 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b7eb28d-a27a-3e0d-93b5-0ff8549b411e | -12.78384 | -53.99852 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deababb6-1ee7-395e-87a6-21e9019a6d71 | -11.39773 | -50.98238 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd01e838-e05d-3499-a061-913d2da624b6 | -14.53705 | -48.29473 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49d2df80-33b5-348e-a419-d029cc8f0529 | -10.68046 | -50.28453 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5be4123e-50d6-3d86-aa52-d76204d4474e | -13.3762 | -46.82422 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fcdc1f0-a582-37a6-97a0-2b8fc456ac61 | -11.12296 | -45.91583 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57996d95-d1bf-38fa-99c8-308dff1804e3 | -11.68286 | -43.50628 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdd53f8f-a874-32c7-ad9a-2aeb0c6c7802 | -11.84283 | -47.78672 | 2026-09-30 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42866c8f-d61f-307f-9a7f-b83c42d5b01b | -15.76267 | -46.03824 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48c9d76d-4b36-3c17-8c75-ee37f85dd509 | -10.79002 | -48.75494 | 2026-09-30 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57123c0c-5309-3342-9b6a-816e029d71b4 | -15.77775 | -46.02956 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 872be638-b5ef-30f9-b673-0c9fd01dd12b | -13.37734 | -46.81715 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b067888-af35-31bf-a45f-c2713d9cff08 | -10.69763 | -44.42367 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a92444a8-f4f2-3922-8d52-ff110550f122 | -8.26565 | -54.75441 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ce84c98-5230-3b8b-a7e5-3bc9f1e1e89a | -9.79113 | -48.23032 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39fa339a-0171-3ec7-be2b-21835251580c | -14.51156 | -48.27879 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f93dd78-04ce-322f-bc13-d33bf41b3363 | -11.83883 | -50.47469 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b28dceb1-7d67-3824-ae8a-15b9c4403a68 | -13.54436 | -49.16961 | 2026-09-30 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d897d1ce-0b1a-3beb-8053-dd1d22ac1a88 | -15.77832 | -46.02592 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6da365d-379e-39ee-9e5d-fed4586bceb9 | -11.39862 | -51.00132 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4f4ed06-6d7f-3883-ab40-a3847eb0c4f6 | -16.11765 | -42.22037 | 2026-09-30 04:34:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 16909ac1-7f37-3837-bec3-3506acebe51c | -13.37343 | -46.82013 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b193c4ef-bee0-3860-bed1-dc4cd274450e | -11.25632 | -43.54328 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 646cf772-be73-3011-8541-259d88dac703 | -12.88096 | -44.80118 | 2026-09-30 04:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcb4730d-64d3-3952-826e-48c5f5104e26 | -11.29447 | -50.97913 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 241aedec-2050-33e5-a4ea-751ce03e10c6 | -10.25727 | -48.33035 | 2026-09-30 04:34:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f17c043-5f97-3736-9f76-2c6c7b809304 | -15.75876 | -46.04132 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0141aed2-b0b9-3da7-b2fd-d60f17e0dfd3 | -11.1728 | -44.82547 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3bf29be9-d166-3e7e-90df-f7e2b5d6daaa | -13.74117 | -43.76497 | 2026-09-30 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4a6a5c4-7df4-3f7b-99d7-64c148bb8359 | -11.844 | -50.95568 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5dadea09-a98d-3c0f-b5ce-24123c8667f4 | -13.54118 | -52.22292 | 2026-09-30 04:34:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 674b10b9-b332-3168-8c8d-fdae0aa8857b | -9.86035 | -44.94159 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07afed88-cbac-3366-8953-5ce816bd3b86 | -12.06475 | -46.46178 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00b09272-7505-3555-8041-f90a18f1a050 | -14.80162 | -45.96038 | 2026-09-30 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c7db871-e7be-3530-8a19-c80c8d029e92 | -12.51466 | -43.0828 | 2026-09-30 04:34:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2594697e-e732-38fa-b9ed-110801ebb36d | -11.51647 | -48.3205 | 2026-09-30 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16af3667-3530-319e-98de-62137881ede9 | -10.81801 | -48.72084 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2f213fa-c8ea-3608-b4ea-d36e8b8ec154 | -12.78081 | -54.01457 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4ec814-328e-35f4-b73a-759ee6866895 | -8.31976 | -54.7632 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d04daa1-a84c-303e-a766-b334aaef9a50 | -10.7098 | -47.83084 | 2026-09-30 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 619d68ed-273e-3f26-b611-e47b807f5a78 | -11.33076 | -50.98137 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a599816-ddd1-3215-8c39-dfff0802b76f | -12.24378 | -50.25019 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22b74513-4a17-3837-a9bd-14b2d95edbb8 | -15.57487 | -47.89293 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56d2bd1a-69dc-3d8d-acc7-0b24b1d5c935 | -12.43093 | -44.1693 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7446ad3b-8bea-305e-a04c-01cfd83820a5 | -11.41873 | -43.42006 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccb4bf29-b471-3a7d-a3b4-dc4e8fae222b | -16.42513 | -43.29505 | 2026-09-30 04:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e028a40-e298-3177-8f2d-88988970f690 | -11.84688 | -47.78353 | 2026-09-30 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5290095a-b6aa-34fc-847b-9f1adb10b48f | -11.39964 | -50.97149 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e6ce860-7f96-3af0-bfa3-71a395a9127a | -10.68439 | -50.28523 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dee35b21-756f-3c4f-8ce2-a652d16312d6 | -10.52526 | -50.75765 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8689eedb-1fab-3408-ba49-c4c09ecad442 | -11.66761 | -44.5105 | 2026-09-30 04:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cea042f-80cb-301e-94d3-d35c7c0a4225 | -16.80515 | -42.57261 | 2026-09-30 04:34:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b900fe1-1447-33f3-8197-264e20cc403b | -11.35645 | -50.97855 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcd87ec3-ab27-38e4-aa36-266a913428d0 | -11.83599 | -50.47149 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1a2ae6c-a2dd-33bf-a50e-5359dc15ae79 | -11.35672 | -43.35127 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 180bef61-b2e3-3c5b-ac41-b4e0f4e6f6c2 | -11.83872 | -50.96209 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ae088a94-1d8e-32c9-bc91-4f2f37276e8c | -13.37066 | -46.81604 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d66d4a7-7e95-3977-acda-dec7a133e90b | -12.43379 | -44.17362 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be1cbf4e-9f31-3605-af13-bade214034de | -15.12643 | -43.62421 | 2026-09-30 04:34:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b122cd6d-dd0b-3796-808f-cee75aabb3e1 | -11.40053 | -50.99038 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fa9868d-53d7-3a73-8e0d-f60697b38934 | -11.82012 | -46.90119 | 2026-09-30 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d998d08-0578-31fa-b764-397c6dd2c937 | -11.17615 | -44.826 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5e996316-86e2-3e85-b158-755b25f412e3 | -15.08735 | -48.32688 | 2026-09-30 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9a66b2e-202a-3d6b-9289-2e145fb3c6c5 | -10.06 | -50.89164 | 2026-09-30 04:34:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d4bc222-afa6-3c47-95f1-125589e6eaf1 | -12.94482 | -46.64336 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README35.md)
