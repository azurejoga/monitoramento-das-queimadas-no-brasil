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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b65e56c3-dbf8-3b4f-8cba-e164f127b59a | -2.8677 | -45.2382 | 2025-11-17 10:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1b85e2ea-8d36-3a59-9f66-2296ffb2693b | -2.8863 | -45.2375 | 2025-11-17 10:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 172b9fae-d2b9-3d22-af5c-d08c655e1741 | -2.8677 | -45.2382 | 2025-11-17 10:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 121.8 |
| c5c7f067-b9ca-3267-b61b-a0b6f0753576 | -2.8677 | -45.2382 | 2025-11-17 10:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c9d6f578-ce78-32fb-9ea0-8ef49cc8392b | -2.8863 | -45.2375 | 2025-11-17 10:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c977e2b7-d8d8-3b92-8b77-d97b9e35e028 | -3.2116 | -43.3726 | 2025-11-17 11:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 92c065cc-805f-3c61-a6d3-81fcf97ea838 | -3.2302 | -43.3718 | 2025-11-17 11:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6af242be-1a5e-3082-83c7-56516fcaac25 | -3.2302 | -43.3718 | 2025-11-17 11:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 2214dcfb-1e48-3256-8065-6b64ae67141d | -3.2116 | -43.3726 | 2025-11-17 11:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 798a6edd-6da6-328c-a36e-3f520a104901 | -3.2117 | -43.3494 | 2025-11-17 11:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| be6b0e28-e094-3fee-9db9-fe71814eead7 | -3.2116 | -43.3726 | 2025-11-17 11:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| eb9a8765-07ab-3ef0-9f29-e34e5eefda52 | -4.74325 | -37.88631 | 2025-11-17 11:36:00 | TERRA_M-M | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| dc926a46-d552-3560-a00f-a5c8d26a5125 | -5.33095 | -43.04826 | 2025-11-17 11:36:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| fe755c9a-baea-357b-af51-67f48a1c1f37 | -3.93301 | -39.21226 | 2025-11-17 11:36:00 | TERRA_M-M | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 87b40fa7-cfb1-34c3-82fa-0523ca73e50b | -3.31833 | -40.27557 | 2025-11-17 11:36:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| a18d2f65-517d-3545-affc-b3fcc55cd993 | -4.25523 | -40.10781 | 2025-11-17 11:36:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b46193d3-4691-3682-8c19-98198487aa62 | -6.35111 | -38.58858 | 2025-11-17 11:36:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 88afdd87-5798-3248-8572-77a61f0bfb78 | -3.70955 | -39.54755 | 2025-11-17 11:36:00 | TERRA_M-M | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 06417e1c-4c0d-3ae8-b253-ce71c9feb41a | -3.58888 | -43.59843 | 2025-11-17 11:36:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7abc89dd-ee31-378d-97aa-b8285352c11c | -6.0557 | -35.58006 | 2025-11-17 11:36:00 | TERRA_M-M | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 560e81a4-6d49-3755-bd22-80589cdced8c | -5.06885 | -37.42222 | 2025-11-17 11:36:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c69b89ad-7071-39ce-bae7-f9bb83826f0e | -5.53107 | -37.14956 | 2025-11-17 11:36:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 3f498c35-2cd6-35e9-8e18-1e2d388288a9 | -3.21481 | -43.3628 | 2025-11-17 11:36:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| d26f36de-69af-36b1-b3c1-442f6af50127 | -6.05713 | -35.56969 | 2025-11-17 11:36:00 | TERRA_M-M | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 20.5 |
| b50b2059-6501-300e-9741-4d9a832913a1 | -6.40689 | -38.32705 | 2025-11-17 11:36:00 | TERRA_M-M | MAJOR SALES | RIO GRANDE DO NORTE | Brasil | 2407252 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d42b97c5-6f77-3973-8927-f6d25e68f918 | -4.71894 | -40.456 | 2025-11-17 11:36:00 | TERRA_M-M | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e8ab1283-b496-350d-885f-1d5558972f75 | -5.2753 | -38.61554 | 2025-11-17 11:36:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 3a557110-01d8-330d-9ecb-451eff14e228 | -3.43985 | -41.53929 | 2025-11-17 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 878eac6c-5b7c-300a-8672-a1f918e49d1e | -3.94188 | -40.71688 | 2025-11-17 11:36:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d77a059c-f59d-3a75-8c0d-99090aa346e8 | -3.5485 | -41.72153 | 2025-11-17 11:36:00 | TERRA_M-M | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 5da306a3-1eaf-3d9d-8031-eeabc719b235 | -3.21744 | -43.34493 | 2025-11-17 11:36:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 9dbb6521-1b67-3ee8-ad02-06383bb9f8c2 | -9.66179 | -40.62091 | 2025-11-17 11:38:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 4b5021d9-7b20-3638-8f36-1fe61ee91f54 | -7.9052 | -40.13953 | 2025-11-17 11:38:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c6d73345-9bd2-3923-8385-f0821e45f116 | -10.00454 | -39.16879 | 2025-11-17 11:38:00 | TERRA_M-M | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| eca08cf8-904c-3fce-a11b-998062a6119e | -9.8547 | -44.18243 | 2025-11-17 11:38:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 9fb1e4f2-cda4-386b-9d56-79e132120358 | -7.41951 | -38.78175 | 2025-11-17 11:38:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 90b3c638-6858-3ec3-ab45-b2a066e19103 | -10.09943 | -44.76172 | 2025-11-17 11:38:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b3fbc198-1180-35e4-b55a-4cb18429fb57 | -6.65799 | -38.38127 | 2025-11-17 11:38:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d39ef950-6c52-3e88-8b5c-99a9b89746fa | -8.69291 | -40.36925 | 2025-11-17 11:38:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 60633009-935c-39ce-972f-4ada6fa2d809 | -6.74621 | -38.07978 | 2025-11-17 11:38:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ab33c4e3-d164-3313-bdf4-9e5bbe2dfc42 | -6.12629 | -41.81554 | 2025-11-17 11:38:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 78959a13-0189-33ba-a721-8e45f482c2af | -11.40923 | -43.33104 | 2025-11-17 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9a908312-980c-3f1c-bb41-ae1206462087 | -11.76797 | -40.06069 | 2025-11-17 11:38:00 | TERRA_M-M | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 21b60e05-e0b4-3fa4-bc37-5b800fe1f298 | -6.20876 | -43.2698 | 2025-11-17 11:38:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 621fdb44-7811-38da-8ba6-9a3bd74e16ae | -5.89489 | -42.90381 | 2025-11-17 11:38:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 15f05cb8-9d54-34d4-be65-120bb889d8c9 | -6.13514 | -42.44876 | 2025-11-17 11:38:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 6dbcf677-7b1f-3f3e-bd71-92da56a5569f | -10.65327 | -44.60348 | 2025-11-17 11:38:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| f4e09b1b-9511-31e2-97e2-5f59833284ad | -8.31985 | -36.53305 | 2025-11-17 11:38:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9ab7cbbe-a152-3ce6-b9fe-ea58815664b4 | -8.30791 | -44.20348 | 2025-11-17 11:38:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 366747d7-ff47-37d8-9d29-1aa3983b1252 | -10.52694 | -45.38327 | 2025-11-17 11:38:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3248946b-bd4f-3d99-8e0c-721fcb1e94e6 | -9.98046 | -44.77287 | 2025-11-17 11:38:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| a06564b2-8e1c-35ce-9bc3-1611ab5212e9 | -6.74495 | -38.08857 | 2025-11-17 11:38:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6c6a742d-3dd8-36b3-a7bd-6d341c4cd22b | -9.61583 | -44.36789 | 2025-11-17 11:38:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1c238877-9ced-35ed-9b7a-686ba7b1cd78 | -6.20817 | -43.25956 | 2025-11-17 11:38:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3cd469e6-84f2-34ce-9413-736fbde32c3f | -6.65926 | -38.37247 | 2025-11-17 11:38:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 21.7 |
| c58362e2-37a2-3497-85a5-af83c5fff02a | -10.09664 | -44.77935 | 2025-11-17 11:38:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2a612f80-8ed5-3cf2-9d75-f8a9d50d68b7 | -7.36775 | -38.82862 | 2025-11-17 11:38:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2493e140-37bb-3b57-b46e-61971dc7ae1a | -11.99338 | -43.27533 | 2025-11-17 11:38:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2bbb6cec-66f3-32b7-a73b-dcd376ce5b25 | -7.7536 | -37.48563 | 2025-11-17 11:38:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 27.9 |
| b108a8b0-56e0-3b78-8751-d34da2e3b1f4 | -10.60261 | -42.31746 | 2025-11-17 11:38:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 1337373d-9788-3b1e-b8d9-ee19fee6d7bb | -9.61919 | -44.37883 | 2025-11-17 11:38:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f529f099-1f26-3a0d-94fb-812247a0d15d | -8.79696 | -41.09863 | 2025-11-17 11:38:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 5fffc893-6db9-3524-afa9-9264a6a07c83 | -7.31666 | -38.48167 | 2025-11-17 11:38:00 | TERRA_M-M | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 59664430-5bed-3618-87af-9722d8837f13 | -12.29903 | -41.20819 | 2025-11-17 11:38:00 | TERRA_M-M | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| cd22efbd-18fc-3093-af4e-2398372341a1 | -11.41131 | -43.31783 | 2025-11-17 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8dcd87d1-b2a4-33a1-aefa-a20caa1c036f | -10.10324 | -44.76921 | 2025-11-17 11:38:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 1959d87d-63e7-3968-ba61-563e5b327876 | -8.94751 | -40.83639 | 2025-11-17 11:38:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 376bb732-67bf-30e1-b2ac-d403f812ce73 | -7.33093 | -37.46941 | 2025-11-17 11:38:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 656936b5-dc57-3748-87e0-22bce8d62954 | -8.3106 | -44.18647 | 2025-11-17 11:38:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e9c8c284-c07f-38b7-80e3-d07708e6e77c | -6.68641 | -42.03131 | 2025-11-17 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| e798ad39-793a-3490-bad0-59c1ef928069 | -7.72691 | -37.48194 | 2025-11-17 11:38:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 3d284834-d6b4-3fe9-b566-c9e94a9be6cf | -6.90561 | -38.89481 | 2025-11-17 11:38:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3eace860-7b15-3b5c-bf47-2eb04421e1c6 | -7.32964 | -37.47844 | 2025-11-17 11:38:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 06d145be-f594-3dac-8660-dc22d6473128 | -7.47191 | -37.97952 | 2025-11-17 11:38:00 | TERRA_M-M | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 15.3 |
| d929bd6f-15c4-3487-9efb-9cc690d1dee1 | -6.1331 | -42.4625 | 2025-11-17 11:38:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 1236d21d-c0bd-36dc-9867-e5d7a127c69c | -9.07754 | -40.39231 | 2025-11-17 11:38:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5e151700-db1e-36f0-a18c-7520e7d66998 | -8.3199 | -44.20526 | 2025-11-17 11:38:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 70dc8beb-f79f-38a8-b23e-bb5dd77cafbe | -6.97969 | -37.61134 | 2025-11-17 11:38:00 | TERRA_M-M | CONDADO | PARAÍBA | Brasil | 2504504 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e0527f4f-89a4-3147-99c1-2af8a0a9e95a | -7.70896 | -42.94171 | 2025-11-17 11:38:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 69aea0e6-4481-3860-acc9-23a19669acdb | -7.47065 | -37.98837 | 2025-11-17 11:38:00 | TERRA_M-M | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1639281e-9127-358a-aaa9-99683259970c | -6.68451 | -42.04371 | 2025-11-17 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 095848e4-17f6-3fcb-addd-030896c3580a | -10.64144 | -44.60152 | 2025-11-17 11:38:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 254b21ce-0374-3d96-a7fd-f7e15098545a | -9.62491 | -44.38668 | 2025-11-17 11:38:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| ca87decb-2ce0-3c11-b252-504b219e3c46 | -7.74111 | -37.18048 | 2025-11-17 11:38:00 | TERRA_M-M | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 91c0e8f2-bbab-3e82-bfe0-dcde25318e9d | -9.45499 | -44.8609 | 2025-11-17 11:38:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 274529e2-5d04-31cf-a6e6-d38e899e42da | -6.14009 | -42.44159 | 2025-11-17 11:38:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| cc2ed3ab-095e-3f08-8522-cdc644070b6f | -7.54775 | -37.38011 | 2025-11-17 11:38:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 563ccf2c-5415-387e-b86a-3f0f6c85fccd | -7.89723 | -37.58242 | 2025-11-17 11:38:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| cf1f5fe0-ba86-34d6-aff1-f30e9bf75aba | -8.69436 | -40.35958 | 2025-11-17 11:38:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d06ed153-4157-3c51-b4c4-697405ad268e | -6.79669 | -37.66388 | 2025-11-17 11:38:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 10.0 |
| da5dd5f4-71a3-3515-a4aa-8df7464ab203 | -11.76663 | -40.06979 | 2025-11-17 11:38:00 | TERRA_M-M | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| dfc45fd5-4c6a-3887-a0c0-8712e76ccf36 | -8.32118 | -36.52332 | 2025-11-17 11:38:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 09d24fc3-408d-372e-ae3e-3a8db207962d | -7.8985 | -37.57342 | 2025-11-17 11:38:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8fc00d50-76d5-377b-98ca-9e6a025e69a6 | -6.89877 | -38.6316 | 2025-11-17 11:38:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 21ba1cd5-b867-3955-aa64-a00e79f3c7a0 | -11.68414 | -44.72526 | 2025-11-17 11:38:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 26a062d2-84d9-3ecf-b645-01ccad80fc5c | -6.13797 | -42.45516 | 2025-11-17 11:38:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 91ed60cd-0c8d-3fe4-9e08-202df6c1acf1 | -6.84603 | -38.35752 | 2025-11-17 11:38:00 | TERRA_M-M | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7487f354-4bb2-331a-b601-ca1f443ae466 | -3.2116 | -43.3726 | 2025-11-17 11:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b6637878-0fea-3629-af8d-ccaeeec619ea | -12.83199 | -43.15776 | 2025-11-17 11:40:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 13cd17e1-09bd-3413-9baf-91ee2f519636 | -13.82098 | -43.46429 | 2025-11-17 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |


[Clique aqui para ver as próximas entradas](README53.md)
