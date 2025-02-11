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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 238404bd-0f5e-34fc-94c2-4805180a82dc | -6.97884 | -42.99346 | 2025-02-11 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2bcb32c-f389-33e0-a5a6-fc6505e60a77 | -7.24083 | -44.71262 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c577da9-5f94-3706-94de-e92cc71bda41 | -7.23368 | -44.71504 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 371988f8-e8f9-30b3-afae-97f990f76d6a | -8.35495 | -45.18766 | 2025-02-11 04:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d87f24aa-da9c-3067-a56e-0f41917f9fd9 | -7.23037 | -44.71452 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c0124f-0472-3371-a610-4adac6a860e5 | -6.97036 | -42.82057 | 2025-02-11 04:18:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fffdc564-86f1-3b5b-9a0c-283b9a08a787 | -7.91769 | -44.88028 | 2025-02-11 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abbc8615-1e9c-3e23-8bc4-ac4a863c3cb4 | -6.97322 | -42.82484 | 2025-02-11 04:18:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 16824e56-7e04-3285-b7fb-04f00fcd5136 | -7.07539 | -44.38138 | 2025-02-11 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e5329a2-b364-3e29-8d1e-f42e44499a43 | -7.921 | -44.8808 | 2025-02-11 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f19bdec-3cc5-3682-86cf-90bca57277fc | -8.48464 | -44.62036 | 2025-02-11 04:18:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b7796cd-a587-3c4a-abb6-303bc4fbc948 | -6.97379 | -42.8211 | 2025-02-11 04:18:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c87abb2-e9c5-3531-ac5a-07c4174378e8 | -8.70667 | -36.16368 | 2025-02-11 04:18:00 | NOAA-20 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 71185657-5238-36d1-98c5-83a20d02a079 | -7.25075 | -44.71418 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a770ffe7-3614-327b-9069-5566062cc3b6 | -7.25129 | -44.71072 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1566af3-8b05-37aa-a294-a608aabba295 | -7.08642 | -44.37596 | 2025-02-11 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47e515ab-9bfa-3cce-9335-4becd55f9bc7 | -8.35165 | -45.18713 | 2025-02-11 04:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16b060ee-7cc6-34cc-8f24-d9ae999c15d1 | -6.53155 | -43.09941 | 2025-02-11 04:18:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d74f1c07-f41e-3e8e-bdad-52a76a44503f | -7.24635 | -44.72059 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90ca7839-9a2d-32b2-a07e-23d035f60c93 | -6.97665 | -42.82536 | 2025-02-11 04:18:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28839369-97ca-3143-a475-79ac25282984 | -8.35826 | -45.18818 | 2025-02-11 04:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1080fa1c-03df-3c42-8f41-4470fe7ebb9a | -7.24029 | -44.71608 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c37ee72-a9d2-319f-8426-e0c29182d0e8 | -7.24305 | -44.72007 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 351aecd3-5407-3963-a27a-2695bf737088 | -6.7356 | -39.99451 | 2025-02-11 04:18:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d22a8e28-0a5f-3eb2-a1ff-3fa9f1babbfb | -4.70909 | -38.46704 | 2025-02-11 04:18:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7df0ffcb-9f4e-3b72-88b5-a55f11f04708 | -7.2469 | -44.71712 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6db1d99-19b4-324a-923e-de8a15dc7ae7 | -7.23974 | -44.71955 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 861f84af-dfb5-3f65-9539-e92e046b0c50 | -6.98225 | -42.99398 | 2025-02-11 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9f4e5aa5-e1c4-3c16-8a68-2e1f5fbf215e | -10.53715 | -44.67518 | 2025-02-11 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfdd9386-b402-3e38-9ec4-533484e0c252 | -16.26533 | -45.08746 | 2025-02-11 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdd09cd9-dfa3-3bc3-ab50-6d0d11c58b3a | -11.76435 | -44.30423 | 2025-02-11 04:21:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11057079-87c4-30e8-99c6-83a3a365aafc | -12.84663 | -43.82402 | 2025-02-11 04:21:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5790866-5cc7-3891-883f-88803503c615 | -12.89394 | -45.05484 | 2025-02-11 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09937e3b-ec7b-3b7c-b771-484d35e7b2df | -13.48263 | -44.01732 | 2025-02-11 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a16da26b-b973-3b5b-9c70-72f59dce5df3 | -10.53659 | -44.67874 | 2025-02-11 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24ff7bb6-03f6-3e20-94c4-74aff3bec632 | -12.89114 | -45.05069 | 2025-02-11 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 854bcce4-406c-3462-93c2-96fcf2f9a6c5 | -12.8501 | -43.82457 | 2025-02-11 04:21:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56c89fb0-f48a-3a32-b0d6-b4e72fe86fcf | -9.87803 | -41.80179 | 2025-02-11 04:21:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e299eb22-52be-3ece-a3a4-8d63f5e43472 | -16.68054 | -43.88576 | 2025-02-11 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2556f0bd-ba02-312c-bf3d-01c548e181a2 | -12.49354 | -43.78521 | 2025-02-11 04:21:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1ae3183-cf04-3476-80a9-6668298096ef | -11.76718 | -44.30845 | 2025-02-11 04:21:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c093a2c-29fc-38c3-8c87-9105be554f9b | -11.8262 | -44.22263 | 2025-02-11 04:21:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a67672b4-0d9d-381e-8aee-a57d90a995bb | -16.10791 | -46.20191 | 2025-02-11 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3742cfe6-5067-3b8e-9651-88152905e479 | -9.87869 | -41.79733 | 2025-02-11 04:21:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0db80add-8bbf-3088-a490-bdd37c2a9f05 | -12.84495 | -43.82468 | 2025-02-11 04:21:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ef524bf7-e19c-34df-8e09-500e8e1e5696 | -16.59164 | -44.08269 | 2025-02-11 04:21:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2fa979d-527a-3aa4-ac5f-3df8f215ed25 | -11.76774 | -44.30475 | 2025-02-11 04:21:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69245e08-af10-3443-bacc-bb6762f3847f | -20.28331 | -55.00091 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cce2d221-9212-31ba-bdab-bedc5be601a4 | -20.28682 | -55.00663 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7864a7b-dca5-3348-b6da-44432052e06e | -18.53624 | -39.93279 | 2025-02-11 04:23:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f6597108-e330-370e-abe7-dbe7c1aa3b4d | -20.24715 | -54.15088 | 2025-02-11 04:23:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08dbf712-f586-388e-85cf-c1adc80e82ca | -18.53761 | -39.93326 | 2025-02-11 04:23:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b17a93c0-063e-3337-bfb5-fc1e22d0a795 | -21.05251 | -48.4744 | 2025-02-11 04:23:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 418d121a-2036-3374-857a-d46c6501c432 | -18.53152 | -39.93219 | 2025-02-11 04:23:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8dda4a73-4db8-37e8-b415-118b18e67733 | -21.47185 | -48.57198 | 2025-02-11 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c085fbc-7cd5-3f10-909e-1f5f6160713b | -27.15676 | -50.6531 | 2025-02-11 04:23:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3bdc3532-f67a-3839-ab16-de0327272f5b | -18.53289 | -39.93266 | 2025-02-11 04:23:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ff84fc0b-dbd2-3b99-815e-5eebf81a4982 | -21.60336 | -48.45042 | 2025-02-11 04:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bab4edd8-89a2-33e1-904d-cfa97c77f59c | -21.49346 | -48.77803 | 2025-02-11 04:23:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ca18d69-0ca2-395b-a9ed-617a92b2bbb3 | -19.7592 | -54.79736 | 2025-02-11 04:23:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7ccfb75-f32e-38a1-a116-853e08eed86a | -20.28773 | -55.00198 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ce83b6b-2cf9-39dc-b499-47da5d776901 | -21.20559 | -55.75533 | 2025-02-11 04:23:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87f3f13a-33ca-34c9-89d1-de233a0c5843 | -20.28421 | -54.99627 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45e948bf-fae3-3e34-bbbc-bd779d46fe1c | -16.46049 | -46.22617 | 2025-02-11 04:23:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cdcffbe-273e-306a-821b-88ef5ccc5204 | -21.60667 | -48.45102 | 2025-02-11 04:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84c76a84-4447-3c72-b07c-c46226cba233 | -21.04919 | -48.47379 | 2025-02-11 04:23:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79fe3d58-a4c1-3dce-8b6e-cdf9110f3496 | -21.44297 | -48.68869 | 2025-02-11 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0586dad0-13bc-32d1-b835-727dcc089abc | -19.02258 | -57.6259 | 2025-02-11 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f0615b43-3609-3ae6-82f2-662fcac52d60 | -20.47716 | -47.53242 | 2025-02-11 04:23:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3c13a24-4355-379f-9a82-6cad7c8880e8 | -20.52889 | -48.8385 | 2025-02-11 04:23:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2cab87df-0172-3e28-a7ed-f6894fdb4caa | -20.75148 | -53.9584 | 2025-02-11 04:23:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baec9a00-c80d-3c08-a3af-bd68f55fb8c2 | -19.02333 | -57.62243 | 2025-02-11 04:23:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e786af1e-7f07-3da6-99e8-1e523b897e6f | -20.28864 | -54.99733 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49adc0df-5c14-30d8-8d67-dec531b3c3db | -18.62508 | -40.34971 | 2025-02-11 04:23:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 766d04b7-0d94-3684-9652-1585f94dcaf4 | -20.48048 | -47.53299 | 2025-02-11 04:23:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe063e2b-be30-39fa-aefa-e9c607b50490 | -21.51938 | -47.14841 | 2025-02-11 04:23:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e02812dc-b69c-3949-b6c0-783ad7b2efa8 | -18.76818 | -39.86298 | 2025-02-11 04:23:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ea1286ba-03a0-3495-8747-7864e49c1864 | -21.04861 | -48.47748 | 2025-02-11 04:23:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae24e38c-4412-3e2e-ab54-65da95035ecc | -28.58559 | -49.44127 | 2025-02-11 04:23:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d3407238-f47f-35f1-a833-e92bc2842322 | -19.07421 | -46.21059 | 2025-02-11 04:23:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3faaa9a1-553e-3ff9-8536-289c3bc279b2 | -21.43965 | -48.68809 | 2025-02-11 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59db2be1-2dd3-3f97-a5dc-b3d1e20885c7 | -21.89049 | -53.71725 | 2025-02-11 04:23:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b013aa7-5a1a-3aea-a5d1-498bfa717f29 | -27.82866 | -50.30431 | 2025-02-11 04:23:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4365fec7-9c7b-3728-b1ab-5c399f31859b | -20.48105 | -47.52931 | 2025-02-11 04:23:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d550132f-d2d8-34fd-9cb0-cda8d1894612 | -21.0603 | -48.46821 | 2025-02-11 04:23:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1846c3af-e114-3577-a775-4fadaf4322b7 | -28.86264 | -50.8733 | 2025-02-11 04:23:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ad7780f9-51f5-3470-9f3d-389eef29797e | -20.72451 | -54.60815 | 2025-02-11 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15fb94e7-e946-3406-a818-9a8ed391faf5 | -21.07598 | -56.39057 | 2025-02-11 04:23:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8b06b28-8076-3259-99ac-8e8d5fd6f7b2 | -21.49678 | -48.77864 | 2025-02-11 04:23:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8059d9fe-9767-3cc7-9d63-30df37e24d26 | -20.52497 | -48.84161 | 2025-02-11 04:23:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6b5bf6f8-bc17-3661-bdca-ad53ceb84ead | -18.76862 | -39.86449 | 2025-02-11 04:23:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fc963e27-f9eb-36e6-845e-26bb1f66e27f | -28.862 | -50.8773 | 2025-02-11 04:23:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c87d6e7a-9790-3b8b-bc79-95078c59ccdd | -26.57512 | -51.02259 | 2025-02-11 04:23:00 | NOAA-20 | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 330ea06a-59ce-3131-821a-d05802f3a354 | -22.33919 | -55.04602 | 2025-02-11 04:23:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d83ad71-ea6d-3a61-b8bb-e8c515dab039 | -23.40649 | -46.55661 | 2025-02-11 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6cf39400-b134-3b45-8cc3-c7b7d4e11831 | -21.35614 | -48.61622 | 2025-02-11 04:23:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 38bc0a53-7859-3848-830a-aa105db46813 | -20.56495 | -55.09105 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed277a18-9966-346b-a5e0-272eb9a59186 | -23.59339 | -47.43795 | 2025-02-11 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 479755c0-b22d-375c-86e3-e6da27c20880 | -20.13095 | -50.49477 | 2025-02-11 04:23:00 | NOAA-20 | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f1cfc3b2-9707-3f36-9e4f-bc3803c7514f | -21.05581 | -48.475 | 2025-02-11 04:23:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README4.md)
