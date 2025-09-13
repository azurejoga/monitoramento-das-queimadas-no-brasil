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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 738d3e8b-a7d6-340f-98cb-0d3132159af5 | -16.55017 | -49.21947 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 2a99aa9d-df3c-315b-8384-c12052cce751 | -14.43522 | -47.33326 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| b7e3ec55-c42e-3583-a4cf-8918cb810705 | -15.59597 | -54.76109 | 2025-09-13 00:50:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 53c78caf-101d-3e84-8293-4af5fff8d8c4 | -15.11892 | -52.45964 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 35f029ca-78f8-3bad-895c-eba279320e1f | -16.6474 | -49.75223 | 2025-09-13 00:50:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a7510b0d-20a8-3d06-9d43-a3b5f9879f02 | -13.00265 | -44.10415 | 2025-09-13 00:50:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| e91a4f32-5185-39b2-90a4-0273799ab3cf | -17.10271 | -48.85302 | 2025-09-13 00:50:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66ec5a1c-6239-39fc-a30e-2060b15d58ba | -16.43331 | -49.05579 | 2025-09-13 00:50:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3c7bd1e7-276c-3ec9-9961-bb1698146b57 | -11.0589 | -51.48307 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 411bd205-62e5-37bd-a913-13043daeb45b | -17.43665 | -49.22882 | 2025-09-13 00:50:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c9f15194-ab85-3798-9e15-10217c7c7485 | -17.30887 | -48.74133 | 2025-09-13 00:50:00 | TERRA_M-M | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e1fb1c19-98e6-3425-8468-77e72d291424 | -15.53611 | -54.68624 | 2025-09-13 00:50:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6e7c9fbe-d91e-364e-8a42-db892ca9b6e6 | -20.42112 | -50.75303 | 2025-09-13 00:50:00 | TERRA_M-M | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| ad8fd0fc-2340-3b61-80ae-539dcb831678 | -14.19965 | -46.28503 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 085be42d-4695-344f-a418-599c48b19764 | -16.98209 | -45.81017 | 2025-09-13 00:50:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7c64b419-5636-3709-971f-7cf57951a7f4 | -17.35722 | -42.70784 | 2025-09-13 00:50:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 142.7 |
| bf040faa-3f4e-3ef4-bfc9-33be30bfe855 | -16.49952 | -55.1557 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 96ab18ca-9b61-39c5-9f0e-d1489e9fc9d4 | -15.11249 | -52.4793 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cdc2b63c-0957-3206-a90d-501a870bcc33 | -16.01406 | -47.923 | 2025-09-13 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7284c470-3388-39d7-85d2-65de32cc57a0 | -13.00728 | -44.13038 | 2025-09-13 00:50:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 2f069c76-1c0d-3453-8989-a40150b283ab | -11.47606 | -43.62074 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 198b5726-9a92-3611-ad05-afabab9e2fb3 | -15.86249 | -47.2275 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 196da25f-043c-39c4-8b3a-b49c40969471 | -11.27588 | -51.12932 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4b961416-2942-3a80-8ba2-4c174607c1c0 | -11.61565 | -52.22738 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 77a12414-71a4-32d6-96f7-a48d2765359c | -12.99974 | -44.11018 | 2025-09-13 00:50:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d49c252f-1b8b-36ea-8c4b-34c187694aeb | -18.89454 | -47.06139 | 2025-09-13 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| a4796093-2f6b-3ca2-9297-a0bdc0d450e0 | -15.13566 | -52.50722 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dceb1d66-22a4-36d8-acd4-0885d9ecef4f | -15.13442 | -52.49796 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f4f4f4a4-2803-31f4-93d4-81b33cc4ed90 | -10.65764 | -46.26101 | 2025-09-13 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 31a9694e-8a0f-3217-9a58-8af9771140ca | -11.60684 | -52.22867 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5f19a857-b0fb-3375-bbd7-ed459691f8e9 | -10.76687 | -50.53987 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 86f7bf7a-5b0f-3dda-b1e8-af85ad27f572 | -12.10523 | -44.89611 | 2025-09-13 00:50:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 71d6c0b3-926f-3de8-bfa3-a4d8c8eb2a68 | -15.15199 | -50.12431 | 2025-09-13 00:50:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3efda4a9-222e-32ad-a8fd-8823a3ed4cc9 | -16.02592 | -47.93313 | 2025-09-13 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9be76951-81bb-381e-833b-951c24b7461b | -11.43357 | -43.5401 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c4341877-8ace-36c9-b049-9cf96a2b20c6 | -18.97681 | -48.59507 | 2025-09-13 00:50:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 805bedc4-1068-3fd8-98d4-fbec5dd2754d | -16.29271 | -50.04062 | 2025-09-13 00:50:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 61e2956f-8c9e-3522-ba07-3e22aee94689 | -16.55943 | -49.21787 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 7209b73d-f1b4-3712-9af0-0d4ffe915931 | -14.46196 | -47.33826 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a8aac313-ed31-3cf7-8e2d-a1414d088ecf | -16.5532 | -49.23977 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 13051f46-5b68-3ce6-8a58-6a4d4e065dfa | -11.83173 | -50.57429 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 7248939b-b4aa-33d4-9809-1cb08ee31d78 | -14.43286 | -47.31822 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| b84df100-0ed5-3b7f-99d9-3dc1ca4805b8 | -11.10037 | -51.96785 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ed173854-a9b8-35fa-a1c4-ce21a8bb8964 | -10.72855 | -48.6243 | 2025-09-13 00:50:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ce59194e-a1e2-38aa-85d3-ca418023f35a | -16.16595 | -48.86035 | 2025-09-13 00:50:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1d146086-229e-340c-af97-8acc40f4231e | -16.64122 | -49.77347 | 2025-09-13 00:50:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ff0ab8a-e87c-35f9-b7da-74160c87a226 | -15.11125 | -52.47009 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fb066229-6a20-381d-81e5-fc56ab02a4a9 | -13.00281 | -46.74111 | 2025-09-13 00:50:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 22d911f0-04fc-36af-bcd5-ea505e25b8fa | -12.92131 | -54.75101 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 14a31c62-c661-374e-8f14-c95ca32bcd96 | -11.70707 | -46.56353 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4c7b0781-8134-32cb-88a3-af6f4817794b | -16.39749 | -49.0723 | 2025-09-13 00:50:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| db472e5b-cb67-3fee-b6c6-0a2cccf11de7 | -12.96414 | -54.75042 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f74056ac-2836-3e93-bf3b-015a4bfaa2b7 | -11.43501 | -43.56597 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5807af56-a6fd-3f77-9047-07b23754cb1e | -11.15079 | -51.41614 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 11769f86-fb27-3ab3-961d-50832f638f75 | -16.87229 | -49.33474 | 2025-09-13 00:50:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5a59de7d-eeb2-3f2a-821f-fe7cc550bb7d | -15.15761 | -52.40033 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2adb0ff3-befe-3426-919a-e2574b6353b2 | -12.806 | -47.98771 | 2025-09-13 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a32a3014-c909-32fe-b5e6-7c16fe30d676 | -18.85769 | -46.83197 | 2025-09-13 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c7bb0577-2671-3fa1-830c-b98dcf571a2f | -15.12016 | -52.46883 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a43f90b6-2bca-37fa-9398-1640c1ad3d56 | -20.33964 | -46.65881 | 2025-09-13 00:50:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d9eda2e2-4514-3dad-936b-8ce28f96e791 | -11.22666 | -54.99968 | 2025-09-13 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a91847fc-adf9-3e8e-bbbf-4ea21d0f91fb | -15.00414 | -50.12375 | 2025-09-13 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 185909a6-d73b-3cf0-99d8-0c1df22a78f1 | -11.73098 | -44.20359 | 2025-09-13 00:50:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| bdfad706-dac1-3d37-b728-e18a95deb28c | -17.8314 | -50.41887 | 2025-09-13 00:50:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 135b4b33-3599-3126-8300-d564f76d19fa | -20.29683 | -46.58872 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3d20c47e-a22a-3017-9d4f-af2e92c48a8b | -15.76271 | -53.49927 | 2025-09-13 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 14aa4bd6-4365-3ea3-94f2-17c208afd677 | -15.20332 | -56.67475 | 2025-09-13 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0213c6c5-6279-3e4d-8946-ae6e28682111 | -15.77066 | -53.48764 | 2025-09-13 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 87529274-6d44-39dd-bfc2-f58615d7890c | -11.72478 | -46.59709 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c807df8b-4526-33f0-bd83-b2b8cb7d6e08 | -19.65709 | -45.86574 | 2025-09-13 00:50:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 0a92e183-b3b8-3f66-8a14-9973b2a08d2f | -11.73563 | -44.23023 | 2025-09-13 00:50:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| c51019b4-f957-3b0d-92e6-26eff6f6080b | -16.5323 | -51.74182 | 2025-09-13 00:50:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| bc230100-8e7c-3aac-9ae9-0d1196579659 | -14.45907 | -47.34464 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7529f7c7-ee2f-3eb6-b42c-4ece481da939 | -18.0401 | -45.43691 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 6cd48532-9d1d-3f39-9722-d82e743286dc | -15.17006 | -52.49272 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8028e8f2-343c-34f4-8952-36de99eb51d9 | -12.91312 | -54.76318 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2e2f862c-f765-3d6c-bccb-de504b032b95 | -14.87591 | -55.85769 | 2025-09-13 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5361e118-8902-3ba4-9b99-019cd176c2f8 | -15.17427 | -52.32256 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 286a56b0-3bdf-30c8-a6f6-74d8d4c0b2c5 | -15.54909 | -54.79122 | 2025-09-13 00:50:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f14055c9-7066-3975-934a-1150c57bbc15 | -16.61347 | -49.45611 | 2025-09-13 00:50:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc91e706-c16f-3e3a-94bf-4ad3c8cbf82f | -10.75617 | -50.53136 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0fd7d727-efe5-30b7-8313-d2aec7c20beb | -12.93093 | -54.74972 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| dc1e3af3-efcd-33a3-9014-05f2f30762e8 | -17.29357 | -47.2491 | 2025-09-13 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| af85cce8-0e22-3227-91a8-fb78d6063ede | -16.00586 | -47.93665 | 2025-09-13 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 33777438-be79-3c37-99dd-be567dbc0770 | -15.71684 | -50.58756 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| f3ed0e27-cbec-328a-bb55-411de3be41f8 | -18.16106 | -49.18962 | 2025-09-13 00:50:00 | TERRA_M-M | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 4a3c1ec4-652d-3f09-ba1d-b410d24f9a74 | -15.37581 | -52.10621 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3cf268af-af9a-3941-a7f9-cdb517c91c4e | -17.28247 | -46.09707 | 2025-09-13 00:50:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 32ee2e86-ccb9-3e51-9871-9591a3704463 | -14.21804 | -46.2746 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b6ec7e3e-da03-3ddf-bc7a-1c7212d0a6f2 | -18.1356 | -48.45843 | 2025-09-13 00:50:00 | TERRA_M-M | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f28d4292-d227-3ceb-a978-27de593fba3c | -14.20866 | -46.26593 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 320.4 |
| 7ca88449-21eb-3da5-89c8-608f5231108f | -11.16234 | -51.4332 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| effb499c-3614-3585-8a6e-80fee72ba778 | -11.16997 | -51.42267 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 227.9 |
| f61187c8-6163-340a-a8c0-7b7b9db437c5 | -10.72659 | -48.61155 | 2025-09-13 00:50:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2626e43c-2852-323e-b082-4a3fd6b8930a | -12.99474 | -46.74819 | 2025-09-13 00:50:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2d8e7f0e-32ca-3cb1-b46e-3040f0548b14 | -14.71529 | -55.64181 | 2025-09-13 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 56e16856-3e17-398d-900c-da2bec4cbf00 | -15.8352 | -42.61254 | 2025-09-13 00:50:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.1 |
| ccc2a645-f4a7-3e51-b8c0-6d957f62cdb9 | -11.99832 | -47.74712 | 2025-09-13 00:50:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 27e5f22e-4c4f-3d6e-bf87-de502e254266 | -15.11497 | -52.49768 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8d641f13-b10b-3ebd-bc1d-660c4b0b5a48 | -16.03643 | -47.93768 | 2025-09-13 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README8.md)
