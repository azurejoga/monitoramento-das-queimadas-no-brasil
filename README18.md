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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0351a796-9be1-31d5-9a8f-7269b40baf27 | -11.67427 | -50.35595 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1a9aaee-0bdf-381b-8712-aacf3c7d765f | -9.54709 | -66.1894 | 2026-07-23 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4671bbbd-1528-3362-bd4e-597166cb0e01 | -11.66994 | -50.35907 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9f1ff5a2-91e1-3496-add1-6b4b7bc05380 | -11.70299 | -50.36956 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7b3be335-75f3-3ac6-97b4-eaf5b6246aef | -11.67059 | -50.35294 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1daf3e25-2c4c-3ed1-8021-36f12d0a3386 | -12.88297 | -58.29019 | 2026-07-23 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 972d7e59-fa14-3183-8fc2-97d5882e8da2 | -11.69625 | -50.36869 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 965dda1d-882b-3077-bfa9-d7f0a9265741 | -14.38223 | -58.3355 | 2026-07-23 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5db44ebb-6304-39f1-968b-133f6ae4987e | -13.31473 | -54.32947 | 2026-07-23 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6974507e-dc56-3f0b-b98c-15dbe0dd8a6f | -11.96261 | -50.35939 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e1063c5-bbd3-3a01-b053-aadabf26f3f2 | -11.79934 | -50.38711 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a4de0d36-4edc-3f5d-bd05-c1fedb947699 | -9.89896 | -67.02031 | 2026-07-23 05:31:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c993c7a2-72d0-3634-918a-4f268ad3f40b | -13.32259 | -54.30935 | 2026-07-23 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fef6aede-1b74-3e2a-8ee3-c8df8101298e | -11.6938 | -50.3646 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 80df5870-98b2-3aff-9443-f049c545072b | -11.33502 | -62.22181 | 2026-07-23 05:31:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd2aa75b-40c5-3eaa-a600-d60c4c42f95b | -11.80412 | -50.38249 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| da3da076-4fb2-3f42-85b8-fcd8afc22923 | -11.34115 | -62.22644 | 2026-07-23 05:31:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b292216c-61e8-3292-b3d0-bc4bc39e31a0 | -11.68951 | -50.36781 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26d85492-cc63-3e6e-8eb3-06a3237cd662 | -11.70587 | -50.3785 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6ee73e74-06fd-3591-9e11-b6cd009a6cd3 | -10.25506 | -63.33398 | 2026-07-23 05:31:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5ba1f0c-eba2-30a6-a765-f3a6be8c13bd | -12.24741 | -64.35638 | 2026-07-23 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| affa9817-1408-308e-bf04-eb33b6b563a6 | -13.36981 | -54.30551 | 2026-07-23 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aadcd5a3-72bf-3bbd-a9bf-f2938b2c3763 | -9.82408 | -67.88525 | 2026-07-23 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f04bc43e-0eab-3877-ad22-9f4c2cefcab4 | -11.6789 | -50.3651 | 2026-07-23 05:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| f4966e29-c980-3279-af9a-60ec8f9dd50e | -11.698 | -50.3629 | 2026-07-23 05:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| dee72e24-5350-3acc-88c9-508d406464bc | -11.6792 | -50.3437 | 2026-07-23 05:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 757a75c6-d20d-3c5c-84a0-1f51fff1f957 | -11.6789 | -50.3651 | 2026-07-23 05:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 3a71ecb6-e0db-31a3-beee-fe8b10ae73ce | -11.6792 | -50.3437 | 2026-07-23 05:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2f7d691d-34fe-3391-b9b3-84b0fb01db18 | -11.698 | -50.3629 | 2026-07-23 05:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 44bd4fbd-e565-33b9-bf8a-a73fd38a069d | -11.6792 | -50.3437 | 2026-07-23 06:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c429c3a4-c0f6-3f8e-8249-4fa3a27b5279 | -11.6789 | -50.3651 | 2026-07-23 06:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 7da16d33-9ef0-3acd-a419-fb5781aca532 | -11.698 | -50.3629 | 2026-07-23 06:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 110269ec-dde7-37ca-953b-5eb421b64f18 | -9.1003 | -59.40489 | 2026-07-23 06:05:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1325ebd1-9118-301f-bda2-6c9826b983c9 | -9.10361 | -59.40115 | 2026-07-23 06:05:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ca2681f-597e-35eb-b762-eb727cb3c7ab | -9.16948 | -58.31271 | 2026-07-23 06:05:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d32c61a0-9f00-32eb-bde9-c9dd2d011f65 | -9.12797 | -61.06493 | 2026-07-23 06:05:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db4ffd15-9ba0-3fb4-816b-286481bcd08b | -8.8252 | -63.90265 | 2026-07-23 06:05:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc2c5a09-a337-3ecf-82d1-c13b6a2c25ff | -9.12719 | -61.07069 | 2026-07-23 06:05:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef6fa9c6-a02e-3f7f-9eb4-97f6a397a6d2 | -9.12371 | -61.0585 | 2026-07-23 06:05:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4699f06e-4076-33dc-a795-b08f9dbef612 | -9.55262 | -66.19231 | 2026-07-23 06:05:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 816f7831-980d-3a66-9cd2-562ac6cd12a5 | -9.16891 | -58.31723 | 2026-07-23 06:05:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 350313e9-ef2d-30d2-a7c8-868e6ba9c63a | -8.56026 | -66.67119 | 2026-07-23 06:05:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5180453a-7441-39d5-a859-0e25f86dd186 | -9.10079 | -59.40104 | 2026-07-23 06:05:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc6d8e97-85e1-3606-9c68-c5df34ab4c21 | -9.16345 | -58.31182 | 2026-07-23 06:05:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faa61b30-0e82-3831-be23-066cd211379a | -9.10309 | -59.40495 | 2026-07-23 06:05:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae2f2d31-d75e-3140-9ff5-e0d999fecd8a | -8.82467 | -63.90639 | 2026-07-23 06:05:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d195f57a-29f5-3272-aa1a-ea9a94314415 | -9.89769 | -67.02116 | 2026-07-23 06:08:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee423ed5-053a-3b6d-8bc0-3bbd12a9c392 | -14.382 | -58.34148 | 2026-07-23 06:08:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5af3754-9bed-386c-b03b-8ff5285de66f | -14.38142 | -58.33497 | 2026-07-23 06:08:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef9ebddd-cb23-3f92-af7f-cb05a33bf20a | -14.38259 | -58.33577 | 2026-07-23 06:08:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4773037f-5707-3ba6-8891-59ce44e6e091 | -9.8254 | -67.88499 | 2026-07-23 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa54c75f-5690-3142-a109-221bbfe6c5e5 | -9.82144 | -67.88814 | 2026-07-23 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5c535f9a-f67f-3563-82ea-6314e7587a23 | -14.3808 | -58.34067 | 2026-07-23 06:08:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed786ffa-8f71-3f4f-8926-d849528247d2 | -12.88232 | -58.29063 | 2026-07-23 06:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21f9af9a-e5ca-322b-9cd5-f9056cf10ad1 | -11.698 | -50.3629 | 2026-07-23 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b1bbc32a-9a8d-3186-bc4e-f2785495eea3 | -11.6789 | -50.3651 | 2026-07-23 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| b619aab8-cbf7-34c1-891c-20f5eee19b8a | -11.6792 | -50.3437 | 2026-07-23 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| e380ac79-aabc-3301-933c-364bcf38de42 | -11.6789 | -50.3651 | 2026-07-23 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| a95efd2e-f728-3881-9b85-8d7aad379271 | -11.6792 | -50.3437 | 2026-07-23 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7ca639dc-5479-3ba3-a79a-426f06f72055 | -11.698 | -50.3629 | 2026-07-23 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c425fa65-167a-3dfa-99e3-2f7a6e8bcf71 | -9.8234 | -67.88718 | 2026-07-23 06:27:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b4a934d-c73d-348b-847a-1736504d29fe | -9.82414 | -67.88176 | 2026-07-23 06:27:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85969b16-be1c-3f25-9d4e-717d79ed592f | -11.6599 | -50.3673 | 2026-07-23 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| d36ca4d9-4ede-3b36-bf63-3f6214887e02 | -11.6789 | -50.3651 | 2026-07-23 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 477f5bb1-8647-3121-b4d7-bafb1a228bdb | -11.6789 | -50.3651 | 2026-07-23 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| bbf85c91-b6fc-3506-af2f-916ce22ddcc4 | -6.49642 | -42.22086 | 2026-07-23 06:40:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| b4149d55-4dd4-3720-8a05-f557abb68936 | -6.20964 | -49.42558 | 2026-07-23 06:40:00 | AQUA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| eca56785-59fe-364c-b02a-99d22a0e1c7e | -6.04608 | -43.86513 | 2026-07-23 06:40:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2caed003-270b-30c9-b5f6-a3db4f40a8c4 | -11.95808 | -50.36512 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 755d7332-cd3a-3f5c-aa81-6133e2c0d563 | -11.66431 | -50.3478 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eb006e81-82b4-3cda-b78c-2ab37d947eb8 | -11.67931 | -50.36916 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8bbc78e3-e79b-3dff-9fe3-5b64f0b9f6cf | -11.92988 | -50.37014 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bcdfffc7-c683-33c4-8cba-0f88fd6aad51 | -11.58189 | -48.3996 | 2026-07-23 06:42:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 621dcccd-b7f1-3df8-b76b-4e604c2ffa07 | -11.67181 | -50.35848 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d22e2d43-e5ed-398b-9772-4fcea80a0069 | -11.68824 | -50.37057 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 06ab8c61-f4f5-343b-99ac-d346b23964c4 | -11.88161 | -50.37561 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f8684edf-2793-3219-a5bf-ec9cfd158b4d | -11.69718 | -50.37199 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 411feb03-3d24-325f-8def-b21b3100fc03 | -11.94915 | -50.36371 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| dfc29d2a-79f7-3840-bf91-319cfe2ab2af | -11.95059 | -50.35447 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| cf632b45-4b98-34e0-8046-f1dd30fc0d83 | -11.88018 | -50.38487 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e30feee2-4d5c-3e23-80a7-c13fc6f7bc98 | -11.67037 | -50.36775 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e1c10069-12a7-38bf-bc70-2732f8152152 | -11.64934 | -50.32647 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d971455-77a8-3eb7-9e37-09d0dfb43aa0 | -11.78151 | -47.0976 | 2026-07-23 06:42:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3836eec9-83e4-3033-b710-e810daede681 | -11.68074 | -50.35989 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 77195ad2-5415-378b-a8a4-3ea0b2b001da | -11.79998 | -47.10026 | 2026-07-23 06:42:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 89b17ccd-8dbb-359c-8bdd-d9befb201fea | -11.90914 | -50.38582 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f3a8bd2a-e0ec-36eb-a48e-b4a61c3449ec | -11.95664 | -50.37437 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ed8563a-6627-3ad3-b034-479fe70b8513 | -11.79075 | -47.09892 | 2026-07-23 06:42:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ecf7109e-978b-3c40-a88a-919be697310e | -11.81304 | -47.32825 | 2026-07-23 06:42:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b6408821-df3a-3f86-b234-1dd6d492d889 | -11.78008 | -47.1075 | 2026-07-23 06:42:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7ee32a56-a46d-3424-b3fd-2225f1f03f93 | -11.66287 | -50.35707 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| ee026810-46ce-392f-8404-e9a481548d54 | -11.68968 | -50.36131 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0115e132-1f28-3351-946c-f9c519afa25b | -11.91058 | -50.37657 | 2026-07-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b7d1ebfb-83dc-3bd0-9c64-1ca89f1a22b4 | -14.30457 | -52.0761 | 2026-07-23 06:44:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6a4b21a5-5e2b-37c6-8bfd-8ea8a0278d0f | -15.72302 | -48.23937 | 2026-07-23 06:44:00 | AQUA_M-M | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 18096c7e-3832-31fa-af67-a53e6967166c | -11.6789 | -50.3651 | 2026-07-23 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 550625e9-b87e-3193-a23c-1082fee050e6 | -11.6789 | -50.3651 | 2026-07-23 07:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 63e2eba8-e932-3c78-b01c-7d793f0f3473 | -11.6789 | -50.3651 | 2026-07-23 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d505d724-96a0-3b2e-9a1a-1194ae60eac8 | -11.9641 | -50.3747 | 2026-07-23 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b383e3aa-b870-3357-979e-b3f85c2bd24b | -11.6789 | -50.3651 | 2026-07-23 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |


[Clique aqui para ver as próximas entradas](README19.md)
