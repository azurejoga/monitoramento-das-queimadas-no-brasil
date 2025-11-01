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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47c8fd66-8cb6-3b02-9268-3535703f7530 | -4.86517 | -45.82753 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21d870be-6dcb-358d-a471-0af0b6129703 | -4.50344 | -45.67474 | 2025-11-01 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c72c0296-2d2a-3e6e-b913-463dccbf93a8 | -4.80688 | -45.87314 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12948c8e-5936-3026-a931-cbabb050c7ba | -5.23475 | -45.05624 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7268275-3ec0-3d91-9cbc-7e6bd232a878 | -8.12031 | -55.31273 | 2025-11-01 04:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc0dec3-499c-306d-ad67-c4b5f2c89fbc | -5.22584 | -46.16957 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a980d8e8-beeb-31b0-97ed-59e19f6a59ad | -7.0261 | -37.24649 | 2025-11-01 04:38:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6c532c8a-54f9-3b90-a0e0-5de04790fd10 | -8.15184 | -45.43762 | 2025-11-01 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 714f4d26-921c-3dc8-8fb5-a8556dfa223e | -4.84765 | -48.7565 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f676ebd2-4a00-328f-b34b-123695c63247 | -5.49127 | -46.86922 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d190cc-0937-3a9f-a7c3-45c61a62ffef | -4.67195 | -45.81398 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56bb3e17-263f-34f3-a14d-fe8992aa2f08 | -5.17433 | -50.07721 | 2025-11-01 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6514d523-6306-357d-aef7-2e28a9b62ec4 | -5.1166 | -43.3831 | 2025-11-01 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3f3bae41-6317-318b-85a9-03072dabb389 | -3.234 | -50.5789 | 2025-11-01 04:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b2b46b04-a1bc-3650-af28-332810c08869 | -12.99584 | -43.63842 | 2025-11-01 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f95e947-0fa0-37aa-be52-5d253f51885f | -13.75383 | -43.60078 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e2f2bb9-790b-32c1-aeaa-c5d17fc163a3 | -12.87602 | -54.74827 | 2025-11-01 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c71fec0a-9a9a-3571-bfe4-7b63e69075b3 | -13.8259 | -44.44884 | 2025-11-01 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72a397df-7ac7-3e10-af7c-0668f689960c | -10.63488 | -52.18327 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cb7fcf24-7edd-3a7a-b448-0f2fe5df6bc0 | -11.74532 | -59.30417 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f3e14de-366d-3a7b-ac63-2d6757ae20ee | -13.65286 | -44.40174 | 2025-11-01 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c035882-95a6-3858-99cc-683386bfe55a | -13.71528 | -43.78371 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 457e8a85-9ed3-3e44-bd6d-04945b35fe68 | -10.63622 | -42.31878 | 2025-11-01 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 601b4f37-ebdb-30a9-b44d-7176a2061360 | -13.67482 | -47.22141 | 2025-11-01 04:40:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fcbe8d0-dc78-3bad-b21a-5bfd63416827 | -12.87682 | -54.74363 | 2025-11-01 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad93061e-3339-3c66-9fd2-554883a91d7d | -12.76529 | -61.45988 | 2025-11-01 04:40:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b16bd5-868d-3ecb-b79d-115c34b2e39c | -11.38112 | -48.92895 | 2025-11-01 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0e50e5b-367b-3c3a-a64a-791be30a2f6c | -13.1461 | -48.44902 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff633bca-178f-3b45-952b-9004f3950e49 | -11.73846 | -59.31238 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ec5958e-0748-3469-98d2-dd4f7d28e0b4 | -11.73785 | -47.46701 | 2025-11-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce935762-1ab6-380f-907a-c3366644414c | -10.63829 | -52.18383 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa58dbb9-ef24-3a8d-b877-44d7eee6d6a5 | -13.38246 | -54.29729 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dd23290-eb1e-36cb-8a6a-e2c0baba61ba | -13.51826 | -47.10728 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4213436-4971-3962-b8b3-7264b9a56578 | -11.04828 | -47.90402 | 2025-11-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5338aa22-fe3f-302d-be51-baa8fbe0345b | -13.66741 | -47.22034 | 2025-11-01 04:40:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05ea2ce3-9c48-366c-b5cb-d0a862fecdc8 | -13.2014 | -48.31567 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01d41849-37b4-3daf-876a-bf632b5a1661 | -10.87187 | -47.55492 | 2025-11-01 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 460bd76b-ff23-3b5d-b6a6-b07593536e03 | -12.99677 | -43.63721 | 2025-11-01 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db503e2d-cb7a-39cf-950c-45b6ba9f152c | -13.20081 | -48.31965 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91c508a5-e6bd-3b24-bfc5-fd1a3640892d | -10.33991 | -44.64868 | 2025-11-01 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34261002-59de-386d-ad82-c93791c03715 | -13.16182 | -42.28539 | 2025-11-01 04:40:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ecb7d95-8290-3d0f-9176-a5a48bc35435 | -11.33933 | -54.37858 | 2025-11-01 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 058b7ce8-af77-33a9-9b26-95889ef8dbed | -10.63208 | -52.17896 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67668133-ddb0-3702-959b-f09adf92d4fa | -14.60698 | -42.88519 | 2025-11-01 04:40:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 630e6ee8-6481-3362-9621-23e9fdaeee7e | -10.6389 | -52.18007 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8e53ae2-e265-3bee-a15a-b85d4466d657 | -9.91299 | -50.50015 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b23e9432-1ac9-3f6b-ad42-aff0659f0df8 | -13.41124 | -42.99633 | 2025-11-01 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e8a07be-0dc1-36c9-9ecf-9b8c16fb39c0 | -11.37831 | -48.92477 | 2025-11-01 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adc8b631-8b40-3746-a0c2-b8328d6c3aa1 | -13.32784 | -60.71834 | 2025-11-01 04:40:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e72f24c2-f33e-39f9-b772-023598736aad | -10.53217 | -44.23057 | 2025-11-01 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90c7b2c9-70b8-3679-a5f0-e83a311be401 | -13.16072 | -42.28211 | 2025-11-01 04:40:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 640542ca-dc66-307f-a6bb-ec84ad98817d | -11.64079 | -48.60531 | 2025-11-01 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1899ef36-8cd4-36d6-9b8e-c03b385884ed | -10.62684 | -52.18965 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3ace4fa-6c91-3d5f-8d1b-6c27ec7a42da | -13.37603 | -43.59023 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 201d0192-b897-3c91-bf3e-fbdfbf4b1214 | -10.63026 | -52.19021 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc8f7437-f560-3d14-943e-f33bcbc962ee | -14.15174 | -44.32037 | 2025-11-01 04:40:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d8d4f4e-2125-3b28-8d71-308d4e12230d | -13.37668 | -54.28744 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f364f84f-cfd6-3572-946d-e67f191e1464 | -13.32856 | -60.71472 | 2025-11-01 04:40:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 510d69a6-7cf5-3cfc-a582-6c7644a69063 | -10.41157 | -44.35121 | 2025-11-01 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8772f2f-b14c-3d30-aab4-6b53b780df7d | -13.03388 | -48.2545 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b0c3278e-390d-35ec-b44b-3acb90b5ccfd | -9.91023 | -50.49613 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf1bd42-5371-3a93-9301-f02ee2b31e7b | -10.41524 | -44.35579 | 2025-11-01 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 761de5b2-5ec2-36c5-9836-8419fefffd45 | -9.91354 | -50.49666 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 678fbaa4-13f8-3a67-97bc-d0dcdc87c2b0 | -11.05176 | -47.90454 | 2025-11-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef6464c6-f1f3-3b2f-8b9e-55e93b42a584 | -11.72995 | -59.30133 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 163dc100-7f9d-3db6-9717-334ede3c902a | -12.02438 | -63.74525 | 2025-11-01 04:40:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02ff0039-bf52-3af3-8fe5-919cb4670029 | -13.74915 | -43.60015 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 30eb851c-bbda-3c0d-9652-189bd3dbbddb | -9.90968 | -50.49961 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be23e183-aaef-3587-8f72-fa69a0e03787 | -10.63694 | -42.31329 | 2025-11-01 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4fc325d8-ce7a-387b-8710-ab241d108800 | -13.32239 | -60.71726 | 2025-11-01 04:40:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 332b305e-4296-3395-9455-e64a6d0ffa87 | -15.03035 | -56.45889 | 2025-11-01 04:40:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aff810fc-0e87-3ec5-89ab-27e5b914b986 | -15.11755 | -42.25678 | 2025-11-01 04:40:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3360df5a-8fde-3a35-a974-c39020ec28d5 | -10.64171 | -52.18439 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4edfc3e-828a-3de4-a1bf-ea7440f2ebc1 | -13.37305 | -54.28681 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 663f5802-84b5-3141-89b8-50f95b445eec | -12.64165 | -46.7915 | 2025-11-01 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d782d848-f7a3-34e8-a2f9-836106e72cd2 | -11.97432 | -60.7316 | 2025-11-01 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b93e2db8-2aae-380a-a3df-b92a0f845c85 | -13.71136 | -43.78221 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ee35708-5d37-3be0-b286-b8db895e894b | -12.60196 | -48.33713 | 2025-11-01 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ddf93e0-8346-3d2e-883a-c927b61ffdcb | -11.97805 | -60.73203 | 2025-11-01 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d5848f6-ca32-3863-b20d-290350ef4357 | -10.41228 | -44.50562 | 2025-11-01 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69f34033-7512-37b4-9ef6-3408e171095e | -13.78908 | -43.25283 | 2025-11-01 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3c16c46-925e-361c-8f40-9274ce3ee54b | -8.63476 | -54.89509 | 2025-11-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b58484e-c7f5-3024-b5d7-d886094b3101 | -13.32167 | -60.72089 | 2025-11-01 04:40:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b6d4ed25-1299-3fd5-b976-bbc6e107bd4d | -13.38393 | -54.28872 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa0f20f2-76c6-36fb-9db3-317c3c2dbd2a | -13.38682 | -48.52918 | 2025-11-01 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db04df01-5aa0-3191-acc1-ccef0919f269 | -13.6567 | -44.40381 | 2025-11-01 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ed7646d2-c9d6-336f-a73c-a2e04b468334 | -10.79634 | -48.46295 | 2025-11-01 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bdc42ae-5926-3297-8583-af81316ca4d4 | -13.33418 | -43.18666 | 2025-11-01 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79bbc787-1787-3e7a-b64e-0d2f42de859d | -13.1658 | -42.28283 | 2025-11-01 04:40:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 474ecee1-b021-3011-b147-558ef58de679 | -15.11234 | -42.256 | 2025-11-01 04:40:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c70fce67-35cc-39e2-a035-ff0486626882 | -13.20978 | -43.12983 | 2025-11-01 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 04098df0-337f-3653-a19b-a3b41ce06fb1 | -9.91629 | -50.50068 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c44595c3-dd0b-3719-875b-9f91743cfb16 | -11.97243 | -60.73111 | 2025-11-01 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb436532-ffc9-306d-9134-4af1fdccceda | -13.34455 | -48.33187 | 2025-11-01 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad3a0198-b318-36c6-8d0e-4aa1eb1cc112 | -9.91244 | -50.50364 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8514e080-0912-3ff7-9403-a1aaaba81a1e | -13.19733 | -48.31907 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4d69a1f-337d-34b1-9a8d-9c17de344518 | -10.15294 | -43.91925 | 2025-11-01 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7746f5ba-1a1d-3297-930b-5000f93f89d3 | -13.71073 | -43.78714 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3167c712-b9ad-33fd-a751-d65f081d3a7b | -12.91126 | -45.06767 | 2025-11-01 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14597d91-0583-3ed1-abd6-3b5c9cf2bde3 | -13.39281 | -48.4649 | 2025-11-01 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
