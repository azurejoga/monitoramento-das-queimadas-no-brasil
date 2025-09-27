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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fc535db-b968-3f75-aa29-502a938c1a0c | -5.30804 | -47.22549 | 2025-09-27 03:53:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b217f28-4ada-385f-a61f-6bf710997267 | -6.31695 | -43.45562 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8bdc0c2-d4b7-39e4-95ac-e159352faac0 | -5.76266 | -42.55087 | 2025-09-27 03:53:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 736dba40-526d-337e-8ffd-077b0de01376 | -5.56606 | -43.44073 | 2025-09-27 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be6bb745-8151-38e4-a45a-e27710e28cb0 | -5.4821 | -43.05844 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1719e37-cfb2-3af4-8829-5d237ec8f75b | -5.09094 | -43.05655 | 2025-09-27 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d695fff8-1fad-387d-aabc-541a8778de7e | -11.50357 | -43.54389 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f30242b-c0bb-3de5-bfb2-72511328c1b6 | -7.88117 | -44.02463 | 2025-09-27 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 285fad7e-7d28-3df6-aaee-057f6176bfa3 | -10.00176 | -44.17483 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bf5f11e-3420-3006-9a76-2773023f0125 | -12.29959 | -47.21728 | 2025-09-27 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8993ab50-49a7-3f22-a222-e7743aff7b5c | -10.29047 | -45.21515 | 2025-09-27 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa4ff37b-f708-3dda-bd13-a8ff4c400df2 | -7.78849 | -46.94518 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c12b9ec7-c363-3e4f-9dc4-7f487dc0720a | -7.64008 | -40.1622 | 2025-09-27 03:55:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4278dab0-71a7-36d6-a00b-f10b0b9e5a13 | -11.53961 | -46.94664 | 2025-09-27 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a9730a1-a90e-3a2a-9402-6a5834f6c410 | -11.7769 | -44.86444 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64a09a75-02d3-304c-8758-d3b307671ab7 | -8.5245 | -44.63665 | 2025-09-27 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffbb25b4-bf6a-36da-8bca-8b3cde1a9bdd | -11.41188 | -43.51044 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8a6d83f-0915-32f4-82bd-903be0f8bee5 | -11.69001 | -44.46461 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 253ace55-1b1d-3a0f-ad67-676a092b4de5 | -11.38298 | -44.93729 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac8c29bc-8eea-3646-8d77-255e59911e1a | -9.11233 | -45.8818 | 2025-09-27 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f0d84d4a-c9b4-371d-b953-14780eb87865 | -11.94458 | -47.87532 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94483d59-2916-3767-b6ce-b02037d76f47 | -10.41711 | -46.16694 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b27cdf05-56db-3d96-b5ea-96d98aee89db | -9.00384 | -49.16988 | 2025-09-27 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2417192d-61e6-3d51-ab10-2def91f4b7bc | -6.94894 | -43.2479 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0694b7d8-b11d-3732-b0ea-bf48f18d0102 | -11.65737 | -45.34526 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 940796e0-10a5-33b0-870d-49ef1e5ccb71 | -7.87773 | -44.02032 | 2025-09-27 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea3478ba-9a4e-3a58-92dc-f606d382c49c | -12.87543 | -47.08951 | 2025-09-27 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0c826d4-0c56-3820-9b9c-62aa10b9bda6 | -11.61241 | -45.42206 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6893596-ea44-3d1f-a9f2-d18fa37dc51b | -9.05506 | -45.5112 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| add71872-33e9-38eb-bc1c-4ea37f550270 | -8.82735 | -46.26661 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a97d8d76-c366-3bec-96ec-0f2de432f905 | -11.71446 | -44.4161 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ab7a6309-0123-3904-82c6-4b40f2b38753 | -11.43447 | -44.97648 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 398963e1-a710-3d5a-80df-76692e79f87f | -8.72348 | -46.68552 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39733a1b-9d3a-3540-b714-52430867dcb9 | -11.97167 | -46.59488 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a79bb59-2f52-30eb-bfbb-3651edf86854 | -11.96589 | -47.89694 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0767f2e-ada6-3b2d-8507-1d5686333814 | -8.83285 | -46.26262 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dba5347b-16aa-315e-8fc1-7affdeea2b73 | -7.37556 | -47.03145 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 97414b9c-748c-34bd-8623-5607541c78e4 | -6.61557 | -42.93179 | 2025-09-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b72e7daa-aad1-3761-97aa-f60506753668 | -9.69405 | -48.94277 | 2025-09-27 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bdb9e6e-22c2-304f-9431-d7bea36b4422 | -7.62418 | -43.83681 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c57a2ed-683b-373c-a2e1-d1fb841bb0a1 | -7.00169 | -46.98961 | 2025-09-27 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4c9bf0d-bc17-3325-b313-51effcd616b3 | -10.60473 | -49.63798 | 2025-09-27 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 864075d3-c39b-3aab-9304-a3157c59aa44 | -11.41576 | -44.91589 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f414c44-a62f-3f9a-8975-6efadd318957 | -7.12185 | -42.18103 | 2025-09-27 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 22935005-1d0d-3598-95cb-d612f4555441 | -12.03885 | -47.05884 | 2025-09-27 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a419da2e-bfb1-3672-83fb-11cd7d9d1009 | -11.35614 | -45.0193 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3f6e498c-0b47-390d-b740-2001c9984356 | -10.65635 | -47.27131 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a171c76b-4744-3072-a460-6bd6326692ee | -6.63108 | -43.82306 | 2025-09-27 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d531bb0-087a-30ff-b8ab-52d773c3e5cf | -10.8114 | -45.37266 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49ebadcf-42c1-31a3-860e-c5ba80bdf655 | -11.04396 | -45.87339 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92de1557-a79e-389d-9b88-ef354e65da88 | -9.18621 | -46.63628 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8965ec93-7184-3241-99c8-033619316195 | -12.44706 | -43.53912 | 2025-09-27 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d36a452e-9377-3db6-8960-5f2a265b5cdb | -6.93159 | -44.6429 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e543d97-3d08-3471-b2b1-ac5e63d58870 | -7.04684 | -43.02742 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| deaa3ff2-02f1-3756-b36a-d517e84cff10 | -9.1177 | -45.87771 | 2025-09-27 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aa8a13a8-35b4-3d8e-82dc-f6a4111d7da0 | -10.81067 | -45.37672 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ede82208-b476-33dc-b652-206c19411f50 | -7.35353 | -42.09649 | 2025-09-27 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 487530e7-9692-335f-a36c-0260756b9401 | -11.44554 | -44.93743 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 655c6ee8-bb19-3876-98f2-64beaafb5107 | -12.26548 | -44.07441 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34c4fbf1-e9d1-3740-a422-bd82672c7829 | -13.45056 | -44.55562 | 2025-09-27 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91ca4c9d-4386-3fb1-929f-953bb7239060 | -12.83349 | -44.68722 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20aeb51c-4b1d-3f50-9c6c-91e489d52dc4 | -10.00396 | -44.17642 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30a357f0-9311-33a3-a639-7c6ba4923fab | -7.8132 | -46.89293 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bdb1bb0c-b577-3493-833f-13c5ad2285ae | -6.68721 | -43.12572 | 2025-09-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe688458-1279-3138-a21c-eb22a80a3b31 | -12.95457 | -48.90939 | 2025-09-27 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4941ceb5-b1f3-3886-a6a6-57eaac93fa4e | -9.97895 | -43.58984 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ccf6db2-cdc9-33e1-8395-8613ed72f755 | -7.26224 | -42.98162 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 36370c02-1406-336f-bba6-b0b1c2f00325 | -11.43192 | -44.91943 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb795c97-d680-385a-890b-9781f5838255 | -11.79353 | -44.91205 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15becdf6-ea04-3025-aa95-8fdba029e930 | -10.57099 | -44.07419 | 2025-09-27 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc5548ca-361d-370d-9855-613d4e6147b8 | -10.13083 | -45.30954 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61fb748c-c2b2-3d57-953f-8edc809ea3f3 | -6.78775 | -41.7663 | 2025-09-27 03:55:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b4405ee-3ac3-36e8-a30e-ff37efe1aac7 | -11.36758 | -45.00205 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b603217-686d-3190-844f-a9902b5e7b94 | -10.17998 | -46.93004 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b4fdf2ce-efbe-3eae-be35-f1b5dd26a5f2 | -11.43673 | -44.98759 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f75f36fe-0a22-3d2e-8982-38fd515c7d84 | -12.82868 | -44.69165 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0bcce37-8a64-34d7-90f8-dc026a690f94 | -11.69713 | -44.4206 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e80cf46e-5f63-3d9a-a099-f07fd06524be | -11.96379 | -47.89911 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2ab3c72c-c3dd-3d66-b0f8-2bfb2f0a8f9b | -9.69953 | -48.94378 | 2025-09-27 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7bda7bb-4d9c-341b-bd34-4ea8d7f147d8 | -11.68986 | -44.46155 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d250bb5-4db2-36f9-98a7-ea1164156941 | -10.10721 | -45.34444 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6572c87d-baa7-3179-a449-b5569a4163a5 | -10.18001 | -46.92656 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b524c810-61ec-3803-adf0-e75aa9055f04 | -6.53281 | -43.83658 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a0b3f18-a1a1-305e-81f7-9f7113efe6e5 | -11.24444 | -45.55907 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7cca06bf-692f-3837-a194-23d9da63ecd9 | -10.12288 | -45.33023 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| baa56cda-ed95-3a2e-832f-53098d36e137 | -7.56735 | -42.42023 | 2025-09-27 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7c25e08-d544-3225-b36b-f29815b55074 | -7.77931 | -46.93932 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ddfaa76-e4c2-3f66-aaf5-f9f0b0975f9a | -11.43794 | -44.98069 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3ff95876-6e6c-35c7-9bff-fc995654ef07 | -11.78487 | -44.86639 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4660cd93-dbd4-3182-b4e4-0f7dcd533f14 | -9.75633 | -46.13864 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76054fa6-5b0d-3fca-9a88-06d73ac5017c | -8.51114 | -44.61448 | 2025-09-27 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dcc6f2b-7e14-3ba7-a91e-4dd315190fe1 | -7.04954 | -43.02559 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e5fea59d-458d-39ba-948a-b2503534147c | -6.22461 | -47.32932 | 2025-09-27 03:55:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc24a1a6-fddc-3681-a64b-08be8af6c4e9 | -11.38181 | -45.03529 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90a1755f-a815-3a7a-b8b8-f66daf088ead | -11.43284 | -45.00968 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c527a8ce-f85f-3f4c-a32b-02e53e202e48 | -11.62057 | -44.42058 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d581981a-8e96-34f8-9126-d31f145cb23d | -11.94831 | -47.87256 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d242ce3-26ae-3d82-8a45-dbee3ef5ceec | -10.12601 | -46.48006 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f55ae7ad-2d46-3955-b6ba-58b573061c93 | -12.54223 | -45.84994 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64ba0878-edcf-35c2-8a87-37952c1d3aac | -8.81806 | -46.26484 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README16.md)
