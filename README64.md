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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d22c6fa4-99bc-3c69-8c78-06ab583932f0 | -2.9115 | -53.0809 | 2024-11-20 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9711e76d-6cc5-3838-abc7-79912335bf0c | -2.75 | -51.8377 | 2024-11-20 05:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 400cecc9-12e5-35ea-adcc-cc92d619f89e | -11.092 | -54.6221 | 2024-11-20 05:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8323baff-10da-37f1-8787-d14c76f68485 | -11.0917 | -54.6425 | 2024-11-20 05:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c391db55-a8dc-30fe-96f8-b5bbf5dc8220 | -11.1109 | -54.6204 | 2024-11-20 05:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f116088d-d51e-3969-928f-e7aa5bb88211 | -2.93 | -53.0601 | 2024-11-20 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 33cfb997-a70f-301e-b334-3d05569e993c | -11.1106 | -54.6408 | 2024-11-20 05:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5c3ab8fb-7b91-3dc6-91e2-c2041141e80a | -2.9116 | -53.0606 | 2024-11-20 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a04e77f6-313e-384c-8081-02cacd70ab45 | -4.459 | -46.5966 | 2024-11-20 05:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5c0dab7d-bd5a-3423-876d-bf5f011f76b4 | -4.4405 | -46.5754 | 2024-11-20 05:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 50acf757-ca40-30a3-85e8-40348a3c0231 | -2.9116 | -53.0606 | 2024-11-20 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e2203478-e607-3fb0-80bd-82fd837be965 | -2.93 | -53.0601 | 2024-11-20 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c48fb792-c435-37bc-a09b-ffc0e258d9f9 | -2.7317 | -51.8176 | 2024-11-20 05:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 169c5b21-ee33-377f-bba3-e9d1e4e808b9 | -4.4592 | -46.5745 | 2024-11-20 05:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c632a865-a385-3fc3-b138-1165b6ecdc84 | -2.7217 | -49.3508 | 2024-11-20 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 29ec07dc-6816-322b-ab3a-7281dab19129 | -2.7316 | -51.8382 | 2024-11-20 05:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 504f32fe-26c5-344d-bc22-b7bdc1fa9d9f | -11.1109 | -54.6204 | 2024-11-20 05:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| cf20414b-37ea-3500-b33f-c4dfbe3f26fe | -2.7501 | -51.8171 | 2024-11-20 05:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fb95ec69-9d36-307c-bdb5-6dbff19fd3e6 | -2.9299 | -53.0805 | 2024-11-20 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a9fea1dd-9c0d-3bf5-8bad-11a67ebcd39a | -11.092 | -54.6221 | 2024-11-20 05:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 95e613c4-d7ca-3d8a-896d-136db622988f | -1.8613 | -54.2714 | 2024-11-20 05:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 16f775e0-ff26-3e4c-a099-95c40473cc23 | -2.9115 | -53.0809 | 2024-11-20 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| fb2daed6-3a98-3e19-98aa-10a5373fc937 | -1.2017 | -53.6769 | 2024-11-20 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b3e1960c-e9c9-3d03-946b-e03333ae72d0 | -2.75 | -51.8377 | 2024-11-20 05:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f3506a3b-062f-36da-b655-ff3e1b4d34b1 | -11.1106 | -54.6408 | 2024-11-20 05:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1d5692b2-8b59-3da5-a4ed-f6c45e74c08b | 1.53847 | -55.91991 | 2024-11-20 05:12:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 655d9644-d577-3ccf-898e-b90c3df35aca | 0.64346 | -50.73436 | 2024-11-20 05:12:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02c92c2b-bd8f-3e0f-b0a7-bd95ea5dc633 | 0.75425 | -52.07172 | 2024-11-20 05:12:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2f3d472-45b6-398e-92ef-e4a706a7e154 | 0.61606 | -51.77219 | 2024-11-20 05:12:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eedb614-8262-3e2c-b7b9-efc79c0fbe52 | 0.61667 | -51.77607 | 2024-11-20 05:12:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79bacc3c-f7b8-324e-aea9-702d7f7ec0f2 | 0.64191 | -50.57694 | 2024-11-20 05:12:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 439a5246-dc57-383f-b853-43de76c14a97 | 0.64416 | -50.73883 | 2024-11-20 05:12:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9b01a4-82dc-3fac-b13c-c78b621154b3 | 1.53456 | -55.89516 | 2024-11-20 05:12:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b192c5a2-052b-35db-9fc1-4e2099b3cbfe | 0.63737 | -50.57766 | 2024-11-20 05:12:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cecec8b-9edd-3ac2-8f5e-049aab38ae50 | 2.56208 | -61.34777 | 2024-11-20 05:12:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdfbf385-1444-3760-adf0-03ce8578b40b | 4.42111 | -59.85615 | 2024-11-20 05:12:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93378e55-72a8-359b-a853-020a4180c7ab | 4.41689 | -59.85291 | 2024-11-20 05:12:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31cb0d6a-71f0-34f5-8e21-c19adc89c754 | -3.33834 | -53.31169 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd7cdcfe-26d0-3997-81e2-af40c7681836 | -2.72484 | -49.35024 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e6b7b8c-878e-3059-8a05-dc5a568f774c | -1.59868 | -47.14085 | 2024-11-20 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee127c69-0b07-3da3-b0f3-59037b835990 | -4.06296 | -54.05207 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee855e9-c659-3df2-a5c0-b3a179793ce9 | -1.6258 | -52.5911 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6173b345-7884-3822-ac5a-fbfc2c6a24dc | -3.73143 | -47.37753 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf518e56-fa0a-3e51-8178-25f98cb8045f | -3.56078 | -45.02222 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 47ebaa57-11d0-3cd9-b6eb-21d27f913455 | -3.10078 | -53.09966 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee073110-f62b-3eaf-a84c-6d6c48682073 | -1.11111 | -52.39025 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5cf74d0-9ccc-3332-afa0-e75dc1c47e11 | -4.38961 | -47.77812 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 264e5533-69b3-3abd-8873-0b1c054d5859 | -1.21696 | -51.74748 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8040a5a-799c-3875-9808-f7cd3976b615 | -2.60513 | -57.05001 | 2024-11-20 05:14:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2915a73-4ec7-3933-a5c9-2968efb99025 | -0.29725 | -51.54639 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34782bef-79ba-3412-a074-b9ee2936be40 | -3.1193 | -49.15862 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2458c33f-9c29-36d0-a2ff-64e5a18560ef | -1.19852 | -51.76676 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c46b22bf-0854-3360-89c1-2ee1c2459b55 | -3.50821 | -53.79849 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39dc05b7-856a-3775-a2c6-a1306e9aa659 | -2.45681 | -53.69603 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 176299b2-f775-31d8-8ac8-21464521956e | -0.8333 | -52.8753 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41e7a176-94cb-3027-9fb4-279bcca9238c | -1.13972 | -51.69087 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d831e1a-2dd0-32c6-aae3-5a2c52f84812 | -1.63078 | -52.4028 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39ca46c6-cfc6-343a-9bf9-6ca104a98643 | -3.53536 | -54.08722 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2b89d1b-f89d-3678-bd25-9b7248e8f88d | -2.95433 | -53.7169 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b425e7a7-da50-3883-910c-3e8768d3b395 | -2.65765 | -48.48774 | 2024-11-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 368c136f-bea1-337e-b7ae-99cf2e38f262 | -2.90401 | -53.05223 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50924836-460a-33fe-95b0-9efe6cd475d4 | -2.19752 | -53.67932 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4f6d8fc-eaa2-380e-bb5e-87e6e1e144b6 | -4.38794 | -47.7646 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4618b8d9-3204-319b-99f2-af60956b7073 | -2.53246 | -54.01327 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a076578-a80a-3a6d-949f-111c661be7a5 | -1.1348 | -53.66372 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae07581-d608-35f9-b9dd-af6bddd2e116 | -1.83068 | -55.04598 | 2024-11-20 05:14:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c058c827-6ce3-336c-9c16-5cc8ee976c60 | -0.88028 | -51.72567 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 687da4dc-7c68-374d-8dc9-78061b8e5954 | -1.64317 | -52.64207 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52b9b3ea-199c-3ece-b2dd-eab5110400ea | -6.63746 | -47.35162 | 2024-11-20 05:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dac01481-c942-3e0b-bf1b-dc931972c1c0 | -3.51285 | -53.79413 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 28d4847e-7bf6-39c6-b924-264a5e686a19 | -2.27722 | -53.63457 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad59ff01-acde-3b97-9c29-11ffaeb22628 | -2.95358 | -53.72175 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dfb27ed-624d-3caa-bc09-eedeac14d2bd | -4.55355 | -48.00858 | 2024-11-20 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45916f04-bcc9-3e2a-a798-9e1a014b943c | -1.30992 | -52.40545 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9eec240d-aed4-3a33-a9e5-8510e3a0ff83 | -0.77675 | -51.75212 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f6fd5cc-607b-3a85-990b-5a806e67fa83 | -3.36441 | -53.06222 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3a96381-9dd4-3436-82d4-739689bb086b | -1.54746 | -52.27187 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37a539df-091d-35e9-86dc-e2a4ddc00ad3 | -2.53879 | -54.55492 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8a7a354-4c67-3b6a-b9d5-88ccf30b67a2 | -0.95434 | -51.71977 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ab651a6-3b3c-3785-82f4-016cec3c4070 | -1.9677 | -52.10205 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f46ccc70-5c0e-395d-ac3d-46b09ceb279d | -1.7275 | -52.79775 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e70c6703-642a-3fee-9aeb-bb51f0ba69a4 | -1.45263 | -47.12074 | 2024-11-20 05:14:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7d44f01-7ed9-39fc-9ddc-02d40ac207a0 | -3.88682 | -52.24128 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef685fe6-51d9-3044-8fdd-05dbc3ab9e78 | -0.48347 | -52.07238 | 2024-11-20 05:14:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb82c531-d54b-35fa-9537-3998f9ae5f73 | -2.97978 | -60.98338 | 2024-11-20 05:14:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83c287bc-7a5e-3232-8193-8f37e794d37d | -2.52084 | -44.99611 | 2024-11-20 05:14:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1191096-3159-3a2d-b98e-7780cd6b1ada | -2.68788 | -46.23623 | 2024-11-20 05:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92041f6d-090f-30fd-89c8-edb5dd658da2 | -2.49493 | -49.02945 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2d05631-6e78-3168-a638-7fd0ddad54d5 | -1.26704 | -53.41468 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06ae0b8d-419a-3fe9-aeb6-d1091d9aad24 | -2.05826 | -53.44215 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24dd8734-c581-3a7d-bc62-4ad12bdb0ebd | -2.92261 | -53.06595 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| edd55ca2-88bd-3786-9d6a-223391bfce71 | 0.14676 | -51.21212 | 2024-11-20 05:14:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd0a6769-6fcd-3f46-890b-93577a284c9d | -2.34107 | -54.79246 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a6932ac-01f5-3aa8-8c01-c39fb41a6c0f | -2.38157 | -54.43648 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa1690ed-c7f0-3a6c-80a7-e600e8e2902c | -3.10025 | -53.10316 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0b0ab19-9837-3000-b212-e0ad84a75250 | -2.911 | -53.0607 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f7dcec9-f9ec-3841-9da4-b6522b9c2e70 | -3.03623 | -49.45779 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e516788d-9170-3abf-88de-4a19bd514637 | -3.48422 | -50.31831 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a8a99ea-ebb4-338d-a8af-0d040e0c75a8 | -1.11055 | -52.39395 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c5d162c-4d56-3028-a1b5-d5ad9056acee | -2.53176 | -54.01784 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README65.md)
