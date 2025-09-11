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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b2a2b97-ebf8-3654-a301-6c3a80bb2ad3 | -22.5888 | -51.8985 | 2025-09-11 00:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 184.3 |
| 14ea73e1-3c36-39e6-a3bd-4fc2196dbae1 | -3.1771 | -42.8141 | 2025-09-11 00:50:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 397ee3f0-5a3e-34de-8416-4bb45c045faa | -9.0234 | -49.762 | 2025-09-11 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 4836fad4-23dd-3023-b302-c873f27d995d | -11.0393 | -45.0564 | 2025-09-11 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| d5aca235-41d6-3ef1-8e9c-f0440f680577 | -12.4165 | -63.8038 | 2025-09-11 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0e99c9cc-6a43-3b4e-9db0-3cf26fe961d7 | -12.3975 | -63.8239 | 2025-09-11 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 28f35fbf-df31-358b-9f52-fc54ceea233d | -10.034 | -51.7223 | 2025-09-11 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9b0995fd-069b-3a8d-9265-b245361ec760 | -22.6097 | -51.8941 | 2025-09-11 00:50:00 | GOES-19 | SANTA INÊS | PARANÁ | Brasil | 4123600 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 646b8995-89dd-317e-b018-469fbb75e38d | -13.1644 | -45.2897 | 2025-09-11 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 223.2 |
| cb9349db-bd6a-321c-8bec-7111b78b658f | -11.1813 | -52.0301 | 2025-09-11 00:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 95b1f9ec-208d-3427-8896-fe3a65e68646 | -13.1648 | -45.2665 | 2025-09-11 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 2dd6b9ee-3c7a-3146-8e65-8b6a16ab317a | -6.5706 | -44.1978 | 2025-09-11 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 7e07a0c6-1a31-3064-b2df-85a1acff1ee0 | -19.2016 | -47.9889 | 2025-09-11 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a6da1d3e-42ae-306d-b7f3-3bfa2e82d349 | -10.015 | -51.7451 | 2025-09-11 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ba8ea96e-d577-30cf-ab62-13fef2656ecc | -9.9966 | -51.7049 | 2025-09-11 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 1b46c096-27fb-3d7d-8ae2-a10504a08fb6 | -9.0579 | -46.9688 | 2025-09-11 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d7812283-0fda-34d3-9cc5-60452636d2fd | -9.0753 | -47.078 | 2025-09-11 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 90dab796-70c8-3860-b473-b0908b3f8aa8 | -15.9865 | -42.9719 | 2025-09-11 00:50:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 61e4e238-1d9e-3a3f-968a-a147f46c5079 | -11.1624 | -52.032 | 2025-09-11 00:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 8e5d76fd-64e1-341b-8601-817fab06024c | -20.6963 | -46.0688 | 2025-09-11 00:50:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f278161b-4e9f-3711-9fc3-40e08540bbb4 | -22.5894 | -51.8759 | 2025-09-11 00:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 221.8 |
| e6ce7715-40b5-31b6-929a-2b09e56dc772 | -12.3976 | -63.8048 | 2025-09-11 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 2f158ab8-c181-36e1-8e19-0c1693c268ed | -14.3074 | -54.7492 | 2025-09-11 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 38.7 |
| b4da9f16-1b07-3b70-b6c3-1270d76c167f | -20.4047 | -46.261 | 2025-09-11 00:50:00 | GOES-19 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 16757efc-9160-31b3-a180-e72a78d2cffc | -12.1335 | -44.8508 | 2025-09-11 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 8b51cef0-994c-3ab1-a766-00c73d1e8a08 | -12.3976 | -63.8048 | 2025-09-11 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 13788fb3-6fc3-39dd-940d-135e1cf9d6b8 | -15.1371 | -52.4252 | 2025-09-11 01:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ca3af031-6335-378f-b822-b1841b5f94ba | -12.4164 | -63.8229 | 2025-09-11 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 97dff65d-25f4-37cf-8c09-c76282dc7cf7 | -15.9858 | -42.9964 | 2025-09-11 01:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a08ebc75-e7bf-309f-bd53-579368b0ca65 | -15.9865 | -42.9719 | 2025-09-11 01:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 48960883-95ce-30b3-beee-6f5aff267b36 | -7.3401 | -49.6027 | 2025-09-11 01:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c481324c-b3c0-3185-b4f3-8b8d31aec1d0 | -11.3771 | -46.5368 | 2025-09-11 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 191bb063-7d22-3247-9b23-c5f867aef178 | -22.5888 | -51.8985 | 2025-09-11 01:00:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| 6cbdf337-76ae-367f-8aa1-df7bc152316a | -12.4165 | -63.8038 | 2025-09-11 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5d75a322-1eb4-3143-bbcd-3cb1fb903ba7 | -20.6963 | -46.0688 | 2025-09-11 01:00:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4a3ce704-94e6-3306-958c-db712dc69620 | -14.7527 | -60.2321 | 2025-09-11 01:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3c5d101c-28bf-3b13-9920-c18d06782344 | -11.1621 | -52.053 | 2025-09-11 01:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| e1cf700c-14c5-36ef-94d2-47848005f1ce | -12.3975 | -63.8239 | 2025-09-11 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 95c38197-0a9d-3134-85dd-fb79cd1b5593 | -11.9895 | -47.5971 | 2025-09-11 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 640221d4-c36a-32a3-a063-126c0d625125 | -9.0579 | -46.9688 | 2025-09-11 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3a463b70-a3fb-3ec2-a3a8-c4cd868642b8 | -10.0152 | -51.7241 | 2025-09-11 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 17b7a5f1-1003-3223-b665-07f11b511b38 | -11.0201 | -45.059 | 2025-09-11 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 3ee968fd-4e3d-3737-ab02-235763c04920 | -9.0232 | -49.7834 | 2025-09-11 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c6b06689-b2a8-345d-8f7f-7a3c1b202f1d | -14.7334 | -60.2337 | 2025-09-11 01:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e0196188-0057-3869-9ba2-be2a53515dd6 | -11.1624 | -52.032 | 2025-09-11 01:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 99a213db-6c3a-3185-a8ca-dd1933d3a639 | -13.1648 | -45.2665 | 2025-09-11 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 2c14a3cd-f200-3cb9-974c-8769aeb85255 | -10.1637 | -68.1583 | 2025-09-11 01:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 64b4474b-cfbc-3ee7-bb82-673f604279cb | -13.1644 | -45.2897 | 2025-09-11 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 240.6 |
| a683685a-8d0b-3e34-ba3c-6871e2f646ba | -19.2016 | -47.9889 | 2025-09-11 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 62b7f5ed-022c-3c07-8fbd-994bf535e5ca | -11.3775 | -46.5142 | 2025-09-11 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 815344b2-f157-3307-977e-88635b29753a | -19.2617 | -47.999 | 2025-09-11 01:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| b11c32d8-81f0-3612-8b69-a17c5e418e19 | -7.503 | -48.2551 | 2025-09-11 01:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 408347fc-804b-36c6-8ac8-8369b4736ed7 | -12.0086 | -47.5945 | 2025-09-11 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a6f15e46-f546-34c0-a365-d3956093a7f9 | -9.9966 | -51.7049 | 2025-09-11 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| d51e62ae-98c7-3001-8c1b-81c18878d65f | -19.2421 | -47.9802 | 2025-09-11 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d1fd7b74-b0eb-3033-a8f7-c2208bd32468 | -10.015 | -51.7451 | 2025-09-11 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| fe1a780d-32bb-3857-b1e3-0695c0346c23 | -11.358 | -46.5393 | 2025-09-11 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 233.9 |
| 44d2539d-cb58-38e2-bec5-1542d435efff | -19.2415 | -48.0033 | 2025-09-11 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e32e968f-769c-38d3-810b-5349d65e99c8 | -10.034 | -51.7223 | 2025-09-11 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 311b3f0a-e87a-3af2-bf63-94c448da895a | -22.5894 | -51.8759 | 2025-09-11 01:00:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| 3ea57e9d-4edb-3296-a762-b9880ab4f72b | -11.3584 | -46.5167 | 2025-09-11 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| ece9beaf-c029-3e3d-b125-95cc897821da | -19.9994 | -47.6271 | 2025-09-11 01:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ba77c5ee-7e0d-3eb1-9fd2-ca5f690021c2 | -20.00365 | -47.62754 | 2025-09-11 01:07:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 6fcf2264-07cb-3ffe-87ca-8455834411a5 | -23.25039 | -55.52936 | 2025-09-11 01:07:00 | TERRA_M-M | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 7a51c165-1b27-34a7-8ef1-97854b7381fd | -19.23322 | -48.00417 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 14660f2d-94b4-3ce5-ae98-d4ca27ae8313 | -24.20025 | -51.76361 | 2025-09-11 01:07:00 | TERRA_M-M | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 26398be2-2edc-3177-a364-d6afb233ff1f | -19.9976 | -47.63431 | 2025-09-11 01:07:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7f5b47c4-c02f-34ed-9935-12786ba93905 | -23.35322 | -47.22062 | 2025-09-11 01:07:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 3da1ae47-a138-3e17-ba50-e8dcefe7b352 | -20.40726 | -46.28851 | 2025-09-11 01:07:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5ddff777-a420-34b7-91c1-f47d0a7dc386 | -19.22705 | -47.99878 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6f53fd5a-7869-303a-bd54-2059de97c156 | -19.01675 | -46.24785 | 2025-09-11 01:07:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 35aa9156-64fc-3bbc-97ef-a52e1a5a3391 | -22.63186 | -47.9584 | 2025-09-11 01:07:00 | TERRA_M-M | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 38.9 |
| ce108ce0-b1e5-31de-88ae-6eec807e7579 | -22.66252 | -53.12383 | 2025-09-11 01:07:00 | TERRA_M-M | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| a3a87c6f-164e-389b-bf9d-05f78d6c2566 | -23.73277 | -51.79095 | 2025-09-11 01:07:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 6270f3d8-9593-37a5-95a7-9082015a47c5 | -19.2449 | -48.01942 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| df5be61c-a69b-35e3-951b-09cef6cfba7c | -22.58651 | -51.88674 | 2025-09-11 01:07:00 | TERRA_M-M | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.0 |
| a1447681-6dc5-3ffe-828a-0f34fd1d13b4 | -22.21759 | -46.99226 | 2025-09-11 01:07:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d66cf739-fd10-35a9-b419-87a5f59502e1 | -19.98383 | -47.63635 | 2025-09-11 01:07:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2dc0fedc-e88a-3d34-9e62-6923952a6ad2 | -19.25835 | -48.01667 | 2025-09-11 01:07:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 0b34ab5d-f7f6-3bf2-b58e-035e50467891 | -18.68152 | -47.66398 | 2025-09-11 01:07:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 232f8717-50c8-3ccd-88aa-2669a9065b15 | -22.52098 | -49.09538 | 2025-09-11 01:07:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 193396ad-d2eb-3dd4-919b-5d884a72a524 | -22.71753 | -48.57225 | 2025-09-11 01:07:00 | TERRA_M-M | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b0a0d18d-2369-33b0-86b9-799815cfc1d3 | -19.01828 | -46.27509 | 2025-09-11 01:07:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| b28d8621-848c-39c7-9479-08b41289f5ea | -20.40912 | -46.29469 | 2025-09-11 01:07:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 36.3 |
| db215882-37a6-37bc-bccf-4b7418d5bec4 | -21.11452 | -48.04118 | 2025-09-11 01:07:00 | TERRA_M-M | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 30.1 |
| e97f1207-92e8-3881-8437-f5aaaa9dfc24 | -19.20194 | -47.98594 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 43.8 |
| aa86440a-d561-3106-88b1-3186fd092b27 | -19.24669 | -48.00141 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f7245de3-86f9-36d6-9c0c-da2e4ba14de6 | -23.34888 | -47.19812 | 2025-09-11 01:07:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 64f9566e-baf9-344e-ab22-b52837d868ad | -19.24053 | -47.99601 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 213.8 |
| c807aa47-1352-383c-afb3-d5eaf40b9286 | -21.10161 | -48.0439 | 2025-09-11 01:07:00 | TERRA_M-M | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 10bf948f-a499-3caf-ab56-03b105617a67 | -20.40335 | -46.26432 | 2025-09-11 01:07:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 2f8ea2a0-ad3a-38ce-8ef2-2ccbad02f051 | -20.3788 | -54.66815 | 2025-09-11 01:07:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 25a4d0a8-25f5-33d8-bb10-715012447056 | -23.58418 | -52.56251 | 2025-09-11 01:07:00 | TERRA_M-M | SÃO TOMÉ | PARANÁ | Brasil | 4126108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| f101fe4a-a7c3-357e-8d5c-a3ed65806621 | -23.33442 | -47.32438 | 2025-09-11 01:07:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.0 |
| 11832a6c-da46-3a39-9a27-4d47a57b46be | -22.58874 | -51.8805 | 2025-09-11 01:07:00 | TERRA_M-M | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| a9939dd3-e381-3135-b23e-a8422b5a4abc | -22.67311 | -53.13235 | 2025-09-11 01:07:00 | TERRA_M-M | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| b249f1c1-3a34-3270-bb4b-9e30188764d8 | -19.98992 | -47.62987 | 2025-09-11 01:07:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 3785e32b-8437-318a-8d93-c7824178e2c0 | -19.19279 | -48.01241 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| cd7030fa-bdd9-37dc-a3a3-a82be8da811b | -20.48762 | -54.91441 | 2025-09-11 01:07:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b18aef10-aa7d-3e10-b852-045539f6cffc | -23.3527 | -47.20401 | 2025-09-11 01:07:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |


[Clique aqui para ver as próximas entradas](README5.md)
