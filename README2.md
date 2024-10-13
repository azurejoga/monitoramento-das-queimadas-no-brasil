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
| 57d341f9-0ddb-31e1-8740-6afd45e204eb | -12.9182 | -62.5287 | 2024-10-13 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 429192f1-9043-3562-b64b-5f682387a6c9 | -12.9372 | -62.5275 | 2024-10-13 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 193.2 |
| eb13da96-0cab-3b25-abaf-c1c9f8c38a81 | -12.9373 | -62.5083 | 2024-10-13 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 9b85b3ee-6571-34da-b1e1-dbd3aea2fb20 | -13.1475 | -62.3215 | 2024-10-13 00:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 141.2 |
| ff5a003c-a605-3303-9c68-9f8df706d3b3 | -13.4683 | -43.6664 | 2024-10-13 00:06:22 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| af5d971d-5569-33db-91ff-53aca2f217f0 | -13.7153 | -60.6289 | 2024-10-13 00:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 8a1b8ff4-ab1e-3024-bfc9-4d3100bab971 | -13.7155 | -60.6093 | 2024-10-13 00:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| df7b00fa-aa45-3cfc-8b7f-28d9c72f9e19 | -13.7346 | -60.6079 | 2024-10-13 00:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 9262a284-a0bc-3b34-974f-bb12f118eb8d | -13.7348 | -60.5883 | 2024-10-13 00:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 64657474-655a-34f7-860e-b35baa6ec0c9 | -14.7635 | -57.8192 | 2024-10-13 00:06:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 3ac5615f-e23d-375c-a1e0-8504eb818909 | -14.7638 | -57.799 | 2024-10-13 00:06:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 80196766-c18a-374a-a196-5ee93cb24fec | -14.7641 | -57.7789 | 2024-10-13 00:06:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 03c640d0-8df5-37d5-bc6d-60dc534945a5 | -14.7831 | -57.7971 | 2024-10-13 00:06:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 2303668f-2d93-30df-bbfa-05212d378f20 | -14.7833 | -57.777 | 2024-10-13 00:06:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5c06e3dc-ee7a-3414-a93a-ca01d3a1a0e0 | -15.6419 | -59.9767 | 2024-10-13 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 644ad8de-6e23-3e85-97a5-8fdec86576f4 | -15.6421 | -59.9568 | 2024-10-13 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| eccdf998-7ac1-344f-940c-63941f8f1875 | -16.9998 | -57.4586 | 2024-10-13 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 53196a6a-ae86-3bd0-9431-e70bf24586cf | -17.0001 | -57.4381 | 2024-10-13 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 12448164-62b9-39ff-b1e5-f2f8093da282 | -17.1169 | -57.4859 | 2024-10-13 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| c87ac047-4bee-3b0e-a3f1-28138d255511 | -17.1172 | -57.4654 | 2024-10-13 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| 4e211538-6872-3eab-9e95-0c0b07d5571c | -17.1758 | -57.479 | 2024-10-13 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.4 |
| 5f92cb85-218f-3033-845f-090f88ca91b1 | -17.1761 | -57.4585 | 2024-10-13 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 228.2 |
| d8f767a1-9124-3d6b-9193-219ff0af0737 | -17.1764 | -57.438 | 2024-10-13 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.5 |
| c380edf3-c6f9-34b0-b6b7-b150b4a9f7a6 | -17.1954 | -57.4767 | 2024-10-13 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.6 |
| e3964dc8-2fd4-3fb0-bd2e-8024d7e2659e | -17.1957 | -57.4562 | 2024-10-13 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.9 |
| c653b1c2-f189-30f4-bbf1-ee060766b18f | -17.6862 | -56.3241 | 2024-10-13 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 179d13b5-750f-3caa-92bc-4a1ce2c53cc7 | -17.964 | -57.3843 | 2024-10-13 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.6 |
| 666d986a-4706-3ec8-a94f-1d412274ddb5 | -17.9643 | -57.3637 | 2024-10-13 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.9 |
| 1215426e-c27f-3c79-8baa-ccb926a5cd5b | -17.9837 | -57.3819 | 2024-10-13 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 52f88e49-952a-3ba8-979b-f709f6c1152c | -17.9841 | -57.3612 | 2024-10-13 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.6 |
| 8b98946b-3124-30a0-90d1-ada72584c61e | -18.1949 | -56.5899 | 2024-10-13 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.0 |
| 5533148f-7c74-3e63-93be-388ce7757f41 | -18.1953 | -56.5691 | 2024-10-13 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.7 |
| 724327f3-fdfd-392a-aa15-22d6c96fdded | -18.2147 | -56.5873 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 203.6 |
| 744468a7-57f6-3f70-b37d-719ce6c11a5e | -18.2151 | -56.5665 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 317.7 |
| 5259a892-a0e5-33a0-a9b0-725376580827 | -18.2155 | -56.5457 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 78e42039-021c-393b-a047-db9f5725ae6d | -18.2162 | -56.504 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 0007c7f9-f412-3e91-a68a-3b1438a6b2da | -18.2166 | -56.4832 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.9 |
| a7890d27-05d9-33af-9ccf-e1c2b38b131b | -18.2169 | -56.4624 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 2624149c-9522-3a29-b4d5-9e4a9dbf5ae4 | -18.2349 | -56.5639 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 5cca8fec-2f49-3517-b8b3-7e7a54ba1742 | -18.2364 | -56.4806 | 2024-10-13 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| e2e11ccc-c978-3868-80fd-8417e5998288 | -1.6635 | -52.147 | 2024-10-13 00:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 1c85709d-57ac-3ad5-9529-4d9889e0a794 | -1.6635 | -52.1265 | 2024-10-13 00:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 057133f0-d225-3e8a-a69e-0778c34a5c30 | -2.1508 | -48.8112 | 2024-10-13 00:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 32139228-9f6b-3b39-8a40-26c30c464fed | -2.1692 | -48.8322 | 2024-10-13 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 247300d4-9826-3bcc-969c-5fd37d8437b7 | -2.1693 | -48.8108 | 2024-10-13 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4c17009a-6fc7-3a21-870b-fd5f894c79d6 | -2.5258 | -47.2674 | 2024-10-13 00:15:21 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| e5db8b24-02d2-3815-bb7a-c2d88442a27f | -3.0731 | -54.2473 | 2024-10-13 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8c061ea2-66bf-3795-ba96-c678a982005c | -3.0732 | -54.2273 | 2024-10-13 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| dd0bc7cd-2a76-3b71-ab3b-ab85eec504c1 | -3.0773 | -53.036 | 2024-10-13 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0f3dd27b-8770-370c-9b12-490aee3c3bb3 | -3.0915 | -54.2469 | 2024-10-13 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 2e2e4d5a-f8af-3928-a636-4f46e1252340 | -3.0956 | -53.0559 | 2024-10-13 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 9e988393-1607-30aa-9bcc-00b784db2418 | -3.0957 | -53.0355 | 2024-10-13 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 0b3e9421-0942-348a-b7f7-7c05a1affc9e | -3.0957 | -53.0152 | 2024-10-13 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c938d443-19d6-3148-a4e6-9ab01b02f0b3 | -3.1791 | -50.476 | 2024-10-13 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 59c70c17-bc66-3c77-8969-ceb7fc96ce01 | -3.1792 | -50.4551 | 2024-10-13 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 66dcc8a3-a527-3c13-9e9e-fc03adc71c54 | -3.1976 | -50.4545 | 2024-10-13 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 211e10b8-da9b-3b29-815c-488b846e0761 | -3.114 | -53.0554 | 2024-10-13 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 35d8ae29-34b6-3eee-b888-048944d0aec9 | -3.1141 | -53.0351 | 2024-10-13 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 95ce26e3-4fee-3c99-9f92-af62426707d5 | -3.2225 | -48.9306 | 2024-10-13 00:15:25 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| bc0154fb-e5f9-36cc-bad6-aa57c2824511 | -3.5264 | -51.257 | 2024-10-13 00:15:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7f8c8797-3739-369b-b825-3ed617233039 | -3.5449 | -51.2564 | 2024-10-13 00:15:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| e14c19ce-1c24-3482-9cf1-960e25929b31 | -3.545 | -51.2357 | 2024-10-13 00:15:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4e6f838b-96cf-3240-86c6-533b9654ad0a | -3.7127 | -40.7346 | 2024-10-13 00:15:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 4e1ee0b2-5c60-3bd7-a4da-ecc2e1b27e7a | -3.7128 | -40.7102 | 2024-10-13 00:15:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 126.7 |
| 03ae99b7-b59f-303d-866f-95480fc4e5ce | -3.625 | -54.132 | 2024-10-13 00:15:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ca5da523-1502-385d-be6c-b9bb56f547a3 | -4.085 | -43.9319 | 2024-10-13 00:15:29 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6e6b7858-c56d-37f7-bf1a-8849309240ee | -4.1037 | -43.9309 | 2024-10-13 00:15:29 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c78c34ae-05b9-350d-9534-e63350e00b51 | -4.1148 | -48.2515 | 2024-10-13 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.2 |
| 1a4477bf-09f7-3a9d-a3a6-6c2c50b7c703 | -4.1149 | -48.2299 | 2024-10-13 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| e15c7422-43f8-31c0-8c82-a547c394eacb | -4.1479 | -45.7896 | 2024-10-13 00:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 3198b7c8-cf6a-3598-bf52-0409094fee34 | -4.148 | -45.7672 | 2024-10-13 00:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c6c1b776-fa71-3f4d-a064-daa1524fabeb | -4.1665 | -45.7886 | 2024-10-13 00:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 3a334dde-21d1-3ab2-97f1-713427132f4e | -4.1666 | -45.7662 | 2024-10-13 00:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 200.9 |
| d2776a62-e60b-39c7-a14a-6626512d51fa | -4.4026 | -49.7563 | 2024-10-13 00:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 469063ce-9928-33e7-91ff-553044812d19 | -4.7188 | -60.7882 | 2024-10-13 00:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cf147a49-0382-306d-9917-b667a5200451 | -4.7189 | -60.7692 | 2024-10-13 00:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ea50737e-41dc-322f-ae75-79b420a03350 | -4.7371 | -60.7877 | 2024-10-13 00:15:34 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 02c18f71-0b64-3940-8e3f-8389606ac058 | -4.7372 | -60.7687 | 2024-10-13 00:15:34 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e9eaae6f-2acc-3884-bdbf-270849d91b2e | -4.8604 | -47.738 | 2024-10-13 00:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 78007316-50f0-3b2c-a193-f0c4167af3ef | -4.898 | -47.6707 | 2024-10-13 00:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 472680f9-6334-34c3-b79c-11f7ee17c71d | -5.0713 | -46.8499 | 2024-10-13 00:15:35 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 8f61bdc8-daa1-3cc8-ac8b-e7ac392adaa0 | -5.1381 | -45.3969 | 2024-10-13 00:15:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3b028c8f-43ad-3011-8717-727466e3c99b | -5.1695 | -46.1569 | 2024-10-13 00:15:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5e096569-1b16-3181-ad8b-b3e10d8e67f8 | -6.1299 | -47.2884 | 2024-10-13 00:15:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 42db8d32-38eb-3214-8b07-296a02e66daa | -6.1301 | -47.2664 | 2024-10-13 00:15:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c9c57440-2c42-352f-a240-614bfc072c3d | -6.8734 | -59.802 | 2024-10-13 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f29c1063-21a1-3d35-889b-8f2212b28d13 | -6.8918 | -59.8013 | 2024-10-13 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 21278274-0cd8-3fd5-b4ee-feae2a08e500 | -7.3823 | -47.2586 | 2024-10-13 00:15:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3d7be3f2-ea21-3103-b7d5-4d420facf2f2 | -7.3657 | -64.6656 | 2024-10-13 00:15:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 1d551677-c2fb-3db5-b3aa-4070b351b5ed | -7.3658 | -64.6469 | 2024-10-13 00:15:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 6b0182d6-e5ac-3fd1-8c76-33c0762091de | -7.3841 | -64.665 | 2024-10-13 00:15:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 2f92e6a0-0ed4-338b-9a6a-dd693a28c986 | -7.3842 | -64.6464 | 2024-10-13 00:15:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b6fc238d-c643-3055-b5ae-65fee7de3547 | -7.6627 | -47.3229 | 2024-10-13 00:15:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| a378e622-2e8c-329b-8d1b-b1fc1690f013 | -7.6629 | -47.3009 | 2024-10-13 00:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 5603055e-ad18-3ebe-94a3-3264495a60f8 | -7.6815 | -47.3213 | 2024-10-13 00:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| a36f4f91-f67d-3114-87b6-c8d3186e7e9e | -7.6817 | -47.2992 | 2024-10-13 00:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 93fcf06f-8948-3b4e-b962-0b02bbf04dc5 | -7.8713 | -54.7217 | 2024-10-13 00:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 7e3438d1-9652-3891-b6a7-65ef6ccb40ab | -7.8715 | -54.7016 | 2024-10-13 00:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 75830653-9978-3c65-8485-17e11f55767d | -8.0672 | -44.8388 | 2024-10-13 00:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9259818f-344c-3a53-9276-2fb775f33741 | -8.0675 | -44.8158 | 2024-10-13 00:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 234.1 |


[Clique aqui para ver as próximas entradas](README3.md)
