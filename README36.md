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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b479dc3-0a5f-36b7-930c-336d08ab005f | -12.83113 | -48.11357 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 098187ab-1715-3e7e-8205-033e233302e5 | -12.0674 | -43.46923 | 2025-08-29 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b172abb5-dc47-322c-b40d-0f5ee9a23c7f | -4.11063 | -48.01842 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f9b56912-83ca-30d0-ba83-8a9218a2905c | -6.1452 | -44.43224 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3faed92-00c7-3b7f-9043-1b3cd322d4d5 | -11.30386 | -43.54636 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdfe9ab8-f7c3-3d21-b0bb-007ab0dcd9b2 | -5.8587 | -42.94048 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 868f0adf-ea62-31b2-9e1c-a9468bf74cb4 | -6.26744 | -43.81818 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 888a03bd-8a49-3743-b4f7-b0018694b5bb | -4.07623 | -48.04751 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85b02a01-1a9b-3e27-a4f3-f859079cca59 | -10.02669 | -48.07022 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc234a40-570b-3f07-b50b-f2f57277594a | -12.83301 | -48.163 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 013834dd-875d-3d77-9eef-f1424a081441 | -5.85796 | -42.94474 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1e2185dc-71b3-3486-a6c1-50dc4f250c62 | -13.54695 | -46.87426 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 301e3b3a-b163-3a42-bbd8-72c9c40577ed | -12.32007 | -47.05006 | 2025-08-29 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e5c1b4c-0f5f-3180-8395-4e62bf7a6b09 | -10.69699 | -47.07216 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c935f8ef-746a-3daf-9c6d-99d5ae6767a5 | -12.09432 | -44.72923 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 8b99fc07-36ac-378b-a461-fc1ff8179a2a | -13.40747 | -47.00787 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d84a038-fd8c-3db3-a5f0-865f1ab433bb | -6.22271 | -42.75375 | 2025-08-29 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a65d55fb-f62c-3031-a8da-bcb8e07b154a | -9.462 | -60.549 | 2025-08-29 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 901a53ca-5fe3-3da8-a439-92ca965aa796 | -9.7322 | -64.9067 | 2025-08-29 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 925f12cb-44de-3008-8d2a-91439ab28028 | -9.4618 | -60.5682 | 2025-08-29 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| d7a2df60-0741-3771-a35b-92dd86a24125 | -23.676 | -51.8192 | 2025-08-29 03:50:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| b98d8a2c-e5ae-307c-a555-fd6f6d806a27 | -10.3624 | -57.8258 | 2025-08-29 03:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4c7e127b-3e6e-3fce-a945-20bfb60751bf | -9.4433 | -60.5499 | 2025-08-29 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ffe2ccac-1832-351b-baba-30d005da2a08 | -9.1154 | -65.7886 | 2025-08-29 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| fa510f8b-2aba-3631-a85d-dd92362bbc5c | -9.773 | -64.2469 | 2025-08-29 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 22ccdc5b-8d73-33bf-ac8d-fdfcf300031b | -9.9328 | -59.9247 | 2025-08-29 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e7009859-532f-3c8d-9689-0affeecb1a3d | -9.1155 | -65.7699 | 2025-08-29 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 76ca0aca-4596-368f-8b70-1b5a172b0c6f | -6.5546 | -43.9221 | 2025-08-29 03:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 43771a09-2558-3291-9fd3-982ef7152c68 | -9.4432 | -60.5692 | 2025-08-29 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f3563ecb-f9a6-32a5-a74c-31e6d48b9a33 | -3.4254 | -49.0517 | 2025-08-29 03:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| aeb2f2db-c135-387c-9c60-78cd24016991 | -12.4345 | -63.9173 | 2025-08-29 03:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 95a3dd84-0f75-3cd0-9cfb-be47f2407416 | -8.1758 | -61.3755 | 2025-08-29 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 02ef5297-a563-3b20-845e-2a19ad971db7 | -19.1161 | -46.68229 | 2025-08-29 03:51:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c20dd745-2560-3458-88b8-3392df5405fb | -20.67821 | -44.82333 | 2025-08-29 03:51:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6bfb91f8-c56a-3375-9585-e77664320662 | -20.49426 | -42.24718 | 2025-08-29 03:51:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 530bd539-d26b-30c2-9eab-f1e07e4c299d | -20.23673 | -45.74174 | 2025-08-29 03:51:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94faccd7-6e61-36d9-aa8c-a2d30a8e80b2 | -19.89638 | -43.60509 | 2025-08-29 03:51:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 35698115-81ac-3c36-9bcf-812cbf18e058 | -18.19763 | -45.59587 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 335b3870-1b30-3a41-8cb5-9759e1ad50c5 | -18.08316 | -44.7212 | 2025-08-29 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33f9227c-edb0-37c3-876c-f529d1dedbe8 | -20.23264 | -45.74085 | 2025-08-29 03:51:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4d81e30a-6bb2-3549-84e0-f361d837db0f | -16.28058 | -53.62087 | 2025-08-29 03:51:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ccdb1c6f-e071-336b-a2bc-d4a4f3f9f306 | -24.16623 | -49.57063 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 36f61f88-62eb-337a-9a4d-0a659776b41c | -24.16546 | -49.56646 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5dc4e8f2-7858-30c3-96e1-379ba28125ef | -18.31169 | -45.13535 | 2025-08-29 03:51:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 79a88b0f-05be-3635-a1a6-d07778c2103f | -24.17689 | -49.56808 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7213bbe1-28d5-3f59-876e-b7fe54474414 | -20.23337 | -45.73693 | 2025-08-29 03:51:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0dd121b2-df5d-31e3-9d21-393e22444110 | -19.7332 | -45.84698 | 2025-08-29 03:51:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3be00ad9-b0df-36f9-af87-7a892efa8a5d | -23.67311 | -51.82486 | 2025-08-29 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 947625f4-7aec-37e9-9d7e-766da03d699c | -20.03304 | -41.41412 | 2025-08-29 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6b95251e-6544-34de-8835-9e4d40c29e32 | -21.01274 | -45.0666 | 2025-08-29 03:51:00 | NOAA-20 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31139fcc-2723-3bd2-82c2-ac58418a4420 | -18.97512 | -52.94769 | 2025-08-29 03:51:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 54bee9d6-ab46-3d01-86f7-4f4f5f75185b | -16.27832 | -53.61406 | 2025-08-29 03:51:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9dda131-bdad-3d19-9e12-351ecad7ade0 | -19.16344 | -41.83035 | 2025-08-29 03:51:00 | NOAA-20 | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ac5b283-2927-38a0-82b7-cecb64da73c0 | -18.21678 | -45.5868 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2efa56a6-f654-3b06-880a-3852060af7fc | -20.28518 | -41.29915 | 2025-08-29 03:51:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 19de50b3-63f6-350e-9984-9dd54f1eadad | -21.53403 | -45.32547 | 2025-08-29 03:51:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e7c14e4-f70c-3f21-85c7-7298757ccec1 | -20.02967 | -41.41352 | 2025-08-29 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 52fce8a0-9612-3fec-a495-5669e4287285 | -21.53485 | -45.32347 | 2025-08-29 03:51:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b17d5a43-b4db-3a99-8c10-b765d47950cf | -24.17496 | -49.56925 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a09968fe-2144-32c9-9504-92ca76f715e4 | -18.21908 | -45.57443 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c66c84f8-ed03-3349-98fc-0989ab588075 | -23.67513 | -51.82568 | 2025-08-29 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4ca1cd81-172b-3f9c-bdfd-cffc8d889f70 | -19.90004 | -43.60577 | 2025-08-29 03:51:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6805c531-16c3-3d6f-9459-01f543ee84e3 | -18.21765 | -45.58196 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 451c635b-e6f2-3a4a-af29-0538a9eca3f4 | -22.09066 | -42.17488 | 2025-08-29 03:51:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d3791539-86bd-39b3-854b-20e219f1c5cf | -24.16981 | -49.57762 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 95457c56-c517-3cfb-b7dd-664e7242b6d3 | -22.49019 | -44.15823 | 2025-08-29 03:51:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d2d7f9d6-d518-3ad8-b42d-b9d641bca460 | -18.2149 | -45.57344 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fd15a99-9814-3f1a-b6ae-cbf9a975df68 | -20.00451 | -44.75013 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e346009-dc0c-3789-882f-fb3094bfd10b | -18.28651 | -43.84842 | 2025-08-29 03:51:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6a30606-d74e-3726-8b25-cacbc29bf2c0 | -23.67047 | -51.82034 | 2025-08-29 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 055d619d-b589-3231-9b14-6bb7dfcb108a | -18.21832 | -45.57854 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb9b3bdd-0520-385c-811f-6370cad56425 | -20.24083 | -45.74259 | 2025-08-29 03:51:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44503826-534d-32d1-80e2-775886d0ed7a | -20.67437 | -44.82248 | 2025-08-29 03:51:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 461ad2d6-63ce-3ec6-9004-124c6c21c180 | -24.16903 | -49.5732 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8aee0e74-56f8-3ac0-8c6e-cda5ba98c991 | -20.61087 | -45.11772 | 2025-08-29 03:51:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ee1b00e8-cd0d-355b-9a3e-fc6bfd0b142c | -20.37141 | -43.97172 | 2025-08-29 03:51:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89a146c5-d1c2-3ed0-a79f-8a7d14185bbc | -24.17141 | -49.5624 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 24cc37e9-e035-3431-bd34-d744596cfb49 | -24.16666 | -49.561 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 070c41e7-070e-3e3a-9bac-371612d71ec7 | -19.94844 | -45.0917 | 2025-08-29 03:51:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5bd23f3-468c-347a-abc9-e197432479be | -21.14101 | -44.21415 | 2025-08-29 03:51:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cc160b0a-a0ba-3705-99f8-89d26e9188bd | -24.16739 | -49.56519 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 79be1039-e157-323d-b045-b62c2c4e5305 | -21.0264 | -44.79772 | 2025-08-29 03:51:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dc4918c4-5444-3846-ad7d-0b6b251a424e | -20.9994 | -42.79318 | 2025-08-29 03:51:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4cf4fb1a-e344-3065-a43f-3c4e71916131 | -24.165 | -49.57644 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 933bf50c-255c-3415-b83c-301e0353f411 | -18.21755 | -45.58266 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0b6c555-fb4f-32a4-815a-becdc20eab64 | -19.90717 | -43.8414 | 2025-08-29 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 53ba77dc-173e-3b62-8d2b-d8907de16729 | -18.30763 | -45.13439 | 2025-08-29 03:51:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d64daed2-3635-36c5-9b96-376d446a5595 | -20.49714 | -42.33438 | 2025-08-29 03:51:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1cbd61f4-ea67-376b-aace-b8ab817860b1 | -18.21506 | -45.57277 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d1663fc-0c3b-3e48-9df1-66bf449d53f9 | -20.56001 | -43.84881 | 2025-08-29 03:51:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d8a4e7a6-8194-3908-9d2a-5806e522546c | -19.11516 | -46.68699 | 2025-08-29 03:51:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dcff8f1-b264-3468-8c3b-a9f6e928821a | -21.56402 | -45.12576 | 2025-08-29 03:51:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f5da9074-7ef7-3c35-9a38-6b82cd4aac70 | -19.66273 | -43.86007 | 2025-08-29 03:51:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68e83bcb-d8de-3c99-979b-f0042112f521 | -18.15899 | -47.92273 | 2025-08-29 03:51:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57548fae-faf5-3bc6-bac9-8be6eb994f38 | -20.0045 | -44.7519 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71942f8b-5a9c-3035-8761-3293a0591e83 | -19.80606 | -45.12708 | 2025-08-29 03:51:00 | NOAA-20 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6db5348d-d869-38fe-b9ae-08ac4e30adb5 | -16.27655 | -53.62154 | 2025-08-29 03:51:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b045ad6c-e7c9-396c-b635-f14e2b471350 | -19.73813 | -45.84381 | 2025-08-29 03:51:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| effb0e71-4b02-3993-baaf-4669f59be250 | -21.56264 | -45.12861 | 2025-08-29 03:51:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 037b060a-7c17-3e51-8374-4c99beca05a1 | -19.40038 | -41.44509 | 2025-08-29 03:51:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README37.md)
