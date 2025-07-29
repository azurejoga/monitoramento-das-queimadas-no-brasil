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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0322bb7-2682-3f0c-a65b-166463ec8f47 | -9.8287 | -41.79333 | 2025-07-29 12:32:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| cabbd91f-d118-39fe-b289-5b701f9b7cf3 | -7.74443 | -51.10062 | 2025-07-29 12:32:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c3e4e185-59f4-3ae4-bf31-77300c6bfd2f | -7.25038 | -43.05654 | 2025-07-29 12:32:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| b93325b1-86b4-3559-9666-686eebee3396 | -6.12377 | -43.95274 | 2025-07-29 12:32:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 2f14c4ad-6155-39f1-8eb4-77a049aa8ca6 | -7.73585 | -51.10247 | 2025-07-29 12:32:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6692c7e2-e02b-32f2-b652-564bfe118ba5 | -9.40668 | -47.4771 | 2025-07-29 12:32:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6732d6c6-dea5-3b81-b9b7-890ee4c4ebb7 | -6.94614 | -44.23159 | 2025-07-29 12:32:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 53a99642-d38a-39d7-b3f9-dcb28b222a4d | -11.58119 | -47.34237 | 2025-07-29 12:32:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3b790103-628e-37fc-af01-e2d2598a3c5a | -11.29212 | -55.13184 | 2025-07-29 12:32:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 02661286-bc4a-3c3e-bf1a-27ed3ec8e1cb | -6.95936 | -44.22774 | 2025-07-29 12:32:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3a3db8b7-ba83-3fc7-9b4f-b835069432fc | -7.7646 | -43.84439 | 2025-07-29 12:32:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fd547763-61d7-3234-b5e4-0fdff79ec702 | -14.03148 | -42.24417 | 2025-07-29 12:32:00 | TERRA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 00cadb6f-e168-3573-a2e0-08adf3de0c90 | -11.57559 | -44.846 | 2025-07-29 12:32:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| ea3acb1c-d3da-3576-9605-dd4f35a96bd4 | -8.83772 | -44.50607 | 2025-07-29 12:32:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| df378552-a5e0-3ca1-a32a-94d6975fca84 | -12.43674 | -44.73521 | 2025-07-29 12:32:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 21ec01a1-f893-337e-b931-669c3ee636f8 | -7.34276 | -48.06925 | 2025-07-29 12:32:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4bc419b8-7d50-3747-8a15-d30a83d7afc2 | -14.02713 | -42.2819 | 2025-07-29 12:32:00 | TERRA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 6b4e44d4-a3a1-371c-97b7-ef9545934f45 | -10.05175 | -46.56125 | 2025-07-29 12:32:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 97c26b24-9aa4-38b9-a1f6-bbaec25f2c6c | -12.02291 | -46.94499 | 2025-07-29 12:32:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 9b2904e2-0707-3328-8d6c-daa755c5afbf | -14.02802 | -42.27515 | 2025-07-29 12:32:00 | TERRA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 03152b45-4c41-3747-9a9a-9068e222241e | -13.06992 | -47.37301 | 2025-07-29 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 206f185b-18c8-31e0-ae7d-e679ec5c323b | -10.15785 | -51.20446 | 2025-07-29 12:32:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6f166e7a-a7a7-3384-9bcd-d7929b23e65c | -8.94434 | -46.7435 | 2025-07-29 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3ae1d168-aa67-3fe0-887f-512d6a90cfd9 | -6.94586 | -44.24154 | 2025-07-29 12:32:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 2987e2eb-96e6-3f0a-8eed-0bfaa4eb6f9a | -7.28401 | -39.6419 | 2025-07-29 12:32:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 9834d377-91c8-37c0-8673-8c3fdbe9dfdc | -11.99913 | -46.97131 | 2025-07-29 12:32:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 822fc3e1-f46c-3b59-a104-9a7246694752 | -6.80047 | -43.87288 | 2025-07-29 12:32:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 23e3f3cb-d108-334e-adf9-3ad86245e698 | -11.58268 | -47.33138 | 2025-07-29 12:32:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| afa25462-7e49-3339-88b4-b8bd0a36394c | -11.36439 | -50.65652 | 2025-07-29 12:32:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 650d545f-1d3f-38b2-9439-503c09fec7b0 | -10.45591 | -49.08047 | 2025-07-29 12:32:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 44c00fb5-7499-3abb-9bb5-75341424cabb | -6.50247 | -45.30725 | 2025-07-29 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 49b88d77-0ee3-37f0-93b0-b3873906bf5d | -7.65809 | -47.46585 | 2025-07-29 12:32:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6efbc9f2-b825-3327-b584-2bf24d9e5455 | -6.12482 | -44.78717 | 2025-07-29 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bf4a4777-3027-3dbb-a62e-4c80c3e57b42 | -11.42549 | -45.13157 | 2025-07-29 12:32:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 6d156df3-72a8-3c3b-83ca-e2aca8245dd2 | -8.63756 | -45.51407 | 2025-07-29 12:32:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 8b9ac613-68a3-310d-adb0-1ba12f625088 | -7.50556 | -50.2207 | 2025-07-29 12:32:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 0efd5153-9253-30ee-8efd-9a9e7ebbdd6c | -8.95411 | -46.74475 | 2025-07-29 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 97a81f15-8505-3e2b-8ab3-8e8cf1626235 | -6.0319 | -47.5589 | 2025-07-29 12:32:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ca34120d-25ff-3fd4-8ecd-3364831acd2a | -6.12829 | -44.43319 | 2025-07-29 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d7568b62-4f1b-34b7-87a1-ead9e86c637a | -6.8428 | -46.3906 | 2025-07-29 12:32:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 077520d1-ae3d-376a-9027-a833121c9a8b | -12.36816 | -49.96831 | 2025-07-29 12:32:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cf17e654-cf1b-3fb4-95f4-6b5a17e22fe2 | -11.74217 | -48.18255 | 2025-07-29 12:32:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9f5c645c-6dcf-39e1-aa45-7b29e01dcb95 | -6.03987 | -47.56646 | 2025-07-29 12:32:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 054fafab-ff35-3637-8a2d-3032bd547ee7 | -12.32888 | -50.05439 | 2025-07-29 12:32:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54953160-fd70-3609-b306-84ea4e413cb0 | -14.03033 | -42.25108 | 2025-07-29 12:32:00 | TERRA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 39.5 |
| d9ad8f23-0ba9-3836-acda-e4bba56f5fb3 | -6.04118 | -47.55708 | 2025-07-29 12:32:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cdaa74fb-1053-3c98-9b1e-c1e92e9c1845 | -6.12683 | -47.73599 | 2025-07-29 12:32:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3c767823-de59-36b7-a0ae-222442c33a86 | -7.29507 | -39.63623 | 2025-07-29 12:32:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 87.6 |
| b3743a62-68f6-3126-b069-7a3d11a31ac0 | -10.93071 | -45.77702 | 2025-07-29 12:32:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| de38e04e-6641-314a-9d6a-1db09860030c | -13.49527 | -45.61197 | 2025-07-29 12:32:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 74baee07-ff3a-3fc3-98d5-8d6ba173dc55 | -12.95572 | -46.91114 | 2025-07-29 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 575fc58f-b8a3-349d-b9fc-61996564b459 | -8.95262 | -46.75578 | 2025-07-29 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 05e5f112-b2b5-3b78-9d42-0dff281c3b7f | -10.52569 | -42.5426 | 2025-07-29 12:32:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 873d9d73-0edd-3cab-a59f-3171baeedc68 | -6.55898 | -44.21511 | 2025-07-29 12:32:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1b28d94a-4f7f-39c8-8152-aa6085672634 | -7.50688 | -50.2117 | 2025-07-29 12:32:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 24860e80-9335-324b-adb9-1b03a1b1c6e4 | -6.95754 | -44.23321 | 2025-07-29 12:32:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| d08c283f-3708-35e2-8f7e-1d52b235477d | -7.55201 | -44.42604 | 2025-07-29 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8dbbd006-47c2-3133-9184-5dbcbe12392d | -9.29223 | -49.48158 | 2025-07-29 12:32:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3ea9aa91-4722-3ad1-ad55-d232c21503bf | -6.52122 | -43.63388 | 2025-07-29 12:32:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7fb27da7-ec1b-3ea5-bc77-8e131f075a88 | -13.50473 | -45.62885 | 2025-07-29 12:32:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 80ac1e17-186b-3b89-a7e6-04fc7a447d83 | -11.42737 | -45.1262 | 2025-07-29 12:32:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| cf6e44f2-55f8-3b8b-9ee2-ab052f3e67a1 | -10.53136 | -42.55003 | 2025-07-29 12:32:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 588ecd97-e8da-33e0-a0ff-0c33947ea846 | -16.78504 | -44.33508 | 2025-07-29 12:34:00 | TERRA_M-T | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 49221bab-9094-3965-8f78-2d0773a2d616 | -18.45283 | -54.66395 | 2025-07-29 12:34:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b18db406-aa02-38fb-87c8-0bff53324b05 | -14.73662 | -46.30901 | 2025-07-29 12:34:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 96844384-8ab2-3117-b2ba-a69b66fc6444 | -15.97976 | -52.83872 | 2025-07-29 12:34:00 | TERRA_M-T | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 922e489a-afdb-3d8c-b7ed-4509a49d7e35 | -18.50743 | -44.64059 | 2025-07-29 12:34:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 867519ea-2a18-32cc-a9d3-16895281a92f | -14.50106 | -46.55014 | 2025-07-29 12:34:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b37a5f9e-ac58-3b7f-8e72-3c37cc06c838 | -17.96539 | -45.52034 | 2025-07-29 12:34:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0e283b63-1aef-3066-aaf6-df76c2cb4f0d | -18.44314 | -54.66231 | 2025-07-29 12:34:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d475cc43-6834-3b43-b2b0-96315c00cd71 | -14.00326 | -44.62712 | 2025-07-29 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 56efa2eb-a027-322f-9ead-b42397a4bea2 | -15.10214 | -49.12738 | 2025-07-29 12:34:00 | TERRA_M-T | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8a52f86c-b4eb-38a5-b673-87276553e8d0 | -17.95871 | -45.50655 | 2025-07-29 12:34:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 98e1eafb-8259-3f2e-94bb-9072782d113e | -17.72934 | -44.08679 | 2025-07-29 12:34:00 | TERRA_M-T | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 835f7a5c-a5be-3920-8fd4-e9acf98356fe | -18.35331 | -44.7302 | 2025-07-29 12:34:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a2f7f765-c616-3c9f-9439-cfd9425fc214 | -14.83144 | -47.23405 | 2025-07-29 12:34:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 24570fb3-c210-393d-a8eb-304a22a025b6 | -16.78746 | -44.31319 | 2025-07-29 12:34:00 | TERRA_M-T | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 73ce533f-fdc3-37ae-a9a8-aabd7962ef4f | -16.32248 | -42.30275 | 2025-07-29 12:34:00 | TERRA_M-T | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 5e495d02-2923-3455-b687-3bd9fabd5cc1 | -14.32383 | -54.15822 | 2025-07-29 12:34:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ed7deea5-7860-3a96-9c6c-4b1bbd37ddeb | -16.31895 | -42.30793 | 2025-07-29 12:34:00 | TERRA_M-T | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 9da68c0b-b108-3d8b-ab32-d40b3359daad | -17.96753 | -45.50195 | 2025-07-29 12:34:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a93b941d-2f79-317b-959e-62ec7ecebdc2 | -14.73844 | -46.29454 | 2025-07-29 12:34:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6751518e-cd1a-3585-8efd-758563615364 | -14.50279 | -46.53639 | 2025-07-29 12:34:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 1f2b1108-7d65-3fff-84bb-4ae38fda01ac | -20.86998 | -48.66238 | 2025-07-29 12:34:00 | TERRA_M-T | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ab37e5de-ff78-3552-ba8a-7813ef4474e5 | -18.58566 | -55.93987 | 2025-07-29 12:34:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d0f2c8c4-1ad5-325a-89da-87a46abfceaf | -6.9456 | -44.2342 | 2025-07-29 12:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f1bca73c-e660-3454-b013-8301e517d5ee | -13.5058 | -45.6032 | 2025-07-29 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 94af50af-06ef-3bac-a910-0419cc60873e | -6.5033 | -45.2992 | 2025-07-29 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6252d042-c9f7-38f2-8e49-06e6483f3456 | -6.9456 | -44.2342 | 2025-07-29 12:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 7402207a-3855-391e-993a-af8420e21c3c | -6.9456 | -44.2342 | 2025-07-29 13:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 29e4d482-ada2-35f3-ad7e-bc5af3b21fdf | -6.5033 | -45.2992 | 2025-07-29 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 51c207fe-a56a-3271-8cb4-92bc02d44f8d | -13.5058 | -45.6032 | 2025-07-29 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 8a77cafc-fb69-3102-ab52-ca0ff639d2ce | -7.7834 | -44.9584 | 2025-07-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 7d9eae78-031c-3359-a9eb-e4ea06316fd0 | -6.9456 | -44.2342 | 2025-07-29 13:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 73f1b5be-b425-31fe-9b4a-1ad6dfad181d | -7.6128 | -45.066 | 2025-07-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 36b47d6d-0152-373d-b82f-15c0a5c389d7 | -7.6131 | -45.0432 | 2025-07-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d35285e0-1db3-3a45-880c-19eb88c7d7eb | -7.6317 | -45.0642 | 2025-07-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 6291ff4b-1e1c-3304-b045-0cd2204242a7 | -7.6128 | -45.066 | 2025-07-29 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 241.6 |
| 2306a12e-c23e-3109-b909-3dd30ec94fa7 | -7.6317 | -45.0642 | 2025-07-29 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 9fbd7b67-be1a-3c65-9f15-05da70f6fdda | -13.5247 | -45.6231 | 2025-07-29 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |


[Clique aqui para ver as próximas entradas](README26.md)
