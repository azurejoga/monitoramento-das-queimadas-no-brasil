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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16af5f48-f593-3ffb-82e0-8f6a6fe6c015 | -8.36395 | -43.64519 | 2024-10-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6a352e2-13cd-3e18-bfd0-e481e4e2a28b | -8.36248 | -43.65382 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a535ba30-f183-39cd-8a37-3a1a6c0f3bb6 | -8.18564 | -43.73262 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 13d592a1-2dc0-314a-ae78-ed9417102ad1 | -8.18486 | -43.73707 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca0379ee-df10-39dd-a0bd-386cfb389307 | -8.17831 | -43.72218 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d3bc7a8b-3bb4-3f1e-9b7b-ad00bffcbdbd | -8.17753 | -43.72663 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cd285df7-61be-33d1-8dd4-fe2f59a135c1 | -8.17387 | -43.72142 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d512bea7-1dfa-3075-84c0-4ee7108bce3f | -8.17309 | -43.72588 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b33d9042-3f75-3807-9db5-bc86e17bd249 | -8.10994 | -43.78154 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c24f3f4f-162d-3d12-90b5-084a21b3445e | -6.43518 | -44.03501 | 2024-10-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19d8f604-72ed-34c6-8a87-6c6f34860043 | -6.42394 | -44.07294 | 2024-10-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0aa0523-a700-36d6-b114-59de23622c6f | -6.08485 | -44.70397 | 2024-10-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4e4c7df-322d-3680-b69f-078a338811d3 | -6.07991 | -44.70322 | 2024-10-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79f7faa5-41f0-3d5e-b4ec-2c10cfe990e6 | -6.07497 | -44.70251 | 2024-10-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e677342f-d6b4-3fb2-9243-8268c0fc191b | -6.07003 | -44.7018 | 2024-10-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00d00b12-382b-3492-bd8a-1578462f3c37 | -6.06905 | -44.70747 | 2024-10-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f51c525e-ad4e-3786-b6c2-e07746a9548b | -7.4012 | -45.23037 | 2024-10-05 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c3289a3-061e-3b69-9fc6-3eb4d31243b4 | -7.40068 | -45.2333 | 2024-10-05 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53841f02-a446-39ca-b2db-0013bc16c089 | -7.18073 | -45.04859 | 2024-10-05 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33abd196-6273-34b3-a24a-e152aa8a33ed | -7.16195 | -45.03961 | 2024-10-05 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 09033508-7d9c-3bc6-a704-ed581eab87f2 | -7.09541 | -44.44049 | 2024-10-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4cf776f7-51c0-3591-b881-1052246188f8 | -7.01867 | -44.39828 | 2024-10-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72b15260-50fb-3554-9ce2-e4854634105c | -7.01389 | -44.39772 | 2024-10-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73e40cd0-7c7d-3f48-befc-b83f7b478d86 | -6.68131 | -43.99479 | 2024-10-05 03:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 906b938e-eed3-328d-adbe-7dddad6582ab | -6.68144 | -44.83547 | 2024-10-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fd0a3e8c-1c98-3c3f-beeb-7b5db507295c | -6.66552 | -44.05729 | 2024-10-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24c4d4e0-6a44-37ab-86f4-5ea8bd3b5b67 | -6.58138 | -44.64552 | 2024-10-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ac7a0e4-7009-3e03-9324-0bc1c486c59a | -6.57951 | -44.17659 | 2024-10-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f70de5fc-1358-3439-aac4-835bf8824e1a | -6.57462 | -44.23286 | 2024-10-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 485db02d-df78-3641-b505-17616c57b8a1 | -6.56898 | -44.23732 | 2024-10-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 445c30c0-4ebf-3cbf-af02-31bec385101e | -8.29954 | -45.43046 | 2024-10-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78234731-75c7-3d45-b61b-bd69607f5d75 | -8.15713 | -44.40699 | 2024-10-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea4ed169-37ee-3fc9-826b-9f78f2cfa105 | -8.15624 | -44.41197 | 2024-10-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a448c328-546a-3b35-9028-9a26b013a407 | -13.11175 | -46.36726 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 160.1 |
| ed2d88ed-1329-3d46-8cd7-67b9e1897b2f | -13.111 | -46.32849 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a31fd0dd-981c-341e-94a0-518f23e8183b | -13.11068 | -46.37279 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4aa1ae86-32b9-371d-985e-5d059ed916d3 | -13.11014 | -46.34941 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 282fa7fc-e802-3aa6-8822-48ad0e53bae7 | -13.10996 | -46.33415 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 36f35499-8018-3651-8a6d-232735a86a20 | -17.15103 | -44.77719 | 2024-10-05 03:51:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d201b75e-faad-34b1-b0e8-58fb5c864a60 | -14.27924 | -48.17068 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cdc3d563-6a97-3586-bce3-6295037caecb | -15.17894 | -45.48155 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b1f49d1-a833-3531-a80d-1989e39939d3 | -15.1781 | -45.48605 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eeaca13-d6be-32b2-81fe-82bc5e4dab2b | -14.20646 | -46.46436 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a066a248-bd70-3f65-9b74-bc0dec6e608e | -14.20438 | -46.47518 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0620e083-5c91-3524-ab18-e592b7502551 | -14.20339 | -46.48036 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c115d67-edbe-3ac5-8ea0-59ebb1c7cf6b | -14.20277 | -46.45769 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 945ee6c4-8683-38c7-8461-1e90df99247c | -14.2017 | -46.4632 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34ffbcc0-6800-30b1-aa88-b2e69065ad2c | -14.19957 | -46.47429 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af4c1242-1ff0-30c0-9244-750d42b2e923 | -14.19852 | -46.47977 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d5e83d8-6810-3128-aea1-d7a50621faec | -14.19259 | -46.48465 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0290e36e-9eca-3036-9c10-3f7941b44c1b | -14.05041 | -46.37615 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d48f6b71-3e85-3fa8-86e1-850ad884b1dd | -19.14055 | -46.64098 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 73e0fd37-fe90-3af1-bb69-943f644f953e | -19.13967 | -46.63863 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0ec74d40-8bab-3041-b384-4e369c885a5f | -19.13907 | -46.61861 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26b92712-2f5e-3caf-b817-4879f25dcef1 | -19.13543 | -46.61976 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c7e5f13-04d8-3986-be79-46fe0309e69c | -19.13361 | -46.62925 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7159eaca-c9d3-3726-a786-512858ddb2fe | -20.66874 | -47.08888 | 2024-10-05 03:51:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 709b5cbc-7ee7-393d-b3d1-56b8b971d2a9 | -20.66783 | -47.0935 | 2024-10-05 03:51:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2edfb64c-786a-36d3-a029-f9ce345b46a2 | -20.6643 | -47.08801 | 2024-10-05 03:51:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54e06c57-6992-3712-94fb-bfd33031b9bd | -20.66339 | -47.09267 | 2024-10-05 03:51:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8ebda27-3a57-36c0-a042-39862c1bee9d | -20.48357 | -47.01221 | 2024-10-05 03:51:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18d6ea7e-3b22-3fab-9c5e-2a012e02f4e8 | -20.28221 | -46.87732 | 2024-10-05 03:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 012288e9-1f77-306c-bd53-bee55f40a084 | -20.2813 | -46.88197 | 2024-10-05 03:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc90d505-d99d-3de4-bedb-650ace425d0e | -20.23513 | -47.09432 | 2024-10-05 03:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b775ae48-0858-3b34-ba07-cd87713a55ef | -14.79598 | -48.09236 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 670ca016-8cc2-33bd-9d9d-0015b50cd999 | -15.22369 | -47.15726 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 457059e0-4f0f-380f-9698-559a1f30c6e5 | -15.22155 | -47.16047 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e23e9a64-a613-3453-8991-1298d78a3f07 | -15.21271 | -47.49951 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce69bec1-f20f-3569-a3dd-98179780f7dc | -15.20716 | -47.50113 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| adeea69c-35d4-3a36-b996-29adf72b31b6 | -15.20205 | -47.50047 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c23c381b-460e-386f-b415-9e2eedde6175 | -15.20156 | -47.50293 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c914e262-b970-3f05-acb9-b8fbde9872a8 | -15.2011 | -47.50525 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6973fde7-63fd-3860-97b1-2aefb1472717 | -15.20066 | -47.50749 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b688ec55-3499-32da-ab29-ce8b366f1aa7 | -15.19545 | -47.50731 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ea135f2-3073-34c9-a309-320c6650b767 | -15.19456 | -47.51183 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e0bfae92-cd81-356e-b5d3-2ab3cea3a913 | -14.79533 | -48.09561 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f6a860d-0283-3020-9a6a-b84f57c7b26e | -14.77686 | -48.05068 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd45c859-3805-3bda-b1b6-9fd82f883d40 | -14.77291 | -48.04308 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 076bac4b-b014-3d4b-8ad5-9aac8787c70d | -14.77222 | -48.04649 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e32732c-1c22-3428-bd5e-3edfedae0c01 | -14.77152 | -48.05001 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b4d31a5-81ce-3980-b3e5-064bfa06dd9e | -14.76371 | -48.03438 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bd8c400-73f1-3ee0-acf5-8e8439e493af | -14.76302 | -48.0378 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12ed66df-a459-3bdb-862e-037162e30859 | -14.29594 | -48.17068 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5430de29-968f-3193-b7d8-028c6c63bfa8 | -14.28991 | -48.17299 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9d56fd0-07b9-3399-ba12-03848fc8a9ba | -14.28458 | -48.17181 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 281d4c1f-932f-3688-b509-e56a197f9298 | -14.28385 | -48.17542 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afa43de2-da76-353e-aadd-582a28239099 | -14.27609 | -48.15876 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b56f2328-94c4-37f3-9145-8377ded4f253 | -14.27536 | -48.16236 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3208d307-9f77-3ea9-842b-f4172ed5bc28 | -14.27462 | -48.16598 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 30b1bdd9-186e-300f-8921-850173e96f00 | -14.2739 | -48.16957 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7f3624e0-b0fc-3ecb-a9ad-b460c81593b4 | -14.27336 | -48.15803 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1dc718af-1afc-337c-9780-6370f71e24ad | -14.27264 | -48.16171 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d9322b49-bc58-3f86-a33d-539d9533e323 | -14.27194 | -48.16532 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 29a12fc8-5bf0-3de4-9688-c46c85f74a37 | -14.27124 | -48.1689 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92c8236f-5dce-36d0-8b65-008023ab4b35 | -14.27076 | -48.15759 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fcab7ae5-4e2f-30be-8e46-eec7cb71fa63 | -14.27002 | -48.16124 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0c20efe-83c6-30d0-afdb-58f9f9a91a97 | -14.26929 | -48.16483 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77551eb6-7d96-35f5-9a56-04551a96a856 | -14.00509 | -47.26947 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cf906033-7a60-3520-84b1-593c1924acee | -14.00445 | -47.27282 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b06c9672-387c-321a-a2bc-f21e72b58897 | -14.00356 | -47.26692 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README47.md)
