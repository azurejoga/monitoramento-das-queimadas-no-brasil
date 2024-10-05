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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a97ab67c-3a5d-32ce-8eca-b70f774694cd | -17.0316 | -56.6956 | 2024-10-05 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.7 |
| 6dd970f4-0eff-3a9f-bc3e-6fd3b3f723b0 | -17.0113 | -56.7392 | 2024-10-05 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 893341be-d8fc-31b9-a7e9-5f3b92184920 | -17.0123 | -56.6773 | 2024-10-05 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| ee87aff0-7c31-3024-8bbb-9be0e574f103 | -17.1085 | -56.7892 | 2024-10-05 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 860b7ed7-52af-36a4-9425-031f7f212a02 | -17.0319 | -56.6749 | 2024-10-05 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 3f031e08-1f23-359e-8a77-72e795f08b0c | -17.012 | -56.698 | 2024-10-05 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| b136cbbf-90fd-3950-8b7a-893ef8f3635c | -17.1378 | -57.4016 | 2024-10-05 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |
| 548b30ec-de12-3c89-ab39-3b769ce764c2 | -17.1375 | -57.4221 | 2024-10-05 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.2 |
| a580e583-c6fd-3bf1-b32d-dd0bbfc71145 | -17.1182 | -57.4039 | 2024-10-05 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.7 |
| 9eae300e-2871-338f-b802-a54b4b22313c | -17.1178 | -57.4244 | 2024-10-05 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.3 |
| 6b978592-f237-3ce0-8a08-1ce1b4491e79 | -18.4849 | -52.8876 | 2024-10-05 06:46:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| faf24839-7e16-30c7-8353-a733190d5eba | -18.4853 | -52.8659 | 2024-10-05 06:46:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 166.9 |
| f080b1a3-d2b8-304a-a06d-c823dc9bd7b5 | -18.5053 | -52.8626 | 2024-10-05 06:46:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 13800eee-7b51-3195-810d-04f8e9fec41b | -18.6785 | -57.2734 | 2024-10-05 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.6 |
| dc8c37d9-578e-33d3-a017-c54a5df21782 | -18.6582 | -57.2967 | 2024-10-05 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 939bcc57-2e5a-38f5-9c8e-8cc2d862142c | -18.6782 | -57.2941 | 2024-10-05 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 3242bcb7-6eb2-3f85-a4c8-00000198e9cd | -18.6586 | -57.2759 | 2024-10-05 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.8 |
| cf5e650f-61f8-320d-8aa3-96389266f1e0 | -9.19788 | -61.57977 | 2024-10-05 06:48:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1a3ee1d1-ee3d-3324-b937-2550e7512bda | -13.41335 | -61.92384 | 2024-10-05 06:48:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 6f9d43bf-2637-38a7-b9eb-da4d2c312fba | -13.41044 | -61.94948 | 2024-10-05 06:48:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 763.3 |
| e6f519d6-fa39-3fed-bf0d-db60473eec0f | -13.40639 | -61.94414 | 2024-10-05 06:48:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 350.3 |
| 8c7b9e31-1f7d-3988-bc89-24fa35697052 | -11.2566 | -60.5825 | 2024-10-05 06:56:11 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5ea91867-bb55-3b86-8ab5-e9b66b19d59b | -11.2754 | -60.5814 | 2024-10-05 06:56:11 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d28908ef-1045-323f-be0a-8f419728c047 | -16.554 | -57.2237 | 2024-10-05 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.1 |
| ef436d3f-fc2b-3d22-91bd-91d22e6db45f | -17.012 | -56.698 | 2024-10-05 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 8b53e664-a3a8-3544-a77b-33f011d838db | -17.0316 | -56.6956 | 2024-10-05 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.9 |
| 73f89dcd-2830-3571-b32e-fad42ead1fd4 | -17.0319 | -56.6749 | 2024-10-05 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 02a01e79-7379-3cd1-bf0b-de5562e6f0a9 | -17.1178 | -57.4244 | 2024-10-05 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.9 |
| 343ef23d-d43b-3f5c-93a3-71f00949485e | -17.1182 | -57.4039 | 2024-10-05 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.0 |
| d450c168-5838-363e-a9d2-20dc6d3134da | -17.1375 | -57.4221 | 2024-10-05 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| f678480e-7ac6-30b5-8a47-2f75fa28bda6 | -17.1378 | -57.4016 | 2024-10-05 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |
| 7293d564-b8ab-3061-98be-926924460dee | -18.4853 | -52.8659 | 2024-10-05 06:56:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 245d3902-3bf9-3ed5-a1e1-5384f3ec2028 | -18.5053 | -52.8626 | 2024-10-05 06:56:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| f9b69cdc-e76e-3904-856d-bfac4bcc1f3b | -18.6586 | -57.2759 | 2024-10-05 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.4 |
| 8602e13f-8137-3b8f-bc1a-5b1b9d3548bb | -18.6785 | -57.2734 | 2024-10-05 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.5 |
| d55470ea-be38-3e6e-b482-c04a704a4751 | -16.7644 | -57.5061 | 2024-10-05 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 95993669-8003-36a8-8a8b-33f745c8f2bb | -16.7647 | -57.4856 | 2024-10-05 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 5ebb9f5c-694e-37ad-b086-81f9fed8688c | -16.765 | -57.4652 | 2024-10-05 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| f389045e-35f6-32ca-985f-7c5925c934ce | -16.7843 | -57.4834 | 2024-10-05 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 1295e3d3-069d-3f16-aa4b-530b728f0803 | -17.012 | -56.698 | 2024-10-05 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 642ed609-fe67-3889-b261-f275f1695db8 | -17.0123 | -56.6773 | 2024-10-05 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 8ddc8820-f3c8-3d4c-ab23-2a74500e733b | -17.0316 | -56.6956 | 2024-10-05 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.4 |
| 3c015ddf-e996-3276-a94a-d81db55e24cd | -17.0319 | -56.6749 | 2024-10-05 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 723b7573-e300-3b1d-ac17-77514bd4d99d | -17.1182 | -57.4039 | 2024-10-05 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.4 |
| e0dbaa21-8dcc-3e52-8452-49508588cba6 | -17.1178 | -57.4244 | 2024-10-05 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.6 |
| ee758a0c-8bb2-3b6b-a44b-c24f308a42c0 | -17.1375 | -57.4221 | 2024-10-05 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| ab1aa415-f9be-3276-9705-53b7ee3eee20 | -17.1378 | -57.4016 | 2024-10-05 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| a1f23153-3d03-3671-9b85-f3c92708891c | -18.4853 | -52.8659 | 2024-10-05 07:06:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 0627350c-278d-3eb0-81ab-b162103bd278 | -18.5053 | -52.8626 | 2024-10-05 07:06:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 73f0c3e0-aaa8-3a9c-bf8a-0e65757b4908 | -18.6387 | -57.2785 | 2024-10-05 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.2 |
| 870c74ce-b37e-3852-86c5-faeb1bab13cc | -18.6582 | -57.2967 | 2024-10-05 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 7954e33c-9d3e-3d3a-8150-57b334178a5f | -18.6586 | -57.2759 | 2024-10-05 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.3 |
| fcc649bb-fb35-3c10-8f17-7809d85eea70 | -18.6785 | -57.2734 | 2024-10-05 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.2 |
| b150e5ed-a281-3c75-bf68-cbc81f8b3a81 | -11.9149 | -56.9338 | 2024-10-05 07:16:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d7f26a0d-9ab3-37a5-8478-74fcdf64d874 | -16.554 | -57.2237 | 2024-10-05 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.0 |
| 02eba076-b232-31fd-8902-90dfceb38aa2 | -16.7647 | -57.4856 | 2024-10-05 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| eddb7c48-a2f5-3573-8c7b-bef69895d6d7 | -16.765 | -57.4652 | 2024-10-05 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| c6798f2d-e1b0-319c-8e97-570c0377e5ba | -16.7843 | -57.4834 | 2024-10-05 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| dde9e995-e0ba-3f22-a146-091470da8db7 | -17.012 | -56.698 | 2024-10-05 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| f3710982-c510-362e-a245-a80afb9355c8 | -17.0319 | -56.6749 | 2024-10-05 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 51053538-eb43-3da5-afc8-0e0e5af549db | -17.0316 | -56.6956 | 2024-10-05 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.3 |
| a73429f4-b3cd-3ae1-8cd9-34f1e1edff64 | -17.1178 | -57.4244 | 2024-10-05 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| 49a6953d-ee19-3825-933a-c4c5d84947df | -17.1182 | -57.4039 | 2024-10-05 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 36ed8a32-6d4a-36b0-9ade-7200cfb7332c | -17.1378 | -57.4016 | 2024-10-05 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 376840d6-1c7c-3baa-9e19-077705bfa316 | -17.1375 | -57.4221 | 2024-10-05 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 696c2a61-fe80-39ef-8040-55938187af5a | -18.6582 | -57.2967 | 2024-10-05 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 1c774fb8-184e-3069-95de-e059d8b95343 | -18.6586 | -57.2759 | 2024-10-05 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.2 |
| a261061b-7b88-3d70-84b6-e9a404f910c3 | -18.6785 | -57.2734 | 2024-10-05 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.2 |
| 41cd07d3-b7c9-3eca-8746-b8012eabb517 | -16.5345 | -57.2259 | 2024-10-05 07:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 4de6d51b-96f7-3b93-a5be-9204fd8de8c0 | -16.554 | -57.2237 | 2024-10-05 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 39bf12c7-8033-383b-864f-e12ebbd0819a | -16.7647 | -57.4856 | 2024-10-05 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 091ed6a5-c349-394d-905b-ceb666017fc1 | -16.7843 | -57.4834 | 2024-10-05 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 6e5b07dd-235a-3492-b474-f14980c0fc71 | -17.012 | -56.698 | 2024-10-05 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| cd4041cc-9c00-35c4-9d33-7ba979740c48 | -17.0316 | -56.6956 | 2024-10-05 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 3deb369f-40bc-370c-8049-ed6afd64bf4b | -17.0319 | -56.6749 | 2024-10-05 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| b85f8d6e-94dd-33a4-876a-49b508084010 | -17.1182 | -57.4039 | 2024-10-05 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.0 |
| dafffcab-648c-31ea-b1f0-224a3fc7b428 | -17.1375 | -57.4221 | 2024-10-05 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.1 |
| 51b9db45-965f-3fa8-9c0f-4901a82c40a6 | -17.1378 | -57.4016 | 2024-10-05 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.3 |
| def07047-4449-39f6-af95-0472b084dc86 | -17.1178 | -57.4244 | 2024-10-05 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 60b3279e-eab5-345a-97e6-ca8d596a979b | -18.4853 | -52.8659 | 2024-10-05 07:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| ee832e56-6117-3db9-aa09-cccb7f0ef4f6 | -18.6387 | -57.2785 | 2024-10-05 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 5eab9d50-0e33-368a-a7de-b5634af8f259 | -18.6582 | -57.2967 | 2024-10-05 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 99c9c2a5-ee72-3fb2-b7b5-07572e53559f | -18.6586 | -57.2759 | 2024-10-05 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 221.1 |
| e69db058-50b1-36d0-a3db-22c129c6edf8 | -18.6785 | -57.2734 | 2024-10-05 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.3 |
| ccde9d9b-6f4b-3aec-8f8c-a441627ab045 | -20.629 | -51.4722 | 2024-10-05 07:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.8 |
| 7169e17a-30b9-36cf-8e66-11daac203f11 | -12.6532 | -54.0415 | 2024-10-05 07:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c39bf2f2-88a8-3436-b667-0f472cea65eb | -12.6283 | -53.1108 | 2024-10-05 07:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 9e9ac449-61d5-3213-b36f-58132f4b3a6f | -12.628 | -53.1317 | 2024-10-05 07:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 9a47f73f-6083-3e18-976c-956323ee0571 | -12.6092 | -53.1129 | 2024-10-05 07:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 1b33e5b9-7f5a-32ea-b48f-b1551743c59e | -12.6089 | -53.1338 | 2024-10-05 07:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 1ab3d43e-6d61-377f-a306-9d304d34c0b8 | -16.5345 | -57.2259 | 2024-10-05 07:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 29eb89ed-7573-30dd-9e9a-2708110ceeca | -16.554 | -57.2237 | 2024-10-05 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| e02c5e1f-53dd-30a9-9610-240909ed71b1 | -16.7843 | -57.4834 | 2024-10-05 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 092680be-8f98-3478-9cde-d286539a5be0 | -16.7647 | -57.4856 | 2024-10-05 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 58ed6832-cbb0-3140-8ff6-57c9cfc6e3a7 | -17.0319 | -56.6749 | 2024-10-05 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 092b501c-e14c-36b8-bb2f-769cf3d42664 | -17.0316 | -56.6956 | 2024-10-05 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.1 |
| e6f20955-30aa-3550-a044-c6c74e5fa021 | -17.012 | -56.698 | 2024-10-05 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| f4d5e37c-ac93-3972-901b-177dcd3308b9 | -17.1378 | -57.4016 | 2024-10-05 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.0 |
| 0e101179-0a57-3095-9ef5-8f6a7bede5a1 | -17.1375 | -57.4221 | 2024-10-05 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.4 |
| e11010ef-4ab1-3bea-a576-515d274dc64f | -17.1182 | -57.4039 | 2024-10-05 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.7 |


[Clique aqui para ver as próximas entradas](README154.md)
