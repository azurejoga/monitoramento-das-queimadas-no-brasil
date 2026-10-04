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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11aea9ce-34d3-35e0-a8cd-820c01a1d36b | -3.5787 | -55.537498 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f28f5572-a46d-317a-ac88-7a243c68e23a | -1.9956 | -54.1012 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e24f741-51c6-356a-8fe2-474186f7bd75 | -1.4923 | -49.4492 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86447276-2ff9-397e-a4be-fed71cd15c5c | -2.2435 | -51.905102 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 134b773f-2072-3e61-948a-28736ebc6d42 | -0.4707 | -52.041401 | 2026-10-04 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4136722e-3d53-36dd-bc0d-c91aa6080747 | -2.8041 | -54.129902 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d21e8a-2517-3495-8b04-e6f70c21df47 | -2.9038 | -49.399899 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 172dc816-03ab-3cbf-a1c3-8fc68c4d6f73 | -3.306 | -52.969002 | 2026-10-04 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f6d8bf-f1e5-3f9b-92a7-beca5857be33 | -3.076 | -49.5224 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee8f7ba9-2c05-3ce8-9fdf-1d5c117be437 | -3.2064 | -50.736599 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72549c77-80d5-3843-8839-2d61391d6e57 | -4.2629 | -46.377899 | 2026-10-04 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40ec461e-6140-3e7f-b5eb-3ca400b29c62 | -3.4713 | -50.084 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a99b216-e150-3a82-aba5-61335968e700 | -3.208 | -50.7435 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a82e90fb-7012-3823-8f2e-f652297af6a6 | -4.1576 | -47.530399 | 2026-10-04 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd60f823-a58c-3a1e-a47e-9bad2618912b | -2.9159 | -54.0783 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73ef6170-3a94-3d29-a09f-7bfbe059c6cb | -3.1243 | -53.722 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33cc3a1d-aeac-3d16-970f-ef70a43a1de0 | -2.8139 | -54.1278 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18bc02d4-4616-3480-b9e4-5ab3ae3e1fb6 | -4.2828 | -50.254002 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5bf1a77-7e15-3501-b834-4439ad32356d | -2.7511 | -51.5513 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38196209-9835-3b6e-ab65-ce10c387d0ba | -6.0007 | -53.628201 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2581604a-5a36-3968-a5cc-5d600aefb7be | -4.715 | -56.1423 | 2026-10-04 00:09:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef11d31-5995-350c-a1ba-0f4afe2383b6 | -3.2817 | -53.8283 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da14aabc-f290-30c7-9ebf-8630cae742a6 | -2.8003 | -54.112598 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2cb9b1c-e50a-30d3-a4e1-2d671c6652be | -5.5468 | -45.253101 | 2026-10-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7af5edb-9739-3acd-a440-85bcbdc49fe5 | -2.9081 | -54.089001 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecf1b6bb-2e9e-3de9-8497-7d460f68232b | -3.8855 | -49.682301 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b710b99-9b23-3531-9038-9d76ee8d159f | -7.7563 | -49.203098 | 2026-10-04 00:09:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| add56337-680c-31c3-a038-5d11b1077198 | -3.1281 | -53.738602 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9267ea6f-a3a0-348b-a89e-3bef1eb8c851 | -7.8891 | -45.302502 | 2026-10-04 00:09:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 867c459c-5c2b-3d40-bb6c-fb670e40f554 | -1.4777 | -49.43 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0273c768-b779-33c8-89a4-4e5e76f9177b | -4.4527 | -47.917801 | 2026-10-04 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59b4eaee-9217-302f-9002-51273e95b1e5 | -0.3643 | -52.0723 | 2026-10-04 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0568cdae-a33c-346e-9ec1-93c2e5ec6d88 | -2.8923 | -54.1106 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce2ee3b-3ce0-3c55-92e8-363231809e74 | -2.613 | -51.2127 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c26ba29-a55b-3864-b766-cfaf76da9920 | -4.2608 | -46.368999 | 2026-10-04 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6a5cafe-8c5c-3ded-ab82-fae11d1234ea | -2.5787 | -51.838402 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6a68358-dab6-35c9-9226-6487942c595d | -4.8244 | -49.868099 | 2026-10-04 00:09:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cee3503-0d38-3c57-b7da-c592f12287ea | -3.5262 | -54.604698 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46fa1447-d883-3f0c-a5af-718c132d6d85 | -3.0588 | -54.165501 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfdc68a7-f690-3a51-8dc2-6d3a89a984e5 | -2.5737 | -51.861599 | 2026-10-04 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0159fff-3d5d-39af-8951-a385c86f0c03 | -3.0693 | -49.538399 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 838476ce-123b-307d-abb4-a2fde9cdfecc | 2.0935 | -50.73 | 2026-10-04 00:09:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f3523997-8d5c-372e-80b6-0a42bf621ddb | -6.0205 | -53.5312 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8d6ce7c-92ee-3143-a4fd-975ce726ada9 | -1.4742 | -49.460602 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28501d44-3c6c-37eb-8c33-59e356f060e9 | -4.2859 | -50.2677 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79c76d44-a572-37a2-bc56-c8bd55baf4be | -14.5673 | -52.870701 | 2026-10-04 00:09:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41513511-3d63-36ce-89d8-cb14b215d52c | 2.3467 | -50.749802 | 2026-10-04 00:09:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 76626340-670b-3c77-9db5-80b4ba7101f0 | -3.5045 | -54.599499 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44061222-abc4-3ce2-bc11-0f2c5ceab78b | -1.4094 | -49.265701 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27cfd375-adaa-3708-a013-4c3517260ce6 | -2.9079 | -54.134499 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63f46007-31f8-37b5-9c70-b03e02741ecd | -4.453 | -50.963902 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7dd51ac-b176-34de-9d4f-679cf3b64cf7 | -7.8934 | -45.320999 | 2026-10-04 00:09:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5b3b54a-1f5d-3c6e-8b2e-d2d00f84c382 | -3.8953 | -49.680099 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c446e527-14b8-3054-becf-a72060a97e33 | -2.7964 | -54.095402 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 568a90ce-43a2-36b2-a127-a0d18d2e4853 | -18.917299 | -47.905899 | 2026-10-04 00:09:00 | METOP-B | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b561798e-ec6b-3b84-bff6-0ca35ca16841 | -2.7983 | -54.104 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2386d5c-16bb-3456-a1a3-f61bfc110afa | -2.8944 | -54.074001 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b43b91-a119-3c02-9b12-7f5ae97d613a | 2.3565 | -50.751999 | 2026-10-04 00:09:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 12ab1ab6-e18e-3a63-8066-46ba099fb640 | -3.307 | -49.132599 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af0fa25b-a2b8-317d-a2fb-11530b004504 | -3.2216 | -54.296799 | 2026-10-04 00:09:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a6a696c-3380-31e3-a202-c2db104b0979 | -9.1332 | -65.9559 | 2026-10-04 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6c0ae297-3ef5-36e5-a392-1990797cc108 | -8.593 | -66.8081 | 2026-10-04 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 78ded8ce-40f2-397a-9055-afd5816390fc | -3.8757 | -55.7986 | 2026-10-04 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d19465f5-d831-3a77-97cb-7c74ffe0fe53 | -3.8573 | -55.8189 | 2026-10-04 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 8603628e-bfaf-3abb-bfcb-c5ebf4ede1eb | -3.8756 | -55.8184 | 2026-10-04 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 18f6e700-315c-3e5d-83b7-0b3f91635674 | -3.0548 | -54.2277 | 2026-10-04 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7fafca13-423f-3a7f-a896-e1ef941d22f6 | -4.2887 | -50.2675 | 2026-10-04 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 15d0cfc9-2094-3a7c-b6a4-e2d3e4fc849f | -3.1838 | -54.104 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| dc92ff9e-b47f-33a4-a498-b37f6d4d6a12 | -3.0905 | -49.5519 | 2026-10-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 91dfc030-d821-3a63-91fb-59428eaa8187 | -2.6026 | -51.8619 | 2026-10-04 00:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 13bfe507-c558-3974-81e3-c81b1d45f2b6 | -9.899 | -65.0132 | 2026-10-04 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2b595899-1e11-37be-ad4e-4e71db7fcf98 | -3.5128 | -54.6162 | 2026-10-04 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 36d3d5da-349e-3a6f-a561-a23aff14e17e | -3.13 | -53.7229 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 70ff4544-ccad-38d5-9d1d-acfc9684b398 | -2.9817 | -54.089 | 2026-10-04 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 13e16a79-53f1-317e-b46a-88131b282a3c | -3.0721 | -49.5313 | 2026-10-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5d383ac2-dbe7-34ea-9c1d-b8c9798eb466 | -3.8573 | -55.7992 | 2026-10-04 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8cf7feb1-430f-3139-bf39-3530828deb89 | -2.7979 | -54.1134 | 2026-10-04 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 67036cf6-80b0-3e05-a11d-1bdaf8a6732e | -3.4577 | -50.089 | 2026-10-04 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| bb8481d4-97a7-3927-95ef-84d6d3a2db31 | -3.1116 | -53.7234 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 242.6 |
| 4e9fae02-d2c2-3430-9a13-bf6b5c17f52c | -3.8848 | -49.6933 | 2026-10-04 00:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2649c9a2-bc5b-334f-92f6-e2064a749426 | -3.9033 | -49.6925 | 2026-10-04 00:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ee5a6e4a-e805-3e82-adf2-b2cd2d23fa21 | -2.5843 | -51.8417 | 2026-10-04 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 30a22cb6-6d9b-3ebe-af04-ab513c7a056a | -3.3607 | -43.3893 | 2026-10-04 00:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| dd6a97ae-d2a5-3537-9e7f-5cd7f6c8567f | -3.1299 | -53.7431 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 00063bf7-9958-3b6a-bd43-8d52d6079a98 | -3.1115 | -53.7637 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| bac1c2a7-ec90-339b-96bd-df84282fbddc | -3.072 | -49.5525 | 2026-10-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c746ea5c-f826-3658-bafa-9277b7158822 | -2.8163 | -54.133 | 2026-10-04 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 557b1c49-7247-3f43-85d4-744e29d0bdab | -4.2744 | -46.3846 | 2026-10-04 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5b1e6337-e213-3457-859b-8964b893a365 | -3.1301 | -53.7028 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 64204f13-dadf-3b44-ac94-138c76933792 | -3.514 | -59.8065 | 2026-10-04 00:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ba7edf04-1ede-301b-a017-7448e4a12da6 | -15.241 | -40.5346 | 2026-10-04 00:10:00 | GOES-19 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.5 |
| 7a6d49de-2d52-3d06-b195-52bd38100245 | -2.798 | -54.0933 | 2026-10-04 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b853ba51-fdd7-304f-948a-1fa31b8ae318 | -4.2745 | -46.3624 | 2026-10-04 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 35937ab6-d7e8-3326-a263-82051084f7dd | -3.4576 | -50.11 | 2026-10-04 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bc9bb997-e8dd-37ff-a86e-9c556314a8e5 | -14.5683 | -52.8814 | 2026-10-04 00:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 82248a60-9378-3c15-a169-a65d536f03db | -3.1116 | -53.7436 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 312.9 |
| b2672d7a-f373-3992-af06-7b55a1caeb5a | -2.2297 | -53.7026 | 2026-10-04 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 08ed7a8a-6ed9-3f5a-980a-6b5ad6f598e3 | -9.0857 | -61.1629 | 2026-10-04 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9d9c54ec-72a6-32ba-9826-77677920e129 | -4.4847 | -45.5253 | 2026-10-04 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 23891a37-3c2d-3765-91a8-22a0116051a6 | -3.4762 | -50.0883 | 2026-10-04 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |


[Clique aqui para ver as próximas entradas](README7.md)
