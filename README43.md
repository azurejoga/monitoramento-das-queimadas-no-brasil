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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65ce7c68-690a-3f20-92be-84f5f2e942e5 | -4.66208 | -46.73792 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dad677af-6c70-3396-8d00-33a5c64f5310 | -3.65345 | -50.2248 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46eb595a-d775-3eef-8a1d-1c44cc7422a8 | -3.64942 | -50.22418 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc184c5-8933-3d8e-8f88-2414167d13b8 | -4.74313 | -46.39655 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 028c1edb-e47a-315a-bcd9-f151f5afc1fd | -2.93816 | -51.07214 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ce92486-68ae-39bf-a8ec-32b489742e5a | -3.81216 | -51.17627 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5111c24b-c679-3b3a-b478-a8e57c808bbd | -3.466 | -50.12158 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdacc4aa-a2fc-3032-8722-eb02405a830b | -7.25538 | -48.0131 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2aa5b30-913f-372a-bf3d-5fe5d1707a3b | -3.75221 | -51.81552 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6001261d-b667-3810-8c83-b64efe691150 | -6.48218 | -47.18817 | 2025-11-17 05:08:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abbdd439-81a4-3625-a4cb-1dc9a0c61c04 | -8.11391 | -43.52648 | 2025-11-17 05:08:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 188e201d-3a95-312a-99c3-957bb439172b | -6.71829 | -42.93684 | 2025-11-17 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f8b92d74-13b4-30f6-b906-0eb4bdc46eae | -3.47827 | -50.25537 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f3dab09-dba1-3d3b-9c14-5125f43f1d56 | -11.0578 | -45.15623 | 2025-11-17 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4122a250-a43f-3b7d-bf79-e5444a24ff86 | -3.79526 | -51.15944 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ab2a843-5096-3ec5-8d7a-0b8a2c4f61e7 | -4.02813 | -48.99196 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88463978-a945-3d10-9a7c-055cb41b6236 | -10.85253 | -46.7525 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6e646ae-3f1d-39e1-b6db-6a589c7fcefd | -2.89159 | -53.28339 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| add420f6-2aa9-341b-8b49-8b43a08a2898 | -4.73968 | -46.38274 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae11961-b8ea-3bc5-95e0-620e9a8084df | -3.5903 | -50.71708 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bdb4169-836d-3a9a-9bff-0c8c800b72ef | -3.7826 | -50.97282 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37e422d6-4c76-3e5e-a6f3-b5e33398beeb | -7.94974 | -46.84381 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eb204a5-6e9b-386e-9155-6a96c49d773b | -3.36029 | -50.18704 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| faabe954-0fe3-341f-b164-5f4c33dff3e7 | -3.91458 | -45.79945 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4f9ec564-8097-3dd6-ad41-800f9397f711 | -3.28643 | -53.82006 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee657d4a-c6d0-35e2-883f-f136698f26f9 | -3.23193 | -50.50311 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a37ce3e4-7404-3761-82f8-3af04adab5f0 | -3.22878 | -50.49754 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 204d6b02-e2ce-3e82-b8a3-35724b5ef213 | -3.53148 | -49.10278 | 2025-11-17 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f39b70f-8828-38cc-bda4-10e36af3e094 | -2.89384 | -53.29122 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a11a3ab6-da95-3871-a241-c98e16db463c | -8.88347 | -44.78444 | 2025-11-17 05:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 424f8ee9-1f2e-31f8-8a77-1657f4489ebc | -6.13323 | -41.81472 | 2025-11-17 05:08:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c96e43f-2aee-3533-b58f-27e6fb93e6a8 | -7.1273 | -47.11987 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6cec56da-ca2d-31fe-9062-f462cf8b3048 | -3.32849 | -50.28718 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18f72f74-3782-3881-ac73-71762859a246 | -7.21905 | -47.98478 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc694ab8-c909-3e5b-aaac-c8bc4c26be4d | -9.06361 | -44.79531 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14eb4bd4-b32c-3704-8a3e-06e3f931192a | -4.99515 | -44.363 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2fe641e3-d941-3c43-a700-c471ea215b7f | -6.67767 | -42.04245 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 77dd8870-5294-3343-9b68-72c73d2eb9df | -4.01555 | -48.81001 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff31e11c-10a4-3426-94ac-e522463354fd | -3.47701 | -49.68812 | 2025-11-17 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4f47126c-0eeb-3720-b0c1-823701898bc1 | -9.51312 | -47.26971 | 2025-11-17 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57fa3b3d-bf3a-3eef-955c-d44ef653a66a | -3.46708 | -50.11453 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf5a1e14-86fd-3dbe-a23b-61f641db8396 | -3.39549 | -50.17883 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50b34197-39b3-3ccd-bf03-322ebc1ac610 | -3.18939 | -50.64735 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b5db77d-41ac-3936-be4b-8003c0b53702 | -3.14599 | -51.32304 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4d5ed77-d51a-3f7e-b248-9040b26be09b | -3.32928 | -50.28207 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40c1a52e-56e3-3e79-810e-fc7e2392f0e0 | -3.81128 | -47.49703 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe1c7de8-c461-3ec1-81c5-ffbc9b5a40e4 | -4.54772 | -48.47709 | 2025-11-17 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4ec4a87-87f6-319e-a4f3-f7f977274de3 | -3.7734 | -47.74259 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f920781-af72-3886-a5df-fda052bd28c3 | -2.88457 | -53.97168 | 2025-11-17 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1987216-bf28-3ce9-858d-49792e2ce2fb | -3.35629 | -50.18635 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9908166a-a4cc-3ec6-a00c-982384e4e813 | -3.60184 | -50.1526 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db25197b-e76b-3ddd-a95a-b17efbc402b6 | -6.6858 | -42.03633 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 445e7e66-ee7e-34bc-91c7-e1733774eb18 | -11.40199 | -43.33047 | 2025-11-17 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b68b320-0ed0-36bb-a413-681263042476 | -2.88512 | -53.96816 | 2025-11-17 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f078ef8f-da8d-3130-a44b-a4333fd6e6b0 | -2.86914 | -51.47323 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33a1c320-bb38-306f-90c6-cc4739b37784 | -4.72945 | -46.37819 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a6a045b-7a88-3cf6-9af2-d28ce5cd0c25 | -6.21932 | -47.23961 | 2025-11-17 05:08:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85b7bd1d-3260-353b-8c0a-ddc8cd569956 | -9.71897 | -43.95351 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a8b14fc-5e2c-3e79-a5af-54fd684621b8 | -3.58294 | -50.42096 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c3309ed-e679-377f-8090-0a8745fa1644 | -6.67456 | -42.03292 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 02857bb4-bd8a-34f2-b552-adafcb8ba286 | -2.88818 | -53.28286 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2bc9e31-1517-33ea-969b-761fab0309fb | -5.3369 | -43.03502 | 2025-11-17 05:08:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 433f7895-a3ed-3aca-a34e-df3c2df4d942 | -5.88514 | -46.44564 | 2025-11-17 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a483267-ff48-3b28-b975-f9debcaf11e7 | -8.68488 | -51.29241 | 2025-11-17 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2e34bd-6c5d-36e9-895a-56faf7dca8cc | -3.39899 | -50.18293 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cc0d671-5f28-3fa2-a358-802f8a1df6f7 | -3.86374 | -49.98311 | 2025-11-17 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98938cbb-7d88-38bb-a1d1-f16d4a342ba0 | -4.24037 | -49.67678 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8fcd1fa-bc3a-3158-9840-271b286cbfd4 | -9.63436 | -47.89251 | 2025-11-17 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deea13b6-867e-3350-8ae6-c509343ffafc | -4.64768 | -50.41708 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dffdcdb-8d0b-3401-9c2a-f6cda09fa229 | -4.93994 | -44.53077 | 2025-11-17 05:08:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18f0a674-3314-363a-93d9-ab98fbe1ad1e | -8.8306 | -47.36157 | 2025-11-17 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35241ccd-b6cb-30b9-b5c2-2539a7aef310 | -3.60136 | -55.5393 | 2025-11-17 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c16d00b1-b027-3a18-ac99-d73bcbac50c0 | -11.15909 | -44.03657 | 2025-11-17 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0c594efa-9393-3be2-a9e1-fc5182414708 | -4.68718 | -46.31142 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8de1be92-5561-37dc-a9c1-2fe87efbe726 | -4.2135 | -49.13192 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6a5bac2-439c-3022-bbde-0eadb68439a9 | -4.57101 | -50.94198 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e748892-7f11-3c9d-8e37-cdf43ea60b9e | -5.88562 | -46.44236 | 2025-11-17 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 844cce63-1e13-370e-9925-70e73d8b6015 | -7.9715 | -50.00625 | 2025-11-17 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b507f97a-dee7-39a7-94ef-86ec845be0ad | -6.48174 | -47.19124 | 2025-11-17 05:08:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 532fc9cd-b36d-3c56-bb01-feb8da1b109b | -3.55967 | -49.88214 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 731f8819-1227-3f86-8601-85d152402332 | -10.55879 | -44.81961 | 2025-11-17 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fd70525-cf71-3879-841f-4d0a218dca49 | -3.5864 | -50.7165 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c1a3625-dfbe-35a6-903b-4f53bea6e252 | -3.59809 | -50.71828 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85d4e705-4b2b-3966-9778-8627760058ff | -6.04329 | -49.12954 | 2025-11-17 05:08:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8527b7-0077-3945-b5a7-551ae1b8f169 | -5.35932 | -44.86449 | 2025-11-17 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 593c3901-3994-3283-a1a3-8b1857b69c73 | -3.47188 | -50.24372 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c1bbc6-de10-3889-b758-690810cc0c90 | -6.35947 | -46.15159 | 2025-11-17 05:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eea9133d-dfd9-3350-80d4-108103aab0de | -3.80129 | -51.0934 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2980b488-4d82-3794-8e4f-a0112c6f1a11 | -3.77765 | -50.14225 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e34473b4-ee8c-3d24-a900-9fbf19ce7dae | -3.4625 | -50.11742 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46015f26-53eb-3244-b1ae-5612a675f408 | -9.4749 | -48.74613 | 2025-11-17 05:08:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de7b5dea-0205-3af4-91e8-eaf6f6098820 | -3.29963 | -50.07075 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36204d9b-b623-3e81-88b0-5bdcb53e4ba3 | -3.24254 | -50.50648 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1df6e05d-a5dd-378a-859b-b8012b9b405a | -3.41193 | -50.12394 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a34ad365-aca4-3b96-952e-a408507f3c2a | -4.93869 | -44.53947 | 2025-11-17 05:08:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b131c7-dadb-317a-86fc-33e410453d25 | -3.30636 | -50.21766 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ce4f14d-243b-3505-8e35-04f1dd142c50 | -3.23225 | -50.49467 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7e9d2f4d-f457-36fc-8353-67ecc8816e38 | -3.55791 | -54.57313 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bce02c1b-4e84-3253-bc78-aa823d152a26 | -3.39527 | -53.39007 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b43d55bd-eddc-3cf8-be9c-ee0ae37f1b02 | -5.88525 | -43.97577 | 2025-11-17 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README44.md)
