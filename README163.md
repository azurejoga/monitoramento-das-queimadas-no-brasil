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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a00302-3bf2-32bc-84ec-aa937e3bf5df | -28.23763 | -49.60587 | 2024-10-05 12:42:00 | TERRA_M-T | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| cfbfc384-7d16-3610-b7e5-e5c927f79e41 | -30.4993 | -52.46924 | 2024-10-05 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 17.4 |
| b51c0c46-973f-3776-94f6-6915aee3e5e7 | -6.9698 | -59.0852 | 2024-10-05 12:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c6974b3d-0274-39e6-9192-cdb46f5967ef | -6.9514 | -59.0666 | 2024-10-05 12:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 222.9 |
| b0724b75-17f2-3e2d-8c4f-7ae59734eaf7 | -6.9515 | -59.0473 | 2024-10-05 12:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| f3d8a174-865a-3008-99ff-61e94a42b039 | -6.9699 | -59.0658 | 2024-10-05 12:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 7cb2119c-6601-318d-b92d-360c0b70708b | -8.1183 | -43.7718 | 2024-10-05 12:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 152.0 |
| fcc0ec45-3075-397c-828b-e4445cc1cd8f | -8.8738 | -45.1875 | 2024-10-05 12:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 6aedb008-bc95-32d7-a037-f50558ec3b7b | -8.7772 | -49.955 | 2024-10-05 12:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 309c032b-f718-31f2-af2a-1b492980cf25 | -9.3647 | -51.0898 | 2024-10-05 12:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| bb8e5958-1ebc-337c-98d3-f5a7fc089e1c | -9.8858 | -47.1901 | 2024-10-05 12:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 880fc698-f06a-36f3-a6da-c6fedd18283b | -9.8545 | -46.7257 | 2024-10-05 12:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 03ab888d-9028-3da0-bc5c-7763ec99fd8f | -10.4424 | -50.7336 | 2024-10-05 12:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5df0e21c-6174-3516-99c6-a966ff9a42b8 | -10.7542 | -46.1894 | 2024-10-05 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| cdd7d99f-0e38-3a57-b13c-55c9a016bdd7 | -10.7736 | -46.1643 | 2024-10-05 12:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| f3d28680-9072-38f4-9e1c-d6bbe7cd7565 | -11.3662 | -47.2113 | 2024-10-05 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 0655b7f6-8752-31a2-83e8-ae7fba2b887d | -11.3665 | -47.1889 | 2024-10-05 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 857abb38-b54b-31ee-a4b1-66023302146f | -11.6995 | -47.8131 | 2024-10-05 12:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5a8649a5-ecb0-3c8c-b874-249ab7448fc6 | -11.7187 | -47.8107 | 2024-10-05 12:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 73b7cbf7-dc13-3dc6-867a-883f659bef70 | -12.8343 | -47.4791 | 2024-10-05 12:46:18 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c8c67636-ef0a-3ef4-bf38-67cbdcc05fdf | -12.7623 | -50.5782 | 2024-10-05 12:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8f93be5e-d254-3143-8279-0dc894f0912e | -12.6532 | -54.0415 | 2024-10-05 12:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| c88fe0f3-b1bb-31b8-a1ed-4d0c0a2ef160 | -12.7815 | -50.5758 | 2024-10-05 12:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 97f822bd-54c5-3d77-8ece-0610e61f0bf4 | -13.0598 | -51.1195 | 2024-10-05 12:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 068bfeab-ad47-3bb1-befe-56e61e2269c0 | -14.0577 | -45.138 | 2024-10-05 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 4209798a-a35a-3793-bcdb-d0f9051a4f3e | -14.0582 | -45.1146 | 2024-10-05 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| f1138046-f4bd-3b3c-9c19-a257369b30fd | -14.0504 | -45.4877 | 2024-10-05 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1c0fcab0-1bb3-3572-b3f2-65be49de26f3 | -15.1821 | -48.0754 | 2024-10-05 12:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a2e6fdbb-87a7-3c68-a182-93b09607f5e5 | -15.1826 | -48.0528 | 2024-10-05 12:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 2c7aac52-0ab7-3643-bdd7-9c661b985007 | -16.6797 | -55.4985 | 2024-10-05 12:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 70972be4-058f-30c5-923b-332d977fb3d1 | -17.1085 | -56.7892 | 2024-10-05 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 172.3 |
| b5524652-c75e-3a39-8d53-d51c26649cb6 | -17.0892 | -56.7709 | 2024-10-05 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 68089e8f-3755-3b85-bbd2-3da3a7f9bf6f | -16.9717 | -56.7646 | 2024-10-05 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 252.9 |
| fb49f6e9-bc2a-3fea-886b-375e71340c64 | -17.1088 | -56.7685 | 2024-10-05 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 2522ba27-817a-35a8-a2ba-2a6f89604c09 | -17.1185 | -57.3834 | 2024-10-05 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| e7948502-61a3-3e7d-b703-10b761f90516 | -17.1774 | -57.3764 | 2024-10-05 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 4bbaa2fc-b301-3219-afe6-c33c959e8066 | -18.6984 | -57.2708 | 2024-10-05 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 8710fedf-6e5b-3c13-a45f-6f52e2feba15 | -18.6981 | -57.2915 | 2024-10-05 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 4bc77c9b-312c-3fe2-9955-05c827f15d30 | -18.6586 | -57.2759 | 2024-10-05 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.8 |
| 64d13a03-07af-3ac3-90c4-4b05a74c29d4 | -18.6785 | -57.2734 | 2024-10-05 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 182.4 |
| 51ccb67e-3d90-3b20-b9b0-d0ff54186f9d | -6.9515 | -59.0473 | 2024-10-05 12:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 469c14a5-c420-359b-a187-1b00e5cafea2 | -6.9514 | -59.0666 | 2024-10-05 12:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 01b2fa68-643d-37b6-964b-f9248aaeb12d | -6.9698 | -59.0852 | 2024-10-05 12:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a1f27b95-7324-3dec-81ed-cb1564266a8b | -7.5028 | -44.8254 | 2024-10-05 12:55:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 16da9634-4884-37e0-8957-8ac8e3f91a1b | -8.1183 | -43.7718 | 2024-10-05 12:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| cbf9b80c-b444-30f4-820a-93f61f73f21e | -8.7584 | -49.9566 | 2024-10-05 12:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| e4f2d1f6-59eb-3e08-af31-9a81844fca24 | -8.8714 | -48.3297 | 2024-10-05 12:55:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 5c415037-53d9-308e-bcd4-aa8ba45e6009 | -9.3647 | -51.0898 | 2024-10-05 12:55:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0f95bc2e-f414-3f76-b2c9-15fd20ffaba4 | -9.7883 | -46.0593 | 2024-10-05 12:56:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f4fdaa42-71ce-3ece-96e2-ff59c7747741 | -9.8545 | -46.7257 | 2024-10-05 12:56:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0f5dbed8-5891-3513-910d-08192befe8c1 | -9.9735 | -46.353 | 2024-10-05 12:56:02 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0d12e688-e301-374a-bc04-c92225f84b52 | -9.8858 | -47.1901 | 2024-10-05 12:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| e4f3d6a8-c3d9-3ad6-9503-772a324bbe06 | -10.2711 | -45.4787 | 2024-10-05 12:56:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7cea0f95-b292-3b13-a2ef-6a0442cb6c98 | -10.4424 | -50.7336 | 2024-10-05 12:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0846142a-d0a2-3124-961d-9b962ca4a503 | -10.3131 | -50.5128 | 2024-10-05 12:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 6e36f474-33aa-35d1-8e3d-82ada1426c38 | -10.7542 | -46.1894 | 2024-10-05 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| e1d65f35-e9c6-3991-ac78-c7ea653404ca | -11.1983 | -46.9871 | 2024-10-05 12:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| d4b61d17-f9af-3d2a-b5fe-2bfc41e87bd5 | -11.2427 | -46.5997 | 2024-10-05 12:56:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| ac17956d-3ee9-3de8-b85b-93be2ff6ea6c | -11.3662 | -47.2113 | 2024-10-05 12:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| e6cd6282-a0b7-3684-9ee7-be3106c8db39 | -12.0503 | -47.3882 | 2024-10-05 12:56:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7594b5e5-16ca-3222-9b55-a741075cd54e | -12.6723 | -54.0395 | 2024-10-05 12:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 66f3f189-e361-3404-951b-a35ed488c002 | -13.0598 | -51.1195 | 2024-10-05 12:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 94d31315-cc9f-36e9-a682-def7f0db991e | -13.1056 | -46.3321 | 2024-10-05 12:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 03ae7b83-7ba8-3df1-a309-bb538914aa50 | -14.0572 | -45.1614 | 2024-10-05 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 79b32652-fbd9-3a9a-94f5-5e1c5647b982 | -14.0504 | -45.4877 | 2024-10-05 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 47450fc1-3877-30b1-891c-69fd47660bb4 | -14.0577 | -45.138 | 2024-10-05 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 1616c9cf-5ead-3fad-9ad5-d7d08d625303 | -15.163 | -48.0561 | 2024-10-05 12:56:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 386c54f4-8c0d-36d8-b274-3a88bfe4fcd5 | -15.1826 | -48.0528 | 2024-10-05 12:56:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| fceb7fc4-2204-3688-8539-f57eb629d986 | -16.679 | -55.5402 | 2024-10-05 12:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 315f8064-2e4e-3071-99c1-377bfaf8faeb | -16.6797 | -55.4985 | 2024-10-05 12:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 40daa8c6-2518-3514-81dc-0a0a11f2c4eb | -16.9283 | -55.8405 | 2024-10-05 12:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 7cc67717-313c-3bf3-81b3-a9223d59c175 | -16.9714 | -56.7852 | 2024-10-05 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 267.9 |
| 8404b355-7bc0-3ced-b43a-5e2c46b884b7 | -16.9711 | -56.8058 | 2024-10-05 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| beedda8c-319d-3616-94f6-61c4501ba0a5 | -17.1088 | -56.7685 | 2024-10-05 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| d14b273c-978d-325a-b1cf-bc0127bbb95f | -16.9717 | -56.7646 | 2024-10-05 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 268.3 |
| 86bb91c8-8521-33b6-a8f6-c7388860fcc7 | -17.1281 | -56.7868 | 2024-10-05 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 2c05f8e0-5e80-34b7-9431-c7457e532ae9 | -17.1185 | -57.3834 | 2024-10-05 12:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| e1a20603-cd94-30a8-9731-c454447cebf4 | -18.6785 | -57.2734 | 2024-10-05 12:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 213.0 |
| fb89cef3-1dd5-3b1c-b02a-b1b9bbbfc558 | -18.6789 | -57.2526 | 2024-10-05 12:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| fb3e947a-5f8c-3d1e-8ad0-79c78d5b7444 | -18.6586 | -57.2759 | 2024-10-05 12:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 181.5 |
| 19696f7e-96b1-3122-9361-d46e4d9e1273 | -18.6984 | -57.2708 | 2024-10-05 12:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.3 |
| 2ce65deb-04dd-3e8a-af4b-ca8af237704c | -18.49 | -52.97 | 2024-10-05 13:03:40 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 42320cf1-c89d-33f6-8ea6-fc02e078f65b | -17.03 | -56.78 | 2024-10-05 13:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65b08a2c-8a4d-30d7-941d-638074fa2d62 | -17.03 | -56.86 | 2024-10-05 13:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f0cb9b3-ca2a-338b-afe0-506111e0effa | -17.0 | -56.76 | 2024-10-05 13:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5819aa1f-19bf-311b-8a3e-8afe2c9d83c5 | -8.88 | -48.32 | 2024-10-05 13:04:35 | MSG-03 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5b8864-c635-3061-a5d8-c3b7bae7ac49 | -6.9515 | -59.0473 | 2024-10-05 13:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 680f2d65-ffab-3681-931c-94fc4dc7534f | -6.9514 | -59.0666 | 2024-10-05 13:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 229.0 |
| 6f9762f8-7d70-3ef2-afee-471859f6ce50 | -6.9698 | -59.0852 | 2024-10-05 13:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 0be45508-5c23-371c-97fb-23f0af532ad6 | -7.5028 | -44.8254 | 2024-10-05 13:05:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| cf35fc96-e025-3b86-a38a-0f12bce9277d | -7.7498 | -43.0618 | 2024-10-05 13:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 96d66774-7d0a-336c-b21c-bf9c4a422401 | -8.1183 | -43.7718 | 2024-10-05 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| e51c9150-dc22-376d-b160-8fb9a9e82f06 | -8.4538 | -47.0959 | 2024-10-05 13:05:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b139f208-4c98-350c-b355-e9342d5f4378 | -8.8528 | -48.3097 | 2024-10-05 13:05:56 | GOES-16 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d54fe6c1-380e-3ee4-88c8-f753def55aeb | -8.8714 | -48.3297 | 2024-10-05 13:05:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 353.9 |
| a9603a19-db3e-36dc-96d6-3011e2f8f075 | -8.8525 | -48.3315 | 2024-10-05 13:05:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 2399fe72-8c6a-3f62-86d3-c0591dee3c4f | -9.8855 | -47.2124 | 2024-10-05 13:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| e0efb196-cc75-3667-b2a3-b67f1f3f8b30 | -9.8545 | -46.7257 | 2024-10-05 13:06:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1bba4b19-28a5-3087-9cab-ba004b53660c | -9.8858 | -47.1901 | 2024-10-05 13:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| edf87d39-6ec6-3244-9abb-ceae890c404a | -10.2942 | -50.5147 | 2024-10-05 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |


[Clique aqui para ver as próximas entradas](README164.md)
