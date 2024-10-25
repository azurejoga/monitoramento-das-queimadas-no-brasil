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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd665b3c-7a10-3732-b2bf-d70bbc4294e0 | -4.51518 | -61.14359 | 2024-10-25 06:18:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4b7aea8-de0e-352c-b42f-3cb949bd21e3 | -9.437 | -67.14472 | 2024-10-25 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c46e2524-3a5d-3df6-b656-8b9ec413b0e4 | -10.3227 | -68.67853 | 2024-10-25 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27005605-38da-3210-8165-dd8123efa2e0 | -10.27235 | -68.70515 | 2024-10-25 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ecd859c-19fb-3aa7-a17d-f59f14a6ee2d | -8.46707 | -69.69489 | 2024-10-25 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 099ddcae-1792-358e-88a6-2ac1b88ee80b | -8.47124 | -69.69548 | 2024-10-25 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67970c16-89b5-3c0d-b7a0-e1f622494d26 | -8.20287 | -70.97554 | 2024-10-25 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4329e7f1-848d-3240-b99f-844eb71eb38a | -8.98409 | -70.63488 | 2024-10-25 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0788a972-b883-3331-a0af-6939d2fc3f0a | -17.764 | -57.5526 | 2024-10-25 07:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| eca84f6b-6c60-3438-b73e-084a13dd5ba1 | -17.7644 | -57.532 | 2024-10-25 07:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 7bdda293-4c97-3166-8a28-0a5e6747fac7 | -17.8628 | -57.5407 | 2024-10-25 07:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| ccc8125a-0ef6-3ba9-8fdd-465360b3b388 | -19.6071 | -56.6688 | 2024-10-25 07:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| 2e9c5daf-75de-3349-b6d5-835f832aa696 | -19.6268 | -56.6869 | 2024-10-25 07:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 6e971622-f108-3f53-9d67-aabe558a4019 | -19.6272 | -56.6659 | 2024-10-25 07:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| ea3aa1fa-16bd-3e06-942e-3bbc5fbb0d9d | -16.9792 | -57.5223 | 2024-10-25 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 66af40be-3d5c-36e0-b46d-f3676240ef1c | -16.9596 | -57.5245 | 2024-10-25 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 10a3a33c-ac7c-3b04-b869-b8666a818001 | -17.7644 | -57.532 | 2024-10-25 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 46667210-a8d3-33b4-a92c-e4d04e4821bc | -17.7446 | -57.5344 | 2024-10-25 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 142302bc-d045-3faa-82c5-91ad0217e749 | -17.8628 | -57.5407 | 2024-10-25 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 627c0002-c6fa-3304-ac10-4d99e46b9257 | -17.843 | -57.5431 | 2024-10-25 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| ad849829-0e64-3b60-8ac2-06767566d14b | -19.6276 | -56.6449 | 2024-10-25 07:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 49b417bd-bafe-3370-844a-5386d717112f | -19.6272 | -56.6659 | 2024-10-25 07:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 8af2d656-a11f-372c-98b2-2f607d9c41a1 | -16.9596 | -57.5245 | 2024-10-25 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 3defe360-6741-3ba7-9e9e-9ce2bd556a06 | -16.9792 | -57.5223 | 2024-10-25 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 58514b7d-05a4-37d7-9f79-9bb471f93238 | -17.2537 | -57.5108 | 2024-10-25 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 8fd0574f-2edd-3bf6-88a9-f1cc649c2c5d | -17.7446 | -57.5344 | 2024-10-25 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 3507e9db-76ee-3e37-8a49-02f66cd1deb8 | -17.7644 | -57.532 | 2024-10-25 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.2 |
| 12c5c395-d1f5-3761-9186-4b6b05390bce | -17.7647 | -57.5115 | 2024-10-25 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 68f1d1ce-0182-3fd5-97ec-a063e5b36ab9 | -17.8628 | -57.5407 | 2024-10-25 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 550a9f72-fdde-3cf1-8f98-8c5041bfa2da | -19.6071 | -56.6688 | 2024-10-25 07:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 4f9f9813-21b7-32ce-99e5-8ef0f3366648 | -19.6268 | -56.6869 | 2024-10-25 07:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| b77f09d3-4273-3b58-88d8-7e8e6c9543e5 | -19.6272 | -56.6659 | 2024-10-25 07:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 3815f0d0-b360-3dce-92d7-2559a4f9bd7f | -19.6276 | -56.6449 | 2024-10-25 07:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 6ae8a839-49f2-3ec3-9824-36d70fa94cff | -16.9792 | -57.5223 | 2024-10-25 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| ff05d888-0485-3643-993b-1b6326b5a77d | -16.9596 | -57.5245 | 2024-10-25 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 71cca6bb-6a08-38a3-8f6b-9b34f0635587 | -17.7644 | -57.532 | 2024-10-25 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.2 |
| aa83ab20-ee11-3367-b5d4-cddad6fc4a25 | -17.7446 | -57.5344 | 2024-10-25 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.7 |
| 9ef28d09-8be9-36fc-9ce0-afc79118fa29 | -17.7443 | -57.555 | 2024-10-25 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| fca1aa3c-fecf-3db8-ae1c-50baad41084c | -17.7647 | -57.5115 | 2024-10-25 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 0983cd08-05c0-32fa-8b00-e47fbceea08c | -17.8825 | -57.5383 | 2024-10-25 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| c15c0b0c-d613-3acf-be9b-690865520461 | -17.8631 | -57.5201 | 2024-10-25 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| b622874c-f5db-3a55-abec-6528a6b4f6d7 | -17.8628 | -57.5407 | 2024-10-25 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.0 |
| 1f531b88-314a-3b9c-950d-459f4548b3c9 | -17.843 | -57.5431 | 2024-10-25 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| d8ee9e49-8ff7-3d37-83c7-68fdd5acd106 | -17.0381 | -57.5155 | 2024-10-25 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| de529719-9454-3353-981c-c561b617b9e2 | -16.9792 | -57.5223 | 2024-10-25 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 61734294-db71-355f-a265-cd81af206c10 | -16.9596 | -57.5245 | 2024-10-25 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 3dea4ce6-3ad9-3bec-bbc3-1846a8a96220 | -17.2537 | -57.5108 | 2024-10-25 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 5b25e192-3007-3da8-9ec3-fd8620355d01 | -17.7647 | -57.5115 | 2024-10-25 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| f42a0f82-a26c-3e63-9269-99c13400fe72 | -17.7644 | -57.532 | 2024-10-25 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 10127c6b-c4c3-3fbf-ba0a-0d0b56dc3746 | -17.7446 | -57.5344 | 2024-10-25 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| e82aaba9-484d-31ed-8139-6afa4102344a | -17.8628 | -57.5407 | 2024-10-25 07:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 0e830045-a6ad-3ee4-a849-57172a34f823 | -16.9596 | -57.5245 | 2024-10-25 07:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 6ecba8bf-f883-3908-b1b4-4449e46fd88a | -16.9792 | -57.5223 | 2024-10-25 07:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 27843d53-f574-3190-b8f5-a4bf8ad1b859 | -17.7446 | -57.5344 | 2024-10-25 07:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| df1cd093-74ba-3c7b-871a-a96a962dc29a | -17.7644 | -57.532 | 2024-10-25 07:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.4 |
| 14e9ddce-9253-3544-833d-f945eeac6e00 | -17.7647 | -57.5115 | 2024-10-25 07:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 1ed0f029-7363-3bc4-bc32-77775a7787d7 | -17.8038 | -57.5273 | 2024-10-25 07:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 51bb5ba5-9b04-3b61-a562-4ed5e1d9e7be | -17.8628 | -57.5407 | 2024-10-25 07:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 2f7569db-82b9-3605-af59-df3ee3ffa8b1 | -16.9596 | -57.5245 | 2024-10-25 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| e0925728-c7be-3736-aee8-aac848535ccc | -16.9792 | -57.5223 | 2024-10-25 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 7d52e5cd-d0a8-3831-bd2b-268266cafc96 | -17.7644 | -57.532 | 2024-10-25 08:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 0109ba21-10f5-3b2c-a663-1f5f20b0a3b0 | -17.7446 | -57.5344 | 2024-10-25 08:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 9d0177b5-88d2-3f29-a51a-396f43fe91a3 | -16.9596 | -57.5245 | 2024-10-25 08:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 68b8108b-b721-347f-9810-c3336835bf4e | -17.2386 | -57.2256 | 2024-10-25 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 2b9a64f2-d1ce-31b7-afb8-8e4d9aff59b1 | -16.9596 | -57.5245 | 2024-10-25 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 93c4ef68-3699-35a8-97bc-53e21e5f20e8 | -16.9792 | -57.5223 | 2024-10-25 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| e4f8223d-acd0-35b9-87de-a30550e70245 | -17.2386 | -57.2256 | 2024-10-25 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 08b3b629-d18c-3208-b50f-eb7ff11dd20f | -17.7644 | -57.532 | 2024-10-25 08:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 7ff6bf2e-6ff5-35c1-94dc-56eb046d91d9 | -17.7647 | -57.5115 | 2024-10-25 08:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 1bf5813e-9b03-366a-84ed-c38a75333d98 | -16.9792 | -57.5223 | 2024-10-25 08:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 3c1a6049-b74f-3d6f-88fc-976ebf867c8c | -16.9596 | -57.5245 | 2024-10-25 08:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 7101fb6d-797c-34aa-95ac-0be491f5708c | -17.7446 | -57.5344 | 2024-10-25 08:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 62c8377d-df4b-3064-b352-3be2ca20ec61 | -17.7647 | -57.5115 | 2024-10-25 08:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| eca45077-c581-3af2-9243-83771ac5a195 | -17.7644 | -57.532 | 2024-10-25 08:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| 6920c96d-4cf3-3b3f-a622-6bd60bfcbbaa | -18.0452 | -57.2506 | 2024-10-25 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.9 |
| add9e4cf-ba45-3456-a1d1-b23ff7b1fe3e | -18.0455 | -57.2299 | 2024-10-25 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 189803a2-e538-374b-b76f-6f55c2f2c5ac | -19.6071 | -56.6688 | 2024-10-25 08:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| af3043cf-7cb6-36f2-9d76-09b403f7a8b7 | -19.6272 | -56.6659 | 2024-10-25 09:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 127.2 |
| b2843903-7c41-3aa1-8d3e-359d0baf31ee | -19.6272 | -56.6659 | 2024-10-25 09:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 00266a5e-307b-3d47-8fd6-6271d42e3c0a | -19.6469 | -56.6841 | 2024-10-25 09:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 3f87d6ac-741c-3907-b80c-6607488f0560 | -19.6272 | -56.6659 | 2024-10-25 09:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.9 |
| fbbadcf3-77f7-3fea-b5b3-3bb12ad9ef5f | -19.6272 | -56.6659 | 2024-10-25 09:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 5dd0d2ec-eebf-32c8-89cd-4547d51e888e | -19.6272 | -56.6659 | 2024-10-25 10:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| bdc542c0-5f6f-3c6f-ba45-e682f819700f | -19.6272 | -56.6659 | 2024-10-25 10:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 72fc690a-82b7-36a2-b395-12f1aa92776b | -19.6272 | -56.6659 | 2024-10-25 10:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 076c271a-7e95-3b9a-af89-93bebc46f187 | -16.3424 | -42.2045 | 2024-10-25 11:06:36 | GOES-16 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.0 |
| d91f54e2-36b3-3fd3-9195-9f324d9fb634 | -19.6272 | -56.6659 | 2024-10-25 11:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| e612c2d7-2169-370e-ac21-5ff850ff83a8 | -17.2386 | -57.2256 | 2024-10-25 11:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 93f80a06-1c90-31bf-8cd2-56ede5aa7810 | -18.0452 | -57.2506 | 2024-10-25 11:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 4014e2e9-e2b5-3325-909b-6ebfb868566f | -19.6272 | -56.6659 | 2024-10-25 11:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| b70fb864-156e-33ec-bef1-54ca6295bc60 | -17.2386 | -57.2256 | 2024-10-25 11:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| c9362a99-7209-3c94-97f1-b9ab4151bc44 | -17.7446 | -57.5344 | 2024-10-25 11:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| e86238a5-f79b-34f9-a22f-d6dbb9f8ee21 | -17.7644 | -57.532 | 2024-10-25 11:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 47706ddd-f7ec-3729-a173-2000574129c6 | -18.0431 | -57.3745 | 2024-10-25 11:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.7 |
| ae514478-44cc-39e8-9de8-307c671884b8 | -19.6272 | -56.6659 | 2024-10-25 11:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| d7f3b3a5-059d-3ee0-9886-9222e605b7c8 | -17.2386 | -57.2256 | 2024-10-25 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| cf148472-b937-36d4-b554-57dce6de6422 | -17.219 | -57.228 | 2024-10-25 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.0 |
| 385186bb-84f7-35e5-a950-846461288f2f | -17.2186 | -57.2485 | 2024-10-25 11:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| b84d945b-46e6-364b-be7b-9b010f1c9c83 | -18.0431 | -57.3745 | 2024-10-25 11:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 02ddc58d-67d8-3397-b458-bab3b1318ff3 | -19.6272 | -56.6659 | 2024-10-25 11:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.2 |


[Clique aqui para ver as próximas entradas](README112.md)
