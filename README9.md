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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf9c8c0f-7903-3a41-95f8-a0a787bb9532 | -19.5083 | -56.5989 | 2024-11-01 02:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 27882ba7-1acb-3f86-a0d1-ec17de2001d6 | -19.5087 | -56.5779 | 2024-11-01 02:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| dfa5cb46-a2f3-364f-8cf2-8d6b4966949a | -19.4882 | -56.6017 | 2024-11-01 02:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 30d17b26-57a6-3739-aff7-f04d1c38a082 | -19.4878 | -56.6227 | 2024-11-01 02:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 2c240df4-9c1e-3333-bb81-c59b4d9bd21b | -2.1695 | -48.7252 | 2024-11-01 02:45:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a3b0b5c7-d220-36c8-9a31-dc0d791488bf | -2.57 | -45.3382 | 2024-11-01 02:45:20 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 48ad8fde-b780-3c50-8bbd-9fb52c0674c8 | -3.0353 | -49.4901 | 2024-11-01 02:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 488411d5-05c4-3af2-a323-d30be7848302 | -3.0354 | -49.4688 | 2024-11-01 02:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5d3f5f2f-f60d-3891-8be2-6aaac1914332 | -3.0538 | -49.4895 | 2024-11-01 02:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c4d8752b-8908-3bc4-abea-4904918868b4 | -3.0539 | -49.4683 | 2024-11-01 02:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4480a7dc-5449-36c9-95af-e376fd808457 | -3.5631 | -47.3847 | 2024-11-01 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| d0b49811-a070-316b-a079-e6a9ea47db29 | -3.5632 | -47.3629 | 2024-11-01 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e69ab5a9-0aa8-3bc2-a860-59bc3ee6b78c | -4.3867 | -43.4757 | 2024-11-01 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 7aa16c14-f1b7-3efa-afee-5407025eb5dd | -4.3869 | -43.4525 | 2024-11-01 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 882891d2-c8d9-32d3-86b0-46b17e651ae2 | -4.4054 | -43.4746 | 2024-11-01 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.0 |
| c4f3b253-3495-3372-886b-79b213c54cbd | -4.4056 | -43.4514 | 2024-11-01 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 981c4b01-4796-36e0-8990-94cf40c5bc59 | -4.9023 | -47.0577 | 2024-11-01 02:45:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 3e085570-28aa-3b47-936f-9c62187702e5 | -4.9024 | -47.0357 | 2024-11-01 02:45:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 987eb545-5c31-3255-9147-076d2bf3bf5a | -4.9211 | -47.0346 | 2024-11-01 02:45:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 42d892f5-6ec1-3f66-92de-71b5f777e670 | -6.1039 | -43.9824 | 2024-11-01 02:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ce1448ce-40fe-3f0a-a407-1fa33a03be04 | -6.1041 | -43.9593 | 2024-11-01 02:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| d4798c71-bc27-3f52-bcae-2f15108336a1 | -6.1226 | -43.9809 | 2024-11-01 02:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f4eed9e2-0f86-37e4-a7a9-de3873b61fa8 | -6.1229 | -43.9578 | 2024-11-01 02:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 650b32e2-7c9d-3b39-84d7-89bd1b613e80 | -6.0931 | -47.225 | 2024-11-01 02:45:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| d1219da9-abd5-3342-b024-e0eebd88c9f0 | -16.9008 | -57.5313 | 2024-11-01 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 45320bc0-a47f-3ced-a6e1-c0d1f4a697a8 | -16.9012 | -57.5108 | 2024-11-01 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 2ac48eb7-a6c0-37c1-879a-12012186d31b | -19.4878 | -56.6227 | 2024-11-01 02:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 0d07d21c-eead-3a4d-8e11-11f4b663656e | -19.4882 | -56.6017 | 2024-11-01 02:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| d335d00d-adac-3a61-8751-4758307117ef | -19.5079 | -56.6199 | 2024-11-01 02:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 5488f447-3980-3702-846c-c5de24274e1a | -19.5083 | -56.5989 | 2024-11-01 02:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 9100acd9-f1ed-327d-8606-ca6026d094b1 | -19.5087 | -56.5779 | 2024-11-01 02:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 1e523300-4c38-37a5-b830-bd12dff26007 | -19.6063 | -56.7108 | 2024-11-01 02:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| f6ac1837-8f0d-38af-8c61-4494d55f28d5 | -5.78415 | -35.39417 | 2024-11-01 02:49:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 121a8312-3b47-3444-889a-c62dfb09c884 | -5.78319 | -35.39034 | 2024-11-01 02:49:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 98ef0cad-0bd9-3e80-bae9-fe0b5afd83d0 | -5.7821 | -35.39635 | 2024-11-01 02:49:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 25bef273-be7c-3193-aab3-355069f5423d | -3.0538 | -49.4895 | 2024-11-01 02:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 26a64043-3d33-3493-98d3-89135efba2aa | -3.0353 | -49.4901 | 2024-11-01 02:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 48ff447b-aa01-3795-a900-17f76b8f588b | -3.5631 | -47.3847 | 2024-11-01 02:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| b05c4b84-4b99-3bc3-8f05-0ec2d5f161e6 | -4.4054 | -43.4746 | 2024-11-01 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| a73acb85-33cf-3667-a836-411c2b09d681 | -4.3869 | -43.4525 | 2024-11-01 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a9872a38-06aa-3bb8-8b75-fe5e39022fd8 | -4.3867 | -43.4757 | 2024-11-01 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 185fab79-ca43-382b-91b7-6b91b4e74b79 | -4.9211 | -47.0346 | 2024-11-01 02:55:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 95897ca5-ee48-35ec-9da7-895db2728016 | -4.9024 | -47.0357 | 2024-11-01 02:55:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| dd1b2f92-720f-33bd-b598-88c591c9f270 | -6.1229 | -43.9578 | 2024-11-01 02:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 3d9f92b4-328c-3e25-8c56-5696c5d28e1f | -6.1041 | -43.9593 | 2024-11-01 02:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f5774f20-e305-3d3d-ad87-0001da4ba7af | -16.9204 | -57.5291 | 2024-11-01 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| cba47539-c04f-3c46-8328-c07efc987f0c | -19.5087 | -56.5779 | 2024-11-01 02:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| f40160a1-b625-371b-ae0a-7e7305caf3c2 | -19.5083 | -56.5989 | 2024-11-01 02:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 2f488bf8-c632-3968-8eb7-ea3bf0ea73fc | -19.5079 | -56.6199 | 2024-11-01 02:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| a8ee3dde-cf6a-36fe-a12a-de97d6f512db | -19.4882 | -56.6017 | 2024-11-01 02:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| f5c4d74d-d793-3bcc-b67a-3a19e1a31649 | -19.4878 | -56.6227 | 2024-11-01 02:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| bd40c1d6-e610-3e62-b056-efaf89fe675a | -2.1695 | -48.7252 | 2024-11-01 03:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d548aa84-3286-3e50-a437-4915363a29ea | -3.0539 | -49.4683 | 2024-11-01 03:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 40c591cf-f566-37b9-998c-9388f7efefaa | -3.0538 | -49.4895 | 2024-11-01 03:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 75b0d774-2a65-398b-a867-3d46bdf192ba | -3.0353 | -49.4901 | 2024-11-01 03:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 8c878ccc-d651-34ff-9916-20edde53b0dc | -3.5631 | -47.3847 | 2024-11-01 03:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| dca2aa87-b6ed-31ad-899f-832b84e53b44 | -4.4056 | -43.4514 | 2024-11-01 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 0daccd6f-11b1-3733-afa7-5994ca5af3cf | -4.4054 | -43.4746 | 2024-11-01 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 97b46e80-068b-31fc-8cd8-95ceb59d07e5 | -4.3869 | -43.4525 | 2024-11-01 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5400306b-b3f4-3e7d-b2ca-59d6aaed48ee | -4.3867 | -43.4757 | 2024-11-01 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 9ba405c4-abe5-321c-98b0-786cb380c054 | -4.9211 | -47.0346 | 2024-11-01 03:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 693c5a5d-f29f-3913-be66-9ce4bb35ddef | -6.1229 | -43.9578 | 2024-11-01 03:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 5d697013-341b-35db-91f7-bd7717c8fa4b | -6.1041 | -43.9593 | 2024-11-01 03:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 3cc44682-15ae-345a-9560-7c05bb51b805 | -16.9204 | -57.5291 | 2024-11-01 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 8b05cb54-a5a0-3170-b6ed-c20474dde676 | -19.5079 | -56.6199 | 2024-11-01 03:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 8ab74a87-3843-3326-95c7-9b6471d14a6d | -19.5083 | -56.5989 | 2024-11-01 03:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 5ea4de22-45d2-3893-b8b8-b638bc09ce9f | -2.1695 | -48.7252 | 2024-11-01 03:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 63308f73-f6e9-37b1-950d-03a9cf67d154 | -3.0354 | -49.4688 | 2024-11-01 03:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3b3bd099-0d66-34a4-8fbf-9f7f9cf0b286 | -3.5631 | -47.3847 | 2024-11-01 03:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| e5c9880c-c03b-346e-b1d1-171bfc745322 | -4.3867 | -43.4757 | 2024-11-01 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 3623976c-eb8d-3859-9366-c191951b4d40 | -4.3869 | -43.4525 | 2024-11-01 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a21b2352-5ed8-3dd0-be85-c6f72d4f0f4e | -4.4054 | -43.4746 | 2024-11-01 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 232.4 |
| fda33e40-20e7-3a28-bb0a-f226b9bf26bd | -4.4056 | -43.4514 | 2024-11-01 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 73555742-eeed-3318-bec4-c209db4d89e7 | -4.9211 | -47.0346 | 2024-11-01 03:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8d7c0fe0-bc98-3fa4-88fd-b4f646e1f7cf | -4.9023 | -47.0577 | 2024-11-01 03:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c26835b5-cfbe-3793-85fc-b24cf3048e2a | -4.9024 | -47.0357 | 2024-11-01 03:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 39b56a9c-cab7-3f70-9ba7-0a07984abdbb | -6.1041 | -43.9593 | 2024-11-01 03:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f4b4fde2-e83e-3a94-8cf9-5c5810634a21 | -6.1229 | -43.9578 | 2024-11-01 03:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| aa4156d5-3ee5-3c03-a44a-29f9aeb43837 | -16.9008 | -57.5313 | 2024-11-01 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 195980d4-dda3-3620-9b2d-1c7fd0b2d58e | -16.9012 | -57.5108 | 2024-11-01 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 81685d8d-0cb7-3d53-a862-857aa5cb65a6 | -17.6664 | -57.5028 | 2024-11-01 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| d907d1d8-acf4-359b-8696-8a3a341626e1 | -3.0353 | -49.4901 | 2024-11-01 03:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 29351b70-cf1d-37c8-856b-ddfd09b9430a | -3.0354 | -49.4688 | 2024-11-01 03:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| eb2705f4-c2be-3dcf-b7dc-6d3c47703afe | -3.0538 | -49.4895 | 2024-11-01 03:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 135f76a0-b146-3e6c-993f-c38106bf06ac | -3.0539 | -49.4683 | 2024-11-01 03:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| eba4239c-2805-3f42-9b08-117cb6dcc998 | -3.5631 | -47.3847 | 2024-11-01 03:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 9ebad719-49f7-3d13-aeb3-0645854dbb37 | -4.3867 | -43.4757 | 2024-11-01 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 3821cc6c-4502-39b9-8cc4-57e7e89e9c94 | -4.3869 | -43.4525 | 2024-11-01 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9b3c39a8-d373-381f-96e5-d492a2dc68d5 | -4.4054 | -43.4746 | 2024-11-01 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 20fe88f2-7ddb-32e0-8be7-2fb7efbfeb8b | -4.4056 | -43.4514 | 2024-11-01 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7a0fee84-a198-324a-bab9-7da885e129b5 | -4.9024 | -47.0357 | 2024-11-01 03:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e1ffdfdd-23cb-3e56-832e-f7e6146610e6 | -6.1041 | -43.9593 | 2024-11-01 03:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 25080e7d-2645-3a6b-b4d4-586aa6591b87 | -6.1229 | -43.9578 | 2024-11-01 03:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 9bdbf3f5-ebbd-3fc7-a378-fd370c64ea1a | -9.9186 | -64.8246 | 2024-11-01 03:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f57623d2-a1fa-363d-9a90-d083c981c972 | -9.9187 | -64.8058 | 2024-11-01 03:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0927e8f8-86d7-3ff3-a4fb-f8324907db26 | -16.9008 | -57.5313 | 2024-11-01 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| c8a47ff2-79be-3733-ad3b-cba7dc09bd4d | -17.7249 | -57.5368 | 2024-11-01 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 7290d4ec-c0b0-3d4d-a4e7-cf2e8154f95e | -3.0539 | -49.4683 | 2024-11-01 03:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 3f4b7597-ae66-3c2e-b7eb-51cbbf2fcb06 | -3.0538 | -49.4895 | 2024-11-01 03:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| b72a8ae2-bc14-3173-9ba9-fa51a03ae764 | -3.0354 | -49.4688 | 2024-11-01 03:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |


[Clique aqui para ver as próximas entradas](README10.md)
