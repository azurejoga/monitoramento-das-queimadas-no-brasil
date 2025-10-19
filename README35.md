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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 101aa0f9-094e-31d5-8fe7-2beefc3fd602 | -15.79297 | -43.25173 | 2025-10-19 04:14:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4bc33166-7a89-3eb9-bf5e-faf6c9a88765 | -14.45487 | -45.56006 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbb4fa57-32bf-3642-b64f-163ea240c341 | -13.90514 | -45.53601 | 2025-10-19 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2698c351-5499-342e-9189-cf07f6974a66 | -14.46822 | -45.5864 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b76ee3d-3da4-3d41-8806-c012919e9417 | -15.26583 | -43.58253 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58c6c4b3-f2b1-3acb-9f2e-ea9b3d718115 | -17.08518 | -41.69456 | 2025-10-19 04:14:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 805169ba-4d5d-3d13-8cb8-acfd37633288 | -19.27378 | -43.72083 | 2025-10-19 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08794e26-f138-3b43-b12c-70dce52a5fcc | -14.56401 | -43.19108 | 2025-10-19 04:14:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96bd4ca7-18bc-3504-952d-86c9c02cabb6 | -15.23741 | -43.33915 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e8b597c-4b32-38ca-892f-e4c3ab0d1444 | -16.75854 | -42.76477 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7aabd1e4-8eff-39dd-aa0d-33691a13f9bb | -16.76359 | -42.77707 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 075f428f-c35d-37e2-bad1-2fbf6ae048ef | -16.82631 | -41.79672 | 2025-10-19 04:14:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 09f2edbd-5c7e-3c7e-999d-330f656110b4 | -15.52778 | -43.83721 | 2025-10-19 04:14:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2bf092a3-955d-3b41-861f-3878f35125a3 | -15.98148 | -41.20854 | 2025-10-19 04:14:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 33b5a5f5-b09d-36b4-8c30-e7c2388be6dc | -13.92677 | -45.60739 | 2025-10-19 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c3b2546-0b55-3a3f-85c0-04a1d519fa94 | -15.52835 | -43.83362 | 2025-10-19 04:14:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30f8bbb2-8012-3294-820a-94229019ec73 | -15.70533 | -43.48425 | 2025-10-19 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81ec8c27-771e-3e32-b74e-5aad39f5c796 | -15.7031 | -41.2635 | 2025-10-19 04:14:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2071b64a-1824-346d-a917-d625fd890d0e | -15.50993 | -41.54255 | 2025-10-19 04:14:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 75bd75b2-dfb0-31ac-ae8d-63279c1ad661 | -16.7765 | -42.76023 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a59c424b-b364-3e9f-a8b4-528e2234f6c7 | -16.14768 | -41.15288 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| d3f2746a-84e5-3e14-9591-658e37b0daf1 | -15.4719 | -45.93726 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1d9820f-be4d-37a8-9552-ab3c8575ec0d | -14.4814 | -45.59267 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76293a3d-6a89-3647-9dca-58efc1971cc1 | -16.75685 | -42.77594 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| a6ea4fde-ad74-32e5-9c15-7e231a7d207c | -16.7877 | -42.82278 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77c80051-f142-32af-8172-381b6b768100 | -16.76639 | -42.78136 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 1e9c564d-6186-370f-b398-8a7b4a3a98b8 | -15.45091 | -45.91309 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eee39e4b-52c2-3743-8e3a-06b993576740 | -16.26446 | -42.48109 | 2025-10-19 04:14:00 | NPP-375D | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00f2bbb8-4e23-34cb-8998-96915bc8388e | -16.78381 | -42.75758 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ca1b5b88-081b-370b-b17f-6a3b68d117eb | -16.82228 | -41.80002 | 2025-10-19 04:14:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| deebd24c-cca7-3153-9d3a-670cb2fe16ad | -13.93307 | -45.61251 | 2025-10-19 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93685504-d58a-3417-989e-ee741fe12e00 | -15.52419 | -45.34466 | 2025-10-19 04:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6600b025-7b35-365f-bf49-39741b37c471 | -16.75517 | -42.7642 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1452947-dde7-3b01-9b52-7fc4949576a3 | -15.09492 | -40.16964 | 2025-10-19 04:14:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df72f295-9195-3f95-8441-b9abb8fd6fd1 | -16.75011 | -42.77482 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d6a4381-9c08-3a65-a1d3-ee640e3f26f4 | -16.75348 | -42.77538 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41755c42-ed1f-3ebb-a86c-fdfade3997d6 | -15.80117 | -43.65096 | 2025-10-19 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 691f6e74-fb64-36db-8e46-2e6e5dedbdf3 | -16.14415 | -41.15228 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 131d8fe4-5050-3512-8a72-a96a74662f88 | -16.78865 | -41.46534 | 2025-10-19 04:14:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a2ebf90c-8cd8-3b58-b519-4bdb6115fa55 | -15.79784 | -43.6504 | 2025-10-19 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f9e5975-782a-387d-8d92-dfb108f43ebc | -14.55833 | -43.5086 | 2025-10-19 04:14:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aed8ec63-8681-3c24-85f9-51129c6bd274 | -15.53182 | -42.83996 | 2025-10-19 04:14:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 363b9777-b8c0-3a68-a85f-8d42df2f69f1 | -15.5311 | -43.83777 | 2025-10-19 04:14:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 147969be-f704-3f1b-83fc-4ae6f185a326 | -14.02815 | -47.08729 | 2025-10-19 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a68c339-3335-3a22-9bb6-942edc2d6672 | -15.78842 | -43.64513 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78536f86-52d8-3bae-aea4-68a2c5f05639 | -16.74619 | -42.77796 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d64303b9-42c3-3964-a9a4-3d05ca32822a | -15.7863 | -43.25063 | 2025-10-19 04:14:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fccda91-b40b-345e-8828-9a59dfd36a2a | -15.46712 | -45.94449 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3c77ec79-a16a-3b0a-adb6-e5c680ad40c6 | -16.74338 | -42.77369 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bde1a5da-0a11-3a1d-837e-2621c6ce669f | -16.82575 | -41.80051 | 2025-10-19 04:14:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| edde2ea5-9a43-331d-9cea-15bb6d1fd4d3 | -14.90493 | -46.72773 | 2025-10-19 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f45e7c8f-67d4-3730-a24e-bea52436b8b2 | -16.77538 | -42.76765 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 60383ced-58ac-3cbc-94e8-32bf5358a68b | -15.78215 | -41.33967 | 2025-10-19 04:14:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d923d3c3-d202-3a59-813b-3c8c376a4363 | -15.7984 | -43.64681 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d006f59d-b02c-3f13-9259-5e2a035656f5 | -15.98088 | -41.21258 | 2025-10-19 04:14:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae2fe508-7ccd-3427-a342-1dadad122979 | -15.51253 | -41.67709 | 2025-10-19 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aa40741c-2be7-3881-952c-9aa787a23441 | -14.45355 | -45.56784 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6fd25cb2-61fa-3837-b4cd-19078fea4070 | -15.77574 | -41.33457 | 2025-10-19 04:14:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6723bbe1-a470-3a32-9f7f-62ad67f8ad17 | -14.74767 | -42.46027 | 2025-10-19 04:14:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0aa9532e-9eb7-33a9-b2bd-a295a9172c07 | -16.75742 | -42.7722 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 77927823-0136-3e65-8f04-a599bb2bc8b3 | -14.30031 | -44.01609 | 2025-10-19 04:14:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f27b5ecd-c5d3-38d8-b817-a65776990a98 | -15.78519 | -43.25779 | 2025-10-19 04:14:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41e2a9e9-c996-34e1-b4a6-b7a2a30b4db9 | -15.01193 | -40.46362 | 2025-10-19 04:14:00 | NPP-375D | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 9498ff40-6d0e-3556-8345-33f2f9f77194 | -16.74844 | -42.76306 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7b76ea9b-d273-347d-a19e-2b65e490b7f8 | -16.14826 | -41.14884 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ecd7d0eb-8239-310a-b5b8-e312fcbb258b | -15.52286 | -41.67881 | 2025-10-19 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8e17e08f-76bf-33b2-a548-2ad0120372bb | -15.18748 | -43.56955 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9af39682-ae15-369c-9fe2-f88e06c2ebfc | -15.90285 | -41.57125 | 2025-10-19 04:14:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fe18a051-79a5-34f5-963e-0a6aaa88af8d | -15.51541 | -41.6815 | 2025-10-19 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1275eaad-d940-3ae9-96d5-fce6d0845533 | -14.18377 | -44.79586 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15d3fc29-79f1-3532-ab42-22ea62ee75e2 | -16.20558 | -42.71057 | 2025-10-19 04:14:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bf1e033-c5dd-33ac-a233-0be088cb8121 | -13.7945 | -47.11492 | 2025-10-19 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af6039fc-ceed-30a8-b913-9a06ae2e5de6 | -16.79056 | -42.75862 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6c020054-dc6b-3f42-935a-1c3a7428f55a | -17.40499 | -40.16301 | 2025-10-19 04:14:00 | NPP-375D | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b78702c0-4e1e-3382-8dc9-ba4829214ff1 | -15.19081 | -43.5701 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5febce1c-2c36-303e-a747-5cb909e4eb7b | -15.3641 | -42.99867 | 2025-10-19 04:14:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 878c1850-d9ca-309e-903a-d1b660319477 | -16.77594 | -42.76394 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d22fe791-54f4-37dd-a4b2-4399c6d35fa8 | -15.5314 | -45.69464 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79b87a5c-8dd1-30aa-9786-2339a1258ddf | -16.80755 | -41.00757 | 2025-10-19 04:14:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 24531ab3-3c3e-3e6f-bbca-0bfadc6b8025 | -13.92959 | -45.61191 | 2025-10-19 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f09dc9bb-875f-36f6-a28d-505bb981992d | -14.45981 | -45.5729 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad2e4a11-9d4c-3725-97f3-70d2cdb38562 | -15.77865 | -41.33913 | 2025-10-19 04:14:00 | NPP-375D | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 098d618b-25ff-3126-8f74-1541530739e8 | -16.79487 | -40.94169 | 2025-10-19 04:14:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11832c00-608c-33bc-964a-bd1c86fd3787 | -16.76302 | -42.7808 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 7a43794c-50e7-3250-ba47-6cbc195b644d | -16.79 | -42.76233 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a281bf47-19a1-3fcb-8031-a6eaf5abed45 | -15.51655 | -41.67381 | 2025-10-19 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| caf867f4-57f5-3296-9567-6a353c68ce1a | -14.30365 | -44.01665 | 2025-10-19 04:14:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f78c4c-aa9a-359e-8b29-f44102cee941 | -14.73008 | -42.31989 | 2025-10-19 04:14:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4f92e3d6-c5d9-32c7-aff2-922dec7ad1bb | -16.78268 | -42.76501 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bad36996-fa2e-3cac-9e9b-60ced25806aa | -15.44744 | -45.91244 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d2bda8e-f0da-39a9-9bce-0daa3adfb356 | -14.55168 | -43.50748 | 2025-10-19 04:14:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ca7954f-e876-3d33-b0be-c126c1884b22 | -16.97742 | -41.1584 | 2025-10-19 04:14:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c2b6982d-b6da-3bff-a9ea-61ff61318301 | -15.57178 | -42.60364 | 2025-10-19 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16935d25-1d05-35b9-b3e9-f9e6f9315901 | -16.78662 | -42.76182 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bfa0988f-44f6-3d95-aecb-a593dd4dc842 | -16.74675 | -42.77426 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 051600c7-d305-396a-a097-585e3a38a0eb | -14.45832 | -45.56065 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d96a9b73-e610-3a66-b85c-920a0e9b94b7 | -15.19137 | -43.56652 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37e15cb5-e387-34bc-b67d-8e2cedf1d5d0 | -15.23684 | -43.34274 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b9e79ae-4af9-306f-818e-524248500777 | -15.5301 | -45.70232 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2608a15a-63fd-352d-9274-35333c6a7f88 | -16.81465 | -42.82711 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README36.md)
