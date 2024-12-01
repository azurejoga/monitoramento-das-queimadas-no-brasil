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
| 8a3bfd9b-9045-3054-b703-24610fa0398c | -5.37391 | -46.3068 | 2024-12-01 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f51db1d-909d-313b-974c-becf63c75a07 | -2.81276 | -53.06111 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e973e76-3593-3889-ad9f-0a085f0282f6 | -3.99575 | -46.65536 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7432137-20cb-3fbd-b490-9f804fa9d737 | -3.30475 | -50.27376 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cf5503b-4c6a-3de3-8ceb-16b6099126d0 | -4.69702 | -42.3934 | 2024-12-01 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6444727-23c7-3865-ab31-19054505a566 | -2.14716 | -54.87221 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4511a5b-7635-30aa-aeaf-4a20d0d760ed | -6.71619 | -47.26788 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3b3a5be-0ed0-383c-ace0-549190f4983f | -2.04834 | -54.6891 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c026d7f-629f-3335-b381-ed60b91419a5 | -2.32058 | -53.8517 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3dc3e74-5e81-3615-877e-af51059f4739 | -2.87553 | -46.79865 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecda593e-e477-3372-9b25-e1727800a316 | -2.77141 | -55.35279 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 866d8228-6a5a-3d11-a468-64955209b863 | -3.25706 | -53.64499 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c566a9e-f9c4-3a49-ad25-ffde4518d4f3 | -2.75144 | -51.75394 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 354ac78b-59e4-3da4-bf56-cbea9c76c8e4 | -4.26534 | -48.35943 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b8ccaa66-40a9-3520-bc48-f2adce4790ee | -3.30753 | -50.27772 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26616c85-f7b7-390d-8c8c-a518a57d6e92 | -3.1272 | -45.98139 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b66b4a4c-d137-3f78-ab3a-b62e2e0af6f3 | -4.3244 | -48.09082 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8c5f8f2-7348-3335-a97a-45be1ac2af45 | -3.41348 | -50.24816 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb453fa5-a00e-38c0-8202-95ffaf84fefb | -1.88848 | -53.29108 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfe28fe9-d493-39bf-a2fa-53ef29833642 | -3.08868 | -53.29859 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 294dcb76-44b9-3ab7-ac6e-1bb82a02e192 | -3.11628 | -53.99189 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89913174-8710-31a6-b21a-8789e68cf700 | -1.09782 | -53.38487 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba33c497-9d8d-302c-ae7a-62882a1a2dc5 | -2.11355 | -46.55048 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2826b104-8e5b-312d-a476-3b33fe98b6ec | -1.93875 | -53.44225 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11759a14-43ae-3a9a-9421-f55b6ce466c8 | -3.0328 | -51.54342 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ae35015-bbda-3a2a-ba3d-a98724a15305 | -1.05138 | -53.20985 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd63ca41-27ab-352b-8c13-8804e6d15b96 | -4.41182 | -50.82636 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e914a03-e5fd-3998-bb68-eaf8e444b574 | -7.02494 | -44.84534 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59f29856-c26d-3993-b8d3-91c89702c797 | -3.02541 | -54.03034 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14332232-ad4b-3b15-ba04-97479f58c260 | -1.68144 | -52.50935 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8f86430-8638-39d5-a61d-ee7172d52b4f | -1.69677 | -52.64147 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c86d3c3a-f119-3778-b4b4-353637d484f5 | -1.36688 | -54.65775 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12f0bbd1-10a8-349d-b92f-ae736e5a9158 | -3.8181 | -52.24978 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f5896cc8-121e-3d73-8126-1704d57cbfab | -2.01428 | -51.20269 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2efceb6-53ce-3962-a0c5-ec1d7078ef17 | -1.19571 | -51.74499 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1113dc8-e2db-3082-8a10-1e894dc64598 | -3.31655 | -50.02811 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f615cd36-1d1c-3053-b6e1-82ee99281825 | -0.99956 | -51.72697 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53197264-c292-31e2-a69e-3d580405b828 | -2.36319 | -53.65839 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c6c68c6-63af-3317-bb32-215b170c6071 | -1.32405 | -51.96712 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb6e7313-cb2f-39e6-9508-d1e25914d44a | -1.7489 | -52.64904 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8b65e0b-9983-3920-8a60-cceb255e95fb | -3.9917 | -49.95258 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51c17a61-2513-3fe0-96a2-cd07a25e4f3f | -3.28314 | -53.00822 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d626182d-8ac7-38cc-8bb4-3ca72a76115e | -4.00093 | -44.75593 | 2024-12-01 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 8f2fb7cf-8bfe-3b91-ae7d-951b704d74c6 | -3.82094 | -46.58735 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a23c9e63-4335-3e7d-add7-5a6a34c8cd9b | -2.18947 | -53.77565 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b19c0763-ad68-31d6-9c75-f91ed9753fb3 | -1.82085 | -50.90467 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0d283de9-650e-3540-8a90-5a0752346f8a | -2.63153 | -54.19938 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 085c86c0-e06a-3b23-919a-8ab94d91f976 | -1.09197 | -53.63866 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 104dab60-bf5b-3921-a00a-4e7fdaf8057b | -5.32888 | -45.44122 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8560f4bb-219d-3d6b-9a53-6824f1a5e790 | -3.9662 | -48.83011 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e686a8-bb34-3a02-819a-214d0d2c3796 | -1.49088 | -52.43715 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d395edd-c89f-31ff-a41b-8e1288646e2f | -2.24027 | -51.82888 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de619015-38ee-3832-afca-a84c089a28b6 | -3.85931 | -46.53828 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce7210cf-0b61-3b39-99ad-5f5e7c9c6064 | -1.26204 | -47.61292 | 2024-12-01 04:44:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d36053c6-9728-3e8f-b39e-658f9cd43526 | -5.42342 | -45.11449 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 009c6cb4-3cb7-35b7-9094-fae039d1854e | -5.33089 | -45.43846 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77dcb88e-a4b8-3290-b077-0d6f99345338 | -2.11983 | -45.96111 | 2024-12-01 04:44:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b99d413c-73aa-3938-ad13-1e978e89fc90 | -3.30423 | -50.49279 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 774d1af8-2bee-3250-8d0a-4a9efee1b102 | -2.83658 | -54.09922 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53709525-96c6-3721-8562-ba2167f94c5b | -3.7533 | -51.78025 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18f898f2-ebcb-3712-b405-04fb7f26d4a3 | -2.60428 | -54.24727 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 726f3abf-3a02-35ef-9ef0-8e1854a21977 | -3.38424 | -49.8545 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0870c59c-8ca1-3212-875e-4936d5d5f535 | -3.23924 | -53.9234 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c75251b4-6973-3071-868d-c112d73c9749 | -3.06167 | -53.67967 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06bf0a18-6bf5-3caf-a7d6-7083b2668cf0 | -1.29602 | -51.37354 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1835a4f-0c1c-3983-bb8d-9c2c6b9dc513 | -3.82326 | -46.59723 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4d8344c-5912-3f54-8d90-d6cc3159c75d | -3.68745 | -51.81802 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9907d801-db3f-3dac-8d13-3d8b1604bee7 | -3.49568 | -53.80154 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59584bf5-69bd-38cb-9938-9eda6092a99e | -4.07271 | -46.68434 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c74d2df0-9f43-3d54-b5e0-b321b9d134c1 | -1.73 | -49.8115 | 2024-12-01 04:44:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4bce3db-fc5e-373d-a0b4-5826003fb92a | -3.99496 | -49.94951 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa215dd1-303e-3791-bfd5-f958fdaf849b | -1.7716 | -50.85769 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66317323-af53-3f78-91ed-e05b73ea8d32 | -2.93546 | -54.30358 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25341ebd-7735-318e-a209-338b3868055d | -3.9507 | -49.95329 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d45ad27a-b2e1-3ef1-8b17-e4b53b38ef11 | -1.24377 | -51.78997 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 416aac74-4f7b-37db-9dd1-85a623260ff9 | -3.71349 | -51.06826 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0342e73c-0f31-356b-bd9c-c473f20c9a30 | -2.48601 | -50.36074 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b45847f8-495f-354b-a200-1586f75831a7 | -5.23852 | -56.06219 | 2024-12-01 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eae934a9-0a11-3510-b677-4a5b11e9a5bd | -3.6651 | -50.9503 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46d4953f-bba9-3712-8f61-0858a554092b | -2.99004 | -53.28376 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb65c04f-7036-3544-a1f9-085ad77310a0 | -1.06501 | -51.75172 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed54495b-3c47-3982-8bfa-580ca89be5dd | -3.8199 | -52.08418 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aad649a-6b60-366d-a6a3-14a2571da03e | -3.11837 | -53.81108 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3818f6e5-1c2a-3a5f-a84a-d295a6a4d941 | -3.96942 | -47.24433 | 2024-12-01 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed6a3f6d-9f02-3d9f-928c-7a8b50ce057f | -1.56608 | -53.51931 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd0d09b8-2960-3130-8616-49a2eb283cff | -1.44493 | -47.11142 | 2024-12-01 04:44:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2964516-10d8-3b69-a3d3-8136147458f0 | -8.13313 | -44.47693 | 2024-12-01 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5db7025b-c6b2-3a64-8957-4299c076c098 | -4.10686 | -48.88841 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d01ecea4-43a5-3d96-8b7a-cd574eb7ef09 | -1.27692 | -51.82572 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c03d6067-28db-37fc-a747-586f82c435fb | -4.25961 | -47.61629 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a509616-8968-382d-9fa8-1b1b628e69c1 | -3.41561 | -50.17442 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35b388fc-a1c5-33cf-946c-fbc94f3948ed | -1.70591 | -52.46901 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c75fe3a2-e4d3-3484-b96d-282fa049cd13 | -2.84087 | -54.04861 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fcb36de9-c524-3647-8c85-3866f4955e05 | -2.61609 | -51.81529 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7e8e708-a451-3a9c-b1f7-7e4a3d53ec20 | -3.47539 | -47.68452 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a153e9b1-a913-369d-8476-cadccc57d203 | -3.3832 | -53.50794 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13916e21-b1d2-3e5c-b945-a98fe7819cbc | -0.98002 | -52.40554 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8511eec-111b-3337-80a1-f4887760402a | -3.41511 | -50.23781 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e0e36bc-d326-3148-a69a-1c9fe71b74ad | -1.19337 | -51.75988 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f6cc795-0765-3b05-bbea-b0851bd84a96 | -3.61586 | -50.19194 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README65.md)
