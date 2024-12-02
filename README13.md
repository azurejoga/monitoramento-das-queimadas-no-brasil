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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aef40708-0ac9-310b-9875-3cc8cc6ced8a | -1.01831 | -51.72689 | 2024-12-02 01:13:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9586b457-2d44-381d-8e7b-355429d515ca | -1.69884 | -52.43475 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb32715a-15ad-3446-aaa3-3f7a9ddd53e9 | -3.28209 | -53.34945 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 31974ed2-8a88-302e-be88-2553e3788b5c | -2.69571 | -52.91279 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3d93dc07-03ac-3863-b499-c5b8dcfb406d | -3.20353 | -53.12207 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9cef710-ad5b-3166-96e2-d2669709165b | -1.37882 | -52.39141 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea550b6e-7104-33af-ba56-dc17343b55b9 | -2.63952 | -53.36584 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| fb28b904-e9ae-3baa-9e67-cd17733a196b | -2.01652 | -54.31255 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f0d8dd89-b7e0-3bae-acc1-5bea59d645ce | -1.65133 | -52.75441 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5845cd72-05e8-3a29-a52d-05cb2d4f620c | -2.61066 | -54.07801 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f9dd4bc-ece5-304d-ba78-05e050e1736b | -2.8632 | -53.98526 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3339f48e-a541-3932-8670-d87e0d2f125d | -3.3282 | -53.55034 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 01085808-d264-3c6f-8ae3-f360572b0963 | -2.55381 | -53.41105 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d7af7ab6-ff5c-37e2-a42c-2224adf5b342 | -3.28982 | -53.66372 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e6aa6d1-0fd7-348b-a6a9-369f57ed101b | -1.03547 | -53.55735 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b1bc6bc8-5965-3a26-b217-7be2859c42ef | -2.58857 | -53.99766 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c2e66abc-14b9-38bc-89ca-110ec6966b0c | -3.32697 | -53.54152 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b80c59e-a837-3bdf-a1cb-9e361626f000 | -1.44792 | -55.19574 | 2024-12-02 01:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 45dc5a34-a732-3c43-abcb-7917c496d488 | -2.71692 | -54.38729 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7c6a2ad-8e96-37f3-8db4-3612d28619ca | -1.30639 | -52.85609 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 93c0ad0a-b382-3558-a9d4-4379bd7f72f7 | -3.24605 | -53.62231 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3b43e30e-4237-3a7d-b0c1-dc3fdf1409d4 | -1.07563 | -53.44513 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 289ce5f8-8a2c-3a76-842c-eae16aaf856a | -1.59558 | -51.25372 | 2024-12-02 01:13:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a8de76fd-a9df-33ea-9c21-ad24faa647aa | -3.1091 | -53.10489 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| af72d725-8942-3c03-b892-98837287e410 | -2.54368 | -53.40342 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cf55124f-f9d6-3e41-8f32-35def1d2af3b | -3.12133 | -53.98467 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 950fd0e0-bc82-3015-94cf-527ec21011fa | -1.35212 | -55.16896 | 2024-12-02 01:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10dabe9a-7516-38cd-bc36-9a9a1ab8538d | -1.94575 | -53.34922 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35b44a13-c164-3d00-8f6f-aef539b5ef2f | -3.18834 | -54.33598 | 2024-12-02 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ede1a5b6-aaa1-3891-a2fd-ad9603caf18d | -2.56022 | -53.39203 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3fcae7f1-e5db-3713-80c5-c336fe9a55b1 | -2.30622 | -57.08966 | 2024-12-02 01:13:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7415f6fd-4869-3620-96cd-0d73ab29bdb7 | -1.68875 | -52.62875 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54fa5432-ec43-38bf-b737-fa90eb7606ad | -2.84373 | -54.10485 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 41b088f2-6ee1-3192-8187-34672411ecb6 | -3.24974 | -53.64877 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fd3420c9-7cf9-3200-a8af-b88c72abd686 | -2.81549 | -53.0463 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4d6bc279-405f-3054-9fda-26c1d8e47013 | -1.12453 | -53.2023 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0adfef68-5efe-3feb-ac3c-4c9f27def4a2 | -3.2536 | -53.93586 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3f5f7ab2-96be-3e36-a55e-32f4608800f1 | -2.73281 | -54.0998 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 26bfb597-261a-381b-8d3c-8a283e25deba | -2.37812 | -48.60757 | 2024-12-02 01:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| af5a9b44-49da-349d-8356-4a3e450f16ec | -2.79887 | -53.05781 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3d3868ce-d5d5-35e5-9ba6-b15d78ad5987 | -3.06669 | -54.04635 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8fd6bef2-9cdb-3df9-8159-58da74beb7f3 | -3.48523 | -52.1064 | 2024-12-02 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8fe72292-3103-3907-a5d1-3bf31abe1d64 | -2.62174 | -53.36835 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| db745084-71e4-3834-a5da-c0181bdf2686 | -3.46679 | -53.88457 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 86090262-b96b-3ffd-b6c5-826265c1474b | -1.49933 | -51.94131 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 96f78949-e72d-3dc9-9c34-093797f4ab1a | -2.79761 | -53.04883 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 572f6b17-c615-31b2-8f92-30c973ef3d86 | -2.61735 | -53.9962 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36f2ed90-9581-3b08-b565-1e6cba0b43bb | -1.27516 | -54.55238 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f31e46d2-8095-36b8-93bf-6f84f85c99b3 | -3.25737 | -53.6387 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cb05cd3c-c5aa-3d94-8f18-5239f7b65ac8 | -2.54728 | -55.22029 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d01e97cf-c35c-3aff-91a6-179d900a0663 | -2.38699 | -48.61637 | 2024-12-02 01:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 930d377d-66ca-32e6-bf28-b99d4b30de97 | -2.89069 | -53.97548 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01b3185d-05d3-357b-9e99-25d507914393 | -3.27206 | -51.1119 | 2024-12-02 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 89249a87-a216-334b-b9d5-8b7aa7fdcccb | -2.77676 | -55.34616 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0080af89-9c43-3745-b2df-c5488f3f86a5 | -3.25859 | -53.64752 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 94bdd1a4-1e42-31d1-acd9-475344571eb5 | -1.21601 | -54.19262 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a32ff57-e6fd-3683-a066-e44d7920e2cd | -1.33464 | -54.97858 | 2024-12-02 01:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4222f4aa-94f4-3648-b544-3ef394122134 | -3.17946 | -54.33725 | 2024-12-02 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8663b391-033e-3e9c-bed4-ea9140acee36 | -2.36262 | -54.48877 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bb2f5b7d-2c4c-3be5-9bc6-85d96d8f130f | -3.02983 | -54.1835 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 946e3737-051d-3d97-a0cd-012f442fa733 | -2.23434 | -53.69722 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a46c7b6a-d4c5-3c5f-8793-c07e873d835e | -2.80779 | -55.30699 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35ebd427-84a7-3daf-9394-62f65e787e74 | -3.02423 | -54.01328 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec761952-3a9b-37f7-bbbc-a9788ac384df | -2.88383 | -53.3308 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 61cbb110-2c32-3afa-bcc7-7f2cd9417d70 | -1.73563 | -52.63165 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 920d8230-c208-37bc-b8b5-1294058cf993 | -3.06952 | -53.67743 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 903a9024-9599-3c25-9506-fb5828cd7860 | -2.45478 | -53.62099 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 2cb2970d-3450-3511-ab24-82f59c50bb5a | -3.0998 | -53.23359 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 75f34f7b-e778-3f2b-b875-bbdd1edb54cb | -1.07688 | -53.45406 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| af5483b4-2b6b-34e4-bf5f-77a7e68847ff | -1.59714 | -51.26463 | 2024-12-02 01:13:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1b66f63f-c8ba-3ca3-9c8e-2e7b1bda3b20 | -3.52066 | -52.15919 | 2024-12-02 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 97079c34-fbc5-3bd3-8890-f91f3c2f8f01 | -3.36598 | -51.12454 | 2024-12-02 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3a2832a-cbfc-3a32-8c8d-f95cea9cd86a | -1.62525 | -53.88915 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfebc846-d5b4-3a34-9bd1-7424c4c153fb | -3.1122 | -54.04891 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2c866e23-5c78-372c-b81b-815c2960bc39 | -3.08657 | -54.12455 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8aa77717-259b-3e32-b858-a9897c3914e1 | -1.23047 | -53.36524 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7ca027d-6fa7-326c-a45a-fdf6aa798ca1 | -3.00778 | -53.23475 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e21263e4-11a1-3ba7-8254-5cea9df8d573 | -3.75624 | -54.51102 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05f0081c-97e4-3e85-9f84-fe59f066b869 | -2.83128 | -51.83836 | 2024-12-02 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 689a93c7-1a2c-3af9-8094-b6fea4711970 | -3.74855 | -54.52124 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4329b62a-d381-31b6-a2f1-d7f5477e5f9e | 1.2459 | -50.67541 | 2024-12-02 01:13:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1700f44-3be9-3434-9d84-85c22ad67a40 | -3.47467 | -53.8115 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89a9f4bf-422a-3efc-b6ae-b1b7c87b263b | -1.6164 | -53.8904 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cec0798e-20ad-3d03-9a57-c5af78f67209 | -3.42232 | -54.03169 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f357a776-2317-32e9-8808-14202b7ff1e8 | -3.09449 | -54.05142 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 598c4867-7b28-36fc-bd56-2b993cbe6608 | -1.72381 | -52.47966 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 57069c87-01a1-33f9-9e18-6a187340beb4 | -1.37746 | -52.38179 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ed9dd50-18c5-38ab-8921-1a17f680b6b0 | -3.11247 | -53.98592 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f97450db-9a89-303a-9e70-33d2418fed33 | -2.2696 | -53.61428 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 027a5101-9fbd-3d98-b1cd-25db9be438bb | -1.64937 | -53.86771 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d351a4c6-eca8-3d79-8841-b2ed508482ad | -2.89808 | -51.58776 | 2024-12-02 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7fb3bbef-9250-3410-83f3-bc0d5c2287c6 | -3.22117 | -53.83256 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 76ebf324-78da-3832-b3cb-55f1578df9b5 | -2.9103 | -54.11657 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 88e025c7-b549-3ecc-afd7-f9a65e7404e9 | -2.98172 | -53.90244 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5cf2584e-e2d3-323f-a719-822ee8c6bf42 | 1.60771 | -50.94712 | 2024-12-02 01:13:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b9685557-0e8c-3471-9646-3579d040f973 | -2.89993 | -54.17206 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fe98f092-9a9d-3491-a8e7-6f43fd09b63b | -1.95607 | -46.44708 | 2024-12-02 01:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1aba183a-aade-30ae-8de3-6a649779e451 | -2.79972 | -54.04812 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7c5120e4-ca66-3277-9e59-290d8be47445 | -2.80906 | -53.06553 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 31562bb9-b537-3167-9bb2-0138f242a740 | -3.0909 | -53.23485 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README14.md)
