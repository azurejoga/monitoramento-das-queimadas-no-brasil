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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87cd52d6-d383-35c7-b6dc-4a86d9c91b55 | -3.1546 | -51.12622 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7df01802-099b-3c00-825f-be871778ec73 | -2.43553 | -53.66449 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58df34fb-a3ab-3f64-8189-868021dd55a6 | -3.02561 | -51.52946 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19cf682-d3a5-30f4-9df0-41fc62d57210 | -3.10175 | -53.33007 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75dfb80b-3aa6-3255-8431-fd8d58866a5d | -2.79196 | -49.65653 | 2024-11-09 05:20:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7d73dd4-b291-3e20-bbc8-5f0d22724dc4 | -3.84248 | -50.03865 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 779ea179-7c9d-38ff-99e9-eaf385d4d9ea | -1.57445 | -54.63448 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7b74d2d-cfaa-3c6b-bc82-db706a5febac | -3.0235 | -53.87214 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95822091-fcb6-3097-ab2c-de9126cdfdee | -2.36286 | -54.75473 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bc7c24b7-162d-357d-b2a0-16b6ed2b4734 | -1.39267 | -54.64555 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0dee85c-bf40-3bcb-b456-1304773a691a | -1.30058 | -54.67007 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc122c0b-72f4-3e81-ac9d-38ca8c103fcf | -2.93515 | -51.05177 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6c12222-3dd9-3b9e-bd2f-23435be820f6 | -3.38553 | -54.68566 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc74cd7-589f-39f4-8b6d-f6d073d7f902 | -0.22356 | -51.64377 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| df2042d2-2fea-36e2-9472-6efadb8eb8af | -4.09018 | -48.86039 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdd79bc4-e259-3498-b022-49068bd9d701 | -2.04645 | -52.08768 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07d70642-a2ea-3cc9-b5d1-3d984aca4328 | -2.81805 | -57.12288 | 2024-11-09 05:20:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 237a86c5-b0b2-3ecd-8f2d-7a0cc7e97eb8 | -1.45868 | -52.56913 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1381481c-de72-3463-aee8-4e4f85a6dd5d | -2.30995 | -53.87103 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75cd3778-a92e-3a97-ab61-7c607556b296 | -0.38758 | -51.94231 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a60250de-5937-30d0-ba97-01bc16388c18 | -3.53925 | -51.10653 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ccb8dac-bad9-34ce-ae3b-959cf7726333 | 0.62188 | -60.09069 | 2024-11-09 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e93d5d5b-75d2-3351-9087-6095be6f1f1a | -3.82611 | -52.16619 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30b9c2ed-216a-3a08-b49d-0f696f875c20 | -2.80392 | -52.94512 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06aa8753-a3d9-3d81-aa43-c5206793d68c | -3.03005 | -50.35744 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc961d71-ded3-3187-827c-dcd14f9e446e | 0.62846 | -60.09299 | 2024-11-09 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e57a4d8a-55e4-3753-9d44-943dc9523a7c | -1.45842 | -53.41912 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 622e4bd3-9f23-3084-90da-89fa84d31151 | -3.06366 | -54.77952 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 072378d6-f8b2-3252-9b50-fab7680fc9be | -4.38169 | -48.58228 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58eb8368-e8d8-3354-9b26-337ec2a05b6d | -3.04138 | -50.32705 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b0fec61-84da-35c5-a908-9381bdccba29 | -3.75457 | -54.63995 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb16a529-2c02-3f2a-a3cb-6f9b86b38aac | -3.24028 | -50.45866 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 298db3d0-ae5c-30ca-aabb-519224ae1647 | -2.15063 | -49.14175 | 2024-11-09 05:20:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d45dfe02-9b6b-3727-a6b7-1e46e0edc57e | -3.58438 | -50.26961 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8cb6432-81de-34cf-ae47-c6141b7a9843 | -3.60492 | -48.92602 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff7a1fb-431a-3346-a431-3dfded4521b7 | -3.97037 | -48.17805 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 422b2725-5f35-30d3-94cd-91a62d6b8788 | -3.96402 | -48.17707 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b6c44b9e-66a9-3562-bb25-1e88e23718b6 | -2.94173 | -54.46026 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b3689e-04f0-3a65-bea9-86773d0b6951 | -3.25769 | -49.92595 | 2024-11-09 05:20:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb1d4d49-d6cc-3b79-82a1-2eec46339616 | -3.83522 | -50.04925 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3091bcd-9d6b-3e77-b266-271548639069 | -3.62236 | -60.20009 | 2024-11-09 05:20:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efa8f319-b423-31df-8b78-130df97ad18a | -3.12371 | -50.14848 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f685c6f2-1d65-346b-bb53-de9aa8844d5a | -3.5837 | -50.27757 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f070e445-3488-37d3-aef5-2047bb28a5cd | -2.54645 | -47.12889 | 2024-11-09 05:20:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6076c84a-d9ef-352d-a45d-88af33d0ce21 | -2.62532 | -51.29668 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 095f78a5-fe90-3c5d-b054-4e7c09e6cf91 | -3.11318 | -50.14311 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff6a7c01-9987-3bc6-8744-ab4f729725b4 | -3.04514 | -50.37812 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d6c788e-3279-3dae-b97e-7660e542e65c | -2.84008 | -51.80305 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32e283b-3414-3eed-bff5-06fad40b6703 | -1.82748 | -53.71706 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db5053df-3738-3be9-9938-7de206d33162 | -3.58455 | -51.20333 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d1a1817f-71c5-3232-9847-e4aa9a4fd578 | -3.09221 | -51.29344 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e37f744e-87cf-36c4-af0e-793383e6be55 | 1.78103 | -50.43397 | 2024-11-09 05:20:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 332af6ec-126b-3c79-9461-4aa9de43fdd7 | -2.40712 | -55.71251 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32a0f633-5da2-384c-90ed-877a510f6e06 | -3.11367 | -48.64158 | 2024-11-09 05:20:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a00e62de-599e-380e-90ed-2c5ae1c98ff0 | -3.45598 | -50.37605 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd320e39-bed1-3a00-9016-73ce579a4fd5 | -4.20388 | -48.54911 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5dc56b01-8a13-3077-8760-753b6aca1d76 | -4.19766 | -48.54811 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 80eb8569-0b82-3afd-a106-0503e5409cee | -2.73564 | -51.71774 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7d612ab-026d-3edf-8238-6171670fb73f | -3.23128 | -51.18993 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be5cce10-55dc-3301-b39b-b73c8287631f | -1.45227 | -55.27552 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a2f669-ddc7-3aea-befb-bde564d91bcb | -1.82991 | -53.72955 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49946ad2-79b6-3f98-a0d9-2b620356b6c0 | -2.96995 | -47.92904 | 2024-11-09 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39352d65-5d1c-37be-9a0f-19bd29f9e52f | 1.08578 | -51.30422 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86fee55c-5aad-33a6-8ecb-b0143279fdd2 | -1.40308 | -52.16361 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 379254a0-f8b1-3fb0-8148-7d9f08a29869 | -2.88041 | -51.47206 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55f59e40-fe25-3f71-943c-fd829c06bc6c | -4.38245 | -48.57715 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adc39074-7fac-3be6-9270-35387eda6d63 | -3.63644 | -50.18359 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f57e16e-953c-34e9-9c4a-da5f96ed0d06 | -3.58968 | -50.23775 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fec40ad9-32da-33c2-915d-0971d6ff1bb7 | -3.83683 | -50.0379 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9eae059-4e10-3969-bc39-bf7fb9a2e3ae | -3.58903 | -50.23703 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b4dc5f2-d650-329c-8d90-654ac03dec3b | -3.24676 | -50.45261 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df68795b-c322-3117-8d8e-8d14e3730553 | -3.52132 | -51.53054 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39eeac3f-c9cb-39cb-a877-d3cc8c7cc506 | -3.25066 | -51.13228 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a64ab8e8-309e-3440-9a6a-dc8b381f12fb | -3.07819 | -50.56689 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e7f0cbe6-a202-3307-84e7-fd7935771842 | -2.27768 | -48.73553 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78b399e8-ba88-389f-94ff-eb988b35db9f | -3.34931 | -50.26163 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93b56163-beb6-3dfb-b510-864980fe8edf | -2.91682 | -51.67509 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba3ff189-8433-3c54-b33f-404de5cd73e8 | -3.21864 | -50.38053 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96bb2a79-b514-359d-b3c4-5b5e48993b0b | -1.38837 | -52.71516 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87cfcedb-7eff-3066-8ef0-54aefc93b5c2 | -3.34525 | -50.36371 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7e56f28-1107-3fe5-ab62-06ac980ddbb3 | -3.83761 | -50.05051 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 564dea63-4d88-3c82-ad46-db1a9a834565 | -2.86152 | -50.32139 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b749ad38-ca75-394c-9ef5-536a0319ef6d | -3.03337 | -50.37225 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbdd516d-8e9c-35b6-acf4-b5b5cbef31a8 | -3.073 | -53.88214 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7cfcca41-8411-3f6a-9c1e-a8c07026d58d | -1.76569 | -55.10882 | 2024-11-09 05:20:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4356b4c5-70ff-3e7e-8f5c-0a2f710e01c0 | -2.36393 | -54.74784 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1501b853-b8e7-332a-ad32-f447a8abb833 | -1.6799 | -53.1811 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a277b6d1-ae20-3509-bba3-d7cc9b5e6a0a | -3.0147 | -53.42891 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6de97b0c-0274-345f-b95b-5108d1511406 | -3.47651 | -50.80853 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2a9269a-d62a-3b20-829e-903731a1ff44 | -1.2345 | -51.75847 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f331d9b-dc07-37a2-a6ec-a302cc5bfe0e | -2.8675 | -50.31863 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0a3cb5c-38a0-30f7-abc7-646cf2fb35d4 | -3.29599 | -46.41479 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d66e9f3-62dd-3bef-9fb1-66315b5fd739 | -3.23649 | -51.19048 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d93e507-3bb7-3cc2-b5ec-e10754aec6bf | -3.95216 | -48.16923 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 824da4e1-a8f0-34bd-b8f5-85fcd54e68a1 | -1.30462 | -55.72939 | 2024-11-09 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 380d6b7b-cf81-3f1e-a516-aaf096aa68a7 | -2.91956 | -51.04951 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f32d6d62-5689-3a69-a948-60701cb84122 | -2.23591 | -53.73071 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a45241f6-d812-3243-ad01-0ff1ccb3a902 | -2.69453 | -51.68849 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 208cc905-6a72-36dd-9283-acac08de40b0 | -4.20958 | -50.62171 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22cef984-cef7-3570-99e6-09efad429d03 | -2.45119 | -46.31144 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README107.md)
