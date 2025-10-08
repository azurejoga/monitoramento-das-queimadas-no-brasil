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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40f83542-d6c9-30b5-9596-e2794e40dd73 | -14.39538 | -46.02977 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5d09470-bef2-306b-87c3-774496681ec9 | -7.4841 | -47.15633 | 2025-10-08 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8be2efac-de8c-3253-8d11-872f23ba160c | -13.33757 | -48.02047 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae7c105-0449-335d-8d48-3d939bc51080 | -14.90794 | -46.82132 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efa0bca8-7ed5-3b44-ba93-f5843a3d7cd4 | -8.22261 | -46.83471 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f15dc58-2fed-3cf9-8916-cf4963ad9025 | -18.05179 | -44.44975 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f660c8c3-f44a-36f4-a1f3-bbdf708f164a | -13.22191 | -51.71004 | 2025-10-08 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57321f45-4512-3b80-8311-b612e19cba66 | -8.18527 | -43.33617 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 7484907c-59c5-3ede-bfee-d54b6ee2b9ca | -18.03065 | -44.96146 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6407c1d6-22b1-384e-957d-0672b0473a00 | -17.28843 | -42.65126 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0eb061a-e29b-3adc-a713-d5cfc264a92e | -15.40182 | -47.99746 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3edf919-7894-3c6d-a024-b44ec5966366 | -14.69095 | -48.41261 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9b60327-fc4e-372d-8667-edc4d8db2ea7 | -17.73207 | -44.37645 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2692cca2-6500-3665-8537-b5e9a23113ad | -9.18214 | -47.79547 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c3eef38-0a51-3b1f-9abf-4e9524c72b13 | -16.34205 | -47.04654 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0257acf9-4a4c-3ab7-82bd-2d66d0dd56ee | -8.68031 | -44.729 | 2025-10-08 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27fa59b2-f9a3-3a4a-9ebd-0cd5de81dfba | -14.79852 | -41.62892 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2506b31-5042-3ed8-8eea-e703d9cf55ce | -18.42138 | -45.21065 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8953faf-07b3-35c2-9be5-d375c5de8b9f | -8.93091 | -46.59463 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bfa15e6-56a2-3ed2-a0f0-88a84ddb2c6a | -8.17306 | -43.32708 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7888b764-3e5a-353d-b358-bbd7e316f0a2 | -17.57548 | -46.05882 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 77cd5e58-cb6f-3132-8ade-cd4402fd477a | -19.46828 | -43.89291 | 2025-10-08 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f498000b-9809-36a3-8983-4617d9f5d628 | -18.50371 | -43.89965 | 2025-10-08 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c059bbf-627c-31b9-a36b-53fbf0e6c42b | -19.57879 | -44.64932 | 2025-10-08 04:19:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a7d9a1e-a13b-3ffe-92cd-f9f967a8240b | -7.71226 | -44.68793 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a3e4438-34b7-3b70-b9b6-3466d96a8ff0 | -15.36446 | -47.29581 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0c71033-86c1-325a-ba6f-23d60f0aa061 | -17.93951 | -57.53417 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e5020633-8054-38fd-938a-aacd2686c4c2 | -9.18135 | -47.80018 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 265a258c-fdef-3d5c-8457-882f0a77e6a3 | -7.80718 | -44.22545 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a40a5b74-23ad-3412-b708-021df7ec8166 | -15.37199 | -47.32389 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f615057-814a-3ca2-9fdb-b25d56a8d778 | -17.86863 | -57.65292 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ff42dec6-5c04-3f6f-832f-ab5756dc8b64 | -8.41401 | -46.80648 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f05f1dbe-4cea-3daf-980b-0dc26c0662dc | -17.82562 | -57.64511 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 54664319-0c6a-3072-b2c4-b6d5920d38cc | -18.34674 | -42.39062 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3138bb56-bc03-3f53-85bf-4d44bf75bf76 | -18.4062 | -45.20791 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bab50417-5abb-3b77-8d35-d693da02d073 | -19.51516 | -44.06773 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82efd422-7896-3735-8ff8-3b5e3f9da9f0 | -14.91179 | -46.81755 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e85a171-ab66-3c74-b503-7269a523cba5 | -15.2559 | -46.36349 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebd403c2-8ba9-352d-bd3c-9700fd73e473 | -7.79328 | -44.20519 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53dd7617-9de6-3063-8bdf-245e0b6454d6 | -15.36967 | -47.32871 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4af4c873-9bc3-3795-b9fb-2c5870b6526f | -15.38391 | -46.28337 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86d56e4d-403a-394d-9bea-0a0304c0490a | -14.39478 | -46.03342 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c347037b-efa5-3c0a-8b1c-50ee3528390e | -13.80616 | -45.80478 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b90d6ad9-10cd-3b18-a1bf-678786ee330b | -15.62959 | -52.57581 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6512309d-3284-341a-a42f-f52b16dc3b82 | -9.39688 | -45.95422 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86dc273a-48eb-3dd0-83a1-420663b7cb63 | -15.31333 | -46.15892 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a69e9d05-95e1-3cfa-9331-8eaab151254d | -9.17521 | -46.9208 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8bb9573-9c26-3167-a0ec-aa8ed4838bac | -8.62033 | -45.09979 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49af6589-1f6d-3196-a3cd-a5dd1753cb5b | -14.71696 | -46.02806 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a03491c-1f75-33f3-9bdc-cecd3c88980d | -15.65033 | -43.67238 | 2025-10-08 04:19:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7100acf7-0ff8-3b5d-84ba-c145c777693d | -8.11439 | -44.77413 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28ed6452-781c-31fe-9d14-9cde69fdb377 | -17.277 | -58.11976 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f478e758-80b4-35d4-a2ff-894f2e66e892 | -17.97919 | -57.49629 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 9417cae1-f91b-38a9-89c4-271d964511f6 | -17.84931 | -57.59487 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dcb5fd65-f20b-3c54-9b64-d787bbef52b7 | -20.29949 | -48.51236 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdff7d29-40b7-37d2-996d-032d3c996627 | -18.05347 | -57.53368 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 933c5bde-45d1-3d8a-b781-3d38a1bc712d | -13.76961 | -45.8063 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27c8bae0-b7b8-3ae6-9166-fb0f044c2e30 | -7.79884 | -44.21329 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e89cfba-4935-33f8-9f11-b76b90b775cb | -13.73117 | -45.70336 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a32c8647-f877-387f-8c60-be859751c700 | -7.77156 | -44.19099 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f335daf6-cdaf-3d2b-8117-2f714b82f2ff | -18.27463 | -45.40455 | 2025-10-08 04:19:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e89aafb-9168-31a8-b03c-ed2087443661 | -21.27842 | -45.80827 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ede5909a-0127-3f86-a0f6-19f5cb92b4d5 | -15.40251 | -47.99341 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 307237ed-790b-32c0-8390-15e944f748ea | -7.79761 | -46.02242 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a06a852-baec-3040-9744-af894915f77d | -8.60468 | -48.2504 | 2025-10-08 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08a6aa1e-bf76-3c06-bed0-1d17d977aedc | -16.29072 | -45.24582 | 2025-10-08 04:19:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d8b37e2-b1a3-3b6e-b0c5-602b930903b5 | -15.3216 | -46.17167 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f5e5c080-af83-3f85-bc30-5f0daeb9f24c | -17.97936 | -57.49763 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0efeae65-4855-329d-94f8-8b567f765ef0 | -16.01066 | -51.05189 | 2025-10-08 04:19:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae95d58e-a0b2-335c-a7af-6d78b15eb2b7 | -17.97029 | -57.50819 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6465d261-54b9-336c-a589-504d8de5af1d | -14.74908 | -47.8609 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf4902b6-e751-3fec-8171-db08ba7ed7e9 | -14.56275 | -47.00072 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b967821b-b875-3cdc-953f-51e96092bfed | -8.22478 | -44.1948 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4febe17-2743-39ef-9a28-6c00d98309c8 | -17.99871 | -57.49579 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 676cd6f9-fce3-3f5a-8e83-101420120109 | -14.52599 | -46.63634 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4515240a-e74f-3616-ae40-94ce56066b6b | -15.25317 | -46.35905 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4b439b7-73b7-396b-a4d3-f2abcdafec1d | -17.83848 | -44.33917 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7fe1841-2464-380f-bfb1-038e723d02ad | -16.62813 | -45.42417 | 2025-10-08 04:19:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 701920aa-5963-323d-8fb6-cc075e026eec | -13.35695 | -47.77797 | 2025-10-08 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c54a5f0-c5b8-3294-8898-4bb3aceed4ff | -17.84131 | -44.34345 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c20a0de-7f07-3cd1-8d68-c1a5d5ed432c | -14.90235 | -46.85542 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20ba877b-9986-34f0-b0ca-bfbc3ee5f663 | -16.33401 | -47.05285 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26c3d76c-9106-340f-8f91-475e41839cfb | -7.58338 | -47.20861 | 2025-10-08 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c3b3a75-738e-3991-b031-b00d97058013 | -8.19125 | -44.1104 | 2025-10-08 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26493edc-1b81-31f8-88b7-5fac585833f3 | -16.34144 | -47.05027 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ccd0259-d666-33ce-9dab-d80ed4828be0 | -15.06376 | -49.49113 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f52f1870-e7cb-3233-9752-04187d85b915 | -13.32224 | -48.02256 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69bff251-ec12-3468-b5d5-adfe38f47c54 | -15.70116 | -47.51207 | 2025-10-08 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2fa55ebf-e851-36f2-8339-f45d69839c8f | -7.79385 | -44.20168 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f94e1d19-5961-3759-921b-fc85b5a9589a | -15.29099 | -56.92278 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c3f14fc-f711-3501-a646-a1f90c198006 | -13.73698 | -45.66741 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9d56eb5-83bc-3142-bc64-fee30fe0b1c8 | -18.3601 | -43.58487 | 2025-10-08 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| faaa8377-8bdb-3302-86af-90daade13c07 | -8.60075 | -48.24974 | 2025-10-08 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e13decbd-4b2f-3c02-81b1-9e496e9fa9b4 | -17.83423 | -57.63541 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| a3fa80c5-28bb-3aef-8456-711a41d70a0b | -18.05265 | -57.54156 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 506b2109-5414-3256-8904-0b2aab142568 | -17.8263 | -57.64227 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| ad3e50bd-6907-3900-acb7-8793d6319231 | -18.40285 | -45.20735 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc092b57-c873-39b0-a63d-a031e7512e1b | -8.67295 | -43.90777 | 2025-10-08 04:19:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 466fca32-a9e2-3bd3-a12a-9b5a6a659036 | -18.50953 | -43.89519 | 2025-10-08 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9db6eddd-828c-3839-8c1b-8be6b530a326 | -13.35768 | -47.77374 | 2025-10-08 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README55.md)
