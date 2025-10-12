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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4964406c-1f81-312f-a486-30a6f58cff90 | -6.725 | -42.07762 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1547e23b-e78c-3c0b-b9e2-c495f36034ea | -6.72588 | -42.20388 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c3b4b51f-7773-32e2-a289-dd075490b62c | -6.17649 | -41.75027 | 2025-10-12 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fceebb41-82aa-3f31-95f6-1b9d07e5a966 | -7.12633 | -42.18706 | 2025-10-12 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0509b0ed-e10a-3c6b-b31d-9c0d966aab12 | -10.15328 | -44.61325 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f246060-43ce-3076-8c85-bec4f1fd201a | -7.41033 | -42.96756 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd2df573-0b0d-39a4-b441-9cf9d684ad2b | -6.75444 | -42.81091 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e74a56db-2eca-312e-b0cc-c401461f45c2 | -6.7176 | -42.21336 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 124b4d08-7117-3ca5-8062-9262d238d1ca | -4.18415 | -46.23339 | 2025-10-12 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1124b00-d6ca-3ebe-aee4-5b15476d09e7 | -8.21992 | -43.36192 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed9ffe7f-e067-38b4-b976-29795b067386 | -6.79137 | -44.52073 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5972427-89bb-3d14-8cb0-46e01a52552d | -10.21212 | -44.60844 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99639635-f813-3d6f-90f0-ab81a84e3ae8 | -6.72834 | -42.07812 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7d014da8-dc02-3554-9dce-d5c2e985e6f9 | -5.29071 | -44.45608 | 2025-10-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b019935-3227-3e9f-8c54-50c66cb19ce4 | -5.31931 | -42.88696 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0d5d9e5d-a0bd-3e27-95a2-620d8535c7d5 | -6.1317 | -44.04213 | 2025-10-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01dd0a12-d3b1-319d-a9f4-e01a5fdd2b9b | -6.04587 | -42.46577 | 2025-10-12 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1fcb1ba1-38f5-351c-b30b-15ed7e15e3ae | -5.2689 | -43.10095 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8704860f-dc68-3d43-90eb-984aa67956e2 | -7.13404 | -43.25602 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 82e82275-3f9b-3a97-8eb2-a6bddccbfac5 | -9.00815 | -47.35675 | 2025-10-12 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3e70405-27a6-3dfd-8541-8b974ebc5d4d | -5.74096 | -40.76426 | 2025-10-12 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e815b4e-549f-3eb9-adae-80c5f9aca682 | -7.51602 | -44.60729 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd072f14-2119-3381-98dc-1ecf6585dd4d | -6.24493 | -43.01955 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1390be3c-4881-302a-86c5-daad1b6966f4 | -5.88805 | -42.66699 | 2025-10-12 04:14:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 6b15a91c-d1cb-3a3e-ab9d-f52fb8800b44 | -5.58003 | -42.98471 | 2025-10-12 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f66791e-fe8a-31f8-b53c-93efbfc650ba | -11.36847 | -44.00793 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9e966f1-aad1-3648-990d-43c3ffb637ec | -5.68595 | -41.7362 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 942e067d-df57-3733-aa33-350705b20094 | -7.89255 | -47.06531 | 2025-10-12 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32bb00d8-c490-39d6-a358-7540abc6dd88 | -5.70254 | -40.71569 | 2025-10-12 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 274a19af-7c84-3c3f-8dd1-55fbd4a91b02 | -7.42933 | -45.15028 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24769bf0-4978-3b54-8fe8-699ccfa6c52f | -7.26179 | -44.15034 | 2025-10-12 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7cac3be-ea20-309c-99fc-bcb87b73a4e7 | -7.13134 | -43.27327 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e63f9d4-c346-374b-a812-548a85c8c363 | -9.51847 | -47.86204 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f87b8419-28fe-337c-8122-2b5e4d87d253 | -6.7572 | -42.81488 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40864fbe-e0e7-3bc5-b3f8-238c0ba0f6d7 | -5.64911 | -42.78067 | 2025-10-12 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3bae9028-d9c4-3f20-ad29-6321e1d7be40 | -8.15149 | -43.31868 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74e99118-7e9d-30e9-850c-f674addc4ef2 | -7.52049 | -44.60072 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5639e877-3bcc-392a-aa28-857d6314cd93 | -4.28032 | -46.93348 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e60ca825-83c3-34c2-819f-72b9c56535b1 | -5.97253 | -42.25839 | 2025-10-12 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1b258dd-fb6e-3fe4-a078-86aa175407a9 | -8.02062 | -44.45236 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f70a6f1c-fbaa-3ac7-bdb0-a488ed2e9811 | -5.92942 | -40.88503 | 2025-10-12 04:14:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5f24b28d-5704-34af-bfc6-471569aa6b95 | -6.16327 | -40.89307 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 35b2fce2-084c-3b58-b0f8-34661e36ab55 | -6.74369 | -42.87992 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f269174f-895e-3347-b0c1-9530f45dd8a8 | -7.85897 | -44.52762 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73686689-9507-3361-9ca0-97dded722eb0 | -5.59545 | -41.11548 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 516628b9-ea01-35ff-b77b-81db76dc39de | -5.06051 | -40.46125 | 2025-10-12 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd84991d-36c7-36a2-965c-7c291ff631f6 | -7.74923 | -44.21074 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4e524ca-cc21-341a-ac75-b3f4502bedaa | -7.85297 | -44.47942 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d72de83-7364-3126-9232-1048244244d9 | -7.80849 | -42.41555 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97b3cfd1-4d14-319e-b5a6-3596e67a2b85 | -4.43508 | -46.35614 | 2025-10-12 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a33ae3c6-f593-36b3-bf2e-6ff3a874a2ae | -7.40596 | -42.97395 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 769229c0-5731-3c0f-bc4f-6ca29869e1c8 | -7.87036 | -44.88038 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad9b031d-c2fd-3f4c-8b64-deed6f95dabe | -6.2388 | -42.99393 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78264b1b-7d6a-38bf-a8b1-9c2da5b0a780 | -4.88409 | -41.55148 | 2025-10-12 04:14:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b96c838e-5018-3bf7-bdb3-bf95b09fbf61 | -7.3449 | -43.85999 | 2025-10-12 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 126f5c64-358c-346a-b33a-4edc9d76242b | -5.15051 | -42.60016 | 2025-10-12 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66db6683-ee86-3e4a-9813-451c014575e4 | -7.14999 | -42.49605 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d74880c9-4bca-3538-8246-d216494cbdaa | -9.6778 | -37.08596 | 2025-10-12 04:14:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6d5fa9d9-b665-39d0-a842-f5dc91b35665 | -7.85508 | -44.53064 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 65a8e66b-bdcc-35c5-b50f-46e7661c0a6a | -6.26894 | -42.97394 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0801fab9-82ae-3e08-be03-757815ba15b7 | -7.88511 | -44.51361 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e2bd5c0-a48a-3599-a737-653c815022bb | -7.15354 | -42.18764 | 2025-10-12 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3ed046a-fe9e-3b5f-89f5-801eec97153e | -6.46472 | -44.64141 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1db62ee1-7b30-37b0-9844-5047a9e0edcb | -8.81709 | -47.30954 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0f01c9f-4e43-3509-a5b2-49dd8d0c72cb | -10.15719 | -44.54556 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23758187-2446-3bdc-808d-c7f1f4233032 | -6.96275 | -42.43089 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d1258ab4-90d1-3991-8b9b-1c29c50c818d | -5.48542 | -43.39325 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bfa35d2-d950-32d4-b75b-65e44a99526a | -6.24677 | -42.74822 | 2025-10-12 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17fcf987-66c0-3e7d-9aa0-4feb8829bc35 | -7.02376 | -42.74002 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 68039d85-24db-3670-8de7-d7b149f3f8ca | -6.22498 | -42.66689 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be8b5c47-fdcb-3cd9-89af-87bb13e262ec | -6.30002 | -43.77507 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 774f35dd-3c3f-3378-99f9-b4b116217211 | -7.80966 | -42.43015 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2cc5083e-c84a-3038-8ff3-f42bd3cf7609 | -6.25391 | -42.74581 | 2025-10-12 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3dc83444-16f2-3ac5-a80d-a219b36cab71 | -6.72446 | -42.0811 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| acae985a-ed99-3b1c-9eae-081751377f30 | -5.78231 | -42.47384 | 2025-10-12 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c95ba696-532c-32cf-9e1e-002ae76941a8 | -11.3668 | -43.99691 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3559c68d-91fe-3a75-9408-2feff44d8aa3 | -9.00446 | -47.35613 | 2025-10-12 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33834529-83bf-31c4-aff5-901cef84e3a5 | -10.17206 | -44.53728 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26ec00c4-4a01-308c-8203-18c320d90361 | -6.43472 | -43.37091 | 2025-10-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c8559fe-9266-3987-b8cc-158d08eead96 | -8.03003 | -44.45748 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b290bf2b-efc8-30e9-88ee-8a93134df6a3 | -7.65469 | -42.57466 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8eefc9bc-f54f-3f5a-a0c9-4f9576ba6c0d | -11.49499 | -43.22985 | 2025-10-12 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2dd0e867-3799-347c-a6ea-90cd36820bf1 | -11.72575 | -44.28769 | 2025-10-12 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6add64fe-adf2-38a2-89b2-4f69ce9e38d1 | -7.88732 | -44.52122 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a726ca04-87df-3ba0-8092-cabebf9fef3e | -4.67258 | -43.25748 | 2025-10-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 145a692a-819a-3318-ab64-590e648a3b67 | -6.04972 | -41.88994 | 2025-10-12 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3801e43f-5ef2-3039-993a-5bf5a77905ba | -10.14892 | -44.555 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 429586fc-3993-3c73-bb63-5cf4ed1e97a4 | -5.47304 | -45.23509 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 434e8900-7aa2-3124-94a1-955238148294 | -5.64742 | -42.76984 | 2025-10-12 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9285f401-903b-3d47-8882-c7dfb81ee779 | -5.65688 | -44.48022 | 2025-10-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66aff517-875d-3bab-a31d-40fe6f5ad9cc | -10.14501 | -44.60113 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0b3a86b-7f5f-3d7e-813e-6cc31754a989 | -8.68574 | -48.57475 | 2025-10-12 04:14:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2886d23-282c-36c9-a490-a4bd07efb234 | -5.97531 | -42.26238 | 2025-10-12 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b4190232-a678-3ec1-a157-8822bc0a89ad | -5.48212 | -43.39273 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68646473-5194-3e32-ba7b-48c08d851b85 | -6.73559 | -42.20591 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cdc30c6d-3065-3a76-8115-83d605d345a4 | -6.73446 | -42.08264 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6c57d70-356e-3e04-a0dc-3ca938c8fb64 | -4.37172 | -44.58256 | 2025-10-12 04:14:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c79d5c77-8852-305e-9dd4-e3a753b9daab | -6.28171 | -44.40285 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f72324-540e-3e80-a21f-295976fe4986 | -6.24244 | -42.92748 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d7c0ae8-f7ac-3dbc-b028-4b635a029864 | -7.85952 | -44.11726 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README20.md)
