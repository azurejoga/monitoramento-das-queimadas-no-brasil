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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df5cf93a-5952-3444-b447-df1dce746d23 | -6.02557 | -46.66649 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 988125fd-243d-36b1-bc81-79ef370295bb | -6.28667 | -43.60367 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ddd7228-3972-3879-a984-bcb12768eb34 | -6.93899 | -42.9727 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23584b3f-d580-3658-8f78-f8d3b117b25d | -8.02991 | -44.14485 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70c5cf1a-1f08-3abf-89d6-9f02b9b1d35a | -6.26782 | -44.51164 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cdf58276-9715-3314-80f9-f07d1d1dac32 | -7.81331 | -46.08787 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e0deeb0-948d-3612-a90c-8d1fafc2c36a | -5.93985 | -43.04735 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b368f2c5-0cc8-31e9-93da-9405c8535b17 | -5.70251 | -45.40037 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05186aab-c242-32b7-8d46-162b23cb5dcd | -6.29358 | -43.5096 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3340a3e9-9e78-3b96-8c01-20129d6e5a43 | -7.50838 | -45.35012 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bae96a9-f615-3f2a-b8de-08a641092483 | -6.23935 | -42.62421 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0bb8fb32-daab-3f3d-869d-e0686220018c | -7.01595 | -43.23339 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 154d9c9d-1b60-3bfb-8417-8400776bb2c4 | -5.83845 | -42.99926 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3b44c03-0d9e-3321-87af-1c595acfeabe | -2.7839 | -49.61929 | 2025-09-04 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45969b6c-7053-314d-8435-992c84fb28d3 | -7.04934 | -43.26331 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 741a155e-f9cf-3647-8236-010bc289dc41 | -7.55304 | -45.72403 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c6f502-1849-309b-8275-ecb702cc8a35 | -6.50459 | -43.07397 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0c4a9ca-bae3-3715-93cc-24200f8541e9 | -6.06087 | -43.41877 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2defec92-044c-33e9-978a-35be708ec827 | -6.677 | -48.40413 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6b664adc-5897-33ef-9607-91fb446e894c | -5.80334 | -45.62697 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f60e9cc-8257-3a39-aaae-32edba5eba5b | -3.9804 | -43.24027 | 2025-09-04 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db54a6e3-1756-359e-9cb0-9345d39532a7 | -6.86857 | -45.57835 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d4f0ada-b880-3cbc-8604-2cf630510f16 | -6.8085 | -44.46221 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3dfb86e-ac64-3907-8c33-e09d846333e7 | -6.74062 | -45.91992 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa3c0f65-fc54-3c42-a7c6-c4167ec582bb | -6.95469 | -44.95195 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2325f37f-37ab-3d0e-840c-b8bd12b90bad | -4.89412 | -44.95554 | 2025-09-04 04:25:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70599d4b-4731-321c-af8c-7dee5990e5a5 | -6.26224 | -43.28839 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88cf35ee-2674-30b1-b202-026fa65d16b6 | -5.91096 | -43.33569 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8de160ac-cf0c-3e2c-9624-4329c60dcf79 | -7.79646 | -45.42765 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25f293a1-12e6-33e5-9545-d9633604d958 | -6.12528 | -44.11421 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d0191f8-ff2d-301b-b72f-a2cc72976d53 | -6.0234 | -46.68031 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 844b6851-128a-335b-a56b-145ef5346c83 | -5.86711 | -46.11502 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3368674-9aff-3daa-aa70-f692abf053a3 | -5.82294 | -46.11172 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00e5d305-da44-39e4-ace1-b4262b7bee02 | -5.70009 | -45.17347 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee50f770-d834-304b-8889-37a6badbe3f7 | -3.62437 | -53.70583 | 2025-09-04 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf3928ae-dea0-323b-8ff3-f5c546f3e516 | -6.34167 | -45.68605 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9a42120-ea3c-374e-b09d-e4323d5d9308 | -6.46439 | -43.69777 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5cd40c84-8b4a-3b1f-995b-ab5041bd5866 | -6.78906 | -44.45144 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5912795-a31e-33cf-871d-b577fd8f4812 | -6.1585 | -43.3192 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 889dd5f8-d95b-3178-ad78-4ce6c9734ef5 | -6.26845 | -43.58029 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb6c4422-c904-34ec-9b7e-75c4ce5381bf | -5.5862 | -45.51464 | 2025-09-04 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d2c7148-e818-3c94-9133-eec15749d5b9 | -2.7843 | -49.61813 | 2025-09-04 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b58d7b8-9358-31d1-baa7-c7e92049e473 | -6.62293 | -43.97 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75ecb5ec-90c1-3566-8a37-80c1c6215104 | -6.23898 | -43.53605 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6cbee6-6cdb-3509-be96-3c4718aa1254 | -6.27181 | -44.50843 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4c69972-37f0-3b14-9106-48ab2f93bcb5 | -6.30884 | -43.28542 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d108ca0-5cf9-3ea2-b6cf-d2ecbe9a64d8 | -4.35243 | -48.72329 | 2025-09-04 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e0c657-b9a1-3a2e-a93e-946f4fe8b8f8 | -5.804 | -45.31596 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27c2a669-430d-320c-9bfe-dc652d9fca92 | -6.54453 | -43.91108 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95d6e560-d3e7-387c-adaa-525ef7b72e7c | -6.69713 | -48.41113 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21fa8211-2a2a-3726-8ea9-3ec30cfd0a4b | -6.12356 | -42.94602 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9a467287-e65d-3668-ba0b-751bda0a3240 | -2.96293 | -49.35356 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| be324c33-47e8-319e-9645-9523e3ae8a16 | -6.77144 | -44.49833 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93ca6c63-7022-38cb-ba35-ea7156c13de1 | -6.68009 | -48.40825 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4aa6d062-e75d-3275-819b-ba58556955c6 | -6.67095 | -46.47909 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a0e6da2-0bd9-3072-ac9d-97fac803c27c | -6.36488 | -45.64728 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1837ba7-20db-3fe3-b9b5-24d8b14a207c | -6.68227 | -48.4164 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c52ac94e-f8e6-3e04-b477-b487edfedace | -4.83431 | -42.73506 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5032bbe4-d767-37fb-9bf5-66d404e7b1d9 | -6.28171 | -43.84953 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92fc488b-e8c7-3853-a464-74e4c6e0dbe9 | -6.32565 | -45.67989 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aadbc743-1bce-39a2-9408-f6eda291b7e8 | -6.7743 | -44.50262 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31d61916-9ba6-3ec3-99f4-86b903427e83 | -8.03462 | -44.13738 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b67d6c83-b754-321d-a873-b27645a024d1 | -5.38331 | -45.94383 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ce81b9b-dc1f-3eb7-a073-6719a2f04f16 | -7.15297 | -46.17988 | 2025-09-04 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d19c4eb3-092c-3f66-ae97-54950472419a | -5.87041 | -46.11554 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e1f0a60-3de7-3e89-af9a-b1aae0653d22 | -4.8371 | -42.73667 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d0460f2-9bec-32a4-9462-c540b1814757 | -5.55574 | -43.09184 | 2025-09-04 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2f0bcc97-6221-3c8c-a787-2bf77e0687e0 | -5.82174 | -46.36207 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8646832d-350f-3133-b6eb-5c36d2bdbb9c | -6.734 | -45.9189 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e4c3381-5cc6-38a4-be92-9818cbf89fc6 | -5.69416 | -45.38835 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8c92997-7259-3b10-a994-e426ed83249e | -6.75042 | -45.92493 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 859836a7-3ab5-3355-b0c0-c2432f869fe1 | -6.38314 | -43.53889 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31dc60bb-2fc7-3238-bb8f-6d2d34f93346 | -7.50792 | -45.37563 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 514c56ff-b55f-395a-84ca-d5ab641ffef7 | -6.20021 | -47.84576 | 2025-09-04 04:25:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 637da090-4e0c-3234-b027-46e5b40335e8 | -2.96221 | -49.35798 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3802ca5c-40fb-3a8f-9672-825b1ddd5758 | -6.21311 | -43.39481 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cf137c8-ef30-3a4d-af85-bbd0accd8087 | -6.2305 | -43.37654 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6909d862-967a-3ff0-a8a5-7b83fddbd7d5 | -5.27068 | -55.95878 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0722061b-f76e-336e-8e79-9553ea774b86 | -6.92918 | -45.55866 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc80f5f0-b488-3541-811c-83a29dcd9349 | -6.12658 | -42.95084 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 39b04b6f-9399-3192-bcb8-4465c4f395d9 | -5.38385 | -45.94038 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3e6967c-a677-3f96-9776-d6edf8c1a7c4 | -2.95778 | -49.36183 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f0a5d779-96af-39e8-8a3b-d313dfe67a0a | -3.68932 | -49.57017 | 2025-09-04 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88e43e5a-b4c2-3ef4-8771-e7447109eef1 | -6.2265 | -43.54646 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f513a075-e00b-34c7-942e-077445bff18f | -6.2259 | -43.55037 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 672eb0b4-9c9f-3f41-84c8-dd98b8199910 | -5.89406 | -45.96381 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c7c8d6f-c779-30fc-897d-6202c1a7b0ec | -5.71394 | -43.1055 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7734d7b7-347d-3006-8ad9-daae0fdeff7f | -5.69783 | -45.16588 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83343376-6bd3-389f-b500-cf0e188f94c2 | -4.55703 | -40.35086 | 2025-09-04 04:25:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53ffeb46-0126-31f2-a7fb-e3b243cf9c50 | -6.88401 | -44.24492 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aca79a52-2d97-36eb-8ca1-e7ca76648728 | -6.74658 | -45.92786 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee895956-c58e-3db2-b640-e85a1c7df330 | -6.31886 | -43.55866 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 773c516d-80e5-3268-ae48-5a02b3decfcc | -6.22816 | -42.44266 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e9f861c1-0dea-3ac6-a869-1f70e6a98bfa | -7.01359 | -43.2244 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df7e7a9e-d3d8-3719-88b3-705c5fb4f513 | -6.8913 | -45.5637 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c1942cb-7766-3903-b3fd-589a7fcfedb9 | -7.55691 | -45.72102 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1aec4b5f-6b2c-3237-94f3-ad0f4cad1aa4 | -6.22989 | -43.38061 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b4718b4e-1eff-3fb7-87b7-603edb28ccba | -6.26006 | -45.15852 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b7c2f24-99dc-3e7e-894d-75c8ca513a41 | -6.77487 | -44.49887 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb52c513-a1cf-3809-95a7-747bae0461a9 | -6.7845 | -44.45841 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |


[Clique aqui para ver as próximas entradas](README29.md)
