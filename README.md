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
| 6d4cc613-424f-3212-bdde-4e0d3dbfdc4e | -21.520399 | -42.0397 | 2024-09-28 00:10:21 | METOP-B | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c6ebd0d-1a80-3343-a37c-11aede545bbf | -21.5089 | -42.033798 | 2024-09-28 00:10:21 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27840839-a0e3-3435-98ac-b12f2f4c7bc9 | -21.510599 | -42.041901 | 2024-09-28 00:10:21 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22859931-8138-3f27-9685-b2b6ec9d06fc | -21.512199 | -42.049999 | 2024-09-28 00:10:21 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4576bba-ca46-355f-89c4-a50e94f42d74 | -21.2906 | -41.916302 | 2024-09-28 00:10:24 | METOP-B | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e011c4e-fa8e-3173-a5ed-673f0fbd5786 | -21.2922 | -41.924198 | 2024-09-28 00:10:24 | METOP-B | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a06fa039-7ec7-3d00-8867-81857c04c7ef | -21.2939 | -41.932201 | 2024-09-28 00:10:24 | METOP-B | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88a564e7-a7cb-3e09-ae89-7121c03a482a | -22.346901 | -47.629299 | 2024-09-28 00:10:24 | METOP-B | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 24697bf6-241b-3476-bf45-eec0ddd58018 | -20.991899 | -41.2621 | 2024-09-28 00:10:27 | METOP-B | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbe0441d-8675-34b0-b837-b048dcd20aa8 | -21.130899 | -42.238602 | 2024-09-28 00:10:28 | METOP-B | EUGENÓPOLIS | MINAS GERAIS | Brasil | 3124906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0c81441-ddaa-3276-8afc-53faf4e98039 | -21.1325 | -42.2467 | 2024-09-28 00:10:28 | METOP-B | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df9ff537-5734-38ef-b0ff-f3ce58e174bb | -20.827299 | -41.605202 | 2024-09-28 00:10:30 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cceb2e7d-c6a0-3169-9725-fb48db323ff1 | -20.828899 | -41.6129 | 2024-09-28 00:10:30 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0718c4b-9ed2-3e39-b4b8-35efb9aec220 | -20.8305 | -41.620602 | 2024-09-28 00:10:30 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 06ff422b-662d-32a8-aa61-725d530eb306 | -20.817499 | -41.607399 | 2024-09-28 00:10:31 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11d59202-41f9-3f76-98c3-7ab6f83423b7 | -20.819099 | -41.615101 | 2024-09-28 00:10:31 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de81ea01-0251-376c-b720-35fb456e32dc | -20.8207 | -41.622799 | 2024-09-28 00:10:31 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ec33f48-fda7-3c35-8ab8-69a4d7f3601f | -20.788601 | -41.517399 | 2024-09-28 00:10:31 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 621c3347-fe95-3cf4-83b8-11816c24409b | -20.790199 | -41.525101 | 2024-09-28 00:10:31 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b196798-850b-373c-b551-05c0ea171d04 | -21.0294 | -42.6497 | 2024-09-28 00:10:31 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38c3a967-4a64-3905-86ae-34d6f8afe2ad | -21.031099 | -42.6581 | 2024-09-28 00:10:31 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67c8d5be-8b53-39ae-b5cf-e5450b33584d | -21.032801 | -42.6665 | 2024-09-28 00:10:31 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc24a666-cfde-3264-8c01-3afd00414da4 | -21.0116 | -42.662498 | 2024-09-28 00:10:31 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 967b1613-7196-3e91-88b3-0e11cc8c9d1e | -20.622801 | -41.213799 | 2024-09-28 00:10:32 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 106ca1eb-2c40-3cad-b1ae-22f13dc91e8a | -20.6243 | -41.221401 | 2024-09-28 00:10:32 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b31df93e-3489-3d0b-9684-653737a8ca24 | -20.888201 | -42.404499 | 2024-09-28 00:10:32 | METOP-B | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 546666cc-842a-3e41-8d0e-566e23e1e2ad | -20.889799 | -42.412701 | 2024-09-28 00:10:32 | METOP-B | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14d7bb8b-f2f9-3824-88e6-0d9c1aeccc51 | -20.613001 | -41.216099 | 2024-09-28 00:10:33 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 00c10668-eb5a-3071-ae5f-c64026d80755 | -20.6145 | -41.223701 | 2024-09-28 00:10:33 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3716640-7218-363c-ab34-a84f2277d2ac | -20.6161 | -41.231201 | 2024-09-28 00:10:33 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e1e7dbf-8acb-3fd5-a183-5fa3d717de32 | -20.617701 | -41.238701 | 2024-09-28 00:10:33 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b549729a-31ae-33cd-8bd6-5d6cc83b52d4 | -20.5418 | -40.926998 | 2024-09-28 00:10:33 | METOP-B | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1309158c-c216-3cec-9aa0-a5575cd0e14b | -20.6063 | -41.233501 | 2024-09-28 00:10:33 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aaffeec1-36ad-37ea-8ace-359ff9be1829 | -20.628401 | -41.3391 | 2024-09-28 00:10:33 | METOP-B | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea00027b-30a4-3ecf-af12-e3ebdcfe4766 | -20.629999 | -41.346699 | 2024-09-28 00:10:33 | METOP-B | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7437b5a2-0247-39b9-a527-ccccf2af990c | -20.5949 | -41.228199 | 2024-09-28 00:10:33 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dcd1da4e-ec62-324d-8630-2707eb4563ae | -20.531799 | -41.1721 | 2024-09-28 00:10:34 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15664353-8f76-3a00-89bb-00757aae891b | -20.5334 | -41.1796 | 2024-09-28 00:10:34 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b6c65c9c-2f13-338b-a200-f4cc2d6c83e9 | -21.837999 | -48.1903 | 2024-09-28 00:10:34 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04b075ee-7d42-30b3-b8f0-7bf3e0abb630 | -21.8832 | -48.466202 | 2024-09-28 00:10:34 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a3f3e35c-643b-38d4-8cb3-1182b89a269a | -20.5914 | -42.002102 | 2024-09-28 00:10:36 | METOP-B | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe8e43fb-55ee-3392-a079-709eff33b0ac | -20.593 | -42.009998 | 2024-09-28 00:10:36 | METOP-B | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 565f6064-5822-3254-a0f0-d5530148cf92 | -20.594601 | -42.017899 | 2024-09-28 00:10:36 | METOP-B | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05416718-8646-399f-80a3-6f96ddf9f288 | -20.813299 | -43.3106 | 2024-09-28 00:10:36 | METOP-B | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bb8166b-69ba-3830-94b2-b60ef6862af2 | -20.633499 | -42.258701 | 2024-09-28 00:10:36 | METOP-B | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6166d76a-5142-30ba-850c-1a5f91289597 | -21.281401 | -45.7882 | 2024-09-28 00:10:36 | METOP-B | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1b103cc-e455-3527-a93b-135f38062d24 | -21.2836 | -45.800598 | 2024-09-28 00:10:36 | METOP-B | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c798f97-741a-3260-8387-e468ca21e518 | -21.618099 | -47.714298 | 2024-09-28 00:10:36 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ecb8833a-6b02-3ecf-b4c9-95219ec6fb2f | -21.620899 | -47.730999 | 2024-09-28 00:10:36 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 898d32d4-9215-303c-b8b0-f5a0f9b809f2 | -21.623699 | -47.747601 | 2024-09-28 00:10:36 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e6cd12e8-c4e5-3f58-b85f-35262f9492b1 | -20.436501 | -41.996498 | 2024-09-28 00:10:38 | METOP-B | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 781766c3-245e-3cfa-aa82-22339a14489d | -20.2593 | -41.2911 | 2024-09-28 00:10:39 | METOP-B | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e22fe5d-d713-3e51-a682-2610c32dc54b | -20.2609 | -41.298599 | 2024-09-28 00:10:39 | METOP-B | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 326bcab2-fed1-3cb1-a08a-c7fc849204d4 | -20.287701 | -41.426601 | 2024-09-28 00:10:39 | METOP-B | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4981ea1c-14dd-32a8-9b6b-d08d854a2838 | -21.4039 | -47.7547 | 2024-09-28 00:10:40 | METOP-B | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc7b83d-303c-355a-887b-39616d3fcb35 | -21.406799 | -47.771301 | 2024-09-28 00:10:40 | METOP-B | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b967603d-c3e0-378a-b6ff-6602c25e5ca3 | -19.9559 | -40.540798 | 2024-09-28 00:10:41 | METOP-B | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64151203-fefa-3a0c-b2d2-144f1b8d0ed7 | -20.4482 | -42.911701 | 2024-09-28 00:10:41 | METOP-B | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79017de0-1b76-3662-a203-3f54dff17159 | -20.4499 | -42.9202 | 2024-09-28 00:10:41 | METOP-B | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 52c779c3-a3cb-3804-8675-2ec2af274122 | -21.1674 | -46.964199 | 2024-09-28 00:10:42 | METOP-B | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 73d00f43-8b3b-321c-bb67-37680962255e | -21.169901 | -46.978802 | 2024-09-28 00:10:42 | METOP-B | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1f76910-2938-3e68-a37a-3672e7ff4940 | -21.413799 | -47.7528 | 2024-09-28 00:10:42 | METOP-B | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec80b465-8470-35e6-bbd0-0d593c9f63db | -21.416599 | -47.769402 | 2024-09-28 00:10:42 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8bfadff1-e3af-3691-8cea-d5c104e1eba3 | -21.1108 | -46.244801 | 2024-09-28 00:10:43 | METOP-B | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ffd67b7-37d2-3b28-9ee9-23e180d57add | -21.113199 | -46.257999 | 2024-09-28 00:10:43 | METOP-B | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24b696c0-365d-3405-8435-dd3092981a42 | -19.615299 | -39.873299 | 2024-09-28 00:10:44 | METOP-B | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1f2cc20-04e5-3ade-a8e5-dd5e8654c5ef | -19.616899 | -39.8806 | 2024-09-28 00:10:44 | METOP-B | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8395b412-5b32-3c34-82a5-a57e6ac6bfa9 | -19.9307 | -41.7803 | 2024-09-28 00:10:46 | METOP-B | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc501608-a259-3727-a1f9-091642f173ad | -19.983101 | -42.132999 | 2024-09-28 00:10:46 | METOP-B | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0f7c107-415d-3fc4-a6f1-a7aed858bf12 | -20.180099 | -43.514599 | 2024-09-28 00:10:47 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0e11114d-1d97-36ef-956e-90ba97d3b417 | -20.181801 | -43.523602 | 2024-09-28 00:10:47 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14893366-8f2f-342f-bf4c-b477e4523789 | -19.995899 | -42.3951 | 2024-09-28 00:10:47 | METOP-B | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f98e782a-ab12-34a1-8805-5722bf99e302 | -19.997499 | -42.403099 | 2024-09-28 00:10:47 | METOP-B | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2b3ea44-b23b-3d56-801c-f25b30868d1b | -19.9196 | -42.122898 | 2024-09-28 00:10:47 | METOP-B | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8a5dacc-03ed-30bb-a5bf-fd5c4aabd9f6 | -19.9212 | -42.130699 | 2024-09-28 00:10:47 | METOP-B | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84f9628c-ba43-36cf-8670-3a3a03b12557 | -20.1136 | -43.4366 | 2024-09-28 00:10:48 | METOP-B | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11c57770-1429-3521-af26-35f8107c8487 | -20.1154 | -43.4454 | 2024-09-28 00:10:48 | METOP-B | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae15275f-bdcb-3ba0-9e4f-27a0f89aa4d5 | -19.873899 | -42.1497 | 2024-09-28 00:10:48 | METOP-B | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f6969f1-1152-3a35-ac5b-66b0e64135ea | -19.8755 | -42.157501 | 2024-09-28 00:10:48 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aae271b1-3b3d-31d7-b592-72ebc30b542a | -19.8641 | -42.152 | 2024-09-28 00:10:48 | METOP-B | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c628871e-8027-3cbe-aa58-7097d7f96299 | -19.8657 | -42.159801 | 2024-09-28 00:10:48 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a15a5896-939e-3dcb-9d8e-7511701b4370 | -19.8214 | -42.392899 | 2024-09-28 00:10:49 | METOP-B | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3663191d-1a61-383b-8616-c4cd1ba6221e | -19.823099 | -42.400902 | 2024-09-28 00:10:49 | METOP-B | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ab9785a-edfe-3138-83d2-8ae899c6ce95 | -20.506399 | -45.8689 | 2024-09-28 00:10:49 | METOP-B | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 028dc761-9557-36cb-88d3-81ee5a8259cd | -20.5795 | -46.27 | 2024-09-28 00:10:49 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a10b2683-f87b-33d9-a2a4-cf891c53051e | -20.5819 | -46.283001 | 2024-09-28 00:10:49 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 05c1c6a8-3695-38cf-ab80-ff2b08795328 | -20.4967 | -45.870899 | 2024-09-28 00:10:49 | METOP-B | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3c95be57-a4f3-337b-bfd3-de5eb1b3dff4 | -20.498899 | -45.882999 | 2024-09-28 00:10:49 | METOP-B | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ede7330e-6efb-3e1b-918c-5db2b8d7f423 | -20.5651 | -46.2463 | 2024-09-28 00:10:49 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 55397336-3591-326f-a435-896dcbe14dfb | -20.5674 | -46.259102 | 2024-09-28 00:10:49 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bef82800-027e-3d48-a4eb-1706c6b3e183 | -20.5697 | -46.271999 | 2024-09-28 00:10:49 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8f54e3cd-6b3a-3133-a00f-908dca99278d | -20.5721 | -46.285 | 2024-09-28 00:10:49 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc94dff-4622-3ce7-bff3-49e6dcf7fc65 | -20.5744 | -46.297901 | 2024-09-28 00:10:49 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 089aaef1-cb9b-3602-ad8a-e6898fd616b1 | -20.557699 | -46.261002 | 2024-09-28 00:10:50 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b0a9f865-d2a1-3948-96bf-ad35b0369696 | -19.5217 | -41.541698 | 2024-09-28 00:10:51 | METOP-B | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5436ecae-42c0-3376-bc91-56a349ea239b | -19.865499 | -43.165298 | 2024-09-28 00:10:51 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a277c7fa-a940-3f4f-8f2b-7b2cc78709b3 | -19.867201 | -43.173801 | 2024-09-28 00:10:51 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63339c07-4338-3374-8497-c040cd33e815 | -19.8689 | -43.1824 | 2024-09-28 00:10:51 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 277496c3-e35a-3e53-ae64-36f83a400909 | -20.1117 | -44.4702 | 2024-09-28 00:10:51 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c70ecb9-ddeb-3b5b-aef2-1a916b4eaf21 | -20.1136 | -44.480099 | 2024-09-28 00:10:51 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
