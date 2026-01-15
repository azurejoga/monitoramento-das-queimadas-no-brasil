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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a3cd03d-b45c-374f-af74-b2ed78b8cba9 | -20.30419 | -55.79424 | 2026-01-15 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c55d5c9c-c650-3629-955d-8f28b6ea5df5 | -20.41961 | -57.83609 | 2026-01-15 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 73fde85e-0869-3700-8828-dbe8b85830d2 | -20.41863 | -57.82072 | 2026-01-15 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 14c2e9d0-3662-3062-812c-0c94877be143 | -20.4098 | -57.81155 | 2026-01-15 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 55d9c56a-d95f-3fa1-bd73-11de9174ad48 | -21.35857 | -56.86575 | 2026-01-15 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a7f425b7-8a47-3343-9609-4fdc6e62da5b | -29.77505 | -51.17897 | 2026-01-15 05:10:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 2136130a-5103-3a75-bcda-e32230d9a59c | 2.70099 | -60.07202 | 2026-01-15 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 588c71ae-e8ef-3f50-84af-7113ef000096 | 2.70044 | -60.06844 | 2026-01-15 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbe18b3b-bba2-35b2-8dee-93f17250c6a6 | -10.3132 | -59.0635 | 2026-01-15 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d52142e-bb8a-39cb-960d-7cc37701bd12 | -15.59385 | -57.34169 | 2026-01-15 05:25:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92798540-3e1d-32ca-9be8-3f835f5b5f7e | -11.91022 | -63.80598 | 2026-01-15 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcb07cbc-1d3b-3b53-8cdb-a2c2fb9749c9 | -15.58922 | -57.34498 | 2026-01-15 05:25:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f950efa-e579-3df9-9a8b-25ce55bece4e | -15.59333 | -57.34557 | 2026-01-15 05:25:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a55274a-e07b-3a72-be49-1546c603b7e4 | -15.58974 | -57.34109 | 2026-01-15 05:25:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cf6ccbe-4076-3ebf-b10c-f881873070b1 | -10.31378 | -59.05958 | 2026-01-15 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a128cfc6-a751-3db2-9736-c096267091f3 | -14.00162 | -56.08144 | 2026-01-15 05:25:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 141a8236-0120-3c53-b9f8-4aeb59139526 | -12.83899 | -58.29982 | 2026-01-15 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1b0f45d-f3c2-3bce-a792-35036e6d80a8 | -13.99723 | -56.08091 | 2026-01-15 05:25:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97672dcd-74e1-32a6-a422-198fa325a0e6 | -10.31728 | -59.06013 | 2026-01-15 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275d9d1d-389b-3894-a84d-3e874cda76a4 | -15.25505 | -56.72338 | 2026-01-15 05:25:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c15b9fe-a1eb-31af-b909-85ee8cce823f | -13.98102 | -60.3331 | 2026-01-15 05:25:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d139991b-1ed4-3740-87d5-3c55624faea5 | -13.99781 | -56.07649 | 2026-01-15 05:25:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef091368-3d92-373e-9cd7-a4f9fe35814c | -20.40849 | -57.81172 | 2026-01-15 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3d65088e-050f-3ee5-94cc-dd755189a99f | -20.42251 | -57.83935 | 2026-01-15 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 07c267f0-b166-35cc-a4ee-1d8e9968b1bb | -16.5878 | -58.21708 | 2026-01-15 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b8766213-6de2-35ed-bb79-28cdfe20d1e3 | -16.44821 | -58.16209 | 2026-01-15 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8d6e5ec5-6c3e-3e94-8d84-0ad27709a7a5 | -20.41824 | -57.83876 | 2026-01-15 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ea5321be-371e-39ce-9144-81ca0f1937b1 | -21.3557 | -56.86753 | 2026-01-15 05:27:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9041f4a1-78c6-3c1d-981c-827c3d0a1124 | -3.22954 | -41.79778 | 2026-01-15 06:03:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f314bbb2-0caa-3681-9a0b-1b62ce5f4892 | -6.88025 | -42.8402 | 2026-01-15 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d72d183f-f377-3708-acfd-e10cecb50db7 | -3.65914 | -43.50928 | 2026-01-15 06:03:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 22e55386-762f-38e2-bbaf-dd1e2571ed59 | -1.46873 | -45.71373 | 2026-01-15 06:03:00 | AQUA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a7b2f2e9-bc30-31c2-b5b5-e2f158a388d8 | -7.24711 | -43.05259 | 2026-01-15 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ce106169-25a5-3523-9bdc-83ace2b4267d | -7.23772 | -43.05124 | 2026-01-15 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 900b6514-512e-35ad-8747-4daa93771464 | -7.04961 | -43.94946 | 2026-01-15 06:03:00 | AQUA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d8624202-54cd-33ad-8257-763c6ff8fb7b | -7.22834 | -43.04989 | 2026-01-15 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| c69a7f1a-ff72-34dc-9650-b8f155c3a4cd | -1.47014 | -45.70436 | 2026-01-15 06:03:00 | AQUA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5931f8a1-931a-3e43-8317-bad969881859 | -5.8978 | -42.54795 | 2026-01-15 06:03:00 | AQUA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 76fe0ea2-9249-3dc2-8f6a-67b66d4c0cac | -3.65779 | -43.51827 | 2026-01-15 06:03:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 71254e5f-3264-35f0-a6f2-a366a221b809 | -10.59328 | -44.97022 | 2026-01-15 06:05:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 87578dc5-d71a-36d7-bae6-ba1893fc14fa | -12.66227 | -46.76156 | 2026-01-15 06:07:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 094fb95c-122f-3267-960d-070cd595bcdd | -12.65349 | -46.7602 | 2026-01-15 06:07:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 059df0aa-eec6-3bec-97d4-5758356d222c | -2.51349 | -45.8149 | 2026-01-15 12:31:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 9bb65ad1-21a1-39a8-8f61-a23e2fd4ac23 | -1.24745 | -47.50154 | 2026-01-15 12:31:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 5424e252-f3d5-35b6-a812-58af4ef400e1 | -7.49075 | -45.54567 | 2026-01-15 12:33:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| f76ce838-49c8-372a-bc0f-8864f9039060 | -7.50561 | -45.55285 | 2026-01-15 12:33:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 0bde9443-5473-32f2-adc5-48662594a1d5 | -8.85557 | -44.16211 | 2026-01-15 12:33:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 6bae21be-e9ae-3cc3-ad5d-03bf2a421222 | -8.92255 | -45.98135 | 2026-01-15 12:33:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 02d4acbf-da66-378a-933e-e07220b5ac47 | -5.94777 | -48.0145 | 2026-01-15 12:33:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 09a8b2dc-daf7-33ed-a2aa-8b23138f53ef | -8.92675 | -45.96017 | 2026-01-15 12:33:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 855b8114-e723-3657-84ad-49bb7f0c9d12 | -6.71701 | -44.06308 | 2026-01-15 12:33:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 90995612-12c0-315c-b44e-19d466b5bd46 | -7.32868 | -44.25178 | 2026-01-15 12:33:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| d5362172-4bae-3df7-a492-e688fa986378 | -6.71274 | -44.09855 | 2026-01-15 12:33:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a2d3ae55-3bdc-3193-8816-6f65f7df4685 | -7.50557 | -45.54753 | 2026-01-15 12:33:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 94c47650-65fe-3e49-bdb0-e78566c2e384 | -6.72258 | -44.09222 | 2026-01-15 12:33:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 25677ced-d4d7-3c76-b770-f1c678c22295 | -8.85989 | -44.16926 | 2026-01-15 12:33:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| d692d506-9fde-374b-b729-0795a161423b | -7.32164 | -44.24589 | 2026-01-15 12:33:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 87a510ff-94fc-3a41-aade-88ed6f00c2f1 | -11.45393 | -52.75829 | 2026-01-15 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 458dc150-8b37-35f4-aeb2-632a8b780294 | -16.67826 | -49.13974 | 2026-01-15 12:38:00 | TERRA_M-T | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 8476d8b3-c040-33ca-8f93-857c45e8f927 | -12.84025 | -52.52142 | 2026-01-15 12:38:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d7c24f97-3e2a-3697-b6e9-1ff8697dd8a9 | -13.68529 | -55.68418 | 2026-01-15 12:38:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 6d05e807-0830-3df1-bfa1-78d2c4e51a8c | -16.3184 | -45.10509 | 2026-01-15 12:38:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c780510c-d569-3423-a9bf-0b33490fdec5 | -13.22316 | -57.54894 | 2026-01-15 12:38:00 | TERRA_M-T | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 28f8b803-a0f3-388f-b16d-b466aacf8e81 | -20.06816 | -57.19134 | 2026-01-15 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2fcb6ba8-081f-3c9c-ad27-1b605418048e | -20.44219 | -52.87903 | 2026-01-15 12:38:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 492a13f1-95dc-39b0-bcaa-97fa1341333e | -13.69417 | -55.6855 | 2026-01-15 12:38:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| b672cda7-c4d1-38d6-9fa2-edae5a48196c | -16.31661 | -45.09782 | 2026-01-15 12:38:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| cbd9491a-ef9d-3e37-91e3-4b5ab24b84e4 | -14.19847 | -57.26487 | 2026-01-15 12:38:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 9bf12cda-3394-3b0a-90c3-1e774e2e6c29 | -13.6955 | -55.67638 | 2026-01-15 12:38:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4dfa727a-a5df-3c87-b238-36371bda1505 | -14.2 | -57.25473 | 2026-01-15 12:38:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f579802f-27f2-3724-acf5-1acf852e79f4 | -13.68662 | -55.67506 | 2026-01-15 12:38:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 19c74d50-0787-3b8b-bb27-d4abde9ad8d1 | -12.81939 | -56.85393 | 2026-01-15 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7e04d9bb-6694-3313-9330-e8282da022d9 | -7.2411 | -43.0428 | 2026-01-15 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 191.3 |
| 98c32f67-a96e-358c-a555-3d4f25a3911c | -7.2222 | -43.0447 | 2026-01-15 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 302.4 |
| b01fcdac-7256-351b-9b54-b60ee8218e03 | -27.94408 | -52.91535 | 2026-01-15 12:40:00 | TERRA_M-T | SARANDI | RIO GRANDE DO SUL | Brasil | 4320107 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| a8e8ed74-7d4a-3642-8d05-f0a9c2f2912b | -26.16238 | -52.96101 | 2026-01-15 12:40:00 | TERRA_M-T | RENASCENÇA | PARANÁ | Brasil | 4121604 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1c955de7-2447-3220-8e6f-1ad70b756ce7 | -28.97289 | -51.06956 | 2026-01-15 12:40:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 537a216b-8f11-3df6-9a42-44184059d9bd | -25.58535 | -51.16014 | 2026-01-15 12:40:00 | TERRA_M-T | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 55ba8148-7b75-31cc-8782-d56a6ec34a81 | -27.80246 | -51.14036 | 2026-01-15 12:40:00 | TERRA_M-T | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| ffb07ccf-d6a0-39e4-9b16-304aeb3b96ad | -25.57915 | -54.57246 | 2026-01-15 12:40:00 | TERRA_M-T | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 22716a81-b811-36b3-93a9-198080141848 | -26.26034 | -53.61872 | 2026-01-15 12:40:00 | TERRA_M-T | DIONÍSIO CERQUEIRA | SANTA CATARINA | Brasil | 4205001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 81ffcec8-6cde-3fe1-b338-3bebb4a04772 | -23.869 | -53.65211 | 2026-01-15 12:40:00 | TERRA_M-T | PÉROLA | PARANÁ | Brasil | 4118907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| ec936bfa-7cc3-3aff-bb36-52749554e4e4 | -26.15559 | -53.02241 | 2026-01-15 12:40:00 | TERRA_M-T | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 9df7be08-4a48-393a-9865-3d1ee176812d | -21.86957 | -53.85149 | 2026-01-15 12:40:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 22b2b05a-e731-3641-877c-cf1939a3f696 | -25.66936 | -53.80725 | 2026-01-15 12:40:00 | TERRA_M-T | CAPANEMA | PARANÁ | Brasil | 4104501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| fbbd5bfd-09f8-3cd8-8228-835f3b5bd560 | -27.80453 | -51.11803 | 2026-01-15 12:40:00 | TERRA_M-T | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| b52d76e3-545c-3489-bea8-573fdbd07eb9 | -27.80037 | -51.16285 | 2026-01-15 12:40:00 | TERRA_M-T | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 13c89f0e-4ccd-3996-aab4-1a9328a204e6 | -20.39233 | -57.80112 | 2026-01-15 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 69376aa6-19e9-37ee-b965-b536e03c80a1 | -29.22163 | -51.32577 | 2026-01-15 12:40:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 88733911-94f8-3120-87c2-ef5355155828 | -7.2222 | -43.0447 | 2026-01-15 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 272.6 |
| 956d165e-69c0-328a-8974-bb21aa959e4e | -7.2411 | -43.0428 | 2026-01-15 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 177.0 |
| 89af4998-7e0d-322f-b12e-a25d7c020fa2 | -7.2222 | -43.0447 | 2026-01-15 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 305.2 |
| 493e369e-ff34-357d-92c1-fdb7e15099a7 | -7.2411 | -43.0428 | 2026-01-15 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 206.8 |
| 4182040e-7516-3e12-83d6-9afaec3c860b | -7.2222 | -43.0447 | 2026-01-15 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 270.7 |
| 7a23f995-e6ba-38b7-9b67-8e092cf5cdb7 | -7.2411 | -43.0428 | 2026-01-15 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 214.8 |
| fa2c0e32-4f9e-36d4-af17-7e9918ce4be1 | -7.2222 | -43.0447 | 2026-01-15 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 313.0 |
| 229b8d65-f908-3545-82d8-3fcffb4b89ec | -7.2411 | -43.0428 | 2026-01-15 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 203.8 |
| 65ee81af-3c09-34bb-9d91-28dbcce8999e | -7.2222 | -43.0447 | 2026-01-15 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 327.6 |
| d00a4300-7971-3932-9743-cec572ea9fe7 | -10.1518 | -42.218 | 2026-01-15 13:50:00 | GOES-19 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 33e0fafc-f2ef-304f-b7f4-15a1c6d1ccf4 | -10.1518 | -42.218 | 2026-01-15 14:00:00 | GOES-19 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 124.5 |


[Clique aqui para ver as próximas entradas](README9.md)
