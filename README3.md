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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb354d24-8f4c-3c8e-b143-3a7103d4c456 | -2.2169 | -45.4159 | 2025-12-12 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 224.5 |
| 6ee81632-d2f3-3432-a582-eb45a1e6537c | -3.6293 | -45.3878 | 2025-12-12 00:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a8ceed72-bd09-3b77-82c9-3e3effe76ebb | -12.4135 | -58.0292 | 2025-12-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 348.2 |
| 89920416-3d72-341b-aa70-51d5b6607ac8 | -3.9699 | -41.5176 | 2025-12-12 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 03717089-a556-3744-88c6-19b007e45dcb | -8.051 | -43.1237 | 2025-12-12 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| b5833c7a-1c02-3ccc-8c0d-0110362e8d93 | -8.0513 | -43.1001 | 2025-12-12 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 318.1 |
| 334a6d84-14d4-396d-80a0-53ad72b6cccd | -1.5337 | -52.7414 | 2025-12-12 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c831bee6-9436-3210-8ecd-b0cbce6a5137 | -12.3943 | -58.0506 | 2025-12-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 0972f988-8605-3118-b315-8724a56e35b6 | -6.1306 | -41.2875 | 2025-12-12 00:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| fd003072-c5af-3ade-8322-ec963d07fc67 | -8.0516 | -43.0765 | 2025-12-12 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| d2121889-132e-3d86-9a7c-947098091754 | -6.1117 | -41.2892 | 2025-12-12 00:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 7d807765-923d-35c6-b637-57a274a786a2 | -8.0321 | -43.1257 | 2025-12-12 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 5eaa368d-060e-3cef-8a98-0bb9f6bb12d5 | -2.2356 | -45.3929 | 2025-12-12 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 4366ac03-330e-329c-b673-2b31a56307f7 | -4.7261 | -43.0822 | 2025-12-12 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| cdf4504d-06e2-36a2-a8b2-c817e6451fb5 | -3.237 | -42.0802 | 2025-12-12 00:20:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d1ecdb99-f6a9-3180-bdd2-74a5247e1c9d | -2.487 | -47.7692 | 2025-12-12 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 10dc4eb2-b6dc-3e12-a9a9-c87f6f7e7f50 | -3.9511 | -41.5186 | 2025-12-12 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 1a7f394a-d7ce-3334-9899-8ceb88032aa0 | -8.0324 | -43.1022 | 2025-12-12 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 620.3 |
| 66b0c2d5-6388-3de1-bc39-0aa698a0cf27 | -4.334 | -45.78 | 2025-12-12 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 35d13d93-c75b-3360-ac0a-fd741f8d5df7 | -6.0315 | -43.7105 | 2025-12-12 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 106e6e98-63cf-31d6-8446-e09c4d354a2d | -12.4323 | -58.0475 | 2025-12-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 147.8 |
| d57f92b2-5c08-3ebe-8102-4b4b8f253fbb | -3.0695 | -45.814 | 2025-12-12 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| eef54c97-41da-36f7-b877-7541c167267b | -6.1308 | -41.2633 | 2025-12-12 00:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| d109742c-cfa6-3ec4-9273-d332c9e8aade | -2.142 | -45.642 | 2025-12-12 00:20:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3837906d-3d24-3fcd-95bd-8317e5d7a0fc | -12.4325 | -58.0276 | 2025-12-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 4f1527e1-3962-3fca-bf26-c78aa65b4a36 | -2.2355 | -45.4154 | 2025-12-12 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 172.2 |
| 12bdea11-de46-36f0-9165-3d54723bab4d | -3.2371 | -42.0565 | 2025-12-12 00:20:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 63837865-efa9-34f8-91b8-7c0d067a3887 | -8.0327 | -43.0786 | 2025-12-12 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 235.0 |
| 28ebc94c-6dd6-3613-8478-f3d87933d299 | -2.217 | -45.3935 | 2025-12-12 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 263.8 |
| c994bec0-5d44-3503-9c45-d07f50eac11a | -4.7448 | -43.081 | 2025-12-12 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 34854fd3-f24f-32f1-854e-69f0abb2dbb3 | -6.112 | -41.2649 | 2025-12-12 00:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| a3ec5387-abeb-3b1f-aece-206a3d309d02 | -2.4923 | -51.8027 | 2025-12-12 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 014a606f-d7a4-3c20-ad42-8c05af443b77 | -4.3858 | -43.6149 | 2025-12-12 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 7f0667a5-f5ff-3362-9932-2568b48cad4c | -12.3943 | -58.0506 | 2025-12-12 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e20d9fe9-b624-3ec2-8c3f-71b56e7c9de7 | -2.217 | -45.3935 | 2025-12-12 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 0b9f0044-ce18-3677-943b-96327074a941 | -3.0696 | -45.7917 | 2025-12-12 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 152.0 |
| b8dfaf60-105d-3881-87d1-26e6305b0ab0 | -3.9699 | -41.5176 | 2025-12-12 00:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 2a326d6f-19db-3dde-96b7-f116cbcdb965 | -4.334 | -45.78 | 2025-12-12 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e9eec15d-3c01-3aab-9226-757866447c03 | -2.2355 | -45.4154 | 2025-12-12 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 45ecc6c8-ae9e-3243-84f0-3fd65ab48e6c | -2.142 | -45.642 | 2025-12-12 00:30:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f2c32571-6697-37c6-a879-c7107b7383d6 | -2.5108 | -51.7817 | 2025-12-12 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 17d2303c-1a5b-38d6-a0d0-b08c3726f89a | -3.0511 | -45.7924 | 2025-12-12 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 7e9b53fe-ae02-3411-8905-d35b81af4760 | -6.0315 | -43.7105 | 2025-12-12 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d2699e06-142c-32aa-97d3-c97055566801 | -2.487 | -47.7692 | 2025-12-12 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 34e4100f-9bce-36c1-b278-4bc677255973 | -3.237 | -42.0802 | 2025-12-12 00:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 4172e541-6945-34b1-8057-b0d9c0cdf49b | -2.2169 | -45.4159 | 2025-12-12 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 136.3 |
| a3ddd1a6-c6f8-36fb-8679-9e262e597e06 | -12.4135 | -58.0292 | 2025-12-12 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 302.4 |
| 8fb95191-d48b-3330-b32a-020f2ac1669c | -12.4325 | -58.0276 | 2025-12-12 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 31b98094-38a8-388e-bb14-547b83d7dfe1 | -12.4323 | -58.0475 | 2025-12-12 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 50604e16-9395-3b55-a4ad-6fac853c556a | -2.1419 | -45.6644 | 2025-12-12 00:30:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 2b674534-ea5d-3160-90c4-4ce71999e69a | -3.9511 | -41.5186 | 2025-12-12 00:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| f2174061-efcd-30f9-a82c-6cdfd80789ed | -4.4043 | -43.637 | 2025-12-12 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 81af10c9-7f5c-3fe0-802b-3c1e7bb21793 | -3.2371 | -42.0565 | 2025-12-12 00:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 4d412577-f24d-3484-b2a3-a4b18197fd2a | -1.5337 | -52.7414 | 2025-12-12 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 96cfa8d5-dea9-37d2-ad43-26ab5abbfc3b | -3.6293 | -45.3878 | 2025-12-12 00:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 28bca3b4-dd97-3f57-9661-24a540a2acf8 | -4.7448 | -43.081 | 2025-12-12 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d64ba217-990d-3f59-b9f6-274f0d20a409 | -6.1117 | -41.2892 | 2025-12-12 00:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 1654bf0a-57b7-313e-b49f-05794f9a433d | -3.0695 | -45.814 | 2025-12-12 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 73cacd92-1878-3a50-a8da-8dd61ae43f08 | -12.4133 | -58.049 | 2025-12-12 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 258.2 |
| 25169ac1-1045-3e04-8bcc-5125c4a9e116 | -12.3946 | -58.0307 | 2025-12-12 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 219d9a88-8ea8-3f39-b585-ceb362edbb5c | -4.7261 | -43.0822 | 2025-12-12 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 48897398-a1be-3a76-a13d-1a33f898b47a | -4.3856 | -43.6381 | 2025-12-12 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 427079c4-366e-310d-bdfc-00f8fe7dec72 | -9.6791 | -36.3577 | 2025-12-12 00:30:00 | GOES-19 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| 5e430b55-4ba5-3dae-a724-9688fe7733e2 | -2.4924 | -51.7821 | 2025-12-12 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| e51aa2fc-6e45-37aa-a565-df4580b0f692 | -2.2356 | -45.3929 | 2025-12-12 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 825811e1-a35f-3639-9da2-0486bd4f85f3 | -4.745 | -43.0576 | 2025-12-12 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a25f59a9-ffe6-3b47-a61b-5941873a68b0 | -6.1306 | -41.2875 | 2025-12-12 00:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| e98f265c-aa1b-3cfe-8df7-6c7a5c911b8e | -2.5108 | -51.8023 | 2025-12-12 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| c6c1e30b-2100-3a01-aab2-4654e5266180 | -2.142 | -45.642 | 2025-12-12 00:40:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 1f87a551-f2e5-34bb-ab7c-cc744377e8d2 | -12.3943 | -58.0506 | 2025-12-12 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 46e8cc74-b510-3daa-94b4-835d56689272 | -4.7448 | -43.081 | 2025-12-12 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d9347317-8f41-3cfb-ba97-3faab30ab6b1 | -12.4325 | -58.0276 | 2025-12-12 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 3df5d686-407f-3071-9aca-5113f385c829 | -2.4368 | -51.9068 | 2025-12-12 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| cd59fc95-6f35-3693-a78a-83a924d82b11 | -1.5337 | -52.7414 | 2025-12-12 00:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 10cf8084-6bc3-3222-89f8-22f3494f65f3 | -3.6293 | -45.3878 | 2025-12-12 00:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 7ce8b79c-87c0-36cd-a035-1fd7c29bf6a9 | -2.2355 | -45.4154 | 2025-12-12 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 634c9dad-68be-3f16-8c9e-d37236293806 | -12.4133 | -58.049 | 2025-12-12 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 242.7 |
| cf22e447-c8c8-38f3-bd6d-c94a1d6ff9a9 | -10.119 | -36.4956 | 2025-12-12 00:40:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 332bc24b-a2ce-37d5-8d6e-cc49e024e0ca | -8.0513 | -43.1001 | 2025-12-12 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 3bc9a8e9-9271-3d35-a487-ca000052518b | -3.0695 | -45.814 | 2025-12-12 00:40:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e52df300-1665-30c1-bafa-e94fba58ba6d | -4.3858 | -43.6149 | 2025-12-12 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a996a3b2-77d5-32a7-bc67-0e7fbc67900e | -6.0315 | -43.7105 | 2025-12-12 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 290f5d28-8319-3a8e-ac53-96c54a8406df | -2.217 | -45.3935 | 2025-12-12 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 60ad7b40-6e07-3832-b12b-750a39f13856 | -4.7261 | -43.0822 | 2025-12-12 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d37443eb-fcf4-32a9-976c-d30e86d92390 | -3.0696 | -45.7917 | 2025-12-12 00:40:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 1f7b1c45-f89f-386c-9852-8d3d5dd2e220 | -12.4323 | -58.0475 | 2025-12-12 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 249cca5e-6104-3b04-917f-3fffb0605aac | -8.0516 | -43.0765 | 2025-12-12 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 4054b5ad-780c-39b3-b533-9fcafe4038b6 | -2.4924 | -51.7821 | 2025-12-12 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a7b6de2e-e4ce-3541-ba4c-873db258aba0 | -8.0327 | -43.0786 | 2025-12-12 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 3e9a39c8-9456-3b9b-b4f5-d52352ee2319 | -2.4367 | -51.948 | 2025-12-12 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 1907ade5-cc6d-3567-a326-462c311deb67 | -2.4923 | -51.8027 | 2025-12-12 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 235168f8-e4f5-3252-82d5-2221e58e7e6e | -3.237 | -42.0802 | 2025-12-12 00:40:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| ae3f3f0d-5928-31e1-972a-5965774f0a09 | -8.0324 | -43.1022 | 2025-12-12 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 149.6 |
| 2580183a-31d3-3015-af98-9057a01b00ed | -2.1604 | -45.6639 | 2025-12-12 00:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e0b530aa-cc02-3830-8b89-62c91d9bd17c | -2.5108 | -51.8023 | 2025-12-12 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 7456b7ef-fb35-3b9e-b4ff-62958cb0f1a8 | -6.1117 | -41.2892 | 2025-12-12 00:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| deed36ec-bd4b-3341-885c-b9b6a0ddea9a | -4.3856 | -43.6381 | 2025-12-12 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1aafb064-92da-3f00-b9c8-1eb0cd67ee56 | -6.1308 | -41.2633 | 2025-12-12 00:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 777db1b3-04e0-3cb3-b6d9-dad947d564f3 | -2.4552 | -51.927 | 2025-12-12 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 068669ba-fb07-30d4-9ab0-7afebd796642 | -2.4183 | -51.9484 | 2025-12-12 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |


[Clique aqui para ver as próximas entradas](README4.md)
