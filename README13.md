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
| 49275e88-e8fc-3f1d-8bd4-48d7002b21fe | -1.7691 | -54.4928 | 2026-09-15 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3c00246a-3794-3c1d-afed-96d375484ee6 | -9.5152 | -40.331 | 2026-09-15 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 190.9 |
| b49c53a7-9c0e-3f49-bc7b-50f1d6f4aa46 | -2.6966 | -57.5889 | 2026-09-15 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 661a44e7-02e5-3ff5-aa02-f9bf51eb76cf | -16.129 | -49.4993 | 2026-09-15 00:30:00 | GOES-19 | SANTA ROSA DE GOIÁS | GOIÁS | Brasil | 5219506 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| fe4636bd-5604-3b27-9343-13a735a1e773 | -2.9209 | -50.4208 | 2026-09-15 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 474067ca-85a1-358e-ba1d-6a7a9ee9cf01 | -5.1256 | -55.9352 | 2026-09-15 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9fffafd5-1f9c-32d9-8e25-ef86e9822dde | -11.1208 | -40.478 | 2026-09-15 00:40:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 60.0 |
| f11d11d1-fe38-3c71-ae51-6ac996a063ed | -2.9024 | -50.4423 | 2026-09-15 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 52bba898-9c2a-3165-a979-01cc76e9e186 | -6.7195 | -48.1201 | 2026-09-15 00:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ed35c80f-5569-31bf-aaaa-81f2c45fd697 | -3.8957 | -60.5984 | 2026-09-15 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 3910accc-9bc8-3dd1-a685-1d624f11b4b2 | -4.6774 | -42.0951 | 2026-09-15 00:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| f9214585-8179-3152-a761-5dad2f107a21 | -1.7875 | -54.4925 | 2026-09-15 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| caef7061-42b8-3ff5-80b0-5ec9068208a8 | -2.9025 | -50.4214 | 2026-09-15 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 02314b9a-ef1a-3355-9fc5-a71e24fbbf24 | -6.9612 | -44.5316 | 2026-09-15 00:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 428a126d-d903-319d-a28b-7afc805e7a5b | -9.5156 | -40.3061 | 2026-09-15 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 091400d8-5c13-36b0-ba40-d2869431b8b4 | -2.6783 | -57.5893 | 2026-09-15 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 9e5fa132-8a6f-329a-943a-d89e410909b7 | -6.1109 | -57.684 | 2026-09-15 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 68c6cba5-c58c-3354-9a4d-4bebbca35a44 | -6.8446 | -55.5611 | 2026-09-15 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c2a01a87-75cf-33c6-a3e4-61ba74804357 | -10.7572 | -44.8184 | 2026-09-15 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 980e1d7e-a4ac-3992-9a0b-781acb3d553e | -11.884 | -43.8142 | 2026-09-15 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 22af77e9-d928-34a9-9eb1-82bbc7cdf900 | -3.3637 | -61.3282 | 2026-09-15 00:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 79ac3ce0-d05d-3b29-94e4-faa001a06f23 | -3.1816 | -61.1235 | 2026-09-15 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2e51d3dd-b6ff-3233-a863-4d4b72166f94 | -3.382 | -61.3279 | 2026-09-15 00:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 14705955-08dc-3e2e-8bd9-f0a8efb61835 | -9.5152 | -40.331 | 2026-09-15 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.0 |
| b45a234c-cbfb-3ed2-aa8e-bec417fce492 | -11.9033 | -43.8112 | 2026-09-15 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4749305d-3864-3189-845c-a9f3673076f0 | -4.6589 | -42.0726 | 2026-09-15 00:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 83cb1f11-5ae9-348a-94e8-943af2f60f0d | -4.6587 | -42.0964 | 2026-09-15 00:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| d468c873-4a32-3fc2-bca9-630119f3ba5e | -15.2827 | -42.783 | 2026-09-15 00:40:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 5467527c-0527-339a-98b6-626d45ac3908 | -9.5343 | -40.3282 | 2026-09-15 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 922e2098-7f2e-3095-a059-8a1e193f3dec | -4.6776 | -42.0713 | 2026-09-15 00:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| df399978-aa00-3f6d-9fbc-df53c1b22b8a | -5.4297 | -43.9869 | 2026-09-15 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2eca378d-50fa-39f1-a22f-40e66f4ebb7b | -8.0924 | -50.9642 | 2026-09-15 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9322eb41-be91-3fec-a231-befd069a13b6 | -18.1709 | -51.7685 | 2026-09-15 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c2cc25d9-033a-3629-b08b-b3ffcc19c82c | -8.0924 | -50.9642 | 2026-09-15 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ba8fc2c8-81e2-34af-8f19-0d2b854b2bf4 | -13.3391 | -51.6176 | 2026-09-15 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e90bd3ba-4cdb-38d6-8f8e-989974045930 | -6.7195 | -48.1201 | 2026-09-15 00:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1910d517-6055-3f4c-b3f3-e2764b000d34 | -15.2827 | -42.783 | 2026-09-15 00:50:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 197.0 |
| a484e5cc-33c9-36db-b416-89c173f44193 | -11.8836 | -43.8378 | 2026-09-15 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 22f0646a-2d44-3806-a2af-7b0b80bb9682 | -9.5152 | -40.331 | 2026-09-15 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 135.1 |
| 4fe7bd07-b9dd-3b3a-bef7-f77f2b1aa50f | -4.115 | -60.6886 | 2026-09-15 00:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 06da8a53-715b-3368-97c3-c4b339239468 | -2.9025 | -50.4214 | 2026-09-15 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 09cfdbab-eda1-3dad-a264-80f792d3cab6 | -3.5336 | -53.9939 | 2026-09-15 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 56b2d4fc-2b8c-3e86-9ff4-297f7a715f90 | -5.1256 | -55.9352 | 2026-09-15 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ccb0aa24-db29-3da4-926f-b7e39e931ace | -3.382 | -61.3279 | 2026-09-15 00:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 519dd3a4-a7e7-367f-90ab-d5857874bdb2 | -6.1109 | -57.684 | 2026-09-15 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2e247f9f-b3dd-37cb-84a6-9723b2f48e83 | -4.6589 | -42.0726 | 2026-09-15 00:50:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| d7566b3c-aa0e-39d8-ade4-55006a739655 | -9.5343 | -40.3282 | 2026-09-15 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 3a46c2cf-ad25-3005-9619-0c815f5e64e3 | -15.2833 | -42.7585 | 2026-09-15 00:50:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 85ccd269-fe72-36ae-95e9-77942c9fbea1 | -5.1255 | -55.955 | 2026-09-15 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ac5a8c82-4eb0-3847-b038-ecbf89129f77 | -6.8446 | -55.5611 | 2026-09-15 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5b18d228-261f-351a-8f79-cb33dfb280b4 | -18.1714 | -51.7466 | 2026-09-15 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| cfbdda96-8b33-3f2d-90d4-27986f32c30c | -2.9209 | -50.4208 | 2026-09-15 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b5cfe3dc-8c9f-3af6-b98b-8520c730e15b | -15.3024 | -42.7788 | 2026-09-15 00:50:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3059e6f5-4ebd-3d54-8fac-db74961ed83b | -4.6774 | -42.0951 | 2026-09-15 00:50:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| d0336993-e8d4-3d76-a828-48e4ce35e86f | -4.6776 | -42.0713 | 2026-09-15 00:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 0297e321-f13c-3ac1-8f66-ebda576d7a02 | -13.3394 | -51.5963 | 2026-09-15 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9983def0-22b9-3f94-a053-24ef2a5ef858 | -11.884 | -43.8142 | 2026-09-15 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 837d1c65-9d9f-3a3a-af67-706b66300607 | -3.1816 | -61.1235 | 2026-09-15 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 94646858-f336-3adb-bf75-a18da3b3966b | -3.552 | -53.9934 | 2026-09-15 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 20b5817f-6076-3e68-831b-fc738d1dd84d | -4.6587 | -42.0964 | 2026-09-15 00:50:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| fd6bd24c-4a3d-35c3-b07d-0108d5716544 | -9.5152 | -40.331 | 2026-09-15 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 182.8 |
| 9a1612e8-5392-3406-8641-386ac1af4a63 | -10.7916 | -46.2298 | 2026-09-15 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 832e80d2-ac13-3860-87b4-483c46f77f42 | -4.6774 | -42.0951 | 2026-09-15 01:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| cbee961c-3e05-3e65-8936-0ecfe090e0e6 | -15.2827 | -42.783 | 2026-09-15 01:00:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 111.6 |
| aebbf854-8e8c-370e-9c55-69cb44d11622 | -6.7195 | -48.1201 | 2026-09-15 01:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 04cd8da8-c3fb-3749-a09e-6d20a9b05d76 | -11.884 | -43.8142 | 2026-09-15 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 8ea61963-8286-3dec-bb7e-69e9b9c2ddaf | -3.4272 | -58.2138 | 2026-09-15 01:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8fc831e4-0e15-3cc4-b520-040a0213a702 | -2.9024 | -50.4423 | 2026-09-15 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4cc8ec9f-51d0-3c04-a894-8a2af74371b3 | -6.6953 | -58.6903 | 2026-09-15 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 90f2beed-019e-36e9-9d29-fa526bdd6a05 | -6.8446 | -55.5611 | 2026-09-15 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d193356c-73d1-3d01-b0cf-2eb846e68a3a | -2.9025 | -50.4214 | 2026-09-15 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 06ca05be-121f-344a-b407-90313d70ed54 | -18.1714 | -51.7466 | 2026-09-15 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 133.8 |
| d70f6b25-bdb7-3db5-a7b5-48758d5b4acc | -11.8836 | -43.8378 | 2026-09-15 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9b0ecc35-a543-3405-bf76-939cfead94cb | -3.1816 | -61.1235 | 2026-09-15 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d1ba1109-f21b-349b-b54f-4e9bd8bc2b75 | -13.3199 | -51.62 | 2026-09-15 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| c7a13219-4487-39b8-9671-89c1301ff082 | -4.6776 | -42.0713 | 2026-09-15 01:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 2b4b5f03-a9e8-35b4-a241-855b4e293b1f | -13.3391 | -51.6176 | 2026-09-15 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 21f2d1a4-7a17-3fed-96f9-f0a52b527493 | -5.1256 | -55.9352 | 2026-09-15 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cd8f0285-3ebe-3eb5-abc2-7e472a801046 | -9.5343 | -40.3282 | 2026-09-15 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 206.3 |
| a24ce3f5-8c73-31c5-b95e-f9f72f57b799 | -4.6589 | -42.0726 | 2026-09-15 01:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 1397f12d-a879-39e0-a8be-51183dbedf2d | -4.6587 | -42.0964 | 2026-09-15 01:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| b099027d-5892-3fdd-aeb3-1e8ab8036b8e | -18.1709 | -51.7685 | 2026-09-15 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 73fedc72-bb92-3f84-b090-7f7b4b759171 | -2.9209 | -50.4208 | 2026-09-15 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8254e01d-455d-3bf7-8c63-cc6f57e65213 | -6.1109 | -57.684 | 2026-09-15 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 0262e875-0a2b-37b3-be56-be1146977099 | -3.382 | -61.3279 | 2026-09-15 01:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 265f5398-2ccd-3795-a248-64267865cb29 | -18.1714 | -51.7466 | 2026-09-15 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 879dbd56-78d5-3a71-a4ae-2b60ca28d509 | -6.6953 | -58.6903 | 2026-09-15 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 45985a24-5dc0-3e2c-b061-b387d83a92be | -10.7572 | -44.8184 | 2026-09-15 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 236c4a3d-4b67-33c4-97e8-963e9437cea8 | -11.8836 | -43.8378 | 2026-09-15 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fd25b94a-3042-37db-a014-2e75e3deea85 | -18.1709 | -51.7685 | 2026-09-15 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 795056d7-08b6-35f2-a217-ebdce982546c | -12.4901 | -41.4012 | 2026-09-15 01:10:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 9e5739e6-53fc-363b-af3a-25247559cdcf | -10.7916 | -46.2298 | 2026-09-15 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 141524e7-9709-321d-b963-0cb4af52f759 | -2.9209 | -50.4208 | 2026-09-15 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| abb3ee02-b825-313d-b209-28644c9a22eb | -4.6774 | -42.0951 | 2026-09-15 01:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 3b1c7f56-6e68-3ae8-97db-f389b84137fb | -11.1207 | -50.9179 | 2026-09-15 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| cc30737b-a384-3ea6-a602-53bc4d5aa6f1 | -4.6587 | -42.0964 | 2026-09-15 01:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| caae22bf-980d-332b-989a-3299d73adf27 | -3.3637 | -61.3282 | 2026-09-15 01:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9aad5437-3c85-39cd-bbe5-ff7e710e42c0 | -3.8957 | -60.5984 | 2026-09-15 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 5807fbca-5992-3bb4-bf81-d8e9e39a5813 | -11.884 | -43.8142 | 2026-09-15 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 78b2b748-6c04-39df-b520-3ae1f0d44f2e | -6.8446 | -55.5611 | 2026-09-15 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |


[Clique aqui para ver as próximas entradas](README14.md)
