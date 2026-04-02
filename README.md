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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c072b397-cd34-3bfd-ae5a-348fea2bcf77 | -19.6716 | -49.335201 | 2026-04-02 00:27:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dfb3c2c8-a5e5-36a9-9096-ab00b802be0f | -20.2834 | -50.432598 | 2026-04-02 00:27:00 | METOP-B | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac1db829-b10b-30a2-afc0-24b746586f9b | -22.1887 | -56.9464 | 2026-04-02 00:27:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1d681ea9-666c-3882-a10a-7e6f6325ca16 | -19.669901 | -49.3279 | 2026-04-02 00:27:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf697a72-5772-3656-826c-fa25dc925c81 | -20.924999 | -49.522202 | 2026-04-02 01:00:00 | METOP-C | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47ac10f3-c61f-347a-89f3-22a22fcf951b | -20.9233 | -49.5149 | 2026-04-02 01:00:00 | METOP-C | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c36a4363-d1fe-3f3b-aaf2-10e158e8ddc3 | -20.915199 | -49.5247 | 2026-04-02 01:00:00 | METOP-C | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cdcc37e2-7306-37d6-8392-c045db5bbf24 | -20.9266 | -49.529598 | 2026-04-02 01:00:00 | METOP-C | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7482269-b55e-3f0f-9302-193f048a25dd | -22.180901 | -56.9617 | 2026-04-02 01:00:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b7d67ebc-8288-3e7a-ada1-adf155d122c7 | -22.1821 | -56.97284 | 2026-04-02 01:17:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c88d53ee-850a-3a65-a78f-60d5e4e86b5a | -16.42698 | -54.91199 | 2026-04-02 01:17:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6a1a4828-ae2a-3478-913d-503e13458be6 | -19.5972 | -40.07436 | 2026-04-02 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 979af3e5-2725-32f4-b755-08d349586fb8 | -12.06228 | -45.34107 | 2026-04-02 03:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2b6c1fc-3960-39a0-be25-0488dac1bde5 | -19.38191 | -43.5836 | 2026-04-02 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b32e4849-a04e-3adf-b4d2-0d451ebeac3b | -19.60225 | -40.06398 | 2026-04-02 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b01c7c9-c41e-36e0-9be7-b52e6af31a6f | -19.37942 | -43.58508 | 2026-04-02 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d98a575-13e8-38bf-aaa7-e9196d33ce7b | -19.60167 | -40.06764 | 2026-04-02 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 208c58d5-7836-3bb8-a3e3-d093ef3fccd9 | -19.59057 | -40.0732 | 2026-04-02 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54108ce7-6cd0-333e-97ea-8fc3ee5f57af | -19.36393 | -43.58635 | 2026-04-02 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4758ac6a-dffc-3fcd-b4fc-c612a07f967a | -19.37041 | -43.59291 | 2026-04-02 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f67fdce-7661-3b74-a774-8f6b3bad3fb6 | -19.58784 | -40.06896 | 2026-04-02 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d9036cc-cf14-36a5-b836-a3f28e8216b6 | -19.36674 | -43.59211 | 2026-04-02 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2cf8b62-ab25-3bd4-8938-475da372b91f | -19.38026 | -43.5803 | 2026-04-02 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab0d10c6-181d-3996-98fe-4d6aa190d529 | -19.36758 | -43.58729 | 2026-04-02 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32c6a28b-5de1-3ab5-af3c-3ae37fd877b1 | -21.71614 | -48.43314 | 2026-04-02 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 477de3ed-f69d-376c-9c69-895c04431cff | -21.71144 | -48.4319 | 2026-04-02 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29573032-79fe-370a-afcf-e283c6a2963b | -19.67164 | -49.34092 | 2026-04-02 03:53:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb62ccd-ffdd-3cb0-9a29-c9ed5c1b1d94 | -19.67167 | -49.34077 | 2026-04-02 03:53:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76f3871a-7f8e-3557-9326-774fe7802b39 | -18.79058 | -48.54956 | 2026-04-02 03:53:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6636eee2-53d3-3d15-b835-e63dd4243d51 | -21.71528 | -48.43524 | 2026-04-02 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d6d2019d-27f4-31ba-954e-bc9124328ea1 | -30.05766 | -50.8503 | 2026-04-02 03:55:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 3553b663-2434-3673-bebd-7b368c613a63 | -25.47557 | -49.8655 | 2026-04-02 03:55:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7138235a-ef58-3f53-a4f7-cfa93f6c6b5f | -25.47437 | -49.8665 | 2026-04-02 03:55:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5a766d90-4bf1-3240-9ee6-b1d97b605e1d | -25.47433 | -49.87129 | 2026-04-02 03:55:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6fe1ba2c-a5e1-3499-aef3-abbc8a1c2a14 | -19.38118 | -43.58181 | 2026-04-02 04:23:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3dc40b5-9ee0-37ef-883f-b8524163a700 | -19.89781 | -43.96266 | 2026-04-02 04:23:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8fe4d75b-9203-397d-a0fe-3ba936df9aa1 | -16.43313 | -54.91182 | 2026-04-02 04:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49d9b49e-7046-36b0-a796-9c6b92859a96 | -19.27774 | -55.15846 | 2026-04-02 04:23:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5e1000f-d8d4-3227-b48f-9a2dcf22d3b7 | -19.67344 | -49.34267 | 2026-04-02 04:23:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe8913d-f809-3c91-94c9-3df80c5ca1f8 | -16.4317 | -54.9188 | 2026-04-02 04:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c83b39fc-9bca-37da-b1e3-da2a405a2c52 | -19.67419 | -49.33835 | 2026-04-02 04:23:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c32c937-1119-3368-b0a4-1bfba1316d44 | -19.60143 | -40.06638 | 2026-04-02 04:23:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8741bbb3-e685-382b-9f3f-b934c6d72434 | -20.91889 | -49.52538 | 2026-04-02 04:23:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7582b330-f883-333f-9f31-7f26208af4ae | -16.43242 | -54.91529 | 2026-04-02 04:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| faed48ab-50c4-33a2-a2c8-cd4968a21b9e | -17.9051 | -54.12354 | 2026-04-02 04:23:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60313d01-bff6-362f-8cc8-b94d28276a61 | -18.79082 | -48.5486 | 2026-04-02 04:23:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56498896-58f7-3e60-aa6c-edda2e0bcf7e | -19.3806 | -43.58587 | 2026-04-02 04:23:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7853b0c9-0223-38a2-a594-a78120edb540 | -19.59917 | -40.0682 | 2026-04-02 04:23:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0fef2fd-a552-3db1-9501-a8f302e4efb6 | -19.66986 | -49.34199 | 2026-04-02 04:23:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe82cfe7-007e-3a29-9793-59d3d4fdaffb | -19.59972 | -40.06395 | 2026-04-02 04:23:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a0876855-8535-3e38-849e-f0414f99cc51 | -19.27844 | -55.15517 | 2026-04-02 04:23:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e81f853d-c5b4-3130-8e44-e5ae61e21126 | -20.91458 | -49.52895 | 2026-04-02 04:23:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 536933fd-a333-3bd8-83f3-e2b543fb910b | -20.91813 | -49.52964 | 2026-04-02 04:23:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 13f8f364-73ff-3d46-ac0d-2ae629ddba8f | -22.18522 | -56.96917 | 2026-04-02 04:25:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 120938e0-2a37-3098-b2c9-fec01c6ef094 | -22.18442 | -56.97279 | 2026-04-02 04:25:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32b76e3c-7e09-3e2a-8782-6aa7986ce2ef | -22.17914 | -56.97112 | 2026-04-02 04:25:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aec1fc17-58fa-3148-8b49-35d76256a405 | -25.4756 | -49.87057 | 2026-04-02 04:25:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 72610648-7b5a-39a9-8c1a-8401c9b41c7b | -21.04194 | -54.31004 | 2026-04-02 04:25:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95a31159-5586-3460-bb65-99622ce8c07b | -25.47631 | -49.86645 | 2026-04-02 04:25:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 073ee2f5-f820-3c16-8e91-3211c18892c5 | -30.05903 | -50.85165 | 2026-04-02 04:27:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 9da2a089-6e25-35f8-90e3-f273ae235da7 | -30.0583 | -50.85586 | 2026-04-02 04:27:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 2d2e59c8-bcfb-3267-b417-63c58c41b618 | -31.55211 | -53.28447 | 2026-04-02 04:27:00 | NPP-375D | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 88570f1c-1260-35cc-9fb8-a08b6c6313b0 | -30.0549 | -50.85508 | 2026-04-02 04:27:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| abb689b2-10ac-31d1-a310-dd9491d7f000 | -31.03536 | -53.08983 | 2026-04-02 04:27:00 | NPP-375D | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 4efec9d7-c439-3d1e-bd54-2bf6520cfc15 | -18.43597 | -54.71867 | 2026-04-02 04:44:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaa7fe20-1a7a-3df0-8a22-1b338c0074e7 | -16.43423 | -54.91199 | 2026-04-02 04:44:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0e6cba3-9b0f-3e55-9cc6-0e97f20ba50e | -17.90338 | -54.13038 | 2026-04-02 04:44:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8124f609-8adb-33a8-b1aa-219017ec7dbc | -19.30241 | -49.69687 | 2026-04-02 04:44:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 230154a0-63cb-362a-8a7c-16cc9f209f6f | -18.43319 | -54.71405 | 2026-04-02 04:44:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b86c1bbc-0073-3aed-8d13-7c09b04c8aed | -17.90467 | -54.12267 | 2026-04-02 04:44:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1551a2ed-25d7-3931-84f4-dbc288c660e4 | -17.90402 | -54.12652 | 2026-04-02 04:44:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a534d6-52c3-3794-a420-de29e18ee007 | -16.43067 | -54.91129 | 2026-04-02 04:44:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9cb887a7-5dd4-3847-b4cd-4320a6f36ce2 | -19.27611 | -55.15372 | 2026-04-02 04:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cb9dc31-47fb-3908-a770-547edeca78a4 | -16.42993 | -54.91554 | 2026-04-02 04:44:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8faed7d-f4a7-365d-ac27-b0bef2a3fc44 | -18.79177 | -48.54732 | 2026-04-02 04:44:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9da9fc3d-6734-3565-9804-09632abd9ca0 | -18.78805 | -48.54671 | 2026-04-02 04:44:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b2e0542-e805-34a5-8898-f4f84d4621bb | -19.67277 | -49.33767 | 2026-04-02 04:44:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06dcc997-950b-3e52-bce3-23f77aa3e766 | -19.67217 | -49.34205 | 2026-04-02 04:44:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a72a75c-f2b3-30d1-9f7c-2ce013f939f4 | -21.66715 | -56.32034 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dae4627f-fcf1-34ec-923b-a97b889d5562 | -21.6952 | -56.30787 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8a87aef-1929-3f95-9659-27c563868fb9 | -21.71289 | -48.42967 | 2026-04-02 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 345e8991-08ea-3b5f-969a-b5ea8df450a5 | -22.1868 | -56.96929 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96197ea5-bb2a-3737-b7a5-9808c81a3140 | -22.18316 | -56.96846 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15785f71-894c-3166-b32e-964e5ec77766 | -31.55032 | -53.28362 | 2026-04-02 04:46:00 | NOAA-20 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 3ac90e69-d3e1-326d-8dca-ef1831169cbd | -31.03312 | -53.0872 | 2026-04-02 04:46:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6261bbe8-fd6c-3fab-8edd-8f54c787d49e | -22.17952 | -56.96762 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e880a9fc-1cfe-31e4-9170-738b33f17143 | -22.17868 | -56.97224 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f83c01a-b1b2-32f8-b881-c0fc1765ec81 | -21.66359 | -56.31956 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d160dcca-79e4-3282-a9aa-0544009a6643 | -21.04483 | -54.30932 | 2026-04-02 04:46:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4dba3e2d-6248-3bc9-b700-6aa213fc070d | -20.14437 | -52.83731 | 2026-04-02 04:46:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28c67942-a8ec-316d-ab75-8123f9c9a984 | -21.7122 | -48.43488 | 2026-04-02 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26ead000-b97c-36f5-a23c-40c929e4f67c | -19.98906 | -54.74132 | 2026-04-02 04:46:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aa527ce-6b22-30ae-8e7d-5009ea1c390f | -21.66281 | -56.32394 | 2026-04-02 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a91ec14-61de-39a6-af28-cc69d0e7b9ae | -21.04147 | -54.30868 | 2026-04-02 04:46:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7d0c73d0-f3f8-3049-b4ea-99e1cdf73689 | -29.11073 | -51.32758 | 2026-04-02 04:49:00 | NOAA-20 | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 77327d37-9efe-30df-96e6-4f8488884fd8 | -22.18294 | -56.97251 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 993ab44a-35c7-31b4-a860-2e944936b796 | -22.18326 | -56.96939 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6effa5ca-93df-33e1-bd08-79e462249904 | -21.66493 | -56.32434 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 775f7308-2fac-3333-be66-0c03c5202c4d | -16.43029 | -54.91323 | 2026-04-02 05:33:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39f9d586-b399-3bb3-8103-084bb182ee77 | -16.43567 | -54.91378 | 2026-04-02 05:33:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README2.md)
