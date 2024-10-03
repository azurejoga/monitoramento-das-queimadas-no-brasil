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
| adfb08a0-9aa3-3e1c-b3b8-28cd303c1010 | -22.58268 | -42.14463 | 2024-10-03 00:26:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2c9a9fec-a90d-33e9-aa7c-a51282753d56 | -22.44846 | -46.8929 | 2024-10-03 00:26:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 5ec4c2f9-09e9-3a51-ba54-4413a8898c92 | -22.44594 | -46.86349 | 2024-10-03 00:26:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 51.3 |
| eba51e59-4b29-3ee7-988a-2fe8c03a58c7 | -22.44547 | -46.86877 | 2024-10-03 00:26:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7d16d091-9e2d-336f-ada3-cb1e65516934 | -22.37028 | -47.93211 | 2024-10-03 00:26:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 19c8f7d3-6958-387d-a4da-d165e3fff853 | -22.36415 | -47.97535 | 2024-10-03 00:26:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f2b323de-06e8-3e9b-a9e2-01aa8e6de393 | -22.36095 | -47.93853 | 2024-10-03 00:26:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 254.7 |
| d83812e2-ab8e-3b4e-886e-85a1aac1b231 | -22.35727 | -47.97007 | 2024-10-03 00:26:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 53824bb1-14b4-38b9-8a2a-9106a2c0825e | -22.35432 | -47.93316 | 2024-10-03 00:26:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 259.5 |
| 37f67b0f-8527-31c9-9e67-45ae5a96e4d7 | -22.34504 | -47.94011 | 2024-10-03 00:26:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6a57c7fe-7552-3eaf-a647-a880dbf5e9b5 | -22.34279 | -48.30204 | 2024-10-03 00:26:00 | TERRA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 5155d365-551d-312d-9b23-ef9f2a55c24d | -22.30951 | -44.07681 | 2024-10-03 00:26:00 | TERRA_M-M | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 2a80643e-6240-3aa2-9be8-6f5ed8380311 | -22.30755 | -44.05834 | 2024-10-03 00:26:00 | TERRA_M-M | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| e0765e46-fde3-3527-93ff-42513ded2bca | -22.27178 | -44.23612 | 2024-10-03 00:26:00 | TERRA_M-M | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 1b11847b-c231-3912-9926-c7f8b6470def | -22.26484 | -44.2308 | 2024-10-03 00:26:00 | TERRA_M-M | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d66abcb4-25ac-39a8-be6f-983265ea7685 | -22.2405 | -48.43707 | 2024-10-03 00:26:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d6270639-cb68-35ff-b88c-c65d565cd19e | -22.16128 | -42.54034 | 2024-10-03 00:26:00 | TERRA_M-M | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| cd604159-c6c6-3838-850c-c2e5dc1508be | -22.15241 | -42.5565 | 2024-10-03 00:26:00 | TERRA_M-M | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 72a541f4-771b-3f5f-96db-59008b746811 | -22.1508 | -42.54258 | 2024-10-03 00:26:00 | TERRA_M-M | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| b14b3968-ab9a-367e-a03d-86e742795183 | -22.07718 | -42.09179 | 2024-10-03 00:26:00 | TERRA_M-M | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 2b6a5c13-518e-35c0-befd-1897bddb18b9 | -22.04064 | -48.73542 | 2024-10-03 00:26:00 | TERRA_M-M | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| e5241923-86fe-32f0-9b9c-9f9fa8bec83c | -22.03584 | -48.74048 | 2024-10-03 00:26:00 | TERRA_M-M | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.1 |
| 39531fdc-fc25-337e-8483-be6bbc428a38 | -22.03263 | -48.70096 | 2024-10-03 00:26:00 | TERRA_M-M | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.5 |
| 4ff71d90-5728-3aef-ac40-6014b2776cf7 | -21.9221 | -48.44958 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 39744de3-c373-32e5-a385-945e92c508be | -21.9189 | -48.41114 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a4adde78-77da-3a5c-8b37-a4fd0e40b73b | -21.91573 | -48.37326 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 7514ce44-2d8a-30b4-920d-4258cc464fb5 | -21.91273 | -48.33741 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 101.4 |
| bd82d37a-1db2-33d0-9fa3-b1e7b0016ec3 | -21.90644 | -48.36805 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 186.2 |
| ffb6ddf8-eef5-323f-a916-9bb38235e0cb | -21.90566 | -48.4509 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 68.6 |
| cde9c9c6-2683-3024-9777-00226b9ea0ec | -21.90248 | -48.41225 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 35d49b1c-6b1e-3f2f-9a0d-1aea0fa7d265 | -21.89945 | -48.37539 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 142.4 |
| bae32605-69ce-37d9-af71-9041d218b797 | -21.88913 | -48.45114 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 35dac24d-5e55-3151-a55e-683edc748db6 | -21.88611 | -48.41385 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 0d8ca2fb-cde2-30c4-b5c9-36805fab8fc5 | -21.88313 | -48.37705 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 165.6 |
| c72f8a6b-e54d-3a5f-97d5-40a2dd7b8725 | -21.88246 | -48.45725 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 74f4ffd4-b60f-3350-9da3-c90b7c84f1f9 | -21.87924 | -48.4202 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 5821a3b2-97e9-3098-84eb-20385ceec93d | -21.87602 | -48.38335 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b1387c4b-acf9-3b51-b585-cac813c1aeef | -21.87273 | -48.45282 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 179.0 |
| ac9eb3a7-c5a0-36bc-988f-5367920488af | -21.86976 | -48.41566 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 4ac125eb-afb7-3190-b35c-1d17dc02f8a7 | -21.86607 | -48.45908 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b4ca1292-f0c9-3de8-ab01-bf8f3f73ca4a | -21.86291 | -48.42223 | 2024-10-03 00:26:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 24eab0c2-58fa-3474-abf6-38d3320faab8 | -21.79018 | -42.49454 | 2024-10-03 00:26:00 | TERRA_M-M | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 1ea596f3-33ca-3579-9cee-1b8b017b64ee | -21.78864 | -42.4814 | 2024-10-03 00:26:00 | TERRA_M-M | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| bdd4a8bc-7f22-3ec3-a178-e571acdf2549 | -21.58649 | -41.3003 | 2024-10-03 00:26:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 2c45e04d-0ccb-375d-ab9f-5983883c7f09 | -21.56625 | -41.23991 | 2024-10-03 00:26:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1acb904f-45ac-3a4b-9c12-51508e2bd622 | -21.56482 | -41.22858 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 89e26ca0-0d86-30f7-a28b-af4217b2040d | -21.49376 | -44.57832 | 2024-10-03 00:26:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| cc29b68c-268c-3f8e-aeb7-5b192d2cdd5a | -21.4899 | -44.58414 | 2024-10-03 00:26:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 95254ff0-2171-3001-aee2-b9fe06c1d25b | -21.48801 | -44.56657 | 2024-10-03 00:26:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c19a41ed-5ffc-3dc2-91fc-0033bc8c5d28 | -21.48405 | -42.14117 | 2024-10-03 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 9a63d0cc-5ff4-32a1-926c-3e4f839c996e | -21.48148 | -44.57907 | 2024-10-03 00:26:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 1e441166-ba5a-3bcb-a935-dae247bcf317 | -21.45334 | -44.58903 | 2024-10-03 00:26:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 41cc04a9-7130-3665-8819-330152191368 | -21.39074 | -47.68985 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 80c9894c-552d-3532-8433-438f07d0bcbd | -21.38799 | -47.65865 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 81.4 |
| db7848e5-1892-30c4-846f-93e509b38db3 | -21.31421 | -41.40331 | 2024-10-03 00:26:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| eebd5bc8-9042-3983-b859-4a7b4a76f6f6 | -21.31247 | -41.40947 | 2024-10-03 00:26:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 67e65964-a25d-3249-b8ab-c1b9ab78b939 | -21.30871 | -47.60783 | 2024-10-03 00:26:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a96c0048-035f-35ca-95d6-b4cc5d387420 | -21.30833 | -47.63497 | 2024-10-03 00:26:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 970258e9-72e7-39b4-8494-c4faefc5cffc | -21.30549 | -47.60069 | 2024-10-03 00:26:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 33a92114-752c-3cca-8c7a-75e7e895008c | -21.29327 | -47.60829 | 2024-10-03 00:26:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 187983c4-44d7-3ab1-9c31-61cb342022ea | -20.7686 | -46.31005 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 9348cef1-7806-3886-bbc1-8512639b1d9c | -20.69106 | -41.98021 | 2024-10-03 00:26:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 9ef7d17c-24ab-342c-8aee-f135186c9cc0 | -20.66399 | -42.00877 | 2024-10-03 00:26:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.4 |
| 88d90701-7dec-3c8d-a675-fee01c10a956 | -20.66239 | -41.99525 | 2024-10-03 00:26:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| d34fd306-ad2d-365d-898b-5a92c62e4d3b | -20.54588 | -43.37049 | 2024-10-03 00:26:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 9506f452-4721-3eb2-bf1f-ca819d78a8f6 | -20.54433 | -43.37709 | 2024-10-03 00:26:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| ba5e2569-6b7e-3347-beef-39d7d4dae0e4 | -20.54257 | -43.36214 | 2024-10-03 00:26:00 | TERRA_M-M | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 32703add-2232-3047-b8e2-6a59c00c86d8 | -20.51912 | -43.75039 | 2024-10-03 00:26:00 | TERRA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| fbdd50fe-2ca5-3763-a3e4-aecd999b4b18 | -20.5174 | -43.73481 | 2024-10-03 00:26:00 | TERRA_M-M | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 4caceaea-afd7-3a45-88af-a9de481b5606 | -20.43828 | -41.99392 | 2024-10-03 00:26:00 | TERRA_M-M | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| b526729f-a3cf-3df9-b09e-1cbe69a46fe2 | -20.28905 | -43.52485 | 2024-10-03 00:26:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 4f8f1663-f4ee-3f1f-887e-fdf3a85ecd2b | -20.28824 | -43.53086 | 2024-10-03 00:26:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 4ae409cd-fe77-3a9e-8942-4774912dd289 | -20.27793 | -43.52561 | 2024-10-03 00:26:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| e6193f3f-d86a-312a-a402-5081c95fbd13 | -20.2232 | -42.48625 | 2024-10-03 00:26:00 | TERRA_M-M | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 712923fb-41b1-30d8-a860-85b019316d42 | -20.21294 | -42.48757 | 2024-10-03 00:26:00 | TERRA_M-M | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 73b72845-ac84-39bc-bed4-3fadcebd7358 | -20.21139 | -42.47464 | 2024-10-03 00:26:00 | TERRA_M-M | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 6cfc2cce-fb82-3293-aa1b-7cbd90eddd16 | -20.15829 | -41.8717 | 2024-10-03 00:26:00 | TERRA_M-M | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| 9bac361f-9ea9-3f4e-bdfb-5778f60fcfaa | -20.14848 | -41.87334 | 2024-10-03 00:26:00 | TERRA_M-M | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| d3d2bc45-31a9-3810-bc20-2cae3c5a76d8 | -20.14387 | -43.85922 | 2024-10-03 00:26:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 484776dc-8f0e-3a0f-a2ca-2d4b50b0101e | -20.14267 | -43.85377 | 2024-10-03 00:26:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.1 |
| b45e3839-d45b-34cc-b630-de7112441e4c | -20.14207 | -43.84371 | 2024-10-03 00:26:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 6d71c07b-d748-3f6d-b48c-906ce256c102 | -20.14099 | -43.83829 | 2024-10-03 00:26:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 2ea1e571-b72f-3656-960b-8ba4977ff781 | -20.14026 | -43.82814 | 2024-10-03 00:26:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.0 |
| 278d4f20-d50c-3037-943c-ce96eba0b7f7 | -20.13929 | -43.8227 | 2024-10-03 00:26:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| 2bf8253a-7903-3150-8574-3870ac425325 | -20.01995 | -44.52279 | 2024-10-03 00:26:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| ebdbfe87-78b5-33d0-b2b9-40bdbfae23f4 | -20.01206 | -44.51153 | 2024-10-03 00:26:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.2 |
| 9c0d1c0b-4768-3c14-be60-14e7116af7cf | -20.0099 | -42.07207 | 2024-10-03 00:26:00 | TERRA_M-M | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 4fe197df-0e59-30e8-bfdd-ec5b660f7f48 | -19.87249 | -43.16423 | 2024-10-03 00:26:00 | TERRA_M-M | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 6791a43c-86c5-3add-867d-5b4f2c402721 | -19.86879 | -43.1698 | 2024-10-03 00:26:00 | TERRA_M-M | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 6cd430df-13ae-3ddc-b554-5acf647cc370 | -19.81075 | -43.84248 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 95767dba-e17a-3ce4-aeee-6b1ea3dbbe06 | -19.80898 | -43.82678 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4863f817-8103-38f6-91b9-68590017b262 | -19.76594 | -43.64481 | 2024-10-03 00:26:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0e08badd-2bc1-3bf5-9a17-251607b514b0 | -19.76424 | -43.62962 | 2024-10-03 00:26:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c64d4d7d-3bad-3249-9631-ff05f455af12 | -19.76365 | -43.52521 | 2024-10-03 00:26:00 | TERRA_M-M | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 86c6f281-1b0b-3b9f-8087-2918fa68391e | -19.74299 | -44.26347 | 2024-10-03 00:26:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f3d7e618-6e50-383a-b63e-72289ae37391 | -19.74115 | -44.24656 | 2024-10-03 00:26:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 06905d46-3903-35dd-a1d1-a4b731af0fd9 | -19.7408 | -40.68119 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 99fe0f86-3f65-3043-9eb9-fbd7c2edb1d6 | -19.69051 | -42.03803 | 2024-10-03 00:26:00 | TERRA_M-M | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 51b07e39-6d02-3151-becf-95feaaaa25a8 | -19.50619 | -42.87797 | 2024-10-03 00:26:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 5c470eff-bd2c-35e0-8837-0f4d60c04fdb | -19.50471 | -42.86531 | 2024-10-03 00:26:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |


[Clique aqui para ver as próximas entradas](README14.md)
