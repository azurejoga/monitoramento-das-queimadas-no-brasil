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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c198ca71-65b9-3817-98a1-663b8f7daa37 | -10.42305 | -64.43454 | 2025-08-24 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aedb122c-45fe-3e45-9074-93e9b832ee51 | -9.72441 | -65.71327 | 2025-08-24 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b153673-b0b3-37e9-81a8-d86f67cf83b5 | -11.99326 | -61.02047 | 2025-08-24 06:16:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4af1f630-401f-3a9a-9da3-b4f482723a5d | -12.0003 | -61.02116 | 2025-08-24 06:16:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7f166f4-bed9-3d06-9ee9-40be7d53fa95 | -9.50086 | -68.47344 | 2025-08-24 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc59092e-61b6-33d7-b96e-9380cb3c84d1 | -10.4133 | -64.42171 | 2025-08-24 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 608b8ea4-8b71-3847-a908-56f874f4c214 | -9.71934 | -65.71261 | 2025-08-24 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d780ad7-3fcc-32d0-a3ed-671816afe54a | -9.56384 | -68.5804 | 2025-08-24 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a84cd79-d9d8-37eb-9477-21aed895b834 | -9.3554 | -67.56009 | 2025-08-24 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 631e5771-861c-3848-a591-cdc99b4d8356 | -10.41796 | -64.42993 | 2025-08-24 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1558055a-e448-33f1-b677-f03354366549 | -9.1721 | -59.4823 | 2025-08-24 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 049c3de9-a756-3566-b06f-48ab45bb80ec | -20.3594 | -51.7023 | 2025-08-24 06:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d6cfcec2-d3cb-310e-8cf8-7a9be9d1dec5 | -17.6176 | -44.298 | 2025-08-24 06:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 4ae23ecb-a35b-3ec9-ab0a-d9685f266cd2 | -20.3599 | -51.68 | 2025-08-24 06:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 117.1 |
| a800f422-940a-3392-95c0-131bd08d7a55 | -9.0232 | -65.6982 | 2025-08-24 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 5b3cc3bf-391e-306f-9b4c-246f45062c3e | -14.8157 | -47.9118 | 2025-08-24 06:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d25432a6-dc97-385d-ad90-8d8c5a4161bc | -14.8153 | -47.9343 | 2025-08-24 06:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b7b9085b-c1fa-3f9c-955c-c1b82380a7b7 | -9.0231 | -65.7169 | 2025-08-24 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c6a0ca1a-04f3-3db4-99fa-67a64d3e51d9 | -20.3396 | -51.6839 | 2025-08-24 06:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 591bb824-133d-3c91-bff1-155ca9e2b6df | -9.1535 | -59.4834 | 2025-08-24 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d4e6f0b5-53e7-33bb-bf8c-7c6fdec54b15 | -9.1536 | -59.464 | 2025-08-24 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 07366fbd-15c4-3568-b07b-ad791383dc2a | -9.0232 | -65.6982 | 2025-08-24 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1094eaf9-dfe4-3f5e-b26c-d6d231dfb994 | -9.1535 | -59.4834 | 2025-08-24 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ed1910a9-21f9-3bc0-b7e1-7064cf979f60 | -9.1536 | -59.464 | 2025-08-24 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b950aaf0-0aaa-31ae-8eb3-739e392e601a | -14.8157 | -47.9118 | 2025-08-24 06:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6009de60-13ac-3bbf-b7dc-511e38f782d6 | -17.6176 | -44.298 | 2025-08-24 06:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 807d144b-34c4-38b4-ac22-9c7f5cae5699 | -20.3599 | -51.68 | 2025-08-24 06:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 9078c15e-c827-34ef-9bfd-25141e85bbea | -20.3396 | -51.6839 | 2025-08-24 06:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9614e07b-1de7-3e99-b646-89ddce2f30c4 | -20.3594 | -51.7023 | 2025-08-24 06:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1c849bbf-6cb3-3d5b-8439-88c6267a5126 | -10.4354 | -47.1709 | 2025-08-24 06:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 76cc7135-c7d4-3d75-9ace-526d015d1663 | -9.1536 | -59.464 | 2025-08-24 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c10d0b89-0909-328c-9c2c-1e284516a5f6 | -9.0232 | -65.6982 | 2025-08-24 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e4075236-3127-3ea2-95c1-a3215e45ec45 | -10.416 | -47.1955 | 2025-08-24 06:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| be94c3c3-7559-3c92-8353-6947771ab463 | -20.3594 | -51.7023 | 2025-08-24 06:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8fbfd01c-d3db-3b1e-a528-3831e3917884 | -20.3599 | -51.68 | 2025-08-24 06:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 225f73d6-711f-383c-830f-02a95a3f7b5c | -14.8157 | -47.9118 | 2025-08-24 06:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 8422a894-1169-3c12-b11e-3cb718c0d86b | -9.1535 | -59.4834 | 2025-08-24 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e9ee9c1e-522e-341c-b2ed-07ed17be245f | -17.6176 | -44.298 | 2025-08-24 06:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8ecc5278-e711-3574-be1f-4c7065e56256 | -10.4167 | -47.1509 | 2025-08-24 06:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| a5b671ed-b714-3908-aae4-5bc30dc0a3e6 | -10.3974 | -47.1755 | 2025-08-24 06:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2b2804c9-867d-38e5-98c5-5d1a08bcce6a | -10.4164 | -47.1732 | 2025-08-24 06:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 492.0 |
| 5e65cabe-7b95-3f47-a9e1-db26d439bbd1 | -20.3396 | -51.6839 | 2025-08-24 06:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3d2799f9-de0e-3ca6-b5e7-62b2be0b98c4 | -8.67546 | -68.69141 | 2025-08-24 06:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 447fbd70-2e1e-3650-9504-a209efe6c2e0 | -8.68088 | -68.68866 | 2025-08-24 06:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e87fcbf-7de2-3c26-bc49-20ce320ec51e | -8.68161 | -68.69227 | 2025-08-24 06:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd3dd058-ba0c-3c19-9277-c461063f5f15 | -8.66994 | -68.68581 | 2025-08-24 06:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ef9fa16-20cb-3b0e-8c3c-2e3c7b0b4954 | -8.77894 | -68.65186 | 2025-08-24 06:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 074d0317-c14d-34b5-bcb2-521ac1a47687 | -8.68703 | -68.68951 | 2025-08-24 06:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bdd7beb-c49d-33ac-a884-0e34986c13c9 | -8.7851 | -68.65277 | 2025-08-24 06:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7da7b809-23df-3c08-94b0-31eeb3c2e5f6 | -14.8157 | -47.9118 | 2025-08-24 06:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 152676df-7417-3c51-be11-991a02ca7be7 | -14.8153 | -47.9343 | 2025-08-24 06:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| d107acce-143c-3006-a5c5-64b5e01b8d8d | -17.6176 | -44.298 | 2025-08-24 06:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 49.7 |
| fe0a1f05-17c1-3a3a-80f1-e1b2d1c2a54d | -9.1535 | -59.4834 | 2025-08-24 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f27f1b87-8475-34ef-a8e1-63fa07f7269f | -20.3594 | -51.7023 | 2025-08-24 06:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9be4131c-80c5-303c-81ab-3de9de900b37 | -20.3599 | -51.68 | 2025-08-24 06:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ebcc001e-2479-3f25-832e-e95d30d81346 | -10.4164 | -47.1732 | 2025-08-24 06:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 6ae0915c-2d23-393e-bdaa-67f14854f7ac | -20.3396 | -51.6839 | 2025-08-24 06:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 969577dd-56e8-3c40-b80f-a04e12a5b413 | -18.9418 | -47.9294 | 2025-08-24 06:50:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 47.8 |
| d1c5ee3a-bc62-35c9-aa09-e1b6ef0a4341 | -10.416 | -47.1955 | 2025-08-24 06:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| ff0c703a-0ada-3194-b0e1-b5716f1b5fef | -9.0232 | -65.6982 | 2025-08-24 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0d0f9fe4-49e1-308d-a7f0-e6b6d0b1bb73 | -9.1536 | -59.464 | 2025-08-24 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 5b3c01ff-4ceb-3191-8e3e-ab61a7cb4c91 | -5.41807 | -60.16716 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| d6928944-2084-3f24-8093-0fb7cfee6e2c | -5.75301 | -57.57757 | 2025-08-24 06:57:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| bb7c5cb2-a3d9-3116-a8b6-1d6caf8ec2e2 | -5.61141 | -60.23803 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f252e980-bdae-3263-851f-9ad64481504a | -4.9547 | -55.82229 | 2025-08-24 06:57:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d85f1bdb-226f-3fc0-9dc3-426274938289 | -6.67965 | -58.85586 | 2025-08-24 06:57:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f98e6468-e842-31e6-9d8d-e40903ba0155 | -5.75081 | -57.59277 | 2025-08-24 06:57:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5190e1bb-d299-3a8c-8556-8d482244a2c5 | -5.45263 | -60.19267 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 930f8ebb-005e-3108-a243-eb3127da61d2 | -5.42892 | -60.15843 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a810294c-4e27-3dc7-9a16-4f0bb9e800f3 | -5.42745 | -60.1685 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 36795e02-3575-351c-810b-6a801018f7da | -7.55748 | -63.85671 | 2025-08-24 06:57:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 30e35093-5eb2-317d-b164-62bd6536ecfe | -6.31093 | -59.8725 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2c9d6982-c462-3bd6-8a00-d560867a496f | -5.75098 | -57.58448 | 2025-08-24 06:57:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 9b27f197-d37d-3a89-8af9-c08326f1049a | -8.13413 | -62.85943 | 2025-08-24 06:57:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 51fb2db5-5808-385a-b61f-9140a5b2107a | -7.5486 | -63.85537 | 2025-08-24 06:57:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e0aa6ee8-2629-3b83-acf3-7f976bd9c663 | -6.6846 | -58.84982 | 2025-08-24 06:57:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 52484ed9-b63a-339e-91fe-449fae09a93a | -5.44326 | -60.19133 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b531c9f7-3159-32c2-9705-53a48f0a4cf8 | -5.44474 | -60.18127 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 968cad15-a957-346d-ab39-eecbda44b70b | -5.80125 | -59.21829 | 2025-08-24 06:57:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 51fda11a-b027-3e8d-8aa6-34f8ac530a86 | -5.61288 | -60.22799 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 03708411-63ed-3680-9a1a-e6eba3e8996b | -6.57689 | -59.87472 | 2025-08-24 06:57:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8920c57b-03a7-3457-8e74-36226bfa6d0b | -5.74168 | -57.57592 | 2025-08-24 06:57:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| bd392874-bb5c-3233-8e5d-b57bf3b1bdcb | -5.73951 | -57.59108 | 2025-08-24 06:57:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c4f3a8ee-15c2-346c-87e1-91565536ae3d | -7.97081 | -63.07488 | 2025-08-24 06:57:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b2fd6688-b4a7-3f36-8379-b11a45e1f380 | -5.45412 | -60.18261 | 2025-08-24 06:57:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4bc0ce75-99f4-396d-93fc-2174b9b4dd60 | -9.19248 | -59.61882 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9ce9251a-db3e-3c80-9f07-9d356c870064 | -9.01839 | -65.69975 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| cdc1f2a7-cdb9-3e29-b66e-a3b47a5d44a6 | -9.33132 | -63.19028 | 2025-08-24 06:59:00 | AQUA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5da8658c-fe9d-3882-b94e-251c4d104f3a | -9.01674 | -65.71014 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1be13546-dfc1-3d06-9dfd-893b9f259f8e | -9.17067 | -60.80605 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ec5c491d-d954-3dbd-b5d8-0d998c446196 | -10.41095 | -64.42564 | 2025-08-24 06:59:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7d672656-9b34-3098-b560-2c81486db7b3 | -9.01055 | -65.68799 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f08c5672-1f35-3916-84a6-7b338e255802 | -9.23155 | -60.91978 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c73775e9-2e5e-36cb-8907-edc724e8f796 | -9.20354 | -60.77888 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 45a31874-01ab-323a-b0f9-8c67c9b7c6e1 | -11.99664 | -61.01736 | 2025-08-24 06:59:00 | AQUA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 25375a07-7f09-3b71-a3f6-64049a3d490f | -9.16394 | -59.46937 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| a0ff871c-b30b-3acf-95a3-97d34dd2152c | -9.01355 | -65.39014 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4d66b302-1ceb-3165-801a-8caa2b3c64a1 | -9.00727 | -65.70867 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5e6266db-e34f-35f1-99c8-eab067f2b0b4 | -10.41235 | -64.41656 | 2025-08-24 06:59:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 11ecdcb6-a5a6-34e6-979d-f28818ec7c91 | -8.60665 | -62.59231 | 2025-08-24 06:59:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |


[Clique aqui para ver as próximas entradas](README89.md)
