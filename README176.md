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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5404891-7a81-3fad-bd7a-9c281c75ef0a | -12.6267 | -47.2851 | 2026-09-28 18:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| e80bbfa0-dccf-3fd4-b768-1a56aba67397 | -11.0034 | -54.1396 | 2026-09-28 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| bc589b47-c6d1-3837-858d-743e651efdf5 | -7.6851 | -54.7734 | 2026-09-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 40ce2e25-dea0-3410-9146-0ddb9213e174 | -5.4764 | -45.1035 | 2026-09-28 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 2ba79897-e59d-3207-8d81-7b04fe92c433 | -5.7388 | -45.0172 | 2026-09-28 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| e79c67a1-5a33-3eae-bd90-e9a878905dac | -11.9832 | -57.5867 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 918d5785-395f-3b7e-9a9b-61d6d054a8d7 | -11.1331 | -50.0409 | 2026-09-28 18:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8e14d615-b8e9-32d8-9588-5700c5d97b97 | -7.4974 | -55.0256 | 2026-09-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 0b5a4820-5b79-3aca-b2ff-8edd6dd37548 | -11.6017 | -46.7993 | 2026-09-28 18:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4832dd9a-767a-3955-a9c0-9ac23f09d1fd | -9.2048 | -45.8548 | 2026-09-28 18:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 8fd77bfb-68d6-3841-8e2b-7d8878bd372b | -10.8187 | -57.2192 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 4d47c859-37a6-34b4-84a6-0af1028e7003 | -14.0915 | -46.3096 | 2026-09-28 18:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e2ace0de-ed5c-3969-8d62-6f6e93f278b4 | -12.8061 | -54.0048 | 2026-09-28 18:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 1c11cf25-9320-384c-856a-cd0468371b44 | -10.8191 | -57.1795 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 180.9 |
| fc251356-421d-3e41-8985-46ca3d12d373 | -12.0019 | -57.6051 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 2efc3fc1-86cf-3181-99a5-d59a9b1bcf19 | -10.8379 | -57.1781 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 7f07cf7b-33f7-394d-92c4-4911bec45693 | -8.1871 | -54.7824 | 2026-09-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 9558e05e-2d28-3e30-8f50-f760270634b3 | -7.1993 | -45.0814 | 2026-09-28 18:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2bfa58d3-85c8-3a97-9f37-5d076aee599e | -9.6864 | -58.1258 | 2026-09-28 18:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 07dfaebd-feda-3f53-a6b1-739d8a972a60 | -11.1327 | -50.0624 | 2026-09-28 18:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 18dbbb2d-9176-3adf-948c-eb876d35a5ce | -11.1966 | -44.7805 | 2026-09-28 18:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| e496940b-1f7c-346d-b57c-b6f41f69e2eb | -9.7684 | -44.8312 | 2026-09-28 18:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 44b1c7f9-4428-336c-8d08-4fea2f9d4ca8 | -10.9637 | -43.8821 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 55dba830-081e-33cf-b9c2-c85f3fafa991 | 1.6749 | -55.9422 | 2026-09-28 18:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 05613a01-eee9-3b10-bf71-87fdbafbcb08 | 1.6749 | -55.9225 | 2026-09-28 18:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 861b0b96-8026-3af6-b892-3c5014c75ba9 | -10.0148 | -50.2443 | 2026-09-28 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 189bbdeb-9c28-3d61-9b62-158a40489fa1 | -13.3272 | -43.9285 | 2026-09-28 18:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 43581af9-cff1-32a0-90a5-77cd8575c53e | -11.6784 | -43.5158 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |
| c7bcaeff-961f-37fa-b807-e3b68a5f2f39 | -11.678 | -43.5396 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| a6342633-50b4-388c-89d7-5f3b2324ec45 | -7.6852 | -54.7532 | 2026-09-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| a3bc1909-2073-35e5-83aa-4cd7c165b941 | -11.1771 | -44.8064 | 2026-09-28 18:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 194.9 |
| adc6f8ce-66fd-392b-ad55-4e80132861ab | -11.6209 | -46.7967 | 2026-09-28 18:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 338.0 |
| d78823ec-911d-361e-bbb2-f9fa9dd3f3f5 | -9.0971 | -49.8836 | 2026-09-28 18:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 7ff16aa2-b7ec-33a8-813f-ba046aeb62da | -10.824 | -60.7246 | 2026-09-28 18:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 204.4 |
| a162ff9d-1320-3ab0-8c38-f083ee15bae4 | -11.6404 | -43.4981 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 342.6 |
| 34ae782a-4d82-369c-a4cb-9155572ac468 | -12.9457 | -51.0695 | 2026-09-28 18:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 0c3880b6-a865-3eab-87ec-aca0571447ad | -10.8001 | -57.2007 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 885b2eb9-9d18-38d2-b2f9-1229d17c0670 | -11.5904 | -44.1411 | 2026-09-28 18:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 090b2af1-8e48-378b-9c9e-409efa6fdf86 | -6.6627 | -55.1112 | 2026-09-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f9ca20ae-7cbc-39c3-9019-ec9559e87070 | -20.0991 | -57.2067 | 2026-09-28 18:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6cbcf161-b526-3034-9ec8-90a31460c476 | -12.7677 | -54.0296 | 2026-09-28 18:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| df682934-3004-3c6e-882b-6af838e8e5fa | -12.9461 | -51.0481 | 2026-09-28 18:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ea7066d0-a883-32a9-bade-ca00504f3b39 | -10.9538 | -50.6592 | 2026-09-28 18:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 1818df51-6858-3b9f-b3f1-91b12b01a76c | -10.8189 | -57.1993 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 331.0 |
| 7c4780dc-579b-3f51-b866-5c0d0ba514c9 | -8.9637 | -44.1422 | 2026-09-28 18:50:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 36af37dc-fa6c-37ec-9d0d-cab4d8074139 | -11.6994 | -43.4178 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 55f9d3b0-f9aa-3a0b-8d4e-c976bca8aad4 | -9.0783 | -49.8853 | 2026-09-28 18:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 7f91040c-f0f6-3c7a-80df-9a6fa9fca2ec | -12.702 | -47.3638 | 2026-09-28 18:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 10ed3a6c-3840-3b0b-9b35-7173cd53eca9 | -10.8373 | -61.3988 | 2026-09-28 18:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 359e4444-6696-36e1-9200-64f8cb0f0b3f | -13.3262 | -43.976 | 2026-09-28 18:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| b5dab0b7-3557-3ee6-b786-bf50e197902c | -9.9781 | -50.1626 | 2026-09-28 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 80918178-a3bc-3897-b8ce-145e1a0c7a88 | -11.6592 | -43.5188 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| c6aa576f-a34e-3491-8a13-3e492434e5ae | -10.9154 | -50.7059 | 2026-09-28 18:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 376a0b01-da87-3621-80b4-c9093297e50e | -7.6903 | -44.8761 | 2026-09-28 18:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| ece70335-6522-3c2a-8b8b-41e578b94a18 | -6.3137 | -43.6178 | 2026-09-28 18:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| bbeac5f6-4afb-352a-b9a8-3d7877ee5603 | -10.1098 | -50.1921 | 2026-09-28 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 94a68db1-79ff-34fb-8fa4-3cf2fad08269 | -11.5157 | -47.3926 | 2026-09-28 18:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d1f3eff5-6920-3a0f-9d29-e3281ce8ece0 | -9.1525 | -49.9639 | 2026-09-28 18:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| fff45cdd-7800-3274-b4fa-17388dfab6c0 | -11.8641 | -47.1004 | 2026-09-28 18:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 6ece3e64-f643-3de8-8c1f-2ee8a226f87b | -10.9536 | -50.6805 | 2026-09-28 18:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 8278a7dc-5c81-3afe-bec4-062dbf6ff1e7 | -10.9445 | -43.8849 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 1e6b2bdf-6625-3747-aa5d-ede2091d53b8 | -10.8967 | -50.6866 | 2026-09-28 18:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| e9fb4270-8d53-38fa-a4c3-d0b80a1bbc9f | -14.7295 | -45.5527 | 2026-09-28 18:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 9999d128-9a07-3fac-8b48-73e0acd2d97b | -10.7916 | -48.7377 | 2026-09-28 18:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7c2f86d0-e42a-3da2-b572-dea58e3b93a6 | -9.9396 | -50.2304 | 2026-09-28 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 204.3 |
| b4c20ba5-4c15-3000-9b6f-7134925173af | -9.4535 | -41.8088 | 2026-09-28 18:50:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 84.5 |
| dd8948e8-3579-3952-836e-625c16faced0 | -12.6071 | -51.9595 | 2026-09-28 18:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e7363a54-ccd5-3d9a-928c-4838b32d7876 | -8.2291 | -45.4602 | 2026-09-28 18:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5fedf25e-5435-30db-81b2-a698f3ff0cb1 | -11.1775 | -44.7832 | 2026-09-28 18:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 51174534-ea46-3a3d-975d-b234351b4c44 | -11.1962 | -44.8037 | 2026-09-28 18:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 8938181e-b3f1-3c70-ae0a-18eea4e59e16 | -11.6096 | -44.1382 | 2026-09-28 18:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 3621d7ed-82df-3ae6-b873-d8d0d3d391f4 | -9.9393 | -50.2518 | 2026-09-28 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 207e90ff-2967-363c-9796-da14699fa75c | -12.7868 | -54.0275 | 2026-09-28 18:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 11095dcc-fa16-30c4-98f4-cae64dec2521 | -0.5073 | -49.1326 | 2026-09-28 18:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 11eedb8b-ddc4-30bf-a752-357b11477148 | -12.588 | -51.9617 | 2026-09-28 18:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| eff7d5ec-bf32-36c7-ae54-a090ed6b6ced | -8.2804 | -54.7562 | 2026-09-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 04d62c2d-8a98-3e37-a868-1805e9fd6f3a | -5.7384 | -45.0626 | 2026-09-28 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 027b00f8-66c0-367d-b6c7-5b572e4c7df2 | -11.6213 | -46.7742 | 2026-09-28 18:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 334.7 |
| b2222c7f-65a8-334b-8947-ab4f829dbc02 | -10.8238 | -60.744 | 2026-09-28 18:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 257.7 |
| a9ce2228-6f37-3571-b4ba-0394f587decb | -10.8052 | -60.7257 | 2026-09-28 18:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 430541bf-4b7a-3e0a-b488-3b97d33c1eed | -11.7178 | -43.4623 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| ceda1dca-9e44-365b-86ad-6035b10cdcfa | -7.7037 | -54.7722 | 2026-09-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| af574062-90f8-3c29-9946-34de073979f4 | -12.2301 | -50.4288 | 2026-09-28 18:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8db5ff04-2884-34fc-b054-b232d25f2702 | -10.8184 | -61.4191 | 2026-09-28 18:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 810ba5f1-5658-30c4-b461-bd2fc8aa21d4 | 1.6566 | -55.9227 | 2026-09-28 18:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ac7323b7-463e-3645-84d6-140ccfa45836 | -13.9015 | -53.6548 | 2026-09-28 18:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| a161bb82-c38d-3dee-ab3a-616e8f18f85d | -6.314 | -43.5946 | 2026-09-28 18:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| da78d791-7fa5-31fc-a642-49a279902206 | -9.1337 | -49.9656 | 2026-09-28 18:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| e86bb065-d1d3-329b-81e5-1f3f2ee8a9ca | -13.6866 | -56.6131 | 2026-09-28 18:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 190.7 |
| feb682f1-5fba-34bb-bf07-a8bd6f2cabc6 | -10.9254 | -43.8876 | 2026-09-28 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| eb552bc6-5993-39d5-b0d5-da9af6861af2 | -12.1202 | -57.1767 | 2026-09-28 18:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 7d2a5978-13dc-3566-a82f-807563ead7f1 | -9.0786 | -49.8639 | 2026-09-28 19:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| f11f8c73-b008-3b94-9006-4488026b1ca8 | -0.5073 | -49.1326 | 2026-09-28 19:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 45a4ef29-1ae1-31c7-aab5-1c3079e2eb5e | -11.1514 | -50.0818 | 2026-09-28 19:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 3743744d-79f8-342c-9c7b-7b70234e82f4 | -11.2945 | -43.551 | 2026-09-28 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 521.8 |
| 4af77c19-531e-31ff-aeff-1b051a072597 | -12.6828 | -47.3666 | 2026-09-28 19:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5070c364-894b-3cbb-b6b0-e35b29848e8a | -18.6834 | -48.6234 | 2026-09-28 19:00:00 | GOES-19 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 142.8 |
| d822207f-7579-3c28-a05e-4228dd562c4d | -12.1202 | -57.1767 | 2026-09-28 19:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| f6af6dd0-ccb4-31a0-a7b1-53b397f5e23b | -11.0796 | -46.079 | 2026-09-28 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 3aec7770-7f7c-3ff1-8853-2e07d116fab5 | -12.9461 | -51.0481 | 2026-09-28 19:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |


[Clique aqui para ver as próximas entradas](README177.md)
