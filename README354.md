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

## Dados Diários - Página 354

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c35e0782-5a76-32a0-9c73-04024c2c6d35 | -2.94232 | -54.159 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 57b4e175-7435-3567-92b3-5c2c99537fc1 | -3.00342 | -54.76065 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 68e12bab-ffea-3a8e-b98e-4cced1a599fa | -0.73851 | -57.97174 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4fe838bb-d007-382c-a143-eef2e6554c6c | -3.8523 | -44.12314 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 20001025-feff-381f-90e1-0e42d86861ce | -5.41141 | -45.86749 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8a9a4e6d-d910-3651-bef7-6b0e3c4a6f63 | -1.53473 | -54.82822 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 4a05c5b6-a5b6-31f4-8a20-aad862d14ec4 | -4.3707 | -55.32285 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| adfe473c-1eda-32de-acef-8e9c6a139d9e | -1.85624 | -57.04918 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c160c5a3-44a6-3bf3-b70a-fd218877c10c | -3.00426 | -54.76618 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e4d29e74-c0ec-3a75-a7fc-01f892249a70 | -3.14744 | -58.55852 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 01447e6a-c810-35b6-99eb-dbae4efa9533 | -3.68888 | -43.05298 | 2026-10-08 16:39:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c63bc934-bd40-39fe-8298-ab734506cb89 | -5.29571 | -42.70528 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a921b0f0-cdb8-396b-988c-8196a9ed8d93 | -3.66721 | -57.08926 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d4abc2c7-2e88-3f2e-8634-04f909bddfbe | -3.51993 | -50.34621 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| d4d679e4-f628-3b15-81de-bfdb65eccf6d | -2.45888 | -47.5815 | 2026-10-08 16:39:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f0c04074-e5b0-3285-8d20-15674b46f701 | -6.74534 | -55.12205 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f8051b5b-7d57-3f93-9209-ac3d6b034336 | -0.38128 | -49.93954 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 68380931-01b8-37bb-949a-9a13c529209b | -1.54641 | -60.0318 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 9543616d-2986-356c-a375-4f1af5b5ad20 | -1.84908 | -56.18572 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e28b1347-5faf-3c53-abfd-21eb01a2279b | -3.73279 | -43.33354 | 2026-10-08 16:39:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 539c35ed-e100-3504-a25b-b787fc20e90c | -5.07941 | -46.22749 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22561726-1997-3d77-8c6b-f7c6d0f9ffad | -4.65253 | -44.85844 | 2026-10-08 16:39:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a37a19ed-ea05-3224-97d8-a862833ac005 | -6.73228 | -55.10654 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b46dea8d-322c-314f-b2e6-c3ce28db4666 | -2.56178 | -57.43492 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2b5fd172-9e79-34dc-b661-cc399b38c127 | -4.41299 | -55.43218 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 23fbd2e8-2da5-3342-aef9-5ab94639e23e | -3.17778 | -50.59017 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 217.8 |
| 4e3173a9-c04b-30d1-83c3-30e97618020e | -6.78237 | -56.23476 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| e57b0ddc-f8b0-3b1d-8cdf-169955ff464b | -2.57015 | -56.15216 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb2939a8-3139-36a9-8963-3abb0319fcf3 | -5.08218 | -43.05926 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d7f2a987-7c54-3d31-946b-07e427acfb1d | -6.74817 | -55.14293 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f6d0c678-674f-3c2d-8d0e-8f9b069a1c72 | -3.49336 | -57.98204 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d870a85b-96b6-3047-8c54-1753a907188b | -3.16673 | -52.12425 | 2026-10-08 16:39:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a7b9618c-13cd-3863-81f7-32a720adc121 | -3.31556 | -53.86471 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 049ef748-f493-3fc1-9fe0-4bd94940d0d2 | -2.06219 | -46.56059 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97c5fb2b-d424-30fc-b52a-0a85f6209df5 | -6.15902 | -47.94244 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 934c7025-d375-3fa9-8692-efa7007787db | -4.57648 | -55.99413 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 858634ad-252f-39b9-a9f0-79155c231446 | -3.14934 | -58.55725 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c8be763-d04f-343f-bf1a-0cc2ebafeb86 | -6.2262 | -52.883 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| 7a629532-43a5-3d62-a6e9-3e90f493bc71 | -5.39893 | -45.6534 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a06c933-1f54-3666-97d8-bd1d16fc0203 | -1.77418 | -55.06043 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 75860c82-b078-3c89-90c7-16b6fc79fa62 | -6.126 | -47.93219 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 60b3e01a-764a-3b35-b70e-fe905ccddac9 | -2.88298 | -54.87703 | 2026-10-08 16:39:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c6629b72-1233-3cb3-ba8d-488a06196e01 | -6.44593 | -55.0405 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b035d153-839d-3b7e-879e-c1ba6fb002cb | -3.79495 | -41.66371 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 37d1edd0-f8b3-3ae7-b45b-8a63209fbfe2 | -3.08407 | -53.96583 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b2baa4f6-26ec-38c2-8aaf-39f8590809af | -3.11575 | -57.59546 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b590f8d-7a2d-374b-aded-66d5e6d07b12 | -3.22632 | -54.29393 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f48d1919-fea8-3179-9092-3a49472f6c8a | -6.18759 | -52.87395 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4e12a9cd-6656-34fe-966d-d85c6f156742 | -6.16134 | -47.93452 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b89d8e9e-be85-3d33-964c-21d849dbcd39 | -3.30848 | -53.71697 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 457b2d68-65db-327b-b72b-08baef1b75a8 | -0.0994 | -49.49083 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 4bedf1eb-a3f2-3438-8697-f79a87f2e7ad | -3.00047 | -53.85344 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 42c7e6bf-c6e5-376a-886a-677b914e5e16 | -5.0929 | -46.2035 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 30e56b8e-a8b7-30ee-8e30-49d834134d4a | -6.0806 | -53.72078 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 84820ad5-2bab-395a-b2b3-c76e04fd652b | -2.80931 | -51.72661 | 2026-10-08 16:39:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 2e814344-d13b-316e-908d-49b19ddae6dc | -3.18036 | -57.85747 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72bd76c8-9434-39f6-a838-f3cbcd6dfca0 | -4.80787 | -54.67745 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c32243e2-f98b-3617-b163-17c84401d471 | -7.2289 | -55.08942 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 363b18fa-923f-3931-98e0-4373c7fbf5ef | -6.58134 | -53.01413 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3eff2b56-5290-3059-80df-1f77df47d1aa | -4.08889 | -44.11064 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 421f8d07-8df4-3077-96a3-f4c51cba9732 | -3.09275 | -53.95964 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3b2b9a21-0711-38c4-aee8-720558856074 | -5.97277 | -53.54833 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 227503b9-550f-3803-8554-5c1f523efa17 | -2.6623 | -59.40692 | 2026-10-08 16:39:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 513aa316-041f-33dc-be89-26d950b2e487 | -2.11461 | -46.39317 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d610222d-4dbb-3162-af9e-504fef938aa0 | -2.61414 | -56.48184 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 94cb8dce-1b36-3537-a189-a5eec2648693 | -5.54347 | -43.22918 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 26310e73-0b62-3062-80b5-ca3d236a9767 | -3.43562 | -45.25153 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a72cbe4-72fe-3fdf-9acf-3ad6775866d8 | -1.56268 | -48.22587 | 2026-10-08 16:39:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3074531b-28ab-34a2-963b-96469eb4ff83 | -3.48757 | -58.60544 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88211ee2-60e0-32b9-8f2d-c82755c6fae3 | -3.31268 | -53.86197 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4280c4cd-d923-311a-83cc-ef5619b6c93a | -6.21307 | -52.78993 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 75ba8b3e-e906-31c6-af0e-11512030a67f | -3.3155 | -54.04029 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 77db2f40-e086-34c5-b598-20f3f0a59f14 | -7.18574 | -52.62337 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b8c27ebb-7a22-370e-ac3a-d58e7d0811b8 | -6.25687 | -52.67603 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8b1e8953-1a08-30c6-8a37-07f0f2e4c2ee | -6.16859 | -51.51053 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fdee0ac6-7d11-3d6e-815e-f39f86c3689c | -1.43559 | -55.26164 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c7256bfb-6a1a-38b1-9cca-3b61b941b88d | -3.26592 | -42.95311 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3494de7e-54b8-39a8-b8ca-6f4f3e80a6c5 | -1.37988 | -56.88905 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c9ab800e-4da3-3e4d-9222-439035b9c4ed | -3.1696 | -50.45774 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 801aa9a0-c02a-3aec-881e-aad929acd16f | -1.6617 | -45.04349 | 2026-10-08 16:39:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecb8e703-4b30-3125-a68f-a6cb4a0493d0 | -5.73685 | -53.46635 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 63e48099-a859-37d1-8ccb-b7cb45df9803 | -3.94773 | -44.71581 | 2026-10-08 16:39:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 67523808-75cf-3012-a446-d33400146fc7 | -4.92186 | -43.0368 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 288428c6-a10a-399e-a632-fe40d142eb00 | -1.70867 | -55.85327 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c61595a-8161-3a1e-a76c-8d07f6a82519 | -2.09302 | -46.56298 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa1f1baf-d076-3c60-8c22-e99467296746 | -2.49526 | -56.1702 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 64ad8082-4aa1-3002-abe8-6e60ecbe1527 | -3.01277 | -43.34829 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 26fd7e1b-4eed-336f-b861-3e5438cf577f | -2.38685 | -45.99849 | 2026-10-08 16:39:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b51e6c72-5b00-3943-b8d3-76be646b9419 | -1.32439 | -55.44197 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| df005624-3db2-3bc0-9253-14a7c9addb70 | -6.03548 | -51.72176 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8d6024e-09bb-3395-bd3d-67ac81949fb1 | -6.78816 | -56.23386 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 8d7aa54c-c4e4-30fb-bfa7-ac1286df1693 | -3.46855 | -60.24527 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 9107435b-a9f6-3c8b-951e-2420cb67d3c9 | -2.99193 | -43.28589 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| df7cc0e0-75aa-3440-b225-9aa3b6bbf399 | -3.08879 | -53.9652 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7686cc56-1bfa-32e1-a6a2-1ebec479366c | -1.39247 | -56.07265 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aac73be4-fc4e-32eb-80ab-ad78d0f62c93 | -7.21716 | -55.16467 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2666dd29-335e-364e-8291-0f71daef091d | -7.60571 | -55.71185 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7f5fc9c1-4bd7-30d9-89be-3b91c5e2748b | -4.38663 | -43.9538 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f7cb81a-2de3-3639-8759-582b1d21ec47 | -3.30925 | -54.03092 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 04a6e833-a6b4-3c3e-bf2c-ad7a2542d694 | -1.77402 | -55.03287 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README355.md)
