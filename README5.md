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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4cc7d7f-0b69-35c9-a0aa-65f3e81aec41 | -11.82893 | -51.62113 | 2026-06-15 04:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3c7711f-4df7-34c4-9b1b-90a9067e1005 | -6.12131 | -48.48762 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fdc0b67-ceb7-3fc1-a4b5-8f46e9658d78 | -7.31539 | -48.8787 | 2026-06-15 04:55:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d69c5dd4-4ad8-34a7-80ed-0618897f2a23 | -10.40919 | -49.44012 | 2026-06-15 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af6782c0-31b4-33ce-935b-f148e306e226 | -10.15701 | -56.59547 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 066127de-213e-3c9c-b827-97d9d4595a37 | -8.96683 | -46.90575 | 2026-06-15 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 913efdb5-fc60-3cfa-a88c-7d153729ed4e | -6.12297 | -48.50225 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86364349-1f2a-332d-92cd-f1bce5fbdc9b | -11.02366 | -44.69525 | 2026-06-15 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d68e0f2c-d158-3aed-9899-17944df39ba4 | -10.16059 | -56.59609 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f3073ac-1cf3-32d5-84a4-a2b78cae395d | -10.77033 | -54.10628 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3665d8dc-beee-37c3-9254-ddf9d5e38f6b | -8.06707 | -47.18223 | 2026-06-15 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1569b0d8-ea8c-3b29-bd9b-be2eafad6b40 | -6.8995 | -51.16244 | 2026-06-15 04:55:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c99ebcb9-0acb-3ba4-a98e-df2bf31f309e | -10.87419 | -54.09474 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7659be41-c04c-3b14-9860-5a3ddc76843d | -7.31985 | -48.87465 | 2026-06-15 04:55:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ce2e039-bc4e-308d-87f3-818c30d79eb3 | -13.50464 | -47.84824 | 2026-06-15 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d200bbbe-8390-3409-8011-ddcd3d49230e | -9.26753 | -50.65667 | 2026-06-15 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6fd9e94-9570-3132-8451-832bc18637d5 | -11.2691 | -53.96097 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f03e6d10-2938-3796-982b-031a9b69aa54 | -7.92104 | -48.25076 | 2026-06-15 04:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcfe5ab4-827f-317f-98e9-f7e7855a83c6 | -7.32363 | -48.87521 | 2026-06-15 04:55:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1700af29-acb1-38d5-a543-8012e36048e0 | -10.15562 | -56.60379 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4085cd02-11a2-38d8-89c0-b6410a8b395a | -9.77748 | -48.97065 | 2026-06-15 04:55:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9ca2679-dd71-3f7a-9c1e-52c3c38f95ca | -8.96655 | -46.9075 | 2026-06-15 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07d4859b-8d29-3477-b92b-7e3b6fdc6c5f | -6.16667 | -48.49133 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10320b5d-0b6c-35b5-855e-df5a2cb67ddc | -10.15273 | -56.59901 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5dc784af-07dc-39c5-974e-2395cbad9541 | -11.82258 | -51.61624 | 2026-06-15 04:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7ccf532-3c26-3f31-bec4-35507387e9fe | -10.58781 | -48.37788 | 2026-06-15 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af592d67-0e0b-3de7-a9fc-bccc2d0d901e | -12.71227 | -54.20107 | 2026-06-15 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b29a3204-9503-3f8c-848b-5be93756791d | -7.31607 | -48.87409 | 2026-06-15 04:55:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a9483e2-83c8-3747-9383-3b5c9c2800c1 | -13.20237 | -53.26287 | 2026-06-15 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd082804-cd28-386a-8092-25439eac37a8 | -12.9088 | -54.2257 | 2026-06-15 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5ac2fcf-ba7b-3181-bdaf-7925b03cacb9 | -14.37076 | -45.54148 | 2026-06-15 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5ce138e-be58-39dc-8f5a-cc7d876ab59c | -12.90549 | -54.22515 | 2026-06-15 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adefafaa-1f3c-3033-8f15-d47b65e0a0ba | -14.0462 | -47.04912 | 2026-06-15 04:57:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4f16b98-ad44-3a03-be08-37e0d78b1f08 | -15.52838 | -53.4906 | 2026-06-15 04:57:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4bd7a8de-190a-3a75-9b77-747c0cbb2417 | -16.45229 | -53.65537 | 2026-06-15 04:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fcd286d-28c8-3644-a368-4f4bee24a550 | -22.81673 | -43.31628 | 2026-06-15 04:59:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7bed76f3-4e7b-328f-a8f7-898ce3c57ad1 | -22.81628 | -43.32223 | 2026-06-15 04:59:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9a606843-da55-31b3-a5c5-835d81bac430 | -10.77645 | -54.10862 | 2026-06-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c69c625e-360b-39ec-b590-3f5a24bfddf9 | -11.27077 | -53.95989 | 2026-06-15 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2a9015d-623b-309a-bb66-df587e8fb4e3 | -7.94073 | -63.45321 | 2026-06-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a84a02b7-f5b6-3f6f-a3aa-fd9b45dcd3d2 | -10.16237 | -56.60197 | 2026-06-15 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e8221ab-8054-3dc5-859e-ca48408069e9 | -10.77189 | -54.10983 | 2026-06-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6261561f-a2d1-33b2-8c17-3ee97a2922e4 | -10.77007 | -54.10769 | 2026-06-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f11f521b-682f-3381-8add-312cf199244e | -10.80352 | -54.17289 | 2026-06-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2825fda-4758-3743-a9ec-e5c6e7dcae00 | -10.77249 | -54.10453 | 2026-06-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a57ea77-8649-316f-8113-8f93b2c7a362 | -11.71931 | -54.4887 | 2026-06-15 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5797155b-c149-3714-aad3-8887c16640a7 | -10.15695 | -56.60133 | 2026-06-15 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5668911-337c-3461-99e0-8cd9944f3b10 | -10.80927 | -54.17907 | 2026-06-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e322d8f6-ce3d-395b-ae7f-5dd6bca7e844 | -11.7804 | -62.68802 | 2026-06-15 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3336aee-7769-3069-a184-962e276e16a9 | -12.05781 | -58.04011 | 2026-06-15 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10289244-8d02-3979-a708-dda0363091c3 | -11.71873 | -54.49375 | 2026-06-15 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d104d80a-8dff-398b-a8a2-5e96fb4a20c5 | -13.10947 | -57.22993 | 2026-06-15 07:12:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cb7bd30a-89e8-31bd-a43e-c2e86b8572e1 | -10.15487 | -56.60002 | 2026-06-15 07:12:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7314332c-2be4-33ca-816f-745f045f8bed | -8.9641 | -46.934 | 2026-06-15 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e3080152-2dc4-3934-a1dc-6dd6d5e9d189 | -7.7845 | -48.1883 | 2026-06-15 13:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c26f6ffb-85f1-3add-888e-9c6199b49af6 | -3.623 | -43.1909 | 2026-06-15 14:00:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ae854b84-278b-397f-9ec4-6944ac587f9b | -10.1495 | -56.5915 | 2026-06-15 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 651ee717-9904-3636-b9b3-d4f2e558bbe4 | -3.623 | -43.1909 | 2026-06-15 14:20:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 70ec0568-c498-33b9-af00-f1efa42b0b78 | -10.1682 | -56.5902 | 2026-06-15 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 52bb777a-4b60-342b-8093-ea12a40418e4 | -10.1495 | -56.5915 | 2026-06-15 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 4db8c3c3-bdd1-3008-91ec-f15183e72a9b | -11.8007 | -57.0032 | 2026-06-15 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d49b1338-0713-3228-89e1-550e1f249338 | -10.1493 | -56.6115 | 2026-06-15 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 71bdc799-3543-3e9c-9916-0f2b97ba169e | -10.1682 | -56.5902 | 2026-06-15 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7d6c7cb6-a3b1-3dc6-8252-7ff95125b7de | -11.8007 | -57.0032 | 2026-06-15 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d882fd17-44be-3738-b36b-714df2619871 | -10.1495 | -56.5915 | 2026-06-15 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b77f9314-5e9c-3e8a-9cce-b87c9539a673 | -10.1495 | -56.5915 | 2026-06-15 14:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a3c42e1f-996c-3d18-8544-73d2f8021d75 | -11.7172 | -54.4835 | 2026-06-15 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 86ac6ed6-eea3-38cb-826d-ecdeb9dca140 | -10.1493 | -56.6115 | 2026-06-15 15:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 653ea34e-0033-3162-8911-42410fa58a6c | -10.1495 | -56.5915 | 2026-06-15 15:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 50b5df6c-b812-30b7-8e56-7df92afd0c05 | -11.7172 | -54.4835 | 2026-06-15 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3d954424-b73a-3941-9874-3a55faa600bf | -10.1495 | -56.5915 | 2026-06-15 15:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 480c2177-9dca-38ae-b55c-05bc72229c60 | -10.1493 | -56.6115 | 2026-06-15 15:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8cc9d567-5e3f-3424-9c34-2573ac0c37ac | -6.194 | -48.5033 | 2026-06-15 15:20:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 92343bd0-8d6b-3be1-9277-0b89b4e8551b | -11.717 | -54.5039 | 2026-06-15 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e417ac3c-2ad0-3ff8-a356-9a701d337c87 | -11.7172 | -54.4835 | 2026-06-15 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4180e61c-a905-31af-9d91-fd555b5292b9 | -9.2258 | -48.5782 | 2026-06-15 15:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b29a4ade-6f90-3a73-aaf1-6dce37a83765 | -6.194 | -48.5033 | 2026-06-15 15:30:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f9593b4e-fbb4-36d2-94e6-719145bd53c3 | -11.7172 | -54.4835 | 2026-06-15 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| aa79e984-54be-32fe-8fbd-34c097808fe0 | -12.0682 | -45.2768 | 2026-06-15 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 13eb1d69-e77a-3598-b84b-e98c60b0c067 | -6.194 | -48.5033 | 2026-06-15 15:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8ab33a70-3c7b-32d0-a9e2-433644c116f4 | -10.1493 | -56.6115 | 2026-06-15 15:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| fa0b1e61-07ea-32bf-b9d3-0bfa36d6a644 | -11.717 | -54.5039 | 2026-06-15 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 3c978f94-3caa-32b6-a170-07e646f8f62e | -10.1495 | -56.5915 | 2026-06-15 15:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9d89f253-8ecb-30f0-8d5b-8594bd103cc4 | -11.7172 | -54.4835 | 2026-06-15 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 8a2ecf42-f5b1-3c98-9830-f50db533fe3e | -11.7172 | -54.4835 | 2026-06-15 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 0d027981-9c49-32aa-ab75-a54dfe28d83c | -9.2258 | -48.5782 | 2026-06-15 15:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 783dcf33-454d-3d20-87e9-8b773cbecc7a | -11.717 | -54.5039 | 2026-06-15 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 99d4bed0-2420-3ca4-9c24-b7bc2372e71e | -6.1569 | -48.4841 | 2026-06-15 15:50:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ea750a9a-8929-337c-ac00-cd8dcd9eb14e | -11.717 | -54.5039 | 2026-06-15 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2729c549-01d4-3702-94fe-099c6351a26a | -9.2258 | -48.5782 | 2026-06-15 16:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 41c2b5f9-22e0-3f4d-a1ac-05158782866e | -11.7172 | -54.4835 | 2026-06-15 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 06d209e4-cf44-34ff-9b6f-1458dd112feb | -10.1495 | -56.5915 | 2026-06-15 16:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 57594b96-4ecc-393b-8bf6-8f689137098f | -11.7172 | -54.4835 | 2026-06-15 16:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9e96cdce-43a5-3d2c-b1e0-c1f45017c662 | -11.717 | -54.5039 | 2026-06-15 16:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 82970292-d8b6-320d-a2aa-f3d0f4ef0077 | -11.7172 | -54.4835 | 2026-06-15 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e7db5852-6b71-320b-ab16-23c75717454c | -11.717 | -54.5039 | 2026-06-15 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 948052d0-efd4-3a91-92a9-d7712e8f8139 | -10.085 | -52.1775 | 2026-06-15 16:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c5798170-2356-383c-ac6c-fbce0470f61d | -9.2258 | -48.5782 | 2026-06-15 16:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 41a10062-9e74-347e-b9b1-cdefaa420e54 | -11.717 | -54.5039 | 2026-06-15 16:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f0388f20-93b3-3048-bce3-4b28c1b75e4a | -8.9641 | -46.934 | 2026-06-15 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |


[Clique aqui para ver as próximas entradas](README6.md)
