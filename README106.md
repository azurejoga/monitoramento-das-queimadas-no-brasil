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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fe0ea98-5220-35a7-9b7c-d79b3e9f8352 | -6.94795 | -59.36754 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9ee0baa2-545e-3313-b092-e4336d1ad910 | -8.32348 | -49.1181 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3fcdceb-50e6-3c82-91cc-8eb71bb21cfe | -13.1785 | -54.31157 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1029049-4e4b-3bfb-b875-eb0ba111e1c4 | -7.58224 | -45.64038 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29f7ccb8-dc40-31a5-9d8d-24706cbceebf | -12.2122 | -57.13769 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87c3a1a1-66bb-31d6-9861-b9becb3f5bf7 | -12.20884 | -57.12682 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94279f40-e969-388f-967e-69d25b90c22f | -12.21348 | -57.13116 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 564cb6c0-f32d-3be6-8ba8-59c39e44401b | -8.3332 | -49.12357 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 130bf15a-393a-3995-8bc8-0b0198cbb3a3 | -9.22824 | -45.659 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f543157-74aa-36b8-86a4-ec660a85f0a0 | -13.81732 | -44.19066 | 2026-10-09 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1a70d5c-4e49-3264-8b58-6c28192781d3 | -8.96996 | -45.16659 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9f0ddc99-5edf-33fa-bdea-4b9a7baeb054 | -5.81764 | -53.82921 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10be901e-d074-3599-8c4f-765894b49321 | -10.23242 | -48.0443 | 2026-10-09 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81eda801-5f9d-3fb2-b04a-e08b74c7e72e | -9.07728 | -45.10574 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9966220-4efe-3172-9a5f-d248ae03ca1c | -12.01233 | -43.49469 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6492fca9-db67-3276-a30a-ffec4b84b6d2 | -8.84647 | -45.42284 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e943e7-fe40-340c-bef8-20f8d4a5dc34 | -7.08357 | -52.68567 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e862754-e917-3a56-a0cf-5b8f3bd80f60 | -12.23123 | -57.09638 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 01501f3a-f06e-3bd8-bc7b-86287154d8ac | -11.76805 | -46.76761 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36c6c6bd-dcf9-3042-8c03-37ba1aaa9c3c | -8.01281 | -47.1616 | 2026-10-09 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 030f40f2-691e-3684-a013-536cf002cb58 | -7.1875 | -52.61036 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c95d99-ca06-3113-986b-7d24eaf0ac4d | -5.22385 | -60.04926 | 2026-10-09 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c9a55a9-b44e-3f8a-bd43-cd43a078f83d | -8.9978 | -47.73684 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7adf6dba-358a-3529-884a-901d33439ce9 | -6.57945 | -53.0138 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0b3b13e-6800-3fd0-85ac-d2b9102df9f7 | -14.4458 | -47.05839 | 2026-10-09 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f294de9b-a8e6-333c-b9b7-f22054eba60b | -9.87041 | -47.47033 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36226faa-93d5-3fc1-b2ad-cf024b37c95b | -11.63997 | -43.69719 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 859c8150-2c5b-36e9-aa7d-4c6d5172112a | -7.51654 | -47.33165 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 87d4a69e-abd0-3e0e-b689-d69fe6f430dc | -11.86978 | -43.60149 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0c3b593-8950-3da0-9074-7e1104b80b3f | -10.92505 | -45.38421 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e6095ad-7960-3792-bcaa-b1923c841824 | -7.38269 | -55.21381 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fa69688-17d4-36a8-b082-15f303a29599 | -6.49715 | -55.96149 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a190618e-d82e-3921-8304-2619b65da41b | -6.51382 | -55.41045 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e25b3dec-7ef2-323c-a17a-3692008a4768 | -8.22226 | -46.38602 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 342bc6e8-122b-30e2-8a07-99ab3484f8e8 | -12.24109 | -57.10195 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9743d33-d146-3b18-aa16-c12f81d6241f | -11.85446 | -48.03153 | 2026-10-09 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff9c2258-c300-3c2f-b8f5-7b8378b24c32 | -9.9105 | -44.78691 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ed565623-c5c3-3a80-aae2-f94052e2fcdb | -8.24804 | -54.73049 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffa99a1d-46ca-3fc0-9757-9835ac3a6d76 | -8.98622 | -47.53112 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0167af9d-3d6c-3f4e-af82-bdcf776084cd | -7.51599 | -47.33512 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37055b2b-4d95-3767-9fb2-cd906789ece1 | -13.16313 | -54.34789 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8d85844-cf05-330a-bf2a-e59335ef8090 | -11.76394 | -45.46881 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffc98bfb-a0b1-3127-a838-fc38d1f6f2c2 | -7.58007 | -45.65452 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 809b3461-2de5-3724-a021-6ee1bd7e45b7 | -12.21538 | -57.09344 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e732544-835e-3ea3-8413-11a6f0b97c31 | -11.06212 | -44.06004 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d50bf06b-5ea5-3fe0-b933-d3bde95c092d | -6.46127 | -55.49425 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 895542b2-3344-3240-b460-4e650dfbde0c | -11.65319 | -43.685 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ae40aa3-7e10-3ae9-8037-2185936561b0 | -13.20497 | -54.37208 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0436f3a5-af8a-39ee-ba8c-fe9105527a86 | -7.4765 | -42.85585 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 116dc15e-217c-31f3-a625-2a47831f79eb | -7.53545 | -45.87823 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed057ea1-1c87-3cc7-a66e-3da426442a0b | -11.64244 | -43.7069 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 20780c54-cbf3-36ad-8b84-1fa94baaf2f0 | -6.73131 | -48.11654 | 2026-10-09 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32ffe1bf-33f8-3d81-b01d-4c8e4d633f82 | -6.45344 | -53.69017 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a65c406-3dfe-3e18-b07f-03d7a2bb11df | -8.03803 | -49.40056 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 338683a1-ae67-36dd-9c3b-f819001b0a42 | -7.51174 | -45.76671 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57dda690-3e3e-3105-b37e-f457d9df9820 | -11.75013 | -61.06673 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 69ddfdf1-fb14-3743-a943-09008d5098ca | -13.73032 | -43.86906 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c8d80bd-ad18-3ed8-bc50-8c0ddfb8d27e | -12.23058 | -57.09971 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b807346c-b194-3bb0-88f8-271a762ea73b | -9.20879 | -57.72734 | 2026-10-09 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8be35093-5413-3564-8428-7ab4e093ba7e | -11.76199 | -46.785 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81986cbb-880e-3966-ad63-07bf3ca807a9 | -8.08152 | -45.64128 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 857ce8c6-e7d1-37b9-a87f-4d55c3aa501b | -13.41003 | -43.72593 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b5d76df-111e-3cd4-9414-b8a57b16bc11 | -11.83923 | -43.59954 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a313b91a-f25f-3051-8184-04d3b244c033 | -13.15971 | -54.35048 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eef7c94e-ab90-3898-a889-bc80172bcecf | -13.44405 | -50.45646 | 2026-10-09 04:27:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59268131-3850-351f-863a-43bccdf88804 | -8.74265 | -45.13969 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1a1a3fe1-0272-3adc-b0d9-ca18b62ab2a1 | -13.19709 | -54.36623 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d0dc2c0-c49a-3aed-a3fa-b49ea6e7b813 | -8.91051 | -45.21444 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6568b6eb-e6b3-3635-b7aa-0bc3a433c3fc | -14.43196 | -43.93016 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96571e61-6a66-3dcb-9570-77c7254187e7 | -9.00243 | -45.91423 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bfc1c53-28f4-319e-89cf-30c8e1ab22e9 | -8.32286 | -49.12191 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ddb381d-7ec1-3acb-87bf-50cb740e1816 | -10.99583 | -45.40226 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f8042b3-5d26-37eb-a47d-953e612bfdc8 | -7.38104 | -55.22305 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52a2fde1-a56d-3aec-b235-5f938b8f827f | -6.1331 | -53.05756 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a88d2ebd-bc12-336c-ba39-798d12414cde | -11.00786 | -45.41577 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7293dc69-e7b5-3520-8ad8-c993eca9bf4b | -8.65644 | -54.53889 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50206a25-984e-333b-b977-f2737d42274a | -10.36701 | -45.12952 | 2026-10-09 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c02f3ca3-2655-321d-b6d3-4f055b4d1975 | -11.779 | -43.53265 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd7b3986-1a5c-3624-a586-a6705151f472 | -11.60499 | -43.69448 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72c1bcb0-b90a-3177-bf15-786522d291df | -6.92913 | -59.26063 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a57365ea-c47e-3876-b548-dcb74be5e86e | -11.18352 | -45.31622 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73d3af05-b986-3c1b-ae1d-779e094372d6 | -14.44349 | -43.93186 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66698556-239b-3393-87bc-adbc42d5b34d | -8.97687 | -45.92484 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa30cb5c-9e65-332a-b526-270b28776ddc | -6.48583 | -55.28835 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f49a28c9-5c57-306a-942a-1c18dbbb336c | -7.41083 | -44.76245 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 126d74dd-5d59-3ebf-994f-ed3829db476d | -13.26169 | -47.0027 | 2026-10-09 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 111c9044-da63-31e4-96ee-675b949f6f88 | -7.3983 | -44.75293 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1081368-c4c6-31cb-8fd9-be38fe62709d | -12.22056 | -57.10055 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| e70a44bf-faab-3646-bbcb-6d523888e1cf | -11.7535 | -44.92796 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bd49b4d5-4361-30ef-ba1a-7000043c621a | -8.25974 | -46.91046 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d6078dc-9c1f-3461-8aff-df0d37df6161 | -8.67127 | -47.08589 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92c9e438-5e8c-32d7-8b65-269b18b43a2f | -11.84126 | -43.58546 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff667ec9-5a23-39bd-bad1-874823f11cd1 | -10.28439 | -47.82286 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ea1219b-a03c-30e0-aeb9-471320dc7942 | -11.22493 | -45.32266 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5142e89-690a-38d6-9080-65595b38b746 | -12.23519 | -57.10416 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 58a1a78e-6093-349c-bf43-27f1c263e997 | -13.37717 | -43.87819 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc64fc0e-2eaa-3db8-a650-b392eef66278 | -6.14213 | -52.90181 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89783f35-3292-3dc4-85c0-e4fb29cc1d33 | -11.78836 | -45.5854 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d84185d8-6341-3fd4-b376-65ac4100fdf5 | -13.16324 | -54.35557 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 898b5cf1-84c8-3b04-a399-a44c254bb42b | -5.87939 | -53.52143 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README107.md)
