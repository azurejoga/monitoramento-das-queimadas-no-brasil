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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d340629-bc91-30bb-8bf1-e777237672ad | -12.9628 | -46.7626 | 2025-06-06 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| e25405ba-b244-3017-abd3-fad2ee463f96 | -12.9628 | -46.7626 | 2025-06-06 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 0ffd316a-2d5d-3b1f-92c7-8c2694c5fe57 | -12.9623 | -46.7853 | 2025-06-06 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 339c5ffc-0943-321d-adaf-cf419d67b28b | -7.0169 | -44.5954 | 2025-06-06 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| dde5c8cf-6678-3fdb-9b79-f5c913f9b73f | -7.01009 | -44.60511 | 2025-06-06 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 85ab6c03-6892-324b-9276-150ad285a73b | -7.02097 | -44.60125 | 2025-06-06 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b6d57dd-bc26-31ea-b05e-d2ce3ef1cd20 | -8.07418 | -34.97769 | 2025-06-06 03:21:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e975fd4-4c46-38b9-afc3-e8c3250f01f4 | -7.20899 | -43.13405 | 2025-06-06 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fa2124cc-2b1e-3385-a6a3-778df50b91c9 | -7.72162 | -44.18296 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f003def1-df6b-3f0c-b13b-b097a01979c3 | -4.00087 | -43.24586 | 2025-06-06 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f39e87c-eac1-360b-8ce0-e507e54dfd25 | -7.72753 | -44.18587 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7443c762-2c76-30cb-b733-5609c70e69d8 | -7.20242 | -43.13286 | 2025-06-06 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9e12cd98-380e-3e40-9e70-34ae83dd5579 | -7.72287 | -44.17639 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9044de97-085d-3d8a-8e4a-b7be0b6fff15 | -7.72881 | -44.17929 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48ce27bd-541f-379e-90ac-567410a90077 | -7.00867 | -44.61266 | 2025-06-06 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a75cfb2e-841c-38a1-aad4-43b2aa9cbf66 | -7.01107 | -44.614 | 2025-06-06 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 777b9cef-cda8-363f-9ffb-cb71ba47921d | -7.00511 | -44.60646 | 2025-06-06 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b68e359d-93ec-33c8-b520-7a1ea2ee44c3 | -7.20384 | -43.13549 | 2025-06-06 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43483189-0c5c-3fe6-8e3b-a73f5f0b8669 | -7.71626 | -44.17017 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bae728c6-5311-33aa-addd-3bbc9aff42c1 | -10.65053 | -44.49563 | 2025-06-06 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1e056bd-0961-32a0-b9eb-b9284195da86 | -7.72853 | -44.18433 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eebaba25-8159-3f3e-a234-d0aaff772c98 | -7.19728 | -43.13424 | 2025-06-06 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fdecbb15-022a-32d1-b051-691023d3f180 | -6.95394 | -42.06958 | 2025-06-06 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1925bdbf-9a2d-3c74-9d99-ede972e00df2 | -7.71497 | -44.17672 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e608f60c-3501-36ac-9feb-7ab04b751340 | -7.43369 | -37.21041 | 2025-06-06 03:21:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3010edd3-f18d-316b-b8b9-79b9443c5d3e | -7.7219 | -44.17798 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54086f39-73d4-30b7-bef3-fd5a49d23b7e | -7.71594 | -44.1751 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 54ae2892-350f-3979-8df9-33a6f54de318 | -3.99392 | -43.24464 | 2025-06-06 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad97520d-3817-36f4-bc09-af0b912b0c80 | -7.0125 | -44.60664 | 2025-06-06 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8c07cfd3-0058-3316-98a3-82e0b50646fe | -10.64799 | -44.49578 | 2025-06-06 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0314abb4-4bed-3f33-a2e7-3d7d3d7e95a0 | -7.01861 | -44.59919 | 2025-06-06 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc607139-1aea-3553-a0e2-ba156d6e5323 | -7.20132 | -43.13866 | 2025-06-06 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 000b2e63-2ff9-3433-899c-d3f47229e788 | -7.72978 | -44.17775 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ef2120f-131c-3a77-b844-5e057a92ad40 | -7.19474 | -43.13747 | 2025-06-06 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cab249f7-a908-3876-9933-b9c77f44d5cc | -7.71754 | -44.16363 | 2025-06-06 03:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ce9978e-1c0d-3ded-bc89-0e134bc0ec86 | -14.73527 | -45.10041 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ff28ab7-ab43-3b6f-98c7-79bd5bb519ba | -14.90283 | -45.99615 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd27e9ff-829c-3448-95e9-e767714ceacc | -14.73014 | -45.09287 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f315d29-b161-3274-939f-3fdf7b5f9766 | -14.23104 | -45.4935 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 479c8615-13a4-34d4-b11a-551b9f85a51a | -14.73162 | -45.08961 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e324c586-0368-3fec-b1cf-2c413b920af0 | -17.25116 | -43.64138 | 2025-06-06 03:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 279c69fb-cb38-3f43-a617-aefb1d36f471 | -14.12533 | -44.83532 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc8a9594-0e31-3ed6-af68-6c78e24af00d | -14.223 | -45.49817 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1491dcd2-93ea-3b34-9dd8-d05ba5ac8da9 | -12.15762 | -43.20843 | 2025-06-06 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12964b74-96a9-3ead-83c3-1ddbf69e8c0a | -12.15857 | -43.20372 | 2025-06-06 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 854fed4a-f118-34c0-8640-eb8537c5ea0b | -14.73137 | -45.08732 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4f35f5e-f855-368e-80f2-fe76d73a0a52 | -14.11888 | -44.83391 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f0ffd9a-6c90-3614-ab7f-5cc081100187 | -14.74199 | -45.10466 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18df0d0c-8d81-3b76-8d8d-edf1701e8354 | -14.73682 | -45.09704 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a44cf11-a9eb-34f3-9569-fd0158d865a1 | -14.22865 | -45.49273 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f07a609-8eb2-33fa-8b45-1a18c2dbef66 | -13.64081 | -44.44891 | 2025-06-06 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 458b5e7d-7cbd-3cb5-a54b-fbdc8aa8b158 | -14.22198 | -45.49121 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72d2111c-4b3f-3aa3-9784-8b393c8c7d64 | -14.23239 | -45.48735 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b1b8a8e-054a-3bfa-a830-113f4e93172c | -14.73654 | -45.09466 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e66c737-0bd2-3a75-8038-5b885e4ce858 | -14.22436 | -45.49199 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83642532-faeb-3c00-bff4-0eea38b57813 | -14.22066 | -45.49738 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30cbda94-f233-3802-9225-94a137263876 | -14.74167 | -45.10221 | 2025-06-06 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17ebd4d7-1ee0-35a5-b7a3-1199c6b3e4e4 | -14.22997 | -45.48657 | 2025-06-06 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 258fe9de-128a-36c2-b352-af114782319a | -19.83901 | -40.08221 | 2025-06-06 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 77a4c9e3-72e8-3be6-b822-3cb75e319808 | -17.75297 | -42.89519 | 2025-06-06 03:25:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1dd1195-aa22-3ee3-ba82-6201b6d4c9e3 | -19.24274 | -45.02115 | 2025-06-06 03:25:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4776ad5d-68ff-306d-8927-22e825eaf2fd | -19.2438 | -45.01644 | 2025-06-06 03:25:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 342e1505-004d-3319-9656-897306b454cf | -20.09261 | -41.34164 | 2025-06-06 03:25:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1cf0aadc-5d65-3311-abea-c30df738bc2e | -11.9214 | -54.8117 | 2025-06-06 03:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 98d49282-2595-3f5f-ae43-929884c53144 | -7.0169 | -44.5954 | 2025-06-06 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| ef98d939-09c1-3c34-8b27-fc12d725d031 | -7.0169 | -44.5954 | 2025-06-06 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 2fbfd7a7-338e-3d58-96c2-3bb4e66b058b | -11.9214 | -54.8117 | 2025-06-06 03:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 9ddbc38a-7fbd-3556-a1db-6832cd03eca5 | -7.0169 | -44.5954 | 2025-06-06 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 1ac60999-450f-34a9-a017-25ac33b46155 | -11.9214 | -54.8117 | 2025-06-06 03:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 32288975-4cf0-3ac0-848b-102c2b2e9942 | -7.0166 | -44.6184 | 2025-06-06 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 27367089-5054-3ff9-8ea6-e4509c83fd3c | -7.0169 | -44.5954 | 2025-06-06 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 96a48e4f-d2e9-353b-8f4c-c966c1c50a06 | -7.0169 | -44.5954 | 2025-06-06 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 59058d90-6d5f-3032-8373-dc17c27a2c32 | -3.13801 | -41.79008 | 2025-06-06 04:12:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc2c1137-5596-3654-9294-c0b2a1fa6a41 | -3.41904 | -44.31125 | 2025-06-06 04:12:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fffba67-f58d-3179-a795-f5477cd9feed | -3.13033 | -40.98781 | 2025-06-06 04:12:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e967b51d-2002-3958-9350-b026abf0c011 | -2.91851 | -48.23363 | 2025-06-06 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 466e67e0-d8e6-3d8c-aadf-fc790835d3fc | -2.94806 | -41.76373 | 2025-06-06 04:12:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d783d2a5-5ee3-33a0-9886-c48afe123e4b | -6.20445 | -48.54348 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cee6cfa8-c7f4-373f-935f-eb7b4c762099 | -7.90415 | -50.36353 | 2025-06-06 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 116b7603-b751-3ffe-8965-f38f585cf0ba | -6.66498 | -51.96059 | 2025-06-06 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 467f2bb1-e605-3497-b148-a9ace0dd16ca | -6.959 | -42.07039 | 2025-06-06 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 91531565-0dc5-378c-a651-d58783f52e4a | -6.46817 | -48.0263 | 2025-06-06 04:14:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0462661-99d3-3062-8f89-aa2cdaa6abca | -10.57226 | -45.98647 | 2025-06-06 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fa24206-00c0-37fb-8860-4721a164347f | -8.96409 | -47.97169 | 2025-06-06 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 017b9e0b-ea9b-38b5-99fd-02a5ad7e7289 | -6.96212 | -42.90545 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b6ffecf-0094-3e45-9698-81c88d29baa6 | -6.06562 | -44.23783 | 2025-06-06 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 255b5aa6-6356-3057-81ee-77f6508c4e95 | -4.42379 | -47.73187 | 2025-06-06 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd41a12b-6383-3ad9-becf-2c095e554c79 | -6.64096 | -47.35168 | 2025-06-06 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05acfda4-6930-3e36-9549-679795014713 | -9.6093 | -49.01985 | 2025-06-06 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c18662a-2ae7-3cc9-b7ae-7bf60c5de603 | -8.49592 | -43.91483 | 2025-06-06 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3708e892-269f-3946-ab64-0bae61a7111b | -9.20198 | -49.68612 | 2025-06-06 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 867a3cac-aac5-3bc8-8e87-8e5cdddb2509 | -8.66909 | -44.2628 | 2025-06-06 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82045bb6-1f57-324f-a22d-196b881cd95e | -6.1889 | -48.56036 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6c8ad87-40a0-3f5c-8509-5d31011719f0 | -9.39657 | -48.42643 | 2025-06-06 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f1320bf3-d4b2-3818-adc5-998afd96bbc6 | -7.5551 | -45.82246 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 102494cc-e531-34c3-bd31-1192a449d1f0 | -7.02331 | -44.59733 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f75ce4c5-1be7-39c2-9570-8bfb5e5367bb | -8.46778 | -46.48632 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52eed3d9-21e4-34c7-b691-6d5c039b8047 | -7.19915 | -43.13401 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db8df41c-eb9e-3b9f-8110-5fcfd2ce115f | -7.72029 | -44.1709 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6faef9b1-4551-3d06-acde-f774a9f5bd6d | -7.72581 | -44.17892 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README3.md)
