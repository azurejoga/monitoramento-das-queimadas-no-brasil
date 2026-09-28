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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f1d109b-ed53-3eb2-aa42-30dd1971c5bf | -11.37988 | -43.42992 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 819cbd20-ca46-3d0d-9262-e3567d9b6cb1 | -7.37901 | -42.11035 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c67e5e88-bd82-35af-98b6-85e1179d9a57 | -7.34187 | -42.07779 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c6b97620-9c12-314d-838c-5706fac0284e | -6.94724 | -41.60675 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2f48331f-8990-302b-96b2-be177f99738c | -10.88312 | -43.68466 | 2026-09-28 03:30:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae8798ad-3329-3248-92d8-1bdfc1ad92ee | -11.68877 | -44.54057 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14dce232-fb9d-3b9d-a74b-b12ae32c148b | -10.8845 | -43.69154 | 2026-09-28 03:30:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 89907eb6-c55d-34f6-bc5d-ac72398eafee | -11.38074 | -43.42388 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 688a5f1e-8647-388b-b977-b8889f13be29 | -7.71106 | -39.34783 | 2026-09-28 03:30:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e87e9a8-de05-3a3f-8858-1c657a0b8df4 | -11.37303 | -43.42839 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ba12511-d948-3620-96c8-d3b48c902bbe | -7.3339 | -42.08265 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d439e355-d7ae-37d4-befb-ee8d1acf107b | -11.70165 | -44.55148 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f3beaa6-668e-3619-8066-414646fb6e81 | -7.71227 | -39.34664 | 2026-09-28 03:30:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75fadb1c-ce48-3560-85be-1ba5ad1f6cc4 | -7.378 | -42.11015 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0bf95cb8-24ed-3fd4-8be8-a54e84ba5f18 | -6.94509 | -41.61834 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ff38ec08-1be1-3348-a2e3-886a01b38942 | -7.71149 | -39.35083 | 2026-09-28 03:30:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 436507fa-ad04-3cb5-b23f-5f829f0f1a8b | -11.38116 | -43.42369 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60f49d70-31d1-37ef-a19c-9a6b8f991003 | -11.37941 | -43.43011 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8b88a96-f48e-3c0b-b46b-a1c7a39b1371 | -6.94236 | -41.61142 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ad2bc5ac-b823-357d-bb60-c26828ea0eb1 | -11.70323 | -44.54396 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 434996e6-59f0-3db5-aa46-665e475c2c44 | -11.37256 | -43.42862 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 56bde8e1-be2d-30b8-bb2f-c2b2a9493c14 | -6.94126 | -41.61715 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e0ad59cd-9493-36a9-b190-be0e38498c43 | -11.67994 | -44.54645 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a97c26a9-4178-3ecd-9297-420999e3ac7b | -6.94617 | -41.6125 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 548a3e83-3760-334b-a0b3-15350719cc53 | -7.343 | -42.0719 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a7885c44-ec4d-323f-a40e-217f2a42463c | -7.15739 | -39.3156 | 2026-09-28 03:30:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 04138df5-bec2-31f9-9e2c-b5bb350b357f | -11.69194 | -44.52559 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 832ef980-4bef-3e78-a0ce-dc8c3c00fbc7 | -7.37918 | -42.10387 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a7847a0-d344-3efb-8054-6ccc7c276fda | -18.12166 | -44.38427 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 231c2cf8-4ad4-3d26-b3ff-39ec4f8c7f06 | -16.35399 | -42.56945 | 2026-09-28 03:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52efc38f-206b-3c1f-904f-2438fd5f3e5e | -18.61159 | -43.37164 | 2026-09-28 03:32:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3cf30c38-1992-3f78-aa84-a1eb7b883c15 | -16.19955 | -42.8712 | 2026-09-28 03:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92f6e411-96a2-3079-b406-5e4e30b11942 | -11.69097 | -44.53069 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 354030a4-15d8-327c-873c-f213ee5467af | -19.15139 | -43.83145 | 2026-09-28 03:32:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d46977a-5a94-3c9d-bc81-640a2ee5404c | -16.39248 | -42.56543 | 2026-09-28 03:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a46bf413-c4fe-3420-96ec-dc6176366101 | -18.11036 | -44.37447 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f5acd514-6c82-327b-9710-e6fea297587b | -15.1462 | -43.62897 | 2026-09-28 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 91ec2a5c-243e-3195-a649-cd8eaef09816 | -16.78991 | -39.41067 | 2026-09-28 03:32:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b624a2b2-01a6-3a4e-98cb-2eded319bbb8 | -15.3425 | -42.16804 | 2026-09-28 03:32:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 55f1cd30-789a-384a-94b1-304323679b5c | -12.87573 | -44.79495 | 2026-09-28 03:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 3659f315-bacb-3f76-8eea-f2921474390a | -15.15001 | -43.61164 | 2026-09-28 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a086327-8e74-3225-866e-a4569613ab18 | -18.67439 | -41.46717 | 2026-09-28 03:32:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7447c450-9013-35e0-9f19-6b0e960b79d0 | -17.90836 | -40.16367 | 2026-09-28 03:32:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2fa0e170-96ca-3cf8-b8f4-18709495f5e7 | -18.61156 | -43.3732 | 2026-09-28 03:32:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 407e91d4-7dc0-3d51-b793-1d689f5d06d7 | -12.87732 | -44.78769 | 2026-09-28 03:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| e0d0782e-081f-3589-b528-ee0f5a8f0af1 | -17.9169 | -40.16669 | 2026-09-28 03:32:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 0b6cc6ce-8754-30bf-83a6-c6475806b623 | -16.38564 | -42.56807 | 2026-09-28 03:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c4778c4-0b33-363d-82c4-590e330d9055 | -18.10278 | -44.378 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 00aa9bea-1d76-3438-be3a-e040f9f73d93 | -13.74369 | -41.27999 | 2026-09-28 03:32:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b93e539c-2b11-3aa6-9131-d9ccb3618e0a | -11.70705 | -44.52653 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68b470cc-6f17-37f9-8874-d17524481d10 | -11.68771 | -44.54566 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd547c6b-1be5-3991-bb8a-2389fdb816e4 | -11.70543 | -44.534 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14fff9f3-b244-3bd0-85b3-2eac77d3db7a | -15.16142 | -43.59068 | 2026-09-28 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8706c530-631d-3be6-80f8-b59e20e06111 | -12.87888 | -44.78056 | 2026-09-28 03:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 132db2f2-25cd-3699-9d30-3c63a0171efe | -18.68036 | -41.46548 | 2026-09-28 03:32:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a73e43f5-3df5-3ff7-8379-f25fb2f1715a | -18.12414 | -44.37346 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08674fa7-3860-3327-ba6f-dbaf8c1cb2d7 | -18.6751 | -41.46383 | 2026-09-28 03:32:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2507fc98-099e-32a7-86c2-1dc7f81fa2a2 | -19.14412 | -43.83517 | 2026-09-28 03:32:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0da4865-1baa-336a-9547-a95457d2e002 | -14.18757 | -44.36972 | 2026-09-28 03:32:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f667c7e0-0a14-3964-9605-976c04922b34 | -11.70218 | -44.54897 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d3c7954f-1d25-32e8-9639-46c544119c14 | -18.10907 | -44.38011 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bd6f968a-74e3-3b4e-8f6d-a648d0369efb | -18.61262 | -43.36859 | 2026-09-28 03:32:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 90274466-d359-3197-b126-a57f7ba16ff7 | -18.09524 | -44.38127 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dc30d91-fbbc-3e8e-b471-2f22fcc8399d | -16.35299 | -42.57407 | 2026-09-28 03:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee81ed74-96ee-3ac5-9938-88590f5900d8 | -18.67371 | -41.47039 | 2026-09-28 03:32:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7e9f6d4c-b203-3173-89d5-d4749aa9b37c | -19.14871 | -43.83656 | 2026-09-28 03:32:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca05294a-039a-3838-8cd7-970fc509cfa9 | -16.20573 | -42.87221 | 2026-09-28 03:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49116d37-8256-31bf-b25f-51f465aebe8b | -19.15034 | -43.83612 | 2026-09-28 03:32:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46c237b8-e231-3c1a-b1b4-f76e726cdd8a | -18.10152 | -44.38343 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 080f5a45-c24e-359b-8da7-39086891fcef | -17.83497 | -44.39646 | 2026-09-28 03:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c67e74b0-118f-38a2-920f-ec528fa9718d | -11.68047 | -44.54404 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2164d586-2fd6-3ae3-be3c-49bf82b4c854 | -14.19438 | -44.37159 | 2026-09-28 03:32:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 351e5a25-1c35-3916-ab77-cafc76e4765e | -11.68211 | -44.53654 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a67603fc-33e2-3cef-8910-f47d6e9b7204 | -15.14876 | -43.61732 | 2026-09-28 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eeb4a1ea-8b9c-3011-95e9-cd70b30a2893 | -16.38661 | -42.56357 | 2026-09-28 03:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9107af4-2b13-39c9-966c-c5f46f950686 | -15.15648 | -43.61319 | 2026-09-28 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 34c56d84-4764-3a34-9411-c565d27f39bd | -17.8336 | -44.40238 | 2026-09-28 03:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93613192-5855-3c62-805f-2e7fbb282f38 | -18.10782 | -44.38554 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| c8668517-46d5-351e-b433-e6645e4d896d | -16.39289 | -42.56776 | 2026-09-28 03:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c23aa9a-be15-3022-a157-6e5923ee1f82 | -15.34847 | -42.16929 | 2026-09-28 03:32:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a4578b79-05c3-32c9-8e0a-8e35a584d4a1 | -11.70381 | -44.54148 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afa8b085-f378-3699-bee8-6580aa254a65 | -17.83461 | -44.40147 | 2026-09-28 03:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0008689a-bbd1-3d00-94e2-a266f0224257 | -15.13449 | -43.62015 | 2026-09-28 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8dcc6780-4452-34e3-a88a-0f6f84b5e8c2 | -18.12295 | -44.37867 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a684ee24-e94c-3e8d-89d4-a6125bfa432a | -11.68935 | -44.53815 | 2026-09-28 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b384d81a-d218-3771-be99-f2f892f1f494 | -17.91315 | -40.15952 | 2026-09-28 03:32:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 4743d6bb-a851-358c-a552-1ff2921becb6 | -13.73796 | -41.27837 | 2026-09-28 03:32:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 94b44ebb-5f2b-36ed-bffe-4fb693ffb23a | -13.7389 | -41.27374 | 2026-09-28 03:32:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aee97895-cf40-31c5-ad08-3f3e05ac881c | -19.14979 | -43.83189 | 2026-09-28 03:32:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fe182d9-5509-3dbb-b17b-90b4ad7c3f81 | -18.11538 | -44.38214 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49cfe68a-f402-34cd-8786-39ce91fba673 | -18.54991 | -43.58663 | 2026-09-28 03:32:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72932c4e-7f7a-38c8-9f94-af5e23cc294b | -15.16019 | -43.59631 | 2026-09-28 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f6b69b4-2696-36c3-b684-d7fd69d6c922 | -18.54874 | -43.5917 | 2026-09-28 03:32:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83a7e72f-09e9-3bec-abc9-59b8669057a7 | -18.6126 | -43.36705 | 2026-09-28 03:32:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8041996d-d138-36f7-a290-3f189b4eb0ab | -17.91197 | -40.16522 | 2026-09-28 03:32:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 106.6 |
| 30668eeb-49c1-3245-b5e5-02090d202c4f | -18.11666 | -44.37654 | 2026-09-28 03:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cbdaa06-9ed1-394c-b27b-8909ac29eeed | -16.39148 | -42.57008 | 2026-09-28 03:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4a02275-f293-3b9f-84b1-c538f5c96bcd | -18.67952 | -41.4695 | 2026-09-28 03:32:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f4b0b158-31f8-3ee4-8a57-e2c53492a7bc | -21.52172 | -45.1142 | 2026-09-28 03:34:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bd58b73a-cee5-3394-b3e8-e589c7d65b80 | -21.52303 | -45.10872 | 2026-09-28 03:34:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |


[Clique aqui para ver as próximas entradas](README16.md)
