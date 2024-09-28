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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cde45900-8f34-38bf-a036-ab9792650ed4 | -17.79178 | -43.2696 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bacdf26-ec79-30b9-989c-9657a9cfdd55 | -17.79052 | -43.27903 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e12becc4-fab4-30fa-8824-38aea5e575d9 | -17.78868 | -43.26425 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c90cd6e-0870-3b5f-a185-22c41dee9f7d | -17.78238 | -43.28266 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6b3d6f7-bf5d-3111-af78-68b079419726 | -17.4694 | -43.02505 | 2024-09-28 04:23:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adcd5cd4-c189-3bba-88c4-c59e47a5dfa7 | -17.80114 | -43.28526 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35ba184d-f080-3463-86bb-99dcce86ecac | -17.79993 | -43.26588 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| dda992ac-43d3-3196-ba55-778c174ff578 | -17.79616 | -43.26548 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9561d957-c7bf-35c8-bdab-afebf641fd9f | -17.78988 | -43.28374 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 836fe5b2-b911-3734-90ac-1ccce8b317af | -17.78493 | -43.26368 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 952398d7-9a64-3ced-84ee-9f459ba08701 | -17.78181 | -43.25837 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba1dc1db-a9fc-35f2-b90e-8f06dc9183fa | -17.78112 | -43.29205 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8491816d-e3ae-3a8b-a2c3-91fd2f8d9116 | -17.46916 | -43.02749 | 2024-09-28 04:23:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f6bb5a5-92c8-355d-9a75-12f4e2f346e4 | -17.79553 | -43.2702 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8d37140-563d-347f-b7f5-1451af856c1a | -17.79115 | -43.27431 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cb5d8b2-a48d-3964-a78c-1cac0864f7ce | -17.78804 | -43.26899 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 411c99ee-fa69-3ac3-900f-90f35a4d0d9d | -17.37372 | -43.13475 | 2024-09-28 04:23:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f1b3fd78-f523-3087-9321-1a9bd677e338 | -17.77806 | -43.25775 | 2024-09-28 04:23:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb824caf-6f95-318f-938d-b6d8cf917441 | -17.37434 | -43.13012 | 2024-09-28 04:23:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f6a86fc5-a454-380c-8d1d-89a1cc5997c7 | -18.73142 | -43.84993 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61476392-04f6-3a9d-bcc2-20d6d1c3fb00 | -18.73075 | -43.85473 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62acc0f2-1c34-3a9c-8047-37a5f9754a83 | -18.71179 | -43.91077 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3bc4b40-48c2-3a4d-be78-c385527f8654 | -18.71119 | -43.91508 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54090ae2-d516-369e-b13e-2a7a4329e2b0 | -18.52179 | -43.8818 | 2024-09-28 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d75fe3e0-5632-39b7-8274-c4e133b0a142 | -18.50283 | -43.88385 | 2024-09-28 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bea6a785-19f1-302c-b59b-df38ae9b769c | -18.47797 | -43.8472 | 2024-09-28 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 721ecf61-c36e-3029-9e07-d479937371fd | -18.4743 | -43.84672 | 2024-09-28 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4fddc77-2136-33b8-a494-ade9c69b574a | -18.36978 | -44.0097 | 2024-09-28 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 555518f0-0d1c-3b5b-8a9e-bb2b34fedcdb | -18.36556 | -44.0134 | 2024-09-28 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 06d60449-97a1-3bd9-a892-ee7eb9eae062 | -18.36194 | -43.9591 | 2024-09-28 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbfa3752-1b1d-3f17-bea2-c65c44ca61bc | -18.36193 | -44.0129 | 2024-09-28 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ca536c8-7afa-3350-a403-ea9f186f72a6 | -18.36011 | -43.99922 | 2024-09-28 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45f663e8-204f-303a-88f3-93819c0762d8 | -18.35952 | -44.00351 | 2024-09-28 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d45c74ff-f6b0-36ca-93ff-38d00e17b340 | -18.35893 | -43.98089 | 2024-09-28 04:23:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5b95fac-2a5d-3c65-8612-106aa06b4860 | -18.18767 | -43.92247 | 2024-09-28 04:23:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68cec1c8-7f8a-346d-8dac-7dfb6105b4c6 | -18.05555 | -44.34329 | 2024-09-28 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8723388-147f-312d-a98e-992a80bbba82 | -18.05431 | -44.37848 | 2024-09-28 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 021febde-1657-37c9-9459-945f6514e585 | -18.05371 | -44.38278 | 2024-09-28 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 315d3ffd-3935-3b4b-8ab6-b669a00e5979 | -18.05311 | -44.3871 | 2024-09-28 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f4f5b6e-2ad8-367c-83ac-f3d4dc4eddbe | -18.05076 | -44.37791 | 2024-09-28 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| db91472e-cbbb-368d-b903-fa7925d179f9 | -18.05016 | -44.38221 | 2024-09-28 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 923cedcc-fa9c-30af-a19b-ed88ca1f5291 | -18.04956 | -44.38655 | 2024-09-28 04:23:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3996347f-9894-3dc5-bb5c-cf5532a1a416 | -18.01609 | -44.31875 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 31bae688-e5fe-3e4c-a6ec-6fb6616b12a6 | -18.0155 | -44.3229 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 70c665e6-b6b3-3e19-a958-b219d95b5478 | -18.01491 | -44.32704 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0f935e6-ae59-3916-92bf-afecb888604c | -18.00838 | -44.32182 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee7601e-fec1-30da-a238-3c758381a47c | -18.00779 | -44.32598 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2c9a12f-817f-3a10-ad6e-7eeee4f9adfb | -18.00112 | -44.47472 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f63658fa-96b2-3c98-a425-2e8d51e61f62 | -17.99831 | -44.34154 | 2024-09-28 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29b0ea55-b3a0-3a05-9b1a-74c391c0aba8 | -18.60403 | -43.4025 | 2024-09-28 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9dc2c3b3-e981-34e7-8072-0e20acf5db37 | -18.60341 | -43.40725 | 2024-09-28 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 23f8332d-d708-394c-90db-582031b371fa | -18.60282 | -43.40553 | 2024-09-28 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5be20d9e-1227-3589-8b29-6de7e298ca83 | -18.60217 | -43.41025 | 2024-09-28 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 83e0deed-6f07-3300-9f06-0e27c982c1b7 | -18.59965 | -43.40668 | 2024-09-28 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 53185d43-968f-327c-9d0d-bf3ae87b058a | -18.59904 | -43.41135 | 2024-09-28 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 32ecaf48-c296-358b-b365-4581875d14a0 | -18.59842 | -43.40964 | 2024-09-28 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b63eca4b-eb33-3af1-8825-26a42884a585 | -19.24203 | -44.37329 | 2024-09-28 04:23:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afc9a0e0-00c8-300d-9393-83f36cdbd894 | -19.24085 | -44.3819 | 2024-09-28 04:23:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a97275d-558c-34d9-9160-343da1496710 | -19.22286 | -43.71138 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea16715a-2138-3679-bd26-fdf3a5a6c3b0 | -19.10632 | -43.4529 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94ac976a-aea1-3aa8-b100-5dbed9dca5b8 | -19.10255 | -43.4523 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69fec4ac-d0a4-3a19-9c73-74187347061b | -19.09881 | -43.45153 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad273a02-4be7-3039-8291-91f21c50194f | -19.09815 | -43.4564 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48ed3a5b-4394-3cc1-b343-538f83c1f8f3 | -18.95218 | -43.50932 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38b4cf09-f802-3d85-80b1-b2efc52d14f2 | -20.11709 | -44.49344 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7c11eb4a-0402-3243-8f6c-44cc619540fa | -20.11649 | -44.49783 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 66a99ebb-587a-3160-b0e4-d547492ea697 | -20.11407 | -44.48851 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b427cb2e-a1b0-3f00-b3cf-6522e7d532a0 | -20.11347 | -44.4929 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2da09198-b1dd-3b1b-b927-7cbb8e975458 | -20.11287 | -44.49731 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 32be385e-c708-376a-955e-4bc64e55e19f | -20.11047 | -44.48783 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 18a717d9-16ab-3f43-8562-6955952541f3 | -20.10987 | -44.49226 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| eee6dd2a-3112-3500-94ca-1b5768d63163 | -20.10627 | -44.49158 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9bef4d3d-7741-3a92-a844-212ffceaab1a | -20.10266 | -44.49092 | 2024-09-28 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dd2be650-66a9-360b-95da-744272475b73 | -20.91388 | -43.90609 | 2024-09-28 04:23:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 00b6d04d-9a54-3cfa-ac7a-e92402e31093 | -20.91353 | -43.90364 | 2024-09-28 04:23:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5c3e5611-1f57-3b72-ae36-a4e2849c9e5b | -19.81583 | -44.05052 | 2024-09-28 04:23:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cff1d421-810f-3a2e-bd36-e3607c1f4abd | -19.81477 | -44.05225 | 2024-09-28 04:23:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56f09773-49c4-37ce-82d3-8cb042c6da36 | -19.79416 | -44.20729 | 2024-09-28 04:23:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6a233e3-8a04-3bcd-ab5d-cfceb16599b5 | -19.79373 | -44.20982 | 2024-09-28 04:23:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e48234c-0a5d-3008-93cb-041cd8fa43e2 | -19.79068 | -44.20491 | 2024-09-28 04:23:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 378766c6-11bc-3808-8315-3dc095544509 | -19.7905 | -44.20681 | 2024-09-28 04:23:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c50e61a-018a-328a-ae96-7185cfe55d26 | -19.77973 | -44.28744 | 2024-09-28 04:23:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fa21f18-c858-30de-bba0-18f2a034c963 | -19.76772 | -43.70405 | 2024-09-28 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ea41ee2-8881-3546-8bfd-f43412525c15 | -19.76395 | -43.67439 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9dd3054-ec76-3315-af40-b10b21f5c54f | -19.76287 | -43.67725 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5043be94-4e8a-3396-ba1c-8b8f750efbf3 | -19.75957 | -43.67863 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a14ce9e1-e526-3ca5-a8ce-f630a300aaba | -19.75896 | -43.68328 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f7c33ce-23a4-38b7-a38b-7fa777bfab0a | -19.75848 | -43.68135 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b56227-4771-3636-9d62-5ef6db668001 | -19.75785 | -43.68597 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ce4c44f-9424-3ba4-b6ce-eb449ddd1312 | -19.75578 | -43.64883 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2119fdb3-7978-3a6f-a017-ca6da0c5eae9 | -19.75549 | -43.647 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d02fdde5-ce30-3f24-a642-5fcd4494676d | -19.75487 | -43.65157 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95bfd694-c5a9-33d5-b6c0-76c469092dd9 | -19.75173 | -43.64644 | 2024-09-28 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90f7f8be-db21-399d-a61b-b9a2a003b3d8 | -19.74778 | -43.96931 | 2024-09-28 04:23:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdbb0f14-2afa-305c-a3a8-697df35bf363 | -19.69111 | -43.89659 | 2024-09-28 04:23:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c156787d-cd3f-3fc1-b366-68ac0ade5ecf | -19.69047 | -43.90133 | 2024-09-28 04:23:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc3e7140-8a5b-3ce2-ae71-af40511b74f4 | -19.65349 | -43.80952 | 2024-09-28 04:23:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2289924-c718-31c4-8a62-f87ae24af453 | -19.64001 | -44.18902 | 2024-09-28 04:23:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f8edf03-e2d6-3712-818a-103176a0a795 | -19.63939 | -44.19353 | 2024-09-28 04:23:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28381379-9a70-3353-a030-54cbf417e80a | -19.63575 | -44.19293 | 2024-09-28 04:23:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README63.md)
