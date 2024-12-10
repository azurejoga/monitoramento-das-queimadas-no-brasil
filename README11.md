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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad6b9ad9-e3ac-3365-b875-baad2ae5e518 | -4.49849 | -44.31996 | 2024-12-10 03:36:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7ce65a7-80a7-3501-b7f5-0c059cad9cbb | -5.33527 | -45.11475 | 2024-12-10 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e30b3d7-c3f6-35ed-a775-7f2cd840821e | -4.49766 | -44.32458 | 2024-12-10 03:36:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85e3d665-ea79-3ae2-82e2-e1076e0ba32a | -6.91804 | -43.51401 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d6d0ecd9-9ad3-394a-a86a-9e9c9fda032c | -5.29147 | -44.91173 | 2024-12-10 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c5e7604-3aab-3de3-880b-672cb3e72ef8 | -6.26607 | -43.55783 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a152c487-7f9c-3cc4-9aa1-e0db09780ddc | -8.80292 | -35.65782 | 2024-12-10 03:36:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7992bf31-96dd-3a2e-96f8-70426149d00c | -9.03983 | -36.1089 | 2024-12-10 03:36:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40f43ae7-0732-3ce4-89b1-d60c0b2bc060 | -10.71327 | -37.60825 | 2024-12-10 03:36:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1996673-1d28-3889-8cdf-ca1e18625b2b | -6.25482 | -43.55569 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 829db66a-5ea0-3e6e-9b62-6eabb9009db4 | -10.44287 | -44.89328 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b003c84-2ea2-3482-b9e5-d8e232adbf7f | -5.62514 | -44.83543 | 2024-12-10 03:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9723be53-6be1-3493-8360-0135e751f755 | -6.58541 | -38.45346 | 2024-12-10 03:36:00 | NPP-375D | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74244718-7f9f-326d-a60f-951cb38d6e45 | -6.83682 | -44.38954 | 2024-12-10 03:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a2ec3873-90f7-3c07-af8c-d6ebb44ce076 | -10.69685 | -37.05035 | 2024-12-10 03:36:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa16b9f6-6263-340f-933a-b12dee23a422 | -6.00857 | -35.37332 | 2024-12-10 03:36:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b8e370f-3053-3993-a060-4473cc7e9703 | -10.75427 | -37.83337 | 2024-12-10 03:36:00 | NPP-375D | SIMÃO DIAS | SERGIPE | Brasil | 2807105 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 36c193fa-1e81-30fb-8203-c716e55af037 | -6.96161 | -42.98925 | 2024-12-10 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c3ddaf4-ae8f-3067-b2ac-dff884fed76f | -4.70562 | -43.79234 | 2024-12-10 03:36:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f194ef7-0684-3793-9d04-e950d9f6341c | -5.33986 | -40.85884 | 2024-12-10 03:36:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c6997339-a8c1-3340-b972-2e4caf2e00b7 | -5.7163 | -46.55155 | 2024-12-10 03:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b44046f3-e509-398d-8766-a7facdaef7a8 | -4.49055 | -43.85096 | 2024-12-10 03:36:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f34cbf3-f7cf-33dd-9b1f-d2b49c5431c5 | -6.83096 | -44.38827 | 2024-12-10 03:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8854bf6c-6cc0-395f-9097-f58626061526 | -4.49752 | -44.32439 | 2024-12-10 03:36:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11aecc70-9ebd-3be3-b831-c0f9a8b0d211 | -7.75473 | -35.13446 | 2024-12-10 03:36:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| dc9bc580-37a5-3940-9893-616f27dbb935 | -10.45304 | -36.78127 | 2024-12-10 03:36:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d8291abd-b47a-36a1-b7a3-912a5f85b6e2 | -6.94816 | -42.84806 | 2024-12-10 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f74ac79-ac34-396f-97e1-cf52e111342b | -4.48463 | -43.84993 | 2024-12-10 03:36:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ab1ac9c-b8c7-3a82-96eb-e98fd4d3b067 | -5.34566 | -39.3483 | 2024-12-10 03:36:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c71d46d1-a76c-3adc-9973-8dc4883aaddb | -6.26041 | -43.55693 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c79135a8-3a62-333e-ae50-b43c44adc6c7 | -7.0715 | -39.05229 | 2024-12-10 03:36:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 57d56be9-2f6e-3ee0-9d95-048e6ee912ca | -9.4104 | -36.00491 | 2024-12-10 03:36:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c8546ab8-486a-3c45-b51f-9249eea92fbf | -5.87653 | -40.16005 | 2024-12-10 03:36:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e74ac6d-4798-39d4-ab20-ad498b043161 | -6.39861 | -35.20438 | 2024-12-10 03:36:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 53a8ccd7-59c7-3e66-954b-8f315fd3cbd4 | -6.91314 | -43.50937 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a1a7473a-5290-322e-8e8c-c293dff493ce | -9.76438 | -36.21446 | 2024-12-10 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f8e4134e-195d-37d6-92c1-4e21ff7f1056 | -6.73312 | -46.29206 | 2024-12-10 03:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 387d76c4-acc4-3334-b76a-eb527b8656ec | -11.17492 | -40.36142 | 2024-12-10 03:36:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d116ec24-d565-3789-8bd1-df7b2737950a | -6.91437 | -43.51439 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1cadb1d4-d516-3386-b195-11c84ffc7698 | -6.967 | -42.99011 | 2024-12-10 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74365dfd-1e57-3a1e-86ba-679521ed1839 | -10.4486 | -44.89431 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ea56b39-39cf-3e36-8825-ac09a9f3f676 | -6.91308 | -43.52182 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b54b0b37-899d-3968-b25e-8984147af76c | -6.91372 | -43.5181 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b959ee93-6d63-34ec-817b-3a107ccb19c8 | -7.96431 | -40.01826 | 2024-12-10 03:36:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c58b36b-c175-3911-acf8-69f8cf338e8b | -6.94285 | -42.84705 | 2024-12-10 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf52a26e-3306-386c-88ad-605d939a4c4d | -9.76095 | -36.21389 | 2024-12-10 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 0cd10391-558a-3e8b-8637-9bc152d73d35 | -9.03592 | -35.70695 | 2024-12-10 03:36:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7af77f22-deb8-31e2-8f86-aa07e80bd67d | -8.18769 | -35.28808 | 2024-12-10 03:36:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c11a3c86-f895-32bf-b7de-f2b4f94fb49d | -5.63051 | -44.84105 | 2024-12-10 03:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9ce82056-f26d-3409-aebc-41a22c8b21da | -7.07211 | -39.04865 | 2024-12-10 03:36:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ddaa60b6-ee4b-34b6-b930-6f9a3d1a85d3 | -9.93553 | -36.45107 | 2024-12-10 03:36:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 43dc34bc-e454-3a7d-85d1-5cb8186c7b26 | -6.26352 | -43.55898 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92e6975f-ef6d-3812-bbde-7d1ccf613175 | -6.26414 | -43.5554 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a66be3ec-a28e-39db-9503-fec70670a552 | -5.53843 | -39.22164 | 2024-12-10 03:36:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd048297-f3ec-3a29-a079-6535ed2efb95 | -7.87462 | -35.14983 | 2024-12-10 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a7376704-4bdc-352f-9e79-b61e1b55bc11 | -8.4466 | -40.60946 | 2024-12-10 03:36:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e95eb9da-3f8b-3137-8eb0-ef898a30e793 | -7.75416 | -35.13805 | 2024-12-10 03:36:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| a35e55bf-55b4-35b5-ac7a-de365215d354 | -7.23637 | -40.85287 | 2024-12-10 03:36:00 | NPP-375D | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cbbeba20-7c0f-3f44-9733-5f9d1ebb8e26 | -6.91567 | -43.507 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 708e20af-afc7-33dd-a15a-adcc97b8bf30 | -4.56004 | -43.30217 | 2024-12-10 03:36:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daa65ef2-0103-3edb-a277-acc89b747f23 | -7.91933 | -35.20074 | 2024-12-10 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 7418bc79-f6cc-395c-bb34-fd15092990d8 | -5.71034 | -46.54481 | 2024-12-10 03:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3caaf543-3c80-3860-9195-156fc214154d | -6.33402 | -43.43701 | 2024-12-10 03:36:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fb71bb1-f317-33de-83d9-20e1cf31dcde | -6.91668 | -43.52145 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fd5dbe3-3ab0-3f8a-94ff-909ce63ad073 | -6.72649 | -46.29089 | 2024-12-10 03:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 249b4742-2471-39b4-bc35-8712655d2c47 | -6.91247 | -43.51307 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b18069a-b827-38ec-8100-b2f88102dbfc | -9.04326 | -36.10949 | 2024-12-10 03:36:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eebcf562-a516-3154-b2c3-b1ece89df5e6 | -6.15994 | -35.27585 | 2024-12-10 03:36:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6d109d36-725a-3466-8ee4-82ba34d2c382 | -8.97272 | -47.0845 | 2024-12-10 03:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c676bbff-f3a3-391e-bf03-0bf642c403d9 | -7.91596 | -35.20021 | 2024-12-10 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 161542ed-f15f-31ca-bc72-acd0eb4776b0 | -8.8645 | -47.67326 | 2024-12-10 03:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bc41562-2702-38a5-95cc-89c12c5bce72 | -11.06667 | -45.37935 | 2024-12-10 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d738ee8-c0f6-3288-a1a0-89a35ae143fa | -13.8348 | -41.79668 | 2024-12-10 03:38:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef34ef8e-4a42-3af0-9ccc-7b69915c9a5d | -10.87811 | -44.3398 | 2024-12-10 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4651c6b1-6e5e-3907-8986-78fe65af2fd0 | -15.65513 | -39.18838 | 2024-12-10 03:38:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d908edeb-687e-311a-b78c-cdb28f898a8d | -13.94466 | -44.35675 | 2024-12-10 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad606198-67ba-3557-ab4a-40025b53b4fc | -11.87498 | -43.72284 | 2024-12-10 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c55d4c4-9a59-3485-beca-dfd89a7c6300 | -12.85526 | -43.81786 | 2024-12-10 03:38:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98d693dc-cb8a-3310-a601-3c758576ff4d | -13.08009 | -43.99985 | 2024-12-10 03:38:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80a1a255-370b-39c7-b0ea-a30dbdd435fb | -14.83471 | -43.14891 | 2024-12-10 03:38:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 580a70ab-cb53-3538-8744-0ffc5bcc47a1 | -14.97127 | -44.41435 | 2024-12-10 03:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b5ff3f1-9f54-3519-bf8a-006983e3812e | -11.87042 | -43.71863 | 2024-12-10 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 041a4ae5-eee0-3261-b836-140d83607be2 | -13.9395 | -44.35556 | 2024-12-10 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8ece725b-7a9b-35c5-a85e-8942e1614c35 | -15.99409 | -43.28535 | 2024-12-10 03:38:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc62c7f9-05a0-31bf-9f43-e179440c11fe | -10.50698 | -44.93287 | 2024-12-10 03:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec699152-2d6a-3646-a8d0-edfd9f8e8eb6 | -16.03212 | -38.99354 | 2024-12-10 03:38:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87ac1000-1fb7-397c-a146-fef26b48c75d | -14.53571 | -45.48084 | 2024-12-10 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 213f3d85-d951-3fcd-96e9-8ffdbd87be48 | -11.06578 | -45.37724 | 2024-12-10 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9218d7e-2279-3c1e-a199-be8292c30bfa | -11.06409 | -45.38573 | 2024-12-10 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6755458d-a2f7-3e5d-91e8-64a0975ff910 | -13.93824 | -44.36206 | 2024-12-10 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92f22a74-ac7b-307e-866e-d700c059c603 | -13.10406 | -43.32013 | 2024-12-10 03:38:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2c04b73b-ca6c-3f5b-b519-10007b3c0c39 | -18.76907 | -39.86545 | 2024-12-10 03:38:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 89cdbe12-c6e3-3892-9c05-2e19c3757ec3 | -18.73505 | -39.90915 | 2024-12-10 03:38:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 60f00ee7-c195-314c-80f7-72da84c30259 | -17.62712 | -39.92764 | 2024-12-10 03:38:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43d4b847-1516-3e87-83e5-59c3e0fdfc69 | -16.24792 | -39.09038 | 2024-12-10 03:38:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d8f61e2-ff49-3f41-99c2-16908891190b | -18.7387 | -39.90986 | 2024-12-10 03:38:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 12ed8f3d-47d0-3513-9ea7-a93c949dfda2 | -11.02514 | -44.93839 | 2024-12-10 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33e62aa6-2bc9-3691-b152-323e2fd7ea04 | -13.10297 | -43.32576 | 2024-12-10 03:38:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 80e98430-e4d3-3365-a0dc-1536e3992387 | -15.64456 | -42.11619 | 2024-12-10 03:38:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17f7064c-35f6-3f0e-843b-68366e8d498d | -13.06263 | -38.9138 | 2024-12-10 03:38:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
