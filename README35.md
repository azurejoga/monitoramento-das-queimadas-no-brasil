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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a5fb156-cdb7-3335-bbd8-fec3dd849f4c | -5.32163 | -50.954 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5a709b1-1bcf-3017-9345-90b8d681cfdc | -8.1106 | -50.03839 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db480797-1cb7-36c4-ae10-24b3848de260 | -6.86459 | -59.45268 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81bcf892-2a49-3faf-a517-4abee3fba227 | -8.09439 | -51.6659 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8a2abcb-af18-32ec-a8e7-9eea324056f7 | -6.65486 | -56.43747 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd515cb0-09d2-3038-a395-7a92c20133ab | -4.18254 | -49.39877 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c3bc3ee-5898-35ff-afd5-b8a2bd57fd23 | -8.56177 | -54.70073 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 681fc028-78ee-3ce0-8d51-3b87a395881d | -4.45043 | -55.38752 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ada8e364-60b1-36b6-8f7c-550f1e2c88d7 | -10.77987 | -50.30132 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f4ca504-a1ac-3ad1-81b0-07b30a76ce4f | -4.88912 | -56.28473 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f0e9589-1ab3-3b93-ba9b-1109aab509c7 | -6.58221 | -56.3725 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da7f05e6-7855-3448-99b3-c345929ef6b2 | -10.75103 | -50.33118 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0319232c-8968-3eb6-9869-75aeb9e28467 | -6.24656 | -55.42498 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af230300-2d54-3491-b5df-c2cca63ee8ab | -6.60898 | -58.39285 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66787aec-391d-382b-bcf3-14d507bb5b9e | -8.89645 | -60.55036 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 89c1ddb5-f540-3f2f-aaeb-ab4356d6fd96 | -8.40804 | -62.69177 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5ff6795-7cf1-3dbd-a439-d5a6a81cae38 | -9.11405 | -61.60296 | 2026-08-21 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b34bbd6-5da6-39d2-a93e-54fc479cffe2 | -4.88975 | -56.2809 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fa683fc-6e79-3186-aecb-0ad57185f0ff | -9.21688 | -59.77623 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 955c6d32-6b69-3174-949e-6a493bb5073c | -9.40483 | -60.55589 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9aa7ee3d-fe12-3bfb-87f9-7dafcd8203ad | -3.76073 | -59.42549 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d919bd1-64ad-3862-8e50-2001fd462c83 | -9.05612 | -57.07134 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c6794bc9-087e-3e41-b140-ede90ab6974a | -8.05794 | -50.10123 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2feed14b-6984-3fa3-9dbd-e83949f25265 | -6.16475 | -55.44164 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46ace523-3874-34b1-bf9d-d50c784cb3fb | -6.8732 | -59.43218 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c5d9b41-7167-3afa-8d51-a08aea4b69cb | -8.8976 | -60.544 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 17439eb0-7f05-3ab2-950b-423e0dbeed2b | -7.44255 | -60.00293 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64de40cc-e70f-37d2-ae26-b51f0a02e3f0 | -6.57778 | -58.96626 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83adfa92-c31d-3870-820e-f494509dc07c | -6.88452 | -59.42984 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 852c0176-5254-3fd8-acfa-2f3682a7c499 | -9.44818 | -51.61795 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9208d99d-7986-3d7c-b209-f839e61bff14 | -6.21407 | -55.47919 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f731810-78a5-3b71-976e-af5d39dc18ec | -6.94198 | -52.78176 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d30772f-6375-31fb-aeaf-83dc6dad655a | -4.94541 | -55.78357 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 023a1d2d-c850-3e51-b620-bb39f34b28cf | -6.20861 | -55.48835 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 933400f6-9bf9-36f2-ba45-65cf1e68693a | -9.21398 | -59.76439 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f308f3f9-3c73-3ed6-86a4-d182634a60d0 | -8.66007 | -54.63133 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f57e2315-9a80-3caf-9a79-6432fe954bfe | -10.77591 | -50.30452 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4400301-674b-3e50-9768-7c6fb7ef5fb1 | -10.26646 | -50.28935 | 2026-08-21 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28075fd6-bfe6-31da-b1fe-29923fe1b4a4 | -5.93668 | -52.2143 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3eb1412-dce0-331d-b079-4f5a4ae5ee42 | -6.88926 | -56.43551 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 246ba695-e26f-32c0-8529-a71fc0c5e888 | -9.40296 | -60.42294 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 82fabb09-74ff-30b6-b368-d9d51d958383 | -8.9871 | -50.73 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d254165e-6711-3811-b794-3cbb60d8e86e | -10.77139 | -50.31146 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1436667f-25ba-3350-ab44-fd24cc505497 | -7.05513 | -59.83643 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3387fef8-b98f-3491-b70e-64a2c4f3780d | -10.90519 | -50.28234 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9f688eb-69e6-3169-846a-651829beea3d | -6.86206 | -59.0276 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 48cb1aa6-27cf-3235-9344-12a16d769742 | -9.42502 | -60.41733 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49b054ea-29fc-3cbf-8fe1-e32041949be3 | -9.44324 | -51.62787 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8d941fb-b685-3baf-8bd7-0f9389cf43b9 | -9.40596 | -60.54972 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e90c365b-3cee-3cb3-a101-47d750e22661 | -6.82141 | -59.40584 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e712e104-7a37-3e7a-b95d-1c1f499ceb9d | -7.77903 | -61.16287 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cfe7a128-dd5b-3d50-af19-97d3e7f70833 | -8.0342 | -54.02412 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cfe0cfb-fdb8-3677-be25-50f2b89074ee | -8.17923 | -54.99191 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15305be9-189d-3325-8844-243fdb11c561 | -8.54274 | -55.31784 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 289d2bfe-ba13-3292-9da5-1ce26f613937 | -6.77306 | -47.407 | 2026-08-21 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 496d411b-f177-3722-a9e6-6d18d0fc816e | -4.88636 | -50.91044 | 2026-08-21 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83fed2e3-da53-3fc4-9e53-03a9f82d95cb | -6.86253 | -59.43465 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a88ac06-f6e7-312d-9462-0d627ee6d86f | -9.41623 | -60.55153 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 577f3764-dc79-3821-b0c5-c35cf47b06a3 | -7.01289 | -59.54903 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bbd63ab-472b-3597-ac77-c482bade6951 | -4.92087 | -56.25979 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98d28bfe-2d18-3e5a-8980-a75c7a801dce | -6.85754 | -59.43386 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 667c2ed2-fa3e-3a84-8b16-2938850f6ea2 | -8.59088 | -54.74793 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c64c6260-d521-33a9-bf6f-ebfe85517a1c | -7.34774 | -55.68917 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ae82e7e-c6ba-3254-9302-255c95057fc6 | -3.84469 | -59.37761 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfb2f179-de16-3ce8-bd21-45d2baf3e1f5 | -6.5556 | -56.25816 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d638c4b-4add-36db-bb4e-a854363973d5 | -9.4151 | -60.5577 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ce69bb2-0940-36e1-b0fe-5a215aaaadca | -6.47444 | -43.54473 | 2026-08-21 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90cc46e8-4237-3d2f-ba37-e0ca388af662 | -8.16742 | -54.99504 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58709e13-379e-383c-b234-0cf8651c47c7 | -8.55298 | -54.77604 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8646a228-8680-3050-981f-820d80513c33 | -7.55106 | -55.56226 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 225ae08d-a444-35b0-aec5-6c905febaafd | -6.12771 | -59.91162 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fe6d846a-5a3f-36d1-affe-3114f4cae137 | -6.6619 | -56.34604 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 379d1c93-bf68-3eac-aefc-a0e6d30c2fc2 | -10.5246 | -50.80669 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6da687b8-b80e-3b15-9590-8bd7be33d8d4 | -9.39799 | -60.5642 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 119be787-b847-3475-bad1-986a5ef0b6ff | -4.10876 | -56.36162 | 2026-08-21 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4412c32-87c4-381d-8bc1-e433d87275c9 | -9.42747 | -48.24161 | 2026-08-21 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e75887e-dd77-3793-9273-a2835a67b05c | -9.44764 | -51.62143 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c43aec5b-c05a-3777-9171-13420afe3ea5 | -6.96574 | -50.4165 | 2026-08-21 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5084b470-2d2b-3a2e-a60c-0f6f1a32d3fd | -6.89445 | -59.43161 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53a30c86-0450-307e-9e49-2e57b8609a9a | -6.11579 | -53.07341 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ad7b81ed-4663-3aa1-88d5-1f7b7b217eb1 | -10.3091 | -50.38219 | 2026-08-21 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8cfbeff-226c-3eb9-9b5f-1656898e3716 | -10.11037 | -46.35117 | 2026-08-21 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a118b150-7c09-3cb6-aded-afcd557db970 | -9.20788 | -60.77246 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 328a8e41-ebb7-3647-9fe0-42b3cf0f84f3 | -6.71449 | -59.09186 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 047a0e77-f036-3544-bc70-77c99468f33e | -7.77551 | -61.15105 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21637fe1-d4fb-36f3-9271-fda512174eed | -7.37091 | -45.80718 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 454f8ef7-bdd2-3ef6-844a-20510bbf39bd | -9.2069 | -59.76151 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9f02022-19ee-392c-916b-d886398311c1 | -6.11262 | -59.90596 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a6c4bfad-3c94-3fb0-a551-8260e45481f9 | -4.95759 | -56.26911 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9c79b99-3e87-3748-b9e5-5940815128ec | -6.10604 | -52.238 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aba69736-2c51-3646-b810-5e24165d0eea | -9.4103 | -60.41168 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e2e05e9b-809d-32c4-8256-df42e06455fd | -8.38753 | -62.70203 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b4972019-b673-3839-9816-b5518a9acef9 | -6.31494 | -55.91968 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 656ae642-ae4f-36c0-98f8-8c3ee3bb1b8d | -7.35787 | -45.80911 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cd44556e-bf6e-3692-959d-fd55f1f739a3 | -9.17548 | -57.00917 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e62cad2e-a652-3dee-8a51-30fd0d9408d1 | -4.05064 | -50.29588 | 2026-08-21 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9714d2f2-333f-39a0-a42b-2d457879c867 | -10.86583 | -44.80561 | 2026-08-21 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28b05cee-5ffe-36fc-9f4c-643b48b9f5f7 | -4.45843 | -54.83812 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5401e80a-4258-3eff-8218-74cb5676e869 | -7.36981 | -45.8148 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c6a6e935-6fe9-337e-9770-95ce833a69ee | -6.61608 | -56.34418 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README36.md)
