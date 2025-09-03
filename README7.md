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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f6d46b9-b3cd-3711-8d04-91cc004a7347 | -9.6439 | -47.850601 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1b73048-7da5-3678-a9c4-0bcce4744f5a | -4.1525 | -46.7896 | 2025-09-03 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81cce20f-ede1-31b4-aa5e-b36452e532bb | -5.9357 | -46.475601 | 2025-09-03 00:24:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 593fab7b-6dec-3f63-aeb3-b013fc2e672b | -12.8323 | -48.064098 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f09a1cd6-71f5-393c-8997-c7ea6c4614b7 | -8.0547 | -45.368599 | 2025-09-03 00:24:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f35d8b8b-7d6d-3cbb-b8ef-11b1ae90fe7e | -7.926 | -46.536201 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 754eccd0-2165-363c-9fb1-9347592c57d1 | -6.5057 | -42.185501 | 2025-09-03 00:24:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69ef9ff9-2988-3b14-8504-38e613a601be | -8.0156 | -44.065601 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01b9c096-f97a-3398-841e-4f664340ba60 | -4.1509 | -46.7826 | 2025-09-03 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc0f95ad-d0c0-3362-91c9-c63afddb807c | -5.6116 | -45.006901 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2a95421-2017-385f-8f5e-21f909e0d551 | -6.3673 | -43.007 | 2025-09-03 00:24:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b587b66d-ed47-3d1a-b54b-391e9d980f4e | -12.4355 | -48.7089 | 2025-09-03 00:24:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e76ad53c-4648-39d6-bae9-09ff3fa7800e | -9.747 | -46.912601 | 2025-09-03 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9620c749-30c4-389d-9588-1e3a84f76df0 | -9.1621 | -45.208099 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc1969e7-2a9a-3cf3-9adb-3bb80edb5035 | -6.5716 | -47.3801 | 2025-09-03 00:24:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2bbe157-cdff-39dc-935a-02502aca4330 | -10.7293 | -44.803501 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0521e18d-e0dd-3ce8-b2a3-c3720caf7cee | -11.5747 | -52.0756 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca67b01-5ccf-34a4-a64e-2c383bab1c7d | -11.5879 | -52.091099 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9906558-36c2-335d-bec5-cc15c113f7d6 | -10.9561 | -44.2094 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 806a9ef7-3d25-350a-9040-18b810bba72e | -5.494 | -42.6255 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16e15e76-d8a0-3a5b-a1d4-d3dc0d582997 | -10.4717 | -50.349998 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbaea0e0-b65a-384a-9932-2f08f61a2673 | -11.6101 | -52.0504 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f91717c7-7cf1-3a35-844d-bc95413a58a8 | -12.5946 | -48.198101 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e28bff61-16ab-37be-810a-9df519846342 | -6.9992 | -43.2388 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 611bcc58-b7c4-3f91-99dc-fade594444b3 | -7.7007 | -48.721901 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9c33a6-fdc0-38a5-9215-f104e9c0077a | -6.6938 | -48.390598 | 2025-09-03 00:24:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b10e8981-48b5-3801-bccd-94312b108ab0 | -7.284 | -45.2868 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf2883fb-98c9-342b-9672-d204cbdab127 | -7.8867 | -46.452202 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5efe936a-6ee1-330a-82dc-bef86295fcf9 | -5.9059 | -46.617199 | 2025-09-03 00:24:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 228dc31d-87c2-3e35-a732-e30c588aa592 | -11.271 | -40.4566 | 2025-09-03 00:24:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 31d6d4e0-da5b-348f-8a26-443c978543c4 | -11.5914 | -52.108601 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 330784ec-f3d0-3b49-9dda-cbe82cfd2a98 | -13.73 | -46.930901 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b41798f-f7e7-3ab4-a004-deacb7f2db2f | -11.4435 | -47.306198 | 2025-09-03 00:24:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04f9b7ff-2a27-3c90-be23-7dc0c981851d | -15.5853 | -52.660702 | 2025-09-03 00:24:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99c1f5c1-d359-3316-816d-c405b8e2439f | -10.91 | -50.845699 | 2025-09-03 00:24:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 109cc632-4bf8-3b28-82d5-8e9749b00f4a | -13.6987 | -46.928398 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3b7787-4b14-3042-9bd4-03adfff3b9e9 | -5.777 | -45.278702 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af26933b-00c2-32c0-8864-96de32768240 | -7.0102 | -44.359299 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1773cd1c-9e4c-3401-8422-76cc47400704 | -11.3863 | -46.850399 | 2025-09-03 00:24:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd10c70-d33c-3be9-80f1-1ecf719347b8 | -4.1623 | -46.787498 | 2025-09-03 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d364b0b9-ff24-31d2-ba1f-6cc0eebf168e | -5.5038 | -42.623299 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb22b317-1c8c-3412-a3f6-8d59adad5337 | -7.0086 | -44.352501 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1864899f-bbbf-329b-998c-8a5bae533a04 | -20.403799 | -45.6861 | 2025-09-03 00:24:00 | METOP-C | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dbdda831-ee34-3fa5-bbcb-64e4590a94ed | -12.4946 | -47.479401 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62298927-6ae5-395b-b663-1e4e4cf363ed | -11.3829 | -43.636902 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6296ec42-cead-374c-a03c-e4cf0c362329 | -6.2717 | -44.512001 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df9be4c6-53ad-3687-99f7-53f0b50a7a53 | -11.1481 | -43.647099 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc1186c2-678a-3aab-a54d-f1f302f4e906 | -11.1171 | -45.110298 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d14417b-561b-36e1-89f7-fba91a529bf5 | -5.4373 | -42.912998 | 2025-09-03 00:24:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a364b62d-2890-3d47-bbc8-a7be305f2c8e | -7.6154 | -42.648899 | 2025-09-03 00:24:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 98eccb9b-91b6-3d35-9091-9359fcb03a4e | -11.1139 | -44.635399 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4568b300-34c0-3615-b9b9-0a999afd8e94 | -5.6213 | -45.184399 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d2b750f-63b3-31e9-8a52-2b445ff26449 | -5.6908 | -45.940899 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81121572-0323-3a73-a858-fa68d48cd9d6 | -11.4398 | -47.288898 | 2025-09-03 00:24:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9e4ef80-6dc3-399b-8785-82ad6f2b2929 | -5.8081 | -43.220501 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48d7397f-52b0-3201-adb4-9a59409faa57 | -6.8347 | -44.268501 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 146a90d2-96dd-3817-b77c-12d37bac5f41 | -9.4988 | -48.8876 | 2025-09-03 00:24:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e271f913-da56-30b8-bbf0-a20de25f0b1e | -8.0046 | -44.784599 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8dfa22cf-a735-3444-b437-53fb1c280994 | -5.7033 | -45.137199 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54d231b3-41b2-3b6c-a6bd-6d6dab8b916b | -11.5852 | -52.128201 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b020a14a-4cc2-3836-b74e-ff72abe3a200 | -7.7146 | -48.738201 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1dcd55f0-6a89-350e-9eb5-c9e07aabf440 | -7.9342 | -46.5266 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d75a4edc-c41b-3139-aaee-9b51a057cf37 | -6.7274 | -42.2505 | 2025-09-03 00:24:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08ccf3f9-5a2c-3f62-9087-7094561f6918 | -11.1056 | -44.644699 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6359a379-4115-3571-afb0-e0cce44771b4 | -6.9975 | -43.231602 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d5dbe279-6ccd-34b6-8118-f904ecf0ca4a | -10.1209 | -47.449299 | 2025-09-03 00:24:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 488d98d2-75ea-3a4b-be34-a5cbb47fc074 | -4.0195 | -49.755001 | 2025-09-03 00:24:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f8d7677-582d-3116-b184-d90ed23369c1 | -14.9702 | -50.188702 | 2025-09-03 00:24:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4bc55c2e-240d-38be-aa21-2e48fe7e234a | -9.6341 | -47.852699 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 884a6a9f-645f-386d-9afb-420c91be6675 | -10.127 | -47.430302 | 2025-09-03 00:24:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e73cc4f0-394e-31df-9cf9-0e92ec013d96 | -12.8792 | -48.0438 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5175362f-1b9f-33e5-be75-c3da37bf74d3 | -8.8776 | -45.821499 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ef5a17f7-411d-3d16-a78e-4aa3a9dd0a61 | -5.5075 | -42.638802 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d808815c-edf4-3d18-ad68-088ff4715714 | -7.5291 | -47.431801 | 2025-09-03 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed16bd33-6d0f-3461-9799-8a379f187641 | -12.7967 | -48.0406 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f07b4116-3169-3b1a-b936-c87c6004f710 | -7.699 | -48.761002 | 2025-09-03 00:24:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b2396720-7099-3302-bfbb-129bcaff7687 | -6.8363 | -44.275398 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3153d28d-afed-35ee-9035-66d324451f8e | -8.014 | -44.058601 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be8d685a-2959-3de3-96dc-04cb2e176da4 | -9.636 | -47.8615 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c46d8960-ad8d-3847-9dff-9cd24d1810e0 | -5.4958 | -42.633301 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22c9d9ee-432d-3d76-bb05-6b59451b8cfa | -11.1072 | -44.651699 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1be051c5-ab36-3f3f-988f-02f25a89295b | -8.0532 | -45.361599 | 2025-09-03 00:24:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4436a6ca-1be2-38f7-8d0a-f669805619d1 | -14.62 | -48.926998 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be2207ca-36bb-31c3-950f-0922e724fbb8 | -6.8469 | -52.810001 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7cfd74e-3305-3876-af86-cf568bbbc3a9 | -3.2218 | -47.137699 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7be9ab0e-ed7b-36fd-8f5e-8ee9ba1aed13 | -12.4848 | -47.481499 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e1a5eb2-232b-3d75-a87b-067aa9d1d02e | -3.4072 | -44.258598 | 2025-09-03 00:24:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b879ae3-f929-36fe-9d1c-9b4d56c9c659 | -11.4417 | -47.297501 | 2025-09-03 00:24:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a99affa-4114-3e37-8a5a-f171d49275b4 | -11.1088 | -44.658699 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab0fe53f-32be-327c-ba3a-79f9819a8a3b | -11.3813 | -43.630001 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bab1378d-8ae6-3cc1-be67-3455e78cb7e4 | -7.9079 | -46.4552 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff2bc4e7-cd0c-3625-872f-d294691ea22c | -7.1309 | -44.570499 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c816d1d-f413-3640-8e8d-5f0b4e48b20e | -5.6229 | -45.1912 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c407b73-b0ad-3baa-8994-23e3df853ba5 | -10.2844 | -47.494202 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb9d945-1a81-3061-9ad6-4c62fe8931fb | -6.6883 | -44.170799 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 797496ca-0af1-3cae-94ff-bb1ab87b4148 | -6.2504 | -42.6381 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 679b868d-f7d5-3ba3-a5c5-aae49b1b5344 | -7.9063 | -46.447899 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c253227-c712-3543-82ec-39b44785fbdf | -10.5393 | -50.43 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55347b3c-107f-3560-8866-a6ee1e3cedff | -20.395901 | -45.6978 | 2025-09-03 00:24:00 | METOP-C | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3470f6-25b6-3cdd-878a-34186bf11869 | -11.572 | -52.112499 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
