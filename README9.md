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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55837436-49e4-3297-b14c-f5438370aa5c | -3.65997 | -44.69554 | 2025-12-11 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2679ba20-91fe-3ef8-abc6-27406611bb88 | -2.30924 | -46.48525 | 2025-12-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d4d8e2a6-0c3e-3862-81b0-c976554cdb19 | -3.3803 | -44.72653 | 2025-12-11 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e9d18a7-bc47-3b26-b176-a501417f5ce5 | -6.07713 | -41.76639 | 2025-12-11 04:18:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0c864e32-0470-3be7-b12c-024c4c7b4541 | -3.34274 | -44.40841 | 2025-12-11 04:18:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfab03e0-0401-318c-b569-ae6bb51cb547 | -3.39532 | -42.10466 | 2025-12-11 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d4e30d41-cce7-3e57-9290-2f5f1e1de543 | -5.98548 | -44.59646 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e62e949-3f6d-3500-978a-7ff338539112 | -2.08356 | -52.05294 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6aad8a14-943e-3b10-98f0-341ce804860d | -1.48243 | -54.2053 | 2025-12-11 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8496d82-6c5f-3faf-bc3f-04c5e2cc8cfa | -1.584 | -53.76227 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be0f3b62-5ee3-3859-b88e-53293f136e45 | -3.04057 | -50.49434 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97d0a7db-d178-343a-87af-3c1c1ecb6403 | -3.40858 | -44.17366 | 2025-12-11 04:18:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06ef6e8d-abdf-3671-8dac-b5d89a6019d9 | -1.57888 | -53.12347 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8051c936-2cd1-337c-9c09-648d88ee787c | -9.80159 | -37.73626 | 2025-12-11 04:18:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2956247-d1f0-3e79-9d3d-f075d74256e8 | -9.16473 | -40.10995 | 2025-12-11 04:18:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 23cfa0bd-edfa-39f3-a603-681d3cae8ca4 | -4.27389 | -42.17844 | 2025-12-11 04:18:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f47083f-e3ff-3ed4-8fc2-67140a75758d | -3.10849 | -45.22801 | 2025-12-11 04:18:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23ed9c2d-819a-3e65-afa2-e44ba67f64ba | -3.55213 | -45.45618 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5e36630-6c21-33f3-908f-49c200c358ec | -6.02539 | -43.70829 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0db63c29-d9a8-32f2-b60a-23a5392cee87 | -5.57431 | -39.00804 | 2025-12-11 04:18:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 78f49d41-ffd7-30bd-be6f-dda5d97416b0 | -4.23289 | -45.398 | 2025-12-11 04:18:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a64103e9-14d4-343b-8192-f960ba4c011d | -5.98606 | -44.59284 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24c16623-51e0-38f8-8b0a-acf6ecf33b4a | -8.35522 | -42.04296 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 69f5cfa7-11a9-35e6-b5ee-61b56a68a6e9 | -6.94319 | -38.61454 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c94eeb92-a79e-3d99-a417-4b00ac60ce07 | -4.15361 | -43.21899 | 2025-12-11 04:18:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31a60375-0f5a-3d65-bc9f-5ca9bccd2ded | -2.07795 | -52.05196 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80f4fe73-027e-3a1c-9017-96b2d7ab68b0 | -6.54366 | -39.47594 | 2025-12-11 04:18:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7a2813c-1174-3d73-9a1b-bf23259ddc2c | -3.36168 | -45.34029 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e93d2371-d78b-30cc-b47a-05cb4088a251 | -3.60293 | -47.53534 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1756f9d-829c-3368-a2c9-2a0e2da6c31d | -2.90691 | -46.7279 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 546d96e7-ab97-3259-96d8-34072810741e | -4.93872 | -43.96099 | 2025-12-11 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55142cc5-cf8f-3177-af52-9420d7a0a863 | -5.00962 | -41.29281 | 2025-12-11 04:18:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 717ae4f1-f8f5-3e8a-ad14-4c62f9dc7af3 | -3.17555 | -48.0287 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0ba75dc-de4a-34f7-aacc-858457911be8 | -4.49308 | -44.33929 | 2025-12-11 04:18:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14084cf0-0293-3da6-8921-032c10ca538e | -3.68111 | -52.53128 | 2025-12-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdcd2506-19db-34d9-9949-2412cbe748b3 | -9.38151 | -40.75138 | 2025-12-11 04:18:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e3238175-86a9-3fc5-8e87-d2094cbf968d | -4.20914 | -44.47494 | 2025-12-11 04:18:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6440cd7f-f83a-3542-9f27-6712025a9f95 | -2.69125 | -51.64629 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753b0810-4c94-3f97-935f-bee5aa23daf2 | -2.07985 | -48.36574 | 2025-12-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2edad744-5f91-3b19-ac86-adec31a0a825 | -3.0905 | -44.89425 | 2025-12-11 04:18:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7797475e-e598-3f0f-bf07-4b5f4ffc694d | -2.37961 | -47.41961 | 2025-12-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab8c157-da2d-3ffe-858c-a461e133f3f8 | -3.5365 | -45.46199 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d5147d9-60ed-3f3b-b64e-b242feb9da83 | -4.99971 | -44.55709 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 090e0d52-964b-3752-a1f9-98bb525213c1 | -5.40912 | -45.22221 | 2025-12-11 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea10ccee-0803-3a25-9d89-b8f366210e87 | -5.89253 | -38.17868 | 2025-12-11 04:18:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f286a62-baed-321b-bca7-6112594ceabe | -2.55171 | -45.32323 | 2025-12-11 04:18:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19716a61-0d1a-3bfe-8939-80ce31afff24 | -3.88437 | -42.52466 | 2025-12-11 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e12839df-5892-3a8f-99de-f94d8e38964a | -2.31 | -46.4805 | 2025-12-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 211e6f6f-85b4-3de8-8163-61e3e87b6c1b | -3.23479 | -47.47291 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd50c47d-8c0c-34dc-a292-c7dce0b279b3 | -6.60524 | -39.52863 | 2025-12-11 04:18:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c1469cf3-025c-3cd3-8057-bd7168107df6 | -6.504 | -41.48959 | 2025-12-11 04:18:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9081c1e1-25dd-373b-8d3a-de22c5fc8546 | -3.21489 | -46.06596 | 2025-12-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c65b395-b570-3451-afb7-3a780dbdc580 | -1.30397 | -53.48882 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daea78a7-7b65-3b0c-8830-d09e33f46e55 | -3.62925 | -44.64421 | 2025-12-11 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b363c51-d66b-36ad-9bb1-3f8aad74674d | -6.9152 | -44.13762 | 2025-12-11 04:18:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4a3e585-b6f6-3b46-bb79-40a06764f689 | -4.31633 | -44.50275 | 2025-12-11 04:18:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6572bd09-e6b1-304e-b837-6a11342f752a | -3.68047 | -52.53505 | 2025-12-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebfbaccb-23b4-37b4-ba18-b0a719c1ef52 | -4.12479 | -43.22868 | 2025-12-11 04:18:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dd87e78-0c0f-38b5-ba1c-92f241805c96 | -4.6572 | -44.49252 | 2025-12-11 04:18:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6843a44d-b2c2-37b1-89df-977d0d6b0e16 | -4.76576 | -43.602 | 2025-12-11 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 390ed349-ab02-3a4e-aec6-a9fe8caa791f | -5.55955 | -43.80624 | 2025-12-11 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b881af06-d95a-3c1d-9d43-7425142c5010 | -3.81177 | -45.18804 | 2025-12-11 04:18:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8e430a4-3eec-379c-830f-adda466934db | -6.02859 | -44.32683 | 2025-12-11 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00dc1fdf-a31d-3fca-8b56-246851f6b761 | -4.41911 | -44.80106 | 2025-12-11 04:18:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 47bb05f9-5307-3700-946d-fd2ea22bc2bc | -6.93922 | -38.61401 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1758e820-a08f-3639-92dd-bb20f654735f | -4.50052 | -40.52087 | 2025-12-11 04:18:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af08aed3-8f6a-3f97-8d38-d1bf6f75a206 | -6.8227 | -39.38916 | 2025-12-11 04:18:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3003e5cf-3cd1-3998-969a-fbd648a10fdd | -4.22935 | -45.3974 | 2025-12-11 04:18:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d15ada1-c9b6-3862-9ed1-7f8c5f49a865 | -4.3937 | -45.40543 | 2025-12-11 04:18:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67889306-c11a-339d-a5e6-151aa7996237 | -6.91026 | -38.09891 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 382154ba-6f90-38e9-89d1-c2d30525981a | -3.42645 | -41.65397 | 2025-12-11 04:18:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f5379c74-6e90-3450-aff1-e2e0adfb062c | -5.21263 | -43.41505 | 2025-12-11 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b0fd504-9b92-3119-a02f-4c10fee922d7 | -6.5555 | -35.21175 | 2025-12-11 04:18:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60f76d6b-88f0-3215-a180-3f9ea9adff9c | -6.74046 | -35.01844 | 2025-12-11 04:18:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8ea82268-1bce-3ac0-94c6-728fbf9f636e | -3.34919 | -46.86301 | 2025-12-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc8b3162-23c5-3253-acd6-098853208ff3 | -3.95742 | -41.52339 | 2025-12-11 04:18:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc96972f-73c4-3b5f-a770-b5f0dca7fd31 | -3.75451 | -45.49852 | 2025-12-11 04:18:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 46b67b78-5ed8-384c-9dbe-629743d048a4 | -6.90617 | -38.09834 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2119325b-9dbd-38da-828b-547c296ab94e | -3.7594 | -45.49097 | 2025-12-11 04:18:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 236f84f6-6a23-362e-b0cd-936535117d36 | -2.21484 | -51.89418 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc185ad6-f83b-3742-b117-f61797c8d0db | -3.8426 | -47.82463 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de0a24c5-8e12-3841-b53a-735f339c71db | -2.20868 | -51.89688 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f35aae3-86fb-3fa8-a8e9-cb4627d7b265 | -2.65757 | -51.64122 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 284c8878-5ab3-3e54-96b4-3431571563e7 | -5.98887 | -44.59701 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 408e09d1-42e1-369f-80b4-3a32fd5516ec | -2.07918 | -48.36987 | 2025-12-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee206232-28c1-3970-838e-cc3412cad382 | -3.21814 | -42.69213 | 2025-12-11 04:18:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 202efdf6-9e63-3162-88ec-b3815457d92b | -3.54921 | -45.45156 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e6e9d85-2ba1-34c8-9b82-4d1311999d2b | -7.06531 | -47.35708 | 2025-12-11 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fedd7aa-f777-3362-a60e-c0bf2ea97004 | -4.31291 | -44.50221 | 2025-12-11 04:18:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd5846c8-cd32-3521-8ca2-75f9aa35e81c | -4.29823 | -44.63656 | 2025-12-11 04:18:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 237886b6-7148-325b-a9ac-85cfe3d97175 | -5.57502 | -39.00343 | 2025-12-11 04:18:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f1e7d922-5d95-3a43-af3f-58032836cfcc | -7.62656 | -39.0694 | 2025-12-11 04:18:00 | NPP-375D | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc6e779d-7421-3760-8619-21a05ee700d5 | -3.39477 | -42.10812 | 2025-12-11 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5c872468-960a-3d5a-a77e-bee263f4e0ca | -3.23424 | -47.47636 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 502458df-d123-38f9-8761-9812f2a897e3 | -3.75517 | -45.49446 | 2025-12-11 04:18:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ed3f2c7b-6994-3446-b9b8-0c1896b41391 | -7.86096 | -38.7289 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c44da841-d57e-30a4-8f81-e8a761570c68 | -3.62864 | -44.64797 | 2025-12-11 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006ad196-8c88-37ff-ade2-4473c7cac57c | -5.16006 | -37.69942 | 2025-12-11 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 88b32584-f649-3b98-be56-3ef496f86995 | -3.10914 | -45.22401 | 2025-12-11 04:18:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f93e2a52-838b-3249-aefe-5cb1864e0c08 | -3.66861 | -45.77671 | 2025-12-11 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
