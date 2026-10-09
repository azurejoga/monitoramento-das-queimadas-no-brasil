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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 524245c5-213d-3a58-85ab-32e1bdc365fd | -3.3081 | -54.02 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b3fec8-d7b3-3b59-807f-64080519f1a9 | -6.8792 | -45.9142 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00333a66-1250-3852-8729-3098cbae548a | -3.7243 | -59.450699 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd5baf17-6165-3969-a638-0f4a62afcb52 | -3.1701 | -50.592701 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc6f439-4179-3185-8d10-47c5d5db4e09 | -3.0804 | -54.242599 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 112134a1-7f7b-3d82-8682-cb888bbf68a9 | -15.4611 | -45.438301 | 2026-10-09 00:06:00 | METOP-B | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa4c72c5-e71b-32c3-aee6-02166bfc6191 | -9.6841 | -58.0704 | 2026-10-09 00:06:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b04e42f7-0745-3376-9227-868db3697f8d | -18.3312 | -42.368999 | 2026-10-09 00:06:00 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84ae6837-2f69-3058-bfd5-4ff28c67ec7a | -4.9386 | -45.729401 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb88c84d-7b3b-3db1-b3b5-06cbd27aa81c | -15.4249 | -43.244598 | 2026-10-09 00:06:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3d9fab51-a8a3-3525-abba-4e0a188af347 | -5.9521 | -55.3382 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d904486-52aa-369d-9360-17efe33c6cc7 | -7.3778 | -44.034 | 2026-10-09 00:06:00 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae1787cd-34a0-3c23-99d7-da7d3973844c | -6.7299 | -55.1078 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19b819dc-90ae-3fa6-93e5-5a6136aa8c32 | -4.2253 | -46.929001 | 2026-10-09 00:06:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc0f2c57-f4fb-31b5-812d-0d0510de930f | -3.2918 | -49.123001 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f53d350a-66c3-3378-aa9f-48a88d8673b6 | -13.164 | -46.866798 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c6c44cee-af21-3008-a136-471946b7f460 | -3.013 | -54.124599 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0451bba3-00dd-3885-923e-641ed258145a | -1.8918 | -54.668701 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32081150-261a-36e6-9d1a-c331f28efecd | -3.1222 | -53.7841 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b046541-ec0e-3cca-bbad-0417ef534530 | -11.1947 | -45.295799 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd1e9a6c-8960-3cc3-94aa-8c330a2e4b6e | -5.7173 | -41.7827 | 2026-10-09 00:06:00 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93826719-de1b-3fd8-a167-af58a7f6e44f | -14.8698 | -50.288898 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 50960301-8525-3890-ab73-0ba3ec042a80 | -15.105 | -43.639599 | 2026-10-09 00:06:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 4f9844a6-ef8c-3d46-869d-cf50c128db3c | -3.0052 | -54.2281 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68075d46-d1e2-3b69-90f7-abd93e02a03a | -3.0002 | -54.067001 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a02e129-41b2-37ce-afcf-9afaa5c8c141 | -11.0761 | -44.0867 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8d5ea65-fad2-317b-981a-a1a833dddc8d | -14.8832 | -50.304001 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 786da463-f471-39b2-a825-3d1c1056bdfd | -14.0827 | -43.776402 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b63790db-0bad-3d92-b3e7-c73dd020240d | -7.5127 | -47.3228 | 2026-10-09 00:06:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1733d8f0-d7fe-3da4-8dc6-2f291c43dd5d | -18.2887 | -49.500401 | 2026-10-09 00:06:00 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab4f43e0-9195-3b60-aa95-587690ed23fd | -6.8755 | -45.898102 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58d98b25-5242-3b3b-b88d-b52a52f92a30 | -2.9947 | -54.0882 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5331049f-14f0-34d2-9fad-8889a9cbe789 | -11.647 | -43.7062 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b28445f-fa6b-3352-a559-3b7dc2f53c5d | -3.0296 | -54.0606 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176da8cf-7b5f-3dab-944b-e5718627e3c0 | -7.5642 | -46.691502 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6218ef3f-0e91-3b4e-afe8-4da67eb9cfcf | -3.9319 | -56.012402 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c039bece-1afe-3049-8551-038a6c2b1928 | -9.8592 | -47.4823 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a15fef7-954a-3149-b284-c8be01f3a4ae | -13.1708 | -54.3536 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2fc396-2bff-3f52-9663-836a786c2fbd | -3.1843 | -49.240299 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9ad6fa4-9bb0-3289-9c86-4826ede07d18 | -11.7629 | -44.941799 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54639345-cdec-32ae-9e0c-b26c80a05831 | -13.7574 | -43.625702 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb960b6-6418-37f2-9525-c1a493733126 | -5.901 | -52.040298 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d22e02a-8d18-3672-83dd-a8f35d5622b5 | -5.7874 | -43.848499 | 2026-10-09 00:06:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a58935cd-2413-3307-8f45-15ad8ed3804f | -10.2442 | -49.674 | 2026-10-09 00:06:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7248502-af1d-3444-b33b-f8d7a92bce3d | -2.2168 | -58.098598 | 2026-10-09 00:06:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2d5ae86-5119-33cf-8c5d-921f2ee7b976 | -3.01 | -54.064899 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd2a6d11-a99d-31a7-9bb0-b4bcdda21743 | -6.7407 | -55.158501 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eedf85f-b591-38b3-9d6c-3a742741b3b7 | -5.1 | -46.204399 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb283739-c686-353f-a3a9-3719aa1aca1f | -11.7963 | -46.791698 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26f58cd8-2829-30d3-b7ec-b887976c4e21 | -11.7622 | -43.539398 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7486caf-bd12-3352-8ee1-2036dc15a5e6 | -8.0796 | -45.618099 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59528418-d420-3fef-a5f0-54fbdb43ee2c | -5.3932 | -45.911201 | 2026-10-09 00:06:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a63a4ae-f148-3e27-87f6-2c90aa4950b6 | -7.5059 | -45.768799 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2be48351-89ba-332c-ba10-e87369a84b6f | -7.4172 | -44.770401 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 704d86bd-f1ca-37c4-8f47-135fd4f370eb | -5.9934 | -40.926601 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5afe176f-742a-3d1c-8877-ba0abfefd516 | -13.161 | -54.355598 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29bf570e-ef5b-3dc3-928b-fd92a4dff182 | -3.1064 | -53.944199 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 563e0921-78ae-3161-ac65-e2711a49291c | -2.7427 | -48.429501 | 2026-10-09 00:06:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a07753c-657b-3c69-b8de-300d99aafe7d | -3.8935 | -55.884102 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffd2f6ec-9f21-3f0c-bb3b-a0fed61ef4bd | -18.290501 | -49.508999 | 2026-10-09 00:06:00 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 802a8e13-dab1-3246-8cf8-b2dfb799935d | -13.8714 | -43.801399 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd515ca7-e0b5-302c-b90a-195e340d2173 | -14.2644 | -52.789501 | 2026-10-09 00:06:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96bcfb4c-8a76-3e11-9142-16025eb8c163 | -11.307 | -46.681099 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22a8edfc-4119-3d54-920a-090ff6ca52ae | -6.3874 | -55.272999 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 336fd336-6785-35e6-8493-9319a66b65b1 | -6.1112 | -51.734699 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c307bbb8-64c4-3153-8f13-1dc4823ba92f | -2.9595 | -48.7486 | 2026-10-09 00:06:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a877f27-ea2c-346f-add3-bcbd1bbc8b6a | -11.6253 | -43.701801 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40e58598-e6fa-363d-af99-31d499f3fa4b | -3.2575 | -54.0619 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2de8f599-f8d5-3c5d-8ea7-88affddae15a | -3.1879 | -58.6433 | 2026-10-09 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f8c29a08-e26f-3887-8525-8c00ffe719dc | -3.0925 | -53.9455 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 17bac218-57a3-30fd-93ad-ad6c17cb05e8 | -6.021 | -40.9577 | 2026-10-09 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| d59a4ee2-9648-34ca-a08d-2621508d5029 | -3.0186 | -54.068 | 2026-10-09 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b6cf6a55-a1f8-3e84-a62d-00671ddc69d1 | -6.4411 | -55.0424 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ffaaa6ae-cc15-3804-b7b5-7a1563dad9aa | -5.8842 | -43.4199 | 2026-10-09 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| fee0003e-f0e6-32c8-94a4-a857f70a642b | -8.6301 | -66.77 | 2026-10-09 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4ad57574-f0ee-3b8e-9b9e-0b803b7048e9 | -11.8495 | -43.6072 | 2026-10-09 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e2712d13-1abd-3eac-a424-485196eb9ea3 | -6.0024 | -40.935 | 2026-10-09 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| efd95248-4665-3ab2-9459-afd17e5a7bba | -10.0253 | -48.036 | 2026-10-09 00:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c15bec50-eea7-318f-be5f-8f43ab9fa704 | -7.2182 | -55.1416 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 9410c870-907d-32ca-b34b-c928091fc182 | -3.1101 | -54.1661 | 2026-10-09 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 949b73a3-5b31-32a3-bf0a-0e730ab8f43c | -6.8907 | -45.8988 | 2026-10-09 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| afd5e6ba-05f6-3787-a3ec-f941463b44d4 | -3.0926 | -53.9254 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f97533cf-261e-3cb3-85a6-61adea214b85 | -3.5676 | -54.6946 | 2026-10-09 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| c4b47581-b2ba-3bd2-9c0b-515ed0e4b74c | -6.4903 | -62.8554 | 2026-10-09 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| db373d91-7623-3936-9174-d2066f02d7f2 | -6.0207 | -40.982 | 2026-10-09 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| d59d86aa-9eaa-3bc8-9aa6-6bba1b61417d | -2.499 | -56.0675 | 2026-10-09 00:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 9cbf2e5c-7afb-38d4-8023-d06eeeb6590a | -13.1827 | -54.3571 | 2026-10-09 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| c1143a42-d4b9-322b-ba11-b6b6504b18a2 | -4.5491 | -47.0328 | 2026-10-09 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 542d0a27-1ca9-3c58-827d-a517ab72013b | -9.2549 | -60.8863 | 2026-10-09 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ac1cd8b4-67b8-3505-a0ce-2b04381fbb98 | -3.1109 | -53.9249 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5d89ca57-c38b-318a-8919-effbe988f44b | -6.0262 | -53.491 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| cd3ab6af-f9f8-3f45-b95a-7b9549f92b3a | -3.6004 | -61.6259 | 2026-10-09 00:10:00 | GOES-19 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1441fc9a-6408-3799-9778-5f746d90df84 | -11.8692 | -43.5805 | 2026-10-09 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ff357937-0607-3ea4-bdc2-38ac5547dc1a | -2.7428 | -54.1347 | 2026-10-09 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 233e08ad-9c05-3f68-bbca-11b7c67063a5 | -5.7117 | -53.4862 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| cadc9fc6-a725-3028-944d-930ab082c3a5 | -5.7119 | -53.4658 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 61d62c25-d80b-3984-8c62-d91a37bab97a | -3.2057 | -58.8546 | 2026-10-09 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 9e83d2d5-0a58-3fbb-a09a-df94ba21578a | -2.7429 | -54.0945 | 2026-10-09 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ca882c50-79d9-38e7-bfab-299bed2ff48f | -8.8961 | -44.9336 | 2026-10-09 00:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 99b557be-da95-30b2-bdce-7bff730e2894 | -6.0019 | -40.9837 | 2026-10-09 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 260.8 |


[Clique aqui para ver as próximas entradas](README20.md)
