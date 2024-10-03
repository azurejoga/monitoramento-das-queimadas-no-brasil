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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47299d2-c3b5-31cc-894a-1abcfcdb1854 | -4.53984 | -43.31712 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f17792ba-a47d-3ec1-92bb-321fd345daa3 | -4.53977 | -43.30903 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ed0fea99-8a54-3bdf-9005-9fbcdb89bc0c | -4.53842 | -43.31707 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6205e50d-2112-33c2-a89e-9841a298602a | -4.53624 | -43.30411 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a5303f5-b4fe-36c4-9a2e-aaba50053c46 | -4.53554 | -43.30811 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 69b6ace4-1146-3032-8d0f-fa16b61e6489 | -4.53483 | -43.31213 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 087b179d-ed19-35f1-9287-23292b2c5b7a | -4.53412 | -43.31614 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 594e96f5-db20-34fb-b0de-ed0b8131b1e5 | -4.53405 | -43.30804 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 05b3f026-8f78-38b8-a89c-3a7d836f491c | -4.53337 | -43.31208 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 304c4643-229d-372b-8298-b536c7d6951b | -4.53269 | -43.3161 | 2024-10-03 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 787e96ed-4bb8-3d4f-82ae-4aeaa1ad455a | -4.48861 | -42.87334 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 776a3e84-11cc-32f2-9b06-111013f31b0e | -4.48799 | -42.87701 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 23fcb637-8f02-3989-b633-cb2ed0251a28 | -4.4874 | -42.91445 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 924705f3-4e54-3f5a-994f-7e74e34fc4a3 | -4.48675 | -42.88436 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3aa19cf9-ffc1-3144-b530-2955aab9b46a | -4.48304 | -42.87238 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d90b65f5-63ed-396e-b52a-0786c1e2c88f | -4.48302 | -42.90638 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8e223dd-3843-3f03-adf6-4f144ae805a6 | -4.48243 | -42.90989 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c26e931-a640-37f3-a0e0-1cf12af2455a | -4.48242 | -42.87608 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 25f54e8e-906b-3653-8e7c-0f96488b7777 | -4.48183 | -42.91345 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97249f5a-29dd-3ad0-8837-95f098ab44e1 | -4.48179 | -42.87978 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| a6ca9a2e-040f-31d8-a8c5-9aad7fc98f45 | -4.48121 | -42.9171 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 967dd319-0095-35d1-aff2-2e8d6de95d53 | -4.48117 | -42.88343 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1e7495dc-5b5f-3459-8439-d033646ad39f | -4.48058 | -42.9208 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 252239e2-3b1b-35bc-9121-b341ab2c1a54 | -4.48055 | -42.88709 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e7442f93-be2f-3949-af27-1b6352db317f | -4.47684 | -42.90895 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4e40a51-4af6-3516-bde7-bd813dde6a48 | -4.47624 | -42.91253 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40c06635-b72c-3fc3-a0fb-208fbb22e5b8 | -4.47622 | -42.87884 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8a74ac2d-cc8f-3a79-ae06-0158c9638d89 | -4.47562 | -42.91619 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2217ab7-18d0-30f4-aa3d-615791a7378f | -4.47559 | -42.8825 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2f1b61d6-63b4-3849-965f-5cc64719704f | -4.475 | -42.91985 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b57be0c9-ee39-3088-9bb1-b2152756a8c9 | -4.47498 | -42.88612 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5fe6be84-7ca4-3b1a-ba2c-23a4df1f17f4 | -4.47063 | -42.91172 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e327434a-2632-319b-a9f4-42d12790e947 | -4.46878 | -42.88883 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd376b76-4d34-30ae-b277-cd775be80a69 | -4.05543 | -38.30481 | 2024-10-03 03:34:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ebbda85a-b3ae-375e-917b-e0181fdc5f8a | -4.02176 | -43.23956 | 2024-10-03 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c7e94ec-9f04-371f-a063-b75b11fff5c8 | -4.02069 | -43.24088 | 2024-10-03 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b71dbfbe-729e-398b-8092-e55c63b9ebdc | -3.94766 | -41.50838 | 2024-10-03 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ff53794d-2d90-3b0f-a2f9-345353ab9529 | -3.94715 | -41.51143 | 2024-10-03 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e0a92fb2-1203-3924-8122-883405fd6218 | -3.94664 | -41.5145 | 2024-10-03 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| deb85351-fbd7-3b01-9eda-e03d84fb315d | -3.94612 | -41.51757 | 2024-10-03 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 01cfdd49-7a65-3176-88e5-b928a39c55dd | -3.94561 | -41.52066 | 2024-10-03 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6f19bf86-d81e-371f-b4f4-84d19a4e1c88 | -3.73173 | -38.72368 | 2024-10-03 03:34:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5dc9fbf9-304b-3f96-a769-c21f0bdfbcb5 | -3.46979 | -43.36111 | 2024-10-03 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46670e0e-c0e9-3d17-bb24-db4a19699365 | -3.41625 | -42.28173 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2230f3b7-7b3d-3d5a-8302-8b03c57ef64a | -3.41566 | -42.28526 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b1f72fd-aeb5-3447-9629-2264dd888723 | -3.41509 | -42.28878 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab88939b-6974-3129-ac92-af939f4945ef | -3.4125 | -42.2705 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45bb7c7a-4e0b-3539-a041-7388859ab7ee | -3.41193 | -42.27393 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afcad264-9d97-3f1b-946d-3391137e9796 | -3.41138 | -42.2773 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48070238-6784-33f8-9490-c48dbfe3f059 | -3.41081 | -42.28072 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09e83cab-0e51-3a62-977c-c94a35b48772 | -3.4107 | -42.32121 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1436329-6c94-36a2-96c9-c00b4dbde338 | -3.41044 | -42.31702 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c53703e-aa7c-3a17-bf67-4e8fe07b50a3 | -3.41023 | -42.28424 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41f64301-cb27-34e0-a07e-a236a8487ce6 | -3.41009 | -42.32475 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec69da93-c956-3890-87f0-b82052479e1f | -3.40986 | -42.32053 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f0e7f52-b4b2-3fc8-b418-02e5bbc5b82d | -3.40966 | -42.28773 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45d2110e-2eaa-33c1-8064-6464e49159ff | -3.40948 | -42.32831 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cce01e3-ac74-33a1-9fee-4d76c55fdbde | -7.29228 | -42.26268 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 224c00d1-3977-3fae-9a38-7a7139e2d8fa | -7.19719 | -44.16144 | 2024-10-03 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 38b95703-176a-3274-b4db-47fb9735a758 | -7.19701 | -44.16177 | 2024-10-03 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e72c3029-2fea-35c5-a401-186c5294ccd9 | -7.1964 | -44.1657 | 2024-10-03 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2844df60-2146-39f8-835d-cb85be207d7c | -7.19626 | -44.16602 | 2024-10-03 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c5ab69d1-36f3-3d66-8f93-e95932dadfac | -7.12434 | -35.13741 | 2024-10-03 03:34:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d0fead75-d965-3a1b-b0ed-c223df93bf27 | -7.07385 | -39.14702 | 2024-10-03 03:34:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3fc136a0-f6fe-3772-ad82-ce5ad40b04d8 | -7.03276 | -42.81804 | 2024-10-03 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7d7f9160-0741-3f9b-b38b-26913befc0a8 | -7.02564 | -42.82715 | 2024-10-03 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a63240e4-34b6-31cd-b312-0042e69c3bd4 | -7.02031 | -42.8263 | 2024-10-03 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c3b45024-a933-33b3-b095-0296c253bff3 | -7.00525 | -42.57856 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a6686a5-5a32-3952-81f8-3200e75144bc | -7.0047 | -42.58166 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e5d4e631-9cc6-3d83-a84e-ef71e9cce1fb | -6.87948 | -43.60692 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47f307c1-f846-3f58-a9e4-406e65ea5f36 | -6.87877 | -43.61084 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daeec9d8-2962-3d8c-8fbc-d470592c3d2f | -6.87807 | -43.61473 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4148f799-9abc-35c0-bd35-eaf53d2b2763 | -6.87386 | -43.60597 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 925651f9-0f8a-3cbe-a095-f19fcdcb4342 | -6.87315 | -43.60988 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d47adca6-de0b-3eef-b4b0-07b479494197 | -6.87244 | -43.61377 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0c11f103-20b7-39f8-96da-0592d129c84f | -6.87048 | -43.60542 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 826bcb99-67ee-3d8b-9ac8-b741cf6b006a | -6.8698 | -43.60933 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7032a198-c0b2-341d-b8b7-b199f5d66954 | -6.86912 | -43.61324 | 2024-10-03 03:34:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 880a6b0a-73af-39bd-9bd8-9a45c0ae956e | -6.65785 | -43.13611 | 2024-10-03 03:34:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ecfc04a-1f97-3d30-bd1e-938d7bfdadfd | -6.60907 | -42.99352 | 2024-10-03 03:34:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbef68bc-264b-30b4-b25f-c85d9ddc20cf | -6.60847 | -42.99696 | 2024-10-03 03:34:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9135f1ce-8262-319a-babd-dcff411511be | -6.60786 | -43.00041 | 2024-10-03 03:34:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da64166e-8791-32ce-8621-0a64d4cc9876 | -6.58754 | -35.03017 | 2024-10-03 03:34:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3debfe41-5ac1-355b-9130-d6e8ce2fd917 | -6.30583 | -43.04462 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85b0f6f6-547b-34fc-b2ff-082cb216249d | -6.30419 | -43.43757 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e9d0777-31f8-34b5-b12e-484759d8a35d | -6.30036 | -43.04366 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d240de3-8260-3e76-b85c-dd6db6babb5a | -6.30032 | -43.03918 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bca2c475-6986-3e53-924b-d2610a11b6fa | -6.29971 | -43.04727 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30af62cf-db3a-322f-ba00-48190c11c47d | -6.29859 | -43.43654 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f25be57-99bf-3b64-b533-ad6990026db7 | -6.29791 | -43.44038 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45d05bcc-647b-35c1-a885-21978053effd | -6.29723 | -43.44422 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fadd0d2d-159d-3d65-afda-968876989383 | -6.29621 | -43.0304 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da9168db-51d9-341a-8a34-feb42d1cdd46 | -6.29555 | -43.03424 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6365d6cb-a1f1-3f40-8851-580c65a117ba | -6.29489 | -43.03805 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72c1b2d9-931f-343e-b553-8244bf2106c8 | -6.29425 | -43.04174 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd56ee5a-9dc8-316e-a0be-b3f82a74e3f0 | -5.31523 | -42.97096 | 2024-10-03 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4842a127-7dea-3471-9dcf-340dc676f5c3 | -6.29297 | -43.43561 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a7e997-b4c8-3e40-8549-a120fe17109a | -6.29229 | -43.43947 | 2024-10-03 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80e04215-f7bd-37e6-b85d-cbd40bf30b36 | -6.29077 | -43.02935 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bc5eeb4-5c93-3245-913e-0e6e031b3e47 | -6.21309 | -38.52344 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README64.md)
