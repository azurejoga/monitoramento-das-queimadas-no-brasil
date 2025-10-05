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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0de85b0-4653-3af3-8d30-9c607208e194 | -11.8418 | -45.0799 | 2025-10-05 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| dd014892-3578-39ca-b05e-292fc11c8690 | -12.4669 | -45.5155 | 2025-10-05 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 351e612c-0ed7-3956-afd9-17c8bc5d1116 | -12.1461 | -50.9309 | 2025-10-05 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d2fdf4b2-72ae-3875-af4f-6d64478efcc0 | -4.4445 | -43.2397 | 2025-10-05 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3c0c2bf7-7996-3cf6-997d-4c2bf4ade361 | -6.1534 | -44.6903 | 2025-10-05 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d9adbdf9-eb7b-3268-94e9-f594f40c8836 | -6.1536 | -44.6675 | 2025-10-05 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 411.5 |
| 85258a54-50ea-3108-8adf-2f1fd0129dbf | -8.5956 | -46.2798 | 2025-10-05 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1487f538-bfd1-3ac0-be2d-c450998527dc | -14.3353 | -47.6755 | 2025-10-05 03:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c6368ca3-2502-38b9-98ca-7ee1a17909f9 | -8.5764 | -46.3041 | 2025-10-05 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 7d91d5bc-7da0-3a06-aba6-c59b8fde71e0 | -4.3197 | -48.0908 | 2025-10-05 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 923f0ffb-f120-3047-8770-ee754e2b1c03 | -5.8891 | -42.9048 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| cefe9faa-6a52-34c6-b128-8682ee052185 | -8.595 | -46.3246 | 2025-10-05 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 8b703ab7-a70f-35e9-975b-dd88b1a0215a | -18.3338 | -45.8971 | 2025-10-05 03:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e9b2d32a-46fd-3606-99e2-57ba43e21f9b | -4.6505 | -43.1805 | 2025-10-05 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 6824643a-5250-32a3-bd64-9c5da029698c | -12.1271 | -50.9332 | 2025-10-05 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3543a73c-caed-3046-8a6d-4441c7d18218 | -5.8374 | -44.4399 | 2025-10-05 03:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d0774e88-c621-3012-a022-9926595d22d4 | -14.6906 | -48.335 | 2025-10-05 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5f1e3a31-75d6-38d5-a574-646a3ea18ca7 | -10.9303 | -47.0882 | 2025-10-05 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| f4fa24b5-aa4a-32b7-bdd8-67de98f00b3a | -16.3884 | -52.1612 | 2025-10-05 03:30:00 | GOES-19 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6a450f42-dc33-317a-ab7d-104eda4c15ab | -6.1349 | -44.6689 | 2025-10-05 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| be451b43-36fe-3310-8b09-24a74d449af7 | -5.8889 | -42.9283 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| fb218ed7-f930-3c0c-9a3b-5fc3e4e97be0 | -8.5953 | -46.3022 | 2025-10-05 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 9ffe7271-d5cb-3511-a1ec-ef35f8b5b810 | -9.2973 | -46.0026 | 2025-10-05 03:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ed35c90f-d160-3718-acaf-bd0cab61844f | -5.7952 | -42.9123 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 862a6fd6-0c76-3692-a0d4-5264b8f08e29 | -10.9307 | -47.0658 | 2025-10-05 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8a473dae-0d0c-336a-8e4b-23ccc9d4808b | -5.776 | -42.9607 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| f81ea909-91f8-37c4-9a12-6f98b8b26a98 | -5.7948 | -42.9593 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 5746b833-5370-3c39-a340-03acda2b6563 | -13.1585 | -50.9359 | 2025-10-05 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d7c6ba96-b729-3954-a5eb-3650a68f4dde | -4.6504 | -43.2038 | 2025-10-05 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 25e8e496-6c9a-3acb-87dc-1dd8c2e57e66 | -13.1393 | -50.9383 | 2025-10-05 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 73367ff8-063b-3212-a135-4d8c2a8bb9ce | -6.1723 | -44.666 | 2025-10-05 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| e37dd463-b980-32c7-a27f-2c1829b0114f | -10.9494 | -47.0858 | 2025-10-05 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 334.1 |
| dd419589-ffab-3ad8-ab9e-88f2d3938faa | -6.1538 | -44.6446 | 2025-10-05 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 314e47d9-2b28-3ce0-8811-cdf6de6b1bea | -5.7764 | -42.9137 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 184.4 |
| 683b8f46-1a1d-354c-a729-7b9b79720011 | -12.1274 | -50.9118 | 2025-10-05 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| fd2586a3-38cd-3ed6-8a70-fd61118ec6dd | -6.4134 | -43.0489 | 2025-10-05 03:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 8451b3f2-ce70-3d20-855f-fdd2aceb7e9e | -10.9497 | -47.0634 | 2025-10-05 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 218.2 |
| bbb6786a-5be5-33aa-a2ce-6a7ce4afb266 | -5.7762 | -42.9372 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 457.4 |
| 7c31779f-af4f-3386-b65e-340f0e63b51c | -5.22744 | -43.70876 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce22dcf-8493-32f5-9706-487fff7bc1c6 | -7.04891 | -42.76373 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 00ecfa39-ea55-369f-97dc-388375943c51 | -6.01661 | -44.02409 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7211f667-4232-3df5-8421-538884a06eb0 | -4.44089 | -43.24031 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 746a02ed-7576-3ff4-8ccf-997de219a21d | -6.13625 | -44.63712 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02ac71d9-3434-3014-8392-4268fb63a8c8 | -7.05473 | -42.76493 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cca216b7-56ce-3308-8064-f5980c956161 | -6.55707 | -44.16749 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4199433a-9e89-3442-98c7-dd090035de87 | -5.89489 | -42.91119 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| b44af52f-8b9f-3cef-8880-11b0ec9d4485 | -6.44517 | -44.16139 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1ab5a0c-5dec-3497-8468-c979ee1c2e86 | -5.66715 | -42.74693 | 2025-10-05 03:32:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05973cf1-a5bc-3447-9b14-a3a25813f75d | -5.99525 | -44.3599 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdd2f6ff-7b8e-3278-91bc-7e72a63c6237 | -6.14646 | -44.65615 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 54178380-4a69-32c4-9400-7cd99dad34be | -5.25448 | -42.97957 | 2025-10-05 03:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c88f679b-c0da-38f8-9ea5-f3afc813132c | -5.22902 | -43.70768 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9ac9d2f-bbc1-322e-a502-11d54332eba2 | -5.896 | -42.91064 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 9045794c-42e3-3d45-a234-8cc480f70598 | -6.46496 | -44.58765 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bec9324d-13b5-333e-977f-e34af56ed065 | -4.63465 | -43.18413 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2105fb6f-d3aa-3908-90de-2d798718663e | -6.06205 | -41.24701 | 2025-10-05 03:32:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01493fa4-313b-346b-a7af-86ae174bad25 | -6.40151 | -43.06483 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1ead9025-f361-32a1-8f32-5bef9210fa38 | -6.41099 | -43.05528 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6f213525-1257-3a56-b5d2-2bb19ee5f6d1 | -6.21412 | -44.07711 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35fb26ed-3367-3328-9658-1fe057918ffc | -6.70803 | -42.83942 | 2025-10-05 03:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 375591c7-748d-3834-8492-a9d5a65c265c | -5.49172 | -39.507 | 2025-10-05 03:32:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57b5136d-e3ea-3b37-a8a1-be8ad9a8f3a5 | -5.78605 | -42.92192 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 9c601377-1400-3221-ae6a-b8bbbf808ed2 | -6.52804 | -43.3754 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1eda3d01-2f08-3991-88ff-c3ad9e2b1150 | -5.87712 | -42.54192 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ae86be30-6a5f-30f8-ac6e-d11ce300943f | -5.737 | -42.04791 | 2025-10-05 03:32:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 036f7cfb-6493-3152-8609-abad79d42456 | -6.63793 | -42.80182 | 2025-10-05 03:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| dfd4b2dd-6bfe-3b6f-8b7f-69c214652ab6 | -8.17068 | -34.97996 | 2025-10-05 03:32:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a0a6f0f6-1ebd-3fac-8b9d-90a9335f79f0 | -6.43157 | -46.031 | 2025-10-05 03:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3ca7ac0-7445-3451-960b-28d4309d28fa | -6.43367 | -46.0286 | 2025-10-05 03:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57e10290-2f91-31d1-bf86-7b8290e635c3 | -3.84397 | -41.58366 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2db7f812-5573-3f66-a96d-32de5bc8ed2d | -6.59546 | -44.31969 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d142a38-5b8c-3d43-a12c-cddfcbed730f | -5.92557 | -43.33204 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| caa4a163-c7ef-3139-9939-bddb2bd4256d | -4.90006 | -37.2814 | 2025-10-05 03:32:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb76a844-99ca-310e-8140-42b28dd16e6b | -5.77071 | -42.97821 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74759c5d-90c8-3676-87c9-7652d8345be9 | -5.91676 | -42.89266 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 70bba8e0-f1b4-3b7d-959d-fd4125d14277 | -4.45065 | -43.24 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2383db4a-7522-3a69-826e-bcb364284946 | -5.27752 | -42.9216 | 2025-10-05 03:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7723a35f-986c-3c99-9900-fb8415acd69e | -7.02913 | -42.77272 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac39a48a-ab81-39de-84e1-63d63540f773 | -5.92193 | -42.89851 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e8cb8443-7767-3cc7-83e9-77b40271b255 | -6.00381 | -42.52059 | 2025-10-05 03:32:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3ac0748e-c95f-32f3-bab4-abe93ef9c2d0 | -7.29268 | -39.27198 | 2025-10-05 03:32:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 579d8f6b-bbbe-3e74-8e36-ddc813c4cf16 | -5.99051 | -44.35794 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3919909a-d147-3d22-9619-191a92723d98 | -6.91647 | -37.44164 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a70ddac6-e3a6-3bae-973e-63ae0a69bf87 | -7.43181 | -41.12385 | 2025-10-05 03:32:00 | NPP-375D | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b409ecf0-eeae-3818-8aa9-f8b53f596cef | -5.92625 | -43.33521 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45913c04-012c-3029-9245-89c68060b12a | -6.20659 | -44.07838 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1930047-e9d5-3d59-8ba4-98d9743591ff | -5.91718 | -42.89661 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 96f76710-6511-36b3-aca2-bfa919820042 | -5.88287 | -42.909 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| dea05284-6de5-3f51-8735-9d41fb8b7640 | -5.78525 | -42.92647 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 213.8 |
| 674f7668-a510-3a20-9a0d-9cc5b118c306 | -6.40091 | -42.69281 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d656d3f-6c67-38f1-9bc1-f1415cbb0dc5 | -6.30325 | -42.44463 | 2025-10-05 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 326351e0-6c94-3ffc-b3ee-bf6d655869b1 | -5.74505 | -42.04401 | 2025-10-05 03:32:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d03a74ab-1c78-3381-b6e3-1b6e698f9c10 | -6.15166 | -44.60806 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af686837-efef-32e7-9559-ae9c28502ab7 | -6.15753 | -44.67076 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a0992505-82ce-3090-a2dd-3b66e20f6d44 | -7.03537 | -42.80466 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dc23b3ec-076a-319f-9712-39e640b47970 | -6.30398 | -42.44065 | 2025-10-05 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cce7c8f3-0a5f-3d7f-acd1-e3ab418753ca | -5.48856 | -42.79938 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1450e1f4-755e-3a8c-9b68-5107b998fdb6 | -6.13972 | -44.63629 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9718c2c3-8378-34a7-b297-8bdabe5163ee | -4.44 | -43.24524 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1dac8bf6-b87a-3571-8408-cb805bd0dcac | -4.63378 | -43.18908 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |


[Clique aqui para ver as próximas entradas](README21.md)
