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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593b8b15-2083-3832-aae3-562e8d233046 | -10.0623 | -48.0978 | 2025-09-02 14:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| db77a9ab-4355-3ccf-9966-7370ba89cf63 | -6.9632 | -44.3477 | 2025-09-02 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2103d0ff-e716-3d9e-ac03-6b369289c89d | -7.6783 | -61.0908 | 2025-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e83818fa-963d-3440-89a7-6a005d21fde4 | -12.0066 | -51.351 | 2025-09-02 14:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 47ac9254-45d6-3e1c-9359-3c481186f90b | -4.8936 | -43.1882 | 2025-09-02 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 1793bac3-49b8-35f5-a26c-c96cb7e49ace | -8.201 | -49.5131 | 2025-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 165aab69-10c3-31d9-8709-77a9295f6ae4 | -11.0845 | -44.6343 | 2025-09-02 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 258cee87-2ced-3d21-8146-186523cc79b9 | -11.9879 | -51.332 | 2025-09-02 14:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3f648e97-56cb-317d-a015-d1308bb89667 | -14.5662 | -53.0081 | 2025-09-02 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 40a4c40a-0a3b-3b69-bff9-25473be00a89 | -7.1091 | -44.7474 | 2025-09-02 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 405b9cab-882d-37ec-9973-79c9fef9983b | -4.9122 | -43.2103 | 2025-09-02 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 76547eb4-ea44-32f5-b19f-9bda7cfa6485 | -7.4969 | -45.3495 | 2025-09-02 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 259c4e61-45e8-3bb3-932a-fa7407b4c30f | -6.2583 | -43.5294 | 2025-09-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 85ba1127-7b75-33d1-bda3-ddb2592cce80 | -8.5758 | -62.6323 | 2025-09-02 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 4270c50a-8eae-3b8b-833a-6519274c1bf5 | -7.4652 | -44.829 | 2025-09-02 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9a6a95f1-1bec-30c7-96bb-4839beb56565 | -9.0141 | -45.9886 | 2025-09-02 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 0acda6d5-f79b-3951-b91c-3c6e827f29b4 | -6.204 | -43.3241 | 2025-09-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e80a43f6-b8ba-321f-aa34-861904866994 | -11.3496 | -43.6842 | 2025-09-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| a77310f2-0c03-3e0d-994a-73bc716173a9 | -11.834 | -51.4551 | 2025-09-02 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 73c37a7b-15eb-386c-bc3b-577fa8a22d65 | -6.8724 | -45.8554 | 2025-09-02 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0757f1c8-7ef8-3d42-8dec-067182416892 | -13.3175 | -51.769 | 2025-09-02 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1875021e-06e2-3cf6-8c99-260e8f03932c | -6.8909 | -45.8763 | 2025-09-02 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| f5e038e8-e5e5-3aa9-8fa9-92a79f1499ab | -11.6717 | -52.189 | 2025-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 79f6f9e9-9c9d-3dfe-8e37-195ffc1d3e68 | -6.185 | -43.3491 | 2025-09-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 70bd5d4e-d0b2-36c0-a63a-82194001a1bc | -12.0069 | -51.3298 | 2025-09-02 14:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 7c459a17-7e12-3102-9282-7194610d956f | -5.8882 | -42.9988 | 2025-09-02 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 156.9 |
| 8002ed1f-58f0-3cb0-9d95-b749e206a8ef | -9.7294 | -48.9834 | 2025-09-02 14:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1fbf724d-f5ff-313f-b270-d355151df8c3 | -11.6715 | -52.21 | 2025-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| feee4f85-0d90-33b7-acd6-3300e782b378 | -9.5025 | -57.8032 | 2025-09-02 14:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| fe8507a6-4231-316c-abfd-f27e120fda53 | -11.3907 | -46.8724 | 2025-09-02 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| b939d77d-7cdb-32af-b0ca-5cfa219d0c6c | -9.0141 | -45.9886 | 2025-09-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 808801fc-a529-34f2-8037-a1715245245c | -11.6644 | -57.3733 | 2025-09-02 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 079b2294-cad5-3271-8c10-1bded1560fa2 | -6.9942 | -43.2308 | 2025-09-02 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 187.6 |
| da7288c4-46d5-33eb-b29f-626df1faa0c5 | -14.5662 | -53.0081 | 2025-09-02 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 846a85f8-2b20-3b71-bc65-84221e1105aa | -11.3893 | -43.6075 | 2025-09-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| f83e8efc-b61b-34cd-b5cc-060d6a692d2f | -11.3901 | -43.5602 | 2025-09-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5610f742-3035-35b5-a6d0-9d9670d3c9c9 | -9.5025 | -57.8032 | 2025-09-02 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 3ab9d421-82ee-32da-bf79-9fcaffb7d9e2 | -9.4791 | -46.5218 | 2025-09-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 585.3 |
| 57beebc1-df26-391e-bd1f-89f4e810c371 | -11.6715 | -52.21 | 2025-09-02 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| e7734e16-8128-3183-9691-7c75ada1a57a | -8.2198 | -49.5115 | 2025-09-02 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| ef8224fb-ccdc-3311-82e7-593137fb6c58 | -9.4981 | -46.5197 | 2025-09-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 17691a5b-e1f4-3d87-908f-f7b013b879d3 | -10.062 | -48.1197 | 2025-09-02 14:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b70a3762-0511-33f2-bfd0-cd0399b00bee | -11.853 | -51.453 | 2025-09-02 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a5af19f5-f18a-3cd7-9584-c52d1295d3b9 | -11.6647 | -57.3533 | 2025-09-02 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 0510a693-c3a9-3edd-ba0d-fd8e1bc0a421 | -9.4984 | -46.4973 | 2025-09-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 4af0a0bb-1946-3c0f-ae6f-b3e07242dd29 | -6.2221 | -43.3927 | 2025-09-02 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| b0bf8c77-0479-3662-b875-f8916db4c251 | -5.7357 | -45.3796 | 2025-09-02 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e8efcb2c-fb5e-384f-ad0e-3b3090d21f55 | -4.9122 | -43.2103 | 2025-09-02 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 03922993-f3e3-36c7-85aa-7e263579e23f | -6.0291 | -46.0103 | 2025-09-02 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 1199bda3-e152-34b5-88b8-dc67b06a965a | -5.8692 | -43.0238 | 2025-09-02 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 7562f563-2c6c-3e77-bde5-7183485654be | -8.201 | -49.5131 | 2025-09-02 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| f3d99d25-d268-323e-9ae7-0c8703cdf744 | -7.4969 | -45.3495 | 2025-09-02 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 786de115-3bba-30b8-b8da-09644abf98d6 | -15.7363 | -53.6772 | 2025-09-02 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 76abf23e-a603-321d-8a84-6fb67e246b67 | -7.4652 | -44.829 | 2025-09-02 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8dd8895c-f683-3247-aa68-1818d5c679b5 | -12.2156 | -50.1295 | 2025-09-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3e3aa0b4-f044-38a1-acdf-17962a549d76 | -11.4491 | -46.7973 | 2025-09-02 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b91959b9-18f0-3884-9858-28bc8c4ef99d | -16.2953 | -52.9443 | 2025-09-02 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9bd20f09-eb0e-3493-975a-7ff3998cd0c1 | -5.7168 | -45.4035 | 2025-09-02 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| cb486f92-19aa-3659-9a4e-0d9956e474ad | -5.9037 | -43.3485 | 2025-09-02 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b233a7b8-e235-34f6-ab3f-02b07abfcf0b | -11.9415 | -50.6131 | 2025-09-02 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 4ec8ea5b-5c0f-3c5a-b9c1-54cf83251d92 | -12.8047 | -48.0627 | 2025-09-02 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 31ed96c1-47b6-3037-8ce8-ffd59ebda097 | -11.9876 | -51.3532 | 2025-09-02 14:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 4bbebc7f-ce36-3205-a2ec-1944105b6fe2 | -9.7483 | -48.9814 | 2025-09-02 14:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 21494478-044a-39fd-92be-600a1cf3d01f | -8.3291 | -44.9948 | 2025-09-02 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 447c7525-5375-35df-8afc-bd06ca362b0b | -12.938 | -57.0057 | 2025-09-02 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 494.9 |
| 93043898-7844-39d3-9041-02aad8c4e71d | -16.2949 | -52.9656 | 2025-09-02 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ab15f48f-ac0e-3d79-a13a-728168ee07b1 | -11.3496 | -43.6842 | 2025-09-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4943b010-07f3-37ff-bd56-5ffda1ae4d6c | -11.0841 | -44.6575 | 2025-09-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 4cc36766-f052-3f9a-9f82-9bcaff47bbd6 | -11.3709 | -43.5631 | 2025-09-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| c352dcac-608a-346a-80cc-3563de870b5e | -5.7359 | -45.357 | 2025-09-02 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2d2f8d16-321a-395e-82e3-2b94c5930305 | -6.9754 | -43.2326 | 2025-09-02 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 184.5 |
| 56b2d11a-4b96-3c21-a69d-ee8c41233224 | -5.8694 | -43.0003 | 2025-09-02 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 163.3 |
| e7d4592c-5c05-38ba-b2be-435f0b85fcec | -7.9163 | -46.4577 | 2025-09-02 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| d417978b-b9df-3103-ad21-9754bbe3969b | -10.8487 | -47.4546 | 2025-09-02 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| cf5914ac-62fc-3492-9681-045d01e8962c | -5.3974 | -43.3867 | 2025-09-02 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 8603cc3c-6754-36f2-8fd7-c9be5421ff37 | -7.6783 | -61.0908 | 2025-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 8437fb3f-6c31-3eb8-9838-3ae4d564d5b9 | -12.0069 | -51.3298 | 2025-09-02 14:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 298f0403-ee08-37cd-85dd-cc4dd9bfc6bd | -6.9632 | -44.3477 | 2025-09-02 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b32e8459-0e7c-37d4-b338-2aa0448964b5 | -12.9194 | -48.0909 | 2025-09-02 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f6d3f550-f764-370d-a347-9a0e5f40e120 | -11.1029 | -44.678 | 2025-09-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 4eb413ed-adcf-3d33-bc2f-e4a0fe70550e | -12.9386 | -48.0881 | 2025-09-02 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d6b01c1e-08f1-376e-8542-e02475e6fc86 | -11.834 | -51.4551 | 2025-09-02 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 5c264f94-f8ea-3206-b8d4-a57f66b64a54 | -9.4987 | -46.4749 | 2025-09-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| e3ef501a-8e58-35bd-a7b5-ae1666f52eee | -8.8854 | -45.7314 | 2025-09-02 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 49ae64c3-765f-35bc-9d05-7fcb07e38c1e | -9.4794 | -46.4994 | 2025-09-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 1ff873d7-fcd7-31c9-bb1b-7ae441d69347 | -8.4022 | -48.2864 | 2025-09-02 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| bc41a379-2a54-38ab-9cc9-e75da0852a82 | -7.1089 | -44.7703 | 2025-09-02 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2f3accf9-c6fe-3294-96d1-f67ad979e0d0 | -11.1033 | -44.6548 | 2025-09-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 409.8 |
| c21ddb7b-1f32-333e-9381-3ffb781b4a1f | -8.5943 | -62.6315 | 2025-09-02 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 49bda5e8-473a-331d-ba5d-b112455225b6 | -11.9879 | -51.332 | 2025-09-02 14:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 627fb06e-acaf-33ad-9cf1-374632a7653d | -4.9124 | -43.187 | 2025-09-02 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| c6e7335b-4f97-306d-81da-c529f0e984b1 | -6.2036 | -43.3709 | 2025-09-02 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 773e6ade-4edf-36e5-958c-23a80224abf9 | -8.2008 | -49.5345 | 2025-09-02 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| ab247a4b-e657-33f5-89df-ed3ad5481937 | -7.2296 | -44.0466 | 2025-09-02 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2812ac88-043b-3ec6-8d75-8f1c6c42f8c5 | -12.9189 | -57.0074 | 2025-09-02 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 3f4d5ad7-f556-3b80-8253-0ca2cae34656 | -12.9382 | -56.9856 | 2025-09-02 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 295.7 |
| 788bd2a0-f4cf-3dcf-89cd-610a4ccf68a2 | -5.717 | -45.3809 | 2025-09-02 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 988.1 |
| 378ad9b5-e065-30b4-bd26-0066da34ea72 | -12.9385 | -56.9655 | 2025-09-02 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ae9f4a0c-c394-3903-a750-c043a0f1fd23 | -5.8882 | -42.9988 | 2025-09-02 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 170.3 |
| 199fdf3f-a4ec-30d5-9fc7-c5f991849099 | -7.5476 | -61.3437 | 2025-09-02 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 241.3 |


[Clique aqui para ver as próximas entradas](README101.md)
