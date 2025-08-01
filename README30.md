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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca054bca-b8fa-30fa-b6dd-8b06b8031e95 | -8.051 | -43.1237 | 2025-08-01 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 3aa0123a-a8cb-395e-9177-0b188bb17558 | -6.74816 | -59.14871 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 838a99c7-59c1-37b0-8d14-3ef4f0b10cd4 | -10.08081 | -46.75776 | 2025-08-01 12:51:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| bc7da648-4d13-3102-8be0-e80990fb0cd0 | -12.66499 | -48.09438 | 2025-08-01 12:51:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5bec2b0c-7360-363a-a500-ef48bb0d584f | -7.72449 | -45.08322 | 2025-08-01 12:51:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 19bee061-8eb6-3596-ab93-9a61d032eee0 | -10.11058 | -58.22988 | 2025-08-01 12:51:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b88f8f77-51ce-3034-bc8e-a92767a4e119 | -11.26634 | -52.74154 | 2025-08-01 12:51:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7324c5dc-5652-3b3b-9ccd-eba22dc15f53 | -12.12941 | -58.18965 | 2025-08-01 12:51:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 35c7c5f8-2828-34fb-b71b-910db2860c8d | -9.46261 | -57.83702 | 2025-08-01 12:51:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| f394bd31-16ef-3211-8edb-a1e1a0d8971a | -6.81203 | -59.25637 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| aa1d06b3-8f7d-3fc9-9b18-4d5d99699ba9 | -8.16664 | -45.44104 | 2025-08-01 12:51:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 5fe4b45b-32df-3337-aa5f-d147fd3bf5b8 | -6.65248 | -59.097 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 67dd62d7-1d43-3803-b0cc-f3bcf2f91fd2 | -8.1707 | -45.40862 | 2025-08-01 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 323.5 |
| eb8f0d66-69b4-315f-9dc9-65cedbc37b5f | -11.16423 | -45.75614 | 2025-08-01 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4cde9085-ee40-3917-913b-66127a4d5e24 | -6.7435 | -59.1787 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 0d9cc570-184c-3c2b-abbb-d9cfc64523d3 | -13.04992 | -47.40937 | 2025-08-01 12:51:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 306ffad7-2f96-30b3-b807-db47b266e8a9 | -6.74584 | -59.16364 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c8020fbc-2c1f-3e1b-9964-991232eba3f9 | -11.19675 | -51.48542 | 2025-08-01 12:51:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e307f50b-4072-3888-b6ca-4b06fcd37bcc | -12.65714 | -48.09977 | 2025-08-01 12:51:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7507d391-f6d8-34de-b607-268d0c144251 | -11.17203 | -45.76203 | 2025-08-01 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e63d92b0-fba0-325b-a9f1-0524576fad1a | -6.80963 | -59.27165 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 0cabd095-8a08-3ecf-ba10-3a83aeae4bd0 | -11.27586 | -52.7428 | 2025-08-01 12:51:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 32051fd9-acb7-38ca-9088-9ef0ff619fcf | -6.64124 | -59.09532 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 08b6eeaf-2ecd-3797-834e-fbb598b12093 | -7.333 | -59.61298 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8d0f970b-9514-3822-8e07-4d037e6673ac | -6.82338 | -59.25802 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1175.1 |
| 8581470a-8285-377f-b7fd-ba8fedaf9c48 | -11.19512 | -51.49788 | 2025-08-01 12:51:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ca167123-3a3a-33cf-9ad9-6e90382b869e | -6.73219 | -59.17709 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 231.9 |
| cacacfe6-5966-313d-be28-c82cf9d833c6 | -6.83472 | -59.2598 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 337.4 |
| f9583528-4cef-3f29-a338-3d1e7c66ef73 | -6.73453 | -59.16209 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| c8e192f8-4aba-323d-bdd1-797031db23e3 | -12.12522 | -58.19389 | 2025-08-01 12:51:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2fba6269-7c56-3ba9-8d3d-72c8f26994c5 | -8.16375 | -45.41341 | 2025-08-01 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 314.8 |
| 566c13ce-3cc0-382c-ae4c-252813d6f7c7 | -9.45281 | -57.83562 | 2025-08-01 12:51:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f2919169-2117-3e02-aca3-b108db6dcbbe | -11.18481 | -51.49651 | 2025-08-01 12:51:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2151e055-6693-316b-8441-4bd95d9f7849 | -12.65981 | -48.07572 | 2025-08-01 12:51:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| f6498fec-c1d1-3ac8-a94e-3a7da28f8170 | -6.83239 | -59.27489 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 387.1 |
| 8f4f1221-686f-38ae-866a-93e39e0cd4a3 | -6.82102 | -59.2732 | 2025-08-01 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1437.2 |
| 6cfd39c3-f3c6-354a-b338-488bfc9390f2 | -14.95958 | -49.27688 | 2025-08-01 12:53:00 | TERRA_M-T | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 424b0737-3934-30db-8038-9de40ec50059 | -16.59828 | -49.40382 | 2025-08-01 12:53:00 | TERRA_M-T | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f6d3f09f-1277-367e-be10-f1c989b1236c | -16.65337 | -53.39087 | 2025-08-01 12:53:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 058e87ec-2cfe-3ed8-b223-02d564aadcf5 | -13.30426 | -51.68141 | 2025-08-01 12:53:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3f9e48d2-173b-32cd-8220-94363a2170d9 | -18.97524 | -49.76347 | 2025-08-01 12:53:00 | TERRA_M-T | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 3bbb26d9-a1f4-3f7c-8353-9a4a1901a0d9 | -15.08377 | -55.20202 | 2025-08-01 12:53:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8df55b63-960c-353d-8146-3cad96b3405e | -16.65483 | -53.37957 | 2025-08-01 12:53:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| b96f24a0-983b-3a77-ade3-ed4fb070797e | -21.33183 | -55.62727 | 2025-08-01 12:55:00 | TERRA_M-T | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 54791b1e-223c-30dd-9254-28714bf5ec80 | -22.01652 | -55.16801 | 2025-08-01 12:55:00 | TERRA_M-T | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d13841d9-b8ee-3c3d-a993-7527af39d2c8 | -20.4445 | -56.99326 | 2025-08-01 12:55:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc77fa97-434a-359b-8470-35d2ef37e02c | -28.71826 | -49.86311 | 2025-08-01 12:57:00 | TERRA_M-T | TIMBÉ DO SUL | SANTA CATARINA | Brasil | 4218103 | 42 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 0bc6b824-ce56-3f60-b078-303cfba55d09 | -28.7153 | -49.90046 | 2025-08-01 12:57:00 | TERRA_M-T | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| dd88b127-898f-3124-8f0c-43474e28116b | -24.01097 | -53.75548 | 2025-08-01 12:57:00 | TERRA_M-T | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 6ffb3165-080d-30f8-a46e-e270851c9a75 | -25.21387 | -48.9897 | 2025-08-01 12:57:00 | TERRA_M-T | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.8 |
| 64e72e88-e6e4-30fd-84ca-3bf802a3f176 | -28.71696 | -49.87234 | 2025-08-01 12:57:00 | TERRA_M-T | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| ba9fafe2-3259-3017-846c-33e63a80586e | -29.93533 | -54.77289 | 2025-08-01 12:57:00 | TERRA_M-T | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 29.1 |
| 6ea7c7a0-d7bb-3ba9-b13e-c97a820f5945 | -28.71452 | -49.90612 | 2025-08-01 12:57:00 | TERRA_M-T | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| 953a7516-ce77-3da3-8c95-f34811b63c57 | -8.051 | -43.1237 | 2025-08-01 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 164.7 |
| 420893f9-75e6-3adb-a3d1-32b1f406ab46 | -8.0513 | -43.1001 | 2025-08-01 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.8 |
| f7876b50-9452-3146-99a7-9d1e9eaf3d71 | -6.7294 | -59.1723 | 2025-08-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 206.8 |
| cfe9ea87-ea9d-32e6-ab11-6077a85cd0c4 | -6.8026 | -59.2658 | 2025-08-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 248.0 |
| a4672abe-834a-3cf2-8b65-4f9262cf67d9 | -6.8395 | -59.2643 | 2025-08-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 496.7 |
| e552dc1d-f6ad-317d-809c-51a5a7e57e27 | -11.7666 | -44.9986 | 2025-08-01 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6baf9e1d-b1c5-3d41-9d9c-cc5de66cebfa | -6.8212 | -59.2458 | 2025-08-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 180.9 |
| b02b5d53-17ca-3391-a763-9778e7b83338 | -6.8397 | -59.245 | 2025-08-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 658caf5d-7049-3912-9a16-a3ddcd2a3eb9 | -8.0321 | -43.1257 | 2025-08-01 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 4d104e59-cdba-3fdb-a000-2bb26400296a | -6.8211 | -59.2651 | 2025-08-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1262.4 |
| 7af74a49-5925-3aa1-b073-133c75c9165c | -8.0324 | -43.1022 | 2025-08-01 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| a5e372e0-8934-344f-8c65-29bdb98eb5f1 | -6.7478 | -59.1716 | 2025-08-01 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.2 |
| e12ef8fc-e0ca-3e9c-8c50-d27372b0b3de | -8.0324 | -43.1022 | 2025-08-01 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| 1b7bdf62-948e-34d2-813b-4380b7578474 | -11.7666 | -44.9986 | 2025-08-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 74d0e299-ab0a-34cf-993e-c1c667c3bb7b | -6.8211 | -59.2651 | 2025-08-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1278.5 |
| a2d5f10b-5709-3268-a0e0-343fc0825abe | -6.8026 | -59.2658 | 2025-08-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 58520ec0-5c71-3d72-b78d-57a42e755fff | -6.695 | -43.0709 | 2025-08-01 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| bbd0ef72-f5e7-3548-9c77-bbb28cf99a6b | -8.0321 | -43.1257 | 2025-08-01 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| 27a1d2b2-64f9-3a69-897b-51396301b61a | -11.1884 | -51.5035 | 2025-08-01 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5c32b4f2-64c4-3e06-b1b5-65fe0caa1929 | -8.0513 | -43.1001 | 2025-08-01 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 198.9 |
| 64336891-57a2-3ebe-ab1b-082019ee8cfd | -6.8397 | -59.245 | 2025-08-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 9c04797b-487f-3c72-b842-28801b828d9c | -6.8212 | -59.2458 | 2025-08-01 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 294.3 |
| 9a5eb019-7c96-331d-9731-8735abeb78f1 | -11.1884 | -51.5035 | 2025-08-01 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0cd23abd-5042-331c-92b0-02c9bb1e1279 | -6.7139 | -43.0691 | 2025-08-01 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| d292c60c-7ff1-3fef-975f-273530a7117f | -10.5974 | -45.2767 | 2025-08-01 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 7d114c78-8347-355a-baf7-0db608f8c561 | -11.7666 | -44.9986 | 2025-08-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 313bbf09-a668-37a1-9ec9-891953bdfedb | -8.0324 | -43.1022 | 2025-08-01 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 161.6 |
| 344ab3db-59e3-3685-ae5d-34ee4fc550ab | -8.0321 | -43.1257 | 2025-08-01 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 198.3 |
| efd1a567-6f01-38d2-8c48-b7ec7db215b7 | -6.695 | -43.0709 | 2025-08-01 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| daa7385b-1714-39aa-af6f-258f9fc3a6e1 | -8.0513 | -43.1001 | 2025-08-01 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 175.0 |
| 85c2939f-80b9-321a-bab4-018d532bb6ec | -6.695 | -43.0709 | 2025-08-01 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| d6720627-f9a2-3799-9762-d4381fc70266 | -8.0513 | -43.1001 | 2025-08-01 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 156.9 |
| ffd9cbf0-a89e-3ca0-857a-d9f956e854b6 | -8.0321 | -43.1257 | 2025-08-01 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 189.0 |
| 3a2e6550-f817-3e54-899a-613e4a0ce4b6 | -10.0815 | -46.7441 | 2025-08-01 13:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 085548c6-44d4-3380-bfe8-87de3f254924 | -8.0324 | -43.1022 | 2025-08-01 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.9 |
| 0e62cbdd-26ac-3685-a808-9bb18f4f3c15 | -8.051 | -43.1237 | 2025-08-01 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.6 |
| f566e564-082a-3d3c-b54b-2e4cf89fdd06 | -11.7666 | -44.9986 | 2025-08-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| cd5bf799-7ff5-37a6-9a78-9bc18cfdf4d7 | -11.1884 | -51.5035 | 2025-08-01 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 195.9 |
| cf19b3cc-c56e-3679-9683-0dc714f150ab | -8.0321 | -43.1257 | 2025-08-01 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 238.8 |
| 2e23d768-33a5-3d79-944d-4f24528e5792 | -8.0513 | -43.1001 | 2025-08-01 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 179.8 |
| 2fdf2ba9-61bf-3db8-8c80-deb54f83c113 | -11.1884 | -51.5035 | 2025-08-01 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| ceb65058-80dd-344a-a9cd-ad957de1b58d | -10.0815 | -46.7441 | 2025-08-01 13:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 7e075459-f4f1-3bd6-a928-852355ec0cb4 | -8.0324 | -43.1022 | 2025-08-01 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 187.6 |
| 55707fe6-32bf-3ca3-8a9a-977a827d8f65 | -10.5974 | -45.2767 | 2025-08-01 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 93353639-b613-3c8a-87e4-752001b03644 | -11.767 | -44.9754 | 2025-08-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8a15dc1e-30bf-3c87-82c2-d1a112cbb962 | -11.7666 | -44.9986 | 2025-08-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 29ce2572-aae9-36e6-870c-3adddbec3229 | -11.7666 | -44.9986 | 2025-08-01 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |


[Clique aqui para ver as próximas entradas](README31.md)
