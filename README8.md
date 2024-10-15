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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27cf38bc-47a7-39ea-ab2f-6d6bd943f485 | -14.09063 | -46.17822 | 2024-10-15 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 739.3 |
| 9d9c4060-88b1-371f-9d40-70ec9e3b5a06 | -14.08977 | -46.17168 | 2024-10-15 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 901.8 |
| 3bf8b53b-4627-3888-b8ac-9644620c46df | -14.07782 | -46.20192 | 2024-10-15 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| af38ed94-bce2-374e-ad5e-c046e1be8c22 | -14.0757 | -46.17987 | 2024-10-15 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 479.7 |
| fb380731-d3bb-30c6-8bd4-c9ed6186e694 | -14.07484 | -46.17337 | 2024-10-15 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 394.2 |
| 77b3fda9-bd19-34fc-a543-322e701ec48f | -13.87755 | -43.04131 | 2024-10-15 00:20:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4b04c755-edce-3eaf-8335-12a05dd555dd | -13.19289 | -42.4851 | 2024-10-15 00:20:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 65c00812-b462-3a4f-a30b-2b8589f527be | -13.19123 | -42.49088 | 2024-10-15 00:20:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| a7dd19eb-a6dd-3afb-9537-be4e615bd4bf | -12.8795 | -44.61816 | 2024-10-15 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1b1ca6a4-2621-3b3c-973d-259233710030 | -12.8681 | -44.62497 | 2024-10-15 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 6f451010-9129-3d1c-8ff4-6ad0be14ee2b | -12.86567 | -44.60442 | 2024-10-15 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 324d903e-49cd-3711-8b21-cacfa53e86fe | -12.37754 | -42.75442 | 2024-10-15 00:20:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 50d8353e-7e23-364c-bab3-5d9ab4bfd207 | -12.37571 | -42.73996 | 2024-10-15 00:20:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| a4cf5802-7a0c-319b-a22d-c16b4d465bcc | -12.08784 | -43.90421 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b9a70b13-5f3a-35c4-9dbb-7b5a6927258c | -12.08565 | -43.88669 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8cd0fc5f-5bd6-3c1d-8bea-f0939b681133 | -12.08049 | -43.89946 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| ac5e9924-6d11-364f-b241-6dce277dc1a7 | -12.07842 | -43.88186 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 7ffc2895-7f41-3f4b-8c80-1fa403547649 | -11.89401 | -43.81784 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d950732d-f5f0-332e-825e-0851d235dc2c | -11.88983 | -43.83022 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a257700c-8a45-3bdb-ad2f-391a85dac62f | -11.8878 | -43.81299 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 783ff519-c356-3646-ad87-f23415452399 | -11.88207 | -43.8194 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5b2b4be8-e251-3ce0-bcfc-3fd59a0b2120 | -11.87992 | -43.80222 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6c461225-e732-3e3a-b819-7bae784d48c5 | -11.87586 | -43.81455 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1fabc97e-6612-380e-b2f7-7ecfae82ad16 | -11.1352 | -44.19254 | 2024-10-15 00:20:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7071a1aa-2724-3d31-b6dd-ecd12a614492 | -11.07372 | -43.88324 | 2024-10-15 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d551e383-3ce6-3e33-af57-73243086e0aa | -11.06749 | -43.8904 | 2024-10-15 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9e90e796-cc29-3e71-91e3-08c18212905c | -10.94744 | -43.75922 | 2024-10-15 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d0ebd419-7a6d-34ee-88dc-fa423fe2105f | -10.93367 | -43.74435 | 2024-10-15 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 80c2e604-ea94-33fd-aae5-bfd946f098b8 | -10.8392 | -44.4555 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 18820578-42b0-3337-b9cc-58588e2aabcd | -10.75647 | -44.84112 | 2024-10-15 00:20:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 653df166-11f5-3ce3-b997-7a08cb456002 | -10.53746 | -44.86691 | 2024-10-15 00:20:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ac0254eb-6ea4-32c1-9c62-b8a98f52399b | -10.52141 | -44.20441 | 2024-10-15 00:20:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 83247929-f247-34cc-8d23-94ba1fa79106 | -10.51923 | -44.18679 | 2024-10-15 00:20:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ff564b3b-1ee4-3b4c-b42b-9d79e49857c9 | -10.50933 | -44.20585 | 2024-10-15 00:20:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 5b2197cf-e6ec-3076-b744-1da1dc66bc1c | -10.50716 | -44.18819 | 2024-10-15 00:20:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 50aceeb8-b938-346a-b6de-3457c25c8cdf | -10.49118 | -44.91222 | 2024-10-15 00:20:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b905f604-fc3e-301d-85c1-043e37ec2a46 | -8.86946 | -40.87787 | 2024-10-15 00:20:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 7fb73e19-d330-306a-8a52-a9d8055ab760 | -9.45216 | -44.18076 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 96b6b15c-f396-39f7-9644-eb3991e38a20 | -9.45319 | -44.15342 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 10081030-a56f-3196-a8ba-2c58837818db | -9.45746 | -44.1865 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3eb03306-d8e6-3c69-b6f3-49c0015e44f0 | -9.45995 | -44.14609 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 916f02b4-156f-3cd9-a01b-c6b4228b5f2d | -10.48245 | -42.4435 | 2024-10-15 00:20:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 72.7 |
| e6eceae7-ee5e-3de6-854a-c8da2cfefa23 | -10.4684 | -44.07005 | 2024-10-15 00:20:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e61aa189-88a4-3a8c-87fb-3c9d7d2d58ae | -10.39024 | -44.83222 | 2024-10-15 00:20:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1c737ae4-b865-3017-a085-dc357bd1ba1a | -10.38791 | -44.81289 | 2024-10-15 00:20:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 3ba97fc7-8a6a-3a30-b888-86d6f56bbf1e | -10.26184 | -43.97335 | 2024-10-15 00:20:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9d98dd01-b16a-31a3-91a3-f96bdba6c150 | -10.25509 | -43.97971 | 2024-10-15 00:20:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6af988bc-56af-3bfd-bd2f-461f15dc2143 | -10.09042 | -44.21973 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| eaed3354-fc06-38c5-8ffb-af82210f84a7 | -10.08822 | -44.20242 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 42dd0ab8-2dff-30d2-a8f5-1fc349e8f7c6 | -10.08061 | -44.23867 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2fc02afc-8c5d-3fb0-add6-a8210ea00b7c | -10.07624 | -44.20395 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 07372c84-f6c6-3f2c-b480-cd2722b51cd9 | -10.05869 | -44.25877 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5cca904c-6ac7-3111-9d49-bd595e18eaa3 | -10.05135 | -36.4039 | 2024-10-15 00:20:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 425b9bbf-b5b8-3e3a-8fd4-8f65b7882ee2 | -10.05018 | -44.19 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 903aeb67-a803-3a55-9ee2-c343e1c2ada4 | -10.04032 | -44.20858 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e4177f00-b363-34ca-9860-81382de0695d | -10.03821 | -44.19144 | 2024-10-15 00:20:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fd972601-bb29-3c49-aa0d-59fb42def6d6 | -9.94162 | -48.15126 | 2024-10-15 00:20:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 02d87b80-fbbf-34fd-a56a-166c9dee1b40 | -9.69054 | -46.48981 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 625957bd-4778-3b31-a770-b6b854a408d7 | -9.52829 | -47.79034 | 2024-10-15 00:20:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a07fcd0c-f7a3-3ff5-a645-00a830e884a5 | -9.52195 | -47.78448 | 2024-10-15 00:20:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cc1889b0-23a5-33f5-bede-59866c01ba9e | -9.5073 | -45.83599 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6e5875a1-6eba-3478-bbe2-0650198c0bf9 | -9.20133 | -48.66113 | 2024-10-15 00:20:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 6858fc3a-4c03-3304-aaf9-cc4318a5a504 | -9.19684 | -48.66661 | 2024-10-15 00:20:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 29.9 |
| eaa4dc3c-5495-3db4-9de4-97443f1c8155 | -9.19669 | -47.56007 | 2024-10-15 00:20:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 70fff293-48ee-3064-ac88-dc7a828968ac | -9.19309 | -47.52987 | 2024-10-15 00:20:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| bd4709b5-1ad0-3b11-8eed-2440827fe7d3 | -9.18908 | -48.85767 | 2024-10-15 00:20:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 10001673-7b6c-32c4-a4e1-8577a397cd18 | -9.18581 | -48.86253 | 2024-10-15 00:20:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 4c58bbb5-ec02-35b7-aac1-f547fc23ead8 | -9.13892 | -48.55823 | 2024-10-15 00:20:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d16ecdf7-4702-3e97-935e-2d12bd9cb3d2 | -9.09227 | -47.806 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 54bd7bcc-0aec-3d0e-94f4-1954ad5558b0 | -9.08836 | -47.77414 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 383a05d4-b69d-3da5-bf02-9c8047e534b2 | -9.08657 | -47.80159 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ea41ed34-9de3-3b66-bad6-70752794bd1b | -9.08291 | -47.76976 | 2024-10-15 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 24fd04b5-7b20-3694-9c92-0a5ac014c460 | -8.92272 | -47.90395 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| a2324263-0bd9-3d97-9b07-c084214fb6d9 | -8.92032 | -47.93181 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 27a54b1a-99f9-31f1-ba5d-d4d12b33cb58 | -8.91659 | -47.89939 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 1581c436-dff6-3e0c-b3cf-b76dabb21205 | -8.91087 | -47.93841 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| f0261190-e431-3b05-9dcc-77134bc7f871 | -8.90694 | -47.90613 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 795a4ec2-eca2-38e0-a031-a6b458a128ed | -8.90449 | -47.93386 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 88168845-5cdb-3266-bbf1-33ecbf9f81c7 | -8.47492 | -47.82707 | 2024-10-15 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| d851c5c7-2a28-3224-9628-3213da620d42 | -8.46995 | -47.82067 | 2024-10-15 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| bfafbf4b-1556-3247-a4ae-a5c8a1d3b26f | -8.45932 | -47.82911 | 2024-10-15 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 53441f03-aef8-3f7f-9d35-9e99507371f1 | -8.45548 | -47.79821 | 2024-10-15 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0fed98cf-96dd-384b-97bd-3006b05ad63d | -8.45438 | -47.82295 | 2024-10-15 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 8f4435c5-a198-375d-b9be-0f06c44e0387 | -8.45074 | -47.79177 | 2024-10-15 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| b8f46472-cbf3-375b-ba34-59bc3a332d64 | -7.87267 | -47.74975 | 2024-10-15 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 29155be8-c3fe-3aab-924b-28ce86ae8b25 | -7.86912 | -47.74347 | 2024-10-15 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| fea3ffe6-44bc-3928-98d1-942678c74797 | -7.52547 | -49.49536 | 2024-10-15 00:20:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 2069b0f4-3bd4-3541-a816-699d10760c31 | -7.50805 | -49.49761 | 2024-10-15 00:20:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 960dd2cf-5e83-361a-8d8c-145a78358be2 | -7.49473 | -48.10685 | 2024-10-15 00:20:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e1a25ad1-1bcb-31eb-9da8-063f5b1dc367 | -7.1252 | -45.3541 | 2024-10-15 00:20:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3f65fa79-ca03-326b-8631-24b738ab32ad | -7.0559 | -46.8205 | 2024-10-15 00:20:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 797e3029-8afb-3c2f-a0ce-9625062b1da6 | -7.0378 | -47.37465 | 2024-10-15 00:20:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c7fa31e0-0e82-326b-b37b-ebb3aee7e7ce | -6.9479 | -47.50541 | 2024-10-15 00:20:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6fce1da9-950b-3d87-a3dd-cd3a5ed84c57 | -6.86509 | -47.93861 | 2024-10-15 00:20:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3471af7d-0b24-33ee-8764-98c7dcd13c99 | -6.81409 | -44.4746 | 2024-10-15 00:20:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| bdb89dbc-e878-3aaf-9fe4-3d79b544cc18 | -6.81198 | -44.45858 | 2024-10-15 00:20:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2f0129ec-4b40-3728-9bca-c67a6bfe538c | -6.41969 | -49.61831 | 2024-10-15 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 6375f939-0884-3ce0-885c-5f89376c4469 | -6.41789 | -49.62403 | 2024-10-15 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 07f66e6c-f281-311c-af4b-0fed901254dc | -9.58707 | -43.51167 | 2024-10-15 00:20:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 16f37f50-3553-3023-baa7-cb75d84380d2 | -6.41482 | -49.57816 | 2024-10-15 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |


[Clique aqui para ver as próximas entradas](README9.md)
