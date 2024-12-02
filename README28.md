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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 894f1f1f-07f2-3854-bc2f-30a3de8ecf70 | -2.80466 | -48.59142 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12748c49-c87e-3db9-9000-f89a450d1f69 | -1.22806 | -53.36327 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f5f8800-e840-3d8b-9c29-e4d8394e4acf | -1.95249 | -53.34321 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4a75ccc-546f-3e5e-897b-bfaf3c0b39b6 | -3.13816 | -45.98521 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc19cfbd-b64e-35b2-8a75-1636ff77f700 | -0.60523 | -51.69146 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0796762-13c5-3e9c-b496-b064c3cda11f | -1.03714 | -46.95832 | 2024-12-02 04:23:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c62dc0f8-836d-3e6a-82c4-b598a7adb0c8 | -2.71581 | -46.19702 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2fca8f-f174-3308-95c3-5b2050bd0fb4 | -2.72978 | -46.2386 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bfad1eb-a9d5-371f-a7a6-4aea04e7c522 | -2.61337 | -46.26705 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 423924bc-8819-351e-84b1-74da56e469c2 | -3.27542 | -46.44935 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| cf7937f2-af49-337c-9bea-f86bb25ebcdc | -2.5842 | -48.20147 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f8209ea-642d-30de-937b-083beaf3ae7c | -2.80328 | -45.3844 | 2024-12-02 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43ec45d9-aa72-3f58-884c-e2932d99c5da | 1.13295 | -55.98669 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86f71490-0973-37b4-a234-09f0cdb0c84e | -1.45122 | -54.51884 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ac04367-4ee9-3929-99d8-bcea664fe146 | -2.67636 | -46.62034 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c59dfaba-473b-34e0-add6-8f535d38e43c | -2.45778 | -46.52409 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f61543d-ed55-3fe5-9ca9-34fd1386c1a2 | -3.21744 | -45.76373 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a45badd4-fbe8-3727-aa3d-7d564d5cbc0f | 1.12994 | -55.98605 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62987f3e-13b3-3d03-ae5f-712e50ebef62 | -2.77335 | -48.57788 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c2e1e0b-ccee-3e2b-ae0a-89a19a10d261 | -2.7524 | -46.11694 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cfe7c50-fe90-3a59-9118-10f3aff65c0a | -3.30544 | -46.40366 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1cdb3e7-2f12-3857-b61d-1b7062a3b162 | -2.58955 | -46.57047 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca5b07c3-8004-3a85-ba25-384d91df41eb | 1.14094 | -55.97425 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8cd2b46-336c-3522-8a86-82fbaf95506c | -2.59084 | -45.99905 | 2024-12-02 04:23:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b73ac0d-664e-34d8-9368-bf09e051ce70 | -2.84584 | -48.10195 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57f3a24b-0201-39de-aa10-90225313fb1f | -3.13574 | -48.52478 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac537cc3-7e0a-319d-bd0f-b11b565a500f | -2.6599 | -46.12393 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa8f981-ba74-344f-8622-97eb01c82bcc | -1.67664 | -52.10062 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f895339d-2da3-3a76-9d04-362f76a7c09d | -2.70467 | -46.18094 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32281b4c-f086-3b58-b1e6-c40c51ef8111 | -1.39052 | -53.55479 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6bc5cf7-ed6c-3d01-8324-336da4b1cb5b | -2.56126 | -48.55096 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 638660e6-d857-3900-9ebd-1d0cb68739ab | -3.13761 | -45.98867 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3be9eeef-bdea-39a5-83dd-48821c8734bb | -3.14038 | -45.99265 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d4042213-684a-3676-99ee-d2a70887d9c0 | -2.24012 | -47.05893 | 2024-12-02 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5df31b5-7324-3fa9-81b7-8fd1ee3591da | -2.5918 | -46.57809 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8eef5020-588e-3add-8591-8675f1f199d3 | -2.45531 | -46.09158 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7446d639-25fe-3d7e-b776-af0c27092e5e | -2.92152 | -48.01289 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 669d1df9-a88d-35e9-ba7e-d8eea523f2da | -1.27627 | -54.55595 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67e15a60-eb80-38f6-afe9-ec68b89bed3c | -3.12488 | -45.98618 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb50132d-948f-3bbb-816b-7b9f7d245106 | -1.43729 | -55.43131 | 2024-12-02 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20d5dd9b-6ecd-3775-826a-d87375f384c0 | -1.99412 | -46.45546 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cd0c621-01f8-3602-8288-fb30af0db4ac | -3.19564 | -46.5848 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57eeb0d4-374d-3835-bd31-3d69bce00613 | -2.34651 | -46.94054 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26efc54f-87f9-35d7-84c4-6b77497abc32 | -2.66762 | -46.0966 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ff85cde-54ff-30e6-86a9-17a357ef4018 | -3.02754 | -47.79789 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0be2e9e-e6cf-3b86-a685-7de6bc03107d | 1.10475 | -56.01094 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36146731-0423-3bca-b08e-586e1eaf2b31 | -2.27208 | -53.60654 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5829c1-bb18-334e-94c8-ab7ca139b755 | -2.65546 | -46.13039 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7fa6305-0f66-33a2-ab5f-065ece32ab9f | 1.12123 | -55.99355 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08ce2385-3b7e-3496-b1f6-477b997f5a3a | -2.26749 | -53.60282 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20829faf-02ab-3938-bb36-30911703b82f | -2.0217 | -54.3118 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e896cfb-0cf6-31ee-ae94-3da32f8289da | -2.47516 | -46.56684 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 729c8c47-d829-3673-8512-61836e1aa59c | -2.23752 | -46.39564 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4623f979-ebe6-374f-9725-4a524cd1fab9 | -0.57861 | -51.68235 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 884f147b-f16b-3f46-b0ea-503059fd1a2b | -2.7513 | -46.12391 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 879a739d-b74f-390c-90c9-76c950bd7c5b | -2.75295 | -46.11345 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e97a9789-d397-32e3-81e2-fcdd61ed9dbc | -2.4746 | -46.5704 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3780278c-872d-3bd2-ae71-6829a1dafb0b | -1.4014 | -53.64945 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 437077ab-ea3c-3807-a54e-3860b39b38ae | -2.7711 | -46.02009 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ec0c43-77a8-301c-bfdf-f76c37d279f6 | -2.19648 | -53.77776 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc503b78-b635-3c6b-a3bf-7cede5f93aa2 | -2.47404 | -46.57395 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 178d322e-5f82-38f7-869d-697296a7e09f | -3.26204 | -46.44722 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62f63667-40b4-3adb-b6f7-180bd60f11a3 | -1.07302 | -53.44879 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 578b1b32-03f5-3ea6-8e48-98108f09af1e | -2.65336 | -46.61309 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 023fa632-3362-3eeb-b8b7-e7e15588e1b4 | -2.21485 | -48.38197 | 2024-12-02 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7504bfa5-6ed0-38a3-87d6-8fd0e2b4ba32 | -2.16789 | -50.12476 | 2024-12-02 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b3ca145-fd4e-3c1b-ac46-b585996f3466 | -2.75828 | -47.90324 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c759988-d7be-31d3-8a1d-e6ef62e64a4e | -0.92438 | -47.61743 | 2024-12-02 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c0401e4-0e08-33a4-81b2-f0327466e129 | -3.26818 | -46.45179 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e75665b1-dc95-3a2b-af64-d32d3ba94d01 | -1.38539 | -53.55402 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b5551bd-a348-3ec6-b48c-975136f8ef72 | -2.77904 | -49.21572 | 2024-12-02 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 12e560aa-125e-319b-b36c-937f57b37477 | -3.26873 | -46.44828 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc4ee36a-5388-3771-b627-c752717fbf1f | 1.11025 | -56.00517 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a199ff-c9a2-372c-9296-b2a982c0dacd | -1.62395 | -53.89592 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c02df772-bfe6-3c8c-bfc3-780ae443fa19 | 1.104 | -56.00616 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4df700e7-4d66-3be1-a446-68feacf7ef36 | -1.73257 | -52.6375 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 671dbcd1-0e8b-32f7-b8bc-bb80b0833d26 | -3.13483 | -45.98469 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51bd4696-8266-358b-8fe4-1d4a5667e6d2 | -3.12101 | -45.98913 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e64b0def-9072-30ba-8dde-05aef591eba6 | -2.46282 | -46.57948 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 133b8139-0489-3a96-b6ed-b10d9076fee5 | -1.72779 | -52.63671 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2bc1705-454c-3915-92d7-3ea8f36a864a | -1.43797 | -55.42715 | 2024-12-02 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86b59c1a-515b-34b0-bfe5-eee47a15aedc | -1.99076 | -46.45493 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82d3fb55-09dc-3b04-8e97-403411ee4c3a | -2.65935 | -46.12741 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f048992-7c43-33c4-87cb-228bdf95d005 | -2.28316 | -45.74465 | 2024-12-02 04:23:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19b55d33-daa1-342f-8341-29924fa49a96 | -2.2606 | -51.25696 | 2024-12-02 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7561d42-3984-3c86-896d-7783e49786bb | 1.21011 | -56.00794 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c06e0806-ea24-335a-b6b2-7de02ddc3a55 | -1.25438 | -54.55196 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69acc611-c17d-3a16-92c7-814fcf22ad30 | -2.55311 | -46.56108 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 113d3361-3e36-3e01-a944-f28ad8e795c5 | 1.14935 | -55.96912 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c71442f-3cc0-3e37-8a62-fd3681ae5b11 | -2.66817 | -46.09312 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec0a4452-3062-32e3-b4dc-62668d6e68fa | 1.14311 | -55.97012 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45558942-f304-3b3d-acc9-38388574f376 | -1.34726 | -51.38255 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97decd30-cf19-344c-8498-89ced515cc3f | -3.27208 | -46.44881 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 378b5005-399e-3f86-979c-916a5bc57092 | -2.0186 | -54.31116 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b47389f7-378b-34b4-b515-4f0e8659d8e6 | -0.58317 | -51.68309 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 280a1553-fdd5-3ba5-98c5-acf623db4920 | -2.16018 | -49.75581 | 2024-12-02 04:23:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ba5d591-3acb-3962-8272-1220164337d9 | -2.56768 | -46.40395 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bdf0a71-94bf-3c92-940d-73d554ef0179 | -2.55591 | -46.56516 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83e60be7-df56-3cd2-bf34-f4205c128fe9 | -2.97449 | -46.94117 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a286950f-e5bf-3156-a3ca-6b78543ff5f5 | -3.1221 | -45.9822 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README29.md)
