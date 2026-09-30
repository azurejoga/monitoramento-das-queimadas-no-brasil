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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61ca5741-0554-325e-a7fb-12722e75d4ed | -3.71318 | -54.22604 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af4df68a-e3ea-30e4-9816-6f1302375636 | -8.38924 | -45.45142 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5c39527-31a9-3831-bac0-194d3fd55841 | -10.7128 | -47.82696 | 2026-09-30 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d8cfae6-0e6c-3eb9-b2c7-449096677de4 | -5.73014 | -43.28294 | 2026-09-30 04:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e9104fc-e807-3a91-a600-3b08b5108b8c | -3.373 | -50.95467 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e03c8522-057f-346a-8425-d1c970cc28ef | -7.68094 | -45.95948 | 2026-09-30 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb6dae8c-b92a-3faf-a3a2-3d8c4872b4a2 | -2.75236 | -54.67646 | 2026-09-30 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 611d682c-4f16-34d0-a307-59c10422eb7e | -3.37907 | -50.95917 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77965b56-ea17-3596-9d9a-e6f45bd685fb | -14.92017 | -51.86859 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 413107a2-9f08-3c4f-b559-8ba7cd096817 | -3.18491 | -51.24056 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f6e99a1-39d5-3c71-b313-edd281a19d6d | -14.1259 | -46.26099 | 2026-09-30 04:53:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef4a7ea4-6b9e-39b8-a07f-ffdb706976a8 | -4.28765 | -48.6065 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc36e5e5-d259-3545-8f34-80360d1d9d2a | -4.02746 | -54.20512 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da07ed4a-561b-3e22-a1ca-7953d364faf8 | -5.76308 | -45.17788 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7afa7e3-3d99-3d41-a81d-993636814cba | -15.76061 | -46.04177 | 2026-09-30 04:53:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ae6f5fb-8a75-36d7-86e5-520d2c68ca87 | -18.07424 | -44.36652 | 2026-09-30 04:53:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 193bc628-376c-392d-81b1-f5d4b27f276f | -15.13196 | -43.62313 | 2026-09-30 04:53:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc2d3702-1168-3cc5-9fc0-d799cd0e61da | -5.0262 | -43.57188 | 2026-09-30 04:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e89a2e6-7ebf-35a1-a2e8-daab909e8747 | -10.64974 | -50.72176 | 2026-09-30 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86792d0e-c507-35b2-b2c3-94015e659aff | -6.13235 | -53.29745 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 746696ad-568c-3337-a9c9-b324e9a31e05 | -7.33746 | -46.08995 | 2026-09-30 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1709ce9-2da4-357a-8028-2f5b359e44b9 | -15.19906 | -46.14315 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91a3b568-3185-3f46-abf0-f70dd900a94b | -7.51073 | -55.03524 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 038bb9c4-4c28-3f83-95f3-53495738e03d | -2.90407 | -54.09259 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| abf16868-56ea-39f6-b4dc-0dcfefc5653c | -8.48842 | -54.90836 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9e173e6-73f5-3ed0-9adb-c5b795898a1b | -6.70965 | -45.63644 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6cb4f3cc-8c31-3a21-bf34-15e09260fcdc | -5.72793 | -43.28421 | 2026-09-30 04:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e41cb240-9906-3474-8a01-b5e265428b01 | -6.3022 | -43.60746 | 2026-09-30 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b72df71c-0cb9-3fa7-8f5e-3176d0f65e37 | -10.6821 | -50.28382 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14330944-e001-33a3-b997-17a9484ef8c7 | -7.07793 | -41.75454 | 2026-09-30 04:53:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3c510ae-f184-3f7e-94ee-d8410f9788a3 | -9.54202 | -56.15984 | 2026-09-30 04:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a743bcdd-76a7-3f6a-bc93-531fcc0f1b73 | -6.13146 | -53.29663 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 650f10e6-5cea-3d06-ac99-4f527456770d | -18.07471 | -44.36232 | 2026-09-30 04:53:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17ca2353-fa0e-3315-b7b5-b4018f198a4a | -10.81424 | -48.74893 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f50d1129-f36c-3961-b94e-30994c2e7917 | -8.48771 | -54.91256 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49809428-ffd5-3cb4-92ef-57c99e117ce8 | -6.13084 | -53.30042 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60dba9f1-7c3d-3514-b003-97791b27ceed | -3.00997 | -53.87622 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c9f5a8b-4a79-37e3-a7b5-f932903d1327 | -7.49655 | -45.80419 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5b8c555-8039-34c2-ac03-96c59d4a4fba | -7.38791 | -47.01299 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2b0f1b0-ace9-3fcb-a273-bc22fd630e96 | -6.71229 | -45.9908 | 2026-09-30 04:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3b04425-95f8-3388-98d8-c9275ddfdf81 | -14.94064 | -49.74945 | 2026-09-30 04:53:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab57d19b-e0dd-3187-8f9c-37a87a0b85b7 | -10.81874 | -48.71838 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09e2c48a-9e12-33c8-9b8d-a9b5e68e798e | -3.00713 | -54.22099 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f1ba664-80ce-3abd-ab14-d0a53ecca87f | -6.4357 | -55.80254 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a40dbda6-c11e-36f5-90a0-3e5b0bc055fa | -7.42344 | -64.34682 | 2026-09-30 04:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19e254b9-c729-3994-9176-75a694986c86 | -8.30368 | -54.71331 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e342c83-6208-3336-96ab-4d8b792b50db | -8.64417 | -55.05114 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd8fb13-aa86-3081-8abf-b3b352c8092d | -12.11867 | -61.14752 | 2026-09-30 04:53:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 190184f4-4da8-3c14-bb37-af27d9c7f9fe | -6.82129 | -45.05219 | 2026-09-30 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edeb91ac-9a0a-3e88-ba72-891fa523522c | -4.95045 | -49.41457 | 2026-09-30 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5223736-a4ce-399a-acde-b4d097bd2e68 | -10.56057 | -50.8751 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5479b52e-792f-36ce-9f34-6b525222f989 | -10.75909 | -52.12809 | 2026-09-30 04:53:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b7db7c9-af9c-3b6e-928c-e81ab1621571 | -2.89237 | -54.11781 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a31f54ee-20ed-3b74-b821-795c9d562db1 | -8.36661 | -45.39135 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98f32573-5fa3-35bc-ad15-20db8fe8f32b | -5.09264 | -46.03872 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 307a905b-d17a-3e7f-bd50-1739f8f728cc | -6.32688 | -46.12207 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e322de6-00bd-3a5b-bf1d-dbffbc105e44 | -3.71687 | -54.2267 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba213e47-8bf6-394a-afb6-19be69db5d8d | -7.82976 | -47.93224 | 2026-09-30 04:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38dd3a65-a4b2-3fa8-80d5-7d097e551817 | -8.34686 | -45.98119 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b79b64e-4351-3837-aecf-f65ba88083bb | -3.81887 | -55.90661 | 2026-09-30 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 573c3724-1488-36c2-9ff2-407630d3c1d2 | -6.11012 | -55.70581 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0116c50d-bb10-3cef-b3fb-3f162077838a | -6.17589 | -53.28445 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 667b4a27-7a58-35eb-a48d-d2bf32db6666 | -16.67136 | -41.84997 | 2026-09-30 04:53:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 9dd02166-e696-3aba-a73d-f0395707b5cd | -15.25469 | -44.82171 | 2026-09-30 04:53:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e748126-7b3f-30a6-a951-842f42769a67 | -10.72009 | -50.49463 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbd93a4d-dad9-300d-ba4f-46bae061f1e6 | -4.30144 | -48.60866 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e4826c0-dc3f-36e2-b049-5382e653d74e | -3.96124 | -49.01566 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86c8ce41-9a70-3d4a-99e8-a13afd2b04e6 | -3.91477 | -49.37638 | 2026-09-30 04:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8f31bc3-2083-3cd2-83c7-41900de6e431 | -9.80681 | -48.21495 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5677c317-83ce-32e6-8e62-02d2fa9fee21 | -8.93893 | -49.78034 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7366b895-507b-33a1-ae5f-759f8fc74064 | -8.55955 | -47.78871 | 2026-09-30 04:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a963496-7722-3cf8-839b-06da7ce67560 | -15.95433 | -55.61573 | 2026-09-30 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5784ecf-2c4d-32a6-ba7d-262d08146f73 | -3.71246 | -54.23043 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4882ff46-a43b-3ec4-a6ec-f8680790b4f0 | -5.40734 | -45.90231 | 2026-09-30 04:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e992b2b3-df51-3e6e-96fa-9c8a9137c3c9 | -5.73709 | -45.05896 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b627869-18a8-3fd0-b7fe-45530ff6dd81 | -9.10226 | -47.17313 | 2026-09-30 04:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8e18232-e5de-372e-9178-8d96fbef1e1b | -7.43076 | -55.18228 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad29dbfa-2ac3-39c6-9d5b-bb208bbfe3eb | -3.18546 | -51.23709 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cae1ecd-0e0c-30da-8f23-1a8db45ae648 | -3.16191 | -54.09922 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d3fb706-6af7-389f-9eb6-b55321ff59c3 | -8.86639 | -50.68542 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5812a8df-8129-31cf-a498-2b19d514cece | -7.49193 | -54.97097 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a68fc45f-aecf-32da-a997-3b72af2a1a16 | -11.07015 | -48.88754 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e97d3d20-815e-37b0-88a4-96f229cbc011 | -6.78628 | -55.82204 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d3a6255-b421-3da1-ab9b-dd01ebaed335 | -10.72107 | -44.42663 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7abd364c-718d-3be6-b92f-9fbb274a1d28 | -4.28877 | -48.62212 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19370bd6-0be7-3f74-957c-c1bde544e4dc | -8.21335 | -45.46123 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29219ce4-ebd7-3054-b990-45d500d6a512 | -7.93273 | -47.37268 | 2026-09-30 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddfd3471-d56b-36f7-b0ab-743c6c7ba314 | -11.19187 | -44.84369 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b82698a3-3215-37e5-8273-9990cedf8fb0 | -4.31145 | -46.7737 | 2026-09-30 04:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7308cc1-cf3f-32cd-8f1b-30e4ce182c1f | -7.0767 | -44.36129 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fac6e3c1-b54b-3b97-a3f8-e2fe808a72e6 | -11.44059 | -43.43734 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b23cd24f-729c-3e2b-893b-611d348605df | -17.92066 | -44.40227 | 2026-09-30 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d26c9e7c-208f-39c3-b39c-239e59db3015 | -7.50076 | -45.80476 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ad860e4-6dd2-3688-bf1d-0e7ab9c2ad28 | -2.90478 | -54.08818 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 7a1d7452-006b-36ad-8c3b-0e6e78dac8c4 | -6.09845 | -53.09238 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbcd80ac-527c-3556-96ae-ad4324e3ea4b | -4.45772 | -47.92507 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e4e639c7-3347-3dd6-9cc7-5662632b7a09 | -11.71075 | -43.45301 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60abd9a7-b286-333b-a706-4e01040079fa | -15.62976 | -43.23386 | 2026-09-30 04:53:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d408c905-621d-341c-b275-14ee2cb5dd15 | -6.4872 | -58.53139 | 2026-09-30 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 872e6407-877b-343b-873f-1e38c5198f03 | -14.53262 | -48.29844 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README47.md)
