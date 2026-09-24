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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50988777-baf4-3588-96c3-a0e677ecb86e | -3.7201 | -54.204498 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edbe45cf-051a-325b-9f5c-e7302af9078d | -14.0029 | -42.902 | 2026-09-24 00:16:00 | METOP-B | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 53eca033-2c98-3643-8596-d3686e7f72e5 | -11.2673 | -51.353802 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce31b9bf-3420-31f5-a99f-e7f2b84c6fe5 | -1.4288 | -54.5909 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56b2446-c6ee-3499-803d-090e193587f7 | -3.7325 | -59.4104 | 2026-09-24 00:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2e3202-6424-38cd-b9c1-d6a9b1c78111 | -11.2477 | -51.3582 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0b6efee-ad53-3be8-b830-9b893b678aab | -11.2395 | -51.3675 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14c41af2-0201-3e21-a32a-3e543ab96aae | -11.9468 | -50.748299 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2896e96-f5f0-313c-baf9-8edddb3ee359 | -7.0418 | -49.8326 | 2026-09-24 00:16:00 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf8eebb4-7dee-39f4-a790-6d88b4803c33 | -12.0301 | -50.288502 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7720cb1-7afa-368b-b5f4-e1820520900a | -8.1413 | -49.5438 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d51375c2-eb1a-3f65-9505-cf272a529359 | -3.7157 | -49.0411 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a867e722-e842-3595-b6d3-835b8d97ff79 | -8.1279 | -54.816799 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 576db800-5493-3a64-9729-8dd96f27dc8a | -1.6313 | -54.895401 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d96f1b02-246b-3b03-9abb-b756b0d84a21 | -2.6301 | -51.695499 | 2026-09-24 00:16:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af0aca0-2901-3f88-bd81-52921e7baa28 | -3.8181 | -58.868801 | 2026-09-24 00:16:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26ed4228-f04d-3974-8783-c26595ea75b0 | -10.9326 | -43.854198 | 2026-09-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfc54137-4b04-35ed-8476-6fdfc4b5117e | -13.2152 | -51.566799 | 2026-09-24 00:16:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0f5ac4-cd6a-3bf2-9f39-c3807197d9b7 | 1.2923 | -50.8466 | 2026-09-24 00:16:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 13c81db8-2f79-32e9-85ce-ba2c332a4f24 | -7.4174 | -47.3522 | 2026-09-24 00:16:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4b5a829-53a9-3a21-ab0b-26bb6792ef8a | -2.9839 | -54.271702 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15f97182-c346-3128-afca-7772cd15ce4b | -7.6762 | -45.483799 | 2026-09-24 00:16:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 162484c7-d8f2-35c7-a86c-d464efc5b257 | -6.6506 | -55.0504 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83bc0de0-452c-3315-9872-a8e37dce2a28 | 3.8385 | -51.797798 | 2026-09-24 00:16:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e628b955-ccba-36b4-aa5f-3c30350dd647 | -5.7881 | -49.176701 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3fe0b4a-c392-3be2-b718-314598c94828 | -9.2301 | -47.381802 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6accb8-f846-31a3-a69a-63746992b9e3 | -5.5566 | -42.719002 | 2026-09-24 00:16:00 | METOP-B | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82bfa44d-0358-36d3-9b65-4e585533c39d | -12.0152 | -50.313801 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 251c0f52-e518-3c83-8f47-043785596454 | -1.3293 | -54.652 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dc2ffcd-1992-34bc-8cc2-2d83ab0a6f5d | -13.212 | -51.551899 | 2026-09-24 00:16:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74c9254e-a502-3fd9-91f6-7eb4fb2604d5 | -9.1384 | -40.105301 | 2026-09-24 00:16:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1f952045-4b70-3603-b9f8-d2e120305320 | -10.653 | -51.320301 | 2026-09-24 00:16:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6f85920-f76f-30aa-b6fa-1b21a770c502 | -10.8841 | -52.045399 | 2026-09-24 00:16:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6950cd-98a4-349d-939e-6c352ad9a365 | -12.8501 | -44.380699 | 2026-09-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e61b587-e9df-3ced-a6a6-78b2d016e194 | 2.16 | -50.8801 | 2026-09-24 00:16:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c0d08b27-57b3-3ef0-a9d6-6504263818be | -9.1404 | -49.946701 | 2026-09-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2542599d-ff62-3e9e-82a0-a7973e2dafde | -3.4557 | -50.067101 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b47dbacf-1e99-3663-af46-d19ab3959a95 | -10.8825 | -52.038101 | 2026-09-24 00:16:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69bf9fd4-a2ed-3521-a981-192dd90cdf23 | -5.1876 | -44.680199 | 2026-09-24 00:16:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23b005d7-0d49-31e3-bfc6-894c2bda6ef5 | -5.9587 | -49.966099 | 2026-09-24 00:16:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4a76cb2-dccb-33dd-8435-3065e198bd39 | -4.2796 | -55.425701 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855c97d3-3616-357e-868d-5d327656b4d5 | -10.0937 | -46.013302 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0a2adbd-065b-335b-80b7-68b0303f93f4 | -13.2006 | -51.5466 | 2026-09-24 00:16:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5dfa76d-4091-30fd-893c-d5cc8e01aa0b | -6.5176 | -52.812099 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd95c69b-cfc1-330d-95aa-21c060f6ad23 | -3.4493 | -50.084 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66477b1-b4c8-3690-afe4-a7ddc0f26d2c | -15.4735 | -47.906898 | 2026-09-24 00:16:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b551108-d1e7-32ba-ac3d-dda8e07e142e | -4.0228 | -52.0662 | 2026-09-24 00:16:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61fa403-388a-3c61-a07c-33784fe7e22a | -9.1388 | -49.939701 | 2026-09-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8758af-04d4-34c0-945e-4fc064dfb76d | -4.0993 | -56.189301 | 2026-09-24 00:16:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceb442e2-6563-3ad6-8dd8-4d865b52af64 | -4.052 | -56.300201 | 2026-09-24 00:16:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68b8a4fd-7da5-3dbe-880b-ca8494ef7c7f | -3.731 | -51.276901 | 2026-09-24 00:16:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b497a1fa-e0d5-3e55-9f2b-edb3cc355d9b | -4.5166 | -54.964901 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 883a482c-ea9e-3670-b22b-48d34494fc9b | -1.6348 | -54.910801 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 628f9fb2-37b5-316c-9f8a-8d74dbf3c3cc | -1.8329 | -55.700901 | 2026-09-24 00:16:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2030db3d-275f-38fc-b7a6-b1930a19b3dd | -3.7916 | -52.4118 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb15887-8359-3c14-bf05-9517a1a65878 | -4.1082 | -51.076599 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ca81b2-52bb-3d0d-b620-02cedeb00fad | -4.5362 | -54.960701 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d96642-8d63-3b9f-82a4-f8789ed0f941 | -3.7087 | -54.1991 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c6471fb-4126-38b3-9167-661f7f24735f | -11.2411 | -51.374599 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c52e7d0d-81d1-301b-b595-5ddded8dfc3e | -1.6232 | -54.9053 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0f539c4-096d-333d-8096-cacd97abdf48 | -5.1041 | -60.243401 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cae75c61-d71f-33d4-ab41-2e72587b2724 | -6.4382 | -59.927399 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 162ee579-3548-3c7f-b35b-2ff8d78397c7 | 1.3004 | -50.8563 | 2026-09-24 00:16:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 84e07562-4c7c-381b-a1d3-d1039ced930d | -9.5886 | -47.767399 | 2026-09-24 00:16:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5de272b5-eec1-3640-a1a1-6979521edf41 | -2.2464 | -48.744701 | 2026-09-24 00:16:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dada53fa-59c4-3cf4-929e-2674e994f982 | -11.0125 | -49.701199 | 2026-09-24 00:16:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8959588-1927-3eea-aa63-a6a45c003061 | -11.6574 | -43.4865 | 2026-09-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f4bb2b8-9a01-35d4-a84d-82124f4d93c5 | -7.2656 | -45.534302 | 2026-09-24 00:16:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4804322-a45d-38d0-83ae-74febc5313f5 | -12.1 | -50.743198 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a9bcdc4-0b2f-32c6-88dc-0b1b82b8af0a | -12.1355 | -47.3549 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e20de593-caa7-3fc0-afdd-019961b536e3 | -2.1147 | -49.5201 | 2026-09-24 00:16:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e58bff62-9de8-3e20-9fa4-a6f9b91afb1d | -7.5517 | -54.997299 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d716f895-77ab-3612-b8e3-e205f6b7d22d | -8.4508 | -45.919498 | 2026-09-24 00:16:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4722fb92-6db1-3416-9c27-4fd059ddfdf7 | -5.7703 | -45.095798 | 2026-09-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3a3cbeb-d547-3223-9aed-0d8da710bf4d | -8.2612 | -54.769402 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3575b890-0e8e-3c08-8bbf-6a031a6a906c | -3.4476 | -50.076599 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54cbec41-9eea-38ab-9699-9f1e4d7c6e96 | -4.3019 | -49.125301 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6ffac5-cfe3-340a-b258-93efe93a9049 | -3.2412 | -54.3176 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8da0caf2-99e1-3349-ab49-d6f98d1607fb | -8.7257 | -47.607601 | 2026-09-24 00:16:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b212d347-f137-3670-af44-f8529347ba45 | -3.7053 | -54.184101 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3646168-42ce-3349-9562-f7c741e72074 | -4.1092 | -54.4729 | 2026-09-24 00:16:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf3907d0-220a-31b8-ab11-d75e629307b4 | -10.9261 | -43.828201 | 2026-09-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31d6db6d-0bf4-3b39-9974-30dd170e0601 | -3.6423 | -54.731602 | 2026-09-24 00:16:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69aec07a-3d2b-3d38-a5cf-81b028e4b105 | -6.7154 | -44.146801 | 2026-09-24 00:16:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbfeabea-ca60-3bee-a1a7-7e93cef427de | -12.3507 | -48.195099 | 2026-09-24 00:16:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b40c29df-bd06-3a6a-9de1-f1283eaf7b68 | -11.3479 | -43.363499 | 2026-09-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca742a7a-9cd8-3409-a8df-cbc54173e5bb | -10.9731 | -54.0849 | 2026-09-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 217e8502-028c-3cf2-bb32-55c6d5f3df53 | -2.9805 | -54.256802 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6e2e615-e84e-32f6-9d67-54417edde984 | -2.1686 | -48.315601 | 2026-09-24 00:16:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c10b014e-55e3-3763-9789-63117da00e71 | -2.1129 | -49.512199 | 2026-09-24 00:16:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 630e3cb1-e6c3-307a-8112-d5070bb01f9f | -3.5226 | -49.367901 | 2026-09-24 00:16:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d43e670b-edeb-3c67-a48e-b8d402b8b614 | -3.2123 | -53.362499 | 2026-09-24 00:16:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6390e70e-492e-34e6-99c6-9accb6da3fa3 | -12.6865 | -47.0173 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e230538-5eda-37a8-8323-26be99a9bee1 | -11.7978 | -50.9594 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5db299e-0610-3a71-88df-feb744143728 | -15.9539 | -42.959499 | 2026-09-24 00:16:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7548d8-9e20-357c-8379-da0bb5decb8e | -7.4322 | -49.826 | 2026-09-24 00:16:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfbe097-1dff-3e78-8431-7eecd718e743 | -5.8769 | -51.5597 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b8716fe-cb34-36a8-85f9-959bf09ec7ab | -11.4805 | -42.3297 | 2026-09-24 00:16:00 | METOP-B | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 303e717c-6a0f-375e-8140-aa271b124f15 | -8.1259 | -54.8078 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a7d85ac-30cc-322a-a9b2-e1cf6ffc2e28 | -3.7036 | -54.176498 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
