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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0022511b-4083-3348-aee1-6fe4a611ae48 | -8.22492 | -46.24789 | 2025-11-01 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eacce40-4b4f-3aa8-920a-1ee11fcdf81c | -2.91198 | -53.9525 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf1f5dc6-bb9e-33f7-aba6-c35c538ae88e | -4.85086 | -47.52826 | 2025-11-01 05:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 156615db-0a9e-3fcf-be46-c0300fffdf45 | -10.4153 | -44.35505 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 76cb6fcd-b0c0-3a35-9ad0-0bbac368082f | -4.66835 | -45.81003 | 2025-11-01 05:08:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ab2b16a-c454-3f2f-826f-77d394e95177 | -5.25978 | -48.47592 | 2025-11-01 05:08:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5162cc15-9d44-3e80-9d05-2f1c86fc0234 | -4.55057 | -45.80233 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a9c24a-84d0-3305-ac38-0ed269f9b121 | -3.08644 | -52.92002 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9eea28e-9505-3235-abc1-56f33056631b | -3.74546 | -51.26709 | 2025-11-01 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 390eb1f6-759e-3d6b-b57a-66f8899795c7 | -5.21864 | -44.79732 | 2025-11-01 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 132bd163-ea65-3626-ac70-d1ed48d33259 | -4.77255 | -46.50008 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d00a93be-c08d-360b-9b5b-44582648010e | -4.18061 | -47.65487 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 71c249e4-7cc2-30d7-994d-7954da1b0a57 | -4.44452 | -46.0383 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a83eda18-b0b3-3c68-bb83-c6207043a7e6 | -6.45926 | -46.72896 | 2025-11-01 05:08:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4cd1b55-6d35-318a-82a9-0e5b779d0ff3 | -5.14342 | -49.87125 | 2025-11-01 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab435940-9c8a-374c-ad3c-1aae87cfce63 | -3.6567 | -50.18872 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbb81204-7a43-38f3-b662-b88cc98475fa | -3.83681 | -51.34729 | 2025-11-01 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96370c98-6f8d-32e6-8c18-90bb0aebfd6f | -3.37768 | -51.07117 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04fec6b3-dd92-397c-a90c-428953f13dec | -3.73462 | -51.71057 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8601e48-3fd0-3adc-a7f9-237aa4f9ba13 | -5.59303 | -50.0607 | 2025-11-01 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aca7fb44-9f75-31ec-ae01-78db69963a95 | -5.13017 | -43.38765 | 2025-11-01 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a95865e-bd69-3615-a653-5a9c83ec4475 | -5.88753 | -44.52504 | 2025-11-01 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23772189-0689-3bbe-914b-b836a7d4bed7 | -5.09333 | -47.71407 | 2025-11-01 05:08:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6479574e-52b0-3906-afe4-e43929d93990 | -9.91077 | -50.50193 | 2025-11-01 05:08:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04223de2-bd7b-3552-a7a8-d591fd02ed1c | -8.11745 | -55.31261 | 2025-11-01 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aed92cb-ea2c-3e2d-afbc-040b54bedb99 | -3.60559 | -50.62663 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35f0888a-436b-315a-a000-c381ee55ef43 | -4.42808 | -47.59676 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20bbcde6-7817-3592-931b-c04239e97169 | -3.01441 | -53.96889 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55b96b16-c00e-3faf-a0db-7c6c19265135 | -10.41596 | -44.34957 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07c9a962-b12f-3f24-a1ab-0395cbafd927 | -4.25426 | -50.66982 | 2025-11-01 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e88cccaf-0150-3c0b-9859-6e9eef043b25 | -5.59724 | -50.06129 | 2025-11-01 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf137e2b-4179-30e4-b2d6-5b2d7b527b98 | -3.19936 | -52.86751 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac43bd2d-ff39-35c8-8a96-8a5afaa81b2d | -5.12891 | -43.38784 | 2025-11-01 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76c6fec8-3d38-32f9-bbe8-28650595e61c | -3.86461 | -51.16928 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c305899-a037-3434-976b-ccad438c16a7 | -8.23328 | -46.24753 | 2025-11-01 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8bf2485-5af0-3b5a-8baa-7b15f7145dc6 | -5.8814 | -44.52412 | 2025-11-01 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65480b84-97ba-31c6-b894-3f92f6525974 | -6.87857 | -42.84971 | 2025-11-01 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 38ec8400-b5c1-3d6b-a500-63f0ac91a832 | -3.53905 | -50.17026 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9495a1c-6799-31f4-83aa-5d02ce131020 | -10.62762 | -52.18258 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc435b3d-b13d-3491-909b-a37672603514 | -4.67446 | -50.44606 | 2025-11-01 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c84481a-7a47-3e42-9342-0b439158c745 | -5.89896 | -49.14421 | 2025-11-01 05:08:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e65f2959-2ec8-3481-9775-116dfa27fca2 | -3.47466 | -53.49882 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eef222f6-872c-321d-8212-7776f5e7b820 | -3.80093 | -51.61209 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463369f7-12fd-3474-9c0f-6af17ed225f0 | -5.68118 | -48.65897 | 2025-11-01 05:08:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 713ee2e5-6b7b-3d7e-8a91-2998179915b1 | -4.66759 | -45.81069 | 2025-11-01 05:08:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2825995e-45c2-3fc8-b3c6-91d59492a69b | -4.18324 | -47.64875 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2735d113-650d-3c84-9adc-8fe93e4a7738 | -5.88202 | -44.51974 | 2025-11-01 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 692913f4-dcf5-3312-ae85-18c0f8919c07 | -10.41467 | -44.36031 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e891c5d2-5532-3906-85ab-9cfcc790e3a4 | -4.5311 | -46.40266 | 2025-11-01 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6853cdc1-4138-32b2-96ba-add1fe2eb6cd | -3.46378 | -51.44171 | 2025-11-01 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bff00fe-4bca-3f2f-a414-8daab03a5aff | -5.88819 | -44.52035 | 2025-11-01 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69d8c484-791c-3fb3-ab49-d454f88e6153 | -10.41132 | -44.33258 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2fd4c1f-a848-3873-893a-1873ab73019b | -7.06743 | -47.36588 | 2025-11-01 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17e6d824-8a38-3919-bc2b-d12475a3a5e9 | -4.54924 | -45.62672 | 2025-11-01 05:08:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30a5b2b4-1f55-3d94-9fa2-b8b674ae5b8b | -4.29462 | -46.26053 | 2025-11-01 05:08:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 863c1227-e84c-3654-bad2-4f4cfba0d507 | -4.79811 | -46.4727 | 2025-11-01 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cd78833-036c-3995-9ab8-7ca47215c293 | -10.62444 | -52.18044 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6f65391-9840-31e4-bb95-8007f45be023 | -9.06757 | -48.8319 | 2025-11-01 05:08:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4daafee7-577b-324a-8559-03c61348dc77 | -4.29415 | -46.26383 | 2025-11-01 05:08:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db44ec8a-c81c-34be-a315-3718ab627135 | -4.77784 | -46.50095 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b591c7dd-43c4-345a-8c54-b9ee88af5ea0 | -6.58052 | -48.73247 | 2025-11-01 05:08:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e015b910-11f0-3d92-9bea-533528acbd96 | -4.42322 | -47.59581 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64cf81d-c0a2-3bb7-abfa-cca28bfe6245 | -7.35996 | -47.7809 | 2025-11-01 05:08:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 529fd45e-50e3-3e4f-9bac-d14696f9e5e2 | -3.58914 | -50.80996 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58ec3166-51af-3379-8c4a-91193c9f6160 | -4.55977 | -46.68445 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32c9994f-7b56-32e0-87ba-b6678e1038b2 | -3.49264 | -51.5502 | 2025-11-01 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4febb91-ab3d-3d72-8a62-b96652f2fe43 | -3.79349 | -53.69273 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f42046d-7dce-3717-93a4-108802bbc70c | -4.77371 | -46.50035 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c92a6aef-2bb5-30ff-8239-130bf47163ec | -5.35489 | -45.03419 | 2025-11-01 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a5d27bb-d03b-3693-a2cb-32046482bafe | -3.44242 | -52.80939 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9674b3c8-c546-37e8-8489-c2c808d657cf | -4.70986 | -55.98889 | 2025-11-01 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b57ae3fb-dfdd-3f77-bf70-d9cfba41a988 | -8.22763 | -46.24665 | 2025-11-01 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd1368a1-0b62-36cc-a027-d37cd0b20a5e | -5.21803 | -44.80155 | 2025-11-01 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfdff05c-182e-3f00-a992-35e6ecce3420 | -3.59241 | -54.03975 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 565a995b-245e-300e-8bf7-d4f33a4399f2 | -3.47271 | -53.12781 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3a8d434-53a1-3a10-95c8-4f7b6dd9eaa9 | -3.74185 | -53.3966 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0029ad24-2cf1-3b6f-b864-035f7e1724a9 | -4.79282 | -46.47171 | 2025-11-01 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53d8b33a-cf98-3d7c-8942-3d7d01bbdc4a | -6.87901 | -42.8431 | 2025-11-01 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a3753a74-c2bf-3818-9531-e79d421c9376 | -9.08755 | -47.88424 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e8e4f22-6995-3210-a2e2-a0ad938df15d | -3.3687 | -51.57713 | 2025-11-01 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5249692-0692-3802-9200-b96b394e86a5 | -10.63549 | -52.18375 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b1bc2a75-96de-3406-9bb9-2c116e59f207 | -4.83224 | -42.72985 | 2025-11-01 05:08:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbd236aa-4aa6-3cc8-b0a5-d0e08930ecb4 | -4.43377 | -45.91785 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57900f47-f16e-38a2-b6ff-400bfd1f7a94 | -5.94711 | -48.33447 | 2025-11-01 05:08:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f35e20b3-e370-35c4-b3b2-4a6b0cab3872 | -5.26203 | -45.60909 | 2025-11-01 05:08:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c891012a-a346-35d7-800b-20126c50f5a1 | -3.65616 | -50.19221 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a7bf327-f8bc-3cee-88ff-fe58e76b2534 | -6.3241 | -43.62355 | 2025-11-01 05:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c022c93-5af4-3408-9877-ccc9ddd96612 | -9.09268 | -47.88504 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2be75b67-049c-3e82-a4a2-a33585e1bd30 | -3.46915 | -50.93612 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e181ec2e-6ad6-3b96-8349-11d77dc729a8 | -6.55871 | -52.79927 | 2025-11-01 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef80cbc0-9e91-3413-8dc8-7bc9972ae818 | -3.74207 | -53.39709 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 879b2697-3306-3eb1-a5d0-f0f351d374c4 | -4.6785 | -50.44662 | 2025-11-01 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 305c9d88-6af2-305d-b7b5-dd5b8eb5d2d7 | -5.07136 | -45.11527 | 2025-11-01 05:08:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e542b72-79f6-3326-b50e-19ae58d0a35f | -3.46676 | -52.16507 | 2025-11-01 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d899fe8-4a85-3acb-beb1-c9a9ab398390 | -5.14402 | -49.86735 | 2025-11-01 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7f78056-20bb-3591-a17f-8a736a16025a | -4.5511 | -45.79854 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6b23c51-1c7f-35cc-91a3-172b2d207063 | -6.88637 | -42.84391 | 2025-11-01 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8ae47be3-edac-38d6-979e-48d69e718c03 | -3.8608 | -51.1687 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c168f503-b400-3804-9b87-c6a3cc0d9740 | -4.77901 | -46.50119 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d28023e-7944-3b33-9911-44e3c204b064 | -5.22124 | -44.79939 | 2025-11-01 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README28.md)
