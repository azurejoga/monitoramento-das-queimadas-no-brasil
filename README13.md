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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc23a055-2428-3e10-8590-0f706f0246bf | -6.92321 | -44.24851 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e34fef2b-7d56-3772-900d-6c836b274986 | -12.66648 | -47.02826 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54643666-28a6-3d06-ad84-48705eda1141 | -6.2433 | -44.06978 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c4d5c57-83e5-3a25-8217-2b427a566f3e | -6.88834 | -52.87098 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 721f7742-668b-39ce-a335-ee8114cf28d4 | -6.17542 | -58.06643 | 2025-07-28 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7db26d7d-ba74-31db-8369-3d5e34a0b9cc | -7.80899 | -50.77588 | 2025-07-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e88c4285-f392-3516-bd68-dcd83f3cd350 | -6.49528 | -56.2082 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 36b163d5-e942-357a-acd0-6612c70ca79f | -6.23158 | -43.70717 | 2025-07-28 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d706a34d-fa0d-3092-9232-6b3006135311 | -7.10118 | -44.93711 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 307d127b-9af1-3d61-a455-6a336d7abe3e | -7.09799 | -44.94864 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| be44029e-2bfb-3dad-b4b5-9420396581e5 | -7.38149 | -44.47785 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17c595f1-6d94-3501-841d-304890556b14 | -10.45928 | -46.51133 | 2025-07-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1531c713-78e7-334d-a338-6e9c9af42efd | -10.83647 | -46.68303 | 2025-07-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99846a44-ef9e-331d-b7f4-2de5cd668117 | -11.97852 | -46.69893 | 2025-07-28 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2322d2e1-60c2-38bb-a67a-098f55a9f948 | -7.11066 | -44.91661 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 66b5f92c-abb9-3fc0-86fb-da6a8637b4cf | -12.67215 | -47.01513 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e292978-59f5-3cfc-ace0-ec8495b9861c | -10.75494 | -48.00009 | 2025-07-28 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc18551f-223a-3afb-ae18-153228438b4e | -6.50419 | -56.20969 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f90cfb0a-8388-32a4-8874-b6d9602bd2be | -8.03487 | -46.90118 | 2025-07-28 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c1a2784-ca49-3920-a91b-a9b3410a094b | -10.92225 | -45.77403 | 2025-07-28 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ab9ade8-a8d1-3a46-9fe2-4996f80da8db | -6.17999 | -58.07029 | 2025-07-28 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3379995-aed5-32b4-84aa-1ce01544978d | -7.9187 | -43.11147 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4f801ecf-2047-36a6-aa38-311b04de000b | -6.55046 | -56.19879 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d4aeb59-60a1-3cdb-9b62-22d9e0540638 | -7.53353 | -44.3962 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3302a63c-aa4a-362f-a19b-f6867d82a65a | -6.55489 | -56.1996 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c2d6b88-d720-3918-bdc7-b1f3010c4939 | -12.74305 | -44.73841 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09fdf359-5357-356e-af23-0840eff7bc7d | -6.40836 | -53.34972 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc13f49b-7c7e-36fc-a003-b246d8065d6b | -7.69816 | -46.04552 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b291f618-9fee-322b-9a58-0dc13b5cdaf2 | -7.21163 | -44.16846 | 2025-07-28 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4988205-65d9-35e5-ada2-a60d2085d3c8 | -7.08192 | -44.90241 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9aa3480-9b5e-32db-b33b-993cc583a5fe | -6.43928 | -41.8885 | 2025-07-28 04:40:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| de7099a4-290b-3ef2-a9eb-eea0a1af7e60 | -7.21464 | -44.1703 | 2025-07-28 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03c2d52d-331b-3745-a5af-b3fc378cf771 | -12.71437 | -47.01638 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f43a880d-5d53-3103-b047-8712606c4686 | -7.91211 | -43.09167 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f20473b8-51bf-3357-837a-021e9e0ce8cd | -7.80579 | -46.57462 | 2025-07-28 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 114c9500-e259-3a01-a231-a04622a6cc6f | -6.76274 | -44.78096 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e680051-1d9f-36c2-b259-ab6b13925631 | -7.92446 | -43.10332 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| acf60f65-1689-3eab-9fbf-75afc9a23f84 | -13.1018 | -47.31124 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1ceac18-c895-3d4d-89a6-b734fe08a19a | -7.10593 | -44.93257 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 782d22cb-1a5d-3430-8cbf-911399eb8a16 | -6.95733 | -42.68475 | 2025-07-28 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 71ebee61-c8ed-3bd6-b39a-528bd2644ba6 | -7.10972 | -44.92317 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7424a9d6-934c-3838-8534-d5bbb68f227a | -6.6361 | -47.56965 | 2025-07-28 04:40:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 351baeb6-899b-3820-aa68-24cec7173891 | -6.92845 | -44.24155 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8752a5a-72d5-3f62-b4a5-adea3bd503a5 | -12.68847 | -47.03617 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0903507-f9d4-3b80-8e51-c35591fa5937 | -7.09399 | -44.94823 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 71c513e6-ff1a-3ac8-99ec-127d84735902 | -7.69844 | -46.05223 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a77c330e-734e-308c-8a39-fd2d22c62b1c | -6.70437 | -43.07485 | 2025-07-28 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 739f71f0-e4d9-3491-a0ed-1cfc218e6e6f | -6.56893 | -41.51848 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b1488b30-5a60-393b-bdf3-0278126dcfcf | -12.7425 | -44.74273 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16eb0771-1ff2-3847-bf84-011c3863045f | -12.71941 | -47.008 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a901ce8f-5433-32c6-b09d-35424cb0a99d | -6.92901 | -44.23766 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c56f301-b201-3126-8063-ec5bb7636a27 | -7.3939 | -44.67672 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dbca38b-5e76-3641-80e5-d679047bc683 | -10.32096 | -54.15508 | 2025-07-28 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ea0c38d-153c-399c-8fe6-660dc1885551 | -6.40246 | -53.36251 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4587127-956a-33ad-81fb-deb80cd5313b | -7.10828 | -44.91678 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3ba76de-8eec-3ecb-bbbf-c6cae2af9f47 | -7.33211 | -48.06529 | 2025-07-28 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22538e64-29c7-3ac8-8b4d-9ed7597a2048 | -13.30315 | -44.18302 | 2025-07-28 04:40:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e402d290-60d0-3ca4-9fff-4312b3ee041c | -6.49899 | -56.21335 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 099f613c-0615-3e79-b9b8-078a8217c00f | -7.91029 | -43.09811 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d0b8c7a0-fd85-3663-ad25-54f5de30d573 | -7.09474 | -44.94288 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 930a66ac-0cec-38b6-bd14-2c6fcb05d538 | -7.11464 | -44.91722 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de851e55-261f-3598-a09c-cf89a0abd646 | -6.56239 | -41.52896 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 74b2f70b-d264-3e33-ade4-2e98143bd729 | -7.29112 | -43.07734 | 2025-07-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05c51ea4-7fe6-3e54-9c3e-8c6a1420a284 | -7.10714 | -44.91273 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5a28570-69dd-3bb4-890d-8737229ef62c | -10.54119 | -50.24826 | 2025-07-28 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a6c2c8ea-c0d2-3748-9387-a9dab2f98f2a | -9.29702 | -48.32888 | 2025-07-28 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a50df7d-25bc-3ba6-bd55-6a58e172c1d1 | -6.50047 | -56.20454 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf6c355d-e741-3b6f-9093-edb9c28374e7 | -6.49454 | -56.2126 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5523138d-b0f0-3239-a12c-b132a2a653d0 | -17.91191 | -54.13238 | 2025-07-28 04:42:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85dfde98-0bbf-3977-ab33-93d806afd27c | -13.50768 | -45.58816 | 2025-07-28 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c9a2835-3c54-397b-8be4-48440276f726 | -13.25731 | -50.13461 | 2025-07-28 04:42:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 257b2be6-0fb5-3c70-8881-f506e8ab97da | -14.98291 | -46.97206 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5e92aed-d74c-3d8b-b063-2af53f9221f9 | -14.98624 | -46.97679 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| af1fc292-7c96-3f92-b3fe-639154003314 | -17.36243 | -42.64402 | 2025-07-28 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6014ad61-f782-3df3-8176-84a3f331167f | -14.50006 | -48.64545 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11711fbf-db60-3979-b9d2-a1244e4e566e | -14.98749 | -46.96766 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67132743-b64f-3e5f-a3a2-8622262cf3ed | -14.49356 | -48.64024 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6199452c-3701-3fa8-be42-88b56874f8c5 | -19.39602 | -44.3231 | 2025-07-28 04:42:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3187e591-d76f-31b2-937e-f7806258aaa2 | -14.3159 | -54.14725 | 2025-07-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ce5ce481-8192-3d1a-951a-b46b8d58eccd | -14.31171 | -54.15068 | 2025-07-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e0b9da11-d51c-3157-ae2e-612f8af7c393 | -14.97322 | -46.98484 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbbf4862-a769-39ca-b950-63e765d8b69a | -18.13808 | -49.97938 | 2025-07-28 04:42:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b9337e-9ac0-37ce-8cfa-ad2960bd1a8f | -13.5265 | -46.29496 | 2025-07-28 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 498d6d28-2668-396f-8201-3c3177098a21 | -14.49002 | -48.63966 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c0d91db-969e-3a5e-b984-c124c9ffa749 | -19.39665 | -44.31739 | 2025-07-28 04:42:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81cba34f-2a48-307f-a315-35abba5e34f1 | -17.35707 | -42.64335 | 2025-07-28 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 166a05a8-45fd-3215-ae29-4f3937338224 | -17.36281 | -42.64053 | 2025-07-28 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b6c632c3-fbc8-3871-840e-a209da9bb3c5 | -16.6074 | -47.82371 | 2025-07-28 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e1f053c-4237-3633-8eee-8b54c5d41aa8 | -14.98418 | -46.96275 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f713dcc1-97d8-33ea-bc3f-59e0e1b1fbf9 | -12.07727 | -63.54991 | 2025-07-28 04:42:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84ba6feb-054d-399d-a9c8-01a08a101a66 | -19.08306 | -43.63556 | 2025-07-28 04:42:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1fc3804-0606-322f-8a1f-37ad1998a6f3 | -14.30819 | -54.15004 | 2025-07-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b44666a9-ffea-3291-b8b2-d096437dc1ef | -14.50656 | -48.6506 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4c71a1-9812-312d-be83-2238b60ee81d | -14.97778 | -46.98055 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c07592a-ea1f-3b34-bfd4-b08db6e14b51 | -14.50302 | -48.65006 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb132dd9-134d-39de-a57a-023fd8a6b653 | -14.51248 | -48.65982 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24e16bcb-2556-3cde-abb3-b12c7b814602 | -15.3728 | -52.18251 | 2025-07-28 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e90debff-e7f7-36bf-9360-57ba28a83947 | -14.2201 | -43.9496 | 2025-07-28 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04deb769-18d6-306d-a24b-24427827330c | -15.95736 | -49.16533 | 2025-07-28 04:42:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69f7f931-33e0-396c-8992-e824f3529022 | -14.49594 | -48.64892 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README14.md)
