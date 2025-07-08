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
| 673de7d6-dd7f-374a-a243-4a7bed76f9e1 | -10.6489 | -49.4483 | 2025-07-08 05:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e1f7ff09-3f8c-3157-88ee-645b0262654a | -11.4397 | -45.0923 | 2025-07-08 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 951a85b4-da46-3a3f-abda-f41ac9e26c03 | -11.4393 | -45.1154 | 2025-07-08 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 78599049-6235-3ec5-b018-5787fc9a0577 | -11.4201 | -45.1181 | 2025-07-08 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 790e6ba1-3a38-3d53-a837-8ce9d18fdf15 | -11.4205 | -45.095 | 2025-07-08 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2e8879a6-edb3-3923-9a22-027657716a79 | -10.6486 | -49.47 | 2025-07-08 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 62779e90-cdba-3263-937b-69cebff4134b | -11.4201 | -45.1181 | 2025-07-08 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ed109ccd-4719-3e4d-95aa-2d5aa25c2d62 | -11.4205 | -45.095 | 2025-07-08 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d0f911f8-8ebb-3cd4-8952-8ac7beecc21b | -11.4397 | -45.0923 | 2025-07-08 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 753c844e-95b3-3238-9b19-bd7369710d8c | -11.4393 | -45.1154 | 2025-07-08 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c87d232e-10c8-3050-8ddf-7bda904f28e4 | -10.6299 | -49.4504 | 2025-07-08 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 702235d4-91b4-3dc0-8bce-ba83b69ec69e | -11.4205 | -45.095 | 2025-07-08 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 0c7c627e-58c1-3ae3-aa8d-31553ba868ed | -11.4397 | -45.0923 | 2025-07-08 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 7f13c1d8-eff4-3552-81ba-913191dcd9ef | -10.6299 | -49.4504 | 2025-07-08 05:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 92c3fc3c-ecee-3a4b-b1cb-3b7d476192ab | -11.4393 | -45.1154 | 2025-07-08 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| fe920882-0ad6-3acc-bf1d-adf0b646e49a | -10.6489 | -49.4483 | 2025-07-08 05:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 115d05c6-d4a5-3fa2-b553-f1fa24d9c717 | -11.4393 | -45.1154 | 2025-07-08 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 85e4bec4-161e-3d6f-b300-211e13d45020 | -11.4205 | -45.095 | 2025-07-08 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| de0cfb40-bb27-3b84-b1d7-e29d2026b10e | -11.4397 | -45.0923 | 2025-07-08 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 32a42f53-8fc0-3909-9256-391c31c50c03 | -10.6299 | -49.4504 | 2025-07-08 05:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f7396791-ae33-35b6-8df2-b5511fb62b4b | -11.4201 | -45.1181 | 2025-07-08 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 08187358-8f5c-3ce0-bc9e-66977f3c3794 | -11.72302 | -62.82116 | 2025-07-08 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 467a287f-e103-37ae-a3fa-4aaa6b686b08 | -9.6213 | -67.27309 | 2025-07-08 05:55:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 749a56a0-27b9-3864-98b4-c8b502ecfd9f | -10.04465 | -64.99313 | 2025-07-08 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7a07ac1-1099-3c89-a588-e786f5e46ad7 | -10.25504 | -67.17816 | 2025-07-08 05:55:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59d82b49-6897-3ce3-92f1-9fd493d9cbb1 | -12.03025 | -57.08278 | 2025-07-08 05:55:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69956243-0bce-3a14-b5bf-c60629568f6d | -7.91981 | -61.55856 | 2025-07-08 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b819132f-9926-3703-84c1-be2bd80dd8a2 | -9.71009 | -63.31908 | 2025-07-08 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba2eb074-5323-3904-805e-5475f1966f33 | -11.72761 | -62.82174 | 2025-07-08 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e00b058-c1c0-3106-bdfb-7ee1da74ef4d | -9.43094 | -63.46014 | 2025-07-08 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5734657f-d813-36a6-a31b-1f712f6e1910 | -9.57138 | -62.26238 | 2025-07-08 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2b64e37-eaa4-30d5-ad9e-7f33fd87c199 | -9.33917 | -58.84652 | 2025-07-08 05:55:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd89ffe-d26a-3661-8f07-54244c48c5aa | -8.50178 | -69.98953 | 2025-07-08 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e069e5da-8fe2-3923-b95d-2e370beebc6e | -9.34447 | -58.85139 | 2025-07-08 05:55:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7e7e791-e482-3c35-91f6-9a876bcd94e8 | -10.70974 | -69.4924 | 2025-07-08 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d267b103-c66d-3686-a662-07b0760320aa | -9.42725 | -63.45556 | 2025-07-08 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e7a09d1-d2be-36c4-88a8-6a940e74ab57 | -8.92193 | -69.33076 | 2025-07-08 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c08bfd8-29cb-3021-b7a4-a34323399332 | -7.91632 | -61.55909 | 2025-07-08 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 437855b9-69ad-3316-b833-ccc3981d3854 | -9.51418 | -65.58788 | 2025-07-08 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d9a4c0d-91c4-3cda-8307-d0033db37fb3 | -9.02316 | -61.23234 | 2025-07-08 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed37f63c-350c-3503-9feb-6eb21b35f3dd | -11.28547 | -61.46021 | 2025-07-08 05:55:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5857e11-1461-3feb-bbf1-fe8d457a8ecf | -9.62474 | -67.27362 | 2025-07-08 05:55:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65b01d2a-cdf3-33a5-b315-116ae5c8af09 | -11.4397 | -45.0923 | 2025-07-08 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0f59cfaf-cfe9-3db5-9d96-2e61bdce11dd | -11.4393 | -45.1154 | 2025-07-08 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 21e860fb-f4b1-351c-b4c1-902feab8d5f8 | -11.4201 | -45.1181 | 2025-07-08 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a024862f-edf4-3888-8c95-438899b8b42a | -10.6299 | -49.4504 | 2025-07-08 06:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| eab33099-f89e-303f-882b-155f56a5d3ce | -11.4205 | -45.095 | 2025-07-08 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 56f429dd-619c-3927-9321-bbfbb6be8dc3 | -8.06822 | -43.09858 | 2025-07-08 06:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| ca6a4408-c736-356b-9784-ad1d5cfd0e5f | -8.05872 | -43.11704 | 2025-07-08 06:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 3ba8033b-623e-3dca-a6f8-7e6f18687a62 | -5.40195 | -43.24096 | 2025-07-08 06:01:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| fc8abbe2-dc26-341c-8b54-7288feea4ceb | -5.41074 | -46.06749 | 2025-07-08 06:01:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| af85bdbd-cca5-35bf-8629-31b5bd886df8 | -5.40123 | -43.22653 | 2025-07-08 06:01:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 29be5860-a136-397b-a36d-12e57555d435 | -7.24883 | -43.07881 | 2025-07-08 06:01:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| b8505bd7-b1b6-3fb2-8477-ae1d4570a37a | -5.39844 | -43.24733 | 2025-07-08 06:01:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 40c16d9a-cab6-3f65-8ab6-ce1ab7e9be53 | -10.57822 | -49.11153 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a3246987-b96a-3382-be11-2ee5921c86f5 | -13.39811 | -47.87984 | 2025-07-08 06:03:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 55560a1e-3b17-33d9-9040-26f5c18f4616 | -10.63668 | -49.47329 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50767f59-f5fc-3e1b-bf1a-d54c49d151e6 | -9.17755 | -50.17167 | 2025-07-08 06:03:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dccf9f85-add5-38db-8e31-7b51ea390c74 | -11.4294 | -45.0944 | 2025-07-08 06:03:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 611e165c-e567-32a2-aa67-0f59d0dd3b1e | -13.01518 | -46.29039 | 2025-07-08 06:03:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d28bfc8a-b57d-390f-ad0d-5bd729fb2c5a | -11.41691 | -45.0928 | 2025-07-08 06:03:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 86fb405b-dc40-39fa-bdc1-84f9686458bc | -10.63806 | -49.46375 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 73c723f5-73c0-32cd-8d5e-7a050d71c620 | -9.21538 | -48.59325 | 2025-07-08 06:03:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a60c42f5-4403-3481-9e48-e576bcee171c | -10.62122 | -49.45151 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0cc7f0d1-ed65-3dc6-a307-87434ac47984 | -10.63033 | -49.45284 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 80ee5eb2-4a88-3227-a8b0-494d42558e70 | -10.63944 | -49.4542 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ad7e8cc8-f051-3ef8-8a72-8e0db394e47e | -11.43945 | -45.11489 | 2025-07-08 06:03:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 239fb199-6932-312e-a484-9647387820ef | -10.64718 | -49.46507 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 2f051de5-ae77-3b9c-a0d1-0b428f0750a4 | -13.40406 | -47.88758 | 2025-07-08 06:03:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e804889a-727e-35e1-885e-faf4a811a22b | -9.17621 | -50.18061 | 2025-07-08 06:03:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c2bb943a-06bf-34b2-8b02-b438566cf028 | -10.63171 | -49.44328 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e9d981a7-6f46-3ad0-8936-b6d894a2d2ca | -9.22619 | -48.58451 | 2025-07-08 06:03:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 592365bd-d191-3383-88a5-e4a3b4dcd013 | -11.42697 | -45.11329 | 2025-07-08 06:03:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 14d6d6f9-0116-3269-b62b-4fcf6207f537 | -9.22473 | -48.59458 | 2025-07-08 06:03:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 500ea6ce-380c-3dbc-91f1-f899e69d6273 | -11.41451 | -45.11162 | 2025-07-08 06:03:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 73a52025-b7a0-3bbe-a99b-86e0fd13d67c | -10.64856 | -49.45552 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 784b6c6a-c53a-396f-bc5c-3f12b1468752 | -10.57681 | -49.12139 | 2025-07-08 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 82d40880-62e2-3c5e-b549-c858c21139ed | -9.21683 | -48.58325 | 2025-07-08 06:03:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e64c039f-de93-3012-b54f-47e2f9a8ad59 | -10.6489 | -49.4483 | 2025-07-08 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7320c74f-7227-3f12-890d-a23bd949b80f | -11.4393 | -45.1154 | 2025-07-08 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 441fd93e-09f2-31d6-a921-d01d5ddc7385 | -11.4205 | -45.095 | 2025-07-08 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b0cd787f-3b85-3c24-a7c0-bc37edbf5638 | -11.4397 | -45.0923 | 2025-07-08 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c4fa61a3-34b2-38cf-9688-fa63915773da | -11.4393 | -45.1154 | 2025-07-08 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a6ad583a-f72b-373c-a37e-125767efa8ae | -10.6299 | -49.4504 | 2025-07-08 06:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| e642fe7f-92f3-30de-b61d-4f207e3d843b | -11.4205 | -45.095 | 2025-07-08 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4d9aec98-fa25-3585-b57b-6282f5d60f7e | -11.4397 | -45.0923 | 2025-07-08 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 479b4056-fb7e-3553-92d0-193319ef5bc2 | -8.92182 | -69.32958 | 2025-07-08 06:22:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f427b3bc-9dbc-3008-a277-91ec6fc51b1b | -8.92124 | -69.33371 | 2025-07-08 06:22:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04fdc435-a2ac-39d0-97ec-5c525ab9ea8e | -9.43015 | -63.45809 | 2025-07-08 06:22:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ba0dc47-1ad8-3138-b0c7-6c54fa9ed640 | -11.4393 | -45.1154 | 2025-07-08 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b2de674e-f2bb-346d-a3e1-eea3c1da275f | -11.4205 | -45.095 | 2025-07-08 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| def291fc-23e4-3b05-8f5b-65590f24a4da | -11.4397 | -45.0923 | 2025-07-08 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f85a4443-c876-391f-8875-c06bc7e98a33 | -11.4393 | -45.1154 | 2025-07-08 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 13d59ee8-ef04-3bcc-98cb-8690f1eb7adc | -11.4397 | -45.0923 | 2025-07-08 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 9c32e7cc-10f4-3eb3-99c9-010fa3c02145 | -11.4205 | -45.095 | 2025-07-08 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 04af7f54-a0e6-3198-ab30-328cce16c2f2 | -8.92084 | -69.3293 | 2025-07-08 06:46:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cecc2433-a5d3-3aaf-b39c-4db42280e516 | -8.92014 | -69.33501 | 2025-07-08 06:46:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66e66974-92e8-37d5-bd5f-eee6335aa05c | -8.17628 | -72.9224 | 2025-07-08 06:46:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3979a212-c2b8-317a-9448-f8c86f6186fe | -8.17671 | -72.91925 | 2025-07-08 06:46:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24b1b511-af74-3630-a8b0-9a73309b522f | -10.6299 | -49.4504 | 2025-07-08 06:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |


[Clique aqui para ver as próximas entradas](README21.md)
