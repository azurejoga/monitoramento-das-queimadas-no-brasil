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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9581d90-4df3-39de-9039-daa067fa5d14 | -9.0657 | -61.3743 | 2024-09-26 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 9f4168be-c129-343d-9e34-69d28336a55d | -9.086 | -61.1245 | 2024-09-26 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 729e5a19-35bb-3ded-b625-290188403327 | -9.1046 | -61.1237 | 2024-09-26 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5ba5f609-622c-3891-bcd0-6a22b57bfbc4 | -9.3462 | -51.0704 | 2024-09-26 03:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 4c906c17-f441-36bc-b6de-ad55af1714ec | -10.8161 | -45.8868 | 2024-09-26 03:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 0bf1e538-628e-3965-84bd-240182a37c0a | -10.8165 | -45.864 | 2024-09-26 03:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b083a3ec-235d-3626-b474-231649ac9775 | -10.8352 | -45.8843 | 2024-09-26 03:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| f9cc2c22-284b-3a28-89b8-85da2a98fd97 | -10.8355 | -45.8615 | 2024-09-26 03:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 3b348ada-d792-31d3-971c-c0583171d25c | -11.222 | -45.536 | 2024-09-26 03:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 670d85de-3d97-3c8c-9e04-07dc7651984f | -11.1845 | -54.7769 | 2024-09-26 03:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e19c0ee0-2181-3b72-9ebc-a9e34b1190ea | -11.2031 | -54.7956 | 2024-09-26 03:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 231.3 |
| a3885980-d81b-3170-8908-7301e8f49153 | -11.2034 | -54.7752 | 2024-09-26 03:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 319.8 |
| d2ce2237-670f-3bc1-8201-b07169c5b546 | -11.2036 | -54.7548 | 2024-09-26 03:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 40104306-c4b7-3a9d-82d0-caac9daf8c1f | -11.222 | -54.7939 | 2024-09-26 03:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6704425b-c111-3fde-9962-799e3d84b636 | -11.2223 | -54.7735 | 2024-09-26 03:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| d9d71e42-26e5-347b-8055-b87b6c5fbb16 | -11.2412 | -65.2997 | 2024-09-26 03:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fcbbbbc6-7f3c-3c82-95ed-60c3d89e0c04 | -11.2413 | -65.2809 | 2024-09-26 03:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f092ac82-846a-3ec6-b41f-6a56e237fd55 | -11.2599 | -65.299 | 2024-09-26 03:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 81ec4756-ab18-3a0a-ba7a-4c0240cffe2b | -11.26 | -65.2801 | 2024-09-26 03:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 120.0 |
| b19f3812-a338-3983-a124-e17e586a4264 | -11.2786 | -65.2982 | 2024-09-26 03:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f3eccdf0-3d14-3d7a-bf79-095daae34ea9 | -11.2788 | -65.2793 | 2024-09-26 03:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1818c2af-c525-3b84-b00f-24fb23d6048e | -12.2367 | -45.5045 | 2024-09-26 03:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 1fab48ca-32b8-3755-aca4-2cc4dd6b6def | -12.2175 | -45.5074 | 2024-09-26 03:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 95bb111b-b3be-34c6-a543-0af0c491c505 | -12.2363 | -45.5276 | 2024-09-26 03:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| de11b550-d260-302f-8ee9-4c1aa7fd02f5 | -12.5218 | -48.9173 | 2024-09-26 03:36:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ce6efc8a-b7ed-356d-bdb6-eef90dd10f48 | -12.5273 | -53.5168 | 2024-09-26 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d9fca412-17b4-340b-9ff6-f2b871bb763a | -12.5276 | -53.496 | 2024-09-26 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 83da8446-664b-324a-b4a4-b4a32e778263 | -12.5467 | -53.494 | 2024-09-26 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 179.6 |
| af620d52-0e00-3759-864b-daa5d69fe62d | -12.5464 | -53.5147 | 2024-09-26 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| efaa90a5-1aba-3afe-ac4b-9b795024f745 | -12.5026 | -48.9198 | 2024-09-26 03:36:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 74706ff8-c2b1-320a-9f16-cceccacb2927 | -15.3371 | -58.1651 | 2024-09-26 03:36:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e6c5de8e-ec1b-31cc-9e19-1a95b50bebba | -16.098 | -52.0111 | 2024-09-26 03:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 69886893-59c3-3f11-82fd-81d17d183536 | -16.0985 | -51.9896 | 2024-09-26 03:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 191df467-ef0f-3e1e-be02-4438e12c4971 | -16.1176 | -52.0082 | 2024-09-26 03:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 005859d2-7104-3906-8bc9-5e2d52d6bc16 | -16.118 | -51.9867 | 2024-09-26 03:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 219.1 |
| f31ca438-080f-345c-aa32-b508d9df819c | -20.6074 | -51.5209 | 2024-09-26 03:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.4 |
| 0df8e305-113d-3454-bfb5-06c1547ee6b7 | -20.608 | -51.4986 | 2024-09-26 03:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.1 |
| 3d9f72f2-69d5-33f5-a094-6a7ec9be75c0 | -21.9374 | -48.5688 | 2024-09-26 03:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9346329c-c67b-39d3-8d7a-905eb740c634 | -22.2162 | -47.5603 | 2024-09-26 03:37:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| ace4c166-4181-3aae-89d5-e92061d82e6d | -2.6785 | -57.531 | 2024-09-26 03:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d1ec5063-986c-3f56-8bd0-5ed5988e6c2e | -2.6968 | -57.5307 | 2024-09-26 03:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c77a5ac8-b6a8-35a8-a632-af688e34c29a | -3.5673 | -50.3794 | 2024-09-26 03:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| b04ed061-eba4-312a-a2ae-5d4401bb1abc | -3.9208 | -46.4459 | 2024-09-26 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 80978982-143c-34dc-b28d-ce650126739f | -6.8024 | -59.3044 | 2024-09-26 03:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7cfb759f-92cb-31ad-82c5-e9e1034373b6 | -6.9306 | -63.1053 | 2024-09-26 03:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 0022369b-da87-3b14-bd38-bbdf7deaf3ba | -7.3824 | -55.4924 | 2024-09-26 03:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 520f5ea5-07a5-33c0-b044-81219b33ff46 | -7.3823 | -55.5124 | 2024-09-26 03:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 7ffb8686-7347-3081-8577-b98cb2cd119b | -7.3639 | -55.4935 | 2024-09-26 03:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| c6069550-568d-3fea-b7da-37ac602542c3 | -7.3637 | -55.5134 | 2024-09-26 03:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 275.0 |
| d034b04e-ab22-3094-8242-4f96acacfe9d | -7.3636 | -55.5334 | 2024-09-26 03:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 9f54fd8d-cc80-3010-a843-0b34032fac17 | -7.2905 | -61.106 | 2024-09-26 03:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f79d5164-870e-3eaf-9724-3af60c9695ec | -7.8156 | -54.7252 | 2024-09-26 03:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 3b3b7e88-c0f0-3741-a20e-a2fe51100445 | -7.8154 | -54.7453 | 2024-09-26 03:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 60d608e2-caef-3796-897b-c0f888b118d8 | -7.797 | -54.7263 | 2024-09-26 03:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2676ba5c-3754-320c-86ea-5d9a6b52a860 | -8.1579 | -61.2809 | 2024-09-26 03:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 1298effa-7129-3fe2-9043-f9ce1c3d572e | -8.1394 | -61.2817 | 2024-09-26 03:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| ccc2bf65-83f3-3707-a4c7-a19c6f3e1dc9 | -8.3155 | -54.9956 | 2024-09-26 03:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a0f2672a-2b34-31e8-9864-ac6baeae308b | -8.8098 | -58.2172 | 2024-09-26 03:45:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1bfd59b6-308c-344d-ac09-5091fb047fce | -9.1046 | -61.1237 | 2024-09-26 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b3e594da-6c98-3e86-bf6d-1acba1531052 | -9.086 | -61.1245 | 2024-09-26 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 473e11cf-6309-3033-aa2e-65d2e335cc2c | -9.0657 | -61.3743 | 2024-09-26 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 5cc26584-ac5b-39d1-88ba-8b54650c903a | -9.3462 | -51.0704 | 2024-09-26 03:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d71955b7-a273-3ec9-8452-9a93f4f17b11 | -10.0515 | -53.4432 | 2024-09-26 03:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| baed4920-1cc8-3826-bc66-f7fc9ae5453f | -10.0513 | -53.4638 | 2024-09-26 03:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 706242a2-9772-3903-9858-0614632e7a49 | -10.0327 | -53.4448 | 2024-09-26 03:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 179.0 |
| f594bbdb-dd00-3ba2-ac70-b1fffca88f2b | -10.0324 | -53.4654 | 2024-09-26 03:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 360.4 |
| b7ce8164-174b-3699-8510-19864b7a7d72 | -10.0322 | -53.4859 | 2024-09-26 03:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 2d765302-9728-3ca0-a16e-8a022195fee4 | -10.032 | -53.5065 | 2024-09-26 03:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| fb988763-2e4f-3a39-898b-3a886369624a | -11.222 | -45.536 | 2024-09-26 03:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 41057c17-f88d-398e-86dc-55e29f336432 | -11.212 | -51.1627 | 2024-09-26 03:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a29c63a0-d479-3578-843d-43f663886166 | -11.2788 | -65.2793 | 2024-09-26 03:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| bb904478-f7dd-3d05-a594-fde46069216e | -11.2786 | -65.2982 | 2024-09-26 03:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f97cb470-5e3b-306f-a1d2-332361913542 | -11.26 | -65.2801 | 2024-09-26 03:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 3f622522-96eb-3ec0-9988-b2fb2f857f3b | -11.2599 | -65.299 | 2024-09-26 03:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 4afeaf7d-1ed4-36e7-bc92-ecef8bc54e7f | -11.2413 | -65.2809 | 2024-09-26 03:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| edc3b14f-ad38-3466-810b-c72587176ee1 | -11.2412 | -65.2997 | 2024-09-26 03:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8330b5c6-fc83-385e-bd74-8b01fc223e64 | -12.2367 | -45.5045 | 2024-09-26 03:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 47537210-ec14-386f-866c-16b8047f9f9d | -12.2175 | -45.5074 | 2024-09-26 03:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 46ba2040-4344-38e5-950c-06234a05dff3 | -12.5467 | -53.494 | 2024-09-26 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 9aa9bf39-22ef-3574-8d46-c8c47994af75 | -12.5464 | -53.5147 | 2024-09-26 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| f56d3ee5-9196-32aa-b336-b65b24d131d1 | -12.5276 | -53.496 | 2024-09-26 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| f51b80ef-1998-3ed4-9ed7-9dbadd53032a | -12.5273 | -53.5168 | 2024-09-26 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| d15029a9-ed36-39b6-9e50-47513265f5c2 | -12.5218 | -48.9173 | 2024-09-26 03:46:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| c97b2b83-5284-3767-9df2-c869a31e00c2 | -12.5026 | -48.9198 | 2024-09-26 03:46:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| bc3eedab-d724-39fa-afa3-d12aa5276bb9 | -12.5023 | -48.9418 | 2024-09-26 03:46:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1ca82c1b-00eb-3b7e-a4cf-6add6cb07a0c | -12.4835 | -48.9224 | 2024-09-26 03:46:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a5e79a21-e33c-31cf-9ec9-76d1d0f29fab | -13.4993 | -61.2698 | 2024-09-26 03:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 93cb8705-22dd-3ab2-b13e-24c321690749 | -14.9018 | -51.4965 | 2024-09-26 03:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 605a187a-a0b3-3232-9575-3c49a1a6e0ab | -14.8828 | -51.4777 | 2024-09-26 03:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 881fc8e3-0310-3e08-a1f3-a5b3cfa8c3de | -14.8824 | -51.4992 | 2024-09-26 03:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 276.1 |
| e2b03ffb-7474-3a2d-94dc-f437e6bf0ac3 | -14.8634 | -51.4804 | 2024-09-26 03:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| eacb603b-dc73-39c9-95d7-0c0b9c3c8640 | -14.863 | -51.5019 | 2024-09-26 03:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| aea8691f-88cd-317a-82b6-028e2e488c86 | -15.3371 | -58.1651 | 2024-09-26 03:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7e7a9bcc-316f-3a20-808a-d34f9e34e003 | -16.118 | -51.9867 | 2024-09-26 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 28e0edb9-ecb0-3d74-8450-ec4a5791d963 | -16.1176 | -52.0082 | 2024-09-26 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a1e21c8f-ac94-3c4e-909f-b847d20477ec | -16.0985 | -51.9896 | 2024-09-26 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 6236672d-5e33-38f3-b5a2-bd315286d5a1 | -16.098 | -52.0111 | 2024-09-26 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 064a29af-befa-3d33-9aad-b8896d5fc5af | -20.608 | -51.4986 | 2024-09-26 03:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.4 |
| a5c3c7b3-ebd7-3b43-b4d7-71494f6f215b | -20.6074 | -51.5209 | 2024-09-26 03:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.2 |
| f0b5978e-4c9a-3d46-9626-bc36c2526398 | -21.9381 | -48.5453 | 2024-09-26 03:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 85.8 |


[Clique aqui para ver as próximas entradas](README55.md)
