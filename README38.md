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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fe4f51b-67c0-370e-8a1b-76ef3616679d | -5.12729 | -41.69009 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e5e527d8-d013-3227-96b5-6dec2eaa1137 | -5.12497 | -41.68166 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e326dc92-c3f1-3f72-9019-c295ab03ee4c | -5.12437 | -41.68562 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c445d0b8-51b4-32c1-803e-5148aab9e4b4 | -5.12369 | -41.71382 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 927427b9-2df2-319d-bb5f-809c492a56e3 | -5.1231 | -41.71775 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 56fd5a3a-c7d8-38d9-97df-fb5d01bf047b | -5.12257 | -41.69751 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c8c0dcb6-f7fb-38ee-81a6-94f6dcfeaf22 | -5.12204 | -41.67717 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f6a1adfb-13ff-3c7e-8138-7115b918ae48 | -5.12197 | -41.70147 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5fbc8796-36b5-3647-bf06-1d1a92ccbffc | -5.12144 | -41.68115 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0754accc-8782-3592-ba7b-d18f47c37516 | -5.12077 | -41.70935 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c9bfa8a6-086b-35f3-a0cb-32da698468eb | -5.12017 | -41.71328 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8976127d-e4be-346e-bfa9-bb390768b776 | -5.11964 | -41.69303 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34141617-7aaf-31cb-af48-cc47d3abe845 | -5.11958 | -41.71721 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e89314dc-5328-3d11-87ea-e01c3383d8aa | -5.11852 | -41.67665 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7ee4dff3-0190-3265-9eff-c86f7f492260 | -5.11845 | -41.70092 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b4bb6e6-fe87-367e-a4ea-f2fe9592dec5 | -7.33577 | -41.18834 | 2024-10-14 04:19:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4953a43-bf66-32ed-970c-3c652cf4a962 | -7.05062 | -42.09487 | 2024-10-14 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8edf9b62-0dbe-3626-94ee-58d2ea563351 | -7.04709 | -42.09436 | 2024-10-14 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fe795dbd-4641-3c1a-978d-5c91ab393a5d | -6.98945 | -41.99704 | 2024-10-14 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76d95207-7cff-38cd-9e15-021cb84652dd | -6.78576 | -41.09591 | 2024-10-14 04:19:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ed8226a-6e68-3c8e-813c-5b37e38ce138 | -6.61506 | -41.57907 | 2024-10-14 04:19:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 546640f5-ae5f-3b56-8fe4-4435f3ef1774 | -6.61146 | -41.57854 | 2024-10-14 04:19:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 311f99b7-258b-328f-9e49-56181430ed9d | -6.61083 | -41.58269 | 2024-10-14 04:19:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcb33391-bf9c-3104-97b2-87d3560dc898 | -8.58072 | -41.32552 | 2024-10-14 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe9b9ffd-a571-3e18-a165-5177d4badda5 | -8.50426 | -41.40587 | 2024-10-14 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 21a48c07-55b6-39b7-8a65-5cfc303c5a77 | -8.50054 | -41.40528 | 2024-10-14 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77860c6d-a3a8-34f2-97e5-2b9c0fd94fdd | -8.34944 | -40.97535 | 2024-10-14 04:19:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9d56a4dd-0bcc-3ad1-9bba-d10085330bb9 | -8.14541 | -42.32815 | 2024-10-14 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| dabe1d75-dc19-309d-be41-bdc11442cdc6 | -8.14483 | -42.33212 | 2024-10-14 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a975deae-38cc-3100-87c6-7428cdbcf2de | -8.14188 | -42.32763 | 2024-10-14 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 17d444c7-6046-3147-85e2-ac2471d39666 | -8.14071 | -42.33555 | 2024-10-14 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e62ead7f-56a3-3cd1-9d29-cbb10495f3a7 | -8.14007 | -42.33681 | 2024-10-14 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a30dd13e-7b60-378c-990a-73f9b1ca9579 | -8.13718 | -42.33502 | 2024-10-14 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 808323c4-a325-345a-8250-d47fde1ed340 | -3.62259 | -41.50766 | 2024-10-14 04:19:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d2c7a4d9-ce29-3b57-a87d-69e7b34ed403 | -3.62141 | -41.51545 | 2024-10-14 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| daed90f9-d2bc-3059-864e-2694accbffe4 | -3.35804 | -42.10976 | 2024-10-14 04:19:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e595fef-2af7-3794-b8f0-13d5005eeda8 | -3.10269 | -41.85529 | 2024-10-14 04:19:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4f808066-28bf-3ec8-9c67-3858f53bac8f | -3.10212 | -41.85902 | 2024-10-14 04:19:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ef1aaf9-9373-34b9-9b3c-0ac2b49fc469 | -3.3117 | -42.84246 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81c39941-d34b-3608-9c82-9a6ac372f10c | -3.31115 | -42.84598 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bf07cd56-21cf-347f-9926-8cbd3f584bd5 | -3.30945 | -42.8349 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 62bc35af-f7d8-3717-9c69-ccb4a106bb4e | -3.30891 | -42.83842 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0fe68141-23cf-341b-a681-3c827126a481 | -3.30836 | -42.84195 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| fc9d63df-3678-374f-a875-81361a088f60 | -3.30781 | -42.84547 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 43b37f6a-abe4-3780-8405-2d233761024f | -3.30666 | -42.83086 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4025bf1d-094a-30c8-ad05-fc95016509bb | -3.30611 | -42.83438 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a3664ecc-cbcd-3d19-8027-7741cbd3bd95 | -3.30557 | -42.8379 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a1559273-8dc8-345b-a939-39e80c02016c | -3.30502 | -42.84143 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 097c074e-7ae4-31b7-8932-b55fdafae31c | -3.30447 | -42.84495 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 42c737b1-c779-3b3c-a5dc-bb0d1a248877 | -3.30393 | -42.84847 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5179efb4-ec66-3586-9961-403f582d280c | -3.30332 | -42.83035 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ef7ba5f4-41f1-32da-b25a-07a65670e38b | -3.30278 | -42.83387 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 36ecd4c6-e804-3926-bc46-6a6d36072ff8 | -3.30223 | -42.83739 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ac9d50e8-39da-3c5d-a647-bcab0f6aec87 | -3.30168 | -42.84091 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f124f968-a0bd-3866-a887-66ea97c825bd | -3.30114 | -42.84444 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 68f8f26c-be1d-356e-a47f-d598e1889f76 | -3.30059 | -42.84795 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| b40dae99-e320-3eb2-b3ff-e04d7d64825d | -3.29944 | -42.83335 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d5547e5b-4024-390d-a305-977f0c79be64 | -3.29889 | -42.83688 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 37d80b23-08e4-3f86-ae40-28d047dd7dac | -3.29835 | -42.8404 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4ade3e77-ced8-3b14-8f01-32abf8f32a60 | -3.2978 | -42.84392 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8b51c55c-40d6-357c-8cf4-7d82fd063e76 | -3.29725 | -42.84744 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 2b53776f-4dca-3230-a559-be7cabab2a9f | -3.2961 | -42.83284 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470ffc70-f96b-30a6-927f-dce288288dac | -3.29555 | -42.83636 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c7361cac-f409-3cbc-84be-abdbff196538 | -3.29501 | -42.83989 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 2506f6c1-2acc-3808-9a7f-0e9f87667e6a | -3.29446 | -42.84341 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dd36439-0d05-3ea2-b327-4629d7900a0d | -3.29167 | -42.83937 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 18f74e25-ac62-3f51-829c-5dd922e59bb7 | -3.29112 | -42.8429 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d756249d-91a6-3242-8ca5-32b6f005e1cb | -4.09148 | -42.29247 | 2024-10-14 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c2bb655f-4048-3ec3-9865-39b0752bf52a | -4.08865 | -42.28825 | 2024-10-14 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 206fd90f-cce5-3670-9eae-672545f96852 | -4.06934 | -42.30038 | 2024-10-14 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b186925-cbff-3eed-a371-25b692aa0d04 | -4.96813 | -41.81077 | 2024-10-14 04:19:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac867e4b-96cd-3c45-ac84-b52c4d8c6d76 | -4.96755 | -41.81467 | 2024-10-14 04:19:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c33428ed-d0ad-35e6-99a1-a3b1c44474fd | -4.96522 | -41.80634 | 2024-10-14 04:19:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 05d0ac10-7eca-3ba5-a562-d468176faf4e | -4.95017 | -41.82509 | 2024-10-14 04:19:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5c330440-c35b-381a-a898-50ab63bf017f | -6.35218 | -42.81324 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7160ed2f-cdc3-30f7-85df-ec80292bfc90 | -6.34878 | -42.81269 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e17e67d2-97c5-381e-9303-a63906e2bed0 | -6.34482 | -42.81578 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ff85607-d678-3244-be13-11d3c6450fda | -6.28821 | -42.61045 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ece111e-4edf-3254-a5e5-2725ea7f1de9 | -6.28765 | -42.61419 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7015598a-6112-38d4-8312-31b94c9bb415 | -6.25992 | -42.4988 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af357cf1-c3a3-3072-b421-068fd6f76b7f | -6.25649 | -42.49824 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6d871f9d-591f-3f0a-ba92-a67133a1b5ec | -6.25591 | -42.50201 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6547bb6f-e772-3f14-9254-a1884e047b6f | -6.23914 | -42.6106 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55cd4140-431b-3219-bf4c-4d3a91e9957d | -6.23571 | -42.61009 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0ecf59ec-1c68-3c2c-a85e-47f858195f10 | -6.23352 | -42.51023 | 2024-10-14 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 36abd8bf-da69-348f-be6e-963e668a82c7 | -6.17688 | -42.58194 | 2024-10-14 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6e619c8c-ede6-3297-81d0-998d8155b844 | -6.17345 | -42.58144 | 2024-10-14 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a00ba43a-38f2-3ea5-ae06-72285c758d29 | -6.17002 | -42.58092 | 2024-10-14 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5741ea1e-d1d6-3919-a38d-20d75b157832 | -6.15342 | -43.00782 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 133a51e1-aafa-3e78-9182-6934bfa6ac3f | -6.13957 | -42.78124 | 2024-10-14 04:19:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5cdccf76-9e43-3f58-b45d-a383dd4f55a1 | -6.13616 | -42.78072 | 2024-10-14 04:19:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45812bbf-7d91-373f-925a-22e3ef0dce16 | -6.13561 | -42.78439 | 2024-10-14 04:19:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a81ce81-5f58-39d0-81fb-4226bbedfa06 | -6.13276 | -42.78019 | 2024-10-14 04:19:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9ce270d-845d-33a0-b542-1aab866e50e6 | -6.13164 | -42.78755 | 2024-10-14 04:19:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4d578b9-282a-365b-b386-17a2473028b6 | -6.12824 | -42.78704 | 2024-10-14 04:19:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5cf81632-6571-3e2a-8b4e-b641744c21c8 | -6.37162 | -42.98148 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dc70d70-f797-33c4-a0bd-59421da30309 | -6.08817 | -42.40334 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a2720875-90d4-3009-93bf-5d1c34c8528d | -6.08415 | -42.40659 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bc45a07e-134f-357a-ae9a-18b8c9b60856 | -6.07782 | -42.40176 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8429936-aa9c-327e-9bde-d18ee6de2613 | -6.07381 | -42.405 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
