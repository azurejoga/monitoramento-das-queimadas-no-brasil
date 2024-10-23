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
| d8c964e8-68ef-39c4-83cb-981aab0ee7c2 | -4.18782 | -47.95211 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9a136b1-eab8-3fab-b121-fd1bad5df5e4 | -2.47387 | -49.1214 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b6b79b1-d239-3f7b-87cc-14d2cd258524 | -2.47333 | -49.10918 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee27aed1-aa43-360e-b960-da20bdb5fd22 | -2.46893 | -49.10045 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f5c926b-c391-3eec-a8db-1e79767caf41 | -2.4683 | -49.10433 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d15516b-613b-3b34-9125-75eead941277 | -2.41812 | -50.37103 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d08ff30-5547-360d-bace-cb3117e83a9d | -2.39028 | -50.31332 | 2024-10-23 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7929c763-0ad3-3ef9-b59b-bd5d42b5806e | -2.3901 | -50.3128 | 2024-10-23 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5fcb844-848a-3fcc-a927-a16c86d78b77 | -2.38416 | -50.31224 | 2024-10-23 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01bf45a4-3151-3a7b-95c5-72f25840b29f | -2.38398 | -50.31175 | 2024-10-23 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 821479fb-3652-30c5-96d8-a79be37f4ae8 | -4.42125 | -49.80526 | 2024-10-23 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0769fa56-50f9-3ae2-a9aa-ed97f88f2f32 | -4.42125 | -49.76573 | 2024-10-23 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2447aa40-4069-33a6-81ec-a164d523a6ca | -4.41554 | -49.76456 | 2024-10-23 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44cae9f3-7fac-398d-959f-cf026ac45b5a | -4.38618 | -49.76358 | 2024-10-23 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e1ff8b1-9a7e-3dd2-92c1-b789551cb479 | -4.38115 | -49.75843 | 2024-10-23 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc06b2df-2354-3f57-a71e-d27103017e6e | -4.38045 | -49.76253 | 2024-10-23 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b2906f59-9708-33fa-9008-f10356d90d54 | -4.37795 | -49.41718 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb659541-cd2f-30e7-940c-ec7477c32da3 | -4.37732 | -49.42093 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f774c757-6204-34d7-8c97-4795016c18db | -4.37584 | -49.41713 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e70cd3ed-2fbc-3706-8039-c941ccfa9aef | -4.19242 | -49.40086 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d937f02-6a3b-3468-8068-d08a06eca901 | -4.19177 | -49.40462 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fface732-d17b-30ea-951e-474fa8d0c10a | -3.79774 | -50.03272 | 2024-10-23 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adf5d667-4506-377f-90da-eef1d2ac0803 | 0.98484 | -51.15625 | 2024-10-23 03:57:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f39e806-cef1-3a7e-8c80-16cf6d3539dc | 0.97903 | -51.16358 | 2024-10-23 03:57:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78518fd8-596b-30a3-95a8-33004527d528 | 0.97809 | -51.15746 | 2024-10-23 03:57:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68716077-e752-3044-a924-4a0a508ab2ac | -3.23758 | -50.85 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de8db3d7-360f-35eb-9e37-82b04340309c | -3.23674 | -50.85499 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6133f718-2852-3157-ac9e-575c762ac74c | -2.46732 | -51.97162 | 2024-10-23 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2859f6a-4200-3f0f-be7f-5123d3119d2d | -2.46628 | -51.97772 | 2024-10-23 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b4cb43d-487e-3716-aac8-1cce9013d17f | -2.46468 | -51.97541 | 2024-10-23 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3dd92aa3-cb26-3e19-b512-8c8d692db008 | -2.41196 | -50.4833 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7f04b76-cdfd-3eab-83f4-c644ad6a8fe0 | -2.41115 | -50.48812 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4029b355-309a-3f2b-9ad4-d8e2ed3bfdb1 | -0.11922 | -51.64564 | 2024-10-23 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 593def7a-e2aa-388d-a38c-a113e0388d49 | -0.11823 | -51.6519 | 2024-10-23 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 62a53549-fd84-3b49-b918-80d6d87be678 | -1.39227 | -51.99916 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d90eebf1-4d14-3465-81ac-99dac81c1487 | -1.39139 | -52.0037 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ad026e9b-3c34-32ee-b0e7-48e87ab7a871 | -1.39119 | -52.0056 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7f64f443-5fbc-39c7-93f9-38ec82dfadcf | -1.39037 | -52.01006 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c4f54211-4e0a-311a-bf03-711d5853a9fa | -1.38553 | -51.99615 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 030ef7a4-c500-3861-8663-da11f1d51656 | -1.38537 | -51.99809 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 47ef225c-6596-3cec-9926-f0997d115075 | -1.38451 | -52.00251 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 87eac664-156c-3c2c-a4d1-3fe6a4f63e6f | -1.38431 | -52.00443 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 285f2ac9-fad1-32dc-a4c9-3123328400ff | -1.37865 | -51.99495 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c26d459b-2be6-3144-8009-8e58bfc33640 | -1.37849 | -51.99691 | 2024-10-23 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e48e675-865c-3cb1-8a08-097ea536e010 | -3.78561 | -52.3919 | 2024-10-23 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f8fec15-7259-3c41-b2ae-b10b4bd82da0 | -6.48058 | -35.23866 | 2024-10-23 03:57:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9de9ddc5-0741-3125-bbfd-6bbe36dfead3 | -6.17236 | -35.29044 | 2024-10-23 03:57:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d8b9545f-5ab2-3f67-ae61-d7ed2a1f098c | -5.89927 | -35.43073 | 2024-10-23 03:57:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05720944-8e0f-3a98-9436-31c4ed2c369b | -6.50593 | -35.25813 | 2024-10-23 03:57:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d0fbc33f-49dc-3a0c-8389-1cae74187bd5 | -6.48452 | -35.23932 | 2024-10-23 03:57:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9238dbe-540c-3218-a017-8846ad54a304 | -4.96623 | -37.92715 | 2024-10-23 03:57:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 31969a85-8971-34e1-9f0f-95690f2db6ed | -4.9481 | -37.42806 | 2024-10-23 03:57:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c57b4485-ea2d-33b8-956d-b83dc58380c4 | -5.13386 | -37.97144 | 2024-10-23 03:57:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8c615990-5e01-35c5-b40e-da9524723478 | -3.32435 | -39.69897 | 2024-10-23 03:57:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e41a2f25-b81f-353a-908a-443d1291ccf0 | -5.02032 | -38.91658 | 2024-10-23 03:57:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ce0d0b8-d294-375a-b4dc-fdd10d349cb2 | -3.71585 | -39.1335 | 2024-10-23 03:57:00 | NOAA-20 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ddb2c1b2-541f-35cf-8372-6fb1e226b38a | -5.75134 | -39.78136 | 2024-10-23 03:57:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 09036689-c8a8-3ce0-9a39-bb4f34c17a16 | -5.74858 | -39.7774 | 2024-10-23 03:57:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 12e61a11-081a-36cc-b1ce-8c8ad9013392 | -5.74804 | -39.78085 | 2024-10-23 03:57:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2de0fef4-de56-301d-a57f-232382f70c57 | -3.44924 | -41.26149 | 2024-10-23 03:57:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc0d71d0-7462-3f52-89e4-7482250a1a80 | -3.44643 | -41.25719 | 2024-10-23 03:57:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6381fd3f-5a29-377c-8b0a-a297be1edece | -3.4446 | -41.26854 | 2024-10-23 03:57:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bcfe9274-9817-39ad-a283-6ec3697a323f | -3.44117 | -41.26801 | 2024-10-23 03:57:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c28d038-df5d-3409-ad56-91b287b0bf29 | -3.024 | -40.20331 | 2024-10-23 03:57:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7eb04c08-3d05-37d1-8fa6-db3718b7e3c8 | -2.94637 | -40.49892 | 2024-10-23 03:57:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e30f743-9308-34c7-a6f1-330593309053 | -3.86335 | -40.90893 | 2024-10-23 03:57:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf032794-80c0-32bc-8238-5d06e10950cc | -3.85275 | -40.70269 | 2024-10-23 03:57:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e11f77dc-a0bc-363a-a62d-0da382efee9c | -5.46745 | -40.39523 | 2024-10-23 03:57:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0f2ce3f7-5dc0-3998-ba79-7b2c50329e72 | -5.33564 | -41.52844 | 2024-10-23 03:57:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20b0526c-5110-324c-ab33-54e488156842 | -5.32883 | -41.52733 | 2024-10-23 03:57:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e9ef6f0d-d404-357f-aea0-830ecc3fd253 | -5.26918 | -41.19603 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 64a0ceb8-ed79-3219-a8ab-64a22e898368 | -5.26581 | -41.19549 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 626e8acf-f89b-3901-9b74-64ffddcc6b04 | -5.26244 | -41.19495 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eddce7fa-f0db-3f7e-88b2-92b74d322202 | -5.26022 | -41.18718 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7fa854a4-310a-3d45-9dea-b8daa751296b | -5.25964 | -41.1908 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e597f289-8e3e-39e5-b50f-ec251f0f2df5 | -5.25578 | -41.17165 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8676aee3-b78c-32cc-a4ab-64c793e81824 | -5.2552 | -41.17527 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d1a9205-4147-33cb-b34c-089d1e92b6d2 | -5.25462 | -41.17889 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc7250d9-2fd7-368b-8cf3-9f91af84da73 | -5.25405 | -41.18251 | 2024-10-23 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aab04ee6-66a9-3850-adf9-3bbbfcfce3dc | -5.24432 | -40.60284 | 2024-10-23 03:57:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 521629a8-10f0-3eef-9d83-b46c0fcabbb3 | -3.40136 | -42.71584 | 2024-10-23 03:57:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2698a781-6ded-3cc5-82d4-e2aa63c316e0 | -4.31424 | -43.02461 | 2024-10-23 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 610125c1-44bf-3210-a954-b74c8c24094f | -4.12632 | -43.0072 | 2024-10-23 03:57:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce8c928a-f5af-3ace-af92-badcfb0e412a | -4.12562 | -43.0116 | 2024-10-23 03:57:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ee724a9-edc1-3891-8eba-fa792f7a42b6 | -4.11825 | -43.01036 | 2024-10-23 03:57:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b7e51d5-b96f-3a40-931a-06473d791697 | -4.91767 | -41.9717 | 2024-10-23 03:57:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b343f2f5-b23c-3557-85b5-4970a06fe2f3 | -4.91706 | -41.97555 | 2024-10-23 03:57:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45c3a788-10c0-318a-a4f2-f414d067bd24 | -4.86162 | -42.05369 | 2024-10-23 03:57:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a81392a3-af68-332d-ab6c-ce2aa1870391 | -4.72088 | -42.66023 | 2024-10-23 03:57:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e9978f54-b8ac-34f5-a278-b8164d3e3ad6 | -4.72022 | -42.66436 | 2024-10-23 03:57:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c97f924-8028-320b-8c94-df975d1669fc | -4.71171 | -42.67149 | 2024-10-23 03:57:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c88e6954-66b2-323f-bf96-585766e0b8e2 | -4.62014 | -42.3815 | 2024-10-23 03:57:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f0bcb94-500d-359f-8002-f61f594647cb | -4.32192 | -42.29947 | 2024-10-23 03:57:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a48d0a70-f3be-3aa1-b500-eaeb5673a884 | -3.8031 | -42.54832 | 2024-10-23 03:57:00 | NOAA-20 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97301aef-c77c-3247-a88b-7c540c6f1578 | -3.71781 | -41.68612 | 2024-10-23 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d874cf37-43a7-3677-837a-1d14f17c9a45 | -3.71434 | -41.68555 | 2024-10-23 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 24319d52-e8a4-328b-ba4c-1112adf3b8f0 | -3.61723 | -42.44501 | 2024-10-23 03:57:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 65d14730-4747-3f23-bd98-fdbfd07c3405 | -5.53416 | -42.21705 | 2024-10-23 03:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 994e98bf-29ef-376c-99f3-4cc9538b29ab | -5.53354 | -42.2209 | 2024-10-23 03:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d1a1a246-649d-391f-b658-e256090351e6 | -5.53068 | -42.21644 | 2024-10-23 03:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
