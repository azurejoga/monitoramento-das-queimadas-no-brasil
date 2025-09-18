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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58154a26-9258-385a-a229-c6f3d1fb993f | -22.34113 | -46.75371 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d33843b0-611d-3fcf-a782-9f095b4ce7df | -22.34503 | -46.75059 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1add3003-ffd5-3920-8a50-c9d6186bce65 | -22.33782 | -46.75311 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1b125677-c2ad-3b26-b726-33cfd3d71e80 | -22.66734 | -47.4995 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96cdd253-98ed-32bf-b6b1-9f1e99b82065 | -5.78275 | -43.87814 | 2025-09-18 05:04:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| ad3c263c-ca04-3280-bfd6-a18a390a5251 | -4.81112 | -42.72616 | 2025-09-18 05:04:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 47e70914-60d3-33e3-8518-1e17e69ad592 | -5.78252 | -43.88617 | 2025-09-18 05:04:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 60664a01-4217-3c46-9a9e-4f48ac68b75d | -4.80223 | -42.71979 | 2025-09-18 05:04:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 6d1f0958-a1d9-322e-94a5-aa974b80c6ec | -5.77583 | -43.91899 | 2025-09-18 05:04:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 0b3b3b32-18cd-3604-a7f7-947072d55d14 | -13.07162 | -42.14322 | 2025-09-18 05:06:00 | AQUA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 74.4 |
| d02d183a-2302-3ab1-a241-f6f70f3bbaf7 | -13.07595 | -42.11874 | 2025-09-18 05:06:00 | AQUA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 42489dce-39b6-3023-b43f-333b9134702d | -15.9757 | -38.93954 | 2025-09-18 05:06:00 | AQUA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 0df7521c-478b-3e04-a0f7-301a61a6c399 | -15.97426 | -38.93372 | 2025-09-18 05:06:00 | AQUA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 2ebd939d-3ddf-3f34-9dbc-0bf2e982f73c | -15.9724 | -38.94518 | 2025-09-18 05:06:00 | AQUA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 310e886b-e0fb-3a95-b047-fa2c0e516c1f | -11.93112 | -38.32702 | 2025-09-18 05:06:00 | AQUA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| a2b81786-2461-3273-8912-7dfe8ecaddb4 | -15.97378 | -38.95092 | 2025-09-18 05:06:00 | AQUA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| c7a2accb-82a7-3242-9911-dbaecea023d0 | -12.89939 | -44.65224 | 2025-09-18 05:06:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 29fda684-10f5-30fe-b40d-d865b6df9e4c | -12.90609 | -44.64857 | 2025-09-18 05:06:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 729c8c67-4a88-398c-aea9-29d899bc98a7 | -18.53449 | -46.03382 | 2025-09-18 05:08:00 | AQUA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b2e696d1-d28f-300d-95cf-d938642caaab | -18.53991 | -46.03011 | 2025-09-18 05:08:00 | AQUA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 36.9 |
| b526553c-112f-3536-8c47-d8318585e5a5 | 3.15268 | -61.00285 | 2025-09-18 05:29:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b0e5dc8-30fa-3736-b802-720784551616 | 3.14317 | -61.00795 | 2025-09-18 05:29:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6b9a47d-15b6-3972-a134-6ed6a199c26c | -0.9081 | -47.55072 | 2025-09-18 05:29:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2309319c-c7fd-38ae-a40b-9605b25deb7e | 2.41412 | -60.69927 | 2025-09-18 05:29:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fced6f45-3d70-3349-b133-9b8c0f7b6654 | -2.9225 | -48.31417 | 2025-09-18 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e071d11-a53d-3f1e-b70a-760027470546 | -2.30098 | -48.14566 | 2025-09-18 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d9c1e78-213b-33e8-9f71-1cca71e6b62c | -2.38146 | -47.71963 | 2025-09-18 05:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f08511f-365c-3d3a-936e-478ab9e3b2b0 | -2.92196 | -48.31454 | 2025-09-18 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d11fe929-f2e6-30c1-8e4e-1b6acf96f38c | -0.90214 | -47.54289 | 2025-09-18 05:29:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac50b684-7a39-346c-acf8-797db3b27850 | -0.90292 | -47.54747 | 2025-09-18 05:29:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61702e43-d731-38d2-9bf1-9d58d2861833 | -2.3785 | -47.72203 | 2025-09-18 05:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7788e70d-ec58-3a86-9dce-56e0071a4558 | -0.90988 | -47.54878 | 2025-09-18 05:29:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a239afa-77b5-3e49-8d6a-1f8bd4358f17 | -0.90911 | -47.54418 | 2025-09-18 05:29:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d0255d1-70b9-3063-ab44-d53749cb2add | -2.29409 | -48.14465 | 2025-09-18 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75a8bd7f-2089-3272-ba72-08175d11ec82 | -8.66965 | -62.59618 | 2025-09-18 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04890698-2411-3daa-855d-ecd611cd356a | -3.51531 | -49.44792 | 2025-09-18 05:31:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a355665-94cb-3e8d-948b-f3875c6477b3 | -3.28066 | -49.14727 | 2025-09-18 05:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4c2fd5d-930c-3373-a774-a24d578cf527 | -8.07796 | -50.16956 | 2025-09-18 05:31:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef02142d-7965-33d5-bf95-e353ac73c92f | -3.19978 | -54.97774 | 2025-09-18 05:31:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dae7db29-31ef-38fe-b12f-1da09eaf2a86 | -3.60617 | -52.62783 | 2025-09-18 05:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f4a4248-4a03-3ce2-bcc9-011f114e1328 | -3.68994 | -55.95724 | 2025-09-18 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c47f7e29-d09e-3660-919d-17e559cd2db5 | -4.35721 | -55.58844 | 2025-09-18 05:31:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cb59b2f-ecd3-3b83-8857-454504bd78f6 | -3.94713 | -55.84886 | 2025-09-18 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18c7a884-6522-3cc1-b978-be1897aecf52 | -3.51231 | -52.75487 | 2025-09-18 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fab3e6f-1544-31c4-afd2-d943effaa2a2 | -2.57406 | -54.65644 | 2025-09-18 05:31:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a1567a8-d53c-317e-ada7-0c76d24be927 | -4.30847 | -55.3443 | 2025-09-18 05:31:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8472789-65d2-3b0c-8ea7-6a98f9012aa8 | -3.518 | -52.75247 | 2025-09-18 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3dfa0cc2-6efb-3646-be42-e214d0813cc9 | -2.71056 | -54.95748 | 2025-09-18 05:31:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab81f59c-ee6b-3f60-ab33-9664178f477e | -3.5171 | -52.75541 | 2025-09-18 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3575cc8-9673-3e80-a931-7e654905cd0a | -3.94287 | -55.84826 | 2025-09-18 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2faedc44-0ff5-308f-9ee2-64e1a5e0918a | -2.71566 | -54.95385 | 2025-09-18 05:31:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9f5dcb2-7b18-30d8-b696-be002ccf048d | -8.07853 | -50.16521 | 2025-09-18 05:31:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deeb2651-a48e-3372-a70d-b2544025dcc4 | -5.33417 | -55.88863 | 2025-09-18 05:31:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47c23bcb-5b8b-3a14-8f41-a5919bb7d5c5 | -2.56955 | -54.65574 | 2025-09-18 05:31:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a8a926f-03de-31c1-be50-c5f8d3bda0ba | -3.51758 | -52.75224 | 2025-09-18 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2da837bf-6840-38bf-be9e-2d1599b0582d | -3.74024 | -49.05256 | 2025-09-18 05:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bec237c1-30d2-3c38-928a-92b65e258aec | -3.61148 | -52.62839 | 2025-09-18 05:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8075b505-4b54-358d-93b4-9af567cdaa9c | -3.73681 | -49.05174 | 2025-09-18 05:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00862386-4fbe-30dc-8592-5c8882fa510f | -3.94346 | -55.84436 | 2025-09-18 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 363dc17d-67c1-3385-a804-bcd6ecbf1a19 | -8.6702 | -62.59269 | 2025-09-18 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91400a0e-35ed-3046-b640-79e14fb5c169 | -7.24015 | -60.64579 | 2025-09-18 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4f5c820-e6d7-3623-9526-737f62f64790 | -3.74343 | -49.05294 | 2025-09-18 05:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1567f995-c410-35be-a4ba-3ffa6ee2b483 | -3.51278 | -52.75164 | 2025-09-18 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c7c82893-b10f-3c0c-9824-ea3a42af5c64 | -2.71122 | -54.95319 | 2025-09-18 05:31:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d3e1b11-8ab4-38d1-85ca-e13029993bd4 | -6.85602 | -59.963 | 2025-09-18 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e158245-72bf-3fcf-85b4-2dbdafe83cd3 | -3.2741 | -49.14624 | 2025-09-18 05:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e31047-0dcb-3534-8d04-dfd5ae8eadc2 | -3.19533 | -54.97706 | 2025-09-18 05:31:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57950b4c-bfb5-3bfb-beb5-95ecdf3887a4 | -3.51188 | -52.75464 | 2025-09-18 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2112a634-6b76-33c3-8ad2-3658ca0af816 | -5.32984 | -55.888 | 2025-09-18 05:31:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 391a0060-084a-3f41-ab42-a28ff900e767 | -3.51237 | -52.75143 | 2025-09-18 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c11f1df-f263-3713-9dec-b4195abef308 | -10.40464 | -61.19754 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c9f57dd1-2b8a-3297-ad3f-68f9e2489d7e | -15.31667 | -59.40848 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc526ec-06f9-3261-9ba8-2bd4f617cc49 | -8.96494 | -67.46886 | 2025-09-18 05:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46a48bb6-2c5b-33b9-b190-45b0fcbbea93 | -10.41494 | -61.19913 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83e1cbbd-e9dd-3135-9903-34016b810ab8 | -15.92238 | -56.28446 | 2025-09-18 05:33:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 12b7e820-2afb-30c6-9a33-302cc05bc035 | -15.32701 | -59.40672 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2b87fad-ee63-3839-9f4f-9fc73615d7d2 | -12.82058 | -52.98355 | 2025-09-18 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21a0c79c-153d-3ffb-b103-e2900f7cfc26 | -9.47032 | -60.48183 | 2025-09-18 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e8cc8ae-e3ea-3f21-866d-ea9a3df84eb9 | -9.49262 | -63.46478 | 2025-09-18 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 210965d2-0186-3379-9236-8eb43b1b6fb1 | -9.46682 | -60.48129 | 2025-09-18 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c434c22b-47dc-324f-9118-a1e52554e142 | -10.40235 | -61.21254 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b062c54e-263a-3cbd-872c-5cba4be39e07 | -14.78935 | -60.23275 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10aa260d-b1dd-38cd-989d-f7c062ec2014 | -11.3719 | -50.8368 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6954c675-a0dc-3879-9364-3cf2bdd8ef4e | -9.15335 | -61.17528 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f30a458-3e01-39a5-bff1-4eb0bdaa77ea | -14.78185 | -60.23169 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6e63fe4-e677-3b66-8ba4-90174760dd6f | -15.31305 | -59.42062 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 46f58200-e21a-30b1-88b6-e96236ebdde9 | -14.79629 | -60.21031 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0a477c2-ad5c-3b67-9f15-bb7204665562 | -15.81388 | -59.40089 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dda49059-af46-38fc-87f1-d27dac87686f | -9.77929 | -66.07799 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f22e51f7-730c-399d-9f07-250106cacd0f | -9.00105 | -63.67968 | 2025-09-18 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2e90f70-e660-398e-8d1f-3fda73925c2a | -9.42428 | -67.61192 | 2025-09-18 05:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb6eb345-b187-3958-8135-2cf07a09bb7b | -14.80005 | -60.21086 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1a657e8-9771-3562-8488-3f7df58766bb | -15.30658 | -59.42292 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c59049dc-08e0-355b-bdf4-9b9bdb668dca | -10.94059 | -60.75486 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01093396-c73a-3d9d-9d4d-b3a239a00888 | -10.40751 | -61.20181 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06078097-17ea-3b14-8891-23c1b66316c5 | -9.15373 | -60.36004 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff595ec0-5e7f-332b-bd1a-54473f6471c5 | -9.14478 | -61.93303 | 2025-09-18 05:33:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 712eb2c3-dd63-3906-be06-c7a2a703d33c | -15.31837 | -59.41096 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bda1608a-9b6d-3528-829d-2e81cfad577f | -9.61561 | -63.58587 | 2025-09-18 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84e49d72-94b6-3752-b3fe-fbb5b7567488 | -9.9352 | -66.73026 | 2025-09-18 05:33:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
