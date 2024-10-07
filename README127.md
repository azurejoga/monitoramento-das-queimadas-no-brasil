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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26440843-742f-3bd3-b1d7-9e9cf4aeefe5 | -21.59264 | -47.72641 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8a12d143-5a02-34ab-91fd-29f8f9e3feee | -21.59233 | -47.71415 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21d0dd04-3ec9-3edb-a38f-9c1281eafedc | -21.5922 | -47.73298 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ad1bce64-c5e3-3319-ba30-88ad0f55bd81 | -21.59179 | -47.95389 | 2024-10-07 05:21:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58212eaf-ae5c-3a86-8183-8c8c0062112b | -21.59178 | -47.72184 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b9f521e-ab10-3740-8db7-36f6d5083b89 | -21.59175 | -47.73987 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c4e95195-768d-3858-9b24-ee8fd28c1866 | -21.59132 | -47.72815 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d668dcd7-6794-3b34-9baa-c72a602cf6b5 | -21.5913 | -47.96122 | 2024-10-07 05:21:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0be01b01-5e07-3c3d-8c25-ef11ca34a616 | -21.59084 | -47.73485 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7c06089d-cb04-3b6e-9a78-e94b27f04a77 | -21.58968 | -47.94818 | 2024-10-07 05:21:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 646ad6ad-e9e8-313d-8fe0-d9b0d919b34c | -21.58913 | -47.9555 | 2024-10-07 05:21:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8277dc0-1350-3f20-97e1-bd6cc93709c2 | -21.58577 | -47.72041 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 52a49e5b-9884-3dfa-a85b-825a6b7f0d3d | -21.58538 | -47.72641 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 17097231-7bbd-3f7d-bfb0-2d98b34497e8 | -21.58501 | -47.7148 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cfa2dad1-7e07-3949-ad24-cccfc167a8de | -21.58496 | -47.73273 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 6568f543-6f81-31af-a462-8a2282c3dc7d | -21.58465 | -47.95345 | 2024-10-07 05:21:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d5ea75b-126d-3e67-b59c-c87d25f43e19 | -21.58451 | -47.73957 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 17b0b84f-564a-3160-adc6-14f1128feeb4 | -21.58449 | -47.72215 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55380ebd-426f-3c6a-a5ca-72951ef011eb | -21.58406 | -47.72812 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8049eaf7-f8b5-3ad5-a060-858bed62e1fc | -21.58359 | -47.73462 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 93889843-0452-352c-9ba1-358d67ddc337 | -21.5831 | -47.74144 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2c3027d1-d005-3eaa-975d-de52f722fc70 | -21.58261 | -47.74832 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 47820bd6-3c6c-35d8-97e1-9a8df62b30c9 | -21.57853 | -47.72012 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2559787f-5700-3eb2-a980-bc25f2134b17 | -21.57812 | -47.72636 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d88bc0df-e219-3595-9141-d8886093a2b0 | -21.57771 | -47.73254 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 476b933d-43f2-39b0-b972-668851722e04 | -21.57729 | -47.73896 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7945226-d9c0-350e-a908-8ce84705d874 | -21.57723 | -47.72202 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce9c5dc7-4399-34ce-a23a-8cc0a1ad5586 | -21.57684 | -47.74583 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| effe6332-ff61-3711-90a6-8af908258e57 | -21.5768 | -47.7281 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 970eb91e-0242-36bc-a264-af127e9c99b9 | -21.57639 | -47.75271 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41af2b99-c9e0-359b-9f35-9c754cefe87a | -21.57636 | -47.73426 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f02cdaa-1029-3096-b2cb-cae48442c6ab | -21.5759 | -47.74075 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ee7f368-c62f-3ba9-b70f-e7fd59df5e64 | -21.5754 | -47.74765 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b8d9de3-910f-356d-a269-ca1547320cbd | -21.57491 | -47.75456 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d91e850-c444-36c4-b60f-8c94060a682d | -21.57087 | -47.72615 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e07b6698-f38c-36c3-9094-20802da4e016 | -21.57048 | -47.73214 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aafc02ec-83ec-3ce3-8c9c-965aeaa90d1a | -21.57009 | -47.73805 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fafc92a0-d6dd-36af-bb95-af7f1c099358 | -21.57002 | -47.72118 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df3b62a4-c082-32cf-a2b2-f3407e06de39 | -21.56964 | -47.74491 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45b29b98-e3ca-33e5-a360-1a84a4ff4ffb | -21.56956 | -47.72771 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69f24a04-89cd-3245-a9c8-78fb63f80e77 | -21.56919 | -47.75192 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0790974-a418-3be2-81ea-0b64fa4586b2 | -21.56914 | -47.73369 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ceb31ebe-e621-31a2-9c8a-da6060f25f3d | -21.56872 | -47.75916 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ca1b07e-c746-389d-b15a-ced1ef8d0405 | -21.5687 | -47.73994 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c9dad79-e440-3785-901e-64a24ec52fad | -21.56824 | -47.76654 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5517f7f8-1995-3c7a-ac3a-416c0da71c3d | -21.56821 | -47.74678 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e857156b-d290-32f8-b4eb-4fa956264d4b | -21.5677 | -47.75391 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43b8fd0f-866a-3011-91c8-10038d43ffd5 | -21.32525 | -47.60986 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf96588e-4284-3acc-8977-081f1181adb9 | -21.32003 | -47.60485 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3f247ed-026e-39dd-9179-ef044b531b10 | -21.31959 | -47.61126 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 765aa0d1-f3b3-379f-9304-44f7380f6f6a | -21.3184 | -47.60387 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6ac2800-8979-316e-b8f0-e3b2a5dad71e | -21.31793 | -47.61018 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee5df1d2-7946-31fa-a258-723d1e01ae58 | -21.31268 | -47.60561 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aaa9777d-8214-3dcb-9493-d3ea798cae7c | -21.3123 | -47.61119 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32454eb4-2be5-3059-a86c-d846777b29ae | -21.31062 | -47.61032 | 2024-10-07 05:21:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d71838f-37ec-33bb-a033-1f5b0128d34a | -21.28202 | -47.39694 | 2024-10-07 05:21:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a875902-1ebb-3527-8441-66fab0d1e0f7 | -21.27466 | -47.39676 | 2024-10-07 05:21:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5a4879d-5b0d-3759-bdff-4194f156496d | -21.08696 | -47.23323 | 2024-10-07 05:21:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13cab2ba-7f3a-3b57-8109-ed78588cc73a | -21.08688 | -47.23129 | 2024-10-07 05:21:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58e53fdb-8ccf-3e9a-a476-197f2503d288 | -21.08655 | -47.23904 | 2024-10-07 05:21:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff679036-33b3-3562-88c6-8823c4a67472 | -21.08652 | -47.23685 | 2024-10-07 05:21:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 450575fb-f639-39cb-90a7-5a41ac5bf9f6 | -21.07956 | -47.23292 | 2024-10-07 05:21:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61581e91-ad66-3595-8092-9738c3311ac2 | -21.07913 | -47.23899 | 2024-10-07 05:21:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 521736f7-b9f0-3ccf-949c-ffcb8c9af1ca | -21.07162 | -47.24025 | 2024-10-07 05:21:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5302429-a778-3d74-8377-463328d60a2f | -21.06417 | -47.2407 | 2024-10-07 05:21:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd4585d6-1577-3303-a5f4-a523316b1d4c | -18.9098 | -48.19056 | 2024-10-07 05:21:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17c2dc6e-be0e-3c49-96c0-83491401a9b6 | -18.90926 | -48.19706 | 2024-10-07 05:21:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91858434-55fe-30e3-9cc8-9ab7dda46153 | -18.64375 | -48.66963 | 2024-10-07 05:21:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22059ffb-4df9-35b3-87e3-11678fe92152 | -18.64019 | -48.66831 | 2024-10-07 05:21:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fbb49f7-98ba-313e-9ebd-1d37f38023e6 | -18.63709 | -48.66889 | 2024-10-07 05:21:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 425a8d4e-c2e6-36a7-b75b-1159b3c1e20e | -20.75763 | -49.47612 | 2024-10-07 05:21:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c6fc39ef-ce2e-36d2-9568-db78ff31511f | -20.75718 | -49.48169 | 2024-10-07 05:21:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a833dbe3-4b90-31aa-8982-5a8f37cc9094 | -20.75678 | -49.48438 | 2024-10-07 05:21:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c3095c23-0c08-3c9e-a4cf-03f09ce21869 | -20.59107 | -48.50727 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 01b67123-b477-3e0e-9143-845d86f83624 | -20.59006 | -48.508 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 36a8647e-bc82-3b4c-9274-124441dd09ac | -20.58472 | -48.49985 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7e53060d-2f9d-3296-a0d3-7cccb5b20c22 | -20.58422 | -48.50662 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f05b3ff6-d9b9-3f8f-92da-deccf482042e | -20.58375 | -48.50067 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ad5bdfbb-f27f-3c5c-a4ce-e73e3c760571 | -20.58371 | -48.51346 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d4a540dc-8183-38ad-9ae7-caf7c91ffe86 | -20.58319 | -48.5075 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9b142e39-f74c-3719-b356-5e8d7137d776 | -20.57634 | -48.50686 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 066dc173-c062-3a41-a5c7-ae5e4d5f3bcd | -20.57582 | -48.51343 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1bd7f865-5aa6-3214-af51-146c59a2985f | -20.57532 | -48.51966 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dbc3e55e-3f54-3440-a846-10b5ef8a4fd0 | -20.569 | -48.5123 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 35a6250b-b631-3cbb-bbe6-0fa98d20e441 | -20.56849 | -48.51876 | 2024-10-07 05:21:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3b7eab7d-86dc-3be2-9ed2-82bd53873ed5 | -20.35059 | -48.80468 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7334e2e4-2591-361c-ae6e-6490dfb44415 | -20.35007 | -48.81089 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 8024faab-9e68-396b-bd94-d4c2a181c94f | -20.34385 | -48.80416 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 25.9 |
| aba24af5-0ee3-3468-8704-494ceff502a0 | -20.34334 | -48.81034 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| b7918c78-b79d-3a0e-a2b3-37bf480c222c | -20.34284 | -48.81642 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 5a159813-a3ae-3eac-a584-2d1db483fc71 | -20.18951 | -48.7272 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fd046c5-5ae3-3751-9558-4f7a50a4e29e | -20.18545 | -48.72627 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c1863de-e24c-3810-a850-be535009784c | -20.18495 | -48.73259 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81f7c306-fc93-3b9a-9bd7-aff69aa8cdd9 | -20.18278 | -48.72646 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d36c8037-98f4-3279-ad95-e7eabd21e0f2 | -20.18223 | -48.73281 | 2024-10-07 05:21:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7c887b19-473a-3c80-8272-dac3528bd425 | -23.03648 | -49.8466 | 2024-10-07 05:21:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1e90489c-ffaf-3143-b422-ef812389d52f | -23.03605 | -49.85237 | 2024-10-07 05:21:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2dbfbb32-5198-3650-bcce-41905f4976fd | -19.16536 | -50.63482 | 2024-10-07 05:21:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1613bdd8-a298-344e-be4b-064630328f6f | -19.16454 | -50.64371 | 2024-10-07 05:21:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5889fcd8-600b-3f40-8c2e-5e530cc6fba5 | -19.15942 | -50.63395 | 2024-10-07 05:21:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README128.md)
