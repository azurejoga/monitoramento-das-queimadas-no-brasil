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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 787da125-1125-3a9f-b3cd-b30efa448fa5 | -10.52327 | -69.33237 | 2026-09-28 06:16:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b85f13b-bd6c-3dcd-950e-e2eed84ad7e0 | -9.16995 | -61.408 | 2026-09-28 06:16:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 5038b639-b560-3ca5-a64c-15315c3b8cc3 | -9.92777 | -60.72225 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 138b5e2a-c743-3491-b0f6-2b1baea57022 | -9.93379 | -60.72385 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca66f68c-679b-3f8e-a08d-27c42a0d7135 | -9.1707 | -61.40183 | 2026-09-28 06:16:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 7a6b571b-08a4-399c-b550-2d251ff51e4b | -10.12122 | -69.14768 | 2026-09-28 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f79a45a-7d7b-3090-a756-27feae7ae405 | -7.69475 | -72.42161 | 2026-09-28 06:16:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bace0dd-a9f4-386a-ba77-4830fd8e5dd7 | -10.81488 | -60.74557 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7dc34f7c-a44b-31e4-86b6-b0067267bea4 | -10.57553 | -68.27833 | 2026-09-28 06:16:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30583448-92af-3e65-840f-83ec4592930e | -10.17053 | -63.0585 | 2026-09-28 06:16:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92893078-49ee-38c2-bdfc-2df80f12bc7f | -9.93456 | -60.7171 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5d0f90a-457d-3348-8757-d9836cedc892 | -9.92757 | -60.71619 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6307b181-81ca-3754-b3b4-c7141da68f1c | -9.177 | -61.4073 | 2026-09-28 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 20248eb8-6922-3977-a2c5-15359b9246cd | -9.1584 | -61.4082 | 2026-09-28 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 29cc8be0-d990-3275-9e94-432d20483d9c | -9.1584 | -61.4082 | 2026-09-28 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| b3fe8500-aa30-37f8-ac51-7d250c536460 | -9.177 | -61.4073 | 2026-09-28 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| df75c608-be46-3f4c-bc87-facc4e123684 | -3.94227 | -42.54781 | 2026-09-28 06:31:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 054d145b-8e99-35f3-b783-038d6286283e | -6.30627 | -43.60155 | 2026-09-28 06:31:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2c2d30d6-e09e-3fff-9c86-caa493801d18 | -2.76802 | -49.47574 | 2026-09-28 06:31:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| bec424c4-26f0-322d-9ccd-6012ed1a47ca | -5.72682 | -43.27507 | 2026-09-28 06:31:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 031778cb-526e-323d-9b95-072f9677f857 | -5.99618 | -47.39846 | 2026-09-28 06:31:00 | AQUA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9e0c972a-5977-373f-9031-b3215f9e6883 | -5.63302 | -43.71677 | 2026-09-28 06:31:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b6e0f0ca-03d0-380e-934b-246f4efcddd9 | -2.77166 | -49.4688 | 2026-09-28 06:31:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 00017773-e165-3b68-a8ba-678f4e6a9bd5 | -3.93348 | -42.54653 | 2026-09-28 06:31:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| c1f00191-3415-3a27-b1f8-8d917edf1028 | -6.30495 | -43.61028 | 2026-09-28 06:31:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b236a07a-b64e-3e7d-8d21-82d45fc4bbad | -5.63169 | -43.72552 | 2026-09-28 06:31:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 74832294-8a61-3a6e-9fbd-36c8f69a322b | -2.7685 | -49.4896 | 2026-09-28 06:31:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 4c3ae161-4d2f-3698-90b9-eeeb71649225 | -3.93217 | -42.55529 | 2026-09-28 06:31:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 0554eb47-0ea9-395f-8056-0da6fe0ee4af | -5.7255 | -43.28381 | 2026-09-28 06:31:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 92899229-ab52-3971-a7c1-198676583512 | -3.94095 | -42.55658 | 2026-09-28 06:31:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c2e29988-52c1-39cd-9faa-b75248573a10 | -6.94373 | -41.61805 | 2026-09-28 06:31:00 | AQUA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e63c94f6-2172-3208-b1ac-1f8ade8d68e7 | -5.99818 | -47.38581 | 2026-09-28 06:31:00 | AQUA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| aa417a73-34b3-3668-806f-a86acb3c8c25 | -2.76469 | -49.49648 | 2026-09-28 06:31:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d6e9de61-438f-3239-ad30-0cd64ad9818f | -1.93446 | -52.12546 | 2026-09-28 06:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| e85963c4-ea73-37f2-908a-2bfe813d585e | -6.94517 | -41.60817 | 2026-09-28 06:31:00 | AQUA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| badd7e12-5198-3142-b710-e13d7ccecf87 | -3.41358 | -48.32715 | 2026-09-28 06:31:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c64d35f6-12da-3ed4-94ac-0739050b827c | -9.14888 | -45.63483 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2133a34a-d821-3a97-b47d-3925e79159d7 | -11.86197 | -47.09254 | 2026-09-28 06:33:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 27299488-b0ca-3767-8f38-b16ffe91ddbd | -7.38106 | -42.1064 | 2026-09-28 06:33:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 66cf9c91-0bab-3c94-b52d-24fcecbbe83a | -12.74155 | -47.31968 | 2026-09-28 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 06c6f41c-8674-3c07-a642-92cf5f5f8103 | -11.5496 | -50.5021 | 2026-09-28 06:33:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 837f8895-f72e-3082-a195-0e29beeb7c10 | -12.7372 | -47.28724 | 2026-09-28 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e07f0d53-3a3a-3016-940c-c9aad0648d32 | -12.63105 | -47.31592 | 2026-09-28 06:33:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fa0f2fd1-8dba-34d0-b61a-a15a7f9e1e8b | -12.05373 | -46.47191 | 2026-09-28 06:33:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8eca2551-41e6-3723-8bce-89968c715bdb | -8.24115 | -45.40409 | 2026-09-28 06:33:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 461c0273-cc36-3332-a73b-0085b599ccb2 | -7.88262 | -45.44843 | 2026-09-28 06:33:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0acda689-033e-3991-bc45-4b61e771bba4 | -11.18231 | -44.81321 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5546e1c1-ab07-313e-8620-c9cb146a5b49 | -11.18366 | -44.80434 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 278.9 |
| aa87c4de-806c-37e5-bbcc-e47722585ff6 | -12.68333 | -45.02537 | 2026-09-28 06:33:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a778e9cf-75c3-3fe2-b708-6fcf39d3ec45 | -8.65507 | -45.41712 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f202db39-d57c-3995-a5d4-e9b35bc70334 | -10.7946 | -48.73737 | 2026-09-28 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5b0523f9-8bd1-313f-8715-0d1b1bc835ec | -11.13109 | -50.06019 | 2026-09-28 06:33:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 75e521db-d212-30ee-8305-38dc452b39c0 | -11.62426 | -46.78661 | 2026-09-28 06:33:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 4c2328b6-48fd-398a-9616-e7e4a084f27c | -10.79687 | -48.72345 | 2026-09-28 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 17908f8f-6adc-348a-8f1d-cf23eddc510b | -7.68004 | -44.78923 | 2026-09-28 06:33:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c4178662-5815-3e43-a8cd-1b7c66233988 | -12.21663 | -50.34267 | 2026-09-28 06:33:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8ec61e09-85d7-35a0-9a06-e5221b519c53 | -12.74321 | -47.30939 | 2026-09-28 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 5ac36276-2392-3d43-8ab5-59014f59655e | -11.38694 | -45.40247 | 2026-09-28 06:33:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c5eda68b-25db-312e-b6e6-adb8df4d9799 | -11.19107 | -44.81455 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1a9a8aab-8544-3ef5-a672-34797ff06316 | -11.19242 | -44.80568 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c023824b-bb9a-3554-ae7c-2ce2c0baf129 | -12.68723 | -47.32505 | 2026-09-28 06:33:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1afb4ca5-e20e-3eb0-b75f-e03c01e7b9cf | -12.62938 | -47.32621 | 2026-09-28 06:33:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3de748cc-9b7a-3f51-aee1-ee9349005dc3 | -11.48479 | -47.37953 | 2026-09-28 06:33:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f7049ea1-3088-3736-a269-20c377c4d18b | -12.74487 | -47.29908 | 2026-09-28 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f439ba87-1768-3883-81b5-e4bc08a3f2db | -8.36434 | -45.44783 | 2026-09-28 06:33:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b69d70e0-b424-3152-a5a3-7927f163d920 | -8.43612 | -44.86208 | 2026-09-28 06:33:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b6b1d533-aea6-3bd6-a82e-acaad76bef21 | -11.18635 | -44.7866 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30f4e791-1b91-3739-b488-61a95f2c4184 | -10.29198 | -48.15591 | 2026-09-28 06:33:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0e63b819-f6f7-32d8-a358-609e9f608090 | -12.7476 | -47.34178 | 2026-09-28 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 44bd4282-eef5-3d78-9f43-5adda2c40568 | -9.77361 | -44.8317 | 2026-09-28 06:33:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 556d6880-7275-3e31-99bd-d7ce82872cc9 | -11.44187 | -44.92665 | 2026-09-28 06:33:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a111c9f0-82d8-3f81-9ccd-39c37da00f90 | -10.80525 | -48.73869 | 2026-09-28 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d2ed429c-658a-350b-9acf-5710ce46c8b0 | -7.88407 | -45.43905 | 2026-09-28 06:33:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e2033ab5-c2dc-35d6-b560-15b39ef58fa4 | -12.65914 | -47.32048 | 2026-09-28 06:33:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 80d84fd4-ddb2-3276-95a3-d7cf53915fdc | -11.70422 | -44.53383 | 2026-09-28 06:33:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3aa430c-09da-3b18-a7e9-fc5a4f37a0f6 | -12.65748 | -47.3308 | 2026-09-28 06:33:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 65aacbb7-2b4b-3e68-a69a-a5b88c59a280 | -12.73989 | -47.32995 | 2026-09-28 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3823e20c-6f65-367b-8637-6592a39a0cf3 | -12.31336 | -46.40599 | 2026-09-28 06:33:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| fc964bfd-d726-3c6c-ad95-0872ca8686e9 | -8.36575 | -45.43868 | 2026-09-28 06:33:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f534729c-f2ae-3e35-b662-45fbb051c92f | -11.62269 | -46.79648 | 2026-09-28 06:33:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 01dbfe30-f21b-3e24-b9c4-ae3613583f02 | -11.44928 | -44.93689 | 2026-09-28 06:33:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68cdb7af-ff2d-339b-a233-133809eddd00 | -11.78555 | -48.33107 | 2026-09-28 06:33:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| be146bdd-89c4-3d72-aefd-3822c8b8a996 | -11.18501 | -44.79547 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| ede33e22-378c-3f7e-b7ed-1b490c6d34c4 | -11.19377 | -44.79681 | 2026-09-28 06:33:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ce97c33b-16fb-3de0-8b18-cdc744bb7a6a | -12.68468 | -45.01646 | 2026-09-28 06:33:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d00f064d-168e-3b64-8dd3-da04731d225f | -7.38139 | -47.01563 | 2026-09-28 06:33:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d7cd43a-a65b-3c8f-8f6e-c9f745516f9d | -7.2711 | -45.33936 | 2026-09-28 06:33:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d2241ce9-6319-37da-92ae-6329964cfa2f | -11.70556 | -44.52493 | 2026-09-28 06:33:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d6c62f8d-66dc-3fd2-a18e-e8bca88761a0 | -12.06275 | -46.47356 | 2026-09-28 06:33:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1022e370-071b-3e61-a543-54442e2b1d0e | -11.45064 | -44.928 | 2026-09-28 06:33:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6b9947dd-7b9e-351d-91ff-4a0f8d724e19 | -7.26206 | -45.33799 | 2026-09-28 06:33:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 596fc303-653e-3eb1-b191-d27531a5892e | -12.74925 | -47.3315 | 2026-09-28 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 63f678c3-daa6-312a-b1d3-e17de9c6f55a | -10.80736 | -48.72565 | 2026-09-28 06:33:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8b8eae10-4eb0-317c-9157-77689ea61ded | -8.22639 | -45.43983 | 2026-09-28 06:33:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b7aa1a7d-ec97-3e13-aeaf-3c68e7fac373 | -15.02152 | -49.57865 | 2026-09-28 06:35:00 | AQUA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 85c991a8-5006-3bfd-8e5f-cc223c0b3e08 | -14.59585 | -45.58918 | 2026-09-28 06:35:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 45f8c877-711b-310e-8e6b-1dc805d419b5 | -13.4685 | -48.59837 | 2026-09-28 06:35:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b19a5c99-023f-3c8f-bf04-a766bf81317d | -15.18184 | -46.16214 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| cec27b88-5843-3064-a528-e4f16e736123 | -13.1584 | -48.54508 | 2026-09-28 06:35:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e6a8be96-dad0-3826-a61a-fb5d11aca278 | -15.41091 | -47.93079 | 2026-09-28 06:35:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README68.md)
