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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02ad2008-03b8-3690-a52c-3af4c7994120 | -1.347 | -54.609798 | 2024-10-27 01:10:49 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4df60bc-b29c-3f17-8b63-a5c25454e293 | -1.5958 | -55.694599 | 2024-10-27 01:10:49 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3437c4a8-86b0-3b27-b288-c47f85d1b57a | -1.5974 | -55.7015 | 2024-10-27 01:10:49 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1887aff1-207f-30b5-9da5-3e79110a4a26 | -1.3419 | -54.632401 | 2024-10-27 01:10:50 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a231fdd3-2fa1-3892-9fdc-7d5c74d440ea | -1.3435 | -54.639198 | 2024-10-27 01:10:50 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab397c4-e80b-3a84-9e64-5e9a0896712e | -1.4221 | -55.0718 | 2024-10-27 01:10:50 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca2e809-a75a-3fb9-b4fb-f81f2f19cb7f | -1.17 | -53.8843 | 2024-10-27 01:10:50 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a01cbc8-9e5e-3471-8094-a5f4117f41ba | -1.1716 | -53.8913 | 2024-10-27 01:10:50 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21a4ac0-e594-3052-a6de-89970d51734b | -1.1732 | -53.898201 | 2024-10-27 01:10:50 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42408878-4a27-35a3-ad8c-1874fea14f57 | -1.3403 | -54.625599 | 2024-10-27 01:10:50 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67fcf8a9-0314-345c-8a21-b046125b249d | -1.1212 | -54.1208 | 2024-10-27 01:10:51 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6b65a2b-b0ca-3c5d-841c-95845526ec6b | -1.1228 | -54.127701 | 2024-10-27 01:10:51 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a13f094f-c6cc-3eca-b1f9-0d0b646a6b14 | -1.1114 | -54.123001 | 2024-10-27 01:10:51 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5d33614-cdca-3657-8f09-c6586c36eaed | -1.113 | -54.129902 | 2024-10-27 01:10:51 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e87fd5af-c744-34cc-bfa2-a67dd6b884f7 | -0.9878 | -53.675201 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9373920a-7cde-3d2f-9ee9-d5d9a4119545 | -0.9894 | -53.682301 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45449ceb-e648-36f1-b7ac-0f2693ccc8ef | -0.9911 | -53.689301 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbc10c76-dad1-35eb-b72d-5150cbad8c18 | -0.9927 | -53.696301 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3294db58-c907-33e1-9410-3dd7e164731c | -0.9943 | -53.7033 | 2024-10-27 01:10:52 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8820ca89-8b33-3024-aeb7-1b038c74acb2 | -0.978 | -53.677399 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b7d43e5-8c72-3f20-b140-3e7fcd5a9877 | -0.9796 | -53.684502 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e21d65b-77ee-3bc6-bfec-7f37903e3c82 | -0.9813 | -53.691502 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf35234-578b-3a8c-bdba-efdfbebfdf2f | -0.9829 | -53.698502 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1008725-e6b1-3b5a-82d4-432eae4a8344 | -0.9845 | -53.705502 | 2024-10-27 01:10:52 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b80a3a9c-4a07-39fa-983e-cf2cd6108ea4 | -0.9861 | -53.712601 | 2024-10-27 01:10:52 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f89b537-1a43-3e60-ad22-d92ba5347f6d | -1.3716 | -55.391102 | 2024-10-27 01:10:52 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 602c5085-275d-3406-9d6c-4fb1503b784c | -0.9715 | -53.693699 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5e3350-f44e-3494-9d93-d2dc2c5ddfa6 | -0.9731 | -53.700699 | 2024-10-27 01:10:52 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90c7f008-a5e8-36c0-8897-50bc2d570bf1 | -1.2889 | -55.705002 | 2024-10-27 01:10:54 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd0096da-be7c-363d-ad75-6e9e3b43d491 | -1.2904 | -55.711899 | 2024-10-27 01:10:54 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c78406ce-77dd-3248-bb0c-0e2110335e64 | -1.292 | -55.7188 | 2024-10-27 01:10:54 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7691aa9c-f546-3d3e-9fe1-fb8cf9db69da | -0.111 | -51.6129 | 2024-10-27 01:10:58 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 79cdc287-3a4c-3870-abac-5becfca5a45c | -0.113 | -51.621498 | 2024-10-27 01:10:58 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 279b901c-1b11-338e-8306-7f925c36d2cd | -1.9102 | -59.963402 | 2024-10-27 01:11:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab89e2de-f439-3011-900f-4233bfc99cb1 | -1.9127 | -59.974201 | 2024-10-27 01:11:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df619b78-3ba5-3793-b290-a5373f96edba | -1.9151 | -59.985001 | 2024-10-27 01:11:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4cb89b-fbb5-3768-8473-8cab866b9784 | -1.9029 | -59.976398 | 2024-10-27 01:11:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4891857-246b-3f81-9bfb-a1c81330ced6 | 0.3238 | -50.930199 | 2024-10-27 01:11:03 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9de88bcd-6b52-32ed-880f-3847754060b5 | 1.7779 | -50.461201 | 2024-10-27 01:11:25 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b9a02cfc-bebe-3038-9e51-002d5a3ddb95 | 1.9173 | -50.841801 | 2024-10-27 01:11:28 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf2417a-8c1f-3e61-aad0-bfeea9981d02 | 3.4349 | -51.2621 | 2024-10-27 01:11:54 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f01d888d-c856-32a2-947e-4a4002ea9c36 | 3.3988 | -51.285702 | 2024-10-27 01:11:54 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0d1107cd-a60d-3f82-82b6-68de9bdc8b3a | 3.3965 | -51.2957 | 2024-10-27 01:11:54 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| de0782d6-2b34-3b7f-8068-b1c561d3166a | 2.3078 | -61.3265 | 2024-10-27 01:12:14 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5defc0c3-7ab4-3fb3-8f73-89ccf1d89715 | 4.328 | -60.445202 | 2024-10-27 01:12:43 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd8e7ab-f4ee-3c66-88f9-557e18f7ca74 | 4.9382 | -60.263599 | 2024-10-27 01:12:52 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8db688-afc4-3fa4-b8ee-a2ab073eb562 | 4.9361 | -60.272701 | 2024-10-27 01:12:52 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c04f7f47-9f3e-3b02-a456-ff7cf8f506fc | -0.9815 | -53.7192 | 2024-10-27 01:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0d4ced12-ac65-3794-8dd4-0695718ab52c | -0.9815 | -53.699 | 2024-10-27 01:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 249.7 |
| 85026f3b-f7f4-3570-bb61-e71bcfc2ded7 | -0.9815 | -53.6789 | 2024-10-27 01:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 61a16cea-4eef-3474-b780-d4d051d0aced | -0.9998 | -53.719 | 2024-10-27 01:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4b8b7ce9-b2a7-3136-91bd-4a7a01ecc3aa | -0.9998 | -53.6989 | 2024-10-27 01:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 602ead0d-311e-3afe-a5e4-03d9ff2d12a9 | -0.9999 | -53.6788 | 2024-10-27 01:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c7c6830f-89b0-3255-8adf-fe3f71e1cc87 | -1.1831 | -53.8985 | 2024-10-27 01:15:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| baa32392-34b7-3b1e-b086-c604470f3840 | -1.7874 | -46.4065 | 2024-10-27 01:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| e0ea159e-96c4-3900-9fd2-3ab854ed23b0 | -1.7875 | -46.3844 | 2024-10-27 01:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 00f776a8-d171-3536-8e69-879e03e74039 | -1.8059 | -46.4062 | 2024-10-27 01:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| fc65eac3-a696-3f25-a1b8-da46c8c23b1d | -1.806 | -46.384 | 2024-10-27 01:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5d95f77b-ce13-3c7f-9f54-6aa41f7433b5 | -2.4567 | -45.8567 | 2024-10-27 01:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 14d3024e-b951-3a19-bf3f-83ae9861bbba | -2.4568 | -45.8344 | 2024-10-27 01:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b1d652ef-5a50-36f4-b97d-5317684c15d9 | -2.4598 | -50.412 | 2024-10-27 01:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ee6c9fcb-21c4-3750-b465-0f4266a13602 | -2.4753 | -45.8561 | 2024-10-27 01:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 9f20eb62-ddff-3ec5-9331-d1a3ea4bcee2 | -2.4753 | -45.8338 | 2024-10-27 01:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 161.7 |
| a4184dda-0f9a-389a-8e9a-5fda8e601773 | -2.4786 | -50.2858 | 2024-10-27 01:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 86ad9805-298e-33a7-9a09-8c56f731c67b | -2.486 | -48.0507 | 2024-10-27 01:15:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| e7eea648-a29a-31d5-b4b1-00c2fd132c43 | -2.5045 | -48.0502 | 2024-10-27 01:15:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 32bb891b-b0d8-3617-a0fd-1208f023efda | -2.6297 | -49.247 | 2024-10-27 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d0070d6a-990e-3ef3-b489-868b455fe19c | -2.6321 | -54.2975 | 2024-10-27 01:15:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c04e4239-fb9b-301d-b680-d107758e3b1c | -2.7033 | -49.33 | 2024-10-27 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c4135e70-4407-3aab-8c4f-0df1f252fa34 | -2.7034 | -49.3088 | 2024-10-27 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 2a4b3e78-8a28-3196-a9a1-0dc2c6c06044 | -2.8145 | -49.2418 | 2024-10-27 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1153628a-5553-370f-9c60-9cb1113d8d4b | -2.8329 | -49.2626 | 2024-10-27 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c3c65897-9b92-3313-92e4-11a32dcab95a | -2.833 | -49.2413 | 2024-10-27 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| dddb33b7-6b6e-3775-bbe3-ec1faf6a9c11 | -2.8397 | -52.5532 | 2024-10-27 01:15:21 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ff73d3b4-33aa-3d8f-a6d3-b477a77fa199 | -2.8515 | -49.2408 | 2024-10-27 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c1b5bd0e-2097-3d7f-b0fc-5ff7e4af8b93 | -2.8687 | -45.0125 | 2024-10-27 01:15:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0820428d-1175-3077-b8ca-f5bb2640ea7f | -2.8688 | -44.9899 | 2024-10-27 01:15:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 5d0aa300-7791-3f9b-b4f2-a8c230fd2431 | -2.916 | -51.7716 | 2024-10-27 01:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c695d4cb-78d8-378a-a09a-c7f9ea65ba65 | -2.9161 | -51.751 | 2024-10-27 01:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| d9ba16b6-4b2e-37e1-8f7c-2653e4333c9a | -2.9214 | -50.295 | 2024-10-27 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| cdee00cf-27ed-37a4-b71b-1d2b68615476 | -2.9215 | -50.274 | 2024-10-27 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 4851c746-6984-3153-8ec5-5d7aa93a8fba | -2.9345 | -51.7711 | 2024-10-27 01:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 0b500264-6571-3d78-88dd-b9bf8d3510e7 | -2.9345 | -51.7505 | 2024-10-27 01:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| bc0cc06e-749b-311d-9fff-530a0ecb7ef4 | -2.9399 | -50.2735 | 2024-10-27 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f3fbd441-83a3-3b6f-a2fb-8a9c9d2b1bdd | -2.9669 | -53.0389 | 2024-10-27 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c9139440-ea17-3be1-8a67-cfdc1ad4fe91 | -3.1106 | -44.9809 | 2024-10-27 01:15:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| db6ec24a-0692-3c4b-b4c9-2e2a3d774d24 | -3.1292 | -44.9801 | 2024-10-27 01:15:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4ef8fc50-5fbf-37c1-8635-528a4dcb220a | -3.1242 | -50.3519 | 2024-10-27 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 62e879af-43d5-339b-b938-71aab5ae7b35 | -3.3256 | -50.7641 | 2024-10-27 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 73841213-ebba-3bca-8d64-cd6556d48497 | -3.344 | -50.7635 | 2024-10-27 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 894df64c-66b2-33ef-a9d6-ad894efa62b5 | -3.3441 | -50.7426 | 2024-10-27 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4a3d314a-60fb-3fd8-a37d-b2e7959f9c1b | -3.4392 | -50.0896 | 2024-10-27 01:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f3608063-ba95-3104-956b-44267ceee3b5 | -3.4762 | -54.5772 | 2024-10-27 01:15:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 23666992-86a8-3932-85fc-f02b97e55e65 | -3.5202 | -52.7384 | 2024-10-27 01:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| fd40e033-969a-31f0-a810-cd392df88e44 | -3.5626 | -51.4217 | 2024-10-27 01:15:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 4e99f448-7b98-31ee-9aee-b10b7ad54494 | -3.6798 | -54.2107 | 2024-10-27 01:15:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2175b33c-9682-30d4-9250-7c3d17cb0d3e | -4.2799 | -45.5138 | 2024-10-27 01:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7fec2f60-6acf-3b3f-9e20-1743f48c1a26 | -6.1674 | -47.2638 | 2024-10-27 01:15:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4955d803-cac1-3b06-a432-0ca1691f8324 | -7.2452 | -46.0482 | 2024-10-27 01:15:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 91e3b869-48a7-325a-ab80-ce12ef0833af | -10.5424 | -45.1463 | 2024-10-27 01:16:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |


[Clique aqui para ver as próximas entradas](README21.md)
