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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a7d83fc-d18b-3055-bd2c-32de42cfe1d8 | -9.432 | -45.8293 | 2026-10-07 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b73d7d93-6c8f-35c9-a562-76bb87324663 | -11.3742 | -46.7173 | 2026-10-07 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 28384cf9-c493-3ec6-a111-b6a070fc1f8b | -7.1813 | -55.1237 | 2026-10-07 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 0ee0e2aa-9ad4-3300-9447-3ad55f0fc9c6 | -7.2 | -55.1026 | 2026-10-07 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 8a6d3e17-e60a-3d6c-a7ac-1b7a19ba3a65 | -11.3937 | -46.6922 | 2026-10-07 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1625a171-c139-32aa-853a-6413ad243d2f | -11.0867 | -45.6459 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 6d8ec8cf-906c-3e1b-bf7b-cfaadf50704c | -8.2184 | -46.3396 | 2026-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 233e1770-fde1-3f20-8d49-66388d8ced62 | -7.5568 | -46.7128 | 2026-10-07 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5bdc1d78-ce3c-3c73-b6af-bb4c780b35a8 | -11.0459 | -45.8109 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| d51a0dfe-0e3b-3179-891e-671d167d5a8f | -7.5284 | -45.8885 | 2026-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 74ada9f8-e63b-33b3-8d39-467f74a47c43 | -11.8408 | -47.3496 | 2026-10-07 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9f35dcef-a14f-36ff-8b07-ae2ce4118a28 | -11.7943 | -46.7056 | 2026-10-07 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7a3d88e2-022c-38c0-b3a1-398724eb323c | -11.8503 | -43.5598 | 2026-10-07 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 259b1b89-4f4d-3f1e-a554-e8c55b5a04f0 | -10.8591 | -50.6692 | 2026-10-07 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2f6b166e-56fa-3582-8cf9-433933dab858 | -7.8679 | -44.1922 | 2026-10-07 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| ce2f54ac-29db-379e-b597-a23cf16cd98d | -7.7595 | -43.8092 | 2026-10-07 13:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| e32eba29-0c72-34b0-99aa-e8383a08d9c1 | -7.2179 | -55.1817 | 2026-10-07 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 373350c0-fb40-3b52-8f3b-8389c4a3c737 | -7.8865 | -44.2134 | 2026-10-07 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 7a1b046b-eb7e-3390-bbd4-9eb2839b7924 | -11.7947 | -46.683 | 2026-10-07 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2d28461b-dcf6-3cfb-9a3d-e3d1fc7568bf | -8.5356 | -55.383 | 2026-10-07 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 33bcb8b0-2a77-3569-92ce-2cdd331eb342 | -7.5756 | -46.7112 | 2026-10-07 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 2d28aeb0-e25b-342f-9a7d-1a9aab6f3593 | -7.8789 | -72.3492 | 2026-10-07 13:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 91.2 |
| e5e50e42-200f-3cab-9a1b-221c976db33e | -7.3475 | -45.2725 | 2026-10-07 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 96c61a50-8250-377f-b7b7-bf1779af24ed | -11.0646 | -45.8312 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| d0decf10-9bb6-3bcb-a333-2da2642851e9 | -7.1814 | -55.1036 | 2026-10-07 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| e37f53d4-7f36-3602-b88e-5f9b9c182506 | -11.7335 | -43.649 | 2026-10-07 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 29fcdae9-5c55-31e9-aec4-f85cfe9dd049 | -7.7213 | -45.4418 | 2026-10-07 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3cae067e-276f-3a6a-93eb-f18efe47ce1f | -11.0863 | -45.6688 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 3edb3cf5-85ed-3b28-affa-9b05fc19e16f | -14.2531 | -41.6256 | 2026-10-07 13:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 4d5eb210-e32a-32c9-b2c5-0d705970bbc9 | -7.7592 | -43.8325 | 2026-10-07 13:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 873a4285-553c-3ab1-946f-64b6e68a0839 | -7.7399 | -45.4627 | 2026-10-07 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4f9bb290-c29b-3917-b850-98afe58f6a92 | -7.721 | -45.4645 | 2026-10-07 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 1cf2748e-fbd2-3325-9dc0-0ee322e97fd1 | -11.1556 | -46.0916 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d9fe1930-3f7b-3af5-8e86-fa88492d19c5 | -7.5571 | -46.6906 | 2026-10-07 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c98f371c-e708-37ae-af88-8bf53789ff50 | -11.3745 | -46.6948 | 2026-10-07 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 6c5136d2-e321-3d7c-939a-6fe0ead1f023 | -7.5286 | -45.8659 | 2026-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 7728c550-5e0d-3301-8c4a-8c536aec85d8 | -11.1051 | -45.689 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 268ffe5a-34a9-3013-b21a-025f08518280 | -7.8676 | -44.2153 | 2026-10-07 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 317.2 |
| b659a914-a51e-3453-8c41-6961698f7195 | -6.4413 | -55.0224 | 2026-10-07 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| f65095ba-1f4f-3b35-97c5-6e10056141e2 | -8.5051 | -54.6202 | 2026-10-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 428.0 |
| f5400fc3-6f30-3dd3-a095-eea0aa7d1a23 | -14.3608 | -55.032 | 2026-10-07 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| a8de7094-46e9-3023-89d2-cd5001aa9285 | -7.721 | -45.4645 | 2026-10-07 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 3b9e23f3-10af-3c0f-90d7-b38b72ad417b | -11.1556 | -46.0916 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 5c4c8462-2ac4-30c5-8367-bd1f62166411 | -11.3937 | -46.6922 | 2026-10-07 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4d326eaa-1c65-3fc0-883e-3d8fe5420562 | -8.5844 | -45.6729 | 2026-10-07 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 123720be-1d54-3341-9342-ef8f9a438238 | -8.5238 | -54.619 | 2026-10-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| b625b1b1-5681-37a0-837d-efeeb02c497d | -7.7595 | -43.8092 | 2026-10-07 13:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| efeca149-20c8-3964-a0ef-364bd4998a8f | -7.1813 | -55.1237 | 2026-10-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 842f9b7a-e376-3d04-8a5c-92373c21f4cc | -11.3745 | -46.6948 | 2026-10-07 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 3d4259db-0960-30f0-aa54-1b5374aa8b0b | -7.3935 | -46.2144 | 2026-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 412e638d-2ad3-3b4f-a019-aec736918f76 | -7.5284 | -45.8885 | 2026-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 7ba0855f-9a57-3d41-9068-8fa010376343 | -11.3742 | -46.7173 | 2026-10-07 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 163.6 |
| e52144d3-9251-3694-abed-9e229dbb08f0 | -7.7399 | -45.4627 | 2026-10-07 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| df5cf466-11bd-359a-992e-422b15008f0a | -7.8146 | -45.5009 | 2026-10-07 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1720ac8e-7329-3dd1-b3c0-ffda6c3a20a3 | -11.7335 | -43.649 | 2026-10-07 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 00bc4445-938d-35c6-894e-7d0418ce6f1e | -11.065 | -45.8084 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 5427f606-4f7d-3b5f-ab15-14e1ad6d21a3 | -7.2816 | -46.1571 | 2026-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 6ac7857f-77e2-3e14-9aff-3bd764292d6a | -8.524 | -54.5987 | 2026-10-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 2c27ff59-6977-33da-aa26-d8780b0d981f | -11.0642 | -45.854 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| f007461b-2bd5-36ac-be4c-653360e509ad | -6.4413 | -55.0224 | 2026-10-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f5b2f293-c38d-3b56-9687-8ddda66b173e | -11.0646 | -45.8312 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| de55d715-f805-3e56-8ea9-d58e85f76283 | -11.1054 | -45.6662 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| fe8835d9-4dc0-3930-b5bf-6d52c70ab35c | -7.2 | -55.1026 | 2026-10-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| cbc2022d-119e-3973-bc23-e2105e875107 | -7.8679 | -44.1922 | 2026-10-07 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 100c4adb-7608-39e6-987f-81976614cd31 | -11.0867 | -45.6459 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 42e381f1-3788-3753-a1d3-55316f9f49d8 | -9.1583 | -45.11 | 2026-10-07 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 304.3 |
| 66a1eaa6-d7bd-3c3f-9b91-e21a8eb9d521 | -11.8508 | -43.5361 | 2026-10-07 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 134bd7c9-69a3-391b-8025-c99bb08c1fc2 | -9.158 | -45.1328 | 2026-10-07 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 3f45d9e9-6954-3081-b007-95b1050b1b8f | -11.0863 | -45.6688 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.8 |
| c8872934-532f-384c-9de5-b37a2b852ea9 | -7.8865 | -44.2134 | 2026-10-07 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 143c09e2-e9db-3fe0-8261-1998605b540c | -7.1814 | -55.1036 | 2026-10-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 2edc22eb-8078-3216-9067-d4217aa60b8e | -11.7947 | -46.683 | 2026-10-07 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| aa144676-8bee-31b8-b43f-b3bf4317b348 | -7.8789 | -72.3492 | 2026-10-07 13:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 98.6 |
| b12d2eaf-7e5e-3b34-8791-63becd5a109e | -7.7213 | -45.4418 | 2026-10-07 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 137.5 |
| d1552aec-3e83-3b83-a230-b1825e2a44bc | -11.8503 | -43.5598 | 2026-10-07 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c89c8a12-0f50-354c-a20a-07e3c88b14a2 | -12.2132 | -44.6991 | 2026-10-07 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 06b6bd20-7986-32f9-999f-c3c38854dca7 | -7.8676 | -44.2153 | 2026-10-07 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 582b2bb6-d057-33d1-add6-a29ac75a679f | -7.5756 | -46.7112 | 2026-10-07 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 9db8ed20-013b-3bc7-8c66-66c720719cf7 | -7.5568 | -46.7128 | 2026-10-07 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 8f8101d8-0581-30a2-93a7-a3522c1cf3fa | -10.3738 | -46.2146 | 2026-10-07 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 243.9 |
| f9a47155-77d8-3ad4-a841-b6744e71de56 | -10.9953 | -45.4068 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 19b72072-486d-3d5a-8690-9c60e10ff6e2 | -8.2184 | -46.3396 | 2026-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1c80512b-2d2c-3ff6-826c-ad3e0d6a27b4 | -7.5286 | -45.8659 | 2026-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 59967e74-70ad-326f-a966-98537e929afb | -10.3735 | -46.2372 | 2026-10-07 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 270.2 |
| c820fc63-b5b1-3605-bf32-e5965c4c235a | -7.3475 | -45.2725 | 2026-10-07 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 685d596f-d034-3e25-a4ba-c142bdddb12c | -7.3747 | -46.2161 | 2026-10-07 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 11963d28-29e3-3043-9705-115842f52afa | -12.2136 | -44.6758 | 2026-10-07 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| b0b61790-8129-37d2-9d09-f96a24e0e86a | -10.8591 | -50.6692 | 2026-10-07 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 668d4fae-2a3c-3add-9b38-6ff20d06124c | -11.1051 | -45.689 | 2026-10-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| fba41768-997d-35d7-bcd8-e099ed356629 | -7.7579 | -54.9499 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ab2fdbdf-9d34-3920-8c7c-943772369342 | -7.5571 | -46.6906 | 2026-10-07 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8fa5b6e6-58d7-349a-b8e3-4d2c187c8bd9 | -8.3022 | -44.1467 | 2026-10-07 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 84017fc9-3596-315f-b26d-a607b019f94b | -7.3747 | -46.2161 | 2026-10-07 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 6ff83a5e-8db0-3ffd-b887-4d6e5e2e821a | -11.7335 | -43.649 | 2026-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5d3d21a7-5e2e-3f9b-92a0-a4b98640497f | -7.5756 | -46.7112 | 2026-10-07 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| f190735f-19cb-3c45-b9c5-da213670a5cc | -7.8676 | -44.2153 | 2026-10-07 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 361.7 |
| b00fa778-6633-37b6-9f5c-612819dc2469 | -11.0459 | -45.8109 | 2026-10-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 0261ca59-dd2d-39d2-a65d-988cde389943 | -8.5238 | -54.619 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 569f88cf-9fb8-320d-8e7d-ea322cae1e47 | -6.4413 | -55.0224 | 2026-10-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 472352ab-1e2b-35b3-9f23-2ddf22933116 | -7.8865 | -44.2134 | 2026-10-07 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |


[Clique aqui para ver as próximas entradas](README130.md)
