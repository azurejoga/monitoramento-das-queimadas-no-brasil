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
| 9934f66a-87ca-390f-a362-2bbab6a6627e | -2.67455 | -57.52193 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7a4e41c-1571-3963-809c-9a0c057d88ee | -3.40384 | -59.25174 | 2026-09-13 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 81b23c2d-514f-331b-a3d1-f427c7f8b479 | -3.36871 | -50.75135 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbd4b25d-bbea-33ad-b27c-483831e5739d | -3.16171 | -58.64752 | 2026-09-13 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41e6d212-d38b-3d20-9fee-846510ec2f3f | -2.94836 | -50.40977 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61b17421-326d-39f1-b7d7-51ade2c35fa9 | -7.01446 | -44.62286 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1115c2d-ecc6-3505-b3d1-0dbfe90dfada | -4.9266 | -45.83238 | 2026-09-13 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4bfcc9fa-a0e6-3b6c-9875-81877c932752 | -2.94731 | -50.39458 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 934c6a93-fce0-3942-bc07-7d8e940d7941 | -5.1364 | -55.967 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 516c3886-b119-3891-9dcc-3cbf22169656 | -5.81042 | -53.81081 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f42535f-8424-3eee-9001-512434dc49b3 | -1.46565 | -52.96439 | 2026-09-13 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 59cd14df-a223-3429-866f-96956bf3b0e7 | -2.94672 | -50.39825 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4b72d68-8389-317d-ab5e-9d77f776d0fa | -5.96417 | -47.20745 | 2026-09-13 04:49:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41f93ec2-ac48-3837-8d58-90dbecc56c41 | -2.89609 | -40.46139 | 2026-09-13 04:49:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 71a19715-e545-3602-be56-78f1d715ef41 | -7.02098 | -44.63468 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc572461-0173-38cc-890f-c1c74d69d70a | -4.6028 | -46.31586 | 2026-09-13 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54bc8b4b-2f3e-3a58-9126-076fa1837a59 | -3.0455 | -51.25709 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e350debf-7116-3d3e-8028-73479aa0c61f | -2.94718 | -50.41709 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea384d96-8acb-332d-a578-7fc3f64e540a | -7.38043 | -45.35916 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88167a41-ed6f-3d3c-bb36-bd96af7b92fe | -2.11937 | -47.11662 | 2026-09-13 04:49:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0b3ad07-8148-355f-8f23-05785e5b189f | -2.90114 | -40.46219 | 2026-09-13 04:49:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 075a5ac6-58fe-3461-af40-1797a80fd1a1 | -2.82271 | -51.34017 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fece59f6-0dc9-33f3-9628-4ba50c878851 | -2.82865 | -49.23769 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80f17b6-106d-3305-a470-c6be5d1dd065 | -6.1435 | -43.64425 | 2026-09-13 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 021829f7-3b55-378c-88b2-afb4d8d86552 | -5.12577 | -55.97459 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cb207f2-6019-38f5-acea-42bc9b083077 | -7.28741 | -46.23967 | 2026-09-13 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de5a8eea-95a7-3d0c-a05a-53c54e49756a | -6.79297 | -48.66196 | 2026-09-13 04:49:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d758bcb5-41e5-3d62-884b-17dced511585 | -3.39162 | -50.76265 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa58de24-ebc5-386c-8518-42b40630bce9 | -2.62771 | -51.75946 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 430f436e-707b-3747-af46-35c545947e41 | -4.92593 | -45.8367 | 2026-09-13 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d903f06c-3e00-30da-84b8-d9a035889b27 | -3.93589 | -51.04305 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df81b89c-a4a6-3e63-acfa-0928ab3836e4 | -3.33392 | -42.29279 | 2026-09-13 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2795644c-4c9b-3340-99e9-fd404fe7f3f5 | -3.64147 | -58.63181 | 2026-09-13 04:49:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25242cf7-2e75-3d04-979f-842152bb600b | -6.24016 | -51.69812 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0ed3bdc-9be4-3186-8d69-55ca3e2b3a09 | -6.16152 | -47.71503 | 2026-09-13 04:49:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28fe94df-a497-3d40-b828-6fc8ee843fd4 | -2.6724 | -57.53477 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6f77c00-7c63-325f-8e1d-e2dba296596e | -7.00997 | -42.11433 | 2026-09-13 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 05ba4d2d-47e7-339c-a82b-545ba692a24f | -5.88938 | -52.25803 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff5ec514-4f4b-34e1-b90c-42d11c0e6793 | 0.14711 | -51.46443 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1f9d3fd-4ba3-3d6a-b6ab-7fbaa1d90f90 | -5.27965 | -56.03529 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b212ee5e-299a-3cde-b894-8e75c2ec91b4 | -5.64426 | -45.91178 | 2026-09-13 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a4e4a16-a97f-3b4a-8bb7-0976bf39e3e1 | -3.87796 | -51.19385 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c1a086f-3a90-30bf-af6e-8061372e2150 | -5.96359 | -47.21124 | 2026-09-13 04:49:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4886fcc-f1b5-3612-acd9-1e29e654f731 | -3.82744 | -51.88736 | 2026-09-13 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9aca689-0141-3dc9-bc25-f19e0aaf77f8 | -6.07869 | -51.75873 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb7196d3-e0c8-3610-981f-280e34814ec2 | -1.46171 | -52.96374 | 2026-09-13 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f20203ba-2596-30b1-93a2-2a24364e6685 | -2.94212 | -50.40503 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d4a49ea-dd98-3c51-92d9-ad043f345453 | -7.37123 | -45.36761 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89cc1a6b-7cc9-34ee-b61a-9b582c924945 | -6.50481 | -47.59638 | 2026-09-13 04:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 927391ef-e784-3f2a-bd0f-57329e084abf | -5.93398 | -46.35178 | 2026-09-13 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e0ed4d2-debd-3d05-bbbf-5fb9d4def710 | -4.5108 | -55.45766 | 2026-09-13 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963d0fc9-6926-3fdb-9801-8b447f5f48f0 | -3.87509 | -51.18943 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1ba84c2-151d-3163-ada1-1a0d18a96b0c | -2.95814 | -50.39256 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dc70482-0840-3c77-94c2-13144ccd90b6 | -1.71979 | -54.95729 | 2026-09-13 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 792c6d9d-e34c-3fc7-a418-761839d830bd | -4.13662 | -56.32883 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8ee47a-ae9f-336e-999e-a3376dfa82a4 | -5.57933 | -46.80423 | 2026-09-13 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72562bb3-a438-354b-8f1f-924f94150a11 | -7.01746 | -44.63052 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5a98fdcd-630e-3158-8ebe-4743009f8cb5 | -0.90551 | -48.07421 | 2026-09-13 04:49:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc6aa799-f1be-3935-b5e2-9413283cb4bb | -6.23036 | -51.69257 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b03df6bd-b0e9-3c07-9cdc-87072a54bfb6 | -1.87597 | -47.90799 | 2026-09-13 04:49:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ea35d6b-c06d-3225-9f2d-9e3510bc0fd4 | -5.81984 | -53.80233 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78cced30-c1aa-3ea0-a4b7-e1e0c0f98f25 | 1.06116 | -50.96523 | 2026-09-13 04:49:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cb7c7f9-8cfd-3e12-bf27-03fb45b3bbab | -7.19876 | -45.92484 | 2026-09-13 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdf1dd3c-8462-3389-8ed0-a168fcf3912f | -5.77488 | -47.17147 | 2026-09-13 04:49:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc22fe93-f452-37c2-82e9-bd8c5e7c79aa | -6.79192 | -48.65849 | 2026-09-13 04:49:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8da9368b-5a1e-309e-9909-731a20647026 | -3.60053 | -59.07125 | 2026-09-13 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fa5095a-9ee0-34c6-b8e4-3bf4567f3662 | -5.80734 | -53.80522 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d94496bb-485b-3da1-9365-a4327c30f2d6 | -4.45876 | -50.15971 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b493594-dac1-399f-aafc-c6b25113a9f4 | -3.22396 | -50.58877 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 985788d3-c0ec-3fd6-9b47-e4c4024be12c | -1.22453 | -54.12789 | 2026-09-13 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5fff701-e22e-33e1-8244-ec923db4a055 | -6.22973 | -51.69639 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a05c10a-c215-3932-b5ce-30427d069101 | -5.80653 | -53.81013 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c86a6ca6-a3ac-3f4d-a094-057186470303 | -3.56801 | -53.0059 | 2026-09-13 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 938fdbb8-e12f-32bc-8a97-c718ca6605d4 | -5.54368 | -44.46151 | 2026-09-13 04:49:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e709e7c-e567-304a-8bb3-5e77196f22c2 | -6.23668 | -51.69755 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94a10dc1-4089-3aeb-a47d-a802d7794296 | -2.95355 | -50.39933 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b30584a1-f432-3f47-9b5c-3eb943428936 | -7.19571 | -45.91969 | 2026-09-13 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8981b12-afc3-3adb-93ab-6d99e9269c74 | -5.81513 | -53.80659 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 304872e3-4684-335a-93a6-1d4835bea4ae | -3.64776 | -49.51262 | 2026-09-13 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5af47c2-d1ae-35a4-b860-fecf3fafa17f | -7.20821 | -46.0962 | 2026-09-13 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 441c51f1-af08-3699-b4f5-b242bdceafa9 | -4.13554 | -56.33164 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ec4f91f-b614-3ce4-b119-85ea49868027 | -3.16734 | -58.6485 | 2026-09-13 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 889416c1-f7ce-37c0-bd15-b9d3bcf0c9bc | -3.33746 | -53.26777 | 2026-09-13 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 541163f8-f424-302f-be3d-d13324e13539 | -7.37051 | -45.37244 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7be6aeeb-c272-3afd-8c02-9bc568e7e779 | -7.01902 | -44.61991 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfa4b227-8120-31d7-9ee3-4a6d8e3882e1 | -2.93759 | -50.38964 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a47fbb96-a24f-33f6-ade0-a69354970563 | -1.73164 | -55.84714 | 2026-09-13 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f2ecb49-0203-3214-93b2-3d03c4f9b63b | -5.0236 | -49.99253 | 2026-09-13 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 16eedf72-f9bb-3942-a94d-3172f0208f1d | -3.82198 | -48.99365 | 2026-09-13 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5d7f982-f15d-316d-ae3b-ee6198cf6e71 | -6.69347 | -45.90734 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac0b7d7a-3066-3e58-83d5-b2d4151923d3 | -2.6142 | -54.75788 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7d10628-5dc9-3522-bd5b-8dec498b5228 | -7.09198 | -43.943 | 2026-09-13 04:49:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c59e6b6-991d-3646-b532-5c8c943f1e48 | -2.90157 | -40.45929 | 2026-09-13 04:49:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bba22607-8ffb-3433-b54f-b67f3a3b2b8e | -6.22466 | -51.68378 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55400916-0ad5-3687-bde7-6a4d81162253 | -2.68186 | -57.54301 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 01bf6c69-4b4b-35a4-8f86-c1bc0aec7241 | -7.2025 | -45.92541 | 2026-09-13 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3664f1c2-eddb-3a03-99c7-bc75d0830dd2 | -3.40967 | -59.24699 | 2026-09-13 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bf92c6e8-db38-3e6e-aa5c-1ba907156dc7 | -3.72944 | -61.7588 | 2026-09-13 04:49:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8935906-47b1-365a-ab75-100b71e53f55 | -3.38593 | -50.75407 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5af65416-514c-3f84-8864-d1eccacc8bd6 | -3.33325 | -42.29715 | 2026-09-13 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README33.md)
