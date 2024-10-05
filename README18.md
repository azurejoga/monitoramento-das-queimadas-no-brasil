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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37945452-9a3b-3d55-9820-3d8bc354f2eb | -17.020201 | -56.724602 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 779e2d9a-f117-38a1-9524-3f19523ba317 | -17.021799 | -56.732201 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0e925d4-c977-35e2-ae65-1035ef3e342d | -17.023399 | -56.739899 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 472d1a33-45c8-3139-9afb-835e3b5bb9d7 | -17.0298 | -56.7705 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b55713ba-da9c-36c0-9d71-08d8ec4943d5 | -17.0315 | -56.778198 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac31c467-8b40-3af0-a481-cdfd1160f82a | -17.0331 | -56.7859 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a2e61848-bd04-3fab-97c7-a2c9108d90be | -17.0347 | -56.793598 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6aeada63-75f2-35d2-aa04-d5b1aa002bed | -17.1577 | -57.384701 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ade6f8c-a055-3188-928a-d4956de41c34 | -17.159401 | -57.392799 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62677601-4b64-373f-8949-19c894d92c2b | -17.160999 | -57.400902 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54a4e829-4be7-35ed-ab31-580c30ad35b6 | -17.008801 | -56.719101 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec9d5d09-b2bc-33db-9841-5c42f8869989 | -17.010401 | -56.726799 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af75830e-c011-3f15-bd43-1d70005bd45f | -17.011999 | -56.734402 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51602059-b360-3598-802f-49773036db51 | -17.02 | -56.772701 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf8aa46e-d3f4-30d5-89a9-201dce8e4470 | -17.0217 | -56.780399 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d2b5e33-0a48-37ce-9503-a81431b222fb | -17.0233 | -56.788101 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd58c089-0b99-3e59-bca8-3879247c6011 | -17.1413 | -57.3545 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e1e3cdf-a040-38de-96fa-9037b6146bc7 | -17.1429 | -57.362598 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c0e69e8-0c2c-32b9-a807-e977ba2b924c | -17.1446 | -57.370701 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8b634ae-b8f1-39a6-90cc-df927938ca97 | -17.1479 | -57.386799 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6cc0c2fb-a272-3d7e-bc2d-36cc1d87a8de | -17.149599 | -57.394901 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a2998f20-0e79-38f3-b875-dd74aef6ce88 | -16.823299 | -55.894699 | 2024-10-05 01:07:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18faa285-bb34-39ec-9816-08eaaf21508f | -16.999001 | -56.721298 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 717ffd41-30cd-32c1-bc2c-08e43f5ed71a | -17.000601 | -56.729 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d83427f7-cde0-39d0-bcaa-63393b4caa41 | -17.002199 | -56.736599 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1e129ba-a154-3fe6-83a3-4f6fe9f03c15 | -17.003799 | -56.744301 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76a1ea12-79b3-371c-b9b6-ddfb22b3aeb9 | -17.0054 | -56.7519 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5e8cadc-306f-314f-ac1d-bf7c429dbf02 | -17.0086 | -56.7673 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad595a79-3b39-33cb-8426-a7f554addc72 | -17.010201 | -56.774899 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 87ab993b-5289-347d-939b-7d60aa99278a | -17.0119 | -56.7826 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bee2c8b3-7c11-3650-89da-7c715bd6e8f9 | -17.1348 | -57.372898 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d12249c9-ec97-35d1-81ca-05467ca8703e | -17.136499 | -57.381001 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 413295b1-aaf0-3d17-8636-ea7ea17ea768 | -17.1381 | -57.389 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 865ee2b6-82c9-3441-9a3b-9af05ffd0a05 | -17.139799 | -57.397099 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f8e3e5d-0fa2-3d01-acef-6d11c96aaa0e | -17.1415 | -57.405201 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ca22386-ef3b-3cf5-b72e-d71eae6c479b | -16.812 | -55.889599 | 2024-10-05 01:07:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5114ef43-5cb0-396a-b193-2ca2393ddb60 | -16.813499 | -55.8969 | 2024-10-05 01:07:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 27e841d6-533b-3f66-969f-dcb18c173673 | -16.990801 | -56.731201 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb478a7b-6ffc-3e81-b48b-9054a0137dc3 | -16.992399 | -56.7388 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1861810a-68be-394b-90c3-909b9d6f779a | -16.993999 | -56.746498 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68f40c77-34a5-31e1-b5d2-688368a301ba | -16.9956 | -56.754101 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6596244-5b37-3207-b37b-5e94db03c611 | -16.9972 | -56.761799 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7ca97e6-5933-390d-942f-300046c9b85c | -16.9988 | -56.769501 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3edb925e-06ec-376b-9f39-96ca134a8adc | -17.000401 | -56.7771 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c38e7bd1-bf73-3961-9a7e-f0849deae30e | -17.0021 | -56.784801 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b54cede8-9ef5-36a1-ae42-f43110a24f8e | -17.123301 | -57.367001 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5bae0997-f698-3621-aa2f-c36479a08f0f | -17.125 | -57.375 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b217e64-287d-3797-a4bf-e47dfafb34fc | -17.126699 | -57.383099 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b08340cf-1f93-3fbb-9bf8-ded2e912436c | -17.1283 | -57.391201 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1e45f40-1a2a-3837-85ab-cde59201338e | -17.129999 | -57.3993 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ecf560e7-a9e7-3074-b4fb-e36c9492d809 | -17.131701 | -57.407398 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c007f929-0c16-3243-bda5-a81b44ad1fac | -17.1334 | -57.415501 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f62e81e-6cc6-3f6d-9ae1-32c648b970d8 | -16.9842 | -56.748699 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa376afc-34db-3c85-8656-b10c98fc6b13 | -16.9858 | -56.756302 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b638d054-aa30-347e-bdb6-9ca04a5f0fb5 | -16.9874 | -56.764 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c21c1a9-1f3a-3df3-9fa8-86bae385f7df | -16.989 | -56.771702 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b0e1e358-0f33-3c0e-8fef-493b9c11eb2f | -16.990601 | -56.779301 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 126791ac-fd22-364c-8245-53a179d73948 | -16.9923 | -56.786999 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 887da529-a047-34c1-8660-65b8ff63f52e | -17.116899 | -57.3853 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acbcd6f0-fede-3fc2-b2f7-f73afb88ec24 | -17.1185 | -57.393299 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61b695d9-fc22-3b6f-ae18-ec11064e57d8 | -17.121901 | -57.4095 | 2024-10-05 01:07:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7cfce3a-02d6-32d2-b584-dd0035296ede | -16.9744 | -56.7509 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 14fde531-9eba-3133-900a-a53e184f0b69 | -16.976 | -56.758499 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f429fc71-d6d3-3caf-b22e-6469bd625fd9 | -16.9776 | -56.766201 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 637d7fc6-f506-3539-bc1f-0fb5f7ec46d3 | -16.9792 | -56.773899 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6b7a831-2c0d-3249-9420-ed02f124568f | -16.9646 | -56.753101 | 2024-10-05 01:07:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4ab120b-1850-3731-8eb5-85e502aaf64e | -16.9662 | -56.7607 | 2024-10-05 01:07:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5613721b-047f-3317-bbaa-56e71c9d30db | -16.967899 | -56.768398 | 2024-10-05 01:07:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e00313ae-78ef-3529-9d22-9f7d06e0ba68 | -16.9695 | -56.7761 | 2024-10-05 01:07:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62b44c8e-9d5f-3631-aade-f00835b0bf4d | -16.9711 | -56.783699 | 2024-10-05 01:07:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9731458-8d48-3bb0-ac72-2fcd9ef50cff | -16.680799 | -55.472401 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fbb0a4a8-57f3-3864-9ac7-3e7e2857b782 | -16.6824 | -55.479599 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76be546d-03d8-303c-9956-9039b6377fda | -16.683901 | -55.486698 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 270b761b-5ed0-3e88-afbf-42923e7de50e | -16.958099 | -56.770599 | 2024-10-05 01:07:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca161d15-e04c-3e94-b9b3-2b9cc414f828 | -16.671 | -55.474701 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c63f128-8d1e-3b8b-a9e0-e452e140d06a | -16.6726 | -55.481899 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 171fa407-a8a9-38b7-9654-0a8d8860122e | -16.674101 | -55.488998 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 913d2784-4a9a-3875-a816-fdecd4c95cc4 | -16.6628 | -55.4841 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f01c78f-2671-30a1-9015-c46568deed54 | -16.664301 | -55.491199 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a29f0415-720a-399d-abb8-022b5b5d3b89 | -16.665899 | -55.498402 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7668c448-6a31-3fc6-92e8-44f8ab4751cb | -16.6674 | -55.5056 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 957d1f3f-dd04-375e-981f-056c79545448 | -16.6737 | -55.534302 | 2024-10-05 01:07:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05908671-fe3a-3405-b17f-32d1d33ab311 | -16.6752 | -55.5415 | 2024-10-05 01:07:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec48e1aa-cae8-3e06-9fb6-54370f5e08d2 | -16.653 | -55.486401 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3777b3be-083c-3532-94f0-ad82a275eb96 | -16.654499 | -55.4935 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88365e04-4e6a-34a8-9009-81602be6da07 | -16.656099 | -55.500702 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52945ba2-f297-3628-bb4f-7bedbc2c9792 | -16.6576 | -55.5079 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee534a4b-6a02-3301-bb86-0812d1727625 | -16.659201 | -55.515099 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8d0c79f-82ca-3306-8f67-9d8837ca6bb8 | -16.6607 | -55.522301 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e685a84-1ec0-3951-a14e-7ba017fba02b | -16.6623 | -55.5294 | 2024-10-05 01:07:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c4ca090-7f8d-334f-99fc-14d995d73ad6 | -16.6639 | -55.536598 | 2024-10-05 01:07:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6b81a6a-6611-3a00-b6ce-145124f4c9dc | -16.6478 | -55.510201 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96160214-6b8e-3d04-ae80-2be5370ddf9e | -16.649401 | -55.517399 | 2024-10-05 01:07:51 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 94aecf98-77a2-34db-9be2-e99ae999e6c5 | -16.6509 | -55.524601 | 2024-10-05 01:07:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f6ca4a8-8206-3ca4-8224-0d9052a92a0e | -16.6525 | -55.5317 | 2024-10-05 01:07:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cacebf1f-425e-3c59-9d79-f0db6dfbe884 | -12.7557 | -50.550098 | 2024-10-05 01:08:36 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36616754-e82a-3b90-838c-1feccb007667 | -12.7583 | -50.560902 | 2024-10-05 01:08:36 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c07ca33c-fe55-3834-acad-a89b40d7bf85 | -12.761 | -50.5718 | 2024-10-05 01:08:36 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8bc70f67-3594-34ad-b24d-1f664a21e635 | -12.363 | -50.9758 | 2024-10-05 01:08:44 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 560b25ab-6dcc-3502-b7da-19e04ba55f7d | -11.1582 | -46.9034 | 2024-10-05 01:08:47 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
