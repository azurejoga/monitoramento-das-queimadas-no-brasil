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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 746a9ac1-752a-37d7-864c-7519ba2bb856 | 2.51478 | -60.9932 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8fd22e6-b0b6-3904-9785-af878568afd9 | 3.68613 | -60.5416 | 2024-12-07 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0298b5b6-dbd0-3361-b1c3-dc9ddf91de4b | -0.64282 | -63.02877 | 2024-12-07 06:12:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c88ebf73-cd15-3539-94a2-0c2431344648 | -0.64231 | -63.032 | 2024-12-07 06:12:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97a8c0a-75ad-33d5-8bd8-abd52ed1396c | -15.73 | -45.95 | 2024-12-07 11:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5ea9d91e-4568-3694-b4f7-3eb54194fe80 | -17.4 | -44.88 | 2024-12-07 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 16602b25-e0d4-30cb-b903-fc58d96a6e61 | -17.4 | -44.93 | 2024-12-07 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ad7f2a4e-e370-3d66-b64f-1c0d76384bbb | -9.19331 | -37.55774 | 2024-12-07 11:59:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a412a5d5-ae6e-34c4-b20e-5645a4466417 | -9.27204 | -37.83802 | 2024-12-07 11:59:00 | TERRA_M-M | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b75801cd-869c-3a66-8131-0eb27ed560e4 | -4.36177 | -38.15408 | 2024-12-07 11:59:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| d6a214d9-bf64-3ef3-80b6-21330484f8e4 | -10.93022 | -38.81072 | 2024-12-07 12:01:00 | TERRA_M-T | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| cc527282-f792-323c-95c0-da2c3824f2bd | -10.36951 | -39.22881 | 2024-12-07 12:01:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 994c5dc3-58b4-3f54-a8fa-40e1ed1b7cf4 | -10.1964 | -36.27514 | 2024-12-07 12:01:00 | TERRA_M-T | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| e50f02a5-9025-3b7c-9f77-9df770ab37f9 | -16.2871 | -39.59483 | 2024-12-07 12:01:00 | TERRA_M-T | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 0d6646b5-3636-3267-9ef3-a27e2aa48a38 | -19.59635 | -40.18342 | 2024-12-07 12:04:00 | TERRA_M-T | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| ad130ea8-b895-31c1-b8ee-948332991962 | -20.20458 | -40.31526 | 2024-12-07 12:04:00 | TERRA_M-T | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8aa328a3-40ba-3ab3-b5d6-bd7e2d77040f | -20.20596 | -40.30586 | 2024-12-07 12:04:00 | TERRA_M-T | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 69ca6062-a111-3231-a6df-762809f0e1c0 | -6.7535 | -46.5131 | 2024-12-07 13:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| d6857792-766d-3dfd-a263-a2ae3c61b8ba | -6.7535 | -46.5131 | 2024-12-07 13:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 21210945-4860-3e5b-addf-18ca9f9f0842 | -6.7535 | -46.5131 | 2024-12-07 13:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| f739c33e-1561-3c4f-8ea2-4722e4bed6de | -6.7533 | -46.5353 | 2024-12-07 13:20:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| f616fe63-8cce-31d9-8e72-43ad0591a5b2 | -6.7535 | -46.5131 | 2024-12-07 13:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 44ed4e83-ea87-3055-920e-3e71ba22bda6 | -6.7535 | -46.5131 | 2024-12-07 13:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 48cb6acf-942a-3231-8d05-0e6f5595f94f | -6.7535 | -46.5131 | 2024-12-07 13:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| a7fed913-0d46-3280-b41b-b86060dd7f1e | -6.7535 | -46.5131 | 2024-12-07 14:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| e1a5984c-8424-3bf7-b219-671b37e27784 | -12.4088 | -46.596 | 2024-12-07 14:00:00 | GOES-16 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d688326c-fd72-32d1-bfbd-ad40554f97d3 | -6.7533 | -46.5353 | 2024-12-07 14:00:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 5195d725-3b21-3113-a8a5-1a82d8efdcf7 | -6.7535 | -46.5131 | 2024-12-07 14:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| ec9eae2c-a381-3f1c-a1c2-b869c3123e67 | -12.4138 | -49.6725 | 2024-12-07 14:20:00 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 14cb6127-590e-35d2-b514-3132bf3a1374 | -6.7533 | -46.5353 | 2024-12-07 14:30:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |


