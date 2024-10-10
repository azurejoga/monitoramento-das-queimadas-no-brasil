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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b902e280-a0fa-3c33-a4be-3bbb2c610698 | -11.32951 | -50.96076 | 2024-10-10 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 3b61acdc-cc6c-3e98-abc1-62f6f1756275 | -11.21441 | -41.43446 | 2024-10-10 12:42:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 34.2 |
| ed83827e-0ac9-337d-9ede-9e33d657ebd9 | -14.90055 | -41.64911 | 2024-10-10 12:42:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 0e47da27-31b6-3341-8146-6b5ec79c4e55 | -14.86515 | -41.62526 | 2024-10-10 12:42:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 12076ba4-fe99-31f4-ad02-a0736bf2449b | -14.86393 | -41.61834 | 2024-10-10 12:42:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| b3a015d0-7a31-38ea-a829-7514a4f1b73f | -14.86158 | -41.63772 | 2024-10-10 12:42:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 92491754-d18d-3351-b292-6769c8d249a0 | -14.59192 | -41.84113 | 2024-10-10 12:42:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.9 |
| d6282ea9-276c-3793-b5f8-63c9e6af6f64 | -14.40729 | -42.16487 | 2024-10-10 12:42:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 107a48c0-bf15-3e03-b68f-45c30e622f66 | -14.39849 | -41.49987 | 2024-10-10 12:42:00 | TERRA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| a7ab903d-3251-37e6-9380-d6ad3fc7183a | -14.25624 | -42.1591 | 2024-10-10 12:42:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 32a9df7f-3d44-3d8f-b727-43577afdfb76 | -14.24019 | -40.94773 | 2024-10-10 12:42:00 | TERRA_M-T | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| b941b6e7-11ec-3468-ad08-38b3eedb5d3a | -14.04434 | -41.41049 | 2024-10-10 12:42:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| c952c455-3f37-381a-b49e-93ff40109e7a | -9.79679 | -42.624 | 2024-10-10 12:42:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 3210325e-344e-379a-a3ad-3066e3b15716 | -9.79327 | -42.61712 | 2024-10-10 12:42:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| d09b53db-5a05-3786-ad7e-8abe3f32399c | -9.79148 | -42.63032 | 2024-10-10 12:42:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 788de7cf-55a7-3f60-ace5-692ead06577c | -12.23137 | -42.02114 | 2024-10-10 12:42:00 | TERRA_M-T | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 3ee2c41e-0a60-371b-8f42-3a016076a505 | -11.39673 | -42.28327 | 2024-10-10 12:42:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 34.7 |
| ea4f89b5-ea00-3e80-9389-fca32aef8be2 | -11.39593 | -42.28896 | 2024-10-10 12:42:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 8f714052-c780-34b3-8bc8-70bc79561244 | -13.13545 | -42.99857 | 2024-10-10 12:42:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 740a9df3-2b83-3e86-a691-30c00a00725a | -13.01738 | -42.22134 | 2024-10-10 12:42:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| e94e8e99-009e-3424-bf04-46ace5cb8019 | -12.99217 | -42.23436 | 2024-10-10 12:42:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 4a5be67d-ff73-3bce-ab6d-d2b502191bc3 | -12.99022 | -42.25022 | 2024-10-10 12:42:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 2ddd493c-51af-3e84-a492-ec88cc6108d8 | -12.83996 | -42.36316 | 2024-10-10 12:42:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 376af329-83f4-359f-9cea-a6993b063108 | -12.83797 | -42.3787 | 2024-10-10 12:42:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 74dac0fe-7f81-3147-9dbe-119e33585614 | -12.83758 | -42.36891 | 2024-10-10 12:42:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 44.0 |
| f149eced-1663-3621-aaf4-602a822ea3ed | -12.76506 | -42.21213 | 2024-10-10 12:42:00 | TERRA_M-T | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 5212955f-f884-3059-8a00-49053016e7ef | -12.69341 | -42.33842 | 2024-10-10 12:42:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| c48e94c0-4b3e-3be6-8e96-0ae764d684bb | -12.59256 | -42.41379 | 2024-10-10 12:42:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 51.0 |
| ea771c1c-ac1c-3ecd-8924-c556efffcbea | -12.48168 | -42.02374 | 2024-10-10 12:42:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 7f5d3018-7e41-3e95-9e1e-bb870f3738d9 | -14.61718 | -43.14606 | 2024-10-10 12:42:00 | TERRA_M-T | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 4c5af66a-f63d-3df7-966f-0576e5038989 | -14.61537 | -43.16068 | 2024-10-10 12:42:00 | TERRA_M-T | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 29181baf-34f7-382d-ba5a-9f6598ee11dc | -14.53077 | -42.64518 | 2024-10-10 12:42:00 | TERRA_M-T | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 7db95cf9-bbdd-3989-97f2-97040bdbfb69 | -13.91587 | -43.16808 | 2024-10-10 12:42:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 41.5 |
| 088c75ef-d390-388a-ba69-277b9ddb959a | -14.03801 | -43.55976 | 2024-10-10 12:42:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f5820701-fcdb-3738-9ee6-5967e1817417 | -14.0363 | -43.57308 | 2024-10-10 12:42:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 20eafc2c-4682-3b24-b7e1-c060d1d0da00 | -10.46117 | -43.78307 | 2024-10-10 12:42:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 99ec8479-b069-3f87-84f2-2c2383ef5383 | -10.45979 | -43.78865 | 2024-10-10 12:42:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2765b3fb-f1c8-3759-9bad-a971ad28f358 | -9.93477 | -42.9262 | 2024-10-10 12:42:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| cff76047-0afa-3941-91e5-f401b4ebf637 | -9.92966 | -42.93192 | 2024-10-10 12:42:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 369b374e-87b2-3fcf-932b-911b6e60b7bb | -9.60149 | -42.79922 | 2024-10-10 12:42:00 | TERRA_M-T | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 8b2da140-6176-3e61-a58d-8b873ceded33 | -9.59096 | -42.79779 | 2024-10-10 12:42:00 | TERRA_M-T | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 27a43711-b31c-35b0-9b2d-2ca1905123ec | -9.94275 | -44.06052 | 2024-10-10 12:42:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f71b2e49-0953-395b-9f70-b21a4df72ddf | -11.79369 | -44.49628 | 2024-10-10 12:42:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 0dbe2b46-ae72-39ce-bdf5-e2358c6e81bc | -11.25833 | -44.23098 | 2024-10-10 12:42:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 1cee3b28-451b-3853-8fb4-b7da80a86b9d | -11.25685 | -44.242 | 2024-10-10 12:42:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 547.3 |
| d8f4a168-a6f0-323f-85f2-9ffba368bc61 | -11.25538 | -44.25301 | 2024-10-10 12:42:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 27070123-e693-359b-b5fc-1f6e67f4fd3f | -11.24708 | -44.24069 | 2024-10-10 12:42:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| a1d7fedd-d012-3dd1-a1c3-0d28e7c9b331 | -13.38287 | -44.67832 | 2024-10-10 12:42:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3ed924a8-5666-3089-8256-1dec645d7e00 | -12.29154 | -44.81989 | 2024-10-10 12:42:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cf4bd3ad-7d0a-3f92-99f0-1bb1a0f4e918 | -14.09581 | -44.9926 | 2024-10-10 12:42:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 566831d6-ed95-3a1c-b79c-dff9a4b5d3ac | -14.03964 | -44.01297 | 2024-10-10 12:42:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a035b5a5-b087-36cd-822f-b72eef43e5cc | -13.96003 | -44.55157 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b758fac1-fb62-379b-b237-d940f049cdcf | -13.92726 | -44.56412 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e66e5e28-95f2-3753-a45f-327068bb7da7 | -13.89083 | -44.68646 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 01adc8b0-fb80-324c-b87f-767e2d89f482 | -13.8795 | -44.69643 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 625342c4-fc97-3d66-84a4-a78925e734b0 | -13.83618 | -44.55767 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 9e36ef8b-31cf-3781-9653-7851c5e52004 | -13.83465 | -44.5691 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e72f7d92-d3fa-3da2-a124-8c1a1c1b7b92 | -13.83083 | -44.52213 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| b1ce193f-e97d-37a6-882f-7aa21842b0f6 | -13.82778 | -44.545 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 331ea93f-7f7a-359a-aa5a-f35b448f4e03 | -13.82626 | -44.5564 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 8634ee2f-be6b-3124-bb08-e9bfb3cebc4c | -13.81938 | -44.5323 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 6e672993-0c84-3ceb-ab5b-da8f86feed90 | -13.81635 | -44.55516 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1d26cbc2-cec0-3af0-8573-594c54c30a90 | -13.81335 | -44.57777 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c9ea1480-b7b4-3526-94d9-1fbfcf5eac1b | -13.80946 | -44.53091 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 69425d53-0b87-3c8b-a7bd-6fd292827360 | -13.80795 | -44.5424 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 841dfa20-1a72-392c-b6a3-369a2589e0cc | -13.80644 | -44.55386 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 91d5ad15-d534-3e47-9648-39144db6aaeb | -13.79653 | -44.55249 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 20375594-b180-333d-b99f-cb13bd323bc8 | -13.79503 | -44.5639 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 5b4b3b87-0528-30ca-91f5-11627683bca7 | -13.78813 | -44.53962 | 2024-10-10 12:42:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 55127c2e-139f-3129-a4f0-6f69ad290933 | -7.96252 | -54.77717 | 2024-10-10 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 4d7359f4-95c5-3ccb-a7c3-41dfdd8010a6 | -10.31054 | -53.71838 | 2024-10-10 12:42:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| c4508f01-8cf5-3f9c-a498-58ad34547917 | -10.31406 | -53.69712 | 2024-10-10 12:42:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 219.9 |
| d24f27f0-07ea-37e8-9688-cb55bb029f32 | -10.88494 | -53.74564 | 2024-10-10 12:42:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 37cdb199-b4dd-31c6-ae91-5f15ae913bf7 | -13.12217 | -51.66473 | 2024-10-10 12:42:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 4791d72f-3345-3627-90f4-75b66174e415 | -13.1243 | -51.65147 | 2024-10-10 12:42:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 743fee73-25a8-36d7-b81c-de2116b354bf | -13.14134 | -51.68148 | 2024-10-10 12:42:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| def9aec7-d2c9-3476-af6e-0f89e5e0fad7 | -9.31454 | -45.32993 | 2024-10-10 12:42:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 8e8751a3-f395-31dc-ac7b-2b28c67b3a3f | -9.31323 | -45.33918 | 2024-10-10 12:42:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d79b06d5-4cee-3689-8350-e206b0c5ed1e | -9.97561 | -45.47173 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bb1b2553-9723-38cb-83f2-30fe414e2d7d | -9.96653 | -45.47044 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 10b33da5-d31f-3b53-a367-d122d33353c5 | -9.83423 | -45.49671 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5090eff0-d015-3244-8496-229b39f0580f | -9.83291 | -45.50605 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 65075f82-a4c9-3877-b69b-b0281c5d4105 | -9.56866 | -44.42091 | 2024-10-10 12:42:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c25013d3-6a02-34a6-8f87-e47ea9ad9079 | -9.56726 | -44.43115 | 2024-10-10 12:42:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 8116c6cf-97ba-32df-aad3-343a981e7fed | -9.55919 | -44.41957 | 2024-10-10 12:42:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9c966ddd-b82f-3dfd-a83c-252f478df7e9 | -9.55779 | -44.42985 | 2024-10-10 12:42:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 66a5acd1-54a3-3935-934e-d697160d5e53 | -9.5564 | -44.44009 | 2024-10-10 12:42:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 80e666ce-3f2c-34a5-8c2c-68f73498ddef | -10.31439 | -45.4227 | 2024-10-10 12:42:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 029c5a93-749e-3450-9c81-bd91b35d2117 | -10.30529 | -45.42132 | 2024-10-10 12:42:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 779c0e2e-4aee-313b-ace5-d1a6f19ca009 | -12.30611 | -45.31966 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 83337ab5-82bc-3984-8470-6de7ac2c4087 | -12.30476 | -45.32962 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 6ad2c6be-cf85-3a90-ad31-9c2c072453aa | -12.2968 | -45.3183 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 016fc573-a635-3990-b577-4bbbb17d9a38 | -12.29544 | -45.32827 | 2024-10-10 12:42:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 580f1ef5-11fe-3388-a9be-09696c4b037f | -12.98717 | -46.25061 | 2024-10-10 12:42:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 084943ed-f1b5-39ea-93e6-ecefa074ceb0 | -12.98073 | -46.23062 | 2024-10-10 12:42:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a5bfbdf1-e381-343c-b6ce-45e88f754b48 | -12.97944 | -46.23989 | 2024-10-10 12:42:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6453d0c7-5be2-33ab-bd01-752ca3dc19ba | -11.33148 | -50.94804 | 2024-10-10 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e9265952-0ef9-30f2-9bc7-29f7137b3450 | -9.24659 | -46.44901 | 2024-10-10 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3ac16cdc-0f5e-3913-be25-b85511a4a321 | -9.23271 | -46.41968 | 2024-10-10 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9e0d5024-92be-3c41-87d7-ff54202cf7aa | -8.91112 | -46.02912 | 2024-10-10 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |


[Clique aqui para ver as próximas entradas](README149.md)
