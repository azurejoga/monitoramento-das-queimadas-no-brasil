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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e42c2d0b-7cd8-3cd3-b42c-4385e2a2b243 | -9.6091 | -45.3544 | 2026-09-18 15:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 62869296-e267-3db9-8119-6a4af55054ba | -9.769 | -46.0841 | 2026-09-18 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| a2171a8f-4605-365c-a85d-a69d888f654f | -9.7501 | -46.0863 | 2026-09-18 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4c0971d4-c2d3-38dd-a93c-291fe89f805b | -9.5505 | -45.4752 | 2026-09-18 15:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e243df58-3c58-3fe5-86e5-0bec864552e8 | -11.8115 | -46.8158 | 2026-09-18 15:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| ac8b0577-a496-3c77-9291-319018b4752c | -12.1453 | -44.2195 | 2026-09-18 15:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 117d3fdd-5b6a-314b-ab7c-8eac8f807439 | -12.998 | -46.9381 | 2026-09-18 15:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 02597609-345e-3d26-b405-6626ac89f988 | -8.6374 | -44.5029 | 2026-09-18 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| fe7981db-dba7-3409-a0d2-01fe32750914 | -10.3307 | -45.3112 | 2026-09-18 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a91e74fb-fa7e-382e-acf4-d21479037239 | -15.6557 | -52.7366 | 2026-09-18 15:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0a81431a-c7ab-38b2-8a05-d99262b5f4a9 | -7.1675 | -44.5589 | 2026-09-18 15:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 04a39381-9981-3950-8f0a-06a94aceb287 | -9.3251 | -48.1758 | 2026-09-18 15:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 04044a49-a372-3cf7-8ef4-62e563e282d4 | -11.2975 | -43.3851 | 2026-09-18 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 62494542-ca5f-3b7e-a7b1-b418e035932c | -11.2979 | -43.3614 | 2026-09-18 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 63fdcfb7-4bde-3952-8849-86b6b9455016 | -10.3116 | -45.3136 | 2026-09-18 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 00421ca5-a9b4-3831-b068-3219ed8b8c54 | -10.1168 | -45.6346 | 2026-09-18 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 391a5826-a6a1-3578-a937-16f0d8045dfd | -0.803 | -48.6825 | 2026-09-18 15:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 85d2ef85-341f-38b7-b92c-aba60f260c3e | -11.875 | -47.5902 | 2026-09-18 15:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b95d72c7-5ad3-3944-b2fa-8280e5fe71e8 | -11.064 | -48.2898 | 2026-09-18 15:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 8c65cbfc-3729-3ca7-a70c-706118822349 | -7.8221 | -44.8632 | 2026-09-18 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| dffa9ce5-22af-346d-bb95-5fa479969970 | -7.803 | -44.888 | 2026-09-18 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c0f94246-e7d3-3900-a706-218c6c3d7c6a | -14.1932 | -45.1606 | 2026-09-18 15:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 8b1c8710-a48c-381f-a94b-9ed6186a64ca | -2.0768 | -56.4282 | 2026-09-18 15:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2840103c-a3af-326a-adb7-0d129a4c8c92 | -15.6752 | -52.7339 | 2026-09-18 15:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8c373d44-4d02-3313-8779-4203bc305de2 | -6.745 | -45.483 | 2026-09-18 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| ac13b02d-7d2e-3857-b33e-47eebe3e11a7 | -7.841 | -44.8614 | 2026-09-18 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 0ec1116e-ef96-3bd3-b1ed-48fbe3c21b1a | -11.3171 | -43.3585 | 2026-09-18 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 9eb8b2fe-ba95-3b67-b38d-27064c20a714 | -2.0768 | -56.4282 | 2026-09-18 15:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d4aa8326-a0e4-31e8-9bac-9409a0308709 | -14.1737 | -45.1641 | 2026-09-18 15:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 233.7 |
| f020221e-29aa-3dc6-ba6b-eb798a2bc52b | -14.1742 | -45.1407 | 2026-09-18 15:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| ef4c7441-ca9b-3ddb-97fc-fb6b3c8f21ba | -11.4732 | -47.6649 | 2026-09-18 15:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e6827bd2-08d4-32d6-942d-0ebae57d6032 | -7.8033 | -44.8651 | 2026-09-18 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| e334bcb3-4691-3e77-b631-787222966ab6 | 1.2793 | -50.8926 | 2026-09-18 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4478a4e5-c0c2-3f4a-af6c-788727cccc21 | -11.3433 | -44.0376 | 2026-09-18 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 579.4 |
| ff07c6a5-fc4b-32a3-a29b-b9fc91e5cf2e | -11.8115 | -46.8158 | 2026-09-18 15:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 0cc840bd-538a-3905-98c2-fe250a6a8192 | -11.064 | -48.2898 | 2026-09-18 15:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 843a5de7-8731-371d-8f15-958e356ddde3 | -12.998 | -46.9381 | 2026-09-18 15:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 4c8a3464-8271-3f30-b72d-0e88f402fac1 | -1.6042 | -54.415 | 2026-09-18 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5de65dd1-67db-3485-86b5-9e67ed81f6a9 | -4.0089 | -41.2748 | 2026-09-18 15:40:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 140.1 |
| bfd7958b-ca84-3f30-9dd0-f2718e89eae7 | -11.3809 | -44.0788 | 2026-09-18 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 4a150fa6-0fb9-363b-a1e5-6196a645a230 | -9.769 | -46.0841 | 2026-09-18 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 6fc748bb-8a26-369b-8bc7-96a1650496b1 | -12.177 | -48.9623 | 2026-09-18 15:40:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d519d215-0dea-357a-8fdb-75b19b262481 | -15.6557 | -52.7366 | 2026-09-18 15:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 4a9fbc73-0449-316e-a3c9-847432f90dfc | -10.7733 | -46.1869 | 2026-09-18 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a47d0083-063a-3f0d-8d1f-777c8508351d | -11.4541 | -51.4754 | 2026-09-18 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c86a60de-602c-3526-b58e-72cc692bae10 | -11.3171 | -43.3585 | 2026-09-18 15:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 7bd0b7c3-3b34-3f90-9f07-3181e5da27d5 | -6.745 | -45.483 | 2026-09-18 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3e6e2766-42c8-379c-8cdc-c89c264e149e | -11.3621 | -44.0582 | 2026-09-18 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 59dad983-c7ff-3942-86fe-17c6dd91cf7a | -7.8224 | -44.8404 | 2026-09-18 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| cb28b5fd-4775-3f28-8392-d6c9aba51516 | -14.1547 | -45.1442 | 2026-09-18 15:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 13eef506-fe8f-3f8a-9191-5bf9cd5340d8 | -6.1838 | -47.5258 | 2026-09-18 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| a810d2db-126a-35ee-857c-651462939479 | -7.8601 | -44.8366 | 2026-09-18 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 41ebd712-6757-37c4-91e8-46d37990363f | -11.3437 | -44.0141 | 2026-09-18 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 0d77a4ea-5339-37cb-8b16-0e4e1c372f54 | 2.2003 | -50.8773 | 2026-09-18 15:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 85a4005d-4c13-3fe6-8032-a6f6238ff371 | 1.2611 | -50.7679 | 2026-09-18 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.0 |
| ab0843c5-4298-3daa-b29c-0a1a0ae06e27 | -1.6583 | -54.9329 | 2026-09-18 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 22985de5-a170-3b32-8776-778bf812d8da | -0.803 | -48.6611 | 2026-09-18 15:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1c21d255-2373-3ccc-bb93-d8920eb96366 | -11.3442 | -43.9906 | 2026-09-18 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 1c6157c2-1ea0-394f-b56b-f9a07e3990af | -1.6042 | -54.415 | 2026-09-18 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| c7fc51be-d4b2-38d5-888f-9f7802e0059a | -11.8115 | -46.8158 | 2026-09-18 15:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| bd7f2261-af01-31cc-8d5e-3600b397b23e | -11.3625 | -44.0347 | 2026-09-18 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| a979a74d-5d49-37c5-8bfd-70528803fced | -14.1547 | -45.1442 | 2026-09-18 15:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 230a7cf6-0b3b-33e2-b33d-3f7c3c018e5e | -11.3161 | -46.7699 | 2026-09-18 15:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d76e5ef9-1e24-3951-a947-ad092b14b8e0 | -1.7134 | -54.8924 | 2026-09-18 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 634a2d9a-95bf-3738-9f4d-93f802e2f6f5 | -8.58 | -44.5552 | 2026-09-18 15:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3036fd71-242c-3bc0-a8bc-4b8337283384 | -15.6557 | -52.7366 | 2026-09-18 15:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 743fedb1-d65e-3d4b-a662-d964d842d5e6 | -14.1932 | -45.1606 | 2026-09-18 15:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 692028d3-15d3-3b95-be44-f11191a02a56 | -12.126 | -44.2225 | 2026-09-18 15:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 62bffff1-1cee-3e19-ae71-eb781d00a611 | -11.3621 | -44.0582 | 2026-09-18 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 5ded0d61-28e1-39fc-8a78-8a943a7815e9 | -14.1737 | -45.1641 | 2026-09-18 15:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 9176a0f6-4504-3a0e-be15-b196d8a9ed91 | -1.3747 | -49.0177 | 2026-09-18 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b7df28b8-2f27-3a01-a200-f79c3781f8df | -7.8221 | -44.8632 | 2026-09-18 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a8e1977c-f96d-3989-a242-dc9ca612bc21 | -12.1453 | -44.2195 | 2026-09-18 15:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 09624741-7f64-364f-b92f-b7f04371951d | -11.064 | -48.2898 | 2026-09-18 15:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 061a6079-5213-3068-ab31-c7c98f862e60 | 2.2187 | -50.8769 | 2026-09-18 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 25e4fc59-b8e7-3c48-9243-1a4007abe669 | -0.803 | -48.6611 | 2026-09-18 15:50:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 69c8f1f0-7ed6-3779-aa8a-6a3a46519223 | -11.3437 | -44.0141 | 2026-09-18 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 9467a3db-cea0-3de4-8657-b07a0e26e224 | -11.3442 | -43.9906 | 2026-09-18 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 3f6b1365-aec4-3cc4-bfb4-8eda6366ade2 | -11.3809 | -44.0788 | 2026-09-18 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| bd3607d5-674f-3abe-bb38-2f04cec41e47 | -14.1742 | -45.1407 | 2026-09-18 15:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 0e715e63-e71c-37bc-95c4-0b1b0fe65c29 | -8.3769 | -47.236 | 2026-09-18 16:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b40c4fa6-4007-3210-8cf9-4549ca3baa3b | 1.2794 | -50.8718 | 2026-09-18 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.6 |
| c10c871e-c141-3107-ac0a-1f22809e93c0 | -11.064 | -48.2898 | 2026-09-18 16:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 6624b9e7-0693-36d1-80de-1dc22d33dd42 | -0.803 | -48.6825 | 2026-09-18 16:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8b1271a8-adf7-3d82-ac5f-99f9c9e05939 | -15.6557 | -52.7366 | 2026-09-18 16:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 98e9193a-0780-3bfd-b53e-15160cacb6ef | -14.1737 | -45.1641 | 2026-09-18 16:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 198.2 |
| e5993037-82d5-38fa-b33b-ade26292c062 | -11.3437 | -44.0141 | 2026-09-18 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| aab8af5f-e881-34fa-87e6-feafe0cf6c0b | -14.1932 | -45.1606 | 2026-09-18 16:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 33401718-982a-3b5e-9112-7379ad27c444 | -11.3621 | -44.0582 | 2026-09-18 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 2e9ebfd9-8fdb-3c21-a1eb-0613485d9d53 | -11.3442 | -43.9906 | 2026-09-18 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 3f481937-56e0-3555-9c9e-09570fb51a2c | -0.4503 | -52.056 | 2026-09-18 16:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 404beaf5-ee0f-3feb-9a5c-b2f3ce868073 | -9.6091 | -45.3544 | 2026-09-18 16:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4493a7c8-5dfa-3077-9209-77701f463e0d | -0.803 | -48.6611 | 2026-09-18 16:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c3d2be5b-c515-34eb-8d3f-62f8f467b3b7 | -7.8033 | -44.8651 | 2026-09-18 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 7ca9b0b1-7337-38f3-ba11-778fc81dcd6f | -14.1742 | -45.1407 | 2026-09-18 16:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 9c3d7c86-f1b4-374f-a85a-5d7fbf85f62d | -1.6042 | -54.415 | 2026-09-18 16:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 1e7636cf-12a4-307f-9230-ed1f1f00834d | -7.8036 | -44.8422 | 2026-09-18 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 07ed00e4-3474-3c63-a9b1-286ab06084e5 | -11.3809 | -44.0788 | 2026-09-18 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 217.1 |
| c58eb17d-dc61-3d6c-b6ad-5b957684dd9a | -8.481 | -44.9102 | 2026-09-18 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 43671bd6-704a-31e7-9191-5e7aa09f2b6f | -8.5986 | -44.5762 | 2026-09-18 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |


[Clique aqui para ver as próximas entradas](README108.md)
