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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1087736-55e3-3d4e-8521-dc2736e7acad | -14.25682 | -50.41159 | 2025-06-25 04:59:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d127c2d6-2491-3da6-9475-5d847861dbdd | -10.8281 | -54.0027 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34e6db1e-12cf-3b8c-a3cc-0a1df749be99 | -10.10392 | -58.22791 | 2025-06-25 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eca97d72-19c1-3231-b64d-106cdc4df5d1 | -11.92956 | -47.84164 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 748ba2b2-31e0-3550-97b6-6c07f4d2ec26 | -11.14312 | -53.93945 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5906d6c6-20c8-30cc-97d0-76c3215caa5b | -10.83145 | -54.00323 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aa2bca2-0287-36b0-9da5-48615a2c1740 | -9.85413 | -55.15829 | 2025-06-25 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7af9aa9-fb06-345e-9010-be7274d63438 | -10.34383 | -51.38169 | 2025-06-25 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8856ab10-ee30-3af8-8058-130e5e48a256 | -10.55877 | -52.01398 | 2025-06-25 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9310e17-c3b1-3abc-82fa-c5d4e63ab117 | -13.61048 | -43.97647 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4af53ff8-8dfa-3d72-a90a-b7664142a5f5 | -10.36099 | -57.2549 | 2025-06-25 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1cbe31e5-d321-3011-9339-404047f89152 | -11.91027 | -54.81921 | 2025-06-25 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f52e2502-fa57-3cc2-ab46-41c8aafff035 | -13.04076 | -48.82801 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d8846957-04c5-3f8a-8eb9-84974757345b | -13.60776 | -43.97564 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e45fd2b6-799a-31f4-b4e4-ea1359d588d8 | -9.553 | -40.3503 | 2025-06-25 05:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 05c2d41b-fc21-3dfe-b091-2a102dfd0282 | -9.5534 | -40.3254 | 2025-06-25 05:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| a76de767-ea7a-3fb3-a478-faa5dd0a47d1 | -4.5429 | -48.0151 | 2025-06-25 05:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 51979e77-cf1d-3861-a3a4-f15f94f9a09c | -10.443 | -47.945 | 2025-06-25 05:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 76cc038c-3385-3562-90df-e21b3c949f06 | -23.98405 | -48.91894 | 2025-06-25 05:01:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b400446-2513-3f71-99ea-362b154d8279 | -21.67853 | -57.34522 | 2025-06-25 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4f41bf5-be55-32ad-98db-f37189709b0c | -21.8149 | -56.29662 | 2025-06-25 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac81eade-3f3c-3f3e-9eb6-b1a8f3289894 | -17.45345 | -46.29665 | 2025-06-25 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bbb2d50-7773-35c2-bf07-33d7d4f46ef0 | -20.92618 | -49.09814 | 2025-06-25 05:01:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| ac1207fc-2a27-3cda-b7b0-755fbeb7518c | -19.54985 | -49.68171 | 2025-06-25 05:01:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3467155e-e603-3f05-868b-a13e0020b3f5 | -21.81547 | -56.29274 | 2025-06-25 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 550b3f4c-caa9-321d-8eca-57eeed3199c6 | -21.29243 | -48.5567 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cab13543-ca89-32ef-873a-641072cc8da3 | -17.14478 | -52.491 | 2025-06-25 05:01:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad4fee12-3b77-3cd7-96a1-88ecbd2c4885 | -22.31435 | -53.58669 | 2025-06-25 05:01:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9922f54f-31a9-3b95-ab20-9ae650dac30c | -19.47597 | -54.8443 | 2025-06-25 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9925eddd-7040-3794-9d66-924aeb4339d1 | -21.20143 | -48.51861 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ba223be-e944-310a-a3a4-b66603bcf539 | -16.02671 | -58.61337 | 2025-06-25 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8e4ede78-9ad1-344b-a436-e5c2f781412c | -20.10517 | -55.2445 | 2025-06-25 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 792665fe-6308-3d82-a76f-3a6d16b824ee | -16.33885 | -53.95401 | 2025-06-25 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69c0f591-37e9-3b92-b3d2-bed830b7c472 | -17.45388 | -46.29252 | 2025-06-25 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b323ab2-154a-342a-942a-2f1c5672b3fa | -22.09906 | -56.17055 | 2025-06-25 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90e7bad0-3712-37a8-bbd9-8d964fdfb842 | -21.20566 | -48.52015 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1ff6e16-d966-3cfd-9ea4-23348cc1ab37 | -21.20531 | -48.52357 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc7122f9-57e4-3ed9-b6f2-2da35e18a17d | -18.09513 | -54.28497 | 2025-06-25 05:01:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a75104b5-ca07-35e4-a001-89ab36896cb0 | -21.02182 | -57.01588 | 2025-06-25 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67ba646a-ef72-38c1-b51d-84f80d8b6af0 | -21.20602 | -48.51674 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cda16ce4-dced-3bbb-90e0-15d8376e073c | -21.81152 | -56.29604 | 2025-06-25 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21f316ff-4b44-3fa9-8c10-148345af5015 | -21.20697 | -48.51576 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8943b2c9-68da-331f-a919-1e742e0efefb | -20.92688 | -49.09345 | 2025-06-25 05:01:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 195ed201-5807-38e5-8d72-58f66b7fc11b | -20.47807 | -53.67637 | 2025-06-25 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5fa4c50-4432-3053-9182-f907b51b7eaf | -21.58016 | -45.31264 | 2025-06-25 05:01:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c2fb5da4-af70-366a-870d-1e3dc285bdcc | -23.67576 | -46.82368 | 2025-06-25 05:01:00 | NOAA-21 | EMBU DAS ARTES | SÃO PAULO | Brasil | 3515004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 79169d89-139a-331f-8729-516ef73aadc9 | -21.20664 | -48.51918 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8432abc6-14e7-3478-81cb-ec3842233e73 | -20.92628 | -49.09945 | 2025-06-25 05:01:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 311dc66a-c2fe-34fe-aa67-fbb0995ae0f6 | -21.20631 | -48.52262 | 2025-06-25 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f6ef8ff-0efa-3814-9566-a7d0ec97586e | -18.42913 | -54.55782 | 2025-06-25 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d5a3597-f957-33ee-bc94-d589685256c5 | -21.81209 | -56.29216 | 2025-06-25 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c207ef55-b14e-3d73-b334-64ea5f784c82 | -18.42763 | -54.55907 | 2025-06-25 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3998408b-b9fd-3e61-9f6a-7b5572b43f2c | -21.68185 | -57.3458 | 2025-06-25 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9aaf369a-24c6-3268-a92a-89009f8874d5 | -29.81191 | -51.22574 | 2025-06-25 05:04:00 | NOAA-21 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 02095a91-ed62-3b33-82ac-b26f36fa52bb | -27.8286 | -50.30455 | 2025-06-25 05:04:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d5b9fbb0-8811-3d13-b5ba-17ce68bfe376 | -6.1791 | -48.0712 | 2025-06-25 05:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 4aa51b70-dad5-35d2-80b0-aa1cb05e8b6a | -10.443 | -47.945 | 2025-06-25 05:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| df5979b6-bef1-3960-85b2-54e5725ed89a | -6.1791 | -48.0712 | 2025-06-25 05:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| cdc4be00-7b12-393f-babb-776386ec46c6 | -10.443 | -47.945 | 2025-06-25 05:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 9b76417d-24ec-3b67-a333-0ce3ca607d7a | -6.17943 | -48.0792 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 321d7c74-42dc-3ff4-9743-628ad1ba1428 | -7.09651 | -49.17253 | 2025-06-25 05:23:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76a3a571-5a78-39ce-841f-c53c1ede57b6 | -6.17815 | -48.06218 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9b6efec7-43eb-3fbb-8fa0-34af3cf5ad81 | -6.1766 | -48.07337 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4cd344a8-d705-3b93-bdce-090647853f87 | -6.18165 | -48.0624 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 800abf05-141f-3da9-987c-aba442ec14a6 | 2.74921 | -60.36629 | 2025-06-25 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f8f16d8-3f39-3df6-b99a-fc0843885518 | -6.17906 | -48.05564 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 851195f1-eab1-31f8-95f1-4e21aaf233b7 | -4.54126 | -48.01252 | 2025-06-25 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0fbb9808-2400-3138-b506-f223f64f5cc8 | -4.54205 | -48.00694 | 2025-06-25 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18b49ed4-9e72-3145-b3f2-7d02daa07f26 | -4.53481 | -48.01115 | 2025-06-25 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42aa00ab-035d-328a-af3f-3e5b5c3556ac | -7.09589 | -49.17733 | 2025-06-25 05:23:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f61dac26-946c-3ce9-a2bb-091905d94ed4 | -6.18322 | -48.07433 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| aaba3ec0-95ae-3e8e-b77f-1bcab54225ba | -4.5356 | -48.00554 | 2025-06-25 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f475b785-e93b-3cb0-8bed-490a63bfbb19 | -6.18399 | -48.06882 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78efd0ab-a75a-39cb-8578-a98caf6cd2f0 | -6.17735 | -48.06794 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 69028429-e664-3d52-b46f-4d1b77329dc0 | -6.18484 | -48.06276 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f32d06c-92a6-3cc2-9586-026cf25a42ff | 2.75264 | -60.36576 | 2025-06-25 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 658979cc-01fe-35b2-8272-c75933d97087 | -6.18087 | -48.06832 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8717ec9a-b1bd-3d32-8afc-49ae25cb3ed4 | -4.52838 | -48.00958 | 2025-06-25 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ac1faf6-99e0-341f-808d-d625cb96d994 | -6.18014 | -48.07386 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f70869e3-37d5-37f6-b28f-99bf447aaeca | -6.175 | -48.06155 | 2025-06-25 05:23:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b67a1ce6-1d44-3c59-8013-f6de50fed543 | -7.09916 | -49.17759 | 2025-06-25 05:23:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bd5a1446-f301-3fc8-b8e2-15e093beaa9f | -10.44801 | -47.95652 | 2025-06-25 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9cb29116-eb7d-38a9-b98c-c16b0fa4e93d | -7.92701 | -61.55838 | 2025-06-25 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be88a1a9-ac1e-3a1b-8ebd-ff4a31d10b2f | -14.80914 | -48.29224 | 2025-06-25 05:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1c6d285-a2b6-3305-9054-8b7e8e2dd38d | -10.30056 | -57.13291 | 2025-06-25 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0890bd0-5fab-37e9-9efc-2505f6df1f9d | -11.86775 | -54.69559 | 2025-06-25 05:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7773fb38-b0c6-325b-93b8-6c9d32a409f8 | -12.80789 | -48.73632 | 2025-06-25 05:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47f1a939-5690-3cb5-8358-59335070ef42 | -10.8331 | -54.0058 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1472ebd-a542-34a3-9c2f-65379125f5fe | -10.59732 | -49.46439 | 2025-06-25 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a81be554-4a14-3fe3-b5a5-75f0cf89e9b1 | -10.05669 | -51.11347 | 2025-06-25 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46d83673-da4c-3563-a085-ddc604ceff63 | -10.44101 | -47.95536 | 2025-06-25 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c7c476ee-9fb5-3840-ba87-f0c97210952f | -10.82763 | -54.01028 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d99feb2e-3e61-34e2-a372-a6064d10653f | -8.47544 | -50.27886 | 2025-06-25 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55816cad-bbd3-390c-82fe-5fd502da1f79 | -10.45503 | -47.95758 | 2025-06-25 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8280c07e-00ba-3484-8f48-928bad6d650c | -3.61231 | -47.53636 | 2025-06-25 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b094dc2-2308-3efd-9ea0-7642e50a3610 | -10.59668 | -49.46967 | 2025-06-25 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0a67608-7503-351e-b98e-e159bf902079 | -10.86779 | -54.32293 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37521c94-bf38-3faf-8e19-74c673c810d2 | -3.61466 | -47.53556 | 2025-06-25 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6c788b0-6bc3-3968-93c4-882a59ea1acb | -8.67165 | -51.4628 | 2025-06-25 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17659beb-f0fd-304b-b943-cc5e8cb8cf5f | -13.04715 | -48.83635 | 2025-06-25 05:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README17.md)
