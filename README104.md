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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 026c9752-3952-37b7-b053-28b17ecdbd73 | -16.74795 | -45.77581 | 2025-09-01 12:00:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 419c1a98-500f-3902-ab8c-4f131a5baea4 | -15.58266 | -48.33852 | 2025-09-01 12:00:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e7bf6370-c56e-302f-914d-a6641c2ffd2b | -15.69172 | -48.9308 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 08b5809d-60f9-38b7-bdea-b6a3b4fcee2b | -19.49329 | -46.58646 | 2025-09-01 12:00:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 96196f7a-29b4-35f0-a8d7-444ab85b4742 | -19.71043 | -47.96542 | 2025-09-01 12:00:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a7bce5ac-656b-38df-8847-81109607a457 | -16.74964 | -45.765 | 2025-09-01 12:00:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| decb29ef-cbb2-3717-ada2-353117b5b203 | -18.07694 | -45.94773 | 2025-09-01 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aafaef95-e5e6-3350-b962-8b3302580869 | -15.73406 | -49.00296 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e367d4c4-a228-30f2-9477-12a01cba1568 | -16.05343 | -42.44422 | 2025-09-01 12:00:00 | TERRA_M-T | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0003a05e-b224-3ae5-91ec-7c1af4a1e999 | -15.61299 | -48.3497 | 2025-09-01 12:00:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5fa91976-1eac-3fbe-97c0-d4cc8b7b27cc | -15.59147 | -48.35777 | 2025-09-01 12:00:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 46.3 |
| cf40dff7-bf16-36a0-9c01-73073ae7753e | -19.15648 | -43.75357 | 2025-09-01 12:00:00 | TERRA_M-T | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ae2408e8-3750-3069-ac20-6f8dc78ffb3c | -15.7171 | -48.88319 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 370.8 |
| ff4f4c8d-99c0-329b-a30a-d1e02eddbd0d | -17.20774 | -46.06027 | 2025-09-01 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 41938098-2242-3503-9c81-b4e92d783c80 | -15.72554 | -48.87895 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 9b1662aa-4197-3ade-9e3d-a56b0995e62f | -15.71403 | -48.90073 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 34719ba2-c362-354c-9585-f516e5e93f74 | -15.71328 | -48.87736 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 118.8 |
| a7ee1324-3beb-3b5a-bf0c-8363c81f1599 | -15.69791 | -48.89421 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5deb0daf-372f-30c3-a28e-6a1a13cc8948 | -19.48175 | -46.59651 | 2025-09-01 12:00:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 4f9c4d63-507d-330c-a108-13a7816c4c06 | -17.85899 | -44.73172 | 2025-09-01 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9de3e865-4650-3bf2-ab18-330694e46223 | -15.7047 | -48.88237 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 22636c2e-9e05-37b0-b7c2-0ea42afa5e38 | -15.5841 | -47.91813 | 2025-09-01 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 6070e21f-fb99-3178-b196-df99cc8abe26 | -15.57975 | -48.35577 | 2025-09-01 12:00:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7f66268b-3b5a-3cd1-bdb2-5eb0e2ceab9e | -15.72262 | -48.89637 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 3d661b32-29db-33bb-8900-433014abf60a | -15.58568 | -48.32053 | 2025-09-01 12:00:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 033bbb4f-5edb-3222-a868-cf5ca0b42e20 | -17.85755 | -44.7413 | 2025-09-01 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 4c6d41bc-4957-36cf-ba1c-cd9254ebde70 | -18.81757 | -47.51834 | 2025-09-01 12:00:00 | TERRA_M-T | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 3390bed3-2968-337d-882e-32e58ee0dbdd | -15.68855 | -48.94955 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9b81e7d1-44e7-3776-8147-4bbcff7cda29 | -21.48943 | -45.31815 | 2025-09-01 12:00:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 3444a9e1-d7d2-3982-ad4d-515d586807bc | -15.71044 | -48.89426 | 2025-09-01 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 148.7 |
| e5c55df9-fa0c-3ac6-8d14-ce934f5abdb7 | -17.40191 | -45.06602 | 2025-09-01 12:00:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fc9e5bf4-092b-359e-8832-d3e0beb1baba | -17.51572 | -40.0255 | 2025-09-01 12:00:00 | TERRA_M-T | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 43.6 |
| 1884ffc2-c2cc-385d-809d-db435f92c833 | -15.58855 | -48.37521 | 2025-09-01 12:00:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f6813128-4087-3010-a114-82c0d8d1081a | -16.40797 | -45.65037 | 2025-09-01 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ea9c709-00be-33c7-be34-85fb787417ce | -19.48362 | -46.58475 | 2025-09-01 12:00:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 0af7e4b6-29f0-3071-855a-23c7a54cefb0 | -22.31766 | -45.87857 | 2025-09-01 12:00:00 | TERRA_M-T | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 41acd26f-4069-39e4-a155-ba67c5115660 | -23.16275 | -45.78582 | 2025-09-01 12:00:00 | TERRA_M-T | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1bf1dcae-2105-3063-871a-a1ea478be03e | -21.93757 | -48.40593 | 2025-09-01 12:00:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1b650d72-5593-38f8-b4dc-c47f7fe37cb3 | -23.35724 | -46.90445 | 2025-09-01 12:00:00 | TERRA_M-T | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 728dee88-40dc-3a04-8874-9cad8b5af589 | -23.30774 | -46.46916 | 2025-09-01 12:00:00 | TERRA_M-T | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 42265971-8f9f-3711-92ab-a834e41264be | -21.9353 | -48.4193 | 2025-09-01 12:00:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 15bb127e-4623-3ba1-9071-b64a83c7c6c1 | -11.3705 | -43.5868 | 2025-09-01 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| be5c806d-bd3d-35cb-9f70-ca2df44ad27a | -11.0568 | -45.146 | 2025-09-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 44c30127-dff3-36ac-a133-cd8acfe29dba | -6.7626 | -43.7881 | 2025-09-01 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1760e91c-0999-3a6d-b92c-19402df4413d | -6.8426 | -43.3385 | 2025-09-01 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| fc0be47d-35af-3e76-a6d8-2d3e4afa64a8 | -7.0757 | -44.3606 | 2025-09-01 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 9089ac9a-2b50-3b1b-baf4-1ba405a9d487 | -6.7438 | -43.7898 | 2025-09-01 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7788e40c-652e-35e4-a1bf-0195db096c34 | -7.0948 | -44.3358 | 2025-09-01 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ff5e7e82-8069-3e6e-8649-456fb8ade687 | -7.0572 | -44.3393 | 2025-09-01 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1a663b5a-0366-3f06-8bdd-25ae674a895e | -9.1567 | -45.2243 | 2025-09-01 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ca7e1fc9-4cfc-3c4b-a4a2-576de2e42b59 | -11.3709 | -43.5631 | 2025-09-01 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 32a0d4e7-17a7-3b07-939c-a0eebac572c1 | -12.9768 | -48.1049 | 2025-09-01 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 7247e59f-752e-305e-badd-13cb9d45e710 | -7.9539 | -46.4542 | 2025-09-01 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| ebabdeb4-d9de-3470-9532-7a78975eefe1 | -7.076 | -44.3376 | 2025-09-01 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 222f87a6-0277-3e94-993c-32d213a14654 | -11.0377 | -45.1487 | 2025-09-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| d673939e-3074-317a-bc1a-6cf38b46e690 | -8.1943 | -46.788 | 2025-09-01 12:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 8bdc9899-959f-3778-85d5-a7e80788737f | -8.8437 | -47.5217 | 2025-09-01 12:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 432e9342-ef97-3481-8c1c-f5e931436b93 | -7.0946 | -44.3589 | 2025-09-01 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 01dcb035-e418-3182-a54f-a0dd1e7d1723 | -8.1945 | -46.7657 | 2025-09-01 12:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| a63b512b-2e59-3f93-8e3b-138fe45c5c85 | -6.8428 | -43.3151 | 2025-09-01 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| e50aba36-b47a-37fa-8c0d-9ea98e432cb6 | -6.7992 | -45.6815 | 2025-09-01 12:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 93526db0-07dd-3cb5-965a-aad118666c09 | -11.9623 | -45.8428 | 2025-09-01 12:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| d077e978-a6ba-354d-9f94-77c778a34aaa | -8.8437 | -47.5217 | 2025-09-01 12:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 74490a6c-6586-3d92-a825-0b588e524d9d | -6.7628 | -43.7649 | 2025-09-01 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 0d4b5fc1-552a-3311-9875-0b15e710f3ee | -7.9351 | -46.4559 | 2025-09-01 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5f4e6b36-5e20-3c07-aaf9-71c1e3fec1ed | -9.2258 | -47.1066 | 2025-09-01 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 62a70660-f830-3324-b167-df9907447ad4 | -6.8426 | -43.3385 | 2025-09-01 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 0ca8cffb-c0dd-357b-bc66-1d06ba632bbe | -12.9768 | -48.1049 | 2025-09-01 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3e835f5c-7d79-3e46-9d8b-eac7feb29320 | -7.9539 | -46.4542 | 2025-09-01 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| a691a453-855e-30c2-a121-1499b456bceb | -8.1945 | -46.7657 | 2025-09-01 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c1db2445-5d5f-3552-b99f-17d7189b9a34 | -11.3705 | -43.5868 | 2025-09-01 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| eef52111-7bae-3a28-916d-dc9f6559e2f1 | -6.8428 | -43.3151 | 2025-09-01 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| ef367d3d-3309-3dc2-81ee-a59403fe2931 | -7.076 | -44.3376 | 2025-09-01 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 958349ae-f00b-3f33-bfc9-7e2973b2d0bc | -11.0845 | -44.6343 | 2025-09-01 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| a7cb0442-1f5a-3d35-ac1d-19ebb8b434dc | -6.7438 | -43.7898 | 2025-09-01 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 212.1 |
| f1b33059-4c23-35ab-9f89-110a506110fe | -7.0948 | -44.3358 | 2025-09-01 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| cccdac9e-6a7d-3a0a-8e93-88123d294198 | -8.1943 | -46.788 | 2025-09-01 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 715e190e-4b69-3942-ac67-9afbec240d9d | -6.824 | -43.3168 | 2025-09-01 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 6af17f97-7035-3e1f-8d47-f1432252515c | -11.0377 | -45.1487 | 2025-09-01 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| b997790f-0c4b-3f07-ba62-4d5f69a0c226 | -11.8527 | -51.4742 | 2025-09-01 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 4bd58e16-1f14-3093-8608-6c0bfc292ca1 | -6.8237 | -43.3402 | 2025-09-01 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 75f4ef61-f6b7-397d-b5c3-e26cfb7b54d6 | -11.0568 | -45.146 | 2025-09-01 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| c8cca44f-6c2f-3949-ba93-0717f4fa7bda | -7.0757 | -44.3606 | 2025-09-01 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| d79efece-1dbd-314e-92f6-2e5752ef2f36 | -7.0946 | -44.3589 | 2025-09-01 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 230bb492-5c6f-3db7-80cc-e64f9ddb2c78 | -11.8524 | -51.4954 | 2025-09-01 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| bd81f441-1c76-3ea7-89d6-f4591272ad1e | -11.3888 | -43.6312 | 2025-09-01 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 51d86b74-d21d-38b4-a21e-9867088e1303 | -6.744 | -43.7666 | 2025-09-01 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 1c6c0798-465d-3207-96bf-eb4051bb244c | -19.4813 | -46.6005 | 2025-09-01 12:20:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 4ae37fac-e650-34ae-960b-0a61276c1c5f | -6.7626 | -43.7881 | 2025-09-01 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 1887999a-a46f-311c-86d0-a0fa1cec9a8c | -7.0572 | -44.3393 | 2025-09-01 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 3d41ca58-58ea-3bcb-a410-5ffce63b3975 | -7.3992 | -47.4333 | 2025-09-01 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 441ebd8f-ad2d-33e3-9712-60830af6ce94 | -12.9764 | -48.1272 | 2025-09-01 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c0e51ae5-ed76-38b1-9875-d652137fdf10 | -6.1665 | -43.3273 | 2025-09-01 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a4c77484-5821-3973-9274-13cc6ff37988 | -7.0757 | -44.3606 | 2025-09-01 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| ba41ecc2-7a7e-3969-838b-3546c1e2144a | -6.8428 | -43.3151 | 2025-09-01 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 0ca5a545-f07c-36c8-b737-bd70eea194d4 | -12.9768 | -48.1049 | 2025-09-01 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3d3d4fb3-972e-3810-9bc1-35d318fdcad0 | -6.8426 | -43.3385 | 2025-09-01 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| e86ab89b-ef97-32bb-adbe-d6430dd23845 | -11.9623 | -45.8428 | 2025-09-01 12:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| b97ffcda-44a8-3a64-a80a-742d6663939d | -11.3701 | -43.6104 | 2025-09-01 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 91d75444-2cc6-3342-b348-583b1bf33af1 | -15.7116 | -48.8809 | 2025-09-01 12:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |


[Clique aqui para ver as próximas entradas](README105.md)
