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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 883ff82d-1ff9-3dca-9f11-8e197ae0e70f | -12.62286 | -47.27561 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6df59e2-1420-3827-8e98-b57e20c78db0 | -10.80399 | -48.7331 | 2026-09-28 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 64e70b77-d15f-3e10-9229-2157834536ae | -12.86859 | -44.8007 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ab15d81-6425-37e6-afbc-8c50797a2a39 | -6.82168 | -46.14081 | 2026-09-28 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e887dec5-401d-3b11-ae5f-fac90710498d | -7.99282 | -44.81985 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cdafac06-d155-350a-9bbe-8a5fa041592a | -6.66515 | -55.10839 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63966676-21dc-3ba2-ae2e-3a8300f15878 | -9.82335 | -45.2685 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 720ec087-4655-320f-b660-acb01165ca71 | -6.66625 | -55.10116 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bed1f86-5dc4-3d40-8a5d-956767803e92 | -7.82565 | -55.13499 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bc5a497-97dc-31e6-96e8-625bb8413c83 | -10.70623 | -50.47572 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a50aa4a6-7452-32f6-9195-461daaae100b | -10.72203 | -53.9956 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38eac16c-4e71-3afd-9a3b-268c5531256e | -8.6513 | -45.35133 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79742723-d9ed-3be4-99d5-81ec928b4b6c | -9.1705 | -61.40913 | 2026-09-28 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 67214fe4-4128-3c29-bc8c-1c511535b442 | -10.1626 | -46.57745 | 2026-09-28 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9933ac6-d874-301a-b69b-871684acfbb7 | -11.18913 | -44.80904 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| f1ea62fe-68e3-35e2-8640-eb600f7f962c | -12.74301 | -47.29326 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a34385f3-77fb-3203-8cbd-5083b26d68e0 | -12.15651 | -50.36286 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dab92c4c-3434-31a5-8677-8c4403c6fcf1 | -11.19682 | -44.81016 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9ac5b1db-6e12-30b6-9113-407f08631b93 | -7.82486 | -55.13962 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed245b62-e81f-3edc-b112-023af7885b35 | -11.74097 | -50.66447 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24821761-87f7-3737-a3ed-f6529aa4b648 | -9.07957 | -49.8721 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29a1092c-635c-3bc7-a0ba-40e6c86f7967 | -11.69374 | -44.52531 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5cd2b1b-1f47-36ef-afca-914fc0f829b4 | -9.15875 | -45.61269 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ce5b5f2-fa94-3d5c-a0fe-ab147843fae2 | -10.89534 | -50.68643 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6f6abc1-5181-3c8e-922b-9fa0af614550 | -8.25564 | -45.40294 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cbb73308-a815-3c38-aaa8-0e0a09265784 | -12.31655 | -46.41523 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c72ca4c3-0ec7-3592-8a7c-8dc9d5d968c7 | -10.4846 | -43.13262 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d370a00-2824-32a4-9d0b-8ab359dbe64b | -10.4191 | -53.8344 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74630801-1300-31cc-b091-6d5f44b28a61 | -10.42306 | -53.83507 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20ac09ba-2437-3d10-ad70-668342404a3e | -11.63141 | -46.7789 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88bc1c98-4b85-30e7-be70-f8061017e6ce | -11.70875 | -44.5327 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bdd84f94-6278-36e0-916d-2f07d2ad22ad | -13.20165 | -48.32563 | 2026-09-28 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab31a8f9-3365-3c2c-a111-44b1a8a30aeb | -11.43931 | -44.92078 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f83defcc-1c54-3ca9-bcb6-244081a7213a | -13.55987 | -46.36576 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea241c75-53d5-3611-b51e-aed5a91599c5 | -11.70362 | -44.53854 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e01a23bd-b805-319a-af01-c61049709013 | -11.52872 | -47.35755 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd10e9b6-01a8-347c-9e1b-46859b0b9793 | -7.03584 | -42.85862 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| adfd4e6d-7131-35b4-b678-73a0f0249aad | -10.21617 | -49.98282 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd09dbab-15ab-31fa-bcaa-ba783994c2c3 | -11.19505 | -44.79493 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85791e7c-22b8-3ee4-8f3a-1227ed58b66c | -9.74885 | -48.95326 | 2026-09-28 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f38c557f-4c77-3d29-9918-0d7e145ffe5f | -9.16974 | -61.40408 | 2026-09-28 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 9c049d52-9a05-3996-ad6f-ff5861524690 | -12.5946 | -51.96341 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd1512f2-bf67-3dc9-8467-cacfe32ed8ee | -10.89196 | -50.68588 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cf1949e-b804-3c4e-a6f0-9fab65a3eae9 | -6.08443 | -57.79587 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8ab6154f-50ed-39af-bd65-fc3ac0a2c051 | -9.32669 | -45.36878 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60be7145-e768-3e5d-b36f-efc800bfd89a | -11.70772 | -44.5117 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd399083-1de6-3e4f-b345-5844f9b85ae3 | -9.19734 | -45.76383 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0bfbbe6-7f3f-3b06-8c7d-a9d41557f327 | -10.82419 | -61.4074 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1604db72-2c06-3814-bcf7-038116667476 | -11.37727 | -43.3909 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 898ffbf5-009e-376b-949c-aabc9d6e376e | -8.23532 | -45.44169 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 191da81f-4d65-3ec0-8c5d-49b13298740b | -12.31298 | -46.4147 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc7c143f-aa1a-3a46-ac9d-04d11fe2021e | -11.38044 | -47.43137 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15d1f662-6468-30df-9871-d19dcd17c64b | -13.0819 | -47.41886 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2573ee9d-7683-3db1-9e7a-578470ca0f25 | -13.09857 | -47.4013 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df33419d-b21f-3917-b530-62f1568b21af | -6.73956 | -55.08643 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f4fd15-dbb2-38b9-a9ab-bcd21b9a827e | -6.70462 | -45.58956 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f285a847-f9e8-3846-95ea-a1c8e3ce7ee6 | -13.57195 | -46.35891 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1187695d-530b-3e01-b5f4-2897d583f5a7 | -9.98204 | -50.15018 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b8727f69-e76c-347d-97ad-a38270768dcd | -11.8387 | -45.00109 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c80a544-02c3-34bc-858f-68793d3b4582 | -6.70231 | -45.65264 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52d158f0-12d2-3a1a-b378-bd7f690f9a79 | -12.16088 | -50.37825 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4dd5f071-7d4e-3362-bc5d-b43734c60db1 | -13.15415 | -48.54793 | 2026-09-28 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b1018665-a7a6-3513-84d8-623f1010d0c5 | -10.20724 | -49.996 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ade68f6d-0a36-3312-b21a-43bf21f92a2c | -10.20163 | -50.00972 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3d6aa4f-af56-33f6-adc5-7d55184335cb | -7.33238 | -42.08237 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c063fd25-d31a-3933-9aab-7ec2b762bf8f | -10.2039 | -49.99546 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb1f4221-970b-3171-ac07-214398626239 | -12.06044 | -50.21905 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd4f81dc-e185-3808-b7d0-5985df03b9f5 | -11.70893 | -44.5289 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 123d006a-fe08-3eb0-9c81-5b5cc09edb26 | -11.72081 | -50.66114 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d79de343-af8e-3995-86ca-d45b31d052bc | -8.3702 | -45.46085 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d078a9d-477c-3bea-a1e4-05bd29e05958 | -10.54378 | -57.43843 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a6ee10b-4679-336a-8b59-1c2c4c2589f8 | -6.00184 | -47.3942 | 2026-09-28 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 39e5b687-878c-39ae-b9d0-c43ffc7c36e5 | -8.23354 | -45.47874 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77a8421c-aa5e-34ec-ba6e-8eddf5b758a2 | -7.3766 | -44.76495 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1719e37-0939-327f-94c9-dbed1e0e238a | -11.1434 | -50.05763 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa47abb2-0960-3d78-bffa-eb0751db4593 | -9.14345 | -49.96683 | 2026-09-28 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e72e89f-4c63-3812-8eb3-566debab80dc | -10.92475 | -50.67619 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49d5ad0a-d4a4-37fc-abc5-c73422c0d73a | -10.82457 | -60.74645 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2594262f-e1f5-382a-9bc1-e517f0b49667 | -11.62735 | -46.78229 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15e6ce1f-b0f9-37ef-b6c1-ebb523163bf1 | -13.07862 | -47.44104 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c373d68-6eaa-3d29-9400-e233b6ae48be | -6.94345 | -41.61652 | 2026-09-28 04:34:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ddb74888-d262-3a3c-b836-cb8de5dec472 | -11.37664 | -43.42723 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85039c0a-ac83-37c7-8303-37799ef6de4d | -8.24071 | -45.42979 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bcc38b45-b61d-3134-9caa-a7d57d74f897 | -7.89068 | -45.44765 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fae0035-0b53-33da-bdfc-ccb0cef0791c | -12.14263 | -50.34595 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 663f1475-84c8-3b2b-b734-eafbb7d9032c | -10.21838 | -49.99049 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c405d5eb-dfd5-3ccb-a040-6e3fb7f949eb | -9.82029 | -45.26376 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b52a7b98-a6b8-3d46-ae7b-168beea2ffde | -10.88853 | -43.68593 | 2026-09-28 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c93cf944-1cb6-32fb-a9d7-b111095b365b | -8.23592 | -45.41257 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c9f9a0e-6838-357a-b078-fab787f1f1c1 | -13.10321 | -47.41754 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0b404beb-97f6-3586-9196-809b5af672a9 | -10.92535 | -50.67252 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0815844b-5664-3154-9a75-fe089749a675 | -11.12953 | -50.05902 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 53c6f251-5a48-3081-9522-62394bf413dd | -6.07016 | -57.81226 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad258b0d-cb94-35c0-9b39-88c438108684 | -10.40195 | -53.81568 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e7ae56a-5883-3918-8a3a-413e7359dfa7 | -10.21227 | -49.98585 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d078cff-8611-3bd9-b730-3f7ffc06a9d5 | -10.21278 | -50.00421 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c36bcbc-dce9-376b-b416-1f070394c719 | -10.82257 | -61.41062 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 36fad7f7-4ffa-348c-9864-923416c5e730 | -7.93583 | -45.46255 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4e25e52-0bbe-3b02-96e5-27c04e0290c3 | -8.66883 | -48.96552 | 2026-09-28 04:34:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5d22f58-e11a-32d5-8b02-3a60db06c0b0 | -7.71606 | -39.35062 | 2026-09-28 04:34:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
