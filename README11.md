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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfaa145f-6e24-3a1f-b5d1-cb29a01476db | -10.58758 | -55.42108 | 2026-06-30 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 979b9d81-ec70-370d-a22c-eb3e07c8c170 | -9.32434 | -58.01778 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e47e5b08-48e9-31ce-84bb-c74748f7887d | -8.98924 | -45.72267 | 2026-06-30 04:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 113a26fa-7c87-312e-b70e-c522096b5f04 | -11.77583 | -46.41257 | 2026-06-30 04:55:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef75041e-2c72-3861-8e2a-595e5bff79cd | -9.90923 | -46.29473 | 2026-06-30 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f9426bd-49ae-3d9d-9a77-0f6ee2694b36 | -9.12761 | -58.26313 | 2026-06-30 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee90b99-7ecf-3d60-832b-fe9539da9505 | -9.32576 | -58.03514 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ddcd368-b167-3df9-ae7a-09f8aed98f11 | -11.4718 | -47.41868 | 2026-06-30 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6377eeac-eef0-36d3-82e8-15e50ccae91e | -8.98489 | -45.72203 | 2026-06-30 04:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 676693bf-6e95-3ba5-9d5d-a1c0a378b15a | -10.14122 | -52.40338 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cdab904-8317-303d-870d-803bf3286e64 | -11.782 | -47.57015 | 2026-06-30 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afa70c4a-bc16-31c7-90e9-97f7525db2b9 | -8.73991 | -48.92958 | 2026-06-30 04:55:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3096c834-3b04-3415-bac2-cd7de52c6d18 | -6.50122 | -42.2339 | 2026-06-30 04:55:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c5c6644d-1349-3b94-8195-f82f011f4213 | -10.28931 | -50.17782 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 76a9dc5c-eead-343a-bdab-c86792755540 | -11.91312 | -43.39722 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67b5a14d-111f-396a-bf90-e98a538a7bdf | -7.43084 | -49.87691 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ce24ea49-b626-3694-82f9-3c6f20e6ee21 | -11.92219 | -43.39797 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28a50687-ebb4-3c3b-8507-9051d625c411 | -7.43425 | -49.87737 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca81ef32-1cba-3ab8-a1e0-bb3ea5f564cb | -10.93751 | -43.0382 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9a283661-bb0d-3b1b-9894-bd07ee0035b8 | -9.59288 | -56.92575 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dacabfb1-d154-3529-8fca-d55784fdea93 | -9.6015 | -56.92368 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be3be805-a658-35b3-9d93-6c2483e4d5d5 | -9.31784 | -58.02942 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec9e67bb-c726-390c-ac07-c35c2aef9698 | -10.12679 | -52.40824 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc53a61c-5e15-3d47-9efa-4f6c25bb0c01 | -9.74555 | -49.02782 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d959587-7d39-3a08-b144-420158309c23 | -11.9242 | -43.3952 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1a1e823-e9d6-3fcc-93c2-3167ae12f51c | -10.2962 | -50.17889 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05dc9149-5dfd-3348-b952-64c46d33f973 | -10.69593 | -49.61061 | 2026-06-30 04:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46085c63-783b-3ec6-884c-1a0d7ac9b809 | -9.44812 | -50.83809 | 2026-06-30 04:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0330cfb-ca21-3e6c-9f9e-5d92618bb4ef | -10.59048 | -55.42593 | 2026-06-30 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e68df6c-24a0-387e-8dd3-2192dee2bd01 | -10.58686 | -55.42529 | 2026-06-30 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55ca9e46-c80e-3657-aa9c-001382f34e17 | -8.29834 | -46.98868 | 2026-06-30 04:55:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92a140ff-dcdc-3f43-bb2b-257402e0c81a | -9.74789 | -49.0298 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f258ec4-ab25-3383-a9bb-347460697c34 | -10.3821 | -49.59034 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62a47f87-4179-302d-be29-b41dd325fc8e | -9.59627 | -56.93002 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d8e0153-4538-38e7-ab03-d0772956cf77 | -6.50615 | -42.23747 | 2026-06-30 04:55:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 45935110-608e-3940-bc54-0e8f2240be47 | -11.78004 | -47.57377 | 2026-06-30 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1cc74c4-6f98-3153-af59-a7704bbca954 | -7.43139 | -49.87333 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a94fee10-ae5d-3cc1-a4f5-335aa52d6a61 | -8.98806 | -45.731 | 2026-06-30 04:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eda3d763-6975-3503-ad4d-2dd0bac2eb4f | -10.93256 | -43.03409 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4ef7b2f-bc38-306e-ae5b-6634e4231e96 | -11.47631 | -47.41587 | 2026-06-30 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99fc4fe5-ff5f-3d55-bbe1-a77755b2149c | -10.52988 | -48.16077 | 2026-06-30 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7583c6b-a591-3832-b210-1c74d3eeca25 | -9.21135 | -45.33093 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cccca9b-796a-3080-9c47-541029068419 | -9.08626 | -59.39254 | 2026-06-30 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cdfe239-d375-328e-b5c1-08f96130d0d8 | -9.74854 | -49.0325 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d708d8d1-ae61-3369-9072-5d0d177f8f45 | -8.71022 | -50.71277 | 2026-06-30 04:55:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b7db15e-e7e4-3dda-87b4-f65c6a50196d | -14.95742 | -52.85859 | 2026-06-30 04:57:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3682968f-0adf-3a73-a467-e0f1e5a3ca10 | -12.21425 | -56.55963 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ed683fd-c69e-30f2-8eca-eb59cb190a0c | -11.31472 | -54.47154 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9f64e01-18d4-357d-900d-3fe59effba1e | -11.63449 | -59.01254 | 2026-06-30 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f3deda8-4cda-3b6d-a2d7-3e31c8cf437b | -17.70702 | -46.77734 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff012eda-0023-3007-8773-b1af62f1f1b8 | -11.2121 | -53.82138 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3d89bc0-0ad8-3cf1-bbc8-33fdf18fe7cd | -18.24429 | -53.84683 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed41e30e-6ead-3deb-8c42-28ce8d2b642f | -15.07232 | -55.80811 | 2026-06-30 04:57:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46bff9a3-29e8-34b6-8f3a-83992bab4c5b | -13.26739 | -56.80336 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f62886-c84c-3b4c-b64b-35e50a84626b | -12.84764 | -44.39552 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fd520e6-e424-3531-8f13-53f6c224de2e | -10.90938 | -56.85301 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6052f40-0170-3963-a0a7-049d15e65627 | -13.25249 | -56.8033 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44884494-9423-3912-b798-d3cf60d14ab3 | -12.50973 | -48.26465 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9f0c03f-a588-3a25-b031-d0ace630397a | -17.70644 | -46.78217 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3148c898-b51c-3b0c-875f-db70586e2687 | -13.26364 | -56.80263 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74c6f0ca-d464-35a4-9d76-43ace7ad6970 | -12.21883 | -56.55568 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7190e232-638d-3323-96de-e65b1e409fbb | -12.44599 | -58.49558 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 483dfb5d-d043-33eb-b249-77fc28a6e2e2 | -13.71043 | -47.87117 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ddc56c6-ed45-336a-8f6a-d0a5e9bbedb5 | -11.96006 | -58.61408 | 2026-06-30 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 849e1d0f-d5f1-3771-9c4e-e28b3982a097 | -12.45593 | -58.48904 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08af6639-f1bf-3bd5-9682-4826027ce72e | -12.54244 | -57.19807 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e4a89ba-e3ab-3174-ba45-8dc4885182da | -13.25863 | -56.79013 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa9d3163-09a2-3cc0-bddf-ee4bd9f75f2f | -12.21823 | -56.56292 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cbb6faba-2077-38a6-9b2e-f4142a1a542a | -11.90067 | -57.12603 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 449e3902-9b3f-364d-a98e-dc348831ab4c | -10.90851 | -56.85798 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb7a797c-43cd-3d19-8f87-987f99e83a54 | -13.25705 | -56.79935 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1f9a3049-9386-3b48-b78b-9b599b60d2ac | -11.22298 | -54.30849 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2480991-8ff7-375a-8c03-036bd8cd527c | -14.0477 | -46.3338 | 2026-06-30 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de12de5a-8dd9-33dc-9434-49fc4126b31d | -11.31881 | -54.46832 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed3000af-21c5-30e9-9e2b-d23e4bf61688 | -11.88549 | -57.12594 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f85cdc69-bfe6-39cd-bc54-95a80671093c | -17.44188 | -47.16592 | 2026-06-30 04:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 122745b5-d811-3864-97c9-bc9cec8684a8 | -13.94722 | -53.95504 | 2026-06-30 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e2409ac-eac9-3ea4-aa78-b6c7dfa931e1 | -13.26161 | -56.79542 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1b12c9e-3b14-3510-8c20-989fdb3762a3 | -11.90593 | -57.41811 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 994a7be8-b323-3c10-8f5c-b0e71a267b32 | -18.24543 | -53.83956 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0b70e88-55a9-391e-aa91-fd4aeb7f6891 | -13.26082 | -56.80005 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 62ee3edc-9b5d-3884-9e8f-8f3352e8e052 | -12.54222 | -57.20153 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bdd67f6-7b8e-3e28-834f-8d45f6d26a10 | -11.91943 | -57.388 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dc0de5e-1e19-3a6b-9e07-1b27d0a4b5a2 | -13.70597 | -47.87364 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4907c8c0-c40f-369f-a8fa-c0c4d804ccfa | -16.19656 | -59.3237 | 2026-06-30 04:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6010bad-a1fc-3efb-83d2-fbea2548b305 | -13.71945 | -47.86539 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 900f5ef2-4be6-3fd6-b58d-1c47bf035c84 | -11.31599 | -54.46391 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45f5c147-ccf6-358c-9edb-2312f896a0d7 | -13.23902 | -51.56619 | 2026-06-30 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abc866e5-0bd4-302b-b1f8-9fb019a6bca4 | -17.43742 | -47.16536 | 2026-06-30 04:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa3413b4-4b80-3ded-a194-a4986022cf98 | -12.20236 | -52.86592 | 2026-06-30 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b524643f-5898-37ae-b4f2-20dba452f30e | -11.2286 | -54.31722 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fa48b8e-2073-398f-9bfb-432194897c53 | -11.22641 | -54.30908 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6378bbeb-2f9e-3309-9858-dec4a8fe4a34 | -11.73699 | -59.35591 | 2026-06-30 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43b4a032-63b5-327c-b67b-d454e6023ff4 | -15.40334 | -59.5014 | 2026-06-30 04:57:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c4ab6d0-214a-3869-a364-85d691d2741e | -11.31536 | -54.46773 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dff5969b-eaad-302b-b790-cb93bd35abba | -13.23677 | -51.55834 | 2026-06-30 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 934197e0-2ca8-3b0e-9ab7-7322ce346e7f | -11.05208 | -55.7627 | 2026-06-30 04:57:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d482002-4584-3dde-b0d2-a0ebf9cdb444 | -11.93731 | -57.71295 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 492371a0-e073-302a-a5d0-a5b631d8368c | -17.71557 | -46.78372 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57cf66e9-6aab-377c-9d85-51f0b2c5d7c0 | -15.0845 | -59.90431 | 2026-06-30 04:57:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
