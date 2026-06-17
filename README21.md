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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db447b8d-f79f-31f1-a03a-e244cdf1a72e | -12.2333 | -52.778 | 2026-06-17 16:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 3fba01e8-ee7c-39c8-aaf3-fa57068c5a00 | -9.6986 | -47.0555 | 2026-06-17 16:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f99dc155-528e-3a0e-8d3f-8b3e60806444 | -9.5702 | -48.1724 | 2026-06-17 16:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fd979102-4fce-3a5a-92ae-1c407a1cb2cd | -10.1493 | -56.6115 | 2026-06-17 16:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| da214677-bc04-390d-bb2e-dfb84d70495a | -9.0015 | -46.9524 | 2026-06-17 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f2c75eaa-5d90-3759-9cfa-b582d2930bc8 | -10.5372 | -53.7299 | 2026-06-17 16:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| aaef5f49-32d0-3ee2-9522-bf68eefe2eb7 | -12.1955 | -52.7612 | 2026-06-17 16:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| fd436eb4-e26b-3eba-9408-a2e29f886fb4 | -12.1762 | -52.7842 | 2026-06-17 16:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e9962bff-715c-3ab1-8812-33a3da7773da | -10.1493 | -56.6115 | 2026-06-17 16:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c0dc670f-eb34-3060-9e9a-5b20f69e6d28 | -10.556 | -53.7283 | 2026-06-17 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4bee88e7-6be8-31bf-8b41-fcb577b144f8 | -13.2845 | -46.0528 | 2026-06-17 16:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 08442c41-9516-3e17-a3b6-b3fb6d8bd94c | -12.2333 | -52.778 | 2026-06-17 16:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 204.4 |
| 343bd247-5d8c-3efc-b724-1de0b8102a43 | -12.233 | -52.799 | 2026-06-17 16:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 6f8c6d40-eec4-35bc-a514-75ecd72fd246 | -10.556 | -53.7283 | 2026-06-17 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4c335312-0c75-3b2b-b075-d56a3706faff | -12.1955 | -52.7612 | 2026-06-17 16:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 57da0bbe-15db-35be-a254-4f95709b5fec | -12.2333 | -52.778 | 2026-06-17 16:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| d9dc5f3c-d604-32a5-9126-13d44a430043 | -10.1493 | -56.6115 | 2026-06-17 16:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5c9a5ee4-b9cd-3dfa-982d-9454a7614c85 | -5.8132 | -45.0573 | 2026-06-17 16:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 36963ed2-23b8-3929-b556-5283e2e8d188 | -8.9635 | -46.9785 | 2026-06-17 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c04b7c92-df49-3dfe-b910-c45c0e24ae50 | -12.2143 | -52.7801 | 2026-06-17 16:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 480.0 |


