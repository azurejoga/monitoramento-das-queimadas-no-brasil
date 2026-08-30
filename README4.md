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
| 2d55c1f7-24bf-304d-93fd-623fd6939c11 | -6.7467 | -55.656502 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5569eaa-4d8e-3cbe-9d50-540a210ad80a | -6.6374 | -53.179901 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d72057-b392-340d-81cf-c88c92f5fb9b | -11.1918 | -55.0998 | 2026-08-30 00:32:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe75eaa9-6744-3367-8be0-d345a9562529 | -12.227 | -50.514999 | 2026-08-30 00:32:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcace4f7-791a-395d-bc64-8b4408bdd709 | -7.5692 | -55.559799 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11d2f5ac-c94b-3200-9550-907e74cb727a | -5.884 | -57.739799 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6a27686-7ea1-3327-aee7-5dc8bb2e6156 | -5.8773 | -52.0765 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccfb03c4-18b9-371b-909d-cf0c3341c396 | -6.1238 | -53.546902 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd8bbdc8-a934-3a09-b055-0d9916a62674 | -13.8565 | -54.124298 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dd3effbb-097e-3607-8964-091fe2034696 | -6.7013 | -58.935902 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fa91e64-a28e-36d7-9d87-b95baa38a805 | -10.8003 | -45.323399 | 2026-08-30 00:32:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8177c9e4-806b-3ff0-b1f2-da75c08160b0 | -8.178 | -54.923199 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83f326ca-f5c8-3fa5-b9b9-779a4b6bf21a | -7.2962 | -60.600899 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 103628de-eabf-382b-bf1b-87da8c2fc70d | -10.7423 | -50.829399 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29119b3c-1aac-361b-a8a3-09860c45f7ae | -14.2808 | -57.0205 | 2026-08-30 00:32:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7c44c3-b662-3eb9-8c89-81079618334b | -6.6357 | -53.172401 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3866a6f-2ada-374d-a1a1-f6e9f2f55953 | -12.2249 | -50.506302 | 2026-08-30 00:32:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4d6dc80-0b77-3c9b-a3c0-720a26aa088c | -11.2342 | -53.996101 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81bfd05a-46b4-370f-b4cd-10217ee10e2d | -9.166 | -58.294498 | 2026-08-30 00:32:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0eb481-fa83-351c-acb7-b8d452d85ced | -8.4979 | -55.293701 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69f455e5-435c-3f3c-8095-9257b4f4b60d | -6.8824 | -59.391602 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 795d9c20-fc29-3e08-b934-5a434ba63852 | -9.1788 | -59.603802 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 397d969a-ca39-3895-8a03-c6ab9ea19016 | -10.5645 | -59.589699 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b728179b-0e14-31b2-aff5-1c4e78021a1c | -6.7777 | -55.656799 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e850c35c-dbab-3760-b9d1-5ccb56ac920b | -6.9614 | -55.695499 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb3e7ba4-86ed-3c62-967a-44cb9d3c1b54 | -8.6127 | -54.796101 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cab6c1d-2837-3302-b7e1-0e5971599f9d | -5.8758 | -57.749599 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9388aa-3dcf-3965-8c58-300d0060e54c | -10.5765 | -59.598499 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2790b34c-6b44-3313-b3e4-ca29652ae61d | -14.3919 | -52.555099 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76178aa2-05af-35c2-b65b-d951869b96db | -10.7582 | -54.031799 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab5f6da8-c8df-3db4-8b35-b81a31e05c02 | -6.9273 | -55.6814 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a35e7ea-5d17-31f2-981d-5c8b169e08f5 | -6.7792 | -55.6637 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fee06f7c-f2c0-3dff-9c6a-8f40432ef32e | -12.9131 | -45.875801 | 2026-08-30 00:32:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a8ebcef-436c-356f-a774-013fc6683536 | -6.6772 | -58.731701 | 2026-08-30 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd80c18-42a7-34fb-b2eb-d062432de16a | -3.8107 | -52.361801 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebeee486-e392-3198-916b-09bf0e66ed21 | -8.568 | -55.285301 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e655ab61-1ef2-38d2-9a47-552f0f8c591e | -9.7168 | -60.712399 | 2026-08-30 00:32:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 680acda4-4509-335f-9b1c-5b9c2ae2220a | -6.9515 | -55.697701 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 591a97dd-ed21-3156-8aeb-6d8d2f3fadb3 | -9.6668 | -55.0896 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12e3c28a-e919-3f27-b121-787e45004dd8 | -10.7907 | -45.325901 | 2026-08-30 00:32:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d41ca262-462f-3bae-a351-6e7df5a03eb6 | -8.6204 | -54.692799 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 068981db-1343-3931-a981-30632f9e000b | -6.7746 | -55.643002 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 299a477e-20db-3a11-a8bd-d5c1ebffb753 | -16.350901 | -50.970901 | 2026-08-30 00:32:00 | METOP-B | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7a345078-f1ff-3d3b-8b3d-1bf8d12bccd5 | -14.9133 | -52.627701 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad86901f-4f03-3af3-bebb-81887a33efd9 | -6.1921 | -55.433899 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad98d6b-36a5-30e7-a80e-044c57312f16 | -5.8798 | -47.701302 | 2026-08-30 00:32:00 | METOP-B | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e723f4f-98fd-34c4-81d0-8cc5365eaa2a | -14.4033 | -52.559898 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 93c56fb3-9983-3fd1-996f-baa849a7ed8d | -9.4145 | -51.679298 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba43923d-9117-31ae-9fa8-f7e5f52af10c | -9.6495 | -58.929298 | 2026-08-30 00:32:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 884a11c2-1aae-392b-ac51-7dd9f79aae5f | -5.8618 | -57.546902 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84ae39a2-3f0e-3172-89ce-585876835bc9 | -9.6683 | -55.0966 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 677e8402-2a24-30c8-9bdb-899532fb7926 | -16.1238 | -43.037701 | 2026-08-30 00:32:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d58bd0b4-cd22-3caa-b4e6-2aeec6b50e34 | -11.7682 | -54.497398 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcc8028c-4f7e-357f-9f6b-650ad32e871a | -5.9897 | -55.7243 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53c5c87b-3273-3427-919e-60ed021bec93 | -10.742 | -50.653301 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e498d6b0-62d3-3c47-b6a2-fde00b0c2659 | -10.484 | -59.5952 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 187c9835-1908-3d0b-a746-7a14435403b5 | -6.8748 | -56.551998 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 609fec1e-c1bb-3bd7-9272-b4c93e198aeb | -13.8616 | -54.100899 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36fb5512-3f6b-39b7-86c8-04981e013837 | -10.7567 | -54.024899 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a941b351-0178-36f9-8dab-4f0a7107c64d | -7.5677 | -55.552898 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9946498-3db0-3dd4-a6ff-c59e204eaf41 | -11.4451 | -61.4646 | 2026-08-30 00:32:00 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8953bbe-e879-3731-aa4e-0dd46e67f088 | -8.6034 | -54.7547 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5265a27a-ba0e-3be4-926b-9370a5f690e3 | -8.4948 | -55.2799 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52c9a769-8a52-35c5-875f-c4b930e119a2 | -5.8694 | -57.766899 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92482cd6-3e94-373d-8ae1-e607a1056fc5 | -16.117701 | -43.0154 | 2026-08-30 00:32:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 403e0ab9-f011-305d-8cbb-58be949098dc | -8.1795 | -54.93 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 435dec3c-ec59-387d-a037-6ff41bb46eeb | -6.0781 | -57.8741 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab1fcdac-0af9-3735-bc9e-3d92219c5bfb | -7.514 | -55.267799 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a2a88aa-9d17-3a03-98a1-26da928ec303 | -5.8836 | -47.717201 | 2026-08-30 00:32:00 | METOP-B | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3058de79-da3d-3bb8-87dd-c8bede6eec40 | -11.2957 | -54.040699 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb570f10-5067-3995-bc02-1da4a0f6d9d8 | 0.1465 | -60.377899 | 2026-08-30 00:32:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 50bf9c09-de52-39a4-85dc-ba7a0c873788 | -3.9424 | -59.3167 | 2026-08-30 00:32:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b85604f-131c-38d7-83a2-1777c5da880f | -6.9304 | -55.695202 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2b74c9-89c5-3db2-bd88-d942d1b4882f | -6.1274 | -57.678501 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d645e95d-4b9a-3ea3-bd56-e6374cd18ebb | -14.7623 | -48.7197 | 2026-08-30 00:32:00 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c09cf46-dc09-374d-b774-2b7ad82c98bb | -10.7761 | -45.309299 | 2026-08-30 00:32:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9132ef8-c01e-3db8-a7f5-9ef3858d6656 | -9.8978 | -60.258701 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca45da4a-5413-3368-9071-ecda73d560c1 | -9.9326 | -60.4753 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e48f85a9-06a7-3052-8107-3c6a2aef9228 | -10.7547 | -54.062 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa90e0c3-0b15-37dc-8ef9-f01fa25d324f | -6.7648 | -55.645199 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eba1f444-59c1-3338-b63c-856cd8b8095a | -5.8675 | -52.078701 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f79b4b37-034b-35eb-a7c7-d0366b035bca | -3.6139 | -60.519901 | 2026-08-30 00:32:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1b840e-b94a-3775-afe7-6e846e06e1d8 | -9.157 | -59.500599 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acc27b57-6fd9-37ca-ab13-c999c2f12a4d | -4.0652 | -45.9217 | 2026-08-30 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca2dd56e-97c0-3550-9f40-5c59fb24c81d | -11.0281 | -57.228699 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b18da4ca-85f9-37f6-a219-147653357d8b | -10.9431 | -43.0378 | 2026-08-30 00:32:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d72f3e0-9b72-3316-9db2-0b8ce00c0917 | -14.7429 | -48.724701 | 2026-08-30 00:32:00 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e02352b6-5cab-3e2b-ba05-5d9dfd19eaf5 | -8.6286 | -54.683701 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1581abfe-3746-3abd-9162-ba12bc1975e0 | -14.3935 | -52.562199 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8aae8dd-9700-3eb8-8033-caec4220db7a | -6.8555 | -59.456501 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90c2a734-37a1-3888-89c0-7b7dd2110903 | -13.8534 | -54.110199 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8800281b-d6cf-3980-8983-25946d71c1fb | -14.4229 | -52.555199 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5775c72b-beb1-38d4-9268-027a9abca7e7 | -8.5905 | -54.743099 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5088c3a-691b-327a-8580-6ee977fb4fdd | -4.955 | -55.839699 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1adb5792-6ad0-30cd-9033-da93ae0b55c2 | -9.6095 | -55.109798 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36d760a2-ab03-37fe-9825-17ce53bc6a05 | -14.1696 | -52.8484 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1fc503-c6ce-3fb6-ac7d-bb41dca207d4 | -5.8873 | -57.755001 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e410ae7-140f-3f0c-b464-0066d61ee40e | -6.2509 | -55.4207 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3188052-48dd-3c48-ac03-3cfca6db85a0 | -7.0768 | -51.561699 | 2026-08-30 00:32:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbebe355-5930-3fe5-847c-655a122d6bf3 | -8.5046 | -55.277699 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
