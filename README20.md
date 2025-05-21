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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a65de387-36cb-3e71-8941-10d19a45d6d2 | -12.3137 | -52.4764 | 2025-05-21 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fc97f158-8cdb-3425-97db-f143dea21a4d | -12.294 | -52.5205 | 2025-05-21 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 97aab032-9ca2-32d7-a998-70a4939ad6bb | -12.48 | -57.1863 | 2025-05-21 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 275.8 |
| 0ea4e1a3-6fdb-3bc3-a11d-db200f0b66a3 | -12.294 | -52.5205 | 2025-05-21 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d63e2a39-e964-3050-8453-37a4887b7b7c | -12.3515 | -49.9833 | 2025-05-21 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 277.6 |
| 6dc8eae8-43ff-3b8e-bc39-15495d21055e | -12.499 | -57.1847 | 2025-05-21 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 361.8 |
| 98eba8c4-a6bd-34fc-86f3-04b7fabe8a99 | -12.3324 | -49.9857 | 2025-05-21 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 6db0331a-7a4a-33f9-b653-0a1a81ff1cc1 | -12.3519 | -49.9617 | 2025-05-21 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 97f011fb-991f-397a-b92a-11217f4abd6e | -12.3706 | -49.981 | 2025-05-21 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 4623fad7-e551-36d5-a524-30d4f2eaeceb | -12.3134 | -52.4974 | 2025-05-21 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 10becb30-141a-3a3a-937f-abd10189b3f0 | -12.2946 | -52.4785 | 2025-05-21 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 337.1 |
| 7ccfcb1d-364d-30f6-9f58-dcd8edb69f68 | -12.48 | -57.1863 | 2025-05-21 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 261.1 |
| a18e9966-bdd8-307f-968f-7a9618153105 | -12.2943 | -52.4995 | 2025-05-21 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 461.2 |
| 0f9222c8-ecae-30a9-99d4-94eda8f49d1a | -12.3137 | -52.4764 | 2025-05-21 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a4fa0165-b112-320f-9ecb-b2bb0b75c74d | -12.3327 | -49.9641 | 2025-05-21 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 197.8 |
| d68681e2-c29a-35a9-8e72-b2dbe08a7d9b | -12.294 | -52.5205 | 2025-05-21 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e903f03e-9d79-368e-940c-61e0ea066016 | -12.3327 | -49.9641 | 2025-05-21 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 16388fd6-7d79-3b6c-abaf-d860bd27abba | -12.2946 | -52.4785 | 2025-05-21 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 265.3 |
| eb149ce4-f191-3bb1-8ad3-3e91c1b53f8f | -12.4798 | -57.2063 | 2025-05-21 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ef77354d-e376-383e-9ebd-49471cef1f31 | -12.3137 | -52.4764 | 2025-05-21 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 1dd15e05-a0ba-3b2d-a1af-7bc94eb9291a | -12.371 | -49.9593 | 2025-05-21 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6518a1d5-255a-3e1f-b91f-ff3dff23d8a5 | -12.2943 | -52.4995 | 2025-05-21 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 396.6 |
| 3c2b84a0-d2fb-35b9-a1eb-69ad6f9ba176 | -12.3519 | -49.9617 | 2025-05-21 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 237.9 |
| eafbce52-81e2-38a1-b33d-2ee4fcbddd86 | -12.48 | -57.1863 | 2025-05-21 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 332.7 |
| bebab1d1-fa6e-3aa0-94c2-8ff00ad9c824 | -12.3515 | -49.9833 | 2025-05-21 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 263.5 |
| 4f926acb-1971-36bd-965d-5a2dd7813ab0 | -12.3134 | -52.4974 | 2025-05-21 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 0cfc4640-6f57-3a07-83cf-4a79edcfb4bb | -12.3706 | -49.981 | 2025-05-21 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 43c71964-717f-3bf1-b6d1-f36d3bb871f2 | -12.3324 | -49.9857 | 2025-05-21 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 28ebbc77-f682-314c-b40b-654291e49a10 | -12.499 | -57.1847 | 2025-05-21 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 245.9 |
| 074a2622-c02a-3f0c-b203-6bd2383d6d6b | -12.48 | -57.1863 | 2025-05-21 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 310.6 |
| 7c420727-4d25-3b55-a531-0b8a566c4225 | -12.3706 | -49.981 | 2025-05-21 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 843dea86-22d8-3c55-b757-e79ea786d6ab | -12.3327 | -49.9641 | 2025-05-21 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| d35ebe58-408c-39bb-a04f-058a1feaff21 | -12.3519 | -49.9617 | 2025-05-21 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 202.7 |
| 73479496-e4d2-3564-ab26-a9984bc3345b | -12.499 | -57.1847 | 2025-05-21 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 201.7 |
| a82a64e6-d82f-3542-874a-06263be36574 | -12.3324 | -49.9857 | 2025-05-21 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| bc1edc19-b3c2-3698-8796-5405c7b11619 | -12.3515 | -49.9833 | 2025-05-21 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 266.3 |
| d7aa492a-5656-39c2-bf99-6008ba9144ab | -12.3519 | -49.9617 | 2025-05-21 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 174.9 |
| f46d2b1d-043b-3cd6-a606-5b388c4f804a | -12.3324 | -49.9857 | 2025-05-21 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| fe594407-d64f-3df9-9e1a-d95738b61f26 | -12.3327 | -49.9641 | 2025-05-21 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| ef4fe476-c8bc-31e3-9c1d-1bec72c24dcf | -12.3515 | -49.9833 | 2025-05-21 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 57ab950a-ec36-3cd9-bd95-90914e5347d4 | -12.48 | -57.1863 | 2025-05-21 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 179.8 |
| ef72859d-1032-3009-a33c-cb221570e465 | -12.3137 | -52.4764 | 2025-05-21 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 41706858-711c-3c81-8980-13671e7fed39 | -11.5881 | -47.6279 | 2025-05-21 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bc9cc6a9-8000-3858-b88e-654f9baa2325 | -12.499 | -57.1847 | 2025-05-21 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 241.2 |
| 520df508-e45f-3a4f-b20c-96601852bc4a | -12.294 | -52.5205 | 2025-05-21 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| af4b2f90-ef4a-379c-9b66-7aae8a8bc3c2 | -12.3324 | -49.9857 | 2025-05-21 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 771928a8-0d19-3385-a27e-b7753e119338 | -12.3134 | -52.4974 | 2025-05-21 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 506f9748-5f71-321e-8d5f-3a34b5e96f8e | -12.3327 | -49.9641 | 2025-05-21 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 8e995eb5-ebde-3715-92ae-ec28bbd30358 | -12.2943 | -52.4995 | 2025-05-21 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 600.5 |
| 4b088e62-a716-3a03-bb14-e5b99a22abc6 | -12.3519 | -49.9617 | 2025-05-21 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 8ad23794-5d7d-3a18-9004-71fc98d19464 | -12.3515 | -49.9833 | 2025-05-21 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 4e1b735d-3bd6-3d92-8cff-1e452101652b | -12.2946 | -52.4785 | 2025-05-21 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 423.1 |
| 13bd2cf6-ef73-3eeb-9b1c-3454b440f460 | -17.7652 | -56.3139 | 2025-05-21 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 38a05c0f-d23f-3663-b635-853a08b7d5ac | -12.3519 | -49.9617 | 2025-05-21 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 2f2c2f48-d61e-3556-a13f-19a1c98061cf | -12.2943 | -52.4995 | 2025-05-21 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 641.2 |
| a77ac315-eab4-3e47-949e-7ee5d30bc0f9 | -12.3134 | -52.4974 | 2025-05-21 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 162.6 |
| bb7f04f8-9d47-3e67-b6a3-08c4f01e4579 | -12.499 | -57.1847 | 2025-05-21 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 206.7 |
| e5058da2-01bf-3cce-9e6b-954151692a7c | -12.2946 | -52.4785 | 2025-05-21 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 432.5 |
| fffa3db7-f1ee-3a1b-a993-b3d0cb2caee5 | -12.3137 | -52.4764 | 2025-05-21 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 1edda012-cc39-33a5-ba9c-6e1528efcc11 | -12.48 | -57.1863 | 2025-05-21 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 187.2 |
| cb53a749-b31a-3689-96a2-1f760d57f3c1 | -12.3327 | -49.9641 | 2025-05-21 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 33b30fd6-80b3-3231-8be5-3de8b590ef55 | -12.499 | -57.1847 | 2025-05-21 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 208.7 |
| b9b4dee6-1980-3ffb-b6ac-d4b7726103d9 | -12.3324 | -49.9857 | 2025-05-21 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 71d86c54-4e70-384b-98a0-51ecf5f022cf | -12.2943 | -52.4995 | 2025-05-21 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 678.5 |
| 95892526-392a-3757-b6fe-de5182ed51ec | -12.48 | -57.1863 | 2025-05-21 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 199.9 |
| a445c0fc-968a-32a2-a939-ce956f367eb2 | -12.3515 | -49.9833 | 2025-05-21 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 600d6085-cc19-37d9-9a21-ad72baad48b0 | -12.2946 | -52.4785 | 2025-05-21 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 408.6 |
| 828fd49b-33a7-38dc-b91f-d482294eb376 | -12.3134 | -52.4974 | 2025-05-21 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 71ade286-1aa1-31d4-9f5c-1506a3cc4526 | -12.3137 | -52.4764 | 2025-05-21 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| be2f3aef-0f1c-3b6e-b0a0-762e04b21732 | -10.6041 | -52.8575 | 2025-05-21 14:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| dcfbf73f-f4fb-3ea8-ac03-3eda92cfd9bb | -12.294 | -52.5205 | 2025-05-21 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 96ae8e79-51ae-315d-ab0d-293e6c768566 | -12.3519 | -49.9617 | 2025-05-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 12d66cbf-bdd4-3c4c-a661-88bb8e3ba64c | -11.5881 | -47.6279 | 2025-05-21 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 718e0716-7cca-3a10-ad19-65cab9b7e1ab | -12.3134 | -52.4974 | 2025-05-21 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 173.2 |
| df31247b-b629-317d-a4b3-42f571bd5091 | -12.2946 | -52.4785 | 2025-05-21 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 464.7 |
| 4af12c29-8e2f-385a-a3f0-05bae85f4076 | -7.241 | -44.7126 | 2025-05-21 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 800d9d52-5e57-3912-bc94-1edb32ab0022 | -12.2943 | -52.4995 | 2025-05-21 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 712.7 |
| 9cf50138-a901-3575-9a7b-4d8c1bca0c9a | -12.499 | -57.1847 | 2025-05-21 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 5f08c792-a356-387b-abee-758982f669f6 | -12.3137 | -52.4764 | 2025-05-21 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 530c6b65-0218-36d2-b3b2-9677a2fd2631 | -12.3324 | -49.9857 | 2025-05-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| aa5feeb1-194b-377e-ab3b-5af6548e05c1 | -12.2756 | -52.4806 | 2025-05-21 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1ec644a4-88f7-391e-a30d-39fc84bc6967 | -12.3706 | -49.981 | 2025-05-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9c43cc45-620a-3dfc-8d38-0ab8234129ad | -12.3327 | -49.9641 | 2025-05-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 5ea2a9d0-d916-3b99-91bd-fcd9bed45b70 | -11.3478 | -49.6287 | 2025-05-21 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 055de24f-ad0b-3f12-8ae6-092b669615f3 | -12.48 | -57.1863 | 2025-05-21 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 63a6088a-3dc2-354f-83a0-380ff37cefd5 | -12.2946 | -52.4785 | 2025-05-21 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 432.6 |
| 5192eda6-ac3a-3728-bd7d-a7950276d7b3 | -12.3137 | -52.4764 | 2025-05-21 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 02e9f622-d38d-3a84-9d34-97350ae7a5ce | -11.3668 | -49.6265 | 2025-05-21 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 2396b06b-6e2f-3810-9d4d-b26808ff3f68 | -12.2756 | -52.4806 | 2025-05-21 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 3c4f01d1-7e76-3af7-8891-421984275dfd | -12.3519 | -49.9617 | 2025-05-21 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 2514046e-eca4-3496-a33f-b51ae4586ea9 | -12.2943 | -52.4995 | 2025-05-21 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 638.1 |
| 9010b88a-4068-3aa5-aa21-140a2335f88b | -12.499 | -57.1847 | 2025-05-21 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 44d491cf-3ab0-3076-bb43-d97b655224e2 | -12.3324 | -49.9857 | 2025-05-21 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| d463d556-f9b9-32a7-9122-ad50a4a0921b | -12.3327 | -49.9641 | 2025-05-21 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b4c2e71e-dc69-3841-94eb-1b2b12e56571 | -12.3134 | -52.4974 | 2025-05-21 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 237.7 |


