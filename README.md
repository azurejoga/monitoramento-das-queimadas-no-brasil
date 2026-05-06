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
| 2d2a252d-ff78-3e71-8516-ae3fe24a1c33 | -12.5031 | -58.4979 | 2026-05-06 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 93ee09b3-1429-3a0d-ad40-e429fccc5967 | -12.5033 | -58.4781 | 2026-05-06 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 180.7 |
| e60ba2f3-05f0-3ee4-80f9-410d086d86e6 | -12.5222 | -58.4765 | 2026-05-06 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| fbb1d9a4-f9cd-342d-afef-da6d392d37df | -12.4843 | -58.4795 | 2026-05-06 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| fa1bc5ee-31f6-3bfc-bc5f-6309486d8410 | -12.5035 | -58.4582 | 2026-05-06 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4a976aed-af41-371d-95f7-a877b1387cfa | -12.5222 | -58.4765 | 2026-05-06 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 97b8120e-a3f0-30c3-b69b-41ee90189b40 | -12.4843 | -58.4795 | 2026-05-06 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 09d4db08-7182-3abf-a3ec-b00b9970ed13 | -12.5031 | -58.4979 | 2026-05-06 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 13a4fedf-b850-3964-b138-86a41f754ef1 | -12.5035 | -58.4582 | 2026-05-06 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c0614ff1-b953-3ba7-84f7-1e81f82d7457 | -12.5033 | -58.4781 | 2026-05-06 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 175.4 |
| cdc77854-c584-3fd1-a7ff-a54aa7f895a6 | -12.5031 | -58.4979 | 2026-05-06 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| c72b5b16-5adb-3f54-a815-e447cda124b8 | -12.5035 | -58.4582 | 2026-05-06 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a4269cf9-6df5-392d-865d-4b2fbf3d4c44 | -12.5222 | -58.4765 | 2026-05-06 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| efae2e9c-4b70-374a-9b11-e85a0400f526 | -12.4843 | -58.4795 | 2026-05-06 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5ab80525-8ee2-3a2c-a352-6324811f7b0f | -12.5033 | -58.4781 | 2026-05-06 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 4860c21d-4320-384b-9e1a-06a34da5c7b2 | -16.416201 | -54.9025 | 2026-05-06 00:25:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2152b4ab-c97d-3b4b-8056-31b51c921770 | -12.3278 | -44.5704 | 2026-05-06 00:25:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5471d49d-1187-39d0-b9e0-b153ad643d94 | -12.4646 | -54.441898 | 2026-05-06 00:25:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 775cd757-5585-3da1-b899-f6a4a722d7fd | -12.3436 | -49.993801 | 2026-05-06 00:25:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5751ff56-af2f-3ee5-966d-e1b1d6632b27 | -13.9914 | -56.631699 | 2026-05-06 00:25:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6de3f2d0-db31-31c4-a74b-860b2b68d273 | -12.4946 | -58.452099 | 2026-05-06 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6083427c-e284-362f-b7ce-6d9e06c24124 | -12.4973 | -58.465801 | 2026-05-06 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3994de2-f8cb-3c11-8f78-8550ce0e9fe9 | -12.5071 | -58.463902 | 2026-05-06 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa139601-d8c5-3a51-8e4f-20c4c0dc441e | -15.6319 | -47.887402 | 2026-05-06 00:25:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 103d9589-8907-3d1a-95cb-f0fc8430bbaf | -10.9304 | -49.416901 | 2026-05-06 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5942e42-1d97-3304-a74c-f2c17d923083 | -14.0661 | -47.7785 | 2026-05-06 00:25:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45897f4c-97d6-36ad-81f1-8aa6e45dd595 | -22.6115 | -49.554001 | 2026-05-06 00:25:00 | METOP-B | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9a0e96-8223-3639-95d5-cec1d802741f | -17.800301 | -46.700298 | 2026-05-06 00:25:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1fed0f59-74a8-335a-95be-1a33aa55d788 | -12.2704 | -43.493198 | 2026-05-06 00:25:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e420523-6911-36fd-93ea-b5b55717edc1 | -18.080799 | -46.360802 | 2026-05-06 00:25:00 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d4a745af-8f0c-3c2a-ba2d-d59e904136d3 | -18.782499 | -51.931801 | 2026-05-06 00:25:00 | METOP-B | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 759a34d8-f740-3409-a0f9-b9b948005911 | -11.4352 | -55.0938 | 2026-05-06 00:25:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7085b0-9f44-3d32-8c46-6bc8472b050a | -18.431999 | -54.684399 | 2026-05-06 00:25:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8f7dd461-be80-375b-9ce6-f76564bd6209 | -13.7037 | -55.667999 | 2026-05-06 00:25:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d76277a4-f949-3f5c-8a6f-756d11cf62f8 | -20.211399 | -50.633801 | 2026-05-06 00:25:00 | METOP-B | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f69f3fe-005e-335a-8fe4-bd1bcd219612 | -10.5358 | -47.017101 | 2026-05-06 00:25:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34f40de2-a49e-326b-9862-d676daf4b7ff | -12.4629 | -54.433899 | 2026-05-06 00:25:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b11e0931-6bf1-3f67-bdf1-6ebc495155d1 | -19.949301 | -54.371799 | 2026-05-06 00:25:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2251010a-ef84-3a8a-a704-03c43e34cadf | -21.9736 | -57.571301 | 2026-05-06 00:25:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 670c1c4e-eeed-38e1-bf21-3c91e4f5dac8 | -21.983299 | -57.5695 | 2026-05-06 00:25:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3e597a68-b551-386c-b229-80e879aec159 | -8.6204 | -49.511398 | 2026-05-06 00:25:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb283c8-2dae-3a60-acf3-10456c60918d | -12.3314 | -44.5849 | 2026-05-06 00:25:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 167e4874-74c7-306c-b110-e4322fff0d73 | -21.195999 | -49.197102 | 2026-05-06 00:25:00 | METOP-B | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a651836-29d0-3974-a0cc-cb9339d21fe2 | -12.5044 | -58.450199 | 2026-05-06 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46d6aa5c-b992-3545-a6c2-0cebebaf2c72 | -15.6339 | -47.895802 | 2026-05-06 00:25:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| c71efb05-7d83-3682-8a46-c0b0129565be | -16.424101 | -54.890999 | 2026-05-06 00:25:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6d7756c-2602-3087-a1f9-2ba4b0440d3d | -18.0126 | -49.387501 | 2026-05-06 00:25:00 | METOP-B | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57c3397d-b417-3514-9f50-ee1f36c2d549 | -13.1828 | -52.679199 | 2026-05-06 00:25:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99047e43-7e3a-3052-b170-1c8d9bc3e799 | -19.9473 | -54.361801 | 2026-05-06 00:25:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d4ec5d67-5f47-3930-a717-0221460222c2 | -11.4334 | -55.085499 | 2026-05-06 00:25:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e31288f-2db0-3920-8f9d-bf8425c08f9d | -11.4432 | -55.083302 | 2026-05-06 00:25:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6531b1-9349-33a4-a38b-be90ea7f04da | -11.134 | -45.122299 | 2026-05-06 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e647f2b-6fbc-31ee-b60c-3947cc4e0b4b | -12.5001 | -58.4795 | 2026-05-06 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d574853d-2993-3933-96ee-8555eb9ef31f | -11.445 | -55.091702 | 2026-05-06 00:25:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55247220-ca63-3752-a917-817218457626 | -17.810101 | -46.6978 | 2026-05-06 00:25:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 35026e04-9ff2-3a3c-8ee5-bfdf8d00c976 | -11.2957 | -54.0158 | 2026-05-06 00:25:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d588d324-c940-3671-a61c-452126648473 | -21.712999 | -48.414902 | 2026-05-06 00:25:00 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b6e5570f-f3cb-3453-a97d-1f5dc9a963ac | -11.6185 | -48.042999 | 2026-05-06 00:25:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f226aba8-e9b1-3b87-85be-52eda1257b2d | -12.3504 | -50.023499 | 2026-05-06 00:25:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11a5d2a6-30e6-3318-bfa8-bd1390b2c1ca | -14.0779 | -47.784901 | 2026-05-06 00:25:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f12726c4-f6e6-31b4-bc0b-19393dd156f1 | -18.507 | -55.489201 | 2026-05-06 00:25:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 755125e8-1ed3-33f2-b8bc-1aeb1981bd2f | -12.3487 | -50.015999 | 2026-05-06 00:25:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94f42ce0-8cee-3c0e-a603-60234e7def9a | -23.703501 | -51.6674 | 2026-05-06 00:25:00 | METOP-B | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82d3c34f-de34-3b6d-9021-96712411d7e7 | -18.4438 | -54.6922 | 2026-05-06 00:25:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fbac370b-0a8b-3cf9-9246-f40a5a59fb81 | -12.347 | -50.008598 | 2026-05-06 00:25:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07951b6b-f54e-339b-958c-4eb616a47fc8 | -21.2789 | -48.966099 | 2026-05-06 00:25:00 | METOP-B | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6c58829a-b186-352f-8002-45a5bd7269ae | -20.212999 | -50.641201 | 2026-05-06 00:25:00 | METOP-B | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f52b2556-ccce-3841-b7d7-6fbea791b5bd | -13.4309 | -43.828098 | 2026-05-06 00:25:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9ac02ef-2673-3f5e-afab-8f9467e6d106 | -6.226 | -55.631302 | 2026-05-06 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc876ab-5b4c-3dbb-9df1-619712843167 | -18.497299 | -55.491299 | 2026-05-06 00:25:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1b086c33-8075-383e-9428-95c10a1f3cf7 | -12.4919 | -58.438499 | 2026-05-06 00:25:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2463d548-f89b-3fda-95dd-2ff41b3d2e3f | -12.2608 | -43.4958 | 2026-05-06 00:25:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 216347b5-010b-34ba-aa41-ac64d547a7fd | -18.434 | -54.694302 | 2026-05-06 00:25:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe727fa9-6946-3257-b639-f5af8e5112cb | -8.6185 | -49.503101 | 2026-05-06 00:25:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0acf11-46d6-3b8c-b6bb-ba364e07652d | -23.0847 | -48.603401 | 2026-05-06 00:25:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7e1b081e-18ae-3799-8e3e-b7adbb3d9a1a | -20.2253 | -50.746799 | 2026-05-06 00:25:00 | METOP-B | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f2aaa9d6-a8e9-3146-8f95-9ef09878a88d | -21.7113 | -48.407398 | 2026-05-06 00:25:00 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 838ce133-09cc-3357-925b-a635d12453a8 | -16.4279 | -54.909901 | 2026-05-06 00:25:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 473448a6-25cd-32d4-8097-66cb053a2111 | -18.499399 | -55.5023 | 2026-05-06 00:25:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f135dac9-bcb8-387e-8293-f34979eca61f | -21.9708 | -57.554501 | 2026-05-06 00:25:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2e0c245a-cac1-342c-bd22-4f39cee237bb | -23.0863 | -48.610901 | 2026-05-06 00:25:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 586e2983-ffaa-3e7b-9345-20fca0d7eb05 | -11.6438 | -54.153999 | 2026-05-06 00:25:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b44d232a-1ed4-301c-a0bb-c1d6f4807839 | -21.194401 | -49.189701 | 2026-05-06 00:25:00 | METOP-B | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99a7a4d9-1eea-3e3a-b85a-f2bbd3aafe5a | -12.3453 | -50.001202 | 2026-05-06 00:25:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0a6287a-d6e2-3ef8-9e3b-83af60d25388 | -18.078501 | -46.351398 | 2026-05-06 00:25:00 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37edc047-f627-38a9-aeb8-d152dbc3ad4e | -10.942 | -49.422501 | 2026-05-06 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 727d9fb6-5320-333b-9e61-155e3a3ebdc6 | -12.5017 | -58.436501 | 2026-05-06 00:25:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5f0d2df-8330-3e3f-b3ee-9e25a07aa7f1 | -11.1242 | -45.124802 | 2026-05-06 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f508f6b-36ec-3b75-85f1-be868ab0cb36 | -17.8025 | -46.7094 | 2026-05-06 00:25:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 609e2240-5248-3bad-9213-c2e14be2115d | -12.5141 | -58.4482 | 2026-05-06 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5957c0c6-4d5c-3e29-a835-eea19d74aaf5 | -16.1077 | -49.221298 | 2026-05-06 00:25:00 | METOP-B | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 507e5a44-01bf-3e98-8ca1-d2c672fe23b4 | -11.6422 | -54.1464 | 2026-05-06 00:25:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf1b2e6-7aba-39fd-a24b-1218b512d418 | -16.426001 | -54.900398 | 2026-05-06 00:25:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cbc2561-f0a1-3694-964f-4cb2601ce8e8 | -21.7983 | -50.757999 | 2026-05-06 00:25:00 | METOP-B | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8711990d-b2ab-3408-ad48-8dca1edb489a | -10.5384 | -47.027901 | 2026-05-06 00:25:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd06d5b0-be56-3bde-a158-e8625eec09aa | -14.0758 | -47.7761 | 2026-05-06 00:25:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 328bd27c-8575-3636-aa0c-7488773d97d7 | -14.0682 | -47.7873 | 2026-05-06 00:25:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc7822ff-92c2-30af-81b1-20b923067202 | -18.4359 | -54.704102 | 2026-05-06 00:25:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b49cba21-654d-3126-ad25-b1adadbb0417 | -12.4876 | -58.4678 | 2026-05-06 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1d9300f-d96d-3b8f-b7b3-1bd54eb20d52 | -16.427299 | -57.242599 | 2026-05-06 00:25:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README2.md)
