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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bfc2940-ffc2-372d-b144-40b9c902b65e | -15.22043 | -49.29995 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb7e2466-9188-3a28-b188-d1e711809a77 | -14.77564 | -46.0656 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| e4733e80-651f-3ff6-a057-813f065209a3 | -11.94955 | -46.42747 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae75f17c-31ba-3943-a65c-4a22458cb90a | -13.26985 | -48.0588 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36533173-3e48-3693-bf6e-c63676c410f1 | -13.2204 | -47.81238 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d86b932e-9b2a-364e-9754-bd813419b234 | -10.15275 | -53.71581 | 2025-10-07 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b862883-2f2b-313f-9340-07f824f739a2 | -12.92401 | -54.72207 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4928bfd4-bfd9-386f-91e4-3eb74423cb3d | -14.61592 | -46.13602 | 2025-10-07 04:38:00 | NPP-375D | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1b58f8c-e7fa-38c8-9019-89e06d25eb9b | -10.45476 | -50.41059 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5476b058-10fc-3e74-8061-dda3477e62ac | -15.3468 | -47.32898 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb50390f-002e-3b74-8418-2707adc2d569 | -18.04819 | -43.15 | 2025-10-07 04:38:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c3283427-2884-3818-8d71-e87ac3a5ff22 | -10.39353 | -51.59757 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91eed3b0-2062-39f7-b4aa-697134cc46a3 | -15.21797 | -56.77063 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccc57b56-ab93-383c-bb16-c806bb87f4f6 | -15.1938 | -56.82349 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8980694b-dcb2-3d3e-a555-058af1ec50fc | -15.99598 | -50.9431 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7d9bd62-fefd-3de0-b502-2862c37525da | -16.00643 | -50.96357 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4eb6cc76-0f46-3e4f-95ac-8a8b5f8f7c99 | -13.72589 | -48.1979 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c1d4046-5e5c-358f-8367-f9c10775cd22 | -10.32377 | -51.45344 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e654a31-d665-349a-b174-b77fa190e091 | -13.38418 | -47.5354 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70e57b18-85af-3ad8-a4c0-6cf568f391b3 | -10.378 | -50.30014 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1bd488e-de8c-3a70-a275-2ae3f5940274 | -13.337 | -48.03186 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceb20d52-0c75-32dd-aace-02c4f11f0449 | -11.77509 | -45.13561 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6dfec9de-9328-343c-b922-c7057ccf5a3e | -10.38938 | -50.29781 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 132ad526-06c2-35ee-b68f-a66cdd7623c8 | -15.3917 | -48.00589 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d64a4e54-8d68-369e-9119-da8673c3e7be | -10.43491 | -50.33928 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2632b7b-d1f0-3035-b378-a335bf6cb356 | -13.50079 | -43.67496 | 2025-10-07 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| d639f4ce-5824-360a-b574-781e41d52dab | -12.25531 | -47.16745 | 2025-10-07 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c7a6fbc-87e2-3245-8a5f-18712e424e71 | -11.22467 | -47.77971 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f18ec5c0-3309-3030-a57e-d61f5247cd96 | -11.13216 | -47.22057 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd08e367-170e-3e4e-9b73-329ed07bb48f | -10.5811 | -51.47064 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bb7252be-8799-368e-98e3-b16a79aa01aa | -10.44796 | -50.40946 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa7e9f6b-11a3-31bb-8593-d1a30552d672 | -9.40105 | -61.44588 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23d69611-3a17-3940-9417-c28ddc9fd0ad | -13.25677 | -46.47537 | 2025-10-07 04:38:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f836035-9280-3a67-81b9-e0ecf34d332b | -14.66493 | -48.39672 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 342ee9e0-d67e-346d-b36e-888a1b64d940 | -12.21498 | -44.2556 | 2025-10-07 04:38:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41ab760a-5d28-3b6a-b299-4ccba276e1f2 | -10.42431 | -50.31868 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ec978e2f-5441-37ac-a59a-79b66d32069a | -17.09285 | -43.3815 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deb3130d-e3fb-35a9-a6c4-4d67b8bc1210 | -15.61972 | -52.54774 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97224227-c201-3837-8fa1-5f0a07210d96 | -16.05837 | -50.99103 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 712360de-b789-3a70-a2bc-6969e439ca4c | -14.311 | -45.84612 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a413dc9d-2839-3676-9e7f-9b1a21679c37 | -15.9356 | -49.00063 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34ad67db-20ac-33e8-8a09-df57e3340575 | -18.66859 | -44.04168 | 2025-10-07 04:38:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28aecc4a-ef4e-3e5f-adfb-26dc118c13b3 | -16.04461 | -50.96983 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60c8a95f-c0f7-3289-b343-c134c02ec29d | -14.75659 | -46.01138 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e291be1-2957-3683-8d31-05c0fb69b8ce | -14.6514 | -48.37164 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a98365d-8ed3-3a5d-b308-95b99d6a3205 | -12.61828 | -44.75258 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73418ea0-edc1-3b3c-9d0f-cec0da4d1cb1 | -10.38139 | -50.30402 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 183468e0-e20a-319c-8bea-a3963acc5273 | -14.92732 | -51.41271 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 720a59ab-4ccb-3435-8b49-c571ab3ccddd | -17.54786 | -46.76316 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e07baa07-b081-3126-b288-f7e7a144753d | -15.38911 | -48.01038 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e49caae8-5e5f-3732-b98b-2c326d5a8f95 | -13.34459 | -47.17761 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05c5c5c3-58f4-3b45-9e96-0f29aa620d57 | -13.68958 | -47.95596 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c3d983d-d210-3f59-b66d-a8f792e49929 | -13.33932 | -47.76202 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6066e20d-8b86-39a0-bb0b-0bf6e9284624 | -13.59258 | -48.68394 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce8893d0-3028-397f-83d1-f1acc2029485 | -15.59692 | -42.36242 | 2025-10-07 04:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c82d05f5-499b-30b7-9392-574d8a2cbaeb | -11.04746 | -50.92508 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9db4ed6-7ac9-3fa3-bf2a-9dd5e6a5e4db | -15.98709 | -50.93426 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dafac5a4-beb3-3442-902e-3157e67e5ef7 | -14.55114 | -46.644 | 2025-10-07 04:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daab961e-1f88-3aff-9285-6ebd743117bc | -14.66211 | -48.39244 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 730898dd-0164-32f2-a431-05a3238f6cc5 | -10.87901 | -56.06811 | 2025-10-07 04:38:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc24eb48-5bc6-33d3-beda-7cc97abe42dd | -17.74987 | -50.37706 | 2025-10-07 04:38:00 | NPP-375D | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb55c336-6e4b-37c6-9ee3-dac6552cb55b | -10.99362 | -49.58119 | 2025-10-07 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2331479-cad4-33f9-aed9-c20b92e6c14a | -13.24292 | -47.238 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efcec995-4093-33b3-8355-cd8a923f16ec | -12.37667 | -51.11286 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdf11a64-c04e-36cc-a4a0-a1be39549c33 | -15.99262 | -50.94258 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22d34c3f-31b4-3c60-a4ed-4deb80760663 | -11.94465 | -46.46005 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d7082b5-0abd-3825-8adc-84a013025ceb | -15.38003 | -46.27665 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14985927-2c8f-3ba1-95f0-ff2fd4f43965 | -15.26332 | -48.05705 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06d807e7-da88-3a66-a3c4-26a180c99e07 | -13.23624 | -47.24963 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09f5a280-3d23-3d26-8db9-5066737ff25d | -9.16841 | -59.55804 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2b02a38-c564-3b88-97c8-433d976ef722 | -12.97893 | -46.784 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3015114d-0274-3356-8ced-556bbdfa1f80 | -13.6597 | -48.72845 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 937a7ced-515f-312f-8afa-221d263ccf2f | -15.20421 | -56.81367 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f7e3e8f-76c0-3570-9f8d-5eb2c7fa2b0d | -13.3292 | -48.03416 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d38ff251-036c-33c9-8412-fb009ba06c71 | -16.19767 | -43.65973 | 2025-10-07 04:38:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44bdf24b-d5f7-3302-9c91-a27885cf1b95 | -10.33184 | -51.23211 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd29b2c2-92fd-3c98-981e-37fc10a1d05f | -10.4501 | -50.35313 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 81a37a34-6ea7-3c83-93e7-b9823741561d | -11.38261 | -54.34746 | 2025-10-07 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2db4ef0-df39-3ef9-a05f-75877e8f6c35 | -9.44828 | -56.65822 | 2025-10-07 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a88dd625-bd2a-3991-821a-3d7a02cfb1f0 | -13.25204 | -47.17599 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f775975-2854-3d8d-a6b3-08f9341fae9b | -12.90911 | -54.7345 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 558aaa13-efce-3fab-9b48-e06cffd71355 | -16.00858 | -50.82224 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a15e5726-ad57-3146-8aa1-0c4d198f5070 | -11.43889 | -43.47802 | 2025-10-07 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a29eeee-6635-385b-849b-1525d164148b | -10.40854 | -50.30853 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ca85e32c-500e-3023-8834-5a2b036afa03 | -13.23831 | -47.24505 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c6c1285-6666-34e7-a67b-4fe2968fcb21 | -12.38071 | -51.10967 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74fa7de0-961a-3e54-b1dc-f8097fd2098e | -14.92949 | -51.42078 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cc7689e-b9f1-3aef-9f35-d3b7090a6a77 | -11.1042 | -47.19693 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c69cc8d-a312-39e8-a404-c4c8cc3ef0a2 | -13.24502 | -48.06232 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1696a86e-9afc-32e9-8701-6f262b22c0af | -10.4361 | -50.33194 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d358e35c-0aec-37ef-8258-d793501a5ad0 | -11.15503 | -54.87698 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 929a5f47-dc5a-38d3-b653-5713b53b65e6 | -12.61394 | -44.7607 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 477ca22f-6ea2-3dc4-b5c4-6c857e49b223 | -13.73675 | -47.94412 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 928c503f-fca4-3521-924e-c96302d259a2 | -14.51475 | -46.9214 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b7be962-e661-38e3-aa8e-867165b0d4e3 | -15.11937 | -43.86657 | 2025-10-07 04:38:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9172a26-af11-336e-8367-582eb742daa2 | -15.39114 | -48.00971 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 494cb6fa-9f89-3a82-96e1-b31602604399 | -14.76214 | -46.02625 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e0ca385-d949-3846-87c9-87ebc44c0bb4 | -14.92518 | -51.44699 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1fe37a-3c15-34e5-a8e9-ab4d4cc57105 | -14.90645 | -46.83195 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f199ffc-6dc5-361e-b8ca-9164d5782c8f | -13.33138 | -47.5584 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README64.md)
