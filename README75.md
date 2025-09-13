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
| f6554146-9bc8-37c8-bf38-cd1de5625d46 | -3.22589 | -47.13183 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 593fcc91-6927-3aaa-8f58-362ea34d48b5 | -8.09515 | -50.18549 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4a2eb9b-254a-3cee-8679-133e5c46ef2d | -4.92309 | -55.7747 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2e4152f-96e7-315d-9e41-cd4c9e500af3 | -3.23213 | -47.63041 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea1a7344-12a0-33d2-8b11-6fb4ee3c703a | -5.20544 | -44.31527 | 2025-09-13 04:57:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 740a8ef8-08d5-3ff3-ba4a-02f6dc7fcb17 | -3.81198 | -52.08727 | 2025-09-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13572626-f363-3c43-af79-4f45f01bee67 | -9.97392 | -51.71659 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a1e69a5-3dc1-3bb8-8aa8-eb39466e2831 | -8.03925 | -52.32708 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cdd89f2-c33a-37b5-becb-e01e36e1f6c6 | -8.30186 | -44.87988 | 2025-09-13 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b33f8de-489b-30c2-8815-228e07b43427 | -9.49926 | -50.90009 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daac3d9a-aaa6-3d34-a100-435b110276d6 | -9.25651 | -51.24566 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8527b212-954d-3ad5-afcc-aa32f555658c | -9.238 | -51.25416 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5c97a62-6414-3633-b902-2c0686f4f35b | -7.41439 | -44.35948 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b41db042-4bfe-35b8-845c-02c52c9ef732 | -10.34052 | -48.82508 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fc3ac08-7d1b-319d-9deb-2e87d8487d18 | -10.3401 | -48.82657 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23b663ce-5599-3326-b918-93f9dd893c3b | -9.24845 | -51.26035 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b107ef4-709b-39c1-91ac-d3e69cd22b33 | -8.42387 | -55.63169 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab6f8eee-9cd8-3b9d-be6c-7bc5c6c238e3 | -7.4194 | -44.35227 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bde276a-89a1-3fbd-8f5d-4258bddaf01a | -3.22354 | -47.62912 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| dc2f4cef-2291-3584-bb1f-6322b6868e3e | -9.01247 | -45.76408 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb693abc-87bf-3a27-bbe5-a16f924b7f23 | -8.30691 | -44.88495 | 2025-09-13 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c54d4b5b-d205-310e-b216-dda90992544a | -9.70238 | -47.52911 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1aaf614-af0e-38e6-b022-b63bb6398a96 | -7.43002 | -44.41759 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b20a3ca-3f4c-392f-bb2b-aa14191e1c31 | -9.24655 | -51.26235 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 69541bb4-1733-3d3d-833d-2337843d719c | -6.25103 | -43.47757 | 2025-09-13 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5054e2b0-5e9c-36a8-92ba-c16c5fb69f5e | -9.90353 | -51.88672 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75ce152c-9917-37da-81c4-bce9385a622f | -6.10664 | -45.94592 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86c9a410-18cc-389a-931e-1725eb325a6e | -9.79128 | -48.89455 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad30488b-b508-33f4-ac8f-c395272f2f9b | -9.24408 | -51.26424 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 17a7eede-c438-33d8-b5e1-d9ea2231cc95 | -10.12114 | -45.50591 | 2025-09-13 04:57:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1bb8e5d-b59d-3450-b852-368d0b3234ad | -2.50756 | -51.82278 | 2025-09-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48f3c80d-75fa-3c48-a331-35c911714b5e | -6.74445 | -51.92533 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ceca1dd-e5da-3fa8-9357-a67ee33bf4c8 | -3.86241 | -55.9947 | 2025-09-13 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91fb23af-ea85-3758-8577-7d2eb55317ac | -8.10438 | -50.17696 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a230559-32a5-31bb-a3fe-cd94e6d9515e | -9.90231 | -51.89494 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15f3ed73-cdb8-3b2b-88ef-fa76f37b9aa0 | -10.32744 | -48.8208 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16898f3c-a692-3f31-a233-d4cff8e07830 | -5.71527 | -46.44666 | 2025-09-13 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a73ccfc-6d9a-3cf5-956f-b9ace27c5e42 | -5.09724 | -56.15953 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d6ad12f-d01d-3372-be6f-c4d441c79b15 | -8.10298 | -50.18636 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86c5facd-a7c8-3690-b2de-d9520934dae5 | -9.19706 | -45.78135 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5417f7b3-ab27-32b6-bb07-740b93bc88f9 | -7.2541 | -44.5952 | 2025-09-13 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0586ce0e-b958-387f-9237-6b974513dd4f | -10.32362 | -48.81596 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 723dc356-2dc4-3438-908c-b0a6b5c4912e | -9.05848 | -45.81714 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27faa866-196e-31b2-a0cf-f6f4620993f4 | -3.86395 | -52.39024 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53df9ba5-1728-3d25-8095-362e9a57f91d | -9.89005 | -46.4561 | 2025-09-13 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3551253-e0fc-3261-9792-493225828b3e | -9.90843 | -51.87864 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f13e68b0-8805-3d8d-bd3a-7fc90dadb7b5 | -7.4137 | -44.35133 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 261d5e11-5a3b-35bc-bb0c-d7656c516fd5 | -3.48582 | -48.43515 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c442e2ac-7539-386e-940d-484b2d16b1d7 | -3.79828 | -47.57878 | 2025-09-13 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2d31324-cc0f-37b3-a201-16de49ff4730 | -5.95021 | -42.77466 | 2025-09-13 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2d3a91f-e750-37fe-82d6-36c9c5d96caf | -9.95203 | -51.68711 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6a380b2-067d-3b22-9abd-aab8d2b35337 | -9.80074 | -48.90073 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b86c437a-3b23-3228-8879-3fc25b38d813 | -7.31573 | -46.5872 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1a4b3111-78d6-38e8-b9f9-1f422f24e1f8 | -3.22723 | -47.63382 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| aec23a72-5e5e-3eae-8368-87c1faa71964 | -3.22293 | -47.63318 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 37fa1033-8e99-3432-b5ea-82faa00521ef | -9.01204 | -45.76728 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 79d0b7ef-86cf-3b59-a138-169f4eca3190 | -8.43719 | -55.63361 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c0a7c9d-c1f2-3ed3-8f06-fff34621ee68 | -7.52481 | -44.37668 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 093f6ae9-3819-3c06-be30-1c27f34a560f | -7.41543 | -44.35148 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30a944c4-1ff9-38fd-9a80-28ea64506b5c | -9.03761 | -47.05967 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b059a935-d3b4-3b20-92e6-67a35f990aca | -8.50405 | -47.31586 | 2025-09-13 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 964368f0-efd3-3e75-b362-490651083ea9 | -7.43727 | -44.40664 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d33b79f7-cee1-313b-84b3-945c3e2556d0 | -6.56099 | -44.7752 | 2025-09-13 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a397616-049f-37d1-a95f-caae24c531c3 | -9.71262 | -51.00262 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41768a76-fee5-35cd-adb0-5e84400c04a9 | -3.63706 | -49.20533 | 2025-09-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb223770-f8e3-3bb7-b480-4f4015dca497 | -2.71401 | -49.44185 | 2025-09-13 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d9be8b2-224b-3104-abdc-71d631bfb3d9 | -3.80117 | -48.64006 | 2025-09-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbdbc28d-37d6-3e3e-baca-2abdac332e18 | -9.23081 | -51.22573 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b1b1898-c435-31f8-90d6-e9abf50ae388 | -9.01161 | -45.77049 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 45982fb3-f707-348b-bfd1-fea7501da20c | -3.24149 | -46.7826 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 41577457-2f62-377b-911e-98fdeebcfc13 | -6.28525 | -44.23875 | 2025-09-13 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9490e8e5-92b7-3bdd-847b-719191654437 | -4.92931 | -55.77941 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9231794-145d-3a9d-8330-47db749d0ca9 | -9.05805 | -45.82041 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e605e270-961d-33db-b879-bca7d33d7de5 | -6.25404 | -43.47614 | 2025-09-13 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aad62951-7feb-3855-b2d2-269eb6925dca | -7.32144 | -46.58227 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8ee5b6b-95ba-3fa7-86ad-f57d56d184e5 | -10.01957 | -50.3834 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a98131b1-e8c6-3225-9e9f-b98661a2ea29 | -7.42061 | -44.35641 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07be40fc-822b-3c9e-b5b1-e55ac70669a5 | -9.79732 | -48.89329 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 709ae2bc-cb90-32cc-907f-d56836d8a0cc | -6.56052 | -44.77861 | 2025-09-13 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fec44a1-36b8-3e91-b603-7ded37c8a690 | -3.21926 | -47.62838 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7274d76a-957e-3570-9d9d-e7858a9852c5 | -3.23099 | -47.12817 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4351d075-81ad-3220-a6e2-4ce3cffa6f55 | -3.90752 | -59.6539 | 2025-09-13 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a45978a-f200-35ff-b44f-4194f98eec28 | -7.52296 | -44.37514 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5255b775-9f90-3800-8ef5-bf6607d3ac47 | -9.91079 | -51.88757 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f02f46f3-dc94-30bb-b4c5-74a85e5abc88 | -7.66828 | -61.1694 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eac9b18-c63b-3bc2-a0f0-d3d4c035e95a | -10.33688 | -48.81747 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38775197-745b-3e75-8d71-1fb8fdc80cfc | -8.86483 | -52.00803 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a9d7ea9-d0d3-3cd6-b883-8d2bdd4c0e43 | -9.02722 | -47.06297 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 044d684b-3008-3ec8-ac69-aca104c0277f | -9.90292 | -51.89085 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55871eba-2b66-392e-b1eb-46a4058d6d8d | -8.09099 | -54.74371 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8794216-5bc8-3906-9319-f1c35b0e9030 | -9.79411 | -48.90586 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abed7144-2ac9-32f0-a978-682f8ee173d9 | -9.79681 | -48.89705 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24ae7e47-cfc2-3e9c-a976-de335e6eda66 | -8.10167 | -50.17289 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b96bf39f-fe2c-3d1b-b372-63b03848748d | -9.79096 | -48.90758 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9a124ef-168c-3728-a494-49714d737c03 | -9.81821 | -48.9025 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7569575f-d512-35ba-bea1-e62beeb15558 | -6.10243 | -45.93941 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5ad369c-87d4-3166-a7c6-07539c73cc02 | -3.21767 | -47.12603 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4f72603d-453f-33d8-afa0-ed6a798e1a1d | -9.7859 | -48.90131 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82e41c7f-3460-3490-9b99-366b73498b9f | -6.42708 | -43.32388 | 2025-09-13 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4b01c34-787d-3f17-9f81-cb85ad968db7 | -7.32745 | -44.60319 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README76.md)
