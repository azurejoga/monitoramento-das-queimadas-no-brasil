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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d4fb369-f7f7-3c52-b365-bb95b52a414f | -4.45255 | -43.25032 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcb3a145-a048-3bb1-9c37-34c542c7c417 | -5.90262 | -46.23656 | 2025-10-22 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bb36fe6-01f9-36fb-b988-817f0a8247c3 | -8.17132 | -34.98111 | 2025-10-22 03:34:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6a757592-1f23-3bc9-9e29-54b7cab4e0c2 | -3.66522 | -40.48458 | 2025-10-22 03:34:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 517eaf71-1301-38b3-a1b6-456468d157ad | -4.39608 | -43.30244 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2a0821e8-512f-36c0-9653-244209f53303 | -6.30127 | -38.52388 | 2025-10-22 03:34:00 | NOAA-20 | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5b126d7a-9509-34d6-a78a-2b0ed31d9e18 | -7.07746 | -44.11029 | 2025-10-22 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5ea7937-2347-3e4f-bb82-6ea17bbff572 | -5.30118 | -35.97707 | 2025-10-22 03:34:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a84e952e-90e4-35e9-8bf6-a76744f3d627 | -3.4506 | -41.84846 | 2025-10-22 03:34:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3c7bf13-ed42-39e0-a9c8-967858e70779 | -6.30167 | -38.52367 | 2025-10-22 03:34:00 | NOAA-20 | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3083afc5-a2c3-3ac3-bcb0-347fa33b372c | -7.64232 | -34.88865 | 2025-10-22 03:34:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e902dc41-7830-389c-af1b-f323757aa085 | -4.38888 | -43.30958 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a0c6d02-12b9-3645-823f-c93955babcca | -7.11188 | -45.36215 | 2025-10-22 03:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f91e5312-6114-337e-845f-494856717130 | -7.11283 | -45.35701 | 2025-10-22 03:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72fdfb44-c107-3473-a5a6-6e1b9e96a195 | -3.44532 | -41.84741 | 2025-10-22 03:34:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c58220dd-fd2d-33a2-ba02-54842a38ca9d | -3.99301 | -43.2848 | 2025-10-22 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbae05c5-9fe2-3995-b914-bcef593e2c5a | -7.43734 | -35.18788 | 2025-10-22 03:34:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a84d468c-44c1-3fe3-9f1e-93f9690bb4c0 | -4.90705 | -37.20041 | 2025-10-22 03:34:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 253010f0-aa3a-3720-b0a8-117473d15f43 | -4.45462 | -43.23844 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 0602d676-dc37-39c6-a17a-a598150da858 | -4.83716 | -42.11559 | 2025-10-22 03:34:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9a968c3-981e-3e27-82e7-848f2f16eaa7 | -7.63484 | -42.17657 | 2025-10-22 03:34:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f453e856-dd56-3991-bdec-194c2c871bd7 | -4.3896 | -43.30555 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a7501150-2e3d-3971-ade6-1944c6dbf444 | -7.63539 | -42.17352 | 2025-10-22 03:34:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a04ee7de-0969-3638-9473-1b00879fe0ce | -4.44889 | -43.23742 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| cd7b324c-0bc7-35c1-a27d-693d9c197506 | -4.4553 | -43.23447 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 6e155bea-96a6-3b0b-bd6d-271b944057aa | -4.38816 | -43.31362 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a96e176b-c8c3-30a9-a51b-cdb6d68df706 | -3.23323 | -42.0762 | 2025-10-22 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 635ab198-1512-36a0-aa67-c6c5c98ee862 | -4.45324 | -43.24636 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 803c0d7e-214c-320b-a0bf-66db8a053784 | -5.15485 | -37.64479 | 2025-10-22 03:34:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d6c674c5-4648-356d-9bcc-dc2715a503c4 | -8.32668 | -35.8693 | 2025-10-22 03:34:00 | NOAA-20 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a46e343-bf8d-3003-b930-1f0c0c5b0325 | -4.39031 | -43.3015 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f89a5c45-830f-3bc9-ad17-6eec4851727e | -5.90546 | -35.64087 | 2025-10-22 03:34:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f2ec8f1c-4a0b-3c6a-97ba-6446ef5863a4 | -5.24086 | -37.73247 | 2025-10-22 03:34:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64555256-9400-323b-b40d-5416ba407681 | -7.07161 | -44.1095 | 2025-10-22 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19e76349-bb7e-3b09-a412-f2d0c48ee45b | -4.44821 | -43.24136 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 509267fa-2f11-3422-b7a9-37cfa41c2d29 | -7.87496 | -35.2578 | 2025-10-22 03:34:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10d45234-c8ec-39b9-a59b-35d3b9b8a17b | -6.53557 | -44.3672 | 2025-10-22 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f661c36-7f2f-3efe-87e9-0ce12635edba | -5.65672 | -38.30873 | 2025-10-22 03:34:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8aa4725d-419e-3314-9c5d-c9904916ef79 | -4.44752 | -43.2453 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| c494ae17-18cc-358d-a1b3-fe53bbd3297d | -5.66018 | -38.31285 | 2025-10-22 03:34:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 163481ec-4d49-3389-887f-f8406cf69854 | -7.07675 | -44.11416 | 2025-10-22 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb9d168c-c73e-3772-929d-22014e02737e | -5.90396 | -35.63924 | 2025-10-22 03:34:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4f7f3c7-6510-3bee-8d4e-587c7accd9f9 | -4.83188 | -42.11469 | 2025-10-22 03:34:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9cff87a8-2c0e-3e73-a459-260f980c3c52 | -3.23382 | -42.07276 | 2025-10-22 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0306d90-a597-3d20-b18d-53a01365f27d | -4.45393 | -43.2424 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| fada498e-db15-3de2-abef-990052fba255 | -7.9033 | -37.05956 | 2025-10-22 03:34:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f700608b-7e7f-3bd2-a300-cde083a8906e | -3.44476 | -41.85076 | 2025-10-22 03:34:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 207c2bd7-e8f4-3dda-be58-3bba57108971 | -5.06666 | -40.47501 | 2025-10-22 03:34:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 7ae4c7fc-4586-38e5-8c2b-daa819aed67e | -3.13881 | -39.65486 | 2025-10-22 03:34:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e831fb26-a28d-38e3-bd32-afed7ff85b53 | -6.99815 | -38.2679 | 2025-10-22 03:34:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bf0a13bf-a7d0-3f5c-97f9-69f96e4d62c2 | -3.99329 | -43.2832 | 2025-10-22 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fad16185-7425-360c-9e10-3cf86c996c78 | -6.64282 | -43.60697 | 2025-10-22 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 720a3ab5-ef13-3de5-81e5-58ab59614707 | -2.98908 | -39.96868 | 2025-10-22 03:34:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 13d2b4e8-af4c-363e-865a-deb56c7bd551 | -7.48301 | -35.05449 | 2025-10-22 03:34:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c68ae48e-df45-3a7a-872f-b717e1ab915a | -13.37601 | -44.41033 | 2025-10-22 03:36:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52baab46-df71-393a-a77a-0ae601d82c82 | -13.37465 | -44.40907 | 2025-10-22 03:36:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6252e13-f150-3352-9fcd-09a01dc4837f | -9.55813 | -43.0158 | 2025-10-22 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2325c40a-c053-3e51-87ea-279da732abaa | -13.37396 | -44.4125 | 2025-10-22 03:36:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0876da4b-fb3d-3745-b10e-61c7f212dff1 | -9.6226 | -40.33878 | 2025-10-22 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 777d0a16-c387-3f60-a9db-9531ab7b7cfc | -9.2774 | -35.62891 | 2025-10-22 03:36:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4ad17244-7830-3fbf-96e6-7ff3b50dfe92 | -9.62691 | -40.33955 | 2025-10-22 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2eb9ad6f-81fc-3c32-9028-35cad80f8f31 | -9.27402 | -35.62835 | 2025-10-22 03:36:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 031b3a85-3819-385e-a096-e4d58dd92acc | -9.62186 | -40.34294 | 2025-10-22 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8c77a2b7-619a-3d8e-9552-3f998911851c | -7.92881 | -46.01414 | 2025-10-22 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3cb58e2-96d5-33c3-9ca8-9df60ec34633 | -7.93426 | -46.02052 | 2025-10-22 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48e737d2-7db5-3b05-b582-52dbb270d95b | -13.37074 | -44.40913 | 2025-10-22 03:36:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8711d70-cd0d-3139-8eb4-faad29cda790 | -13.36937 | -44.40789 | 2025-10-22 03:36:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e12b5f0e-c80b-3d9c-9f10-4104abbe2440 | -7.92782 | -46.01936 | 2025-10-22 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1a6b641-ec0c-3509-b76b-a273e0e9be11 | -9.56273 | -43.01985 | 2025-10-22 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24e26b7a-37d0-389f-be22-b5f650a2f657 | -7.93922 | -44.8518 | 2025-10-22 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53801486-9bc7-3cb3-bb32-7325bc0b993a | -7.94008 | -44.84718 | 2025-10-22 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c24292d-841f-3bd7-8e87-8c09014b2206 | -20.44031 | -44.85765 | 2025-10-22 03:38:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad008f63-187a-3cc4-b156-7e8a48aa85f2 | -19.14557 | -46.34283 | 2025-10-22 03:38:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56fe250e-7404-3c59-875c-bd9db2861871 | -21.24502 | -45.14193 | 2025-10-22 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6bf68a69-6722-3193-8197-fb0fbbab78ca | -20.56686 | -45.89227 | 2025-10-22 03:38:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e992dfb3-b9bf-3dc5-8f56-f5224d495616 | -18.65128 | -49.09008 | 2025-10-22 03:38:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87fbb860-cceb-3975-a7f7-1d40e442ac0a | -20.30006 | -46.54719 | 2025-10-22 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e21a434-f136-3eac-b09d-e02e255a99b8 | -19.09209 | -44.34369 | 2025-10-22 03:38:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0136683f-7920-3475-951d-b5314ced9f37 | -18.64992 | -49.09587 | 2025-10-22 03:38:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f5c5d92-e510-3095-bde6-5044ab7f5cd8 | -20.75334 | -43.21542 | 2025-10-22 03:38:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 944d25a4-b914-330a-86f9-41b46ea246dd | -21.21603 | -45.0653 | 2025-10-22 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 415e746c-3f3f-3932-9593-cce141e44108 | -19.15093 | -49.12667 | 2025-10-22 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 653d0139-0d50-3297-b381-412301140ee6 | -19.91161 | -46.11895 | 2025-10-22 03:38:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dadbb04e-4002-3b44-96c2-de422206ffe1 | -18.11137 | -48.53573 | 2025-10-22 03:38:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c7983d4-d396-3892-9d41-210b0456d310 | -17.62077 | -46.61712 | 2025-10-22 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad81e44f-6e25-31b4-9ce4-e070b2d13fa0 | -19.15829 | -49.12364 | 2025-10-22 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f518ff3-fe65-337a-88dc-7e71a634d529 | -19.8708 | -46.3345 | 2025-10-22 03:38:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdb89a8b-7b83-3223-baab-9d197a55786e | -20.30086 | -46.54346 | 2025-10-22 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b5ae709-0254-37e9-8a3d-d1caed0059ff | -18.33703 | -49.51012 | 2025-10-22 03:38:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e0e98597-40f1-3780-898e-76973c761e89 | -17.6398 | -46.63822 | 2025-10-22 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f74a85a-701e-3ade-a387-9770bbd2b7c9 | -19.91085 | -46.12246 | 2025-10-22 03:38:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72622f28-b3fe-3c05-be64-7da816c839b0 | -19.15587 | -49.13413 | 2025-10-22 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0689cc84-f899-3539-99de-a52352092859 | -20.76039 | -43.22497 | 2025-10-22 03:38:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 974347b2-561b-3102-b69b-a9bc2f35581a | -17.62636 | -46.6185 | 2025-10-22 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b244b8ee-5b46-33a1-bc79-8fa5b9731a67 | -18.1126 | -48.53022 | 2025-10-22 03:38:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8e44e68-a68e-3e03-9823-e38c5d46aa45 | -17.6572 | -44.30751 | 2025-10-22 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3374c177-424c-3894-b113-9c0995b19c69 | -19.87152 | -46.33117 | 2025-10-22 03:38:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3728b23-2f83-3f16-88ca-910ffc65c4ca | -19.15705 | -49.12901 | 2025-10-22 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8933c5b8-f734-3a33-b80a-69251cdee08a | -20.03649 | -46.70713 | 2025-10-22 03:38:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af2936e7-a2f1-3634-b4af-48b8843c66e2 | -17.72854 | -44.74761 | 2025-10-22 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
