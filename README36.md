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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fe8d7da-361a-344b-ad51-3f047278ac7e | -8.11649 | -54.85784 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3834f516-20fc-3899-8bb4-c1d697276e75 | -11.70912 | -43.45007 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e6aaec3-7843-3bf9-9891-9238ed48bef2 | -11.2627 | -43.54823 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49a89c3e-a7b1-3b90-a826-bda865b8ead1 | -14.11903 | -46.26036 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91270694-6201-316f-991b-cb89ec5395f3 | -11.43853 | -43.43116 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c4ef213-ed97-3859-9d7b-5e7b5802f1d2 | -9.80466 | -44.82391 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d5eb481-0f81-340a-a44f-773ae8b8fae0 | -10.19669 | -49.97717 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86c00129-1839-3f02-b531-b0e015723686 | -11.41279 | -43.48321 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e193d5b-b88a-3ae3-8104-8bdb1e68da97 | -10.68181 | -50.28276 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaa6df48-4d28-3a70-b9c2-367b1dc160d4 | -11.18856 | -45.12 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b579c90f-f959-3b54-83b7-d9723b89db58 | -10.29024 | -44.61706 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b0683f2-5ae2-36f5-8d5d-04b8e10480a4 | -13.33048 | -43.96053 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 963a4031-696f-3b1b-af3a-79762621b5c5 | -12.51405 | -43.08697 | 2026-09-30 04:34:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12324a18-be47-3265-b5cf-dec8eecf0b2a | -13.37172 | -46.83077 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7996a8dc-6a2d-3cd0-80a1-6857d3115903 | -11.34911 | -43.35413 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b17e68e-2e85-3eb4-8fb1-3940dd96a574 | -11.43504 | -43.43061 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a38f87b9-f99d-30cf-8f1e-cff24644feea | -11.3834 | -50.96848 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| befadeca-7156-3139-8967-3ebb50cfcf96 | -9.80132 | -44.82338 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc91bac7-17eb-33eb-af5f-14493c4dd784 | -11.37106 | -47.44595 | 2026-09-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 000deaf7-63b0-353b-bc72-f8db27c78a12 | -9.82014 | -48.20998 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad512d2d-ff21-35c7-ac42-0b7af95b6add | -11.35303 | -50.97419 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c229927a-e3da-3704-be89-0ba4e4e8afb0 | -11.25575 | -43.54714 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc5a8ff2-d502-3760-9fa9-9211d2e2d2d5 | -14.50409 | -48.2814 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b98733-cf07-3c68-a53f-44e6c34306a4 | -11.3785 | -51.02023 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21379cb6-14ee-32b1-a41e-ef76c37def22 | -17.71193 | -42.05186 | 2026-09-30 04:34:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8619f848-28ff-3a74-b4f4-6c8c4ae6c599 | -10.74852 | -50.50314 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb5e2b30-cd3b-37bb-8800-e5faf745982b | -14.1218 | -46.26447 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ade3a68d-b7a5-3642-a088-a1e9af2d5ff1 | -8.93671 | -49.7798 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3162da8f-2f4a-3bcd-af67-af3f5fad39dc | -11.09979 | -37.14765 | 2026-09-30 04:34:00 | NPP-375D | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5f921e5c-b6b1-3f28-8f22-cd0c6604735d | -11.79485 | -44.31532 | 2026-09-30 04:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7de3e2fc-6773-3bb5-aa03-68bfa1606647 | -12.43437 | -44.16985 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dff8e5e6-68f7-30b6-9ff2-5148f0f0a4c6 | -12.49907 | -44.97212 | 2026-09-30 04:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68fb4382-f36e-3946-a929-b7a17b2e8f1a | -13.69045 | -44.08214 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 360f9b45-f248-37f6-9dc1-31138f054fc9 | -13.41777 | -43.56603 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53284ae9-3dbb-3916-8276-31c4348174c9 | -11.85081 | -50.96433 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec38b4d8-d62b-3570-ac31-e7d74056e247 | -11.38608 | -43.37481 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59df335f-2c33-3963-a348-c6b75e9b7c74 | -15.44633 | -45.689 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3817253a-4f26-3ff9-8f9e-214ee63ddf20 | -15.20099 | -46.12888 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c68ce7-2eeb-3656-994d-f7765f61b8c2 | -12.7925 | -54.00581 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbc41d5a-21d7-3e9f-a123-e9045f0df7f5 | -14.32245 | -44.9033 | 2026-09-30 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e9d508f-b2a5-3a8b-b4b1-823d9d2d4d82 | -10.7218 | -44.42376 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 04980e90-8f15-3c35-ad02-77655717d787 | -8.29608 | -54.70683 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a00d48e5-f652-3a49-b0f2-66e32b2c9299 | -15.47316 | -46.12194 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c03f32b3-94ab-3d7d-a0bc-c5e9a2c8cdb1 | -11.39024 | -50.97726 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b19c14a5-c64e-3c33-858e-7db23fd54ab9 | -13.32705 | -43.93601 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2fc538b-a002-3647-8e1b-a2f3c10ab417 | -13.5408 | -49.16898 | 2026-09-30 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0406b4cc-367f-37c8-addc-1ca55eb74ebe | -13.18989 | -48.55135 | 2026-09-30 04:34:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9323079-9af2-3a2c-b436-6a4471454ba9 | -13.37286 | -46.82366 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee346c7f-68b6-3b92-afc4-3af75b537b6d | -11.40823 | -43.41845 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 08a3e054-130d-304e-9715-faad7e6e04d3 | -12.24462 | -50.24538 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7958bb6-f487-3349-b51d-a150d9cc0fdd | -10.28968 | -44.62062 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55bd9d4c-23b6-351d-93fe-df722eaaa4ed | -11.85887 | -50.96582 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1199af65-89ae-3b27-bed9-bcc677f30c68 | -11.83691 | -46.90398 | 2026-09-30 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5552f9a3-15ab-38bc-aaa1-441b705f8dae | -11.39419 | -43.46435 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7a410e7-d0ec-3d34-af31-75c6bf3d1ec3 | -11.39133 | -43.38769 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e42d4267-55b5-39f7-bf6a-ef1d7a37e17a | -16.35401 | -42.58614 | 2026-09-30 04:34:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14cacedd-7caf-3f70-ac91-58c7dde1bbf7 | -11.39088 | -50.97363 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e7c4febc-0cbb-3977-afc6-2fc57b9ac201 | -11.70211 | -43.44899 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e18650f7-7d9e-3bc0-a8e5-fc19f3898e6e | -9.77906 | -44.81259 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e9c274e-ad5f-3a9a-9071-2f6d41c53ab9 | -11.17 | -44.82137 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 39ee41a5-8d1f-35d1-9412-7210457746d8 | -9.087 | -49.88268 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4f910fc-0f83-321c-afb5-81bf4cd2ced0 | -10.08653 | -50.3149 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ecaa036e-e2c5-3b4c-badf-600c23cb7001 | -15.62958 | -48.19906 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39ab689a-3c81-335e-a713-1ec6e6de0f73 | -12.14483 | -47.20068 | 2026-09-30 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25b38f6d-fb16-3053-ba83-d4b028a84b5a | -10.83309 | -48.69701 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c0042d8-ee64-3dca-ac66-02e3e1fdeb79 | -16.29005 | -43.66685 | 2026-09-30 04:34:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03807ecb-1a0b-365f-b2ed-d97ecce4d0d3 | -9.86315 | -44.9673 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cffc67c7-8400-34c3-9089-26e1ab0e3deb | -11.2569 | -43.53942 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe287563-6504-3637-8213-c24137ea2a19 | -8.95328 | -49.79461 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80a06aff-8c69-3faa-b701-cfd54265d615 | -10.95117 | -47.27868 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33356caf-d67f-3990-b65d-555162534bbf | -10.28633 | -44.64207 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e76388b8-f6ff-3955-89fb-6abfb89834f3 | -10.71051 | -50.83923 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f2e0a8a-91eb-3265-966b-ecdd13c70e3c | -11.8264 | -50.43359 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67678c1c-f83e-3e34-97f1-0fdf26fab933 | -10.68402 | -50.29361 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 942dabfb-3e2c-38fa-b71e-4a2e850d1c07 | -12.95149 | -46.64445 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7512ab6e-3fd9-3db8-a4ee-948d1dab3aee | -11.18006 | -44.82297 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e8ec110-81a9-38ea-9859-9a9947c23eb1 | -9.93419 | -50.15663 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c9c3d5ca-b4ef-3725-bdc7-2efdb592d31e | -9.93024 | -50.15593 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c410b11-0c2f-3396-9c62-d0dbf8b880de | -11.25864 | -43.5278 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab257af1-1a18-3a19-b395-400ee55d82e4 | -14.12845 | -46.26558 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36a64067-e098-33fd-9f67-2f71984d3351 | -11.40293 | -43.45374 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a5b5896-5e6e-307f-87ca-d1a17a8a9990 | -11.39558 | -50.97074 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6583007a-2003-3270-8830-bcb6cc14000f | -13.53654 | -49.17239 | 2026-09-30 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38bc980a-fa05-3b60-9518-636f09f7c2b5 | -15.6703 | -39.92328 | 2026-09-30 04:34:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 28d96f5d-9a05-3409-94a5-962d08d33713 | -16.67445 | -41.85417 | 2026-09-30 04:34:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| d12381ef-bf76-322d-8978-0037ea8c1c72 | -15.66576 | -39.92265 | 2026-09-30 04:34:00 | NPP-375D | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5dc19a7d-7391-3a12-b694-aea1ce03178b | -11.81122 | -50.45146 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 160932cf-ee2a-3165-b807-6b7c86eb7782 | -14.90771 | -43.41374 | 2026-09-30 04:34:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6a509d4f-bda7-33b7-a617-0e0ea8a5a101 | -8.9376 | -49.79187 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 256f8949-5269-3c2d-b1d8-c37b755a8dde | -11.70561 | -43.44953 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eda3f0bf-e2da-383c-a0ea-c6c0df1af675 | -11.63213 | -43.53168 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52f9b5a9-9783-3651-83a0-56fadccb878b | -10.55219 | -50.86796 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da60ecc-c75e-3cbe-ae00-4d80d95b3720 | -10.771 | -47.71907 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 19968070-c0c2-3aa6-876d-c6efdbf964f4 | -9.80578 | -44.83855 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6f4d330-6517-318a-bfc9-d4de570fd694 | -11.40027 | -50.96786 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f411a3e0-b8ec-3321-b7fa-1839b7aa4533 | -10.70917 | -47.83467 | 2026-09-30 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44026304-4fd7-3134-b6a3-95ecc5a19ce0 | -11.39264 | -51.01152 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 735d0f7e-723d-3d13-82f2-7cd9a888c08a | -15.77719 | -46.0332 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44a86dd7-500a-3347-998d-c1a9f78205d4 | -11.83747 | -50.96925 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88ead9c6-63d9-395f-9acb-848809a9b978 | -11.40001 | -43.47324 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README37.md)
