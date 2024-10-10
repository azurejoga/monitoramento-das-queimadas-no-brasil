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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52562b89-7fb2-3459-9586-7acaff87759f | -4.54706 | -55.51969 | 2024-10-10 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a448d242-015d-3e10-a687-a0b2792ee7b3 | -4.15367 | -55.55074 | 2024-10-10 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f11538b-5d4a-3f44-9e28-7880604a61a0 | -4.06574 | -56.23169 | 2024-10-10 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d389fee-cb0a-3359-af4f-1db4ad2c3c7b | -4.0615 | -56.23104 | 2024-10-10 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7a12a4b-d4c2-3743-87d4-a9eaafdec459 | -6.54935 | -55.9793 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c68237b0-d48e-3345-8c2f-5e924121ce57 | -6.47641 | -56.02081 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a539b358-3921-3c02-9174-5e4b1bff2072 | -6.47583 | -56.02426 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8bb6542-f825-3824-927b-5b2e054e0e26 | -6.47534 | -56.02081 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6582f3f-bcc9-3dc6-9b21-a238ef9d1712 | -6.47478 | -56.02427 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7c473da-5da1-396e-aec0-d6765768440a | -6.47184 | -56.02343 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab4663a7-d8ac-3c79-b712-4b7aaaecc7f6 | -6.47125 | -56.02689 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc5b32d2-9209-3576-8dd1-d86dcd5ef7bf | -6.47078 | -56.02346 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c19ce9c4-d891-3e25-8aa7-d96bd93f8040 | -6.47021 | -56.02694 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da6907e0-5a0b-3381-b1d0-ddb4a29015df | -5.29939 | -55.992 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7c3fa6d-4c6b-34c6-8123-1603c748140b | -5.29878 | -55.99562 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ac563a-9e5a-34a2-afac-8392a7dfecd9 | -5.27108 | -56.09268 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bf48a01-4a3c-3aec-bbae-451bd0f4dccd | -5.24925 | -55.96834 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 111969f6-522f-35de-92de-ff0e19241277 | -5.24875 | -55.94587 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bf50946-f1cb-394c-9f5f-c5540b3793e0 | -5.20094 | -56.03166 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be5aefb-d6c5-34c0-98df-ef18e0abb6e0 | -5.20032 | -56.03536 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64b5384b-7e6d-37e5-838f-45ec29bbd5b5 | -5.19746 | -56.02724 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2241a199-2f3d-3779-a99c-b56816031ca5 | -5.19684 | -56.03094 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e93394dc-f420-32cc-9449-7497def6ee22 | -5.19622 | -56.03466 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70b8ffa5-26ef-3a28-bafa-8450767e1abb | -5.12927 | -56.01345 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a13f8272-ef98-3720-b2b1-5c2900be4982 | -5.12866 | -56.01717 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10772f37-28d8-3158-b276-74b9e5bcead6 | -5.1258 | -56.00894 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18eb500c-4e38-3678-9137-305ab15c9d7f | -5.12517 | -56.01274 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1fdbd9c-f808-3c44-b7f5-81a38f6a4b76 | -5.12456 | -56.01646 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1510394f-232f-3a34-8de8-3625cf1d5a8e | -5.12171 | -56.00821 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e657813-df51-3d1a-b5fe-df37efa0f82d | -5.11025 | -56.23291 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8aa126e-9cd4-3ab8-8624-a6e0d192dc80 | -9.25203 | -57.77962 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e49a3f92-d577-31ae-be85-27bcaad32be5 | -9.99521 | -57.68081 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae150484-bb36-3aaa-8016-9aa3a79461bc | -9.9949 | -57.68015 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2e15c30-6368-3c2d-b108-fa890448f7bf | -9.99097 | -57.6801 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b8252b0-28ce-39e9-b35e-c7a2078d8b27 | -9.99066 | -57.67944 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b01a7f90-ad94-3796-b02a-af69393ae431 | -9.94795 | -58.11836 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 634243a1-83db-382a-9d65-9d63bdacbbb1 | -9.94719 | -58.12265 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21aab91b-e9b0-3391-80f3-cc4911d8f55b | -9.94644 | -58.1269 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1948a0e1-2863-3ae1-86fe-f03f610e1e92 | -9.91748 | -57.47956 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 14ffcdfd-506b-31bc-8f61-628182927c07 | -9.9168 | -57.48342 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae9c1533-161e-3e95-938f-ec04a07545ef | -9.91661 | -57.48035 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ff6cec2f-c81d-3349-95ee-c3d96177d400 | -9.91595 | -57.48423 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6dadef81-48a3-32af-af20-12c6fd6810bc | -9.91587 | -58.12151 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 465ce79e-29de-3860-9807-36861c313f90 | -9.91586 | -58.11826 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 258a89b9-ba51-35d3-8f30-284d19027165 | -9.91512 | -58.12253 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a764e41-a495-30db-9b90-78fadb5b1dbe | -9.91511 | -58.12577 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9372a4d-5bdd-392f-bd85-12b224ee108a | -9.91439 | -58.1268 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00970221-5159-3abf-ac30-9695af7ff68f | -9.91434 | -58.13005 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0705867-b42c-3ffa-bf47-52366875cee9 | -9.91365 | -58.1311 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d817c91d-e862-3803-bd8f-4c151f86dea8 | -9.91331 | -57.4788 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d3884b50-b1c0-365a-9422-e88f289bad5a | -9.91261 | -57.48269 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c9450b1a-39b3-3dd1-ac81-4c3dd8aa0889 | -9.91151 | -58.12073 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57408cfe-f24d-319b-bc0c-a57b2f78e86d | -9.91149 | -58.11747 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67d0ca94-b9f3-308b-a71e-fd77576bd33b | -9.91076 | -58.12174 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9544cbd2-99dd-33f8-99ce-2038db23740d | -9.91074 | -58.12499 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32b0a884-ff86-3f0c-941c-8f47d8188ac8 | -9.91002 | -58.12601 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c975e1c8-9c9c-3457-92fe-2f5dbc37572d | -9.90997 | -58.12925 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| addc8038-7faf-3fc9-af26-fabfb4946d0e | -9.90928 | -58.13028 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c515aa5c-b66a-33e8-856f-376c5d4e8df8 | -9.90715 | -58.1199 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6400a507-6d8b-3e08-80c9-9d784cb31910 | -9.9064 | -58.1209 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1172240-81b7-3321-aeb7-b1c2856457ed | -9.90639 | -58.12415 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11188712-25f9-32c9-ba98-2e454dfa6438 | -9.90566 | -58.12517 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57ae1905-a363-39ba-ac20-670867869200 | -9.90562 | -58.12841 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa58956e-8f42-34e2-9c14-848a6f43b9aa | -9.90493 | -58.12944 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9162fe30-eab5-3da6-b280-453882ab3992 | -9.90484 | -58.13272 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28aa60f4-f043-39ae-9d1a-a6f87edb59af | -9.90418 | -58.13377 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de14f8b9-fa2f-3f13-8900-c3797dc7bf45 | -9.90204 | -58.12006 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d78a498-0814-3d14-8e1c-77d5852eb8e6 | -9.90131 | -58.12432 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c74e9ca-6eb0-3726-82f8-ee497d9d050c | -9.90057 | -58.1286 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ac87da0-234c-3ca3-976c-d11cd474ad51 | -9.89769 | -58.11921 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f801ed4-9990-307c-996d-768aeca65260 | -9.89695 | -58.12347 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| baba0aab-b70b-39a3-a7db-46dcd186741e | -9.89621 | -58.12775 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f508fbe-22ed-3e0a-9aa1-2ed94c99bcc2 | -9.89546 | -58.13208 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a0eea84-36c5-3e7f-8793-c07132f33368 | -9.89259 | -58.12266 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1ca706e-08a4-391e-bb33-1b00a514df2d | -9.89184 | -58.12695 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b017bced-18fa-3625-b2ee-1bdaaa2d3d0e | -9.89109 | -58.13127 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 305ce0cd-99d4-35e4-911d-31db9ce36c6e | -9.79798 | -57.38791 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2430a035-206f-3508-88d8-a381eb596b9d | -9.72904 | -57.86523 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83940524-e7b0-3cf1-bee7-046eb3fb2945 | -9.68366 | -57.22345 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cc14e6d-2311-35ab-8f5c-ae8c1d10c134 | -9.67954 | -57.22266 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94c85897-5883-3498-a6f9-b27a2965e333 | -9.65943 | -56.95258 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eac076b-38fb-3493-a8e0-b28723097094 | -9.65537 | -56.95188 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b23f6e90-15c7-39bb-ae11-0467ec3f0aff | -9.65131 | -56.95118 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40e35e58-5f05-3c7b-8435-fdee91a0f3a1 | -9.65069 | -56.95482 | 2024-10-10 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1051f70e-34a4-37c1-9753-7a8ef03ba7cc | -10.57868 | -57.77109 | 2024-10-10 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afde55a4-651f-3e06-a19c-dd792b814bbb | -10.26052 | -57.95538 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb1d15c2-65e3-3b44-8950-609150486d26 | -10.2598 | -57.95958 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7a2e281-1189-3e1f-9b78-da26f2e493e6 | -10.25551 | -57.95874 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a22541ac-ac96-3377-9712-d00eaad0cc7b | -10.22431 | -57.8094 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0cd7133-81b5-38f5-84d1-abcac50a2eb6 | -10.22361 | -57.81339 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfa838b5-dbc9-31cc-8df9-618f81d7d749 | -10.19163 | -57.99427 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f1731d0-7c6d-389b-855e-f58fa3530737 | -10.08528 | -57.80679 | 2024-10-10 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9f9f94f-14be-3558-b660-569d4a7fb3ea | -3.14448 | -57.06272 | 2024-10-10 04:44:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890493a7-7da3-3f12-9252-f1a107468989 | -3.77563 | -57.00015 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e00d76fb-0669-3550-9dd9-75604b42495e | -6.47606 | -58.43609 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47afb0aa-13fb-3e5c-b494-0460c14ecc3f | -6.47133 | -58.43525 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04ff553a-e0f8-3b36-b40d-3f61869ec491 | -6.47046 | -58.44039 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f68831e-4041-3e57-8782-1450fae21f90 | -6.52832 | -58.4214 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a742798-0d6e-31b1-989c-682477de6756 | -6.52744 | -58.42643 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2295fd40-2406-3d5d-95fd-7650f6ce5467 | -6.52273 | -58.42559 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README114.md)
