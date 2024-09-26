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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca059f73-6341-3d35-bdcf-9c09c0219453 | -20.6279 | -51.5169 | 2024-09-26 03:17:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.9 |
| cdd52e68-fef4-3505-a308-8ca0dc3bd1fb | -20.6284 | -51.4945 | 2024-09-26 03:17:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| fb4a0230-b5b0-3915-9ea6-a68699d1ed2b | -21.9374 | -48.5688 | 2024-09-26 03:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9b202080-5322-38ac-bb9c-614d7d995ed7 | -21.9381 | -48.5453 | 2024-09-26 03:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 744d7039-187e-3318-96be-efa04fff803e | -22.2162 | -47.5603 | 2024-09-26 03:17:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.3 |
| 6fac674f-001e-39d4-acf2-d459597ac297 | -19.04838 | -42.73134 | 2024-09-26 03:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 961c3014-9a50-3435-9395-47d85b8788b1 | -16.32751 | -45.67742 | 2024-09-26 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c2305f8-5b8b-31c5-b4eb-209555f6ab7c | -19.67912 | -42.43699 | 2024-09-26 03:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0393df72-0103-33f1-bbcf-91793b6dc071 | -19.67827 | -42.44098 | 2024-09-26 03:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 020da243-d1e0-36f8-855c-76498184c5d3 | -19.6736 | -42.43564 | 2024-09-26 03:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 617fd30c-2511-31c3-861b-7fbbdfb22419 | -19.67275 | -42.43957 | 2024-09-26 03:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 197016ae-b7ca-3f32-80e0-df9debb8a0bc | -16.65184 | -41.89728 | 2024-09-26 03:19:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9c288691-f6ed-3046-b9f5-627807c8a5f6 | -16.75148 | -42.47283 | 2024-09-26 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97ea8ea9-0ef7-3155-8db1-c16508fb64d8 | -16.75242 | -42.46849 | 2024-09-26 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9402c9bd-7e07-3f0b-8036-f5acbb5ca22c | -16.75733 | -42.47427 | 2024-09-26 03:19:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a622e6b1-a2c0-3b09-b740-6d1a2869e216 | -16.75827 | -42.46991 | 2024-09-26 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7025b66-1968-3448-b594-09bb63515411 | -17.04959 | -41.15434 | 2024-09-26 03:19:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 35ef23e2-5b5a-38bc-b137-bd198c57f2c2 | -17.05032 | -41.15081 | 2024-09-26 03:19:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c1a130ac-b429-3051-a8ab-4c3a12558187 | -17.05425 | -41.159 | 2024-09-26 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 917f900a-9e6e-3db4-a949-2bd877d2027e | -17.05508 | -41.15501 | 2024-09-26 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 943ab88b-bed6-36f5-89e2-19909b9102be | -17.56157 | -42.86092 | 2024-09-26 03:19:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43be7b9a-3d04-3cba-a178-1056945d8cdd | -17.79043 | -43.24624 | 2024-09-26 03:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90a708b1-3661-3530-afeb-a9de426ef834 | -17.79628 | -43.24842 | 2024-09-26 03:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0379454c-de84-3806-93ca-2aaf089b88d9 | -17.79723 | -43.24414 | 2024-09-26 03:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c427398e-63c8-329a-9c99-545849d3ed92 | -17.84268 | -44.45786 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16b34d91-5446-3f3e-ba78-ddf0972297bf | -17.84909 | -44.45956 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e445d14-fa40-30a8-97b2-b24d50770561 | -17.90784 | -44.20247 | 2024-09-26 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70bff8b1-02a0-3b94-a38a-f65d21d71c43 | -17.90893 | -44.19768 | 2024-09-26 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f50c670-8697-3dcd-b97d-2282951981b1 | -17.92623 | -44.27465 | 2024-09-26 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6534698d-cb74-37af-8f04-02b8977e9c92 | -17.92746 | -44.26939 | 2024-09-26 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36f43425-f4e6-33f1-bc30-99859fc92cdc | -17.9812 | -44.47564 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03682bdb-4adc-3192-bb79-648cd72ca544 | -17.98405 | -44.46313 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39cec93d-a518-36e1-84be-9835bb1e92fb | -17.98441 | -42.30843 | 2024-09-26 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a1a09192-ae24-32c0-b3d1-6461b0f569ee | -17.9853 | -42.30433 | 2024-09-26 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0242f18e-250a-3195-b273-dbc7868c2707 | -17.98617 | -42.30033 | 2024-09-26 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ac12841d-f309-30c1-a474-6526fa2f542e | -17.98775 | -44.4767 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5ab4eb18-e7d2-36d9-8bb8-ef52039fd07e | -17.98792 | -44.47557 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 07ac6a6e-a206-3c7e-b5c4-eb2943cc4792 | -17.98907 | -44.47087 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0173e9f-abf1-327f-9211-314bd2de5ae2 | -17.98929 | -44.46972 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 293b874b-f4d9-3362-968b-33071362d1fc | -17.99043 | -44.46488 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df086f2a-ba85-3d32-abe4-dabc2949bc63 | -17.99069 | -44.46374 | 2024-09-26 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0678f3e9-ebb7-3fb6-a984-4bfbe9576f83 | -17.99092 | -42.30586 | 2024-09-26 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 08ccfa71-fea7-3f3a-8257-3892640eeace | -17.99181 | -42.30181 | 2024-09-26 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e02caea3-da3a-33c3-bf81-6e984c0c5473 | -18.0107 | -44.34599 | 2024-09-26 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12ba1792-a871-345b-9eb5-4c51f711204c | -18.01719 | -44.34705 | 2024-09-26 03:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dc31a09-4379-330f-8973-ee7c8e0df366 | -18.02014 | -44.39351 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66d9524e-a25c-3a3c-88c6-27e76cbf0f97 | -18.02084 | -44.3927 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b808081-a604-3ce0-840b-0af65d743b6e | -18.02769 | -44.38997 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd0bb583-9cc2-347e-95ae-65a8aa7bda24 | -19.04923 | -42.72299 | 2024-09-26 03:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 82dac6de-af3a-3786-8989-4a98a99d5279 | -19.04999 | -42.72413 | 2024-09-26 03:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b5cc13b0-fee7-3a6d-be68-f276fd7c2b4f | -19.18884 | -42.58126 | 2024-09-26 03:19:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 643680e2-3bbc-3dab-85ae-41bb55ab914c | -19.25998 | -42.72806 | 2024-09-26 03:19:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cc0e8f55-6df2-327c-a566-63b00261a950 | -19.26066 | -42.73125 | 2024-09-26 03:19:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| da0d4eb8-8a34-33ac-a4b5-4c89b2734bf3 | -19.26077 | -42.72442 | 2024-09-26 03:19:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6421ceab-b8be-327a-adf0-6dfc9b81620e | -19.26158 | -42.72718 | 2024-09-26 03:19:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7bd67ac6-28af-3fa4-aacd-1ec5203023d7 | -19.26487 | -42.73303 | 2024-09-26 03:19:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 74b736d9-d60b-3d91-bbe7-d54f14a52323 | -19.26583 | -42.72863 | 2024-09-26 03:19:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 67edab17-5f6a-39ec-bc26-5c3200f74646 | -19.43772 | -40.78692 | 2024-09-26 03:19:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fca30051-6be7-371c-9aca-d3109f690945 | -19.44213 | -40.79103 | 2024-09-26 03:19:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 81210109-4a6a-3c9f-a9e4-39c53ebf5ab8 | -19.44269 | -40.78831 | 2024-09-26 03:19:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1232aaa6-89a2-313e-ab9a-91bb36e333d0 | -19.46374 | -40.90619 | 2024-09-26 03:19:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 05e80f9b-7eef-352a-8347-05f2a94a7978 | -19.55309 | -42.69211 | 2024-09-26 03:19:00 | NOAA-21 | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 60e9b27d-34d6-370e-bbac-b5d3dc723bb9 | -19.55395 | -42.68819 | 2024-09-26 03:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 2e511f9f-5710-3109-9ff0-6eb699e7c49a | -19.56027 | -39.94598 | 2024-09-26 03:19:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5a154cad-1f97-3689-908d-4640018f924f | -19.56802 | -42.59767 | 2024-09-26 03:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d1567687-2eb7-3b9a-b2e1-ccfe6e16cc1a | -19.57362 | -42.59901 | 2024-09-26 03:19:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cce996b6-beba-3e76-91c9-98ae945038bd | -18.02843 | -44.38908 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 707d4958-d8b6-31c3-aefa-38f98892fc95 | -18.02884 | -44.38486 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| afef88ae-88ce-35b7-a64b-95769ca8cee3 | -18.02962 | -44.38395 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 784b02ef-c967-321c-9b4b-aada03de534a | -18.04339 | -44.35023 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6260c23-0475-3882-abcc-7c8dbc842bdb | -18.04441 | -44.34928 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06dfaaeb-7a79-3c9e-82cd-e2985e192b0f | -18.04875 | -44.3563 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8c5ce5f-2282-3208-a05c-e9e521a055ad | -18.0497 | -44.35553 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0aeb38c2-5049-36a6-ac46-32208083bf75 | -18.04982 | -44.35152 | 2024-09-26 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d72e8cad-a363-34a3-aad3-f88768e1f4b5 | -18.15515 | -42.77465 | 2024-09-26 03:19:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8a0f8700-2d17-37c0-b65b-6155dd02066d | -18.25329 | -41.31628 | 2024-09-26 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b7e0d01e-a911-3b87-8c69-9be4adafd243 | -18.25402 | -41.31279 | 2024-09-26 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e8eb7861-01d7-3468-9d3f-57c79d6583ed | -18.25796 | -41.32059 | 2024-09-26 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 6cc742f9-e97f-34f0-a60a-343b2a1f13a5 | -18.25869 | -41.3171 | 2024-09-26 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ce0138f6-91f9-3ddd-ba7b-567b0d464716 | -18.2594 | -41.31367 | 2024-09-26 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2e27a2c5-6997-3358-a87b-b451d6ef68fc | -18.26677 | -42.67747 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7dd0514-33c5-31be-a7fc-2d94572f5836 | -18.27143 | -42.68392 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fc6bc1ee-3d75-3192-bc33-0c120ee396c2 | -18.27245 | -42.67924 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85374c0b-f071-3b1f-bc8f-fbe15db4bf4e | -18.2966 | -42.18664 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f1abb75d-47a1-38dd-b516-9373e5be0987 | -18.29915 | -42.18797 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| de2b0a8b-4cdf-3602-98b8-204baf7f20f2 | -18.29996 | -42.18417 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 524e65af-0fdf-387b-8654-e581dd9d4f58 | -18.38437 | -42.80076 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 20a264f7-d399-3a5c-b910-26dca4676b74 | -18.38546 | -42.79589 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 83c1af0c-543f-39e6-bbaf-b8137f5a5bfa | -18.38657 | -42.79522 | 2024-09-26 03:19:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31761af1-ddc2-3502-bb8f-6c00f724a5f3 | -18.42827 | -45.1024 | 2024-09-26 03:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a24c56d-c6b7-39f5-9d46-26e30f48dca2 | -18.42972 | -45.09608 | 2024-09-26 03:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f8d4a0c-5f38-3a81-b810-2850fe0a33da | -18.48653 | -42.86363 | 2024-09-26 03:19:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 92cd73f3-9127-334b-a247-48d185c735dd | -18.50048 | -42.96133 | 2024-09-26 03:19:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 3e32dd8e-b7c2-3a37-8b5c-825ccda688d1 | -18.50149 | -42.95678 | 2024-09-26 03:19:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 1baa3ad3-3c43-3f5f-a83a-bc39ecf5705c | -18.56773 | -41.32285 | 2024-09-26 03:19:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| df3bc69f-bf7b-3e49-bfb4-a7339972ce67 | -18.56849 | -41.31923 | 2024-09-26 03:19:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1e5bf1f9-7d14-35bf-af12-a9ec6c124f2d | -18.57302 | -41.32404 | 2024-09-26 03:19:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b8a99507-0fe0-3f40-b719-794aa7f5944e | -18.58541 | -41.64976 | 2024-09-26 03:19:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cf0142e1-452c-3ae5-b747-9543e2039564 | -18.86096 | -43.43837 | 2024-09-26 03:19:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e2ddd160-ff9e-33d4-8731-da70d90112f4 | -18.86188 | -43.43425 | 2024-09-26 03:19:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |


[Clique aqui para ver as próximas entradas](README51.md)
