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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ae32a4d-e5cb-30c9-b82f-b912cfd806be | -12.80591 | -47.964 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 50f82acf-1577-3635-89ab-f4d16c81239c | -12.92781 | -47.96208 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57d745ae-82c5-3700-9bd2-94a375af8bd8 | -11.47332 | -50.77215 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8369c49a-21f6-33a8-a976-7325473eeb82 | -12.95944 | -48.04802 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a80d88c-b93f-30e2-8ba6-00e1c0882781 | -11.43834 | -50.47198 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82cc746c-7cc9-303e-bdff-2c0f3477c4ee | -13.94856 | -44.84221 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 271.1 |
| f18b3652-695b-3515-a92d-99e2542a0da3 | -11.47277 | -50.77565 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d20dd537-0866-36c9-b69f-02cd893bda00 | -11.45571 | -50.7765 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fec54136-258a-3197-8156-ca2d806d1c15 | -11.49039 | -50.79282 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dc8062e-489a-33f4-9904-973dd0ee17f2 | -13.93538 | -44.84028 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| dad13e83-1c7c-3d02-9994-2ee7904a4617 | -7.39554 | -49.9781 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41fb24d4-905d-3285-a2e8-7fc78dede5b9 | -12.09271 | -51.37669 | 2025-09-14 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e138f6c6-4aab-31ec-b88d-8cc8c771c988 | -7.38094 | -44.35358 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99aa5932-7a12-34cb-9b60-a984f6dc949a | -11.38572 | -47.3435 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 741dd7da-f499-3ca9-89bd-c8f1cf6d908e | -11.49092 | -50.76781 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27f9e02e-b418-3390-a724-8cd12d6b0f7d | -12.78918 | -48.00352 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| faacc3c8-2e95-3786-8a80-a54056b98272 | -12.61917 | -44.20258 | 2025-09-14 04:40:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d726547d-6998-33c9-944d-cc0f6b4778eb | -12.14112 | -47.57859 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 239fabda-047e-33c6-9091-896473dfd506 | -11.37733 | -47.71477 | 2025-09-14 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72b8c4cf-326d-3186-8ce9-df85ec767e8c | -11.69236 | -46.89452 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e9c4dea-f911-3312-ac9f-502f765a8fbe | -12.79048 | -47.13694 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e891618c-0108-3853-8a2f-4cf9a91d0b64 | -11.44219 | -50.46901 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c9d113da-d9e4-3d0e-a17f-ad27f7d8d5ca | -11.46122 | -50.78455 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d340efaa-797a-3cf9-98db-783b37628819 | -11.48502 | -43.61441 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36d6d5d9-a577-372b-a6e2-56c738dd6448 | -12.0949 | -51.38428 | 2025-09-14 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fef77d76-4b64-3df2-b1b1-0ebcf018d169 | -13.9657 | -44.81354 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c20d210-3597-3062-9611-20dec7c7a70d | -11.48599 | -50.79929 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bfd3c521-c4b7-3018-9ca0-0ac23139cdd8 | -12.80109 | -47.97198 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d7b67cf7-cf1f-30e0-9bc4-3a0b54dbac3e | -11.83278 | -46.3665 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f4e51d22-b57a-3f35-8c17-9d9cf3ff79d8 | -6.67853 | -45.51811 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe44ff02-5029-397c-8d92-7cce44846c4b | -8.11678 | -50.17453 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba10e9d8-06a8-3214-8788-22c83bd27023 | -13.93483 | -44.84461 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| ea96fa13-03f1-3206-aa20-432b9976b6e5 | -11.39505 | -47.33416 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d0fd567-f774-3271-a94e-b605ed7cd44f | -9.52028 | -54.62969 | 2025-09-14 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 031faeb9-c965-3b9d-b281-bcfbac018b54 | -11.48432 | -50.76675 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed88140c-337a-3914-a5bc-cd456910636a | -11.06765 | -43.23621 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 154c9ec4-06c2-318a-870b-5a269a3bf0d2 | -12.82077 | -47.95216 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b54df13-a4b5-38c4-a291-2c60924e1b92 | -12.80543 | -47.13922 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ca90ebf-9166-3a02-a74d-2e693a4a5e9a | -12.93318 | -47.94993 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3db26e82-2939-31b3-9f3c-2cd7afc8b806 | -11.11126 | -50.69569 | 2025-09-14 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9160544-a0ca-3bce-97fd-938da7706864 | -10.92982 | -47.18905 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d828ca8-499d-3448-a77e-517d187f0d0c | -10.34377 | -48.83004 | 2025-09-14 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1ded3808-b57e-32b5-8422-dd8b172e4154 | -12.76719 | -48.00402 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 047070ca-8b04-375a-859a-d15b6c466446 | -8.94245 | -46.18309 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ff030c6-634e-3236-b9f2-704ff18e37d3 | -11.48652 | -50.77427 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b2e39ba-1f2e-3d79-a893-cc4d02654f6e | -6.8023 | -43.40032 | 2025-09-14 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8125b6a9-82e1-3330-8f2d-6be12b884b8e | -9.05608 | -47.02837 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85b22043-eaf1-3589-b0e1-3abc9471bc3d | -11.13917 | -45.32793 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7bba8c8-8929-32e9-9122-24935566d507 | -11.4535 | -50.76897 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca0daff4-bf20-3886-8872-e56d21bd7adb | -8.13733 | -43.66015 | 2025-09-14 04:40:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 408097ea-cac3-36de-bd42-981f60849355 | -8.93268 | -48.65666 | 2025-09-14 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ad93d0b-15cd-360c-88e4-800569597c73 | -11.62895 | -47.37004 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66eed69a-000d-3eb9-9fc6-d9854c8821f9 | -7.50607 | -44.67452 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f98596f0-202e-371f-b97e-415aea06a8da | -8.76627 | -46.03856 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4f7629ad-3b8a-3655-aa75-f7da1cc3fb4e | -11.13362 | -45.30814 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8993b809-0932-3f4c-ba14-47cc441122ed | -6.1414 | -55.78773 | 2025-09-14 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e92ec62d-76c1-3854-8314-2a80390c310f | -8.91438 | -46.16466 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9516a2a6-abf3-337b-b363-017d3be68275 | -9.7707 | -45.39296 | 2025-09-14 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0edfa34-3560-3efe-a2e7-2916abefcca3 | -11.24218 | -47.63 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8a2f7d5-49cc-3ed4-a1e7-a83311ceee6e | -12.92 | -47.94993 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a09477d1-c9cc-3658-baf5-95eacdd9d756 | -11.50305 | -50.79844 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f2bf3fa-0b85-30b0-a2e2-c54d4ab702f1 | -12.74279 | -48.0214 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 30dab663-32c1-33ec-abbe-b9b32aecbeef | -8.11624 | -50.178 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f809cca-8f80-34d6-87f3-2433a912984e | -12.81225 | -47.14495 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b164c56c-396b-30ab-aac7-d3d42387e07b | -11.63259 | -47.37056 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf5e08b7-f04a-3044-bbf7-6f2d844394de | -10.96599 | -49.56627 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81882821-b3f1-3aef-86bf-b866afefcf66 | -11.4665 | -43.57723 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3d64948-bc95-3325-8fcb-af71ca510e08 | -11.46452 | -50.78508 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcd24bfe-3cb5-379e-92e8-cafac5f36c65 | -9.82183 | -47.17308 | 2025-09-14 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35598b60-9636-30d7-b548-00c38626d863 | -12.75707 | -47.99825 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c44d0d36-2b9f-303a-bfa5-df417d0e6b0e | -9.02609 | -47.03221 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5499ff03-f464-3c19-9aa3-6551c223626c | -13.94193 | -44.85893 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f72e5f2b-530f-34f4-a070-21e0a5944f4a | -12.97305 | -48.00431 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58152925-e827-36ad-ad86-3c72f8134acc | -12.7529 | -48.00185 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ffc7555-8ef5-329c-89d6-aeb565802bea | -7.04405 | -44.67703 | 2025-09-14 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8af5accb-5726-3be1-af64-08bb2d4b7f09 | -7.37624 | -44.33821 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3604c523-ad22-3bc0-918b-70b56f59c65e | -10.43903 | -48.61377 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19f0e07f-2683-3464-8a50-3de89235e374 | -11.39869 | -47.33463 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d9f2e2a-f30f-35a7-9d61-03a0f960b7c4 | -8.90994 | -46.1688 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38947323-c8b0-3718-98ef-d225250330d3 | -11.47769 | -50.74417 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa1201f1-231c-31e5-8765-6c07b4b45d93 | -12.09546 | -51.38076 | 2025-09-14 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7ca5c95-cf9a-3a21-8df6-cfff40b56923 | -13.94631 | -44.85962 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 284d7f34-f660-3b83-a608-15b1a07cb452 | -11.46947 | -50.77512 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 62293716-c022-3ed0-bf6c-50fb43847613 | -11.30069 | -50.82995 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cfc6ab4-88a2-386e-a140-45c4dbdd1e82 | -11.47001 | -50.77163 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a8377f53-bcb4-3918-a62f-1c9b78cfadf7 | -8.49381 | -44.72055 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9d3025b-ad29-3a64-8175-a877fe434214 | -12.08676 | -44.72852 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4ad43f8-568d-3402-b126-08928f2f0cc6 | -7.71088 | -44.86819 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63e4c682-178e-37e9-a649-5a411ba8225b | -11.47715 | -50.74767 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 279c9028-56b1-3dba-b774-add32fab37b3 | -8.9859 | -45.78 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b63fca21-047c-3076-a0f3-502e6c378adf | -10.53766 | -49.78905 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3187402-25d0-3e89-90d7-3c9bdaf8d3b9 | -9.72424 | -46.8658 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b8ff8e3-b5ca-39ec-b85d-84487c647d99 | -9.72439 | -46.86459 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb0687d6-cd5c-3d73-9e52-27cccd824ffa | -12.95049 | -48.0341 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d987ba7-cc47-3820-84f1-7f2d042b8e30 | -7.69613 | -44.68432 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5e0381a-7853-30a6-b037-698e11f7a992 | -11.34297 | -50.82242 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ccdfc79-5a07-3cd3-a02e-881e029fbee8 | -9.63465 | -40.61938 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9b5cd2d6-cbff-350b-9429-b3d73e7f220b | -7.60213 | -49.87671 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bfeeae3-e15f-3c35-84fe-5e1ef95a106a | -12.73447 | -48.02859 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| cfb9f29d-63bf-35d9-be83-28c2f56fe57c | -12.72733 | -48.02753 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
