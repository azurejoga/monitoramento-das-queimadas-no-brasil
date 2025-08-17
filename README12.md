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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de047f61-9dda-3865-8f85-3fdadbb3c1f2 | -10.84022 | -45.32278 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8df5bf93-3211-3bea-99c4-aee3e616f433 | -14.36583 | -47.04662 | 2025-08-17 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0684afeb-0499-322c-bc99-06d5cf187332 | -11.9027 | -43.42715 | 2025-08-17 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 960baf00-eba7-3a73-a1c8-84bab8d3c8ff | -10.83695 | -45.36239 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 466b5c78-1525-352b-a8a8-0956f301409e | -13.43749 | -45.88709 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 95d3e939-e66c-32e2-a85a-51fb57db7a24 | -15.53092 | -42.34071 | 2025-08-17 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 574f83ac-4be0-3323-b4da-8a799e3613ee | -13.60234 | -47.75027 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a09ddef2-de54-39e7-aca4-bbe3a8ec1741 | -14.1902 | -45.32393 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 604ef58b-e14a-381a-b0ec-67410f291894 | -9.69576 | -46.2639 | 2025-08-17 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e374df7e-0e67-3a61-b20e-f817c820a938 | -13.59347 | -47.76723 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79536889-cc8c-3a3a-bc6d-00466d036890 | -12.87408 | -46.07838 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1704830b-f8e4-3bdc-b55d-47ae9b391f8e | -12.19225 | -47.23273 | 2025-08-17 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 837510df-94fe-3903-8105-a9d556996cd7 | -15.5346 | -42.34142 | 2025-08-17 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9276701c-9303-34b9-a71e-6d3ed8c96ef6 | -14.54739 | -48.59489 | 2025-08-17 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a019633-e4ea-3483-9ada-4f7c7fbbf5c9 | -15.14976 | -48.7624 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d00dcbc-141d-3b88-a61e-bac5eaaf0726 | -10.84073 | -45.36879 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2a3d367b-b8ef-378e-8ec8-8f514f26ceec | -15.18671 | -48.77963 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75f20663-c8b5-37ab-9be6-de98ac66e571 | -14.18848 | -45.33328 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ccb26bd-c173-3bd6-9ac5-60b7fff7d88c | -12.61007 | -46.90903 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7519ec63-ea1c-3926-9a88-44f257a5272a | -13.65101 | -45.90049 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47bde87c-88e0-3177-b996-98a87a9ec387 | -11.90202 | -43.43098 | 2025-08-17 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a42544e2-fa55-3262-9d50-f94f94fa5f6d | -14.9393 | -47.06 | 2025-08-17 03:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa58cc76-5088-3ba5-b860-706fa02ba251 | -11.65272 | -46.66291 | 2025-08-17 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62fc0c52-20ff-3409-a199-901a07257fab | -10.84507 | -45.35109 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1f83ab71-677d-39c9-a3ce-1e0de824a445 | -12.61589 | -46.9067 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 472ebad9-0954-32dc-a412-b8dfb3fab251 | -10.84657 | -45.36416 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5cfcb00e-52fc-30aa-a505-136d8cc2b69b | -13.4432 | -45.88284 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5f80e95-81a5-3d30-885f-e372371fdf5e | -15.17725 | -48.76939 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2aa09c82-44d2-3ad9-9def-f89f3e917091 | -10.85922 | -45.32288 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5aff9de3-0bc6-3241-beda-da94fad5697c | -9.7657 | -48.75144 | 2025-08-17 03:51:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f95fb72-e348-39fe-982d-9b1c36611155 | -13.60894 | -47.74496 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f48188e-1f5a-3af2-bae2-c9ca10043c37 | -14.19386 | -45.32948 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5e0a713-9b3c-342b-a151-7c2cfe2d025c | -13.58434 | -47.78547 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00be2f27-e83c-3bc9-9460-35106a09bbb3 | -16.49432 | -45.11282 | 2025-08-17 03:51:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99c7438b-a3b2-3a57-9dfc-d50c3685e383 | -14.19471 | -45.32686 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0abb2830-1587-35b0-acc7-918ce5ef44f8 | -13.42994 | -45.89771 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23fff303-4e0b-3aca-a125-bf6b4f118b8b | -13.58586 | -47.77768 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05eedf35-ff5e-3e6e-8c98-167df4353c9d | -15.53171 | -42.33622 | 2025-08-17 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd4566cb-c21b-34ac-a61f-fe6fc4e6f8c8 | -12.5548 | -46.94322 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8aa40bad-c889-34b0-8070-7f2e134a3ee3 | -10.84291 | -45.33058 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1455fa54-90a0-3b0a-9306-350d05144cbc | -14.1874 | -45.31373 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 469b3e5d-c44f-35c3-8296-1548a5685e95 | -14.18931 | -45.33061 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da333b61-44f8-3e5a-9e04-4b29e38da78d | -15.15058 | -48.75846 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36240f8a-0197-3dae-9b6f-34da8cff3a63 | -10.83928 | -45.32805 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e07a9d94-4da8-39b0-a256-e33c7fb2b83e | -12.13097 | -47.90528 | 2025-08-17 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c4edc0a-a089-3067-8819-a5567641e361 | -14.2024 | -42.78451 | 2025-08-17 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c21ab76a-b7f7-3471-bbd3-b293519f4a19 | -12.13495 | -47.91444 | 2025-08-17 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f9fee7b-4515-33eb-b5b1-c257eeb68650 | -14.18934 | -45.32858 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b3d1786-a070-3175-ab20-a8fb128ba335 | -13.01891 | -42.32639 | 2025-08-17 03:51:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 63cf725c-8149-38a3-aef2-533371305212 | -15.14345 | -48.73719 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a36e0632-cc08-30bc-b868-0ec3be7ddfb7 | -10.8391 | -45.32439 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 31ec03dd-30c9-3449-9b2a-1e58f29d8941 | -14.58712 | -47.95079 | 2025-08-17 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63de3214-576b-34aa-abdd-a309ded123b1 | -10.83812 | -45.32965 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cdcd9025-dc26-374f-9c13-2ca5a3f3daf6 | -10.86301 | -45.32921 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dd70245c-0f7b-319c-a740-8e615487bada | -15.14385 | -48.74221 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db1ba7d8-76e8-3109-9f82-5bc3d2bd2632 | -13.8752 | -45.5479 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5009d575-bd7b-338f-a4d4-b7bcb7f20f07 | -12.45133 | -47.00357 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c14a308-c71e-3e13-9e4e-e261c9446805 | -15.68619 | -43.20859 | 2025-08-17 03:51:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d9c7c75-fa2a-39ed-a2b9-2eb9a41ea7a0 | -16.48927 | -45.11614 | 2025-08-17 03:51:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2c15184-f52b-38cb-afa3-69202c8e4f2f | -14.18747 | -45.31578 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eef074ae-5c1f-3adf-a9c2-d41d6d22fa50 | -9.69544 | -46.26393 | 2025-08-17 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 478b95ad-f07d-33c4-af82-244a6ce9e185 | -16.49005 | -45.11195 | 2025-08-17 03:51:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39ae7353-73a8-338b-9890-ccab976ab2e4 | -9.69633 | -46.26072 | 2025-08-17 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ab2446c-2d73-3092-b13d-d5f88c47f395 | -12.55 | -46.94027 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 354b8a4e-527c-307d-b506-b6a717cfb550 | -10.84217 | -45.33959 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65e8922a-f6ef-3d10-b588-698ede3ae70b | -10.84556 | -45.36956 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6c4c6719-d95d-388b-bd40-23e67aad5f9c | -14.36525 | -47.04961 | 2025-08-17 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 579bc1d7-08e9-3a3f-aac1-fba39e5a838b | -15.86155 | -50.19387 | 2025-08-17 03:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd34873c-dd2e-33b5-9629-b255b0e75574 | -11.09575 | -44.80848 | 2025-08-17 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46a8541e-6d25-3d9a-8d30-1e43f31e3881 | -14.93434 | -47.06476 | 2025-08-17 03:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6432909c-bdf5-3edc-82db-5a214f2a54a1 | -10.84092 | -45.34118 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b380718-51a1-3a41-b2fa-5fccd50a34d7 | -13.61458 | -47.75743 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76227f64-4ec6-3494-b64b-7bc159ced9ca | -12.62008 | -46.91265 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb4f6ff1-880e-3a76-9c31-b19844d3885b | -15.76297 | -47.80392 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30ca8329-7e83-3cb5-8689-ca552846d9ab | -10.84121 | -45.34491 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c778d61c-f63b-33cd-b4c1-f0b21d6be5d7 | -13.87979 | -45.54889 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 327296ef-2246-333a-95ee-5fd6047b00f6 | -14.1902 | -45.32596 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b328c03-02ed-3bca-b20c-4f91352a113b | -10.85553 | -45.32032 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54062292-4ce9-34dc-ac28-7efd9fff7815 | -10.84026 | -45.35021 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f5415211-1a05-3e2d-8b0e-dedf1f3adaf6 | -10.84696 | -45.3405 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1b4b6532-4dcb-3892-b038-fda608e8dff5 | -10.85823 | -45.32822 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8ec6cddd-0453-3c67-bf3c-6bd25f67bc6a | -13.61677 | -47.76194 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c2ff41f-cfca-3f3d-8148-45c04b1a5733 | -12.81754 | -45.9907 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f94f782e-38dc-3331-9e03-5aa9824dea9b | -13.56721 | -46.9906 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd7c0ce8-514b-30cd-b52d-39f95fe0284c | -14.18841 | -45.33531 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4635bb84-a2f2-3f42-a021-43b7465bea38 | -13.60635 | -46.89856 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52257c51-f455-37dd-8652-d8ee27716e72 | -12.13577 | -47.91024 | 2025-08-17 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b603743-9b65-3712-b82c-ae860e77cf5e | -15.14463 | -48.73835 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc9b492c-66cf-3eb1-a886-8ededc7cd184 | -10.84317 | -45.36172 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 06cd6ef0-5b69-3d27-b749-0e055579d115 | -13.43081 | -45.89654 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9b3bb77-ada3-34e3-b96a-30fd9e0f9498 | -15.17801 | -48.76567 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de16c322-cc53-31db-96dd-8314ad407fa7 | -10.83712 | -45.33496 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15007e97-363e-3bb4-84ae-8985e13f9471 | -15.13837 | -48.74075 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0e91772-b657-3ea1-99dd-30e414815b3c | -10.82874 | -45.33149 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de003ad7-8e1c-3fb0-a1c1-91e69bd03587 | -15.63984 | -48.12018 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab23a485-4331-36ef-97e7-146661b48124 | -12.57252 | -47.04865 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55252fc2-eb0c-30c2-8641-c59aeef01bfc | -13.61002 | -47.75244 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac2211a4-f3b6-36b9-9931-cc76a0153c18 | -13.60566 | -46.90207 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4634aac-895e-3459-b025-c3b60d53720c | -13.61159 | -46.89866 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa8773b0-abe4-397a-b1e7-199a86852838 | -10.84473 | -45.34735 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |


[Clique aqui para ver as próximas entradas](README13.md)
