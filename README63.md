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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97ab3ed1-cf9e-37ec-8842-4759c3aee5b7 | -2.7961 | -49.2211 | 2024-11-01 14:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 25eb6c72-70b0-3924-8cd3-da5b79636ba6 | -2.8537 | -48.6642 | 2024-11-01 14:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a4b0ff68-9a6f-3de9-b5e1-b08ef2bbd74a | -2.9094 | -48.6196 | 2024-11-01 14:45:23 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 01bf9445-38b9-38dc-8497-319565c100ae | -3.0379 | -53.7858 | 2024-11-01 14:45:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b9edad1f-981c-333a-bd1f-594fb5c4da62 | -2.9354 | -46.7722 | 2024-11-01 14:45:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1d300579-02e3-3c1e-8da3-e341a5522d47 | -3.0539 | -49.4683 | 2024-11-01 14:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 55bf8edc-1bc1-3653-82f6-3ad57aa7d275 | -3.2047 | -53.3977 | 2024-11-01 14:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d4c51d88-91b4-3329-9ea9-eca0c016e622 | -3.0917 | -54.1666 | 2024-11-01 14:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d2891b7d-018a-34c0-9995-29c4203f62c4 | -3.2231 | -53.3972 | 2024-11-01 14:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 580.9 |
| 3a2fed47-f451-3cdb-94c3-0d4522019874 | -3.2611 | -53.0717 | 2024-11-01 14:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| e44217a9-ef85-3341-b059-b016e64cc9e0 | -3.42 | -42.7798 | 2024-11-01 14:45:25 | GOES-16 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| c0c49b7c-6b4f-3ca2-b832-e8a2725d9650 | -3.2232 | -53.3769 | 2024-11-01 14:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| f987628d-80b9-3d42-ac0a-b27ea87dc984 | -3.2535 | -50.3479 | 2024-11-01 14:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 6135f9c7-5c75-3727-9590-42ba18d794e9 | -3.2417 | -53.3562 | 2024-11-01 14:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 2c3f333a-f4b0-307e-ad2f-790cc6df52fa | -3.3891 | -41.6201 | 2024-11-01 14:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 4cad914b-902e-3044-b873-1b6d27b8df61 | -4.1458 | -43.187 | 2024-11-01 14:45:29 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 79f01f62-760a-3851-b200-89f6d90bebd4 | -4.1457 | -43.2103 | 2024-11-01 14:45:29 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8d73b6d0-a11c-3f25-a6ed-4062962511a4 | -4.1981 | -46.6981 | 2024-11-01 14:45:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f8701e40-ba4c-31a1-ab57-a738fc6be77d | -4.1795 | -46.699 | 2024-11-01 14:45:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4ef4c321-8f84-340b-801e-2cb6aef0847a | -4.3869 | -43.4525 | 2024-11-01 14:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 07cf6597-1189-3e7f-8178-8b40f726d743 | -4.3867 | -43.4757 | 2024-11-01 14:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 242.0 |


