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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 002f4a38-0b85-3800-acc3-1cfa7c367fce | -19.63321 | -41.8467 | 2025-11-21 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 34d75c56-9a55-3055-82f9-74168c92425c | -17.39829 | -44.47332 | 2025-11-21 03:55:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9013fbf5-2d75-3361-af45-646997886dae | -17.58261 | -46.67352 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd82d191-eace-3e9c-99c3-26552a0fcfe3 | -19.85188 | -46.31017 | 2025-11-21 03:55:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 083b7139-b2bd-3b75-9014-b08437e472c7 | -21.2462 | -44.0821 | 2025-11-21 03:55:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 830a0a0c-244d-33fb-9516-c1c4fc2a741b | -16.51744 | -43.54531 | 2025-11-21 03:55:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef39b674-7c5f-3051-9b40-aca6afa39917 | -17.58521 | -46.68441 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99d7db3e-cd10-3b14-b437-6a304733cf74 | -20.7657 | -43.21227 | 2025-11-21 03:55:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a5fb3e2-5576-32ac-81c8-aa189713cca3 | -18.11112 | -54.52105 | 2025-11-21 03:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f231361a-ed77-3064-be6e-847a53112ff6 | -17.8132 | -44.31213 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4481df0e-f73b-373b-8212-8d3b6844ebcd | -17.8369 | -46.99868 | 2025-11-21 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cbfd11b-3e9c-3cdd-87d8-d451f3be12ea | -26.48738 | -52.60736 | 2025-11-21 03:57:00 | NPP-375D | SÃO DOMINGOS | SANTA CATARINA | Brasil | 4216107 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2cc5e4e9-6977-30e4-8bb3-f2750be763dd | -22.92546 | -48.68248 | 2025-11-21 03:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4d3a214-b58c-387d-8494-fc7c3e646d70 | -23.42038 | -45.68518 | 2025-11-21 03:57:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c89dc46e-e722-3d27-9ebe-82a0e80fdb52 | -27.17546 | -51.24842 | 2025-11-21 03:57:00 | NPP-375D | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0e6e20ec-ab28-3e8f-8eab-72a307e0f972 | -27.17344 | -51.24814 | 2025-11-21 03:57:00 | NPP-375D | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9d86c45e-0581-39fc-b15e-4eca6d0083b9 | -27.17044 | -51.24708 | 2025-11-21 03:57:00 | NPP-375D | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 475a501c-5324-35ea-9a13-71a441967417 | -22.92192 | -48.67581 | 2025-11-21 03:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e71b4d2b-acbe-3223-9960-2f3e2767d8d4 | -22.92081 | -48.68115 | 2025-11-21 03:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 10770e1f-c5f1-3483-b942-53d12909ee56 | -23.42042 | -45.6894 | 2025-11-21 03:57:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b9b6da0b-a8bd-38c9-bb16-d5d4c48bd600 | -23.41649 | -45.68873 | 2025-11-21 03:57:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c1db9004-eb0d-3780-a8d5-0ef48dbe7e69 | -25.14288 | -49.6954 | 2025-11-21 03:57:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d161600d-cf6a-3421-a1e6-18bf1aeeda7c | -25.66173 | -49.36629 | 2025-11-21 03:57:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a523fc34-085f-3236-9aaa-eb3a77052771 | -27.17419 | -51.24493 | 2025-11-21 03:57:00 | NPP-375D | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 737825e9-a537-3f9d-aed0-747e1230335b | -26.49279 | -52.60926 | 2025-11-21 03:57:00 | NPP-375D | SÃO DOMINGOS | SANTA CATARINA | Brasil | 4216107 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f0e9fe06-66f1-33f5-ab61-ff713837d265 | -2.26547 | -45.58187 | 2025-11-21 04:12:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628a0334-6b43-3c67-85f4-88a245403804 | -3.47666 | -45.8771 | 2025-11-21 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9495dc8d-8b85-3776-85fb-872bf16283fb | -3.14178 | -40.18365 | 2025-11-21 04:12:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f60dc777-b5ba-3b98-aa4e-81f2241b3616 | -3.58519 | -40.95707 | 2025-11-21 04:12:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 10fc9a18-6d8c-3a4b-acc5-f1628eb95a28 | -3.43578 | -44.3675 | 2025-11-21 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9196bce7-aad2-3933-a11a-23741b7f7df3 | -2.1165 | -45.87988 | 2025-11-21 04:12:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9643ea10-99c6-3963-a724-96e6e841f224 | -2.5948 | -47.0011 | 2025-11-21 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65414c12-00d7-391a-ad6e-df9b4896b02d | -3.77626 | -43.94471 | 2025-11-21 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e41ea178-9f9b-3bc6-856f-6a4404ce9389 | -2.82821 | -45.41632 | 2025-11-21 04:12:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 448728c5-8a4d-3f58-9577-190d139b22ff | -2.83064 | -40.35942 | 2025-11-21 04:12:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| da33e95a-eee2-3ab4-ad59-d635c70e8831 | -1.16733 | -46.1388 | 2025-11-21 04:12:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c28c43cf-7bf0-37fc-9d3a-b5a60bb4b7bd | -3.34789 | -45.00251 | 2025-11-21 04:12:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 495e3855-2a18-3460-abdd-c7a231d30454 | -3.34509 | -45.67078 | 2025-11-21 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 179b9fe0-9a2d-3435-9300-123bcfc083e8 | -1.9017 | -45.60724 | 2025-11-21 04:12:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 321d3ff9-6150-3538-9625-2c64533b88be | -3.45868 | -43.41595 | 2025-11-21 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb599bbd-d9a5-3569-9a85-aa0bf998efd8 | -4.35185 | -38.89489 | 2025-11-21 04:12:00 | NOAA-20 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2a98498-97d0-392b-956b-3e1c64c3c929 | -3.25979 | -45.75769 | 2025-11-21 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12162734-0cd5-3386-994d-55b4ed5e3a9b | -2.33922 | -45.63615 | 2025-11-21 04:12:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a35e016-2580-306b-9120-261f022e72b2 | -2.90197 | -45.3692 | 2025-11-21 04:12:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6302baf3-9f4d-3e1d-9b03-2e5a1dd81aa0 | -3.42195 | -43.19947 | 2025-11-21 04:12:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 311463ef-1399-3838-a1c5-3620930e96ef | 3.63161 | -51.2917 | 2025-11-21 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 953d9adc-02f6-3824-9223-bacfd4880cc6 | -1.16497 | -46.13573 | 2025-11-21 04:12:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cbea9bb-78a8-32f2-9cba-a503b329bc75 | -2.99991 | -44.39521 | 2025-11-21 04:12:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cd0ad4e-319b-329f-a5de-d71f40094d7f | -2.97731 | -44.58014 | 2025-11-21 04:12:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f47157e7-cbfc-3ba2-8790-17ff7afd28fd | -3.8941 | -40.68586 | 2025-11-21 04:12:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 665ea864-374d-36c1-9170-a1bc79abe86e | -2.96045 | -44.59687 | 2025-11-21 04:12:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe3b5143-ecff-3e4c-b396-a8b9aa6300e2 | -2.97386 | -44.57959 | 2025-11-21 04:12:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20698e7b-eb39-3256-9342-b9b70112e79a | -3.45297 | -40.52584 | 2025-11-21 04:12:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 279e3104-2a12-3802-b46a-fcb5d662267d | -3.68524 | -43.96317 | 2025-11-21 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b021107b-682f-3974-95b7-2b579ac1d333 | -2.89008 | -41.6827 | 2025-11-21 04:12:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 556eb582-1904-37ee-84bb-59bf169c4952 | -2.99931 | -44.39894 | 2025-11-21 04:12:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4245897a-5c39-3ab6-9db5-cadd4f99e975 | -2.50668 | -45.98888 | 2025-11-21 04:12:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1703c3e0-f4c1-39f5-9aa8-ea20d9e9ff9b | -4.00031 | -42.48594 | 2025-11-21 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3dad160c-1660-3add-b48e-ad00f7ed42c1 | -4.24141 | -39.74646 | 2025-11-21 04:12:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fda077f9-ed05-38a5-a146-8e07601923a3 | -2.75006 | -44.95634 | 2025-11-21 04:12:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e009c55-ea05-3add-80f1-4e33200ba7ac | -3.99976 | -42.48937 | 2025-11-21 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 051f9c92-2df0-3d39-9b91-dc877e170558 | -1.92742 | -47.07856 | 2025-11-21 04:12:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45f825c7-7b98-33f6-8767-4d54fec534f6 | -3.99439 | -41.05332 | 2025-11-21 04:12:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22b24640-9990-3938-b26d-fa8bbf788df9 | -3.14582 | -40.18042 | 2025-11-21 04:12:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 777ecc5e-7f0e-330f-862e-f418753743e3 | 3.63099 | -51.28759 | 2025-11-21 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f251b544-97d8-33b4-b191-2c37c498ca55 | -3.13364 | -41.88337 | 2025-11-21 04:12:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97c299c0-5d2a-301c-97be-0eff578905c8 | -2.35033 | -44.80403 | 2025-11-21 04:12:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e104e08-ed7b-36e4-8b31-214ec0113230 | -3.48776 | -42.09491 | 2025-11-21 04:12:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 635fdd38-2abc-35df-90b1-cf4f65aeafde | -2.50595 | -45.99332 | 2025-11-21 04:12:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4dc6a711-b7ab-3a41-9a6b-928cab969b89 | -2.89285 | -41.68668 | 2025-11-21 04:12:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 78dfcdf6-52ba-36f3-b619-36419e61a325 | -3.46201 | -43.41648 | 2025-11-21 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d317c469-dc04-396d-bdc7-e643269c0a75 | -3.14237 | -40.17987 | 2025-11-21 04:12:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edaeb010-1f9f-34b7-90a3-d86039ff1e08 | -3.14524 | -40.18419 | 2025-11-21 04:12:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c8fd914-f7b9-3443-9833-4145954164df | -3.14111 | -45.34623 | 2025-11-21 04:12:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f86cd61f-0037-3ee7-88ca-37eb28e233f5 | -4.24422 | -39.74579 | 2025-11-21 04:12:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 40807811-cb20-314f-bf65-4a54127ec664 | -3.46256 | -43.41298 | 2025-11-21 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f13489af-6170-3b41-bba2-c4c3e397dda4 | -1.90179 | -45.60931 | 2025-11-21 04:12:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dcd9b11-bc23-3b14-9d45-668b32bee7a2 | -1.901 | -45.61155 | 2025-11-21 04:12:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3669c1d8-9132-3c7c-a2ca-287e22f734b6 | -1.93087 | -47.08269 | 2025-11-21 04:12:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b198c111-fc01-3fae-be4a-bd2641a3eaee | -1.16809 | -46.13411 | 2025-11-21 04:12:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c8ed77c-3f81-397b-99ad-803f68308ea3 | -3.37198 | -44.06512 | 2025-11-21 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29fd5f3c-329b-3e4a-b6b5-064e842dda45 | -2.96117 | -41.55509 | 2025-11-21 04:12:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 684678e6-ce46-3c58-916b-0bc004ecbb18 | -4.62572 | -37.94439 | 2025-11-21 04:12:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c1bdbfa-32e2-3253-87fc-ed2e0aba93cd | -2.55202 | -45.80308 | 2025-11-21 04:12:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76677b1a-a43e-393d-8c74-43a30e68c449 | -3.34577 | -45.6666 | 2025-11-21 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06fa1c44-7412-3da3-8480-44ad1e20754f | -2.11279 | -45.87928 | 2025-11-21 04:12:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acf5b35e-9352-3027-9eef-b7ecd3832a3e | -3.20528 | -39.58806 | 2025-11-21 04:12:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8059e8df-6be7-3284-90b1-5becddf27a4c | -3.99776 | -41.05384 | 2025-11-21 04:12:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a3480ce2-3880-36c3-97c0-01ad9963fe8d | -2.89839 | -45.36863 | 2025-11-21 04:12:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56365fa8-bcbe-3a1e-9c2b-24f7edc0391d | -3.46388 | -40.52337 | 2025-11-21 04:12:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ab98452-d5f7-3548-8792-c683f2356427 | -4.00361 | -42.48645 | 2025-11-21 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6d9021b0-b3f3-37d5-a107-fea0ed3a996d | -4.00415 | -42.48302 | 2025-11-21 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6d5286af-f6ab-3e25-af51-5a5750202a9f | -2.95785 | -41.55457 | 2025-11-21 04:12:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86703d62-c930-3dbc-9c85-1a40f85f3e39 | -2.89774 | -45.37272 | 2025-11-21 04:12:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19fe28ad-2b5d-30c4-b48f-20b5b1e1a9bb | -3.96744 | -38.55202 | 2025-11-21 04:12:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a71f6c97-f752-3ee2-8e0e-5e5b74cbe5fe | -2.84198 | -40.10796 | 2025-11-21 04:12:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3aa24466-b6db-3775-b00a-5130abdf5cf1 | -3.46145 | -43.41997 | 2025-11-21 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 931b64af-e0c2-352e-8e02-e6b0e8ed387d | -3.14014 | -45.34485 | 2025-11-21 04:12:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83f93dfe-a5d6-35d8-b1f4-a302fc5c0cbd | -2.89339 | -41.68321 | 2025-11-21 04:12:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f272796c-b445-3c0f-b5ef-dfb0cd70608f | -3.48031 | -45.87769 | 2025-11-21 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
