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
| 07c34289-0b0b-3800-9e9b-ec78ec881a5b | -9.97408 | -48.24256 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e0eed2ab-7d93-321f-a9a7-70290e6a5cc8 | -14.73577 | -48.40556 | 2025-07-01 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 446f80b8-caf3-3300-9fc4-f20fd34ba23d | -17.81942 | -45.31994 | 2025-07-01 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6bfcf0d-3c15-327e-aa3a-efed7f5f98aa | -14.13669 | -46.34487 | 2025-07-01 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91d97dac-0e02-31e9-b5d6-db1f73b506d0 | -14.73794 | -48.40477 | 2025-07-01 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a3de8b2-66bc-3ab5-b76e-49cd66b740f0 | -9.56949 | -49.10749 | 2025-07-01 03:55:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0df2b7a5-aa5e-32c1-966b-8f964cb1b3e9 | -10.06386 | -49.65955 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10785a34-f5a9-3781-87b1-42fb27f2e551 | -14.20525 | -45.51859 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6232189-f416-36df-9532-8d15dc4dc3f6 | -12.82031 | -47.36763 | 2025-07-01 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27e19a6a-2995-3d60-8061-fb7b15e277ac | -14.6177 | -46.81432 | 2025-07-01 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf874b27-0806-3351-8283-888a20ec646f | -18.45688 | -40.03717 | 2025-07-01 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e0664240-ad33-3fb9-8ffc-6dcd16a0f5a5 | -17.75383 | -42.89256 | 2025-07-01 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f9abba9-9701-3b23-8c7a-47c4ca7893f7 | -10.68442 | -47.20766 | 2025-07-01 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8776c59d-bc49-3b51-b0c7-7cd5c67ca5c8 | -9.96885 | -48.24164 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30d8359e-3334-3c98-9092-0a807343da03 | -9.97 | -48.23543 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 543b85b6-5d44-3d5d-b044-ca5613fcf038 | -9.9758 | -48.23324 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d628eb4b-c374-3d27-b55e-d9f3da4904d4 | -10.07829 | -52.75334 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 886dd23b-60f9-3232-8d74-3fcd14c1eb93 | -14.31439 | -43.70857 | 2025-07-01 03:55:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9449a6bc-715f-30b7-a501-8389a5484042 | -9.9735 | -48.24576 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4ae34f2-6f5b-3d7b-844d-a8f1db95ea96 | -17.20069 | -44.32703 | 2025-07-01 03:55:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c32fff28-9e7b-3c37-b756-4a1e211778a5 | -11.57432 | -47.43322 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82aecd0b-4cd5-3b5a-a0bf-a863e5bd54eb | -13.00741 | -53.42847 | 2025-07-01 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77f07c81-8e51-3e52-a097-a518d4b4997c | -15.1375 | -44.84606 | 2025-07-01 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a830791b-8978-3462-9690-048e54e0dacf | -10.08777 | -52.74163 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a82f420a-d2a2-3c4b-b01d-75787eaf2016 | -12.32731 | -42.83506 | 2025-07-01 03:55:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3247ca99-719e-32ce-ace0-8ff006af26ee | -15.92057 | -43.51571 | 2025-07-01 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cf846be-c087-38e0-a99d-870ab3bf5571 | -12.01949 | -47.77656 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 92102ffd-0f0a-3c2f-ba88-8536eb507a64 | -13.70202 | -45.61819 | 2025-07-01 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 542fc633-88d9-39f0-8b4f-207992a7c1ef | -14.44142 | -48.87075 | 2025-07-01 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a4ae1c1-8fc6-3f9e-86db-7ca3d1af91df | -15.07925 | -48.944 | 2025-07-01 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a8a9dca-26e8-3cbf-8a9f-493b2eb46926 | -14.20457 | -45.52228 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71327f08-494b-3890-96b5-b509e71d2297 | -9.97524 | -48.23626 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4fdd5ef7-affd-35e5-ab47-2bb808c56500 | -10.07961 | -52.74673 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| edd130c1-ed3d-3fde-a53e-8caa8594383f | -14.20053 | -45.52152 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aacb521-18f6-30d7-a19b-d2c54be1c6e3 | -9.96943 | -48.23849 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9a315d7-bc57-3552-89d3-96bc7fcb9bec | -12.56964 | -48.88866 | 2025-07-01 03:55:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfd57055-4672-3298-93cc-1ec190a6de6d | -20.76345 | -46.77015 | 2025-07-01 03:57:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bead584d-3d3c-30b2-b768-a9f47e946e86 | -19.98152 | -47.17715 | 2025-07-01 03:57:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aad228c4-da95-306c-a604-b980d8993994 | -19.38338 | -40.2097 | 2025-07-01 03:57:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51a8980e-0ecb-32e8-a01d-0406e0002bdb | -21.12986 | -48.59211 | 2025-07-01 03:57:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5606954d-ae6c-3740-bb87-6bc552f7175a | -21.50842 | -44.31254 | 2025-07-01 03:57:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6acd8a91-3013-3c1a-80ca-abf2e8f09f45 | -18.35715 | -43.5409 | 2025-07-01 03:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cab501be-4bf7-3c2e-9d90-a92f61d48287 | -21.13062 | -48.59077 | 2025-07-01 03:57:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5a1c1220-88ea-3353-b707-bb06bbd41f8b | -19.73304 | -43.42904 | 2025-07-01 03:57:00 | NOAA-20 | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8614814b-df0d-3c16-b2d8-098c0c6855e1 | -21.6265 | -43.46764 | 2025-07-01 03:57:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bb440f85-ce94-3216-aa22-16b0abe47284 | -21.16519 | -43.0387 | 2025-07-01 03:57:00 | NOAA-20 | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 133f8324-940f-3a3f-b0f7-b55efd7d2c3c | -20.80552 | -44.63271 | 2025-07-01 03:57:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| a585ac01-a772-36c6-8d89-dd4132dc13b6 | -17.93488 | -48.92286 | 2025-07-01 03:57:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59dab971-edff-3529-9151-c2638bc65833 | -19.51172 | -44.27786 | 2025-07-01 03:57:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0be0fc84-43e8-3f61-bbef-b9ab786ef174 | -19.4527 | -45.30715 | 2025-07-01 03:57:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6ef8bb0-1afe-3684-b089-549b0165686f | -17.93593 | -48.91759 | 2025-07-01 03:57:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c8765f3-0895-30ed-9e30-0edec2048908 | -18.95582 | -42.09755 | 2025-07-01 03:57:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 77c4d830-be1b-321f-a0e2-12402a0c6c74 | -19.43883 | -44.34177 | 2025-07-01 03:57:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4db8498-c57c-3cb4-a883-c8c000307f4e | -20.41849 | -43.55148 | 2025-07-01 03:57:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ef41777-adaf-3dc4-a1c4-d9befaf259a2 | -22.79599 | -50.19742 | 2025-07-01 03:57:00 | NOAA-20 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3dbccd26-7ae3-3bbb-880e-ffc41a8f6236 | -19.88953 | -40.65244 | 2025-07-01 03:57:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 29244ec7-8644-3dc7-8628-f83837450f67 | -20.09199 | -41.34123 | 2025-07-01 03:57:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bdecb930-6c0a-32d6-a103-57d1822fc248 | -20.69627 | -42.07475 | 2025-07-01 03:57:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9425eed0-27e3-397f-a75c-066e0e2f56f9 | -18.44449 | -47.34923 | 2025-07-01 03:57:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dda95a57-0a96-3a7e-ad0c-69e4962b32a0 | -19.77662 | -43.44128 | 2025-07-01 03:57:00 | NOAA-20 | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c8614b7-2448-38af-a26e-7c131405fc57 | -18.89821 | -42.14128 | 2025-07-01 03:57:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a566a8db-409b-3b84-ac16-bdf4fa6c5499 | -21.1342 | -48.5931 | 2025-07-01 03:57:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9269c1fd-138e-384a-af1c-143a08c00456 | -22.01839 | -44.29542 | 2025-07-01 03:57:00 | NOAA-20 | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 39f1e1d4-ae5f-3bbe-a54e-10423ad9f853 | -18.29175 | -44.68452 | 2025-07-01 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36b086b1-723c-37a1-bfbd-25b55bdf7f4c | -20.69685 | -42.07106 | 2025-07-01 03:57:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb697991-98c5-3c89-b9a3-9cdbd77df2b4 | -19.46874 | -44.2954 | 2025-07-01 03:57:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 725c5874-68d2-36c9-a976-ca61d8c70c74 | -21.74715 | -43.37576 | 2025-07-01 03:57:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e806ea10-1d50-31f9-ab7c-8c3370e42491 | -21.84012 | -47.47165 | 2025-07-01 03:57:00 | NOAA-20 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7fbbf352-49df-37dc-ad3e-1d456df5b028 | -20.52826 | -48.57513 | 2025-07-01 03:57:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb9edb16-4c65-3077-ab0e-e4e914dea221 | -19.98081 | -47.18095 | 2025-07-01 03:57:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 264db5bc-c36a-3d73-804c-14c8b4bb0c3a | -20.59555 | -41.22253 | 2025-07-01 03:57:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 31ebe3e3-6ba2-3d69-904a-0ea7cc769cca | -22.70772 | -47.35573 | 2025-07-01 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6379ea94-17fc-34ef-a55b-0c9eb2c9eb3d | -20.22424 | -41.01229 | 2025-07-01 03:57:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bcd06670-1cff-3de0-9068-99016a0eb05a | -19.52159 | -44.26265 | 2025-07-01 03:57:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3f7205c-47dc-3a8d-b06d-8781a92898fe | -21.8882 | -45.01009 | 2025-07-01 03:57:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9982dde9-b3f4-398e-ad74-f2184cbd9390 | -22.33064 | -47.4073 | 2025-07-01 03:57:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| febd90a5-2c6c-30eb-92a3-1592dd1521e9 | -21.17918 | -43.97954 | 2025-07-01 03:57:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c4d97c00-f64b-32c7-b02c-dfcbccfb4190 | -10.8832 | -56.4367 | 2025-07-01 04:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 035a330d-8616-3e32-9c5c-f0abfcf0be01 | -28.58456 | -49.44091 | 2025-07-01 04:00:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 21078515-4522-32a4-bf40-279a6b29b55b | -6.2943 | -43.6891 | 2025-07-01 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| d772d7b5-5975-3a85-a10c-d9101f025731 | -6.2945 | -43.6659 | 2025-07-01 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 84f75045-0d71-3b41-bbbc-66ffacb2a0e6 | -6.2945 | -43.6659 | 2025-07-01 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 75877324-6003-35bc-9082-c84774ecce1f | -6.2755 | -43.6907 | 2025-07-01 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 432bc0cf-f818-37c7-b085-7f9c86b85fd2 | -6.2943 | -43.6891 | 2025-07-01 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 672556df-b589-31de-94a4-16bce6ba3d59 | -6.2943 | -43.6891 | 2025-07-01 04:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 9788f21d-4f88-3cef-9452-8c03af504207 | -6.2945 | -43.6659 | 2025-07-01 04:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 0bb98524-fba6-332f-b026-f8a4cde76065 | -6.2945 | -43.6659 | 2025-07-01 04:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| dd046d82-0209-3022-8c53-edd28293706c | -6.2943 | -43.6891 | 2025-07-01 04:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 8513f479-d995-3234-9b06-28d5d0b474ed | -6.2755 | -43.6907 | 2025-07-01 04:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b8941a14-cdd4-30b7-83a3-a9f5de7eca3a | -4.54816 | -48.01257 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cce9676b-664f-3273-8e31-e7bf1cc67cee | -4.54936 | -48.00461 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbbcb953-76e1-3c82-bb08-d9e6c2e88b5f | -2.58856 | -51.92369 | 2025-07-01 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64326e5c-9f21-3f99-b213-e0716dbff99d | -4.53931 | -48.02336 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39d19916-2e02-3ca9-aed9-edaa79905f25 | -2.17155 | -52.45737 | 2025-07-01 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56997dde-232d-3b7e-9f9d-269e26cd360d | -4.3762 | -48.06944 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04c34689-fa5d-3045-b9e6-ef0df35314b6 | -4.37971 | -48.06997 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7cfb1b7-e035-3522-980a-58f75e8ced7d | -4.32055 | -48.08095 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeb24243-312f-3815-866c-df7752a346e0 | -4.31645 | -48.08436 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58f1ff6c-1d16-3d11-98fc-edda41dcb2f8 | -4.54876 | -48.00859 | 2025-07-01 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6faa478-ef69-3c62-aac5-5c67b4b3ea53 | -4.11054 | -47.93733 | 2025-07-01 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
