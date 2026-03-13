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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 585f512e-a17c-35a1-a3d0-349604b60386 | 2.05619 | -60.57383 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21bb6081-cd14-3892-a76f-a26c40d39953 | 2.98688 | -60.68364 | 2026-03-13 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24871624-cdfe-3edb-9adb-791af20cfa2c | 0.9446 | -60.18414 | 2026-03-13 05:33:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10258f21-9a13-3b36-b259-18e4a584b22b | 2.31411 | -60.23716 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7851cbdf-bb71-393e-b1a4-2fe1efb5431d | 1.24911 | -60.81498 | 2026-03-13 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 684150fe-6fb3-3c25-90c3-4fcb634e5662 | 2.316 | -60.2409 | 2026-03-13 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| fff8d4e2-0dbc-3b98-902a-315cc84d39d5 | 1.33449 | -60.72781 | 2026-03-13 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15f60431-2dd0-35fc-a1f9-99a69b770c5f | 2.78212 | -60.65763 | 2026-03-13 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0dfa741d-712f-33ce-8871-79e38d1a5b8b | 1.25343 | -60.81429 | 2026-03-13 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61447b9a-d146-33f5-a8e5-56282df60cdd | 2.31154 | -60.24133 | 2026-03-13 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dc6cdec7-c67d-3470-9311-eaa9b6436308 | 2.66537 | -60.39084 | 2026-03-13 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cb0f1ed-4c69-3b4e-b124-5b02eccadc47 | 2.31532 | -60.23674 | 2026-03-13 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 43127fed-722d-3bde-a2c1-2b8b5ee282de | 2.74635 | -60.46835 | 2026-03-13 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45120a53-dd92-3855-87fb-42f586a28d0b | 2.31085 | -60.23711 | 2026-03-13 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3837e76a-c02f-364d-8ec0-c940e4f1af0e | -24.11505 | -48.28739 | 2026-03-13 06:29:00 | AQUA_M-M | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 69552388-3cb1-3daa-b14b-7f24441155cf | -11.89893 | -45.26426 | 2026-03-13 12:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| dc587dd8-bd19-30ea-add9-6c937865e4e5 | -8.80474 | -44.80216 | 2026-03-13 12:08:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| cf434d6a-7187-33ba-b6ee-1e7a769c7a51 | -12.01605 | -45.35995 | 2026-03-13 12:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b4dbf816-e869-31c7-a8ba-9e471f8a33d6 | -11.90069 | -45.25073 | 2026-03-13 12:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a190ec14-09eb-3a0f-b029-1cd90e661bb5 | -12.01773 | -45.34656 | 2026-03-13 12:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 2df8a6db-371b-36be-9d29-7143c425b9d7 | -7.88175 | -46.33567 | 2026-03-13 12:08:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1233dfba-a032-3767-933a-a16bec37a292 | -23.03053 | -52.66631 | 2026-03-13 12:12:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 46fbf6b2-69ed-34f3-965c-38b6de808af9 | -26.93622 | -52.56891 | 2026-03-13 12:14:00 | TERRA_M-T | XAXIM | SANTA CATARINA | Brasil | 4219705 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |


