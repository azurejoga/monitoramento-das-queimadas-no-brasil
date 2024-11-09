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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c71db06-d1fb-31ca-a7c3-0813a78574cc | -5.7475 | -41.9927 | 2024-11-09 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| c567d56e-b7bc-356e-99c5-7d75aef2d76d | -4.1244 | -43.6064 | 2024-11-09 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ea340855-76c2-34a0-afa0-c34d8ee09f77 | -0.3403 | -51.4388 | 2024-11-09 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 352c26c3-2cf7-3ccc-b928-6c52c639c047 | -2.0478 | -46.0903 | 2024-11-09 14:30:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 141.2 |
| e63f8f6d-75bc-3ce3-b34a-98890c144502 | -2.6758 | -46.7806 | 2024-11-09 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 9e81f832-d644-3f91-95a9-11f7baa9977c | -3.9485 | -48.1508 | 2024-11-09 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3f9cee63-6635-3a45-a31d-14450c50a13c | -2.2032 | -49.8505 | 2024-11-09 14:30:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 6855f8ce-fa7f-3d28-8e8d-6ac0638325c6 | -1.535 | -52.0258 | 2024-11-09 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 19e742c5-4f10-3b52-bdd3-b935166d84fc | -3.5464 | -43.5431 | 2024-11-09 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0076a8fa-d804-3778-8928-371d53e5cd66 | -2.0086 | -46.8205 | 2024-11-09 14:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 4f582a36-a538-33d1-80a8-f5e332244d21 | -0.3403 | -51.4595 | 2024-11-09 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2d942183-5dfa-32de-bae6-e5c29fce4510 | -7.1592 | -41.9834 | 2024-11-09 14:30:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| b940afe4-e348-3a2c-834b-1944267a274a | -2.2315 | -46.6169 | 2024-11-09 14:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 29178bcb-3283-3d0e-8e06-efe07617472e | -1.535 | -52.0053 | 2024-11-09 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 37f80ecb-e80a-3f01-974f-7b8a70824728 | -3.0319 | -50.3547 | 2024-11-09 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| f40c2e4c-2283-345e-a6f8-27a88e761f29 | -3.5462 | -43.5663 | 2024-11-09 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 72a2e5d8-79a0-3284-94e2-b037ec9e51f7 | -3.6111 | -48.9167 | 2024-11-09 14:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 76bc227e-6682-3fc8-9fe3-c815343b7650 | -1.1306 | -51.9485 | 2024-11-09 14:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a55b4ff0-cf2c-3243-a5c4-7d153e2a0197 | -2.8659 | -50.3176 | 2024-11-09 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 02c86206-dfb1-3a92-a25c-3118d96734c4 | -2.3061 | -46.4825 | 2024-11-09 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d3e4b331-a912-319e-88ce-1e0f34426798 | -3.2154 | -50.6213 | 2024-11-09 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f42312fa-20d0-3feb-a63f-e9746aca47c8 | -2.379 | -46.8552 | 2024-11-09 14:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 179.7 |
| 611324d4-e543-3a4d-be93-6a9b3c2f4de2 | -1.5348 | -52.1489 | 2024-11-09 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b2991636-371e-3299-bc73-9fd38b1caefc | -2.0085 | -46.8425 | 2024-11-09 14:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 9d62fdbf-2add-3821-b34a-54a5717d9b54 | -1.4806 | -51.5737 | 2024-11-09 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 364de589-83e0-32c6-8404-856991cf8c18 | -5.1357 | -48.2436 | 2024-11-09 14:30:00 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 866764b7-25ae-3c9d-a193-e903a272b835 | -0.046 | -50.7755 | 2024-11-09 14:30:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 5d157899-933d-39d3-8a74-53f821989cfb | -6.1366 | -42.5544 | 2024-11-09 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 5dece464-cdb9-3c7c-a57b-c145129840e1 | -3.2346 | -50.4533 | 2024-11-09 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a465ffa1-9793-34bd-a4f8-30cdbd5c72b2 | -2.3733 | -48.5703 | 2024-11-09 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 749a52be-ad42-38aa-83e1-f0c51e998129 | -6.9974 | -41.3016 | 2024-11-09 14:30:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| e17e577f-e569-3c07-b359-52b65c5a06b3 | -1.5347 | -52.1694 | 2024-11-09 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| a0861cfc-d97e-3524-8e06-d381b3335424 | -3.125 | -50.1419 | 2024-11-09 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 20286c26-5761-3874-9cdd-52b91da8db32 | -3.2538 | -50.2639 | 2024-11-09 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9af7da87-bb3f-3f9a-b554-b849dd543965 | -0.2115 | -51.6455 | 2024-11-09 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 04f0b7bd-e077-3cbf-86c0-2726d79856a6 | -3.3744 | -52.3545 | 2024-11-09 14:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| df2d59d6-a568-326e-9094-67ee3be1142e | -5.2483 | -48.0857 | 2024-11-09 14:30:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| aa945d45-1640-33b9-b293-447a2f5763ff | -6.3689 | -45.6483 | 2024-11-09 14:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 881fbad8-45e3-31cd-9265-b44aba58d5d1 | -1.7692 | -46.2741 | 2024-11-09 14:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 8eea2ed1-5e79-3bd1-ae0c-676f013aae44 | -5.4734 | -43.2646 | 2024-11-09 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 178aa83b-440c-37be-b1d4-b812f5080bdb | -2.2804 | -48.7226 | 2024-11-09 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 24bc44d2-2784-34c5-8117-6314f4f4c872 | -2.2803 | -48.744 | 2024-11-09 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 980f5b89-3629-3dd8-9ce5-018de3f5bbd6 | -3.9483 | -48.1724 | 2024-11-09 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 9034f215-0663-3fa6-a292-93898d705004 | -2.0842 | -46.3334 | 2024-11-09 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1b2059fe-f16b-30a3-a823-ddfd2ff03e8a | -2.646 | -49.8819 | 2024-11-09 14:30:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1607a901-6547-30d3-83df-c1fc6559502f | -2.2642 | -47.9916 | 2024-11-09 14:30:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 2f068cce-118e-3212-87d5-21a9f36bdd00 | -2.0836 | -46.5103 | 2024-11-09 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e0417c95-cd95-35a1-9aa4-673bc2309320 | -3.2153 | -50.6423 | 2024-11-09 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a308d7ee-4de5-32b8-b53c-db448f30ab3e | -2.0805 | -54.6877 | 2024-11-09 14:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bcf5d42c-6401-3984-9e69-adf76d6e9dfd | -2.3556 | -54.7427 | 2024-11-09 14:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c5ea9965-514f-3b0e-bb51-c89c22ea7ba8 | -3.9625 | -48.9883 | 2024-11-09 14:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9cef8196-6ab8-378a-9063-a91a40a3dfb3 | -2.8921 | -48.2977 | 2024-11-09 14:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f0ecbec4-2da8-34e0-8014-fc1ede8b9bc9 | -2.0835 | -46.5324 | 2024-11-09 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| d3e4c7e7-a6b6-381a-9618-d3f420591bfa | -3.5305 | -50.3387 | 2024-11-09 14:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 82d6c24f-0aa5-3ade-a321-47eadda52e5e | -5.4359 | -43.2673 | 2024-11-09 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c52c42ef-77ab-343a-aa71-9b63b87d11f4 | -7.1778 | -42.0055 | 2024-11-09 14:30:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 82d5dee5-b837-3f6f-9636-5d493c735111 | -2.2417 | -49.2993 | 2024-11-09 14:30:00 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 3350fb6c-5c3f-343b-9e3a-30b6949ca0b3 | -4.2878 | -50.4356 | 2024-11-09 14:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f6260224-c0d4-3d2a-90ba-4e3673f99a70 | -4.5713 | -43.789 | 2024-11-09 14:30:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a92e6e96-4ec9-3aee-8d29-10c34dec3e21 | -0.2299 | -51.6249 | 2024-11-09 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 102.5 |
| e731ec4a-8197-34ac-879f-cae56fc66dd8 | -2.7221 | -54.9148 | 2024-11-09 14:30:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f9ddcc01-97a2-3f8e-9b0d-f0e527fb940f | -2.3605 | -46.8557 | 2024-11-09 14:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| c56c674a-820e-36b0-bca8-51d326442440 | -6.1363 | -42.578 | 2024-11-09 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 68f44fe3-8d5c-3404-bdf1-90776183dcc8 | -0.5992 | -49.5352 | 2024-11-09 14:30:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 91f573d1-4447-37f6-999b-623e34341982 | -3.3694 | -45.2865 | 2024-11-09 14:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 887dd16b-85a9-331c-9ca6-2872465af39e | 1.3164 | -50.7255 | 2024-11-09 14:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8eeb6d7e-43a6-3729-bb5c-970b6b686621 | -2.5781 | -48.1777 | 2024-11-09 14:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a47c4498-74ba-30b1-a067-2fc016c00c93 | -4.1246 | -43.5833 | 2024-11-09 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9e56fcf3-828a-3869-80e3-e05a143588d0 | -0.2482 | -51.6454 | 2024-11-09 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 118eb0be-bc1c-35d7-86af-3a8627d44cbe | -0.2299 | -51.6455 | 2024-11-09 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 180.2 |


