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
| 90788270-81aa-34d4-a53e-2cec1d5481f9 | -5.15924 | -37.68727 | 2025-07-14 03:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c7608d9c-067e-313e-92d3-1b782195b16c | -4.51171 | -38.54832 | 2025-07-14 03:10:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4f8a2352-0e0b-38da-8379-c85000f3dafb | -4.51085 | -38.55323 | 2025-07-14 03:10:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| aee83968-2c3e-3431-bba0-b88cb67657e8 | -22.89946 | -43.75113 | 2025-07-14 03:15:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1e9fa123-13a7-3966-8d68-69cff4e999fb | -8.5022 | -43.3085 | 2025-07-14 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 406c4b2a-fdc5-35ec-bca2-b35da52cce86 | -8.5211 | -43.3063 | 2025-07-14 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 486fae48-a67a-38f0-9cdf-185812efe114 | -8.5211 | -43.3063 | 2025-07-14 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 863d7047-8b2a-386a-b14a-e5af4969af67 | -8.5211 | -43.3063 | 2025-07-14 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 760662c5-510f-3f18-9e82-d2f3af4e5c80 | -8.5211 | -43.3063 | 2025-07-14 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 24b0de5d-82f6-3d3f-9dda-6861cc53df5f | -22.4715 | -52.4162 | 2025-07-14 04:00:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.4 |
| ab6703f6-a030-3713-af18-36532e08561c | -8.5211 | -43.3063 | 2025-07-14 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 956f119e-1b3d-3e1d-802a-6ab9d5bafbc9 | -22.4929 | -52.3894 | 2025-07-14 04:00:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 2de7c7f1-935a-34a6-a14f-902d5b0abc4f | -22.4721 | -52.3937 | 2025-07-14 04:00:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 177.0 |
| 7c150d7a-5380-395c-843b-b4ef1ea2ca9e | -4.33858 | -38.64158 | 2025-07-14 04:00:00 | NOAA-21 | BARREIRA | CEARÁ | Brasil | 2301950 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90032cb9-6e00-3748-afe4-a605d097b72e | -2.91321 | -48.2403 | 2025-07-14 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9d14e188-0833-3bcb-9bf2-5f3f5403bc19 | -5.15879 | -37.68545 | 2025-07-14 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 70771826-4adc-3a1b-9172-015fe98573bb | -4.51605 | -38.55059 | 2025-07-14 04:00:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 50b81b65-a701-34f8-b708-f4dea463d248 | -3.78784 | -47.08804 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33e69074-4e08-392f-9569-8c1b40a2aa34 | -3.58213 | -47.52803 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0dd8e767-7758-3d85-8a35-4d682431e778 | -3.58306 | -47.52242 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 35e1a4af-7ae9-33a1-9254-d345f3838592 | -3.58399 | -47.51682 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a1a927a9-26ca-3bfb-a892-142ed311b740 | -4.51326 | -38.54655 | 2025-07-14 04:00:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d6fd08af-4413-3e92-80b4-6810e5d50426 | -3.58492 | -47.51123 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| db86e63a-34cc-3cbe-a433-0abf1338321a | -5.15822 | -37.68922 | 2025-07-14 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8c8c189e-24cd-3591-844e-bf673d003960 | -2.90794 | -48.23953 | 2025-07-14 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| edfee7aa-5e1e-3e6e-ba5a-bbff4af8f5ac | -3.58801 | -47.52325 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13e44edc-f3a2-3598-bb77-557fc8493745 | -3.58706 | -47.52894 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3c9f4117-1e5b-3f65-835c-d88a36e6cb4b | -5.15535 | -37.68493 | 2025-07-14 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e82f8682-dcb3-30b5-836e-d86ec1f85512 | -4.5166 | -38.54706 | 2025-07-14 04:00:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f59ec6cc-661d-3f3a-9ea8-f6db0d11ab31 | -3.57904 | -47.51604 | 2025-07-14 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 736b15b5-afec-33ba-81a2-8071a33aa18c | -4.51271 | -38.55008 | 2025-07-14 04:00:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 342903e4-d76d-32d5-8ff5-fffd7ad50653 | -10.99 | -47.08888 | 2025-07-14 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7070b762-224e-34e4-8a39-0161cc2cef6d | -6.65541 | -43.09036 | 2025-07-14 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7e7b37d-4ca6-3c18-b300-9236badd2472 | -8.04842 | -50.10036 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dace61d-279b-3581-a636-8954e1e1f03f | -6.5318 | -42.37021 | 2025-07-14 04:02:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5fc2c222-83c6-3428-afeb-4b2426b1b598 | -4.3031 | -48.10343 | 2025-07-14 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3ef2fcdc-12b2-3f66-b4ff-eeb98e2c6e99 | -8.04895 | -50.09739 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d80349a-84de-3e95-9b49-4384fc950631 | -7.35051 | -41.15506 | 2025-07-14 04:02:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b6a8f896-1108-39b3-bd51-46a005821695 | -4.1211 | -47.35762 | 2025-07-14 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c38ee035-53b0-317e-839b-d5a931a5fca6 | -7.26528 | -45.31424 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6f20a29b-939e-3905-8c4a-61325a077ec6 | -5.24868 | -39.48062 | 2025-07-14 04:02:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 53c96f8c-c35f-39c5-bd07-83070253d4ab | -6.85019 | -42.76492 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 47ea6312-9162-3deb-9d27-4f84d76a2a4f | -7.31132 | -50.06203 | 2025-07-14 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7f46d36-77a9-3741-a894-0b38b288e0f4 | -7.05318 | -43.96065 | 2025-07-14 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af5f95fe-c4f0-3db8-afbb-eba35574efbe | -7.58366 | -44.72392 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e159282f-6b6d-34ef-aa23-1c5e27e38a19 | -4.30457 | -48.10551 | 2025-07-14 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| a1f0eb91-928b-350f-88af-2df7449f3e65 | -11.0317 | -47.07584 | 2025-07-14 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f4d2673-2e0c-3f48-87ff-f1ae38abcc61 | -7.54115 | -46.08447 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a591d2e9-7421-369c-aefc-a5d4df5984b3 | -6.64778 | -45.0215 | 2025-07-14 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a711e96f-810b-3e14-90a2-6f141937e7c6 | -4.86536 | -43.22075 | 2025-07-14 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 429e26e4-7496-3947-97f1-79ed400bb55c | -7.01882 | -43.73013 | 2025-07-14 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47264e7e-e82f-3d8f-9829-ad1ae21e1fc5 | -9.50771 | -47.5681 | 2025-07-14 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa4a6ad1-cf1f-3634-a16f-8419c255995f | -5.2684 | -45.12782 | 2025-07-14 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c399a2f8-9ef9-3811-9341-990f8ac17f14 | -8.9083 | -47.34983 | 2025-07-14 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cda4e4e6-1b0d-3f4a-b56e-e7e764036a14 | -5.44768 | -43.58768 | 2025-07-14 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c6b2f35-2b79-3554-9867-a274062d78a1 | -8.03824 | -50.09426 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b8963878-1bd2-3b34-9b71-16298d2a797f | -5.28072 | -44.87917 | 2025-07-14 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15bd6e18-0735-3d95-ae9e-d9a6b82a73e2 | -8.44047 | -45.80621 | 2025-07-14 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea59365e-62cc-337b-832b-275172c088b8 | -9.48823 | -40.38793 | 2025-07-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 47dd7cf4-bb42-3931-acee-0235738fabb9 | -6.27643 | -43.42862 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8ffef2b-90dd-3f1d-8762-ede719c69ecb | -6.84189 | -42.77174 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 68ba6c2b-4457-3461-8a50-7b8b97d3294b | -6.28288 | -43.41222 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bfdd468-9dfe-3768-a2c8-341666d989f1 | -10.27868 | -47.61551 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 56a02ec2-2649-31ae-9ea9-02d4b9c43ccf | -4.58422 | -47.26779 | 2025-07-14 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f62493c-8414-36f3-b388-fa193d509ce4 | -7.27332 | -45.31554 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d14b25fb-fba0-3fa8-9e74-3ba63aec7185 | -8.86575 | -46.87165 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aa0325e6-2525-3e77-af3f-67b12702420e | -9.50321 | -47.56734 | 2025-07-14 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa4363c-7a07-3748-8b78-4db2ca770105 | -4.30767 | -48.10729 | 2025-07-14 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c7562a1a-abd9-39b1-ab83-ea0068b55e22 | -6.85083 | -42.76098 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d95389af-187a-3b14-91f2-f675ac68bcf3 | -9.9483 | -48.16626 | 2025-07-14 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11684966-6858-333c-9c34-ef119281a3d3 | -6.46525 | -45.37 | 2025-07-14 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 016fa7cf-7af0-3bc6-bf04-58f1da42b8f8 | -6.82348 | -44.02113 | 2025-07-14 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acbe902e-5af9-31b0-bec4-4b0f0023c5d3 | -7.04823 | -44.32678 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1d8a192-7f23-3d1a-bc55-3068c5040012 | -4.58512 | -47.26247 | 2025-07-14 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12eb4d5e-8e67-3b03-a376-eb65ef08a1e0 | -6.84669 | -42.76436 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f521f280-c3a4-3497-9232-451bb122010b | -5.28415 | -44.88341 | 2025-07-14 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a469e29-c688-3e93-b878-4a7403300fa2 | -4.30819 | -48.10428 | 2025-07-14 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1a36b2a3-db43-3149-9dd7-ddc6b8bc603b | -6.96415 | -42.73427 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c616912f-6e0c-3a51-af1b-c6beedee0162 | -6.26063 | -43.36198 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c3447c1-d1f4-3c98-aa37-5a2ec93b59ad | -6.96478 | -42.7304 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd4e3ed3-caba-3ad2-b42f-12b3d0e5a452 | -6.87188 | -42.76421 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f947759-c779-37ca-85d3-5b0b2801c632 | -6.95413 | -45.24957 | 2025-07-14 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f6949cd-5f7b-3504-973c-cdba64f7781e | -7.58285 | -44.72868 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 890ae220-f4cc-380c-9b26-d6d958b48aaa | -7.58148 | -44.72595 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 738590a9-7091-3e61-b7c7-b58df8818a6b | -3.98344 | -48.42017 | 2025-07-14 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2aed087-4fb7-35ed-b1ce-12d5438fc048 | -5.28012 | -44.88276 | 2025-07-14 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b3b72ca-7b53-33d9-b334-f5c1d70a2010 | -7.04437 | -44.37378 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 901ff23a-11e8-3e9e-8499-ecad154b8921 | -8.03888 | -50.09068 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 75a9a932-77ea-3023-b32b-eef05b1b49cb | -7.29701 | -44.62857 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 175ad668-d0a5-3ca8-adfb-524c24e955b2 | -7.27183 | -43.49337 | 2025-07-14 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 243d554c-271f-370e-b647-1a3b01ae4335 | -6.88185 | -44.10972 | 2025-07-14 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50c9492e-517d-3088-9a5c-c0e5486c4934 | -6.68758 | -43.68951 | 2025-07-14 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9a1c1df0-06f2-3fea-89c9-760128ee282f | -8.24822 | -41.93317 | 2025-07-14 04:02:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2587953c-c9ff-33e2-9700-1c5792a289f3 | -8.8708 | -46.86833 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c77701f-10e3-3dc5-8380-b02d27c32ba9 | -4.01044 | -49.4705 | 2025-07-14 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 150f7dd7-6ea1-3b2f-a9b4-d84a8d954766 | -6.24089 | -43.34587 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 563d894f-f8cf-3378-b4aa-4499a109b919 | -8.04493 | -50.09408 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1efcbaed-f36e-3532-b243-580d5bcd4dce | -11.57971 | -47.32633 | 2025-07-14 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e2a3732-6526-3ce5-9666-202235663f5e | -7.41921 | -43.89646 | 2025-07-14 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe04f76-754d-3364-bc6b-395d2348dd66 | -9.49276 | -47.56278 | 2025-07-14 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README4.md)
