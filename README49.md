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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b5aba01-1e25-30b9-8f7c-bd1fbaf4e009 | -10.22954 | -56.26616 | 2026-09-15 04:34:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ce70575-d4fd-3b19-afa8-f396efaacc13 | -8.84035 | -45.87578 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 561bdc73-36c5-3b89-92f9-6e4356b913d0 | -10.4746 | -50.99512 | 2026-09-15 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a194ba06-32ea-3bc4-849d-20b64a48e0d8 | -8.46368 | -50.76977 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b56aef6-aa07-3de1-bb13-631ba42b9b48 | -14.86568 | -49.95422 | 2026-09-15 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a97c49f-af16-3442-bc76-0594821ddbd5 | -13.77508 | -48.82506 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30200585-6397-32db-9ebb-e1ff979e439a | -17.31105 | -49.23123 | 2026-09-15 04:36:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| daeb33b0-1766-3fe4-a2fd-94006417e937 | -15.5271 | -53.84662 | 2026-09-15 04:36:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22e20d87-c6f1-3468-93c2-d6bef803e488 | -15.55147 | -48.82607 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27b36e8c-3b20-3d63-b455-3f3df107c553 | -17.44398 | -41.91079 | 2026-09-15 04:36:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 666690b6-421d-3585-abf3-ec3634b576ce | -16.86159 | -50.15611 | 2026-09-15 04:36:00 | NOAA-20 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89fb2d15-79c7-34f0-8315-4a457b8a678f | -16.99138 | -45.46796 | 2026-09-15 04:36:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99d12f17-2b8e-3f63-acac-14740f5eadd6 | -17.98503 | -44.32876 | 2026-09-15 04:36:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2074888-b58b-3a9f-93b4-473e3c17587c | -18.48108 | -51.74063 | 2026-09-15 04:36:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a02148d3-a5f2-3ff3-a7f8-0bef0ccfa791 | -15.57759 | -48.79016 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ecc68c-e9a8-3643-97f0-aa88083f228a | -18.16906 | -51.75893 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b484805-e38c-3462-8e23-87f56ed805e0 | -15.53573 | -48.79797 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15a0e180-bb81-3021-8470-016c75dbc60a | -16.96673 | -43.36024 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a4f82e8-0e9c-3e13-90ea-312e677413eb | -15.58752 | -48.79182 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f842d3a2-0688-3f96-b5a0-6b250bae5ca3 | -15.36328 | -52.99973 | 2026-09-15 04:36:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f105ba29-c867-3b83-8c08-7223b638c0bb | -15.53516 | -48.80154 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ffb1179-5fcf-3cfb-8f04-35ef2c77fc1c | -16.05181 | -52.27555 | 2026-09-15 04:36:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ff3bb3b-af09-3ac7-b34a-3bd20ab626d0 | -16.9704 | -43.36433 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97928af7-37c6-34e4-8244-b8d6cfb66e83 | -16.50689 | -47.81876 | 2026-09-15 04:36:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a9b0ad8-e4bf-3b47-bd16-6f963858baea | -17.44855 | -41.91138 | 2026-09-15 04:36:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a9b1eaf6-9c85-320e-baa5-ad0f863481bd | -17.87088 | -44.34756 | 2026-09-15 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c087e36-266e-3bc5-8933-b922963ccacf | -16.9723 | -43.36733 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 251ab1da-28b7-3b95-9b02-00e473e19360 | -18.47482 | -51.73529 | 2026-09-15 04:36:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6ab98c1-7b32-359f-905f-cdbdca1cbace | -16.99566 | -45.4641 | 2026-09-15 04:36:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56a9d73d-cace-318a-9958-29bbbc1cb32f | -15.53047 | -53.85108 | 2026-09-15 04:36:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3591aa09-e141-3e4a-a9a1-ee4af71729b3 | -18.17116 | -51.76773 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 893e7135-6425-31e8-9b05-ac9d2b42ead0 | -15.54211 | -48.82081 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d39e3d4-7cf9-37f5-910a-5c49b0a7ed97 | -17.31867 | -46.91303 | 2026-09-15 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3a6ab8f-49c0-3cb2-8049-bde67de797a1 | -15.57816 | -48.78659 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c080c63-03a7-3528-a64f-f34c03c47c3a | -17.35003 | -47.17109 | 2026-09-15 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30f8bbb9-d353-363b-ae69-46cac039ea3f | -15.86735 | -50.18302 | 2026-09-15 04:36:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2ef9e96-e836-398b-a22b-ebb47a7c6388 | -17.20803 | -41.48846 | 2026-09-15 04:36:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 14482f6c-1522-34b3-8d87-d447cecf94b9 | -15.58147 | -48.78715 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac009443-cd93-3e0b-bb6c-b1dac32278ee | -16.023 | -49.44459 | 2026-09-15 04:36:00 | NOAA-20 | SANTA ROSA DE GOIÁS | GOIÁS | Brasil | 5219506 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb2832ec-4419-3c35-928a-b3bc94fe7392 | -15.58183 | -48.82758 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9a40c14-ea23-3342-9998-55b847672285 | -17.98436 | -44.3338 | 2026-09-15 04:36:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d41a1ca-2897-31aa-98ea-06abc63176d0 | -15.53451 | -53.85186 | 2026-09-15 04:36:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed55e61b-ea67-3448-8825-aeb7f6c76b7c | -18.17047 | -51.77177 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b114342-df75-360f-8c33-f71a0fbe3c2f | -16.49184 | -47.82751 | 2026-09-15 04:36:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cc8981b-35ce-3aca-bebb-5e5df247ebfd | -18.48038 | -51.74468 | 2026-09-15 04:36:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d852f184-08d7-33cb-a59c-f38f9818a16e | -17.9837 | -44.33883 | 2026-09-15 04:36:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09a9318c-ad4a-3ac8-9a2f-d40b70a7500c | -15.53889 | -48.79831 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 016f1241-a934-3b8b-a18c-08ab4fbd298e | -16.96724 | -43.35647 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dbd5289-becd-39db-bb3c-e63efa74df01 | -16.51146 | -49.97417 | 2026-09-15 04:36:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19d90dab-0cae-3ee6-b3d0-b864cad99d88 | -16.21553 | -47.50467 | 2026-09-15 04:36:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc0806e8-e22c-3730-969a-653d7aa3a48e | -17.98044 | -44.33308 | 2026-09-15 04:36:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57f5a39d-9e5d-3467-9f96-a37662509f23 | -18.87114 | -42.00839 | 2026-09-15 04:36:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 034daf8e-7bd1-3605-aeef-42ec768fa8c7 | -18.47691 | -51.74402 | 2026-09-15 04:36:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc2c5252-8527-322d-9070-440b163c55bd | -16.97276 | -43.36371 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5ae9634-92bd-3623-8d5f-1d5d16015957 | -15.55204 | -48.82249 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 854461ab-5c15-3916-b312-5b39b9f9354e | -17.46876 | -43.66183 | 2026-09-15 04:36:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca9106bf-065b-3ef1-a778-2fba542ef030 | -16.48219 | -43.42044 | 2026-09-15 04:36:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 773a1254-e2e5-3ea7-9d1f-7e8d22feeb1a | -15.54268 | -48.81725 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c7ea677-e839-38ee-ac83-4ca5a1d74a54 | -18.79104 | -46.46964 | 2026-09-15 04:36:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aa48f2e-a8c4-316b-85d1-d749cdee348a | -15.58364 | -48.79485 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3af683d2-5e2e-362f-8daf-c789ffe26ee7 | -16.48572 | -47.82278 | 2026-09-15 04:36:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef29416c-6be8-3211-b3ca-bbd4afbfda2d | -15.54816 | -48.8255 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 799f669b-4f77-3c11-b834-d839b9a9c9e3 | -15.5346 | -48.80511 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf032342-ebb3-3675-90e1-97a138d11902 | -16.48906 | -47.82333 | 2026-09-15 04:36:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da98d45e-3431-381c-9d95-a2184a8398a3 | -16.97088 | -43.36066 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed3b9edb-6279-34cf-8fa5-b01b6f4118f8 | -17.34944 | -47.17501 | 2026-09-15 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7ffbfa1a-0cdd-342a-8406-7d8e2a99ab77 | -15.57872 | -48.78304 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78aa6dae-dd18-3bac-90e6-c038f03bd2e8 | -16.9737 | -43.3563 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 552764da-6fe0-37b8-b2f8-7eb1ef7cb678 | -17.34661 | -47.17056 | 2026-09-15 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 529f60d3-6a5f-349a-b213-e63a8263bae2 | -18.14028 | -42.85378 | 2026-09-15 04:36:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0cf20971-6cef-39d5-85d7-80512b5e7026 | -16.51973 | -47.80209 | 2026-09-15 04:36:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b01d2418-6dd0-3167-a937-f24a66705e8b | -18.8665 | -42.00776 | 2026-09-15 04:36:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 74b25d75-968d-3d6c-8b54-deb107788f87 | -15.53776 | -48.80544 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5d7b13e-3a26-37f9-8e71-35c8b3829af8 | -16.97322 | -43.36002 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff9c7d2c-97b3-3616-a87f-bd350ca2e246 | -17.46263 | -43.64545 | 2026-09-15 04:36:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfd3a77f-04ad-33dc-9888-c28b2a4411e6 | -16.96991 | -43.36793 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 49d3594c-9808-3c0d-9eb5-3b500d8dec7f | -16.96624 | -43.36394 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 15b23893-38d2-3369-aa85-de474a6b3938 | -19.52037 | -44.01309 | 2026-09-15 04:36:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec62f7f2-30e4-37b0-acdc-6a80fa05c3f6 | -18.1628 | -51.75348 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 592c7e78-506f-3d60-b746-de979e038bf1 | -16.86494 | -50.1567 | 2026-09-15 04:36:00 | NOAA-20 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 947f5c33-d948-3aa1-b45c-87b74f62ded0 | -15.56036 | -48.57862 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58b97d17-96cc-371a-8c01-de46704a7a43 | -18.13757 | -43.95884 | 2026-09-15 04:36:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e38b666-dc4d-391f-8bed-206898aa9eed | -18.17324 | -51.75555 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f58979b7-bd41-34db-b8ea-90f4914c148b | -15.53833 | -48.80187 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5cb6612-cb93-3c09-8a7f-c0248ff846e8 | -15.57692 | -48.81573 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4959c2a2-ddc8-3358-a983-5cf47cb56522 | -18.52462 | -42.85062 | 2026-09-15 04:36:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a2be259-b710-3cf9-a1f2-c3462420d3ca | -16.56586 | -51.62548 | 2026-09-15 04:36:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7d563e0-db01-3404-90b4-80798e2ee446 | -15.55705 | -48.57806 | 2026-09-15 04:36:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eae9575-cbac-385e-b276-6a022a85d24d | -15.57909 | -48.82344 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 899526f1-2f3d-3382-a726-27a60768c236 | -15.58628 | -48.821 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 369f1510-6349-30a6-851e-7d7b4e733b75 | -18.16419 | -51.76639 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1d3ff33-55c9-3570-a3b7-8634097f3fa0 | -17.20974 | -41.49036 | 2026-09-15 04:36:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d25e70a-ba1f-31f8-be8e-458f8f7d8f9c | -17.98897 | -44.3294 | 2026-09-15 04:36:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1532d99-8dea-35d0-9844-84fe65807d6e | -18.86538 | -42.00422 | 2026-09-15 04:36:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eee8f41f-03e0-379f-9539-993565305b90 | -16.97138 | -43.35694 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abfe719f-8a58-3a8d-9566-144c7cb54009 | -18.76569 | -43.2146 | 2026-09-15 04:36:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 724d3e7d-d4e4-3be1-b592-4081473d83ff | -15.54278 | -48.7953 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f494555-16da-3435-a788-f770cba4509e | -17.97976 | -44.33819 | 2026-09-15 04:36:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65d17f7f-11bb-3474-9cf5-c4ab051c2549 | -17.65975 | -43.09259 | 2026-09-15 04:36:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 655b0309-5007-3695-80be-1dd85e654e3d | -15.57966 | -48.81987 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README50.md)
