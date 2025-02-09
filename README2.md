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
| ea569567-3d71-31ae-bba4-b85dbb448a28 | -18.71581 | -39.99974 | 2025-02-09 04:10:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7878e8b6-5825-304b-8499-24fce735b71d | -14.46672 | -44.42355 | 2025-02-09 04:10:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef48e63a-d96d-38c2-a73f-86c36d8b9194 | -15.31836 | -43.73579 | 2025-02-09 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 14a3866c-a434-32ba-9d81-ac6b215b2a60 | -19.82793 | -40.09875 | 2025-02-09 04:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b1bd5bee-3e06-3b9b-9260-2d8eb7d16c4e | -13.61902 | -55.45671 | 2025-02-09 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f6975794-3cd4-3f34-95f9-4bfab49474e5 | -12.21496 | -50.92179 | 2025-02-09 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0257998-5588-370d-8600-5c72fca13b9a | -19.82409 | -40.09819 | 2025-02-09 04:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c7960cc3-7af5-3a7c-925d-a8e514e607ea | -15.46814 | -51.94958 | 2025-02-09 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 26dd720a-a566-35e3-9016-e6f9c62f920e | -15.03069 | -43.37835 | 2025-02-09 04:10:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f5d8c8ed-09ff-3d5f-a084-90ab05d87ee6 | -19.6653 | -42.94889 | 2025-02-09 04:10:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e44fb7e-d926-3680-a9f4-4e48324fb5a2 | -19.71833 | -40.35263 | 2025-02-09 04:10:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8dd54f21-c693-39bf-bbe4-2523d08e1a2e | -14.13614 | -41.69173 | 2025-02-09 04:10:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42ff6873-8a18-3880-b139-6c8bac6d801e | -13.62019 | -55.45116 | 2025-02-09 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2dc114a-fa1f-3d43-8416-9b3d250ef68b | -12.34794 | -52.49089 | 2025-02-09 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f119c12b-395b-3973-bfa4-7dc695ff714d | -21.07759 | -56.39457 | 2025-02-09 04:12:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a1021f3-f97b-3d35-abaa-0ba9537bb23b | -21.61531 | -48.46306 | 2025-02-09 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc5c6116-ae4f-324d-8934-192f6aad9578 | -22.67833 | -42.85312 | 2025-02-09 04:12:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 51a5d8f3-60bc-3756-a978-3d3da059aeca | -21.0786 | -56.3902 | 2025-02-09 04:12:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88120d7e-6feb-3370-8bf2-47ac32e5620a | -21.19567 | -44.93936 | 2025-02-09 04:12:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5b00bfba-bf4b-31ab-964a-eca2acb84eed | -20.28279 | -49.92517 | 2025-02-09 04:12:00 | NOAA-21 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a29368b3-997d-3094-bdfd-0e37b1c48341 | -21.0795 | -56.39212 | 2025-02-09 04:12:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cbff252-fd8a-3102-b712-e18f15f3d6d8 | -22.54035 | -48.8127 | 2025-02-09 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc309d05-b068-379a-8a25-16b90a6d1419 | -25.19321 | -49.32553 | 2025-02-09 04:12:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24552ab8-e56a-354d-9bee-8f2567b1da7a | -21.4357 | -43.88121 | 2025-02-09 04:12:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9a4a4d35-fb9a-332d-8440-76eae90f7768 | -23.33936 | -46.77214 | 2025-02-09 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a8e32e99-da02-3454-a848-de78408bbe62 | -23.69907 | -46.67791 | 2025-02-09 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2307c2a2-3955-3560-884b-cbaa88ab4835 | -21.13355 | -42.07618 | 2025-02-09 04:12:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 041d7955-d0ea-3b4e-b3db-07c76633c0b4 | -21.6125 | -48.45792 | 2025-02-09 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4746dae-7235-3001-933f-0d6cfd7691c9 | -20.28348 | -49.92146 | 2025-02-09 04:12:00 | NOAA-21 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 130328da-f1be-3d29-8ea6-2d94686f5878 | -23.98347 | -48.91791 | 2025-02-09 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 097fd49a-b87f-3629-808a-b9d88de85425 | -21.89617 | -53.72206 | 2025-02-09 04:12:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42874be8-50c3-353c-ad0f-f88c3a43c151 | -21.09008 | -44.61108 | 2025-02-09 04:12:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 81b414de-716c-3107-82b1-a2a347e0c6be | -21.17954 | -43.98016 | 2025-02-09 04:12:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 20385285-b043-316a-a592-268f1946372d | -23.98704 | -48.91864 | 2025-02-09 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 756f554c-eb38-3748-9c8e-f8dc49e1cace | -22.67774 | -42.85723 | 2025-02-09 04:12:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 45c75ce2-05a8-3e52-892b-60f5afc04e67 | -23.59408 | -47.43752 | 2025-02-09 04:12:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d5c2abe-747d-3fcf-9e0c-80641bdb7f54 | -20.28675 | -49.92606 | 2025-02-09 04:12:00 | NOAA-21 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6df6825-045d-32ff-9161-c2771ec8d190 | -30.05545 | -52.10055 | 2025-02-09 04:14:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| b9562a4c-2777-3d77-b789-52c661d91a9c | -30.05923 | -52.10156 | 2025-02-09 04:14:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| bdf32377-023f-300d-96be-33d5fc6b4ef0 | -6.978 | -42.9977 | 2025-02-09 04:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 5bd5fe46-faac-3bfb-8cfd-6a43815a44db | -6.978 | -42.9977 | 2025-02-09 04:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 0d30f8fa-a0f2-3798-8e37-cb3f05c85432 | -7.1316 | -34.99341 | 2025-02-09 04:31:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bcb97072-4640-3217-90d9-01ca0d395bc8 | -7.13236 | -34.98736 | 2025-02-09 04:31:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 97120c29-294d-320d-93cb-dd912bd5802b | -7.13923 | -34.98878 | 2025-02-09 04:31:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b8457a05-efab-30d0-9eb2-86884750cf4c | -7.13845 | -34.99496 | 2025-02-09 04:31:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b9929e24-0721-376e-b1f4-0d950acaaa85 | -7.13989 | -34.99273 | 2025-02-09 04:31:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 11484d39-4c7e-37e0-9462-5c8fe463ef7f | -7.13303 | -34.99131 | 2025-02-09 04:31:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 41a47bcd-a3fc-3d94-9042-f5c9c4f4acbb | -12.209 | -50.92815 | 2025-02-09 04:33:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe6e2e1e-d762-34f7-ab71-8a463a3dd42d | -12.34515 | -52.49042 | 2025-02-09 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f8c4ea3-d00d-3d8c-beae-4d7ca6ce2b87 | -7.24463 | -44.71675 | 2025-02-09 04:33:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3181e90-7e02-3faa-8c6d-9bfc8efe274a | -12.35308 | -52.48747 | 2025-02-09 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed6637e1-1be2-377b-85a4-63fa597e8863 | -12.21301 | -50.92502 | 2025-02-09 04:33:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5852805-7f47-3d09-8b1d-40631581484a | -6.98271 | -42.99386 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 80af7c7c-0bbc-3e6e-9195-93d054fe66ee | -6.98325 | -42.99023 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9a9462c5-cd23-3392-b251-65582fe85a30 | -12.2124 | -50.92873 | 2025-02-09 04:33:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 174932cd-ed04-3507-b2c5-fa357d1c0427 | -6.9781 | -42.99687 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| bff12361-4512-3e37-bbe4-a05f03b0ba5c | -6.97917 | -42.98964 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7c83b470-7fea-3db3-ad20-746c52a50b38 | -6.97757 | -43.00043 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| f1c3f173-82a3-3646-add2-23918e16523f | -7.22988 | -44.71452 | 2025-02-09 04:33:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c03e6bc-351f-3dc4-a387-188b40c3a596 | -6.97863 | -42.99327 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0852c5f5-20b8-36ae-afc4-e14bd388549f | -12.34587 | -52.4862 | 2025-02-09 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbe7080d-3e1a-32fe-aca2-86873a2f55d9 | -6.59815 | -44.1983 | 2025-02-09 04:33:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4697770b-3215-3b9f-bd58-2780bd721f80 | -6.6297 | -44.11606 | 2025-02-09 04:33:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddaaf883-7985-311e-8e48-d6ae36e1fde7 | -7.89852 | -43.91758 | 2025-02-09 04:33:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e13bf2-7a12-352f-832c-72a30cfd73c2 | -12.35019 | -52.48263 | 2025-02-09 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf5e2ef6-04cd-38d1-a435-63cd34f05585 | -6.98218 | -42.99746 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 63e50275-176f-3181-bb43-592ef73c51d4 | -6.63033 | -44.11399 | 2025-02-09 04:33:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b76b729-1f6f-3db0-a9d1-7b89c6839b13 | -6.98165 | -43.00102 | 2025-02-09 04:33:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| ade68673-4176-3b45-a719-aea4f903d594 | -6.62932 | -43.03419 | 2025-02-09 04:33:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ebb4690-39df-3e14-ab09-9dfc82a7a0e2 | -7.47507 | -46.23129 | 2025-02-09 04:33:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bb4fef01-e40b-321d-8fac-3489eb7d722f | -12.00642 | -48.91749 | 2025-02-09 04:33:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca8f8455-57f2-31e3-a1c0-0f367de54ab6 | -12.34875 | -52.49105 | 2025-02-09 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9388ee6b-fd8a-35ee-b2da-24375372f792 | -7.47162 | -46.23077 | 2025-02-09 04:33:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 884d93d6-313b-3d36-9c40-e63414b8d353 | -12.34947 | -52.48684 | 2025-02-09 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678b4035-a6a4-32fb-8edd-f088ad1922d4 | -19.51921 | -49.28907 | 2025-02-09 04:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f344f027-fa58-3f80-a30a-3aa6bf379290 | -13.61715 | -55.45776 | 2025-02-09 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c068a5f-402f-3e2b-b338-5279ebbe6c9a | -13.61367 | -55.45294 | 2025-02-09 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c07f84f7-d3dd-33bb-ae6a-d94bcde0f108 | -17.75873 | -42.94563 | 2025-02-09 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8c35c88-4750-3b4d-9f73-6dd0cd372a4f | -17.00962 | -49.78136 | 2025-02-09 04:36:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a865751-b7f8-3aa4-a2eb-2e42f58a6b1b | -19.82535 | -40.10217 | 2025-02-09 04:36:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5b7fac78-42c5-3794-96a8-18c8d5c0b744 | -19.8232 | -40.09898 | 2025-02-09 04:36:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 689bfc25-60dd-3ca2-b202-ab962160d94e | -17.75395 | -42.94501 | 2025-02-09 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d45ce45-caa4-397e-a39b-9a2d548749fc | -13.62699 | -55.45137 | 2025-02-09 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9943cc0-69d5-3704-8d41-c7ebcb22226c | -13.61788 | -55.45372 | 2025-02-09 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 003c4a5c-458b-3774-8855-1a17db30209c | -13.62208 | -55.45454 | 2025-02-09 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73921ccd-19bf-3f39-ac12-a2c21835724a | -19.82579 | -40.09771 | 2025-02-09 04:36:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f336a5a5-81b2-3354-a351-4c243caac00f | -13.6228 | -55.45052 | 2025-02-09 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1ff5d2f-13dc-390e-81a9-fd160882c954 | -18.59778 | -53.15578 | 2025-02-09 04:36:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2d396c6-0982-3646-bfe0-6032a2f5dee2 | -25.57302 | -49.35481 | 2025-02-09 04:38:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a70ba2ff-3107-3e0e-b941-f4982bdeb0cb | -20.2851 | -49.92166 | 2025-02-09 04:38:00 | NPP-375D | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c839df9-dbaf-3bf3-9226-808efeebadad | -25.56756 | -49.36778 | 2025-02-09 04:38:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f0f14494-7db5-382e-bf8f-b9b1224bd1ce | -23.59304 | -47.43856 | 2025-02-09 04:38:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6151df22-b480-3c1e-ada6-8b947b7586dd | -21.61467 | -48.46301 | 2025-02-09 04:38:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18a8b731-dd39-34f9-99ed-c074a444f86e | -21.07768 | -56.39194 | 2025-02-09 04:38:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 946e06d6-3f4c-382d-9fa4-3c9cdbe3b082 | -21.89867 | -53.71832 | 2025-02-09 04:38:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 492175ad-4fc4-3e7f-8b6d-7a47e7c48a57 | -22.88256 | -52.72958 | 2025-02-09 04:38:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a1d1b03-7c33-3a08-bea2-83ea005d45de | -21.61578 | -48.46098 | 2025-02-09 04:38:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3f61605-8570-3a62-9d35-8e0a66ba60ed | -21.19361 | -44.93719 | 2025-02-09 04:38:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53dbedd8-a9c3-36b3-bdda-28eca13b70f6 | -23.33695 | -46.77328 | 2025-02-09 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a0db69d6-872a-3f3f-8da7-1d7bc1140d6a | -21.89454 | -53.72165 | 2025-02-09 04:38:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
