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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a13f02d0-da78-316f-b9c0-37a0fba651fa | -11.32849 | -56.88455 | 2025-06-10 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 605cad01-7847-33dc-9942-dc3bea26e549 | -12.24648 | -51.43082 | 2025-06-10 04:40:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19bc884a-4c4e-3e39-b056-705bc1e6e22e | -11.70656 | -54.50135 | 2025-06-10 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80af96da-741f-36e8-8304-26384c82f5af | -11.83752 | -60.92601 | 2025-06-10 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fca6b5d-ca7e-3b27-8db9-adb6c3cf9f2b | -10.2776 | -47.60391 | 2025-06-10 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b40371b-5933-3ec7-9c09-1b037bf4ab4e | -10.94331 | -55.31339 | 2025-06-10 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cfddec7-d75f-3acb-b2b0-6f5e02af157b | -12.12967 | -54.66615 | 2025-06-10 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9b4e8c6-705c-36d2-a050-fab5939be7ab | -9.39148 | -48.43389 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 953d9988-9829-331f-9b56-f9210e232189 | -12.2901 | -50.10424 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3dbc677-7552-3b2a-aa93-6e5b437dbf9c | -10.847 | -53.76723 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4320b6c2-ab78-3f2c-9433-4e6bc7580e3b | -14.21337 | -45.48749 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50e41ac7-04cf-3b24-a4f0-e6a98eeceee3 | -12.21412 | -49.62282 | 2025-06-10 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d514df2d-c9da-3d63-bcb7-324c39c709c5 | -11.57389 | -48.13873 | 2025-06-10 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 037b2a0f-2418-344f-b34e-08592e1d7cbe | -12.29287 | -50.10832 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98a905ed-29e5-33c3-a2e5-8478e95c4503 | -14.20022 | -45.4897 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a0f80ef-28bd-34ee-8529-af4171082b8c | -14.50179 | -43.80628 | 2025-06-10 04:40:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87681d7e-a999-3df4-8133-8723ded583ab | -8.33761 | -48.45015 | 2025-06-10 04:40:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9ab7b51d-8efe-3809-9bb7-de504c85a294 | -9.38071 | -48.41332 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b2d845d-a0dd-3587-8462-3d01fb424d72 | -9.01436 | -49.58208 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80a6704b-9a55-3d90-8b93-7385d5dee993 | -11.13545 | -53.94524 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dc411f9-cff2-35a1-acd8-5e6865abbe3e | -10.37123 | -57.50077 | 2025-06-10 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa5858d3-1cac-344b-ba30-f578879562a8 | -10.30358 | -57.14045 | 2025-06-10 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67e5ccb2-e0a4-3785-a88b-5c1c28686c02 | -11.62611 | -47.6832 | 2025-06-10 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88d9ed84-960d-3d60-91bd-bc7ad108967e | -13.09323 | -52.2888 | 2025-06-10 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b18755-2e53-3ec7-805e-40a8b92aa9df | -10.05207 | -48.66146 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df2b910f-961b-3fa1-8bae-189a5e0096f1 | -10.04257 | -47.74647 | 2025-06-10 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3697b5a5-e802-3a1d-8379-0c81b555fe4c | -7.86027 | -46.42192 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 133eaddd-33f1-3872-9d40-636b7b0cec9b | -7.09328 | -46.44891 | 2025-06-10 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e853a0e-89cb-39a3-8d00-a0fb1c571a43 | -10.95298 | -54.37864 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8af7bf35-0c70-31ad-a389-8df684231947 | -11.36852 | -56.56241 | 2025-06-10 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a928a1ee-b97f-3497-863d-8eb9e24045f6 | -10.95214 | -54.37124 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9c9efac-88d3-3b76-91f2-277a53b8cbc9 | -8.6137 | -46.58923 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21cacbe2-1b37-363b-815a-e8e548d8c420 | -12.04913 | -48.08032 | 2025-06-10 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c84d74c-8b94-3c87-9464-29220fb90524 | -9.8629 | -47.88772 | 2025-06-10 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7389aa64-2d00-31b3-b42a-3c69a2979c33 | -11.76627 | -54.37422 | 2025-06-10 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dae8e6c3-0cbf-3d24-aac3-6819d09f6d20 | -10.94852 | -55.32997 | 2025-06-10 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee37bbcc-e50b-344f-86bb-6eaca784f9d7 | -7.92045 | -47.09858 | 2025-06-10 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83d4a0b5-ca42-39c6-8131-cde0e4c6ba6b | -11.26245 | -52.47602 | 2025-06-10 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6699a09a-7959-35b6-a573-697f16d13fc8 | -14.2139 | -45.48351 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ed3b548-73cb-3cbc-94a5-5b492d884a6b | -7.99832 | -50.72257 | 2025-06-10 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7fef776-d88f-3485-b84e-afa561bb809c | -14.20864 | -45.49088 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 206d182d-c801-3c18-b71d-191f71377a8e | -9.68828 | -48.5126 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a533c046-c4c4-3923-9e0c-cb686a248864 | -10.23999 | -52.21728 | 2025-06-10 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbc2d25c-76f8-383e-8a97-6940adfd36ca | -8.71507 | -48.01637 | 2025-06-10 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd96bece-3e99-34f0-8b47-704a925f054c | -9.59563 | -40.34316 | 2025-06-10 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 783c7314-58e7-3080-b72c-5a28cef819d0 | -9.08339 | -49.63931 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53ccd3ea-b651-3412-97a0-9a26cad956e4 | -10.86284 | -53.78308 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c6ef38d-d2a1-38b3-8b30-779b0bcc0216 | -8.96463 | -47.96492 | 2025-06-10 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 845b166a-2e77-3a63-a9dd-ef122008be36 | -10.8782 | -54.31206 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 854839a7-1af2-3eda-baa3-771721cfad70 | -9.08615 | -49.64332 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c15f53af-d213-326f-b571-24b4da82e434 | -10.05829 | -48.66617 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ce3899b8-aa11-38a8-92e8-a7cd816ea0d3 | -11.13655 | -53.9441 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f4115fe-843f-36cf-8283-4b134f1f4252 | -10.22852 | -46.9278 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 72d153cd-c36a-3b96-914d-e730a4ba915f | -8.70657 | -47.14425 | 2025-06-10 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acc754cb-5d6b-33ec-ac39-acbe06447236 | -8.61067 | -46.58436 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe3ea9b3-4777-375e-ae2b-4a1fddada1e9 | -12.29065 | -50.10069 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d0e4526-1944-37ef-8598-fa2ab222b9ad | -11.57702 | -44.88163 | 2025-06-10 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 684c016e-7864-3737-a643-350d9c95c2b7 | -12.28955 | -50.10779 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae0babd3-44ba-381c-aa9b-c9a5c251216f | -14.20969 | -45.48289 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3dfdfe3-21df-3771-8ecf-b582ae1212ed | -9.00235 | -49.19619 | 2025-06-10 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2f8e235c-e87b-390f-b639-aab482e8190f | -7.86023 | -46.4197 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 584ffe46-47b0-34db-868a-310e85132ac9 | -14.19653 | -45.4851 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e36c9b5a-812c-3736-8ba0-f100b61db8d0 | -11.13908 | -53.94584 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6978227-9799-3673-a02a-1570bfaaabd8 | -10.84268 | -53.77086 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6e06e7c8-11a1-3284-9e6f-f12496a55fe4 | -11.76995 | -54.37486 | 2025-06-10 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ed705cd-4c91-3360-b35c-8d701909884d | -9.00791 | -49.57751 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ef1bba6-55c7-3d48-b3c5-6ec18dafff40 | -8.61004 | -46.5887 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc7222d4-90e9-38ad-b771-bc76896b942d | -10.88113 | -54.31717 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17d37871-0823-3016-a7dd-d2345f6a248f | -6.8657 | -47.85864 | 2025-06-10 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6f70ab8-48b7-3e69-aa6a-132cf2e1765b | -9.59515 | -40.34695 | 2025-06-10 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2b7ef0f4-c405-334e-9d68-684a6fe91880 | -10.23939 | -52.22097 | 2025-06-10 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbc10946-ece0-3f23-9ecb-4426915b31fc | -12.13044 | -54.66165 | 2025-06-10 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 368fa229-8720-3ecb-9888-3987b7c884de | -10.22423 | -46.9316 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 35a0b787-e3a4-3e10-a5c2-33af3b38f893 | -10.84195 | -53.77512 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9be19404-8235-3647-98c3-a69fd6f59ce5 | -14.20074 | -45.48569 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd63d987-3114-3635-8109-4cf8da56c723 | -10.05097 | -48.66881 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e25d6a0a-448e-3e8d-a3d1-456acc0f4e2c | -9.65899 | -56.1083 | 2025-06-10 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8476aa3-f431-3653-b24c-9ba030cc2bb5 | -9.1411 | -48.21421 | 2025-06-10 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab5f6446-89c9-3a32-ade8-8871258637bf | -13.06235 | -49.25006 | 2025-06-10 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 227733b0-1785-3738-98c5-786e79c82972 | -8.60096 | -46.5741 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31f665a2-90c0-3dc0-b25e-ad9f44a6ecf0 | -11.57184 | -47.43577 | 2025-06-10 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a2f611d-d849-3aab-9a5d-5591981d2cce | -10.24459 | -46.89451 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abac2b68-5592-3ebc-bbd3-24afda2e5a18 | -10.84442 | -53.77259 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 05c12506-d7db-355f-8c90-a0284eaec552 | -14.21706 | -45.49209 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 412a8419-ba22-35af-9733-b8f7065451f0 | -10.84511 | -53.76834 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9737e643-0e91-31e9-877c-a3ad03b184af | -12.21077 | -49.6223 | 2025-06-10 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cf4289c-fd60-34ce-95dd-1c6677e18c3a | -14.20548 | -45.48227 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f90d5bce-5dc6-39b3-a99b-a9d2cdf38b43 | -10.87743 | -54.31652 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad224c7-ab96-3c1f-9936-33d43c1b138e | -10.04813 | -48.66462 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ea8f9c0d-6914-3191-b787-b9e8057a99a1 | -9.22044 | -48.86232 | 2025-06-10 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e472c85-afa4-3cb9-88c9-0ce2d75a9436 | -11.59076 | -51.33765 | 2025-06-10 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89e478ea-a746-3d9a-a065-48e330a58613 | -9.85942 | -47.88718 | 2025-06-10 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6f750ee-ee94-39a5-8783-d1e5348f64cc | -12.10012 | -44.75068 | 2025-06-10 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1cbc5e5-0319-3e1f-bd12-32449295defb | -8.60524 | -46.5703 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d422d1ff-42a2-36f1-9319-1b8abaeacefc | -10.01413 | -48.67498 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9b442fb-aacd-3148-abb3-187a91acd317 | -9.00845 | -49.57403 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af61d56d-9b08-371b-95e3-d0b7cb7a93a7 | -12.27561 | -44.59153 | 2025-06-10 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 355dcb1f-64d6-3089-9e9e-53a82c3a264a | -7.27455 | -49.56981 | 2025-06-10 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09d73806-7322-3738-ab14-2ea4f4716781 | -10.84011 | -53.77626 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6be7645d-ded6-3d13-9664-4aae616bd21e | -9.64882 | -48.56691 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README10.md)
