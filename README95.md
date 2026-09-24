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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62cadec6-390e-366b-85da-ff70c2aad14e | -6.8841 | -46.5471 | 2026-09-24 14:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 922c707f-2239-3050-9cc3-555f8b3e4a46 | -13.168 | -51.5324 | 2026-09-24 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| cb12b7e0-3088-3b36-800c-882fc9d38b67 | -9.2563 | -46.2323 | 2026-09-24 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 98933cbc-8de2-3c8e-91a3-d2cf80779d2d | -8.18 | -64.0416 | 2026-09-24 14:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| dec85e4f-1b4c-39c1-81d9-7a12e5439763 | -9.0158 | -60.5138 | 2026-09-24 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4c64fa39-3174-3cb6-a77b-6f32ed89a162 | -12.0096 | -52.4675 | 2026-09-24 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9a931903-0742-30bb-b2b3-fcaf26426720 | -7.894 | -45.1527 | 2026-09-24 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d12ed0e3-dd91-3386-9746-4b950f4966c2 | -13.8151 | -51.8553 | 2026-09-24 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f1a9fa7b-dfac-354b-b07f-880b7cfe2222 | -8.5803 | -44.5322 | 2026-09-24 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ff8510ae-ac2b-3ec6-aa85-fff58138f677 | -7.8787 | -44.8577 | 2026-09-24 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 82b647fb-f276-3edb-a5c1-488aefd3d25b | -3.4635 | -58.3096 | 2026-09-24 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| f48f0abc-9a9b-3105-93e3-f2ee481b6784 | -8.3761 | -47.3023 | 2026-09-24 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 1dae56bb-e536-3afa-9957-b3ae7ec1775c | -17.7756 | -46.6272 | 2026-09-24 14:20:00 | GOES-19 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9909b050-688e-3661-a837-c6707ff42d3e | -11.0991 | -54.0285 | 2026-09-24 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3440516e-a799-3dbf-aa44-30bcba25b64c | -3.046 | -46.9223 | 2026-09-24 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 07577091-e6de-3f9f-ace7-110a39cdb8ad | -9.0401 | -66.052 | 2026-09-24 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5ad13105-1ca2-3884-a4d4-1f88f6125275 | -9.0401 | -66.052 | 2026-09-24 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3c6e6d48-a0f0-34c9-83cd-2c41de6d06d7 | -7.468 | -44.5768 | 2026-09-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 173cf730-ce9b-37ee-b57e-7c7fe140aed5 | -5.5833 | -60.1924 | 2026-09-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a0f0d355-dc12-3721-8754-8a8ad8802fb6 | -6.1653 | -47.5052 | 2026-09-24 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0fb6ae2a-6359-305f-8b79-af6e2dca041e | -11.1183 | -54.0062 | 2026-09-24 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 42b05d1d-1e62-3631-8e45-76043545289d | -10.7115 | -60.7312 | 2026-09-24 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 258b014d-0e82-3a02-a551-da66048635e5 | -6.0462 | -53.2662 | 2026-09-24 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 81eb65fe-40bf-38c3-912c-472496b1593d | -3.5356 | -58.6939 | 2026-09-24 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 00df831a-6d93-3674-9ac5-32581ad6462b | -6.9871 | -47.4885 | 2026-09-24 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 40d502a9-2525-31ac-9956-5fbda9ee3b99 | -6.2759 | -47.6506 | 2026-09-24 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f8b962e7-aedb-3421-8481-c9c57fd1ab62 | -3.4791 | -59.1948 | 2026-09-24 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 44f1217e-b789-3d95-bfe9-bdba3f5932b7 | -7.4283 | -44.7639 | 2026-09-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6023c5db-d723-358c-b867-64819be82db4 | -6.4487 | -59.9526 | 2026-09-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 2d00d841-192a-34ed-9576-f7dea8b37a3e | -5.1948 | -42.9805 | 2026-09-24 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 71.3 |
| af632526-57f9-39e0-9d22-b53f49f0418b | -9.043 | -65.4175 | 2026-09-24 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3c070b75-2222-3188-aa02-5c5bc1c229c6 | -6.1839 | -47.5039 | 2026-09-24 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 6ec99c85-a8f4-36a7-bc17-b284682e40c4 | -6.9223 | -42.9323 | 2026-09-24 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| a16e30ab-9414-3be5-904d-fae36a06a9e7 | -7.4092 | -44.7885 | 2026-09-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d596e251-1ebd-3fb4-af15-bea1ac43939b | -6.9683 | -47.4899 | 2026-09-24 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 267f7275-ab63-38c2-a29b-84801250979a | -8.3761 | -47.3023 | 2026-09-24 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 83ce79f2-9c80-3be6-942d-49568195f3c9 | -13.7993 | -54.0617 | 2026-09-24 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 597a811b-6119-3c16-af1e-52087e2e169c | -11.7165 | -54.5449 | 2026-09-24 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f7ae1e71-6e7d-3c1f-9d7e-fa71e4bc4120 | -8.754 | -44.2589 | 2026-09-24 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 21729f50-858d-3963-83b4-4b41cb436cce | -10.8569 | -57.1568 | 2026-09-24 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5e57d753-ebd3-3130-9bc7-ee01edc98d28 | -7.7444 | -46.7184 | 2026-09-24 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5168da33-ecb7-368b-a7f2-6561ca09675a | -8.3581 | -47.2378 | 2026-09-24 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ce8d249e-f28e-3bd6-ba81-3d0f3e9677ca | 2.1697 | -55.8169 | 2026-09-24 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e801484c-6d58-37a0-b4d4-7c3461c7b3d2 | -9.1392 | -58.9207 | 2026-09-24 14:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2239d32e-6d65-3340-9907-ed0bf52c7929 | -6.9228 | -42.8852 | 2026-09-24 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 42a79bcb-2106-3a96-92d4-3e7c6145248f | -7.8789 | -44.8348 | 2026-09-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 33ef5bac-7240-3197-8aed-3c8d41bee6af | -5.6016 | -60.1919 | 2026-09-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 232.1 |
| 7624732a-10d2-37a7-ba30-6dfe3a534b1f | -18.5218 | -50.3411 | 2026-09-24 14:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 340be117-a69f-3ce1-92a4-d3d115c3b419 | -5.195 | -42.9571 | 2026-09-24 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 35feb61c-b437-3ad9-805d-41fdc59d06c8 | -14.7017 | -48.7559 | 2026-09-24 14:30:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 59549695-6fce-3026-930b-7abd3e8d2ee4 | -7.4095 | -44.7656 | 2026-09-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8f9e2681-93e8-3223-bea5-43200cc321c4 | -3.4635 | -58.3096 | 2026-09-24 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 18f75b8d-3f9d-3c37-9809-8fcd47152318 | -3.3309 | -59.8673 | 2026-09-24 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 964ecc80-1804-346b-862b-be0d3e8103e8 | -17.6569 | -49.8992 | 2026-09-24 14:30:00 | GOES-19 | VICENTINÓPOLIS | GOIÁS | Brasil | 5222054 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 91946d2a-531f-313f-9b0e-077fa6c0c8a7 | -13.8151 | -51.8553 | 2026-09-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5c4b9d3a-0b96-39d1-b866-bd74e7b862db | -13.168 | -51.5324 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| f3064312-f25c-3b89-badc-0e8f11e05cc6 | -13.2791 | -51.7737 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b08b9724-5045-3985-88c6-12a4f64b59b4 | -6.9225 | -42.9088 | 2026-09-24 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| f8988a7e-03d9-3664-b3c3-7c6d3c4b5a68 | -3.5467 | -43.4735 | 2026-09-24 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8dff58b2-3eb7-329c-ac21-3d0bf10a6c69 | -10.8567 | -57.1767 | 2026-09-24 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2a2a00c1-3160-3f3b-a1f3-0218392c108b | -7.1203 | -42.083 | 2026-09-24 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 605ca3e0-8330-3429-b92f-46f48e0170db | -11.9906 | -52.4695 | 2026-09-24 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 7f598fc9-0ce8-3501-949b-9869866ecfc3 | -3.331 | -59.8483 | 2026-09-24 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ac1f4180-9fef-3465-ab7a-91e734711344 | -6.4303 | -59.9532 | 2026-09-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| faf68849-6315-325e-8750-f7fefb528286 | -12.0096 | -52.4675 | 2026-09-24 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 640dfe0f-5a05-39c8-b999-07c9ef191ea3 | -13.3171 | -51.7902 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 23cb365c-4cc4-3a3e-b203-253e1e0159e8 | -13.2979 | -51.7926 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 98d02d9c-4fbb-3e29-a884-beb750338292 | -13.2983 | -51.7713 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| b8c3aa31-507a-30f7-b294-8dbe0b3a4651 | -5.6567 | -60.2092 | 2026-09-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9b92a49b-339d-3ff4-a01b-e09e0160d0aa | -7.7441 | -46.7406 | 2026-09-24 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6a2c05c1-d750-3483-b616-a80a21b7d7b3 | -8.0486 | -44.8178 | 2026-09-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 12fe9533-cc18-3129-beb4-a0a6f5b56e78 | -7.8787 | -44.8577 | 2026-09-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3e26db27-be55-3b9d-a068-fd98b09fdcfa | -8.58 | -44.5552 | 2026-09-24 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2667d0d9-ac0b-39bc-858b-32411872fefa | -6.2026 | -47.5026 | 2026-09-24 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a1ec4ab5-d0b9-3599-9efa-a80e2dcc2b1f | -6.4302 | -59.9724 | 2026-09-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 12617171-f4ea-3844-a1dd-b0cf27d53ac5 | -13.2057 | -51.5703 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 36368b20-5019-3bcb-83f4-e9f8fa7d9728 | -7.7629 | -46.7389 | 2026-09-24 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 6ef265c8-c489-34fd-8f15-de6513c4062e | -13.8154 | -51.834 | 2026-09-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| da13d697-7400-38fa-b533-53bcf3b7c8f7 | -13.2599 | -51.7761 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9065cead-133c-33a1-9039-2a54de24d2bc | -13.1872 | -51.53 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7859f3a0-bee3-368d-b39b-c3491cf136cb | -9.0158 | -60.5138 | 2026-09-24 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 42bf2794-680f-38dd-98ca-4ebb594ebb30 | -8.746 | -44.8586 | 2026-09-24 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 56e3b930-aead-356d-b10a-6b927938d7b8 | -13.2249 | -51.5679 | 2026-09-24 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e3d59ceb-3091-32e8-b9f0-5b4971640b0a | -9.1392 | -58.9207 | 2026-09-24 14:40:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 81dc3d24-9217-3e8d-90da-8ac71042320e | -11.9906 | -52.4695 | 2026-09-24 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d998a055-3961-3e6b-a350-590095df0428 | -11.1183 | -54.0062 | 2026-09-24 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c2968d4d-bfb6-3b3e-b382-ab1f5c125787 | -7.3495 | -54.9538 | 2026-09-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 276150a4-faab-3ae7-bb1f-197feff43dc9 | -5.6567 | -60.2092 | 2026-09-24 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 534f9700-d8e1-3609-8fe2-fdfa72e9a55c | -6.8985 | -41.6976 | 2026-09-24 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 4bb1348b-de49-35cf-8d18-5693ec1ec100 | -7.6309 | -46.7951 | 2026-09-24 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 35f2663a-e0b0-3905-b725-a3f72ddffde7 | -6.9416 | -42.8834 | 2026-09-24 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| f8ecc4f1-7469-3a7e-aced-c94952818af5 | -18.5218 | -50.3411 | 2026-09-24 14:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 05a0685a-1d94-31b2-a488-dfdc7bc149e5 | -7.6115 | -45.1799 | 2026-09-24 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| fad879eb-c191-350e-a00a-87ab11997e8d | -7.7444 | -46.7184 | 2026-09-24 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4c130c11-ab24-3215-a68a-9070a2baabae | -6.9871 | -47.4885 | 2026-09-24 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8439bf4f-d8ae-3dda-9cd3-087c8bfd7873 | -5.5833 | -60.1924 | 2026-09-24 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d37fdcb4-c042-3981-9f13-7628bb995f9c | -10.8567 | -57.1767 | 2026-09-24 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 83d98b85-a75e-33a4-a16c-798c69ba6ac4 | -7.1088 | -43.0792 | 2026-09-24 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 3943d67f-39e7-343d-9a62-0f60c7523e49 | -6.9683 | -47.4899 | 2026-09-24 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| dd96f02f-a3a5-327f-884e-d81340f80745 | -7.4283 | -44.7639 | 2026-09-24 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |


[Clique aqui para ver as próximas entradas](README96.md)
