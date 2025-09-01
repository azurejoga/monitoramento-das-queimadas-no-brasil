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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 636b52f1-4d4c-33e6-86dc-68843942524c | -13.38014 | -47.06968 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af03aec0-c3cb-3994-b23f-7c2e76f422bd | -12.62716 | -57.00152 | 2025-09-01 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a494df2-75d9-318b-b036-c74d377b9c30 | -16.40692 | -45.65262 | 2025-09-01 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa144a05-85e7-319a-8c0d-572e16ce0f3c | -14.53148 | -39.73985 | 2025-09-01 04:12:00 | NPP-375D | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 83100e6d-9b09-3819-a304-3d844fe71846 | -13.33616 | -46.99121 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01c4924e-70e7-3bba-a7fe-c74212f744dc | -13.64991 | -48.15671 | 2025-09-01 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d749f79-0c2f-3d5b-af99-2ffa0709caea | -12.57407 | -48.21076 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e908cb91-0d71-33fb-8a69-2c69f1d5ce91 | -15.6878 | -48.95008 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 353f8b1d-d7b0-3a3b-ae41-18e0a7e4324d | -15.7056 | -48.89812 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bf3b596-7c36-3b8c-807d-c96845a57819 | -13.70684 | -46.92941 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfbcda85-6d77-3a1b-a26a-609495166150 | -13.49724 | -46.9766 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a239675-3d24-3a1c-964a-eb9a21e370f6 | -13.5453 | -46.96729 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bce75225-4390-3c5d-a2f7-a0e99b779719 | -12.62239 | -48.19293 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51441214-7032-36b2-99c8-c23c2342dea2 | -15.6986 | -48.8904 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c465f0ab-38f9-3d62-9481-1105358bf487 | -14.64092 | -43.95967 | 2025-09-01 04:12:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1ed7bed8-9fd2-38f3-b059-848d8e1798fa | -13.32115 | -46.85381 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54242a88-4886-36ea-88ed-d796d9c03db8 | -12.85227 | -48.07452 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8462acf4-7032-328d-9322-f03b864079e9 | -12.96977 | -48.11555 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2fbf5b2-f9f9-3f37-a695-e69eb6a3b48e | -15.58838 | -48.31881 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b15f1967-400a-398c-927e-ac7b806c3b7d | -12.86648 | -48.06522 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3976f21d-630e-3a07-b3e4-346cc09a4a25 | -15.58346 | -48.32363 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 703b8afb-46fc-395c-950e-3f88dc4a4240 | -16.29135 | -52.93821 | 2025-09-01 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a767cec-ff65-33a0-83aa-b37568de29dc | -15.70144 | -48.8979 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdf0cea8-9c10-3cf5-821e-3b77e91a3c4a | -11.96459 | -51.36147 | 2025-09-01 04:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7ce7ef5-b75b-354e-b118-e58f69240670 | -13.574 | -46.93514 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b90bd575-42b2-37d6-ae57-674b86a7f241 | -14.04738 | -44.57667 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ba558cf-add5-3822-b3e7-5a997dc406b4 | -13.50012 | -46.98229 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7979b083-3676-3d28-9edc-fed7d46cf13e | -15.7021 | -48.89423 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76481f4e-c9bf-3609-b90a-85376f884dbe | -12.59804 | -48.21891 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 841c0aeb-ee07-3f6e-9799-870d52661387 | -17.02212 | -44.15693 | 2025-09-01 04:12:00 | NPP-375D | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78065436-601a-3193-93b9-f1e1afeeebae | -15.73154 | -48.95847 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0782d5b5-e842-3cda-a376-48c2cf871732 | -13.51046 | -46.98966 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb79d081-afd0-3d66-8cd7-b9a13dbaf745 | -15.32615 | -46.09857 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a74d517a-f9d2-3803-93aa-6d5379da7086 | -12.14259 | -47.19119 | 2025-09-01 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52ed32ee-aa72-309d-aece-a007b192c9a9 | -15.72247 | -49.00734 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| adb7422d-78b2-3dfd-bd5a-95fe33127fb8 | -14.74899 | -46.76637 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0d49591-adee-3354-a9da-ee8e2b00156d | -12.80457 | -48.08449 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca75aaf5-3610-3f65-964d-df40b03a14d1 | -13.68959 | -50.7631 | 2025-09-01 04:12:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 330751d6-b5fd-30b3-81e5-24c1908c73e5 | -15.72659 | -48.89826 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0a7d39c-2584-36de-a316-f7c3aa7256e3 | -15.60125 | -48.33794 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f1566af-1164-39c7-9416-47efb4c6471c | -15.30016 | -52.78844 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33961b25-f711-3bf2-955b-da252ff77cce | -12.80048 | -48.08395 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b97c28c-f9b4-3e80-ba1a-9b0321e210a2 | -13.48043 | -46.98407 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b51feaec-b278-399b-98d0-3a851054c9ef | -13.50388 | -46.98294 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e5969dd-acef-3e6a-8d0e-064dd864522a | -13.59443 | -48.14224 | 2025-09-01 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ea14dd0-1bc6-3b74-8ffb-1b18fee4d80a | -12.86981 | -48.06991 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd003829-e996-344c-9361-eed7d47df761 | -13.37511 | -46.94329 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| abfa692d-5a1f-3851-8770-2c345846bc48 | -11.96402 | -51.36448 | 2025-09-01 04:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 076f9ac9-5c74-3197-94b9-5934a8cd2046 | -13.69157 | -46.92447 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4bc08b4-8c14-35de-bfd5-198bb9e6b7d2 | -13.29425 | -46.89752 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4703f7d9-9096-33d6-95b8-cedfaeb7eff6 | -14.74979 | -46.76175 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd66ba1e-2927-313f-b820-09e862d1c7d2 | -12.64002 | -48.16541 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c87175c-c9da-372a-bc3a-e36ca678e10f | -15.69337 | -48.94255 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aca28ba0-70cc-3fd8-a9c0-d094625adadd | -12.97743 | -54.75543 | 2025-09-01 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de8449b0-fe2f-3d8f-8ede-6c06968b882d | -13.16913 | -45.28289 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3dc01aef-2516-38df-8bd0-6bac890f13ec | -14.82134 | -46.73744 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3754a6b6-fb83-3814-8128-41587bddb783 | -13.48712 | -46.99014 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 65f7ffa9-b9fa-30fb-be82-dfd3abcb83e6 | -13.3668 | -46.94651 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbba2490-64a1-3a89-b418-8be017a52863 | -14.37171 | -53.31057 | 2025-09-01 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b75b9198-978d-33fb-b0c6-8c8738111b04 | -15.72461 | -48.9958 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| adf664f6-9802-33ab-8c82-9ceac6edf1a9 | -13.39771 | -47.05829 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 665386cd-5534-3850-9cb4-49b3ab563cb0 | -12.56455 | -48.21673 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b15e1af8-f73a-341f-a984-abc9ab35053a | -17.72291 | -44.384 | 2025-09-01 04:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a73d84d2-c5f3-3d67-9374-6d819e04ad3e | -14.79079 | -46.74206 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f722ce74-e2f4-382f-9d72-94157c619192 | -14.85069 | -47.09937 | 2025-09-01 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dda2ba5e-07f5-3181-8331-90496e4c2c75 | -16.41035 | -45.65325 | 2025-09-01 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ef74169-4212-3663-a0b7-dc034774d68b | -14.81628 | -46.72473 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5a54c8d-a332-3e09-9842-1401fab3188d | -12.60475 | -48.20473 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73dfa058-959c-3395-a241-bdde4cbe7fd6 | -16.97212 | -49.313 | 2025-09-01 04:12:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81ec6129-c2d9-3ae7-b25f-8113268ec4ba | -12.41171 | -47.78354 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8839bf8-76f8-3123-ac6b-94fc8dac3e01 | -13.5461 | -46.96267 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 720b21db-6a21-31a2-a0e0-d29c286d4006 | -15.32595 | -46.05675 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d34a1f13-d51f-37ac-9a42-e426891ba4cc | -13.55059 | -46.95904 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bee9fb0e-da6d-31aa-9fe6-66ee24679e93 | -17.14981 | -46.08553 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b812e464-ae66-343e-a52b-810736cf5b33 | -14.78787 | -46.71521 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5307137e-7fb2-3e2f-a32d-c53581b439cc | -15.72324 | -48.89352 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2c2bf9c-62e7-3f45-95ed-7f274c9a8d3b | -15.6954 | -48.93131 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf41febc-08d6-3d2c-926d-2eb25dfea010 | -15.71836 | -49.00667 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6abd7750-ae8d-3adc-978b-5d5aafdefbe9 | -14.02102 | -44.61024 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ad6675b-43cb-3238-8b58-6280b0c438b3 | -15.71983 | -48.99874 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 763babf5-e7ff-3f0c-b110-fd0009390cc3 | -18.12036 | -44.98973 | 2025-09-01 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 232165ed-7a09-3795-9dda-5504c10b97c2 | -12.97783 | -48.11726 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8919aaf-4995-30bb-ad90-48eb8d782b5e | -14.04581 | -44.56503 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a9cbf3f-a87f-352c-8e51-155ab1104211 | -12.62869 | -56.9945 | 2025-09-01 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eda0b5a-5d45-3257-8ddb-b6a4d1518a98 | -13.31737 | -46.85338 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89af8173-98e2-3055-befc-42ab0294e9c5 | -12.58424 | -48.20105 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecfd82cd-3ef2-3fe5-a6b0-5e0cb3a312cd | -15.58943 | -48.33581 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a022040-58fc-315a-ad13-16340cacc6d7 | -15.32663 | -46.05274 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ecb8592-6cf8-3a75-b000-bb3c7d6f0c7d | -16.51194 | -55.03809 | 2025-09-01 04:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1251f1e5-ac99-342c-9d9b-0d40f6062ff7 | -15.6987 | -48.95981 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0d91bf34-8611-3b13-8bc6-32b58fea63cd | -14.04484 | -44.54969 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 435e52f2-3740-3629-94a3-60ef13f0c241 | -16.96879 | -49.30822 | 2025-09-01 04:12:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c3258b4-139b-3efc-9ed5-4cb1bf6ba39d | -12.60195 | -48.21237 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d13362d3-d982-31f8-a90f-87f29243a37b | -13.51796 | -46.99111 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2cab58b8-02e9-3c96-a0cc-22036a5e4045 | -15.31133 | -46.07901 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 345fa4b5-3052-38a6-9580-170aadd94f45 | -12.7789 | -48.08765 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a60c732-757f-397c-9f5f-6f8446fd2412 | -12.55978 | -48.21975 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 81a80f77-543f-3712-822e-e45cc4804025 | -12.57492 | -44.79576 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfffd57d-a10e-3dbc-a8db-1274c41bf958 | -15.72743 | -48.98062 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80eefefe-0a5e-3b75-8b45-8e248c6777e1 | -13.69866 | -46.90527 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README47.md)
