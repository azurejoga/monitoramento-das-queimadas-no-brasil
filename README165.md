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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc1ad702-1c6a-306f-86a9-9cdece653346 | -6.45392 | -41.76935 | 2024-10-25 16:52:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 3afad4ef-10ad-34eb-bfcf-9dcb34b27151 | -7.47068 | -42.06813 | 2024-10-25 16:52:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9bb6f312-e044-39ef-8790-ae584e5926e1 | -7.40899 | -41.98207 | 2024-10-25 16:52:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 3c948ac4-fbe0-3bef-97be-efeddf6885c4 | -7.32972 | -42.17894 | 2024-10-25 16:52:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1902188c-4cad-3bdb-9913-0515db4a517a | -6.99664 | -42.09977 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| bb334c1e-5078-314d-80ec-aad3cf463c8f | -6.99614 | -42.09688 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 28de508f-c778-338e-ab42-a1b72b1af9c7 | -6.89056 | -42.08246 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 29890276-852d-3082-b2f7-0f7400cf0f85 | -6.74864 | -42.06633 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| bac43141-f9e4-3f39-bacf-e49cf21c1613 | -6.74808 | -42.06311 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3991a288-6ebc-3125-b0e2-13bc09921b40 | -6.66634 | -41.94552 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| f3882590-d19f-3571-83ce-1725c2d6a15b | -7.88851 | -40.78495 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 033afac3-bf86-347b-93e0-ffedd7e1e467 | -7.86876 | -40.78275 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 079f408b-a946-388d-8075-82b22ffd6015 | -7.86395 | -40.78688 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 7a7af057-88f7-3d67-9483-31f7e52fb5c5 | -7.86334 | -40.78344 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 4cf3c94c-46a2-36e9-b015-17cae63fad14 | -7.85862 | -40.78807 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 54e638ba-6727-37af-8fab-3936b8d524a0 | -7.858 | -40.78461 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 4faf3aa4-f9be-3b17-bbe4-64d2c034ff60 | -7.62796 | -40.79966 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 42d1c6d0-f7db-3bd1-8ea3-484646abf156 | -7.62734 | -40.79618 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dd4e68a0-fa8b-3449-9afd-0889fe4d1a9d | -7.44111 | -40.80631 | 2024-10-25 16:52:00 | NOAA-21 | PADRE MARCOS | PIAUÍ | Brasil | 2207207 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2e3dce3f-b3ac-3718-b4a4-6284b74a986d | -7.31847 | -40.72271 | 2024-10-25 16:52:00 | NOAA-21 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fc340ae2-44d2-38e6-bf91-e0dbe5faff43 | -8.02015 | -40.87287 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 14ffe3c5-fd31-38fb-b193-faba548dc858 | -8.01956 | -40.86953 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 5a410466-35cd-36c9-83c0-48fbc364ab88 | -8.01787 | -40.87039 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 1264582b-e122-3f58-bd34-2e8e374037bc | -8.01726 | -40.86705 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| facceb12-14a3-3304-bdad-a8851e3b6b48 | -7.96237 | -40.97974 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9bb004a5-e8ed-35c3-8d74-43b93e60ecfb | -7.92695 | -41.11301 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| f627bf62-9835-3842-9b06-a6d507c89b61 | -7.92638 | -41.10979 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| c8b089d8-a65b-3bfb-aa9c-0708cf57d00f | -7.92582 | -41.10657 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 342a1bba-0e0e-3042-853a-7ecbab2a830b | -7.92115 | -41.11086 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| fc5ab825-43da-3cf4-802b-f3a80d1be737 | -7.92058 | -41.10761 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 79fcd655-b039-310d-9058-d948b547dec3 | -7.91591 | -40.87455 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 04b9c586-9a4c-3069-9891-c71b214fba70 | -7.88965 | -40.99414 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 3c380ed8-344b-3209-8a48-d89dc1e94196 | -7.83194 | -40.97745 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 7b09a705-c493-3581-8414-77e7f95a6deb | -7.82725 | -40.9818 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 5206615a-47ce-3773-b98c-7a4765c6e981 | -7.82665 | -40.9785 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 672ab974-bf6a-377d-8e01-df9fa548b8de | -7.82276 | -41.81407 | 2024-10-25 16:52:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 80b60b3b-38cd-3411-88f6-b9ff6ce3d97f | -7.82225 | -41.81115 | 2024-10-25 16:52:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 39fe4261-87e1-344c-b2a3-58315384b40b | -7.80949 | -40.93534 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ffe8e31b-d8ea-310e-bb50-47bccd6b9a34 | -7.76112 | -41.12472 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 3118a719-dd8d-34eb-a1dd-b573f193d22d | -7.76053 | -41.12143 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 4fe86ea8-dba0-3b52-8246-8bc0310ecc65 | -7.75994 | -41.11815 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| c5482cd0-7455-3fd3-8700-9ff4ed6d709e | -7.75585 | -41.12563 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| f4d279b2-6857-3477-bbc8-a800dd8a7e29 | -7.75526 | -41.12234 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 6d529b00-32d3-34ef-88aa-edeb8e0e1387 | -7.72847 | -40.97374 | 2024-10-25 16:52:00 | NOAA-21 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| df261812-dcb9-3d5a-aebe-7997e2776ea5 | -7.72787 | -40.97041 | 2024-10-25 16:52:00 | NOAA-21 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| b8371d5f-f666-358b-a4b8-d8c13d38e019 | -7.54862 | -41.05423 | 2024-10-25 16:52:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ade3e5ae-7779-399a-862e-2dec33c8a012 | -7.5017 | -41.15215 | 2024-10-25 16:52:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| d7e08e89-9efa-3db3-b467-fd26d5fdd3dc | -7.48249 | -41.7235 | 2024-10-25 16:52:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 230b3801-49a0-3e88-b1b4-6dd40485c3f2 | -7.47743 | -41.48045 | 2024-10-25 16:52:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| fe1d798b-9997-3cfb-910b-eca671d9c2d9 | -7.47689 | -41.47731 | 2024-10-25 16:52:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 19924fcb-24da-3ea6-876e-ad09172a5b79 | -7.47389 | -41.48105 | 2024-10-25 16:52:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 2e7ef510-0544-378a-b51e-e8d6e0fbd39b | -7.47333 | -41.47796 | 2024-10-25 16:52:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| c89753fb-e961-3b1c-bbbb-37caa2060bed | -7.42385 | -41.79769 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 654957a5-57a3-33d7-b9d1-b33376b1fb1e | -7.42263 | -41.79904 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f00ecaa-65b1-364a-b12b-12ca07335635 | -7.41878 | -41.79852 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 774b641e-befe-3d4e-9510-f61a38d32531 | -7.41828 | -41.79559 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9cc266fe-4ae4-3333-affb-b896a01191b9 | -7.41704 | -41.79694 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9e305142-c957-329f-a89d-d44ebdbfd2c3 | -7.41651 | -41.79399 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 016ce195-4d92-35a4-b282-a82b457f50d9 | -7.41015 | -41.86933 | 2024-10-25 16:52:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e6c3c8d6-adce-3cee-a6aa-c7f365721441 | -7.36984 | -40.88911 | 2024-10-25 16:52:00 | NOAA-21 | PADRE MARCOS | PIAUÍ | Brasil | 2207207 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c879118f-521d-3831-a719-df12fd5d25f7 | -7.33912 | -41.79077 | 2024-10-25 16:52:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7d475e9d-493f-3791-9b56-71ba1ec3a566 | -8.24861 | -41.1288 | 2024-10-25 16:52:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| fd447011-88fd-395c-9d1e-cfb7619e3c64 | -8.24803 | -41.12547 | 2024-10-25 16:52:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 9ced1527-bfa4-3c36-bac6-62901e7b7da8 | -8.23055 | -41.67031 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0968c7e7-8fb1-30dc-9a0b-469a64fd3335 | -8.10684 | -41.21152 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b9365932-35f2-3590-8933-6c6dd8567813 | -8.10166 | -41.21255 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1cf3ae6b-b440-3b08-a3d2-5b1e506a1039 | -8.05027 | -41.44091 | 2024-10-25 16:52:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6d6bc094-9911-37dd-8d73-4a5aedd6506f | -3.5306 | -42.45771 | 2024-10-25 16:52:00 | NOAA-21 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4663ea2b-4a6a-3f58-ae2f-91290e75d2c0 | -3.52918 | -42.45976 | 2024-10-25 16:52:00 | NOAA-21 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d29afac3-f073-3445-8d62-ad6523d6b1f0 | -3.48309 | -42.87358 | 2024-10-25 16:52:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d72938dc-a191-3fa1-8bfd-5755446c5264 | -3.22868 | -42.69919 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e006010-7581-3970-aca1-b622f31558be | -3.22818 | -42.69613 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9fa4f2b-f9c0-3643-911c-c94dbf3b50bc | -3.0729 | -42.69554 | 2024-10-25 16:52:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 753b0ccc-5db8-36b0-a15e-915d72771305 | -3.06534 | -42.64974 | 2024-10-25 16:52:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94618ffc-4bbb-345b-b0aa-e4b6961b862a | -3.06483 | -42.64664 | 2024-10-25 16:52:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4db2de0-ce3f-34a2-84cf-38fb0bd7fd87 | -3.02214 | -42.08999 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d165a76-784e-359c-ba7e-f2e07a2c2fdd | -2.95926 | -42.6924 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4cb3885d-d0f9-332d-8b3d-88e4cd989e8a | -2.95362 | -42.69017 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ae810c43-8d6d-317c-a31b-fd465a33182c | -2.95311 | -42.68711 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7002a3db-4f64-3f72-9874-1f5ad56a70a4 | -2.9526 | -42.68403 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46475883-ffff-3cda-a123-15d9e20f0f4d | -2.94746 | -42.68484 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| af32c332-59ae-33d7-b932-ab2dbd6a1141 | -2.94741 | -42.71622 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 29206fc7-7ca0-35de-a494-3a05398d8efe | -2.9469 | -42.71315 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05399ad9-1780-3af9-99aa-463fdd761b73 | -2.94638 | -42.71008 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e200e319-e897-30a2-ae99-d4ddf2632642 | -2.94232 | -42.68564 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5bbebfcc-5a73-31aa-b4c6-1aea97338e66 | -2.94182 | -42.68261 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 54430616-e0ec-3ab2-8411-fee52f935093 | -2.93984 | -42.7848 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a45c70a-e363-391d-810e-c19e327daa9a | -2.93805 | -42.78602 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d47ce694-f14e-3632-90ed-27464470628f | -2.93668 | -42.68342 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b388b9a-8160-3b91-87e9-75c92f530b83 | -2.83813 | -42.58067 | 2024-10-25 16:52:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86a6974f-0b23-3701-b1c9-6a7dbcd92d5f | -2.78977 | -42.32011 | 2024-10-25 16:52:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9840cb1f-9570-3b43-b04e-334b6abb787a | -3.34235 | -41.41455 | 2024-10-25 16:52:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 39.0 |
| df00a249-8d0a-3f9c-81e2-6c79f7bdda5d | -3.34174 | -41.41082 | 2024-10-25 16:52:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 39.0 |
| 0412351a-977a-31cf-9580-23f70fb06334 | -3.31576 | -41.42639 | 2024-10-25 16:52:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 244.4 |
| 87ae062f-4e5a-312f-bb96-f43fc61b54a5 | -3.31467 | -41.41984 | 2024-10-25 16:52:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 700a48b0-5556-38e5-b26f-90160fa9b440 | -2.90016 | -41.82093 | 2024-10-25 16:52:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5d9ba873-39ff-3044-be5c-33f981a4fd72 | -2.89957 | -41.8174 | 2024-10-25 16:52:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e56b3cef-aeea-30fa-94ab-a418019bcc37 | -2.89898 | -41.81389 | 2024-10-25 16:52:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| babbd1b4-e294-3c23-91bb-abdf9948b2b2 | -2.89879 | -41.82038 | 2024-10-25 16:52:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b2ec574-75fc-3584-aea4-7ece7827f489 | -2.89822 | -41.81685 | 2024-10-25 16:52:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README166.md)
