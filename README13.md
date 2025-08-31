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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9861c510-6798-3242-af75-73c9e6f1cd4c | -6.1853 | -43.3257 | 2025-08-31 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| d27dedb6-da6f-339b-a439-fa9213d9724c | -11.8181 | -46.4314 | 2025-08-31 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 6955d0b1-bf7e-3062-b974-fb00ea5eecd8 | -11.3312 | -43.6399 | 2025-08-31 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 91f1fe7c-3645-3fc3-826d-44305a00ac0a | -11.3293 | -63.2681 | 2025-08-31 03:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f9b3fb3d-7c94-3527-8d4f-85e72a117770 | -7.1139 | -44.3111 | 2025-08-31 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8dd8d0a9-759d-3072-8d1b-566a2cca9d39 | -11.3106 | -63.2691 | 2025-08-31 03:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 763aabd2-009e-39fb-aba0-5198bb2dfd8e | -9.4683 | -62.3476 | 2025-08-31 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 600a52c7-1003-3b70-9601-2baf1a48f0ac | -11.8373 | -46.4287 | 2025-08-31 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 83f7d6e1-2d11-3259-9a29-ca88eb3c37cb | -8.744 | -62.379 | 2025-08-31 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b68e5dae-bfd6-34ed-974b-989f60d1288f | -9.4431 | -60.5884 | 2025-08-31 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| dc22b22c-aed5-343b-b8d0-18216e0a28e3 | -9.4432 | -60.5692 | 2025-08-31 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 1b9dcd9c-7f9a-304d-b5ab-c16a81a4d2b2 | -8.91642 | -40.43922 | 2025-08-31 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d5a8cc0-2266-3aa5-b413-48046eb2e6fd | -6.96963 | -40.94358 | 2025-08-31 03:10:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 859ff3e8-4eba-3f40-af85-0b3cfc06de51 | -9.58977 | -40.35289 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 09189434-4689-36cb-82f7-71af5c8c93a5 | -5.5309 | -36.84873 | 2025-08-31 03:10:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 947a5ce6-4b57-3385-9f94-707ef8e10bbc | -9.5876 | -40.36382 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 593af0d6-ff89-3882-a3af-2eb0a6fcadfc | -9.5888 | -40.35551 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dab43958-64a9-3e04-ab8f-f811fc53bfde | -6.96838 | -40.95024 | 2025-08-31 03:10:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48e33148-46ad-3c9d-933e-deaf7a36103f | -9.58869 | -40.35834 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0ec95e9e-9e4e-3d97-9f4b-67f66c06bfd1 | -8.91535 | -40.44487 | 2025-08-31 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b678596f-bafe-3daa-8e5d-3d35bf1dbf6b | -9.58776 | -40.36098 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6635957f-53a2-30e5-ad6e-679bf89e168e | -9.59419 | -40.36232 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f6739b6c-9b10-387b-a8c3-b6c3c05cdfad | -6.96767 | -40.94665 | 2025-08-31 03:10:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 077b91de-bbe5-3b80-bc71-40a7223870fb | -9.59523 | -40.35684 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3930741e-24f7-315f-a988-a283f69b5305 | -4.93845 | -37.36334 | 2025-08-31 03:10:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 952a65fd-5e39-350b-bbae-569a72c23c81 | -4.93915 | -37.35928 | 2025-08-31 03:10:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d07f0417-5116-3e55-ad18-9113e131d218 | -9.59512 | -40.35965 | 2025-08-31 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a705d629-8620-322d-b54b-701d76a917a0 | -5.5296 | -36.85607 | 2025-08-31 03:10:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d38bd8ff-2e9d-3ca2-a7d6-cf04fd9d5f31 | -5.53514 | -36.85706 | 2025-08-31 03:10:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b01b0684-d6eb-308d-9d28-bd192041808d | -5.53025 | -36.85241 | 2025-08-31 03:10:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2de94f73-2bc5-3f06-af01-1489382e33c6 | -5.53579 | -36.85338 | 2025-08-31 03:10:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 796cd323-4bc8-3a4d-b135-d8cbf08c585d | -15.49027 | -41.52486 | 2025-08-31 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7c9e47b5-43dd-34f6-b97c-2691e3bfd290 | -13.33318 | -43.20209 | 2025-08-31 03:13:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3c28d233-bc64-37d5-8568-d8bc185fd691 | -15.94292 | -41.41074 | 2025-08-31 03:13:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f8f8510f-3213-3dc5-bb2e-e1cf3ecdcb17 | -15.49431 | -41.51905 | 2025-08-31 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 74d90748-8433-3291-a75f-79f427406f5c | -11.83375 | -37.57115 | 2025-08-31 03:13:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c471ac35-0ea4-39d5-9479-f0cf706b4963 | -15.49142 | -41.51962 | 2025-08-31 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 01216559-41f4-365e-9041-fec9e50b0344 | -13.32611 | -43.20042 | 2025-08-31 03:13:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60cac4b0-f79e-35e1-bbfd-d8325af86156 | -15.94205 | -41.40972 | 2025-08-31 03:13:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 021041c4-1e78-35b0-b68d-4e27fcb97711 | -15.49321 | -41.52423 | 2025-08-31 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7a0540bd-4578-373d-85a7-17ef9f946075 | -11.83418 | -37.57087 | 2025-08-31 03:13:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3cfb3b7f-bac1-34c6-abcf-e9ad16e29da0 | -15.49754 | -41.52147 | 2025-08-31 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7fb53836-da44-37ba-b202-a8001009d93e | -15.94817 | -41.4111 | 2025-08-31 03:13:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76f7ffa6-3890-3e65-905f-76425388bc23 | -15.67131 | -43.23354 | 2025-08-31 03:13:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 44f4aa3d-995d-330d-a8cd-bf86cddbaf24 | -15.67798 | -43.23579 | 2025-08-31 03:13:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ecb29d4-ab21-3d52-84e8-68e32a5113e4 | -15.67279 | -43.22702 | 2025-08-31 03:13:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 15615d70-ee25-3432-b403-3a6e6ec59505 | -19.51228 | -40.70144 | 2025-08-31 03:15:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3c6b252-b6d1-33dc-add0-871db373122b | -17.7361 | -39.52971 | 2025-08-31 03:15:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1d1a6dbd-85c7-367b-ad40-3c2356494b50 | -17.73341 | -39.52452 | 2025-08-31 03:15:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 814d76a1-e5dd-3ab0-b007-203a3f20946a | -22.21236 | -45.87449 | 2025-08-31 03:15:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 00cf6b35-1d69-3c13-a3f0-e82007fb9fb8 | -19.51144 | -40.70528 | 2025-08-31 03:15:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 40924a08-22d3-30c3-a5d9-662aea94bfca | -17.7327 | -39.52797 | 2025-08-31 03:15:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8381894-fd0a-3f67-a16a-e071dcd5af60 | -17.73798 | -39.52922 | 2025-08-31 03:15:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd40cd3b-d027-37c9-a0c0-38dfd8ecb0e1 | -17.73683 | -39.52626 | 2025-08-31 03:15:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4ad67bbc-7293-339e-ab88-a307e9f781cc | -18.55098 | -40.05587 | 2025-08-31 03:15:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c59270ce-67a9-3fe5-8dbc-d649e01f7d83 | -18.55021 | -40.05946 | 2025-08-31 03:15:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f662f777-c064-3789-b5e0-941cc093a221 | -9.4684 | -62.3286 | 2025-08-31 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 67dee079-2ca5-3087-8fb5-4be5157b0ac8 | -9.4498 | -62.3294 | 2025-08-31 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 122ea6ba-a207-3307-89cb-464baa9d5dd8 | -7.0951 | -44.3128 | 2025-08-31 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f2ce4d20-70f6-3ff7-be4a-e04e8352a130 | -8.7439 | -62.3979 | 2025-08-31 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9ed033df-1366-340a-bb19-94fa4a252c9b | -9.4683 | -62.3476 | 2025-08-31 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 813ea005-8803-37f5-a461-8a35cf305ae7 | -10.7567 | -59.8175 | 2025-08-31 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 4cbf6ec4-82df-3e2d-a740-b8483e832196 | -11.8177 | -46.4541 | 2025-08-31 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e85b4ed5-f6fa-378b-8933-3f6064842e86 | -9.0613 | -65.4542 | 2025-08-31 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 856eaa4e-3f41-3c8b-9c2d-7426b1128dfa | -11.8181 | -46.4314 | 2025-08-31 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d28ff088-6a55-3f28-9b19-a6e7a389de34 | -6.1665 | -43.3273 | 2025-08-31 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a34d3438-d788-3c62-b54f-95c71916470e | -9.4495 | -62.3675 | 2025-08-31 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a6c166a0-ca3c-320f-a324-b8a1f6c96c7b | -9.4497 | -62.3485 | 2025-08-31 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 247.7 |
| 85376ddc-8627-3ae4-ad03-0e4f92a64d05 | -12.0976 | -44.717 | 2025-08-31 03:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2b1c8d98-326e-3306-bee4-24d795b51046 | -16.2221 | -52.6778 | 2025-08-31 03:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 910e3bea-56a4-35e5-ad73-f857b3635a26 | -9.4432 | -60.5692 | 2025-08-31 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 3b0ae4a3-4e7b-3a72-b2d6-42e9a3d3b7ea | -9.0614 | -65.4355 | 2025-08-31 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 606b6565-2d41-316d-a33b-3ef7082497b7 | -9.4681 | -62.3667 | 2025-08-31 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b38512ae-c03b-3e51-8457-3a8bdd1a1a81 | -16.2217 | -52.6992 | 2025-08-31 03:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 99b6422b-3b00-3535-9a81-527eaa0e5d12 | -9.4431 | -60.5884 | 2025-08-31 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6708f3de-ed5e-3a4d-a03f-06e37d4b0e9b | -9.4498 | -62.3294 | 2025-08-31 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3115c4ba-2df0-3b09-b65a-66999fb7a1e8 | -16.2221 | -52.6778 | 2025-08-31 03:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| dc8af6de-4d2e-3116-b030-505f8ddc376e | -8.7439 | -62.3979 | 2025-08-31 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cb0ef847-0ad3-3d4d-ad4b-914c3f48b39d | -9.4431 | -60.5884 | 2025-08-31 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 443c1010-69cb-35a4-a26e-3bb5d5821359 | -6.1853 | -43.3257 | 2025-08-31 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 530e2d3e-13df-3382-92bf-967cd6968346 | -9.4681 | -62.3667 | 2025-08-31 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| eab2159f-a3f6-32ed-851a-cb4583ec760d | -9.0613 | -65.4542 | 2025-08-31 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| eea3dafb-8bb0-38c4-b780-632e10faa75d | -6.1665 | -43.3273 | 2025-08-31 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1bd9498e-c971-3627-a160-a9e90327d50c | -8.6538 | -61.9647 | 2025-08-31 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d7f5cffa-24b5-3a95-bf37-d3ec1147f611 | -9.4683 | -62.3476 | 2025-08-31 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 8d59bd21-ab4e-33ab-b942-28ebfed6362a | -8.6539 | -61.9457 | 2025-08-31 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| cbea29cc-8abe-3219-9178-2f8489e3f884 | -9.4432 | -60.5692 | 2025-08-31 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 867fdff4-c9d2-3b52-813f-09f17707b653 | -7.0951 | -44.3128 | 2025-08-31 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 12def667-111c-3dce-bde5-a263dda9407d | -9.4497 | -62.3485 | 2025-08-31 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 133.8 |
| af069660-4f06-3792-9c8e-ee56895749d8 | -9.4495 | -62.3675 | 2025-08-31 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8a2b1f13-a5b7-3d13-a9cc-5e8db2d7fa84 | -16.2217 | -52.6992 | 2025-08-31 03:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 2079834f-cb52-34e6-a1c3-601c6f82d94b | -9.4684 | -62.3286 | 2025-08-31 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0ac9ec4e-1e31-33f8-af6e-ed6b412e0277 | -9.4432 | -60.5692 | 2025-08-31 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5c8ae5cd-eece-3b52-b9ec-0c1380fb6ad9 | -9.0799 | -65.4536 | 2025-08-31 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 71e67941-5b03-36ac-89c5-206525fac0b4 | -16.2221 | -52.6778 | 2025-08-31 03:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b216b8bc-d175-32ac-a33b-5082910b014f | -8.7439 | -62.3979 | 2025-08-31 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d7bf8085-715d-33f8-b699-6be929afa6c9 | -6.7093 | -51.4165 | 2025-08-31 03:40:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7f119ff3-e941-30eb-b7a7-366fd75a25e7 | -16.2217 | -52.6992 | 2025-08-31 03:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| dec9e85c-bf51-3963-b295-b726efcea4bb | -6.1665 | -43.3273 | 2025-08-31 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 495c2be4-1e40-3cbb-8a0e-56b95a81e65b | -6.1853 | -43.3257 | 2025-08-31 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |


[Clique aqui para ver as próximas entradas](README14.md)
