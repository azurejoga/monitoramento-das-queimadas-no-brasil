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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fea7bdde-4ccb-329e-bca9-e3ed5a0606fe | -8.2788 | -54.9376 | 2026-09-01 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b6d1bc86-7bf8-3a7c-a7c6-b8f49f48eeb2 | -8.7819 | -46.4399 | 2026-09-01 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7c8d9aa6-8464-34dd-bfd5-ec2eba9dc150 | -14.6538 | -53.5433 | 2026-09-01 12:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 14812461-90c9-3e29-8b72-38be0e4fcc3e | -11.2295 | -51.2667 | 2026-09-01 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d82208d6-17f8-3fbf-9bd0-ccb1c69def39 | -10.1542 | -45.6755 | 2026-09-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 7ffeccb2-538a-313f-b18e-eee2a4839f6d | -11.51524 | -62.49531 | 2026-09-01 12:51:00 | TERRA_M-T | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2788d669-9e92-3598-86cc-b584267339bd | -12.11033 | -54.1646 | 2026-09-01 12:51:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5f582799-eda9-3736-aabe-2d514559c04b | -10.95458 | -61.66417 | 2026-09-01 12:51:00 | TERRA_M-T | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 285e87e1-a61b-3252-8a8d-e178f033b612 | -10.9504 | -61.65745 | 2026-09-01 12:51:00 | TERRA_M-T | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b30ee92a-2e87-3e54-bae5-43f0225ac29c | -15.87422 | -56.46947 | 2026-09-01 12:51:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 81ec3a77-47e8-3608-836d-16112e220217 | -10.95595 | -61.65385 | 2026-09-01 12:51:00 | TERRA_M-T | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6a87a67-259e-3018-a304-a06990c96437 | -14.6732 | -53.5408 | 2026-09-01 13:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 2fbd81d3-f4fc-327f-94b8-dee6980123ab | -9.9912 | -46.4409 | 2026-09-01 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 211.1 |
| a85c2c37-bb8e-343a-86ba-74b522e18435 | -11.6914 | -47.1461 | 2026-09-01 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 37e831e8-98ae-34a0-8560-95d76866c48c | -7.571 | -60.4643 | 2026-09-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ae59328a-db35-3cec-b3a7-f18a7279027a | -9.4719 | -57.0354 | 2026-09-01 13:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d7db695c-4c48-33e2-ab18-04594d6910c6 | -6.9553 | -55.6151 | 2026-09-01 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7636379a-fcba-3236-8d02-b32743e3cf68 | -10.1542 | -45.6755 | 2026-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 96204a48-8f1b-34c6-a93c-9ddaea0b982e | -8.279 | -54.9174 | 2026-09-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| e4e9607d-7eeb-3151-970a-7d7084c26ab0 | -12.8839 | -45.8412 | 2026-09-01 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c990c115-826e-3edb-a774-be9ab9481064 | -14.6538 | -53.5433 | 2026-09-01 13:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| e566727c-217c-3cab-b39b-d2a62d0ef9cf | -11.2317 | -46.1041 | 2026-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| bc3b8b77-c895-3802-90e4-c9c3598a6402 | -10.8624 | -45.3789 | 2026-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| e88b7be7-7978-36d9-a241-a9b595429a86 | -11.8056 | -46.0476 | 2026-09-01 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 7df889f3-ada7-3e5b-92b1-16e653a49f93 | -15.4235 | -52.6836 | 2026-09-01 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 7d2c26bc-9c09-3bd1-82bf-c504e92788f4 | -3.8604 | -44.0585 | 2026-09-01 13:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 9211d4d5-ca5f-37f1-ba34-07352f67952b | -8.7817 | -46.4623 | 2026-09-01 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a29c3628-5f92-349b-ab44-9c239f478951 | -8.1296 | -54.9672 | 2026-09-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1fb54c58-c057-3b9a-9a35-43160194985b | -11.2295 | -51.2667 | 2026-09-01 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 3540ca43-240d-31b5-8381-093e2135beb0 | -7.3487 | -60.5883 | 2026-09-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e2cb09e8-a7eb-34f1-91a5-e8fcd84371bb | -10.1538 | -45.6982 | 2026-09-01 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 9a47aece-aa59-33eb-9e2c-6a3d8278eb30 | -11.5287 | -45.4703 | 2026-09-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| bd012c50-8dba-340f-b718-71192d37f250 | -6.1659 | -57.7403 | 2026-09-01 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 18ffa8c6-f474-306e-a8fd-0cf27ad9e3b9 | -11.5479 | -45.4676 | 2026-09-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 469.6 |
| c16f1c0c-e293-3833-8061-f40a094351e9 | -8.2788 | -54.9376 | 2026-09-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 741300b1-8e77-3dd0-81bd-edfee392b34b | -10.0101 | -46.4386 | 2026-09-01 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 367bd783-576d-3faa-9a02-6e8a7a4dcfb1 | -10.8818 | -45.3534 | 2026-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 312.5 |
| e2c41770-1fa8-3e39-946c-78f12877d668 | -8.8816 | -46.0253 | 2026-09-01 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2d4c9c21-c665-34fb-b3d3-de3d29eb445f | -8.7631 | -46.4418 | 2026-09-01 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ac55ed7f-b11a-3b17-94b8-d7de7550717f | -7.8904 | -47.0821 | 2026-09-01 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| bbd6fbf5-934a-32df-81bf-443c157c7639 | -8.7819 | -46.4399 | 2026-09-01 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6d31752e-55c7-3b44-b283-50b03e773092 | -8.7628 | -46.4642 | 2026-09-01 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 186c5bd8-092f-31d3-b970-d113a7d70ab8 | -10.8627 | -45.356 | 2026-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 372.1 |
| 595062fc-e047-3bf1-a344-3c48f2e1af4e | -17.1146 | -46.8556 | 2026-09-01 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 47963e93-ce41-3dce-baa9-f94065718f64 | -10.036 | -44.7056 | 2026-09-01 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1109665b-054d-3de9-a20a-aa426a3b3d41 | -10.696 | -46.2646 | 2026-09-01 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d0fc89f0-cf9f-3e41-9716-008c2fb8cc0e | -12.9032 | -45.8382 | 2026-09-01 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 9728282d-2560-393b-9503-c293032fec28 | -3.879 | -44.0576 | 2026-09-01 13:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 0e0c18e1-9f8e-342e-a709-6b8cba879131 | -10.8631 | -45.333 | 2026-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 64cf078c-a7a4-30ba-8c8c-4e6040022092 | -10.7856 | -50.5066 | 2026-09-01 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| ab63058d-d263-3823-ab90-c3b881bd9185 | -14.6535 | -53.5642 | 2026-09-01 13:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| bae7c1e2-1b65-3af6-9bc7-4c1744450316 | -15.4429 | -52.681 | 2026-09-01 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 258.8 |
| 0849898a-e813-3913-8497-f1e62057bc7f | -6.9552 | -55.635 | 2026-09-01 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 1d6a41f7-e48d-3adb-a858-74985cfe7ad9 | -11.5475 | -45.4906 | 2026-09-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c976b577-2a25-34da-977e-fd77c66c1355 | -14.6732 | -53.5408 | 2026-09-01 13:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| e0fdffa4-d291-3540-8463-ec6a2a900634 | -10.8818 | -45.3534 | 2026-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 463.9 |
| bb148726-e102-39e4-aa21-30a6a0506b37 | -11.6914 | -47.1461 | 2026-09-01 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 52d1f091-21bc-3196-b434-f79962353e78 | -3.8603 | -44.0815 | 2026-09-01 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a97d603f-766c-3af0-a130-c6c913d779a2 | -8.7819 | -46.4399 | 2026-09-01 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 0b0a4936-4161-3639-85f3-38a4f43fa8d3 | -8.4235 | -44.9849 | 2026-09-01 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4324e437-a6c9-3ae0-a9b2-b352bbcde0c9 | -8.8816 | -46.0253 | 2026-09-01 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1384da39-0fd2-3eba-8a5e-c4be6defaa2e | -7.3488 | -60.5691 | 2026-09-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fc5cca6b-afde-3562-9ff4-1e244b467e73 | -11.8056 | -46.0476 | 2026-09-01 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 257.7 |
| 7af844b1-9398-395a-9b26-cfe50d7580ac | -8.7817 | -46.4623 | 2026-09-01 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 6ac01c13-e98f-3da0-822d-2f29908affa5 | -9.9912 | -46.4409 | 2026-09-01 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 057b2aae-acf0-34a4-a027-c11004f2134b | -8.279 | -54.9174 | 2026-09-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| aee9d057-4978-3e60-8550-51e9b8a31640 | -11.5479 | -45.4676 | 2026-09-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 299.1 |
| 4026f746-4c14-3615-beef-081399b04efa | -8.2788 | -54.9376 | 2026-09-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e37a43ac-45e5-31cd-bb79-e222653d6be1 | -6.9552 | -55.635 | 2026-09-01 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| ce5e6ef6-2129-3f26-a67f-77cc631ab0ae | -15.4235 | -52.6836 | 2026-09-01 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| de9ee936-98fb-38e8-bedf-bfebe0c19b60 | -10.1542 | -45.6755 | 2026-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| fba299ba-d6e6-3c6d-a029-86c952690515 | -11.5287 | -45.4703 | 2026-09-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c6b9809b-562b-317f-a147-d3b0c78b842d | -7.3487 | -60.5883 | 2026-09-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 7d60ada4-9bf2-3676-a3d2-f2c20bdea2aa | -11.2317 | -46.1041 | 2026-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| def89b66-a8d4-3bfa-912c-641e732a476f | -6.1659 | -57.7403 | 2026-09-01 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 314d9b45-1db1-3cf7-8236-5e41f70dca82 | -15.4429 | -52.681 | 2026-09-01 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 673d43f1-2335-31d2-bd22-039238276449 | -10.7856 | -50.5066 | 2026-09-01 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 036c2045-647d-347c-93a0-10da5c3bb023 | -12.9032 | -45.8382 | 2026-09-01 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 5ea6026c-adb7-32b3-9700-26d87a6f53d5 | -3.879 | -44.0576 | 2026-09-01 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 9cc252a8-4bb8-392d-bfd6-8aabc15704d3 | -3.8605 | -44.0355 | 2026-09-01 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 96f09a93-4683-390a-a488-92737b6ec4e4 | -8.1296 | -54.9672 | 2026-09-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 0d338fc0-45f7-3474-a06d-608981bffa78 | -3.8604 | -44.0585 | 2026-09-01 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 265.3 |
| 9b7c5938-2242-30ac-8a5e-7ca34f437ca2 | -8.7628 | -46.4642 | 2026-09-01 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e4d3e98f-6b47-3fec-a284-ce6328400a42 | -10.1538 | -45.6982 | 2026-09-01 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4c54d40a-0cd2-37a8-8537-50e66600b171 | -6.9553 | -55.6151 | 2026-09-01 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1deb7950-129b-31b0-bdd5-1c05a702d96f | -8.2602 | -54.9388 | 2026-09-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3adcd284-afd8-3812-8037-848ef1713147 | -10.8627 | -45.356 | 2026-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 1ae90ff6-ab92-30bd-b361-4845a5c02cd7 | -7.571 | -60.4643 | 2026-09-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 757f59de-86c0-3229-be71-4d68c8a7c98e | -10.8624 | -45.3789 | 2026-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 939204b0-f6d8-302c-9419-20c386853f7c | -11.2295 | -51.2667 | 2026-09-01 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| be25dd40-5207-3931-8f7f-8a4413298499 | -6.8036 | -59.0921 | 2026-09-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1e0439c3-05d1-3cff-b12d-6a906419aaef | -17.1146 | -46.8556 | 2026-09-01 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.5 |
| e0a3a3ee-a496-3175-a2c0-c84e629cdd0f | -9.9931 | -46.3057 | 2026-09-01 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d8e7844b-7d51-3dae-9270-3771f0a20b64 | -7.8904 | -47.0821 | 2026-09-01 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8921c712-fdb7-3787-95dd-2ec99dee1935 | -14.6538 | -53.5433 | 2026-09-01 13:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 5d877e21-764b-36bb-a761-883c416260ca | -10.0101 | -46.4386 | 2026-09-01 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 233dbae2-4463-3be8-aff5-d9354010e1af | -10.88 | -45.39 | 2026-09-01 13:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3a30570-06c0-370b-9eb0-d2a791d11dff | -10.8046 | -50.5046 | 2026-09-01 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a4f2c7df-5e4f-3ee6-a428-7790a5fb4ecf | -8.4235 | -44.9849 | 2026-09-01 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 07e1c3a7-1fa4-32c7-99e6-c1fbd802a261 | -3.8604 | -44.0585 | 2026-09-01 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 234.9 |


[Clique aqui para ver as próximas entradas](README95.md)
