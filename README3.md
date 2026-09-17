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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b26bc20-a641-34aa-a843-efd66812207b | -9.1123 | -45.7067 | 2026-09-17 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| fefc42ca-b047-3e65-bc9e-b4c8b0425f9a | -5.6472 | -44.7964 | 2026-09-17 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d6cfd901-373a-347f-8a87-b69ee5efeac3 | -12.5097 | -50.845 | 2026-09-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8d9d1bf1-54f2-3a91-828f-cc7f1fe63d2e | -8.5986 | -44.5762 | 2026-09-17 00:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 308086ec-9a85-3b41-b05e-41baaa8e8443 | -3.4941 | -54.6967 | 2026-09-17 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| b5029904-8a52-3b18-9d68-3180d4428833 | -8.4796 | -57.6478 | 2026-09-17 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2279e0d5-23f1-3d3d-a44b-1de4541b2961 | -4.5587 | -42.9523 | 2026-09-17 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ae63bb70-6940-3c00-b0d5-f47953dcfea6 | -10.8118 | -46.1594 | 2026-09-17 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| af186675-b255-348a-8f79-200543405d6d | -12.5104 | -50.8021 | 2026-09-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 972c1bb4-277d-3aad-a058-10a1d060dbe3 | -9.112 | -45.7294 | 2026-09-17 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 297.6 |
| 81419296-3c12-3686-99fe-d993929bac3d | -12.8543 | -44.386 | 2026-09-17 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 954b642f-06f6-39cd-9339-90cff16b6ce4 | -10.7221 | -54.0213 | 2026-09-17 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8e70b702-49a3-3d70-bc6e-0b1b9d5f8c35 | -13.3949 | -57.0242 | 2026-09-17 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| c8e6cfb4-8c12-3dde-9977-ec4db63720b1 | -6.8962 | -59.0303 | 2026-09-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9b6138d1-dce4-33a9-a80c-40911948d597 | -9.4102 | -62.7113 | 2026-09-17 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 4ac3cdb8-b9e0-35ad-8c69-db1d3842eaa5 | -12.4916 | -50.783 | 2026-09-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 3cb0b583-5ad0-3553-941d-5bcb83defd06 | -14.1405 | -48.7317 | 2026-09-17 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5da504e1-7b11-3124-b8af-03356a28a376 | -3.4757 | -54.6972 | 2026-09-17 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 247ecb11-286b-3606-9f1b-67b579f05e01 | -9.2939 | -60.6345 | 2026-09-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1adfc75c-f6a8-3f55-8241-26480405d446 | -2.6966 | -57.6084 | 2026-09-17 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9942e26a-43be-3891-ab1f-59c3e5ab76fe | -3.4757 | -54.7171 | 2026-09-17 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 231.7 |
| 8792691b-9dff-3f73-8dad-4f53cee03a0c | -2.9582 | -50.3149 | 2026-09-17 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 98d5c323-a0ea-388b-99a8-fa370024efd7 | -2.9581 | -50.3359 | 2026-09-17 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| e913b2c4-d9d6-3a2f-9caf-a84b01138556 | -6.9147 | -59.0295 | 2026-09-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 08fb8bf3-3a3d-3432-991d-3204db956482 | -6.8216 | -59.1686 | 2026-09-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ff493aad-0bae-3ccb-8dc5-e2340e5415e1 | -9.628 | -45.3521 | 2026-09-17 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 217.6 |
| 21183b5f-e007-3f75-a89f-193ecde1483a | -6.8032 | -59.1693 | 2026-09-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 31330d78-9173-3fa8-8fc4-977b981f524b | -4.5044 | -54.9845 | 2026-09-17 00:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 4901b80a-9be9-355e-8a4c-1bfe2836ccfa | -8.7604 | -66.5623 | 2026-09-17 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 680e7f05-b31f-3e8c-a8d5-ab0bad200ace | -12.4913 | -50.8045 | 2026-09-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 341.6 |
| 923fb4ac-40e7-35fb-8c8d-e559c963ce13 | -2.9766 | -50.3354 | 2026-09-17 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 8c2d00da-80c5-3fac-87c3-d233242b91b6 | -6.9309 | -63.0301 | 2026-09-17 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e0e5301b-91ee-3552-813d-9b7bd7aa7990 | -10.7223 | -54.0008 | 2026-09-17 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| b33cfd47-087b-3789-a5d5-cf14582b0614 | -6.8215 | -59.1879 | 2026-09-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 655f9602-a6af-38f0-9429-592bdf04866f | -8.4983 | -57.6271 | 2026-09-17 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a6a78cf0-09bf-32dc-8a74-a1d0c52e1e71 | -9.294 | -60.6153 | 2026-09-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 40cfd8bc-97fc-31ab-a031-66ef920facf7 | -6.8031 | -59.1886 | 2026-09-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e5b5086d-357b-3dd3-b81a-2420a6090fdf | -8.4982 | -57.6468 | 2026-09-17 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 8d42a129-b518-36cc-ac3b-a2436dcf786d | -9.1057 | -60.9511 | 2026-09-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8482d867-211f-3563-bb44-70fdb970f66c | -10.7923 | -46.1845 | 2026-09-17 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| d83228ed-f0fa-3699-bdf7-b93d98f8c52a | -4.5045 | -54.9646 | 2026-09-17 00:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| cf10ab9a-230b-3d05-9dd3-c3d11e373cad | -12.5101 | -50.8236 | 2026-09-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| bed6d6b0-0077-3a26-80d2-12d110484654 | -9.5769 | -66.2592 | 2026-09-17 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 85c9574e-81ed-3a30-b0b3-0fb4dc542543 | -9.131 | -45.7273 | 2026-09-17 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 31eaa73b-8ee8-31d5-9d7b-c170704f9a6d | -2.908 | -54.171 | 2026-09-17 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 5276687c-6cdd-347e-9465-bc5c168dd89b | -2.908 | -54.171 | 2026-09-17 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| fcd0da7e-983b-3efd-abcd-ec82d8331349 | -2.6965 | -57.6278 | 2026-09-17 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ff1e7b20-4f5b-3ed5-be75-e50933b047e6 | -6.8216 | -59.1686 | 2026-09-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d8680fc0-5532-3def-9895-6dac173d9bef | -8.4982 | -57.6468 | 2026-09-17 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 12a9fe79-ba1a-3497-b7d0-f451865b9098 | -10.8343 | -54.0933 | 2026-09-17 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ffe6ebf0-e438-3e6f-914f-10ce16f40659 | -9.8881 | -48.4013 | 2026-09-17 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a331d163-6d99-3140-8683-7e37ba386703 | -6.9147 | -59.0295 | 2026-09-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5b9a4d4e-b9f2-3b14-aeb0-2c55c40541e6 | -2.9581 | -50.3359 | 2026-09-17 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| e3b7a12d-ae84-3fbe-bd4d-7f21a0ea0a25 | -6.9309 | -63.0301 | 2026-09-17 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 4e42089f-a7f4-3178-8518-1a6a07b1bbbf | -9.112 | -45.7294 | 2026-09-17 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 260.4 |
| 5057347a-b4b6-3c96-a23a-cea548d71310 | -9.2753 | -60.6355 | 2026-09-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9bdc0e61-970e-3dc0-9fd9-e3fce6dbb3fc | -9.131 | -45.7273 | 2026-09-17 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.0 |
| b7d6037e-07d9-3390-9b10-912ff0cfbbb8 | -4.5589 | -42.9289 | 2026-09-17 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 90847d2e-d0bf-3a30-adc0-5797c868327b | -5.6472 | -44.7964 | 2026-09-17 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 6d5ae156-44a8-34ed-962a-614c50b4847b | -14.1405 | -48.7317 | 2026-09-17 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 199bbf9c-435f-3d17-991b-28ccd60e11d7 | -9.2939 | -60.6345 | 2026-09-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 699eb050-b1f3-3fb3-928c-e548e151f20b | -5.7752 | -45.128 | 2026-09-17 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| ad02ef8b-53d1-3bb1-ba42-62652ce025d0 | -10.7223 | -54.0008 | 2026-09-17 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 03aba5e2-cbb7-3fb5-be4e-b00662df9212 | -4.5587 | -42.9523 | 2026-09-17 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 42b81845-f44a-38a1-8754-3e08f2184835 | -6.8962 | -59.0303 | 2026-09-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7fb270f3-cf8d-34fb-b464-59eb72cee353 | -2.9582 | -50.3149 | 2026-09-17 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 1086bd64-01bf-301d-b9c3-5ea126c2755a | -5.7754 | -45.1053 | 2026-09-17 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 556.3 |
| f2860ff0-0070-356a-9ea6-49d6b69ca297 | -4.5044 | -54.9845 | 2026-09-17 00:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 872a1c38-dcb7-3091-864d-48c3f459d946 | -12.491 | -50.8259 | 2026-09-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 749c0688-54ac-3983-b332-73c0981f748e | -2.9079 | -54.1911 | 2026-09-17 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 9d9fc8b5-9148-3cc7-ad8e-b8c2ec769ceb | -9.1123 | -45.7067 | 2026-09-17 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 83b5563c-64cb-3931-9a3f-6adcc534b189 | -14.1401 | -48.7539 | 2026-09-17 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 058342a6-2c84-31a0-a012-fbd1e41577d2 | -11.2766 | -43.4829 | 2026-09-17 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 62e25ec3-0501-371a-86a7-bdfd95d61288 | -13.3758 | -57.026 | 2026-09-17 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 01ec6543-2a2d-38f5-a059-8da8c2b83d5d | -6.8032 | -59.1693 | 2026-09-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c61ea55a-00fc-346c-a5f2-1fd04cccb03c | -12.4913 | -50.8045 | 2026-09-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 3713451d-fe41-3af8-a9f4-59245af23d88 | -12.5104 | -50.8021 | 2026-09-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3a8386ac-4173-3afe-b842-ecc00477e243 | -5.7941 | -45.104 | 2026-09-17 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9332eaa9-2169-33e2-810f-1831def3f1d4 | -12.5101 | -50.8236 | 2026-09-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0251b803-5b4e-3b77-a3ab-7d6508dbabd7 | -3.4757 | -54.6972 | 2026-09-17 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| ebb6d36a-67dd-3dce-ba94-33d4d60f67e0 | -6.8031 | -59.1886 | 2026-09-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c1a1df03-ed3a-3841-906e-a89954fe81ef | -4.5045 | -54.9646 | 2026-09-17 00:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 4edd30fa-a8b4-364c-9610-629df62a16f0 | -8.4796 | -57.6478 | 2026-09-17 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fd97994e-4d62-3ff5-8ed0-b8eac6c1acea | -11.277 | -43.4592 | 2026-09-17 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 29527944-6e09-3a15-b36a-9a02c2c6c582 | -5.7756 | -45.0826 | 2026-09-17 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 41bd11fd-ecaf-3f49-9236-87fc715e1d15 | -6.8215 | -59.1879 | 2026-09-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2c6c51e9-e036-3dd4-b8f6-d43fc7bc3bbb | -2.6966 | -57.6084 | 2026-09-17 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 78fb7941-0afd-3e22-a093-b345604e7427 | -3.494 | -54.7166 | 2026-09-17 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| fa7c8038-95a4-3edc-9e21-f4596e20f441 | -13.3949 | -57.0242 | 2026-09-17 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a41481c8-3592-30c9-9011-5c4e3162fbba | -5.7567 | -45.1067 | 2026-09-17 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 284.3 |
| 047e3476-61ef-37d0-8536-afca3a615579 | -8.7604 | -66.5623 | 2026-09-17 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 24a31140-7df2-3372-80cf-cca56024eff4 | -3.4941 | -54.6967 | 2026-09-17 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| bb65c375-2b38-34bc-8c4e-fa3bcf9da07b | -12.5097 | -50.845 | 2026-09-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 19e36c68-2d99-364c-8449-14a8567080b4 | -9.4102 | -62.7113 | 2026-09-17 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| c5cfae00-bea8-305a-a39c-15404d2141b8 | -3.4757 | -54.7171 | 2026-09-17 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 215.0 |
| 97eba009-9c6a-36f5-be5f-be607786d8d7 | -9.1056 | -60.9703 | 2026-09-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 502d39e3-f45b-30c2-b524-52512c89c6df | -12.4916 | -50.783 | 2026-09-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c9b9a6e7-646d-30f8-a495-5b86c34ee477 | -12.8543 | -44.386 | 2026-09-17 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| acd549cc-68d4-3acd-83c1-5a76a4c1ba99 | -5.7565 | -45.1293 | 2026-09-17 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6a5b6fc8-61a9-31a3-9592-689dddc7970e | -9.8884 | -48.3794 | 2026-09-17 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |


[Clique aqui para ver as próximas entradas](README4.md)
