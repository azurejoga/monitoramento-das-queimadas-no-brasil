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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09134b9a-7a1c-3595-8fda-39dd5cb8da97 | -12.1474 | -50.60358 | 2026-08-25 11:34:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 779879d3-3658-3c98-aaca-2f4461317186 | -13.35314 | -48.19316 | 2026-08-25 11:34:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 73bf9bce-614c-3165-8008-7d2e44125f34 | -13.82539 | -42.1629 | 2026-08-25 11:34:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 576244b9-5eb6-3308-b720-e8a56565bc5f | -17.73845 | -42.0783 | 2026-08-25 11:34:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 590b04a0-5ea1-351f-a67e-556865e6c45d | -9.68878 | -46.06782 | 2026-08-25 11:34:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d85512f-dea8-3017-9a96-d3ab1ac8a48e | -10.85545 | -50.53669 | 2026-08-25 11:34:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d750b5e6-d757-3a61-9a18-19423ea3f681 | -10.03321 | -46.42256 | 2026-08-25 11:34:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e88b5e0e-daf3-3949-9c88-8c9b28262abe | -12.86412 | -48.50161 | 2026-08-25 11:34:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ac7aa801-69a0-3651-9878-bb16310403b3 | -7.43186 | -43.11963 | 2026-08-25 11:34:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 829d66e4-ba2e-31e0-9df2-c773c903e6c6 | -7.27547 | -45.35706 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f417896d-b5c6-3a75-98a3-35c9f1b4f1a8 | -7.28555 | -44.07034 | 2026-08-25 11:34:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 44a8eee8-561a-3491-af34-95a20222a5e5 | -6.7704 | -44.89651 | 2026-08-25 11:34:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5e97de9e-464f-32b8-a9ca-24865d024245 | -7.30137 | -45.3668 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bc4cb4a8-d5f3-3d9c-8777-c88341cfbd36 | -7.31375 | -42.97171 | 2026-08-25 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fe17a4ba-1ddc-31c6-875f-1d8080a89d21 | -13.23469 | -43.5811 | 2026-08-25 11:34:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 07eff7ff-4479-36f7-a42c-7c69d862de90 | -8.16742 | -46.6912 | 2026-08-25 11:34:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c096a65b-75be-382e-8e3e-49d181916a79 | -11.66149 | -46.57827 | 2026-08-25 11:34:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 0beed04d-8feb-3d19-826b-540dd1507d2d | -14.63745 | -41.95049 | 2026-08-25 11:34:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 9bbc1783-606d-3a7c-83af-210ebb658a43 | -8.17547 | -46.70324 | 2026-08-25 11:34:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8c2d1732-e993-315a-8c8d-d983f137e250 | -11.39263 | -45.14937 | 2026-08-25 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 51b5b97f-ee41-3216-b0db-57bc8a9595ca | -8.66056 | -47.30403 | 2026-08-25 11:34:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 13711c4f-b9f4-358f-abbb-ae85d69cbf13 | -7.27545 | -44.07794 | 2026-08-25 11:34:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e9e2cfd0-6358-332d-8615-c5ce200df985 | -7.98263 | -45.25138 | 2026-08-25 11:34:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0f6885ec-5e6e-3a84-bce6-a6f8b818f385 | -9.97283 | -48.31422 | 2026-08-25 11:34:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 66134867-e11b-3d17-9d9d-ea49fe7391a2 | -8.66873 | -47.31694 | 2026-08-25 11:34:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 201.8 |
| ece5311a-5b15-3f0f-a7f8-455ce32c30e9 | -6.83496 | -45.02441 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 423b43b4-43fb-3cf7-8e2e-0e9c06b7f401 | -11.78028 | -47.27082 | 2026-08-25 11:34:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 26ca6561-5724-374e-8e88-0202a21c8e30 | -7.44454 | -43.0939 | 2026-08-25 11:34:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 45727dd7-f196-37d3-9690-ea07ee88d826 | -8.08014 | -44.64422 | 2026-08-25 11:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b564b06e-f0d8-3ced-b3ef-fc2d9f9be8d8 | -11.43965 | -44.55599 | 2026-08-25 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6b3c84fd-aa82-3c65-abd0-bc19732edb83 | -7.15127 | -42.75178 | 2026-08-25 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e64e2bd0-2771-3e96-ad01-b7aaefab5580 | -11.98171 | -45.91161 | 2026-08-25 11:34:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 91546580-3f81-31fe-91d1-41275793b90a | -7.44201 | -43.1119 | 2026-08-25 11:34:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| ccea3523-62b8-3f1e-be70-f984697a5c56 | -8.6705 | -47.30548 | 2026-08-25 11:34:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 132b2a90-f467-3f93-99e1-a58d12312365 | -7.30276 | -45.35738 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 94c04c2f-c8ce-3410-8c09-68e26881e507 | -7.89728 | -46.38594 | 2026-08-25 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c4a984c1-4550-39f2-b209-5df81ca35cc5 | -11.28518 | -47.04583 | 2026-08-25 11:34:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2893225f-2d7f-3fe9-8bf7-01566e4ebd75 | -12.76093 | -46.44542 | 2026-08-25 11:34:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c28a8c81-1570-3057-adc8-8fb0e0b963d3 | -11.43209 | -44.54578 | 2026-08-25 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 333.4 |
| 7c3faf67-f043-307a-a1c8-454d958408ac | -7.26719 | -45.85302 | 2026-08-25 11:34:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bdd1c8e3-7b4b-316c-8e77-f5a61e982149 | -7.90039 | -46.36523 | 2026-08-25 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 91fafc31-d3c8-3d97-88c6-6249d4850b26 | -7.9222 | -48.25113 | 2026-08-25 11:34:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e7aabcf7-b8f3-3b19-8d7f-bd36575fa10d | -13.34983 | -48.21443 | 2026-08-25 11:34:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| eab5914a-7256-398d-8a52-21d2283c1590 | -7.28593 | -45.34891 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| dc157d55-f50e-3ff0-8172-26bbc614f97a | -19.5831 | -49.2253 | 2026-08-25 11:36:00 | TERRA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 82b75b1d-a357-31f4-925b-c562808ae6d3 | -19.98489 | -42.24305 | 2026-08-25 11:36:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| d0779eef-fa74-3b3c-9cd2-f43ab3b127ab | -18.90936 | -47.47789 | 2026-08-25 11:36:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 40da8bec-ebe8-3241-a0f1-0aa564dc87ce | -20.52025 | -44.72913 | 2026-08-25 11:36:00 | TERRA_M-M | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8657653e-fef6-37a4-97d9-a6657a783c98 | -20.46163 | -46.56585 | 2026-08-25 11:36:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d552a66-03ca-38c0-8832-dbc6d5902013 | -19.58484 | -49.21426 | 2026-08-25 11:36:00 | TERRA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 37635338-ff28-37ff-828f-9246cf1abed2 | -18.90181 | -47.46693 | 2026-08-25 11:36:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a605297b-301a-397b-85c4-cb8cf1d01d61 | -21.42652 | -45.44632 | 2026-08-25 11:36:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0f0066ac-14da-3b2b-88dd-b171b624b275 | -18.91078 | -47.46835 | 2026-08-25 11:36:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 791fe954-f447-3a60-8858-f4c548ff4440 | -19.41846 | -43.71903 | 2026-08-25 11:36:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 54c0a78a-721c-3c1d-9793-6c77c383abcf | -20.01017 | -47.14097 | 2026-08-25 11:36:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8406692e-6a75-320f-b997-dff0191a37d7 | -18.90038 | -47.47651 | 2026-08-25 11:36:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c599f789-61e4-398e-b84a-0965d531d530 | -21.11133 | -45.60191 | 2026-08-25 11:36:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fd852512-cdb1-3bdf-8440-28c87733448e | -21.24892 | -45.46817 | 2026-08-25 11:36:00 | TERRA_M-M | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 61463317-dc21-3742-9651-67a1dd308310 | -22.08157 | -47.0376 | 2026-08-25 11:36:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7001673b-2c85-38be-8e13-f3b00cc5c8ab | -20.10699 | -49.078 | 2026-08-25 11:36:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0960c7f5-10f1-38cb-b73b-5d3281066e94 | -22.40186 | -48.61273 | 2026-08-25 11:36:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 7b86dd73-f291-3a1c-81a7-c52e695dcca3 | -11.4298 | -44.5615 | 2026-08-25 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 781.0 |
| febdfd26-7bb5-3ccd-95c9-b789c57859ff | -7.2901 | -45.3683 | 2026-08-25 11:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 0640737c-488f-3e56-823a-4a6923212e07 | -11.4494 | -44.5353 | 2026-08-25 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 08b7a8e9-afe7-35a1-8f55-97e8f0c750db | -11.4302 | -44.5382 | 2026-08-25 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 565.9 |
| 0caefeb4-6886-3368-8aac-173f16ed1288 | -7.0057 | -59.2575 | 2026-08-25 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 178dbdca-41a9-355f-a92d-092e50910fe3 | -7.2903 | -45.3456 | 2026-08-25 11:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e9d1fbfa-5456-3724-b679-32a746437640 | -6.9872 | -59.2582 | 2026-08-25 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 6a46414c-801b-329a-9f46-65ccbccf110c | -6.6357 | -45.1752 | 2026-08-25 11:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 88fddf4a-3c2c-358e-b947-8f6cabce32ed | -11.449 | -44.5587 | 2026-08-25 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 199.7 |
| d132e2b7-9dd7-3307-99fc-42167e7a4131 | -7.2903 | -45.3456 | 2026-08-25 11:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 4590d0e6-1d59-33fe-9325-895d5daf8b64 | -7.0057 | -59.2575 | 2026-08-25 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| d94ab0ce-3fce-370f-8ba2-9a19c2fd661a | -11.449 | -44.5587 | 2026-08-25 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 232.9 |
| dbb8a62e-dc0c-3e0e-b5f8-0fd76c1d4188 | -11.4302 | -44.5382 | 2026-08-25 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 564.4 |
| 44167520-b4f9-33e7-995d-0d0c9687b3c5 | -7.2901 | -45.3683 | 2026-08-25 11:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| cd319cdd-0924-3fa2-b475-a934d20754e2 | -11.4494 | -44.5353 | 2026-08-25 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 74fd85b2-21ea-3604-98a0-e7b8411fc24c | -8.0918 | -47.527 | 2026-08-25 11:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6d3b0033-2f5f-3270-8dfe-6887eee4798a | -6.9872 | -59.2582 | 2026-08-25 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 4a50548e-417b-3cbb-9fb6-71687f2680ea | -11.4298 | -44.5615 | 2026-08-25 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 589.9 |
| f417c9e8-5c8c-3ae8-b139-c037036aaa1f | -7.0057 | -59.2575 | 2026-08-25 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 0d7b9fdc-1bc9-3b6f-abd8-a3fde4c49c0a | -6.9873 | -59.2389 | 2026-08-25 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2a660326-6789-3978-8654-b1d770b9fa48 | -13.3595 | -48.2051 | 2026-08-25 12:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 17e32f98-084f-3938-9d80-7e2a82ac9658 | -7.2903 | -45.3456 | 2026-08-25 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| e334d2c1-2054-3b4a-844b-cb9734c58b9b | -11.4494 | -44.5353 | 2026-08-25 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 92b7cb2f-6370-3540-9ade-cbcb501d4bdb | -7.2715 | -45.3473 | 2026-08-25 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 0b2efb4f-fbd2-32c1-b1e9-d968356f6f30 | -8.5775 | -54.8575 | 2026-08-25 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 7d4a4beb-a25c-3656-a384-7ba3624f6628 | -7.2713 | -45.37 | 2026-08-25 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 652103e1-754e-3791-a9f9-3aa9e56987da | -11.4298 | -44.5615 | 2026-08-25 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 712.5 |
| 9809a559-a25c-3f31-b7e3-8608a1809b62 | -7.2901 | -45.3683 | 2026-08-25 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| a7cd350d-1a3b-3358-b50c-f827de0e9336 | -11.449 | -44.5587 | 2026-08-25 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 208.8 |
| d5f62c27-60c6-3b9a-99dd-0d90169e14a4 | -11.4302 | -44.5382 | 2026-08-25 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 678.6 |
| b6909140-2a95-3018-8bd9-70033fcbde0d | -6.9872 | -59.2582 | 2026-08-25 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 192.0 |
| a5b2baca-d4ac-3af6-a739-eb210d6aaeae | -7.2713 | -45.37 | 2026-08-25 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 26fc39fa-fa42-3f48-9fa0-17ee6cae6870 | -11.449 | -44.5587 | 2026-08-25 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 35194d07-122f-3c46-a031-cc27d48d3a6a | -6.9872 | -59.2582 | 2026-08-25 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.4 |
| c0536258-aec8-349b-92aa-8c706c193353 | -7.2901 | -45.3683 | 2026-08-25 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 220f184b-b5fe-340c-8865-fbd6f3b0fa30 | -13.3595 | -48.2051 | 2026-08-25 12:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f65ba4cd-2b71-3987-aeb4-16d3afbb9c88 | -6.6226 | -58.4995 | 2026-08-25 12:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 618c40bc-5844-3513-b4e8-aca2284acb84 | -11.4302 | -44.5382 | 2026-08-25 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 607.9 |
| 469267bf-841d-3b40-bc88-29b77ca3aaa2 | -11.4494 | -44.5353 | 2026-08-25 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |


[Clique aqui para ver as próximas entradas](README72.md)
