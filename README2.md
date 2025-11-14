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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 372dabd6-74d7-3055-9fff-982db31a69ad | -7.8668 | -44.2846 | 2025-11-14 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 0191bfe4-ad1f-31e7-8634-eb554ca376fe | 3.0912 | -60.7464 | 2025-11-14 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| eda1663a-ed01-34c2-9c52-20b2093ea12e | -2.8295 | -45.4868 | 2025-11-14 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f727717e-be3a-3ae6-86d0-d69d9e36ca24 | 3.1094 | -60.765 | 2025-11-14 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 206.2 |
| 1461e875-f4eb-3385-90de-fb444870e20d | -4.702 | -46.4286 | 2025-11-14 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 875e5f57-3b81-338d-9058-34c21ac73446 | -2.9434 | -49.3655 | 2025-11-14 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d016ec88-c5f5-35e8-b4f9-8dcda5f35a6c | -7.8479 | -44.2865 | 2025-11-14 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 217.6 |
| ee776961-2c9a-3dae-a013-0180e7489e3b | -12.6992 | -45.4335 | 2025-11-14 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 4da83b62-1292-3143-bf01-d13b0cabf2c9 | -2.5238 | -47.8115 | 2025-11-14 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d1480d6d-a81b-33fb-a81b-7340df8e4194 | -11.8681 | -49.1976 | 2025-11-14 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5eb740cb-6f38-388b-a136-804357d578e9 | -4.7204 | -46.4497 | 2025-11-14 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 7833f37e-d176-3ba7-899c-59f19a996730 | -7.8665 | -44.3077 | 2025-11-14 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 83a33df1-9586-3d05-97be-5692a627eca0 | 3.146 | -60.7075 | 2025-11-14 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 68e17ff0-5ed7-38af-9897-f7730db68b6c | -6.1606 | -48.0507 | 2025-11-14 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 3379850b-0c8c-3849-9aaf-08af3d22332a | -12.6996 | -45.4104 | 2025-11-14 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 76ffd16c-786d-3370-825f-8cd6a3dd6ef0 | -11.8483 | -49.2436 | 2025-11-14 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e8670795-dea7-3e4b-b50c-a74d07a034e5 | -20.10079 | -41.68649 | 2025-11-14 00:30:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 9e0ad69f-4cc2-32c0-97f7-18e5a0cb2467 | -20.11725 | -45.83943 | 2025-11-14 00:30:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3a30e72d-e481-3560-a6e8-28c7e1ed6f72 | -17.63506 | -46.706 | 2025-11-14 00:30:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c592d838-8574-3aac-97ca-0ebf16e95984 | -17.79521 | -44.98641 | 2025-11-14 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 956fd624-f538-348f-8aa4-cc65e496f66b | -17.62609 | -46.70745 | 2025-11-14 00:30:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e6f9eca-6f50-33ee-9ea0-301105e68120 | -17.03413 | -46.75766 | 2025-11-14 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f3fd1ab4-b176-3106-adb3-adf8c4552596 | -20.1082 | -45.841 | 2025-11-14 00:30:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed403352-d124-3989-8850-3919a8891eeb | -17.97942 | -42.93338 | 2025-11-14 00:30:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a9ce157d-8dac-344e-b196-f7c6d7d408c3 | -20.0977 | -41.66859 | 2025-11-14 00:30:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.8 |
| 44e5b661-7061-3f2e-9ee8-ff31dca6773d | -18.70559 | -43.01027 | 2025-11-14 00:30:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| cc63ef96-22de-302b-a8a2-737746d67261 | -11.99335 | -44.2866 | 2025-11-14 00:32:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3a31b099-cd40-34eb-8fc0-96769ba11020 | -11.03522 | -44.64593 | 2025-11-14 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bfe63117-5ffd-3825-b1fb-3ab3d73d626f | -12.66334 | -46.75409 | 2025-11-14 00:32:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 297e7235-d09c-3417-9a14-3e5579af76ef | -10.73245 | -44.02351 | 2025-11-14 00:32:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 9b610a19-2bb9-3c0b-b0ec-f93d5a76d1e0 | -10.63328 | -45.00758 | 2025-11-14 00:32:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5f04cdbf-7f15-38a7-b252-99ddfbe6e8c2 | -13.68628 | -48.42155 | 2025-11-14 00:32:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5c5a552-94ea-3c44-856f-9eec27a46317 | -9.81639 | -48.35014 | 2025-11-14 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| eb918432-8c42-36dd-ad53-ede51e832a54 | -8.91561 | -41.07677 | 2025-11-14 00:32:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 5bda8757-4487-34c4-a410-b50cb966d9c4 | -9.43532 | -46.9738 | 2025-11-14 00:32:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 99ab73e2-7aba-358a-b679-150f1940cd86 | -9.49584 | -47.45982 | 2025-11-14 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3c92371f-21b6-3df1-ace2-0f56ec899b80 | -15.39024 | -48.96065 | 2025-11-14 00:32:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 84890b78-3dac-3957-83c6-ce9bc29fd0ee | -12.0205 | -46.77231 | 2025-11-14 00:32:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6facb9e7-badd-328d-9ff8-352483a33404 | -11.84469 | -49.21707 | 2025-11-14 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d6acbc4d-b433-3a30-8164-590609880b13 | -10.75484 | -44.91127 | 2025-11-14 00:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 777a697b-a599-3093-9af6-a74b813391fd | -8.91294 | -41.07193 | 2025-11-14 00:32:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| d7618271-dc4e-3a3b-9491-01c13a9ef307 | -12.06341 | -49.40286 | 2025-11-14 00:32:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 19a78c8c-a33f-3ec6-b3f5-159faec0d202 | -14.95132 | -48.44327 | 2025-11-14 00:32:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 92d0e8e5-b24b-37d4-bcaf-9755204a17fb | -14.67439 | -46.57067 | 2025-11-14 00:32:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| ca8fac03-4aeb-3fbe-a0e6-0327f72b7626 | -11.85478 | -49.22477 | 2025-11-14 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 353.2 |
| c036aa62-7b2f-3899-8c83-9fcfdf16b67b | -10.33904 | -49.9135 | 2025-11-14 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc63056a-9143-399d-8771-7d61fdeb2786 | -14.13629 | -44.20354 | 2025-11-14 00:32:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 55be2955-b660-396e-8246-d2a1dc0a9984 | -10.7466 | -44.5634 | 2025-11-14 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2fe356fa-fb21-341d-91c6-bd38e81b0d1d | -10.74662 | -44.55772 | 2025-11-14 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 60cca275-3f13-34ac-a43c-1e2e9b91c2f9 | -11.2526 | -47.50122 | 2025-11-14 00:32:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1858099b-139c-310e-969a-722c27a8e8e5 | -15.47376 | -43.55248 | 2025-11-14 00:32:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 598f3a3f-fe04-31dc-b7f0-5e2150d5ee95 | -12.69608 | -45.41241 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dfb1cc05-13f9-3a24-9355-e22dd745cf16 | -15.29946 | -47.38473 | 2025-11-14 00:32:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1dafdc10-8a00-364e-8545-2dfc38031136 | -15.2503 | -47.94542 | 2025-11-14 00:32:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 20ba2f6e-570a-3f49-b125-31a0d1af2b5a | -9.35057 | -46.59803 | 2025-11-14 00:32:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| aca261db-20f9-3e79-a7ee-65fc7bd94e2b | -12.6979 | -45.42443 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 5b1302d4-236e-3c02-a503-546b0a0699ec | -10.3761 | -47.68442 | 2025-11-14 00:32:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4497dd0c-2a29-3cc0-aa4c-f5ce28083cd2 | -12.70619 | -45.41074 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 19d547b8-9b9e-371e-b25d-3ee3f743df2f | -10.757 | -44.92525 | 2025-11-14 00:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 49b18e3b-1b4a-39dd-b101-c81651b2de50 | -12.0111 | -46.7738 | 2025-11-14 00:32:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5f849317-4e5b-3bbf-8028-b9776f3d5eaf | -11.59241 | -55.5582 | 2025-11-14 00:32:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 551b392a-5f7b-3f80-8eab-4065dbf6dcab | -12.04177 | -49.44284 | 2025-11-14 00:32:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ff3892bb-73bc-31e2-9ca6-db80fcb82017 | -13.15172 | -48.21676 | 2025-11-14 00:32:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1eda115-3efa-35b5-b610-50a180d02ca0 | -11.4407 | -49.0897 | 2025-11-14 00:32:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4bbcb5d2-c2de-3436-8154-ed67f3ca98c7 | -9.9142 | -47.87225 | 2025-11-14 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2c7eb3b5-555c-39f5-843b-c555cb84e4d0 | -12.07238 | -48.20945 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e858d3c4-7765-3429-a96c-b72baa54c195 | -9.30861 | -47.83222 | 2025-11-14 00:32:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0cdee76c-deb6-3806-93f4-c7b87b77754e | -9.31781 | -47.83084 | 2025-11-14 00:32:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 53d51445-7ecc-378a-8f2a-e78f3d57eb1c | -12.29754 | -47.91258 | 2025-11-14 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0b461ee-9ba5-3fd9-8563-60d1c0cffcff | -12.00957 | -46.76353 | 2025-11-14 00:32:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c5ed2429-7bd6-3d82-a2f5-d5c8e95c0515 | -11.85354 | -49.21578 | 2025-11-14 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 346.5 |
| d16e8ad4-c58a-3a40-bced-eb404c780f55 | -11.7393 | -48.52506 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5fdb698d-8916-36bc-9ef3-4ddba5112fbc | -10.05257 | -44.76831 | 2025-11-14 00:32:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 05a2698b-04e5-3d17-bfa5-51833ff797d0 | -11.63601 | -48.57407 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae04cccf-0033-3fa7-b9cf-c7552fe41786 | -10.63046 | -45.01379 | 2025-11-14 00:32:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 37619ce9-0e33-3887-90cc-f5ec185c4439 | -12.13832 | -48.02438 | 2025-11-14 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ab94f4fa-c658-31a4-90a1-e849b920bbb9 | -14.30959 | -44.58097 | 2025-11-14 00:32:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb0171a8-ebbf-386b-bfb6-ed124debfb9f | -11.93951 | -43.94822 | 2025-11-14 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| fb3b7fae-38dd-371d-9fb8-9cb92fd941ba | -15.16071 | -46.61552 | 2025-11-14 00:32:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cfe6707b-cf96-323a-84c0-cc18331d9c85 | -12.68961 | -45.43799 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| a16add41-3f06-3ba7-9e2e-fea14aafd716 | -9.8177 | -48.35942 | 2025-11-14 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa61be0c-2861-35c9-959b-1ed67b6f09f7 | -13.68988 | -43.00495 | 2025-11-14 00:32:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| df321e89-a156-393d-a280-8384b235b4ca | -14.67583 | -46.58039 | 2025-11-14 00:32:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77a14fd8-63f2-3354-a04d-17f230a16877 | -9.91283 | -47.86265 | 2025-11-14 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1f784da3-2169-3acb-a204-87f5128cbdc4 | -12.69971 | -45.43642 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a6779907-b677-30d8-9c4e-7d05bb45f63a | -9.31922 | -47.84055 | 2025-11-14 00:32:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f5f91476-9961-3963-8651-22481acca99d | -11.85602 | -49.23377 | 2025-11-14 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9012c90c-fb47-313f-be68-00dea8275e52 | -12.06465 | -49.41189 | 2025-11-14 00:32:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0fc5bc0-2021-3a21-9c4d-304e521977ab | -12.7199 | -45.43314 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 187a8151-89ff-3f1f-9df0-fdc085a2dd13 | -12.18192 | -48.07424 | 2025-11-14 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dd00a41b-4511-3646-bf50-580c644e1650 | -9.11886 | -43.94513 | 2025-11-14 00:32:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 18da4731-ed71-3fb2-9b25-ba6dff863746 | -11.99568 | -44.29556 | 2025-11-14 00:32:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5e1239fb-4607-3f4e-9d71-ed3092582d14 | -15.5555 | -44.49315 | 2025-11-14 00:32:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 30a63e53-e7fe-3376-a1af-2ad4734daeda | -11.93059 | -43.95524 | 2025-11-14 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e7c677ac-24dd-318b-85e5-aa9deea692f5 | -11.82001 | -47.79604 | 2025-11-14 00:32:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8f1b5ec4-d710-33ec-8b21-f4400dfe840a | -10.75894 | -45.0094 | 2025-11-14 00:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 504c40de-5a70-3d8c-a432-5e74cbd7b6fe | -11.94823 | -44.59456 | 2025-11-14 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 03d9c7c1-fafb-3723-8e49-abe6310b893e | -13.02735 | -46.52711 | 2025-11-14 00:32:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 35299938-d14c-3450-b3e4-f43a43e901d5 | -12.00498 | -46.77013 | 2025-11-14 00:32:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 063126d1-1450-3044-a872-cf8097f07d4f | -12.06216 | -48.20161 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README3.md)
