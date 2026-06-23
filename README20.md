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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27de566f-d14f-35e7-8c7e-723852f9bdf1 | -11.2983 | -43.3376 | 2026-06-23 16:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| b6b680e7-249d-36d1-b11f-68e04866322f | -6.9979 | -42.9016 | 2026-06-23 16:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| bc4ee26a-0f47-3595-ae9a-bd1075239a2e | -10.777 | -47.1742 | 2026-06-23 16:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 2d1553e7-53ee-340c-a1f7-6ba85d7bcf24 | -8.8118 | -47.0606 | 2026-06-23 16:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 168.6 |
| e2647c29-76f6-3f0d-a8a5-c80d3ff63fd5 | -12.8736 | -44.3828 | 2026-06-23 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| d099203d-a7ca-39dc-a2fc-8600352f9c78 | -5.7885 | -43.6366 | 2026-06-23 16:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 3ee57824-dfbf-3757-a6c5-b11ca48d7175 | -12.7949 | -44.4661 | 2026-06-23 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 504969b8-edc9-3386-b36a-73781671f922 | -8.8115 | -47.0828 | 2026-06-23 16:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ba46d664-757e-3611-8135-f3d18b8411fe | -11.4892 | -46.6795 | 2026-06-23 16:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 7ba19355-e675-375a-9669-09200d9c1db1 | -8.8118 | -47.0606 | 2026-06-23 16:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a0f65586-7977-30fc-b90d-e3e7aa61903f | -6.3223 | -44.6542 | 2026-06-23 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 05c2163a-19d6-3cce-a386-c5e3820f3c10 | -12.8736 | -44.3828 | 2026-06-23 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1ec97b63-b9bd-32e2-849a-d4e9ecaae960 | -8.0861 | -46.3971 | 2026-06-23 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 875d6e6a-1d7c-3888-b00d-1bfdbcd4b723 | -12.7949 | -44.4661 | 2026-06-23 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 0185160a-f378-3f49-9e37-4672f1e0ff1f | -6.9979 | -42.9016 | 2026-06-23 16:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 5a2e8cd7-a7b0-3e0a-aac8-af89717252fe | -8.8115 | -47.0828 | 2026-06-23 16:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 60be5cd9-b6d8-3eca-99ac-641807f59691 | -10.777 | -47.1742 | 2026-06-23 16:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 164e0b90-3537-30be-8ca9-c2c7674cc181 | -11.4701 | -46.682 | 2026-06-23 16:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 4cffa195-52ba-3fd5-b9ad-4e3db6a2f910 | -5.8073 | -43.6352 | 2026-06-23 16:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |


