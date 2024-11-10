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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3643858b-a7f7-35e7-9982-5364f253ab0b | -4.277 | -48.18366 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7ae0e93-9c2a-351f-8d92-f0c1e3a177f3 | -3.03675 | -50.37637 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ead0812-f54e-3be6-b9e5-80beb82bdb7b | -4.32083 | -49.76538 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8920d912-80a8-351d-bc3e-b53e5a80f01d | -0.95201 | -52.4455 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56a6f23f-e8e6-3638-9007-ce48cc35e90b | -3.96534 | -49.94431 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 971ec4d2-31c0-3b4f-b0a0-3a0b6a8072e3 | -3.96851 | -48.18089 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1b66313-bdb3-362d-899f-99df7564cc34 | -1.6806 | -52.05589 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08fe66c0-377a-3d38-a564-979cdad26e3a | -3.24641 | -50.27368 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 380c7db1-be64-3dac-a124-f7efb0edfd9d | -2.6817 | -51.81899 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 50c75edd-5eba-37a8-a0b0-308d82aaf498 | -4.09411 | -49.12429 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb83fc16-360d-394a-9ef8-304795650608 | -2.20787 | -47.73943 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9a24f885-b6c9-340a-aeab-d49c86bbcb76 | -3.21363 | -50.38404 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7c5a021b-a156-3349-a7fc-c77db91aa389 | -5.26926 | -46.31332 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b0408a6-4e6c-3d19-b0e5-71b3413b1573 | -2.56908 | -50.68164 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2fec1af-ce18-3697-ae05-377c2b3f934a | -3.28578 | -53.25629 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7fcbac6b-819b-3e16-85a7-ac827db372e2 | -5.40064 | -48.26162 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 017dc5bf-f7b6-37dc-87b1-bfc59b01f4ac | -3.99194 | -46.41403 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf2d4973-50ae-36fc-b47a-977f078aabaa | -2.6856 | -46.80902 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efa16485-881d-35e8-9cf1-464cb227e731 | -2.30047 | -46.72292 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e0f433b-59be-3676-bae6-1e549098d1c0 | -2.19843 | -48.36665 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83389fc4-3fae-36c9-9f6d-41bf7564557e | -3.64306 | -45.64316 | 2024-11-10 04:14:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a871b24-08de-3d16-b144-a44034f42fa9 | -3.87265 | -50.25935 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d022f7c8-985c-3853-aa43-4e79dccb30ab | -2.15274 | -48.84887 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 376f0260-0ab3-3730-ac2e-a97162c45b13 | -4.71027 | -46.3835 | 2024-11-10 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4771320d-061a-3d9d-b644-d472524bc180 | -3.81337 | -48.96358 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34a4c04a-508b-37f9-90db-e3588467a63d | -2.61327 | -51.7508 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5d0dd47-621e-3d35-b450-6f60df9390e6 | -5.32864 | -44.84022 | 2024-11-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 473b9c3f-d17f-30a8-8b44-2b4e524ec26e | -2.25078 | -46.56337 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c31ad00a-654f-373f-95f1-8cb305367012 | -6.25117 | -43.55618 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daeb7407-ee51-30b5-9d44-549a1155d755 | -3.05486 | -51.07069 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8de357a-c19e-3f46-ab5c-3e29e82870a9 | -2.32529 | -48.52975 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ac9450b-4792-38a7-9cc0-a83cabf801a1 | -2.76851 | -49.3545 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6af10476-be9c-3645-9f2f-72f959c35c24 | -2.62804 | -46.15157 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 713315c2-8e1e-34f8-a0c1-bd074da9c0c6 | -2.93081 | -48.31591 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba468773-93eb-320d-a1af-a116520b06c7 | -4.36845 | -47.25542 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 996650a3-f5d1-381f-aa81-a76a38779890 | -2.657 | -49.40201 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 059c5dd7-1e5e-332a-892a-cde3879669c2 | -3.20564 | -50.62876 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ba76c7ef-ed61-3341-a038-bc647eb295e4 | -2.59963 | -48.19273 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2359c09-cc77-32e4-a7ed-07c458776d19 | -3.80857 | -44.68446 | 2024-11-10 04:14:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f913c738-fe24-3382-8e9e-b6e1bf2b796f | -4.10491 | -48.9741 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c46f568e-0de9-3080-a5f0-6ffeb167469a | -3.11442 | -50.14738 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6380d7c-18e8-32b9-bd56-e226ca67db74 | -2.8696 | -50.32261 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99546b60-c149-37d8-a982-e0eb0aabfb2f | -3.24442 | -50.31703 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 45da270b-6307-3525-a905-15693aad14d4 | -3.57199 | -44.53731 | 2024-11-10 04:14:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f614e366-0bc0-3783-b173-2da7a347ddae | -2.18436 | -46.57003 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 647c3cc1-c614-348c-a327-5dcd3ffc22f3 | -3.23675 | -50.27195 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| de254f1f-d9cd-3c7a-a23c-2826a99c6e5e | -3.96789 | -48.18464 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ca79439-0693-38a1-b630-c41665797603 | -1.23074 | -51.96605 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb38b04-555a-3853-8c34-95af82ef9e24 | -3.07759 | -50.4957 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16e5a604-5f1f-3aea-9fba-9ed0f89c6294 | -2.84965 | -51.3653 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed1a917f-d0ba-36f6-bc50-cefc49bbc545 | -3.44344 | -50.29954 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 57ea5922-5fde-3be2-bd84-410b6528c4b0 | -1.5969 | -47.56796 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb3209a-d7c9-3731-a5c3-f5d2ff2cc17c | -4.10767 | -45.70388 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8309be7c-178e-338b-a72f-39e5e4138686 | -1.43567 | -48.14416 | 2024-11-10 04:14:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf5243f9-7bed-3f4b-8698-bad7962a8b63 | -3.52012 | -40.90903 | 2024-11-10 04:14:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2180e578-4474-3481-940f-0c04c4412262 | -3.38778 | -51.46875 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6c998bf-9aef-3299-ba05-0e67cb33ba26 | -5.38298 | -45.44678 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c79ae90b-f8b9-3045-b33b-d86adf749462 | -2.11739 | -46.47941 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9d08ab11-0667-35ea-ae6c-e9bbca5db333 | -2.901 | -45.56733 | 2024-11-10 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f71be1a3-f3c9-304d-8f83-ad7cd8562a5d | -2.68872 | -46.81436 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c945bef9-e56c-30e0-9323-ff2541ed2778 | -1.39601 | -52.36064 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d03b382-d280-3c03-adac-8fc9a7f8014e | -4.9369 | -48.52223 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 711d11ea-72ad-3b30-a6ce-72dd40b8cfaf | -4.43547 | -47.2428 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebb6b21b-68fc-3f84-a3c4-3f7a92f30c8b | -3.1147 | -45.97216 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af3bb719-206f-3e16-9961-feaf92d91033 | -3.22274 | -50.29707 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a33274e1-5117-3e8e-9c68-ddaf636946bf | -3.00248 | -40.28228 | 2024-11-10 04:14:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 83c18a66-2944-398a-9cf1-b93862c2bd95 | -2.4197 | -46.6807 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 213e6c4f-c7ba-36b1-bf7b-ef62602986da | -4.11924 | -48.23636 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92325072-72e2-3e28-adbb-5c23f1b02207 | -0.29012 | -51.72949 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c0d509-70d7-3eaa-a6be-876f06f53301 | -5.32466 | -44.84335 | 2024-11-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48ec8a71-60f9-3819-bdf3-87ba4fa38b8f | -3.52801 | -49.99688 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 024c0816-d815-36f0-8a49-513400a6bdb4 | -4.38182 | -48.57358 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 606cd2c7-aa56-39f0-8b79-c13130cf70e4 | -2.17555 | -48.31693 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8b51566-6c6f-3d50-83d6-ff2b2d23d8cb | -4.11482 | -45.70498 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b7be062-d401-3dd7-84bc-ca68fe7ab1e2 | -2.39439 | -47.71859 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c9939f6-4394-392e-b11a-995a4da9367a | -5.36924 | -48.24899 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81a2833e-053d-3d34-947f-4fbba80a250e | -2.66935 | -46.7867 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69521a95-d274-3ffe-9597-9ece84aedd09 | -3.9527 | -48.14768 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 54d1dc9b-cd49-36df-ac38-5027964c7e5f | -3.5374 | -49.26387 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db507900-08bd-3949-80cf-7f76bb7e294d | -3.1325 | -50.44963 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 547aaa02-f8e9-339e-bfdb-a2fed036ea01 | -4.09338 | -49.12862 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4dc2859-7288-3847-87f4-af01cd0ae1c5 | -4.09706 | -49.13368 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 493b9bd9-3ce2-3b8c-8ca9-eee0cf006a57 | -5.30155 | -46.2277 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e76916-a45d-3a65-a8b6-457488c95437 | -3.61972 | -50.61834 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c57421d-60e1-3808-958d-1042ebab588e | -3.48063 | -48.24184 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 769fe59d-3b64-34b8-bb2f-3717dccc4be2 | -2.12433 | -46.38514 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74061ddd-bc09-3e01-af39-bdb4bb196293 | -3.96111 | -48.12236 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd4edf5a-585c-31cd-8550-017b25d30995 | -2.68016 | -46.79341 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070fb65f-8af7-3408-9dc2-f7e22999539c | -3.26012 | -51.00899 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b242e0de-b169-32ec-9435-e938c520076b | -5.17528 | -47.61728 | 2024-11-10 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54309ab7-63ff-387d-afcc-38c3c4440de3 | -2.63043 | -46.77245 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be1eeacb-06d0-3166-9f78-672a2a0a50af | -3.62368 | -41.57849 | 2024-11-10 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da5fde2a-f648-36dc-a01a-ed09b8ce6034 | -2.08994 | -48.8224 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 78534cec-1dd7-3c4c-8082-7185a8600e9d | -3.25327 | -50.315 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bde908d9-c7db-3b72-a25e-848863ed7a78 | -3.78177 | -47.73988 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6205889-2cd0-37bc-8233-71174dbf51f7 | -3.22766 | -50.68034 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bd53055a-2668-3206-a38e-0d5d7430ea9b | -6.25063 | -43.55964 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb38b6c2-2881-3bde-bd91-7996086c3df0 | -1.33956 | -54.6298 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b625e472-8736-3518-8120-d9250b34835b | -3.83732 | -44.12767 | 2024-11-10 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 113d10cc-10cb-336f-b305-5cf43e030768 | -1.13707 | -54.10399 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README40.md)
