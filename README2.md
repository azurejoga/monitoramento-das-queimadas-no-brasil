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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2cf1645-957b-3924-900f-c5416147d32e | -12.42092 | -64.13894 | 2025-12-22 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79624643-2729-37a4-9f09-a5cf9fd6aedb | -12.37473 | -64.01415 | 2025-12-22 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ede2d31-73af-3719-af6f-9e746721152b | 4.03984 | -59.76299 | 2025-12-22 05:50:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 348cfde7-1803-33f8-a6e0-53743732f758 | 4.26215 | -60.11252 | 2025-12-22 05:50:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc70015f-6a71-3ea5-b84e-d5c5c18321e2 | 4.0404 | -59.76638 | 2025-12-22 05:50:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d0b84a7-c719-388a-a8f8-3984b8e3b898 | -9.72226 | -60.19928 | 2025-12-22 05:54:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b7e3f69-f305-31a4-8f9e-5bddc3a4f9b1 | -9.25206 | -60.33504 | 2025-12-22 05:54:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c4c9578-5770-314a-97bc-e53791c2cab0 | -9.24733 | -60.33441 | 2025-12-22 05:54:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eac4ff52-70a2-36a8-93bd-42757a4bf450 | -17.61895 | -56.34024 | 2025-12-22 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 75617cea-b253-3cbc-af97-737807252a61 | -10.52281 | -42.43398 | 2025-12-22 11:36:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| bfde45c0-e6d7-3d98-bfd8-1f9dacd8ad7a | -10.51296 | -42.43253 | 2025-12-22 11:36:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 49365b20-c3be-3bc1-bbed-51dc13ad0c6a | -10.59365 | -38.72982 | 2025-12-22 11:36:00 | TERRA_M-M | BANZAÊ | BAHIA | Brasil | 2902658 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f4de704b-1f50-3344-85e8-68ef1afae4f5 | -10.59493 | -38.72079 | 2025-12-22 11:36:00 | TERRA_M-M | BANZAÊ | BAHIA | Brasil | 2902658 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bac7d15a-e6f5-3e5c-b2fe-067e3181bd8e | -16.31473 | -42.98726 | 2025-12-22 11:38:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |


