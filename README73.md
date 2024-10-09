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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8b2d55b-e9c5-3c2a-8f73-1c2f6e4e8cb8 | -3.30133 | -43.50918 | 2024-10-09 04:14:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4125e696-7e50-349c-9550-7898b3ae8891 | -3.46419 | -43.36217 | 2024-10-09 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94eb3073-04aa-3a87-86bb-7827bfaafb20 | -3.46806 | -43.35921 | 2024-10-09 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27090ec4-8ebd-3b9d-b1b0-5e0c624b0b9e | -4.94641 | -43.67534 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93d32079-8506-3fb8-84b0-3b597adba05b | -4.94254 | -43.67831 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d05b4aa-6cae-322d-83a9-6a7beec1c3b9 | -4.93375 | -43.77739 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0a5500d-0c99-3f10-9836-78671ce558a1 | -4.89374 | -43.96618 | 2024-10-09 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dde7725-b0c4-3031-b1c3-cbd2dc9f8fbc | -4.48152 | -43.77443 | 2024-10-09 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ddd2142-fb68-34ae-a520-e3ea6cc6feff | -4.40444 | -43.52903 | 2024-10-09 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed9e5124-8a74-3427-abf1-2a4b3fe4502e | -4.39115 | -43.52694 | 2024-10-09 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a529c96-653a-3b6e-bca4-05626623294f | -4.00701 | -43.60965 | 2024-10-09 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c320c9f-6594-3415-8aab-7bf93bc8cd31 | -4.92955 | -44.01596 | 2024-10-09 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dde7f2a-be1b-3e70-84e1-5bfe748f348b | -4.92563 | -44.019 | 2024-10-09 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe0c223-0adf-32c3-b0c8-d63ff63a28a7 | -4.81861 | -44.35417 | 2024-10-09 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb7bdcc7-6dd6-3bf5-a142-4cf01f3f0125 | -4.74196 | -44.10653 | 2024-10-09 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f582750-4989-35ec-a5d8-6b0bcdd236dc | -4.6512 | -44.3727 | 2024-10-09 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f2aa324-b12a-37ac-85a6-536361f56efc | -4.64781 | -44.37216 | 2024-10-09 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 46f6520d-85d7-3f07-8ff4-9abeb3dbc5d4 | -4.64722 | -44.37581 | 2024-10-09 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ba501f17-9eb3-335f-9812-9f7d060faa5e | -4.64443 | -44.37162 | 2024-10-09 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 69e244c1-c39d-3536-be24-288830a74fea | -4.64384 | -44.37527 | 2024-10-09 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 21dffd35-7e2a-33cb-a875-877ee02dc67d | -4.37271 | -44.44122 | 2024-10-09 04:14:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc5d5d4c-8096-3ea5-8d21-6a2c56d51b8b | -4.28514 | -44.39413 | 2024-10-09 04:14:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7650421a-45c4-309a-8e1e-2b25c3d5074e | -4.28456 | -44.39779 | 2024-10-09 04:14:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b28645a4-9a29-39cc-9739-b85b7430fb50 | -4.28175 | -44.39359 | 2024-10-09 04:14:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b654d133-d86b-3f1f-98c2-63d87b032197 | -4.28117 | -44.39726 | 2024-10-09 04:14:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7746fb8a-b537-35ff-a3b2-5b53d7aeb207 | -4.28059 | -44.40092 | 2024-10-09 04:14:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9dabd722-5c5d-3722-967d-5530500faa23 | -6.16329 | -43.70846 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3be6de1-0cc1-3d31-9eb4-18e6b74e33fb | -4.2319 | -44.26999 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abeafe14-5cd9-30cb-8e4f-dbb74333c149 | -4.2291 | -44.26583 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32a2ba68-0358-3d60-b69d-8c636e62e7a2 | -4.22852 | -44.26947 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0abc371-739f-3ac4-8c07-411bd4df6d4a | -4.22572 | -44.2653 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37c62ba6-2316-3db7-9c3c-cd5d4b882e70 | -4.22513 | -44.26894 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a4d2afd-032e-3843-9d30-7b78874cf3b2 | -4.22455 | -44.27256 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c55f86-258b-3ecd-8468-8f1ed0baf7f9 | -4.22233 | -44.26477 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75ae7198-3cac-3e17-a62d-b51c18ec1282 | -4.22175 | -44.26841 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0df6801-4c8f-3f78-829c-3d3961e23156 | -4.06343 | -44.04723 | 2024-10-09 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 692441ff-ec7b-343b-ad89-63acb90019ad | -3.71805 | -44.20792 | 2024-10-09 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 009b23f6-86ea-3514-9023-524324837c2c | -6.48357 | -43.87743 | 2024-10-09 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5a3b7b2-12a0-3b38-a8b3-1faeb739c1f8 | -6.48302 | -43.88092 | 2024-10-09 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21452c29-5659-30a5-a2fd-dbc9a6592a67 | -6.35581 | -43.58662 | 2024-10-09 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c187abdb-37d2-3695-a8a8-1d7c99d45ab7 | -6.32735 | -43.76702 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61cd9611-2e7c-3b16-9562-c7d49d5ee33e | -6.2738 | -43.76219 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4c360ed-e569-3e2d-bb95-1c37cf132539 | -6.27049 | -43.76167 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e7c6797-c25e-3328-9323-39fcbf85e44d | -6.26083 | -43.62772 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d87efc4d-a1ea-3a4d-9c9e-165b5fe7369d | -6.25277 | -43.87319 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 700c7423-0a19-33e5-9290-3a6669d25473 | -6.25221 | -43.87668 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48e97a1f-25cf-3d8d-97dd-14b334bac946 | -6.51065 | -44.00705 | 2024-10-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 463ffb9c-0f9b-36fb-a476-995faef21373 | -6.50843 | -44.04259 | 2024-10-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 742929e1-cb81-3a9d-873e-02ac454e6a74 | -6.50787 | -44.0461 | 2024-10-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eee3593c-070c-38c7-a982-4c1cb4726f49 | -6.50177 | -44.14939 | 2024-10-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c913fde-c9c0-3aea-9b72-951464b98dbd | -6.41724 | -44.596 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 616a57fe-2a37-3f81-96f8-ae00ef2e7c90 | -6.41666 | -44.5996 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bded3eaf-ccde-3ffa-be37-741a7c282e7b | -6.25312 | -44.81214 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a0d8bbb-1dcc-34da-bc80-42e27e0b999e | -6.17046 | -43.70603 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2cd0062-c379-373e-bf3c-82aa28d2a8fe | -6.16715 | -43.70551 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b0bed02-aaba-3a08-b18e-e7108063819f | -6.1666 | -43.70898 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de25eb15-3893-3236-b799-6a0f8cc0d75b | -8.30377 | -44.09841 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9289aab3-1292-33b9-9e2c-817b8deb5aed | -6.16273 | -43.71194 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b364ad7c-0f2b-3537-9604-675e1ca8a90e | -6.10121 | -43.88442 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1965544-3574-3e64-a3cc-0f5e13bc8c12 | -5.8909 | -43.79354 | 2024-10-09 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25636da5-1d7b-3d05-a6ea-715357e37229 | -5.85108 | -43.74442 | 2024-10-09 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 283ffea0-8596-3d75-986a-8749304be5a3 | -5.85053 | -43.74789 | 2024-10-09 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18fe8886-3327-3847-bf5a-43d5d2a63f3d | -5.83782 | -43.65674 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 433a8ab3-c36e-39b5-a38c-ff4bb4c727b6 | -5.81109 | -43.97467 | 2024-10-09 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac84f740-bb1a-34a8-a3d2-a4ec64451489 | -5.80776 | -43.97415 | 2024-10-09 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acfd0b3e-3643-3c1a-a90d-d068e2f5764e | -5.76536 | -43.83454 | 2024-10-09 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca3df42c-3458-30d4-8973-b5d1734e5e0b | -6.18157 | -44.44827 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52ef547d-cfa3-3b31-95a3-77bf69c14937 | -6.17821 | -44.44771 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fe2c634-e822-306f-b372-cf1a3d3c1df9 | -6.15988 | -44.00845 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86722125-734d-35c3-b840-01566995ef24 | -6.15655 | -44.00793 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b61829-d775-3f8a-876c-77840d93e077 | -6.13768 | -44.01936 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2a763db-dbfb-34ec-8901-f20748aa807b | -6.13492 | -44.01531 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e94431cb-3399-356d-9d30-18c7e0ffefd2 | -6.13488 | -44.69641 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52f3131d-13bf-3f43-9392-acf9247367f2 | -6.13436 | -44.01883 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5f05a50-2dff-30b5-a741-5b70f33d9ebd | -6.1343 | -44.70007 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e3537f2-4c6a-3882-b652-402dcb0c7994 | -6.06512 | -44.49565 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc82e15f-d97b-3aa9-8b38-68b0eae3de6b | -6.06455 | -44.49924 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7081ff3f-58b8-3c9b-99b4-4619089b8f52 | -6.06189 | -44.02525 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fcc19f4d-3264-3747-a1e6-3cafea2b598f | -6.01555 | -44.5248 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42c12610-6051-3878-8b71-1c7e0988211f | -6.01424 | -44.5211 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 627f4c73-a380-3bf0-85f7-ca09b30b678d | -6.01367 | -44.52473 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6be384b7-7106-3141-8d9f-3ba77804992b | -6.00596 | -44.62709 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72a09f85-5246-386e-9fc2-cd8cf15f14fa | -6.00538 | -44.63072 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef98665a-7053-3371-a785-fcc13257f347 | -6.00258 | -44.62655 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cefcbce4-fb8c-39d7-b8b5-97763bdca8e1 | -6.002 | -44.63018 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d66f03a2-0f5d-31bf-8f56-3832bf28ff7d | -5.99921 | -44.62601 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae4340a4-3cc1-378b-b10a-8d903bb47a92 | -8.30322 | -44.10189 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a8615e4-f2e8-3ec6-a2eb-0c2db4f10343 | -5.99862 | -44.62965 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd50fafb-4d0c-30ff-9071-a9f7896da2da | -5.99764 | -44.62603 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db8bef26-f9ad-3904-aec8-46710df057f7 | -5.99706 | -44.62967 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2505947f-3646-3773-8eaa-722a43c07f5b | -5.99649 | -44.63329 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 712f0a48-41df-3e94-a1b8-56b95ed06eb6 | -5.99368 | -44.62912 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1ccfdd09-17bd-3bb6-abab-595b7231b972 | -5.96228 | -44.58701 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a1ff579-5654-34a5-a899-0a3d379fff8b | -5.95948 | -44.58287 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bad1f71f-15e1-3749-bc11-6ea56c8155de | -5.95891 | -44.58648 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f644a138-95f6-3c1f-9a35-315cc3a3dd40 | -5.95611 | -44.58234 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b51596ae-24f6-3ecd-abf7-dc60723f4dd2 | -5.95553 | -44.58595 | 2024-10-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 853060ad-840c-3bae-b89d-efeacdb8fdb4 | -5.91421 | -44.62763 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c368a09-5814-3770-862e-8305b266ba07 | -5.91245 | -44.63854 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8044114c-adda-3ef2-b90d-74fba263dec3 | -5.90561 | -44.83258 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README74.md)
