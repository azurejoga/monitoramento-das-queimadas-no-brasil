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
| f8734cf9-ca3e-3608-a22e-b914f8811917 | -17.0583 | -57.4722 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 39227fab-f91c-3825-be27-768e9b7dd609 | -17.0586 | -57.4517 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| ff97c814-69cc-315f-8c9c-3d61dc47d8c0 | -17.059 | -57.4312 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 84037b7f-a363-3803-850c-f355669b508c | -17.0786 | -57.429 | 2024-10-25 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| aa94c75c-9b3a-3806-8736-c818c4c10d42 | -17.2186 | -57.2485 | 2024-10-25 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 2170aa33-2680-38b2-96ee-f4f02d757d04 | -17.2383 | -57.2462 | 2024-10-25 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| f423887d-ced5-36e0-8a8b-146e4b8e771b | -17.2386 | -57.2256 | 2024-10-25 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| b99b91f5-13ba-36c6-851c-58522e14c51f | -17.2537 | -57.5108 | 2024-10-25 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| bc738356-5007-3e62-b421-070e0a967b93 | -17.8239 | -57.5043 | 2024-10-25 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| b0af3101-2a32-38ea-887b-94e58be53a86 | -17.7634 | -57.5937 | 2024-10-25 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| ca8ab9ce-274d-3113-9ffc-f3d27e0edd2b | -17.765 | -57.4909 | 2024-10-25 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 9489b802-903c-3dbd-af13-07a14f1cbb55 | -17.8038 | -57.5273 | 2024-10-25 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| a76b87f2-1ae7-31ab-a922-a5ee30bbfef4 | -17.8042 | -57.5067 | 2024-10-25 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| c2a7c8d7-a058-307b-a249-bd2802ae231c | -17.8624 | -57.5612 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 7eab7fab-1586-3464-8f38-97ffcb4fcb6b | -17.8628 | -57.5407 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 8cafc21b-f28c-3ca8-a616-ae39e3053ae4 | -17.8822 | -57.5588 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 951c9112-ed95-3a9c-8574-ce080a2a59c4 | -17.9023 | -57.5359 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| c0976756-6b73-3351-a5b6-2ee492c58f7b | -17.9272 | -57.224 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 50a3888b-ee79-3cac-9507-940cef615896 | -18.0056 | -57.2555 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 18f6635e-518d-3370-a432-1ee8626505a9 | -18.0243 | -57.315 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 52725f7c-ada1-33b7-8b70-40ea1b35930f | -18.0254 | -57.253 | 2024-10-25 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| e7b4c35e-d3ab-358d-8ba7-9c3baecd8887 | -18.0438 | -57.3332 | 2024-10-25 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| c4656a2f-441f-3b9e-9354-026203cfd371 | -18.0441 | -57.3126 | 2024-10-25 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.2 |
| 65190b4e-8358-34f0-8c58-a9a11c64e5d3 | -18.0445 | -57.2919 | 2024-10-25 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 08117c0d-0ac0-30c4-872f-8e44c8e398e6 | -18.0452 | -57.2506 | 2024-10-25 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 97835151-f061-3f11-a558-f66817629d16 | -18.0639 | -57.3101 | 2024-10-25 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 48bdae14-43b1-31fe-90d4-44efad14b578 | -18.1223 | -57.3647 | 2024-10-25 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.0 |
| 151ed6e1-e935-3ba7-86c7-359b22643b9a | -19.628 | -56.6239 | 2024-10-25 01:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 78b61e27-eb1f-36c0-8e36-f295145d855d | -1.0445 | -47.6237 | 2024-10-25 01:15:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 189b86e5-4558-314f-a4d7-6c0c3fba78a7 | -1.0446 | -47.602 | 2024-10-25 01:15:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e96a6845-2b26-3dfa-8f68-a1b5252a82f6 | -1.063 | -47.6235 | 2024-10-25 01:15:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 749b1906-ba52-3f48-b548-cfa98018bc04 | -1.1834 | -53.6771 | 2024-10-25 01:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5a9b52b8-ef3e-3871-b56f-8f95c20149fa | -1.1834 | -53.6569 | 2024-10-25 01:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1632baf7-c58f-3aab-bfdd-01a5ec2bb8ff | -1.1925 | -47.6002 | 2024-10-25 01:15:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 842dd00a-0ac8-3416-ad35-6c31d00be6b7 | -1.1925 | -47.5784 | 2024-10-25 01:15:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e065229f-5df8-37d5-9bf3-b4f9296e6ecf | -1.211 | -47.5999 | 2024-10-25 01:15:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| b29b9763-cd72-3d55-acbf-a5eda1407721 | -2.0592 | -56.1141 | 2024-10-25 01:15:17 | GOES-16 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 4c7f75bd-6ec0-3aa2-a104-15e806cc2673 | -2.6192 | -52.4564 | 2024-10-25 01:15:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 77813fc6-79fe-3a1c-bc9f-f3cab27cfb9c | -2.6193 | -52.4359 | 2024-10-25 01:15:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ddb7ff5c-ee23-3e43-810b-861912fe567b | -2.6297 | -49.247 | 2024-10-25 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cd84f418-2ea3-3c2d-8398-f40d8d622ec6 | -2.6482 | -49.2465 | 2024-10-25 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 52cd40fd-5d3c-3d07-81e4-7fa7bbcdd60c | -2.796 | -49.2424 | 2024-10-25 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a934d492-2fad-331a-bca8-d1b6e8f15ad4 | -2.8144 | -49.2631 | 2024-10-25 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7e420f63-983e-35ab-bab0-64074ec00ff9 | -2.8145 | -49.2418 | 2024-10-25 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 0546f2f1-cb1e-333a-a731-1f73213e5bd9 | -2.9578 | -50.4198 | 2024-10-25 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3fb2082b-a78c-3185-8d91-c3dc4a0f369c | -3.2135 | -46.8063 | 2024-10-25 01:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 1a127fd2-9947-3eb5-b642-0561f9ac1dda | -3.2136 | -46.7843 | 2024-10-25 01:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| a06532bf-c3ea-3244-9d73-296a82e140b9 | -3.3124 | -49.5235 | 2024-10-25 01:15:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 08403209-ed1a-30cc-aac3-cd5ec5894dc9 | -3.4951 | -54.4366 | 2024-10-25 01:15:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| ad6d46df-9d4a-3c92-9ac4-a4b2c18d0e02 | -3.9396 | -46.4229 | 2024-10-25 01:15:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 00ec9986-e1cd-3404-99af-c453f56eb47c | -3.9581 | -46.422 | 2024-10-25 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a54f5515-d5e3-3b08-b74a-9d6e3b77ca0a | -4.2429 | -48.5474 | 2024-10-25 01:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 54eee37d-2f54-3c94-8f21-af0f34d04aed | -4.2441 | -48.332 | 2024-10-25 01:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8cd5cfcd-0a4b-3cf0-9f4f-76ef3dce1512 | -4.4271 | -45.7751 | 2024-10-25 01:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 542eb8f6-f9f7-3877-9a50-046856d89dbb | -4.5045 | -48.2117 | 2024-10-25 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8724f271-e10d-370d-a06a-a30e89b8bd4a | -4.58 | -48.0132 | 2024-10-25 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8c8191ae-1777-3f1c-9b7c-52a34a0add5a | -4.5986 | -48.0123 | 2024-10-25 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9ed110a6-a0f3-3aac-81b8-3ad3c188a012 | -4.861 | -45.0298 | 2024-10-25 01:15:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e5d96956-90ce-3b1a-8b30-c06620282a03 | -6.5219 | -60.0457 | 2024-10-25 01:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6784366b-2f56-3951-9073-8adb7532ee10 | -6.522 | -60.0266 | 2024-10-25 01:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 064cee22-3d74-3693-8c16-226aabe4628a | -6.6472 | -47.8642 | 2024-10-25 01:15:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ed12084a-1080-3196-8ad9-227f30bc3d1d | -8.9064 | -48.544 | 2024-10-25 01:15:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e89422a3-f3fb-36bd-9aab-f399ecd85846 | -10.6519 | -47.9207 | 2024-10-25 01:16:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ee70af85-e0c1-3210-9348-ac86a958dc14 | -11.902 | -56.4135 | 2024-10-25 01:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 9a89559f-aa18-3a91-8c5a-d95dc233bad5 | -11.9022 | -56.3934 | 2024-10-25 01:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8e58aeda-f83a-3256-8c7a-84ae0c0b5957 | -11.9824 | -63.9022 | 2024-10-25 01:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f19ee65e-aef1-3488-83e0-1d623fea5107 | -12.0011 | -63.9203 | 2024-10-25 01:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0f601475-f360-3431-9857-307a46d562b5 | -12.0012 | -63.9013 | 2024-10-25 01:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b9cbd4e8-3959-3cbd-af91-221def1cbe3b | -12.0444 | -63.1547 | 2024-10-25 01:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 4d7b5479-eca2-3ef3-a5bc-3864b934d340 | -12.0445 | -63.1356 | 2024-10-25 01:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a981a89c-7b77-3aaf-bf4e-b1fa842b7fe4 | -12.0632 | -63.1537 | 2024-10-25 01:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 42011d8b-22f3-3cc8-8f8e-a6285c489f1e | -12.0634 | -63.1346 | 2024-10-25 01:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 56499fa3-4f4a-3d55-b85f-afb4580ab713 | -12.3782 | -63.8821 | 2024-10-25 01:16:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| bef95203-2616-3edd-b1e8-dd69beb654e7 | -12.3783 | -63.863 | 2024-10-25 01:16:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7e82140d-22a9-33ca-a9f8-97278a2acfb1 | -12.3971 | -63.8811 | 2024-10-25 01:16:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2289795a-246b-3ef5-9de1-a64917ba8c60 | -12.4589 | -63.1895 | 2024-10-25 01:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 54e07c85-8985-3e97-8a34-c88fa3940ee9 | -12.4591 | -63.1704 | 2024-10-25 01:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 5d4bcfd1-8427-3a7a-a472-86b0964779ed | -12.478 | -63.1693 | 2024-10-25 01:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 92903e7e-d67f-3902-afff-96336b6c7a09 | -12.4781 | -63.1501 | 2024-10-25 01:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 71ab62dc-080e-35c1-890d-50d5be026869 | -12.5167 | -63.0521 | 2024-10-25 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 08dc1be4-3e9c-31c0-a565-8ce0fc82f5e0 | -12.5356 | -63.051 | 2024-10-25 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a586e877-19b4-30c0-8987-2eab4b80268c | -16.94 | -57.5268 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 1975068f-27f6-359a-a550-f8e3d856b97e | -16.9596 | -57.5245 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| e557f124-60dd-3709-9718-1a724a577b9f | -16.9792 | -57.5223 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 166.4 |
| 8f499836-1662-37fd-920a-fc530e6be4a3 | -17.0184 | -57.5178 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| c844a390-43ff-3a28-922f-a33ebb26c5d6 | -17.0381 | -57.5155 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 8944b160-8e45-3c49-b7e8-0f26b4a7ac5b | -17.039 | -57.454 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 65761e9b-2c2f-3c06-b46c-462b5d7f3a73 | -17.0583 | -57.4722 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 6ec658d3-805f-3658-8293-ca205a5e1384 | -17.0586 | -57.4517 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| e0b1da84-42c4-3a32-b8d7-48431166c6d8 | -17.059 | -57.4312 | 2024-10-25 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| b1f3ad6a-1b7f-3df0-a518-b582f107d20e | -17.8239 | -57.5043 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| defe1cc1-f735-3dc4-8e83-b3d379b74792 | -17.7453 | -57.4933 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 07a34652-745e-3e1e-a1ed-c610ca6b3c89 | -17.7634 | -57.5937 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 1350bf88-2ac1-3de8-a149-371655a8cd5d | -17.765 | -57.4909 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 66f4f237-65c6-3f2b-99bf-386dc494be47 | -17.7671 | -57.3673 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| fa1af1c1-7942-3f47-a3fb-dbbde304d9af | -17.8032 | -57.5684 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| aef39fa1-5611-3be9-9390-4be4aa14adca | -17.8038 | -57.5273 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 79dbdb74-73e1-35f7-aff4-24a928ad320c | -17.8042 | -57.5067 | 2024-10-25 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 02d8df3e-1446-36a8-8649-9d28c3fe2379 | -17.8822 | -57.5588 | 2024-10-25 01:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| cd781817-997b-3c6e-a4da-c01eeaf8cf81 | -17.9023 | -57.5359 | 2024-10-25 01:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |


[Clique aqui para ver as próximas entradas](README12.md)
