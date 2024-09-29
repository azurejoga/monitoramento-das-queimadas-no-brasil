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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ebcdd0e-ac2c-3d5a-88e6-e8a7d58744d6 | -5.56986 | -49.01188 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cae968af-ca99-354e-a62b-e833dd202a4d | -5.56743 | -49.01157 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f020f8d3-0556-391c-981f-942b7dcc0cdc | -5.55738 | -49.02032 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78b8f9d0-dde2-36cc-a092-ab02cf1eade3 | -5.55486 | -49.02 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee12e109-7102-3766-8362-0c45b326f0e5 | -5.55425 | -49.02341 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71746f86-72ed-3728-926d-2a17a5e43e05 | -5.27102 | -48.88555 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bff22fa2-3700-3166-b3c3-0784fc2ebcfa | -5.26789 | -48.88437 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1b88e9b-3eb6-3a1c-94ff-d3ffbfe2b866 | -5.26732 | -48.88774 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1fd018c8-2053-30ce-aa93-c2cde1a74f6e | -5.26568 | -48.88465 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d70f19d6-1b5c-3e77-a93b-c6ed0ff9afa9 | -5.21934 | -48.18786 | 2024-09-29 04:02:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31af1e71-46db-338e-93c3-794ce4e2eb2b | -5.21882 | -48.1909 | 2024-09-29 04:02:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b3bff66-38f0-37f6-a15e-66b48bbe858b | -5.96351 | -49.18337 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5001bfcc-9eba-38f9-8166-dd7a10737fd1 | -5.96135 | -49.18097 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df093a8f-f69b-3096-aee0-116a805c1780 | -5.96076 | -49.18444 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f1ec2b8-6e16-360b-a10a-4c3e24a952fc | -5.95874 | -49.17897 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 918e0f35-0a5f-38b4-ba1e-183ae0247add | -5.95597 | -49.18001 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cfae81f-18fe-3932-892b-ea6a6dfebf0f | -5.95537 | -49.18347 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a42e3aa-45dd-3b2f-a314-81a87e4090e2 | -5.93137 | -49.19373 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 471a0824-7b2e-3c2e-9f5d-eef69bfa57e9 | -5.57756 | -49.01673 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b77c7d3f-0212-3b6d-abfd-69fb9cc5cace | -5.57465 | -49.01618 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1249ebd2-dea4-37ef-8f69-33b240743ab4 | -5.55679 | -49.02374 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89e05f29-aaf1-31f7-9070-84e68c62bcf1 | -5.27161 | -48.88221 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 977da731-105e-381a-9d19-db2a4111e17b | -5.26508 | -48.88802 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc441af5-9c0f-33c5-bfdf-baea0e132faa | -7.58471 | -49.19185 | 2024-09-29 04:02:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5b72a53-debf-379a-bffc-32b2010ea300 | -7.59049 | -49.19072 | 2024-09-29 04:02:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 116af336-33a1-350b-b6ec-3c687be416ed | -7.59047 | -49.18996 | 2024-09-29 04:02:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0488552d-2c48-3f7e-8990-9b445a4390f4 | -7.5853 | -49.18948 | 2024-09-29 04:02:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a239540f-4635-3e1b-b9c6-b8fcf0ea988c | -7.58528 | -49.18873 | 2024-09-29 04:02:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8061bc4-cc26-3c92-bb1b-70281ce6b60d | -7.58475 | -49.1926 | 2024-09-29 04:02:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cde31de-8dba-3c63-942d-10df703d42db | -8.24263 | -49.38396 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaf8ced2-c2e0-3477-a150-81aee8caea04 | -8.24201 | -49.38736 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79353e92-cd54-3053-a60f-9b66ea848d40 | -8.23503 | -49.39587 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a183e3cd-6df7-379c-91ed-f8e3c4be0d6c | -8.23093 | -49.38855 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46ec0679-65ad-3fbf-b9e9-eaba31a74269 | -8.22977 | -49.3949 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aad7546-b283-3cc7-b5e8-7a0d5fadc923 | -8.22449 | -49.39408 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f23f3e5-0f05-3fc9-a0a0-c8f4237e19c7 | -8.02346 | -49.89997 | 2024-09-29 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91a05d34-6e0f-342b-a05a-96b08012f756 | -8.99629 | -49.82867 | 2024-09-29 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ff368be-24ad-35c0-ac1c-c5195eec77ee | -8.70688 | -49.60245 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d25fcf-b8ef-3046-aa35-7e63b7fdef93 | -8.7059 | -49.60246 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bda3272a-e3a5-3db4-b511-d7f5ced43645 | -8.24028 | -49.39686 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 143deb8d-f941-3542-9aee-daf29b077919 | -8.23618 | -49.38958 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4658fad1-e9ff-3996-aeae-f9f262b834e8 | -8.23444 | -49.39909 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5a11064-3af3-3624-9089-0ac2f273a317 | -8.23035 | -49.39174 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d496092-19cf-36e9-93d2-54df616c4dbe | -8.22572 | -49.38739 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3532bf5a-230d-359f-8115-8d8b2acd7943 | -8.2251 | -49.39077 | 2024-09-29 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69c67be5-eac5-3d54-a986-296146174892 | -8.02411 | -49.89645 | 2024-09-29 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f21c5003-b2c9-31e2-8650-f9ca0a2fa33d | -10.6313 | -49.91349 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a62ad7b-99d3-36cf-9be5-ed71fbd8f6c5 | -10.62669 | -49.90929 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88c7640d-77ca-3b77-ae9d-d40bfba57764 | -10.44906 | -49.17551 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7b04ad1-8174-38c8-9163-8c53a4d0ed3d | -9.57861 | -50.1957 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f9ad686-340d-3db1-ac0c-f8af8983bd65 | -9.57797 | -50.19923 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5f39290-ff34-3a47-9017-dc280c7c53a4 | -9.57732 | -50.20277 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9d2189f-9da9-32f1-8ded-8a8a380102c5 | -9.57545 | -50.19165 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0272f873-ddda-33f3-98b9-1912d0e54afe | -9.57478 | -50.19517 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 640cba7b-9832-37f4-a2c5-8e30541167c5 | -9.57411 | -50.1987 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8dbc6e-72d5-3420-bf94-500698d1b27c | -9.57344 | -50.20223 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1295d895-e705-3844-96d6-1fe13a8d12e5 | -9.5732 | -50.19467 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf05eba-8e34-3193-b297-f6289b05f424 | -9.57277 | -50.20576 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e77f59f-2531-3115-95cb-f1f46a6f8584 | -9.57255 | -50.19821 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1920576-a9e3-33b0-be50-fb1f449bef5d | -9.57191 | -50.20175 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d70d27d3-79c8-3703-871a-a77bfc5d5570 | -9.57126 | -50.20529 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 246af29c-91db-36d1-895a-1d58a97626f7 | -9.56937 | -50.19416 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55d1946d-72d1-3e69-b308-c233ae8d738c | -9.5687 | -50.1977 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b309c093-6a16-35da-be66-b0f2d23c1b7c | -9.56735 | -50.20477 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61ca19a5-6e09-3c54-8c50-1407d685dc2a | -9.56713 | -50.19719 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7ad41b2-cf2e-31cc-b704-a444c20f09bc | -9.56649 | -50.20074 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36e337f3-7647-3686-a2fe-26b88b44de95 | -9.56584 | -50.20428 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f98f42b6-15b4-3a0b-95c0-e524ad58602a | -9.43319 | -50.15423 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0189837c-fd7f-380e-9012-74c392d404a2 | -9.41079 | -50.03457 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e9d0e8e-bc46-379f-b40a-cf78569cdabd | -9.39089 | -50.00727 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee0f1172-a426-3d5b-bf5b-8ab9567ac09d | -9.38847 | -50.00555 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31927e02-1b22-3b64-a0a3-9d66e90135e0 | -9.38783 | -50.00897 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bdea3d3-a862-3a1a-a226-f05a46611557 | -9.38552 | -50.00629 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 482aa977-5da4-36d0-a603-716fb1034d25 | -10.10444 | -50.00742 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9421ffc-eb5d-339a-8db7-e305ef7aa5c2 | -10.10382 | -50.01075 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91766eed-dc2e-3753-adca-894b4841364b | -10.09913 | -50.00644 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e2c1704-5dc6-3e98-8f76-a22b368f8e2e | -10.09851 | -50.00977 | 2024-09-29 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b90eeb61-783e-3b54-901e-2c96a5994b58 | -11.0383 | -50.62242 | 2024-09-29 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dafa4fb7-7bcb-30c9-b04c-778173014774 | -10.94616 | -50.11246 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5abc53ec-913b-3501-bb90-7f33999dfb91 | -10.94554 | -50.11576 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4263f923-93ca-3c8f-ba3b-724f42f9dbef | -10.94214 | -50.10487 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e234b8-93c1-3779-a3bf-0fe2292e6619 | -10.94152 | -50.10816 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f2819c9-56d1-3338-a788-7c9e7b9551fc | -10.9409 | -50.11146 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6a4424a-17ed-396a-ae2a-13a0d0b0f5db | -10.94028 | -50.11477 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25a3bafd-66d8-3a11-b072-d0f5fec8f2cb | -10.93966 | -50.11806 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19f4d0f8-392a-39fb-8278-fab949fbb34e | -10.93904 | -50.12135 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 340d23d4-9fb8-3494-b843-e9802b3a2554 | -10.93841 | -50.12466 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d82f2f7-861e-39ca-9ca5-a07c0ae07fbd | -10.93627 | -50.10716 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9bef51d-e1d6-3589-a63d-97b64e9b6944 | -10.93163 | -50.10288 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1088e3fc-fd03-36c9-952e-a287affe5c36 | -4.84378 | -50.92809 | 2024-09-29 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec991306-2d66-3c77-be6d-a22c13f4004e | -4.83767 | -50.92686 | 2024-09-29 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea29f0ce-6f2e-3907-b7cf-ab7e9e4b81f9 | -4.83678 | -50.93187 | 2024-09-29 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c64ab693-6dd5-37c6-ab96-7649d172265e | -3.57368 | -50.57209 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f95f1968-3633-308e-b073-403962268585 | -3.57213 | -50.58131 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6205517-256b-3dfa-a56d-5f3b7c0148b5 | -3.57188 | -50.58361 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 43e275f8-e6ea-3851-98fd-6dd954332ae2 | -3.56939 | -50.37515 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c47718e7-f58a-3e9c-84a9-4290063f42c4 | -3.56758 | -50.5709 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a5bb446-d58f-31c7-93b8-97c6b01bb0d9 | -3.56658 | -50.57784 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 48984a4c-23a2-329b-87d6-25b4130ed923 | -3.56603 | -50.58009 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cef26fc1-3f3b-31e9-b2ee-8e8c6823eea8 | -3.56577 | -50.58245 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README27.md)
