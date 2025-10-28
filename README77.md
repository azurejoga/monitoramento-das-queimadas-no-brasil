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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0052e091-a824-3d13-8414-b6397f7251c7 | -9.46248 | -46.88189 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e7dd3bc-33f4-324b-920f-95858e47e3b0 | -10.60293 | -46.61619 | 2025-10-28 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14a09b02-f7e2-3c07-8a68-8774207ed2c9 | -11.04223 | -47.86093 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a1855ae-4a7e-33d3-a1a3-06ec92116a81 | -7.9638 | -46.75797 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c49f63f9-91e6-330a-8e96-b4a6a4c523e1 | -8.18095 | -45.71891 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daa85c05-55d9-30f4-a284-8ada56210cf3 | -10.56055 | -49.82361 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ad744df-b413-3267-b142-524f36ec0abb | -10.92292 | -50.2652 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2b0ac66-fa3f-335a-8277-0f923f7b85b0 | -10.56423 | -49.7958 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adf6ad9e-5818-3c36-a4b5-b9800987dc63 | -12.09176 | -45.67379 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7561cac7-71f2-3564-a305-611743832b66 | -13.30634 | -47.69584 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce818fb1-e98d-3891-a55d-06330ad14c52 | -9.55934 | -46.96917 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a42a54eb-d8e8-3893-b6a2-6989ed77ef2d | -10.87972 | -48.38077 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1cee5d12-3c42-3db3-9a9f-85837c29ac6f | -7.97594 | -46.74901 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eec9813c-0a2f-3025-9cb9-1656b7ef0f92 | -8.1975 | -46.93623 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49d1449b-7e99-33e2-b616-7a7def61404b | -8.70855 | -47.98751 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 090f17d2-b5d6-397e-8885-e3e2fbc7e18e | -7.67823 | -47.41757 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6df32ab-cc5c-3d2e-bc8b-ff9c984f3782 | -11.28267 | -45.50851 | 2025-10-28 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 59759fbf-6656-3285-8861-b5cc03804c2c | -11.13952 | -44.93924 | 2025-10-28 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90977276-f664-31d7-904f-4c1f92a54542 | -7.97098 | -46.74509 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9298142a-5f8e-35ca-a9a0-a794fa26fbb2 | -9.94946 | -47.1104 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f760a54-b9f9-3b7a-ad3f-c1fd8f5c359c | -10.29257 | -47.24926 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b99c6ead-9357-32cf-98cd-b8d3a3959d1f | -6.948 | -55.25328 | 2025-10-28 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e71d10e-9053-3e27-97f0-fc87d0515707 | -7.97658 | -46.72417 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd557321-f244-38ef-9330-fdbf462562ee | -7.81227 | -46.4554 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c96d6996-e23c-3bc1-ba0a-9150d42cf44b | -7.95371 | -45.46874 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c520bd46-7274-35ce-b431-3536514e603e | -7.07681 | -44.95087 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 56690988-8a76-39cf-9a4c-f7874e07ba10 | -10.5593 | -49.78872 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a60d3de0-125d-3c80-8af6-790e4237e6b8 | -12.08619 | -45.66851 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae54f847-734e-3d16-b3fe-4f9f4bdd0413 | -8.11684 | -55.29367 | 2025-10-28 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1057518-2254-34f3-bc18-fbf41d94877d | -9.4723 | -46.90352 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf76b76a-6506-3d84-900e-b8949b057503 | -12.55192 | -44.94076 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fd8023a-709a-3959-be92-19643848cb74 | -9.41216 | -49.33079 | 2025-10-28 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa95f07a-96d6-3823-9b08-e3c184a4e77b | -7.07203 | -44.94102 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 759cbb61-89c6-3589-b40e-a2e5aa76b21d | -10.58217 | -49.76516 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3fd5493f-e3fe-3c1a-8a87-ba9193aa8927 | -13.6698 | -46.53189 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fcd40cc0-2f9c-3196-bfc9-9da6080a88c4 | -7.86443 | -46.39999 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66a30714-ee95-3ac2-bcac-7f9d5d3beb84 | -7.86534 | -46.39333 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558c91ee-bba3-3ad0-9dd3-eb58984ffda3 | -12.70436 | -46.3195 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3ddc5fde-9500-32c6-85a0-fc674752fbcb | -13.55817 | -47.15889 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eadbcd6d-f48e-3701-8a0f-cafbdd5a08b1 | -7.45497 | -47.16214 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eefc238e-7eac-360c-82a3-25908ad07b46 | -8.17899 | -47.31008 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21e83125-507d-32d3-92d7-76927db5d525 | -10.92245 | -50.27095 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2987848a-b653-3382-ac16-8ea6f9ca6b67 | -13.22515 | -47.10794 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f6cb2e8-f888-3b8f-b3e9-2665ceedb50b | -12.69989 | -46.31991 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dc8563a9-f657-32fe-822f-3bc649224918 | -13.26626 | -47.87412 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 461037ff-3c2c-3c92-a2f7-44c727abfded | -12.07615 | -45.6483 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70ea901b-586b-33ed-b7a0-8b1e974a797e | -10.7582 | -44.75385 | 2025-10-28 05:04:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a607cac9-71f0-33b2-8e5f-ca46c2d74dcf | -8.03834 | -45.14647 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bfc367b-6298-3c62-ad90-fb9b646e712f | -9.34097 | -50.35302 | 2025-10-28 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a5cc997-e411-3bc6-810f-55366df34f21 | -11.0754 | -48.33137 | 2025-10-28 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05606a24-2d42-32b5-ac52-b094c55b90e5 | -13.62484 | -46.47084 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 435c26e9-e643-3fed-94ae-bc28888e7793 | -8.70163 | -50.80583 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f0e0ad7-dc16-36e1-996a-92a0b91985b6 | -10.33604 | -47.78189 | 2025-10-28 05:04:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eb2d14cc-fdb4-3161-852a-ea6d301b06a5 | -7.67521 | -47.41878 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 643f7ac2-8271-3e6d-9782-49c5b3a5d2f7 | -6.54483 | -55.05108 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 478e4a9e-c1ff-32f3-ba3d-a22a834e5665 | -10.28264 | -47.24126 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00367868-cddf-370a-8cee-28c08b9bbc71 | -13.37343 | -47.41031 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e36bd70-033c-33a2-8063-67a087b8edaf | -7.50965 | -46.27964 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5af0966c-c988-307d-bd73-e4bdee201d3c | -9.2355 | -45.60994 | 2025-10-28 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b83cc0a-33b3-3575-b652-c1ad1a20e62d | -10.03295 | -47.16085 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66e3dffc-82b0-3f3c-b24d-521d59f15d4a | -7.83441 | -46.415 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1af2814d-217f-3b7b-9210-3393a79e8f6a | -7.94745 | -45.51652 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 899f96ca-db4b-31a4-bc44-b21a93459fd2 | -8.19288 | -44.43788 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af451b18-1b9f-3b5d-816d-18178886d5e8 | -10.28932 | -47.2318 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c1b36fe-23a9-3d3c-90b2-6a6c630092ed | -7.9647 | -46.75114 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0325493c-cc9d-3c55-916f-1b55f2d8b3a8 | -9.46367 | -46.88441 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf3dc1a3-d05a-30e9-a072-fd307f4c9f52 | -7.35185 | -47.64227 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d827d299-8826-327b-b90c-29835d90653a | -10.22527 | -49.90228 | 2025-10-28 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b78a05be-54a7-31d4-a18d-41665bc552e5 | -10.32772 | -47.1466 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f973b49-d1b2-30bc-9906-1a9ae648fd35 | -13.6235 | -47.04058 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfd5117b-1d7a-3f06-8005-e27d9a408c9f | -12.08323 | -46.3941 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 616f1841-52d9-3e4f-a6da-a83827d4be1e | -7.78461 | -46.44677 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5f3ad55-c471-3f92-8e1c-0030c7a930c4 | -10.5863 | -49.80361 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78912d9e-96a5-3b5a-b7a9-03509fa8ffb1 | -13.2609 | -47.87331 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d00b443-e50b-3063-8fb0-595a2523192b | -7.8114 | -46.45477 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d0e1c13-14ff-3174-bb2d-03bdd19ba902 | -10.92686 | -50.27157 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f51bbe2-6297-3326-8ceb-c7cab880e518 | -8.16116 | -47.00566 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80e27051-ed0f-3a4f-86b5-4e7fa7f067bd | -12.70482 | -46.32876 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 469b1b73-e887-3c89-93e2-5b202c9b9138 | -7.80812 | -46.48663 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 840b16f6-3d89-3562-8aea-34b8ef910684 | -10.88551 | -48.37555 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdd36358-e7cb-30e4-be2c-f59e02d8cfcd | -7.8086 | -46.48306 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49ae5cf1-efc5-3700-bfcd-4d62bc594181 | -8.19398 | -44.44915 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb9c152c-0912-37d5-bc7c-5a6f4e760838 | -10.75679 | -49.78207 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 751d2773-3f51-3630-ad58-fa419febfc7c | -10.91742 | -50.2747 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0dc5db46-d8aa-3c4c-85df-c3800c83b8ac | -6.97062 | -47.3365 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b0876b5-f8fa-3b82-94b4-9a8ab313d433 | -13.53177 | -47.16409 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00c49960-eee6-3c5f-b51a-7cb188e388b5 | -13.63076 | -46.47146 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00af97c3-8c89-3d49-9d2e-c7c61facbd53 | -7.97706 | -46.72067 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1493e11-5252-371f-ab55-0b867abde44b | -10.55698 | -49.78059 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c1026ed-d230-3a3d-9f7c-a11a6020d22b | -9.9772 | -47.16793 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70da2d1a-1776-31cf-8dfc-a7482e6927f8 | -7.88883 | -45.69498 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db366d64-42ed-3aeb-a362-86157b28ecdf | -9.95364 | -47.07904 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d54b7a4-189c-36e1-8b1c-ab5afc43b344 | -8.11919 | -48.82006 | 2025-10-28 05:04:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69b2010e-9414-36f4-b3df-62d13b0b26c3 | -10.88175 | -48.63829 | 2025-10-28 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77aee109-5c7e-330b-92a9-a752f33ac57e | -7.61211 | -46.48016 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3146737-268b-37c9-af03-6b1ae13757d4 | -8.16132 | -47.01167 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 545f4997-abbd-3766-b22a-8988637bc1ff | -7.36648 | -47.79297 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5487ca70-e482-3423-8590-7ad0ab57eebb | -10.57162 | -49.79987 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c56dbac-1a4f-3ffc-903f-f7ae43885c5b | -7.98009 | -46.73836 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ffdaded-a346-32e9-9afd-47d7feddd1da | -7.81046 | -46.46902 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README78.md)
