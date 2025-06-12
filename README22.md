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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19428a24-29a4-3376-9e9d-8409193151d7 | -9.2487 | -57.53932 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fcfb22f-c506-380c-b129-b49b947c1e33 | -13.8975 | -54.64831 | 2025-06-12 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 69b56d5b-1189-3b17-9a56-bd4cab55f667 | -12.70972 | -58.03473 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 750e6c56-4107-3894-bb5d-58634ecba534 | -11.13867 | -53.95066 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec463033-155e-3fba-a6eb-3fe7182ff64d | -12.7124 | -58.02933 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e57690be-3074-3242-913f-f3ba58c4bf15 | -12.70577 | -58.02436 | 2025-06-12 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5b574d5-2be3-3ef9-b134-fc2c4cdda48b | -12.22703 | -55.52479 | 2025-06-12 05:44:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b02c0c6c-0e58-3d5e-9aae-7107542a2491 | -12.43647 | -54.87344 | 2025-06-12 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0a7312b-9445-319a-9c7d-6b537dec7b13 | -10.88766 | -54.75787 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ebc6a7c7-99de-3d10-b3f6-5e9d57f374b8 | -13.71507 | -58.67893 | 2025-06-12 05:44:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a91d7e9c-beb6-3b6e-a9b8-be501630ed50 | -9.83807 | -62.8854 | 2025-06-12 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd5703ca-37e4-360c-aa59-76e34a09226a | -14.03202 | -55.13121 | 2025-06-12 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c33a4e2f-b817-3e1d-afd3-10ff650b4b9c | -11.77002 | -54.37885 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4917e276-8e00-31b6-8f43-29d61df736bb | -9.24951 | -57.53333 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f9a3b8c-36b7-3be3-9870-b284f8507981 | -13.71527 | -58.67647 | 2025-06-12 05:44:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18c0169f-3c95-3905-ade3-5351b372c73b | -11.7771 | -54.37396 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf0aa7ce-b9d8-399f-a4c9-cc7715f2ccba | -11.9988 | -57.20988 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 060ce429-02f9-3703-a09e-2b2eca511cae | -10.29853 | -57.13745 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dde254bc-ee84-34fc-ab9c-946cb955d3ce | -10.09997 | -64.9625 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f177b7f-2c53-3568-a63a-fb71f978102d | -10.88143 | -54.75696 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b27ccc54-3d9e-36e1-822e-dc322204b7a9 | -11.37675 | -55.11244 | 2025-06-12 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 190344f7-c521-3c4e-9250-f40b6521913c | -11.7764 | -54.37399 | 2025-06-12 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70e53575-9b5d-35e3-81b3-d6f46755b880 | -13.28898 | -57.07001 | 2025-06-12 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fdbf000-13eb-3816-a576-36d16d2efa26 | -10.88822 | -54.75301 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 98d34cb6-d710-37c6-ab2d-5ec6c67556f0 | -8.75758 | -64.80238 | 2025-06-12 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba24a284-9343-338b-9b23-da7da46fc394 | -18.66311 | -55.72892 | 2025-06-12 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bec649dc-3b69-31ce-a488-d98aea77c2c9 | -20.73628 | -56.65848 | 2025-06-12 05:46:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 558c8db8-e56b-352d-ac53-ad6e588e88f0 | -21.83027 | -56.26569 | 2025-06-12 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d368b38-aca7-39c7-bfe4-2a092ca6e5d8 | -20.72851 | -56.66216 | 2025-06-12 05:46:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26cda272-a0cf-3ebd-a0ff-d890678e4391 | -18.66262 | -55.73444 | 2025-06-12 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 71bc8cb0-9d8d-35a3-9aed-b8390bcd93d2 | -20.73518 | -56.6573 | 2025-06-12 05:46:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 403f9917-3bb9-3d82-92cf-6d79758017c6 | -20.73015 | -56.65685 | 2025-06-12 05:46:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 41f21b00-653f-3036-8828-75520c9d62fa | -20.72904 | -56.6557 | 2025-06-12 05:46:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0b4178c-526b-3e2b-9ea5-d6c230b9072e | -9.87424 | -61.40192 | 2025-06-12 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5878956f-969e-3089-bd95-94cf09be4198 | -9.6355 | -67.26665 | 2025-06-12 06:10:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1503df98-775f-34a2-b142-c36417582bac | -11.83619 | -60.91844 | 2025-06-12 06:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23f68c6f-935f-3c1c-ac40-b35c3857d80f | -9.18055 | -61.86718 | 2025-06-12 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d75f5f6-456e-376b-8c18-73be21018296 | -11.83558 | -60.92372 | 2025-06-12 06:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f16de43a-ae79-38e7-b792-827a6b0828fb | -9.87482 | -61.39728 | 2025-06-12 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 107f1284-2c3e-370d-9f84-c13b70afc3b0 | -9.18108 | -61.86305 | 2025-06-12 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ea14e97-1244-30f0-8691-046a87582154 | -20.0965 | -50.8638 | 2025-06-12 08:00:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.0 |
| 9fc755e7-5fd3-3622-8979-98ca8cd9d96a | -20.0965 | -50.8638 | 2025-06-12 08:10:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| bb44e645-731e-3289-8bd0-b8e4dc0eb826 | -20.0965 | -50.8638 | 2025-06-12 08:20:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| d12a17fc-323b-39e5-aea4-f2ac1af24b22 | -20.0965 | -50.8638 | 2025-06-12 08:30:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| e19b6528-e850-3406-a633-4ab4ab1a0557 | -20.0965 | -50.8638 | 2025-06-12 08:40:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 311acc65-a3f1-3209-a488-6186614c2ec0 | -20.0965 | -50.8638 | 2025-06-12 08:50:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 1a5545db-fd7c-384c-88fe-9d59504badb4 | -20.0965 | -50.8638 | 2025-06-12 09:00:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.7 |
| 551646e7-6bba-31f9-8544-aa68766c4398 | -20.0965 | -50.8638 | 2025-06-12 09:10:00 | GOES-19 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 8ac510bf-8cb1-3ec6-9e50-fab0812209d8 | -8.7996 | -45.0815 | 2025-06-12 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4a72c59f-aa0f-329d-a6c0-5815ac193c10 | -8.7996 | -45.0815 | 2025-06-12 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| e099f0f8-d50b-3c86-ae8e-2aeeae80691f | -8.7996 | -45.0815 | 2025-06-12 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 7610b257-09a0-3447-babd-71358eac06b5 | -8.7996 | -45.0815 | 2025-06-12 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| f744ab41-2d4c-3517-a74b-c4d1ad9eefe2 | -10.8694 | -54.3151 | 2025-06-12 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a1daada5-314b-34af-8145-5be018b088e4 | -8.7996 | -45.0815 | 2025-06-12 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| bacf5d7d-c65c-36d4-8c13-af06c4a5c767 | -10.8694 | -54.3151 | 2025-06-12 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8fcf0eed-f3ea-36e6-9364-04ca2f64a6c2 | -11.5775 | -44.8645 | 2025-06-12 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fd2de3d7-554a-3e42-81d8-5938ea929a56 | -8.7996 | -45.0815 | 2025-06-12 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| d9d09bc8-f688-3afe-baf3-d396bdb7e2d5 | -11.6179 | -46.9767 | 2025-06-12 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| aa6564b0-37ea-3b3f-8759-62778193b11a | -10.8694 | -54.3151 | 2025-06-12 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 72047b17-3cdb-3b99-8947-8debb5255afc | -11.5775 | -44.8645 | 2025-06-12 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 44e8048c-aeb3-301f-ba4a-eb3588867a91 | -8.7996 | -45.0815 | 2025-06-12 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 73ce6a82-9a4b-365b-997d-76ea11214091 | -11.6175 | -46.9992 | 2025-06-12 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c53daa73-4784-3c95-93c2-3857cede8bec | -8.7996 | -45.0815 | 2025-06-12 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| db16fe88-efb5-328b-b314-20cdd2db1ba3 | -10.8694 | -54.3151 | 2025-06-12 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 82789f48-9a94-37d0-a9b9-949fbf8c146c | -11.5775 | -44.8645 | 2025-06-12 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| f5c4228a-dcb7-3042-8a4b-810b3585ca35 | -13.9059 | -54.6291 | 2025-06-12 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 3c731772-8176-3d41-9725-f1a9bf59f249 | -12.5238 | -58.3378 | 2025-06-12 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cb78eab3-d58b-32d6-823c-600370960030 | -11.5775 | -44.8645 | 2025-06-12 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9eb78450-3ef6-3d90-84bc-e1ba51bff798 | -10.8694 | -54.3151 | 2025-06-12 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 89a78010-129f-36cc-8194-31213543b9f2 | -11.6175 | -46.9992 | 2025-06-12 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d2bd5b01-4261-3f45-a1ba-d7b443345fa4 | -11.6179 | -46.9767 | 2025-06-12 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 6fa36b3a-a088-3c7e-a097-9a4d3a004d72 | -8.7996 | -45.0815 | 2025-06-12 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 4baf4d81-8454-3b01-b87e-7232e5c23dc9 | -13.9059 | -54.6291 | 2025-06-12 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| ece48525-473a-32eb-af09-5851ff86151e | -13.726 | -45.2421 | 2025-06-12 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6aa23d38-692a-39cb-b2bc-a2e750abd3a9 | -12.5236 | -58.3576 | 2025-06-12 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| bec77bbc-4e2a-3c7e-bfa2-2b4fbd712798 | -13.726 | -45.2421 | 2025-06-12 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 71afa7d0-0b12-37d2-b52f-8860f04f4643 | -10.8694 | -54.3151 | 2025-06-12 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| c9c09caf-49d1-3136-9b8e-e77f0a98c0fa | -13.9059 | -54.6291 | 2025-06-12 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| c235d7ab-e31b-33bd-8478-8d55e4e620df | -12.5238 | -58.3378 | 2025-06-12 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| cf6a20bf-ccb8-30b5-bde2-dd2537654ee9 | -8.7996 | -45.0815 | 2025-06-12 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| ad6fb5f9-78a3-3554-8bb5-0e16f4965b2a | -11.5775 | -44.8645 | 2025-06-12 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0572d899-8905-3a78-8d9c-255e670be5a0 | -8.7996 | -45.0815 | 2025-06-12 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| eceda8e2-bce2-3b64-bf8d-c338d3a0b6a6 | -11.6179 | -46.9767 | 2025-06-12 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 29e037b2-10e5-352b-aff1-201ef8552aa8 | -12.5236 | -58.3576 | 2025-06-12 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ca41337e-b62f-328e-b30c-2949b1da8234 | -13.726 | -45.2421 | 2025-06-12 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 42ceb07c-c55d-3425-9cdf-b6f8a90c3fad | -10.8694 | -54.3151 | 2025-06-12 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 815d0f70-9cc3-36cf-8e01-1dba7f1937d1 | -11.6175 | -46.9992 | 2025-06-12 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f047e2d3-c32d-32c9-9a98-e521d1731f98 | -13.9059 | -54.6291 | 2025-06-12 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 4374ad75-8be3-3c2b-8bf6-d7458e3f557f | -12.5238 | -58.3378 | 2025-06-12 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 20babe56-22cf-3569-bd74-29e56138b40d | -13.9059 | -54.6291 | 2025-06-12 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 01c0fdd0-6307-3a73-8ffa-a182b42c6b94 | -12.5175 | -57.2231 | 2025-06-12 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2aeff649-271a-3861-bc46-7f0101c76bc3 | -11.6175 | -46.9992 | 2025-06-12 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b6f6b70b-b14b-3b63-9825-707363f49433 | -12.5236 | -58.3576 | 2025-06-12 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 24db3e96-a7b7-33e4-8e7e-457fa88655f7 | -8.7996 | -45.0815 | 2025-06-12 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 44520543-54b4-3c88-98d8-cb322373e0f7 | -12.5238 | -58.3378 | 2025-06-12 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 289.1 |
| 00416ebe-ed1c-33b3-9b13-18fd6eed9bea | -13.8867 | -54.6312 | 2025-06-12 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 71a0eab1-8d2f-3114-b3e1-60b449a2878f | -10.8694 | -54.3151 | 2025-06-12 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 7ed45935-6d79-306a-91c0-d8faa782331f | -13.726 | -45.2421 | 2025-06-12 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| cfdd6fac-6b7d-35eb-8d45-1cb9b583d5d6 | -11.6179 | -46.9767 | 2025-06-12 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 33ffb2c6-cbbb-39b7-8691-9a36a84113f9 | -13.726 | -45.2421 | 2025-06-12 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |


[Clique aqui para ver as próximas entradas](README23.md)
