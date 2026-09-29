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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bef13354-e127-3387-b18e-463678f34d6a | -13.1992 | -48.5603 | 2026-09-29 13:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c8177efa-f53f-3392-8dfb-7f0c7840082b | -12.7421 | -47.2684 | 2026-09-29 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 214.2 |
| ed6577cd-a925-35c9-9efe-8bfef1cb9845 | -11.9428 | -50.5273 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 299b7f4b-494d-3c5c-abe9-872605beb0a3 | -12.2897 | -50.2712 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 67b73b9f-0a6b-343c-bbdc-f4737bd65744 | -18.1144 | -44.3988 | 2026-09-29 13:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f3541c39-a771-3811-a598-d666db7deb6c | -11.9047 | -50.5317 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| faed625f-3753-3bec-abef-a677b73e88c9 | -8.6451 | -45.3489 | 2026-09-29 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 5adee53c-7db7-3ef7-81f8-94f97bc6ce50 | -11.4307 | -43.4358 | 2026-09-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 1e7925f5-3e2e-35fe-8f72-a541be1b6017 | -11.8453 | -47.0806 | 2026-09-29 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 4a74220f-04a3-319c-85db-8e97251e8695 | -8.664 | -45.3469 | 2026-09-29 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a82b3392-6721-3cbe-98d2-3588dee969ac | -12.7598 | -47.3555 | 2026-09-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 81c7debe-617c-3dfc-be4e-7ad3a51d4709 | -7.064 | -42.0648 | 2026-09-29 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 16d2ef16-6170-3c20-add1-803b3247104b | -18.1151 | -44.3745 | 2026-09-29 13:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 128.6 |
| a7319282-f3be-3a71-89ce-512a577d37c4 | -11.4495 | -43.4566 | 2026-09-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 162bb0a4-4788-32ee-aa5f-b199c60125e3 | -12.1543 | -50.395 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 1593a015-b71b-3e00-be56-b0fb83b4a89c | -12.6078 | -47.2653 | 2026-09-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d32dada1-80f1-3800-929a-a57aeceea610 | -11.1897 | -50.056 | 2026-09-29 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 8696a6c8-57a4-30ce-9a01-9d645502293a | -10.3894 | -61.2502 | 2026-09-29 13:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 214.4 |
| 97ba3bca-58a2-3846-bdcd-faf81d0c56ce | -11.9034 | -50.6175 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 000ca18d-0d74-3c2c-8009-a116d2e6941a | -10.1095 | -50.2135 | 2026-09-29 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d3b6cfe9-3288-382a-9e97-4d7ef8431d79 | -10.3895 | -61.231 | 2026-09-29 13:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| ed2a8b1c-726a-3562-a893-946c03da006d | -12.761 | -47.2881 | 2026-09-29 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1b8d9bd6-34c7-3927-884c-fcffc0311c31 | -11.4298 | -43.4833 | 2026-09-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9794aae3-46ae-3776-90b8-d79f388b379c | -9.4702 | -45.8023 | 2026-09-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c61b1a64-7d06-3e4e-baca-ea0c7dc56b36 | -8.9294 | -49.7706 | 2026-09-29 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a6fe44b4-0de4-3363-98fa-4306eb9b8fb5 | -11.4302 | -43.4596 | 2026-09-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 59c1bb39-08b0-3d3a-9b05-6023aed0dfce | -9.9773 | -50.2267 | 2026-09-29 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c57415a7-18fb-3c55-b080-fc543741eaa3 | -9.9595 | -50.1431 | 2026-09-29 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ece268f6-a4de-392c-8a07-07aa7fb965d3 | -11.8675 | -50.4718 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0d439bbc-0120-3fcb-ac4d-b7e2237ccf67 | -12.2723 | -50.1657 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 1944da82-6c15-370c-9bba-5335fc4a06d0 | -9.1337 | -49.9656 | 2026-09-29 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 03a52481-d0c7-37d4-88ab-290bc2350c89 | -11.9037 | -50.5961 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 26230421-7d7c-3cbf-b950-1943d2116d6e | -14.1309 | -46.2801 | 2026-09-29 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 751fe1ad-72a0-37da-994e-2080c9d74a7f | -11.1907 | -45.1274 | 2026-09-29 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f36e5c37-55b9-37a9-9cf0-efa33be62915 | -12.01 | -50.97 | 2026-09-29 13:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7088f0b-ca92-396e-a315-138224dde0e1 | -5.73 | -45.14 | 2026-09-29 13:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2ed61ae-89e5-3759-8eb0-84c0069c72ca | -12.01 | -50.91 | 2026-09-29 13:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2233869a-1587-3b9d-96b1-20cd843ec3b1 | -5.73 | -45.18 | 2026-09-29 13:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2140b655-fe0f-3671-93a8-856189d10a0d | -12.04 | -50.92 | 2026-09-29 13:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1381315c-ae03-3e34-91c2-c3b7f2c4147f | -11.98 | -50.96 | 2026-09-29 13:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35cebefc-c5f9-3416-99e2-beb7c5e725ae | -12.04 | -50.98 | 2026-09-29 13:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cad6daa1-028f-3f5c-ad76-2f3742b58079 | -10.3895 | -61.231 | 2026-09-29 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 5b02c5c5-ec7f-36e2-ad31-d06922b125c1 | -11.1907 | -45.1274 | 2026-09-29 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 86d38512-ee5f-37af-9463-e1388cc01800 | -12.1074 | -47.4027 | 2026-09-29 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8c2900ae-2fd5-381b-942c-087962c2fa3c | -14.4839 | -47.0414 | 2026-09-29 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 14d51bc5-702b-3ea5-b5aa-4a710f729eba | -12.6267 | -47.2851 | 2026-09-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 773c8d1f-38c7-341a-9ffe-5131af427852 | -7.5057 | -44.5733 | 2026-09-29 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 44b11991-c7d1-3672-a8eb-1719295c2cb6 | -10.3894 | -61.2502 | 2026-09-29 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 680bde8a-c7a5-355d-884b-c3ff85e589b0 | -12.386 | -50.2163 | 2026-09-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c85ed1e5-0a5c-3bb8-a29f-76f52d780cb9 | -12.7598 | -47.3555 | 2026-09-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 661ad6cc-aa34-3d89-bf75-a53eeef54573 | -9.977 | -50.248 | 2026-09-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 708d2bf1-ffc3-340f-9d47-0452df32a156 | -11.6213 | -46.7742 | 2026-09-29 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 666f2b37-4850-33aa-8e2a-a051ce73f6c2 | -11.0983 | -46.0992 | 2026-09-29 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e98a9a0d-8435-3c72-8725-8e0686fe7a52 | -14.1309 | -46.2801 | 2026-09-29 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 145.5 |
| cbb9a3f1-6c59-3c83-b300-c55e304908db | -8.0355 | -42.866 | 2026-09-29 13:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 038c48f1-fad3-30f4-bcc8-a3ece5053bfe | -10.2843 | -44.6274 | 2026-09-29 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a1118480-78de-37f9-ab0b-af122ea5d13c | -7.7315 | -44.5743 | 2026-09-29 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1f523729-80cc-35ee-9911-e57dcc84dc67 | -11.1966 | -44.7805 | 2026-09-29 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 4c3d65a9-e75c-3039-9ac2-fadb77e29378 | -12.8847 | -44.8015 | 2026-09-29 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.1 |
| 95cdd42e-f3bb-3d32-b8a6-eb99c90b78f5 | -13.6762 | -45.7822 | 2026-09-29 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 498.2 |
| cb79d2b0-ebac-3e18-8cb8-827a123fcdfa | -7.506 | -44.5503 | 2026-09-29 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| cbac8f4c-7c77-3110-be1e-4098442741d9 | -12.7417 | -47.2909 | 2026-09-29 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 125e3539-84e3-3e48-b0d1-d0bd6d4ed25e | -11.1775 | -44.7832 | 2026-09-29 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 419.9 |
| 84da0588-c9e8-39d3-9b63-5a1a1d839e87 | -7.4871 | -44.5521 | 2026-09-29 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 52b9f820-d492-3b60-be7f-43be568459c6 | -12.2723 | -50.1657 | 2026-09-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 860d0d81-c909-3df7-8805-a468880a9148 | -12.761 | -47.2881 | 2026-09-29 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5ac33206-69d7-3216-9294-7082e8ba3365 | -12.6078 | -47.2653 | 2026-09-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| eb3ab3d5-481a-348b-8cd7-9471d7e02938 | -12.7602 | -47.333 | 2026-09-29 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 26bc2d36-1352-3d34-9bca-21e9b1bd11d3 | -13.1799 | -48.5631 | 2026-09-29 13:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ea93cd02-9a16-340d-8b69-e5f4bf339dde | -11.1771 | -44.8064 | 2026-09-29 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 329.0 |
| a2281c36-4d69-3777-b92c-12abb1d2d13c | -9.1337 | -49.9656 | 2026-09-29 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5b83cd73-4020-3ce9-83a2-b9b9817ebb48 | -9.9784 | -50.1412 | 2026-09-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b18273e8-7c1f-3522-9e2d-1497d22d9f83 | -11.4791 | -49.743 | 2026-09-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 40102d5b-9b28-3a11-bc1b-21bb2cf668bc | -11.1583 | -44.7859 | 2026-09-29 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 75a3cc75-d59c-31df-9724-181ce81de070 | -11.5727 | -47.4074 | 2026-09-29 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a74f09b2-58f3-377b-b568-b28b363bd3e9 | -8.6637 | -45.3697 | 2026-09-29 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 21215529-4cb4-3339-ad15-24c90ad37908 | -10.2565 | -50.5185 | 2026-09-29 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 756e9db4-a36e-3fbb-8596-455a229d49d6 | -9.9595 | -50.1431 | 2026-09-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b4f14034-78a5-3871-b089-66e52cc06aba | -11.1962 | -44.8037 | 2026-09-29 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 47618725-09a5-34b0-8cd1-d8c27b0a0236 | -12.024 | -47.8148 | 2026-09-29 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| d2ac4fc7-324c-3607-b737-34b4971a8356 | -9.9973 | -50.1393 | 2026-09-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 810c696f-175b-3428-9fde-20b9dc9035de | -12.6639 | -47.3469 | 2026-09-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a4f2786e-2990-3dbc-bd3e-b5eee01a0eec | -12.1078 | -47.3803 | 2026-09-29 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 5b0b535e-f7d7-375c-8a0f-22cba273207a | -12.7421 | -47.2684 | 2026-09-29 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 4dad829f-2cd9-3702-a212-c8f5e08759ba | -14.1115 | -46.2834 | 2026-09-29 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 27b06394-626f-3177-9980-7a34f3c79b6a | -9.9959 | -50.2462 | 2026-09-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0285b7e5-1a54-3e38-b56c-800671aecbdd | -12.6074 | -47.2878 | 2026-09-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| eb41f8f2-a8ce-3799-8b91-1c17bbf0365d | -11.9034 | -50.6175 | 2026-09-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0aa92bf0-cb76-3a8b-9a7c-03b4379bf199 | -8.2293 | -45.4375 | 2026-09-29 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 94d0b393-23bf-3115-aaa7-10d33cdb44ef | -9.9773 | -50.2267 | 2026-09-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 64262f60-b7b0-313e-a4bb-d60309ffab0c | -13.1992 | -48.5603 | 2026-09-29 13:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 397136a3-14db-3b9a-af22-6585e53c84b3 | -12.6271 | -47.2626 | 2026-09-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| d6e6060e-494f-31b8-b445-0e11d17a9297 | -11.4298 | -43.4833 | 2026-09-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| a378a4b0-1dbd-373a-befa-aa7603176a7f | -11.8989 | -50.9169 | 2026-09-29 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| beee7adc-1369-3b6a-91df-369d3702f10d | -11.449 | -43.4803 | 2026-09-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 7d6246b7-c0d3-38e8-981c-32a6b184da45 | -8.38 | -45.4448 | 2026-09-29 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 66d8a676-f45c-32d5-a2af-218db61a0b1b | -11.1517 | -50.0603 | 2026-09-29 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5f7f32d1-b5b2-3ed7-8081-0dcf7fb66a12 | -9.0463 | -45.0083 | 2026-09-29 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 6dc1d21f-ed69-32a7-bae6-a2a931d30208 | -7.506 | -44.5503 | 2026-09-29 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 142e28da-4244-3b91-8dc0-a81c405d81b9 | -9.9593 | -50.1644 | 2026-09-29 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |


[Clique aqui para ver as próximas entradas](README77.md)
