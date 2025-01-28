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
| 0b2b1570-9a24-331e-880b-25db29840cef | -29.61175 | -56.45542 | 2025-01-28 03:49:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 9ace111c-8183-3d01-9648-e8d4832de6ac | -29.6097 | -56.4627 | 2025-01-28 03:49:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| f6fa7068-3dd4-30dd-bf2d-14b22c006164 | -0.82761 | -47.45107 | 2025-01-28 04:29:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2299fa65-0584-3b2e-b086-26c419cbdb9b | -6.49826 | -47.48849 | 2025-01-28 04:31:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09ff8e20-1d50-36fe-8dc0-5225977dbe1d | -1.28341 | -48.44508 | 2025-01-28 04:31:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 864506c1-3416-3098-8335-ede35fe9b3ef | -5.44971 | -44.80484 | 2025-01-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5814ea2e-0aa8-36c0-aebf-3e792357c8ed | -5.02305 | -45.96838 | 2025-01-28 04:31:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62b49a5b-2dd0-3dd3-8e74-9d2976a12704 | -6.50156 | -47.48899 | 2025-01-28 04:31:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 910bd596-4f9d-3e6f-8e18-c4474a1ae462 | -5.44792 | -44.81679 | 2025-01-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8ac7b92-65b1-32b4-a65b-69c6c41fb320 | -6.21041 | -46.22247 | 2025-01-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1220f66-0543-3177-98b7-235ed2f94fed | -6.21095 | -46.21888 | 2025-01-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05d14e48-0b68-322e-96f7-9c76f076c959 | -7.26141 | -39.66274 | 2025-01-28 04:31:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 18b4629f-72bb-363e-a115-0781f28bad8a | -4.26512 | -50.52459 | 2025-01-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 757a7d89-1dc0-3570-acdf-b5dd709fb8bd | -7.26604 | -39.66641 | 2025-01-28 04:31:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91d919f4-c0a2-3e57-9583-56c963002af2 | -2.82331 | -49.01351 | 2025-01-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 619fda6b-16f9-348a-9671-79b3b689534e | -6.92524 | -47.78177 | 2025-01-28 04:31:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 512f46a1-2406-3cd6-9086-55096d9fb5a5 | -3.17455 | -48.69897 | 2025-01-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a3c739-bcd6-39b5-9b31-bfbbe53db7b6 | -5.27439 | -45.77333 | 2025-01-28 04:31:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4217c66a-a82c-33dd-94f6-0a4560be7f45 | -6.21432 | -46.21941 | 2025-01-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65279f48-bf16-30cd-bd49-e48548d9030c | -3.13686 | -40.04493 | 2025-01-28 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29cdfd6f-14c4-3a76-87e0-34aeaaf51e74 | -3.58628 | -53.70926 | 2025-01-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7dfc84f-3b25-3194-93be-fc24fe3419a9 | -3.24817 | -48.07611 | 2025-01-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0df30fc5-f509-33b4-ad34-3009388f2b3c | -6.00584 | -45.85695 | 2025-01-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8c40e33-69a7-3235-a035-f322a3d57a41 | -6.34159 | -47.09528 | 2025-01-28 04:31:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 082e62c8-5ca2-30a1-8c6c-5dd365e642b7 | -2.81234 | -49.01601 | 2025-01-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6c41d10-8a1c-3568-97e3-a8b9fe68b56f | -5.62644 | -44.83138 | 2025-01-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 555b6ff1-e643-33ef-958a-4aa1326c34c7 | -6.0064 | -45.85329 | 2025-01-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cf64b72-bae7-3976-9307-798bb36dcc8d | -2.90667 | -54.28857 | 2025-01-28 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 204a77e9-b772-3d8a-bafd-fd4d15e98d4f | -7.86456 | -43.08425 | 2025-01-28 04:31:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d8a0fd79-4205-382e-a5b1-9cae5dc2a679 | -2.81587 | -49.01615 | 2025-01-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f26a3440-a2d6-3768-bbe8-40f4bddec7fd | -5.27496 | -45.76968 | 2025-01-28 04:31:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c78302-f96c-3563-b0e7-9f66f160fde7 | -5.45144 | -44.81733 | 2025-01-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01b9643f-60b4-3b80-88f4-765dd80d89f4 | -6.52176 | -52.43408 | 2025-01-28 04:31:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6f550fc-4cdc-30d7-a013-8e5289c53746 | -5.39111 | -45.28836 | 2025-01-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b137c81-9849-339b-bdea-42de653d03a8 | -5.41722 | -47.56786 | 2025-01-28 04:31:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 275a3625-1f2e-3abd-bb0d-29976d02f5aa | -5.44911 | -44.80882 | 2025-01-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d35598e5-420f-3969-ab7c-1136d98aa941 | -5.6462 | -40.52877 | 2025-01-28 04:31:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00c3b53b-e9a8-3627-b29b-9e1d484f8714 | -2.81244 | -49.01561 | 2025-01-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f868fe1a-b91c-391a-be3c-3791ad09084d | -2.91133 | -54.28954 | 2025-01-28 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7df6ffe-27a9-317d-bbee-fd7967b06dbc | -3.45796 | -52.86204 | 2025-01-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f64c0ecb-d365-3523-bda3-f6fa810a6cab | -7.26643 | -39.66349 | 2025-01-28 04:31:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b405a47-92e0-3ffa-80c8-7edf9a859672 | -8.02805 | -46.63214 | 2025-01-28 04:31:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a614774-2cf6-3508-857b-049012af5b19 | -5.02361 | -45.96478 | 2025-01-28 04:31:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aed0e19c-219d-3e63-a1ac-63b2cecb61af | -6.34105 | -47.09874 | 2025-01-28 04:31:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b99e0608-6795-39b7-8cf1-5e7dc2a8109a | -2.81929 | -49.01669 | 2025-01-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20f93612-5da3-3d2b-bfef-754d30c38ade | -9.77959 | -42.00953 | 2025-01-28 04:33:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a628da33-83a9-3f11-b726-6dcb8cd8abec | -14.21285 | -47.01869 | 2025-01-28 04:33:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9647df2c-86ae-356f-9b43-d6072103a32f | -12.61534 | -52.46298 | 2025-01-28 04:33:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 083ab243-e551-3e88-b196-530367b11815 | -15.07815 | -48.94503 | 2025-01-28 04:33:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d02b074-9f2b-3b13-84b1-bb5ada859351 | -13.97004 | -49.62376 | 2025-01-28 04:33:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bb22f91-8804-3010-887d-72b5ecedfa7c | -13.96674 | -49.62322 | 2025-01-28 04:33:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a168762a-7d9b-3cb4-95a3-15fbe0f3b88b | -12.35422 | -47.99502 | 2025-01-28 04:33:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a54a4f5-2ffd-3d14-a623-43f491d01d71 | -13.10346 | -49.72397 | 2025-01-28 04:33:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cfef192-24c2-393a-9ab0-4fb5d991914c | -11.03025 | -45.06327 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c149d75-4c36-37e2-a33d-18e62363b464 | -14.5572 | -53.97722 | 2025-01-28 04:33:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20589c5e-d72c-3499-a468-20d1dd970347 | -13.23746 | -45.30853 | 2025-01-28 04:33:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e652e79d-2c09-3fad-aea1-7d86b8ba7bef | -12.77449 | -44.83592 | 2025-01-28 04:33:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a507683-d96f-3078-b9b8-942f0f091a58 | -13.10401 | -49.72044 | 2025-01-28 04:33:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb71fd5d-e193-3776-9e0d-543fc7f4ab37 | -10.6923 | -54.35755 | 2025-01-28 04:33:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f82a4a6-e7c6-3e83-a22d-612adf9fecbc | -11.14568 | -55.56232 | 2025-01-28 04:33:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cf93371-c1a3-3f5a-b38c-0456316dc422 | -12.488 | -43.78918 | 2025-01-28 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0a34669a-ea2f-367f-9174-3c0508f59ad2 | -11.82868 | -41.22675 | 2025-01-28 04:33:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12b59b35-48ce-35e4-b0f2-5358dfad6074 | -9.25764 | -60.31607 | 2025-01-28 04:33:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd6be898-21eb-3fe2-b6a0-7a50265b15e1 | -11.03195 | -45.06144 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf148f15-cfe9-3c49-8f0a-17a2ab264bd6 | -14.43081 | -54.05346 | 2025-01-28 04:33:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb2d78bf-8166-3289-b6f0-053f1b2f3480 | -11.03088 | -45.05874 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1ce20a1-f91c-3373-8e22-db51d8e22a4d | -10.94735 | -45.1764 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 895b3b92-8b4b-365e-a865-75ab5ddb61ad | -12.09972 | -51.22129 | 2025-01-28 04:33:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 834ed69b-569e-3394-aac7-c3981b19dd59 | -10.46291 | -45.0904 | 2025-01-28 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e2a66a3-47d6-3008-bc10-5422ed6d9722 | -11.0289 | -45.0564 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8522f9b6-425b-3868-a45e-8b3bf479eb2a | -11.05613 | -45.38214 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bdceaae-2fd0-3559-89b9-8b55889271ae | -12.70655 | -54.91093 | 2025-01-28 04:33:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a78646c-c504-3fbd-8f33-6f595324e060 | -15.65153 | -39.18817 | 2025-01-28 04:33:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b6465e8-5c4b-3c30-a987-6fddbfeb2640 | -11.03129 | -45.06597 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eb6ff11-1719-3724-a882-0cf637128558 | -14.43168 | -54.04855 | 2025-01-28 04:33:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abc67788-049f-32e9-a533-dccd5ca2d181 | -11.05248 | -45.38161 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94bfafee-d0ff-3b65-92b6-c37b345bffe7 | -11.02824 | -45.06092 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65ca9fb4-8d26-3aef-8d1c-97640beb8efe | -12.01964 | -43.01563 | 2025-01-28 04:33:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 175e5966-c080-3c7e-839b-0e51f6f258dc | -14.82402 | -47.4048 | 2025-01-28 04:33:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8064c5e9-9ec9-30c2-8c51-bc75dee508f6 | -20.5819 | -54.69572 | 2025-01-28 04:36:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cdd755e-2173-3813-b3ed-baf7c367305e | -23.33997 | -46.77364 | 2025-01-28 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 06d54794-421b-32b3-94cc-6e969e74a52a | -23.63299 | -46.42677 | 2025-01-28 04:38:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 10c611bd-e7c9-35ae-8053-b9211e7cc194 | -27.87535 | -50.0188 | 2025-01-28 04:38:00 | NOAA-21 | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9dd33c7d-ee22-3997-b4b7-d4e0e1152991 | -28.3994 | -55.56736 | 2025-01-28 04:38:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| b1441be6-7f7f-3ada-81fd-b2c537976953 | -27.44913 | -48.44755 | 2025-01-28 04:38:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d5e60bc4-52a0-329e-b855-350bec0b20a3 | -23.40646 | -46.55478 | 2025-01-28 04:38:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37fd8eb4-ac3f-3bd3-93cc-7cea418e0ce8 | -23.33966 | -46.77447 | 2025-01-28 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 21f9509c-92d4-3e2e-a9c3-75aba5debddd | -27.87886 | -50.01945 | 2025-01-28 04:38:00 | NOAA-21 | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c38e39f-3198-334a-a6f0-adc5b4cea8c5 | -29.61373 | -56.45431 | 2025-01-28 04:40:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 864df77f-2aa0-3fa9-a40e-9f8281bb7847 | -30.88014 | -53.32882 | 2025-01-28 04:40:00 | NOAA-21 | SANTANA DA BOA VISTA | RIO GRANDE DO SUL | Brasil | 4317004 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| ba1d65ed-550a-327d-ad6d-b56c81cb8573 | -31.62454 | -52.43115 | 2025-01-28 04:40:00 | NOAA-21 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 551de6c8-0b6a-3a5f-84df-3289752e8ef1 | -29.61022 | -56.45349 | 2025-01-28 04:40:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 0cdaf2e1-040b-3cfb-a398-614d6e31572f | 4.32411 | -60.85509 | 2025-01-28 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cac07b38-b733-35b1-bf3d-60e23612b32d | 4.32456 | -60.85817 | 2025-01-28 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4904460-95f3-3868-ae8b-eb38550e5fdf | 4.87279 | -60.51193 | 2025-01-28 04:55:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c0e1848-3fd3-3b4b-8563-c2fe489502c7 | -0.82415 | -47.45269 | 2025-01-28 04:55:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 759bc533-d168-3c77-9410-a4e72951646f | 4.87238 | -60.50901 | 2025-01-28 04:55:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38dc435a-29ee-3d9c-a583-f877a07065be | -2.93008 | -54.20658 | 2025-01-28 04:57:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5b33f64-41ca-31c6-88cf-c12da560de22 | -7.93389 | -55.01832 | 2025-01-28 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56f6428f-399c-3797-84af-6cf6d23548f4 | -6.9257 | -47.78046 | 2025-01-28 04:57:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
