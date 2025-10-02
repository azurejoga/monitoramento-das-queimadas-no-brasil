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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59a02e3f-26fd-3dad-9717-c9d0e7666baf | -10.81785 | -46.61562 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7fce7d5e-8281-34a9-bf5c-f28f0601edb7 | -11.58806 | -50.16974 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 13c8b14a-0dbb-3abb-afe6-cce4e97d3b3b | -7.76774 | -42.54361 | 2025-10-02 04:02:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 11406c9c-f4c8-350e-8236-99034cd070fd | -11.10358 | -49.80452 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f52020f9-8072-3d7a-a0c8-a17fa51c130c | -10.24063 | -50.3275 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4e9efd64-04a8-3e7a-ad12-f2622ecaaba5 | -8.57714 | -44.7905 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f01b230-c4eb-33d7-ac07-42a7806a45a1 | -9.92857 | -43.71743 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 235f5169-2d59-39f0-883b-20c6841c374b | -10.25608 | -50.33398 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e13d0922-31af-3559-99d7-4bc571e6d6bf | -10.99868 | -46.54477 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01056d19-3c8e-3e4c-831b-b3addb58bf76 | -12.42452 | -44.09047 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c7faead-6b19-3c0b-8aab-aeb360ce82f4 | -7.05281 | -43.27388 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1538725a-c4cc-31fe-a516-e84ebded9ae6 | -8.16471 | -41.3299 | 2025-10-02 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97bec9e0-0368-345c-a5ae-fbed25f4cd53 | -10.23331 | -50.33686 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd092234-cca6-37e3-bd26-f776277630ff | -5.64104 | -45.9683 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33e68ec9-197a-320e-bbe5-94a18bd6b437 | -10.19658 | -50.27989 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa83d1d-d32c-3e09-b1bc-43bc9690ff04 | -5.94156 | -45.88029 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 879323bb-f5ea-3491-a51d-4858f78d5e25 | -8.57216 | -49.60213 | 2025-10-02 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dac215d-ad7b-3ebd-9e47-5cf879c14d66 | -13.22037 | -43.36533 | 2025-10-02 04:02:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64a91e03-ac9f-31d3-8188-71ae39b24896 | -11.77284 | -46.83129 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 420104d0-0fad-3c20-932e-798193db48e1 | -11.81067 | -45.00027 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66aa91fc-4c28-3eae-967e-4184804134e7 | -5.92303 | -44.86272 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3ee04a5-2071-3caa-91b2-0701a3b2883e | -6.49761 | -44.29174 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa225f59-cdb3-30f8-ab5a-60ab97055592 | -10.82065 | -46.62403 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c9a7219-4ddd-3d65-b44b-21d94536a981 | -10.23056 | -50.32204 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 779c00b3-5288-3f3c-9fef-304719cd44bc | -6.96469 | -45.34115 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7618ce0b-f910-3ff8-9b3a-e0552d0d1676 | -9.84441 | -49.95896 | 2025-10-02 04:02:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a248396-7d49-33cb-a163-062bc42b4a66 | -6.48143 | -44.29437 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20a73e5f-c8a7-3001-ad75-1231fb4733ae | -10.66981 | -48.5232 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a23d340-34c6-3929-a442-6adfb5761771 | -12.62988 | -44.85173 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3175ec48-341b-3507-be57-4cbf8ea150b8 | -10.8037 | -44.24401 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5e2a2cf-9152-3187-a7c1-53a855acb1e8 | -10.11034 | -45.67422 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c6995720-0ac3-30aa-8caf-6bc4dc7c144a | -10.84207 | -46.62378 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49140ae6-defa-3a1a-a1ab-ab69e22daf8b | -10.25071 | -50.33297 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a7728ee-53fb-31c3-91da-9d6ccf75f886 | -6.82671 | -47.97576 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62ea56a5-cc0e-39c2-92d1-bd97a7b31684 | -6.77341 | -45.58446 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bbaa39de-3cb6-39db-bd08-8e2ff36ba574 | -11.44667 | -43.50137 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eebb665b-5982-336a-8a17-19443de8ba50 | -10.83592 | -46.63459 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af8cc85e-d13a-34dd-8cbc-d682f50f7f60 | -11.81729 | -45.00602 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f7c62c2-76f7-367e-a331-697efdbce3af | -13.41256 | -43.50129 | 2025-10-02 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5849cedf-bcb9-3136-8825-86066dc23ac1 | -11.47999 | -44.98699 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4534aaeb-f226-3c40-b87c-2f80be0dc3c6 | -10.94302 | -44.26208 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b76d14ae-7a91-369f-a851-c836e91132be | -11.68083 | -45.32076 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee3d7654-cf23-3bed-8177-5439aa1d4581 | -12.89099 | -46.90661 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63949910-bb14-3619-8bbd-deffb61a53c5 | -11.79556 | -44.98553 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff0569de-9cf7-3b50-99ab-7952926d426d | -6.46517 | -44.58009 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fc72566d-36d6-3b1e-95df-68a5f7a0cea2 | -9.79167 | -45.94177 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85ef3b95-f88f-3dde-ad4f-8dda54e6d303 | -11.70551 | -44.30693 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c543d43e-c6af-3354-adef-2aea1d523598 | -10.90786 | -46.65052 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 497f689f-31c7-3ab7-b15f-205147bd6d7b | -11.18484 | -47.81994 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88fe470a-4c1f-3518-8fdf-4a42ba2212e3 | -6.29521 | -42.48168 | 2025-10-02 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 48ee36af-58d7-3eef-86aa-80d7ceaa8e69 | -12.88295 | -46.92857 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 834f6eec-f457-3c58-a3b8-ba08640370c5 | -12.64263 | -46.96041 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d9d1a5e-c570-33f0-8bad-91e874eaff1f | -7.78021 | -42.51054 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| f71a3d6b-67a9-3fbe-a3ed-5e6db6479be6 | -12.69193 | -47.56293 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faa3eeff-5538-373e-a338-e44e36000303 | -6.32757 | -43.02364 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4786413f-eb87-390e-bb6b-e39275e7cf1c | -11.17976 | -47.25751 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f1f18da-9da3-3d1a-b613-3c12ffe48c9e | -7.78181 | -42.52247 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eb10e992-8f3b-3655-aa5b-580a39961194 | -11.67297 | -47.49509 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b78adc60-af0e-376a-a90d-097b5df97b6b | -11.49574 | -43.50572 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa1a0a94-7f6a-397c-8c09-e5a8bfc96bd3 | -9.93519 | -43.74383 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fff990f9-72d1-3b6a-8aac-71a33899e92c | -9.93988 | -43.71515 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30282465-4f34-3a8b-a710-04a07ec48870 | -9.4501 | -45.47729 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcff6457-ce19-33d3-82c2-2b7d01f99797 | -10.65286 | -48.50933 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c47d2f46-6bee-3853-bd3f-f0d439f02a45 | -12.62914 | -44.85608 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c8d3ac9-ff5d-3834-ba86-36439cbb7deb | -10.99786 | -46.54121 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4a24d34-5d81-3c4f-9fb6-eaaa5ea1b48b | -10.89266 | -44.27522 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68468169-0645-3e8d-9f40-43bcccff88a6 | -11.92004 | -47.05986 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb8de4f3-7497-39ae-a4b8-25cea7519030 | -11.83846 | -44.9495 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 689c5f49-7ce0-38d0-8f6d-1658943a42f2 | -9.94629 | -43.65368 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a20f3a8-060a-3b84-8ebe-b7cf649e6fec | -12.66185 | -46.87508 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b5eaf4d-68f7-3164-abaa-82d05a565fba | -10.26274 | -50.32808 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dd7e3fef-cfbb-3089-9686-c9a0063562e0 | -6.77279 | -45.58815 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff267941-cef3-3003-aac8-c94d9147dfb0 | -9.33754 | -45.71194 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af801fc0-fd4e-3c4b-8c7e-8ddf2aa2a144 | -6.67586 | -42.36769 | 2025-10-02 04:02:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c20d8d99-b797-3bde-b16a-0adef4efc3ff | -11.80115 | -47.57005 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09b064c8-2ca3-3375-b274-4c536f0b69ee | -12.80219 | -46.8613 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e76205b5-0b1f-36e4-b5b2-bcfa9a6add66 | -12.89902 | -46.90534 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cb40e63-5f9e-324c-bf0e-58b21c212c61 | -12.82769 | -47.02583 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cda2907e-a682-3b7b-96f2-bde934577fc0 | -11.1316 | -43.38575 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9eb9f9d-f712-3889-8db2-a1d5c2b085a3 | -12.67327 | -46.858 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f113e4d4-5931-3363-8fe1-788958092ddb | -6.67302 | -42.79498 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b4ecea16-8c39-37f7-ab1b-3fb3ea4d4bd3 | -10.84275 | -46.6199 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2e81e08-50f3-3885-8721-a616d3e16e8a | -10.22794 | -50.33586 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f59faa63-9e42-3be8-8b8f-c9f0af4c6d16 | -10.23657 | -50.3196 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5fda4929-3d0d-37a1-a296-041b7cc71d12 | -9.80067 | -47.8459 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4de5c22e-6336-3d02-845a-3ef4303dc4e5 | -6.49149 | -44.2881 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87fe1b6f-705b-3d26-b57f-96c658c5e6a4 | -11.91398 | -46.74426 | 2025-10-02 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 55b47d1a-6144-3272-aab9-0479878347b6 | -7.78463 | -42.52683 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6c940adf-a03b-3098-bf3b-f215faba85fb | -7.79277 | -42.52029 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| d225d93f-dd7b-3434-9467-9f9910bae9e2 | -12.02618 | -46.62986 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e7a5bcf3-55bc-37d5-b458-97c986ff7f61 | -10.95705 | -46.66283 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72b843f4-9c8b-3382-bf0e-8d2710a74f00 | -7.03204 | -44.46785 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8772ba7c-d466-383b-8ff8-7c7f2f65cde9 | -6.23886 | -45.3286 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c02d81b8-bd71-384e-b2a6-473a98f157c4 | -12.86056 | -46.93589 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4db00c5-f9ed-3667-8721-908ab74f2c41 | -12.65776 | -46.87432 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e699c8-7e74-3623-bcbc-153b75d8fb25 | -7.45836 | -46.46666 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16a3cbe9-5d22-3e25-8dc6-327bfe9a6265 | -6.82458 | -47.97737 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5ce23a10-8e32-330b-9093-ca72cb736cc7 | -13.01202 | -45.21116 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7b2434a2-61b1-3f36-b2b5-12388d755a79 | -11.99812 | -46.57524 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4003a15-f3a9-384b-a480-44419a5a4042 | -11.59264 | -50.17392 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README34.md)
