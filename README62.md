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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e685fded-6426-340d-b48c-73fa405b5f92 | -7.82286 | -55.12941 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b483676-1cc0-3727-b8b0-cc49da13693c | -6.00621 | -47.39677 | 2026-09-28 05:29:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35db44d2-6562-3e89-8468-4a8e0ddb6900 | -6.89067 | -59.8459 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff36ed8e-ffea-3dde-a6b0-1ecc7128c5d1 | -10.00616 | -50.12588 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 88062d63-a58b-3379-968b-c1596c483587 | -7.68948 | -54.76581 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a5718e0-795e-3def-b3d5-d9a7c2eca3c5 | -6.86401 | -59.88506 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84ba6ff2-9c29-34a5-bb4d-e867978edb56 | -10.00587 | -50.13254 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6cf93c7d-8400-39da-a17c-08c9d13b1a2e | -7.82224 | -55.14216 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7bba0ca-7960-3980-a0b5-6d22b1d5e4d3 | -7.82546 | -55.14203 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cb4723e-15c7-3268-85fc-60c01edfa75d | -6.89401 | -59.84642 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a480ccd-2699-389a-8270-ac83341801c2 | -6.64028 | -59.94767 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc9c2b3-c556-3f6b-bd9f-6824fc418d84 | -6.64749 | -59.94519 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72e254ed-cbf0-39f2-aacf-28abeb500b4d | -7.83085 | -55.13469 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71d5922a-2b3f-31d4-8d5c-d8f50b4b03c6 | -10.20822 | -49.99549 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1884eb05-eacb-3d3a-8104-2584f5a63865 | -6.07919 | -57.8313 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e75b83-a915-3d10-a471-22d03c1912cf | -8.59877 | -54.65038 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17df7fce-2b10-3437-9ea0-4f8f784211ea | -6.08477 | -57.7949 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2899dd82-0bce-3b29-89fc-d396d12cb755 | -6.07161 | -57.8095 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b4f6d3-5515-316e-9aca-94911ab8810f | -10.21816 | -49.98134 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08b94a65-4589-30b2-913f-f15d842fe40a | -6.86012 | -59.88806 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81df9df1-9425-3d28-8ef5-9a61061b24b6 | -5.99928 | -47.39581 | 2026-09-28 05:29:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 31c1541d-2609-35d8-8309-96f5a4b837e1 | -7.81973 | -55.12959 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa8e61a1-4745-378f-a3ee-eb2f8b6a546b | -6.64306 | -59.95168 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46df893b-b9c0-3247-aba4-b2af26ff290b | -9.97741 | -50.15628 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 54b30f05-e561-3711-acbb-aba71da042d0 | -8.66368 | -64.03172 | 2026-09-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d2a4ae9-02db-3d86-81af-1764ecf661ca | -11.07605 | -51.40373 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54755d78-c26b-376f-bcd0-e3f5aab63c87 | -7.55843 | -61.36058 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 259e1af1-f277-3a76-a0d4-d5c354129ba9 | -6.06853 | -57.82966 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36f1bf04-5532-3b93-9ecd-94b6aed62623 | -10.23502 | -49.99852 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b64bdd44-a552-35d5-ab59-97fda9cfcd56 | -10.88999 | -50.68618 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3ead1cc-a831-39e2-a2ad-21fb9d215042 | -11.10958 | -51.32618 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a96e9f23-ff5a-3e9e-8ef7-856483f1581d | -7.50338 | -55.02117 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fb64e31-0277-33ba-b869-8159a049535d | -11.11326 | -51.34186 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebeaf40b-1534-3358-86de-16b8ea01fe6a | -6.63973 | -59.95117 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f39bf2ac-c560-31d4-881c-c6693a6176e7 | -11.10642 | -51.34936 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 781b3e38-7f07-33c8-bfb9-d5d2bb98b158 | -9.98531 | -50.14269 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b9f258c8-47d7-3075-8e64-93180e70bce9 | -9.07503 | -61.43723 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e990070-5812-3d21-87c5-fa539ba822a6 | -7.82283 | -55.13817 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f48f7799-2baf-347e-9704-8fc3de50ca3f | -5.97683 | -57.69668 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6a4aa17-61db-37a8-8e20-52681fd6b627 | -7.55899 | -61.35711 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29e1b64d-3236-3ee2-9b80-67eade554b6b | -3.96395 | -59.34335 | 2026-09-28 05:29:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffab82c4-7db5-39d7-979e-109d1f802331 | -7.82602 | -55.13805 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac068a3-7b58-3f21-a0cd-be0869d50ff3 | -11.11483 | -51.3295 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba4f343e-3b06-3d42-ac71-efa85cac8aa8 | -6.7837 | -59.37296 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12310f90-95e4-3a69-8c7d-19c0e8b0b695 | -10.20999 | -49.98064 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d427037-0570-3a38-b0c2-b6e0d7a44ccc | -9.97684 | -50.16107 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 007fce89-d7da-3dad-9e37-e107688c6cf8 | -10.80334 | -48.73589 | 2026-09-28 05:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6ad12805-e51e-31bf-9d1e-62379796163d | -7.46591 | -55.00771 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db6183b1-adaa-3ee3-9d16-640577603321 | -9.97873 | -50.14859 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de495711-152e-39db-8b6a-26ca66176da3 | -6.89456 | -59.84289 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6802160e-db23-3cff-bde0-af6f78d58429 | -9.16505 | -61.40469 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 4d44c2dd-6692-3aa3-9e4c-d38558d0f00f | -7.27905 | -55.57908 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16b69760-a582-349c-83ea-63334775f4ee | -10.9359 | -50.67572 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2457dd65-af83-33fa-b438-2a2753407c5e | -10.41671 | -53.82198 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a07805de-f65e-39de-bb0f-05f7937ae783 | -9.60529 | -61.81938 | 2026-09-28 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88b6840c-a69d-3ce1-b817-541fb2372a98 | -11.08234 | -51.40039 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cdd6149-0a75-3503-a896-e5e36de0f387 | -6.8768 | -59.89066 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9e02893-5dd7-3ee6-812e-efeae96b4f5e | -9.78451 | -59.78214 | 2026-09-28 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21a93bbf-ac23-3d88-8e18-c0ff8971c932 | -7.82174 | -55.13742 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 091a04e5-1994-386f-b61b-49eea442a47a | -6.69488 | -59.96664 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c121952f-e6a0-320e-8c8f-ecfab759da44 | -7.71953 | -54.77441 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0084eb28-202e-3011-aad7-1d14190d2a70 | -6.06205 | -57.8245 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a0f090-ef36-36a3-9cbb-4a5e0d07b174 | -9.99969 | -50.13176 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a132026f-2506-3201-bc13-5ea76ec07d08 | -9.16781 | -61.4087 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 86ab32af-391a-3363-8932-b6bce6e8245e | -10.79664 | -48.73433 | 2026-09-28 05:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c8a37cad-c30e-3e0c-9c69-492e207e92fc | -10.2219 | -50.00187 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8f2b197-d461-3995-8bae-1ae21e1d1bc6 | -10.25606 | -57.71647 | 2026-09-28 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 694b4e75-4504-3060-8082-1a737f73e118 | -8.03346 | -54.90072 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84c2fbf8-d1b4-30fe-b192-e17a6251fcab | -7.49907 | -55.02072 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 343420aa-e62e-3a45-bab3-66d57f61857f | -8.03467 | -54.89229 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3b00285-740e-30f6-922a-f36f650b74f9 | -5.30388 | -55.83157 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f29ab9a-6a75-333b-ab50-9d31fadfd7b5 | -6.78485 | -59.38787 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 177de5e0-de8e-32a4-a590-abeef5523f04 | -7.55893 | -61.464 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1392b465-90f9-3527-9ce8-cae015b0d98a | -10.22315 | -49.99201 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d48a3c7a-fb69-39df-935e-53947b25a1c9 | -10.21388 | -50.00125 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 319fa5b1-f1ef-346d-b41e-a33d308fa0ec | -9.08275 | -61.45274 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0f84e75-4778-30a1-8518-6b1a53c99e79 | -4.98154 | -56.15283 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dfad36d-fd8b-3546-83bd-e14a95c10510 | -7.28316 | -55.57973 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ea1a515-9003-3949-8d2b-ac4bbb9799ba | -9.99998 | -50.12507 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e86d503c-bdd0-3d53-b399-07371b860e4a | -6.07995 | -57.80259 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e42fc803-6bb6-3834-8a60-a2c5ecef64e4 | -10.89199 | -50.68397 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1c6c9f9-baed-3cf4-8371-7f75e7c181ab | -5.72344 | -53.45401 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b19b36b8-3be6-37d7-aec1-91d6212281a4 | -6.78259 | -59.38015 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ed842b-c390-3074-bd00-b80daef7e494 | -7.82118 | -55.14142 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c25e1bfe-50c8-3cdd-9fe4-b851fab662e0 | -9.13857 | -47.98873 | 2026-09-28 05:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a06a1ac3-29aa-3e44-8409-17422f116ebe | -7.93982 | -61.52539 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0908d4c-734d-329d-9552-0fe27138e120 | -11.06977 | -51.40707 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d3c438e-3f1e-32e9-bd0f-460750838ad6 | -9.97799 | -50.15149 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c20491d-be01-3b1d-b8ac-24ca1182e467 | -6.64639 | -59.95221 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db677538-02ba-392e-a3e8-e67834b3633f | -10.41113 | -53.82672 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c25c1c46-ffa7-3d0b-86b2-a3b15f1ea237 | -6.78652 | -59.37708 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4550639c-37df-325c-9788-cb56ced7050a | -10.40699 | -53.82056 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4309429-ac26-337b-8648-ed332b5f0069 | -10.21629 | -49.99612 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58b39c58-de33-3729-a16a-df5127a73cb6 | -7.83029 | -55.13867 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47362dee-9fff-3bb6-9c55-8fb1219b3e43 | -9.99264 | -50.13389 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 56d5f85d-2a6e-3e8d-84cf-9f672d479c6b | -11.10712 | -51.34681 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65281355-276a-3e58-91c7-944d1d4e4578 | -6.7854 | -59.38427 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4c30fa3-6df6-3c1d-b795-b9c086d8f327 | -11.10663 | -51.35094 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15dfa7cc-0e49-3c85-ad9e-d40ea9f64726 | -11.1085 | -51.33289 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27a9e6c7-3d6e-3d78-a902-be3bfa27d6de | -6.64694 | -59.9487 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README63.md)
