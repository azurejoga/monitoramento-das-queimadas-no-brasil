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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f63607bd-6876-356f-abee-5c6525a5f7e2 | -18.12976 | -47.14093 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee29e218-fe79-3f1d-84b2-e0ee9215a95f | -16.28464 | -43.91363 | 2025-11-29 04:16:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d81e8695-b82e-35ad-a9b5-a1be1a4d68ab | -18.73544 | -47.69517 | 2025-11-29 04:16:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46290c41-adb7-32b6-8a3a-54cba4f08110 | -12.39192 | -43.67437 | 2025-11-29 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21f32c8b-8f9b-3be5-acf6-1ad93e3b597d | -18.17463 | -47.23722 | 2025-11-29 04:16:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d07ef840-8e17-3f8e-a299-1c042ff28326 | -11.80137 | -44.17303 | 2025-11-29 04:16:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3d19876-d346-3bfe-ad7c-ffc4b15a28e1 | -17.41506 | -49.23306 | 2025-11-29 04:16:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ea02e79-f7d8-3cbb-8f7e-c5a43c06d4bf | -22.08344 | -46.82124 | 2025-11-29 04:18:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30e6e286-831c-36c2-b0cd-ae2c0bea1156 | -20.4357 | -57.92504 | 2025-11-29 04:18:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 57bc77e8-88c5-337a-a670-a5aef18306ed | -22.95519 | -49.06343 | 2025-11-29 04:18:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf624516-d80c-3ed1-8c80-100321daf14e | -22.95246 | -49.05877 | 2025-11-29 04:18:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 604ae420-5d15-33b6-a32f-ec4ee9dacc21 | -21.47469 | -50.36852 | 2025-11-29 04:18:00 | NOAA-21 | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 645b9ed4-1e93-3bdb-bb0b-0791fa7d6033 | -22.9545 | -49.06747 | 2025-11-29 04:18:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42488a4f-da25-3060-8596-348ed568c121 | -23.602 | -48.3458 | 2025-11-29 04:18:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6eaf742-2f5a-3172-96c2-657e11d5b73b | -21.71727 | -49.46524 | 2025-11-29 04:18:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c37f8e31-8dda-3527-b29a-f625f38fd234 | -23.13851 | -50.14122 | 2025-11-29 04:18:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a3ff68aa-ae8b-328e-87c6-960f56ed56a8 | -20.44155 | -57.92651 | 2025-11-29 04:18:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cec3e261-eab2-3d49-a747-69f6b05ae36c | -21.75657 | -45.90077 | 2025-11-29 04:18:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1baa4181-4101-3298-9b64-6680f0d93158 | -22.88787 | -47.30587 | 2025-11-29 04:18:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dc468e08-55d8-3bec-a5e7-b8e8cb315eb0 | -20.40574 | -53.00338 | 2025-11-29 04:18:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3e5b7ca-75dc-37a2-a467-069780b1781e | -22.11346 | -46.93296 | 2025-11-29 04:18:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f48a810-9ddd-36e3-ad4e-3b0072209a82 | -23.13419 | -50.14485 | 2025-11-29 04:18:00 | NOAA-21 | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 54644ec2-4eb0-3adc-8d27-a40deb40eb28 | -23.57877 | -46.93325 | 2025-11-29 04:18:00 | NOAA-21 | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8f4782ad-952a-344d-92de-33d686ada203 | -22.76375 | -44.98579 | 2025-11-29 04:18:00 | NOAA-21 | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| eb946863-83ae-3eb8-87c0-40f8507c4739 | -22.08286 | -46.82495 | 2025-11-29 04:18:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b45014e4-ac93-3ff5-a77c-10c315b8889d | -21.6873 | -47.95477 | 2025-11-29 04:18:00 | NOAA-21 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa01fc7a-319a-3f4e-ba18-b4a4181a3244 | -22.96838 | -47.03225 | 2025-11-29 04:18:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 83d303df-fba1-3dda-8047-286e3f8f526a | -22.97545 | -46.23627 | 2025-11-29 04:18:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 707a31db-a5a6-316e-9622-1119801f749e | -22.97878 | -46.23685 | 2025-11-29 04:18:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2c06ef9a-6c9f-3a85-91ae-4a2c83a68cbc | -23.13496 | -50.14048 | 2025-11-29 04:18:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c83296c3-4294-3127-be39-f68f4bbe140a | -19.89576 | -57.447 | 2025-11-29 04:18:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7fbec958-4fe6-3c47-b941-16595c985303 | -23.48866 | -45.84677 | 2025-11-29 04:18:00 | NOAA-21 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ff47395c-69b3-301c-a988-a54852ee2e00 | -22.73149 | -49.34338 | 2025-11-29 04:18:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 876bf440-16d6-332f-96b3-3e73db807da1 | -21.47836 | -50.36923 | 2025-11-29 04:18:00 | NOAA-21 | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff3e4f64-70fc-3bcb-9636-9bab3dc6d770 | -21.12259 | -48.41506 | 2025-11-29 04:18:00 | NOAA-21 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1078f0e-5d3b-31ea-a7fb-eb6c1756b8cf | -22.22637 | -47.07916 | 2025-11-29 04:18:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ecdd3c9-315e-3ca5-b80e-005927725e0f | -22.44337 | -47.01875 | 2025-11-29 04:18:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76f44ad8-2e20-3198-b3d6-d6e7e2134aa9 | -21.69065 | -47.9554 | 2025-11-29 04:18:00 | NOAA-21 | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8574d6b9-859e-3ec1-94d8-0280b894ceb4 | -23.13774 | -50.14558 | 2025-11-29 04:18:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 66dfd97a-1303-344a-a7f4-51c1fc9c0e22 | -23.60413 | -48.34548 | 2025-11-29 04:18:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b77551ec-fc78-36ff-8525-ebe36c0fce22 | -22.73079 | -49.34751 | 2025-11-29 04:18:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a947d436-d48e-3fe6-aa0d-695aa364de92 | -21.69002 | -47.95922 | 2025-11-29 04:18:00 | NOAA-21 | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f7b9de8-b70e-3bc3-b84a-182deaf99cbe | -21.11919 | -48.41442 | 2025-11-29 04:18:00 | NOAA-21 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73f68439-552b-3f04-8df8-c88929acad3d | -22.38997 | -46.94828 | 2025-11-29 04:18:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 475ae078-bb94-3946-a515-b2e0039512b0 | -20.92679 | -46.80176 | 2025-11-29 04:18:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 485e6a4f-2958-38bd-97ac-ac4b128dd8f3 | -19.40998 | -47.69732 | 2025-11-29 04:18:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8347b86-ec88-307c-9814-ac1e04e1b193 | -20.1864 | -52.37767 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 78d16aaf-3502-3854-95c6-3d2d4f16f303 | -20.2155 | -47.54225 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885db4b1-000b-3eb4-90e5-77dcc99df6c1 | -20.41712 | -47.22066 | 2025-11-29 04:18:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 062d0e41-46c2-35e1-a1a2-7af117126346 | -20.1806 | -52.38511 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ce811e77-4e9b-3435-84cd-7f7a83e594e7 | -19.61859 | -45.53247 | 2025-11-29 04:18:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97eb457e-123d-3a01-a6f4-b00b65b9f253 | -20.4528 | -47.50782 | 2025-11-29 04:18:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68a480ab-f8d2-3efb-bce0-44928056969c | -20.98444 | -48.62921 | 2025-11-29 04:18:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3a411baf-92c7-30cc-a622-e456a2b00392 | -20.44946 | -47.50722 | 2025-11-29 04:18:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 892b0c4d-dfe3-3742-b853-06438deff7b6 | -20.98651 | -48.63787 | 2025-11-29 04:18:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 190a5d28-0ef9-39c3-a233-411cf89025ab | -17.48739 | -57.12556 | 2025-11-29 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a06d229d-ca58-3817-af2e-544b8a73e4d7 | -20.21796 | -47.5272 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4ead91d-558c-3145-992e-8b763676a043 | -19.90973 | -48.95904 | 2025-11-29 04:18:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| db233c87-5f04-36c0-ba4a-8159bbdc598d | -20.17802 | -52.37594 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 17ef2320-c12a-3df5-aa71-d86a5dac5fab | -20.75339 | -47.20469 | 2025-11-29 04:18:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 851fed04-7e78-377b-a680-047f841fe12e | -20.74947 | -47.20779 | 2025-11-29 04:18:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7668947-0e7e-30c1-91f0-23c4fcef7e42 | -20.72839 | -49.27239 | 2025-11-29 04:18:00 | NOAA-21 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 451d8789-5ae8-3c97-afd1-923feb46d60a | -19.7221 | -49.53149 | 2025-11-29 04:18:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1048c3ec-146a-3586-9419-2ad9a538ab4a | -20.18979 | -52.38271 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a61740b-a4a2-36da-8b35-22033453cb63 | -20.1856 | -52.38184 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 92049c65-273f-33a9-b853-12bd6bff4dff | -20.44885 | -47.51097 | 2025-11-29 04:18:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| db0076e9-35a9-30a7-ad70-96a3ff54d982 | -20.18479 | -52.38601 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 81b0ee33-b545-31ce-8af8-c4db4ae6a95e | -20.21216 | -47.54162 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35409cdf-7d20-3373-b7db-f0ebd1d5fed8 | -19.11363 | -46.97049 | 2025-11-29 04:18:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ae3612a-2493-3e04-936d-23faee2fee18 | -20.18221 | -52.37681 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 21c52108-cb29-3cc6-ae40-1bc92ad7cf57 | -18.79691 | -48.02076 | 2025-11-29 04:18:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce1261fe-9fab-3a66-8900-3c03211bb777 | -20.18721 | -52.37349 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c3dbc2ef-9e1c-3cc2-921c-4030e6f73f8e | -20.75279 | -47.20841 | 2025-11-29 04:18:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef2ca9a7-d5da-35e5-bdf0-4edbc402d10e | -19.93372 | -44.09061 | 2025-11-29 04:18:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8ee9ae5-a27b-3082-b880-faa8c0253a67 | -20.4455 | -47.51038 | 2025-11-29 04:18:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8db96230-6929-3fe5-9e3f-4ca72896959f | -21.37579 | -42.9414 | 2025-11-29 04:18:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bc5804e4-5f6b-39f8-84a1-755a86f2688d | -18.79625 | -48.02469 | 2025-11-29 04:18:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc3a8a14-d0ca-3bf3-adf7-3c4d141b550e | -17.4864 | -57.13009 | 2025-11-29 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e01eb283-8d25-381d-ae12-70b97bd2f042 | -20.21154 | -47.54539 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f09df08-fb89-3f11-9d9e-56f21529cba7 | -20.21489 | -47.54601 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9760e75e-b619-36ef-939d-c16ff91bc0ca | -17.49331 | -57.12693 | 2025-11-29 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0d7f2ea9-72b7-3421-a2a6-ff75ee170bec | -20.17722 | -52.38007 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db6fe4c7-257e-3a6e-b0fd-b838c571f2fa | -20.41771 | -47.21698 | 2025-11-29 04:18:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8ced508a-a83c-3d73-9e7a-93da67cfcd94 | -20.22069 | -47.53157 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 820f559b-58e4-3f68-9f49-6cf6611dd6d5 | -20.22131 | -47.52781 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b2b8a02-b884-3523-9849-796e56da0fcd | -20.96511 | -47.36927 | 2025-11-29 04:18:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 334cc5d0-4fdd-39dd-aed9-f2ebc4badfbd | -19.71471 | -48.78358 | 2025-11-29 04:18:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 638f2c12-5c29-391c-8d74-0c0b14137141 | -20.98719 | -48.63387 | 2025-11-29 04:18:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6dfa512b-14aa-3856-939c-8940e44dcbbd | -20.98376 | -48.63321 | 2025-11-29 04:18:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7d8262b0-d735-3b68-bcd5-b37ecc2b1415 | -20.41378 | -47.22009 | 2025-11-29 04:18:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 223b6373-fd06-33fa-8045-2985f267237f | -19.71367 | -48.78372 | 2025-11-29 04:18:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55cc5aa1-5725-3489-ae0e-ea40d8fa2a32 | -20.19059 | -52.37855 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b118f792-73c4-3c15-8488-f7fa1fb388f8 | -20.98101 | -48.62856 | 2025-11-29 04:18:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1c2a2ce0-3e12-3389-9431-0290a5697c9c | -20.1814 | -52.38097 | 2025-11-29 04:18:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fb322af8-0b49-345a-a2d3-2cd31d5a5c4a | -20.98169 | -48.6246 | 2025-11-29 04:18:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b525971c-8cdb-35b9-bcee-cc808f3efd7d | -20.75007 | -47.20407 | 2025-11-29 04:18:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e316a5b0-3173-3ba5-950e-7ef85ede5760 | -20.21735 | -47.53096 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7b6a484-7ce6-3b09-b0ca-d50250b89081 | -20.214 | -47.53034 | 2025-11-29 04:18:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8c1b498-da77-35dc-8228-7cac4418a5d0 | -20.41438 | -47.21641 | 2025-11-29 04:18:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa8dce5a-10e0-367d-ad40-b47d1cbb14b0 | -17.49231 | -57.13148 | 2025-11-29 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README19.md)
