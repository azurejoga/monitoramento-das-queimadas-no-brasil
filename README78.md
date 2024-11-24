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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aa17cdd-1255-3cf1-8fc7-4041ae870228 | -1.64758 | -53.87602 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 265ee55e-4216-3ea3-b9c9-2e6d658c8e2e | -2.94656 | -51.42859 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d4acf71-7f34-34bd-a175-0cfcc3e738d2 | -3.24545 | -50.11963 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f97d22d-2e3c-346e-93d2-4c7c7bed583d | -2.80537 | -46.80354 | 2024-11-24 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd6995f0-798e-3ec3-b43e-d4195abb3f95 | -3.20703 | -52.57297 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf129f9-a2d1-37e5-818c-7175e48fed02 | -2.14574 | -50.9173 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab2ee6b3-a1bf-3037-b831-61f0e2efabe0 | -3.25937 | -53.27209 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e414d3b-d2fd-3200-82e5-4f9eead9c8f5 | 0.08236 | -51.48904 | 2024-11-24 05:14:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18e700fe-0779-3522-b4a9-a648ee7542e2 | -1.1177 | -53.39567 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7c01d7e-ee15-31e1-adac-1c55bcd7a226 | -2.273 | -48.42756 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bd402bb-58c7-31f3-bb3f-676a61862308 | -3.20646 | -52.5768 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08a900f1-f3ed-3e6a-a046-8c1f9283ec7e | -3.56717 | -51.11412 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6524cc55-811e-30ae-807d-f93854c73184 | -1.42267 | -46.05617 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecbcf05d-7af6-33af-ab18-51c7fa9ef25f | -3.28107 | -53.83688 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f37749c-a740-3be5-9086-eec360b713e5 | -2.70167 | -46.28866 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8191307-8679-32af-a061-d2a4fcaed51b | -3.28585 | -53.85723 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea57916-416f-3fe8-82eb-0f749b8e9395 | -1.2645 | -51.76225 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0b52a71-cd18-3334-ad5f-036b99f616e0 | -1.81973 | -46.632 | 2024-11-24 05:14:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1b224ad-7bb0-3148-b6d0-512981d27a69 | -1.61261 | -53.30402 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 312f1a35-50c9-313f-9d3c-a76a52ee640e | -2.61756 | -51.80384 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ea43876-2d7b-3adf-a03f-f590498365f1 | -2.71665 | -46.27537 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f100d5d-4684-3193-962a-68b22b9c04d0 | -1.95299 | -49.52256 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16ba1344-2d41-3b22-832f-79e63a7dbdaa | -1.19692 | -51.77248 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3fe86bf-4bef-348f-a43d-4dc799a047f2 | -2.73716 | -54.39137 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f0b5bb4-4dea-388d-bcdd-0c291a5cda48 | -3.26953 | -50.62662 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 958f8b17-6856-3868-b107-e924945e2ec2 | -2.31503 | -52.1753 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8805713e-49b3-3fd1-88b0-2d9539fbd53e | -3.21845 | -53.38015 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17c4695e-72c7-33f0-ad52-7a852a41e202 | -1.44821 | -54.51295 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 039822d4-9567-3314-9268-3c8d1b834c73 | -2.75549 | -54.0685 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9ae8c8d-f377-32fe-bbce-cc14db23290d | -2.17938 | -53.63841 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 207a88aa-f651-39f4-ab60-9f5bb93e9eca | -2.6218 | -54.26274 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eaf0c264-fbb1-3ebf-bb45-1ce6b41e9610 | -3.27557 | -53.82104 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2004564e-9064-34b3-8bba-b1060cec3e8c | -1.40631 | -54.47102 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6533934e-9be9-34ca-b2b2-722d3c33fda8 | -2.78689 | -54.04044 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a2b80e9-4b9b-365a-b7a9-dcfd094d4f21 | -3.68108 | -47.12872 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2915d5e6-9ee3-39fa-8676-827a4dd36587 | -2.17827 | -53.78575 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 321013ff-2494-3bfc-8f1d-98c9428ec017 | -3.03944 | -49.44382 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1fa3f14-c4bd-3a9b-b149-45cd6b4d1f44 | -3.28659 | -53.85244 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6630bc8e-8bb1-35c6-8685-0965d1635c00 | -1.23693 | -51.74145 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a325b2d1-dc3f-36e6-9d5b-d8ecb6666c7d | -3.23909 | -54.23598 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15b44c95-0174-39f1-8828-164d92ff4884 | -1.21048 | -51.7415 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c07831f-90cc-3a7b-b5c7-4c4bcab2593b | -3.2405 | -54.22688 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb13d055-fc26-344b-b4b8-0f6f3d6eecb4 | -1.44984 | -53.40112 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cace414e-cf0a-318b-9d31-db6505b60a07 | -3.18251 | -54.32856 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f427c693-f2a0-3435-870b-933585520619 | -3.86267 | -50.05172 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 905ec258-6d82-3b13-bbc8-d6e587675b5c | -0.36103 | -50.02695 | 2024-11-24 05:14:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83bb7054-85ae-3152-8189-dd9eb99d61ab | -1.2602 | -51.76156 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb139dae-c89e-3285-9c49-89cd1079e0af | -1.40267 | -54.47044 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5cc9947-e58a-31ac-abd0-75bbe8209dab | -2.96917 | -53.86017 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cd3c95c-e385-3d01-8868-28ff3bb58e73 | -2.62058 | -54.93486 | 2024-11-24 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6135a98-8a18-39ad-89dc-de7485c5aab9 | 0.00929 | -51.18841 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9fe0412-74ad-38d0-a754-bccd32a5e6eb | -1.72419 | -53.25191 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec1b2b48-7936-362b-8734-6f3276091917 | -3.13771 | -52.98237 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12729a79-67c0-3282-80f0-12bba42937a0 | -2.08258 | -49.61167 | 2024-11-24 05:14:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 727d9dfb-c1e9-33ac-92be-048db8cd660d | -1.12224 | -53.58214 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 53cfe351-6f29-3845-872c-db412d9e64da | -3.07329 | -54.5579 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8bffe40-0d44-3884-b415-97d8ef55e605 | -1.54777 | -55.90428 | 2024-11-24 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 26c7fc81-b5c2-3b82-abd4-f3b0e8987b48 | -1.45299 | -53.40649 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 27c30be7-1dd9-3e4e-a46d-6b58b0aac768 | -1.45304 | -48.20265 | 2024-11-24 05:14:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 229a084d-5e3c-3593-b6ef-a47ec5465435 | -1.9645 | -48.38852 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23d75599-4cb6-3455-9af6-48d7415d6c01 | -3.24407 | -50.66489 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d49862ab-d03a-3928-a9ca-c9e4af12a9e2 | -1.98663 | -53.13248 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 168ad074-9768-33f7-96c0-a1664f4b8ebb | -3.11797 | -53.11087 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd5b9878-7385-34dc-a665-c378e0ecf9c0 | -1.25781 | -51.74879 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d187affc-ddde-3097-a9bb-d0d85cce85ba | -3.29431 | -53.85364 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a46bb4c6-4db3-36ac-9245-00ac5b70dfd8 | -3.29452 | -50.36563 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8256cb6-bd7f-3d71-8619-0108fe77cbbd | -3.25032 | -53.27771 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9926fc7-b891-3fb0-86ea-45ac9e05185a | -3.0433 | -49.45366 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3efe4b12-5434-337b-9185-7a8f6f687e26 | -1.45024 | -53.39447 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e558927-c9aa-3e30-ac74-4a509a876134 | -1.63845 | -53.31784 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e758aac7-a3a3-3fb0-aff0-afc85ccda606 | -2.16539 | -53.79325 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff5a3605-4567-3f4d-aebf-55314e63c102 | -3.8209 | -52.23497 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8511ec7-7ef4-30f7-b869-05824a8c51df | -4.25479 | -48.69217 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b36839a-dc1f-3f2c-aff8-b1f7f143179d | -4.03212 | -54.18653 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee5a1674-c359-30ff-814e-057f0ea99898 | -3.50163 | -53.80552 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d05e69cc-b039-32a9-b25d-50cecc42e153 | -3.97736 | -49.928 | 2024-11-24 05:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57f935f3-741c-376b-8da4-c718816398cf | -4.08873 | -54.7565 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ed40ed1-b0bf-30e9-9635-9f08e7ca5fa4 | -4.37748 | -49.7514 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e22b0a-e0d3-33fc-8597-6f4ab97b6654 | -3.18299 | -54.76652 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcfed68d-5cc2-3728-bfd5-6c17fe8cb52b | -3.81548 | -51.99893 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26a8399e-891b-3b9a-910f-f122e5abd01e | -3.24498 | -54.22291 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50954107-4759-3a63-ae16-93fc2bfa662d | -3.64287 | -52.25298 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6082c6c-350e-3040-8f6d-c37c49384e23 | -3.6644 | -51.71867 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ab455b9-ca62-303e-b7e7-6b541df5e305 | -3.50333 | -53.82036 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 789a1fe8-6bdb-3e53-8394-e8aaef265c45 | -3.20517 | -54.88512 | 2024-11-24 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7b2eef7-ed03-3309-9136-095edeba5dfd | -3.89028 | -50.07362 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a8b277c-f14d-3bd2-9c37-f203ca5badbc | -4.11883 | -49.44011 | 2024-11-24 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f98a0b11-1312-3d8f-888b-d3c4c841d010 | -4.09546 | -51.07276 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80ac3357-6607-3312-a684-21f96dc39b6f | -4.12697 | -54.20597 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e45ba97b-8741-38a9-adb7-8606cd2a7b64 | -4.88605 | -48.90435 | 2024-11-24 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e5cbb27-530c-31c9-88b9-953c1a4d7978 | -3.51502 | -53.82187 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8269c979-83a4-3942-9084-5d980c38268f | -4.23393 | -48.63955 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5bbc3fc9-c9e3-3aae-b272-e47679f026b4 | -4.37328 | -49.74762 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2515f5bd-2475-3849-9e68-01283f42e7e0 | -3.80459 | -51.3364 | 2024-11-24 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea180d47-9dc7-3caa-9e20-76c22b8c01d9 | -6.22371 | -55.65712 | 2024-11-24 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 29fd7c06-9135-391d-8bb2-8a42d0e73034 | -4.69831 | -45.84757 | 2024-11-24 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7141cbe4-d35b-3e70-8d7d-b7e59abcd511 | -3.25182 | -54.22862 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc44067f-ea61-3f6f-9a72-52473d169500 | -3.52039 | -53.81276 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35512649-f9af-39e6-9a1e-742b5c28db33 | -4.51885 | -45.71974 | 2024-11-24 05:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79f5062f-432b-3bcc-ac15-e6ef4259a7bc | -5.19203 | -49.15231 | 2024-11-24 05:16:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README79.md)
