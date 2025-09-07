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
| fd246440-74cd-30dc-956d-00ebaeed9916 | -8.11922 | -45.31387 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0824d2ba-068f-3bff-b179-8abb29a5e179 | -13.03726 | -48.06637 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 871ddc79-4b25-32af-ad70-e7c86c5eda15 | -11.31958 | -46.56937 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c7c18faa-8ac0-35e1-aa58-d33e090a0f93 | -6.17593 | -44.31586 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18a81476-2a24-3582-a64f-82a1e127b8a8 | -10.73686 | -44.35283 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abb73793-a5e2-3419-96fb-7cd4437e5895 | -6.23647 | -43.27538 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53961d81-27b5-302e-9f1b-8bf8781781ce | -8.11391 | -45.31779 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33e3a243-7821-3a7e-83df-53811a90f6a5 | -13.05492 | -48.05479 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3618ff39-1056-394c-92a4-ae84ea922944 | -6.96298 | -46.51592 | 2025-09-07 03:57:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d63af6b3-2d7e-36da-a495-a13599b98c97 | -11.40773 | -43.62809 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ab18247-013c-3426-a37e-259120105151 | -7.63307 | -46.75776 | 2025-09-07 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83ae223f-a492-3f19-99c7-123e7743b8ee | -8.51685 | -41.19345 | 2025-09-07 03:57:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 09e2de70-6c6e-3091-8365-2b207a983934 | -8.43618 | -47.30583 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1be9772-4f36-3cc9-bc54-3ff891990b09 | -6.22812 | -43.57387 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b766a99-75e9-3c03-a345-a62fb1a301e5 | -6.34191 | -43.79699 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 238b784f-ffb9-3f2d-8eef-d3d923c668e6 | -6.91949 | -45.20075 | 2025-09-07 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1800c05f-f37f-3c99-86f0-b5f92d5062f2 | -6.19869 | -43.37461 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65779055-61b2-3994-b9e7-e5e24ccf6587 | -11.29628 | -46.54018 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a57373a2-35c6-3165-b83d-4287fbd3fb7f | -11.3593 | -45.57828 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f44b69ea-4972-3c55-8584-7aa6b105f788 | -7.67496 | -50.30233 | 2025-09-07 03:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d2c5e23-677b-3a8d-ac8d-9b60ea286c4b | -12.80452 | -48.01852 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2b755290-76cd-3bf3-bf4c-afe4b9ec62e4 | -10.79956 | -47.72076 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b749b040-e07f-32c8-8c42-3f733c1f05c9 | -7.68031 | -50.30854 | 2025-09-07 03:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2548f82e-32b9-3efe-9f82-6f57b71328fd | -11.90181 | -46.64605 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f750aaff-54b4-36f3-bad7-3a173520d823 | -6.19496 | -43.3781 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad8d7364-7e19-33df-b172-f8e88cbdffe8 | -6.53908 | -44.82235 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cb7f8fde-3255-3a84-90b8-bd8b550cbc74 | -10.16041 | -46.22258 | 2025-09-07 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d022f6d-be38-343c-882a-1a18cb4d5735 | -11.59232 | -47.168 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4c3bf256-e5c0-3ff3-a49f-a5def828e74f | -8.2944 | -45.38837 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41947b42-0e57-348b-8af2-b20f8c5f482b | -11.15334 | -48.39409 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99145aa6-b3f9-3561-8f53-ffb65195b881 | -11.31098 | -46.53805 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 148e82cc-a26a-3970-a2a8-920edbd0f780 | -7.19824 | -44.72913 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91566e2b-849e-3be7-b883-a4f3acb1eaef | -11.83685 | -47.56364 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc3c0273-8fad-3421-b4bb-23d1e41b8aef | -10.15603 | -48.74378 | 2025-09-07 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb264ff1-125d-3cd0-9ee8-4f4de14e06ce | -11.40638 | -43.61304 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4f43040-2fdc-3950-a1a0-1f081724e1be | -7.33848 | -48.51148 | 2025-09-07 03:57:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63b9ac9c-d5f6-3ebb-a83c-42a9d7f95f02 | -10.72199 | -48.59585 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4a04eda-d99a-3a0d-bf05-f6fe0b714311 | -11.83198 | -47.56258 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3a919e4-7fb2-340e-8c22-60ae2500b0ca | -7.59566 | -44.69267 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfec8e9e-b8e0-33d7-93f0-cbb55006c305 | -11.56929 | -47.75252 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67790b0b-d7a6-330e-a0e2-dc2b82b52d50 | -12.92469 | -48.03514 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bcc5116-e0e6-39d9-833b-782c42d743df | -13.01883 | -48.08173 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2eb9bf1-19c3-3ae1-bc0c-451c48d57d51 | -6.1993 | -43.37107 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8579974d-c503-33fe-810d-8455b81e17a9 | -10.7855 | -47.74033 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15ea1f09-b716-3deb-9a72-2f1b5ed5a32d | -11.5834 | -47.73183 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b1654b9-108b-3bfb-907f-71e8c86a1c95 | -7.25069 | -41.88821 | 2025-09-07 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b29efae9-4d4f-366a-b93b-1662dda2c3c6 | -13.05056 | -48.07733 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2168ddb-e636-3b37-bd6f-142ec3f1818c | -10.60226 | -44.33522 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 890738e4-0b4e-318e-a824-b55650970d88 | -13.02428 | -48.05133 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d492fe2-6e3a-3ac2-9d87-592967449383 | -11.59486 | -37.84669 | 2025-09-07 03:57:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b78c7321-6860-380b-bec2-2da2502b0655 | -6.88171 | -45.58721 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10cd3880-5eb7-3907-9bfd-417dbee95397 | -8.9391 | -48.65626 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0adf09b-7249-3270-8fb9-19981e2c9723 | -6.88467 | -45.59806 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b2adcfc-d407-3173-8195-b622f3c73438 | -6.21172 | -44.39469 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c9b5ffa-48fe-3f3a-914c-b202683f04f9 | -8.35371 | -48.26844 | 2025-09-07 03:57:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e49b5214-99fe-3635-8039-996e2fd4b918 | -8.44778 | -45.02503 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48fa4e74-b904-3fce-988b-8eb5514907ed | -8.93762 | -48.65505 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e24ebc28-a777-3764-8b44-b1dd96a684c9 | -8.4999 | -45.05915 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521adf5e-eacb-3438-92ec-bfe555d84bac | -5.94714 | -46.16594 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11958e28-3991-35c3-8e9f-2c983b396f51 | -10.6097 | -44.34029 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f6503def-f604-3591-97d8-eb9f41c41fb7 | -10.58879 | -48.47004 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d9db625-04eb-3f22-86d7-07d7bcdbe0c6 | -11.58892 | -47.16632 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed25c5be-c20b-3931-8636-04582b80aedf | -10.57973 | -48.47128 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f155905-62df-3b4c-98c0-30afcab38d0c | -14.04059 | -41.9887 | 2025-09-07 03:57:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| edd9901a-d445-3708-b261-abacc606bf83 | -7.81828 | -45.12933 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed6e8da0-cce8-3d9e-9d16-928181b0d5e2 | -12.93916 | -48.03984 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01ee9db1-13ea-3b98-b40c-17f63be43f82 | -9.77845 | -46.89627 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37fface2-0de0-346d-869a-4fdc034f49d9 | -7.19753 | -44.73327 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 78a6f2cb-605f-3eca-bc00-48024caccd97 | -8.14838 | -44.85594 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 171dc8b0-0b07-3252-9f75-894f8a55fb2b | -11.28657 | -41.99794 | 2025-09-07 03:57:00 | NPP-375D | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 23e0a0d8-9f6f-3f47-86e9-fa1d814cafd2 | -7.0169 | -44.95504 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45244c23-9e51-33d6-8d15-3887018bd002 | -12.85169 | -47.98721 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01d104ac-5e31-31ad-a2fd-48510230003b | -11.32047 | -46.56453 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cd812738-3e07-3266-b689-6c74c5d87838 | -11.38867 | -43.55638 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ff09c52-2e60-3bc4-9c0d-a5866690e56c | -6.60174 | -43.97374 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1540c6b2-a256-3e17-a65d-a9ed95c4edd7 | -11.81021 | -48.23568 | 2025-09-07 03:57:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16c7ed20-2520-3c53-be07-d1572d325a22 | -7.62846 | -46.55284 | 2025-09-07 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c76845b7-d6cf-31d7-a291-8d07f5f3610b | -8.49669 | -45.10852 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 220bd21e-1513-3637-a5ad-311eca9fc786 | -6.27146 | -43.49113 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbd6dea2-642f-3f89-98dd-cb57860a432e | -8.48361 | -45.17577 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d27619f9-fab3-3c4d-be94-56752cfefa12 | -5.8683 | -46.054 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a989a9fa-87ed-35a7-9e54-4847bb30d9fe | -11.3865 | -43.54631 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1e3616e-ae78-30cf-bd53-2d92ed511e4e | -11.40174 | -43.61708 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb1c9b93-3286-3456-9890-292c364ec557 | -8.08081 | -45.48277 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 285ca8e8-e1bd-368a-a873-ab78dfa40b44 | -12.80948 | -48.01947 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85d99b32-2fc6-3a47-b9e3-9e1ca0c3a28b | -7.63339 | -46.55368 | 2025-09-07 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5db43295-3791-39b3-b58d-44a4f6be692b | -8.91478 | -45.81347 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de1a67ff-e610-36f9-bd6d-021939bb84a3 | -6.34313 | -43.79309 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87773a8b-60f2-3d75-9b09-fcce86286f5a | -6.22476 | -43.29532 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c81308e-aa94-3f23-812c-07b466021012 | -7.01392 | -44.94542 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eccf1540-902c-39fe-bca6-71bdcc2dd068 | -5.94123 | -46.17084 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68918f0f-2794-3a18-941c-d0a7f1a02b35 | -7.83496 | -44.92636 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c03c817-407b-307c-9852-612879d54508 | -12.89445 | -48.005 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5f20b49-904b-3768-bc89-b918ba6116a7 | -6.19737 | -43.58021 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72299803-a004-3d88-8f8e-c395cf9ba7d3 | -7.3441 | -44.31462 | 2025-09-07 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04679505-f0f5-3f89-9792-5ad75b78acff | -12.81557 | -48.01458 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8c04e15-4163-3044-a8bb-f65b8d5b6da1 | -7.7183 | -44.71604 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfd29bfc-5c5e-3a16-9d76-822e6c48d189 | -6.30161 | -51.4109 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ee5d78b3-17f4-3730-a865-366b164a25a6 | -10.34944 | -46.45153 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 97d2dbd6-6349-3b10-bc39-228fef6891fc | -7.01604 | -44.97078 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README27.md)
