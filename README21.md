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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9150e7b7-3caa-36cc-91b3-e60070de4292 | -3.1983 | -50.2867 | 2024-11-11 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 085def4a-db11-3c18-b137-3d8cc0ae563c | -9.457 | -35.8825 | 2024-11-11 02:10:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 98.8 |
| dc5f4382-29d6-3cec-89b9-f37ad08818eb | -3.2428 | -53.0519 | 2024-11-11 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a7bf9b9b-dbb6-32e1-b208-3398a978c175 | -3.2244 | -53.0524 | 2024-11-11 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5c16d93b-d947-37c2-93ec-3583fb15eeda | -3.2603 | -48.7582 | 2024-11-11 02:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 65809792-cc5d-3362-bd7f-f32b69f9e501 | -3.2588 | -53.6994 | 2024-11-11 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 19ed0e10-5e05-39fd-bdee-0849d3fc0b91 | -2.8508 | -49.4108 | 2024-11-11 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 216b6cb6-0d13-3034-9780-57b33d509bdb | -1.626 | -52.5362 | 2024-11-11 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| fbb4247f-5e41-350d-b2be-f21631f0cce4 | -3.1458 | -54.4859 | 2024-11-11 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4edc8b6d-dfe6-325e-9062-287d4eecab10 | -2.2075 | -48.3811 | 2024-11-11 02:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bbe93c9a-a3f1-33da-9797-cd503c6ad350 | -2.2298 | -53.6623 | 2024-11-11 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 81b31fa9-5664-3f28-aabb-83f0d2675b6a | -3.0214 | -53.2404 | 2024-11-11 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0ffd0b38-f4ea-3483-b24b-eb1d30e1da71 | -3.1458 | -54.4659 | 2024-11-11 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b903f5f6-7273-33f3-b6da-5f36c34129d0 | -2.8508 | -49.432 | 2024-11-11 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0b0ff88e-2108-3937-a7ae-3e8f854e6968 | -3.0296 | -50.9607 | 2024-11-11 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| effd23bf-ed26-3ba3-bc3a-5bec6ed45b0e | -2.189 | -48.3815 | 2024-11-11 02:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 609ee7d2-7192-39af-8f99-fee9df1ba89f | -2.189 | -48.3815 | 2024-11-11 02:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 22baf71d-7d06-31fe-b7f8-dd1649d6ded2 | -2.2663 | -53.7422 | 2024-11-11 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 112e0b23-101d-3fcb-ba77-0a0d61729fd5 | -17.2737 | -57.488 | 2024-11-11 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| c583733a-e304-34e9-b582-c460464e6092 | -3.2244 | -53.0524 | 2024-11-11 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c9c65134-95ed-31fc-a98d-e87f23b9fe3d | -3.2603 | -48.7582 | 2024-11-11 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ee71cf8c-0d06-3004-bb10-e9da0ec384ed | -17.6073 | -57.5099 | 2024-11-11 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.0 |
| ce5d9b9f-7ba5-3daf-8e95-f3f195508421 | -3.2243 | -53.0727 | 2024-11-11 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6c909dc3-92a8-31a3-8e5d-bb9b90173a7f | -1.4057 | -52.3758 | 2024-11-11 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e2640f8a-010b-3cf3-8d06-6fcbbb840989 | -2.248 | -53.7426 | 2024-11-11 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b7412ee0-f21f-33c4-9bb6-a7c75f8bb9c9 | -17.2936 | -57.4652 | 2024-11-11 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 1a6d27c4-5964-380a-8b53-2071f98de0fc | -3.0845 | -51.0631 | 2024-11-11 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d12b9aa4-b8f9-3cfb-9c8c-8c6c23e98028 | -3.0295 | -50.9815 | 2024-11-11 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c5fc40f2-2046-32fd-8ce4-03b6f4f2295f | -3.0111 | -50.982 | 2024-11-11 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6978189d-6aec-37cc-b8e4-46278cd59b38 | -3.2428 | -53.0519 | 2024-11-11 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7eaef54b-c4ef-31fd-bc95-b47c2c85a72a | -3.2588 | -53.6994 | 2024-11-11 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c439ca29-77f2-3886-9b6d-2375af8a2b9a | -2.2075 | -48.3811 | 2024-11-11 02:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d99fee83-de5e-34f4-84ee-9d1890973802 | -3.1458 | -54.4859 | 2024-11-11 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 634bf791-5aa3-36a4-ab64-f60a15dc3939 | -2.2298 | -53.6623 | 2024-11-11 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ff33cd3d-b821-3e6e-ae3e-df53b53507a4 | -23.9312 | -54.034 | 2024-11-11 02:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| 3409e11d-3138-388b-a269-5564d54d3de0 | -17.6066 | -57.551 | 2024-11-11 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| aeb2d811-7c8f-30d0-a112-d27d1fc95a16 | -2.1891 | -48.36 | 2024-11-11 02:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 867d95ba-49d1-36a2-98ae-545924ad579d | -17.5875 | -57.5122 | 2024-11-11 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 57404379-8bda-3c4b-96d4-2d763986c8aa | -2.8508 | -49.432 | 2024-11-11 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c83bc359-fd05-3163-b853-986395d8461e | -3.0214 | -53.2404 | 2024-11-11 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 7f217a56-763d-3d85-b580-526fddb29320 | -9.457 | -35.8825 | 2024-11-11 02:20:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| 85614e4e-d7af-3147-9ea2-53f1f7f9be0a | -17.6086 | -57.4276 | 2024-11-11 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 4b7a1895-a8e5-3781-9998-1b413ba40dbe | -3.2427 | -53.0722 | 2024-11-11 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 19d9e51a-6ad2-3547-949c-50bd8c3cb6c9 | -2.2297 | -53.6824 | 2024-11-11 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 319ec6f4-9a56-38d5-88ba-6d3ed9571b63 | -3.1458 | -54.4659 | 2024-11-11 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 1587b9b7-4762-3b3d-8588-5cfec3ed771f | -3.0296 | -50.9607 | 2024-11-11 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6de53f8c-d083-398e-aee5-3c64081e5d9c | -17.6266 | -57.5281 | 2024-11-11 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.5 |
| a1d1dcd0-8240-35a1-9abd-a268f69bf022 | -3.1983 | -50.2867 | 2024-11-11 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e93edae7-c94a-32fe-ba2f-3c12c50009fd | -1.626 | -52.5362 | 2024-11-11 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 4e810d69-0723-3a13-9c98-af7c6b5c27cf | -3.0213 | -53.2607 | 2024-11-11 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e85b0f7d-c0fc-3a15-906f-898c55ea1996 | -17.6069 | -57.5304 | 2024-11-11 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 199.7 |
| 8e7b3b17-996a-3a40-9ef4-6a6be38e3191 | -17.2933 | -57.4857 | 2024-11-11 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.9 |
| 1d0a79a6-4617-3807-a1ab-15dd2ce811d9 | -9.4762 | -35.8792 | 2024-11-11 02:20:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 74bb9c19-8765-3a3c-9b8a-121832f23170 | -17.5872 | -57.5328 | 2024-11-11 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.1 |
| f4e6fbcd-9595-3d96-b5bb-a45e5ebbd390 | -3.2603 | -48.7582 | 2024-11-11 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2f0de938-0886-355c-bb2a-360960f852bd | -2.2298 | -53.6623 | 2024-11-11 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| fe43677d-9076-30ed-a363-970681b15eff | -3.2244 | -53.0524 | 2024-11-11 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 914d8ef6-4266-317b-9692-6edd6297f6f5 | -3.0296 | -50.9607 | 2024-11-11 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 17de9a62-5e86-3e71-8c99-7cad34aee3cf | -23.9312 | -54.034 | 2024-11-11 02:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.6 |
| 23109c2f-c36e-320b-a27d-4160540e23fe | -2.2075 | -48.3811 | 2024-11-11 02:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 918072af-fed8-360a-a486-021013568d8f | -3.2427 | -53.0722 | 2024-11-11 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5c33b913-4e42-32aa-817a-532617b033a0 | -2.2297 | -53.6824 | 2024-11-11 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ad51f9af-5901-3c1a-9a6b-8912f157b9f8 | -17.2933 | -57.4857 | 2024-11-11 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.2 |
| 536cb7c0-190f-3551-a209-28834e9238b5 | -2.248 | -53.7426 | 2024-11-11 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ab849ab2-fc7a-398a-91f3-d774ab9e0e12 | -2.3863 | -50.3299 | 2024-11-11 02:30:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7b58d623-e310-3e29-a102-1bcd9f4389e7 | -17.313 | -57.4834 | 2024-11-11 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 20b9017e-9ae5-3b12-8395-3b0e5ac7b187 | -2.4367 | -51.948 | 2024-11-11 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 83d96f6d-99a8-3d39-a2a4-37d27e7edee6 | -3.0213 | -53.2607 | 2024-11-11 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3ae03cc6-9f3a-354c-97e0-bc8ba6440e79 | -17.2737 | -57.488 | 2024-11-11 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| a198cddb-ee91-3e11-bc97-6a975cb2bc05 | -1.3872 | -52.4169 | 2024-11-11 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 17070b69-b4b5-37a2-abb3-ad7ab29c8c49 | -3.2428 | -53.0519 | 2024-11-11 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e81c2740-978b-3c4e-b92b-61c7a3dafc8c | -3.0845 | -51.0631 | 2024-11-11 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 04b909e8-180e-3cc6-b2c2-8e8924ea7425 | -3.1983 | -50.2867 | 2024-11-11 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 291d90f4-8b06-3c62-906b-7ea5cf3a9468 | -2.2663 | -53.7422 | 2024-11-11 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 93d006be-3a8c-347d-b923-ef62f2bfd3b8 | -3.5346 | -45.7061 | 2024-11-11 02:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| eaab423a-6d40-34af-931d-d204b444eb7d | -2.189 | -48.3815 | 2024-11-11 02:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| cd5ed5e1-ade9-3e27-a2d1-f3471e87bbe5 | -3.0214 | -53.2404 | 2024-11-11 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 942a5812-042d-3628-97cd-8f5f0e8baf50 | -2.8508 | -49.432 | 2024-11-11 02:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 15200d88-6ef2-3a89-b964-b24e3f89b391 | -3.0295 | -50.9815 | 2024-11-11 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b0706f35-4109-3466-aad2-aeb4eee10d45 | -3.1458 | -54.4859 | 2024-11-11 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 53f53432-49fe-3b34-9c51-60caf59e342f | -1.4057 | -52.3758 | 2024-11-11 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9641efdf-5720-362b-97fa-af6c76b926b8 | -3.2168 | -50.2861 | 2024-11-11 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 71cdbe67-e9d3-3516-8e7e-489793004837 | -2.248 | -53.7426 | 2024-11-11 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 21bbf026-cf2e-3691-818c-a3758d373014 | -2.2663 | -53.7422 | 2024-11-11 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b1a261ba-fe15-3ad9-8e0f-93bb89b22c1d | -2.189 | -48.3815 | 2024-11-11 02:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| c55898bc-4224-36dc-a45b-67f91f4da0bd | -1.3872 | -52.4169 | 2024-11-11 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| bbc21ebf-d79f-35d8-a7df-545c9952da0f | -3.1458 | -54.4859 | 2024-11-11 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f226dd84-2c0e-3c5d-9545-8505fb34ee51 | -3.0296 | -50.9607 | 2024-11-11 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 597dc4fe-8f6c-3161-8cca-1b2a09df34b3 | -3.0213 | -53.2607 | 2024-11-11 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 140429ec-46a9-3fff-934b-6d78fccae35e | -23.9312 | -54.034 | 2024-11-11 02:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| f04be857-b458-31c7-94bd-8c57bf68e207 | -3.2427 | -53.0722 | 2024-11-11 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ef4941de-1ea3-3eab-bb15-533a045b0375 | -2.8508 | -49.432 | 2024-11-11 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d66a227a-3372-34fa-94b7-a7568b47a7bf | -17.2737 | -57.488 | 2024-11-11 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 418eb1d5-d9ea-3131-8383-c4351e24b15d | -2.2298 | -53.6623 | 2024-11-11 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 315c57f9-71ca-3e2b-b2c4-7d55747b75d0 | -1.4057 | -52.3758 | 2024-11-11 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| bcad974a-20f5-3ad5-bca1-9cb71f512049 | -3.2428 | -53.0519 | 2024-11-11 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 58dc5e55-72c8-3fb1-8f4a-d08754bc286f | -2.2075 | -48.3811 | 2024-11-11 02:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 31a43b99-a0d0-332e-9a42-c99d6d0e7e5f | -3.0214 | -53.2404 | 2024-11-11 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 51885231-1da9-3b18-bf41-f39719ef5f08 | -2.4367 | -51.948 | 2024-11-11 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e3c2a0ba-c379-3ec6-b888-be21588022b6 | -17.2936 | -57.4652 | 2024-11-11 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |


[Clique aqui para ver as próximas entradas](README22.md)
