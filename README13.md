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
| 00588cad-0bde-30a1-9bdf-5b4c1091bcc7 | -8.9213 | -60.7489 | 2025-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 94e15dde-b55b-348f-8e37-a218ab906c8a | -9.3808 | -61.5124 | 2025-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a5947c98-a87c-3cdf-a823-dc46fd3ced5e | -8.9401 | -60.7288 | 2025-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 50e52b22-f343-3247-90c7-33eb39da9049 | -7.0615 | -59.1779 | 2025-08-10 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6a52b02f-7798-3a29-af0c-564541dfa3cb | -7.0614 | -59.1972 | 2025-08-10 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| eec7b956-f570-3e70-84be-d65e6f929262 | -9.362 | -61.5324 | 2025-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 22e36114-1471-3cb0-b600-cfb90507604a | -9.3806 | -61.5315 | 2025-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| e45489a1-634b-3bf8-ba0a-b085a55c9d41 | -16.3731 | -42.5425 | 2025-08-10 04:20:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a5ae4e59-44aa-3de7-94c0-d06c23091727 | -8.9399 | -60.7481 | 2025-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 930e2b99-ae89-3d1c-8c07-d6688140be3c | -7.0799 | -59.1964 | 2025-08-10 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 14ca0692-684e-3c6d-b822-395380bbeb22 | -9.65557 | -45.36546 | 2025-08-10 04:21:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9adca8be-95be-3b18-9738-88576a76f6d0 | -7.29097 | -44.1612 | 2025-08-10 04:21:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99cfe2c4-4db2-36cb-b9a4-93dde0808e6d | -6.19092 | -46.09885 | 2025-08-10 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e4358c5-2a4f-3f2e-8859-19f0bd289198 | -6.36875 | -44.68483 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28ff9ed4-85e2-3c36-a8ef-a2cfe931ff79 | -6.34864 | -55.56382 | 2025-08-10 04:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcf1142e-0549-3074-8f5d-d5059757d236 | -4.30076 | -48.07761 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3fc974e-4c13-313b-a09e-c8f131bc7406 | -3.83695 | -47.74597 | 2025-08-10 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cde96ca2-2f8a-3ca6-a6f9-570251e58442 | -7.34515 | -44.59063 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b491f2a-dadf-3fc6-a786-9ee341f50594 | -8.30116 | -45.00588 | 2025-08-10 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2adecfa4-8321-3f44-bfaa-0107a5bd545b | -4.29457 | -48.27477 | 2025-08-10 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba80a1a8-041b-3d43-89bc-c526cd58eb17 | -8.36886 | -46.98297 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d1b95d2-a07b-3e1f-a90a-40343b694120 | -7.21629 | -52.60968 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86977341-0375-32d5-b798-df1b0133cf8d | -8.07545 | -46.85137 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7a58a2d-a9b5-332f-a712-cb961f41e118 | -7.04867 | -43.5667 | 2025-08-10 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba9fdf15-8e4c-3fa7-9072-744b8cbef767 | -11.75074 | -45.02896 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19474a04-afba-32f6-8d1a-08635a432463 | -7.51734 | -49.56121 | 2025-08-10 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b259b8dc-e8c5-3de3-bb84-83ee38ea8b9f | -11.72846 | -45.01812 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 804d0676-abb9-3f25-9b3b-f22d33042ca8 | -6.98449 | -44.79734 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c63deba5-ab05-3b38-bf42-aeb194d75624 | -11.11608 | -42.35528 | 2025-08-10 04:21:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6de292fe-6663-301c-80e8-81b09dda49ed | -6.58714 | -43.39705 | 2025-08-10 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1b288d0f-df81-30c6-ae4d-95c451b514b4 | -7.41839 | -43.9939 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb57dabe-bd92-32e6-a342-aa5fb4de8dea | -5.84629 | -42.94924 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb72a92c-f282-3ba6-afab-76d4f346c9d5 | -5.84912 | -42.95337 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| be297008-3526-38d2-88d4-32918ea2e1fc | -7.39417 | -39.68034 | 2025-08-10 04:21:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 04120ab2-66fc-3c3f-aca2-81fb636d7ab9 | -8.98254 | -45.68419 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8575d729-48d5-3b46-a27f-6772ded5ab2a | -6.0611 | -44.89952 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ba1d3c8-73ad-3efe-bf56-55fdba142436 | -7.59588 | -44.41648 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0f6250d-6445-3113-8dad-12e1470ecf4c | -6.67952 | -44.73439 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1deafac-e1d6-3231-91fb-7ab4c7c509dc | -7.69855 | -45.54258 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92b2d21b-4f32-3074-a548-c15a2288dd8b | -6.18164 | -44.58446 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb3c0c7e-1d50-36e0-80ef-d60c6af8d6a9 | -7.70745 | -45.52961 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d671168c-4d3e-3ac6-8767-cc2d0e0adb70 | -11.75129 | -45.02538 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7c794fe3-2cea-3638-b316-d9cb2d1f710f | -4.30332 | -48.08017 | 2025-08-10 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fdcba18-1d30-345c-969f-c9e8df29d4db | -4.07081 | -47.96996 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc81919b-f2b1-35b8-b841-6e6e05f05193 | -5.47364 | -44.69938 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c7706e9-8cf4-3259-a185-d07d06d321a2 | -7.88584 | -45.55497 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b0ff31d-b6bf-378e-ae47-61e8c237c768 | -5.47309 | -44.70284 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8845a82f-0279-36d4-9b9e-c6473bbcbfb9 | -7.55785 | -47.0448 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e45a6248-9ee6-33c2-91c2-af80d976e818 | -6.57662 | -44.57253 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e88e6342-6867-3d8c-a256-c3d8ccf9fcf1 | -10.23577 | -45.31181 | 2025-08-10 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6f281c8-1ca1-302f-a224-8fae65d832ce | -7.87307 | -45.54934 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc26c7e-b2ea-3973-a63a-f36d35890217 | -9.49409 | -46.29176 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7bbaaeb-2878-3ad5-9348-0df69f95381d | -6.58048 | -44.56959 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c9b0e4c-7dbb-3827-8e76-35e84cee02e3 | -5.31814 | -44.35593 | 2025-08-10 04:21:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 955e795b-0bd1-3f6f-923f-2d02ee8bee70 | -9.87312 | -49.95206 | 2025-08-10 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63d3ae0b-f8e8-3a68-abb1-37259c1dfef6 | -6.05642 | -43.74931 | 2025-08-10 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e1f7b5d6-4fd1-3705-a0de-6f3aa04136f7 | -10.96371 | -44.85365 | 2025-08-10 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f29cfb1-ace4-3493-a9c2-6bb960f56bc2 | -5.39335 | -41.32759 | 2025-08-10 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f35c19f-cc8e-3776-8706-31d9ca71f13e | -7.05089 | -43.55241 | 2025-08-10 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78cc29f4-32d9-31d9-82a1-3567c9c0f7b7 | -5.38618 | -41.32631 | 2025-08-10 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d8df926-78f4-340e-b5e9-a510fdb4ef9f | -6.94812 | -44.55332 | 2025-08-10 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dea948f1-00e3-36d9-a155-13944d779502 | -8.49786 | -44.74844 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b931aaf-63ff-3d5d-be2d-622a631c8920 | -7.56561 | -45.41732 | 2025-08-10 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 332b1cfe-6259-35ea-9813-32119c7245be | -8.08521 | -46.85292 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24ed33eb-9ac1-3f71-9f82-1f490981e9d3 | -11.72901 | -45.01455 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f1c5297-ef52-345e-932a-f2eb1bc339f1 | -7.3435 | -44.60106 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 906d5a28-0432-33d4-a13b-6e0fb30e87ff | -4.95532 | -47.59584 | 2025-08-10 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 316339e5-463b-32f0-afe9-d5f00b90c2c7 | -7.3947 | -39.67674 | 2025-08-10 04:21:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c4fa8ec-de0c-31f9-943f-a2e94406ce78 | -6.19772 | -46.0999 | 2025-08-10 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b41820aa-e1c9-3597-a460-7fb18700170b | -9.49188 | -46.2841 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c11d32ac-924f-3036-a739-c842f3d75ba5 | -8.08582 | -46.84917 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58bd0688-b9a9-350e-8370-906f98204bea | -8.30171 | -45.0024 | 2025-08-10 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db3e51d4-a276-355d-a2fe-7adf1b6cdaa3 | -7.88651 | -43.54499 | 2025-08-10 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24b5efbe-5b63-3182-9501-d52da98dd01b | -9.49629 | -46.29942 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bdfa5eb-521f-3557-a87f-5c36186e3400 | -7.1143 | -44.22646 | 2025-08-10 04:21:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35148359-8a8a-31c7-af12-7ed9837ff2d0 | -6.11054 | -44.63022 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80de5b20-15b9-3c17-8cf9-cbd4dfd04019 | -10.46119 | -47.94804 | 2025-08-10 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e0e95bc-0408-3a80-a334-f63f1ba48f27 | -5.32736 | -45.14744 | 2025-08-10 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e33e3171-e196-35e6-8b91-8d7d55d0061e | -8.11914 | -47.4341 | 2025-08-10 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0d6a73d-e577-3922-a227-2e1ef99d6b42 | -5.3826 | -41.32561 | 2025-08-10 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 410cb0dc-a8a9-33a6-85b1-cb02d3a03dc6 | -6.98781 | -44.79787 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c6c2664-b2ff-38d9-a1b6-b30628a6e126 | -11.73011 | -45.0074 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 269ee1dd-1f05-3424-90e0-8a05e2a89a99 | -6.19132 | -45.44294 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 50a15012-75bf-3c85-a8c8-4b586fbcf14d | -4.34905 | -47.53857 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4c5c54ef-1780-3314-b217-1cb8e2d9c53d | -7.34459 | -44.59411 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c8e15d0-59d6-3ffc-b062-a52f3cd0a3cc | -7.72688 | -45.5364 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d3b0f36-7ff9-3d99-a71d-1fd86649e9ec | -11.74684 | -45.03202 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50d9d260-6541-33a4-9bdd-6434b64251f7 | -11.73836 | -44.95387 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 502640d0-7783-3393-b56a-990b94b1d591 | -9.86269 | -49.96569 | 2025-08-10 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a851013-c326-3d6c-8140-31436e639351 | -7.87528 | -45.55687 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d5f6629-c626-3d8e-8769-96ccbe799d1c | -4.14479 | -46.45478 | 2025-08-10 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84656865-2456-397e-8eba-98297a1457b8 | -9.64098 | -48.34715 | 2025-08-10 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5ba4fd9-50f4-3c85-a2fa-209dc7e8a14a | -6.57716 | -44.56906 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fecc10b4-692c-3537-8708-b69282a5be94 | -6.13424 | -42.96274 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f2982880-ab59-3517-ba51-f5de49a14c99 | -6.54257 | -43.18828 | 2025-08-10 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3ee2783-d686-371f-aea8-49f6b0eaca31 | -3.96918 | -47.88061 | 2025-08-10 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f6aee3a-3d69-35a0-97b6-ac42b1eabf0e | -7.87918 | -45.5539 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 676d4614-67b4-3c18-9642-6709b04cd486 | -10.44013 | -44.34391 | 2025-08-10 04:21:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 670591e4-ef8c-3c01-afe4-5925ea0b6b43 | -7.32265 | -44.69027 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5ec2520-af25-3b16-8f6e-e1c3c24b800a | -11.73906 | -45.03812 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README14.md)
