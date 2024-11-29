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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 573fa629-afe6-338a-ab4d-231b7caee66c | -17.63779 | -57.57518 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8b6ea2a0-f389-3763-93cb-95ee1d0a6737 | -17.6361 | -57.57664 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 58351a2a-e5c5-37d7-bfbb-8280de5cbfcd | -17.57799 | -57.60917 | 2024-11-29 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 62ca1031-ab64-3f9b-bc27-a6d4d8c52869 | -17.63829 | -57.57017 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| be772592-6bf6-3553-9128-276817406523 | -17.63657 | -57.57161 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fed4c3bd-8b2f-3d65-8608-ea8d96db24dc | -17.649 | -57.57298 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a8717f3b-b62f-33a4-a681-3f746133cf64 | -17.64451 | -57.57083 | 2024-11-29 05:50:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3c1930cb-ba8d-3c3c-acd5-511f0fbdfa05 | -2.6684 | -48.7767 | 2024-11-29 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 86a237fc-5c7d-34ef-80b5-7582ab842e94 | -2.9844 | -53.2819 | 2024-11-29 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| d031889d-c490-31ec-b438-bbee92440805 | -2.6499 | -48.7772 | 2024-11-29 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 28decdea-8ce7-3afd-986a-11a02dddb3d2 | -2.966 | -53.2824 | 2024-11-29 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1ac616d5-4e87-3040-95f0-f826a9cd0cb3 | -2.9844 | -53.3022 | 2024-11-29 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 550b68d2-ee8e-3107-8566-ce69c0d63d4d | -2.6683 | -48.7981 | 2024-11-29 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 0cdbb6e7-34c6-3d05-acd3-9058b6d5341e | -2.6498 | -48.7986 | 2024-11-29 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d32d748b-5eb0-3a9f-886e-25d73feebff3 | -1.6997 | -52.4535 | 2024-11-29 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 48b2d809-6c03-3466-85e2-0bb554515113 | -2.6683 | -48.7981 | 2024-11-29 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 989b7f7a-9074-3653-94a2-0fe20365b8d1 | -2.9844 | -53.2819 | 2024-11-29 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 44295286-bc7d-3ca0-bbb9-cf5e66f090d6 | -1.718 | -52.4532 | 2024-11-29 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c5357df7-959d-3ba1-831f-d7c4dcc104ca | -2.966 | -53.2824 | 2024-11-29 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0fd69d1f-e16a-3a95-91e2-11d6a73daca6 | -2.6684 | -48.7767 | 2024-11-29 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| c1d32c71-a357-3166-a827-e57ea59919b3 | -1.6997 | -52.4535 | 2024-11-29 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 83a9e719-ed42-34d3-8783-6e43b5191fff | -2.6498 | -48.7986 | 2024-11-29 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e3cc2efe-8ba7-373f-b6d1-f9d31f71eeb4 | -1.5869 | -53.8336 | 2024-11-29 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 148acf5b-7df0-3787-ae4d-e9019b733e14 | -2.9844 | -53.3022 | 2024-11-29 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 359fafb7-2dd2-302d-986e-f686d650c263 | -2.9844 | -53.2819 | 2024-11-29 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 1d7f74f2-9e4c-3f60-b7fb-0fc29ad63e4c | -1.6997 | -52.4535 | 2024-11-29 06:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| c8bc457a-60c5-32a9-be51-353d80ff4e33 | -2.6499 | -48.7772 | 2024-11-29 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6103d2a4-8f9b-3b62-ab99-abc21ecd7c2d | -2.9844 | -53.3022 | 2024-11-29 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 80909390-8e57-36dd-9143-1958a7617b24 | -2.6684 | -48.7767 | 2024-11-29 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 81bf653b-7fe8-36f6-bcec-6188bc96af00 | -2.966 | -53.2824 | 2024-11-29 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 865aad54-2e1b-3e10-95fd-f64f34a347f2 | -3.259 | -53.6388 | 2024-11-29 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0a90afe1-0faa-316f-ac3a-27e238e9743b | -2.6498 | -48.7986 | 2024-11-29 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5bb7f66d-e836-3980-8289-8a5c9f18fcc0 | -2.6683 | -48.7981 | 2024-11-29 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 210a7013-8eaa-362d-a4e6-74390da92927 | -2.966 | -53.3027 | 2024-11-29 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5fdf1bac-c758-3c6f-8bba-b8a6744161a2 | -2.7377 | -45.2201 | 2024-11-29 06:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 84d336b0-680a-3dc1-aa3a-c48714105c20 | -1.6997 | -52.4535 | 2024-11-29 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 81c3d95e-d594-37da-88d0-2f0c3bdd09b3 | -2.966 | -53.3027 | 2024-11-29 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e54e4d44-3344-3423-be5c-ce3412c495c1 | -2.9844 | -53.2819 | 2024-11-29 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 41f949fc-5ef0-3c0e-8485-a874b2682585 | -2.9844 | -53.3022 | 2024-11-29 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f41512a3-3d91-31a2-9b89-be2149b197b6 | -2.6683 | -48.7981 | 2024-11-29 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 269ee652-808f-3e2f-9722-5f94dd7fcdf0 | -2.6498 | -48.7986 | 2024-11-29 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 78b55500-bbf8-345a-8f72-744611bf040a | -2.6684 | -48.7767 | 2024-11-29 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7412e96d-ef65-35d7-8b83-85cf84874f2a | -1.5869 | -53.8336 | 2024-11-29 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1657ff02-d115-3a6b-889d-33e39a9fad52 | -2.966 | -53.2824 | 2024-11-29 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 17db0708-163f-3a82-8be4-c6484468dbf0 | -2.6499 | -48.7772 | 2024-11-29 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 77dd4eb1-b7cc-37f6-8af8-6c3ffd43b9b7 | -3.259 | -53.6388 | 2024-11-29 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| de18752a-909d-30bc-b4ce-fb40cf5d7059 | -2.966 | -53.2824 | 2024-11-29 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c0320efb-9248-387e-8a28-879211ad24c8 | -2.9844 | -53.2819 | 2024-11-29 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 5c914eb8-dbb1-36be-b515-5dbe92e50b39 | -2.966 | -53.3027 | 2024-11-29 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3c6411f5-eabb-357f-9b6a-5852ec0171ca | -2.7377 | -45.2201 | 2024-11-29 06:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c89c9054-b0af-3785-be2f-d160cfe0600e | -2.6499 | -48.7772 | 2024-11-29 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b85e3e4d-20aa-3325-8b30-15239b09b948 | -6.9723 | -43.5133 | 2024-11-29 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 27ced141-878a-378d-87f6-30588b64ba26 | -2.6684 | -48.7767 | 2024-11-29 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 74bbbf33-d918-3ce9-8896-b766c46e8cef | -6.9535 | -43.515 | 2024-11-29 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.3 |
| d8e053d0-b8dc-3b61-b8d6-00be3eebe5f7 | -2.6498 | -48.7986 | 2024-11-29 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 92936def-9055-3f55-ae4f-871830a8beaf | -2.6683 | -48.7981 | 2024-11-29 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 1dd12173-3cab-3df2-a200-a47bf2c836b5 | -2.7191 | -45.2208 | 2024-11-29 06:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 900886d4-1f2d-36b2-bfe0-76b0a544a95f | -2.9844 | -53.3022 | 2024-11-29 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2a61611b-3aeb-3dea-b83b-97773df44f96 | -3.259 | -53.6388 | 2024-11-29 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 52f5764e-27ee-3a4b-9dfb-04ff86396241 | -1.6997 | -52.4535 | 2024-11-29 06:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 7b1cf1dd-79f4-359a-9c07-b665165764fe | -6.9725 | -43.49 | 2024-11-29 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 970e901a-8c7e-3b7f-8a79-345d6fa76b7b | -2.9844 | -53.3022 | 2024-11-29 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f611e542-55ad-31ae-b2e9-e777f57eee96 | -2.7377 | -45.2201 | 2024-11-29 06:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 78f3c3d5-4ef8-3c45-b805-79f02767a5d9 | -2.6498 | -48.7986 | 2024-11-29 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fac03cac-9dc2-3659-97fa-aebf1da49613 | -2.7191 | -45.2208 | 2024-11-29 06:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| fc13208a-4c76-3dfe-9af8-816dda17a679 | -2.6683 | -48.7981 | 2024-11-29 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| f5a67d93-8950-372f-a5b0-82f655496a9d | -1.718 | -52.4532 | 2024-11-29 06:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b15346c5-ca79-3ec4-8831-3df0f2f0075e | -2.9844 | -53.2819 | 2024-11-29 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| feba9608-60b6-3ee0-9085-e8465c670d89 | -2.6499 | -48.7772 | 2024-11-29 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0a26fe01-594e-30eb-8b4f-0c4b2d36bd5e | -2.6684 | -48.7767 | 2024-11-29 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 014132af-acab-3797-a969-ccac52658564 | -1.6997 | -52.4535 | 2024-11-29 06:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 3842a031-5791-38c3-a25d-d291c457caae | -2.966 | -53.2824 | 2024-11-29 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| aa814f8f-c324-3e39-9616-faf91a7d4a4e | -2.7377 | -45.2201 | 2024-11-29 07:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c1b4d832-05d7-3384-9617-73948e87fc5a | -1.6997 | -52.4535 | 2024-11-29 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 78870eb3-a3c8-3cec-be10-2af00c919e90 | -2.6498 | -48.7986 | 2024-11-29 07:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 462791f5-44a8-38e0-87b2-24bcbc77e920 | -2.9844 | -53.2819 | 2024-11-29 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 381f0efb-85ca-3c68-8e53-f22dee4244d3 | -2.7191 | -45.2208 | 2024-11-29 07:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 131.8 |
| d7b34889-e59d-327f-b9ed-c2390f311092 | -2.6684 | -48.7767 | 2024-11-29 07:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 5dcf085d-9969-3ca6-bedf-3e57d0b517ec | -1.718 | -52.4532 | 2024-11-29 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e8efd3fb-8f66-31f2-b467-08e7300e1417 | -2.9844 | -53.3022 | 2024-11-29 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 20a4f429-b300-3c0b-9193-31b2a6b06f1a | -2.6683 | -48.7981 | 2024-11-29 07:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 050b9caa-7164-38c1-b4e4-f5c570058038 | -6.95 | -43.52 | 2024-11-29 07:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b16ccf8d-0029-30dd-bbdd-50e45dced075 | -6.98 | -43.53 | 2024-11-29 07:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a1e98e05-afb0-32d2-8dbd-db23aa58bcfc | -6.9723 | -43.5133 | 2024-11-29 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 579.9 |
| 28b5e97d-83f8-358e-bf79-30efd67613c2 | -6.9911 | -43.5116 | 2024-11-29 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 75c78ea4-221d-3627-a997-0c2db39183a5 | -6.9725 | -43.49 | 2024-11-29 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 1c400d30-61c6-370c-bfa8-832a9a5ff7b1 | -6.9537 | -43.4917 | 2024-11-29 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 98529e65-4a6d-3ad6-a089-155d60080f4c | -1.6997 | -52.4535 | 2024-11-29 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| df15b339-be13-3e18-9da2-e0473f05d4a0 | -1.718 | -52.4532 | 2024-11-29 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bfea1315-0833-3080-8bf3-e41f267556a3 | -2.6684 | -48.7767 | 2024-11-29 07:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| e2ef9904-b6b8-3724-9e5b-5b6a864e8ebc | -6.9535 | -43.515 | 2024-11-29 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 3c675311-0b94-35ae-8c06-49ec1ecd4663 | -2.9844 | -53.3022 | 2024-11-29 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| dc4b87fa-a7d9-3f76-88d4-e45715a639c3 | -2.6683 | -48.7981 | 2024-11-29 07:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 27bf12bf-44eb-38d4-9cdb-9d5d6ba7bf3e | -2.7191 | -45.2208 | 2024-11-29 07:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 07a52d7a-8c13-3b2d-bcc3-7cdcb21bd26e | -2.7377 | -45.2201 | 2024-11-29 07:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7093b17f-51e9-325c-a719-c111abab95f0 | -2.9844 | -53.2819 | 2024-11-29 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| c5466582-1eda-3ca7-9b86-a47d1743278a | -6.972 | -43.5366 | 2024-11-29 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 01e05cb7-cee8-38f2-8399-16a159c1ac53 | -2.6683 | -48.7981 | 2024-11-29 07:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 1b7f4771-86c6-3ba7-be20-a6c44366d243 | -1.6997 | -52.4535 | 2024-11-29 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| e66f016b-90c5-3392-81bb-5ea11a6c8042 | -2.6684 | -48.7767 | 2024-11-29 07:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |


[Clique aqui para ver as próximas entradas](README108.md)
