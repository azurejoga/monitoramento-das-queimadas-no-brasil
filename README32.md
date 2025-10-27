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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1174ad1e-c402-38e6-a8bf-8db580dff1fb | -7.93383 | -47.19197 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ab1c42-ddc8-3461-a4e2-e082622eeb3d | -6.9635 | -49.4045 | 2025-10-27 04:32:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cb012dc-1e1d-3809-a4f7-12452cfb987a | -3.92799 | -50.0259 | 2025-10-27 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 917bf8d3-4b66-3550-8308-97b3e4892f91 | -3.72204 | -47.64695 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30c2c1e8-e84a-3b34-8820-b212ba5992d1 | -5.6029 | -47.10854 | 2025-10-27 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83a08dad-9da2-3a52-902b-e5977129ca2f | -6.44713 | -42.34919 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 11c3c015-4cf4-3cad-bd85-ae45a11f8859 | -7.8533 | -46.50066 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44aaed85-a817-39b8-a4a3-53e6009121f7 | -4.39083 | -43.31976 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 8528dc49-4592-385d-acec-72860f948901 | -4.47984 | -43.42377 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 1ba253c9-f611-38fe-8140-789fa5b480e6 | -9.56133 | -46.80077 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7607e3e9-015d-33ac-97db-3610adab58e3 | -7.77281 | -45.38729 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc3db1aa-f2c8-37df-98eb-6e090b7bd225 | -6.37533 | -44.2632 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acb86746-e857-334f-9b00-77dcf5db8f33 | -4.36243 | -48.65801 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cdcc37a-cb26-3c45-948c-0850325afc45 | -7.53285 | -46.25797 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25c703cb-30ef-3b95-8a91-951f48ec68a4 | -7.68116 | -46.34027 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f597961-502d-35b2-a651-77899f02bd63 | -5.96548 | -42.76912 | 2025-10-27 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5b08572-c4e0-3532-bca9-ddfabac2debd | -7.8872 | -45.72733 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 935e6912-55e7-3f28-8057-d69392da6a30 | -4.44533 | -43.41635 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f612184b-0587-3515-af61-9458dc2b236f | -9.163 | -46.37671 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5489bfa0-615d-31f0-9918-5e5270f15d15 | -6.90061 | -52.19113 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb3315d8-65cb-3255-8499-32ff9b9cdfc0 | -7.83415 | -46.49032 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 23a33102-a535-34b9-8de3-163a6073cbc0 | -6.82319 | -41.20734 | 2025-10-27 04:32:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e9cd9e09-be30-345f-ac9c-71887209bd38 | -6.10287 | -41.77935 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eca9f917-dafa-329d-a728-6986ebc85d3b | -8.02711 | -46.76326 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aeb1ebd4-be83-35ee-9f6f-f7687d5af510 | -3.71598 | -47.64247 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55ec4f8d-0c56-34cf-8f9f-563ff477cd43 | -8.7006 | -44.42575 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b273945-1e49-3534-9c91-c78f218ec0f8 | -8.88421 | -47.9956 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a606784d-c77a-389f-ad35-28f412a53d64 | -6.17401 | -44.20796 | 2025-10-27 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bba6cb0d-d560-3d6d-9bb6-2bf096c784cf | -7.86215 | -46.42027 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 574abe1e-da8f-3e9a-ad3a-a4c870c6341d | -7.1329 | -47.04943 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cb37d27-f7a3-378d-881c-2975d97c6273 | -4.45361 | -43.41971 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9125c77-2c06-382a-96e4-cb165c25c555 | -7.78807 | -45.38147 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c97f6ae7-24cb-3a57-ac34-59e0cb831f76 | -6.8927 | -45.14511 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a18b2d4-71ce-3918-9c0c-b9d40aec9bdd | -4.22808 | -48.36486 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb3869aa-619e-342b-9cd8-1e727e8b5e70 | -7.92997 | -47.19495 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee4e596f-1212-3784-bff5-3af5929051db | -9.04416 | -47.6212 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f30101a-79a3-3e63-a3b7-898118ff3c54 | -3.75821 | -47.58905 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1437e127-e4a9-35e6-9d46-3bb8d16775da | -6.3781 | -44.27002 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27c8d6c5-83c7-36f5-ad3d-3ab0cd19bfeb | -4.2057 | -48.35728 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ddc0432d-e580-3f3d-9d82-afd24d7c8845 | -4.73117 | -46.80896 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 457f4f74-90e9-3322-97eb-982043591a04 | -3.8048 | -51.8568 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9615d43-e817-3923-b0e0-1ea519079307 | -3.71159 | -47.64885 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae209789-4492-3f8f-9ee3-ba7adb928f1f | -9.58317 | -45.18846 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bd748a0-6568-3ce4-849b-04956a096136 | -9.23914 | -45.57858 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b98ba2e-a4c5-39c0-a2a3-9e8fb8c1fd62 | -8.33236 | -46.16573 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d2977a6-cf9e-3cee-8087-5dd05bceca53 | -8.96517 | -47.1858 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 511ec9f6-7f3e-3e27-b08b-a16a60849237 | -5.64044 | -47.62931 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 266c1b78-4911-3d83-bca3-f2d15e487c1c | -9.34222 | -49.27937 | 2025-10-27 04:32:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c89822b-bc8a-3090-904e-1e118619c760 | -6.49473 | -42.21426 | 2025-10-27 04:32:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0509744b-5c66-39eb-8fcf-78d602d6a5ee | -3.0986 | -49.45007 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d7166c5-4050-3c73-8d3d-2875d1a30306 | -7.83912 | -46.45776 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8bef39b3-69ff-3571-81f9-a544950a51dd | -9.14359 | -51.30489 | 2025-10-27 04:32:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff7e143f-812a-379c-af55-8926b12654e8 | -3.11354 | -51.21121 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bc456f66-fbc9-3406-9b3c-e885512b7522 | -4.22753 | -48.36836 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8ca32ad-ce3a-3742-bf2e-dca8b071e0d1 | -7.84634 | -46.41045 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38106c2b-1844-3774-aac4-e83ea4e603d0 | -7.86045 | -46.40873 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b326c5-f9d4-3c8e-b4d0-3eff9b879cc7 | -4.44825 | -50.1538 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2712d8c7-d3ee-31e9-bb53-759ce3623281 | -4.4402 | -43.42475 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 268f286c-b30f-3be0-b861-94ac4060d873 | -8.23323 | -46.92699 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0e780eb-e2f7-3fba-99ec-a6113984ce50 | -3.37186 | -50.17188 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2af79c71-e659-3bac-bd47-d8b7c66d8071 | -2.11176 | -52.77884 | 2025-10-27 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e295241-b37d-344f-8356-e6c56b59682d | -8.27738 | -46.87859 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a067808-8931-3d86-8fab-a428f664feff | -6.08334 | -46.99627 | 2025-10-27 04:32:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d6df58b-a8ba-385d-ad35-dbe26757b25e | -8.709 | -45.80648 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f93ce1d-f2aa-3dc6-99a4-63569f825090 | -5.96997 | -42.76621 | 2025-10-27 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d17f154-1c76-35ae-8fad-1198bba1af06 | -5.71872 | -49.3046 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0169533a-5aad-3ab7-9b34-06ed2ccf0ac1 | -7.79217 | -45.3781 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37e98fc5-cbb2-3e02-b2f5-20210c67d92f | -6.88385 | -45.15584 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0f80a85d-1bcc-3ea8-8a9c-2959edfbaf01 | -4.47849 | -43.43282 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b0128b3-b000-3681-b0e4-8b38f69d0ec8 | -3.72259 | -47.6435 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca0f507a-28b2-306a-bb6a-aed19c723564 | -6.49003 | -42.21735 | 2025-10-27 04:32:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 28d11e92-6ac2-3eca-b1be-61c80b0efb28 | -8.03377 | -46.74228 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 186f0f4d-bfa7-3063-bcf0-bdbea13ddd0a | -4.4686 | -43.42199 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2abb6fe6-691b-3b88-9b41-ed555ee8ac2c | -3.92859 | -52.25109 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3022c53-9f11-3913-b6e0-828ec5437947 | -9.26916 | -45.59577 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b375b4f6-4166-3fd9-a7c3-a58d6e9f3046 | -4.26688 | -48.55207 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b544ca55-05ef-392f-9a24-1181cdcc3e55 | -9.57428 | -46.90709 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3b37460f-583b-3d67-9e00-7a01e80bbdad | -6.51227 | -46.2263 | 2025-10-27 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34536b14-6d11-3620-bf55-5dfbc0d219dd | -6.80788 | -49.35036 | 2025-10-27 04:32:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ea460dd-c606-38ba-953c-966f8c709b5a | -9.34722 | -49.26933 | 2025-10-27 04:32:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45e7e34e-45c9-3c02-9da7-291564f231c3 | -4.42867 | -45.97376 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ed48655-3985-34dc-8c27-59341fc9556e | -4.73078 | -41.55124 | 2025-10-27 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 974ac815-a56c-3c02-837b-f725406648c1 | -3.72589 | -47.64401 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae2c9ec8-a380-3f10-bb13-4e752de40fc8 | -4.43147 | -45.97788 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6def9be-b4ee-3516-9754-e087d5ed9b3b | -9.1336 | -51.29908 | 2025-10-27 04:32:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89f46a2f-cbd1-332a-9b51-49e5c635a720 | -9.43733 | -46.3021 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3334f5c5-6ef2-3793-adb4-bdf60f29b161 | -7.8336 | -46.49394 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0aeeea99-2e79-303b-b652-258dfd0c7a2f | -8.12543 | -47.03068 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14311841-1624-3c86-8ae4-d08737f2b023 | -5.10282 | -43.19841 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fce905b3-fed3-3d67-a09a-3289118d14ed | -7.68228 | -46.33301 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcabd1b0-5137-38d5-9889-2371c1786588 | -4.20341 | -48.71389 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0181910a-5325-3fc3-a16b-648e2202c147 | -4.48291 | -43.42889 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d86df9a4-3356-3eee-b462-ea1819f30f5f | -3.23018 | -45.93705 | 2025-10-27 04:32:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 683effd3-124b-3df6-ba67-096b64e9d1f4 | -7.83864 | -46.48359 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fd070ad-b5db-3877-8f1a-245b58812056 | -2.44634 | -49.02668 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98584eea-7ddf-3a41-b49a-c4d27c8c9a19 | -7.78455 | -45.38096 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6f417d7-307d-3455-b500-75188f0d2271 | -5.53224 | -41.72183 | 2025-10-27 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 428ce33e-07cf-35b3-b4e0-f552c9476379 | -4.44769 | -43.42591 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94788601-2ec0-352a-9e01-175e8a21f1a7 | -8.10104 | -47.05589 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b61a315-008d-3681-857f-3787281841f9 | -6.23371 | -42.5533 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README33.md)
