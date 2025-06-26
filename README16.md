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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27d96b15-4f1b-32fe-b449-d3759cb5d7c0 | -9.48022 | -56.07416 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3be4e237-668c-35d9-818a-aea60b03bead | -7.89832 | -61.52294 | 2025-06-26 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96640040-f6ae-3e34-9d2f-519b0fca84ea | -7.97849 | -49.65285 | 2025-06-26 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45beaa55-f010-3f03-8caf-b0bfaa42bb8d | -8.71083 | -47.85696 | 2025-06-26 05:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6d76267-6277-3f4e-9a77-41a03d63844e | -9.70939 | -49.47635 | 2025-06-26 05:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a30fdcf8-832a-30f8-927c-d9939af22e42 | -4.68759 | -48.86993 | 2025-06-26 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e82b951-80b8-3117-936f-4d859ec51566 | -4.70905 | -55.99201 | 2025-06-26 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25424a85-cf01-3609-af4f-b4574d3bf5ba | -8.47769 | -48.26394 | 2025-06-26 05:06:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a02724a8-a6d8-3309-bcc6-88330cbbb59c | -7.92687 | -61.55476 | 2025-06-26 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bb070fa-a5e3-3b5d-b1dd-64d1a6911a30 | -11.07009 | -46.63661 | 2025-06-26 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd275aa2-1806-3257-8621-d764dc0cb102 | -9.50131 | -56.09189 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 75987647-c5fe-341c-a459-f4e786ccffa3 | -9.11694 | -49.44702 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8f123174-ade8-35d0-a336-180ddc6be858 | -8.26197 | -47.02607 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 410d5c5a-09d7-3f99-b03a-8808ff7de7ca | -5.84251 | -48.39475 | 2025-06-26 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 724d0169-3451-3c9b-88e0-5665b3341eff | -8.26001 | -47.0265 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5c6128c-4ad1-32b0-bc18-1691e5429dcb | -9.67525 | -48.77126 | 2025-06-26 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e244540-f689-31c5-b6a2-cf0e05d22939 | -8.72036 | -48.016 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e15ccdd-53c2-3d50-806b-0efdec7c97f9 | -7.20831 | -43.08356 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b106a424-87cc-38cc-a984-d946f65fe7b8 | -4.68823 | -48.86554 | 2025-06-26 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1237537-ce27-326c-a2a8-ce76aca2efeb | -8.97068 | -49.8642 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4be86e1e-b2bd-3102-bb3e-7bfbd70c24fe | -11.8086 | -57.35213 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 386712dd-27eb-3c0c-b456-822232b86c3c | -10.82798 | -53.73953 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efa6325a-d7b3-321c-9c74-7dc480484e55 | -11.36499 | -48.71262 | 2025-06-26 05:08:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a415f6b7-896f-39ed-b2e3-bba2db51634c | -11.79758 | -47.53846 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b2fcf03-db9b-35de-a12e-d6c160a7acb2 | -11.06994 | -46.64278 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa6306da-4709-379b-a42a-4821d82785ad | -11.82438 | -47.54888 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d24ec49-6225-3a2f-aaa8-34bf59d02067 | -11.88546 | -54.67848 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 278d1d3f-86ea-3027-8c42-8bfe0817dac3 | -11.08521 | -46.66095 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79c0c5df-e1c4-304a-a645-55d6807141c9 | -11.81217 | -47.55801 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d1af2fe-3ba3-3db3-8131-8f7cdb3c906b | -10.71493 | -59.13305 | 2025-06-26 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8802255-7b7c-309c-8819-3a5f457842d8 | -12.61508 | -57.87629 | 2025-06-26 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 848076ea-ee90-325f-bb3b-cf9b790f2c95 | -12.0229 | -57.09028 | 2025-06-26 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7736fa11-f1c1-37e5-b468-86c974e564de | -11.56699 | -52.09169 | 2025-06-26 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fec7987-f345-3681-897a-70f1bbb24fe5 | -11.2981 | -54.70778 | 2025-06-26 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3876a7c0-0e77-3a5b-8163-e44e335e8518 | -10.32002 | -52.56412 | 2025-06-26 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55afbc97-cc5f-38d9-9db7-7819173f7fbc | -10.87195 | -53.77449 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42c4f005-dd0f-3e5f-bdc2-53fecd1decc9 | -11.95776 | -47.01942 | 2025-06-26 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d969ab47-1876-361e-8e7f-c0b2051c8ea7 | -12.58024 | -56.98855 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 110cb795-747e-3be0-9648-b2e9dae2a19a | -11.80324 | -47.54021 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4193fb6f-e750-332a-95ea-76d393b05bec | -10.06852 | -55.54934 | 2025-06-26 05:08:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7cd4fa9-19eb-36a6-9085-26955392a698 | -11.0857 | -46.65698 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 138238ef-32fd-3580-9d85-79a999b54f66 | -13.10097 | -52.29171 | 2025-06-26 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ac29abe-e4e2-3498-91fb-d1e4ec88bdc9 | -11.81192 | -57.35268 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 803206fe-8554-305f-a772-f8b0a2b2654f | -11.60916 | -46.51024 | 2025-06-26 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dd7c481-9a24-3abd-95ad-cc0dc68e2795 | -10.81715 | -53.73789 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b255d99-cace-397c-ba89-47998adc8c2e | -11.79784 | -47.53896 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c7f02b-dd9f-33d0-8df3-47f60568927c | -10.104 | -58.23153 | 2025-06-26 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77ea1e4e-ef6f-3cb5-a0cd-a39f5fd80088 | -12.52861 | -57.18673 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02006e2c-0a67-37ad-8b37-342543156256 | -11.44432 | -54.47761 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac317e13-7aac-32b4-82d5-468e838bbaac | -12.13088 | -50.17449 | 2025-06-26 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ba55f8-66a1-31c6-b528-7d204afcd039 | -11.14058 | -53.92151 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51c83817-8494-346d-a18a-445cb8c5baee | -11.88606 | -54.67456 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 976c9a6c-9a03-309d-8700-b3fdda0980aa | -10.70859 | -59.12805 | 2025-06-26 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2429138-38b7-362f-984f-9541852d6101 | -12.76227 | -44.40879 | 2025-06-26 05:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60794880-6521-386b-adab-968e6f20eccf | -11.24015 | -49.48789 | 2025-06-26 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5f2fa28-2e23-34c0-b2fc-8d871e0049d6 | -9.79317 | -57.42992 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6d5729a-4c10-3b1c-8319-ec8da6ab618a | -11.80253 | -47.54311 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37c5959f-06c0-3d56-8b96-41be1b324d01 | -10.50491 | -53.58831 | 2025-06-26 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23307023-85ba-3184-ac5f-21552ade220f | -12.58449 | -57.38754 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36a4720c-220b-3bba-a3ba-b0ee9780e31f | -11.79743 | -47.54237 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11dc2aa0-e2ce-3e50-b64b-63082e1ed6ff | -14.48938 | -46.49794 | 2025-06-26 05:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eb584b0-2262-3f4b-9e05-144d88e0b501 | -11.91581 | -54.81379 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a0bf3ca-1275-303d-8c56-5a78edd8d009 | -11.07259 | -55.36988 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 509a839d-bee0-3f88-b4dd-137afe092d51 | -11.93221 | -47.8477 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54362a40-439e-392e-b1fc-4bafd85c40c0 | -11.82894 | -51.25582 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3245c831-1aea-38e3-9f42-301fbdf408be | -11.84111 | -51.26166 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca07c7ff-6278-33e4-b36b-9cdc00d96e2f | -11.95113 | -47.02641 | 2025-06-26 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed722845-eb3f-301b-b5d8-5fba53a97296 | -11.83194 | -62.7647 | 2025-06-26 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb93f8d1-b16e-3f40-a795-777444c7c607 | -14.90556 | -54.32953 | 2025-06-26 05:08:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fe7b409-978a-35bc-b919-56a4ce5f5722 | -13.78102 | -54.29701 | 2025-06-26 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 286994ed-7b77-39c6-a6f2-9078362ab049 | -11.81803 | -47.55541 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 975a8281-9bca-3969-8ea6-67371ab47e11 | -13.10049 | -52.2953 | 2025-06-26 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c622987f-cb80-3051-9931-2d285eb4c4d5 | -11.57083 | -47.43301 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef704043-d20e-3055-aa5e-5a4fcbf1db7d | -11.8142 | -47.54133 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24805dfd-b9d6-307b-a001-bbe26e775ad8 | -10.82923 | -53.73112 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8abb1993-bc4b-3645-a1a1-6488ad8b9f41 | -11.81248 | -57.34916 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 308e86b0-a284-3019-9cce-830dac86aac2 | -10.82013 | -53.74265 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f79ef594-70d8-3f80-8e21-40f6f3f6e4c5 | -10.1636 | -53.92389 | 2025-06-26 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84abc310-1bf4-3bd4-ac16-7d62a12e5fc8 | -11.86503 | -54.6954 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa6216f-bc93-3539-aafb-8b630c0a63d7 | -13.03856 | -48.82764 | 2025-06-26 05:08:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 895a9d47-99ef-3e4d-8035-1c03d156adde | -13.29231 | -57.08205 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d344e15b-d029-3fc7-a8d6-25c9a9352df4 | -11.23958 | -49.48648 | 2025-06-26 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6db3418e-9ca0-3a2e-a685-709fe2461d2d | -10.87787 | -56.45464 | 2025-06-26 05:08:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e3bca92-3ed7-3f52-bd92-5c330480606c | -11.57024 | -52.09757 | 2025-06-26 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 63a2e194-2ea0-3993-acfe-c3845ba297e3 | -11.806 | -57.35121 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d430936-2514-3331-8790-d5120dcc55fe | -12.80335 | -48.73262 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69c6e21f-7fde-3c4d-ab14-01dea0e787dd | -11.95396 | -47.02528 | 2025-06-26 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ad03dca-cbc1-30ac-932a-72ecb2558b33 | -10.70574 | -59.12362 | 2025-06-26 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb2d4222-d89a-37c6-8671-2f0f79aa8959 | -11.06525 | -55.3725 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea0a83f8-9848-370f-b009-6d780cccd4b0 | -11.81258 | -47.55466 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4dd8df0-7b0d-31e5-b9fa-6db319f25dff | -12.80845 | -48.73336 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deaf3662-05aa-307e-8a6a-4112671e1d6c | -11.8247 | -51.25518 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c913266f-2c98-3774-934e-f826287a13e6 | -15.08029 | -48.94317 | 2025-06-26 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 145bff0a-9af5-3aac-b59d-eab96a73843e | -11.80871 | -47.54086 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b054156a-ba8d-3a3e-bef9-a16028208d0f | -12.58837 | -57.38455 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae32466-7080-3dcb-9581-392aa7fe984f | -11.83888 | -57.85878 | 2025-06-26 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae0db456-17b8-3174-aa43-eb381c922b07 | -12.80296 | -48.73563 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aa22254-a409-3d70-82cd-a580804aeef1 | -10.52462 | -53.62995 | 2025-06-26 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d7fbcd5-9dc2-3ef4-98bc-82b197951bcb | -12.04603 | -48.07641 | 2025-06-26 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b729c048-f117-3e26-9bcd-0f1ea3868366 | -12.58891 | -57.38108 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README17.md)
