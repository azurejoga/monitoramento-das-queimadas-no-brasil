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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26e1cdb0-7365-357c-8cfe-57de0ca3e566 | -2.97452 | -54.04397 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46f79682-3d81-3375-9eb5-6cfdf176c42b | -3.11029 | -54.16115 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d31044cd-9712-360a-99df-c8899a82cf78 | -0.79076 | -52.49832 | 2026-10-09 05:23:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2fe2963-8708-3fbf-bcd4-750c4d54c12f | -3.68475 | -60.63751 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c136ec2b-cb04-31ff-8f4d-efe772566f43 | -3.25564 | -54.01931 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa3b9de5-6e10-376a-813e-7047fba620d8 | -3.3099 | -54.02758 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91bd421d-a498-36c0-9150-7baea6fcc4f7 | -3.74469 | -59.47253 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf91325d-7bf8-3b6d-81ae-bb6d603f4c1f | -1.90476 | -58.26331 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3c03474-cf20-3139-8f2e-a0c778ca1ab8 | -2.52483 | -58.10387 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e97f6ab-7988-3207-9407-99c1467953cb | -3.25201 | -54.04326 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 16cdf267-f657-30bf-878b-056db7dba002 | -3.08307 | -58.09659 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6b14ee4-dbf3-3b4b-ace5-fe85d60d1cae | -3.74026 | -59.45747 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9b3de45-96cf-36a3-b2b7-3610d77375bb | -3.45726 | -59.56733 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 708a03cc-874c-3db3-9e80-e405ed172ee3 | -3.87853 | -59.57313 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2eafd4c-025a-3963-90d2-093b38bf983b | -3.1893 | -58.64922 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 266788aa-c1d0-37e0-8142-394332e47356 | -3.26608 | -50.39124 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09ff9cb4-baed-345e-b626-02999faf6ce5 | -7.90396 | -54.71807 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b8c6c8e-eaee-3986-a5e2-55525e7121a7 | -4.37828 | -55.16503 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 069fb97d-674a-329e-81de-a9c422238e1c | -3.97002 | -51.86971 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f742b8d-ad0c-3132-9a91-088e122fa8cd | -3.25269 | -50.41222 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 468c5633-1b25-3f5f-b1c9-fde83917329f | -2.54435 | -56.28365 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f928ea1-8ab5-31de-b001-e2bec492e320 | -3.15292 | -57.67556 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f482f75f-218d-357b-8517-a1a98e50b414 | -3.56623 | -54.66986 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64ac21ee-efe9-3409-9d38-de90f95fbde2 | -2.89685 | -57.20966 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78366584-039f-3ec5-8c95-da9dba785295 | -3.08289 | -54.2943 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcf4a8cb-e473-3a7d-94c4-04ae9a9b2968 | -2.73106 | -57.46359 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7bc81c95-b548-3dbc-af0b-a3479bc1a112 | -2.50587 | -56.14782 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbcfd67e-b333-3b77-8750-18ee056ebcdf | -3.00769 | -54.05888 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c3ae2b6-58fa-365c-87dd-757bd4c44505 | -3.80485 | -49.94267 | 2026-10-09 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba98a646-f279-37f1-9ceb-f093eab7afa9 | -3.00256 | -54.1165 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dad7499-4bdc-3931-a4e6-1f0372ce0f2c | -8.75004 | -62.62522 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4aab58fc-786e-3c19-89e7-e4c4d6793a7d | -2.66275 | -59.41703 | 2026-10-09 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e9f229-1532-3072-a534-4fe02d244f10 | -3.00746 | -54.12436 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e079725a-6f8a-339e-b2b0-40d4d3bb63cf | -2.46393 | -56.061 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b37fc4c-a4f9-3ae3-95a7-4924349247b8 | -2.93582 | -53.92688 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da71af4d-61d1-3ea6-a9fe-e7e14fda7d61 | -2.62998 | -57.73922 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ea4a137-81f7-3598-838a-dd13d5c9c653 | -2.50646 | -56.14405 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd5f0506-1890-3c68-85a6-053aa11d87b0 | -3.30051 | -54.01127 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95746994-93df-3277-889d-7244cf3c91de | -2.77747 | -56.51859 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd4f3d92-bfd8-3071-b775-4d060b65cc47 | -2.99215 | -53.85279 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3728550-aced-3d13-af3f-671d4b9b4241 | -2.98502 | -54.77137 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76331419-9afa-3f33-a957-f662390789e9 | -3.18147 | -50.58139 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fc72a500-9f86-3ac0-96c3-dc648d56e257 | -3.89505 | -58.95559 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc6fd84a-8d61-3df8-a61c-1bb8b63a606e | -4.55729 | -54.21238 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 827263a6-f39b-324c-ba2d-b9be5549e940 | -2.77933 | -54.08219 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55c68096-e442-3561-9b84-a03c5fd70492 | -4.28221 | -55.13428 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8624c6d9-1169-3c72-af15-fab0fcd4ff4a | -3.58902 | -61.61282 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa1a9ec6-4bcc-3a30-b42f-9b2f84faa7c5 | -7.57437 | -61.54868 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c397434b-9094-3bdb-a253-51def0916f7e | -3.59016 | -54.56886 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d6ae1e6-48e0-3368-af4b-5bd7849df3dc | -3.95278 | -55.332 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 21008dca-286f-31bc-a7e3-ff8879bf48fd | -1.52703 | -54.52624 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4999c04a-3db7-3258-90a2-680d8753317c | -3.07967 | -54.26524 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c89e77f2-2a67-38f3-b06f-ff0d9e5b8352 | -2.97108 | -57.90305 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca07278b-6147-30f0-b330-1288c7c43c74 | -2.54602 | -56.29528 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4be043dc-d4b4-35af-8a7a-4ba92a1098ef | -3.72328 | -59.69282 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c471124e-78eb-3cc9-b974-0c9ac5ffb97f | -2.51282 | -56.32792 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c633d83-cc6b-3cc0-8b59-388bccbf7304 | -6.68157 | -63.02634 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 664720ac-ff5a-3919-9188-3760bd9e70a8 | -3.06099 | -54.20981 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bc0a0a5-5b88-35b5-bc6e-8b235074822e | -3.05275 | -54.03358 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5f3ca61-0e23-362f-b2a8-31138cd71d34 | -1.18783 | -55.66127 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e3633d5-9b25-3721-85c9-67261bb9e318 | -3.08143 | -54.30079 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a142fb8b-035b-3ab8-aceb-0e442e68cf30 | -5.09832 | -46.21637 | 2026-10-09 05:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1baccdc7-e8bc-39d6-8749-8e38ce9d34bd | -2.47071 | -56.0852 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f4c8551-8225-3894-befb-2907c04c6cc8 | -3.56714 | -54.68848 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 068a32a6-f00d-3f22-ba35-bb77eaaa05c5 | -2.99838 | -54.04277 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39a37709-829c-33f1-99f1-084dacc9289d | -2.58948 | -59.98553 | 2026-10-09 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0179e47c-c964-3f42-bf92-36892d901177 | -3.09246 | -53.95562 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 686863b2-a603-3915-8b25-fbdbb7dddc77 | -8.17575 | -54.71683 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f2a284e-d6e0-3190-9a77-2dcdd17e4a26 | -4.1045 | -54.0258 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5931e0af-4e92-3cd1-ab62-06ee51337b28 | -2.57117 | -56.18094 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6da4158-0560-3a06-bc57-85a8e9aa1bbe | -9.09832 | -59.39343 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ff5a545-08e8-370a-8c9a-d3063375b6a4 | -3.54681 | -54.67159 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c63c46df-5b5a-34ff-a65c-715f1d556036 | -3.54097 | -54.68447 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aab9127-d069-3fe1-9955-f67cb4f7e05a | -3.56647 | -59.09784 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad4b32a6-b53f-3acb-be99-7bb8e19f7500 | -8.69534 | -62.40972 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1c31cc37-e4b8-328f-852a-54d018bd5d23 | -3.71758 | -59.36432 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0861da15-a0e6-3692-9d03-0e5ae1bc2ad3 | -3.08733 | -54.28749 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f319f65-cdd8-3d1e-8cb1-eeeb4da5e200 | -3.54494 | -54.63435 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9b9655b-665f-3200-90d2-6986bf84a700 | -11.40546 | -46.67899 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 90a03d2f-dc52-3ada-b102-db2b2e00954d | -3.11192 | -53.77746 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf773424-319b-31a5-b52f-f60a79bc498a | -3.70994 | -57.09512 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d441661-fbd8-3613-b24d-94ca8cd6e5a5 | -2.3918 | -51.30186 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41d512c6-2f99-3485-b17d-01290f19021d | -8.09675 | -61.82317 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bfa6bf0-c24a-3bf0-b187-cb7ab8575783 | -3.12141 | -53.79409 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17514a0d-aee8-308c-9991-3ee18ba66e19 | -2.33982 | -48.87338 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37b9d2ae-ef94-3ec3-8337-f711cc44409b | -3.59262 | -61.6134 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90f655db-891b-30ea-a2c7-c411ba258918 | -3.71387 | -59.64425 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 659e3197-ad90-3365-aafa-c71eab20aae9 | -4.93784 | -49.21627 | 2026-10-09 05:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5faa0af-9af1-3c58-9a26-3c78d3ca60e4 | -11.26484 | -46.27236 | 2026-10-09 05:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4a4a1bd1-2a7b-3113-91c8-6daad9f71dc2 | -3.55037 | -59.47752 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d307056b-4522-3adb-8994-2bee9f251534 | -9.49801 | -57.25392 | 2026-10-09 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1b33dac-7835-384f-82dc-6cf4f63921ca | 0.79172 | -59.19781 | 2026-10-09 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2852e13-e7a1-35e0-a00e-d9606217d0ca | -3.11281 | -53.79777 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 686adb67-acca-3abc-84fa-ea3cf513ae60 | -2.92994 | -54.05185 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdf6499b-4047-3835-aae1-e3e167d216b0 | -2.57687 | -56.18944 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa797bda-b84a-384a-ad2f-b60bdad0faf8 | -3.63246 | -60.63301 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de2f10a1-362a-3476-ad10-363011131c3a | -3.08201 | -54.27514 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35079d6d-5596-3493-b586-1a9743672915 | -3.97357 | -59.35805 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75407f66-cd02-32e7-979c-fc1c724ecb77 | -1.2079 | -55.6916 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a074a6e-5a72-38b1-8665-9d512e60c7d4 | -3.49876 | -59.26873 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README185.md)
