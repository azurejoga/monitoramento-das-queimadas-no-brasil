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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db2456f1-188c-3f2c-b376-c9aad77adda0 | -1.56646 | -45.78149 | 2024-10-17 04:10:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 489c03fa-6904-3dd5-8c16-b4985c3a8b38 | -2.65468 | -46.05317 | 2024-10-17 04:10:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff1ddc90-36d5-3c52-a2fd-2d1201316b71 | -2.3774 | -46.48296 | 2024-10-17 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50b7843e-24c9-37d9-8c28-4de593058210 | -2.37204 | -46.49187 | 2024-10-17 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a71b132-2fd3-36c7-a866-e9289f362ae5 | -2.36509 | -46.48591 | 2024-10-17 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5242407-5d0e-39ad-b457-415425a49f7f | -2.26432 | -46.48667 | 2024-10-17 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c07576f-bdf7-3bf0-888e-6aa99c2f0863 | -2.26046 | -46.48605 | 2024-10-17 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 241c8221-2a4d-3e7a-aca0-5bb41345a497 | -2.2591 | -46.74854 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7872598b-7550-3028-ae29-42ec85458dc6 | -2.25866 | -46.7511 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 401bf372-0f9c-3823-9113-6573c7df2002 | -2.25828 | -46.75352 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a4fc2ef-2459-3532-9162-40f7041ef288 | -2.2571 | -46.76106 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc05e6c5-d20d-36dd-9831-75010e8e4560 | -2.25666 | -46.76345 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edd28e17-8b68-3ac8-8b46-b66e54536086 | -2.25633 | -46.76605 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69e4c9a8-a0a7-36ad-b608-9b7c83d9e065 | -2.25391 | -46.73004 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9b474a4-a04c-3063-b932-89d0e06e9a3d | -2.25368 | -46.73247 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd06c6d3-0ff3-3bf3-9c5d-d5d7a832feb3 | -2.20573 | -46.4577 | 2024-10-17 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 131e1bc6-cf1a-39cd-a4f6-3f1d4783be7f | -2.1944 | -46.72558 | 2024-10-17 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 080f91f5-43d3-30f7-8c68-98e460b9afe9 | -2.1392 | -47.9888 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90f33a9e-2807-350a-b175-e5020022b95b | -1.0554 | -48.00193 | 2024-10-17 04:10:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5fb946d-551d-3b9a-a1e7-0b37fd1b5de6 | -1.87308 | -47.80968 | 2024-10-17 04:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf6a33ff-5f0c-35fd-9a7c-916c5667138a | -1.87244 | -47.81357 | 2024-10-17 04:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edc12da4-7821-3e5b-b45f-ba51a76df077 | -1.74769 | -47.37867 | 2024-10-17 04:10:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3db5e1fe-cc45-36e5-beb9-77b5163faf4d | -1.52929 | -47.20911 | 2024-10-17 04:10:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e913e4f-0a1b-3d26-b678-5f5663a3dc31 | -1.52893 | -47.20913 | 2024-10-17 04:10:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e02ae44e-65f2-35c6-9642-fb265080f65b | -1.24974 | -47.8344 | 2024-10-17 04:10:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe4d53c0-d9ef-3fb1-8caa-88a8c0a4138f | -1.23459 | -47.71416 | 2024-10-17 04:10:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c775b141-52db-33ca-b7c7-1556cb9eedb6 | -1.23429 | -47.7137 | 2024-10-17 04:10:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 044fa557-73d6-3fc6-ace4-43bc9b089b09 | -2.70166 | -48.70505 | 2024-10-17 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 550d1097-b568-3953-b403-cec1e7fab9ee | -2.70086 | -48.70288 | 2024-10-17 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efea35d7-edba-3938-b168-5aaa5b242ec4 | -2.60657 | -48.25741 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 52d560fc-8d6c-36cb-ae21-f7bea2a119a1 | -2.60592 | -48.26147 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 11c1856c-48fa-3abf-ae50-bdd8a26d4dcd | -2.60227 | -48.2567 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b815eb3-9bc4-317c-a8ca-c4f167edd4f5 | -2.60162 | -48.26073 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4f1a3f7-eac0-37c9-b570-d32fa6ab2a45 | -2.44974 | -48.50317 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4f09d44-e402-3944-a127-dad8c22478be | -2.42964 | -48.65517 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dbadc48-f176-3e04-9bc6-e81c3c07e713 | -2.42907 | -48.30162 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59447c07-f2b6-3bbb-9d40-154ef8821f8b | -2.42731 | -48.30226 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe075da0-517b-33ad-86e5-24ee4ef40afc | -2.42568 | -48.51244 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83fc88c9-b4d8-3985-b21d-3c634a1b12e9 | -2.42498 | -48.5167 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3d69478-3d71-3200-960d-9ab839f1a3d4 | -2.42129 | -48.51171 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e19f15c8-723c-3b78-87e9-0fddd5604306 | -2.42059 | -48.51598 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37df576d-d797-3e78-ae7e-e1bfa0aba4d7 | -2.4199 | -48.63104 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77e1e441-27cb-3cff-b562-f17de5272774 | -2.35799 | -48.29096 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48664a85-9506-3dd5-8932-8b8e876966d3 | -2.35365 | -48.29025 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a01332a-8e9d-37a9-b593-890613a89e29 | -2.2391 | -48.83921 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ce0ef0b-1334-3e83-9feb-d976923d50c2 | -2.23309 | -48.02336 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c69a5224-eb19-312f-8c97-bb596f6018e6 | -2.18282 | -48.22764 | 2024-10-17 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c31d131e-71b7-3714-b96c-f84bd8241adf | -2.16338 | -48.40483 | 2024-10-17 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2872c6d4-e04f-3aea-814f-cdfe670c0c6e | -2.63322 | -47.6312 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210581af-6e27-36ed-9b26-ee8f2c28a17e | -2.63264 | -47.63489 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87f67d8a-5474-3cba-89e6-b5a66d40edec | -2.62852 | -47.63418 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01a0dcaa-d52b-3068-adaa-c43ca565f3b7 | -2.58186 | -47.47926 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6f65df4-930c-3ff0-8b1c-a08d9dec4e03 | -2.46153 | -47.84043 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc131d9e-7cbd-349b-b455-4e4053d0bc33 | -2.46092 | -47.84425 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4507a1b0-ccd5-3412-b761-bce9aa7c134a | -2.45744 | -47.81243 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0c37a91-0d99-39fe-919c-551b0c046768 | -2.40579 | -47.64587 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81cd8c73-3212-3a5c-aed2-290d51a6d227 | -2.38961 | -47.7208 | 2024-10-17 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdc203d7-eb9f-3da7-abbc-b08fefb9c6bd | -0.76027 | -48.68836 | 2024-10-17 04:10:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63157dc7-0086-3982-8356-3ee54e3b335b | -0.76008 | -48.69054 | 2024-10-17 04:10:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95af787c-8e69-311a-9979-a4bbd77b1923 | -0.75955 | -48.69304 | 2024-10-17 04:10:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1040683e-6484-33b3-81cc-73d7ec73f4b8 | -0.75932 | -48.69521 | 2024-10-17 04:10:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90aa6548-f4b3-3bfe-925f-fc876e9eafae | -0.75883 | -48.69772 | 2024-10-17 04:10:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60789aea-92e8-37c1-877a-8dd2a29e703b | -1.12465 | -49.16698 | 2024-10-17 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fa568d8-5978-32e4-98c4-e684b1c745f3 | -1.12384 | -49.17194 | 2024-10-17 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f40b66e-0b16-30f2-a650-d8b580f344a4 | -2.17 | -48.83707 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13c1ebd7-b354-3b84-99ba-45be78976fe0 | -2.63545 | -49.26812 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| cf281241-1c6a-3cc8-8b32-26871863721d | -2.63466 | -49.2729 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 31df20e3-2dd8-372c-84ad-7c9f77132d82 | -2.6299 | -49.07414 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90be728f-7af3-3a77-bf21-9996f6b071f6 | -2.62913 | -49.07876 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2824c717-fb29-3c62-a4e9-e6396a886320 | -2.62902 | -49.07656 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5686623d-10d1-3ac1-87a8-83885c0f9ff6 | -2.62534 | -49.07339 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bdd4e505-0135-3cb7-a5a8-3120a474b84b | -2.62457 | -49.07802 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37eeb1b8-945d-3634-b0eb-182d5dde7fa9 | -2.62447 | -49.07581 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d60ba317-e86f-3de2-9f4c-bb371f8fbd99 | -2.61471 | -49.10766 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2abdd7a-5224-3455-910e-041f31ce4458 | -2.61356 | -49.48921 | 2024-10-17 04:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 288f95f0-66c2-32fc-8a36-23a144ea1a5d | -2.61313 | -49.08824 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b45f8d1-490d-38b6-850a-5ee3df3f9f21 | -2.61239 | -49.09288 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a4742f1-a2d8-38e2-a4ea-63724a40bf04 | -2.60887 | -49.48843 | 2024-10-17 04:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 31db4b6b-95ba-3112-9623-312e5824513b | -2.60782 | -49.09215 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92ae255e-196a-3be0-aad9-13361be330d3 | -2.60419 | -49.48765 | 2024-10-17 04:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 630337ee-6f1f-3573-a830-5a46b30b4563 | -2.60337 | -49.49261 | 2024-10-17 04:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5d064bf7-35f1-3b80-96df-c0329ba78998 | -2.57209 | -49.0815 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aad81f9-983e-3a7f-a5d5-6d9076031c8f | -2.49115 | -49.29409 | 2024-10-17 04:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffa12929-20de-33a3-b999-2d9ce901b58e | -2.4859 | -49.37551 | 2024-10-17 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e42a58a5-e6b0-3d02-b2e7-9d30e1cde965 | -2.48273 | -49.37746 | 2024-10-17 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76730ac3-98ba-309b-b323-ffce01de1fcb | -2.31619 | -49.0943 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6765399b-fd05-37f8-8884-caa1f7afdf76 | -2.31572 | -49.09699 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fd27aa1-4c16-39bb-a740-d2c1b50a8d6b | -2.2745 | -49.58195 | 2024-10-17 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ced12c21-a8f0-3db3-9ff7-ab97142e18c5 | -2.26976 | -49.58114 | 2024-10-17 04:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96682850-0792-36ec-9b1c-84f7e54bf347 | -2.5878 | -48.95652 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ca81782-2499-376f-a1e1-ce46083242df | -2.58477 | -48.94667 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9a86795-34eb-3bcf-b29a-deed84a86d1c | -2.42405 | -48.9481 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83a09c17-4a40-34ce-bfc8-ed25bb89a9f0 | -2.42332 | -48.9527 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7a8768f-8bd1-3bc6-b675-aa8ab24b8763 | -2.41879 | -48.95195 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cfcc0b8-ba6b-324f-8b3b-09e56d751efa | -2.41426 | -48.9512 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4e75466-ec21-35ca-818b-8dbcbcdff4eb | -2.41092 | -48.88512 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dc1be3a-6a5a-37e1-8c38-9ef81a181235 | -2.40899 | -48.95506 | 2024-10-17 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 621d056a-d53c-34a9-b325-c9a591414561 | -2.41357 | -50.30273 | 2024-10-17 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 012ea48f-3a8b-343f-817c-bbf352b79d29 | -2.39523 | -49.83711 | 2024-10-17 04:10:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bba3a29-ab2a-397b-883a-97b53b12a97f | -0.07146 | -51.30165 | 2024-10-17 04:10:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
