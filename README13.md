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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17385d4e-8433-36a5-adfd-2d6863c731b9 | -4.00031 | -43.39286 | 2025-11-23 12:16:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e64723c0-fe2d-3b71-9491-f3097eb1fb96 | -12.96624 | -49.03255 | 2025-11-23 12:18:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e30fe03a-d858-39de-b58e-0efd55dc5da6 | -12.96496 | -49.04157 | 2025-11-23 12:18:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3c483edc-50b3-320d-85be-ab256ebb576e | -10.15683 | -48.0941 | 2025-11-23 12:18:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b1a76eb-063a-3e9e-89f4-c3447a82605d | -13.51713 | -48.6508 | 2025-11-23 12:18:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f769fdd9-2b62-3dab-8076-e31a5d2b4390 | -20.89193 | -52.33124 | 2025-11-23 12:21:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4328e23b-5c5b-397f-a2a8-c7e323a29225 | -20.88299 | -52.32974 | 2025-11-23 12:21:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 628da9c0-4030-3d49-a977-36b67f26b3ab | -5.5758 | -42.292 | 2025-11-23 12:50:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 8d936d46-2442-35bf-902f-850141a0971c | -3.6519 | -41.463 | 2025-11-23 12:50:00 | GOES-19 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 697b072b-8519-362a-991d-5a5bd86c4e89 | -3.1234 | -42.3694 | 2025-11-23 12:50:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 69ef6c97-c6eb-3413-8d34-a58aa8fdb5aa | -3.1421 | -42.3686 | 2025-11-23 12:50:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 199.2 |


