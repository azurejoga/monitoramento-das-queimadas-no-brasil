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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7562826-7b4c-3b01-8d0d-a2e14603b832 | -4.3685 | -43.4071 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| c660630c-f88f-3a61-b890-2b6ea027f7a3 | -4.1161 | -48.0136 | 2025-10-16 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 8f116765-5cad-3971-bbc5-675cb8b22c47 | -3.0158 | -45.3679 | 2025-10-16 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a616dfe1-f768-381a-9a5f-8ee3e5665904 | -4.3687 | -43.3838 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 7e2d51a7-bba0-373e-b47c-26d76b50c873 | 1.8217 | -55.7629 | 2025-10-16 03:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 4cae11d0-34bb-3a00-ad3f-bdf7dfea71bd | -4.6626 | -44.0832 | 2025-10-16 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 029f3a7a-b803-3bfd-91f8-4c78239749b1 | -7.9628 | -44.1362 | 2025-10-16 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a18f57dc-29f0-39d9-ba09-5b784ba9a30c | -4.6437 | -44.1073 | 2025-10-16 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a8ed0607-2466-3f60-9995-ce9230ad2d93 | -6.1534 | -40.8971 | 2025-10-16 03:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 7730d54a-098e-3217-81b0-46bb2bc54126 | -4.3685 | -43.4071 | 2025-10-16 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 274.5 |
| 8b5bc639-07e2-3eff-9564-c274ff62b230 | -2.9971 | -45.391 | 2025-10-16 03:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 2cc317be-d071-34b6-8fd1-45f22417a3dc | -5.4762 | -42.9367 | 2025-10-16 03:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 3170406b-3f59-3022-9b21-0883c1e97803 | -5.6821 | -45.0893 | 2025-10-16 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 3320afec-3881-3097-86db-31216d1a6d35 | -3.0157 | -45.3903 | 2025-10-16 03:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 725b2f90-8e70-3dfc-8519-077acae444e9 | -5.4764 | -42.9132 | 2025-10-16 03:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 96c5a2a1-f666-3f4f-adb6-3cfaedbdc980 | -7.3955 | -39.6845 | 2025-10-16 03:20:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 5dff8df8-243e-3104-bb2f-dabcbc782f94 | -4.0974 | -48.0361 | 2025-10-16 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 8a857562-0fb5-30f5-ac57-7a106797ed9c | -4.1161 | -48.0136 | 2025-10-16 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 730af3da-70f6-3992-9070-dbd217b3646e | -4.3872 | -43.406 | 2025-10-16 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 305.8 |
| 673f8d5d-ffa8-3980-8741-87925ecb883b | -4.3687 | -43.3838 | 2025-10-16 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 285.9 |
| 36bcc711-63df-3916-9df6-034a4fb7ca5e | -4.6439 | -44.0843 | 2025-10-16 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| a1e780a3-4b27-30dc-90a2-83000749aceb | -5.5147 | -47.3069 | 2025-10-16 03:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0ecdbc34-c653-30a8-929a-b5ebb4a5123b | -8.4528 | -44.1767 | 2025-10-16 03:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c788b08b-76da-3499-9d65-ea06ee376422 | -5.8802 | -43.8613 | 2025-10-16 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 881c9ee8-b99c-3a65-86a8-5f2df9192555 | -4.4059 | -43.4049 | 2025-10-16 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ce501a10-e5cb-3ec3-8867-c7e11ab732aa | -14.1749 | -47.9477 | 2025-10-16 03:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| a7941b6b-0b36-342c-ba0c-da31a187313e | -5.6819 | -45.112 | 2025-10-16 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 7ea52e23-6705-3961-bced-9c3a283a0b5b | -7.9439 | -44.1381 | 2025-10-16 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e665b4ad-d105-3826-be97-11266cbc23ef | -4.6813 | -44.082 | 2025-10-16 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| dca61442-fdb6-3a29-9f48-142cbe87d6f6 | -8.4717 | -44.1746 | 2025-10-16 03:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 03d12bf6-6977-3ff3-b60b-3b5fedf854ec | -8.4714 | -44.1978 | 2025-10-16 03:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ed40bf6f-cb94-389f-9b20-f5e4247d3a0a | -4.116 | -48.0352 | 2025-10-16 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 6efa77f3-c16b-3b5b-98da-453ac19a5a7b | -4.4061 | -43.3816 | 2025-10-16 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 871cb001-6bd0-3951-a431-467341e67e50 | 1.8401 | -55.7429 | 2025-10-16 03:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e389487e-d748-3b44-bef4-99e8deaca459 | -12.6805 | -43.4235 | 2025-10-16 03:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6cf813f4-d87f-3002-84a8-6e694eb61231 | -3.0158 | -45.3679 | 2025-10-16 03:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.7 |
| ad7cca6b-f649-34e1-bab4-66b43eaff81a | -4.0976 | -48.0144 | 2025-10-16 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 7ca04236-4a07-3b4a-996f-f3d3285d54a5 | -4.7224 | -46.1608 | 2025-10-16 03:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 29cd26d7-85a2-3b74-8fe8-990658591ba7 | -4.6624 | -44.1062 | 2025-10-16 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 00d9db4a-130f-38b2-9167-f6cdf1ccce0c | -6.3733 | -41.4828 | 2025-10-16 03:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| fafdf77d-938f-34d3-b2d5-9f31b87aff58 | -6.1723 | -40.8954 | 2025-10-16 03:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 32db3699-ec29-3660-9f34-79f8b4441a8f | 1.8218 | -55.7431 | 2025-10-16 03:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3aa53d6a-94eb-345a-9cd9-c19534d6d72e | -5.8799 | -43.8844 | 2025-10-16 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 297987a7-5282-3a55-a7b9-787b91329a0a | -4.7411 | -46.1598 | 2025-10-16 03:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 107180e7-b6da-3716-8e38-60926a82480b | -4.6811 | -44.105 | 2025-10-16 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 79cd1a44-15d2-3fe6-80cc-ac477111e936 | -4.3874 | -43.3827 | 2025-10-16 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 269.0 |
| a968bdc5-2889-3369-9638-fa973c544106 | -6.16141 | -40.91268 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 2e3dc9dd-119d-3298-bd95-123e3e0de895 | -4.91698 | -41.55639 | 2025-10-16 03:25:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 638bb973-b9cf-3c36-b5b1-9bc213f57592 | -7.39292 | -39.69916 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 7ccdcce3-8db2-37aa-a3c5-2b961c830377 | -6.36828 | -41.49208 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| bad5c7e9-50fe-3907-8c7d-8a3f2b4c3740 | -5.87609 | -42.81416 | 2025-10-16 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 03731a34-f04d-3e48-b7c3-3a6a9cf92890 | -7.16945 | -42.5149 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bb84f4f2-3edf-3fdc-98ed-75d74480fe36 | -5.79153 | -35.59919 | 2025-10-16 03:25:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da31630b-1c3c-36a0-aa80-09385e647a58 | -5.44728 | -44.27546 | 2025-10-16 03:25:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| aec3b4c2-2a18-3907-a2f5-a47886edcb1e | -4.36604 | -43.37828 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53e226cf-9756-3442-9db5-5010337dcae9 | -6.10534 | -40.88986 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| cbe74b00-959f-35c3-a6d7-8c3b353af060 | -7.46865 | -41.52123 | 2025-10-16 03:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44a4ac3c-b285-3cf8-b436-552fd0a2e19e | -4.37182 | -43.38635 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5096816e-7898-341f-8a0b-1973c38d1b14 | -5.40991 | -40.91558 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b6d2f41-28b7-3f18-92e0-af94cf6e0673 | -5.46823 | -42.94456 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e42f4b30-c50f-3211-bd50-444991aeab9b | -5.44887 | -44.27341 | 2025-10-16 03:25:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3a7ff69-129a-3df5-a45d-cfb2b0bf974d | -5.88196 | -43.85699 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fb75879-6cf1-3bb6-9d45-e9400526d0a0 | -4.66594 | -44.12367 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fece2a0-030c-39bd-9543-c5d6d0481852 | -6.14467 | -41.78366 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b88bd9a8-09c6-3abe-8f54-b2f6f8ed3432 | -6.15409 | -40.91453 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 2e21b263-8db3-3842-b3aa-38e89c70acee | -5.79366 | -35.60294 | 2025-10-16 03:25:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c035dccd-57cf-3593-aaf9-ae16eda7b18f | -4.66852 | -44.11498 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ce61f54-5cfa-3cc0-a812-c9ecb7d415bf | -4.66663 | -44.0845 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5043c8fd-0b91-33b7-b5fe-d4a84ed8cb7c | -5.88199 | -43.89571 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b996588f-02dc-3e2b-995e-74610af08305 | -7.46494 | -41.52248 | 2025-10-16 03:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e83346c9-1bf2-37c8-a6cb-8b57bb461f06 | -6.06252 | -41.89611 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 95bcfab6-e930-32e4-8aa1-6640cf1ed04d | -6.04295 | -41.93335 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 065d68b8-762d-32d7-986e-c8d359e27872 | -5.86267 | -43.84418 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c78475c-2621-39ef-8bc9-fed3f103418a | -7.18366 | -42.36527 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 26392930-a9f8-3639-8633-04b812086757 | -5.47414 | -42.92687 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| b2e660d5-c0a2-3b4a-b2ac-36d3999ae126 | -6.15485 | -40.91576 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 268d17af-d6d5-3bed-b787-949f90aa65b5 | -4.36065 | -43.39602 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8f0f55a0-f33e-3afc-9644-9effb3740d1e | -6.38211 | -41.4796 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 625aadeb-daad-32f1-8a97-03a7dad75242 | -6.15991 | -40.91565 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 9046cdfd-e91b-3675-9cb5-86b786531e3c | -6.57335 | -42.96499 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72ff605b-c27f-33af-8270-038a043bbb72 | -6.37515 | -41.48858 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| bf4e9fe1-5270-3255-b941-cb300429d7a8 | -4.37701 | -43.38502 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d206a1bd-25fc-3329-bace-145362befa3c | -4.36139 | -43.40506 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 56883226-7a9d-3b6d-92f9-9cc8f35db7a5 | -6.7541 | -44.37455 | 2025-10-16 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c64f20f6-2850-3346-9d63-9412a78ac94b | -4.38854 | -43.4009 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0706abda-d583-3422-8555-2afbca51f526 | -5.4278 | -40.98554 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b18831dd-89c9-38eb-9e69-e4d4ebb08583 | -6.06696 | -41.90707 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4199ce9e-9265-3a88-88da-6706203ad65f | -5.86327 | -43.87953 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d441a0b5-3117-3428-b353-5fa963625f41 | -5.87629 | -43.84867 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6c6eb1f-64db-3e8e-8459-911830aa4a5f | -6.37457 | -41.48703 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 2ca91f3e-a76b-38d4-baf3-5e99a9db6baa | -4.38157 | -43.39966 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 50eb1c91-209e-3c87-8b59-fb313679aa67 | -4.3673 | -43.41243 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 150eed71-e37f-30d4-864f-75d0c9622b85 | -4.36839 | -43.40614 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c8b9e0ce-2204-3034-8906-415b84d3800d | -5.87716 | -43.88274 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5cb9bc20-01ef-3536-becc-da42d878ac80 | -6.45261 | -43.3858 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b819b720-c0a9-33d1-860c-4d82c9deb833 | -4.37415 | -43.37292 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04c6c49d-d022-3411-9507-b75c03ce58e0 | -5.53648 | -41.32409 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2259e9ce-ca02-31f8-98d6-a67f8132e159 | -7.01265 | -41.95645 | 2025-10-16 03:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e90e07db-557c-32b8-9c90-ae75a6e378ed | -7.39351 | -39.69589 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.1 |
| be43230b-4685-3ae2-ae87-60725ac1bee9 | -5.47145 | -42.92659 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |


[Clique aqui para ver as próximas entradas](README12.md)
