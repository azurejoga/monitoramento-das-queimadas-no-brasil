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
| 4a9c186f-83fd-34cb-8448-b7226de05e37 | -2.92119 | -48.72319 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4a45980-2add-3070-9f3a-8d3b311070c4 | -6.03529 | -46.55586 | 2025-10-31 04:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94ca4ecd-83c0-3f8d-a90e-dee6d752616e | -3.47329 | -51.58861 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7297fb41-46e4-3a1e-8ed8-cbcd0a2de4c3 | -2.91653 | -48.72751 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7f91ced-8e64-3e62-9a9f-03c7af420631 | -3.3288 | -54.07932 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1c850cc-2be2-3200-a4f5-ec8fd88f2686 | -5.8788 | -44.71107 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eea5eeae-5eb3-3193-85b3-c6e69302903d | -4.43109 | -48.0091 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f0ac6cb-2ef5-350b-bd4a-344b05c5d594 | -6.2034 | -42.51341 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 01c8eed7-411a-35af-ba1b-759941fbe855 | -3.01492 | -49.4486 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6a497daa-c54c-370c-b528-697ac911a19e | -4.05217 | -47.50372 | 2025-10-31 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd6c60fb-c618-361c-b25a-ed970f02a3be | -6.1073 | -41.72787 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| eb82eb3c-4070-3679-9cc2-d336097af0d2 | -2.45026 | -49.01086 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6962d037-1bc9-3cb3-8cb7-ae18e9d68a7f | -4.77009 | -45.99005 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94b207d7-ccdb-362a-9154-c0cc89d6508f | -5.13964 | -46.1467 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77500c3c-41a2-3ea3-b725-dc0e6868d286 | 1.29486 | -60.42049 | 2025-10-31 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4be274e1-8615-37e0-9eb0-f6f4caa4079a | -1.48097 | -55.67719 | 2025-10-31 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b4b92a6f-e873-3cd3-827a-b7a042375610 | -3.22859 | -50.64834 | 2025-10-31 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 616dc13c-0263-39b7-abf7-e9d269c562e8 | -5.28022 | -45.42246 | 2025-10-31 04:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43a0a589-9695-3913-b614-7681bfeac054 | -6.01458 | -41.97232 | 2025-10-31 04:55:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 185b3f45-c3b1-3570-b085-711a77094909 | -3.99606 | -48.32437 | 2025-10-31 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f35e003-0b97-34be-86ac-e88b9e88b97c | -3.93329 | -52.23323 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50090f2e-f1c8-33c8-88f2-a241e4e0601e | -4.49544 | -55.79965 | 2025-10-31 04:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b54afffe-2ed4-39df-8bd0-296e3998a944 | -4.24458 | -55.87343 | 2025-10-31 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d258155-d9de-3888-b03e-a3c28dcbf7c8 | -5.01939 | -45.56568 | 2025-10-31 04:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c86c6af3-29d8-3dd0-bd7d-29778c22298a | -5.26245 | -45.51282 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4be4dea-c280-3b76-9e93-9ac1f6ee7065 | -3.94274 | -46.97007 | 2025-10-31 04:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 361fbc8d-e2b3-3330-9d76-749673fe43b5 | -4.83399 | -45.32757 | 2025-10-31 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af231487-3d98-3890-be79-a4f28d3d03f4 | -4.27395 | -48.64413 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eb4b096-d459-3223-9d3d-757339a9483c | -2.31683 | -48.5797 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 23d560b5-72a6-39c0-9a22-d0061a8809fe | -3.54524 | -46.42794 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 536f6b3f-aed9-3272-bbf0-17e3822ce0c3 | -4.67511 | -45.81103 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51aaf699-3ab5-3a72-8405-0c5dc33589cb | 1.10389 | -52.41792 | 2025-10-31 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c853bc8-57b0-32ae-9179-8d8df757712d | -2.66521 | -54.07811 | 2025-10-31 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f2dc511-37a7-333a-9705-e2db7d9dd7d8 | -4.92104 | -47.32383 | 2025-10-31 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73e0feff-2aa4-39d4-b871-77ad19063871 | -3.51964 | -46.00019 | 2025-10-31 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c156e913-8b1d-3c7a-be4a-7698ceaf4278 | -5.93542 | -49.76652 | 2025-10-31 04:55:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de1fe790-44e7-36ab-8822-4393257f2170 | -4.75758 | -45.7795 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c621b58-df9f-3038-a461-0f10c34b5835 | -4.36246 | -45.65332 | 2025-10-31 04:55:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c591e854-ac23-33b7-8f97-0b81eda403ba | -4.64141 | -49.4874 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a0af8cf-99bf-3dc7-8e36-0ab15ae973b3 | -4.14726 | -50.68293 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dafa09e0-2790-395c-903c-3ded0813ba8d | -4.55623 | -45.64977 | 2025-10-31 04:55:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05cd2a53-7cdb-3731-9578-36e6178b359c | -3.32603 | -54.07533 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2c7d49b-285b-3c02-a2a5-69d51e327958 | -4.84568 | -42.73205 | 2025-10-31 04:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ce18c5a6-e71e-36a8-bb5c-81e465b53264 | -6.09301 | -41.7863 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d51db1b3-5b2b-3f5e-9355-b52b390ff7a9 | -3.0224 | -49.44975 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 62f820cc-b644-3bbd-8fd3-2e65d2a185cd | -3.23503 | -50.65337 | 2025-10-31 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6fbc52c-625d-3f2a-a1b1-6cac981d2ca0 | -4.74513 | -45.8982 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df5cc679-f0d4-372f-9f7c-9c89692e4476 | -4.85709 | -42.73821 | 2025-10-31 04:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8c877b5-03f0-33fd-a10b-ff07662cd757 | -1.75259 | -52.10415 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae2833a4-1251-39c9-a01a-0aa99531b462 | -2.90395 | -49.80418 | 2025-10-31 04:55:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2378c30-20cd-3142-b058-5252e616f70d | -2.90198 | -53.95856 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0e69f30-c075-3956-af01-738f66ead85e | -4.81085 | -43.02206 | 2025-10-31 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3fed7fbd-86aa-39c9-9e3f-af6d2bf9298d | -2.91017 | -54.29491 | 2025-10-31 04:55:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ab77a2f-b74e-3330-bd3f-48bc408d1868 | -5.61531 | -45.97604 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e41db945-74e1-36f4-84a4-ec0908ef100e | -5.05814 | -45.9326 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70fc31eb-6f11-3a9b-8c12-fd370ea97dc2 | -4.74029 | -45.89733 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 661c855d-5347-3156-92d0-a1d8e8498708 | -2.89215 | -47.85123 | 2025-10-31 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a8e17d9-86d6-3db6-a394-89f83f2417aa | -5.41622 | -41.24265 | 2025-10-31 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f81af16f-baa8-3df9-b0c6-465c35ce846c | -5.20492 | -45.4152 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87491b4d-57dd-357c-8faf-0c5da7b94e75 | -2.42583 | -49.30001 | 2025-10-31 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 60fc3c74-c00a-31a1-944f-b6fcafb70645 | 0.21255 | -51.44104 | 2025-10-31 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b93f08d-2870-3ac7-8ee6-044134caa62f | -1.93247 | -54.06318 | 2025-10-31 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8032743b-7c8f-33f9-b457-d7e50e99715f | -6.10823 | -41.72106 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 168e9039-ec11-34b4-80f2-0aee8c007393 | -1.05746 | -47.3434 | 2025-10-31 04:55:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 32578c7b-9c2f-3ec1-9589-bb0b215f802b | -4.21456 | -48.0934 | 2025-10-31 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 389ac8f8-2cb3-309d-92e2-d3aa25399322 | -6.13691 | -41.70492 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 36a4c99c-3711-3941-ad37-f76f14f7f61e | -4.4841 | -45.19338 | 2025-10-31 04:55:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58875773-7a37-32d2-9784-6d75adf17133 | -4.49456 | -48.27836 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec7c785b-14ef-39e3-9250-211a1a61a249 | -4.42952 | -43.71526 | 2025-10-31 04:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24b16da1-c152-3be5-ae6c-ba2d2cd0e553 | -3.30301 | -51.58089 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eed1929-a530-3046-839f-7490be1299f6 | -3.48992 | -52.35196 | 2025-10-31 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acb19fc4-6579-3570-8927-9b093dc094a5 | -2.31292 | -48.57909 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ba014ee-5410-3bc8-ad01-ff736f1d9948 | -5.20659 | -56.09625 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 882867b7-80e1-36ec-893c-a6ebd1931429 | -10.64027 | -52.18907 | 2025-10-31 04:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfd0226c-2257-3ca3-a1ca-549b51f38ebc | -12.53592 | -47.54678 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86b79d03-0746-393b-903f-68518f0d15ac | -10.5062 | -42.40485 | 2025-10-31 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 3b4f77a0-8a15-3081-a09d-5b130379b104 | -10.64381 | -45.24741 | 2025-10-31 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c01f739-5d47-3c67-9b36-fb2322eac03c | -12.6058 | -47.5287 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a61f32e7-e63f-3477-9de9-21b4f552b975 | -11.12224 | -54.6335 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a9b9ab3-0718-3d35-892f-90289263808c | -7.08388 | -44.93755 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30d17968-879d-3cac-9f6d-ab396af0d0a1 | -13.53561 | -47.42461 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e164af5-1619-34e2-b97d-c046408e2d99 | -7.81652 | -46.39957 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2f6a98b3-98da-32ea-9b28-c69448f6ac37 | -12.82495 | -43.49305 | 2025-10-31 04:57:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d3f5bf6-acb9-3d49-bb66-399aaae72616 | -10.43418 | -44.33101 | 2025-10-31 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8f07937-be79-383a-a95a-21c1687e1c9f | -7.35133 | -44.98934 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 16295abd-fcc5-31ff-90c9-1bb29da5f801 | -7.3528 | -45.00169 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9bf40c7-525b-302e-8439-4ab7352625ac | -9.85602 | -44.85192 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57640ad1-bd8c-3c7e-8f4c-b8fa47057093 | -9.28059 | -47.65385 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 446c85ae-bea7-323f-829c-9bf5cfab41d9 | -12.06633 | -47.33655 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02aa1107-9d3e-3da6-82d3-58a7d5aa43fd | -10.48822 | -47.75493 | 2025-10-31 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b95fdf8-b0fe-3da8-9c3c-98a1570ecde4 | -12.28881 | -48.06604 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d6d839a-4133-3013-ac3d-91c08d946123 | -12.6027 | -47.52818 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c0ff829-cfd7-39ec-adff-269bdfbe5479 | -9.46668 | -46.99379 | 2025-10-31 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8aff3e3-8d66-35b2-b989-a664b7cd5e3b | -6.77522 | -50.52402 | 2025-10-31 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd4c23a4-33f6-3d9e-89f6-42d28cc0af49 | -7.07847 | -44.93703 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd0613ab-82b1-3d35-8479-a73107067d82 | -10.9304 | -44.76396 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 006f30a8-f171-358f-905d-3b9ec3b319f4 | -7.61744 | -46.46801 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da89e4a0-9c52-37d9-b09c-0c220ca97ea3 | -7.6643 | -43.59776 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67077be9-3d2e-38c7-8f55-582b2d670709 | -6.85406 | -45.13309 | 2025-10-31 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c478f692-4708-3ec2-ba59-57a36d46a385 | -7.66004 | -43.60026 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README36.md)
