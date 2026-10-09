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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6844b12b-df4b-3e05-a6ca-7d7a1d436a5f | -11.1974 | -45.314499 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3616672-8498-388b-b16e-29072cd0ce3f | -18.3869 | -43.473499 | 2026-10-09 00:28:00 | METOP-C | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8f100cf1-ff75-3f97-81b4-a7bcfd1a1dd6 | -3.526 | -54.669998 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0044e3fa-3385-3933-966d-b28113ff5a70 | -7.1782 | -52.6325 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e776b71-e4a2-3f44-b16b-bd8dd9d64e0b | -8.9693 | -47.548302 | 2026-10-09 00:28:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b5b65e2-d0ca-3eea-84f7-afcfeebf8d6e | -7.539 | -47.132801 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe3dd21-023e-3f7a-a169-1bca0b7edd3a | -11.087 | -44.058102 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c21f80c-945a-321f-b74e-0edbe4651e7b | -10.8756 | -44.8027 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d613fa1-437e-315a-8b2d-3bbec560fd2d | -15.2594 | -42.367699 | 2026-10-09 00:28:00 | METOP-C | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0ade22de-8d09-32db-87d9-b5630f8fda46 | -13.3575 | -43.883202 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b86d3857-e1bf-3a30-b24f-d77bcb011727 | -11.6424 | -43.691399 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ba66594-4831-3279-ac41-1f70e8a5cfe3 | -2.9366 | -54.178001 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1caee59b-2abe-335f-99f6-60f0d3a9ae9d | -6.0067 | -40.9855 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf6816e3-b796-37cf-b8e0-cac26933f634 | -2.984 | -54.070202 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08492af4-6fd9-3523-8253-645b2730960e | -4.39 | -41.818001 | 2026-10-09 00:28:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8e6dacc-fc45-3c01-b634-eb64136f1e0a | -9.8654 | -47.464001 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff8fcfe1-12a3-32ab-b623-395732a9d5cb | -15.1108 | -48.529202 | 2026-10-09 00:28:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b6d51e6b-e90a-32b1-ba1f-1dbde9775e5a | -5.754 | -43.2729 | 2026-10-09 00:28:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f0102e0-bb9d-3b78-9b74-70683d47cdc5 | -11.8594 | -43.558498 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c20edc7a-52fa-3ea0-8b7c-bde79b43afc4 | -11.0543 | -44.0509 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2d4edb4-93bc-3355-96f5-36ed1b3c6a1a | -12.3082 | -47.0821 | 2026-10-09 00:28:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e91b4387-74ae-3401-80b2-bc9b64b92ccd | -11.6195 | -43.726501 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c941131-ef75-3cd3-828e-b85c59fa2388 | -8.9676 | -47.540699 | 2026-10-09 00:28:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49a85af6-0df2-36c6-8ee7-dde633ae481f | -3.5552 | -54.6637 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13c5d411-cade-3342-9605-b6fd75ca0518 | -8.2949 | -45.738701 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8878e913-dc95-3bd4-a7cd-b17aa79bc86f | -5.6851 | -53.458199 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c636fdcc-af10-30e3-af38-8871e5fce781 | -3.3577 | -50.492298 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c3e4e2-ebfd-3935-a635-fad0d3d0095e | -3.0443 | -53.929298 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b86e7f51-a599-30bf-af4d-43c0928f03ee | -13.255 | -46.9995 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89af3d16-08c2-395b-8e70-96d85f61b42a | -8.9108 | -45.2295 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe73c44-bbb7-3107-90fd-2bd334fae467 | -3.0964 | -53.933899 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d07aa93-a5d7-35a7-a1e9-847fa68b65a4 | -14.441 | -43.932999 | 2026-10-09 00:28:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 12b808b8-9bd0-3f58-86a5-f988764296e6 | -12.0111 | -43.500401 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea270fd4-0396-37f2-84c5-6aac70c4d1ef | -13.4136 | -43.722 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76d07c5d-2883-3a0a-a171-2d236031b23f | -6.9955 | -47.691399 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cee142e5-5724-315e-80bb-fc537d474aa8 | -9.8556 | -47.466099 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77979a94-1e5a-3ac7-9ce5-999fc3631730 | -1.0006 | -47.6544 | 2026-10-09 00:28:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f50563-d433-30ac-9c49-2803578e6a45 | -9.0432 | -47.742802 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ccc50ac-6135-3b95-b5ae-6959efc89629 | -5.719 | -41.769199 | 2026-10-09 00:28:00 | METOP-C | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6feee709-0445-3939-a91e-06887989d376 | -16.121599 | -43.754002 | 2026-10-09 00:28:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3194eb15-b079-355a-8735-24cfb03f709d | -11.7612 | -46.7868 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c68b8281-0142-34d8-83a2-a364b37165f9 | -16.1201 | -43.746899 | 2026-10-09 00:28:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5e3e0010-0880-3999-8f30-183fff1b6d8d | -15.7835 | -44.690399 | 2026-10-09 00:28:00 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95fbf441-200f-3fc5-b9ce-26036949d281 | -17.516199 | -43.680199 | 2026-10-09 00:28:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8c3267-e17c-3ca6-9f55-8daef780b633 | -8.901 | -45.231701 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ac67a66e-f2ff-3d5d-96b0-1ef5de4b1c91 | -10.9967 | -47.470699 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c21a1818-e70c-398a-9ed2-5c3e51fe68e9 | -4.5418 | -47.044899 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d306f8c2-2738-301c-a48a-03769a38a9ad | -7.4791 | -42.8391 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b497e15b-a53e-3212-b040-067b36a51bc0 | -2.0828 | -46.5741 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6b38b74-8064-3496-8149-82e73fea717c | -3.5222 | -54.652802 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e59174-f2fa-3c2f-9c9e-02d578200dd2 | -12.0209 | -43.4981 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84c1d23b-e8a1-3ade-bc28-4e532181717a | -2.8817 | -47.854301 | 2026-10-09 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2239a631-a757-30b6-ab38-9499bb409efa | -3.0104 | -54.096802 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 624e25ae-30de-33d3-b57e-467935578a3c | -4.0818 | -44.1096 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc464d23-32ea-313f-bf8b-34dd7bccb509 | -10.7016 | -44.492298 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed2e6497-d2e8-33df-b294-c461ae1d237b | -12.0208 | -43.453098 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 547e476f-8e6f-3056-998d-5eca4c771227 | -4.5057 | -45.807598 | 2026-10-09 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec23767-c2f4-3764-bcae-51a4e010daa1 | -10.3642 | -45.138401 | 2026-10-09 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6506c802-0ea8-3c06-bc1c-c1a289ba7f71 | -10.2604 | -44.637501 | 2026-10-09 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af9528c7-d122-33c5-856d-692e6cae6410 | -9.1032 | -48.810001 | 2026-10-09 00:28:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 969211ea-0c18-3b74-a6e0-cf58131bd798 | -5.6948 | -53.4561 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d11d754-8f96-3b0d-adff-411c0ff7705a | -2.9953 | -53.892799 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d1dc4b-babc-3cfc-8660-07c437c78732 | -11.7825 | -46.7901 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f3f5808-e140-3cf3-805a-7a506772e71f | -11.4126 | -46.697102 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10479b7f-26e7-3f59-be06-21722402e4f8 | -3.1884 | -49.245399 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffaa2280-13c1-3dc7-a8d3-88bb2c5b78d7 | -14.2565 | -43.664799 | 2026-10-09 00:28:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7508a95-1748-3415-90fe-d8c1319b4674 | -4.5037 | -43.618099 | 2026-10-09 00:28:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 280e610f-5567-3190-a243-3c258c516863 | -5.9993 | -40.954399 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6f130ca-2ca1-343a-8cb1-de4f107392d5 | -4.1479 | -47.9842 | 2026-10-09 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0551c856-08b5-3d29-af33-c6888f4af62c | -3.3531 | -50.426601 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb9c967-88ef-3b6b-9d07-4b73b690e357 | -2.9784 | -54.136299 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07de8924-7140-310e-90d2-0a459fed9848 | -18.119499 | -42.460999 | 2026-10-09 00:28:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e6abe7c-26bb-3d28-a80c-fcf3546e57f5 | -8.1934 | -45.7906 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9185a0d-395d-3dd5-872e-938f00eccf3f | -6.2168 | -44.150101 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be23b5c1-d2ae-399e-b696-bafa904288a6 | -10.7401 | -48.557598 | 2026-10-09 00:28:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62fbc12c-a21d-3327-bb0e-2d323f08110e | -13.1963 | -54.368301 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a019e989-82f3-3984-bbb7-7a4f6bba36d8 | -4.2887 | -48.604801 | 2026-10-09 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 687a9bf2-2b6d-37f8-a7bc-6cb6a5621ff2 | -5.6943 | -49.090401 | 2026-10-09 00:28:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a1d5ccf-25ed-3372-947e-548f6e04e32b | -7.5373 | -47.1255 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 313268b1-28b5-392c-bb24-c1a169b296ee | -6.187 | -44.111 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 874c268d-d7f0-35ed-9ab6-7e4ae7f15545 | -3.5263 | -44.338402 | 2026-10-09 00:28:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2574265c-0ce4-36e7-be9c-b14abc1f2adf | -4.9866 | -44.9855 | 2026-10-09 00:28:00 | METOP-C | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55ecff97-7b31-3969-a183-b8d4daedc019 | -8.9636 | -45.915501 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e76bb0b-09dd-3aa8-a2e3-d48474aa21ca | -6.7185 | -55.147701 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03612fc7-bf47-3645-a1d7-9b0dd46f9df2 | -9.9033 | -44.8797 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f2a5e361-b541-3c36-8bbc-3f5c6ee712f9 | -9.7366 | -46.975201 | 2026-10-09 00:28:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97f51271-0ccc-3b59-b493-d4f981aa29b9 | -3.2093 | -54.301701 | 2026-10-09 00:28:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d03000d1-8047-3895-8d04-64569cd38b62 | -6.8866 | -43.702499 | 2026-10-09 00:28:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 738a6208-da48-3719-a280-768045692fdb | -8.7339 | -45.132099 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8be8d7d6-3c30-3481-bb86-93d98737ca2d | -6.374 | -42.530499 | 2026-10-09 00:28:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aba67372-368b-3d0e-a401-4a9078359a08 | -5.4178 | -44.6199 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1c6f22-8564-34b9-97a9-eb61a9fb9bb0 | -4.2845 | -49.086399 | 2026-10-09 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 444b0dde-9d97-31c3-a427-445038b47815 | -6.8796 | -45.9062 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 329c9146-90cc-329f-bcc5-43720cadb28a | -2.7273 | -54.110001 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ec9a5c-e902-33a9-ace1-5cb06f0145ee | -9.0172 | -44.389099 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3be0095c-2578-315f-bde8-1fa5fd17564d | -14.9957 | -44.062901 | 2026-10-09 00:28:00 | METOP-C | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 14e45fd8-c55a-34d6-9ce7-43e3a1790be8 | -3.7461 | -49.390202 | 2026-10-09 00:28:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 739a17c5-4d1c-3c7f-ad84-778f3c1567cb | -6.5786 | -43.048801 | 2026-10-09 00:28:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b55abdc8-fcae-3985-9e77-01635abccef4 | -7.133 | -41.813499 | 2026-10-09 00:28:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 545f3c98-2572-3b77-873c-c355be7137f2 | -5.3008 | -45.722099 | 2026-10-09 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README30.md)
