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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30c182da-5d06-38e4-b04b-283594514d55 | -9.46102 | -63.21393 | 2025-09-19 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0678bf8-deb9-3c84-b368-aef8fb755b18 | -16.68626 | -54.96139 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2977bd50-63c9-350d-8252-3369b93dc5ea | -15.90895 | -59.44189 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cad080ee-eb75-39ff-82c8-6b8e1be37a09 | -15.79767 | -59.40424 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| beef70a6-1679-3f11-9144-a30232dd53ec | -16.68544 | -54.96931 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a72fb539-5bb6-36b5-b675-09ee77a5ba1d | -15.32717 | -59.41106 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49ff2324-69af-3616-a374-7be6808e9800 | -14.83358 | -60.2435 | 2025-09-19 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de1cbd0f-9654-3b26-a41b-90f80688b929 | -15.78238 | -59.38431 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032291c6-7c4e-3aac-808a-7dd5c58f55e1 | -15.30807 | -59.42176 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93091ffc-6b98-32de-aa6b-e51985592d5d | -15.31734 | -59.4185 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 246c50bc-281e-37a6-b482-b7033de7c429 | -16.68585 | -54.96535 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b576919a-266b-31bc-8e9c-7cc7a1ec431d | -19.58886 | -57.81987 | 2025-09-19 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0ca877fc-cdaa-3c8d-b8d9-3fe8e312ca13 | -15.79713 | -59.40839 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecad6c48-360d-3023-a3d1-48d9c5b8cfd2 | -15.77745 | -59.38787 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e594eadd-6a52-3204-9c3b-4e5e047862ce | -21.28636 | -54.8071 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1427329-faa3-3ed9-bc43-8828369cf710 | -16.69145 | -54.96949 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa530548-78a9-3f78-8da0-ab49593e72e5 | -21.2859 | -54.81245 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 93deba89-28ae-3566-9629-530f317a2398 | -14.82493 | -60.24578 | 2025-09-19 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb7d36c-000a-3e2d-97b1-95564f6162d3 | -15.78895 | -59.40261 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1307120c-7de9-3cfa-bc99-0efb8343c811 | -21.28953 | -54.80701 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 608232b1-20d6-3834-92e3-e5b70f74eda0 | -14.82951 | -60.2428 | 2025-09-19 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 288008be-21dd-341f-90bf-ac515698da90 | -15.79331 | -59.40341 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 457a4dc1-17d9-36e5-9abc-b128f22b23fc | -15.78296 | -59.3798 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 502d8917-6f2e-3b97-829a-dfb78732410c | -14.82645 | -60.23458 | 2025-09-19 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 512a0623-53fd-3c00-acf8-a861d5d3f8e1 | -15.91333 | -59.44248 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ac3ce16-1089-3a83-80a7-f62f5dfbea17 | -14.8341 | -60.23975 | 2025-09-19 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e106c421-9e4d-3c6f-8d49-0f10edef44d1 | -14.74398 | -60.20178 | 2025-09-19 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d13b909f-2097-3b99-b76c-f6972f45579d | -21.28322 | -54.80629 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a0eef29-b621-32c2-bbf5-312801be4c3a | -19.58852 | -57.82306 | 2025-09-19 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 14d54871-83f1-33d1-b9fb-aeb2f79668d5 | -21.28544 | -54.81777 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3355ec12-c8b1-37a0-ae61-9bacf03c105a | -15.31244 | -59.42216 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d909f622-f733-36ad-aa84-c4118121d531 | -17.09352 | -55.50829 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6a0f606b-362e-3491-8a9c-00f33406d10e | -15.81716 | -59.46315 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c757964b-7ea8-38d9-ace5-a6b9265cb866 | -15.90956 | -59.44068 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5eec8021-17d2-3778-b172-c2a387766b46 | -15.33644 | -59.40792 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7305b0e9-4a7d-3860-af8f-993fac5fe0c9 | -17.09308 | -55.51247 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b827a600-d31e-304a-b300-a5480f9e5350 | -21.28867 | -54.81767 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c509c889-636c-3b5d-9b37-caf825de8070 | -21.28279 | -54.81167 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 125d336a-a14a-3390-ba89-84147c42cc56 | -17.09398 | -55.5041 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4a8e6953-2de8-3950-8425-c31b97e722f2 | -21.2891 | -54.81235 | 2025-09-19 05:38:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0635ca67-baa4-3393-8d90-807faed3bfe8 | -15.79657 | -59.41265 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 233494ba-8d02-35a8-8783-6d817fbaac23 | -15.33154 | -59.41156 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12d1e963-a8b4-30cd-9320-8d665f6cc10e | -16.69056 | -54.97804 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fc27ff65-a7fc-36dd-ac00-2f5f7eb2d26f | -15.33208 | -59.40738 | 2025-09-19 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 841fbfdf-3048-331f-a2a3-ca65003f404b | -16.69101 | -54.97365 | 2025-09-19 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8361b76-1c25-3257-8e44-0b7341a24531 | -22.23852 | -55.97672 | 2025-09-19 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17ca9c83-981b-3ca6-b2f3-9b83c37091cf | -22.23887 | -55.9725 | 2025-09-19 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1e899e4-acca-3938-8d37-40d1cf328ed3 | -5.53632 | -42.15482 | 2025-09-19 05:42:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c8a16d52-dea9-33b8-b49b-2fbe0bd6724d | -5.13244 | -47.82365 | 2025-09-19 05:42:00 | AQUA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 935396ac-1c7c-31da-8fd8-0ccfb1789adf | -5.72253 | -43.63741 | 2025-09-19 05:42:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1e4e8229-dcd0-3db7-8bfc-a7d411b71ab1 | -3.40551 | -42.98487 | 2025-09-19 05:42:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e1ffd2a-a5d1-3f01-97f7-c63c4263f951 | -5.36387 | -43.007 | 2025-09-19 05:42:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 18a4b655-26b4-3509-89e0-93a815ceca80 | -5.12128 | -47.82202 | 2025-09-19 05:42:00 | AQUA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aa68cf69-2149-31ee-b347-e18a6461f923 | -3.15245 | -43.25838 | 2025-09-19 05:42:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f750ebd8-90de-3078-bfb5-1228023734de | -5.73267 | -43.62991 | 2025-09-19 05:42:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4b0b76a6-5ef5-336c-ae8a-be30d58a3121 | -5.7252 | -43.61981 | 2025-09-19 05:42:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b27eea8f-5aee-37c5-ae01-4654e00ef56b | -5.20824 | -45.17085 | 2025-09-19 05:42:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4fdb2a1-ca73-3160-b2df-b18ce7263563 | -5.75978 | -43.39142 | 2025-09-19 05:42:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2bdb5284-ea55-3fa3-9d31-bfd55cfe31ed | -5.72387 | -43.6286 | 2025-09-19 05:42:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| fefd0613-b090-3e41-896e-0d3aa21c14b0 | -5.53498 | -42.16384 | 2025-09-19 05:42:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0d048f59-97be-3623-bde7-4c6a636ba09f | -9.02149 | -44.96706 | 2025-09-19 05:44:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d9d11812-504a-37cc-a40c-971dfe7f9da8 | -7.36259 | -44.57556 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93d4e10a-a5e1-30b5-bce4-5b79c6a3feb2 | -6.89965 | -44.76342 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 59102dd0-49c8-38ed-92f1-6833956b845b | -10.29877 | -50.20486 | 2025-09-19 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 23770ed5-750a-36d1-99fc-616e8410d887 | -11.17928 | -45.3649 | 2025-09-19 05:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7243131-285c-3fce-9914-24314146fb12 | -6.18529 | -41.19316 | 2025-09-19 05:44:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fdec5ec1-c5b8-326c-a791-c170ecc438a1 | -10.02972 | -46.2326 | 2025-09-19 05:44:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 55498414-96a8-3803-a37a-8dc9c767553c | -5.79122 | -45.35704 | 2025-09-19 05:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c09009a-39ad-3eea-a929-b40cbc2d42f0 | -7.21874 | -44.36643 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c36873c7-63e2-331c-a897-3ae2155c76e6 | -9.14257 | -44.84951 | 2025-09-19 05:44:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b27d41d1-68cb-3e6a-bc38-117a8670f85a | -10.29078 | -50.23407 | 2025-09-19 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 8f6562c1-eb1a-31eb-9186-d582940d17ef | -12.15017 | -44.94007 | 2025-09-19 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 39cd71c4-0be9-35a8-84b9-06b52f05dfa2 | -6.93731 | -44.7571 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f1798f8d-05c9-3359-bb6b-5508227a41ef | -6.92937 | -44.74918 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0cb2fdf8-319e-3c45-86f3-580357019a68 | -8.13713 | -44.46615 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 463e9c34-d2f8-37d1-b6dc-b48408eb7993 | -12.14881 | -44.94905 | 2025-09-19 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9ca58f24-3e9f-3f89-a373-7bd3dd9ce17d | -6.37724 | -43.33171 | 2025-09-19 05:44:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 891baadf-0c6b-3e8f-9c51-7bc8b421f677 | -6.38602 | -43.333 | 2025-09-19 05:44:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56f2421b-4b47-3fdc-8073-e53ab7e3382c | -7.35228 | -44.5834 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 732d2a0c-1931-376a-a446-eb9be46f746e | -7.28628 | -43.922 | 2025-09-19 05:44:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b984a227-b5b1-34f1-a4d8-fdc864c823ea | -5.82014 | -45.90169 | 2025-09-19 05:44:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0afc0f22-a3b1-3155-b1f4-31e8f14ae678 | -10.29383 | -50.21576 | 2025-09-19 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 606bdebd-b08d-36cc-9ae2-f18c0f3c0017 | -8.05832 | -44.08394 | 2025-09-19 05:44:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 81f2583f-5e6d-30dd-a878-1352085f0602 | -5.80441 | -43.63154 | 2025-09-19 05:44:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ebeb587-e6d9-32c4-9616-3b26244b7433 | -12.0851 | -44.82263 | 2025-09-19 05:44:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f5061f8f-40b6-38da-95bb-fa0bc71676fc | -6.89825 | -44.77256 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9c692a78-ab1e-39ca-9d1f-ead46d83e03d | -11.20993 | -49.62585 | 2025-09-19 05:44:00 | AQUA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ebc84968-e513-3934-93db-b0a0c4dcb58a | -8.3739 | -44.67642 | 2025-09-19 05:44:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| affef1b8-aee3-3bb0-bf51-eab970286a56 | -7.57363 | -45.48241 | 2025-09-19 05:44:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5bac2b90-85ad-3623-aaac-1d6353af0c29 | -10.36782 | -42.45348 | 2025-09-19 05:44:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| dbb51de0-888f-3c59-ad2d-42b2a602951d | -7.58434 | -45.47404 | 2025-09-19 05:44:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9517ea86-f268-3834-8062-fa5f9dec5a8b | -10.2785 | -50.23195 | 2025-09-19 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 48360d3a-dcfd-370d-9fd8-2b9b91fc9180 | -7.21737 | -44.3754 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c68bd707-a219-3b80-a2d1-ed8964e3df88 | -12.09659 | -44.80609 | 2025-09-19 05:44:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0f9045ea-a10e-3a97-91f8-d15049af7691 | -9.17357 | -45.30989 | 2025-09-19 05:44:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 98c2ddf1-2738-3208-a1a6-6f2dde71e67c | -6.32434 | -42.38961 | 2025-09-19 05:44:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 219ca30d-1df1-308f-8839-b9f899e9b708 | -7.3612 | -44.58464 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cbf87044-fab0-3bf7-89e6-8a7e1b3474d7 | -5.79271 | -43.89856 | 2025-09-19 05:44:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a05e9b3f-8972-3df9-8505-45e558184ec5 | -10.28157 | -50.21365 | 2025-09-19 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 4087872d-98fc-31d2-871e-9e5d4397fc69 | -10.03123 | -46.22287 | 2025-09-19 05:44:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README37.md)
