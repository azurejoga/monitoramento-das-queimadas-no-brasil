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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dacfb070-ad00-320a-bc49-3a7ea830fa1e | 0.82791 | -60.5897 | 2025-03-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d31d27f2-3c41-304d-a507-bdd8cc2fac62 | 2.19246 | -61.81747 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f72ef81c-d304-31cf-a681-e11c1adc5046 | 4.27881 | -61.3275 | 2025-03-30 05:53:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abc6c3c7-8baa-3310-9eba-8e2f7cb5a194 | 2.07556 | -60.95786 | 2025-03-30 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de82fb66-f730-3e85-98c9-985d7187f580 | 2.13832 | -61.85669 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5250ef8a-ae53-311a-86c0-dcb8ae0a7bcb | 1.12236 | -60.52429 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 496ee8cd-d8cc-33e5-a21c-98bd4eb49ebb | 2.13912 | -61.86164 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a99cde3-1bb7-38cd-8f2b-1346e33c8ccc | 2.06822 | -60.96371 | 2025-03-30 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8752353e-9edb-3cd7-9cbf-fa9c9814ea7e | 2.13873 | -61.85743 | 2025-03-30 06:14:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d99f04bd-8de4-3a87-a17f-24455e6194c7 | 2.13948 | -61.86182 | 2025-03-30 06:14:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1864c76-50d5-390f-88b5-4d2219bc0fc8 | 2.07455 | -60.96271 | 2025-03-30 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bd5610d-a5ca-324e-b8ad-ebec0e006fdd | 1.83173 | -60.88008 | 2025-03-30 06:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd9fb013-79a0-3e13-a7e7-b35a5c023a53 | 0.82628 | -60.596 | 2025-03-30 06:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91d45150-4d8b-3a48-b010-39fa9d5a04a4 | 1.83257 | -60.88524 | 2025-03-30 06:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16cca264-d173-30d6-8660-cac0f56c1a9f | 0.83068 | -60.59003 | 2025-03-30 06:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 849b3fa2-6781-32de-8d8f-4f76230ce843 | 2.13595 | -61.85921 | 2025-03-30 06:16:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b9269f-9abe-3220-beb2-e57540babbf0 | 0.82408 | -60.59101 | 2025-03-30 06:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 298a3642-7161-3108-b769-85c91129a6ac | 2.14193 | -61.85826 | 2025-03-30 06:16:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b00a1ee4-c03e-3cd1-b5f4-0f62d3e194ee | 1.82535 | -60.88112 | 2025-03-30 06:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98d74ec9-4a8a-3f1e-b410-0373fa2e841c | 0.82537 | -60.59038 | 2025-03-30 06:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd2c95b2-4875-348d-a57e-ccd36e24e580 | 1.8262 | -60.88626 | 2025-03-30 06:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b9be799-e87c-3859-b14f-c0e86594e2e4 | 1.11931 | -60.52402 | 2025-03-30 06:37:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |


