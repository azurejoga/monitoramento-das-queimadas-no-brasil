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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b83d57f-527a-31f2-b4ab-8dd76927db54 | -1.23 | -54.106499 | 2026-09-28 00:55:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25266622-388a-35bc-afec-18d3627d5566 | -23.760799 | -51.911098 | 2026-09-28 00:55:00 | METOP-C | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 078e69b0-54a6-377d-80fc-8f3838af5471 | -2.7254 | -54.195499 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 192da62c-b145-379c-9284-e7452b9c9cb1 | -11.6927 | -44.554001 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 189397ae-f463-386f-af1b-ec731e116578 | -12.7463 | -47.293201 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d4b03a0-b3d6-35b7-9ed2-b2e7e6a091c8 | -8.3639 | -45.445702 | 2026-09-28 00:55:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee10ebc6-c6c9-3e2a-9a7f-62463577452b | -22.1045 | -46.812401 | 2026-09-28 00:55:00 | METOP-C | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 981c52c5-23a2-33dd-92b0-3508b7f8340c | -14.7999 | -45.958599 | 2026-09-28 00:55:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4012ccdb-78f1-3d19-be36-cab164601505 | -1.9318 | -52.137901 | 2026-09-28 00:55:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8de18077-9d12-36b2-b967-13f6a71c1279 | -3.9491 | -42.561699 | 2026-09-28 00:55:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d8076b2-e117-3921-8be3-9fcd34010318 | -2.6637 | -56.452202 | 2026-09-28 00:55:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad892051-294f-39b1-81c0-b360314b1400 | -11.1054 | -51.339199 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b283315-a785-3290-a466-ed8a7e1fbc88 | -11.7049 | -44.520599 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67181ce7-8250-3919-92be-f9813d11c79d | -12.3149 | -46.418701 | 2026-09-28 00:55:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3a2be2f-bc5c-3f5f-9b02-e7dacb736270 | -11.3856 | -45.3857 | 2026-09-28 00:55:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df115b17-c015-3c11-ba18-584e6203f385 | -8.6701 | -48.957802 | 2026-09-28 00:55:00 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5e043ee-fe20-3eb6-ba19-c69c3a31472d | -13.5619 | -46.354698 | 2026-09-28 00:55:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1752e4c1-1d90-3aef-b853-4f91215fcc7e | -3.3584 | -50.4631 | 2026-09-28 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c824f5-c7de-3bc5-b0e1-0df24c419d1a | -2.9942 | -54.738998 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4936f6e-c5f5-3b7f-9ec5-4aa632dd4eb8 | -3.816 | -44.0993 | 2026-09-28 00:55:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c184d8a4-f606-3a20-b22f-7297a1a0bc3a | -11.4458 | -44.926601 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08a5d37a-53a5-33c4-b462-78a71634aefe | -15.1601 | -43.581402 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 66bda741-6610-3643-9147-c4d901b9a4d4 | -10.4096 | -53.832298 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8b26698-a3c9-3670-9745-729f34007c11 | -15.4189 | -47.907501 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71102d07-7802-38f0-8e64-5d7ac977a7a0 | -13.2022 | -48.327999 | 2026-09-28 00:55:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e30c2a1-8cb4-30fd-924a-4bdba257f032 | -17.8391 | -44.393398 | 2026-09-28 00:55:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca8f46b-d005-3a51-82dc-4563fd5adca7 | -12.651 | -47.326801 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4d498f5-2daa-32ab-a048-0db55a547d5a | -1.2269 | -54.092899 | 2026-09-28 00:55:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe41c67e-271c-3f55-b97d-7a6b22de657a | -13.6893 | -48.813301 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10536a6f-9ac8-3262-80a0-20149138d40c | -10.8116 | -60.7318 | 2026-09-28 00:55:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62952f47-b6be-3ab4-a2c2-ab8c67a9b47f | -11.1403 | -50.059399 | 2026-09-28 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fef07a05-3e34-3346-b4cd-a9deb41380a0 | -3.8257 | -44.096901 | 2026-09-28 00:55:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14512fcb-1810-310b-acee-c4ca5c3ccc5d | -12.7388 | -47.304901 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff36e53b-1396-30cc-bb5c-431c75d667d8 | -7.2814 | -55.579601 | 2026-09-28 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a833842e-862f-376b-957c-aca2f74e912f | -2.8991 | -54.098999 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d3a2053-23b8-3c85-855a-b91bf915a650 | -12.7343 | -47.2864 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cdcd89f-e4a3-3feb-ab8c-5d13a215d06a | -8.3673 | -45.459599 | 2026-09-28 00:55:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed32eb7-8b24-38b7-9df8-239e0a5cfd52 | -3.5344 | -55.526299 | 2026-09-28 00:55:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cadb9ad8-3fd8-30d9-ab94-5c62b4b096b1 | -20.185699 | -48.577801 | 2026-09-28 00:55:00 | METOP-C | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a0ad70cb-5ae0-33a9-b4a1-7f5922f7fdaf | -7.8295 | -55.132198 | 2026-09-28 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08f6b56d-847f-306b-aa1e-d814759c2136 | -2.9054 | -54.1264 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0d9f3a-71bf-3809-8ae6-a14966299904 | -2.9227 | -54.201801 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf223d1b-e31a-3776-a448-455669671b01 | -12.7485 | -47.302399 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b572ab9e-ebb4-3c1d-a23d-62ab7ab86911 | -3.0689 | -58.0121 | 2026-09-28 00:55:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56b68577-0dea-3ebc-826a-5857e3d09b04 | -11.184 | -44.790298 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52f5c3df-0339-3665-af0a-cae2c7b6af93 | -15.1676 | -43.610199 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3c1755e4-e006-3604-b8b8-fab7197faacb | -3.2187 | -54.323799 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e502601-f4b1-3755-8833-8835e67c911c | -20.634001 | -45.606499 | 2026-09-28 00:55:00 | METOP-C | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa342da2-d09f-33ac-9dd1-3b2eeafd796c | -3.1425 | -54.0807 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6828d2eb-705c-34f5-8c86-b093746e965b | -21.528799 | -45.1082 | 2026-09-28 00:55:00 | METOP-C | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e2e3257-a17c-308e-8db7-e412636cae69 | 2.3851 | -51.018398 | 2026-09-28 00:55:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9de176e9-275a-303e-a494-00390157473d | -11.0113 | -54.137299 | 2026-09-28 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10b4f9d9-8919-3177-b6b5-b6e07be3c501 | -12.681 | -45.0243 | 2026-09-28 00:55:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c23817f7-9e1f-3751-9d51-972b758090df | -10.8918 | -43.685501 | 2026-09-28 00:55:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d791fd13-96c7-33b0-a1e0-0c35e3a79ecb | -10.8227 | -57.218102 | 2026-09-28 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6d6ad3-10c2-3ee9-b13d-eb02f1f0d38c | -3.2152 | -51.043701 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950cedbb-c303-3ec0-81de-1e366adb2b0b | -15.1519 | -43.629799 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 48b2cd70-8b9e-3862-989e-cc58c5b59584 | -11.2755 | -43.530899 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5188e4b2-3d9e-38b0-be83-7be02853c4fd | -2.907 | -54.133301 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7ab404f-8814-3fe0-ba1a-aa999748500d | -8.7355 | -47.978901 | 2026-09-28 00:55:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c5eb20b-21e1-3aa1-b37c-62dcfa2e7053 | -11.7085 | -44.534801 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c37ef06-6525-306f-9e43-b49a61ca9829 | -8.2397 | -45.402401 | 2026-09-28 00:55:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 267311a4-0bba-3bff-9e5c-d95aa984c47b | -10.8179 | -57.195702 | 2026-09-28 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a041b751-0c35-32d7-89b0-4ff590778b11 | -12.63 | -47.282902 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9d666ac-c3e8-356c-ad35-63e4b8956095 | -12.1484 | -50.354698 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb30afa5-02b4-33c4-83e4-df5100aac409 | -7.7092 | -54.777199 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 620c3e20-d1da-389f-988f-94358312a7ef | -11.2192 | -44.766399 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c7c3db0-b2d0-3b22-ae60-87805fd47e38 | -18.103201 | -44.370098 | 2026-09-28 00:55:00 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b04c64a-1932-3ed9-9a62-72a39f5fb2c4 | -3.2285 | -54.321602 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82fa7781-2de1-334f-b751-6f59fc71b696 | -2.6673 | -56.468102 | 2026-09-28 00:55:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2864715d-1134-3117-8e3c-eabefb9e7db4 | -3.1409 | -54.073799 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92813bc7-1f59-3321-b51b-7995aee061f5 | -20.1696 | -48.5975 | 2026-09-28 00:55:00 | METOP-C | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 51cf069e-5c07-3d7b-a2a6-43f74d101554 | -2.777 | -49.4753 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8eacdd6-c690-33d9-9c7a-d93d3adede4f | -11.1287 | -50.054401 | 2026-09-28 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5e7c076-f6e1-3d97-b4bc-e414d1c2a1e5 | -14.7973 | -45.9482 | 2026-09-28 00:55:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 653923bd-9495-3309-a738-0c75844c60ea | -9.495 | -46.387501 | 2026-09-28 00:55:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e38e58c-f5d8-3ca0-9996-866ab6caa8d8 | -2.9274 | -56.570702 | 2026-09-28 00:55:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87690542-5c2f-369e-8d5f-9905057bf816 | -9.3278 | -45.379601 | 2026-09-28 00:55:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 720aaf12-44a9-3b1b-b817-158bac2c92fd | -15.1482 | -43.615501 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1ea5a24d-e1e1-329f-8cf0-3e05bf1514f6 | -15.4208 | -47.9156 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6ea318-bb19-3355-a29f-5d3b8bb1a9c0 | -13.0802 | -47.4328 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 348076d7-73c4-32a2-80a2-7616334b53ef | -2.9113 | -54.197201 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a2711bb-7707-307f-a0ff-d27e6477f5cd | -10.7963 | -48.730999 | 2026-09-28 00:55:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c845bab-ba50-3882-a60b-f08fd9cc1901 | -9.9701 | -45.346298 | 2026-09-28 00:55:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f820e9f2-51e7-30f3-9b88-26344383c7d9 | -12.2072 | -50.386002 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33379ba7-7b38-3484-95c3-4d2d48188f77 | -11.0908 | -51.320599 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6afc8165-0cc0-3b06-a996-63e02c9b6017 | -12.6874 | -45.009102 | 2026-09-28 00:55:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 369485cd-b399-36d4-9d17-a8b97311564d | -12.6293 | -47.322498 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd54571-1399-3cb2-a031-b5b72832f4f6 | -2.9137 | -54.117401 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c451e50d-1524-3c39-a0ef-8aa24fef8008 | -8.0328 | -54.890999 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 793f4a9e-a306-3cfe-9029-b7f9f315e830 | -6.696 | -45.662701 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c65891b7-0090-30dc-b8be-387a6546b0e4 | -11.2157 | -44.752499 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b375d113-aafa-3cfc-8b17-3f58dacb0507 | -6.7048 | -45.614899 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b1c1809-917b-3601-962c-5c40c7d81897 | -11.1038 | -51.332199 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 798d2cd3-a3a6-3d79-922a-062987277fb2 | -15.1638 | -43.595798 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 39994f83-fd6c-394c-ac3a-058cf271a18c | -3.2036 | -51.0383 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faa94596-634e-3276-904e-9435d75105fd | -2.7672 | -49.477501 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea926d1-58c2-364e-b3e6-7d4f4eea7df9 | -15.411 | -47.918098 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5cede937-ab3d-3567-bf5f-37b8a2818da1 | -15.2837 | -47.6884 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f6a80197-4c4e-3dac-97c0-70965b9d7ca5 | -10.7983 | -48.739201 | 2026-09-28 00:55:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
