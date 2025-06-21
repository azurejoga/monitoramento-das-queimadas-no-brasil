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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0169df75-ed3e-337a-8e65-c04486707a7b | -10.46622 | -47.03764 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7582ce1-9a6e-3c93-80bc-c06de1a4a2af | -7.87168 | -47.88611 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6f99ba3-048d-31eb-a675-f5926b78eb85 | -9.46037 | -57.84101 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0da418df-79aa-3342-a397-bf61d992e399 | -14.22256 | -45.51396 | 2025-06-21 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 486faa7e-72ba-3950-bd48-1238e58a8eb9 | -13.03764 | -53.71198 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ed3b61ea-351f-36e1-a6f7-cd4245d32cd2 | -8.9796 | -49.86472 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1cebe84-c0c2-34b9-b673-2fe658f19995 | -9.25622 | -57.53466 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a7d1543e-6438-3b2c-a599-44bb046b65aa | -11.87375 | -54.66627 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3cf84936-e4ac-35ff-a37e-fca5493649a7 | -9.73814 | -48.33147 | 2025-06-21 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 543f365d-3745-3e0e-8e07-c3f6d88ae469 | -10.51741 | -47.577 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf6c0589-e2f8-3568-ab0d-87cc86267ed8 | -11.95308 | -58.75817 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8df69e4-86c9-3ea9-9407-f2390a5aad12 | -14.07983 | -53.05923 | 2025-06-21 04:34:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4780ea5c-2ea9-314a-9f88-fe1c3a3d1af4 | -11.93798 | -48.42114 | 2025-06-21 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4a0828-8059-32e5-b9f8-a7a22f5d29c4 | -8.37899 | -46.97563 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| caebe51b-daee-37b0-9a77-6af6ff41f796 | -11.26194 | -47.82122 | 2025-06-21 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6934ec44-5a78-3e12-89d8-d17e0a3f422a | -11.95837 | -58.75956 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b2ea673c-1c03-31e9-8ba7-5d1636f43770 | -12.44273 | -48.14122 | 2025-06-21 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33343c9e-e313-3624-b821-f2e6740ddaca | -10.44753 | -47.04612 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed2eda45-12d2-32d9-be73-6fb9c2b27ebb | -11.88538 | -54.67227 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c75272fc-ed1f-3e9a-af74-a58c3e67cb52 | -8.01081 | -47.66913 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d07ee1ff-55cb-3ab1-bbeb-5b08cc539461 | -9.47855 | -57.83087 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bee64c4e-81e7-356d-a8e7-2cc3887ad45e | -13.25927 | -46.82847 | 2025-06-21 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fba67e9-1875-3330-9a2c-3631ceb48736 | -13.29364 | -57.08524 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 711b57f7-9c5c-315c-86e5-a3a9accfe890 | -9.4745 | -57.82311 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a299b762-780b-32e4-879d-27836b3f5eab | -12.1632 | -48.68132 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3de4ffb1-1999-3bfb-aab3-39a7d28ee7ef | -9.01712 | -61.23204 | 2025-06-21 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae198cfc-9a12-3aa1-b169-2216f5a0f61d | -12.44219 | -48.14478 | 2025-06-21 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28aecb66-d0f8-3441-b5a2-76fd0b6e7533 | -12.51378 | -58.34897 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97a998ef-789d-34e2-9fe0-b84c9c3c4c70 | -8.1333 | -46.83116 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05ab0772-70ec-300f-945a-45b2dc6d6fd9 | -9.47488 | -57.81736 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b5eb48a-c263-3c7b-b71c-d61bf2b738d3 | -10.06945 | -49.7096 | 2025-06-21 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1708e563-d3bb-3b4d-9f3f-ac5abf0a65fe | -12.02521 | -57.09409 | 2025-06-21 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdb0c12e-a5c6-3f5d-9cf1-ff358ea741e0 | -9.47364 | -57.824 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b927626-a4e0-3b0e-af92-1e81db2ae600 | -14.81091 | -48.47662 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e21a689a-dd8a-31b6-8a79-e0b67e51e483 | -10.51631 | -47.5842 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b84bcaf3-0ee2-374f-a096-607daa2f1161 | -10.95227 | -54.37926 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c929c587-1253-3a5c-acbf-b33474b70357 | -9.47915 | -57.82752 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5dec42de-8d65-3802-9a99-7e537c870a71 | -9.4697 | -57.84974 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 647507fa-d83d-366e-b9dc-b604d8868762 | -14.81253 | -48.46587 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a938d7ed-dd1a-3b70-bf3d-94d818a65d9f | -8.02977 | -47.65826 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 84d21731-166f-326f-97a8-0ae7ae747819 | -11.91429 | -54.81459 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 603275e9-d395-3863-b0ab-6ade99ee4cd4 | -8.73309 | -47.99029 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30adc05e-3a68-334d-a557-d04f7a3c58ea | -14.96647 | -46.26458 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98994609-cdbb-3b48-9ff5-0ef4629175df | -13.2912 | -57.08789 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5364bb12-1d81-3027-af0e-24222fb44a47 | -12.29105 | -50.10189 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21f83b0f-ee82-3acc-a2f7-401f7da60f12 | -10.58835 | -46.92521 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c11ba416-f28a-30a9-b7d8-f7448b74236b | -12.29162 | -50.09834 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2d7f3d9-330c-3731-8976-f55bbf5cd900 | -8.01575 | -47.65918 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c716962c-5977-37c2-b717-deb193fedfd7 | -11.57619 | -54.56749 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20f73b56-ad74-3af1-9154-7bc960e7e38c | -10.51406 | -47.57648 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2f05f4e-ec24-39ab-ab35-4501a5b4c6f9 | -14.02316 | -53.36894 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ffae97e-9e12-38fd-b1b2-2b6b698f9107 | -10.84985 | -53.76977 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f2510f5-3123-38ff-be2e-bb11e4b80f17 | -7.61302 | -49.9347 | 2025-06-21 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3834e4a7-2b52-3213-b69c-32254da69833 | -9.48065 | -56.07608 | 2025-06-21 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a47f6f-45b9-3011-91c6-7a5448f8567d | -13.10061 | -52.29291 | 2025-06-21 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bde4c77e-6ab9-38cf-b089-358ff119944c | -12.54493 | -48.49846 | 2025-06-21 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52edbc89-9dea-3e19-81df-12fb9afaf718 | -12.88736 | -56.98209 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63bf042a-9cba-3ddd-b58c-8917cf39a6c5 | -11.17266 | -46.64814 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 791586d6-01fd-354c-827a-a526cef2c999 | -8.38009 | -46.96839 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a3c8c9f-01b3-3f9c-9508-5cd826955b93 | -10.51016 | -47.57956 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a72f66a-16e2-324d-a575-66d125916b88 | -9.33 | -47.82621 | 2025-06-21 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d16e8e0c-357c-3f20-b98d-3f3fb2a08129 | -8.00804 | -47.66513 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dac1ebb5-835c-3146-8398-4279344dec6e | -9.73869 | -48.32799 | 2025-06-21 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0061720-7793-378e-9998-f6706a3c85b3 | -9.35073 | -57.01464 | 2025-06-21 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef435697-df48-35e5-80de-a9adde79958e | -9.2681 | -57.82222 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a7e4f7b-b596-3cfa-9e37-d38b22f31e72 | -11.94232 | -58.7563 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 107102e9-a60f-390c-9d67-5858b18e19f7 | -12.42693 | -54.87477 | 2025-06-21 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3eaac9dd-9d00-3211-b133-5e15a41bad9e | -11.77543 | -54.36543 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8320fc77-fa28-3047-aa4c-2eaf7ec66d5b | -10.02774 | -54.32419 | 2025-06-21 04:34:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 29a1f325-3330-3d62-8186-911e68fa6c0f | -12.2811 | -50.10026 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aac76cf0-43ab-3de8-9989-4eb8281a051e | -10.29913 | -57.13828 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf2e4499-3429-3689-b2b9-470052538e29 | -12.51195 | -58.35872 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f2d30b53-f62d-32a4-a322-b385f6d3a95c | -9.47092 | -57.84301 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66ef13bf-5f11-3c0a-871c-016fabb78355 | -9.46465 | -57.84282 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e98e6a16-4db0-39a3-aaa2-1b5aef52854c | -12.47773 | -54.42726 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0aa2c2a3-b777-372f-a83a-50756063591e | -12.57755 | -58.38716 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b419ec5-636d-3eed-9e63-b39d3d6c61d3 | -9.4739 | -57.82645 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90b924d2-9db0-34df-a133-74198409f267 | -10.86695 | -54.31433 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8eb69643-58cb-3eaa-b113-64ca3329e94a | -12.97259 | -54.68512 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7ad7368-cc39-3437-86f1-325af13395ca | -11.27407 | -52.4674 | 2025-06-21 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d92d52b-d4ba-396c-8378-89defd9bd8d9 | -11.57237 | -54.56979 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 371cbf31-b1bb-3dad-8fab-ec019225ca61 | -12.88969 | -56.98539 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74de7eb8-953f-354a-b2bb-396469d4f7c6 | -10.03253 | -54.32113 | 2025-06-21 04:34:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6158a255-9dd3-327f-a657-405acf32e38b | -10.99309 | -45.92908 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1f8cc52-0b5d-36fe-b980-b3321cf20f64 | -9.47497 | -57.85081 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72191d73-2076-354c-bca1-0b0d8b245741 | -11.77882 | -54.3698 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 972b8b92-4b03-3d40-8c63-ce6446e3073d | -8.19537 | -47.77338 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94182af9-aba0-3cc3-8730-0895ad5f53d9 | -9.48533 | -56.07692 | 2025-06-21 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d606bc94-6f7b-375b-905e-b88693f32798 | -9.40604 | -48.43185 | 2025-06-21 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc785e2b-7ca0-3b66-bfe6-d37d5b9e9184 | -12.28385 | -50.10435 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7553dd9-4d2f-39d1-9b96-7515a8681ee7 | -9.01897 | -61.23079 | 2025-06-21 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 992a2191-654f-3648-9e07-0d7a8bcd389d | -11.7748 | -54.36904 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21961328-e83e-32c4-b180-70b3d6486c32 | -9.50833 | -45.44657 | 2025-06-21 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d290c31b-fb1a-32e2-bb74-88064d0fe765 | -10.95912 | -49.57233 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6befec1c-7866-36c3-9cb9-3acea4fdb93f | -12.1588 | -48.68785 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0844bee8-8339-3115-b034-d030f7df40bf | -11.93831 | -58.74828 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2f51f9b-e520-300b-9953-262eafdeedef | -9.50657 | -45.43345 | 2025-06-21 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1088818c-c2e8-30d9-b0ce-234d929f8ad8 | -12.97629 | -54.68222 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33b6c0f5-01c4-3ce1-8ce5-36b2d6a93920 | -10.53083 | -47.57911 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 134922de-ba7c-35d8-8511-3f7b0d6301c9 | -12.02623 | -57.08866 | 2025-06-21 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README17.md)
