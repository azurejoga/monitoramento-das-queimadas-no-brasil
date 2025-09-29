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
| 94eaa2db-05b1-3d75-99cc-bfc71ab738bc | -4.4011 | -44.0985 | 2025-09-29 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8e154e0f-9f6e-39b8-9515-ce8fd4891e5a | -9.4192 | -54.7172 | 2025-09-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 49aefb9d-b114-3fc2-8f4c-43889c41c101 | -4.3826 | -44.0766 | 2025-09-29 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 59f2a4d7-3841-3200-aee9-4c36b4b50d63 | -10.0062 | -45.4204 | 2025-09-29 00:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 81cf2a89-856c-3525-9380-913a0459e2aa | -7.87 | -41.0609 | 2025-09-29 00:00:00 | GOES-19 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 2534a083-876e-334c-bf0a-7b99cbdb47e2 | -7.2026 | -44.7847 | 2025-09-29 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 45563e2b-021e-3a4e-b055-9e452dae0059 | -3.1013 | -47.0082 | 2025-09-29 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 58863310-daf6-34c3-8f42-551d887d56e9 | -9.787 | -65.0924 | 2025-09-29 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2b668782-a7fe-32cd-b669-13d509e80e5d | -14.553 | -48.4237 | 2025-09-29 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 199cddce-2bd7-372b-b2de-575f57a49f90 | -9.9875 | -45.3999 | 2025-09-29 00:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 83cad823-7919-33bc-953c-9d6a1d43234a | -4.4199 | -44.0744 | 2025-09-29 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 90d75061-741e-3d82-862d-460e527b35a4 | -14.8036 | -45.7248 | 2025-09-29 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3b29282f-66d2-3b4c-9574-4cae4107a393 | -9.7871 | -65.0736 | 2025-09-29 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e8ff6f8a-c734-32b9-92af-191e35cc9f86 | -15.2893 | -49.5035 | 2025-09-29 00:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 2683f989-fd92-33ac-9a34-ea97c41403fa | -9.7685 | -65.0743 | 2025-09-29 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 4065a771-04ad-3aae-afe9-533425a5121c | -3.1012 | -47.0301 | 2025-09-29 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 495e5fc6-24d4-3948-b732-36b0d5225a99 | -12.9435 | -46.7655 | 2025-09-29 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2070f874-3113-3286-acc0-2cd8c99a4152 | -7.2214 | -44.783 | 2025-09-29 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 268.9 |
| 947dc492-a6c0-351a-b31c-5154482d8455 | -4.7159 | -41.9736 | 2025-09-29 00:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 2cfab83f-66b0-352b-a8dd-74abfa6b9a46 | -10.0065 | -45.3976 | 2025-09-29 00:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 1f43dd4e-4dff-3578-b241-886ccf6ee793 | -14.7841 | -45.7284 | 2025-09-29 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 747eaab7-8e41-3f6a-a2f1-2040baf30677 | -14.7836 | -45.7516 | 2025-09-29 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a3e58394-ed44-31b5-a5b1-c374ff05e1e2 | -4.7157 | -41.9974 | 2025-09-29 00:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 40f9abed-6119-381e-ae32-d0395aff30b6 | -3.5972 | -51.9574 | 2025-09-29 00:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a393140c-1fca-3bd7-a1db-872fa092a385 | -9.4007 | -54.6984 | 2025-09-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f7cd9b09-d354-33c5-8614-1fd8d043ff21 | -4.6971 | -41.9748 | 2025-09-29 00:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 5045b5ad-cde2-304b-9fb6-28eeb160df5f | -14.7846 | -45.7051 | 2025-09-29 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 29f3ed42-3a0b-3c7f-9395-4d762366edb2 | -9.4005 | -54.7186 | 2025-09-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8c7f24ee-0a53-3760-852b-19043c04ec97 | -4.4013 | -44.0755 | 2025-09-29 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 69fb9243-b7cf-3b0b-bd90-b41f2ce4fbdd | -7.2399 | -44.8041 | 2025-09-29 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| cd96076d-50d1-30e8-8364-2eb9eef4707e | -11.6249 | -52.8416 | 2025-09-29 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 49ffdc80-2ecb-3e36-8a2d-b83cf3694fa5 | -9.4194 | -54.697 | 2025-09-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 16205ae6-df6d-3c34-b341-3fc1168f51ea | -2.5773 | -48.3931 | 2025-09-29 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 293b0f38-8c05-38a2-9a63-f0e27e6cd283 | -20.0491 | -41.3251 | 2025-09-29 00:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| a211ddc4-2356-3ba9-8179-cd09311fe54b | -7.2211 | -44.8058 | 2025-09-29 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 55022949-dd2e-3504-a827-1546586c6702 | -2.5772 | -48.4146 | 2025-09-29 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2f82f797-ec8c-3dfe-951e-d3a21c318f58 | -12.7687 | -46.8594 | 2025-09-29 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| af45d460-a530-3fe7-aba8-94873bd99e1b | -9.7684 | -65.0931 | 2025-09-29 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d4d724e3-0fec-3321-b095-7203f843a466 | -11.7609 | -47.5608 | 2025-09-29 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 053c8b34-2a9b-309d-b9c8-3aa4abaeea12 | -7.2402 | -44.7812 | 2025-09-29 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 97821bb2-9f03-3dde-ae20-f361e3f5cf6e | -9.9872 | -45.4228 | 2025-09-29 00:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 17beb421-6778-3e7b-890e-0745c69d6fea | -13.7506 | -47.9016 | 2025-09-29 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| c4ab7d73-a545-3e6b-9f69-ddb5c013f298 | -4.4011 | -44.0985 | 2025-09-29 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 60cc4412-70fb-3ff0-bd08-5dee422993a4 | -3.5972 | -51.9574 | 2025-09-29 00:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2483036b-2c1a-3f14-ae69-01da24335829 | -15.2893 | -49.5035 | 2025-09-29 00:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 5d2c5ed9-4524-3347-ada6-75d82225a4ec | -11.7609 | -47.5608 | 2025-09-29 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 802eee29-9c55-377c-8b08-122310c5ed0a | -3.1013 | -47.0082 | 2025-09-29 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 7c08eaa6-9022-36d4-b5b7-f8c70b5471a5 | -7.2211 | -44.8058 | 2025-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 50d2f9db-66b6-3930-b703-d8b654378634 | -15.2897 | -49.4813 | 2025-09-29 00:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| f54cac35-bb31-3631-bc93-99fc4b95f971 | -13.7506 | -47.9016 | 2025-09-29 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 2a7542d1-5345-33ce-9d04-a04f5283095f | -11.6249 | -52.8416 | 2025-09-29 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1ed425ad-f003-3456-ac95-b63138ccf160 | -14.553 | -48.4237 | 2025-09-29 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b88974f1-c623-3f89-91c6-2e441d72409f | -4.4013 | -44.0755 | 2025-09-29 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| c7f47008-095a-3843-9064-854e1fe844dd | -2.5772 | -48.4146 | 2025-09-29 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 40329637-9132-3ec1-b063-5ca39efef762 | -2.5957 | -48.4141 | 2025-09-29 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8b55da3c-c465-3e58-8617-e9326fa35339 | -7.2214 | -44.783 | 2025-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 272.3 |
| 515f35b8-f22d-3b0b-9361-14ca0d3b536c | -2.5773 | -48.3931 | 2025-09-29 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| be62a439-e81a-3cad-9aff-36180fb70579 | -3.1012 | -47.0301 | 2025-09-29 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2cf58368-ef4a-3212-89a6-5226d0f5be0b | -9.4192 | -54.7172 | 2025-09-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 4d8e7e75-f98f-39bb-9f48-0bb07b28713f | -9.4007 | -54.6984 | 2025-09-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1fce5b57-fc0d-3c0e-a004-bc39e6550659 | -15.2698 | -49.5065 | 2025-09-29 00:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 8366e970-bd78-3321-a5c2-e0115616bd7c | -7.2399 | -44.8041 | 2025-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 95f32791-9b04-390f-8e7a-0b901b9f3f21 | -7.2402 | -44.7812 | 2025-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 0077e5d0-64cb-3243-8e56-afaa2428dc02 | -7.87 | -41.0609 | 2025-09-29 00:10:00 | GOES-19 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 6c3c6279-d6ca-3077-ad7d-264aa2f62f32 | -9.4194 | -54.697 | 2025-09-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d5798950-045a-364a-80a7-1b6e79913136 | -14.7841 | -45.7284 | 2025-09-29 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 02cd849c-65fd-35f0-a385-95c786b28e86 | -20.0491 | -41.3251 | 2025-09-29 00:10:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| e39ac1b1-842d-3716-ba42-ad2a74fdc8e0 | -15.2698 | -49.5065 | 2025-09-29 00:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4182a16e-874b-38fd-9ddb-d3327125ddda | -9.4192 | -54.7172 | 2025-09-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dc827f77-b97f-348c-ab75-0804c199b9cd | -14.553 | -48.4237 | 2025-09-29 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 5f6255cb-02d7-35ea-8485-1cdebd0a9504 | -4.7159 | -41.9736 | 2025-09-29 00:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 2fe2a5fd-1970-3a7b-927c-6ad0e2cddf6c | -7.2402 | -44.7812 | 2025-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| bfc1fc78-5972-3f59-8682-c352be737406 | -14.7841 | -45.7284 | 2025-09-29 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4f997bf6-c7f2-3677-a65c-efa19b7c480b | -2.5773 | -48.3931 | 2025-09-29 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| fc724b00-7a6a-3c6f-98ec-3469e7a2291d | -10.8036 | -46.6787 | 2025-09-29 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8c0068fc-8b99-3b45-9669-064400a6fb7c | -9.4007 | -54.6984 | 2025-09-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c3aee483-5875-365b-826f-e58a791b3298 | -6.0623 | -42.466 | 2025-09-29 00:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 4d542e3e-074f-35aa-a49b-08b4f25c2e2e | -4.4013 | -44.0755 | 2025-09-29 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 699a71a4-5abf-3d58-bcfd-e9986a6350f0 | -2.5772 | -48.4146 | 2025-09-29 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 70c51706-eeb5-3e9f-9820-e475c9acd510 | -4.4011 | -44.0985 | 2025-09-29 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 0bba5c66-cd57-326e-a923-debfe7d4b499 | -7.2399 | -44.8041 | 2025-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| aa9523ed-0823-348e-aeac-63bff788dfc0 | -3.1012 | -47.0301 | 2025-09-29 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 18d1c9be-73b7-35a0-b55e-6f9330cce9ba | -15.2893 | -49.5035 | 2025-09-29 00:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 235.7 |
| ba138f51-396d-390c-8b8f-bc645acbb454 | -9.4194 | -54.697 | 2025-09-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d7958869-c5a0-3b07-b667-8d7f1806e25f | -9.4005 | -54.7186 | 2025-09-29 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a0e5f7c8-ba42-3824-938c-ae287acca5ec | -3.1013 | -47.0082 | 2025-09-29 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 70b44586-7e9c-3697-be08-cb016e427f16 | -7.2211 | -44.8058 | 2025-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| d0fbb199-352e-308b-9a6e-d127b11ee7a8 | -7.2214 | -44.783 | 2025-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 285.2 |
| a38c9051-061f-3547-bc04-034ea63eb620 | -15.2897 | -49.4813 | 2025-09-29 00:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| bace3206-715e-3c3d-bc79-e49be05c99da | -15.2888 | -49.5256 | 2025-09-29 00:20:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 54bdf543-fe68-3dd0-99b4-44b3783e8988 | -14.5336 | -48.4268 | 2025-09-29 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 940a4c3b-7ae6-3b1a-9c92-cc1421117fc4 | -4.7157 | -41.9974 | 2025-09-29 00:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 471ae2df-0593-3b45-91ec-eed9be868f9e | -7.5447 | -46.1115 | 2025-09-29 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ce9a0834-5337-3ee8-a295-8c600d8e6b5d | -7.2216 | -44.7601 | 2025-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3d8253d9-be2d-3805-9cca-54ff546b5852 | -14.5336 | -48.4268 | 2025-09-29 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ff18aa49-635c-3c8e-9ce5-947f85746c40 | -4.7157 | -41.9974 | 2025-09-29 00:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| b4859738-1205-3952-90e1-db2b361a3790 | -15.2897 | -49.4813 | 2025-09-29 00:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 5c97b2b6-0120-351c-a596-ad7e0024fd70 | -7.2402 | -44.7812 | 2025-09-29 00:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 29e8785a-2d9d-369f-8929-aaf03aa1ca43 | -20.0491 | -41.3251 | 2025-09-29 00:30:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 1954c935-9ffc-3b74-9e90-f33ad62f95b1 | -18.1778 | -53.3239 | 2025-09-29 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 71.9 |


[Clique aqui para ver as próximas entradas](README2.md)
