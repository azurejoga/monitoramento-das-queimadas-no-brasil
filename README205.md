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

## Dados Diários - Página 205

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13c3fd8a-dbec-3997-96d7-c037d00f6fdb | -15.32411 | -46.73259 | 2024-10-02 12:17:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d9bc8007-889f-3e01-8cac-b0bfd811185a | -17.10545 | -47.11485 | 2024-10-02 12:17:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 75c65a2e-dc89-369f-8ade-8316f1bffe12 | -17.09383 | -47.11296 | 2024-10-02 12:17:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| d85e5401-c08f-3e5b-861d-3f651fb33bfe | -17.09098 | -47.12941 | 2024-10-02 12:17:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 41.6 |
| d437e73e-78e8-36a0-b36d-db7f4d06dd1a | -19.36497 | -47.13621 | 2024-10-02 12:17:00 | TERRA_M-T | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| e2a1fd60-f8a5-3e39-ab0b-44abb6fa8b1a | -19.3644 | -47.14298 | 2024-10-02 12:17:00 | TERRA_M-T | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 71cddd77-ee4b-3581-b44d-0e0cf71f6eb0 | -19.76761 | -46.61028 | 2024-10-02 12:17:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 21c90e9c-fb7f-3aa5-bba3-51d0e67f19ab | -12.28673 | -47.64668 | 2024-10-02 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 9d073409-84f5-3bef-8473-ad24cf5509a3 | -12.2819 | -47.65255 | 2024-10-02 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 81ed5eed-42ff-39dd-9562-6a9382d37d98 | -15.28301 | -47.51126 | 2024-10-02 12:17:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 875a401c-a1c0-3022-a667-e942d5349d9a | -15.28006 | -47.52829 | 2024-10-02 12:17:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 99d72474-4ca7-3fb4-a49e-f66e6185a882 | -15.20768 | -47.94402 | 2024-10-02 12:17:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 76f5e879-a1bf-336f-ac2d-e12294c9b702 | -15.19493 | -47.94126 | 2024-10-02 12:17:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 1f1c1fdb-cd9f-3b5a-bf6b-702b777cfc29 | -13.23195 | -48.61713 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 2339f29e-6c8d-3232-b1c2-ccd9acef5739 | -13.22836 | -48.6091 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 02832a0c-ef26-30c2-a2ef-6453752de88a | -13.22406 | -48.63434 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 304ea2d5-595f-3127-a152-d84c4a7a997f | -13.21803 | -48.61388 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 215.7 |
| b8ccdec5-977b-3a6e-b60f-475c09dd2ac7 | -13.21436 | -48.60627 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 07f8a497-a1ee-3387-bf4f-3394ee474ad3 | -13.21344 | -48.63954 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 1bf07975-29e4-3811-a14d-72c0b71d3141 | -13.21006 | -48.63137 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 256.3 |
| eae38b94-727b-38f3-a4e2-87427b366942 | -13.20395 | -48.61149 | 2024-10-02 12:17:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4560989a-8af1-359b-8438-8c738ab57cb5 | -14.81078 | -48.78638 | 2024-10-02 12:17:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| ced1d290-3ea1-3030-9f64-494fdef57324 | -15.89934 | -50.15715 | 2024-10-02 12:17:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cafeff29-b184-33f5-b250-2207fa912066 | -15.89691 | -50.16449 | 2024-10-02 12:17:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 332c9c64-bd0a-3d4e-bca6-ec3c1a443c28 | -12.16189 | -50.06145 | 2024-10-02 12:17:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 04722e6e-67e9-3234-a1f8-79fd71343110 | -12.15367 | -50.0542 | 2024-10-02 12:17:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| baa1a111-4e47-367a-a0b6-1ba2c7e964b2 | -13.55041 | -51.18075 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 4386fd60-3bf4-3cd5-a186-77b640e1a907 | -13.54434 | -51.14563 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| fd80b277-958c-3be2-b3c6-597bff096ea8 | -13.53694 | -51.18393 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1027.2 |
| efeb33e2-2e8d-3a9e-94d8-51bf306d176b | -13.53356 | -51.17746 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1183.5 |
| c22056ef-d34f-37fd-8832-37b9b32b1735 | -13.52948 | -51.22252 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 253.3 |
| 9df2e69f-23da-322f-872e-3f44ce56cb1c | -13.52635 | -51.21611 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 361.2 |
| 909334d7-1780-3c76-971d-7f17da0a0df2 | -13.51671 | -51.1742 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 397.1 |
| f68dbcd3-0d23-3c8d-bb72-f6ad23281c99 | -13.51398 | -51.16616 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 12f96b27-3a0c-3bbf-b6f7-cec86e205c72 | -13.50945 | -51.21284 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 429.5 |
| 97fea6bd-daff-355c-9960-fad45207365a | -13.50698 | -51.20483 | 2024-10-02 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 517.6 |
| b0109fb4-0007-3b5d-8151-e1807d4df4e8 | -13.19916 | -51.21271 | 2024-10-02 12:17:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 11aac749-4888-39d7-b706-35e3bdbccb6d | -17.89337 | -45.92211 | 2024-10-02 12:17:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7ff9f682-9b37-3726-96c2-d72a0bc02d4a | -14.2337 | -44.88746 | 2024-10-02 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ae304378-4ca2-37f5-a7db-cb17014cb8b4 | -14.77145 | -44.35033 | 2024-10-02 12:17:00 | TERRA_M-T | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ec80a24c-7ad7-3130-852e-1268062ca81d | -17.47235 | -39.77872 | 2024-10-02 12:17:00 | TERRA_M-T | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d89960aa-0c6f-3801-843a-55607ffbfe37 | -17.46302 | -39.77736 | 2024-10-02 12:17:00 | TERRA_M-T | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 156.6 |
| 67d5f795-74d2-307b-8bf7-4a15a5ba11b5 | -17.46166 | -39.78761 | 2024-10-02 12:17:00 | TERRA_M-T | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| 74f01b3a-115e-34ce-a2d8-46211b041961 | -17.29911 | -39.51427 | 2024-10-02 12:17:00 | TERRA_M-T | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 3389bbed-e47c-3405-8c4d-c81cad54c90f | -19.32448 | -39.87793 | 2024-10-02 12:17:00 | TERRA_M-T | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| bf8ac27c-76c3-3c74-9226-3af81be1e242 | -19.32307 | -39.8886 | 2024-10-02 12:17:00 | TERRA_M-T | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 129933ba-bb04-397f-8a03-343ec5d43643 | -18.13913 | -39.88566 | 2024-10-02 12:17:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| afb7c1de-96e9-3c1d-af53-18c4d84891c7 | -18.13774 | -39.89597 | 2024-10-02 12:17:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 7d078027-3e61-32d7-9774-93b4b630721b | -14.49654 | -45.24244 | 2024-10-02 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c34c80f7-b75d-3424-956d-1b9a57f2e495 | -14.49868 | -45.22903 | 2024-10-02 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5e295912-07e5-3ea3-9112-232c48b88f22 | -14.50712 | -45.24415 | 2024-10-02 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5865fc41-0f8e-3048-8176-52538f027311 | -14.50925 | -45.23079 | 2024-10-02 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ac09a06e-bfb6-3a94-acdd-c7c0468e479d | -14.71317 | -44.01067 | 2024-10-02 12:17:00 | TERRA_M-T | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 291111fb-d045-328e-890b-e79fdd0947fd | -12.5385 | -43.74367 | 2024-10-02 12:17:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a372eab3-b32f-3c4c-9ab5-7555ab689973 | -12.53869 | -43.75025 | 2024-10-02 12:17:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 8d4d4517-5aab-3354-aa35-e9c68a238eff | -12.98942 | -44.72367 | 2024-10-02 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4f516f1d-ccf7-3f26-8f1a-407f24df581c | -12.99987 | -44.72541 | 2024-10-02 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 69dfc8da-9ffc-3add-b77b-a9b27a028309 | -13.47686 | -44.86827 | 2024-10-02 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 93ed059c-4c35-31c9-9380-6dd99df2031d | -14.5134 | -45.23817 | 2024-10-02 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 9efbc79c-fd49-3547-addc-51b9bc1ea59c | -22.90827 | -45.10773 | 2024-10-02 12:19:00 | TERRA_M-T | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 93628981-c73e-3b09-b02e-0e6c4e1d2f36 | -22.49334 | -44.14901 | 2024-10-02 12:19:00 | TERRA_M-T | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| fd75bfb2-1c6b-314e-974f-a66da055b8a9 | -22.77543 | -44.23609 | 2024-10-02 12:19:00 | TERRA_M-T | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 14996fb2-427c-36a1-b761-dab6aaad3e59 | -20.9248 | -44.8659 | 2024-10-02 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.4 |
| fa21fba9-cc1e-35bd-a02e-770154df6a52 | -20.92648 | -44.85513 | 2024-10-02 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| d273e84a-4695-3464-9fe4-a864f20d8d86 | -20.93251 | -44.87832 | 2024-10-02 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 82700102-2f10-3077-b825-ba736755bdd6 | -20.9342 | -44.86755 | 2024-10-02 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 187.1 |
| 8e528075-096d-3f7e-8ea3-91c392a475fb | -20.93586 | -44.85693 | 2024-10-02 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 119074fd-d5d6-3b33-816b-410389c00064 | -21.19942 | -44.16372 | 2024-10-02 12:19:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0de00279-ca4d-3885-8fcd-c8954e406f2c | -21.47579 | -44.57993 | 2024-10-02 12:19:00 | TERRA_M-T | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| ad3312d1-89f6-3291-aa21-21d879b2d3a9 | -21.47742 | -44.56957 | 2024-10-02 12:19:00 | TERRA_M-T | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8e276775-0d43-3a8a-8b25-e6c7999a7aa1 | -21.67183 | -43.97015 | 2024-10-02 12:19:00 | TERRA_M-T | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| c26edd6f-9053-3a97-9abb-e7caf3c1dead | -22.00492 | -45.31865 | 2024-10-02 12:19:00 | TERRA_M-T | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 32232054-93da-3ccb-884e-98a8e713ab35 | -22.00666 | -45.30783 | 2024-10-02 12:19:00 | TERRA_M-T | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 222034c9-5ecb-3b01-a3b9-e783471acbdf | -20.51187 | -44.01692 | 2024-10-02 12:19:00 | TERRA_M-T | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 03cc3cae-fa01-3140-9b08-30e40438cccd | -22.384 | -43.52719 | 2024-10-02 12:19:00 | TERRA_M-T | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e09db0b8-86f2-3668-82b9-57ed3f427af6 | -22.38544 | -43.51748 | 2024-10-02 12:19:00 | TERRA_M-T | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 2bba077b-b2b7-3bc6-aef2-b940f010a636 | -22.51096 | -43.84971 | 2024-10-02 12:19:00 | TERRA_M-T | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| d559070e-469b-36af-b852-3a8373b8c4c9 | -22.51242 | -43.84 | 2024-10-02 12:19:00 | TERRA_M-T | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 2d9f35a4-3685-300e-903f-9181084fd6be | -22.67103 | -43.70377 | 2024-10-02 12:19:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 926c3cfb-46e8-3dad-93e3-894fe10d3441 | -22.76772 | -43.79644 | 2024-10-02 12:19:00 | TERRA_M-T | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| e5c0c236-f9fa-3d1a-ad60-e482eb949c3a | -22.77761 | -43.79439 | 2024-10-02 12:19:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| 9ab0fa5a-86f7-355c-a1a6-04b47fbbf61a | -22.78656 | -43.79599 | 2024-10-02 12:19:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 162.8 |
| cd1337c2-85fe-37f1-88fc-8c77ec0c3028 | -22.78802 | -43.78627 | 2024-10-02 12:19:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| 5cb30b2f-0411-3287-856b-4768e09f542d | -22.91834 | -43.71532 | 2024-10-02 12:19:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 2c23c9b8-62b7-3a3c-a52a-f8bdb2ff14a8 | -21.61494 | -42.79905 | 2024-10-02 12:19:00 | TERRA_M-T | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| 3faab417-bec9-3b6d-85f5-33771ea03340 | -21.61632 | -42.78954 | 2024-10-02 12:19:00 | TERRA_M-T | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 4b51713d-f9a5-3874-a6b9-3b8567b8589f | -20.82571 | -42.3348 | 2024-10-02 12:19:00 | TERRA_M-T | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 87ac261c-e7b0-3538-94de-f06b86b1e25c | -20.89672 | -41.89923 | 2024-10-02 12:19:00 | TERRA_M-T | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a0ceeb40-e9d6-3ab7-88f3-7c79dab652b3 | -20.89807 | -41.88966 | 2024-10-02 12:19:00 | TERRA_M-T | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 686fa771-c2e4-30a4-8b41-5cdb309134e1 | -21.00469 | -41.78524 | 2024-10-02 12:19:00 | TERRA_M-T | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 7ce2d3ff-f51f-3b05-b200-abdd9dbc1d17 | -21.31571 | -41.73262 | 2024-10-02 12:19:00 | TERRA_M-T | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 34.1 |
| 9fc9d540-d84f-3a51-85c9-a14923575283 | -21.3229 | -41.41457 | 2024-10-02 12:19:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| ab78665b-0261-3bd6-b434-887c2d46e6d7 | -21.32426 | -41.40465 | 2024-10-02 12:19:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 83101996-2e98-3e54-a02f-29338c2c0e93 | -21.67791 | -41.37145 | 2024-10-02 12:19:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| a8f59019-7c99-32e2-b747-c0a3abdc2099 | -20.63558 | -41.9863 | 2024-10-02 12:19:00 | TERRA_M-T | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e4acf9ac-5437-32e5-bbd8-d7031144fb43 | -22.51126 | -46.04602 | 2024-10-02 12:19:00 | TERRA_M-T | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 162598ad-345d-303e-88a4-a68e42197134 | -22.69299 | -46.99731 | 2024-10-02 12:19:00 | TERRA_M-T | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d19b1da2-bc4f-3620-aa5a-e4fbbaf65edd | -22.71525 | -46.67742 | 2024-10-02 12:19:00 | TERRA_M-T | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| fbc45551-d586-3440-9447-8d7e1844b0ee | -22.77155 | -46.82803 | 2024-10-02 12:19:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| b5bfa7e5-b945-35d3-a89a-e43eefc84633 | -20.87014 | -47.0396 | 2024-10-02 12:19:00 | TERRA_M-T | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |


[Clique aqui para ver as próximas entradas](README206.md)
