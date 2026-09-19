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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01235015-033c-3497-b64e-2c74c2a71d0f | -9.8837 | -49.093899 | 2026-09-19 00:41:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 484eeb27-3ac3-3510-81e0-14c2e8b332f5 | -5.8598 | -52.0298 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3975fc5b-3e9c-3832-9620-8c38f768fe37 | -5.8471 | -52.065399 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5073f316-138f-3be0-905c-ace2e7a5d6e3 | -7.8581 | -44.8759 | 2026-09-19 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6291934a-d202-3c04-a00a-d3c6933115ed | -3.4266 | -50.6595 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f196f85-efe5-3295-9692-2c0d1874a61d | -13.5921 | -46.946301 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8f91618b-5407-3ff2-be62-ea015d48a03e | -11.0756 | -48.3041 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7abdc694-e9b8-3057-b123-279fda37625c | -5.523 | -43.7882 | 2026-09-19 00:41:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0037c401-7c99-3e46-933d-51a162029c11 | -11.4231 | -51.4519 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83c8942e-83a4-3273-91b5-4ac25fae7a14 | -8.3908 | -45.637402 | 2026-09-19 00:41:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2901bb3e-ccd8-3833-84e2-3021eaa50f3c | -9.5625 | -45.481499 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 05295cbf-d0d2-35c9-841a-48015058ea12 | -4.4353 | -44.3671 | 2026-09-19 00:41:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa2f2c3f-285e-34de-a613-ab7253f5b384 | -11.056 | -48.308601 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cdeacc9-dbf7-3b41-bcff-a769ae770460 | -9.0359 | -48.719101 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e983695e-a050-3836-8fae-0c9851fde975 | -4.4219 | -55.5224 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 337a1120-a985-3dea-9ca5-3ff716d82851 | -8.4398 | -45.756802 | 2026-09-19 00:41:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ead0a04-c1c3-3a17-8118-77660a69f59e | -18.398199 | -49.158901 | 2026-09-19 00:41:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d150a2dd-81c0-387d-8b7f-17c1def1bc9c | -1.2042 | -49.114498 | 2026-09-19 00:41:00 | METOP-C | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 129107cb-9087-35aa-af12-0cdf08bf66e7 | -8.4653 | -44.5224 | 2026-09-19 00:41:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0cda0889-1512-35b0-b7dc-d9c0a754ad00 | -10.0226 | -51.8993 | 2026-09-19 00:41:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85c8de93-7209-300c-8c3c-fa7e50bc20ef | -8.8388 | -50.446602 | 2026-09-19 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe4d167-497c-35da-af81-1e4c88ca1520 | -18.4097 | -49.164799 | 2026-09-19 00:41:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 263a35a8-5880-32bb-836a-97a300354718 | -8.7655 | -44.2253 | 2026-09-19 00:41:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f44788c4-2e9c-3f51-9213-6e5d338d5165 | -1.2195 | -47.7076 | 2026-09-19 00:41:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebe71e7e-c208-339e-a607-1c94f1bf9aee | -3.5186 | -50.7911 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66fc04c9-9723-3810-b8cd-98d5d51d6693 | -7.2142 | -49.637798 | 2026-09-19 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7918785-fd72-3438-ac85-3e58ee76c60e | -5.8451 | -49.872898 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1c1e5a-6ba7-3313-b6cc-8707a7142d00 | -5.5258 | -43.799801 | 2026-09-19 00:41:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0646b28b-9452-3d59-bb5b-9b5a0cbb35ef | -10.8808 | -54.051399 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc27c4a-25c9-3c06-b92c-bcfd6522fe07 | -3.3338 | -50.119598 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d50b1bae-1da8-3303-b02a-6130372277e9 | -8.4191 | -54.717701 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4526d2-8149-3e50-bc55-dd6d61e376fd | -12.8641 | -46.341 | 2026-09-19 00:41:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b8aa194-a552-338d-a79d-d57464310eb5 | -11.3468 | -44.128799 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb90da3e-d8e3-3f84-9943-3252ff7d81e3 | -3.023 | -51.193699 | 2026-09-19 00:41:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce496d67-cbd0-3874-8f10-bcfb53cbd9fd | -4.536 | -54.930099 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92cae729-aced-35ec-ba5b-b382b8244162 | -11.4023 | -47.296501 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10dd8be8-8c56-3387-aa19-a6e11195cbf0 | -13.0212 | -46.931702 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec60b60d-34e8-3a9d-bc7e-e0fb560aca3f | -12.6975 | -45.937 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc53f72c-d6d5-3f55-8be3-387e1b3e908e | -10.968 | -49.750198 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca9cb0fd-6c6b-38e8-ad05-9f6d82ed97cc | -5.2305 | -49.3064 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08afad7d-aa78-3aac-bead-1d027ced7265 | -4.5017 | -54.960201 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c63651-ed72-35ed-aa7d-fd2a7788a234 | -8.8659 | -49.7421 | 2026-09-19 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7783042-c62b-3811-a1aa-33be9a21acdf | -3.3795 | -50.453701 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f362f4-678e-3c95-ab49-6dc71988be90 | -7.0011 | -49.743599 | 2026-09-19 00:41:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9759c06d-ab6b-30d8-8247-ca61e5e29fc0 | -8.4359 | -45.740398 | 2026-09-19 00:41:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa185050-4b07-3643-862b-678edf5c6125 | -10.8832 | -54.063301 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b282a3e2-5020-32dc-84ea-f71f553c2c2b | -7.6564 | -46.112701 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc94f817-aae2-3ae6-9fed-e82c3a5734e6 | -12.2807 | -49.174599 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64e99060-3c6b-3e7f-841e-946e3608c965 | -3.32 | -59.7915 | 2026-09-19 00:41:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 517ca335-90e6-399c-bae0-fe918b4c8e71 | -12.9902 | -46.976398 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fce75386-89f5-358d-b4a0-9a32bc8c43b4 | -12.9931 | -44.8255 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4140822-28a5-3d70-be69-923c92c2b662 | -11.1168 | -45.281898 | 2026-09-19 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56f378c4-4ff2-3f68-a32a-a6bf8703e8d5 | -7.8753 | -46.428398 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0e193d3-b9e6-3fd8-8ddb-d8b4ebc50dbb | -4.3634 | -47.7873 | 2026-09-19 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab2c0043-36d3-3fe0-b602-229a4e6e6e01 | -10.5255 | -44.839699 | 2026-09-19 00:41:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f729a8eb-8c7b-3814-b6c5-4776a766db68 | -13.0016 | -46.981098 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c02adaa-6bac-304b-b712-779c19c1e5ed | -18.3999 | -49.167 | 2026-09-19 00:41:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd22df71-5393-3837-9f62-e3627a43bf2b | -5.7522 | -57.440701 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8fc47b-adcf-3b39-845c-03dd071fbcf0 | -12.8624 | -46.333698 | 2026-09-19 00:41:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6e4d5b5-9ce8-3007-88e9-28c517a8b32c | -3.7246 | -49.039101 | 2026-09-19 00:41:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ba823c-7d5c-3479-89f4-c6b0a82fd133 | -10.6084 | -50.262199 | 2026-09-19 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e942054-bcae-3cd1-9889-e26b80c863ee | -8.7716 | -46.904099 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cac5ba05-fb43-3d3f-8ced-6f70f56dce93 | -1.5905 | -54.438599 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f600c7b-bbf8-3d6f-9d74-30b514cf3a37 | -11.0772 | -48.3111 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 834a7952-c4dd-3321-bcfe-835fe7f77740 | -2.387 | -48.5186 | 2026-09-19 00:41:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2d4daf8-bcc9-3a6e-91c2-459123b4ec38 | -4.58 | -42.951698 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 384dbfda-7321-3cfe-8540-7d78d5e5eb80 | -6.0124 | -51.793098 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4970a8d6-7063-3669-a03b-94ed015a1374 | -13.5905 | -46.939201 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f176b126-6eb0-3c3f-8761-b88583ad31d5 | -8.8747 | -45.936001 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 201de606-9a5b-37e3-8b1d-c5014d5c204b | -11.0545 | -48.301701 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6141ecc3-290a-3f38-a751-5800631e9ce0 | -18.8715 | -49.515999 | 2026-09-19 00:41:00 | METOP-C | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90636350-d0b3-397f-a36f-0f1d62cb1d47 | -12.6895 | -45.946899 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8c31170-25fb-3722-9317-fd9b01f49904 | -10.2719 | -49.997398 | 2026-09-19 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 330a87d0-3530-3dd8-9bae-abaf0527d765 | -12.3914 | -48.471802 | 2026-09-19 00:41:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33c3e1c3-fff1-3c71-b4ff-447f758a7213 | -11.8312 | -46.829399 | 2026-09-19 00:41:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6bcce06b-5d65-3aca-9798-670e6fddc772 | -10.8255 | -50.921799 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1364824-9726-3c59-acea-7879d47f01b7 | -9.0143 | -44.916 | 2026-09-19 00:41:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8d06481-11f6-33b8-aff3-1a17391cad24 | -9.9627 | -46.609901 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac8c6c0-881e-3b2b-b7e9-3c67b8530082 | -8.8405 | -50.453899 | 2026-09-19 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d13ad468-e7b5-30fc-b348-395626bd31f0 | -11.0674 | -48.3134 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d82ca00-fbd4-325d-b0fa-f2bfd919443d | -11.0807 | -48.281101 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 058209b5-3ae2-3d4b-aaa1-92af27842f49 | -11.3067 | -46.7938 | 2026-09-19 00:41:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8247bf62-6a63-3f99-9cd7-d091d5fd1f59 | -14.9634 | -47.5369 | 2026-09-19 00:41:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e8a3932b-f28d-3544-b934-447245c51948 | -12.5431 | -47.096401 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e1e3400-6c57-381b-9f09-5cd88d88b2e7 | -5.7559 | -57.457401 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0807b73f-6b11-39b5-92fd-10941746babf | -12.5911 | -49.089401 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9da52e0-ff06-3cb0-a767-55462e6f9eb9 | -6.4972 | -43.8088 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5695f40-dd3c-3e51-866a-b578c111896c | -12.1531 | -46.9716 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3985723-89c2-33fe-b029-b6766af74d5f | -2.8148 | -50.465 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7449fb35-08f5-307a-bc8e-27f891d98c39 | -4.0488 | -56.237598 | 2026-09-19 00:41:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0819e82-8764-352c-bda9-6fbbb145f9e2 | -12.6877 | -45.9394 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8b66245-7399-30d2-a78d-ec76189131f9 | -9.9131 | -46.5746 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c1570f6-2243-3819-87a8-5044db46e3c7 | -2.5845 | -48.436001 | 2026-09-19 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eccfe3e5-d6de-38b3-9fef-5af6aab761b9 | -5.2427 | -49.404202 | 2026-09-19 00:41:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b55f9d06-74a8-3724-9e0d-bf19a93492ef | -9.0323 | -48.748901 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9c76e18c-adec-38c1-9c7d-4211d4726769 | -11.3588 | -44.135601 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1644d1e2-d85e-3e13-b09f-057ebb7b68da | -3.7568 | -44.372601 | 2026-09-19 00:41:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81e9d109-d126-3e4d-85fc-20c1622bf1b4 | -14.6901 | -46.648602 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8398c424-1bda-391a-b172-0fb07cd4cf85 | -4.5574 | -42.985802 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcbe10f2-612e-3aa8-9e07-ea4eaaa782f2 | -14.6721 | -46.660301 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
