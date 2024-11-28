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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f849908b-9cdb-35cc-8adf-48868eda7a44 | -20.32738 | -48.82309 | 2024-11-28 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8585991-5826-35d8-970f-1e8c5e5bafd5 | -22.53895 | -48.81208 | 2024-11-28 04:27:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec28c60d-aacf-3b00-bbce-ae72c9cd8b02 | -19.02182 | -57.62173 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f8e38a80-4119-39f8-8c71-e95497ad962f | -17.09471 | -44.9768 | 2024-11-28 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87442a04-026f-3339-8d36-6ea044622f49 | -21.50158 | -48.61261 | 2024-11-28 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab110527-c69c-36e4-a17c-b883162bf97f | -21.12031 | -48.65036 | 2024-11-28 04:27:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4d6bae81-1d18-355b-8310-5b2fc5917a78 | -21.82942 | -44.19176 | 2024-11-28 04:27:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0412e2bb-6d76-320a-b45a-6c233a3d6b27 | -24.10375 | -49.85251 | 2024-11-28 04:29:00 | NOAA-20 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 520e24df-856b-30fd-a282-8a361033ba7b | -24.10317 | -49.85629 | 2024-11-28 04:29:00 | NOAA-20 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f456653a-8afb-385e-bca2-a26bac1211f7 | -1.5897 | -52.271 | 2024-11-28 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 02d2f6bb-5f14-38f3-a1f9-eac22a189408 | -6.1735 | -42.6221 | 2024-11-28 04:30:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 572f3650-bd2f-3a2a-922c-f308680d6360 | -5.979 | -45.3395 | 2024-11-28 04:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| cb1deeb5-7c8a-31d0-a5a4-280af557abe2 | -6.1737 | -42.5985 | 2024-11-28 04:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 5325e7de-f723-3c33-a69e-1295a0a480cb | -3.3837 | -50.1125 | 2024-11-28 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d2cb4570-d969-388e-adc8-81eeea6b1438 | -5.9788 | -45.3621 | 2024-11-28 04:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 230.2 |
| ee2e4452-20dd-300c-a5de-5adaa655ad87 | -3.1113 | -53.8242 | 2024-11-28 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| da9cb0f7-29aa-3b31-81b6-5011140f422a | -3.2939 | -45.5144 | 2024-11-28 04:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2f6443c5-b272-38b6-8923-a5070b4e67b7 | -1.5897 | -52.271 | 2024-11-28 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 030e31be-ecd3-3c12-959e-f5accacc0958 | -6.1735 | -42.6221 | 2024-11-28 04:40:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| d36fdfbc-1300-3b5c-86a4-4530ff167392 | -5.979 | -45.3395 | 2024-11-28 04:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| a388820d-9f82-3c74-bf02-b8d8587d050e | -3.3837 | -50.1125 | 2024-11-28 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 209bb181-c8d5-3a57-828b-8eb6c4ccc6f8 | -2.7612 | -54.1142 | 2024-11-28 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3b7f2ebb-07ba-3034-a66f-36de75a9dcac | -5.9788 | -45.3621 | 2024-11-28 04:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 32334af6-64c7-31aa-8b58-b11fa5c478fb | -5.9788 | -45.3621 | 2024-11-28 04:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 202.8 |
| ccad69b3-1bbb-38e9-b0fd-b56329697455 | -5.979 | -45.3395 | 2024-11-28 04:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 76a29ea8-1e8e-3b2b-b6dd-47a2fb25a0c9 | -1.5897 | -52.271 | 2024-11-28 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d817acc5-8178-3fc0-a934-7ba8054b3126 | -6.1735 | -42.6221 | 2024-11-28 04:50:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| cf483964-9d29-3371-ab67-dca2481f8272 | -3.3837 | -50.1125 | 2024-11-28 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1dc0536e-5e53-370d-966c-9a9750181e68 | -5.9975 | -45.3607 | 2024-11-28 04:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f222054c-5ae7-3331-bc6c-edb42f4ced06 | -6.1735 | -42.6221 | 2024-11-28 05:00:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 68f65a0e-6037-36c8-85ea-162a3aa3aa19 | -1.5897 | -52.271 | 2024-11-28 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 535c4117-6921-3c5e-b088-7aa4dfd37c50 | -3.3837 | -50.1125 | 2024-11-28 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7a7dc96d-60bd-369b-b299-25fb3aff9db0 | -5.9788 | -45.3621 | 2024-11-28 05:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 208.8 |
| b4886adf-af7d-3a7f-bfee-fc22192ad8b1 | -5.979 | -45.3395 | 2024-11-28 05:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 0c63b449-b957-3520-839c-3fa92576ec34 | -6.82867 | -44.39561 | 2024-11-28 05:03:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3d019403-4aa4-326c-a04e-49fe1bcb1eb9 | -2.73214 | -48.88602 | 2024-11-28 05:03:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 1a1e5711-66bf-33e8-aa67-31bd1945a81a | -3.95589 | -50.18808 | 2024-11-28 05:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| cce352a2-c38a-3d17-815d-a40ac647eeae | -5.98505 | -45.35088 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 14354d8a-2cee-3f26-a620-ce50a2e9122a | -5.97427 | -45.34926 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 251.1 |
| c7f4adae-01ef-3f70-92ba-d3c2ab3f4e3a | -6.17206 | -42.60518 | 2024-11-28 05:03:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 547aa17e-b519-3e60-87a9-3b9a57030c27 | -5.98705 | -45.35778 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f9c1ec91-b599-36b8-b4ba-a20158f3b9b5 | -2.86359 | -46.85488 | 2024-11-28 05:03:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 54bc762b-24ec-380f-850e-dc7947f454f6 | -3.37567 | -45.83956 | 2024-11-28 05:03:00 | AQUA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 32.2 |
| bef12c6a-df13-3e12-8207-8d55b05ced84 | -3.28821 | -45.51263 | 2024-11-28 05:03:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5769b261-c393-3474-984e-fba56d348b22 | -3.37899 | -50.12312 | 2024-11-28 05:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ac86f1d7-c9d1-3c33-8ec2-004c2e75a0a1 | -4.77303 | -44.42297 | 2024-11-28 05:03:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e105f7ac-478a-3874-af6e-b71f65a5ca34 | -6.83043 | -44.38435 | 2024-11-28 05:03:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 93f6cc12-1215-30ec-9130-032f9101167a | -4.92672 | -45.41671 | 2024-11-28 05:03:00 | AQUA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b434ea70-d7fc-373b-a77b-67d2ddc2593b | -3.28976 | -45.50723 | 2024-11-28 05:03:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b732f24a-4c7c-3948-ab84-2a3f3f3df26b | -5.21759 | -44.91199 | 2024-11-28 05:03:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0d9c05a8-9e23-39db-b96b-77166a443dfd | -7.69504 | -42.96989 | 2024-11-28 05:03:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fec3295f-f71f-34f5-ac44-b897e0741ede | -6.08911 | -48.02536 | 2024-11-28 05:03:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 25ace19c-b97f-315e-a3a5-12a45a8178d3 | -3.96621 | -48.0759 | 2024-11-28 05:03:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3ea8eb7e-6500-3be7-8a63-ff20bc88878c | -3.38893 | -50.09602 | 2024-11-28 05:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cb6a9356-8e79-3af5-8804-4600084db5b1 | -5.82739 | -44.1049 | 2024-11-28 05:03:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9631b5c7-483b-3a11-9b49-f18066e9262d | -7.6936 | -42.97929 | 2024-11-28 05:03:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 40769283-9fc8-307e-b7ea-928c16a73b14 | -6.36932 | -45.69574 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6a66b36f-4890-346e-ac62-4ad16d98bf2e | -5.97219 | -45.36272 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 25589777-073b-3958-a7dd-479ee9a81211 | -3.95611 | -48.09361 | 2024-11-28 05:03:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3ad95af5-1756-3b4e-a9ae-38453c331545 | -3.19432 | -46.58735 | 2024-11-28 05:03:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9745e3b7-e7e3-3ace-8d2e-f47d46fcb589 | -7.03199 | -34.99812 | 2024-11-28 05:03:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| b3f11abe-3a9a-3f47-a146-a4c32d020e72 | -5.97842 | -45.34283 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 148620f3-3e47-3837-8481-a394ad800cbc | -4.80246 | -43.29601 | 2024-11-28 05:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1e51ce0b-465f-3819-b37e-a5fca780d037 | -6.16919 | -42.62395 | 2024-11-28 05:03:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| ba4ae6d0-cfbc-355b-bfa3-3a51cce535ee | -2.7334 | -48.8812 | 2024-11-28 05:03:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 94b5e05a-ec19-3b28-92f2-4c7ee7b8b1c5 | -3.08053 | -49.20413 | 2024-11-28 05:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| dc67f9a6-09a8-34e2-a60c-bf0410bd2809 | -5.21966 | -44.89909 | 2024-11-28 05:03:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 80c10647-f7fe-34cc-9cc1-3cb6f703aae7 | -3.19438 | -46.59488 | 2024-11-28 05:03:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ed152d8b-e53b-3d49-8598-abad0bf9a1a9 | -5.97409 | -45.36965 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bab55c78-f6fb-3512-9c35-1adb502b1581 | -6.16153 | -42.61322 | 2024-11-28 05:03:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 273e3903-4502-383a-a7b3-5509f88a22a0 | -5.97626 | -45.35618 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 248.6 |
| 58113e7d-01c8-38a0-ae81-ecb57ecac7d9 | -9.24429 | -35.45721 | 2024-11-28 05:03:00 | AQUA_M-M | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| dd5159cd-25a2-39ff-8b3c-6938e39743f6 | -6.10528 | -43.95619 | 2024-11-28 05:03:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1af6d8e0-ca30-3ab8-aa97-30a9760bee05 | -7.02861 | -35.01219 | 2024-11-28 05:03:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 8c71c249-993d-392f-a516-aa2b7a9c5125 | -6.16009 | -42.6226 | 2024-11-28 05:03:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 19e7184c-2f5b-37f0-8d31-ad159175f529 | -5.983 | -45.36424 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ec49353c-4162-30d9-8ef7-dcc5378e6fbb | -6.17062 | -42.61455 | 2024-11-28 05:03:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| afe0a4d3-bd32-31dd-a2e9-0d0126f87a18 | -5.22258 | -44.90714 | 2024-11-28 05:03:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1e01df2c-251c-3733-aca5-70d710b7ed72 | -6.10361 | -43.96712 | 2024-11-28 05:03:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5c1becd3-3612-37e3-a681-0d2a5b9666b1 | -6.37152 | -45.68162 | 2024-11-28 05:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 74a04834-7685-3041-8052-6bcf4ac3b543 | -3.38456 | -50.08766 | 2024-11-28 05:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a8993822-a27e-30e5-9f6b-a99595162877 | -7.03127 | -34.9929 | 2024-11-28 05:03:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| d49036f4-4ec5-32ec-be06-000bf0af1679 | -6.09151 | -48.04074 | 2024-11-28 05:03:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fb2ff005-eb89-30cb-8100-96ca859446fb | -6.09385 | -43.96572 | 2024-11-28 05:03:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| d53401d0-52c3-3f37-a0be-873da78e2f32 | -3.95983 | -48.06996 | 2024-11-28 05:03:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 9f342d66-0f1a-3317-a877-04e11fc18cb2 | -9.97875 | -44.08723 | 2024-11-28 05:05:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c5800ac-e6db-3332-9ac2-2f41bfe0ded8 | -3.3837 | -50.1125 | 2024-11-28 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 818b4656-cdf0-3202-ba43-00f48cf2f622 | -5.979 | -45.3395 | 2024-11-28 05:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 83cec133-baf4-39f9-ad73-261f168e91b7 | -6.1735 | -42.6221 | 2024-11-28 05:10:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 5e80a8c2-4dbb-36a2-888c-0cf3f2c581ff | -3.3852 | -45.8465 | 2024-11-28 05:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 24f7e83a-19d1-3a62-8820-8c47e93e212b | -5.9788 | -45.3621 | 2024-11-28 05:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 1ea3dcb6-d89a-3b5a-871e-96f75fe22e0f | -1.5897 | -52.271 | 2024-11-28 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 221e8a39-345a-3be0-9dc1-e84a50df8036 | -23.37011 | -47.06195 | 2024-11-28 05:10:00 | AQUA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| aba22f54-fb0f-363a-9c16-1a2ea1566893 | -23.71411 | -50.56395 | 2024-11-28 05:10:00 | AQUA_M-M | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| e382555f-7e98-3c14-ad6e-cb0fea069f1c | -23.7172 | -50.54737 | 2024-11-28 05:10:00 | AQUA_M-M | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 3dd8b795-4ab1-3c58-8375-4f5dc790a0b4 | -1.64351 | -52.10847 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17d82c9a-6bd4-38f4-b630-a52d88502e55 | -1.71539 | -52.4829 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c79bc0b-a956-3341-8e6d-e99d7dd5910e | -1.78132 | -52.73665 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 422bb984-1187-3298-a374-3cb796796210 | -1.04538 | -52.41261 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 296ca328-06e2-305f-a5c1-6567c7818557 | -1.43483 | -52.66729 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README73.md)
