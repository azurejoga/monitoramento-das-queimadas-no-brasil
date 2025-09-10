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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdea6b14-b652-3ea7-806e-62b229c4d88a | -17.58662 | -49.81815 | 2025-09-10 04:19:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e07a1bb9-361e-309f-8cd0-d42f4da1f126 | -18.31514 | -49.33172 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44f06d33-b7c3-3c5f-9179-ee69697bea9c | -20.2845 | -46.24699 | 2025-09-10 04:19:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7605864c-bae6-375e-a597-34f7519e42ec | -18.98759 | -44.22949 | 2025-09-10 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78502e21-9888-336d-a179-74860eae20e9 | -20.16216 | -44.76591 | 2025-09-10 04:19:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dd9f101-4e65-34c4-aec7-f6c454a6ae09 | -19.29671 | -47.98789 | 2025-09-10 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0a2d7ef9-428d-3b69-964f-734f90d0da7c | -19.52011 | -45.01616 | 2025-09-10 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b3d1343-d911-39c5-ab94-0a9da0bbafb8 | -18.13272 | -51.72369 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4099789-7935-3be1-9f8d-9653bd8d28e5 | -20.15974 | -43.65891 | 2025-09-10 04:19:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e8dfee9-b7e1-3a33-b2b4-901e1af6c451 | -19.51675 | -45.01559 | 2025-09-10 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a338c15d-88d3-31e0-b7b4-2f940195abad | -18.33524 | -49.34439 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22c92d28-e296-31f8-9624-12ac59ac882f | -19.30073 | -47.98466 | 2025-09-10 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c048d15-9c6f-3ffd-b1ee-23f641dd092e | -19.64503 | -45.04481 | 2025-09-10 04:19:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 47c1366f-827a-36c5-a49e-36725b0cbe94 | -18.90486 | -48.99287 | 2025-09-10 04:19:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bf31fed-9f4d-3c42-8faa-30863fa28043 | -19.8144 | -47.78753 | 2025-09-10 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef34e4c8-224d-39fa-aebf-8321b725c8e6 | -18.00604 | -47.11343 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a0f28b0-a100-3a47-a04a-e61f3114c6a1 | -19.66684 | -44.89789 | 2025-09-10 04:19:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69af164c-b5f6-34b1-85c4-f4f72529b993 | -18.13613 | -51.72841 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c4a85ae2-a905-369b-a40d-e4b40a1879ef | -18.02975 | -47.13663 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55903483-238a-3939-ac21-e740d689cf53 | -18.03467 | -47.1487 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3442eb99-f3b7-378b-9211-fd2556a538a2 | -19.13978 | -47.13772 | 2025-09-10 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2acd531-6270-3912-81b9-d5fe5349cb7d | -19.17073 | -43.0611 | 2025-09-10 04:19:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5fc4d4d5-42f8-34b1-9ee4-ca214a6a7dcb | -19.28995 | -47.98666 | 2025-09-10 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 402d57ec-29f8-367a-b031-8f9b105f076d | -19.58037 | -48.80957 | 2025-09-10 04:19:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da9532f1-9e25-314d-bdb8-93d59f15f4d7 | -17.20847 | -50.17323 | 2025-09-10 04:19:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5adec656-e24b-3418-a6e3-d541f30e7c27 | -18.01152 | -47.122 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d929c996-310d-35e0-987c-64c41255038e | -20.01863 | -47.76614 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ca00d88-177f-31fb-a626-491b974cbe71 | -18.45095 | -49.56802 | 2025-09-10 04:19:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7ca6cdd0-ecb2-3309-b7eb-7296c35f3609 | -17.57783 | -51.06438 | 2025-09-10 04:19:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b58c07d5-33fe-376e-8ca3-72086cd3f7cd | -18.0109 | -47.12579 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea9880ee-96a2-387f-9b1a-becbe7f0bb61 | -24.12809 | -48.29797 | 2025-09-10 04:19:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 04b6aa25-3eea-3a95-aa89-25fa02b3a639 | -17.20466 | -50.17246 | 2025-09-10 04:19:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8eedb930-6497-3323-9d3c-2960acfd2cf9 | -19.85043 | -48.10438 | 2025-09-10 04:19:00 | NOAA-21 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbb0b80f-538e-3cde-a85f-c96fb63658d8 | -18.35325 | -49.34765 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 25edc848-b2aa-3f63-b597-62cc18a2162d | -20.22291 | -40.36207 | 2025-09-10 04:19:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0ffeac60-9711-32a7-9820-1a1b9cd19762 | -20.01336 | -47.62974 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f4269d9a-f84e-3096-a074-2ae150d92754 | -27.0365 | -48.80552 | 2025-09-10 04:19:00 | NOAA-21 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f84f1f42-666e-30a6-87e1-67953e4f0e54 | -20.06045 | -47.53049 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19b6c963-79c0-3782-9bbe-330e5a0b9aea | -20.01064 | -47.62533 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8439dbf6-0c04-3aa4-af68-e83b708d2e9f | -17.20345 | -50.15701 | 2025-09-10 04:19:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ebc3f33-2ab3-3778-b451-89412f91078f | -20.02915 | -47.61729 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a832c69-bf55-3191-afe8-8984fec58893 | -20.05984 | -47.53422 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b01d461e-ea3b-36a9-8ff9-b255334e33e7 | -18.69922 | -52.58933 | 2025-09-10 04:19:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ce50a11-4318-3cc2-921d-225b04fd7f90 | -19.91812 | -46.15421 | 2025-09-10 04:19:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df107cff-a181-302d-886e-ef8e3b663f57 | -18.46298 | -46.47492 | 2025-09-10 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd3373e-a85e-379d-9647-279a36f4a55f | -19.17014 | -43.06538 | 2025-09-10 04:19:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37d519a8-7562-3212-8ece-358fe2b480fe | -18.03526 | -47.14503 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 651a983e-0d6b-32ce-9a4f-91cf7d2a6de3 | -18.35495 | -49.34623 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 61c389e6-15e9-3d11-9356-2ec9153e9dbf | -19.30573 | -43.26052 | 2025-09-10 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2885f589-6560-3262-9aa5-71ca7e259336 | -19.64559 | -45.04104 | 2025-09-10 04:19:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 467603f2-dc9a-30b4-b28f-f6324c41704b | -20.05134 | -44.13485 | 2025-09-10 04:19:00 | NOAA-21 | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a760ff96-ca89-3116-9fca-247fd0582309 | -20.02199 | -47.76674 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 403b946b-943b-35ba-842a-9e2786d972a3 | -19.75101 | -45.71581 | 2025-09-10 04:19:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e7ba323-8853-34ef-8393-c3f6b7425173 | -18.01042 | -49.39521 | 2025-09-10 04:19:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 100edc81-0f8a-3784-a468-42d6e0333d8c | -18.14439 | -51.73001 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| df186661-f3b7-3ddd-a2c9-552717d4c9ae | -18.52608 | -43.28191 | 2025-09-10 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ab53ae9d-3623-38c7-ba81-8e912fbf5ada | -18.69322 | -52.59725 | 2025-09-10 04:19:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75519cfc-53af-30e2-90c9-e65642b630ab | -18.89132 | -48.18202 | 2025-09-10 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40ae259a-0ede-3491-b4a4-1ea3e5221cc6 | -18.95671 | -42.38914 | 2025-09-10 04:19:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 812c008b-b2fa-3c67-b614-76a1e72f5e27 | -26.67776 | -48.89597 | 2025-09-10 04:19:00 | NOAA-21 | LUIZ ALVES | SANTA CATARINA | Brasil | 4210001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77168fa1-6c70-3f79-b585-e3c1885bfb09 | -19.30009 | -47.9885 | 2025-09-10 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 86257f8b-0456-397e-855d-91ef0f265208 | -18.28532 | -45.38926 | 2025-09-10 04:19:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e021290-3de0-3072-8235-d72bd10cab31 | -20.01397 | -47.626 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 144b6285-2c6d-35ec-82ad-19ceaad85dd9 | -20.06925 | -47.53973 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 579c7cce-6147-3fec-a883-08582d5f6154 | -18.02128 | -47.14648 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eb32be58-f6be-3dc6-b3f8-a2676b08037f | -19.77736 | -45.78812 | 2025-09-10 04:19:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0b83117-5fe2-3c6a-ac57-1f3200bd1eb4 | -19.85106 | -48.10053 | 2025-09-10 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 057382b3-84ed-303e-93b8-6313ba74aa9b | -19.87318 | -44.02949 | 2025-09-10 04:19:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 24df8455-7702-3fe1-ad52-6705f5d70bd4 | -18.03192 | -47.14447 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e973a06d-3073-3001-8a40-3ad3c0ad89f0 | -18.46025 | -46.47074 | 2025-09-10 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91d83d94-5106-36d1-b7c5-fa517e11249a | -24.22988 | -48.48993 | 2025-09-10 04:19:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8d9c4fef-3a9b-3875-9f2a-97f7c671a677 | -18.01058 | -47.10668 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7d80396-63d5-3b8d-8fd9-22359b03ada5 | -20.00185 | -47.61598 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5da792c-cd70-31f2-a7d3-382bd1ebf7a1 | -20.05955 | -47.51488 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4430d13c-52d5-327d-86cf-128722df5377 | -20.19117 | -44.44872 | 2025-09-10 04:19:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2e3a4c0f-da66-36bf-a528-bdb8a5d1b1bc | -18.14026 | -51.72921 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e40fa8e2-a189-38ce-9d19-d13be4ac397a | -18.34105 | -49.33223 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a39972a3-f8bf-345c-88cf-ef2be58ae3a6 | -18.31154 | -49.33107 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4185f147-aab1-333b-96f9-516aeb951651 | -20.06652 | -47.5354 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1f592fb-578f-357e-a7e1-735b797ecadd | -20.00366 | -47.60492 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9153c2b4-bf9f-3d92-b960-5e4fdb4aeb36 | -19.53924 | -46.0972 | 2025-09-10 04:19:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4f2347e-c5bc-3de7-928c-9c16ce06ab92 | -19.28784 | -47.97835 | 2025-09-10 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 105118c8-0e0c-3118-b9ab-305c967a1f6f | -5.66916 | -43.34765 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c9782df-aa79-3057-a672-6e5b6bcfcad8 | -5.94858 | -45.80414 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae5c2b86-b37a-39b7-a4a4-8501a02875e5 | -4.09274 | -50.69231 | 2025-09-10 04:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f332c6c3-2077-3e37-bfa0-86d0ca8928d5 | -4.54486 | -43.30132 | 2025-09-10 04:40:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f308c640-d7bf-3b8b-9029-9d9b3f04bf83 | -2.38579 | -47.71552 | 2025-09-10 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc45b775-83c6-328d-876a-0119aaefdc55 | -4.88571 | -44.96074 | 2025-09-10 04:40:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf20296-f0a5-360f-8803-c80a6ff0c032 | -5.90492 | -45.79297 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2630081-620d-31e7-b7ef-5e827480c7a5 | -5.20708 | -43.70783 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 617f2e83-1952-3b38-a8fb-e39c749680ea | -5.22657 | -43.69156 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e0ca1c4-fb67-348f-96b9-680d902bb4bc | -5.56924 | -42.92699 | 2025-09-10 04:40:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7e6bd8f3-db47-321a-bfaf-f22a62fbef6c | -5.73331 | -45.59927 | 2025-09-10 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 943fded0-3e29-307e-bbb6-32719639c1fa | -2.79015 | -48.60563 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c4a5e24-fc66-3f75-862d-960d5afd9902 | -3.96809 | -47.16985 | 2025-09-10 04:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90849180-63a5-3910-a082-70e55046a155 | -5.66715 | -44.91477 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 712595c8-1e45-3a12-a62d-35ab8ff1fdfc | -5.39292 | -43.44445 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8357fe4-404f-3a96-8649-e7a83c58018a | -4.49405 | -47.82174 | 2025-09-10 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 016d0080-e8c5-36ba-a2d2-a06b68bf23e1 | -3.98897 | -43.25035 | 2025-09-10 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a99f6003-e74e-3ace-bc72-971dea8a3d8d | -5.72115 | -45.42114 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README51.md)
