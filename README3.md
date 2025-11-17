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
| 1ff3f457-cf19-391b-9262-801defa3fdc5 | -3.5951 | -50.709301 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74e14070-2a55-31b0-89f0-82b642b14a3f | -4.6483 | -50.409801 | 2025-11-17 00:31:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f486db3-df28-3f96-a76f-ff09d7fd0268 | -2.9411 | -51.757999 | 2025-11-17 00:31:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25cc7134-34ff-3d54-a705-4a2d48ef0f96 | -2.683 | -52.069302 | 2025-11-17 00:31:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a793f0c-9889-3942-9dd1-5cde7869a50a | -4.9311 | -44.539398 | 2025-11-17 00:31:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee1b733f-ab9d-3a44-9ed8-b63d61e5d584 | -4.1564 | -50.199902 | 2025-11-17 00:31:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be162d05-9677-3218-94fb-f8f853312038 | -14.996 | -43.357399 | 2025-11-17 00:31:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 291e35e7-8e7d-3cc4-a48f-a8fc8368f175 | -3.0078 | -51.332001 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c54c7d18-5d36-3ebd-85a6-7ae008f0dc9b | -10.8719 | -44.628502 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4374e1f6-7e99-3192-8aa5-86e0ffce7adc | -10.6661 | -49.375599 | 2025-11-17 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb49410-589c-3c8f-8226-201965968527 | -3.1449 | -50.188499 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f2c3ee-d6cb-332b-a8a4-883316881a46 | -3.4255 | -52.925999 | 2025-11-17 00:31:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8daff6c7-3ca7-3594-a34b-6d12692be3fc | -7.9752 | -50.000198 | 2025-11-17 00:31:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608abf2b-2c57-389f-a92e-a342aaa44e8a | -4.0159 | -48.807999 | 2025-11-17 00:31:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e14936f3-9d17-389b-8d12-c4de4df8c7ae | -1.7709 | -56.164398 | 2025-11-17 00:31:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8071e1-dfc8-3c01-bc83-e575f38d5bfa | -11.6976 | -48.848999 | 2025-11-17 00:31:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0691b0c-4956-3752-877a-1e9d0ceeed25 | -3.2258 | -50.493301 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9f15e60-9b17-34fd-aea7-8342f182717f | -10.6619 | -49.358002 | 2025-11-17 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce1b9ae-5f9d-306d-9452-5afa760b829d | -3.7649 | -47.744301 | 2025-11-17 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc2ea5dd-ce26-33e6-b459-9c8f2a8ffec3 | -3.1876 | -50.639198 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b524eb3-3fdf-346a-953f-f1d01b49d3a5 | -9.3175 | -46.574299 | 2025-11-17 00:31:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 569f8e22-8ffa-389f-9f1a-2f724fd44882 | -3.5206 | -51.233101 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81384b8b-d35b-34ab-a094-24ca70bcc972 | -11.6998 | -48.858101 | 2025-11-17 00:31:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84d56f81-6ae9-3295-96c6-fe300d3a9204 | -2.6683 | -51.870899 | 2025-11-17 00:31:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1455a3c6-e2ec-3708-ba79-1f4b46993bb8 | -3.7711 | -50.1371 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edad5005-7b26-37d0-93c2-8dcfa3034ae7 | -3.4709 | -49.688 | 2025-11-17 00:31:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c86275e-5140-3678-b9be-b22752aaf9c6 | -3.4576 | -50.116699 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 632c4171-2b97-3657-9584-efb881400002 | -9.7205 | -43.953899 | 2025-11-17 00:31:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 05b68729-9efc-34b4-8894-184239e7e2d5 | -3.3379 | -43.491798 | 2025-11-17 00:31:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e025aa5-aebd-3b70-a64f-40d0e9fae589 | -5.8335 | -48.833302 | 2025-11-17 00:31:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f578cca9-23ba-31b8-9432-268df922ac37 | -9.63 | -47.895802 | 2025-11-17 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31fca397-9052-3c25-95ac-8d73a1cb2cd3 | -5.1288 | -56.034199 | 2025-11-17 00:31:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9271e4-647b-39b5-b1b6-ee3c28cc2cc6 | -3.6478 | -50.226501 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aacba99-29a3-375b-88bd-117a0938d196 | -3.0098 | -51.340599 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be1d3513-d344-394a-91cb-3fb3fb1d5978 | -2.6702 | -51.879002 | 2025-11-17 00:31:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 314b02e4-e6d1-3140-856f-c14ac9463125 | -11.7096 | -48.855701 | 2025-11-17 00:31:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94955b4a-4f03-3c96-becd-ea054996f3ab | -2.9945 | -51.006401 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ddc6e6c-9fab-33d7-b6e1-d13141523cf2 | -11.2014 | -49.412102 | 2025-11-17 00:31:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b7afe1b-3f09-3be2-983a-7d706e0d2c94 | -4.1587 | -50.2094 | 2025-11-17 00:31:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bce9f5eb-08af-34e2-a4d8-7f6e373bfb05 | -8.8634 | -50.179199 | 2025-11-17 00:31:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2229b9b8-8864-3b60-b534-b316800f38dd | -10.664 | -49.366798 | 2025-11-17 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82e4a56d-ed24-3b94-b060-089489c9ec4b | -11.8185 | -47.5942 | 2025-11-17 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59958103-3ce7-342b-ba14-56718d18afaf | -10.9463 | -48.688099 | 2025-11-17 00:31:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3b5633d-f0a8-3f41-94af-b588ffcb8759 | -6.6566 | -42.044701 | 2025-11-17 00:31:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d369da08-d044-3107-b744-7a438984fafa | -5.8205 | -48.995899 | 2025-11-17 00:31:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08e8f0a1-3085-342e-83f9-18edde8a9ade | -2.8787 | -53.9622 | 2025-11-17 00:31:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dc7582b-3631-3477-b15f-d398e3a7ce74 | -4.9437 | -48.250099 | 2025-11-17 00:31:00 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa52f3b3-3e26-3222-8157-0a0b119b86ac | -11.1994 | -49.4034 | 2025-11-17 00:31:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e38ab76f-fa43-3f2b-824a-55d447687add | -10.8675 | -44.611099 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 88d20d5e-ec5b-3b4a-8d09-f5afec4ad7ac | -10.6522 | -49.360298 | 2025-11-17 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b5d424b-bba8-3310-91bb-3edffe5c2736 | -9.7993 | -48.555302 | 2025-11-17 00:31:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29febfcd-773f-3bbd-a3f5-da3bd9bbf82b | -10.9486 | -48.697601 | 2025-11-17 00:31:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 858f4b03-e6f6-3906-8e88-02055eda1582 | -3.3908 | -50.183601 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1311bfb3-5bca-3b00-97c4-251bc483f1a0 | -3.7613 | -47.6422 | 2025-11-17 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 843cf4a4-84e3-3693-9bfa-42e280d2b880 | -11.0457 | -45.149502 | 2025-11-17 00:31:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3e20521-6490-3596-b789-f75e2f9407a7 | -3.8396 | -55.7938 | 2025-11-17 00:31:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9f3ff2-2dba-3c8e-a228-8f321b47cfdf | -4.9408 | -48.237801 | 2025-11-17 00:31:00 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca6fa63-46fa-3692-8f1f-9ea977311a01 | -4.8792 | -44.870899 | 2025-11-17 00:31:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a478ec5-d81b-336c-b194-4357f1d47409 | -10.9559 | -44.5131 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc99004c-7d58-38f4-83a5-195acafd044d | -3.8995 | -54.145802 | 2025-11-17 00:31:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19e4d69b-25f7-385d-9820-d545aa639acc | -2.5185 | -47.812401 | 2025-11-17 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe07d05-af80-3a1b-8007-a5e4bc089bc9 | -4.7195 | -46.367298 | 2025-11-17 00:31:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fdbc99b-644f-34ef-9343-111e88417d26 | -2.2442 | -53.620098 | 2025-11-17 00:31:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 807ef6ff-e38e-309f-aa40-30c6dc0c2dd3 | -2.5054 | -47.800201 | 2025-11-17 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30ebfa45-a785-38f8-8aed-e35deefe5587 | -1.3863 | -53.8344 | 2025-11-17 00:31:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73ddda1-bfae-351f-8084-231b7eed722c | -4.9683 | -49.663101 | 2025-11-17 00:31:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a807e85-296f-39a3-a50e-14ca8b0ca451 | -3.3054 | -53.844799 | 2025-11-17 00:31:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bad071c-dac0-3b07-bd53-a9455a66f2a7 | -3.1778 | -50.641399 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a7ddbf-c648-3035-b0d9-50096913fa5e | -4.0879 | -48.023499 | 2025-11-17 00:31:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01c51a7d-123e-3702-8ca2-78a0bee7a8d5 | -1.5293 | -55.507099 | 2025-11-17 00:31:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1645719d-fb11-3ae1-9e94-f3c50530fcc0 | -10.6543 | -49.369099 | 2025-11-17 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7d760d2-7e25-3d6a-af9a-86536a77cf38 | -2.2426 | -53.612999 | 2025-11-17 00:31:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0678da07-a8e1-3eae-8e0a-05a077c47de0 | -3.2378 | -50.500401 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 985f02f2-e7b2-3302-b673-ede41b97dd4e | -2.6794 | -52.053398 | 2025-11-17 00:31:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 705e5575-48cc-323b-82ab-077ee2dfd8be | -3.5296 | -49.102501 | 2025-11-17 00:31:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e297f9e-3de0-36ea-9056-8b06c5538447 | -4.7576 | -44.416199 | 2025-11-17 00:31:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d9f8d8a-377a-3822-965e-6a13d2c54cf0 | -7.9732 | -49.991402 | 2025-11-17 00:31:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c7ea01-d05a-3bc8-8654-7cd73afa97e4 | -3.8473 | -51.309299 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a0f175-d863-3600-9424-499ed903e3d2 | -4.1662 | -50.197601 | 2025-11-17 00:31:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fad9e44-9428-33f5-aeaa-107e9fb36dfa | -6.6801 | -47.378601 | 2025-11-17 00:31:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db1fe438-aaa5-33ca-9f98-4e2931ad15c7 | -2.8867 | -53.2743 | 2025-11-17 00:31:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd9a26d-e3fd-3dd9-bc26-7342098df537 | -2.4649 | -50.2295 | 2025-11-17 00:31:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 215fd824-be8d-3a74-9445-7b1658ab2e1b | -20.323601 | -57.758301 | 2025-11-17 00:31:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a037d951-8c4f-3d9d-8dcb-778767b42783 | -3.2236 | -50.483898 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e41d5a00-fd8b-39ea-814a-d6042a55ce55 | -6.2133 | -47.2351 | 2025-11-17 00:31:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3716f6c-4b28-35ed-8ba0-fc5549c6cf1a | -4.7678 | -48.4198 | 2025-11-17 00:31:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5105a598-5dea-3260-b37c-d37fa589fb26 | -3.4064 | -50.118198 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 678d1996-a962-32d1-88c9-a2ba5a22ddcb | -6.6583 | -42.011501 | 2025-11-17 00:31:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fd1b0ba4-9302-3761-b6a9-398cdac9c796 | -2.8883 | -53.281399 | 2025-11-17 00:31:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4e3d19-95af-3796-9858-6bbd21489563 | -16.2428 | -46.946499 | 2025-11-17 00:31:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ae7b9235-213b-3cbf-b540-2a4580d0922b | -1.6905 | -53.6772 | 2025-11-17 00:31:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fbb4641-32a5-3b9e-bae2-17f5a936035c | -4.9892 | -44.359402 | 2025-11-17 00:31:00 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2828b564-fd4a-3b46-bdda-cb6e68526a36 | -3.4006 | -50.181301 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd9f38c0-c748-35f2-9c46-f2f846b76e72 | -4.3923 | -45.818298 | 2025-11-17 00:31:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12649a04-94b2-3421-ac2f-1e0fe5696694 | -15.4607 | -44.181301 | 2025-11-17 00:31:00 | METOP-B | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d303f940-5517-311c-be56-f1a4505e04af | -4.9257 | -44.5173 | 2025-11-17 00:31:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0d7bc23-4933-3003-8e9c-7dfd21b338cd | -12.2019 | -49.625 | 2025-11-17 00:31:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7556e8c3-6790-35ed-a308-41869a595af0 | -11.8133 | -47.572601 | 2025-11-17 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 079e3069-7b61-3979-85fd-8162413f013e | -8.3143 | -45.395302 | 2025-11-17 00:31:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 865f361d-7dc6-3d16-afa7-413d479e916f | -3.7964 | -51.089298 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
