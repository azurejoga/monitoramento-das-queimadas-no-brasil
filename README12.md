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
| 139ca0e3-d0ce-30c6-9a86-b62a08d7ccc1 | -9.3997 | -48.44695 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b47a2ff4-3179-33a0-9ee4-4091421f80f1 | -10.4673 | -47.95094 | 2025-06-07 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77fcf1d6-e780-345f-b8a2-75b4db3a4cc7 | -8.74279 | -48.0335 | 2025-06-07 04:21:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 634f40e6-558b-30f5-b75e-d4b34395211b | -7.73711 | -44.16508 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a524d865-c547-3749-b522-108a0f1b33db | -6.95511 | -42.91033 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c2425c37-f297-3abb-9d31-aab04706f8bb | -11.81996 | -44.26539 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e6e5438-c1f8-3770-95da-b482520cd535 | -7.85832 | -45.17686 | 2025-06-07 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6872d20d-5842-32ef-9236-ed5a5dbc13ae | -6.94659 | -42.80511 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4ca5217f-12ad-3de7-89a8-ab40ee2d41bf | -7.19075 | -46.22918 | 2025-06-07 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8664b18-c6ad-3767-95a7-d78222c2b299 | -10.497 | -53.66695 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2bb400f4-8e7b-34ee-ab42-9fe10f67abfa | -9.07203 | -47.14602 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 994a50a9-864e-31b8-8e0c-dc65eb593245 | -10.87709 | -54.30479 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a42d4d9-15db-3628-8e1e-65ace68cd384 | -7.72706 | -44.16354 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 71f69c42-e9e4-3990-b56a-816813a42cfb | -6.94823 | -42.90925 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 40110052-745b-3313-a781-6d8f1128cb76 | -8.87391 | -50.18248 | 2025-06-07 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 683c9d3f-890b-3805-9658-c85da67b9efa | -5.6483 | -43.70654 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92403fb0-c55d-3554-875b-0b3e30c853aa | -6.30809 | -48.48799 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b32a91c-2ff3-3f69-99df-273a3deac1ff | -6.94881 | -42.9055 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1f88399-47b5-3701-98cb-f957f21bd40f | -10.49905 | -53.65599 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 525df9e3-d414-3fe4-9b65-ce31e4e5feaf | -8.44886 | -46.48604 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24e55391-88a0-3f2e-9169-7e374e2b7c2c | -8.21269 | -48.97945 | 2025-06-07 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cc51106-f9e8-3784-bb3a-8abb34530eb6 | -6.80701 | -41.7412 | 2025-06-07 04:21:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e557cabc-26d9-3c41-80cd-ec4987b0371c | -6.29381 | -48.50082 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0699e5e1-bece-363b-b228-0d6c7e623ce4 | -10.43682 | -48.81155 | 2025-06-07 04:21:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a171963-9586-3306-9d25-0f923c4921f8 | -5.92488 | -45.52514 | 2025-06-07 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c632b33f-e291-359b-863f-79c86bf4b675 | -8.45224 | -46.4866 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8189eefd-92ed-3c2b-abe7-e1f21cec0a98 | -11.78038 | -47.40071 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c76a132-259e-3918-aa0c-740e77760ddb | -10.64626 | -44.48822 | 2025-06-07 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0e7b396-7e12-3b1c-b7b2-7f38677fe911 | -7.73155 | -44.17873 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b0d49530-f323-31fd-9f7a-004befb3091a | -10.65771 | -49.36179 | 2025-06-07 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9f5f949-9901-375f-99ca-20199135bc84 | -6.30245 | -43.65308 | 2025-06-07 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a39aabd0-3cef-32ec-a6df-44a05cfab384 | -5.64664 | -43.71709 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 696ac879-8716-3c53-8fc3-b2522e71202e | -6.14635 | -45.96809 | 2025-06-07 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbee8d0b-693e-30c8-a447-a15e0498f117 | -8.72455 | -47.989 | 2025-06-07 04:21:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa84c597-7c16-311e-b9cb-4f98837aff2b | -6.96257 | -42.90768 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| da646473-795f-33e6-90c0-2906ac37735a | -6.21505 | -44.50698 | 2025-06-07 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac245f5b-9a15-3b83-aab6-0e719c303df3 | -10.73627 | -47.61076 | 2025-06-07 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7f6d8bf4-df98-3a31-a52b-9ac407aba367 | -7.72092 | -44.15896 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b553ca9-d6e1-3ad3-829f-ce2c513bbeda | -6.0683 | -44.23769 | 2025-06-07 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0015998-2f09-3056-8038-683ffaa49d3e | -7.18399 | -42.8283 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3bf90f32-d86b-3dc0-9563-9e47d81864fc | -9.36563 | -57.43816 | 2025-06-07 04:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bfd9067-ad58-3ff7-8e83-1813d2bfa9d0 | -7.2167 | -43.11331 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f1be3441-a05b-32ca-a6a8-082c93ecc439 | -10.29548 | -57.1353 | 2025-06-07 04:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 752acd6d-fce0-30b5-b4ef-3f7d38fbdaae | -9.06518 | -47.1449 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f4770d4-d555-3b2a-89be-0b4b9e0b28ca | -6.24297 | -48.5521 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10d7364c-32a2-3f2f-8b02-fb8fa8bf942c | -7.72261 | -44.17009 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3ef613d6-fe8c-3f05-bbc9-439d040427b5 | -6.94478 | -42.90872 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d351515e-7442-3bc7-9c7e-914208ec0340 | -7.72596 | -44.17062 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8ce0f4a2-642e-3485-94f6-e0df49bc695c | -8.31798 | -47.91704 | 2025-06-07 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 678c1a9c-9eab-3f87-b6c0-692fb2b65acc | -7.72541 | -44.17415 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4abb4c1d-7a08-3e63-a77e-a8aaaf55c4d6 | -9.08008 | -47.13974 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c315231-0985-3214-b57f-b1494e5c744a | -7.72651 | -44.16708 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 07eb38e7-76ce-3402-a87a-1affc4b9e241 | -10.23393 | -52.23842 | 2025-06-07 04:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac5108b-94f1-303c-924c-917c9b758141 | -11.78376 | -47.40128 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 20fba55e-7041-3db8-925f-023d55445e12 | -6.95569 | -42.90658 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 4de1dd0a-5732-3e05-a38f-1eebcc63e339 | -7.72931 | -44.17114 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fcfa6de-9a80-35ae-b622-2a4d1465716f | -12.38478 | -47.31686 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cea39c01-7f2e-37bb-9496-aef9345a5109 | -7.72875 | -44.17467 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07f93201-c213-3994-99d3-e37fe10fb045 | -6.23997 | -48.54685 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a17e4c-f029-371a-b4d4-94dceccf9905 | -6.19915 | -43.33247 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ef5793f9-d945-3792-a7f9-dbf28148c94e | -11.82053 | -44.26165 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffea06b2-6243-3eb5-96bc-68a72b737a68 | -8.45841 | -46.49131 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f91d63-dc04-389a-9297-fe4579a7bf58 | -6.95225 | -42.90604 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cc448d2b-0620-34b1-bc62-93d3aaccb6bf | -5.6444 | -43.70953 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4d912d6b-e578-3f61-a419-c43cb33c9adc | -8.45166 | -46.4902 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b24069b3-a195-363a-933c-798a10293d1e | -7.72486 | -44.17768 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68d5995b-71b6-39a2-b184-c7a691e81d10 | -6.95797 | -42.91463 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 2753b291-9c67-37ae-9ff0-9f8c47b0d785 | -9.87877 | -44.80039 | 2025-06-07 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fb09b0c3-798c-34f0-9719-c218f6c1e587 | -9.00969 | -48.7232 | 2025-06-07 04:21:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c581f42-332d-3aaf-8224-d28a594ced71 | -12.5357 | -45.41311 | 2025-06-07 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbce5067-785a-3ef7-8411-6b34988c3d35 | -11.78656 | -47.40553 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2538c029-7a57-3053-a0f1-22176e5a10cd | -11.55607 | -47.61763 | 2025-06-07 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1849cd5e-7078-3544-ad1a-325239338396 | -6.95005 | -42.80563 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 64a78f7a-ffa5-3250-b222-7b1f6fb1bc3d | -10.88161 | -54.30878 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aba51c2-b003-34dc-9aea-35046f90ed48 | -6.80764 | -41.73706 | 2025-06-07 04:21:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb096a22-cdba-3363-96dc-8ff48754048f | -5.92304 | -45.52434 | 2025-06-07 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8a2681c-96f5-3ddd-bdf0-0326f7b45004 | -10.63066 | -49.43085 | 2025-06-07 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6609ac75-2eb1-385a-b59b-3a3013ee5beb | -6.21118 | -44.50993 | 2025-06-07 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1bbc6b7-0a29-341b-a23e-b1f085eb16d2 | -12.27361 | -44.60465 | 2025-06-07 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f22c17a7-2fd7-3832-916f-6082ade0d974 | -9.07887 | -47.14716 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa75c399-64ab-3bb6-9ebf-179008104e26 | -7.25377 | -43.46025 | 2025-06-07 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7f86552-84f2-3d74-8e34-d9ab6174dd55 | -6.95063 | -42.80185 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 79c56910-66fe-3a6a-8a4e-cd0f99136244 | -7.80756 | -46.49874 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fb3470a-cad6-3a41-b8e9-bdda7a605a0e | -10.46793 | -47.94706 | 2025-06-07 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32a51415-bc5b-318e-81d2-77a40bb18bb0 | -5.64219 | -43.72359 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 05267a9c-8aab-334c-b88a-d320bbf5d82a | -10.49001 | -53.67065 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7fdf620-b01d-39c5-a078-694239ea5199 | -6.48745 | -47.01497 | 2025-06-07 04:21:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16cc97f4-f07f-35ad-8447-9fe595696513 | -7.73991 | -44.16914 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8fe74cf0-5951-3975-8242-d8a4a3ecaea4 | -11.08997 | -48.46427 | 2025-06-07 04:21:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84c3ab30-d50c-345b-ae42-b96eb2a962c4 | -10.87729 | -49.54843 | 2025-06-07 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d5a924e-1dda-37b5-8a4d-bd40ddb61f6e | -6.94765 | -42.91301 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b54627be-190b-302e-a149-80dcca3e34ed | -11.77699 | -47.40014 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10d8c487-8ea2-37aa-b760-16dabed5f9dc | -5.64755 | -43.60173 | 2025-06-07 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e8ee0b3-633d-3d8e-8b50-90f1003d1854 | -11.04281 | -48.80859 | 2025-06-07 04:21:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f69b0ce-d6ad-3907-a794-7f05f4ee6ee7 | -11.78097 | -47.39704 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8e24b99a-121c-3a04-91ec-91442bcac0fd | -9.20961 | -48.02412 | 2025-06-07 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a55c79a0-128f-338d-863a-a63e8ee4295f | -7.73376 | -44.16457 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d2580c09-f9b8-31f8-9dc5-98f3b8e06388 | -10.49101 | -53.66509 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a3b39762-a794-3282-89ed-51936b9cc231 | -9.06235 | -47.91177 | 2025-06-07 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfa76fa2-e0f2-34b0-8a3e-d44b01262e03 | -7.71537 | -44.17257 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README13.md)
