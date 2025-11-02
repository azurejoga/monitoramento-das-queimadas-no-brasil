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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9deff501-c0e6-3371-9718-2a149ea15dd7 | -2.57107 | -54.00945 | 2025-11-02 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4e40250-c0fb-3f2a-b3df-5c0e5413ab67 | -3.52027 | -50.32548 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20b7b536-b006-3d99-b8ef-fc900d0c24fc | -3.77583 | -51.34423 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86b17cb1-89ad-3f2e-8dec-16da51e9ced7 | -1.43892 | -55.28561 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ef211e5-f9bb-35f9-ad74-6ff330b774b7 | -1.49129 | -55.34009 | 2025-11-02 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cdc331c-8271-3ca0-b324-b88ab573335b | -3.13214 | -49.23885 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f70a67-500b-3f5a-bb20-e2a745a95403 | -3.2535 | -52.90756 | 2025-11-02 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56cc9fd2-d9c9-3d80-95b9-93009b537031 | -3.93136 | -49.96471 | 2025-11-02 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f57d4af6-430c-3e5d-a4ee-fa24fcfb8867 | -3.15759 | -50.83014 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 145d6f9e-e2f2-3781-8e7f-a5d162a2e213 | -2.9327 | -54.16911 | 2025-11-02 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53a5a83b-eaeb-32b7-8370-5abfa3185a76 | -3.66001 | -50.71021 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02c9ecb6-9364-3bf6-8fbc-e2bcd26179c3 | -4.13912 | -48.81856 | 2025-11-02 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b15db33-3e08-3a22-9373-b8451c077391 | -3.42751 | -52.89003 | 2025-11-02 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 101c55d8-8f77-3f5a-aa30-f829e3957040 | -3.42475 | -50.24299 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a246eea2-37cc-3751-8e9a-ba2ba3b5b59a | -2.9333 | -54.16529 | 2025-11-02 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c08ff4f-4749-3ec0-a510-7d7f88099bec | -1.75007 | -54.44664 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ceab597-37c2-341e-9559-88a02d2be353 | -2.89142 | -54.85863 | 2025-11-02 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3476fa5a-855f-3924-ba6d-00583cce0009 | -3.07756 | -51.25941 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa364730-1a0c-33f8-8865-a9e0a821d612 | -1.74099 | -54.46023 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c271e17d-4d7d-387c-91f4-14cd7ba4e254 | -2.3124 | -48.58454 | 2025-11-02 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 07df825c-4ad9-3d9a-b565-b9ef1bdb777e | -3.08282 | -51.25265 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31c7a7ee-8f19-3b52-ae47-ddab93e0eab7 | -2.34645 | -47.54402 | 2025-11-02 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e61364b-e1d3-3a19-92a6-327b41257f7a | -1.25554 | -53.8471 | 2025-11-02 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b904f482-ded7-33a9-a437-400b28ed3931 | -3.45437 | -50.2231 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46e0fe81-6dfe-3ebd-bc17-047723f613a1 | -2.31157 | -48.58982 | 2025-11-02 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 662648d1-76ba-33b3-a517-172dff0c5428 | -3.83356 | -51.31346 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ba4f13e-392b-3eff-a438-008d769009ba | -3.39313 | -51.67154 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 527cedc5-b69b-3cc7-a234-0bf7b6c05ff9 | 1.69794 | -50.88943 | 2025-11-02 05:08:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ab8568f-dca9-35f2-9907-740535e10b44 | -3.01734 | -49.44198 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 227cb096-ccb9-331a-97d6-07c98f0bfd93 | -1.41998 | -55.23267 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85917011-1e61-3c36-aaab-cc359314109b | -3.45459 | -50.22546 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5445a4f-c06a-3511-8477-f01e395accf5 | -2.44363 | -49.02967 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19da0ecb-edd0-38f0-96cf-22d951993e8d | -1.56284 | -55.42599 | 2025-11-02 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 953af177-d7c2-322f-8066-7d0674cbc5a3 | -2.87165 | -53.97929 | 2025-11-02 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab326ad1-6d20-3203-8c8c-0b48d3b2c1e6 | -3.14117 | -49.4194 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7339f19e-7f2d-3ccc-8ccf-537f03a06b11 | -3.58277 | -50.26696 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 144a11ac-b97f-3fec-a618-ac49a5c2769b | -3.61814 | -51.47744 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c800fe6b-5150-3597-b9ab-860378bac6e4 | -2.34072 | -47.54639 | 2025-11-02 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a1bb594-81ab-3d7e-b00d-07cf98df880b | -3.35042 | -51.68289 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c301a536-a368-3d3c-9a1b-75fd0e35f819 | -3.07837 | -51.17304 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dffa30ef-2371-306f-9422-317bba77ea79 | -1.26697 | -53.86447 | 2025-11-02 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e061f39e-be53-34e6-a4e3-05e03d4c11b1 | -3.77115 | -51.34731 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d1c7013-d2ba-300c-acf5-d207368b0db5 | -3.28731 | -51.54788 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04a39530-8d94-3bbc-82bc-86ce0d3aa5f5 | -3.56431 | -51.64394 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a2392cb-64a4-3927-b2e6-418c4c0d271b | -3.3799 | -49.98132 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8e9ecc3-c677-383a-bbaa-ac77709329f5 | -3.32042 | -51.57439 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a7b9da0-ee78-324e-a009-56f5506c90a0 | -3.7717 | -51.34368 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18afa228-15ac-3ab3-afcd-d4e1c98de2f3 | -2.15369 | -53.64172 | 2025-11-02 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06b4b4d3-3ffc-3673-a2f3-7b6ddf261c02 | 0.15102 | -51.42044 | 2025-11-02 05:08:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f49601b2-b2d0-3400-b3a9-36818598f848 | -3.02273 | -49.43787 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fa012ad-19db-3a73-ab4d-2502a6beb416 | -3.38215 | -49.97957 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d13a0b1e-6841-3e69-80c3-17723b11b9f6 | -3.961 | -49.29605 | 2025-11-02 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ed5c6da-a985-3ad4-90e5-609a56f9dd05 | -2.79208 | -50.28738 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 775d8467-1d83-3d87-a7b0-f294df0c7330 | -3.04517 | -51.2244 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a40ea187-07a6-32b8-8fba-714320b7a2d5 | -2.35084 | -56.05515 | 2025-11-02 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d884a3cb-8102-3b51-8538-053e10ff17bd | -3.72576 | -51.7011 | 2025-11-02 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97e05725-e94c-303c-82de-5f5d2a29328e | -3.15817 | -50.82623 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efcfd35b-3312-3438-a769-19854ad4f756 | -3.91307 | -50.03497 | 2025-11-02 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbf6bdd5-6159-38c4-bad9-68e89142467e | -3.38059 | -49.97683 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c1465f4-ebf5-302a-9269-3903ec036a93 | -1.27778 | -52.9273 | 2025-11-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11c24c4a-c49e-3c23-9083-4f0022dd844a | -3.44699 | -51.61535 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9008e74b-81d1-3d35-8110-85dbf3286714 | -2.92897 | -51.46522 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7dc99e3-3c72-36be-b098-1b492088c3f4 | -2.61952 | -55.75046 | 2025-11-02 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09e10af6-5abf-334c-b43a-90e2e74dd6d0 | -1.73758 | -54.45971 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea6328dd-90af-3c5f-b4f5-004c7a5746be | -4.13993 | -48.81308 | 2025-11-02 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3170c291-2cf0-3418-b7d7-aad2ba9dc271 | -3.4391 | -52.63813 | 2025-11-02 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3d709c85-0e99-3a39-a934-ee6c458f369c | -2.74213 | -52.94389 | 2025-11-02 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5644347-bc08-3e66-be23-ff8d41cfeb86 | -3.42314 | -45.91347 | 2025-11-02 05:08:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41acf005-e8ad-30ee-91e6-91e7e5ac4864 | -3.60472 | -50.62349 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 967ab82a-645e-3bc6-8bb4-74063c270ebf | -3.66433 | -51.71652 | 2025-11-02 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 643b1e44-6403-3e91-ad07-72313221143c | -3.56332 | -51.64394 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 033a354a-4e91-3ed2-9599-7e74381a6366 | -3.01537 | -53.9675 | 2025-11-02 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8be7418-04f6-395b-9374-201d45fce3c1 | -3.82818 | -50.48893 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e10d2ee-40d3-328b-bb16-f6723e6d3613 | -3.6698 | -51.71791 | 2025-11-02 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d58c1aba-c9c2-3bfc-ae39-233ae743e0ac | -1.2641 | -53.86017 | 2025-11-02 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa45022c-61cd-3466-a8e3-3be76557eb35 | -3.0637 | -49.37516 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a2333e1-2e6d-3eac-966d-62eeebc17ca7 | -1.55952 | -55.42548 | 2025-11-02 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6734a981-88df-3be4-8d61-7e214e4583c0 | -3.8332 | -50.48535 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f66427b-b9b3-3a86-bee9-7d01667bcb7a | -3.63383 | -49.89128 | 2025-11-02 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ead74844-7ee3-349c-8026-8972d6946caf | -2.90961 | -54.2938 | 2025-11-02 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77d94d9e-2505-394d-b017-49237bbf6f25 | -1.81768 | -55.16837 | 2025-11-02 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 845c5182-d43a-3183-b33b-d8114a843f31 | -3.722 | -45.55303 | 2025-11-02 05:08:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f9701995-2fce-3402-bb62-314fe7438dca | -4.18031 | -47.65243 | 2025-11-02 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbd85334-6fed-37ac-97da-207d55776634 | -2.62961 | -47.30212 | 2025-11-02 05:08:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf0cdb15-45bd-3c0c-b4f4-e48d0325ea31 | -2.31006 | -48.58577 | 2025-11-02 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eab473ca-ed59-3caf-8a35-34c692595ce9 | -3.52947 | -51.64971 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f77d8f42-4f8f-37e0-a258-dc075a902a1b | -3.82883 | -50.48467 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d51d959-c749-39f8-b5b7-cfc59b6ae21b | -2.49242 | -48.15235 | 2025-11-02 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5769213e-629b-3863-a85f-2c2983da6f21 | -2.82537 | -49.131 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db0c91e7-1260-32a3-8d96-40dfe4cecc53 | -3.72523 | -51.70459 | 2025-11-02 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5956767e-32c4-3064-8e57-e21a52b7c66c | -3.50206 | -50.47382 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 030321ef-2281-3a97-baa4-70e2de03d5c1 | -3.24094 | -50.79464 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f0d50e31-2a46-3597-a0fe-7d813e047a15 | -3.22019 | -50.58664 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f778bdc-4ad1-3154-93d3-b29aea99832b | -3.2294 | -50.58391 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 845319f0-5df3-3438-b8c1-7a3457b417b8 | -3.07518 | -51.24777 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47d94eee-8cd9-3d9d-8a48-ae4c2abfc8f9 | -3.07928 | -51.2484 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3189107c-a96e-3209-a273-298f29735b7c | -3.14155 | -50.44954 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57b2ff7e-5904-3ad0-bdd2-96a70d39fb4c | -3.66631 | -51.71374 | 2025-11-02 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa9b7dbf-929a-395d-a6a5-4f24dacec142 | -3.72266 | -45.54838 | 2025-11-02 05:08:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 589ec07c-e610-356e-b553-8003fed6bc4e | -2.44438 | -49.03174 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
