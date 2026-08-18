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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c26ec2-a84c-3249-b169-e3d28d82616b | -8.20428 | -55.03143 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a20bf072-350e-32c1-8a8d-c76c353b06a3 | -9.21387 | -50.09469 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 461c2433-4e4b-38f1-82d3-18871a72d3cb | -6.74764 | -59.16501 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e484d6da-a203-31d2-9415-bcd428bcca11 | -9.07441 | -50.84039 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1c2dd77e-d080-3c28-ae1e-d1a6504eb5ff | -7.63873 | -55.62505 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d2b2a86-9d75-35e1-b0ee-514eed22d2f0 | -9.05069 | -45.82399 | 2026-08-18 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34714b3e-b058-33df-b176-ff9bc0a47b8f | -7.40069 | -46.48283 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc62fdbe-d6f5-3a90-9d55-4aba591829d3 | -7.63912 | -55.62846 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c088d8c-20ed-35fc-bfe7-2e7816298081 | -8.55252 | -55.31583 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87eaa226-a6d0-333e-b617-e6c6922151b6 | -8.33222 | -46.47385 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70f1a1df-14a2-38e2-b363-84e877ad341b | -9.07297 | -50.82605 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70dd465c-fa62-3aef-8876-fa64411c1c85 | -6.67583 | -56.16057 | 2026-08-18 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1518562b-45a0-36cf-9abd-fe9a28237d9b | -4.53345 | -42.93062 | 2026-08-18 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63bb9af0-1fe7-3378-9fc9-cefc60cd677f | -6.03981 | -57.96539 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b53b8f0d-9aac-3b93-b6b3-312329acfd5b | -3.68156 | -47.64992 | 2026-08-18 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f408507a-d7fa-3de0-8fe9-d72c8ec47a8a | -8.33112 | -46.48082 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f190a9bd-6f48-32a0-a0e0-5bf3a0a1d9f5 | -9.49031 | -51.60465 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27550aa1-583b-3415-a77c-0a55d545bda5 | -8.58124 | -54.70957 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 950252c0-63b0-31c4-9d9f-66c1496f5460 | -8.57544 | -54.71394 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9eda1d65-1078-30e1-a83a-ab0abfb3c319 | -7.63175 | -45.74524 | 2026-08-18 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f369f060-3f8e-3563-8f82-eefeffb3d167 | -8.57833 | -54.72567 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 26d92b49-2dc6-3536-8835-b582136a45b6 | -8.56141 | -54.69202 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d5a76b0-b9d4-3576-811e-9562c197545b | -8.5725 | -54.73014 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d70926f9-5ab1-3672-98f7-acba3c7eeb4a | -9.70823 | -48.37555 | 2026-08-18 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 627eebbd-ae16-3dc6-8a9c-a1a19e29cf10 | -3.26525 | -49.5241 | 2026-08-18 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4d60c08-18c9-34e4-9863-f61ffff06318 | -6.74065 | -59.14946 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41b35597-e1c5-39e8-a9cb-2fc9164ad979 | -5.74055 | -43.27272 | 2026-08-18 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 443e95b4-b4ad-3d52-9b85-f8adc5638ce0 | -8.58514 | -54.71577 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 06e2bbf9-a776-3c36-a7c1-106179ac3bcb | -6.3052 | -47.89391 | 2026-08-18 04:38:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f47c92d1-0f76-3d1e-94a9-b265ea2b54d0 | -7.38601 | -46.81143 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c8b0fc9-9953-3c49-9848-46edb58b6bb7 | -9.76478 | -46.72688 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9093776e-3dcf-31ed-89fa-dca815020228 | -9.49419 | -51.6054 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 870c2405-a669-32bd-a08f-71fac365f8b2 | -8.74395 | -45.32811 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f133050-118e-3693-aab0-da0b9e757829 | -8.63557 | -54.71383 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d07aad6e-7517-3a53-b19d-ae4ea53ea69f | -4.12704 | -49.44963 | 2026-08-18 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82a186a3-ae26-36e6-b6a9-ab48922b4fb9 | -7.61703 | -55.63085 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71c947c1-f6e6-39e5-9991-e214f8350d0e | -8.0852 | -44.3549 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3d03eff-fb69-3240-bae3-7b5e8496153e | -2.83289 | -49.14152 | 2026-08-18 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48331c13-e7ce-30d8-8d26-e847383d0929 | -8.55141 | -47.3774 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5307bbff-879e-3bb8-bcf2-fc4357c6daa7 | -7.12246 | -47.54765 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb0dac45-317d-3377-8fbe-be79eee3a8d6 | -9.46847 | -51.66203 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad9f514a-c294-37fa-8b27-03f70525ed0b | -8.36144 | -46.37469 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a69f540-12fb-34f7-81a8-44fdbc2bff49 | -5.14456 | -56.2774 | 2026-08-18 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0201f27-b809-3ba4-9685-7aa174151aad | -6.75758 | -59.16949 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26b7f1b6-8074-31e8-9641-5b2af946b1ca | -2.70781 | -54.22423 | 2026-08-18 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a08f69-f3f5-37c9-baef-848c6d1d270e | -8.56533 | -54.69826 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7f90fc9-0c5b-3435-b5f9-50f4cf208f98 | -9.46453 | -51.66156 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e007e91a-978a-3691-b766-565b1339d72d | -2.70677 | -54.2271 | 2026-08-18 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41968e47-a67c-3d56-a348-4435ff431429 | -6.18011 | -47.78132 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d20d790-25e8-3c9b-b76e-6d254a0de71e | -6.75959 | -59.15858 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 003b876c-1728-305c-8f15-ab3c0e8554db | -6.26499 | -43.27841 | 2026-08-18 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ef76f0ba-9429-3f2e-8e65-009af944d008 | -9.46662 | -51.62588 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df8a806c-5baa-3ed5-bcce-422a6ede8579 | -3.50218 | -48.03456 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e96000a3-837e-3dc4-b705-b247aeb2174e | -8.31729 | -46.4822 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f4c775b-f3d0-3ba7-b27d-022766ecdcdc | -8.18217 | -55.01479 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8744fe4-2978-3329-84d5-23160b45e291 | -7.81658 | -44.60163 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4814940-e1b4-3759-9ebb-dfd2eba54087 | -4.96995 | -42.21369 | 2026-08-18 04:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f7cb0e0c-49c6-3671-ad22-7c835a6ba329 | -3.68217 | -47.64621 | 2026-08-18 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c61c8cdd-7165-315d-bb53-51148b49f7fa | -7.17483 | -43.42097 | 2026-08-18 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e7f989a-473f-3c5a-bcae-43ecf17c5792 | -7.37916 | -55.48587 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3447006f-6d2a-387e-95c8-80f888762c17 | -7.53857 | -46.61541 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c67352de-763f-33d1-8719-0c1c1983b4f0 | -9.46447 | -51.61503 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c04d0feb-9c5e-39b0-8b14-e49e1b9cae08 | -7.01774 | -45.90496 | 2026-08-18 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e4632e1-6a8f-3d7a-88a0-58e8b31fa406 | -8.37138 | -46.35479 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6cd7734-5ef5-36bc-bfed-5b9a341a1931 | -8.5941 | -47.36638 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c4d2e71-b589-3aae-8866-0371536de210 | -8.20634 | -55.01999 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d967c488-c6c6-3a9f-a738-ab5e53e93101 | -6.74867 | -59.18048 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0f9e361d-6ab3-3cba-8513-397c52a429d8 | -8.55915 | -47.39301 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 783619f8-a60b-3ebf-bb56-f95bfeed88e0 | -6.53517 | -43.11874 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e474761-60c3-347a-a9f9-4ec5f31eead4 | -4.48663 | -42.55785 | 2026-08-18 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87e5dd5f-5956-3f35-a1fe-b3aab0e5f1eb | -8.36531 | -46.37173 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7385aaba-4ea6-33b5-8fd4-c5668998f138 | -6.58407 | -42.23184 | 2026-08-18 04:38:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5d2e1275-657f-3c87-aa8b-615cff8d4b5d | -8.56865 | -54.72373 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| b6abd570-ee79-336b-ae62-21ab2414b1f5 | -9.07373 | -50.82152 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf633378-9c2b-304b-9bec-4325b851a3e6 | -5.48596 | -45.04262 | 2026-08-18 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 741d757c-5c01-3e95-a7cc-8f0c10771deb | -4.53449 | -42.9293 | 2026-08-18 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20913502-c2fc-3b02-8cc5-7991ef092bb8 | -8.58998 | -54.71672 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 016250da-b00f-30ad-af91-484cf4088e7c | -8.32393 | -46.48325 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a903a9bf-d13f-3fac-9e85-96c82d5e3def | -8.33664 | -46.4674 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fee4ed84-50e9-3402-96ff-ec31a5f02d5b | -9.76367 | -46.7339 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb85455d-e1ef-329b-abdb-72e61ec77887 | -8.57736 | -54.70334 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 50ebbf9a-558e-31c1-a4d8-10d6dbf31e4d | -6.17543 | -47.81022 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83c365e6-794c-33f1-a4e5-86321dc360da | -8.57543 | -54.7417 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 997ac7ae-7f02-3460-8adb-b0c490b475a1 | -7.39738 | -46.48231 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1939a5f-6298-3c91-8f9b-51673a5a3512 | -6.40003 | -54.94179 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcd37c56-a9a2-369c-90e6-2a3aa9fcf949 | -6.84934 | -58.98946 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88aaea0f-550b-3822-ba3b-6943947ac96e | -9.403 | -48.25181 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9f3d408-474e-3054-a859-8a004728b10b | -6.13875 | -57.73971 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0263302c-eed5-3fbc-8862-c627d72fe96f | -9.4052 | -48.25957 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d4b6e4-20c6-3228-b675-6fa43a20bcdf | -9.89537 | -47.73515 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 887cc4e1-912a-3a7c-9dde-377bd72cc898 | -8.36973 | -46.3653 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90ed08ff-eead-3371-9db4-f676fad94f48 | -4.96997 | -42.21136 | 2026-08-18 04:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 91658cb2-6a7f-383c-a97f-27c124c95055 | -7.37972 | -55.48271 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f372a2b-74cc-3c2b-b60d-d6fbee414815 | -7.53377 | -55.58199 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9204255-ef87-3346-9824-8c68ad7846ec | -6.7452 | -59.16204 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0e5f6357-2bcc-3689-80c3-abac0eb9c383 | -6.69915 | -58.9433 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c44b8fd2-7ccf-31cf-aef3-9bc7c4beb00d | -8.56048 | -54.69738 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8ad218f6-a48f-3f6e-993a-00fe6bd97611 | -8.63653 | -54.70843 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b881f50c-770a-332b-bf31-bdd5d0139821 | -9.4103 | -48.2493 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15d2088c-f94b-3a48-ada4-f8646451f105 | -8.58991 | -54.6893 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README22.md)
