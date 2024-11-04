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
| 1b61b3ba-3694-3a50-bf2f-17cb7fa3a5da | -4.6464 | -46.358398 | 2024-11-04 00:04:06 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d21ac55d-4425-37c9-b77a-a1eacb2960b0 | -4.6603 | -46.375401 | 2024-11-04 00:04:06 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0a17993-b18c-3de2-93fb-5f2c59353978 | -4.6561 | -46.3563 | 2024-11-04 00:04:06 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f31951a8-6257-343a-a433-e0b4310b97a0 | -4.6037 | -46.4883 | 2024-11-04 00:04:07 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 868cb002-f51e-3030-90b0-0f9946396acf | -4.6176 | -46.505699 | 2024-11-04 00:04:07 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e55d1566-3f8f-3e54-ba05-ae5b2200b1c2 | -4.6134 | -46.486301 | 2024-11-04 00:04:07 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e624754f-2c53-304e-8566-0f69c898e140 | -4.6091 | -46.4669 | 2024-11-04 00:04:07 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64932873-064e-3b17-b897-49880e4f8333 | -4.3643 | -45.721001 | 2024-11-04 00:04:08 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5051957-c965-31a2-b48a-db09683e67b1 | -4.3605 | -45.703999 | 2024-11-04 00:04:08 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc6be4d4-3487-3faf-acc0-d137873dafda | -3.2476 | -41.1301 | 2024-11-04 00:04:10 | METOP-C | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2172d657-c651-3042-b942-2a99e6b28b12 | -4.2018 | -45.9548 | 2024-11-04 00:04:12 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 930cca14-2dac-3539-ac9d-fc539a335142 | -4.2115 | -45.952801 | 2024-11-04 00:04:12 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b70a1ae5-a5aa-38c2-9b8d-6ddc79fe6994 | -4.3493 | -47.229599 | 2024-11-04 00:04:14 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 917173b8-1106-3a32-a6de-d22036732685 | -4.3446 | -47.208 | 2024-11-04 00:04:14 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0064091b-67b7-342c-8837-6eca00de441d | -4.359 | -47.227501 | 2024-11-04 00:04:14 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1bb828e-b405-3ba1-aba2-806fd76819ef | -4.3543 | -47.205898 | 2024-11-04 00:04:14 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c966cfc8-a54f-3c35-9d96-b667a5480f1e | -4.053 | -46.249802 | 2024-11-04 00:04:15 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e0b2d4b-e25f-3610-9cfc-ef30a2243965 | -3.3231 | -44.159199 | 2024-11-04 00:04:20 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 695ff098-bca8-3150-9752-2e2b61c1f4a6 | -3.3203 | -44.1464 | 2024-11-04 00:04:20 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b85859e-d556-3cb6-af61-e9782da09e96 | -3.057 | -43.201099 | 2024-11-04 00:04:21 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 628f1d27-b8ef-3aa3-a552-23f1284c4f76 | -3.0545 | -43.190102 | 2024-11-04 00:04:21 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f142462c-eb71-3e7d-a296-9abd5d575b69 | -3.628 | -45.986401 | 2024-11-04 00:04:21 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40037f6e-59d8-3d8a-915b-dc49bf706ef5 | -3.9547 | -48.111801 | 2024-11-04 00:04:24 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


