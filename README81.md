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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0474327f-22fc-337a-bed3-8660d2284333 | -2.43843 | -49.37423 | 2025-10-16 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d04dd9e-78f2-3c4b-aa38-b22356118c03 | -2.87814 | -50.7397 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64775c13-6093-318f-9e8b-849dc7d36b9e | 1.77338 | -55.75841 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1a6dcea-04d4-3804-8cf2-0282c057464c | -1.99068 | -56.91862 | 2025-10-16 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b239fe31-8f5e-3e61-b469-d065d339077d | -2.87358 | -50.7306 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4119702f-91e7-34da-878e-216160a35632 | -1.11169 | -54.07014 | 2025-10-16 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc9868b-997c-3911-90e8-343d4a3c83b0 | -2.70275 | -49.86455 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69d2e2ce-9c91-3f57-ab4d-cfaa27f39aa3 | -3.07564 | -49.51207 | 2025-10-16 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bfe7b3a-80bd-34d6-bba0-1894c6f69ff6 | -1.48775 | -55.44277 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b08a028d-0f57-3157-8475-e7bd4e5f7258 | -2.42782 | -57.12119 | 2025-10-16 05:25:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 077573de-0952-39a6-bea3-724806064884 | -1.48832 | -55.4391 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4fae45c-96f4-3f21-9f1a-9b8fc4bf1193 | 1.81957 | -55.75112 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4f8d223-7709-3560-8766-499904f55b9d | -1.48719 | -55.44643 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31a4b270-a876-321f-9d57-9e2f05ad6cc1 | -1.49187 | -55.44342 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82a4a41d-7fc4-3476-931d-8bfe38040d78 | 1.82884 | -55.73497 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80b31849-7ae8-3042-abbb-fcf8226f3d06 | 1.73918 | -55.80472 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a43a3a83-cac2-3fdb-af72-507652a3bbac | -2.70888 | -49.86542 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0edb825-b4ac-32fb-9477-f20af8c61c57 | -2.87295 | -50.73475 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b27be7ab-6a02-367e-af5f-833adec6b9a5 | -2.81092 | -54.38303 | 2025-10-16 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adad0d3f-0a1c-3f88-87eb-01d04ca4abde | -2.88457 | -50.73648 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 453c6ef5-0c5e-3dea-b94d-3ff3759c312f | -3.07638 | -49.50722 | 2025-10-16 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94f6d2cf-de97-3cd4-8569-b420bd2b0e65 | 1.86401 | -55.67303 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bc08083-81fa-332e-af18-634a4ee90e87 | -2.86653 | -50.73799 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fdd95e4-2f97-31da-a9f4-6f81bfeadb26 | -3.05867 | -52.65775 | 2025-10-16 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4ff67ce-d8c7-3285-914c-398c566e9088 | 1.23174 | -51.03184 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0edf0e32-d9f1-3bb1-b325-d207ae56ca08 | -3.6841 | -47.63938 | 2025-10-16 05:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ad65124-112c-3f1c-a12c-233aea9b596e | 1.78492 | -55.75653 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfbef199-0d7c-3502-bd6d-323b62040a1f | 1.75156 | -55.78328 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b79c0d2-36bd-3d96-a49e-e6bd84c11a28 | -2.70412 | -49.85506 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fb9a598-7304-36be-84a4-cb3d1e235bca | -3.42165 | -50.25148 | 2025-10-16 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1143a7ee-2d20-363e-b223-ff6383f600e1 | -2.79588 | -48.94494 | 2025-10-16 05:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e26af84a-cc4a-39bf-a76a-de62ad3c2e8e | 1.82266 | -55.74574 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc1cd359-8537-3c7f-ad13-d197c33ad634 | -2.70956 | -49.86073 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61b8bf84-49e8-345e-b0bb-79a0a04c1075 | -1.98998 | -56.92318 | 2025-10-16 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a9531cd-d89f-37e9-8d8d-e3884c5efd15 | -2.88001 | -50.72736 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee3cd755-1f45-34ca-80b6-20f0c25ae85f | -2.8742 | -50.72649 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ce7a784-67a3-3624-b318-62fcaa20e55a | -1.48421 | -55.68036 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a1a86d7-af10-33f9-ac9a-fe447a5cd609 | -3.05355 | -52.65699 | 2025-10-16 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bda2448-8f47-3e79-a3a2-13ba8de647f4 | -2.88395 | -50.74058 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3190ce48-962d-338e-9f17-184a0002c07f | -3.07384 | -49.50487 | 2025-10-16 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71cd60d9-0b2f-35ec-b334-dcf0d1ee5193 | 1.84634 | -55.7103 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd2badb8-b68b-34e1-b014-45ed75b05b5f | -2.87876 | -50.73559 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5160c8a-8c21-3e02-ac99-253b332f61d1 | 1.74956 | -55.7817 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd007fe0-5aa7-38b2-83c4-e74fcc387451 | 1.04624 | -51.045 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb666dd3-c151-3f92-a018-df6159851b70 | 1.83029 | -55.76899 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1ff29ee-f853-340d-9a55-7891abb651fa | -1.65971 | -55.14256 | 2025-10-16 05:25:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db1cb1ed-9bed-3e86-a99b-fcea369508e5 | -2.70387 | -49.85775 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36358cc6-e063-3085-8137-64d4a1b9e3e9 | 1.82493 | -55.76005 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48ff5d2e-436f-3a07-bb9e-9834147d5392 | -2.93609 | -54.1745 | 2025-10-16 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9b6df75-2f04-3f70-b362-dfd68aa74b6f | 1.74302 | -55.80412 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1167132b-e4a6-3049-81e7-01c80171c38a | 1.81462 | -55.94057 | 2025-10-16 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 547a8f9e-e085-3031-b491-ae878bc43a04 | -2.25872 | -56.0584 | 2025-10-16 05:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b231f1ed-bbe4-3fce-a10a-892333be3bf9 | 1.06018 | -51.02914 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60f947ab-88d1-33b2-90c4-3496127c0aa3 | -1.11482 | -54.06326 | 2025-10-16 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21ffad25-9e86-3426-afb8-5da2c585d57e | 1.04998 | -51.03411 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8284a52-fbb5-30de-bdb7-ae6213e02799 | 1.84199 | -55.7182 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90e70d58-95dd-3a29-9eb0-6b81ac471803 | -3.49018 | -50.09224 | 2025-10-16 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27aa2a2d-1f7b-347e-b1ee-0c17b4906fed | 1.81387 | -55.93591 | 2025-10-16 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 550fd76c-f797-3323-9ee6-105d32977974 | 1.74537 | -55.79404 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 687e7d07-55ab-3d78-86fc-be7e2a79ae44 | 1.80556 | -55.8844 | 2025-10-16 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e43c9175-ea8b-3114-a561-729e9bf7e6da | 1.76087 | -55.76719 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d8f5722-2d55-3cf8-9a0c-e6429815bdca | 1.83413 | -55.76836 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1421950-1f51-330f-9afb-f7360a216ce9 | -2.44472 | -49.37519 | 2025-10-16 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d2f539c-cbf8-3562-958b-7f44d1e7c1ae | 1.74772 | -55.7839 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b55cd05-bb4c-39ed-bc90-a904300a7ebe | 1.0457 | -51.04165 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d821253-7d1a-3444-9ff1-90cf04d5ddb8 | 1.83187 | -55.75409 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6de246e-73b8-3da9-b36e-2ddd0f7a9a11 | -3.4063 | -51.57158 | 2025-10-16 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee235f9b-c768-33b3-9a4f-9f224837ea73 | 1.89116 | -55.88815 | 2025-10-16 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66585323-56a1-3d77-9b1a-37ac09ed11c2 | 1.22103 | -51.03345 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683b0c32-2eba-3c1e-a099-b68eef0eae75 | 1.75082 | -55.77853 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eb61657-fa4c-3024-b8c0-044129422cd6 | 1.83504 | -55.72421 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa1dfe0b-0cce-3316-9901-b0eed74fde69 | 1.8358 | -55.729 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a943125-a03d-35ac-a047-4fbbd591ce43 | -2.70928 | -49.86338 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d52909e-2b79-3aa0-b165-d84eec40f832 | -2.70857 | -49.86802 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73579f24-541a-355f-919b-75eed39847ef | 1.22639 | -51.0327 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 403787b8-81f2-39dc-b0f5-e38169da27df | 1.83194 | -55.7296 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e8964ed-c84e-3044-bc49-e68d31301c4b | -3.43506 | -50.25699 | 2025-10-16 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49b81877-0679-3e7c-a1ad-7d54c8a24d54 | -3.68079 | -47.63567 | 2025-10-16 05:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e783578f-cd6e-397e-afbb-89bf1abcc4cb | -3.05611 | -52.65889 | 2025-10-16 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fba4c43-d127-328b-b829-74a2a26c0e17 | -3.42363 | -50.25071 | 2025-10-16 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25eaef81-4a43-3b86-af69-3f45871ee8b9 | -2.87752 | -50.7438 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8e33ff7-b4d7-3198-b319-622da1de725b | -3.12776 | -50.213 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f655fed-208d-3594-903c-925b6fdc1292 | -2.86715 | -50.73388 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e037ab6f-75c3-3381-a1c3-046d5e020c8b | -2.70343 | -49.85983 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a364fb6-5128-3e40-b8e9-c8d8a125c80b | -3.68507 | -47.63251 | 2025-10-16 05:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 740e9e18-5aa0-301d-8097-deb0ef44426c | -3.05653 | -52.65603 | 2025-10-16 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbb49a0d-7563-35e6-841f-eb4aa81b0cc4 | -3.13375 | -50.21415 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c0aa3ba-187c-39a5-a124-32e90c52c1a6 | 1.05052 | -51.03748 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d510aed8-5a04-3ad6-8645-45946da3ec67 | -2.79667 | -48.93964 | 2025-10-16 05:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 965f0940-a40f-39ce-95a9-f319af9ff7ed | 1.79108 | -55.74577 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5c386000-15ac-378a-adb9-08d412cd0e8f | 1.82418 | -55.75529 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a7fafab-8659-3316-82ca-b55c9bae7d73 | -1.65549 | -55.1419 | 2025-10-16 05:25:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1348b726-841f-30f9-a9a1-0f5c39663ad2 | -2.25924 | -56.05502 | 2025-10-16 05:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a5c8b3-6ed9-3881-89c3-af8e8c4259f4 | -3.06936 | -49.51105 | 2025-10-16 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc055926-a22b-393a-8531-2c016e1c36b6 | -3.06165 | -52.65681 | 2025-10-16 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dc6ab63-1c6f-3e3b-ba21-61d76f725759 | -2.87939 | -50.73147 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7ab1068-8ae7-3100-990f-0119a35dbcdf | 1.81495 | -55.74693 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46057d03-961a-320b-9a7e-0f85b75f9690 | -3.67978 | -47.64249 | 2025-10-16 05:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 02f8040e-1f90-34bb-a265-5d0430162a6d | -3.51043 | -50.21455 | 2025-10-16 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a86acd53-474b-3a17-9347-196ac03b2a57 | -3.07316 | -49.50966 | 2025-10-16 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README82.md)
