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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe9f0f1f-9a37-3606-9129-686593fe733c | -3.91876 | -47.71537 | 2025-09-15 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c2dfea9d-c8ea-39a2-8aca-2fd639ffb0e2 | -3.65653 | -54.05849 | 2025-09-15 00:35:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 75bef87b-609e-3a94-b0c8-8851239debd3 | -3.85774 | -51.3372 | 2025-09-15 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d0ab9c67-0094-3a48-9753-a337da671552 | -2.794 | -48.63836 | 2025-09-15 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a59aba43-7f81-31b3-81f0-4c7dbe569a46 | -3.91747 | -47.70609 | 2025-09-15 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5b3a1e4e-5fc0-339f-b9a7-f8848a0a1e8c | -15.7981 | -53.4793 | 2025-09-15 00:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 575c1478-5c1e-375b-8a4a-76cdc8551a7d | -17.3442 | -42.6333 | 2025-09-15 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 1ffdd3ad-c36f-3317-9de5-d900be4e6764 | -7.8564 | -43.5896 | 2025-09-15 00:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 280.8 |
| e0878afe-c0b4-3ecc-82b8-dc614bb4582c | -12.1668 | -44.0988 | 2025-09-15 00:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 9738c456-32f8-3ace-a711-8de04359ea02 | -12.9103 | -54.7352 | 2025-09-15 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b5f09205-b5ad-3e98-aaca-1003b30e7172 | -12.9791 | -47.9713 | 2025-09-15 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 35b566e0-132f-3768-b3cb-082e36bd3ad1 | -12.9294 | -54.7333 | 2025-09-15 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| c77215fd-597e-3090-a1a5-0d64a33eb220 | -7.8942 | -43.5857 | 2025-09-15 00:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 311f3c1c-19f6-3361-8b84-8c95d383b21b | -12.006 | -47.7505 | 2025-09-15 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 53fb3f12-bcd7-35f4-afdc-74f3ea1e3849 | -20.371 | -51.2335 | 2025-09-15 00:40:00 | GOES-19 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 209e8ee7-a46e-3915-9d3a-c45e16456d8e | -12.9984 | -47.9685 | 2025-09-15 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a98b98ba-1746-365f-b075-316596b127b9 | -5.7047 | -49.1998 | 2025-09-15 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 606ed6c5-e6d7-358e-9bd6-13b415e5b2d0 | -15.4816 | -49.6271 | 2025-09-15 00:40:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 45deb667-e522-3803-8d12-fbb2882d21f8 | -7.8756 | -43.5643 | 2025-09-15 00:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 225.6 |
| 2fddd196-f73f-305a-8c7e-7ba28f449491 | -15.7985 | -53.4582 | 2025-09-15 00:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 201b0ad3-746b-39eb-abab-7997e6de32c2 | -7.8753 | -43.5876 | 2025-09-15 00:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 297.7 |
| 0754146c-3c58-339d-9031-18bd3c1e7df2 | -15.779 | -53.4608 | 2025-09-15 00:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8d7fec39-ac11-381b-858b-13c93bc7a50c | -7.8567 | -43.5662 | 2025-09-15 00:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 496f5a69-4e14-3b74-a0dc-c10644a287fd | -7.8756 | -43.5643 | 2025-09-15 00:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 1341a05b-3cc1-3dc6-9819-55f277cc3eda | -12.9103 | -54.7352 | 2025-09-15 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 80775393-8e08-35f1-92d1-550865c82685 | -12.6633 | -54.6988 | 2025-09-15 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 325a3e1d-9b04-35f7-9336-284b0d5be9ec | -15.7985 | -53.4582 | 2025-09-15 00:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 154.0 |
| a63c9d10-8771-3cc6-b49a-97ce21e6ec6c | -7.8861 | -63.7135 | 2025-09-15 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 288698c7-4c92-37bb-b093-abc7a88755c6 | -15.7981 | -53.4793 | 2025-09-15 00:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 6ebeaade-103b-3eba-bbfd-c1d6d7335ded | -7.8862 | -63.6947 | 2025-09-15 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d7f2c54b-a4d7-3879-ae5c-17f4948725fb | -12.1663 | -44.1224 | 2025-09-15 00:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 64cc7a53-a400-32ec-a7f6-bcef0aaf65d6 | -7.8942 | -43.5857 | 2025-09-15 00:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 0f0b9a46-4c7f-3454-acb8-ece05b7e9b98 | -12.8204 | -47.1896 | 2025-09-15 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f3fea0b9-8db9-33da-bb09-cdfd9e62f855 | -7.8567 | -43.5662 | 2025-09-15 00:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 330.8 |
| 57664252-62b2-37ec-85c6-cf1d5df0694e | -12.6636 | -54.6782 | 2025-09-15 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5c861ee6-2b45-30f8-b17c-6307f0bdb73c | -5.7047 | -49.1998 | 2025-09-15 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| c5a1d84a-f9c8-3f80-82de-284ba5d71e8e | -5.6861 | -49.2009 | 2025-09-15 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| e62be5b5-6dac-3f6c-956d-92490cb41529 | -12.1668 | -44.0988 | 2025-09-15 00:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 240.7 |
| 2b2cc4e2-805c-3ab9-8332-0ed38cc99a4f | -17.3442 | -42.6333 | 2025-09-15 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cfaf9eae-589d-39d1-94e0-a56e5913647b | -7.8753 | -43.5876 | 2025-09-15 00:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 80e20b90-bca3-37c8-9706-d424f12a4072 | -7.8945 | -43.5623 | 2025-09-15 00:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2eaf34c7-3ec6-304d-856c-6b44d1c1d7ba | -14.6405 | -52.0454 | 2025-09-15 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 03c99871-e98c-3ad1-8cc8-acdc4e6daa99 | -12.9294 | -54.7333 | 2025-09-15 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 00dbd7cf-f14e-3aed-924d-f94663fa0e44 | -7.8564 | -43.5896 | 2025-09-15 00:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 368.9 |
| 53957a0e-aa24-32a6-8b1b-cd3c9bb7789d | -12.006 | -47.7505 | 2025-09-15 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 36b63aab-23be-3671-8d81-a865706ce91f | -20.371 | -51.2335 | 2025-09-15 00:50:00 | GOES-19 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.4 |
| 46032c76-4b3c-3944-8881-ab4f96b29d1b | -11.78 | -47.5583 | 2025-09-15 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a35679f7-5f9a-36db-b0e2-9ef37a8eeb4b | -15.7985 | -53.4582 | 2025-09-15 01:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 27528856-5b47-3f2f-8ee1-c91a74f0e5aa | -12.1672 | -44.0753 | 2025-09-15 01:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 44874d61-1740-38d7-8215-cdccf51a86e6 | -12.006 | -47.7505 | 2025-09-15 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c1d8d189-ab5a-3d8d-a626-13588206943f | -17.3442 | -42.6333 | 2025-09-15 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a0ccb7b0-5558-3f5d-bf16-68a030ee32cb | -12.6633 | -54.6988 | 2025-09-15 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 05f3ec59-7c10-309e-8fdc-f3c0e71cc8e6 | -7.8564 | -43.5896 | 2025-09-15 01:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 437.5 |
| e48e9d2e-d1af-3037-8e48-0c3ee647f0ee | -5.7047 | -49.1998 | 2025-09-15 01:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 24523959-ab8e-3a16-adcd-b4c6efe347be | -7.8567 | -43.5662 | 2025-09-15 01:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 420.6 |
| ba16b51a-d41c-372f-994b-63b14fa579f7 | -15.7981 | -53.4793 | 2025-09-15 01:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b366611c-edc7-3c30-af93-83ae21a71bcf | -7.8942 | -43.5857 | 2025-09-15 01:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 8a6a1297-8961-3b40-b719-10445ad531d6 | -7.8945 | -43.5623 | 2025-09-15 01:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| a3a7c0d2-fe43-39b1-9660-046528379b29 | -15.779 | -53.4608 | 2025-09-15 01:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 3487d236-16cf-3660-9f47-f5b4b3f47924 | -7.8753 | -43.5876 | 2025-09-15 01:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 307.7 |
| 5cfa3946-c356-38c8-881c-3ae86433219b | -17.3435 | -42.6581 | 2025-09-15 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5356ed69-a03f-3e3a-a76b-905f8df83298 | -12.1668 | -44.0988 | 2025-09-15 01:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| aac55ddb-3b95-3b32-9498-1b0010f37056 | -20.371 | -51.2335 | 2025-09-15 01:00:00 | GOES-19 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.8 |
| c990dcd1-fcb5-3e64-86da-d4c1746ffdcd | -12.9294 | -54.7333 | 2025-09-15 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 33aca116-02c0-3081-944c-c17f413acc4d | -12.9103 | -54.7352 | 2025-09-15 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 1ad9c096-1a03-3885-9ee9-846bd5de6705 | -7.8756 | -43.5643 | 2025-09-15 01:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 358.1 |
| 648536ea-52ec-3e76-b008-4dc2cf176e3c | -7.8567 | -43.5662 | 2025-09-15 01:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 525.9 |
| 14621cdf-5aae-3d7d-b4ae-daf6e2e71d41 | -7.8756 | -43.5643 | 2025-09-15 01:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 458.4 |
| 6fcf2396-9448-3df0-a26e-8082149de39d | -7.8753 | -43.5876 | 2025-09-15 01:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 427.3 |
| 9f9844b4-f76b-3b3b-b6c4-cb398a45e707 | -15.7981 | -53.4793 | 2025-09-15 01:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a35f3bb6-22d1-3a44-8b29-37e8d31d4460 | -7.8564 | -43.5896 | 2025-09-15 01:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 599.7 |
| 89b7b385-368f-30dd-b3eb-ec16465fdc2a | -15.7985 | -53.4582 | 2025-09-15 01:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f033c30e-a4bb-3dc4-96bc-65af67ba7b20 | -17.3442 | -42.6333 | 2025-09-15 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 1f3a2304-12fa-35f5-b641-5d8c9e7de6af | -12.9103 | -54.7352 | 2025-09-15 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 274de190-162d-3053-a2e4-987dcc64f736 | -17.3435 | -42.6581 | 2025-09-15 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4a5496b3-7242-37ac-893d-2a4822a5b5c0 | -12.1668 | -44.0988 | 2025-09-15 01:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 258dd13d-8d2d-3fc9-8cbf-3c80521623df | -12.006 | -47.7505 | 2025-09-15 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c9b0eeef-46f9-34ac-b723-d0dce8392979 | -7.8942 | -43.5857 | 2025-09-15 01:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 85518c88-54c2-36b3-8b41-6ba30438e724 | -12.9294 | -54.7333 | 2025-09-15 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 683872ff-3a68-3c4b-86b3-3dc4518bfe2f | -7.8945 | -43.5623 | 2025-09-15 01:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 242ed915-f9d7-3609-a62d-42ea754da716 | -17.3435 | -42.6581 | 2025-09-15 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 46cab195-658f-3b10-b9a2-0287a453311b | -7.8756 | -43.5643 | 2025-09-15 01:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 486.4 |
| 54123919-6a01-362d-9e24-0314d49a148b | -12.1668 | -44.0988 | 2025-09-15 01:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 37d7835c-89f7-3c43-b62b-cdde940daa17 | -17.3442 | -42.6333 | 2025-09-15 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 0b5b53d7-0bc6-39b5-9558-da68174539c6 | -11.8297 | -50.4548 | 2025-09-15 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 40b5e912-cc26-3952-bed2-cfd6182c6182 | -20.371 | -51.2335 | 2025-09-15 01:20:00 | GOES-19 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 0c4de81b-2e7e-3138-b10a-c4eb1f402f36 | -12.1861 | -44.0958 | 2025-09-15 01:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 35790385-0893-3708-b1ac-368915ec1d85 | -7.8564 | -43.5896 | 2025-09-15 01:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 533.9 |
| 6b83c6a0-7e55-357d-81e4-af7aa77d9f12 | -15.7985 | -53.4582 | 2025-09-15 01:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 130.9 |
| b2f58fb7-8a46-39f3-8851-f844232a8c40 | -15.779 | -53.4608 | 2025-09-15 01:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 91db421b-f4f3-3be3-a8fe-c5d006989cfb | -12.6636 | -54.6782 | 2025-09-15 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 02330da9-38a2-3cb1-b254-c5c2eb0a48ac | -12.1663 | -44.1224 | 2025-09-15 01:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d9951888-f168-32c9-b89a-118d68366a67 | -11.7919 | -50.4378 | 2025-09-15 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d6483c48-b9a2-38be-96e1-5b00c0f6fec4 | -7.8753 | -43.5876 | 2025-09-15 01:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 460.6 |
| 346ad5a2-2f4e-32db-bf84-2b77712345ac | -7.8562 | -43.613 | 2025-09-15 01:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 48807993-db02-3df3-b905-021dff1eb6e8 | -12.1475 | -44.1019 | 2025-09-15 01:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a9483374-100b-37f7-9bf8-a9bc51fdc48d | -7.8942 | -43.5857 | 2025-09-15 01:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 202.9 |
| dbfe72f9-bf47-3631-8d09-71844dc3fa58 | -11.7916 | -50.4592 | 2025-09-15 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4fe1adb9-cd60-34fe-842a-aed699f1de3a | -11.8107 | -50.457 | 2025-09-15 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d2d81ae4-9485-3325-9ce0-9fc1d009411b | -7.8567 | -43.5662 | 2025-09-15 01:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 435.0 |


[Clique aqui para ver as próximas entradas](README7.md)
