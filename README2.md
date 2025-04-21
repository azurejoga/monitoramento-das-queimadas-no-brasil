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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d9973ef-6a95-3063-8a6c-125937355368 | -20.87122 | -49.05237 | 2025-04-21 04:27:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90816c66-09c6-3082-9324-3d615590f6d5 | -17.59581 | -43.19695 | 2025-04-21 04:27:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c88a94c-10af-3eb7-959d-a9d1893db34e | -20.57696 | -44.57383 | 2025-04-21 04:27:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67889b5a-3e5a-3065-a5bf-7ba82bbcf21f | -19.72937 | -49.79121 | 2025-04-21 04:27:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b574d65-fe4a-371b-9d45-17f0defe4f8e | -20.41813 | -43.55273 | 2025-04-21 04:27:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9b48ddac-65c3-3735-af7f-6617fd0bf797 | -21.19642 | -44.93756 | 2025-04-21 04:27:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed67424f-0493-3ea5-967c-59ed3bfdb2b6 | -17.77921 | -42.80931 | 2025-04-21 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dde7870-1cd8-31f5-903c-bd2605b00a1e | -17.00829 | -49.78145 | 2025-04-21 04:27:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e668f4c3-b6c6-33f6-8654-9a63102c941f | -30.32019 | -51.5126 | 2025-04-21 04:29:00 | NOAA-20 | MARIANA PIMENTEL | RIO GRANDE DO SUL | Brasil | 4311981 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 854e4fde-4834-3e30-b7be-68a8d45623fd | -24.242 | -50.73866 | 2025-04-21 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2fbf5085-48ff-3e42-a44f-0902cf566d47 | -11.40474 | -52.95899 | 2025-04-21 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a831ea3-8673-3ff9-907f-3db868d4db5c | -11.40075 | -52.95366 | 2025-04-21 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e780cca-3623-39e2-9040-5e90a3b9aea6 | -11.86901 | -52.26798 | 2025-04-21 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88e30a7e-33d8-3e58-b5f7-5f727ce99d1d | -11.40015 | -52.95839 | 2025-04-21 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 913df7b2-e2f9-3f6a-8b30-7f7f7609a3cb | -11.86831 | -52.27346 | 2025-04-21 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e25abc91-5c9e-3c2a-9c35-ac81f1cf05e6 | -19.72457 | -49.79144 | 2025-04-21 05:21:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44d56ed2-83a5-3389-aa61-a975f44d04d2 | -19.72409 | -49.79663 | 2025-04-21 05:21:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a8dc606-1038-3451-9640-08a03bcbe4e9 | -19.72834 | -49.79179 | 2025-04-21 05:21:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd0ed63a-e389-3699-9f66-185af0b646b5 | -11.39822 | -52.95186 | 2025-04-21 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 48c169bf-3786-3655-bb4c-67d387711837 | -11.1467 | -39.1378 | 2025-04-21 13:50:00 | GOES-19 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 95.5 |


