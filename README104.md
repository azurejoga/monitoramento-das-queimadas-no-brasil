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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcb31868-5dee-37c8-9409-b1bf5a5848be | -9.34438 | -48.94609 | 2025-09-12 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b0d3d9-7bda-3ea0-88fd-6e04c7123030 | -9.51573 | -54.6359 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d49f2f5-8dce-3d2c-ae99-8a4cf08acba0 | -9.89718 | -51.88633 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 143c61fc-b368-3f97-81fb-72f3c2fc4d8c | -9.71525 | -48.30716 | 2025-09-12 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d3b5f478-2a23-30dd-8024-338cc7be5db0 | -9.07609 | -46.9529 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8cd1542e-099a-3d02-8640-b268133e79d1 | -11.95413 | -51.1768 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2ff11899-d05a-3db1-af52-621ac0adbd95 | -10.55666 | -51.48715 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8dce86e-a033-3d70-9f71-e061be2793ef | -11.95498 | -51.17009 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c1e1337b-9c71-3d84-82e7-af5b5596ff21 | -11.03334 | -51.51653 | 2025-09-12 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b002d85d-189f-34e1-b03f-4c3ca46715ab | -11.16349 | -57.1859 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fb1aa23-89a1-3c48-9243-058a764321e2 | -11.19033 | -55.08543 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c759469-1738-3dee-898f-5cc3190681d2 | -10.33352 | -58.02425 | 2025-09-12 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5287d4e-ab40-3638-888e-7cfa41c15d0b | -9.79695 | -57.44579 | 2025-09-12 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6048e5eb-da39-38d1-8fba-5925ef9e8f87 | -12.50022 | -47.43526 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ad473b8-024a-3a67-9c6b-e834709e1344 | -9.52028 | -54.63298 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 9da5cd7c-6c90-3e2d-b63f-02777a18c34c | -8.08105 | -54.74915 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56c052a0-38d2-3379-8e98-37cdf72504af | -8.64673 | -55.24975 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3709d152-be82-3fc4-922f-d7179f0fc7a5 | -10.42658 | -50.62488 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae43067e-7135-302b-b1b7-b6cd4766921d | -10.54022 | -51.53521 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 504b979e-9c45-34c3-a250-f2c82c2bcf6c | -9.12513 | -65.48586 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6660c871-28ed-3e11-823b-77fa1e02ffce | -9.91958 | -56.05986 | 2025-09-12 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3eb303e0-38ac-360c-9c0a-e25977a9e0db | -11.98427 | -51.14058 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4948c2c0-3c33-365f-9d72-f2f2f8917719 | -12.82208 | -47.96997 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b49cdc0d-c7a2-391a-bb8f-e77b17cef61e | -9.52385 | -54.63701 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 572f4bec-79f2-375b-b58d-d2d1d89bb705 | -10.67266 | -48.64251 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ccca7e20-0588-3e64-bb9d-1f49e34bd4e6 | -11.19282 | -55.06757 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be96b823-552e-3060-b905-d2feac7e1484 | -9.079 | -46.95865 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cdb4f0b8-a347-382f-ba1c-e94cdf0c65b4 | -9.90957 | -57.05695 | 2025-09-12 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a505ab02-6d1f-38c5-95ac-0fadd17e869e | -6.82929 | -52.7924 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e9ca4ba-e4f3-30d3-add3-c2a1f14d4aac | -10.40158 | -60.81416 | 2025-09-12 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c691df70-f885-36d6-9a99-3fd38b4c7c8b | -12.83116 | -52.96251 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3aed962a-6e48-3c60-b690-0abdac090d0a | -12.82257 | -47.96552 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1a71c8bc-cbb1-397b-b0ab-57421c4b217c | -11.95244 | -51.1808 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 278b6c16-add7-3047-8ec1-bb01fc2ce01c | -12.24602 | -46.75657 | 2025-09-12 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16de825f-dd49-3a42-8366-d0afdff66ea1 | -11.95815 | -51.17817 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 878e8bb0-c4cc-3f2c-873f-deb0f47861ab | -9.4584 | -47.65125 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c588611a-d5fb-344e-a518-e8821133a9ff | -9.03752 | -47.08037 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c40459ca-e323-33e0-93c5-571bbfe53996 | -10.3627 | -50.52164 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 369e6bfd-3f57-348e-add1-06a18c052f25 | -10.67212 | -48.59333 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5c2c27a-1f0e-370f-b4a2-c8dc746b638c | -12.90227 | -47.95813 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 491c792d-2317-3b95-a238-84f5e4cb766b | -9.06092 | -50.50274 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f0adf08-b5e2-3477-9461-4cb0402ea44a | -12.0077 | -47.76474 | 2025-09-12 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09f41b06-b885-3a56-8fb8-ba3a9bfc9f77 | -7.56241 | -61.31231 | 2025-09-12 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9e60b4f-11a1-356a-a8e1-4cbd3f42543f | -9.98722 | -51.7094 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24bc868c-f4f0-37ef-bedf-526e95dd3865 | -12.20228 | -53.86031 | 2025-09-12 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a07e610a-5697-3102-9969-a07a5198b8cd | -11.54548 | -50.4016 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e98ee3ac-1f1c-37b0-a6e6-4f37e18fe24c | -9.98998 | -51.72722 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b26d9ed5-fae0-389f-88ee-419bddcab1a6 | -9.98157 | -55.0498 | 2025-09-12 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f70f51fc-8d54-3372-82bc-33c8701ca949 | -10.66684 | -48.63952 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d9eb057-56c0-3463-ab38-1668f4b6b738 | -9.60306 | -55.01006 | 2025-09-12 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 446fb5ac-9d0b-3478-88ee-8a7f6e0caccd | -10.3514 | -50.52368 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7dc53601-fab5-35e7-81f7-bc98261edac6 | -10.36042 | -57.48705 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e709d18-f7c2-319a-ade0-7ebe79fa5492 | -7.41897 | -50.65916 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae000496-8c95-3db7-8f3f-7ffff7251128 | -11.96997 | -51.16957 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| be7e9153-9b5d-3422-bb1b-72e7711b7a72 | -10.361 | -57.4831 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72088606-2732-3e97-89b2-d508225233af | -11.18426 | -55.06995 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93c457fd-c7b8-3d92-9c9f-a21a32dc7dcf | -9.72681 | -64.93063 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f311bd66-0486-3ee1-a9f8-55c0487193f4 | -11.10991 | -51.3423 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a9b7b2a-56fa-33b6-b0ae-5a2d85748a9a | -7.85627 | -61.16918 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5669a3b9-33c4-3a5b-b085-9b2e4b59b427 | -9.25628 | -57.07072 | 2025-09-12 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cd38c3e-784d-3eb4-9a47-657f2053e011 | -10.6776 | -48.65382 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a2786384-5d3d-3f02-8eb5-4d923cb2e143 | -7.85966 | -61.16973 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc57e20b-4762-3d03-b24a-3c1823652e9d | -10.67167 | -48.60034 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ca77516-0f52-30d7-8e7c-c4c9d63004c8 | -9.89162 | -51.89046 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a032a2ec-3238-3a38-b1d2-c450282a2702 | -6.4884 | -55.52246 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 132b86d4-71c6-32f5-b222-58ff2fd3d755 | -9.35682 | -65.45338 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4ef95c4-6630-3fd0-a78d-5e4861d01946 | -9.87656 | -62.14685 | 2025-09-12 05:18:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99bfec01-359e-3280-8d60-810cd05a3c94 | -9.35197 | -65.45654 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60be281c-d6c9-3379-850a-5159118777ca | -10.52878 | -51.50268 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8db7cafe-0d75-3fa2-b385-ada7507808d4 | -10.53454 | -57.08612 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f60f6ca-f2b8-3e9c-9f63-d27e3a191607 | -11.87489 | -58.8187 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f5339e5-e7e1-391e-9e26-2c7a857add6b | -7.56182 | -61.31604 | 2025-09-12 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b2aabb8-095f-3061-9b3f-10e8f959fae6 | -6.62887 | -62.84822 | 2025-09-12 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7ee37f2-3a12-32bf-bff9-87d84c8925ff | -7.42236 | -50.65641 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0a78fd43-5b57-363f-8df3-614618bc3718 | -7.49142 | -54.94674 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d116b9f-0e6b-3ee1-80d1-1d48e713613b | -11.95284 | -51.17744 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 55e3761c-edb2-33b7-ae6c-811aa9fe7a20 | -7.65851 | -50.26895 | 2025-09-12 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41f887f2-39fa-3a37-aa85-9fe33f3700ef | -11.52196 | -50.59688 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc0eba89-e6b8-304f-8eac-3f2f99582124 | -9.72435 | -64.94486 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 639ce88e-f430-37ff-8a92-0f0c5d152747 | -10.67793 | -48.65092 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19fa4eb4-d3f4-301b-83af-9d8c2d2dc705 | -8.60502 | -54.69812 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14f17e9c-eba2-3a2f-bc4f-a36741868450 | -8.05233 | -52.32328 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abd0a9ce-6f1c-304d-ba4c-726a0a22e2b0 | -13.02281 | -48.00201 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28ecd138-625f-320f-ba0a-218a236f2721 | -12.98383 | -48.00502 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c24e542a-d64e-3b05-80e7-eb9c8e2e8528 | -8.08714 | -50.18624 | 2025-09-12 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 525f8f7f-029f-3d14-9851-82ed76bbbbb2 | -8.57869 | -51.34964 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dfcf84ac-02cf-3e00-8dad-80ccd62f4d66 | -10.5319 | -51.51916 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 586b2bb2-be23-309a-9162-3c4cf5d20668 | -9.51622 | -54.63243 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4f61df6c-d548-3f03-8d6b-3e6d46612c52 | -11.87207 | -58.81453 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47086af5-844f-32c7-b1e2-13af3901664c | -7.85105 | -46.0665 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1076b0d0-e8d1-3e0c-9179-e01d49d7f8fa | -9.95009 | -50.3171 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 042ee327-6f13-3cef-8bc4-f64a63c7ad74 | -9.0613 | -50.49979 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6679d044-d179-3a64-b877-ee28441e03f7 | -11.87151 | -58.8182 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d78e6ee-f225-3bd3-96d7-536832e1ddba | -9.06482 | -47.04256 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 14830ebd-3d7d-3451-a3ac-c7e7a7039179 | -9.07162 | -50.50401 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f982453-91fc-3424-86cc-395e48a8455f | -7.72127 | -50.35819 | 2025-09-12 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2228a5b6-592e-358a-904e-1e0c4d187167 | -10.546 | -51.53042 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd136d70-6c54-3546-b1f6-3d6b131b5478 | -11.95456 | -51.17345 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 589b69a7-c231-34d9-9df7-383b3c471bb9 | -10.55553 | -51.5368 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed0315d3-82c6-3364-840a-09b4dd02a25e | -11.70417 | -48.28942 | 2025-09-12 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README105.md)
