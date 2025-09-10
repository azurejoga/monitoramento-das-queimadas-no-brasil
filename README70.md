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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d37a7b60-bab8-323c-adc2-b297a475fa7d | -8.49047 | -51.33788 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5f7052d-966d-3c5f-9eb1-abaa6db9724b | -9.06408 | -49.83098 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3623579-64db-30f0-afeb-7baddae34921 | -11.10721 | -48.45469 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28eaf72c-6720-3382-a62d-36f5e870ea29 | -10.01268 | -51.6695 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32329f04-b80a-3601-999c-d36073589cc2 | -9.39303 | -49.21937 | 2025-09-10 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e5435c5-75f7-315a-8e42-01b318d639db | -8.04583 | -48.69709 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5adc41c-8d9f-36f4-aca8-d619fa16fd5a | -9.99717 | -51.70073 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abd3de51-02d7-3ec1-b89c-168fb7892b3d | -8.41394 | -49.10999 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1022dc23-890f-361c-a337-3d4e3a893541 | -6.84941 | -47.93455 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30acf6f6-ae22-3698-a3e3-c14de1c65524 | -7.672 | -47.96067 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f86ed76e-8753-3468-ae9d-b5d924a6eb41 | -9.82329 | -46.05606 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 758acf08-68bc-3cee-a860-6a24a8cde648 | -8.0458 | -48.67524 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8460731-666f-35ba-b964-4752b1ee994c | -8.42617 | -49.1118 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad68a528-e3b5-377f-8d57-c144403cfa0d | -8.63287 | -53.1131 | 2025-09-10 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5e337fc-0a7c-3fe8-a53a-a9010433ebd9 | -9.82848 | -46.04737 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f12804dc-b80e-3b8c-b1aa-2cf9a5766b83 | -8.04071 | -48.66367 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2840f950-855d-3398-ae3a-c55520df53ec | -10.08521 | -48.1795 | 2025-09-10 04:42:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12138600-3a1c-34ad-b3d4-559701cbcd11 | -6.87389 | -47.8902 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77cdc6f5-b3c3-38fc-af6f-c44887c59674 | -12.43757 | -44.74636 | 2025-09-10 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5d2e516-b838-3427-ac1c-722682846ca8 | -8.10346 | -44.85595 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f1fcdc9-e161-3e97-ba44-4ea9f9ff90b6 | -7.55177 | -44.66407 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d00efd8-be96-3dee-afbf-5be77ccf49df | -8.38383 | -45.02636 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a20c5506-7a58-342f-ae69-ba6bfb9f7690 | -8.07449 | -50.18848 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 166c7163-2e6d-3169-bab0-65dec92cfe73 | -10.74316 | -48.18178 | 2025-09-10 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d1574cb-1b7c-3020-a32c-0a431a03145f | -11.43829 | -43.59134 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4f4c838-ac14-3efc-aba6-4eaad42e6de8 | -10.73802 | -48.28716 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8134e879-9c9c-35d6-aab0-cb4096de1ab2 | -11.13653 | -46.35341 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74509e0c-f7f0-3dee-be63-b0a59639b3d0 | -9.06247 | -45.7522 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4014e250-396d-372b-8b30-243e83a57e2e | -10.56363 | -51.99711 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9848a5ee-3bf5-394e-8dcd-9c80544cae32 | -8.49588 | -45.66557 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa06226f-d9f3-36c5-ad0a-2fc14cd2f537 | -9.00938 | -49.53487 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 379d0355-db44-3aee-9a77-648a1f0c9e55 | -10.16789 | -52.61762 | 2025-09-10 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7f82540-88ff-387a-ade3-e97f8e8e178a | -8.74665 | -47.09535 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57af0610-87e7-3474-8245-74095eb39281 | -10.02284 | -51.67123 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f14e2989-14ff-3bb5-aed6-b6b0d5ac6504 | -10.72069 | -48.28454 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a969bdb-549a-3cbc-916b-9455ea757a93 | -7.44517 | -49.26661 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b701592-17ce-3492-bd4e-97a7f901dc17 | -8.04916 | -48.68627 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0de8ebc1-da12-39fa-8144-64d911c48721 | -6.21767 | -45.62874 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 042e4c55-3a44-3766-8ab3-ee2b1cbf3625 | -8.44525 | -47.28239 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15474d36-ad7f-303d-93c4-887a128b6a67 | -6.38234 | -44.45634 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fac09ab-e970-30a9-8a8e-90fa51d5a188 | -7.86045 | -46.25501 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c4c821a-8eb5-397d-8040-a0ba98899bf5 | -9.44461 | -46.69981 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66fd1bf8-7e91-3ec1-b888-986a1a55108e | -9.21822 | -50.54801 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63d196e8-ed92-3a66-96aa-7b48eeb90ea7 | -9.69683 | -46.757 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 538b2381-9f3b-3449-99d0-5849ae50d2b8 | -7.77502 | -50.77231 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48b9ba25-f3fd-3f97-b07d-d36ab6bba44a | -5.41748 | -51.53519 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43a63bc3-30d6-345a-970a-a0953e3f20c4 | -7.37449 | -47.44001 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 955eb9cf-f76e-39ea-b9cf-a6af25129ca5 | -6.87038 | -47.88945 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03aa5768-99a9-3852-9d5d-6df7ab03218e | -10.02682 | -51.66817 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 804e5cfb-f338-3622-b20f-4fc1eb633728 | -9.67318 | -46.58393 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b65ef556-0a28-358b-ac28-98cd00c566ee | -9.07578 | -45.769 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c7cc994-dfde-34f2-a45f-8f0ab5aeb1dc | -7.74038 | -50.75204 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7189c1d9-2e4d-3455-b750-31bf279bc3b1 | -10.19352 | -46.68261 | 2025-09-10 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b766a8e-8340-3b82-adff-b68bbe1d5289 | -9.09804 | -46.98098 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78ad7bb9-e12c-3dc8-9b36-e15f1e8b69f0 | -7.79172 | -46.09482 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41cfee13-6452-3a19-892b-5de8c9cfc752 | -11.66824 | -46.91051 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d840fa54-aab4-3757-a608-9908ea1e4772 | -8.38194 | -47.99117 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 064f62ca-8d7c-3b08-b079-2fc134b85689 | -8.04299 | -48.67116 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7355ba4b-fe34-3316-a465-98bfb7e5c3af | -10.02343 | -51.66759 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d46a6273-245d-3215-8dc8-8fee99af37a2 | -10.17127 | -48.3465 | 2025-09-10 04:42:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d521c3de-61c9-377c-8f4f-0598bfe85a60 | -6.44174 | -44.05663 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b57ccf08-4edc-3374-9c40-cdfb7023af5c | -8.06421 | -52.32641 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7713608-ece8-3f55-82be-355ee72ff847 | -9.76488 | -51.1265 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28757fb7-ca5a-36b1-a3d1-6a0ad45dc70b | -10.54907 | -51.50711 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9728e39b-6b90-307c-ab55-ef3dbdbb5b00 | -11.26436 | -51.12231 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e428929-e859-328f-bdc9-9044904739c9 | -7.71126 | -45.14856 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8a28f71-4d8a-3557-811b-b58c8e69c94d | -11.49436 | -50.42125 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d53b7c0-cf0c-3c45-876b-258deaead612 | -8.19342 | -47.161 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 693b989b-dba1-3e13-90bd-dfe6cba1f312 | -11.66762 | -46.91487 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecfdeb0b-2c81-3d7d-8058-ba174a618799 | -7.7683 | -50.77122 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65de5a71-8217-3680-8671-3c5115bbc580 | -10.14447 | -46.17405 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ba64dfe-4111-3fa9-8123-1b2fe154d87e | -6.87333 | -47.89386 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7d35801-563f-3661-b0d2-5a11f9a204ad | -9.09926 | -46.97277 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df9f8edb-9cac-36ae-97f4-afa262c8cfd0 | -9.31891 | -46.72442 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5300abdb-acb1-36b6-8244-48ae405ed816 | -9.6719 | -46.5928 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a56e6844-fb2c-38b1-879a-c49e18a616cf | -6.52772 | -51.055 | 2025-09-10 04:42:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fbc2a59-a34d-3639-9403-ca54870c3f1a | -9.06869 | -46.97482 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e3ecce9-b0a7-384e-a5d3-8bc23c1673f8 | -9.35788 | -46.50124 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa3a709b-afc5-358b-a75a-3b7455819001 | -6.60156 | -43.96075 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55f6eb89-3729-39ce-ae54-23fde0d8519b | -8.42671 | -49.10826 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74ab7646-f165-3096-988f-b6df6e363530 | -8.04102 | -52.37939 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db3acd79-e436-327e-b1de-7895669b7214 | -9.8891 | -46.47546 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88926573-95a8-3576-80d6-08d7f3ecaf61 | -7.88292 | -46.26964 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2ba56edf-96c2-39e0-993d-791a1c8f9d8c | -6.67917 | -44.10579 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52c1b84f-8610-3630-9219-acea1888d092 | -11.43383 | -43.62447 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a94d56-4c6b-3946-b802-7bb1e4d97991 | -11.4337 | -43.59064 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed0a16f8-f17a-382a-9bb0-3c17e758caa7 | -9.04763 | -50.49553 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19fea01f-c61a-3810-91cd-36465e0d9a04 | -8.04635 | -48.6717 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c07ceea1-9c47-3ed9-aa0e-803e6d730542 | -7.25992 | -44.45739 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 945d717d-b939-3c2c-82da-a3e85ee44b8f | -10.72647 | -48.29325 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6130b3f9-54f0-3a9d-a22b-5e349ff2eb20 | -10.01355 | -51.70707 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ca45b42-9744-3fa4-b6ff-cf7a0a870527 | -9.52041 | -54.65009 | 2025-09-10 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e8bf1c-7f4a-3e0b-b4ab-c941d9cdbc5c | -11.42117 | -43.57927 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b877aac-d64a-3738-a85b-24806f148025 | -8.04806 | -48.69339 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| acb1384d-2a81-3d9e-82d1-619eeba37abe | -5.79597 | -51.67266 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36d5d13e-89f0-309b-8004-08872ef91aeb | -8.84488 | -49.5738 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22726dbe-cf98-3df2-adf7-37123163f465 | -11.49769 | -50.42179 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ad7484-b008-3419-a906-fb572e2f1f8e | -11.57461 | -44.65837 | 2025-09-10 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efcea3d8-7b7a-378e-9a12-123feec7d1fa | -10.55917 | -51.5088 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb4739d0-5e5a-3b0a-baf6-95587e6a543a | -8.04414 | -48.68589 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.1 |


[Clique aqui para ver as próximas entradas](README71.md)
