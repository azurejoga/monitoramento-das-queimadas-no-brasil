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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04cebfde-5ab2-39bc-b790-cfd942e68507 | -2.29939 | -46.73043 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34f98b9d-acd3-370f-a5c9-e9aa3f8f680a | -2.16978 | -48.97402 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4effc857-410c-35d0-99da-8ae56f4b862d | -2.3077 | -46.74226 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d48fb7a5-4bc4-38f4-9591-3caa137224f9 | -2.12356 | -46.37456 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41d25f13-1106-3e60-8e20-be89604c0ca9 | -0.17028 | -51.4183 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccb19d4d-5c26-3cf3-9443-60ae4a1b72d9 | -2.65206 | -48.63078 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e9b0eb3-17ee-33b9-9489-8b24932c08cd | -2.05077 | -48.64142 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0abfcc7-e4fe-303f-8186-bad42d813239 | -2.16513 | -48.5299 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98845dc5-ed46-3f17-be13-bdc2796d826b | -2.65039 | -46.07086 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40b26380-a41e-3f91-b3d9-9a44e7d22681 | -1.62727 | -52.23966 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b7b8024-f2d4-373e-a382-029a40de519b | -2.32922 | -49.6947 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cb3f1c1-422b-398b-ba0e-ce09eefdf216 | -1.36058 | -47.31762 | 2024-11-09 04:31:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13f7d3c4-65bc-3281-a529-bbb188864caa | -1.85932 | -47.82811 | 2024-11-09 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3145269-bf57-3e9d-aaa0-d54625dcea0d | -2.45888 | -47.93199 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1850c9d2-f05e-3361-a010-2976e5441541 | -2.83669 | -48.46972 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba51afea-e3a0-3c87-8631-ce69b1847677 | -1.38098 | -51.41091 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d3c8454-5070-3fde-9a21-8dd7cdf7bbd2 | -2.87144 | -47.90461 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 201ac5a1-d391-358f-8bd3-0aa81bcdf7b4 | -1.3965 | -52.06531 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ef617ed-4307-3ea5-8eff-f70e2c81bccf | -2.30198 | -46.69212 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a75ba1-1811-3045-be65-b50bddd4c0e0 | -2.29067 | -46.50353 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8219a02a-c266-3a5d-a29f-9afda5a6a911 | -2.31983 | -46.49034 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16e97a5d-1c61-38eb-932e-1be04b8c90a2 | -2.7025 | -46.67696 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f5498c0-94b7-3eca-8c5b-8f4966176e3c | -2.12524 | -48.56422 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3535f7bb-7932-388f-af21-dd046163c1b3 | -2.62287 | -46.15991 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e47a25a8-6ae6-325a-84bf-5a39ad48517d | -2.14034 | -46.68408 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a215b93-0b37-36b9-9eba-735444d236ec | -2.14756 | -49.13827 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbf7d16f-c964-3887-bfdd-cf40e77ca603 | -2.14292 | -50.8092 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48e4b58f-6187-3c12-b0f0-36049068ff59 | -1.5188 | -51.30761 | 2024-11-09 04:31:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08466995-4a25-3143-af5f-2abbacb36b30 | -2.34955 | -48.92641 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb9e397e-6c65-3660-ad8a-0d67e71e8857 | -2.39241 | -46.59322 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d4b5596-17d1-3fc4-b3cc-946105f93940 | -2.31594 | -48.53821 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97d8313e-79f1-3770-bc81-3361e0931ef9 | -2.39594 | -46.76639 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37f8b72e-6019-3c1e-9f09-b2f5282ebe1c | -2.08949 | -46.52829 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6951cb7b-9d69-31fb-a62c-51af157c7da6 | -2.14088 | -50.81078 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cd22781-be17-3c84-b6b3-aa7ea79f2724 | -2.36747 | -46.79717 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3acb8d40-7d2e-33d6-932d-d0992c58098a | -1.24174 | -51.78008 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c51cf5ad-3f1a-3796-ae80-e80848bfc228 | -2.60982 | -46.24372 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5bae5b1-3426-380b-aab2-8e04703b71b9 | -2.37675 | -46.78102 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c1aa1e-e131-33f5-826d-8e21804780ab | -0.00218 | -49.96031 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd8ed712-4e63-3a94-a7c1-f77e18db7ccf | -2.30439 | -46.74175 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04d0f57b-ac58-3f9f-b1c6-2535afb1fb4c | -2.05409 | -48.88474 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bda803e5-2402-32d0-b049-aad763456938 | -3.1303 | -45.76283 | 2024-11-09 04:31:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bb58188-90ea-3096-946a-9ff4c9d071b6 | -2.11101 | -50.66127 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f2c1825-e0a3-3992-b1ee-bc1e7387edd8 | -1.66606 | -50.48653 | 2024-11-09 04:31:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bf8a1eb-2553-3e92-b350-89fa9b3b5c6c | -3.10786 | -45.77406 | 2024-11-09 04:31:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ceefb29-4601-3a8c-840b-215eaf7a5026 | -2.84006 | -46.64512 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b379461-60e2-39f9-9ad0-26390251cac8 | -2.57636 | -49.13488 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cb419d9-38ea-3e23-b062-e1f80d7f1bcb | -2.31613 | -48.23626 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 601dae94-468c-3948-a159-71a7fbeaf53b | -2.62674 | -46.15692 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33fa028-88da-3900-870b-1ae7a3ee23ab | -1.39618 | -52.06625 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbebd4e8-b063-3137-be35-2fb811a9e272 | -2.46906 | -46.88667 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d932975c-defb-3ad4-8b19-30f872ce6ae0 | -2.87089 | -47.90807 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc70a1ac-86be-32f8-8431-4a12fa8d2f35 | 0.69675 | -51.44268 | 2024-11-09 04:31:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86a2e6d5-0beb-35e8-b34c-c6de5f1983e4 | -2.13476 | -46.7852 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fa0b0c7-8188-37c0-82b4-2e49b41c085f | -2.36203 | -46.8104 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25c0ac1b-b285-3e9b-96b3-0013ac2edb14 | -2.23367 | -46.49755 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d3c7245-3a16-396b-b589-883243a4162a | -2.20963 | -46.80373 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa8c5f76-b8cb-3848-a349-e882b073315e | -2.64812 | -48.63384 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5fd20a9-b96e-315a-8503-4c7d7491bca5 | -2.67672 | -48.49552 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e878fe3f-9883-3cbe-9970-a588f118a212 | -2.4129 | -46.74437 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 170602bd-f97b-3de0-9eb7-09313552e5ef | -1.64185 | -47.82608 | 2024-11-09 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60928aff-67e5-3931-90d8-575ca6116858 | -2.21293 | -46.80424 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 727cefc1-5b94-383f-8fdc-a19345729913 | -2.39626 | -46.59029 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 686d444a-534b-3957-8a28-ce1715a5d7e4 | -1.94047 | -51.40467 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 17206bea-61fc-3a41-b9ec-5fd4a267b395 | -2.55699 | -46.18913 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c32e6011-6307-34b0-b0ff-b29b77bf39f5 | -2.11031 | -46.76381 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 307a6f63-b0db-3926-88b3-62ce729f9ad8 | -2.28683 | -46.50647 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e52bf70-5e50-35f2-bf04-39eb7e11d048 | -2.4238 | -48.47858 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac382e4-3725-39bc-b0d1-d9d08138d782 | -3.59504 | -42.84097 | 2024-11-09 04:31:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3297e13e-d20b-3551-9a9e-7a159be43608 | -1.66835 | -48.72424 | 2024-11-09 04:31:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8daa0ef5-9d92-36ef-941b-e78106ad14e9 | -2.51789 | -47.18571 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33bf9fe1-2861-30b5-9e9a-99716f6d60a7 | 0.0475 | -49.54053 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e932b97d-c269-3ed0-8b16-e20a900a580f | -2.84787 | -48.44242 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f9e621d-237a-3406-bb71-435a47455894 | -1.38435 | -52.19128 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c58f462-7be5-3f08-a0c4-f9cf34ddd0d8 | -2.23392 | -46.8469 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c67cb5-aba2-3a8b-b1b1-f65a5fdb0001 | -1.83752 | -52.01738 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cbc2d9-7e1f-3274-a77d-30907184be9f | -3.10703 | -45.95651 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 208554af-8bf6-37ab-8ee6-12a15552dbfc | -1.14272 | -53.65073 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6cb05aa3-7a2d-368c-9f11-5640be8c8ba8 | -0.33425 | -51.57565 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5fed009-05c1-37fd-aec9-4bb0bdc3d91b | -1.76573 | -45.60983 | 2024-11-09 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5fb0a3d-fe9e-3440-b540-d62f3eba5dba | -3.10423 | -45.95245 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8daace4c-9640-35f4-b8ad-e12455766e73 | -1.44611 | -53.00271 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c7a4ccb-7d1b-3a2e-94a9-9d1d32ac3436 | -2.39684 | -49.22609 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44320631-e90a-3e1e-8630-b1f29bfa629d | -1.4771 | -52.08245 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9e91fa2-3499-3198-8988-a8fb49c4ee9f | 2.10185 | -50.85378 | 2024-11-09 04:31:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0cca9aae-4b37-3907-b84a-efb04a3eeaf7 | -2.43343 | -46.26299 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68c0b344-d754-33cd-adaf-8f5bbdb1ed99 | -1.63264 | -47.36386 | 2024-11-09 04:31:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b85b8e8-c54e-354a-9083-c10bbaa96c45 | -2.42452 | -48.93799 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f868ef4-b0e9-355d-9d32-6cce7babd081 | -2.52099 | -46.31197 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a70c6d4-af05-3eb6-855b-f5fd2c78784c | -2.602 | -48.19088 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f114792-1dc1-3fea-8576-322c19e4ecd6 | -2.30694 | -48.55151 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2837cbc9-d7ff-3cd4-a786-e4dd65312e59 | -2.41147 | -48.49129 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 745b2c83-bf56-308d-995a-ca2fb94099aa | -2.57497 | -48.45066 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dd8c171-da3b-3e34-ac06-60713d3301d2 | -1.99837 | -47.85312 | 2024-11-09 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77e4f25f-9f46-356a-905e-246044fc0901 | -2.45685 | -46.30931 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecd4955b-f3f3-3a68-a812-930eb9dbac90 | -2.09329 | -48.9021 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f60c0d00-244b-3228-b885-874ea5441720 | -1.34972 | -51.40609 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5bb2d3e-0de5-3340-b7cd-e44626c79f59 | -0.40562 | -51.47396 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb8831f6-fa0a-31f2-87bf-358dc3da3202 | -2.58309 | -48.18077 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 712c8144-3d36-3043-8332-c0f609ab91d5 | -2.2326 | -46.50445 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README28.md)
