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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a2d435d-196e-3c6c-be61-7eeec8d9c7d1 | -3.0735 | -49.1914 | 2024-11-25 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 9f35e97c-66a6-3dfb-8250-3b2764341e48 | 1.8398 | -55.9007 | 2024-11-25 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ba6098fc-e43b-30a8-9b12-90beb421a998 | 1.8398 | -55.9204 | 2024-11-25 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e18e7e99-a1c5-3659-a2bf-e61432804aa5 | -2.3394 | -53.8818 | 2024-11-25 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 57412d0a-c17a-3630-9613-94aa2a7a2032 | -3.0883 | -53.253502 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d681b5-9483-3370-ab48-280be1379981 | -2.1712 | -53.796001 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed36fc6-5de5-3de5-9115-2def0af47013 | -2.9152 | -51.703201 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50242015-0785-3288-8136-83c1818dccf1 | -1.3176 | -51.750401 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7b3b5e1-7a9d-3b7d-b327-4abcec5a49a8 | -3.8554 | -52.1534 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2856bc06-f7e2-3243-882e-dd14023f6079 | -1.8886 | -53.330399 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a74afd-7731-3c59-93e6-78beea4d35f4 | -3.264 | -53.703201 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd41f5d8-24e4-33a7-84f8-7727ceed5265 | -2.6311 | -51.767601 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99191b9e-0064-3d56-b35d-9182e47e66e0 | -2.8216 | -54.112099 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4064fa2f-1c5b-3535-a01a-398b8e089569 | -3.2696 | -53.817402 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dac518ec-b101-3f27-9096-55ce04783d2c | -1.1168 | -53.383801 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd67db68-0917-3083-a0ce-0e7f62874128 | -1.4694 | -51.515499 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8940237-262e-36ea-9b6e-9151e787973e | -2.5699 | -53.959801 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 266db66e-775d-38d0-80da-2990ce363fd6 | -2.829 | -54.0098 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ace9f7-d3e5-38ca-b703-6d92421161b2 | -3.7108 | -52.419899 | 2024-11-25 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20bf481b-82b5-3b7f-bf2d-349e687e7120 | -2.8486 | -54.005402 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c95e4445-322c-3582-8f6a-0392f0598161 | -1.7719 | -53.630001 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 033ac8cb-90a8-394b-b9b1-a0e11d7ece91 | -1.4521 | -53.405899 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea94aa59-fe61-30e9-9b24-3ac50732ceb8 | -3.513 | -53.798801 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28f6d2ec-83d3-3abb-b248-b943c45cef2a | -1.725 | -53.247501 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc4c585f-8c06-316a-a04e-54827a036e52 | -2.8314 | -54.109901 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca59f36-98e5-357d-b471-ca4aa1c2d1d4 | -1.0921 | -53.634899 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d9667c2-deb0-35b1-9e9d-0b35cdd31ae8 | -1.7405 | -52.7328 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98df0a5f-0a0e-3a30-9491-15201639c5ff | -3.2468 | -53.269501 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5f3a513-ddaf-3668-9352-0f28bb2d192a | -2.8553 | -53.989601 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbbd604-987a-3f2f-949b-9600d2f57741 | -2.1664 | -53.775299 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1bd1ba-5940-3382-85ad-ddf5e21afe1f | -2.1762 | -53.773102 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33b91034-b462-3deb-877d-a9b0094af03f | -3.2856 | -53.662102 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b19ae59-c42d-39e1-a05f-b4cf598e8e8d | -2.7666 | -54.052502 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc9b43da-b27a-3714-9e7c-f10d3d3c0359 | -2.9032 | -51.562698 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2191d70a-b2e2-3eb5-8bb1-3c7da79edcbc | -1.6139 | -53.302399 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1079f4ff-dcbb-3db4-b97d-08063a4ffb2a | -1.2415 | -51.733002 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb1e48f1-a1bb-3a39-acc7-0bc5e78d2eed | -1.6012 | -52.263699 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad6aba5-b28d-3c30-90b0-4c565aff97a1 | -3.822 | -52.231701 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5c3999f-4c45-339d-9cf9-9257ddc95b9d | 1.8529 | -55.905899 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de12a70c-da26-3d4a-bc9f-22d86f1e2191 | -2.8251 | -54.0826 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b618538-16fc-302f-8e33-f38283d6e146 | -1.6303 | -52.434502 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7c5557e-8075-3d74-9bd8-655d8a8e5c4b | -1.3891 | -52.327702 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdb0cd26-110a-3663-b7ae-47def779e448 | -3.2871 | -51.129601 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e958b6c7-a75c-3ee0-b704-22a01bccf491 | -2.3405 | -53.8596 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b417435-aa96-3dab-8add-c9ce72133986 | -2.7733 | -54.036598 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc869b5-ca71-393f-a8e1-3ac9caa42b13 | -0.8892 | -51.7253 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 363e8263-f9c1-3b23-9cfd-ea5bea63c5dd | -3.2329 | -53.926498 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13527193-05bd-36ad-a9ad-a5e41abefd55 | -0.9503 | -51.6325 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb7f8840-2e33-3eef-94bb-53c00a7db5f2 | -1.5258 | -51.6255 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1837f1d-4ba3-32f0-9247-6d895a38974d | -2.8306 | -54.016701 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e1a051-99af-3e10-82be-373a48fd7883 | 1.8384 | -55.924099 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39bd27bc-3b54-3552-aa28-3ca6fa6aebe5 | -3.1033 | -53.991501 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e495b60-659a-38c0-b33e-073f8b9044d8 | -2.5421 | -53.973301 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e117c2d-1522-319d-ad94-05dbcd84cd3d | -1.2434 | -51.741299 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1966b446-3133-3193-84d8-d5788b51620c | -1.7192 | -52.7299 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 609f6472-1c81-3ccb-b047-adbc18427192 | -3.0589 | -53.215801 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 155a71a7-f46a-38a3-9a43-bad9d915f729 | -4.0224 | -48.084801 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7759a624-c2e3-303d-ac3e-40ddcde9d663 | -2.8337 | -54.0303 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36aca25b-ba76-3122-acdf-a4111b07b89b | -2.8953 | -51.573101 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65d6ff1b-6861-35bf-9f0e-2fc4208d4a22 | -2.811 | -54.021099 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd18b3b3-5ad2-321d-aa66-4229ca158fc5 | -2.8231 | -54.1189 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11b3a6f5-badc-337c-8aaa-731a98047d33 | -0.0622 | -50.818901 | 2024-11-25 01:01:00 | METOP-C | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7403760-4d70-37cf-9173-38c261e75427 | -3.0378 | -54.0205 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1803fd1c-88b3-395b-8e00-5ac2eecfac38 | -2.8023 | -54.073299 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87966dac-d8e1-3c58-8386-31ae838d0b6d | -3.1905 | -49.047699 | 2024-11-25 01:01:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d3ab9f-8593-347e-b390-32361f42b455 | -3.8519 | -52.1385 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e983adab-db0f-3475-ab74-061427ebfa64 | -0.2184 | -51.183998 | 2024-11-25 01:01:00 | METOP-C | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b631d0a-ff4b-3cda-88f0-c242c84669ad | -3.5146 | -53.805698 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c051dce9-7c19-3f77-8b37-920529a6d866 | -2.7878 | -54.054901 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f420666-8ded-3735-a646-ff4b19f564cd | -2.8584 | -54.003201 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e40c5f55-bfae-3a06-bc9f-dfc9595b5b16 | -2.3443 | -52.177101 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 370d4ea6-61cd-390d-a867-b5b03dc98393 | -2.9317 | -51.7743 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec8a185e-1fb0-3721-a25e-e4069576a9e5 | -2.568 | -53.9963 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0e6f519-0293-3e04-b1dc-f50f8aae82d4 | -2.8619 | -53.973701 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd5cbe4-485b-3e96-8d40-3f10db3e9d6f | -2.8537 | -53.9827 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a975d2e-a4ea-3d11-9d88-36062e7f8d55 | -2.6525 | -51.771 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c812add-7fba-3cb0-8e4c-55d49e6a25f2 | -1.726 | -52.759399 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b0fad9-1b82-3e96-837f-62e96783fcf0 | -2.5829 | -53.971401 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd2015b-14e0-3cfb-a173-498653c624d2 | -3.7101 | -51.794601 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5639965d-7a24-3bae-b82a-c123d04fbb9a | -2.6178 | -54.257999 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d8241e-262e-393d-9b9d-f6ff7ceab813 | -3.0573 | -53.208801 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e724f893-016c-3fd0-9b10-78433378fad8 | -2.3421 | -53.866501 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d27f09b3-0a12-3ddf-b0f2-abcdc564322b | -3.2313 | -53.919701 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 404acffc-84bb-3b9b-b59f-9b7083e09633 | -1.3021 | -51.728001 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e473555a-3042-3470-a6c6-8589057a2c0a | -2.917 | -51.711102 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2858b2-09ef-39d5-8d4f-3e2f44bfe196 | -1.0458 | -51.7337 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 14642988-ac5c-327b-bfa2-7121510fbe88 | -2.1915 | -53.6604 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7366cd1-9ed0-35ca-9492-552915357727 | -2.8321 | -54.023499 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 651607f2-68bf-3a4d-bf53-9a8c4264ed38 | -2.8282 | -54.096199 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af2a5838-f4cf-3c05-b9a6-9b4c66a569a3 | -2.6064 | -54.253399 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ca8f0e-18e3-31bc-a0fb-d09287e474da | 1.8333 | -55.901501 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e7da778-5def-3fb8-82ea-da3c7184c06e | -2.946 | -50.993099 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408f6f43-e17e-3a7e-bc52-ad4e21f1507e | -3.5035 | -50.467201 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b319b41d-bd51-363a-9fb7-a0f2a6b7559c | -3.7085 | -47.116199 | 2024-11-25 01:01:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0597e415-c143-308c-a22c-8e8deef5bc8f | -1.6145 | -52.365898 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 167947a4-3c73-3e6b-8c8c-a7d6f58a18a8 | -2.5888 | -54.042 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb42152b-b899-3cbd-8bb2-a6ce3f10a5fa | -1.1963 | -51.760502 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08daeea9-2c1e-312b-95a8-52a7fdca613a | -2.5715 | -53.966702 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c33d73a-a226-36ab-b5df-e99abcdcba4e | -1.6029 | -52.583599 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24a5ba48-934e-308c-9bab-36ac62fef12b | -1.7703 | -53.623001 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
