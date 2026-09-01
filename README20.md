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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e982ab8b-a88a-38df-b05b-4810a80f124e | -20.38344 | -41.61057 | 2026-09-01 03:38:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e843d03-396c-3f8b-bfdc-3f0cdbabcf7e | -18.00521 | -42.69447 | 2026-09-01 03:38:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1e3b221-fdf7-3d00-9176-9f94bf0eb856 | -17.37198 | -42.37693 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 281c38ea-f3ae-3cf9-8452-0ac836063b9d | -17.38824 | -42.35163 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1d68d28d-69f0-3c5b-b420-b18cf49a91d1 | -17.13626 | -46.83708 | 2026-09-01 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01e8d863-aab6-3c6e-82ae-782da1978cb6 | -16.3716 | -46.88054 | 2026-09-01 03:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3934fdb-7e71-378f-99b4-0669887b4e53 | -17.39182 | -42.36053 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 01a7bd32-5fc6-33ad-bd9f-327f924c7568 | -17.38673 | -42.36353 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ba5888d3-c796-37d7-88c4-5b9ab515b7be | -15.17785 | -46.2491 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 36e1dbaf-1416-3d18-adb7-25423e92b7e0 | -17.3942 | -42.35356 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 80068d75-0fda-34f0-9d79-2aae1b8b19b3 | -15.19815 | -46.2227 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de890fe4-6f85-3eda-8c59-525f7dd1b074 | -17.38002 | -42.36476 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 726590bd-5b90-3eda-9da0-22e67f380643 | -16.3057 | -42.03643 | 2026-09-01 03:38:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bef3cf2c-a3bd-3713-bdfa-d110cda54c9c | -17.37784 | -42.37507 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb5c2f70-0e3a-3114-bb27-19f720e770e6 | -17.3199 | -42.7012 | 2026-09-01 03:38:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8572a063-2ef2-3571-afa9-c901421f38ac | -15.60309 | -46.58123 | 2026-09-01 03:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a137e8be-fcee-3338-9c8e-d9e3d8a06029 | -12.95199 | -45.96621 | 2026-09-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 278a7df1-1063-3659-bff4-a9605ae5b218 | -19.57087 | -45.71484 | 2026-09-01 03:38:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a505f574-fed9-3324-9214-59531985f0ba | -13.37737 | -41.34794 | 2026-09-01 03:38:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f511509d-22d9-355f-a27f-3ee1321e6b6c | -15.65967 | -45.9128 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d09fd870-1e72-3191-b078-b308daf531d0 | -15.6608 | -45.90764 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6f05c38-32ff-3962-bb3f-140b34fb8e0b | -15.1725 | -46.24095 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf810987-fce5-315b-83eb-9b20efeb3bc5 | -12.06978 | -44.99656 | 2026-09-01 03:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71eecb78-f932-30f6-95bd-45b964bceb86 | -18.30693 | -45.08585 | 2026-09-01 03:38:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 501d94a3-8f76-338e-8272-891cf27d5b4f | -19.57691 | -45.71664 | 2026-09-01 03:38:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c4eaf4b-8f96-34aa-b19f-e4a0c0f8c913 | -17.37364 | -42.37428 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6627e160-63f8-33c3-b00c-7ad27106d89f | -15.17138 | -46.24629 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12489be7-99d6-3428-91d2-97364cfc8355 | -18.30098 | -45.0831 | 2026-09-01 03:38:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff05ec9-4ae6-3432-9a6b-554f24437758 | -17.79027 | -39.70588 | 2026-09-01 03:38:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e1713bea-2cfe-34f4-b97e-fcd3abbe0eb2 | -15.66355 | -45.90878 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3689371-75b8-3875-a48f-89ceeea0da8d | -15.20509 | -46.22368 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03fa2eaa-c36d-36a1-8011-cc1391b10572 | -17.37229 | -42.38091 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e141029e-47fa-30df-9196-f41ae062b7f9 | -17.3875 | -42.35978 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c19a6329-a683-309b-af1e-f9ad27ad69f9 | -15.67238 | -45.91861 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b3ceffb-70a8-3476-9a84-aff9c93f0054 | -13.37665 | -41.35151 | 2026-09-01 03:38:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9d4d72c-639a-3519-b0bf-9e93ac0514fa | -17.37856 | -42.37165 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e3cca37-1754-3854-a95a-dbc0ea18600f | -17.37712 | -42.37846 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28060fa9-7a82-3a6b-83ad-bb5394477651 | -17.3795 | -42.37233 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06603918-ef9f-3d0a-b2aa-bde6d45e696f | -17.38159 | -42.36202 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 041194c6-458d-3207-9b3e-7d63c191ed6b | -17.37432 | -42.37096 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5b8bdf3-3b3e-3fd9-95f5-401bee521d29 | -12.10127 | -44.98074 | 2026-09-01 03:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e706cef6-d4d6-3569-9912-b93ac1b193c5 | -19.39615 | -40.86892 | 2026-09-01 03:38:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c25e658c-f3ed-3612-aabb-28998b96f787 | -17.14316 | -46.83914 | 2026-09-01 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04853131-5303-3cd1-9c9b-8274d55f3fff | -19.57245 | -45.71317 | 2026-09-01 03:38:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0e9aa61-58f1-3126-b451-16af8387b1f7 | -18.21151 | -43.97727 | 2026-09-01 03:38:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1bfb165-e273-3ad9-a139-b018dfa8d5ec | -17.13637 | -46.83741 | 2026-09-01 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd356505-7eb9-39fb-805d-42f3b946f0e0 | -16.6096 | -43.373 | 2026-09-01 03:38:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 511c6db6-d336-3036-8c57-e3acb99918f0 | -17.38903 | -42.35218 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bad8798e-1c6a-39a0-bb70-b2e5916a79a6 | -17.53281 | -44.61664 | 2026-09-01 03:38:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4940c3c6-f118-3a6d-ab54-df8bdbc955cc | -17.38666 | -42.35913 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e783e26e-972d-37e9-9b08-b3cdcaf081c5 | -17.39265 | -42.3612 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 87a9be1e-ce4f-33b6-a1b3-e7b83b72cb08 | -17.3764 | -42.3819 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50b231c0-dded-3315-af78-1ce395baf10c | -15.17114 | -46.24698 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24f8c9a1-93ed-3583-85d9-0a5c99594abf | -17.38827 | -42.35592 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 658596ab-6401-3aea-a958-cf35c3f5feac | -17.31785 | -42.70156 | 2026-09-01 03:38:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff55f487-32ee-3850-bab8-2d26152ffce4 | -18.56587 | -41.27139 | 2026-09-01 03:38:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 194b9983-5f01-3086-affc-829955e10ab8 | -17.37129 | -42.38024 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55c639df-094b-37f1-ba7d-77aae7a5a4a9 | -18.30095 | -45.08415 | 2026-09-01 03:38:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e98b38d9-838b-3610-b3d4-c09b1155a5fc | -15.17269 | -46.24031 | 2026-09-01 03:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c570292-edc1-3063-993c-370adc6f4487 | -12.07092 | -44.99126 | 2026-09-01 03:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 907d6135-2748-3e18-8356-8654d6dda01d | -18.53457 | -42.16284 | 2026-09-01 03:38:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ee7f2d52-72b5-3664-be5d-a9adb3c5a6e9 | -15.65575 | -45.91234 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 491865b0-3ce7-3f73-9899-f3ffcaa32e8c | -16.35953 | -46.87967 | 2026-09-01 03:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9027810e-3c13-37ac-91be-a2b0b9d1a6fa | -15.66734 | -45.90968 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 705df4b6-abf7-348b-890c-14c3a7621c59 | -17.3788 | -42.37576 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66dd4002-8360-3aa1-b66c-ddbbd10ee9c1 | -13.34461 | -43.67318 | 2026-09-01 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c965c1e9-f2ef-333e-816a-21bfb7879e9a | -17.3809 | -42.36544 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1b6985a-e5ed-3b00-81eb-d30f02823f84 | -17.37268 | -42.37366 | 2026-09-01 03:38:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c25ff627-24e2-3121-b68c-6fd7c357c09e | -15.67639 | -45.91388 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc619bc7-f40d-3979-bf9d-2e9e2514ec0b | -16.61526 | -43.37414 | 2026-09-01 03:38:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdf35e2c-ccfc-3dd9-ae4a-fc7fb19c413b | -19.57133 | -45.71815 | 2026-09-01 03:38:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a7b5374-845d-369a-b8be-ac02e19d83a4 | -18.52956 | -42.16159 | 2026-09-01 03:38:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ca424dbd-8e88-3267-81cc-d9b492402957 | -18.20593 | -43.97551 | 2026-09-01 03:38:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 505a0b82-6af5-30e3-aee7-e353e7c6a30b | -16.36463 | -46.87911 | 2026-09-01 03:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61f6dfcf-db0a-382c-8dd1-083973bc1917 | -15.67 | -45.91121 | 2026-09-01 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| feb5fe33-5613-3ac4-a28c-31cc5917d5cd | -19.11682 | -39.75312 | 2026-09-01 03:38:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 97022b84-60d2-34d8-99dd-9a210c7e64c6 | -17.14303 | -46.83884 | 2026-09-01 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf3cafc5-b2bf-354a-8be2-10cee23802fe | -12.95891 | -45.96809 | 2026-09-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c036d9f9-3ee9-3f5c-91f5-d12262a08901 | -7.3487 | -60.5883 | 2026-09-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ab71f4f1-d13f-3fe0-85a8-ff5e31589b29 | -7.5895 | -60.4636 | 2026-09-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| d5ee3d25-e30d-353f-9005-9d63998bdff6 | -14.478 | -52.5126 | 2026-09-01 03:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 4edc8e8a-d5db-3a73-a357-1f18e3e4ebd7 | -14.6732 | -53.5408 | 2026-09-01 03:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| e03abd1a-35ec-33d9-85ea-6af62a8c7d8c | -18.5089 | -50.8974 | 2026-09-01 03:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f02680d9-ff66-319a-b65c-af0bbb7b3f8c | -7.5894 | -60.4827 | 2026-09-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| fb451c38-8c7e-3b0a-b229-bb47edc5b7ff | -7.5709 | -60.4835 | 2026-09-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d1b3686b-1633-36de-b740-795dafd7319e | -14.4777 | -52.5339 | 2026-09-01 03:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2d314b51-8cad-3302-8072-8c36a1806156 | -6.6036 | -58.5972 | 2026-09-01 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 401c5016-1664-3302-9c42-ebb7b5d2b484 | -14.4587 | -52.5151 | 2026-09-01 03:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| c347c884-6fee-36bc-b23b-b9eb115315ed | -7.571 | -60.4643 | 2026-09-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8b71ae8b-d338-315f-b0be-e238240b21a3 | -21.24636 | -44.52271 | 2026-09-01 03:40:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0fb4e58b-e6f6-38a4-b988-314a6464c0d2 | -21.45667 | -43.91451 | 2026-09-01 03:40:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5f075820-c5aa-30f6-ad4f-ef9e41caa209 | -21.2479 | -44.52515 | 2026-09-01 03:40:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34daaf69-b665-348c-b824-78d2cfcd538a | -21.46197 | -43.91578 | 2026-09-01 03:40:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4221cd95-2e81-3c44-be9b-e5fd920df1e2 | -21.87246 | -42.03538 | 2026-09-01 03:40:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0fcb8960-c3b4-3c3f-a146-dd1a7121841b | -20.90118 | -43.29528 | 2026-09-01 03:40:00 | NPP-375D | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 93cb13e6-6e67-349f-b1aa-fc177c83fb1b | -21.24876 | -44.52129 | 2026-09-01 03:40:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34cfce88-d81a-33d3-8eff-7276b76b7617 | -21.45745 | -43.91095 | 2026-09-01 03:40:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 09a1bf2e-4bcd-3dfa-a0f2-a52b9a0ce6d3 | -7.5894 | -60.4827 | 2026-09-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ce7484e1-e02b-327b-8d5e-3b2313021394 | -14.6732 | -53.5408 | 2026-09-01 03:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 9db9b048-3a4b-3d2d-bcc8-293acf7ebdd5 | -7.3487 | -60.5883 | 2026-09-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |


[Clique aqui para ver as próximas entradas](README21.md)
