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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4786244-5cc5-350e-b87f-08c38f79f483 | -4.32595 | -50.93791 | 2025-12-04 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dbfad2d-514f-38e4-aa84-f2be8c86a829 | -5.22191 | -43.96411 | 2025-12-04 04:21:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ffdff18-55d0-3e52-bf2a-40ac1aaea659 | -3.04232 | -48.41661 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9630ef44-90dd-3a85-8435-197f187e3c2f | -2.53683 | -49.45528 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8a039360-0c90-3a8e-a26d-92b0b906e9a2 | -4.21034 | -44.2566 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80451cea-279c-3339-830c-49ff1e738b9d | -2.8288 | -48.44308 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c42f0ba5-de7f-36f2-8d21-67ae9d4e66db | -3.38654 | -47.2775 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7687e956-caea-3bef-86dd-9ae21cd7681a | -4.69692 | -45.70211 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f805bac7-97e2-3412-917f-559d451fda2a | -3.7921 | -43.60202 | 2025-12-04 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4cf4873a-b1a5-354d-9955-e62c9dc6c0c8 | -4.39854 | -43.1354 | 2025-12-04 04:21:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1715ddea-a441-3275-a24a-494ae55ddb4b | -2.53139 | -49.46234 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 78e5ad45-ac6d-3e17-a6d2-63b1fb770a82 | -2.48398 | -47.83158 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c218d7d-0cdf-36d7-b412-25dcd10e6420 | -3.72235 | -45.58261 | 2025-12-04 04:21:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d97768f5-2696-3d38-9caf-32e5dd22adfe | -2.07965 | -48.37455 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c64a885d-8d28-354e-bac6-e425dcbae90f | -5.56804 | -45.41964 | 2025-12-04 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5be17e56-bac2-300f-af39-0ebd09aa990c | -1.12254 | -53.44341 | 2025-12-04 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a157a2fc-aab4-3763-b66b-e809169ff241 | -2.54164 | -49.45213 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b29c5539-d99c-3b17-b51a-13d93ec5f5b0 | -3.32979 | -44.38241 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9f613c7-d91e-3804-a2d4-a772548c9979 | -4.52106 | -44.65867 | 2025-12-04 04:21:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47c88fd3-9b36-321c-98c8-8ef8cfbec1d2 | -4.68934 | -46.43702 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bf41737-f970-3fa7-8442-7da85259da68 | -5.68982 | -47.5086 | 2025-12-04 04:21:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a921678d-f27a-3e23-9f92-317e8b1fc859 | -4.05153 | -50.52742 | 2025-12-04 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4016ff25-c981-31fd-b5e7-a6fd78c85a31 | -7.12813 | -44.75728 | 2025-12-04 04:21:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 366ddb00-86a8-3cef-ac0c-f0b03e62e81e | -2.42114 | -45.79626 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3114df03-1c2b-3ece-8ec0-e07917d95fa4 | -3.66288 | -43.60266 | 2025-12-04 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f7e623a-55e6-32b8-957d-82ad28d71da5 | -1.87899 | -50.96177 | 2025-12-04 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 140a428a-1c24-38a2-be8a-896c1be4ed45 | -4.50664 | -40.51007 | 2025-12-04 04:21:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12ed260f-b92a-3a79-a7a7-34fb548078ba | -4.20704 | -44.25609 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13277e62-7ea6-3180-ae11-1de4b6530311 | -5.22204 | -43.37125 | 2025-12-04 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f549f4f1-17a3-3e94-9be8-e2ae011c6844 | -3.36459 | -46.85501 | 2025-12-04 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5694af3-7d68-34e6-90e5-34974e1df91b | -3.18723 | -46.60448 | 2025-12-04 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8352103-eaf4-3ed9-acb5-855880037663 | -4.33445 | -48.76528 | 2025-12-04 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5df8930f-a8b7-3ee1-be66-7dc910f39b03 | -6.58403 | -44.67068 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0f6682f-a62b-353b-88c0-826101d52d03 | -5.00819 | -46.8543 | 2025-12-04 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d6e67a8-bfea-383f-9000-1fcb41b15eb8 | -4.59261 | -46.05318 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac5cca38-f7ad-3128-a132-ddb7bce7ae40 | -2.14267 | -47.87902 | 2025-12-04 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d11ef9e1-9097-37cc-8d5c-06a3f6ceaf5d | -3.36749 | -44.09936 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f2c2510-ea43-3d0c-83c1-bae0c87704e7 | -4.11755 | -47.29702 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8dc5eba-5fe2-35a1-9a52-621c36dba1fb | -3.95277 | -42.58924 | 2025-12-04 04:21:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df9707c4-7b28-3131-934c-6c7d02994993 | -5.92151 | -42.27991 | 2025-12-04 04:21:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 56c684c2-6947-3658-a7de-fd3baaa2cb67 | -3.72573 | -45.58313 | 2025-12-04 04:21:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 53e44fb3-1c77-3b31-95ac-01cc5b52ff72 | -8.16284 | -43.17227 | 2025-12-04 04:21:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab59dd98-62af-3ffe-ab21-4c5ed8fe4d89 | -3.68949 | -41.86572 | 2025-12-04 04:21:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0746cb0e-074b-36f9-a9f2-c3fe2b2e7f0f | -5.93031 | -43.52058 | 2025-12-04 04:21:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9b9db02-5ddc-3704-89e9-c7d2ca9058b8 | -3.21847 | -46.0602 | 2025-12-04 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 219ea2e1-e72a-3730-aeea-95c308f7c5ca | -4.80857 | -43.07504 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec8db915-fbb0-374d-99fe-1f6790f326f4 | -3.32977 | -44.16326 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38bb6805-3a13-38cc-b24a-2a4446956e24 | -4.90489 | -42.80736 | 2025-12-04 04:21:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a63323e-2b15-3d0e-b303-5856f8543604 | -2.44691 | -46.31275 | 2025-12-04 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9644ca0-0ff4-3a8a-b7f3-581196ca2a48 | -3.06846 | -48.03514 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| af81ca28-33ac-3e47-9694-0ea63dc7ed25 | -4.21418 | -44.25368 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8d3a7c-5fa5-3b58-a590-766cfd0e275d | -2.73476 | -49.49348 | 2025-12-04 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e32432f-003a-301a-a915-5370235ecc63 | -4.34584 | -45.79116 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a65fd0e0-989b-30b3-84be-cdc2498ef473 | -4.51871 | -42.78199 | 2025-12-04 04:21:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 926c14cc-9abd-32ea-a8de-db06c8ed8646 | -3.13769 | -45.48788 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 827520e2-4dcf-3002-a19b-31a6b375f4b3 | -2.53802 | -45.3686 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 5233a163-036a-3976-b3c4-495e6673c86b | -4.05223 | -50.52311 | 2025-12-04 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37aea20c-dbff-38a1-93e2-4072d785442e | -6.06788 | -45.93727 | 2025-12-04 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04c81010-0ae4-3551-a2fe-77f4f9dfbd1d | -4.05166 | -50.52697 | 2025-12-04 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f181eac6-1abb-3800-840a-f7ef7a53786c | -4.52463 | -46.47739 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f7cb8a1-7d48-3b15-9545-182bdb2fca1e | -2.60767 | -49.25306 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53c12a45-b7c0-35e7-9beb-c012801d2856 | -2.86034 | -45.24276 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ff5d8e-4371-3fc2-87e5-3dec9e556043 | -4.39562 | -45.54165 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b1ef952-41a4-324f-aa5b-3fd514afe73a | -5.35979 | -40.47927 | 2025-12-04 04:21:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc8c8ad9-620f-3307-b112-a08eb7cd6646 | -4.69814 | -45.62902 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad82fc59-61b3-37c0-938d-831aa431da79 | -4.54795 | -43.31324 | 2025-12-04 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8094b951-67a7-36b6-9277-302773b72c51 | -4.52697 | -44.23271 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79d7d974-a5d5-3ddc-96fd-9549cbb635a8 | -9.31196 | -35.64026 | 2025-12-04 04:21:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| acb14868-09d8-3731-abc2-e139c818497f | -3.93863 | -47.20664 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b3ebffa-2a54-336a-b17c-300eb6018363 | -4.58742 | -45.10241 | 2025-12-04 04:21:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 457c9e23-4261-3c04-b9a8-fbf66edeea25 | -4.3886 | -46.66816 | 2025-12-04 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3703a069-c075-3b10-b4b5-9d67f51b83ed | -4.83408 | -43.19887 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90350d20-3c46-3e8b-b88e-51fa758c2bed | -4.4351 | -43.86143 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d4c6172-b7b8-303f-86ed-351a8c4dd1b4 | -7.59205 | -45.89383 | 2025-12-04 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a12e6d0e-e5fd-3ddb-8336-065d87de8268 | -3.40739 | -44.99181 | 2025-12-04 04:21:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 47813357-6c2a-3c14-8dab-3a3f0cb2d711 | -2.41778 | -45.79554 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84406af8-57c7-3807-82b3-f93b207fe5e1 | -4.03505 | -46.97217 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c31503f-e8b5-3ca7-b970-ddc587c867ca | -3.81973 | -46.07673 | 2025-12-04 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a36d8626-c11b-3b98-beca-9bc781c72449 | -2.48202 | -49.41489 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2865b25f-4298-3465-9584-daf635302e9b | -4.02807 | -47.33941 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fb542c1-51ba-3b44-acf5-7879ef771346 | -5.33159 | -43.56434 | 2025-12-04 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd6815af-a46b-3ffa-a575-ca02693963b0 | -4.21196 | -44.24629 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33231d80-080f-3b5f-a962-9e9ac49cfe16 | -4.40294 | -45.38657 | 2025-12-04 04:21:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7479079a-35e2-343b-9a93-9b2433868762 | -2.57533 | -48.22268 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ee6c9c0-ced7-3cf8-a193-51444854e802 | -3.85222 | -47.05229 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31277d28-e9ec-331d-8ccc-2f1344065066 | -2.63331 | -48.03635 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58669d33-64c4-34ed-adca-ceedab5b4916 | -2.92782 | -48.23179 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e161b5b9-4f3b-39b7-8063-ef51c720995a | -4.37195 | -45.85411 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1aae072-1e52-347e-b0ba-c75b7620b172 | -2.28555 | -46.52599 | 2025-12-04 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42aadc69-dab9-325e-8be9-4ee6c9e8a81f | -1.1213 | -53.45101 | 2025-12-04 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9871e1f-e93a-302c-ac59-a072c6e7e4a7 | -4.24538 | -40.34626 | 2025-12-04 04:21:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71b7a35e-110f-3880-a61a-d3d6929837cc | -6.28466 | -39.68609 | 2025-12-04 04:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d86c010-923f-3fdf-bb76-8eeaf0998de0 | -2.38762 | -49.3882 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 72798fbc-a858-3a95-9f9a-2118bb819340 | -2.60354 | -49.25242 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98b511b8-8342-36ce-b62f-6677bbe37a32 | -5.02276 | -41.00611 | 2025-12-04 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| efa4b40a-9460-36e9-ae89-128fbf597db4 | -2.8637 | -45.24328 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7162a48b-54a6-3703-b6a4-31538d07613a | -2.42121 | -45.79608 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 72db43ea-c824-335a-b20a-8f9d3f326d08 | -6.64112 | -43.14609 | 2025-12-04 04:21:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34d514a7-f4bb-3a15-b739-3204376ad066 | -3.60355 | -45.66771 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcbf1b19-c344-3966-b26d-8fd751d95dba | -4.5993 | -43.35385 | 2025-12-04 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
