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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43882454-400f-3c04-96b2-1f8f3f12c3c0 | -4.12559 | -51.07481 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8cc61169-ded4-349f-9ec1-c8fe2cff3a18 | -4.12506 | -51.07826 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4f06c5e-966e-3cdb-a1e8-d40d1e1a5bcd | -4.12229 | -51.07428 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5ee1edd-306c-32ff-ba5b-94a2c986eeb5 | -4.12175 | -51.07773 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62300973-66aa-3489-9c38-29760bd0be59 | -4.11978 | -50.98203 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bf0eee8-0ee1-324e-b964-77383805d546 | -4.11925 | -50.98549 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84694500-9f61-343e-920b-5f776fb92ddf | -4.11871 | -50.98893 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9afa7e9f-c5a4-3d81-81fa-ecc116707981 | -4.11594 | -50.98497 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11732526-2093-3181-9b85-0c3fc407117b | -4.00179 | -51.04076 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ba824ab-7e0d-37e4-94a0-4c334dcaa69b | -3.86189 | -51.28181 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41da94e8-9eb4-397d-be21-959e725a6a34 | -3.86134 | -51.28529 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e31c6e9e-2deb-3474-a5d6-675203d8c7b0 | -3.85857 | -51.2813 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67381719-65d4-3442-9d43-17fa91549b27 | -3.85802 | -51.28477 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b467e60-1ffe-354f-9b1e-c06dfc7fd3ba | -3.78669 | -51.32722 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e845c020-1cb4-3896-a7e3-ecd2dbf9c941 | -3.68179 | -51.2148 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac0539ce-60ef-335f-9646-eb1af948cd81 | -2.05789 | -53.25443 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b53754e-d11d-3693-811b-debeb5ea8229 | -2.04965 | -53.23616 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 753b7340-0dce-3b10-b2b8-699edb256b42 | -2.01391 | -53.2989 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49764b7a-8af3-3fae-b5ce-41595ea6cab4 | -2.01029 | -53.29834 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1bff4e82-845e-3744-8812-7c82551297fb | -2.21794 | -51.9569 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 868cfed5-209c-306b-8053-286eb70b3aa2 | -2.12217 | -52.70245 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51bf203d-7441-3dcd-aa3a-540b667e3f83 | -2.08251 | -52.47787 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 275a0ab6-e0fe-3fc3-8ad3-783d05cf3251 | -2.07845 | -52.04075 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8db5e1ae-dc8d-395e-a182-98b6bbd0eefd | -2.07453 | -52.02121 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 312b7881-6d70-3187-bdd7-0b844c2d90d3 | -1.94645 | -52.00949 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48ae49a4-e776-3730-adfc-2d4ad8f738d5 | -1.93071 | -52.67375 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09bdce33-8879-3ab5-8836-cef53c16eb97 | -1.93009 | -52.67772 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33d2fafd-bf47-3402-b5e7-7ed68985c2ba | -1.88941 | -52.12677 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7f4c58e7-7ea6-3610-978b-af7613b9a627 | -1.88883 | -52.13051 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fe4521f9-68d3-3842-a616-e2f142782d3b | -1.88824 | -52.13426 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9061f124-9b24-3330-a663-0a26bb19b918 | -1.88597 | -52.12625 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2c4e74f0-e279-3c22-a897-6f8c241303b7 | -1.88539 | -52.12999 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 906fb21d-7ef5-3118-aeb4-77a6dc19bc91 | -1.8848 | -52.13373 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a16b9934-4bb0-3da3-bd88-7665a2fb3c90 | -1.88253 | -52.12573 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4845491a-5948-35d3-8824-54f2fe875389 | -1.88195 | -52.12947 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8368f837-2dd5-31f5-9e93-66dd7bc42e54 | -1.87893 | -52.17129 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4167b1b-faa8-31a2-a663-32241f17e666 | -1.87835 | -52.17504 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88905ac8-4808-3728-b6e0-37960b3f3027 | -1.85063 | -52.32965 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a83a4f28-9132-3290-a684-0b48550dfbd5 | -1.85004 | -52.33345 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c8e49b3-0cfd-3716-ae61-1d939023e800 | -1.84094 | -52.18855 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64bc93f5-71f3-328c-bcb7-6cff92da62c0 | -1.83689 | -52.19181 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4d6d12e-05b6-30f1-8e2f-ff65693ff6e2 | -1.82031 | -52.27439 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88ca4607-03c1-3e13-ac82-94c2a4b63a07 | -1.82008 | -52.41106 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5193c6fc-50a6-3300-b350-50bc9a5b2bb6 | -1.81805 | -52.26629 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20273520-a235-3986-989c-16319b5e0d46 | -1.8166 | -52.41053 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bc14eeb-0d06-3611-b80f-2383d3132599 | -1.72916 | -52.34212 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd954953-ac24-3ab8-8b15-dcbcbf5e06e8 | -1.72856 | -52.34594 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b019ec5e-0b5d-3a92-9907-a541bf838a2b | -1.72796 | -52.34976 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce1d602f-7a51-37b8-8a8f-f33bdf5c0165 | -1.70911 | -52.49269 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75eefbd8-b543-33c6-b694-34c2ea9e0dce | -1.70562 | -52.49215 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a142a046-a3ca-3734-a380-a97e1b7b38a8 | -1.6961 | -52.34878 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3332344-2d99-3ae9-931a-a801eca1b543 | -1.69263 | -52.34824 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d50190ca-e599-3d88-a80b-ea4ebb984bab | -1.68915 | -52.34771 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec2985a7-eddf-3541-a372-1d5cb03b4af9 | -3.57336 | -52.51432 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f1cb39-d80b-3bd2-a81b-1ce542e7902b | -3.54579 | -53.12836 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec84cc1b-238d-3c8c-9781-ddd693e79b37 | -3.52275 | -53.62084 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b505be33-b886-39ce-812d-da32c0a672bc | -3.51916 | -52.74601 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fd7ea05-e819-3383-bcfc-d16958520121 | -3.48777 | -53.03566 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ec40d48-269c-3a24-8b09-461cbcc08392 | -3.48426 | -53.03506 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a01672-3cec-3962-8bdb-fbb2b6ce84ee | -3.41939 | -52.39896 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e9bfdc6-1c2c-329e-b129-bb28f50228fc | -3.41879 | -52.40271 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0f0239c-c588-3064-944c-6b22408e91eb | -3.39664 | -53.68431 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26be7004-4830-36cb-ab36-72957bc15d64 | -3.37834 | -52.41495 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f4836e1-10ad-3f44-866b-a3f05b3133ce | -3.26558 | -53.40516 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5856f209-4b62-364d-9e4e-25d3d3f97eca | -3.26425 | -53.41342 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72e74ccc-25d1-3bfb-b524-f179837cc3c8 | -3.26199 | -53.4046 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3079878d-d3aa-32fc-95a9-337f95083118 | -3.26133 | -53.40873 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad8efca6-f2c8-38e1-a987-be2259dbee44 | -3.26066 | -53.41286 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a5b4cbc-d3a9-3160-9e56-bf23d879d280 | -3.26 | -53.41697 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 086cbb2a-94f8-3f03-8a49-866800d866b4 | -3.25774 | -53.40815 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2490b5f2-ee68-3338-994e-ce1a5f439a84 | -3.25708 | -53.41229 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e09719a1-9f66-305d-bc76-dfff9adf522f | -3.25641 | -53.41642 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b4185e-f9e0-39b7-9979-9403b8292afb | -3.25416 | -53.40757 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d29560bb-86af-38f9-934b-f2a408bb20bc | -3.25349 | -53.41172 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5f8278a-119c-357c-a2b0-29300394300f | -3.25282 | -53.41586 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18ef6e09-5ea8-3cf5-aa28-779bf098c645 | -3.25057 | -53.40702 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08b9b4e8-44f3-340f-b492-81c8590c8a76 | -3.2499 | -53.41116 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70022d7a-0239-3492-9acc-00b1d6264114 | -3.24698 | -53.40647 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f9830ff-34bb-349d-b5a4-e720b7f11318 | -3.24631 | -53.41061 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca2eb5de-7425-3826-b438-087a3e7fd048 | -3.24406 | -53.40178 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54b764bd-2aff-3aa6-a32e-e1e3d5879576 | -3.24339 | -53.40593 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93de657a-7673-3013-b4a8-3eead83db1dd | -3.24272 | -53.41008 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5fbe850-24ea-3bb7-87fd-67f7e899b031 | -3.24195 | -53.40173 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ca38e21-bc19-31d6-aec0-254b1ea9a961 | -3.2413 | -53.40589 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7109eb5f-525d-3084-b322-59cfdb8dc267 | -3.24047 | -53.40124 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3db5628c-f886-360e-a8b5-3bd04ee14f8e | -3.2398 | -53.4054 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7551ab0-14f4-3d87-bc7d-3b8ec0cfbe54 | -3.23836 | -53.40118 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb95e72e-3bfe-35d0-a24a-c7238e85af8b | -3.2377 | -53.40536 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3431ffbb-ba6e-341f-85ed-d127d8a124d6 | -3.23706 | -53.40951 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63b5b8e2-a017-31b5-8e44-0a25620e075c | -3.23688 | -53.4007 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9318bb59-2b40-3441-8441-4edff92e7b64 | -3.2362 | -53.40486 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0f0ef8a-d0fa-3ac8-a939-7b43eb4df0f5 | -3.23553 | -53.409 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d8163f0-9b5a-302b-8bc2-7e28839bde38 | -3.23477 | -53.40064 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5684071-31d6-3379-8f07-92f7bbc5f513 | -3.23411 | -53.40481 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89fe110b-5294-3b74-a36a-29a942371567 | -3.23346 | -53.40897 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfdc375d-beec-374d-b5eb-5e06d263e41d | -3.23118 | -53.40009 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f46ce0c-115a-3135-aa58-e626d9641d49 | -3.23052 | -53.40427 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeee3ab1-49c9-3750-bccd-068b4ad7f67c | -3.22824 | -53.3954 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5da2d06-4f39-3a84-8df8-c1b834cf9c54 | -3.22759 | -53.39955 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6d48a25-5301-3b24-847c-cbe987784cbe | -3.22693 | -53.40371 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README55.md)
