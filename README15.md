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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 621148aa-4512-3cc4-b8b0-0529e846db8f | -13.14377 | -56.80396 | 2025-06-21 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a897e0c3-3355-350a-b914-0c5b5379f611 | -10.03043 | -48.65993 | 2025-06-21 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ff562bc-d9a1-3284-84b6-e67d86255792 | -13.04409 | -53.71663 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 599caccb-a897-3ec5-90e3-96e36e6d8f76 | -12.47827 | -60.13737 | 2025-06-21 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aa58da3d-a0ae-3443-a49d-d8aaf5984012 | -11.33707 | -45.22894 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c34dbf5-80e3-3850-b3e1-57e93a38dbaf | -9.41757 | -48.42299 | 2025-06-21 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ede92bb5-466e-34a5-aa2c-756735bdb950 | -10.45037 | -47.05037 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0cd1763-3196-3f75-a8bf-b5d3e370438b | -12.42349 | -54.87028 | 2025-06-21 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88853b51-b2fb-3dfc-994c-5d427f6e07bb | -11.784 | -57.24775 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| eda02194-f462-3f1b-bd13-275f54650aa7 | -11.86749 | -52.25468 | 2025-06-21 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76041952-9e8e-35e5-b5dc-bcbcacad4358 | -12.472 | -54.42619 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b539bd2a-0b0b-3440-9997-c0d05ed605bf | -11.08358 | -55.05264 | 2025-06-21 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5279ef8e-6069-3bc4-83e6-c41f0716d9e2 | -9.10178 | -50.03245 | 2025-06-21 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40011855-2707-3adb-a2bb-cf1605065b92 | -12.28993 | -50.10899 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4e952b3-dd71-36e2-8403-2742bd3710a6 | -9.12421 | -49.66155 | 2025-06-21 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 096eb018-0615-3f13-b72f-c1a6096d98a3 | -11.17846 | -46.65697 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0888b827-759e-34b1-a202-93420e220cec | -10.44524 | -47.03815 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce00512-6084-30cd-9fe0-8e69112d87ad | -9.33332 | -47.82673 | 2025-06-21 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31b05398-3b47-3243-a152-2a6195f7b61e | -10.15252 | -48.99024 | 2025-06-21 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b1e66821-b5e3-3bfb-b3d5-aba924f59efd | -11.53308 | -56.97873 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f00894f7-1556-34fe-b9f6-6121f43ed6bf | -7.28076 | -49.99086 | 2025-06-21 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bffe558-3412-33c8-a60d-cf54a3084f80 | -9.33278 | -47.83024 | 2025-06-21 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe0d9d6f-ff68-3267-9714-64663add964a | -9.47764 | -57.83171 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ea35555-e3f2-3076-bb72-46e0c75727fa | -10.45093 | -47.04665 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 795e96df-7f44-312c-9180-fae4ad65cba2 | -13.04143 | -53.71267 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 26c4d6c1-9b85-3b4b-a6cf-04c361cfea40 | -9.46062 | -57.83524 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 856e58a1-a0a0-3041-b2be-3842dae8a10b | -8.37672 | -46.96786 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2466233-752f-3909-b761-b68f82b75eed | -9.46565 | -57.84197 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfb99080-592b-3f70-90b8-30c9609864b7 | -9.099 | -50.02828 | 2025-06-21 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7e552e3-ba79-3bf7-826b-fa37f4bf37d3 | -12.97727 | -54.68225 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0aafc66c-25f4-36e3-bacb-b5c968fbb497 | -11.94771 | -58.75718 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ede49fce-d376-39e7-a4ec-aaa4afbd78e3 | -9.40934 | -48.43238 | 2025-06-21 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 480cbea3-2a24-342b-981b-a2224d4750a3 | -8.02623 | -47.65726 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77b5f6e7-7d77-3478-83bf-b169b18464b2 | -9.09959 | -50.02466 | 2025-06-21 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 08da4505-dbd9-314d-945c-798e6142f54d | -9.09622 | -50.02412 | 2025-06-21 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53f1ae0f-c79b-3f63-b467-665bbcd83c01 | -11.57709 | -54.56683 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0adfb80c-57a7-3b68-a3b5-704afa35f783 | -9.46865 | -57.85057 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f18aa694-fa05-3b76-a7fc-07203f7f3fd4 | -12.29055 | -48.80325 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6149cddd-e941-3f7e-a483-14e6da4d7fe0 | -8.01135 | -47.66564 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| def64f29-6789-3749-a1ab-655d93f68f73 | -11.87525 | -54.68201 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62c8d505-d5c0-35b1-aa38-ac65d97c1712 | -8.01852 | -47.66319 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 71819fe7-53a1-3387-9249-8d3314e7cd53 | -13.24318 | -48.41816 | 2025-06-21 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8d1e829-1351-3d82-8cc1-5eae9341a770 | -11.14443 | -53.93778 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb343e2e-f2d5-3997-8c13-831e1d25e0fc | -10.47359 | -47.035 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c959337-6709-32c1-9270-6a4eca8e3663 | -12.51012 | -58.34754 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52a2c5c3-b757-3961-ae6b-f56857f5be82 | -11.52828 | -56.97783 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 41049ea5-6374-3608-8dfe-9463a0d0988c | -12.51256 | -58.35547 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afe3e21c-2c47-3646-9c14-6b8df017b3e6 | -10.52105 | -53.61943 | 2025-06-21 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90a4ef25-3fdf-3c04-99e1-3b4e1eb9c8a7 | -10.8859 | -56.46331 | 2025-06-21 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 74d59187-5ee6-31c1-9f25-8628634bf1d4 | -12.44165 | -48.14837 | 2025-06-21 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f106064-b76e-32be-ab64-35fbac013dc0 | -7.84769 | -50.22515 | 2025-06-21 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0a8eed2-c727-3e2d-8165-804fededba63 | -10.44413 | -47.04558 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce153370-986a-38ca-8f5e-0a08a08057ae | -14.49437 | -46.98664 | 2025-06-21 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 579fe0d9-2f20-3d78-94bc-bde7af8f4916 | -12.03002 | -57.09492 | 2025-06-21 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8505a74-e805-322d-9f15-df5e3f2d487e | -9.47426 | -57.82067 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af85baba-207a-31e7-81a8-bca6a336d253 | -9.47239 | -57.83062 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 99332a16-c49d-34c8-9fe2-ff14e99d5e04 | -11.57364 | -54.56237 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5001fa4a-e1f7-3b90-ba28-8bb887c3d3cf | -8.37954 | -46.97202 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c0ca649-5103-36ad-a771-7904f8dbf6e6 | -8.01906 | -47.65971 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9cb63c59-6f85-3bc0-9cbc-d618a5f6bd15 | -14.33106 | -45.42357 | 2025-06-21 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17211e52-58ad-3292-927a-1ac1e7ee8c47 | -9.47152 | -57.83965 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b809af9-0dc3-361c-a71e-74ca73bf90a4 | -10.03187 | -54.32493 | 2025-06-21 04:34:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fc74f68d-d448-3248-8c3f-c3e59f11e037 | -11.33333 | -45.22838 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5c94380-9114-38b2-a5a5-96f25f1b2e19 | -7.98117 | -46.21959 | 2025-06-21 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d1c1f7a-14fb-3e1b-ae38-0c9fa222e184 | -11.52925 | -56.97254 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f983fa8-95e0-3a5b-8d2d-7a2b8cca0fe0 | -8.00858 | -47.66164 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb8bf734-523d-3924-a606-0e528afae636 | -10.52077 | -47.57753 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a083296c-d028-30ad-b742-4e0dc8f74d32 | -10.4492 | -47.03495 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b19cd7b8-cca5-3c00-b94d-7e8ef38cc736 | -12.02901 | -57.10034 | 2025-06-21 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84da2eb2-5b79-3b5a-b309-60f54cf914e2 | -12.1329 | -54.66708 | 2025-06-21 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4b9cae4-de52-36b1-9bc9-3d63851ddab6 | -9.48911 | -56.08281 | 2025-06-21 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78c8ae45-2130-30e0-9768-b41313f9cb65 | -11.61888 | -58.29295 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bfa8941-d219-386f-8c06-d21b41ba720d | -8.01798 | -47.66668 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb9d2b70-bfbe-3549-b7bc-c9e372c10177 | -8.73802 | -47.98037 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e111b527-5a1f-31d5-9a30-3e1bd509c05d | -11.943 | -58.7528 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ade35ad-43c4-3622-aa83-4ffa02431d6a | -11.14004 | -53.91563 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81d2dd8c-bccb-3104-ba5e-644a555caa3d | -10.30408 | -57.13926 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4328bc3c-e5f8-3b6b-accb-68e0644f938b | -12.28717 | -50.1049 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c13e7976-e9db-3fbd-9273-bca0055decf2 | -8.19429 | -47.78036 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0f6dde8-b5e0-3958-8053-a3ebb38b2d3c | -10.14977 | -48.98623 | 2025-06-21 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8da4ea81-38c9-3930-93ac-9325d7310876 | -8.70573 | -50.04315 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cb00157-856f-3f5b-8a85-e4e581d64f24 | -11.77079 | -54.36827 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 145ec3c5-31a5-3315-8255-3ce17cbe9e8c | -14.81199 | -48.46946 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7549fe9-0ea9-38df-bdf4-cbb3878775ce | -11.91775 | -54.81914 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce66bbb3-6fdd-3b77-bc99-eea9e9575f1a | -9.47736 | -57.8375 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9efecec0-a03c-329e-9dbc-87b506439a07 | -9.46505 | -57.84532 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d028d9c7-1fe5-3e25-9582-288c44dde716 | -14.15435 | -45.4777 | 2025-06-21 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a95c11b8-6170-32e3-a506-1c25cb5a7b66 | -9.4187 | -48.43741 | 2025-06-21 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40dbd84a-d8fe-3537-bb7e-c1b3097d8377 | -10.52247 | -47.58884 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c03c41b1-00d5-3494-8334-8c13bf7b2988 | -9.09842 | -50.0319 | 2025-06-21 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b556c62-705e-33de-80c1-d1045826eaba | -11.13872 | -53.91755 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1d69707-8a2e-3d04-bb22-3a8acb338a49 | -8.0119 | -47.66216 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e3a0ece-8a6f-3cb9-9a71-b9375f191532 | -10.86343 | -53.76163 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c636df0c-8493-3e59-8647-67f19fe11501 | -10.47415 | -47.03125 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6dfb607-c640-3fcf-931f-d7052745991f | -10.24912 | -48.1728 | 2025-06-21 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 111ace0a-546a-3505-8eb5-ee9d1f5f39e7 | -9.46528 | -57.83948 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c273e08e-6b15-370f-aa33-f51cd5bfe69a | -7.99411 | -47.18037 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63bbc7eb-faf2-3fd8-a3c1-af4d0561a631 | -11.95169 | -58.76538 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3a74e4f3-74ac-3493-a96d-c622366bf2ba | -12.52317 | -57.20626 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b94c0673-506c-3647-8b58-aa7b34d62723 | -9.47556 | -57.84747 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README16.md)
