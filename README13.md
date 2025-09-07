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
| efe2e82c-191f-3726-bc80-2b1c91cfe014 | -15.1027 | -48.085701 | 2025-09-07 00:45:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93ba72e7-b6ff-3c2f-9100-171397d0b0a4 | -3.8083 | -54.130901 | 2025-09-07 00:45:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ade7fb-8a1c-3901-8b45-068940f73c2d | -10.9956 | -52.057701 | 2025-09-07 00:45:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0670bf18-aaa1-3779-bc91-ae6dc9876484 | -5.9698 | -44.153301 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80a74dbd-366b-3bbd-b3df-11b867b3b2d1 | -12.8821 | -48.012402 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d087afa2-4436-3d1e-bf98-dd23dab3d650 | -12.5345 | -48.070499 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2052407-a076-3511-855b-5975b5851146 | -8.344 | -48.279701 | 2025-09-07 00:45:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 752f9ced-69b6-3bea-a5ef-aa4a5145569e | -7.9196 | -49.310398 | 2025-09-07 00:45:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de1ed686-d90d-39cd-8b34-54787f8b79c4 | -6.1277 | -44.252899 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58c5ba84-03c5-3a3a-a405-3d48cbdbf2e8 | -8.6155 | -54.657501 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5061359e-0707-3474-911f-5c3236e262ed | -10.7356 | -48.1842 | 2025-09-07 00:45:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b90aebaa-5017-3d92-87c8-6233f6bf23ea | -6.1896 | -43.396599 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5dbc0f9-c51e-32fd-99b9-58b922369abb | -6.1837 | -43.372299 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89bb9f42-3581-343c-b876-f400c5a117c1 | -11.2064 | -55.009399 | 2025-09-07 00:45:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6527458b-1d1b-389e-86bf-7685adea1d71 | -20.067801 | -41.722 | 2025-09-07 00:45:00 | METOP-C | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 074694b1-8424-3fa0-b100-ddfafbe3f982 | -3.2317 | -50.814701 | 2025-09-07 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87ef741c-ea0e-3489-bd8c-c404f5f165bf | -8.1756 | -44.7878 | 2025-09-07 00:45:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 025517bb-bf85-3583-ae67-91359c81d5cc | -11.2686 | -46.421799 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5686b523-358a-3492-a519-56745709cbde | -11.6061 | -47.165199 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e53b389-83e1-3ae7-b545-f7c36228f102 | -10.0483 | -48.064602 | 2025-09-07 00:45:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac96bce4-e776-3ff7-9b9d-1eeba6345017 | -7.9769 | -49.835701 | 2025-09-07 00:45:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5efbc243-efea-3b21-a9aa-460c486b63eb | -12.5117 | -48.061001 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e236c90d-75df-3a43-bc90-f98d196c6456 | -5.9822 | -44.1619 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfa8cc70-b81a-365b-9060-5e1bc134921a | -11.1447 | -48.396801 | 2025-09-07 00:45:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77daa5ca-8b7a-3615-990b-81916453ef6d | -10.9937 | -52.048698 | 2025-09-07 00:45:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0666cde8-926d-381d-9fa6-c17f72039744 | -11.8392 | -50.550098 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d70dd52f-20f0-39d2-a905-7caad5d9842e | -11.2514 | -46.4804 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| face907a-d93b-3dbb-844b-6c8e5344ef69 | -7.6686 | -50.295502 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad17a55-a3a2-3102-a5e2-5bebca210a7c | -9.731 | -48.980999 | 2025-09-07 00:45:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e15c9c3e-80f8-320a-b597-9ec6d3602aef | -6.2673 | -43.505001 | 2025-09-07 00:45:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14f051e1-cb98-3e0c-82d8-f91f0ef9f7ab | -6.5657 | -51.113701 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c2ee92-30f7-3c46-8b5f-242e787da97d | -18.0945 | -45.166599 | 2025-09-07 00:45:00 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe69e854-a68b-3877-8403-6719e596bd76 | -11.4105 | -43.634998 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f964754-f417-317b-879c-626c71aabde9 | -6.2602 | -53.431499 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1544bd-ca0a-3d25-85e4-ad4c6ef16b13 | -11.2543 | -46.448601 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37ff03c3-7f25-3ce2-bbcd-943c14f8f64a | -6.1802 | -45.424999 | 2025-09-07 00:45:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2950590d-cca5-3ede-9e19-e0459b3c8464 | -17.68 | -43.537102 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee538b0f-6ce6-3b2d-98d7-1411734b94eb | -15.1109 | -48.076302 | 2025-09-07 00:45:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c02352b4-6dad-3f5d-864b-9d4d51eaf083 | -14.8432 | -46.701401 | 2025-09-07 00:45:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d3a4ae31-2a7a-3ebb-9353-0d86dc26a54b | -7.9785 | -49.842701 | 2025-09-07 00:45:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c768487-0ea8-3939-9cdd-188008b98c12 | -13.8144 | -43.863499 | 2025-09-07 00:45:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2bd8031-6ab9-3c94-bb0d-a4faa7047c7f | -15.5273 | -42.652302 | 2025-09-07 00:45:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ec8f829-46d2-3097-b0b3-9c047321f488 | -6.27 | -53.429401 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47358491-fa40-3466-8a16-700ee291ab1b | -6.1935 | -43.369999 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf51bfb-b477-3ec6-aade-190645960c4d | -14.8168 | -48.189098 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 52aaccd8-37a2-3afb-8bc4-816de198c266 | -5.9376 | -46.1889 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 203ae453-ec7b-3938-92af-ea4c7178af38 | -17.6682 | -43.531101 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ae37b0ca-8e3c-3d2e-aed6-0bcc2f3ecf8e | -5.7133 | -43.943802 | 2025-09-07 00:45:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ecc1081-f908-3763-a981-40f3d824ef75 | -13.03 | -48.073898 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3ae0a1a-1eda-3853-83a6-9e81e26ba046 | -11.7791 | -50.604198 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd69c6f3-9695-3f56-969d-e62c39fdb07b | -1.9216 | -56.594002 | 2025-09-07 00:45:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af91897-3a57-38c7-a463-69d8db1fea7d | -15.2209 | -52.370701 | 2025-09-07 00:45:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef2ab0fd-6929-3b42-8c65-65f3b1a904dc | -8.5056 | -51.3241 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8d6e6f-fb69-33a4-8bdb-2e92e9c0c1c9 | -21.696699 | -47.2006 | 2025-09-07 00:45:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89937f29-907c-3085-9b12-4bc74c970ea6 | -9.9819 | -51.6381 | 2025-09-07 00:45:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4be4953-e23b-304a-8dc3-172d095e718a | -17.672199 | -43.548199 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7d200ee9-3d94-33aa-9566-144d6ac35174 | -11.5881 | -47.176899 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb303df-5216-351d-98d2-139813b50a4d | -22.414801 | -47.444801 | 2025-09-07 00:45:00 | METOP-C | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| affd42ef-3633-3546-9dcb-52ed990cddde | -3.8062 | -54.121498 | 2025-09-07 00:45:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3bcf042-bae4-3240-a86c-d8002e05da1b | -5.7106 | -43.932499 | 2025-09-07 00:45:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a875e36e-fedd-3768-8fcb-6ab7289f7b75 | -8.9252 | -48.6558 | 2025-09-07 00:45:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e035131a-b8e3-3f6c-8137-1019f7ec6815 | -10.3761 | -44.960701 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 81224202-9ed7-38d4-abfd-a7ad7c6fc65e | -12.5315 | -49.1157 | 2025-09-07 00:45:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d37eaaef-8bbf-3ac5-a65b-1184cb164d75 | -7.7272 | -50.327099 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e27d5d6-191e-3b9d-a976-57a080ee6282 | -5.6675 | -45.438499 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98ad8de9-2fd4-3270-8c29-97e98a94438e | -19.870501 | -45.028599 | 2025-09-07 00:45:00 | METOP-C | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6636c2a3-f02c-32a1-a3ad-44ff9eb36cc2 | -19.4056 | -44.312698 | 2025-09-07 00:45:00 | METOP-C | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2787d6c9-4026-3d7d-a09d-45d21fdb98a4 | -11.1869 | -55.013401 | 2025-09-07 00:45:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b430f2b4-1373-3b67-899b-cc40172f063e | -11.8325 | -50.519001 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a2bedc0-6d2d-3115-9aaf-3fe1d4fdd967 | -3.5771 | -47.522202 | 2025-09-07 00:45:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdbed71f-8986-32c5-85f5-b1eafad9ef75 | -14.8399 | -46.687099 | 2025-09-07 00:45:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5ef54e-704b-3dd9-96b1-1c1b41c52b39 | -11.3984 | -43.627499 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 050bf396-65ae-3b0d-8b32-53e2509c5150 | -11.0441 | -54.173801 | 2025-09-07 00:45:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a62fc1d-1d55-3eeb-8c6a-ebb9d1e92084 | -15.9694 | -42.386398 | 2025-09-07 00:45:00 | METOP-C | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 363f9af2-b416-363f-9bc6-aa9f2c5f14c8 | -13.0284 | -48.066898 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7360c01d-e32c-32d1-b600-cc5cca8cb398 | -8.672 | -54.6828 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd3e37ee-8cdf-3303-94aa-505a211e35c2 | -6.1824 | -45.434101 | 2025-09-07 00:45:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7e374ce-b0c1-361c-af55-0ba5e62ee398 | -17.6759 | -43.5201 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 10e0c937-ca26-347d-9772-22e606741af6 | -5.7274 | -43.916401 | 2025-09-07 00:45:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b22f5ee-61a6-3303-b651-5eedd50605c9 | -13.0366 | -48.057701 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3595c4c3-0438-36cb-8936-4bf2142219d3 | -3.777 | -48.921001 | 2025-09-07 00:45:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3157b75-c4ee-32fc-a210-08021b352af4 | -7.7224 | -50.305801 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2bce931-9f95-3539-a700-13e2c247d440 | -19.474701 | -47.762901 | 2025-09-07 00:45:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 15f92327-7c75-3345-a127-9a36848b5446 | -19.476299 | -47.770401 | 2025-09-07 00:45:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a3f0be2-94cf-3683-9316-bff6ab042608 | -6.2001 | -42.6334 | 2025-09-07 00:45:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf5b2464-89cf-3d11-9bd2-67c80104146d | -13.8416 | -46.250702 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e469f26-2788-37ad-9c87-6eedfacd6ccc | -7.7256 | -50.32 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c9765e8-3919-3975-b11a-35666e63e404 | -5.7544 | -45.543701 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec56eea2-5cad-38e6-a848-7b67091613dd | -11.4668 | -55.540001 | 2025-09-07 00:45:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d734467-23b9-3eba-8a13-395f3c291ab2 | -17.003201 | -49.1726 | 2025-09-07 00:45:00 | METOP-C | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f59ef605-4198-30bb-b2ab-c10e22d864eb | -6.2721 | -53.438702 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604523ca-faa2-37b7-b35c-c860a956156e | -8.477 | -45.185398 | 2025-09-07 00:45:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99fa19f5-0950-35f3-a92e-42df58d2194c | -9.9659 | -51.658901 | 2025-09-07 00:45:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b630752d-2a3d-35f6-9ae7-42adf2a9e6a6 | -11.4085 | -43.6046 | 2025-09-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 7e13fa24-e070-3733-9efd-b12ca36cffb3 | -3.5995 | -47.5142 | 2025-09-07 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 42234266-3d92-36ed-a0c1-e49e6194b6e0 | -2.4263 | -49.3161 | 2025-09-07 00:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e50bc544-b0ec-3213-899f-715a628f7eb8 | -11.4772 | -55.563 | 2025-09-07 00:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 197fd06f-4f49-337b-9fd9-95b6c4474c75 | -9.3156 | -66.621 | 2025-09-07 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 21be70de-ff9d-3624-87d5-621255481955 | -7.7404 | -48.8204 | 2025-09-07 00:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e67a65af-a5cb-3037-ad1f-2235574a22d7 | -11.3888 | -43.6312 | 2025-09-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |


[Clique aqui para ver as próximas entradas](README14.md)
