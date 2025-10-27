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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 892de7d8-5ef4-3f50-b0f4-11d035719f53 | -4.09749 | -44.61233 | 2025-10-27 04:32:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f111db09-c609-398b-ac77-67ec9b5e8ec9 | -7.85553 | -46.48616 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89f5e5a5-335e-3275-967c-8d7f5f765dbb | -6.13386 | -41.71505 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0676404b-dbc3-31d3-a2d7-9594fcf83913 | -2.3232 | -48.58002 | 2025-10-27 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e8ef9a5-d6cc-3cd0-996c-65a2dc86cddc | -2.61143 | -47.34809 | 2025-10-27 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d76b7cf2-a910-334f-b974-e2e563151ae9 | -8.06849 | -46.95643 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4400eb84-d2a7-3cbf-9e64-1cf542c9401f | -3.86894 | -50.8895 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fc3c510-1b8e-38b2-8df0-e244395c9007 | -1.38027 | -55.34619 | 2025-10-27 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f8771c3-0108-38f9-ab66-357fb1b3553a | -9.57646 | -46.89264 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bda4965-cde0-38dc-9cac-955914aeb5d9 | -7.84202 | -46.4841 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35d011c9-e16c-3221-b951-12a4c0df4ec7 | -9.35075 | -50.61951 | 2025-10-27 04:32:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 079133c3-b734-3795-98df-326cd338dbc0 | -7.6437 | -46.77735 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c5fab22-6ba0-3c1c-be51-0444b223b84a | -7.83574 | -46.45728 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f885f72a-8efc-3506-9ab1-a20a4ae6dc4a | -6.13444 | -41.71097 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 48807014-0620-3c81-8e3e-b6da5b5ca08c | -4.4417 | -43.4225 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca48d55f-5c92-3064-b1bd-da1173ec5c51 | -3.55829 | -53.0159 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 373e2a79-767d-3084-b644-f167ab9c7f43 | -3.07429 | -48.02132 | 2025-10-27 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d49aefcb-be89-3d3b-8caf-2353b96f89c5 | -7.07476 | -47.35795 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a3bb1d1-434f-35db-b59d-f18303f486d7 | -6.88223 | -43.57513 | 2025-10-27 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5c829e6e-eacc-36a3-a93f-913fdd121f08 | -7.44342 | -41.86711 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a193b7ec-cc78-305b-ad05-82cf05f7c053 | -7.97429 | -45.46843 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aab25ded-daee-3a0d-8358-e9461d9dc0df | -6.3868 | -45.76874 | 2025-10-27 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45e01d41-573a-30a7-85cd-443e10a0e331 | -3.81489 | -44.53956 | 2025-10-27 04:32:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e17f489-1287-3c0c-9b00-abc2c3e1c9b1 | -3.14716 | -50.33511 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0edf579-74d0-3d02-8dbe-77435b8d607f | -8.10382 | -47.05999 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4213fe18-884a-35cc-a89e-1897226cd034 | -2.53188 | -48.24327 | 2025-10-27 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b17deaf-9b33-3a32-8958-894a7fc23b56 | -6.62699 | -44.62989 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3b231e2-7f3f-3b75-b559-ee20191ae9b0 | -4.08987 | -46.927 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3caa647-9f1d-3416-9d24-7bff5e92b49a | -7.78866 | -45.37755 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e1ad448-fae1-322e-be50-566eb82af0b1 | -9.45931 | -47.72946 | 2025-10-27 04:32:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2b3ce20-7499-366d-8bb5-2200ab719fa7 | -4.4601 | -45.45309 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c92b6f9-c222-3fb5-860e-218d397d07af | -7.35451 | -42.45673 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 35fccef6-8162-30b9-ad79-54516483f249 | -8.90408 | -48.02008 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ba6fe88-2f0f-3709-b047-88bf84531b40 | -1.35025 | -53.48489 | 2025-10-27 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a3b2ae1-a898-3af2-a7b6-e9a3e459ff6b | -8.01344 | -47.38067 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 303df7c2-2995-3b15-98d1-1e8570dcaf12 | -3.10085 | -49.45829 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d857832-b696-3020-907a-6040060b32d5 | -3.73062 | -44.51992 | 2025-10-27 04:32:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3d7e01-6b7d-3fbf-b625-6ebaa96d8185 | -8.88612 | -44.84213 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2893323b-2e62-370b-9c4d-87fc45530b64 | -5.88871 | -49.37971 | 2025-10-27 04:32:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1a2feb0-5481-3032-a0bc-d8b0ac6cdd27 | -6.28835 | -44.71332 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e77c0aa8-bcc2-3a2a-93c4-285f2e39b6e6 | -6.88676 | -45.16036 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a65b5eb-2720-3985-a254-2afa330b2724 | -3.14259 | -50.22271 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ce5f37a-81f4-3d23-aa79-2e77c3ba948c | -8.52694 | -47.20509 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f91291fc-c61e-30f9-b9eb-0116c3a91399 | -6.43889 | -42.02894 | 2025-10-27 04:32:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d83048da-097f-3345-b584-925e554914a2 | -7.87641 | -47.255 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6311d77-4739-3921-b89c-6ea114f6a322 | -7.2247 | -46.8729 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f405ad5-95b8-374c-ba8d-016ba8fc9172 | -6.87973 | -45.15923 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 92ee2a57-8121-3d53-85c9-969650e09931 | -7.83808 | -46.48722 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2914bea5-6c68-3bd6-8fb8-d5f7a6055d71 | -3.11485 | -51.20829 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c518381f-ee87-307a-94c7-4210ee9b0108 | -3.79851 | -51.34943 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dd59280-9c57-30ff-877e-29fb52db3134 | -5.63162 | -47.62089 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a97f6ad-0f29-350e-b0c6-c01fed96ac21 | -2.97597 | -51.03102 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 277a133c-baf4-30b8-85b5-2ab45a1d71ff | -6.49418 | -42.21804 | 2025-10-27 04:32:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 13988ceb-2285-31e2-bfb5-5546c0e8d45a | -4.76728 | -46.42303 | 2025-10-27 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a443c79f-a758-3f21-b312-9125bef3c405 | -3.57538 | -49.01773 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d782df54-f232-3b8f-875c-d3ea8fbf7803 | -8.10049 | -47.05946 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 039ef4b0-8fc8-399f-a87b-ec405bd3caaa | -2.86883 | -52.7959 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8902ffe9-0def-3855-a308-f3d533739b4c | -7.77223 | -45.39117 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 188a53b1-0b1f-3e4e-9c00-07d588c2cb58 | -3.1027 | -49.44674 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c528c650-f16f-35d7-879d-3be1d53a8652 | -3.80521 | -49.2939 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e4554c9a-f187-3ba3-90bf-8152a13fdcce | -4.45467 | -45.46031 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e5cfef2-c5ed-30a0-8c1f-99ef82612558 | -4.45053 | -43.41465 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 068ac723-e415-3f59-8608-6f7e03b22f38 | -6.53792 | -41.61911 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10b6cce4-143c-3054-8f7b-2811951304ae | -6.2332 | -42.5568 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cca025bb-5e16-3f4b-bd00-ecbf0e7bb858 | -4.39391 | -43.32491 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 39d41b10-560d-3eb2-899d-f4c2952d6c2b | -7.24547 | -46.95917 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bbd9a968-0e65-3548-b15c-c46be1610f3d | -6.83797 | -44.00069 | 2025-10-27 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02a1bf82-8f09-39de-9a6a-8fdc17d06d01 | -7.34353 | -48.48802 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0437887d-5322-3212-8b58-d2b109642852 | -7.8285 | -46.48209 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74061851-9b2c-36db-b527-e7faa2690932 | -5.57189 | -46.4329 | 2025-10-27 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1393cb88-9ad4-301c-ad18-afc9147ebfec | -6.43059 | -42.02678 | 2025-10-27 04:32:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f5f797cc-b342-3305-a92e-5c58569410b4 | -6.88294 | -43.57035 | 2025-10-27 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c20e7ef8-4000-3835-8de6-f488ad4ddb8f | -8.6634 | -44.75471 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b60fcaf-977d-3b23-8bfd-1f0b2a697d5b | -4.45227 | -43.42871 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eccb0f5a-c9c5-3947-a5a0-55cf89b3d747 | -5.6399 | -47.63275 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0f61008-57ce-30f4-8456-0fb5a52a0273 | -4.76395 | -46.4225 | 2025-10-27 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b521e3cc-4960-364e-8739-edde88f177ed | -3.84803 | -51.38231 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35e8e04c-bfe2-3df8-8164-56dea3661b3a | -7.78572 | -45.37314 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b105d984-46b2-385e-85ec-cdbc6f07e694 | -6.64137 | -44.63221 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 559ee7b1-90e2-3cb1-a532-e37b5b9721c6 | -4.45749 | -45.46457 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa66f08e-b0c7-3805-abd6-8e569d59596a | -3.54378 | -51.09748 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8187855-cd9c-3c47-b313-9fe6bca8f74d | -6.22051 | -42.5299 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8ba8e657-65ab-3dd2-938b-1b7fdc2ecf45 | -8.74061 | -49.61264 | 2025-10-27 04:32:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e07e105-c51f-3330-a86e-01403e6c0c2e | -7.65582 | -46.89928 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82328a0b-f20b-3e36-ae74-4187294da1d9 | -7.85762 | -46.40456 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85ebc7f7-b25b-3000-baa4-fc41cdf0b53a | -2.88209 | -44.38016 | 2025-10-27 04:32:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e550c8e5-5bf2-303c-8617-ecc60b1fdb8a | -7.0436 | -41.64275 | 2025-10-27 04:32:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 78cb30fa-4f11-35dd-92b2-49167d4ac29d | -6.37505 | -44.26535 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1655366-0330-3d23-b7d1-a72b98b09dbb | -4.22475 | -48.36433 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee1394ab-2738-3e18-a8b2-643a2b4af12d | -6.88798 | -45.15243 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09a4ad0b-08a6-318d-bf52-fdbcd3900e07 | -8.65046 | -44.76627 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02d3614c-fbcb-35ae-a4d0-e83aac76ef67 | -3.75305 | -51.75423 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1966277-7217-36a5-a47d-2a0efb53e87d | -4.42812 | -45.97736 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75c4d78b-2b58-3ac0-b987-fe38da8c6e9b | -7.99355 | -46.20267 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed995c31-372e-3fc7-975f-fa093ac423b6 | -7.03864 | -41.64626 | 2025-10-27 04:32:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f958f396-cc78-39ce-8ece-7c9e38b047ba | -6.37872 | -44.26581 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a78d61d-8a8a-3a78-8594-67f730ac601e | -6.14996 | -43.12859 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c4b0efd6-31bd-3681-921d-b7b1cb227049 | -5.96946 | -42.76971 | 2025-10-27 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5979c6a-41b9-3bae-8853-7f7dacf768d0 | -4.86946 | -43.25478 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d45645b5-da75-3fb8-8deb-c9e09fc3e114 | -7.24389 | -44.98047 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README30.md)
