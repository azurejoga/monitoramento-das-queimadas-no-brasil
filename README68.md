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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae409cdf-8d9b-3d0d-b834-ab2befe5a4b3 | -5.6923 | -43.9217 | 2024-10-27 14:35:37 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 17514673-ae7b-3bef-ae79-ec48358d4f3d | -5.6925 | -43.8986 | 2024-10-27 14:35:37 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| b79a030b-638d-34c8-a435-6ac7406f2aba | -5.711 | -43.9203 | 2024-10-27 14:35:37 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b9250951-22d4-3e38-b9cd-8e48ee5e59c7 | -6.0905 | -45.4216 | 2024-10-27 14:35:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e2066acb-55d4-3551-ac3b-c9b1a17081f4 | -7.5893 | -39.3611 | 2024-10-27 14:35:47 | GOES-16 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 188.2 |
| c747195f-29f2-30f7-b458-054362b935d1 | -7.9999 | -39.8621 | 2024-10-27 14:35:50 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 79e2f15d-163f-3986-be34-1fb200fa8b15 | -9.3537 | -43.3711 | 2024-10-27 14:35:57 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| e82ea782-90db-3a7c-ba7d-729b5f06a74f | -9.3727 | -43.3687 | 2024-10-27 14:35:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 174.4 |
| 9b189d57-303e-3b94-8529-85acd518c151 | -10.5757 | -44.2636 | 2024-10-27 14:36:04 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 795c178c-261c-3044-a053-435ee9bdcd2e | -10.6139 | -44.2584 | 2024-10-27 14:36:04 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 441668e4-a011-34b0-8d87-1113a8aa7fda | -10.5948 | -44.261 | 2024-10-27 14:36:04 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 173.8 |
| bbf61d84-e533-37b6-91c7-e67f1638841b | -11.3021 | -44.2074 | 2024-10-27 14:36:08 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b5ebc891-fedf-3771-90a8-ecfda4fe06f0 | -11.2829 | -44.2102 | 2024-10-27 14:36:08 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 0aaba390-e13e-3209-8f6e-c652c62549bd | -11.3221 | -44.1577 | 2024-10-27 14:36:08 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 777da059-94d5-3d68-b7ee-a1e67349047e | -12.8883 | -44.6143 | 2024-10-27 14:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 5d36443b-9785-3ca0-9393-230169f9e1a6 | -12.8695 | -44.5941 | 2024-10-27 14:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ee8e98b5-8747-318f-96c0-2ed056fac9f6 | -12.869 | -44.6175 | 2024-10-27 14:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b8b2b474-a846-3c3b-9469-2b855595e185 | -12.8888 | -44.5909 | 2024-10-27 14:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 47bd97fb-5e73-3299-9d23-417bde7b87b5 | -13.0747 | -42.1261 | 2024-10-27 14:36:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 140.8 |
| 159cbbe1-cf9a-3c9b-a61c-0ac470494b3f | -13.9074 | -43.1072 | 2024-10-27 14:36:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 274.1 |
| 0b818003-6b7e-3391-a381-c3e757578e5a | -13.9069 | -43.1313 | 2024-10-27 14:36:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 133.1 |
| cafce4ae-cfd1-3cf0-9975-71c5f3140d6d | 1.7775 | -50.468 | 2024-10-27 14:44:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b50fa361-c0d2-38a1-a1f9-513c582e2639 | 1.1503 | -50.998 | 2024-10-27 14:44:59 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 109.2 |
| af5b2b6b-671c-3d27-be8e-e9764813005c | 0.1197 | -50.5042 | 2024-10-27 14:45:05 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| dcd077c3-af2b-337d-bd2c-b7b2313cb8bb | -2.4598 | -50.412 | 2024-10-27 14:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| f1e5e250-9948-3480-82f3-87de0010a1a7 | -3.3891 | -41.6201 | 2024-10-27 14:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 84ca03e0-454b-3b05-904f-3063cbd32a77 | -3.5775 | -41.3948 | 2024-10-27 14:45:26 | GOES-16 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| eecf2e6c-2f4e-3391-9919-0491f8da2723 | -4.3336 | -45.8472 | 2024-10-27 14:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |
| a5c5ea2c-7537-33ba-917a-38ecd3f3b02f | -4.3522 | -45.8462 | 2024-10-27 14:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6be827a7-cc6f-3074-a861-fc3cb056b824 | -4.7565 | -46.6249 | 2024-10-27 14:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d8e49a44-c992-3127-bdb2-78a35ad5e617 | -5.568 | -45.3235 | 2024-10-27 14:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 3c7225f0-7cb4-3a4e-9880-5244b3bd0109 | -5.5682 | -45.3009 | 2024-10-27 14:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| fcdbe6d6-592d-3332-997d-bd25a765e65a | -5.6925 | -43.8986 | 2024-10-27 14:45:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 54d63ae3-bddd-3ba5-bea9-46ac9151dc36 | -6.9974 | -41.3016 | 2024-10-27 14:45:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 4ef1958e-0074-3853-babf-ec4abc5f8339 | -7.5594 | -38.7576 | 2024-10-27 14:45:48 | GOES-16 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 6003f5ec-6aec-3493-8860-cbc095116ea0 | -7.9999 | -39.8621 | 2024-10-27 14:45:50 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 214.0 |
| f6230ae3-9c61-3400-80f3-c42e97f38426 | -10.826 | -45.2693 | 2024-10-27 14:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2750332d-18b7-3c78-ad90-2f6a2d0711bd | -10.807 | -45.2718 | 2024-10-27 14:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ebae11bf-0732-3769-be14-6fcdb128fd5f | -11.2829 | -44.2102 | 2024-10-27 14:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 6fad4104-89f7-31c8-b1a6-8897ddb832c2 | -13.0747 | -42.1261 | 2024-10-27 14:46:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 110.6 |


