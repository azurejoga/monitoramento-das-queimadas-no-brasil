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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 303fe616-c011-3c22-9f7a-3637932111ce | -8.34404 | -45.98072 | 2026-08-04 06:08:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 89cc4007-cea0-37fe-9da7-31ec74e22d3f | -8.3544 | -45.9897 | 2026-08-04 06:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 72791998-13df-329b-bd71-a294b8dbd787 | -20.0888 | -45.28415 | 2026-08-04 06:10:00 | AQUA_M-M | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a558605a-e531-364e-a449-1781c6765a04 | -20.10233 | -41.42828 | 2026-08-04 06:10:00 | AQUA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 6a7996f4-53bc-3fb2-9c10-cd97eef068a3 | -8.3544 | -45.9897 | 2026-08-04 06:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 99765fa6-d27f-3513-b151-91ffa2e2dabd | -8.3544 | -45.9897 | 2026-08-04 06:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| f218b1ab-4335-39f2-84fa-ce595fb226e5 | -8.3544 | -45.9897 | 2026-08-04 06:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| f4fe6981-505c-34b7-b4d1-d1c0a28ea456 | -8.3544 | -45.9897 | 2026-08-04 06:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| da5bd883-0809-34bb-94f3-bd4964407a25 | -8.3544 | -45.9897 | 2026-08-04 07:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f984ae6b-9f39-3d97-8d6b-d7c63ebeb8f9 | -8.3544 | -45.9897 | 2026-08-04 07:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 1fd5fc45-bcee-3ed6-9c58-99c5fad73eb0 | -8.3544 | -45.9897 | 2026-08-04 07:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| fc5f15a6-1316-3eaa-b56c-57b9eb15c2da | -6.56592 | -55.15117 | 2026-08-04 07:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ac85301b-a4b8-3508-ac5c-0fee54d6753f | -8.3544 | -45.9897 | 2026-08-04 07:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| d5c445ee-48f5-3712-b39a-5a443c016ed0 | -11.2213 | -54.855 | 2026-08-04 08:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| f73f740b-3ef2-3740-bb84-d72966466cb2 | -8.3544 | -45.9897 | 2026-08-04 08:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 12da5904-7bc4-344c-8e20-404554edfc83 | 0.3179 | -65.8191 | 2026-08-04 09:10:00 | GOES-19 | SANTA ISABEL DO RIO NEGRO | AMAZONAS | Brasil | 1303601 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 79ebb57a-7acb-3c29-a55a-0c5747ab1826 | -13.63684 | -42.88355 | 2026-08-04 11:02:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c3c80ce2-0ea8-3f9c-8f98-2f0e8a5a1fe4 | -19.32524 | -40.5746 | 2026-08-04 11:02:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 1ecc7918-95f3-3d48-bde4-043e5658cfcc | -19.32333 | -40.58647 | 2026-08-04 11:02:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| e7eb6ddf-5f5d-37df-81fe-b82207d0b9d1 | -19.24251 | -40.5774 | 2026-08-04 11:02:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| bf86bd98-39a3-3b73-87e5-d1c344355861 | -19.48631 | -40.47316 | 2026-08-04 11:02:00 | TERRA_M-M | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 58fdd6fe-af5f-3398-a961-858b47779c9c | -17.9695 | -44.577 | 2026-08-04 12:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 245.6 |
| 7f873c6e-cdff-3a89-ac4b-7620e1f8618d | -17.9695 | -44.577 | 2026-08-04 12:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 152.5 |
| f79b90fa-01c0-35c6-967a-4f0b5646f958 | -14.2687 | -45.2636 | 2026-08-04 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d798deb5-3bf2-33f1-8c83-63c3d2f30152 | 2.52896 | -60.3592 | 2026-08-04 12:34:00 | TERRA_M-T | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04e4966d-6bcd-37e6-8064-72c8a189d09a | -3.09265 | -49.34209 | 2026-08-04 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 64aa8794-cc1b-30f0-bd4e-0eddc865d2e5 | -7.2424 | -59.45051 | 2026-08-04 12:36:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 33e83a97-5d4f-387d-88ed-f0451df4758a | -6.5788 | -51.11466 | 2026-08-04 12:36:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 1904f338-4f1f-3d66-85d6-e5b1d383f45b | -11.23023 | -54.85978 | 2026-08-04 12:38:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 75f22cb9-f932-3f5a-b263-1cb19309cde4 | -10.02381 | -59.34601 | 2026-08-04 12:38:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ab6e6235-e60a-3ecc-868b-1aeb0af7f0c9 | -11.73696 | -57.82006 | 2026-08-04 12:38:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ac6efdeb-8707-3cb9-b129-f334bd2e275f | -11.91626 | -57.41015 | 2026-08-04 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 6c49fdba-d7f9-3a90-aabe-e039973ddf2f | -11.76691 | -50.29387 | 2026-08-04 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 75d59e40-fcae-3653-90bb-62b601a4b835 | -11.76374 | -50.28659 | 2026-08-04 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f4ae6d5a-1dbe-3504-8f15-3f80df325fb6 | -14.2687 | -45.2636 | 2026-08-04 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 4b6d9364-8875-38fe-a691-c8c104cdce1f | -16.064 | -60.16462 | 2026-08-04 12:40:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2613c3eb-abfa-3fea-8f54-044bac205e42 | -16.06531 | -60.15513 | 2026-08-04 12:40:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a03e8a6d-8af5-3cd1-80c1-64ffefaeaa7e | -14.2687 | -45.2636 | 2026-08-04 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 6f45e501-fd69-318a-a769-421286e62876 | -6.0376 | -45.0634 | 2026-08-04 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4fdb851f-ad83-30d5-ab54-9f63d7736a18 | -8.9491 | -45.202 | 2026-08-04 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b5d26e88-b0a6-391f-adb4-6350710751ff | -14.2687 | -45.2636 | 2026-08-04 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 16accf1a-06c4-3361-8e5e-be1670f36959 | -11.5666 | -50.2494 | 2026-08-04 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 734d0fa2-f2a1-370f-a3fe-8d29112d7780 | -8.54 | -47.749 | 2026-08-04 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| c799fcb5-8ef6-36dd-9001-30c8ff938e3a | -8.9491 | -45.202 | 2026-08-04 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 638a6f82-5058-3588-8be3-476881ff310e | -14.2687 | -45.2636 | 2026-08-04 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 8b688419-4234-3caf-9584-d06c647fb657 | -8.5588 | -47.7472 | 2026-08-04 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e26dc033-706b-39c4-9f82-f08b3f83f09c | -6.1672 | -45.2123 | 2026-08-04 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f8855008-7bfb-3962-9aa6-afea9590ee60 | -3.6639 | -49.4686 | 2026-08-04 13:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d87d415b-c343-3a81-910d-8b4d2613dcc7 | -14.2687 | -45.2636 | 2026-08-04 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 596829b9-3c6f-3c33-8b82-face2e8aa3b6 | -11.5666 | -50.2494 | 2026-08-04 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2ca0dd75-1139-3897-a0d5-75b13aa1b1c5 | -8.9491 | -45.202 | 2026-08-04 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.2 |
| af1e59c9-03ce-36fd-a283-d86c2f6e8194 | -9.9401 | -53.3293 | 2026-08-04 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ffa5fe21-48a5-3f27-b797-9ffb32fff1b8 | -3.6639 | -49.4686 | 2026-08-04 13:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 66cb5f89-950b-3fba-842c-9a55a9e10f0c | -14.2687 | -45.2636 | 2026-08-04 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| e66ddee6-834c-31e0-807b-8281614e8deb | -8.9491 | -45.202 | 2026-08-04 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 069d458e-ae8d-39ed-8cdb-3f952c6c892c | -11.5666 | -50.2494 | 2026-08-04 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 265b1f9d-1b36-3ff6-aa17-c98dc34603c6 | -8.9302 | -45.2041 | 2026-08-04 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| eeb44ae5-ea2d-37a9-93dd-4e5df4376e39 | -11.1279 | -50.4057 | 2026-08-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f6c67c82-4791-3cb3-9f6a-ca7bbf22d66d | -3.6639 | -49.4686 | 2026-08-04 13:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 609243c2-43cc-3361-a711-a8082169c057 | -8.9491 | -45.202 | 2026-08-04 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 23f12e73-c500-3817-9c4a-2fd4b60e20ac | -10.8121 | -65.091 | 2026-08-04 13:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6a355937-db42-3f34-8b50-b00fed80b5f9 | -14.2687 | -45.2636 | 2026-08-04 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1273adad-006c-39bb-8141-150f412f3252 | -8.3544 | -45.9897 | 2026-08-04 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 176c4614-6b9a-378c-b50a-5f960a619a71 | -8.9302 | -45.2041 | 2026-08-04 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c5475d88-3ae8-3605-826a-68aa25d3fbf3 | -9.9401 | -53.3293 | 2026-08-04 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 207.9 |
| 1ec49264-ceaa-3e96-8606-b9b9bca4b3ea | -14.2687 | -45.2636 | 2026-08-04 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a74e8af1-bbea-33db-89ba-1087ff2bdde6 | -6.0372 | -45.1088 | 2026-08-04 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d34292f4-e645-3c58-990f-4c50af5cc802 | -3.6639 | -49.4686 | 2026-08-04 13:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| dee344e7-d464-341b-8027-8c8349887be1 | -8.3544 | -45.9897 | 2026-08-04 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fd17e14a-d6c9-3e45-8fc5-78e0205f2e75 | -11.5666 | -50.2494 | 2026-08-04 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5f5cbfdb-bb1b-313b-bbb2-36ab86e22986 | -9.9213 | -53.3308 | 2026-08-04 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 024a3884-33c5-3c4e-a29a-f475f02169f8 | -7.6288 | -45.3145 | 2026-08-04 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2e8f7e0a-d7d5-3d3b-9767-c2f28f130543 | -10.8308 | -65.0902 | 2026-08-04 14:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 152daa8c-f5ca-3508-a491-a4567a611fb8 | -3.6639 | -49.4686 | 2026-08-04 14:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 2fd1c34d-11cb-3b49-8876-15d7cf671da6 | -14.2687 | -45.2636 | 2026-08-04 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| dccf9d8e-0dd3-321e-8900-1585602cf325 | -11.1279 | -50.4057 | 2026-08-04 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c84c98e0-ec53-302e-90fc-99dda23ca9ae | -11.5666 | -50.2494 | 2026-08-04 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e4b4385e-d3ff-3fed-b404-a8b98478d97e | -14.2687 | -45.2636 | 2026-08-04 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 65dbd184-279b-38b7-86d4-26612ee1c0bf | -11.1279 | -50.4057 | 2026-08-04 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1b280e8e-fb69-3d2b-a351-126fe0d71ac2 | -8.9491 | -45.202 | 2026-08-04 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 948ddc66-1387-335f-a4f0-f7acff8b0533 | -11.1162 | -49.8923 | 2026-08-04 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 74a7c225-525d-3601-865b-7f1ed9962452 | -6.5514 | -55.1569 | 2026-08-04 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 75fb3a7d-d679-34cb-8381-8bec33f541b2 | -11.1159 | -49.9138 | 2026-08-04 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| d4c25a8f-a42f-3168-96a1-34ca42c7f5a1 | -8.3544 | -45.9897 | 2026-08-04 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 83dbf314-620a-3411-a7b8-95408b6830f4 | -10.8121 | -65.091 | 2026-08-04 14:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 03fe5f3a-b4de-303d-8215-f535dc7c1c9c | -6.5699 | -55.156 | 2026-08-04 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4236a1f6-b1f9-302c-8476-f7c7e6e4fc76 | -7.6288 | -45.3145 | 2026-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 3dbe0826-b0a7-37d9-bf17-330e7bbd3b58 | -8.3544 | -45.9897 | 2026-08-04 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d352f378-dec2-38ac-8fdb-60709f88cd4b | -3.6639 | -49.4686 | 2026-08-04 14:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a95de42c-d29f-3a4a-98ff-3b75931a6274 | -4.3874 | -43.3827 | 2026-08-04 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 85593e41-d279-3019-aa4d-9cb608d2a7dd | -11.1279 | -50.4057 | 2026-08-04 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2b77bd12-23a6-3e02-b247-b6a0d0192c90 | -11.1468 | -50.4036 | 2026-08-04 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 95b1357e-464a-370d-98a3-7cfe35f64e42 | -8.9491 | -45.202 | 2026-08-04 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5d12ad73-19d7-3dd2-8268-a1d630676249 | -10.8308 | -65.0902 | 2026-08-04 14:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| aa745447-f396-3fd2-b2ac-3b3d811f5b39 | -10.8121 | -65.091 | 2026-08-04 14:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d06b73a8-a846-3b8b-a7c2-cffaf49a7124 | -8.9302 | -45.2041 | 2026-08-04 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c94fc7df-f072-3589-8674-e2ebb9362050 | -6.5699 | -55.156 | 2026-08-04 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 55558421-41e7-3432-9402-50d6dd40decd | -6.5514 | -55.1569 | 2026-08-04 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2d502435-9125-3312-93f0-ab42af711335 | -3.6639 | -49.4686 | 2026-08-04 14:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 678c3985-aee6-3068-b2d9-2b34d4ff3da8 | -14.2687 | -45.2636 | 2026-08-04 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |


[Clique aqui para ver as próximas entradas](README17.md)
