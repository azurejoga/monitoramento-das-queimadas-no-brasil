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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3f00b1e-b68b-3cbc-8a64-49f4bc7d7791 | -10.04151 | -44.1893 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ca9b48f7-68a7-3347-b676-3e490042f080 | -10.04028 | -44.19743 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d8998f6-0d64-3646-b1a7-7e6084259726 | -10.03967 | -44.2015 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ee3b6d1-cec9-3c08-93b1-d6f56c5fa38f | -10.03906 | -44.20554 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9975382e-7241-3c18-93cd-e58385b6de5f | -9.58284 | -43.50185 | 2024-10-15 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 063d2607-7f78-3d69-93d1-5a9c390e7c63 | -9.57187 | -43.50013 | 2024-10-15 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d2e3ee4-49dd-3331-9bf2-fbd40e276954 | -9.56821 | -43.49956 | 2024-10-15 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af80596d-2ef0-3413-acfd-b3c06e25b9a1 | -12.08324 | -43.88964 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47d1e3c5-14a0-3816-8194-420d9e1cc6a3 | -12.07955 | -43.88908 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 622445d2-4696-3621-a764-fdbbbf28f37b | -11.89 | -43.81435 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbcb1aba-fe98-39f1-83c9-796824de2780 | -11.8863 | -43.81379 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fab4745-aa44-34fc-8df3-8ab2fd252c9c | -11.88566 | -43.81822 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bce1c5cc-bb46-34c9-98a0-d6981777c660 | -11.8826 | -43.81323 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e7ab0a6-324d-392d-886f-24245e50969c | -11.88197 | -43.81765 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f6eb10a-adf8-3353-8b75-79983c360a8a | -11.87954 | -43.80826 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fa5d6f6-969a-3e6c-8d89-28622526b5e4 | -11.8789 | -43.81268 | 2024-10-15 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51b3dfe3-a576-31d3-998d-435b1ba27f9c | -11.72488 | -44.57919 | 2024-10-15 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a06e3792-0a43-32a2-a52d-9d6878baba9a | -11.72133 | -44.57866 | 2024-10-15 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77ba45ba-d75f-3a01-b806-99950a6f545f | -11.13452 | -44.18125 | 2024-10-15 04:25:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33822700-c06a-3215-aa60-2f12315d3775 | -11.13354 | -44.17839 | 2024-10-15 04:25:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b1cb0ba-a7c2-363c-a750-b5029e3f74f5 | -11.13292 | -44.18255 | 2024-10-15 04:25:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa83c3ae-f43b-31ed-bfb5-83e758edd02f | -11.11831 | -44.46871 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f09efbcd-f403-3373-bd41-4ffcc979b5d1 | -11.11772 | -44.47275 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4fb053b-3cfb-35d8-9324-866ca699083e | -11.0686 | -43.88788 | 2024-10-15 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ad764b4-02c6-377f-8228-df220b189a80 | -11.0634 | -43.30284 | 2024-10-15 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3248961-d4c6-33cb-bf63-ac51ab77e732 | -10.9467 | -43.75808 | 2024-10-15 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f57dd3b2-7c3b-3150-96bd-c485c2e3928c | -10.84121 | -44.44629 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccfef664-f462-3d62-9cd7-a09defedf0ab | -13.26777 | -43.62175 | 2024-10-15 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e207f2a0-23fe-356d-8261-7529ef1530dc | -12.87449 | -44.60976 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 888bdbc3-7816-303e-8e2d-df3652fe0124 | -12.87388 | -44.61396 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d4208087-830e-3d68-8bf2-ba85af0d36c8 | -12.87028 | -44.61344 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 83e2f9dc-746b-3080-80ff-2e5910089e6e | -12.86669 | -44.61292 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0b3c700-f7c5-3c67-8044-86b92c312ce4 | -12.86309 | -44.6124 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d923bc40-8c2a-313b-930f-29d1090decf8 | -12.86248 | -44.61654 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1037f1d-2dc7-36c5-8cdf-6169e8e456d3 | -12.61158 | -44.78302 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3a2f555-9652-369c-b385-ed38da7f2e6e | -12.60803 | -44.78247 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d1d8114-2802-3c55-bf74-a32070f7ce30 | -12.57782 | -44.74028 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aff32a4-c01e-377e-a3e6-74de053d75e8 | -12.57723 | -44.74437 | 2024-10-15 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d4a71b2-ba2c-316b-b9e1-c1ee00660806 | -12.27179 | -44.5926 | 2024-10-15 04:25:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02d1e2d7-1a6c-3b5d-b685-b03f395ca48e | -12.26822 | -44.59207 | 2024-10-15 04:25:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee451262-afb4-3300-a543-b8accf67d600 | -5.97718 | -43.89298 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| edecfc84-b11a-3e9a-a0be-4e466ad2822e | -5.97659 | -43.89678 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8896dcb-f9b0-3f7c-942d-285808f61895 | -5.976 | -43.90055 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c5c52ca-9c0b-3738-84b0-6d703d8e37c7 | -5.97542 | -43.90433 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23fd40db-4030-329f-ad4c-cc355f0fb4d6 | -5.97489 | -43.88481 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27f93856-0ff6-3b15-8137-0233dfe440b2 | -5.97312 | -43.89626 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ebd388f2-7ab1-3ac1-86cf-866bcc33d716 | -5.85278 | -43.74609 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0da375a-d08b-373d-a71c-26b30fda3b9e | -6.40045 | -44.74211 | 2024-10-15 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6d3b654-40a9-3d68-aee7-771ffab1a0d1 | -6.26555 | -44.96671 | 2024-10-15 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f28c2d0-312b-3543-bb99-59e31766972a | -6.265 | -44.97027 | 2024-10-15 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faeaf80a-d7bf-398f-8cf2-44afe9ddeb9c | -6.26385 | -44.96662 | 2024-10-15 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccd94107-5bf4-3fe0-b8f6-576808aeae89 | -6.2633 | -44.97018 | 2024-10-15 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a1df5c1-be2a-3b93-a690-32856905dcb1 | -6.2355 | -44.1854 | 2024-10-15 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eada4f22-a131-31ea-b13d-bca36816b652 | -6.14318 | -44.91538 | 2024-10-15 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cedb2699-e7a9-3b70-8d4c-066484d27c15 | -6.13981 | -44.91488 | 2024-10-15 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dab994d-79bd-32d7-8f73-e1f7a6711bcf | -7.94868 | -44.52318 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 840aa381-be5e-3693-84ab-634fa7108259 | -7.9481 | -44.52697 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2475789-75e9-3201-81b6-62712d79ab28 | -7.94751 | -44.53075 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfe1c78a-d9a3-36de-bb9e-8b5aca0f42cd | -7.93778 | -44.52532 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9dcc514f-4ca1-31e0-b5a0-6c76a2f4c8e4 | -7.93434 | -44.52479 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab6dc0df-d16c-305a-b26e-24b7f6c709e0 | -7.93376 | -44.52855 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbef9bac-6f5d-3aca-a4e9-42309ee92892 | -7.89017 | -44.53728 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46377128-3562-3111-a52e-8593ab5f79f4 | -7.88959 | -44.54113 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 92803299-cd4e-3125-a698-babc3d81f026 | -7.86773 | -43.99471 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47513f7d-0d51-3adf-8aca-a9490c4c1007 | -7.84368 | -45.2454 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d00e12-3202-3656-ae62-b98cfab4281b | -7.82444 | -43.99614 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4594f589-f88c-3573-8ac0-9c3f0cd94abe | -7.7901 | -43.86679 | 2024-10-15 04:25:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feed0fb2-ad5e-365d-aa2a-76b43a36be71 | -7.77829 | -43.89722 | 2024-10-15 04:25:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f04d7408-59c1-3a92-815f-9df98b7b0c3c | -7.77048 | -44.54257 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ada17150-6fb3-313c-8632-5eed705ff0c6 | -7.7676 | -44.53841 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd5fa91c-8752-394a-8e7b-74291aceef98 | -7.76416 | -44.53789 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df5f396a-6b83-3401-8bb1-e5769cdee820 | -7.76129 | -44.53365 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aae240fb-d518-3f06-bbfc-1dac4569dcfa | -7.76072 | -44.53738 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64d2c4b8-110d-3f1f-a0c3-3651f85231df | -7.75672 | -44.54058 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69dd11b7-df33-36c7-ab19-7243f853de93 | -7.75492 | -44.8951 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c7ff5f5-30a2-3fb7-a1cc-0774e32d5de5 | -7.75328 | -44.54008 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b31b159-e56b-3d07-b122-3bd263cca227 | -7.75272 | -44.54381 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfa381db-d7cf-3d7d-b327-15c55c739370 | -7.75216 | -44.54752 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0383be14-0dc7-35d1-b49e-783ac1e60aee | -7.74872 | -44.54701 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66589796-0aed-39b0-9d1a-4acdb5a2b1bf | -7.74816 | -44.55071 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e6a7508-c18e-3aac-b8a6-9ad0a066db9d | -7.65371 | -44.66991 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc737982-097f-360d-be75-f17cfa5ab958 | -7.6503 | -44.66939 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c10833f-653b-3708-8e09-1e8b781918ad | -7.64688 | -44.66887 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1f8bddc-45b9-3938-86cc-1a364bbcc0f7 | -7.62811 | -44.6773 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37ec8f51-8504-3de3-9a05-833ba29a9e70 | -7.61905 | -44.69088 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5395d582-3955-3677-b01e-73f8e31df0fe | -7.61509 | -44.69393 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a408a55-c087-32be-a656-bc857b3b783b | -7.59515 | -44.6643 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9302f5a8-0371-3957-b6ef-83af1cd82e0d | -7.59119 | -44.64468 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0931ee5f-48d3-30de-be35-688f26582c6e | -7.58777 | -44.64415 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef5c7cf8-a926-3e99-96b0-ca3c3cbbfb62 | -7.57837 | -44.9577 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1267171f-65e2-37ca-ba54-56fa97c79be3 | -7.57498 | -44.95719 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69670164-1b3d-3c9f-ad7f-46b67c9f742c | -7.57442 | -44.96083 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 039ac30a-ca9e-3aba-a77c-0aaa70a9f64c | -7.56332 | -44.77994 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17f4238a-8bf4-3eda-9fbc-9784da4e0469 | -7.55934 | -44.78312 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b491188e-09f9-33e7-ae80-b0e08466093e | -7.47504 | -44.83355 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f5e907a-7d79-367c-abee-4b6a5a182c41 | -7.4749 | -44.83415 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d154243-82df-323f-a54a-9fc7439f3748 | -7.4632 | -44.09483 | 2024-10-15 04:25:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e3829e1-d153-3a0c-9045-0fe2fea69ce6 | -7.4626 | -44.0987 | 2024-10-15 04:25:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68fe4e37-a3b8-3039-a7d9-46eaccb212f5 | -7.33062 | -44.27821 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02b9cd9b-31ea-3395-9c35-4c710bd3407a | -7.33004 | -44.28198 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README49.md)
