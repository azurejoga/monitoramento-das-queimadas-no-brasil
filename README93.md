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
| 1eb9ebb6-ea51-3978-b26c-65d0bdaa1af9 | -19.52234 | -43.83659 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcf8d34b-0146-334d-9df7-084308490132 | -19.57697 | -48.0211 | 2025-10-04 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f103b331-223f-3686-817b-c038c40a2d93 | -17.99106 | -45.0135 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c525f7fe-0f9e-387d-b1b8-626f87c41b72 | -15.56453 | -46.96304 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1024c3d0-30af-37c0-8c74-4a66426d3ee4 | -19.96635 | -43.71114 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 78b9e0dd-eefc-329e-8cef-636e685a06a3 | -18.54545 | -45.04511 | 2025-10-04 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74cd3006-e8b1-33e9-868b-1fc8025605b8 | -17.9636 | -44.39482 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12be3168-a89e-3efc-9290-73f774552879 | -21.26014 | -45.18649 | 2025-10-04 04:17:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 35c70482-0340-35cb-9c67-7727c7b17d8f | -20.10344 | -44.63633 | 2025-10-04 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9adc0347-0679-39d7-99ec-f9792a5ea59c | -15.86873 | -46.26934 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a25457a4-5cc0-3ce3-a4dc-d96161a3c0ac | -15.22734 | -56.82778 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20abb9e8-6e60-3889-b0b3-df07b3d19fbf | -19.96105 | -43.64851 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ef65c1e9-580a-387a-9bca-131690cef5ef | -20.78516 | -43.22086 | 2025-10-04 04:17:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ec657b2-e04e-321e-81f3-2ce379a4ec77 | -15.69859 | -46.27395 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e892c5b1-6ffe-3a0d-8aa3-47ecbdf89eb1 | -16.29198 | -45.24141 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46626a5d-c617-3122-aa58-15bbaeada632 | -18.17307 | -53.34983 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 935cd8d3-642f-3aa9-980b-402ae1b13b7f | -15.7275 | -46.28664 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3921633a-fd87-3ba1-9a83-592465758116 | -17.03 | -43.43843 | 2025-10-04 04:17:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f4cd06a-faf7-31ee-a4d3-0b391e39252f | -22.43387 | -46.88515 | 2025-10-04 04:17:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9411710a-8eeb-3f5e-aa9d-6691c9070027 | -15.34777 | -47.82137 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c9b778d-9011-3a85-8adb-4f1497ebf9b7 | -16.0942 | -51.06912 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f9f617-614f-3573-9ca6-d29aeb2555d5 | -15.36813 | -47.9555 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e525f24e-96d1-3ee4-b725-a718f74e7c65 | -16.16166 | -45.12037 | 2025-10-04 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf975de-f1a8-3016-990b-ca46e5aed6c0 | -16.34783 | -47.08709 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0c68928-1e19-3bcc-aa13-d184b327ce92 | -15.72618 | -50.18809 | 2025-10-04 04:17:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c87da00c-fc9f-3185-9470-6fa12ee1eb64 | -15.7214 | -46.28178 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beb2f599-5c71-3b39-97cd-93a9ab360b4b | -18.45653 | -49.4397 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c97b3ad-e7f9-385e-8359-6d2d2a23c21a | -15.52947 | -46.8136 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30077364-1831-3a6b-a37b-5917a179968b | -14.9817 | -49.9758 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c7d43a64-8d50-3e44-be30-83eb1b990902 | -15.58936 | -46.94012 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93afb61b-be43-3175-88a9-9d7f2b889651 | -22.00156 | -45.46566 | 2025-10-04 04:17:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 657f3206-f17c-3eec-813b-3ad8b72130f9 | -16.05967 | -50.90221 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0be49ba4-d40e-3fcc-9cd2-c9537fb63e16 | -16.04157 | -51.04641 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc09a76e-c4ac-3c15-80b0-5cfe19e75d72 | -20.13545 | -43.99161 | 2025-10-04 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 93b3ec8d-7875-3cde-a2e0-18d33a2cc6ca | -16.01012 | -50.92935 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 91e41742-0c91-3ad8-b587-43306eae0e92 | -15.82557 | -46.24691 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6445cdf7-9cea-3e1a-b687-fee0ee9f29b3 | -17.95649 | -44.25959 | 2025-10-04 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e07de5b7-613c-349a-ac72-2f2c84002eff | -15.82891 | -46.24747 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a4c9ea2-69f4-30bf-9d36-ea51ed4fc7f7 | -17.08417 | -46.23781 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf8504a8-19a3-3705-b113-bf2f96e68de2 | -17.99684 | -51.63612 | 2025-10-04 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55a137e6-aa6d-39bf-b02b-7ec4d76c85d2 | -20.12506 | -43.99032 | 2025-10-04 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5de286f6-3e12-3c37-9bb1-0e5f419b5809 | -22.92494 | -43.55773 | 2025-10-04 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d366ab57-b494-39b6-bb39-ebebff24f8e3 | -21.18697 | -45.13568 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f9e7021e-63e4-380b-a47b-7ffa43dd5f34 | -15.62092 | -46.94178 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eba2c944-9506-325e-be7e-cad1c0beaee9 | -20.47095 | -44.82451 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8dece641-6c52-3a6b-8567-079fcc960a41 | -17.45168 | -47.47937 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa938955-c413-3279-9611-c751df3a147d | -16.07258 | -50.90198 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37bef4b3-10e4-3589-bb21-b2dc67b27b1d | -17.0824 | -46.24873 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f61989a-8a8e-32f4-a322-6b7199a83cd2 | -15.722 | -46.27806 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b66ff7f-7875-3ac1-a13d-862f4c240eb3 | -16.04002 | -51.05476 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0becd011-8af5-3017-b915-44995a6a9f1e | -16.37234 | -47.00194 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e2d6176-d854-363d-a357-4b293349a17a | -15.32273 | -56.94872 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50290945-85b3-3d5b-8d85-550691924d54 | -15.85536 | -46.267 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27335f95-bca0-375e-ab6c-b7ec22994ce1 | -15.5273 | -46.80558 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca6eab41-201a-3172-87b4-9677aff171ba | -16.73078 | -46.21441 | 2025-10-04 04:17:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed18e2ef-da5e-3750-a2c4-acb457c9a0b1 | -17.61388 | -44.46416 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fda8485-4c2b-3943-98ec-e44522acb3d6 | -16.00825 | -50.92469 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 634aa0ea-c7c3-3f0f-b224-903101a38775 | -18.68888 | -48.17842 | 2025-10-04 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8de5a92-2fa4-3a31-9584-2fcb1114dac9 | -15.95522 | -43.3291 | 2025-10-04 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6d85edb-cfc9-3e8c-a30f-bc525ce01cad | -17.00708 | -49.15358 | 2025-10-04 04:17:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71755f2a-fbc8-3471-9960-fe67479e5bea | -15.52845 | -47.93261 | 2025-10-04 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21f48dfc-0e74-35e3-a86a-05189e5bffbd | -17.62042 | -46.69966 | 2025-10-04 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 623a7335-1b0d-3bbd-8baa-e0bae9e6b2e5 | -17.15029 | -47.03526 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36053088-9bda-3e71-96fd-49f6e98d62f4 | -17.15304 | -47.03965 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48713beb-b8b6-34a4-baab-04e8290af813 | -15.58004 | -46.95408 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 428b32f4-dba1-3ad2-ad05-2ec49a712ba5 | -16.04642 | -50.92737 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 183bb028-4cb2-3bd5-8c65-5526521d2ad1 | -20.136 | -43.98778 | 2025-10-04 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 941f46f1-040c-3cec-b055-14b0377c045e | -15.37168 | -47.95613 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13cfc77f-4ced-3813-ad95-7c64fd02f138 | -15.60421 | -46.93506 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d341fc4-7028-3127-be41-9e8fee4cdfb4 | -19.74673 | -46.50055 | 2025-10-04 04:17:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e2504bf-a98a-3837-aaf3-40c64d8a0865 | -16.75363 | -43.95855 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a78fd21-9da9-3b9c-a353-08c2ca2ce390 | -19.97682 | -43.7126 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec1a589a-e8a9-3677-a1cd-503853e8b29b | -18.31407 | -44.04465 | 2025-10-04 04:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb76ea38-e515-3674-b7d7-fb4752629c85 | -15.35748 | -47.95367 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebf351e2-906a-320b-b12c-04899c80019c | -15.52791 | -46.80186 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 817ae907-9bbe-3a15-8975-82fb2b42087f | -17.7022 | -47.09311 | 2025-10-04 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 282f633f-9005-37dc-a2cf-846789c80c65 | -15.22723 | -48.05623 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 208156f2-1158-36e7-8cc9-f6a5d24b1f2a | -21.19646 | -45.14132 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 97ba0a2c-be70-36d9-b568-09981b9ff659 | -17.70557 | -47.09372 | 2025-10-04 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a9b57ec-e479-3cf0-930d-ef3e143cf03f | -17.27501 | -48.30968 | 2025-10-04 04:17:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21ebb955-73ca-39af-ae5c-964190041c4f | -17.16717 | -47.03834 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e25e008b-9932-3400-90bd-eeef7f3fde22 | -17.08123 | -46.25602 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51953820-851e-34df-b782-d9c24506f56a | -19.59593 | -44.64418 | 2025-10-04 04:17:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f21a782-b5b1-322d-a314-22bd6069050c | -22.28992 | -46.7224 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 508b636b-e9cb-3df7-814f-893ab814c7d1 | -22.2786 | -46.75094 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d23a4428-fb1c-336a-980a-809fe0aab8c1 | -18.27892 | -45.90651 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17076f1a-b2c9-37d7-b901-9777c6fcb5a5 | -15.7919 | -46.26372 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e1f280f-2c15-3b2e-80ef-5b2c64361a2a | -15.28363 | -47.92031 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1384f2c-2fe4-34da-81cc-a2ba1e12bbf2 | -22.6897 | -47.43127 | 2025-10-04 04:17:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd729f35-1670-3e69-b9ea-9420b954a359 | -21.85117 | -41.37386 | 2025-10-04 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a9aa7e8f-9c61-3813-8089-f01304947444 | -19.96983 | -43.71169 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 60454759-1f01-3cda-a835-e49807068113 | -17.64235 | -44.45745 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1e4fecc8-fc7a-33c1-8306-083b32e98f58 | -15.34045 | -47.33375 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9154bbfd-f2d7-3f90-8a1e-9765e9fb8049 | -19.71055 | -44.12759 | 2025-10-04 04:17:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69ee0481-7d2c-34cf-86b5-90f994fa58e3 | -15.69524 | -46.27338 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00881439-7530-38e2-9b94-a50e6bd1d87b | -21.1931 | -45.1407 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 154c846a-86a9-338b-bbbb-8110bad0f17a | -19.59875 | -44.62523 | 2025-10-04 04:17:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 949c2109-be60-3163-aa0e-17c814eeb6a7 | -17.99788 | -48.33089 | 2025-10-04 04:17:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54746525-84cf-3592-9ba2-e4bfc720c34b | -17.98164 | -45.00825 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a11f718-947b-348e-a551-65e55fece950 | -16.08104 | -51.06718 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README94.md)
