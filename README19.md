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
| d1b8ef1b-8755-3006-a64b-7e5f473713a6 | -3.4762 | -50.0883 | 2026-10-04 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 28cbc006-4775-378a-8f5e-6868f47ae298 | -2.5842 | -51.8623 | 2026-10-04 02:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 7faefe84-f974-3c6a-912a-a91751c2a0f8 | -4.2558 | -46.3855 | 2026-10-04 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 64795380-7bc9-3697-9e0d-2b30d8c47f7b | -2.5842 | -51.8829 | 2026-10-04 02:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 18973c36-87fe-38b3-929b-718523e525b7 | -3.0721 | -49.5313 | 2026-10-04 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ed99ed12-9293-36c1-a3ec-9f480caa5def | -3.8756 | -55.8184 | 2026-10-04 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 02ec201a-df54-3b2d-9add-4b0f7c4bc3d9 | -3.1117 | -53.7032 | 2026-10-04 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a06a7c27-0c2a-3c79-9f03-0b96bc22f1e1 | -3.1116 | -53.7234 | 2026-10-04 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| c88e919b-485b-35e7-a644-32dd4aba6cf3 | -4.2887 | -50.2675 | 2026-10-04 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 938.7 |
| f1b92227-e84d-3ee4-9078-f52227ee222b | -3.13 | -53.7229 | 2026-10-04 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| b8585b49-b396-376c-b2bd-be92546b23b1 | -4.2702 | -50.2683 | 2026-10-04 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 78aec4a5-50cb-34a0-ae33-bfbf9a1fff19 | -4.3072 | -50.2668 | 2026-10-04 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 986d6cf9-56bd-3835-992c-c0fbca82a187 | -4.2888 | -50.2465 | 2026-10-04 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| f6a9fcbe-ba47-377f-85e7-d18828594c2e | -2.7979 | -54.1134 | 2026-10-04 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a7903148-5c1c-3904-8a02-f725041469d5 | -4.2701 | -50.2894 | 2026-10-04 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 0ffcaf00-3ffa-33ba-bf87-9ed9a6d4731b | -3.1116 | -53.7436 | 2026-10-04 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| abb7d032-5eac-35ca-8ba6-ae96f6cfd3d4 | -2.8163 | -54.133 | 2026-10-04 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7c2973a9-b448-33b2-b0d0-92dfc34b8fd1 | -3.4761 | -50.1094 | 2026-10-04 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 43aabbe0-84f1-335c-9db8-01b910f88ab6 | -4.2745 | -46.3624 | 2026-10-04 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c796ab44-c531-3f69-94ea-e4d6bdab5c99 | -3.9033 | -49.6925 | 2026-10-04 02:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 37bbb9af-4440-390b-a60b-2e60f6f0d850 | -3.1299 | -53.7431 | 2026-10-04 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 2056d89e-ca38-3f3e-b2aa-391f996bc0b8 | -3.7559 | -49.5711 | 2026-10-04 02:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9aee72fc-2147-321b-be93-bcdb1d64e583 | -2.8163 | -54.1129 | 2026-10-04 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 488313d2-d5ea-36b7-b035-186af8a93ae8 | -4.2886 | -50.2886 | 2026-10-04 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 221.3 |
| cb95dfb6-e35b-3a66-afe4-f369d1a99a9b | -3.8757 | -55.7986 | 2026-10-04 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d975d47d-f051-3e60-8aaa-9d3d98baa900 | -3.8757 | -55.7986 | 2026-10-04 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d5a66788-deca-3bdd-a7c6-c9a8571f0d24 | -3.4761 | -50.1094 | 2026-10-04 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 620b8b61-cea4-3adf-95b7-6732105b3e53 | -3.9033 | -49.6925 | 2026-10-04 02:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 49378142-fced-313a-bf8d-e91f5f1c310c | -2.5842 | -51.8829 | 2026-10-04 02:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 35ff5ad6-c03c-3c68-8d74-51354da61ba1 | -3.1115 | -53.7637 | 2026-10-04 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 528a16d8-5adf-3a87-b88b-fa583a8eb78b | -3.072 | -49.5525 | 2026-10-04 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c8c5d9d8-dd28-3c97-850e-e57c430140d7 | -2.8163 | -54.1129 | 2026-10-04 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 0e09006e-b7e2-3496-b206-93a764f7cf6b | -2.5842 | -51.8623 | 2026-10-04 02:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 7118b129-d836-3aa6-9e63-0c66eb73dc88 | -3.1116 | -53.7234 | 2026-10-04 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 193.1 |
| dd4dfae6-c87d-3524-bcf3-d36e77196622 | -2.8163 | -54.133 | 2026-10-04 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 653071a0-c5b1-3e9d-98d6-01ff78cf9db4 | -3.13 | -53.7229 | 2026-10-04 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| ca3d7f85-2649-30bd-978d-28cafd9ee9b5 | -4.2701 | -50.2894 | 2026-10-04 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 32dfc7a3-82ea-362b-aba5-1794806e6f7b | -2.7979 | -54.1134 | 2026-10-04 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e6583176-fccd-3042-8221-5f2a86c1a5ca | -4.2744 | -46.3846 | 2026-10-04 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5e19e262-a75c-32a6-8c93-88e1018f47a6 | -4.2702 | -50.2683 | 2026-10-04 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 0c2866bc-be61-38f1-939e-a71f03f937b5 | -2.8164 | -54.0929 | 2026-10-04 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 5ec41583-9b2c-3990-a935-066c1e8c7184 | -4.2559 | -46.3633 | 2026-10-04 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 6c378ce2-2aa5-3851-a1e6-3099a35a2cc4 | -4.2745 | -46.3624 | 2026-10-04 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 12c38b33-8856-3ccc-be5a-8a4a8178fdff | -4.3072 | -50.2668 | 2026-10-04 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c29f3267-3a8d-396b-a7f6-c9db3dae534f | -3.4762 | -50.0883 | 2026-10-04 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 1e241f2c-4b87-342b-8cee-09ee327b5f25 | -3.7559 | -49.5711 | 2026-10-04 02:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d0337142-87ed-32cb-bb09-81273fb228bb | -4.2887 | -50.2675 | 2026-10-04 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 761.0 |
| 58852eac-f28c-3de9-88b3-a130b22512df | -3.0721 | -49.5313 | 2026-10-04 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4728133d-66a9-340a-8e4b-c143db0aa153 | -4.2886 | -50.2886 | 2026-10-04 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 290.4 |
| 6f30d4f9-a706-34f6-b323-cc096353740c | -3.1299 | -53.7431 | 2026-10-04 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| cd6ccf25-daaf-3f8d-b625-aa68745590a1 | -3.1116 | -53.7436 | 2026-10-04 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 181.7 |
| b20d7400-9342-3436-8473-ea2762e9ac54 | -3.8756 | -55.8184 | 2026-10-04 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1f05c3b5-b495-3a0f-bf7d-fe6f3c61ff94 | -2.2297 | -53.7026 | 2026-10-04 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f6b454e2-8e98-345f-8d38-c93cd5e54beb | -4.2888 | -50.2465 | 2026-10-04 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 6f85ff5e-f913-3eba-b35c-51a61dfce3c6 | -3.2951 | -53.8395 | 2026-10-04 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 906269de-17ad-3060-a512-eb0a99f8dae8 | -4.2558 | -46.3855 | 2026-10-04 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b0ab1904-7822-320a-b2ca-db62d5e00973 | -2.5842 | -51.8829 | 2026-10-04 02:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1f6e38c2-622d-3753-b691-6d5066c17aa3 | -3.4762 | -50.0883 | 2026-10-04 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 15f5d7d2-3931-3fa0-9ddf-ea23a6537032 | -4.2888 | -50.2465 | 2026-10-04 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ee5f2233-1b9f-3800-af9b-14def36c3e13 | -4.2558 | -46.3855 | 2026-10-04 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 16147d67-eff3-3359-adf8-e1c7cd5de402 | -4.3072 | -50.2668 | 2026-10-04 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 416d19e9-80c3-3ee7-836e-fd5f749cbfc1 | -4.2701 | -50.2894 | 2026-10-04 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1e4e66e7-cae4-3a9b-aeb9-26f17ee9e5f0 | -3.0721 | -49.5313 | 2026-10-04 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c0bf0afb-86b2-3ab8-b71d-45a24f4b9625 | -2.7979 | -54.1134 | 2026-10-04 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5447b240-b52a-3f8b-bba2-83a53bc0faa1 | -3.8757 | -55.7986 | 2026-10-04 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 575cbde3-4701-3969-bf32-9cb19f8a84a4 | -2.5842 | -51.8623 | 2026-10-04 02:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 556b278f-6870-3f4a-ac20-303aea1a64f3 | -3.4761 | -50.1094 | 2026-10-04 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3e4b98b8-04ab-32e2-bf69-ce86c238887d | -3.1116 | -53.7436 | 2026-10-04 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| eecea08f-570f-371a-85ad-653d5d044e3c | -4.2744 | -46.3846 | 2026-10-04 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| b80aad49-9784-3e7b-a98e-f206fcf34b21 | -3.1299 | -53.7431 | 2026-10-04 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 706e96e0-c43d-3ef2-a569-9e38dbf6b7c8 | -3.8756 | -55.8184 | 2026-10-04 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c071f7ef-0cb8-37e9-8831-79b4470ae0a3 | -2.8164 | -54.0929 | 2026-10-04 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 2015a109-8733-390c-8c5a-04c055c2e9c8 | -3.1116 | -53.7234 | 2026-10-04 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 1aeed289-f3ac-3c58-a73c-28550cd8bcdf | -2.8163 | -54.133 | 2026-10-04 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 48d387e6-1cff-30a3-9d3f-9b133b5cf995 | -3.8573 | -55.8189 | 2026-10-04 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9ad9c6f3-10af-3180-8266-9e332b9024a3 | -3.13 | -53.7229 | 2026-10-04 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 57c25e80-c8da-39d0-90bc-dc1733fdaefc | -4.2702 | -50.2683 | 2026-10-04 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 193.9 |
| fc264ba7-0329-3866-a975-0e7371f006b1 | -4.2886 | -50.2886 | 2026-10-04 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 247.4 |
| 70b4c6cd-de64-3b27-a63d-235dd8b4b101 | -2.8163 | -54.1129 | 2026-10-04 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| bcb40b47-0300-30b9-a014-ec0062ccfd45 | -3.2951 | -53.8395 | 2026-10-04 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 27372f62-56a0-34ab-a487-e2cb84a04ca2 | -4.2745 | -46.3624 | 2026-10-04 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0a6b31b7-036d-3f8a-9bb1-d762d25b5053 | -4.2887 | -50.2675 | 2026-10-04 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 770.7 |
| a87d228e-51e1-39bb-9389-da5a1bf1e5af | -4.2559 | -46.3633 | 2026-10-04 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 2cdd0f8e-bbc7-39a2-8140-f71dbb4860eb | -2.2297 | -53.7026 | 2026-10-04 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 511cb217-ab21-3f62-999c-7772eca14720 | -3.072 | -49.5525 | 2026-10-04 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7c11b548-6535-3898-8c71-a2700f8574c5 | -4.2559 | -46.3633 | 2026-10-04 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 7cd4b271-4ce4-3543-b0bf-5765161971b6 | -3.8756 | -55.8184 | 2026-10-04 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7b91ec54-d6a2-3762-a80c-32633a0efbb1 | -4.2745 | -46.3624 | 2026-10-04 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 37c3a817-1468-31b9-aa78-25d78bb282ea | -4.2888 | -50.2465 | 2026-10-04 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 79e29fdb-1104-3730-9385-9c1df0e4339c | -3.4761 | -50.1094 | 2026-10-04 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 106163ca-98df-3236-b825-7ec1eef54efd | -4.2701 | -50.2894 | 2026-10-04 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b734c484-9de5-3742-b9a3-6c43f965a7b3 | -3.1116 | -53.7436 | 2026-10-04 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 19034a40-cca5-3936-bc89-d0c775b80f29 | -4.2744 | -46.3846 | 2026-10-04 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 043a4033-4ead-362b-831f-6d0c04f5508e | -4.3072 | -50.2668 | 2026-10-04 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 77302c70-0898-3412-bc28-b5f6d492104d | -3.13 | -53.7229 | 2026-10-04 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 2dd7d3bf-5c59-3617-9db2-90fe18848ea9 | -2.8163 | -54.1129 | 2026-10-04 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 8dbaf849-b269-397f-b82c-479a5d2ef09d | -4.2887 | -50.2675 | 2026-10-04 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 597.6 |
| f8b549b5-dcd0-3c6d-8469-61c77157d085 | -2.5842 | -51.8623 | 2026-10-04 02:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9c6c7854-e28c-3390-84a3-42720dad1863 | -2.8163 | -54.133 | 2026-10-04 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4c39d056-fe13-30c0-be06-c95f14722d59 | -3.0721 | -49.5313 | 2026-10-04 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |


[Clique aqui para ver as próximas entradas](README20.md)
