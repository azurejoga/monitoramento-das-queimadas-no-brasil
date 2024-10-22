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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5b98e1d-f2f4-3508-a803-4d737eca2cdf | -2.75981 | -49.30919 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| fdd37df9-5a34-3b46-8883-e18c8ea892e0 | -2.75949 | -49.36155 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a00888e-bf9e-30b6-9855-fdb9209dae4b | -2.75914 | -49.33157 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c78554a-d281-39fb-ae00-0103e0910312 | -2.75905 | -49.31408 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0167cea4-1db1-373d-a90e-fba8bbfca84d | -2.75829 | -49.31898 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 871268a2-f672-3477-8d60-ec3ae1735e88 | -2.75807 | -49.30636 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6ec3e3b1-9f7d-3e5b-b0b8-6ad9b65b18f4 | -2.75754 | -49.32384 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 8ce1dff7-146a-3f1c-9569-4f3f6bb34e20 | -2.75735 | -49.31128 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2ac54aab-615c-39e5-b810-67c042a42ff0 | -2.75663 | -49.31618 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| e4888d8e-7004-31dd-b425-0ef9f084ae1a | -2.75591 | -49.32108 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 4180b8dd-9700-31b7-9cfe-7dc15e1805cc | -2.75514 | -49.30844 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3aa3abce-f401-38ba-b6ba-1ef32568b2ba | -2.75438 | -49.31334 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7ccf8d49-267e-35d6-aef6-2bd9db2d81d8 | -2.75363 | -49.31823 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 2c5a4b4d-9e71-3ed6-897d-4bd6d98874cb | -2.75268 | -49.31052 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19762335-8e44-3931-b81e-1ba6c9b166ea | -2.58086 | -49.24001 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c191380e-9312-36cb-88e4-74e666f5af29 | -2.58012 | -49.24495 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aba568f4-9940-3173-933f-27f7e88cec40 | -2.57006 | -50.0638 | 2024-10-22 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc1e8930-8aa8-3dcf-8b53-9eacefea171a | -2.56628 | -50.05882 | 2024-10-22 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab342e3-b168-359b-9c8a-bfaf8ddc1429 | -2.48668 | -49.11676 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a1c6cbd5-a5a9-3080-a4b8-0cc79743b4d8 | -2.48271 | -49.11101 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b98e1ff8-510e-34aa-83bc-d72c1387219d | -2.48197 | -49.11601 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0de792fc-d616-3b13-9ba1-b5901112296c | -2.48122 | -49.12104 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 612372ac-d771-3949-a3f3-68a3c4a635e8 | -2.47874 | -49.10527 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d13cabc-38c1-3e9e-b3ae-d97677f6f50a | -2.478 | -49.11026 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9354afb2-1f99-3fd5-9b05-ec5fc9b40ec6 | -2.47725 | -49.11528 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03a8e378-03ef-3d8d-8288-5f57f4ac5d17 | -2.47005 | -49.0987 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d32b46fd-1661-3ecc-bd0b-b8d3142b3855 | -2.46872 | -49.09631 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6455c0f5-be9e-3f06-81ec-21b8de639d39 | -2.46607 | -49.09292 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6cdf7de2-3658-3a24-94c8-7804c2562fc4 | -2.44611 | -50.25678 | 2024-10-22 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f21c02c5-0085-31c5-8aba-6ce7a2b3f3ca | -2.42427 | -50.28336 | 2024-10-22 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b094a947-f8db-3049-873d-c74e0abf529b | -2.42364 | -50.28753 | 2024-10-22 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8948a9f4-2b75-39fc-88b5-6bd366d99a38 | -2.42302 | -50.29169 | 2024-10-22 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5ea3dd2-9ee1-3e68-8949-d13ca6a94974 | -2.41867 | -50.29101 | 2024-10-22 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24af4bd6-3a96-3484-8339-36b481c2ec9d | -2.19163 | -49.70612 | 2024-10-22 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0b60f9-7d66-3d85-b952-105ca76773ea | -4.4254 | -49.80335 | 2024-10-22 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37ccd888-9acc-3e27-ae0f-95e3cb6aba28 | -4.42146 | -49.79786 | 2024-10-22 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa0e5930-75a2-331b-a051-d030805d7d27 | -4.42076 | -49.8027 | 2024-10-22 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ce6120a-ed9b-3600-869f-8b39634bb1c1 | 0.99063 | -51.1598 | 2024-10-22 05:10:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a78db76-b212-3248-bc1a-202bfa8ab537 | 0.98674 | -51.16042 | 2024-10-22 05:10:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 826ea071-fab6-3ee7-b4e7-5b4b3ef9b009 | 0.98202 | -51.18135 | 2024-10-22 05:10:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 470ffc12-4a2a-3f07-bd0a-c48515377f99 | 0.98125 | -51.17643 | 2024-10-22 05:10:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19439c09-fc92-3514-bb91-486422e3c3af | 0.97736 | -51.17704 | 2024-10-22 05:10:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24cf2ba1-b458-3a33-9702-5ee127214c76 | 0.88681 | -50.67617 | 2024-10-22 05:10:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 25d9424c-3df0-35ea-b97e-6c8383153ee6 | -2.24171 | -50.54959 | 2024-10-22 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dcdcb9e-3d85-35d3-8bb2-8ded3e2f2295 | -2.23338 | -51.88449 | 2024-10-22 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f50b3df-4ea6-3443-8d93-612093fd5036 | -2.22948 | -51.8839 | 2024-10-22 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88120ba9-a9eb-357e-b7da-b90f2ccfa5be | -2.31314 | -50.47778 | 2024-10-22 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7956e418-2952-3b41-99a9-2de8529c39ff | -2.30947 | -50.47311 | 2024-10-22 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f601aaa-ee2b-3a58-bda4-1b96f6df2b5d | 1.00907 | -52.21976 | 2024-10-22 05:10:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d49bb192-4611-3592-9e68-23d59ec6267d | -2.21279 | -51.99113 | 2024-10-22 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f258f46e-373e-3634-bb27-6dc7670f3b57 | -2.08789 | -53.22898 | 2024-10-22 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17c547a8-2565-354a-8991-626579d6f66f | -2.08726 | -53.2331 | 2024-10-22 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b57a254-8415-33c8-b1bd-05a03051bb7d | -1.93475 | -52.10511 | 2024-10-22 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c50e370b-0725-3339-82be-0b116a6c888a | -1.93402 | -52.10986 | 2024-10-22 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7bde717-7bf4-39e5-bc94-a5ca704bf29b | -1.93092 | -52.10455 | 2024-10-22 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f15eb20-0035-3d52-b371-c2d00774a5dc | -1.80203 | -53.1591 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05cdc4c4-36e3-30df-821c-fb582a2a1aa3 | -1.80139 | -53.16324 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee7b48f9-9434-3401-8010-40b992cca6d0 | -1.79843 | -53.15854 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9fef6442-d489-371e-a605-04597d3060d5 | -3.11122 | -53.12757 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71d2c1ab-b79a-3104-9405-80ce018165f1 | -3.11055 | -53.13194 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f50e9a31-de56-3ee2-819f-f69ebabfefb9 | -3.1089 | -53.1183 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72ec0dbe-2b49-33ec-93b5-107a8142d362 | -3.10689 | -53.13135 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1baa7bd0-d775-3b3b-8f44-7926619148ae | -3.07095 | -53.24355 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e63605-3483-3fcb-b8c4-255952ee3e27 | -3.07029 | -53.24783 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f144600-ba51-3fc6-85f7-9e86fe79acd5 | -3.06964 | -53.25212 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c54b92df-c8de-3649-aa4f-0182c1e591d5 | -3.06797 | -53.23868 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 458cd41c-ad70-3cf5-a92b-86e8cb25d34b | -3.06731 | -53.24297 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17406e12-d9c1-309b-994d-b31177d14869 | -3.06666 | -53.24727 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a09b5a62-0f53-3cb9-ba1b-88c9d7dc7478 | -3.06433 | -53.23809 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69323053-4cd7-3588-b1b2-2a66007965f6 | -3.06368 | -53.2424 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2211d334-eb82-3f9d-8b28-52def9180b66 | -2.85455 | -53.33428 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b6d01b0-4f71-34c4-9591-6493a3b74b26 | -2.8539 | -53.33845 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93b007ba-6857-3d1f-ab61-be28a984a1d2 | -2.85093 | -53.33372 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cccd63ec-53b4-34cf-989a-ce89278865ce | -2.85029 | -53.33788 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81012c53-a384-3613-9e09-846e12098a74 | -2.84965 | -53.34203 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8255144-0b20-3140-89e8-e34b0cb672c5 | -2.84732 | -53.33315 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c52b278-4da8-3c2d-9748-8354be09c104 | -2.84668 | -53.33732 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 613587ce-8cc2-37d6-83e9-a43c282856c0 | -2.84604 | -53.34146 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85ef8579-6a6c-3b53-90a0-810632ffadfc | -2.84371 | -53.33259 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa7966af-874c-3f6c-a9c7-4210b185edec | -2.84307 | -53.33676 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72b80649-b8a6-3d02-b8e0-c71ec5c0d678 | -2.84243 | -53.34091 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aedcc58e-8f22-3289-9b4b-088408e6f393 | -2.84138 | -53.32369 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34bcf060-0733-3859-83b2-838259f32baa | -2.8401 | -53.33203 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff1aaf02-667e-3f8b-9c94-10b465002b64 | -2.83946 | -53.3362 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3e93bf3-163c-3919-b217-a30a61515b70 | -2.83882 | -53.34035 | 2024-10-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ce6678d-211f-3242-83bb-e6ac0362e504 | -1.52602 | -54.814 | 2024-10-22 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c27ec5c-a796-33ad-aecb-5cea749a0e67 | -1.52546 | -54.81758 | 2024-10-22 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6106309-106b-33ab-a1dc-11a9a22162d1 | -1.30404 | -54.18952 | 2024-10-22 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbfb7319-0bbe-32c6-9fd0-ecd05c53508c | -1.20166 | -54.17008 | 2024-10-22 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 036555b8-a11a-335d-a9ce-5b44ea448ba2 | -1.08965 | -54.16833 | 2024-10-22 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 389d66db-a2cc-3007-877d-a6c826f79e67 | -2.089 | -53.57396 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f9b83fa-2002-3a60-a284-96f34d6eefa1 | -2.0761 | -53.56378 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e59abe63-ea8f-3b3e-b650-f9d060a24cac | -1.58159 | -53.50397 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7620341e-9679-37ad-98ba-60b31ffceb05 | -1.2385 | -53.37822 | 2024-10-22 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54da62ca-f974-3808-84f7-ec472f140f1b | -1.23787 | -53.38224 | 2024-10-22 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2b92af8-d263-391b-8da1-16f8b54b9bd0 | -1.23496 | -53.37769 | 2024-10-22 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f57da489-eb80-33e6-b464-04b87b78f309 | -1.17933 | -53.66339 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46afc9d1-264a-3a19-8bc7-33d8f411ffa4 | -1.17646 | -53.65889 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e0a0919-6b24-350a-92a0-c11830bd95b5 | -1.17585 | -53.66278 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0025e275-4aa2-3752-bfa7-9d832edb18d2 | -1.17524 | -53.66665 | 2024-10-22 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README28.md)
