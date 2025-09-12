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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9336b8a-4c11-394d-8a14-de9490ea4bc5 | -12.91412 | -47.97614 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8544a9b7-8179-38d2-be5c-6750ab301657 | -15.07831 | -48.01186 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 418c37e9-0769-3afa-9ce1-04ea553a4781 | -13.25082 | -43.7719 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f66cc254-a002-30aa-bf72-dc227fc8bac9 | -19.56729 | -44.24333 | 2025-09-12 04:27:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46c20b72-fba5-39a1-91b9-5cdd1b37f737 | -16.48162 | -51.40152 | 2025-09-12 04:27:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 650bce70-791b-3536-8148-cf82d42ce84e | -19.66804 | -45.86036 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3722d250-40fc-3902-900b-a97507f4823f | -15.88281 | -48.18509 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f21f7da2-a6b9-3c54-b335-77a2c3578cf2 | -11.94304 | -51.17959 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2c76e0aa-7e05-369c-bab1-02ca31d9efc7 | -17.35588 | -46.68761 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fd9b32d-319c-3499-8f2a-f9106e752e3f | -13.04049 | -47.99362 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ca9e0e8-e231-3805-a66f-81abaf2f9ab4 | -17.14871 | -48.49039 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b71960eb-9c44-3047-9888-031403da45d4 | -15.79066 | -52.2297 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 451167ec-0252-3d2f-b035-9ebde3ba428c | -14.28049 | -45.04934 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd945ea2-3ea5-3d57-9648-2a5c6e3ad9d8 | -15.91977 | -51.79634 | 2025-09-12 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ce6adf5f-4581-3f25-829a-335563b5af2c | -16.82003 | -47.80902 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd1d1958-2206-3f8c-815a-ef3811c57730 | -19.05074 | -48.74191 | 2025-09-12 04:27:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 601ad2ea-8de7-3953-834c-3245d7857ff0 | -15.60043 | -52.73396 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ac0edfa-8efd-334a-a383-fed7d3736c0c | -12.95382 | -54.74246 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7429310c-a5af-356f-ad1e-9efa6fce0253 | -11.95484 | -51.17715 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ff967ee5-2a49-3f6b-9423-05af09e6e089 | -18.68118 | -47.67542 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7be91206-9a9d-3ba3-8661-9bb05b95b4c5 | -18.05612 | -45.44897 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b43d709e-8b20-36c9-8ecb-c4e5d8cabf37 | -18.82296 | -46.88604 | 2025-09-12 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0aadcd93-32ea-3a07-9e0b-ea6653f492bd | -17.46111 | -45.10216 | 2025-09-12 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4c3244b-e0f4-3125-940a-f5724ccc0b10 | -18.65645 | -47.65583 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b35603d2-8fb5-3eef-b8c1-4dd6bd1a3fab | -16.48727 | -51.98656 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ccc59ee-6eb7-3c03-90e5-41fc005daca0 | -17.20192 | -48.69144 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ff204f1-f0be-3dbc-a0d6-149ea6d93853 | -11.60469 | -52.22394 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8e24346-ffe2-3f58-9115-eee7854e5993 | -13.35124 | -41.92907 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a61f4b48-08ad-3089-9e2e-05ad180b4462 | -12.87055 | -47.95167 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a802464-1619-3cb2-8ff1-7798739155fe | -13.17123 | -45.28027 | 2025-09-12 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d90f66e1-aac6-3414-8871-b815987e376e | -12.99178 | -46.74189 | 2025-09-12 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cc1fa97-e68b-3121-8f3f-f4e2ad605ebc | -14.16476 | -46.19183 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d342821-2786-3666-b128-af4d48d29775 | -17.37557 | -52.91821 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 36251bfa-f690-3b24-9751-4cb5728ddcc8 | -14.50806 | -53.92269 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b08d97f-6020-3d74-8f4f-9cd71d714ab9 | -13.95317 | -48.23515 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79b44e5b-9e3c-302f-9996-c520e3a56aca | -16.00376 | -48.0837 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0464f90c-a307-3898-87c0-95184966f228 | -15.16629 | -52.41323 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7589b158-aee7-3424-8eb9-6605deb36a6a | -14.18759 | -46.20279 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5576d3f6-fd44-3297-9c09-66bbf748dd35 | -14.29726 | -46.49545 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6869a3a6-9a5a-3f32-90bb-d9fe49145963 | -14.17444 | -46.17357 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17fb29ca-2113-32f1-af72-f4faa239607d | -13.38359 | -51.8257 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38457700-d0e6-3a4c-a45d-fdb94e78870a | -15.64884 | -41.82839 | 2025-09-12 04:27:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a7e4a500-f241-33a6-9fa9-b5c9c329530f | -14.16876 | -46.18842 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66e2d9a5-2522-35d9-b940-6c167f9059d6 | -13.9896 | -48.21864 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb2d2477-d490-33cd-a59b-f64f02994ce9 | -16.20254 | -47.98305 | 2025-09-12 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d3979e8-40ca-36cb-9945-f6c450058768 | -15.07886 | -48.00831 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54a9f2bc-a4ab-3ee8-858c-5f0790f82fb7 | -17.34442 | -46.69375 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a1b9131-326a-3702-839c-a09a8aaa7724 | -11.95486 | -51.12505 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc9b31de-c16e-3c05-b20c-382408755c92 | -13.36611 | -41.91546 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7afa6aac-c53a-3875-9787-ba5247518bf3 | -14.43898 | -53.27921 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 793ef5a6-f514-3a14-b65e-a812175f8f0c | -15.68209 | -47.01419 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86b516f8-d3cd-3774-8857-8f4e56af6041 | -14.417 | -47.31063 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7113666-4f40-3486-b0c4-d7e499eb68af | -11.6405 | -52.25167 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b9ed51-5076-355e-a8fb-b6d6392fcc89 | -12.91877 | -54.80119 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecedae5c-49a7-3f90-91d5-3b7c5207b549 | -13.90068 | -48.2446 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b773cf1-7404-33bf-8e41-b9151a2e14d2 | -19.99947 | -44.22869 | 2025-09-12 04:27:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9c3591ac-ba5c-3106-bf64-91c809412652 | -17.36164 | -46.69647 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31e49537-d628-37ce-937c-ece404efda51 | -14.17843 | -46.17027 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3256ee9a-6ad1-3708-a8e3-3c29f7cbac28 | -15.2471 | -53.76303 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bf0e7b0-1052-349d-b17b-6cf03d54aa79 | -17.47381 | -43.72718 | 2025-09-12 04:27:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b0adf36-30e3-35ff-946b-f193c85f8b1b | -11.78438 | -50.56258 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa29db57-c59b-3730-86f0-303282ee75e4 | -14.51293 | -53.91959 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45944e6b-33b1-378d-8c14-a6052221f2fe | -11.96853 | -51.17754 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5726812f-5008-352e-8653-b4511efb91ab | -15.1311 | -48.60208 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b494d603-53ed-3ee0-a7c7-d21f2bdbb364 | -15.12609 | -48.61221 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22e526ef-5c7e-31b0-a563-3dfd3e13b3d2 | -16.65504 | -47.62593 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48f6ec5a-0d56-33d6-af25-7405800432cf | -17.20532 | -50.15131 | 2025-09-12 04:27:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdd15528-b3ac-3a71-a193-22e84f1cd514 | -13.26682 | -43.74054 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14b39e96-2a4b-3c86-ba8c-16825f53b930 | -14.76878 | -48.23132 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fb05691-b89c-3350-9b56-7ad911b76765 | -12.98302 | -48.01293 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93f48676-5db2-34d6-ab24-4b49ed3bce66 | -19.06126 | -48.73996 | 2025-09-12 04:27:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 244fdd66-1ad7-30c2-b5cd-041500f9b6ae | -13.25905 | -43.76831 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b94e600-56da-3d71-8698-496ccba07466 | -14.17905 | -46.2132 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0925e775-f7f0-3878-bdae-eb5e4e10324e | -11.8777 | -58.8201 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 498703ad-1157-32f5-8705-932b019771e1 | -18.05912 | -45.42685 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d82b1e51-ee42-3e18-87fb-bab2056a3396 | -18.32811 | -52.05752 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05496710-467e-348e-849b-661f78ad8a31 | -19.98926 | -44.21231 | 2025-09-12 04:27:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61c57568-6754-33b3-8549-78f935f1979f | -16.48151 | -51.4001 | 2025-09-12 04:27:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7b958de-09b9-3945-8ad4-660f298a9f1c | -15.10355 | -48.00119 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd767bdb-564d-3fac-8197-436221e54b48 | -15.11223 | -48.09769 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f045267d-5a65-39c6-9776-a8378888648e | -12.92332 | -54.80203 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c863af9-82b7-39b7-856e-4162ef751758 | -13.89849 | -48.23698 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1661a46b-b2e5-3178-841e-1d13dee9d549 | -15.66527 | -47.03431 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aa2076f-e514-3795-96d7-385748f74536 | -14.51501 | -53.90797 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66fc3ff6-a31d-3fba-a38a-99aa9f609bcb | -12.89373 | -47.95547 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 771efaa5-b2cd-3647-8c5e-ad6ba782138f | -15.79807 | -52.23109 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faf9b5c8-c2ba-3418-b167-48e6b7b41314 | -19.83789 | -44.58661 | 2025-09-12 04:27:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d3aea33f-681e-3614-96e9-8b5ded9aa56e | -19.63249 | -41.57618 | 2025-09-12 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ead119ec-39c3-3056-9911-f9de5b0fb4df | -15.69164 | -47.0196 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e9f7794-4a3d-3f47-9f31-9f9f106e03d6 | -11.92105 | -50.71259 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67e659a1-4bfa-31af-b403-478707cc6c64 | -16.20849 | -50.82767 | 2025-09-12 04:27:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81256bb7-711b-3cdd-a9b9-d10bc1da5ee8 | -16.66683 | -47.63057 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06339304-7fb2-3846-91e3-4ec0bf4e3de4 | -12.92291 | -54.75272 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 98c90c8c-e6b2-31ba-b235-d40e669279db | -11.92584 | -50.69796 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5da07eb-8dc6-3772-9973-39d0b4d77d74 | -17.37642 | -52.91339 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 259c029c-6665-340f-9e14-3a8e4f8ebb80 | -15.57376 | -54.74787 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94b2ab9c-3d8e-3bf7-aafb-9e7aa6ae4f0d | -13.17285 | -50.0883 | 2025-09-12 04:27:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e86267a-1ca2-3b9f-98a5-62366d2bd43d | -13.8963 | -48.22934 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bf57aa0-d466-3588-a570-55ae7c795f24 | -15.10682 | -52.46237 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f3546b8-2589-3ca2-9096-1b2f12ecbf18 | -12.84295 | -47.95435 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README85.md)
