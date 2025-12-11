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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b0862d9-8be5-3668-9014-a0587c699863 | -2.2169 | -45.4159 | 2025-12-11 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 236.3 |
| 966c7082-184c-3c9a-9ef1-379c12813c80 | -6.0315 | -43.7105 | 2025-12-11 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 882a0544-6c63-3f08-b2c0-d8655b06f00d | -2.921 | -45.7971 | 2025-12-11 00:00:00 | GOES-19 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b58e240a-8c60-3408-8c1a-165266cac6d8 | -4.0866 | -43.6779 | 2025-12-11 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6042c1b4-5479-3f9d-990b-8f9bd684f3dc | -1.6944 | -46.563 | 2025-12-11 00:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 3c857f42-9a6c-3fab-9496-886611c4bba2 | -4.0865 | -43.701 | 2025-12-11 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 453577b1-5028-312b-a02e-16d9fc770c52 | -4.5322 | -44.0449 | 2025-12-11 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a568ec56-3522-3540-bad4-4fb37e534bbc | -3.2525 | -46.4075 | 2025-12-11 00:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 122.1 |
| f407841f-2fcf-3091-9c0b-13e8799ed5f0 | -3.271 | -46.4068 | 2025-12-11 00:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0a7bf80b-ef5b-3f4d-a81f-6e0f3c54e7a0 | -4.5508 | -44.0438 | 2025-12-11 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 47aa0d0a-419d-31e2-a29a-3f7567dc185b | -3.2709 | -46.429 | 2025-12-11 00:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 176fae11-5670-3711-ac46-a1a736fc4d24 | -2.2169 | -45.4384 | 2025-12-11 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1a98b014-e17a-3bfe-bf53-f48887abb194 | -2.217 | -45.3935 | 2025-12-11 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 602fb5a1-7950-3f03-9270-73391a735b28 | -1.6758 | -46.5634 | 2025-12-11 00:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a90de836-c86c-3ad6-9b71-3d3a64ecf83a | -2.1984 | -45.4164 | 2025-12-11 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3b855872-947e-3c25-8b60-af92866e903c | -3.2524 | -46.4297 | 2025-12-11 00:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 07f7bbf1-5b23-39cf-8d53-06e7e8d539d0 | -4.068 | -43.6789 | 2025-12-11 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0fce243c-d86f-3e23-ba9f-181d8e84be8d | -4.0678 | -43.702 | 2025-12-11 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9021f087-3c48-3929-9584-b70598d58c69 | -1.6944 | -46.541 | 2025-12-11 00:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 5642a4e8-6a46-37eb-bdc7-58c3c4d66e31 | -4.068 | -43.6789 | 2025-12-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 911501d7-19b0-305a-a0fe-65d2fa132391 | -3.229 | -47.4629 | 2025-12-11 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 063e62f6-0592-357d-a457-7f1317835bcd | -2.921 | -45.7971 | 2025-12-11 00:10:00 | GOES-19 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 34fcd7e6-8b16-32fb-adc1-644046ae98c6 | -1.6944 | -46.563 | 2025-12-11 00:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| c1b10e72-eabb-3d96-b966-8b7b01f2e044 | -2.2169 | -45.4159 | 2025-12-11 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 65fd842b-c539-3360-a1a7-0698c49e9925 | -2.9798 | -45.1214 | 2025-12-11 00:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 29ca0db1-6144-3f90-9843-70ad977c75dc | -4.0865 | -43.701 | 2025-12-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ab40abaf-b28d-39a6-94ab-aea7a9d984cb | -2.1984 | -45.4164 | 2025-12-11 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d73e9537-86f1-3f67-b817-b40dc4c1f632 | -12.5046 | -58.3591 | 2025-12-11 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 0154f6da-af93-34c5-b73c-9f9654bacd86 | -2.346 | -45.6589 | 2025-12-11 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b85fe19d-aca0-3f3e-bbc3-2e74d98fbeab | -3.2524 | -46.4297 | 2025-12-11 00:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| de5fe5d9-ce4a-32a2-aff0-fd832fdf98e3 | -6.0315 | -43.7105 | 2025-12-11 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| e0b4ac5c-8359-3d2b-b6cd-f80895c9dfcd | -3.2525 | -46.4075 | 2025-12-11 00:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 97.3 |
| b2381f47-089f-3a24-afef-bd89975a31eb | -1.6759 | -46.5413 | 2025-12-11 00:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 73cf3c4a-71b6-39fb-84b8-eb260b4fd758 | -1.6944 | -46.541 | 2025-12-11 00:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 39cb709d-e3ba-3337-a008-19e774666275 | -4.5508 | -44.0438 | 2025-12-11 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 81e1f9b5-ea15-3f0a-9753-30675ff3b5f3 | -3.271 | -46.4068 | 2025-12-11 00:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2b48b4c9-b2dc-3b62-9126-e43425f1d916 | -4.0678 | -43.702 | 2025-12-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 9c632c13-b528-3344-92da-01af75ee5784 | -4.5322 | -44.0449 | 2025-12-11 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b53354cc-3e44-3375-a8b8-20b0bf5856b4 | -1.6758 | -46.5634 | 2025-12-11 00:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| c0383ca0-bff1-354f-83e0-bbbaf490e0a6 | -5.35295 | -39.71353 | 2025-12-11 00:11:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 25.6 |
| d41db857-da99-3aa1-a70b-ad2739cfe309 | -5.59313 | -39.13745 | 2025-12-11 00:11:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 7f34e187-47f1-361e-a109-30f6c5656298 | -6.03664 | -43.7052 | 2025-12-11 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6b078d4c-9c46-3b8e-a859-b585ab0dbd14 | -5.98674 | -44.58712 | 2025-12-11 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d013544-3ac3-395e-ac43-58ad2f6492d9 | -6.02739 | -43.70652 | 2025-12-11 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 418cf687-d293-3a9a-9c4a-5a1a58584675 | -7.4576 | -35.2253 | 2025-12-11 00:11:00 | TERRA_M-M | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 43.0 |
| ad463d74-e31e-3dec-8dd7-549288658818 | -5.97907 | -44.59752 | 2025-12-11 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ebb5b5e5-a5bf-3e68-ab98-d96937cae74f | -5.35095 | -39.72003 | 2025-12-11 00:11:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 5e613ed4-a387-3efa-943d-71cf5d47c3fa | -5.55544 | -43.8115 | 2025-12-11 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| caa817ac-e230-31db-8e3c-444708bce76b | -6.28049 | -39.88251 | 2025-12-11 00:11:00 | TERRA_M-M | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b274f074-3d36-3107-9101-4709cfb95b06 | -5.57877 | -43.79194 | 2025-12-11 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e517733e-68d7-3b44-b851-e8567d18dc6b | -5.3484 | -39.70253 | 2025-12-11 00:11:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 6507c3fc-d09c-35b6-abf1-c293b54be698 | -9.57387 | -44.60094 | 2025-12-11 00:11:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efb05caf-8892-3ff4-9715-3d4646d08fa6 | -11.66962 | -47.12517 | 2025-12-11 00:11:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c687f1e9-87be-3a82-b671-2bd9fca88f75 | -6.9419 | -38.6144 | 2025-12-11 00:11:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 1ef471cd-dcee-3e81-9b20-bfd4ab05ff33 | -8.35612 | -42.04755 | 2025-12-11 00:11:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2b2661c8-4f83-3793-b21e-431aa2d77c12 | -7.45468 | -35.23086 | 2025-12-11 00:11:00 | TERRA_M-M | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |
| 006c01bc-b0af-3222-b18a-510bc1a328d1 | -5.98802 | -44.59622 | 2025-12-11 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 1f0cd31d-e195-3e3e-aa1d-0f11723986d7 | -5.3204 | -40.55522 | 2025-12-11 00:11:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 69d1ec95-fced-3e7d-99ab-e19d9510c671 | -6.02598 | -43.69675 | 2025-12-11 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ee8bfd5a-abf6-316c-8964-a6ed07aa057f | -5.56334 | -43.80045 | 2025-12-11 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 20c3adf5-65d2-3e4c-88e3-b8c6b8cc302c | -5.59768 | -44.37716 | 2025-12-11 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c7561f5-b1f0-3821-934a-bd273efd2f30 | -6.06069 | -43.74144 | 2025-12-11 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b8baa57-f0f8-35a0-af74-864991c187ab | -6.03803 | -43.71491 | 2025-12-11 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 51839390-8e85-378d-81f2-05f2e540062b | -6.28761 | -39.89249 | 2025-12-11 00:11:00 | TERRA_M-M | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| dc851736-3ea1-377c-9c97-6013be9168d6 | -8.06048 | -41.85246 | 2025-12-11 00:11:00 | TERRA_M-M | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 5109465e-9f2a-3f96-9571-e2c65699ea44 | -5.35438 | -38.06586 | 2025-12-11 00:11:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 30.8 |
| ed2ba05f-dab8-3211-aba3-dc38f2d7021a | -5.35764 | -38.05976 | 2025-12-11 00:11:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 58be661b-5375-3016-acaa-c1cf9c1539e0 | -8.35418 | -42.04223 | 2025-12-11 00:11:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 57096103-8d26-3332-8e70-82aade4c91d7 | -6.02878 | -43.71622 | 2025-12-11 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 640a28c1-20e2-39c7-a387-6aced9866e07 | -5.56471 | -43.81027 | 2025-12-11 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 25fed1a1-9d0e-3a13-a1b1-459770ca8429 | -5.57091 | -43.803 | 2025-12-11 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 918291fe-2518-3897-b347-65cc1011cca8 | -2.42356 | -45.27349 | 2025-12-11 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f5bc567-2cd5-35f8-ae85-1ae026a5c516 | -2.21358 | -45.41687 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 176.9 |
| d455ab75-abe5-36dd-a8c3-0c824d1e4414 | -4.39536 | -45.40577 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d64f854b-6abf-3179-9f05-7c6034d8ef4c | -4.34892 | -45.93132 | 2025-12-11 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91d830a9-df13-3ebd-95a4-56f1c4ba1cae | -3.21664 | -46.0653 | 2025-12-11 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1bf7cbc-214e-3823-bf10-0c0dbb8de037 | -3.84427 | -47.82539 | 2025-12-11 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 764b209a-4da5-32a0-9a7d-fe76af5bf6d0 | -3.17527 | -44.39151 | 2025-12-11 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 67a49549-e193-3ccd-a296-ba020725080d | -2.35729 | -45.65556 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 751638ec-663e-30a2-8147-895638ae7f84 | -2.52589 | -45.28054 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e8c274fa-a2cb-3d64-8f56-ee07ab77f6b8 | -4.46252 | -44.7598 | 2025-12-11 00:13:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de5a77ae-671d-3fbe-aa89-119a51aceac2 | -1.68775 | -46.55042 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 420.0 |
| ae4f9e72-c164-30f4-acc4-3dbf1d9d3972 | -1.68896 | -46.55918 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 74ae0e4d-2d3b-36b6-a7ea-ddb352409edf | -1.86747 | -46.64707 | 2025-12-11 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9cbdb97a-8c8f-37c8-89e1-8ce28d7a600f | -4.49786 | -43.4254 | 2025-12-11 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c34094d2-8986-3e38-b944-00b0106e503e | -1.10009 | -46.62461 | 2025-12-11 00:13:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd8e5329-1b38-3234-b381-1d6c8b5a8544 | -1.09128 | -46.62584 | 2025-12-11 00:13:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f42b70dd-a8b6-3fce-a26b-44856ba51f1b | -2.35308 | -46.35477 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73a354df-e1fb-3744-b1de-ffd854e9eb0d | -2.29185 | -45.65285 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e4adbe22-c33e-31db-a205-265bab487660 | -2.75083 | -45.63927 | 2025-12-11 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4f697275-68b0-306f-9093-1cd8162bf5ca | -2.26114 | -46.09618 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de040ab8-fc76-37ca-bb1f-96aaaac65d12 | -2.42167 | -48.26666 | 2025-12-11 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7dfbe36a-0d40-3062-906d-84dc0e5b1df9 | -3.36305 | -45.33725 | 2025-12-11 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46efa115-30b3-350b-8655-48e59e1acc03 | -2.68764 | -45.57552 | 2025-12-11 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4bc5d740-332c-3cb7-9c0d-cef1b4a7a3cd | -4.72285 | -44.31903 | 2025-12-11 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 050b683c-4149-3443-a42f-1915096e4f99 | -2.42298 | -48.27632 | 2025-12-11 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1ad42aa0-7d26-35d6-aaf0-b30cdd928752 | -2.6278 | -49.11094 | 2025-12-11 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a014d93-d617-33f3-9668-c3ce8f1b1ffe | -3.35578 | -46.20949 | 2025-12-11 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d096b03-d126-3f36-83f2-84a3a591cd55 | -2.12932 | -45.34238 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e9ff7350-e9f4-33c1-beaa-39707ede9558 | -4.64399 | -45.27077 | 2025-12-11 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README2.md)
