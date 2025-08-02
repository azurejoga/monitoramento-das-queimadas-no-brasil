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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ad40fd5-c0f5-3d2f-8256-dc82db95fadc | -19.75912 | -46.04058 | 2025-08-02 03:57:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9779b7e9-9993-37e8-94cd-fad9593a588d | -17.59703 | -43.19701 | 2025-08-02 03:57:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5a21d17-1ca6-38e9-8d47-79a0330b3da4 | -23.76592 | -46.84632 | 2025-08-02 03:57:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 28c72672-fbf9-3693-b2a0-76aa10b62e35 | -18.21912 | -44.70452 | 2025-08-02 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb24de71-da8a-397f-a8c1-6ac7e1c47fd7 | -22.665 | -53.37856 | 2025-08-02 03:57:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 722015ef-6577-3b30-b844-97a278b1536a | -20.07201 | -45.81862 | 2025-08-02 03:57:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33b77ec4-d2d2-394c-853b-7f2a241a4738 | -23.65523 | -45.49768 | 2025-08-02 03:57:00 | NOAA-20 | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| df13c7d4-c6a9-3c7d-a220-d48c7eb5acc1 | -18.92319 | -52.4839 | 2025-08-02 03:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29f4e5c1-272c-3210-a7bc-2066ad3b1249 | -16.70919 | -47.57837 | 2025-08-02 03:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4b4f689-7c98-35bc-b768-eb6c5a61feba | -18.2411 | -45.17322 | 2025-08-02 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10723810-4aad-3a46-ac54-90028eff973d | -22.32341 | -48.71552 | 2025-08-02 03:57:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d91a9fb6-070f-3e6e-911f-c7fe013e7b36 | -21.54502 | -48.71913 | 2025-08-02 03:57:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8d4805e-fd93-39b6-a40a-39d05cd3b422 | -22.82573 | -43.0109 | 2025-08-02 03:57:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 05807a90-3b06-3261-ad5d-0d8df16c7874 | -20.77001 | -48.56618 | 2025-08-02 03:57:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75347194-e01b-3e4a-a0b6-45e97344997c | -20.22072 | -43.80413 | 2025-08-02 03:57:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 65be6203-258d-3ddb-874e-d087c9914951 | -18.21469 | -44.70834 | 2025-08-02 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 930e7df6-5a71-3b48-a64d-6c8b91a3c717 | -20.61469 | -40.44118 | 2025-08-02 03:57:00 | NOAA-20 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a79e1c99-123a-36e3-8978-755f9d2a40aa | -18.92802 | -52.48936 | 2025-08-02 03:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afe2b7eb-df2c-3c23-8f34-cf0404e5d018 | -17.91866 | -42.74396 | 2025-08-02 03:57:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 448c6943-150f-34a6-9073-6fafc225a18a | -19.24763 | -43.69772 | 2025-08-02 03:57:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1af4943-c1ce-3b68-9f60-bd7a3e810820 | -18.2095 | -44.71647 | 2025-08-02 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f705c15f-49c7-3899-9474-e9a1a3bf5e52 | -20.07665 | -45.81451 | 2025-08-02 03:57:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fec356d5-419a-3bb9-b3aa-f39b18044bda | -23.14466 | -47.10386 | 2025-08-02 03:57:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3a2b5e8b-7500-3bce-98b6-f4da22f33d04 | -21.14421 | -48.01793 | 2025-08-02 03:57:00 | NOAA-20 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f20b80d-ec46-3d06-a9f8-26520077efab | -20.322 | -46.62971 | 2025-08-02 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39e74e71-5a7f-31b2-9bf7-e18bd237ecd0 | -22.39936 | -46.78827 | 2025-08-02 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc4b3459-09a5-3da3-9f88-a9f24fb01ff2 | -19.74208 | -46.02562 | 2025-08-02 03:57:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 779f83c9-8190-3164-af1b-2a32122caa2b | -22.9778 | -47.04115 | 2025-08-02 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4424bde5-73e4-3f7f-83fc-866dd4c36b27 | -20.06166 | -41.40199 | 2025-08-02 03:57:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e4189242-3389-3b45-a461-2e706e3d3606 | -18.9289 | -52.48573 | 2025-08-02 03:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 073ffff8-c722-3fbb-aa07-b3ae0539ea34 | -23.46552 | -46.28109 | 2025-08-02 03:57:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bdb78a34-741c-3b73-a001-dfef0ba469a2 | -20.31711 | -46.63428 | 2025-08-02 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7053fea8-e49e-3814-93ef-633a1d1c9228 | -18.92797 | -52.49001 | 2025-08-02 03:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63785532-d3b7-378d-8506-2749bd63944f | -21.89055 | -42.74078 | 2025-08-02 03:57:00 | NOAA-20 | ALÉM PARAÍBA | MINAS GERAIS | Brasil | 3101508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f5eed369-8537-3cac-acb1-04f6d4ffddd2 | -16.71004 | -47.57396 | 2025-08-02 03:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79903266-ac73-361b-bd23-2f73fd4fc182 | -20.76912 | -48.57068 | 2025-08-02 03:57:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 769c1b70-aeb2-3b61-a935-e6f00577e4ed | -18.92312 | -52.48449 | 2025-08-02 03:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5cb0415-d8a8-3f0f-8cdd-b5db2bd2c5ad | -22.32767 | -48.71654 | 2025-08-02 03:57:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b8d6ec1a-723b-3e7f-bb8a-82eb035777e6 | -21.14002 | -48.017 | 2025-08-02 03:57:00 | NOAA-20 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a3bde3f-7413-31ee-9c5f-74dca3f322ea | -20.45475 | -46.41307 | 2025-08-02 03:57:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 778535ff-9168-39d5-8435-52e450833003 | -21.66021 | -46.93179 | 2025-08-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d202dbed-d169-3c6c-9256-5ef379c8f1af | -18.21103 | -44.70782 | 2025-08-02 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2577fce-b0f7-32e3-88f8-be471adb0f26 | -16.99989 | -49.47597 | 2025-08-02 03:57:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 93866473-b26a-3447-8c9f-3e518f4a423c | -20.40466 | -42.36745 | 2025-08-02 03:57:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 255ae033-f520-3d39-968b-add78ff54102 | -21.196 | -44.98843 | 2025-08-02 03:57:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 152c2f65-edc0-395a-bd03-ffa326ea54c1 | -20.45094 | -46.41208 | 2025-08-02 03:57:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc434488-88b5-30c9-8764-837b2272b321 | -20.07577 | -45.81934 | 2025-08-02 03:57:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42b17a3e-d083-3e50-8d9c-32b85a8b7603 | -8.0321 | -43.1257 | 2025-08-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.7 |
| 4326d504-06e8-3eb0-b4a5-7731ee35959c | -8.0513 | -43.1001 | 2025-08-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 7411a02e-1f59-3a7f-8dce-9aa735627bfc | -8.051 | -43.1237 | 2025-08-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 2490a9a6-8312-3b8b-ab3b-622764786a36 | -12.6591 | -44.5117 | 2025-08-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 842f9090-5731-3cec-addf-c7993d6347ac | -12.6784 | -44.5085 | 2025-08-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 80eb8ca2-03f3-3b4d-b9aa-1afc245cdb60 | -8.0324 | -43.1022 | 2025-08-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| b7a9766c-a976-39fb-9dbf-2644a87d5df3 | -12.6595 | -44.4882 | 2025-08-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 03c82cc0-3382-39e5-bd85-77fd40a5e081 | -12.6789 | -44.4851 | 2025-08-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f3df350e-b2d9-387e-92fe-b029b92fd01d | -8.0318 | -43.1493 | 2025-08-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 3ac8fe27-fcc0-3fd2-8898-f3897122b87c | -28.58883 | -50.15059 | 2025-08-02 04:00:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 55c40dc9-a65f-3c2e-a9ac-1b27cc8d7aec | -28.51996 | -50.55152 | 2025-08-02 04:00:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 26d4f730-11bd-3db4-90e6-3cc85c607ae4 | -29.43657 | -50.31816 | 2025-08-02 04:00:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 78b04878-34b3-3641-8bfb-82b101c11aa9 | -28.78818 | -54.76126 | 2025-08-02 04:00:00 | NOAA-20 | BOSSOROCA | RIO GRANDE DO SUL | Brasil | 4302501 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| b9d7f384-d50d-3d4f-b518-88cf88a1bc6b | -28.16572 | -49.36253 | 2025-08-02 04:00:00 | NOAA-20 | GRÃO PARÁ | SANTA CATARINA | Brasil | 4206108 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2b65d1cd-a424-3d17-af91-e929c5f89aba | -29.36422 | -50.39642 | 2025-08-02 04:00:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2c30a8e6-7aef-3380-9037-93cbcf0135dc | -28.78971 | -54.76068 | 2025-08-02 04:00:00 | NOAA-20 | BOSSOROCA | RIO GRANDE DO SUL | Brasil | 4302501 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 1f8138e2-db15-3baa-847d-ab1376964ae6 | -28.91461 | -50.16703 | 2025-08-02 04:00:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b5a0fe0-8ee1-3937-b6a1-fe95c67b1a1d | -28.44722 | -49.57728 | 2025-08-02 04:00:00 | NOAA-20 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc23284f-12cd-3b9c-881e-c98a17739572 | -26.02647 | -48.97412 | 2025-08-02 04:00:00 | NOAA-20 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0267041c-fb06-38db-b842-9c3454389300 | -24.6403 | -51.17115 | 2025-08-02 04:00:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f62ff5d7-c63e-3459-96b5-b5839ac226e7 | -23.70242 | -51.65349 | 2025-08-02 04:00:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cb7ccf86-f7af-33fa-b443-7dee2ec21eae | -23.71065 | -51.78326 | 2025-08-02 04:00:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e3c7daa-8723-3931-b3d3-88251bb78046 | -23.70313 | -51.65026 | 2025-08-02 04:00:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6dbc9067-3736-3d86-b4c3-5b40405414cc | -26.02566 | -48.97818 | 2025-08-02 04:00:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5beea2c5-9c69-3b02-ae8c-ac790519941a | -26.02161 | -48.97723 | 2025-08-02 04:00:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 195b384e-5bbf-3b15-9dba-d7a9a604323c | -24.68791 | -49.89618 | 2025-08-02 04:00:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3c369e0c-8ab2-386d-9e1f-336d5332c89a | -23.08664 | -55.18845 | 2025-08-02 04:00:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 3f6be2fc-fd08-326f-bc55-818aeb1c3051 | -24.02148 | -52.40442 | 2025-08-02 04:00:00 | NOAA-20 | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de9f7eb2-5ad5-3d2f-bf75-49b5508c5316 | -23.08956 | -55.18646 | 2025-08-02 04:00:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| f771d926-505a-387a-9735-d1fe9bc0e7ef | -23.08829 | -55.19175 | 2025-08-02 04:00:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 6c2f511b-2db6-3df9-9d46-3b6f1960dcf4 | -29.77488 | -53.84138 | 2025-08-02 04:02:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.8 |
| 78f13199-9488-3496-8888-91562f43a526 | -29.77833 | -53.84939 | 2025-08-02 04:02:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 04a03b17-35ed-34b2-9b78-ff4a95992dd6 | -29.77339 | -53.84783 | 2025-08-02 04:02:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 81004ac6-2b06-3907-ab7b-dce38d01b483 | -29.77714 | -53.84999 | 2025-08-02 04:02:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 7.0 |
| 0f37cafa-68ba-3812-b60a-a28f969681f9 | -29.77414 | -53.8446 | 2025-08-02 04:02:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.8 |
| c4e2ed61-54a1-379b-93d0-29c584292113 | -29.77789 | -53.84679 | 2025-08-02 04:02:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| 67941c33-def5-3420-a85f-944de6b5d4fe | -12.6591 | -44.5117 | 2025-08-02 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 953604f4-9c1d-3f05-be52-90c9f8e7efd8 | -12.6595 | -44.4882 | 2025-08-02 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 9484c499-31ca-3844-ab45-fbc0bbb586c8 | -12.6789 | -44.4851 | 2025-08-02 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 311c8e19-0da5-3ed6-8d2c-6adb89af2ca9 | -12.6784 | -44.5085 | 2025-08-02 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| fe290d52-fe38-3d0d-8514-520197a8969f | -8.0324 | -43.1022 | 2025-08-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 21f4d82d-2e77-31e9-a41b-54bb562736f7 | -8.0513 | -43.1001 | 2025-08-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 9fb406b0-56b0-3b20-a8b5-6e6e76cf6547 | -8.0321 | -43.1257 | 2025-08-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 4f725eb2-80cc-34ab-9898-f8ba5bc5b394 | -8.0321 | -43.1257 | 2025-08-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| efe77b77-b26c-3999-8be2-218659a66576 | -12.6591 | -44.5117 | 2025-08-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1e4b00e0-6689-35bd-9313-8ea39b8843c2 | -8.0513 | -43.1001 | 2025-08-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 5e31d00f-bb83-3929-b1ca-119c11c1c280 | -12.6784 | -44.5085 | 2025-08-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 460753c6-37d7-379e-8fc4-fd257554958d | -8.0324 | -43.1022 | 2025-08-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| d2b5c5a6-3359-31a2-a66d-59988073a3b9 | -12.6595 | -44.4882 | 2025-08-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 7286e30c-06f2-3fcb-abf3-ab03765a923f | -12.6789 | -44.4851 | 2025-08-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5314553c-d944-3edf-a0e6-6d91d62718ee | -12.6789 | -44.4851 | 2025-08-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b9e5c11c-40a4-3199-a083-21a2cc683592 | -12.6591 | -44.5117 | 2025-08-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fdf92313-3098-3b9b-8ab5-b55366a1c8a2 | -8.0321 | -43.1257 | 2025-08-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |


[Clique aqui para ver as próximas entradas](README14.md)
