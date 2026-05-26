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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8d8ccab-1af7-3a5b-bdd2-071e8ac4f98e | -20.91595 | -46.78981 | 2026-05-26 03:40:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2afe0346-c11c-3c9c-9044-9b07632f154e | -18.29504 | -40.14491 | 2026-05-26 03:40:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ee46330-1404-3f7f-a297-2927dde09c4f | -20.92117 | -46.7914 | 2026-05-26 03:40:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 302199d3-d7a2-3f02-85df-1f3f85cbee3f | -21.31983 | -47.07234 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| feb99650-46d1-3e4b-a5fd-21572f4acb72 | -18.08265 | -46.8756 | 2026-05-26 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca75412b-0a6d-360a-aa25-50bee09be8c6 | -21.32272 | -47.06978 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f0533d8-eaa7-3ad6-a33f-a3f201930d3e | -18.0847 | -46.88148 | 2026-05-26 03:40:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55f3112e-33a5-3f55-a36b-f4968bc27b60 | -21.32191 | -47.07343 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6841f8dc-fb4c-3ed3-9ab8-580ec599e176 | -21.32594 | -47.07005 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccd046e4-0b74-384e-a550-4d27d7b989cd | -21.55298 | -47.05616 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3879e36-7334-341c-9894-fe9ad75f1b53 | -11.3584 | -52.9514 | 2026-05-26 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 24142f65-da2e-33ed-a795-1d51822b3ed0 | -11.3773 | -52.9496 | 2026-05-26 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 51ff7272-4869-3964-b5ac-60f94ba051f1 | -11.3584 | -52.9514 | 2026-05-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 4fe85720-aaf6-3f94-bbe0-46ad72dbc6f2 | -11.3581 | -52.9722 | 2026-05-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 48dbaef7-ef4b-312a-85bb-90871dbd181a | -11.3584 | -52.9514 | 2026-05-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| cdcd13a3-e0e0-3098-a86d-b8fe2c96125d | -6.08329 | -44.00721 | 2026-05-26 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84e11f05-4c79-331b-ac19-4c7c7c32ab9a | -7.13513 | -44.07402 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1141a3ce-09fc-3fa9-a06f-b34a5fd2db50 | -9.34191 | -40.21084 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 703c678b-6b50-3757-9f43-628f07621fc1 | -7.13292 | -44.06429 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb558d5b-97b7-33dd-88ec-1f64f3f6d713 | -5.34974 | -45.18703 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cfbb12dd-9f44-392b-93d6-c882aebaaa74 | -7.14117 | -44.06101 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e73be879-1dab-3900-8e4b-917f71d39063 | -5.30239 | -43.06303 | 2026-05-26 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2cf06ff-c4d1-38f1-90ec-bd41d57969b5 | -9.33802 | -40.21383 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c20f81a4-c84a-39fe-9022-b9d02a434181 | -5.95295 | -43.48746 | 2026-05-26 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d62eec4a-e4b7-3a6a-821e-29a18a3bf3c6 | -8.72105 | -47.9154 | 2026-05-26 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a3ed707-7298-3da2-8113-e16434df73e4 | -5.78802 | -45.12495 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2910424d-d1d0-37c3-8200-de98c3746286 | -3.35835 | -43.16773 | 2026-05-26 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8557b3a8-899b-3d8e-b2a6-6493b087e040 | -7.01066 | -45.00198 | 2026-05-26 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff47f85c-6974-3aa2-ad0b-4adc6f3fc8b3 | -3.35861 | -43.17118 | 2026-05-26 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6ca1022-571e-3ae3-a4bc-a8d447975c0d | -5.18378 | -35.86182 | 2026-05-26 04:10:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1b10ab2-bd7f-36d8-b477-db416d550a91 | -6.07951 | -44.00658 | 2026-05-26 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 148ac0c1-5edd-3994-8a74-88ae2c4646eb | -7.57508 | -50.17713 | 2026-05-26 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ccb64ee-cac1-3144-821f-8f8932efda3d | -3.95995 | -43.12768 | 2026-05-26 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73e9a77a-cdf8-3c36-aa53-37e72209193a | -7.64176 | -45.30009 | 2026-05-26 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e00e90c7-5f33-39a0-8ee8-f3588eafcdee | -7.13591 | -44.06941 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e8cf9c60-7d79-3304-97c5-6cc80cc8399b | -5.79086 | -45.13296 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58ba09ad-9f50-3b5b-aab1-e89108dd55e6 | -9.48646 | -40.29842 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3267a5df-7ba1-3bf6-9b83-106a29bf8c14 | -6.10614 | -44.73675 | 2026-05-26 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91ad8cf6-a973-3b74-833c-52309a63829a | -5.81224 | -43.20957 | 2026-05-26 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea4e5ed9-679c-37fe-8f79-40106ebb8ed3 | -5.79025 | -45.13663 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 181feeec-e675-3481-a2a1-5375080d0a5a | -9.33857 | -40.2103 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 931551ab-5290-3d57-95ef-9ca9d5056794 | -7.14338 | -44.07077 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b883f0f-8710-3b07-a859-bb2fb804ff37 | -5.81749 | -43.22325 | 2026-05-26 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd0df59d-c16f-305a-a7c4-bccc44000a40 | -3.95553 | -43.13146 | 2026-05-26 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d900e4e-4c04-32a0-a291-9db5d5246122 | -6.10218 | -44.73608 | 2026-05-26 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f5d687c-b272-315f-92eb-7107ed849737 | -5.7933 | -45.1184 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2b111351-998e-352d-8b42-ceab4ea06ed1 | -8.61703 | -45.02511 | 2026-05-26 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1c9eb7f-cfc2-34df-a8fe-5417c651705d | -2.96377 | -39.92145 | 2026-05-26 04:10:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e7af8afb-9aa7-3040-b364-0e6edbbcfd90 | -5.78923 | -45.11772 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65dc8391-e21b-3a86-b2a4-368caea587d2 | -7.13743 | -44.06036 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef8e2d2d-1902-39c4-9c4e-faa06a3793c3 | -7.59978 | -46.46264 | 2026-05-26 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8322896a-1c06-3b40-9622-24abdf8fe895 | -7.14491 | -44.06166 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e289ed42-9b0a-37cc-9679-f8755e73ba8a | -5.78863 | -45.12133 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 729c3ef5-aefe-3396-aece-53715f259614 | -4.43274 | -47.72991 | 2026-05-26 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d16232c9-6732-3f09-9984-d384dc056f55 | -5.30171 | -43.06723 | 2026-05-26 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b15d6cf6-e1a6-3d63-beb8-5a358e9148af | -6.72846 | -44.37138 | 2026-05-26 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91e97373-6735-3692-b74f-3770c09169e9 | -9.48925 | -40.30247 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 324b9985-8c9f-3ee7-a5cf-74532ee6e990 | -5.81292 | -43.20538 | 2026-05-26 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ff17e46-d872-3c37-b29c-e8b4cc97e252 | -7.3571 | -46.21892 | 2026-05-26 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a11ec8ae-da54-36ae-ac47-679662bca4d5 | -5.79148 | -45.1293 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e8d1aa8-ee0e-34fb-98e1-66e2fcfc34a9 | -9.48591 | -40.30194 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 30.8 |
| aa037472-2349-3698-8aec-5087bd2c5209 | -8.33187 | -45.37885 | 2026-05-26 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa203b19-f070-3fc7-8b0d-32eebb9e921f | -5.53697 | -35.52629 | 2026-05-26 04:10:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b845e08-989e-36d4-8a8e-67dfad2c9ac9 | -8.55262 | -45.98201 | 2026-05-26 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b374110b-e56e-326a-8ec1-976c1651a5d5 | -5.30535 | -43.06781 | 2026-05-26 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6ecdd4d-f719-37b4-bc25-a6cb88080e4c | -8.8764 | -46.93739 | 2026-05-26 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09bc8c57-a5a6-3c5b-a13e-2484e6d4228b | -7.64089 | -45.3053 | 2026-05-26 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24b83f95-0bdf-3b53-b7fd-800d783d9fa3 | -7.14041 | -44.06553 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cf2cac49-a9da-3b35-9690-c91b6f31518c | -7.14788 | -44.06688 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e62fe759-1272-3942-99c6-de8a5ca74893 | -5.30671 | -43.05939 | 2026-05-26 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4733c3b9-f54a-3a31-8f17-3dcf096176e5 | -2.96043 | -39.92093 | 2026-05-26 04:10:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f5a11df-974e-3da7-941e-17728095987a | -7.01461 | -45.00271 | 2026-05-26 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc89bbc3-4219-3f6b-9c08-8c6d1e8fd441 | -7.14415 | -44.06621 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0bc59ac-b354-39d4-8ab7-022ad89e1073 | -6.76029 | -46.53012 | 2026-05-26 04:10:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8ea1c7b-ed36-3463-993d-8b5f165ff1a9 | -4.65747 | -42.43507 | 2026-05-26 04:10:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a80bc41a-9ce6-3276-845d-c723b6ec300b | -5.78741 | -45.12857 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b23ebc90-26f0-3430-af50-2bf307366676 | -3.95625 | -43.12707 | 2026-05-26 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36a47e2b-4e7d-32e9-afd9-a5f3b1aaf337 | -8.62479 | -45.02643 | 2026-05-26 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 30f5b414-5a14-3abb-b6dd-52f69e354011 | -8.72222 | -47.91716 | 2026-05-26 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f695a0da-5a76-3df5-af61-7e27cadea06d | -7.59907 | -46.46675 | 2026-05-26 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c5fa919-6b39-3e64-b1e9-88a70a17d57f | -8.55674 | -45.98278 | 2026-05-26 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3ccbb94-285e-31ca-8c3d-928d7755a1e8 | -7.21731 | -45.35172 | 2026-05-26 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe6bd775-5f3f-32c2-befc-6c176812dcca | -7.21752 | -45.35228 | 2026-05-26 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86cb53d6-42bb-3b04-a202-cc240300b3a8 | -5.53717 | -35.52404 | 2026-05-26 04:10:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 205a467c-d4ad-3d7b-9768-9c995a942c86 | -8.33587 | -45.37944 | 2026-05-26 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea96cf39-22ca-3263-a633-46a263f417cf | -5.81385 | -43.22264 | 2026-05-26 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 733385e2-b3b8-369f-a773-8aa1d1ebd040 | -9.33468 | -40.2133 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 79075046-8957-3ca4-96cb-5bcc968696f8 | -8.56084 | -45.98357 | 2026-05-26 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b452e00-0157-375d-bf53-3fdbc871f75a | -9.53542 | -40.33507 | 2026-05-26 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b5cad9e-34df-3d9a-88d9-b7640807d722 | -4.40814 | -42.14571 | 2026-05-26 04:10:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b8ced64d-0c67-332e-8daf-df309de1200f | -7.01151 | -44.99689 | 2026-05-26 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dbadd86-aa8f-32f2-8096-2bf35ad92b6c | -6.21673 | -46.8833 | 2026-05-26 04:10:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96c286e6-be08-3cf0-b715-35cd5be31a11 | -8.56021 | -45.98723 | 2026-05-26 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61864947-3660-3c5b-8209-8712ebeb1735 | -4.42777 | -47.72908 | 2026-05-26 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a841198d-de78-373e-90cd-d2b1fbac45e9 | -5.22926 | -43.1899 | 2026-05-26 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc47df7f-b60f-3b63-bd14-93558507557c | -5.30602 | -43.06362 | 2026-05-26 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec5aef6f-3f2c-3ce6-9807-aac3f05aff79 | -8.55199 | -45.98568 | 2026-05-26 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c06be36-de6a-3b6f-b25c-a0a986b97167 | -7.13965 | -44.07005 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2f63abbc-e32b-3250-a36c-7050b691929d | -7.59475 | -46.46598 | 2026-05-26 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6c24ae3-d525-3e4b-8148-25a93728ff33 | -8.6162 | -45.02997 | 2026-05-26 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README6.md)
