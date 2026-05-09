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
| 007622aa-7f3f-39f7-bd5a-b6541eff7976 | -6.2256 | -55.64466 | 2026-05-09 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef1f8a96-5b21-3f9c-ab5b-453f7996f3db | -5.78508 | -45.12909 | 2026-05-09 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dfdae94-e22a-3777-b589-624934c59955 | -6.19204 | -44.87022 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59e15252-31d5-38bf-9655-e6fcc631239f | -6.33072 | -44.63601 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29dca3b5-e7dc-3115-b74c-39856025142f | -3.14132 | -40.63995 | 2026-05-09 04:27:00 | NPP-375D | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 80d751bb-8c7e-302a-982f-3076bbcfee75 | -5.53326 | -45.95229 | 2026-05-09 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae75c13c-2c40-357d-8f16-780de9c37c96 | -6.1854 | -44.86917 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 013b4992-046d-35bd-a4a3-c7c1cffe7c04 | -13.65776 | -47.69605 | 2026-05-09 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55cbcd08-7fbf-306f-8f41-0104171c2c42 | -13.81293 | -42.88953 | 2026-05-09 04:29:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93539327-fd96-34b7-a4fe-3c73fe915f24 | -8.72528 | -48.32177 | 2026-05-09 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06f4ad07-d3ff-3027-8939-b6580c96dcac | -10.63977 | -48.02477 | 2026-05-09 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 747b4d49-ff1f-3d40-8a2d-78afbfaf264f | -8.70404 | -49.08534 | 2026-05-09 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a8b99c5-8d70-3b06-aeed-5b87897defdb | -10.66456 | -49.7037 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e68ee29-6c17-3c2c-bdef-14789a8fe7b7 | -11.82271 | -47.33891 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 24b75a99-7ca5-3529-8878-0e153a4b1b6d | -12.86216 | -43.75736 | 2026-05-09 04:29:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3825aa6e-d2a0-3dce-ac3d-1aa96bc26e63 | -13.81101 | -43.65438 | 2026-05-09 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 854c6861-df4f-33f8-8166-21bdae643538 | -13.36025 | -43.12249 | 2026-05-09 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 65389124-3824-3687-9953-4977e0281127 | -11.91634 | -54.10359 | 2026-05-09 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 535d76a7-e8f8-3f65-a467-8b1d48a3463f | -8.68981 | -49.07132 | 2026-05-09 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b535c9ad-1d95-33a0-b7a7-4b4c1ab22233 | -11.59831 | -47.10123 | 2026-05-09 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cb0e15d-6910-3ed9-931d-8050741ce470 | -10.04854 | -51.67081 | 2026-05-09 04:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59f79fd3-569f-336f-ba3c-90e152bf456d | -11.91793 | -54.10674 | 2026-05-09 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aeedd300-13ae-34c8-b92a-a123f6d90217 | -11.29467 | -54.75687 | 2026-05-09 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efd0f7b3-0210-3fc8-9222-dadc0cc8aa94 | -8.72618 | -48.33107 | 2026-05-09 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a8811e8-b522-326f-b9db-770c07d744f6 | -11.76709 | -43.64735 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd8e8790-3aad-37d4-84c4-bb42bd175555 | -10.66616 | -49.71563 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7de4d91-6bb7-3c55-88a1-71b58f81c989 | -11.92387 | -54.10215 | 2026-05-09 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62297a1e-0d09-3992-a5e8-4c3b8d0a2d88 | -12.49893 | -45.43403 | 2026-05-09 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 077048cc-ba51-37d3-b8a9-bb46a9c6d605 | -11.76781 | -44.09085 | 2026-05-09 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97a1a7eb-48a3-3f02-a87e-f0f244e4df13 | -14.13814 | -45.38946 | 2026-05-09 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b815fc27-16c6-3bf9-9a04-27ef0caf1e0e | -11.78158 | -47.09473 | 2026-05-09 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 662f0cd6-c5a9-31a9-b88e-16f2a67cbc15 | -10.664 | -49.70582 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d3d8c4e-06aa-3ca6-ab5c-17da48de0193 | -11.95496 | -47.89402 | 2026-05-09 04:29:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0aedb95-cbca-3fea-8b2a-71131935d9be | -13.37098 | -43.20289 | 2026-05-09 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4089c784-a180-3f7d-b1aa-3552f360f597 | -11.60166 | -47.10179 | 2026-05-09 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc5727d7-b3e3-39c7-9fde-9ce3973722e8 | -11.92122 | -54.10455 | 2026-05-09 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2778ed25-94a9-3ab4-8696-47b64e3b27e3 | -11.86127 | -48.97504 | 2026-05-09 04:29:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00025890-ec14-363f-a901-a95ec448f917 | -11.81933 | -47.33834 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b3587455-fdaf-303f-b6fb-9aff41a93e9d | -11.77934 | -43.66142 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5531e98-cdc5-37de-a7b6-a951ffa08cc5 | -13.37036 | -43.20718 | 2026-05-09 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 60401e19-5a13-30b2-8699-df27ad9214af | -10.71188 | -56.04508 | 2026-05-09 04:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b157325-be8a-339f-b961-76cc0e04649e | -13.65836 | -47.69238 | 2026-05-09 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb608a7-ccc0-39eb-bc59-4e294123250b | -10.66479 | -49.70126 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54a8967b-af25-363b-be1a-a850e63a23b5 | -11.82667 | -47.33584 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4bf57f0-7889-33d3-8d29-2a502991e381 | -11.29286 | -54.76632 | 2026-05-09 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e9b6ff4-4acd-3a96-8289-cee6d7ec1c53 | -14.65428 | -40.9996 | 2026-05-09 04:29:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 463306ec-3c90-3ec9-a40f-af0e854ee450 | -12.78286 | -47.42724 | 2026-05-09 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c467cba-f097-3c26-b4ce-7ad43464f64c | -10.64323 | -48.0254 | 2026-05-09 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68286adb-ef81-3e50-9571-fa74643b7ced | -10.67388 | -49.69345 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 400d90ba-5b5f-3861-9ea2-1ba0791a985b | -11.93983 | -43.3787 | 2026-05-09 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a28973b5-e980-3f7d-865d-58da79304808 | -11.295 | -54.02595 | 2026-05-09 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebd6742f-a7a0-3e97-91f0-33fdf8712272 | -11.77584 | -43.66087 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfb90d15-ee78-300f-888a-b76eae38a1b5 | -11.919 | -54.10119 | 2026-05-09 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16bfd5bc-908e-31fa-bd50-156d253034ca | -10.6335 | -48.01957 | 2026-05-09 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c185c663-7aa4-393c-b7b2-00a4f5b99cad | -8.72921 | -47.97899 | 2026-05-09 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 642cdafc-07c5-336a-b2a3-8e8af7c25ed0 | -10.97758 | -44.53795 | 2026-05-09 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41903f95-74e2-3c43-b876-60e47f52dfa0 | -11.76942 | -43.65581 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92a95de1-8e34-36dd-9c8e-d98d0af4748a | -11.77292 | -43.65636 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b15d22cf-562f-3334-b46a-3a4ddc27f004 | -9.45974 | -47.82218 | 2026-05-09 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65419d8a-5979-3cc5-9c11-ed4f662a52f6 | -10.67092 | -49.68823 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6183581d-38e1-3e37-afc6-21f1f3de2bef | -14.14151 | -45.39 | 2026-05-09 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa9914e2-6b8d-3a60-b36e-ca9cf376eeb7 | -8.70481 | -49.08086 | 2026-05-09 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94cd0ab1-669d-3d7a-a0c3-19ce59401b8b | -8.704 | -49.10143 | 2026-05-09 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56029d2e-fe30-3d8c-b570-fc2836020980 | -10.63004 | -48.01895 | 2026-05-09 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42001a82-75b7-349d-ad82-eaf89b2e2e05 | -8.7255 | -48.33519 | 2026-05-09 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17e79004-b435-3386-b538-92382acf226e | -12.13894 | -40.89471 | 2026-05-09 04:29:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea6a0da2-52be-3049-901c-cebf776f30d2 | -9.64548 | -42.96251 | 2026-05-09 04:29:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a5a83a84-433a-3aef-96a8-193ffe4f9a54 | -11.59772 | -47.10483 | 2026-05-09 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f4b9842-09d9-37e1-b3a8-34df2bd83818 | -11.9882 | -47.36981 | 2026-05-09 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e721ea96-cafe-3673-a564-0e7e3f4145c1 | -10.55768 | -56.34327 | 2026-05-09 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f50150-209b-3d03-9071-af5c2354c639 | -11.77126 | -44.09139 | 2026-05-09 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63a54878-56e4-3346-980d-8ce3548e2234 | -11.82608 | -47.33947 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7c8afd9-eeb0-3a86-bc45-1050983bd596 | -11.77875 | -43.66538 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d86b804-c8ef-3e12-9bd4-500a0f9d6a36 | -10.55414 | -42.43688 | 2026-05-09 04:29:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 93b35e21-870b-38de-a3c6-15a9b8c12892 | -9.64427 | -42.97049 | 2026-05-09 04:29:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bdddbb32-6849-3ce2-abf0-42717a752739 | -11.29347 | -54.76316 | 2026-05-09 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6fe5573-bb36-3595-95d5-30c3e88ea14b | -11.86321 | -48.97379 | 2026-05-09 04:29:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24b7c40f-aad7-321e-859d-55eb2c1400dc | -10.71263 | -56.04127 | 2026-05-09 04:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d75dde1-3f1d-3be5-af56-1c82780f3032 | -10.63415 | -48.01568 | 2026-05-09 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da84fe14-a69c-369b-9445-4f27662aa78b | -12.31841 | -45.46801 | 2026-05-09 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a105432-381e-3b63-9446-971909c0ee4f | -11.79893 | -47.09395 | 2026-05-09 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d1282fd-3468-30e7-9351-59c4008d079d | -13.3639 | -43.12308 | 2026-05-09 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3a7f09a9-ebdb-3edd-8ca3-d43b2560099f | -11.9772 | -46.7893 | 2026-05-09 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea11642d-13e1-3608-835d-583c04e56133 | -12.88486 | -49.33713 | 2026-05-09 04:29:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d11124f-665f-3bb4-acab-65aada9ba41c | -11.77993 | -43.65747 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cf07579-bdac-39a6-b100-24d7c2be2f76 | -11.78216 | -47.09113 | 2026-05-09 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36723075-e14d-34e8-a91d-eb8ef181d2d6 | -11.77001 | -43.65185 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf186a09-aeba-34cb-8aed-1728c5e7513c | -13.64266 | -44.2873 | 2026-05-09 04:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c9a3614-44e1-3a79-9f5f-2bb4787768a5 | -11.2999 | -54.02692 | 2026-05-09 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46640a96-f09c-3ce8-bfa1-f05f2c3d2db0 | -12.34907 | -50.03203 | 2026-05-09 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a4a1a25-db62-369e-a2e2-6809b4a6a74a | -8.72393 | -48.32232 | 2026-05-09 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad933fba-70f6-3c55-af3a-f87cd8f7f12c | -8.72987 | -47.97501 | 2026-05-09 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c44405b-67d9-3640-99f4-16f20a8b59dc | -8.70469 | -49.10394 | 2026-05-09 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93567943-c45d-3112-97a5-f0fd103e36a5 | -10.04783 | -51.67486 | 2026-05-09 04:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c4c7508-90a0-399d-9389-ecf9c952e6da | -10.04926 | -51.66676 | 2026-05-09 04:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94e4a912-bff8-3026-acbf-1c2b2c59b4e4 | -12.85863 | -43.75681 | 2026-05-09 04:29:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97afedf1-fc2a-390f-ab4f-1c066d4df2a1 | -12.13589 | -40.89495 | 2026-05-09 04:29:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a00160d-fd43-34c2-b752-1f1afdd10b17 | -10.66854 | -49.70192 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 246e5e25-58c7-3db0-bc50-95536cf37a78 | -11.81993 | -47.33471 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1716a4d3-decc-319b-b183-bda71daad2c8 | -9.45868 | -47.82289 | 2026-05-09 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
