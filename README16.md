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
| 15ab5365-d3e6-3e7d-8fb5-4537bb254310 | -4.69944 | -45.84352 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5fb000c6-2c73-3ae9-a9dd-c8004fb585b0 | -4.69938 | -45.82239 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9344ff6b-bdf3-320c-b167-a88981cdfca8 | -4.69884 | -45.82582 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 916417bc-c790-3a14-a1c4-692f9ce5b343 | -4.69392 | -45.83562 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1170f727-5e9c-30ee-8025-acab448fdd39 | -4.69338 | -45.83905 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d8875e-7bfc-354b-98f2-72f79dfd8ee6 | -4.69285 | -45.84249 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 515fbc34-e32d-3601-b779-47837d27beae | -4.48763 | -45.6977 | 2024-10-19 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 126c6533-ab0c-397c-8742-651c3c284512 | -4.46681 | -45.89498 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3113487c-d215-39e7-ac33-fb3f3df80b1e | -4.46351 | -45.89447 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 731e0bf4-5765-363a-aaa4-5009c5872ee1 | -4.41795 | -45.79187 | 2024-10-19 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c245a94f-f141-315b-8526-8d2ece1af503 | -4.36747 | -45.81215 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b933582-4bbe-34be-b54b-1152b71cc8f9 | -4.31349 | -45.63482 | 2024-10-19 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b90033e-877b-3222-b7e0-36bb07457e75 | -4.27625 | -45.85057 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c796d16-d915-3092-a183-25a835ce52d3 | -4.27295 | -45.85006 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4b6d4a6-daf5-3ede-bada-7858f0d6d83a | -3.89641 | -45.66749 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0bd80b93-550b-3b89-92d7-4ddde7871dfa | -3.88705 | -45.66252 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf49043c-847c-3ad1-8a33-634a301f6c50 | -3.81668 | -45.71778 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2713bcd6-a8f4-35d8-bd22-2db028ffb74f | -3.81615 | -45.72121 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f51cd8f8-9538-3463-9c7f-269d1072ee22 | -3.7703 | -45.81953 | 2024-10-19 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3635b040-bb2d-394e-b0da-cccc48aad24c | -3.69513 | -45.71278 | 2024-10-19 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0b57ff0-d8c1-38d4-bc93-e35cfe6b5cc0 | -3.69459 | -45.71621 | 2024-10-19 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b108d04e-0fe1-36fc-9c64-7391acc9bb8e | -5.80673 | -46.31208 | 2024-10-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef4d818a-8b6a-3162-a3af-378ac8f5301a | -5.7612 | -46.38243 | 2024-10-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cafdd1f4-c228-3920-82b4-24ff96b5784a | -5.68487 | -46.43758 | 2024-10-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24e8fe59-c50a-34ef-9afa-c792f38b499e | -5.68157 | -46.43706 | 2024-10-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e251ca5-8503-3ef7-a0d7-1e85dba69f40 | -5.53866 | -44.95591 | 2024-10-19 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e5c3b4b-89c8-370a-9f2e-6a53363770a0 | -5.51187 | -45.34587 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e22416de-cd5b-348e-93be-a8caa8f48760 | -5.51083 | -45.4849 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ce9f2e2-1bd4-3763-801f-21115fa1e124 | -5.51025 | -45.1385 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77a277c8-584a-3bec-ad46-d6c9faeeaa5b | -5.50856 | -45.34537 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5e8433e-be47-388b-a125-4521c25996b3 | -5.50752 | -45.48438 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdd52cb1-18ac-342b-960c-bdca1f66dcc1 | -5.50698 | -45.48784 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 943f6962-090c-3f8f-b0a1-6fc57108cf2c | -5.49751 | -46.28738 | 2024-10-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a0d91ed-e6f3-3bf1-a39a-bc5807eb892a | -5.43916 | -46.35234 | 2024-10-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5ecd261-8ddc-3630-b941-fd17e687e6b3 | -5.38625 | -46.08253 | 2024-10-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f502c2cd-15b1-3ef1-962f-f39cc61ea163 | -5.38163 | -46.00432 | 2024-10-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44a4d070-c338-30c6-8dd9-eccfdd79b66b | -5.34748 | -45.48381 | 2024-10-19 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5345cc1-4e55-3de9-a5d1-5646130a5433 | -5.32252 | -45.05579 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b93f541-2377-3dc6-9bcf-ebe241b2513f | -5.31886 | -45.16632 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 923e4362-7ac5-382d-8660-9ceecde9a2b7 | -5.31554 | -45.16581 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74624b4d-44c8-314f-bd94-fae8f402e530 | -5.30776 | -45.15029 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1db6c3f3-8478-3bbe-a4e3-b252ab73b096 | -5.23177 | -45.94215 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c472ad0f-04b2-3a71-a233-4a794c9bd885 | -5.1435 | -45.35226 | 2024-10-19 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a7dee2d-b45e-3a26-ae24-726eb109f946 | -5.13817 | -46.10348 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4956ac04-a565-3fa1-b477-cb016821de56 | -5.1263 | -45.15747 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0e7df3f-afbe-3ed9-b376-d854ccdabf2a | -5.12352 | -45.15347 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b66631b-e3ed-39e7-94e5-2fed4dd5ef3d | -5.12298 | -45.15696 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1e664ea-0052-3b0b-b4ea-924e3eadb73b | -5.09872 | -45.94589 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9702ed44-516b-3c21-a6a4-a4d4418a2dac | -5.09542 | -45.94538 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef620b65-1e70-3ce1-b120-6dfaf84a9b18 | -5.07875 | -45.7661 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 864b3cab-76dc-38ac-a4e4-6ab2408edb20 | -5.07822 | -45.76954 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f82b1bd7-4cc0-3fa2-83bb-e458eedce4c5 | -5.04837 | -46.08883 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 519daa41-90d5-327f-94c6-1a707ed86a60 | -2.16383 | -46.27405 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7ddc5fa-627b-3d59-8cb2-3e9d851fd1c1 | -2.05248 | -46.89249 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd071126-fece-34e6-a3fa-d539c372292b | -2.0491 | -46.89196 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8856b94-1c36-3874-8f2a-49d4c84619ae | -2.02381 | -47.05168 | 2024-10-19 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 862eb44d-0244-3125-bb1a-22a2132d2684 | -2.02041 | -47.05117 | 2024-10-19 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47c59a1c-8c99-3598-af4d-4bb0b67a40af | -1.9775 | -46.61309 | 2024-10-19 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4613ec8b-e243-3ed0-a232-e7251e163085 | -1.6697 | -47.15874 | 2024-10-19 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81adb102-441a-3d61-a744-0346280fe308 | -1.42559 | -45.90504 | 2024-10-19 04:25:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00ad2fc3-f355-3fa4-ae0a-7a629c906022 | -1.37952 | -46.69932 | 2024-10-19 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b7505b0-c795-3f2e-a00a-18633abe96a7 | -2.75759 | -45.96219 | 2024-10-19 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be148fe2-2c7b-39b3-a366-efe2fa6b1e95 | -2.58209 | -46.126 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26b39a8e-86f9-3d15-9a82-fa7731b643f1 | -2.57314 | -47.06553 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1410ad1c-9edb-3cf0-902f-5b86a17fdb69 | -2.57256 | -47.06916 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ed1e4ac-a0c4-3536-8789-67c90216ea27 | -2.57199 | -47.07279 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0ba97ad5-df63-3f8b-b3d1-4727038e9b38 | -2.56976 | -47.06499 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f93ed98-adf9-39fc-9e3d-178d911250b7 | -2.56918 | -47.06863 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57c083c4-5875-3633-9789-9009d3b50624 | -2.5686 | -47.07226 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 43609867-0595-3e73-9649-81675fcea2e7 | -2.56637 | -47.06449 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 094462f6-44e4-3d76-b48c-a748b795ae7e | -2.55711 | -47.29896 | 2024-10-19 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 725b722d-2d47-33bf-a457-c2e4f6efee6e | -2.53751 | -47.22437 | 2024-10-19 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db86d74a-e1d3-3696-b3f2-99e26b126a59 | -2.5341 | -47.22383 | 2024-10-19 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da9bd6d5-8b17-319e-b971-f43c60d69d97 | -2.53352 | -47.2275 | 2024-10-19 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efb21371-4883-3343-a33b-5d24e6d362d8 | -2.51044 | -45.99784 | 2024-10-19 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b447d85-e315-392c-a781-5470d15da45c | -2.50989 | -46.00129 | 2024-10-19 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbaf31f6-2abc-3a58-866b-991f5e48c41f | -2.50436 | -45.99335 | 2024-10-19 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9db5600-14fb-30fb-b3ec-ef476166e0fd | -2.50327 | -46.00027 | 2024-10-19 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 185c18a6-fd15-3e15-82e4-2195c1d9ec9c | -2.40548 | -46.70524 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e93930f7-4b07-38f4-9143-7ca11e5c1ece | -2.40379 | -46.71592 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00dc56de-72fc-3666-900e-40b34329858c | -2.39988 | -46.71896 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48f6d9a1-59b9-3e9d-9fd0-1377e397fdad | -3.09053 | -46.54891 | 2024-10-19 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d78f786e-8a33-300d-abfb-d1196c4621bf | -3.43287 | -46.34228 | 2024-10-19 04:25:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03e723b4-9fe5-3244-9a0c-21e504386c4e | -2.36911 | -46.97861 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d03b7aa3-985b-3153-a4b3-f14aedcbce11 | -2.36325 | -46.47782 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d7fd0b6-d4a5-3c5a-8e9b-e8247cf2bcf0 | -2.3627 | -46.48133 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e74d4b-7cb9-38fd-abad-120a0404c32b | -2.35547 | -46.48381 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd41e33e-59ac-34aa-b0ed-881c94031ad1 | -2.3538 | -46.49437 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40bb36e0-09fc-3c14-bc99-efd7876155fc | -2.35213 | -46.48329 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5da55ce-303f-3d40-8cab-9ca438510841 | -2.35102 | -46.49033 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06f5783d-d255-3e34-9d89-57be745e2549 | -2.35047 | -46.49385 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 482998c7-35f1-35e4-9500-494eba1e8142 | -2.34991 | -46.49737 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53d31d0c-2c98-303f-9530-ec19d86c9047 | -2.34936 | -46.50089 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a058dbe-416f-3452-94fd-9e574aeb837b | -2.34879 | -46.48277 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef42c2e3-276f-331d-a2aa-12e220b849f7 | -2.34768 | -46.4898 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8cde6c1-fd8c-3bf3-9bce-18f8a621e256 | -2.34657 | -46.49684 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02d7d550-a2f0-350d-a37d-ba2fbe4a57bc | -2.34435 | -46.48928 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8460c5ef-9ad8-35ef-ad9c-03d4c4410103 | -2.34212 | -46.48172 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 722a7d4f-bd4b-3d6c-aa26-a9e1d9c6af0e | -2.33968 | -46.83759 | 2024-10-19 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a330493-a659-3ea2-8a60-48d6fccfc863 | -2.32876 | -46.45805 | 2024-10-19 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
