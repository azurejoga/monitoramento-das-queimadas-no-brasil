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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27c48dd9-6844-3169-9d62-6726358cd663 | -13.67798 | -41.88903 | 2026-09-28 17:07:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 66ef53d5-efbe-3944-9334-61a370d962c8 | -17.3533 | -42.15021 | 2026-09-28 17:07:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 154d663d-6b86-350f-87bc-16b64f952ab2 | -12.68289 | -46.98047 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 41396117-b927-3837-88d7-b0a874bf7437 | -11.39481 | -43.43884 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 46874438-7087-37f4-a549-1bd08a2216d6 | -14.35641 | -52.12054 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a3d26edb-caf0-304e-be5e-880ac303698c | -14.51612 | -52.48629 | 2026-09-28 17:07:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 67bccb2e-d083-3134-ac66-c84c2f94a35b | -13.6915 | -48.82265 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a59cb42f-2bac-3760-86dc-732f645d8363 | -12.91147 | -52.067 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3cb2f39e-96ff-3325-8494-d2cc5e599023 | -18.44132 | -43.95794 | 2026-09-28 17:07:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ff7a69fe-abd4-3d31-8ff4-f0f57cf0893f | -12.93835 | -46.64728 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e1aa8237-90d5-3b66-bea4-94222195cb38 | -14.11308 | -46.29675 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 21148c70-516c-3703-a6dd-98b0c3d7bfa8 | -11.29005 | -43.54913 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 4aa13a2e-060e-3577-a1fd-1cb1715dbe84 | -11.32197 | -42.21795 | 2026-09-28 17:07:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 61d50807-c8e7-39e0-9918-8bc0b3e3f34e | -15.16387 | -41.20682 | 2026-09-28 17:07:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| 9f63b4e1-8e68-3c02-ae06-ae41378cc577 | -11.89839 | -47.00512 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 48b9102a-b96e-35a2-9417-3979cadc8866 | -15.64584 | -40.43078 | 2026-09-28 17:07:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bc155749-1746-3f46-bdbb-380ec5a356c6 | -13.17064 | -48.55075 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 71b91537-aab8-3d5f-a03b-b9a72c9f6a83 | -15.16789 | -46.1686 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fec5307b-cb20-3fc4-8560-f8bb2bd4349b | -12.69 | -47.36392 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8a2ed1a1-a956-38c4-945f-15f65ce5baa0 | -15.74275 | -46.02934 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d5435c19-c628-32f0-b46b-bdd14be52764 | -13.4813 | -48.60312 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7c5c82c7-ebc6-3b5e-9eb4-fba390ac8f7e | -12.74876 | -50.68356 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 068351bb-1ab2-3c77-bbed-799c166195b0 | -14.44546 | -40.75055 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 70043f08-b300-3aa6-880f-ccb59f2a5190 | -18.12259 | -44.39009 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1b71d2b6-a918-340e-9d12-d1e477872781 | -17.21004 | -44.81264 | 2026-09-28 17:07:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6d1284d9-8595-3571-b0b2-15bbe65f9abd | -14.29195 | -41.57708 | 2026-09-28 17:07:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b5ccc58e-5d57-3eb0-93b9-850f988903c4 | -12.72922 | -50.67809 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 52b072d5-8f81-33b1-bbde-95ea94861ae0 | -11.71093 | -44.54951 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0cce8d63-ca38-3ea5-83ac-3907cc62d238 | -12.62973 | -50.71219 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 95eaffe3-b392-3345-862f-60e6ceb1a2ff | -24.65834 | -49.4586 | 2026-09-28 17:07:00 | NOAA-21 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4a90f360-89d6-3d66-950a-201c57fb3a5a | -12.98723 | -44.73392 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6574498c-e1e4-3867-bccb-1677ceaf24ed | -11.38383 | -43.41368 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b90e2e93-e786-3515-bf2d-82967a2d57ff | -15.85297 | -41.2712 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| caed8310-a511-3b3f-991c-9c63dd5a26d8 | -15.2176 | -46.18223 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 89c4c5db-5176-3db6-8eee-6facf98b239b | -16.26417 | -41.31757 | 2026-09-28 17:07:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| c66f03df-a8cb-3d29-8e70-9fda29fd7303 | -15.15411 | -43.61712 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.7 |
| dd96bee8-edf4-3ebb-a3a8-2335850daa5f | -12.98786 | -44.73462 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dacd8aea-d206-35d4-8af3-3405ac17bb1b | -18.74727 | -48.23466 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3426961e-6a30-389e-a78e-3dee5a05a9e7 | -12.61409 | -47.31596 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ca536077-e1a7-3bb5-b042-5f15d0808bf9 | -14.19951 | -44.94252 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 18de4cd4-dddb-3ee7-9235-a4240b7b7b80 | -16.34851 | -42.56668 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d202ea03-57c2-36b0-b972-85c3a4c2b6aa | -17.17661 | -51.73846 | 2026-09-28 17:07:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f81609db-bc4c-3507-afd3-26bb232ef180 | -12.79421 | -50.59299 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2265bbd0-aad0-3884-adae-50350d42cc8e | -11.60815 | -44.13383 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| fb03d975-cf5f-3375-a429-0c3c17f5ef0a | -14.48907 | -45.24148 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| eceee703-0001-3fc1-86ed-db13f5726c66 | -16.30749 | -43.13293 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 38b380c7-8f9c-3933-a597-b1610b73de9b | -13.56406 | -46.37228 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0cbed13b-4d18-3a8a-b90c-c2133e697c2f | -16.42118 | -43.29429 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c915fc37-e2f7-3eb6-9f43-7845fd4797b6 | -13.87417 | -42.13177 | 2026-09-28 17:07:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 76481edf-8233-3f87-87b4-bf553de13b91 | -12.62218 | -42.75869 | 2026-09-28 17:07:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 32.7 |
| aff5e173-471c-3593-9437-fd4514f56a18 | -14.80371 | -42.83448 | 2026-09-28 17:07:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 03132439-dc0f-3b20-86c7-100574c7928a | -16.38049 | -42.95925 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0a597726-2ada-3a1a-91f9-7491fe873486 | -11.68029 | -44.53692 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 280afe76-d691-37b4-8fe4-c4d935bedcef | -15.36533 | -52.80591 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9742b0f-9491-33df-9203-4cffb81f47d8 | -11.90145 | -47.02656 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 16d3685a-ccc1-301e-8b27-1a6ad5e270c9 | -15.50149 | -42.8825 | 2026-09-28 17:07:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34017a38-22d8-349a-a3a0-fc3ee888649c | -14.96517 | -41.06244 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5a3d81f0-4dc3-3283-b6a8-0dca359e6c93 | -13.44704 | -48.59801 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c0f7c02c-a381-3858-bcdc-1bfc1edd3ae8 | -17.68451 | -44.75446 | 2026-09-28 17:07:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 195e3c28-49ac-3097-89d4-afde7936de78 | -12.67197 | -45.04138 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69ee7d8d-16a9-366c-9b8a-03e9f6ce790e | -12.60963 | -47.3168 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 592fe42b-6ae7-3a01-a1af-01cd64b66a97 | -18.87352 | -46.92601 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3f4b186-0bd9-3df0-b352-3ea5bcfa9fea | -12.71601 | -46.98137 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 02a6ce5b-12da-318c-a9d6-836d6651818f | -14.97328 | -41.53592 | 2026-09-28 17:07:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 60e4e81b-0433-3be4-b752-77974372e0a6 | -11.35421 | -43.35602 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| b8bf9f1c-01b8-320f-a950-c4a49852184e | -15.09971 | -53.89234 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 692e731b-0c20-33b0-b856-632e4864f358 | -18.87655 | -46.66634 | 2026-09-28 17:07:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5de54dc0-abc3-38e6-a433-c2857a356eef | -11.63495 | -43.50035 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 006ec5ae-7a37-322a-b052-0ccc0099c715 | -15.15557 | -43.62423 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 0c73bc8e-40a6-38af-976a-c4f2d9c15155 | -12.75239 | -50.68292 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 23408471-2f6e-30e7-851e-3db9b06c4600 | -14.08909 | -46.32285 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| cb51f22c-cac1-3b4b-9fd9-49b346e98ae0 | -17.81584 | -44.44011 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 52117487-4a47-323f-ab8e-ceb2e7c79a48 | -11.35696 | -43.40119 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f6f180c0-96dc-39fb-a204-3c0b6d4b2ada | -15.55966 | -47.91685 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 82e503d1-c406-313c-93b8-ab0235372416 | -14.64504 | -52.12141 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fd6ee2f6-361d-3d91-b93a-dbf1df946853 | -14.50999 | -48.30607 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d4953827-2546-3abb-bdf8-d6e4654dc3f3 | -11.77049 | -41.15379 | 2026-09-28 17:07:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 81a3c537-4b2f-3f62-8e1f-00324e23ff67 | -12.69728 | -47.35323 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 465c7b40-651c-3f46-b2c6-e6bb36a061ec | -14.31823 | -44.81527 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d3283ae7-7c1e-3ca3-80e2-05e98ed49c52 | -15.39701 | -47.91943 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9ee04a5d-a905-37cf-be72-04e19fcf04ad | -13.58413 | -40.01098 | 2026-09-28 17:07:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 51.8 |
| 302b9cc2-cdd8-31d2-a54c-85796f32ab39 | -12.75296 | -47.28831 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3d74e536-0f93-32e2-8d39-79ce8ac93611 | -14.32005 | -44.82453 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2fef9076-1a4d-3845-a1bb-b7f51a5e8ce4 | -18.92849 | -47.19853 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9f678b3e-ec01-34b4-bec8-d94f4cf13939 | -13.48191 | -48.60669 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fefa1c47-4c12-3631-b246-069109af47d7 | -17.32455 | -53.9674 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2a69ac4c-3efc-3f16-b45b-03916df32c3c | -15.06622 | -54.60056 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 58b3e480-2280-305e-9d7c-db12b615428a | -18.11184 | -44.3872 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 674fe3ab-61c4-33d4-86e5-a6a53def02af | -11.67588 | -43.52671 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fa62e2bd-b912-39fa-938e-79384696793c | -15.4658 | -46.1413 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 13db5f58-4a85-3062-8aa8-09e6f8dfed24 | -13.45048 | -48.59379 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0e383300-da87-3c8d-aeea-5727bc6a2df6 | -13.07093 | -48.50712 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| caa44369-4599-3e95-a663-dabf6ce444f9 | -12.97812 | -44.79813 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 432d35b6-7490-35c0-a9da-7c45b24d3dd8 | -15.19377 | -46.15411 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 94c24dcd-5448-395f-b00a-b73067535674 | -19.13158 | -46.6793 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 015a5c14-bbf9-3fcd-b17c-ba1dfadf67e6 | -15.94345 | -54.96724 | 2026-09-28 17:07:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e304a2e9-63ea-372a-ba0c-168dad232815 | -15.45735 | -41.44818 | 2026-09-28 17:07:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 23c03cc9-56cf-3a1d-bfcc-30faec70b0b5 | -12.67953 | -47.35671 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| c6c54230-be35-3055-a863-a6cf1cc37dc2 | -15.08068 | -54.60581 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 63cffdbd-0fd9-3394-87df-5d29f5dbe809 | -14.54382 | -40.73824 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |


[Clique aqui para ver as próximas entradas](README140.md)
