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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d5e303c-c3f4-3a32-b537-9f38e907c18d | -8.01885 | -43.14806 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 66b2ec70-da6a-32ea-8f59-4f65596707a2 | -8.03253 | -43.12496 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.4 |
| d1ce3431-ecb6-39c4-8e98-6dab87d4063c | -12.65847 | -44.49491 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| e95a7f1f-ee81-3aaa-9796-6c8e117b4004 | -11.94296 | -46.67122 | 2025-08-02 05:53:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ef7cbca9-05f4-38da-a12a-57f81c298e75 | -12.6701 | -44.48455 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e32387d3-167b-3d7b-a513-c16673f5256f | -13.05658 | -47.43938 | 2025-08-02 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67cff464-83bf-34d4-8735-f711b0e1ccb3 | -10.58711 | -45.25909 | 2025-08-02 05:53:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f4ca6370-19d7-3731-b9c7-83e7bbeb2614 | -9.39214 | -45.49304 | 2025-08-02 05:53:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 96d1dfc4-52ec-3f29-b062-378fd7e7cba4 | -9.39075 | -45.50253 | 2025-08-02 05:53:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 89fe9b33-d389-3e04-8cee-9b976525e4e2 | -12.6636 | -44.53139 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c0a57dd8-a370-3c18-ab35-97cf1c72e97c | -12.66848 | -44.49628 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| b511cce7-99f5-3bfe-9323-59f77f64fa31 | -9.08483 | -45.89254 | 2025-08-02 05:53:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c38db25-dc43-3fc3-a49d-50c0026d2d75 | -12.67399 | -48.0868 | 2025-08-02 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ee0c5608-67d4-39d1-a8fd-24a5d260807e | -14.21744 | -49.05325 | 2025-08-02 05:53:00 | AQUA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 129ab53d-78d0-395d-9250-d885df4c2bd5 | -12.66685 | -44.508 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 15f34124-bc9e-3492-a80f-3626e356c150 | -11.94162 | -46.6804 | 2025-08-02 05:53:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e734c97c-fc10-3682-a731-c9f38ac98018 | -12.67357 | -44.53279 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0895e7a6-0201-35c7-9604-c8b4cb68cfa7 | -12.65685 | -44.50664 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 1f1dbe7b-7fca-31d2-a715-d81bed671ff0 | -12.6601 | -44.48315 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 49b0781c-a329-3eac-912d-3a0d470a20bf | -9.05874 | -45.05497 | 2025-08-02 05:53:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| abfda28d-09cd-3a99-a713-13f3766c6b3a | -9.04807 | -45.06361 | 2025-08-02 05:53:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 584ee96c-45ca-306c-a84a-4f75de7bedf2 | -9.18984 | -45.29499 | 2025-08-02 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3bc74634-5500-35a2-98de-ace889e13c11 | -9.19123 | -45.28533 | 2025-08-02 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4c1733d9-580e-3140-bc1c-8cac22b99686 | -12.64847 | -44.49353 | 2025-08-02 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 215c4189-22a7-3095-b02c-d4dc8c0018ca | -23.70605 | -51.65224 | 2025-08-02 05:55:00 | AQUA_M-M | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 615bc6b3-e330-3ce3-bed8-7d304d0efb92 | -21.14621 | -48.01105 | 2025-08-02 05:55:00 | AQUA_M-M | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f49976f1-62ba-3383-bf1d-a3a8771aebbe | -29.77751 | -53.84128 | 2025-08-02 05:57:00 | AQUA_M-M | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 13.4 |
| a130a143-e2bc-31f2-a839-ceaf5d7746cc | -29.77571 | -53.85209 | 2025-08-02 05:57:00 | AQUA_M-M | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 7.9 |
| 3e7217a7-b7b8-3e36-b960-c5e445ddf7c7 | -12.6595 | -44.4882 | 2025-08-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 51f2d154-9068-3dff-8962-457740bacc9f | -12.6702 | -48.0815 | 2025-08-02 06:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d5cc22d0-50c3-3319-9b72-ca3900052a23 | -12.6784 | -44.5085 | 2025-08-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 53534260-88fa-320d-b07c-c1f46d1a5f6f | -8.0321 | -43.1257 | 2025-08-02 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 6d66d785-104c-384e-940d-7345bd76c13f | -12.6789 | -44.4851 | 2025-08-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| fcd0bf36-0d5d-3c1b-880f-220caa6a75f6 | -12.6591 | -44.5117 | 2025-08-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| a1b46b8a-78b4-33f5-a363-a884c31db01b | -12.6595 | -44.4882 | 2025-08-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ba66bf80-b530-3785-b08f-298b1519080f | -12.6591 | -44.5117 | 2025-08-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 06ca79ec-323f-3c93-ad4f-635734f45e96 | -12.6789 | -44.4851 | 2025-08-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| bb7b6d34-4d74-3ee7-af16-bdb910010752 | -8.0321 | -43.1257 | 2025-08-02 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| cd320c45-2046-39c9-b531-e978bd1fb7c6 | -8.0321 | -43.1257 | 2025-08-02 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 9b933083-d4a2-31bd-8a55-59b5c10ec6bd | -12.6591 | -44.5117 | 2025-08-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| f0089e0d-c843-367a-a43c-824dbb43674f | -12.6595 | -44.4882 | 2025-08-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c141ba24-a849-3155-9561-6aeb4d031cd2 | -12.6789 | -44.4851 | 2025-08-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8e87acc6-05cb-3a15-867c-e64e47360f9a | -12.6789 | -44.4851 | 2025-08-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 4c7e0821-0a29-3d95-abf7-7ab3dcc4f6a6 | -12.6595 | -44.4882 | 2025-08-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3410f80e-ece9-3802-a48f-5ccb908fe612 | -8.0321 | -43.1257 | 2025-08-02 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 4920cf28-d9ff-30ca-b6c8-b902364d144e | -8.0321 | -43.1257 | 2025-08-02 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 661a7070-645a-304d-931d-12d6eb00f70a | -12.6595 | -44.4882 | 2025-08-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 28dc1abe-666b-39d5-afd7-5b673fc6537a | -12.6591 | -44.5117 | 2025-08-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 7e760898-a9b9-3ada-ae0c-5bd75062c979 | -12.6789 | -44.4851 | 2025-08-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b6eb8fc2-28ae-3991-86c5-d7fb827bac52 | -12.6789 | -44.4851 | 2025-08-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 23c0ee83-db95-3910-aecd-045ea0576f58 | -8.0321 | -43.1257 | 2025-08-02 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 2636ed7e-d396-3a76-b332-8f0ebfc32aef | -12.6595 | -44.4882 | 2025-08-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 9b69d954-8914-3eea-ae1d-b638c8e9cce4 | -12.6595 | -44.4882 | 2025-08-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 63807080-bb84-3be6-a359-21761cdbfe3a | -12.6789 | -44.4851 | 2025-08-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ff4fc40d-e898-3891-b46a-7990bc8012ac | -8.0321 | -43.1257 | 2025-08-02 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| f5dbf0cd-d25b-3eec-be78-cc49e4914298 | -8.0321 | -43.1257 | 2025-08-02 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 1e30c130-8650-3f2d-bcb2-8d7dfb19892b | -12.6789 | -44.4851 | 2025-08-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| b53cd0b6-abe0-3138-b265-13e72045b96a | -12.6595 | -44.4882 | 2025-08-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 20693a8c-ed9f-364f-80b8-412b35612c1c | -12.6595 | -44.4882 | 2025-08-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| fd138977-4861-3c8e-ae78-727ea598c1d8 | -12.6789 | -44.4851 | 2025-08-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 02918a84-c019-3d62-a64f-f6d39c85c6e6 | -8.0321 | -43.1257 | 2025-08-02 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 1951d799-5c44-3830-9861-2bb3622822ff | -8.0321 | -43.1257 | 2025-08-02 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| d723e150-4521-3603-9278-7cd9d678a650 | -12.6789 | -44.4851 | 2025-08-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| d61d3dd8-662a-3930-8188-bfa0fe17d326 | -12.6595 | -44.4882 | 2025-08-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b54f3952-51a3-3b92-a09e-737b0b89c818 | -8.0321 | -43.1257 | 2025-08-02 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 29288258-21e8-3fcd-91f6-1dd5c0bcc2b5 | -12.6595 | -44.4882 | 2025-08-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 59f9c2eb-309d-3bad-bb55-e0eb7c6ac94a | -8.0321 | -43.1257 | 2025-08-02 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| f49ff9cd-dc75-3720-9ac2-8a544dc23c9b | -12.6595 | -44.4882 | 2025-08-02 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5a0ba88a-301f-3d6f-8719-143f59de3ce2 | -8.0321 | -43.1257 | 2025-08-02 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 69a46cda-b3d9-326f-9569-869be9d10fc4 | -12.6789 | -44.4851 | 2025-08-02 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| d4d4647d-c824-352e-ba6f-73d311c65514 | -8.0321 | -43.1257 | 2025-08-02 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 91b26d80-1d32-3e02-82e2-cabe563393c6 | -8.0321 | -43.1257 | 2025-08-02 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 09f566d1-223c-3bba-ac6f-af0f2dd6eaf2 | -8.0321 | -43.1257 | 2025-08-02 10:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 3d3da9fd-954b-3648-b5a8-569aab8e450c | -8.0321 | -43.1257 | 2025-08-02 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| 8906d298-b5f7-3bad-95a5-cdf9d638e0a8 | -8.0321 | -43.1257 | 2025-08-02 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 4d0dad1b-4582-30e6-a3aa-4410eb17fd0b | -8.0321 | -43.1257 | 2025-08-02 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 17604fe3-3c1a-39ac-be80-ca4f49a0f962 | -8.0321 | -43.1257 | 2025-08-02 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 681ab166-9636-3f69-ad8c-7b23b5a28a53 | -8.0321 | -43.1257 | 2025-08-02 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| b648ce6c-a643-35ec-b278-893535270883 | -8.0324 | -43.1022 | 2025-08-02 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 9713e602-3278-399e-ba35-253708dc4765 | -8.0321 | -43.1257 | 2025-08-02 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.9 |
| cd1b0f85-3951-35f4-8c58-276bc84a3bb0 | -8.0321 | -43.1257 | 2025-08-02 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 203.1 |
| 8d37cb16-dc40-38b2-a30d-7f89fcc4d06a | -8.0324 | -43.1022 | 2025-08-02 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| 53bf3c4f-2206-3606-9c45-3869b8dfe04a | -14.1672 | -45.4673 | 2025-08-02 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 604b6011-b5dc-34e8-a09e-5fb6397cc778 | -8.0324 | -43.1022 | 2025-08-02 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.8 |
| 5e9b5f5c-8fd6-383d-90fe-39aed86b045d | -8.0321 | -43.1257 | 2025-08-02 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 226.6 |
| 6403b202-37d0-353a-a21f-be66d0defe15 | -8.0513 | -43.1001 | 2025-08-02 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| e41a4049-aaf8-3818-9c80-a80c9cbe8b25 | -6.61385 | -37.62923 | 2025-08-02 11:51:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d78dac1c-1872-3480-8069-2eed471be01c | -2.88157 | -40.29747 | 2025-08-02 11:51:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6a7b127b-c659-3985-971c-5cb6f4a5f635 | -7.85806 | -44.21614 | 2025-08-02 11:51:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ec06c7df-47c9-36e6-9a2f-e92b1b69d464 | -8.03639 | -43.12741 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 44326933-e51d-36aa-94a0-7da607446589 | -8.04817 | -43.11729 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| ce6f36aa-7242-39e0-a961-020310c80e1d | -8.04993 | -43.10569 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| f84d39ce-aa92-33fa-809f-f815f23c7677 | -7.12281 | -40.07787 | 2025-08-02 11:51:00 | TERRA_M-M | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 977e59d6-3c66-3120-8177-a5f5cb6a044e | -6.07184 | -42.34486 | 2025-08-02 11:51:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f07e2ea8-d95a-3261-80e6-e9d2dd46ec59 | -8.02815 | -43.11432 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| ea3bbc36-9766-354d-9d15-975e60930f51 | -8.02459 | -43.13756 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 0cd273b7-cba0-3df3-a5a5-af500aacb5ac | -6.39684 | -37.99435 | 2025-08-02 11:51:00 | TERRA_M-M | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5e0a5c09-0f05-34e6-adeb-774f63d97121 | -7.84719 | -44.21434 | 2025-08-02 11:51:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| f17f542a-7e46-3fe2-b4ad-0db4b8108103 | -6.68394 | -44.35249 | 2025-08-02 11:51:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 04969046-f873-33e9-9d53-b56f46c8297b | -6.70053 | -43.34647 | 2025-08-02 11:51:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.3 |


[Clique aqui para ver as próximas entradas](README25.md)
