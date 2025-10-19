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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0ae7985-537d-3331-863e-a7f13e3603f3 | -6.28711 | -46.64907 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88541e37-cf87-3ac8-9adb-c3343ff51b96 | -6.09575 | -44.02533 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab4d29f6-b4a3-3eda-bed2-ec5cbf26a828 | -9.97069 | -48.2395 | 2025-10-19 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b0f4cea-e3f8-30b2-9043-2589f922e63e | -12.18286 | -40.62136 | 2025-10-19 04:32:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6a2835c-c21e-3347-8bbf-d034f9771dd9 | -8.95703 | -44.92609 | 2025-10-19 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84bff3a9-7561-310c-91ac-ba7ec63915e1 | -8.4307 | -44.15407 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 429d4c2a-7d14-30e5-ba50-0bd698edb22b | -10.67754 | -47.42455 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61cf1a5f-8808-3e7f-b080-b90119bc1c4b | -12.32573 | -43.4375 | 2025-10-19 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 42a9400f-b34f-3b55-b4da-66a3951966a3 | -6.41926 | -43.92083 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db695d52-7d58-3c16-911b-8e887fad7187 | -6.40239 | -47.21429 | 2025-10-19 04:32:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f23d7a0-01e6-3933-b9d0-2b93e8e1933b | -7.41153 | -40.07903 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 62beb337-1356-372c-82f4-78c0d21dde1c | -10.2256 | -44.05423 | 2025-10-19 04:32:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 088b3648-51ad-32bc-ad1b-80ce8c129744 | -10.3994 | -49.20102 | 2025-10-19 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ec08588-f36f-315f-b15d-ec9e52525e48 | -10.72711 | -44.54171 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8fee325-d50d-3675-8d55-f43d730a4bac | -7.71344 | -46.6038 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5a31aa2-ea4b-3b3f-ae4a-5eefaaab7409 | -5.88139 | -49.86806 | 2025-10-19 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d11cf9f1-a300-3840-aa64-332580b54730 | -9.21928 | -46.05723 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9a471da-8004-3c8b-87e9-f68a7fd85a7e | -12.46959 | -45.43219 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea449329-4d99-36ed-b513-c447e65e0e32 | -5.90866 | -44.25048 | 2025-10-19 04:32:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6e6ff2f-b9a2-3f6a-8d75-55710c18614c | -6.3576 | -45.74458 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 790ec5ff-cc0f-3bf1-bf32-168b1d77bdcc | -6.36386 | -45.74943 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7545cbb-6d67-384b-b4c7-dc332f0ca3e7 | -8.17412 | -46.86883 | 2025-10-19 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e32ab6f2-c519-3811-8096-4b6544ad41af | -8.2491 | -43.32486 | 2025-10-19 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd344a50-5cfb-3b78-8341-0b1ff98ba212 | -5.71383 | -46.51324 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32653e53-1ca2-38ca-a446-2106e3afc79f | -10.8826 | -47.90215 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f9f29ef-b84c-3f4d-aa58-147867dd9564 | -5.35576 | -47.21588 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 33105965-5444-33bc-8382-42ea6ddd5b8d | -10.55843 | -49.79855 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c192bed-5e27-3aa0-9431-bc9129c4216b | -8.23915 | -43.98756 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8d76f4d-599b-37dc-977d-f48ed09b0580 | -7.16028 | -42.38052 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7d800222-4f60-322e-af6e-bc530ba0b05f | -5.93227 | -42.25119 | 2025-10-19 04:32:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d213c82f-e518-32ab-9e7a-59d25b1abbaf | -10.89133 | -46.07255 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e95fa71-cb7f-348a-b507-c410b6eef12b | -7.94361 | -46.01922 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f7d73b6-9fa3-3cf7-9557-0abcbcf2f2ec | -8.54383 | -50.08334 | 2025-10-19 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22ff56c0-d6db-3c16-88b7-6b21a10932f2 | -5.48156 | -48.64948 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6375acd8-6252-3c03-845d-eccc2fae436a | -9.9998 | -48.0758 | 2025-10-19 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aabd640f-260a-3627-a05c-a616f2f2309a | -6.15181 | -44.30032 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8990e4c-9249-36a1-80e2-f48e3ccc6dd8 | -7.0048 | -47.42308 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0870ff99-66bc-3808-a0b6-442f56b4931e | -7.94377 | -46.01944 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fdb276e-3476-3a47-9c00-608d39251db0 | -9.90879 | -47.65833 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65eae505-e933-3fac-ad72-6b7086029a4e | -9.74976 | -43.96315 | 2025-10-19 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d06c2478-d472-3ca7-adcc-d15e17494424 | -5.25962 | -50.90708 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0874a065-4f5d-36d5-b92b-11ab9614e372 | -5.36346 | -47.21002 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b8e238ba-7328-3eac-93cb-86a65b13e286 | -8.43515 | -44.15264 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66f25d13-c2e8-3930-aa2e-99d626a9166d | -10.22631 | -44.04921 | 2025-10-19 04:32:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9c9035c-1c12-34d6-9d39-202559d440c1 | -6.99697 | -48.50494 | 2025-10-19 04:32:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dbb0878d-50a6-3cf7-b0dd-3c4ef9458341 | -5.75982 | -44.00292 | 2025-10-19 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62b9802d-d985-37de-96be-a57b7d3e9850 | -8.41767 | -44.13805 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3f098b8-1b26-3efb-9b6b-ce0e9ad68426 | -5.10491 | -47.79458 | 2025-10-19 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 5a00e438-50c6-3e3b-81c1-987dac8e8c45 | -9.23312 | -46.05939 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8bbd5f9-251b-31a3-a96d-888c9815eb0e | -8.00916 | -45.14615 | 2025-10-19 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 884bf4e1-eb7f-3921-bd82-d3b5a7ffdddf | -12.49795 | -45.41833 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1964373f-d921-3ca5-a265-27b790456f97 | -8.51532 | -49.50407 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc899233-6a2e-3891-9848-fc1e3522bb85 | -10.54668 | -45.03642 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccc2ae0d-917b-3747-b2fe-792f463573ac | -9.09107 | -47.78489 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4c77c14-9c04-3b6d-94c1-1b5a9e945b3c | -10.87963 | -47.45555 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d66518f0-9bb3-3982-9d6f-5aa56326437e | -8.21534 | -43.96486 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 559de5ac-d997-382f-a13b-7a1f9a33bbb7 | -5.36439 | -45.27871 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d067591-aca1-3e4e-8c4c-ca115c20f56b | -10.8878 | -46.09638 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1313a7bd-f5c4-3eb3-bfbd-9234342cf89f | -10.45148 | -45.02376 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 08cc863a-dcd5-374d-826f-48aaceaf32f8 | -6.36727 | -45.74998 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95b73111-7dfb-3d24-b834-1d2c5b0e0e64 | -6.32678 | -44.30383 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 07acecf8-da27-30f9-b3a0-36f7a116d9e8 | -12.32734 | -43.43685 | 2025-10-19 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 327d9b6d-6a2e-334c-8b27-225a077c0640 | -9.93744 | -47.12546 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a11a89c-a7cc-3a94-9fb9-3bebcbfa9eb3 | -7.16776 | -46.92298 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3cf6d82-168b-35d6-888a-27bd00fe664b | -8.56532 | -48.51329 | 2025-10-19 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b3170017-237a-3fd8-979e-8708059c1021 | -7.4123 | -40.07366 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a65002bc-4bbc-3713-8d7d-eaad06358789 | -6.33707 | -44.30969 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0abdcaa-cfbb-3a83-9eff-16a5942b7335 | -11.34877 | -44.28317 | 2025-10-19 04:32:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30696103-01d2-39bf-b2ea-8a99ed64ad83 | -6.4397 | -43.9218 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0651ec9d-e7aa-3118-b5c5-7d0ff5783cd3 | -6.87009 | -47.99726 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a085e829-2b37-3604-a64d-a07762e1d594 | -11.00416 | -47.88538 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9920c23-eb99-3e3a-b87c-84992159a5ff | -10.68601 | -47.94398 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a1bd2c58-c7c9-327e-995c-194fce5afa08 | -6.12662 | -44.21894 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74e72314-2f0a-3232-a460-86d075611967 | -5.52925 | -46.1914 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c97c2e3-22c7-338a-bacf-65d24323351f | -10.97736 | -42.29681 | 2025-10-19 04:32:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de602d96-a871-30fd-9746-67c80cb4f7d8 | -7.36874 | -41.95495 | 2025-10-19 04:32:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 85158547-2a1b-3e95-98d7-8ea34132af78 | -5.54556 | -46.52719 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c756b737-2547-3064-848e-aef1739a690f | -7.16304 | -42.36182 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4e05a010-93a1-3598-b9ff-7f60280b776c | -6.7247 | -46.31942 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb862613-874f-3e3d-b5e9-a955f9155920 | -6.15118 | -44.30451 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd1f39de-3e3a-3e24-9351-c350e7b9340d | -11.62806 | -44.09201 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 048c584d-cec4-381f-8e39-d6f690b7a2b5 | -10.09815 | -44.56212 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2f03afc-7879-3125-b70d-ecc51b219944 | -6.3764 | -45.75892 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3d786cbd-2a37-33a8-86c6-b77f0b2b6b63 | -7.19449 | -42.20656 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f4d4586-a3ca-3cd4-b427-3c90985345db | -5.7586 | -44.00537 | 2025-10-19 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1033434b-79a4-3384-8486-17e8a7657664 | -5.36502 | -44.93895 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ccbcd61-8dd0-3d6f-8d3e-e6f55d913c9e | -5.93582 | -42.2556 | 2025-10-19 04:32:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f6392c3a-8a9d-3fc2-af32-98597498dd9b | -10.98982 | -47.93378 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0d25f6c-c690-35fb-8e28-c8d03ec50654 | -5.89575 | -43.91369 | 2025-10-19 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d233b1c-09b9-37be-9526-eaccac76bf7d | -9.75365 | -43.96369 | 2025-10-19 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcf7260d-e556-38fd-bc72-f51aeb62e9d5 | -6.30689 | -43.98552 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 292ef62e-f9a3-331d-9e59-93f2ed3b99d8 | -8.43448 | -44.15454 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db31ee2e-7ed2-3921-813c-e4e4b8b87be4 | -6.21548 | -44.67382 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67f2e3ac-740e-35dd-a993-318ba12b8cdb | -5.75614 | -44.00235 | 2025-10-19 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74763700-56e7-3d91-841b-4e1952d27c10 | -10.92342 | -47.9885 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a904a794-bcc9-3f45-b1cf-c94e560469d5 | -5.29716 | -45.07859 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a861564-fc50-38ce-b32e-8be6ee7557ab | -10.95339 | -45.46621 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80fdbb05-e967-32ec-8744-f5f6b8bb2643 | -8.61868 | -40.19359 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 82b5fb18-e9d8-3d5a-97d8-6e6c27646bd6 | -5.20831 | -49.25496 | 2025-10-19 04:32:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60d951ae-f842-3f76-a901-8e0283477dc9 | -7.12388 | -46.15813 | 2025-10-19 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README52.md)
