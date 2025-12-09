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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe39b654-e525-3fdf-8462-379cb70f438b | -1.10489 | -52.24178 | 2025-12-09 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8edfcd7f-1b34-33da-b671-e9e9e3947b83 | -1.98326 | -46.62399 | 2025-12-09 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fe0d5f0-868b-3afe-8ab1-5ca7e97c319e | -4.1848 | -43.8283 | 2025-12-09 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 748b8fd6-75d4-3811-8e70-e90f0543995b | -4.15614 | -38.13655 | 2025-12-09 04:25:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 54b7becc-0503-3373-90b3-493af26f18ff | -5.36632 | -36.84116 | 2025-12-09 04:25:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 709991e7-afc2-3a5c-b258-39e137b75afc | -5.00414 | -41.2981 | 2025-12-09 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d67f17c-a0ae-3109-8d0b-34c2e0971bf6 | -4.40127 | -44.08403 | 2025-12-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21b6d6a2-0e22-3174-8802-c1cf7c4a82be | -4.74743 | -45.20404 | 2025-12-09 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f194d58c-a190-39b4-bce5-dc6742841670 | -3.42455 | -41.66142 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dd273725-4c7d-33cf-8ea8-e602ff04485c | -3.43725 | -41.65401 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| fa71e39b-8ac3-343c-af58-5a82857fdbcf | -1.67268 | -45.79053 | 2025-12-09 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5421b035-9c04-3946-9300-75c9faff8bf3 | -3.63325 | -43.35738 | 2025-12-09 04:25:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2389a53-a672-3f36-b660-83b73f6a3953 | -5.675 | -39.60023 | 2025-12-09 04:25:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9a6c8f74-1246-3f0c-acd3-0cb100cdd8f6 | -4.82357 | -42.98518 | 2025-12-09 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b7d84d2-440f-3785-903a-bd2d272f481a | -2.05424 | -46.50069 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a822b02b-8d0f-3f56-aa7c-1697da2f812d | -1.06844 | -47.12202 | 2025-12-09 04:25:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21e2171-65f2-344e-9288-050bacbbea76 | -3.2146 | -46.06524 | 2025-12-09 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b181187-a36c-3eff-8a7d-14d216b70b6a | -3.95821 | -41.51839 | 2025-12-09 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 7c1ff6ed-706a-3622-8738-3da1a897371a | -4.48249 | -42.99543 | 2025-12-09 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e30f995-4413-3969-9f1d-3207dc8747dd | -3.0985 | -45.20108 | 2025-12-09 04:25:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 564579bf-3c11-38df-948e-b16c2fc487cb | -4.40854 | -44.31513 | 2025-12-09 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f544bf0d-26d0-3e70-9899-4716521f062d | -5.08633 | -37.54748 | 2025-12-09 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| cb216644-72f5-3ea0-ab71-f222b7b8955b | -2.09615 | -45.80029 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0d22e404-b256-3fbc-9dc8-9bf3fc899e46 | -3.43279 | -41.658 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| fe6d2f9b-3975-32ec-8e07-baaae14317ad | -3.16403 | -44.19129 | 2025-12-09 04:25:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c968dcd4-c34c-3d3d-bb4d-368ac9be2c4b | -2.09669 | -45.79684 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ee6eb9ea-9e63-386f-acc4-fbe8693c52a6 | -2.50886 | -46.78575 | 2025-12-09 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d2ccc00-502c-3745-a3e3-9a034415622c | -2.03169 | -45.8221 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df77007f-dc0d-398e-9543-aa7330c9d491 | -3.63613 | -43.3617 | 2025-12-09 04:25:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fe7e9f0-8a89-3dcd-9de6-8279d812955c | -1.96147 | -46.4424 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fc9092e-f40f-3b0e-ac5a-5d4f5f195da5 | -1.5998 | -48.39085 | 2025-12-09 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7480a58-56de-3d68-a7a2-d00d04890722 | -0.80302 | -47.86207 | 2025-12-09 04:25:00 | NOAA-21 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 019e59f7-126a-3c5a-b796-088f56db4eca | -4.21728 | -43.25755 | 2025-12-09 04:25:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c2a43f-16e6-3ffc-945d-084a83d4b653 | -5.72492 | -42.04716 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 129d0b09-f6a0-3f0d-8a5a-8bee8611448d | -6.60189 | -39.53765 | 2025-12-09 04:25:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27990969-2c36-3969-904a-0cec17f9ea92 | -4.32415 | -43.15226 | 2025-12-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e9ae9ae-99f1-3d37-924c-3d0f7ee7ed39 | -4.72263 | -42.0416 | 2025-12-09 04:25:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d6f845db-0094-34e4-b78c-7482b01ce250 | -4.0524 | -45.64704 | 2025-12-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f90b4291-a1a0-3d92-977f-5bed2347c238 | -2.06177 | -46.25742 | 2025-12-09 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9ba1cef-aadc-313d-bd10-7d70bb952561 | -1.01675 | -48.16259 | 2025-12-09 04:25:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fd3867e-dc61-312d-901f-7ce54f6c01aa | -4.18537 | -43.82459 | 2025-12-09 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47ae181c-fb58-3229-96c2-d28fb7ab9d0a | -5.04467 | -43.59985 | 2025-12-09 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5af92cf3-fbcc-38d4-bc1b-f254024e2f88 | -3.95671 | -41.51987 | 2025-12-09 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c518c50b-f2c2-3a13-a873-73dbf5f8d8ae | -3.4182 | -42.89643 | 2025-12-09 04:25:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07136216-0001-325f-9f6c-11f5262d2789 | -5.52732 | -39.84746 | 2025-12-09 04:25:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f9c32c1-918d-301a-a4a1-16f16dd1d58d | -2.06149 | -46.49819 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88e5595a-340c-341a-ae73-c50fde06133d | -3.42832 | -41.662 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 29ca06ec-0e04-3da2-8127-3d8af0311759 | -2.77604 | -54.52652 | 2025-12-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62f6f60f-e448-3cae-b198-67ec93fbc6d5 | -2.035 | -45.82261 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d78d150f-3b53-34b4-af7a-a78fffa7c7ea | -5.00266 | -41.30805 | 2025-12-09 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf085fcc-7404-38a5-95dc-e25e9314062d | -5.08947 | -37.54804 | 2025-12-09 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8296e8bb-d4fc-3735-a6fd-cba90fe7eaad | -19.84886 | -42.02663 | 2025-12-09 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 36e11176-6729-3c3e-86d3-f3ae2a8409c5 | -18.89021 | -41.94779 | 2025-12-09 04:29:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 17af6f0f-9ef5-3b73-9d3d-ab03e1ac5e20 | -1.53599 | -49.44478 | 2025-12-09 04:53:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd0c5f82-0257-39e9-bd32-28e72485ae45 | 1.6898 | -50.62389 | 2025-12-09 04:53:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 032f9b9b-31eb-3f6b-bd8f-d618af79f851 | -0.30229 | -51.68412 | 2025-12-09 04:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0014faac-dbec-3eaa-a910-881eaff6e79b | -2.05433 | -46.50325 | 2025-12-09 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67705e0d-a9fc-386e-ba8f-8143b1af04a4 | -2.57122 | -46.02042 | 2025-12-09 04:53:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c38982a0-9d6b-35fc-8b30-08a48d2ec614 | -1.10196 | -52.23572 | 2025-12-09 04:53:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd3a32f8-0cba-3995-b8b2-1148384ae28b | -2.25656 | -46.46233 | 2025-12-09 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49bbcc41-4281-3e57-90af-6d0dc15683a1 | -2.24603 | -44.83143 | 2025-12-09 04:53:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25bcce21-2e69-3aba-add7-42c5376d05c0 | -0.30561 | -51.68464 | 2025-12-09 04:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22f1b189-fb96-37d8-bc45-aec33070a1a3 | -3.42072 | -41.65821 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c33108f1-3d03-3461-a82a-06d59656b276 | -1.76797 | -46.19616 | 2025-12-09 04:53:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c987961-fa02-3a28-9d48-5ceb854ba1a3 | 1.57034 | -55.99448 | 2025-12-09 04:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 56cebc68-8d83-3cb3-ade3-c0a5b258786b | -0.80055 | -47.86273 | 2025-12-09 04:53:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa63ab07-1d4f-3793-85e6-28081976c549 | -3.43334 | -41.65617 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 30d506b9-c305-3156-bb76-28e987eb5c10 | -3.43272 | -41.66026 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2cf452d9-2759-3d2f-9866-23a275ec7868 | -3.43355 | -41.65183 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 264e06ae-a620-3d41-8a07-c70d0fa36abb | -2.09348 | -45.79368 | 2025-12-09 04:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d246d9df-02f1-33ed-b8e8-302f7f8c0d5a | -2.26294 | -46.06442 | 2025-12-09 04:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 550bec11-a74b-3ff3-8601-85e64c203983 | -0.18685 | -50.23039 | 2025-12-09 04:53:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eea2df6f-08c3-3d7b-bd7b-78fff751114e | 0.07389 | -51.43097 | 2025-12-09 04:53:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 66f25706-889f-3e1d-b5a1-d0c850c977a6 | -3.43177 | -41.66408 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 41d41d30-4e72-3230-996c-32e86c42f05c | 1.39232 | -50.64914 | 2025-12-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea15788c-8b42-3d14-8e12-d5711f183434 | -3.43236 | -41.65999 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2a557a25-1b96-3bbc-8a5d-237c4fffc22a | -3.33198 | -42.83592 | 2025-12-09 04:53:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7060704e-eb32-37f7-8bd2-086c157b9990 | -2.18653 | -48.12903 | 2025-12-09 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59f445f8-9cd2-372f-9d4d-b32edd8ebdc0 | -3.43396 | -41.65211 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 006c7548-6495-31c1-bbe2-33c4fb144779 | -0.60314 | -51.81647 | 2025-12-09 04:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3db4243-6993-31c1-8ed4-71d91726aa0c | -2.26068 | -46.46298 | 2025-12-09 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32c3a7cc-eae3-34a9-bf2b-f6a65895b90d | 1.57441 | -55.99384 | 2025-12-09 04:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ca64877-fb7b-3ada-97d5-68bcbeb17e9e | -1.76906 | -46.19526 | 2025-12-09 04:53:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d41153e-225b-37d3-a4bf-a96a4cc18719 | -1.72695 | -46.18593 | 2025-12-09 04:53:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f2afc82-db06-351a-8f76-65d90b519f1b | 2.02316 | -55.67484 | 2025-12-09 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e3b1ab-8964-36cd-9f39-4ded5461d1fb | -3.00449 | -41.75715 | 2025-12-09 04:53:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 588d6009-4e9d-3578-baad-84989c7d1b2e | -2.25275 | -46.10268 | 2025-12-09 04:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0959883-c5b5-3e0d-b4ee-62244e41efe5 | 1.57385 | -55.99027 | 2025-12-09 04:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cac68612-40b3-3c73-9d98-4a24d57598b7 | 1.1285 | -60.52294 | 2025-12-09 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f423564a-bf83-3d3e-a24f-dc5a66004d43 | 2.01863 | -55.67207 | 2025-12-09 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8847267e-4016-3c8d-bb62-0f60ea053e0a | -0.1902 | -50.23092 | 2025-12-09 04:53:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7f55bc26-a7d3-33ee-abe0-93bcd17aafc8 | -2.05842 | -46.50393 | 2025-12-09 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46d44bca-e6af-3cca-a987-3bd5057d236b | -3.43295 | -41.65589 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 139a0b81-f003-39de-bae0-1ef561f79ba2 | -2.09715 | -45.7984 | 2025-12-09 04:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 089ff66b-ea03-382f-bc7e-19ee06de28f3 | -0.80493 | -47.85894 | 2025-12-09 04:53:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d15f8e77-3bbe-3c02-b958-b10b106736d2 | -1.2049 | -52.09869 | 2025-12-09 04:53:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a21f26b-2823-385d-a192-48d5e693d1a3 | -2.11148 | -45.3623 | 2025-12-09 04:53:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27161ba1-98c4-31b1-96af-9d5091f79a76 | -2.10522 | -45.36367 | 2025-12-09 04:53:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e34205e8-e674-3ef2-8594-f1f6a385962e | -2.44917 | -46.19878 | 2025-12-09 04:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a68e04-58f4-3bce-acbc-e94dd1d2b714 | -1.60076 | -48.39359 | 2025-12-09 04:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
