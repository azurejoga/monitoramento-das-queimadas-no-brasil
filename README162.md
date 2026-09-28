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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d435c35-7400-38ce-9884-ea8231529143 | -3.67198 | -42.6685 | 2026-09-28 17:09:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5399071d-4783-38d7-a611-437c1368f8c6 | -9.28334 | -46.57512 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16d44e79-c93c-3005-9623-02d908bf8fe3 | -11.01341 | -54.14863 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ae618b04-9c0b-3bdd-9288-b02426de6c63 | -8.6702 | -63.98429 | 2026-09-28 17:09:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 4ad8b069-20a2-316e-9df0-c06d2719c9ef | -11.20487 | -44.79591 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e3bb3d5f-b1b9-3546-99a5-c42032f9bee5 | -9.18897 | -46.95564 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 261331b2-1c69-330c-a977-38114bbbce3f | -7.23672 | -44.8581 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3739917a-d36e-36d0-9715-a0c2477542e9 | -10.00859 | -50.11192 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c687e03e-5830-3510-b81f-71c7b3fa1eaa | -10.81885 | -57.22978 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9742749c-db94-3adf-8d32-46d53356ae99 | -9.85478 | -44.94683 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 63b0b96c-dc8f-3634-adcd-389667e63426 | -10.26264 | -44.62834 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 230.5 |
| aad15628-4b55-3f94-8596-c98c74d084ee | -12.21797 | -53.23127 | 2026-09-28 17:09:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cf827c26-8a4c-3e22-8010-a1a6c75030e3 | -7.90479 | -45.45061 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 47d4fecd-2b4d-3f3f-8d23-18420c04fc89 | -9.77166 | -44.86724 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96eaf4fc-a407-3d64-99d2-e0d0f3660a91 | -10.84336 | -61.42238 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f854dd5c-08f0-3ea0-b009-075755b146fc | -7.49017 | -46.9341 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0d0cca4a-b3a6-34e7-992e-77104fe1abd8 | -6.15985 | -47.13235 | 2026-09-28 17:09:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8ea97e5c-7f2c-3794-9e35-6cbf0f6a8d16 | -9.40484 | -46.38965 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9b4269fb-5f16-3058-b142-2ee4e82de317 | -10.80415 | -57.20321 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 80700714-ff0e-30ca-b85b-cab455adf8c4 | -7.4954 | -54.97074 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4e777413-3db2-3317-9f81-20effe423e08 | -8.67563 | -45.34546 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 73ab8250-5a57-305f-8c2e-08a7b7df5ecd | -9.64516 | -45.54509 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ca0c7b4-a5cc-313a-aae2-125789f10ebb | -8.83084 | -46.58305 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4f442b9b-f36a-3b1e-8c95-037ab6530454 | -12.39424 | -50.24596 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e1ce5c51-435c-39ab-85ac-cae5e7a7b65c | -10.41296 | -53.82529 | 2026-09-28 17:09:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| eb543e1a-5081-359b-a031-d6b86871861b | -9.1374 | -56.5607 | 2026-09-28 17:09:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 19126c4d-abda-395e-ab3d-877ec7cf5a47 | -11.11727 | -47.58412 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 696b7209-16a9-3e6e-b49a-22797e4ad8ef | -12.16405 | -50.41153 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 94f3cb64-375a-30dd-8803-f6dc7545c58a | -9.77026 | -44.82961 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8619078b-3cc9-3e75-bfcd-f7c8f9e14681 | -5.20929 | -48.49986 | 2026-09-28 17:09:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab8e8a90-6bd7-3354-bed3-e2dd72c321e0 | -9.78844 | -48.21996 | 2026-09-28 17:09:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| fcab3dec-ac2b-3d1b-8966-4ead452d3946 | -6.66846 | -45.62119 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0fb87234-1c54-3256-a80d-4fa699f8799c | -8.98434 | -44.16206 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ee697dc7-df64-3510-982c-98d419207c4a | -6.30444 | -56.03354 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 461cb2e5-562e-32f8-a5a5-664343febd14 | -7.48932 | -54.97523 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 317f5321-a1b1-384e-ba4c-a45201ac4853 | -10.92347 | -50.65815 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8f8b3ad4-074f-3d31-b09e-38c594241ecf | -8.99019 | -45.51144 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02b2664c-3954-36e8-8ce3-9a41d34a2a12 | -9.96124 | -46.09631 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f94c3f54-9957-39dd-8432-5aac8cbe6c26 | -6.46368 | -45.91033 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7067dc1d-8136-3942-a64d-b420a4c90ce4 | -9.33209 | -45.36193 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 4b215f9f-8baf-3446-891e-131bb08138c6 | -11.85438 | -50.8816 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 19d55c1c-d2b4-364e-8860-abe7df5a2692 | -8.70263 | -66.62182 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5233922-45e2-3f7d-876b-e52f83df0bf5 | -6.3775 | -55.13067 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 88073760-2bdd-34da-9d8e-52ad18a75d4b | -9.96916 | -50.13906 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 979134d9-c259-3921-932b-c41aef7ecaa4 | -11.02838 | -49.70456 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 963ae25e-1b2d-3816-ae2c-e66be53fe02b | -8.34522 | -45.46715 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ad1d01a-70e6-3487-b048-2f2341cb1068 | -9.15705 | -43.08191 | 2026-09-28 17:09:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| a0b60df3-1c99-330c-b3d3-8004d6da4faf | -8.36714 | -45.40029 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| abc3928d-bacf-38d2-9be2-56fe3bba1459 | -6.1418 | -52.7519 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 65c757a8-7b70-3c13-8751-d40dc38ecbe7 | -7.31611 | -44.60024 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4640e143-a3aa-3151-bfa1-c4f25d4595ac | -9.07514 | -51.53854 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| de731ada-f837-399f-bc1e-dfe9e4017ec3 | -11.84272 | -50.90126 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ca49e146-37f6-3a31-bd43-790ed0526fdf | -8.93212 | -61.49054 | 2026-09-28 17:09:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1f780359-f982-30f6-a7d1-26014ae36dba | -11.2217 | -44.7961 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d5633d79-4193-3625-a2f8-e9ef9692b471 | -10.21946 | -49.99928 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 76491768-d864-332d-a6ef-a10f8b2110db | -9.44822 | -41.80957 | 2026-09-28 17:09:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| a48005ce-b4b0-30d5-aa49-799da8a9bbd1 | -12.3161 | -50.15298 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0767a4a5-8fa8-322a-8ae0-d0843fbfbb36 | -9.34337 | -46.53486 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8fc6ee7-f21f-3104-bdd1-4d5563bf401d | -9.50356 | -46.59468 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ace4e79a-89ea-3d40-867e-7bb1499a9a20 | -7.43983 | -55.63117 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| ebb12aaa-9fa2-3253-81c3-42d7c196e645 | -8.85399 | -46.59711 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 56acf61f-428d-3de2-8e84-1dc6a201f79b | -8.98306 | -44.16029 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| dc44056b-d909-3985-a133-e1dfe02eeb82 | -10.92729 | -50.70378 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 061012ca-9ccb-3e94-a927-62d6cbd09580 | -7.99356 | -43.25309 | 2026-09-28 17:09:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 064ff83f-3ceb-3e83-9e17-154646416ea6 | -9.76612 | -44.83799 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3e8d710f-07f5-3e8b-aad3-b8faa1571121 | -9.02678 | -50.8021 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f9aff50f-4195-3c1b-a7bd-17b80f3f066e | -9.50637 | -45.76529 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3487990c-1f58-3912-893f-43133002a82f | -11.53402 | -47.16191 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 697bb494-3b01-322d-8928-97a0585ba6d9 | -9.93597 | -50.23386 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ed032073-f2d3-3009-9ba5-a7e5027c65e2 | -12.30973 | -50.25354 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2d69ea62-fd2e-3780-9911-704bb2b95af8 | -7.43717 | -55.63939 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1f2a1205-4eca-39cc-bc25-61c338806cdf | -10.94505 | -50.673 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f764d56-9e0a-304e-bf90-e86df2f9471f | -7.88918 | -54.72289 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d4693d1e-a5fd-31c7-bb06-e257ca7ed2c1 | -8.97395 | -44.14433 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4331aaa6-121f-3239-8644-bbcab8367d03 | -7.82255 | -55.13071 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| dbeaa1f4-d2ae-331a-8da0-82477d68ad65 | -8.72447 | -44.89531 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1dc84b60-7401-3dcf-9544-d79f77f4cb1d | -11.47621 | -49.75619 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 551bacad-343c-3a3f-ae54-7c16071b72e1 | -12.17153 | -50.42107 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5436f72f-73f7-3f68-bbe3-68beb1808efa | -11.13398 | -48.33273 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0b985a23-44ae-391d-93dd-33cf7f835219 | -6.74707 | -51.44934 | 2026-09-28 17:09:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 4c795b6a-a65e-3679-908d-7925f9dbf760 | -10.97035 | -49.67264 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c217e387-5553-364a-aebb-33d634ce1917 | -6.72286 | -47.7925 | 2026-09-28 17:09:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c8aba194-b2af-3948-8ad6-2f5620c31715 | -6.23797 | -49.36519 | 2026-09-28 17:09:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 72fcff41-b925-3887-b71d-0454a2bcd445 | -10.2715 | -44.62068 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| d3363e32-4abd-32be-bad3-fc51db6ee1c7 | -5.11661 | -45.79834 | 2026-09-28 17:09:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 382efb93-c365-3a31-8722-92a57d472c4b | -12.79426 | -54.01422 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| cd9f580a-ad17-3f72-9e6c-b51434e87092 | -10.82826 | -57.16794 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 49944d7b-128d-33b1-947b-feda7a85a963 | -12.16106 | -50.40436 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c807434d-b4b3-3eb9-a2ec-aeec63b890ff | -9.48402 | -66.77892 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 642cfdd5-7c0a-356b-a88c-22fa54ce01a4 | -11.71919 | -59.35365 | 2026-09-28 17:09:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 715c437c-a29b-3361-907f-6a615d039de4 | -9.1475 | -49.96807 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3178f4ac-2e83-32af-adfd-4f72150b8c8e | -11.84719 | -50.8607 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4a7b9a8b-a8be-3804-a426-f5eb571cc48a | -12.07243 | -48.54826 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| fedcdab8-949e-355d-8838-61c86f278323 | -9.73032 | -53.87423 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 250b2c51-715e-3c8b-ae84-dec2f4c9b9d2 | -12.16481 | -50.39284 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 37730d6f-f0cf-30c5-a04e-16fef4ba9019 | -10.11223 | -43.94512 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 04c6641f-d978-36e2-888d-605956bce8c6 | -7.0248 | -44.64822 | 2026-09-28 17:09:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 807c2040-0405-360e-a15a-27b94f52019d | -10.45866 | -47.48775 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ef126613-0273-31b7-a6e2-2dc85a3e1329 | -4.85246 | -45.27369 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 28927970-c1ef-31d8-aaca-76a6049ccd59 | -8.0007 | -44.97466 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README163.md)
