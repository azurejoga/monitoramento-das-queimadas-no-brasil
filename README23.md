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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd0ed5c0-f8bf-344a-86e9-f3ec93070bc5 | -12.7548 | -44.5428 | 2026-07-08 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 940a7128-ae4e-3efa-ad08-3dac59fbb26d | -12.7741 | -44.5396 | 2026-07-08 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a5668ef1-5e19-35af-8e79-20c831aca852 | -12.7746 | -44.5162 | 2026-07-08 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a530e99b-787a-35f6-9904-581a040da72f | -12.7553 | -44.5194 | 2026-07-08 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 56cb7189-6c7d-32a9-a8f7-94f2caf71d19 | -10.20366 | -61.48465 | 2026-07-08 06:05:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ada7daf-ccac-38a1-9b9e-047e2609acdc | -6.7707 | -68.77619 | 2026-07-08 06:05:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0f8f48-ff1f-3c7e-a393-47768f390944 | -10.20867 | -61.48898 | 2026-07-08 06:05:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 417a1d53-7827-3bc1-aa80-4edfabe7ce3a | -8.09869 | -70.10814 | 2026-07-08 06:05:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0841613-e691-342b-af9c-4156deb5669c | -12.7746 | -44.5162 | 2026-07-08 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| d21d28c7-e633-36c7-bb7d-f7dfbb6c945e | -12.7548 | -44.5428 | 2026-07-08 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6fdc5289-61ee-3372-a17b-7ed48d7e8f1c | -12.7553 | -44.5194 | 2026-07-08 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 39f57c8e-91bc-3cc6-9ac5-3211c8d0b2ee | -12.7553 | -44.5194 | 2026-07-08 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 721bf245-cffc-33b7-8404-8d1edafd1ee6 | -21.8033 | -56.2729 | 2026-07-08 06:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 105f70c9-e27f-327d-84a6-6e884b0f1cef | -12.7548 | -44.5428 | 2026-07-08 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e7e7d4a6-6063-3f5e-b9e5-f74f29d9e05a | -12.7548 | -44.5428 | 2026-07-08 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a473b066-0eec-3d2e-81ff-ea5072954725 | -12.7553 | -44.5194 | 2026-07-08 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| da1a90ff-26f6-3177-ac33-ba157884fa79 | -21.8033 | -56.2729 | 2026-07-08 06:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 4c4631ec-c9b6-31db-b3df-39296444601c | -12.7746 | -44.5162 | 2026-07-08 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 53c34861-2928-3971-86cb-6d0bd06044a7 | -12.7553 | -44.5194 | 2026-07-08 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 42d625ab-b785-3c9b-8b71-557f2cbb3c84 | -12.7548 | -44.5428 | 2026-07-08 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 982cc473-25c7-35d9-bddb-cfde1a36cf6b | -12.7548 | -44.5428 | 2026-07-08 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| aeea466e-2513-3a69-9fe5-67cb0d269234 | -12.7553 | -44.5194 | 2026-07-08 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 10192365-f77e-38ad-868e-1178b5c0f644 | -3.50907 | -48.03027 | 2026-07-08 06:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 44fe7509-0509-3769-9724-706036dab571 | -9.22663 | -48.58067 | 2026-07-08 06:59:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| dfa22b55-96eb-3082-817f-1c8c09569b5f | -8.11926 | -47.10057 | 2026-07-08 06:59:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 05f924b3-5f3b-3bf3-a5c3-d47d876407fb | -10.02774 | -49.6224 | 2026-07-08 06:59:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e94ef4f2-5525-33c0-9f3f-ad0b8f9798cc | -9.21499 | -48.5793 | 2026-07-08 06:59:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 93b50649-e083-32c8-8dd7-3ad14475f41a | -3.507 | -48.04426 | 2026-07-08 06:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 627f5c34-cc55-30ba-83d9-071b3c80958e | -12.7553 | -44.5194 | 2026-07-08 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| cc95d5b8-3fc9-3024-b6e2-5869c9e66b82 | -14.14798 | -52.88524 | 2026-07-08 07:01:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5e86d5f6-b1af-3a77-9a65-b1d592cedf08 | -17.53886 | -54.00691 | 2026-07-08 07:01:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 85436639-c913-30b6-9594-4f3aa7c17a42 | -13.27885 | -54.40687 | 2026-07-08 07:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 16fd4733-cc4e-3691-bdbf-fe3fa0fbed36 | -14.13874 | -52.8839 | 2026-07-08 07:01:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 573539e5-320e-3adb-9847-33f3acd1a22a | -12.75918 | -44.52633 | 2026-07-08 07:01:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 904c96fb-b680-3d6c-a8d2-dd47d975e288 | -13.53956 | -52.94127 | 2026-07-08 07:01:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| bf021d76-bf03-31aa-8f95-8959abd05250 | -13.27751 | -54.41583 | 2026-07-08 07:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e92ae467-01bc-3e77-9015-7223d946d974 | -13.28763 | -54.40822 | 2026-07-08 07:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d97074b1-f815-34cf-b7f5-a4fbffb507bb | -12.75599 | -44.51815 | 2026-07-08 07:01:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 4261a356-807a-3a35-bb34-186ba32a25a8 | -21.79745 | -56.2613 | 2026-07-08 07:03:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 11762240-5fcd-30b9-a87f-073a34f78150 | -21.79605 | -56.27075 | 2026-07-08 07:03:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 83f85b22-6331-3dc3-b13a-06dbdbec3d4d | -12.7548 | -44.5428 | 2026-07-08 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 5f8dad3d-8a75-3419-a1d4-54922c297e15 | -12.7553 | -44.5194 | 2026-07-08 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 9d3cab58-02c8-317f-9f34-6cc5227db719 | -12.7553 | -44.5194 | 2026-07-08 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| ba54765a-ce45-3fcc-84b0-58191bf30478 | -12.7548 | -44.5428 | 2026-07-08 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e30268b2-3aa6-33df-a6b3-71d13b2cb090 | -5.67057 | -37.89195 | 2026-07-08 11:25:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 3ac8cf8a-0400-3ced-abc2-2979e2ecd025 | -6.48488 | -42.22315 | 2026-07-08 11:25:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 42ff27e0-fe29-3b9c-b08d-4376fbfe219f | -6.5018 | -42.23165 | 2026-07-08 11:25:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b7858049-2342-3e00-a3d2-63c98babb38a | -6.49411 | -42.22087 | 2026-07-08 11:25:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 81cae211-4ffd-3cbb-8938-d91c6a4482b7 | -6.50321 | -42.22215 | 2026-07-08 11:25:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 92db4aad-c5c3-35a9-a4b3-6d5fb60bbc1f | -6.5046 | -42.21269 | 2026-07-08 11:25:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 25bfe99d-ed6b-3331-9036-41a6d01efdc8 | -7.24921 | -43.11723 | 2026-07-08 11:25:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 185dcc02-9358-3b54-af10-7afcd4078925 | -9.01725 | -40.99039 | 2026-07-08 11:28:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 81202381-dc11-350e-981a-83fbe51af961 | -9.57523 | -42.05425 | 2026-07-08 11:28:00 | TERRA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a0fad19e-61d5-3ad7-8b14-ba5364dc5ec0 | -15.30743 | -41.83348 | 2026-07-08 11:28:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 3ef524fe-1080-3d93-9b78-97d2341946e8 | -13.29299 | -45.21912 | 2026-07-08 11:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 318.0 |
| 882cd7d4-0166-3c02-872c-c33a81b3afaf | -9.06498 | -44.75368 | 2026-07-08 11:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8b847b6d-a32f-3522-8a4c-d3269c05b981 | -8.39617 | -39.7685 | 2026-07-08 11:28:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 21dcdd43-39f0-3f57-a244-c88f6ad1b9b0 | -13.91225 | -47.35065 | 2026-07-08 11:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 812f7120-906a-316a-8b0f-b7d13ae194e4 | -9.82918 | -37.22501 | 2026-07-08 11:28:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 17.5 |
| c3b67e09-734f-38c1-ae67-162e51821190 | -8.00499 | -44.174 | 2026-07-08 11:28:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 851eb617-da7b-3d7d-896e-df8701c6cef4 | -9.06557 | -44.7601 | 2026-07-08 11:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 9c0ab2be-0109-35c3-82b5-2726cd7c63ab | -12.75497 | -44.44922 | 2026-07-08 11:28:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b6c08560-e79a-3ef6-9b89-7b118e60b507 | -14.12681 | -42.61801 | 2026-07-08 11:28:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 22e46d6a-816c-31ad-840a-680f281ab2b5 | -9.01599 | -40.99923 | 2026-07-08 11:28:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 469a8168-2ccf-34e7-8a16-a1a13328342a | -13.91228 | -47.34112 | 2026-07-08 11:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.4 |
| ac38c645-bf7d-3166-932f-bdd468104bef | -9.688 | -47.01231 | 2026-07-08 11:28:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 2a27c72a-c338-3f0f-95e1-708a3e5fafb4 | -13.9096 | -47.35701 | 2026-07-08 11:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3999096d-ba90-3629-a1ae-715f181060fe | -9.22228 | -48.58274 | 2026-07-08 11:28:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 945a5eb1-4448-3bcb-81d7-f247f61537f9 | -11.79652 | -45.54423 | 2026-07-08 11:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 26c23e0d-7bb9-3682-9280-3ac232434987 | -12.76107 | -44.53694 | 2026-07-08 11:28:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 0dbfc8c2-49b6-336b-85d6-f3786b3f9085 | -15.30614 | -41.84268 | 2026-07-08 11:28:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 380776e1-f22b-3989-bbbd-bd34f2fa3419 | -12.75337 | -44.45974 | 2026-07-08 11:28:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d21bebcf-b347-3555-9c98-669cb6fa5fe8 | -14.31325 | -45.78494 | 2026-07-08 11:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2922c72b-2cbc-35de-a9a6-21d2b4b4ec72 | -13.28043 | -45.17013 | 2026-07-08 11:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6c721e40-2012-3f0c-b53e-4fa79a7925a7 | -9.6852 | -47.02993 | 2026-07-08 11:28:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a3df6d98-4527-3f30-a025-c367aca5dd88 | -12.76269 | -44.52631 | 2026-07-08 11:28:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| bc200013-b6a1-3464-9213-d8cf9f8d3e3d | -14.32331 | -45.78673 | 2026-07-08 11:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad5cb447-2c8a-33cc-a96c-92c97dcf8a3a | -13.29478 | -45.20757 | 2026-07-08 11:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c9042a85-ed7c-3a80-8b10-b6776254ad36 | -8.12056 | -47.10003 | 2026-07-08 11:28:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3b8f6491-5214-317d-8839-1a0b0232840f | -11.79846 | -45.53163 | 2026-07-08 11:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 443294ac-f561-35ab-a740-17f76d1de2df | -13.91485 | -47.3345 | 2026-07-08 11:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b787528a-0ee0-3833-b919-d8031b456955 | -9.21913 | -40.86877 | 2026-07-08 11:28:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ba45c9f8-3bd1-3a72-814d-28d7e03ff9dc | -13.08452 | -48.16047 | 2026-07-08 11:28:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 04717901-c958-3c32-8daa-8b4f4b7b3481 | -9.06308 | -44.76585 | 2026-07-08 11:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 05cf5c17-4603-39d7-bdde-d56addd37653 | -18.14648 | -41.96309 | 2026-07-08 11:30:00 | TERRA_M-M | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dcb4736d-9662-32f0-aec2-91507113292d | -18.63124 | -40.51418 | 2026-07-08 11:30:00 | TERRA_M-M | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| f9ed8a63-73db-3b52-ade4-dfd0189ee3eb | -19.52789 | -40.57883 | 2026-07-08 11:30:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 878ce4c0-51d6-33da-9cf9-47d7908ab83a | -17.25651 | -42.9189 | 2026-07-08 11:30:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae97bb1b-b184-3bb9-af6f-18637d7fe585 | -16.33428 | -43.6147 | 2026-07-08 11:30:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 879eb51c-9e1f-3577-ad93-157ea159ab12 | -17.25782 | -42.90975 | 2026-07-08 11:30:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 903ea9e3-301e-3d9d-8a72-9d2014ae896e | -17.59924 | -44.60783 | 2026-07-08 11:30:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e1b742b3-a624-3809-a209-67c9f8146eaa | -13.282 | -45.2009 | 2026-07-08 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| c9f0f14e-08d9-3ca9-90ac-a8d89c6792fa | -13.282 | -45.2009 | 2026-07-08 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 07fc6a8c-4461-3cee-a390-144b18ce2226 | -13.282 | -45.2009 | 2026-07-08 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 7192a39f-b81c-3b59-9c07-93c936f822b8 | -14.3158 | -45.7884 | 2026-07-08 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 2bc9a074-2c00-311d-a8fa-160bcbaa7084 | -13.282 | -45.2009 | 2026-07-08 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 2058a34d-57fc-3f29-bf7f-e42492063e5e | -13.282 | -45.2009 | 2026-07-08 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 0b93b89b-e7e9-32e1-a9e2-39066d19f0c2 | -13.282 | -45.2009 | 2026-07-08 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| d0d59b4a-89cc-3c8b-a276-b3cdd927f634 | -13.282 | -45.2009 | 2026-07-08 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 59def187-7f7f-3fe9-a7f8-10cb0c7f6c2a | -13.282 | -45.2009 | 2026-07-08 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |


[Clique aqui para ver as próximas entradas](README24.md)
