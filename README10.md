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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a1878e0-d634-3dc3-a96f-70261c183861 | -12.4591 | -63.1704 | 2024-10-25 00:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 1f7b15e4-86c7-34af-b798-52207082900e | -12.478 | -63.1693 | 2024-10-25 00:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| bb2ce6b4-1595-3a04-bbde-1d07ae524e21 | -12.5167 | -63.0521 | 2024-10-25 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ab0da7c9-c7da-335c-a835-c565ff6bed91 | -12.5356 | -63.051 | 2024-10-25 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 79865e7b-20a3-3d77-bdc1-2767698c52cc | -13.4769 | -61.6217 | 2024-10-25 00:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 92883561-e601-3218-b114-7764e177a157 | -13.4957 | -61.6398 | 2024-10-25 00:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c646d2bf-2274-31ae-85ce-466182e7dc75 | -13.4959 | -61.6203 | 2024-10-25 00:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9e9c36e0-3cdf-3131-8657-48ea7863af2b | -15.6836 | -59.734 | 2024-10-25 00:56:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 553d8ee3-8733-32d8-9245-b66741c9f425 | -16.94 | -57.5268 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| cd40be81-3e82-3437-9f37-eed91d083060 | -16.9596 | -57.5245 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| 28d10ce1-964f-30ed-b011-629fd20358d8 | -16.9789 | -57.5428 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 2c0bfc35-6d53-3215-8c31-66145a053ccb | -16.9792 | -57.5223 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 144.2 |
| 3c0ed402-3c0b-3ae9-bd7f-265c6fff6cfd | -17.0184 | -57.5178 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 744b04db-5f3a-3fa5-a9c5-8f641239aeb5 | -17.0381 | -57.5155 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| e9065d52-0b29-3278-ac7a-d2964a03e28d | -17.039 | -57.454 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 59b00e36-35df-30bd-b49b-b00b855d94a3 | -17.0583 | -57.4722 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 6d5ef970-6f3e-338f-9f92-48cf250fb22e | -17.0586 | -57.4517 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.2 |
| f88c8395-d908-36d4-b55f-f168b83746c8 | -17.059 | -57.4312 | 2024-10-25 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 8d9085a2-a5c0-33f1-bef2-591ade2c3a7e | -17.2386 | -57.2256 | 2024-10-25 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| e43e28f2-4fa1-36d8-ad66-ea0dd5fb5795 | -17.2537 | -57.5108 | 2024-10-25 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 10c58e8d-14ab-318d-b44b-6d26ff8b2873 | -17.2733 | -57.5085 | 2024-10-25 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 6552743c-be4c-3aae-b7ec-1028162fde16 | -17.7671 | -57.3673 | 2024-10-25 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 50cc95eb-831f-39f2-a59f-9c63b6993c24 | -17.7868 | -57.3649 | 2024-10-25 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| d256a8a6-55ea-32d7-962f-71b8eaeb1a07 | -17.8042 | -57.5067 | 2024-10-25 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 01a3b153-dbf8-373d-822c-d7cf8bf9f0ed | -17.8239 | -57.5043 | 2024-10-25 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 73ad1ea9-0773-39d8-9232-5e4afd33310c | -17.8624 | -57.5612 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 332738a9-be9c-387a-9583-6d15f7afc7f1 | -17.8822 | -57.5588 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 914bda8e-7cae-3260-8e8a-1e7686d93363 | -17.8825 | -57.5383 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 4caeade6-b888-3860-ba7b-436344fc4764 | -17.9019 | -57.5564 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 1da26560-0b2a-337a-8dbc-ed444137fe5c | -17.9023 | -57.5359 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 94bfda48-b6d2-3c07-b50b-d2edd8e70eb0 | -18.0056 | -57.2555 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| b57bd8ef-9caa-3902-ad4f-504888da6c4b | -18.0254 | -57.253 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 1479ca1a-6085-312d-8b6f-4aa26586c3a4 | -18.0257 | -57.2324 | 2024-10-25 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 13b751a1-f970-3e0f-8ce8-23800ff00864 | -18.1226 | -57.344 | 2024-10-25 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 0562d234-1119-3a00-a713-68f6fd77fbc3 | -19.6264 | -56.7079 | 2024-10-25 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| d94ba856-8dbb-35ea-83fe-04a9d0e3abb8 | -19.6268 | -56.6869 | 2024-10-25 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.9 |
| a1606275-7cd2-3747-9511-342962be3c4c | -19.6272 | -56.6659 | 2024-10-25 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| a4225338-4137-32d1-b7c8-b74022af1957 | -19.6465 | -56.7051 | 2024-10-25 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| b72c831f-1191-3c9f-8e25-3a0945fd9637 | -19.6469 | -56.6841 | 2024-10-25 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| f1e40e03-ae8b-3e95-b92b-83b56bc4253b | -19.6473 | -56.6631 | 2024-10-25 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 8bc92493-123f-3d8f-9706-d51bbf270bf7 | -19.6871 | -56.6784 | 2024-10-25 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.8 |
| 9b22dc25-8190-3901-937c-213c7fe60ac0 | -1.0445 | -47.6237 | 2024-10-25 01:05:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 9d3b9af6-c2cc-3273-8fc1-37b091545e0e | -1.0446 | -47.602 | 2024-10-25 01:05:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fb27cc0d-0359-31dc-b673-453b2b1ff4d7 | -1.1834 | -53.6771 | 2024-10-25 01:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6ec10132-76db-3811-9be6-9b2877289d42 | -1.1834 | -53.6569 | 2024-10-25 01:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ae24052c-79c9-3a99-9eb4-86ebbe219a26 | -1.1925 | -47.6002 | 2024-10-25 01:05:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 9af4286e-d966-30e7-8fc5-534fe0f34faa | -1.211 | -47.5999 | 2024-10-25 01:05:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4e4884c1-b442-3337-82b9-48d300f2dcf3 | -2.6192 | -52.4564 | 2024-10-25 01:05:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 71ed5af1-fa11-367c-9830-2f6554bca697 | -2.6193 | -52.4359 | 2024-10-25 01:05:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| cce77e07-21d9-3cc6-9035-29ad0c7b439f | -2.6297 | -49.247 | 2024-10-25 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 3b582180-5619-3126-a85a-4bde077edc56 | -2.6482 | -49.2465 | 2024-10-25 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 350f49df-018b-3642-8aff-04ee35f70f51 | -2.796 | -49.2636 | 2024-10-25 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8fe67dc7-65af-3eb8-ac39-d12c42e4e5b3 | -2.796 | -49.2424 | 2024-10-25 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| b51e3170-e79b-3b20-8557-87ac3e97bf40 | -2.8144 | -49.2631 | 2024-10-25 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 37937574-cf4d-3221-b6d6-c4ef0c9a3535 | -2.8145 | -49.2418 | 2024-10-25 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 6ff5af96-dc9c-3ec8-8ab2-fcecb372f151 | -2.9578 | -50.4198 | 2024-10-25 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9c1c2ee0-64de-3dac-afb3-5b618f9dd132 | -3.1116 | -53.7234 | 2024-10-25 01:05:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d1357166-9177-3cd0-ad4c-d303a8980796 | -3.3124 | -49.5235 | 2024-10-25 01:05:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 91cc0ab6-08e6-34b2-9a7f-7b9ad4f1bce2 | -3.4951 | -54.4366 | 2024-10-25 01:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9d1462c4-737f-37cd-a0b7-2c363b1bb7db | -3.9394 | -46.445 | 2024-10-25 01:05:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 635c1cac-48da-315a-8159-1829e9c6f543 | -3.9396 | -46.4229 | 2024-10-25 01:05:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 44601cbd-4ca4-3844-ace1-71801ccc5fea | -3.958 | -46.4442 | 2024-10-25 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ed5c5fe3-2b14-32e4-b5a2-f7b8a544c7b3 | -3.9581 | -46.422 | 2024-10-25 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| fd18a35d-3b5c-3bd7-86e1-aff4820a3980 | -4.2429 | -48.5474 | 2024-10-25 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| ace7e370-9361-3c00-a549-ed2daa6ab740 | -4.2441 | -48.332 | 2024-10-25 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 45986a9f-6638-3a71-94b2-4c5e6b9331bf | -4.2626 | -48.3311 | 2024-10-25 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1681625d-e10c-35f7-b024-8b97f22fc11d | -4.5045 | -48.2117 | 2024-10-25 01:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ac16516a-a7e1-37b5-97fc-e43876e0dccc | -4.58 | -48.0132 | 2024-10-25 01:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 34943c65-2df0-30ea-8015-2f6b6a69c8d7 | -4.8423 | -45.0309 | 2024-10-25 01:05:32 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9f220593-e4ef-368b-a9b2-2175a00fdd1d | -6.5219 | -60.0457 | 2024-10-25 01:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| c7441488-7a6d-3416-8748-9e8cb7660b98 | -6.522 | -60.0266 | 2024-10-25 01:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 30c875f9-58df-3bc3-8982-4d5bcfab9be9 | -6.6472 | -47.8642 | 2024-10-25 01:05:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 6b71d8be-be1b-3b96-b45b-273d9df151c3 | -8.9064 | -48.544 | 2024-10-25 01:05:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 3f0cd772-4541-3660-960d-c79773c3b863 | -11.902 | -56.4135 | 2024-10-25 01:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 38944051-0a07-3c1b-9ad0-46e406fe4ca1 | -11.9022 | -56.3934 | 2024-10-25 01:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| bce5c402-5641-3c61-8683-4215d87b272e | -12.0444 | -63.1547 | 2024-10-25 01:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 6662beff-8a73-34ae-b7d1-75e2cdcd3a7c | -12.0445 | -63.1356 | 2024-10-25 01:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 3642df66-9c03-3a89-989d-79958fb2ea21 | -12.0632 | -63.1537 | 2024-10-25 01:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 109.7 |
| f58f33bb-50f1-39c1-848d-bf414c3d3868 | -12.0634 | -63.1346 | 2024-10-25 01:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 104.3 |
| fce564b7-7bef-36da-984d-c15c53a6bb70 | -12.3782 | -63.8821 | 2024-10-25 01:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 64f3a89f-7ca6-328a-8feb-d475c00c462c | -12.3783 | -63.863 | 2024-10-25 01:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 24675bfa-706c-38f9-a903-91b28bc030be | -12.3971 | -63.8811 | 2024-10-25 01:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 46e289d5-514f-3c24-9b6e-9713cf6cb4ce | -12.4589 | -63.1895 | 2024-10-25 01:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e5ff30f6-1387-371e-b94c-10977812f982 | -12.4591 | -63.1704 | 2024-10-25 01:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.0 |
| c935b169-5a8b-392f-a4ac-e5c5d1af624b | -12.4593 | -63.1512 | 2024-10-25 01:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7d1369ca-5105-3947-bc46-7ac5ff74aa80 | -12.478 | -63.1693 | 2024-10-25 01:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 304e8ffc-cd44-3fac-a9e5-55eb463a4de2 | -12.5167 | -63.0521 | 2024-10-25 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f8428def-2119-3449-b715-c54ac7d64e1d | -12.5356 | -63.051 | 2024-10-25 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| cf207673-2cfa-3c6b-a587-cc3357470741 | -13.4767 | -61.6411 | 2024-10-25 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 46e969f5-485a-3166-84f4-db33566c358e | -13.4769 | -61.6217 | 2024-10-25 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| abac170d-f538-3b4c-b19d-b194dfbaf752 | -13.4957 | -61.6398 | 2024-10-25 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 897c09a4-ef8b-3522-83df-5631fab9b2c5 | -13.4959 | -61.6203 | 2024-10-25 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 9ba937f7-1791-3ce5-8756-e80f2e750383 | -16.94 | -57.5268 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| d219ebd2-aadd-31d1-90ca-1ef990221405 | -16.9596 | -57.5245 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 7b4bc578-efd9-363b-857f-798f2ba07e91 | -16.9789 | -57.5428 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| d06076f9-b2b1-3e7f-b178-230ebbe91479 | -16.9792 | -57.5223 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.3 |
| 41c52d96-5a1a-31b2-b9f6-22ed502bb535 | -17.0184 | -57.5178 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 099b10c4-c2c4-302d-bfc0-58294f3b9ec4 | -17.0381 | -57.5155 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 4a2306f7-fa97-3c19-af76-ceea8f0f519b | -17.039 | -57.454 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 1166c5c9-d4bf-37f8-903b-699c36c3d8ed | -17.0393 | -57.4335 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |


[Clique aqui para ver as próximas entradas](README11.md)
