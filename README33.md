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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcca5596-abf9-3543-9355-0f32475223ff | -1.01669 | -52.27313 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91528314-12c4-3cbd-8a37-00763dcd9bcd | -2.62552 | -46.02753 | 2024-11-17 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1bd39410-e33a-34ea-a76b-1a933e90b934 | -4.45672 | -44.54772 | 2024-11-17 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de1d93b0-c9c9-3314-af21-2541a1b40e7b | -3.58255 | -50.5244 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13e1cd14-098c-3694-b72a-3caa3130f406 | -6.31228 | -39.48915 | 2024-11-17 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dd4c67e7-1065-38b7-a045-17c1929c4819 | -3.74198 | -44.52955 | 2024-11-17 04:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a97a57b-7d51-3484-b450-3a77074e0617 | -5.50974 | -46.42833 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd470457-6575-3e41-a970-5382ce746d13 | -3.9813 | -45.97028 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a432878-1a23-315d-a92a-85b2e95d7766 | -2.6669 | -46.17183 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2bc6ed8-1179-3a96-834f-ed6508f73a7a | -2.67332 | -46.85994 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e9cf4fe-0053-3e07-a3fc-326675f69906 | -4.55351 | -48.00535 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fbd2d768-257e-3722-aca6-33d0d45b40c4 | -3.32698 | -50.49825 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc12c740-72ea-3cb3-ad2d-999e9c9952d2 | -3.52854 | -50.26813 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb57f568-77e5-3e71-b0ca-7b378f805fed | -7.42441 | -47.86586 | 2024-11-17 04:06:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f69d145-e8b6-316c-8fc3-a827d41bde10 | -3.89349 | -46.62204 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 553cafbb-4eaa-3560-8406-2fd1b479c5ce | -3.91774 | -46.52515 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 867ea63b-07f0-3c41-9aee-8277e70f5c33 | -2.65713 | -46.20608 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f059210-7cc5-30e2-a156-04a5268be259 | -2.62485 | -48.55959 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 297ec76a-840a-3b8c-b0a6-78662041ec97 | -4.74435 | -48.12328 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 038d2c98-d906-3fe2-8971-52acf8067704 | -2.86803 | -46.71654 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 65edbf97-1fc2-3e82-a210-e1de3ab88864 | -6.95866 | -42.47992 | 2024-11-17 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9d8fa7f1-d1d3-3bda-82c4-f0fe5c67cc3f | -7.82539 | -43.12821 | 2024-11-17 04:06:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8496c487-f48e-34e2-a5a2-08e1666443cd | -4.28331 | -48.20629 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 28c87c8d-fc5c-3683-a059-0bcda5d3d3aa | -3.57 | -50.25697 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 790f58c4-75fd-378c-a6bf-cc46aa36a3fa | -7.58378 | -39.05002 | 2024-11-17 04:06:00 | NPP-375D | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b9a171a-3319-365a-a642-467be3fa75e8 | -4.1828 | -46.81823 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9e32c9b-8bdd-325f-bdfe-372f48f1f273 | -3.33043 | -52.77325 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0a48159b-f2b6-3178-82b6-23b0cfa6c564 | -4.089 | -40.8774 | 2024-11-17 04:06:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed2c8986-b1f7-3e56-9c99-60a8d4f8fd6b | -4.46891 | -44.23497 | 2024-11-17 04:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1f53200-5a87-36c4-ba94-6748cecfc110 | -1.83207 | -46.5984 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bff98084-409b-3653-80e1-4d284b3eeea8 | -4.24792 | -48.53601 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cff1b5f0-3c38-3a77-8809-bb4a9458ff43 | -4.54862 | -46.41258 | 2024-11-17 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f3f32ff-7278-393c-bd1b-3e12b2ce31a7 | -5.87824 | -40.15008 | 2024-11-17 04:06:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d343296-475d-3cab-ad42-5d9ccd22e151 | -3.53845 | -50.51315 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1549c42f-63b0-3794-8bc5-0b7ba479287c | -4.12578 | -45.89973 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73d13fa1-84fe-395b-a034-68433700304d | -2.9289 | -46.72903 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e043abae-ea7c-3da4-9676-9a0db210c5ed | -6.93851 | -42.82019 | 2024-11-17 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96c4ff5a-dc38-33f0-bfcb-869397a90268 | -3.42291 | -41.0241 | 2024-11-17 04:06:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc2cbbdd-a22c-3775-8706-31c046ada08b | -3.58598 | -50.52364 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b3ec958-43ac-333a-96b8-6cad8636c1b1 | -4.15837 | -43.91906 | 2024-11-17 04:06:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ebe2bad-63bf-35fa-8be3-b7cfefcd5a16 | -2.6699 | -46.18023 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8354f38b-ef79-32f5-9676-9a25afc84d86 | -2.36866 | -48.5318 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe1708af-6c63-3c7b-882d-1eba5e6fb9d3 | -5.51755 | -41.0702 | 2024-11-17 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6505a743-889a-34b5-b901-eb07640e201b | -2.62492 | -48.55894 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31ecd37d-71dd-31ce-8605-6bc0423d34e4 | -2.66989 | -46.86146 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4124bb1-2d81-3589-b5ea-7b52bc86e10f | -2.67744 | -46.21255 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 180f0f48-22eb-3de6-b15e-0b834a61f7c6 | -3.7818 | -46.04278 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 822d4226-6d6f-302b-9e08-c68b3b15ca8a | -3.93585 | -46.17303 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7320f966-b50a-3582-a2d8-40574501eb04 | -2.2688 | -46.58914 | 2024-11-17 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9190757c-9da0-3def-a648-ee11b21e34c4 | -3.91718 | -46.52519 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2d00bda0-9bc9-3d49-8868-96d391fdaf04 | -5.67248 | -46.49531 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 231a82b8-6cb1-3875-9e19-0f34e5aaa65f | -3.61477 | -44.792 | 2024-11-17 04:06:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20cc792d-aa7c-336f-b830-59a1b7c95d3a | -4.30121 | -48.06693 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8755406-8eea-33dd-b64e-3cda792f46b5 | -4.70664 | -44.47049 | 2024-11-17 04:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87875a12-3ef9-3897-82bb-558be36e86a7 | -8.51326 | -35.04309 | 2024-11-17 04:06:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 282e672a-e452-3f59-b8a9-dec0fe72aa91 | -3.69982 | -44.42925 | 2024-11-17 04:06:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 863c7536-d1c0-355d-8cb2-59f100c2fc19 | -3.93171 | -46.17238 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54adb4c3-8e7f-36ff-9eb2-e7ce2a9937d1 | -4.29028 | -48.07498 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74fec03c-14f1-3b8f-a2be-6651a846bd8f | -1.83714 | -46.59486 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e9e9f79-da69-36f0-98b6-a4892002aa13 | -3.62586 | -50.22614 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34f45c49-6951-3a30-8047-b0e57e2816d6 | -5.58956 | -45.21139 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ace14608-fb46-3fbc-9ac1-41d8a7d79af4 | -4.10554 | -46.87411 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af2919be-0416-3322-8d9f-f5e496d36535 | -3.53219 | -50.51617 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad3edd6-5f49-3440-8826-419b1d671628 | -3.52168 | -50.2415 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55208ab3-666c-3366-b130-90afe53f5181 | -2.15313 | -50.69863 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c69019bf-dac8-3baa-bc8e-f974ec91f59b | -6.38795 | -45.69056 | 2024-11-17 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06472052-d9f5-3e16-a1e4-e132f822a8a0 | -2.66268 | -46.17115 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f7db5a7-d4a1-3600-80b8-49457d428854 | -5.75346 | -38.81404 | 2024-11-17 04:06:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef27d134-d10f-39a1-b545-22280b8c4dff | -2.46106 | -45.60858 | 2024-11-17 04:06:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c95bdec4-224f-3b90-a1e4-778697dea279 | -6.19821 | -39.77649 | 2024-11-17 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b02e3519-7e02-3eae-9e1e-b887457df152 | -2.66797 | -46.21982 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 09a2d953-b3bd-3a82-b365-874bae8f5578 | -2.22001 | -47.21882 | 2024-11-17 04:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c700537f-4135-3528-921b-6ae4aa76e1ee | -2.67403 | -46.2089 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b11a7e44-7ff0-3255-a21a-6c1e2a1c898f | -3.58065 | -50.53595 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7029ec4-43eb-3e47-bbfe-cefba8e5f1ff | -4.90991 | -44.64352 | 2024-11-17 04:06:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a440ad5-755d-3826-a61c-348a574ae04b | -3.56683 | -41.78576 | 2024-11-17 04:06:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a75a7a2-574c-33f0-971b-7cbebc52b159 | -4.70295 | -44.46992 | 2024-11-17 04:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f602bedf-4096-3120-b213-b6db59ae133a | -3.62443 | -43.15698 | 2024-11-17 04:06:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe718cf4-c884-318a-8da0-49263fe49fd1 | -3.57903 | -45.68315 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c6c0fc5-ddd8-3f60-b270-85bea84d7634 | -4.10417 | -46.88239 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f33b023-7a0c-3229-9fd1-db41c01ffb62 | -3.34527 | -46.06721 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6472807-0c38-3dc0-b0c2-3b0ed7fb4e9c | -2.34901 | -47.46835 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8a5f1c2a-9d79-37b9-8a65-b9281faec9c1 | -4.30306 | -48.06924 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 191c9c83-a19a-3a9a-9989-2672c4af4eb3 | -2.60561 | -47.55209 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb7dbfeb-4ba6-3844-b67f-caa20cfe7703 | -2.23209 | -53.6072 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01e78f1e-2cf3-3736-a52f-1e7a866cd62e | -3.94439 | -46.70388 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195fc811-2f3c-3e4e-bdda-25986419d922 | -3.21869 | -42.08882 | 2024-11-17 04:06:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87ae0b42-18e2-3ab7-9ed1-376e9253660c | -8.28883 | -35.66347 | 2024-11-17 04:06:00 | NPP-375D | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2db4095-1cbd-34aa-9713-f9b394ab54a9 | -2.98765 | -52.60101 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e22b35a-49df-3dd1-b334-96883ac70144 | -3.62645 | -50.22253 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 591ad7b7-d9ee-36b8-b5ab-5d29c7d8b6d7 | -2.47726 | -45.40507 | 2024-11-17 04:06:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c50ac6f-6e28-3f01-b214-7b491f16e550 | -4.35892 | -45.87107 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f4f0f05-71af-3d66-8500-4fe3eb2c10e8 | -2.31326 | -48.46486 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bd79ad2-788e-3f1e-a9cf-40f12e5beaa7 | -3.61097 | -44.79138 | 2024-11-17 04:06:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87cfe11e-04cf-33f8-9852-d0a2b3d2c711 | -3.56575 | -50.24864 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27839341-2974-37c0-877c-e4fe3eb0a52a | -6.93629 | -42.81244 | 2024-11-17 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c5eff8e4-7eb2-3934-8ee7-641431660881 | -2.57378 | -47.57167 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6acd738-10c7-3a8a-8120-edf05162dc76 | -2.13977 | -46.49721 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da691d7f-012c-3234-b143-67f589437f10 | -3.70995 | -51.84468 | 2024-11-17 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04b4bf2f-6b5f-3e03-81f7-90725925692a | -2.67773 | -46.86069 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
