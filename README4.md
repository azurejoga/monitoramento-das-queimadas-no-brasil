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
| 4f77f261-40d7-3abf-9b84-82539372e033 | -14.555 | -45.5146 | 2025-03-18 12:30:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 697e05e0-0599-32e1-b76b-91074dd0d2fb | -14.555 | -45.5146 | 2025-03-18 12:40:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d16e463b-68e4-3031-b4c8-76711993287c | -14.555 | -45.5146 | 2025-03-18 12:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| da8e6b92-59fe-31ff-bf32-155df022e9e0 | -12.547 | -45.342 | 2025-03-18 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ce41c1ac-2ffa-3fe6-a699-4ed001c471b9 | -12.0812 | -45.6195 | 2025-03-18 13:30:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e6bf53db-270f-3c22-880f-f7d0edb445ba | -14.555 | -45.5146 | 2025-03-18 13:30:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2c0804ae-860e-3c5e-9321-5d8f58480863 | -14.555 | -45.5146 | 2025-03-18 13:40:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1036dc89-6fe7-3f6e-98c2-1a7432f7f690 | -12.0808 | -45.6425 | 2025-03-18 13:40:00 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3b146233-e0a0-3ddb-aaac-a0ecb71b0a74 | -8.8456 | -36.867 | 2025-03-18 13:40:00 | GOES-16 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 109.7 |
| bedc93d5-cc3c-303a-a818-c2bc815edbf1 | -14.555 | -45.5146 | 2025-03-18 13:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 62850943-6e18-3b21-b692-ce4b782a4403 | -14.536 | -45.4948 | 2025-03-18 13:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| bc55e668-3f5f-3be4-a8b8-790b053a710e | -14.5355 | -45.5181 | 2025-03-18 13:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 84fd9320-7e35-3526-9ea7-fad505d8d3b8 | -12.0812 | -45.6195 | 2025-03-18 13:50:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 51533bee-7b99-3a1f-97d7-192a4c5253ee | -14.555 | -45.5146 | 2025-03-18 14:00:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d3c49a36-ce1c-37b0-90c8-18061073af0c | -12.0808 | -45.6425 | 2025-03-18 14:00:00 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0892b05a-db64-3a1f-b21f-6c659ae72ad9 | -12.0812 | -45.6195 | 2025-03-18 14:00:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| efc49161-34aa-3edd-8d1d-c89069168a24 | -14.555 | -45.5146 | 2025-03-18 14:10:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c2f287f9-44f0-3fb4-8027-a3ab0994fc93 | -13.6764 | -43.0064 | 2025-03-18 14:30:00 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 30cf3acb-ddc0-3c76-8dee-4c4091844cd0 | -14.555 | -45.5146 | 2025-03-18 14:30:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |


