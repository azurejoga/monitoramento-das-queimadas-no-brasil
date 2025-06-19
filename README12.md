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
| 06e38380-b329-3114-a66c-e7700832f87d | -18.66268 | -55.7594 | 2025-06-19 04:00:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e13786d4-73b3-35da-93b1-514e0dd4f7ac | -16.31992 | -53.79675 | 2025-06-19 04:00:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5186168-fb6c-313a-baa8-968cee19f9fe | -17.68163 | -46.82109 | 2025-06-19 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4f199ae-64c1-3d1a-bf25-46a28f463293 | -17.70685 | -46.30124 | 2025-06-19 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cb61cb6-4d78-31a7-abc6-d8751d01aaf0 | -20.86276 | -48.93415 | 2025-06-19 04:00:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c2a09ce5-f7aa-3c9e-85aa-25086de44264 | -19.54437 | -49.6715 | 2025-06-19 04:00:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c9749900-c158-3fe9-9062-91ecfb5c38a5 | -21.01252 | -44.20972 | 2025-06-19 04:00:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2d2e6de-cd51-33fc-b0ab-ac469fb25221 | -18.65744 | -55.7504 | 2025-06-19 04:00:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 17eefc67-2f81-3e6a-9906-3e4f11738f9f | -18.65952 | -55.75519 | 2025-06-19 04:00:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f4610506-20bf-33ef-a928-47a7df2db729 | -22.90118 | -43.75581 | 2025-06-19 04:00:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a3b4ad9-78cf-31f0-a8e0-6775db122f6a | -17.70268 | -46.30419 | 2025-06-19 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10cd83d2-9a4d-3c15-a144-1551fac22bac | -22.67539 | -42.85558 | 2025-06-19 04:00:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7425fca8-1e06-3f1f-aa7f-5d29abb804e0 | -17.75871 | -52.43455 | 2025-06-19 04:00:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3981b9ff-3797-3559-bca9-3c3c2388c04c | -16.63829 | -48.49159 | 2025-06-19 04:00:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26f62310-f223-37c9-8c2c-522c0ebbd7c3 | -20.93815 | -47.42976 | 2025-06-19 04:00:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5e2df25-5a5a-3a53-8cca-a9512c5d3b80 | -22.11899 | -41.45073 | 2025-06-19 04:00:00 | NPP-375D | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cd53fd5d-481c-3268-8a72-8f08f12bd9c4 | -19.4674 | -44.30005 | 2025-06-19 04:00:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32781d6b-052e-33be-8b57-50c70fe76080 | -20.94149 | -42.83547 | 2025-06-19 04:00:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d674cfac-a144-3581-bace-e7546792cd8f | -20.86724 | -48.93521 | 2025-06-19 04:00:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 84360b72-bad7-3681-8d03-269a51c817c9 | -20.76254 | -46.77181 | 2025-06-19 04:00:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e68cc1cb-f88c-3ad3-8537-6e4b1fe3876a | -22.11565 | -41.45014 | 2025-06-19 04:00:00 | NPP-375D | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 61fefb12-b6be-3be1-8737-76400fc9447e | -21.08807 | -48.68523 | 2025-06-19 04:00:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0113ac06-db8d-3fc3-8e42-b840adcdaa65 | -22.78517 | -43.75819 | 2025-06-19 04:00:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2dc30a31-c226-3edb-8a31-180e77f7377b | -20.93888 | -47.42592 | 2025-06-19 04:00:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05fd09b1-1c26-3db9-bb77-6640ef3036b4 | -19.86636 | -44.95602 | 2025-06-19 04:00:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 398ddd2d-ba7a-3159-b52c-a51bddb2a823 | -16.68188 | -43.88416 | 2025-06-19 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 257c73bc-bd14-34e0-b515-a00cee0498d3 | -18.05722 | -44.49419 | 2025-06-19 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa02db0f-1c72-313a-aab4-d6e04de48bed | -23.69958 | -46.68045 | 2025-06-19 04:02:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9019ef69-9667-33c1-bf35-f94a219ec77f | -23.58486 | -54.41915 | 2025-06-19 04:02:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a45a7b94-8985-38b0-a6cd-497c09e7067c | -22.5404 | -48.81368 | 2025-06-19 04:02:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 396d63f4-45ca-3fbe-af10-f552f55e77d6 | -21.78641 | -52.76265 | 2025-06-19 04:02:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4da455e5-0e08-3994-beff-b8e887cb9c05 | -23.5469 | -47.63825 | 2025-06-19 04:02:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6473bec0-1725-3428-9eb2-0f5a4270216d | -21.78086 | -52.76113 | 2025-06-19 04:02:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21407b4f-dd74-3fbb-80e2-fc4074d2702d | -23.33641 | -46.77387 | 2025-06-19 04:02:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 93384fd5-0ea0-38b1-ab80-056849ba8a82 | -23.54968 | -47.63781 | 2025-06-19 04:02:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f07e9836-3da3-3605-966d-ab912e1a1439 | -23.66307 | -47.35254 | 2025-06-19 04:02:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c3d59bae-1670-3322-a80a-81545eba63f4 | -23.40367 | -46.55734 | 2025-06-19 04:02:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1debb3c3-2746-3ef6-a798-d0bbad31a977 | -23.59383 | -47.43856 | 2025-06-19 04:02:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85d2d71b-dd9e-32f8-bdfd-f64ca27e6c72 | -24.24152 | -50.74133 | 2025-06-19 04:02:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e4c2cde9-008b-370e-af43-ea15045cf243 | -7.2405 | -43.0899 | 2025-06-19 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| bde9174b-0127-33c0-91b1-056b997530bb | -9.7914 | -47.1785 | 2025-06-19 04:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 5f403d01-b1cd-3362-a4eb-5242e25d58c0 | -8.07 | -43.1216 | 2025-06-19 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 006c058f-2d78-3c4d-b46b-685ac1f24bb8 | -11.9709 | -58.7362 | 2025-06-19 04:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ecf65409-a081-345f-b114-5006a9477344 | -8.0703 | -43.0981 | 2025-06-19 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 9fb06a0c-e3df-333d-a2cc-9b2e9adef035 | -11.952 | -58.7376 | 2025-06-19 04:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 47687cf9-b074-30bb-8d37-12eb22e6b120 | -11.9707 | -58.756 | 2025-06-19 04:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b3552e86-df63-3b48-9550-150e93d1939c | -11.9518 | -58.7574 | 2025-06-19 04:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 3538b7b0-605b-3612-87fa-4f6affcf82af | -5.29059 | -44.71947 | 2025-06-19 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d6678c1-cf09-3027-b4e3-4d856a94fe69 | -7.24011 | -43.09024 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 66ca95c4-46bd-3dfd-9d7c-98c89582409d | -5.12637 | -45.02689 | 2025-06-19 04:17:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b4cca67-b8d8-3458-855b-5242e5677308 | -6.29105 | -44.23346 | 2025-06-19 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18026bdd-f2c7-35f9-ac86-07a42644edaf | -4.84494 | -43.18974 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a67509a6-6eea-3178-afb9-b3b841b9806d | -8.0782 | -43.10599 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 562438e6-374b-3661-a767-9aee0bf900c3 | -4.41146 | -47.65621 | 2025-06-19 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7e44e00-721c-3756-be41-a890768d8b2f | -8.07763 | -43.10974 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4dbda717-0e2c-338e-bb1f-bdef9f17df56 | -6.67896 | -43.2067 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2569259-884d-3d32-91f5-7814daad8b14 | -6.69078 | -43.19744 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 725b4b22-97e3-3461-b3eb-f0a55b425b9a | -4.55257 | -48.00652 | 2025-06-19 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fac4372-a84d-3ab6-9da6-8ef1fec3f7d8 | -5.78162 | -43.47511 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc90e316-5025-3206-bbbf-f93feb765636 | -7.23444 | -43.08183 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 01dc6469-e348-396b-a4ba-0a065566b78b | -6.60695 | -41.76785 | 2025-06-19 04:17:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1a052274-9f5a-3b61-af80-1166d14e8b51 | -7.34608 | -43.87292 | 2025-06-19 04:17:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c4634ef-8205-3a47-aed6-5eb4867ab2b2 | -5.12305 | -45.02637 | 2025-06-19 04:17:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30782565-e93b-33d7-8348-684b7e7f2741 | -7.28981 | -47.09787 | 2025-06-19 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e0a8af2-de12-3e2b-9b9c-9dfc9ea3162b | -7.2316 | -43.07762 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a2b6b882-b204-3632-bf3b-22315c0c21bf | -6.68741 | -43.21907 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 57f8c22f-7681-3db1-a539-d64322eb1205 | -7.23102 | -43.10394 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 08bfd104-f0ec-3f1f-80f1-b98f5293bfb9 | -6.29436 | -44.23398 | 2025-06-19 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13b49016-ba52-31a6-891b-6a4e37ef4b37 | -6.67206 | -42.48145 | 2025-06-19 04:17:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 796de51a-7c00-3323-8ece-8368955fd052 | -4.61687 | -43.75481 | 2025-06-19 04:17:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62685af8-d256-3a7c-86a3-ec92a12be1f8 | -4.84605 | -43.18267 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4782c782-9915-3a7e-8711-a62c41f9f137 | -6.32471 | -43.75713 | 2025-06-19 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6737a8-af6f-338c-bd9f-eebd8871959a | -6.68234 | -43.20722 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 820b7369-1c58-33de-9742-d3ce8d03378e | -7.16548 | -43.21375 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6511534-44dd-3769-abd3-2d04dd8e3c58 | -7.28064 | -47.09696 | 2025-06-19 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59d8e7bc-d76a-3962-8162-f337e46a917e | -7.17788 | -43.20074 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b9100f9-331f-3d98-97e3-17311bc23273 | -4.28262 | -48.18546 | 2025-06-19 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9f427ea-2e0c-3bb7-8563-3020c6c3163a | -7.15322 | -44.0624 | 2025-06-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 374dd549-7df7-39ce-b4bc-d0e589e57125 | -3.7324 | -49.68542 | 2025-06-19 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc5a91e9-9ac2-3090-bb6a-c9e23621f2b0 | -5.90968 | -43.45474 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4b9cadde-11cd-30fd-8889-6cd2ca18d6ff | -6.68178 | -43.21083 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2b4936e-0785-3311-8b59-5a3bdc09eced | -6.68459 | -43.21495 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 58887310-b399-36ab-8cb9-cf64307064a7 | -3.16626 | -52.44949 | 2025-06-19 04:17:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db2f2203-3197-32b4-bd71-e65ac4d75bfd | -3.80971 | -48.95857 | 2025-06-19 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e2cc988-f4ee-3887-8bf1-eab10d6a3a34 | -6.68909 | -43.20825 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4af79296-f88d-3013-b927-22f1f0202537 | -8.06736 | -43.10818 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 0a76fe2d-578f-3610-8063-4b9815121470 | -5.12582 | -45.03036 | 2025-06-19 04:17:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c9e4c74a-bc4d-3fad-95cb-a23ec246bd35 | -6.66859 | -42.48093 | 2025-06-19 04:17:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 192f2a25-7480-370c-b64c-0d88cc5772f9 | -4.5533 | -48.00206 | 2025-06-19 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4dafbe0-cdbc-3b91-b257-9e8c315c4ea9 | -7.30184 | -43.05403 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 149fac42-18bc-327c-bf28-7ed56d4648d1 | -6.68853 | -43.21186 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99e14d46-4ce5-3049-8a11-1532f56b017a | -7.36246 | -47.04347 | 2025-06-19 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2882e6a6-96b1-3d2c-836c-4b8a467c7919 | -4.77446 | -47.5663 | 2025-06-19 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4a3ed5e-0c61-32ca-a79c-431047faa646 | -5.91077 | -43.44769 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa0ee6e4-7169-398e-8624-021c0e634a95 | -7.23387 | -43.08551 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| da0b6597-369f-3c1c-b7fb-cedb86bc7d19 | -7.30525 | -43.05457 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 637e8b92-7c15-3972-a202-fd543b0a10e0 | -6.36777 | -43.65586 | 2025-06-19 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e5e542b-5564-3a82-a4bd-8bcec9bdeda9 | -7.14363 | -43.28856 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12ee179a-6a8a-30c9-8d7a-913b4ffafee3 | -5.91023 | -43.45121 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 357c122a-a337-3dd6-bedb-d3040c79af7e | -7.23727 | -43.08603 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README13.md)
