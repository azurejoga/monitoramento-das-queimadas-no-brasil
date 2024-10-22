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
| ccd60c12-a00f-3d00-92cf-1bbaeba9187a | -6.1761 | -44.137501 | 2024-10-22 00:16:49 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89788da4-2939-35d9-a259-a868b6a98619 | -6.1777 | -44.144402 | 2024-10-22 00:16:49 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63fdb303-af09-3e54-b587-50f9e8a54900 | -6.1792 | -44.151199 | 2024-10-22 00:16:49 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2b24e2-4046-3419-8e92-7f6d4d119c3a | -6.018 | -44.626202 | 2024-10-22 00:16:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 358db971-9729-3b71-a80d-612dbdf91570 | -6.0196 | -44.633099 | 2024-10-22 00:16:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9535207-d2a8-329b-94e3-a853400dc107 | -6.0067 | -44.621601 | 2024-10-22 00:16:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6ec7841-0cd3-3eae-9f08-c77e58989b28 | -6.0082 | -44.628399 | 2024-10-22 00:16:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae445d11-b9c3-3d82-b2ca-713f352838ca | -6.0098 | -44.6353 | 2024-10-22 00:16:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1c2b6fc-153d-30ad-97cc-5a056e6c2531 | -5.798 | -43.7397 | 2024-10-22 00:16:54 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7131c7e0-4efa-37c3-9d51-7aec9a33ab6b | -5.7995 | -43.746601 | 2024-10-22 00:16:54 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9102ff28-f51e-3e7e-8cf7-f5c7640c7beb | -5.768 | -43.6525 | 2024-10-22 00:16:54 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7ab7594-f112-373f-b1f1-41b3e750a228 | -5.5596 | -42.7799 | 2024-10-22 00:16:54 | METOP-B | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 92faf43c-fa9b-3a1f-b1ab-7ef7d07ff01a | -5.6417 | -43.1409 | 2024-10-22 00:16:54 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| dd44c406-1581-37b0-9aaa-ae7e4500c092 | -5.6433 | -43.1479 | 2024-10-22 00:16:54 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 0ba5e27b-7c47-3964-8586-fcf8dcb9ac12 | -5.6449 | -43.1549 | 2024-10-22 00:16:54 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| ec641282-6eac-307d-a123-e0c3f8b0cb46 | -5.5315 | -42.928501 | 2024-10-22 00:16:55 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95e08746-d70d-3e0b-bf48-e167d1837b44 | -5.5332 | -42.9356 | 2024-10-22 00:16:55 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b5afed3-9979-3592-afd6-bee69f10961f | -5.5722 | -43.288799 | 2024-10-22 00:16:56 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94c348a9-0cd4-30a0-baab-39521f0a197c | -5.5737 | -43.295799 | 2024-10-22 00:16:56 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| add1c3ef-6a23-3a5d-baab-63490ddda848 | -5.7779 | -44.657902 | 2024-10-22 00:16:57 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38ccad0f-ffd8-3afc-b755-079e818cd61a | -5.7794 | -44.664799 | 2024-10-22 00:16:57 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3d5c628-a4c5-337f-9e6e-6e29ae28b799 | -5.8526 | -45.406502 | 2024-10-22 00:16:59 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 777dbf24-c3b2-3b4d-81f8-8b7bba1b0c49 | -5.8542 | -45.413601 | 2024-10-22 00:16:59 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d879a085-27ef-33c9-b98f-aa30b9e6e787 | -5.8558 | -45.420601 | 2024-10-22 00:16:59 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e35e4390-e4b4-3e85-972e-3f26340069e3 | -5.8573 | -45.4277 | 2024-10-22 00:16:59 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab163f13-8c72-31fc-a1c2-be2388347176 | -5.8459 | -45.422699 | 2024-10-22 00:16:59 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45e379a7-fe0b-32be-b850-c02b26568522 | -4.9989 | -41.9506 | 2024-10-22 00:17:00 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9a796a2e-de18-3e33-be62-d4e2c4e77885 | -5.0263 | -42.566101 | 2024-10-22 00:17:02 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57dbf2f3-9224-3474-bd2c-2832ee2b2be3 | -5.1665 | -43.181499 | 2024-10-22 00:17:02 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 270726fd-6425-3e28-949d-063f2d64fa86 | -5.1747 | -43.172199 | 2024-10-22 00:17:02 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f78ba438-7df6-309a-8d95-6402b67346a8 | -5.1763 | -43.179199 | 2024-10-22 00:17:02 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f862595-cd78-3d6e-92bf-17ab4ace6aba | -5.1779 | -43.186298 | 2024-10-22 00:17:02 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 336f5b95-9572-3945-97f8-694740226f60 | -5.1794 | -43.193298 | 2024-10-22 00:17:02 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77fb8d51-d324-3ed8-b585-fed79753e3b8 | -5.1681 | -43.188599 | 2024-10-22 00:17:02 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ca4b76a-e66e-3b04-a750-15012ca448f9 | -4.8698 | -41.971901 | 2024-10-22 00:17:02 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5972065-5864-3d87-b1cd-e5e48c99dd84 | -4.8582 | -41.9664 | 2024-10-22 00:17:02 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f517842e-767e-3215-9df1-ceaabf1ff49b | -4.86 | -41.974098 | 2024-10-22 00:17:02 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40a5d3a9-6f69-309f-a2ef-f2467768fe9d | -5.5371 | -44.870201 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0f40b55-ff04-37f2-bb20-dbfa33a31082 | -5.5387 | -44.877102 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c405ff10-b4ca-3b3b-9d3e-395d81aa2e91 | -5.5258 | -44.865501 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0327e386-354f-3d32-90af-fad69a6a4370 | -5.5273 | -44.872398 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66297e53-40cf-38a9-8dc9-3445c94e8b82 | -5.5289 | -44.879299 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e47eb7e5-dbfa-3bb3-b7ab-243eb7b94aa6 | -5.5304 | -44.8862 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d875925a-a358-31ac-a9ac-bb78f65e5a5c | -5.516 | -44.867599 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0b6908-683f-3cbb-846e-3b0f0ffe5ccc | -5.5175 | -44.8745 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 676d43ce-bc94-3809-a2cc-f93d63271e69 | -5.5191 | -44.881401 | 2024-10-22 00:17:02 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43b05d5f-6279-3dad-ac0b-170a90bde3ec | -5.2439 | -43.979 | 2024-10-22 00:17:03 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 331b63cc-42c7-38d9-8f68-f31548b76a9c | -5.0361 | -43.107101 | 2024-10-22 00:17:04 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6a3ceff-5e40-375c-a8f1-984859dd9520 | -5.0377 | -43.114201 | 2024-10-22 00:17:04 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e74f82ea-1638-35d0-b4d2-4bdd62b17100 | -4.7098 | -42.263901 | 2024-10-22 00:17:06 | METOP-B | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 27ab4486-7a5a-34c2-957a-89ee8dc592d6 | -4.7115 | -42.2714 | 2024-10-22 00:17:06 | METOP-B | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da02c096-d237-3a99-aa9c-1a8cc0f8ddb4 | -4.8812 | -43.015301 | 2024-10-22 00:17:06 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9b0367c-06a3-3ed6-98a3-d2115172927e | -4.8828 | -43.0224 | 2024-10-22 00:17:06 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fea457c-d726-3053-b3cc-3f66e1862815 | -4.8118 | -43.253799 | 2024-10-22 00:17:08 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efd108f4-8566-3b30-a32e-281743adab1d | -5.0681 | -44.341499 | 2024-10-22 00:17:08 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61504f75-2c70-3416-be8b-609fba08c0e0 | -5.0696 | -44.3484 | 2024-10-22 00:17:08 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f48467af-ba5a-31d0-8a49-1ecb8e0ad630 | -4.5603 | -42.376499 | 2024-10-22 00:17:09 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 355bf81f-9918-38b2-92d6-169b32550c07 | -4.562 | -42.383999 | 2024-10-22 00:17:09 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 41009402-05d1-37da-af64-e3f4a05d085e | -4.5637 | -42.391399 | 2024-10-22 00:17:09 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ad318ed-cbf4-39f2-a6d4-cefeeec83ff9 | -5.4193 | -46.373501 | 2024-10-22 00:17:09 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 106a3ba0-022d-31f9-bca6-6eefca9642f2 | -5.3833 | -46.350201 | 2024-10-22 00:17:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7390149d-25ca-3962-830a-351aa4c1dcfe | -5.3849 | -46.357601 | 2024-10-22 00:17:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3667252e-2e59-3367-8df5-c97a3bfdf588 | -5.3802 | -46.429001 | 2024-10-22 00:17:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4fa15d8-9a2b-31f3-88ad-3f29548a65d0 | -5.3818 | -46.436501 | 2024-10-22 00:17:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4b01eca-3b37-31d6-9857-9e0975f73e10 | -4.4769 | -43.277302 | 2024-10-22 00:17:13 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13d97017-730f-3249-b6a1-140fd591266b | -4.4091 | -42.888401 | 2024-10-22 00:17:13 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd782578-d002-35a4-85b5-5bc3a1644b61 | -4.4107 | -42.895599 | 2024-10-22 00:17:13 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f2d16d1-b751-3dab-b58c-ab2f340a98af | -4.4124 | -42.902802 | 2024-10-22 00:17:13 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffe4e958-0da5-39f0-ad8d-68a640237d18 | -4.414 | -42.91 | 2024-10-22 00:17:13 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 867195f8-de01-35f3-8d2b-48e75c1829be | -4.4009 | -42.8978 | 2024-10-22 00:17:13 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| abae817f-86fa-387b-a887-fb459c010ecf | -4.4026 | -42.904999 | 2024-10-22 00:17:13 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cbad518-3c92-33f0-8318-60fef0cb8069 | -4.4042 | -42.912201 | 2024-10-22 00:17:13 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 120a5441-ac41-3ffc-9e8f-f839ca68177e | -4.4914 | -43.568001 | 2024-10-22 00:17:14 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 450c0a18-39c6-3e18-a138-47bcf2dcb056 | -4.493 | -43.574902 | 2024-10-22 00:17:14 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7b01c63-5efd-3066-8758-0e59fd6cc5d7 | -5.0892 | -46.091499 | 2024-10-22 00:17:14 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76ea50c7-8886-3aa3-a7a7-6b4da9fc8e86 | -4.8979 | -45.418701 | 2024-10-22 00:17:14 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90810537-f0f4-3944-ba8e-1534cd7ed06a | -4.8994 | -45.425701 | 2024-10-22 00:17:14 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04dc4812-fb2e-373e-a4f2-1d97b9a0c127 | -4.8881 | -45.420898 | 2024-10-22 00:17:14 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d9b2e48-bd8e-39d1-8b15-74f9baea1019 | -4.8896 | -45.427898 | 2024-10-22 00:17:14 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a4e86f3-f4d6-3339-a878-35fa642bb29a | -4.8912 | -45.434799 | 2024-10-22 00:17:14 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f133096b-516e-333b-91fa-688fdfa1f606 | -4.3241 | -43.013199 | 2024-10-22 00:17:15 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8c35aaa-96c5-334c-96bf-cb33812c6b57 | -4.3258 | -43.020302 | 2024-10-22 00:17:15 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1dea5ba9-6c80-387e-8ec1-0693d3c4fa6a | -4.3127 | -43.008202 | 2024-10-22 00:17:15 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb69d532-5f2f-3b71-9828-04d1793173ab | -4.3143 | -43.0154 | 2024-10-22 00:17:15 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37db517c-f045-387c-94fc-b3de42e16ec0 | -4.3379 | -43.5732 | 2024-10-22 00:17:17 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08df1d8a-275b-3ef6-ad5b-00bfbd79a18c | -4.3395 | -43.580101 | 2024-10-22 00:17:17 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10e6baf8-e1f9-39de-bb2a-0dd0404ca203 | -4.3522 | -43.9548 | 2024-10-22 00:17:18 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d9b9cb0-736d-378c-9ad7-fb082d20fe60 | -4.3537 | -43.961601 | 2024-10-22 00:17:18 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df26993b-3117-379b-b416-0070c49fb71b | -4.3553 | -43.968498 | 2024-10-22 00:17:18 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ebb1d98-7ca6-332c-a504-350a39b53b07 | -4.1215 | -42.983299 | 2024-10-22 00:17:18 | METOP-B | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a688826a-8660-3856-b8c0-037df25bccdd | -4.1231 | -42.990501 | 2024-10-22 00:17:18 | METOP-B | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb3b8ba1-96cf-39dd-909d-b91f5cfe3a0b | -4.248 | -43.585899 | 2024-10-22 00:17:18 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45e42543-91c5-39c8-bab1-768cf9a54edc | -4.2496 | -43.592899 | 2024-10-22 00:17:18 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd7b8ec9-8603-3b3e-a653-89641b70db5b | -4.1359 | -43.182899 | 2024-10-22 00:17:18 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa3647fd-9587-3a9f-85a1-44d89283791e | -4.1375 | -43.189999 | 2024-10-22 00:17:18 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69fb98a5-b035-3930-9258-62d20f400191 | -4.4434 | -44.3587 | 2024-10-22 00:17:18 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 025e6965-7e9a-3492-85fa-28a172047f86 | -4.1356 | -43.272301 | 2024-10-22 00:17:19 | METOP-B | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81108432-d012-31b6-baa2-9c882443ae7d | -4.0684 | -43.339298 | 2024-10-22 00:17:20 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4172a546-b004-34e7-af2f-28f60dd98bcc | -4.07 | -43.346298 | 2024-10-22 00:17:20 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 959a634f-d647-362e-961b-a4ea2630e71b | -4.5063 | -45.141899 | 2024-10-22 00:17:20 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
