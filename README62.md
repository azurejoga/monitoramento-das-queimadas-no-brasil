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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb713ad8-476d-3591-87e1-548adb45ef1b | -7.8416 | -46.42 | 2025-10-26 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| d82a43b1-b925-3dd5-bfdf-c16fb4ed9825 | -7.4578 | -47.2082 | 2025-10-26 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f5dccadb-5da3-3903-92d3-316f567ccab1 | -6.7272 | -45.3941 | 2025-10-26 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2fc0b7f3-d2fd-36b4-ba47-2c491eb68e8c | -9.2653 | -45.5762 | 2025-10-26 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c1d4cbc9-9a74-3437-8154-056d5d11f979 | -6.9388 | -44.8766 | 2025-10-26 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 69a9c557-0540-33ee-bb9c-1190323a65ce | -10.4065 | -45.3244 | 2025-10-26 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 56c6e63b-bc2d-3d15-8c8a-426281d86ab1 | -7.8875 | -45.6973 | 2025-10-26 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 005f194c-d455-35b9-a004-74ab5c88a5ce | -13.8945 | -48.4586 | 2025-10-26 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 57084fe2-2705-3e8e-aeab-dac152525e9b | -3.6956 | -43.5359 | 2025-10-26 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a2269a19-2415-3f6f-9d62-0166e816fe29 | -8.559 | -47.7252 | 2025-10-26 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 55a0e7d4-73f0-39bc-92df-b92060e647d3 | -13.2777 | -54.3882 | 2025-10-26 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 246.6 |
| 613effd0-417f-30c1-b4dd-d86e48e6e34a | -8.0446 | -46.7353 | 2025-10-26 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d64fd9b2-bfea-3dc0-91e1-31e834894664 | -8.4475 | -47.626 | 2025-10-26 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 2de22c52-f320-3874-a982-dd8464426629 | -14.2974 | -51.7927 | 2025-10-26 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5b285b0f-b755-316c-908e-5e70c6b9ed97 | -7.4231 | -48.7596 | 2025-10-26 14:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3499e61d-1ce1-3190-81d7-ed458dab3655 | -13.6249 | -48.4323 | 2025-10-26 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7360ee99-f0a0-331c-8af4-6c58610d06a3 | -9.5682 | -46.9141 | 2025-10-26 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7812ccb4-ee1b-3764-9def-f69decce8fdc | -8.2282 | -45.5282 | 2025-10-26 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e800e35a-42cf-35f0-9c29-a1a3029a3e9b | -4.8397 | -42.911 | 2025-10-26 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 77152b7e-3796-3485-984a-44ae8ea2f31f | -5.834 | -40.828 | 2025-10-26 14:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 109.7 |
| d84bebf4-f3be-3722-b04e-a2706d347fca | -4.4787 | -43.6789 | 2025-10-26 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 80b34f9c-e2ca-3f1b-b322-3b7269f75748 | -9.2539 | -46.4122 | 2025-10-26 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 6a55b440-8cf3-3936-8fa1-d9c2e354b8d8 | -6.939 | -44.8538 | 2025-10-26 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 0b847577-9d13-36e3-bd13-bd4a40a93f43 | -17.4317 | -46.8608 | 2025-10-26 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 120.4 |
| db53eff0-4546-301d-9476-3702ae0d1ac7 | -11.327 | -53.9254 | 2025-10-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 59552528-172b-3a07-a0c1-ede9a1bd0917 | -6.7832 | -45.4121 | 2025-10-26 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |


