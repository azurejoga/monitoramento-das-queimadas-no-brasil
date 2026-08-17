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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 872207d3-13a6-3022-a153-f4f7cdcc1cf0 | -11.2813 | -45.81313 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f85dbaa4-8f5e-3c3b-ab9f-e2e52765c513 | -7.46127 | -59.99879 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3bd5b672-b235-3cd9-a4cc-585f3ab7966a | -14.48801 | -53.09084 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b60bb9b7-7e99-3a1d-bab2-d6aaacff733e | -6.98087 | -59.0271 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3de8f189-33c2-3696-a01c-10c2ad0f6fb1 | -10.46963 | -46.30991 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8771a1c6-2621-3211-a6ee-1fbce91fc674 | -14.39989 | -51.87293 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c82036bf-61e1-3a0d-aedb-7172e6e450bc | -11.31516 | -46.25173 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aea4011-2147-3a1e-bd96-9c1871de715a | -8.97055 | -60.52541 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b98f706-5fc5-3ed7-af14-707f3bbb2f4a | -14.44975 | -51.83986 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f16863dd-5e4a-3630-8250-ca3799af4ca1 | -8.90479 | -60.5915 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb135860-5e0f-3bbb-871d-60e4f71fd0be | -14.37648 | -53.15265 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa2f7d83-162e-3d49-8a5d-912ee8019a94 | -6.82147 | -56.44346 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21692ba9-1030-3799-80b9-2c01cb1e6ec6 | -10.38174 | -48.27085 | 2026-08-17 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a605410b-36b4-3cee-b7d6-b7ad54b7b8de | -14.87242 | -46.65973 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1576947-b53d-3b62-914d-4747ee619ffd | -7.87953 | -63.75211 | 2026-08-17 04:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba1d85a4-a568-36eb-8c7d-d7dce47d1d5a | -7.36485 | -55.49352 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53288850-e6d2-303c-bb64-a4057ef64e09 | -14.18728 | -53.06634 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ec935ad-87b5-3fe3-9041-9ec444274419 | -10.37173 | -53.86469 | 2026-08-17 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81810b80-8f4e-3b85-bcf0-346361f4af50 | -8.51645 | -54.90475 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5516edc-44c8-332d-aa02-f39d92b4db78 | -7.42044 | -60.01974 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9b0acfa-688b-39a6-8c0d-7061b5fe79e5 | -11.71369 | -54.60625 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6456c435-bff3-308b-b55f-4ee32fb368af | -9.47194 | -60.50052 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45b4893a-8ad9-301f-b6d1-c2d37046dc14 | -12.23698 | -47.03207 | 2026-08-17 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 362d65c2-70e6-385a-9c80-48780d950268 | -7.36564 | -55.48879 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fb1b4f5-a0ff-3e4d-b9a9-bf2a1ed9d2d7 | -8.51057 | -54.8953 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00a804bf-6c91-3069-a54a-cb9982f7e628 | -8.64249 | -54.6883 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e426827a-b71d-30b2-b8fa-513d25c75919 | -9.57343 | -47.09721 | 2026-08-17 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0105d29-41d2-3f09-9cd1-f4da3221c6c7 | -8.63762 | -54.71719 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17506ea3-61cd-300f-a43a-00b8345d6dfe | -11.23062 | -54.02054 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94d01a79-52ea-315a-a82f-fb08544c0a06 | -7.53845 | -55.58514 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b663efb-8133-3395-8855-deafb2bda4aa | -11.72344 | -54.61191 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d30b504b-7edb-3ee4-9b3c-43567b358ef8 | -10.07347 | -60.50369 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bdacd29-2324-32e6-bf8c-c902502d7608 | -7.54842 | -61.18285 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f704f191-641f-3e78-b633-7fc9371a312f | -14.49321 | -45.68044 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 020515d2-2c56-37ba-b898-722bcb5115c9 | -8.89774 | -60.59983 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69a87e6b-9312-34bb-bbf9-fdd6ce63e78e | -15.12352 | -48.17662 | 2026-08-17 04:57:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 443a93aa-0eec-3ba1-8d37-348d56b0636b | -9.17299 | -59.67443 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5a07ac2-93a6-31d4-9d52-cd0505f137ed | -7.88776 | -61.80178 | 2026-08-17 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a392d3e-f7f5-321b-8899-8d052bff081e | -6.62468 | -59.0706 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca00f034-1a9a-3d8d-97c0-17bc4a084eca | -11.72062 | -54.60745 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262fbaa7-29de-3708-9ec7-4c890edf0672 | -13.75601 | -53.43361 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0d6db60-62b3-3714-a2e8-5e42bd2eaf9b | -11.71305 | -54.61011 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb80904-0c23-3972-ae7a-f159001f1c30 | -12.65384 | -48.49496 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b8f431c-3dcc-3413-a034-34501d76fa94 | -10.46975 | -46.30458 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e80e52e9-fef1-3a10-8296-07789eb6dfc5 | -9.48766 | -51.67386 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9430a9e6-cfb8-36e9-a941-817998c1947f | -9.99415 | -53.94921 | 2026-08-17 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 876c3d8a-0d0a-30cd-9d6b-bf4c9faead23 | -7.50112 | -60.07978 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d1751c95-4501-39ba-89ee-1786eb4ee133 | -11.73486 | -54.58615 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f16de9e0-37b7-30e8-9553-5b48195b4df6 | -8.9042 | -60.56534 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56397c0f-b1c3-3594-9e8c-8967be0baaae | -13.75716 | -53.42645 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1bd560d-087c-3078-a574-0a4e714a5d36 | -8.64052 | -54.72193 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a997d0fe-f760-32f4-aba0-5f7b85dab526 | -11.71651 | -54.61071 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 283c808f-77c0-30f6-abaa-9114a29c41d5 | -7.39388 | -55.48385 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 409afc80-3f49-3958-9cb2-515011c82549 | -9.30376 | -49.10126 | 2026-08-17 04:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5abd2588-bc5e-394e-a396-b28669ddfd1d | -14.47379 | -45.68295 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53aa49e7-ee1b-378f-9fd8-bb8ec7608beb | -12.70826 | -48.52216 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9892ff16-8e36-3156-9147-46e284a7f481 | -6.64855 | -58.96326 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27688203-95e1-3c04-9af8-d099e22462d0 | -13.51614 | -46.25799 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9dbe040-273c-381c-b655-2e3e71f45ea7 | -11.22039 | -54.01876 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e4ee517-2306-3aee-84a1-ce8138d81d27 | -6.7822 | -59.45722 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdc6b253-2c23-37ab-bb0d-345de7d48be5 | -6.8306 | -56.46348 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f9de34-775d-3c30-b312-7512cafe5b7f | -6.60984 | -58.97032 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 10572526-efad-3709-bb37-3d9cc9f9c6f0 | -6.96786 | -59.30507 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1f78b01-f4d6-30a1-95db-a76c5c16aca2 | -7.40611 | -60.01101 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bc36661-2c7a-3555-85c1-e032563850b9 | -6.83761 | -58.97236 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ccb80430-cee1-3aab-b809-c87be56fc9bd | -14.32474 | -53.04906 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d372b628-b131-3466-b592-f3aa9ad04f9d | -9.25268 | -60.33417 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 027151f8-5bdf-305f-9d01-327a39b60eb5 | -11.79531 | -51.77988 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e31a400a-fa93-3e19-9425-0b8374c99548 | -13.51172 | -46.25719 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f2303ec-a467-39bb-a463-5617a16059ed | -8.90005 | -60.55803 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff9f9cb6-8520-3952-9a4e-b272e4844b2f | -11.72883 | -54.60098 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef9ea83d-8e05-3ba6-aabf-976028572c23 | -6.62437 | -58.95875 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9601e787-4541-3c47-9c55-8ef9698b1f93 | -13.46809 | -51.80365 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddb2fc82-0c4b-3589-9762-781edc7c86d5 | -6.83247 | -56.45264 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bf0f3f3-4ac9-3eca-875a-49211ffcdbf5 | -7.37472 | -55.50481 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1c673d6-1d56-34da-9852-1c0bfa3ee7bb | -9.20218 | -60.78995 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7cccd3f-26ba-327f-95be-b665c322a38c | -8.89901 | -60.56438 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42ec0ac0-ecbe-3d9f-8c88-0a715973d97e | -6.89096 | -59.00945 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1e852e0-9cf2-3443-a507-5fcaeae94024 | -6.77483 | -59.76723 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a14b40f1-be13-3ea8-9b6e-a013c7d7226e | -12.06157 | -58.03896 | 2026-08-17 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d54f19d-7d03-3bd0-a9dc-a7ffb3226b4b | -11.10189 | -47.29056 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28cdb3a0-1c8b-368a-8b98-c040f476a122 | -7.54909 | -61.17915 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce94a591-bb1e-3706-a363-7f37747bf71a | -14.47601 | -51.98234 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53b0d685-e7e6-3d5d-8fa9-7a7cb7572334 | -8.95618 | -60.51628 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f5e9e46-907c-3231-bb77-505eae70e654 | -8.02214 | -55.15207 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 934f642b-ffb7-3577-ba07-2980ddbcd14c | -6.70255 | -58.93961 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e14eb9ce-8f50-3b10-a684-2ec027aca1d9 | -14.46865 | -52.07416 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2375361b-b7ec-332c-9e0c-855d7c405f65 | -6.71881 | -58.93188 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc7d3562-1a56-3ce0-8966-928e2dcf7275 | -7.78281 | -48.27986 | 2026-08-17 04:57:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bafbffbc-8bad-3cf3-ac03-46c35c30267e | -12.02408 | -46.43111 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0f6b74fb-a9d1-34de-a5f3-4a8a7acf6dee | -6.8218 | -56.44794 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdcf1ed5-5f53-324a-9982-60c90869dac5 | -14.48448 | -45.67413 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e5dbc824-b1a5-3e28-b2fe-ac45336f8c2e | -7.40554 | -60.01415 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65d55b9b-98b0-3d96-a573-1e4dfa573763 | -9.30631 | -56.81039 | 2026-08-17 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8fb4385-c50c-389a-817b-5d95a5ab6b4d | -8.52517 | -54.91961 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f2f371a0-3918-3373-936c-9ae2181e373c | -8.89716 | -60.60293 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0eca51a6-62fd-3cf0-8e69-1842e988e977 | -11.69918 | -54.60777 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a7b5c3-afbe-314f-aecc-30308b92dbcb | -6.64952 | -58.95774 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 467b298d-d120-375f-86d4-de14c40d36d0 | -8.62972 | -54.72019 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 518330b6-2d3d-33ae-83a3-334f78079f89 | -9.47705 | -60.5015 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
