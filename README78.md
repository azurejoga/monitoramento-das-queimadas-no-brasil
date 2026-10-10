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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccc9aa12-c5f0-3dd3-b038-385c5da22e33 | -6.31412 | -58.3089 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa343a10-032b-3cdf-a08e-c225fd984f0f | -11.02691 | -45.4271 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8ffa31d-3c3a-3798-8567-6c7d04076a23 | -6.50028 | -55.31818 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cca33acb-bc65-3755-8f9f-6bae3328161e | -6.36513 | -55.16549 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae59948f-32b9-3fd5-8463-6a32fd4d05a0 | -11.07944 | -44.11935 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e233a70-5bf2-3ac9-ae11-3e3e622385b3 | -7.50422 | -54.99323 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e147ea5a-0b64-3e56-b1dc-acba9b0e51c8 | -14.32926 | -44.66286 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 086b995f-9b46-3b3e-9440-1aeaf02ca2f0 | -11.00124 | -45.39729 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d482317-b59e-3d17-a495-d51506cb8eee | -14.4602 | -43.93224 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c08e4b95-b896-351d-acfa-8a9cacfadaf4 | -13.20055 | -48.13958 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6cda918-9064-381f-bff5-59054098d703 | -12.93073 | -47.44213 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72ade30b-b072-3ef7-8b5e-40e8efda4196 | -8.21963 | -45.80091 | 2026-10-10 04:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34e9f1cb-0978-32ad-8d22-62a3fa55da1f | -6.15093 | -53.31328 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da700ace-33c9-3d39-9451-d5951a40c8b2 | -9.45016 | -48.92427 | 2026-10-10 04:46:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01da48bb-52c8-37fb-b687-7f88c6c0ff09 | -11.05665 | -49.55928 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16d297f8-bf4a-3a7b-b7ca-28c09f862da2 | -9.89382 | -44.78461 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c62e93c-8b38-34b7-8a6e-e347a14ffe7c | -13.10103 | -46.36025 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb932d1d-fed0-3ce2-a266-893155c2ca07 | -6.45135 | -55.28811 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4386b5b-9d62-315e-bc5e-53040ecbdfe6 | -13.53263 | -47.421 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce8f1fae-7bfb-3274-b52b-d159f1a565a7 | -7.0184 | -47.68587 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37b51841-4e02-3b8c-bfbd-9e97347c1cc4 | -7.4719 | -55.70646 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 540e3a68-d3b6-3768-953c-98d1698fdac7 | -9.93259 | -44.7814 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94509a91-b5d1-3ed2-8bcb-040279c61b2a | -10.82674 | -47.95422 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 043c89ae-a62b-356f-86f2-80a8ed576929 | -10.11402 | -49.55505 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67865954-16a6-3deb-95aa-13dadd6ba523 | -7.39982 | -44.76442 | 2026-10-10 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 390d2c94-bff9-34eb-a9f6-0572c3fef907 | -7.03224 | -47.66309 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bb5c3dfa-7641-3375-9bfc-76c97390946e | -12.17554 | -54.27658 | 2026-10-10 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b476dbf5-0c36-3120-9b5c-a68c7430fcb0 | -5.99254 | -55.36941 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 373d8dfa-5c26-38de-85c7-88d7ab1254f4 | -7.00513 | -47.72657 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a64a8ea8-68dc-30ad-b4ef-9e01806ebd21 | -9.25722 | -47.45217 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a16e3198-a72e-3a36-907a-6e0029162e3b | -11.18766 | -45.32461 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e16e89e-b3e5-39e3-a2a0-940639f3e572 | -9.33006 | -46.46134 | 2026-10-10 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00aae824-8077-3416-a6c7-c6383df97f21 | -11.95696 | -43.48 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dec6c20e-a3ea-3307-8019-adb5801d9810 | -12.24372 | -54.38424 | 2026-10-10 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a669b6e-00da-3e7c-a1dc-1972fcfa8053 | -12.07229 | -47.38116 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91bf56f6-9a86-341b-8578-d499a86c4352 | -13.50384 | -48.61092 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f99b4e43-3454-3d11-97dc-fa1a405f64bc | -10.28584 | -43.93656 | 2026-10-10 04:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f9b5565-8264-3dfc-9bc9-9859c3addde8 | -13.10942 | -46.35312 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e716f9f5-f36f-326e-8c2b-41903346316f | -6.15125 | -53.31019 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 069085a1-3dde-32ed-83a4-474bfa14981d | -11.90213 | -46.5601 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0f8fe86-7b42-30ed-9716-b44a506af220 | -9.90262 | -44.77668 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3fab9daa-6074-35fe-801b-3d875c7bbbd0 | -12.36336 | -46.60241 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbdc3352-0ad3-3bde-a83d-8d45bf9809fd | -11.97214 | -43.46275 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d658492-355f-3ef5-bed3-739321cef7cb | -11.59645 | -43.69937 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c610383-1d03-3837-b701-46ff46262e90 | -14.456 | -43.93166 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f62cb288-4a50-3964-b6fa-8f8666395826 | -9.28849 | -47.39471 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27ebf3a2-e3fc-374f-b6b1-7416d2aff2a5 | -13.36889 | -43.88785 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7f0bd1b-1b11-3d17-b0ed-8f46898cba68 | -5.21991 | -60.04735 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 731fe101-739c-393d-9e2e-fc2eaccf115c | -9.48041 | -47.70516 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93d6f669-828f-3de4-9a64-a9308561260d | -13.71616 | -49.12914 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b60550ba-4ac7-33e4-83be-d61a9b7b36d1 | -13.10225 | -46.35207 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dae671c9-fad0-3555-a65c-7cb9c475b384 | -9.71001 | -50.15158 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 668c9b11-bd55-3643-92ae-bc6116e81361 | -12.25059 | -44.42686 | 2026-10-10 04:46:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2f5014a-b88d-3c93-835c-939577439877 | -11.37049 | -54.02585 | 2026-10-10 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f57b164f-d070-33f5-82c2-b6834ae0b826 | -10.83058 | -47.36426 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ece44eca-38f3-33b8-81a1-37d940e92f70 | -11.84249 | -46.81161 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c1f7974-15d6-39f6-8a21-f240093a9c45 | -13.51443 | -48.609 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4d046b1-f938-3682-87ac-7dc641e10e8f | -11.38402 | -55.15829 | 2026-10-10 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e75708dd-1839-3374-b13e-f14bec7b3029 | -12.37626 | -46.61253 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52358788-d890-3595-990d-0e467197f0e8 | -11.97787 | -43.45221 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 538b4a1b-78b2-3572-86e6-5806e2a5d0fc | -12.02502 | -43.48822 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 218051c2-8b1f-3111-abff-85d557d44f9d | -6.37897 | -56.21832 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a722a196-0290-3803-b0f7-17834e158d78 | -14.45232 | -43.9271 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf94a571-844e-3737-b8dd-d77ac17da017 | -11.83621 | -43.60987 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b573bc5-d827-350b-8353-dff6a26e1150 | -13.77403 | -48.12844 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f35ef0c1-76ef-3fd7-bbcb-30bbfd850bb4 | -10.4598 | -47.84129 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa92435d-8358-3535-901f-4b4144433ded | -7.22578 | -55.14552 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c747b4de-e876-390f-b8bd-346409d1e1dc | -11.38479 | -55.15405 | 2026-10-10 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aedd54b-1d18-3dd5-821b-991da6e49eb2 | -8.96138 | -47.38033 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1721638-f1cb-3750-8abb-afa2902f5c15 | -8.65132 | -54.53988 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9403b56-1ecc-39b8-869a-4c976d7e9424 | -7.47486 | -55.70852 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd449a05-4751-3609-aec6-1b24a422dbe9 | -13.2532 | -42.25183 | 2026-10-10 04:46:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 437ac7bb-1e9c-3646-bc4d-4a6bbd3fb29d | -13.25795 | -44.01204 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0257dc53-12c8-3227-bbe1-31d7a826e416 | -7.46525 | -54.97977 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d126abee-686b-321f-bfdf-26cfd6e3cf7e | -10.93077 | -45.37491 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee9fa1dc-7035-3705-845d-99830f2f6a36 | -10.60478 | -60.47495 | 2026-10-10 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a2cd9a7-4f07-3d51-88ca-159aed95b635 | -11.75751 | -46.77579 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d60cb5c-8712-38c6-b052-927e91a391ab | -11.78918 | -46.8115 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0070dc8-675c-3f71-a42d-890383a7f16b | -13.2855 | -48.55802 | 2026-10-10 04:46:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3d6d07a-103f-3747-9df3-7019451bad55 | -6.99903 | -47.72204 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c95acb8-d5d1-349d-9163-173c62c27b48 | -13.25489 | -44.00365 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5677d288-5fcc-3c80-9ba7-30523d3ef8b0 | -11.79728 | -46.70987 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3421963e-fc12-35af-b428-0612ab728a6b | -8.6478 | -54.53704 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 803c036b-94c6-3d97-a985-43ff593c0889 | -7.03446 | -47.67059 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38199707-49ec-344c-bd2d-45f3cc246c7b | -9.88709 | -44.79941 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa631b6e-fd80-325c-aeb3-ee5fd7afbaf7 | -5.07262 | -60.22114 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a1b4cb4-5614-3494-9707-c5a160a5fed0 | -5.07933 | -60.22237 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97deb6a5-828d-3570-a8aa-85a444db8684 | -11.84596 | -46.81215 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13f0dcd9-0930-36e4-bdc7-c0040ecdeb55 | -7.50798 | -54.9988 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e3f16072-cbc2-3834-b521-f4f6c3351cee | -8.96623 | -47.44623 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 480d86c0-ae6f-34ab-af3c-ea0fc90b4bdd | -8.20219 | -45.77451 | 2026-10-10 04:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59edf8b5-5902-3484-a008-35ca4c1ddca1 | -12.05657 | -43.41309 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d38c351-a7f2-3067-a33a-087f3b44c22f | -11.75906 | -46.77509 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40ed4b73-2fff-3ba7-8c0b-b435fa4cb057 | -13.14884 | -54.35948 | 2026-10-10 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c21e258-703c-34f0-affe-0c7d26f47446 | -12.58853 | -44.13959 | 2026-10-10 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 9bc288a2-fd1b-31a0-9d69-fdd1f5bf66a8 | -8.77194 | -49.60586 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3a349b9-4d34-3dd1-ac0d-de55c6e65eaa | -7.52359 | -45.31799 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9f12d26-85a3-3a07-879c-bf6c7d0be016 | -6.15062 | -53.31394 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35c44b0e-2912-3687-95a1-5309d260d183 | -13.36014 | -43.92174 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 572f26af-9fc2-35b1-b5fa-0b64dc92e70a | -6.33778 | -54.76746 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
