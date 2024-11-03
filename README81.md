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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6189aa6f-fb6e-319f-9787-8f78cf81cc53 | -6.05051 | -55.60378 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77588fce-1108-33ab-907d-6a5b0e31bc96 | -6.05164 | -55.61883 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22fd17fa-327f-3b7e-9fee-256a30379304 | -6.04994 | -55.60741 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c24e0d1c-7d30-3165-b903-aac4f192622f | -11.11342 | -56.10673 | 2024-11-03 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbe481ef-bdc7-3953-9358-006b2446c4da | -11.10995 | -56.10619 | 2024-11-03 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 45635c48-14b9-3046-a451-efea9dc436c3 | -4.00979 | -55.55748 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 891e2d0d-b063-39bd-b9bd-a2c0a96b3b9d | -4.00752 | -55.54987 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e973a8bb-5f58-3864-8554-cc6e23e610a6 | -3.99344 | -55.60975 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40e9c74c-c91f-3b8a-9bd4-12a24dcf55b4 | -3.83975 | -56.11007 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dff5974f-dd3f-34eb-8044-5396293dd3d5 | -4.61691 | -55.66538 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1f2023b-9eb9-31d1-8132-b7f2a37a97d7 | -4.59013 | -56.13345 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18a5c8bc-ce76-3f83-a972-4ceb7c886300 | -4.56076 | -56.1328 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d9a9c20-7774-342a-9300-e0e7212d58b1 | -4.40563 | -55.81772 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c192a967-4923-3c8c-9778-3de708af22a1 | -4.40548 | -55.69883 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47c925fc-3b6f-3ee6-a194-a9297d5a7c10 | -4.40157 | -55.70185 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2fcbd23-ab08-3594-9126-d5e848b38803 | -4.36699 | -56.08829 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76abb789-2654-3da7-9ff4-2569f5235d47 | -4.36645 | -56.09179 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c216d789-701e-32ed-9ebe-b31ce11df44e | -4.3642 | -56.08428 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eec3d964-1b36-37f1-ba49-a707ff992ca8 | -4.36311 | -56.09127 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48021fc3-c6dd-39fe-bd0c-7a55b8f37b8c | -4.13462 | -55.54025 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31b72e73-4374-3324-bfd4-23c410f64a4b | -4.07288 | -55.82751 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6c7d62a-0210-3bf4-8cc3-fb04cd6b0cd7 | -4.07018 | -55.8308 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb3379de-ab4c-302a-a4ce-1963b364eae0 | -4.61141 | -55.99685 | 2024-11-03 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1bbeb5d-6e14-3d91-808e-7e41bb8aac03 | -4.54903 | -56.09872 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c51e26ad-f628-31bb-b833-3d55d95afc42 | -4.48235 | -55.65596 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82e38fbd-48d4-37bd-8acb-87ac85a89c2f | -4.41356 | -55.85503 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5684c777-787e-3737-a723-5ed71fbb9422 | -4.40618 | -55.8142 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4e95b9-fb54-3d87-bec6-0a8d74cb5c80 | -4.36754 | -56.0848 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b914b99e-57ab-3789-8b9e-9b3e8ae09f41 | -4.36475 | -56.08079 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e645d368-3d49-3028-aa10-59f47b978b8f | -4.36366 | -56.08778 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7e6f336-9673-3d0b-b03c-4d6dcbe61600 | -4.34853 | -55.5113 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0586efe-d8aa-3cbf-bfea-1eac2bdd6562 | -4.33816 | -55.62288 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88be09ea-a0c9-3d66-a802-72afb49a599d | -4.26853 | -55.46185 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 48365b5f-354b-3847-af07-098967022bc7 | -4.24479 | -55.87902 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0060218-715b-3906-ad39-a091c2630e27 | -4.13572 | -55.53313 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dc4fc33-c325-36e6-8757-bd67c7711e78 | -4.13517 | -55.53668 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c790826-0ec7-3af7-a2f4-755de45ea612 | -4.1307 | -55.54326 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e83005d-0052-3100-aef5-73144b9fd044 | -4.08588 | -55.46723 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01818fbd-dd6a-3042-affe-c885fc850ebd | -4.08532 | -55.4708 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1918b33-976f-3648-ac7d-e70236024018 | -4.08195 | -55.47026 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b19ebe7e-e841-3673-946c-b340452bf1e5 | -4.07073 | -55.82729 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8599c484-c635-34e2-9fee-317e6659cafb | -4.00697 | -55.55343 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fe86a83-49db-3ec8-89e2-6ace16ba21b9 | -4.00642 | -55.55698 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 707d6bf4-1b64-3f7d-ab05-34df15a0ea11 | -3.94909 | -55.54119 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c2764a8-5e0c-317e-9a5e-fe9ef80bb644 | -3.51509 | -58.47013 | 2024-11-03 05:10:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 025c080f-1294-3760-a864-f7349692cf24 | -6.40386 | -51.06484 | 2024-11-03 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d007e54a-c328-3ff9-aec2-9603eb41c610 | -6.40323 | -51.06909 | 2024-11-03 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a0bf283e-7b43-3de7-8e2c-cc2dffd615b9 | -6.40306 | -51.06812 | 2024-11-03 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 85d0b7a9-f22f-3937-9237-892cca97b08b | -6.39884 | -51.06853 | 2024-11-03 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 016d117f-8587-398a-83d0-e3531907e4da | -6.39947 | -51.06427 | 2024-11-03 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd5a8ac-1f89-3cb3-ba39-6aa3980b32eb | -7.13177 | -50.09607 | 2024-11-03 05:10:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 371aae0f-6cc9-34c0-bf59-4509a8bae73e | -2.85565 | -64.97383 | 2024-11-03 05:10:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47f6c9d5-f3a2-3078-b0e2-d2267a5fabef | -6.05565 | -55.61901 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66987baa-547c-34c6-b205-f85b1f64abaa | -2.85052 | -64.973 | 2024-11-03 05:10:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02729280-6aa7-39d7-b470-52878f5e991f | -2.84588 | -64.96918 | 2024-11-03 05:10:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfe312f3-45d6-3f4e-984b-f76961ad0594 | -2.84538 | -64.9722 | 2024-11-03 05:10:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03f7dd7f-4ee4-38bc-b8c2-99e4dface20f | -7.28235 | -44.69536 | 2024-11-03 05:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79eab4a7-ff4e-3803-9493-7a5b40ec9c3c | -7.2763 | -44.68885 | 2024-11-03 05:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdc2e6d8-6833-34ed-9a50-36803a322746 | -8.55075 | -47.97409 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a16e3bc5-6067-3c0b-9503-b8137016d1bc | -8.54862 | -47.97229 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39a34ca8-292b-331d-81f3-49d61dceffc0 | -8.54812 | -47.97614 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e39d440-c402-3a5b-bba0-2ea8856aeab4 | -8.54763 | -47.98 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e26ff156-78c9-30fb-abc8-4433e446f4c3 | -8.54567 | -47.96955 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73e4e24e-b1ca-3b20-a693-fff70354a812 | -8.54516 | -47.97329 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a1813da-d636-30ae-b245-7304cdf5df14 | -8.54464 | -47.97713 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 192ee66d-4a44-3450-a358-fa66f28e4e0a | -8.54413 | -47.98091 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3415a347-19ac-31e7-bb23-a799fa1778cf | -8.54302 | -47.97152 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 37bc766b-b990-3ade-b7c7-c59338d8c17f | -8.54254 | -47.9753 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3809c9c-42f8-3bdc-be93-f3281171a0d3 | -8.54206 | -47.97906 | 2024-11-03 05:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 733c227f-c94d-3a21-a6f1-c0d1b8bd8544 | -8.48377 | -47.7886 | 2024-11-03 05:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11645401-1442-39e2-ba28-db29011f2115 | -8.48328 | -47.79238 | 2024-11-03 05:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7520e5a4-7be4-3f3d-8b56-0e926583b6ac | -11.64229 | -48.04307 | 2024-11-03 05:10:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a79c0590-f60d-3f03-8c9a-94e595055782 | -11.636 | -48.04644 | 2024-11-03 05:10:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d8ad7c2-6075-37d6-8e92-5f3ad43f84c6 | -6.22661 | -49.54354 | 2024-11-03 05:10:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 061e828d-2ee1-30f2-9b40-15a2bcdf19a5 | -5.34344 | -49.45567 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c1fce47-0e68-3af6-ba94-e429edf01481 | -5.80535 | -49.37595 | 2024-11-03 05:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b0cd57d-c4d7-3c70-9d40-f8a46ac12ca6 | -5.34596 | -49.44954 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cbec5b0-1da2-3a4f-a7fd-fc2b44c5df1b | -5.34518 | -49.45476 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee7017f-46b8-389b-90f7-e5ac761cd0f9 | -5.34417 | -49.45043 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d757528e-0c37-3971-a6c2-e36c953fe3b1 | -5.34037 | -49.45403 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50ad6a63-9822-3bf4-86e9-39a8080e644f | -9.48699 | -48.94119 | 2024-11-03 05:10:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f348c41d-3867-3763-b9de-6abb2205d134 | -10.88863 | -49.59074 | 2024-11-03 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f614e4d-7e23-3b12-a75d-079e76d5a245 | -10.25163 | -49.45098 | 2024-11-03 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bd63e66-b915-3233-a8f3-f8ec3c138da5 | -10.25122 | -49.45407 | 2024-11-03 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfd323b7-67bc-319e-9336-ad955a21fc7a | -10.24644 | -49.45028 | 2024-11-03 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a7b73f0-0078-38eb-9e2c-0d9f524669ac | -10.24604 | -49.45334 | 2024-11-03 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49229eb0-5283-33f5-aa88-6208d5ad52db | -10.24563 | -49.45644 | 2024-11-03 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49124de2-a3ad-3672-b1f5-0110c6d4e404 | -10.24522 | -49.45953 | 2024-11-03 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66bf250f-3dad-3e90-8545-3d3aafe09863 | -10.2448 | -49.46263 | 2024-11-03 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53200a33-0bf2-38b8-a398-8db0c9236b4e | -12.2585 | -49.77659 | 2024-11-03 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23f57991-6df7-3730-a8de-84283e9e4daf | -11.29314 | -49.67054 | 2024-11-03 05:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53d5af3f-2a5e-3ba6-991a-0f8c01309f64 | -11.29273 | -49.67368 | 2024-11-03 05:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272cf46d-002a-3fed-ad9f-21de26efc6d4 | -10.89381 | -49.59144 | 2024-11-03 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52361dad-fc5a-395e-9d62-8caa0232efb9 | -10.89337 | -49.58999 | 2024-11-03 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d06ef109-86b8-3789-a986-c88faea9c440 | -10.89295 | -49.59312 | 2024-11-03 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd7b017-5155-3451-9bc0-1ef5cda29fac | -4.96447 | -49.65528 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c947f883-a227-39cd-8ee4-e28747582f14 | -4.96372 | -49.66038 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 391d5350-cde6-383e-8d54-b893ee88d5b7 | -4.83168 | -49.83078 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 228dcdf2-ff16-3b6e-8d30-070b9d946311 | -4.83312 | -49.82101 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba8479bf-736b-3990-b10d-9263256b0c7d | -5.33684 | -49.54414 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README82.md)
