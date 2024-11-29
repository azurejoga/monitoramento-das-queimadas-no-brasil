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
| 5e3411e7-0371-326c-93b7-3b2db1c59b83 | -3.95715 | -48.09058 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7a013f5c-915e-3b8b-b04f-95bf1085a3b6 | -2.33451 | -46.88266 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| b8cd5486-af26-3171-9d85-59b08bd64ce2 | -4.08631 | -47.0326 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36bbb55c-b894-342c-a178-f131b74db5e8 | -2.64624 | -47.12922 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f187b593-9158-343d-92a9-ef68f926a807 | -3.82365 | -44.04084 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40cb289a-cab2-341c-848e-39a0553de662 | -4.23878 | -45.76839 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 944a1df8-eb11-3f60-b3ce-612d1f146007 | -5.1515 | -37.74377 | 2024-11-29 03:40:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2141d34-7fa3-381d-8f59-bfc403bc8b68 | -4.26395 | -42.60732 | 2024-11-29 03:40:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f1db4ed-ac5a-3435-98a6-9fcbf7f18f1e | -2.33746 | -46.86511 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d873773-3c9c-353a-aa6c-cc1f8f30adb5 | -2.84232 | -46.81589 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18081e3a-9734-36a5-9fa0-e2b5e2c188a7 | -3.81056 | -44.04854 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76be0209-0ac4-303e-a368-9733315b470e | -4.23272 | -45.76711 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bf743199-e8b2-3696-be34-c276401041f6 | -4.43623 | -46.59234 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 41f69b64-5816-366e-9bbc-edad2709ce0d | -2.86037 | -45.54059 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d17bc82-a7d1-31d8-838a-39cd44b6da89 | -3.32718 | -46.70313 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ffb749df-ee69-3294-aa91-6f3b7b5904e2 | -2.83642 | -48.10139 | 2024-11-29 03:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0697e41c-44d3-3c0a-a701-4d74a9c1a7e4 | -1.95658 | -46.4417 | 2024-11-29 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf2d602f-b6a6-3b31-a541-419d8afddcf3 | -2.85957 | -45.54531 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47eea0a1-5554-37d0-9b58-bde7683b43f0 | -4.43167 | -46.58062 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fa54ac91-79e4-3171-9f13-9d3659d3a2e2 | -3.81816 | -44.0399 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6da61968-ba7d-336e-9e23-d86979de5c9e | -1.68536 | -45.79564 | 2024-11-29 03:40:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00309a66-c66e-3c2c-a801-0adbedfcb6b0 | -5.88697 | -35.42196 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5aa0f1d4-528a-30d3-b46e-a696b0cc908f | -3.87321 | -48.36074 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 884822ea-56ff-3e52-84f6-cfc588ee20d7 | -3.2028 | -46.57209 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2667d6af-8098-3792-848c-914d4e24c54e | -3.33467 | -46.69871 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| be637856-803e-35ae-9e96-147311e50f06 | -4.45058 | -43.9997 | 2024-11-29 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 881fe85a-621b-3f5b-be2d-fdf8a8767158 | -4.43255 | -46.57553 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ebe7bf48-404f-3d82-a1ba-d60e69098725 | -5.44023 | -45.58179 | 2024-11-29 03:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4d8e669-db89-3f38-8980-986f323ce9f8 | -9.50014 | -36.00456 | 2024-11-29 03:42:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 48d763ab-b192-3ced-89bc-f6800a557416 | -5.81196 | -39.54871 | 2024-11-29 03:42:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa37b2d8-b277-3662-bf4e-1ece7b191fa8 | -5.28185 | -45.12791 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b207890-f30f-3cee-92bf-49c9e5a57efe | -4.69565 | -46.66964 | 2024-11-29 03:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 987a0cd8-3e10-340e-ba0c-98e0bf6e82ec | -4.69655 | -46.66457 | 2024-11-29 03:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 604cfb15-20de-3ab9-b029-d30255c72188 | -7.91364 | -38.41603 | 2024-11-29 03:42:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2cf09a3-6d10-35e0-83c1-269ccc00b646 | -4.91893 | -44.53222 | 2024-11-29 03:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8b2da09-8102-3af1-a0ed-f1849eeceeff | -7.44539 | -39.84243 | 2024-11-29 03:42:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| e37619c3-a9e9-3d19-bd2c-f44230d4ee1a | -5.76229 | -43.39566 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25700556-0823-3ef7-a3d8-c89e423d7891 | -10.195 | -36.33937 | 2024-11-29 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e3209131-1d22-3195-8af6-23e4c5be43a9 | -7.44588 | -39.83975 | 2024-11-29 03:42:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 1a03eab0-2c48-306f-9091-3ee7533e087f | -10.66011 | -36.81623 | 2024-11-29 03:42:00 | NPP-375D | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 12b95f1e-72d4-3d97-a837-6e83d71be0e9 | -6.85963 | -39.43254 | 2024-11-29 03:42:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e10b1c1d-cbe3-318d-9fb1-a1249b2b3f51 | -4.69011 | -46.6637 | 2024-11-29 03:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b29b972-2026-366e-bf8e-08ddb937a105 | -7.02384 | -39.36676 | 2024-11-29 03:42:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6275a217-d1c4-3cd3-b7d5-f553d8efbd65 | -7.27333 | -39.28496 | 2024-11-29 03:42:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8379f63d-4948-399b-b4e4-fe7d82d02208 | -9.55653 | -35.84156 | 2024-11-29 03:42:00 | NPP-375D | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 9e591a38-935f-3a58-9706-978df631c5a6 | -6.48382 | -44.68103 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20ce3c03-7ec2-33a5-a1d1-3f6c47970cf5 | -6.16124 | -44.42664 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93eb3415-74dc-39ca-b3ba-3cb72fd7a498 | -4.79149 | -46.12626 | 2024-11-29 03:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3b947544-8a91-3888-b52c-1e53c4ae99ec | -7.2771 | -39.28566 | 2024-11-29 03:42:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 096e6301-baac-3638-baaf-7a4552b50ebd | -8.12395 | -47.98908 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32af1c27-77dd-39a9-9077-500c81a2e1eb | -4.79062 | -46.1312 | 2024-11-29 03:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f5214a0-8445-35c0-b024-858e14f29c0f | -7.07155 | -40.22525 | 2024-11-29 03:42:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fde036f5-0f35-3a25-9c74-aef03a57b930 | -7.21816 | -39.05828 | 2024-11-29 03:42:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1bd8b121-4c44-352d-b1ae-0b63348902ad | -6.1364 | -44.72921 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 785049f2-5153-304d-a266-dc2e8ebadd69 | -5.86372 | -39.78875 | 2024-11-29 03:42:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 585886eb-647b-32ba-88fe-431b579b44d3 | -5.75404 | -43.39634 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 306acda6-3f69-3b5d-8d25-f96e45878d8e | -9.10759 | -43.10315 | 2024-11-29 03:42:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 255f4c56-8412-3a23-9bdc-3fb459ec3ed5 | -5.75965 | -43.39419 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ba51bdb-8f4a-30a0-b430-6879357f9da4 | -6.91886 | -37.83663 | 2024-11-29 03:42:00 | NPP-375D | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6480b478-eac7-3397-b78c-2aab2318ec71 | -5.86633 | -42.75859 | 2024-11-29 03:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f412279f-7069-3330-b221-584ab52116d5 | -11.37456 | -39.30065 | 2024-11-29 03:42:00 | NPP-375D | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7fe84f3b-3e51-3693-a709-31b498f68116 | -7.01923 | -39.37087 | 2024-11-29 03:42:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d808ab26-e52a-31d7-a08b-3b002832aded | -4.88009 | -44.64489 | 2024-11-29 03:42:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6075769b-1b0c-3ba9-9669-a2d3d0cae11f | -10.789 | -37.20353 | 2024-11-29 03:42:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 864544ed-923b-3b89-b2ce-f023827309a9 | -9.7256 | -37.06026 | 2024-11-29 03:42:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d1989169-e842-3717-a61b-15a8f456c7f9 | -9.31113 | -46.22504 | 2024-11-29 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f40232d1-e2a7-32ef-8623-04fb68ce8098 | -5.75156 | -43.39696 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaf845c4-ef31-3df3-affe-d680bda4cdfb | -5.21644 | -44.92216 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aecf133e-5457-3c32-9a36-2669e9fb2aba | -7.32697 | -39.09977 | 2024-11-29 03:42:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47cb1636-60e4-32a1-827e-11acd9e81e51 | -5.97885 | -45.35638 | 2024-11-29 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d7d1e83-9dd6-3cd3-bfa8-faf6da0acab0 | -5.50316 | -46.25587 | 2024-11-29 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 498b92ea-b8bf-3711-bb9b-b5321f1bea0f | -6.19491 | -44.42572 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 448c767e-0ee0-3986-be87-e223a423c30f | -8.13051 | -47.9903 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e24d5589-3b66-35b4-9883-8ebadd6f568f | -5.51014 | -46.25237 | 2024-11-29 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87e1f83f-298c-321d-bd4d-8ff524fb92eb | -6.0644 | -44.14921 | 2024-11-29 03:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24dbb2a3-1953-362a-b0d9-e94088f24f66 | -7.02307 | -39.37136 | 2024-11-29 03:42:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d55fecd1-8dde-3518-8f45-705e0d1cff2b | -8.28345 | -48.03187 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9efd699-d8cf-3b4f-aa3b-32535c58b85a | -6.48319 | -44.68466 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17f7a1b8-39bb-3561-b06c-ab319e634eca | -7.98133 | -38.27251 | 2024-11-29 03:42:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 266f201d-5a8f-35a1-b360-fc271612075b | -10.19839 | -42.4803 | 2024-11-29 03:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9c31413-b0f0-3625-b1d3-2ab084718bee | -9.07585 | -49.57999 | 2024-11-29 03:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7b8aadd6-3c38-387c-a7a2-3498aab170b4 | -8.13301 | -47.9865 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59a56d24-e1ec-3e0c-ba60-2db3146d7dff | -9.55597 | -35.84506 | 2024-11-29 03:42:00 | NPP-375D | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ad716338-18e1-3948-989c-29c763ffa103 | -10.19917 | -42.47589 | 2024-11-29 03:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad5a6922-ce8b-3276-a57c-bd71efbed371 | -5.86473 | -42.75448 | 2024-11-29 03:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 79b4da92-4ed9-31a1-bfb0-d5e95fecf2fe | -6.02743 | -38.12304 | 2024-11-29 03:42:00 | NPP-375D | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbef73b7-35c6-3a67-a070-00b7b1fc0f75 | -8.12504 | -47.9835 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 559b43f8-f742-3aa2-8011-d553acf76b9c | -6.48306 | -44.68369 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eea13efa-ac93-32de-9d44-1664c736957f | -5.36642 | -44.84502 | 2024-11-29 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4046c503-e054-3a76-a8fc-61da8fa25e4c | -5.75666 | -43.39782 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ab09204-eb91-35f9-ad70-415e52799ee1 | -5.55124 | -41.4148 | 2024-11-29 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b949f832-fa0f-3ced-83fa-9948d53a55ad | -5.04498 | -43.62227 | 2024-11-29 03:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9c3ed8d0-14c7-3029-b354-c876ccfef183 | -6.09641 | -43.96922 | 2024-11-29 03:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dda898a-30e1-3ae5-b07b-402dd8d5e1f5 | -8.90512 | -35.6161 | 2024-11-29 03:42:00 | NPP-375D | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e300b226-a177-35df-89ff-69b56f259f93 | -5.22285 | -44.91901 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65b038a5-d5ef-3f6a-9d13-009745a9c58e | -6.75604 | -46.52371 | 2024-11-29 03:42:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b5d6b7c-4b08-33f3-abf6-fa8f02f56279 | -5.22857 | -44.91975 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3ee08ce-4594-39df-9fd4-5fa7cf9f1ebb | -5.76281 | -43.39266 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fecd5cb-5eb5-33cc-82ac-07ece2b57c21 | -5.93032 | -43.78365 | 2024-11-29 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 550eefb0-dd0c-3ee1-93da-e22e8d354da1 | -5.58783 | -45.21285 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README20.md)
