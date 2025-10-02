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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 775fb649-9e3b-3855-9414-c4b21b3a0ebb | -11.85115 | -44.98293 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc56fd6b-5a64-352f-be81-bd15a3584f5b | -6.71314 | -44.56628 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90fd82b5-6357-3fe7-8a89-b5234d9018ca | -11.59194 | -45.05804 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5022c8e8-134a-3be8-9965-d27fd234e222 | -11.81322 | -47.59446 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b76a18ac-8188-30ef-afe0-f415e5bde325 | -9.94112 | -43.71519 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8c8180c-9d95-31a3-9260-2b116bda9f3d | -10.99207 | -46.60118 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fe59d5ee-8b02-3190-8a92-f151b7d1f6f9 | -9.94415 | -43.72004 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f238ce02-0288-30d2-a5a2-bc4eb489e3e3 | -11.99328 | -46.57504 | 2025-10-02 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f41ecce6-4b19-341d-a422-02ef692f40c2 | -8.55986 | -44.66061 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2919d62a-e622-37f8-8f98-1c1ba318fdd2 | -10.84237 | -46.62487 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d20eb6e3-8105-37e2-9903-9367d25465d0 | -9.89382 | -45.94643 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e946832f-e6f2-3f80-aca3-59f156746298 | -11.83994 | -44.96106 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdb80a0f-1266-3c5c-b88d-08ffe4711f2d | -10.21153 | -48.19909 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80c6246f-5d19-38c9-8292-afa7ce90cf46 | -10.8258 | -43.66661 | 2025-10-02 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 031220c1-c1d0-3792-bd43-c5a39c24b61c | -11.82651 | -47.61834 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70e0c225-1a23-3894-a294-5b02a44a4a5f | -7.79542 | -42.50233 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 700355f7-553e-373a-8432-f5103d51bf4d | -8.65912 | -47.09411 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f4ec3a2-13c5-3c87-bdc6-318e230b8857 | -7.78882 | -42.52072 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f1562a98-4546-3e16-8693-bbaea5564090 | -7.77011 | -42.5419 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 3f485357-a327-3a11-853b-cdba3edc4d8f | -11.18961 | -47.74997 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e38930a-f3c9-3433-a61d-c0ac13d8053d | -10.94131 | -44.26284 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa4dd2d1-4b7d-38c8-8f5d-4d1fc142abc4 | -6.22795 | -45.33174 | 2025-10-02 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 035418e9-df3e-3d50-8257-4e2187205c00 | -11.715 | -44.466 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f7a28ee-eab2-307a-96e4-4896177b0086 | -11.18015 | -47.25408 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3f02951-0d45-39b3-867d-497f83e8be8f | -7.78706 | -42.50599 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3585d7b7-4ab4-3f35-98fc-6d32f099ef9a | -11.82645 | -44.97919 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7be76d65-b18e-313d-a33e-a49aa3041e07 | -6.28477 | -44.06453 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8ce68f2-c9bd-302f-92e5-3db471f27b51 | -9.94009 | -43.77214 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fb6b7c31-5006-3084-b68a-1f416b99fe11 | -11.47704 | -45.00695 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8009d2d-2dcf-3a5b-b1cf-a1afdcd84d9d | -9.89719 | -45.94695 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94d097d0-22c9-38a1-bef1-fa2f2d160916 | -11.16685 | -47.27356 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 354cf36a-73d1-380f-a9e6-bfba50f7efe5 | -10.99652 | -46.5946 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4bf08ebd-ca18-376e-90ba-d2b55bd27f22 | -10.21897 | -43.03142 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6974465b-639a-3d1b-a40c-db55cf137f9e | -7.55162 | -42.64261 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 403465da-c18b-3404-aa8d-a919ac41fcb4 | -11.09661 | -47.71702 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 396f434e-9e04-3ebd-9f7c-7fb174d06370 | -11.67019 | -47.49196 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8a14aac-bb4f-3c65-8852-dcb3ec882bc0 | -11.00711 | -46.59262 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6289d6e-671a-3e8e-894f-676dd02b7530 | -8.5805 | -49.60087 | 2025-10-02 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 722825ed-66ba-3c40-8374-29f79fe5db33 | -11.35715 | -44.94086 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e21bd78-fc1d-3bba-aaaa-f2efef1f6fd8 | -11.79339 | -44.98368 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa0a564e-6cf5-3992-b689-3d360332ec2f | -11.59534 | -45.05586 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cdcc261f-9699-3a3e-83e6-062cad3a4d0f | -11.19068 | -47.18715 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eacb56a3-1b63-3379-9fcd-72e53d43f00a | -5.94885 | -46.54466 | 2025-10-02 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55ee68d4-d9cb-39c0-9be0-832cbd3b9e49 | -10.26013 | -50.32586 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 51dd84ee-ab47-35ec-a490-3eba9810c5cf | -6.72112 | -44.56001 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d65afbe6-1ae9-37ab-bbac-2c4add5bc632 | -7.72642 | -46.21223 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee523e97-279c-336c-b7bd-40bc4cbe6528 | -10.26445 | -50.32228 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e97b2012-a6b5-3541-b0cd-4295ecf36ec8 | -6.66894 | -42.80635 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9e60d0ab-4d4b-36dc-8d5c-6dc9bd096f43 | -9.94286 | -43.72864 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b3b87f29-ee11-386d-b46d-503f4122466c | -11.09198 | -47.81037 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a633407f-0be5-3fd0-a68e-818040ccfab5 | -11.82176 | -45.01121 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 6ca7ae1d-d6e5-3c83-8f3f-bbac078825ae | -6.29079 | -45.89725 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78588dd6-edef-3b3e-8d7d-c2cf0a248e47 | -10.85748 | -45.41269 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6cb3c6a-1281-385f-ad03-d901af907cdb | -7.03545 | -43.34041 | 2025-10-02 04:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 01d89388-7508-3070-8705-2930b780168c | -10.83348 | -46.638 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 46bf806b-bebf-3dd0-885b-b1a2c106c128 | -7.77735 | -42.51892 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 6a3ad94e-1b14-319d-a4d2-f06309829ca5 | -10.91239 | -44.7876 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 079c8523-ebc3-3c16-b4ee-4e92189656e9 | -11.09635 | -47.84728 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61c88f8f-29ee-3a94-9643-68eb7aa29983 | -9.93057 | -43.73557 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| dd0db7cb-5338-3cf9-a9f3-35e5ea9227cc | -5.99647 | -44.6014 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e26400de-74f5-3561-aa51-b5c470099e29 | -9.40754 | -47.57741 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe400158-e4cd-31df-83a6-a36394252ba7 | -11.79514 | -44.99607 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47b40c5e-edba-308a-b545-b7cb502b28f8 | -10.91455 | -44.31854 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3929a3da-6187-3b13-bf36-a937c1f45f79 | -9.62217 | -48.19935 | 2025-10-02 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88f0e896-abcb-3749-8a19-1f2d5fce2e3a | -11.81377 | -47.59093 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7908a97d-6228-37f5-b475-10f45e6d93e9 | -11.7698 | -46.8335 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d22fcf4-4414-383c-963e-b8778d544c41 | -8.663 | -47.09114 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f364ee04-93ec-37ce-b1d1-8caa0398a631 | -11.591 | -47.65269 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 34f14433-9ba3-36d2-9217-440c6160832f | -11.7186 | -44.46655 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b0c13e1-02be-366f-91fd-e3d8d8553cba | -11.46547 | -44.96437 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17054b80-7b76-305b-9fb3-5335830f22a5 | -8.71557 | -47.14251 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 068a3e39-db62-3ea6-9375-61d3d35a9106 | -11.1929 | -47.19474 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31b1437d-5291-34c7-9b70-5ec37b95217f | -10.64428 | -48.50959 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27556d2e-0850-3e5e-9054-c5a1c89456b7 | -8.55237 | -44.7333 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dea5dbf-9e21-34c8-9d26-ea41583b316b | -11.08753 | -47.81686 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c73d8228-22a6-390b-9a95-5e2f5bc862c2 | -11.77649 | -46.83451 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 353886cb-0ca3-34be-b0ed-6106e031e0da | -7.55095 | -42.64721 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b336de62-1d51-3e93-9a47-21e24e935134 | -9.41012 | -47.32553 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38578c9e-33b7-37be-9c7a-7136549e244b | -10.86739 | -47.81765 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20d05282-15ab-3cf8-9395-07e6cf3bd956 | -9.93502 | -43.62978 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de5380e3-e723-3712-a016-1ce29c443544 | -10.26083 | -50.32166 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1d565c86-99a9-3206-9a57-1a92baae153f | -7.16698 | -41.7017 | 2025-10-02 04:29:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0867525b-b101-3b85-b65d-27f02c755f98 | -11.12937 | -43.3792 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c5111a7-4953-3a68-bc9a-85633f75c7cd | -11.27 | -47.80299 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45c91eea-4624-3710-89e5-257904f15ba6 | -11.60947 | -45.06083 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 104eece7-65c0-3c4f-b5be-36b7510a9fe6 | -11.86933 | -45.03046 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7c7606c4-4c3d-38d3-84f5-d9674d1e1a48 | -11.15686 | -47.19289 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8c0ca7f-fc72-3e1c-97f2-363ad76de1c0 | -8.50587 | -44.70306 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e4a685-e597-363a-a593-7d1b588d35a2 | -9.84797 | -49.95852 | 2025-10-02 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 310711b8-312d-330d-9203-1c49898c9e40 | -8.65635 | -47.09008 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 321f193c-0ebd-309a-bd54-65c56f30b90b | -10.82008 | -46.61404 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 726dbae6-e85f-39ad-a938-115ca8327b75 | -11.56569 | -47.01936 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 022ffcbc-82fd-339e-ad24-4976e52b8b6a | -6.2614 | -43.88853 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5969198-7525-33b6-8756-80dc7257feec | -11.39278 | -45.04268 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f88f662-b1b8-3afc-8183-c0f6d0f8b97a | -10.34698 | -43.73378 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09e0ece6-0879-33d7-9596-1b4a2942f067 | -11.82823 | -44.99167 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 226b2cb2-0834-3153-8228-82c7c330d0ed | -11.79808 | -45.00049 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4be0b7ac-58e3-3b29-b3c6-f37cf10e9fc0 | -9.93469 | -43.75818 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d7578fbb-6276-3458-8bbf-82dfef43188a | -11.19345 | -47.19122 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3876b49-ca35-3f14-a79c-d43802244f25 | -7.04569 | -43.34625 | 2025-10-02 04:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README73.md)
