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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e71eddf4-755e-33f3-9500-520419a57cc0 | -4.262 | -45.58543 | 2024-10-22 03:53:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 738130e5-a82f-3b2b-9a1b-0c94e31732cc | -4.2611 | -45.59089 | 2024-10-22 03:53:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20bc8b41-e35b-3b8c-9863-ef3742e0593c | -4.25853 | -45.58585 | 2024-10-22 03:53:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9e8af50-9efc-31c3-8a3c-789bee66e198 | -4.2562 | -45.59011 | 2024-10-22 03:53:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dc7bc3a-d777-3140-b677-93c14ae1ec2d | -4.10293 | -46.1383 | 2024-10-22 03:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3785bd7d-1c5e-3587-9f85-3288bade7114 | -4.10241 | -46.14132 | 2024-10-22 03:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9b668d6e-a7b7-38d6-bec3-831ae6cd9299 | -4.09675 | -46.1438 | 2024-10-22 03:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36c81772-0cbb-346b-879f-7f88f2431196 | -4.01848 | -46.03186 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e07fe33-d3f0-3167-ad38-65ee3dcff720 | -4.01397 | -46.02774 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d866df7-cd0e-3fbe-a454-4958f2c19f9b | -4.01349 | -46.03052 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bfe53f8-c592-37d0-adda-c13e0efeb397 | -4.01298 | -46.03356 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b26d4e8c-ee75-3429-83f7-c5e567310eeb | -4.01246 | -46.03664 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5540e979-979e-317f-8268-379d67289db2 | -4.0094 | -46.02393 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab2c7a3c-96f4-3729-a4e0-f3972686fc06 | -4.00893 | -46.02668 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b54493d3-3266-3f67-a0e3-bfd9e8ed7952 | -4.00845 | -46.02954 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05ce3b13-fd88-3f49-ac96-dc0f73d139f1 | -4.00793 | -46.03259 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3edc448d-1fcc-3f81-999a-a01c93cce83b | -4.00741 | -46.03567 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f72626e-6473-3895-8ed5-ca3848ca6706 | -4.0049 | -46.01974 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 662cb39f-c693-3bc1-8905-a4e5b031bde8 | -4.00442 | -46.0226 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71c2204b-6237-3b74-bd6f-b25562ff35a4 | -4.00391 | -46.02559 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 285873f2-86c1-397a-8252-486e3185cf14 | -4.00339 | -46.02863 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8307aafc-32c4-3900-bf90-b1f07b78e8a5 | -4.00288 | -46.03166 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bacef62-c7b8-3c4a-96e7-31ce931a8070 | -3.74788 | -45.75613 | 2024-10-22 03:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f33b400d-db96-3453-89e7-5230c90ca63d | -5.14926 | -46.09753 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d7ab4c-c070-3299-bef6-7622887d51af | -5.14873 | -46.09864 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a8876af-2fcd-3a5c-8050-c8474584595b | -5.14473 | -46.09205 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d70f1d2-e0cd-3f5f-a391-bf4950258c9a | -5.14428 | -46.09658 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 28e193bd-6c3a-3e50-a1e0-894537b4be8d | -5.14375 | -46.09767 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6db32ab-9a06-39f1-a41a-8fa4e8e4b697 | -5.69527 | -46.46829 | 2024-10-22 03:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 386429ad-6218-362f-a425-1a74d6704832 | -5.56384 | -46.36609 | 2024-10-22 03:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab79d9d5-276f-3b32-835b-edd5eceac6d4 | -5.44165 | -46.35841 | 2024-10-22 03:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cd9cb1f-329a-3769-82bd-bdb2830cb8e2 | -5.43659 | -46.35756 | 2024-10-22 03:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3735f0a6-524f-3d2c-9a2a-85b6f67eb42f | -4.60376 | -46.47573 | 2024-10-22 03:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e3ea2f1-d94a-39a7-b3b1-a543ce774922 | -4.59857 | -46.47501 | 2024-10-22 03:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6206bd-4b55-39b0-a781-9cebd57c2e53 | -4.44355 | -47.77088 | 2024-10-22 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df3b3be0-287b-33cb-9d38-f4fd706bb9f3 | -4.43788 | -47.77002 | 2024-10-22 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc1b0ba0-b627-387b-be8f-7e8c67e2e86d | -4.28236 | -46.28481 | 2024-10-22 03:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ea36fa-d9f2-3519-9a15-8be936dfaa07 | -4.27725 | -46.28382 | 2024-10-22 03:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86e3f59e-8df9-3742-8246-bd994cc5f936 | -4.21385 | -46.17839 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d1e5af92-91aa-3b72-aa01-01dc983575d9 | -4.21335 | -46.18139 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6d0d0e99-48b3-30a1-80c0-0b83107cf98a | -4.20823 | -46.18058 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 924c68bb-8ae4-355e-96e3-41f12459e1f5 | -3.9111 | -46.44648 | 2024-10-22 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55e8f0f2-2ee5-338b-8bdc-621f47315a86 | -3.91106 | -46.44471 | 2024-10-22 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4de6b4f-9bee-306c-9795-a70d7e1893e7 | -3.91058 | -46.44967 | 2024-10-22 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c2ef17f-c2cd-3b3d-85a0-b7b1351d41bb | -3.91051 | -46.44789 | 2024-10-22 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8485c26-59d5-32cf-8a52-3bc0e35ab2fb | -3.82769 | -46.92836 | 2024-10-22 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30e48c6c-4d6d-3ecd-8a48-dfde10634073 | -6.64027 | -47.34448 | 2024-10-22 03:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 041fbae4-8d3c-3668-bce6-f3ff08360080 | -3.80755 | -47.80014 | 2024-10-22 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 40f42fab-be1e-331c-ab92-01bab2511e93 | -3.80686 | -47.80415 | 2024-10-22 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0133f5a5-209d-3e18-b434-20d7f3e10128 | -3.80183 | -47.79916 | 2024-10-22 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ee68336-4106-3ff5-a550-4d6b1a6dac9b | -3.80114 | -47.80317 | 2024-10-22 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 965ede80-cb79-30a9-bbe3-cff68b5f7516 | -3.80047 | -47.79999 | 2024-10-22 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a929ca-8204-310b-ba68-8054dfcc4dc3 | -3.7998 | -47.80402 | 2024-10-22 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 281ecd4f-733e-30e3-b79e-7096ca343c5f | -5.3489 | -35.43058 | 2024-10-22 03:53:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 796f5c4e-8ba7-3060-8688-be1a3108e047 | -7.52335 | -34.86812 | 2024-10-22 03:53:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a0cacf4a-60b3-3fd8-a0f8-1d7498112fe0 | -7.25205 | -35.31809 | 2024-10-22 03:53:00 | NPP-375D | SÃO JOSÉ DOS RAMOS | PARAÍBA | Brasil | 2514453 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ae1ba407-c1dd-3883-8d4e-96e2b381d00a | -9.11432 | -35.45856 | 2024-10-22 03:53:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b07de1d1-1cac-39e9-9e43-e37fb26415dc | -9.11367 | -35.4629 | 2024-10-22 03:53:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 63c7c533-56ba-3e1c-80fb-12a384016e68 | -9.11065 | -35.458 | 2024-10-22 03:53:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 15f727d8-0fbe-39f6-ae9f-4dd37c391be5 | -9.11 | -35.46233 | 2024-10-22 03:53:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e0e06e3b-71c7-385e-9094-7415c75332fd | -8.44876 | -35.0359 | 2024-10-22 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0e4403f9-0b3d-393f-8930-ff82962f29e1 | -8.44679 | -35.03343 | 2024-10-22 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c5c73f23-c4bd-36c9-bad5-c72f0a2df0b8 | -8.44615 | -35.0379 | 2024-10-22 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cf1aaf71-f9ba-3609-80e1-15d936023c10 | -8.44504 | -35.03534 | 2024-10-22 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 06bd6a2f-d8b6-3092-86a5-1a570f9a3826 | -8.44307 | -35.03288 | 2024-10-22 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 01185bb2-7ee3-3ac7-b44a-1e0f7c443d61 | -8.44242 | -35.03734 | 2024-10-22 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| eaa3dfa4-e026-31fd-bf32-c0f61e1ec127 | -8.44131 | -35.03479 | 2024-10-22 03:53:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d473e840-3b5e-330a-a45c-57546cf1c5f5 | -9.9956 | -36.10646 | 2024-10-22 03:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b0173107-2011-3c57-9e53-5833d0ff7129 | -9.99498 | -36.11059 | 2024-10-22 03:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 79fc52b5-8fdc-33a3-a8ef-e006f62df904 | -9.99201 | -36.10592 | 2024-10-22 03:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 9e8e69b0-c629-3b80-8c6c-63e3a4c5f49d | -9.99139 | -36.11005 | 2024-10-22 03:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 0b49d35f-d6fb-39ba-96cd-c8f1443ef700 | -9.46324 | -36.29259 | 2024-10-22 03:53:00 | NPP-375D | PINDOBA | ALAGOAS | Brasil | 2707008 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5898fb47-92df-3808-89f2-0be4e0feea8e | -10.28673 | -36.32586 | 2024-10-22 03:53:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7e72356a-b222-3dfc-bca8-45df4b0134f5 | -7.51205 | -37.03197 | 2024-10-22 03:53:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b71bea4a-e4e2-311d-ab1b-b21631823dd7 | -8.99343 | -37.15033 | 2024-10-22 03:53:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2987d9fc-89fa-35de-b47a-fb35274b287b | -8.99287 | -37.15402 | 2024-10-22 03:53:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d888a4ef-60b7-35b0-948e-45652c58b39b | -9.63034 | -37.15821 | 2024-10-22 03:53:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85f77d0d-e7d5-3f48-8bab-28af925dcbb2 | -10.68456 | -37.03096 | 2024-10-22 03:53:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aee54061-b38d-3c11-ab73-d0b04f2b545b | -10.68399 | -37.03482 | 2024-10-22 03:53:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 04218bdd-da2a-3434-bda5-8210e0bc95cc | -10.29842 | -36.67731 | 2024-10-22 03:53:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f32c00ff-4113-38a3-af66-64048d2ba348 | -10.29784 | -36.68121 | 2024-10-22 03:53:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 28eaaf43-fc87-34c5-a36b-0779f78d7c13 | -10.29726 | -36.68511 | 2024-10-22 03:53:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3a5e0a1-c8bf-36cf-af19-964f77b87dc0 | -10.29434 | -36.68063 | 2024-10-22 03:53:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bfeb6c6a-30bf-3928-93dc-3dab86cfc761 | -4.467 | -42.90072 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d5bdcf3-711c-3275-8107-fc40318adadb | -5.13289 | -38.15269 | 2024-10-22 03:53:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8994822-50c5-3c65-9eab-1c49a771e987 | -6.67201 | -38.58388 | 2024-10-22 03:53:00 | NPP-375D | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3f0fdd1-e6dc-34e6-88d8-622dfac8793b | -8.08762 | -38.184 | 2024-10-22 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bfcc1db5-c5a0-3503-9692-bfa2928535ac | -5.13139 | -39.72774 | 2024-10-22 03:53:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e73e87c8-b1cc-3aff-a6b1-4ae00d2d2df5 | -7.96106 | -39.81734 | 2024-10-22 03:53:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9615a0ab-23a6-377c-90d0-a1e54af08a25 | -7.96048 | -39.82092 | 2024-10-22 03:53:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| adc1c7da-5d1e-376f-9526-d5131844712c | -7.79409 | -39.65845 | 2024-10-22 03:53:00 | NPP-375D | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f73d007-a6df-3fd7-96f6-e5465bca1a47 | -7.60935 | -39.24465 | 2024-10-22 03:53:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 70aec6f8-392b-362c-96ab-ea16baddecf3 | -7.55578 | -39.8811 | 2024-10-22 03:53:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4aa8b020-2bc7-3561-a084-b7b43f9df7b5 | -7.31049 | -39.33779 | 2024-10-22 03:53:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2df37d5c-c231-376f-8cc7-bd6c27f9d930 | -7.30993 | -39.34132 | 2024-10-22 03:53:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 68456b48-9dfa-36df-b6e4-5fe266f9e054 | -6.73127 | -40.48246 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5942c619-1728-32c6-977f-b54e630ecc96 | -6.72992 | -40.47899 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| aa45ca7f-34b3-3eba-af13-c6a89de4cd6d | -6.72932 | -40.48279 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 75f3e4d1-4822-3408-bc4d-75b819c60cfc | -6.72889 | -40.46325 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6b2bebc-9f0a-3aa1-aea2-8ba25502ed65 | -6.72871 | -40.4866 | 2024-10-22 03:53:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |


[Clique aqui para ver as próximas entradas](README17.md)
