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
| 4d491fbc-6439-308e-8654-d1c68b71509b | -6.7829 | -44.083401 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5c078c7-883f-3394-a586-0041bed6e7a7 | -7.4099 | -42.042801 | 2025-09-04 00:04:00 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d0481cd-66de-3cdc-a2ad-a534214c8077 | -7.9307 | -44.9356 | 2025-09-04 00:04:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4e18b53-4053-3f68-8c5d-f2bc527a509e | -11.5932 | -47.7659 | 2025-09-04 00:04:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68f8d507-5f97-3eea-8e2e-4a8ff6bb97ec | -6.5353 | -43.102001 | 2025-09-04 00:04:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f54dd21c-acd2-3dad-8da5-ee1e474fdbb5 | -8.068 | -45.337101 | 2025-09-04 00:04:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f34acf5d-61ae-3f9f-810a-dece696a7902 | -3.813 | -44.115898 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e93b2bf-4770-3f87-b78f-54394d48a0ed | -6.2703 | -39.688099 | 2025-09-04 00:04:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d5d2fcd8-7ddf-3c8e-b306-77360adf5fdf | -6.2719 | -39.694901 | 2025-09-04 00:04:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6057de86-36c8-38e4-be54-4a225e5e4b55 | -9.489 | -47.604801 | 2025-09-04 00:04:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f7c8326-5eeb-339e-910d-3894c56d7c3a | -5.6992 | -45.167198 | 2025-09-04 00:04:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b41b66e7-8c25-3ae6-91a9-25088cd55503 | -6.726 | -42.250099 | 2025-09-04 00:04:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6413ec9f-07b0-3a11-9b5f-3737add2a1e7 | -10.4496 | -50.352699 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c12cb4d-1312-3619-b549-c44113cb7ce3 | -10.4439 | -50.323502 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2dc845c-01e6-3767-87ed-589ca02e5750 | -2.9505 | -49.360802 | 2025-09-04 00:04:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bec0e00-c019-31a5-9ae3-acd8f2c33369 | -8.0244 | -44.043999 | 2025-09-04 00:04:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e54bfd10-91cb-35e5-a935-7574cfd68b71 | -5.5332 | -43.768398 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c625a642-5b9c-347a-ab4a-c87e4b4ddafe | -6.5445 | -42.9585 | 2025-09-04 00:04:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a784a6b-1fb8-3a44-8a7c-ea5cf4fd801e | -3.4811 | -43.3288 | 2025-09-04 00:04:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bcc2072-3ee4-3a95-8c8b-038f018c7e49 | -6.7948 | -44.091 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65021645-313c-3c53-831a-df37b2e1b13d | -7.9282 | -44.924301 | 2025-09-04 00:04:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| efad0d3b-e4b9-3361-ac5c-73f8e7c74e9e | -11.3798 | -43.566799 | 2025-09-04 00:04:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 039f4f3c-52de-388a-980e-a4b133468561 | -8.3523 | -48.329899 | 2025-09-04 00:04:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb1f3d2c-cee6-35e2-a60e-eefc6dfabc71 | -2.929 | -48.809101 | 2025-09-04 00:04:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4326d65-f5c5-3ad3-ba75-3f8a8de219e2 | -6.7144 | -42.2444 | 2025-09-04 00:04:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f523670-aa21-3e0d-8208-17d9478132fe | -8.358 | -48.308201 | 2025-09-04 00:04:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0b70ef9-3054-39f4-9c71-9866906319be | -8.0265 | -44.0541 | 2025-09-04 00:04:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c705be3c-580c-3943-88b3-f6c053c22bec | -11.0536 | -45.1357 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2464896-126c-3505-80d9-a3c92aca7643 | -5.9679 | -44.1087 | 2025-09-04 00:04:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| accbd60d-ec48-3b6c-a482-375528cdcdf9 | -6.7709 | -44.075802 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4d78f67-0435-3404-84b8-5f764cbe378e | -3.8032 | -44.118099 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71b02745-4d0c-3851-873b-d4ea08458027 | -8.009 | -44.7775 | 2025-09-04 00:04:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c650044-62d3-31d5-9232-381fc275a363 | -6.7295 | -42.265701 | 2025-09-04 00:04:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 185ef928-9a6b-3286-af35-fcaea73daaec | -8.0287 | -44.064098 | 2025-09-04 00:04:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3966e006-6e11-3592-958d-fa61429ad298 | -6.7863 | -44.425999 | 2025-09-04 00:04:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a3657be-c94c-3940-b9df-881682147b21 | -5.0867 | -44.8997 | 2025-09-04 00:04:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abd3e13d-8076-3119-a4a9-6987a838dd26 | -5.7929 | -43.228401 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15d6efa4-8fd8-3ce4-a9dd-894128f2a429 | -11.3864 | -43.5984 | 2025-09-04 00:04:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96c3ecb0-fe52-3307-b6b4-4260a33b538e | -4.6111 | -41.408298 | 2025-09-04 00:04:00 | METOP-C | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1a5608aa-0df3-3214-a003-465282aa22bc | -11.1256 | -44.646198 | 2025-09-04 00:04:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f84cdd84-5503-3c9a-a790-1ecd91029b4a | -5.6944 | -45.145401 | 2025-09-04 00:04:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d606479a-7133-3963-94d9-2ccb9dced8bd | -5.3431 | -45.085701 | 2025-09-04 00:04:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92179c62-6a3f-333b-bb66-eaabe1c0ce31 | -6.793 | -44.4566 | 2025-09-04 00:04:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb755df-1ddf-3348-9571-fcd8023b8734 | -3.7447 | -40.412701 | 2025-09-04 00:04:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a44ae3dc-fb44-31cc-bf02-053eb2782599 | -10.4593 | -50.350899 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a04d854-f025-3a1c-a58f-b7e88cd94b3e | -3.7934 | -44.120201 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d386800f-9364-3e36-b8cf-7b6e73340abb | -6.7885 | -44.436199 | 2025-09-04 00:04:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7868a460-c271-315d-9283-77e57b9f9d5e | -11.2293 | -44.950802 | 2025-09-04 00:04:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff21cc93-6e63-3e57-8dbe-673ebf9b9fba | -10.4343 | -50.325298 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61b1de6e-afcc-36a2-86b5-0ef86d5837cd | -9.4695 | -47.6087 | 2025-09-04 00:04:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a954fd8-0921-38a6-a867-2e0d53281d35 | -7.9331 | -44.946999 | 2025-09-04 00:04:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32b5e657-d954-3b0d-b97b-96054dbab0c3 | -6.7809 | -44.448502 | 2025-09-04 00:04:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae194aab-ff0c-3266-94c9-1dbd9d06c680 | -4.5123 | -41.971699 | 2025-09-04 00:04:00 | METOP-C | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0621b799-dfb6-3d0f-80d5-e42de1a3c745 | -5.5528 | -43.764198 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3aac7bb9-4240-3fc1-b412-637c5eecc3e5 | -12.9997 | -42.470299 | 2025-09-04 00:04:00 | METOP-C | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9e7845aa-380b-3722-90fa-86ee8b1afe20 | -5.7831 | -43.230499 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f08cd5b8-c869-3840-aee1-d3c432af54bc | -11.3918 | -43.575199 | 2025-09-04 00:04:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d58dd7e4-a665-32e0-bcda-a1a95bc6478d | -11.0502 | -45.415699 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6a4141e-304d-3c96-b052-2166ec1e34f6 | -8.445 | -45.094299 | 2025-09-04 00:04:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cb562814-f36a-3224-8350-75d938ebf6d2 | -6.7807 | -44.0737 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 141e1772-e802-3533-850d-1b79caecae0e | -11.2417 | -44.961601 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55772b40-4538-3524-85ed-91300a56725c | -8.0246 | -44.139198 | 2025-09-04 00:04:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 08a40ef4-4bcb-3d39-9a72-4dfa4ea72f8d | -11.3842 | -43.587799 | 2025-09-04 00:04:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 766efff6-3bc1-3347-b9ab-67eaf6048c5c | -5.4767 | -45.226601 | 2025-09-04 00:04:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbe67042-31ef-377d-ad9b-2cdddbc411bb | -13.7422 | -46.938599 | 2025-09-04 00:04:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 80efe0ff-db27-34e4-aaf8-4b4bac8a5443 | -9.4793 | -47.6068 | 2025-09-04 00:04:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 421be91f-8f1b-3562-8f1d-4cc409fa040c | -10.4303 | -50.3564 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d6de875-67b6-339f-acbc-bec915902084 | -5.543 | -43.7663 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1550189-dfe6-3f72-bf11-eb2c4bb82187 | -3.7914 | -44.111301 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f47b151-923b-3c66-bb85-921554fe3492 | -3.4297 | -42.466 | 2025-09-04 00:04:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| a00769d0-4979-33fb-8937-6f7e3b07f658 | -9.4755 | -47.588501 | 2025-09-04 00:04:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db0e2526-9a3f-3eec-801b-03951fff729c | -6.4494 | -42.392899 | 2025-09-04 00:04:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f054f0d-536e-302a-9edd-8dc3e1bc94b1 | -7.4936 | -44.806099 | 2025-09-04 00:04:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97b18f8d-c469-3a24-aefc-26ecc22cbece | -11.1231 | -44.633999 | 2025-09-04 00:04:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52ffa656-677e-35a5-b09f-2e1ed827841a | -8.362 | -48.3279 | 2025-09-04 00:04:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c8cb7d4-a437-30a1-a08f-e997c420034b | -10.4457 | -50.383999 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5622b6a-bf42-3bea-87af-118fc40a4105 | -2.9462 | -49.341702 | 2025-09-04 00:04:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0586dfb-338f-327c-a696-28b861a36e3e | -5.97 | -44.118198 | 2025-09-04 00:04:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f037672d-5c34-3b80-895f-7ed4cdd21784 | -2.9602 | -49.3587 | 2025-09-04 00:04:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1659ca6-9ee3-30fc-a295-129bc51082ff | -9.4658 | -47.5905 | 2025-09-04 00:04:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02b372aa-6a71-33ec-a285-59799de17795 | -4.6095 | -41.401299 | 2025-09-04 00:04:00 | METOP-C | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e332723-e856-3bb6-954e-0ccac5e87d45 | -11.3776 | -43.556301 | 2025-09-04 00:04:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4889b05d-cf23-371d-99f7-2163c832f825 | -11.0563 | -45.1488 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10f476d9-e45d-3ea2-bdee-41426bdf00ed | -13.4493 | -46.936001 | 2025-09-04 00:04:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5d95e198-5b04-39cc-9be7-db39ee0542fe | -6.3769 | -39.252998 | 2025-09-04 00:04:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 30e673e9-5fea-3678-b2c9-32f146685274 | -10.44 | -50.354599 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b08451e3-84c0-39cb-9a44-b94c9c261390 | -4.1651 | -42.985802 | 2025-09-04 00:04:00 | METOP-C | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 417ea50d-2207-36e1-95f2-2bd780e26739 | -3.8052 | -44.126999 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e006d1c6-3547-37da-9838-20d9bc31613c | -11.3896 | -43.564701 | 2025-09-04 00:04:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18e109df-1b1b-3f68-9ec3-b8e7d6b60839 | -12.4944 | -48.049301 | 2025-09-04 00:04:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb27ab8d-f6a5-3764-80c2-f712c7762eed | -6.785 | -44.093102 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 620c3fbf-5160-33a0-b74a-00938d308b2d | -3.7954 | -44.129101 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc5874c-8951-385d-bef9-a3ed0f07e9b2 | -6.7242 | -42.242298 | 2025-09-04 00:04:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1dca645f-89d2-33d6-8d7d-d65b1b34843b | -13.7458 | -46.957802 | 2025-09-04 00:04:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 65e6a60a-99a1-3d9c-83d7-1bc1c5faeadd | -9.0679 | -46.988499 | 2025-09-04 00:04:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f45b08c7-1e3c-3f07-85b1-7f189f4fe279 | -8.0148 | -44.1413 | 2025-09-04 00:04:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6ecb1cf-c6c2-34b8-9fee-3bfe6639dae7 | -6.7654 | -44.097401 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd1eca9a-2ac7-3c99-b720-4512c956a29c | -5.791 | -43.220001 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f298a1b-d67d-3c62-82ed-89a869b0fe7e | -9.6148 | -47.032001 | 2025-09-04 00:04:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3a856e-51e0-345a-813a-927f67c94a5c | -6.7832 | -44.458698 | 2025-09-04 00:04:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
