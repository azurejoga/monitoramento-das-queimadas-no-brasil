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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aabd55a2-4b54-3523-9c80-9abdb3136af7 | -3.88312 | -51.0307 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5e51632-c2a9-3ff2-a06d-66dd0139e42c | -3.88288 | -51.0382 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfb74f7a-25da-382e-a4bc-54ed34d42fae | -3.88243 | -51.0354 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0405e743-c437-360b-a64b-09f4f329f034 | -3.86918 | -52.20196 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dc36fe9-9df0-3439-8204-c45531963cda | -3.86794 | -50.90526 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 732a6bd0-1b0c-3c95-baaf-82a40649450e | -3.84458 | -51.39552 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d6bf472-630f-319f-b684-65637ebcb249 | -3.84287 | -52.0845 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70f91b2a-77e0-3dc5-b92c-a22c7ea47fa0 | -3.84225 | -52.08867 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84291389-1f28-35ef-9cee-d8d33e9e93b3 | -3.84111 | -50.97887 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83feef0e-2452-3386-aa84-a28453c12af9 | -3.83728 | -50.97829 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bfbb664-cbda-30c1-aacb-ec13125086b3 | -3.81553 | -51.25023 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e56aef3-2ba8-3b56-8ce9-55c67479438a | -3.8128 | -51.16643 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42f29161-5299-350c-b7b5-c1030c571bee | -3.80971 | -51.16127 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9007da9-47a2-36b5-8321-5d77e585bdb4 | -3.80902 | -51.16588 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6430dde-266c-32f1-87f3-a5363d20c124 | -3.79989 | -52.25441 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28c78bff-7eaf-3408-9b84-591fc93b2606 | -3.77127 | -51.05461 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a4f4ec5-0475-3192-bd1f-0dd30c8278a6 | -3.77124 | -51.05765 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72d4973b-5249-345d-a9e7-6456f720de33 | -3.76289 | -51.06133 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00c64e85-08fd-3dfd-a68b-f223c064f1c5 | -3.76226 | -51.06303 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92fcfa93-cc9d-3344-860e-0e7b89b692eb | -3.76218 | -51.06593 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b1fdb57-0749-3098-91e8-b0d960bcf6a5 | -3.76024 | -52.22748 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36ab79da-3a92-3fae-8f0a-09bf2d9cdbd6 | -3.7591 | -51.06067 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76bc3d9f-6a66-3b31-ab18-37126553621b | -3.75839 | -51.06528 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 211bba5a-06bf-31e3-b7ac-40c6bf60f342 | -3.71072 | -51.61657 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e796f63-84ff-3f71-b98c-5e17fdcc9602 | -3.71007 | -51.62096 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b0c669c-8c41-35d8-9859-6ecc9548d42f | -3.70869 | -51.21313 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a21245b-c329-3413-ac42-a8035aa43f64 | -3.69536 | -51.17379 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52014396-6dd3-3cdf-bd91-74ecff16784a | -3.69475 | -51.12651 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92203403-2460-38b8-807f-25ffbb44a011 | -3.6916 | -51.17317 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6aee18b8-427b-3bd5-83b7-d8eb52bfd7dc | -3.69091 | -51.17773 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 426a4360-a543-37a5-8142-f4d60085ca8e | -3.61826 | -52.20714 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 705bc01b-e10f-3e90-b470-96df59600871 | -3.61765 | -52.2112 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c2ceeca-aef5-3e65-9664-70230ac91209 | -3.5333 | -52.17089 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddc12de1-3186-3440-86ad-73874d1beb3c | 0.86931 | -52.01628 | 2024-11-02 05:04:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84527fb2-2916-30e6-a421-d311e3a8648d | 0.72843 | -51.37368 | 2024-11-02 05:04:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eac4348b-3b62-3370-8dfe-3242ef5f06ec | 0.40684 | -51.4979 | 2024-11-02 05:04:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a051a8-ce5a-369e-875c-94dbb46c5d17 | -0.73964 | -51.70059 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfa853d7-b9d8-3df9-9a76-3c1cd5e133ae | -0.73956 | -51.70173 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cad6c330-ff29-3a40-bdbf-14a1c557784a | -0.73904 | -51.70458 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b8f906b-d31d-3c6a-9f03-a791030122a0 | -0.73893 | -51.70572 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1156997d-59a4-37fb-bfda-f5cf44868910 | -0.70374 | -51.67575 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66c2f02d-8c77-3a08-aa0c-210b7fb00375 | -0.7002 | -51.6752 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d51c7321-b9ec-3c32-9e07-7159ecbd7e8f | -0.68602 | -51.67299 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08ae5026-dc84-3585-928b-eafe55d30828 | -0.68541 | -51.67698 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 660c497c-ef5b-32c5-adb0-e6b1402aac2e | -0.68355 | -51.68895 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6639c9fe-5469-35bf-a086-3e3ed27536f9 | -0.68293 | -51.69293 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e3abf0d-f8d8-30db-ba98-2e9ff626eb0a | -0.68125 | -51.68042 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 439c13a4-341a-30b1-8905-41334a86ddce | -0.68063 | -51.68441 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 64836c55-a6de-38cc-9d36-be0cb916a6c8 | -0.68001 | -51.6884 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37e2dfd2-417d-30d1-bfbf-7298b2469851 | -0.6777 | -51.67988 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e24807d3-85fd-3e6b-b60e-e781d00f6f67 | -0.67709 | -51.68387 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c1fdaff-78af-3bf2-a914-8f17ff876f22 | -0.64902 | -52.3168 | 2024-11-02 05:04:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4c31c64-df33-39cf-80c4-3cfa6a9c12e6 | -0.46257 | -51.75794 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 753bc7ca-9db6-3c29-bee1-e7db3d5ae86c | -0.11985 | -51.63096 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b92e218e-c666-3277-b0d2-21d0af5d1bc3 | -0.11924 | -51.63492 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ea337ae-0273-3357-a3ce-07b7167ac714 | -0.09201 | -51.59941 | 2024-11-02 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeee6a85-a2ad-37bd-88ad-274451acf673 | -1.88781 | -52.13018 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e1b266c-b564-3d7f-bd65-b59f71516f5d | -1.88721 | -52.13411 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e185060-6bd3-3f07-b534-af770755fe67 | -1.8843 | -52.12963 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 425330d5-3397-31d1-8ea6-d63b9dab6a89 | -1.8837 | -52.13356 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afeb72e8-f4f1-3d6f-8085-c21e6cd83e5c | -1.84134 | -52.19156 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50578ca8-0738-31bd-a51e-52e7595a2723 | -1.78762 | -52.19131 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 421c5bef-069d-3e8c-afb9-38ff86ba9ee0 | -1.70061 | -52.1669 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0016fdb5-0fc9-33a9-8fa2-31c1f3841971 | -1.66334 | -52.12933 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6039073-f2f2-3c1d-b5ae-a312b7f315a6 | -1.59454 | -52.1954 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 883a40d4-8c15-353d-8f5f-4f9a0738c4fb | -1.59127 | -52.14713 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2614995-9ca9-391f-ab0c-fc18131bc913 | -1.59115 | -52.17106 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14c8da4a-7f90-3860-9a8f-6d8836069488 | -1.59067 | -52.15102 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1f9119ab-5b95-3a29-b486-c6491c56538b | -1.58946 | -52.15887 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3cf7c36-fbac-3194-a1f7-bbcf33b7dec0 | -1.58886 | -52.16275 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cc5970d-3009-301e-a7cb-894f8976e752 | -1.58837 | -52.1427 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06428756-3f15-3106-be1b-21b88c254aa0 | -1.58826 | -52.16664 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 177094b6-561b-30b5-a931-143281e70ff8 | -1.58777 | -52.1466 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b776ba1-8473-32e7-8a9a-e0477886997f | -1.58766 | -52.17052 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2505cb06-a0c9-34b4-a635-a867544c5bdf | -1.58607 | -52.13437 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90d778ab-c396-31c1-81d3-1d0af25cb42d | -1.58547 | -52.13826 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32cdc0ce-92bc-39a6-8e43-bddaefe131d3 | -1.58476 | -52.1661 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 29eafbaa-7d82-3cb5-9a9a-bbeca240a7e5 | -1.58246 | -52.15779 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b2de7695-5be1-32b4-a8c9-c946475e20b7 | -1.58186 | -52.16168 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 73794314-e047-307e-b15d-a352ddebf21d | -1.58137 | -52.14163 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfbe17a6-a35a-3923-9e8d-c76558c7ab59 | -1.58126 | -52.16556 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7541ed01-fe1b-3ab9-9e19-657eed126e4d | -1.58077 | -52.14552 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfb900f0-14dc-3f9e-bf95-68cf781769e0 | -1.57956 | -52.15337 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1af70930-1e7e-3100-b1e7-6d716393050d | -1.57896 | -52.15725 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3bbd904f-f3a1-321c-9b58-0f62f856938a | -1.57787 | -52.14109 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59654973-e422-396c-bc12-c0321852b47f | -1.57727 | -52.14498 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 77d770ba-0a48-325f-9404-a0fbfcd40d92 | -1.57606 | -52.15283 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a54f7cec-5e41-35d0-b2bb-d08b7b2f55e8 | -1.57556 | -52.13275 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1c2c00b2-b696-39b2-b72c-f26e06e2110c | -1.56252 | -52.19443 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3639940-3ad0-3c20-aefc-d18d70ff4e16 | -1.56192 | -52.1983 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed33875b-383c-330d-acb1-aef4672b1011 | -1.56133 | -52.20217 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 39d5b4d3-51c6-3eb3-85bf-c43705f9fe61 | -1.55902 | -52.19389 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4882810c-79b5-3bdb-b1ec-f6d80dc86fbc | -1.55843 | -52.19777 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7d1d891-ff57-3fb2-b838-2d87af95933b | -1.55784 | -52.20164 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8b97452e-9e8b-3595-bbd5-6e241cd39f1b | -1.55613 | -52.18948 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba5f9c6a-3191-3af9-aa05-462ee097c754 | -1.5374 | -52.16302 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdf06a5b-72b4-3222-8039-1fe25986f6b2 | -1.53521 | -52.16243 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba50a15c-a226-3765-b723-4e00dd875666 | -1.53224 | -52.15031 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b581726f-2695-31bc-9113-f142db6f74c3 | -1.52601 | -52.12141 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92261b27-a134-3db8-bf87-3f704dcd9333 | -1.52433 | -52.1092 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README72.md)
