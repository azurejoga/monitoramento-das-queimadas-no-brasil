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
| cc0c7081-4095-37fa-a519-f355932370cb | -12.4798 | -57.2063 | 2025-05-20 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 195.5 |
| 61a3c882-c785-3b08-8629-0614ce34f5ea | -11.4265 | -44.7476 | 2025-05-20 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 59197b86-c236-322c-90a8-2fe2ea72626d | -12.48 | -57.1863 | 2025-05-20 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 530.4 |
| 40245f94-8efe-3eb2-ad69-469666016248 | -12.461 | -57.1879 | 2025-05-20 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 52d46651-4cd7-39ad-96b7-9de696ddfc6a | -11.4465 | -44.6983 | 2025-05-20 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 12dcc6d1-1983-384f-92ce-a84208465cf2 | -12.3515 | -49.9833 | 2025-05-20 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c52e3303-39ea-3648-8fe0-22a38ceccf4a | -12.3522 | -49.94 | 2025-05-20 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a8846f0c-2dd9-329f-a557-e85de7dfff6b | -10.4346 | -49.9019 | 2025-05-20 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 8cc598ac-952a-3f68-a808-31fcd5486dcc | -11.8863 | -46.9179 | 2025-05-20 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 8faff190-56c5-3913-af01-4e14500b2590 | -11.4461 | -44.7215 | 2025-05-20 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 8ded37bc-1141-35fb-8596-d61d90aabb6b | -10.4346 | -49.9019 | 2025-05-20 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 7276ea06-6cb0-3a0c-a0ff-284b74d3382f | -6.2228 | -43.3226 | 2025-05-20 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7059151c-b661-3640-bd41-21eb3560c138 | -12.4798 | -57.2063 | 2025-05-20 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 13edf55e-b15c-3a5c-8b7a-36cdb0b3c39a | -12.3515 | -49.9833 | 2025-05-20 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| acea76e9-67e7-35a9-a939-c3f9b028bb16 | -12.2949 | -52.4575 | 2025-05-20 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f66a25ea-dd01-37bb-8a4f-b6d028b280bc | -10.2703 | -46.7889 | 2025-05-20 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 72e2bfab-ce8c-39c5-8349-8d988ab48270 | -12.461 | -57.1879 | 2025-05-20 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 581c6db4-88ec-3095-9135-009aae24464f | -12.3519 | -49.9617 | 2025-05-20 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 608a0c06-bd15-33fd-81a8-92e35a5ffbfa | -11.4273 | -44.7011 | 2025-05-20 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4449830c-6172-383a-a758-96084ea68498 | -12.3327 | -49.9641 | 2025-05-20 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d5178546-89b7-3c8f-949b-9ad8809fbe13 | -6.204 | -43.3241 | 2025-05-20 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a67a5b8e-3aaf-328f-a732-5a46752f05a6 | -12.48 | -57.1863 | 2025-05-20 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 552.5 |
| 5b3927b4-2f45-3e20-88d7-7ce369c2afbb | -12.3522 | -49.94 | 2025-05-20 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9eb4d325-4784-3be0-8b9c-5f646c9f43f7 | -11.8859 | -46.9404 | 2025-05-20 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| f01cfe7e-1c75-3b96-9334-41535c5259e8 | -10.251 | -46.8136 | 2025-05-20 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2d1b4e84-2577-3919-8e4b-eee141ec7ee0 | -12.2946 | -52.4785 | 2025-05-20 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| a218841e-ef6a-3f12-b749-26b52cdf1076 | -11.4265 | -44.7476 | 2025-05-20 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d9258825-1af9-3741-8a88-d9d90821bf73 | -12.2946 | -52.4785 | 2025-05-20 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 0ab10515-f20c-3977-9f12-83c10771685e | -6.204 | -43.3241 | 2025-05-20 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3b914c45-a3cc-327d-9c33-523964fe25a6 | -10.27 | -46.8113 | 2025-05-20 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a527676b-81e1-372e-b57e-106f91579bba | -12.3327 | -49.9641 | 2025-05-20 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 592d13e7-d6c5-3b41-8914-9c8c4a07d404 | -11.8863 | -46.9179 | 2025-05-20 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 8472479b-677d-3a77-b4a8-895236cdf62e | -10.4346 | -49.9019 | 2025-05-20 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 075ceebe-230b-3313-80c5-3e4cfc595339 | -12.3515 | -49.9833 | 2025-05-20 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2d234217-57eb-3178-b2f3-b3d3934f14f1 | -14.6805 | -45.1191 | 2025-05-20 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5124f7e2-e687-342b-86ee-cad9d740fb26 | -11.8859 | -46.9404 | 2025-05-20 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 764ae937-2ef9-39cb-9b74-a54db69ac13b | -12.48 | -57.1863 | 2025-05-20 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 502.2 |
| 27b096c3-df04-330e-9b2f-e544acafc3ef | -12.4798 | -57.2063 | 2025-05-20 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 196.2 |
| 3de3234e-643b-3bd3-b132-9c16da682ee3 | -11.4465 | -44.6983 | 2025-05-20 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9d08f3ea-a372-3e1f-8dfb-553453277545 | -10.2703 | -46.7889 | 2025-05-20 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 3599bc5c-0948-3b97-a93e-84dc169f2455 | -12.461 | -57.1879 | 2025-05-20 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 59e87614-62ab-3767-9027-5caa024dd73f | -12.3519 | -49.9617 | 2025-05-20 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 5a2a3f8f-fc97-3683-8ae8-a0847be07502 | -10.251 | -46.8136 | 2025-05-20 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 69ad5e93-ca83-382d-bd76-4af64c15752b | -11.4273 | -44.7011 | 2025-05-20 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 0791f7fb-ec63-3321-8989-17aada19ee6a | -6.2228 | -43.3226 | 2025-05-20 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| aea94fcf-046c-3e84-9ecc-388628a1dc4f | -11.4269 | -44.7243 | 2025-05-20 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 66c0705a-f0e7-399e-9183-41d1da37488f | -11.4461 | -44.7215 | 2025-05-20 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| ad83b060-b373-30df-ad96-df12ea652bb4 | -11.8863 | -46.9179 | 2025-05-20 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 7f32a756-d444-3187-a252-5647404284e3 | -12.3519 | -49.9617 | 2025-05-20 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 8b01985e-6b8f-3812-9f87-a7937ece4eb9 | -10.2703 | -46.7889 | 2025-05-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 38e5713c-ffff-369b-8711-796acec7b633 | -12.2946 | -52.4785 | 2025-05-20 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 9e5cbcd8-ca16-36a1-ae4b-b4e6591edb7c | -10.4346 | -49.9019 | 2025-05-20 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 9445aa99-e495-370e-871c-753d86945c30 | -10.2514 | -46.7912 | 2025-05-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| fd5c7e88-af57-3b05-b329-40e46f5980c7 | -12.2949 | -52.4575 | 2025-05-20 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b9ad5c06-aff4-3b46-9e4e-52d06b932d8e | -12.3515 | -49.9833 | 2025-05-20 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a5796a43-e0f9-3015-bcd7-395d41904686 | -12.461 | -57.1879 | 2025-05-20 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 93faa098-73f1-3b3c-92e4-47dc4d1c3e93 | -10.4156 | -49.9039 | 2025-05-20 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 65a94fef-5be1-3fcf-9c99-6950b80996a3 | -10.27 | -46.8113 | 2025-05-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 30785190-a392-3d63-ace3-63efeb36b501 | -12.3327 | -49.9641 | 2025-05-20 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| d475130c-2ddd-386a-ba12-87202958e77d | -12.4798 | -57.2063 | 2025-05-20 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| a64358a3-6050-3a64-9c72-a9d801dd6b97 | -11.4273 | -44.7011 | 2025-05-20 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 5ff33eca-328d-31b6-916f-31901a1895e2 | -10.251 | -46.8136 | 2025-05-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 271.8 |
| 33644ca2-fb25-3d9b-b46e-3b9761982639 | -11.4269 | -44.7243 | 2025-05-20 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 259.4 |
| 582b06f7-2c8c-3993-a779-a72ef03aea99 | -12.2756 | -52.4806 | 2025-05-20 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1f67d385-b67e-32af-ad79-17c7c70ce149 | -11.8859 | -46.9404 | 2025-05-20 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 201.6 |
| eccd8037-b920-3978-b316-a85d0f9fd86c | -11.4465 | -44.6983 | 2025-05-20 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5560214a-33da-3b55-986d-2e147af313cb | -6.9135 | -43.7281 | 2025-05-20 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 83daf871-dd0e-3304-b9ef-8b9a47a61591 | -12.4798 | -57.2063 | 2025-05-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 70882d3a-4bcc-369b-b93b-7f2a31b9b136 | -10.251 | -46.8136 | 2025-05-20 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 8c75e136-9694-31bb-881d-6de251fb4abe | -10.27 | -46.8113 | 2025-05-20 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| db667749-fc76-378a-b72b-14551a74971b | -11.8863 | -46.9179 | 2025-05-20 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 296eaadb-1d7f-3456-ab81-a8a6616dc703 | -12.461 | -57.1879 | 2025-05-20 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 7f7c4068-8ac9-3f33-8776-b766f95f24e4 | -11.4273 | -44.7011 | 2025-05-20 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| d0d4ec12-af95-3c5a-ae12-af7e6da2e041 | -12.2756 | -52.4806 | 2025-05-20 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c52e3694-381f-32f5-ad72-01c0ac6cb801 | -10.2514 | -46.7912 | 2025-05-20 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 14480c58-5915-3544-933f-3b713299a5d0 | -12.3515 | -49.9833 | 2025-05-20 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| b1368490-1918-381d-8ba1-c502fe9ba813 | -10.4346 | -49.9019 | 2025-05-20 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| f4f52538-a0bd-3768-b29b-525ed22e6b74 | -10.4156 | -49.9039 | 2025-05-20 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| ced93ddf-3234-3a5d-89c5-44e030e354c6 | -12.3519 | -49.9617 | 2025-05-20 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 193.0 |
| d724ae44-923e-3e54-a116-62734a11079f | -10.6091 | -46.9716 | 2025-05-20 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 30adc60c-bfa3-35c0-b213-4bfd9fa78808 | -6.9133 | -43.7514 | 2025-05-20 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| b9a0698d-5317-31e4-a85f-e137f4af2d37 | -12.3327 | -49.9641 | 2025-05-20 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b79218d7-4e4b-3fe0-a810-7187be52ed5f | -11.8859 | -46.9404 | 2025-05-20 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |


