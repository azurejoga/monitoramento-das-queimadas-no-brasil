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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49475ab6-0b2b-3f7e-bd70-4a343ab342b1 | -7.13163 | -47.12713 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e7c2206-799c-31d9-b8cf-702ff85c432b | -3.40249 | -50.187 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6bf4de0-770b-3048-b7d5-a8405166d8e9 | -4.57468 | -50.94063 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 607a02ca-cebe-31bb-b03d-e423bd327373 | -3.01262 | -51.34089 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dccb7ae8-230b-3827-8665-658b0bf8bf92 | -5.35638 | -44.86112 | 2025-11-17 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba3ae4f0-8857-356b-943c-86fd2d57694c | -3.3117 | -53.85679 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ec45814-3486-39f0-9cd1-d66d9aec32ed | -3.23115 | -50.50809 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4905cc3b-9f6e-3b7a-bc56-d933092dcade | -3.28665 | -51.43373 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc4f767f-e3b8-3fdb-99a5-6fba24b5f59a | -9.71825 | -43.95919 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7bc8f56b-0ffe-3974-841c-2749a3759505 | -3.16447 | -50.16457 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d37dc19-ae1a-315b-bc45-d88b7dc37b7e | -3.33406 | -50.27755 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 252216b1-8b22-3643-bbc3-e1c9f15c3b03 | -7.09641 | -42.72923 | 2025-11-17 05:08:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f86f135e-3740-3c34-86c7-7649a30ad6e4 | -4.99539 | -44.35968 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 99bd65ba-6dfa-357d-8e44-2c0b06cccc69 | -4.69743 | -46.31598 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1794e26-55d6-31ec-8593-236372ea3de5 | -3.83677 | -49.80905 | 2025-11-17 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 577fff98-49f3-31b8-ae24-5b660f2fce48 | -4.72043 | -46.38118 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 994ec0ea-aa08-305d-9733-ab309c7f55e6 | -5.41094 | -44.06699 | 2025-11-17 05:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d8f5ecb-addc-3abc-8489-ed6e3c37fd73 | -10.65737 | -48.16514 | 2025-11-17 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a711cf95-053f-3722-8356-4fe6eb985be2 | -4.39462 | -49.65565 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44da20c8-cba9-3ee2-bc09-2ddac1939511 | -4.38691 | -54.83091 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf2f27c3-8c8f-3c8e-b121-3c2be44073bb | -6.48711 | -47.53884 | 2025-11-17 05:08:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6678f1ba-3a4b-3b29-9db3-2ba082585dc6 | -4.72092 | -46.3779 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53fb68a9-f007-3a60-b65e-3fd10bae4ffb | -9.5185 | -47.27048 | 2025-11-17 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8b0a160-23b5-34d4-b7b7-654eaae127d1 | -3.7778 | -47.74607 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 354a4141-e1c7-3db9-b785-dcd662df6746 | -5.83467 | -48.83144 | 2025-11-17 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0beae27-9589-35df-a96f-6021e0307ed1 | -3.08301 | -51.25616 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d4f3ca9-a1c9-331a-898c-5c4c5734e0fd | -4.40285 | -45.83527 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0c7b59a-b931-36e4-88d1-1fde32c5dea0 | -5.33769 | -43.02933 | 2025-11-17 05:08:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| df8624ae-0f6c-3808-8047-fb6014615a84 | -2.88314 | -51.43085 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b1423d9-d6de-34db-9f76-da273972e8de | -2.94455 | -51.76272 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9c60e5b-b06f-3521-ac14-556e2d63699b | -11.40903 | -43.33135 | 2025-11-17 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9965aff4-b7e4-3262-bbb0-01b8d9b29258 | -6.39891 | -42.28657 | 2025-11-17 05:08:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 4cc3f8b4-b534-33be-8c7b-cb48c0e0c143 | -3.23618 | -50.49523 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 65f0cb0b-18b3-30aa-8609-ff52d64e079f | -9.57962 | -49.11821 | 2025-11-17 05:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d6c362c1-a336-30c1-8deb-56728b2840bb | -3.76454 | -51.85668 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2a12bc0-a688-3a94-b3eb-859fe082765c | -3.4227 | -50.37726 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b3663a6-342f-3e8a-8c8d-60b1935db761 | -4.99605 | -44.35494 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5baab530-c421-357a-a1ee-4298766100b2 | -3.30609 | -53.84864 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f823bb28-893f-3682-beef-58a4fa6ff7fe | -4.65484 | -46.89916 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f517bc2-6f99-34c5-8559-d7bb18371851 | -4.05864 | -47.49543 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4ec9cb7-d992-321e-ac38-48d93ee2fb94 | -11.19813 | -46.62442 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb245555-1b28-34d2-81c8-fe7557e6ae8c | -3.82456 | -51.19693 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e9fa8d-5483-373d-8938-09154d673aee | -3.43455 | -52.88892 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 016fe508-f5cb-3345-adf4-f754c0c73f5b | -3.32849 | -50.20695 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b82cba5-7c66-3dcc-b232-b4beb83b8475 | -9.72141 | -43.95895 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa9923e1-fe99-30e4-b31d-7f93595ed892 | -4.99582 | -44.35832 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2e13708-be24-3f93-8965-e40d7a5cd3c2 | -3.23861 | -50.50589 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fcf6b353-6511-3691-9fcb-5eeb4484cf9c | -4.12909 | -47.29285 | 2025-11-17 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99ef82c2-e796-3561-a249-d2e7a0d4331e | -3.57527 | -52.09432 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64e95676-31c0-3a50-84a2-4a77eaf171b6 | -2.99773 | -51.00826 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2a9963c-c8f3-3f90-9a05-e544a61ef4f2 | -7.25666 | -48.00819 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01b2fd52-361b-372a-89d1-d79fde3e5913 | -9.06802 | -44.79214 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e33dffe-14d4-3559-bc34-7b074ceef2f4 | -6.12606 | -41.81338 | 2025-11-17 05:08:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e68d3249-0b81-3508-be1e-f9e276fb8f54 | -6.68796 | -42.0423 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a5581464-a7ff-3832-a744-47283ffe74c8 | -3.08371 | -51.25168 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ae82b30-537a-3ac6-831d-d7918bb854d3 | -2.94092 | -51.76211 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c40f44b9-b161-3247-8879-8925c99867b1 | -10.65377 | -48.16478 | 2025-11-17 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00f6b5c6-50aa-3431-b8a7-0ff57ab2ef77 | -3.23745 | -50.49362 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92fa76e9-794b-3e5e-ad12-c80aa4bae556 | -3.0801 | -52.92096 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cffacf04-ef19-3ba8-97d5-9f90a2c69871 | -4.61324 | -50.66622 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f3f86ca-9ec2-382e-be66-e7cf8c584430 | -3.29859 | -50.07741 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfb23071-4a57-3b17-96f9-fefc6a18f5b2 | -3.23149 | -50.49971 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 77521217-dbf8-33f7-9807-3af0d576f350 | -3.2398 | -50.50426 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34720952-ac6e-3066-8929-9f1ad8483930 | -6.68316 | -47.38829 | 2025-11-17 05:08:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0a1f6eb-f64f-3a80-bd25-c090e965ae46 | -4.46541 | -54.97816 | 2025-11-17 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f979633c-3f66-3ffd-a9b7-467969c652b5 | -3.43987 | -50.10312 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3a41647-6500-30ee-a941-63fab997720a | -3.30313 | -50.07488 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34008877-6182-341c-8944-0c37212a41e6 | -7.65825 | -45.35424 | 2025-11-17 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5adc70f-bb43-3a0e-bdd3-f78cf0498aa4 | -5.00148 | -44.36068 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e08c477a-c57c-3c51-8dac-c2a4a4e2c156 | -3.74679 | -47.59515 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdf33e5b-ce40-3f9b-9327-7eb51183712d | -4.60928 | -50.66562 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a18aa526-89ad-303e-83c3-4b1d768462ff | -4.69256 | -46.31197 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c828af83-0adc-3fbd-bc7d-ae0b1d0cae62 | -3.33485 | -50.27239 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6df9c7fa-0ec7-3585-911f-0fbd43940fcf | -4.69208 | -46.31523 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d538c73-344c-3f8f-a65c-f64b5cf1d9a8 | -9.15181 | -48.06217 | 2025-11-17 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51899d7c-cd22-3c31-952f-c7ea40284306 | -5.88456 | -43.98062 | 2025-11-17 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc27b1fa-5069-3990-872d-f742f794ba46 | -3.39795 | -50.18989 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a1a25d1-837b-3491-8fd7-d032ffa00f93 | -3.75055 | -50.42698 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6e6f2c1-6fb4-34e4-bc98-8bf2c84e412a | -6.89962 | -52.19423 | 2025-11-17 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| befbfadc-1f95-38c8-b53d-ffac8226e90a | -7.13642 | -47.13111 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dc7c05a-8510-3801-8c99-bb62c82cd0c7 | -2.91128 | -54.16239 | 2025-11-17 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d67d64a-421c-3602-95c7-73c934253bfc | -4.66162 | -46.74112 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 01848a16-1099-35e5-8c03-6acd19f087ac | -3.23823 | -50.48863 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8b4253c-16bd-32fc-8832-ef0d891eea28 | -11.05077 | -47.60961 | 2025-11-17 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 841755d0-76e4-38c9-b87c-750ce5b9dc24 | -3.14668 | -51.31858 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8593d4f5-2606-3d92-be46-b6444884da81 | -3.12864 | -50.28999 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 099b2464-544e-338a-8256-e1315f8a031c | -2.89044 | -53.29069 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 651dd162-cdea-38b9-9365-3b8de7fae100 | -7.36492 | -45.83114 | 2025-11-17 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1878e7fd-479f-3f38-9f1f-56f76eb34a41 | -3.30368 | -50.07137 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30902b39-7591-3f96-b876-dc674d5cf043 | -3.13262 | -50.29059 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8011bbf-7631-369d-9c6e-1011d67cc452 | -10.65339 | -48.16779 | 2025-11-17 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95709099-bf2b-3b96-8e5e-397f8e9427e3 | -3.30258 | -50.07838 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70da8c18-6be0-3961-bd8f-f9cfc74d64d4 | -8.88408 | -44.77961 | 2025-11-17 05:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8616981f-4397-3609-9a31-070c436d1ec0 | -7.95516 | -46.84446 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dcfb556f-71b6-3fa4-b9d3-17a244128716 | -3.51456 | -50.31978 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc4f601-e130-39b8-96bb-dfe74cf78fdc | -3.27787 | -51.26838 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f6feb4d-85cf-3f0f-acd1-7fb4cad89548 | -3.30668 | -50.07863 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09981839-95d3-3516-a51e-3c5ddf623d17 | -4.70918 | -45.10379 | 2025-11-17 05:08:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22e57922-fda2-356a-85bb-2210350c5505 | -10.92169 | -48.69261 | 2025-11-17 05:08:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c3f4e35-3d98-3f5d-a0e2-fa734738a744 | -11.15838 | -44.0425 | 2025-11-17 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README46.md)
