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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de31a7a2-7242-3679-a888-a87ddac3560c | -2.69494 | -52.91612 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4bcc3fb-f29a-33be-9f0b-dea7b83b87ee | -2.89615 | -51.57552 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e1e6fe4-a101-3451-bca1-593d8964f2ca | -2.78467 | -51.66847 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d461948-8f13-3de3-ac63-a34cb3b9f5b5 | -1.77715 | -53.71748 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f6a9a73-3b5e-3a30-a2ca-7e5c38ca87d5 | -2.58963 | -53.97196 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a64d154-8f0d-39fd-8c47-6e62196f014f | -2.61473 | -53.98661 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b21da594-16c8-339b-9542-63b24ae5c785 | -3.62014 | -42.74013 | 2024-11-30 05:01:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ea14d22-3b25-354f-93d7-31101a42b43f | -2.78299 | -49.82767 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ff256d3-5d23-38d9-99a5-40ef760933c9 | -3.10954 | -53.99906 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f840834f-a831-3036-864b-03c1fef3f83a | -3.48853 | -53.80324 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5cf444d6-70f3-38b6-ab81-9710c12762da | -3.32859 | -54.13691 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cda92b72-e995-371d-995d-d9e09c5459f0 | -2.8749 | -53.99138 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ab5a3f4-8594-3bfe-ac1d-e1caa35d4f18 | -2.63096 | -51.74908 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 0b458822-aded-3d87-81b6-b90c7fa8612a | -1.24878 | -51.74065 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd7c741f-2682-34cd-9e46-110a691e9038 | -2.63075 | -51.77452 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb1713d8-acc6-3cf5-91ce-55aa0345a32d | -4.88457 | -41.30479 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c5843bfb-d6df-3ccf-9cae-71aef9ca5816 | -2.60063 | -51.94598 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05abef98-e4e2-305a-a771-a57e533f9bc5 | -2.79178 | -52.98725 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15700cad-c4f9-3caa-b6c5-e4bb80b5a123 | -1.58956 | -51.25629 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59f3a715-ea53-32f2-91b3-46dac38efe5a | -2.97787 | -53.87384 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e73b6703-ece3-343e-88fa-26f48ca1ad85 | -1.3711 | -53.63331 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58cc0e48-2c1c-3e87-8329-282ec639a74e | -2.18653 | -47.14312 | 2024-11-30 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7099120b-f1e8-34cf-a8ac-45f0ebe49a8b | -2.83026 | -52.9439 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2a6b49b-f699-3c92-b1f3-9d34618ca87e | -4.11422 | -54.41641 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5856e40b-d980-3ffe-ad27-39abe622a613 | -2.83719 | -54.07882 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4c94992-ce3a-3987-a3a6-e7adc28bdcdc | 0.94834 | -50.74888 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e19b5ab-5922-3cf9-a9fe-caf20bd032b1 | -2.83819 | -54.02878 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57072886-889d-3076-a335-401847281833 | -2.82328 | -54.08025 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90457105-b544-3819-8f6f-857f130a826b | -1.09577 | -53.3633 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4577ef5-0272-35b4-830c-f6fe14690578 | -3.25457 | -53.64374 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d53e020e-b152-3b72-a7f4-00406ced3eff | -1.53275 | -56.06542 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90c3c1fe-44a6-32e0-9c7a-26aed448b213 | -1.66055 | -52.40772 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2671b72f-3ff1-38fa-9501-a4287cb1b1dd | -3.22529 | -53.63183 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 840b2ed2-99c3-3d8f-89f2-f9e0272dda6c | -2.95834 | -53.88882 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e2215a4-11ae-3ad1-84b4-470564c8b6d1 | -2.32982 | -50.67701 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4fba535d-fd2d-3df6-a88f-3a928c8555b2 | -2.73573 | -47.53878 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abccd5b6-4c4a-377f-86ce-cfa29d327fc0 | -2.95554 | -53.88477 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57bc1365-e1f8-3e0a-b102-c95d536d9b63 | -2.32725 | -54.50399 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 879ca7f4-3dc3-3376-aed6-8564c700bd28 | -2.23451 | -54.92031 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e485aaca-b931-3654-bbd0-71627c237c85 | -1.27365 | -51.62865 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9d130cf-9978-3231-b545-19ce8ffc894d | -2.86211 | -54.00736 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52412507-967b-369e-b206-cca364408016 | -2.91857 | -53.07158 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6cf13d2-d91d-30cd-b483-aedd46c81d31 | -3.164 | -53.64791 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68440532-04c1-3f23-b2cf-78c8384ff31b | -3.43746 | -59.2883 | 2024-11-30 05:01:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f6dd951b-138a-3c0a-acc6-3244a071149b | -1.32843 | -54.61633 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f954403-dc52-3f5f-8fec-518b52a1d34f | -2.89981 | -51.5761 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0861d1c-ebcc-3ea0-bae6-71f12e20aa28 | -3.19953 | -51.25727 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90f2aa2e-bd0b-3e34-91e6-29d9f55fadaf | -2.72827 | -53.19249 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0277ed2e-935f-3e64-becb-1b47844d33d5 | -1.30125 | -51.73229 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b5b1a41-1248-39fa-9de4-58d8962f026a | -1.81956 | -50.90323 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4545b406-6db6-36ca-8e9f-cf11572947d8 | -0.90596 | -52.41122 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 619343e1-a063-3d10-8de5-effe8fd6cbd2 | -3.24725 | -53.64627 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41d1bb54-9d25-3693-88ca-764caf6bae2b | -2.42745 | -54.01856 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d86e534-5b36-3630-8533-c3c7fb6caec1 | -1.30716 | -55.74167 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39d02665-a04b-3394-898b-33378dcfd323 | -3.04906 | -49.37233 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d2b75bd-0bbc-3102-aa0c-10313cf2c626 | -2.9865 | -53.34797 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7a22b81-fec5-363e-af16-6d6310311c59 | -1.40199 | -53.39238 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf6837ca-f7ad-37bb-9ff4-8834a683095b | -2.97566 | -53.88795 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40a0befc-8236-30a5-8caa-cf39b77793f5 | -3.11227 | -53.98148 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eb92172-2372-35a5-b959-9aed903df4a7 | -2.23171 | -53.68961 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15b86117-4654-3fa8-8b37-26b1cfdc37ab | -1.41682 | -55.02196 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e276d9ae-d70c-3597-872e-f9db4c59a8e4 | -1.56498 | -53.79919 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1740e81-6c96-38bc-acf2-aa718c473ba9 | -2.83375 | -54.03527 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc26c55f-4d8c-3a80-ad2a-8a6e12847699 | -3.36405 | -51.06444 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 957e6ceb-47f8-312d-a244-aff5bfb01720 | -2.32559 | -50.66887 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 419e4ba8-a82b-3887-b2b9-31ca38201a60 | -3.14323 | -45.9836 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e22f568-1a4f-3e55-bc81-2ab16607dd76 | -3.04897 | -48.52599 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 804a6e9c-7a58-3cd4-82ea-fd88264ff5d7 | -1.62536 | -53.86582 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f56ced6-7e58-33a4-af7b-87214a7144f2 | -2.41299 | -46.50359 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fc2f327-ea92-3a23-9318-97118b88d81d | -2.99411 | -49.53488 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c029a68-0a4f-3df0-93d3-80161cb9af95 | -1.24481 | -51.78926 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab4f5282-79ca-32ed-987a-d6ef8dae770c | -3.33029 | -54.14796 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cecc10c-dd06-3cdf-8452-d9b350dfc514 | -2.9684 | -53.89043 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dddfe832-c844-350e-843a-fde947b2481f | 0.10755 | -51.47104 | 2024-11-30 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f088aa5d-a6ad-3d1b-9652-acecd6813de6 | -3.7297 | -49.87335 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 142b3911-bcb9-3a03-a66f-cb2d62e03137 | -3.26551 | -54.10927 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43762ee5-35c7-32e7-aaa9-70a8637d907d | -1.20269 | -53.67529 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42381a98-ce24-3573-8e88-8f88427e9c3a | -2.83051 | -54.07779 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9398caaf-a1b2-3d87-97a2-a193cceac114 | 0.55089 | -60.36361 | 2024-11-30 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f636a858-6997-35b8-80cb-4f2f423f0122 | -3.32853 | -50.2201 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23dee161-5ba1-3e7e-bdf2-a32ae2eff5b1 | 1.67352 | -50.66537 | 2024-11-30 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22730053-5456-3843-8762-e0946795862f | -2.62245 | -51.75629 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d2ace15-4091-302a-87a2-84876f805d1b | 0.065 | -51.49263 | 2024-11-30 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c462662f-c4d7-3390-bac1-a4e95971697f | -3.03613 | -54.01601 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e7f8d8a-5895-34e7-be2e-2bde1b6a2818 | -3.33791 | -53.31122 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ec88f3a-154d-347a-9c7f-37e28f08893c | -3.15097 | -53.82092 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dff36bb-279d-3a4e-84b2-f157cafa144e | -1.31094 | -51.92041 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d4e4df8-8585-39ff-83c4-dca55261b188 | -2.37715 | -47.87824 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8954f351-4685-309f-8411-7122e9e5c6c4 | -3.42584 | -53.88839 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dbb4e36f-a5ea-3fb8-9aea-45b44007109c | -0.04641 | -53.25944 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25ea20df-2be0-350c-9165-7c02fdcd3926 | 1.42427 | -55.88517 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5400179-b707-3175-8a23-df818dd49692 | -3.31925 | -54.17484 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acb30071-f585-34fa-9fba-0a2f0a26d196 | -1.88723 | -48.64668 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f6ab452-d6ed-3543-9cdb-10aac7fa77cf | -3.04613 | -54.49277 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 186fc78b-95d4-368d-925e-0acf1c46d7ec | -3.61538 | -50.18779 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 336e2752-2a98-3af7-8356-ae1993168a9b | -3.46073 | -54.56746 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54d47211-1589-325e-880e-04b1c2001729 | -3.21235 | -50.27312 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 909c379c-d7a2-35c2-a26c-185fcaf0ecb2 | -2.66421 | -48.78764 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b96f722-65ed-39f0-a4e6-0e7452c1beb6 | -1.93568 | -53.44134 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c77962f-f74a-31ba-8a89-18972fafe312 | -1.89319 | -55.48026 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README104.md)
