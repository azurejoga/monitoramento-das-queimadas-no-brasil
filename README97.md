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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4ece668-8913-3010-bc52-0ab53535a426 | -3.68671 | -50.92812 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78e8d9d9-d0dd-3e21-b77d-96cb66f4e60a | -4.20286 | -50.68986 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0312aa3d-57b9-3a10-bd90-7f619933f33d | -2.88108 | -53.3098 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea77cfbe-5148-3077-8677-86364d367e78 | -1.30189 | -51.72826 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19901b00-41b9-3df1-9b37-ee3add4284c3 | -1.33784 | -54.62132 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b81d810-09f5-3e6d-9e6f-398005bdc0d5 | -3.24982 | -53.85785 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cdf95d6-b03b-3849-b3c2-b55b0828fb9f | -3.09539 | -53.72477 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f92358f8-9853-34a9-a56e-56ff82eb97fe | -3.30186 | -53.83324 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6c7946e-f116-3127-b413-4134fc8c6204 | -1.26226 | -51.63106 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a8d23e9-b4c0-39dc-8830-57eafe76144d | -3.77448 | -51.67918 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb53e033-bd1f-31d5-8ad6-d97c2ba65171 | -3.28924 | -53.67061 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aee53b27-de44-3930-b408-19708419b9bc | -3.25882 | -54.10823 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ce43961-697a-39eb-b1ef-61dcc58d6c94 | -3.1713 | -53.6454 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18f4b0a2-b24f-3f97-a4a3-f87cda90d407 | -2.81049 | -55.30045 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831cc5f6-046c-385d-a69a-68bb078602c4 | -4.17838 | -50.66557 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b12e1fa-aec8-3e3c-9410-4287d37246cb | -3.29939 | -53.69425 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d27efc19-69e6-3f1d-988d-d04a695a6ac5 | -1.59618 | -55.55598 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e416613f-98b9-33ae-9b2e-c0d2e1351524 | -3.09316 | -53.2932 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5eb77bac-e6a6-30f4-b5e4-3b6b59bd3149 | -2.60471 | -54.20295 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 847c11a6-542b-39ec-b09e-35c383977012 | -2.52086 | -48.46488 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 623dfe3c-685a-3424-b50e-4b056aaae8d2 | -2.36025 | -46.87752 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4cb9144-5bfb-3c59-b035-1620d3bedbc9 | -3.00487 | -53.23125 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d12c53c4-41b7-3cc3-afbd-131659fa6e97 | -1.58011 | -53.85521 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86c46117-d717-33f8-8af0-b10cbf329406 | -3.10967 | -54.04228 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 071229d1-a72f-325b-a7b3-1a607921cf35 | -3.23226 | -54.73052 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c259514-c7dc-3e78-98cc-47926d597ae0 | -3.22473 | -53.63543 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 487f76f5-daaa-3a07-bba3-b9e59f358da2 | -2.60191 | -53.98104 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1491f6d6-7581-3acd-8175-0bd12a074bad | -3.29177 | -53.83168 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d1ec67d-c1c1-3816-a3d2-c051724b5938 | -2.57851 | -53.97741 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 485afffd-47b4-37ae-8d83-8baedbc26c0d | -1.29728 | -51.72633 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb3d4d56-b47f-35c6-9d25-f7a74502639a | -3.45887 | -50.23102 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d092d042-bf75-3d66-a126-72a1a25592b9 | -2.87041 | -53.97631 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a52ef28-cb22-3480-9492-debbc689f64f | -3.09088 | -53.70945 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1873576d-b883-3f91-8988-dcc61246574e | -2.5792 | -54.21331 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ac77ab9-f6f5-3b3a-8f88-66e737033ff2 | -3.11395 | -53.76041 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e27c0c5-8ecd-391f-9e90-e7d1fcff76bf | -3.31242 | -50.02816 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fb1f13c-5da4-3a6f-a910-830e5c099ec4 | -3.39447 | -50.30517 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d986775-9704-30a9-a775-f8ed5d74a62b | -3.09359 | -54.02129 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12b6c51d-e8ad-3a34-a822-3bf8c6fc0f0e | 1.20317 | -55.94553 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f9b461c-c80f-30d3-9de2-11bf88e1aac8 | -3.14822 | -53.83857 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b186abf5-5672-36c8-9e94-3c68bbcc539c | -1.49896 | -51.93898 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d48c2a73-1e8b-3c62-979e-0de5bfcd0529 | -2.96505 | -53.8899 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb6d3c51-a0aa-3157-8a43-27d9198a09d2 | -4.19107 | -54.7632 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c81edab-505f-3f84-bbd5-fa1e102f2965 | -4.87717 | -41.30449 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| eba396c1-f2c0-3d21-b027-073daef5e58c | -1.04019 | -53.35493 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74895d97-40b0-35cf-96f7-4998d849c9ab | -0.8197 | -51.60062 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91a7e018-2012-35cc-a502-f45a9ab50345 | -3.25043 | -54.09616 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5734ea25-83d8-3200-a071-0574e6433bf7 | -3.10353 | -54.03771 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1abdead-5d38-3923-b8b3-28164016991a | -1.90818 | -52.87774 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8e94a8-75c4-3763-b1fc-3008b49b83fb | -1.88141 | -53.31616 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50056b2c-fa3c-3a0f-a5ba-a3338838a5ce | -3.27072 | -50.43931 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e0dec05-931b-3849-8c44-29551fcb22c9 | -1.99129 | -53.28506 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e34b2242-1d46-33a8-ada1-de3cd54dd7f5 | -3.31616 | -51.62897 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f10a087c-0a74-3894-8383-e208598eb2a9 | -3.29668 | -50.24149 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 302265d1-b3c0-3d10-bc18-a31058892f45 | -1.97006 | -48.42963 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faf01ddc-5311-33b7-b797-d2e5fb3fc715 | -1.3896 | -55.19501 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ef9fa66-88e3-34e5-96be-8a973d506429 | -2.72787 | -48.66444 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c539a7-23cd-310e-a9e9-7e6fb17ecac8 | -2.57521 | -51.83845 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13321bc0-c88e-3c8c-a0ce-8f154e0fd4f2 | -3.22112 | -54.17415 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b988165c-5da3-3c37-8c84-fdeed8d51c51 | -1.36183 | -55.17645 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9819baf3-fdf5-3173-803c-30f5001dd308 | -1.85504 | -55.61398 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f8755086-1cff-3041-b424-652dbabe5529 | -1.04057 | -51.735 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ef8d0bf-ebe3-375a-8083-e94cc47505d9 | -1.42381 | -54.7615 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c84724c9-5359-3ef9-8f82-b51c843f85b6 | -1.35072 | -51.9669 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d8a9fec-cce0-3865-a903-e8538c998eb6 | -3.34006 | -53.20638 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a58d6ec-1815-3776-8013-f2716f9b1cc2 | -2.72464 | -54.108 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99600588-a7a2-3282-83a2-ec56df3f4395 | -3.29121 | -53.83523 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b458440e-cd93-3d47-b454-60bc0f4b83d4 | -2.88234 | -51.78458 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a15ea1d8-deaf-3683-918d-b24c113f536f | -1.52024 | -52.03511 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cda5d785-b654-3877-9904-4c944d43633e | -1.19612 | -53.71699 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a01a6460-55ec-3113-bd8f-da11710e6cb9 | -3.74908 | -49.93235 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f7838c0-12cf-33e8-afe0-9e870f2efd83 | -1.10251 | -53.3861 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab7a5044-c9c0-34d7-860a-fcd7422c15a1 | -2.86711 | -53.99736 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65685e71-9323-38e9-8ea7-731706978cee | -2.9712 | -53.89448 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4e62373-4f55-357b-9578-3b92738d67b6 | -1.30799 | -46.77628 | 2024-11-30 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc1ea64b-b099-34cd-9902-05df0a136e99 | -3.6389 | -54.44611 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de16c461-886f-3d7f-b91d-51aa5aeef9ab | -4.01951 | -47.00243 | 2024-11-30 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8530d2ed-9012-3c39-8b24-c17974960c7b | -3.07529 | -50.33348 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ac4d221-1319-3c89-bc24-6f9091c81290 | -2.81594 | -54.03968 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60eba40c-66c3-3a5e-8788-430d97e46bcd | -2.46297 | -53.96683 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afdc9bd5-8eef-332c-9daa-d07e94f6f6a2 | -3.58079 | -50.33687 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90ffc82f-c427-30e3-acd8-d8a7d5118d00 | -2.88169 | -51.78872 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6609db29-3fee-35f4-b349-1e6fb636c989 | -3.2495 | -53.63192 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f34b3610-7539-31be-a5a6-316936317c8b | -3.97151 | -41.5105 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 74d26def-28d9-3d02-8ed6-4913c2a10fb1 | -1.39062 | -53.63993 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c058762-46ec-30f6-bfd4-ddc9c6f900e9 | -2.8801 | -54.21407 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bce48fcd-fd96-382d-a32a-b4a82d731caf | -3.2388 | -53.63395 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0378f263-3ad3-3bd3-be97-0fe1327e116c | -3.5449 | -50.18811 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7f75cbe-2957-3a32-b99b-4d71e2a0b582 | -1.80453 | -52.73668 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 153cc820-7923-35b4-97e9-afb154d6f832 | -3.21037 | -53.83743 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c117274b-8c78-39a8-8b5e-9c9482b63733 | -2.85237 | -46.68992 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5931216-c2fb-38a5-906b-9eda0f3dd54f | -3.05406 | -54.05473 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f483ddbb-3b6f-3234-9a5f-fe7088ec1a58 | -3.09763 | -54.29458 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1995abfb-74e2-3f4b-a8c8-0c7f21cddb53 | -2.21042 | -48.38389 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4303e57-3766-3b7c-8621-aa033a1394c2 | -1.39509 | -53.63331 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37a21eec-f997-357f-93ec-c17a2c95fc34 | -1.48882 | -52.32755 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af13c561-22c0-3cdc-b318-9081ca6c0d50 | -3.28036 | -48.77206 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ba728b8-3001-3945-ad41-a6162f794d65 | -3.28666 | -48.75991 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68033776-bd6b-340c-b17c-4f44c0bd6ef1 | -3.03235 | -51.53772 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6dacc2bd-836b-39b7-aa46-b90966db6722 | -2.89302 | -53.32221 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README98.md)
