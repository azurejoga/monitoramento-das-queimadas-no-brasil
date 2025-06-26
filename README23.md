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
| ebe88c91-56b9-3a0c-8a8d-0fe0aa7449cf | -9.1213 | -49.4313 | 2025-06-26 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 303.5 |
| eddcbf3e-77b8-3282-8525-36aa659e9ba3 | -9.1025 | -49.4331 | 2025-06-26 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 24da286b-4819-35c6-ae59-28729490f02b | -14.2247 | -45.5036 | 2025-06-26 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| c26b3e56-128b-32fd-9fd4-a97f6a07eb6a | -6.118 | -42.5323 | 2025-06-26 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 5e1fbb32-4adf-3c47-8779-11db4c5c9455 | -8.8195 | -45.0108 | 2025-06-26 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 1f903136-60ef-34bf-b290-00d2bd796576 | -8.8006 | -45.0128 | 2025-06-26 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| fe8f3760-b281-3195-8855-38ab487594b7 | -10.5107 | -47.2065 | 2025-06-26 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 6e074a61-5e43-35e3-8475-78d6ffdae0aa | -14.2057 | -45.4838 | 2025-06-26 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 178.5 |
| d08dbc1b-1817-3917-b0b4-24239bff0580 | -14.2052 | -45.507 | 2025-06-26 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 369.9 |
| 02d20000-683a-399a-b504-34a6c6b5ee43 | -9.121 | -49.4528 | 2025-06-26 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 77061f01-ab1d-390a-8065-e7fd6e2ef2fc | -8.8198 | -44.9879 | 2025-06-26 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| e73f520e-64ce-3bfd-b28f-901824ca3ef9 | -14.2052 | -45.507 | 2025-06-26 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 331.1 |
| 03ee06d0-e41b-3d23-83ed-7ae64240accd | -8.8195 | -45.0108 | 2025-06-26 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d134172c-f3dc-3069-a1e6-582d8e56d96d | -6.118 | -42.5323 | 2025-06-26 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 158.2 |
| 274cd592-ef40-3484-8667-4ae642197894 | -8.8009 | -44.9899 | 2025-06-26 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d4ed135d-3041-3fb4-a63d-9c5ba28cc1a9 | -14.2247 | -45.5036 | 2025-06-26 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 319.2 |
| 54750c5d-ee62-35e3-9338-eb9cbf7b37eb | -9.1025 | -49.4331 | 2025-06-26 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| d8b4b8b6-1167-39e3-bf09-d23b0965cef0 | -9.1213 | -49.4313 | 2025-06-26 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 327.4 |
| b6645bf3-e87a-30ea-8cb5-aa1659b1448d | -9.121 | -49.4528 | 2025-06-26 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 364d1cdf-f72b-3c49-8bf4-f3518a32d160 | -14.2247 | -45.5036 | 2025-06-26 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.3 |
| e6cad8e7-5b17-30fb-a377-16c0ec9c6532 | -9.1213 | -49.4313 | 2025-06-26 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 300.5 |
| 7efd5089-2ffd-329d-bdf4-736a884c1316 | -14.2052 | -45.507 | 2025-06-26 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 359.8 |
| 7cfb4bed-9356-3c0b-b6ef-de5750c65475 | -12.537 | -57.1814 | 2025-06-26 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0e663b2e-56f8-33e3-b131-0729742ad7da | -8.8006 | -45.0128 | 2025-06-26 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9fbd8bf2-5c09-3fe9-bbdb-8579704a7e2f | -8.8195 | -45.0108 | 2025-06-26 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c30ddc94-599a-391a-bcfb-df6600dc8265 | -9.1025 | -49.4331 | 2025-06-26 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 10e4852d-6186-3886-9dea-0934731c3adb | -9.121 | -49.4528 | 2025-06-26 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 9ec0b3f5-93d9-3125-8e64-5f7261b9e64c | -9.1213 | -49.4313 | 2025-06-26 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 319.3 |
| 47d6306a-478b-3b42-9a6d-41048a7728d9 | -14.2247 | -45.5036 | 2025-06-26 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| c6bf46c2-772b-3336-a081-f29c6f3919f7 | -12.537 | -57.1814 | 2025-06-26 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 311d91e9-3077-3d01-b0e3-383d495adc6a | -14.2052 | -45.507 | 2025-06-26 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 344.6 |
| 29f0ac66-6ba4-31ff-b269-451cbb3a5300 | -9.121 | -49.4528 | 2025-06-26 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 3d1888c4-2509-3e68-a528-dc110669bd57 | -8.8195 | -45.0108 | 2025-06-26 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| bf31c753-b096-369e-8030-2e115971acaa | -8.8006 | -45.0128 | 2025-06-26 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| a611173b-d172-31d4-8d27-ee785e7ba319 | -9.1025 | -49.4331 | 2025-06-26 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 35766cf8-132f-3195-84a9-2cf07df73c6a | -9.1213 | -49.4313 | 2025-06-26 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 275.9 |
| d13fa508-657e-3b47-9b22-4a7e57d15bfc | -14.2052 | -45.507 | 2025-06-26 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 415.0 |
| 5200a561-1123-326b-b9a6-4e089b246701 | -12.518 | -57.183 | 2025-06-26 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c3ba880e-19aa-34d4-a30a-435ad07b02d2 | -6.118 | -42.5323 | 2025-06-26 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 31cc9a86-6aa3-3686-a8b0-c9cd9ccac36f | -14.2247 | -45.5036 | 2025-06-26 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 234.0 |
| d6701f01-c8ad-30bc-9370-a0e4e72b13b1 | -9.121 | -49.4528 | 2025-06-26 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 51f3b514-c5b5-3ecf-8b61-1df5a7ef212f | -8.8198 | -44.9879 | 2025-06-26 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c7133ab0-858c-3e37-97e4-7776fe505685 | -9.1025 | -49.4331 | 2025-06-26 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 1830c535-18aa-3994-ad5f-74cbcf0b65fa | -8.8195 | -45.0108 | 2025-06-26 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 4507fcad-1f7f-3497-9ee8-0ccbaad5d500 | -11.1407 | -47.0169 | 2025-06-26 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| e3577ad7-7f29-375a-b9ca-3e3eb3c5fae4 | -12.537 | -57.1814 | 2025-06-26 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ab0a1a79-ce9d-3b9d-b723-f55a04ec4280 | -9.1213 | -49.4313 | 2025-06-26 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 309.7 |
| 301054a4-fb1e-383d-9078-33c40b7ddc6b | -11.8156 | -57.3612 | 2025-06-26 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 73374129-b6df-3e4d-b9e1-8bb19766235b | -11.1404 | -47.0393 | 2025-06-26 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 09576cce-4047-3a02-80c8-4a735f790c37 | -11.7967 | -57.3627 | 2025-06-26 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ad9092e0-feee-3994-b1a6-5b63c2b68c58 | -9.121 | -49.4528 | 2025-06-26 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| d07c6cb7-df39-3a57-92ce-141a45ce7532 | -9.1025 | -49.4331 | 2025-06-26 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 37c25c71-12bb-3df9-a124-1ef729850fd8 | -14.2052 | -45.507 | 2025-06-26 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 296.9 |
| be6a4500-d0a0-3891-9a5d-b6f63a0e6d44 | -9.1573 | -46.5793 | 2025-06-26 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |


