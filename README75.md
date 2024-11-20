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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a01e5e9-787c-3ccb-9818-94eecc96ea35 | -2.92631 | -53.05129 | 2024-11-20 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 6a5eebed-3693-3765-9056-aa7dd3b6cb51 | -6.9421 | -41.1859 | 2024-11-20 06:20:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 44.9 |
| ce283d5b-f392-37f2-9ef1-768e56cc15ad | -2.9116 | -53.0606 | 2024-11-20 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 6465c958-be24-34fb-942d-b1eb8285219b | -2.7218 | -49.3295 | 2024-11-20 06:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| b4df9d89-c1ec-3c44-8cc4-08358fb94cb2 | -2.7217 | -49.3508 | 2024-11-20 06:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c35731ba-e225-30ce-8b71-87639b9d39ad | -6.9233 | -41.1879 | 2024-11-20 06:20:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 38.9 |
| ed8396a7-d840-37e6-8883-8b3770877d67 | -2.9115 | -53.0809 | 2024-11-20 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c2af8474-b59b-358d-aa84-1a0e76bfbf43 | -2.9299 | -53.0805 | 2024-11-20 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| cf99c7a3-3e36-3898-81cb-7c7b76129414 | -2.93 | -53.0601 | 2024-11-20 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 12210cc3-92f8-3b5a-b772-ab9cdb1d204a | -11.10571 | -54.62929 | 2024-11-20 06:20:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5ea9a474-b985-3dc1-a790-9781ba174d2d | -11.09283 | -54.62749 | 2024-11-20 06:20:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| aadecab1-c938-3db3-a0a2-a62aa5f35068 | -11.09538 | -54.60715 | 2024-11-20 06:20:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b24078ba-38f0-338e-92e1-7da71195298b | -11.10828 | -54.60897 | 2024-11-20 06:20:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 35d3e103-7cd9-3f2a-b291-b9fd5d13ecef | -17.12316 | -57.49454 | 2024-11-20 06:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| d5dcd578-da3d-3992-ac3f-a481f08ea60b | -2.9115 | -53.0809 | 2024-11-20 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bd024cba-ff5b-3dd2-bebd-75497211ec9e | -2.93 | -53.0601 | 2024-11-20 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 6e37001f-f7a9-3ff2-8861-46dba892c8a3 | -2.7217 | -49.3508 | 2024-11-20 06:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 56b9765a-a89c-3556-b147-244b839e24ea | -3.2951 | -53.8395 | 2024-11-20 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 97da12c8-4d18-3ac4-bea4-b2d3724bde1e | -2.7218 | -49.3295 | 2024-11-20 06:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 249d9baa-b55d-3ad0-82c1-64d4a3cecd87 | -2.9299 | -53.0805 | 2024-11-20 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| a764e494-bc51-33e2-92f5-4955cc4f68f0 | -2.9116 | -53.0606 | 2024-11-20 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 39c60d33-0c39-37eb-bc9c-6e14c8fe1301 | -3.2951 | -53.8395 | 2024-11-20 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bf59412b-205f-3362-8210-a40349b75f26 | -3.9288 | -45.0807 | 2024-11-20 06:40:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2f78ee44-ce62-394f-bf21-0a1c6d53564a | -2.7217 | -49.3508 | 2024-11-20 06:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 075fa1b9-a9a6-30df-aa8b-f857ed99f53c | -3.9287 | -45.1033 | 2024-11-20 06:40:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8c6aa496-9525-36b8-befa-3df2eb41574c | -2.9115 | -53.0809 | 2024-11-20 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 089eb75e-90a0-3a39-80a7-fb22a5446b86 | -2.7218 | -49.3295 | 2024-11-20 06:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 87c42c88-e2e4-3472-aa64-6725ad554868 | -2.9299 | -53.0805 | 2024-11-20 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ef749594-b22c-37d5-a2f1-0cfba123933f | -2.93 | -53.0601 | 2024-11-20 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a13230a4-05ec-352d-9bcb-9c22f2e30812 | -2.9116 | -53.0606 | 2024-11-20 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3ab41c8e-a73b-3cfa-bb22-2fcb9c052c39 | -2.9299 | -53.0805 | 2024-11-20 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| efbc8102-7503-3a1b-9d97-f50fafc34f24 | -2.9116 | -53.0606 | 2024-11-20 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| dcb04ff2-662d-366b-a01a-e59a2a171a73 | -2.7217 | -49.3508 | 2024-11-20 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 71f94329-19d4-3f84-8e37-1f0fbdf97b5a | -2.93 | -53.0601 | 2024-11-20 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 753a582a-3522-3bad-acbd-499438801691 | -2.9115 | -53.0809 | 2024-11-20 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2d518644-8ae9-3ca7-994a-93d22dabc5fa | -2.9115 | -53.0809 | 2024-11-20 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 85e72db0-becc-36bc-9293-5742bf272f04 | -3.1466 | -45.2278 | 2024-11-20 07:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 63472d95-1032-38c7-901e-6e18639dcb89 | -2.9299 | -53.0805 | 2024-11-20 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c8f2c6f0-fe29-3258-931a-369ac78d940d | -3.994 | -43.5671 | 2024-11-20 07:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 61e6f0f3-e0e0-3966-8b28-d0bbdd255282 | -2.93 | -53.0601 | 2024-11-20 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d8c771c1-04a0-33ec-9cda-1d68a6b08b51 | -3.9942 | -43.5439 | 2024-11-20 07:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| da88575c-3705-3283-88dd-5b72afaa6769 | -2.7217 | -49.3508 | 2024-11-20 07:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 62fede5a-9144-377a-85fb-6d31f4ebf168 | -2.9116 | -53.0606 | 2024-11-20 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 88678634-31fd-35ad-85f5-6aa84608ebdb | -3.1465 | -45.2504 | 2024-11-20 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 0bd1aed8-af6d-35da-8f8a-7b82b9e8155b | -2.9116 | -53.0606 | 2024-11-20 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f54e9eef-c0e1-35ba-bddd-d0d926080d7a | -3.1466 | -45.2278 | 2024-11-20 07:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 151.0 |
| fff914ed-4425-3304-bd4d-9b630df4eaca | -2.9299 | -53.0805 | 2024-11-20 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c2e473d4-cff0-3301-93c1-4cf76992a829 | -2.93 | -53.0601 | 2024-11-20 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c81704fa-257b-3ce7-b769-56cdfd5b0773 | -2.9115 | -53.0809 | 2024-11-20 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c46e25b6-fc40-36d5-8698-cbe3070b2017 | -2.9299 | -53.0805 | 2024-11-20 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a99fd339-e544-3434-9552-aa58481099b2 | -3.1466 | -45.2278 | 2024-11-20 07:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 9bc20617-44e9-361f-848e-2edc9fed79d1 | -3.9078 | -42.4256 | 2024-11-20 07:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| b73326be-356b-3ef9-8cd7-735aa878120e | -2.9115 | -53.0809 | 2024-11-20 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a7010cb8-5144-38d8-8f2e-fd0995b20040 | -2.93 | -53.0601 | 2024-11-20 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 80c57d73-a14f-31ac-8aaf-488803a68d32 | -2.9116 | -53.0606 | 2024-11-20 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 87667dc7-c90c-3ec1-a940-9611984dc481 | -3.1465 | -45.2504 | 2024-11-20 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 1388bc09-395c-3a53-8623-535723b9a598 | -3.9078 | -42.4256 | 2024-11-20 07:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| de464552-0635-3484-96e9-de0bd7769f1c | -3.1466 | -45.2278 | 2024-11-20 07:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 253b9317-66ee-37c9-8e15-2dd5f59050c6 | -3.1465 | -45.2504 | 2024-11-20 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c6af4009-686b-3d1d-943f-4a331e3ee66b | -2.9299 | -53.0805 | 2024-11-20 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3c6d8062-6e4b-36e4-956d-2b6a1c222c15 | -2.93 | -53.0601 | 2024-11-20 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 50981f03-6850-3eab-b851-7c5ee1cdde53 | -3.9265 | -42.4246 | 2024-11-20 07:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 97c35b82-8fa1-3841-9ac6-43ce5ebecbd2 | -2.9116 | -53.0606 | 2024-11-20 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c2ef5f2e-8d2a-35e1-98f6-01344b5d14ea | -2.9115 | -53.0809 | 2024-11-20 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 84a1faef-ae3b-368c-8eb1-3998108d2300 | -2.9116 | -53.0606 | 2024-11-20 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e10ca82a-0d9b-3015-bcd9-4cdbda8303f6 | -3.9265 | -42.4246 | 2024-11-20 07:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 68bb6d8e-49b4-3cd9-a327-65e3a92c12c0 | -3.9078 | -42.4256 | 2024-11-20 07:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| b905e31e-b3e7-3a6f-b8d8-076182353d25 | -3.908 | -42.402 | 2024-11-20 07:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 477dd6bd-c0c1-3fb2-84b4-1ed624fa0cc6 | -2.9299 | -53.0805 | 2024-11-20 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 38049c68-ed04-3aef-988c-904ab0698233 | -3.1466 | -45.2278 | 2024-11-20 07:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 2cdc5b81-4a0f-302a-b18e-830d9e1185f6 | -3.2767 | -53.84 | 2024-11-20 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 6ad0d606-f1c3-3210-a7b9-6e41c701aceb | -3.1652 | -45.2271 | 2024-11-20 07:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| aad53b77-7aea-3a9d-a2b2-a539c2021539 | -2.93 | -53.0601 | 2024-11-20 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 103eeacc-47a8-302b-81c8-4e4ef358f3ad | -3.2767 | -53.84 | 2024-11-20 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 4e8e713e-019f-3a45-b61e-ca670adf008c | -2.9116 | -53.0606 | 2024-11-20 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 585eaba5-c597-3514-931a-b39dcfe46e2c | -3.1652 | -45.2271 | 2024-11-20 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 0875cdec-ca05-3351-94c4-c6b89550cf4b | -2.9115 | -53.0809 | 2024-11-20 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f3387840-a4fc-3b2d-802c-35fbfe0137da | -3.2024 | -45.2256 | 2024-11-20 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0d670e60-a3e6-38e1-9c7f-f9628de34191 | -3.1653 | -45.2046 | 2024-11-20 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 28540623-49a0-3846-9677-dacae90aaabb | -2.93 | -53.0601 | 2024-11-20 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 70f28aa1-a48b-3678-a4ef-a18eea8edf1f | -3.1466 | -45.2278 | 2024-11-20 07:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 299d31a0-8b62-38b1-a2dd-ab559971d924 | -2.7573 | -44.9711 | 2024-11-20 07:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 93a1a8b0-ec8c-3eda-bfe8-a89b0801f7f1 | -2.9299 | -53.0805 | 2024-11-20 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5a5f3757-3818-31e6-b390-9540ac75858c | -2.9299 | -53.0805 | 2024-11-20 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| de1cf974-64e4-3658-b6c5-16105a3c9fba | -2.9115 | -53.0809 | 2024-11-20 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| abc1ad29-eee1-3f3f-8a25-079534ab8816 | -3.0353 | -45.1644 | 2024-11-20 08:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| dcfe77d0-a750-3bf0-a01c-e91bc0d532a9 | -3.2024 | -45.2256 | 2024-11-20 08:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 70a13e38-04a3-32b6-a636-549429a4c432 | -3.1652 | -45.2271 | 2024-11-20 08:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 110030b9-04b7-39c8-a246-e06f6273ec0d | -3.2767 | -53.84 | 2024-11-20 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 6d6f30cf-8aca-3376-8ad1-5ba3392ab55e | -2.93 | -53.0601 | 2024-11-20 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 61199cb4-9113-365d-9c71-7f8b3970ceab | -2.9116 | -53.0606 | 2024-11-20 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 45779acf-0bee-3313-a5bb-80342aa26cdf | -3.0354 | -45.1419 | 2024-11-20 08:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 483e862a-9602-341b-b59f-fa4ae0ddb1b8 | -2.9115 | -53.0809 | 2024-11-20 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 55f20880-4f93-377b-a9f2-0f00c711cdd0 | -2.9116 | -53.0606 | 2024-11-20 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7cd80c92-21bc-3da0-ae0d-fa8473ae73e4 | -2.9299 | -53.0805 | 2024-11-20 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| b2aceed8-ac13-3d92-a656-f4cd97a10ffb | -2.93 | -53.0601 | 2024-11-20 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| e8b4ac9f-d615-32d8-81af-a54a259341ea | -2.93 | -53.0601 | 2024-11-20 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a9e8d4dd-6cfe-3f6b-a270-160098219221 | -2.9116 | -53.0606 | 2024-11-20 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5b0c9063-74ee-3b2d-bed5-d8bae4e67c11 | -2.9299 | -53.0805 | 2024-11-20 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5e37f08c-6c93-3521-8350-9e9398bb4794 | -2.9115 | -53.0809 | 2024-11-20 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |


[Clique aqui para ver as próximas entradas](README76.md)
