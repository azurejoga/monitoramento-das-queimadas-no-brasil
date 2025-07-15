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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b942fa9-72c3-3fd4-a801-ff7456d06ceb | -9.61481 | -49.01987 | 2025-07-15 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56b0a653-bbc0-3423-8b48-88f7cb5349a2 | -10.3748 | -47.14942 | 2025-07-15 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80ef3752-e895-32a5-8a77-16c9654eff20 | -5.48497 | -42.14801 | 2025-07-15 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 964c1f99-e847-3169-b27e-f02c5f91bd66 | -7.09529 | -49.17855 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fba526ba-272e-3edf-b889-08ce3fc77130 | -5.37114 | -43.92315 | 2025-07-15 04:32:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a2ace04e-a2f6-36df-931b-456a1bfdc10d | -8.59287 | -47.43565 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6701371-0910-3525-b789-b3eca8464aab | -7.75986 | -40.631 | 2025-07-15 04:32:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f71f4a93-4d87-3d30-8e17-035607d656db | -6.17978 | -44.38752 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3cf3033-3a0f-33f3-b4dd-b801b99b5d96 | -3.58247 | -47.52084 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3428fa9c-c089-3abc-b931-83dc46043e9f | -5.79187 | -45.1161 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30c427e9-45b9-3aed-9e1f-1ebaabb97312 | -8.81646 | -48.43874 | 2025-07-15 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 955ec6f0-0d82-399a-ba59-bc087db3043f | -6.75196 | -47.37261 | 2025-07-15 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04c1b7cb-cf92-3430-9c8d-4ea86bfc65d5 | -3.75853 | -47.11569 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ad0f0f0-a292-332a-a1af-a585381f1d54 | -7.28773 | -44.03268 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2135e9e-02e4-3869-b574-71cf8cd324a8 | -6.13413 | -45.84921 | 2025-07-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f65d092-7092-3280-a31d-500e58b83dfc | -9.15603 | -44.42061 | 2025-07-15 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab64ba0e-1648-336b-b96d-b39edefec627 | -9.44326 | -40.31907 | 2025-07-15 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e630d319-a031-34df-9ca1-483ee05b2c15 | -2.91522 | -48.2399 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a75cd3e2-d054-32f7-9617-a9ed6bd04fe4 | -7.27943 | -44.03619 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23fe8fca-865d-3f34-b496-c4d3132c09bb | -3.38007 | -47.46816 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d9df2ce-dafb-3e88-b7a0-b50871db6ad9 | -6.29606 | -44.23289 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f8106ce-e461-3b0d-b0a4-2ea7b8eaf041 | -6.63403 | -44.57374 | 2025-07-15 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7c09ab84-7251-3b41-897f-ed6bcbe4b180 | -7.09919 | -49.17555 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3be9ef46-ef39-3c24-80a6-b0ba30f11215 | -8.64563 | -47.75124 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 353c2e3d-168c-3e6f-9b89-06d31f989ed3 | -6.28843 | -43.41245 | 2025-07-15 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6a9399e-1367-343c-8838-0dde7c5d1cfd | -7.30551 | -44.53387 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1119910a-c2bc-3489-8faa-bd199318dcfb | -8.22964 | -44.91873 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41afc939-e1f5-383c-bfa6-4e3cd80c1643 | -5.79541 | -45.11663 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88e71123-bdd1-3807-9888-4a74e675969b | -7.8138 | -46.56348 | 2025-07-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36329ac6-fefb-3bcb-882b-801067614842 | -6.88729 | -47.02635 | 2025-07-15 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f97945-863b-3069-a48e-6721e6872295 | -6.38292 | -43.72346 | 2025-07-15 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 071c5700-c247-3d8b-9e47-f4f57a76da1d | -18.00692 | -45.75793 | 2025-07-15 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76ce24a7-2983-3e06-9eed-ca5de2c04ed6 | -10.87489 | -54.05918 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67325118-a128-3434-9072-bf4b75bee6e0 | -11.35937 | -48.72688 | 2025-07-15 04:34:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9f34e1b-8954-3799-afbb-40b42d294df9 | -11.90122 | -46.74616 | 2025-07-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be61f52d-bc84-3276-8c67-526529312986 | -11.43659 | -45.12626 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e10610dc-aa0f-3f77-b912-401bf18ef43a | -15.2249 | -46.97641 | 2025-07-15 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8197857a-eaa3-3938-899c-93b96928c2f5 | -11.4554 | -45.10278 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| af6518a2-bc5e-3832-93ff-75b3bcc8f0ce | -10.8807 | -54.04937 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dcfc5c9-22d1-374c-bb68-55456b0578d7 | -11.56065 | -47.3171 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5f18a9b-7ccf-3e3d-9ab7-2865ba146132 | -12.6219 | -54.22173 | 2025-07-15 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fc6bdca-e923-3765-9d41-bafbc55ea32d | -10.87429 | -54.06269 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41474410-6285-36de-9b0a-3c24dae37fef | -11.44413 | -45.12737 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| db229383-74ab-3c76-9c14-b513181b30b4 | -11.45269 | -45.09534 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 25333d35-be9e-370d-8ff3-98e638894266 | -10.57177 | -49.13505 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b5fb56d-27b3-3f75-b280-108b5523e172 | -11.4498 | -45.0876 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f3608f3a-b08c-3807-b899-e01536da3604 | -11.73602 | -52.39244 | 2025-07-15 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d58eda9-0b27-3d0b-8d37-b8a0e5ab0261 | -11.44915 | -45.09231 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 78eada87-6369-3416-bcfa-3069a80140d3 | -10.56736 | -49.1415 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9f3a5cc8-1456-36d3-bc40-481600565726 | -12.34453 | -49.31057 | 2025-07-15 04:34:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77fc9e47-ff61-327d-982d-3e279cb5639d | -12.07327 | -43.48145 | 2025-07-15 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 424e29b1-dd1c-3440-85d8-b22bee82a549 | -12.58251 | -56.98364 | 2025-07-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b03c95c-a635-3b11-a4b8-862a1abf487a | -13.04068 | -47.80779 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08c798d6-074c-36f7-8443-9d85853f4bdd | -11.46633 | -47.31768 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11db869b-a0c2-3093-985b-fec517fc6afd | -10.37899 | -49.89749 | 2025-07-15 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb668991-cb4c-3af5-a7e4-9a51a61bba87 | -11.46852 | -48.52781 | 2025-07-15 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1667c5ae-8682-3cb1-8fa0-5e72a82ef60e | -10.09792 | -60.50247 | 2025-07-15 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 101f3125-4126-32ff-8d12-e97c6f6b7766 | -11.44458 | -45.12497 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 1a31f760-56be-3b84-b30c-fc44b74e757e | -12.06818 | -47.98542 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8854ba3f-1abf-3d29-903b-f1d9494228a9 | -15.7493 | -49.64439 | 2025-07-15 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bbcc824-9fca-3d33-a8e9-1c44571fed1f | -10.96436 | -49.25231 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a9fde1e-36b6-3ede-8fe3-e0f7f4cd9b08 | -9.35612 | -58.83386 | 2025-07-15 04:34:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37493d9-5487-39dc-87af-d6b44c04fcfe | -12.6952 | -47.87223 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2665e40a-67ce-32cd-854d-acdefeaeaeab | -10.57067 | -49.14204 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 996b5c6b-9a51-34ff-b741-7d543cf4fcf2 | -10.62723 | -47.4697 | 2025-07-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 397a8987-8990-3a8d-9136-baf90dbf8a9c | -11.452 | -45.10001 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 13d021d8-0f5c-3363-9cd0-a6a5f60b1e62 | -11.44791 | -45.12791 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 70581604-a722-3000-ac50-96724941332e | -10.05371 | -59.10908 | 2025-07-15 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dcd8d76-0de1-370c-9013-616b6370921c | -11.45716 | -45.09115 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 89d7ff3e-603e-3431-bb32-337034295feb | -10.8795 | -54.05637 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 176db9d8-4524-37a3-8e00-5298fd288321 | -10.79039 | -49.25619 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52d76110-d780-3dab-8858-50f27c5a23a9 | -13.04633 | -47.81642 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23fb535b-b86f-3f4d-bf8b-4ddf5a07ce99 | -10.54403 | -54.25536 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1aab465-ff6b-3e02-8b16-56420242e6e9 | -11.45359 | -45.08813 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 4615afc4-de23-39bd-bfb7-ca67d0714766 | -11.90297 | -46.7585 | 2025-07-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b2a2f83-29ac-3e31-9f74-4f50456ec3dc | -11.73404 | -47.04762 | 2025-07-15 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed9cefff-999e-33e7-9c85-026c877e6f3f | -10.8853 | -54.04661 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fa837c6-42c2-3850-b7ea-6a7fb835d33c | -11.56122 | -47.31336 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7f30d0a-2824-312f-8176-39d17190d7f5 | -12.5778 | -56.9827 | 2025-07-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d86de16-456f-3565-ac81-d23c74591a2e | -11.45888 | -45.10577 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 396ac890-7aff-326b-b09d-781599c3d728 | -10.89636 | -49.20872 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3d2b158f-c9cc-3274-82fe-c6ea168bbc69 | -14.58667 | -48.11664 | 2025-07-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 286a6268-e578-3f58-a452-6cf7a38d188a | -10.56681 | -49.14499 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8cebdf61-d30b-375f-871a-93e87ecdc8cd | -10.8958 | -49.21222 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aa714c1-5594-3e2a-bbe6-005188f1432d | -11.45647 | -45.09588 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 4928f2d2-92d1-3b08-845e-77128509992b | -11.46117 | -45.08917 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| b82f8b5d-ccf0-3e9d-9439-931bdc1bb88d | -11.44328 | -45.13427 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ec05c6fd-7789-32ad-9dcc-6df05b1624ba | -10.54811 | -54.25602 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41224072-6718-3c5c-995a-89ced8b60f09 | -12.58155 | -56.98876 | 2025-07-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c33431c-f88a-37dd-9000-33d90825f201 | -12.69464 | -47.87591 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c756559e-6432-313a-a98d-219b0ba08442 | -15.74985 | -49.64082 | 2025-07-15 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2d96f10-6ae2-3803-87ae-c4e5eceb0f29 | -14.58613 | -48.12026 | 2025-07-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb8c542-a9d4-37a1-a5be-6a56fd6efe40 | -11.44959 | -45.0901 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 1db39fd9-4293-3087-991f-12dc232ba70d | -11.5263 | -48.96254 | 2025-07-15 04:34:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b62ee79e-0083-307d-8f60-16fbf402d6bb | -12.70617 | -46.7976 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7310676-5be1-38c2-8d25-7b7e60046c64 | -11.45918 | -45.10333 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a1b06992-b764-3886-8075-457a2023f379 | -11.561 | -47.31589 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6780e30c-adf6-32ae-8a58-a0336149b103 | -10.45348 | -49.5795 | 2025-07-15 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 629271c2-611d-3746-bb66-102e6f7676f1 | -11.36268 | -48.72741 | 2025-07-15 04:34:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f80412ce-3502-31f6-9b1b-86eec700d720 | -11.4652 | -48.52728 | 2025-07-15 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
