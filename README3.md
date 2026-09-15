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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4307001-2ef1-3f69-b5bd-5299f1dbe223 | -8.7918 | -45.888302 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d8086cc-5684-3b40-9512-0e4b070a5a58 | -17.3002 | -42.5047 | 2026-09-15 00:02:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8f0c82-c94e-3d71-bc84-096c1171bb04 | -2.675 | -57.511902 | 2026-09-15 00:02:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e21ed4d1-c6fe-388b-87d6-4e895bda4dba | -8.8018 | -50.476002 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0a22a5e-f0bb-3bbc-9b88-ce56a9e5e537 | -10.5736 | -47.720798 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df321a16-bb17-37b3-8526-347581851274 | -15.5878 | -48.804798 | 2026-09-15 00:02:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 59797c84-c454-3fd7-bc4f-991e2929329c | -4.5354 | -54.885601 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 505c8796-7cbc-37f4-9a9e-2761a209460e | -11.2234 | -43.420799 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8a98b88-7d79-367e-b51f-8a556ad33493 | -15.273 | -42.762699 | 2026-09-15 00:02:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5f843439-5b75-318b-b863-051e73d12c62 | -4.3528 | -47.764301 | 2026-09-15 00:02:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b99d8561-a0e9-3bd8-b440-0a96794782d1 | -4.2909 | -49.0886 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaf5140b-fefc-3c53-aad8-29588b9294f9 | -11.8796 | -43.797798 | 2026-09-15 00:02:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 233d9b04-9f48-37e2-879f-c44d2c9e1d0a | -5.4147 | -43.417301 | 2026-09-15 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 840c7e5e-dad5-3eae-a385-77aa760ded54 | -15.0514 | -48.538799 | 2026-09-15 00:02:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d52a2dde-2482-35a8-87fe-904b3624b93e | -5.417 | -43.427101 | 2026-09-15 00:02:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4ab1f62-f7bb-3252-bb09-54e2d20b9e63 | -8.8116 | -50.4739 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f28f1f10-ec8c-338f-bb04-b91a5e022710 | -3.2219 | -50.565102 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08ca7c90-7b3c-38d3-9c9a-f2a797c7d8de | -6.778 | -48.654701 | 2026-09-15 00:02:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d0d048a0-c2e2-3c1d-bfa3-3e835b90e96d | -5.7307 | -43.270901 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9de7fa0-b254-345e-896c-33efb209d2d4 | -4.5152 | -54.933102 | 2026-09-15 00:02:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d483591-0b9d-35b4-9dac-e301446ab940 | -7.6323 | -46.138802 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76f61d51-ba01-3391-91bb-404d7b7dd29c | -13.5096 | -44.149502 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3d673c1-26ea-3ba2-a489-d1d56a03d598 | -14.6796 | -47.990501 | 2026-09-15 00:02:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1e7e09bc-4bee-388d-900b-41e64cb036a6 | -7.378 | -49.5042 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae93f8f1-777d-333b-9ea6-38d8360773be | -17.3197 | -46.895 | 2026-09-15 00:02:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 136f7f82-8b8a-3d63-a829-018318ffe5a3 | -10.069 | -36.239201 | 2026-09-15 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84197804-c334-3793-a204-c121b63bb99c | -11.2293 | -43.4459 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 062aa4e7-ba46-30bf-95b5-80aa06559eee | -14.8668 | -49.923801 | 2026-09-15 00:02:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dfc339d9-2628-3a0d-bb0c-3270b17cca78 | -5.4132 | -48.491501 | 2026-09-15 00:02:00 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 739a9fcd-dd5c-3679-a77d-7206f74cce44 | -7.4675 | -46.139 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41838d3-aa6d-3416-81cf-403fc2686285 | -3.3932 | -50.733002 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6424a079-5732-375e-b6a3-f50886d47a6b | -9.8443 | -48.331902 | 2026-09-15 00:02:00 | METOP-B | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4759542-b3a7-34a0-9968-9b3422870653 | -4.3626 | -47.7621 | 2026-09-15 00:02:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97d2314b-a572-3a05-98f2-17524eec9b54 | -5.3264 | -47.877399 | 2026-09-15 00:02:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32095fba-4bca-3dda-bb29-13267e341a7e | -13.0736 | -48.588799 | 2026-09-15 00:02:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eec3c86e-29b3-3179-a8ed-cf51278e4a68 | -5.3248 | -47.870602 | 2026-09-15 00:02:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51146f93-e3bb-372f-a49e-eae9f84ac6d5 | -8.3636 | -49.032001 | 2026-09-15 00:02:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60cdc298-7973-3252-99f0-d3d2990ae9fa | -10.6598 | -54.092999 | 2026-09-15 00:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7921ff1-f6fe-39fc-beb4-585c7d73214b | -2.8893 | -50.413101 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d695cf-3441-3330-b00e-3eebfa0d3343 | -13.6103 | -48.2677 | 2026-09-15 00:02:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95cc9cf5-ab4d-387e-819c-64b368567de3 | -18.956699 | -47.275101 | 2026-09-15 00:02:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 46c60bc7-0711-375c-8ac9-25ac53cde188 | -6.048 | -46.334301 | 2026-09-15 00:02:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08e4734b-ec6c-3d60-9d60-50bd40a47d01 | -4.6543 | -42.065899 | 2026-09-15 00:02:00 | METOP-B | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 27a6103e-2a91-32e7-a2d7-0583a41e9697 | -9.3616 | -50.075901 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa18c14b-425d-3b42-baeb-b56f80674b9e | -7.6109 | -47.2714 | 2026-09-15 00:02:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f30c2d9-1f5a-3986-832a-f1e02cc0da51 | -5.5485 | -43.417 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 920cd4c5-5a59-3823-a1f3-68913c41ca3e | -6.3329 | -44.127201 | 2026-09-15 00:02:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4282391-d5f8-38ff-a538-fde3999b63d0 | -11.4972 | -45.771 | 2026-09-15 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 971a35a3-9593-3796-9b41-e6e85b843cfa | -3.0739 | -51.0532 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91d9fdf3-41b9-32d7-a0e8-0129200595d9 | -3.4779 | -54.6297 | 2026-09-15 00:02:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 571543f2-d24d-3b38-b465-0a693760e14d | -11.8114 | -46.573601 | 2026-09-15 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb0b0330-bcb0-3e81-a3b2-399b144aea37 | -13.8812 | -43.614201 | 2026-09-15 00:02:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ebe6cec-0954-3fbc-84e8-7098cfb758d6 | -6.7859 | -46.450699 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2307b5a7-7a7a-3e5a-b662-30787c3256b3 | -11.2391 | -43.443501 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9b3f14-24aa-30b2-917b-ed63cbf11b6f | -4.1352 | -40.828701 | 2026-09-15 00:02:00 | METOP-B | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 405c3afa-1237-381d-8944-e17ec7ffcba1 | -11.1119 | -40.467098 | 2026-09-15 00:02:00 | METOP-B | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 756f0f22-e2ab-3669-9cff-a00014403c73 | -4.5337 | -55.5821 | 2026-09-15 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f34d33-1d61-3884-beb1-98f7ef8ee0f0 | -9.4141 | -50.081699 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c18b5d1-466b-3fb4-9d73-202c0e44b159 | -9.4159 | -50.09 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23db4bc7-83f5-35b6-993f-1931b52ff044 | -3.2317 | -50.563 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52013d47-ada3-37cd-9620-a85c5544a592 | -11.1089 | -40.454601 | 2026-09-15 00:02:00 | METOP-B | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d9c39806-6e1e-3c68-8ab6-579ba2a041c3 | -6.9401 | -44.520599 | 2026-09-15 00:02:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44ffdb26-b44d-3a1c-8650-53cbba37c53d | -4.6611 | -42.051399 | 2026-09-15 00:02:00 | METOP-B | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f3403232-a70d-3338-9554-1eee268875ff | -5.4186 | -43.963902 | 2026-09-15 00:02:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16d31a85-fee2-386f-8b89-579918af3e34 | -14.6678 | -42.825802 | 2026-09-15 00:02:00 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 59fab540-a701-3b2e-8b56-c5322a738dc6 | -15.2487 | -40.976898 | 2026-09-15 00:02:00 | METOP-B | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24d522dc-cae3-3efb-8df8-52f684b0a3ba | -1.2292 | -54.1017 | 2026-09-15 00:02:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29b87a26-1734-3917-9c3a-f5382e6e2a2c | -10.7901 | -46.1996 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9269b7c-24f0-387d-8bfe-636420264186 | -4.1849 | -48.6633 | 2026-09-15 00:02:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc1f914f-1f01-368f-b9b2-6874ebee2c4d | -9.3634 | -50.179298 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19285f22-17ae-347b-b07f-ae2bf4239a11 | -15.2365 | -40.969299 | 2026-09-15 00:02:00 | METOP-B | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 78c96bdb-13ba-3ce9-94cf-94f5a5c8187c | -6.1614 | -52.766201 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e694e58c-feaf-3461-927a-9a2222c1efa3 | -13.5694 | -51.423801 | 2026-09-15 00:02:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d33ad3c-33cb-3c7c-b616-39c7a7f93187 | -6.1621 | -52.722301 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 401fe7e6-871f-345c-9a31-3bf82c991a31 | -5.7261 | -43.250999 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df970feb-5822-398b-8dfd-8182de656bc9 | -10.9915 | -48.313202 | 2026-09-15 00:02:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a77a9676-68fd-3d75-8f4b-50bd6c1afbff | -13.7713 | -48.784901 | 2026-09-15 00:02:00 | METOP-B | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 159ba959-3422-3d70-a50c-8a1e0e8c1a0d | -13.4318 | -43.813499 | 2026-09-15 00:02:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f3c2945-cbd0-3fc3-b248-ab114f97ba85 | -6.1613 | -55.6707 | 2026-09-15 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1456e547-1f51-3fd9-946c-21510864697f | -2.9122 | -50.3773 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e880a40-9447-394c-be2e-3150629a8cf4 | -15.5808 | -48.770901 | 2026-09-15 00:02:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e728d3a9-352a-3d9c-ac59-b96a2ed8d061 | -15.5906 | -48.768799 | 2026-09-15 00:02:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44ed1395-8cb0-30d8-81e4-6c0b54130eec | -15.5218 | -41.764099 | 2026-09-15 00:02:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de44b808-0c83-373c-8367-4c1626dfbd4b | -10.0309 | -52.069801 | 2026-09-15 00:02:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86d527bd-fb98-3140-83b5-15a623c8bff1 | -4.2638 | -46.5112 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f204f7c-9f9b-37aa-b07d-30250dc65cfa | -4.3642 | -47.768902 | 2026-09-15 00:02:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b849bfd0-a130-3fe1-a159-b7b49e6acc39 | -1.6871 | -55.868099 | 2026-09-15 00:02:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1547eae5-9a1b-3055-8773-efa95ec598ad | -5.3531 | -55.839802 | 2026-09-15 00:02:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47753193-9712-3461-8cb3-75c3a0f28264 | -3.9133 | -54.470001 | 2026-09-15 00:02:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33dc1d8f-9d3c-3c28-8113-6a3985d78cc3 | -7.0711 | -41.795601 | 2026-09-15 00:02:00 | METOP-B | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| def4fa83-5933-3c57-90c9-acda281f68df | -9.6856 | -54.794201 | 2026-09-15 00:02:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 440a1276-5175-3efc-b2c9-7fdb4ed4dc82 | -13.6385 | -47.872299 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5d15b52-4fe9-3083-93fe-a5d0876a0460 | -10.0755 | -36.264099 | 2026-09-15 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44a4e381-6aa0-321d-86ba-ecff3e724edb | -5.8942 | -49.954899 | 2026-09-15 00:02:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c279a18a-5d95-324a-afa7-582356a26571 | -6.8395 | -55.512699 | 2026-09-15 00:02:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f924825-7072-3771-b422-23f6f61fb3a8 | -8.8 | -50.467602 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb2abdc4-4aca-3263-96e9-a4058ed70d43 | -14.7651 | -42.9324 | 2026-09-15 00:02:00 | METOP-B | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3fea6512-4a9b-32da-9f16-0cdd534553c0 | -6.3375 | -45.527699 | 2026-09-15 00:02:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e60daaa-aa50-3c86-9f58-3f2443f67af6 | -15.2462 | -40.966702 | 2026-09-15 00:02:00 | METOP-B | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 207a3d06-969c-322e-9cb6-c01e77586af2 | -2.7949 | -49.3979 | 2026-09-15 00:02:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
