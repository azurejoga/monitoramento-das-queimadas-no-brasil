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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d71b1c54-7516-3c7d-b761-8b6456910949 | -3.1968 | -42.6255 | 2026-10-07 14:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 3070ff45-91c8-3647-aac9-dee6751b9e56 | -11.7139 | -43.6757 | 2026-10-07 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4857690f-e3be-3e81-b7a0-132391b10533 | -10.8591 | -50.6692 | 2026-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 078892b2-5d10-39ee-9d87-acb4cb105135 | 3.1098 | -60.5943 | 2026-10-07 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| eab9bc5a-8755-33b4-b3e3-ba83affcf78b | -9.3394 | -65.4638 | 2026-10-07 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4337e154-8360-34dd-99f4-e89270a44534 | -8.3022 | -44.1467 | 2026-10-07 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b2fecfe4-dd4e-36a5-b7a5-89dd72efd585 | -7.5847 | -55.7205 | 2026-10-07 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 8db05017-1081-3432-8909-0d124d6b690b | -7.5571 | -46.6906 | 2026-10-07 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 11a7f16c-3ed2-3ec5-bb97-f886fd948450 | -9.3619 | -45.4288 | 2026-10-07 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d736ff98-27f8-3af6-b9c4-241d0872e05a | -11.014 | -45.4272 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.3 |
| c703f06d-a074-3dbf-998f-4a9f6dc05e1a | -6.2162 | -52.7876 | 2026-10-07 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 28e8901c-3900-346a-808a-e80b1e3471b6 | -7.8789 | -72.3492 | 2026-10-07 14:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 113.7 |
| a9dd9018-afda-3731-bfdc-ea27151b0284 | -8.9054 | -63.3378 | 2026-10-07 14:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6d2d628b-95ce-312b-9f72-4edb683ab5b0 | -11.1545 | -46.1597 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 5741ff1e-0419-32e6-b40a-903539a3e8c2 | -8.6033 | -45.6709 | 2026-10-07 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4fef6a37-6480-3d2a-9b96-3d7fb727f127 | -7.5849 | -55.7005 | 2026-10-07 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 46d1ba1a-0343-3f87-917e-2b609ef88a3d | -11.0646 | -45.8312 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 2860339f-c154-3603-814b-ba9432cc6fe7 | -7.89 | -54.7206 | 2026-10-07 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 832df0a5-f73b-32df-8b4b-5f15171702c0 | -11.0833 | -45.8514 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a20c126f-12bb-3c1b-8ed6-513e927483de | -7.5568 | -46.7128 | 2026-10-07 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 25388c14-8ee2-325e-818e-af18c05ceba3 | -7.5756 | -46.7112 | 2026-10-07 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0fc3cdb6-450b-3f0f-8f6d-4160158a3af1 | -8.5238 | -54.619 | 2026-10-07 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2d554154-1223-3031-b6de-ebab777b89c2 | 1.9681 | -55.8792 | 2026-10-07 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e6eacb02-3bea-3e28-9211-4bee5dca032d | 1.7671 | -55.5661 | 2026-10-07 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 77e679ca-6dfb-36ee-b370-ca267df798da | -11.3745 | -46.6948 | 2026-10-07 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 238.8 |
| c8b27b54-b1c6-3606-9b5c-8e1778cabe86 | -10.8989 | -46.6667 | 2026-10-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c802f0eb-5606-3d38-b3e9-be25b0a8ab32 | -7.5849 | -55.7005 | 2026-10-07 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 899a25af-11d1-3823-8afc-8f1248215fc3 | -11.7139 | -43.6757 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 0b488d66-fc9a-304f-b7b2-61fffabd8550 | -12.2132 | -44.6991 | 2026-10-07 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 384.2 |
| a40f4412-9751-334c-9100-99803a94d481 | -12.2136 | -44.6758 | 2026-10-07 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 30a3d14b-8af1-3962-95fb-7acec837479a | -7.8973 | -72.349 | 2026-10-07 14:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ebfd8d80-b12b-3119-b15c-110157e522bc | -7.8146 | -45.5009 | 2026-10-07 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 83d07fce-003a-397d-93b4-4361f7e6cec7 | 1.7671 | -55.5661 | 2026-10-07 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f6ee1ce8-6ecd-3ed0-9e75-441ea38c2fe3 | 3.1463 | -60.5937 | 2026-10-07 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d040f12c-4ef5-38ac-b2b9-2803cf9ed670 | -7.1813 | -55.1237 | 2026-10-07 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0be24121-5773-3dce-ad76-54ff70189eb1 | -4.3471 | -43.8021 | 2026-10-07 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f28ea88e-d107-35b6-b9f7-4e5f5e2e09c6 | -7.5571 | -46.6906 | 2026-10-07 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 29c534b4-e433-3e49-b31c-ca90cfd9762b | -10.9949 | -45.4298 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 115efa16-bb14-3bef-96d5-21092703e5b7 | -11.6181 | -43.6669 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 42296337-7013-38d8-a6ae-6f6f1072ac62 | -11.7362 | -43.5068 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| ed6fb289-f4ff-3a07-b4a7-ddada75659fc | -11.2295 | -46.2403 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 6961411a-f68c-339d-b896-2fecc636dec6 | -7.5284 | -45.8885 | 2026-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 827a6c71-2e73-33c1-8efc-d7800b22518b | -9.4492 | -44.6167 | 2026-10-07 14:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b64c0ee4-f415-3da6-b4f8-4df3d2c5855d | 0.7266 | -51.3749 | 2026-10-07 14:30:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a71569ce-5f9b-31b4-9c53-807a0015372d | -7.89 | -54.7206 | 2026-10-07 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d813f3fe-9a52-3635-a421-15a6eff24b46 | -9.4509 | -45.8271 | 2026-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 257.0 |
| e85d8469-6933-3430-8086-7315a1eb414e | -11.1545 | -46.1597 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 248fb964-f0f5-3ade-888a-da1ecaffcbec | -7.8789 | -72.3492 | 2026-10-07 14:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 316f5cb8-c615-3db3-9fa3-70c660c0ad53 | -9.1363 | -65.2835 | 2026-10-07 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 404e8692-ff42-313a-8c7c-88e4b4ef2bdb | -10.9953 | -45.4068 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 698ef98a-0bbc-3c7b-acbc-9a9c43649739 | -6.2053 | -49.3826 | 2026-10-07 14:30:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 462e840c-f33b-392c-be0b-6b48c5cf4efa | -9.4513 | -45.8044 | 2026-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 083c6e3f-2cfa-353a-b9aa-938a1c2481ce | 1.5283 | -56.0227 | 2026-10-07 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| aa40ca79-2335-3b03-8691-64f9bac67bf7 | -11.0867 | -45.6459 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| f5742fa9-38ee-3fe8-b2aa-b42fff2bb821 | -12.1554 | -44.708 | 2026-10-07 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 09ab8245-e951-306b-a129-e4bde0dcb568 | -6.7037 | -44.0248 | 2026-10-07 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| f3b57ac1-59f0-35f7-808e-93529dd0a13a | -6.65 | -43.7749 | 2026-10-07 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 377ec15c-aef9-3c03-9d8c-21bcad3f18af | 3.0916 | -60.5567 | 2026-10-07 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3bc2c456-5ba7-389e-adec-a3e262754af1 | -11.7143 | -43.652 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| f62c2658-b10a-3266-9942-23dc451352ad | -7.47 | -42.8078 | 2026-10-07 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 6851b44c-672c-3793-9a1f-12a9560f039c | -1.2455 | -49.062 | 2026-10-07 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| e043a30a-e5be-35b2-bff2-381b657ba647 | -9.1362 | -65.3022 | 2026-10-07 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| b1f16cf6-d457-344d-bc78-93697e27af7e | -7.3935 | -46.2144 | 2026-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 688d6833-862b-3b2a-abd6-b6ab04e1d6db | -11.7335 | -43.649 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f994760f-bcf3-31f2-9f8e-930c024f5a18 | -6.217 | -52.6851 | 2026-10-07 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| cd9e8524-352e-39e9-a3e7-0e0fd1e8d585 | -8.5844 | -45.6729 | 2026-10-07 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| cb427167-0900-3eb2-8b28-6b2845576401 | -10.9762 | -45.4094 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 52b90379-5387-3c09-a2dc-af705455c485 | -7.8679 | -44.1922 | 2026-10-07 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bae12f51-2d36-3d2d-b864-368f5e269c47 | -6.2158 | -52.849 | 2026-10-07 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 264.7 |
| eed69853-b9ef-3f75-a60b-4837d92ded2f | -9.4124 | -45.8767 | 2026-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 22714dab-13ed-3937-b7ed-00025e9b38d8 | -3.526 | -43.8444 | 2026-10-07 14:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 25e29c84-b23b-3613-bfff-42c0fe2bf57c | -17.5269 | -45.4622 | 2026-10-07 14:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 182.8 |
| e7795847-add9-3b50-acc6-ce9d8b79fabf | -11.7751 | -46.7082 | 2026-10-07 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e3a320f5-1b47-32de-9055-e26b565f7bd0 | -7.5756 | -46.7112 | 2026-10-07 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 081c05d0-a251-3e7b-8c2c-04a03bbe853a | -11.6951 | -43.655 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 558d65bd-c34c-3e73-9c1a-b0e553083eeb | -4.3154 | -42.9904 | 2026-10-07 14:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 688f7632-fb14-3b62-853f-672566fa2b99 | 1.7121 | -55.6063 | 2026-10-07 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7c9bdc9a-7604-3a5b-8972-530d8bed8eb0 | -9.343 | -45.431 | 2026-10-07 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 2f01364a-0a50-3da9-bc09-0be508bdd5d5 | -11.0863 | -45.6688 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 7eada37b-2a41-366c-b4a9-f1064d342fae | -11.8315 | -43.5391 | 2026-10-07 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 290.4 |
| e3e95adc-e393-35fe-9292-eeb47a9d3bd3 | -7.5847 | -55.7205 | 2026-10-07 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 0fb89b12-ec8c-3aff-ba2b-a55d06d317b8 | -8.8364 | -62.4321 | 2026-10-07 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 870f513f-4f26-39ad-b40b-a15e14a76d70 | -6.9925 | -45.1223 | 2026-10-07 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 64f07435-ad45-33f5-8055-7aa970a6436c | -5.9838 | -40.9123 | 2026-10-07 14:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 398.8 |
| 25f855cb-c18f-3ea2-9b85-cdb72b8f97c8 | -8.5238 | -54.619 | 2026-10-07 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2c6b95b1-c78a-3016-bc3d-7e2229408ef6 | -11.1556 | -46.0916 | 2026-10-07 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 076c829e-dfcf-3b4f-9f57-e18578da4b7f | 1.5283 | -56.003 | 2026-10-07 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 660990cf-0a22-3567-902d-99e6edb9bde0 | -7.2179 | -55.1817 | 2026-10-07 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 222d9c6f-a6f8-31c3-b64d-5b19f7839cab | -7.2 | -55.1026 | 2026-10-07 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| da3460f1-24bb-36e8-810d-79f647ec0913 | -11.3745 | -46.6948 | 2026-10-07 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| f8f0d120-15bd-3a40-be60-490364d00557 | -11.0935 | -47.6019 | 2026-10-07 14:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 16894935-17e9-348a-9259-6c04e700fecb | -7.8789 | -72.3674 | 2026-10-07 14:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c69166b9-e2dc-3e65-b4c1-94583ff2f994 | -6.2159 | -52.8285 | 2026-10-07 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 315.1 |
| 6304c618-2100-326d-9588-009df474377e | -11.3742 | -46.7173 | 2026-10-07 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5ffe4b79-59a5-305e-bb76-cb56020ab07e | -11.7943 | -46.7056 | 2026-10-07 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ab01776f-d3d2-384e-bf8a-b5613fa64411 | -6.1974 | -52.8295 | 2026-10-07 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6bde604f-9cb9-3c3e-9899-b841f34c8202 | -7.5568 | -46.7128 | 2026-10-07 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e6fcbf48-9dd0-3396-9fb3-47b5a3eeda71 | -9.432 | -45.8293 | 2026-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 382.1 |
| aaf81cd8-04cf-3aa8-bdb5-1f9866f9aedf | -4.3152 | -43.0138 | 2026-10-07 14:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| aa4940a4-df6f-30ce-933a-4625e55ebdb0 | -7.2884 | -47.2885 | 2026-10-07 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |


[Clique aqui para ver as próximas entradas](README134.md)
