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
| 0dd9278c-8b24-3ab6-b317-650412051dfa | 3.83547 | -61.01064 | 2026-02-14 07:09:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ef4a84c-5487-361e-b4ba-9f2d41eb566a | 3.88277 | -61.02628 | 2026-02-14 07:09:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c1c2f32a-5a3a-35c5-a557-a0a84950a9a8 | 4.20835 | -60.54106 | 2026-02-14 07:09:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a1abb0f1-571c-3d02-b50a-21fa721a3e04 | 4.20618 | -60.89272 | 2026-02-14 07:09:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb69fa06-a1f6-3851-a195-be0e94d493c9 | 3.87221 | -61.01804 | 2026-02-14 07:09:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d4f5890-e89d-3b39-bf4c-1f348495c244 | 3.84318 | -60.99974 | 2026-02-14 07:09:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 73e75667-9023-3e56-8e61-558cf924d515 | 3.73868 | -60.92366 | 2026-02-14 07:09:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d43903e-f089-3104-bf82-fa1a50c00590 | 3.1101 | -60.31198 | 2026-02-14 07:09:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b096b0ef-6cac-33f0-b1a3-dbafec91dea1 | 3.7302 | -60.9242 | 2026-02-14 08:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d0b6b38f-329b-36a3-9d02-48588ec23c8e | -11.96941 | -54.13179 | 2026-02-14 12:31:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d129d5e1-2c45-35be-bbb9-8c7abc9933e7 | -14.05329 | -52.14976 | 2026-02-14 12:33:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9e907177-8088-3a07-a849-01313f63cb69 | -16.18315 | -47.05793 | 2026-02-14 12:33:00 | TERRA_M-T | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| bbf84519-9df8-33e2-a585-3bae1c00f3a6 | -16.7689 | -47.95717 | 2026-02-14 12:33:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| fd23c325-6669-39dc-aa93-df6aa86f464a | -14.4979 | -46.98644 | 2026-02-14 12:33:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 078b48da-c325-3036-9b40-a8c3a03525f7 | -20.73192 | -56.05522 | 2026-02-14 12:36:00 | TERRA_M-T | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bbd7596f-166e-3e5e-a24f-4d7a8aadbc00 | -30.33051 | -55.90298 | 2026-02-14 12:38:00 | TERRA_M-T | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| dd16e4eb-710f-3f7a-9da7-8bd299021c1a | -30.33277 | -55.90984 | 2026-02-14 12:38:00 | TERRA_M-T | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |


