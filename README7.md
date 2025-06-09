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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3cbec2e-e618-392a-897c-5e908d001bf4 | -11.38634 | -56.55271 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ed0b940-ab39-3e75-a15f-076af58baecd | -10.49295 | -53.66622 | 2025-06-09 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be20e215-b757-30df-8b67-902324125ada | -12.3516 | -57.42745 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a219bf58-f90e-3d94-8e41-8bd38bdf5a8f | -13.65799 | -47.7726 | 2025-06-09 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a989222-1463-3b37-a3c1-49978a3f057d | -10.36278 | -57.50537 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62aba82d-4514-3615-b861-3fbea2c9b2cc | -12.37619 | -57.40485 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b42ab4e4-e197-3a4e-a979-8fe6b6024968 | -13.00585 | -47.11383 | 2025-06-09 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1b653a3-fd88-3c5d-bbca-78c704ba610b | -10.93505 | -55.32012 | 2025-06-09 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1257ab7-b4e5-3e65-b011-e05c357f04e9 | -12.16131 | -57.72927 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb61d141-12e9-3efe-a56d-ab400707804c | -15.07842 | -48.94513 | 2025-06-09 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32b26c86-511a-39a4-84c2-31c1400dda54 | -11.383 | -56.55217 | 2025-06-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db01024b-f61a-340e-a441-19b692904235 | -10.29674 | -57.13611 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d502527-8528-3ff4-a8bb-dc10ad79b8d3 | -11.13921 | -53.94715 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 399cc045-74d2-373b-8ddb-2f7b6d4e4bfe | -12.36819 | -57.41117 | 2025-06-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1143bf16-0225-3b54-9127-62920cb0ca69 | -11.7877 | -54.77764 | 2025-06-09 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21c6b9ba-b087-36eb-9b2c-28f3ee861cfa | -10.9345 | -55.32361 | 2025-06-09 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d85b69e-e43d-3556-b219-d901295399c0 | -11.87563 | -56.06894 | 2025-06-09 04:59:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d226e35-5c6e-3052-be58-46fd83b0dfa5 | -10.83899 | -53.77465 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66f961b8-657b-3d49-b70b-e35b3ed57623 | -11.14078 | -53.91393 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46ed718a-3672-333d-a2f5-9ac85e51341a | -14.23938 | -45.47248 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8df0ddc2-2674-34c4-8b33-481d1ebf5cdb | -13.01283 | -47.86696 | 2025-06-09 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a47019b1-a9b1-3770-ac0f-e4bb80d8e238 | -10.74405 | -52.50904 | 2025-06-09 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b58e4ad0-f840-313c-9bda-ed489fea634f | -10.95478 | -54.37808 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e0ecec0-10e3-3384-a02f-94eb30427d4f | -10.85474 | -53.78455 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b5b099-200f-3c88-a554-46ad86d25004 | -10.81465 | -56.95395 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8efd4351-fc41-31a8-a9e2-c6f565a9b903 | -13.55679 | -44.19639 | 2025-06-09 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9693d844-c9b1-37f9-9869-57536e401501 | -14.02902 | -55.12635 | 2025-06-09 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 872d6f1c-9f3a-3ef2-b991-adeb0553200b | -10.84464 | -53.78298 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 18f7c72a-c8b2-38f9-8484-688bfa67b59f | -11.13796 | -53.90976 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a681466-7b22-339d-a8c8-7b427211ee9f | -10.85138 | -53.78403 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d11c1d64-5ecf-371b-9bc7-48ce2ea5b094 | -10.36624 | -57.50594 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa54cfb6-8a79-317f-98b9-79509e7db950 | -11.91666 | -54.82375 | 2025-06-09 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3ac69bb-f84b-3475-8b52-b241de444152 | -14.2571 | -52.46883 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f215fdd-705a-34d4-b858-55caaaa8d649 | -12.16067 | -57.7331 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 305013e2-21a2-3a75-8874-af3a1d11979b | -10.8542 | -53.78819 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7235c07a-c060-32ad-bbd0-143c1afb75ba | -15.56963 | -47.8546 | 2025-06-09 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8091dc1c-f980-3d9e-89ce-686141a29e24 | -10.85584 | -53.77727 | 2025-06-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 66ce431b-e6d4-3665-ae1e-545ea7477045 | -14.0379 | -55.13514 | 2025-06-09 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6681fed2-b886-38d3-9e9a-4c9b84bb5592 | -14.25342 | -52.46832 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f1984dd-911d-3cbb-b0f0-0fca67990c28 | -10.36342 | -57.50152 | 2025-06-09 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0a0bf68-846f-396b-abfc-a35cc640b4df | -14.25084 | -52.46494 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c11dea1a-6d03-3557-9e76-b6fb390812a5 | -14.25452 | -52.46543 | 2025-06-09 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b9159cb-c11b-3aaf-9409-716d910c9029 | -14.23844 | -45.48092 | 2025-06-09 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1980a43-117a-32a4-820a-aa86466e50e5 | -19.02516 | -57.62154 | 2025-06-09 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| abdb3e62-7f15-3ef3-a1ea-e24eb71a8f53 | -20.58167 | -44.5771 | 2025-06-09 05:01:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| def9ddf9-1363-3a22-a0f6-bd0bfd484515 | -4.48704 | -43.77082 | 2025-06-09 05:14:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f3556fa3-b0cd-3512-9d1c-87b52ba0a681 | -7.00475 | -44.61967 | 2025-06-09 05:16:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 670e82c8-cdd8-3f2a-be9e-de1c0e1b1c93 | -7.00568 | -44.60949 | 2025-06-09 05:16:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7e0ec141-a327-3b57-9f5d-5fba05e758ec | -7.01717 | -44.61094 | 2025-06-09 05:16:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 6185d2f0-4a95-3831-a9dc-82b8e6104bb9 | -7.01867 | -44.60566 | 2025-06-09 05:16:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a2546bc6-4e5d-387d-a596-d56028394c73 | -7.00721 | -44.60402 | 2025-06-09 05:16:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c559ec52-9160-3fae-8a7a-51d12355a3d0 | 0.41317 | -60.56528 | 2025-06-09 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52f2ad83-9b58-3588-97b5-ce7785014c66 | -11.3691 | -56.56281 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9728fe37-037c-3874-9d0c-328776b2751e | -11.38332 | -56.55015 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c90c4b75-0c70-34ac-ae40-c12faf1fd932 | -8.96598 | -47.9679 | 2025-06-09 05:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67e14cb3-3e43-3d87-bbb0-11feb731927b | -12.52565 | -58.34697 | 2025-06-09 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41df586e-33a1-3e1b-95e1-400aee440b40 | -7.92977 | -61.55827 | 2025-06-09 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49d96a6c-0852-3659-b35c-efa92d3bc989 | -11.36551 | -56.55864 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d2c0335-e2f2-393f-ab1e-de17243e56da | -9.41313 | -48.44296 | 2025-06-09 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b00dcbb9-c0ed-3c75-be9a-70cdb77d74eb | -11.73866 | -62.72738 | 2025-06-09 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e7fcd371-ebb9-3d41-89c9-13cf88dd2d1e | -11.37466 | -56.55258 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94704955-6148-37ce-8349-48cdf59ea733 | -12.15682 | -57.7321 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b960cfaa-eb2b-3219-8899-bee443b6a1c7 | -12.37012 | -57.41342 | 2025-06-09 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b698be4-95ea-3a4b-90ea-d5a0809bc079 | -12.20084 | -54.26519 | 2025-06-09 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a977ef7d-be2c-3924-827b-93ba5c747b1d | -10.37117 | -57.49902 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c0a2079-c1c3-3905-93c9-ca227fae58b4 | -10.74413 | -52.51039 | 2025-06-09 05:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47457721-cd57-3dac-802b-31497dcac11a | -10.49015 | -53.66299 | 2025-06-09 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb2468de-222b-38ec-a154-f6801e885d91 | -9.41385 | -48.43686 | 2025-06-09 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a332ce-ec22-3aba-93d7-bf325204e8a9 | -10.85443 | -53.77848 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 62090d43-5a02-3e26-ab0e-10eb588995ee | -10.84954 | -53.77786 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 924b3945-f4fa-3432-b9e4-f4a9d4913e4c | -11.13757 | -53.94687 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c88c3fc-02ba-3487-b5ac-6d2a93794848 | -10.36737 | -57.49845 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ec50686-c4d2-3cca-8646-b023cb21995d | -9.41086 | -48.44294 | 2025-06-09 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2e07147-5d6f-38d2-a9fc-a383c0a5849f | -12.37404 | -57.41399 | 2025-06-09 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7038aa93-50c4-35b3-a053-42d67e9c1fab | -9.92843 | -59.93442 | 2025-06-09 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04eb45de-3ca4-3a88-b528-d50d0ab7248b | -11.37775 | -56.56042 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 170a166b-7ca2-3fe1-b792-e355a5f123a0 | -11.91585 | -54.8285 | 2025-06-09 05:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90cea82e-9d50-316c-b3d8-0cac958d9acf | -12.36691 | -57.40786 | 2025-06-09 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4def5a5-d3aa-3098-b3d3-127f76de5ac8 | -10.36952 | -57.50582 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebbbd59e-17ca-3d72-a90c-5f87842b1543 | -9.41161 | -48.43687 | 2025-06-09 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f074e61d-3dc9-3116-854d-d512afc61cc8 | -11.91123 | -54.82786 | 2025-06-09 05:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53ef95a5-f297-311f-8dbc-7ec975b90755 | -10.49504 | -53.66378 | 2025-06-09 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c8ccb23-1c89-335c-a6a7-dba9277c1aaa | -11.36502 | -56.56224 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb967eb9-c118-381c-b3dc-869f467fc6a7 | -10.37018 | -57.50117 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 092a6308-3e90-3e6f-9e48-314954144651 | -10.84883 | -53.78319 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd7d4f33-7598-37b7-83dd-f0e39093eb43 | -12.52937 | -58.34755 | 2025-06-09 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35ecd08e-28b8-3ed1-97a7-406e050166f0 | -12.37544 | -57.40405 | 2025-06-09 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af99c0ea-ae75-3f56-bebb-3fb42793857d | -10.3622 | -57.50716 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42e262b6-f16d-337f-957f-1c1920c944b2 | -12.02606 | -57.09077 | 2025-06-09 05:25:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d2525ab-41a2-3af6-b081-0ed0674f13d3 | -12.35233 | -57.42635 | 2025-06-09 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a76515d-0329-3235-9f67-85ff27ed6d70 | -7.89336 | -61.47356 | 2025-06-09 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68a22bc5-c3d4-3b42-b735-229f6d1b9161 | -9.40485 | -48.43597 | 2025-06-09 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b412149-17e4-39c1-89a2-8f235c7d6a66 | -11.36959 | -56.55921 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f587479f-5f59-3457-9d4b-8af017db66c8 | -10.74456 | -52.50701 | 2025-06-09 05:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 608325c8-5a96-3f64-be34-e33897a0b413 | -10.36638 | -57.5006 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f95c97d8-2232-3b48-a881-61f075018d00 | -14.25438 | -52.46741 | 2025-06-09 05:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d19a822-ba33-3488-9d77-957e1c343936 | -2.58558 | -51.91845 | 2025-06-09 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1176daf2-7656-3297-9879-473307379277 | -14.24875 | -52.46703 | 2025-06-09 05:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61b3e36b-12b5-3f69-a632-da7edd333ba0 | -10.84395 | -53.78251 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c5c7c3f-ab63-3731-9109-0021b4390593 | -14.03552 | -55.1382 | 2025-06-09 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README8.md)
