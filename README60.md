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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aac5c50b-8572-30b5-8139-15c37ab05379 | -13.45633 | -43.7601 | 2025-10-18 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ac369ad-2aa2-364b-a763-642fb5e14313 | -13.04541 | -46.96394 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e575ba8-abbe-34d7-9be7-e97e42334da1 | -15.79197 | -43.65082 | 2025-10-18 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 754a2d01-8cf3-3d77-ae7f-bcdd02f09e97 | -11.36055 | -47.29188 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55d27656-a3c4-304c-aa19-da3bc890dcbe | -13.03089 | -46.94689 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2c279ff-6f43-390a-ae79-2dc00ad8a847 | -11.37199 | -45.27099 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17c40379-a0c8-31b9-a1b3-c774199c14b5 | -11.10976 | -47.655 | 2025-10-18 04:32:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f990e073-f4b1-3cd3-9bfe-97c134b897f7 | -13.92476 | -46.52967 | 2025-10-18 04:32:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89da7f22-493f-39a3-a77e-d6471f78c6e0 | -11.35782 | -44.30275 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4121599b-8976-3e67-ad65-34b5a58e8bb1 | -11.60957 | -44.08259 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 33d81a85-a8c5-31b7-886e-0bb5a90cbea2 | -10.96686 | -47.89203 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa71a1ff-5f23-33b6-9dc5-f81389ed9dc3 | -13.50935 | -47.99216 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cd578a2-b497-3d70-b2e7-63946f2e7339 | -17.95958 | -46.74452 | 2025-10-18 04:32:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f45b6c2-7b42-3fc2-8e04-ebd7685532f8 | -11.35513 | -45.25757 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69ec9054-95c8-357f-abb5-c740cb60d06d | -11.49387 | -44.2392 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 265eb6d2-17a7-38ae-928f-e6c079f65df3 | -13.84209 | -42.38815 | 2025-10-18 04:32:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 089be78a-ce5f-37ff-88c0-bd4f70e9adb8 | -14.01811 | -44.69355 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 894d390c-9665-3e07-b693-424e673584b7 | -11.36909 | -45.26659 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83d9d0e7-bf48-394e-a3af-cb22eeb0f1a4 | -12.16225 | -45.06048 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95457747-05c4-3766-ab0f-a3f241dd1b80 | -11.58701 | -44.05694 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 818239cf-c6b7-3345-8d27-3883a1161ac9 | -13.03704 | -46.95154 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b2cb656-378b-381e-9831-b5c701b43b0e | -13.48745 | -48.10869 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0799d94-dd59-3960-9458-6ac5e7e4e1d9 | -12.16925 | -45.08641 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a941717-0e76-35e9-bdda-32c3bda087d5 | -13.04413 | -48.19583 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1165918b-9c89-33ed-a0dc-7fe6c7752f3c | -13.96068 | -41.72233 | 2025-10-18 04:32:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6363505-9f99-32ea-9814-e6c65c005445 | -12.70096 | -48.6224 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 047bc0eb-5e51-30c1-8c29-1b56bbfedd0b | -16.34735 | -46.40509 | 2025-10-18 04:32:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e004d09-e9c7-3396-a971-01eac07fe757 | -13.03828 | -47.28518 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a97d18a5-c3ca-3331-bab2-be5834491aa8 | -14.47839 | -48.60757 | 2025-10-18 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 173883a1-5e38-36eb-8c70-cfb91e3e1239 | -18.39726 | -41.84834 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2ac431ee-82a8-3b05-ac28-58ed4272dd9a | -12.61255 | -52.82203 | 2025-10-18 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54f6f9cf-87af-3090-a1f4-b212be1e2ee1 | -14.28168 | -44.66061 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a7e2b39-4949-37b8-bed0-546520432bbf | -10.62948 | -48.01479 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a18a737-d2f0-3fd1-b702-7c21684c71d7 | -14.92302 | -46.71236 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7eff402-6579-3200-81d7-8d5e48947dd3 | -10.758 | -47.88735 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16dd07b9-0668-3966-bce4-8eae7ecf25ea | -11.36645 | -44.26945 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54bc7dfa-9033-3bed-a5e2-1a6550be1518 | -11.60828 | -44.09131 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 98a94f21-4db4-3e2a-823d-5e1c08112d38 | -11.49023 | -44.23865 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 867d552b-d449-37f8-b3d2-39be55b6bbef | -11.38444 | -44.29813 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a863aa9-b8a5-3c36-86a4-267c939ffafc | -15.96334 | -41.87307 | 2025-10-18 04:32:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2907a209-0a1f-3792-bf13-567646a3d8b9 | -17.84742 | -42.61836 | 2025-10-18 04:32:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 91a69804-1beb-33bb-9968-044558913890 | -10.97898 | -47.9231 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 885cf44b-662f-376e-918f-29fee845aee6 | -11.37482 | -44.28803 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10f3af72-fdcb-3dec-a1cd-dd4b956af880 | -11.15014 | -47.72295 | 2025-10-18 04:32:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10695d9c-1cff-39b1-bc4c-2fa32f122b1e | -11.20974 | -47.83435 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f08ad9cb-d905-322a-a8f6-f05d7a699387 | -12.98876 | -48.45673 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8fc4212-9030-371e-a8af-12f32576545a | -12.92178 | -48.59602 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43683e32-2b54-33eb-b959-4918dbf5fa73 | -16.21842 | -43.524 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ef0678c-b0a1-377a-b427-2913313836ea | -11.20032 | -47.82918 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51e5e832-9c8d-319f-837e-a572b263ee07 | -10.94481 | -47.56717 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8df003f-485f-3767-ab95-d67c6e97100d | -13.77756 | -48.23717 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b947b6f-25aa-3076-ae3e-5218c9c25156 | -16.2378 | -43.50787 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2c17330-42f2-36df-a64b-ddf5c8bf79b9 | -15.0795 | -48.45609 | 2025-10-18 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c80c043-3943-3ee0-9a4f-fe9095fd76a8 | -14.91394 | -46.72622 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3904c9d4-7e44-3184-b779-9bdf87a102e5 | -11.20754 | -47.82675 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 94460a85-63e9-396f-9960-61a543911568 | -13.53261 | -47.99598 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbd45128-2c0a-379e-9104-d1590d23a5a9 | -11.00626 | -47.90221 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be23e860-0bd7-3558-9e1c-708de7c02cc9 | -13.43433 | -47.92937 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17571879-0817-3639-8db1-6e89f9a40256 | -12.1769 | -45.08345 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec80bee7-09db-3ef7-9839-b8deb76dc483 | -15.78328 | -43.655 | 2025-10-18 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb1837ad-da95-31db-838b-5bb8414634b3 | -11.99436 | -47.15099 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5db455e-4245-3663-9055-64471b9fec55 | -12.48626 | -45.46671 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cc9faf5-0944-3f61-a346-b439ff235446 | -15.25504 | -43.24618 | 2025-10-18 04:32:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c1e8b063-d036-37ba-95f2-bda7b4d742eb | -11.51575 | -44.06626 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bbac9cf-c7fe-3a2a-92fc-01970f026977 | -11.49994 | -44.04607 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 170824a8-a95c-3476-ae24-0c25fef47169 | -14.0926 | -42.91621 | 2025-10-18 04:32:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66e9fd3e-55c9-3797-9db7-02625cdc83f1 | -15.0438 | -46.60443 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51f00860-9228-3314-a5bc-e7767189c0aa | -16.5364 | -43.67714 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c267627c-2012-3a89-bff0-d5cde63ecad0 | -12.15458 | -45.08817 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a8f38d2a-ddaf-34f0-848b-1e6496b3afb4 | -16.90718 | -53.02447 | 2025-10-18 04:32:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7921c491-f207-3597-9146-5f18c380a81a | -13.40986 | -47.97628 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f42a9d9c-703c-3894-9c74-b4b4cfd44941 | -17.86921 | -45.54427 | 2025-10-18 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b669ad9e-d067-3d12-a792-27149a538f28 | -13.43229 | -47.98304 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1775e03-4ad5-303f-892f-174bc6b423e8 | -13.72495 | -48.3745 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c88079c7-3918-3e65-807f-2b4d3f27b1b1 | -13.6195 | -43.96396 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac94c5e7-4d80-3467-a224-c77d4ebe53b3 | -10.98508 | -47.92775 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b7b46b-fb01-32b3-bde5-66e52d93c659 | -11.34841 | -44.24069 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82cc2a2b-b247-378f-96f6-3b5802a0f3de | -14.48613 | -44.60511 | 2025-10-18 04:32:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91ef9a10-8869-346f-9d9a-f893200f35e5 | -12.75116 | -48.63072 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14f42eb4-391b-349b-a0f0-c1f22d5b5a42 | -14.90977 | -52.40209 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e9822ec-f7ed-3893-9c49-54c54369870b | -13.76313 | -48.24208 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9267211a-4bf4-309c-a79d-f96eed4a1348 | -10.99734 | -47.91524 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b31caa7c-26b0-354a-9adc-7ebb5ada20eb | -12.16572 | -45.08592 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a3e4c94-4a6a-3c88-a65e-c40ee3848866 | -13.72162 | -48.37395 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49a9ec6d-3ea8-38b0-a6cc-dfb5d7ec1344 | -11.36812 | -44.18258 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e96700d-0710-39b6-9ad8-f9f00e8a7800 | -10.71969 | -48.14692 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43337319-562b-3e54-ac1d-8337e8f51f25 | -11.35342 | -44.2066 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da699ba9-9be4-32a4-9cf0-2c66251bdb48 | -10.99904 | -47.90465 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e755842-d6c4-30bb-a2a8-0bd965383afe | -12.93122 | -48.60131 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 044c21cd-2bc5-3939-9bf4-e1dadaba103d | -11.45695 | -44.21178 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 097d28c4-0fda-33f0-9414-ccc2b75ee778 | -14.90302 | -52.39599 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05fc49c1-a7eb-391e-b0bd-a484783d3d40 | -13.04193 | -48.18817 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6542ff1-65b1-322e-8c4d-41a31e01a695 | -12.92076 | -48.58112 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 502f73bf-94aa-3453-8d8a-da9e71ad0d61 | -12.39495 | -47.20413 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 439f2653-17a3-3405-b290-78b45a758206 | -14.12638 | -44.71283 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fdf365e-1478-31f0-a07e-b3cc7838a9b1 | -16.58373 | -45.67733 | 2025-10-18 04:32:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9947fc4-4b38-36e9-a63f-dd9418561d66 | -15.94495 | -45.21224 | 2025-10-18 04:32:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 275d7774-cd33-3d53-9122-4296b8854e74 | -11.49848 | -44.18301 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0d76947-d51a-3c9e-ae94-faf9b1272e58 | -12.63746 | -44.13783 | 2025-10-18 04:32:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56f599c7-cbfd-31c0-bfec-3cf00171be8a | -16.43518 | -43.73293 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README61.md)
