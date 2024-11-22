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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b999bf26-d013-336a-925f-73aa52ac6b6b | -4.23444 | -48.6319 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 697e2534-d232-3495-9dc8-43634d1eda85 | -3.17768 | -54.31881 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b59a3818-11f8-330e-945f-79d97f063c92 | -3.17871 | -54.31642 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 061eba65-28d4-3920-86ec-cac503b35ed6 | -3.23574 | -54.25132 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 33fccdd9-1a5d-3812-8552-f91911d0b7b0 | -4.48025 | -48.11804 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 764c781b-e449-3d8f-88da-6d8b72ab6762 | -4.70658 | -45.80972 | 2024-11-22 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c026fde0-8cd8-3005-aa93-da0b5dc92138 | -5.58783 | -45.20773 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e01e26c8-b3c4-3264-adc8-d6784c3498d9 | -2.94931 | -53.71717 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7710ce9-04cd-3018-a0bf-bb7c31ea362f | -2.43955 | -46.54215 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8fe876e-6054-378b-a8a8-6146c895f8c7 | -2.75127 | -51.87976 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e14eb856-b687-3adc-8f32-dbca8398a9ed | -1.74555 | -52.39903 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 879591a5-9022-3e13-b56b-8b6f44e8832c | -3.33596 | -53.32906 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8260d46-34e8-3339-b894-ea5026c715eb | -2.74568 | -51.87888 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e15f0e7-633d-3261-88cd-441955389c51 | -1.78348 | -47.10361 | 2024-11-22 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5989cfac-0833-34d3-b369-3e632da4a70f | -2.70368 | -46.22128 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2499b01-f2c6-3ee5-93f4-bf9250453003 | -2.70031 | -46.05026 | 2024-11-22 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60999d98-c107-359a-9c4b-f7f73cdaebac | -3.8456 | -51.14318 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c2a2c45-9184-3f05-a113-43a68c3c0cdc | -3.89264 | -50.07439 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9973428c-2d0d-3a84-a2a7-c162afc5eac1 | -5.59245 | -43.74266 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8ec1ea6-08a0-33a7-8fcf-90265f88c08f | -3.17676 | -54.32417 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf4b25fb-45db-3749-adac-9281226c9aeb | -1.50681 | -53.13469 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca8d8f10-183b-369b-aa31-e26016ac62e1 | -3.8899 | -43.9924 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ed1dac8-43ca-3238-bb76-275e8d37cdf1 | -4.83549 | -44.92971 | 2024-11-22 04:12:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e73c5357-9f0c-3014-a1d2-5e3005e1bbfd | -2.64436 | -45.13213 | 2024-11-22 04:12:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98777d89-7134-3673-bf97-8c4e7276d8a8 | -5.00152 | -42.9482 | 2024-11-22 04:12:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a509d576-40d8-3ddd-b392-d8d13cd41d73 | -4.01986 | -43.98634 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c33f041-59e1-3975-9b17-e6f20bffcb88 | -4.06237 | -46.41396 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cfe5b70-8ef2-3ea7-b78e-5cff19ffee3c | -2.69515 | -46.08445 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c89e8f8a-b325-37f3-bd0e-248b90f7750e | -2.78364 | -51.72018 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92e78486-85d8-3e86-a729-8db541841133 | -3.00851 | -51.31288 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb9a827d-c56f-366e-941d-bd980d412af0 | -1.13702 | -51.67853 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e360560c-d02f-3fc4-a452-4d05942b6250 | -3.71911 | -52.09347 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a6a8fd7-0b51-37bc-9a56-025d3ce0517e | -3.45761 | -45.90226 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b892703c-7fc7-3759-8c2e-7643d71c69f3 | -3.57572 | -54.5149 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7c30ea0-2e13-3be0-90ba-2bfb9b899b17 | -1.11869 | -53.40126 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0a6e8bf-98e1-33b4-a66a-b1fe64d5ec5e | -1.21037 | -51.74448 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79fe5d3c-734f-3227-97cf-ddb6965a0828 | -2.15423 | -50.46771 | 2024-11-22 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83454227-f021-3674-ad45-8d8c96febea9 | -4.00626 | -49.92671 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99f2f217-bf62-3b89-93de-c467dfd7a923 | -3.38148 | -44.44562 | 2024-11-22 04:12:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d16fdae5-dbb9-3f97-b0b3-99fed13c20e9 | -2.68838 | -46.171 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e69d5a3-9e36-327f-bd7a-3ad11c43b303 | -1.11951 | -53.39626 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c8e9b995-5ca6-3036-881b-b85bfcd7f219 | -2.68599 | -46.09026 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51694a5d-6a42-33cf-a8b5-36f9a339acf3 | -5.00754 | -45.51745 | 2024-11-22 04:12:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9311eef9-7860-3d96-a95c-b66718ffedc1 | -7.64765 | -35.06459 | 2024-11-22 04:12:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4c69bb6c-a92d-3dff-ae14-57f31ceff6b5 | -2.91943 | -46.83844 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a3fa755-8ed4-39bc-872f-b643ba108258 | -3.05149 | -51.33323 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e720cac-24f5-332a-9bac-e480de1f867a | -3.28336 | -53.85681 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 280b9a66-8d62-34a6-9777-6941abc0a122 | -3.22838 | -54.25564 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 53e19438-ff8d-3b1b-8ff2-19b4a844c08c | -3.07998 | -45.96987 | 2024-11-22 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d457c398-d72f-38a3-8510-7144d673b03b | -1.62719 | -52.6017 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c3f1bc-5060-3230-9f9d-92f3977807b5 | -3.46805 | -45.90844 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0393408f-3dca-3010-91b2-56a7f4c73ecd | -6.77966 | -35.19535 | 2024-11-22 04:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b26113a6-95d9-3f72-bda9-2737bc2c840b | -5.1028 | -43.16347 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9274a988-0908-33c4-b6ef-7d4e1a7cd6ae | -3.68348 | -50.21809 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 133a9b36-2869-3bec-8a20-95f11c283cb0 | -3.33518 | -53.33355 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ec677ce-285e-3454-aa6b-7ea234c80d5f | -3.2275 | -54.26081 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e8d3d49f-8b7f-3765-9789-d1a68c8c30ec | -1.21438 | -51.97783 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9d41590-8a3d-33e6-be7e-4f204661c065 | -4.51852 | -45.70461 | 2024-11-22 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5c2099-81af-32cc-8a06-e35e64a1df50 | -4.19007 | -53.58105 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2d0ec8c-275d-30ac-aa66-81e71b9e6d46 | -0.81203 | -51.79026 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c24bf356-bf25-315f-aadc-4d8dfd11015c | -1.1313 | -53.4033 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b01877c0-5256-3bc6-a83a-4455829f98fc | -3.09859 | -53.21101 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dfe6c75-4972-3c55-9d43-afe132408a37 | -1.64215 | -52.62197 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea4b7706-ac36-30fe-8c05-c4b1e6e9f7a4 | -3.46827 | -45.91527 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6229021-8d31-3658-8cad-e9f3a661f4dc | -2.19958 | -53.6508 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de278e81-9b2e-36c2-8983-ae003ed354c0 | -3.51028 | -53.81324 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e3e054b-e53c-3f20-923d-b7eb6497f114 | -3.45622 | -45.91102 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e74e6601-6b97-3f34-87a3-717fb18b465e | -2.69811 | -51.86836 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 373b8b3f-85b3-3734-b14d-398d02a2ed58 | -2.61065 | -46.199 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28f232a4-9f77-324d-97a3-1bdc620e49eb | -3.88818 | -46.66378 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2779c182-8a57-37e2-bfed-592b1a5b7831 | -1.22471 | -51.73937 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bbe4b9b-56f8-3927-8921-95e9e32caed5 | -2.40243 | -46.02776 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b904525-f32c-3f35-b09d-02e434c997fe | -2.30777 | -53.59829 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9ec7a0c-0302-3c08-9c78-4e4d84060d5a | -2.65055 | -46.24383 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be5cdcfc-6fa9-3e12-a6e2-6068c1f4a709 | -4.01117 | -49.92397 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c8d56fe-ced5-3c07-aacd-cf8064d6a560 | -2.65552 | -48.78692 | 2024-11-22 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26ab349b-609c-3c16-aed9-9bd406ba0f77 | -2.83966 | -51.82256 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b195806-328c-3bdb-a6a3-40f26e3eda57 | -1.77468 | -53.60851 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b46b02cb-9154-3fc8-97cb-42863fc5640f | -2.75874 | -52.11333 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaeb4854-185d-364a-b6d9-d64ca88bedb7 | -1.19964 | -51.95906 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5bb3dfbf-6ffa-3550-a55a-301705ace235 | -2.43876 | -46.54705 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c823ca8e-9d07-3486-aa90-cda769436dc3 | -3.60035 | -51.55598 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e7fade2-8888-3701-b432-67cae3efcfd2 | -3.13688 | -44.87591 | 2024-11-22 04:12:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0c87be3-5809-3d7b-8128-bb377796f8cc | -1.72704 | -52.71394 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d577afb-bb5e-3d12-92da-bef260874a25 | -1.7921 | -53.63285 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8757b711-b0f7-3546-ae86-a668421d7edc | -2.6814 | -46.17218 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9f9c69c-d5e6-33ad-a3b5-0e069b539ab7 | -4.57882 | -48.02007 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed65b585-8f8a-372a-9493-48dd2b36c641 | -2.15374 | -50.47073 | 2024-11-22 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 513ca767-8fdd-38a1-aed1-1c255690eb0c | -2.7063 | -45.23072 | 2024-11-22 04:12:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25b5c3fa-593b-3596-badc-6e97afc8e52a | -3.10064 | -53.98628 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bcd99c8-5771-32dd-91ef-387d7b59d18d | -1.14266 | -51.67949 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc299c1c-465f-3d8f-95b9-67aa892968b9 | -3.20813 | -54.2578 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4945403f-3c99-371b-b9ed-f45f93390716 | -3.40339 | -46.24323 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ab08578-7883-36c6-8ed5-5071a094d33c | -6.81624 | -46.77807 | 2024-11-22 04:12:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2749ed69-33d2-3e1e-8d54-f88976226aa9 | -2.58257 | -46.5475 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98be25ce-47e9-32ea-bc01-915c94f5dd99 | -4.14233 | -54.66356 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1754d8d3-e207-3f0a-9f1a-4caac3da9a5e | -2.35086 | -48.56039 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7754b8b8-be6b-394f-9114-4fd2942cff45 | -4.11259 | -51.05428 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe2e64c-1d7a-3130-962d-6c9ed9cb66df | -4.13582 | -54.65639 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb72b7e2-9879-3d99-a6ea-272cf2c966bb | -1.77739 | -53.60442 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
