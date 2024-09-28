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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a25371af-7667-3bd0-8b7b-4f90cac3ccf7 | -3.45397 | -54.10333 | 2024-09-28 05:21:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9b0fac68-9ac6-36e5-b6d0-2f47eaf1ad6b | -3.44377 | -54.07609 | 2024-09-28 05:21:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 54a13592-ec67-326b-a9ce-0393d271006e | -3.33242 | -50.30443 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9e96b5e1-740d-3e6e-9f39-46c000963bd6 | -3.32591 | -50.29782 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 8db4967b-24e3-3a50-b753-3f696d60e0eb | -3.324 | -50.31047 | 2024-09-28 05:21:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7622c309-f230-3ea2-a079-e893bdfb7ad4 | -3.19348 | -50.42717 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 514e4124-124b-370b-9d9c-071487b6d998 | -3.19149 | -50.44031 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 31815adb-d74a-3c75-8cb2-96b1f817f3bc | -3.13789 | -53.68657 | 2024-09-28 05:21:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| efb2f3ba-022c-31a8-8eba-5992470b9afb | -3.12768 | -53.66195 | 2024-09-28 05:21:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3ce15f06-bbf9-3bbc-bf7b-3baf99e337a4 | -3.11321 | -53.75383 | 2024-09-28 05:21:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 4fd1ae82-2e82-3466-81af-938421aeb7b6 | -3.08293 | -50.47121 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 51af4a12-5991-3193-a2e4-8d0f0867f5a9 | -3.08094 | -50.4842 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 1afafa04-81f7-3fca-806c-86c131c9975d | -3.07231 | -50.4696 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 995fb3dd-ccb2-37a6-a974-607f5e58c42c | -3.07031 | -50.4826 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2dcb8026-1169-3c19-97e9-23f229dcb5eb | -3.05921 | -49.55123 | 2024-09-28 05:21:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 71a17917-001b-3224-974c-aa1e946784aa | -3.05749 | -49.56259 | 2024-09-28 05:21:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 70b6f839-96fd-35fb-972a-779e61dd3743 | -3.04753 | -49.56114 | 2024-09-28 05:21:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4cacfe27-2e25-31df-90e7-6021c39d5d9b | -3.00601 | -51.04753 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f52073d7-1e50-3cab-863d-b4c0cf320dfc | -2.94682 | -49.35638 | 2024-09-28 05:21:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e290841f-c0b5-3881-b182-a123c681436a | -2.88789 | -50.46964 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 620b427f-55e9-3509-8946-34411d6b4215 | -2.8756 | -51.66628 | 2024-09-28 05:21:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 7a53cef5-5362-3af8-a071-2283987c534f | -2.87309 | -51.68241 | 2024-09-28 05:21:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 4c6f7e71-afa9-394a-81ae-95e0bce7fec0 | -2.86388 | -51.66452 | 2024-09-28 05:21:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d8751a07-75b5-3628-b28b-45935b02ddad | -2.82246 | -51.34659 | 2024-09-28 05:21:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 62b27ddf-f799-3ac6-bd53-479f6160f96a | -2.71901 | -46.71955 | 2024-09-28 05:21:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ad82e694-c847-3070-bc34-42199f86f0b2 | -2.71769 | -46.72837 | 2024-09-28 05:21:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 335b4f4e-bafc-3337-8bf8-99b955b1ded3 | -2.70884 | -46.72707 | 2024-09-28 05:21:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 84de1694-89e9-36e2-b415-65f266d0c355 | -2.63008 | -48.05164 | 2024-09-28 05:21:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f78c0aab-11e4-3983-96f3-e5b04e2ac824 | -2.62513 | -48.31438 | 2024-09-28 05:21:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4e9618d9-e07d-3b16-a85a-6ac551a5690e | -2.61872 | -48.31683 | 2024-09-28 05:21:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1e42500c-9ec8-3fe9-bc31-bc3e439e4058 | -2.48046 | -48.05304 | 2024-09-28 05:21:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1fe9d807-5a25-35c1-bb0b-12ce1b1e16d8 | -2.47495 | -49.1482 | 2024-09-28 05:21:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 495ee97b-8ab1-37eb-a152-c0aef3672b43 | -2.47332 | -49.1591 | 2024-09-28 05:21:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 94a6ada9-f242-3ae1-9dd9-710102aa0a42 | -2.47317 | -48.05521 | 2024-09-28 05:21:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 038458dd-9140-3b1a-addb-9ed469d3d4a3 | -2.35744 | -47.59353 | 2024-09-28 05:21:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dc7cbd5c-1af4-37d8-bc43-6e84c22ce564 | -2.35606 | -47.60276 | 2024-09-28 05:21:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| be3ca5c4-cd44-3035-9a39-273d557a67af | -2.35468 | -47.61203 | 2024-09-28 05:21:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| da34bee3-2ab6-39be-a208-8a6a168b9987 | -2.10623 | -47.11073 | 2024-09-28 05:21:00 | AQUA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 65945e19-ba22-3a91-91b2-241d9bf3c84c | -2.10488 | -47.11973 | 2024-09-28 05:21:00 | AQUA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 973699e5-6df8-318a-9907-20bd610b68df | -1.76131 | -47.19228 | 2024-09-28 05:21:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03a21699-a477-35af-81ce-b787215c2434 | -1.72601 | -47.12241 | 2024-09-28 05:21:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| e2c87df5-0739-3294-86d3-04144fdf03d2 | -1.72464 | -47.13144 | 2024-09-28 05:21:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f59f484d-76fb-3543-9f71-02e61448374b | -1.71705 | -47.1211 | 2024-09-28 05:21:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29929bfd-0613-3bf6-92eb-dd39de7f4a8e | -1.66465 | -47.46803 | 2024-09-28 05:21:00 | AQUA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fce0f498-52fc-37da-9799-75134d96ae90 | -7.76311 | -44.68331 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c35f73a2-d6c4-3588-a1c0-5ce603d72ad4 | -8.87448 | -45.65281 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 96175b86-d345-32d8-b559-87a2289d06e3 | -7.88923 | -44.60299 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c262bf78-b074-3112-af6d-7ac0c3e34e61 | -7.88769 | -44.61399 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| b1bbce86-ad1b-38ca-b0bd-7d577dcb5d1f | -7.88105 | -44.59024 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bfde2423-b7e4-3bf4-8b16-bc56835d4220 | -7.87947 | -44.60159 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 8bcbfb1c-569c-3b1e-b52b-884dc1b48600 | -7.87738 | -44.59543 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 534426fb-f81a-335b-bb1f-ff1011ed9854 | -7.87575 | -44.60659 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cef33942-fd08-3dd9-b48d-4a735e6af287 | -7.83151 | -45.47985 | 2024-09-28 05:23:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2d4e9313-52fe-3a2e-bbaf-8258bb297cab | -7.78861 | -44.66068 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 301f4913-3eb1-3448-88ff-dbccc6bdbd77 | -7.7871 | -44.67146 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 6d5c22c8-cb92-3bc7-b9b8-a0dbc321c6e4 | -7.77437 | -44.67392 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d0298617-e125-3d4b-879d-1e9d5125a176 | -7.7728 | -44.68473 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5b21c2f6-660d-3910-8850-06a9c2752f1c | -7.76467 | -44.67253 | 2024-09-28 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d3a4d81f-fb14-3b27-9f15-308ce9ad1154 | -13.45297 | -48.58261 | 2024-09-28 05:23:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 243b88c0-51af-3e16-a820-2576114e3baf | -13.34296 | -46.29583 | 2024-09-28 05:23:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ae282022-645f-37ce-88cb-38d99b22325c | -13.27241 | -46.31726 | 2024-09-28 05:23:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 400edc97-ac5d-3e8c-9ac6-437d7b623d5a | -13.27099 | -46.32748 | 2024-09-28 05:23:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8a1556af-8c98-32dc-93fe-5dbd34362b6c | -13.26152 | -46.32632 | 2024-09-28 05:23:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cb85ed1e-c35b-304f-b537-adbe1b7ffbea | -13.25197 | -46.32582 | 2024-09-28 05:23:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f89dc29d-d83f-34c8-9cd4-8d30526e0d0c | -13.24675 | -46.3288 | 2024-09-28 05:23:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 54df8b6c-ff93-37da-93b9-649899a98bf4 | -13.16807 | -48.51171 | 2024-09-28 05:23:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| acd22c9d-ade3-3403-8aae-4883327bc387 | -11.10376 | -45.58626 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ab0ee657-6809-3dd4-8419-20027f2ea750 | -11.04349 | -45.73869 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 4b58ff79-17e0-3a64-ac22-723a0949d26e | -11.02297 | -45.70875 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| f762e599-ed93-3b14-af2d-6e4a93529872 | -11.02147 | -45.71917 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8224568f-1f22-39da-ba3a-2d968e841840 | -10.98926 | -44.42059 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 096ca4f6-2498-3d82-ab66-781f74e14725 | -10.98756 | -44.43303 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 050d033c-3e33-375e-945d-3c7ed262fc7a | -10.86672 | -45.51338 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0831f54c-3bda-3590-b5ca-927df42d0347 | -10.84308 | -45.54205 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| f86abb39-ce5a-3530-b6ad-e0c83df273f0 | -10.84163 | -45.5523 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4bd4d8db-1b9d-314f-94e6-722491ae4c25 | -10.82749 | -45.9668 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 979c892e-716a-330b-988b-faea9b4c6513 | -10.82608 | -45.97681 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d01b974a-e896-313c-b99a-948a9fd55466 | -10.69624 | -45.86338 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5a3cb94a-cf81-3739-ab15-5883ae1cb412 | -10.67533 | -45.94315 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dd613a3a-f259-3907-b3c8-524aa049d98c | -10.65035 | -46.05189 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 134bc021-a39c-3ee7-897c-b090f4e7ff63 | -10.64895 | -46.06176 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d7b24d21-5ffc-3d5b-aef3-54fe4bbde981 | -10.64245 | -46.04065 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7d3ac822-bd8c-31bb-8adf-55a6364e6c71 | -10.64105 | -46.05053 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 9c139a6c-1e91-30e2-ba9a-2044a2a2245b | -10.63965 | -46.06039 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 6119f369-0901-30a6-bd65-f8a50a7e4d1c | -10.62896 | -46.06896 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7b70af21-669f-3017-bd5e-babb2bd54f2d | -10.61332 | -46.06109 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 24f21d5e-2355-3339-97e3-5c31ab42f39c | -10.5897 | -46.02732 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b6ba6f4-981c-37d5-9b84-3cbac114dc03 | -10.58827 | -46.0373 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a373aceb-46c2-351e-9fe6-ebc7bc17a060 | -9.89243 | -50.13496 | 2024-09-28 05:23:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c590fbd7-a603-387a-9b38-65768c5e115b | -9.6374 | -53.58577 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 802700fc-363b-3368-a812-f00590239523 | -9.55767 | -50.19006 | 2024-09-28 05:23:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8b6260b6-6491-3e6b-8081-d1702c55cfe0 | -9.38141 | -50.01385 | 2024-09-28 05:23:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b568bbb4-59ec-3ab4-9750-414b8e1eb299 | -9.37604 | -50.01666 | 2024-09-28 05:23:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 8aef7336-b9aa-3cc1-9c36-2681a57aad24 | -9.34668 | -50.73513 | 2024-09-28 05:23:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f847840c-2cb8-352d-a262-7b9d01bd3236 | -9.34496 | -50.74622 | 2024-09-28 05:23:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c51ff099-e7f9-3baa-8854-8a8bd1e58609 | -8.80599 | -58.17701 | 2024-09-28 05:23:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3240084d-b648-36e1-929d-a4eb55c17d92 | -8.80372 | -58.17208 | 2024-09-28 05:23:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e13910ac-3137-3536-8f6a-c640d75495a1 | -8.79859 | -58.21696 | 2024-09-28 05:23:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7573a341-3798-3494-bf12-076ff242e0e2 | -8.79658 | -58.21204 | 2024-09-28 05:23:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 15d3d0d5-b732-37ad-a14f-dd4848aaa2f7 | -8.74744 | -49.77228 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README97.md)
