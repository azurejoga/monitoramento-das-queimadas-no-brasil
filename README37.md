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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ad06d87-d364-3722-a3c7-e3468344580b | -8.19694 | -43.33033 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0e25d136-74c3-30dd-99d2-d48339d1ca59 | -5.64233 | -45.97068 | 2025-10-10 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f129843c-1f8e-3bd6-8cba-5aefb6b0f632 | -8.89959 | -46.0079 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a1787d9-ad40-38b8-bee1-0ee2725a2e70 | -6.56821 | -44.78254 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8234ca8-1cc8-3866-9a64-8bdb40e3a58b | -9.6658 | -43.84565 | 2025-10-10 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd6eadef-65a7-3db1-8595-57efcc8f3725 | -7.26627 | -44.10042 | 2025-10-10 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdbf7480-4aee-364c-ad13-d26023507cdb | -5.85093 | -50.07173 | 2025-10-10 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 163e40da-a320-3d84-8ad2-bea3cb082118 | -8.53537 | -46.10883 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 562cf5ea-d8cf-346c-90e8-39218f3e8bbb | -12.27164 | -47.85081 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98e113b0-b822-3173-bbba-34413ef1a3a0 | -8.22065 | -44.13654 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17f7e657-4bd6-32df-bb8a-a1a2fca117d8 | -12.62993 | -45.05704 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e1fadb30-7d97-3969-b33f-185837b9ecc7 | -7.08391 | -43.51557 | 2025-10-10 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a3362e7-561d-3fdb-9c3c-9c9e72d47364 | -8.52553 | -46.11225 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90ea8484-b524-39cc-b230-193385682edb | -8.50201 | -46.14721 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fe3c916-5a37-3e94-b5fa-7c4e873ce76d | -11.09931 | -41.05477 | 2025-10-10 04:51:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 21a7cc8d-e59a-3529-9491-b6d85e2a088b | -10.03901 | -59.36513 | 2025-10-10 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3ef97b3-028e-395b-8202-204df1adb511 | -6.72114 | -42.14486 | 2025-10-10 04:51:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8fdc02c2-8756-31f1-a472-5e586b7f66ea | -12.40838 | -46.70308 | 2025-10-10 04:51:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5d6d8ad-552c-36cc-81b4-de3c4c1d5137 | -7.00204 | -46.99349 | 2025-10-10 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8fac0a5-dd60-38ff-bba3-bf8b1144d189 | -8.89103 | -46.01053 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01e8d0a7-3e98-3bbf-8273-cfe0af73ed89 | -8.19741 | -43.32669 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 88c366af-9b4d-35cb-bb7a-07d4ae701c7c | -8.20772 | -43.37732 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 662015d3-2772-3558-8a2f-1a47a9e522f8 | -6.58022 | -44.62653 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bf307797-8f76-3ff1-84c5-7f9dfb6e9c08 | -8.52094 | -46.1116 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d5d0b16-4543-3490-91a3-e9bbd69c65b2 | -11.78659 | -45.04194 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc13b745-6955-33c4-b789-5c842a06c574 | -6.50497 | -44.43303 | 2025-10-10 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 216e647d-790c-3bb2-ad74-5299365a0f23 | -12.15502 | -47.91728 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c703caa3-8f75-36f8-a323-c966c7352c8b | -7.78207 | -44.04804 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37578f53-7e2b-3b74-ab96-37dc1c5492e2 | -7.317 | -44.84702 | 2025-10-10 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81402903-cc1a-375d-85f9-692d560fe30a | -8.00444 | -43.75542 | 2025-10-10 04:51:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 472a9b7b-b2a2-37f8-a11a-f6574f7a60d8 | -11.77569 | -45.04489 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a0eb2fa-afd1-395e-bf05-845ce916e5ec | -7.77737 | -44.04671 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b7aefd6-7ef9-3162-9f43-73854389ce90 | -8.20198 | -43.33485 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1564fff3-3af5-30b5-8fd9-a7bf53033d50 | -12.78011 | -45.77805 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d79a2305-b9a2-33ac-bf93-e8b6f1aa5784 | -13.06608 | -43.84474 | 2025-10-10 04:51:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19f72140-89f3-3433-9560-82526762c670 | -7.78075 | -44.05756 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f7e5a80-d976-3c55-a926-4160121c371f | -8.00586 | -44.45319 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bb6ee53-c1ff-3773-bb4f-52782547cc15 | -8.52946 | -46.11766 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a168331-d2d5-368a-861f-41b0a535fbbf | -6.82324 | -42.79145 | 2025-10-10 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3d506800-7be4-30a8-b8bb-63346eef7b5c | -8.50652 | -46.11438 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8ece7e5-cff6-3f9e-a76a-4197abc99044 | -7.53497 | -44.29866 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c7643d1-b466-31ec-8ed2-99a249008d7d | -7.32 | -42.94276 | 2025-10-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6c3033d1-7044-39a5-927f-00c8c79ebabd | -7.38082 | -46.94238 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc1349aa-b257-3640-9e25-0919cfacc7f5 | -7.78697 | -44.05479 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f7ff9d6-dded-335b-ba1c-013a55195c40 | -7.77685 | -44.04719 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1ae2d46-f310-3504-ae5d-9292bacf7ca0 | -8.50392 | -46.13329 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 97924009-3fd7-3985-add4-3cd8ce349db6 | -13.39176 | -44.23098 | 2025-10-10 04:51:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c12b2f73-6dc7-3b3a-b497-15137ebbbeac | -7.42685 | -42.98673 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 054bc1b1-546c-323a-b4f5-0ff1aadf49a6 | -13.03073 | -47.88244 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47475a08-892e-3448-9601-b89664abe56b | -8.19964 | -47.86026 | 2025-10-10 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c287f35a-05a9-3355-ba39-bc00f8e75f23 | -8.51504 | -46.12044 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 77bc5b04-c86a-357f-b4ee-02699dbb33fb | -12.63476 | -45.06104 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c0a6473c-c932-398b-96f6-244c6e7a4718 | -8.51244 | -46.13931 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f639a1bd-7881-30e7-b366-333e10171d0e | -9.33162 | -46.11083 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64832c98-4d33-374e-9b68-2ab9f39de561 | -7.78133 | -44.0571 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14f18351-3f36-35cf-9685-1d0818b3bab3 | -7.54609 | -44.59886 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fb887d7-be02-3bdd-853f-50b6fd1db8fc | -7.84423 | -44.54899 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ce826ed-6940-35bb-ac1c-46578982802f | -11.96936 | -45.20776 | 2025-10-10 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb1327ab-c51e-33f1-9ba5-3830b01d99ae | -7.52904 | -44.304 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ac14d50-2237-3d3d-902b-7788cf5242b3 | -7.56182 | -44.29335 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37b4e543-154b-352e-b320-86dcc1816ce6 | -8.5052 | -46.08989 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2feb2a6-30ff-3af5-befd-28f0fae55116 | -8.50587 | -46.11913 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 62c2ac03-6fc8-3392-9463-148191c970a1 | -8.19141 | -43.32958 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 85759855-a863-33a5-813a-5bd5b49c52d4 | -11.63656 | -47.53192 | 2025-10-10 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ae6704d-8f8a-32d7-8d73-a3c60f4f7661 | -8.52356 | -46.12649 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e946c784-7ca4-38b1-891c-c1b470b0c8e2 | -12.22715 | -43.78696 | 2025-10-10 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11ac04e9-e291-3c09-9cf8-c59ca0e5a75b | -10.04396 | -59.36176 | 2025-10-10 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79b4d1fb-a35a-3af9-89f4-9b88d29f0165 | -7.27755 | -41.97244 | 2025-10-10 04:51:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ecf81e7-d51d-39e4-9ca4-32873174cc93 | -7.13344 | -44.13299 | 2025-10-10 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d90cba62-be35-3210-ab6f-c82932be58d3 | -7.78739 | -44.05159 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8fe8fbd-ccf4-350a-9d6c-a581290e9e4c | -8.99833 | -45.48059 | 2025-10-10 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 805eb780-9fb6-3f59-ba78-d7c4ac20ede9 | -7.57707 | -47.05488 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3f55421-04fd-3198-85bd-edb25737d8a5 | -8.17553 | -43.32164 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 49c7ed06-0f90-3d12-b6cf-f06a89dd76cf | -10.16286 | -44.55491 | 2025-10-10 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16f3d44f-94b5-348f-a471-919efd2b8f22 | -7.41718 | -42.97373 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 309a2e63-a215-36d1-9d32-c03451c60753 | -6.72062 | -42.14864 | 2025-10-10 04:51:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1013135f-d16d-3f4c-b00b-781c005c3693 | -7.78217 | -44.05076 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef7e84b9-cfed-3129-9c68-2efb515e9dec | -7.77215 | -44.04584 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74a36688-3df5-381e-abc2-66cecf133b38 | -7.79662 | -42.61167 | 2025-10-10 04:51:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8791a1c0-8708-3a6b-9cd4-4d03565f3b5f | -7.05422 | -45.045 | 2025-10-10 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e22ddb6c-1e20-3cdf-a070-f73e29a03a44 | -7.78259 | -44.04755 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 778ea491-5ace-37ee-9d76-8f8ab7d6dcf7 | -7.13389 | -44.12964 | 2025-10-10 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c5a5061-f266-3f26-b691-de9cdf10a59a | -7.13433 | -44.12635 | 2025-10-10 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a500d0-3a3e-3361-bad1-9f65d805f3ea | -11.723 | -47.45637 | 2025-10-10 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce82dffd-6528-3690-ba08-c6f2007296e2 | -7.03629 | -49.3023 | 2025-10-10 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14b7f504-d630-3883-8b0d-c15ffbd49b99 | -8.50786 | -46.13864 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 040fc918-4a21-3f8f-82df-e97db1d81826 | -9.09848 | -45.02887 | 2025-10-10 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13369bf0-8fb1-3598-bf3c-abe1f3574c79 | -12.62876 | -45.06662 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b9d6c3c-586e-307a-a4ae-034f1fa52234 | -12.9294 | -45.05676 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 700eb303-c9e5-3fc5-b4f2-4c47c4054968 | -5.79799 | -45.11084 | 2025-10-10 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b883275-88a1-3d05-9211-010c4d8917a4 | -7.14783 | -42.18951 | 2025-10-10 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7e4d109-23be-3cb6-b473-828f219b7adb | -13.0167 | -47.92178 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bc83d17-5d8d-3bde-a458-2aa1d29cba71 | -12.63515 | -45.05785 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6ff85c56-ed2f-353e-b079-106f044e990c | -7.77654 | -44.05299 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f164814-cdd5-3ce3-ab53-0f730c26ab24 | -7.63195 | -43.05191 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33f1d614-0bdb-3eb1-8117-d8b85ffa2751 | -6.66372 | -47.74578 | 2025-10-10 04:51:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38939d48-f5cd-35b7-abd6-1820b0ab922d | -12.64078 | -45.05532 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 34b9efcd-188f-3c58-bc39-c08f99a8342f | -7.77256 | -44.04269 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7681c0ae-4327-3ba3-9be5-735eddefdc7f | -7.57684 | -47.05424 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afd40616-0bc7-3d0c-a6ca-bb570056009e | -8.51635 | -46.11095 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README38.md)
