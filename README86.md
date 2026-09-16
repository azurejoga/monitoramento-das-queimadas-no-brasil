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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6126e32f-c313-3b5a-bb6b-8518033551af | -9.8032 | -59.7964 | 2026-09-16 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e7a3e488-1db9-3096-8194-9bbbe4773368 | -13.3199 | -51.62 | 2026-09-16 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 79f790cf-2cf8-36e8-b5a0-870f08535005 | -9.7979 | -60.4734 | 2026-09-16 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 6e00c685-bb56-35ff-b12d-fcbabf7afbc5 | -9.1708 | -59.6568 | 2026-09-16 16:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 62e9483e-a479-38e7-a4ff-70452b13d0c7 | -10.331 | -45.2883 | 2026-09-16 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| a0fe2aaa-f9ef-3065-82a8-d20a2c6b10d8 | -8.5497 | -64.0477 | 2026-09-16 16:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| d7543e05-a8e1-3400-9563-d57d3151cc47 | -6.3381 | -59.9949 | 2026-09-16 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| fcd846c8-5797-3c86-8064-8b748ca31daf | -8.0748 | -54.8499 | 2026-09-16 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| caf2c4a6-0d3e-3296-a67e-ecc03d518ff5 | -9.7358 | -47.0958 | 2026-09-16 16:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 84ed8c79-5c47-356e-b3fb-2b427ba78331 | -9.1725 | -59.4241 | 2026-09-16 16:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0c26d39f-ee75-3671-8c7d-b820f062300e | -12.1265 | -44.199 | 2026-09-16 16:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 6c9508c2-0287-3b53-a584-337d9151b2b1 | -8.396 | -47.2121 | 2026-09-16 16:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 5f4c0886-1bfa-3ea7-9b72-23e9923c3ca8 | -8.8456 | -45.8939 | 2026-09-16 16:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 189.2 |
| d8689289-710b-3878-a9a2-9d5a5d4acc0e | -8.6493 | -66.5839 | 2026-09-16 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5ef28d89-07d2-3deb-ace6-81a7a0ddf40c | -9.6205 | -61.8259 | 2026-09-16 16:00:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0880834c-8d70-3ca4-ab66-279a119e6522 | -3.4279 | -57.9816 | 2026-09-16 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 5171c84b-b51d-38a6-8327-02fa5ad4bab1 | -9.1337 | -65.844 | 2026-09-16 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 239.4 |
| 9b078607-5c19-3da4-aa87-7825eee19677 | -2.6602 | -57.5119 | 2026-09-16 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0b8ed84c-5201-3624-93b0-53581d61aac5 | -6.338 | -60.0141 | 2026-09-16 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 812e7535-3542-3230-b741-6d06a27ab5fa | -9.1337 | -65.8253 | 2026-09-16 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 62ade1e0-7ace-3478-a56e-43cf49a7f1e3 | -6.3198 | -59.9572 | 2026-09-16 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e51550dc-53ad-3156-8cfa-530a3db4acd9 | 2.2186 | -50.9393 | 2026-09-16 16:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ca400a23-1d61-371b-99f1-279ff534d4fd | -11.2693 | -54.0129 | 2026-09-16 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 847db2e6-47af-3696-a84b-c93028a70f36 | -6.3013 | -59.9771 | 2026-09-16 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 162056bf-a082-349b-9cd5-3f2288104494 | -9.3702 | -58.0079 | 2026-09-16 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| e7bacd9c-d38f-3168-902f-76dacd1d16aa | -6.4484 | -60.0101 | 2026-09-16 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 01436047-334b-3149-97b4-3a69004a415d | -8.9239 | -63.3371 | 2026-09-16 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4d047a59-47d2-366e-9036-dabcbd67aef0 | -6.2731 | -55.2904 | 2026-09-16 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2b2107dc-5c25-3a70-90d2-4d9580896e88 | -3.4278 | -58.0009 | 2026-09-16 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 59e9f6e2-8c67-3c1d-b76e-4bcda004de98 | -11.2113 | -54.1208 | 2026-09-16 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d5535b85-b590-3b51-90b6-dc3bf306262c | -6.3197 | -59.9764 | 2026-09-16 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 221a1446-af3e-377c-ada9-dcc261e8fc05 | 0.1931 | -51.3565 | 2026-09-16 16:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9cba02f6-8507-3f8e-9fbc-678a7c3d8a80 | -8.6311 | -66.5287 | 2026-09-16 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 138b0160-af25-3405-8e22-98784cae59dc | -8.5428 | -44.5132 | 2026-09-16 16:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 463.2 |
| e6a71634-c805-3ec0-95b6-13c4c201a10a | -9.006 | -65.4 | 2026-09-16 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e586b1d9-1b3e-376b-91c3-2fcfff0dad52 | -9.7793 | -60.4744 | 2026-09-16 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 9f03dd01-3abd-3aa4-a58c-772a52cad729 | 4.15 | -61.1996 | 2026-09-16 16:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b778c961-65a0-36ef-ab72-b29a2e10b54f | -13.3391 | -51.6176 | 2026-09-16 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 09a62593-0b36-38d2-b455-64a96a5204b9 | -9.7909 | -45.8782 | 2026-09-16 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 7b36c228-2669-372e-a72b-609a7582ef2a | 0.1747 | -51.4805 | 2026-09-16 16:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| fab28c74-96c9-34e3-b200-c14b6c3d438d | -13.414 | -57.0225 | 2026-09-16 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| d250364a-a2ee-3c71-bd31-dc896477f26d | -8.6188 | -44.4819 | 2026-09-16 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 249.1 |
| 4bac2d95-1fc8-32ea-a560-409bbb6d9d86 | -9.7979 | -60.4734 | 2026-09-16 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 88e67466-f218-345b-b746-1b5c847c36d9 | -8.5989 | -44.5531 | 2026-09-16 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 412.3 |
| 005a0115-dbe6-3f4f-8806-04f1b91df0d7 | -9.5725 | -46.601 | 2026-09-16 16:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| f0da5afa-8856-333d-aa4c-4d8496edaea4 | -8.6493 | -66.5839 | 2026-09-16 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| cb339a09-6a9d-3e98-a884-73dd8a55935f | -9.1725 | -59.4241 | 2026-09-16 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a567fd06-9c9a-35c2-9532-b139efe7c694 | -8.6311 | -66.5101 | 2026-09-16 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b0b5ee06-20c4-3ca8-8de8-ea62d662424e | -9.4423 | -47.8568 | 2026-09-16 16:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 979d2291-f726-3deb-9ba6-00891f3c5bc5 | -7.7993 | -66.9018 | 2026-09-16 16:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 11582b88-bb58-37fe-910f-0b2e9427d6a2 | -9.3572 | -50.137 | 2026-09-16 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| efac4d73-cebb-3bf1-953b-2e0b9d52db06 | -3.4278 | -58.0009 | 2026-09-16 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 5a3078e0-d686-3e8d-bb7c-bd4c38c54a91 | -10.8114 | -46.182 | 2026-09-16 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| f4d0ef5d-4a33-39fb-8e74-dac846968152 | -9.4623 | -60.5104 | 2026-09-16 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 450958c9-1875-3d0d-9709-34bf442e7109 | 2.2187 | -50.8977 | 2026-09-16 16:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6062323f-4e6f-3cfa-95f8-f70b12ea12aa | -11.4905 | -50.2581 | 2026-09-16 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ab647e00-e7f3-3bd2-8965-a239c2683fbc | -9.1151 | -65.8446 | 2026-09-16 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| dfd29c11-5db7-33a4-9f69-e03a6019334f | -9.3575 | -50.1156 | 2026-09-16 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| bae1f85d-4568-3c7e-a925-248901a883fc | -8.6309 | -66.5658 | 2026-09-16 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2d71decd-65c3-3b6a-9967-94de01ce5301 | -13.3949 | -57.0242 | 2026-09-16 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 3e65a0f4-f233-3c5a-a69f-1ec7d6260894 | -8.6181 | -44.528 | 2026-09-16 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 53c6cfbf-8a72-3d3c-8036-70312269e08f | -8.5428 | -44.5132 | 2026-09-16 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 369.2 |
| 84763cd9-8e38-378a-8d5a-23a516686b2b | -8.6184 | -44.5049 | 2026-09-16 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 291.5 |
| 16c7ea75-6202-39cb-af59-0f453f2f07b2 | -14.2558 | -53.131 | 2026-09-16 16:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 12ddbffa-caaf-36c4-b8a4-4b865134a59b | -9.1337 | -65.8253 | 2026-09-16 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8ce6109b-dd7a-3501-9824-36866b74756f | -9.3954 | -50.0908 | 2026-09-16 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 22b773ae-5587-3787-8449-f026a94b7423 | -1.2268 | -49.1899 | 2026-09-16 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f05a785e-1094-32e6-a5c3-64b7c8fff264 | -8.5497 | -64.0477 | 2026-09-16 16:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| c1209225-c919-313a-b93d-7613bc6784d9 | -12.1265 | -44.199 | 2026-09-16 16:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 73f8323a-31a1-35f0-b2a5-faf6cdf39594 | -10.331 | -45.2883 | 2026-09-16 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 69ddf003-3fa8-3810-be80-faa93eff1ff0 | -3.4279 | -57.9816 | 2026-09-16 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0bcb809b-45cc-304e-ae74-f9ed475dabc4 | -10.7729 | -46.2096 | 2026-09-16 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 245a612c-a711-3113-bcf0-26380b00030d | -8.9239 | -63.3371 | 2026-09-16 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2ba64491-4551-32a7-9efb-90a212136d8e | -9.6205 | -61.8259 | 2026-09-16 16:10:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| c8434f4a-5909-3e4d-b092-d149f7f080fe | -9.4139 | -50.1103 | 2026-09-16 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 0a80dff5-b56c-36be-8db7-243d67a92fe3 | -11.2693 | -54.0129 | 2026-09-16 16:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9d543647-1e00-3ce4-ab06-bad5b1003e95 | -14.54 | -40.8 | 2026-09-16 16:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cddcd889-9618-33a9-874c-a1cad2d18bba | -14.57 | -40.81 | 2026-09-16 16:15:00 | MSG-03 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7bfab6df-8eb1-350f-815e-b62412837719 | -8.6309 | -66.5658 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| b20492ee-2563-36b0-b567-ce409cae3c4d | -12.6821 | -54.7174 | 2026-09-16 16:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 033308a1-7463-3f9d-a983-ac47e14333eb | -3.4645 | -57.9808 | 2026-09-16 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 97e6d9d7-036b-3f97-a06e-75e06d0cf95c | -8.6188 | -44.4819 | 2026-09-16 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 576bb777-8ca4-3a5d-ae52-ddd248981f06 | 2.2187 | -50.8977 | 2026-09-16 16:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f502f2a0-d0fd-37e2-b706-2b08fcf05bb5 | -9.3572 | -50.137 | 2026-09-16 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 58074a36-0a75-3530-9644-2191701d1ba3 | -8.6493 | -66.5839 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6782f992-bb99-3938-8817-d6fc95addc51 | -11.2693 | -54.0129 | 2026-09-16 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f770c69d-c80f-3caf-aedf-2d9244fe7bf7 | -12.6636 | -54.6782 | 2026-09-16 16:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 0759ab23-0f58-31b0-9f04-4527ed4812ad | -14.2558 | -53.131 | 2026-09-16 16:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 659a625d-89b4-3fc7-927e-434233e3a559 | -8.6184 | -44.5049 | 2026-09-16 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 4f5089b6-9403-373a-8ef4-df4585bdbe45 | -9.1337 | -65.8253 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c3ac6a0f-c3b6-396e-9aea-189b26f90a3f | -9.1151 | -65.8446 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 403eeeb9-4fef-34a7-803c-7fc2c82b0fb3 | -3.4279 | -57.9816 | 2026-09-16 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 97d41058-c16b-3e4a-8fca-d5278baf5df1 | -9.6205 | -61.8259 | 2026-09-16 16:20:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b7af7e35-d4c8-3a32-900d-955a3d88d200 | -9.2075 | -65.9163 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c229664a-4d86-3295-bb7a-205a917b83bc | 2.2002 | -50.9189 | 2026-09-16 16:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 23f3aaec-1214-3c75-98da-990427fe65f6 | -7.7993 | -66.9018 | 2026-09-16 16:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 822d847d-48c8-3284-a330-87b8b9968d5e | -9.3954 | -50.0908 | 2026-09-16 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 4a8505ce-146c-3ab9-ae13-2d5aa67fe43a | -12.1265 | -44.199 | 2026-09-16 16:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| de557c2e-e31f-3534-b40c-fb302f7da050 | -8.6311 | -66.5101 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 35fb3def-6e41-3660-bfa6-cab9f04be07b | -12.6826 | -54.6763 | 2026-09-16 16:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |


[Clique aqui para ver as próximas entradas](README87.md)
