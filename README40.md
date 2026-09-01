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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36943e4a-efd1-3b2b-bede-3da11e108c3c | -10.02721 | -44.69278 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| adc3ed0f-4da9-366a-ae4d-aa23618a00e2 | -5.87235 | -57.78078 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 347621da-4a17-37f9-ab80-c985f8295e65 | -7.34303 | -55.19461 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2f7ce52-7e5b-3075-b181-e7aeefb499a6 | -7.10376 | -42.75732 | 2026-09-01 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f370cca9-394a-3968-a8b6-7c351ef14e69 | -6.95182 | -55.62655 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f5a2327-d993-3970-94fe-9232283a3455 | -6.18536 | -47.03736 | 2026-09-01 04:40:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc651c81-6dee-3122-bf55-600341a52ed1 | -10.03448 | -44.70198 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a579b31-1606-3043-81ac-122c399f3e02 | -11.32283 | -45.15931 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae8572a6-6aac-3a0c-a1e3-40220134c3d4 | -11.27879 | -50.58366 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a36dd40c-b0de-30fd-9495-a2cd36271ccd | -10.74393 | -54.02709 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00943044-ee99-350b-a9c3-f9feb8fef66e | -9.60914 | -47.76429 | 2026-09-01 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e488953-e73d-326f-832e-5cd5d64e815c | -8.71514 | -52.36892 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5d7dfaf-f958-3512-95ad-d650a5d015fa | -6.60682 | -58.59793 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9683218e-72b6-3f72-a4a1-6315c4e87d16 | -9.18663 | -59.46235 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df9849c5-192f-3a53-802a-87997729a3f9 | -7.41558 | -55.16512 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12f0efe6-4912-3235-bb78-50531312e462 | -10.34875 | -50.00452 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9fae4f25-0b41-3b5d-a6fb-f034ba2af1e4 | -8.78937 | -62.48947 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a7f7b13-5767-3465-886d-8e301fa6aea4 | -10.83366 | -50.71246 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 678b0ad9-fce8-39c1-9829-809084c22902 | -11.21657 | -53.98301 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 715ab341-6cc0-36e1-8004-ad768b869fb5 | -7.03105 | -55.64429 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0cfcefd-d949-3b66-9487-ea526a22aa32 | -8.23053 | -54.93773 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a7a598-d724-30fd-8b00-2ed347e0236e | -10.74686 | -54.03204 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b2d27fc-72ba-3999-ac99-ca9cdf19261d | -7.53656 | -61.3887 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae9e8d41-9b21-3dc0-ace2-576d876406e4 | -8.62607 | -54.85566 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2eeeef1-9840-3741-a960-05bf058be94a | -5.95714 | -57.67816 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ebfec3f2-a182-37ce-b51b-7be5f2cf72a8 | -11.28595 | -50.58121 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 814ee356-d167-3a44-883f-957633189511 | -8.59564 | -54.72584 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 117900c5-7056-3c7f-adb8-7cb7e3262358 | -7.73199 | -55.22287 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18b40811-cb85-3ccd-9551-45bc9c684568 | -11.91269 | -44.81698 | 2026-09-01 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf8aa11f-9ea4-39a1-a21b-deb9ff2f253a | -9.461 | -45.62798 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e09ef0ae-3964-3a7d-b0cb-44a625ee9aca | -7.05132 | -52.71714 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a276280-9ab0-3f58-b406-24d9f10b3109 | -11.67128 | -47.60982 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 989796f3-06af-3c31-8e97-d4679e28b0ec | -6.96051 | -55.65279 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7cb3cee4-e70c-3915-b9ff-a11543fb8411 | -6.6606 | -59.4296 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b6e36a4-3136-39b7-860c-146c2753d10e | -10.82595 | -50.7184 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec1323db-f567-32b6-bed8-f1fabf1ed884 | -10.74908 | -54.04129 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba340b11-4452-37d7-ac1a-ade31117a9e8 | -7.6312 | -55.29371 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aadd05d-183b-36cd-b009-1d70b3fa9ec8 | -11.66648 | -47.61745 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4b3cd3cf-d09c-31c3-ad97-81498f833051 | -10.8223 | -42.37004 | 2026-09-01 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4ea6b3cf-8977-384b-b12e-a33860937423 | -6.15542 | -47.37404 | 2026-09-01 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19273177-3d02-3dbe-a8cf-d4fbfb72644a | -6.95788 | -56.43783 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c31400f-9fac-3087-b113-1594836acf2a | -12.07046 | -47.19727 | 2026-09-01 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3f3a8f-dc01-38b5-8ee2-1fe8f4d5bfff | -11.21755 | -46.09264 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2cdef86-9375-3288-a93d-1816feeb573e | -7.53742 | -61.38393 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27c9ada3-6c9f-3763-b56d-f2c88fb6eaf8 | -9.20293 | -59.55257 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef30fb90-e471-32c3-996e-08631b63dc24 | -7.65778 | -46.72794 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c79d06ca-c139-3873-8b4a-26c3a2d987b2 | -9.39645 | -60.57022 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82fca398-baaf-39c0-b16e-6ddf94a74805 | -10.03911 | -48.69172 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f642a1a-4014-36c5-990e-2e0b49ff6908 | -6.25393 | -55.43901 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d914164-4989-3c2f-96ac-4ae8c56dd079 | -10.86346 | -45.35983 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c63a6bf-9342-37f2-beee-b0884a00c66b | -5.02333 | -47.68875 | 2026-09-01 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9bccdec-c6d5-3602-a162-9bfac3f5f1ac | -3.61139 | -59.0729 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47d265a1-27dd-39a3-963c-b2fb451bc74d | -11.27552 | -50.60467 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e1c2e47-be25-3574-a0a6-11f9e76bde22 | -8.77548 | -46.45411 | 2026-09-01 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d2cb71e-c1c7-3c64-be3a-8cd79142df18 | -4.79873 | -55.9706 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f86ed7d8-2fb3-355f-9122-75cf1bb8c3be | -11.29973 | -50.57982 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 7cafb81e-e491-340e-9c09-6cea85d4d57c | -6.91733 | -55.69944 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e36bea3-b7b5-33a7-8f15-450276777b62 | -7.41155 | -49.73898 | 2026-09-01 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68b041f3-1535-3c0d-a187-aeba916d5f5d | -10.06362 | -59.40694 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78e1e052-3d22-3466-aea5-c3b5670ac154 | -9.43283 | -45.62882 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df243556-24d6-303e-b96a-aece23442a06 | -7.28603 | -49.82498 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 385d4c40-700b-3c33-80a3-080d34c81949 | -7.35348 | -60.57924 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 64b3ebac-365e-3580-bf17-d6d2984051fc | -6.88547 | -59.4103 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8282fc60-c492-3df3-ad2e-0a56d56ede6c | -5.95872 | -53.61032 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d842fa3-11a0-3789-bf67-e5b1da547e48 | -7.35056 | -60.58577 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bfe14949-35af-3d8d-9626-44e2ed640e79 | -11.66708 | -47.61338 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 85923916-70ea-3dfe-a5c4-0b4829956724 | -6.37614 | -51.758 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c68f790-d4cc-3418-a91a-fe92484a07af | -11.29257 | -50.58227 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 87ca8107-714a-3648-bb8d-08c13d482963 | -3.62196 | -60.55358 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b20cb35-ba40-3188-8f2c-440091f38836 | -7.08571 | -45.8131 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 461141ce-a715-376f-b459-c2409c4877a2 | -4.97319 | -55.85385 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3e4d2f8-e8f2-30ca-a185-c801cb8d0dfe | -12.10678 | -45.00889 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69c50648-4d07-3bd3-a0da-03d6d0b9e055 | -7.18387 | -60.68663 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 852a03b1-06ac-306c-9bb2-3308da8125e4 | -11.51794 | -46.94068 | 2026-09-01 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3dbfa8aa-7755-31fa-9a99-c501ab0017b3 | -10.35869 | -50.00609 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| cd4c72e1-fbc3-388b-99ef-0c3210a14ffb | -10.39727 | -48.23626 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c98d90fc-83e9-33e9-8719-755901783a03 | -4.96947 | -55.84865 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b12b3eb3-baaf-3ca6-b771-c17bfc780247 | -10.75352 | -54.05983 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf7ea4d-ded2-3948-89b5-d2602fce06e1 | -7.56203 | -48.36229 | 2026-09-01 04:40:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0432170-8007-3515-a1ca-88fd3a67fbe6 | -7.09917 | -42.75654 | 2026-09-01 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b63d4776-c320-34f3-9fb7-ade81f18f098 | -10.15329 | -45.68738 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1c727c-00d0-380b-b74e-3a68134d1a3b | -11.19722 | -45.03998 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2493da8a-29b5-346c-b1b9-7cf80135f445 | -6.15686 | -53.75041 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83cb67e3-761a-3fd7-95c3-529ccfd8be94 | -9.47439 | -51.5827 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dff295e-8c63-33c0-9fb5-e491ed46a6d9 | -6.10978 | -57.86558 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c9f0bcb-2e0e-3c22-b9e3-75c9d2fa6bdc | -7.29236 | -56.68691 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0803322-a964-3514-bfb2-3d644cc6f015 | -6.69678 | -55.41411 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb629fb1-50ad-3c65-8da7-5a601507e47e | -7.63256 | -55.29431 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64a42605-db22-39fd-8724-468bd63d58b3 | -10.03868 | -44.70258 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23f442bb-cdfe-3643-9b05-c440f3b49e9b | -10.75866 | -54.07423 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af1dfe4b-435c-3e69-9811-95e41385538a | -7.97403 | -52.08624 | 2026-09-01 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 373ed27a-c286-3834-b67f-1ebcabdd3db6 | -6.69389 | -55.40551 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3c93c89-3a88-3330-89b3-15a7952b1652 | -11.29152 | -50.61081 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b1920fa-d5b8-317e-a700-9ac2756b6c02 | -6.4203 | -52.20028 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8ef89fd5-c242-3a3a-b479-0c29938837fb | -11.22144 | -46.0933 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd67f254-adf7-3edd-93ad-9629d8918625 | -11.20352 | -55.10593 | 2026-09-01 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fe994d3-a509-3018-aba8-6a225a200b72 | -10.74841 | -54.06793 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8688b9ef-9193-3a75-9336-885c06e7b38a | -10.34148 | -49.96335 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32fd1999-fdab-3399-8522-d722399c2abb | -3.12041 | -61.23838 | 2026-09-01 04:40:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c580a645-298d-33d2-8f02-705971696ae6 | -10.99848 | -48.39167 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
