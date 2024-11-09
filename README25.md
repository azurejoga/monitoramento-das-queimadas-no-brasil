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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f018363a-e2e6-34f2-88b8-48788779b263 | -2.40271 | -47.81312 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0c61e3b-967f-3adc-8739-15e309e4b667 | -2.37218 | -46.74514 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88413472-7cec-3aaf-945a-c3088c21b71f | -2.40985 | -48.87567 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 393df181-c5e9-3aa4-8c8b-7b327bec770e | -2.58205 | -49.14339 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ceb89344-fc8d-3da1-b486-ed3cf783a1c6 | -1.85152 | -46.28612 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 096b2ce7-56fe-3e3a-aa02-5a3353831462 | -2.40862 | -48.53111 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc37bf61-3345-366b-a3cc-f10b5702d493 | -2.49694 | -46.22643 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f6454fd-3901-33c8-9e64-682ad387043d | -2.39924 | -46.7669 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 697d8532-fd4f-3d6b-b62a-5dd9b7e29612 | -2.2147 | -50.76572 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e0f6fd8-24e7-3453-a623-daa002eb1f43 | -2.58037 | -49.13168 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c25d442-bc50-3707-a994-ee522e2120c2 | -2.17344 | -48.43224 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad615b7a-4ec5-3726-ad94-de9111634709 | 0.84757 | -50.17336 | 2024-11-09 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d35ccd2-35c7-380d-9a02-b11d0cdca820 | -2.19241 | -46.39219 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9153e26c-cf3c-3d41-9265-05968932beca | -1.22672 | -51.75964 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f318e555-9667-3a7c-9535-bb5518a4c326 | -2.20695 | -46.6908 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eabf130-af6e-3b5b-8e39-9600853bd0ec | -1.69565 | -48.15462 | 2024-11-09 04:31:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d9c32c9-3d2f-3b8f-add5-ff5bf006cb22 | -2.3182 | -48.52389 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1a06287-a0cd-38e7-ab31-2bfe907c9d54 | -0.54622 | -51.79294 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f9d8928-559c-3173-8bf6-1b6981ac355c | -2.50748 | -47.46883 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53d05608-8afa-3e82-86fb-6b94cd98e68c | -2.37159 | -46.85756 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e1d52ced-aefd-352d-b8f2-beccdb37dba4 | -1.55918 | -52.27847 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95617b79-dfeb-3b3c-bbb5-5fc00c2087b4 | -2.20409 | -46.79586 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee4159a3-d377-34d5-b745-f31ef1273133 | -2.82659 | -47.86577 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e28a6f3-556d-3819-9a1a-fcec28e5f387 | -2.64736 | -49.24155 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb1f881f-21a9-3e4a-8891-a13d7a9c386a | -1.19032 | -52.15314 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd8564d0-e91a-3e05-a9a3-2cf213210ae8 | -2.34449 | -50.51241 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0ff97e1-e58f-3df9-b3a2-9c5b7a1dcfc5 | -2.20068 | -48.38164 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ae999a87-b37a-309f-b344-cf807b629b14 | -1.22003 | -51.77641 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 377ca45c-eca5-32b3-b42c-8bac95396822 | -2.26353 | -46.83038 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1954d4e6-bf51-3beb-9110-8ae32407c574 | -2.65936 | -48.65026 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bd7cb1a-95e5-3a94-930c-fc4e94e70087 | -2.30435 | -46.48088 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f323e44a-a9e5-3d25-83fc-de17b80f75fd | -2.13873 | -46.69439 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bde89a35-402f-3dc1-a67e-1f72871c03aa | -1.36004 | -47.32107 | 2024-11-09 04:31:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc9f4e9d-bcb6-3eed-87ff-e3102c394a57 | -0.22318 | -51.64453 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 46cf8898-1578-3268-9dc5-f208f38036dd | -2.329 | -48.94583 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a399ba3-8637-34ef-9692-de6267cd33da | -2.9522 | -46.75422 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35552707-4aa9-32e8-911d-69ac09eef295 | -2.37106 | -46.86099 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 545660bc-3aac-363a-9515-d646773f8309 | -2.67785 | -48.51025 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c75f0d8-3b6b-39d3-9815-773a574d362a | -1.21736 | -52.93899 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f5e740f-1473-3871-800a-7c6ff0228abd | -2.53081 | -47.38446 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 809cfaf6-093e-35d4-aaa0-1b5e2d739b32 | -2.21842 | -50.76629 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cdc56d3-4c75-331e-aa2a-90ff8022ad94 | -2.31098 | -46.4819 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ebfc355-d792-3bfe-9c56-eb610205d30b | -1.14897 | -51.99384 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a39526ae-a160-3069-a9d6-c700b2ed0cd5 | -2.2367 | -46.56504 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c3d6923-caba-3af7-8fc8-4d43ef351082 | -2.17665 | -48.32346 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16ad9ac6-f7f6-30fd-9f61-2a4e771ba010 | -2.37134 | -47.92559 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27b5df5a-2408-374c-9144-8c36af4157a5 | -2.38996 | -46.78305 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff9a5fe6-92e8-3f4a-a023-f1ca9b7a594d | -3.11558 | -45.96173 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 722f075d-aae8-384b-8e34-2c9424335eca | -2.21132 | -48.35781 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9820091b-a87a-3a8d-b14d-74f279da07b4 | -1.52264 | -52.21611 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3e7c4a8-8227-3c89-8912-defec32700c1 | -2.09387 | -48.89841 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26985241-6e63-3094-a708-4fc5bb0e4740 | -2.52069 | -46.20511 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b965cc0-01ed-3bac-9f91-d0747460ab58 | -2.58031 | -48.17675 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 219419f1-534c-377e-86a0-9ca3b6706374 | -2.6727 | -46.78162 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea129067-0f77-3641-88c1-7a25e7829445 | -2.11743 | -48.95081 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f618db59-5035-3116-8ae7-96edf8171741 | -1.51032 | -52.16175 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 260ad53c-43a1-3e6c-b7c8-6b6bd6e695e4 | -2.34468 | -46.63528 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa5b129d-c030-3c83-a0f5-e34bf96e1bb1 | -1.18672 | -51.99229 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 986c8359-c190-3f65-bd42-05adc7525276 | -2.04844 | -52.08761 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa44f87b-4fa5-338f-bed1-100e12479e5d | -2.75328 | -46.00001 | 2024-11-09 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6eb87db-9a40-3da9-b8b8-e34da970d9bd | -2.51079 | -47.46935 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aadd3a92-8f72-3741-b870-19ad8c0893e3 | -2.33446 | -48.57412 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee68f6ac-60ba-31f3-a910-2461bd70a2d9 | -1.51441 | -51.61065 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85eec64b-298b-3b12-9e4a-bbac27cadb73 | -2.39957 | -46.59079 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a8db2ec-517d-311a-b807-7cfa7072349d | -2.43622 | -46.26698 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 990a7972-b6b8-3942-8cc6-187e8dbb67b8 | -0.90651 | -51.76274 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df4415b-52f7-3ebd-bbd6-c8a09098ead9 | -2.39049 | -46.77962 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f79de3f-a767-3cc0-a9d0-395c22f41e03 | -1.14351 | -53.64997 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d58d9afb-5412-37d7-9108-74f8953df0a2 | -1.48496 | -51.74475 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a35ba4a-c9c2-340f-9f84-2502bd884173 | -2.17174 | -48.42102 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9edaae5-f635-3b00-8bac-e22d426e3015 | -2.19503 | -49.12603 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ffdbd31-50d8-30ee-a57b-a53c6256bc06 | -2.56803 | -47.34097 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeca3282-c205-3df7-b8b6-48b2c3e224b7 | -0.21787 | -51.62566 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c24206e-44d0-3d3f-a722-0f53c299f480 | -2.40919 | -48.52753 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cba7962-8d85-3bf3-bc07-62f01940594f | -2.21346 | -46.80081 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fd66d35-0975-3852-b11a-d2ccf816daae | 3.37136 | -51.27796 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b773ecf6-8d04-3f40-9f44-6917ea95d4b3 | -1.33231 | -47.95688 | 2024-11-09 04:31:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a42a08-cf0f-388b-8f53-18622037c730 | -1.63075 | -46.10964 | 2024-11-09 04:31:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9285e2e-06bf-3d1d-8c04-848285bb8347 | -2.3526 | -46.67523 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b59f2f6-bcb1-321a-ada4-95cc1e0fbf9d | -2.16176 | -48.52938 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2033ae9-d93f-324d-ae2f-e8966c205472 | -2.07357 | -52.26808 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db3af58-e7d0-390a-a51e-2f485db5da13 | -2.1833 | -46.45095 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbb3bc6e-f342-3c41-950d-0b11a04a5b05 | -2.20741 | -48.36085 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54334668-0e77-3349-9291-e5a235f0c304 | -2.65485 | -46.54529 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39411b60-4595-3eb2-a685-726c96f8e075 | -2.09365 | -46.34872 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 914f75be-daa1-3e8d-b70c-6ac15d8c2a0c | -3.2473 | -45.92348 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b28977b2-edef-36d6-ad70-4a26fdbc11a8 | -2.10467 | -46.47425 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6022346b-dfdb-325b-836d-688dc9eec22e | -2.52456 | -46.20213 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db10d99b-a631-32c3-8011-54a751805c11 | -2.39256 | -46.505 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e64dba03-c627-35d9-81cc-02283ff7128c | -1.85987 | -47.82463 | 2024-11-09 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f5790d0-ceb7-3e47-a01a-e991d3415fe7 | -0.91529 | -51.65717 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 711b6978-c72f-31b3-a0f1-504689c30ab8 | -2.4204 | -50.48411 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2be86b2-f0c1-3292-b27d-84bc69a162f2 | -1.37777 | -52.25825 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21ea0dfb-3c71-3c5b-9ace-a374d3dc7b10 | -1.72795 | -52.36888 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6a26eeb-0a30-36e9-860f-54a517171d29 | -3.00334 | -40.22815 | 2024-11-09 04:31:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 163fe854-40de-3652-bed8-7e5592acfd54 | -1.51794 | -52.19285 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4bef90a1-be1b-3805-a41f-023f4fa351f4 | -2.23257 | -48.37563 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8073a96b-a11d-3d1f-81a9-d29c51b773cd | -2.49996 | -47.23563 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0855e20d-22f7-30f7-863e-b890df8cf9e5 | -1.63407 | -46.11015 | 2024-11-09 04:31:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 902d6bf0-9745-3de2-b6b6-0add878b184b | -1.31795 | -55.88261 | 2024-11-09 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README26.md)
