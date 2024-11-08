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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70fa78aa-814b-361b-b978-1b6f6839b26e | -3.5408 | -43.622101 | 2024-11-08 00:14:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb85b6ea-9520-393b-a65d-3838f3394199 | -4.5032 | -45.694801 | 2024-11-08 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdc4015a-70c3-3707-afd2-63f0e0a1d6d3 | -1.817 | -46.368401 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8df2ed7c-7893-3f3d-80bb-6148d89a66ff | -4.6168 | -46.525101 | 2024-11-08 00:14:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4addef9a-6f3e-349b-be9e-1ddf17478cc4 | -3.7979 | -44.028099 | 2024-11-08 00:14:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c73d8ef7-2f59-3c4b-99a0-720d3a9f9b53 | -3.2849 | -44.445801 | 2024-11-08 00:14:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e591964c-56f2-3393-a41d-ec8bc14c2bcb | -4.8218 | -47.3092 | 2024-11-08 00:14:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84fe4285-0945-3907-a19b-fa720eb3ee7d | -2.6764 | -51.8189 | 2024-11-08 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b2ae106a-9b4f-36c9-8c4d-b1d21aa91a14 | -3.1642 | -54.4654 | 2024-11-08 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 063bc18f-64a2-3886-b0d3-4fd0b2e23969 | -4.6646 | -46.4528 | 2024-11-08 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b32e16e7-084b-3348-b353-8cc42a5dc3e8 | -4.3161 | -45.669 | 2024-11-08 00:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9e2fb6e3-8938-350a-9261-5b23df593b54 | -3.7255 | -41.6748 | 2024-11-08 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 158.9 |
| 53f3506b-4d01-3dd6-bc60-2941c5d19ae3 | -4.2974 | -45.6924 | 2024-11-08 00:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 405ab1b5-6f4a-36e4-9c42-61ee4b6eb63c | -3.5632 | -47.3629 | 2024-11-08 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d2057ea0-65be-3659-867d-0c4d84754627 | -3.7861 | -44.0162 | 2024-11-08 00:20:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 92fe6e9b-8ba6-316f-a9f4-a24782642a64 | -3.0698 | -45.747 | 2024-11-08 00:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 127.6 |
| fef5db01-e5ec-3116-92a1-4b94c40ca3a8 | -2.6228 | -51.3038 | 2024-11-08 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| de08753c-a26a-3b2e-abd4-888c64d34087 | -1.3961 | -47.5103 | 2024-11-08 00:20:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 748f959c-3dbc-3cdb-9d08-f9c8889beb2f | -3.5631 | -47.3847 | 2024-11-08 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| a057a77a-20ec-3910-8e29-448636f331b3 | -3.4838 | -52.617 | 2024-11-08 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 688e96c5-c256-34af-a045-2bfe210de37e | -4.702 | -46.4286 | 2024-11-08 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 008996bc-0df8-3bee-b007-1d628684f3af | -2.6214 | -51.7585 | 2024-11-08 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| d1d721fc-8405-3589-9ee0-0000fbac2fde | -4.6832 | -46.4518 | 2024-11-08 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 417.0 |
| 7432c7f1-ef39-3820-9ad8-229271a0036a | -3.8047 | -44.0153 | 2024-11-08 00:20:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| bfec9fba-1fcf-312c-a5c9-66cd4f57c7a2 | -3.5447 | -47.3636 | 2024-11-08 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0cab7f5d-0026-3b0b-93f9-aa0ec7bcfa5d | -4.6834 | -46.4296 | 2024-11-08 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 223.2 |
| f817cd53-7a4c-3bc8-8263-ee4f8a2e3114 | -3.1641 | -54.4854 | 2024-11-08 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| c3de643c-0b89-3b02-93a3-cfb2cffe87a1 | -4.6835 | -46.4074 | 2024-11-08 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ec7b58fd-a5a7-3730-bbbf-3181fb71498e | -1.3776 | -47.5106 | 2024-11-08 00:20:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| deee750b-9807-31e6-9b87-c1e0ef2c4d7e | -3.1458 | -54.4659 | 2024-11-08 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 77815b46-6694-3585-be9e-177491e15d9d | -3.5446 | -47.3855 | 2024-11-08 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 9beff332-8bc1-3c6c-9a82-44a07dbeda5d | -3.7254 | -41.6987 | 2024-11-08 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 179.8 |
| 684aeb24-e31a-3a9e-b1a4-133ed02788d0 | -3.1458 | -54.4859 | 2024-11-08 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6ab30af0-ee52-31bc-977e-63948accbc2a | -4.7018 | -46.4508 | 2024-11-08 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 5a18d355-e399-32c8-9129-4ee9588a3077 | -1.7331 | -54.153 | 2024-11-08 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a76c562c-b7bc-332f-8eeb-d968852cc40a | -3.9669 | -48.1716 | 2024-11-08 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| af24148d-2b7c-38cb-b5a6-89bccfb7816f | -4.316 | -45.6914 | 2024-11-08 00:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1e4e57ea-27b1-3b1f-802f-3fffd3c62c2e | -2.6214 | -51.7378 | 2024-11-08 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 585e6855-cabd-3faa-91b5-e69b5057f0a0 | -3.0884 | -45.7463 | 2024-11-08 00:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b5a2ad46-b327-3415-b9eb-6d397d5a61b3 | -3.7066 | -41.6997 | 2024-11-08 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| ebf21972-b74b-3d74-bec8-ff6fdc189d6a | -3.1458 | -54.4859 | 2024-11-08 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5516d107-a68b-3c64-8eeb-d3b392e404d8 | -3.7254 | -41.6987 | 2024-11-08 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 135.8 |
| e5f76ac6-806c-3f8a-bbb5-54224a2f390a | -3.5631 | -47.3847 | 2024-11-08 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 33960154-2980-3d03-bd49-b08a14f0876a | -1.3961 | -47.5103 | 2024-11-08 00:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 243.3 |
| 5a83fcbb-4f24-3fb4-83b7-a29c4e72b1db | -1.7331 | -54.1329 | 2024-11-08 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5b871ddc-74ff-3941-b269-66b3f652adde | -1.7331 | -54.153 | 2024-11-08 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| db59894f-21b0-38ad-bf16-f4d53f3b583d | -3.7068 | -41.6758 | 2024-11-08 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| ab4108bf-37eb-3000-a3e4-f04e10a6bdec | -1.3776 | -47.4888 | 2024-11-08 00:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 45453f68-34a4-3e2e-8ac2-351bfd5fa937 | -3.1642 | -54.4654 | 2024-11-08 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 53f77d67-dd5c-3df3-84a1-d1c3edd3517b | -3.7861 | -44.0162 | 2024-11-08 00:30:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 75b724d5-e08f-32a6-b214-3be7c6fe6434 | -5.082 | -47.9433 | 2024-11-08 00:30:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c2202346-0b6b-3294-8ded-0df893ff0512 | -2.6214 | -51.7378 | 2024-11-08 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e958a5d4-4356-3b64-a6f6-294053305117 | -4.316 | -45.6914 | 2024-11-08 00:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| bd69d254-4865-3fa1-914d-033cad33a85a | -3.967 | -48.15 | 2024-11-08 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 04024780-b066-3673-b793-df7b55b1e225 | -3.9854 | -48.1708 | 2024-11-08 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3319e8ca-cb01-3f86-b5e8-a297dea18736 | -3.1458 | -54.4659 | 2024-11-08 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c2d0fd9c-f71a-39f7-a165-7a50e39c9972 | -3.0884 | -45.7463 | 2024-11-08 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| da4bfd9e-62f6-36e7-b4e1-e4fb60bd1e3b | -3.7066 | -41.6997 | 2024-11-08 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 254829fc-b7c6-3ceb-b207-a5656157045b | -1.3776 | -47.5106 | 2024-11-08 00:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 186.9 |
| f8bcb1e7-c497-3328-98b2-72aa924db2b9 | -2.6764 | -51.8189 | 2024-11-08 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 70501473-e59f-3ab8-8263-0d42f32a85f8 | -1.3961 | -47.4885 | 2024-11-08 00:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 35ef04c6-7561-38ea-8ccb-efe574dc2eb1 | -2.6214 | -51.7585 | 2024-11-08 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6d2e1026-baa5-371d-b4e2-b765638e8f98 | -4.2974 | -45.6924 | 2024-11-08 00:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bb3ae432-7f2f-35e9-bd80-f739112ff906 | -3.1641 | -54.4854 | 2024-11-08 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| fdf345da-7efb-331b-ae43-00fb5a0f22d8 | -2.6948 | -51.8185 | 2024-11-08 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| dc7ac121-8590-3679-a473-fa9f78bce1a4 | -3.5632 | -47.3629 | 2024-11-08 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0b8d7c06-122f-3e07-8960-33762a9298b9 | -3.0698 | -45.747 | 2024-11-08 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 48433b08-42cf-3f33-9d88-d39daff212f1 | -2.6228 | -51.3038 | 2024-11-08 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 75fb44ba-bc92-377f-b23c-fab07b02f2f3 | -9.9116 | -36.2634 | 2024-11-08 00:30:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| 387573fb-b84a-3a82-b292-7e2db7e474cf | -3.9669 | -48.1716 | 2024-11-08 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 0ad2f2e4-63be-3b35-9609-924efd928ee9 | -3.7255 | -41.6748 | 2024-11-08 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 138.9 |
| e1272cab-5304-37ac-bda1-9592ad9c58b3 | -3.5447 | -47.3636 | 2024-11-08 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 0bc33719-e427-3c0f-a20e-fd4ba52618a5 | -3.5446 | -47.3855 | 2024-11-08 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| eb21474f-da84-37a4-9327-69f8f138d407 | -2.82 | -52.9613 | 2024-11-08 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 9b0817d8-e7fc-3682-9b85-ae968f435bd5 | -3.1458 | -54.4859 | 2024-11-08 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 74cc5b81-51dc-39cc-9c05-d88e6f96c2eb | -2.6214 | -51.7378 | 2024-11-08 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 45244554-4f91-3b6a-8c72-1761c1785752 | -2.6764 | -51.8189 | 2024-11-08 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f4941473-8e63-339d-917a-b6b18b8417f5 | -4.316 | -45.6914 | 2024-11-08 00:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 12c5f3eb-759b-3cce-9a1e-2406517b9ba2 | -6.2642 | -39.3546 | 2024-11-08 00:40:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 76.3 |
| e7fcea55-845d-3fac-8d77-b4ec12243db5 | -4.2974 | -45.6924 | 2024-11-08 00:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 75b1a2cf-d5e2-3d2b-aa6d-670836dfc18b | -3.4838 | -52.617 | 2024-11-08 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 24593fd8-c5b9-3e9b-8659-f039b29febbe | -2.7832 | -52.9418 | 2024-11-08 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d8368003-ba9d-3e1b-9adf-3657d8e21789 | -2.6228 | -51.3038 | 2024-11-08 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f2d49b19-d8e8-3d43-9d08-ae67d849a2e2 | -2.8016 | -52.9414 | 2024-11-08 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 308.5 |
| fa0a12a9-ae43-3b6e-8efb-74a54cfa840c | -1.3961 | -47.4885 | 2024-11-08 00:40:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| dbf3cffb-bbe8-3097-9bc8-ff897dfbaf6e | -3.967 | -48.15 | 2024-11-08 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| bc38dac7-468d-3f51-82f9-bf2a6f2810f5 | -2.8016 | -52.9617 | 2024-11-08 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 4d4937ae-662d-3c5e-a891-5d884f202859 | -1.3961 | -47.5103 | 2024-11-08 00:40:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 93942939-5b73-307d-89ed-6f7573dac816 | -3.7066 | -41.6997 | 2024-11-08 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 752ab892-2041-3127-9426-d4f15dd7e0a2 | -3.7255 | -41.6748 | 2024-11-08 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 7c4e6a10-08bc-34e5-9ec1-c9b54a1ac8b8 | -3.5632 | -47.3629 | 2024-11-08 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 4d862858-c46e-3f8f-9064-85ea2b2a1104 | -6.264 | -39.3797 | 2024-11-08 00:40:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 073e681d-f702-371d-8775-e716211506f1 | -3.9669 | -48.1716 | 2024-11-08 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 7147e7ea-5664-32db-b49b-a1f3c4d8634c | -3.3388 | -44.0139 | 2024-11-08 00:40:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| ed48903d-7742-36da-a3ee-40ebf3dd2166 | -3.5631 | -47.3847 | 2024-11-08 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| cf1970a5-060a-3ee9-b743-b5a9795a3292 | -1.3776 | -47.4888 | 2024-11-08 00:40:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| ec57caec-fa1f-3781-8fea-af41c5f69aa4 | -2.8017 | -52.921 | 2024-11-08 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| edfa57ac-1731-309a-8a4b-08275b43fb41 | -3.5446 | -47.3855 | 2024-11-08 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 7abba527-2f28-3a12-b63e-fea830d572e7 | -2.6214 | -51.7585 | 2024-11-08 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| cea82da0-945e-3bd2-b1be-1ef02cadceb0 | -3.0698 | -45.747 | 2024-11-08 00:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 122.6 |


[Clique aqui para ver as próximas entradas](README6.md)
