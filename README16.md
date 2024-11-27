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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8dbf363-2480-383c-8be0-bcdad4455b5b | -1.59642 | -52.26154 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5253dfb-4378-3726-9718-f3a01881facd | -1.76009 | -53.63171 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3b82361-1fa2-303a-84cf-6acb5e7397fb | -1.55425 | -52.0249 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8f2244a6-32fc-33dc-8ef7-3258814510fd | -3.02962 | -54.02 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fd4425a4-f31b-3225-9708-32b044c662e2 | -4.00851 | -50.34584 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e3c7e92e-95be-3812-82c8-a6fbdfc88c88 | -1.62657 | -52.47817 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 114fe661-490a-3c86-a387-9996e278dc7b | -1.66641 | -52.42956 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f89b053f-a140-39ed-9370-6fd3d108c4c1 | -2.96611 | -53.89083 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01250251-b075-3870-82f4-1088b52fbda6 | -1.35925 | -54.65819 | 2024-11-27 01:09:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ead5248-bf32-3f33-ad52-8cd0d01443e4 | -3.75867 | -52.17527 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea72be4f-39e7-3cc3-a746-8995d0117edf | -3.97212 | -48.06269 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| eb753ae7-74cd-37ac-8c19-29882ca1e2da | -3.49624 | -50.46134 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eaf7d285-2d41-3791-820a-d2f1714f282f | -2.93285 | -48.02153 | 2024-11-27 01:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6768173f-319e-30ca-afec-ff12d7a1829e | -3.09592 | -54.03254 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| adfe5c31-4e76-323d-bf16-d5ea057a7244 | -2.9439 | -49.12292 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cae493c7-cd27-323f-bc44-e1f5faccb8ba | -2.57592 | -51.88757 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 813eabee-72ee-3bfd-ab6e-2100c1f56f92 | -3.06871 | -49.20163 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8ccdafa2-0cad-3993-8828-5f60a3a80fe5 | -2.57219 | -53.97675 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90186242-0c07-32f3-9a71-5569eab15798 | -3.2537 | -51.14143 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5c796a83-bff2-3300-bced-c527b0d719c4 | -1.29173 | -51.73118 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 9c477c10-baa8-30b5-a562-6b830f1bef80 | -1.49385 | -52.44786 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 900bc942-fac0-3419-8dbb-5f64e3ece170 | -2.59915 | -53.96664 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 701b7a8d-80a5-3d24-9b86-00a8594d5d1c | -3.90352 | -50.59667 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e8ba78fc-a329-3793-abeb-8a5ef4a57d0c | -3.04883 | -54.02656 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 278c1f23-b8c6-3084-a599-d440a38260ee | -1.70379 | -52.76106 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6363df98-03a7-39ca-add5-6e6125769b98 | -3.7205 | -50.19185 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e4bdf305-7b6e-3a2c-8418-a473a47edce9 | -1.73191 | -52.04391 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 76b82d3d-e61c-3913-92b7-06cef5d16b47 | -1.67661 | -52.43729 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b1df4be6-8adb-3673-9933-4e425b95b105 | -3.50578 | -50.45991 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5ee5a447-6985-3a5c-9fa2-f6015b0661ee | -3.39242 | -50.3116 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ac306b3b-2074-33bd-a94c-a3f34c7b173a | -3.41584 | -53.88029 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fe68ba80-2bee-3b3d-81cc-b504ab9fe466 | -1.63945 | -52.43971 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fe3876f8-5901-3b60-b268-72b053ca62db | -3.58459 | -50.60533 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f97d3616-0ed6-31d8-b7bf-ef593b6833ff | -1.10691 | -52.11858 | 2024-11-27 01:09:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3f4b87c7-efa5-3831-8900-1630b09c4241 | -2.80077 | -54.02729 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7428f372-0496-3a7c-bb94-6dc5f05b0f90 | -3.09941 | -53.72895 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7b70ec4e-6b22-3d44-9f70-2ff6e61b6232 | -3.15568 | -50.58742 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab8349d6-fc9d-3452-8875-192075922c07 | -1.64693 | -52.49359 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e2f8444f-e688-3ec8-af2f-fec4380b4f3a | -3.24285 | -54.2294 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 67e170be-58e2-3e67-9111-dc2e8401b3fb | -3.10402 | -48.01515 | 2024-11-27 01:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 67d396e5-856e-32d0-9ee0-90a761922064 | -1.24143 | -51.62747 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 817cfe90-05f1-33a5-a31c-60c79da58467 | -3.10698 | -53.25116 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 358.7 |
| 824ba761-ef9b-308d-8388-458ec2fc3b13 | -3.05009 | -54.03562 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0d4beca9-d0cd-3a06-9059-a7c3ab0a6bee | -3.07101 | -50.95068 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d45b4706-295e-3e41-91e6-1e05a324fa88 | -1.57107 | -52.0131 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 580ee2b2-d526-3901-b176-eb54390fb75d | -4.21336 | -50.89667 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 82fffbb8-3076-3c9c-ba51-f1b98dcd4503 | -2.97412 | -51.57385 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 368b2acb-2330-393e-9f06-0fb325e58d2e | -4.22123 | -50.88562 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ddaa5d69-d17e-3aad-8deb-1a7f3959f13f | -3.53373 | -52.15239 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| f3a962f4-8309-3a1c-adf7-28b995e2d047 | -2.9028 | -45.36951 | 2024-11-27 01:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 45df1d26-d719-3eed-af02-a1338bbb4de9 | -2.90647 | -45.39451 | 2024-11-27 01:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| a73eaa21-204b-3979-88e1-da731b901735 | -3.72283 | -50.18509 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 111f7147-dae2-308b-aac0-2a2ede902d08 | -3.67472 | -53.6876 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 51da3837-2129-348d-bbc3-de50ce42ce6e | -3.11706 | -53.25872 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| bb7e994d-ff97-34de-8fa1-9b9c71d14030 | -3.24293 | -50.13776 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d531da8a-3913-3ad1-b5f0-04fa2712aa8f | -1.94568 | -45.70656 | 2024-11-27 01:09:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 0e57c0a0-cef3-3d46-a59d-10b39518bf09 | -3.31477 | -53.2907 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d46cf014-bf28-3c5b-90b4-7e0533d45478 | -1.06593 | -53.01732 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d964516b-7003-35a3-9f96-6401b835a669 | -1.0647 | -53.00848 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 861bf618-79ec-3f16-9042-a4f277e0fff4 | -3.05113 | -48.52274 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 250b3f9e-d014-3b36-85b4-f5778bd74fb0 | -4.06468 | -54.38298 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 59240405-b0e8-37c7-8421-91d1d4a305e4 | -3.2831 | -50.56276 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a47d7233-71a0-3e38-bc6f-f119d727bea0 | -3.97421 | -48.0774 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ddada9b6-8e2e-3dc1-866e-01e58a463d32 | -0.69961 | -51.97298 | 2024-11-27 01:09:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e7d1cef2-85cc-3567-8b3d-5bf4bb14e156 | -1.73063 | -52.03472 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| de62103c-5327-3ffc-b3b5-5552cc6a15a9 | -1.69276 | -52.61753 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ae311db1-8872-3826-a4e9-a56478b64b2d | -3.73552 | -54.26253 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 95ef3168-7efc-361f-a9be-0916db1aa495 | -1.58541 | -53.83065 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 30b94b17-88a1-3da3-9adf-1ae64df49d87 | -2.40805 | -53.85048 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e8fe1f6c-e316-3a11-bbb6-56374316f00b | -3.05635 | -53.6805 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e685d1d6-8877-3aef-9105-1374169b0547 | -3.9144 | -50.6055 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f2d5dc12-f567-3bb1-a31a-7f1d55e8b8e6 | -2.24783 | -53.63144 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 2580e8e6-a61b-3b6c-9d52-1f29c2d90efc | -2.34723 | -47.64681 | 2024-11-27 01:09:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e6f6cb4c-5da7-3bd1-934b-9a4a9d94f8f2 | -2.89296 | -53.96247 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d823089b-edb8-3125-9dba-169c69edb974 | -2.57455 | -54.05925 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fadd06e4-c3c4-39ad-998a-67ea9180bfb5 | -3.67101 | -53.66068 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c2e6ca98-c294-37f5-b986-ffe56fce51fb | -1.17955 | -51.97961 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5510dcf3-9b77-367b-95dd-4ed7787efc3b | -3.7721 | -52.40028 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 3773c4c2-44b1-3333-bfe5-2b825988b3e9 | -3.09049 | -53.26248 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 82da3f44-f6da-3ff4-9d07-9012eb2886de | -3.10529 | -54.97659 | 2024-11-27 01:09:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2c977f71-f7ea-3d63-9022-fadfef236a00 | -1.36956 | -52.55095 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20681503-3bd3-361b-a13b-72e3451ea1ca | -2.59596 | -54.21338 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 5c14aee8-5ef8-3a82-866e-e1abe9f868ff | -1.66893 | -52.44753 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 07732d15-6d18-3386-b4de-e29f71757c06 | -2.58351 | -54.058 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 02566a0c-9213-340a-92dc-f850b81489da | -2.60809 | -53.96539 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e51e8a39-fac4-3a2a-b14e-3e074d98285d | -3.43758 | -50.12461 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aacdcd5a-f532-3c1d-8490-36278007cf35 | -1.76631 | -52.28998 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2da2c4c9-9d97-3272-b6df-d203ab05e5de | -3.73876 | -51.83829 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a76e3e90-b87f-369d-ba35-d969a20353eb | -3.68637 | -50.22939 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2fa38de2-d780-344e-a0a9-c72ddc71946d | -2.24537 | -53.61374 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2716099-cbc6-38c6-9a23-719abc0ac75b | -3.11207 | -53.75454 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 08ec5174-5d5c-3ddd-9619-65e5f20bf5ec | -2.28297 | -47.91301 | 2024-11-27 01:09:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| da72f3c5-4c9e-354c-94cc-e7a4e905a8fc | -1.65989 | -52.51284 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd08661b-61e5-30ed-9b66-e08576a9e6c9 | -1.63925 | -52.50382 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9e591dca-be17-3a7c-bdc0-609052025d01 | -2.77272 | -54.02839 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d9dd7f43-b8ee-38cf-90fe-f5dd7e4e77f2 | -2.11096 | -52.77847 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| df74043f-8834-3110-bed2-30fb18875533 | -2.82072 | -48.60287 | 2024-11-27 01:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dfb1484e-07c2-3040-ad78-daa5f0a75faa | -2.82442 | -46.80657 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0b70da3c-bdb8-3006-8ca6-62116aa66170 | -1.67673 | -46.92985 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| bcfe723f-ce47-37f4-9105-dcba4c4c0eb2 | -2.99304 | -53.35452 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README17.md)
