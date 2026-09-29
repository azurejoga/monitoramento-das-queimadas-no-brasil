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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e6361e6-da6c-3d46-97f4-e13a9e09c0a1 | -12.77471 | -52.81212 | 2026-09-29 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fe7ba41-d38e-33c2-ad46-e6b9292d5d68 | -7.67198 | -44.89163 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb6be8b6-9d04-3152-8063-c43884cbac3f | -10.43156 | -49.37561 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bb0677c-b311-394d-a302-bef7d4f731a1 | -12.02416 | -50.94466 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ca2cd3e-b290-3bea-8d23-433cd8f1ff70 | -9.63001 | -46.54167 | 2026-09-29 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba5a1e6d-b3cf-372a-b5fc-051ff4a902fc | -12.0057 | -50.99599 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9e914d8-30d4-301a-b76a-cd7c8576f70b | -11.6428 | -43.50292 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86db6fe5-ab71-35be-baaa-08ff3fb24779 | -9.96355 | -50.16613 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36e323ca-b325-33b5-9c28-7d28d7870463 | -14.43129 | -42.3082 | 2026-09-29 04:51:00 | NPP-375D | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e8b346b9-2d49-3fe0-9a19-57e72ab8388d | -6.3146 | -52.61862 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6fcb3ad-4896-3189-81fe-41ad143a0478 | -12.01689 | -50.9688 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84ecb0c9-e54d-3601-9b5e-94f13d763bca | -6.67431 | -55.11243 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ca690e8-d072-3dfc-ac0c-6cdcca8b7024 | -12.71669 | -46.98446 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d05696c7-a28e-3508-a9c9-db3d56ccdcb7 | -5.72184 | -53.45957 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce53c9d0-b71b-3f67-bf17-0ef48ebcdf02 | -11.52966 | -47.16372 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca664736-f8cc-3b59-acd8-271d178343a0 | -9.16763 | -61.40498 | 2026-09-29 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be41bcb9-33f3-3508-a944-836769f46762 | -6.14366 | -51.7358 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 009301ed-6d1b-3be0-9bb2-7b9359843963 | -11.73211 | -49.12539 | 2026-09-29 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9cecc11-2e1c-3807-a4c9-230957a62f0a | -12.79989 | -54.00639 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78946ed2-4350-34f0-97c9-c1fcb0df902f | -12.04166 | -46.49792 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73c22655-816a-33a8-a219-36e01781ebe4 | -12.04697 | -50.93026 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b7b5b21-5897-3781-a46f-dd5ca8065acd | -9.12988 | -49.96397 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb69463-6df3-37ca-b135-d4049a683e4e | -11.17483 | -44.79752 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| da5b538b-17d8-3511-b1e4-86ff821293ba | -11.40215 | -43.42048 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5667172d-23ae-3771-bf83-2b556e23bc2a | -12.7855 | -54.02554 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bbeaa33-2704-34f3-9553-01d4b3e317db | -11.02116 | -54.14506 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 327916b4-8dc4-3203-9f1c-8079963951e5 | -6.51459 | -54.96061 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb65836e-1f5e-369e-9495-f6d1f0dc1eff | -11.39888 | -47.44722 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92d8f383-bd8b-3176-a8d6-8fa266fb2819 | -9.82656 | -54.66444 | 2026-09-29 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70fcd2d3-4804-3799-bf29-958f998da61e | -9.16191 | -61.40665 | 2026-09-29 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff48217d-edef-3e57-959e-2d36c6301dbd | -11.40357 | -43.4457 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cccc56e0-7c00-3774-b8e9-bd9ba9f52162 | -14.48778 | -43.26322 | 2026-09-29 04:51:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ea207df-b783-3947-ba65-32d91f5b109e | -11.18828 | -45.13502 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22e1f260-3f8d-3f2a-b724-13fee2f7ab18 | -11.86433 | -47.08187 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca724a88-0dc0-39d7-b60a-926a84b67c89 | -7.54142 | -47.12205 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b034fa11-4ccd-3d17-bde7-c9f9563206df | -10.80045 | -48.74463 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cf332f6-5e8e-3eaa-8b8c-44ea88490324 | -11.5032 | -47.39677 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57cc5693-675b-33bd-a515-ccd693d98dc2 | -11.42951 | -43.46407 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2478173d-2156-344f-8c35-ec45e8ddd32a | -13.08779 | -47.44351 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f018ba3-b0e0-3f3d-8ace-55385565ab73 | -14.48849 | -43.25762 | 2026-09-29 04:51:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb3648aa-5afa-393e-bcc9-bd20154707cb | -12.68467 | -45.013 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc8da91c-1c12-3452-83f4-48477c4681c1 | -11.20021 | -44.79982 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04124eec-9ab4-303c-b055-617119ccf35e | -12.7597 | -52.81732 | 2026-09-29 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 549cd2b8-76b2-3750-ac8c-5df8e5b4eccf | -7.27881 | -44.30433 | 2026-09-29 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 116005cd-8dab-324d-98f7-68d6f6e58fd3 | -12.03472 | -50.94276 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58203a1f-7f64-3a5e-8c02-5015d92f77f1 | -10.7925 | -48.75084 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89500839-bd02-3c2a-8ebd-527242a9f4cf | -11.8353 | -45.01735 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c39c86a9-448d-30fb-813e-fb4f3ee341be | -14.08954 | -46.30547 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 265cfdd4-0e06-3642-b4a2-f3de26dbe4ba | -6.15288 | -52.90264 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2359d706-b64b-3194-acf7-eb6419eaa260 | -11.4401 | -43.45562 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b705e0b5-285e-3441-942b-56d8700ddb73 | -12.05613 | -46.4932 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4d00db9-391f-3b8e-9702-d23a65e57cc2 | -12.75153 | -54.05014 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a21780e-d4ed-39e4-85e6-809b599a967d | -12.59717 | -47.28258 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c086f700-f8d5-3f87-80e2-b7ff30867ae5 | -13.19043 | -48.53433 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79a7c625-c4bd-38fc-8a61-a2041c7f09de | -13.73981 | -48.97745 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef1512d5-f687-33ae-abe0-c5bffaae8f7e | -6.90729 | -47.00686 | 2026-09-29 04:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e033070-a59e-3236-b4fc-5d9812aca518 | -9.82768 | -48.20366 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 838a45ad-c756-32ea-a5e9-b5a4cc46c7bc | -12.44644 | -48.21709 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6b29761-f87e-385b-b943-015cd17ece17 | -11.18362 | -44.82666 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1faa25a-bae1-3623-b272-17ca0d170c10 | -11.17427 | -44.80149 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2d38134e-600a-3368-94c5-07ede5ef1eac | -10.43325 | -49.38686 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf97b46c-fc8a-3639-a79d-7ed883e1c502 | -10.8067 | -48.72668 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b24aefa-c1f6-3d9c-a618-fc2785022ed2 | -11.14416 | -49.049 | 2026-09-29 04:51:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b3a541d-0e7d-3f64-abff-65aa9d60e49f | -11.4348 | -43.45985 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd78e7aa-5759-3ff2-af1f-af17877072dc | -10.71631 | -44.43287 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aec3316-2750-34e9-a68d-8bc562c3e17c | -12.75572 | -47.29536 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5f77ddc-b912-3ea8-ba1f-10446f9d5dc6 | -13.17414 | -48.54743 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92e03a60-c2fc-39cc-bebb-cebcd1838ef4 | -11.85322 | -47.08013 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb8fed83-481b-3547-9e68-7cf0b3e2a4c3 | -10.51601 | -45.36274 | 2026-09-29 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7c9753f-5293-348b-aaf9-c99faad896db | -11.39744 | -43.43323 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d2d10ac-3927-369e-94f7-c810a3cb398a | -13.55753 | -48.94209 | 2026-09-29 04:51:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65e4085f-a7ca-3f82-a852-0da6dd39c554 | -12.03713 | -46.50206 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93e4b4fd-d697-3acb-9d37-2165fa9143a5 | -14.11175 | -46.29244 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 357b2606-4341-3aa6-8aea-71f52ec14a32 | -11.39528 | -47.44661 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61bf9129-d623-3409-9155-61338c3fdb00 | -11.44677 | -43.47635 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c18b0cdd-3e47-34e7-85fc-d9bcef4a3384 | -9.78866 | -44.81746 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24f37a7c-e931-3aa1-b02a-25eeaf123b86 | -7.6957 | -48.8633 | 2026-09-29 04:51:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 24ed86c2-d72c-38f1-8827-81036d26666e | -12.30092 | -50.24531 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 190cd896-b292-344c-b997-1bdf1f5b8ce9 | -11.93396 | -50.91541 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 561bf27a-588b-3c19-a548-29363a50a44b | -8.74121 | -47.87465 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0784fcb-9344-345e-8011-8fe0517cfef6 | -9.95801 | -50.13648 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3528546b-6f2e-3a84-87f6-db310e8e1538 | -10.01352 | -45.17422 | 2026-09-29 04:51:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16e418a6-dfe9-3326-9572-1164e0a458af | -11.45272 | -43.46725 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6985fa80-e91d-3009-b60d-c0e20cc93d37 | -12.78261 | -54.02066 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc35add0-c00f-3074-9a45-87464ded7dcc | -12.00904 | -50.99654 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fb906ed-f86b-3077-b64e-66da70ae2038 | -11.86803 | -47.08244 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0e8b29f-1851-3ca3-ab31-637961908b41 | -7.08586 | -46.71054 | 2026-09-29 04:51:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 592d33a0-c374-32c6-98f5-c6112b844240 | -11.38326 | -47.45295 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 722566e0-5330-3555-a7f4-ea58d2278cd7 | -13.71434 | -48.83148 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d681602-0156-3da1-a963-dc1093d01156 | -5.72569 | -53.46018 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49271de4-ea99-358a-8b76-f61331442424 | -13.43889 | -48.82529 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d20ce1fc-4e27-353f-b8c0-af929b9a7549 | -7.67273 | -44.88644 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c488505-2ec1-39f1-af90-305559683dc0 | -11.97942 | -50.95186 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33086d4b-d508-33a3-b12f-c7dec5978dd4 | -10.91217 | -43.85504 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0a1e4d1-61e4-3a01-9780-9a7dd781cfa8 | -11.38737 | -43.38836 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f667469-f422-3fde-89b7-eafb7d3f585d | -13.33283 | -46.8149 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6395058c-3830-3a3e-a886-b31b28e7007d | -12.79628 | -54.00574 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c7bb75c-c228-3d2f-ae99-5fb0b9ba89e9 | -7.50937 | -55.03375 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1d154d3-2046-37d1-9b44-e08c165c9df5 | -7.24234 | -45.26293 | 2026-09-29 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 093e0cb1-4443-3e1d-bb2c-e2b8bec8e465 | -11.36035 | -54.03912 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README45.md)
