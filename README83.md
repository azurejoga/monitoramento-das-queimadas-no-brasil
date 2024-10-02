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
| 0c3d1139-6cce-3050-84b2-306a1cc545da | -2.87895 | -49.14883 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3f4b582-39a7-3f33-9c36-3328c4439bc5 | -2.40118 | -50.3276 | 2024-10-02 04:44:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9d271a7-c1fa-35c3-b23d-daa972ec24a4 | -2.40064 | -50.33103 | 2024-10-02 04:44:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60462cff-1ce5-3a7a-b824-61c01485e27a | -2.39458 | -50.32658 | 2024-10-02 04:44:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09110826-c8aa-3352-bffd-d403ac8449b6 | -2.39404 | -50.33001 | 2024-10-02 04:44:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2630a509-1c7f-3ca4-932f-cc258388109e | -2.38799 | -50.32556 | 2024-10-02 04:44:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69d20a20-5f96-3b69-9151-8864cdb655b4 | -3.56681 | -50.58242 | 2024-10-02 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8132088e-91ab-314b-971f-6b2218840054 | -2.88346 | -51.67456 | 2024-10-02 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8a68206-b249-3b4a-ae4b-821618b20ae2 | 2.13539 | -50.91151 | 2024-10-02 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51bccd33-ce21-3963-9f91-ff82beb8c500 | 2.13199 | -50.91203 | 2024-10-02 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d4264d1-6bdb-36c3-8235-424f89d151b7 | 2.12032 | -50.67239 | 2024-10-02 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6e6c94d-7a50-302e-9b3e-fa9902a663b3 | 2.1195 | -50.89896 | 2024-10-02 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29007a2d-df8e-3430-87f4-068c0af36c66 | 2.11694 | -50.6729 | 2024-10-02 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e7e819a-83bd-3020-bda7-0f256e972be3 | 2.1161 | -50.89949 | 2024-10-02 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26e7c0f9-1de8-3111-b407-9164a05406a3 | 2.11327 | -50.90366 | 2024-10-02 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48615c43-1b5b-393e-9afa-f9506d43de23 | 0.99155 | -50.06521 | 2024-10-02 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1366b164-15d0-3b9e-9ddc-3d964de3ce33 | -2.8829 | -51.67814 | 2024-10-02 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb187dde-ccde-380f-bfd1-410a3106b36c | -3.32736 | -50.78385 | 2024-10-02 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f304fc3-ba33-3825-8c9b-adf05c47c314 | -3.22063 | -50.79181 | 2024-10-02 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7d54c7d-7fd6-3d45-97bf-0824a04a2b67 | -3.22008 | -50.79526 | 2024-10-02 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c8ca3ef-0d6f-33f2-b95f-5b66ce26af51 | -3.78647 | -51.32501 | 2024-10-02 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3ca19ce-067b-3a0b-ac9d-d5faf71703c2 | -3.78315 | -51.32449 | 2024-10-02 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 174afe9f-ab63-3a26-9b4b-dc60b575f5d8 | -3.07062 | -54.77527 | 2024-10-02 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a2fbe40-ce85-3aeb-80b0-33b74dd4d1dc | -2.65684 | -54.61996 | 2024-10-02 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a76e44e7-b04e-33f4-9b61-341d97a1636f | -2.65606 | -54.62479 | 2024-10-02 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6660754-5d47-35a7-a91a-107c196e61a0 | -1.50802 | -55.37538 | 2024-10-02 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0ddc93-2aa3-3f97-96d8-a8d17933cc4f | -8.20708 | -44.35516 | 2024-10-02 04:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 94f5c323-caa2-3a93-b2ae-e8dc02a4c129 | -8.19902 | -44.35919 | 2024-10-02 04:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1a4c00de-92ff-3625-83f3-52cc99ad2858 | -8.16316 | -43.68351 | 2024-10-02 04:46:00 | AQUA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 02cde549-21c1-371d-95a9-e997a6044e36 | -7.7197 | -45.42119 | 2024-10-02 04:46:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| afe0c902-8148-318c-82cf-5f21dc7d3ced | -7.71599 | -45.44375 | 2024-10-02 04:46:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 576cc277-3dc1-366d-82ef-4f136dca84c7 | -7.70615 | -45.41957 | 2024-10-02 04:46:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 2edfaa40-2a42-3f03-bd58-4167e66e7468 | -7.70072 | -42.98148 | 2024-10-02 04:46:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| d4edf14c-620e-31f7-acfa-146d6166921e | -7.69836 | -42.99597 | 2024-10-02 04:46:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| f88cc153-5124-3459-8ca4-af6326d4a95f | -7.07562 | -39.14746 | 2024-10-02 04:46:00 | AQUA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 6a99cdc0-8231-3803-99b3-c03cacbcb393 | -5.20044 | -37.6255 | 2024-10-02 04:46:00 | AQUA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e8a11018-1685-35cc-b56d-7760706fd9e1 | -7.17371 | -46.94754 | 2024-10-02 04:46:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| e2a7d0e4-5a05-3d70-82e8-8323ef363b45 | -6.59624 | -44.1723 | 2024-10-02 04:46:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5308150c-af4f-30fd-bdbe-10bc2c704ca0 | -3.20775 | -46.7779 | 2024-10-02 04:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| d7a5fbf1-10fc-3904-9727-81a6c8ca3191 | -8.43572 | -41.93417 | 2024-10-02 04:46:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 719a5b70-15bf-3f7a-8309-c02f340b2efa | -8.43526 | -41.93767 | 2024-10-02 04:46:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 68e7dfa6-5977-3709-83ff-3d046bb3ac24 | -8.42971 | -41.93763 | 2024-10-02 04:46:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8f5ecb87-efc4-32d7-89ab-04372af34457 | -7.87855 | -42.66994 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 06f74c57-14d9-37bc-96dd-1fc33f9b36fe | -7.8734 | -42.66916 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9bfd789-ff6b-3e4c-bad8-939a78d26fe2 | -7.87298 | -42.67229 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0164c815-580f-34a6-8227-cbba501793b9 | -7.87135 | -42.6679 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 755d0870-cd78-354a-b7f8-2e14fbf194b6 | -10.79692 | -45.5602 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 980cbd84-4322-3b38-8425-7da123f0ae7b | -10.79251 | -45.55957 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0f7943b-f1b6-3f92-a450-b8346affd7d5 | -10.87495 | -45.96548 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09b42fab-5aa9-3fc4-a446-66e68fb36eb6 | -7.55481 | -45.15506 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fdae719-89ce-37bc-a17b-3f2b3209062e | -7.42865 | -44.83617 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cef9cc63-284a-3dcd-ae1e-c43dad54e235 | -7.4236 | -44.84 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a16329a-9eab-392b-9aae-c88f1ee7d785 | -7.31831 | -43.8226 | 2024-10-02 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b9ac30c-3d15-39a6-b46a-b1bd0d8a318c | -7.27417 | -43.81536 | 2024-10-02 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19d8fda3-c92f-3584-8cd9-7eaf6ddda0da | -7.26958 | -43.89781 | 2024-10-02 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59b3cfe0-5552-3e8f-bc5a-65427aebfb46 | -6.49886 | -43.82888 | 2024-10-02 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f5573cea-e8c3-3176-8995-30642c32aab2 | -6.44509 | -43.97353 | 2024-10-02 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fe78876-9d20-34c6-aa24-52bfe1f0811f | -6.44442 | -43.97826 | 2024-10-02 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fbf89f1-06dd-3763-a1f5-65ab19f9345b | -5.94558 | -43.69596 | 2024-10-02 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c7337f9-9b92-3c01-94e6-5a449531fc76 | -5.88662 | -43.72089 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f863384-bb6f-320a-b306-5158d6744ac7 | -5.8859 | -43.72581 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cb50714-d3c8-3b57-86be-f3b105b3e462 | -5.88197 | -43.7202 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b8cf9a0b-72c3-396d-9d01-8ee6e1058ee3 | -8.16174 | -43.6645 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9944f5e5-6328-3af9-8b32-4a573755d927 | -8.16079 | -43.66463 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f12978bb-7812-30e2-8d5e-e993678e5450 | -8.1588 | -43.68543 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a6f040c-b08c-3373-bb29-b319c24e2cc3 | -8.158 | -43.68569 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d5c3be2-4999-3d99-b01f-8b958f4c0169 | -8.05927 | -43.91051 | 2024-10-02 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3acd5f11-696d-3d93-82d6-5a54b37f4ca6 | -10.12372 | -43.92542 | 2024-10-02 04:46:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34caee40-8271-3af7-9ab6-80bf834708bd | -10.04981 | -45.6428 | 2024-10-02 04:46:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74728cbc-3f60-3d0c-8492-85ac14148539 | -8.15 | -42.90572 | 2024-10-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f707a631-a253-346d-acae-9f42b993b1f6 | -8.14489 | -42.90514 | 2024-10-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 03ebcd8e-7fdf-37a3-8736-45ef9742bacd | -8.14449 | -42.90808 | 2024-10-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6df9b736-9f57-3f6d-b660-145e059688bc | -12.07804 | -38.9707 | 2024-10-02 04:46:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b3d904e6-7dcc-335f-9115-f3d962efa819 | -12.07742 | -38.97221 | 2024-10-02 04:46:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| df11cf49-0d20-3687-8465-a817e9c0c909 | -12.7197 | -40.2179 | 2024-10-02 04:46:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc4235a0-4b3d-34bb-821d-7698ec04cae5 | -12.71908 | -40.2234 | 2024-10-02 04:46:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ba0f65a-eb9f-394b-be0b-30ba69bc5860 | -12.71327 | -40.21695 | 2024-10-02 04:46:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 707c6cf4-e6da-3a91-b1ad-caa0d826222b | -12.08389 | -43.8925 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 680b1905-72d3-3da6-aa4a-2512dbb6d48e | -11.88501 | -43.81201 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6360b95c-872a-3029-ba73-2772e6908307 | -11.88462 | -43.81498 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e261a918-c177-3558-aa48-f93e11989fbb | -11.88424 | -43.81794 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c4cc3cf6-32aa-3c4e-9b4f-2bea259c8d0e | -11.87996 | -43.8113 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d586ba6c-7761-3d7e-b576-b756a2d9d95e | -11.87958 | -43.81425 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7814a722-44fd-38bf-91c6-911cfff436c2 | -11.8792 | -43.81721 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af7b8491-76a9-3adc-8d1a-d1020ae0146b | -11.2709 | -43.38676 | 2024-10-02 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0074872-3420-31fb-9a7b-9f499277fe82 | -11.26575 | -43.38603 | 2024-10-02 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c463f2f4-b454-3619-9e80-5cb5a057a670 | -10.87437 | -45.96959 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 259548ef-b270-3edc-a446-9eb53fca6fd9 | -10.87318 | -45.96736 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4749c4fd-3a4b-33e5-babe-f303580bef98 | -10.87123 | -45.96073 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96822ae7-b154-3f0c-9a82-9970e434638e | -10.87066 | -45.96486 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c80e7cb-db22-30ad-ac6c-0acddb41ef27 | -10.86943 | -45.9626 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1629d8d1-7ce5-34fb-b8a0-fd64a39672f8 | -10.86694 | -45.96011 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 687373ac-f873-3d31-8b2f-7157f996eef4 | -10.86514 | -45.96196 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ded7e7b7-b9b2-3cee-a40e-6d7ac014e1fd | -10.86265 | -45.95948 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 748e937e-110d-3675-89e2-d2ed90368cf6 | -10.71243 | -46.16926 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4d23051-1230-3ba0-a6ac-fd8f8595f0bd | -10.71185 | -46.17341 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92dff30f-ff52-3ae5-9264-c2e90c22bb87 | -10.66749 | -44.50472 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 227d76db-b6de-375a-b862-f05d74c57520 | -10.66343 | -44.49892 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b706d8c7-8846-3722-9b15-c63eea11efb6 | -10.66276 | -44.50407 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 80b05ba1-504b-3adc-bce6-4a0419316220 | -10.65802 | -44.5034 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README84.md)
