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
| 03b2af6a-26af-3108-832a-c324bb1e4887 | -12.50316 | -57.77296 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a048a1d8-83e2-3f67-8e9b-da5f70d462c7 | -14.38728 | -47.76271 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2eeeb740-fb07-3e55-82f6-663aafa0cc29 | -14.39237 | -47.75876 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c4a9bac-5ee7-32e7-9c12-59bc0daae66a | -14.74742 | -46.30222 | 2025-07-22 04:53:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 791b78a3-d75e-3f14-bdee-c7df7c9b0be9 | -14.76446 | -47.11363 | 2025-07-22 04:53:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b6c09cc-c6cd-3a4f-891c-2d56d27ac1b3 | -11.96315 | -47.02692 | 2025-07-22 04:53:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e88b5876-cd0c-387f-b6f2-e8d8befd98db | -13.6905 | -45.68897 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00d0032b-9a10-3545-af95-49915f3e3444 | -11.72902 | -48.18491 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5a117b38-dd59-3389-8add-c37c9317f070 | -13.65417 | -45.73139 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a541066-7c64-3db8-8deb-85f94754fa6a | -11.72444 | -48.18506 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a92c703-4712-3e68-b37f-669b27d07027 | -13.69125 | -45.68268 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f5fd6393-a1ca-35d3-be84-1a7a373399ba | -14.77778 | -48.2893 | 2025-07-22 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9502642b-5a89-37d3-99a5-7f0a9c678312 | -12.47247 | -45.86601 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d486fea-fae3-351b-8b69-5eb55be11c56 | -10.68474 | -56.55003 | 2025-07-22 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e51ab0d-5ee2-36d3-8fd7-ed27c628edc0 | -12.65666 | -45.05309 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29dc8af7-905a-3068-bc54-436cbf25d753 | -14.74762 | -46.30193 | 2025-07-22 04:53:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97156a38-0fb3-329a-aa37-cd49879fb0aa | -13.64728 | -45.72435 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 21a3460d-39fa-3523-b5f1-49d8d0734fee | -11.73324 | -48.18553 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6e76ae33-74a7-3fe7-b0b6-fd2b11a22622 | -13.692 | -45.67639 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18d2707a-f1f6-37c9-a3e7-18e2e84c0d82 | -12.65625 | -45.05639 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c3f45c3-829b-3065-99a7-4a2df9994704 | -12.65538 | -45.05548 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e85e2696-5a80-31aa-bcd6-254fbb597cec | -11.73483 | -48.17356 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fd82200-00b4-3d2d-82cd-12a0ddbe8369 | -10.04049 | -59.09669 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9adac531-9b9a-3f1b-bccf-148e435221df | -14.39291 | -47.75443 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| caf91003-78e5-37f4-b129-c9ff0f5c416a | -13.65163 | -45.73131 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b6ac7f36-bd2f-3d6d-9072-5793081276b2 | -14.64679 | -46.83753 | 2025-07-22 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cb9c7b2-f139-36e8-ab1b-c28272b0dc65 | -11.94012 | -63.85216 | 2025-07-22 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c18bdf5d-5a8b-3121-9547-e4c9b88671f9 | -12.50023 | -57.76795 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 56ddfb6c-a26e-3f72-8cfa-b1fb4e66e890 | -11.4644 | -48.163 | 2025-07-22 04:53:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4c0450d-5d30-3056-9f04-f4975cfd2f5c | -12.65576 | -45.05218 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4358ee7-43c5-3a52-a7c6-e8519283b4eb | -11.94558 | -63.85323 | 2025-07-22 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f07f586d-5557-3c53-b7f9-d1af3a8beff1 | -15.93118 | -43.52118 | 2025-07-22 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f7d283c4-f51a-3453-b387-cba04eb532b2 | -11.81053 | -44.27063 | 2025-07-22 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73f2565a-74d9-3e5f-95bb-d8b37082c5c1 | -14.38782 | -47.75842 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ca0e9a3-bfcb-3ff9-a5ba-c7251f4e461a | -15.92994 | -43.5234 | 2025-07-22 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 93309340-b967-3a3a-bcc4-9a4953dd2031 | -10.29687 | -60.54077 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6980a45d-2f63-3b4e-afa0-5a23aef7824f | -12.71672 | -47.79779 | 2025-07-22 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09d3d3de-5da0-3750-9720-22804a988b95 | -14.76848 | -48.25723 | 2025-07-22 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b0ed98c-4255-326b-bcc4-453219efe6ec | -9.97557 | -62.25377 | 2025-07-22 04:53:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e66a83f3-a308-35c3-9ed2-969394713b57 | -12.49656 | -57.7673 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 13106ef2-1c94-3bb9-8c37-35630799301c | -13.45446 | -48.01715 | 2025-07-22 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07f99175-7c4f-3d01-9ee6-9fc153611b76 | -13.65561 | -45.71908 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2faaf999-54f8-3a08-9379-570182f7a030 | -9.98067 | -62.25472 | 2025-07-22 04:53:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35e109c8-cf46-3967-b3e9-04d99b36a36e | -11.73535 | -48.16961 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 641ada59-631a-3c0d-8793-e6687a7f6db0 | -11.72955 | -48.18086 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f268cfda-9cbb-3ac8-88c8-46edd5b737bc | -12.25942 | -63.8238 | 2025-07-22 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c9049dc-82bf-37b9-b892-d477859168f6 | -13.62022 | -47.73695 | 2025-07-22 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da4f4ea2-762f-39cf-9bbe-f9aa19f4c9cd | -13.6524 | -45.72515 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| af173793-5551-386a-a99a-a67d9cbda3fd | -11.31005 | -55.11325 | 2025-07-22 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7330550-61ee-328a-a01f-e30ce17fbdc5 | -12.47675 | -45.87256 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66bf25b9-0c5c-31ea-81be-7284a07f43c9 | -13.68647 | -45.67884 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf1e833e-b38b-3324-9ad2-1a79d5fcbe30 | -9.46371 | -63.15285 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e586fc9a-ec4a-3708-8f59-d3d647818c3c | -10.29607 | -60.54536 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06408383-e635-3194-a30c-d5ecd5dd54f4 | -13.62078 | -47.73254 | 2025-07-22 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbf5b094-af4c-365e-af5a-5ade384d62e3 | -11.18966 | -48.62088 | 2025-07-22 04:53:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 35cb44e8-812c-37df-b387-20393299deb6 | -13.65525 | -45.72217 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bb211e46-e2f5-3404-bd83-906a6ff85e9c | -11.73008 | -48.17688 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e40ecf6-09d4-3af3-843d-9e32f5b4cfae | -14.74796 | -46.29892 | 2025-07-22 04:53:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8c36745-db44-32a5-95ac-2126379a0726 | -11.19424 | -48.6178 | 2025-07-22 04:53:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca817a40-673a-31ab-a0bc-652ceb67b590 | -10.0494 | -59.09431 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb7a5737-7ee4-3d80-a66a-0384810fdf37 | -11.73431 | -48.17749 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 081f5a85-0461-3d5e-9898-35da8f126786 | -13.67647 | -44.22495 | 2025-07-22 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 346fc0b5-4b2b-33b4-98bf-c298f77fe830 | -12.49507 | -57.77604 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f876d4fc-4821-3a73-9a07-4c03bf50b0ef | -11.7306 | -48.17294 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e4db8bb-f9a6-3253-9371-6d4c82ad7646 | -12.6858 | -45.6585 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 548768ea-c824-3a21-833a-9b733708bc91 | -13.49237 | -45.5146 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 732145d7-e163-3b20-8679-6338a5f4e7a9 | -15.93166 | -43.51645 | 2025-07-22 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fee5bf13-bbfe-3142-b258-6a8fb39a3285 | -13.49719 | -45.51842 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2c69ccb-3612-31ad-ac67-eb4dd1ef7f44 | -11.30554 | -55.11992 | 2025-07-22 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38219050-b066-3024-bb75-676e498d7070 | -9.45892 | -63.14822 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e340e733-58c2-384e-ba3c-c9066d00ada4 | -13.65453 | -45.72832 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0670649-58d3-39a7-93ee-d6fcc47414b8 | -12.14296 | -44.93066 | 2025-07-22 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b57f80d-7b5d-3308-b7f7-2d631cf1e09d | -10.29876 | -57.12241 | 2025-07-22 04:53:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3201f1a5-7dba-3da5-8e34-29b543037fdb | -10.04874 | -59.09808 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8cf776b-d956-3283-85ad-4af9008a2d48 | -14.74779 | -46.29921 | 2025-07-22 04:53:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42cc7413-3e0a-3041-847c-eef8d539e919 | -11.3089 | -55.12047 | 2025-07-22 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0634d12-9342-3059-bacd-7d86c31d4e3e | -11.19373 | -48.62148 | 2025-07-22 04:53:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89ebe1df-9863-3e1c-8ad7-91c2fc82050f | -11.73747 | -48.18615 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f9e4fd7e-e7ab-321f-aaf0-7cf8b8ba11f4 | -12.47283 | -45.86307 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6351d5d6-f98e-3ed5-8706-368a408fb80d | -9.86975 | -57.19562 | 2025-07-22 04:53:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 405e2dd3-3083-39fa-9558-9af7c4304bfd | -10.05287 | -59.09878 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15ca8f59-abad-3c71-abb9-dd3fa793de2e | -13.65013 | -45.72135 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9d52f9a4-ab23-31c9-ae62-244771725bfb | -11.8101 | -44.2743 | 2025-07-22 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c987dc20-56b2-396e-8998-3cc7e7d4a528 | -14.38893 | -47.74949 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e305d62d-2a3f-3ee6-8b74-b576571257dc | -12.49949 | -57.7723 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f742685f-bcea-3a25-a74f-a02f6787ed07 | -14.76792 | -48.26159 | 2025-07-22 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69d87c57-a0ac-340e-b824-25081bfc0d9e | -13.64941 | -45.72753 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 791c790b-331e-3fac-bad8-c6720dc0da63 | -10.057 | -59.09946 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aefe7ac8-f80b-3fe9-a8a6-9e67384a4733 | -13.69928 | -45.70293 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3aad1a62-efc3-3afc-9d29-65287be3fa3d | -16.80525 | -51.91095 | 2025-07-22 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24dff58a-2348-3526-b180-b61301da7d96 | -11.72533 | -48.18024 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a3542562-4e1b-3b3e-9538-4cba1ce6bf49 | -13.65278 | -45.72208 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cefb13f2-bd1e-369f-a930-4627a75398b6 | -13.64977 | -45.72444 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f6bc2eab-c59e-3737-95e0-b59baf276597 | -13.65489 | -45.72524 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 67c25fa5-ac0d-3e45-9c3a-2d97a07a2c63 | -11.72638 | -48.17229 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2873f4a5-4591-395a-a75c-e307a5499e40 | -11.71922 | -47.77553 | 2025-07-22 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db68a611-b47d-3b76-abcb-dc70daabba14 | -11.7248 | -48.18427 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1cd2ef55-d599-3411-9a7d-df671058ee64 | -11.73853 | -48.17811 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78d50c3f-d471-33d5-a178-289f936a46bf | -11.738 | -48.18211 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| cef407dc-56db-3622-899c-3db3668e4d1a | -14.64745 | -46.83215 | 2025-07-22 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README16.md)
