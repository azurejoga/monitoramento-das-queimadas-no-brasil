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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0a9154a-c16b-3263-9020-c217d9b7b14d | -3.5386 | -41.6367 | 2025-12-24 07:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| ec3dc873-64ad-34d2-bca2-508a394292c8 | -3.5386 | -41.6367 | 2025-12-24 07:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| bb82e603-1bba-3762-b20f-18efa3788600 | -3.5573 | -41.6357 | 2025-12-24 07:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 2d7bd516-6e43-33fd-af63-9102261384e3 | -3.5573 | -41.6357 | 2025-12-24 07:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 45c3c148-5ebb-320f-9b3e-bbce0f10c63b | -5.81346 | -37.59287 | 2025-12-24 11:17:00 | TERRA_M-M | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 97931044-a7a2-3154-9ff4-a56121f4dcd1 | -5.40782 | -37.66461 | 2025-12-24 11:17:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 211448eb-f31b-384f-b7d6-420b5f3518df | -3.90357 | -38.96872 | 2025-12-24 11:17:00 | TERRA_M-M | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 26.0 |
| fc6a6570-22f8-343e-b5ea-1af1b0a26c0f | -6.71237 | -37.60371 | 2025-12-24 11:17:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 145d451f-0759-3481-a2db-70616f3b25fa | -9.49423 | -36.98713 | 2025-12-24 11:17:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 51794636-b5e8-3192-b3ba-ea997c85e34e | -6.05343 | -35.57817 | 2025-12-24 11:17:00 | TERRA_M-M | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 298b506f-f165-3269-a9e3-f44247d1b93c | -20.05313 | -52.20692 | 2025-12-24 12:59:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 4641ab82-92b1-33b8-8883-daca0195eb2c | -26.12796 | -51.20452 | 2025-12-24 12:59:00 | TERRA_M-T | UNIÃO DA VITÓRIA | PARANÁ | Brasil | 4128203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 6ed00c85-03f2-320f-b100-32b38d7c1dc0 | -17.91824 | -54.13791 | 2025-12-24 12:59:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 55913656-2f6a-3868-9ce7-744e9e3aa79b | -24.38659 | -53.19904 | 2025-12-24 12:59:00 | TERRA_M-T | NOVA AURORA | PARANÁ | Brasil | 4116703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| b41f36a4-d676-3bcf-b56c-363f4e4ed0a5 | -20.4774 | -51.67364 | 2025-12-24 12:59:00 | TERRA_M-T | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 37.0 |
| aaae5e24-cc2c-3a22-88c8-99db48e73b5c | -20.02346 | -52.68853 | 2025-12-24 12:59:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 35.4 |


