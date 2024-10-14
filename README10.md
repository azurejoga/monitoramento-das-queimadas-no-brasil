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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e5c0fe-7253-305d-9b93-9a12a10c1f07 | -6.6666 | -46.165901 | 2024-10-14 00:38:06 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 143ab1b1-28a1-31bd-a87b-cd39bf1c2ff4 | -6.9317 | -47.473499 | 2024-10-14 00:38:07 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e6526c3-5060-3ba2-8838-b33e4f69c364 | -6.9333 | -47.480801 | 2024-10-14 00:38:07 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f904c51d-3d21-3b7e-b8f2-afe1deef5345 | -5.8146 | -42.623199 | 2024-10-14 00:38:07 | METOP-C | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d79b0b1-3ad2-3a77-bb3a-1616ec6a6303 | -5.8166 | -42.631699 | 2024-10-14 00:38:07 | METOP-C | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb587ad2-b1bd-377c-92b9-4c9b410265d4 | -6.1723 | -44.597301 | 2024-10-14 00:38:09 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc7eaf1c-9ab6-391d-8602-0fa019ab0549 | -6.4012 | -45.951401 | 2024-10-14 00:38:10 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da2bf62b-fb94-333a-865e-0c503f0f263d | -6.4028 | -45.958302 | 2024-10-14 00:38:10 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af0f83a7-1052-3dde-abce-63d509bd6b31 | -5.8683 | -44.043098 | 2024-10-14 00:38:11 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ca36880-15bc-3982-80f1-bc13b8e449f4 | -5.7589 | -44.060398 | 2024-10-14 00:38:13 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96a22391-5b4d-31ab-b08d-f2309d41c427 | -5.7606 | -44.067799 | 2024-10-14 00:38:13 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20015008-736b-31c2-84b4-649e5d2edec7 | -5.5271 | -42.936199 | 2024-10-14 00:38:13 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 950e222d-8e08-375f-a344-871cc3356d41 | -5.529 | -42.944401 | 2024-10-14 00:38:13 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1596b74e-3736-3da0-bdd6-055e85f803be | -5.4802 | -42.780701 | 2024-10-14 00:38:13 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e320a041-3697-3a54-95b5-c8192af5832b | -5.5173 | -42.9384 | 2024-10-14 00:38:13 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66e8eb6d-3002-3aa7-89df-c293ff66faae | -5.6858 | -43.746601 | 2024-10-14 00:38:13 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3184571a-c052-3314-b521-6054396ef4a9 | -5.6875 | -43.754101 | 2024-10-14 00:38:13 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f68b63d-9dcd-33e3-a926-3e12a7d30228 | -5.5655 | -43.276299 | 2024-10-14 00:38:13 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bd59ede-249f-3832-9c5b-8a9e64c00d2f | -5.5674 | -43.284199 | 2024-10-14 00:38:13 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9423d4a8-ed47-366c-ae74-28ca74bf8560 | -5.9981 | -45.407501 | 2024-10-14 00:38:14 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03439495-f5e3-3a0a-b518-ec245f1d8bc1 | -5.1267 | -41.676601 | 2024-10-14 00:38:14 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3cead0c1-2ff1-34e8-812e-d6b0e8dc0c85 | -6.2269 | -46.452599 | 2024-10-14 00:38:15 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4ce26d2-3f93-3320-b251-07125bf418fc | -6.2285 | -46.459499 | 2024-10-14 00:38:15 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c102f07c-3d1c-34e1-b4a0-9b95c001bf97 | -5.117 | -41.678902 | 2024-10-14 00:38:15 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0dee0673-91f6-36d2-95bc-e1c4ba78f9c9 | -5.1193 | -41.688599 | 2024-10-14 00:38:15 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71684479-2166-3f15-a331-67cd2bd93fac | -5.1216 | -41.698299 | 2024-10-14 00:38:15 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5959ccf9-a36e-3084-aa74-872f7ace758c | -5.1239 | -41.708 | 2024-10-14 00:38:15 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f89f4f7-1528-3de0-a9ad-e322ec46b97b | -5.1262 | -41.717602 | 2024-10-14 00:38:15 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7cdbeba5-d2d9-368c-aa56-cf56f60627da | -5.1141 | -41.710201 | 2024-10-14 00:38:15 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 26a693c6-735e-3793-ad8c-703ad407acb9 | -5.1164 | -41.719898 | 2024-10-14 00:38:15 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e6f0ebf-c2c3-39d6-85b3-b74be89934b6 | -5.2195 | -42.4617 | 2024-10-14 00:38:16 | METOP-C | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8636f029-b6ab-3a05-98fa-b3b2f1bedfa9 | -5.2216 | -42.470501 | 2024-10-14 00:38:16 | METOP-C | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a1c7f54b-b577-3e01-82ce-27eceb6f7317 | -5.2942 | -42.7794 | 2024-10-14 00:38:16 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 14ccf8b2-0746-3a02-8724-d47a44364dd1 | -5.2962 | -42.7878 | 2024-10-14 00:38:16 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 264af907-f6d9-3b62-9c17-c08f9fd6c6b8 | -5.2899 | -43.0686 | 2024-10-14 00:38:17 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb96e1b-c64b-39a1-8ce7-8c4c1cba32aa | -5.2918 | -43.076801 | 2024-10-14 00:38:17 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0773f19-cd9b-3757-b8f2-06abfc7d6e8f | -5.8763 | -45.5508 | 2024-10-14 00:38:17 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c47afa3f-070c-35fb-b320-ef08e9980613 | -5.8779 | -45.557701 | 2024-10-14 00:38:17 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0cdbe674-6c87-3c11-b555-44268cc3ab86 | -5.5891 | -44.886002 | 2024-10-14 00:38:19 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0f7879b-b664-3683-8e62-965af5ca4f6f | -5.5908 | -44.893101 | 2024-10-14 00:38:19 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcfd3992-748b-3502-a9cd-cc17b5cedfee | -5.7844 | -46.5009 | 2024-10-14 00:38:22 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffe4e623-13a6-3ec8-bb91-a1dada6e280f | -5.3181 | -44.828899 | 2024-10-14 00:38:23 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b1091ea-48ac-39c0-a3c8-46febd74c1fd | -5.3197 | -44.835999 | 2024-10-14 00:38:23 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c12a60ff-ed48-39b9-a57e-13b04d418fc1 | -5.1406 | -44.108299 | 2024-10-14 00:38:23 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73a80535-f777-3e2b-bcbb-2e2c00db83ba | -5.1424 | -44.1157 | 2024-10-14 00:38:23 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76566db5-3b2c-3717-8cc3-fb995f871888 | -5.8132 | -47.262299 | 2024-10-14 00:38:24 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44c0126f-b887-3560-a05d-ae68bcb4db34 | -5.8148 | -47.269299 | 2024-10-14 00:38:24 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33ae862a-d0c4-3ca1-b02a-9f01f5ab2693 | -5.8164 | -47.276402 | 2024-10-14 00:38:24 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a2dbbbe-4b6a-390d-8f72-b7720b076496 | -5.6147 | -46.344101 | 2024-10-14 00:38:24 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a67c4135-b3bc-3546-b554-a81fb2f30dd8 | -5.6162 | -46.351002 | 2024-10-14 00:38:24 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c2da474-9b85-36bd-bc96-88aeb7c6539f | -5.489 | -45.84 | 2024-10-14 00:38:24 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2920942e-76a0-3e55-a6e1-3838168b109e | -5.4745 | -45.821602 | 2024-10-14 00:38:24 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e18de6d2-8b6c-385f-8b4c-c9e865dd84a7 | -5.4761 | -45.828499 | 2024-10-14 00:38:24 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 136d3178-f548-3e7e-ba59-d8c0e2af905e | -5.1987 | -44.759102 | 2024-10-14 00:38:25 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b979ecf3-753d-313d-b5b4-41fadd3eaa8e | -5.1873 | -44.754299 | 2024-10-14 00:38:25 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94f293ef-d713-3c58-a62d-a02859100a18 | -5.1889 | -44.761398 | 2024-10-14 00:38:25 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 266ab4f9-dc4e-34a7-aca9-ad214ba30009 | -5.1906 | -44.768501 | 2024-10-14 00:38:25 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2563c53-5fb5-39fb-95f6-ff4b515c6e4e | -5.407 | -45.887199 | 2024-10-14 00:38:26 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a20ffc9-5957-38ad-bbb8-e02f9a4a6c46 | -5.4978 | -46.283901 | 2024-10-14 00:38:26 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b61a00c-8693-3212-a307-ee70940c39b2 | -5.4994 | -46.290798 | 2024-10-14 00:38:26 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd6131a2-8097-35cf-a654-24d69a5b1717 | -5.4504 | -46.3018 | 2024-10-14 00:38:27 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80a5995c-2668-373d-98f5-3a2fecadebbd | -5.5607 | -46.9212 | 2024-10-14 00:38:27 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b425727-e1c4-30e4-be89-3b07f4032dfc | -5.1781 | -45.294998 | 2024-10-14 00:38:27 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 146a946c-c6a8-375b-85f1-a21d312a8a34 | -5.5332 | -46.8908 | 2024-10-14 00:38:27 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8db3d1d7-205a-3013-bfc6-7e53a037f07e | -5.5348 | -46.897701 | 2024-10-14 00:38:27 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ad723cb-54ab-3057-a256-2d41e11d049c | -5.5364 | -46.904701 | 2024-10-14 00:38:27 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1b5dfc9-e5a4-3894-aff3-b51d48bb02c5 | -5.525 | -46.899899 | 2024-10-14 00:38:28 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fd44486-14bc-3222-b034-066bb1830f6e | -5.5266 | -46.906898 | 2024-10-14 00:38:28 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a5e14a9-cf4e-36d0-9622-96c56168ff33 | -5.1662 | -45.3778 | 2024-10-14 00:38:28 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20a30cff-d978-3082-a373-3008bd5685d1 | -5.1678 | -45.384701 | 2024-10-14 00:38:28 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3af9047-49be-3468-afd1-689f9963436f | -5.1564 | -45.380001 | 2024-10-14 00:38:28 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b03796a-9192-35ed-a281-e6ae1d6faddf | -5.158 | -45.386902 | 2024-10-14 00:38:28 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 217ccdb0-ca2a-348e-bc93-d7f73ef74187 | -5.5202 | -47.1059 | 2024-10-14 00:38:28 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3e90a17-6886-3e05-b5bb-02b66f6cd0ba | -5.5218 | -47.1129 | 2024-10-14 00:38:28 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41545ce6-3e3e-37cd-8e46-e6401e10d98a | -5.5234 | -47.1199 | 2024-10-14 00:38:28 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 423c352c-4a24-307d-ab27-b81f13f6619a | -5.2199 | -46.015598 | 2024-10-14 00:38:29 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1114900-3a08-3607-9ede-1a3be3953fc9 | -5.2215 | -46.0224 | 2024-10-14 00:38:29 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a78696cb-173e-32a0-879c-73a27523208a | -5.223 | -46.029301 | 2024-10-14 00:38:29 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85a6de19-51af-3f41-9705-3029d828786c | -5.6525 | -47.917702 | 2024-10-14 00:38:29 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7798cb59-0cdf-3dda-a587-aaa6eaa76489 | -5.2868 | -46.352798 | 2024-10-14 00:38:29 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2702ca-6e08-30f2-8fb4-fcaade5e7b0f | -5.2884 | -46.3596 | 2024-10-14 00:38:29 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d734162-3a58-37d0-9604-2c389239bd91 | -5.3431 | -46.599602 | 2024-10-14 00:38:29 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e33dad91-8611-3351-a079-ddaf75b9b0da | -5.6427 | -47.919899 | 2024-10-14 00:38:29 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 130ce355-7f9f-31dd-9e69-1330e6f1993a | -5.6443 | -47.927299 | 2024-10-14 00:38:29 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0f74e5b-3b62-3347-b2c6-b62ef032e00f | -4.4252 | -42.8997 | 2024-10-14 00:38:30 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36f311dd-460c-3112-acde-43ef92ce6508 | -4.4272 | -42.908199 | 2024-10-14 00:38:30 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 311dc3d1-00ca-3ca8-a7c8-e74acf0568ee | -5.2786 | -46.361801 | 2024-10-14 00:38:30 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6955ee-1c6d-3df2-8ae7-c1e70cf722ed | -5.1435 | -45.996799 | 2024-10-14 00:38:30 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f16b6b21-3fd9-3686-a004-f8f3e31e8c89 | -5.145 | -46.0037 | 2024-10-14 00:38:30 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33c24efd-94b5-3c22-9173-ad753d2e680d | -5.1466 | -46.010502 | 2024-10-14 00:38:30 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0eceb468-5e3a-3c3a-8a42-6370435c0231 | -4.5408 | -43.57 | 2024-10-14 00:38:31 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a575e51-cbf9-3e1e-be5f-59ca8317576e | -4.5426 | -43.5779 | 2024-10-14 00:38:31 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 866bb823-1a17-3ed9-8cec-1aecd47dcd64 | -5.0673 | -45.754799 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9be161a-478f-3756-a203-9efee72f3f86 | -5.0689 | -45.7617 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5434da14-7ead-3f20-b5e7-8429af5ff324 | -5.0705 | -45.768501 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30cd465d-da8d-3002-8ee8-f489340224a3 | -5.1348 | -46.049099 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4c3c67d-27ab-3530-a765-7092685cf537 | -5.1364 | -46.055901 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 377b590e-ef09-3b88-86fc-041f94ff4094 | -5.0728 | -45.868801 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8dc4653-4d22-3d6a-885f-5f27b66c724c | -5.0614 | -45.864201 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 05fe5c81-8ab1-3261-8525-cb04b4440561 | -5.063 | -45.870998 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
