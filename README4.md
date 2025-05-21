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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53e299fa-3a2d-3e5f-a353-2e922da3e965 | -13.6732 | -53.926601 | 2025-05-21 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5e2f70b-6423-3115-8f6d-950c36cdc839 | -11.0714 | -54.7664 | 2025-05-21 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3f8a8d70-605d-3ced-acdd-d6ef7cea87da | -12.2943 | -52.4995 | 2025-05-21 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8496c560-8525-399b-a988-d132669df740 | -11.0901 | -54.7852 | 2025-05-21 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 106198a8-e873-31ba-96e4-3e94ca2da75e | -11.0903 | -54.7648 | 2025-05-21 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7e429922-27a1-3cac-b903-8d73f2168916 | -11.0712 | -54.7868 | 2025-05-21 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4dd413f1-2d54-3689-9b6f-ed8465ba23cc | -12.3137 | -52.4764 | 2025-05-21 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| eb47218e-a1f0-33e6-85a8-081ee6c273cc | -12.4433 | -43.7242 | 2025-05-21 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 602a78ad-30f0-31ea-bd01-db8490908b83 | -12.2946 | -52.4785 | 2025-05-21 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 3899e3d2-2d1c-3efe-a67c-0b2829c19a97 | -14.1672 | -45.4673 | 2025-05-21 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 7e473340-50e0-3285-bb9d-73769d179094 | -9.0291 | -47.7452 | 2025-05-21 00:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 29890e50-e2b9-3d6d-8b8d-105d5b3b32c2 | -11.0714 | -54.7664 | 2025-05-21 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 1ef33392-3a6d-3fca-a392-4eedf410f7b6 | -9.0291 | -47.7452 | 2025-05-21 01:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 9a68cb5a-9e63-3258-92a3-e51ade35f603 | -6.2224 | -43.3693 | 2025-05-21 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 848dc2a3-c168-3e0d-a136-dd95abbaefb2 | -6.2226 | -43.3459 | 2025-05-21 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| a875b27a-676f-3ea1-b99f-80268b00b7af | -11.0903 | -54.7648 | 2025-05-21 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ae5ea060-3b9f-3f6c-abc3-c57f6c36ffd1 | -11.818 | -44.2703 | 2025-05-21 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2506d42e-466e-3084-b120-6d2141b40e1d | -12.2946 | -52.4785 | 2025-05-21 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 3a11b894-7bd5-39b1-8ea6-8851ff2d7b7e | -6.2414 | -43.3444 | 2025-05-21 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c64ba65c-ff9a-3fcd-89b6-5a43bd8dcb9f | -11.0901 | -54.7852 | 2025-05-21 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4f6b9b68-9e61-38b7-8cf8-7d8d4fd9d466 | -12.2943 | -52.4995 | 2025-05-21 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| de962411-4115-328f-9eb4-506b143a93bc | -11.0712 | -54.7868 | 2025-05-21 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3a198364-4a8c-394b-92c6-fb73909a0000 | -11.0712 | -54.7868 | 2025-05-21 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 54bd48fb-9c32-35b9-ae39-70e1b85b3c61 | -12.424 | -43.7274 | 2025-05-21 01:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d980cac3-5e64-39bd-bd79-283a483f9352 | -11.0714 | -54.7664 | 2025-05-21 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 814bd751-6e62-3c77-ae4e-d197b933cc7d | -11.0901 | -54.7852 | 2025-05-21 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 63cee76a-6014-3629-8e8d-2a6152372e85 | -6.2411 | -43.3677 | 2025-05-21 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 983a3a81-5ea7-372f-9b9a-1cf775664847 | -6.2226 | -43.3459 | 2025-05-21 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d210a2db-76d1-396d-af52-73a81387bb09 | -20.9601 | -56.5967 | 2025-05-21 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 7c1be270-3a1a-3d63-9925-8adba86f6588 | -6.2414 | -43.3444 | 2025-05-21 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 98f22e46-d8b2-309d-8055-90eef96458d1 | -12.2943 | -52.4995 | 2025-05-21 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 6033402b-f478-3e8f-b46a-6a23e9541c04 | -20.9597 | -56.6179 | 2025-05-21 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 35b400c7-b5bd-3336-88f8-a8876aaa77af | -6.2224 | -43.3693 | 2025-05-21 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| a9e00cc7-dd08-367e-88fb-bd18c93125b0 | -11.818 | -44.2703 | 2025-05-21 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9ad20f45-e2bd-3e25-8f89-ff6d989be512 | -12.2946 | -52.4785 | 2025-05-21 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 934213f3-8077-3d3f-9eb5-1d3efe5a9446 | -11.818 | -44.2703 | 2025-05-21 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0b20e34e-46c3-3f8d-a1cb-febb8f1a7bbf | -12.424 | -43.7274 | 2025-05-21 01:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 21ba71b6-20c4-32c2-9206-190309d09673 | -11.0714 | -54.7664 | 2025-05-21 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f813f9cc-52d1-39fc-b461-28199973b72f | -11.0901 | -54.7852 | 2025-05-21 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bd34a7aa-fc7c-3f79-8448-1ff88f57ffc7 | -6.2226 | -43.3459 | 2025-05-21 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 7b1d7896-914e-3725-b299-6d109c502f77 | -12.4433 | -43.7242 | 2025-05-21 01:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| e6353225-8f7c-394a-a6f6-e08042f0c90f | -11.0712 | -54.7868 | 2025-05-21 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 35d73254-e1e7-369a-ae7e-9d9bb2b51b01 | -12.2946 | -52.4785 | 2025-05-21 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| ecc62620-68f8-3182-b2e9-c2a5a9931335 | -12.2943 | -52.4995 | 2025-05-21 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 9589f510-5b71-33b6-ba66-f615f981badf | -20.9601 | -56.5967 | 2025-05-21 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a1dfbbf2-5884-3622-8a93-1ab5abee32e3 | -11.0903 | -54.7648 | 2025-05-21 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9828c10e-1999-3c9f-8a62-73b3191be4a1 | -6.2414 | -43.3444 | 2025-05-21 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5a6515eb-7a7f-35f4-ac81-1649b2942ae3 | -6.2224 | -43.3693 | 2025-05-21 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3ce6ff99-b455-386c-a8c7-e627f35ae3e3 | -9.0291 | -47.7452 | 2025-05-21 01:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 8115468c-5c2a-3a6b-a368-db7f15f34081 | -11.0714 | -54.7664 | 2025-05-21 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| aa6ef52f-d39e-3f9b-a43b-24991d37e026 | -6.2414 | -43.3444 | 2025-05-21 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b849c9c2-70c2-37f7-bbde-f7a4b2bda065 | -11.0901 | -54.7852 | 2025-05-21 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9178c5e1-f5fb-3d01-862d-c50589413a29 | -20.9601 | -56.5967 | 2025-05-21 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.6 |
| cbc79b85-5306-3a49-8eb3-7a6ebfe8abac | -11.0712 | -54.7868 | 2025-05-21 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 498030ac-97f4-3d58-8011-afa0ebcafd03 | -6.2224 | -43.3693 | 2025-05-21 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 1b2ed0e8-c672-365f-8f7a-6b391f7aa69e | -12.2943 | -52.4995 | 2025-05-21 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 43eedd29-ba3d-3819-823d-ef7eba5a3427 | -11.818 | -44.2703 | 2025-05-21 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 355facc7-2237-3eb5-bc80-d982b1258ea8 | -11.0903 | -54.7648 | 2025-05-21 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 214ce498-c93f-3592-9d50-6ec675c18594 | -12.2946 | -52.4785 | 2025-05-21 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| fd95c67c-8d60-3f27-8a9f-09cde935d8b7 | -12.424 | -43.7274 | 2025-05-21 01:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ffef126d-060c-3589-81c0-1fb4dd0cc9f0 | -6.2226 | -43.3459 | 2025-05-21 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| b20514bd-af8f-3c9d-9d5c-e281395c42e0 | -13.6701 | -53.9361 | 2025-05-21 01:39:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f14214eb-62f4-33e2-bacf-4683554c216c | -12.3018 | -52.471298 | 2025-05-21 01:39:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80fb679d-f213-39a6-8a1e-6362cbdc4a08 | -11.3057 | -53.990299 | 2025-05-21 01:39:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 031d5bd6-d831-32f3-9b08-0c8e5f41ad0d | -20.9569 | -56.589699 | 2025-05-21 01:39:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 73c5579a-5076-3035-ba88-fae9ff4f4fca | -11.083 | -54.772701 | 2025-05-21 01:39:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29fe5100-dfba-3a7d-be72-10c186ee2a71 | -10.0528 | -64.995903 | 2025-05-21 01:39:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad6c6a9d-3905-3eeb-93d7-4c9baad98aa6 | -10.0545 | -65.0037 | 2025-05-21 01:39:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0cef4df2-cff4-3399-a2a9-3a9e71c5abab | -20.959 | -56.598499 | 2025-05-21 01:39:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 196a225b-52b9-35d7-b49a-3616b468d3d4 | -12.4836 | -57.1856 | 2025-05-21 01:39:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13e1480b-a8f3-36d0-990c-f54bb0dd0349 | -11.0791 | -54.757401 | 2025-05-21 01:39:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 446a0edf-f52e-35dd-9bd7-4744a18f9a44 | -11.0869 | -54.787899 | 2025-05-21 01:39:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06a49f2b-22ea-3e25-bd4d-17f5d52bbbe8 | -12.2977 | -52.494801 | 2025-05-21 01:39:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18a314c9-9ce5-3a8a-bc55-396d692076f8 | -13.6142 | -55.452 | 2025-05-21 01:39:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3260b94-1206-3fcc-a7e2-a8a0de3772ad | -12.6902 | -58.118599 | 2025-05-21 01:39:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79d460af-08f5-3087-a17d-0ae1625c219f | -20.9632 | -56.616001 | 2025-05-21 01:39:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bbebd2a2-4f01-3112-b4c1-604945181dae | -11.0927 | -54.770199 | 2025-05-21 01:39:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38a24ee3-a4f8-3e0e-baa1-b87f0d98e533 | -12.3073 | -52.4921 | 2025-05-21 01:39:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4aa80a9-9a3d-3e72-8080-ab1c1dd371bb | -11.3013 | -53.973202 | 2025-05-21 01:39:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec1e85c6-aefb-3feb-9755-a335d8daaf00 | -19.7451 | -54.514301 | 2025-05-21 01:39:00 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6f1418be-05c5-3fcc-9d00-51fd84383cc6 | -13.6798 | -53.933399 | 2025-05-21 01:39:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 754c9abd-5283-3c00-90d5-1a0815b9b70c | -12.6946 | -58.1366 | 2025-05-21 01:39:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e13b6087-03d0-3957-99a2-d68b4289b15e | -20.9611 | -56.6073 | 2025-05-21 01:39:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3b39c488-3e03-3fd4-a392-90ef276ae351 | -12.2922 | -52.473999 | 2025-05-21 01:39:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b31d014-73bf-3c40-bd14-a22d4776cfa9 | -12.6924 | -58.127602 | 2025-05-21 01:39:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbae6949-bd53-31d6-8895-cd6038596544 | -13.6239 | -55.449501 | 2025-05-21 01:39:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31c8bb1a-dfde-36af-9d45-ef6dee06604f | -11.0966 | -54.7854 | 2025-05-21 01:39:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 210cb80a-b943-3eb1-9382-9fd733dfddf0 | -19.0644 | -53.4534 | 2025-05-21 01:39:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f046c827-7780-3527-ae4f-431db69c3949 | -12.2943 | -52.4995 | 2025-05-21 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e61dafda-e86a-3214-bc03-4621034e4690 | -12.2946 | -52.4785 | 2025-05-21 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 088984f3-6561-3906-884f-867a51fb44c6 | -6.2411 | -43.3677 | 2025-05-21 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| f09afcff-8e7a-3efe-bbc6-4f3fe13994d7 | -11.0903 | -54.7648 | 2025-05-21 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 30b61e5c-a60d-3d11-9be2-087d1e959d9c | -11.0712 | -54.7868 | 2025-05-21 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 02e91fd7-dc46-39fd-aae1-07e61c5614e0 | -6.2226 | -43.3459 | 2025-05-21 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 965a9c1a-85b8-3e68-ac97-5ce1aa0cf9fa | -9.0291 | -47.7452 | 2025-05-21 01:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| ed29bb14-0b59-3381-99d1-4cb5edd450ab | -11.0901 | -54.7852 | 2025-05-21 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| b36e6766-1caa-3327-9315-c2ed561b1e27 | -12.4433 | -43.7242 | 2025-05-21 01:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d4363ecd-6cee-3fe6-9d79-f9eab7aa0a7c | -6.2414 | -43.3444 | 2025-05-21 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7e6739e3-0e7e-3686-8308-cc777ed9b4db | -6.2414 | -43.3444 | 2025-05-21 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| d3d63637-9f49-3b16-964e-e803dbfa1a47 | -6.2411 | -43.3677 | 2025-05-21 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |


[Clique aqui para ver as próximas entradas](README5.md)
