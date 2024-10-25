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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86d5ff1e-d89a-3a09-885c-d2d43fdde344 | -18.30042 | -56.23308 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.5 |
| 12109af6-eb72-3e4d-9c19-44d0a1da487e | -18.29851 | -56.22605 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| ccb8b031-7d06-368f-82b3-34de89a12ac8 | -18.26456 | -56.03181 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 3414dc4b-7e2e-3a61-968d-846f2e3784ea | -18.25389 | -56.02988 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.7 |
| 454d121e-e835-321f-b0e5-8575c8eb4eab | -20.23188 | -56.89637 | 2024-10-25 12:55:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b381f681-5e0a-3e88-b601-c035e9e1f1c7 | -19.6552 | -56.68346 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 8092e2e0-fb3d-3205-9203-baf911677fd9 | -19.64429 | -56.68141 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 2c4984e4-7a3e-3255-87bc-cd6bcb827af3 | -19.64178 | -56.69602 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.2 |
| c90d55bd-e8f6-39d9-a80a-0fff93b9adff | -19.63926 | -56.71067 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 94424ad5-3fa4-3545-a01e-75af7a6a915d | -19.63339 | -56.67936 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 37.5 |
| 1e9287ed-ac37-3b50-a058-f8956b22ab26 | -19.62754 | -56.64819 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 25f6970d-75e7-3457-8139-965e7887c3bb | -19.62727 | -56.84623 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| e118c4ca-972c-34d9-8551-a0ba612348fa | -19.62502 | -56.66273 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 0d4c1aef-c4d9-349b-ae81-dc7ea67e6b1c | -19.62344 | -56.65645 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 375af201-d914-3f14-a277-b1cc0c9717eb | -19.62249 | -56.67731 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 4c1eb815-3c8d-34a6-927c-ffe81d39bb5d | -19.62101 | -56.67105 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 49f14d7e-e0a9-3bc3-a2f0-d1da11f06ca9 | -19.61995 | -56.69191 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 6dccfc4a-0f2e-3b75-ba19-9fb14056b6a2 | -19.61857 | -56.68568 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| b3cb87f8-2c75-3a80-9d6a-04d68dd786fa | -19.61412 | -56.66069 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 0cba72c0-a9a0-3ab8-bc3f-4aff9b7a47c7 | -19.61255 | -56.6544 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 153426bd-a408-3819-bb38-a91df8dcbb5f | -19.61158 | -56.67527 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| ea0bb908-adba-3f56-a9ab-f1921cb5edc3 | -19.61011 | -56.66899 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 42d18862-d1cb-362e-aab3-d39a443a0bd8 | -19.60903 | -56.68987 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.6 |
| 501b366a-c22e-3542-84b5-490fd961cfee | -19.60765 | -56.68362 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 5e81105a-5b91-3c1f-be80-3f72bde9fe8c | -19.58867 | -56.53078 | 2024-10-25 12:55:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 8623da20-240d-38c6-8085-aa46f2b293b8 | -19.53709 | -56.70061 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.9 |
| ec3227e4-246d-3943-927e-3faf8c4f5f8e | -18.06815 | -57.23877 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 1682c854-1c0d-3e66-81f1-214c2f749350 | -18.04703 | -57.24626 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| b6475efb-a5b0-3a06-a54d-4379dfcebff5 | -18.04409 | -57.37583 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 23b5e0d6-a127-395a-925c-6ec049be2757 | -18.04172 | -57.25131 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| ae76c5e4-12a2-3aaf-bf5d-d2be861d72f6 | -18.03241 | -57.26106 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.5 |
| 6bc50106-aef5-3449-89a2-26fb1b5642e7 | -18.02665 | -57.36648 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 39fc0c76-420b-3dc9-ad4e-5e3ff9fc4e1c | -17.92361 | -57.21609 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.3 |
| de88d2c6-4a78-37d4-9a80-b65c31b11e9f | -17.9223 | -57.54194 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.0 |
| c4f29365-8679-3878-b95f-12203df36e51 | -17.92069 | -57.23308 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 3be29489-e8de-386d-a8e3-0845668fd3b6 | -17.91775 | -57.25013 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.1 |
| a1346e6c-2241-38cf-811d-f28f2006ebd7 | -17.90894 | -57.23086 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| e385a854-5fcc-3e61-82fa-636dd665d14d | -17.90284 | -57.55188 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.0 |
| ad60fa42-abd4-3dda-aab0-0172c138b000 | -17.89786 | -57.53964 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.2 |
| 8c323326-bad3-337f-934f-677c16626481 | -17.89454 | -57.55821 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 3b6ad024-bb24-3454-91df-e7c0c051f22b | -17.88169 | -57.53038 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.5 |
| dcdb1ee1-ee81-315b-8753-856b452a7e9d | -17.86952 | -57.52903 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 5ef855b2-e29b-364a-85df-f220e2de4ddf | -17.82051 | -57.59536 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 04992366-2783-3587-a25f-89aef35e1179 | -17.8173 | -57.61346 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.8 |
| 6b69ec37-a6d0-3605-8671-a2c4280ae540 | -17.7505 | -57.53889 | 2024-10-25 12:55:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 8596863f-e293-36bf-bc52-71971a57a56b | -17.69336 | -57.3379 | 2024-10-25 12:55:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 0bb2192e-de21-3032-a208-5675a1c1b5e4 | -18.15322 | -57.34973 | 2024-10-25 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 8e0c9f2f-9d3e-3a74-aa61-90438942bdfb | -11.8728 | -47.7239 | 2024-10-25 12:56:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 374d6c12-13b6-34e4-abdd-d8c6ed7c1257 | -12.5272 | -43.3782 | 2024-10-25 12:56:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| abc09e5f-d566-3f58-97ea-3b6135d653e2 | -12.5276 | -43.3543 | 2024-10-25 12:56:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2557d649-bfb2-308a-9605-0bb49c88420f | -16.554 | -57.2237 | 2024-10-25 12:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 600f1375-fc7d-3f61-93e4-4b977b993b76 | -16.9792 | -57.5223 | 2024-10-25 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 1be29440-9126-3d1f-b2e1-ac8b18e4a9b1 | -16.9596 | -57.5245 | 2024-10-25 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| c59750aa-9995-373c-8b61-3cd987c81574 | -16.9211 | -57.4881 | 2024-10-25 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 4ec37274-0033-325d-b4d6-02ed7929c880 | -17.0786 | -57.429 | 2024-10-25 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| e3820edc-1ea7-3fe9-95d6-f9f38cff481a | -17.0789 | -57.4085 | 2024-10-25 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.4 |
| a452dc73-b240-344b-98a5-8be284340676 | -17.2383 | -57.2462 | 2024-10-25 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.9 |
| 7d1ae0bd-85bb-3d08-a94c-7edeb7d86734 | -17.2186 | -57.2485 | 2024-10-25 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 193.7 |
| 128a908e-9bd3-314a-a1da-2acc906ff1de | -17.2373 | -57.3079 | 2024-10-25 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 6d2f60a3-66dc-3bcb-9a94-8b7a57d52e32 | -17.2386 | -57.2256 | 2024-10-25 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 727.0 |
| e615896b-2270-34b0-9077-067964694657 | -17.2769 | -57.2826 | 2024-10-25 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.8 |
| a18bae2a-86ac-354d-8e41-708a27c5d50b | -17.2573 | -57.285 | 2024-10-25 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 1b7e9e1f-caea-376c-bc2a-5071e6049981 | -17.257 | -57.3055 | 2024-10-25 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 5b2beab7-16ae-3c8f-ba75-06faa3253856 | -17.2966 | -57.2803 | 2024-10-25 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| e0047797-0be5-3adc-96cb-1ccdeac55e07 | -17.2766 | -57.3032 | 2024-10-25 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 60b19c0a-6ac4-30ae-838a-7420ca6518c8 | -17.2583 | -57.2233 | 2024-10-25 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| a0f1f6b0-b429-3e94-acdc-fd26b151bf14 | -17.7062 | -57.4774 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 9c718771-f8e8-3969-88d6-325b0e3f4689 | -17.6671 | -57.4616 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| dfe9668f-5fdf-33cf-88dd-ecd5d65a31af | -17.6888 | -57.3357 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 83a0cb95-4c1e-3567-ba51-816a39ced755 | -17.6865 | -57.4798 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| f50a3f72-5e14-396f-aa60-f8667f2a3b9b | -17.7634 | -57.5937 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 616ce0f5-0dbe-3297-801f-428ee5cb45c4 | -17.7671 | -57.3673 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 9fd58bcd-901e-3fb0-871e-8da7f418d9a1 | -17.6868 | -57.4593 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| f7d7ae21-4393-314d-a307-9c8da763bd98 | -17.6878 | -57.3975 | 2024-10-25 12:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| cc20fa80-e890-3b4d-bc4b-53b3d91db02c | -17.9071 | -57.2472 | 2024-10-25 12:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.2 |
| fad1760f-b97b-3506-9c79-37184790e667 | -17.9272 | -57.224 | 2024-10-25 12:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.3 |
| c809d8da-1a4f-3811-a69f-5d8e93b86f8a | -17.8628 | -57.5407 | 2024-10-25 12:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 1d644354-c1e9-30a2-8924-d017ba9a29c4 | -17.8825 | -57.5383 | 2024-10-25 12:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| ea3edb08-6405-3f05-827d-4e2ab4ef45bb | -17.9265 | -57.2654 | 2024-10-25 12:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 8bd618b9-cef0-3dde-ae98-391595a95b95 | -17.8222 | -57.6072 | 2024-10-25 12:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| aab4a4d5-ef3b-3e41-b878-302605afa4c6 | -17.9268 | -57.2447 | 2024-10-25 12:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.0 |
| 22f611e1-82f7-3abb-a70f-e1a9a270fc00 | -18.0448 | -57.2712 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 6ce5b421-7e8c-39d1-9532-abb1b5fa20c6 | -18.0455 | -57.2299 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 330ac1a1-a243-345a-8f81-5c84d380fe89 | -18.0243 | -57.315 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 8010e4ad-1305-3da7-8d09-f85166f86d6c | -18.0441 | -57.3126 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 8b2123d5-f37f-3946-8c93-30e54646a92a | -18.0431 | -57.3745 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 7aa33153-18c1-38f1-9f82-c50b79103491 | -18.0452 | -57.2506 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.2 |
| f67bb518-6353-31b0-ae33-6ba5d6433f03 | -18.065 | -57.2481 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.0 |
| d89e8f4c-044f-316e-b705-fa73896f62c7 | -18.0434 | -57.3539 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| 446b722e-db3e-3bad-a17d-5e7411279659 | -18.0438 | -57.3332 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| f0123f25-0deb-3d9d-9926-74bcefcb9528 | -18.0254 | -57.253 | 2024-10-25 12:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.0 |
| d3846ec8-ebcc-34af-8f92-346c0c864114 | -18.2641 | -56.0394 | 2024-10-25 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| bcf1668b-262d-3b9c-b2e2-a91bc6cceff7 | -18.3004 | -56.2222 | 2024-10-25 12:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| f6c59138-dd2c-3bc2-9f81-383abbf373f8 | -19.641 | -56.9988 | 2024-10-25 12:56:55 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| ecfed0fc-e541-3c8f-8648-232c066ce1b3 | -26.48146 | -48.74126 | 2024-10-25 12:57:00 | TERRA_M-T | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 701fb40a-e84b-3e45-a8bc-70e982d98a88 | -27.31466 | -50.51081 | 2024-10-25 12:57:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0aca02c1-6418-39ea-8ca0-c2167f107374 | -28.23205 | -51.51156 | 2024-10-25 12:57:00 | TERRA_M-T | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 01871c0e-729d-3f47-bec8-0b413ad64b6b | -27.62774 | -52.37114 | 2024-10-25 12:57:00 | TERRA_M-T | BARÃO DE COTEGIPE | RIO GRANDE DO SUL | Brasil | 4301701 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b39ce7e9-f847-3be6-b30b-4428a6327d75 | -26.99786 | -52.61059 | 2024-10-25 12:57:00 | TERRA_M-T | CORDILHEIRA ALTA | SANTA CATARINA | Brasil | 4204350 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2d189d53-b52f-3e7f-9729-458cde817fa8 | -23.84706 | -55.32217 | 2024-10-25 12:57:00 | TERRA_M-T | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |


[Clique aqui para ver as próximas entradas](README118.md)
