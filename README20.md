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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa3b6d5-1091-3dfc-8e65-b876f3d738b0 | -5.61616 | -47.08335 | 2025-11-01 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7febae9-87ba-3e2d-b97a-05e8dd493934 | -3.80162 | -51.61022 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 855bd204-f4bf-39c4-8486-422dd1086978 | -4.04579 | -50.5684 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8df19adc-198a-3c03-b23a-bad09f7c956a | -3.82127 | -50.173 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31059ee4-3017-3bf7-bfbf-47cf9f97e1bc | -5.15166 | -45.81953 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10dbaa84-a6da-3e05-934b-ebc44acbea82 | -3.02039 | -53.96753 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 31918497-ade5-31c0-a2b2-c13e3a0da8ff | -4.40433 | -48.21725 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8dfac9b7-155f-3c58-a70d-459763441936 | -4.55129 | -45.79599 | 2025-11-01 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45018980-4b86-33f3-8724-f903a4a04875 | -4.56594 | -45.40666 | 2025-11-01 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f3a7b96-5c05-35ff-8ac2-41ae2497730c | -6.13322 | -45.93877 | 2025-11-01 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6156c046-d54b-393f-987b-0faf2be1728a | -4.56767 | -50.16635 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f553ddf-144a-34d3-b960-10021ce5169a | -5.30251 | -45.34309 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 011a59c0-b802-30e9-b34c-5b6b41cf4e41 | -4.10403 | -44.99662 | 2025-11-01 04:38:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1afe5304-79c2-339c-bb7e-e232c60752dd | -5.94275 | -43.96228 | 2025-11-01 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0659650c-db6d-302e-bedc-ba09daa4b55e | -5.9342 | -50.26608 | 2025-11-01 04:38:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ca7287d-d2a5-32ac-b8a0-295d9c03620b | -4.82151 | -49.63839 | 2025-11-01 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a757ef5b-7d9c-3a73-b2d0-4121c9178cec | -5.06969 | -43.95714 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61f83bbd-9930-3e30-887d-3c31ae6c778d | -5.94785 | -48.33349 | 2025-11-01 04:38:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20d8fcf-51ba-33fa-8cf8-bb040b478bbb | -4.21919 | -49.78944 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c7c6ec4-8fc9-3fcb-9c29-a59ef38df557 | -5.21867 | -44.79955 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f04002e-3e81-3aa1-b354-c0f366207bc6 | -5.58992 | -45.03698 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc48bbf8-34ab-352b-9ae4-bda8b9f0930e | -3.67275 | -50.48781 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891681f2-41c3-325d-83b5-147bead289bd | -4.6766 | -50.44728 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d51fda1-efe0-355b-a48b-9bd5a44e9ec5 | -6.46058 | -46.81464 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4abe4073-9a66-38a0-b44b-07cd01c1ef6c | -2.9289 | -51.46281 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 689eda09-0660-326f-aef2-159b62af06b1 | -3.60503 | -50.62482 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b6a62bd-0266-382c-85c7-a0ff796cb3ff | -3.04011 | -45.8195 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54ea23b9-37d6-3c36-bdeb-5c1c76161b73 | -2.88696 | -40.46706 | 2025-11-01 04:38:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 929fb8f7-3d04-37fe-b922-65e0aa9439c0 | -3.41598 | -50.00344 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 13361e50-8a55-394a-9d34-bcf66d2e045c | -7.06935 | -47.00581 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3da1aafb-8df7-32bb-b28a-42d4680b0153 | -4.96539 | -40.55498 | 2025-11-01 04:38:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2e9ab266-6f9c-39cd-b6ef-fce97165cda2 | -4.21212 | -53.49107 | 2025-11-01 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0867cc36-8828-3b07-91da-ac799375e26e | -4.55798 | -46.68431 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b1b20ce-a083-3871-aac1-0bc65d63b793 | -3.65909 | -50.19225 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 62af323c-f694-36d4-b265-a209a5177434 | -4.95167 | -48.26388 | 2025-11-01 04:38:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8bef2ba8-772a-303f-ba7b-6baa9ce553c7 | -6.40854 | -47.22368 | 2025-11-01 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d90edf-a760-3725-89e0-7ad75b7ba08f | -2.65442 | -48.50926 | 2025-11-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0398111-c245-3db6-aca3-e073630d1d34 | -3.04007 | -50.26978 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e04d23-5487-3a82-bd65-cbb3e0e86bc6 | -5.35408 | -45.03491 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88674bf7-af5f-3f64-8871-3866d4626e17 | -5.6179 | -47.11793 | 2025-11-01 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44f4e65d-66bd-3ca0-9167-72cbebbb44f3 | -5.11091 | -43.39306 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1363594-d066-3f56-b78a-fb7e869d5026 | -5.67492 | -43.236 | 2025-11-01 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 838d0883-0680-3ddd-90ec-d3f21ae44dbd | -3.73388 | -51.6501 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4db66716-a0b6-3c51-b116-d027d7d169b2 | -5.20346 | -49.65623 | 2025-11-01 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42deae8c-2bce-34ee-8225-31c463adeed8 | -4.93961 | -44.82739 | 2025-11-01 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32e2b30f-1fc3-3cac-80a1-628fd670328e | -3.83698 | -51.34656 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a9d7881-44ff-3cec-9367-fe9dbf28fba4 | -2.93618 | -54.16354 | 2025-11-01 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f4d8e27-1359-3704-8ed1-d7cb54b95dbb | -4.56086 | -46.68856 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f3ababd-3e6e-32a4-941d-3019edcd795e | -3.73486 | -51.71299 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 690ef7bb-c5df-36d1-b774-3ebff07aacb3 | -5.88184 | -44.52494 | 2025-11-01 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa91793c-cfd0-3f64-bd49-edae62c55d70 | -2.18684 | -46.56808 | 2025-11-01 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b6f6500-63f4-3a52-ac66-21ec87ee8485 | -4.61232 | -49.58363 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3225c43d-4231-3222-b87f-163aca78e7d5 | -3.43153 | -50.10111 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c8691cb-db45-308b-a935-a00697cd421d | -3.42583 | -51.48842 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8ad7c7a-567f-3aa3-b0bb-d57cf6a7f042 | -4.17938 | -47.65373 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8b9bcd04-d69a-35a9-a9cd-a94ab9e626f9 | -5.49729 | -44.43859 | 2025-11-01 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98375b68-5183-361b-8978-d943914159c6 | -1.26415 | -54.09562 | 2025-11-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa639a87-8f19-34d3-924b-76b0e936a4ab | -4.79538 | -46.46951 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f67dac2-38d8-3cf3-9e9c-361c2262a874 | -5.72677 | -43.98832 | 2025-11-01 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8792bf4c-152d-333f-8bbe-c77e101ff24a | -4.81046 | -45.87371 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e20af49-6988-3007-8cef-eb6e8f2978f8 | -3.58977 | -50.80944 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d43f9255-a973-39e7-8840-138ca42cf09b | -5.984 | -43.6134 | 2025-11-01 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14beb83b-43ae-36e1-ad7f-bb29e4a227ad | -4.18327 | -47.65071 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ba7e399d-28d5-309c-b10f-e243b4af48df | -6.00047 | -45.75052 | 2025-11-01 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 839c71a9-8726-33fd-ab53-4bfaac9a9561 | -6.57607 | -48.73484 | 2025-11-01 04:38:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c04ac027-e24e-3b2a-ac99-761c0a5e5435 | -4.80749 | -45.86905 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57f88678-a667-36cd-870d-0a5e0404bd5a | -3.41319 | -49.99934 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc06961a-45ca-3d92-afe2-c934627ce466 | -4.96032 | -40.55415 | 2025-11-01 04:38:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 59af0c86-6a2b-3fd6-bdcf-510e0dcc9d4e | -6.32316 | -43.62761 | 2025-11-01 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2753f573-add3-316c-9dbd-0b5f9d463916 | -2.89791 | -48.05885 | 2025-11-01 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e089d2f4-73b5-3118-a21d-4b1efba78e1d | -3.57115 | -50.26715 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1e30354-f55a-379a-95a4-bcd2de45b24c | -4.33716 | -44.5349 | 2025-11-01 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dac1111-e9a2-3141-a450-6bc6c2acbca3 | -3.14116 | -50.45031 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 529abf6c-382f-3a97-a412-21aaf190d0e3 | -5.03733 | -43.60559 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8014c48-77dc-3b99-aed6-f4db94dc6c3a | -4.49046 | -48.27658 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f08f7e3-9df1-340d-99e9-b787659cc195 | -5.94453 | -48.33297 | 2025-11-01 04:38:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e878dd1-8a28-3765-93e3-797afa5f5e86 | -2.92824 | -51.46685 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb346d85-a110-35bb-b5bc-de04187cfd06 | -5.11985 | -43.39043 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 235c9662-2c43-31ea-9318-4093f181ca90 | -3.32651 | -44.34668 | 2025-11-01 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0feb10c0-1e61-3388-ab30-95b435efccbe | -6.93649 | -49.63062 | 2025-11-01 04:38:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de039eb5-c65b-3159-876f-a0d7ac152531 | -4.70923 | -49.61712 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 712ee91d-5336-309a-84f5-7f6f54d8fa07 | -3.03925 | -50.34063 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b4e2167-a712-3073-b765-5e13ae61f6fc | -3.30522 | -50.01562 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc76d6e-d99e-372c-a694-aadcae18e6b9 | -3.54007 | -50.16934 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01397997-cdd9-336a-9dd2-332602d9ea14 | -3.79918 | -51.14954 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6632ecd-45b4-3d50-8f80-00b3a3f28128 | -4.6446 | -50.71454 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db8be4d5-fe2f-3385-be92-3a915264688b | -2.8892 | -40.49641 | 2025-11-01 04:38:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 60e8d6b4-ac46-35da-be68-7dacf4835f9c | -5.14216 | -44.82007 | 2025-11-01 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baef766c-e51d-367d-a1f8-df0b4452f23c | -7.47665 | -46.11588 | 2025-11-01 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcc05633-389f-3fcc-b4f0-3c3166e848ca | -5.37896 | -49.27689 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e31184df-0b24-354d-b929-ed6a155da96a | -3.60445 | -50.62854 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3edda765-ab8e-3c77-bf01-a6cde902dd1e | -5.8461 | -49.9828 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 124e4217-51ba-3745-a5f2-6ad888ae2a1a | -2.65496 | -48.50583 | 2025-11-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b2a3682-47a1-31f8-9e45-3a3349e36d49 | -3.10603 | -45.22855 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2ce43aa-aba8-3919-bd73-2c20084e4774 | -2.1897 | -46.5947 | 2025-11-01 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f125fc3b-ac88-3365-bc55-0c291f96b920 | -4.531 | -46.40347 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d59d4ef5-6e38-338d-8821-96ffffd1a712 | -3.73129 | -51.71244 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094adfba-688a-3e26-83df-0539bac2fd7a | -2.90067 | -48.0628 | 2025-11-01 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e223ee1f-9950-376a-b3a6-80054e31994d | -4.49908 | -49.86955 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b5f19fb-3010-3a1f-8a06-74e4322bcbde | -4.51583 | -48.94001 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
