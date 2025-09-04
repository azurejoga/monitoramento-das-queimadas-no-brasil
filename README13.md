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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 302a6bcf-cfd1-3e9f-8949-8e63afd4c7ba | -4.9951 | -56.256 | 2025-09-04 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 66cf58f5-b400-3a26-99db-5ef68930e567 | -10.5746 | -55.4161 | 2025-09-04 02:40:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 4bbeed26-e72a-3f11-bab4-34b92e0551bd | -6.7649 | -63.1292 | 2025-09-04 02:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 449fa09c-c936-3968-a359-27202870cdfa | -2.9619 | -49.365 | 2025-09-04 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1dbc2691-7678-33c8-81b4-e2bba5173288 | -12.9009 | -56.9287 | 2025-09-04 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b9a062f1-aef0-3aff-bcb0-aa1bb1223bed | -6.6796 | -48.4049 | 2025-09-04 02:40:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 268a17cb-63b0-3a73-951e-ab85dbaf5a3e | -11.6838 | -57.3319 | 2025-09-04 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 3678840d-d7cc-3472-aaf7-a36594943571 | -11.0572 | -45.123 | 2025-09-04 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| af01f7d3-31bf-3807-98e4-00a710237edc | -11.6599 | -54.5297 | 2025-09-04 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 15117dd3-8795-34ef-8a66-1847477c71f9 | -12.9006 | -56.9488 | 2025-09-04 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9e94f717-9e05-3cc4-a235-8ebfc2124fc7 | -6.7504 | -58.7268 | 2025-09-04 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 166.2 |
| c8dc70f1-198b-3485-89de-23720ea80efb | -11.6647 | -57.3533 | 2025-09-04 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b5b78b18-49e8-3276-8224-58df8b5e4f06 | -6.7318 | -58.7469 | 2025-09-04 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 02afa713-ce26-3162-9449-6dab0bffe20a | -6.7319 | -58.7276 | 2025-09-04 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ce870591-11a0-3461-95ad-9f62d405a61e | -10.4475 | -50.3499 | 2025-09-04 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 47eccb56-9356-3c67-a99b-7bf31e673a50 | -9.5343 | -40.3282 | 2025-09-04 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 47e89b32-1622-3216-9c80-d2cecb409b68 | -5.6079 | -45.0265 | 2025-09-04 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f4b2349d-e5b4-3c9f-a938-181cba7d892c | -10.5934 | -55.4146 | 2025-09-04 02:40:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f0860a60-5d70-3369-935b-5b303be06cc8 | -11.6836 | -57.3518 | 2025-09-04 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| b35d8431-18a9-3313-a50a-abebf700cc74 | -6.7503 | -58.7462 | 2025-09-04 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 6aa7b7e3-3997-3d92-881e-eb19f4cd1897 | -10.4472 | -50.3713 | 2025-09-04 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4bb7c7ca-f45f-3a6f-9494-0e6cbcc4d115 | -6.7465 | -63.1297 | 2025-09-04 02:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b0cc711e-5785-3940-80a2-08e9f0cc4d52 | -11.0568 | -45.146 | 2025-09-04 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| b35017dd-4131-37c2-8c74-361b495e1ead | -11.0381 | -45.1256 | 2025-09-04 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 627dab2d-4ccc-3606-9ccd-da30d18624ef | -11.6599 | -54.5297 | 2025-09-04 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b5ff9257-c7a7-3e64-a2e9-ba3039bceb31 | -6.7782 | -44.0876 | 2025-09-04 02:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 15e606df-74ce-367a-acc6-161f8ba4c79b | -11.6647 | -57.3533 | 2025-09-04 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7c93bbd0-09ad-3fb2-8cea-d01e5eaa5861 | -12.4785 | -48.0859 | 2025-09-04 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c1daa81e-68d7-3d05-9678-3b8717456041 | -10.5746 | -55.4161 | 2025-09-04 02:50:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8ee28f8f-f32c-30aa-bf37-d7da5e40ea78 | -11.0377 | -45.1487 | 2025-09-04 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 638f9936-9a8d-3c48-8143-31a1a6cf1496 | -12.4597 | -48.0663 | 2025-09-04 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4ad0dc97-1633-3e1f-bee6-efc9afd09d20 | -6.7504 | -58.7268 | 2025-09-04 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 29549c8f-b80c-383e-8834-78d5855ef6c3 | -10.4283 | -50.3732 | 2025-09-04 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 634739fe-faaa-3531-a125-d9daeaea5b23 | -6.7319 | -58.7276 | 2025-09-04 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d8f052ce-cd8d-335a-9caa-86876cf9bfb9 | -12.8816 | -56.9505 | 2025-09-04 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 9ab54b37-6335-3b1f-8fe0-efb12fa32783 | -11.0572 | -45.123 | 2025-09-04 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4614f749-3245-35a9-85d3-c5d05ba47a02 | -6.7833 | -63.1286 | 2025-09-04 02:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1613b6b8-396a-3918-95af-3d53418d062b | -11.6649 | -57.3334 | 2025-09-04 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 689a9f82-a434-3f3f-8798-b30dcd3655a6 | -6.6796 | -48.4049 | 2025-09-04 02:50:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b72357a1-0a8a-3375-9372-74ea5a556289 | -12.9009 | -56.9287 | 2025-09-04 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cbf7afb5-92d5-35e1-bfdb-57778949b68b | -6.7318 | -58.7469 | 2025-09-04 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 225016f5-1c48-3845-a745-7a74b2dfa03d | -12.4789 | -48.0637 | 2025-09-04 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 034b6721-6549-32af-8a66-6570822e0494 | -12.4593 | -48.0885 | 2025-09-04 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 57e4b605-64d8-3dbe-b011-d889ae926106 | -12.9006 | -56.9488 | 2025-09-04 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| f15295ff-1e41-3123-8f7f-749178176720 | -8.3829 | -48.3317 | 2025-09-04 02:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2b56861f-294d-3693-91d7-beabc966bb33 | -6.7465 | -63.1297 | 2025-09-04 02:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4d22bf0e-f8c1-314e-8b75-1bb0985d762b | -6.7503 | -58.7462 | 2025-09-04 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b49c27ad-ae8b-3395-9090-a47e1303edb1 | -10.4472 | -50.3713 | 2025-09-04 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a0dce548-fe72-3533-9bb8-00846f1c62df | -10.5934 | -55.4146 | 2025-09-04 02:50:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ea408514-4206-3b66-98c1-d8ba083dbb4c | -6.7649 | -63.1292 | 2025-09-04 02:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| ef110ba7-4cfc-349b-810a-89101455034b | -4.9951 | -56.256 | 2025-09-04 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f7c5d6fc-6be9-3d7a-8e80-5fbf20f5ce81 | -11.0568 | -45.146 | 2025-09-04 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| d5beed77-1c35-3fea-9953-876ecd149856 | -11.6836 | -57.3518 | 2025-09-04 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| dbc6905a-ce0c-3094-b5b5-85a1522d391e | -11.6838 | -57.3319 | 2025-09-04 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| e0f98919-afa0-3e36-b9f1-42b6e7e7bfa2 | -10.5934 | -55.4146 | 2025-09-04 03:00:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b9271a22-af02-3792-aae5-7bf245c9afb7 | -11.0568 | -45.146 | 2025-09-04 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| afa420fd-1e1c-3e6a-a68d-42367427199f | -7.7252 | -50.3174 | 2025-09-04 03:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 169a549a-2f37-3e2c-bd82-67883a24ec5d | -11.6649 | -57.3334 | 2025-09-04 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 13ffd944-3252-3cef-9b49-7dd01ecc28b7 | -11.0381 | -45.1256 | 2025-09-04 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 12033e5b-097a-3632-b5ce-022a1c8515c6 | -10.5746 | -55.4161 | 2025-09-04 03:00:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7826d142-c96d-397f-8830-fc8d432079a2 | -11.6836 | -57.3518 | 2025-09-04 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 54a6e828-a854-3439-aa14-55db61b48fda | -6.7319 | -58.7276 | 2025-09-04 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 2f456136-4420-3531-88d1-69a2911c54e3 | -12.9009 | -56.9287 | 2025-09-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 30beb17a-594e-3656-b32d-a62b2701933f | -7.7066 | -50.3188 | 2025-09-04 03:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f4f9e2d3-d577-3e12-9b2d-c317bd349add | -10.4283 | -50.3732 | 2025-09-04 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 21e2be62-c4fd-3a1e-a456-4d82fc14192b | -12.9006 | -56.9488 | 2025-09-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 479342a4-f479-3dea-869a-70defeef47d6 | -6.7503 | -58.7462 | 2025-09-04 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 1633fcb1-1957-32df-92ba-1b291b96c4d5 | -6.839 | -59.3608 | 2025-09-04 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 372f5fee-4416-3b0b-87eb-d3a0f154bbf5 | -6.6796 | -48.4049 | 2025-09-04 03:00:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3760ad60-408f-3ca6-9487-89a25a257bf5 | -2.9619 | -49.365 | 2025-09-04 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 657eff3a-3bc4-390f-aece-4df54b0e3e86 | -6.7649 | -63.1292 | 2025-09-04 03:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 9eef7233-2cfc-3499-a755-a5206059327b | -11.6838 | -57.3319 | 2025-09-04 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9069cec3-4a37-3e87-9aed-1cf92c54c771 | -10.4472 | -50.3713 | 2025-09-04 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8c5ce678-761c-3d12-a2fc-2f02fbf7da64 | -12.8816 | -56.9505 | 2025-09-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 5078f5bd-120e-3e4d-bcde-4218dc23ca94 | -6.7504 | -58.7268 | 2025-09-04 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 89304258-93ce-3ef1-acc0-73bccc248cf9 | -11.0572 | -45.123 | 2025-09-04 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 6010a164-3adb-3f3a-93c5-89109ec79665 | -11.0377 | -45.1487 | 2025-09-04 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 9dc09386-bd57-3a9b-8524-6d735db4f719 | -17.1888 | -46.261 | 2025-09-04 03:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0d8a1066-956a-31af-bc7a-ff4624168c13 | -11.6647 | -57.3533 | 2025-09-04 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a5447630-7856-38b0-8356-1e8f4c8c4151 | -4.9951 | -56.256 | 2025-09-04 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 31b35e35-4eed-3b7f-a275-28e0e667332c | -2.9619 | -49.365 | 2025-09-04 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 495375a8-41a8-35db-b6bd-7cc03b73a2ef | -10.5746 | -55.4161 | 2025-09-04 03:10:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0059f688-84c1-3d24-812d-881edd6ff339 | -11.6836 | -57.3518 | 2025-09-04 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| aa90d6cb-b288-30ea-b548-a366181cf0b9 | -12.9006 | -56.9488 | 2025-09-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 5e2ffd93-d08e-339f-bbec-17e65006c12e | -11.0568 | -45.146 | 2025-09-04 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d2c332f8-39d2-326b-b911-95dcc3183407 | -11.0377 | -45.1487 | 2025-09-04 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 167ba74a-f403-3bca-88d0-2edfdd1bf713 | -12.9009 | -56.9287 | 2025-09-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1b66c7e8-523d-3e1c-b1a8-b56cced62fde | -6.7319 | -58.7276 | 2025-09-04 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 05b6a505-d836-3272-986f-a5e527f61828 | -6.7833 | -63.1286 | 2025-09-04 03:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f3777ad7-d02c-3c4a-ae0e-9c0d7e07883e | -11.6649 | -57.3334 | 2025-09-04 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 87f74068-1ea1-35b6-9443-32ea440455b0 | -14.6 | -48.0142 | 2025-09-04 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 67404b46-ec97-3d8d-b9be-086a80976248 | -6.7649 | -63.1292 | 2025-09-04 03:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 73d738b7-953c-3399-8657-92aa17bb77b4 | -6.7782 | -44.0876 | 2025-09-04 03:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 02fb887c-f318-3c04-8da8-c777dbeddfe4 | -6.6796 | -48.4049 | 2025-09-04 03:10:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a85462d7-241a-3bb2-a5d9-1843d7f44c57 | -11.6647 | -57.3533 | 2025-09-04 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f9ac6299-d1ed-3085-b8db-8cd6022c53f7 | -6.7503 | -58.7462 | 2025-09-04 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b71313d7-b19b-300c-a3e2-3d681a1c4b63 | -11.0572 | -45.123 | 2025-09-04 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 94807dbf-f2ea-3b11-9fd2-0cd025e78d9c | -6.839 | -59.3608 | 2025-09-04 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| da6af078-9458-3fdf-9325-f105dfd32164 | -12.8816 | -56.9505 | 2025-09-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7409090a-6e2f-34e1-801f-1c4691bef524 | -4.9951 | -56.256 | 2025-09-04 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |


[Clique aqui para ver as próximas entradas](README14.md)
