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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6b78867-d8e1-3501-b010-aa904df7c4c9 | -3.65617 | -50.21498 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c14dcb90-d6fc-3a09-a132-ebc6a690fc84 | -4.25046 | -55.0088 | 2024-11-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bf73b5f-431d-35a0-9694-c0a04f061089 | -1.49601 | -51.14431 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e4d9a47-1fe6-3ecd-be35-1d288e1ddd0c | -2.24066 | -51.81855 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f15ad4ae-43bc-3dcd-947e-28a0c3f9f8cc | -3.18805 | -54.32045 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2a42e1b-8d4a-3cda-9f6b-8050f837a712 | -4.22433 | -46.45081 | 2024-11-13 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7c0367e-e032-3c0d-9e42-a91002b35ba6 | -4.41724 | -48.85177 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b274161-59ff-3589-9591-ff32575f10d8 | -1.33947 | -51.40598 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4efee42-8385-317e-99ed-017b5743dd12 | -2.7491 | -54.03898 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59b01637-c7eb-37b8-a70b-bc7dc5a785d8 | -1.40315 | -51.99807 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 329d7184-36a3-398a-a82e-00d186e1374d | -2.37321 | -55.75847 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecff1b6d-2fcf-3ca6-9e2a-fd3f5507c360 | -1.5638 | -54.26543 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb12b307-709b-318e-9f00-c46004699c3e | -2.28088 | -53.76855 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd515640-0bc4-368b-8035-0297f5939a50 | -3.15135 | -53.247 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| eb7aef3b-a676-3331-90d7-db2702a500d2 | -2.34205 | -50.57581 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd01d2f0-173f-3fff-98a4-498eee1ac171 | -2.15934 | -53.65428 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5268e6b1-834b-3aa7-927a-86cedefd55c8 | -1.79496 | -48.62635 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ec69690-9463-3eff-a192-9cdfe10e0a8e | -1.47019 | -51.12878 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d242a23-6259-3047-90d6-48838054355c | -1.39333 | -52.39206 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b4334c0-d0e4-3d26-a7df-b0e2f98f9c7d | -1.24649 | -51.75925 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7bbeca4-f712-3134-904d-3796cbe27b49 | -1.65323 | -52.53577 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32af96b7-1cde-30c8-a84a-1e49ed3c616a | -2.69301 | -51.79744 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e60a1269-66a5-3b47-b643-7a02a3170ba3 | -3.04273 | -50.33318 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a6530d5-faaa-3e6d-8666-e71e0215cdf9 | 3.5984 | -59.94907 | 2024-11-13 04:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf519804-18cf-3f2e-9d5d-7ec896656ab1 | -2.95895 | -54.08973 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28d89763-2975-3ab9-ab47-6d8af4eca4cb | -2.33445 | -48.53952 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4c8664b-c710-3cf2-bbc3-ad6b59a88f40 | -2.94289 | -48.31988 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6bc334b-f114-3b22-84d4-f51aa8c92c44 | -2.93206 | -51.00203 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3819b27-9348-336c-98c4-1bebb53d3e0a | -2.83701 | -53.34576 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 601d0a29-213d-3f05-a576-42fe0c77b3a5 | -3.53399 | -54.08835 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95706c9a-80ae-3ef5-83c2-f5f1ed4f7dfd | -3.28019 | -53.66512 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b21a6386-7a3f-34df-a748-7f9bf4f8d96c | -2.66174 | -51.68372 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29319d6-6b97-3914-9e68-d59ed053c1be | -4.58915 | -47.07026 | 2024-11-13 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa8b176d-7a23-39d4-b767-17508103c6aa | -3.53122 | -54.08439 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ee0617-5c33-3271-ace3-931ae2082cf0 | -2.17595 | -50.61746 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b65b431-e8f3-35cd-b50c-978ee8fe192d | -5.363 | -43.53164 | 2024-11-13 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26cc5379-4728-3a74-93d9-b7a96ad46fcc | -2.65951 | -51.72103 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0cfda5bb-8d78-3b94-8c94-1cc589951399 | -3.23619 | -50.66876 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5520e91d-3aec-329e-8774-301d108f0eb5 | -3.50422 | -54.69062 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c499d3f-1af3-31a6-b726-4bbde0923642 | -1.23075 | -51.74949 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83237b56-0e6b-38f6-a55c-02539cf0b453 | -4.02071 | -53.78106 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb9e06c8-dbd5-3f51-99d5-1f9772da857d | -1.46804 | -52.30408 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b9bc252-0e81-3c21-929e-ad6e268f4abc | -3.07626 | -50.33728 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ca10885e-5159-3d7e-8d2f-cee4e6e82039 | -3.93485 | -52.18615 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebacaa03-21a0-3d00-a194-83318c50c042 | -2.77291 | -54.73447 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2576942b-9516-33fa-8d27-f026cf585858 | -3.66259 | -54.65792 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0382ab33-4b9b-347b-a140-cfa8d8aa5876 | -2.98833 | -51.45486 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbbd9775-6527-3f8d-9866-bbcb293772ab | -3.10396 | -53.70742 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 531a6abe-56cd-343e-aea5-47326203567c | -3.1016 | -53.32742 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be35d8c7-75c5-387d-924c-9990a9e7834a | -1.66994 | -52.05741 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f62ac849-e781-31cd-8741-6b29d6d1a2f7 | -1.63164 | -52.52176 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 204719a0-47f0-3372-992b-8a0873187a9a | -4.26765 | -48.19468 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc2c952e-c112-30ae-9e03-365425fa43f4 | -1.61341 | -52.52963 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c551c03-6c5e-3793-b484-a81b9a8aeb25 | -3.01767 | -53.25453 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fc6c71d-51fd-352d-a2ee-049d591d677f | -4.67964 | -44.57486 | 2024-11-13 04:57:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5febe5d5-dd24-3d31-872a-c9c3e0ab48be | -3.81597 | -51.26574 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65751603-4e57-395a-ac82-458314651772 | -2.3679 | -48.51986 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 390d86c4-3cec-3675-ac7d-5c78d73880e0 | -2.84377 | -48.67378 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f808bdf8-36ad-3211-ae0f-e77c877ef975 | -1.38212 | -51.40453 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8af6c31c-05fc-3488-8a5e-afc205b814b7 | -3.06299 | -50.32655 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb4d060b-2a46-3a4c-8c2d-6e39c1f744f1 | -2.73208 | -45.29335 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 715a77e8-167b-36a8-96ce-ac8818ab1f75 | -4.37435 | -48.08487 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef439dec-62d5-36f1-835e-ee1b1509f47f | -2.71222 | -54.68854 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13728341-9ef3-37dd-9095-9e9eef4087a4 | -1.50918 | -55.87621 | 2024-11-13 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c425574f-5a68-33ec-bca9-5a7d72ababfe | 3.27779 | -60.03445 | 2024-11-13 04:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c812e629-cb2e-30df-9b88-2ef21202d27b | -2.20647 | -53.74237 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99eed388-8009-32c9-815b-8697d55cb177 | -3.25792 | -54.52674 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3927e0b-e2d0-3033-8c10-bff0597e1af4 | -0.98538 | -51.78158 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d1e881b-d9a5-363a-aecf-777c649c8337 | -3.83157 | -55.41845 | 2024-11-13 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5af6b00-8ada-33a9-bd5c-1a24bcdac382 | -4.08917 | -49.14542 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 20cf1797-f00f-34fd-982a-cf4ab71b16ae | -4.42129 | -48.85237 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f67f165-04e0-3a23-8118-f77ad02799c8 | -1.5684 | -52.25137 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 661fa47e-4c4f-3343-90f2-8a4813a50e5a | -3.0402 | -51.09821 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23d971de-9193-34a2-8973-4ea525421342 | -2.97096 | -53.272 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65c7e0c3-237d-31b6-9763-6fa78fbd120d | -2.90781 | -53.93723 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a83325b-3029-3330-9e12-6c4846b338c9 | -1.21286 | -51.77607 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4775c43-0a92-304f-b01f-4d9242ad9f7b | -2.89967 | -48.30651 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e11e09c-cb4e-3b20-b65b-9dde02358a74 | -2.16631 | -53.23728 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce21f658-ed49-3471-8514-4530a82b7b5a | -2.16685 | -53.23385 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 335f9802-36cb-3580-9683-768c7847607e | -3.19607 | -54.63869 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b63ba587-ae26-3a2b-bbe5-1e26ef30e90d | -2.46722 | -53.96992 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a42b919-fe20-3762-a03a-630bac83de5a | -3.05196 | -50.32164 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 503ddb4f-3a09-3ec8-9a4b-bcadcdacf0aa | -4.89234 | -48.06673 | 2024-11-13 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 385255ec-73ba-351c-88c6-dd33eaa8023f | -2.48301 | -54.06418 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f2ff586-e9f8-3773-90c7-830fc1f3bb2e | -2.12685 | -52.26549 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aec66342-9eee-310d-a00e-aa0e03598f7e | -1.30266 | -54.66842 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce112415-d96e-32a6-a785-ee3867efa90f | -3.05809 | -50.33446 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d418ed5-8f8c-3cc6-94e0-7d7ee95bf0ac | -4.01805 | -54.60323 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e42b5f63-57e6-3bc3-804c-d97101382ce2 | -2.38938 | -53.66235 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7018b3d-365f-352b-a04e-5bd55c4be3fd | -1.1333 | -51.94224 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2d2ffdd-5816-350c-a8ff-5b2ee0b2fdf6 | -1.39953 | -51.1109 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 930bb876-5647-363e-9982-148ce5a65b4f | -0.19909 | -51.49651 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bda287ce-3da3-3a2b-a18f-670a293fee3e | -1.27302 | -52.20199 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89547461-6c1e-37ee-8832-7c133deaf8a2 | -2.8754 | -49.43209 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ef06e46-e405-32c6-914f-c97820706cc0 | -2.73232 | -45.29614 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 743456ce-31a8-37b1-94ab-3dcf8b9488bc | -3.23322 | -50.66411 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40380f1d-2d32-34e3-a9ea-79c18969ee93 | -3.02735 | -50.97195 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 424b3de3-b883-3fe6-bcd2-c5b203ccfbea | -1.51755 | -51.54846 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27c73ffa-118f-36d2-bba5-bc72406ae045 | -3.14543 | -54.48443 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57e944f2-917c-3ab1-9169-e9288503177c | -0.89731 | -51.72782 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README34.md)
