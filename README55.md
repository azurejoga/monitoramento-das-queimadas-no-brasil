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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01ba6d6f-53cd-3bf6-b61b-fba2ea4720b8 | -7.6329 | -46.6172 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| a42e78be-fc56-3f5b-8ca3-f8ffec0e9c38 | -11.385 | -44.9386 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 06ff4f97-489d-38bb-aa9a-29586b090c53 | -8.8603 | -46.2075 | 2025-09-26 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0d55df88-76f8-3f2e-b8de-9dce045b697c | -11.7019 | -44.3347 | 2025-09-26 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 4bef72bb-0a97-3409-a600-cf8e0e08d56a | -7.3755 | -44.4478 | 2025-09-26 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a32beae6-d0ce-3102-b7f5-d17ab3d4069b | -9.109 | -48.8933 | 2025-09-26 14:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 70856583-4a41-3032-a39a-b6c4312fc220 | -5.3695 | -42.284 | 2025-09-26 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 651a95ac-a496-3ea8-87fe-3306c011eeb8 | -13.3463 | -47.8732 | 2025-09-26 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 0d0a1f02-1d31-3ab4-a264-e7778851f859 | -11.7977 | -47.6449 | 2025-09-26 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a2df1261-ceb7-3fd0-897a-43ec2fa09782 | -17.1746 | -56.3478 | 2025-09-26 14:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| f1e74fad-d1e8-38a3-935e-a3dfae7d0b5f | -11.6814 | -44.4078 | 2025-09-26 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| c776572a-a431-3cb3-958a-e492531cada9 | -12.3427 | -50.544 | 2025-09-26 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 0a5b8802-778b-3962-9ee8-05e116ac67b8 | -13.2393 | -50.6895 | 2025-09-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 0992baf0-5b07-3737-9e50-a8948177d833 | -11.6425 | -44.4369 | 2025-09-26 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3f031e38-841f-3788-93b3-4f801e5aac3e | -11.6457 | -45.3388 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f7932662-f7e7-3699-ae3b-5cbc7001b146 | -7.2206 | -46.6084 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 28643e47-2fa4-3455-a946-d977ed361480 | -7.6775 | -45.9872 | 2025-09-26 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 72ac8ebe-668c-3546-9a96-0e1352d6dcc5 | -11.0131 | -44.3424 | 2025-09-26 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| ac1ea97d-8b8b-30de-875f-95fefc6900a5 | -9.8658 | -45.9372 | 2025-09-26 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a3d9ef60-30f7-3386-a8c5-f22c227f3363 | -3.45 | -44.1238 | 2025-09-26 14:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3ece9c39-284f-387f-9200-551ee88fea9c | -8.8409 | -46.2544 | 2025-09-26 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 1af3d762-4644-3a2e-924e-5992de492238 | -5.4562 | -43.0788 | 2025-09-26 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4e660fc0-6920-3390-9e70-c1216b35fc4a | -14.866 | -45.5511 | 2025-09-26 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b008f3e9-df68-3416-ab6a-bb25f4872cf1 | -10.786 | -45.3891 | 2025-09-26 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d022740b-4a28-32ff-b017-792c247b1180 | -17.1939 | -56.3661 | 2025-09-26 14:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 224deaa9-b604-327e-832b-9ec013277159 | -3.7814 | -41.7196 | 2025-09-26 14:10:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 4c160058-c41f-3558-85e3-e011e971ad6f | -20.7537 | -57.8265 | 2025-09-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 7808a366-d08b-393a-b89d-4ac50de201c4 | -10.5975 | -44.0975 | 2025-09-26 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3a3f6693-36b9-3c88-9450-e3aa9f733bfe | -20.7338 | -57.8083 | 2025-09-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 253.3 |
| ac24bb98-1fb6-36cf-a341-b59915a24d26 | -12.631 | -48.1313 | 2025-09-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 4e8c2d7d-02e9-3415-8d86-83d9b1983496 | -5.8646 | -45.5958 | 2025-09-26 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 87f3a334-92b1-35ef-b257-580090726a89 | -10.9381 | -44.2598 | 2025-09-26 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3054c5c4-31b4-3a44-a8ff-cb2575c5286a | -11.4102 | -43.5099 | 2025-09-26 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 3a610658-2d8d-3d99-98f3-e1bdf6e11b0d | -11.4229 | -44.9563 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| eef18e4a-99c4-3eec-80d3-dad54115b298 | -14.1149 | -51.1968 | 2025-09-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 864a29b1-b0e6-34c5-8520-c92b04ee26e6 | -10.3938 | -46.1444 | 2025-09-26 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 8a2963f8-e8fe-3866-a133-61359d60a5e8 | -11.4033 | -44.9822 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 4d033aad-c749-39cc-89d0-29e858d93d47 | -10.4125 | -46.1647 | 2025-09-26 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 8bef337e-37e0-3249-bc65-7feab19afaf2 | -5.3091 | -42.761 | 2025-09-26 14:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 6e9591de-8414-3d98-970c-97b6b677f438 | -6.078 | -44.7418 | 2025-09-26 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ff1face9-9229-38ff-8fc2-b122507b49c2 | -5.475 | -43.0774 | 2025-09-26 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 503a2861-8ca7-3136-8afa-7e7414f00eba | -7.6772 | -46.0097 | 2025-09-26 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 89ba64b8-6f63-35ce-9906-f75a28a5c2b1 | -14.0964 | -51.1564 | 2025-09-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4d788164-ed63-37a4-9c4e-15febfbc9a3a | -7.3559 | -46.2177 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7bc24ed5-817b-3903-81bc-8551a5ed1402 | -11.6618 | -44.434 | 2025-09-26 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 55d21dd5-53e9-3278-adee-15cc1825dda3 | -8.7708 | -43.0417 | 2025-09-26 14:10:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 660b39a3-9a32-31cd-85cc-f0cf63ea87a2 | -11.9655 | -47.8891 | 2025-09-26 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 1a4ec50d-1b12-3bdb-9a48-63103dbe722f | -14.1153 | -51.1753 | 2025-09-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 45156915-70b8-3f09-b3ce-9bf3949748f2 | -10.8055 | -45.3637 | 2025-09-26 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 13a099e0-6385-3de1-a32b-11f96e431e26 | -11.6233 | -44.4398 | 2025-09-26 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| bc960793-6673-3ecc-9b99-4aa27f020472 | -12.6118 | -48.134 | 2025-09-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3550b904-d845-333c-bb4c-db9d12ac7201 | -10.9374 | -44.3065 | 2025-09-26 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d1e618e6-77f9-39aa-8d6f-3317f0b221c5 | -12.3424 | -50.5655 | 2025-09-26 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 344.0 |
| d13e2f3c-298c-33b2-88f1-346072ec6cef | -10.5979 | -44.0741 | 2025-09-26 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b023b809-a61c-321c-bd47-761f5a5861ea | -11.4225 | -44.9794 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 264.8 |
| a8668108-3459-3fbb-9808-76b9bc9a8f2e | -6.2687 | -42.4957 | 2025-09-26 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 7b8bf77a-deb6-3fb8-96fe-ac152d284fd6 | -11.7006 | -44.4049 | 2025-09-26 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| c8c326e7-575c-35e9-abc8-15a03cee1a2a | -10.3935 | -46.167 | 2025-09-26 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 83358128-4c57-33d0-9352-2c1941a98c86 | -8.7139 | -47.358 | 2025-09-26 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 979b0840-ea39-33d3-876e-50b63ab37b2a | -10.8051 | -45.3866 | 2025-09-26 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 505.8 |
| e5ac7232-e13f-3cde-94c4-7b7e0df6f66f | -11.681 | -44.4312 | 2025-09-26 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b90db07e-3ae8-3024-926d-5b4d8e453544 | -10.8238 | -45.407 | 2025-09-26 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 677.5 |
| a5fbff87-2fe1-3782-923a-e3573e1ea80c | -8.8415 | -46.2095 | 2025-09-26 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0b6aa75e-0314-334e-b947-38f1afde0d33 | -15.9273 | -57.4972 | 2025-09-26 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9f2b8e28-2b3b-33ee-b996-af8e475aea14 | -11.0127 | -44.3657 | 2025-09-26 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| ef456568-27c5-37f4-945f-ae0deb0d4969 | -7.8735 | -45.2911 | 2025-09-26 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| adf39a69-9dc2-315d-b501-fe3d1adb1b5c | -7.2796 | -42.9685 | 2025-09-26 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 1a4f0594-10ee-3a0d-a5db-5866f22b4c2c | -9.8921 | -46.7437 | 2025-09-26 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| ace131a2-105b-392f-a7db-410ac39cd8a7 | -14.8855 | -45.5475 | 2025-09-26 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 85798d5e-7094-38e6-b4a7-432a9b04166d | -20.7334 | -57.8293 | 2025-09-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.2 |
| e4388b5c-cef7-36ff-bb13-76bae1f69b97 | -10.4129 | -46.142 | 2025-09-26 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 55b5ad70-d3e7-3e26-9c21-3e63935e2e54 | -13.201 | -47.4026 | 2025-09-26 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 0e6e3210-f911-3e77-a9d3-f751bf825fb0 | -7.6584 | -46.0114 | 2025-09-26 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 4fc20692-505a-3a25-8e28-57d2d0da4433 | -7.3371 | -46.2194 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 16857fc9-56f5-3a68-8f63-eff25588d7b5 | -17.1743 | -56.3685 | 2025-09-26 14:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| ac4bf2ce-0e95-3567-aeb5-4de549f54d28 | -11.9659 | -47.8669 | 2025-09-26 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c82b7a59-6cc0-3e3a-9f26-8aaf1ea46f2f | -11.4041 | -44.9359 | 2025-09-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e3af9472-60b9-3001-b822-7b553da3ad19 | -11.6826 | -44.3376 | 2025-09-26 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 37950fcc-2864-38cb-a5eb-8215d0fa29df | -7.3371 | -46.2194 | 2025-09-26 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d87f03cc-ed9c-3856-a278-6930432a3b6c | -7.6775 | -45.9872 | 2025-09-26 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7389f281-b65c-3c2f-b97c-747e73f1fceb | -7.3755 | -44.4478 | 2025-09-26 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7f7ac726-677d-31af-a6ae-9a237d9270de | -10.8055 | -45.3637 | 2025-09-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ee5b2629-e078-3f7e-afc2-d1a4e1f0d089 | -11.7977 | -47.6449 | 2025-09-26 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 4a5d6edf-703f-33c2-9a78-8081021f1b4b | -6.7174 | -42.7393 | 2025-09-26 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 2a686eb7-82f7-38a0-993c-ccf0737d17c7 | -5.4752 | -43.054 | 2025-09-26 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 6f5fc5da-cf22-38b3-a918-13dc94af238d | -17.1939 | -56.3661 | 2025-09-26 14:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| dab86221-185e-3816-9594-cfabf762230f | -11.9655 | -47.8891 | 2025-09-26 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 64f3e309-3f5f-3ba9-b133-4475ca2a6d40 | -10.9374 | -44.3065 | 2025-09-26 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 9b4d2955-72c9-3c43-89f4-ef4cd5237374 | -12.3424 | -50.5655 | 2025-09-26 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 258.0 |
| 0f88268b-ce9e-382f-80ed-e8f2d5eed473 | -6.078 | -44.7418 | 2025-09-26 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 450cadbd-0919-312e-9c7f-54030138495c | -5.3693 | -42.3077 | 2025-09-26 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 13b3d29a-c073-387d-a0dc-c8bf340872d2 | -17.1746 | -56.3478 | 2025-09-26 14:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 168808f4-692e-3fb3-a467-ec4f01ef0f91 | -12.631 | -48.1313 | 2025-09-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| b5e60f9a-9e96-31e0-8fff-d0aee0d6c239 | -8.8409 | -46.2544 | 2025-09-26 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 247075e6-d7b2-33a9-b12b-1ac5c0192513 | -7.2206 | -46.6084 | 2025-09-26 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d06b98a5-90a0-3036-9ab3-dc58a930ecf8 | -10.9377 | -44.2832 | 2025-09-26 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 39bc0d60-4dfc-3571-9b8f-0fe68d055208 | -10.4129 | -46.142 | 2025-09-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b779e257-0629-3a91-a576-027a5e7aaa59 | -10.1217 | -45.3148 | 2025-09-26 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ee3b6f2a-17bf-33ca-b8b0-8fdbc46116c8 | -6.9303 | -45.6931 | 2025-09-26 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e30a78aa-a868-343c-bac1-1bda94f4aedf | -11.0635 | -45.8996 | 2025-09-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |


[Clique aqui para ver as próximas entradas](README56.md)
