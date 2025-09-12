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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0647f9a1-db90-3a51-a665-171a912c3bd6 | -13.89355 | -48.22524 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a88a0bb8-95e8-363b-89d6-97b973c11f33 | -13.78308 | -46.2871 | 2025-09-12 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 223b9926-40f8-3323-b118-a94d4d108d67 | -16.42688 | -45.69613 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef6a5c5a-46da-3ff1-9d34-817ab8f2bbaa | -16.49314 | -51.97412 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18199477-bd35-3154-8cd9-28a8122ab72d | -14.39551 | -52.94014 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9d8edc3-dbeb-3c8f-a598-5c2c55125bd9 | -17.13433 | -48.49537 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60c255c4-d0e9-3e81-a517-c8982830925d | -11.70233 | -50.60094 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07fdb2db-8c11-3720-b8d7-00a8ff49d06b | -17.21298 | -48.68593 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e51e051f-0cb2-35a2-bbd0-a030434503b1 | -16.43517 | -45.68897 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9b8ff35-5c76-3b9c-90c7-44a660bf5fa2 | -13.90018 | -48.22633 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a60f3f53-eae1-3c25-87c4-8712adea6a95 | -15.09479 | -52.46726 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d20c6a27-12d7-3515-84ed-4f7e872110de | -15.23097 | -44.03904 | 2025-09-12 04:27:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a19d404e-462a-30af-9354-5e3435a830cb | -15.09511 | -48.09852 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c609cb63-5a19-330c-88c9-a4ad3820de96 | -12.85733 | -52.97391 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae7daff5-c998-3d93-9f41-ecef4919cc56 | -14.16762 | -46.19611 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b891b8c2-552e-3550-82a8-c61852f05e98 | -13.27346 | -51.71634 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 95e4bc89-3f11-367f-b26f-3e02ecae84ce | -18.61801 | -48.24912 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 133c31dc-82b4-3c08-84ed-b798eff022da | -12.9764 | -48.01182 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 444a90d5-161a-3680-8dc4-6252b4a59cd7 | -15.07912 | -52.44495 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee6a8050-3ca5-3b02-9065-1f4b2ee3dd57 | -12.1531 | -48.69449 | 2025-09-12 04:27:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e3da7ca-d6fb-3c22-90c0-4e5c837786ad | -12.85863 | -52.96667 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 713e77a9-17dd-36b6-ab03-3ad0629e7c37 | -11.92753 | -50.69637 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa718984-0c2e-32ce-9866-4e012b8b70ad | -13.90337 | -48.27044 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| d0432ee0-be8d-3655-822f-4e013c54f074 | -17.20593 | -50.1476 | 2025-09-12 04:27:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b9951f-cf9e-3bce-9f85-aa2c7f42be58 | -16.42904 | -49.02667 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f58cafbc-f103-30c2-914e-a88128dc84d5 | -15.08291 | -52.44567 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4afd32c9-a9a8-3f6e-9b3d-4a80822e23c4 | -11.19624 | -55.08237 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e606dc83-801c-3012-95bd-81bae61d1e96 | -18.55733 | -46.56114 | 2025-09-12 04:27:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21c09b61-5565-33dc-bc15-99686ac809eb | -15.68546 | -47.01478 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a889ca3-7fa5-370f-9173-7501c175178e | -15.79194 | -52.24401 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 666447e5-933d-3ee6-9bc0-eb31ec0c4361 | -15.68142 | -52.2306 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59348a75-219a-3ac4-84ad-d8fec80f6954 | -14.18417 | -46.20228 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 54b6fef0-7160-3fda-91f5-f1bf417b04d2 | -18.06114 | -45.44353 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e8c0b98-be6b-3efd-bfa5-7918b27d7f96 | -18.62243 | -48.26492 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 12f604c5-57e7-340e-ae84-c0cfaf47a981 | -14.45303 | -47.31664 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e540231d-637e-3821-bf20-debd884af02a | -15.12116 | -48.6004 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f6c945c-667c-3426-829d-04715aee6ae3 | -18.65533 | -47.66334 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c8ffffc-990a-34d6-b7d7-217a5db3df75 | -11.73359 | -50.62255 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97b3839b-bee1-3cef-9dff-de1fc873dd90 | -16.43064 | -49.03807 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93cea97f-3a47-3ede-9080-f65472feb818 | -16.95694 | -45.8219 | 2025-09-12 04:27:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09e7b0d3-2046-3d74-a70d-311374d83532 | -18.33522 | -52.05885 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42559bb1-bf83-3897-bea3-1a389e5d42ba | -18.32911 | -52.05941 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| beace85a-d07e-3b09-a751-003a9760de47 | -20.03509 | -41.7428 | 2025-09-12 04:27:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a2f4ca4a-1534-3fed-8c35-4658fbcfde8e | -13.9471 | -48.23049 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8eafe6ae-5a8e-3701-a678-fc55241c73aa | -17.36107 | -46.70035 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54b8e64c-8e34-353e-ac52-017f5affab7e | -15.78983 | -52.24546 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc12976f-6aba-3cc4-a8f8-7e9540516bf3 | -17.91272 | -45.70852 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cef23250-99d9-325a-bb95-4e6fec760e59 | -14.28886 | -45.04208 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25e611c1-4ed9-3ce9-b154-6f1e1dff17f2 | -12.93282 | -54.74986 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0dacd459-a7cc-3312-8618-1475738a9916 | -11.9901 | -51.14036 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2937d514-7115-3920-9ac3-4a3962c30f3c | -16.41739 | -45.68623 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dea0f5b-fb66-3e48-bdec-ba1eae190d3f | -11.64628 | -50.58253 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de1b5ca5-e72b-3ed6-9b45-a93505cfe6c4 | -12.92245 | -54.8068 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4a7eb29-fb4d-3fe1-bae7-fc6998c384d5 | -17.34611 | -46.68207 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42475ed9-dd5e-34e4-b776-0b53bd2c96e4 | -13.91174 | -48.23913 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fffcdbeb-da0a-3a8c-ac6b-25e3ef8419c7 | -15.66313 | -47.03891 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 29154056-1d45-3030-8a2c-640647bfa7fa | -12.56341 | -49.1432 | 2025-09-12 04:27:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a4a747c-38d1-345a-8069-31580506a7e7 | -12.8678 | -47.94761 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67222224-9f92-3869-9b3f-074584b93b54 | -15.10091 | -52.4517 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cff2534f-fc40-3daf-8384-69b137d4c89b | -11.9966 | -51.16883 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e670c0ab-6cee-360b-b4c5-984327c77b2a | -11.19148 | -55.08138 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6d761e7-26ef-33ea-87dc-f4ada9e935e0 | -11.93861 | -51.18335 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 501c8aa4-9a9d-3dce-812f-3ac8d3843592 | -17.37009 | -52.92718 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c3b341c-8644-3e06-abcf-104b20a44da3 | -15.12335 | -48.60807 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e5e83f1-61ed-33e7-b839-dfbe1479666f | -14.5546 | -54.52166 | 2025-09-12 04:27:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eb8d196-8ea3-3dba-b998-7f0c9d0b6832 | -18.59362 | -47.18399 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d46b34a6-72f1-34f8-8e1f-7cc49571cb27 | -12.86393 | -47.95058 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 649866b3-1441-30ed-a473-c0dfaf58fd9c | -14.37925 | -47.28974 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e43c0517-b804-30e4-9111-d178c845bb89 | -12.86187 | -52.94869 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 811f9f1f-846d-3fdc-b11f-0a4534023ed6 | -13.78418 | -46.27984 | 2025-09-12 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2160fb7a-2c07-3d74-9e13-ee544a1b00cc | -16.59485 | -49.80888 | 2025-09-12 04:27:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c951ead4-8410-3cbb-acc5-8fd648ef1a1a | -14.42028 | -46.3997 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f4b5164-7965-3683-8f82-913b6f12c895 | -15.93622 | -48.16806 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c735627-05a3-38da-b906-64a8ed540a9c | -14.41402 | -52.92757 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06140023-b06a-3714-a6bb-75ada3002fea | -13.9078 | -48.26392 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ce526a6-a8fa-3fcf-bdf5-9f04991b961e | -18.60443 | -47.18189 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e50676b6-ed00-3801-99b4-77a030aed51b | -17.9819 | -50.08025 | 2025-09-12 04:27:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efa183f0-5e63-3655-bb1f-9435f5a1fe38 | -13.90174 | -48.25928 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 7c24a33c-2397-39e5-98bc-1282cf14e4dc | -12.58745 | -45.67937 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b53a905c-1348-33f5-bdca-dbcadb0ca595 | -18.66713 | -47.65377 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b22ad17-76f5-3106-9c7d-6fa32274922d | -13.35953 | -41.92488 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2cbd8a83-993b-3de2-b892-d617a81b5641 | -13.17792 | -47.26931 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07e50a9a-cf74-3e2a-9b56-3bbf0def8a88 | -17.33818 | -46.67006 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b54c222-0f32-3e9a-938c-ff5fe6e479fa | -12.92204 | -54.75748 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 297b7b7f-f868-3075-bdd1-0a7418d53d5c | -14.14646 | -44.4501 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b47b18c-ae6a-398c-9543-f3d03eb5532b | -16.6156 | -51.80792 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edb76077-64d2-36fc-aeaf-7f6cbd1ed809 | -15.10062 | -48.10674 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f49ff44-08c5-398d-a43e-4ce952672f55 | -15.10299 | -48.00476 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e92b0c3-f776-31f4-8345-8fd82cc3d213 | -15.60316 | -52.73152 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dcea91f-62bd-3be0-95e6-d90b3cf145f1 | -13.17183 | -47.26467 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 915d17d2-5052-31d0-8465-7c3380743a9a | -16.65448 | -47.62956 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2b5cf18-4e39-3ed0-b44f-7bab867651a9 | -18.06099 | -45.44068 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5744a123-7794-385a-a801-7826f9fb2c65 | -12.83722 | -52.94395 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89b92ca2-9e0b-3ff9-b3e7-3549bbab5c55 | -15.88062 | -48.17738 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49054f04-65a5-320b-93da-f15c0bac36af | -13.90724 | -48.26746 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9246b1bc-474d-3f1e-84b9-a55615a62c13 | -13.9023 | -48.25575 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e14939e7-8748-3739-92c9-fa9c87b6fbdf | -11.94672 | -51.18026 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a09683e5-84fc-3c36-b890-d7c7c017ebfe | -15.09786 | -48.10264 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bbd4a5f-be89-349a-b778-8606e0eec3c6 | -15.09923 | -52.46106 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe374caf-f9b9-3723-a2e6-1f099375f066 | -14.42084 | -47.32983 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README88.md)
