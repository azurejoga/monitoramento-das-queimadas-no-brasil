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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bb5a82a-a1b5-374d-aa8c-140a50343b61 | -8.5587 | -46.2162 | 2025-10-09 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d78a0946-6265-3cec-8e50-25dc54db98b6 | -5.3999 | -40.9856 | 2025-10-09 02:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 267.5 |
| eada88bf-001a-33bf-b3f7-07d4abd34204 | -6.6806 | -46.3184 | 2025-10-09 02:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 36b3bb56-e030-39a5-9cfd-cceb0c6f8842 | -10.8558 | -44.6199 | 2025-10-09 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| f57f58fc-30b9-3fc4-b5e0-61f3fb331523 | -5.3999 | -40.9856 | 2025-10-09 02:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 136.2 |
| a3ca1156-6422-3a53-a640-960a88690fb8 | -10.8554 | -44.6431 | 2025-10-09 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 2451015b-a1bf-3813-9ae0-a515776afb5b | -6.6995 | -46.2946 | 2025-10-09 02:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 481780d4-bc9c-3acd-8df1-a76d34a329f8 | -14.4133 | -43.9911 | 2025-10-09 02:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fba349cc-45d9-30e1-b8f8-38041b99602b | -17.6421 | -47.1871 | 2025-10-09 02:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 55bed841-49d2-3144-abb3-740f71f80d74 | -14.4334 | -43.9635 | 2025-10-09 02:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 1650ea43-82de-36f2-9c08-68f14fdc4212 | -8.5398 | -46.2181 | 2025-10-09 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 149d6892-a470-3a90-a357-dccde2b46dc4 | -14.4329 | -43.9874 | 2025-10-09 02:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| aeddf028-f6c7-365f-bdc9-a6f4e6843bc0 | -8.5021 | -46.222 | 2025-10-09 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f6c41c1e-24fb-3e44-a765-9e9ece869c0d | -8.1993 | -43.3424 | 2025-10-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 1c0b95df-4511-39a1-8698-a64faa43c971 | -13.7909 | -45.8552 | 2025-10-09 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8a9a378c-fb04-36e7-9bcb-d059ffc6a33e | -7.7755 | -44.0396 | 2025-10-09 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 3cee52cd-5d8d-372b-b3c9-c0c079ac19a9 | -10.8749 | -44.6172 | 2025-10-09 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f2d4ef4c-ab31-35bc-acf2-290639ca4401 | -14.4138 | -43.9672 | 2025-10-09 02:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 27ce9052-4e53-3613-80f0-2fabec274e6b | -8.5587 | -46.2162 | 2025-10-09 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| dcc75757-f37f-38c4-b86d-2af843c236a3 | -6.6808 | -46.2961 | 2025-10-09 02:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 0be1ddba-084a-30ba-a330-3269040ceb0b | -7.7567 | -44.0415 | 2025-10-09 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 88692a02-c658-3d80-b1ba-3ebb4b77b2ae | -18.4118 | -45.2394 | 2025-10-09 02:30:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 5f50b312-8522-3cc0-ba99-d59f9bd18c47 | -13.7913 | -45.8321 | 2025-10-09 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5ce72bbe-63ae-3278-a5fa-30ccf65ffd56 | -5.4001 | -40.9613 | 2025-10-09 02:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 89763b93-82a8-3438-99f2-e926c335e3b8 | -18.4125 | -45.2155 | 2025-10-09 02:30:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 8025c264-fd0f-3f31-8b90-c27cf85ff2d8 | -6.6993 | -46.3169 | 2025-10-09 02:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 30d20981-7ffc-3348-8606-ebea7cc97c13 | -10.8554 | -44.6431 | 2025-10-09 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| a198795e-421b-351d-9ac2-e15e42bf5efb | -11.666 | -47.5288 | 2025-10-09 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4efa8d47-f366-368b-9aff-6fd86a629667 | -6.6806 | -46.3184 | 2025-10-09 02:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 590fe100-8db0-38ae-816a-374ccf1fb3ea | -5.3999 | -40.9856 | 2025-10-09 02:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 2d81d212-3c04-3c0f-a0c7-4e4c57d0c8d6 | -10.8558 | -44.6199 | 2025-10-09 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| cbaf7be4-c697-3339-892d-50c185980152 | -7.7567 | -44.0415 | 2025-10-09 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 4f226e41-f2b8-3965-b7f4-64e06cf043ef | -14.4334 | -43.9635 | 2025-10-09 02:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4eb5893a-5a74-31b6-ae48-99a7a7ba5f8b | -17.6421 | -47.1871 | 2025-10-09 02:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e4282f12-4c65-3edd-87e8-608f49fdf898 | -6.6995 | -46.2946 | 2025-10-09 02:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 708a6e70-8534-375a-8faa-29095aef7c76 | -8.1993 | -43.3424 | 2025-10-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 8cb5911f-0396-359b-adeb-5e0256ac20ea | -15.0579 | -42.3424 | 2025-10-09 02:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 62a00fe7-9e02-3edc-b12c-bb093543d907 | -10.8749 | -44.6172 | 2025-10-09 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 99fae7eb-c49d-398d-9cca-683fe84bd1a5 | -7.7755 | -44.0396 | 2025-10-09 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 38064606-fe71-3ef6-9163-69656d99b6e3 | -15.0585 | -42.3178 | 2025-10-09 02:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 328b4e23-45b6-37d0-901b-c8501f201a1a | -6.6993 | -46.3169 | 2025-10-09 02:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4aae2aa9-89ab-3777-a759-a80c69d571b5 | -14.4138 | -43.9672 | 2025-10-09 02:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c405416d-104e-3adf-ae02-aec0812f7556 | -18.4118 | -45.2394 | 2025-10-09 02:40:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 7f70bc14-f47a-34d5-8388-7727617d3a84 | -14.4329 | -43.9874 | 2025-10-09 02:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3fa8b02f-1dd5-36e3-bc1d-650771168027 | -6.6808 | -46.2961 | 2025-10-09 02:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| bacd74bf-ec31-3c8b-bc8e-e87de088d2e0 | -17.3771 | -46.6636 | 2025-10-09 02:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f26edef4-92e1-3935-b81c-14d0215c68c9 | -15.0579 | -42.3424 | 2025-10-09 02:50:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 5431e34b-5cf5-39b0-8d0d-c6a4585c101c | -6.6995 | -46.2946 | 2025-10-09 02:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 116d2236-3bd0-385b-9f99-7fa8b1afaa5e | -10.3549 | -50.2099 | 2025-10-09 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 2f7e6e5a-43c7-30ad-96a4-1ff0eb777133 | -18.4118 | -45.2394 | 2025-10-09 02:50:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 9c3aa96c-3bb0-3c5c-9785-d5c1757ea7f6 | -10.8558 | -44.6199 | 2025-10-09 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 5ad83d76-e172-3c5a-a6dd-286849ddfedb | -14.4334 | -43.9635 | 2025-10-09 02:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 9b421898-1130-3139-ab33-a15f3584f235 | -15.3591 | -47.0953 | 2025-10-09 02:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ecb63130-0d5a-33c2-a821-b25f42fa0dae | -15.3782 | -47.1147 | 2025-10-09 02:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 00cd0cc0-ef86-3456-b7e9-26360448ee44 | -6.6993 | -46.3169 | 2025-10-09 02:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6975ee10-8633-39da-a910-1ace3cccfc8d | -15.0585 | -42.3178 | 2025-10-09 02:50:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 1bcd4def-0d03-3f6c-8918-19ccf3515a7e | -18.0388 | -44.9679 | 2025-10-09 02:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b5835f72-9964-3cd3-b759-006cb823ddeb | -15.3787 | -47.0918 | 2025-10-09 02:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 15b522b0-10a0-3197-8a93-2585404103e5 | -9.0829 | -47.9594 | 2025-10-09 02:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 187caebb-174a-3389-ab28-1ac94f0294a7 | -14.4329 | -43.9874 | 2025-10-09 02:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ca557125-5cd8-3d13-bbd0-99e8899a209e | -14.4138 | -43.9672 | 2025-10-09 02:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b3444b8d-545a-3685-8e67-a2ba016cf949 | -7.7567 | -44.0415 | 2025-10-09 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ff1af7aa-8d5d-37a8-ae37-fccd0ff0021b | -10.8554 | -44.6431 | 2025-10-09 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e0185e94-90f0-3ac2-a208-5fc1dde1e75c | -8.1993 | -43.3424 | 2025-10-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 29aa9de2-b46f-3434-af8a-ecfca5121255 | -9.191 | -46.8881 | 2025-10-09 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 96a2246f-c39a-39ce-be0e-c38985a1ea76 | -6.6806 | -46.3184 | 2025-10-09 02:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a6742841-7d6b-3afc-b764-9f0d95d02b5f | -6.6808 | -46.2961 | 2025-10-09 02:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| ade31d9d-8b41-3562-8f24-56c12c62c8aa | -18.0589 | -44.9632 | 2025-10-09 02:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 358bf278-a43d-324b-8a0c-5cf0ebcaa02f | -5.3999 | -40.9856 | 2025-10-09 02:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| d410f0a9-c2b3-339c-81f0-dda79fc7dcbc | -18.0413 | -50.4511 | 2025-10-09 03:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 65814b84-a2c2-3899-befa-ed72492cfb17 | -14.4138 | -43.9672 | 2025-10-09 03:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 714f7afe-0344-386d-af53-3c63bc3a6fa2 | -18.0208 | -50.4769 | 2025-10-09 03:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e3d7dd06-f3cd-3655-a50b-5733ea80a507 | -18.0213 | -50.4547 | 2025-10-09 03:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f5d226bf-d194-3d60-9d67-50f06499ab5b | -8.1993 | -43.3424 | 2025-10-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| e6256682-88d7-3748-b145-6a1bc29e0d7b | -17.6415 | -47.2103 | 2025-10-09 03:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| acf034ef-98ed-3026-bea8-c8a5afad8cde | -10.8558 | -44.6199 | 2025-10-09 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e2773be2-2df9-330e-aee6-adc5cbf6197e | -6.6808 | -46.2961 | 2025-10-09 03:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 12ac2c65-a34c-3593-993d-f12e1644215f | -6.6993 | -46.3169 | 2025-10-09 03:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 92584812-5f1d-3220-9ba8-f561d6b0dc15 | -18.0589 | -44.9632 | 2025-10-09 03:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 172.9 |
| aa484a42-2c94-32f5-a838-eea579689ca3 | -6.6806 | -46.3184 | 2025-10-09 03:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6c82a58d-2c9c-3809-acc8-997f76a4e4c8 | -14.4334 | -43.9635 | 2025-10-09 03:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 69a4ff6e-02c4-3ee1-a432-fa14271a2c0d | -18.4118 | -45.2394 | 2025-10-09 03:00:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 135.7 |
| b275bf6b-2a25-38c2-8443-eaecb710a4dc | -18.0388 | -44.9679 | 2025-10-09 03:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 726512f4-5e04-3c3e-93d0-3d9795fc3dec | -15.3787 | -47.0918 | 2025-10-09 03:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 706ab2a8-b5af-30c5-98b8-9094d7cc069b | -9.191 | -46.8881 | 2025-10-09 03:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0f21299b-a26e-3d30-8b32-f13e85781ff2 | -17.6421 | -47.1871 | 2025-10-09 03:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 226ca8db-a335-3aef-95cb-61f3d29a3cc3 | -6.6995 | -46.2946 | 2025-10-09 03:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 866d8721-3a55-3a3c-b47f-1250b4c117b9 | -18.0408 | -50.4733 | 2025-10-09 03:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 859cbba4-4735-37dd-8edb-00919f0199cf | -18.0208 | -50.4769 | 2025-10-09 03:10:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 87172041-f7f0-3e65-a4e1-667509e4ee4d | -18.4118 | -45.2394 | 2025-10-09 03:10:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 9908261f-905e-3596-8ce7-277196253e98 | -10.5461 | -50.0402 | 2025-10-09 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 866b1348-b06f-3651-889c-c6cc4ff17adc | -8.521 | -46.2201 | 2025-10-09 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cdf30043-30e1-3ee9-bf88-e02cc16533b2 | -18.0413 | -50.4511 | 2025-10-09 03:10:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ca1a2501-ebc1-313a-938e-b45d7e7d1e62 | -10.5275 | -50.0208 | 2025-10-09 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 5bc39792-238b-3e0a-a12e-492b92ecdb50 | -14.4138 | -43.9672 | 2025-10-09 03:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8e21bf26-73dd-3981-8981-d126efff2f17 | -10.5272 | -50.0422 | 2025-10-09 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 0bf03aa6-6e0e-32d7-9a6e-37c25b78f4b4 | -8.5398 | -46.2181 | 2025-10-09 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| aa3940b4-e13a-39e1-9615-0558a3588b25 | -6.6995 | -46.2946 | 2025-10-09 03:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 7d63dc28-108d-3c98-b34f-aee122e5922e | -18.0408 | -50.4733 | 2025-10-09 03:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3e8ab7ac-bc10-310d-a185-56f3f5a2842b | -6.6993 | -46.3169 | 2025-10-09 03:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |


[Clique aqui para ver as próximas entradas](README9.md)
