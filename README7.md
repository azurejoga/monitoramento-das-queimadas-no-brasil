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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f197f8e-1176-3b7e-b1b3-88e4b501347d | 1.32766 | -60.43099 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2f3d190-18ae-395b-8e04-b2f34da5195c | 1.93402 | -60.39473 | 2025-03-02 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92a2ae61-664d-30a7-b501-322ccace9ddf | 1.31423 | -60.43321 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62b383bf-c6f9-3262-8dfa-f338affa9e0e | 1.32376 | -60.42537 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46aed5da-d08e-3c68-a55e-e293059e61f8 | 1.32666 | -60.42509 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78d4080-59fb-3352-85e0-0b3530aabcc1 | 1.31801 | -60.43243 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49bd8584-125d-3cae-8713-2f7db4a27254 | 1.32194 | -60.43797 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2c7a4d1b-3ec9-355e-90c6-b2e66d30d7ec | 1.32094 | -60.43209 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 154dbacf-6dab-3000-9f67-e6ad8fe29a5d | 3.23511 | -60.47574 | 2025-03-02 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd6cfa66-ffe3-35df-8a1f-2ded076ab546 | 1.31896 | -60.43829 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7476edb7-e4ab-3260-b518-d9425ef8dbdd | 0.96181 | -60.53202 | 2025-03-02 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cd7a876-2df7-370b-ad14-4aa2e07e59ad | 1.31994 | -60.42621 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fb818fe-5e69-3e64-b158-6e7e9af3b934 | 2.18888 | -61.85529 | 2025-03-02 06:18:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bad9109-6f9a-3f39-b94b-dc7281d063fd | 3.24123 | -60.47003 | 2025-03-02 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c95a2d3d-4e02-3e67-b939-42f9e75cfbdb | 3.24065 | -60.46915 | 2025-03-02 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46ccd442-8a20-36f3-a64d-e1907ac8da39 | 0.96851 | -60.5308 | 2025-03-02 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72c4c8de-8f36-347b-b5e1-e5c875c97031 | 2.18812 | -61.85066 | 2025-03-02 06:18:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f583ee4-7828-355c-b110-753f5425ebdb | 1.93973 | -60.38783 | 2025-03-02 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e179acf1-c17c-386b-b321-797f91692b80 | 2.58296 | -60.62596 | 2025-03-02 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d237c28f-4aae-37b8-80e0-bb95366c4daf | 2.11349 | -61.81597 | 2025-03-02 06:18:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b1021d1-f66b-33be-a3e6-4dcc8d01ea18 | 1.32567 | -60.43716 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12b39bbe-40ab-3089-b65b-990ba80b686f | 2.18964 | -61.85991 | 2025-03-02 06:18:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69a1e43d-b6ae-329d-bbe8-212bb0305a25 | 1.94093 | -60.39509 | 2025-03-02 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec8a9151-74ae-3a96-bf43-13377d37fe62 | 2.11429 | -61.82069 | 2025-03-02 06:18:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3325ff8a-e3c8-3df1-ba33-6f0359847306 | 3.23472 | -60.47117 | 2025-03-02 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 564520d5-93b4-3aac-8b3b-9f231e8ce7e2 | 2.11403 | -61.81759 | 2025-03-02 06:18:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 647538ec-2fb0-3054-8622-889e6ff1c052 | 1.32472 | -60.43128 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0be947d0-b5de-3e57-9a6c-33f9b9b3c4e0 | 0.7716 | -60.54658 | 2025-03-02 06:20:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3ec06b86-2d02-3472-a508-47041360287a | -9.26139 | -60.30925 | 2025-03-02 06:22:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |


