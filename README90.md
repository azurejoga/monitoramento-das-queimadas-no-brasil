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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20a3c154-6129-370b-b0cf-02898cd8064f | -4.02403 | -57.86793 | 2024-10-29 05:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 636b4544-46ef-3063-a0a9-92cf22228f47 | -3.81317 | -56.94986 | 2024-10-29 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4adb6082-efbf-3c5f-b5f1-198f60f4651c | -3.5641 | -58.69497 | 2024-10-29 05:01:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3147c607-6c3a-3778-81c2-3e852a4d745e | -3.56038 | -58.69439 | 2024-10-29 05:01:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 178710a2-cb90-3189-9a1a-575ff8a58c43 | -3.55134 | -58.67939 | 2024-10-29 05:01:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3043c17-3d49-341d-8d9a-670d19375c25 | -3.55063 | -58.68379 | 2024-10-29 05:01:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a06e47d-ed19-370a-8b86-1abacf7a0fa8 | -3.54762 | -58.6788 | 2024-10-29 05:01:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 957f9396-7ad5-33a3-8c5a-a023ef42944c | -3.43595 | -59.25151 | 2024-10-29 05:01:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0729d87-d172-31e9-bae5-37ddc4b4be4f | -3.43518 | -59.25627 | 2024-10-29 05:01:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9669a74a-d068-3fbe-b7a4-4f31b83f09e9 | -3.11968 | -59.42662 | 2024-10-29 05:01:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25354808-7c37-3ed0-a024-5cff8e672387 | -3.85238 | -58.82621 | 2024-10-29 05:01:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2447e6c-9777-3920-a691-c45e5cd83754 | -3.85167 | -58.83069 | 2024-10-29 05:01:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41de9d63-bf4c-385a-afe7-31645c110bdf | -3.74101 | -59.44487 | 2024-10-29 05:01:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f739e246-b567-30d4-a7ce-12578c0a9855 | -3.7076 | -59.67622 | 2024-10-29 05:01:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb02fc5d-7876-3f90-9597-72c26d074d0f | 0.76369 | -59.505 | 2024-10-29 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac9d8688-ff78-306a-86fa-bc2407a88557 | -1.71726 | -60.13025 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de469ca1-631d-385d-9c5e-0ca729e2f87f | -1.71665 | -60.1341 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7efafcb4-e6b7-3c06-9e92-913fdecf1c5b | -1.62184 | -60.07713 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 818f94c5-f84f-33c1-b4c5-904d23fd3912 | -1.62125 | -60.08088 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13cef7db-537f-35d0-b291-00e8fbfc91f7 | -1.42917 | -60.28744 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a330fa0a-f174-3149-a2e4-612ad30e2c56 | -1.42556 | -60.28283 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aac746dd-8a28-3138-b5d6-11ef8ad60da7 | -1.42493 | -60.28673 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8659be3c-9f47-39e7-bacf-0e091fcb5d50 | -1.4243 | -60.29067 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e4ea5f5-fa21-3ac7-8055-bdd3d29633a7 | -1.42132 | -60.28216 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14add257-1ecb-3c57-85a3-b94e4858e089 | -1.3009 | -60.22374 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3f43e20-65e9-3967-8089-fc9aec533204 | -1.30027 | -60.22764 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e03382b-d4c3-35b3-845a-e31c5c8d859a | -3.42481 | -59.96177 | 2024-10-29 05:01:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a151827-37a8-3877-9ea6-1fc9a019753e | -3.42078 | -59.96111 | 2024-10-29 05:01:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71f01b00-1a3b-3a65-bb43-c1003b01819b | -0.76354 | -62.89682 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2e1cd60-ac1d-3ac1-8f64-9663b85df720 | -0.76293 | -62.88648 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e90bc5f-1c6e-3a42-a1bd-6f34fc27919f | -0.76152 | -62.89555 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc7056c7-1141-3922-8324-48811b6de78d | -0.76105 | -62.89857 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc7c60f7-9ba9-3d5a-bdda-36dca4ebadaf | -0.75989 | -62.88694 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 929f145e-8e05-38b1-97d3-dce494b4644f | -0.75939 | -62.88997 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56f4112b-f2c4-31de-a408-8334f67b1804 | -0.7589 | -62.89297 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2573bc4d-4025-31a4-8d05-2bc3cab9bdbd | -0.75733 | -62.88867 | 2024-10-29 05:01:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff0d4950-6b12-37f3-9f33-07cd79092b21 | -7.34104 | -43.57555 | 2024-10-29 05:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6d3e637c-a013-36bc-b11f-fd1e9fe367e7 | -7.34031 | -43.58094 | 2024-10-29 05:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5978156c-00eb-38e0-b23c-3f39027acbf6 | -7.33968 | -43.57552 | 2024-10-29 05:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f237aa4a-2c51-3435-bd03-0be2d832cb5b | -7.33899 | -43.58092 | 2024-10-29 05:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0f814d61-bc8e-33a1-b3bb-e245ebabc017 | -11.10314 | -43.33889 | 2024-10-29 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7635ce48-9b2a-360a-88f7-6074d14b1f43 | -7.42441 | -44.79638 | 2024-10-29 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76ae1ffb-e820-3530-a1b8-7d16c95e9077 | -7.41833 | -44.79536 | 2024-10-29 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dd0c087-36a7-39f3-acfa-8bbc305c631e | -7.41166 | -44.79879 | 2024-10-29 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 708bddcc-d9b5-39e3-9f9c-e80c7754ffb6 | -7.41107 | -44.80334 | 2024-10-29 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 588f0495-2d01-3192-887a-31c953241ca8 | -14.15134 | -44.07395 | 2024-10-29 05:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9308fa53-9b98-3428-b094-e84b95f9b3d3 | -14.15067 | -44.08048 | 2024-10-29 05:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 33cc10b2-5829-31eb-8f70-834fabff6145 | -14.14441 | -44.07322 | 2024-10-29 05:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5a91cc7d-a5b4-386c-bbe6-848184173429 | -14.14375 | -44.0797 | 2024-10-29 05:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8e2d13b6-2ade-3a44-bd8d-3f8bc3e43e8a | -14.13683 | -44.07895 | 2024-10-29 05:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d15282bf-eb0a-3629-bd0d-732bdb34a5bb | -13.89124 | -43.97192 | 2024-10-29 05:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c417509b-8876-3210-a7ee-f56360544c64 | -13.89003 | -43.97036 | 2024-10-29 05:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2c3dc86-f393-3996-9dc3-e5a7c05a0f97 | -13.88937 | -43.97696 | 2024-10-29 05:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fbd28d3-d4df-3e12-b459-50a2e5a0da9e | -10.3563 | -44.05535 | 2024-10-29 05:04:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c235228a-5a68-3b7d-a732-4439a1601005 | -10.34966 | -44.0545 | 2024-10-29 05:04:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e8cd5be-db75-3a3d-8e14-a244087957c5 | -12.65965 | -43.82593 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f0a68d4-01c0-3189-8bb0-2c8134181d00 | -12.65965 | -43.8181 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75aa848a-bce5-361b-a9da-a36707af0d89 | -12.65897 | -43.82455 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a02ee2ec-530a-36fe-b79b-35a4f3546504 | -13.22726 | -49.83361 | 2024-10-29 05:04:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc33e8e9-719b-3c3c-b079-86bca7a5d671 | -9.62841 | -67.21554 | 2024-10-29 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e8285b5d-f795-39dc-b605-985508bac8bb | -9.62253 | -67.21438 | 2024-10-29 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28c28fd9-7020-3229-8491-90f64388d55d | -9.60142 | -67.19702 | 2024-10-29 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17752749-67cf-3373-ba86-f764f202bdf7 | -9.6006 | -67.20134 | 2024-10-29 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14df6d5b-8693-3166-bfed-2333df624c1e | -8.76294 | -44.72183 | 2024-10-29 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e34a476-002c-30e6-9d3e-82d729e096aa | -8.75789 | -44.71135 | 2024-10-29 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5340fda5-3e38-34b2-bf11-ca8e73d8ca62 | -8.75729 | -44.71619 | 2024-10-29 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed9c783c-935c-35ad-bcf9-592692d2592e | -8.75453 | -44.7103 | 2024-10-29 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 621925c9-c172-3fc0-927c-239b7a5a400f | -8.7539 | -44.71513 | 2024-10-29 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad45423b-5790-3b87-81c7-fb5dd02c1bd9 | -8.75104 | -44.71537 | 2024-10-29 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d70b9c0-38d2-3794-82d2-67ca4815fc81 | -8.25142 | -44.84604 | 2024-10-29 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| febeb800-207a-35eb-84b4-f6c3aac74c91 | -8.25079 | -44.85099 | 2024-10-29 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1c76f4-103d-3ab1-81a0-fffb136a0cdd | -8.25015 | -44.85596 | 2024-10-29 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd522210-c021-3fd0-928d-41ed271cfdf7 | -12.88944 | -44.6166 | 2024-10-29 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdaba3ae-7d7c-3d39-bb8c-591e7546b7a4 | -12.88457 | -44.61572 | 2024-10-29 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 519412c9-2b4a-3b00-af5e-3ac21a49fca9 | -12.8839 | -44.62158 | 2024-10-29 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53d19de5-19ea-3a14-9861-5d647291a7a4 | -12.8822 | -44.62177 | 2024-10-29 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74768bc1-7a60-3d3f-bb5e-fd4cdbb4a2c1 | -12.87727 | -44.62102 | 2024-10-29 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f671842-94d2-3681-aee8-01b8e20b0086 | -12.87661 | -44.62686 | 2024-10-29 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19b75caa-dbaa-33c7-98ae-788ebc9c2b6f | -12.86938 | -44.63165 | 2024-10-29 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1d30cdb-34bb-3ba4-a237-f535ea4813d7 | -12.66728 | -43.82031 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 76a209d2-2e35-3db3-a469-c33921693875 | -12.66656 | -43.81894 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35ce898a-6c26-38dc-8ccd-fbe4c17fe5f3 | -12.66587 | -43.82541 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efb423f3-4fbd-3544-b3fd-d1359da070c5 | -12.66037 | -43.81949 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c08e7de4-b165-3c7a-b04d-d5cf4d7aaa10 | -12.4394 | -43.73614 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2a63dd4-6ac7-3b46-bde8-a739e6c6dd1b | -12.43838 | -43.73485 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 673bfd0c-aea0-3940-811a-21988c5fa3c0 | -12.43247 | -43.73536 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ef3aabb-c4ed-3e72-a0e8-cf1d7e0fa46e | -12.43145 | -43.73407 | 2024-10-29 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 534dd941-7970-3e18-9ed2-0061350a3832 | -13.8843 | -43.9712 | 2024-10-29 05:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51a65c40-f370-3560-ba8f-97761608dfab | -10.54365 | -45.13836 | 2024-10-29 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88b0445c-41cf-3b2f-8fbe-3f1f35323a1c | -10.51754 | -44.84828 | 2024-10-29 05:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8e959f4-7897-3573-a5ff-9adc15e1e53b | -10.51122 | -44.84742 | 2024-10-29 05:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c56d446-07aa-3bff-b7b5-96c16ba56f38 | -10.45213 | -44.89122 | 2024-10-29 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f096373-704b-3d07-b993-eec57b1208db | -10.45148 | -44.89642 | 2024-10-29 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8e4097f-c35b-3796-9505-d1bb1cb8d24a | -10.44813 | -44.89145 | 2024-10-29 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| baf1e8e8-7f77-3340-8eb0-a3b7214d0f31 | -10.44753 | -44.89656 | 2024-10-29 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eb30bea-91e5-3fda-9951-17457de651a8 | -10.44517 | -44.89558 | 2024-10-29 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb3c7f2d-ced4-308a-9657-71ee63afce06 | -11.40598 | -45.13484 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bc3a470-5529-3e4b-bda3-c6e2141950a9 | -11.40541 | -45.13966 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbb1d53e-a7c0-3a3a-9d53-b4ebe8a26a91 | -11.39968 | -45.1341 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bed3d184-4676-3b1e-8e7d-03c401cbac44 | -11.33751 | -45.03661 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README91.md)
