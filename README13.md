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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35802472-829f-3ff4-b4ec-007f8843418d | -14.2654 | -51.4123 | 2024-10-29 00:56:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a0b43bf8-63da-328f-88d4-9c14e53f2b76 | -1.714 | -54.5335 | 2024-10-29 01:05:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 76ca0d45-bde1-3984-b0e0-5fd880fb7567 | -2.3352 | -48.9351 | 2024-10-29 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 3e7c9d21-138b-3fbc-b4e8-5787be30cf59 | -2.3353 | -48.9137 | 2024-10-29 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 10b6c290-5ff2-3c74-a247-26f17236b443 | -2.3353 | -48.8924 | 2024-10-29 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fcc3cca5-be70-3df9-b616-8eb7a72d5d46 | -2.3537 | -48.9346 | 2024-10-29 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f1541a4c-f80d-38da-b18d-c3bb5037671b | -2.3537 | -48.9133 | 2024-10-29 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 328.8 |
| ed975494-d93d-35f6-93ab-848710b41fcb | -2.3538 | -48.8919 | 2024-10-29 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 9e1074f3-6c8c-35c9-94ac-71a805286e22 | -2.5066 | -47.4425 | 2024-10-29 01:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9de30093-1da0-3216-b8d3-b54568b47c7f | -2.5251 | -47.442 | 2024-10-29 01:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b0f8cf1f-5a5f-3c73-8990-2117a2e02f17 | -2.8555 | -53.3459 | 2024-10-29 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e45b4911-4cea-3edf-8409-adc1471fa83d | -2.8739 | -53.3454 | 2024-10-29 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2e00b864-eb27-39cf-9164-b85ad82824f8 | -2.9803 | -54.5299 | 2024-10-29 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 857d7e2f-9b78-3dd0-9ce6-b52284c28e92 | -2.9804 | -54.5099 | 2024-10-29 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 925d83bf-0186-394d-97f6-e1255c8fa706 | -3.0734 | -54.167 | 2024-10-29 01:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5234c671-0b01-3bb1-ba72-3dd4d19a5f73 | -3.0913 | -54.287 | 2024-10-29 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| bab64f8a-060a-3103-bb75-c47f02a4bd96 | -3.1097 | -54.2865 | 2024-10-29 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| cc3b9d7b-f277-36f9-9d34-f1fef5c1c58e | -3.1098 | -54.2665 | 2024-10-29 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 9c8665c0-c7ca-3eee-a5dc-242b90a5235a | -3.1281 | -54.266 | 2024-10-29 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4299c32b-23b9-371b-850a-1d3c478219f1 | -3.1794 | -50.3922 | 2024-10-29 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 318cdc20-0035-3cd7-812a-2da946d9fc23 | -3.3044 | -47.198 | 2024-10-29 01:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 71dbe480-b83d-3453-bf28-317fbfb706f4 | -4.3286 | -43.7801 | 2024-10-29 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 78498125-0e48-3d99-a301-4219f33f25ce | -4.3288 | -43.757 | 2024-10-29 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b4b0b2a2-08ba-3ffc-987a-51f6e326ce11 | -4.3473 | -43.779 | 2024-10-29 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 306.7 |
| 4071a3da-c41f-36fb-b634-eaa5986f7ae4 | -4.3475 | -43.7559 | 2024-10-29 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 753ade98-97ea-330b-9b8f-630804641890 | -4.366 | -43.778 | 2024-10-29 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 1707abee-ba9b-3d3a-b05a-fe2a10c353ee | -4.3661 | -43.7548 | 2024-10-29 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 540c5188-8ec7-3515-9bb5-e06e76bbcb5b | -4.2762 | -46.0956 | 2024-10-29 01:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 81a5d64f-0bc3-343d-8c53-4e85420cc801 | -4.6432 | -44.1762 | 2024-10-29 01:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| daa94265-88d1-304b-86a5-6962c237c13f | -4.6618 | -44.1981 | 2024-10-29 01:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c8fb5a9a-d1f2-338b-a7d6-34f644dc427c | -4.6619 | -44.1751 | 2024-10-29 01:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 0c975a98-d023-3f9a-82c4-aadcb24e73fa | -4.6621 | -44.1521 | 2024-10-29 01:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 902d5d78-7a04-3330-ab84-8371882a2f5f | -4.8397 | -42.911 | 2024-10-29 01:05:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 3319294b-00bf-3b1f-bdf9-79efe376e8af | -4.8584 | -42.9097 | 2024-10-29 01:05:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 886bc2a3-3d8c-3de0-a282-63d492828725 | -4.9326 | -45.4321 | 2024-10-29 01:05:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| c3f1d44d-d0d7-3faf-abb9-fe37f1d46e6b | -6.5956 | -47.3867 | 2024-10-29 01:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d9aa8d01-8c33-3b86-a907-de1edcddc98e | -6.6141 | -47.4073 | 2024-10-29 01:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bd9f3592-4fb5-38fc-b6cf-ba0478538c59 | -6.6143 | -47.3853 | 2024-10-29 01:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 9674f151-b1e0-3d85-a909-95396ac56b8c | -11.138 | -55.5313 | 2024-10-29 01:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| a2fcc3d2-0efb-31b4-a383-66b45626c826 | -12.3334 | -49.9208 | 2024-10-29 01:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 31a63f0f-fca9-38e3-b523-9ac5024c27df | -12.3522 | -49.94 | 2024-10-29 01:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 36288707-fafe-35e6-8db2-17cfffa2f549 | -12.3526 | -49.9184 | 2024-10-29 01:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 01345384-54e0-37ae-9244-dd6c0fedaa8f | -24.012501 | -54.101501 | 2024-10-29 01:07:46 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e0a516a-cb07-30f8-b24d-16551a17a98b | -24.014099 | -54.108898 | 2024-10-29 01:07:46 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d93e60ba-293d-38d5-8d74-d99bbfcc36bd | -24.015699 | -54.116402 | 2024-10-29 01:07:46 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 02357ee9-8c86-33f8-82dc-78f7f1094317 | -21.8165 | -53.476299 | 2024-10-29 01:08:19 | METOP-B | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 04ee0d82-0363-3624-ae2f-a968006536ed | -21.8181 | -53.483799 | 2024-10-29 01:08:19 | METOP-B | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a46ef4c7-62e1-30f3-ae90-2e9a55bc4034 | -20.2796 | -55.4025 | 2024-10-29 01:08:51 | METOP-B | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 772a3ccf-b7ba-3ad0-8107-bbd26e5bf2a7 | -20.2812 | -55.409801 | 2024-10-29 01:08:51 | METOP-B | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 70b67f23-0e64-3395-aaab-fe9703f33021 | -19.597799 | -56.697201 | 2024-10-29 01:09:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6dd8beda-a02c-3efd-b72b-2d69cd252ccc | -19.5219 | -56.578899 | 2024-10-29 01:09:07 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 64b55553-53d7-3414-a4b6-478d749261fb | -19.511499 | -56.676899 | 2024-10-29 01:09:07 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cc02544a-ffef-32ad-8442-8b8ae1491f93 | -19.490601 | -56.6259 | 2024-10-29 01:09:08 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bd6d9997-e6ff-372b-8f81-0077469e8a7a | -14.1379 | -44.0429 | 2024-10-29 01:09:44 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22a85083-c0ea-3ee2-8dd2-21d2dfb45006 | -14.1284 | -44.0457 | 2024-10-29 01:09:44 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9e80b98-00ae-3f37-914f-ba7c3ef6b7e3 | -14.1371 | -44.076801 | 2024-10-29 01:09:44 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 626b28f9-b9b9-3e1a-a5ad-6d63915aa88d | -14.119 | -44.345001 | 2024-10-29 01:09:46 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2539ff3d-6d97-3b6c-8360-6f9af72a2165 | -13.6858 | -46.084499 | 2024-10-29 01:10:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bbe3d60b-69cc-3ae0-a164-ff436f780103 | -13.6762 | -46.0872 | 2024-10-29 01:10:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 319024fa-20a4-3d9b-bf0c-66fa0d2d224f | -13.6824 | -46.110298 | 2024-10-29 01:10:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 219096f2-f853-3f30-a457-ef4bfb03f334 | -14.2622 | -51.410999 | 2024-10-29 01:10:13 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92d9118c-4c43-32a0-8a15-3e44e3880b79 | -12.6343 | -47.536701 | 2024-10-29 01:10:23 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef9138e7-cc89-36e7-9bbf-35de80ea64cf | -12.353 | -49.917599 | 2024-10-29 01:10:38 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31e6da4f-5493-32c5-b1aa-1bfea24305c1 | -12.3399 | -49.906601 | 2024-10-29 01:10:38 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92373f06-43f0-31c6-8541-c9dd22f9ec0d | -12.3433 | -49.920101 | 2024-10-29 01:10:38 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1c32bdf-bf41-3dd3-9f37-cd699923a7a7 | -12.3467 | -49.933701 | 2024-10-29 01:10:38 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3120df3-d87d-3814-93ac-fe364a224c09 | -13.2654 | -53.9147 | 2024-10-29 01:10:39 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34785b0b-2e64-30d3-a764-1c35b4b59e72 | -13.2557 | -53.917099 | 2024-10-29 01:10:39 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25bbbca6-4877-3a48-abb4-c55e31151f30 | -12.0979 | -52.4688 | 2024-10-29 01:10:52 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf08f23-425e-316c-ac90-b1e03d2141cf | -12.1002 | -52.478298 | 2024-10-29 01:10:52 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 514dd0d6-cdee-33ca-b388-ed3fc4ff7522 | -12.7704 | -56.6381 | 2024-10-29 01:10:57 | METOP-B | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab90421-8381-344a-a0f5-7e4259c11521 | -11.9094 | -54.791302 | 2024-10-29 01:11:04 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ced211d6-3a93-3955-ab98-26350d03b7a4 | -12.218 | -57.2122 | 2024-10-29 01:11:08 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd7eadbf-3a61-3903-b9ec-2a6d93639b61 | -12.2196 | -57.2192 | 2024-10-29 01:11:08 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25a69d33-1f0f-34f2-b743-13b8dd962ea7 | -12.1102 | -56.818401 | 2024-10-29 01:11:08 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31804821-ecdc-364f-9289-621be0042cf6 | -11.5652 | -54.4627 | 2024-10-29 01:11:08 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3a01df-d462-3a17-bd98-c3cb55091675 | -11.77 | -55.444199 | 2024-10-29 01:11:08 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c955e5a7-4a57-3a85-b619-35eddd990556 | -11.7716 | -55.4515 | 2024-10-29 01:11:08 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96cc96ef-7266-3473-b0e9-9d2bc5b52c98 | -11.875 | -56.872002 | 2024-10-29 01:11:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2e477dc-8d63-309e-8df5-a1e0ec515e4d | -11.3328 | -55.201302 | 2024-10-29 01:11:15 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1718176b-309c-3280-8705-32db8577995f | -11.3345 | -55.208599 | 2024-10-29 01:11:15 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed36c6f-8558-3b3c-9083-e65b8ba8d752 | -11.4812 | -56.676601 | 2024-10-29 01:11:18 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 107cd5e2-1375-3856-801b-650d6cc0265b | -11.1464 | -55.513699 | 2024-10-29 01:11:19 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b77cc959-13be-3ff7-b918-27f0cf2c4fb1 | -11.148 | -55.520901 | 2024-10-29 01:11:19 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3b35ef-5f84-3a4e-803e-dcd2e2374f0b | -11.1497 | -55.528198 | 2024-10-29 01:11:19 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3a022e7-cb67-3c67-8403-f336213e63f4 | -11.1513 | -55.5354 | 2024-10-29 01:11:19 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce860df5-a0db-38bf-97c3-1bcce7a1b084 | -11.1849 | -56.275101 | 2024-10-29 01:11:21 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8a06a16-bb1e-3f42-b32c-6683c34e9e3e | -11.1865 | -56.282101 | 2024-10-29 01:11:21 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82971a34-4f4e-3e30-a5cf-0645c1053ccc | -11.1751 | -56.277302 | 2024-10-29 01:11:21 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 857f6406-4971-33bd-8b65-5a90ec9547b3 | -11.1767 | -56.284302 | 2024-10-29 01:11:21 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d37e8aba-2a18-3503-aeea-9b729541572e | -12.4491 | -63.655701 | 2024-10-29 01:11:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3fa3cfb-703d-3dea-963b-f9e058872552 | -10.8627 | -56.905399 | 2024-10-29 01:11:28 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85f197ea-706a-3001-8f14-3aa91862548c | -10.8643 | -56.9123 | 2024-10-29 01:11:28 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8d4e78c-963f-3dc1-98df-9afd27efe8b3 | -10.4238 | -55.061798 | 2024-10-29 01:11:29 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91f20242-b477-37e7-832f-5689365b6efd | -10.3494 | -55.007702 | 2024-10-29 01:11:30 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea28d8ea-e1bf-34b7-b1dd-d58a427b6b86 | -10.0363 | -54.324402 | 2024-10-29 01:11:32 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 005871b8-bb67-33fa-8d90-4c836ec12d2e | -9.482 | -54.514599 | 2024-10-29 01:11:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2a27aa5-69d4-3078-9578-c40183f0e1fc | -9.4838 | -54.522598 | 2024-10-29 01:11:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7ebba95-3ea5-3610-bf5e-6cf3846e8f8a | -9.7538 | -56.968102 | 2024-10-29 01:11:47 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16a6af16-2372-3709-87f5-5d23181efda8 | -9.3804 | -56.819801 | 2024-10-29 01:11:52 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
