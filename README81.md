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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87d97147-0059-3933-a500-51b33cb218a4 | -3.74464 | -52.31403 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b1fb848-c51e-340f-89c8-59d18765ebb1 | -3.74357 | -52.31374 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7182a9ba-ba6c-3257-97fc-c1343667d56f | -6.09484 | -52.8286 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d14f7183-0f8c-3fe1-840c-f9886b7f1f4c | -6.09425 | -52.83198 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad1b8ea0-41e9-3350-aa76-92da591d9ed0 | -5.86303 | -53.56441 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb48fa48-6dad-354b-807b-0eec7026f3b4 | -5.86232 | -53.56846 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16b76086-1cc2-35c5-81b5-b15f97d0556b | -1.13484 | -54.10463 | 2024-10-09 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efcfd833-55e4-35cc-ae5b-2b64163f3453 | -1.26364 | -54.21508 | 2024-10-09 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 335485b5-5bf7-3b80-955a-8fa59690c79d | -1.20258 | -54.22243 | 2024-10-09 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69479fd1-032e-387e-b54b-44c47fd9bc49 | -1.19604 | -54.22141 | 2024-10-09 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1fd05be-7c69-3d6c-a440-cad2651a745f | -1.16909 | -54.14071 | 2024-10-09 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 636c29c1-dde2-3b1b-beea-9e0f2a22ba62 | -1.16876 | -54.14174 | 2024-10-09 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 062c4282-5518-382e-9f3b-39468f2166bc | -1.13397 | -54.10994 | 2024-10-09 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 847c0fa7-53d3-31d4-b35b-808b16c344b2 | -2.23549 | -53.65637 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d77df0c-be99-3ec2-a06c-55c08832076d | -2.23452 | -53.65385 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e1de3b2-5c0a-3794-b15a-7b066c8c5a5f | -2.2337 | -53.65869 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c5c8bca-ad2c-3b39-a61a-433a3f790236 | -2.22931 | -53.65517 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6e3f2776-e5df-3ac6-b39f-ed46d77ed3e2 | -3.56589 | -54.34913 | 2024-10-09 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d4ea361-3a8e-3d24-b213-02f3f7d8d746 | -2.22851 | -53.66006 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94ebe6eb-63cb-3ebd-9a62-01090e585ebc | -2.22834 | -53.6527 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 970f1fb9-11dd-35ae-b7cf-5fab30064e30 | -2.22751 | -53.65757 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b49331c2-aba5-31d9-a6e2-c924bd6cdc94 | -1.1241 | -53.63806 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1027ef6e-6cfc-3f22-880f-37d21c0bfc4e | -1.12018 | -53.62241 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54afa0df-9388-3dce-b5c0-76d6d573bf8e | -1.11555 | -53.61119 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ccea2ecb-6bd7-34b4-a4f0-b148bfcc8c00 | -1.11477 | -53.61594 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 2028d800-a0fd-3523-8355-4ff82f6dc48a | -1.11405 | -53.62038 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| aa6270a5-9c8b-317c-9181-b70859b8fc27 | -1.11329 | -53.625 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8f8f1b40-417f-33b6-940b-16a2e5bd0ffb | -1.10847 | -53.61499 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 87ec80d0-0526-3fa8-9b12-a6d186434579 | -1.10769 | -53.61976 | 2024-10-09 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a65ffbbc-f769-3c85-ae09-3bf8c71cae8b | -1.03034 | -53.73397 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4a672c9-9e5c-3ded-934d-5cff7f5539a9 | -1.02859 | -53.72825 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad4e82a2-d797-39ee-96fd-fe8a5f0a8e9c | -1.02792 | -53.73241 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e182a679-9db3-3782-96b7-0bbe70dff55d | -1.02725 | -53.73656 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 780ef625-700a-39ae-aa6d-111b98ee53ad | -1.02474 | -53.72849 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1eac784d-ee13-3edb-aa10-618d328917a9 | -1.024 | -53.73293 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6555dfe1-50d6-3fb8-8664-f3248a4ddb0b | -1.02246 | -53.72589 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84ee0a37-6a82-3018-8008-a54b5e35e38b | -1.02169 | -53.73067 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba1b2c1c-d389-3447-86d2-0225e5713917 | -3.56769 | -54.33872 | 2024-10-09 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a75c8544-4bab-3f37-bd82-284af0426a73 | -3.56677 | -54.34406 | 2024-10-09 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40cded6b-1289-3b5b-bc26-a1e239222d6b | -3.56142 | -54.33719 | 2024-10-09 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ad1f3ed-089c-3507-a827-764e14c32b5d | -3.56049 | -54.34261 | 2024-10-09 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50d6f23b-2162-309d-ad73-56458fac00cc | -3.55958 | -54.34784 | 2024-10-09 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ede66ab9-fe63-3bb6-93d6-3cd9d240ebd0 | -3.54074 | -54.05905 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b20a8a34-4dbc-3a0c-b2cc-d0e822600f73 | -3.53897 | -54.05822 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31b17f7c-4e34-3f8b-9408-a3ae299b5f50 | -3.26001 | -54.18411 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7925dec7-11ec-381d-908a-518e73e1eab6 | -3.2592 | -54.18886 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ef61dea3-8f03-39ac-bc6e-520ed3968cc9 | -3.25836 | -54.1937 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0251ea83-ca8b-3c5f-9a5a-18fc32a01740 | -3.08626 | -54.53408 | 2024-10-09 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5408346-e3b3-30c1-92cf-4ccc1ee9c090 | -3.06518 | -54.77386 | 2024-10-09 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9115943d-0939-3c2f-873d-5394ab381cdc | -3.06424 | -54.77933 | 2024-10-09 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b790d24c-5c00-3bb9-bce1-7e67ef3f4d4e | -2.93654 | -54.82169 | 2024-10-09 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 594dcf28-7f5c-3a2f-81d8-ff4489103830 | -2.93336 | -54.17862 | 2024-10-09 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 407c97ae-9185-3998-b544-dd5e6c6ea1a8 | -2.8762 | -53.96165 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aaafec68-3f24-3bd3-8bde-c6e65f4e7a5c | -2.86991 | -53.96071 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4470f35d-9d94-32fd-8e73-d8de1eead0a8 | -2.85365 | -53.94283 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91d32a26-7ab8-33a5-84dd-5fb06fd6eddd | -2.81493 | -54.36088 | 2024-10-09 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 63d97ff0-44ba-3f74-83c7-ed1418c7347a | -2.81406 | -54.366 | 2024-10-09 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1e48e4a2-07aa-3281-b6e6-36d7ed5aa24e | -2.74434 | -53.95587 | 2024-10-09 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b5c6754-99a3-39b9-ab30-6055d88d9193 | -3.1283 | -53.73905 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c952cfb-cf2b-398d-bb92-4e5838d8cff1 | -3.12296 | -53.73325 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a17ddd65-f669-3001-87ae-8a8a576d3754 | -3.12215 | -53.73802 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c8a20db-71ce-3cce-bf5d-6f7c75a3186d | -2.98085 | -53.71835 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 82322260-f9c7-30f1-a5ad-696ec1602666 | -2.98044 | -53.71806 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9a029bb2-5d90-3f88-b64a-e04f7497fa05 | -2.98009 | -53.72298 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 57d956d2-bcb0-3491-ac14-24142f1b2fb6 | -2.97964 | -53.72268 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ecaee021-e1e3-3944-896a-3e1ebcd67faa | -2.97471 | -53.71721 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4d5d3f46-35f4-36c9-99e6-3577ca477548 | -2.9743 | -53.71694 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 67a689ff-f0f5-3ba3-a5a9-52f6d4f6dac4 | -2.97393 | -53.72194 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 03a6962f-a068-37f5-a388-def97730afc1 | -2.97348 | -53.72166 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8bbb431a-1b07-35a8-a56a-30dcafb07c71 | -3.65597 | -54.29653 | 2024-10-09 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 259651a5-e99b-352d-bf9e-0f58a5202bb8 | -6.63763 | -55.38034 | 2024-10-09 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1ede9ba-58ce-353a-a739-9d08916f78ff | -1.24342 | -55.68988 | 2024-10-09 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50e3fd99-a188-3840-9326-3f82b8f8788e | -1.2407 | -55.68604 | 2024-10-09 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5560310e-3038-35ef-a0ff-9d06e81e556b | -1.23629 | -55.68884 | 2024-10-09 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f361d6b-1bb3-337c-94fd-72a5778dd009 | -1.11 | -53.6173 | 2024-10-09 04:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3108661f-6285-3ad4-b918-c995ffd6ce1e | -3.9023 | -46.4467 | 2024-10-09 04:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 64b12e8a-a4cc-3219-9482-f3eb61ce1d8e | -3.9208 | -46.4459 | 2024-10-09 04:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f900afba-dd9f-3a5c-9731-da0d850937b8 | -3.9394 | -46.445 | 2024-10-09 04:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 09433ecc-377a-314b-b0c6-fd825d5a2a46 | -6.7614 | -60.0559 | 2024-10-09 04:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| ebba5794-88e0-3560-ad8d-7ddb27bbb674 | -6.7615 | -60.0367 | 2024-10-09 04:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5087374a-941d-3793-abfa-a8c586a88f81 | -6.7798 | -60.0552 | 2024-10-09 04:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 82ca6ea5-61db-3376-b0b4-6a20072eb623 | -6.7799 | -60.036 | 2024-10-09 04:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| bf26f067-4152-3db5-b8c8-e63ee2a5256c | -8.4919 | -48.6476 | 2024-10-09 04:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 302857e9-0098-3403-b952-f2052491eab7 | -10.3655 | -64.8451 | 2024-10-09 04:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a0443080-de9c-30fb-938e-7f3654145ada | -10.3656 | -64.8262 | 2024-10-09 04:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f4266dde-f7bf-317a-92b3-76e59364ff6e | -10.3894 | -61.2502 | 2024-10-09 04:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b684ab30-2f2f-3e10-9253-fdca45d98801 | -10.4287 | -60.9979 | 2024-10-09 04:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4d642384-6c33-32dd-a2bd-9d7efac3b799 | -10.6068 | -55.9169 | 2024-10-09 04:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 6674fbed-2e39-3fcf-aa78-9d2f8b00efa0 | -10.6253 | -55.9355 | 2024-10-09 04:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| aa2dc7cc-a196-398f-bcbc-5f88f17d6d92 | -10.6256 | -55.9154 | 2024-10-09 04:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 86b0b819-c472-3b1c-800e-3f46f5744bb0 | -10.6258 | -55.8953 | 2024-10-09 04:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f05dfdfa-48b8-3dfe-95ea-ad5534a08b3e | -10.8754 | -63.9169 | 2024-10-09 04:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e15a2622-811a-3552-8973-4cfaf5663293 | -10.8755 | -63.8979 | 2024-10-09 04:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5b2c5a01-81e6-304c-b895-ae1130370587 | -11.2583 | -60.3885 | 2024-10-09 04:16:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8533f69a-d4f1-3485-a6e0-09c583bb69d6 | -11.693 | -65.0163 | 2024-10-09 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 109.6 |
| ec572dd6-3d46-3deb-8ad2-c0041ec1bf2d | -11.6931 | -64.9974 | 2024-10-09 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| f9f8d3de-0253-36e6-8e6d-2401de31d8b8 | -11.7117 | -65.0155 | 2024-10-09 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 2e3965e5-b2bb-3177-99f8-c63792c925ba | -11.7119 | -64.9966 | 2024-10-09 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 37e64e00-2dc0-33aa-bb95-8d4ee53f99f8 | -13.3786 | -61.9582 | 2024-10-09 04:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 23834002-fc74-38b9-9b44-f38b223f7aaa | -13.3978 | -61.9376 | 2024-10-09 04:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |


[Clique aqui para ver as próximas entradas](README82.md)
