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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf776d92-1b43-356c-bec0-0a8e8cf43273 | -2.8041 | -51.483299 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6776d44-a845-3e2c-a07d-8fe197539e2e | -2.4363 | -53.9258 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a998f5e-1ece-34e1-b572-c13191d5cdb4 | -3.2421 | -53.390701 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db17cdf-34a5-374e-b6d8-98def6958afc | -3.6595 | -50.230202 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f541f09-b786-3787-aa2b-089b52bdff45 | -2.8025 | -51.4762 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9a6300e-6bca-3bcf-8861-9a5006d8c00a | -3.0475 | -53.2612 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab4decf-5195-3a1e-b724-fb2db8c47d11 | -2.8426 | -49.467602 | 2024-11-06 00:54:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb3d2767-83e6-3d2a-b251-640a7a622e97 | -3.3217 | -51.624599 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e98cc1a5-922a-3096-97dc-d0931caa2792 | -2.7959 | -51.4925 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9eada8b-873b-371d-b2db-019a702c230b | -0.8556 | -52.834999 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d53697af-fe9a-3726-99f0-c5172dbf40d5 | -1.2946 | -54.659698 | 2024-11-06 00:54:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5cc7e5a-dbb1-3777-b347-0d8355cbe9fe | -3.7351 | -53.382198 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3bb73ec-8e90-326f-822e-c835b8fc7c2e | -2.8661 | -45.629398 | 2024-11-06 00:54:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 940ff74d-78f2-3c6d-bc67-e1551daf4236 | 1.2085 | -50.758801 | 2024-11-06 00:54:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f68d5f42-4ede-3d26-aff5-bf0fa36fb559 | -2.8309 | -52.901199 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f47c75-2bc1-35bb-9145-fae0510ed235 | -9.8867 | -42.0783 | 2024-11-06 00:54:00 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 87390807-286c-3a9d-bb8b-d4c492930bd3 | -3.9704 | -48.163399 | 2024-11-06 00:54:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbbcec60-4ceb-367d-a042-8b10cbecab41 | 2.2799 | -50.757702 | 2024-11-06 00:54:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1f467eca-77aa-3b2c-9321-21dc1ecde7eb | -3.2308 | -50.3834 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aae2c40-7c3a-3382-ab11-2ae4b7a0d444 | -2.8506 | -51.774399 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 962af65d-ddde-33a0-a395-e3aefdfbb509 | -4.2352 | -48.543598 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb16ffc3-a056-33c6-82d2-4a46f45539fe | -2.8591 | -45.600201 | 2024-11-06 00:54:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2ffc170-7b37-3281-8db6-eb1d24c434de | -3.4917 | -52.094299 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e5e523-3885-33f0-aa2d-2045e9f7e585 | -3.0571 | -52.493099 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5e43aad-05bb-3502-b2ae-fd68a5578c12 | -3.1736 | -51.251202 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b42b08fc-6e48-32f7-94ee-5218109ab1be | -3.3368 | -50.084999 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e450abf4-33c2-38fc-a453-700777b78ee2 | -2.4012 | -46.181499 | 2024-11-06 00:54:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d473179-36e9-3c34-bdb4-9de05ad82b57 | -3.0117 | -53.420399 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b213be49-8b99-3986-b3d4-4dca0e96b5f5 | 0.1901 | -51.065498 | 2024-11-06 00:54:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8749c31e-8d84-3da4-b39f-dcffeae59fb3 | -6.0966 | -43.947399 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 092a27d6-3227-3f2c-953a-0b3d3b770d65 | -2.9327 | -51.0569 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e98f3c8-ddf5-3539-a500-3e495d1d81d1 | -2.9213 | -51.051899 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78219210-7f03-361e-9f91-da150175c195 | -2.8626 | -45.614799 | 2024-11-06 00:54:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0c82de0-768d-3946-94c8-e8f9c08507fc | -3.0347 | -54.198502 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0c1c17-4e67-30d8-a9ce-e1ff78d08f58 | -3.0102 | -53.2337 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 095e383d-abf3-31cb-acc0-52a6cd6627ec | -3.1177 | -51.098499 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34516a5b-01d2-3ced-9254-4fd70bf91cb0 | -2.8222 | -52.9533 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11b172bf-4294-3d3c-a510-f9dbaefa4047 | -3.1769 | -51.2654 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a130f37c-d681-375b-bec0-697c6768edfb | -4.1193 | -43.589401 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62385ad8-019f-3562-b99d-564952a169e3 | -2.8392 | -52.8922 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff0db45-5d39-3212-aadb-8e49070c056f | 0.2097 | -51.069901 | 2024-11-06 00:54:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cba048eb-1441-377b-a311-91a2f60b2c47 | -2.0375 | -53.579899 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20388765-02ad-3d44-9781-25bf295a2bb8 | -3.3019 | -53.111198 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf937fb0-3858-30af-9de9-7edb46015fe2 | -2.8274 | -52.930698 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703b8dec-4f34-3908-81dd-8dd6c7af3379 | -2.074 | -47.061401 | 2024-11-06 00:54:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40ebfd6c-c0b3-306b-8795-c2250aa56257 | -3.1686 | -53.069199 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037befec-7dcd-3b8c-bd21-1289bc56ea75 | -2.862 | -51.779202 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40cdc91e-2c35-39d3-814e-4da7f1a88f9d | -23.930401 | -54.063 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 736a0b1a-8baa-305d-b5cb-67f2c52ee6e0 | -2.3948 | -46.1544 | 2024-11-06 00:54:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5dceeb08-1d9f-3da5-be08-5a78c576cf61 | -4.218 | -50.636299 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de8443d6-a909-3ebc-a480-b94ac439bfc9 | -9.6085 | -49.535 | 2024-11-06 00:54:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c433b80a-ac4e-3f19-aeb1-ce1ce2377d7f | -2.1784 | -53.699902 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ed7dc5-6d60-3b21-8a6b-325c5fcc7a8a | -2.832 | -52.951099 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d50244e-4ce9-3b2a-b353-b56a108cd006 | -3.0086 | -53.226799 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e233bd38-ba07-3475-b46f-f1417f2fd191 | -2.9556 | -54.801399 | 2024-11-06 00:54:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6100e748-cc88-3ca2-a7f9-d18dc4c268d5 | -3.0263 | -53.258801 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a64d05c-fff8-3beb-bcae-b58caf1dcf3d | -3.2085 | -49.223701 | 2024-11-06 00:54:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab1ffda-5861-3a61-9476-f92583a4eaeb | 3.6129 | -51.326302 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e587d838-d053-3200-ae9e-e3cb68d27ee2 | -2.7392 | -54.123001 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d961758-4338-3938-be81-16af1d5e207d | -3.7591 | -48.887798 | 2024-11-06 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c318b45b-15d5-3bf0-9d71-4886a6ab0283 | -6.5103 | -44.666599 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a8cbf58-c09b-3731-ade0-7530c5a2edfa | -6.4848 | -44.688499 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26a27602-a1a3-35c3-a74d-ac4bb93c9ce6 | -4.263 | -53.526901 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a169ac3a-217a-3f44-b513-363c60075c9a | -2.8093 | -52.941898 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d87c0a80-aea4-38b4-a496-b7540cc87bf3 | -23.940201 | -54.061001 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 630823a6-40d6-3304-b332-d99555ef66bf | -2.8144 | -52.919201 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd45795e-2b74-38e2-aa0a-366788f5a81c | -2.8357 | -51.799702 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 602ee5e0-90ef-3442-bf82-d61fd519a525 | -2.9409 | -51.047501 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2998eeec-0767-3ff5-9c7e-46de82a58c95 | -3.7147 | -41.6898 | 2024-11-06 00:54:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb7c72c4-6c40-39f1-b26c-66322a5a1e70 | -3.0587 | -52.499901 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0282a53d-ccbd-3690-9de0-089d75b3bc3a | -3.2156 | -53.094601 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89f9f4e0-d1af-3307-bf2e-4a6b1eb628a4 | -4.6895 | -45.6451 | 2024-11-06 00:54:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3e1a572-3545-3014-be94-2dabff1e36f0 | -2.8325 | -52.908001 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bb3e9a8-b5b8-37c9-88ab-2c76ce6235b1 | -2.3899 | -50.315899 | 2024-11-06 00:54:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aba4d001-7ecf-3624-bd41-4e32624e721f | -2.1591 | -53.660801 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f6d78f-5fe8-3ee8-b8e6-d4b8b38fb3b2 | -3.2192 | -50.378101 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3fc4ac4-fce5-3c0e-a93c-7270c436a70c | -2.4785 | -53.974899 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7649bde-e56c-3bcf-9f7a-63037a365f93 | -4.4718 | -50.662998 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f30909f-fae3-35dc-8ef3-8ecd0854e664 | -6.9331 | -47.779301 | 2024-11-06 00:54:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8397752b-0018-3ed7-9c93-d9efdba19b03 | -6.4909 | -44.671299 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5baf4127-c6c0-350d-a487-483550b6310a | -3.2323 | -53.392899 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5b12dfd-85e1-3d2b-ae49-131e542d5ff0 | -2.9081 | -51.0397 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d50aa45-382b-32b1-b7c2-8a45b9cc1b6a | -3.2014 | -53.212601 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7ce8bbe-b296-314c-8935-3b59cf27073e | -4.0511 | -46.935799 | 2024-11-06 00:54:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0326984f-7911-3722-9804-9d1184eba491 | -4.2202 | -53.565701 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d57c00b-dc5e-3f08-81c0-da4f1e280148 | -2.8074 | -51.497299 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a428e352-e630-30e1-8c7e-82acb7f6d8e8 | -3.8757 | -52.374199 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c75feeab-9675-3cbd-a3e5-c7ce2ec5db45 | -23.9282 | -54.050301 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb2c3a4b-f5c3-38d5-8d0e-6907796156ac | -3.6549 | -50.255199 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176304ea-9c08-3615-afbd-7c858904fe74 | -2.18 | -53.706799 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb2475f-ae01-3cb8-a928-b1ea493b23ac | -3.7177 | -49.417 | 2024-11-06 00:54:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc70bdfb-c4a3-34be-a774-1e049a854095 | -3.0669 | -52.490898 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 069bf3da-e52b-38d0-afe4-c1be9114c581 | -2.9953 | -53.845299 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb1bf936-aec0-35a0-a66c-c6c62929bd2f | -3.4834 | -52.103298 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42b77a0b-482a-3c34-a711-c880a216099c | -3.1826 | -50.576199 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f81bcc0f-09c9-3526-9ed5-123031c95697 | -2.8373 | -51.806599 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29536e0a-f3b9-33a6-82c4-fded56a6121c | -3.121 | -51.1129 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 574a28a5-1f55-3f51-9399-83e8a7c62d32 | -4.094 | -50.502201 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1032fe4-de56-339d-a70e-78f5eb6cdf9d | -2.5839 | -51.8708 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 498f7ad8-f086-32b7-9c9c-d4a0b2ffeabf | -2.9937 | -53.838299 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
