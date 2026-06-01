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
| 8b9f17b3-b76f-3015-83d3-117c4a1da8d7 | -10.66029 | -46.31858 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9f69a52c-8c49-392b-8619-2c20c7a55e88 | -9.70667 | -36.91746 | 2026-06-01 16:01:00 | NOAA-21 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ec926137-739c-3ab8-892c-49f305a70213 | -10.88066 | -46.64146 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4ce7b64a-340e-3499-9466-a4cefcaa0268 | -10.72245 | -46.94675 | 2026-06-01 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d0413c37-2b40-3a96-8707-e4397b4dae9e | -8.35817 | -46.69717 | 2026-06-01 16:01:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 07bddc1f-1072-37ee-a220-b9728addff32 | -13.97463 | -46.02945 | 2026-06-01 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e595ffe0-f5cc-3eb5-8933-b33fcc288198 | -9.61384 | -41.51733 | 2026-06-01 16:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 22075c31-61a3-3f02-aed0-20aa242beab6 | -10.88112 | -46.64515 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 36c0aa08-ed08-3fc9-8c48-6bc30677e83f | -10.64089 | -46.61049 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cf2a8914-1748-3beb-949d-95cf21e5dd1e | -9.79368 | -48.18024 | 2026-06-01 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb07a52d-e6fc-357e-bda8-b4ab333aad12 | -10.70578 | -49.92074 | 2026-06-01 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 749e3feb-6446-3c52-a173-1d6b8393cf52 | -11.99883 | -45.83485 | 2026-06-01 16:01:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcc34535-7c73-3b54-ba7a-f27f6620c325 | -10.58194 | -44.79237 | 2026-06-01 16:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a613a8bd-5079-3f0d-a235-79a844019e7c | -9.61525 | -41.51894 | 2026-06-01 16:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9c09b484-80ad-39b5-ac5c-abc77ce5269d | -10.97204 | -40.85253 | 2026-06-01 16:01:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 026c8a85-070f-39ff-9172-0f01afd2e182 | -8.64794 | -47.48893 | 2026-06-01 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b65b2e47-a38f-31ec-94e2-032bc857f2b8 | -9.71051 | -36.92043 | 2026-06-01 16:01:00 | NOAA-21 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bbfc029b-dfe8-3d22-966f-19e953f347d3 | -5.57441 | -42.72461 | 2026-06-01 16:03:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| d9ac3c1a-283d-303e-ba9e-611731c70e0f | -6.58107 | -51.46923 | 2026-06-01 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c666717b-1ca0-33f1-880f-3dcc4e756b7d | -7.21392 | -47.18424 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 7bdf7377-d3bd-337c-b787-a6262a2fbfe8 | -5.89554 | -44.14196 | 2026-06-01 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b97b7e57-21ad-34d9-9567-59ec8e9751e6 | -7.87409 | -47.1564 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2158d4fd-7103-3cce-a49a-f798a8e92cfa | -6.63429 | -39.74718 | 2026-06-01 16:03:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b0e81250-b577-347d-a8da-464ccb0870b5 | -6.98998 | -42.88292 | 2026-06-01 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a4e21ad6-01f3-3472-9fac-7ec8c63e9e48 | -7.21943 | -47.18351 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4edd14a6-df02-35ba-b90f-2005caa2b65c | -6.6465 | -43.92199 | 2026-06-01 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f1845003-3bf7-354a-a6e8-14a2db5ab7fc | -6.92655 | -43.67342 | 2026-06-01 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| deb0251c-249b-34db-ab4d-056850aca6a3 | -7.33311 | -46.89008 | 2026-06-01 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d745d3ea-511c-3e5c-b883-44b0526a5091 | -4.44197 | -48.26987 | 2026-06-01 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9351a50b-145a-3685-b4de-9558e2b00137 | -6.93085 | -43.67278 | 2026-06-01 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 846a49b2-0e42-3f36-98f1-c2887f54dab7 | -5.5298 | -44.41624 | 2026-06-01 16:03:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 315253a9-c403-34e5-87aa-138effdc5352 | -5.5207 | -37.48484 | 2026-06-01 16:03:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8d123d59-5311-3fef-b261-102f18667e72 | -6.64152 | -43.91826 | 2026-06-01 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 298dda39-b9ad-32ad-887d-b9241fc3dcba | -6.64212 | -43.92252 | 2026-06-01 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a3ef75f0-7699-38b9-814c-e209e11c8003 | -7.12732 | -47.4631 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 108154de-c781-38f8-93b0-73ae12c97871 | -6.09719 | -44.32603 | 2026-06-01 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e955af10-2b3e-3b77-8f7c-3674470f1b2e | -6.63772 | -39.74663 | 2026-06-01 16:03:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0ed525e8-39d8-3159-84e4-e2a43a7e5cc3 | -7.31172 | -46.99392 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a36ca289-f1fd-35ac-90d3-1f4ed404bf0d | -5.57522 | -42.72208 | 2026-06-01 16:03:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 1c7614ab-240c-312a-bb64-5b40ddb1a5f5 | -7.36191 | -41.03997 | 2026-06-01 16:03:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8440eee8-b89e-3de0-ae37-a9a50d02a5d4 | -5.60709 | -40.84069 | 2026-06-01 16:03:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9275e49c-12e9-392d-a105-761cc91001f6 | -6.98945 | -42.87928 | 2026-06-01 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cbdfe15a-540a-31ac-b552-0da24bb798ae | -6.53662 | -35.53749 | 2026-06-01 16:03:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9a260986-a25d-35e8-a227-bf15fbf334c8 | -6.07552 | -45.61619 | 2026-06-01 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8b7ee3a4-aa09-3bc2-a369-f69670eaa477 | -7.95402 | -46.83268 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 90191135-bf7b-3ef2-ac43-87edda614b82 | -6.99322 | -42.87896 | 2026-06-01 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 0e5aa5d7-b134-3619-a18b-b9118a67caae | -6.6459 | -43.9177 | 2026-06-01 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2baf54c6-01a2-3039-8231-f0ac63adce91 | -7.13942 | -47.42583 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b96a3c3d-7182-3968-ba3f-105537e68526 | -5.33582 | -42.68196 | 2026-06-01 16:03:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7a21a396-ad51-3889-a769-e6426daee7aa | -6.92909 | -43.23587 | 2026-06-01 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 639c1656-7978-3b99-abf9-0a428853734a | -6.07478 | -45.61076 | 2026-06-01 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d8665db3-50c8-3c72-b1a9-c3cd737a3967 | -7.1268 | -47.4592 | 2026-06-01 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| cca2a6a0-d848-30ad-b9b8-665eed236764 | -6.75095 | -42.69079 | 2026-06-01 16:03:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ba343b2-1c71-3669-8239-03d139ac4005 | -6.99355 | -42.87876 | 2026-06-01 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 9e4ce033-4ebf-3947-a00d-a9d1aacdd0ff | -5.33665 | -42.68383 | 2026-06-01 16:03:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6ac0cf64-27e2-3143-b759-bf72d8e94be2 | -6.07653 | -45.61242 | 2026-06-01 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1e408eb2-7657-3664-bf22-3987f5d24031 | -5.10301 | -46.94693 | 2026-06-01 16:03:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e41a5bcd-6294-3598-8b79-a5cb69d2cb5d | -5.1029 | -46.9458 | 2026-06-01 16:03:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67e18bdb-d050-3de6-8601-f014e397a880 | -14.7647 | -52.687 | 2026-06-01 16:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 034d58d6-4caa-3278-8c0e-3f2b0f29a118 | -7.4975 | -55.0055 | 2026-06-01 17:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c95063fa-cb43-3bd8-9186-6667eaade7d7 | -7.5161 | -55.0044 | 2026-06-01 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 86c161f4-b977-394f-8989-95a95dafb58d | -7.4975 | -55.0055 | 2026-06-01 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8eb4c4c4-14bc-35c9-8ffa-b01542540af5 | -13.9941 | -53.8731 | 2026-06-01 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b3fc25ab-f15f-3e97-9b7f-ba014ca78705 | -12.556 | -57.1798 | 2026-06-01 18:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 3e2eeeeb-cbbd-3441-85e2-9cf3f1b324ac | -12.556 | -57.1798 | 2026-06-01 18:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 13fe589b-be2b-3e8c-9bdb-89dab86b1195 | -12.7272 | -54.1988 | 2026-06-01 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f185ab8d-c39f-3119-98a8-76442d5003ea | -11.5836 | -54.5777 | 2026-06-01 18:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7acd7f31-96bd-3962-8e1c-db1fb1cd7682 | -11.3224 | -51.4049 | 2026-06-01 18:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c8453183-eacb-33ac-9ead-0b2ff9064147 | -12.556 | -57.1798 | 2026-06-01 18:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ed6dd6eb-a360-3d90-9637-1d8536ccee5f | -11.5647 | -54.5794 | 2026-06-01 18:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a01ad60f-0301-36ee-9ffb-f5f61920fdb5 | -12.556 | -57.1798 | 2026-06-01 18:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 69b1a2e7-aa07-3b9e-a26d-39349df507ad | -13.9749 | -53.8753 | 2026-06-01 18:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 2f9c7cc6-485e-3cf5-a102-17cd14c764c4 | -12.537 | -57.1814 | 2026-06-01 18:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f4058bf9-ef7c-323d-bd8e-38432d065bd0 | -12.307 | -57.4008 | 2026-06-01 18:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e4bb4d21-09e3-3993-b525-bf870c658021 | -11.5647 | -54.5794 | 2026-06-01 18:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c60dfe7a-6689-3e6e-aee1-116202d22c69 | -12.556 | -57.1798 | 2026-06-01 18:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |


