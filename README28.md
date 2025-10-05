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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 444a9077-e0fd-3139-a669-7d104bc6d9ed | -13.07382 | -47.90586 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50e83bfd-6bca-34b0-a05c-d8114fda720d | -12.69652 | -45.85341 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2d726453-65c0-3be4-afbe-d2b255611e8d | -11.69059 | -47.49376 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71464fda-d37d-3323-9dcf-0e7759bdc298 | -9.05121 | -47.02298 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40ff6895-bb45-39f7-afaa-acdd7523f2d2 | -8.57826 | -46.32075 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 83214589-26e1-3da3-90e5-ab4c338324fa | -13.00043 | -44.00191 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1b1c221-7adb-3488-86cb-360ea89d4cf5 | -13.3035 | -47.79921 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e39e7d57-da53-3460-a43c-19fa9916c40b | -11.01195 | -46.69163 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a842f0e0-0cec-36fc-b91c-ef1d03a7eff8 | -8.54631 | -46.27597 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 148b5c2b-5b5c-344e-a4f2-76630e5fdbe4 | -11.49045 | -46.78683 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70423f95-011e-3de7-bfd8-2948124d63fa | -11.90884 | -46.24136 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 821a2c25-693c-3df7-bf61-5b953308811c | -8.5669 | -46.35805 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfe9dce1-c0a3-3c00-b7a6-30cf4b1325fb | -11.91775 | -46.24519 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2c13e24-f94f-3eda-b560-da41d710a78f | -7.80857 | -42.54694 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cd4e7dac-d417-335b-9bdc-75de9396d40c | -8.58532 | -46.32203 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 61f76931-ac30-3452-a945-99b09386b52f | -8.53701 | -46.32338 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7cae5759-d5ba-3fed-a860-3958922a8579 | -13.30551 | -47.77684 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15a7ce46-455e-3fa1-bb30-41a341b5b78f | -7.79009 | -44.13622 | 2025-10-05 03:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c22eba1d-3c71-3121-917b-08a0166799d3 | -13.26665 | -47.61548 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 510602dc-0c7f-3691-8902-c869743ac628 | -10.94085 | -47.08868 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| c24da655-4569-3ee8-8107-f4a5bb26b50e | -13.27422 | -47.18364 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce02d64a-bc4b-3fe8-89c2-67f98869e130 | -11.80311 | -46.82373 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70a17a75-1db4-3ba8-b769-9eaa77216be7 | -13.85998 | -43.99089 | 2025-10-05 03:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3466ab81-ea2c-39d4-9ced-a342bc5a9242 | -8.55006 | -46.31527 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e59bc88d-4bb1-356d-910f-e419d8e0ec66 | -13.34235 | -48.06607 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50d01717-c3e6-3f1f-9c80-87a3bc906de3 | -13.723 | -48.08469 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b42b940d-fc97-339d-9f20-39858cb9ac8d | -11.91657 | -46.25084 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cde3a98b-53e8-3833-805c-e75cf27882fa | -11.83025 | -45.06266 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2c821d4-4c51-3d76-b133-63940adcdd6d | -8.55197 | -46.28438 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1fc1d9a-4b91-311a-a6ba-929b9fcceb7e | -7.80115 | -42.56299 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f18ed3dd-c3be-3781-bd56-1ca127de3d1b | -9.29558 | -46.00491 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1d10c3da-8dba-357e-974d-5d469d2e859c | -8.6392 | -44.90659 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 159ba725-5118-3c61-9f48-bad5d4b4058a | -9.27271 | -46.01239 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28d0fe74-8bfd-32bd-8ac6-4f8c8cc659dd | -11.6235 | -45.02396 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad872bac-4e62-33d3-95c2-31575afb3a45 | -7.70519 | -42.56442 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea388d67-b185-37df-9f5e-0e8a92ef8c3f | -10.19587 | -45.5397 | 2025-10-05 03:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e88c1617-945b-36c7-bba9-938a71c7bbcc | -13.1207 | -43.84327 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8e43350f-fb66-315e-bd92-74826b7f4e53 | -9.04538 | -47.01429 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d8f98e3-33b8-30ef-a769-d375e69d8baf | -11.81442 | -45.07726 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c57208-a251-3f40-9bd0-f8fc63de0dc9 | -8.57487 | -46.31697 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 95c82787-fdfd-3436-91cb-c251c5534b84 | -7.79393 | -46.02067 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a9a6cba-1845-34c6-a017-11fdbd35c923 | -11.819 | -45.05423 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 880b4de9-6168-3ce7-8f42-05cfe986de85 | -11.89399 | -44.9911 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9399f35-18d7-3c8b-86ea-36f1ba35d3af | -13.58906 | -48.16109 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fca20acf-74ba-3640-94d8-25ee6873b2d2 | -8.63062 | -44.91187 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d304af40-d27a-3448-8009-f4065c698859 | -7.51127 | -41.27761 | 2025-10-05 03:34:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 632eb195-9d99-3a66-87d1-d973cc01161c | -10.20645 | -40.55139 | 2025-10-05 03:34:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3742f707-89c1-367c-a7cf-46a9d6af035b | -7.6172 | -45.46964 | 2025-10-05 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 002adcfe-e5a4-338b-98df-9f5560dfbbf6 | -13.48514 | -47.23181 | 2025-10-05 03:34:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66a0b8d2-7179-3f1f-a481-f6c0d7823335 | -7.75595 | -46.32693 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 827497dc-1c3a-3151-8d68-43835049557e | -13.81913 | -43.17288 | 2025-10-05 03:34:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c6445c9d-c803-3097-97ea-311d4354aa25 | -7.78082 | -42.60305 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52f82962-6239-3219-bf57-e45de821743e | -12.45986 | -45.51337 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14672f62-d215-3ae5-8880-e5d62fd0833f | -7.68862 | -42.58997 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 38c1006c-2fa9-3cb3-a188-d5468c9dee75 | -10.94738 | -47.07538 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 65809e0d-8198-309c-a054-e0f381604a4d | -8.12282 | -44.10349 | 2025-10-05 03:34:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d2be10d-c3ae-3c50-8e03-18ee04fd35d2 | -12.8887 | -47.31745 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c75952d5-2558-3ff5-b4d2-56b9d4ea5baf | -12.4501 | -44.73986 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41d5863a-3e96-3792-8876-2832c4eeef7c | -12.46094 | -45.50825 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cf43e2d-a700-356d-a8b5-34f3b0eb96a0 | -11.83374 | -45.09721 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b56ac3a-48fa-39fe-b172-c53f2abaaecd | -11.4902 | -46.7926 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c47557-481c-3549-ba38-6303f0561ac1 | -7.1536 | -46.09514 | 2025-10-05 03:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec720b4b-f38e-3dae-89d4-022ea3708847 | -9.27264 | -46.01233 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dbc40aa8-78d9-3adc-8bc2-dbeb82d470b8 | -11.82674 | -45.08037 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b7beac57-e11e-38fe-b5b7-115ddab2bc10 | -9.29652 | -45.99931 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 727eefb8-a19e-307b-b74d-15df2714fe1a | -10.93884 | -47.08101 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9f64a9e3-19c0-3ae0-a7c9-b0755dcfae3c | -13.34307 | -47.19629 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7de7b201-f106-3299-9f52-89b63554a74f | -13.35478 | -47.58001 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08f5be3d-6bb5-3687-8d17-4e933943378e | -13.35115 | -48.06004 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bd9c99d8-7a1a-3b2b-862f-ab33398568b6 | -8.6317 | -44.9106 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7289f377-5f18-3df6-8682-752c43fc2801 | -11.71348 | -45.35274 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81fe40ed-b349-33e5-bb72-385671a7be32 | -13.28577 | -47.5949 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 18cca185-1316-3f2c-a291-a05ee5db2ee6 | -12.45569 | -45.52532 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2e9bba5-e38a-3b4b-b81e-f9b0dcc353ad | -11.88384 | -44.97766 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0b1c9b8-06e2-3271-93f1-0a12700c1d4b | -13.25469 | -47.81863 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 230de43d-557c-39f1-8832-1bd329b3b107 | -9.2945 | -46.01026 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 079fb639-7637-399a-975f-4dc090fcf2c0 | -7.24446 | -44.88523 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efc362ad-2d76-3939-aff9-fcb50662f2fc | -11.83363 | -45.07827 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a5c24c2-eb59-3738-be84-5fa5c6eda995 | -9.12492 | -44.39082 | 2025-10-05 03:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be9a8b3e-fd60-341f-93e7-4e645ce61dca | -11.67651 | -47.48973 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23b4c4d8-f958-3edf-a544-3a992fcc3ad3 | -11.5005 | -44.99189 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9181b3e-d259-3671-bd39-84a198b1160c | -13.30015 | -47.80183 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fba79f5-b9d0-3d6f-93ed-294fd094ff7f | -9.29891 | -45.98697 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ded438b6-eac3-35f2-bb98-a8dc09612d87 | -13.11185 | -47.83446 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bc2a2e9-42a8-396b-b8c9-dd802df15983 | -12.69761 | -45.84815 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9aad7ba-110c-3d4e-a9a7-82ed620c0184 | -7.64766 | -45.42104 | 2025-10-05 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9d799af-efe4-32ed-97f2-9145a3b15328 | -8.56725 | -46.37563 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b274331-ad4f-3a4a-b5bb-f2bbe1e1b4cf | -11.93427 | -46.43366 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60869321-8164-31df-a727-4f7c47b38cf5 | -8.59292 | -46.29925 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e9c55147-f804-38e5-83c5-eec833c0d9a5 | -13.52135 | -47.29545 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab67db4f-6f1a-3aa3-af2c-6e88ce71bd6f | -9.65187 | -45.85135 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f66a002-a319-335e-a4e3-1c4e4f37378d | -6.98179 | -44.21457 | 2025-10-05 03:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e642f319-525e-3f91-a42f-4ffb2d2abb19 | -11.82845 | -45.07175 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0ec6dfd-c308-39cd-8964-c90646d5691e | -8.53891 | -46.33416 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a69bc2a0-2ff9-3f69-b1db-a6f47d3c59f1 | -9.90925 | -45.95439 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 61913748-0a61-3efa-85a0-4bc2547dd2c1 | -7.31279 | -45.98635 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de808887-def1-3124-bfc3-a0834dd5517b | -10.94175 | -47.06697 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 73358a4f-2791-3fb9-8128-3385380e655b | -13.28724 | -47.58809 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8d08ca96-ac73-3aa3-8ea5-66387f456555 | -13.15557 | -47.9531 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a897b757-dffc-3917-bb3a-f3b42dd221c4 | -7.16149 | -44.99677 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README29.md)
