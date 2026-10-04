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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43300563-6b6c-305c-b091-2779f93af3da | -2.8163 | -54.133 | 2026-10-04 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| df5b54bd-39c3-35c8-8a40-602d89691e87 | -2.8164 | -54.0929 | 2026-10-04 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3eae2ccf-56ca-3cb0-bd0a-4983aa603a82 | -9.4574 | -40.3641 | 2026-10-04 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.7 |
| 3e140523-a78f-30dc-9785-8971dd977030 | -4.3072 | -50.2668 | 2026-10-04 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c2a11c0e-abbf-32b5-b898-669ce0a499aa | -2.5842 | -51.8623 | 2026-10-04 01:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 1d58a427-6115-3672-ae1c-633451b7a969 | -4.2744 | -46.3846 | 2026-10-04 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 1db23d72-5b14-38ca-ac1b-a017ff8cd25b | -3.2951 | -53.8395 | 2026-10-04 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 12d9c089-3d4c-398e-b526-5e7f0c102d6b | -2.5842 | -51.8829 | 2026-10-04 01:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5a91c796-018d-3eb1-9bbb-e336d0acd566 | -2.8163 | -54.1129 | 2026-10-04 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 11d56a4a-9c63-3372-aa1e-557925579cf2 | -4.2745 | -46.3624 | 2026-10-04 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 2072c788-5366-39e5-bf80-53fcb897eb1f | -2.8347 | -54.1125 | 2026-10-04 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c00ab0d1-db27-3729-afe8-ee78dd91296c | -3.8756 | -55.8184 | 2026-10-04 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 216516fd-2a45-3cc6-a729-ad9715eb3f10 | -4.2744 | -46.3846 | 2026-10-04 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6e3507fe-d409-3281-97fa-840a4d46b836 | 1.9134 | -55.7419 | 2026-10-04 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a45fa98e-db4b-3d2b-92f9-4804d9927a41 | -3.5128 | -54.6162 | 2026-10-04 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8b45f65c-3e73-35a3-904a-5c156c8d26d1 | -3.8573 | -55.7992 | 2026-10-04 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| aa9baadc-016c-3887-be39-2c7e33155bd7 | -9.4574 | -40.3641 | 2026-10-04 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 347.0 |
| 6e171374-6b94-3f02-b846-96e74b0e73e5 | -4.2887 | -50.2675 | 2026-10-04 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 444.6 |
| 5307b938-9a49-3f26-bca0-ecdca529ff4c | -3.1839 | -54.0839 | 2026-10-04 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f90c0569-a708-3398-bab3-7f8a92b9788f | -2.8163 | -54.133 | 2026-10-04 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 8d5862a1-8c23-3aa9-b9e9-48a2c22b6755 | -3.1115 | -53.7637 | 2026-10-04 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1de41c29-670e-34e6-af79-10d83a57d111 | -9.457 | -40.3889 | 2026-10-04 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 495adf90-b462-3f4f-96af-6415450c7234 | -4.2702 | -50.2683 | 2026-10-04 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 04c967e8-c957-3f71-9ef4-1c123fd6db04 | -2.798 | -54.0933 | 2026-10-04 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6d8a4fb0-f681-3cc6-b0c9-3ee20bca79ba | -3.8757 | -55.7986 | 2026-10-04 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 47413569-ed7b-3612-abe5-c7d104b2fecc | -4.3072 | -50.2668 | 2026-10-04 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c4928b4f-90ab-3538-a6b1-711513b949b1 | -9.4765 | -40.3613 | 2026-10-04 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.4 |
| d564254d-3f1a-313f-a594-5b1916d17e1a | -9.4578 | -40.3392 | 2026-10-04 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.8 |
| b0ea1e3a-fab9-3718-adce-b26af74aeef3 | -3.4761 | -50.1094 | 2026-10-04 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4a171d82-936c-373f-88f4-2ee827338f25 | 1.9133 | -55.7616 | 2026-10-04 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 48293a7e-db70-35a6-aacd-60ff96010e92 | -3.13 | -53.7229 | 2026-10-04 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 2cbbcaf2-66c1-3252-80c1-7b94dc1945d7 | -2.5842 | -51.8623 | 2026-10-04 01:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| ee8fb57f-20df-330b-b6e4-ae30856b3c41 | -4.2558 | -46.3855 | 2026-10-04 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| f962b5a9-5fd1-30f9-aad9-3aecba064d9a | -2.7979 | -54.1134 | 2026-10-04 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1a9c7bfc-8dfd-3649-9dcb-54967583dfb3 | -4.2886 | -50.2886 | 2026-10-04 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 275c9f7d-ae53-3253-84aa-724c947a1c12 | -3.8573 | -55.8189 | 2026-10-04 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ecf2b417-a97f-33ec-8a7b-a06019dd8762 | -3.1116 | -53.7234 | 2026-10-04 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 1831117c-f9a6-3254-bf97-040c3c9521bc | -3.1116 | -53.7436 | 2026-10-04 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 234.3 |
| c344a9eb-1b86-32a5-a1c0-3c54a30dea08 | -2.5842 | -51.8829 | 2026-10-04 01:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2fa8373a-c0e5-3c32-ac03-7716f4a2a8b0 | -4.2888 | -50.2465 | 2026-10-04 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 87afdfa2-be00-32b3-8fe3-ae0735a20ef3 | -4.2559 | -46.3633 | 2026-10-04 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 137.8 |
| cbccc499-191b-3d15-9aff-c03785e0e051 | -2.8164 | -54.0929 | 2026-10-04 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 90976fe8-1f73-355b-b71c-d6b124e76fc1 | -2.5843 | -51.8417 | 2026-10-04 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1b8c337c-7148-3bc7-aa5a-b0e26892d28b | -2.8163 | -54.1129 | 2026-10-04 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 16963c29-72b3-3259-a80c-164dc6ed9594 | -3.4762 | -50.0883 | 2026-10-04 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d8071d99-15a8-31c0-ab14-b7af863323b7 | -2.2297 | -53.7026 | 2026-10-04 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 283ce95c-b0d9-3cba-9706-62207d67144a | -3.0721 | -49.5313 | 2026-10-04 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2a552eb5-7d25-30fb-b3e2-4876862f57af | -3.1299 | -53.7431 | 2026-10-04 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 5d13bcb0-0e02-36ba-9601-f1bce3b9db22 | -4.2701 | -50.2894 | 2026-10-04 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 85792a85-4158-3b9b-ad27-72eae85d3ad4 | -3.1116 | -53.7234 | 2026-10-04 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 197.1 |
| ae2a4734-a792-3977-b10a-32e676d8bec1 | -3.4761 | -50.1094 | 2026-10-04 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 04cd44f9-0585-37ce-8665-e3cd17fd5ce4 | -4.2702 | -50.2683 | 2026-10-04 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 6a408c2c-db24-32db-9f50-488e0131cd29 | -9.4574 | -40.3641 | 2026-10-04 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 501.8 |
| 831f5a39-fab0-3677-8556-891d535f5a3b | -4.2558 | -46.3855 | 2026-10-04 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| b2cceb4c-298d-37a4-a492-13814ffcf68a | -2.8163 | -54.1129 | 2026-10-04 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a06e3ec0-8e7f-334a-b070-f495b0bf107f | -3.1116 | -53.7436 | 2026-10-04 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 520af277-b13d-3a43-8419-94659155d150 | -3.1839 | -54.0839 | 2026-10-04 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e6a8db3c-2971-35f9-9c55-6d9657589dde | -2.8163 | -54.133 | 2026-10-04 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 3f9d55ab-4cd4-30f7-aa36-e82392c587ef | -2.5842 | -51.8829 | 2026-10-04 01:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 90cb1470-a900-34ec-a4fc-8abcdac8a37d | -4.2744 | -46.3846 | 2026-10-04 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 66de3381-3aad-357d-b451-a6799addc95b | -3.4762 | -50.0883 | 2026-10-04 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ad8cb813-c883-39cf-801c-8bcdf92ca6fa | -3.072 | -49.5525 | 2026-10-04 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d0f7fcf8-cdb6-3a23-98d3-d3e57bf3815c | -3.0721 | -49.5313 | 2026-10-04 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 0c1505a2-0ae3-3dc9-b5bb-5da2b0c6df62 | -4.2745 | -46.3624 | 2026-10-04 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f493d37e-e21e-3365-bf0d-90c29ca85ef0 | -4.2701 | -50.2894 | 2026-10-04 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8b4b2a43-9fac-37cb-8309-ebc5846d1d5a | -3.13 | -53.7229 | 2026-10-04 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 830897fb-a7cc-3803-b1b6-22252c68d5db | -3.4577 | -50.089 | 2026-10-04 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 92e0e99c-6ae3-3492-9864-e73e0681c443 | -3.8756 | -55.8184 | 2026-10-04 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 1449f96b-e4e3-309f-8fa3-083fd5061790 | -9.4765 | -40.3613 | 2026-10-04 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 401.2 |
| 84130b55-bb89-364f-af88-6f8bcd8429f7 | -3.0932 | -53.7441 | 2026-10-04 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1a27bbe2-12e4-3abf-a808-1f5f47b4bece | -4.2888 | -50.2465 | 2026-10-04 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8f6c9d4a-2cd0-3e0d-92a2-e6230f069e8d | -2.798 | -54.0933 | 2026-10-04 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6e9040b5-ce78-308d-8626-6ab566fd8a70 | -4.2886 | -50.2886 | 2026-10-04 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 49cbb074-9d61-3d72-95da-af003f27bb2c | -9.4578 | -40.3392 | 2026-10-04 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 142.4 |
| 022dcfca-ea9e-3930-99a8-1a56126ef7fb | -4.3072 | -50.2668 | 2026-10-04 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| ed36f233-7b43-38da-8502-8e5225fb0365 | -2.2113 | -53.7029 | 2026-10-04 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1f6a6870-54e7-37bc-922f-881f67fcf74c | -2.2297 | -53.7026 | 2026-10-04 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1526d32c-f3f1-3219-8abc-4dc9a3956a02 | -2.5842 | -51.8623 | 2026-10-04 01:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| d917f966-7ea4-377a-bbd9-f007083e6a9a | -3.8757 | -55.7986 | 2026-10-04 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| be1bb8ab-1dfe-30c1-ac87-b6540ae5fdb0 | -8.5551 | -67.0686 | 2026-10-04 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 94dd319f-7420-3b67-aef8-6e1411a5aa2e | -3.1299 | -53.7431 | 2026-10-04 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 41740e8e-e6b1-3c30-9c84-d3683c22ab1d | -9.4769 | -40.3365 | 2026-10-04 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 453c7329-8186-3ee4-a9b7-b4ed5a0947ad | -4.2887 | -50.2675 | 2026-10-04 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 486.7 |
| a9dbee41-1756-3089-9d02-d2c1019c8e72 | -9.4383 | -40.3668 | 2026-10-04 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 48f24691-352c-309d-93c2-c24f0e042d25 | -2.7979 | -54.1134 | 2026-10-04 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d312cd91-09cd-3b35-98b8-97e5cd7b2b73 | -2.5843 | -51.8417 | 2026-10-04 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a9e6fc8b-3412-38ba-801d-965f2ee55191 | -2.8164 | -54.0929 | 2026-10-04 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 75781f78-6b12-35c1-8206-217039f6bf1a | -4.2559 | -46.3633 | 2026-10-04 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 2029d9d9-834f-374d-8eef-0606e1f5c000 | -9.5137 | -54.6292 | 2026-10-04 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 09f354ca-3d45-32e8-b9eb-28b949c8ea32 | -3.072 | -49.5525 | 2026-10-04 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9f3dcd7b-b8e6-3ca9-bdfe-f6701aea4b37 | -4.2886 | -50.2886 | 2026-10-04 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| c4342f1f-97ff-36d8-bcb0-55759037f35a | -1.6215 | -55.0129 | 2026-10-04 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 0421ea72-3b26-3c60-9b2b-33acb44f47cc | -3.4761 | -50.1094 | 2026-10-04 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6a44f528-98d2-327a-b11d-fc3d29057870 | -2.8164 | -54.0929 | 2026-10-04 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a23b5918-d90d-3c9a-8231-803f708db6a4 | -4.2744 | -46.3846 | 2026-10-04 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 78b69e5f-c9c1-3332-9a5f-c61a47fcd5df | -3.0932 | -53.7441 | 2026-10-04 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2654279e-79d8-3b78-94c1-a011f84a694d | -2.7979 | -54.1134 | 2026-10-04 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| c3584635-39c9-357f-8dfd-12bf5ad98744 | -4.3072 | -50.2668 | 2026-10-04 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 056db4d7-e00f-3348-80c6-58a6d6545482 | -3.1299 | -53.7431 | 2026-10-04 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| d5d1b679-904b-3ffa-b2eb-d28086f2684a | -2.8163 | -54.1129 | 2026-10-04 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |


[Clique aqui para ver as próximas entradas](README18.md)
