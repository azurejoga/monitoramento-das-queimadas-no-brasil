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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f305fc2-4802-3777-aeaa-5baba4300b29 | -6.24922 | -45.34607 | 2025-10-04 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15b48ba9-e98c-30b0-9ac9-1303ec410753 | -5.69302 | -42.84558 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 935eb799-5eba-3c9a-aa7a-688e0109ff53 | -4.62592 | -47.45731 | 2025-10-04 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1050982c-0e5e-3a01-a76e-f25d561681ff | -6.20002 | -44.64026 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 57848f63-0dc6-3bd1-8d58-fa7390239d54 | -5.9884 | -43.48896 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d6f8c9f1-4136-3066-9f9b-ed9e4715fc5a | -7.75851 | -54.95929 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bb6bfea-90e5-39ea-b755-2cab87e4b1ca | -9.34238 | -54.5297 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f149c93d-31fb-3a4b-9de1-7ca989062347 | -9.51845 | -54.71251 | 2025-10-04 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dba8a51-ca89-35f0-9204-8450d37f097c | -6.99045 | -42.80069 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9a975716-643c-3bab-aa83-f231e7a900ee | -5.68825 | -42.85007 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e67b56d6-4c92-3e10-848b-591762ce9943 | -6.87825 | -47.23772 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e4d2ed14-ef93-31c0-b5e0-9e7508413590 | -6.28377 | -44.03907 | 2025-10-04 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba73d268-191e-3984-b5f3-7d98679c988d | -8.6279 | -54.98717 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1747f224-6cd9-3006-a614-35b1845d246f | -8.85135 | -46.78721 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 564c9473-20dc-305d-b8e5-0ba1a1cbd3e4 | -9.66401 | -48.20718 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 046bc3fa-c776-3627-a6b0-626d10dbbbeb | -4.55721 | -50.46787 | 2025-10-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f4e3b79-659e-3858-9ab4-7620370a75c4 | -8.97781 | -46.72474 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d911340d-5181-36de-bd80-36314a4ee5ed | -8.62392 | -54.96817 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 840d8b9d-ddd5-3688-abfc-2abcdbfee467 | -9.35044 | -49.00784 | 2025-10-04 05:04:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ba1fb7b-62a9-370d-8842-73388afb3329 | -3.70249 | -50.97284 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0a8217d-da93-3228-ac0f-a379844f9675 | -10.07001 | -48.18699 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a034e3e-2418-3d78-af3f-4b3db294fe18 | -6.73288 | -45.97133 | 2025-10-04 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 575d0a65-fc17-3827-9960-4ac2c669d46c | -9.34008 | -54.52168 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5ca0b087-1e5a-3d79-9868-bffedad1527f | -5.66311 | -42.71146 | 2025-10-04 05:04:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a913ce5a-bab8-31e8-922e-4e36c61d67bd | -7.74365 | -46.31678 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6604272d-dd6b-3cf1-9523-1324bc756711 | -7.79243 | -42.57919 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a5ec33aa-36ff-3f1f-bb39-3fa2b0886f55 | -9.93544 | -50.24613 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23ce9f50-2d88-327b-90b7-92f0341ba391 | -8.62735 | -54.99076 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7308a42e-8b57-3ab9-9623-d4acbe88538d | -8.2235 | -46.80767 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1f06141-0dbd-3d2f-854b-4f32cea3db3c | -4.95772 | -45.07573 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aa4a9201-4608-32f7-b9c6-cb3f9b0405ab | -8.53807 | -47.21075 | 2025-10-04 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e7ae70ce-4fbf-3633-bf81-129ade672a17 | -9.34949 | -45.78154 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ef3f0d9-58fd-3347-8e67-fdb6dc4fc9cf | -9.34206 | -45.79253 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 69e40032-27f5-32b3-a725-e50f704138b6 | -8.1421 | -54.85379 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 241f5774-0506-3903-bbce-a3b85bc3fb20 | -9.91147 | -43.80304 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a112b69b-0bad-3956-9684-69b705abff27 | -3.05107 | -51.10225 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e88827d2-0802-3e84-8d8e-143b48f48d63 | -8.96452 | -50.69512 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36811076-8dbe-32a0-aca6-3aa20b06c41f | -10.01713 | -48.27645 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ddd612e-4b13-3e01-a6bb-4a603853ecf0 | -5.21845 | -46.1703 | 2025-10-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2835010b-1582-31fb-9642-02c8c5e79e7b | -9.32816 | -45.76083 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2fb2d10f-0fa8-3eb6-8851-0cc1ed9200a2 | -9.92893 | -50.19638 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bedc9708-593f-3522-aa7b-dde0b8063ad5 | -8.62399 | -54.99026 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9175a4a-22a3-3b08-96a4-60301fa13f14 | -5.82271 | -42.89366 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 696fd04a-8a6e-3bcf-b71f-181228ca9c56 | -9.66371 | -48.20439 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6368051-e3a9-38b3-a1c6-ddca149f8644 | -3.11571 | -59.11229 | 2025-10-04 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 482e99cc-8c30-3499-9a7a-f90164df324b | -9.67122 | -48.22592 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 653015f3-b251-3bcc-b17d-da6ed9e4b068 | -6.35207 | -43.44778 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 362af419-913b-30de-9af6-d9cf6429b82b | -4.25774 | -48.55909 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d895da0b-5dcd-3113-882d-dc3c2361afb1 | -9.92833 | -50.20073 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8bcba35e-808d-3829-aba4-d497aeac54e2 | -9.93666 | -50.23749 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe3cd236-0b83-3734-bf66-c3e3591de997 | -5.24763 | -45.55207 | 2025-10-04 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfb9cfc1-1cb0-3339-ad4b-7142dcfdcc83 | -6.61054 | -44.2929 | 2025-10-04 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b18db6d-bdf5-3c45-ad18-6cec6fda5f01 | -9.33436 | -54.51311 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 831318ce-438d-3685-b558-ba90ac40ac91 | -5.20148 | -45.07121 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f187b3c4-888c-3717-9395-1d0df9c6c987 | -3.77645 | -54.22871 | 2025-10-04 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17bd0269-d125-3fed-991d-9f7875fa803e | -4.95243 | -45.0704 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fd5b18ba-650b-3a3e-8eab-6951f88dd44f | -5.23167 | -46.2188 | 2025-10-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fec06683-8977-32af-a7f7-ba6cc5d414a6 | -9.66619 | -48.22514 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfe528f1-c655-3006-9586-7d14e8e18d67 | -9.31789 | -54.52983 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 834df757-47d5-30a4-beea-dde4b0028018 | -8.18145 | -44.14329 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a30c81b0-af4b-3330-a346-9b58b4cc51ff | -5.78104 | -42.92491 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 5632c512-622d-30c9-87ca-80da57284241 | -9.94277 | -50.22686 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f292c8ef-ad76-3a69-bff9-e2b53af1fad4 | -9.94106 | -50.23811 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 248090ae-0d97-3dd5-ac42-6a41723e0645 | -4.31835 | -48.08916 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f53398c-2ff9-3eb5-9056-f2701e3b3d18 | -9.34692 | -54.52273 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 443f5b6e-a4c3-3385-a273-c3fb39cf997d | -5.27271 | -46.17836 | 2025-10-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f765ba3-5636-319a-a697-8b5f17b09a73 | -7.77504 | -42.60392 | 2025-10-04 05:04:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d96e5a67-5cc6-333d-b113-7348c63d13ff | -3.8338 | -44.55153 | 2025-10-04 05:04:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c915d15c-4b08-3899-b25a-52ec3fbf3797 | -6.44207 | -44.80148 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 066808e4-205b-387f-9bd7-cb6c466ba9bf | -6.65329 | -42.79799 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2bf64893-1481-3f65-b863-2537bd9b4b02 | -7.77126 | -46.26954 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e036fee2-f39f-3722-ae79-baa5b4394898 | -8.54119 | -50.16303 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04081892-4cd1-3241-a3db-1ce7e64401c4 | -3.84487 | -41.57637 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6d262d56-e3f3-35cd-9b71-fd49153a819d | -9.19759 | -50.75743 | 2025-10-04 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9858d75a-3f39-390c-8ac1-b39aed458849 | -8.21762 | -46.81021 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb38e156-3402-3d93-9729-8fa6e79e6a38 | -8.62454 | -54.98667 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3545ef7-42fc-3556-9a61-3ef8d8820d15 | -5.77849 | -42.91707 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 47275995-3159-38cc-b367-d40945682cc7 | -5.69219 | -42.85153 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c994c09-66fa-31d5-816d-8d78c1b9c484 | -6.66005 | -43.47451 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b98a123-0ad9-3d0d-b745-82ef32f9380d | -3.15695 | -49.17631 | 2025-10-04 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f295eb8-75bd-3e20-a362-9f4cde32baff | -3.69525 | -49.56974 | 2025-10-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 891ea82d-5091-3781-91d7-46a55f8c0210 | -6.43822 | -44.45751 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4aeff73f-a63d-3eb0-9c92-f33015343d3b | -9.10951 | -44.39846 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 40c933ce-a6e0-3628-9a9d-d9a9b85f5fb6 | -9.34064 | -54.51793 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e7cba801-c181-33b0-9468-4d414f2cfe54 | -3.6861 | -49.05142 | 2025-10-04 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ec638cb-b4b7-3a12-b7bd-4e195d947934 | -9.92392 | -50.20009 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cb5f264-7be4-3dbd-817b-920b47eaf7a5 | -5.88011 | -42.51448 | 2025-10-04 05:04:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 82906b04-1fed-3cbc-adf3-bb3d4e7a4963 | -8.87683 | -47.81769 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec089a48-e573-37f7-af2f-167e379759b7 | -5.50705 | -51.01764 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4151b282-288a-37dc-b790-c7b02d86d676 | -5.91462 | -49.29943 | 2025-10-04 05:04:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd0d6844-9155-3046-b57a-ecf81d47e494 | -9.75403 | -43.61081 | 2025-10-04 05:04:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 89256b90-d150-3af8-8c3f-44f3567bcbf5 | -3.49916 | -50.26866 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31903d56-952f-3cdd-b500-755d1c019c19 | -8.91929 | -46.61382 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 832356b9-3b9a-3528-a9f8-27547e0d842b | -6.31283 | -44.27677 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ec551fc-94c2-3228-b5e5-0f7739376b27 | -3.89145 | -52.14685 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a05d71fc-bc3d-30ed-ae4c-232d15bb4b52 | -6.07021 | -42.51303 | 2025-10-04 05:04:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 755a29e2-dbc4-3c54-bb14-7a83aafe5660 | -9.33722 | -54.5174 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 539b35e9-d70b-358e-834e-29fb55fe70b2 | -5.83099 | -42.88305 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a28e22cc-fb07-35d7-8252-082da1c7a1c6 | -3.83784 | -44.55266 | 2025-10-04 05:04:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 958b2f4d-ca54-3736-b7f6-b25f861a22e8 | -9.33535 | -45.65792 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README106.md)
