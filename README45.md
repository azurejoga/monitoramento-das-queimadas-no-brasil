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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02bc59e7-0826-33a7-91e1-1d33f251f218 | -10.17609 | -49.5073 | 2024-10-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e12d2a2-ae8d-389e-b369-1526664b828a | -10.01113 | -49.15141 | 2024-10-25 04:17:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf4fbf8e-0419-3dc2-893e-f431dad45e66 | -10.87324 | -49.53664 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0709099b-d847-3464-8164-1b7418159cce | -11.25538 | -49.95954 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbdc955c-ebca-3c17-b258-5cbaf711126d | -11.25468 | -49.96347 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75f2d199-fc3e-303f-a8a5-4487db0c0572 | -11.25399 | -49.9674 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c7f1e86-3544-3a65-a1cf-d4d37ca4efc2 | -11.15883 | -49.2938 | 2024-10-25 04:17:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0c50115-d0e6-3343-a23a-8efc0b7e89c1 | -11.1582 | -49.29742 | 2024-10-25 04:17:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4f23d95-f5f6-38b4-9d96-0fe80f841c77 | -11.04425 | -49.47102 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0adf109-4743-3560-b1a1-5576c98e6125 | -11.04362 | -49.47468 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eccbf9ee-2106-3d5d-859a-55716fa89e25 | -11.04018 | -49.47031 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba996285-86ec-3cf4-aa36-84f045fce9fb | -11.03465 | -49.59973 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd7c4cf7-3ddc-3cb7-a285-2162ef575cc0 | -10.98577 | -49.20295 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 229cd571-c213-36d2-92cf-57a759763cf6 | -10.98516 | -49.20654 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 090cc92e-7290-3c7f-a029-8968800892b7 | -13.72717 | -49.91768 | 2024-10-25 04:17:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7c0de2f-4ee9-345d-b087-e0031458b937 | -13.69316 | -49.84499 | 2024-10-25 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbba9896-45a7-3659-8094-b318a04c2a5e | -13.84335 | -50.08529 | 2024-10-25 04:17:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b8714c5-af51-3fea-a5f5-d45eba359ca4 | -9.25385 | -50.68822 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14f511d5-f06a-3004-b197-3a229241c701 | -9.253 | -50.69296 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d959ff5-91c6-3bd9-bdbb-75726fe1bb53 | -9.24928 | -50.68749 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d208dc8-518a-33bc-8aa5-a8db16c120f5 | -9.55374 | -51.68156 | 2024-10-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a950771-6fc9-36c5-8b85-690495553515 | -9.91036 | -50.54554 | 2024-10-25 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d6356a19-610e-3af2-9d5c-49243163fe69 | -9.90895 | -50.54448 | 2024-10-25 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| bdfa3d5e-41d9-319b-81bf-6188dc747d40 | -10.55923 | -51.63068 | 2024-10-25 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 627ae197-df25-3ab0-b3fb-ddd18a01f936 | -10.10207 | -51.12409 | 2024-10-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a9e806c-052c-378c-889c-93e04a08073a | -10.10121 | -51.12895 | 2024-10-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b34b122-64bb-3fc7-bf94-336f8c5931a8 | -10.09744 | -51.12331 | 2024-10-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 152a2999-ab59-3e58-a6cb-dcd3b3194197 | -10.09658 | -51.12815 | 2024-10-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d143ff4-ce0d-3569-ba97-4c0ad4a07f82 | -10.61302 | -52.4192 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d336961-706e-318f-a855-db71a9d9a98e | -10.60968 | -52.82432 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10053b78-f490-33cf-b717-ddfdaab1b48e | -10.60909 | -52.82745 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 324e6640-a70e-3045-9b37-557d43b04cd8 | -10.60856 | -52.41536 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1a11d38-b922-3832-9eeb-e024da242375 | -10.6085 | -52.83057 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f94e1b70-9dc9-38e4-95ad-f30fedff625b | -10.60803 | -52.41825 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b492841-f992-341b-8c96-cd9fea314ad8 | -10.60749 | -52.42115 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f675c65-1a85-3c60-ab36-d1d6f64f0f19 | -10.60454 | -52.82342 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca97037f-29bc-3b6b-8b36-c175eaff22e3 | -10.60395 | -52.82655 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 662ce86e-2f7e-31e8-93f4-ba3acff441d8 | -10.99601 | -52.88078 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfe3ec50-9696-3311-95af-d90b2d27e023 | -10.99365 | -52.87929 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 635ce0b6-32a3-31c2-b339-c1923de5c0b4 | -10.99308 | -52.88239 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b3bec33-f7ba-36eb-8408-653560e8dc6e | -10.99091 | -52.87975 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9095d195-9cab-34bc-b0b9-b95b6056b45b | -10.99032 | -52.88284 | 2024-10-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 420b762f-c10a-3034-a275-52e66878a0fb | -10.45172 | -55.09811 | 2024-10-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b196f5-b036-3499-9d91-f3403e1536e9 | -10.45086 | -55.10262 | 2024-10-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 654f2a30-53f4-3338-98aa-08bedc6d4ad4 | -12.03312 | -54.65231 | 2024-10-25 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62642cf9-7187-3015-b56d-83a568b062a3 | -12.03237 | -54.6562 | 2024-10-25 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06b6c97d-851a-337b-a93d-38136bd36b65 | -11.35188 | -54.48485 | 2024-10-25 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 708091d3-2566-3c9a-bffb-61d3d1b529e4 | -12.61851 | -55.22335 | 2024-10-25 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774f27e8-69ee-3345-94bd-846fb7ba74a5 | -12.61787 | -55.22635 | 2024-10-25 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6d7e74b-2bd2-30eb-8966-9b118a7208b0 | -12.50162 | -54.35508 | 2024-10-25 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02522a79-023a-3113-b24f-52a5c9650562 | -12.5009 | -54.35872 | 2024-10-25 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4e978b3-50d9-326d-8bcc-2cf078e58ed4 | -10.48379 | -55.62286 | 2024-10-25 04:17:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01740bd0-1f54-3fed-9c73-ce81b0ca1837 | -10.10419 | -55.38958 | 2024-10-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aceaf7a-a2e4-3890-9343-31d8aa6336ce | -10.07808 | -55.49121 | 2024-10-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6fab8e9-907f-3f3a-be1b-f148cf32bcc7 | -10.07715 | -55.49609 | 2024-10-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c79b90e2-4b55-3fbc-a8d3-1e27c2f046c0 | -12.02629 | -57.08485 | 2024-10-25 04:17:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12da5b2b-644a-35a5-a65f-a5b53d9e1de9 | -12.02512 | -57.09063 | 2024-10-25 04:17:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30060d32-a16b-3230-b00a-413b94638439 | -12.02491 | -57.08633 | 2024-10-25 04:17:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e96b799-4d9a-397c-991a-4d7e0eb399fe | -12.02369 | -57.09216 | 2024-10-25 04:17:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b4fd1c2-09ca-37e2-8de2-909065968c30 | -11.88784 | -56.21651 | 2024-10-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 010aa204-bdd6-3b77-b0fc-9e608669a7f4 | -11.88477 | -56.20867 | 2024-10-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 399b2055-530a-3d3b-bd6e-a940f7d3abe4 | -11.8838 | -56.2136 | 2024-10-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdfcb769-382b-318d-b7b9-b538e99a00d0 | -11.88282 | -56.21854 | 2024-10-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6fab7f3e-3eaa-3ba3-aa67-bdc1c81e6f48 | -11.88264 | -56.21032 | 2024-10-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3dc6547f-6b6d-3954-9ff0-db31b6c4c81d | -11.88163 | -56.21524 | 2024-10-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6541e57-8f93-3aac-9cef-45692392fd42 | -11.8776 | -56.21229 | 2024-10-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b9579f9-c52d-391c-bbff-c9bd870b2d62 | -11.05964 | -57.82396 | 2024-10-25 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aca36f7f-1358-3f57-8977-1106b1057519 | -23.84934 | -55.31891 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d2680d8e-ac83-39d7-9e49-c254e70b95cb | -23.84355 | -55.32299 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1daa50aa-e175-327e-81c0-6f5fd86ea21d | -23.82359 | -55.29357 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f5d718bf-93d1-3c57-8c0e-e02b80d15ad3 | -23.82133 | -55.28909 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 919cd618-c9ca-3ed8-8e22-47144ac05ae2 | -23.82019 | -55.29438 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d888e27f-0fc6-3984-8997-a021ef6af72c | -23.81781 | -55.28262 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 878ff4d9-f006-3c47-a354-81b88e3c78da | -23.8165 | -55.28051 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 02e4afc2-8c22-34e5-a861-1d751e9f27ff | -23.78749 | -55.30188 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| c24532e0-270c-33c6-8928-377334c04ae8 | -23.78281 | -55.3008 | 2024-10-25 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 16a36460-566a-3e52-ae01-cd96a7e60d7b | -17.4031 | -39.87083 | 2024-10-25 04:19:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a90608c1-9d71-3435-8e30-61922add7952 | -17.61052 | -42.5568 | 2024-10-25 04:19:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41a4c8a7-0bc5-3d4c-80b6-5203d75bb645 | -17.68456 | -42.11332 | 2024-10-25 04:19:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9460a2b4-3ff9-3dd1-871f-6cb00424408c | -17.68398 | -42.11546 | 2024-10-25 04:19:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 20e9ba29-b250-341d-81ed-f090fbd1fac8 | -17.01956 | -43.25161 | 2024-10-25 04:19:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fb192ef-e4ba-31df-b0df-460e0bbf289c | -15.66868 | -55.97932 | 2024-10-25 04:19:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 7e0b1885-cd3f-3865-97e3-0d0541ac6aee | -15.66782 | -55.98347 | 2024-10-25 04:19:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| c5b2af01-0eb0-37dc-a8d0-57e80821976a | -17.01522 | -55.99927 | 2024-10-25 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 3587c117-b4f3-34b7-aac3-84c55c273bba | -17.01441 | -56.00318 | 2024-10-25 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| ca721ad0-b625-3998-96b1-a44a8117f6ef | -17.01359 | -56.00713 | 2024-10-25 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| a6230620-097a-3137-bc8e-aca2dbcd11aa | -16.56651 | -56.24575 | 2024-10-25 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9943c627-bc57-3531-a447-855500947a83 | -16.56563 | -56.24989 | 2024-10-25 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9b2ccd88-a04c-3f9c-b729-fbcdcc5f8716 | -16.56081 | -56.24444 | 2024-10-25 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7d2e5f1e-f667-3a3e-bf84-887606ba5566 | -16.55993 | -56.24858 | 2024-10-25 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1219d97c-1053-39bb-8f83-a8d60f99c1a0 | -16.83675 | -56.70758 | 2024-10-25 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 39c68007-57eb-3de4-8375-2914a1af1101 | -16.83652 | -56.67987 | 2024-10-25 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ae4c1239-4dc1-342b-b2ff-5aa68fd35123 | -16.83581 | -56.71199 | 2024-10-25 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 467bdbfe-7c22-3095-b1fc-fde5e6f1e9c7 | -16.8307 | -56.67853 | 2024-10-25 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1b8bce5d-3dd5-3b28-a0e0-eaa17f1d2e0c | -16.82976 | -56.68291 | 2024-10-25 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 430a4c74-0e49-385c-ad5f-503adb033fd7 | -16.74807 | -56.67074 | 2024-10-25 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 711d4bbb-63a0-3ddf-a341-2c5bf51663fb | -16.74715 | -56.66869 | 2024-10-25 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 385782e6-8cd6-36ea-b1d8-90f8a3a1fecb | -16.70329 | -57.44944 | 2024-10-25 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c6f24b16-fedd-37d0-bea1-8c91cb29b230 | -16.70223 | -57.45439 | 2024-10-25 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ec436b5d-2d73-3fb7-9cf5-48516821674e | -16.65006 | -57.45784 | 2024-10-25 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |


[Clique aqui para ver as próximas entradas](README46.md)
