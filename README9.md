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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b49002b6-a188-3406-a178-c135d1d893f4 | -2.55046 | -47.65741 | 2025-09-30 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9c93b261-d18d-3b01-a156-541a5fe4cfc1 | -7.20112 | -48.60116 | 2025-09-30 00:35:00 | TERRA_M-M | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e9271fb2-7d85-3d62-a3b2-99235b64eab5 | -6.52174 | -45.22756 | 2025-09-30 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c0f716dc-ccf2-3d06-925f-823b88ea25b7 | -5.05004 | -45.31969 | 2025-09-30 00:35:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| c2dff187-ddf1-3802-9b91-c41d9d6ca8e8 | -7.91686 | -48.1861 | 2025-09-30 00:35:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 27dc8731-4891-3a05-8f48-8c800e03b26b | -5.87889 | -48.11711 | 2025-09-30 00:35:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f8fd7417-519a-320c-92b7-0d9ef2c7e69e | -5.82171 | -42.77194 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 0fcf1dae-0276-3768-b866-ff800c20e80d | -3.50208 | -52.46696 | 2025-09-30 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 762cfc40-3873-3a1b-8a28-ef9e0bf02d8f | -3.04879 | -48.7102 | 2025-09-30 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2b5d557d-f4bc-3b5f-b125-bdc1c23c7a6f | -3.28642 | -50.03037 | 2025-09-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 23ebdae5-37f7-315d-873e-d54e3a7e8c62 | -7.04632 | -46.41983 | 2025-09-30 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ae6866d9-6b9d-355c-8930-5c317408d856 | -3.84997 | -48.96952 | 2025-09-30 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cc35cc03-4b16-376f-bfe5-013608efdd6b | -4.87922 | -48.88333 | 2025-09-30 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b9e7825-4f83-3f2b-a110-71e00c7a3126 | -8.50841 | -54.59988 | 2025-09-30 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| acf1b625-ab2a-3485-b8c1-2f450404abec | -2.98896 | -49.27894 | 2025-09-30 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff290f9d-9c7b-3077-9acc-bb372a5cbd36 | -6.82139 | -48.71601 | 2025-09-30 00:35:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a6adec1b-4747-3181-a581-b6e8c2bb8651 | -3.74995 | -51.3816 | 2025-09-30 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2b83f1ed-7bde-3972-b321-50b37efab4a9 | -2.95919 | -48.5988 | 2025-09-30 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1884f6ff-04ed-37d9-9655-7caa5c096db4 | -5.97877 | -44.14005 | 2025-09-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4e5e233c-29e2-3938-b7c6-feefb1c9c603 | -5.7357 | -42.8103 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| cb856c84-4c34-3461-82f7-b6f6952841f6 | -5.31742 | -44.79193 | 2025-09-30 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31050559-0d0f-3001-8752-4603ada98737 | -7.40957 | -47.07825 | 2025-09-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8eb79e8c-821d-33de-8701-7c00546bff46 | -7.68572 | -49.63691 | 2025-09-30 00:35:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 083c8eeb-d057-38e0-b2b8-c9f58f9a6917 | -5.22269 | -45.24098 | 2025-09-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3c5053f6-2d70-3aed-bc1f-3e2310c5653a | -3.10447 | -47.0133 | 2025-09-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 07b88bd9-871d-37f3-8510-438d574c11b5 | -7.92571 | -48.18483 | 2025-09-30 00:35:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0d4e8633-ecd9-3ec6-ba2a-dbfdc5a29d55 | -7.66169 | -47.4184 | 2025-09-30 00:35:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| de9f54b4-0ec7-3e2c-950b-fd287c091366 | -5.96488 | -44.12614 | 2025-09-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6e829554-68e6-39b9-b479-27557cd987b8 | -5.04809 | -45.30653 | 2025-09-30 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7ace5c57-7964-30ea-a868-69f2aa6b8404 | -3.84601 | -52.28818 | 2025-09-30 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6b32b432-3b18-394f-bbb9-a44578266d18 | -5.77768 | -48.50616 | 2025-09-30 00:35:00 | TERRA_M-M | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e6784a0c-4fbc-3e44-8ae7-6db246de9161 | -7.19989 | -48.59231 | 2025-09-30 00:35:00 | TERRA_M-M | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 083cbfc8-102e-3d9f-8546-9f14b8ba109a | -5.66446 | -45.2977 | 2025-09-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c008f5c8-f472-30ec-8c47-7d5d1e44b4f7 | -7.55773 | -46.76265 | 2025-09-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a15c769-4ca5-3bbf-856e-c1e7fecd253f | -6.5622 | -43.41755 | 2025-09-30 00:35:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 784b1eb8-da3d-3ee3-a66e-89d040d18f43 | -7.04761 | -45.18747 | 2025-09-30 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 2b7001f0-ddf7-3933-8864-6e78dfd1537c | -4.47849 | -47.66745 | 2025-09-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e3a337d0-23a8-38bb-bcc3-2c49ae98dffa | -5.52669 | -43.87529 | 2025-09-30 00:35:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 30c0ea90-2c6e-337c-8d89-fde5aae4a4bd | -5.04026 | -43.61039 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c3b9dac3-ad1d-3889-a9c0-7edc9bcceeed | -3.28764 | -50.03914 | 2025-09-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e1b5766-0fd3-3cd2-8a9a-80ee7dee082d | -3.98383 | -47.883 | 2025-09-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 90f817d8-a80e-3aa2-a02f-82b05f1d85a9 | -3.22071 | -49.34515 | 2025-09-30 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e32c442-eefc-39c1-880b-90c8feb39d59 | -3.25305 | -49.12408 | 2025-09-30 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0b13fcf3-c88d-3f73-b746-83686eb08b14 | -7.47522 | -47.27458 | 2025-09-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 472ceeb6-78e0-3b87-aa2f-ba1a97bb9436 | -7.80356 | -48.03447 | 2025-09-30 00:35:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| af384810-e390-33a1-b1e5-15e21a5a4845 | -6.80197 | -47.08135 | 2025-09-30 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1dacb596-5148-3a08-a2a9-10f43855b512 | -5.73877 | -42.83078 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 28357310-1ee7-30fa-a9a5-d7303c1475b8 | -5.32457 | -45.23259 | 2025-09-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 84306d60-1069-36c5-a4ad-ab40b3e1844e | -5.97644 | -44.12471 | 2025-09-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 71e8af59-cc72-3f67-8d68-49c7a6f09fcb | -4.97629 | -45.29576 | 2025-09-30 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 59a20261-3e13-3267-af83-75245ebd6dfb | -5.52915 | -43.8919 | 2025-09-30 00:35:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ffbc6b9f-1b7d-34ed-afdd-dfc108ba2319 | -3.86006 | -48.97716 | 2025-09-30 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1c28fdc7-aebd-3849-b7ce-a290df9f37ea | -3.22078 | -47.63223 | 2025-09-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ee1c196c-9456-39e1-9ef6-65fef6193446 | -6.50438 | -44.26445 | 2025-09-30 00:35:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ac02508a-4483-3662-bafb-83294c5b3a2e | -5.96785 | -44.13148 | 2025-09-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 85193457-82ad-33a3-b746-52335c990f67 | -5.85474 | -50.06722 | 2025-09-30 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 547d918a-72ce-3385-a138-d1487641cfb9 | -5.73605 | -43.96596 | 2025-09-30 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6fb0ae5f-aaf3-330e-bf7e-3e3ddf8bb1fa | -3.09475 | -47.01468 | 2025-09-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 5b25684e-1249-3efb-a39f-791509d2f4df | -3.0932 | -47.00377 | 2025-09-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5effe566-774f-3ef7-9ea6-6426f0e4fe51 | -5.09677 | -47.47582 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f790e6d9-765d-3c45-99f3-dc16e953317d | -3.81192 | -47.58551 | 2025-09-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7510788c-1f2c-30bd-b9a1-c2c5ea5ae1bc | -4.98021 | -46.799 | 2025-09-30 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6dda2be0-15a4-3698-afa0-ae85fb2d01b5 | -5.58372 | -48.96877 | 2025-09-30 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 02236f2c-5d0a-30f9-8f89-09c94919a260 | -6.51128 | -45.2291 | 2025-09-30 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b740f1e0-2f03-3af4-8701-dc9d54fe25b3 | -5.85598 | -50.07618 | 2025-09-30 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4c5273a3-0c2b-3c79-af1d-ee664494dbfa | -6.43336 | -43.06853 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 0d8ab262-3cea-32b5-9594-e034522d5d18 | -7.65602 | -49.56485 | 2025-09-30 00:35:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f2a58c7a-4780-38c3-9186-6badbec71d5f | -7.50695 | -45.44459 | 2025-09-30 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b54c99a7-5c19-33e8-8214-82c50e041b5f | -6.09486 | -42.66745 | 2025-09-30 00:35:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 0b7001d9-aed6-3dae-a263-f7c64fe41a2a | -5.9849 | -51.91367 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e56d67d0-3b15-3c47-a24b-8208c005b74c | -3.8512 | -48.97842 | 2025-09-30 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 401308b9-c3a4-333a-9350-a4a0ce651f77 | -6.25321 | -43.64841 | 2025-09-30 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a725b1d3-541c-3a67-9695-c55e27925be3 | -3.84107 | -51.17512 | 2025-09-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a1c89b55-34d0-390d-869c-c1cc89c73bfc | -4.58583 | -50.69449 | 2025-09-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e8331403-8c43-36aa-ab68-3dee06593fda | -7.51709 | -45.44309 | 2025-09-30 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9ed97495-761a-3205-8328-e193e413ddab | -7.0495 | -45.20007 | 2025-09-30 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| dedfba61-34e1-32f2-b6aa-4c852711710c | -6.29182 | -43.91136 | 2025-09-30 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5b17564b-eb52-3bb6-b0c4-1810d4a4b44a | -4.26168 | -48.5513 | 2025-09-30 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ac0e8848-ab67-340a-bc73-bc5ba290b0fb | -6.27333 | -43.65699 | 2025-09-30 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3401f99e-ad74-3949-8b43-312d85201162 | -6.84256 | -44.83261 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 404d0221-3e3e-36e2-bec8-81ec49cccfec | -7.43162 | -47.81062 | 2025-09-30 00:35:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 004099dc-915a-3469-87f6-c8f1d2df9b2a | -6.09306 | -42.66208 | 2025-09-30 00:35:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 21551ed3-2509-3566-bdf4-318090f746e9 | -4.57688 | -50.69574 | 2025-09-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d1d503c3-0680-367d-a494-aee08cc3a087 | -7.56663 | -49.84933 | 2025-09-30 00:35:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 276a9228-2d12-3c47-9654-de72741ed3aa | -5.22072 | -45.22766 | 2025-09-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 5c141b57-010f-3b0a-bbf6-474090a63153 | -6.8293 | -46.62922 | 2025-09-30 00:35:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 249c2b05-4c2b-38a9-8413-9ea79a575a46 | -4.47988 | -47.67718 | 2025-09-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 536d84b3-94b9-3904-bfe8-362034ffc078 | -4.58458 | -50.68541 | 2025-09-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 763984e4-fc31-3817-a9f8-6083b13ecb6b | -4.89024 | -43.47231 | 2025-09-30 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 2b064bdd-c441-38c0-b316-7cc46c11bb5a | -7.52214 | -46.69228 | 2025-09-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 854d3f74-1b60-3a93-91b7-f288a0f6f240 | -3.50352 | -52.4775 | 2025-09-30 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 99d20bc7-32c9-386c-b922-95370da2e80f | -5.74358 | -42.68579 | 2025-09-30 00:35:00 | TERRA_M-M | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| d76cdb3a-7920-3d2b-a64b-6199242132a7 | -5.82474 | -42.79205 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| f4273f81-7534-3443-8208-af2cf2df6392 | -4.2963 | -48.27003 | 2025-09-30 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| eb762558-73c0-31d2-94d5-81daf095e042 | -4.33435 | -47.88607 | 2025-09-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ee398bd0-b1bc-3e09-b0fa-57c295c75fe7 | -5.91794 | -45.85376 | 2025-09-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2948c70-d5fb-3634-b317-170f4383a854 | -5.22422 | -43.69637 | 2025-09-30 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1006d660-5454-3ca8-9595-6224c0c536b7 | -4.07915 | -48.03738 | 2025-09-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e51d3902-5096-3a02-ae25-a15ab5ed4da8 | -3.54975 | -50.32514 | 2025-09-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7acf3e5e-3a61-3f3f-908c-be838073bf09 | -4.26294 | -48.56031 | 2025-09-30 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README10.md)
