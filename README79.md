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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c37e2b50-3ba4-3cf9-83b6-b9906ecf4724 | -19.97988 | -47.62881 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1856fa3a-fb1c-36df-9653-d854dfe86703 | -19.23244 | -47.99779 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c930abb5-ded4-3548-84b7-bc3fdb4d2fd5 | -19.25351 | -48.00869 | 2025-09-11 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e04cc335-c2df-3496-9a7d-2cb9370a59a5 | -20.12706 | -47.68413 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7766a3bf-f2c2-3131-8abe-5e22f2b240b4 | -15.55253 | -54.76864 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4690bf74-ae7b-34f8-b55c-568a344c5f26 | -16.62319 | -49.78382 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bfbc996-fd0a-3d8b-9e93-c6daadb3d361 | -15.10949 | -50.14585 | 2025-09-11 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c07f2df7-5839-3bc6-acac-481fdf920b93 | -20.0 | -47.60962 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d98a0570-76e9-300a-825b-ec320e960a1e | -16.61182 | -49.78629 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2b5f4fa-2cb5-3a18-a170-f0e012af47c6 | -16.53356 | -55.181 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| eae57343-6850-3876-900e-186fd48d89b4 | -15.91011 | -50.19055 | 2025-09-11 04:25:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65fad869-1c0a-3ab3-912e-172bcd213782 | -14.2822 | -54.74981 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b34eedd5-4458-37bc-acde-be69afad3d9c | -14.8883 | -55.83858 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 915e2ffa-e450-37b7-a04f-014ca2adeae7 | -20.08844 | -44.48061 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ba0f1b4e-1672-36f1-8e1f-2b75b0c4a2db | -22.79468 | -47.80513 | 2025-09-11 04:25:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d085d091-d3fc-37fd-b761-237d143042fb | -18.93685 | -48.70941 | 2025-09-11 04:25:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aa87cee-4fa7-3c5f-b53b-04a1da364c3c | -18.84476 | -46.87119 | 2025-09-11 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e99da77a-bf84-3bbd-92e1-f894a0846d96 | -19.95947 | -44.15035 | 2025-09-11 04:25:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9c12c62e-4015-32ac-88a2-594531404665 | -16.6896 | -49.3299 | 2025-09-11 04:25:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a81ab3b-de7b-3bfe-b30a-7fded828d1c6 | -17.99955 | -47.10543 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8ad0b28-f50e-373e-b548-0683e3454cb2 | -16.28612 | -45.68506 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50ed574d-9e59-3399-86cb-6bda3c40ba11 | -20.08936 | -44.4785 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c93a1c09-9c13-3cf3-a682-07f3424ed0c4 | -15.5457 | -54.76527 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a66c0a4-9899-3955-9dba-10ca9eabcccb | -19.64876 | -45.047 | 2025-09-11 04:25:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c8e1ef7-badd-369a-b12e-161954d9fca3 | -18.01414 | -47.99769 | 2025-09-11 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7567619-d75c-3cd9-9288-9d8b19d4372a | -15.16385 | -52.43506 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31cf9583-f83b-3e30-bf42-27b821dbd7b0 | -18.06899 | -45.4313 | 2025-09-11 04:25:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 383cee8e-6486-31bc-86d5-9b683052eba7 | -18.56115 | -46.55969 | 2025-09-11 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d715414-8c30-3bde-8ffd-2e8a211fc128 | -21.43283 | -48.91199 | 2025-09-11 04:25:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd5600b8-a33f-3d3a-853c-31adfcecb86a | -17.56464 | -44.55199 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31e05655-64a3-3ad0-8a4b-3a7467e5351d | -20.51621 | -47.63316 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a1e4c45-6bc4-3c74-b1cf-d650f8905721 | -20.00044 | -47.62865 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67592111-47e4-3670-bf2d-de4782c28f87 | -17.26311 | -46.08772 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc1b12be-26f8-33a6-9f7e-078d330c5036 | -15.80093 | -52.24298 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1058ca05-b7d7-37b5-b0f4-90a513b8995d | -16.27993 | -45.68025 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffc33480-bca3-37b2-af06-078958ef54d4 | -16.40467 | -44.04889 | 2025-09-11 04:25:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2383ec7c-2dd7-31d2-86e7-ac4fda12a71f | -18.02587 | -46.87054 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f72fa93a-1b97-3c4e-9877-d823bca86f63 | -15.12307 | -52.42126 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a76ade55-6fef-357b-bbfd-fcdb42801604 | -16.06046 | -49.96733 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d82f15fd-3555-3d3c-8c9d-dbcbf0b18ae0 | -22.16107 | -47.68534 | 2025-09-11 04:25:00 | NPP-375D | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26f88173-003f-37ae-be02-f219217b9259 | -16.56933 | -49.73645 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fa56d6e-e800-3a13-b51c-27c6d003055f | -15.11098 | -50.07284 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18667f0a-e116-3126-b952-45158cc88697 | -21.91042 | -47.90767 | 2025-09-11 04:25:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40fc1257-b4ed-3e3e-873f-cd2f5997b513 | -17.2491 | -46.08911 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcb0ff36-5dd4-3226-890f-d922a0b5f7c9 | -17.5611 | -44.55143 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8647b36-1118-3e5a-b231-fb9c245486a0 | -16.28274 | -45.68451 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbd9a4b6-413c-3c86-9e78-18b48dcd88da | -17.90775 | -44.59262 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6278ac1a-395a-3e1b-86b9-9565e7f6997c | -15.80159 | -52.2393 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8856f00-5b8b-39fd-8d40-883ced9058dd | -16.06119 | -49.96309 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c859879-c3e2-362d-9e54-c0bb1f466288 | -16.60611 | -49.77703 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3960638-6081-3fa4-af1b-51519bade9c9 | -20.0032 | -47.63291 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e10b4560-6b69-3bc1-83e5-04b84cfb030f | -16.56988 | -49.73797 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cddeebda-4d3e-3458-98b5-ce448f0eba20 | -16.88539 | -45.75386 | 2025-09-11 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2841a21d-4081-3b1a-ba78-c7d47851c4fc | -15.12302 | -52.42268 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8026fc35-432d-3b36-9113-ba9ca92aabde | -16.62664 | -49.76371 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cbb7421-9df8-325c-800f-50f7e4933c94 | -15.5313 | -48.50095 | 2025-09-11 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 342d4247-5f35-34a5-962d-ff57c2e01db0 | -20.16943 | -44.61973 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8743e2cb-90ca-30d6-b5c8-06db0324e474 | -20.00262 | -47.63659 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e0360d41-9d7a-388e-b08d-8f68ad213a90 | -17.93885 | -50.54471 | 2025-09-11 04:25:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07c1a482-eaba-3d65-a26a-f6bb36805bc4 | -19.22794 | -48.00453 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff050d51-5d5f-36ac-85f3-f3c34e7edbf6 | -17.20258 | -50.15576 | 2025-09-11 04:25:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 192c74c3-704a-319f-bc65-fc4c66f1ff3e | -19.58088 | -47.06947 | 2025-09-11 04:25:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d94e27cc-9a77-3c2d-8e7d-13ecd21d7deb | -14.91369 | -55.87521 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce519dc5-6dfa-3cbb-877e-cc1e5f9d23fc | -17.47381 | -45.10123 | 2025-09-11 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d00db17b-0226-35a9-aefd-7f9e18469c33 | -18.00746 | -47.99653 | 2025-09-11 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 151484e6-fee2-3e42-b91f-6f693f94e2a4 | -21.43556 | -48.91636 | 2025-09-11 04:25:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7d24a2e4-e40d-32b6-b2ba-964f676b1a20 | -21.45858 | -45.14226 | 2025-09-11 04:25:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0f71e34-be89-32eb-8c30-b52a44afef29 | -15.80208 | -52.22677 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccd14296-c1c2-357b-847c-dc4f4e84bfd2 | -14.72746 | -55.61882 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d830d5f-915b-3105-9b29-6e3c6b1bdd61 | -18.34422 | -49.32943 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cac7239-1951-31bb-b8a4-a6527d16723b | -15.135 | -52.42701 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d0fc43b-d0ef-3547-b530-7c30720e8f03 | -18.28955 | -47.67345 | 2025-09-11 04:25:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f9340164-6a96-37ac-9abb-43ab8f2dc05a | -17.55757 | -44.55085 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53c992de-36f6-34a8-b7d3-be3c294ee5c3 | -17.82983 | -46.74042 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18cda137-4e79-352a-9a77-6e0afafb6bc9 | -15.17369 | -52.42867 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 098082ad-b8fb-3050-9751-55a9b7f3a35e | -19.75513 | -47.18574 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a08ec2a1-f0bd-33ec-9c72-f1b49e3f39a4 | -15.09929 | -50.07505 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d31287e5-a882-32f7-aa83-2ccb44eea18a | -22.31666 | -50.86597 | 2025-09-11 04:25:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba5e3d56-df57-3a96-9e9e-d278ecfca536 | -16.05627 | -49.88417 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe2d4e2f-6ff6-343a-85e0-e58f3f92d3ee | -15.79719 | -52.25295 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33940918-2eae-30d9-8721-2426df95be0f | -15.13074 | -52.42663 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7003ba6a-32e2-363a-8e1b-8162de47c67e | -20.12315 | -47.68723 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3f4c66c-3981-321e-930e-82809622762f | -16.28668 | -45.68136 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e80d919-5065-388e-a293-ba13663cbbb2 | -20.57653 | -47.68552 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 573eebad-5e6f-34ad-be10-cb0cc1da1aa5 | -18.40814 | -43.47884 | 2025-09-11 04:25:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5c8965c-907b-3abd-a458-123a19d9be06 | -16.64901 | -47.73296 | 2025-09-11 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 255fab28-fcd0-3abe-8830-017be5ea6633 | -16.62389 | -49.77974 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0496bd67-6875-35d6-8acc-aacc8589dde0 | -18.51061 | -46.38792 | 2025-09-11 04:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05e03674-e73a-36fc-9607-7245d88a859b | -15.98457 | -42.98426 | 2025-09-11 04:25:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ba1847b5-85b5-3e9c-9f5e-b0ddcb3ac542 | -21.3413 | -45.79396 | 2025-09-11 04:25:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8d2d0e81-0b20-3738-93a9-b78fb57c3803 | -14.5202 | -53.92908 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d3a03b1-6d90-3163-ae17-2ef0c310849b | -17.95083 | -44.48411 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0ae897c-c80e-3692-a529-3b87d93c988d | -20.91061 | -45.28576 | 2025-09-11 04:25:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 04e6e319-efbf-37b2-ac30-2f50f8f57c04 | -22.35395 | -50.88052 | 2025-09-11 04:25:00 | NPP-375D | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e94aa850-e282-3ecc-9145-1364ef0a11cf | -16.51238 | -55.1524 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aac2298d-acb1-37b6-9548-ece11c8d51d1 | -15.79951 | -52.22735 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 251e128d-7ef6-34b4-9704-65ebcc4c966b | -19.66831 | -45.84944 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c474f91-f914-382a-a84c-90642ef8b5ae | -19.9932 | -47.63116 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5345f9a-04bb-3e06-a082-59f530e7bf95 | -20.12648 | -47.68782 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9164bde-b1a6-3154-b50a-72708b41cebd | -18.60996 | -43.96453 | 2025-09-11 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README80.md)
