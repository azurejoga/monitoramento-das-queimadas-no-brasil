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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4a9a840-511f-3abe-aac1-bbc71cfca497 | -3.583 | -52.172798 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6d4bece-b06e-34d2-8e0c-3dca95207368 | -2.9524 | -51.5284 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0039a8a4-8c46-3da9-8ae4-0cc6f001ec3a | -2.752 | -54.154701 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30b542bf-43fe-3850-bbb3-045ec58bb419 | -3.4723 | -54.4734 | 2024-11-28 00:38:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51675876-fc30-3f4d-90b3-d8a6f19c6d6a | -18.7924 | -55.836601 | 2024-11-28 00:38:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 308ea642-3867-32fb-932d-e4f9dc846557 | -4.7749 | -44.4202 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc58d7f2-85d8-3312-953a-f0b42179740b | -2.7726 | -54.063099 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5f7f59-c1c8-3981-95f1-a19f806aec0c | -2.8269 | -54.0294 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da7a5452-c84c-3ff1-b972-e9bbb4543f77 | -2.7076 | -48.6563 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4a64300-f3da-3d71-ae5c-90bdd1af1dc4 | -2.5127 | -45.208801 | 2024-11-28 00:38:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca6c660-77a1-399e-aa2f-a68537265f9f | -3.3917 | -51.2393 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a4ab15b-8aa6-3719-8359-e7416913885c | -3.0801 | -48.664501 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07aecdc9-d3c2-3a19-9838-9985e637364b | -4.934 | -45.427898 | 2024-11-28 00:38:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54936e10-ae21-3bb0-9f86-97b65e4d1ea5 | -3.6877 | -53.550598 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b35cf7f-e320-350b-9ace-44c61e2f142c | -2.2653 | -53.4571 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0200ec65-2976-3d0b-84a2-785477cdff0e | -2.9343 | -51.448898 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588b42f3-5765-337e-ab6c-37e96315eb26 | -2.7088 | -51.681 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492700c5-9e26-3a22-bf59-b99f24a3a0e0 | -3.9668 | -50.1917 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b79c7b68-5347-3ad8-be4c-e7603bc5debd | -2.8519 | -46.836498 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 271d83d1-6101-364f-a937-1c18ba8fcc53 | -2.7989 | -54.042801 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 796e3ec4-7345-3fb9-bd40-c089dad36185 | -2.8072 | -54.033699 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c712729b-fcbc-3dc0-a8de-b7140cdc7981 | -2.8421 | -46.838799 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3f8126c-4050-35be-8672-013a0b57e060 | -3.9666 | -48.092098 | 2024-11-28 00:38:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 501386ec-817e-3edb-9b20-2ef58fa8a6cd | -6.0996 | -48.050499 | 2024-11-28 00:38:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2ab16f0-739a-3a98-8619-c8da02bf82bb | -2.3289 | -51.960201 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56ef0343-427b-3125-8e1b-801859094e52 | -4.0273 | -46.3283 | 2024-11-28 00:38:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b613b1bd-a280-3a97-8a10-f2687532c22c | -19.5329 | -47.329498 | 2024-11-28 00:38:00 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c3091a5-c590-3869-8313-a7737a4c8bb9 | -8.5749 | -49.200298 | 2024-11-28 00:38:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fe7e8d8-28bd-3d82-a497-378ca1bb6eee | -2.8563 | -54.0229 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7c2a8d8-5945-3462-9c16-1d0e9b3067ea | -4.035 | -46.535 | 2024-11-28 00:38:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d239edc-2206-36ca-ace1-04cb2caea1e5 | -2.1842 | -52.140499 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4e1d092-7802-3bee-9839-2591384957d2 | -2.4231 | -53.837502 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca4d912-a655-343d-9eac-4a65f6c8f86d | -2.8005 | -54.049702 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e999f8-73b7-32b3-b689-62129f6e7f74 | -4.6669 | -44.611599 | 2024-11-28 00:38:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f201c40-6afb-3657-9ff2-3546a6d31f61 | -3.124 | -53.7472 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9d67d0-3f3e-36bb-86c1-83dd33ceb655 | -3.3291 | -45.499199 | 2024-11-28 00:38:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc65a92f-e7e3-3793-82bb-4c2af82d5dae | -3.0958 | -53.301701 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32da3ddb-d334-3b5e-afa6-26ee2684ee68 | -6.0853 | -48.033401 | 2024-11-28 00:38:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9844b67f-27da-3f4f-bdc0-7bc076bb76c1 | -23.7248 | -50.5499 | 2024-11-28 00:38:00 | METOP-B | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 824c1a94-15bd-3b0d-aa1e-26c35a8573dd | -2.792 | -52.868301 | 2024-11-28 00:38:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74e77aa9-d386-3903-8eca-24990e496e22 | -2.7071 | -51.673801 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 824b65ed-cf17-3e48-91cb-13df4d4ec630 | -3.5165 | -53.797501 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f452e7e-4cb9-3ab5-9b04-1c6a6f93224b | -2.1923 | -53.773701 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40dae7ca-a2fc-3b1b-8fac-d35f63321e54 | -3.2882 | -50.5592 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b933d133-492a-3c41-bbf0-84aa71b28c36 | -3.965 | -50.183701 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee46369-0685-3ed8-bffc-561346fdf642 | -2.4437 | -53.883202 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d13a75f5-ada7-3710-8450-689bf30dbfd4 | -3.3498 | -50.512798 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 191337f9-de2e-3eaf-ab26-ef6386f8ace4 | -3.518 | -53.804401 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d96488-266a-3da2-a83d-7af8a6562d1f | -2.846 | -54.0686 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46c93099-5f24-30ba-ad7c-bf30743125d3 | -3.6776 | -45.802399 | 2024-11-28 00:38:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97bd3e0f-f636-38ac-b27b-f9d27538bf55 | -3.7066 | -50.225498 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3cdfbd7-333b-3e75-aa23-1dfa59472c03 | -2.6079 | -54.201099 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a287cb2-b707-32d2-91b8-6e6a613a2f94 | -2.8354 | -54.480301 | 2024-11-28 00:38:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35f6f169-5747-359e-90fe-3117984fc1bf | -3.9618 | -48.0714 | 2024-11-28 00:38:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc1ba1df-7ae3-38e9-b9d3-055003b88aba | -2.8102 | -51.582901 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f230964-9749-3c73-8b78-bf361cae4eed | -2.5454 | -53.9688 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f22e431d-9d5c-35c1-8bd5-a1961d873461 | -2.5851 | -54.053902 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61aa0fc1-b4a0-30ed-93b7-6f28c216d176 | -3.0776 | -50.9911 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e513f6b5-d8c9-3496-bfc1-534b2085e0ad | -3.108 | -53.721901 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2241aa73-5765-3185-b2e2-0d95484cc304 | -3.0822 | -50.9664 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a044d9c2-18ae-332f-b051-a5bc5af03f6a | -2.2693 | -53.7495 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 698fc54c-3380-3ccb-9d36-9dc8e24be31e | -2.6072 | -51.8237 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e9b4f90-d567-3ec3-981a-9b0233699825 | -2.9085 | -54.163799 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 705acfd3-a712-34d5-a392-0941632e5677 | -3.2299 | -48.823299 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8017741-b449-35f0-89d1-15eaa66278df | -3.2414 | -53.627701 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8161b41-3937-3bc5-bff3-d7ba28728df7 | -3.1244 | -53.978199 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37d34f07-6a94-3aac-b4ff-72a799fc57db | -3.1071 | -50.352501 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c353bbd9-fb4a-3d0c-91aa-d652799b1a87 | -3.0896 | -49.1978 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3405b6e-2d62-300f-ab6f-6cdcb6b85029 | -3.0537 | -54.030102 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f18b5f00-9903-3ecf-9e78-0fa67973cc65 | -2.732 | -48.896301 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd01295-30da-35f8-8a93-ab91b9c9d59f | -2.8253 | -54.022499 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 241bda98-4499-369d-a4a9-3951971db266 | -2.8398 | -54.041 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb72e58-a66c-343a-ae93-3851876a33a8 | -3.5777 | -53.016102 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1ba9482-6fa6-3b86-baf9-f852660428ba | -2.3949 | -47.1684 | 2024-11-28 00:38:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c7d28d-bdaa-336e-9c0a-b17e4e88a033 | -2.8532 | -54.009102 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07f8d045-b01d-3d6b-b9c1-0f97a0f24ced | -3.6009 | -50.349098 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60e65595-a82a-3d3b-bce9-9a9c0589b326 | -2.9925 | -53.3461 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43227024-2a58-3ab4-8b66-fe0015de68d8 | -2.8496 | -54.038799 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ada31df-4307-346a-b9a0-d3a212b5ce1d | -3.3172 | -50.279999 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d01e68-2647-337f-b475-19a13e6d1f8b | -2.0296 | -51.186401 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b20ea35-705e-36e5-bc91-7db3d727cc8f | -2.8574 | -54.073399 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979b0488-c114-3133-a18f-bba480a42f7c | -2.5901 | -53.6642 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 306754fb-b2e1-3c3f-8e0b-533e0a235db3 | -3.1734 | -53.234501 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d21d6e5-17cb-36c8-8e14-f32e75f81d61 | -20.6854 | -49.118401 | 2024-11-28 00:38:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a1ce7028-5dee-39bb-9792-afc45a0e5245 | -2.6058 | -53.962601 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26c07828-bf8b-3d36-af84-aa477cc9f853 | -3.0819 | -49.209099 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83719a67-9a71-3840-bb72-9755bd7f4f18 | -3.1161 | -53.254299 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b02f1d20-8ced-33af-afa9-edf59c09ce6b | -2.9916 | -53.8918 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5159ac0a-5e35-3dd1-83fd-e4ce06a3bb51 | -2.8238 | -54.015598 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7508bd-4d57-3806-bac6-a3a1bb4227e4 | -2.5843 | -46.040901 | 2024-11-28 00:38:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c3f4950-1b50-3ee0-a483-bf00fbe5d865 | -2.4524 | -53.967701 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c14bec88-4345-358e-899b-7e7ee97c0078 | -2.8774 | -46.8577 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e28b4f-cecc-34ab-b9ed-15c0e2b2ffac | -2.2637 | -53.450298 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60eec2e2-984e-3c0f-a06e-4321cc141bd9 | -1.946 | -52.09 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 418ffa86-b7fc-3ec7-a009-f07022dcac90 | -3.8073 | -51.389801 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b05d919-1eb3-32a8-be70-0893df1918ba | -3.4207 | -50.146999 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2d93eba-b257-37df-a38d-50bde5348bc1 | -12.0284 | -49.544102 | 2024-11-28 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad45db03-d3a0-3798-aaee-be90ceddadab | -3.0758 | -50.983601 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3986120f-d7d6-376a-bbe0-15d898c6c940 | -2.0147 | -51.1661 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84bcb6ba-a3cf-3390-bf1c-a93ebba5633d | -2.8247 | -54.066002 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
