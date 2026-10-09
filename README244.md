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

## Dados Diários - Página 244

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6de9c3c7-15be-3c6e-9986-8d5dd92a7910 | -12.2145 | -44.6291 | 2026-10-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| c2256269-b19f-39cc-b262-d7a0d26cc58a | -10.4727 | -47.211 | 2026-10-09 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 86fe3732-08aa-379a-8f75-b5ec8d056557 | -9.183 | -43.3688 | 2026-10-09 14:30:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| d2800ddf-7e7c-3194-9de8-b194d510a01a | -1.4569 | -54.7761 | 2026-10-09 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 88a3e6a5-5440-39fe-8665-24c404a44b6a | -3.86 | -44.1274 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f7052d04-cb3f-350f-9694-24d545f29e19 | 3.128 | -60.613 | 2026-10-09 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 92da9c25-d48d-3ef9-a465-5525e0cae59f | -9.9798 | -45.9236 | 2026-10-09 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 592.7 |
| 30d124ef-af5b-3ab3-b111-cab14aa43b6a | -11.47 | -43.3824 | 2026-10-09 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| e306802f-99c9-3b39-9117-7e514d53d0e6 | -12.1725 | -44.8216 | 2026-10-09 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| fea0f1cc-45bf-378b-84bf-0b4fa8c11e25 | -14.4535 | -43.9359 | 2026-10-09 14:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 257.1 |
| 2c43501d-e09a-38dd-aae9-6dc51333ef2c | -5.7317 | -41.6829 | 2026-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 489eb840-cd04-35ff-9cd8-ce656531d1be | -1.4569 | -54.7562 | 2026-10-09 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| de5be91d-40a8-3f83-87f2-32561f8cb652 | -12.2123 | -44.7457 | 2026-10-09 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| e6d4566d-d705-320c-abc9-a01fd5c7b33d | -1.494 | -54.5363 | 2026-10-09 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e8353f15-17da-3ea0-bdb1-87c1b3ad9da1 | -8.9955 | -45.968 | 2026-10-09 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| ee49ef64-1330-3329-9606-0d66f30479b5 | -12.0054 | -43.4878 | 2026-10-09 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 29f5a458-4782-351d-bd6c-0861f0eac722 | -1.5306 | -54.5359 | 2026-10-09 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5c096349-0a56-371b-94d4-f8834371163b | -5.9647 | -40.9383 | 2026-10-09 14:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 154.4 |
| b317b96c-a345-3cf0-98b1-1d4352727d28 | -9.8629 | -47.4809 | 2026-10-09 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 45580287-817a-3ba3-8dc0-699f136ee98e | -1.5123 | -54.5361 | 2026-10-09 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| af0e3039-d730-3783-b015-5e963c46046c | -12.2504 | -44.7631 | 2026-10-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 40b68fde-f678-3a67-976e-2876be2a6f6b | -10.4724 | -47.2333 | 2026-10-09 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 164.3 |
| dbf9c355-28e6-3a26-afcb-dc5026045b6b | -10.8313 | -47.3456 | 2026-10-09 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c60921f3-bd31-31d2-af97-44babb6584fc | -7.3243 | -43.9913 | 2026-10-09 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 4000fe2b-7839-35d3-8a8c-d8c03018e324 | -9.9208 | -44.7893 | 2026-10-09 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 6139393d-7d20-3938-9419-0c0b63bf8d83 | -14.3611 | -55.0114 | 2026-10-09 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 58ff78ea-2918-371a-ac66-be3c05a24f55 | -6.7365 | -55.1474 | 2026-10-09 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| ebed73e5-a710-3768-bf8d-7714737805b4 | -11.2068 | -45.3091 | 2026-10-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| c0232d58-9bb4-3b7e-8fd4-d03eeb0ed2bc | 3.0733 | -60.576 | 2026-10-09 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3ed3cc81-95d4-3fa3-bb09-cfe6fd710c95 | -14.0044 | -48.7743 | 2026-10-09 14:30:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 75e8d6bd-2f55-36ac-8744-2c6e82d6b301 | -11.6787 | -46.7664 | 2026-10-09 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 692dc7eb-d15b-3134-8af6-e1c33f125700 | -8.969 | -45.1313 | 2026-10-09 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 2aab426c-0b5d-33e5-9bbf-76efd318886d | -5.7466 | -42.0882 | 2026-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| 30505568-8c33-3dd2-b4c8-73286a5fc5e2 | -12.1537 | -44.8013 | 2026-10-09 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 421.5 |
| 68fc1e1e-0443-3580-a106-349f60e75b95 | -9.1015 | -45.1164 | 2026-10-09 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| fb215c91-8dd1-315a-bf07-cd9e1567d303 | -12.1964 | -57.1303 | 2026-10-09 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 33978d61-7a55-3567-94e6-cd3456985b83 | -12.1729 | -44.7983 | 2026-10-09 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 62647d3a-a1dc-33c9-9e3f-ed6e1798103d | -5.7131 | -41.6604 | 2026-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 097f108f-7240-356b-8ab0-f20d95942599 | -1.4194 | -55.3526 | 2026-10-09 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e217a131-def1-3908-aa34-36394a57b40b | -15.2541 | -42.3495 | 2026-10-09 14:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 273.4 |
| 4b3b8464-1c5d-3ef8-9e22-7d9d382175e8 | 3.968 | -60.9004 | 2026-10-09 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 83a793bc-96c5-3e24-8b9c-fd84ed5a520f | -13.709 | -49.1042 | 2026-10-09 14:30:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 45bc6880-0e3b-360c-b294-a392939ff396 | -12.211 | -44.8156 | 2026-10-09 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 9727f30d-bb25-3f7a-8bf8-42994f5e9a58 | -7.4097 | -44.7427 | 2026-10-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c9e94cc0-8753-3416-a318-d50f56f27686 | -7.4886 | -42.8295 | 2026-10-09 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 142.3 |
| 6289bce1-e5f0-35ae-adda-35cfc58e14ce | -7.7213 | -45.4418 | 2026-10-09 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 4375157f-f589-336c-9ce7-4d89202474e0 | -8.6703 | -44.8669 | 2026-10-09 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 474a272d-abf9-3c5e-ab55-bf99c8f54e93 | -10.5091 | -47.3179 | 2026-10-09 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 7a870581-ef64-34a2-8bdc-adba8c2295ac | -11.8783 | -47.3892 | 2026-10-09 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 501.5 |
| 3a00b693-9e69-3f27-b101-176ec9eb1579 | -9.9794 | -45.9462 | 2026-10-09 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 551.5 |
| 5ec94df9-7f09-3ccb-82b2-2eecf7e3b56e | -5.7654 | -42.0866 | 2026-10-09 14:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| 4f652887-600d-35e6-9382-a59aa59e6eb9 | -12.2343 | -57.1271 | 2026-10-09 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 204.8 |
| 22de7ee3-fa34-331f-92e6-c7f926ac96c5 | -5.7312 | -41.7309 | 2026-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 32da0710-52ce-3405-9471-28555ae31fe9 | -10.4334 | -47.3046 | 2026-10-09 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 7ae2b1e1-7956-3c30-a1e3-5aaa213c9d77 | -4.0835 | -44.1618 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 1d7a03e9-be3b-3b19-989c-5b39e9999a4e | -12.2508 | -44.7397 | 2026-10-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 68e7e1e7-1e05-32fb-800f-dc51adff3427 | -8.5124 | -46.9128 | 2026-10-09 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b26596a0-ae9f-3406-9424-856fbcaf2793 | -3.8788 | -44.1035 | 2026-10-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 74f12e91-e04d-37ed-9569-c167794eca1a | -8.0575 | -45.6357 | 2026-10-09 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f6637093-b0d4-31fb-be7a-46b525df68c8 | -14.3415 | -55.0341 | 2026-10-09 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4c95eaf9-8e3c-33eb-991b-2be907c5f89e | -14.0238 | -48.7714 | 2026-10-09 14:30:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 189.6 |
| f00c3110-34df-3ec5-a7dd-761be957aa25 | -12.0063 | -43.4402 | 2026-10-09 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 360.4 |
| d7c0f8e9-0313-3588-85dc-f826558f1caa | -7.4889 | -42.8059 | 2026-10-09 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 5538ad58-28c0-3a38-8f83-dac76727445e | -5.7505 | -41.6814 | 2026-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| ccbc138f-38e1-30ac-9159-ee42c72f08b4 | -10.8983 | -45.5114 | 2026-10-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 846.7 |
| 835eac82-a5c9-3d6d-a51a-a14593093354 | -5.9649 | -40.914 | 2026-10-09 14:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 135.0 |
| d0b72153-d970-3366-9923-5c628b239c52 | -11.3371 | -46.6547 | 2026-10-09 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 3c6fc364-fab7-33b7-8670-d276ab1d0cad | -8.6551 | -54.5291 | 2026-10-09 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| abe552cc-e3bf-3c5d-8b2b-0a2139147519 | 0.5246 | -50.8991 | 2026-10-09 14:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7ac8d3d4-021f-389c-98bd-7a9acfb6d5fc | -6.0024 | -40.935 | 2026-10-09 14:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 198.6 |
| 14fe8916-adc9-334a-b339-cf216d717683 | -7.4697 | -42.8315 | 2026-10-09 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| a1fd69a9-968f-3df7-bf7b-0bf5663e2038 | -6.9328 | -43.6799 | 2026-10-09 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 118f2488-a05e-3893-bb1b-41ed3b910f42 | -9.8986 | -50.49 | 2026-10-09 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 79e25e93-3eec-3ad9-88ed-2d4bcb5c9586 | -10.4914 | -47.231 | 2026-10-09 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 78663eb7-4d65-359f-8cd2-8d24a1e82a28 | -6.755 | -55.1465 | 2026-10-09 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2f178aed-eaa2-32df-b79c-cdae251dabff | 3.6212 | -60.6989 | 2026-10-09 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 19225cc6-b4aa-32d4-a31e-cf09e1e29a34 | 3.5646 | -61.3435 | 2026-10-09 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9df2505f-25a0-3d5e-8a2f-4ee62c8715d4 | -10.3735 | -46.2372 | 2026-10-09 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 211a3c4b-4062-3c95-bbba-919d0114e208 | -5.7133 | -41.6364 | 2026-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 7c0e89c7-2fa0-3c44-95f3-91e68ad44231 | -8.9958 | -45.9454 | 2026-10-09 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 9d7ca941-c637-3ca2-b851-266eff5f2551 | -4.4979 | -43.6083 | 2026-10-09 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 0f64c63d-aae2-38fe-bf00-73d1d95549c1 | -6.9684 | -43.8624 | 2026-10-09 14:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 31acb88e-7ebb-3275-a42a-ebe3fb069fa4 | -9.0826 | -45.1186 | 2026-10-09 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| c088b0d0-0bc0-380b-b88f-2463d98492c5 | -2.8491 | -49.8763 | 2026-10-09 14:30:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1e7ad2aa-1f9a-311d-b537-f9bb0445e031 | -11.318 | -46.6573 | 2026-10-09 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| b1625ba7-c738-3b13-b410-6bfd57ba46cd | -1.1094 | -54.1802 | 2026-10-09 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8a2a38ee-7e7a-3bea-b062-e52d8ec76bef | -12.1537 | -44.8013 | 2026-10-09 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3784be28-cc2f-3de7-89c9-d043be65148b | 3.9875 | -60.5014 | 2026-10-09 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| fe1d15ed-c7b8-3cb0-9ef8-4dead1eb7fab | -9.718 | -45.6828 | 2026-10-09 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| c8413f07-7ffc-335b-8466-dee0ef67b9b1 | -1.3829 | -55.2142 | 2026-10-09 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 59756c4f-1514-3aac-b9e0-5b59f998ed8b | -12.2307 | -44.7894 | 2026-10-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 2f03e2fc-d5a5-36c1-8c5b-bf7fdd98b34b | -1.4753 | -54.756 | 2026-10-09 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 63e8dde0-a9e2-3435-a7b4-b5d61ab25c1a | -1.5306 | -54.5359 | 2026-10-09 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 2ec2645d-aaa4-3779-a145-989d9b6ea7e8 | -12.2123 | -44.7457 | 2026-10-09 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0efebb66-eae8-3abe-9ec5-6e85d245d832 | -14.3611 | -55.0114 | 2026-10-09 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 71eb30f9-74c2-3001-bf2c-aedb88ca4377 | -9.9794 | -45.9462 | 2026-10-09 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 468d2227-4cea-3044-9cc5-7aa553426308 | -12.1549 | -44.7314 | 2026-10-09 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| a04337c9-5421-3c87-bda6-b862b1c28adb | -8.6551 | -54.5291 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9d56f30e-bb97-334c-b6cc-191d37de8dd7 | -12.2508 | -44.7397 | 2026-10-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 159fd052-28c9-3c5c-8f6b-77de0bb16c17 | -10.9953 | -45.4068 | 2026-10-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |


[Clique aqui para ver as próximas entradas](README245.md)
