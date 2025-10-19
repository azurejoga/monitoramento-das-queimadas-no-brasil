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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 404fe95a-8e8c-3d3b-919d-1096de875a81 | -4.21888 | -48.3629 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4445c971-42f3-3c60-ab61-25f01f3c4557 | -4.53049 | -48.41221 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aac2bdb-5706-3e9d-9ec5-32279f654b2b | -2.97389 | -49.51805 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7675db65-8fed-3c44-a042-0d5538b98ae3 | -3.5924 | -43.04595 | 2025-10-19 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3e994af-7ad3-329c-9028-2c2d99b0b1ca | -4.24312 | -44.68745 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18bd577b-55a0-3c22-984b-d8829406ed0b | -4.83885 | -42.74234 | 2025-10-19 04:29:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 03291889-a28d-38bf-af24-b4d20953257c | -3.46622 | -47.69144 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d4e5436-9093-3e26-b688-9480dead6d34 | -2.87041 | -50.73786 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 182bd9ed-a577-3f84-8e86-3d610f0d956f | -4.20382 | -48.35702 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a8fcdb-c1a8-35b5-8f04-9ede5c6b0e72 | -4.30105 | -48.06244 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a55e5aa-b882-39a0-a05d-9ec3c9a46988 | -2.74079 | -49.3872 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8ab31e4-f6fc-37ed-84d2-35dbeeb16e48 | -2.68722 | -49.54386 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cfb9c09-6611-31ca-92e0-5d60392fdb55 | -2.90748 | -52.73449 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56b69344-ff5d-3cc9-91c9-4e9e3474a7a1 | -4.78684 | -45.30099 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 762a534f-973b-38aa-925f-14246be206e0 | -2.56817 | -49.11512 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c2b9c35-ab39-3d7f-a8e4-a5a137cfe1c2 | -2.88165 | -50.73968 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63de4882-a06d-3e23-9054-cd7c636f6596 | 1.74463 | -55.95194 | 2025-10-19 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e78719b-6c5c-33fa-86e1-6fbcd99e97a2 | -4.9975 | -44.46032 | 2025-10-19 04:29:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 312ef8c2-aeee-3ea4-b997-cb3496d7b66f | -4.24246 | -44.6838 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4d0421b-1c29-3f7d-a0b5-8d3f1f7994f8 | -2.91239 | -52.73114 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e259a146-2d96-357c-a0b8-2c62e1009a3a | -4.85713 | -44.59581 | 2025-10-19 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 465ff0e9-54c0-3075-8510-640357503a16 | -2.87863 | -50.73458 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bbc785e-1fb2-3751-8dbf-482c1c96072e | -4.85298 | -44.59926 | 2025-10-19 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d66f9b8-9e1d-332f-8282-7ffe054e6f5c | 0.72057 | -51.48212 | 2025-10-19 04:29:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e433a5ff-88a3-30a8-9651-f85de646db09 | -4.46186 | -44.97868 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b959e06d-bade-3380-9ff6-d5341eeff62a | -3.46899 | -47.69542 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1153dc21-2516-3f28-b70a-11aec563475a | -4.14084 | -46.38695 | 2025-10-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9050bb33-ea34-31dd-9f78-54faba1c046d | -2.256 | -51.91876 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 122066f1-8177-3768-a72e-12ba4eff7308 | -3.48874 | -51.47745 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 213805b7-d901-3973-93b0-c6727271a6ce | -2.80594 | -48.66225 | 2025-10-19 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec1825bd-f90e-3316-a5ea-b5fe8e6eac25 | -2.79356 | -49.64943 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fc03ed0-ba86-3856-8377-5067dbeb59bd | -5.03946 | -44.3544 | 2025-10-19 04:29:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0f6a333-4d3b-3744-a10b-0be5313690f5 | -1.66241 | -46.76475 | 2025-10-19 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61f6b441-11e0-3cdd-8d2e-cfd825e2e676 | -4.00725 | -46.24178 | 2025-10-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8e837bf-9cb8-3ac6-8088-54869477da89 | -3.78898 | -47.47687 | 2025-10-19 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5822d0f7-580b-346f-a892-cfc6d4a06f30 | -3.03635 | -47.80937 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dffaad34-b2e1-3ab6-9374-b1eefde2fb2d | -4.30715 | -48.06697 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f0f1e04-93d8-3dbb-9fe9-f73cf04a2d98 | -4.33717 | -48.67014 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5deaf10-bab7-34a4-ade3-b4c47ac4deb5 | -3.81555 | -49.91693 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c24fb27-931f-3e91-826e-4ca1c9f79f88 | -2.80999 | -54.38586 | 2025-10-19 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f78854f-812d-3e27-b7ca-0fd16a38b757 | -2.6924 | -49.55691 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6069fe86-838c-355e-8485-3db37fe1283e | -4.58314 | -45.64282 | 2025-10-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7428717b-f324-30d0-8beb-233d476eb395 | -2.87936 | -50.73008 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4afac0c0-0df4-3f45-a5f2-2657755d8a76 | -4.25423 | -48.55087 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6b20267-9eba-3b46-8353-36be6270be82 | -3.54882 | -46.43693 | 2025-10-19 04:29:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04ab552e-36c1-3096-8c4b-f2f2a242e1ee | -3.04159 | -51.2132 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fab904d3-87cb-3a39-b420-c208125ca0d4 | -3.08948 | -49.21907 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| aebb9d81-eeda-39e4-bce8-f6a7a9e57408 | -2.70549 | -49.54274 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76e0c25e-aa55-3e5d-894a-d0ee4690a983 | -4.24307 | -44.6799 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c00095a-1600-37e7-9f96-a8f362f1ddca | -4.58923 | -46.29977 | 2025-10-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74138a66-a199-32bf-9cfd-3a8f66ca2e64 | -4.15769 | -51.09684 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e5fecb0-4f18-3ae5-814c-8a261c54cf1d | -3.86346 | -49.82174 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71c21470-3712-3ad5-8cd9-b92873476b14 | -3.46678 | -47.68797 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75af1355-0bcd-3fdf-bf13-eba0037da947 | -4.26922 | -44.46708 | 2025-10-19 04:29:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6265ded3-83f8-34d1-aca5-52bc2e4b760b | -3.79205 | -51.76388 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa799df1-1b0f-3024-aea5-675f70d35505 | -4.28915 | -45.48191 | 2025-10-19 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e35c5fc5-a499-310a-a0ee-705feb20dd4f | -3.11764 | -49.10213 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 121fe4a0-2146-3424-b6c1-ef96b2ecbefc | -1.79534 | -48.07136 | 2025-10-19 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fe1bdb2-379a-3a5f-a7eb-d43c51c07d9a | -3.29574 | -50.01322 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5313309d-96b2-33cc-8dfe-4765fbecca6c | -2.77512 | -48.02001 | 2025-10-19 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1d92621-b2a4-3b30-a864-450c818c9c5b | -2.86364 | -50.73218 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7207cd2c-8366-3759-ad1f-09555b3c9865 | -3.13104 | -50.21522 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 797538ce-ec10-365c-9820-b4a56a335a79 | -2.86886 | -50.72377 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6e0dd011-c2c8-39c5-ad67-0dd47565a265 | -4.41218 | -43.96216 | 2025-10-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e48d82ac-7d96-31e4-a08b-246019591d9d | -5.33987 | -42.54948 | 2025-10-19 04:29:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ac2756e7-cae1-39c5-a42b-ac3a1a8cf5ab | -4.23896 | -44.68325 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0af7270a-3147-3824-a252-4ef60f440ae7 | -4.40075 | -44.08456 | 2025-10-19 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e082f00-5790-3938-9486-3cdca2ab07a0 | -4.11093 | -38.17425 | 2025-10-19 04:29:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8dbcd5f4-07d7-3bfa-96f0-a5ae3dccae46 | -4.27549 | -48.56898 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61cab58a-3fb3-38bb-8758-06ae5478db81 | -2.73317 | -49.38998 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 924d2cb9-4879-3cde-a0be-f0cfc8bf3005 | -4.22001 | -48.35585 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd54280e-a970-3606-a1d8-b5fd427352a6 | -3.79972 | -51.94044 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f04dacb0-a9f8-3ea2-b57d-477b39fddc85 | -4.26923 | -48.87825 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7515fce-ed40-3460-b15e-908cc929cfcd | -5.04304 | -44.35495 | 2025-10-19 04:29:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3109d2e8-aa98-342e-8889-651b81848f5b | -4.7269 | -46.15868 | 2025-10-19 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71445a40-6a5e-3fe9-82f4-86304a3ddce3 | -2.15372 | -51.95781 | 2025-10-19 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77653ae7-6ca1-3c17-9c4c-8d9aa004317f | -1.21716 | -49.01809 | 2025-10-19 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7ccc509-66b3-33e8-be3f-057e0a5cec69 | -3.09036 | -49.40342 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e38035c3-0f7a-39ec-84ea-7e5d3d3016bd | -4.26095 | -48.55197 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 040c5cc5-ed7d-3ca5-83c8-c21c60d828e8 | -5.21911 | -43.74679 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27e9e269-4a42-340e-95d7-d4cd2c8b2bef | -4.59225 | -45.38152 | 2025-10-19 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e28b8d47-b4d0-341d-95ae-b01a37c92159 | -4.07001 | -47.313 | 2025-10-19 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3f8cb848-9627-300c-a250-ef083f920f02 | -2.68306 | -49.54727 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 20db15de-3fa6-3f6b-9ddb-c6785cefed08 | -4.42158 | -47.75361 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 574803d0-77cd-3aa1-8348-60f06e8a990f | -3.43821 | -52.82835 | 2025-10-19 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c962a724-f40c-32f3-ac09-8da25c724250 | -3.44169 | -52.11527 | 2025-10-19 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e578eec1-c9a8-3eec-9099-a147154308f0 | -3.34609 | -49.25399 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeafdc73-c69a-3a23-9ed2-8675206cb0af | -3.56678 | -53.25702 | 2025-10-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 209c7b9b-0e35-33d0-8332-7a033303e3e3 | -5.37273 | -42.81694 | 2025-10-19 04:29:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f3a7dbec-0901-35a2-93bf-2b746dc68dd1 | -4.46244 | -44.97489 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43a2889f-e911-3099-8755-480124322d35 | -2.7446 | -49.39089 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4afe50f2-ff97-359a-9e9e-088e18855b97 | -4.15178 | -47.67549 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 985440e8-bf34-3631-bd27-8b416b88d943 | -2.73667 | -49.39054 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 638b82c0-d1e1-3c42-83dc-4110766e30a5 | -2.91174 | -52.73518 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e03949ed-d4b3-3953-a0c9-2c503a88dc76 | -2.86666 | -50.73726 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a59254a4-0ff6-3914-a7b1-343ad5f4bf45 | -3.8639 | -49.81844 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad35ea6-3feb-3336-9b99-cac5132fa342 | -3.75622 | -44.99029 | 2025-10-19 04:29:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a55f2001-9f1f-3f53-8496-2ee3fd552edc | -4.77583 | -45.88944 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e857bba-2af6-33ac-b74c-b78a34987473 | -4.21445 | -48.34771 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b234716f-cb97-3341-8139-7e3b0e4d1ffc | -2.88632 | -42.95423 | 2025-10-19 04:29:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
