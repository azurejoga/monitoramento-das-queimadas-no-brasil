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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30e5761c-8c34-382c-b7b5-73a9e66e64f1 | -4.02658 | -46.817 | 2024-12-13 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 660eda91-c264-32ba-b4dc-ab62d1799d52 | -2.44595 | -53.71463 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce023225-4f2f-3540-9ea9-8c9b3bca0a18 | -2.23485 | -53.71063 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8363cfe7-2743-31d1-a325-28dc03f8e178 | -1.25176 | -52.17134 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 200429af-788a-39d3-b6e5-ae0fc7b4d6a4 | -2.50543 | -51.79923 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dfe2b1e-2d37-3bca-aafc-547e6d66934e | -1.32924 | -46.65238 | 2024-12-13 04:42:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cec86f57-515e-350f-b2c8-79ec32154a82 | -6.92219 | -43.52308 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8d062421-b256-32c1-836d-4c76e8548c6f | -2.4726 | -53.64188 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9d2e461-a2aa-36c3-a897-f4eb2331515a | -2.56067 | -53.41338 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8b05596-c8ea-393f-bf3b-158bfcdf8aa7 | -3.03925 | -47.95181 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a604aa87-a13d-3ae0-aec7-207e05dda521 | -4.24402 | -41.92706 | 2024-12-13 04:42:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ee67956-452c-3e10-80d4-35cecbc269f2 | -1.74395 | -52.03009 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf55434d-f1c1-3857-9330-5fd379e53fcf | -2.48606 | -51.81123 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e10fa6e-79fd-390d-ba89-f0afcfd8283e | -2.60712 | -47.71786 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f3f8424-a78f-3038-a877-cc396a03cdee | -2.49463 | -51.80128 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9741688b-9adf-3d8b-bf3f-3193b61467ac | -6.9244 | -43.50772 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3d803f98-376b-3022-8dab-9c7dfd46b985 | -1.05278 | -47.6634 | 2024-12-13 04:42:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b350a99-4be1-35bd-8769-ba8e42500395 | -5.38191 | -48.35934 | 2024-12-13 04:42:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0098243c-1e29-3a88-8ee5-7f56d5cc47c9 | -1.98813 | -54.50839 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e4572b6-9b96-35f4-811f-f61cd1b43c51 | -6.91487 | -43.50636 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d1343da3-7ee2-324b-a94f-3b9c04bd40ac | -1.23574 | -54.13824 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34989c14-c0ca-300b-a62b-2a22a1b2d67d | -2.5026 | -51.79502 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef4a424e-42f4-33b5-b24f-617f1d5e686e | -2.50365 | -46.84755 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f333ba2a-8339-31e1-b03f-25ac218abc8f | -1.99913 | -54.51539 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fda285d-1d2d-3337-95e4-a09ffb8b3b00 | -2.32227 | -53.57045 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b4a5055-8f17-38e9-a809-1558da9be405 | -2.43921 | -53.63653 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9afc4a4d-bb4f-3cc3-8b65-be64f477860f | -3.32185 | -45.70295 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73f5a3ff-8b97-3673-b7fe-a2e56645fac9 | -2.74323 | -52.97223 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8991db06-6987-3e96-a21e-1fbbf0a0eca3 | -2.24293 | -53.68452 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f988099-c704-3317-a50e-8fcbed001dd9 | -6.91596 | -43.53264 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 319af49f-fab7-3442-9d39-3c4392d16ba0 | -2.79843 | -47.42135 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18323c9f-3cd8-3509-9aab-e361671096da | -1.99907 | -54.51217 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a19b714-a14c-3c73-8b69-c2ff93ddc281 | -6.9332 | -43.51411 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 87b8e303-2b02-387f-80ac-3eba6414f800 | -6.09468 | -44.76421 | 2024-12-13 04:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a759e16-d523-3cd2-ac1b-f27b63aee6d3 | -1.82663 | -53.15607 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5747dc3f-fdbd-3145-9a97-e3c4b3c3973a | -2.71855 | -47.56137 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afc3125b-71bd-338d-b211-a937f126bab9 | -4.51629 | -47.9382 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a60b47b-ccec-340c-998a-eb528536f652 | -3.66867 | -39.57991 | 2024-12-13 04:42:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ab42814e-c350-377f-91ee-1527ddd1dab3 | -1.69077 | -52.78414 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 553e6246-846a-3b81-94a7-8e1084856f17 | -6.76925 | -44.82909 | 2024-12-13 04:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83397840-fbb6-3b02-9183-285fae42af2a | -1.69499 | -52.78064 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 026752c5-ffcb-3fd3-82cf-d6b1c6d26d72 | -2.27264 | -47.90738 | 2024-12-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3870ccc9-a6a5-37ef-afe4-89bd88b07d22 | -2.86719 | -46.74488 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9eb3b92-c49b-3376-93e6-8f28f0793f0b | -6.13343 | -43.95842 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6604ab26-adce-324d-b738-5aea007439ce | -2.23021 | -53.70695 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c91d88b3-705b-330c-acb4-ab1a9e0928cb | -5.23677 | -45.13434 | 2024-12-13 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d652a217-cfcf-3487-8454-ce2f8bb7cbe7 | -2.27273 | -53.68942 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 352be604-3ede-3359-a521-8cdd25151904 | -5.20512 | -43.29661 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 314f54fe-a8c9-30ec-86b7-4f96240973c0 | -2.50485 | -51.8029 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85a526fb-fbc4-31c2-ad6c-884d37ae4471 | -1.58834 | -54.31945 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e33f514-c8fa-3c36-aee2-5263b68ecb94 | -2.71216 | -47.55646 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d94b65c0-7c19-3fdc-b7f9-78cdb55dbfac | -4.16666 | -42.44739 | 2024-12-13 04:42:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| d870783d-cb17-3f58-ae45-0bd8541439b3 | -2.3815 | -53.90336 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16c23cd0-7904-3cbe-9925-fee472e6f4c5 | -1.25526 | -52.17189 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66c4f940-51df-37b3-ac0f-c6630eb10565 | -1.24538 | -52.16638 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3459a89-bb1c-3017-b532-3f7bae017ca6 | -4.54987 | -48.00632 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbea621a-f314-34f6-b287-76cd8f763186 | -3.02418 | -47.78312 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7122ae88-5edd-30c9-8eea-e04d1d5558c7 | -2.50028 | -51.8097 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 327d09f8-ca84-3312-b8ef-e9450f63b7af | -2.23395 | -53.70753 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bcf4bb6-681f-382f-be04-ccc5854ffb96 | -6.92292 | -43.51797 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e6e0c0ad-dd61-3260-91b2-3de4bcd90ffd | -1.46456 | -46.8102 | 2024-12-13 04:42:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6da0f305-4ff2-361f-a2de-e7eff19f134a | -2.39247 | -47.02933 | 2024-12-13 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fad5db3b-8eea-31a7-8395-005b5372064c | -6.92514 | -43.50254 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0a1b477d-4ea4-3e52-85f0-622ee8c18986 | -4.04857 | -46.67292 | 2024-12-13 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52789467-14be-329c-8698-da5c5810565a | -3.00714 | -48.02822 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f33595f1-46fe-3d59-b2ab-0d2b89bfb82c | -4.87984 | -44.40446 | 2024-12-13 04:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84aa7a45-fa93-324d-a53e-9042cd152383 | -4.51844 | -42.07533 | 2024-12-13 04:42:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dbed8c65-897e-39cf-a202-0db329f528ed | -3.35696 | -42.30947 | 2024-12-13 04:42:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ce1c7d4-5ebd-37a0-9d6b-b6f5ecbfbd2d | -1.99825 | -54.51713 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de8d1de8-e354-3bc9-afd1-1bb41bc7842c | -2.2364 | -53.72462 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a8e9a921-1d57-3a09-8d17-5d03e7538ef1 | -1.68725 | -53.85775 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81a0be77-7686-36d0-8d72-a0eabcf232e5 | -2.2274 | -53.72483 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 782ba0f6-5948-3cf1-a895-f53e12352a0f | -6.91998 | -43.53841 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7ce3eb67-efa0-38f0-b3ba-a8f2ff9fbbce | -1.91213 | -52.85041 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee26be15-f9ba-382c-b85d-3be9db219c73 | -2.49803 | -51.80182 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bebb3f8-f8ed-3a8f-bb3b-b5b9842ea97a | -2.45615 | -53.70923 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71b50227-2352-326a-8295-db0ee9b0f015 | -2.46889 | -53.72488 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 208594b2-fd5c-3ca4-b0c4-f77065ddb5c8 | -1.92083 | -54.4012 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e8ce7ee-52df-3ac4-897b-9f5d8a4183b9 | -3.66602 | -49.86746 | 2024-12-13 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9c3e554-0171-3cb1-9cc8-15c0f1d9e7d2 | -2.45898 | -53.68016 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5336de24-e875-31f7-bf55-0d19b1ed8b03 | -2.45411 | -53.71127 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b0587711-d57d-3ce9-88db-47bcf71999ef | -1.91112 | -52.83354 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 298b5af2-02fe-3bc2-856e-913e4c45fa57 | -2.49865 | -47.69373 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1905b846-a257-3d5d-a2d0-9f59d64ecf58 | -4.7318 | -46.50515 | 2024-12-13 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96898acd-f91c-3ec8-ada2-f3e276e35167 | -2.23488 | -53.72602 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 002ac13b-b435-394a-bde0-f3918be7f6b8 | -6.39785 | -44.04234 | 2024-12-13 04:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5389ee21-3f1f-3bac-bae2-27e9ad503ed7 | -3.13802 | -53.29027 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3179c425-85a4-3c29-947d-ab76f1240c0e | -3.30087 | -43.5386 | 2024-12-13 04:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3a301b9-a6e2-38fe-848a-20e6517deaa3 | -2.23185 | -53.72094 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 53d31614-c9bf-34fd-b770-beaed20e8576 | -6.09958 | -44.76086 | 2024-12-13 04:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52cbd759-f5b8-3577-91d6-6bf9669a365f | -2.00298 | -54.51289 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c5af2e8-6c4a-3e64-9f03-e1a600c03d6c | -2.46157 | -53.71239 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3164a1eb-a299-3494-8d44-f0a0b12558a7 | -2.49122 | -51.80075 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 634a6558-11b8-3024-a93b-1fd4530f828c | -2.35432 | -53.88007 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c2d3b88-134b-3387-8a0c-334dcfc7b14f | -2.44292 | -53.63717 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c31f9e8a-248c-3e9e-a977-95b4ff76c8e6 | -5.08134 | -42.56561 | 2024-12-13 04:42:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a22e83e2-f4cb-3169-a96f-62bc8689316d | -5.96183 | -43.36983 | 2024-12-13 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e0a0a09d-0f95-35e7-b4d6-7fd20c30ee07 | -1.73417 | -52.02468 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 208f9d68-a647-3b29-abda-3c41e1460527 | -6.3196 | -44.76226 | 2024-12-13 04:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79346413-4565-3f1a-a0aa-84b05c1ca1b2 | -6.30538 | -43.46764 | 2024-12-13 04:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README26.md)
