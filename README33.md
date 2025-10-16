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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f068cb5b-6371-3e36-94bb-1f40f0ee66c2 | -14.75252 | -42.38207 | 2025-10-16 03:49:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28220c76-d018-34b8-8d4a-824c0c316b34 | -13.80754 | -42.86044 | 2025-10-16 03:49:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b904de2-e844-310f-b4d5-8c9816b6fd35 | -9.15874 | -41.0584 | 2025-10-16 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4ac0a698-56fb-3685-a5cb-25d0c24436da | -8.46416 | -44.18447 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 307af309-b200-3768-92ec-4df07e19908f | -14.64493 | -42.5108 | 2025-10-16 03:49:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 21a44c57-76a5-34ae-9158-8d65f8eab3e1 | -8.46504 | -44.18696 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e24b6c4e-cf6a-3668-b9f3-eb8db0f81541 | -6.94688 | -42.68816 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a08d1073-3349-3435-9bed-4c56694a2da9 | -7.11157 | -44.72454 | 2025-10-16 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8405c549-aef9-3c02-a8ba-74a0ea32c5e0 | -15.8896 | -43.46452 | 2025-10-16 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91d24ce5-7466-3e3b-ad45-4325bad54b57 | -8.18898 | -43.32355 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 405b4652-d08e-3eda-93c8-624dafc9b54b | -8.2886 | -43.39918 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e248f8f8-3cdf-387d-8a07-d976e3a4ee88 | -7.18448 | -42.36421 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ec1be1f9-2387-3a05-9af9-634e40c35f4a | -7.29092 | -42.30259 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2c670a1a-4c81-32eb-8a8c-a5afa49d1d90 | -13.89687 | -45.57682 | 2025-10-16 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cee09d1f-17c4-3de2-a5e8-655233892333 | -7.07699 | -44.94862 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| febff716-9374-3059-af20-976009ce0e5b | -7.54127 | -42.06533 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18fbe758-ab82-384e-98df-73345531b985 | -7.56553 | -43.83408 | 2025-10-16 03:49:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18055e4c-3e21-3cad-af40-ea075d80655d | -7.94407 | -44.14043 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29d6da36-5a93-3745-9457-1f5f01069490 | -8.46978 | -46.24623 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 495f15d7-84c3-3748-9adb-14c314941c9c | -7.9279 | -44.13563 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6650b434-542a-354b-b601-6244dfc255f8 | -8.24037 | -43.41867 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 431ed04e-f785-3b61-97ed-ec44f0bd9f20 | -7.47868 | -42.13753 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfbd2179-29f0-363f-af9a-cb9ab03b46cc | -6.98821 | -42.79563 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4850a5aa-ea48-3c27-90b9-0598bc9b56e5 | -8.39254 | -46.25913 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f06c60b-ef9f-3303-915d-22e2ac6d4eaf | -7.68087 | -42.55891 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 72afa2f0-019e-3354-8773-c90909a4708d | -7.85491 | -45.40745 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b269a29-c802-35fe-a533-72f83252c996 | -6.59359 | -43.92083 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1da5a18a-8764-3e63-a9fd-929555517248 | -8.28497 | -43.39407 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7dcca554-3e22-312e-9f4c-b561dd3cc109 | -15.13038 | -43.6697 | 2025-10-16 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93aa1f67-4948-3b6d-aaea-97e735c9bb36 | -7.33843 | -43.8689 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff8e7346-0e81-31db-9bc2-58dc74a989f5 | -7.17808 | -42.19149 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ee93f8b-4a3a-3e74-95a5-b4ce8225df0c | -7.03213 | -41.81437 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da21a249-ae0f-3f1d-889b-f5c134afb52a | -7.35799 | -43.85888 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cd5a6fd-f884-38cf-a717-f9fada310448 | -13.63627 | -44.41872 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 854f1a33-e8e4-30e4-b0ca-9b2c4f277693 | -14.61109 | -42.3917 | 2025-10-16 03:49:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c6f8117b-a55d-33d7-9c6b-587f3c6c9586 | -8.46916 | -46.2496 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e02b7df-353b-35ed-a20a-0191231b8452 | -15.88994 | -43.46278 | 2025-10-16 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca7e2461-e382-31dc-be6c-fda842c908fd | -8.2936 | -43.42215 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f920bfe2-938e-3c95-b2b1-26d62d23cbf8 | -7.47673 | -42.76195 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 903810c9-4b4c-3292-a0e7-588c78154eaf | -8.46324 | -44.18951 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f9d7be01-3028-311c-a848-e7105534b196 | -14.59217 | -42.04865 | 2025-10-16 03:49:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5a871d7-10ec-3f52-81bf-d0650a579031 | -7.94528 | -43.26937 | 2025-10-16 03:49:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d1df8d48-4192-37e6-abde-97c122cc0992 | -7.29794 | -42.31153 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15220e80-fc4c-3313-be4f-259618dfc5dd | -7.40503 | -44.74596 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 35fc7c11-2b3c-3954-84ae-8dd2b801a98b | -8.25942 | -43.44012 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 109b4025-da17-304b-909a-b9f1eaabd005 | -6.75088 | -44.37166 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54e08352-f713-3fcc-ae6c-f9120473cd94 | -8.29318 | -43.40195 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c61cce67-ef2f-32e2-b4e9-af83f1db3853 | -6.9393 | -47.74287 | 2025-10-16 03:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a120a0ca-9390-33bc-9232-757fecfde7fc | -7.34934 | -43.86059 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 938134f4-6a17-3411-811e-90914462e4d4 | -8.29223 | -43.40429 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d861b8c7-3210-3518-9e68-f640bb83cbe0 | -7.16738 | -42.51389 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1c3b459c-ac3e-313c-83e2-31214687c15d | -8.39784 | -46.26029 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e4969388-2966-30fe-a113-4a9fdf2f0486 | -7.94117 | -44.12981 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f84e5008-b71a-3eb2-89f0-56ce985f7133 | -7.27684 | -42.94983 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6364b825-b4fe-39b6-9f42-be9f0a7e74b9 | -7.54178 | -42.71476 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a92e19e-1a0f-3121-9bca-66ce88404616 | -7.09493 | -45.27782 | 2025-10-16 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcf543aa-7b4a-36d8-aebc-82cbd99c582f | -7.93652 | -44.12899 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6b753eb5-42ea-394b-ad92-b2fada7ca6f5 | -14.12346 | -42.62235 | 2025-10-16 03:49:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c817e29-296d-3bae-b54e-f4c78b630b49 | -7.89533 | -42.95473 | 2025-10-16 03:49:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5075751c-f7a9-3a60-aad2-d3ad5ac6bbf8 | -8.293 | -43.39991 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ee617d3-b62e-38b5-bbbf-19411efb523a | -8.22984 | -44.02042 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eef5ee66-3814-3aee-862f-b9dc043271ea | -7.34852 | -43.8655 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cfe1fabe-9fcb-300a-877e-607adf7247fa | -8.27273 | -43.36244 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bc460d8f-6e36-35a2-bd73-190ef1e3d892 | -8.46384 | -46.24865 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcd099ac-3fe7-39df-9fbf-cad53d8cbb71 | -7.29026 | -42.30638 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f7aa3b4-4eeb-3c74-9d4c-79dbf4406f24 | -7.40117 | -44.75058 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0011e29e-8a95-3fa8-8113-1005066fc7ec | -7.09757 | -45.27777 | 2025-10-16 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3422aa9c-f24d-317c-9815-c18732844644 | -7.47743 | -42.75786 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 488c2f5a-91e9-3921-88bf-938198ab407c | -15.392 | -40.84332 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e0a06704-4e31-3f1f-9915-671d9d6c707a | -6.71412 | -44.38253 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d7eeb36-c32f-3dc7-82ef-a146d6059998 | -6.21776 | -47.04012 | 2025-10-16 03:49:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2167a590-1024-34d5-add5-b2486564a410 | -7.32173 | -39.26513 | 2025-10-16 03:49:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bb20098b-930b-3516-8866-31b660986f03 | -7.47094 | -41.51585 | 2025-10-16 03:49:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b067bf8e-26f2-3d39-9d40-b8d61981c39c | -8.20819 | -43.9822 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| db5956c7-19b9-3f05-884d-3701588565cf | -7.4824 | -42.75451 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| e6252bad-ccb4-3752-b6f5-d43ae651ee11 | -7.67599 | -42.56207 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22cb3bb1-a07a-3a8c-b0b2-85f195eb36a0 | -7.47952 | -42.74561 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ad9ee836-2acf-391d-b158-7bff50c59827 | -8.23331 | -43.32887 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ba1b733-1a3c-34d7-90dd-07cf359fb564 | -7.74875 | -42.49047 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a96e50f5-0b87-341d-82ab-aef6ebeef465 | -7.95337 | -44.14213 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7daf55ee-15a4-39aa-a8da-7089cc34844e | -7.05703 | -45.06125 | 2025-10-16 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e523cb5b-8b1b-322c-905c-86f9ef95115a | -13.6779 | -44.32568 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c48ba453-579a-357b-bd28-12d16e1890f0 | -8.26089 | -43.43151 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3fb43e9-4ab2-37a0-b2f4-1f2d3b22f4f8 | -15.78312 | -43.65171 | 2025-10-16 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 011c98d9-76a9-31ed-83ff-2d4f374f9b6c | -15.79741 | -42.02409 | 2025-10-16 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d8ad073a-9f52-3ac2-82f6-090efd9bc83e | -8.18971 | -43.31924 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| daea6bb5-751d-3abf-b426-4b1494dcf112 | -7.29977 | -41.96102 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b43f1586-cd5d-3df5-815a-90772165cd9f | -17.93284 | -46.73137 | 2025-10-16 03:49:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a08a6f21-83af-352e-8585-71f6901654de | -15.9676 | -43.01913 | 2025-10-16 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1060e547-2d73-345c-8f8e-15384fe0ed08 | -7.86054 | -45.97264 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d53a5cb-418d-3789-8b98-b8a017b29428 | -7.29509 | -42.30323 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 017eaba8-2d21-342d-a903-edd20ffc4830 | -7.46615 | -41.52022 | 2025-10-16 03:49:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5e248b0f-6640-3d25-af76-1b89dcd419ff | -14.18032 | -42.7383 | 2025-10-16 03:49:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0310e83-24ed-3d5c-b2fd-62977c1eca38 | -7.46576 | -42.67254 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50b6cc28-ba47-32ea-9531-56ef0c0fb2ff | -15.73553 | -44.62088 | 2025-10-16 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 882b578e-5e0b-39a0-b0a1-3e0b54827f32 | -7.84927 | -45.40968 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086da31b-7775-3799-9c84-2a011b80956f | -8.28952 | -43.39681 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a5a4b27-ff50-3dc0-9826-63a396167bdb | -7.6636 | -42.37752 | 2025-10-16 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4b949a9a-fac6-3144-b9bc-1fa9ac28b357 | -7.47743 | -42.14492 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 759be798-5372-3fee-a40e-da2ca6ae2af8 | -8.20445 | -43.97663 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README34.md)
