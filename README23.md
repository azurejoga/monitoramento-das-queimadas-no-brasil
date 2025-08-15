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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5a909dd-c0eb-3d1f-942b-1c26b62d6a9c | -15.66595 | -56.38723 | 2025-08-15 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dd522a84-9812-3982-a963-1404d0ff4ef3 | -13.33967 | -43.37858 | 2025-08-15 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 139f21ef-d348-3643-889f-d4356380e326 | -15.89543 | -48.32853 | 2025-08-15 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e387aa0-ab02-3d4f-ba19-94a0adb3bb2f | -13.56921 | -46.9553 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc02bbd2-8f71-3ee7-9b83-ce69b50b2d45 | -11.3533 | -55.42569 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1cd5945e-50b4-3f54-9d00-c935626708e9 | -13.31627 | -45.23088 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 083742d4-0d34-3649-b65c-e82718a44ebf | -14.79644 | -42.72524 | 2025-08-15 04:04:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a66b20d7-8259-35b5-bb7a-b4ab0eb3e918 | -14.90649 | -45.18423 | 2025-08-15 04:04:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52e6ae3b-e320-37fe-b22d-5d08db3466b7 | -17.0609 | -51.79765 | 2025-08-15 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fad5b19a-4c9c-384d-ab09-9f27c99b2070 | -14.56774 | -52.04935 | 2025-08-15 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d95de1e2-946e-34a9-98e6-4c49332fda5b | -11.54175 | -47.25093 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4b7919b-533d-3aa0-addb-fa47967722c3 | -11.36162 | -55.43853 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2e2fddb1-d609-38ab-b785-e51c64622d4c | -19.55273 | -44.84051 | 2025-08-15 04:04:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2c77fd7-9bf5-3890-846c-8d9771a73f10 | -15.49327 | -44.4119 | 2025-08-15 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 53ab45e7-fecd-3961-bdaf-01cd3630e343 | -17.64837 | -44.49422 | 2025-08-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 145f395f-479d-3c8c-887b-11ff3c51bd8e | -12.59899 | -46.96659 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 26fb7a99-d51f-3cec-9406-0e77a7b1e9b9 | -11.36316 | -55.43129 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7c5dd99f-e51e-325b-8857-dd29a85e1864 | -18.0089 | -49.39615 | 2025-08-15 04:04:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3d09f7a-d4bc-332b-b81b-9ec80d0cdcf1 | -18.53216 | -45.45106 | 2025-08-15 04:04:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac37daa6-b4bb-32cc-a039-9e384cc8dc4d | -15.93041 | -48.16024 | 2025-08-15 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 7e1c774e-2923-39f6-8bea-d2d7389f10c3 | -14.24056 | -44.58596 | 2025-08-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 300a7807-3e4e-337c-ae68-82841c0c4da1 | -19.11842 | -44.47344 | 2025-08-15 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1740957c-e5c4-3733-b8e5-c5923ce32c33 | -11.32086 | -55.2057 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7891b24-9cb9-3d59-b8ec-6711fdb2fa8f | -11.35057 | -55.42089 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 674e2e89-b8c3-33f2-aa49-c8cbb63c9173 | -17.36198 | -44.14143 | 2025-08-15 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d87e0a3-092d-338a-9cc8-5f1731745c72 | -11.28771 | -49.11716 | 2025-08-15 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71ca774a-9baa-32e9-9de6-a07cdd3c80db | -11.28289 | -49.1162 | 2025-08-15 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a464bd4-d314-3079-b9a9-986f405b490a | -15.95733 | -48.09063 | 2025-08-15 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8365121d-6a2e-36b3-8803-e4d2dab90e27 | -13.14628 | -46.85931 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cb11426-20a5-36a1-99e0-01a470f16fbf | -12.5105 | -47.43529 | 2025-08-15 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da8613e3-ea1a-38b0-950d-0cb90888f248 | -18.69587 | -48.17845 | 2025-08-15 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9884cbff-c2c5-391c-986e-c774124b4d42 | -13.46831 | -43.75163 | 2025-08-15 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e9376df-7cd5-3910-9601-93ea819a8137 | -12.50721 | -47.01297 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba5bde0a-5418-3f8c-9847-418fe1d1469a | -12.58819 | -46.95612 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0eea420b-e971-3844-a088-0cc968d03ed6 | -13.32876 | -45.22403 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73603b98-9308-3cd6-8498-24402cd0b42d | -17.06156 | -51.79435 | 2025-08-15 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a80acc0b-bb5e-300c-ab80-9774cf569dd9 | -12.49695 | -47.0229 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cde8ce02-2872-384a-a101-9c9be218d3cb | -13.57546 | -46.96689 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6a6ce85-9555-3824-8e7e-938838621f99 | -13.31337 | -45.22585 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d2c59c19-d337-399f-940b-f6df3f15824b | -16.69024 | -49.37109 | 2025-08-15 04:04:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09b8f6e1-5257-327d-9efd-8d95f01d979e | -12.67211 | -44.95216 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21498627-18f1-3d6d-a568-16f4f17bfa45 | -12.49418 | -47.01455 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4306a85d-1393-3f12-ad8b-2909e7536149 | -13.15652 | -46.87189 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57082321-571c-3407-b037-9b81e870e6f8 | -13.58432 | -46.96389 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50d39614-519b-3093-969a-e90ab55fda54 | -17.49749 | -47.84298 | 2025-08-15 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9be6576-8ee0-38b6-b746-7bc61d9e5878 | -12.57789 | -46.9429 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d161aca8-83a3-3bb2-8971-3d349261917c | -12.58885 | -46.95244 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e2c13b9f-fdd3-38a5-b8bc-0a03bdc6c70a | -13.31779 | -45.2221 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ea70a2cc-6db8-3745-9e0f-f76764e769d2 | -12.58133 | -46.94724 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e21ebfb-edad-3b7d-b75e-0354533d8db1 | -11.35626 | -55.41137 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d607636c-5ffb-3b94-b355-41d0018b8408 | -13.31703 | -45.22649 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6cbe1eeb-dbb8-3478-9255-d9f9fd59f5cd | -19.47228 | -43.61369 | 2025-08-15 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff9aff08-578b-30c6-9658-fe6b80192500 | -15.39578 | -46.58835 | 2025-08-15 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3ceebab-0aae-3598-9946-15d87fb86545 | -11.35765 | -55.42239 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 675d2596-3456-3371-9437-201e0302b8c6 | -14.02093 | -52.04076 | 2025-08-15 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc9ab90e-e6d6-3465-a1cc-8821d5255b10 | -11.31382 | -55.20433 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8f020e0-dd2a-36db-b9b7-51739f367b98 | -15.14718 | -41.28222 | 2025-08-15 04:04:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0bfbe2cc-5689-3ec7-9e60-8be5d339231b | -14.05727 | -46.29801 | 2025-08-15 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a315c0f-e14c-336f-ac25-1fbd96a20fb2 | -12.59492 | -46.9657 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba6dbb7e-4198-3464-9cc4-da669e2c48d0 | -17.6464 | -44.50614 | 2025-08-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| facdb417-09c8-3d93-b206-7991f8ca129e | -15.3931 | -55.78228 | 2025-08-15 04:04:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e86c49e-b816-36de-bddd-1831d4e2761f | -15.63722 | -42.55015 | 2025-08-15 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7b25d06-2b0c-3ffa-95da-5478a170e7dd | -13.6125 | -46.92226 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08cc0f70-983a-3e3b-919c-b6f4dfa988b8 | -11.35065 | -55.40277 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b8b03e22-c1f8-3523-bb45-5948aea1dc84 | -12.42554 | -48.70011 | 2025-08-15 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc369f7e-624c-3637-b8f9-5e87db1a61c0 | -12.58951 | -46.94873 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| de5776ef-8694-30be-9c85-75f95557dd10 | -12.43015 | -48.70095 | 2025-08-15 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cf50d4f-91f9-3d80-bdec-e1be9547c771 | -12.77534 | -45.94517 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 413283d0-99c9-3053-a020-de6842fc8fe9 | -12.78816 | -45.96239 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f18f42b2-ae03-3a59-a2f0-93755bab92d4 | -12.35122 | -49.91034 | 2025-08-15 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9707369a-5b5a-3fae-a5c1-5d30f8f8a1bd | -15.40165 | -46.59981 | 2025-08-15 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18d81711-a3f7-3dcd-9ed9-8db58f0ad07c | -12.78898 | -45.95766 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d54e6d7-0414-32aa-937b-fef6246e9269 | -15.8965 | -50.17661 | 2025-08-15 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 75dfeaf3-b5e6-323c-a770-c5db33dc21c5 | -13.27933 | -50.83286 | 2025-08-15 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0df5e141-3a0b-3785-926b-3624b47d460a | -15.93182 | -48.15246 | 2025-08-15 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f24121f1-3c22-3c23-8e77-96f86dcb3e2f | -11.53818 | -47.25118 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17b21831-be75-30b0-a5f3-df6bdcda8a3a | -15.40254 | -46.59482 | 2025-08-15 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1516a72-7fe8-3121-9917-8caff7b686ae | -17.96573 | -41.71018 | 2025-08-15 04:04:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0237f731-0481-3ad8-a029-fb57a946a67f | -12.30851 | -44.3447 | 2025-08-15 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f407319-e558-3042-83b2-724dab43f366 | -13.32951 | -45.21964 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef87379b-9bb7-3cf1-96ac-4e4746ea7463 | -19.47891 | -43.61484 | 2025-08-15 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07e8b9c5-28f8-3f77-b2bc-891f1af519c9 | -14.02019 | -52.04439 | 2025-08-15 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a5b22f3-2e1c-3cee-81db-26c29e181451 | -17.49481 | -47.83498 | 2025-08-15 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa292a32-9d75-3258-aa38-f6d48e97ceb2 | -18.29776 | -49.5514 | 2025-08-15 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 20b01d51-8cb1-3113-b6a1-8beaf3f647c2 | -11.54528 | -47.2557 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a365b97d-a024-35bd-a963-7612a5109f8b | -14.7096 | -42.3073 | 2025-08-15 04:04:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e9e9d98d-c126-391f-8a79-710574c6c337 | -12.50107 | -47.02363 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f82a0ff-a8b9-3abd-b713-762d5a614299 | -18.69985 | -48.17931 | 2025-08-15 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 99906b83-2f15-30c6-8893-5d93a35effe9 | -16.07374 | -43.63208 | 2025-08-15 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2f71131-0ee2-3eab-a1d5-87018a77e801 | -15.89624 | -50.17849 | 2025-08-15 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aadacc43-c6b3-3be2-a059-4caa3b693d4a | -17.49416 | -47.83859 | 2025-08-15 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11f58145-975d-33c5-aad1-7edebe004a89 | -13.32434 | -45.22778 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eabae32c-7d51-359f-9b8d-32acd47fece0 | -11.77772 | -47.39397 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 960723ef-6e67-3be1-abbf-3d4b6ca45e7f | -15.66761 | -56.38005 | 2025-08-15 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08e9f602-e057-330c-9a7a-9051af2ff3e5 | -15.8918 | -50.17526 | 2025-08-15 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| dbfb952c-7af3-3ac2-baf8-1382f5c19173 | -19.37112 | -42.93778 | 2025-08-15 04:04:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 222a993e-ca3d-3e3b-a643-69f03664f5ab | -13.87258 | -43.49428 | 2025-08-15 04:04:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa9dfb6d-96be-3b8d-a9c6-65a4d2828ac7 | -11.31828 | -55.20588 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eda50736-766d-36fb-8ad4-e0ec4ceffc1f | -18.94682 | -48.181 | 2025-08-15 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8b35d86-fbab-3d56-82b3-abe76d5b5259 | -13.31551 | -45.23529 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README24.md)
