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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6919c506-334e-3502-b21f-0e9dab82c63f | 2.36514 | -60.79992 | 2025-08-05 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12f14fda-ac97-3c96-a30d-9513ff0b8c70 | -6.27059 | -57.40532 | 2025-08-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f21cbc92-fd09-3bad-b384-306b78954df3 | -7.42608 | -60.6279 | 2025-08-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0128803e-44da-3222-8c6f-e8e1fad1e193 | -3.49502 | -59.36932 | 2025-08-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ceb7f8fc-7734-33dc-818f-51c173a76013 | -6.15134 | -57.91567 | 2025-08-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f22ff515-be72-3a5d-af2a-6450478de8fd | -9.6964 | -51.94086 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8ac9d76-68a2-3c45-8446-b32b6cb16874 | -6.68251 | -49.79119 | 2025-08-05 05:29:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac47be6a-1783-33cb-b35e-624a38bdbc64 | -6.65491 | -59.10017 | 2025-08-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da9e6f3f-3e6d-329f-bfb2-59f6a84dcbed | -6.14678 | -57.91984 | 2025-08-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83199499-5e49-37ca-9a31-82a23452f282 | -6.15904 | -57.91688 | 2025-08-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1227b8eb-a0c9-3b4a-b300-e700668e6fae | -6.67976 | -49.79509 | 2025-08-05 05:29:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3134928d-ee4b-30cf-9180-7b6c05242e2a | -6.68172 | -49.79694 | 2025-08-05 05:29:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 977260e8-b38c-3e51-897e-1bfe32869456 | -6.89845 | -52.86482 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3489fb1f-1a80-3df9-8aa4-49601f4b4895 | -6.15519 | -57.91629 | 2025-08-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7733469c-a93e-3e83-be0d-c1962312b57c | -6.65296 | -59.10625 | 2025-08-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 133a67eb-1884-3d40-baca-483be6c855ef | -6.90392 | -52.86565 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2fc88d5-5e13-35ee-a231-87821250fe92 | -9.70245 | -51.94165 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a713c144-1609-3bf5-a638-4b381822fd4b | -4.41548 | -54.85767 | 2025-08-05 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43831c82-d703-376d-91f3-a681fc5d162e | -3.65503 | -61.65646 | 2025-08-05 05:29:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 091cabd3-07fe-3ee7-a11a-1f8be4731f70 | -6.90325 | -52.86387 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da48c85d-23e5-3a9c-8857-9dff38e89264 | -6.89777 | -52.86306 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a9555f8-c54c-31aa-b561-5bf136dd5dcd | -5.98931 | -49.91291 | 2025-08-05 05:29:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 836be90a-789f-368f-8e2f-ab006c9dcc93 | -6.65361 | -59.102 | 2025-08-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f21eebc-ccc9-33b7-bf91-b160b7b33bc2 | -6.01216 | -52.15166 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1b0b62e-a1cd-382e-93f6-157e7c891755 | -9.6947 | -51.94192 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b003c64-eb0e-3857-b8ad-5f73ce221e93 | -5.77774 | -51.66493 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c37738ef-e72f-396f-abe9-ac23d4d96b21 | -6.15062 | -57.92048 | 2025-08-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e828127-6d4f-3070-a5ec-2a796e2ca4d8 | -6.0116 | -52.15562 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a5cbe66-da0e-30d3-92cd-a8a05d99008f | -6.90274 | -52.86751 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4287dd14-db0f-380e-91e7-45e248d5f044 | -9.69584 | -51.9455 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d0257f1-3b5f-3cbf-a271-0d9548571305 | -6.65426 | -59.09775 | 2025-08-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eafbbbb9-9a8b-3bb1-bca6-b92a877464db | -9.69411 | -51.94653 | 2025-08-05 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2ba10e7-e454-3f97-bd99-dd13a69183ca | -7.42552 | -60.6316 | 2025-08-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aca06ba-197d-3618-9bf4-d33aa32928fc | -7.04544 | -55.43837 | 2025-08-05 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 450bf9c5-edda-3256-994b-11d5e43d1626 | -3.49444 | -59.37313 | 2025-08-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7816c972-b214-3b8b-a5c7-969549ac3b2f | -6.65428 | -59.10443 | 2025-08-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4e0edba-1237-3813-bb40-2541988dce2b | -8.9478 | -46.7354 | 2025-08-05 05:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d4ac41fe-92f9-3d09-9088-4eb76380a4fa | -17.2256 | -44.817 | 2025-08-05 05:30:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 41eebd45-bb47-3fe2-a1ac-604e6f362b4d | -13.0723 | -56.9131 | 2025-08-05 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 24e178c3-4553-3b40-994a-d7e6e13f0805 | -13.0538 | -56.8746 | 2025-08-05 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e049ac9a-7d50-3cd0-9462-ee9eb4e7cfbc | -13.0914 | -56.9114 | 2025-08-05 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ac46d2e8-9531-364f-a18d-168493a8ac04 | -7.994 | -43.1534 | 2025-08-05 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 8aff0386-dc2d-3db3-8d28-dda4cda48023 | -17.2056 | -44.8214 | 2025-08-05 05:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 6f464727-657d-31f8-b1a3-82fd77e3a80b | -13.08677 | -56.90913 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 67740070-87eb-3ea4-8d50-e6bf0e7e99ef | -13.08283 | -56.90385 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ddf8e13f-a83b-31a4-9548-1941b203959a | -13.04466 | -56.91266 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c861c5eb-6059-3896-ae02-f587bfe26324 | -13.04885 | -56.87984 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e08c686-4503-36b6-9504-5e88f3e15705 | -13.07224 | -56.87826 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c53557f1-cae5-3438-bcda-5952ec1cca73 | -13.06462 | -56.90142 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1fec7e0-654f-301f-8c56-25804b6ab69f | -13.0816 | -56.9133 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3957c49a-7351-3abd-9e0e-c5dda3aacf51 | -13.081 | -56.91795 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c1e27a90-28f5-3145-94bc-62552f985f3d | -13.08221 | -56.90858 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 94c88fad-78fd-3179-aef9-ae4a5c93bbe1 | -13.06706 | -56.88246 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0bec32cf-d2fd-3f0b-8592-f6edfd9f5431 | -13.08407 | -56.89433 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 754fece6-96af-3f24-be1a-382c92ceb9cf | -13.07162 | -56.88304 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bc5e6196-fcbf-3795-a7c6-c7ed85a73f9b | -13.08739 | -56.90445 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 026daa32-4798-374c-9a1e-ff17a68868de | -13.06007 | -56.90078 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35cf930c-2c61-30e1-b509-e1473a6aac10 | -13.0449 | -56.87442 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a283b1bd-1236-3b06-88bc-c86b3fed9aa9 | -13.04945 | -56.87513 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 61fb409a-c7d3-37f2-88ae-6570e0e0b11c | -13.0528 | -56.88524 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc74a424-b326-3720-92cf-e85eb27e3af5 | -13.0534 | -56.88055 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c5a6e08-9fdc-3dcc-a275-c95e04e33001 | -13.05856 | -56.87646 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76a770aa-66fe-31d1-821b-c947ce8d456b | -13.04035 | -56.87371 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b49595b-7f0f-33cc-a07a-a05cba73667f | -13.06768 | -56.87768 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7051eebb-18cb-39e5-8f94-7b7f3785f5f5 | -13.054 | -56.87582 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9bf8283e-98a2-311b-816c-a449388110ca | -13.07557 | -56.88836 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77409f0e-5fab-3ae8-9b66-3fba2c61e6cf | -13.08616 | -56.91383 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b58fb0d8-f66f-3de3-becc-8f7aefc11919 | -13.07619 | -56.88359 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7553b61-0b61-38e9-a2f6-9f18633037e2 | -13.0492 | -56.91335 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a14f81a8-7e94-3a09-8b8a-3438d4a025e7 | -13.0443 | -56.87913 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9316ce29-7d69-34c3-9791-71a745422ea9 | -13.04825 | -56.88453 | 2025-08-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16771bae-53ab-303c-90b3-69ab6909953d | -13.0723 | -56.9131 | 2025-08-05 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c02498a3-51e1-324a-bad0-c70deed8dac4 | -13.0914 | -56.9114 | 2025-08-05 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8158be0f-37ae-3d02-9a53-316bf206ae63 | -8.9478 | -46.7354 | 2025-08-05 05:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a9b777cb-8997-3b8b-a303-2e1877695fcf | -17.2256 | -44.817 | 2025-08-05 05:40:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 86071d62-6a61-3495-86ac-1ebeaceca51d | -17.2056 | -44.8214 | 2025-08-05 05:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 119.4 |
| acf632a1-0459-35b7-b5ff-07419cd50d4e | -7.994 | -43.1534 | 2025-08-05 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 0dd813d2-a011-3a23-b9f6-5201c4789223 | -13.0538 | -56.8746 | 2025-08-05 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0af6668f-8422-33b2-a80c-40be50f27138 | -17.2056 | -44.8214 | 2025-08-05 05:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c6c8b656-0f71-34f3-90b2-409b46b5df6a | -13.0726 | -56.893 | 2025-08-05 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 710b6c54-f551-3d28-89f5-71eb2757ad02 | -13.0914 | -56.9114 | 2025-08-05 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e30ffcbb-63d6-3a22-8df4-0f0166bba32c | -13.0538 | -56.8746 | 2025-08-05 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 89e2d606-6509-3c48-80e9-53d743df9168 | -17.2256 | -44.817 | 2025-08-05 05:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a57e2213-5d48-3e72-944f-09e9373266de | -7.994 | -43.1534 | 2025-08-05 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| c1054212-6fbc-3151-af7f-8db8a403a525 | -8.9478 | -46.7354 | 2025-08-05 05:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 31dbce79-e162-3cf3-bb13-243f0906e5a8 | -13.0723 | -56.9131 | 2025-08-05 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f2e8ab7a-2401-3bb7-b8c6-d3a765a59e12 | -6.65543 | -59.10194 | 2025-08-05 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 202ae908-d8fa-3133-bd55-e053a83345d8 | -7.42553 | -60.63341 | 2025-08-05 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cae4ac5-f06a-36ee-99f8-f2c4e9825120 | -6.64949 | -59.10478 | 2025-08-05 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b624816-5d03-3f8d-b4ab-6dd07afc26bc | -2.98722 | -54.50378 | 2025-08-05 05:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ccf29cc-45ab-38ab-8d1a-a6569a95b992 | -3.49284 | -59.37265 | 2025-08-05 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4eeaae5e-7db4-3ab2-ac03-34bb701136a5 | -6.15362 | -57.92107 | 2025-08-05 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cd055fa-cee4-3f75-9f0a-22d5b592d1a4 | -2.98032 | -54.50265 | 2025-08-05 05:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 522738a8-01d1-323e-a58d-9183beaae9c3 | -6.1542 | -57.91687 | 2025-08-05 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80bfb9a9-085b-35d8-be60-21cb10be86e4 | -7.42646 | -60.63001 | 2025-08-05 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cff1e03-69c8-3ccd-853d-667ec13421b3 | -6.64899 | -59.10833 | 2025-08-05 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11890cba-e92c-39e0-b2cd-49abada1ef36 | -3.49328 | -59.36968 | 2025-08-05 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3478e94b-5cb2-339b-98bb-2efbf668aad0 | -3.49372 | -59.36671 | 2025-08-05 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dbe2b3b-2e56-366d-a97c-bc293a50b510 | -7.42631 | -60.62797 | 2025-08-05 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ee5b696-3fb9-3997-bd13-4a21499f74d7 | -13.06069 | -56.87741 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README29.md)
