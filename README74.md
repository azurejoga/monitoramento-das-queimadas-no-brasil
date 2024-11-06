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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12083a5e-0a2c-37c6-87ba-442a246bad38 | -3.0396 | -53.2805 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9861be9f-9360-3ed2-8be4-8b7eb192a272 | -2.8386 | -52.8794 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 966c056e-933c-3163-be23-a248573b9293 | -2.8017 | -52.921 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| f6ef69e5-fc01-30a9-8c20-686fc6293aae | -2.8385 | -52.9201 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 193.9 |
| 6e9c9570-7410-3aa8-aef7-27c35093e4df | -2.764 | -53.2062 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 5f92ee71-5583-3159-921f-3dccac716f5f | -1.2922 | -54.5585 | 2024-11-06 14:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 317.4 |
| f2b6ece4-f5b5-36d6-91e9-8df5153ee81e | -7.2241 | -42.8797 | 2024-11-06 14:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| d6a0b127-31dd-301f-a730-84601374a352 | -8.5002 | -42.0747 | 2024-11-06 14:10:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 587ee50b-52ec-3317-b4e6-eb56ddad5d3c | -2.9371 | -51.0465 | 2024-11-06 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| bf023434-a822-36c5-adc5-e9bd8d2751c1 | -1.535 | -52.0053 | 2024-11-06 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 3b53fd6e-7fe9-3a00-9840-d55bde7e7220 | -2.8202 | -52.9002 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 27974a05-80e3-3bee-8d62-6e803caaa048 | -2.7456 | -53.2269 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 93a788f7-d515-3b30-afb9-24ec4abd4278 | -1.8258 | -53.6489 | 2024-11-06 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 81919ebd-5752-3798-a249-3e73659e48d2 | -7.7938 | -44.084 | 2024-11-06 14:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c5888902-a7c6-370d-8894-802951c7cc65 | -3.1393 | -51.2069 | 2024-11-06 14:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e5555695-bd52-309f-b3f9-d8fe4095657d | -1.4244 | -52.1913 | 2024-11-06 14:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7774edd1-58d1-3050-89af-d26e69135776 | -2.7456 | -53.2067 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b9d666ed-ad51-3d89-a287-731010e06634 | -3.1213 | -51.1036 | 2024-11-06 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 900f4abb-8d69-35a1-ba3f-9064459771a5 | -1.802 | -47.937 | 2024-11-06 14:10:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 6fc60fef-6943-3d0e-bbe2-83e73fde6fd6 | -2.9186 | -51.047 | 2024-11-06 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| ab38e63f-3353-345d-a757-3a0573367544 | -2.82 | -52.9613 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 63ac3004-5230-3226-b335-98499076553f | -8.1281 | -44.4883 | 2024-11-06 14:10:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| cd83b433-0d16-3725-8cbe-bf99888eda2c | -2.8321 | -49.4749 | 2024-11-06 14:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 626a52bf-d247-3779-b177-cb48e589ddd6 | -1.5348 | -52.1489 | 2024-11-06 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 8fbabe0f-6e9b-3c34-ada1-544b0836fa2a | -2.7243 | -54.1552 | 2024-11-06 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 200.7 |
| c6a93ccd-5feb-3a63-b046-43b3b0a08261 | -3.0023 | -53.4232 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 4e6293d5-9ed5-3693-8d88-c90ef3157a78 | -2.7243 | -54.1552 | 2024-11-06 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 6b599fc1-a0e2-3ec8-9fe7-30d43512b98f | -2.7456 | -53.2269 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| af7bed7b-e076-3a3a-a142-d01c148a8648 | -2.9186 | -51.047 | 2024-11-06 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a4396ebd-7e2c-3c37-8717-0e3d82c6efaa | -7.2053 | -42.8815 | 2024-11-06 14:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 9833664a-a276-3275-9e69-10e9d367dfa3 | -3.0207 | -53.4227 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| d6ff11cc-dabd-3281-a134-21f637306257 | -7.7938 | -44.084 | 2024-11-06 14:20:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| efdf8df7-4fda-3978-bec8-1254e50977a6 | -3.0396 | -53.2805 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c9448149-e80c-3a97-a713-33e67fa41e2e | -6.9424 | -42.8126 | 2024-11-06 14:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| ec7473e7-d34b-333a-8780-5360323c6f7d | -2.9371 | -51.0465 | 2024-11-06 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 2348bd2d-c89e-34dc-9f04-d0aaf3b6c20c | -2.8017 | -52.921 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 553cc50b-8b2d-3232-a7d4-f604622897ff | -2.7428 | -54.1347 | 2024-11-06 14:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| a10c3915-5b88-3f19-9dd3-7bf802e920a1 | -1.2922 | -54.5784 | 2024-11-06 14:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 199.5 |
| e76f880f-d85a-35b5-ba3a-4e5791ce7f35 | -2.8016 | -52.9414 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 27f819bc-071a-3092-8017-56fff556363d | -2.8608 | -51.7731 | 2024-11-06 14:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 5fec0b3f-5a37-396e-b3f6-8282d4ef3af4 | -1.5348 | -52.1489 | 2024-11-06 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a09dc59d-678f-3547-b436-15c687cb8299 | -1.2922 | -54.5585 | 2024-11-06 14:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 306.4 |
| acb01e81-f386-30d7-8f24-10ebc24f9b26 | -1.5533 | -52.0871 | 2024-11-06 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ed318d02-5162-319c-9add-98ef5df933fd | -2.8423 | -51.7735 | 2024-11-06 14:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ea79e20f-1d4e-38eb-a3af-bc654b549fa7 | -1.8258 | -53.6489 | 2024-11-06 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6024d6e7-728f-3de1-b0de-e9e525248b44 | -2.764 | -53.2062 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 165.2 |
| a35aa160-8b78-395d-bd9f-b949d5490e7f | -3.0023 | -53.4434 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 75e74e27-7985-3284-abf3-b9c6435e9efd | -3.0023 | -53.4232 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c734aea6-7327-3221-bb27-a3545b4cde3e | -1.406 | -52.1916 | 2024-11-06 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d104ab81-9ffc-3d83-9fd9-7976ee86874b | -2.8386 | -52.8794 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4bdbb0d7-58b0-3064-aa8b-1a25ee55854b | -1.802 | -47.937 | 2024-11-06 14:20:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| d3266222-8155-31dd-a828-5effaaa92d62 | -1.5347 | -52.1694 | 2024-11-06 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4d3d0cbf-819c-3633-9a0a-0fcae468ae51 | -2.8385 | -52.9201 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 6a6ba4a1-af56-3ea5-9afe-fe9c0fa67982 | -2.8321 | -49.4749 | 2024-11-06 14:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f3aa0e02-f835-3121-8b07-b1d6dc5a419f | -1.514 | -53.4918 | 2024-11-06 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| edfa0764-0310-3af5-9919-eaae3913e781 | -1.4244 | -52.1913 | 2024-11-06 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| abdb41d4-a91d-30c8-9ba9-a6b8bf21bed6 | -1.3876 | -52.1918 | 2024-11-06 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dc9b545f-afb5-306c-8185-8b3beeeafec2 | -2.7456 | -53.2067 | 2024-11-06 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 610285af-b29b-3f98-a863-1d4a4a894d08 | -7.7938 | -44.084 | 2024-11-06 14:30:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0fcf96cb-7db5-3ec1-8720-94464adf89c1 | -1.4244 | -52.1913 | 2024-11-06 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 06a489d0-53ee-312d-ac6a-bfb55b4b6038 | -2.8321 | -49.4749 | 2024-11-06 14:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 4d8174b0-f438-3d97-bdb0-6eb08536fb36 | -2.9371 | -51.0465 | 2024-11-06 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1f0fbb41-c898-332d-bbfb-676c06cfd149 | -1.4957 | -53.4921 | 2024-11-06 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 28dad406-f847-3936-b91e-398415976fb1 | -2.8608 | -51.7731 | 2024-11-06 14:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 35f84711-dc20-364a-97aa-a0feeb9f62d8 | -1.4761 | -54.2565 | 2024-11-06 14:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| eb62743d-7740-32f2-b489-e3aba71d7dcd | -2.9186 | -51.047 | 2024-11-06 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| b704ce41-883a-371c-b78e-f867804d1008 | -1.2922 | -54.5784 | 2024-11-06 14:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 48581e8d-82dc-3504-afe6-277db19285cc | -1.8021 | -47.9153 | 2024-11-06 14:30:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 253d24fb-b420-36f0-b62d-75c4a2a8ca72 | -1.476 | -54.2765 | 2024-11-06 14:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 80171401-c747-3c8b-94f9-4697d239b379 | -2.6507 | -48.5629 | 2024-11-06 14:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 154e4eae-e78d-3ded-915b-969dfbbca95f | -2.8423 | -51.7735 | 2024-11-06 14:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 09841723-e124-3cc6-bf06-0d66c86c708f | -1.3876 | -52.1918 | 2024-11-06 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 6303b6ab-4193-3ce4-9359-770fa3e0bd39 | -3.1393 | -51.2069 | 2024-11-06 14:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e747ce32-bdc9-3af7-95d1-72f69f69ff8e | -1.535 | -52.0053 | 2024-11-06 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 2fb2e570-47b4-3d75-9c39-a43fa4d47158 | -2.8016 | -52.9414 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 0e3491a7-1c21-36bc-bd52-9c915501e223 | -1.514 | -53.4918 | 2024-11-06 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e55879f5-6805-3d08-b5db-c3a4a84bc49b | -1.406 | -52.1916 | 2024-11-06 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d5aedbe6-b90b-3ea3-bd02-264f056aee3a | -3.967 | -48.15 | 2024-11-06 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| fe6b787f-f595-38ec-b941-6eaab5839314 | -1.802 | -47.937 | 2024-11-06 14:30:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| c29b4642-76c3-3d27-93f9-55aa00e1d187 | -2.8054 | -51.8157 | 2024-11-06 14:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 8b60e17c-2db8-3ce1-879e-28310ec9c3e1 | -0.3587 | -51.4387 | 2024-11-06 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 169.8 |
| dc272c25-65a9-3450-980a-baa8f9422093 | -2.7456 | -53.2067 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 9d8943ad-b11f-3250-9f5b-e3fd59798e7b | -3.0023 | -53.4232 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| cdafc737-aec2-31ad-a233-f52e696e3d25 | -1.5348 | -52.1489 | 2024-11-06 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 9135864c-6653-3be4-bc70-be92f905ec23 | -1.5127 | -54.3161 | 2024-11-06 14:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3c121e9a-2847-35a7-aa4d-ea967be383dc | -3.0023 | -53.4434 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 85845bae-3f78-31bc-a0fe-1bccd3c83c5f | -2.8017 | -52.921 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ae11eb91-dfa1-3ec7-9815-5f931e58f694 | -3.0207 | -53.4227 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 189b7638-45af-3d9c-b5b5-b47a85ff5049 | -2.764 | -53.2062 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 192.8 |
| 3e6edd26-8787-35f2-b04b-0788b39a6ad0 | -6.9424 | -42.8126 | 2024-11-06 14:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 4a7a80c7-c325-3433-88e9-38dc5c3e68fb | -1.2922 | -54.5585 | 2024-11-06 14:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 277.2 |
| 6930b554-11bf-369c-8bef-fb91840c9819 | -2.7428 | -54.1347 | 2024-11-06 14:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| df56a617-cccc-3291-83a5-ddbe7579a9cd | -0.3587 | -51.4181 | 2024-11-06 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 742282af-9b15-3dca-9c47-5133ea17ceb5 | -1.8258 | -53.6489 | 2024-11-06 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| bd458003-a017-3535-a488-805e4c336c5d | -2.7456 | -53.2269 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 07879e4a-8fde-32c4-a2cd-037021d2b973 | -2.8386 | -52.8794 | 2024-11-06 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |


