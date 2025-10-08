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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36ca8f23-41b7-30ef-b3c2-99219fe1da97 | -9.18594 | -47.79609 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1e58d5ab-7521-32af-9eca-30c584c6047d | -9.39404 | -45.94979 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0672cb46-85e4-3233-a748-f5873642a389 | -7.78491 | -44.21468 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91638ae0-d181-3add-96e5-6e41cc575dcd | -17.30114 | -58.07023 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5615dadd-fcba-302a-b216-65782d7ef4de | -17.82809 | -57.63385 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ecf26e10-c5d5-324a-a27b-59cda3265325 | -8.21976 | -44.2048 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab4ebc6b-d1c7-34cd-af7f-9835727332fb | -15.254 | -50.20359 | 2025-10-08 04:19:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34880f5f-5af7-321d-96a8-b3b7f1fcf190 | -8.56072 | -46.23547 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16794c4f-6aaa-3767-ab3a-483301d0df55 | -8.50676 | -44.21471 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4348bc7-25ca-3492-b2ff-9e207820880f | -17.56534 | -46.07945 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02b293c4-8864-30b9-a1e2-95a2ce1eb3aa | -7.81782 | -44.18029 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ebda888-fe72-3570-afd3-097b1ca5c5d4 | -8.62372 | -45.10032 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8845191-a3e0-3aea-be99-ac2c6b9b94b6 | -17.8515 | -57.58688 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 841abac0-7e5b-37b8-9107-e4c72ed07f25 | -15.01795 | -47.55822 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce9ad77d-2c9f-31e5-912d-352d77f6cc75 | -21.06969 | -46.89103 | 2025-10-08 04:19:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7eeb5d1-e441-35ff-8e5d-16710a0f71d3 | -15.3149 | -46.17051 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1735c44-546b-38a3-9854-691dc1165b1a | -8.19402 | -44.11443 | 2025-10-08 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd2a06ad-870e-3ed7-aaec-3885df76c075 | -15.16685 | -45.74442 | 2025-10-08 04:19:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d6a10c8-7c61-3dd7-8d52-9f1719d496c8 | -20.09256 | -44.20449 | 2025-10-08 04:19:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 40f6267c-123d-3ca5-8d6c-1573d862f023 | -13.76568 | -45.80933 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce83257f-84e6-36c2-ab65-75ec2632acab | -18.0239 | -57.52459 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7acf7da4-3ca8-35e8-85a8-8c7c108ad5da | -17.35884 | -45.05457 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39afa505-4c9b-39a3-8ab7-4e46d351a94b | -15.28151 | -45.33969 | 2025-10-08 04:19:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f327ea72-78ed-3ff5-b6c1-ef8eca41290e | -16.62869 | -45.42056 | 2025-10-08 04:19:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05018b15-9585-34ce-972e-a878278a7fa6 | -9.19173 | -46.911 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45c62f9b-f992-3f6e-8a21-7fbcda27c6c6 | -18.05426 | -57.53009 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d1379c53-2481-342b-b4b8-42e558c44d62 | -15.59704 | -47.25415 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7079460e-5b64-3393-a9cb-038bdfee6d49 | -17.95844 | -57.50636 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 65bf9cbe-2fd1-3f71-9123-ba7674937413 | -15.07721 | -46.6216 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdf10fec-f7cd-3826-b370-fd07b4682bd9 | -18.02353 | -44.31357 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19bb55c8-1fa5-3e07-816f-56f6e38e87ca | -21.06636 | -46.89042 | 2025-10-08 04:19:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56327e42-0bde-3d38-83ce-a867bdbc566d | -20.08967 | -44.19995 | 2025-10-08 04:19:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 05decf3d-233a-3adf-9eb0-b8f48bfdd496 | -14.70061 | -46.01447 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 391c1f6c-46c5-34f3-8860-33dceaba693d | -14.71318 | -46.07229 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8a0bb772-894e-3160-976b-66037e664a23 | -8.52476 | -46.23367 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80a50f86-b036-392f-86c2-5d907596f95d | -16.88733 | -46.96305 | 2025-10-08 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6955315a-6914-38de-88b9-25d7ae55949a | -20.19 | -43.92402 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6cd121b-7a9b-38f3-922e-838ccdce9abe | -9.19575 | -47.8074 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9e8c9fe-5782-35e5-b3f2-7c1cc44bacdd | -19.5451 | -44.75743 | 2025-10-08 04:19:00 | NPP-375D | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5662347-8282-351f-8873-f31132f0b2f3 | -18.40399 | -45.20002 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b11ac87-9acb-3d15-a916-0261b6790fb6 | -14.82499 | -48.41623 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cc5d5a0-a5da-38c3-a6e2-ded15c08a979 | -21.04338 | -45.67679 | 2025-10-08 04:19:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0dd1c96b-d604-3648-956a-c4cf95e34f71 | -17.36046 | -45.05811 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 969b16de-fc12-30e4-a81a-c972ce79c8f3 | -8.61707 | -44.90629 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bfd45c7-b75f-3cb1-9ab1-ae8d996847a6 | -14.7413 | -47.86366 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8194770-a38c-34fb-b9ab-24cecbc5963a | -19.5215 | -44.07281 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 418ec89a-7b92-3617-9e3d-1d0bd52b59ec | -15.59903 | -47.2515 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6b107bc-279c-31b3-aade-a875c03d30e9 | -8.26666 | -43.82481 | 2025-10-08 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce29c3cc-996a-3492-8528-2dd022c4f6f3 | -8.37488 | -47.05978 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf175928-9a76-3138-bf31-3512d3a63eaa | -7.76017 | -49.53972 | 2025-10-08 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b776861a-4e6b-3621-8406-4027df4ddbfa | -15.07319 | -46.62482 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7f77a1d-ea0c-3d65-85f2-2e1284ec19d5 | -8.12173 | -44.77155 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 77c90cb0-825f-3f40-b42d-827c248e2296 | -14.70415 | -48.40134 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5549b730-e8ee-304b-bc2a-ae91f62e745c | -14.92706 | -46.78912 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e50995c-9a4c-3913-a507-124eb4d2e5de | -13.80951 | -45.80534 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28f863c3-4600-3485-922e-5a46d27a7c75 | -8.85644 | -46.08186 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc9925df-14f9-3a1a-8158-53346ab6ea22 | -7.77825 | -44.19206 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7be20930-1b72-342a-954f-6c7adf6a6932 | -17.8288 | -57.63118 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fcd38c08-0ee0-322a-aded-0ec57e152b64 | -7.43176 | -46.62751 | 2025-10-08 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f22e5366-d2e3-3b16-8fd6-bcec8936282f | -18.05516 | -57.53045 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 768b8476-28aa-3046-8abf-19e6686dc9d1 | -17.27817 | -58.11447 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e3eee43c-7a26-3b68-a3ff-eae81f0b44cb | -18.05917 | -44.46986 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4dd87073-521f-33ad-9a35-637909d236e5 | -14.76802 | -46.0106 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f458f09-dcad-35c2-932e-7a1ace2d24c5 | -7.78825 | -44.21521 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79ccadeb-88d0-346c-a07d-ca990b8d8677 | -13.72303 | -45.66869 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 291f5aae-2819-3993-8dd4-56df57fb4b09 | -15.31609 | -46.16316 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6830b8c7-66ee-37f5-8acd-8e6398376c8d | -8.61291 | -44.90606 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eb31a7d-1f9d-34b7-a37b-a00caec0473e | -8.5847 | -44.3393 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ebe85e5-c0ad-30ef-a31d-f20da7c2f252 | -16.18658 | -43.67008 | 2025-10-08 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 193fac57-b3ad-3412-9dd5-df0377212757 | -8.19458 | -44.11093 | 2025-10-08 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 769fa4fd-9a0f-3da7-b0b8-b0a3c391baa6 | -16.00996 | -51.05224 | 2025-10-08 04:19:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a044bc2a-95fe-3997-ae93-964cf8378399 | -15.07659 | -46.62533 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a65685f-faca-3f05-8e12-e0d1a9f477c0 | -18.06707 | -44.46355 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e9fdf0a-b994-3231-94f2-68468d3fa951 | -8.52742 | -46.2832 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bad0437e-054a-3dff-8057-d306d9777b2a | -7.82394 | -44.18487 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 351c0fb2-5891-34ac-9406-063c6337efc7 | -18.10089 | -44.70345 | 2025-10-08 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acd9a3ba-2d09-39e0-b7cb-49e55a966cd2 | -17.28905 | -42.64698 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d303b49f-962c-3e29-bbda-1839544fb9e4 | -9.1781 | -46.92572 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a5abbb9-9af0-3fa7-84fa-42598a1626d6 | -15.0353 | -49.45058 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35bed975-b96b-3d34-bee6-883b9313aebf | -18.55419 | -41.57468 | 2025-10-08 04:19:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ddb8c75a-ca17-3243-896d-1f7204561b66 | -9.20898 | -46.89672 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bec0b61-a63a-3f07-abba-94c94bf525cd | -12.18512 | -57.2389 | 2025-10-08 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db30dbe-0d9b-31c6-882a-049d76dbee45 | -14.91522 | -46.81801 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96fdfb6b-87d6-3c49-9e82-199f849b0839 | -14.36452 | -45.23878 | 2025-10-08 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81634718-aa72-38ea-a71b-57a9551f39a2 | -8.84011 | -44.43085 | 2025-10-08 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7fbe1ce-953c-3af8-9e75-d8c8d206e702 | -21.23865 | -45.79003 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| feaa9de7-62f3-3e6f-9806-a3c0bc898834 | -17.73263 | -44.37272 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f81db0ba-7bcd-361e-8795-118cc2d0dfd2 | -7.5099 | -45.15989 | 2025-10-08 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6994e33-40f8-3ae9-b6ba-0bd63307d909 | -8.1886 | -43.3367 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| f627722c-cf85-3fed-a2ef-43525557f9ae | -13.75374 | -45.75531 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daa75d8e-50f5-35f1-8303-dfde39ea18f3 | -8.1875 | -43.34368 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9b205389-48e6-3c2f-a92b-1f6e6e6a0202 | -16.32874 | -47.06356 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c88d2750-bd53-3d46-9e5d-e46b1f427e05 | -8.11809 | -47.25149 | 2025-10-08 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2990f415-c48e-39fc-ad94-4a2abd4244f9 | -16.00923 | -51.05627 | 2025-10-08 04:19:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ec618b5-f016-3bfc-983b-61e407b27ff4 | -17.48676 | -43.33557 | 2025-10-08 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9bb60e3-31e5-3be9-a8eb-6989942264b0 | -14.90297 | -46.85163 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5589c64-ec00-32f9-808c-3d2f2641f430 | -20.49986 | -45.95232 | 2025-10-08 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f1f0083-8070-3b81-bc36-8f0e03c584d2 | -18.02123 | -44.94475 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44134fd8-4537-3129-a7a4-aa849e6901f9 | -20.17126 | -42.21171 | 2025-10-08 04:19:00 | NPP-375D | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 13494508-e985-3d94-857d-e85d5edb9fd1 | -8.56491 | -46.23205 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README57.md)
