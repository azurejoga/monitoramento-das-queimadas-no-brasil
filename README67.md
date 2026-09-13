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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afbb12c5-181d-353f-8afa-1e0b2f65fc8e | -6.1046 | -55.6367 | 2026-09-13 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 57c26024-8413-3b8f-9daa-55e27ab6a8ac | -5.2723 | -56.0483 | 2026-09-13 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 95b843a0-76c9-31a4-ab79-058e4fb4566e | -3.5893 | -59.0773 | 2026-09-13 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e9605067-8398-3460-a486-0468146f2fa1 | -2.7149 | -57.5886 | 2026-09-13 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4e656e0e-5bae-36b3-a9bd-1541a98e006e | -9.376 | -50.1352 | 2026-09-13 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| b44a9d2a-04c1-3a73-a941-d4f66ab2f256 | -3.8096 | -58.8994 | 2026-09-13 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b4da32a7-3a06-35cd-b91a-10486103fbc6 | -9.3852 | -49.3847 | 2026-09-13 15:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 86c06fff-4916-3bc5-885e-781a175ee986 | -10.2929 | -45.2932 | 2026-09-13 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 7b227889-4d5a-3481-b599-6f96311f6654 | -1.3007 | -49.1464 | 2026-09-13 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f5dd7ac1-e289-3aa0-8008-b10d35348f46 | -10.2926 | -45.3161 | 2026-09-13 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| e48fcc23-78d1-3f63-bded-6e336bc116ca | -10.1639 | -50.3787 | 2026-09-13 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 287fab26-b66f-3b25-9d5f-fe38a62afb0c | -2.7149 | -57.608 | 2026-09-13 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ffcba0d8-7bba-309c-8f35-0073a8c81577 | -7.0352 | -44.6396 | 2026-09-13 15:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5b32c63d-630c-3e5c-a814-574e31672612 | -3.6077 | -59.0577 | 2026-09-13 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ce861c2d-2d26-3486-8328-6856e77149f8 | -8.4292 | -46.0271 | 2026-09-13 15:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1632b725-ea13-3bf1-8b21-34946c892191 | -8.0934 | -54.8488 | 2026-09-13 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7a9a2b21-5ad9-3166-b3b0-b37038e8212c | -11.9911 | -48.6576 | 2026-09-13 15:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c97dab66-e3de-32a0-a88c-53a78b54f44e | -3.6076 | -59.0769 | 2026-09-13 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 214.4 |
| 04767d07-37fc-31b2-8c08-42d5cb5670a0 | -13.4507 | -48.48 | 2026-09-13 15:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| ec84aa57-f085-3fee-95a0-b9ad2b41625f | -3.1697 | -58.6437 | 2026-09-13 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| cc4c9300-2678-3315-ab0f-3fb54ef5498c | -7.5397 | -44.8905 | 2026-09-13 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3656f700-a6ef-328c-8adf-4fdf28e32eaa | -3.8461 | -58.9178 | 2026-09-13 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 32d61e82-be37-36bd-baf3-91076a566daf | -10.8223 | -50.5879 | 2026-09-13 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0ec04884-14f3-36d6-b9d3-643fd0d44e20 | -8.6383 | -47.3875 | 2026-09-13 15:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| dccc8deb-57dc-33ce-acd5-924552b4213c | -8.2785 | -47.6198 | 2026-09-13 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 48cde0c7-bb56-3821-87ee-cf270a194c5e | -8.5417 | -54.6985 | 2026-09-13 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5237717c-bf33-30e1-ba4c-bfb102408f17 | -6.3198 | -59.9572 | 2026-09-13 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c6e7eb00-36ed-34bb-b768-335b60eaca05 | -11.383 | -43.9614 | 2026-09-13 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 7d0ed6c5-9179-3d0f-bc07-8902645e56fc | -8.2203 | -55.2427 | 2026-09-13 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| aaade4e6-4cc6-3423-9710-86ff27bc60c4 | -2.6602 | -57.5313 | 2026-09-13 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 05b7d412-f3d4-37e5-82a2-694f14902ac4 | -13.3946 | -57.0444 | 2026-09-13 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 02c3bcc8-86e0-37c3-9b3e-f9055436f43a | -8.4299 | -47.5177 | 2026-09-13 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| f5d3d51b-f1a0-37ce-93b1-03d6a6f60d54 | -11.354 | -46.7874 | 2026-09-13 15:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 41d878e3-634d-3c02-8e65-7a1cc3b170f5 | -10.7018 | -54.1458 | 2026-09-13 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| ff6ff1c1-6157-3f21-acb0-ebea136edafa | -8.5415 | -54.7187 | 2026-09-13 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| fc5c1caf-d906-3d29-bce6-106b632dc2f8 | -9.7038 | -54.3507 | 2026-09-13 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 983e9826-bb79-3bb0-b9d4-d8e47c3b9505 | -9.6941 | -46.0251 | 2026-09-13 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 323284a6-b91e-3075-9116-4a7c1c6a7537 | -12.6824 | -54.6968 | 2026-09-13 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6b1523e1-29bf-3714-b1f4-2196af80df02 | -6.863 | -55.5801 | 2026-09-13 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c46bf0a2-dd29-34f1-90bf-168e3c0e42bc | -7.5394 | -44.9133 | 2026-09-13 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c6876d2f-6332-3fc9-b622-3b3d86f50b6a | -3.4058 | -59.2347 | 2026-09-13 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3088e37f-3918-36c7-9b89-1f013c09066e | -8.2956 | -51.2003 | 2026-09-13 15:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f732273b-8e0e-31bc-a429-61d622b4f1dd | -4.1223 | -54.0158 | 2026-09-13 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6735fb15-a9f0-3c5c-9fa1-115567b261b0 | -10.8028 | -50.6326 | 2026-09-13 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 83bca4b9-7546-397e-835e-a5a50c933cd2 | -6.6334 | -45.4018 | 2026-09-13 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 53f0340d-ae22-340a-b4f2-dac197b696b9 | -15.9184 | -42.5472 | 2026-09-13 15:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 216.1 |
| a2b1cca9-030a-34c9-9f22-cd9ea05ce032 | -2.6602 | -57.5119 | 2026-09-13 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 69d1c7b3-63bf-3b73-ba33-4d7fb71057c8 | -9.3849 | -49.4062 | 2026-09-13 15:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| c381021e-f332-3944-a0fd-34b5d4064ac6 | -8.5229 | -54.72 | 2026-09-13 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6c89a29f-91bb-368e-9aff-3eedb4d9ea5b | -10.5854 | -51.3541 | 2026-09-13 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| f1570f29-ab64-3582-aec4-fa5736418aee | -8.1124 | -54.8073 | 2026-09-13 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1a77cde0-2905-3d13-9a4c-57c4735b5b73 | -13.299 | -51.7288 | 2026-09-13 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a1d7b61f-b7f3-3a4e-b904-05026f6fd831 | -6.8632 | -55.5601 | 2026-09-13 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6b83e749-4fa5-3ba0-959a-9acb25f594cc | -9.376 | -50.1352 | 2026-09-13 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 72303682-d477-359b-ad22-2c1d5719045d | -12.0468 | -49.956 | 2026-09-13 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e9521a6d-fe87-34fa-9476-90bd08cd7918 | -13.3758 | -51.7193 | 2026-09-13 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.9 |
| f0a8d353-d4b7-3da9-9e82-0cc2638f29e5 | -6.8567 | -47.4328 | 2026-09-13 15:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 87dd7f38-714c-3dcb-bb28-07f8d95ecdc9 | -3.5893 | -59.0773 | 2026-09-13 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 224.5 |
| b4184e8e-3614-3749-8a83-02cd2b88a2a9 | -2.7149 | -57.5886 | 2026-09-13 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2e32d159-8fed-3994-bbcd-e37ccd0e1d09 | -8.7772 | -49.955 | 2026-09-13 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 18e74971-6b05-36e1-9f74-d1d9460eee9a | -3.6076 | -59.0769 | 2026-09-13 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 296.2 |
| 329abe79-31c0-32af-9466-f23fcbac784a | -13.3055 | -51.3235 | 2026-09-13 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.3 |
| c6f3998a-b324-3ca4-a29a-43ba6cce21bb | -9.7038 | -54.3507 | 2026-09-13 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| de1b9140-f0ac-345a-9b81-fc220a9fdbaf | -4.1223 | -54.0158 | 2026-09-13 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 1dc1eee7-1c2a-3b61-8dae-7fa4aaebd15b | -8.0748 | -54.8499 | 2026-09-13 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 209d23d9-6c1a-3474-8844-6c3b71bcc24a | -10.8028 | -50.6326 | 2026-09-13 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| da05ef38-4e61-35fe-b961-2b0d1fd716a5 | -2.6602 | -57.5313 | 2026-09-13 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 4374dce6-89a0-39db-af2c-5c5b048bba63 | -10.7018 | -54.1458 | 2026-09-13 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 3b4e7acd-3889-3fa0-844f-af123b3af29f | -10.6829 | -54.1475 | 2026-09-13 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 305.1 |
| f6cf0d18-692f-3d3d-a93a-a4d8a8a438d0 | -10.6335 | -50.5651 | 2026-09-13 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 10c34725-aa2a-38f1-9024-8f7df4cd5bda | -8.2956 | -51.2003 | 2026-09-13 15:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9c92b774-f3e7-30de-ba31-5ad794261fac | -10.5481 | -51.3156 | 2026-09-13 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 0f89f91d-027d-3682-a218-78e9030832f7 | -13.3761 | -51.698 | 2026-09-13 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 245f2794-3818-305a-99f2-5087afc0741b | -2.6785 | -57.5115 | 2026-09-13 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 41a4799c-1b3e-3e3d-99bd-2236ba97d7b0 | -8.5417 | -54.6985 | 2026-09-13 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d72e8df4-f41d-31c8-b9a1-525d486b9641 | -12.6636 | -54.6782 | 2026-09-13 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6cf9a087-22ee-3fa0-8755-7c10f9d1735c | -11.0434 | -49.6851 | 2026-09-13 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| be5b50c6-ab8d-3830-bc63-646f024a6dd9 | -9.4137 | -50.1317 | 2026-09-13 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ceb2768a-997c-3831-aeed-8d42697489e9 | -11.0433 | -47.1633 | 2026-09-13 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d399c9bc-1497-3d8b-9b02-468adde1732b | -6.0256 | -59.9293 | 2026-09-13 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2ff2e7b0-450f-3856-be74-4c0d7080c961 | -15.9184 | -42.5472 | 2026-09-13 15:10:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 160.4 |
| af44f25f-e92a-319a-8a4e-490cadac91cb | -6.863 | -55.5801 | 2026-09-13 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 0f3db2e7-7092-3143-9180-4618ee179534 | -6.8629 | -55.6 | 2026-09-13 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ca9c2b5c-3038-38d0-92e6-ebe6cffd39a9 | -10.5478 | -51.3367 | 2026-09-13 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 75cad314-607c-3acf-9d4a-13bf8ed16637 | -6.0312 | -52.7565 | 2026-09-13 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a3d00216-0a39-3944-b502-310b77be1795 | -3.6075 | -59.0961 | 2026-09-13 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 855170e3-5206-3959-b2a4-eeeab3d274f0 | -12.1094 | -47.2907 | 2026-09-13 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| bca16bee-2f8f-30c4-b647-0ba55cf11c97 | -8.2203 | -55.2427 | 2026-09-13 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0f1d9e47-0b6d-3582-853f-8ebce59a2fda | -3.4058 | -59.2538 | 2026-09-13 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c41680dd-b321-3289-be01-e402d0b6794b | -10.7532 | -46.2573 | 2026-09-13 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c28bf6de-79bf-30cd-9b17-9b94202c9a01 | -12.6824 | -54.6968 | 2026-09-13 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 2e84c25a-ac93-3fea-8168-e7af6728959b | -13.4507 | -48.48 | 2026-09-13 15:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 688bd96d-0f84-3b5e-8762-457ac59149e9 | -3.1697 | -58.6437 | 2026-09-13 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7576f789-a0af-3c30-a8d6-b436db1bd89f | -5.2723 | -56.0483 | 2026-09-13 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 10eb4614-6f50-3d7c-ad0a-bd1ce409eea0 | -9.3852 | -49.3847 | 2026-09-13 15:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3d520759-3171-3845-8708-ac733d52861c | -3.354 | -58.1961 | 2026-09-13 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| f3d59889-ee63-3517-8c49-20bc3d69e65c | -3.4416 | -59.5213 | 2026-09-13 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 898db529-eb14-3054-a8e1-46b0f2919c34 | -10.5854 | -51.3541 | 2026-09-13 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3a0c881d-cd02-39c8-98c0-93cb5a4c4797 | -9.6758 | -45.9821 | 2026-09-13 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b7147dce-2b8d-32f2-b46e-0c10a26c2e0a | -7.12 | -42.107 | 2026-09-13 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |


[Clique aqui para ver as próximas entradas](README68.md)
