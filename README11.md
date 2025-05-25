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
| 895597aa-1af6-3b6d-a8e4-9e259a40b480 | -19.10165 | -54.44788 | 2025-05-25 05:10:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c3b25f3-84a4-376a-9f4b-ae5987519f80 | -19.61703 | -54.42791 | 2025-05-25 05:10:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e2676f7-43c4-38da-9874-8b98873deba4 | -20.47703 | -53.6754 | 2025-05-25 05:10:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cd74162-eec2-305e-83c4-ddb59e56a40c | -20.94457 | -56.58879 | 2025-05-25 05:10:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ee9222-2291-31e9-8936-dbd2a9a27fca | -19.37553 | -53.21026 | 2025-05-25 05:10:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 689e7345-1e18-31f7-ad01-ebafca72d253 | -23.97938 | -48.91854 | 2025-05-25 05:10:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a00366e6-2cf5-364b-a921-ab7bbbd4d336 | -19.87911 | -54.37001 | 2025-05-25 05:10:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7a38dd6-4855-3bb5-80eb-6edca4fddc73 | -19.36669 | -53.21312 | 2025-05-25 05:10:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57f374f0-485b-3a3d-aca4-91e2de1114ab | -20.70956 | -50.06688 | 2025-05-25 05:10:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0a253260-d261-3c9d-97a6-ad8a430ec7cf | -23.2428 | -52.34903 | 2025-05-25 05:10:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 7fe63744-2eb8-3f8c-9bee-493c7572940d | -20.51517 | -51.4229 | 2025-05-25 05:10:00 | NPP-375D | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0bbe23b1-6051-30b9-9e22-6be7d7ef3bb5 | -19.37136 | -53.20975 | 2025-05-25 05:10:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 201fc95b-125d-38c5-aa9f-6f43c47fc53f | -23.24337 | -52.34401 | 2025-05-25 05:10:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 20e90d8e-6cd7-3845-8dba-1e2248bd1ede | -7.6574 | -46.1013 | 2025-05-25 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| fab3b575-b924-333b-8c15-fb0879e98c1d | -8.06521 | -43.1272 | 2025-05-25 05:23:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a73a1fe7-ebc1-349a-8a8a-cc3089304c78 | -7.20552 | -43.12378 | 2025-05-25 05:23:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 9196210e-fd72-39a7-9842-5bd2be20222f | -6.55335 | -44.49041 | 2025-05-25 05:23:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7769c134-f93a-3bdc-8288-d64b0ad8b141 | -7.20697 | -43.11435 | 2025-05-25 05:23:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 26cd0947-d027-3875-b0d3-15d1c21d9dd5 | -4.42987 | -37.80468 | 2025-05-25 05:23:00 | AQUA_M-M | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 497c3cac-c7d9-33a2-8f3d-358a84c20b7d | -8.05475 | -43.13516 | 2025-05-25 05:23:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| b4d9dca8-3ef6-3509-be63-962bb5783d6e | -7.66321 | -46.10669 | 2025-05-25 05:23:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 594377eb-0e80-3bea-8558-17e6c384efc8 | -4.43147 | -37.79346 | 2025-05-25 05:23:00 | AQUA_M-M | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 6a7c0723-699c-39b0-bd7f-979f5a19a557 | -7.66544 | -46.09272 | 2025-05-25 05:23:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cb87fa3a-642f-32f7-b1ea-80a913b94acc | -7.22515 | -43.11708 | 2025-05-25 05:23:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 88f289df-6a00-3ec5-a9d7-a68c17560076 | -4.42993 | -37.79786 | 2025-05-25 05:23:00 | AQUA_M-M | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 54746c03-2be8-3de8-8e79-d1dcdc408bc9 | -7.65453 | -46.09097 | 2025-05-25 05:23:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| ac8e07cc-d54b-33e2-8034-514ec5ccabef | -7.65229 | -46.10495 | 2025-05-25 05:23:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ea82af01-3f53-3196-b925-b48290fd8176 | -8.05332 | -43.14453 | 2025-05-25 05:23:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 7e6cca9f-5386-3242-bd9f-8c686c2fe1d4 | -8.90011 | -44.78024 | 2025-05-25 05:25:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 01cd766a-e976-32a8-8440-b61768303847 | -12.27551 | -44.59583 | 2025-05-25 05:25:00 | AQUA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a1d5f22c-3e85-3917-8440-4dc8a8897ed9 | -4.29069 | -48.27129 | 2025-05-25 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b77ce924-767f-39a3-b83a-d5ce43a22447 | -4.28981 | -48.27756 | 2025-05-25 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b018fd2a-e796-35f9-b22b-5c9996357b7c | -9.67405 | -65.53751 | 2025-05-25 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 220ca652-4587-3545-b9ae-3d6170121ad3 | -11.4257 | -54.32933 | 2025-05-25 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9485a6d0-a6c5-3f03-a988-92d85a6fa034 | -9.80291 | -64.75871 | 2025-05-25 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16f92371-c376-3fc7-b6de-6df181a2b93e | -9.7995 | -64.75814 | 2025-05-25 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 947a90af-2668-333a-928e-f556fbf86c9d | -9.42037 | -58.30515 | 2025-05-25 05:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13e027d5-438d-30a5-89d6-a5418c79f363 | -5.12204 | -56.11817 | 2025-05-25 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ed11654-f10b-3fe8-99f5-db3cee79f27e | -11.4253 | -54.3325 | 2025-05-25 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d391b5d-1731-3d50-a2c7-df05d55893d2 | -5.12262 | -56.11427 | 2025-05-25 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaeb1fa3-b8d1-3414-8d36-0d238abb6b23 | -5.32479 | -55.9446 | 2025-05-25 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 974722e6-529d-35e9-b79c-07f0108e95bf | -9.65678 | -65.75033 | 2025-05-25 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 94369a1b-6c72-32b2-8366-0d5c0b2b0a3d | -15.62913 | -57.3054 | 2025-05-25 05:29:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dbe2d24-e261-323a-9239-623cfe998274 | -13.15044 | -56.80845 | 2025-05-25 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb4371f3-eefb-340f-8f2d-ebb867189a41 | -14.04147 | -55.13902 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9d6aa8e-b058-31b6-a98c-a06ff296503a | -14.03195 | -55.13156 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b7b798e-e15f-3f6c-9834-1124b72c133d | -14.68254 | -52.68561 | 2025-05-25 05:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14798543-a6fb-3a38-87dd-0cc2a3ea7e12 | -14.01655 | -55.12951 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0c31cfc-7f75-3013-ac1f-ccd3f55e5f28 | -11.74716 | -54.23235 | 2025-05-25 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1652ac6d-f58f-35ec-bb67-988249bc2f5d | -14.20407 | -60.04949 | 2025-05-25 05:29:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 156644a6-a535-39ba-a734-bc1fb450e42f | -11.74133 | -62.72641 | 2025-05-25 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26329ffb-ab26-367a-a462-4525845a0ca2 | -13.15497 | -56.80906 | 2025-05-25 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ee4c008-6d48-33f4-ae2b-cb7417465748 | -11.75817 | -54.23026 | 2025-05-25 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4616571-c7fe-3edf-8cfa-514496ae8b36 | -13.0882 | -54.86476 | 2025-05-25 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f143639a-b1f9-3e56-991d-ee83506df337 | -11.74793 | -54.23158 | 2025-05-25 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2459393e-3382-3861-a979-cecc7d3be5de | -11.75246 | -54.23295 | 2025-05-25 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8bf4b12-9259-3c9d-b6b9-b0b47b66a1f8 | -11.73801 | -62.72588 | 2025-05-25 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb737694-1aa8-3a5a-b61e-ab2e67a57a74 | -11.75857 | -54.22698 | 2025-05-25 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4144babb-4bbf-3aee-8150-51000faac4b1 | -11.75286 | -54.2297 | 2025-05-25 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2155b2a1-6fac-3e2a-a2a8-39828e809def | -12.49892 | -55.18766 | 2025-05-25 05:29:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 788263e0-e8ec-3382-99f0-a9f468a7ff2e | -14.20781 | -60.05004 | 2025-05-25 05:29:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 069da11a-0d09-3173-bb79-1d63f54c2ec1 | -14.01693 | -55.1263 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 272eac12-673d-3bd6-93fa-6326422c49f2 | -13.15104 | -56.80375 | 2025-05-25 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2861ec5-b6e5-3ea1-8ea0-f4077c015de9 | -14.03632 | -55.13853 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 303461fe-a27d-3c3b-a582-83959fd97017 | -15.62761 | -57.30711 | 2025-05-25 05:29:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f7be04e-dc28-39b1-aa67-bb55fc421939 | -13.15436 | -56.81376 | 2025-05-25 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a79d7d1-a9fb-3856-bca6-8ac64656baf6 | -13.08781 | -54.86795 | 2025-05-25 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e4fa6e8-9487-3630-b0e4-f93babfebda8 | -11.74751 | -54.23484 | 2025-05-25 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 43998ea2-1c10-3394-8927-34b2aa7e8182 | -14.67746 | -52.68808 | 2025-05-25 05:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdcb833c-f4ff-3318-ac0d-eb2f5b6850cd | -14.68308 | -52.68082 | 2025-05-25 05:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a97fb3b5-cc7b-3155-93b8-5011d7d739fe | -14.68403 | -52.68408 | 2025-05-25 05:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee4cddf9-c71e-31ba-a2a9-c744ad61a1c7 | -13.14197 | -56.80259 | 2025-05-25 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49704066-6d1a-3fd8-8c69-124452abd309 | -14.67647 | -52.68486 | 2025-05-25 05:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfea3df9-0d90-3b93-8f76-577090c28051 | -14.06308 | -57.11439 | 2025-05-25 05:29:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3602aa63-be09-33f3-9ec1-5f2616a28268 | -13.98589 | -56.02141 | 2025-05-25 05:29:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cebd76cf-5d4d-3407-ad15-c7e738eca156 | -14.47294 | -56.32057 | 2025-05-25 05:29:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73349311-6d0a-3b16-b289-3764e044a2fc | -12.37301 | -54.89859 | 2025-05-25 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d85c9f5d-195c-3b39-b74a-53d0cc82cf74 | -13.00312 | -55.97443 | 2025-05-25 05:29:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9560c37b-93a0-3703-bb13-7c5eeaa7914b | -13.14651 | -56.80315 | 2025-05-25 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a060b51-0428-37ae-aa0c-a9895bbf240d | -11.99119 | -57.20823 | 2025-05-25 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9dd5ceff-922f-35d4-a1f9-4f569eba3fc0 | -12.50393 | -55.18833 | 2025-05-25 05:29:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fe71536-0b8d-33a8-8b89-650b0e102ff2 | -14.67796 | -52.68332 | 2025-05-25 05:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bb110de-a39b-36a3-8e12-6161290883c3 | -14.02566 | -55.14037 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a934c4e5-39c2-3e35-8cd9-de72c41386a9 | -11.99246 | -57.21165 | 2025-05-25 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b73aa018-063a-37b2-a902-5ed42833dd45 | -14.03709 | -55.13219 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ca801a8-7a79-327a-bc61-60044fa8b6da | -12.37262 | -54.90161 | 2025-05-25 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1c0682d-46d6-3b67-8237-c7cd42f31132 | -14.02605 | -55.13721 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60cc45b8-e97d-38aa-9a43-388a201eccbb | -15.62858 | -57.30985 | 2025-05-25 05:29:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df5cce01-73b5-34c4-8fd7-8e3f2a99ea09 | -11.99301 | -57.20748 | 2025-05-25 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd9799fa-ddc8-3750-9b48-018a466dd143 | -14.0308 | -55.14104 | 2025-05-25 05:29:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 681e3453-0f60-3873-8aed-db64b29927fb | -11.99679 | -57.21232 | 2025-05-25 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aad89e51-3a08-3580-b6f0-2ed3552cfd78 | -11.99493 | -57.21306 | 2025-05-25 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cebeb36-8df1-3c75-91de-ff7543b87643 | -7.6574 | -46.1013 | 2025-05-25 05:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 07b7ba71-15db-37a1-9411-da47bd32c98a | -20.94208 | -56.59158 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 47c96799-aa32-3b96-8555-14320eae512a | -19.87344 | -54.36812 | 2025-05-25 05:31:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dc66b5e-a350-3070-bae1-75afe2b310a4 | -20.94177 | -56.59468 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| eb358762-3c4c-38ff-9690-ec18142e04d1 | -20.93863 | -56.59716 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5c1d2dba-c1a2-3135-a69a-78a8d5e5977a | -20.95357 | -56.60231 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7521395b-4309-323f-8bb6-1aacda68dd8d | -20.94371 | -56.59787 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cfa4c061-3e5b-343e-a200-009986dfd11f | -19.36914 | -53.21199 | 2025-05-25 05:31:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
