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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8c1aea0-cac3-3d43-b0cb-1addc5f921f6 | -10.2941 | -57.138 | 2026-06-28 01:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 4e58b24e-319e-3809-88aa-2f6baed26e40 | -11.5243 | -54.7872 | 2026-06-28 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 60e44022-43d1-329b-b41b-cd5ba79c4b47 | -18.4795 | -54.1105 | 2026-06-28 01:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 7b1429ac-78e0-30cf-bc8b-15a131583316 | -12.4462 | -58.5023 | 2026-06-28 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 43520142-76f9-3e9d-ab5a-712b486866df | -11.2279 | -54.3036 | 2026-06-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.3 |
| d1ff27ae-1440-3cdb-802d-c9771e593044 | -12.6048 | -57.8743 | 2026-06-28 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c27b7a89-d1dd-32a0-965a-cda539684045 | -12.4654 | -58.481 | 2026-06-28 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| b173735e-aeca-3cdb-954d-b275ed2c184d | -11.2277 | -54.3241 | 2026-06-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c96593ff-a857-3c6d-bed9-d374fbb13550 | -12.5858 | -57.8759 | 2026-06-28 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 1d339e36-c133-30d9-9b41-28b58db5b344 | -11.6657 | -57.2536 | 2026-06-28 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| df799b96-a988-30c0-acdb-c71011656d1b | -12.1773 | -57.1519 | 2026-06-28 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6174eaac-8da4-3e6f-a8ed-0f1e125ab283 | -11.209 | -54.3053 | 2026-06-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 283.4 |
| 8ade4f5f-2fa1-3e86-81ad-2edc1216fca2 | -10.3128 | -57.1367 | 2026-06-28 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 5a1ed62d-b382-3bb0-abe2-cb4059fc7b44 | -9.0796 | -59.4098 | 2026-06-28 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7f6122f1-bc26-35ce-9c6b-07847d22733d | -11.2088 | -54.3258 | 2026-06-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 1fc7b149-9181-361f-b2a1-e58e661d50d7 | -12.4651 | -58.5009 | 2026-06-28 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 8c0b8d28-127b-31db-a06d-4c8e8fcf6d01 | -10.2942 | -57.1182 | 2026-06-28 01:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 38a26497-e16a-31e7-8803-0d5658ca1b5e | -12.6048 | -57.8743 | 2026-06-28 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 82eedb41-a6e0-3e67-bde4-cd0f6ee67bcb | -11.5243 | -54.7872 | 2026-06-28 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 607c5a39-cd84-34a2-9348-f557174b702e | -18.4795 | -54.1105 | 2026-06-28 01:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 7f1b415f-37ef-312a-ab41-c499a21fc506 | -10.313 | -57.1169 | 2026-06-28 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2adf47bf-22e3-3c10-8431-5e0cf1d1a27f | -11.2279 | -54.3036 | 2026-06-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| dd47ebc0-142c-3594-9ad1-b2e0726652c8 | -12.1775 | -57.1319 | 2026-06-28 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 83a97890-260f-38ac-a177-25c91908a00c | -10.2941 | -57.138 | 2026-06-28 01:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 9203fe74-9683-3534-a993-4747401edd16 | -12.092 | -52.0176 | 2026-06-28 01:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 68544bc9-5b69-3fe3-83b5-94af672fd219 | -12.0923 | -51.9966 | 2026-06-28 01:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 42ceb9c2-4755-3fe2-aa59-98264eed134c | -11.2093 | -54.2848 | 2026-06-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 87cc288b-7f1e-387a-a56d-f793f2a040f8 | -12.6046 | -57.8942 | 2026-06-28 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1614b226-c676-39f6-8c3a-880018a87e7f | -12.6048 | -57.8743 | 2026-06-28 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5aff7f44-a8a6-30f5-ade0-a8677a367ef1 | -12.1747 | -52.8886 | 2026-06-28 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6d5ce3a2-a1b9-36e6-ad69-4636cbf9b68f | -12.1775 | -57.1319 | 2026-06-28 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| da3a9e55-304f-3ab6-ad84-93db03b7b456 | -12.1934 | -52.9075 | 2026-06-28 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| bcdd85a9-881e-3528-95b5-e20df4e561ee | -12.1937 | -52.8866 | 2026-06-28 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| f2e6e21d-5075-3d06-ae2e-acf86b2507f3 | -12.2128 | -52.8846 | 2026-06-28 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d6cba216-4de9-3403-bc3b-6902c9c18188 | -10.313 | -57.1169 | 2026-06-28 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 482274e9-5d2e-32b8-823b-2d2b36420479 | -12.0923 | -51.9966 | 2026-06-28 01:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1d730e52-9a16-3818-8dd2-e822d519f852 | -12.194 | -52.8657 | 2026-06-28 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 441c10e0-eb6f-3b62-bf70-d31025c744a0 | -10.2942 | -57.1182 | 2026-06-28 01:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| fee1f4a1-1721-36b4-a57c-c914af072a74 | -11.2093 | -54.2848 | 2026-06-28 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0d76d216-c020-3a72-9fb9-d00dec444949 | -11.5243 | -54.7872 | 2026-06-28 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 08732182-863e-3107-a608-560c627b6710 | -11.2279 | -54.3036 | 2026-06-28 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 3120875a-9a03-3e67-8e0f-0eed877ef44a | -12.092 | -52.0176 | 2026-06-28 01:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 97127e48-7911-3809-a06c-843140c0681a | -12.4654 | -58.481 | 2026-06-28 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 33b2200b-612f-34fb-904f-f5e4959b1afa | -18.4795 | -54.1105 | 2026-06-28 01:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ffbff637-ead6-3b2a-8f79-5190c66036ec | -11.209 | -54.3053 | 2026-06-28 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 264.3 |
| f6bf1df6-f518-3a5b-a35b-70126faa5333 | -11.2088 | -54.3258 | 2026-06-28 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 1dbafa28-da09-3abd-8f17-fad3cd80ed87 | -12.1773 | -57.1519 | 2026-06-28 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3b51b0ef-f32f-39af-99fb-32909c1d7547 | -12.6046 | -57.8942 | 2026-06-28 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5da7a200-8d91-3962-8736-4b1b2db30e53 | -11.6657 | -57.2536 | 2026-06-28 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4f099ae8-54c8-32fb-b949-8db629681916 | -9.0796 | -59.4098 | 2026-06-28 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| bd4e2425-f8f6-3836-8f30-5b7f371d588f | -12.2131 | -52.8637 | 2026-06-28 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 94c33db3-41c2-37c0-aeb8-7b87a1fa77c6 | -10.3128 | -57.1367 | 2026-06-28 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 619bb5ab-9f41-3522-82a7-454233500464 | -12.4651 | -58.5009 | 2026-06-28 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| dd21aab1-ca1a-3f3b-be3d-7b090f37026f | -10.2941 | -57.138 | 2026-06-28 01:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 71e1d389-bcf4-38dc-8c38-e72ec54eee1f | -9.0982 | -59.4088 | 2026-06-28 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2a259767-ce30-3017-8f28-d46dd9d6662a | -12.6048 | -57.8743 | 2026-06-28 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 888382d3-be8d-36eb-b79c-1e5ff809a7b3 | -10.313 | -57.1169 | 2026-06-28 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d6127d5a-23c8-3ad8-9d30-0f195a22798b | -11.209 | -54.3053 | 2026-06-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 1f304407-f230-3d66-a27e-19c804d5432f | -10.2942 | -57.1182 | 2026-06-28 01:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 06d95720-dd59-3161-9272-8b25ddc914bd | -11.2088 | -54.3258 | 2026-06-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a52faca2-7b2d-3185-8e79-18eec52ede11 | -12.1934 | -52.9075 | 2026-06-28 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2126d46c-6b36-3641-bfb3-c0cdbf8f6813 | -18.4795 | -54.1105 | 2026-06-28 01:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 60.3 |
| ec76ced9-2460-3ff2-b0c7-cf278afcf9cd | -12.194 | -52.8657 | 2026-06-28 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| ab18e596-5877-37d7-8937-874904f171ce | -12.092 | -52.0176 | 2026-06-28 01:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 3a0371e0-f90b-3175-855a-f976610c500a | -10.2941 | -57.138 | 2026-06-28 01:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| e162fba1-1ebd-3c1f-904e-771215a5805b | -11.2093 | -54.2848 | 2026-06-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 430ec8f5-506c-342c-b4ac-49c253a9314d | -11.2279 | -54.3036 | 2026-06-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 129aa203-f93f-3629-bfc1-012b3d94caf3 | -12.1937 | -52.8866 | 2026-06-28 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 1a87efdc-db95-381a-a92d-d5e813e6f5c6 | -10.3128 | -57.1367 | 2026-06-28 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 49ebd283-428e-386d-9832-95c6a635bfec | -12.1747 | -52.8886 | 2026-06-28 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6188ba0c-2e35-322a-a899-5e5906787d73 | -12.6046 | -57.8942 | 2026-06-28 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 37d9c406-90c0-3aae-8f41-09eaabaf5dd9 | -12.2128 | -52.8846 | 2026-06-28 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4b257c98-9438-30dc-bf4b-c7511fb3e92b | -12.4651 | -58.5009 | 2026-06-28 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5ab62c6c-1971-3997-b416-bba87db550a9 | -12.1773 | -57.1519 | 2026-06-28 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1faac6c8-d030-3ca1-a522-dd98266cac68 | -11.2277 | -54.3241 | 2026-06-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 69f0fb01-7786-3440-a5e3-d4071b7be5a2 | -12.2131 | -52.8637 | 2026-06-28 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 0f0f5537-68b3-3179-9436-671dec76d546 | -12.0923 | -51.9966 | 2026-06-28 01:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9fae044e-6208-311e-a914-8ebbad12b83e | -12.1775 | -57.1319 | 2026-06-28 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a00b17e4-5bc6-3476-92fe-3e4fa1cd136e | -11.6657 | -57.2536 | 2026-06-28 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c07a26e3-9912-38d7-9373-d1e8b41c7ea1 | -10.2942 | -57.1182 | 2026-06-28 01:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 9028fd9f-7bf7-34e3-b578-efb48fec5f81 | -11.2279 | -54.3036 | 2026-06-28 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| f6b64ffa-f633-39f5-b6cb-e20ab5de0edf | -17.3034 | -42.6678 | 2026-06-28 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 9c097396-191a-3537-9075-bdd6b7f1cee5 | -9.0796 | -59.4098 | 2026-06-28 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4197d81a-48be-38d6-a6b3-4daa6fbca9a0 | -12.6046 | -57.8942 | 2026-06-28 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 0a61bbef-3d51-3136-bc26-f258f1eb9aa9 | -11.209 | -54.3053 | 2026-06-28 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| dba69796-c0cd-394f-8ec0-cd3dede07197 | -12.092 | -52.0176 | 2026-06-28 01:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 14c763ad-539c-32f0-b6ca-984be8559dcc | -18.4795 | -54.1105 | 2026-06-28 01:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 67.2 |
| dc9b6a3f-3184-3289-9a1b-7b68a07452c4 | -12.1773 | -57.1519 | 2026-06-28 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9acfaef4-7b6f-3309-a868-975eb08c5f6e | -10.313 | -57.1169 | 2026-06-28 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 03d2a049-9be8-38f4-9466-29b6fc47e11d | -12.1775 | -57.1319 | 2026-06-28 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5fa1a208-2add-314e-847a-37598b80008c | -10.3128 | -57.1367 | 2026-06-28 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 62cf7baf-aa6c-3260-a280-cd533de08384 | -10.2941 | -57.138 | 2026-06-28 01:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| dcabaef5-ef5a-39f1-a892-65f3b5670682 | -17.3041 | -42.643 | 2026-06-28 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c11aa0bd-5d15-3a3d-a925-b40cc0547899 | -12.4651 | -58.5009 | 2026-06-28 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c65a75fe-4ed1-31b4-8c41-2f1373a21ca7 | -12.0923 | -51.9966 | 2026-06-28 01:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| adb79a5c-33f2-3035-9bf6-651723ff2ec5 | -11.2088 | -54.3258 | 2026-06-28 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6618b6ff-2702-3516-911d-97dd8e9f4848 | -12.6048 | -57.8743 | 2026-06-28 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a9bf2906-6aeb-36a2-ae53-449409dc2b77 | -11.5243 | -54.7872 | 2026-06-28 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| b6be6d74-1f9f-3ad2-b8d2-a95f70e98bbc | -11.6657 | -57.2536 | 2026-06-28 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f1245e0d-fffa-3b0e-9b2c-605e6cf24129 | -12.4654 | -58.481 | 2026-06-28 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |


[Clique aqui para ver as próximas entradas](README8.md)
