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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 610949fe-79ef-314a-8802-0ac3f046bb1f | -3.21962 | -50.28561 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 0e042ae8-7ba3-3920-9203-f41d2585a71e | -4.49964 | -45.72915 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 472d0120-2030-31ed-8be9-0724975196df | -3.52933 | -49.97928 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e39767a1-482a-31dd-b9e9-dfcc3e19371d | -4.11192 | -48.49933 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7458188-0b67-3fc5-923e-7f0370d73bdc | -2.8788 | -49.37078 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b58d67bb-743e-3593-83d1-0812e0bfdb14 | -1.34611 | -54.63126 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 55ebae70-fcc1-3234-a831-6a9dfb88a454 | -3.19511 | -48.65956 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 277f155f-6606-3abb-8bd0-e4e1afec02a2 | -1.5294 | -52.20433 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d21052a5-1827-3c51-8800-07caae5d00d6 | -3.8615 | -46.44159 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bb632b2-55db-3995-a79e-da9ff8ea6b21 | -2.2355 | -53.78564 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d26170e3-4645-356b-b0a3-e5ce55a6a797 | -3.34215 | -44.97385 | 2024-11-10 04:14:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a40c95a9-03b6-3d0d-857e-e6707fd16262 | -1.21881 | -51.75557 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97e8b923-e08d-33a0-8e2d-d6f49a5f42c3 | -2.19776 | -48.37077 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5c2573c-ef9d-3a46-8d45-040daf0281dc | -5.04743 | -46.08677 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96e759b4-953c-3d34-b3f6-9844bd3698d1 | -2.92811 | -51.47976 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| dac58051-e78c-3651-9665-cde0d07dd903 | -3.09293 | -49.4146 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84ecc01e-37f0-33c1-ad38-35047cb3d388 | -3.34733 | -50.13536 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bcc96a4b-87d9-34f1-9e29-6449996fabf2 | -2.21261 | -47.73628 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 89d2d59a-c567-3887-a215-6781adf92432 | -3.76807 | -50.38254 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cca79053-0d31-32e5-9a93-707b0ff04b57 | -5.17609 | -47.61228 | 2024-11-10 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65f6449e-7cdc-39b4-8ab1-f3721262c028 | -2.09232 | -46.51435 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3389ca-fdc5-30e9-8f75-eecdaf36e1c9 | -5.2701 | -37.94974 | 2024-11-10 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd17651f-0dfe-3561-801c-07b294b3872f | -5.47337 | -41.64421 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67372d5d-db13-3518-a21f-a50ebcd1b777 | -4.10142 | -49.10771 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 53f4f02a-61b0-3c70-bd84-b315d5435836 | -3.12408 | -45.96046 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a77f33-fbd2-394c-9d68-ca1a3b041c46 | -1.75692 | -55.03904 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30b9350c-9d22-32f9-975f-90feef1a739b | -5.56965 | -43.97549 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4039aae1-8b28-3a9f-9197-cba50cadac17 | -2.45852 | -50.25446 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae637a91-2f48-35ff-949a-320dc32cba36 | -3.1013 | -49.42076 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 294751a5-775b-38a9-ac98-c0eec382d987 | -1.05495 | -47.89721 | 2024-11-10 04:14:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db8283f9-f64a-37d3-a368-38f049a6048b | -2.54287 | -46.31518 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79553026-e630-3f95-95b7-1ba2c2bc3252 | -3.03808 | -50.35116 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb8fc6dc-1ac1-3cc6-9c41-f5a52427bc32 | -1.13393 | -54.21197 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d517b470-3bdd-3dce-884c-73fb976d3513 | -4.60675 | -45.97139 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 94fd02b7-9c87-318c-9f5b-3f99000b1b5e | -4.43578 | -44.62622 | 2024-11-10 04:14:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| aef57b59-352b-39b1-8636-d889e5819bc5 | -4.09746 | -48.31896 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6175aa6f-4cee-30e7-9852-007d1d5aff5a | -2.92178 | -51.6732 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9969258-f33a-3fe0-948b-595f30027647 | -2.90856 | -51.46664 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee8a8706-a975-35fe-92b8-a4dfc0e6caf8 | -4.28815 | -48.19308 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0661233-4b3f-38df-a97e-6b8857a769db | -3.1891 | -50.44233 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0546cff1-0f70-3418-bee2-9e07d0106b89 | -2.15617 | -46.69818 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9facaa68-ac97-3f49-8ddf-24ad0f72cf43 | -3.95634 | -48.12557 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 43135c15-a1b4-3b36-8365-aa3bd56131a8 | -2.86935 | -47.91213 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb67ec63-c58f-3a24-9496-abbe5d28841d | -3.20092 | -46.4962 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a260ce-1274-37ae-8f1d-e84849b2d402 | -2.59185 | -46.17516 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51a1f5c7-a984-36ec-afd6-2b32b8d5e15d | -2.76773 | -49.35921 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7b87272e-29a5-3937-9ec2-87a1012c8db2 | -4.54315 | -44.63522 | 2024-11-10 04:14:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 604c7b69-117d-3a2d-8c74-ad20fa8767f8 | -1.16998 | -52.09305 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ae5a515b-96ce-3c86-b46a-9fa4809d0ab9 | -2.36835 | -46.8563 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc93b6c-ae5e-3cbf-963d-3f7362072a0a | -3.2438 | -50.58294 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e8e583a3-06f5-3ec0-a0a8-54fecbd47173 | -5.24158 | -48.16201 | 2024-11-10 04:14:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7b2c473-b93f-3954-aa18-678441409481 | -2.32159 | -46.48758 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4789ccc5-432f-3db2-b7e2-2e0a4d7aaef2 | -2.87568 | -51.30371 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ba0907-cafb-34bb-8817-e21e259dc6df | -3.13506 | -45.96219 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4192b94d-d2d4-3768-b693-10978142f324 | -5.32592 | -45.05707 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 78c37a70-d9f2-308f-a6e3-2bbe93bed109 | -4.20838 | -48.54651 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be375b97-d1d2-3c60-9713-67d57c9096d5 | -1.42822 | -52.27249 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 946b6919-0e44-3bca-9bb3-a732a00f6cd2 | -3.22018 | -50.39263 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9aab7cc-4be6-3ce8-8b34-29e91cad00fe | -4.18493 | -46.57967 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a33dda53-5287-3629-86a3-c98d4e8bb736 | -0.30481 | -51.70885 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38f23419-6b36-3a4c-afa6-bca257889419 | -1.94523 | -46.41135 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd1fd49d-2f75-3283-88db-78edac1ba758 | -2.59354 | -48.31438 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d32e2856-5798-3b74-98ee-76b925b173d2 | -2.13942 | -50.70022 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77091df7-421f-3171-a346-73bfcad25e7c | -2.94607 | -48.60107 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a96e3aff-eb26-3b0d-acd6-745f5fa1ac58 | -4.07391 | -46.07215 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 62e17cd4-4d0e-3013-8083-c0564243bd54 | -5.86875 | -43.02199 | 2024-11-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8fc56a38-1ba8-3a3a-b72d-708f74cf1ecf | -3.36356 | -53.40835 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14c2faa1-50ef-36d0-a71d-95903ddf1d5a | -3.08786 | -51.22451 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1362e6d6-9b99-3950-8fa4-7d448ab76814 | -0.04094 | -50.7798 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c180666c-0276-3af2-94e3-a2fc16526fe9 | -4.91194 | -43.98322 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c906542-90dd-3ebe-9b28-7a3c9d12cb7f | -3.81104 | -44.46893 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35b50178-b39e-34fd-9aed-ba2ddf485d35 | -4.10054 | -48.97342 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a5bb9d7a-97d0-355d-be3b-3dfb97c3fff8 | -2.28661 | -46.51097 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b6f98dd-bbfd-3324-8fd6-c06f0a6ccdd3 | -0.45106 | -52.03532 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd7cc387-4057-3b18-8b42-d6aa9168a397 | -6.10357 | -44.75642 | 2024-11-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d402691c-c9ca-3891-bf79-8bb2a11068f9 | -2.33599 | -48.51851 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8060ae8e-b20b-3787-9c6e-0f7cb78a4c37 | -3.05537 | -51.06763 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a73d6abc-b370-32e4-b7fb-8924ef766542 | -2.69772 | -51.69099 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2999b78e-e778-3263-8df2-b5ffe1855791 | -3.69137 | -45.81431 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0dcc42a-059f-3800-9385-7f11c734a676 | -2.92226 | -49.36323 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a9564011-d695-3b74-a4b0-84598b5284bd | -3.94824 | -46.41233 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47f1162d-b1cd-32eb-b5d1-25e1be9704a0 | -2.10704 | -45.33207 | 2024-11-10 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27d77556-350e-346b-ae14-860d9f0194ca | -3.34874 | -54.12834 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 783c8277-e8be-318e-8efd-9d4aa53bf5ac | -4.08977 | -42.93242 | 2024-11-10 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f89897a-b7d9-3570-9583-17f691a9459f | -2.62736 | -49.47297 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab51d652-ee1c-339a-9352-a6cc6b72593c | -2.58034 | -51.88159 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42aae8fa-02d4-3972-9cc7-6010d7f2c06e | -2.58236 | -48.13768 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc3b5e7b-a0c2-3fea-be0c-a31c058b1629 | -2.61772 | -46.16812 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48799881-02cb-34bb-86ed-8594d967c792 | -2.45661 | -47.16503 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dd89273-ad20-3a55-be42-cccfb093cf28 | -4.68251 | -45.15078 | 2024-11-10 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ccdc0b-0d20-3287-a3bd-439f24c5ed6d | -2.58298 | -48.13379 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f50e37e7-b17f-3aaf-8471-564e1f5c352f | -2.79808 | -51.76836 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 550e6d4a-6f94-3ecb-bb20-d51cdbae729e | -4.09405 | -49.12587 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2faa4275-56ef-320c-a524-100df24391fa | -0.95233 | -52.44439 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4db5a08d-7751-3d2d-a1fc-a516acbea4ea | -3.95987 | -48.12988 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 39b89ff3-34bd-3d50-8455-731d46455dc5 | -3.2262 | -50.27573 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 7b98c13c-230d-3173-8834-ef1f78f1b8c3 | -5.84631 | -42.48749 | 2024-11-10 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4116df23-51d1-3f00-a024-5bce68bf2df1 | -3.23017 | -50.4371 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e3064a05-e6d1-3aca-9068-83543a38a7ef | -3.3569 | -53.41161 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bc4deab2-8c29-3c92-9cac-3a372d2e36b1 | -5.16895 | -50.68387 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README46.md)
