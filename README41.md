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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a75f4f8d-8b3b-32be-963f-5cf04a5d28ff | -3.11923 | -45.44781 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1d233e4-c804-335b-a466-f60bebb59de0 | -2.30072 | -49.00124 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f59a1393-1c4c-3747-b6e6-7d80e0d32c86 | -1.51913 | -52.3724 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5518cbc3-9498-3dfa-af47-c25e902dc76b | -2.65116 | -46.56643 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75fb0986-5cf8-3553-bb55-d9285c767521 | -3.08944 | -53.13281 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92562b61-5ccd-3ee4-8b52-4f108fa4b97b | -4.40836 | -42.14672 | 2024-11-21 04:29:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ceb731cf-b1a4-30ac-a572-ef254abb7b00 | -3.49251 | -48.22564 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f745d5d-f528-399b-b1a5-013da402bdba | -1.47386 | -52.51661 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b85ae4e-d2f7-340c-81ea-d39d6404c464 | -2.64988 | -46.144 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33fb0059-3f8b-38f4-b3cc-88173237095d | -4.48267 | -44.75777 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7cae7f1-2d27-39c5-9abe-167c35eaf15c | -2.77148 | -45.9516 | 2024-11-21 04:29:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95a6eee7-0579-3a72-9f69-9f821e77e64f | -2.43646 | -46.53312 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 610b69be-523f-3184-8182-8eacda4330f1 | -1.37671 | -46.51589 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d4d22a5-c61d-3a0f-a1b3-bc666868b2f0 | -2.57504 | -49.09341 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b223f55-1938-37ce-ae36-b9052a1f48a1 | -2.76123 | -52.10996 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26d1a463-e433-3b07-b53e-f2b4e69f9b6c | -2.57512 | -46.55457 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84899c09-2bd3-3149-85ca-07997d428a6d | -3.25135 | -46.42956 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3f11575-f0bb-33c6-8923-39329b5c8108 | -2.13491 | -50.70219 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d57878fe-e55a-3d02-afe6-ab1a78381adb | -2.1013 | -48.89356 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11fe668-c7a5-3ffc-8c8e-51c8fbc3e18f | -1.76698 | -52.70247 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14147ca4-4bcf-30ba-b08f-09d7dd84ff49 | -2.75653 | -52.113 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b9cb987d-1c48-33d1-b7c5-1be3e680381e | -2.22703 | -48.51611 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 586dfd35-10ff-3c02-8a8e-b306848f8763 | -2.40451 | -48.60762 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f9db7f5-d86e-380c-a368-d7ac415c9d22 | -0.89299 | -51.72352 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34e25fca-b8ba-37ee-8c4c-73452ca96acf | -0.95174 | -51.64338 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 935b3207-73bd-3e1b-9835-80f7b46047f1 | -3.77421 | -46.67852 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36c39935-5311-34cd-819c-90f0fb1d7d3f | -2.45879 | -47.03429 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0087cafb-00c3-3ea5-bd35-ffb67d11e5e1 | -1.20715 | -51.75783 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8340bf4e-e198-349a-be6a-4f4b328ebf9d | -3.08721 | -45.96445 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce57cd00-8c76-38d6-bb3c-99549836acf8 | -4.09638 | -44.85592 | 2024-11-21 04:29:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74f4ee49-e60f-30e1-a445-cea46b518f0c | -3.11881 | -45.44823 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee5bc53f-4f44-3aea-9280-a36f26b09d57 | -0.8607 | -51.8472 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b3ac9f1-3ef6-3a4b-b4db-70fbffc3fc0a | -3.0639 | -53.28848 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a437e81-46c2-3894-a39b-a1ae82d1e7de | -2.55476 | -47.28637 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cd197de-980a-3ae3-89fe-e0e6d3705ef5 | -3.10937 | -53.09616 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8edaf2e6-4dd6-3693-837e-f6b1d5863f4d | -2.95822 | -49.53994 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26916406-6a35-3dc0-b079-76b8eb6bb8bf | -2.59739 | -44.31675 | 2024-11-21 04:29:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10799434-119c-3fa3-bba4-ee10332404c6 | -2.80266 | -51.80276 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 529fb810-bc73-336e-82b5-4c52e08a349b | -0.41905 | -51.56751 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b66a5cce-6165-36d8-b219-e6f44d1d0d59 | -2.71283 | -46.08588 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4de849a-23e9-3ad8-9756-db9e2ae985b6 | -3.1832 | -46.2624 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fe6cc60-7c64-3bfd-a4d4-bd45b6905211 | -1.54856 | -53.43834 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62340c26-50b3-3e39-8ee5-4f4dc11f7951 | -3.17932 | -46.26536 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a314af3-765c-35ac-8160-2151c94e2dea | -3.23199 | -46.44431 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7049a7d4-55e6-3435-be90-f35275d224da | -2.69143 | -46.07543 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92428a87-8040-3d05-bed5-e1575ce9ec6e | -2.23269 | -46.81857 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09ce16ed-2103-3164-9557-9c46ec11f9a7 | -4.2388 | -46.1197 | 2024-11-21 04:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4fc8fe29-3977-3c6e-b607-548f4db1b6f9 | -3.295 | -53.8597 | 2024-11-21 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4ac03ca6-7bf1-3eed-9008-01ac5b130b3f | -3.2768 | -53.8199 | 2024-11-21 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| cf5e3725-6c34-379d-99e9-85abb71be7c8 | -3.2767 | -53.84 | 2024-11-21 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| e8332840-d134-3b05-abe6-a5b9ca2a51a4 | -2.0259 | -54.5289 | 2024-11-21 04:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 59d1aa32-f4a6-31a4-8b2b-71f2f5debadd | -4.58 | -48.0132 | 2024-11-21 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 3539e937-18ba-3e22-9ee5-c9e5b808e052 | -2.7676 | -52.1045 | 2024-11-21 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 87cc494f-48a2-34e7-851d-96c6be75f2e4 | -6.1182 | -42.5086 | 2024-11-21 04:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 01b77246-d136-3a01-a160-7065d89354d6 | -4.5799 | -48.0349 | 2024-11-21 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 995fdc66-d5f8-3f28-bc27-725446e1f349 | -2.7675 | -52.1251 | 2024-11-21 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 592721f4-f471-3d58-9845-a35d4bea5e8f | -3.2951 | -53.8395 | 2024-11-21 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4068b810-a6cb-33bb-9231-353b3448918e | -3.57275 | -54.68539 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a26058ff-1ba4-3321-bd7b-ade624707000 | -4.43091 | -48.29972 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58287c24-03f6-3e9f-acfa-2630382785ee | -3.68128 | -50.22238 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40b9a14f-ba21-363f-b5b0-74033898d916 | -4.56657 | -48.02243 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e728e4d-159d-3ac2-a8e3-0a81c9644cea | -4.1847 | -53.58205 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9131a48-b1b6-3304-b6ac-811f4d47604b | -5.65171 | -45.19694 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76b897b8-0272-3f76-88c7-e8737e674fc8 | -4.58158 | -48.01405 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0730955-bfda-34ca-990a-8ef81c46410a | -3.20246 | -54.32932 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d1b4915-3338-3cf5-bb2a-822639ee1ef7 | -4.13909 | -47.73404 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d552870c-8929-3771-a470-92c5b963c20a | -4.10115 | -48.48453 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef70d52d-b08b-37f2-ae2f-1ba78d6641ea | -3.286 | -53.83987 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 736ca339-b01b-3dd3-92e5-e219c5cc6eef | -8.14718 | -43.79199 | 2024-11-21 04:31:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6569b2ab-0002-3807-bdf8-072d732b1669 | -4.11371 | -51.05186 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19d4c8ab-236a-3ccd-a559-7787cdc68eff | -3.51758 | -53.79509 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecec8245-659f-3bfc-8583-c7ad8b390053 | -3.96117 | -49.69933 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2eeab574-6311-33be-85b2-15617957f0b0 | -5.24289 | -42.63064 | 2024-11-21 04:31:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2c0adcd-23c5-3c80-8612-20cbfb1b998c | -3.0479 | -54.52899 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be14ab59-3a05-34ab-848f-a268259a8424 | -3.62186 | -51.08762 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4732b5e6-0246-38c6-9da3-c4aa5c2139f0 | -4.7472 | -48.98861 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4c92cb0-c9fb-3fb9-8f20-eb378007c512 | -3.72819 | -51.16131 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b605066-77ed-3a0f-9c59-e6544e016758 | -4.55175 | -48.01289 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8744016-27eb-3667-9590-f4f5897175b9 | -3.28867 | -53.84671 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab3f1fd2-a6fd-3348-8aa3-2ee1d73f8a29 | -4.06996 | -51.03596 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afa48d51-2ecb-38f2-b8e2-1de93b337b4d | -10.11993 | -36.45493 | 2024-11-21 04:31:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 092298e3-d8ad-30eb-9fb2-2a36878d1b07 | -3.68195 | -50.21827 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cb64ec63-49b7-3aa7-a739-f3071aa3e12f | -3.60053 | -51.47506 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29a7ada8-c101-3e3e-a237-79ee02d50f37 | -3.98935 | -49.92603 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 615fc811-0ecc-3fcd-9985-2a2b38c7730c | -4.60581 | -45.73981 | 2024-11-21 04:31:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e81b481b-e9f0-3c37-9956-4bac2875571a | -6.63575 | -47.34959 | 2024-11-21 04:31:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f03abbc4-b859-315f-8a19-199d9f65dd0a | -5.33391 | -49.51313 | 2024-11-21 04:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 971fcf54-b94f-3fa6-a4aa-d79b7d778d9a | -6.18409 | -43.41125 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c01afd87-6a89-3f88-8cc7-6ad2d3e65df2 | -3.24554 | -52.83 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83334d44-78be-3ce2-87c0-f46f57f9485e | -5.18151 | -50.63697 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 191196c1-c53c-30c6-bcf7-fd53763da247 | -3.22031 | -53.83924 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d71782a-324a-336a-8311-fc839e367fdb | -3.18034 | -54.31573 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f8fb326-0101-39ce-a064-bd56dc18c421 | -3.76582 | -52.13794 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56554171-6cc9-3054-8601-4e5b81bd8096 | -7.03214 | -47.62571 | 2024-11-21 04:31:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42c88c84-8cff-3546-8f9c-598f4f86dbb7 | -4.07071 | -51.0314 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d1458f1-a6bd-348a-bb53-b6f439c497ad | -6.86685 | -44.76051 | 2024-11-21 04:31:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ba1a7ad-b645-36e3-95ff-eeae4a68cb9d | -3.56797 | -53.25547 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dfdde07-48cf-33fe-9c6a-17c78c30035a | -3.60132 | -51.4702 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dfad3de-37ef-3fa7-8fa1-d9849e56baea | -3.51149 | -53.80352 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37273b2b-7692-3b30-a373-85b0c026aa7d | -3.82907 | -52.25847 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
