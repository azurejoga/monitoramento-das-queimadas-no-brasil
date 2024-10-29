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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 990ad257-d347-3075-90c4-77a524ab0088 | -12.3522 | -49.94 | 2024-10-29 02:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a0ddc0cc-232a-3a82-8725-f01d52cb0d70 | -12.3526 | -49.9184 | 2024-10-29 02:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 24a863e8-65c2-3573-b679-04f2a2743aa1 | -13.6028 | -45.587 | 2024-10-29 02:26:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a35f3612-7af9-3acb-a6e2-d1be2a903a42 | -13.6887 | -46.1247 | 2024-10-29 02:26:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2fbd00ff-d897-35af-bd5b-28829bb88d1f | -13.6891 | -46.1017 | 2024-10-29 02:26:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| eaebf304-d40b-32fc-9c09-44d05cbe6b2c | -14.1386 | -44.09 | 2024-10-29 02:26:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1808367e-1984-3285-a2ce-88985e4dc403 | -14.1391 | -44.0662 | 2024-10-29 02:26:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 22cce025-b22f-3feb-8a60-b4608764ddf4 | -2.3537 | -48.9133 | 2024-10-29 02:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2f5a3ffa-4b2d-3a6e-aea2-0a645bd4acd7 | -2.3353 | -48.9137 | 2024-10-29 02:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 03d1b279-ec18-3f26-b6c8-dc3bd0056003 | -3.1098 | -54.2665 | 2024-10-29 02:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| ce399e76-b9b6-3b4c-b228-4920b812a157 | -3.1097 | -54.2865 | 2024-10-29 02:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 168.5 |
| fc2fa3c8-58df-3bdd-8a70-1dd10c1cf150 | -3.0913 | -54.287 | 2024-10-29 02:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 57b73bed-7487-3d19-8f1d-e40f6c7825bb | -3.3044 | -47.198 | 2024-10-29 02:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cc75b068-b595-321a-b3d7-0b360c785614 | -3.2503 | -46.8709 | 2024-10-29 02:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 9feded2d-e409-3283-b6e7-b23d0f3e3fd8 | -3.1794 | -50.3922 | 2024-10-29 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4a6fb246-c13b-36a5-acf3-16bd232fab50 | -4.2948 | -46.0946 | 2024-10-29 02:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f6a4d4b4-325a-34b0-a667-60ba95324ef5 | -4.2763 | -46.0733 | 2024-10-29 02:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4b464e68-154e-394d-b47c-6bb84e26a6ca | -4.2762 | -46.0956 | 2024-10-29 02:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 559.5 |
| 803879a1-6e0e-3751-9717-0f580271046c | -4.2761 | -46.1178 | 2024-10-29 02:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 403.5 |
| eda60fee-939a-3cfb-9e5b-2941a320d488 | -4.2576 | -46.0965 | 2024-10-29 02:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 48497a80-9567-3ab3-afe8-cd36a0da7758 | -4.2575 | -46.1188 | 2024-10-29 02:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 119.0 |
| b71972ef-3f66-38e6-9850-eb88a017dcfa | -11.138 | -55.5313 | 2024-10-29 02:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ef5b90ba-39a9-3563-82a5-86b6e1d31b5b | -12.3331 | -49.9424 | 2024-10-29 02:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 046fc10e-bf29-32ba-b519-8b05fb2f9675 | -12.3522 | -49.94 | 2024-10-29 02:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6c3812be-2d20-3feb-9baf-a4ad40d1ce85 | -12.3526 | -49.9184 | 2024-10-29 02:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| bb19cd05-1047-300d-8f82-c4e724f45554 | -12.3334 | -49.9208 | 2024-10-29 02:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7e277034-c53a-39d4-ad83-a55e494accfd | -13.6028 | -45.587 | 2024-10-29 02:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| efafab31-2456-3521-9793-a87aea754dbf | -3.1098 | -54.2665 | 2024-10-29 02:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 050b7a88-c258-36cc-92ee-737e12459b93 | -3.1097 | -54.2865 | 2024-10-29 02:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 71a3c860-f75d-3c4c-be1e-0d7433c3c0e0 | -3.0913 | -54.287 | 2024-10-29 02:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 252403be-08fc-32b7-8570-f84b973c3664 | -3.0501 | -50.4171 | 2024-10-29 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 701d6ff9-a161-345a-99f6-e50d3d0c4b2c | -3.3044 | -47.198 | 2024-10-29 02:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| cf8b5e09-7f73-33a6-9fe9-215c55e4271f | -3.2503 | -46.8709 | 2024-10-29 02:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 07685dc4-0659-32db-9c89-7b308b1fa193 | -3.1794 | -50.3922 | 2024-10-29 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 01eb2341-864b-321c-8804-c40f380ea1fb | -3.1281 | -54.286 | 2024-10-29 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e9877b75-1ace-368f-9580-ea24ee1c002b | -4.2762 | -46.0956 | 2024-10-29 02:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 596.2 |
| df3b7703-d210-362f-ac0c-dae2ee1a3cd0 | -4.2761 | -46.1178 | 2024-10-29 02:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 377.2 |
| 9aa81276-de1c-3870-a064-6211427ea1dd | -4.2576 | -46.0965 | 2024-10-29 02:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 209.8 |
| b59f3262-27ca-378f-8c2d-736874b8bab5 | -4.2575 | -46.1188 | 2024-10-29 02:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 143.5 |
| c0c1745c-b642-35ff-a4bf-b4dbae263191 | -4.366 | -43.778 | 2024-10-29 02:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 374ae486-cab7-3c46-b793-3e1644279842 | -4.3475 | -43.7559 | 2024-10-29 02:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 1cc84810-3b3d-3844-89ae-63c10d3597f4 | -4.3473 | -43.779 | 2024-10-29 02:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 1c2e2972-6495-3b5a-a8f6-8079e5f0125c | -4.3286 | -43.7801 | 2024-10-29 02:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b5695866-24a4-3e8d-bec9-2427b15338a2 | -6.6143 | -47.3853 | 2024-10-29 02:45:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 377607cc-bbcc-3288-b525-4938993ade7b | -12.3526 | -49.9184 | 2024-10-29 02:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e71b465a-0be6-3522-9fe4-06942635fa8b | -12.3522 | -49.94 | 2024-10-29 02:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 31b1bc9a-969c-3e1e-bfa0-61473ac26d75 | -2.5251 | -47.442 | 2024-10-29 02:55:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8101dde4-a88c-3ff6-b64c-36734b2992b9 | -2.8555 | -53.3459 | 2024-10-29 02:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f7ed56a2-f79d-3f03-8ad4-b8adaf790d05 | -3.0501 | -50.4171 | 2024-10-29 02:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d9419ab9-e446-35c4-ad61-c93b7bfdf259 | -3.1097 | -54.2865 | 2024-10-29 02:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 2b9055ea-9ea2-3977-bcec-a32bfbc3abb2 | -3.1098 | -54.2665 | 2024-10-29 02:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 81761f87-b73e-3956-bb20-ad7e994c8d51 | -3.2503 | -46.8709 | 2024-10-29 02:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| b1ae0abb-2078-38e1-9559-00a8b0ea7251 | -3.2688 | -46.8703 | 2024-10-29 02:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 568e1f6d-a10f-3a19-bda6-d147009e333f | -4.3473 | -43.779 | 2024-10-29 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 91e9b845-6968-373d-b8c7-17ef2bb39d3f | -4.3475 | -43.7559 | 2024-10-29 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| f1618a44-2df2-3cc0-b1e4-f8ee52964c77 | -4.2575 | -46.1188 | 2024-10-29 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 122.8 |
| ae03990f-cd0d-3db5-850a-cfe71505c4c5 | -4.2576 | -46.0965 | 2024-10-29 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 8194f70e-86aa-3050-8230-582aec03b636 | -4.2761 | -46.1178 | 2024-10-29 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 8b323d1d-9f9d-3738-abf9-3fac59c62acc | -4.2762 | -46.0956 | 2024-10-29 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 335.4 |
| c2db2c89-46fc-389b-889d-b425459a01ff | -4.2947 | -46.1169 | 2024-10-29 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 036da098-c0b8-3713-81a3-9819a9151a04 | -4.2948 | -46.0946 | 2024-10-29 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6f3fe996-e7f9-3ba2-a5e9-e47cf1840096 | -11.138 | -55.5313 | 2024-10-29 02:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9a57b85d-44bd-31a1-bc1b-f993dd78dcd7 | -12.3331 | -49.9424 | 2024-10-29 02:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8cfb2d58-59b5-3c97-ab43-bf9ebb8726fd | -12.3334 | -49.9208 | 2024-10-29 02:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 5a82d874-2aa7-39fd-8d8d-303b462f33bc | -12.3522 | -49.94 | 2024-10-29 02:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4816a095-3b40-3f34-934c-882d4b24fb56 | -12.3526 | -49.9184 | 2024-10-29 02:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5d9708c6-d2a4-362f-b2bd-51f8872ba4a1 | -13.6028 | -45.587 | 2024-10-29 02:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1d397efe-efec-3020-aadd-c3cd717d6e03 | -13.6887 | -46.1247 | 2024-10-29 02:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 64a014c0-5d2e-3984-81f1-d24c832629b8 | -13.6891 | -46.1017 | 2024-10-29 02:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3649a3b4-29db-30a8-8723-050bde776e6b | -6.82517 | -35.23615 | 2024-10-29 02:58:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6982ea09-58bf-3b5c-bf91-b0d8d84ded98 | -17.17059 | -39.42855 | 2024-10-29 03:02:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d1ce75ea-84ea-344b-a3b8-ec188075e15b | -17.17029 | -39.43013 | 2024-10-29 03:02:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 789c709b-61fb-35ef-abd1-86861f7bafe1 | -17.16946 | -39.43362 | 2024-10-29 03:02:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1cf298ae-d8bd-3a5f-a3b8-755d93606f7f | -17.16384 | -39.42871 | 2024-10-29 03:02:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ca294fac-4769-3056-9e90-9c05053e3cd5 | -2.8555 | -53.3459 | 2024-10-29 03:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 145245aa-e441-32d8-9927-6a4e0f91bcbc | -3.1098 | -54.2665 | 2024-10-29 03:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| c9ce950c-4a99-3312-bba0-5e653c9c8b35 | -3.1097 | -54.2865 | 2024-10-29 03:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 032a56ad-60ca-36ab-a3f6-53afd5ad88c3 | -3.0913 | -54.287 | 2024-10-29 03:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 573979b9-acf4-3780-a798-6e9a36b505ce | -3.0501 | -50.4171 | 2024-10-29 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 802c99ae-9cc9-3bfe-b326-45aee34495de | -3.2688 | -46.8703 | 2024-10-29 03:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9b502716-4e40-31ac-b5fa-c298f83dd791 | -3.2503 | -46.8709 | 2024-10-29 03:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 3938f7c5-1a0a-3299-8a9c-07b0890e4242 | -3.1794 | -50.3922 | 2024-10-29 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e8d144c8-2415-3552-b6f6-427f93a74d1b | -4.2948 | -46.0946 | 2024-10-29 03:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8fb50af0-cf5d-3e15-9fcb-c2e6af255674 | -4.2762 | -46.0956 | 2024-10-29 03:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 230.3 |
| c9610b72-cc98-3d91-b294-6288f5eac0c9 | -4.2761 | -46.1178 | 2024-10-29 03:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 9598feeb-c6b6-33db-86c8-862650063e03 | -4.2576 | -46.0965 | 2024-10-29 03:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 127b9d23-38d7-3001-b750-0286b0cb0f07 | -4.2575 | -46.1188 | 2024-10-29 03:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 724cd76e-0201-3eb8-82cc-3ffc81454c31 | -4.3473 | -43.779 | 2024-10-29 03:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c87505ff-e904-366b-8533-63ccd479455b | -12.3526 | -49.9184 | 2024-10-29 03:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 34882e19-2b6a-37e8-8551-8899c042ca27 | -12.3522 | -49.94 | 2024-10-29 03:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9c6555ad-2fd1-32b1-aa8c-380548968a77 | -12.3334 | -49.9208 | 2024-10-29 03:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b98113f0-3d22-3572-8668-777a88160d9a | -12.3331 | -49.9424 | 2024-10-29 03:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 051dbc3a-182f-3024-9aa7-dff6b26f67b0 | -13.6887 | -46.1247 | 2024-10-29 03:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 67a52457-10dd-3fe6-b8cb-589c0d01402d | -13.6222 | -45.5838 | 2024-10-29 03:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 37d33169-4424-3a99-ad43-a00a7eeb4bc8 | -13.6028 | -45.587 | 2024-10-29 03:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 77a9bb3b-7690-311a-a650-c7fb9f89d342 | -3.0501 | -50.4171 | 2024-10-29 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a318425e-9c56-33ea-afdf-c578bce64706 | -3.0913 | -54.287 | 2024-10-29 03:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1184840b-2706-3aca-ae8a-5b456425ceec | -3.1097 | -54.2865 | 2024-10-29 03:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| d7bad90e-d361-3c3e-b78f-3e2a45b67bc8 | -3.1098 | -54.2665 | 2024-10-29 03:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f8f55402-e624-31a9-ac97-e033ec0ed356 | -3.1794 | -50.3922 | 2024-10-29 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |


[Clique aqui para ver as próximas entradas](README22.md)
