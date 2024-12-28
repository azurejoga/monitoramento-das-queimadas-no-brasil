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
| 2e40ad2c-1340-3e7a-b236-6ffe41e633a1 | -27.92402 | -51.04016 | 2024-12-28 12:57:00 | TERRA_M-T | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| e2eb0e69-010b-3fdf-ba5c-b0504dac4f26 | -26.78756 | -50.94681 | 2024-12-28 12:57:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 673f3523-f43f-366c-b44b-69249a10a982 | -27.87344 | -50.38966 | 2024-12-28 12:57:00 | TERRA_M-T | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 88c2bcd7-992d-3a48-8cb4-cb91fee903b9 | -28.71557 | -52.90181 | 2024-12-28 12:57:00 | TERRA_M-T | TAPERA | RIO GRANDE DO SUL | Brasil | 4321006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8a706bdd-757c-391c-9289-2ec989e46bfa | -29.16065 | -52.19125 | 2024-12-28 12:57:00 | TERRA_M-T | POUSO NOVO | RIO GRANDE DO SUL | Brasil | 4315131 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 80f2fabb-0adc-3353-afe2-e773e89950a9 | -7.98 | -37.61 | 2024-12-28 13:00:00 | MSG-03 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | nan |


