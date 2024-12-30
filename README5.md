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
| 21a572d2-33f5-380c-8f54-e4f80818c4a9 | -13.71235 | -41.78622 | 2024-12-30 12:33:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0281a7f4-e22e-3726-8cf2-ac552bd70ef7 | -11.19767 | -40.31006 | 2024-12-30 12:33:00 | TERRA_M-T | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| a97dda34-400d-389b-aee9-ae6410dd8121 | -15.01486 | -39.43275 | 2024-12-30 12:33:00 | TERRA_M-T | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| ce6efb66-b158-3f2c-8d2d-db97c0a423d3 | -9.70335 | -46.23662 | 2024-12-30 12:33:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4d8ccb06-f829-3210-8670-871d00142dc0 | -11.11114 | -45.29266 | 2024-12-30 12:33:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 22365d9b-a672-3956-8925-65a49f3ff1a7 | -10.40046 | -40.59654 | 2024-12-30 12:33:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| e8463aee-cbf6-34db-9760-2ffa976cd825 | -13.71329 | -41.79602 | 2024-12-30 12:33:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 35c67603-e5f3-3640-ab5e-32bd2b331880 | -12.65257 | -40.24864 | 2024-12-30 12:33:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 75.5 |
| d4200883-7142-3ee3-8137-f782a3d913f8 | -15.00724 | -39.41175 | 2024-12-30 12:33:00 | TERRA_M-T | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 655e913d-25af-3142-92ef-05140c37d050 | -15.0045 | -39.43749 | 2024-12-30 12:33:00 | TERRA_M-T | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 53.4 |
| 7443b787-a00e-3fc5-8349-4b5e7e3610b7 | -9.70206 | -46.24552 | 2024-12-30 12:33:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 05ad7e8d-6423-3d86-b260-7b8276daada1 | -12.65495 | -40.22841 | 2024-12-30 12:33:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 9d11aae7-a4f0-34d6-9c4d-a1b42c11c5a1 | -11.10984 | -45.30185 | 2024-12-30 12:33:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 90a90b9a-4a8e-38a7-bc97-fe6536e2874e | -19.10167 | -50.86509 | 2024-12-30 12:36:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5bea0192-5e41-362f-a5b8-6eb16c7bd6d7 | -18.40073 | -49.62556 | 2024-12-30 12:36:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 52a3841f-0c28-35c3-8dc3-529ef28b8f25 | -16.95832 | -57.4313 | 2024-12-30 12:36:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.2 |
| b3921132-343b-3b3a-a0d7-6032b4bf89c3 | -20.48474 | -50.23949 | 2024-12-30 12:38:00 | TERRA_M-T | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 76e044f0-a165-32de-8968-871f2ac4a3dc | -20.14895 | -48.16483 | 2024-12-30 12:38:00 | TERRA_M-T | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c3132118-7b2d-332f-aece-116e538749af | -22.32949 | -45.56872 | 2024-12-30 12:38:00 | TERRA_M-T | PIRANGUINHO | MINAS GERAIS | Brasil | 3151008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 52a1c793-2267-3e97-ac8b-0583419d64ec | -23.11368 | -47.00723 | 2024-12-30 12:38:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 8980482d-987d-3675-9577-bcedb921f1ca | -22.47334 | -47.53317 | 2024-12-30 12:38:00 | TERRA_M-T | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 46b89c05-09be-3825-a557-17a800af94dc | -22.48608 | -47.5757 | 2024-12-30 12:38:00 | TERRA_M-T | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 31ec4cbe-9f41-36de-aa77-5d320b3de336 | -22.10662 | -46.50206 | 2024-12-30 12:38:00 | TERRA_M-T | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 15d8f808-0d6b-3101-b405-2aeb14df5862 | -26.82447 | -51.47029 | 2024-12-30 12:38:00 | TERRA_M-T | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| bb19c5e4-d9df-3f16-850a-1509b3b0e607 | -22.07792 | -46.57455 | 2024-12-30 12:38:00 | TERRA_M-T | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 13b1f108-17d9-3e0e-8795-fd5772f7ff21 | -22.29088 | -46.61338 | 2024-12-30 12:38:00 | TERRA_M-T | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| aec0b212-6ebe-38b4-9583-c6146a839bbf | -22.63753 | -46.9911 | 2024-12-30 12:38:00 | TERRA_M-T | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 472caf0a-57de-342b-9726-7dfe68624e0c | -21.36935 | -46.51979 | 2024-12-30 12:38:00 | TERRA_M-T | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c3da52f1-ad3c-39cb-9c7c-2921cef69091 | -26.82289 | -51.48055 | 2024-12-30 12:38:00 | TERRA_M-T | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| d91887e4-d43f-3376-b04d-d8e674e931bd | -29.21445 | -51.17089 | 2024-12-30 12:40:00 | TERRA_M-T | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |


