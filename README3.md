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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a89a91c-e340-33f5-91e7-74435f5e1314 | -11.2802 | -45.4823 | 2025-10-28 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e4ced795-bc1e-3b19-a026-b5771e82f595 | -7.9461 | -45.5108 | 2025-10-28 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 814d1d4b-bc63-3fa6-964c-1bc4e2337415 | -6.6875 | -42.0296 | 2025-10-28 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 139.6 |
| e0c4e302-5cd4-3293-8211-8115a2c3d798 | -4.4632 | -43.2386 | 2025-10-28 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 48106ef9-f671-3b03-8c1e-bf4913495078 | -8.5676 | -47.0184 | 2025-10-28 00:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| dd748481-f17c-35b6-b282-195e1b34503f | -8.5673 | -47.0406 | 2025-10-28 00:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 350f09f7-96d6-30dd-8ff0-34604db919f7 | -6.7061 | -42.0517 | 2025-10-28 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| edba717c-d6cc-3f07-8eeb-df50f2447d07 | -2.7556 | -45.3995 | 2025-10-28 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 112.9 |
| ad143088-2bce-3799-9e0e-ab736ed7d9d5 | -4.3625 | -44.2842 | 2025-10-28 00:50:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| cf4756a2-3987-39ad-82c9-a161d9aafd8f | -7.9647 | -45.5317 | 2025-10-28 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 207.3 |
| cd188e49-d2f3-36c9-9480-9f20e9b89e0b | -6.7064 | -42.0278 | 2025-10-28 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 126.1 |
| dc50f747-ee58-35eb-9eee-a69ca75ba78e | -20.12373 | -42.39482 | 2025-10-28 00:50:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| ccc2511f-7871-3862-aca4-14ff704b63cc | -20.14071 | -42.42194 | 2025-10-28 00:50:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 542bfca7-32b7-34d6-99bf-21e56980418c | -16.05632 | -43.55467 | 2025-10-28 00:50:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| db45cab3-d09f-31ae-a0b3-639f94d474cf | -16.05047 | -43.52281 | 2025-10-28 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 12e25c8f-1209-3811-b9eb-9532d1c040d9 | -16.05121 | -43.55029 | 2025-10-28 00:50:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| ef69ca07-2249-371f-b039-0aa53e764da7 | -18.24425 | -44.19425 | 2025-10-28 00:50:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b1ec86c4-a0b8-33a2-8f6f-a67a4d94c697 | -18.05626 | -42.22857 | 2025-10-28 00:50:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| 71152ca0-33dd-3d21-9c97-489414388dd9 | -17.62638 | -43.99903 | 2025-10-28 00:50:00 | TERRA_M-M | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cbab3cfd-55fc-3e9b-a342-f3071aefe953 | -18.82158 | -43.23633 | 2025-10-28 00:50:00 | TERRA_M-M | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| 185a73fe-5deb-3db7-ac88-8e7b50222953 | -18.24736 | -44.18832 | 2025-10-28 00:50:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7c3cd0b6-ef9d-34d1-ac3f-b3934bac447f | -13.63288 | -46.46213 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 35610905-f8d1-3f96-95ba-1c4ddfda552b | -7.96523 | -45.51673 | 2025-10-28 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| addf86e3-0c49-387c-8e76-6f76b62b8a38 | -13.7417 | -48.41993 | 2025-10-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8cd995ad-c1ee-317e-af9f-a56164267361 | -14.14024 | -44.2336 | 2025-10-28 00:52:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fd874cc7-1373-32dd-8525-32352f7c778c | -9.4125 | -49.31951 | 2025-10-28 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 59e74b5a-b233-306b-826c-238cf846de42 | -9.21889 | -48.60161 | 2025-10-28 00:52:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| fe95391e-b7bc-3c8b-8776-2bf829efb89b | -10.95466 | -50.34248 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ec002d21-bd20-3a3f-9ecc-5b4e34ccb2e4 | -12.62096 | -45.0902 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 4c741e0e-bce0-3adc-9a7b-95bd4c64d800 | -11.27995 | -45.49073 | 2025-10-28 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 6c80ee59-c95f-3322-93ea-5ea5c5a0b3b1 | -11.14117 | -44.94189 | 2025-10-28 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 5d7e618a-28a7-3537-9c65-c6e35c0e6821 | -10.5701 | -49.81878 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| dd9e9462-ae28-38b9-b380-1c768617b1a1 | -13.39983 | -48.51797 | 2025-10-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6093ec06-0964-30a4-856f-48271e11081a | -13.66904 | -46.51923 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8c084366-22ab-371f-8ea6-5c930cead2c5 | -9.04833 | -46.93152 | 2025-10-28 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7382da14-6c55-3fad-a090-f6065ab64fd2 | -12.00366 | -46.79428 | 2025-10-28 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| a774bee0-4520-3dc3-9a02-e7af8a7a98fb | -15.34816 | -43.11371 | 2025-10-28 00:52:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 31.9 |
| a49ae843-612c-3b73-a349-87a829826c5e | -8.56435 | -47.04 | 2025-10-28 00:52:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 86ef9a1f-9c5f-3e3d-b610-1bb7edf82bbb | -9.13984 | -51.29369 | 2025-10-28 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 297f264e-47f6-364f-af44-01fc788f1eee | -13.88324 | -48.50705 | 2025-10-28 00:52:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 070d15c5-406f-3e4a-8db9-daf11b19d483 | -7.95482 | -45.55016 | 2025-10-28 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c0f6fb0a-fd85-3983-9f24-12350fa9ee8a | -9.91565 | -47.69679 | 2025-10-28 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ac56d33a-021e-3c31-b9c7-ffe80ff00fd4 | -15.14543 | -46.60775 | 2025-10-28 00:52:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 48bf9603-38af-3d20-b324-c086db98177c | -8.16393 | -47.00964 | 2025-10-28 00:52:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| fb0bb1ea-7cca-3f2a-8735-536c9baa3343 | -8.5781 | -47.03777 | 2025-10-28 00:52:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 63dd22d6-792c-3ace-b8cc-d5079c9ee07c | -13.88053 | -48.4996 | 2025-10-28 00:52:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a26dbeeb-8c8f-3ef8-90b1-60e44ad51157 | -14.61564 | -48.41263 | 2025-10-28 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f51e57e2-239f-3cb3-ac4a-c9fd6ee3ed01 | -8.56061 | -47.01637 | 2025-10-28 00:52:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 420882e2-e7ac-3d1e-8956-5dba5c09da21 | -9.41357 | -49.32572 | 2025-10-28 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 05b86a00-d6ce-36f6-8f60-fddca55e03b2 | -13.72486 | -51.45874 | 2025-10-28 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ff750794-9e6f-3d6a-9df6-1d4221232412 | -7.97042 | -45.54764 | 2025-10-28 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 2aa47e15-419b-3e99-8b15-861d54eea2e4 | -12.52671 | -47.56134 | 2025-10-28 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| fff175b6-90a9-3c66-a39d-ad97b2009da5 | -13.74395 | -48.43409 | 2025-10-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e8a04f9b-279d-3dc8-a0cd-f3c924945351 | -8.56651 | -47.00967 | 2025-10-28 00:52:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 09284fca-8ca5-36ec-897a-f7a8ced216fd | -14.61664 | -48.40617 | 2025-10-28 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5b22e9d0-0ea6-3686-a551-1ab26acb0362 | -9.22492 | -46.37271 | 2025-10-28 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 1d72db2e-592d-336c-be14-a5ce9dbc16d8 | -15.14881 | -46.6273 | 2025-10-28 00:52:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 583d169a-e3ba-3d4a-a930-4fefb90fdbe8 | -14.72633 | -47.36298 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 897e0c99-c136-33df-904a-cb201875a5fc | -10.86251 | -50.13633 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 21c06bfc-5ea4-3baf-b651-ce97c8960f48 | -13.31595 | -48.35052 | 2025-10-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 92bdf517-9e8d-3904-943c-db03e4ad12f0 | -12.19746 | -43.6053 | 2025-10-28 00:52:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| af17078a-8313-394c-9589-4ee89f1a517d | -13.84419 | -49.0699 | 2025-10-28 00:52:00 | TERRA_M-M | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 191549c4-5012-330a-8020-e3a77a89463e | -9.15125 | -51.30336 | 2025-10-28 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3cac772a-a703-36a5-b3e7-a3b06a478b20 | -7.94953 | -45.51895 | 2025-10-28 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 979a6bc8-2609-3d5a-86a2-3432e5685e3a | -10.91201 | -50.25534 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e56ea43a-58d5-3434-ac97-0bbc4589efe6 | -14.15717 | -44.25686 | 2025-10-28 00:52:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 71fd932e-e549-3cbb-ab8a-9e507462d480 | -10.56809 | -49.80548 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 1328659b-56b5-3e8e-b2ce-10bfecbfaf37 | -12.97661 | -48.39449 | 2025-10-28 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c00a5d70-c980-3b88-9a30-b6905e069b00 | -11.27965 | -45.48493 | 2025-10-28 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2fb41396-6dc6-3f08-9b21-94568a2ce8f1 | -14.15143 | -44.22585 | 2025-10-28 00:52:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3200d485-892b-307b-8095-3437c25fc618 | -8.57439 | -47.01414 | 2025-10-28 00:52:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 99e2c8de-c175-3b1f-9a76-42107e2c8274 | -13.22623 | -47.10371 | 2025-10-28 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 44.9 |
| f4395c42-56a4-3fe8-9873-e2834823349a | -14.53856 | -48.00159 | 2025-10-28 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0c7f8fd9-4bd5-3d75-9e0f-cd69d9a66963 | -15.23394 | -47.94896 | 2025-10-28 00:52:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7afc8cd4-a179-357d-8ea3-87ddbae6ecb6 | -14.61896 | -48.42039 | 2025-10-28 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 572a3c0a-b4b3-3c4c-89de-46560d9fb7f3 | -14.12741 | -46.97936 | 2025-10-28 00:52:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c015b75d-9018-321f-944c-fa03236d919f | -8.64369 | -45.28856 | 2025-10-28 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 3ebc4e01-4ebe-3305-b5fc-c1a2a87a3763 | -12.25959 | -51.33372 | 2025-10-28 00:52:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e6ad9f2-1324-3788-bd7f-8003b2f4723d | -7.9551 | -45.52335 | 2025-10-28 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 248.8 |
| e18364b9-25fe-3b41-a69e-c1f79ca187da | -9.14145 | -51.30483 | 2025-10-28 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 027a983b-5424-30f2-9d7c-7f603c04d749 | -12.00016 | -46.77302 | 2025-10-28 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e859517b-69c0-37d9-b483-b0304ab11594 | -12.09276 | -45.67709 | 2025-10-28 00:52:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3d68e5c2-77f6-38d1-970e-9415c2b83430 | -13.25216 | -47.96527 | 2025-10-28 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| da7d2e6b-4e63-3176-b8b5-e0ecea397517 | -11.65097 | -48.53237 | 2025-10-28 00:52:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 80aad606-3ba6-39e5-a76a-772d00216d91 | -11.80136 | -52.5018 | 2025-10-28 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 256a0704-f246-358f-b7c7-65dc83e5752b | -13.62083 | -47.02818 | 2025-10-28 00:52:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| bcab8ca7-a521-3f94-901c-8dbf099ff92c | -13.53805 | -44.12962 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 9efc0ea5-d2aa-3855-aadc-e20e0eda7783 | -11.07904 | -48.33195 | 2025-10-28 00:52:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 98c0a572-4cfe-3b3b-9d30-e1aa877c86f2 | -10.98405 | -47.72667 | 2025-10-28 00:52:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d5c53943-faa2-3197-b961-407093256597 | -13.22929 | -47.12207 | 2025-10-28 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 549c8fab-73b2-34f7-b6da-3cc4550d3bbd | -10.93135 | -50.25898 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a652a401-78cc-36df-900e-a9d9ec2c23a2 | -10.95622 | -48.056 | 2025-10-28 00:52:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ddd68f09-cb62-34d3-beca-9b4269596ce3 | -9.97679 | -47.17285 | 2025-10-28 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1e90760c-a60a-3b78-8f3e-10e4f181c374 | -13.13665 | -48.24241 | 2025-10-28 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 193607b7-0af1-3325-bbf0-c6b761feb15d | -8.57043 | -47.0334 | 2025-10-28 00:52:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| d59605af-3c05-383a-9ec3-8c2ac883efc0 | -12.61608 | -45.06213 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 1f0f0ff4-95bc-35cb-ab1d-3179ffb9e379 | -9.41581 | -49.3407 | 2025-10-28 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| be9c36c1-73f6-3df0-9e42-6dfd42d9b375 | -11.26994 | -45.51635 | 2025-10-28 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e3721a7d-bcac-3b5a-824a-8bad6c8e4849 | -14.63467 | -48.44769 | 2025-10-28 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 836ddb0d-0316-394d-9748-d2cc22641242 | -7.97079 | -45.52112 | 2025-10-28 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |


[Clique aqui para ver as próximas entradas](README4.md)
