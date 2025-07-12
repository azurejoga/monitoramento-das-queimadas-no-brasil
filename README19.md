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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 513ac0de-b281-38b4-a582-8faec2157cb4 | -5.8413 | -48.3748 | 2025-07-12 07:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6b32b860-94f9-3ac4-ab85-d6046c473a71 | -5.8412 | -48.3964 | 2025-07-12 07:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9d258c89-7421-3920-b36e-ace8649c99a2 | -12.8813 | -49.1758 | 2025-07-12 07:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9c706aed-b254-38d5-b8f8-a63d345908cb | -12.8809 | -49.1977 | 2025-07-12 07:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 7f477dd7-150c-35e2-961f-dbcb4fd8e06e | -5.8598 | -48.3953 | 2025-07-12 07:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a796076b-db75-3dc3-bd2b-6bcd7b739632 | -5.8412 | -48.3964 | 2025-07-12 08:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 687f98b2-78b8-35d9-a7d2-b8a91ccd7335 | -12.8809 | -49.1977 | 2025-07-12 08:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 218667a2-d55c-3d87-a7b8-988d306a3dbc | -12.8813 | -49.1758 | 2025-07-12 08:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 496eb70f-e1db-3c05-9bc9-d31e8d248fff | -5.8413 | -48.3748 | 2025-07-12 08:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 3ca87ec0-3e6e-3519-9457-f2340d0a69ee | -5.8598 | -48.3953 | 2025-07-12 08:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 23a000b2-f2cd-3300-b3ae-a26136eed5f5 | -12.8809 | -49.1977 | 2025-07-12 08:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| e482e2f6-eaef-3354-bbce-343a05d5f52c | -12.8813 | -49.1758 | 2025-07-12 08:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| fe1931af-5740-3bba-891c-4b8ead985fd2 | -12.8813 | -49.1758 | 2025-07-12 08:20:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 58c9660a-d85e-3938-9f5b-6089fd41bb96 | -12.8813 | -49.1758 | 2025-07-12 08:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 6e88ef31-13c8-31d8-be9a-92bec931b36d | -12.8813 | -49.1758 | 2025-07-12 08:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 62d864b7-6909-3325-9f35-829030903aba | -12.8809 | -49.1977 | 2025-07-12 08:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e1b3c4e0-ab69-3af0-a2b3-bdcaad6325b3 | -12.8813 | -49.1758 | 2025-07-12 09:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 7baa2a45-9b76-35ff-af26-75a62efa226d | -12.8809 | -49.1977 | 2025-07-12 09:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 1dc20dee-b1c9-3d9a-b4dc-c8041e51ab0a | -12.8809 | -49.1977 | 2025-07-12 10:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 4980a5ce-34e3-37cd-8c4e-cf1883f8f65d | -12.8813 | -49.1758 | 2025-07-12 10:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d5f7d5f1-b095-3318-8543-d94ad7e9f43f | -11.4367 | -46.3934 | 2025-07-12 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a1dde9c3-e3be-39ec-acb2-3c3b037db5d6 | -8.9213 | -47.3374 | 2025-07-12 12:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9aea5ed6-2d6e-31b7-8142-4de200c44670 | -6.485 | -45.2554 | 2025-07-12 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c11f2bce-1b81-3d66-8260-1c71e9745a2e | -8.9213 | -47.3374 | 2025-07-12 12:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d307c987-1736-3ba4-bed8-9258cf1558c5 | -8.9213 | -47.3374 | 2025-07-12 12:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| d60b0f31-28ad-3a1c-9816-9fb80cd0af2e | -12.4862 | -44.4928 | 2025-07-12 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 4f3154cd-a62d-3bdf-bcb6-2fcb737cbac1 | -8.921 | -47.3595 | 2025-07-12 12:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 972e9d9d-ba47-3fbd-bd5a-d986f6a861d6 | -6.485 | -45.2554 | 2025-07-12 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 5c3cc2c6-6f44-367c-ad63-8da84f3cfcf5 | -12.4669 | -44.4959 | 2025-07-12 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 87e37119-437b-3c56-999d-fb368d32441d | -4.81476 | -45.25001 | 2025-07-12 12:46:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| bb673c02-3cad-349f-b0f5-267f2416f0a1 | -3.6896 | -47.42951 | 2025-07-12 12:46:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4918e924-8ac4-3e85-a059-3fb5cc9964e0 | -3.7589 | -47.10728 | 2025-07-12 12:46:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ef77458b-9443-35b6-ad2a-de069ef1dd7f | -4.81611 | -45.28037 | 2025-07-12 12:46:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 4a459c09-c523-3511-9f23-cfc9804bf018 | -4.55047 | -48.00934 | 2025-07-12 12:46:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| bee4cb5f-3cd0-3ddf-98d8-77451ab1f7e9 | -4.81144 | -45.27456 | 2025-07-12 12:46:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 217.9 |
| e77cfe51-1032-39f2-88ff-c62966b6a4b0 | -3.78722 | -50.8336 | 2025-07-12 12:46:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| eceb95f0-9f02-3dbb-babc-cf7864f70194 | -4.80818 | -45.29863 | 2025-07-12 12:46:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 358e1d8a-ecb9-3a9c-944f-732ccfab4f2f | -4.28457 | -46.93506 | 2025-07-12 12:46:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 19b8472c-8cce-3f26-9c86-387abfdab1c7 | -4.80201 | -45.27866 | 2025-07-12 12:46:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 8949bfe6-b81f-3eef-bcb3-3a3b3223f57a | -4.27517 | -48.1799 | 2025-07-12 12:46:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 32ef6c4a-9202-310e-bea0-e948ab3845d5 | -10.90706 | -49.21097 | 2025-07-12 12:49:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 982bb09b-04eb-3fd8-ae66-c16e83043b4f | -11.84334 | -47.51274 | 2025-07-12 12:49:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| bc6b09e8-b435-3647-941c-8e2111385c6c | -12.88009 | -49.17875 | 2025-07-12 12:49:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d360b6b5-41fc-3fe8-bedc-e66ead5917f1 | -12.87809 | -49.19503 | 2025-07-12 12:49:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bf2085c2-7e4b-3d1c-94b8-a652df8dbf4c | -10.34917 | -49.91545 | 2025-07-12 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b21a593b-c828-3c78-a70e-cd7b61062ccf | -13.17633 | -53.56672 | 2025-07-12 12:49:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2cb5b805-299a-3a8c-93ce-560d5137e03b | -12.89178 | -49.18018 | 2025-07-12 12:49:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b4abff89-8a7e-3e8d-aefb-f9c92862bb9e | -6.48792 | -45.27064 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 6164ed16-fde9-3a06-a393-3cbed580efa8 | -8.31843 | -44.9337 | 2025-07-12 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 5293af26-b481-32d8-aac9-de0fb0836203 | -6.44319 | -45.36433 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9366c80a-e7ff-38eb-addb-edc6f0689717 | -10.85077 | -49.11156 | 2025-07-12 12:49:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9d59acce-1f63-3455-b730-8739ab5555b7 | -12.48733 | -44.49258 | 2025-07-12 12:49:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 71503d59-cb1c-3356-9789-7536fd6c674f | -8.91314 | -47.35233 | 2025-07-12 12:49:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 58a40c17-00cc-3b18-a670-997a1897027c | -6.49128 | -45.24397 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 6991000d-dc12-361a-bd31-86322a2047ac | -11.44762 | -45.09908 | 2025-07-12 12:49:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 051fa29f-2632-3a82-b457-da4667b5a526 | -11.43357 | -46.42365 | 2025-07-12 12:49:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 455e26c0-2bd2-38de-96b7-af1f2c99d15f | -11.93434 | -51.68309 | 2025-07-12 12:49:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d49b97cf-3635-3e17-9661-27809c1b6d0e | -13.61543 | -55.45179 | 2025-07-12 12:49:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c50047b4-aed6-332a-b54a-10e859eaa50d | -6.71938 | -45.23248 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 5e4a1859-d4e7-3299-b0d9-ef77752a582b | -6.72069 | -45.23911 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 4c052c4a-c878-3bca-aa22-0b68cc9a23cd | -7.0845 | -49.60136 | 2025-07-12 12:49:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d147c654-4e85-3c29-ab9f-c8d5b934e8e3 | -9.13387 | -47.57361 | 2025-07-12 12:49:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cc615f71-8d10-3880-9040-162eeef7d014 | -10.50985 | -53.58153 | 2025-07-12 12:49:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 925d63c8-2cf3-360b-bfbb-9ca30cb986ab | -7.48149 | -47.51598 | 2025-07-12 12:49:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e7d33354-6045-3ad0-b34a-a8ee56d51480 | -10.05977 | -46.73036 | 2025-07-12 12:49:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ceaf28b0-4d42-38c9-b81d-42ed683b5e06 | -3.871 | -54.23097 | 2025-07-12 12:49:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f72928ff-d44a-3679-b868-98bd6097758c | -7.46924 | -47.51435 | 2025-07-12 12:49:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8774d2b9-4ff1-3f59-8fe5-7b36d9c42357 | -6.43191 | -45.36779 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 329e327d-1800-3a64-a2fa-b790f70565ad | -9.92265 | -52.4434 | 2025-07-12 12:49:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a11defc2-9bfc-3be7-a212-8047c5b7b5e5 | -11.73049 | -47.47149 | 2025-07-12 12:49:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| bfe2f96c-04ea-359c-ad53-d846e9b287bc | -12.47516 | -44.49858 | 2025-07-12 12:49:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 7e109409-b668-32e3-ba3a-0a1deb7dcbad | -11.43642 | -46.39859 | 2025-07-12 12:49:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 87c68ff4-7126-3ff6-9bf9-3bed4dc501c6 | -9.91319 | -52.44572 | 2025-07-12 12:49:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| db1eb8a7-26a4-3e60-b4ca-e2f32de7c0b1 | -8.34192 | -45.62747 | 2025-07-12 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| a1460694-467d-30b3-8aa9-c4b841b6ab29 | -5.7771 | -43.62021 | 2025-07-12 12:49:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 07e7baec-4b74-35cc-88dd-b3ad7537b80e | -8.92585 | -47.35397 | 2025-07-12 12:49:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c8f8190c-7e0f-30e4-bd7d-ebf5fe828341 | -5.98141 | -43.76772 | 2025-07-12 12:49:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 2e30d3e3-4c18-3b8e-a8d7-d01e32d29e0f | -10.67453 | -49.49691 | 2025-07-12 12:49:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 912d461a-7c0e-32e2-9f41-09aa693840d4 | -14.35393 | -53.37651 | 2025-07-12 12:49:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 949d9087-501e-3d88-9661-36ffb1ebabbc | -11.7331 | -47.44988 | 2025-07-12 12:49:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6ff4d540-f844-39a5-8142-d2c0274a5e63 | -14.68618 | -52.68343 | 2025-07-12 12:49:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 96181d00-5789-384d-b826-4f10397b2f86 | -12.47055 | -44.49076 | 2025-07-12 12:49:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 4a2047db-fa66-3c41-b1bb-c117c162de03 | -10.57494 | -49.11963 | 2025-07-12 12:49:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b0eae717-4c67-32d3-a295-43937dddf478 | -7.61146 | -49.94283 | 2025-07-12 12:49:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d78c0c08-0fee-3102-93a3-014a8e0cb1c8 | -11.84063 | -47.51832 | 2025-07-12 12:49:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3883b26d-d13c-3e66-b8ca-6d5940174a0e | -12.07784 | -49.0066 | 2025-07-12 12:49:00 | TERRA_M-T | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1e05c9bb-bfd9-37b7-bd30-ed925a0e7391 | -6.63192 | -56.28129 | 2025-07-12 12:49:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c51b6f5f-354c-3dcc-9d56-746f5526106f | -6.43502 | -45.34239 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 7014d360-4ea1-3695-b019-936e937662a8 | -10.8958 | -49.2093 | 2025-07-12 12:49:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9a5d2c87-48d5-312a-a6ed-c2a0669ce446 | -14.34952 | -54.46684 | 2025-07-12 12:49:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2116ce65-5a47-3aa0-a51b-e23fa00a5180 | -6.48566 | -45.26487 | 2025-07-12 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| be77a157-7514-32a8-b434-a2160c325ead | -8.92868 | -47.34005 | 2025-07-12 12:49:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8da07ae0-ab64-3e8c-8360-0a43cbdffbde | -6.09609 | -47.78391 | 2025-07-12 12:49:00 | TERRA_M-T | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2a222977-9e73-3d8d-b43b-8d1a7ef9063d | -7.08622 | -49.60776 | 2025-07-12 12:49:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 098db144-8efd-3fbf-85fa-8106a5dda590 | -12.58104 | -56.97751 | 2025-07-12 12:49:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7a7cd142-1106-3f33-97a0-c65ad85450d3 | -6.27388 | -43.42488 | 2025-07-12 12:49:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 98558fc4-60ae-3b09-a78b-853b7141cb00 | -10.18166 | -49.50286 | 2025-07-12 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1ec0ef6b-6297-30d8-88c8-7b55b96e6e1a | -12.47911 | -44.4608 | 2025-07-12 12:49:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 02d10224-506c-3537-8399-b6e1831cd980 | -11.42994 | -46.41734 | 2025-07-12 12:49:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e1660896-a9d9-34ad-8abc-5c81273ed6ec | -8.92631 | -47.35957 | 2025-07-12 12:49:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |


[Clique aqui para ver as próximas entradas](README20.md)
