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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abf349ad-6ed1-3de8-83d3-aa5a36265411 | -1.7589 | -47.188599 | 2024-10-06 00:50:19 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b02ae375-2293-38c3-815b-466bb93903b9 | -1.7464 | -47.178902 | 2024-10-06 00:50:19 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7cda943-347f-3ffb-bf8c-69f6777e9db0 | -1.7491 | -47.1908 | 2024-10-06 00:50:19 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b88824a0-d8f4-31e0-9930-cde209f2efcf | -3.0371 | -53.020802 | 2024-10-06 00:50:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9959f099-fe27-3a39-81fb-aead08292c2f | -3.0386 | -53.027599 | 2024-10-06 00:50:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d1b935-d2bc-3f22-89c4-81e2daeeae85 | -3.0401 | -53.034401 | 2024-10-06 00:50:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaa8cef6-c65b-39c3-940c-9dfd81498bd5 | -3.0273 | -53.022999 | 2024-10-06 00:50:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a22a092f-f691-3374-9567-d26c05746315 | -3.0288 | -53.0298 | 2024-10-06 00:50:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b63bd6c6-15a1-3819-af5b-f0a561f004c8 | -3.0303 | -53.036598 | 2024-10-06 00:50:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6283573f-8161-3532-b544-2ecc9d087b70 | -2.9552 | -53.7099 | 2024-10-06 00:50:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96776cd1-9fbb-3127-ba46-c58628ffff48 | -2.9568 | -53.7169 | 2024-10-06 00:50:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc51b118-527c-309a-9d01-d9b339423bfe | -2.9392 | -53.684399 | 2024-10-06 00:50:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 973aa197-49d0-3f5e-a4b3-36cce36f68fa | -2.9407 | -53.691299 | 2024-10-06 00:50:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7218c0d2-ab57-3b17-ac99-479af25656f1 | -2.9423 | -53.698299 | 2024-10-06 00:50:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d2195d-da9d-36d4-83c3-b283cc8b99b6 | -2.8441 | -53.307598 | 2024-10-06 00:50:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cffeff25-b796-3312-b587-27647d222df0 | -2.7787 | -53.199902 | 2024-10-06 00:50:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b15eaae-50d6-3fa9-a614-3dd755c4c85f | -2.7674 | -53.195202 | 2024-10-06 00:50:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 050fe0f1-9072-3b31-be6a-66cb15d06c1c | -2.7689 | -53.202099 | 2024-10-06 00:50:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9940f283-c218-3e63-82ed-5ae1476fa60b | -2.7704 | -53.2089 | 2024-10-06 00:50:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdbd2b82-4cea-39f6-a8ac-6644bb4e1f42 | -3.0681 | -54.764301 | 2024-10-06 00:50:26 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea7f7831-9fef-35b2-9958-5bd407e7e7ab | -2.1308 | -50.974098 | 2024-10-06 00:50:27 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a7eaa58-4d7a-3c17-91a2-e0de92611321 | -2.1325 | -50.981499 | 2024-10-06 00:50:27 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48289d4f-e1af-3a9e-8684-e64b9c383947 | -2.8096 | -54.575001 | 2024-10-06 00:50:29 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39c3752f-d1dc-3db9-8813-ab30fa366b74 | -2.7431 | -54.921398 | 2024-10-06 00:50:32 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03e4f01e-6ae2-3214-b96b-1264913bca93 | -1.8314 | -50.9711 | 2024-10-06 00:50:32 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9b2eba0-d340-3fae-97cd-b73e241c16b1 | -1.8199 | -50.9659 | 2024-10-06 00:50:32 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff26288-530f-31fd-a736-4fe096af94bf | -1.8216 | -50.973301 | 2024-10-06 00:50:32 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aecdc62-1f10-3405-bb6f-4ecebaaeb55a | -1.7514 | -53.990398 | 2024-10-06 00:50:44 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44699f52-2cc5-3865-8303-75e8fa168c76 | -1.753 | -53.997398 | 2024-10-06 00:50:44 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe7d9d14-b6d1-3453-a29f-bd8dd488b464 | -1.5524 | -54.753201 | 2024-10-06 00:50:50 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12dc3f5e-c3f8-3683-9582-92dbb6951371 | -1.554 | -54.760399 | 2024-10-06 00:50:50 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f71248f5-b123-3dac-b48a-21a3ab460943 | -1.5556 | -54.767601 | 2024-10-06 00:50:50 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e08d2af2-57ea-3a31-ba53-e8265e06f4d5 | -1.5442 | -54.7626 | 2024-10-06 00:50:51 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eee0b8f-d78a-3d58-b6a0-092e16211aea | -1.4623 | -54.948101 | 2024-10-06 00:50:53 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f579119-004b-3398-adf6-a1efddf20f24 | -1.4639 | -54.955399 | 2024-10-06 00:50:53 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77a1e6bf-c409-3b13-a88b-647d59989598 | -13.66822 | -51.19568 | 2024-10-06 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7558cb7b-b86b-340c-92e4-9924c68a4517 | -12.77571 | -50.53749 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 90a9510c-e17e-3114-922f-59b087657383 | -12.76473 | -50.53891 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 89c1cb32-59cf-3bf2-84e6-c22bfcf617a7 | -12.76296 | -50.52465 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 2b947c65-335a-3a0a-8499-30e077e4c895 | -12.75551 | -50.55463 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b180b2e2-3194-321c-8d57-b6e09ae29c0a | -12.75375 | -50.54034 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ae92fdc9-c0a7-32cb-aa34-44dce1ffb344 | -12.75199 | -50.52608 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a63d9921-bdae-3b21-8ecb-ed1d5b1b3f04 | -12.661 | -54.71645 | 2024-10-06 00:52:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 780b510a-029d-3593-99bd-ab2aa7a66fff | -12.6603 | -54.0308 | 2024-10-06 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| f2e0a043-5095-300f-9760-e4ddf1f10d79 | -12.65073 | -54.05373 | 2024-10-06 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 871ce504-94e7-33d1-895e-540cb7e5b57a | -12.64582 | -54.03251 | 2024-10-06 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| a3bdd402-ec44-322e-8343-2d46e0888440 | -12.51198 | -47.58236 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 978932e6-2fea-3fa9-b168-1dc397d56fcc | -12.50286 | -47.58363 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 4b97853d-149d-3852-a323-74565c5eee54 | -12.50157 | -47.57406 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| f1024a04-86b2-3148-ba43-5f88a6d4a3ee | -12.49246 | -47.57535 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 11542573-5512-3489-b8e7-fa11dc901723 | -12.49117 | -47.56577 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3398ab9b-d493-34cb-8300-bac57bb3ec19 | -12.48988 | -47.55621 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16afe792-20b6-3047-a198-478bf3064a62 | -12.48077 | -47.5575 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9bc1cc5c-e439-33e7-b62f-2d17afefff4e | -12.47039 | -47.54925 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4773edba-f146-39a7-9537-f8d17ab7059f | -12.46129 | -47.55053 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4d09fad6-9e83-3583-bb6f-bca42c2733c4 | -12.46001 | -47.54096 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe0eed6d-f822-3f50-a69f-5f28ed061e3e | -12.45874 | -47.53146 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 20509e32-985a-3f31-bff5-6ea347cdd12f | -12.45746 | -47.52196 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 475dd9aa-6e72-3a5a-b9ba-8e2b14cbaea0 | -12.44965 | -47.53276 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 711699f0-b3fe-307f-9c5b-a9a7dc46dc8b | -12.44837 | -47.52326 | 2024-10-06 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f4a14f91-71b7-3d5d-9a8d-77533c473eb6 | -12.42105 | -47.04921 | 2024-10-06 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c6cd3615-68de-36c9-a691-c83b4e00fc31 | -11.93446 | -50.10334 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bdb7804c-89cf-393f-aa6b-02970538272d | -11.92885 | -50.11048 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fcb42892-fa27-313b-95b0-fe5be39d7603 | -11.88689 | -50.11605 | 2024-10-06 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d8067c50-1b1c-3450-9d1b-f7bae020558a | -11.7322 | -47.80984 | 2024-10-06 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d654038c-77f2-35e1-9214-886585c5a9bd | -11.72306 | -47.81111 | 2024-10-06 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 241db279-9486-318e-8640-1ca1b1f053b0 | -11.72179 | -47.8015 | 2024-10-06 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa1e3dd3-38f2-382a-9b82-8f6e29971109 | -11.71941 | -47.71364 | 2024-10-06 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 57ff8c0d-4fc3-3717-8800-b6cd913d6a26 | -11.71813 | -47.70398 | 2024-10-06 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fde85964-002c-3d4f-bc46-011638469931 | -11.7145 | -47.80834 | 2024-10-06 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c73a9e9c-87fb-3d03-a75f-1b10c8263192 | -11.64217 | -54.51871 | 2024-10-06 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9230524e-c003-3eac-85af-40b358f8b541 | -11.64213 | -54.52388 | 2024-10-06 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 1717ec7d-bb4e-3bf4-99bb-64aa67c6cad6 | -11.62601 | -48.3273 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eabf3a49-d5b0-3838-9e38-fbd39bf4a275 | -11.52635 | -53.44084 | 2024-10-06 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 411279f7-098f-3804-9580-4e850550fe0f | -11.52043 | -53.43616 | 2024-10-06 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e99e772d-aefb-3ef1-b7c8-f461aef86d77 | -11.368 | -47.22028 | 2024-10-06 00:52:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3985f548-67cd-3295-b198-056106aeefe6 | -11.3186 | -46.79152 | 2024-10-06 00:52:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9aa42bb3-4cd0-3180-a461-386a7ca365da | -11.30974 | -46.79281 | 2024-10-06 00:52:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e0493c54-5d70-347e-bfc1-1c0ac2a19110 | -11.29879 | -46.79158 | 2024-10-06 00:52:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6e0b34af-2b41-36b4-9c81-fe2d027dade2 | -11.29754 | -46.78256 | 2024-10-06 00:52:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7f5fe436-80a2-37bd-adeb-45369341c070 | -11.10938 | -54.23564 | 2024-10-06 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 4ac5e352-ada4-3947-a968-c0e2b34ef0fa | -11.09502 | -54.23763 | 2024-10-06 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| b1c917dd-7d78-3f38-b75b-c25608512c41 | -10.93281 | -52.41453 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8a3736c4-b3d5-3605-9989-5c47eee9dd77 | -10.90096 | -52.38752 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 174d26a3-f26c-3133-b104-dac3ccb011b8 | -10.88862 | -52.38912 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8e7baa71-0112-3d18-b6b6-85b3019d834f | -10.85977 | -50.13778 | 2024-10-06 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b7a6d4e2-339c-3a9f-a4ff-768becd2adf7 | -10.76655 | -52.47279 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 23a874ae-e06b-3092-a818-eb81410069d5 | -10.70719 | -53.04049 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9f76b814-a882-388b-a243-da46210a2e30 | -10.69418 | -53.04193 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| d617dd60-0714-3b63-827d-ca4da4f67964 | -10.68576 | -48.71972 | 2024-10-06 00:52:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e949e88c-345f-3bdf-924d-000e43afef98 | -10.4482 | -50.71626 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 254ea23f-c70a-3078-898a-c83618935ac6 | -10.44273 | -50.75798 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f199c14e-988f-3e3b-b1db-9083390c1977 | -10.44272 | -50.7248 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 226.2 |
| dda0af33-972b-3853-90a2-16399d0e0932 | -10.44106 | -50.71135 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 536.5 |
| 3d28ae55-64eb-3f04-8d9b-b45d6ce3bfe8 | -10.43922 | -50.73111 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 48e34b19-6aa4-3552-be7a-f4d762ec17ce | -10.43747 | -50.71766 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1264.5 |
| 482c72cf-422a-3aef-aa8d-061ce422633b | -10.43572 | -50.70425 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 261.6 |
| f39167e1-e4e8-3e6b-8daf-7461ad8807d6 | -10.43198 | -50.75953 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cad0b540-fd4e-3826-827c-50ec5f731a05 | -10.42848 | -50.73254 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d311ef09-8680-3286-bc7e-5e0cb9cab1f2 | -10.42674 | -50.71908 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 612.2 |


[Clique aqui para ver as próximas entradas](README18.md)
