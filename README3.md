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
| 58e9e815-f84b-3b9a-b7a2-b2e4efd3b1b8 | -25.19139 | -49.32703 | 2025-02-09 04:38:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a193118e-2aba-3c1a-a4f0-15de2d064b29 | -21.83271 | -54.84092 | 2025-02-09 04:38:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0131c95b-250f-3dac-80ce-15752c548380 | -19.57235 | -55.23813 | 2025-02-09 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 846734a5-b223-37a6-81f8-36bed7271c5e | -19.73381 | -54.83339 | 2025-02-09 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42379d2e-4723-3a89-b508-12d7a040ffbd | -20.76365 | -46.77088 | 2025-02-09 04:38:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e259611d-7492-319f-b270-0ecced7de5cd | -21.6117 | -48.45804 | 2025-02-09 04:38:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12585d07-40a8-354c-b903-25fc20f8930e | -21.43463 | -43.88178 | 2025-02-09 04:38:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e9dbfb4a-8ec2-3e5a-bdb1-aa194c0070bf | -19.0229 | -57.62165 | 2025-02-09 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 258a1668-184c-357c-9320-d40b58da756d | -20.18146 | -51.18703 | 2025-02-09 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 90f95645-c963-3036-a419-55f2f8f7843c | -24.08097 | -54.21071 | 2025-02-09 04:38:00 | NPP-375D | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de08ed3a-1b15-3af0-a42d-85c6ce91416f | -20.28454 | -49.92545 | 2025-02-09 04:38:00 | NPP-375D | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95de4764-0c25-3567-9da6-dd82460a25b6 | -21.61529 | -48.45863 | 2025-02-09 04:38:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66f8cbbb-5d02-3210-9ff7-b1a0be4fcd16 | -20.28172 | -49.9211 | 2025-02-09 04:38:00 | NPP-375D | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ffd76c1-8f83-32db-ab5f-52253b97d501 | -21.07982 | -56.39514 | 2025-02-09 04:38:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| daed6601-b74a-3d8b-8adf-cc80234f0737 | -6.978 | -42.9977 | 2025-02-09 04:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| ad67df02-a494-37c9-b32e-d271ccb427db | -30.05791 | -52.09917 | 2025-02-09 04:40:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| bc753424-12c9-3bb2-ac91-533d71cd38e0 | -29.7455 | -51.14487 | 2025-02-09 04:40:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 45423af9-a954-3ef4-a710-d5b32fa96a3d | -6.978 | -42.9977 | 2025-02-09 04:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 3f21c615-a3ba-3f52-8053-3167f6091595 | 3.32398 | -60.49513 | 2025-02-09 04:53:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6c1a2ea-f4fc-32cc-b040-0d9be76cea54 | 3.32722 | -60.49458 | 2025-02-09 04:53:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3eebdf3-402f-3cad-b4fe-d4dc5e2d46e0 | 3.32765 | -60.49757 | 2025-02-09 04:53:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53844d94-6b4a-3070-bece-28709a150f3c | 3.32443 | -60.49813 | 2025-02-09 04:53:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aab20a4-d6f9-3981-918d-a99a4b3c3fbe | -6.97848 | -42.99093 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| df17324f-09d8-3d74-94df-cf5e09a03088 | -6.97722 | -42.99258 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6a197ddd-4761-30fd-8d24-7929729f47c0 | -6.97782 | -42.99575 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 85bf5f00-c34c-32d8-b065-28d8a7ceea52 | -6.9766 | -42.99734 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 8fe50010-8c1a-3928-a733-0af1f515447f | -6.98217 | -43.00286 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 068af638-4c2f-3351-a0e5-7ab7e248ff10 | -6.9834 | -42.99342 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ac4a60fd-3f72-3edc-a00d-68be9f2fdb14 | -6.98401 | -42.99654 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 89a81009-4b9b-3c4e-b4c9-f6d0bb349d87 | -6.97718 | -43.0004 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b9f6a56d-65d6-3c2b-b598-8edcb14cb834 | -6.97654 | -43.00505 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 024f42ee-4442-3d02-847d-040e3aa1d7be | -6.98278 | -42.9982 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8eb42310-baac-351f-a06d-422ae5f69d0d | -6.98336 | -43.00122 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c86bb2c7-b1c4-3fc4-a923-e361230f5a6e | -6.97599 | -43.00202 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 63476ace-0cb5-38ce-87e6-546461c32710 | -6.98467 | -42.9917 | 2025-02-09 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c333a47a-bcb5-3148-b13a-d4a70cd618d1 | -12.34842 | -52.4901 | 2025-02-09 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d314f1a1-775d-38a0-a3a6-5d67158e83c4 | -12.34903 | -52.4859 | 2025-02-09 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e3116eb-db41-3c95-bde3-0d20d5f235ef | -13.62121 | -55.45409 | 2025-02-09 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a8c71fc-0997-355e-9c47-154516fa1323 | -13.62507 | -55.45108 | 2025-02-09 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 350c4c7b-e83d-38aa-b9a8-e936c0076bd3 | -12.35262 | -52.48645 | 2025-02-09 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 591871f5-d7b7-3a04-8c53-dc0a9250259f | -13.61734 | -55.45709 | 2025-02-09 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b5e51eb-1466-3436-9312-2e911e51647f | -12.35202 | -52.49064 | 2025-02-09 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22c9cb7b-50b6-3bbf-85f2-f0c514c5d499 | -15.46811 | -51.94953 | 2025-02-09 04:57:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ebbea00-2135-3902-bf70-2ef187445196 | -12.34483 | -52.48956 | 2025-02-09 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87bbb815-49c7-35a0-ae58-684f5dddd3cd | -13.61789 | -55.45355 | 2025-02-09 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3812887-437e-317b-8528-9774c15898d8 | -13.62839 | -55.45162 | 2025-02-09 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f0804f2-059d-3bc5-b3ec-2470e134c88e | -12.34543 | -52.48537 | 2025-02-09 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 951509da-743a-32db-a549-b81c052b158c | -12.21106 | -50.92869 | 2025-02-09 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a3d3101-f215-30ec-9a67-dcae7fb29657 | -12.21177 | -50.92364 | 2025-02-09 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c43449b7-b959-3a3e-85af-a74e44ecbc01 | -13.62468 | -54.87972 | 2025-02-09 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9d5b656-1889-3290-97d8-c77fc9e514de | -19.73273 | -54.83444 | 2025-02-09 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cd89e4c-af7c-35c0-b0b0-d283421a82d4 | -22.5372 | -48.8122 | 2025-02-09 04:59:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5a69be7-0409-347a-bd4f-850542f1589e | -21.08048 | -56.39245 | 2025-02-09 04:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0a66a97-b10c-3146-92dd-e08b48ffc116 | -19.57343 | -55.237 | 2025-02-09 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47e08588-a4b8-3df0-bd40-c04b7516aa57 | -21.07712 | -56.39188 | 2025-02-09 04:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dc38ddb-8768-3252-a663-bea8dd977e99 | -21.61176 | -48.46065 | 2025-02-09 04:59:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 791b8c14-84dd-3dc6-84b6-f401938ec212 | -21.61698 | -48.46139 | 2025-02-09 04:59:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9fb21d3-f69e-3fc7-8e67-9f4141d11a1d | -20.28101 | -49.922 | 2025-02-09 04:59:00 | NOAA-20 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b26d73-85a3-3349-b0a0-d6791abb9c9e | -20.28512 | -49.92756 | 2025-02-09 04:59:00 | NOAA-20 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e48625e-4aae-34a4-95cf-9554091b2dd9 | -21.83346 | -54.84352 | 2025-02-09 04:59:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ff3695c-63c8-3928-8c3f-1384e5f415a5 | -18.59873 | -53.15912 | 2025-02-09 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ea62458-001e-37af-a414-11c048281ffb | -19.7333 | -54.83038 | 2025-02-09 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b23ad30-723a-3a59-b7c4-61d71239f5a8 | -21.89509 | -53.71952 | 2025-02-09 04:59:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 891c0f2d-85cc-3257-b3d9-2a904e05d7ad | -21.89486 | -53.72148 | 2025-02-09 04:59:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8a6a05a-df81-3ad7-8409-eb1a9076b562 | -20.2857 | -49.92253 | 2025-02-09 04:59:00 | NOAA-20 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac7c0192-ac0a-38a0-b93b-92da4fd6da3f | -24.08213 | -54.21416 | 2025-02-09 05:01:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b31f08e7-4c44-3b5e-8bac-ac2f6d40230f | -6.978 | -42.9977 | 2025-02-09 05:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 9554c7dc-fb0a-345b-b047-43f2229f437d | -6.978 | -42.9977 | 2025-02-09 05:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| e6f49f90-e3e5-3c9e-813c-161ca3f6c2c5 | -6.978 | -42.9977 | 2025-02-09 05:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| bb4a6d27-6074-3b2c-a155-00acc45926b0 | -6.978 | -42.9977 | 2025-02-09 05:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| f12c554e-67c8-35e2-8612-895f33ce3953 | -6.97976 | -42.98653 | 2025-02-09 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| e35d3f16-92f3-3592-9b63-42aef3ab077f | -6.9773 | -43.00461 | 2025-02-09 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 115ec8a1-ff3a-3885-95d6-5f6f654a3eed | -12.34618 | -52.48338 | 2025-02-09 05:44:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 58ffc8bb-bc86-341f-86d2-b81e095b9f34 | -13.62746 | -55.45242 | 2025-02-09 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1349edbc-0fb8-321f-a4f9-e531a5a1e56c | -13.61758 | -55.45539 | 2025-02-09 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10d3d880-8c24-33ae-9bb5-3ad8ec4ec603 | -13.62012 | -55.45757 | 2025-02-09 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1402b1d5-29b9-3757-8936-3f562ea415df | -13.62071 | -55.45173 | 2025-02-09 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7955b87f-5d0e-3dac-98e5-26dd18bd81a4 | 3.69128 | -60.33405 | 2025-02-09 06:12:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a3d4515-cc62-39e8-8f49-031fb67c683b | 3.69055 | -60.32972 | 2025-02-09 06:12:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cef043f-7ba4-3947-896b-03c13960e252 | -9.19923 | -35.70002 | 2025-02-09 11:51:00 | TERRA_M-M | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e2e83a23-055d-3632-abf9-1bfa6928f0ea | -10.50976 | -38.41842 | 2025-02-09 11:51:00 | TERRA_M-M | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |


