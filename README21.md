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
| 5fd263dd-498a-3326-8906-7cacedf9c021 | -8.21217 | -43.32411 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 143fcd2a-3907-392a-96fe-3d65b4f26b1a | -7.43885 | -45.14648 | 2025-10-13 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab10ee2e-9d2c-3600-be2d-5ac418b9cd46 | -8.5416 | -45.42295 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd9355f0-ce97-361d-973e-b91041ff6682 | -5.22113 | -50.95019 | 2025-10-13 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bae29d10-279c-3f4c-9b45-94ea8e1fa2bc | -7.34836 | -44.084 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 024e5346-8086-322f-b39b-f00513ed4cf4 | -7.08435 | -43.51661 | 2025-10-13 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbb83d95-a87e-3086-a544-07e2b6a5dbc4 | -10.80006 | -43.97577 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59fd6fab-efd2-3ccb-962d-a52b9b18d074 | -6.7328 | -42.08882 | 2025-10-13 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 09a3d408-1019-35b8-9edf-ad8dd6e7b5e7 | -7.75264 | -44.20126 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9b7c9827-9fcc-391f-af9f-e3b9da2b4aa1 | -6.58236 | -44.38025 | 2025-10-13 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 906aa15c-fc50-39e4-8f8c-b25f279ade0f | -8.40562 | -45.06478 | 2025-10-13 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0121e7b7-ee73-3123-a5e9-9c9836a57438 | -6.57687 | -45.97514 | 2025-10-13 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78eed0f1-8699-32b0-b9dd-18e780fe0eb0 | -8.46789 | -46.14236 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cc6201a-5f4c-3547-81d0-3371cd34a784 | -7.51233 | -44.59438 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 172ceb63-986c-3501-b10d-791f1822c81e | -6.74355 | -42.16034 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fe6909a5-c23b-3df4-b01a-3ad72b2fe50f | -8.23619 | -43.35061 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a3162e9-8ed0-3b2a-8e18-88faf79ad305 | -7.67872 | -42.56718 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf1a42bd-e54f-3d58-9a57-832c22c78327 | -7.49543 | -42.16372 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 824cb526-5e41-3d82-88e8-bbb2ae230070 | -7.58205 | -46.65477 | 2025-10-13 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28d61583-5c48-39dc-ac12-ebdd2ea264ac | -6.67322 | -46.02695 | 2025-10-13 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d283366-7223-3989-8217-b185890ab059 | -7.69036 | -42.3721 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b96cd3e0-931e-3d3a-9323-1c8ea2599549 | -8.22078 | -43.38254 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08442999-37f4-374f-b721-bcc877b4f458 | -10.80124 | -43.99115 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 628cac6e-b863-393a-b8cd-af63706069e8 | -7.50023 | -44.64965 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3566d122-155d-348e-9b86-244b66dd2ab0 | -10.80752 | -43.99594 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ba88a27-05c9-328e-ad53-8ea4625c3b99 | -8.44565 | -46.1096 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50005738-edcb-3084-99e7-dba84927237b | -6.74648 | -42.16482 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8cab509c-531f-392c-9b31-e2c7701cd80d | -7.51392 | -42.15292 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2719a154-c004-3371-ad71-40a7b1501d6e | -8.2156 | -43.32463 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6a05e230-afd3-3305-9bb0-8efc8adf7c8e | -7.15294 | -42.49512 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0531b647-900f-302c-92b3-f9ddcdeb9c4b | -8.46012 | -46.12653 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21e7d935-4f71-3a8f-98b6-b7019fb10770 | -7.49576 | -44.63468 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e794b8b-abb6-36ad-9035-1cf52cb8d4e6 | -7.7678 | -47.32401 | 2025-10-13 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd20dfbb-af89-3bac-bc78-01f12a11c4ae | -7.34049 | -43.86077 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65478598-c72e-3ba5-9c1d-ceab719c48a5 | -7.05672 | -44.26868 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17afbc6b-9c22-3ba4-b85e-b83eb2033c73 | -7.80906 | -42.44074 | 2025-10-13 04:23:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a07d45c2-0cbd-3815-af5a-e0d8c8e5a1c3 | -6.63285 | -44.65881 | 2025-10-13 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e103b004-8287-3d5f-93aa-0c0b0fc2a227 | -7.50567 | -44.59332 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33bcc709-7356-3217-8a38-5b6d82dc5057 | -7.4973 | -42.15156 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea9be4e1-7309-3ed0-a04b-ced64f474647 | -7.51332 | -42.15697 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 098ef194-2e90-3eaf-a466-83f88fbd8204 | -7.54424 | -46.09279 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 14c050b9-403e-31de-8698-8431e3ced638 | -6.44738 | -44.24501 | 2025-10-13 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a903a8f-bb43-3792-b226-cbcb6fb0d258 | -8.45619 | -46.12956 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1465b5d1-6bd8-3b75-b02e-80bf0d2cb6a7 | -6.28049 | -43.9064 | 2025-10-13 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc531c74-9f05-3348-aa2d-663cc4c1b255 | -7.50235 | -44.5928 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6aae183c-a271-30da-8dc4-877724c2c854 | -8.4763 | -46.13276 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02b47fe8-2b89-3b6b-9819-df011fa0f5dc | -8.22362 | -43.34105 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0682f377-14e8-382d-bb93-02258909f6ed | -6.7665 | -42.81372 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4379d780-2d89-3205-b65f-edba3725b303 | -7.49349 | -44.60572 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcb7e8de-bcd3-3e69-8247-36abaf23a59f | -7.88955 | -44.8186 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd29b35-970e-3fca-87d2-e15379539b9c | -8.21736 | -43.38202 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a8edeb59-5154-35b6-8875-70266ababff2 | -7.68866 | -42.57278 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee7a8c2a-1d16-3c98-bbb5-770015a4aa7f | -7.62054 | -43.04455 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b1b06cbb-bde6-3210-9eb1-0fa1c216b366 | -7.73891 | -42.43154 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ffa5a199-303e-30a8-b82d-50f569005a3f | -8.47845 | -46.16236 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 715e0545-1ee2-3078-ace1-b2b8195bc66d | -10.81263 | -43.9853 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd869e37-52d3-39aa-8ab5-0043d7170657 | -7.77964 | -44.04946 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcf46117-4779-39d1-8a2a-8e2856a981cb | -8.53733 | -44.58707 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77fd222a-6032-3ffe-ae92-b6f88d667377 | -8.38899 | -45.06215 | 2025-10-13 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeffec62-4504-3e94-a78a-44bd94951537 | -6.73932 | -42.85985 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb7fe8e2-2f23-3632-b50e-18473cbcc60b | -7.67435 | -42.38194 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb21b594-f926-314c-9b22-012d114f533e | -7.7819 | -44.05708 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ac484b5-6efd-3824-844e-5175254391cd | -7.69304 | -42.37557 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af6e2815-e908-3172-80b4-b8733412ac98 | -7.80139 | -42.44368 | 2025-10-13 04:23:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| adb79cf8-fb6d-37ad-8c4f-d229bddae289 | -10.7972 | -43.97154 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a2af8a2-dc8c-36a0-a102-961bd78e045d | -10.80293 | -43.98 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f726917-b20f-3df9-b210-474812eda0bb | -7.8413 | -44.52475 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bba52eb6-808d-36f8-9248-26da55caa322 | -7.65289 | -42.56814 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4eda4757-67dd-3386-81f6-7e88be75876e | -8.53149 | -44.58995 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4cfd8be-412b-3659-acd3-d195a77f94c1 | -8.21846 | -43.32886 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0280c726-3f1c-3bed-aec0-483e7f11dcf8 | -8.52498 | -45.39881 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 743ee673-9a5c-3697-989e-92a34f1e8070 | -8.22419 | -43.33735 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1550e246-e6c4-3fce-a6cc-07ed6696f286 | -7.51954 | -44.59195 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4c5858c-1320-3ec9-bb3c-186b7e18a4b2 | -8.45284 | -46.12902 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 61b70664-90c9-3505-aef2-5bf489b02d08 | -8.46511 | -46.13827 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8821c91a-6f4d-39d9-b1e9-8dae1a35fa1c | -8.23333 | -43.34636 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8271e0ae-be99-3252-add5-b16788a49ddf | -7.8901 | -44.81511 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5fa9ee7-d967-3017-8dd4-35398c94cf07 | -7.78525 | -44.05762 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afa008f8-147a-32aa-bfae-7b5fcec99821 | -8.46404 | -46.1235 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c12a2cb-9a7a-3de1-b795-3ae6dae3ba5e | -7.68434 | -42.38758 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a2cab09b-6d6d-3f45-90b8-ce5e39a74413 | -6.58624 | -44.37729 | 2025-10-13 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef9b60b2-d4f7-36a0-9f19-2199ad8d4777 | -7.7858 | -44.05407 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f019a8bf-1bd2-390c-8c0f-a9078aa3a0c6 | -7.51288 | -44.5909 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6de35bb4-9447-3d49-b3c8-2d17e5bef8b8 | -7.55347 | -43.83924 | 2025-10-13 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 890abbac-fefc-387c-a37f-03a65616e55a | -10.78791 | -47.28494 | 2025-10-13 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da8cbc4-4474-3d6a-9626-4c4d63107c73 | -7.55065 | -43.8352 | 2025-10-13 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4211d0b8-30df-39e4-b80e-30931c01a5be | -8.45955 | -46.13008 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1876a613-79f2-3e06-bc86-20bedcec2f30 | -8.45178 | -46.11424 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2116b179-0bf6-39f2-a3e9-9dc2bcf4b109 | -8.47352 | -46.12866 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 264a3e2d-1de8-3d5f-acd6-15931fa28994 | -10.81718 | -43.97839 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3da8e31-dcbc-3b27-b551-f0884b23f691 | -7.48629 | -44.60817 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0222962-2507-3138-be82-92cbf5c71bab | -8.47541 | -46.24594 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3fcc4e7-d07f-35b6-8903-0ce8f8609ad7 | -6.75778 | -42.80923 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fb7ddcd0-3789-39cf-bbbf-b7605301a246 | -7.56019 | -43.84032 | 2025-10-13 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a55d3e10-aa13-3a4f-a888-3a2f24231f91 | -7.5217 | -44.29462 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c4b709e-bf38-3882-ac4d-273f40af2744 | -8.52442 | -45.4023 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 528efa3b-11b5-334a-abdb-787cff5f36ee | -8.71859 | -41.08553 | 2025-10-13 04:23:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 71f336c4-94f2-3002-9e1b-7d9566ca5467 | -7.65413 | -42.58739 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c848dba8-f10f-310a-9df2-6bc16c41d90e | -7.83797 | -44.52421 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ec89931-73fa-3452-8694-cb267f0208f4 | -5.22038 | -50.95456 | 2025-10-13 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README22.md)
