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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e16563e-736b-37e1-b4b3-7e9fc76ddeeb | -3.13092 | -52.98569 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de71f6d5-ddc1-3344-896a-80d568788eab | -3.1006 | -53.73894 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6252ed91-af8b-31af-aae2-7d7b7da2b244 | -2.20827 | -53.66986 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcee9f5f-77a5-3943-beb1-9551962030b6 | -1.51083 | -54.18981 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 567a7a78-afc7-356e-bef1-c6c07fcdcaf2 | -2.30716 | -53.88011 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcade439-f83f-3d42-a849-015534874904 | -2.17284 | -53.63627 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d52d34e9-dce5-3a79-ad66-d108c8e97ccb | -1.61155 | -55.13744 | 2024-11-24 05:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b67cb01-00d8-3fd1-966f-b84680e00ed7 | -0.37661 | -51.54949 | 2024-11-24 05:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc781a98-d097-3207-aa3a-fadb6cf5cc15 | -3.13715 | -52.98675 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a524da2-b6df-3987-b6f3-888069904197 | 0.41014 | -50.86075 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa38293f-cbee-3545-87bd-bdad95f5d38e | -1.52089 | -51.62792 | 2024-11-24 05:37:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 581f272d-5884-31cb-b670-37c3efde23f2 | -3.06439 | -53.22881 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 37b4e264-79c6-3ffa-83f4-8fbc54b24116 | -3.24384 | -53.28605 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c766f3d-685f-3aef-b296-594b27dd8abb | -1.73062 | -52.72252 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b631a6ba-c3fb-36ac-845c-cc89b21eb0cb | -1.22024 | -53.68414 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4517faff-60eb-347d-8fd0-c7d5c1574311 | -1.22548 | -53.68876 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e6a295b5-b256-36a3-a8bd-711d375f9e7e | -2.16534 | -53.79599 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b6c206a-21c6-3a26-88fc-b40de8379326 | -2.28375 | -53.6352 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 644a32e6-584c-3dc2-ab56-7bcbf2b6c466 | -2.94464 | -51.42999 | 2024-11-24 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80df730d-b399-3754-96e7-3d594bf94443 | -2.62105 | -54.93624 | 2024-11-24 05:37:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76e1673e-62a2-391d-a978-0a78a6b4f496 | -3.25889 | -53.26929 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b052a263-88d9-3b0e-8b9b-66a8e7ef78d0 | -1.77313 | -52.72327 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3729ea2c-7fa0-3992-b4db-73340857a8ef | -3.10109 | -54.00642 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e32ade9e-ca72-39b5-b07f-57c722187fe4 | -3.06989 | -50.95441 | 2024-11-24 05:37:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1a2872c-24b4-3e2c-82f0-0beab99a82e6 | -1.48447 | -52.51894 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e335252-88ec-3581-ae6d-2f1d9df84dd9 | -1.4525 | -53.40151 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 308cf299-cc74-3243-ab99-1741fa8e3c54 | -2.63341 | -51.90041 | 2024-11-24 05:37:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edd20339-f45a-3e6a-95b1-26a7a1206a56 | -1.45419 | -53.40819 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b9590b1d-29f2-3e71-a75e-81cb431fb58a | -1.7361 | -52.72833 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d32db80e-9ac2-3380-b3dc-93c5fda48cd3 | -2.85859 | -53.96591 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3173a27-227f-3c1b-871e-ae6599fcd996 | -1.76763 | -52.71743 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbd35822-9654-3185-96e3-f01b8ffb5f38 | -3.24999 | -53.28693 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2167fb2d-89c0-3cd6-8be3-bff0733c0da7 | -2.85794 | -51.8192 | 2024-11-24 05:37:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebf09a45-ff4c-3ca8-b1cc-50fccf3cba17 | -2.17243 | -53.78858 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68e01e6d-4b1b-3112-9eee-8dad61c8b4cf | -0.3757 | -51.55508 | 2024-11-24 05:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6366ece-3703-3a48-9fdb-fa09a7b407e8 | -1.45121 | -53.41014 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c96e4b2d-c102-34eb-848d-5efc57205aa8 | -3.24452 | -53.28146 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e6b68f3-032c-3e29-b456-17f2bfe02f81 | -1.99009 | -53.2917 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27d2ebbe-29b0-327b-8443-0c3b88b3c6b6 | -2.80778 | -54.02607 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31b85b24-8015-3793-a931-80553bcd45bc | -2.91646 | -54.28727 | 2024-11-24 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92e6c01d-4169-3702-b757-ee4077a77d15 | -0.28651 | -51.60948 | 2024-11-24 05:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e88f9305-329f-392d-a342-61f013a16d97 | -2.32066 | -53.86984 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cc749805-4ca9-3a43-a146-8181e010e05c | -1.63409 | -53.3115 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 795a75e6-cd37-36ca-97ce-122952862152 | -2.03889 | -52.09779 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25dceb13-a201-3269-b8a7-5420dc3f4ce5 | -2.91071 | -54.28655 | 2024-11-24 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76827f14-b481-30fa-ae77-645919ee598b | -3.09734 | -53.74081 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9139f28-54e7-3193-bf37-7bdf3257c822 | -3.08736 | -51.32778 | 2024-11-24 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47856c73-ea15-3315-a2af-c0dc17db27ca | -2.82525 | -54.02855 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75cb46ca-b2e7-31ed-830c-9e717362f473 | 1.38776 | -55.91428 | 2024-11-24 05:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6874329d-2d36-3a9b-8830-1a7216c3a2af | -2.2806 | -53.63192 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1423cd62-fd0e-3a16-969a-0cde534c651d | -2.58026 | -51.89337 | 2024-11-24 05:37:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| caf08931-095a-344d-97df-8617fdb0863d | -1.51815 | -51.62845 | 2024-11-24 05:37:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 833d371b-d642-3598-ad65-82833ad66fb7 | -2.03807 | -52.10318 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b47050b-5d5d-3976-b6bc-2a9572ee4e62 | -1.6023 | -52.58773 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f84e178d-0c4d-313a-b6f9-a6759464da9b | -1.59525 | -52.59177 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3dd5af4d-c245-3e25-b486-8db40d78c91a | -3.05889 | -53.22358 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1bfa79b0-deee-38ad-9d67-58f6b79977cc | -3.20206 | -52.57311 | 2024-11-24 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 023ba1b0-4059-30fc-8e48-85c5ef145c81 | -2.85795 | -53.97009 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b27b561-239a-3572-9b33-78a42ac7b06a | -1.44891 | -53.40314 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9f534805-c98f-3e81-bd9a-609a5a13a8cf | -2.71016 | -48.6607 | 2024-11-24 05:40:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b30ffa38-4c61-3254-80cb-dc888a9a9475 | -1.21995 | -53.67229 | 2024-11-24 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 98f50391-49b5-3761-bb8d-2ed1ecf4a3e1 | -2.57717 | -51.88874 | 2024-11-24 05:40:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cad1e3e3-ae1b-339c-8106-51972616ab64 | -2.01094 | -51.17518 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 993af7a2-50c3-37a9-8865-1ed38ce5d2ee | -1.47909 | -52.51508 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 330e961f-92b7-3947-9eb4-6db235050096 | -2.03702 | -52.09505 | 2024-11-24 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 126e7234-fef9-3499-bb8c-cdec872e26f3 | -1.42032 | -53.38189 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| de1bf05a-70b8-3ce3-8035-ca66752cb9aa | -2.11221 | -50.12527 | 2024-11-24 05:40:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0760b3e-9561-32f6-9184-b3b7b51c6613 | -1.51968 | -51.61848 | 2024-11-24 05:40:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0145a125-75de-3a04-a7c4-9c6871132265 | -1.45684 | -51.11399 | 2024-11-24 05:40:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 964f52e1-578e-37d8-9228-34c962414a4f | 0.4158 | -50.85481 | 2024-11-24 05:40:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dcb05800-df53-356a-bf43-4b8fae774d03 | -2.61707 | -51.80032 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7176dc84-0048-3fba-8ecb-f4aaa7c055f2 | -2.70895 | -46.26568 | 2024-11-24 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c5954951-113f-33ae-987b-4fdc7282cc97 | -2.73527 | -49.1125 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4d8b9495-e344-3e49-9c98-75e0b807e7d7 | -0.3749 | -51.54807 | 2024-11-24 05:40:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 716591a8-fb87-30c8-a602-077608660899 | -2.68909 | -46.26962 | 2024-11-24 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2d937e34-ae33-3190-bf10-b6fad9cc2d15 | -1.42214 | -53.36981 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d4ea2af4-0a80-31ef-9a35-778a19a6e132 | -3.44866 | -45.66632 | 2024-11-24 05:40:00 | AQUA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e7928904-5a49-37c8-8f2e-4b8788ebae60 | -2.06669 | -50.30817 | 2024-11-24 05:40:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d10b2d36-6971-33ec-95df-29b748eb9413 | -2.55466 | -46.55652 | 2024-11-24 05:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fdda4ecc-dfeb-36fb-852d-7bfa0d5fd1e8 | -2.46007 | -49.03608 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ebb06356-6976-360e-9a74-b9c12e902e0e | -1.20536 | -51.74545 | 2024-11-24 05:40:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 670ebee4-0479-3a23-82fc-345c526f1478 | -1.44588 | -53.40527 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 54d98727-4110-3906-ae99-5224856b5e1c | -2.22118 | -46.38938 | 2024-11-24 05:40:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 610f70b8-b802-34c5-9f8e-0ab4d72f1a5d | -1.5068 | -54.18295 | 2024-11-24 05:40:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 1e7f3e3e-d8af-3c08-ad0f-dfe3b6bb5d61 | -2.22074 | -46.38403 | 2024-11-24 05:40:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 5ecf284a-23a1-38ce-ba96-4e9320671ab4 | -1.83532 | -46.64152 | 2024-11-24 05:40:00 | AQUA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9abe1ad9-1057-3bcd-8e76-9d41ea0c5189 | -1.19295 | -51.76409 | 2024-11-24 05:40:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 740f7c58-a65f-3762-b38a-bd703d7add32 | -2.44717 | -49.06155 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25d83d4c-b0d5-3893-8eb3-2bfd92979c44 | -2.74403 | -49.12029 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 180d18d2-595d-3f75-a412-8854d077f739 | -1.73475 | -52.71917 | 2024-11-24 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a8a99a46-116e-3f98-901b-7f5045db0ca3 | -2.34944 | -49.04076 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 975fdcf0-a331-3e3b-8f56-b562ebe7fa3a | -2.31747 | -53.87201 | 2024-11-24 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ff9300f9-fc1a-3d4c-9b24-52c84bc2fafc | -1.04088 | -51.73978 | 2024-11-24 05:40:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1f676138-8ee2-3d3d-9bb1-cb15389ac7c7 | -1.21327 | -53.67925 | 2024-11-24 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| d3b7e61a-0ba8-3c16-8e8a-12bd41f3206a | -2.21108 | -46.38794 | 2024-11-24 05:40:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 663d0a5d-cabc-324d-9981-d9f5880df98e | -2.26775 | -50.4554 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03af6ed5-5cfc-3737-b741-57a1c7098408 | -2.46567 | -47.08629 | 2024-11-24 05:40:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3675cc83-6b19-3b8f-aa47-b579fc759b29 | -2.60898 | -51.80325 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e937e722-3fa9-3fa6-a8c4-661b5b4c3d7d | -1.11261 | -53.38211 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f6913ba6-4b7e-398d-aa66-ab83051f74e0 | -1.36283 | -53.83801 | 2024-11-24 05:40:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |


[Clique aqui para ver as próximas entradas](README84.md)
