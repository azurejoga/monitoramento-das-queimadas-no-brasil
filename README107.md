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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89782c69-bfe0-3cec-ab95-e9b405b71b88 | -7.56471 | -42.3947 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 282b826a-f88d-3db5-a444-0d6bd2ca331c | -8.59641 | -44.76252 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c404ecd9-dcc2-3439-ab1c-0d6a54ebdab0 | -7.76965 | -42.59072 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2a94dd58-7b5a-35df-aa6a-a0a111bbbbf1 | -9.54303 | -50.83825 | 2025-10-03 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2acd77cb-c956-3f5c-9f40-ea1e6d2c7319 | -8.72124 | -47.13597 | 2025-10-03 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d1fd14c-d7fd-350b-b435-ce3dac41913f | -7.26122 | -48.47817 | 2025-10-03 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c17d399-9286-31e7-8f94-6f1ac686e7a1 | -4.57694 | -46.50031 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a21a92b4-dd13-30ca-84e7-19db4c88dda3 | -11.82173 | -44.9088 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5aac55fa-bfe3-3b5a-bcfa-f98222bf5b2c | -7.74661 | -46.25349 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 670e8fe6-e68d-3d42-b185-6028492054cd | -7.77072 | -42.58325 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 1a702d1c-86fb-3d79-8c3d-1a3e0e082ccb | -7.77433 | -42.5876 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 083f97e5-b091-34b6-8cff-4a6e8803cb94 | -5.24534 | -43.10454 | 2025-10-03 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03380bf3-6716-3e1c-90bd-94a5bbdbc1ba | -8.19874 | -47.00425 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdd85803-0aa6-3020-bba9-fb8bca66e2d7 | -10.88001 | -46.70646 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a6e24c0-2b94-3b4a-9669-0c247ad58b0b | -6.54816 | -43.87722 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0a14485-640a-3384-a734-43e622fbaa4f | -7.74201 | -42.59062 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59606749-f385-3b23-83d7-b353defe6063 | -7.75843 | -42.55033 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 94691b22-0e83-36f7-9b29-280b086a3600 | -10.22635 | -43.02731 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2b7fcf0-192e-34d1-a99d-0b0a7f720f2b | -9.40262 | -47.536 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc248099-5281-3190-a908-f738403b4f42 | -11.63084 | -47.98373 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8680fe71-ec9b-3c36-a2ca-e3b33826f7e4 | -7.79438 | -42.53637 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef94e5f0-43c9-322e-a206-e240b913920b | -8.21713 | -45.55087 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7d2211a-a9e4-3177-8644-b64b9e4b5e13 | -11.48854 | -44.9944 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28403e70-ad77-37a9-8971-4ea7e44b7adf | -8.53973 | -50.15414 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84c0d0bf-21bc-330e-856a-65572976ae3b | -4.66373 | -45.79855 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a68f2e4-b047-3954-96cb-622fd2bd2a64 | -7.52611 | -47.29298 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d56d9bc-e59b-3bef-8eff-9f980a375f18 | -9.0686 | -46.64872 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 521d9998-ad2a-3113-a7ec-5f2ce9904d34 | -4.26301 | -48.55062 | 2025-10-03 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e777c4e-3c86-38a9-80d7-78c63dcd623e | -9.91304 | -43.74189 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8d3ff722-78d5-3f69-982f-041394b0649e | -7.68335 | -47.76339 | 2025-10-03 04:32:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc90ecdd-a2bf-35a4-b490-f1e0049fa3d9 | -4.66092 | -45.79439 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cee320b0-f8a2-3b29-8e76-f5fb380f9f3a | -11.3104 | -47.83872 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 103b7a3b-b67a-3e4f-8b21-59f719e2cda6 | -8.82879 | -46.77339 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2edbf238-6c3f-3026-b11f-5755989f9cab | -8.30296 | -44.85218 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9052f0b-499d-3582-81dc-57cc3dec75e8 | -8.88557 | -46.59063 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0651c734-da74-389a-b5c5-8e33489159db | -12.29599 | -45.3658 | 2025-10-03 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df915e06-093c-3ad4-9c49-8afa97dad153 | -11.29455 | -47.83612 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eeb1944c-0b22-3d44-be10-d86fb1f97fae | -11.48432 | -45.11257 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa0d999-ba75-37ad-9a30-ccab4f41b7f2 | -5.74261 | -45.08258 | 2025-10-03 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a1c0893-cddf-3c20-a86f-5dcb417f8adb | -6.82474 | -45.98606 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0c1aa0f-b0f6-37be-96e3-ea75fcb9d0cd | -7.31521 | -47.29555 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aee2045-499a-38da-9d34-8d2c1b7e2d18 | -6.10541 | -43.11553 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a3bcb502-2ea6-3f2e-a828-ecec18eb3ce9 | -8.8316 | -46.77759 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51abc36e-b795-38d7-8094-54ea13e96470 | -11.83246 | -47.69142 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0d0e8e3-1605-3a63-8473-61cbf8bd1bde | -5.0238 | -48.46678 | 2025-10-03 04:32:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a39bd06a-9b06-39b4-8ad5-db8bcfd5bf5d | -7.46157 | -47.00926 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78d37321-9e5a-3bec-bb49-6f45d61451e6 | -11.56498 | -47.66088 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4ea261d-5112-33ee-a960-2c126113f4ba | -10.94073 | -46.71916 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d3ec269-a0f3-383c-a0a1-2d9881e93d9b | -10.96444 | -44.33766 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e6a8ea1-c7af-3527-93a5-397cd8b20ec2 | -7.21749 | -46.87359 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a444cf-ef0b-3165-8547-8eabaec5dcbe | -7.77594 | -42.57634 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 71d255b6-e2f0-3dd3-b77d-9532c23e87b0 | -11.43017 | -43.48966 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd6e7347-e7f8-356b-b7ff-e9b144c384ad | -6.35095 | -43.95964 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 803d0381-0cbc-391b-bbbd-bf14a4a2cb46 | -6.22779 | -44.23998 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a6367ca-a46c-3a8e-ae33-05cc8856cd4d | -10.00577 | -50.24207 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| faf9be3e-de89-334f-b4db-508eaae13f42 | -7.26398 | -48.48218 | 2025-10-03 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e0e926a-6efc-3c9f-80af-7086b4868e59 | -11.14347 | -43.40759 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 129a4f0e-7f67-391a-ac37-6377a6910085 | -7.75908 | -46.64676 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 770b8a59-65fd-3d01-aa23-fd1f8b6f4c4c | -10.00118 | -50.24888 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 65f7894f-6182-35de-8728-8743de5424e5 | -4.25908 | -48.55365 | 2025-10-03 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fda57e5-9414-380a-ad8f-fefdf2faf6f1 | -4.65812 | -45.79018 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c0bc7c9-be1a-3f79-ae51-55713b8b5386 | -6.05216 | -44.63966 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf96fb4e-efbd-39b9-a677-bca5dfeede27 | -6.32278 | -43.88443 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 130b127a-73fe-3f75-ad59-2e279f321452 | -9.09392 | -46.71646 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaac46e6-705e-3243-9417-655326cc0a09 | -6.23993 | -44.25911 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a275374-61cb-3723-9001-10a77b9c5b1b | -11.59912 | -47.66253 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e6e53767-573e-3289-ab76-2cd9dd6e51ea | -11.09117 | -47.80792 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85f417fb-87d7-33ef-9e06-8824acf675a2 | -7.31358 | -42.87591 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 86841485-ef67-367d-9b4e-259f48641ed2 | -11.87371 | -45.00312 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54d35a42-92c4-346f-81c3-12f8e4ba538f | -7.76595 | -46.26384 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| ea5c884f-1f8e-3f9e-bf24-b021418457b7 | -11.76772 | -46.83037 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22044e3b-18fb-31fc-a3fd-c80eeecbdb09 | -7.76316 | -46.28217 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e70461d0-9827-3bbe-a634-160db5aee786 | -6.26749 | -44.04982 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab98ccbc-2359-327b-8d45-7e377a5439a8 | -6.33329 | -43.89089 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6375eafd-bb6a-320a-a15c-86fb22b6a8bc | -7.90134 | -43.53899 | 2025-10-03 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d773c0b-b99c-30a8-af2a-c2014f035900 | -5.30405 | -43.75985 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15dc0380-41c1-3ed0-85ef-4d4082d21a4d | -4.67465 | -45.80407 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09d46613-1c3c-3459-97ad-6621be3aacbc | -9.91848 | -43.73228 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7eb43389-2ba2-3bb1-868a-0265ade0410c | -10.96517 | -51.09185 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c1b1d0f-1bec-3f4d-9014-67a31b919e76 | -11.13043 | -43.38035 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 593d939f-23bb-3bd4-96a2-810900fd4e6a | -10.87538 | -47.82144 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3dd5777-84aa-3fd9-b5c0-12709bd38c3f | -11.80752 | -45.00659 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79552c14-24e8-3b27-b345-9f7e694cd756 | -10.28129 | -48.06492 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b4e1a39-def4-3b12-9d9c-4474a78d122f | -7.77901 | -42.58446 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4cb36071-dbe6-3d3d-af18-066cafa39fd6 | -10.87972 | -53.76929 | 2025-10-03 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5606d02b-13c1-3d78-9015-9790cce7652d | -7.77848 | -42.58821 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 077ca099-a068-3383-91f1-71bb47a28901 | -6.04382 | -46.07808 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad07b5b0-a961-30bb-b14b-811bd644c749 | -9.98094 | -48.7867 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42e5589a-31eb-3948-99e8-d2f9e8eb2a06 | -6.27926 | -44.04712 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff639614-36a6-3130-9be1-f165d108c58f | -5.83501 | -53.6746 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b005ace1-cbdf-3188-81a9-abc3c420ad1e | -9.94056 | -43.57866 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb7ae622-1d2c-339e-99e5-046c35186f96 | -11.48174 | -44.98848 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72983a54-1450-3976-afda-23b2d9c54927 | -8.7317 | -47.35557 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfda0c92-96d2-3121-bf6c-cc462bc58a00 | -4.66396 | -45.80603 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b27d302-7d71-3c65-bda0-07231b048bba | -5.34686 | -43.76439 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e2dc3e6c-5eed-3fc6-bb67-fb52420e7333 | -6.37463 | -43.87659 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 559906ea-cb4d-3c4a-9aef-aa93c9246b0e | -7.75004 | -42.56499 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| fd332e7c-e44a-3a9f-93bb-aaaef81a6b32 | -7.74549 | -46.26084 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d9ba20c-0f57-360d-9f88-a3c58de17ae0 | -11.5924 | -47.66148 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53b83880-86d0-35dd-8dab-42628fe39c6e | -4.97331 | -48.66212 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README108.md)
