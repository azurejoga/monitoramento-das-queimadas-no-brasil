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
| 27be9c3f-dcdf-3da9-9e2c-f04421f11760 | -6.9602 | -42.9052 | 2025-06-04 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 3bc3df65-0e08-32bf-8fe7-279c861279d6 | -6.9791 | -42.9034 | 2025-06-04 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 42d48531-a08c-30f4-8685-f7129bc9ab76 | -9.6319 | -62.817402 | 2025-06-04 01:49:00 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f4b0ae4a-094e-3aca-9507-76b23fb85c49 | -9.6109 | -63.255901 | 2025-06-04 01:49:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c21c2167-adba-31a4-abad-4fdac613b709 | -12.182 | -64.199097 | 2025-06-04 01:49:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 087ecec7-f641-35e8-ae0f-ae8754475fee | -11.5674 | -56.420502 | 2025-06-04 01:49:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90c0a216-bcc7-3008-86f0-7ad49b32f8b8 | -6.9602 | -42.9052 | 2025-06-04 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| bcc0674c-9c06-37f9-94b0-a9447b20d3bf | -6.9791 | -42.9034 | 2025-06-04 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| e6871f81-9bc5-31d8-82ba-a29582a8e477 | -6.9602 | -42.9052 | 2025-06-04 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| d190645c-e3fb-3b15-82c8-509dcd8ecf10 | -6.9791 | -42.9034 | 2025-06-04 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 16f1140e-e28e-3125-9cb5-035e95ada063 | -7.9116 | -50.3666 | 2025-06-04 02:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 32be902d-c5f3-3abc-8996-c82940f81200 | -7.0169 | -44.5954 | 2025-06-04 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2d955e8f-ef99-353a-a3f7-338d6b2fa267 | -6.9602 | -42.9052 | 2025-06-04 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| a3627b3a-5107-32bf-b914-a056cbb5adab | -6.9791 | -42.9034 | 2025-06-04 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 1a8bd930-a584-394b-9698-6aa8a594f5c5 | -6.9602 | -42.9052 | 2025-06-04 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 10b3289a-6506-3f45-a4f8-55b54ca31c0f | -6.9791 | -42.9034 | 2025-06-04 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 2d5ffa35-39a5-37f8-a5dd-eb9b512c2ebd | -6.9602 | -42.9052 | 2025-06-04 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 00cf9432-fac3-37a9-9ee4-90914462a9b5 | -6.9791 | -42.9034 | 2025-06-04 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| a45f3db2-681e-3a27-bf1f-3db0bdadd2ce | -6.9791 | -42.9034 | 2025-06-04 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| eea49e64-602a-37ce-a8f9-d75e1b448d25 | -16.3164 | -49.91 | 2025-06-04 02:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 988a1d5a-20c3-375b-bb6e-d771258e4950 | -6.9602 | -42.9052 | 2025-06-04 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| cf5f4e50-abcd-388e-9050-cdb9baae973d | -16.3159 | -49.9321 | 2025-06-04 02:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 16ba31d9-2f07-3aa6-be22-6bc3c9d198de | -6.9602 | -42.9052 | 2025-06-04 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 3056df35-5b36-3c82-8fe7-9cd225084862 | -9.4964 | -40.3088 | 2025-06-04 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| f3fae574-186f-348c-91e9-74c2ea658eef | -6.9791 | -42.9034 | 2025-06-04 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| ec77dd85-3b20-3018-b349-ddd2b85b7b99 | -9.5156 | -40.3061 | 2025-06-04 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 80dedc8e-2314-3cf2-b42d-80a3bdd86983 | -6.9602 | -42.9052 | 2025-06-04 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| ea669597-1644-3e52-ad00-6b84d824c365 | -6.9791 | -42.9034 | 2025-06-04 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| da3f4093-416e-3ba0-8255-a8d1747bd242 | -6.9602 | -42.9052 | 2025-06-04 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 940ed96f-db65-35d3-8bee-a85f773f0742 | -5.22696 | -37.66274 | 2025-06-04 03:10:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bc138529-18ce-336e-8c88-10121a50582e | -5.22768 | -37.65855 | 2025-06-04 03:10:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d65d49aa-76cc-3638-94a1-2ff1154a7d5b | -5.22721 | -37.6574 | 2025-06-04 03:10:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f79d16c7-9e36-3051-8d14-c67320d700be | -5.22646 | -37.66158 | 2025-06-04 03:10:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b3211b22-8f3d-373c-9d58-72f31dacc777 | -9.4961 | -40.31094 | 2025-06-04 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5b002df2-787b-32bd-8505-ec82051d6ff3 | -9.50048 | -40.31647 | 2025-06-04 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 40bbe84a-b685-31c2-9dbe-20fe7a2aad5e | -9.13995 | -41.00679 | 2025-06-04 03:13:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f9cd5e00-7233-3e38-877e-aadf346bdc84 | -9.50252 | -40.31213 | 2025-06-04 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 38f110da-43b4-3f2e-b020-c600f9e14e98 | -9.14112 | -41.00074 | 2025-06-04 03:13:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5b5ebe4-dcd5-3236-998c-4d01478403fa | -9.50151 | -40.31105 | 2025-06-04 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d79c8c78-6064-3a76-ba23-bc3535af3f8a | -9.1432 | -41.00461 | 2025-06-04 03:13:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a0554317-14de-33fa-9ee2-ed928b01e384 | -17.77958 | -42.8101 | 2025-06-04 03:15:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60396027-043f-35c0-bb5e-6c963f8367c8 | -17.75369 | -42.89457 | 2025-06-04 03:15:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72778712-f12b-34ff-8932-0e3125311b9d | -6.9602 | -42.9052 | 2025-06-04 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 2972c826-394e-37b3-9412-e30ce102b362 | -6.9602 | -42.9052 | 2025-06-04 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| e46599ee-69be-35d7-b534-008422b3eb72 | -6.9791 | -42.9034 | 2025-06-04 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 74c1bc32-605d-390e-a5c6-9e43155bc063 | -4.11836 | -38.33811 | 2025-06-04 03:36:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6d8f080-6ff8-3cfd-8abc-07aefb1095ba | -5.22797 | -37.66067 | 2025-06-04 03:36:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 74f3548b-8e6c-37ae-b0b9-472240ad5356 | -4.00339 | -43.24358 | 2025-06-04 03:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27448302-5f6a-3b3a-8d3d-2a16ff11ed98 | -4.91158 | -37.40993 | 2025-06-04 03:36:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 072eae5c-1357-3a6e-874a-eaf058972745 | -4.00911 | -43.24456 | 2025-06-04 03:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71d833bf-6661-3b1c-938c-b1ce54600e9c | -3.13455 | -41.78993 | 2025-06-04 03:36:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 0f54b310-d4aa-34f3-9c4d-011beb217112 | -3.1351 | -41.78669 | 2025-06-04 03:36:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c4a88769-ff66-3c90-b1c2-b34fa2865b3f | -4.1208 | -38.33876 | 2025-06-04 03:36:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b5cd975-db34-3ac3-ac5b-860a2fdec580 | -7.68782 | -44.57402 | 2025-06-04 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a52bc6bd-fea1-3f8a-91d3-d17d30668ade | -10.26496 | -48.46114 | 2025-06-04 03:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3747d92a-6332-3688-ab08-b2caf65e6aeb | -6.96099 | -42.91531 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b9e86d9f-f239-3ef5-86af-eb456e99b225 | -6.96748 | -42.90971 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 6f6e460b-26aa-3659-a971-16fc63ab90fe | -7.88758 | -46.19067 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b27abba-7c31-330c-b30a-af096750b960 | -7.5887 | -45.86673 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e78648cd-be71-3e3d-8fb0-e888c593115e | -7.68858 | -44.56975 | 2025-06-04 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da21347c-c14d-3a81-a59a-94164c489a9a | -7.22372 | -43.12505 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0af3721c-8cd2-39ce-ac27-cd240acc883a | -4.81304 | -45.26453 | 2025-06-04 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d25463da-6881-3f41-ab09-848aba0aef8d | -7.88211 | -46.18674 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73613416-7007-36cf-8d09-2c5cad822e5b | -9.14009 | -41.00122 | 2025-06-04 03:38:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 982626c1-1d6f-3af2-850b-84ed087d2735 | -7.55541 | -45.83395 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a1d6a37-be78-3b04-b2bc-186056daf4f5 | -6.21297 | -43.34064 | 2025-06-04 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5c84e02-551f-3187-a27f-7d6ef97a6cd0 | -7.55444 | -45.83902 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 293e43ae-f21a-31b7-a119-e86c8170af4e | -7.22911 | -43.126 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 301d2ec3-39ce-36bb-9ece-ed3c48db1daf | -10.69706 | -37.04903 | 2025-06-04 03:38:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f258474b-7540-32f9-ad73-0423f6250efd | -7.89388 | -46.19529 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a644af2d-5ab3-3a73-b093-357c6ea22484 | -8.55373 | -44.55638 | 2025-06-04 03:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dac90465-d084-339d-a8b9-32ec7d8703f5 | -10.26168 | -48.46273 | 2025-06-04 03:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b26c2705-a20b-3f72-9c82-3a193c2c3242 | -6.96275 | -42.90537 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e8072d7a-54a9-3097-977d-c2caa534a3ac | -7.01674 | -44.58554 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3d6f3c73-aba4-375d-8436-6cfa0eef3af1 | -7.01409 | -44.58293 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 385c1407-60a1-33ae-a1bf-1dd771273437 | -7.88647 | -46.19918 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad3649e0-1ada-313b-92af-493627960bf6 | -7.69306 | -44.56945 | 2025-06-04 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f140019-d1b2-32e7-9da9-24d69f571620 | -7.89389 | -46.19262 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83cbd67a-7159-338b-9337-5523644b9d04 | -8.07493 | -43.11222 | 2025-06-04 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a0b7f21c-cc86-3131-864f-6ef93169d9a7 | -10.70761 | -48.77653 | 2025-06-04 03:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9579c43b-1e0a-3fe1-90b3-56b5b3b355b3 | -7.00954 | -44.60826 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3c68c831-4da4-3198-b044-0db54392f2f7 | -6.37185 | -43.68253 | 2025-06-04 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6e0b719-41f8-31b4-8ec2-9b65d5f5b08c | -10.55011 | -42.43908 | 2025-06-04 03:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 21ed5904-dc91-3910-a9d3-d1fb599b0b53 | -7.01786 | -44.59609 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 14b23a72-b41a-3156-a5f0-c9d14acbfda6 | -10.26303 | -48.45597 | 2025-06-04 03:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2e6de89-008c-322d-8e06-1099a1409dd2 | -7.6864 | -44.57261 | 2025-06-04 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b38cdf76-09e6-33c7-867b-c4a397d08b49 | -7.01518 | -44.59391 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f73ea4f6-7a28-379b-8e78-e92820eb458a | -7.98202 | -47.2355 | 2025-06-04 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9aa914b7-e101-3b13-81ec-3cba50dcc4da | -7.58968 | -45.86147 | 2025-06-04 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a66be057-c696-3c24-825c-f144ca4aaee2 | -7.01595 | -44.58977 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 759189bb-ffed-38a1-9f34-21668f891111 | -6.21363 | -43.33693 | 2025-06-04 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ace07ee5-9af6-33ae-bb0c-20ee3a725094 | -10.67468 | -44.38391 | 2025-06-04 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 226b7236-2df1-3e62-a0d2-5f4fd7e2769d | -6.9669 | -42.91301 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.8 |
| a8e1b749-001a-3d7b-827d-e73e9f055ff5 | -6.96334 | -42.90208 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 03adc10e-1ef5-39a6-8abe-d3901e89a8f1 | -6.9728 | -42.91077 | 2025-06-04 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 5902160d-b48a-393a-9a20-e8afe22114bd | -7.14695 | -44.045 | 2025-06-04 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46706f9b-7318-3ece-a2c7-4e98bbdfbb2d | -8.06844 | -43.11777 | 2025-06-04 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 7a06811e-5db5-397c-b541-b096788c24ec | -7.98866 | -47.23791 | 2025-06-04 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfa6b322-6056-31a2-83ab-e2d6a185359a | -7.00755 | -44.60188 | 2025-06-04 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b500335d-8f43-342a-9ba8-9c66566872fe | -6.68696 | -43.687 | 2025-06-04 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README4.md)
