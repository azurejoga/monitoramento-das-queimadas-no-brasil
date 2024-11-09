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
| eb664cd0-fb4a-3444-8b70-6e1dfbe92d19 | -3.01458 | -53.42137 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 251a0a0f-e506-3a1b-a8fc-cd2fecda4cb1 | -1.6425 | -50.43772 | 2024-11-09 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acd6624e-a729-317c-9e87-4e435e740f6d | -4.05014 | -51.06791 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b92c853-ca2b-3273-93d1-92a03dbf0460 | -3.30265 | -51.59533 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 538c2ce1-4bf9-3c76-918e-779c51cbd03a | -4.31956 | -48.64928 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdf2bcd4-755d-358e-bb4d-b87ab048fe0d | -1.55726 | -51.17058 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd49fb6e-180e-31a9-826d-ee018e57f06d | -1.72947 | -53.28696 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd2230fc-01f6-3381-a5e1-b4051d139b5a | -2.59063 | -48.1624 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2ec9453-aefc-3a08-864e-b8fdb8cef908 | -1.39125 | -54.64678 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c232817-b2d2-3057-a450-933fe2d1e2b9 | -2.84607 | -51.77266 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06cd9cc6-e1d4-371e-a588-8c6f828b12b9 | -3.59814 | -47.35509 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d9ffaff2-4240-3a94-a39e-c22aee6a3dac | -3.11142 | -54.15664 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c326bceb-b9b0-369d-9530-46ca060b4b23 | -1.41384 | -54.76734 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79a7dd4f-b6bf-3d3c-bc5d-25d4ebab1a23 | -4.07113 | -48.31975 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1244c29c-d09d-37d5-9055-57490baa43cb | -3.44877 | -52.72346 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f51a17da-6c04-33ad-b8e6-8ed834ad3a74 | -2.92012 | -51.05206 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 801ff525-da5a-3bc7-b715-f9985b946000 | -5.07929 | -47.93948 | 2024-11-09 04:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14715a9b-c813-34e2-ba04-cf194312eca5 | -3.556 | -43.56975 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7049eaa-e013-336d-9cb0-cf5fd4c01d0c | -2.97579 | -51.43344 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d97650b-6502-3fbf-823c-882d326cfc6f | -1.62086 | -52.53868 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e93c4f2-6888-3ab0-93bb-bdc6c8b679ff | -1.13655 | -54.22071 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0615665-4a4f-3976-af52-ee69c9a60578 | -2.90511 | -49.71693 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ad41a6d-56cf-3ead-b4ae-15f46db8b354 | -2.147 | -50.76591 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8e413c4-cacd-3c13-afae-07f6f0a92c2b | -3.29292 | -53.11494 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cc0ea10-7d66-3886-aa9f-4327da990667 | -4.81987 | -49.01602 | 2024-11-09 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1052cf9-db49-34d5-92ff-1986ec91a289 | -1.19222 | -53.49642 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d9958de-46dd-342d-88e6-2e1909cb4552 | -2.72556 | -54.90916 | 2024-11-09 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 498b7833-98c6-30fe-8bcb-490763703bd8 | -4.20301 | -48.54401 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4c66c496-ccff-3619-be51-c53c873df129 | -1.43707 | -55.19146 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8f23e1d-456c-3c58-ba09-4623c5f23f52 | -3.95701 | -48.13643 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0935b3d9-9b89-3349-b2ac-3e640818dd25 | -3.12046 | -51.10912 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d282c0ea-46b1-3a3b-a34a-2782d6424d00 | -3.05564 | -51.06791 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 459daac4-4b21-3513-876d-af970276aa29 | -3.07133 | -54.7777 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3bcc238-69d8-3b75-b41e-28e9f796c869 | -2.15578 | -53.69713 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a586fb4-f086-3825-9300-2fea5c562117 | -3.30711 | -50.07853 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 172aa06a-0acb-396d-8e66-55f394de5872 | -3.03553 | -51.54011 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 202c6664-fbdb-3950-9f51-81a5295d2d1c | -3.18238 | -50.59586 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15458696-66db-3bc0-9a76-609cfc3cb6e0 | -3.76163 | -51.76531 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f0d95b8-957d-342d-aaca-d76a0e8ffd82 | -3.34989 | -50.26137 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4c99f1c-47c1-3f55-9541-29b083cdca6b | -3.09044 | -53.71213 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7625361b-1e5d-3e6b-872d-cde87913a050 | -0.19264 | -60.76482 | 2024-11-09 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e85a0c94-b394-3f66-a54c-96d5479fbcdc | -2.79539 | -53.99986 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da51869f-9002-367b-8b99-967295a48be7 | -1.75888 | -52.69161 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d14e9bd-4941-3c2d-b725-cdb74e2520a6 | -2.68057 | -46.78564 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9b80919-6e53-3808-981b-48957cc64044 | -2.35998 | -48.904 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1585d67-715d-31e5-8bed-bc897212a0fa | -4.614 | -49.58603 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82891871-0c80-30f2-b566-9d23e4b26dea | -3.65041 | -50.76017 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8313955e-b3db-3dab-864a-b2a281162f7c | -0.90955 | -51.76453 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ddf39c2-9707-318c-920c-72fac6311156 | -2.23294 | -46.50664 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96e48da1-56ed-338f-a66d-60ac3672ca19 | -1.41397 | -52.32578 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b07238-ee25-3f1c-a313-2df08891fa7a | -1.33235 | -54.6002 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab48a8e7-12bc-33b9-a97d-52909ff30765 | -0.89113 | -51.77251 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e957a7fc-9125-3c8d-a5a4-f92e405a4ce8 | -4.08745 | -48.51333 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d2ba371-72e2-3145-b893-95656b62866d | -2.57571 | -48.17831 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 706ca7e6-42eb-31af-b683-daa9e1bdb3ee | -3.34682 | -49.94009 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b6127174-537e-3939-9aba-78893a779cd0 | -3.53792 | -51.2522 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 757872a1-62d1-329b-94c2-4f3d9754f501 | -2.11837 | -50.81258 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8213206e-89d6-313d-905d-76ec7790969a | -2.60726 | -51.75467 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b351d38-24bd-315e-abcd-5d557e421c8b | -1.18667 | -52.1549 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b9bdb13-3aff-3b8f-913c-f35b8af567f6 | -2.72586 | -46.66969 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b64cb1df-277b-3b91-acba-cfb1e27730d5 | -3.24693 | -48.74957 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dcb48d1-68cc-3743-a122-27e8dd526b4b | -3.52257 | -51.52596 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52281c4e-fdf7-30b7-99c2-1fdacc8a187f | -4.06702 | -50.01191 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ed154510-6420-3641-a42b-e89f61b82322 | -2.96471 | -53.86652 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efa80d65-fe3d-3f2a-bcad-8d3ea9bad90e | -1.60191 | -53.32656 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151a3689-d8e0-3866-b455-8a6e4b60e6e3 | -3.48161 | -50.80566 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 048ff9cf-13bf-33d0-a8d2-b53cbb499ea4 | -2.85676 | -48.45352 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69465217-81c4-35e2-a306-543819c0b910 | -3.08828 | -53.29868 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a987fc2d-d762-3bcb-920f-f70aa9d13a37 | -2.39128 | -46.77851 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afbe02d2-d7ef-37d6-82b9-497a070f035e | -2.39934 | -47.81296 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41487e9f-e1ce-3553-a19c-5a7ae5042873 | -4.43196 | -47.262 | 2024-11-09 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53fefcfc-2954-378a-b4f2-8c01f8cbe908 | -2.72054 | -54.14917 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d24955-492c-3816-a062-6ddb87903a8d | -3.11847 | -50.14386 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 676e357f-64c9-381e-b4c1-3e48dcde6be2 | -2.29083 | -48.73247 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edafb5fd-147b-387d-a994-b1fb9b42a325 | -5.81377 | -44.11811 | 2024-11-09 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca9e865c-aa7f-3c48-87b1-bdd3f910c2ca | -3.53964 | -51.104 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd66e33f-b6f8-32d1-8309-4d353e32fbfa | -4.12741 | -46.85706 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c561f709-5f7a-3d49-9288-6a1e58f42d86 | -2.85568 | -51.77785 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 293b740c-816c-3532-881c-c0d078fc8c31 | -1.24157 | -51.76084 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30795f25-e83c-36c3-b74f-e0610c7e6427 | -2.56886 | -46.54116 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d449efd-c9f5-3a75-9c02-4e449c395fd7 | -1.12526 | -51.9452 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ffc523b-052d-35af-95f3-35f60fd0b530 | -1.2511 | -51.76594 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eee12b5-722a-3742-86bc-5688f0d66b2c | -2.84328 | -49.44592 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0aa6331-e0bc-3f28-99ea-9b6e51206f05 | -1.63271 | -47.36038 | 2024-11-09 04:55:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bebbebf6-e8dc-32d3-82b8-ee08bd8678c5 | -2.86236 | -49.14715 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b891e709-5c93-3374-9007-2c299e0d1590 | -3.74682 | -52.03812 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0802918-231c-3c85-a071-721e6bfa51d2 | -3.23414 | -50.45113 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d9313da-5aae-32ab-9f26-db89936a86e0 | -3.75246 | -52.09462 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2068c81c-a4a1-3921-8d79-45d28349092d | -2.24112 | -50.71614 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed05f450-d9dc-3557-a999-3343b6b11ebf | -3.32909 | -53.1877 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6484c8-7ad7-36e1-ae00-b61035b52ecd | -1.13196 | -53.60395 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c58e97c8-8e6f-3026-932b-3990ec383c3e | -2.13182 | -53.24703 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8ab322d-2f7f-3653-ab64-a8c29cbbfca2 | -3.48361 | -52.87127 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c397378a-c44d-3547-8ee9-73e41f56cc59 | -2.43505 | -50.51247 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f755378-2aa7-34ea-b8a7-dacf953553fb | -2.33106 | -48.86035 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1b3a2d6-fc25-3029-83da-99fa1c50e893 | -3.74615 | -51.09831 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7086f779-d6c8-3dac-a280-9124c904bb7e | -4.22515 | -49.81523 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53260faa-895d-326a-983f-09733461cbd5 | -0.81605 | -52.36086 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aa0b976-bf1e-3688-8c1a-c2bb27eda7d0 | -2.88063 | -49.23128 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efa4fed8-b670-358f-a27c-e2cae7fb7496 | -2.12139 | -50.13433 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README69.md)
