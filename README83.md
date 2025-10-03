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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd8d20bf-a221-34cd-865d-c535830f7faf | -15.30514 | -46.28217 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d0cc876-f981-374a-92fe-9855b9750edd | -15.20738 | -47.99314 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fca4af6-371f-30d2-8306-78117a2c0f73 | -15.30144 | -45.09598 | 2025-10-03 04:14:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6a024b8-957f-3730-bfef-0e1ffb45b85f | -18.68011 | -47.8309 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cc09565-7f3e-3328-945c-75d4e80f59c9 | -14.73055 | -48.10318 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e15c022-bc7f-3470-bba6-c7956c6eed53 | -18.16158 | -53.34654 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27696f16-f374-33fd-a7eb-d7ea275c45f7 | -14.6789 | -48.09868 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a8a62c8-8385-3fc8-87a8-fb52e7075a30 | -15.31296 | -46.30029 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 446e4ce7-8441-3d0f-a4b7-7eca426dc5da | -15.3482 | -47.07112 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62909e23-92aa-3914-a80e-4194c42945eb | -19.51181 | -41.96255 | 2025-10-03 04:14:00 | NPP-375D | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6773c266-a47a-3246-aa97-9327ebb53afb | -19.45459 | -48.93018 | 2025-10-03 04:14:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 99fdb9e2-fe05-3e2f-bfb6-63f03d928af7 | -18.51592 | -44.04122 | 2025-10-03 04:14:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5b26d00-0bb8-38c2-a41f-4ba3bf6a3a94 | -16.67353 | -43.80338 | 2025-10-03 04:14:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db937a85-280e-3b67-a573-2fc73a300cc0 | -17.25509 | -47.0131 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d2f7841-1e82-38b9-9e7d-4c065b6f255f | -15.19404 | -46.40651 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9882ee9b-ba1c-30a0-87c9-a3ea41d646b7 | -14.94702 | -47.52138 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 480d09c1-91ed-3536-b53c-76305ad2643e | -22.2817 | -46.72747 | 2025-10-03 04:14:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7c0befae-6f19-32c1-b96b-065918f30f45 | -14.70549 | -48.20022 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73da8e60-a03c-3ffd-b782-c0e5b481d214 | -14.66321 | -48.25534 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57682c6a-18f6-3f2e-b0ec-fdbfd256f9e1 | -14.72443 | -48.08787 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca6d3b8e-02c4-3192-a23d-3bf6e3a325dd | -14.93269 | -46.9087 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1101a7eb-a81a-343a-80d5-6021a1cc62d0 | -15.21727 | -47.18752 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2dc8770-9870-3617-aa25-80201f6b3c5d | -15.34523 | -46.26 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a1dd477-5115-3a92-bba0-1391b9a0a581 | -14.73744 | -48.12743 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87a8c232-79a4-3f9c-9b55-40b6079f6816 | -14.87377 | -48.33492 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35f85952-52a5-3a14-ad5b-d95fd897641a | -15.94643 | -46.22992 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5f21866-6549-3c4b-a821-34220d09a52f | -15.32663 | -46.39162 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d0c99bb-9968-3b6e-9eab-f36353cfbe53 | -14.93501 | -46.9113 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66051eec-79f9-3cb8-80b8-e64a7851cbbd | -19.01694 | -49.75491 | 2025-10-03 04:14:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dc82e11-70e3-3e9d-aed4-35e9532ccae9 | -14.90878 | -48.33308 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6975765-4967-34ae-b801-4438f358522a | -15.92839 | -43.36237 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f5bb22f-ef63-3948-9f29-d7021de4d7a8 | -15.31246 | -46.38904 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa2e9789-0bfc-3154-bf71-3a93da3e55f7 | -17.86081 | -57.61769 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 581b6bfb-dba3-3ae0-80f1-d1c58763c724 | -15.27668 | -49.32446 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49a2fdbb-c826-35b5-9c54-cd3308604c3d | -17.0604 | -46.62983 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dfddd58-d4e6-32e5-8950-acbd56f1d14e | -15.83171 | -46.2467 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7582f68e-b02f-34dc-938f-3e1882e6615c | -19.46915 | -43.64769 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0af447fe-57d7-3bd4-b277-8b9080a08988 | -19.14775 | -41.49972 | 2025-10-03 04:14:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec7c0eb2-dcb2-3a26-a734-f65522a1846f | -15.9212 | -43.3427 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5efaaf84-cf23-32f0-a022-9fa796443800 | -17.96837 | -45.01128 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c78b777-ceaf-362c-9a5c-9acb899e637c | -15.70796 | -46.27131 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82d59de0-15f5-39bd-9212-328f7c73c41e | -20.12987 | -44.0056 | 2025-10-03 04:14:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bc5bf100-e34b-3555-8592-2081032fb7a7 | -14.72654 | -48.12066 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4001615-fb10-33d8-bf56-728badcb5370 | -17.91574 | -44.61187 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0d5e7bb-a57b-3e5d-9b54-e8962cf6db9c | -15.35708 | -47.06359 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cda9e968-79fd-3a02-8586-cdfa56d04ee3 | -20.06223 | -45.10364 | 2025-10-03 04:14:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 467bfe42-de09-3c83-a0a1-e30438bf61f4 | -20.06164 | -45.10733 | 2025-10-03 04:14:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed13aff9-4c80-3768-b4a5-fe0bd66a202a | -20.11868 | -44.38766 | 2025-10-03 04:14:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ca2374b2-e081-3bc0-b80b-f8229f8d77c1 | -16.04232 | -50.9213 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0aaf19e6-bed3-3913-934f-caa4ea959bec | -15.30022 | -46.28963 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09939ea5-5a03-3834-8948-bcdc49c84d80 | -19.16505 | -46.68678 | 2025-10-03 04:14:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ecfde3c-fbbf-36ac-88ca-68140e740301 | -14.87846 | -48.30851 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aac08105-aa08-3287-af50-66dc77069c7a | -18.20217 | -43.55352 | 2025-10-03 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0ea4f10-8f60-3784-b69c-726fa0fba40d | -14.9112 | -46.96842 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95e12b6b-c0cf-373d-812e-b9b5b3280629 | -18.52118 | -45.04681 | 2025-10-03 04:14:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4adb9eea-6e20-3510-8321-d9a1e5ece057 | -19.66171 | -44.17 | 2025-10-03 04:14:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a04c13a-b9aa-3c9a-9b17-a2086cfe1ff5 | -15.8583 | -46.26026 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d14dc66a-8bc8-3262-9e3f-00a698e7efeb | -15.35026 | -46.29487 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d055dd70-a55c-3ce8-aad4-2ccb8e20c081 | -14.73639 | -48.13317 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a05bd55-6594-317c-9395-07efd012d5c2 | -16.34838 | -47.10932 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 345d27b3-fc52-3cf9-940a-b112e013e60f | -18.16664 | -53.34801 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baa7e201-610f-3bec-a958-c714b53046a6 | -17.90703 | -46.8364 | 2025-10-03 04:14:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f8c31ca-9b3d-336a-9fe2-2134add23996 | -14.98545 | -49.95919 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a2421c1-78aa-38e9-9f21-d1709fd3e7bb | -14.90808 | -48.32541 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cb853ec-60b3-39cc-ae83-878f4ccb5d3c | -17.55757 | -44.79799 | 2025-10-03 04:14:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2067d269-114f-34be-b697-23a89481a309 | -21.35227 | -43.82583 | 2025-10-03 04:14:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 859c956f-d5ab-3f23-afcc-80e6dd985ff8 | -14.68681 | -48.09954 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 700ec779-268a-31e9-93c7-b39aef12ca2d | -15.48424 | -45.92985 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c69e8f8b-4a1b-371c-8bb9-79837b640bcf | -17.62704 | -44.44287 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7adc59a5-f713-3a07-8772-ebc87d36f6b7 | -19.81858 | -46.92271 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4ab684a-78ca-3467-a529-505e20295084 | -15.51682 | -46.81445 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c008b31-bb26-32eb-830e-b82a4561aa59 | -14.64666 | -48.12081 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a1ead1a-afc2-3e20-af7c-ce6f817bb902 | -18.16722 | -53.34516 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d25f6118-9586-313e-9dba-dfe32c96b4a0 | -18.67934 | -47.83534 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66f96ad7-a463-34c1-9e60-181c9fb01142 | -19.28929 | -43.73605 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a46faf7a-e003-345f-b1ef-daa125961448 | -15.51378 | -45.90296 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e42cb02-b368-320e-98af-ec7b6f5510d6 | -18.8347 | -41.8991 | 2025-10-03 04:14:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 357a37bc-e9d4-32ab-8c11-529be4a29cee | -15.5001 | -45.92065 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcc43c91-0e6e-3a19-9523-d60903ad2901 | -20.14718 | -42.01604 | 2025-10-03 04:14:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 95b9f58b-ac85-3e76-a54e-a957b95c82a1 | -15.24832 | -47.9195 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 096ef751-f1f2-3a11-b1a6-09507077fc9c | -19.97163 | -41.66029 | 2025-10-03 04:14:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 67231f72-d708-30b8-985f-3a84daf1fdb6 | -14.93563 | -46.91349 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 407a49c5-a6d0-37ac-b098-45c548d1d021 | -15.20911 | -47.19077 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3c35a5b-48cc-3ad3-ba3c-f0763eb36b8c | -18.68342 | -47.82926 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dff3ddfe-7864-3950-9148-958238e6edf9 | -15.24223 | -49.29653 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c945478b-3d52-3e06-a579-64ff75312417 | -15.21539 | -47.6483 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f0f3a34-9d8f-3aa9-91b5-6fbcaf1c3f8f | -14.68471 | -48.08865 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b71d6ef-111b-3afb-9908-fbd7a076c804 | -18.66507 | -46.58607 | 2025-10-03 04:14:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 344c6e8c-a70e-3dae-bd97-ab87f562fc4f | -17.85686 | -57.61798 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5283f254-3c3f-38de-9614-513598cba8c4 | -15.34877 | -46.26058 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7d28730-a82b-3be2-9e5b-d54ebb9e4b1e | -14.9786 | -46.85543 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efd3ffc4-a57a-3465-8a32-f502c643b59c | -20.99546 | -49.22058 | 2025-10-03 04:14:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1f66d65d-1549-3f7b-85d4-86fec9867d69 | -17.853 | -57.62125 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 281dd006-bba4-3a5e-84cb-a95a5a206fb0 | -19.82026 | -46.92188 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 679e9a7e-4107-3ce8-8a7c-50d186b614af | -14.85945 | -48.27812 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a966a13-36f5-3297-a3a9-c14fd392337f | -15.2306 | -48.71688 | 2025-10-03 04:14:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eaaa0f8-b4a3-37e4-8f58-b7fee2750e15 | -18.70455 | -43.18208 | 2025-10-03 04:14:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 23869f57-5f71-32b0-bfbd-f306d672607e | -15.59392 | -46.90752 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cff157b-aa10-3570-aecd-cebb26fbdef8 | -14.77515 | -50.09718 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f64384d9-75f1-3ef2-80ec-d126fee23911 | -19.47194 | -43.65198 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README84.md)
