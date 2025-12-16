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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 349b581e-88c2-3f18-ab5c-e084991bd9d4 | -11.84589 | -43.73754 | 2025-12-16 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57eb00fc-8133-30c6-a4ea-a7723d5cabf6 | -11.75282 | -44.03278 | 2025-12-16 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3917c411-b5d8-39d8-9c47-dddb06a206d2 | -10.03083 | -48.12302 | 2025-12-16 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acb52ba9-1544-3949-bd92-bcb5aa5ad21f | -10.36667 | -44.88443 | 2025-12-16 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90009098-e28d-3e21-ae1f-21e55ff32e47 | -5.93674 | -44.46133 | 2025-12-16 04:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfb33a76-d107-3334-87dd-64047bfb78f2 | -4.07054 | -46.14702 | 2025-12-16 04:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 645d6804-12aa-3dfc-8b69-b4b477ff479a | -10.5502 | -48.72122 | 2025-12-16 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec4bdfa0-dbcb-35f2-aa23-0d39088d7e7b | -3.02729 | -51.4599 | 2025-12-16 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9acca6a1-6557-3f12-9be9-ffaa45ec6594 | -3.03118 | -51.45694 | 2025-12-16 04:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5d83563-6d3b-3e8c-8b73-aead476be306 | -3.79828 | -49.03117 | 2025-12-16 04:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b359d46-287c-3a73-b49a-44eec34662d4 | -3.65539 | -47.55631 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 83e8d0ec-3fbb-3671-bdd8-7081c4b7148d | -3.65602 | -47.5522 | 2025-12-16 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f9beb09b-1fb5-3829-a35f-8e7121d4468c | -11.0932 | -48.2568 | 2025-12-16 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eefd2640-b4a2-3946-a8c9-d742cb945997 | -14.43708 | -44.87121 | 2025-12-16 04:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ea1e4ec-a7a8-329b-b08e-2e0f13f077e6 | -11.8862 | -43.70826 | 2025-12-16 04:48:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ea451d3-c621-3958-8631-14aedb9aee81 | -14.442 | -44.87197 | 2025-12-16 04:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 792bde05-b22c-368a-b8ee-b4ffd7a0133b | -14.44269 | -44.86648 | 2025-12-16 04:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abd940ac-a48a-3ed6-a9f0-2291f0452873 | -11.88581 | -43.71137 | 2025-12-16 04:48:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 864b6f8a-6ea4-3573-bc83-2e47a4ef560c | -15.46378 | -39.16187 | 2025-12-16 04:48:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3bf583b3-64c5-3c12-a99c-a40327cc1fb6 | -12.78423 | -48.82462 | 2025-12-16 04:48:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c2fadd-2d6e-3389-b66c-12b2f573bade | -14.44421 | -44.86847 | 2025-12-16 04:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26079ede-9b62-3566-921c-9bc82fd4f057 | -12.78358 | -48.82917 | 2025-12-16 04:48:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecc47aea-9e3d-3612-8e2c-9f59734e332c | -11.89136 | -43.70893 | 2025-12-16 04:48:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94284725-49e4-3beb-92a3-7b4e2c67d407 | -12.51093 | -48.38361 | 2025-12-16 04:48:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35a5ae3a-81eb-3ac6-8482-77e9aa05d795 | -15.45665 | -39.16103 | 2025-12-16 04:48:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6b42b0da-3ad2-3b94-b3d4-fd10face1511 | -12.57454 | -45.40781 | 2025-12-16 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be16667e-1316-3fe6-950f-dc1e47f396aa | -16.24183 | -58.84271 | 2025-12-16 04:50:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 09a840fd-916e-359c-a77c-c02715e6dcf0 | -16.9988 | -56.58313 | 2025-12-16 04:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 036e9b8e-a3f5-384d-b3fe-0cc0a2aab161 | -16.23777 | -58.8419 | 2025-12-16 04:50:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1182233b-b240-3bea-bff6-a51102825dfd | -16.23414 | -58.84125 | 2025-12-16 04:50:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 936b24cd-af1c-3269-b46d-8bb83dda9893 | -16.98605 | -56.57208 | 2025-12-16 04:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 57f4c2f3-bf56-3a6e-9f50-bd3f8cbd39b4 | -16.98113 | -56.55819 | 2025-12-16 04:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 37ef9c1a-55b3-3d9d-8d37-41aa359f873a | -16.24589 | -58.84353 | 2025-12-16 04:50:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 392fad19-daf7-366c-ac1d-67f4704f7d55 | -16.99524 | -56.58246 | 2025-12-16 04:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5556a200-b973-3b73-b131-4041b2082e51 | -16.23347 | -58.84499 | 2025-12-16 04:50:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2ee883cb-4172-3bd1-bb9c-341847aebf98 | -16.98249 | -56.57142 | 2025-12-16 04:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7f87316b-8f33-33ef-bda7-8c59593592bb | -16.98677 | -56.5679 | 2025-12-16 04:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8e911cb4-a509-3ff2-ad1f-61b410d278fe | -16.99169 | -56.58179 | 2025-12-16 04:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57cb10c6-5271-3c1f-ba1c-440ba8b8706c | -16.23301 | -58.84481 | 2025-12-16 04:50:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 963452e8-90a6-3012-a2e1-a82f47597fd9 | 3.58768 | -60.22166 | 2025-12-16 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9649f91f-0e24-36dd-b700-5a7ed167bcee | 2.04652 | -60.87118 | 2025-12-16 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac7be663-6bcc-3d4c-887a-0c2008c63cb3 | 0.89265 | -60.43332 | 2025-12-16 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f84c629-7deb-3059-970e-6163e525355b | 0.43127 | -60.48896 | 2025-12-16 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e7f3fc9-1a6f-3d8c-8c99-cd81f268cbaf | 1.0892 | -60.65022 | 2025-12-16 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77bcf2f0-9a74-397d-aefe-d2b37da2c33d | 1.08583 | -60.65075 | 2025-12-16 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb6076d5-3afa-3d52-83e1-66b6aba3796b | -0.84939 | -47.56045 | 2025-12-16 06:29:00 | AQUA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 743df556-638a-3d58-a7f8-2f39dbd63334 | -1.29977 | -46.61652 | 2025-12-16 06:29:00 | AQUA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c7e4ee79-2f0c-3aec-b79f-5ff8d4a926d6 | -1.30456 | -46.60997 | 2025-12-16 06:29:00 | AQUA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| d2f2b9f5-47b1-34bf-b9bc-94feb8a6c7a5 | -3.14873 | -48.14643 | 2025-12-16 06:31:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3dd935a1-163d-3c34-9551-ad6872ae07b8 | -3.15068 | -48.1331 | 2025-12-16 06:31:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 440c6e65-6b3b-370e-976e-c5b6b97bbb97 | -2.79432 | -51.40613 | 2025-12-16 06:31:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17850c74-a736-390f-958f-0e04f3d489d1 | -16.99759 | -56.57925 | 2025-12-16 06:35:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| a02a9f55-ee06-36c5-988e-c543e63e9905 | -16.98051 | -56.56965 | 2025-12-16 06:35:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 8a24ead3-4ccd-3333-80bd-abea603e79d7 | -3.6457 | -45.7908 | 2025-12-16 06:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 00033fa2-c092-3670-a33d-a5523b2f9721 | -6.5631 | -51.1126 | 2025-12-16 07:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f68c0330-0423-3355-923c-2a28831cc66a | -3.4138 | -43.9186 | 2025-12-16 07:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 30a8b4d7-b4b2-3625-a2ee-720cce78be20 | -0.91334 | -48.01667 | 2025-12-16 12:33:00 | TERRA_M-T | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1c5563a2-fad1-334f-a787-cdf001b4b3fa | -1.8892 | -47.64582 | 2025-12-16 12:33:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8f963c54-1203-3018-b89e-605a9ed85585 | -1.27357 | -47.11811 | 2025-12-16 12:33:00 | TERRA_M-T | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 63ad2a59-8a9c-3397-ad8f-38e686ea55f7 | -1.78088 | -47.74908 | 2025-12-16 12:33:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f3ab9828-7cec-32e1-ab91-4ad37e4695d8 | -2.22825 | -51.9391 | 2025-12-16 12:33:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 507cff74-5f34-3d90-96ec-f6466c1f88ea | -1.78216 | -47.75572 | 2025-12-16 12:33:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1377e244-701e-36e1-aea6-121afdd3388f | -1.88861 | -47.63995 | 2025-12-16 12:33:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ce416ce2-07ec-388e-977c-b6070d2761d9 | -1.66552 | -52.0654 | 2025-12-16 12:33:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 458d2824-fbc0-3848-8a49-c244390ff52d | -2.79316 | -51.40389 | 2025-12-16 12:33:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ecc831d5-ae25-3f6c-915b-7aad6a946369 | -1.77047 | -47.42323 | 2025-12-16 12:33:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b70033cc-9566-35c2-8609-a6b56d99bec0 | -0.90913 | -48.00858 | 2025-12-16 12:33:00 | TERRA_M-T | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 82d84e0b-6ba6-34a3-b03a-723740ef59cd | -1.78463 | -47.48571 | 2025-12-16 12:33:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5d0d8d6e-72e5-32e6-839a-14af796085a5 | -2.93389 | -48.2305 | 2025-12-16 12:33:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a817d5b0-64cc-3a31-abe4-51f58a17c393 | -2.79187 | -51.41294 | 2025-12-16 12:33:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e987686c-0fc8-3ba0-aba1-a26f1149f7f2 | -1.30842 | -46.61261 | 2025-12-16 12:33:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 276ff1e1-9aa4-3d8b-a446-1fd87c16ff5c | -2.4873 | -49.31363 | 2025-12-16 12:33:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1282fd42-342f-3d6b-8f34-7c38e850a833 | -4.03588 | -45.287 | 2025-12-16 12:36:00 | TERRA_M-T | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| dc4cf7e9-00a2-3102-b159-6b8852d87ffd | -4.03073 | -45.28095 | 2025-12-16 12:36:00 | TERRA_M-T | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 1759baca-5eaf-32ba-a532-36f06712831f | -4.12113 | -47.28418 | 2025-12-16 12:36:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 4e49a5e5-f6e6-3ec4-a5ad-d9fefd180954 | -4.37947 | -47.32024 | 2025-12-16 12:36:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2fa987f1-555f-3e65-8cb4-5992bbcfb28b | -9.95645 | -47.0453 | 2025-12-16 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 230bb54d-881d-34ba-8c22-8b39978a5648 | -11.82908 | -43.78042 | 2025-12-16 12:38:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 19491e67-4135-3ece-90f6-89969ca4c13b | -31.29363 | -54.07255 | 2025-12-16 12:42:00 | TERRA_M-T | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 8.4 |
| 60b02814-bcb9-3e8a-a21a-eaf0f9bfe3f1 | -31.2982 | -54.06323 | 2025-12-16 12:42:00 | TERRA_M-T | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| a99a7b94-93d9-3fc7-8a1c-f5290ea6fd26 | -11.8271 | -43.776 | 2025-12-16 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| ebf2c43a-9272-3840-ac2b-5275ec7fe651 | -11.8271 | -43.776 | 2025-12-16 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| da2e5b41-2da2-3507-a7fb-1fd61494afb5 | -14.6455 | -39.9852 | 2025-12-16 14:20:00 | GOES-19 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 119.7 |


