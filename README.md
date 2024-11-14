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
| 92907bd4-912f-34fa-bdf4-f7ce79606f35 | -3.8021 | -47.7887 | 2024-11-14 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c968cdab-fb28-3418-9df4-a82504a1cffa | -2.5448 | -47.1356 | 2024-11-14 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a5898af3-734c-3484-b0cf-76d5ca65184a | -3.4198 | -50.3215 | 2024-11-14 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| abdd29f2-6c50-32e3-be32-ad86edaf052e | -3.8206 | -47.7879 | 2024-11-14 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 26b40492-4081-38c8-aee6-d216a2126fc4 | -2.5448 | -47.1137 | 2024-11-14 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| b1e4cddc-3c9d-3971-b399-cb004583cc49 | -3.4198 | -50.3005 | 2024-11-14 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| bbe144f9-ff4b-3b3b-aa9e-99e357718a0e | -4.145 | -46.2578 | 2024-11-14 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5b8d6d9b-a05d-3fad-89e4-5fe8917ba4c2 | -3.4014 | -50.3011 | 2024-11-14 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| adeddaf8-7079-32b1-afe5-81eb078a7ecb | -2.7177 | -45.5803 | 2024-11-14 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1c2d2b43-b9f2-34cd-881d-315c6ae7f0b2 | -4.0005 | -45.5503 | 2024-11-14 00:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 8314089f-4cba-3d0e-97a1-097b0c207fff | 1.2852 | -60.4454 | 2024-11-14 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b8780832-dbc6-32b4-834d-aa7ccf117f89 | -1.369 | -52.3558 | 2024-11-14 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6a6d3502-1b67-3755-8096-417f3d21b85a | -2.0268 | -46.9299 | 2024-11-14 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 3ff09d1f-a9c5-322b-a081-47bd559e06c3 | -4.3755 | -48.0665 | 2024-11-14 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 57946f41-ede9-3685-aedc-684e32a40b11 | -2.6992 | -45.5585 | 2024-11-14 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| dffeb9a2-e496-3519-8c8e-e390b7d2496c | -2.675 | -47.0003 | 2024-11-14 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| c02b65a7-4767-3891-85ac-52d676b7e97c | -1.4078 | -51.1195 | 2024-11-14 00:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 96462fbd-1eb3-3462-8630-98c90c303437 | 1.048 | -60.5986 | 2024-11-14 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ea8bc20e-b508-35eb-8d66-c90c8f79d06b | -3.802 | -47.8104 | 2024-11-14 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9bbb9eee-7c48-3066-a18a-1b71facc27d9 | -2.8791 | -51.7932 | 2024-11-14 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 7e22df56-4c9e-3b47-9989-105e303cb4c7 | -1.3874 | -52.3555 | 2024-11-14 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 4ece11fa-7508-30e6-848f-8d81316b0a2c | -17.2543 | -57.4698 | 2024-11-14 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| c668812d-78cb-38e9-a5e5-cada7db70c61 | -9.9502 | -36.2566 | 2024-11-14 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| f96f4621-3598-3f04-8855-e1d24409b6ef | -4.3754 | -48.0882 | 2024-11-14 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0eb40e2e-445c-3203-8c83-c83b812843a2 | -3.1244 | -50.31 | 2024-11-14 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1498d834-2571-3901-8849-389fd622f82c | -4.0191 | -45.5494 | 2024-11-14 00:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 06114216-74aa-32e7-8872-668eeb25f1e2 | -6.0472 | -44.0331 | 2024-11-14 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8b9ca4eb-1472-300d-ae79-3d000e66c1e0 | -4.1451 | -46.2356 | 2024-11-14 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4e820f53-a0f0-3e2e-876c-2077cc79fd17 | -2.2113 | -53.7231 | 2024-11-14 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 27bdc17a-4c8a-3f8b-83fa-18ff8d2f4457 | -9.9889 | -36.2497 | 2024-11-14 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 198.2 |
| 65cc5c3e-fae4-3bb1-a45f-f199d4107a63 | -9.9884 | -36.2768 | 2024-11-14 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| e8487175-dac2-3201-ab79-1fe9afabbe86 | -3.0504 | -50.3332 | 2024-11-14 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0c951749-1de6-3ce7-a8a9-b37995fd8a70 | -3.1649 | -45.2947 | 2024-11-14 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 068070ff-f530-3f48-bad0-eb6c9008476e | -1.2228 | -51.7625 | 2024-11-14 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 4c9cec42-a6e0-3963-8c4f-008f0f2305a5 | -1.3895 | -51.099 | 2024-11-14 00:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ba64e917-3cb2-366c-b49e-d0c3d68a0d19 | -4.5614 | -48.0141 | 2024-11-14 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3e18f4ed-01d7-3892-bcd9-873317214674 | -1.3894 | -51.1197 | 2024-11-14 00:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| ef597f4a-0523-3e79-8f4c-1b67c5ec2ef7 | -3.1463 | -45.2954 | 2024-11-14 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 8e5c6e37-25ed-3d7e-8e43-d6269ecb279b | -4.1636 | -46.2569 | 2024-11-14 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 837af8e7-4c45-3e26-ad7f-4b2af83c9a6c | -2.7178 | -45.5579 | 2024-11-14 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f1e9f87d-5ecd-38c4-be27-b47f6c0d50e3 | -4.3362 | -45.4434 | 2024-11-14 00:00:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1bd135a9-cd2d-30fc-8b32-cdc614839ddb | -2.3159 | -49.1912 | 2024-11-14 00:00:00 | GOES-16 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 79d18a18-140d-3702-b06d-d16c055c8a6d | -3.0522 | -45.5461 | 2024-11-14 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2968517f-12e8-3c9c-a4b6-0828c237a250 | -2.6751 | -46.9783 | 2024-11-14 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| fdd1f617-cfa2-34ac-8194-333aae889139 | -2.6991 | -45.5809 | 2024-11-14 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| cbcd3474-277f-3155-aaf8-6d9b593f7a03 | -9.9691 | -36.2802 | 2024-11-14 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 150.2 |
| 35c42e0a-5e92-3f9c-a371-d6b9f83eb2d4 | -2.641 | -46.1849 | 2024-11-14 00:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| ddd7432f-586c-34b6-a20b-6d2beae4e5b4 | -2.6411 | -46.1627 | 2024-11-14 00:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 38e1da67-e168-3b03-bf35-83e90e1ece29 | -4.0003 | -45.5728 | 2024-11-14 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 1d868508-4178-386c-9d26-9050d3c6faee | -2.8975 | -51.7927 | 2024-11-14 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 17c31d3b-b433-3c9a-9b63-3bf4d12f557e | -2.6565 | -46.9789 | 2024-11-14 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8f12f5ae-2902-31b4-8b6d-967966982c06 | 1.0663 | -60.5985 | 2024-11-14 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 2ddb588a-5334-3f1b-8414-a4d262a3abd9 | -3.5194 | -52.9218 | 2024-11-14 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b8fc7dcb-a55f-321a-8639-9c148f54d04c | -3.271 | -50.5778 | 2024-11-14 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 99c33c08-b542-3eab-8a19-82e866bc05d3 | -9.9696 | -36.2531 | 2024-11-14 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 386.8 |
| 94e3e6e0-73b7-3eb5-8990-2d39479a05a0 | -2.2297 | -53.7026 | 2024-11-14 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fddd1a94-47ce-328b-9d23-04bcc03bebf0 | -2.9774 | -45.6609 | 2024-11-14 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d2ac1115-427d-363b-a82d-839616486626 | -3.2916 | -50.0524 | 2024-11-14 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3e5c4c9e-6e76-30c2-8c7b-6e18c9d88777 | -2.0267 | -46.9519 | 2024-11-14 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e5a28bf2-bf49-37fc-82b9-b8d210e7afa5 | -9.9701 | -36.2261 | 2024-11-14 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| c4b3525c-e01c-339b-b866-04d9f1408f43 | 2.4341 | -60.6613 | 2024-11-14 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 712ee8ed-cdbe-320f-a4b2-0468a803d7cc | -3.1464 | -45.2729 | 2024-11-14 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 161.8 |
| ad46cf1b-3b12-3748-910a-b7df98e586c2 | 1.2852 | -60.4265 | 2024-11-14 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0b32824b-901a-389d-a220-616ad8638ed2 | -1.2228 | -51.783 | 2024-11-14 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 345afa6b-88fe-3c43-bd81-fae52962aba0 | -4.0189 | -45.5719 | 2024-11-14 00:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 8c404bf6-9da7-31e8-9360-9dafda3484bf | -3.1243 | -50.331 | 2024-11-14 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 36ed86fb-c5d8-3ccb-994b-833a1f7b707d | -3.0523 | -45.5237 | 2024-11-14 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 2e175b82-485b-3973-a2f1-4b6b30145923 | -2.2113 | -53.7029 | 2024-11-14 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 964258cc-9d12-3103-8d53-bbe18ef35226 | -3.165 | -45.2722 | 2024-11-14 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 2bbfa337-747b-3832-9383-c2e46d39ba14 | -2.6564 | -47.0008 | 2024-11-14 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 0c653571-267a-3074-ad6c-ca3b787aad03 | -2.0453 | -46.9295 | 2024-11-14 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5056ebc7-8cea-31a7-9337-26dbd179ca95 | -2.9773 | -45.6833 | 2024-11-14 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |
| b83a5ff1-a7af-3479-b5d9-74057e968896 | -9.97 | -36.23 | 2024-11-14 00:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3860db6b-9e20-3d45-b6cf-11cacea7b62e | -9.97 | -36.27 | 2024-11-14 00:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f2bf7c4-db2b-3a37-9b53-a74370bdbd2a | -4.0 | -45.56 | 2024-11-14 00:00:00 | MSG-03 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b118788-ce1d-3152-bff0-64b073dd0aca | -3.5194 | -52.9218 | 2024-11-14 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 215032df-17f7-3fa1-a439-58d76aafa9e1 | -4.0191 | -45.5494 | 2024-11-14 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 842416ff-71fe-33f4-859c-ed555ac2d3be | -2.5448 | -47.1137 | 2024-11-14 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 23d032db-78b5-3981-ad33-c97d52351cf7 | -4.5614 | -48.0141 | 2024-11-14 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7ff1d40a-ebb6-3a8a-8ff8-a000bd866d5b | -17.5672 | -57.5557 | 2024-11-14 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 430b9303-0b7a-3eb7-b406-35e7cc1d6aae | -4.0003 | -45.5728 | 2024-11-14 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 178.1 |
| d9385d85-53e7-33f2-800c-3d59c383d75c | -3.4326 | -43.8948 | 2024-11-14 00:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6c107bed-11af-3e40-80a4-7072553b684b | -1.369 | -52.3558 | 2024-11-14 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e379c931-7b24-3706-a648-41b653bb68bc | -2.641 | -46.1849 | 2024-11-14 00:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 22e55e3f-7754-333f-9528-10ab3fcaddf3 | -3.7517 | -50.4357 | 2024-11-14 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 13fa1740-bdb7-3179-816f-e9c5d5062aa6 | -1.4078 | -51.1195 | 2024-11-14 00:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 26741d15-f548-3cd6-839a-36115373ffea | -4.145 | -46.2578 | 2024-11-14 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 81b8445d-cd34-349e-991d-a01db73a6aaa | -2.2113 | -53.7029 | 2024-11-14 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b26fe141-f0ce-3535-b64d-18efa3a503ab | -17.6263 | -57.5486 | 2024-11-14 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| c36c16d4-cf43-319e-afb0-4f0e16660d91 | -2.6565 | -46.9789 | 2024-11-14 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 240d356d-67c2-391d-b823-d7c7030a5f0a | -17.7052 | -57.5392 | 2024-11-14 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 9d1e0ecb-e6c2-3a94-b16b-7a0a8b3ddc77 | -4.3754 | -48.0882 | 2024-11-14 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6cd6af06-fee8-39e9-84b4-c88221c620e9 | -3.0522 | -45.5461 | 2024-11-14 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 08bf814f-d905-39ea-9f59-0799372b005b | -4.1451 | -46.2356 | 2024-11-14 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| df894c61-8554-352b-b870-4a0f1bed642c | -4.0005 | -45.5503 | 2024-11-14 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 02665968-4ebf-38fe-9c60-51f90806e829 | -2.8791 | -51.7932 | 2024-11-14 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d87575dd-9584-3c88-a215-480d8b9355dd | -3.5195 | -52.9014 | 2024-11-14 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| bb4082e9-bb96-3881-9915-f7cdbd5fb60b | -6.0472 | -44.0331 | 2024-11-14 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 98a3d0f1-7038-3b14-8d4c-166d63db4556 | -4.0189 | -45.5719 | 2024-11-14 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 192.1 |
| 84b253e3-e979-392b-80bf-4a11a71b6a70 | -2.6564 | -47.0008 | 2024-11-14 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |


[Clique aqui para ver as próximas entradas](README2.md)
