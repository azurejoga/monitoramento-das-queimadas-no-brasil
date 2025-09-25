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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a13b54dd-1b1d-3468-9dc4-d7026910f225 | -20.76312 | -56.92785 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d6f2024-06e3-3412-81e6-99a28894b76a | -20.99483 | -50.00864 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 19ef6bba-bab2-3bcb-ac51-2248319919d3 | -15.24791 | -59.44105 | 2025-09-25 05:04:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 154ec2a4-c041-34fb-9375-41c9bd0cebd8 | -20.80039 | -56.95354 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 831e8d7e-873e-3986-9722-e7416234937c | -15.82585 | -59.60382 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f905cc6b-b711-3bdc-ab2c-baba7f5b4421 | -15.90915 | -59.39837 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a72e2ccd-643b-3dc6-904e-5cc626944897 | -15.90628 | -59.39355 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cb7581e-25cd-372a-8992-7331a0b63d89 | -15.27654 | -59.43045 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15833a2e-3f52-336e-b5b2-a118ffbc5370 | -20.99205 | -50.47324 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 02a06773-ea7b-36d3-9ab2-8d080a6ca113 | -15.90559 | -59.39759 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba83c3d-65ad-390e-848e-5a5eb4eb5c93 | -19.59199 | -57.73594 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8c9b0fc9-d0f2-32c5-bb98-913813df19e2 | -15.75859 | -59.49561 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2b18db62-ba88-326a-854e-3f06c3272205 | -15.28372 | -59.43199 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb5ced6-26bf-3633-8635-3ca532d3fb85 | -21.01194 | -50.02647 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b066d053-33d4-3813-8a85-412c07f25d5b | -16.00721 | -59.48776 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e78314f3-5a71-3bae-80d9-8d403e8b7851 | -20.99956 | -50.00922 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a40dd341-7740-360c-8c11-306cebd563ec | -15.91407 | -59.34762 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18ace80c-120d-3f33-8055-0ebfd003e663 | -15.96987 | -59.50584 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b111476c-6ea2-37d9-80ec-549903d4a646 | -20.99072 | -50.00273 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 241944d2-5c1a-397c-a6c4-19af3db12d26 | -18.18246 | -53.33161 | 2025-09-25 05:04:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f155784-80d7-3140-80e1-d09ef6143b92 | -17.93114 | -55.86189 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 42a98e80-1d71-33a2-8124-7b3b2541e414 | -20.99252 | -50.0291 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 18b42800-b709-3730-bd1e-36af92d19063 | -17.93957 | -55.85187 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d62193aa-99d9-356d-a261-9e14cc7dfa99 | -15.91163 | -59.39386 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5065aec6-3066-3a63-996a-912a524b1e89 | -15.92118 | -59.34907 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7f2416e-60ca-3a94-bb7e-21e7e3f75c14 | -15.35368 | -59.19756 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c39dc833-fe67-3eeb-9b7d-eb09ee64450c | -20.46854 | -56.65666 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e60da91-e2ee-38a4-8bdd-ee0c94dba65c | -17.9592 | -55.85894 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| dc6be8bc-29c6-3ff2-90d0-68f65a5d8ef0 | -17.92722 | -55.86503 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2ccd56a9-dfb6-3a3b-af34-dc040dc9bd05 | -15.8849 | -59.34612 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 513f2f69-f4ca-3e95-9b38-a154be326d64 | -15.88131 | -59.34557 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30a3e6a1-0b0b-37cc-a55e-a7ac43143885 | -15.80991 | -59.48123 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90496d07-18a5-3439-93e6-e750aff20abb | -15.35653 | -59.18089 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25b76e40-c7d7-354e-a739-89b0869bcfa5 | -15.86632 | -59.34716 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2875912-2ca9-30af-bf5a-acec05f986fb | -15.88703 | -59.42003 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb45e9c-3594-3098-be2b-4868601915ba | -15.83381 | -59.60085 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d73f8576-dd85-347a-b778-3b5f1c39625c | -20.9882 | -50.47126 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 73c7a0a2-ac8e-32b7-8768-b9cd56ffdc89 | -20.9984 | -50.01934 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 21565545-1e1b-3d29-b932-4c67dbcc2758 | -21.83237 | -50.58197 | 2025-09-25 05:04:00 | NPP-375D | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1c16ef0d-0816-3cbd-8009-18341b7a276e | -15.77009 | -59.49345 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 90a144b3-28a3-3278-aeb7-8e1a85569053 | -15.82946 | -59.60448 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8ad9b14-ae84-3176-8ecf-1a889fd2e0f5 | -15.25619 | -59.44038 | 2025-09-25 05:04:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5388f6ae-adfd-334d-a606-76966cf31e46 | -20.99426 | -50.01372 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d108a4f0-aae3-34bd-a95c-eeb191e84953 | -17.94574 | -55.8567 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b19fca5d-0f64-3286-90f6-9cff52c525f3 | -15.76503 | -59.50138 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 756d31a5-55b4-3e1e-a3ab-2aa441dcca45 | -22.41145 | -49.14359 | 2025-09-25 05:04:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79816f70-7514-39a8-b0ef-accba0f15de4 | -15.87774 | -59.34495 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bf64867-2bc4-339d-8f15-834d10af9a93 | -15.25517 | -59.44214 | 2025-09-25 05:04:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5498c29f-74ba-36f2-86c7-9ead0769ac13 | -17.93508 | -55.85873 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| dd1fa5bc-a67f-3f2c-8811-16473bd54031 | -20.75885 | -56.92408 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 328a7fa9-3084-354c-856b-b2b8d54508b3 | -20.98369 | -50.02258 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e44069ec-0919-33d6-8be9-4ed0bd971a3b | -15.26423 | -59.43705 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed59ad28-410c-3da1-8196-09b6fcd09de8 | -15.90983 | -59.35088 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae712e51-24c3-3889-8039-229509590efc | -15.88847 | -59.34671 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03fbd74a-476a-334b-a01f-8674219ba8e3 | -17.94294 | -55.85243 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 50c66408-1833-355e-b148-8e09e412555d | -20.99151 | -50.47807 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2a9d019f-e374-3131-b29a-fde15c896f91 | -17.9362 | -55.85131 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f61ac713-9e86-318d-89b0-af6515198001 | -20.70766 | -56.74247 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11fe7885-7292-3623-a32d-f508e9b106b6 | -15.29165 | -59.42917 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f96a49cf-e277-37ab-9389-f00fa67d808f | -21.01664 | -50.02718 | 2025-09-25 05:04:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 208106f4-c937-303b-95b4-9e0d8da61b47 | -17.93338 | -55.86985 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 1557af0c-d192-35b0-a8d7-49a6c43d2469 | -15.93233 | -59.42334 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e38b262-00ee-333e-b300-a4c154cf60d6 | -20.97428 | -50.02122 | 2025-09-25 05:04:00 | NPP-375D | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 273240f3-2f75-340b-ad06-1c51af70fb53 | -22.36249 | -49.47992 | 2025-09-25 05:04:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ee2dbdd-4778-3b22-8e45-0550fbb81ad6 | -15.75572 | -59.49066 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7b589589-ca9d-308f-8f99-9f5e55e05ad6 | -15.27364 | -59.42573 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d1825aa-7a94-3179-bd01-13319e79c9b0 | -20.69583 | -57.86079 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3b8caebd-5152-39f9-9b75-ee43416dfa50 | -20.66474 | -48.82484 | 2025-09-25 05:04:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b342d084-f11a-3ae0-a889-ecef2ffefbdc | -17.93171 | -55.85817 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| ef9a8b52-dc27-3ff7-89d9-acdb7d898fd4 | -15.28014 | -59.43118 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38ad01b3-9502-3ede-8320-d8e66d3e1cb1 | -20.61445 | -56.71124 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4752a3ff-e7f9-327b-993b-c101470f97b9 | -15.77369 | -59.49408 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f7b94b6f-29ec-3c2e-9e60-ba2c6258d46f | -21.16149 | -49.72158 | 2025-09-25 05:04:00 | NPP-375D | UBARANA | SÃO PAULO | Brasil | 3555356 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5775e7f9-a6a6-393e-a081-25bef534ef96 | -20.9737 | -50.02644 | 2025-09-25 05:04:00 | NPP-375D | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| fdd11413-7caf-3f0f-88df-cdbfc31548d1 | -16.85278 | -50.52166 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c840c59-939c-3685-a02e-27cf9b585082 | -17.9536 | -55.8504 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b46a3a5b-c3b8-338c-b531-c23ba1c45222 | -17.02922 | -52.24076 | 2025-09-25 05:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 248ddf52-928b-382e-b302-1f96fdc9c494 | -18.18186 | -53.33598 | 2025-09-25 05:04:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 99789fd2-c12a-328c-a899-ddebf4b04ea8 | -16.84901 | -50.51685 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c70cb05-df66-35cb-9793-4f6252ad9df7 | -15.8963 | -59.34396 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 499d4ad3-4888-3632-9398-b6f236f9b53e | -15.76577 | -59.49704 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3f45ad1-18fc-30f6-baf4-b7e04b508118 | -20.98801 | -50.4678 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c6886c60-b48f-34c0-b26e-7d010b1e1d21 | -20.77879 | -56.91531 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0f63a13-b6fb-3024-a778-e91a28e5551c | -15.34939 | -59.17966 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2abb653-a16f-3fb9-a273-838c9cb7b972 | -20.66541 | -48.81843 | 2025-09-25 05:04:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| adf51fe1-7aaf-3289-ac95-bc09bba6d56b | -15.76155 | -59.47826 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 19dd095c-8936-39ba-ae6d-6cd1ed8fff5b | -20.76463 | -57.87269 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9ce8a81b-f63c-3dc8-8eda-be1b59085801 | -15.90984 | -59.39431 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cbad1d7-e794-3198-87ac-b5cd02928c54 | -15.25177 | -59.44431 | 2025-09-25 05:04:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb70228c-2232-3a3d-9a3e-db4200d0ba19 | -15.88915 | -59.4076 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5f35928f-4452-393f-b123-ee040bfd478f | -15.88557 | -59.40694 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d28ba114-df2b-3045-b999-95487810bc0e | -15.28807 | -59.42833 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96b4a17c-d051-3a39-a64d-834c7a001168 | -20.47247 | -56.65351 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5aa0575-6e68-37f1-984e-c5a3e9a5c17b | -17.95977 | -55.85523 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f9bc3c2d-fcd0-3894-924d-8ab0849dc56e | -15.36509 | -59.1738 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f40913b-617b-3d81-a415-287769035cce | -15.2606 | -59.43646 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95228a94-c971-3ed3-af88-79758a7127f8 | -16.85383 | -50.51336 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48b4f4d9-9a19-3a80-a5d3-d7bb83c432a0 | -15.8251 | -59.60812 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8a2a5a37-6278-3b24-a81a-b58dd53298b8 | -20.99369 | -50.01876 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d4351f23-bef5-35f6-a536-c305de2de15e | -15.79766 | -59.48772 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README33.md)
