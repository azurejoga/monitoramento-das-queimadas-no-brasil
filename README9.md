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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efa5d7bf-e455-3d06-8faf-adf31f6f4fdf | -13.3749 | -54.2745 | 2025-05-10 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| b4c85a21-fae4-34ef-bbe6-693519d3e724 | -13.3752 | -54.2538 | 2025-05-10 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| b0b5e226-9c6a-306f-8998-9f62734944a7 | -13.3749 | -54.2745 | 2025-05-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d75ad5fa-1148-309b-a84d-01128511e587 | -13.3752 | -54.2538 | 2025-05-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a0bf6664-d566-34d4-909b-2c9d9f7c9840 | -14.6414 | -45.1263 | 2025-05-10 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 584aefb5-a43f-32b0-bee7-db12b6281c24 | -14.6414 | -45.1263 | 2025-05-10 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 633b2a71-108a-3b0c-a731-ba5cf6a7793d | -13.3749 | -54.2745 | 2025-05-10 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 1de3ae8a-5791-39fe-a5b5-f22a72b6c377 | -13.3752 | -54.2538 | 2025-05-10 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| c8fcd49a-4a6f-38a9-9bec-7635dbc4b216 | -13.3749 | -54.2745 | 2025-05-10 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 791e641b-5a41-325e-b8c1-d99d891fac41 | -14.6414 | -45.1263 | 2025-05-10 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 29cfac39-1f93-3db2-aca3-6cf8435a786f | -13.3752 | -54.2538 | 2025-05-10 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 84ebec3a-8a22-3b92-8aee-4c05218e2741 | -14.6414 | -45.1263 | 2025-05-10 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 92a350da-b57e-3b2d-a844-bc854ae26458 | -11.0789 | -46.1245 | 2025-05-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 721aa320-3bdd-309f-8e4b-09defca1beb2 | -13.3752 | -54.2538 | 2025-05-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| e9dd13bc-4c80-3d12-90ed-c34c33800630 | -11.0789 | -46.1245 | 2025-05-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ec38d255-82e9-3e4c-8a92-860fb2169824 | -14.6414 | -45.1263 | 2025-05-10 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8189a061-4f75-318e-9f38-e8b50abbcdcf | -7.6131 | -43.4511 | 2025-05-10 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 332007ea-be7c-3787-ae82-e2598d3025b9 | -13.3752 | -54.2538 | 2025-05-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| bcab3191-de5f-3933-a50f-ea1a5a8e6cac | -10.4883 | -46.1778 | 2025-05-10 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| ea76c453-d80b-3309-882b-6fe93d76d65b | -11.0789 | -46.1245 | 2025-05-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 67f57260-dc5f-3487-9800-dd6ef4dde1de | -13.3752 | -54.2538 | 2025-05-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| e18db6ed-8481-3234-af84-a1f29103fae4 | -14.6414 | -45.1263 | 2025-05-10 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fc109afa-da69-349e-a541-1814620dcca5 | -10.4883 | -46.1778 | 2025-05-10 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 1ce989f7-6c8f-3a2c-986e-cb3591bcd380 | -11.0789 | -46.1245 | 2025-05-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 95400788-8168-3497-b0ff-3d5a2e70aac0 | -13.3752 | -54.2538 | 2025-05-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 93b24a59-acd9-3f9a-9160-df780c87e961 | -11.0789 | -46.1245 | 2025-05-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 9a45bcb2-23be-3b3a-8f30-a7a5b11cdcf4 | -13.3752 | -54.2538 | 2025-05-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 1c8dc8ca-8445-3ae3-a69a-72067f17a456 | -13.9902 | -56.8058 | 2025-05-10 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |


