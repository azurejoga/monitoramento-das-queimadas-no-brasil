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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc94b122-28ea-38e9-81bd-a873e5c7826a | -16.20066 | -43.68354 | 2025-10-17 03:32:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c8b7c7c-b9d2-3e2f-9d58-35a30bdea64d | -15.91791 | -43.52723 | 2025-10-17 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1de74537-b548-3a6b-bf7d-30b3e5939ebf | -15.78431 | -43.64951 | 2025-10-17 03:32:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ec69986-8bf2-3cba-a4f4-8eed546947f6 | -20.0322 | -44.07965 | 2025-10-17 03:32:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 820cf887-936a-303c-981f-e4a11f4c41d9 | -16.01605 | -43.4969 | 2025-10-17 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49cf33f6-fbb4-3f5f-afca-8b697a707826 | -19.21692 | -44.12094 | 2025-10-17 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6172017-5f60-36c4-9f2c-6e3916f76eda | -15.78964 | -43.65077 | 2025-10-17 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a2921c-28f2-3f34-a851-e553e637351d | -16.39856 | -41.96094 | 2025-10-17 03:32:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dd9590b0-92fa-3feb-8b84-5a3450b455ee | -15.78361 | -43.65295 | 2025-10-17 03:32:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0cffbae-44d6-3e94-b4c9-a36f1f7eca43 | -18.15933 | -45.30335 | 2025-10-17 03:32:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bc214ea-b991-3c18-bcf8-4b959a1c7543 | -16.54686 | -41.65215 | 2025-10-17 03:32:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bc5cb500-3274-3c15-9fbf-54365ab95514 | -16.81298 | -41.22636 | 2025-10-17 03:32:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43dd99ff-0fe5-3db2-85fd-0f2967644fbf | -16.61301 | -43.36828 | 2025-10-17 03:32:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ea61fb3-f72c-3ff3-a251-6daa3c329b85 | -18.08764 | -42.45456 | 2025-10-17 03:32:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 64e2f087-5719-371d-a2bd-6c7022022064 | -14.71369 | -48.30513 | 2025-10-17 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a72a7e6f-f4d3-3c56-b9a0-b66e20b8578a | -19.2156 | -44.12293 | 2025-10-17 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4329650d-f241-36dc-ba27-d4e6cbee3fb4 | -19.21628 | -44.11964 | 2025-10-17 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b636b26e-766a-3438-bdfe-173468b02fa2 | -16.61234 | -43.37156 | 2025-10-17 03:32:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ef2c21a-4a0a-3be9-8532-efed646758e0 | -19.91171 | -45.89101 | 2025-10-17 03:32:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b32756d-7830-3978-b88b-8aae41ebc837 | -14.7204 | -48.30875 | 2025-10-17 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15c324b9-cfe9-3314-9131-2cca1b7745b8 | -18.08877 | -42.44888 | 2025-10-17 03:32:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 438c0124-0e6b-3f89-95bc-11681a651ff4 | -16.35309 | -43.41719 | 2025-10-17 03:32:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a81fb54-0de4-3fe3-bd70-be3e357fd467 | -16.34139 | -46.40663 | 2025-10-17 03:32:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4747bb0-fb0f-33bc-9ec4-c5ccd17f9d88 | -16.39775 | -41.96411 | 2025-10-17 03:32:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bf17162f-105c-3649-92f6-6e6e9cc4b7e0 | -20.51893 | -43.20003 | 2025-10-17 03:32:00 | NOAA-20 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b9e1d55-b4a2-3a28-b4c1-185dde9ee1ad | -16.02133 | -43.49804 | 2025-10-17 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d688542-cd14-3912-8b08-b8ad88f59552 | -16.20124 | -43.68073 | 2025-10-17 03:32:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b83e876-7c98-3508-b2de-6056822c96d3 | -23.33034 | -46.93249 | 2025-10-17 03:34:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8e6f320-81ec-3550-8e96-a7ecd881b051 | -23.32939 | -46.93654 | 2025-10-17 03:34:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d67086e5-fa8b-380c-8b88-9ac7cdd19f23 | -14.3227 | -51.4475 | 2025-10-17 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 44c2c731-653a-3787-9801-28a1b4e02e22 | -12.4455 | -51.3004 | 2025-10-17 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0f1e52aa-1543-3a63-8c7c-706dd67a6e43 | -10.4941 | -43.4315 | 2025-10-17 03:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 09de343d-8a14-3506-864f-768351d976ec | -10.3126 | -44.043 | 2025-10-17 03:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| fcebf63a-d8d3-3cb8-8626-96209ae97752 | -12.4264 | -51.3027 | 2025-10-17 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 42338a38-2586-304e-af7c-69a096c9a0a9 | -12.426 | -51.324 | 2025-10-17 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 9c384176-c3e7-32f0-a640-e27bd6455c6f | -14.3417 | -51.4663 | 2025-10-17 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 291b60e7-e5b5-38c1-8e65-e5a2f0e17c56 | -4.4248 | -43.3805 | 2025-10-17 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 13ff435f-dc29-335c-b9b9-ab467772644d | -9.1567 | -46.6241 | 2025-10-17 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f8a90d18-55be-3c42-b1aa-244326cb230f | -9.1564 | -46.6465 | 2025-10-17 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| ad2b288f-e60f-3b0f-a0d9-67e6bba4782f | -11.4168 | -44.2139 | 2025-10-17 03:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ee9c13e3-5962-36ba-b21f-19f3905b8a76 | -4.4246 | -43.4038 | 2025-10-17 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e49d8331-d37a-320a-b9f3-10c077e89eee | -14.3219 | -51.4904 | 2025-10-17 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 67cd9497-ec01-3a6e-a2a4-3f8b33ccb65d | -11.398 | -44.1933 | 2025-10-17 03:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 3b229740-e3a7-32be-80c5-c043f481c6e0 | -10.5132 | -43.4289 | 2025-10-17 03:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 0518a3d5-2dc1-3ee2-bfd0-1cc6711970a8 | -14.3223 | -51.4689 | 2025-10-17 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| deae588a-dab3-35cf-864e-678af2ca65c4 | -11.3976 | -44.2167 | 2025-10-17 03:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 1078c71d-b64d-3648-abc6-a8be3c507920 | -10.2939 | -44.0221 | 2025-10-17 03:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 22fe654a-e174-36f4-bf37-6676c4ad9329 | -4.4059 | -43.4049 | 2025-10-17 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| b73b4c45-b849-3221-92d3-cb7689fcffc6 | -10.2748 | -44.0247 | 2025-10-17 03:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b1a7f8ce-2963-3501-857c-ed2781b21aaf | -10.534 | -49.5471 | 2025-10-17 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 45c7c307-887c-3055-be26-c3a4387a21a8 | -12.4451 | -51.3217 | 2025-10-17 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| c5b8a412-a10d-3e55-880e-675cb8634abf | -2.7401 | -49.3927 | 2025-10-17 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| eb161394-5512-3972-9fe7-25b7d8661a19 | -10.2745 | -44.0481 | 2025-10-17 03:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d72cdc44-f7d5-3a8f-a963-f7ad9ec71478 | -9.1378 | -46.6261 | 2025-10-17 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 6eee85d5-8b1e-3ba7-928c-8de5ac21188e | -4.4061 | -43.3816 | 2025-10-17 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 5f2dc1d3-c1b9-31a1-9265-b7cfb6d0c5f5 | -11.4581 | -44.0439 | 2025-10-17 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0d85cb8c-a179-3eec-9452-f4095ce874a2 | -11.4172 | -44.1904 | 2025-10-17 03:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 30d5dc29-af24-333b-a6b0-400154383d92 | -9.1375 | -46.6485 | 2025-10-17 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 387.8 |
| 83b6bedf-1630-3bd1-a89d-e45073682cec | -3.236 | -45.9639 | 2025-10-17 03:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 24f5d7c0-eabb-32f7-af14-ea2b9af489d3 | -11.3972 | -44.2401 | 2025-10-17 03:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2822caa6-32fc-365f-89c7-7b7d9d824f72 | -10.5136 | -43.4052 | 2025-10-17 03:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 19fd1617-ff03-3527-bd3f-1f3be3e0378c | -14.342 | -51.4449 | 2025-10-17 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 54616b82-5f69-3721-a0fb-1562a537195f | -10.5337 | -49.5687 | 2025-10-17 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 2798a8dd-9366-386b-8f21-a46bb5d27cb1 | -10.2935 | -44.0455 | 2025-10-17 03:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 321.0 |
| b1c2e642-0900-3377-bc37-2b8804352277 | -12.4455 | -51.3004 | 2025-10-17 03:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 184.3 |
| d7eea63c-92a2-3ff8-b7eb-9d05d99c98b2 | -10.5136 | -43.4052 | 2025-10-17 03:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 9f9f93b6-12bc-3d05-b171-1f003872ab4c | -10.2939 | -44.0221 | 2025-10-17 03:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 184.0 |
| fa8db841-e96f-3d32-bbcf-3ea1cd2e3eab | -10.3126 | -44.043 | 2025-10-17 03:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5415d154-c566-3ece-b92a-6b89b9e4e56d | -12.4264 | -51.3027 | 2025-10-17 03:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| b390deda-bbc6-39d6-9d5c-5be352545231 | -11.3976 | -44.2167 | 2025-10-17 03:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 940e0e34-83d9-349a-b54d-ea904c29db49 | -3.5028 | -52.4938 | 2025-10-17 03:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a72ae487-7822-388e-bf34-4b0e36aa815a | -10.2935 | -44.0455 | 2025-10-17 03:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 282.0 |
| f2cc336c-24ad-37ee-b37e-b6724a34e386 | -12.426 | -51.324 | 2025-10-17 03:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 5448287e-6b4f-3c2d-b42e-61cd5ff8567c | -10.4941 | -43.4315 | 2025-10-17 03:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 538b3dd2-c231-38db-9dd9-f18d9c417671 | -11.4168 | -44.2139 | 2025-10-17 03:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| e79e4ccb-98c2-30f0-9d49-36a4ee084f38 | -10.2745 | -44.0481 | 2025-10-17 03:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6fca615e-82c5-30be-97ca-c490b197a459 | -9.1567 | -46.6241 | 2025-10-17 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| fd7a7348-72d8-371e-85b9-3f60ddb67660 | -9.1564 | -46.6465 | 2025-10-17 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a0830027-a3f0-3e1e-8d22-180974120b3a | -11.398 | -44.1933 | 2025-10-17 03:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f07ef528-fd6d-32ca-a583-7dff37b8da85 | 1.7668 | -55.7439 | 2025-10-17 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 6f032470-7667-3304-8ea7-4b42e12dc274 | -12.4451 | -51.3217 | 2025-10-17 03:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 199.6 |
| a1df6686-9039-37a7-8664-de0b55534e10 | -2.7401 | -49.3927 | 2025-10-17 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 35c54193-b2fa-35ff-97b2-a82dc48c7d03 | -10.5132 | -43.4289 | 2025-10-17 03:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8d138722-9f3a-3d0e-a3d7-649de643a6e1 | -12.7866 | -44.8873 | 2025-10-17 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 21722f73-b0b2-3fb5-93d4-424acb102038 | -9.1375 | -46.6485 | 2025-10-17 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 205.1 |
| feafc8ee-bf6c-3d5e-b22f-7e79d89a8e3a | -10.2748 | -44.0247 | 2025-10-17 03:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6f3a5c4e-a572-3132-975b-8f98de18f54b | -9.1378 | -46.6261 | 2025-10-17 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 601dd8aa-27bd-3696-aec3-bc8e397cf6ba | -10.534 | -49.5471 | 2025-10-17 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e54c6a58-5091-3530-abec-8ff0c0bfbb08 | -11.3972 | -44.2401 | 2025-10-17 03:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 18b336cd-8cb4-3f16-bb61-e7493693bf3f | -10.2935 | -44.0455 | 2025-10-17 04:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 90d68be6-0698-3f2b-9e7e-a834fc3e0362 | -12.4451 | -51.3217 | 2025-10-17 04:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| a12745c1-8a83-3007-b1c0-3b715926065b | -10.4941 | -43.4315 | 2025-10-17 04:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 75115074-3bfd-3109-bd14-04661b28f625 | -10.5132 | -43.4289 | 2025-10-17 04:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| f50d69e2-e139-3a26-9f83-a632f60eee46 | -12.7673 | -44.8904 | 2025-10-17 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 7cb9b402-2bbf-31d8-9e24-b79e2b673b13 | -10.9472 | -49.782 | 2025-10-17 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cc17f044-938b-3d1e-968f-aa0c33a88633 | -12.426 | -51.324 | 2025-10-17 04:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ef11d1bd-971f-3587-8d7f-f87da9bb7005 | -12.4455 | -51.3004 | 2025-10-17 04:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 1aace208-78f0-37e5-aa56-0c6def1e000d | -9.1375 | -46.6485 | 2025-10-17 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 96316413-b837-3b6c-932c-921213abe084 | -12.7866 | -44.8873 | 2025-10-17 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 611d529a-009a-377b-b9a8-f2b9f0670e9b | -10.3126 | -44.043 | 2025-10-17 04:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |


[Clique aqui para ver as próximas entradas](README34.md)
