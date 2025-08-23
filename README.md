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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78599fe8-d88f-31a2-9fef-6674bba06f86 | -29.0083 | -49.4735 | 2025-08-23 00:00:00 | GOES-19 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 103.8 |
| 95e88fda-e26f-30c7-939d-75fda44fe4da | -9.1909 | -59.4619 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b31b9db7-4077-3e5e-8732-ae6fed41b50c | -3.444 | -49.0297 | 2025-08-23 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 74924b45-6280-3e54-a052-676ec1d32d26 | -9.1712 | -59.5987 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 714c2cb8-29b0-3eab-8e40-d611af63870c | -20.0976 | -47.7442 | 2025-08-23 00:00:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a6ed4f07-1eac-3ccf-93bd-2babd263ad98 | -18.9683 | -46.9278 | 2025-08-23 00:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 41.7 |
| ebebf0b4-c403-38d9-8bd9-2ecf0908ed8a | -15.0186 | -54.8735 | 2025-08-23 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 0672edfa-7648-3f23-ae88-3ec3f6f7196e | -6.6044 | -44.5624 | 2025-08-23 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 183.1 |
| f8157ae0-ad17-3f20-b793-6d54c1e3eb21 | -17.5785 | -46.5523 | 2025-08-23 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d32cc36e-ab02-3d7d-a4fd-55ac66d25696 | -17.2757 | -46.7538 | 2025-08-23 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 6fbe9c88-378f-3ea4-8937-8e35a67af959 | -9.9495 | -60.1754 | 2025-08-23 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 525.3 |
| 1e188d56-d451-3274-a277-c19a95b69e44 | -6.6231 | -44.5608 | 2025-08-23 00:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d1f16a8a-e50d-32b1-9c57-832b525b9c63 | -6.4327 | -41.2114 | 2025-08-23 00:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 229.2 |
| dc97374d-7403-302a-aee3-77abde147990 | -9.9493 | -60.1947 | 2025-08-23 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 522.4 |
| ab53f11a-fccf-3bad-b0c0-8b43d8bd3dc2 | -21.9272 | -48.92 | 2025-08-23 00:00:00 | GOES-19 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 5950d7b0-9ca8-30b3-8361-a1bdc3e93779 | -5.7431 | -57.5814 | 2025-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 76a4fb2c-0159-3b1f-bcc7-d2f7816c9b6d | -6.4324 | -41.2357 | 2025-08-23 00:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 7fa120c5-54d1-3c51-9a93-e71b761aa0c3 | -10.6122 | -55.413 | 2025-08-23 00:00:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e84c8f71-60be-3bbd-998c-1f53a3625e7a | -9.2095 | -59.4609 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f74710c8-2462-39eb-80c9-4ef8b9407ac9 | -9.2082 | -59.6354 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 45684c7b-23c4-34d5-904d-df6ba6e098b7 | -14.2737 | -58.5866 | 2025-08-23 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 9d58e9f3-015d-3d93-965d-e1909a14131e | -3.4254 | -49.0517 | 2025-08-23 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2ffe4f85-249f-3dfe-8842-db74dbab03ee | -14.665 | -56.5952 | 2025-08-23 00:00:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a4e628be-3bfc-37aa-a56b-6142d9eecc2b | -12.9921 | -45.2252 | 2025-08-23 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| c2be41cb-17c4-3541-bd75-18981118648f | -5.7429 | -57.6009 | 2025-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| d9232358-27b6-3a61-8936-65d251b869ea | -8.8921 | -62.4297 | 2025-08-23 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 37990b65-1a54-3b0f-9793-04118fc6464e | -7.813 | -63.5656 | 2025-08-23 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |
| a667ce8b-a117-3c3e-9787-4f7fcaaa574c | -6.4141 | -41.1889 | 2025-08-23 00:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| b455cc24-43de-3efc-b1fd-c1e2fca5bb52 | -17.5985 | -46.5481 | 2025-08-23 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 937415ca-7409-345e-a68a-a7bf4b1bf146 | -13.0355 | -56.8159 | 2025-08-23 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ed89f57a-1d01-3bc2-a159-2e8e80c37761 | -20.097 | -47.7676 | 2025-08-23 00:00:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 125.5 |
| a9e56df0-28ab-371d-ba8f-be54f8cfbb25 | -5.7614 | -57.6002 | 2025-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| a0171a76-dd29-3aec-855b-4fedaf97d50c | -17.5979 | -46.5715 | 2025-08-23 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 52e86e28-e3f0-3bea-b4e2-dcf850763c24 | -5.7615 | -57.5807 | 2025-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 7da9a947-0bf4-3192-8d22-8e6e7022feb5 | -6.4138 | -41.2132 | 2025-08-23 00:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 215.8 |
| 45c07d83-42f2-372e-9ef7-d187ead5de07 | -6.4136 | -41.2374 | 2025-08-23 00:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 6188c3f3-8c0d-31db-aaa4-22b7c3fdfc95 | -7.2157 | -45.307 | 2025-08-23 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 00b8adf9-0b98-3b68-ace9-12b3b595969f | -13.0352 | -56.8361 | 2025-08-23 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a2aa6864-4ce8-3d84-b1d1-796f4247a2b0 | -14.2926 | -58.6048 | 2025-08-23 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 89992f94-4b58-393a-80d4-bb6c69dab544 | -9.1895 | -59.6364 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 1336f559-49e4-3316-836d-0a0a4ede5ed1 | -6.5781 | -59.871 | 2025-08-23 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 714dadb0-87a9-38cc-b050-a607aad51e30 | -17.2751 | -46.777 | 2025-08-23 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e8792810-7950-3f92-97da-c1f20a6daa04 | -14.3504 | -58.5796 | 2025-08-23 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 56dc3a0d-eff5-3c3e-8293-fb7a415f5337 | -9.9681 | -60.1743 | 2025-08-23 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 0baf9db7-aabb-36a3-ad97-ab5490bbbf6d | -9.2391 | -60.4834 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| adc231c5-8241-300d-ae62-caf6fbfb9984 | -14.2929 | -58.5848 | 2025-08-23 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2c6fb3aa-ae3a-375b-8865-0778118f9cac | -9.1897 | -59.6171 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 166.0 |
| d3e2640b-d088-3b22-a007-d48d5c1af3c4 | -20.8704 | -42.5331 | 2025-08-23 00:00:00 | GOES-19 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| bffe22fb-c575-3c04-bf86-83b46f69df1e | -15.1984 | -48.2296 | 2025-08-23 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3648b4ec-131f-3ec5-b321-8fd3d65ccb1e | -11.3303 | -55.2111 | 2025-08-23 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 029bfcd1-beef-33c0-9839-50bf30416063 | -6.6041 | -44.5853 | 2025-08-23 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| dd866877-5f97-3f7b-8bc4-e96200966b2f | -6.8733 | -59.8213 | 2025-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e5067db2-f413-3e4f-be00-b4050e3cbdef | -9.1711 | -59.618 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a7e7be3e-569f-369e-823d-9637b546a158 | -9.4449 | -47.6585 | 2025-08-23 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 3d4c47dc-ac81-3691-a671-85deb277e432 | -9.2083 | -59.6161 | 2025-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 2d52f4f9-d31e-3c8a-acc1-7957bbe13373 | -18.9885 | -46.9233 | 2025-08-23 00:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 9b53bfcd-ed57-3e2f-a79d-9b884dfb61d9 | -7.8131 | -63.5468 | 2025-08-23 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 207491fe-92bd-3a92-a600-63ee724aaa26 | -3.4439 | -49.051 | 2025-08-23 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 281a60a0-e0db-318e-98df-b5728221da54 | -20.0766 | -47.7723 | 2025-08-23 00:00:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 6fb8c4ad-ee4a-3b59-8eaf-983a70a592dd | -14.2734 | -58.6065 | 2025-08-23 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f31b3835-d4b4-3ec5-8805-6534cde68919 | -9.4452 | -47.6364 | 2025-08-23 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ce0f2afd-dacc-33d2-a556-a00b89fb374a | -9.968 | -60.1937 | 2025-08-23 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 6bd22dbb-6771-304d-8a45-fd742998e2a0 | -17.5779 | -46.5756 | 2025-08-23 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f3fae86a-fa2e-38fe-a4fd-54f9aa63ff33 | -15.0534 | -56.3907 | 2025-08-23 00:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 45e8b320-b16a-3da1-86b7-0a371a0954aa | -29.00214 | -49.48486 | 2025-08-23 00:05:00 | TERRA_M-M | ARARANGUÁ | SANTA CATARINA | Brasil | 4201406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 235.1 |
| a49c2929-884f-3e59-bd1a-8971f9f55893 | -29.00246 | -49.49146 | 2025-08-23 00:05:00 | TERRA_M-M | ARARANGUÁ | SANTA CATARINA | Brasil | 4201406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 262.5 |
| ec0f3662-5752-3e32-9b92-a5c7e1610655 | -20.04038 | -43.17821 | 2025-08-23 00:07:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 459e8992-4897-3187-906a-f48666d71475 | -19.95857 | -47.50462 | 2025-08-23 00:07:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7d23f791-9621-38b9-876f-732c04d80a9d | -20.0885 | -47.76793 | 2025-08-23 00:07:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 78d7ed92-e0d9-3e8e-aff1-8eecabb08f35 | -20.87148 | -42.55515 | 2025-08-23 00:07:00 | TERRA_M-M | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 7e873b27-5ab2-3925-9dcd-afc1727be7ff | -20.28929 | -46.65422 | 2025-08-23 00:07:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c856c7ce-9913-3dc0-af0a-154b93fdab79 | -17.70112 | -48.5071 | 2025-08-23 00:07:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 7185df63-755b-3cbb-8055-97cb333bd523 | -17.60787 | -46.70782 | 2025-08-23 00:07:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| af20fa06-7117-34b4-9c6f-2e0e1afb39d3 | -18.37099 | -40.32919 | 2025-08-23 00:07:00 | TERRA_M-M | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 47b724e9-e951-3719-a430-d43545cde2b5 | -20.14231 | -47.8382 | 2025-08-23 00:07:00 | TERRA_M-M | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 33.5 |
| a98dce93-9b17-3dcd-add9-e5d5fbf89755 | -19.95024 | -47.48516 | 2025-08-23 00:07:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ce86cce2-a3a4-318e-a205-cabd88b7dfe4 | -20.44155 | -42.11539 | 2025-08-23 00:07:00 | TERRA_M-M | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 84125396-2ab6-3c08-9827-0cb22d20395e | -18.2698 | -45.57916 | 2025-08-23 00:07:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 3e183368-e919-3799-9968-ff61028e00c6 | -20.1027 | -47.76627 | 2025-08-23 00:07:00 | TERRA_M-M | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 9b3c3c95-2eb0-3a61-b7d3-8df6e3da1bd9 | -17.82833 | -44.41034 | 2025-08-23 00:07:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ef9bebba-6f02-3b45-85ea-af62454bf32e | -23.10398 | -46.80448 | 2025-08-23 00:07:00 | TERRA_M-M | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 1bb493ea-1e0d-3f02-86ae-70e60a2e1c3b | -18.9669 | -46.91768 | 2025-08-23 00:07:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 25e98467-e5c2-3ae5-8434-feceeedf168a | -20.44278 | -42.12536 | 2025-08-23 00:07:00 | TERRA_M-M | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 36523ec9-dddf-35c9-aa5f-8ad38fda0b34 | -20.09107 | -47.79491 | 2025-08-23 00:07:00 | TERRA_M-M | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 6185d00a-29af-35ac-affe-7ebcc6484189 | -20.28076 | -46.6831 | 2025-08-23 00:07:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 91ab53ff-548c-305a-a11f-9f91dd203cf0 | -18.11095 | -47.92696 | 2025-08-23 00:07:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1f6c7617-137f-33c7-ab63-a9f524d4f3dd | -17.33737 | -42.65956 | 2025-08-23 00:07:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| d5e75956-be5a-309c-851e-f605cdce9577 | -17.33872 | -42.67014 | 2025-08-23 00:07:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f0a223e1-1042-3948-bf51-be95990d1930 | -20.55849 | -43.98061 | 2025-08-23 00:07:00 | TERRA_M-M | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 92d4e3af-7fee-380d-9b44-00b26cf756a1 | -17.27816 | -46.78896 | 2025-08-23 00:07:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1354da0e-b46e-3635-9f6b-e5a3b298af50 | -17.69922 | -48.5123 | 2025-08-23 00:07:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| e9d1f457-ec81-356b-ba5c-1d25ab69f1cb | -22.47248 | -44.28306 | 2025-08-23 00:07:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 50522c38-bdca-3c37-b73e-e5f63dbb55dd | -18.26013 | -45.56893 | 2025-08-23 00:07:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4bf5a156-deb4-3031-92b6-ca07889b8c93 | -17.27388 | -46.74981 | 2025-08-23 00:07:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3d974e3f-d91d-3b5e-9df4-74fd63ff1e75 | -19.95287 | -47.51072 | 2025-08-23 00:07:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0c92aace-ca40-3065-888c-a0d156ea9715 | -18.96905 | -46.93923 | 2025-08-23 00:07:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| af6cf122-850f-3654-a7e8-dac7d52abddf | -17.59114 | -46.55148 | 2025-08-23 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f2667b6e-31db-3b9e-9877-24b607e064c1 | -20.16439 | -41.50241 | 2025-08-23 00:07:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ecc743c0-ff96-31ed-8895-7151f936b415 | -18.97169 | -46.94439 | 2025-08-23 00:07:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 718e3ff0-76c3-3708-aefb-5e70cc9ce5fb | -20.61276 | -43.11438 | 2025-08-23 00:07:00 | TERRA_M-M | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |


[Clique aqui para ver as próximas entradas](README2.md)
