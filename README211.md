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

## Dados Diários - Página 211

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e05aa78-bfdd-3974-9601-5f77dd0ee8cb | -8.6291 | -67.0482 | 2026-10-08 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 8856f1d8-9e6b-3dcf-9c74-fa7c9805a5f8 | -8.1876 | -54.7219 | 2026-10-08 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| e722dde9-5331-3a67-9e4b-4ebf3d882d5a | -11.6562 | -43.6846 | 2026-10-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| bf513e38-66fa-364e-9e87-e74de7499db5 | -9.9018 | -44.7917 | 2026-10-08 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 9c216813-62e7-357c-812e-91bebc01ff7b | -8.6107 | -67.0301 | 2026-10-08 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 258.1 |
| 4657393b-3886-3ed9-b312-3e6080efa31f | -11.1051 | -45.689 | 2026-10-08 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 7f4aa530-ea86-3c07-a2d4-0bf9bfce0baa | -7.7213 | -45.4418 | 2026-10-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7975b0e1-fb66-354c-8c8a-8a165f96b4d7 | -11.3986 | -47.5635 | 2026-10-08 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c64dbbb8-feb2-3569-a85e-2abb44e3f2f4 | -11.6186 | -43.6433 | 2026-10-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 3a9aa607-47a8-3864-bf02-de6ca1bcba9a | -7.2185 | -55.1016 | 2026-10-08 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 653fde2f-7adf-3c19-89a8-5e1125bfb515 | -8.9501 | -45.1334 | 2026-10-08 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 2553c278-3c11-30b7-9a91-242c62c2e9e9 | -8.5313 | -46.911 | 2026-10-08 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| cfe268d6-21da-3727-ad90-91b4a50a67ae | -8.6292 | -67.0111 | 2026-10-08 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 887bf032-412d-3dcb-b2ab-474595e37000 | 1.6937 | -55.6461 | 2026-10-08 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e688d115-b183-3c31-af7f-18e030b4d0a1 | -7.7025 | -45.4436 | 2026-10-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 247.0 |
| 074d6be7-ae76-3c61-97cd-b89a844dea5d | -8.6106 | -67.0486 | 2026-10-08 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 566f217e-c590-3d4d-9e64-378c2626a6b1 | -11.6365 | -43.7113 | 2026-10-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| e5edf8b5-7d37-3c42-b157-cc15e16cfab1 | 3.5448 | -51.2772 | 2026-10-08 13:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 385284a8-18a0-3577-8095-8dad69079e5c | -9.9585 | -43.5752 | 2026-10-08 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| d0b285ea-344b-3a3e-af01-c63a68bf810d | -7.5571 | -46.6906 | 2026-10-08 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ba3a4f03-2675-38de-a9a0-d82393cc3ffa | -11.1238 | -45.7093 | 2026-10-08 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| af055d9a-878b-31b3-be16-7d20818ccac0 | -7.0065 | -59.1223 | 2026-10-08 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 89c3547a-2d86-3d0a-9c36-547b1361ad1d | -9.475 | -64.3525 | 2026-10-08 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ac3b7e97-e8f2-351d-9289-702ba04ec98a | -9.9589 | -43.5516 | 2026-10-08 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 1a9e5884-3b7d-33a3-b590-9e86bd2b04bb | -8.6107 | -67.0116 | 2026-10-08 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 0da2421a-4fc9-3979-a208-3a2908a3886b | -8.8902 | -45.3679 | 2026-10-08 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 45a99623-0213-3c7a-8dfb-99118617c6e4 | -11.6374 | -43.664 | 2026-10-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9ac1fe83-75bf-323c-9a1f-b8dd7fa45cb7 | -10.4337 | -47.2824 | 2026-10-08 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 264.7 |
| 4971f371-bfa2-3f43-9a37-2c824903f314 | -13.1641 | -54.3178 | 2026-10-08 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1abb83e7-9c07-37df-b755-66e1fd708597 | -12.1738 | -44.7517 | 2026-10-08 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| f266278c-b9cd-3a16-b217-cb9d3d8aacb5 | -9.1543 | -49.8142 | 2026-10-08 13:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| cf265e87-62f9-3d5a-ab39-09385559ee9b | -11.3103 | -44.8337 | 2026-10-08 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 223.3 |
| c6340339-cd10-35ab-92c4-e45944cc6df6 | -7.8876 | -55.0023 | 2026-10-08 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 740b49b6-9214-3a7f-9b2c-4dbc734b4997 | -11.3539 | -51.8654 | 2026-10-08 13:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 8fa9ea7a-b868-3ef4-ba9e-31c5a683669b | -11.6369 | -43.6876 | 2026-10-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.4 |
| c28d9833-ef5f-30a1-94eb-d45f2e676407 | -9.8795 | -50.5131 | 2026-10-08 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b409b3c7-66fa-3c96-b7b3-04d9e8f5ecf5 | -8.0711 | -55.2921 | 2026-10-08 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ab40b639-605b-319f-b9d3-277da8a24306 | -11.619 | -43.6196 | 2026-10-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 1278310f-9de5-3bf3-b38c-d8d6ee18a6fe | -9.9014 | -44.8147 | 2026-10-08 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 38e4aa13-f079-30a7-80f2-4cd440a5b7a3 | -11.8676 | -48.0348 | 2026-10-08 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 2bddc3e4-dcc3-3a65-8f6d-5b8f6188640f | -11.6557 | -43.7083 | 2026-10-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 4e212559-b0ad-3424-addc-2f4a93ff5440 | -9.0592 | -65.9209 | 2026-10-08 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9a9b05bf-e578-3d0f-b806-9f74e858a571 | -9.9398 | -43.5542 | 2026-10-08 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 6b6353c2-da25-3fb8-9e02-0ec9a06d947f | -10.4527 | -47.2801 | 2026-10-08 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 8d9424c0-51fd-3d24-8f4b-fd606ffa863a | -12.1545 | -44.7547 | 2026-10-08 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| ef3a8e06-a398-3544-b13e-3b220f5dd9aa | -13.1833 | -54.3158 | 2026-10-08 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| cedad4f2-b088-344c-8233-57f72dd7892f | -10.4337 | -47.2824 | 2026-10-08 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 225.1 |
| b06ab3b4-f86f-32df-9dd6-30dcbdf39422 | -10.434 | -47.2601 | 2026-10-08 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a32d7a52-61e5-3c66-aa3e-f035b60f26b7 | -9.475 | -64.3525 | 2026-10-08 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 6be9498d-a4c4-35d6-91fa-ff8195da7d7f | -8.0895 | -55.311 | 2026-10-08 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d22c1d6f-f6b4-3aff-bbe7-14da0c04222c | -12.1922 | -44.7953 | 2026-10-08 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| de4f7196-bcd0-34b3-9229-329650965370 | -7.0065 | -59.1223 | 2026-10-08 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 89aca6d7-c674-3858-a571-505a815ac60f | -11.3937 | -46.6922 | 2026-10-08 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| d467dc4d-5fbb-311b-8cd3-824e446ae7e4 | -8.2826 | -45.7038 | 2026-10-08 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| fe497a42-6941-31e4-8b84-563cdeca3157 | -11.3554 | -46.6973 | 2026-10-08 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f1605762-79ba-304a-ae28-e54302437127 | -11.8595 | -47.3694 | 2026-10-08 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 7adc30ff-1b63-3390-b401-f483b0999b29 | -8.0709 | -55.3121 | 2026-10-08 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7f4af216-a6f9-31b3-a4f7-f5d975d4268a | -8.6107 | -67.0116 | 2026-10-08 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 20bab6e4-8ca9-3be6-8fe4-857bbe71fecf | -11.8404 | -47.372 | 2026-10-08 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ec69b750-42af-3eaf-ba90-e174efc97315 | -10.4527 | -47.2801 | 2026-10-08 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 663cd040-b3f0-3b07-9939-7d9102fddf01 | -9.9014 | -44.8147 | 2026-10-08 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4d2144c9-658a-3200-afb7-2a1d1775203f | -9.9398 | -43.5542 | 2026-10-08 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| b4ab7c3a-e55d-3a22-b382-0ca6e45a93b8 | -8.6106 | -67.0486 | 2026-10-08 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 157.6 |
| eb4d27d6-56a1-33eb-acd1-681ddcbf762f | -13.1641 | -54.3178 | 2026-10-08 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 876df8b3-0106-3329-92a9-4464fbf4afb2 | -11.3103 | -44.8337 | 2026-10-08 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 228.2 |
| a7dff718-d1c8-307b-b6d2-9471d1c889f0 | -7.8874 | -55.0224 | 2026-10-08 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b00cda87-2fc0-3bd2-92d9-da406c53e6af | 4.4436 | -60.9278 | 2026-10-08 13:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 4d8ec0b0-b31d-3d29-ad72-0f7c4e835bf9 | -7.5284 | -45.8885 | 2026-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2f194a80-e56c-377f-8f0a-2c1423a63bfc | -8.6292 | -67.0111 | 2026-10-08 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 1daec82d-4308-35b1-ad5e-4fcd4590b588 | -8.9501 | -45.1334 | 2026-10-08 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 41a652a4-e3d3-3d28-9c51-aafcce70c568 | -13.1639 | -54.3385 | 2026-10-08 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 91b68079-f798-3e5b-bfd9-d7c2eeddf8fb | -7.8876 | -55.0023 | 2026-10-08 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| c4084e24-0dbe-3eea-a851-fc41a8b2e05b | -11.3539 | -51.8654 | 2026-10-08 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 849a4a9d-b54b-3343-aaee-8ae53823cd3a | -13.1833 | -54.3158 | 2026-10-08 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 173.9 |
| f3c7d333-9cc1-3bfe-a2b4-9b9412ee558f | -11.8408 | -47.3496 | 2026-10-08 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 949135be-7f55-3e32-b2dc-b14af8fc97c7 | -10.5094 | -47.2956 | 2026-10-08 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| de4f39f1-1a36-34e8-8624-e82489b285c1 | -8.0711 | -55.2921 | 2026-10-08 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e6b9f9cb-021f-3a11-9878-33bc389a35d7 | -11.619 | -43.6196 | 2026-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 01b8bbc4-93d6-3aac-aa4e-66895ae07a39 | -8.6107 | -67.0301 | 2026-10-08 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 265.3 |
| eef73f02-015c-3f40-85cb-6074b0ff0d10 | -11.335 | -51.8673 | 2026-10-08 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4cf98235-f0d3-3a22-8c21-2ef360691463 | -7.2185 | -55.1016 | 2026-10-08 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fcc5f9dc-7dad-37da-a2a9-e0caf6001dfd | -8.1996 | -46.3415 | 2026-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| bb1532b9-aa2f-3a2f-af64-958825cf881b | -10.6722 | -47.83 | 2026-10-08 13:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| a6d027dc-4a69-3539-8ae8-8e03a007c9e0 | -9.9585 | -43.5752 | 2026-10-08 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 8d573aae-c0f0-3dc8-b904-205225a885b3 | -9.0592 | -65.9209 | 2026-10-08 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4a98d6fc-ab5d-399e-9419-a5b39b26f28a | -7.4697 | -42.8315 | 2026-10-08 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| 17c9c87d-5faa-3767-86a9-258fd86b7785 | -11.6181 | -43.6669 | 2026-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 450.2 |
| b1f351f4-6ac6-3e13-a6a4-746baf8fd676 | -11.6374 | -43.664 | 2026-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| e4443f32-ca2e-3be7-9965-543a608480d2 | -11.6369 | -43.6876 | 2026-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |
| da06a096-3692-327d-9280-63e701d0e60b | -7.4694 | -42.8551 | 2026-10-08 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 53d1d8af-de6a-3549-a9a7-253ea929dce2 | -8.969 | -45.1313 | 2026-10-08 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 78e3a592-dbaf-3573-aac3-d4093afd7446 | -9.9018 | -44.7917 | 2026-10-08 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9ccd340c-9980-3e73-8e8e-4877d0bb840f | -9.4936 | -64.3518 | 2026-10-08 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f42bf70e-6a27-3c41-975b-fd209ef0b85b | -11.1051 | -45.689 | 2026-10-08 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 3818f84c-5cd2-3ac4-834c-7107d17b61ed | -8.1875 | -45.781 | 2026-10-08 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fa092481-569f-3ad0-aa13-5ec26ab8c5c6 | -7.5286 | -45.8659 | 2026-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| fcc71d67-ad95-3295-8a3a-92c44ea03166 | -8.1876 | -54.7219 | 2026-10-08 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 93187e18-ca4c-3d30-9b62-d071d53daa84 | -6.7366 | -55.1274 | 2026-10-08 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b429b45c-148b-3f75-a43b-600a8f8bfb31 | -11.6186 | -43.6433 | 2026-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 710.3 |
| 3dceb138-7d52-3a4c-ad21-4e4ce4d4c6a8 | -9.1543 | -49.8142 | 2026-10-08 13:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |


[Clique aqui para ver as próximas entradas](README212.md)
